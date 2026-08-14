#!/usr/bin/env python3
"""NeoBox v5 — exploded assembly drawing generator.

Regenerates (overwrites) three files in drawings/:
    exploded.svg          (English)
    exploded.zh-CN.svg    (Simplified Chinese)
    exploded.ja.svg       (Japanese)

Simplified 2.5D oblique view, vertical explosion, bottom-up stack order:
  1 main body -> 2 cover-stage -> 3 opal acrylic -> 4 steel shims
  -> 5 film-holder base -> 6 film strip -> 7 pressure element -> 8 lid
Flash + receiver lie on the desk beside the box (they stay outside).

All numbers trace to scratchpad/FACTS-v5.md (design values, mm).
Run: python3 gen_exploded.py
"""

import os

OUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "..", "..", "drawings")

# ---------------------------------------------------------------- canvas
W, H = 1000, 775
S = 1.25          # px per mm
KX, KY = 0.50, 0.28   # oblique depth factors (depth recedes up-left)


def dv(d_mm):
    """Screen offset for a depth of d_mm."""
    return (-KX * S * d_mm, -KY * S * d_mm)


# ---------------------------------------------------------------- palette
STK = "#444"          # neutral stroke
INK = "#111"
GREY_LN = "#666"      # leader lines
RAIL = "#999"         # alignment dashes
WHT_F, WHT_T, WHT_S = "#f2f2f2", "#fafafa", "#e3e3e3"   # white printed parts
BLK_F, BLK_T, BLK_S = "#3a3a3a", "#4b4b4b", "#2e2e2e"   # black printed parts
BLK_STK = "#161616"
STEEL_F, STEEL_T, STEEL_S = "#d9d9d9", "#e9e9e9", "#c4c4c4"
AMBER = "#e8a33d"
FILM_F, FILM_STK, FILM_PERF = "#7a5230", "#4a2f16", "#e9e0d2"

FONT = "Helvetica, Arial, sans-serif"

# ---------------------------------------------------------------- strings
LANG = {
    "en": {
        "file": "exploded.svg",
        "title": "NeoBox v5 — Exploded Assembly",
        "subtitle": "Bottom-up magnetic stack · overall 124.8×154.8×87 · dimensions in mm (design values)",
        "badge": "NO SCREWS · NO TOOLS · MAGNETIC",
        "steps_header": "Assembly steps",
        "steps": [
            ["Set the main body on the desk, open front", "toward you."],
            ["Rest the cover-stage on the walls — tenons", "drop into the corner notches."],
            ["Fit the opal acrylic 68×118 into the hidden", "slot under the stage."],
            ["Drop the 4 steel shims into their recesses,", "flush with the deck."],
            ["Set the film-holder base 94×120 into the", "flange tray."],
            ["Lay the film in the channel — both ends", "stick out of the holder."],
            ["Rest the pressure element 64×95 on the", "4.6 mm element ledge — pressure window", "insert or anti-Newton glass, either one."],
            ["Snap the magnetic lid shut — done,", "no screws, no tools."],
        ],
        "note": ["135-format holder shown; the 120 holder", "assembles the same way."],
        "labels": [
            "insert or AN glass (either)",
            "35 mm film — ends stick out",
            "film-holder base 94×120",
            "steel shims 10×10×1 ×4",
            "opal acrylic 68×118",
            "flange 94.6×120.6",
            "acrylic slot (underside)",
            "tenon notches (underside)",
            "open front",
            "locating tenons ×4",
        ],
        "flash1": "Flash lies flat on the desk, head against the open front.",
        "flash2": "Receiver stays with it outside — nothing goes inside the box.",
    },
    "zh": {
        "file": "exploded.zh-CN.svg",
        "title": "NeoBox v5 — 爆炸装配图",
        "subtitle": "自下而上磁吸堆叠 · 整机 124.8×154.8×87 · 尺寸单位 mm（设计值）",
        "badge": "无螺丝 · 无工具 · 磁吸",
        "steps_header": "装配步骤",
        "steps": [
            ["主箱放上桌面，敞开前口朝向自己。"],
            ["顶盖台搁上箱壁，四角榫槽对准定位榫落下。"],
            ["乳白亚克力 68×118 装入顶盖台底面暗槽。"],
            ["4 片钢垫片放入沉孔，与台面齐平。"],
            ["胶片夹底座 94×120 放进凸缘托盘。"],
            ["胶片条放入通道，两端伸出夹外。"],
            ["压片元件 64×95 搁上 4.6mm 元件台阶——", "压片窗插片或防牛顿环玻璃二选一。"],
            ["磁吸上盖合上即完成——无螺丝、无工具。"],
        ],
        "note": ["图示为 135 幅面夹；120 幅面装配方式相同。"],
        "labels": [
            "插片或 AN 玻璃（二选一）",
            "35mm 胶片条（两端伸出）",
            "胶片夹底座 94×120",
            "钢垫片 10×10×1 ×4",
            "乳白亚克力 68×118",
            "凸缘 94.6×120.6",
            "亚克力暗槽（底面）",
            "榫槽（底面四角）",
            "敞开前口",
            "定位榫 ×4",
        ],
        "flash1": "闪光灯平躺桌面，灯头怼住箱口。",
        "flash2": "接收器随灯留在箱外——不装进任何东西。",
    },
    "ja": {
        "file": "exploded.ja.svg",
        "title": "NeoBox v5 — 分解組立図",
        "subtitle": "下から積むマグネット構成 · 全体 124.8×154.8×87 · 寸法 mm（設計値）",
        "badge": "ネジなし · 工具なし · マグネット",
        "steps_header": "組立手順",
        "steps": [
            ["本体を机に置き、オープンフロントを", "手前に向ける。"],
            ["天板ステージを壁に載せ、四隅のダボ穴を", "位置決めダボに合わせる。"],
            ["乳白アクリル 68×118 をステージ裏の", "隠し溝にはめる。"],
            ["鋼シム 4 枚を座ぐりに入れて面一にする。"],
            ["ホルダー基部 94×120 をフランジトレーに置く。"],
            ["フィルムを通路に載せ、両端を外に出す。"],
            ["押さえエレメント 64×95 をエレメント段", "（4.6mm）に載せる——押さえ窓インサートか", "アンチニュートンガラスの二択。"],
            ["マグネットの上蓋を閉じて完成——", "ネジなし・工具なし。"],
        ],
        "note": ["図は 135 用ホルダー。120 用も同じ手順。"],
        "labels": [
            "インサートか AN ガラス（二択）",
            "35mm フィルム（両端はみ出す）",
            "ホルダー基部 94×120",
            "鋼シム 10×10×1 ×4",
            "乳白アクリル 68×118",
            "フランジ 94.6×120.6",
            "アクリル隠し溝（裏面）",
            "ダボ穴（裏面四隅）",
            "オープンフロント",
            "位置決めダボ ×4",
        ],
        "flash1": "ストロボは机に平置きし、発光部を箱口に当てる。",
        "flash2": "レシーバーも箱の外に置く——中には何も入れない。",
    },
}

FOOTER = "NeoBox v5 — 2026-08"


# ---------------------------------------------------------------- helpers
def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def pts(p):
    return " ".join(f"{x:.1f},{y:.1f}" for x, y in p)


def poly(p, fill, stroke=STK, sw=1.2, dash=None, fo=None):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    o = f' fill-opacity="{fo}"' if fo is not None else ""
    return (f'<polygon points="{pts(p)}" fill="{fill}"{o} '
            f'stroke="{stroke}" stroke-width="{sw}"{d}/>')


def line(x1, y1, x2, y2, stroke=GREY_LN, sw=1, dash=None):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    return (f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" '
            f'stroke="{stroke}" stroke-width="{sw}"{d}/>')


def txt(x, y, s, size=13, anchor="start", fill=INK, weight="normal"):
    a = f' text-anchor="{anchor}"' if anchor != "start" else ""
    w = f' font-weight="bold"' if weight == "bold" else ""
    return f'<text x="{x:.1f}" y="{y:.1f}" font-size="{size}"{a}{w} fill="{fill}">{esc(s)}</text>'


def leader(lx, ly, tx, ty):
    """One-bend leader from a right-aligned label to a target, with end dot."""
    return (f'<polyline points="{lx:.1f},{ly:.1f} {lx+14:.1f},{ly:.1f} {tx:.1f},{ty:.1f}" '
            f'fill="none" stroke="{GREY_LN}" stroke-width="1"/>'
            f'<circle cx="{tx:.1f}" cy="{ty:.1f}" r="2.2" fill="{GREY_LN}"/>')


def circnum(cx, cy, n, r=11, fs=13):
    return (f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r}" fill="#fff" '
            f'stroke="{STK}" stroke-width="1.5"/>'
            f'<text x="{cx:.1f}" y="{cy+fs*0.36:.1f}" font-size="{fs}" '
            f'text-anchor="middle" font-weight="bold" fill="{INK}">{n}</text>')


def slab(x, yb, w_mm, d_mm, h, cf, ct, cs, stroke=STK, sw=2):
    """Oblique slab: front-bottom-left at (x, yb). Returns side+top+front."""
    wp = w_mm * S
    dx, dy = dv(d_mm)
    side = [(x, yb), (x, yb - h), (x + dx, yb - h + dy), (x + dx, yb + dy)]
    top = [(x, yb - h), (x + wp, yb - h), (x + wp + dx, yb - h + dy), (x + dx, yb - h + dy)]
    front = [(x, yb), (x + wp, yb), (x + wp, yb - h), (x, yb - h)]
    return (poly(side, cs, stroke, 1.2) + poly(top, ct, stroke, 1.2) +
            poly(front, cf, stroke, sw))


def top_rect(x0, ytop, u_mm, t_mm, w_mm, d_mm):
    """Rect on a horizontal plane whose front-left corner is (x0, ytop)."""
    ox = x0 + u_mm * S + dv(t_mm)[0]
    oy = ytop + dv(t_mm)[1]
    dx, dy = dv(d_mm)
    wp = w_mm * S
    return [(ox, oy), (ox + wp, oy), (ox + wp + dx, oy + dy), (ox + dx, oy + dy)]


def text_w(s, size):
    """Rough width estimate (CJK = 1 em, latin ~0.62 em)."""
    return sum(size if ord(c) > 0x2E7F else size * 0.62 for c in s)


def rail(x, y1, y2):
    return line(x, y1, x, y2, RAIL, 1, "5,4")


# ---------------------------------------------------------------- geometry
GROUND = 690
X0 = 340                       # box front-left corner x
BOX_W, BOX_D = 154.8, 124.8    # mm: screen-x span, depth span
WALL_H = 73 * S                # front face rises to the wall top (73 mm)
TEN_H = 2.6 * S                # tenon height above wall top

BOX_TOP = GROUND - WALL_H                     # 598.75
COV_BOT = BOX_TOP - 58
COV_H = 10 * S
COV_TOP = COV_BOT - COV_H                     # deck front edge y
ACR_BOT = COV_TOP - 54
ACR_H = 4                                     # 2 mm, min visual thickness
SHIM_BOT = ACR_BOT - ACR_H - 36
SHIM_H = 3
BASE_BOT = SHIM_BOT - SHIM_H - 48
BASE_H = 5 * S
FILM_Y = BASE_BOT - BASE_H - 40               # film plane (front reference)
EL_BOT = FILM_Y - 36
EL_H = 4                                      # 2 mm
LID_BOT = EL_BOT - EL_H - 40
LID_H = 3 * S

HOLD_X = X0 + (BOX_W - 120) / 2 * S           # holder family left x (120 long)
ACR_X = X0 + (BOX_W - 118) / 2 * S
EL_X = X0 + (BOX_W - 95) / 2 * S

SHIM_UC = (77.4 - 12, 77.4 + 12)              # recess centers, screen-x (mm)
SHIM_TC = (62.4 - 41, 62.4 + 41)              # recess centers, depth (mm)


def build(L):
    a = []
    A = a.append
    A(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
      f'viewBox="0 0 {W} {H}">')
    A(f'<rect x="0" y="0" width="{W}" height="{H}" fill="#ffffff"/>')
    A(f'<g font-family="{FONT}" fill="{INK}">')

    # ---- title / subtitle / badge / footer
    A(txt(25, 44, L["title"], 21, weight="bold"))
    A(txt(25, 66, L["subtitle"], 12, fill="#555"))
    bw = text_w(L["badge"], 13) + 30
    bx = 985 - bw
    A(f'<rect x="{bx:.1f}" y="24" width="{bw:.1f}" height="30" rx="15" '
      f'fill="#fbf1dd" stroke="{AMBER}" stroke-width="1.6"/>')
    A(txt(bx + bw / 2, 43.5, L["badge"], 13, anchor="middle",
          fill="#8a5c10", weight="bold"))
    A(txt(985, 758, FOOTER, 12, anchor="end", fill="#888"))

    # ---- ground line
    A(line(25, GROUND, 585, GROUND, "#ccc", 1.5))

    # ================= 1. main body =================
    DX, DY = dv(BOX_D)
    # top face: outer rim + open cavity (cavity reaches the open left edge)
    A(poly([(X0, BOX_TOP), (X0 + BOX_W * S, BOX_TOP),
            (X0 + BOX_W * S + DX, BOX_TOP + DY), (X0 + DX, BOX_TOP + DY)],
           WHT_T, STK, 1.2))
    A(poly(top_rect(X0, BOX_TOP, 0, 2.4, 152.4, 120), "#d6d6d6", "#777", 1))
    # left face = open front: frame + aperture (walls 2.4, floor 3)
    A(poly([(X0, GROUND), (X0, BOX_TOP), (X0 + DX, BOX_TOP + DY),
            (X0 + DX, GROUND + DY)], WHT_S, STK, 1.2))
    adx, ady = dv(2.4)
    ax0, ay0 = X0 + adx, GROUND - 3 * S + ady
    fdx, fdy = dv(120)
    ah = WALL_H - 3 * S
    A(poly([(ax0, ay0), (ax0 + fdx, ay0 + fdy), (ax0 + fdx, ay0 + fdy - ah),
            (ax0, ay0 - ah)], "#e9e9e9", "#777", 1))
    # front face (a side wall) + 2 locating tenons on its top edge
    A(poly([(X0, GROUND), (X0 + BOX_W * S, GROUND),
            (X0 + BOX_W * S, BOX_TOP), (X0, BOX_TOP)], WHT_F, STK, 2))
    for u in (32, 111):  # tenon positions along the wall (12 mm long)
        tx = X0 + u * S
        A(f'<rect x="{tx:.1f}" y="{BOX_TOP - TEN_H:.1f}" width="{12*S:.1f}" '
          f'height="{TEN_H:.1f}" fill="{WHT_F}" stroke="{STK}" stroke-width="1.2"/>')

    # ---- flash + receiver on the ground (outside the box)
    A(f'<rect x="30" y="658" width="48" height="32" rx="4" fill="{BLK_F}" '
      f'stroke="{BLK_STK}" stroke-width="1.2"/>')
    A(line(38, 658, 38, 640, BLK_F, 2))
    A(f'<circle cx="38" cy="638.5" r="2.5" fill="{BLK_F}"/>')
    A(f'<rect x="85" y="621" width="167" height="69" rx="7" fill="{BLK_F}" '
      f'stroke="{BLK_STK}" stroke-width="1.2"/>')
    A(f'<rect x="248" y="623" width="74" height="65" rx="3" fill="{BLK_S}" '
      f'stroke="{BLK_STK}" stroke-width="1.2"/>')
    # emitting face 60x45, centre height 31 -> spans z 8.5..53.5
    A(f'<rect x="313" y="{GROUND - 53.5*S:.1f}" width="9" '
      f'height="{45*S:.1f}" fill="{AMBER}" fill-opacity="0.85" '
      f'stroke="#b9822c" stroke-width="1"/>')
    for y1, y2 in ((636, 618), (653, 648), (670, 678)):  # amber rays into aperture
        A(line(324, y1, 337, y2, AMBER, 1.6))
    A(txt(35, 714, L["flash1"], 13))
    A(txt(35, 733, L["flash2"], 13))

    # ================= 2. cover-stage =================
    A(slab(X0, COV_BOT, BOX_W, BOX_D, COV_H, WHT_F, WHT_T, WHT_S))
    # underside tenon notches (hidden -> dashed) on front face bottom corners
    for tx in (X0 + 2, X0 + BOX_W * S - 2 - 12 * S):
        A(f'<rect x="{tx:.1f}" y="{COV_BOT - 2.8*S:.1f}" width="{12*S:.1f}" '
          f'height="{2.8*S:.1f}" fill="none" stroke="#777" stroke-width="1" '
          f'stroke-dasharray="3,3"/>')
    # flange 94.6 x 120.6, raised 4 mm
    FL_H = 4 * S
    fu, ft = (BOX_W - 120.6) / 2, (BOX_D - 94.6) / 2
    fx = X0 + fu * S + dv(ft)[0]
    fy = COV_TOP + dv(ft)[1]
    fw = 120.6 * S
    gdx, gdy = dv(94.6)
    A(poly([(fx, fy), (fx + gdx, fy + gdy), (fx + gdx, fy + gdy - FL_H),
            (fx, fy - FL_H)], WHT_S, STK, 1.2))                     # left strip
    A(poly([(fx, fy - FL_H), (fx + fw, fy - FL_H), (fx + fw + gdx, fy - FL_H + gdy),
            (fx + gdx, fy - FL_H + gdy)], "#e9e9e9", STK, 1.2))     # top rim
    idx, idy = dv(89.6)
    A(poly([(fx + 2.5 * S + dv(2.5)[0], fy - FL_H + dv(2.5)[1]),
            (fx + fw - 2.5 * S + dv(2.5)[0], fy - FL_H + dv(2.5)[1]),
            (fx + fw - 2.5 * S + dv(2.5)[0] + idx, fy - FL_H + dv(2.5)[1] + idy),
            (fx + 2.5 * S + dv(2.5)[0] + idx, fy - FL_H + dv(2.5)[1] + idy)],
           WHT_T, "#888", 1))                                       # tray floor
    A(poly([(fx, fy), (fx + fw, fy), (fx + fw, fy - FL_H), (fx, fy - FL_H)],
           WHT_F, STK, 1.2))                                        # front strip
    # hidden acrylic slot 119x69 (underside) — dashed on deck
    A(poly(top_rect(X0, COV_TOP, (BOX_W - 119) / 2, (BOX_D - 69) / 2, 119, 69),
           "none", "#888", 1, dash="5,4"))
    # light window 62x95 (95 along screen-x)
    A(poly(top_rect(X0, COV_TOP, (BOX_W - 95) / 2, (BOX_D - 62) / 2, 95, 62),
           "#c5c5c5", "#555", 1.2))
    # shim recesses 10.6 sq at (±41, ±12); near pair hidden behind flange -> dashed
    for tc in SHIM_TC:
        for uc in SHIM_UC:
            p = top_rect(X0, COV_TOP, uc - 5.3, tc - 5.3, 10.6, 10.6)
            if tc < 62.4:
                A(poly(p, "none", "#777", 1, dash="3,2"))
            else:
                A(poly(p, "#c9c9c9", "#666", 1))

    # ---- alignment rails + shim drop lines (dashed)
    A(rail(X0, COV_BOT, BOX_TOP - TEN_H))
    A(rail(X0 + BOX_W * S, COV_BOT, BOX_TOP - TEN_H))
    A(rail(ACR_X, ACR_BOT, COV_TOP))
    A(rail(ACR_X + 118 * S, ACR_BOT, COV_TOP))
    A(rail(HOLD_X, BASE_BOT, ACR_BOT - ACR_H))
    A(rail(HOLD_X + 120 * S, BASE_BOT, ACR_BOT - ACR_H))
    A(rail(HOLD_X, FILM_Y - 8, BASE_BOT - BASE_H))
    A(rail(HOLD_X + 120 * S, FILM_Y - 8, BASE_BOT - BASE_H))
    A(rail(EL_X, EL_BOT, FILM_Y - 10))
    A(rail(EL_X + 95 * S, EL_BOT, FILM_Y - 10))
    A(rail(EL_X, LID_BOT, EL_BOT - EL_H))
    A(rail(EL_X + 95 * S, LID_BOT, EL_BOT - EL_H))
    shim_cx = {}
    for tc in SHIM_TC:
        for uc in SHIM_UC:
            cx = X0 + uc * S + dv(tc)[0]
            shim_cx[(uc, tc)] = cx
            A(line(cx, SHIM_BOT + dv(tc)[1] + 2, cx, COV_TOP + dv(tc)[1] - 3,
                   RAIL, 1, "4,3"))

    # ================= 3. opal acrylic (translucent) =================
    adx2, ady2 = dv(68)
    aw = 118 * S
    A(poly([(ACR_X, ACR_BOT), (ACR_X, ACR_BOT - ACR_H),
            (ACR_X + adx2, ACR_BOT - ACR_H + ady2), (ACR_X + adx2, ACR_BOT + ady2)],
           AMBER, "#c9973f", 1.2, fo=0.34))
    A(poly([(ACR_X, ACR_BOT - ACR_H), (ACR_X + aw, ACR_BOT - ACR_H),
            (ACR_X + aw + adx2, ACR_BOT - ACR_H + ady2),
            (ACR_X + adx2, ACR_BOT - ACR_H + ady2)],
           AMBER, "#c9973f", 1.2, fo=0.16))
    A(poly([(ACR_X, ACR_BOT), (ACR_X + aw, ACR_BOT),
            (ACR_X + aw, ACR_BOT - ACR_H), (ACR_X, ACR_BOT - ACR_H)],
           AMBER, "#c9973f", 1.6, fo=0.28))

    # ================= 4. steel shims =================
    for tc in SHIM_TC:
        for uc in SHIM_UC:
            sx = X0 + (uc - 5) * S + dv(tc - 5)[0]
            sy = SHIM_BOT + dv(tc - 5)[1]
            A(slab(sx, sy, 10, 10, SHIM_H, STEEL_F, STEEL_T, STEEL_S, STK, 1.2))

    # ================= 5. film-holder base (black) =================
    A(slab(HOLD_X, BASE_BOT, 120, 94, BASE_H, BLK_F, BLK_T, BLK_S, BLK_STK))
    A(poly(top_rect(HOLD_X, BASE_BOT - BASE_H, (120 - 37) / 2, (94 - 25) / 2,
                    37, 25), "#1c1c1c", BLK_STK, 1))

    # ================= 6. film strip (35 mm, ends stick out) =================
    fu0, fu1 = -18, 138          # mm along holder x, overhang 18 each side
    t0, t1 = (94 - 35) / 2, (94 + 35) / 2
    band = [( HOLD_X + fu0 * S + dv(t0)[0], FILM_Y + dv(t0)[1]),
            ( HOLD_X + fu1 * S + dv(t0)[0], FILM_Y + dv(t0)[1]),
            ( HOLD_X + fu1 * S + dv(t1)[0], FILM_Y + dv(t1)[1]),
            ( HOLD_X + fu0 * S + dv(t1)[0], FILM_Y + dv(t1)[1])]
    A(poly(band, FILM_F, FILM_STK, 1.2))
    u = fu0 + 4
    while u < fu1 - 2:
        for tp in (t0 + 2.2, t1 - 4.4):
            A(poly(top_rect(HOLD_X, FILM_Y, u, tp, 2.4, 2.2), FILM_PERF,
                   "none", 0))
        u += 7.5
    A(poly(top_rect(HOLD_X, FILM_Y, (120 - 36) / 2, (94 - 24) / 2, 36, 24),
           "none", "#caa77f", 1))   # one frame outline

    # ================= 7. pressure element =================
    A(slab(EL_X, EL_BOT, 95, 64, EL_H, BLK_F, BLK_T, BLK_S, BLK_STK))
    A(poly(top_rect(EL_X, EL_BOT - EL_H, (95 - 37) / 2, (64 - 25) / 2, 37, 25),
           "none", "#999", 1, dash="4,3"))

    # ================= 8. lid =================
    A(slab(HOLD_X, LID_BOT, 120, 94, LID_H, BLK_F, BLK_T, BLK_S, BLK_STK))
    A(poly(top_rect(HOLD_X, LID_BOT - LID_H, (120 - 37) / 2, (94 - 25) / 2,
                    37, 25), "#1c1c1c", BLK_STK, 1))

    # ---- layer number circles (right of each layer) + leaders
    CX = 560
    layers = [
        (1, GROUND - WALL_H / 2 + 12, X0 + BOX_W * S + 2),
        (2, COV_BOT - COV_H / 2, X0 + BOX_W * S + 2),
        (3, ACR_BOT - ACR_H / 2, ACR_X + 118 * S + 2),
        (4, SHIM_BOT - 4, shim_cx[(SHIM_UC[1], SHIM_TC[0])] + 8),
        (5, BASE_BOT - BASE_H / 2, HOLD_X + 120 * S + 2),
        (6, FILM_Y - 6, HOLD_X + fu1 * S + dv(t0)[0] + 2),
        (7, EL_BOT - EL_H / 2, EL_X + 95 * S + 2),
        (8, LID_BOT - LID_H / 2, HOLD_X + 120 * S + 2),
    ]
    for n, cy, tx0 in layers:
        A(line(tx0, cy, CX - 11, cy, GREY_LN, 1))
        A(circnum(CX, cy, n))

    # ---- left fan labels
    targets = [
        (EL_X + 1, EL_BOT - EL_H / 2),                       # element
        (HOLD_X + fu0 * S + dv(t0)[0] + 3, FILM_Y + dv(t0)[1] - 2),  # film end
        (HOLD_X + 1, BASE_BOT - BASE_H / 2),                 # base
        (X0 + (SHIM_UC[0] - 5) * S + dv(SHIM_TC[0] - 5)[0] - 2,
         SHIM_BOT + dv(SHIM_TC[0] - 5)[1] - 1.5),            # near-left shim
        (ACR_X + 1, ACR_BOT - ACR_H / 2),                    # acrylic
        (fx + gdx * 0.5, fy + gdy * 0.5 - FL_H / 2),         # flange left rim
        (X0 + 43 * S + dv((BOX_D - 69) / 2)[0],
         COV_TOP + dv((BOX_D - 69) / 2)[1]),                 # slot front edge dash
        (X0 + 8, COV_BOT - 1.4 * S),                         # notch
        (X0 - 42, BOX_TOP - 8),                              # open front
        (X0 + 38 * S, BOX_TOP - TEN_H / 2),                  # tenon
    ]
    lx_text, lx_lead = 213, 219
    prev = 0
    for (txx, tyy), label in zip(targets, L["labels"]):
        ly = max(tyy - 6, prev + 23)
        prev = ly
        A(txt(lx_text, ly + 4, label, 13, anchor="end"))
        A(leader(lx_lead, ly, txx, tyy))

    # ---- step list (right column)
    A(txt(640, 118, L["steps_header"], 15, weight="bold"))
    y = 144
    for i, lines in enumerate(L["steps"], 1):
        A(circnum(652, y - 4, i, r=9, fs=12))
        for j, s in enumerate(lines):
            A(txt(668, y + j * 18, s, 13))
        y += len(lines) * 18 + 12
    for j, s in enumerate(L["note"]):
        A(txt(640, y + 6 + j * 16, s, 12, fill="#777"))

    A('</g></svg>')
    return "\n".join(a) + "\n"


def main():
    out = os.path.normpath(OUT_DIR)
    for L in LANG.values():
        path = os.path.join(out, L["file"])
        with open(path, "w", encoding="utf-8") as f:
            f.write(build(L))
        print("wrote", path)


if __name__ == "__main__":
    main()
