#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate drawings/capture-setup{,.zh-CN,.ja}.svg — NeoBox v1 capture scene.

Whole-bench side view: NeoBox on the table with the film holder on top, the
flash lying flat with its head against the fully open front, the 2.4G receiver
on the flash foot outside the box, and the camera looking straight down from a
copy stand. All numbers come from scratchpad FACTS-v5.md (§5 light path & sync
speed, §6 assembly stack, §7 workflow). Geometry is drawn once; the three
language files differ only in the LANG text dictionary.

Run:  python3 gen_capture_setup.py
"""
import os

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.path.normpath(os.path.join(HERE, "..", "..", "drawings"))

# ---------------------------------------------------------------- canvas
W, H = 980, 720
S = 2.0                       # px per mm
TABLE = 640.0                 # y of the table surface


def Y(z_mm):
    """World z (mm above table, FACTS §6) -> screen y."""
    return TABLE - S * z_mm


AMBER = "#e8a33d"
AMBER_DK = "#8a5f14"
INK = "#111"
GREY = "#444"
LIGHT = "#f2f2f2"
MID = "#d9d9d9"
DARK = "#3a3a3a"
MUTED = "#777"
SANS = "Helvetica, Arial, sans-serif"
MONO = "Menlo, Consolas, 'Courier New', monospace"

# ---------------------------------------------------------------- text metrics


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def est(s, fs):
    """Rough advance-width estimate for Helvetica-ish text."""
    w = 0.0
    for ch in s:
        if ord(ch) >= 0x2E80 or ch in "—–→≈×":
            w += 1.0
        elif ch == " ":
            w += 0.30
        elif ch in "iljI.,:;'()[]!|·/":
            w += 0.36
        elif ch in "mwMW@":
            w += 0.92
        elif ch.isupper():
            w += 0.72
        else:
            w += 0.56
    return w * fs


def est_mono(s, fs):
    w = 0.0
    for ch in s:
        w += 1.0 if ord(ch) >= 0x2E80 else 0.62
    return w * fs

# ---------------------------------------------------------------- language pack

LANG = {
    "en": {
        "suffix": "",
        "title": "Capture setup — the whole bench, side view",
        "sub": ("Flash lies at the open front, receiver stays outside; camera "
                "shoots straight down from a copy stand. Units: mm."),
        "chip_head": "CAMERA SETTINGS",
        "chip2": "flash: MANUAL power",
        "note": "cheap 2.4G triggers eat ≈1 stop of sync; stay at 1/125 s",
        "L1": ["mirror alignment: lay a small mirror on the holder,",
               "center the lens reflection in the viewfinder (once)"],
        "L2": ["film advance: just pull the strip out,",
               "no lid off, pressure element stays put"],
        "L3": ["shoot in a dim room; keep ceiling lights",
               "from shining into the open front"],
        "L4": ["any hot-shoe flash (TT560-class) lying flat,",
               "head against the open front, manual power"],
        "L5": ["2.4G receiver (ZENIKO T1 or similar) on the",
               "flash foot; it stays outside the box"],
        "R1": "hot-shoe trigger (2.4G transmitter)",
        "R2": "camera, lens straight down",
        "R3": "copy stand",
        "wd": ["working distance:", "set by your", "magnification"],
        "dim_cap": ["table →", "film plane"],
        "caption": "NeoBox v1: overall 124.8 × 154.8 × 87 mm (holder on top)",
    },
    "zh": {
        "suffix": ".zh-CN",
        "title": "翻拍现场：整体布置（侧视）",
        "sub": ("闪光灯平躺、灯头怼住敞开前口，2.4G 接收器随灯留在箱外；"
                "相机在翻拍架上垂直俯拍。单位：mm。"),
        "chip_head": "相机设置",
        "chip2": "闪光：手动输出",
        "note": "廉价 2.4G 引闪约吃一档同步，就用 1/125 s",
        "L1": ["镜面对齐法：小镜子放在夹子上，",
               "取景器里让镜头倒影居中（对齐一次即可）"],
        "L2": ["过片：直接抽拉片条，",
               "不开盖、不动压片元件"],
        "L3": ["在昏暗房间拍摄；",
               "避免顶灯直射敞开前口"],
        "L4": ["任意热靴闪光灯（参考 TT560）平躺，",
               "灯头怼住敞开前口，手动输出"],
        "L5": ["2.4G 接收器（ZENIKO T1 同类）装在灯座上，",
               "随灯留在箱外（换电池不开箱）"],
        "R1": "热靴引闪发射器（2.4G）",
        "R2": "相机（镜头朝下俯拍）",
        "R3": "翻拍架 / 复制台",
        "wd": ["工作距离：", "按放大倍率调"],
        "dim_cap": ["桌面 →", "胶片平面"],
        "caption": "NeoBox v1：外形 124.8 × 154.8 × 87 mm（顶上为胶片夹）",
    },
    "ja": {
        "suffix": ".ja",
        "title": "撮影セットアップ：全体配置（側面図）",
        "sub": ("ストロボは横置きで発光部をオープンフロント（前面開口）に密着、"
                "2.4Gレシーバーは箱外のまま。カメラはコピースタンドで真下向き。単位：mm。"),
        "chip_head": "カメラ設定",
        "chip2": "ストロボ：マニュアル発光",
        "note": "安価な2.4Gトリガーは同調を約1段食うので 1/125 s のままでよい",
        "L1": ["ミラー調整法：小さな鏡をホルダーの上に置き、",
               "ファインダーでレンズの映り込みを中央に（一度だけ）"],
        "L2": ["コマ送り：フィルムをそのまま引き抜く。",
               "フタも押さえ部品も動かさない"],
        "L3": ["薄暗い部屋で撮影する。",
               "天井照明を前面開口に直射させない"],
        "L4": ["任意のクリップオンストロボ（TT560級）を横置き、",
               "発光部をオープンフロントに密着、マニュアル発光"],
        "L5": ["2.4Gレシーバー（ZENIKO T1等）はストロボの",
               "シューに装着し、箱の外に置いたまま"],
        "R1": "ホットシュートリガー（2.4G送信機）",
        "R2": "カメラ（真下向き）",
        "R3": "コピースタンド（複写台）",
        "wd": ["撮影距離：", "倍率に合わせて", "調整"],
        "dim_cap": ["机上面 →", "フィルム面"],
        "caption": "NeoBox v1：全体 124.8 × 154.8 × 87 mm（上はフィルムホルダー）",
    },
}
CHIP1 = "ISO 100 · f/8 · 1/125 s"   # sync-speed fact, FACTS §5 — keep 1/125

# ---------------------------------------------------------------- svg helpers


def A(**kw):
    return "".join(' {}="{}"'.format(k.replace("_", "-"), v) for k, v in kw.items())


def rect(x, y, w, h, **kw):
    return '<rect x="{:g}" y="{:g}" width="{:g}" height="{:g}"{}/>'.format(
        x, y, w, h, A(**kw))


def line(x1, y1, x2, y2, **kw):
    return '<line x1="{:g}" y1="{:g}" x2="{:g}" y2="{:g}"{}/>'.format(
        x1, y1, x2, y2, A(**kw))


def poly(points, **kw):
    p = " ".join("{:g},{:g}".format(x, y) for x, y in points)
    return '<polyline points="{}"{}/>'.format(p, A(**kw))


def polygon(points, **kw):
    p = " ".join("{:g},{:g}".format(x, y) for x, y in points)
    return '<polygon points="{}"{}/>'.format(p, A(**kw))


def circle(cx, cy, r, **kw):
    return '<circle cx="{:g}" cy="{:g}" r="{:g}"{}/>'.format(cx, cy, r, A(**kw))


def text(x, y, s, fs, anchor="start", fill=INK, weight=None, family=SANS):
    a = ' font-weight="bold"' if weight else ""
    return ('<text x="{:g}" y="{:g}" font-size="{:g}" fill="{}" '
            'text-anchor="{}" font-family="{}"{}>{}</text>').format(
        x, y, fs, fill, anchor, family, a, esc(s))


def arrow(x1, y1, x2, y2, color, w=1.6, head=7.0, both=False):
    """Line with a filled arrowhead at (x2,y2); optional head at both ends."""
    import math
    ang = math.atan2(y2 - y1, x2 - x1)
    out = [line(x1, y1, x2, y2, stroke=color, stroke_width=w)]

    def h(px, py, a):
        s, c = math.sin(a), math.cos(a)
        p1 = (px - head * c + 0.45 * head * s, py - head * s - 0.45 * head * c)
        p2 = (px - head * c - 0.45 * head * s, py - head * s + 0.45 * head * c)
        return polygon([(px, py), p1, p2], fill=color)
    out.append(h(x2, y2, ang))
    if both:
        out.append(h(x1, y1, ang + 3.14159265))
    return "".join(out)


def waves(cx, cy, direction):
    """Three amber wireless arcs opening 'left' or 'up'."""
    out = []
    for r in (8, 13, 18):
        if direction == "left":
            p1 = (cx - 0.5 * r, cy + 0.82 * r)
            p2 = (cx - 0.5 * r, cy - 0.82 * r)
            c = (cx - 1.6 * r, cy)
        else:  # up
            p1 = (cx - 0.82 * r, cy - 0.5 * r)
            p2 = (cx + 0.82 * r, cy - 0.5 * r)
            c = (cx, cy - 1.6 * r)
        out.append('<path d="M {:g} {:g} Q {:g} {:g} {:g} {:g}"{}/>'.format(
            p1[0], p1[1], c[0], c[1], p2[0], p2[1],
            A(fill="none", stroke=AMBER, stroke_width=1.6,
              stroke_linecap="round")))
    return "".join(out)

# ---------------------------------------------------------------- geometry (shared)

BOX_L = 530.0
BOX_R = BOX_L + 125 * S            # ~125 mm silhouette wide -> 780
CX = (BOX_L + BOX_R) / 2           # 655, lens axis

PLATE_T, PLATE_B = Y(79), Y(73)    # cover-stage plate 73..79
GX1, GX2 = 570.0, 740.0            # light window gap in the plate
ACR_T, ACR_B = Y(78.6), Y(76.6)    # opal acrylic 76.6..78.6
FL_T = Y(83)                       # flange top
FLL1, FLL2 = 534.4, 560.4          # flange blocks (outer 120.6 / inner 94.6)
FLR1, FLR2 = 749.6, 775.6
HOL_L, HOL_R = 561.0, 749.0        # holder 94 -> 188 px
HOL_T = Y(87)                      # holder lid top = overall 87
WIN1, WIN2 = 618.0, 692.0          # holder window gap
FILM_Y = Y(83.2)                   # film plane 83.2 -> 473.6

FL_BODY_L, FL_BODY_R = 150.0, 412.0    # flash body (190 mm total incl. head)
FL_HEAD_L = 408.0
FACE_T, FACE_B = Y(53.5), Y(8.5)       # emitting face 45 tall, centre z=31

CAM_L, CAM_R = 590.0, 720.0
CAM_T, CAM_B = 172.0, 250.0
HUMP_L, HUMP_R, HUMP_T = 630.0, 685.0, 158.0
TRG_L, TRG_R, TRG_T, TRG_B = 640.0, 676.0, 134.0, 158.0
LENS_L, LENS_R, LENS_B = 627.0, 681.0, 322.0

COL_L, COL_R = 862.0, 892.0        # copy-stand column
BRK_T, BRK_B = 198.0, 212.0        # bracket

WD_X = 688.0                       # working-distance arrow
DIM_X = 800.0                      # 83.2 dimension

RCV = (78.0, 588.0, 150.0, 640.0)  # receiver box (sits on the table)

# ---------------------------------------------------------------- one drawing


def leader(sx, sy, bx, ty):
    """Fan leader: horizontal to bend x, then vertical down to target + dot."""
    return (poly([(sx, sy), (bx, sy), (bx, ty)], fill="none", stroke=GREY,
                 stroke_width=1) + circle(bx, ty, 2.2, fill=GREY))


def draw(L):
    o = []
    o.append('<svg xmlns="http://www.w3.org/2000/svg" width="{}" height="{}" '
             'viewBox="0 0 {} {}" font-family="{}">'.format(W, H, W, H, SANS))
    o.append(rect(0, 0, W, H, fill="#ffffff"))

    # ---- header
    o.append(text(40, 42, L["title"], 20, weight=True))
    o.append(text(40, 66, L["sub"], 12.5, fill=MUTED))

    # ---- table
    o.append(line(60, TABLE, 950, TABLE, stroke=GREY, stroke_width=2))
    x = 74
    while x < 946:
        o.append(line(x, TABLE + 2, x - 9, TABLE + 12, stroke="#aaa",
                      stroke_width=1))
        x += 26

    # ---- NeoBox (white parts, open front on the left)
    o.append(rect(BOX_L, Y(3), BOX_R - BOX_L, 6, fill=LIGHT, stroke=GREY,
                  stroke_width=2))                                  # floor 0..3
    o.append(rect(BOX_R - 2.4 * S, PLATE_B, 2.4 * S, Y(3) - PLATE_B,
                  fill=LIGHT, stroke=GREY, stroke_width=2))         # back wall
    # cover-stage plate with the light window gap
    o.append(rect(BOX_L, PLATE_T, GX1 - BOX_L, PLATE_B - PLATE_T, fill=LIGHT,
                  stroke=GREY, stroke_width=2))
    o.append(rect(GX2, PLATE_T, BOX_R - GX2, PLATE_B - PLATE_T, fill=LIGHT,
                  stroke=GREY, stroke_width=2))
    o.append(line(GX1, PLATE_B, GX2, PLATE_B, stroke=GREY, stroke_width=1.2,
                  stroke_dasharray="3,3"))                          # window sill
    # opal acrylic in its rebate (amber = light path)
    o.append(rect(565, ACR_T, 745 - 565, ACR_B - ACR_T, fill=AMBER,
                  fill_opacity=0.45, stroke=AMBER_DK, stroke_width=0.9))
    # tray flanges
    o.append(rect(FLL1, FL_T, FLL2 - FLL1, PLATE_T - FL_T, fill=LIGHT,
                  stroke=GREY, stroke_width=1.2))
    o.append(rect(FLR1, FL_T, FLR2 - FLR1, PLATE_T - FL_T, fill=LIGHT,
                  stroke=GREY, stroke_width=1.2))

    # faint amber wash in the cavity
    o.append(rect(534, 500, 238, 132, fill=AMBER, fill_opacity=0.06))

    # ---- film holder (black) with window gap
    o.append(rect(HOL_L, HOL_T, WIN1 - HOL_L, PLATE_T - HOL_T, fill=DARK,
                  stroke="#222", stroke_width=1.2))
    o.append(rect(WIN2, HOL_T, HOL_R - WIN2, PLATE_T - HOL_T, fill=DARK,
                  stroke="#222", stroke_width=1.2))
    o.append(line(HOL_L, Y(84), WIN1, Y(84), stroke="#666",
                  stroke_width=0.8))                                # base/lid split
    o.append(line(WIN2, Y(84), HOL_R, Y(84), stroke="#666", stroke_width=0.8))
    # film: amber in the window, dark tail pulled out over the flange
    o.append(line(WIN1 + 2, FILM_Y, WIN2 - 2, FILM_Y, stroke=AMBER,
                  stroke_width=1.8))
    o.append(rect(520, FILM_Y - 2, HOL_L + 1 - 520, 2.6, fill="#222"))
    o.append(arrow(519, FILM_Y - 0.8, 497, FILM_Y - 0.8, AMBER, w=2, head=7))

    # small mirror on the holder (mirror alignment, done once)
    o.append(rect(576, 457, 48, 9, fill="#ffffff", stroke=GREY,
                  stroke_width=1.4))
    o.append(line(582, 463.5, 590, 459, stroke="#999", stroke_width=1.1))
    o.append(line(593, 463.5, 601, 459, stroke="#999", stroke_width=1.1))

    # ---- flash (black), head against the open front
    o.append(rect(FL_BODY_L, Y(54), FL_BODY_R - FL_BODY_L, TABLE - Y(54),
                  fill=DARK, stroke="#222", stroke_width=2))
    o.append(rect(210, 556, 120, 56, rx=4, fill="#4a4a4a", stroke="#666",
                  stroke_width=1))                                  # panel
    o.append(rect(FL_HEAD_L, Y(55), BOX_L - FL_HEAD_L, Y(6) - Y(55), fill=DARK,
                  stroke="#222", stroke_width=2))
    o.append(rect(522, FACE_T, 8, FACE_B - FACE_T, fill=AMBER))     # emitting face
    # foot + receiver (amber, outside the box)
    o.append(rect(128, 560, 24, 28, fill=DARK, stroke="#222", stroke_width=1.2))
    o.append(rect(RCV[0], RCV[1], RCV[2] - RCV[0], RCV[3] - RCV[1], rx=3,
                  fill=AMBER, stroke=AMBER_DK, stroke_width=1.5))
    o.append(line(RCV[0] + 6, 600, RCV[2] - 24, 600, stroke=AMBER_DK,
                  stroke_width=1))
    o.append(waves(104, 584, "up"))

    # ---- light path (amber): head -> bounce -> up through window
    o.append(arrow(536, Y(31), 650, Y(31), AMBER, w=1.8))
    o.append(arrow(650, Y(31), 716, 528, AMBER, w=1.8))
    o.append(arrow(650, Y(31), 596, 524, AMBER, w=1.8))
    for ax in (600, CX, 710):
        o.append(arrow(ax, 516, ax, 498, AMBER, w=1.8, head=6))

    # ---- copy stand (drawn before camera so the bracket sits behind)
    o.append(rect(820, 626, 130, 14, fill=MID, stroke=GREY, stroke_width=2))
    o.append(rect(COL_L, 180, COL_R - COL_L, 626 - 180, fill=MID, stroke=GREY,
                  stroke_width=2))
    o.append(rect(856, 172, 42, 8, fill=MID, stroke=GREY, stroke_width=1.2))
    o.append(rect(714, BRK_T, COL_L - 714, BRK_B - BRK_T, fill=MID,
                  stroke=GREY, stroke_width=1.2))
    o.append(circle(870, 205, 6, fill=LIGHT, stroke=GREY, stroke_width=1.2))

    # ---- camera, lens down
    o.append(rect(CAM_L, CAM_T, CAM_R - CAM_L, CAM_B - CAM_T, rx=4, fill=DARK,
                  stroke="#222", stroke_width=2))
    o.append(rect(HUMP_L, HUMP_T, HUMP_R - HUMP_L, CAM_T - HUMP_T, fill=DARK,
                  stroke="#222", stroke_width=1.5))
    o.append(rect(LENS_L, CAM_B, LENS_R - LENS_L, LENS_B - CAM_B, fill=DARK,
                  stroke="#222", stroke_width=2))
    o.append(line(LENS_L, 268, LENS_R, 268, stroke="#666", stroke_width=1))
    o.append(line(LENS_L, 290, LENS_R, 290, stroke="#666", stroke_width=1))
    o.append(rect(633, 314, 44, 8, fill="#222"))                    # front glass
    # hot-shoe trigger (amber) + waves
    o.append(rect(TRG_L, TRG_T, TRG_R - TRG_L, TRG_B - TRG_T, rx=2, fill=AMBER,
                  stroke=AMBER_DK, stroke_width=1.2))
    o.append(rect(648, 154, 20, 4, fill=AMBER_DK))
    o.append(waves(636, 146, "left"))

    # ---- optical axis to the film plane
    o.append(line(CX, 328, CX, FILM_Y - 3, stroke=AMBER, stroke_width=1.4,
                  stroke_dasharray="6,5"))

    # ---- working distance (no number: set by magnification)
    o.append(line(LENS_R + 2, LENS_B, 696, LENS_B, stroke=MUTED,
                  stroke_width=1))
    o.append(arrow(WD_X, LENS_B + 1, WD_X, FILM_Y - 1, GREY, w=1, head=6,
                  both=True))
    for i, s in enumerate(L["wd"]):
        o.append(text(712, 376 + 16 * i, s, 12))

    # ---- dimension: table -> film plane = 83.2 (FACTS §6)
    o.append(line(755, FILM_Y, DIM_X + 6, FILM_Y, stroke=MUTED,
                  stroke_width=1))
    o.append(arrow(DIM_X, FILM_Y + 1, DIM_X, TABLE - 1, GREY, w=1, head=6,
                  both=True))
    o.append(text(DIM_X + 4, 545, "83.2", 12.5))
    for i, s in enumerate(L["dim_cap"]):
        o.append(text(DIM_X + 2, 561 + 14 * i, s, 10, fill=MUTED))

    # ---- settings chip (monospace, rounded)
    cw = max(est_mono(CHIP1, 14), est_mono(L["chip2"], 14),
             est(L["chip_head"], 11.5)) + 28
    o.append(rect(40, 92, cw, 74, rx=8, fill="#fffaf0", stroke=AMBER,
                  stroke_width=1.6))
    o.append(text(54, 114, L["chip_head"], 11.5, fill=MUTED, weight=True))
    o.append(text(54, 136, CHIP1, 14, family=MONO))
    o.append(text(54, 156, L["chip2"], 14, family=MONO))
    o.append(text(40, 184, L["note"], 11, fill=MUTED))

    # ---- left label column (fan leaders, targets ordered right->left)
    left = [
        ("L1", 262, 610, 456),   # mirror on the holder
        ("L2", 322, 526, 468),   # film tail / advance
        ("L3", 382, 512, 501),   # dim room -> open mouth
        ("L4", 440, 466, 525),   # flash head at the front
    ]
    for key, by, bx, ty in left:
        lines = L[key]
        for i, s in enumerate(lines):
            o.append(text(40, by + 18 * i, s, 13))
        sx = 40 + max(est(s, 13) for s in lines) + 7
        o.append(leader(sx, by - 4.5, bx, ty))
    # receiver label: leader drops from below the text
    for i, s in enumerate(L["L5"]):
        o.append(text(40, 494 + 18 * i, s, 13))
    o.append(poly([(58, 520), (58, 566), (79, 586)], fill="none", stroke=GREY,
                  stroke_width=1))
    o.append(circle(79, 586, 2.2, fill=GREY))

    # ---- right labels (end-anchored at x=940)
    for key, by, tx, ty in (("R1", 100, 660, 132), ("R2", 128, 716, 170)):
        s = L[key]
        o.append(text(940, by, s, 13, anchor="end"))
        start = 940 - est(s, 13)
        o.append(poly([(start - 6, by - 4.5), (start - 16, by - 4.5),
                       (tx, ty)], fill="none", stroke=GREY, stroke_width=1))
        o.append(circle(tx, ty, 2.2, fill=GREY))
    s = L["R3"]                                    # copy stand: underline leader
    o.append(text(940, 162, s, 13, anchor="end"))
    o.append(poly([(940 - est(s, 13), 168), (900, 168), (891, 171)],
                  fill="none", stroke=GREY, stroke_width=1))
    o.append(circle(891, 171, 2.2, fill=GREY))

    # ---- captions
    o.append(text(CX, 666, L["caption"], 11.5, anchor="middle", fill=MUTED))
    o.append(text(940, 706, "NeoBox v1 — 2026-08", 11, anchor="end",
                  fill="#999"))
    o.append("</svg>")
    return "\n".join(o) + "\n"


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    for L in LANG.values():
        path = os.path.join(OUT_DIR, "capture-setup{}.svg".format(L["suffix"]))
        with open(path, "w", encoding="utf-8") as f:
            f.write(draw(L))
        print("wrote", path)


if __name__ == "__main__":
    main()
