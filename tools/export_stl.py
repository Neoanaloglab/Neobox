#!/usr/bin/env python3
"""Regenerate the nine published STL files from cad/neobox.blend.

This is the committed form of the pipeline that produced the files under stl/.
The printable parts are modelled as overlapping shells (interpenetrating by
0.2-0.5 mm on purpose); this script unions each part into one watertight solid,
welds the boolean slivers away, and exports it in assembly world space.

Run headless from the repository root:

    /Applications/Blender.app/Contents/MacOS/Blender --background cad/neobox.blend \
        --python tools/export_stl.py

    (any Blender 4.x/5.x binary works; the file itself needs 3.0+)

Options after a lone "--" are passed to this script:

    ... --python tools/export_stl.py -- --out /tmp/somewhere

exports into a different directory instead of the repository's stl/ tree.
Always finish with:  python3 tools/verify_stl.py
"""
import argparse
import os
import sys

import bpy

# STL file -> (subdirectory, [source objects]).  Everything else in the .blend
# is a mock-up and must never be exported — see docs/design.md section 11.
MAPPING = {
    "main-body.stl": ("white-pla", [
        "main-body_floor", "main-body_wall-left",
        "main-body_wall-right", "main-body_wall-rear",
    ]),
    "cover-stage.stl": ("white-pla", ["cover-stage"]),
    "film-holder-135-base.stl": ("black-pla", ["film-holder-135-base"]),
    "film-holder-135-lid.stl": ("black-pla", ["film-holder-135-lid"]),
    "film-holder-120-base.stl": ("black-pla", ["film-holder-120-base"]),
    "film-holder-120-lid.stl": ("black-pla", ["film-holder-120-lid"]),
    "pressure-window-135.stl": ("black-pla", ["pressure-window-135"]),
    "pressure-window-120.stl": ("black-pla", ["pressure-window-120"]),
    "mask-6x6.stl": ("black-pla", ["mask-6x6"]),
}

WELD = 0.02          # weld distance for boolean slivers, mm
PLANAR = 0.0175      # limited-dissolve angle, rad (about 1 degree)


def select_only(objs):
    bpy.ops.object.select_all(action="DESELECT")
    for o in objs:
        o.select_set(True)
    bpy.context.view_layer.objects.active = objs[0]


def union_into(target, operand):
    mod = target.modifiers.new("u", "BOOLEAN")
    mod.object = operand
    mod.operation = "UNION"
    mod.solver = "EXACT"
    bpy.context.view_layer.objects.active = target
    bpy.ops.object.modifier_apply(modifier=mod.name)
    bpy.data.objects.remove(operand, do_unlink=True)


def export_one(filename, sources, out_dir):
    missing = [n for n in sources if n not in bpy.data.objects]
    if missing:
        raise RuntimeError(f"{filename}: missing source object(s) {missing}")

    # 1. work on copies — the scene is never modified
    dups = []
    for name in sources:
        src = bpy.data.objects[name]
        dup = src.copy()
        dup.data = src.data.copy()
        bpy.context.collection.objects.link(dup)
        dups.append(dup)
    select_only(dups)
    if len(dups) > 1:
        bpy.ops.object.join()

    # 2. split into shells, union them into one solid
    bpy.ops.object.mode_set(mode="EDIT")
    bpy.ops.mesh.select_all(action="SELECT")
    bpy.ops.mesh.separate(type="LOOSE")
    bpy.ops.object.mode_set(mode="OBJECT")
    shells = sorted(bpy.context.selected_objects,
                    key=lambda o: -len(o.data.vertices))
    solid = shells[0]
    for shell in shells[1:]:
        union_into(solid, shell)

    # 3. weld the slivers EXACT boolean leaves behind, re-triangulate cleanly
    select_only([solid])
    bpy.ops.object.mode_set(mode="EDIT")
    bpy.ops.mesh.select_all(action="SELECT")
    bpy.ops.mesh.remove_doubles(threshold=WELD)
    bpy.ops.mesh.dissolve_degenerate(threshold=WELD)
    bpy.ops.mesh.dissolve_limited(angle_limit=PLANAR)
    bpy.ops.mesh.quads_convert_to_tris()
    bpy.ops.mesh.normals_make_consistent(inside=False)
    bpy.ops.object.mode_set(mode="OBJECT")

    # 4. watertightness gate before anything is written
    edge_count = {}
    for poly in solid.data.polygons:
        verts = list(poly.vertices)
        for i in range(len(verts)):
            key = tuple(sorted((verts[i], verts[(i + 1) % len(verts)])))
            edge_count[key] = edge_count.get(key, 0) + 1
    bad = sum(1 for c in edge_count.values() if c != 2)
    if bad:
        bpy.data.objects.remove(solid, do_unlink=True)
        raise RuntimeError(f"{filename}: {bad} non-manifold edge(s) after union")

    # 5. export in assembly world space, then drop the temporary solid
    sub, _ = os.path.splitext(filename)
    out_path = os.path.join(out_dir, MAPPING[filename][0], filename)
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    select_only([solid])
    bpy.ops.wm.stl_export(filepath=out_path, export_selected_objects=True)
    tris = len(solid.data.polygons)
    bpy.data.objects.remove(solid, do_unlink=True)
    return out_path, tris


def main():
    argv = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else []
    parser = argparse.ArgumentParser()
    repo = os.path.dirname(os.path.dirname(os.path.abspath(bpy.data.filepath)))
    parser.add_argument("--out", default=os.path.join(repo, "stl"),
                        help="output directory (default: <repo>/stl)")
    args = parser.parse_args(argv)

    failures = 0
    for filename, (_, sources) in MAPPING.items():
        try:
            path, tris = export_one(filename, sources, args.out)
            print(f"ok    {filename}  ({len(sources)} object(s) -> {tris} triangles)")
        except RuntimeError as err:
            print(f"FAIL  {err}")
            failures += 1

    # Naming convention as a gate: every mesh object is either a mock-up
    # (mock_ prefix, never exported) or a source listed above.  A printed part
    # added to the scene and forgotten here would otherwise ship as nothing.
    listed = {name for _, sources in MAPPING.values() for name in sources}
    stray = sorted(o.name for o in bpy.data.objects
                   if o.type == "MESH"
                   and not o.name.startswith("mock_")
                   and o.name not in listed)
    if stray:
        print(f"FAIL  mesh object(s) neither exported nor named mock_*: {stray}")
        failures += 1

    print()
    if failures:
        print(f"{failures} failure(s): nothing under {args.out} should be trusted")
        sys.exit(1)
    print(f"{len(MAPPING)} files written under {args.out}. "
          f"Now run: python3 tools/verify_stl.py")


if __name__ == "__main__":
    main()
