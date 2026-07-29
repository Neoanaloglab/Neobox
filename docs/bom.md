# Bill of materials and sourcing

Prices are indicative, in CNY, from Chinese marketplaces (Taobao / 1688) as of July 2026. The whole build outside the flash comes to roughly **¥250–420 / US$35–60 / ¥5,500–9,000 JPY**.

## Printed parts

| Item | Qty | Source | Price |
|---|---|---|---|
| White PLA parts: main body, top cover, access panel | 3 | Print service, bed ≥ 280 × 300 mm | ¥150–280 |
| Black PLA parts: 4 holder parts, film stage, alignment blocks, 6×6 mask | 7 | Same order | included |

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
10 个 STL，单位毫米，请勿缩放。

白色 PLA 3 件：
  - main-body.stl（208×273×92，需要 ≥280×300 打印床；
    抽口顶边 190mm 跨度请加支撑）
  - top-cover.stl（214.6×279.6 裙边盖）
  - access-panel.stl

黑色 PLA 7 件：
  - film-holder-135-base / -lid、film-holder-120-base / -lid
    （这 4 件层高 0.12~0.16，底座请滑槽面朝下贴床打）
  - film-stage-printed.stl（填充 ≥30%）
  - alignment-blocks-x4.stl（一个文件里 4 个小块）
  - mask-6x6.stl

其余参数：层高 0.2、壁 ≥3 层、填充 15~25%、哑光料优先。
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
图上 3 个 Ø6.5 孔是光孔，请勿攻丝。
表面黑色阳极氧化（做不了阳极就哑光黑喷涂）。
```

搜索词：`5052铝板 CNC 定制 阳极氧化`，附 `cad/film-stage-aluminium-3mm.dxf`
