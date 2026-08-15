#!/usr/bin/env python3
"""NeoBox v5 — spectral-response drawing generator (flash vs LED).

Generates drawings/spectral-response.svg (en), .zh-CN.svg, .ja.svg.
Panel 1: schematic spectral power distribution 400-700 nm, xenon flash
(continuous) vs typical white LED (blue pump + phosphor), with the three
colour-negative dye-layer bands under the axis.  Panel 2: time domain,
flash pulse vs continuous-LED long exposure.  Data: FACTS-v5.md section 5b
(textbook-typical curves, explicitly labelled schematic, not measured).
"""

import os

OUT_DIR = "/Users/lex/Developer/Neobox/drawings"
W, H = 980, 640

AMBER = "#e8a33d"
INK = "#111"
EDGE = "#444"
GRAY = "#666"
LED_C = "#555"

# spectral plot area
PX0, PX1 = 270.0, 690.0          # 400 nm .. 700 nm
PY0, PH = 384.0, 244.0           # baseline (p=0) and height (p=1)


def lx(nm):
    return round(PX0 + (nm - 400.0) * (PX1 - PX0) / 300.0, 1)


def py(p):
    return round(PY0 - PH * p, 1)


def text(x, y, s, size=13, anchor="start", fill=INK, weight=None):
    w = f' font-weight="{weight}"' if weight else ""
    a = f' text-anchor="{anchor}"' if anchor != "start" else ""
    return f'<text x="{x}" y="{y}" font-size="{size}" fill="{fill}"{a}{w}>{s}</text>'


def line(x0, y0, x1, y1, stroke, swid, dash=None, marker=None):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    m = f' marker-end="url(#{marker})"' if marker else ""
    return (f'<line x1="{x0}" y1="{y0}" x2="{x1}" y2="{y1}" '
            f'stroke="{stroke}" stroke-width="{swid}"{d}{m}/>')


def dot(x, y):
    return (f'<circle cx="{x}" cy="{y}" r="2.2" fill="{EDGE}" '
            f'stroke="#ffffff" stroke-width="0.8"/>')


def smooth(pts):
    """Catmull-Rom -> cubic bezier path through svg-coordinate points."""
    d = f"M{pts[0][0]},{pts[0][1]}"
    n = len(pts)
    for i in range(n - 1):
        p0 = pts[max(i - 1, 0)]
        p1, p2 = pts[i], pts[i + 1]
        p3 = pts[min(i + 2, n - 1)]
        c1 = (p1[0] + (p2[0] - p0[0]) / 6.0, p1[1] + (p2[1] - p0[1]) / 6.0)
        c2 = (p2[0] - (p3[0] - p1[0]) / 6.0, p2[1] - (p3[1] - p1[1]) / 6.0)
        d += (f" C{c1[0]:.1f},{c1[1]:.1f} {c2[0]:.1f},{c2[1]:.1f} "
              f"{p2[0]:.1f},{p2[1]:.1f}")
    return d


def curve(pts_nm, stroke, dash=None):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    pts = [(lx(nm), py(p)) for nm, p in pts_nm]
    return (f'<path d="{smooth(pts)}" fill="none" stroke="{stroke}" '
            f'stroke-width="2.6" stroke-linecap="round"{d}/>')


def label(lines, row_y, target, side):
    """Fan label: text column outside the plot + one bent leader + dot.
    side 'L': right-aligned at x=245, bend 262.  'R': start at 725, bend 708."""
    g = []
    for i, s in enumerate(lines):
        if side == "L":
            g.append(text(245, row_y + i * 18, s, 13, anchor="end"))
        else:
            g.append(text(725, row_y + i * 18, s, 13))
    ly = row_y - 4
    tx, ty = target
    if side == "L":
        g.append(f'<polyline points="249,{ly} 262,{ly} {tx},{ty}" '
                 f'fill="none" stroke="{EDGE}" stroke-width="1"/>')
    else:
        g.append(f'<polyline points="721,{ly} 708,{ly} {tx},{ty}" '
                 f'fill="none" stroke="{EDGE}" stroke-width="1"/>')
    g.append(dot(tx, ty))
    return g


# typical white LED: 450 nm blue spike -> ~480 nm cyan gap -> phosphor
# hump 550-620 -> deep-red roll-off past ~630 (FACTS 5b, schematic)
LED_PTS = [
    (400, .02), (412, .02), (424, .05), (434, .14), (442, .50), (447, .88),
    (450, .97), (453, .88), (458, .55), (466, .33), (474, .25), (482, .22),
    (492, .25), (505, .34), (525, .52), (545, .68), (565, .76), (585, .77),
    (605, .72), (625, .60), (640, .45), (655, .28), (670, .15), (685, .07),
    (700, .04),
]

# xenon flash: continuous 400-700, gentle undulation, mild decline at the
# red end (FACTS 5b, schematic)
FLASH_PTS = [
    (400, .62), (430, .72), (460, .80), (490, .845), (520, .82), (550, .86),
    (580, .835), (610, .80), (640, .78), (670, .735), (700, .66),
]

# RGB-mixed white (three-colour LED): narrow spikes ~455/525/630 nm,
# FWHM 20-30 nm, near-zero between the peaks (schematic)
RGB_PTS = [
    (400, .01), (418, .01), (428, .02), (435, .08), (444, .34), (455, .68),
    (466, .34), (475, .08), (484, .02), (492, .01), (500, .01), (508, .04),
    (514, .31), (525, .62), (536, .31), (542, .04), (550, .01), (565, .01),
    (580, .01), (590, .01), (598, .01), (606, .04), (618, .33), (630, .66),
    (642, .33), (654, .04), (662, .01), (680, .01), (700, .01),
]

DYE_BANDS = [  # (nm0, nm1, fill)  blue / green / red working bands
    (400, 500, "#dce8f7"),
    (500, 600, "#dcefdc"),
    (600, 700, "#f7dcdc"),
]

LANG = {
    "en": {
        "file": "spectral-response.svg",
        "title": "NeoBox v5 — Why a Flash: Spectrum &amp; Time",
        "sub": "Schematic — typical spectra, not measurements · x: wavelength 400–700 nm · y: relative spectral power (0–1, unitless)",
        "legend_flash": "xenon flash (continuous spectrum)",
        "legend_led": "typical white LED (blue pump + phosphor)",
        "legend_rgb": "RGB-mixed white",
        "ynote": "relative spectral power (0–1)",
        "schem": "schematic — typical spectra, not measured",
        "spec_head": "1 · Spectral domain",
        "time_head": "2 · Time domain — pulse vs real shutter",
        "band_cap": "colour-negative dye layers",
        "dyes": [["yellow dye layer", "(absorbs blue)"],
                 ["magenta dye layer", "(absorbs green)"],
                 ["cyan dye layer", "(absorbs red)"]],
        "spike": ["LED: blue spike at 450 nm"],
        "cyan": ["cyan gap (~480 nm)"],
        "flashlab": ["xenon flash: CRI ≥95, strong R9", "(5500–6000 K, near daylight)"],
        "cover": ["flash: continuous coverage of", "all three dye-layer bands"],
        "rolloff": ["deep-red roll-off past ~630 nm", "(weak R9 is common)"],
        "rgbw": ["RGB-mixed white: nothing", "sampled between the spikes"],
        "pulse": ["flash pulse", "1/1,000–1/20,000 s"],
        "pulse_note": "= the pulse is the shutter (vibration-immune)",
        "led": ["continuous-LED exposure", "1/15–1/60 s @ ISO 100 f/8"],
        "shake": ["rig vibration &amp; shutter shock", "all recorded in the frame"],
    },
    "zh": {
        "file": "spectral-response.zh-CN.svg",
        "title": "NeoBox v5 — 为什么是闪光灯：光谱与时间域",
        "sub": "示意图——典型光谱而非实测 · 横轴：波长 400–700nm · 纵轴：相对光谱功率（0–1，无单位）",
        "legend_flash": "氙气闪光（连续光谱）",
        "legend_led": "典型白光 LED（蓝泵浦＋荧光粉）",
        "legend_rgb": "RGB 混光白",
        "ynote": "相对光谱功率（0–1）",
        "schem": "示意图——典型光谱，非实测",
        "spec_head": "① 光谱域",
        "time_head": "② 时间域——脉冲 vs 真实快门",
        "band_cap": "彩负三层染料的工作波段",
        "dyes": [["黄染料层", "（吸蓝）"],
                 ["品红染料层", "（吸绿）"],
                 ["青染料层", "（吸红）"]],
        "spike": ["LED：450nm 蓝色尖峰"],
        "cyan": ["青色谷（cyan gap，~480nm）"],
        "flashlab": ["氙气闪光：CRI ≥95・R9 强", "（色温 5500–6000K，近日光）"],
        "cover": ["闪光：连续覆盖全部", "三个染料层波段"],
        "rolloff": ["630nm 后深红滚降", "（R9 常见偏弱）"],
        "rgbw": ["RGB 混光白：峰间整段无采样"],
        "pulse": ["闪光脉冲", "1/1,000–1/20,000 s"],
        "pulse_note": "＝脉冲即快门（振动免疫）",
        "led": ["连续 LED 长曝光", "1/15–1/60 s @ ISO 100 f/8"],
        "shake": ["架子振动/快门震动", "全部入镜"],
    },
    "ja": {
        "file": "spectral-response.ja.svg",
        "title": "NeoBox v5 — なぜストロボか：スペクトルと時間",
        "sub": "模式図——実測ではなく典型スペクトル · 横軸：波長 400–700nm · 縦軸：相対分光パワー（0–1・無単位）",
        "legend_flash": "キセノン閃光（連続スペクトル）",
        "legend_led": "典型的な白色 LED（青ポンプ＋蛍光体）",
        "legend_rgb": "RGB 合成白",
        "ynote": "相対分光パワー（0–1）",
        "schem": "模式図——典型スペクトル（実測ではない）",
        "spec_head": "① スペクトル領域",
        "time_head": "② 時間領域——パルス vs 実シャッター",
        "band_cap": "カラーネガ３層の色素帯域",
        "dyes": [["イエロー色素層", "（青を吸収）"],
                 ["マゼンタ色素層", "（緑を吸収）"],
                 ["シアン色素層", "（赤を吸収）"]],
        "spike": ["LED：450nm の青色ピーク"],
        "cyan": ["シアンの谷（cyan gap, ~480nm）"],
        "flashlab": ["キセノン閃光：CRI ≥95・R9 が強い", "（色温度 5500–6000K・昼光に近い）"],
        "cover": ["3 つの色素層の帯域を", "連続スペクトルで完全カバー"],
        "rolloff": ["630nm 以降の深赤ロールオフ", "（R9 が弱い個体が多い）"],
        "rgbw": ["RGB 合成白：ピークの間は", "全くサンプリングされない"],
        "pulse": ["閃光パルス", "1/1,000–1/20,000 s"],
        "pulse_note": "＝パルスがシャッター（振動に強い）",
        "led": ["連続 LED の長時間露光", "1/15–1/60 s @ ISO 100 f/8"],
        "shake": ["架台の振動・シャッターショックが", "すべて写り込む"],
    },
}


def build(L):
    g = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
        f'viewBox="0 0 {W} {H}" font-family="Helvetica, Arial, sans-serif">',
        f'<rect width="{W}" height="{H}" fill="#ffffff"/>',
        '<defs>',
        '<marker id="mg" viewBox="0 0 10 10" refX="8" refY="5" '
        'markerWidth="5.5" markerHeight="5.5" orient="auto">'
        '<path d="M0,0 L10,5 L0,10 z" fill="#666"/></marker>',
        '</defs>',
    ]
    # ---- header ----
    g.append(text(24, 40, L["title"], 21, weight="bold"))
    g.append(text(24, 60, L["sub"], 12, fill="#555"))
    # legend row
    g.append(line(200, 96, 230, 96, AMBER, 3))
    g.append(text(236, 100, L["legend_flash"], 13))
    g.append(line(470, 96, 500, 96, LED_C, 3))
    g.append(text(506, 100, L["legend_led"], 13))
    g.append(line(790, 96, 820, 96, "#999", 3, dash="7,5"))
    g.append(text(826, 100, L["legend_rgb"], 13))

    # ---- panel 1: spectral domain ----
    g.append(text(24, 128, L["spec_head"], 14, weight="bold"))
    g.append(text(280, 128, L["ynote"], 11.5, fill=GRAY))
    # axes
    g.append(line(PX0, PY0, 702, PY0, GRAY, 1.4, marker="mg"))
    g.append(line(PX0, PY0, PX0, 130, GRAY, 1.4, marker="mg"))
    g.append(text(708, 388, "λ (nm)", 11.5, fill=GRAY))
    for nm in range(400, 701, 50):
        x = lx(nm)
        g.append(line(x, PY0, x, PY0 + 6, GRAY, 1))
        g.append(text(x, 404, str(nm), 11.5, anchor="middle", fill=GRAY))
    for p, s in ((0.0, "0"), (0.5, "0.5"), (1.0, "1.0")):
        g.append(line(PX0 - 6, py(p), PX0, py(p), GRAY, 1))
        g.append(text(PX0 - 10, py(p) + 4, s, 11.5, anchor="end", fill=GRAY))
    # dye-layer working bands under the axis
    for (nm0, nm1, fill), (l1, l2) in zip(DYE_BANDS, L["dyes"]):
        x0, x1 = lx(nm0), lx(nm1)
        g.append(f'<rect x="{x0}" y="414" width="{round(x1-x0,1)}" '
                 f'height="26" fill="{fill}" stroke="#bbbbbb" '
                 f'stroke-width="0.8"/>')
        cx = round((x0 + x1) / 2, 1)
        g.append(text(cx, 431, l1, 12, anchor="middle", fill="#333"))
        g.append(text(cx, 458, l2, 12, anchor="middle", fill="#333"))
    g.append(text(258, 431, L["band_cap"], 12, anchor="end", fill="#333"))
    # curves (dashed RGB first so the solid curves overlay it)
    g.append(curve(RGB_PTS, "#999", dash="7,5"))
    g.append(curve(FLASH_PTS, AMBER))
    g.append(curve(LED_PTS, LED_C))
    # schematic disclaimer in the panel corner
    g.append(text(688, 150, L["schem"], 11.5, anchor="end", fill="#777"))
    # fan labels (left col: rows 170 / 206 / 330; right col: 196 / 330)
    g += label(L["spike"], 170, (340, 144), "L")
    g += label(L["flashlab"], 206, (312, 208), "L")
    g += label(L["cyan"], 330, (378, 331), "L")
    g += label(L["rgbw"], 372, (404, 380), "L")
    g += label(L["cover"], 196, (606, 194), "R")
    g += label(L["rolloff"], 330, (641, 335), "R")

    # ---- panel 2: time domain ----
    g.append(text(24, 500, L["time_head"], 14, weight="bold"))
    # row 1 — flash pulse
    g.append(line(270, 545, 696, 545, "#888", 1.2, marker="mg"))
    g.append(text(704, 549, "t", 11, fill=GRAY))
    g.append(f'<rect x="300" y="511" width="5" height="34" fill="{AMBER}"/>')
    g.append(text(322, 524, L["pulse_note"], 12.5, fill="#333"))
    g += label(L["pulse"], 522, (298, 515), "L")
    # row 2 — continuous LED long exposure
    g.append(line(270, 600, 696, 600, "#888", 1.2, marker="mg"))
    g.append(text(704, 604, "t", 11, fill=GRAY))
    g.append(f'<rect x="300" y="584" width="260" height="16" fill="#d9d9d9" '
             f'stroke="{LED_C}" stroke-width="1.2"/>')
    rip = " ".join(f"{x},{581 if (i % 2) else 577}"
                   for i, x in enumerate(range(302, 559, 8)))
    g.append(f'<polyline points="{rip}" fill="none" stroke="#777" '
             f'stroke-width="1"/>')
    g += label(L["led"], 578, (298, 590), "L")
    g += label(L["shake"], 574, (508, 576), "R")

    g.append(text(W - 24, H - 14, "NeoBox v5 — 2026-08", 12,
                  anchor="end", fill="#888"))
    g.append('</svg>')
    return "\n".join(g) + "\n"


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    for L in LANG.values():
        path = os.path.join(OUT_DIR, L["file"])
        with open(path, "w", encoding="utf-8") as f:
            f.write(build(L))
        print("wrote", path)


if __name__ == "__main__":
    main()
