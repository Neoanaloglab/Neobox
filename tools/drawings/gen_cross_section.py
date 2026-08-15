#!/usr/bin/env python3
"""NeoBox v1 — cross-section drawing generator.

Generates drawings/cross-section.svg (en), .zh-CN.svg, .ja.svg.
Main view: full x-z section through the centre, to scale (S px/mm),
world z with table top = 0. Right inset: film-flattening detail in
holder-local z with exaggerated vertical scale. All numbers from
FACTS-v5.md.
"""

import os

OUT_DIR = "/Users/lex/Developer/Neobox/drawings"
W, H = 990, 530

# ---- main view transform (world mm -> px) ----
S = 3.0            # px per mm
XL = 190.0         # svg x of box left outer face (world x = 0)
Y0 = 430.0         # svg y of table top (world z = 0)
CXW = 62.4         # world x of the box centre

# ---- inset transform (holder-local mm -> px) ----
IX0, IY0, IW, IH = 630.0, 112.0, 348.0, 372.0   # inset frame
GCX = 720.0        # svg x of channel centre
GY0 = 500.0        # svg y of holder-local z = 0
HS = 2.3           # inset horizontal px/mm
VS = 30.0          # inset vertical px/mm (exaggerated)
XEXT = 816.0       # right end of the inset level hairlines

AMBER = "#e8a33d"
INK = "#111"
EDGE = "#444"
FILL_BOX = "#f2f2f2"     # white printed part (main body)
FILL_STAGE = "#ececec"   # white printed part (cover-stage)
FILL_DARK = "#3f3f3f"    # black printed parts (holder base / lid)
FILL_ELEM = "#262626"    # black pressure element
EDGE_DARK = "#1a1a1a"
FILL_ACRYL = "#f8ead2"
FILL_SHIM = "#9a9a9a"
HIDD = "#777"            # hidden (out-of-plane) features


def px(x):
    return round(XL + S * x, 2)


def py(z):
    return round(Y0 - S * z, 2)


def gx(u):
    return round(GCX + HS * u, 2)


def gy(z):
    return round(GY0 - VS * z, 2)


def poly_pts(pts):
    return " ".join(f"{p[0]},{p[1]}" for p in pts)


def poly(pts_px, fill, stroke, sw, dash=None):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    return (f'<polygon points="{poly_pts(pts_px)}" fill="{fill}" '
            f'stroke="{stroke}" stroke-width="{sw}"{d} '
            f'stroke-linejoin="round"/>')


def wpoly(pts_w, fill, stroke, sw, dash=None):
    return poly([(px(x), py(z)) for x, z in pts_w], fill, stroke, sw, dash)


def wrect(x0, z0, x1, z1, fill, stroke, sw, dash=None):
    return wpoly([(x0, z0), (x1, z0), (x1, z1), (x0, z1)],
                 fill, stroke, sw, dash)


def line(x0, y0, x1, y1, stroke, sw, dash=None, ms=None, me=None):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    a = f' marker-start="url(#{ms})"' if ms else ""
    b = f' marker-end="url(#{me})"' if me else ""
    return (f'<line x1="{x0}" y1="{y0}" x2="{x1}" y2="{y1}" '
            f'stroke="{stroke}" stroke-width="{sw}"{d}{a}{b}/>')


def wline(xa, za, xb, zb, stroke, sw, dash=None):
    return line(px(xa), py(za), px(xb), py(zb), stroke, sw, dash)


def text(x, y, s, size=13, anchor="start", fill=INK, weight=None, rot=None):
    w = f' font-weight="{weight}"' if weight else ""
    a = f' text-anchor="{anchor}"' if anchor != "start" else ""
    r = f' transform="rotate(-90 {x} {y})"' if rot else ""
    return (f'<text x="{x}" y="{y}" font-size="{size}" '
            f'fill="{fill}"{a}{w}{r}>{s}</text>')


def dot(x, y):
    return (f'<circle cx="{x}" cy="{y}" r="2.2" fill="{EDGE}" '
            f'stroke="#ffffff" stroke-width="0.8"/>')


def mirror(pts):
    return [(2 * CXW - x, z) for x, z in pts]


# ---- shared holder half-profiles (u from channel centre, holder-local z) --
def base_half(c, zb=0.0):
    """Half section of the 135 base: window edge 12.5, seat 4.2,
    plate face 3.8, element ledge 31..32.2 @4.6, rail 32.2..33.5 @5.0.
    zb > 0 crops the plate bottom (inset detail view)."""
    return [(12.5, zb), (c, zb), (c, 3.8), (33.5, 3.8), (33.5, 5.0),
            (32.2, 5.0), (32.2, 4.6), (31.0, 4.6), (31.0, 3.8),
            (19.7, 3.8), (19.7, 4.2), (12.5, 4.2)]


def lid_half(c):
    """Half section of the lid (assembly z): base 5.0, cavity to 32.4
    with ceiling 7.0, top 8.0, window edge 12.5."""
    return [(12.5, 8.0), (c, 8.0), (c, 5.0), (32.4, 5.0),
            (32.4, 7.0), (12.5, 7.0)]


def holder_world(half):
    """Both halves of a holder profile in world coords (z + 79)."""
    out = []
    for sgn in (1, -1):
        out.append([(CXW + sgn * u, 79 + z) for u, z in half])
    return out


# left cover-stage plate piece incl. flange, acrylic recess, shim pocket
PLATE_L = [(0, 73), (31.4, 73), (31.4, 76.6), (27.9, 76.6), (27.9, 79),
           (26.7, 79), (26.7, 78), (16.1, 78), (16.1, 79), (15.1, 79),
           (15.1, 83), (12.1, 83), (12.1, 79), (0, 79)]


# ------------------------------------------------------------ main view ----
def geometry_main():
    g = []
    # table baseline + hatch
    g.append(line(60, Y0, 622, Y0, EDGE, 2))
    x = 74
    while x < 618:
        g.append(line(x, Y0, x - 9, Y0 + 11, "#999", 1))
        x += 22
    # main body: bottom plate 0-3 + side walls 2.4 thick to 73
    g.append(wpoly([(0, 0), (124.8, 0), (124.8, 73), (122.4, 73),
                    (122.4, 3), (2.4, 3), (2.4, 73), (0, 73)],
                   FILL_BOX, EDGE, 2))
    # locating tenons (at corner positions, out of the cut plane -> dashed)
    for r in (wrect(0, 73, 2.4, 75.6, "none", HIDD, 1.1, dash="4,3"),
              wrect(122.4, 73, 124.8, 75.6, "none", HIDD, 1.1, dash="4,3")):
        g.append(r)
    # cover-stage plate 73-79 with flange 79-83 (one piece, both sides)
    g.append(wpoly(PLATE_L, FILL_STAGE, EDGE, 1.6))
    g.append(wpoly(mirror(PLATE_L), FILL_STAGE, EDGE, 1.6))
    # tenon notch roofs in the plate underside (hidden -> dashed)
    for x0, x1 in ((0, 2.9), (121.9, 124.8)):
        g.append(wline(x0, 75.8, x1, 75.8, HIDD, 1.1, dash="4,3"))
    # opal acrylic 68x118x2 in its recess, top 0.4 below the deck
    g.append(wrect(28.4, 76.6, 96.4, 78.6, FILL_ACRYL, "#999", 1.2))
    # steel shims 10x10x1 flush with the deck (pockets 78-79)
    g.append(wrect(16.4, 78, 26.4, 79, FILL_SHIM, "#555", 1))
    g.append(wrect(98.4, 78, 108.4, 79, FILL_SHIM, "#555", 1))
    # film-holder base 79-84 (black), then element, then lid 84-87
    for p in holder_world(base_half(47)):
        g.append(wpoly(p, FILL_DARK, EDGE_DARK, 1.2))
    g.append(wrect(CXW - 32, 83.6, CXW + 32, 85.6, FILL_ELEM, EDGE_DARK, 1))
    for p in holder_world(lid_half(47)):
        g.append(wpoly(p, FILL_DARK, EDGE_DARK, 1.2))
    # film plane 83.2 — amber dashed, spanning past the box to the dims
    g.append(line(186, py(83.2), 610, py(83.2), AMBER, 2, dash="7,5"))
    return g


# fan labels, left column: (key, label_y, target_x, target_y)
ROWS = [("lid", 132, 250, 173),
        ("tenon", 206, 193.6, 207),
        ("stage", 230, 200, 204),
        ("flange", 254, 230.5, 184),
        ("base", 278, 240, 187),
        ("shim", 302, 254, 194.5),
        ("acrylic", 326, 300, 197.2),
        ("wall", 350, 193.6, 352),
        ("bottom", 424, 240, 425.5)]


def labels_main(L):
    g = []
    for key, ly, tx, ty in ROWS:
        g.append(text(178, ly + 4, L[key], 13, anchor="end"))
        g.append(f'<polyline points="182,{ly} 188,{ly} {tx},{ty}" '
                 f'fill="none" stroke="{EDGE}" stroke-width="1"/>')
        g.append(dot(tx, ty))
    # film plane label sits directly on the amber line extension
    g.append(text(178, py(83.2) + 4, L["film"], 13, anchor="end"))
    # open-front note inside the empty chamber
    g.append(f'<circle cx="377" cy="266" r="7" fill="none" stroke="{EDGE}" '
             'stroke-width="1.4"/>')
    g.append(f'<circle cx="377" cy="266" r="1.8" fill="{EDGE}"/>')
    g.append(text(377, 292, L["ofront1"], 13, anchor="middle"))
    g.append(text(377, 310, L["ofront2"], 11.5, anchor="middle", fill="#555"))
    return g


def dims_main():
    g = []
    # vertical chains on the right: 73 / 83.2 / 87 (from table z=0)
    g.append(line(px(124.8) + 2, py(73), 584, py(73), "#666", 0.9))
    g.append(line(520, py(87), 624, py(87), "#666", 0.9))
    for z, col, lab in ((73, 578, "73"), (83.2, 598, "83.2"), (87, 618, "87")):
        g.append(line(col, py(z), col, Y0, EDGE, 1, ms="ds", me="de"))
        g.append(text(col - 4, (py(z) + Y0) / 2, lab, 13,
                      anchor="middle", rot=True))
    # outer width 124.8 below the table
    for xw in (0, 124.8):
        g.append(line(px(xw), Y0 + 3, px(xw), 463, "#666", 0.9))
    g.append(line(px(0), 457, px(124.8), 457, EDGE, 1, ms="ds", me="de"))
    g.append(text((px(0) + px(124.8)) / 2, 452, "124.8", 13, anchor="middle"))
    # cavity width 120 inside the chamber
    g.append(line(px(2.4), 396, px(122.4), 396, EDGE, 1, ms="ds", me="de"))
    g.append(text((px(2.4) + px(122.4)) / 2, 391, "120", 13, anchor="middle"))
    # scale bar 0-50 mm (5 x 10 mm blocks)
    for i in range(5):
        f = EDGE if i % 2 == 0 else "#ffffff"
        g.append(f'<rect x="{60 + 30 * i}" y="494" width="30" height="6" '
                 f'fill="{f}" stroke="{EDGE}" stroke-width="1"/>')
    g.append(text(60, 490, "0", 10, anchor="middle", fill="#555"))
    g.append(text(210, 490, "50 mm", 10, anchor="middle", fill="#555"))
    return g


# -------------------------------------------------------------- inset -----
# rows: (key, z_level, hairline_start_u or None, amber?) — None = dot target
IROWS = [("i70", 7.0, 14, 0),
         ("i04f", 6.8, 16, 1),
         ("iel", 5.6, None, 0),
         ("i50", 5.0, 32.6, 0),
         ("i46", 4.6, 20, 0),
         ("i04c", 4.4, 17.6, 1),
         ("ifm", 4.36, 0, 0),
         ("ist", 4.2, 18.4, 0),
         ("i38", 3.8, 24, 0)]


def gpoly(pts, fill, stroke, sw):
    return poly([(gx(u), gy(z)) for u, z in pts], fill, stroke, sw)


def inset(L):
    g = []
    g.append(f'<rect x="{IX0}" y="{IY0}" width="{IW}" height="{IH}" rx="10" '
             f'fill="#ffffff" stroke="{EDGE}" stroke-width="1.4"/>')
    g.append(text(IX0 + 16, IY0 + 26, L["cap"], 14, weight="bold"))
    g.append(text(IX0 + 16, IY0 + 44, L["capsub"], 11, fill="#555"))
    # geometry: base halves, film, element, lid halves
    for sgn in (1, -1):
        g.append(gpoly([(sgn * u, z) for u, z in base_half(36, 2.6)],
                       FILL_DARK, EDGE_DARK, 1.2))
    g.append(gpoly([(-17.5, 4.2), (17.5, 4.2), (17.5, 4.36), (-17.5, 4.36)],
                   AMBER, "none", 0))
    g.append(gpoly([(-32, 4.6), (32, 4.6), (32, 6.6), (-32, 6.6)],
                   FILL_ELEM, EDGE_DARK, 1))
    for sgn in (1, -1):
        g.append(gpoly([(sgn * u, z) for u, z in lid_half(36)],
                       FILL_DARK, EDGE_DARK, 1.2))
    # level hairlines + fan labels down the right side
    for i, (key, z, u0, amber) in enumerate(IROWS):
        ly = 250 + 24 * i
        col = AMBER if amber else INK
        if u0 is None:                       # dot directly on the element
            tx, ty = gx(22), gy(z)
        else:
            tx, ty = XEXT, gy(z)
            hl = AMBER if amber else "#aaa"
            g.append(line(gx(u0), gy(z), XEXT, gy(z), hl,
                          1.1 if amber else 0.9, dash="3,3"))
        g.append(dot(tx, ty))
        g.append(f'<polyline points="832,{ly} 826,{ly} '
                 f'{tx + (1 if u0 else 2)},{ty}" fill="none" '
                 f'stroke="{EDGE}" stroke-width="1"/>')
        g.append(text(836, ly + 4, L[key], 12.5, fill=col,
                      weight="bold" if amber else None))
    return g


def callout():
    """Dashed detail box on the main view + connector to the inset."""
    g = [f'<rect x="232" y="157" width="294" height="48" rx="8" fill="none" '
         f'stroke="{AMBER}" stroke-width="1.3" stroke-dasharray="6,4"/>',
         f'<polyline points="526,157 564,126 {IX0},126" fill="none" '
         f'stroke="{AMBER}" stroke-width="1.2" stroke-dasharray="6,4"/>']
    return g


# ---------------------------------------------------------------- i18n -----
LANG = {
    "en": {
        "file": "cross-section.svg",
        "title": "NeoBox v1 — Cross-Section (x–z)",
        "sub": "Units: mm · main view to scale (bar below) · section through "
               "the centre · heights = world z, table top = 0",
        "lid": "holder lid 84–87",
        "film": "film plane 83.2",
        "tenon": "locating tenons ×4 (75.6)",
        "stage": "cover-stage plate 73–79",
        "flange": "tray flange (top 83)",
        "base": "film-holder base 79–84",
        "shim": "steel shim, pocket 78–79",
        "acrylic": "opal acrylic 76.6–78.6",
        "wall": "side wall t 2.4",
        "bottom": "bottom plate 0–3",
        "ofront1": "open front (face fully open)",
        "ofront2": "towards the viewer; flash fires in from here",
        "cap": "Detail: film-flattening system (135 holder)",
        "capsub": "z = holder-local (world z = local + 79) · "
                  "vertical scale exaggerated",
        "i70": "cavity ceiling 7.0",
        "i04f": "0.4 float",
        "iel": "pressure element, t 2",
        "i50": "rail top / lid base 5.0",
        "i46": "element ledge 4.6",
        "i04c": "0.4 channel",
        "ifm": "film 4.32–4.38",
        "ist": "film seat 4.2",
        "i38": "plate face 3.8",
    },
    "zh": {
        "file": "cross-section.zh-CN.svg",
        "title": "NeoBox v1 — 整机剖面（x–z）",
        "sub": "单位 mm · 主图按比例（见左下比例尺）· 过中心剖切 · "
               "标高为世界 z，桌面 = 0",
        "lid": "夹上盖 84–87",
        "film": "胶片平面 83.2",
        "tenon": "定位榫 ×4（顶 75.6）",
        "stage": "顶盖台（板 73–79）",
        "flange": "托盘凸缘（顶 83）",
        "base": "胶片夹底座 79–84",
        "shim": "钢垫片（沉孔 78–79）",
        "acrylic": "乳白亚克力 76.6–78.6",
        "wall": "侧壁 厚 2.4",
        "bottom": "底板 0–3",
        "ofront1": "敞开前口（前面全开）",
        "ofront2": "朝向读者，闪光灯由此打光",
        "cap": "放大：压平系统（135 夹）",
        "capsub": "z 为夹局部坐标（世界 z = 局部 + 79）· 纵向放大示意",
        "i70": "限位腔顶 7.0",
        "i04f": "0.4 浮动",
        "iel": "压片元件 厚 2",
        "i50": "导轨顶 / 上盖底 5.0",
        "i46": "元件台阶 4.6",
        "i04c": "0.4 通道",
        "ifm": "胶片 4.32–4.38",
        "ist": "承台 4.2",
        "i38": "底板顶 3.8",
    },
    "ja": {
        "file": "cross-section.ja.svg",
        "title": "NeoBox v1 — 全体断面図（x–z）",
        "sub": "単位 mm · 主図は縮尺どおり（左下スケールバー）· 中心断面 · "
               "高さは世界 z、机上面 = 0",
        "lid": "上蓋 84–87",
        "film": "フィルム面 83.2",
        "tenon": "位置決めダボ ×4（75.6）",
        "stage": "天板ステージ 73–79",
        "flange": "フランジ（上端 83）",
        "base": "ホルダー基部 79–84",
        "shim": "鋼シム（座ぐり78–79）",
        "acrylic": "乳白アクリル 76.6–78.6",
        "wall": "側壁 厚 2.4",
        "bottom": "底板 0–3",
        "ofront1": "オープンフロント（前面開口）",
        "ofront2": "手前側。ストロボはここから照射",
        "cap": "詳細：平面化システム（135 ホルダー）",
        "capsub": "z はホルダー基準（世界 z = +79）· 縦方向は誇張表示",
        "i70": "キャビティ天井 7.0",
        "i04f": "0.4 浮き",
        "iel": "押さえエレメント 厚2",
        "i50": "レール上面＝上蓋底 5.0",
        "i46": "エレメント段 4.6",
        "i04c": "0.4 通路",
        "ifm": "フィルム 4.32–4.38",
        "ist": "フィルム座面 4.2",
        "i38": "基部上面 3.8",
    },
}


def build(L):
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
        f'viewBox="0 0 {W} {H}" font-family="Helvetica, Arial, sans-serif">',
        f'<rect width="{W}" height="{H}" fill="#ffffff"/>',
        '<defs>',
        '<marker id="de" viewBox="0 0 10 10" refX="9" refY="5" '
        'markerWidth="7" markerHeight="7" orient="auto">'
        f'<path d="M0,1.5 L10,5 L0,8.5 z" fill="{EDGE}"/></marker>',
        '<marker id="ds" viewBox="0 0 10 10" refX="1" refY="5" '
        'markerWidth="7" markerHeight="7" orient="auto">'
        f'<path d="M10,1.5 L0,5 L10,8.5 z" fill="{EDGE}"/></marker>',
        '</defs>',
    ]
    parts += geometry_main()
    parts += callout()
    parts += dims_main()
    parts += labels_main(L)
    parts += inset(L)
    parts.append(text(24, 40, L["title"], 21, weight="bold"))
    parts.append(text(24, 60, L["sub"], 12, fill="#555"))
    parts.append(text(W - 24, H - 14, "NeoBox v1 — 2026-08", 12,
                      anchor="end", fill="#888"))
    parts.append('</svg>')
    return "\n".join(parts) + "\n"


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    for L in LANG.values():
        path = os.path.join(OUT_DIR, L["file"])
        with open(path, "w", encoding="utf-8") as f:
            f.write(build(L))
        print("wrote", path)


if __name__ == "__main__":
    main()
