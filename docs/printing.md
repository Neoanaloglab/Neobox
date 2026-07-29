# 3D printing

**English** · [简体中文](printing.zh-CN.md) · [日本語](printing.ja.md)

Nine STL files — eight for the default build plus an optional 6×6 mask — in two colours. All models are 1:1 in millimetres — **do not scale**.

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
| `stl/black-pla/film-holder-135-base.stl` | default 0.2 mm layers, **channel face down on the plate** |
| `stl/black-pla/film-holder-135-lid.stl` | default 0.2 mm layers |
| `stl/black-pla/film-holder-120-base.stl` | as above |
| `stl/black-pla/film-holder-120-lid.stl` | as above |
| `stl/black-pla/film-stage-printed.stl` | 200 × 230 × 5 solid plate, **alignment blocks printed on top**; ≥ 30 % infill or ≥ 5 perimeters for flatness |

One optional extra: `stl/black-pla/mask-6x6.stl`, only if you shoot 6×4.5 / 6×6 in the 120 holder.

## Settings

| | Enclosure | Holders |
|---|---|---|
| Layer height | 0.16–0.2 | 0.2 (or 0.1) |
| Perimeters | ≥ 3 | ≥ 3 |
| Infill | 15–25 % | 20–30 % |
| Material | PLA (PETG also fine) | PLA or PETG |

PETG is slightly tougher for the holders and copes better with being handled constantly; PLA prints flatter. Either works.

## Print one holder first

The 0.4 mm film channel and 0.4 mm reliefs are the tightest features in the project — and every holder z-feature is an exact multiple of 0.2 mm with no exposed step under two layers (relief 0.4, rail step 0.8, channel 0.4), so they quantise cleanly at the default 0.2 mm layer height. 0.1 mm also divides them; 0.12 and 0.16 do not and will distort the steps — avoid those. Print the 135 base and lid first and check three things before committing to the rest:

1. Film slides through the channel smoothly, without slop and without binding.
2. The magnet pockets accept Ø6 × 2 magnets (they should press in, then be glued).
3. The base sits flat on the acrylic with no rocking.

If the channel is tight, deburr the entrance with a knife; if it is loose, reprint with a small negative XY compensation rather than editing the model.

## Ordering from a print service

If you are having these printed for you (Taobao, JLCPCB, Craftcloud, a local shop), the essential points to pass on:

> 10 STL files, millimetres, do not scale.
> **White PLA ×3:** `main-body` (needs ≥ 280 × 300 mm bed; the 190 mm span above the front opening needs support), `top-cover`, `access-panel`.
> **Black PLA ×5:** four film-holder parts (default 0.2 mm layers, bases printed with the channel face down on the plate), `film-stage-printed` (flat side down, ≥ 30 % infill).
> Everything else: 0.2 mm layers, ≥ 3 perimeters, 15–25 % infill, matte filament preferred.

A Chinese-language version of this text for Taobao vendors is in [bom.md](bom.md#taobao-scripts).

**If the shop insists on their default settings**, let them — the holder geometry is quantised to 0.2 mm layers precisely so that default profiles work. Only two requests are load-bearing:

1. Holder bases print with the channel face down on the plate.
2. The main body needs supports over the 190 mm access-opening span.

Layer height, infill and filament can all stay at the shop's defaults. (Earlier revisions required 0.12–0.16 mm layers for the holders; the 0.2-quantised redesign removed that requirement.)
