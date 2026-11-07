#!/usr/bin/env python3
"""Generate the NeoBox camera-tube parts for your lens from cad/neobox.blend.

The camera tube stands on the 135 holder lid, is held down by the lid's own eight magnets, and
carries a macro lens by its filter thread through a bought step-up ring, at the working distance
your magnification needs.  The camera never touches it, so the tube needs only four numbers that
describe the LENS:

    --ring 46-52       the step-up ring that screws into the lens: lens thread - larger thread (mm)
    --ring-od 54       outside diameter of that ring's body, measured (mm)
    --ring-h 4.0       height of that ring's body below its shoulder, measured (mm)
    --wd 96            working distance, lens front rim to the film, at the magnification you
                       scan at, measured (mm)

Parts (binary STL in assembly world space, every face on the 0.2 mm layer grid; print them top
face down, no supports):

    camera-tube-base.stl          the same for every lens: skirt around the lid, bearing ring,
                                  eight magnet pockets, the joint on top.  60 mm of working
                                  distance with nothing on it (--base-wd)
    lens-column-46-52-h36.stl     one per lens: the ring pocket on top of a riser, H = wd - base
    lens-carrier-46-52.stl        the same with no riser (H = 0): for wd equal to the base
    camera-tube-spacer-35.stl     optional riser under the column (--spacer), for a second
                                  magnification with the same lens
    camera-tube-coupon-socket.stl the turning joint on its own (--coupon): the base's socket and the
    camera-tube-coupon-spigot.stl column's spigot, about 10 g each, to prove the fit before the base

Run headless from the repository root (any Blender 4.x/5.x):

    /Applications/Blender.app/Contents/MacOS/Blender --background cad/neobox.blend \\
        --python tools/camera_tube.py -- --ring 46-52 --ring-od 54 --ring-h 4 --wd 96 --out out/

then  python3 tools/verify_stl.py out/*.stl

Inside a running Blender that has cad/neobox.blend open, exec() this file with a global ARGS
holding the same arguments as a list; the parts are then built in the open scene as well.
"""
import argparse
import math
import os
import sys
from collections import defaultdict

import bpy
import bmesh
from mathutils import Vector

LAYER = 0.2
PLA = 1.24e-3                      # g per mm3

# --- the box side, from cad/neobox.blend (checked against the lid object at run time) -----------
LID_TOP, FILM_PLANE = 87.0, 83.2   # world z, desk = 0
LID_W, LID_L = 94.0, 120.0
MAGNET_XY = [(sx * 41.0, sy * y) for sx in (1, -1) for sy in (1, -1) for y in (12.0, 42.0)]
MAGNET_SQ, MAGNET_DEPTH = 8.6, 2.2  # the lid's square pockets, Ø8 x 2 N35 magnets

# --- the tube ------------------------------------------------------------------------------------
WALL = 1.2
CLEARANCE = 0.4                    # per side, skirt around the lid
SKIRT = 3.4                        # skirt below the bearing ring
RING, RING_IN = 1.0, 3.0           # bearing ring on the lid: thickness, width inward from the skirt
CHAMFER = 3.0                      # 45-degree transition above the ring
NOTCH_W = 70.0                     # film pass-through notches in the end skirts
CORNER_R, ARC_SEGS = 0.4, 16
BOSS_FLOOR, BOSS_WALL = 0.6, 1.2   # magnet bosses under the chamfer
JOINT = dict(bore_d=84.0, collar_od=94.0, collar_h=4.4, spigot_od=83.6, spigot_h=4.0, flange_t=1.2)
LIP_T, RING_FIT = 1.2, 0.4         # lip under the ring pocket; diametral clearance of the pocket
MOUTH_CH = 0.6                     # 45-degree chamfer at the two bores that print on the bed (the base's socket,
                                   # the column's ring pocket): elephant foot would otherwise close their 0.2 fit
COUPON_X = -250.0                  # where the joint test pieces are parked
SEGS = 128
BASE_WD_MIN = 45.0                 # corner overhang reaches 45 degrees here


def g(z):
    """Snap to the layer grid."""
    return round(round(z / LAYER) * LAYER, 1)


# --- mesh helpers --------------------------------------------------------------------------------
def _mesh_obj(bm, name):
    if name in bpy.data.objects:
        bpy.data.objects.remove(bpy.data.objects[name], do_unlink=True)
    bm.normal_update()
    me = bpy.data.meshes.new(name); bm.to_mesh(me); bm.free()
    ob = bpy.data.objects.new(name, me); bpy.context.scene.collection.objects.link(ob)
    return ob


def _finish(ob, ref_name="film-holder-135-lid"):
    """Weld, fix normals, take the holder lid's material and collection."""
    bm = bmesh.new(); bm.from_mesh(ob.data)
    bmesh.ops.remove_doubles(bm, verts=bm.verts, dist=0.001)
    bmesh.ops.recalc_face_normals(bm, faces=bm.faces)
    bm.to_mesh(ob.data); bm.free()
    ref = bpy.data.objects.get(ref_name)
    if ref is not None:
        ob.data.materials.clear()
        for m in ref.data.materials:
            if m: ob.data.materials.append(m)
        for c in ref.users_collection:
            if ob.name not in c.objects: c.objects.link(ob)
        if ref.users_collection and ref.users_collection[0] != bpy.context.scene.collection \
                and ob.name in bpy.context.scene.collection.objects:
            bpy.context.scene.collection.objects.unlink(ob)
    return ob


def rrect(w, l, r, z, m=ARC_SEGS):
    """Rounded rectangle ring, m segments per corner; r = half size gives a circle."""
    a, b = w / 2, l / 2
    r = max(min(r, a, b), 0.2)
    pts = []
    for (sx, sy, th0) in ((1, 1, 0), (-1, 1, 90), (-1, -1, 180), (1, -1, 270)):
        cx, cy = sx * (a - r), sy * (b - r)
        for k in range(m + 1):
            th = math.radians(th0 + 90 * k / m)
            pts.append(Vector((cx + r * math.cos(th), cy + r * math.sin(th), z)))
    return pts


def loft(rings, name):
    bm = bmesh.new()
    vs = [[bm.verts.new(p) for p in r] for r in rings]
    n = len(vs[0])
    bm.faces.new(list(reversed(vs[0])))
    for a, b in zip(vs, vs[1:]):
        for i in range(n):
            bm.faces.new([a[i], a[(i + 1) % n], b[(i + 1) % n], b[i]])
    bm.faces.new(vs[-1])
    bmesh.ops.remove_doubles(bm, verts=bm.verts, dist=0.0001)
    bmesh.ops.recalc_face_normals(bm, faces=bm.faces)
    return _mesh_obj(bm, name)


def box(name, x0, x1, y0, y1, z0, z1):
    def ring(z):
        return [Vector((x0, y0, z)), Vector((x1, y0, z)), Vector((x1, y1, z)), Vector((x0, y1, z))]
    return loft([ring(z0), ring(z1)], name)


def prism_xz(name, pts_xz, y0, y1):
    """Prism from a closed polygon in the xz plane, extruded from y0 to y1."""
    bm = bmesh.new()
    a = [bm.verts.new((x, y0, z)) for (x, z) in pts_xz]
    b = [bm.verts.new((x, y1, z)) for (x, z) in pts_xz]
    bm.faces.new(a); bm.faces.new(list(reversed(b)))
    n = len(a)
    for i in range(n):
        j = (i + 1) % n
        bm.faces.new([a[j], a[i], b[i], b[j]])
    bmesh.ops.recalc_face_normals(bm, faces=bm.faces)
    return _mesh_obj(bm, name)


def lathe(profile, name, segs=SEGS):
    """Solid of revolution about z from a closed (r, z) polygon."""
    profile = list(profile)
    if not (profile[0][0] == 0 and profile[-1][0] == 0):   # a profile that starts and ends on the axis is already closed
        profile.append(profile[0])
    bm = bmesh.new()
    rings = []
    for (r, z) in profile:
        if r == 0:
            rings.append([bm.verts.new((0, 0, z))])
        else:
            rings.append([bm.verts.new((r * math.cos(2 * math.pi * k / segs), r * math.sin(2 * math.pi * k / segs), z))
                          for k in range(segs)])
    for a, b in zip(rings, rings[1:]):
        if len(a) == 1 and len(b) == 1:
            continue
        if len(a) == 1:
            for k in range(segs): bm.faces.new([a[0], b[k], b[(k + 1) % segs]])
        elif len(b) == 1:
            for k in range(segs): bm.faces.new([a[k], b[0], a[(k + 1) % segs]])
        else:
            for k in range(segs): bm.faces.new([a[k], a[(k + 1) % segs], b[(k + 1) % segs], b[k]])
    bmesh.ops.remove_doubles(bm, verts=bm.verts, dist=0.0001)
    bmesh.ops.recalc_face_normals(bm, faces=bm.faces)
    return _mesh_obj(bm, name)


def cylinder(name, r, z0, z1):
    return lathe([(0, z0), (r, z0), (r, z1), (0, z1)], name)


def boolean(target, cutter, op):
    mod = target.modifiers.new("b", "BOOLEAN")
    mod.operation = op; mod.solver = "EXACT"; mod.object = cutter
    bpy.context.view_layer.objects.active = target
    with bpy.context.temp_override(object=target, active_object=target, selected_objects=[target],
                                   selected_editable_objects=[target]):
        bpy.ops.object.modifier_apply(modifier=mod.name)
    bpy.data.objects.remove(cutter, do_unlink=True)


# --- parts ---------------------------------------------------------------------------------------
def build_base(base_wd=60.0, name="camera-tube-base"):
    """Frustum on the lid: skirt, bearing ring, magnet bosses, film notches, the joint on top."""
    assert base_wd >= BASE_WD_MIN, f"--base-wd below {BASE_WD_MIN}: the corner overhang exceeds 45 degrees"
    J = JOINT
    inner_w, inner_l = LID_W + 2 * CLEARANCE, LID_L + 2 * CLEARANCE
    outer_w, outer_l = inner_w + 2 * WALL, inner_l + 2 * WALL
    ring_w, ring_l = inner_w - 2 * RING_IN, inner_l - 2 * RING_IN
    lid = LID_TOP; z_bot = g(lid - SKIRT); z_ring_top = g(lid + RING); z_chamfer_top = g(z_ring_top + CHAMFER)
    z_shoulder = g(FILM_PLANE + base_wd); z_top = g(z_shoulder - J["flange_t"]); z_collar = g(z_top - J["collar_h"])
    ri, ro = CORNER_R, CORNER_R + WALL
    cod, cid, bore = J["collar_od"], J["collar_od"] - 2 * WALL, J["bore_d"]
    body = loft([rrect(outer_w, outer_l, ro, z_bot), rrect(outer_w, outer_l, ro, z_chamfer_top),
                 rrect(cod, cod, cod / 2, z_collar), rrect(cod, cod, cod / 2, z_top)], name)
    cavity = loft([rrect(inner_w, inner_l, ri, z_bot - 1), rrect(inner_w, inner_l, ri, lid),
                   rrect(ring_w, ring_l, ri, lid), rrect(ring_w, ring_l, ri, z_ring_top),
                   rrect(inner_w, inner_l, ri, z_chamfer_top), rrect(cid, cid, cid / 2, z_collar)], "_cut_cavity")
    boolean(body, cavity, "DIFFERENCE")
    boolean(body, lathe([(0, z_collar - 1), (bore / 2, z_collar - 1), (bore / 2, z_top - MOUTH_CH),
                         (bore / 2 + MOUTH_CH, z_top), (bore / 2 + MOUTH_CH, z_top + 1), (0, z_top + 1)],
                        "_cut_bore"), "DIFFERENCE")
    for sy, tag in ((1, "1"), (-1, "2")):
        y0, y1 = sorted((sy * (inner_l / 2 - 1), sy * (outer_l / 2 + 1)))
        boolean(body, box("_cut_notch" + tag, -NOTCH_W / 2, NOTCH_W / 2, y0, y1, z_bot - 1, lid), "DIFFERENCE")
    half = MAGNET_SQ / 2
    z_boss = g(lid + MAGNET_DEPTH + BOSS_FLOOR)
    for (px, py) in MAGNET_XY:                        # a block under the chamfer, wedge back at 45 degrees
        sx = 1 if px > 0 else -1
        x_in = abs(px) - half - BOSS_WALL
        x_out = inner_w / 2 + WALL / 2
        pts = [(sx * x_in, lid), (sx * x_out, lid), (sx * x_out, z_boss + (x_out - x_in)), (sx * x_in, z_boss)]
        if sx < 0: pts = list(reversed(pts))
        boolean(body, prism_xz(f"_add_boss{px:+.0f}{py:+.0f}", pts, py - half - BOSS_WALL, py + half + BOSS_WALL), "UNION")
    for (px, py) in MAGNET_XY:                        # the pocket, opening downward onto the lid's magnet
        boolean(body, box(f"_cut_pocket{px:+.0f}{py:+.0f}", px - half, px + half, py - half, py + half,
                          lid - 1, lid + MAGNET_DEPTH), "DIFFERENCE")
    _finish(body)
    h = z_collar - z_chamfer_top
    lean = tuple(round(math.degrees(math.atan2(d, h)), 1) for d in
                 ((outer_w - cod) / 2, (outer_l - cod) / 2, math.hypot(outer_w / 2, outer_l / 2) - cod / 2))
    return body, dict(name=name, base_wd=base_wd, foot=(outer_w, outer_l), z_bot=z_bot, z_collar=z_collar,
                      z_top=z_top, z_shoulder=z_shoulder, height=round(z_top - z_bot, 1), lean_deg=lean,
                      joint=(bore, cod, J["collar_h"]), magnets=(len(MAGNET_XY), MAGNET_SQ, MAGNET_DEPTH))


def build_column(L, H, z_rest, name=None):
    """Lens column (H >= 6.4) or carrier (H == 0): spigot + flange resting on a collar top at z_rest,
    the ring pocket and lip at the top.  shoulder = z_rest + flange_t + H."""
    J = JOINT
    pk, hole = (L["ring_od"] + RING_FIT) / 2, L["lip_hole_d"] / 2
    pw_o = pk + WALL
    pk_depth = math.floor(L["ring_h"] / LAYER + 1e-9) * LAYER         # on the grid; the ring stands proud by < 0.2
    assert pk_depth >= MOUTH_CH + LAYER, f"--ring-h {L['ring_h']}: too shallow a pocket for its {MOUTH_CH} mm mouth chamfer"
    sp_o, sp_i, fl, wi = J["spigot_od"] / 2, J["spigot_od"] / 2 - WALL, J["collar_od"] / 2, J["collar_od"] / 2 - WALL
    z_fl = g(z_rest); z_sp = g(z_fl - J["spigot_h"]); z_sh = g(z_rest + J["flange_t"] + H)
    z_pk = g(z_sh - pk_depth); z_lip = g(z_pk - LIP_T)
    rim_seat = "ring shoulder" if L["rim_od"] <= 2 * pk else "column top face"
    if H == 0:
        name = name or f"lens-carrier-{L['ring']}"
        assert pw_o < sp_i - 1.0, f"ring OD {L['ring_od']} too large for a carrier (max {2 * (sp_i - 1.0 - WALL) - RING_FIT:.1f}); use a column"
        assert L["retainer_od"] / 2 < sp_i - 0.2, "the clamp ring must pass the spigot bore"
        prof = [(hole, z_lip), (pw_o, z_lip), (pw_o, z_fl), (sp_i, z_fl), (sp_i, z_sp), (sp_o, z_sp), (sp_o, z_fl),
                (fl, z_fl), (fl, z_sh), (pk + MOUTH_CH, z_sh), (pk, z_sh - MOUTH_CH), (pk, z_pk), (hole, z_pk)]
    else:
        name = name or f"lens-column-{L['ring']}-h{H:g}"
        assert H >= 6.4, f"H = {H}: a column needs H >= 6.4; print the base at --base-wd {L['wd']:g} and use the carrier"
        assert pw_o < wi - 1.0, f"ring OD {L['ring_od']} too large (max {2 * (wi - 1.0 - WALL) - RING_FIT:.1f})"
        assert L["retainer_od"] / 2 < wi - 0.5, "the clamp ring must fit inside the column"
        z_plate = g(z_sh - J["flange_t"]); z_fun = g(z_fl + J["flange_t"] + (wi - sp_i))
        prof = [(sp_i, z_sp), (sp_o, z_sp), (sp_o, z_fl), (fl, z_fl), (fl, z_sh), (pk + MOUTH_CH, z_sh), (pk, z_sh - MOUTH_CH), (pk, z_pk),
                (hole, z_pk), (hole, z_lip), (pw_o, z_lip), (pw_o, z_plate), (wi, z_plate), (wi, z_fun),
                (sp_i, g(z_fl + J["flange_t"]))]
    col = lathe(prof, name)
    _finish(col)
    return col, dict(name=name, H=H, z_rest=z_rest, z_shoulder=z_sh, pocket=(round(2 * pk, 1), round(pk_depth, 1)),
                     lip=(LIP_T, L["lip_hole_d"]), rim_seat=rim_seat, z_bottom=min(z_sp, z_lip))


def build_spacer(length, z_rest, name=None):
    """Riser of effective length `length`: flange on the collar top at z_rest, the same joint on top."""
    J = JOINT
    name = name or f"camera-tube-spacer-{length:g}"
    sp_o, sp_i, fl, bore, wi = J["spigot_od"] / 2, J["spigot_od"] / 2 - WALL, J["collar_od"] / 2, J["bore_d"] / 2, J["collar_od"] / 2 - WALL
    fun_h = wi - sp_i
    assert length >= J["collar_h"] + fun_h + J["flange_t"] + 1.2, f"spacer shorter than {J['collar_h'] + fun_h + J['flange_t'] + 1.2:.1f}"
    z0 = g(z_rest); zt = g(z0 + length)
    prof = [(sp_i, g(z0 - J["spigot_h"])), (sp_o, g(z0 - J["spigot_h"])), (sp_o, z0), (fl, z0), (fl, zt), (bore, zt),
            (bore, g(zt - J["collar_h"])), (wi, g(zt - J["collar_h"])), (wi, g(z0 + J["flange_t"] + fun_h)),
            (sp_i, g(z0 + J["flange_t"]))]
    sp = lathe(prof, name)
    _finish(sp)
    return sp, dict(name=name, length=length, z_rest=z0, z_top=zt)


def build_coupon(z_rest):
    """The turning joint on its own, parked at x = COUPON_X, to prove the fit on a printer before a base is spent
    on it: the base's socket (collar top on the bed, as the base prints) and the column's flange, spigot and
    funnel (upper face on the bed, as the column prints)."""
    J = JOINT
    bore, fl, wi = J["bore_d"] / 2, J["collar_od"] / 2, J["collar_od"] / 2 - WALL
    sp_o, sp_i = J["spigot_od"] / 2, J["spigot_od"] / 2 - WALL
    z_top = g(z_rest); z_col = g(z_top - J["collar_h"]); z_bot = g(z_col - 2.4)
    sock = lathe([(bore + MOUTH_CH, z_top), (fl, z_top), (fl, z_bot), (wi, z_bot), (wi, z_col), (bore, z_col),
                  (bore, z_top - MOUTH_CH)], "camera-tube-coupon-socket")
    z_fl = g(z_rest); z_sp = g(z_fl - J["spigot_h"]); z_in = g(z_fl + J["flange_t"])
    z_fun = g(z_in + (wi - sp_i)); z_up = g(z_fun + 1.2)
    spig = lathe([(sp_i, z_sp), (sp_o, z_sp), (sp_o, z_fl), (fl, z_fl), (fl, z_up), (wi, z_up), (wi, z_fun),
                  (sp_i, z_in)], "camera-tube-coupon-spigot")
    out = []
    for ob, z_bed, z_far in ((sock, z_top, z_bot), (spig, z_up, z_sp)):
        for v in ob.data.vertices:
            v.co.x += COUPON_X
        _finish(ob)
        out.append((ob, z_bed, dict(name=ob.name, bed_face_z=z_bed, height=round(abs(z_bed - z_far), 1), x=COUPON_X)))
    return out


def build_mocks(L, z_shoulder):
    """Not printed: the two rings, the lens and a camera body, for renders and sanity checks."""
    pk_depth = math.floor(L["ring_h"] / LAYER + 1e-9) * LAYER
    z_pk = g(z_shoulder - pk_depth); z_lip = g(z_pk - LIP_T)
    r_od, t_i = L["ring_od"] / 2, L["thread"] / 2 - 1.0
    ret = L["retainer_od"] / 2
    out = [lathe([(t_i, z_pk), (r_od, z_pk), (r_od, z_shoulder), (t_i + 1, z_shoulder),
                  (t_i + 1, z_shoulder + 3.5), (t_i, z_shoulder + 3.5)], "mock_ring"),
           lathe([(ret - 2.5, z_lip - L["retainer_h"]), (ret, z_lip - L["retainer_h"]), (ret, z_lip),
                  (ret - 1.5, z_lip), (ret - 1.5, z_pk + 2.5), (ret - 2.5, z_pk + 2.5)], "mock_retainer"),
           lathe([(0, z_shoulder), (L["rim_od"] / 2, z_shoulder), (L["rim_od"] / 2, z_shoulder + L["lens_len"]),
                  (0, z_shoulder + L["lens_len"])], "mock_lens", segs=64),
           box("mock_camera-body", -40, 40, -82.5, 56.5, z_shoulder + L["lens_len"], z_shoulder + L["lens_len"] + 38.5)]
    for ob in out:
        _finish(ob); ob.display_type = "WIRE"
    return out


# --- checks and export ---------------------------------------------------------------------------
def selfcheck(ob, z_top):
    """Watertight, volume, and every horizontal face on the layer grid measured from the print bed (z_top)."""
    bm = bmesh.new(); bm.from_mesh(ob.data)
    nonman = sum(1 for e in bm.edges if not e.is_manifold)
    vol = bm.calc_volume(signed=True)
    planes = defaultdict(float)
    for f in bm.faces:
        if abs(f.normal.z) > 0.999:
            planes[round(z_top - f.verts[0].co.z, 2)] += f.calc_area()
    bm.free()
    off = sorted(z for z, a in planes.items() if a > 1.0 and abs(z / LAYER - round(z / LAYER)) > 1e-3)
    xs = [v.co.x for v in ob.data.vertices]; ys = [v.co.y for v in ob.data.vertices]; zs = [v.co.z for v in ob.data.vertices]
    dims = tuple(round(max(c) - min(c), 1) for c in (xs, ys, zs))
    ok = nonman == 0 and not off and vol > 0
    print(f"{'ok  ' if ok else 'FAIL'}  {ob.name:28s} {dims[0]:6.1f} x {dims[1]:6.1f} x {dims[2]:5.1f}  "
          f"{vol / 1000:5.1f} cm3  {vol * PLA:4.0f} g" + ("" if nonman == 0 else f"  nonmanifold={nonman}")
          + ("" if not off else f"  OFF-GRID at {off}"))
    return ok


def export_stl(ob, path):
    for o in bpy.context.view_layer.objects:
        o.select_set(False)
    ob.select_set(True); bpy.context.view_layer.objects.active = ob
    bpy.ops.wm.stl_export(filepath=str(path), export_selected_objects=True, apply_modifiers=True,
                          ascii_format=False, global_scale=1.0, use_scene_unit=False)


def check_blend():
    lid = bpy.data.objects.get("film-holder-135-lid")
    if lid is None:
        print("warning: film-holder-135-lid not found; is cad/neobox.blend open?"); return
    pts = [lid.matrix_world @ Vector(c) for c in lid.bound_box]
    w = max(p.x for p in pts) - min(p.x for p in pts); l = max(p.y for p in pts) - min(p.y for p in pts)
    top = max(p.z for p in pts)
    assert abs(w - LID_W) < 0.05 and abs(l - LID_L) < 0.05 and abs(top - LID_TOP) < 0.05, \
        f"lid in the .blend is {w:.1f} x {l:.1f}, top at {top:.1f}; this script expects {LID_W} x {LID_L}, {LID_TOP}"


def lens_from(a):
    thread, step = (int(v) for v in a.ring.split("-"))
    assert 30 <= thread < step <= 95, f"--ring {a.ring}: expected lens-thread-larger-thread, e.g. 46-52"
    return dict(ring=a.ring, thread=thread, step=step, ring_od=a.ring_od, ring_h=a.ring_h, wd=a.wd,
                lip_hole_d=step + 1.0,                    # the ring's larger thread passes through the lip
                rim_od=a.rim_od if a.rim_od else thread + 7.0, lens_len=a.lens_len,
                retainer_od=step + 5.0, retainer_h=5.0)   # the clamp ring (step -> step+3..5), mock only


def parse(argv):
    ap = argparse.ArgumentParser(prog="camera_tube.py", description=__doc__.split("\n\n")[1])
    ap.add_argument("--ring", required=True, help="step-up ring as lens-thread-larger-thread, e.g. 46-52")
    ap.add_argument("--ring-od", type=float, required=True, help="ring body outside diameter, mm")
    ap.add_argument("--ring-h", type=float, required=True, help="ring body height below its shoulder, mm")
    ap.add_argument("--wd", type=float, required=True, help="working distance at your magnification, mm")
    ap.add_argument("--base-wd", type=float, default=60.0, help="working distance of the bare base (default 60)")
    ap.add_argument("--spacer", type=float, default=None, help="also build a spacer of this length, mm")
    ap.add_argument("--coupon", action="store_true",
                    help="also build the two joint test pieces (socket and spigot), to check the turning fit before the base")
    ap.add_argument("--rim-od", type=float, default=None, help="lens front rim diameter, mm (mock and seat check)")
    ap.add_argument("--lens-len", type=float, default=80.0, help="lens length for the mock, mm")
    ap.add_argument("--mock", action="store_true", help="also build the (unprinted) ring, lens and camera mocks")
    ap.add_argument("--no-base", action="store_true", help="skip the base")
    ap.add_argument("--no-export", action="store_true", help="build in the scene only")
    ap.add_argument("--out", default="camera-tube", help="output directory for the STL files")
    return ap.parse_args(argv)


def main(argv):
    a = parse(argv)
    for k in ("wd", "base_wd"):
        v = getattr(a, k)
        if abs(v - g(v)) > 1e-6:
            print(f"note: --{k.replace('_', '-')} {v} snapped to the 0.2 mm grid: {g(v)}"); setattr(a, k, g(v))
    check_blend()
    L = lens_from(a)
    parts = []
    base, rb = build_base(a.base_wd)
    print("base:", rb)
    z_rest = rb["z_top"]
    if a.no_base:
        bpy.data.objects.remove(base, do_unlink=True)
    else:
        parts.append((base, rb["z_top"]))
    riser = 0.0
    if a.spacer:
        sp, rs = build_spacer(a.spacer, z_rest); print("spacer:", rs)
        parts.append((sp, rs["z_top"])); z_rest = rs["z_top"]; riser = a.spacer
    if a.coupon:
        for ob, z_bed, rk in build_coupon(rb["z_top"]):
            print("coupon:", rk); parts.append((ob, z_bed))
    H = g(a.wd - a.base_wd - riser)
    assert H >= 0, f"--wd {a.wd} is below the base ({a.base_wd} + spacer {riser}); lower --base-wd (min {BASE_WD_MIN})"
    col, rc = build_column(L, H, z_rest); print("column:", rc)
    parts.append((col, rc["z_shoulder"]))
    assert abs(rc["z_shoulder"] - FILM_PLANE - a.wd) < 1e-6, (rc["z_shoulder"], a.wd)
    print(f"shoulder at z = {rc['z_shoulder']}: working distance {rc['z_shoulder'] - FILM_PLANE:.1f} mm, lens rim seats on the {rc['rim_seat']}")
    if a.mock:
        build_mocks(L, rc["z_shoulder"])
    ok = all([selfcheck(ob, z) for ob, z in parts])
    if not a.no_export:
        os.makedirs(a.out, exist_ok=True)
        for ob, _ in parts:
            export_stl(ob, os.path.join(a.out, ob.name + ".stl"))
        print("wrote", ", ".join(ob.name + ".stl" for ob, _ in parts), "to", a.out)
    return ok


if __name__ == "__main__":
    argv = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else sys.argv[1:]
    ok = main(argv)
    if bpy.app.background and not ok:
        sys.exit(1)
elif "ARGS" in globals():
    RESULT = main(list(ARGS))
