#!/usr/bin/env python3
"""NeoBox v5 — optics / light-path section drawing generator.

Generates drawings/optics.svg (en), optics.zh-CN.svg, optics.ja.svg.
Side cross-section in the y-z plane (y = depth, z = height above table),
drawn to scale (S px per mm) for the box, flash and stack; camera is a
pictogram. All dimensions from FACTS-v5.md.
"""

import os

OUT_DIR = "/Users/lex/Developer/Neobox/drawings"
W, H = 960, 600
S = 1.85           # px per mm
XB = 210.0         # svg x of box rear outer face (world y = 0)
Y0 = 520.0         # svg y of table top (world z = 0)

AMBER = "#e8a33d"
INK = "#111"
EDGE = "#444"
SOFT = "#999"      # weakened outline for cover-stage / holder parts
FILL_BOX = "#f2f2f2"
FILL_GRAY = "#d9d9d9"
FILL_STAGE = "#ececec"
FILL_ELEM = "#c9c9c9"
FILL_FLASH = "#3a3a3a"
FILL_ACRYL = "#f8ead2"
EDGE_ACRYL = "#999"


def X(y):
    return round(XB + S * y, 2)


def Y(z):
    return round(Y0 - S * z, 2)


def rect(y0, z0, y1, z1, fill, stroke, sw):
    return (f'<rect x="{X(y0)}" y="{Y(z1)}" width="{round(S*(y1-y0),2)}" '
            f'height="{round(S*(z1-z0),2)}" fill="{fill}" stroke="{stroke}" '
            f'stroke-width="{sw}"/>')


def poly(pts, fill, stroke, sw):
    p = " ".join(f"{X(y)},{Y(z)}" for y, z in pts)
    return (f'<polygon points="{p}" fill="{fill}" stroke="{stroke}" '
            f'stroke-width="{sw}" stroke-linejoin="round"/>')


def wline(y0, z0, y1, z1, stroke, sw, dash=None, marker=None):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    m = f' marker-end="url(#{marker})"' if marker else ""
    return (f'<line x1="{X(y0)}" y1="{Y(z0)}" x2="{X(y1)}" y2="{Y(z1)}" '
            f'stroke="{stroke}" stroke-width="{sw}"{d}{m}/>')


def ray(y0, z0, y1, z1, sw=2.2):
    return wline(y0, z0, y1, z1, AMBER, sw, marker="ma")


def text(x, y, s, size=13, anchor="start", fill=INK, weight=None):
    w = f' font-weight="{weight}"' if weight else ""
    a = f' text-anchor="{anchor}"' if anchor != "start" else ""
    return f'<text x="{x}" y="{y}" font-size="{size}" fill="{fill}"{a}{w}>{s}</text>'


def dot(x, y):
    return (f'<circle cx="{x}" cy="{y}" r="2.2" fill="{EDGE}" '
            f'stroke="#ffffff" stroke-width="0.8"/>')


# ---------------------------------------------------------------- geometry --
def geometry():
    g = []

    # table baseline with hatch ticks
    g.append('<line x1="150" y1="520" x2="880" y2="520" '
             f'stroke="{EDGE}" stroke-width="2"/>')
    x = 158
    while x < 878:
        g.append(f'<line x1="{x}" y1="520" x2="{x-9}" y2="531" '
                 f'stroke="{SOFT}" stroke-width="1"/>')
        x += 22

    # main body section: bottom plate 0-3 (full 154.8 deep) + rear wall 2.4
    g.append(poly([(0, 0), (154.8, 0), (154.8, 3), (2.4, 3),
                   (2.4, 73), (0, 73)], FILL_BOX, EDGE, 2))

    # cover-stage plate 73-79 with 62x95 window and acrylic recess (weakened)
    g.append(poly([(0, 73), (29.9, 73), (29.9, 76.6), (17.9, 76.6),
                   (17.9, 79), (0, 79)], FILL_STAGE, SOFT, 1.2))
    g.append(poly([(124.9, 76.6), (136.9, 76.6), (136.9, 79), (154.8, 79),
                   (154.8, 73), (124.9, 73)], FILL_STAGE, SOFT, 1.2))
    # tray flange walls (79-83) around the film holder
    g.append(rect(14.1, 79, 17.1, 83, FILL_STAGE, SOFT, 1.2))
    g.append(rect(137.7, 79, 140.7, 83, FILL_STAGE, SOFT, 1.2))

    # opal acrylic 68x118x2 @ 76.6-78.6 (in-path part, warm tint)
    g.append(rect(18.4, 76.6, 136.4, 78.6, FILL_ACRYL, EDGE_ACRYL, 1.2))

    # film-holder base 79-84 (section shows the two ends; rim top = 83.2)
    g.append(poly([(17.4, 79), (34.9, 79), (34.9, 83.2), (30, 83.2),
                   (30, 82.8), (17.4, 82.8)], FILL_GRAY, SOFT, 1.2))
    g.append(poly([(119.9, 79), (137.4, 79), (137.4, 82.8), (124.8, 82.8),
                   (124.8, 83.2), (119.9, 83.2)], FILL_GRAY, SOFT, 1.2))

    # pressure element 64x95x2 on the 4.6 ledge (world 83.6-85.6)
    g.append(rect(29.9, 83.6, 34.9, 85.6, FILL_ELEM, SOFT, 1))
    g.append(rect(119.9, 83.6, 124.9, 85.6, FILL_ELEM, SOFT, 1))

    # holder lid 84-87 with element-relief cavity (top of cavity at 86)
    g.append(poly([(17.4, 84), (29.4, 84), (29.4, 86), (34.9, 86),
                   (34.9, 87), (17.4, 87)], FILL_GRAY, SOFT, 1.2))
    g.append(poly([(137.4, 84), (125.4, 84), (125.4, 86), (119.9, 86),
                   (119.9, 87), (137.4, 87)], FILL_GRAY, SOFT, 1.2))

    # flash lying on the table, head against the open front
    g.append(rect(154.8, 0, 344.8, 55, FILL_FLASH, "#222", 2))
    g.append(wline(216.8, 0, 216.8, 55, "#555", 1.2))
    # light face 60x45, centre 31 above table (amber band on the head front)
    g.append(rect(154.8, 8.5, 157.3, 53.5, AMBER, "none", 0))

    # film plane 83.2 (amber) with tails riding over the flange tops
    g.append(wline(8, 83.2, 147, 83.2, AMBER, 2.2))

    # camera pictogram above the stack (not to scale)
    g.append(rect(32.4, 152, 122.4, 180, FILL_GRAY, EDGE, 1.6))
    g.append(rect(65, 180, 90, 186, FILL_GRAY, EDGE, 1.6))
    g.append(rect(57.4, 118, 97.4, 152, "#cccccc", EDGE, 1.6))
    g.append(wline(57.4, 130, 97.4, 130, EDGE, 1))
    g.append(wline(57.4, 140, 97.4, 140, EDGE, 1))
    # optical axis, pointing down at the film plane
    g.append(wline(77.4, 117, 77.4, 85.5, EDGE, 1.2, dash="5,4", marker="md"))

    # ------------------------------------------------------- light path ----
    rays = [
        # entry: horizontal from the light face into the chamber
        (151, 31, 10, 31),
        (149, 36, 70, 53),
        (149, 26, 75, 10),
        # rear-wall bounces
        (6, 34, 48, 62),
        (6, 28, 40, 9),
        # floor bounce
        (78, 8, 98, 44),
        # risers through the light window + acrylic, up to the film plane
        (55, 56, 55, 81.3),
        (80, 58, 80, 81.3),
        (105, 54, 105, 81.3),
        # above the film plane, towards the camera
        (62, 85, 62, 103),
        (93, 85, 93, 103),
    ]
    for r in rays:
        g.append(ray(*r))

    # small y/z orientation cue
    g.append('<line x1="52" y1="556" x2="88" y2="556" stroke="#666" '
             'stroke-width="1.2" marker-end="url(#mg)"/>')
    g.append('<line x1="52" y1="556" x2="52" y2="522" stroke="#666" '
             'stroke-width="1.2" marker-end="url(#mg)"/>')
    g.append(text(94, 560, "y", 11, fill="#666"))
    g.append(text(48, 516, "z", 11, anchor="end", fill="#666"))
    return g


# ------------------------------------------------------------------ labels --
# left fan column: text right-aligned at x=196, bend at x=214
LEFT_ROWS = [
    ("camera",  268, (316, 270)),
    ("element", 320, (266, 362.5)),
    ("film",    346, (232, 366.1)),
    ("gap",     372, (246, 370.3)),
    ("acrylic", 398, (247, 376.5)),
    ("window",  424, (266, 381.3)),
    ("chamber", 456, (262, 440)),
]


def labels(L):
    g = []
    for key, ly, (tx, ty) in LEFT_ROWS:
        g.append(text(196, ly + 4, L[key], 13, anchor="end"))
        g.append(f'<polyline points="200,{ly} 214,{ly} {tx},{ty}" '
                 f'fill="none" stroke="{EDGE}" stroke-width="1"/>')
        g.append(dot(tx, ty))

    # right fan: open front / light face / flash
    g.append(text(600, 304, L["front"], 13))
    g.append(f'<polyline points="596,300 491,300 491,400" fill="none" '
             f'stroke="{EDGE}" stroke-width="1"/>')
    g.append(dot(491, 400))

    g.append(text(560, 332, L["face"], 13))
    g.append(f'<polyline points="556,328 502,328 499,422" fill="none" '
             f'stroke="{EDGE}" stroke-width="1"/>')
    g.append(dot(499, 422))

    g.append(text(640, 366, L["flash"], 13))
    g.append(f'<polyline points="810,372 810,415" fill="none" '
             f'stroke="{EDGE}" stroke-width="1"/>')
    g.append(dot(810, 415))
    return g


# -------------------------------------------------------------------- i18n --
LANG = {
    "en": {
        "file": "optics.svg",
        "title": "NeoBox v5 — Light Path (Section)",
        "sub": "Units: mm · box, flash and stack drawn to scale, camera pictorial · y–z section",
        "camera": "camera",
        "element": "pressure element",
        "film": "film plane (83.2)",
        "gap": "4.6 mm air gap",
        "acrylic": "opal acrylic 68×118×2",
        "window": "light window 62×95",
        "chamber": "white mixing chamber",
        "front": "open front",
        "face": "light face 60×45 (centre h. 31)",
        "flash": "flash (any hot-shoe unit)",
    },
    "zh": {
        "file": "optics.zh-CN.svg",
        "title": "NeoBox v5 — 光路示意（剖面）",
        "sub": "单位 mm · 箱体、闪光灯与叠层按比例，相机仅为示意 · y–z 剖面",
        "camera": "相机",
        "element": "压片元件",
        "film": "胶片平面（83.2）",
        "gap": "4.6mm 空气隙",
        "acrylic": "乳白亚克力 68×118×2",
        "window": "透光窗 62×95",
        "chamber": "白色混光腔",
        "front": "敞开前口",
        "face": "发光面 60×45（中心高 31）",
        "flash": "闪光灯（任意热靴灯）",
    },
    "ja": {
        "file": "optics.ja.svg",
        "title": "NeoBox v5 — 光路図（断面）",
        "sub": "単位 mm · 箱・ストロボ・積層は縮尺どおり、カメラは模式 · y–z 断面",
        "camera": "カメラ",
        "element": "押さえエレメント",
        "film": "フィルム面（83.2）",
        "gap": "空気層 4.6mm",
        "acrylic": "乳白アクリル 68×118×2",
        "window": "採光窓 62×95",
        "chamber": "白色拡散チャンバー",
        "front": "オープンフロント（前面開口）",
        "face": "発光面 60×45（中心高さ 31）",
        "flash": "ストロボ（任意のホットシューストロボ）",
    },
}


def build(L):
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
        f'viewBox="0 0 {W} {H}" font-family="Helvetica, Arial, sans-serif">',
        f'<rect width="{W}" height="{H}" fill="#ffffff"/>',
        '<defs>',
        '<marker id="ma" viewBox="0 0 10 10" refX="8" refY="5" '
        'markerWidth="6.5" markerHeight="6.5" orient="auto">'
        f'<path d="M0,0 L10,5 L0,10 z" fill="{AMBER}"/></marker>',
        '<marker id="md" viewBox="0 0 10 10" refX="8" refY="5" '
        'markerWidth="6" markerHeight="6" orient="auto">'
        f'<path d="M0,0 L10,5 L0,10 z" fill="{EDGE}"/></marker>',
        '<marker id="mg" viewBox="0 0 10 10" refX="8" refY="5" '
        'markerWidth="5.5" markerHeight="5.5" orient="auto">'
        '<path d="M0,0 L10,5 L0,10 z" fill="#666"/></marker>',
        '</defs>',
    ]
    parts += geometry()
    parts += labels(L)
    parts.append(text(24, 40, L["title"], 21, weight="bold"))
    parts.append(text(24, 60, L["sub"], 12, fill="#555"))
    parts.append(text(W - 24, H - 14, "NeoBox v5 — 2026-08", 12,
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
