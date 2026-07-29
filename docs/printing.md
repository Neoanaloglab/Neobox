# 3D printing

Ten STL files in two colours. All models are 1:1 in millimetres — **do not scale**.

## White filament (the light cavity)

The interior needs no paint: the white filament *is* the reflector. Prefer a matte white; avoid silk and other glossy filaments, which reproduce the flash head as a hot spot instead of scattering it.

| File | Size | Notes |
|---|---|---|
| `stl/white-pla/main-body.stl` | 208 × 273 × 92 | **Needs a bed of at least 280 × 300 mm.** The 190 mm span over the access opening needs support, or chamfer that edge to 45° first. |
| `stl/white-pla/top-cover.stl` | 214.6 × 279.6 × 14 | Print skirt-up. Three posts underneath take M6 heat-set inserts. |
| `stl/white-pla/access-panel.stl` | 200 × 78 × 16 | Print face-down. |

Roughly 1–1.3 kg of filament for the three parts.

## Black filament (everything near the film)

These parts sit around the film and must not reflect stray light into the lens. Printing them in black means no masking or paint at all.

| File | Notes |
|---|---|
| `stl/black-pla/film-holder-135-base.stl` | 0.12–0.16 mm layers, **channel face down on the plate** |
| `stl/black-pla/film-holder-135-lid.stl` | 0.12–0.16 mm layers |
| `stl/black-pla/film-holder-120-base.stl` | as above |
| `stl/black-pla/film-holder-120-lid.stl` | as above |
| `stl/black-pla/film-stage-printed.stl` | 200 × 230 plate with ribs; ≥ 30 % infill for flatness |
| `stl/black-pla/alignment-blocks-x4.stl` | four 5 × 6 × 30 blocks in one file |
| `stl/black-pla/mask-6x6.stl` | reduces the 120 window for 6×4.5 / 6×6 |

## Settings

| | Enclosure | Holders |
|---|---|---|
| Layer height | 0.16–0.2 | 0.12–0.16 |
| Perimeters | ≥ 3 | ≥ 3 |
| Infill | 15–25 % | 20–30 % |
| Material | PLA (PETG also fine) | PLA or PETG |

PETG is slightly tougher for the holders and copes better with being handled constantly; PLA prints flatter. Either works.

## Print one holder first

The 0.3 mm film channel and 0.2 mm clearances are the tightest features in the project and the only ones sensitive to printer calibration. Print the 135 base and lid first and check three things before committing to the rest:

1. Film slides through the channel smoothly, without slop and without binding.
2. The magnet pockets accept Ø6 × 2 magnets (they should press in, then be glued).
3. The base sits flat on the acrylic with no rocking.

If the channel is tight, deburr the entrance with a knife; if it is loose, reprint with a small negative XY compensation rather than editing the model.

## Ordering from a print service

If you are having these printed for you (Taobao, JLCPCB, Craftcloud, a local shop), the essential points to pass on:

> 10 STL files, millimetres, do not scale.
> **White PLA ×3:** `main-body` (needs ≥ 280 × 300 mm bed; the 190 mm span above the front opening needs support), `top-cover`, `access-panel`.
> **Black PLA ×7:** four film-holder parts (0.12–0.16 mm layers, bases printed with the channel face down on the plate), `film-stage-printed`, `alignment-blocks-x4`, `mask-6x6`.
> Everything else: 0.2 mm layers, ≥ 3 perimeters, 15–25 % infill, matte filament preferred.

A Chinese-language version of this text for Taobao vendors is in [bom.md](bom.md#taobao-scripts).
