# Bill of materials and sourcing

**English** · [简体中文](bom.zh-CN.md) · [日本語](bom.ja.md)

Prices are indicative, in CNY, from Chinese marketplaces (Taobao / 1688) as of July 2026. The whole build outside the flash comes to roughly **¥250–420 / US$35–60 / ¥5,500–9,000 JPY**.

## Printed parts

| Item | Qty | Source | Price |
|---|---|---|---|
| White PLA parts: main body, top cover, access panel | 3 | Print service, bed ≥ 280 × 300 mm | ¥150–280 |
| Black PLA parts: 4 holder parts, film stage (alignment blocks integral) | 5 | Same order | included |
| Optional black part: 6×6 mask | 0–1 | Same order | included |

Filament use is roughly 1–1.3 kg. See [printing.md](printing.md) for settings.

## Bought parts — required

| Item | Spec | Qty | Price |
|---|---|---|---|
| Opal acrylic diffuser | 2 mm, cut to 110 × 130 | 1 (buy 2–3) | ¥8–15 |
| Fully-threaded stud | M6 × 35 | 3 | ¥10–20 |
| Hex nut | M6 | 6 | included |
| Heat-set insert | M6 brass | 3 | ¥10–15 |
| EVA foam strip | self-adhesive, 2 mm | 1 roll | ¥8–15 |
| Rubber cable grommet | Ø12 | 2 | ¥3–5 |
| USB LED strip | 5 V, inline dimmer, neutral white, white cable | 1 | ¥15–25 |
| NiMH AA cells | for the flash, two sets | 8 | ¥60–100 |

## Bought parts — only if you will use the box on end

| Item | Spec | Qty | Price |
|---|---|---|---|
| Neodymium magnets | Ø6 × 2 | 24 | ¥5–10 |
| Steel washers | Ø12 | 4 | ¥3–5 |

## Light source

The reference build reuses a flash the author already owned. Any manual speedlight works; re-derive the enclosure dimensions with the formulas in [design.md](design.md#generalising-to-another-flash).

| Item | Note | Price |
|---|---|---|
| NEEWER TT560 | 190 × 75 × 55, GN38, manual 1/1–1/128 in full stops, 5600 K | ¥200–300 |
| ZENIKO T1 | 39 × 38 × 29.5, 2.4 GHz transmitter + receiver | ¥150–250 |

What actually matters when choosing a flash: **manual power control** and a head that rotates to 90°. TTL and HSS are irrelevant here — do not pay for them. A trigger with power control from the camera position (for example a Godox X2T with a Godox flash) is a genuine convenience, because otherwise changing power means pulling the access panel.

## Optional upgrade

| Item | Spec | File | Price |
|---|---|---|---|
| Aluminium film stage | 5052, 3 mm, black anodised, aperture 100 × 120, 3 × Ø6.5 **clearance holes, no tapping** | `cad/film-stage-aluminium-3mm.dxf` | ¥80–200 |

The printed stage is adequate for the prototype. Aluminium is flatter and stays flat, which matters because the stage is the reference plane for the whole system.

---

## Taobao scripts

Copy-paste text for Chinese vendors. Reproduced in Chinese because that is the language the shops read.

### 3D 打印代打

```
9 个 STL，单位毫米，请勿缩放。全部用默认 0.2 层高。

白色 PLA 3 件：
  - main-body.stl（大箱体 208×273×92，需要 ≥280×300 打印床）
    摆放：正常平放，平底朝下，大开口朝上。
    支撑：只有正面竖墙上那个 190mm 宽方口的上边缘要支撑。
  - top-cover.stl（顶盖 214.6×279.6）
    摆放：平的大面朝下，裙边和 3 个圆柱朝上。免支撑。
  - access-panel.stl（盖板 200×78）
    摆放：背面凸起的方台（插塞）朝下贴床，把手朝上。
    支撑：面板比方台宽一圈，这圈悬空需要支撑。

黑色 PLA 5 件：
  - film-holder-135-base / film-holder-120-base（两个底座）
    摆放：平的那面朝下，带两条长凸条的面朝上。免支撑。
  - film-holder-135-lid / film-holder-120-lid（两个上盖）
    摆放：平的大面朝下，两条短压条朝上。免支撑。
  - film-stage-printed.stl（大平板 200×230，填充 ≥30%）
    摆放：平面朝下，四角 L 形挡块朝上（挡块是设计特征，不是缺陷）。

可选件（需要才加）：mask-6x6.stl（拍 6×4.5 / 6×6 时用），平放。

其余默认：壁 ≥3 层、填充 15~25%、哑光料优先。
```

搜索词：`3D打印 代打 大尺寸 PLA`

### 乳白亚克力

```
乳白半透明亚克力 2mm 厚，110×130mm，切 3 块。
```

搜索词：`乳白亚克力板 定制 2mm`（不需要图纸，报尺寸即可）

### 五金

| 搜索词 | 规格数量 |
|---|---|
| `M6全牙螺丝 35mm` | ×3 |
| `M6螺母` | ×6 |
| `热熔铜螺母 M6` | ×3 |
| `EVA海绵条 背胶 2mm` | 1 卷 |
| `橡胶过线圈 12mm` | ×2 |
| `USB LED灯带 5V 线控调光 自然白` | ×1，选白色线材 |
| `钕磁铁 6x2mm` | ×24（竖用才需要） |
| `铁垫片 M6 Ø12` | ×4（竖用才需要） |

### 铝制胶片台（正式版升级件）

```
5052 铝板 3mm，外形 200×230，中间开口 100×120，
图上 3 个 Ø6.5 孔是光孔，请勿攻丝（前孔在 (145,15)，非对称是设计意图）。
表面黑色阳极氧化（做不了阳极就哑光黑喷涂）。
```

搜索词：`5052铝板 CNC 定制 阳极氧化`，附 `cad/film-stage-aluminium-3mm.dxf`
