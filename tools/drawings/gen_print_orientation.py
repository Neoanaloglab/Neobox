#!/usr/bin/env python3
"""NeoBox v1 — print-orientation drawing generator.

Generates drawings/print-orientation.svg (en), .zh-CN.svg, .ja.svg.
Data source: scratchpad/FACTS-v5.md §2 (9 STLs, colors, sizes, orientations)
and §3 (per-part local layer stacks). All geometry is schematic side-view
sketches (thin parts vertically exaggerated); no dimension figures shown.
"""
import os

OUT_DIR = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                        "..", "..", "drawings"))

# ---------------------------------------------------------------- canvas
W = 960
MARGIN = 24
CARD_W = 293
CARD_H = 182
GAP_X = 16
GAP_Y = 14
GRID_TOP = 116
H = GRID_TOP + 3 * CARD_H + 2 * GAP_Y + 34  # grid + footer strip

AMBER = "#e8a33d"
INK = "#111"
GREY = "#444"
FILL_WHITE_PART = "#f2f2f2"
FILL_BLACK_PART = "#3a3a3a"
BED_FILL = "#d9d9d9"

FONT = "Helvetica, Arial, sans-serif"
MONO = "SFMono-Regular, Menlo, Consolas, monospace"

S = 1.2  # px per mm, horizontal (part widths comparable across cards)

# ---------------------------------------------------------------- i18n
LANG = {
    "en": {
        "suffix": "",
        "title": "Print Orientation",
        "subtitle": "NeoBox v1 — how each of the 9 printed parts sits on the build plate",
        "banner": "All 9 parts print without supports · Layer height 0.2 mm · Do not rescale (unit: mm)",
        "legend_white": "white PLA",
        "legend_black": "black PLA",
        "footer": "NeoBox v1 — 2026-08",
        "desc": {
            "main-body": ["Flat bottom down, opening up", "(the missing wall is by design)"],
            "cover-stage": ["Large flat face down,", "raised frame flange up"],
            "base": ["Flat face down, long raised rails up"],
            "lid": ["Smooth large flat face DOWN,", "shallow square recess UP"],
            "insert": ["Lay flat (thin plate)"],
            "mask": ["Lay flat (thin plate)"],
        },
    },
    "zh": {
        "suffix": ".zh-CN",
        "title": "打印朝向",
        "subtitle": "NeoBox v1 — 9 个打印件在打印机床板上的摆放姿态",
        "banner": "9 件全部免支撑打印 · 层高一律 0.2 mm · 切勿缩放（单位 mm）",
        "legend_white": "白 PLA",
        "legend_black": "黑 PLA",
        "footer": "NeoBox v1 — 2026-08",
        "desc": {
            "main-body": ["平底朝下，开口朝上", "（缺一面墙是设计特征）"],
            "cover-stage": ["平的大面朝下，方框凸缘朝上"],
            "base": ["平面朝下，长条凸轨朝上"],
            "lid": ["光滑大平面朝下，", "浅方坑的面朝上"],
            "insert": ["平放（薄片）"],
            "mask": ["平放（薄片）"],
        },
    },
    "ja": {
        "suffix": ".ja",
        "title": "プリント方向",
        "subtitle": "NeoBox v1 — 9 点の印刷パーツをビルドプレートに置く向き",
        "banner": "全 9 パーツともサポート不要 · 積層ピッチは必ず 0.2 mm · 拡大縮小禁止（単位 mm）",
        "legend_white": "白 PLA",
        "legend_black": "黒 PLA",
        "footer": "NeoBox v1 — 2026-08",
        "desc": {
            "main-body": ["平らな底を下、開口を上", "（壁が一面ないのは設計どおり）"],
            "cover-stage": ["大きな平面を下、枠フランジを上"],
            "base": ["平面を下、細長いレールを上"],
            "lid": ["つるつるの大平面を下、", "浅い四角のくぼみを上"],
            "insert": ["平置き（薄板）"],
            "mask": ["平置き（薄板）"],
        },
    },
}

# ---------------------------------------------------------------- svg helpers

def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def T(x, y, s, size=13, anchor="start", fill=INK, bold=False, mono=False):
    fam = MONO if mono else FONT
    weight = ' font-weight="bold"' if bold else ""
    return (f'<text x="{x:.1f}" y="{y:.1f}" font-family="{fam}" font-size="{size}"'
            f' fill="{fill}" text-anchor="{anchor}"{weight}>{esc(s)}</text>')


def rect(x, y, w, h, fill, stroke="none", sw=0, rx=0):
    r = f' rx="{rx}"' if rx else ""
    st = f' stroke="{stroke}" stroke-width="{sw}"' if stroke != "none" else ""
    return f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" fill="{fill}"{st}{r}/>'


def poly(pts, fill, stroke=GREY, sw=2):
    p = " ".join(f"{x:.1f},{y:.1f}" for x, y in pts)
    return (f'<polygon points="{p}" fill="{fill}" stroke="{stroke}"'
            f' stroke-width="{sw}" stroke-linejoin="round"/>')


def circle(cx, cy, r, fill, stroke="none", sw=0):
    st = f' stroke="{stroke}" stroke-width="{sw}"' if stroke != "none" else ""
    return f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r}" fill="{fill}"{st}/>'


# ---------------------------------------------------------------- part sketches
# Each sketch(cx, ybed) returns (svg_elements, half_width_px).
# Side views; thin parts are vertically exaggerated on purpose (schematic).

def sk_main_body(cx, ybed):
    # 124.8 wide, 75.6 tall; bottom plate + two side walls, open top,
    # locating tenons as small nubs on wall tops.
    hw, h, t, b = 75, 91, 8, 9
    x0, x1, yt = cx - hw, cx + hw, ybed - h
    lc, rc = x0 + t / 2, x1 - t / 2
    pts = [(x0, ybed), (x0, yt),
           (lc - 2.5, yt), (lc - 2.5, yt - 4), (lc + 2.5, yt - 4), (lc + 2.5, yt),
           (x0 + t, yt), (x0 + t, ybed - b), (x1 - t, ybed - b), (x1 - t, yt),
           (rc - 2.5, yt), (rc - 2.5, yt - 4), (rc + 2.5, yt - 4), (rc + 2.5, yt),
           (x1, yt), (x1, ybed)]
    return [poly(pts, FILL_WHITE_PART)], hw


def sk_cover_stage(cx, ybed):
    # 124.8 wide plate, tray flange frame (94.6 span) raised in the middle.
    hw, ph = 75, 14
    fx, fw, fh = 94.6 / 2 * S, 8, 9  # flange center offset, bump width/height
    x0, x1, yp = cx - hw, cx + hw, ybed - ph
    pts = [(x0, ybed), (x0, yp),
           (cx - fx - fw / 2, yp), (cx - fx - fw / 2, yp - fh),
           (cx - fx + fw / 2, yp - fh), (cx - fx + fw / 2, yp),
           (cx + fx - fw / 2, yp), (cx + fx - fw / 2, yp - fh),
           (cx + fx + fw / 2, yp - fh), (cx + fx + fw / 2, yp),
           (x1, yp), (x1, ybed)]
    return [poly(pts, FILL_WHITE_PART)], hw


def sk_base(cx, ybed):
    # 94 wide plate; outer glass-ledge rails (±31..33.5) tall, inner film
    # rails (±17.7..19.7) lower.
    hw, ph = 94 / 2 * S, 11
    ox, ow, oh = 32.25 * S, 6, 6   # outer rail center / width / height
    ix, iw, ih = 18.7 * S, 5, 4    # inner rail
    x0, x1, yp = cx - hw, cx + hw, ybed - ph
    pts = [(x0, ybed), (x0, yp)]
    for c, w, hgt in [(-ox, ow, oh), (-ix, iw, ih), (ix, iw, ih), (ox, ow, oh)]:
        pts += [(cx + c - w / 2, yp), (cx + c - w / 2, yp - hgt),
                (cx + c + w / 2, yp - hgt), (cx + c + w / 2, yp)]
    pts += [(x1, yp), (x1, ybed)]
    return [poly(pts, FILL_BLACK_PART)], hw


def sk_lid(cx, ybed):
    # 94 wide; smooth top face on the bed, shallow element cavity opening up.
    hw, th, rhw, rd = 94 / 2 * S, 13, 64.8 / 2 * S, 7
    x0, x1, yp = cx - hw, cx + hw, ybed - th
    pts = [(x0, ybed), (x0, yp), (cx - rhw, yp), (cx - rhw, yp + rd),
           (cx + rhw, yp + rd), (cx + rhw, yp), (x1, yp), (x1, ybed)]
    return [poly(pts, FILL_BLACK_PART)], hw


def sk_insert(cx, ybed):
    hw, th = 64 / 2 * S, 7
    return [rect(cx - hw, ybed - th, 2 * hw, th, FILL_BLACK_PART, GREY, 2)], hw


def sk_mask(cx, ybed):
    hw, th = 94 / 2 * S, 5
    return [rect(cx - hw, ybed - th, 2 * hw, th, FILL_BLACK_PART, GREY, 2)], hw


# ---------------------------------------------------------------- card roster
# (file, sketch, desc key, is white part, amber warning)
CARDS = [
    ("main-body.stl",            sk_main_body,   "main-body", True,  False),
    ("cover-stage.stl",          sk_cover_stage, "cover-stage", True, False),
    ("film-holder-135-base.stl", sk_base,        "base", False, False),
    ("film-holder-135-lid.stl",  sk_lid,         "lid",  False, True),
    ("film-holder-120-base.stl", sk_base,        "base", False, False),
    ("film-holder-120-lid.stl",  sk_lid,         "lid",  False, True),
    ("pressure-window-135.stl",  sk_insert,      "insert", False, False),
    ("pressure-window-120.stl",  sk_insert,      "insert", False, False),
    ("mask-6x6.stl",             sk_mask,        "mask", False, False),
]


def down_arrow(x, y_top, y_tip):
    return [
        f'<line x1="{x:.1f}" y1="{y_top:.1f}" x2="{x:.1f}" y2="{y_tip - 9:.1f}"'
        f' stroke="{AMBER}" stroke-width="2.5"/>',
        poly([(x - 5, y_tip - 10), (x + 5, y_tip - 10), (x, y_tip)], AMBER,
             stroke="none", sw=0),
    ]


def build(lang):
    L = LANG[lang]
    e = []
    e.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
             f'viewBox="0 0 {W} {H}">')
    e.append(rect(0, 0, W, H, "#ffffff"))

    # title block
    e.append(T(MARGIN, 40, L["title"], size=21, bold=True))
    e.append(T(MARGIN, 60, L["subtitle"], size=12, fill=GREY))

    # banner strip
    e.append(rect(MARGIN, 72, W - 2 * MARGIN, 30, "#fbf0dd", AMBER, 1.2, rx=5))
    e.append(T(MARGIN + 14, 91, L["banner"], size=13, bold=True))
    # material legend, right end of banner
    lx = W - MARGIN - 14
    e.append(T(lx, 91, L["legend_black"], size=12, anchor="end", fill=GREY))
    e.append(circle(lx - 13 * len(L["legend_black"]) * 0.62 - 10, 87, 5,
                    FILL_BLACK_PART, GREY, 1))
    lx2 = lx - 13 * len(L["legend_black"]) * 0.62 - 30
    e.append(T(lx2, 91, L["legend_white"], size=12, anchor="end", fill=GREY))
    e.append(circle(lx2 - 13 * len(L["legend_white"]) * 0.62 - 10, 87, 5,
                    "#ffffff", GREY, 1))

    # cards
    for i, (fname, sketch, dkey, _is_white, warn) in enumerate(CARDS):
        col, row = i % 3, i // 3
        cx0 = MARGIN + col * (CARD_W + GAP_X)
        cy0 = GRID_TOP + row * (CARD_H + GAP_Y)

        border = AMBER if warn else "#cccccc"
        e.append(rect(cx0, cy0, CARD_W, CARD_H, "#ffffff", border,
                      2 if warn else 1, rx=6))

        # color chip + file name (monospace)
        chip_fill = "#ffffff" if _is_white else FILL_BLACK_PART
        e.append(circle(cx0 + 18, cy0 + 16, 5, chip_fill, GREY, 1))
        e.append(T(cx0 + 28, cy0 + 20, fname, size=12, mono=True))

        # amber warning badge
        if warn:
            e.append(circle(cx0 + CARD_W - 22, cy0 + 20, 10, AMBER))
            e.append(T(cx0 + CARD_W - 22, cy0 + 25, "!", size=14,
                       anchor="middle", fill="#ffffff", bold=True))

        # print bed: baseline + plate slab
        ybed = cy0 + 128
        bx, bw = cx0 + 18, CARD_W - 36
        e.append(rect(bx, ybed, bw, 6, BED_FILL, GREY, 1))

        # part sketch, shifted right to leave room for the arrow
        pcx = cx0 + CARD_W / 2 + 12
        shapes, halfw = sketch(pcx, ybed)
        # amber down-arrow pointing at the bed-contact face
        e += down_arrow(pcx - halfw - 18, ybed - 60, ybed - 2)
        e += shapes

        # one/two-line orientation caption (visible-feature wording)
        lines = L["desc"][dkey]
        y0 = cy0 + 153 if len(lines) > 1 else cy0 + 160
        for j, line in enumerate(lines):
            e.append(T(cx0 + CARD_W / 2, y0 + j * 17, line, size=12,
                       anchor="middle", bold=warn))

    # footer credit
    e.append(T(W - MARGIN, H - 10, L["footer"], size=12, anchor="end", fill=GREY))
    e.append("</svg>")
    return "\n".join(e) + "\n"


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    for lang in ("en", "zh", "ja"):
        path = os.path.join(OUT_DIR, f"print-orientation{LANG[lang]['suffix']}.svg")
        with open(path, "w", encoding="utf-8") as f:
            f.write(build(lang))
        print("wrote", path)


if __name__ == "__main__":
    main()
