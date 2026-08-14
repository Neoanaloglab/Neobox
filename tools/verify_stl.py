#!/usr/bin/env python3
"""Verify every exported NeoBox STL against the invariants the design depends on.

Run from the repository root:   python3 tools/verify_stl.py

Checks, per file:
  1. watertight        every edge shared by exactly two triangles
  2. layer grid        every horizontal face sits on a 0.2 mm multiple above the part's own base
  3. minimum step      no exposed horizontal step below 0.4 mm (two layers at 0.2)
  4. bounding box      matches the published dimensions
Exit status is non-zero if any check fails, so this can gate a commit.
"""
import collections
import pathlib
import struct
import sys

# published bounding boxes, sorted descending, in millimetres
EXPECTED = {
    "main-body.stl": (154.8, 124.8, 75.6),
    "cover-stage.stl": (154.8, 124.8, 10.0),
    "film-holder-135-base.stl": (120.0, 94.0, 5.0),
    "film-holder-135-lid.stl": (120.0, 94.0, 3.0),
    "film-holder-120-base.stl": (120.0, 94.0, 5.0),
    "film-holder-120-lid.stl": (120.0, 94.0, 3.0),
    "pressure-window-135.stl": (95.0, 64.0, 2.0),
    "pressure-window-120.stl": (95.0, 64.0, 2.0),
    "mask-6x6.stl": (94.0, 80.0, 1.0),
}
LAYER = 0.2
MIN_STEP = 0.4
MIN_FACE_AREA = 1.0  # mm^2 — ignore slivers when looking for exposed steps


def read(path):
    data = path.read_bytes()
    count = struct.unpack_from("<I", data, 80)[0]
    edges = collections.Counter()
    planes = collections.defaultdict(float)
    lo = [float("inf")] * 3
    hi = [float("-inf")] * 3
    for i in range(count):
        n = struct.unpack_from("<12f", data, 84 + i * 50)
        pts = (n[3:6], n[6:9], n[9:12])
        key = [tuple(round(c, 4) for c in p) for p in pts]
        for k in range(3):
            edges[tuple(sorted((key[k], key[(k + 1) % 3])))] += 1
        for p in pts:
            for axis in range(3):
                lo[axis] = min(lo[axis], p[axis])
                hi[axis] = max(hi[axis], p[axis])
        if abs(n[2]) > 0.999 and abs(pts[0][2] - pts[1][2]) < 1e-4 and abs(pts[1][2] - pts[2][2]) < 1e-4:
            (ax, ay, _), (bx, by, _), (cx, cy, _) = pts
            planes[round(pts[0][2], 3)] += abs((bx - ax) * (cy - ay) - (cx - ax) * (by - ay)) / 2
    return count, edges, planes, [round(hi[a] - lo[a], 2) for a in range(3)]


def check(path):
    problems = []
    count, edges, planes, dims = read(path)

    open_edges = sum(1 for c in edges.values() if c != 2)
    if open_edges:
        problems.append(f"{open_edges} non-manifold edge(s) — not a watertight solid")

    levels = sorted(z for z, area in planes.items() if area > MIN_FACE_AREA)
    if levels:
        base = levels[0]
        off_grid = [round(z - base, 3) for z in levels
                    if abs((z - base) / LAYER - round((z - base) / LAYER)) > 1e-3]
        if off_grid:
            problems.append(f"face(s) off the {LAYER} mm layer grid at +{off_grid}")
        steps = [round(levels[i + 1] - levels[i], 3) for i in range(len(levels) - 1)]
        thin = [s for s in steps if s < MIN_STEP - 1e-6]
        if thin:
            problems.append(f"exposed step(s) below {MIN_STEP} mm: {thin}")

    want = EXPECTED.get(path.name)
    if want and tuple(sorted(dims, reverse=True)) != want:
        problems.append(f"bounding box {sorted(dims, reverse=True)} != published {list(want)}")

    return problems, count, dims


def main():
    root = pathlib.Path(__file__).resolve().parent.parent / "stl"
    files = sorted(root.rglob("*.stl"))
    if not files:
        print(f"no STL files under {root}", file=sys.stderr)
        return 2
    failed = 0
    for path in files:
        problems, count, dims = check(path)
        if problems:
            failed += 1
            print(f"FAIL  {path.name}  ({count} triangles)")
            for p in problems:
                print(f"        {p}")
        else:
            print(f"ok    {path.name}  {dims}  {count} triangles")
    print()
    print(f"{len(files) - failed}/{len(files)} files pass" if failed else f"all {len(files)} files pass")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
