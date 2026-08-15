#!/usr/bin/env python3
"""NeoBox v1 — manufacturing overview drawing generator.

Generates drawings/manufacturing-overview.svg (+ .zh-CN.svg, .ja.svg):
a "kit card" grid — 9 printed parts (top) + purchased hardware (bottom).
All numbers come from scratchpad/FACTS-v5.md (§2 print table, §8 BOM).
"""

import os

OUT_DIR = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "drawings"))

W, H = 980, 752
FONT = "Helvetica, Arial, sans-serif"
MONO = "Menlo, Consolas, monospace"
AMBER = "#e8a33d"
INK = "#111"
S = 0.72          # px per mm, shared by all printed-part sketches (same scale feel)
SB = 0.55         # px per mm for purchased flat goods

# ---------------------------------------------------------------- language ---

LANG = {
    "en": {
        "suffix": "",
        "title": "NeoBox v1 — Manufacturing Overview",
        "subtitle": "9 printed parts + purchased hardware · all dimensions in mm",
        "spec1": "standard PLA · layer height 0.2 mm · infill 15% · no supports on any part",
        "spec2": "largest part 154.8 mm → a 160×160 bed is enough",
        "sec_print": "3D-printed parts ×9",
        "chip_white": "white PLA ×2",
        "chip_black": "black PLA ×7",
        "sec_buy": "Purchased parts — 3 required + 2 optional",
        "white": "white",
        "black": "black",
        "optional": "optional",
        "buy_names": ["opal acrylic", "magnet N35", "steel shim",
                      "anti-Newton glass", "black flocking sheet"],
        "credit": "NeoBox v1 — 2026-08",
    },
    "zh": {
        "suffix": ".zh-CN",
        "title": "NeoBox v1 — 制造总览",
        "subtitle": "打印件 9 件 + 外购件 · 尺寸单位 mm",
        "spec1": "普通 PLA · 层高 0.2 mm · 填充 15% · 全部免支撑",
        "spec2": "最大件 154.8 mm → 160×160 打印床即可",
        "sec_print": "打印件 ×9",
        "chip_white": "白色 PLA ×2",
        "chip_black": "黑色 PLA ×7",
        "sec_buy": "外购件 — 必备 3 + 可选 2",
        "white": "白色",
        "black": "黑色",
        "optional": "可选",
        "buy_names": ["乳白亚克力", "磁铁 N35", "钢垫片",
                      "防牛顿环玻璃", "黑色植绒贴"],
        "credit": "NeoBox v1 — 2026-08",
    },
    "ja": {
        "suffix": ".ja",
        "title": "NeoBox v1 — 製造オーバービュー",
        "subtitle": "プリントパーツ 9 点 + 購入部品 · 寸法単位 mm",
        "spec1": "標準 PLA · 積層ピッチ 0.2 mm · インフィル 15% · 全パーツサポート不要",
        "spec2": "最大パーツ 154.8 mm → 160×160 ビルドプレートで可",
        "sec_print": "プリントパーツ ×9",
        "chip_white": "白 PLA ×2",
        "chip_black": "黒 PLA ×7",
        "sec_buy": "購入部品 — 必須 3 + オプション 2",
        "white": "白",
        "black": "黒",
        "optional": "オプション",
        "buy_names": ["乳白アクリル", "磁石 N35", "スチールシム",
                      "アンチニュートンガラス", "黒の植毛シート"],
        "credit": "NeoBox v1 — 2026-08",
    },
}

# spec / qty / optional flag are language-neutral (indices match buy_names)
BUY_SPECS = [("68×118×2", "×1", False),
             ("Ø8×2", "×32", False),
             ("10×10×1", "×4", False),
             ("64×95×2", "×1", True),
             ("A5", "×1", True)]

# ------------------------------------------------------------- svg helpers ---

NARROW = set(" .,:;()[]|·'/!iIl1jt")


def est_w(s, size, mono=False, bold=False):
    """Rough text width estimate for layout (safety-biased)."""
    if mono:
        w = len(s) * 0.62 * size
    else:
        w = 0.0
        for ch in s:
            o = ord(ch)
            if o >= 0x2E80 or ch in "—→":
                w += 1.02 * size
            elif ch in NARROW:
                w += 0.34 * size
            elif ch == "Ø":
                w += 0.70 * size
            else:
                w += 0.58 * size
    return w * (1.06 if bold else 1.0)


def T(x, y, s, size=13, anchor="start", fill=INK, font=FONT, weight=None):
    a = f'font-family="{font}" font-size="{size}" fill="{fill}" text-anchor="{anchor}"'
    if weight:
        a += f' font-weight="{weight}"'
    return f'<text x="{x:.1f}" y="{y:.1f}" {a}>{s}</text>'


def R(x, y, w, h, fill="none", stroke="#444", sw=1.2, dash=None, rx=None):
    a = f'x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" fill="{fill}"'
    if stroke:
        a += f' stroke="{stroke}" stroke-width="{sw}"'
    if dash:
        a += f' stroke-dasharray="{dash}"'
    if rx:
        a += f' rx="{rx}"'
    return f"<rect {a}/>"


def C(cx, cy, r, fill, stroke="#444", sw=1.2):
    return (f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r}" fill="{fill}" '
            f'stroke="{stroke}" stroke-width="{sw}"/>')


def LN(x1, y1, x2, y2, stroke="#444", sw=1, dash=None):
    a = f'x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{stroke}" stroke-width="{sw}"'
    if dash:
        a += f' stroke-dasharray="{dash}"'
    return f"<line {a}/>"


def crect(cx, cy, w, h, **kw):
    return R(cx - w / 2, cy - h / 2, w, h, **kw)


# --------------------------------------------------- printed-part sketches ---
# Each draw_* returns svg elements centered on (cx, cy). Top view, scale S.

def draw_main_body(cx, cy):
    """Main box, top view: floor + U walls (left/right/back), open front (amber)."""
    w, h = 124.8 * S, 154.8 * S
    wall = max(2.4 * S, 4.5)          # exaggerated for visibility, not dimensioned
    x0, y0 = cx - w / 2, cy - h / 2
    x1, y1 = x0 + w, y0 + h
    el = [R(x0, y0, w, h, fill="#f2f2f2", stroke="#444", sw=1)]  # floor plate
    u = (f'M {x0:.1f} {y1:.1f} L {x0:.1f} {y0:.1f} L {x1:.1f} {y0:.1f} '
         f'L {x1:.1f} {y1:.1f} L {x1 - wall:.1f} {y1:.1f} L {x1 - wall:.1f} {y0 + wall:.1f} '
         f'L {x0 + wall:.1f} {y0 + wall:.1f} L {x0 + wall:.1f} {y1:.1f} Z')
    el.append(f'<path d="{u}" fill="#d9d9d9" stroke="#444" stroke-width="2"/>')
    # 4 locating tenons (2.4×12) on the side-wall tops
    tl = 12 * S
    for fy in (0.28, 0.62):
        ty = y0 + h * fy
        el.append(R(x0 + 0.9, ty, wall - 1.8, tl, fill="#a8a8a8", stroke="#555", sw=0.8))
        el.append(R(x1 - wall + 0.9, ty, wall - 1.8, tl, fill="#a8a8a8", stroke="#555", sw=0.8))
    # open front edge, amber accent
    el.append(LN(x0 + wall, y1, x1 - wall, y1, stroke=AMBER, sw=3))
    return el


def draw_cover_stage(cx, cy):
    """Cover-stage, top view: plate, flange frame 94.6×120.6, window 62×95, 4 shim pockets."""
    w, h = 124.8 * S, 154.8 * S
    el = [crect(cx, cy, w, h, fill="#f2f2f2", stroke="#444", sw=2)]
    fw, fh = 94.6 * S, 120.6 * S      # flange surrounds this tray area
    band = 3.5                        # illustrative flange band, not dimensioned
    el.append(crect(cx, cy, fw + 2 * band, fh + 2 * band, fill="#d9d9d9", stroke="#444", sw=1.4))
    el.append(crect(cx, cy, fw, fh, fill="#f2f2f2", stroke="#444", sw=1))
    el.append(crect(cx, cy, 62 * S, 95 * S, fill="#fff", stroke="#444", sw=1.4))  # light window
    sq = 10.6 * S
    for sx in (-41, 41):
        for sy in (-12, 12):
            el.append(crect(cx + sx * S, cy + sy * S, sq, sq,
                            fill="#e6e6e6", stroke="#666", sw=0.8))
    # corner tenon notches on the underside (hidden → dashed)
    nz = 12 * S
    for fx in (-1, 1):
        for fy in (-1, 1):
            el.append(crect(cx + fx * (w / 2 - nz / 2 - 2), cy + fy * (h / 2 - nz / 2 - 2),
                            nz, nz, fill="none", stroke="#999", sw=0.9, dash="2.5,2"))
    return el


def _plate(cx, cy, wmm, hmm):
    return crect(cx, cy, wmm * S, hmm * S, fill="#3a3a3a", stroke="#111", sw=2)


def _window(cx, cy, wmm, hmm):
    return crect(cx, cy, wmm * S, hmm * S, fill="#fff", stroke="#111", sw=1.2)


def draw_holder_base(win_w, win_h):
    def d(cx, cy):
        el = [_plate(cx, cy, 94, 120)]
        # outer rails ±31..33.5 carrying the 4.6 element ledge
        for fx in (-1, 1):
            el.append(LN(cx + fx * 31 * S, cy - 56 * S, cx + fx * 31 * S, cy + 56 * S,
                         stroke="#6f6f6f", sw=1))
            el.append(LN(cx + fx * 33.5 * S, cy - 56 * S, cx + fx * 33.5 * S, cy + 56 * S,
                         stroke="#6f6f6f", sw=1))
        # element seat 64×95 (dashed = seat outline on the ledge)
        el.append(crect(cx, cy, 64 * S, 95 * S, fill="none", stroke="#9a9a9a", sw=1, dash="3,2.5"))
        el.append(_window(cx, cy, win_w, win_h))
        return el
    return d


def draw_holder_lid(win_w, win_h):
    def d(cx, cy):
        el = [_plate(cx, cy, 94, 120)]
        # element clearance cavity 64.8×96 on the underside (dashed)
        el.append(crect(cx, cy, 64.8 * S, 96 * S, fill="none", stroke="#9a9a9a", sw=1, dash="3,2.5"))
        el.append(_window(cx, cy, win_w, win_h))
        return el
    return d


def draw_pressure_window(win_w, win_h):
    def d(cx, cy):
        return [_plate(cx, cy, 64, 95), _window(cx, cy, win_w, win_h)]
    return d


def draw_mask(cx, cy):
    return [_plate(cx, cy, 94, 80), _window(cx, cy, 56.5, 56.5)]


# 9 printed parts — FACTS §2 (file, colour, envelope, sketch)
PARTS_ROW1 = [
    ("main-body.stl", "white", "124.8×154.8×75.6", draw_main_body),
    ("cover-stage.stl", "white", "124.8×154.8×10.0", draw_cover_stage),
    ("film-holder-135-base.stl", "black", "94×120×5", draw_holder_base(25, 37)),
    ("film-holder-135-lid.stl", "black", "94×120×3", draw_holder_lid(25, 37)),
    ("pressure-window-135.stl", "black", "64×95×2", draw_pressure_window(25, 37)),
]
PARTS_ROW2 = [
    ("film-holder-120-base.stl", "black", "94×120×5", draw_holder_base(57, 85)),
    ("film-holder-120-lid.stl", "black", "94×120×3", draw_holder_lid(57, 85)),
    ("pressure-window-120.stl", "black", "64×95×2", draw_pressure_window(57, 85)),
    ("mask-6x6.stl", "black", "94×80×1", draw_mask),
]

# ------------------------------------------------------- purchased sketches ---

def buy_acrylic(cx, cy):
    w, h = 68 * SB, 118 * SB
    el = [crect(cx, cy, w, h, fill="#fbfbfb", stroke="#999", sw=1.5, rx=2)]
    el.append(LN(cx - w / 2 + 6, cy + h / 2 - 8, cx - w / 2 + 16, cy - h / 2 + 8, stroke="#e0e0e0", sw=2))
    el.append(LN(cx - w / 2 + 13, cy + h / 2 - 8, cx - w / 2 + 23, cy - h / 2 + 8, stroke="#e8e8e8", sw=2))
    return el


def buy_magnet(cx, cy):
    el = []
    for i in range(3):                # stack of Ø8×2 discs (side view, stylized)
        y = cy + 12 - i * 9
        el.append(R(cx - 15, y - 3, 30, 6, fill="#d9d9d9", stroke="#555", sw=1, rx=3))
    el.append(f'<ellipse cx="{cx}" cy="{cy - 8.5}" rx="15" ry="4" fill="#e9e9e9" '
              f'stroke="#555" stroke-width="1"/>')
    return el


def buy_shim(cx, cy):
    el = []
    for i in range(3):                # a few 10×10 squares fanned out
        off = (i - 1) * 5
        el.append(crect(cx + off, cy + off, 26, 26, fill="#e3e3e3", stroke="#555", sw=1.2))
    return el


def buy_an_glass(cx, cy):
    w, h = 64 * SB, 95 * SB
    el = [crect(cx, cy, w, h, fill="#f4f4f4", stroke="#888", sw=1.5)]
    for i in range(4):                # matte-face hatch
        x = cx - w / 2 + 7 + i * 8
        el.append(LN(x, cy + h / 2 - 5, x + 7, cy - h / 2 + 5, stroke="#d5d5d5", sw=1))
    return el


def buy_led(cx, cy):
    el = []
    for r, dy in enumerate((-9, 9)):  # two 120 mm segments
        y = cy + dy
        el.append(R(cx - 48, y - 4.5, 96, 9, fill="#f0f0f0", stroke="#888", sw=1.2, rx=4))
        for i in range(5):
            el.append(R(cx - 40 + i * 19, y - 2.5, 5, 5, fill=AMBER, stroke="none", sw=0))
    return el


def buy_flock(cx, cy):
    w, h = 38, 50
    x0, y0 = cx - w / 2, cy - h / 2
    el = [R(x0, y0, w, h, fill="#3a3a3a", stroke="#111", sw=1.5)]
    el.append(f'<path d="M {x0 + w:.1f} {y0 + h - 12:.1f} L {x0 + w:.1f} {y0 + h:.1f} '
              f'L {x0 + w - 12:.1f} {y0 + h:.1f} Z" fill="#8a8a8a" stroke="#111" stroke-width="1"/>')
    return el


BUY_SKETCHES = [buy_acrylic, buy_magnet, buy_shim, buy_an_glass, buy_flock]

# ------------------------------------------------------------------ layout ---

CARD_W, CARD_H, GAP = 176, 196, 8
BUY_W, BUY_H, BUY_GAP = 148, 150, 6


def color_dot(cx, cy, colour):
    if colour == "white":
        return C(cx, cy, 5, "#fff", stroke="#444", sw=1.4)
    return C(cx, cy, 5, "#3a3a3a", stroke="#111", sw=1.2)


def part_card(x, y, L, part):
    fname, colour, dims, draw = part
    cx = x + CARD_W / 2
    el = [R(x, y, CARD_W, CARD_H, fill="#fff", stroke="#ccc", sw=1, rx=6)]
    el += draw(cx, y + 80)
    el.append(T(cx, y + 156, fname, size=11, anchor="middle", font=MONO, fill=INK))
    el.append(T(cx, y + 173, dims, size=13, anchor="middle", fill="#333"))
    word = L[colour]
    tot = 10 + 6 + est_w(word, 12)
    dx = cx - tot / 2 + 5
    el.append(color_dot(dx, y + 185, colour))
    el.append(T(dx + 11, y + 189, word, size=12, fill="#333"))
    return el


def buy_card(x, y, L, idx):
    name = L["buy_names"][idx]
    spec, qty, optional = BUY_SPECS[idx]
    cx = x + BUY_W / 2
    border = dict(dash="4,3", stroke="#999") if optional else dict(stroke="#ccc")
    el = [R(x, y, BUY_W, BUY_H, fill="#fff", sw=1, rx=6, **border)]
    el += BUY_SKETCHES[idx](cx, y + 54)
    if optional:
        btxt = L["optional"]
        bw = est_w(btxt, 11) + 12
        bx = x + BUY_W - bw - 5
        el.append(R(bx, y + 6, bw, 17, fill="#fff", stroke="#888", sw=0.9, dash="3,2", rx=8))
        el.append(T(bx + bw / 2, y + 18.5, btxt, size=11, anchor="middle", fill="#555"))
    el.append(T(cx, y + 108, name, size=11.5, anchor="middle", fill=INK))
    el.append(T(cx, y + 124, spec, size=12, anchor="middle", font=MONO, fill="#333"))
    el.append(T(cx, y + 140, qty, size=13, anchor="middle", fill=INK, weight="bold"))
    return el


def section_header(x, y, L):
    """Printed-parts header with white/black colour-group chips."""
    el = [T(x, y, L["sec_print"], size=15, weight="bold")]
    cur = x + est_w(L["sec_print"], 15, bold=True) + 26
    el.append(C(cur + 5, y - 4.5, 5.5, "#fff", stroke="#444", sw=1.4))
    el.append(T(cur + 16, y, L["chip_white"], size=13, fill="#333"))
    cur += 16 + est_w(L["chip_white"], 13) + 24
    el.append(C(cur + 5, y - 4.5, 5.5, "#3a3a3a", stroke="#111", sw=1.2))
    el.append(T(cur + 16, y, L["chip_black"], size=13, fill="#333"))
    return el


def build(L):
    el = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">',
          R(0, 0, W, H, fill="#fff", stroke=None)]
    # header
    el.append(T(30, 44, L["title"], size=21, weight="bold"))
    el.append(T(30, 66, L["subtitle"], size=12, fill="#555"))
    el.append(T(W - 30, 38, L["spec1"], size=12, anchor="end", fill="#444"))
    el.append(T(W - 30, 56, L["spec2"], size=12, anchor="end", fill="#444"))
    # printed parts
    el += section_header(30, 98, L)
    for i, part in enumerate(PARTS_ROW1):
        el += part_card(30 + i * (CARD_W + GAP), 110, L, part)
    row2_x = (W - (4 * CARD_W + 3 * GAP)) / 2
    for i, part in enumerate(PARTS_ROW2):
        el += part_card(row2_x + i * (CARD_W + GAP), 318, L, part)
    # purchased parts
    el.append(T(30, 546, L["sec_buy"], size=15, weight="bold"))
    n_buy = len(BUY_SPECS)
    buy_x0 = (W - (n_buy * BUY_W + (n_buy - 1) * BUY_GAP)) / 2
    for i in range(n_buy):
        el += buy_card(buy_x0 + i * (BUY_W + BUY_GAP), 558, L, i)
    # credit
    el.append(T(W - 30, 736, L["credit"], size=12, anchor="end", fill="#666"))
    el.append("</svg>")
    return "\n".join(el) + "\n"


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    for L in LANG.values():
        path = os.path.join(OUT_DIR, f"manufacturing-overview{L['suffix']}.svg")
        with open(path, "w", encoding="utf-8") as f:
            f.write(build(L))
        print("wrote", path)


if __name__ == "__main__":
    main()
