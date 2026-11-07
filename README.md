# NeoBox

**English** · [简体中文](README.zh-CN.md) · [日本語](README.ja.md)

> An open-hardware, 3D-printable desktop flash light box for camera scanning 135 and 120 film. About 125 × 155 × 83 mm, twelve printed parts (four of them optional) at roughly 300–350 g, held together by magnets alone, with no screws, no threads and no tools. Any hot-shoe flash lies at the fully open front and fires in. An insert platform keeps the film flat, and a single universal anti-Newton glass is the optional upgrade.

**Contents:** [What NeoBox is](#what-neobox-is) · [What you get, and what you must already own](#what-you-get-and-what-you-must-already-own) · [Why a flash](#why-a-flash) · [How the light works](#how-the-light-works) · [Documentation](#documentation) · [Quick start](#quick-start) · [Repository layout](#repository-layout) · [Adapting to a different flash](#adapting-to-a-different-flash) · [Status](#status) · [Licence and credits](#licence-and-credits)

![Licence: MIT](https://img.shields.io/badge/licence-MIT-blue) ![Status: v1, built and in use](https://img.shields.io/badge/status-v1%20built-green) ![Formats: 35 mm and 120](https://img.shields.io/badge/formats-35%20mm%20%C2%B7%20120-lightgrey) ![Outer size about 125 by 155 by 83 mm](https://img.shields.io/badge/size-~125%20%C3%97%20155%20%C3%97%2083%20mm-lightgrey)

![NeoBox v1 from an oblique angle: the white box with its open front and a flash lying at it, the black film holder on top, and the camera tube now in development standing on the holder, with the camera shown as a ghost](drawings/neobox-45.png)

> [!IMPORTANT]
> This is the first release. The geometry has been checked dimension by dimension in the Blender source, and the exported STL files have been checked numerically. The author and friends have printed the box and used it to scan 135 and 120 film. **The evenness and flatness figures in the documents are still design targets, not instrument measurements.** Read [Status](#status) before you spend money.

## What NeoBox is

NeoBox is a white box, fully open at the front. It turns one bare speedlight (an ordinary hot-shoe flash with nothing attached) into an evenly glowing surface. That lets you photograph film with a digital camera instead of using a scanner, a technique called [camera scanning](docs/glossary.md#camera-scanning) (also DSLR scanning).

The flash lies flat on the desk with its head at the open front and fires **horizontally** into the white cavity. Light reaches the film only after several diffuse bounces and one opal acrylic diffuser (a milky white acrylic sheet).

Because the flash stays outside the enclosure, the box only has to contain the mixing cavity and the film platform. That is why twelve printed parts, roughly 300–350 g of PLA (the everyday 3D-printing plastic) and a 160 × 160 mm build plate are enough.

| Item | Specification |
|---|---|
| Outer size | ≈ 125 × 155 × 83 mm (footprint 124.8 × 154.8 mm, 87 mm to the top of a seated film holder) |
| Formats | 135 and 120 up to 6×9; 6×6 via a mask insert; 6×4.5 by cropping in post; mounted 135 slides via the optional slide plate; 4×5 sheets via the optional 4×5 stage, with an evenness caveat |
| Printed parts | 12 STL files (3 white, 9 black, including the optional 6×6 mask, slide plate and 4×5 stage); ≈ 300–350 g; all print without supports |
| Bought parts | 1 opal acrylic diffuser, 32 Ø8 × 2 mm magnets, 4 steel washers; optional: 1 anti-Newton glass, 1 flocking sheet |
| Enclosure | A one-piece main body with a fully open front, and a cover-stage that drops on over four locating tenons (small pegs that fix its position) |
| Diffusion | Single opal acrylic diffuser, 68 × 118 × 2 mm, under a 62 × 95 mm light window, 4.6 mm below the film |
| Film flatness | Insert platform: a 4.6 mm element ledge in the holder base carries a printed pressure-window insert, upgradable to one universal 64 × 95 × 2 mm anti-Newton glass |
| Film holders | Sliding-channel holders for 135 and 120, closed by Ø8 × 2 magnets. To change format, lift one holder off and set the other down. A pocketed slide plate holds mounted 135 slides |
| Film plane | 83.2 mm above the desk, identical for both formats |
| Light source | Any hot-shoe flash with manual power, lying flat at the open front. The reference build is a NEEWER TT560 with a ZENIKO T1 trigger set |
| Assembly | No screws, no threads, no tools. Magnets and gravity only. Levelling is done on the camera side with a small mirror |
| Licence | MIT |

## What you get, and what you must already own

NeoBox is one half of a scanning rig. It replaces the light table. You still need the camera above it.

| This repository gives you | You must already own or buy |
|---|---|
| 12 STL files (3 white, 9 black). Every one prints without supports on a flat face | A camera body with manual exposure and raw capture (mirrorless or DSLR) |
| The Blender source `cad/neobox.blend`, the authoritative geometry | A macro-capable lens. One 1:1 macro lens covers every format in this project |
| Drawings, in English, 简体中文 and 日本語 | A [copy stand](docs/glossary.md#copy-stand), or a tripod with a horizontal or reversible column, that holds the camera squarely above the box |
| Ten documents covering shopping, printing, building and scanning | The flash itself, plus a trigger set. The transmitter goes on the camera's hot shoe, and the receiver stays outside the box |
| The committed STL exporter and the geometry verification script | A remote release, and software that does [flat-field correction](docs/glossary.md#flat-field-correction) and negative [inversion](docs/glossary.md#inversion) |
| Copy-paste [vendor scripts](docs/bom.md#vendor-scripts) for ordering every part from a print shop | The consumables in [Tools and consumables](docs/bom.md#tools-and-consumables). Assembly itself needs no screwdriver, wrench or soldering iron |

> [!IMPORTANT]
> The build cost covers the printed and bought parts only. It excludes the flash, the trigger, the camera, the lens, the stand, the release and the software. If you own none of those, budget for them first. [Getting started](docs/getting-started.md#what-you-must-already-own) itemises the whole list.

## Why a flash

**The flash pulse *is* the exposure.** The camera's shutter dial stays at an ordinary sync speed (1/125 s is the recommendation). Its only job is to be open when the flash fires. What actually defines the frame is the tube's pulse, which lasts just 1/1,000–1/20,000 s at working power. The front of the box is open, so room light can reach the cavity, but the pulse is far brighter than room light. Shoot in a dim room, keep ceiling lights out of the opening, and room light contributes nothing visible.

**That makes vibration irrelevant.** The pulse acts as the real shutter, and it is one to three orders of magnitude shorter than the 1/15–1/60 s of real shutter time a continuous LED panel needs at ISO 100 and f/8. Copy-stand flex, shutter shock and footsteps on a wooden floor stop mattering. Nothing moves measurably within the pulse. This is the project's central claim.

The second argument is about the spectrum of the light, and film is pickier here than it looks. A colour negative is three stacked dye layers: yellow, magenta and cyan. They record blue, green and red respectively. The cyan record and the orange mask both work at the red end of the spectrum. A scanning light has to deliver enough energy in all three bands at once. Wherever the source is weak or has a gap, that dye layer is under-sampled and the channels stop separating cleanly. You pay for it after inversion. The colour curves cross, and stubborn casts remain that no single white-balance click can fix.

**A xenon flash tube is the native light source for silver-halide materials such as film.** It emits a genuinely continuous spectrum at roughly 5600 K. Its colour rendering is daylight-class (CRI typically ≥ 95), with strong deep red, the R9 test colour that LEDs struggle with. A typical white LED is a blue pump plus phosphor, that is, a blue LED under a phosphor coating. Its spectrum has a spike near 450 nm, a dip around 480 nm (the "cyan gap"), a broad phosphor hump, then a roll-off past about 630 nm. That roll-off lands exactly where the cyan layer and the orange mask need light most. The figure below shows the shape of the problem. The curves are schematic, typical of the two kinds of source, and not measurements.

![Spectral and time-domain comparison of flash and LED](drawings/spectral-response.svg)

"White" mixed from three LEDs fares no better, for the opposite reason. The spectrum collapses to three narrow spikes with almost nothing between them, so whole bands of the dye spectra are never sampled at all. A one-shot colour camera (any ordinary colour camera) makes it worse. Its colour matrix is calibrated for continuous light sources. Three spikes read through the Bayer filters produce cross-talk that the calibration never anticipated, and the white point baked into the LED mixing ratios fights the orange mask. The result is colour casts that change from one film stock to the next and refuse to grade out.

The best possible result comes from a different setup, and that deserves saying plainly. It is a monochrome camera with sequential RGB. Three exposures, under narrow red, green and blue light, on a sensor with no Bayer mosaic give a densitometer-grade trichromatic scan. Every channel is at full resolution, and the light source alone defines the colour separation. That is the approach of the drum scanner. It costs a niche camera, three shots per frame and a registration workflow. NeoBox deliberately takes the practical point on that curve. One flash, one shot, any camera, and a continuous spectrum, so the single-shot route does not run into the gaps described above.

Consistency is the third argument. It is less dramatic, but real. A manual flash at a fixed power fraction gives the same light shot after shot. Every frame of a roll receives the same light, so one inversion profile fits the whole roll. There is no warm-up drift, no colour shift as the light heats up over a session, and no PWM dimming (dimming by rapid flicker), so no banding appears under an electronic shutter. And all of it arrives at f/8 and [base ISO](docs/glossary.md#base-iso), with power in reserve.

There is a commercial precedent. Ricoh's [PENTAX FILM DUPLICATOR](https://ricohimagingstore.com/pentax-film-duplicator.html) is the benchmark camera-scanning rig, made by a camera maker with film heritage, and it is built around exactly this recipe: a digital camera with a macro lens, and an external flash fired through a diffusion screen. NeoBox uses the same optical recipe, with a light box you print at home and a film path of its own.

**An LED panel was considered and rejected.** A panel is already a glowing surface, but neither the effective-shutter argument nor the spectral argument above applies to it. The reasoning is in [Design](docs/design.md#8-flash-operation) and the [FAQ](docs/getting-started.md#faq).

## How the light works

![Optical path through NeoBox: the flash fires horizontally into the white cavity, which mixes the light over several diffuse bounces; an opal acrylic diffuser under the film smooths it, the black parts above the diffuser absorb stray light, and the camera photographs the film against the even glow](drawings/optics.svg)

1. **The flash fires sideways into the cavity, never at the film.** It lies flat on the desk with its light face at the fully open front, aimed into the box. The trigger receiver stays outside with it.
2. **The white cavity does the mixing.** The bare white filament walls and ceiling scatter the light in every direction over several diffuse bounces, the way an [integrating cavity](docs/glossary.md#integrating-cavity) does. There is no reflector plate and nothing to adjust inside.
3. **One opal acrylic diffuser does the smoothing.** A 68 × 118 × 2 mm diffuser sits in a shallow recess in the cover-stage, under the 62 × 95 mm light window and 4.6 mm below the film. Dust on it never shows in the image, because the diffuser itself is the glowing surface. Wipe it occasionally and move on.
4. **Everything above the diffuser is black.** The holders, inserts and mask are printed in black filament. An optional flocking sheet (a velvet-like sheet) on the cover-stage face removes the last of the glare. Stray light is absorbed before it can veil the image.
5. **Nothing touches the image area.** The film rests on narrow raised lands along its non-image edges. Above it sits a pressure element on the 4.6 mm element ledge, leaving a 0.4 mm channel across the full frame. With the printed pressure-window insert, any bow in the film stays within 0.28 mm (inside the depth of field at 1:1 and f/8). The optional [anti-Newton](docs/glossary.md#newton-rings) glass covers the whole frame continuously without Newton rings. You advance frames by pulling the strip through, so you never open the holder mid-roll.

<details>
<summary>Why the flash stays outside the box</summary>

Earlier NeoBox revisions sealed the speedlight inside the enclosure. The box then had to be sized around the largest supported flash, and changing its batteries meant opening the box. v1 leaves the front wall entirely open. The flash lies on the desk and fires in, so the enclosure no longer depends on any flash dimension, any brand works, and the radio receiver sits outside where nothing blocks its signal.

Fully diffuse light also has a side benefit known from darkroom enlargers. Fine scratches and grain look softer than under directional light.

</details>

## Documentation

Read in this order. Everything below the line is reference material you can reach from anywhere.

```mermaid
flowchart LR
  A[Getting started] --> B[Bill of materials]
  B --> C[3D printing]
  C --> D[Assembly]
  D --> E[Scanning]
  E --> F[Troubleshooting]
```

| Document | Read this if… |
|---|---|
| [Getting started](docs/getting-started.md#getting-started) | You are new to this and want to know whether the project suits you, what it really costs, and how long it takes end to end. |
| [Bill of materials](docs/bom.md#bill-of-materials-and-sourcing) | You are about to buy. Parts, tools and consumables, sourcing in China, Japan and elsewhere, and copy-paste vendor scripts. |
| [3D printing](docs/printing.md#printing) | You are about to print, or to brief a print service. One settings block, a card per part, and acceptance checks. |
| [Assembly](docs/assembly.md#assembly) | The parts have arrived. Pressing in the magnets, the stack order, a checkpoint at every step, and the mirror levelling trick. |
| [Scanning](docs/scanning.md#scanning) | The box is built and you want negatives. Camera, lens, magnification, the camera tube, parallelism, focus, exposure, loading film, inversion. |
| [Troubleshooting](docs/troubleshooting.md#troubleshooting) | Something is wrong. Symptom, likely cause and fix, across printing, assembly, light and capture. |
| [Glossary](docs/glossary.md#glossary) | A word in these documents means nothing to you. One line per term, plus why it matters here. |
| [Design](docs/design.md#design) | You want the engineering: the dimension chain, the optical decisions, and how to work with the Blender source. |
| [Design log](docs/design-log.md#design-log) | You want to know why it is shaped like this, and which alternatives were tried and rejected. |
| [Contributing](CONTRIBUTING.md#contributing-to-neobox) | You want to send a patch. Which files are generated, the export and verify gate, and the three-language rule. |

## Quick start

- [ ] **1. Check that it suits you**: what you must already own, and a realistic timeline. → [Getting started](docs/getting-started.md#getting-started)
- [ ] **2. Buy**: one opal acrylic diffuser cut to 68 × 118 × 2 mm, 32 Ø8 × 2 mm N35 magnets, 4 steel washers, and optionally one 64 × 95 × 2 mm anti-Newton glass and a flocking sheet. → [Bill of materials](docs/bom.md#tools-and-consumables)
- [ ] **3. Print**: 12 STL files in two colours (3 white, 9 black), plain PLA, no supports. Every part prints on a flat face. The white filament must be **matte**. Silk or glossy white leaves mirror-like reflections in the cavity. → [3D printing](docs/printing.md#printing)
- [ ] **4. Assemble and calibrate**: press in the magnets and stack the parts. No screws, no tools. Then set a small mirror on the stage and centre the lens's own reflection in the viewfinder. The sensor is now parallel to the film plane. → [Assembly](docs/assembly.md#assembly)
- [ ] **5. Scan**: focus on the grain, meter, and shoot a roll. → [Scanning](docs/scanning.md#scanning)

> [!TIP]
> **[Bed size](docs/glossary.md#bed-size) is no longer a constraint.** The largest part is 154.8 mm long, so a 160 × 160 mm build plate is enough. Every mainstream printer qualifies, and the large-bed warnings from earlier revisions no longer apply.

## Repository layout

| Path | Contents | Kind |
|---|---|---|
| [`cad/neobox.blend`](cad/neobox.blend) | Blender source: the authoritative geometry for every part | Source |
| [`cad/film-stage-aluminium-3mm.dxf`](cad/film-stage-aluminium-3mm.dxf) | The aluminium film stage of the printed prototype, now superseded. In v1 the stage is merged into the cover-stage | Historical |
| [`cad/legacy-plywood/`](cad/legacy-plywood/) | Two DXFs left from the abandoned plywood route. Not a complete build, kept for the record | Historical |
| [`stl/white-pla/`](stl/white-pla/) | `main-body.stl`, `cover-stage.stl`, `cover-stage-4x5.stl` | Generated |
| [`stl/black-pla/`](stl/black-pla/) | Four film-holder parts, two pressure-window inserts, `mask-6x6.stl`, `slide-plate-135.stl` and `sheet-plate-4x5.stl` | Generated |
| [`drawings/`](drawings/) | Optical path, cross-section, print orientation, exploded view, capture setup and manufacturing overview, in three languages, regenerated from the generators in `tools/drawings/` | Generated |
| [`docs/`](docs/) | The documentation set, each file in English, 简体中文 and 日本語 | Source |
| [`tools/export_stl.py`](tools/export_stl.py) | The committed exporter. Regenerates the twelve STL files from `cad/neobox.blend` | Source |
| [`tools/drawings/`](tools/drawings/) | The drawing generators. Regenerate the 18 SVG files under `drawings/` | Source |
| [`tools/verify_stl.py`](tools/verify_stl.py) | The geometry gate. Checks watertightness, the 0.2 mm z-grid and every bounding box | Source |
| [`tools/camera_tube.py`](tools/camera_tube.py) | The camera-tube generator. Builds the base and a lens column for your lens from four measured numbers | Source |

## Adapting to a different flash

There is nothing to adapt. The reference build is a NEEWER TT560 with a ZENIKO T1 trigger set, but no dimension in the geometry depends on either. The flash lies flat on the desk with its head at the fully open front. The receiver stays outside the box, where nothing blocks its radio signal and you can change its batteries without touching anything.

Choosing a substitute takes one criterion: **manual power control**. TTL automatic metering and HSS (high-speed sync) are useless here. Do not pay for them. There is nothing to re-derive and no CAD to edit. Set the flash down, aim its head into the opening, re-meter, shoot. The dimension chain that actually sets the enclosure (window, cavity, film plane) is in [Design § 2](docs/design.md#2-dimension-chain).

> [!TIP]
> Never fix the outer height first and back-calculate the layers. Sum the layers, then read off the height. Doing it the other way round made the first draft physically unbuildable. That is entry 1 of the [design log](docs/design-log.md#design-log).

## Status

First release, v1 geometry, built and in use.

- **Verified in software:** all twelve STL files are watertight single solids with zero non-manifold edges. Every horizontal face sits on the 0.2 mm layer grid in its print orientation, and every bounding box matches the published dimensions. Run `tools/verify_stl.py` to reproduce this.
- **Verified in plastic:** the author has printed this geometry and has been scanning 135 and 120 film with it since. Friends have run it with their own flashes and film. The 6×6 mask, the slide plate and the 4×5 stage have also been printed and used.
- Every evenness figure quoted in the documents is still a **design target** from the CAD. None is an instrument measurement. The box scans evenly by eye and in the inversions, but no flat-field numbers have been written up yet.
- The decision to use a single diffuser came from the author's existing light-pad workflow, and the printed box has confirmed it.
- The film-flatness figures (the 0.4 mm channel, the ≤ 0.28 mm bow under the printed insert) come from the CAD stack and the tolerance analysis. They are not measurements of real film in a real holder.

If you build one, the project would still like to hear what came out tight, loose or uneven on your printer.

## Licence and credits

Designed by [Neo Analog Lab Inc. (ネオアナログラボ株式会社)](https://github.com/Neoanaloglab). Released under the [MIT License](LICENSE). Build it, sell it, modify it. No permission needed.

---

[Documentation index](#documentation) · [Getting started](docs/getting-started.md#getting-started) →
