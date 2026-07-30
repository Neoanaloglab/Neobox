# Contributing to NeoBox

> How to change NeoBox without breaking the geometry, the published numbers or the three language editions — read this before you open a pull request.

**Contents:** [Source vs generated](#source-of-truth-vs-generated-files) · [Verify gate](#the-export-and-verify-gate) · [Three languages](#the-three-language-rule) · [Terminology](#terminology) · [Design log](#rejecting-an-alternative) · [Variant or fix](#a-variant-or-a-fix) · [Pull requests](#pull-requests)

NeoBox is a hardware repository: the files under `stl/` are build output, not hand-editable artwork, and every document exists three times over. Most contributor mistakes are one of those two facts being missed.

## Source of truth vs generated files

| Kind | Files | Edit directly? |
|---|---|---|
| Source — geometry | `cad/neobox.blend` | Yes. Every printed part is modelled here. |
| Source — flat part | `cad/film-stage-aluminium-3mm.dxf` | Yes. The aluminium film stage is drawn directly. |
| Source — prose | `README.md` and `docs/*.md`, in all three languages | Yes. |
| Source — drawings | `drawings/*.svg` (+ `.zh-CN.svg`, `.ja.svg`) | Yes — hand-authored, not exported from the `.blend`. |
| Generated | the nine `.stl` files under `stl/white-pla/` and `stl/black-pla/` | No. Re-export them from `cad/neobox.blend`. |
| Historical | `cad/legacy-plywood/` | No. Kept for the record only; the plywood build is superseded. |

There are **9 STL files = 8 parts for the default build + 1 optional 6×6 mask** — never eight, never ten:

- `stl/white-pla/` — `main-body.stl`, `top-cover.stl`, `access-panel.stl`
- `stl/black-pla/` — `film-holder-135-base.stl`, `film-holder-135-lid.stl`, `film-holder-120-base.stl`, `film-holder-120-lid.stl`, `film-stage-printed.stl`, and the optional `mask-6x6.stl`

They are binary artefacts committed to the repository, so a diff never shows what changed. A pull request that edits an STL by hand will be closed: change the Blender scene and re-export. [Design § 11](docs/design.md#11-working-with-the-source) documents the collection tree, which objects make up each file, and the export procedure.

## The export and verify gate

Any pull request that touches geometry regenerates the STLs with the committed exporter and then shows a clean run of the verifier, both from the repository root:

```
blender --background cad/neobox.blend --python tools/export_stl.py
python3 tools/verify_stl.py
```

The exporter unions each part's deliberately overlapping shells into one watertight solid and writes it in assembly world space; a naive File → Export → STL produces multi-shell files that fail the verifier. Regenerated files may differ from the published ones byte for byte (triangulation is not stable across Blender versions) while being geometrically identical — the verifier is the referee.

It walks every file under `stl/` and exits non-zero if any check fails, so it can gate a commit. Four invariants per file:

| # | Invariant | Why it matters |
|---|---|---|
| 1 | Watertight — every edge shared by exactly two triangles | non-manifold geometry slices unpredictably |
| 2 | Every horizontal face on the 0.2 mm grid above the part's own base | the default layer height has to divide every feature |
| 3 | No exposed step below 0.4 mm — two layers at 0.2 | design-log entry 19 |
| 4 | Bounding box matches the published dimensions | the documents quote them and the fits depend on them |

As of 2026-07-30 all nine files pass: watertight single solids, 0 non-manifold edges. Keep it that way.

> [!IMPORTANT]
> The geometry is dimensionally verified in Blender and numerically verified from the exported STLs by `tools/verify_stl.py`. The design has never been physically printed, built, photographed or tested. Do not write "measured", "tested" or "empirically" about any enclosure or optical figure, in any language.

## The three-language rule

Every document family ships as `x.md` + `x.zh-CN.md` + `x.ja.md`, and the three move together in one pull request. 简体中文 and 日本語 must carry exactly the same facts as English — no localisation drift in any number, claim or caveat. The one exception is this file: `CONTRIBUTING.md` is English-only, and there is no `CONTRIBUTING.zh-CN.md` or `CONTRIBUTING.ja.md`.

Numbers come from the project fact sheet or from `cad/neobox.blend`. Do not invent one, do not round differently, do not quietly "improve" a dimension.

## Terminology

One name per thing. Use these and nothing else: main body, top cover (never "lid"), access panel, access opening, the cavity, aperture, film stage, corner blocks, diffuser, film holder → holder base / holder lid, land, rail, channel, window, stud, lower nut / upper nut, heat-set insert, steel washer, film strip, build plate. Definitions live in the [glossary](docs/glossary.md#glossary); a synonym introduced by a pull request will be sent back.

Japanese: 本体 must never mean the flash — write ストロボ本体. Chinese: 打印台 is forbidden for the film stage (it means build plate) — write 胶片台.

## Rejecting an alternative

If your change rejects an approach — another diffuser stack, another fastening scheme, another material — add a new numbered entry to `docs/design-log.md`, continuing the existing 1–20 sequence, as an H3 heading (`### 21. …`) so other documents can link to it. Say what was considered, why it lost, and end with the one-line lesson in bold. All three languages, same entry.

## A variant, or a fix?

A **fix** corrects the published design: a wrong dimension, a broken link, a failing check, an unclear step. Open it against `main`.

A **variant** changes what the box is for — a different flash, 4×5, an LED panel instead of a speedlight. The published STLs fit the NEEWER TT560 only. The formulas in [Design § 2](docs/design.md#2-dimension-chain) give the new numbers; they do not resize the files, so a different flash means editing `cad/neobox.blend` and re-exporting every affected part. A substitute flash must have a head that rotates 90°, manual power control, and a body no longer than 190 mm and no thicker than 55 mm lying flat — otherwise the enclosure has to be re-derived. Keep a variant on its own branch and state in the pull request which parts changed and what you re-verified.

## Pull requests

Branch from `main`, one topic per branch, named `fix/…`, `docs/…` or `geometry/…`. Title the pull request with what changes, not which file, and describe the change in English.

- [ ] Every number traces to the fact sheet or to `cad/neobox.blend`
- [ ] English, 简体中文 and 日本語 editions updated together, with no drift between them
- [ ] Canonical terminology only
- [ ] Internal links resolve, and each one points at an anchor that exists in the target
- [ ] `python3 tools/verify_stl.py` run from the repository root and passing — required for any geometry change
- [ ] STLs re-exported from `cad/neobox.blend`, never hand-edited
- [ ] A new numbered `docs/design-log.md` entry added if an alternative was rejected
- [ ] No claim that the box has been printed, built, photographed, measured or tested

---

[Documentation index](README.md#documentation) · [Working with the source](docs/design.md#11-working-with-the-source) · [Design log](docs/design-log.md#design-log)
