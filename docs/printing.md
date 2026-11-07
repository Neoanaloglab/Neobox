# Printing

**English** · [简体中文](printing.zh-CN.md) · [日本語](printing.ja.md)

> How to print the twelve NeoBox parts: why almost any printer can do it, one set of settings for the whole build, a card for each file, and the checks to run before you assemble anything.

**Contents:** [Will it fit your printer?](#will-it-fit-your-printer) · [Print settings](#print-settings) · [Filament](#filament) · [The twelve parts](#the-twelve-parts) · [Print one 135 holder first](#print-one-135-holder-first) · [Check each part before you assemble](#check-each-part-before-you-assemble) · [If it came out tight or loose](#if-it-came-out-tight-or-loose) · [Ordering from a print service](#ordering-from-a-print-service)

Twelve STL files: **eight for the default build plus four optional: the 6×6 mask, the slide plate for mounted slides, and the 4×5 cover-stage and sheet plate**. Three are white, nine are black. All are 1:1 in millimetres. All print without supports. The default build takes about **300–350 g of filament, roughly a third of what the printed prototype needed**.

![One-page manufacturing overview: the printed parts, the bought parts, and the print notes for each](../drawings/manufacturing-overview.svg)

> [!CAUTION]
> Never let a slicer scale these files. "Scale to fit the build plate" is the single most common way a print order goes wrong. The files are already 1:1, and every check below assumes they stayed that way.

> [!NOTE]
> The settings on this page come from the geometry. They were not read off a machine. The box has been printed and used, but the values below are the design values, checked in CAD (`cad/neobox.blend` is the authority). They are not the log of one particular printer.

---

## Will it fit your printer?

Yes, almost certainly. The largest parts in the set, the main body and the cover-stage, take up 124.8 × 154.8 mm on the plate. The tallest part is the main body, at 75.6 mm. **A 160 × 160 mm bed prints everything.** Today that means practically every desktop machine, including the smallest current ones. The old warnings about oversized parts and sending the enclosure out to a print service went away with the prototype.

| Part | Footprint on the plate | Height |
|---|---|---|
| `main-body.stl` | 124.8 × 154.8 | 75.6 |
| `cover-stage.stl` | 124.8 × 154.8 | 10.0 |
| `film-holder-*-base.stl` (both) | 94 × 120 | 5.0 |
| `film-holder-*-lid.stl` (both) | 94 × 120 | 3.0 |
| `pressure-window-*.stl` (both) | 64 × 95 | 2.0 |
| `mask-6x6.stl` | 94 × 80 | 1.0 |
| `slide-plate-135.stl` | 94 × 120 | 5.0 |
| `cover-stage-4x5.stl` | 124.8 × 154.8 | 10.0 |
| `sheet-plate-4x5.stl` | 112 × 138 | 5.0 |

---

## Print settings

One block of settings covers the whole build. Every other mention of a print setting in this repository points back to this one.

| Setting | Value | Why it is this value |
|---|---|---|
| Scale | 100 %, millimetres | The files are already 1:1. |
| Filament | Plain PLA: white for the two enclosure parts, black for the rest | See [Filament](#filament). |
| [Layer height](glossary.md#layer-height) | **0.2 mm on every part** | Every height in the design sits on a 0.2 mm grid. At 0.2 every face lands exactly on a layer boundary, so a printed 0.4 step is a true 0.4 step. |
| [Infill](glossary.md#infill) | 15 % | No part carries a load beyond the parts stacked on top of it. |
| [Supports](glossary.md#supports) | **None, on any part** | Every part is designed to print without supports in the orientation shown on its card. |

> [!IMPORTANT]
> If your slicer proposes support anywhere, the part is oriented wrong. Go back to its card. There is also no [bridging](glossary.md#bridging) to tune. The longest bridge in the whole build is the 3.3 mm roof of the locating notches under the cover-stage, and default settings handle it without trouble.

<details>
<summary>Why the geometry is quantised to 0.2 mm, and what that buys you</summary>

The manufacturing rule behind every part in this project: **every horizontal face sits on a 0.2 mm grid in the part's print orientation, and no exposed step is thinner than 0.4 mm.** Both rules came out of real print-service orders going wrong ([design log entry 18](design-log.md#18-layer-quantised-holders), and entry 20 for orientation). They are the reason a print shop's default profile produces a working part.

| Part | Horizontal faces, measured from the plate (mm) |
|---|---|
| `main-body.stl` | 0 · 3.0 · 73.0 · 75.6 |
| `cover-stage.stl` | 0 · 2.8 · 3.6 · 5.0 · 6.0 · 10.0 |
| Holder bases (both) | 0 · 2.2 · 3.8 · 4.2 · 4.6 · 5.0 |
| Holder lids (both, printed top face down) | 0 · 1.0 · 3.0 |

Every number is a multiple of 0.2 mm. The finest exposed steps in the build are the 0.4 mm land and ledge steps on the holder bases. Those are exactly the steps that define the film plane. That is why the spec pins the layer height to 0.2 mm on every file. Each of those faces then lands exactly on a layer boundary, a printed 0.4 step is two clean layers, and nothing is left to slicer rounding. A coarser layer such as 0.28 is slightly cheaper, but it drops the grid between layer boundaries and blurs exactly the steps the film plane depends on.

</details>

**Nozzle.** Nothing in the build is finer than the 0.4 mm steps on the holder bases, and no wall is thinner than 2.4 mm. A standard 0.4 mm nozzle handles every part.

---

## Filament

### Plain PLA, two colours

The spec is ordinary PLA throughout. No engineering filaments, no specialty finishes.

**White for the three enclosure parts: the main body and either cover-stage.** The inside of the main body is the reflector. The flash fires into the fully open front. Its light reaches the film only after bouncing between the white walls and the white underside of the cover-stage. The bare white surface *is* the optical surface.

> [!IMPORTANT]
> Use plain white PLA (not silk, satin or another specialty finish) and leave the interior faces untouched: no paint, no sanding, no coating. How much light the bare white walls reflect is part of the optical design.

**Black for the nine parts near the film.** Everything the film sees at close range is black, to absorb stray light: holder bases and lids, pressure windows, the mask, the slide plate, the sheet plate.

**Quantity.** About **300–350 g for the default build**, roughly a third of the prototype build. The optional slide plate adds about 25 g, and the 4×5 pair about 35 g. One spool of each colour covers it many times over.

---

## The twelve parts

![Side views of the printed parts on the build plate](../drawings/print-orientation.svg)

### Part vocabulary

The print instructions here always name a feature you can see on the part. They never refer to a hidden face. This is what the words mean:

| Word used here | What you are looking at |
|---|---|
| Rail | One of the two long outer ridges on a holder base. It runs in the direction the film travels |
| Land | The narrow raised shelf along each rail. The film edges ride on it |
| Element ledge | The 4.6 mm step cut into each rail. The pressure element sits on it |
| Channel | The 0.4 mm gap between the land and the pressure element. The film slides through it |
| Window | The rectangular hole you photograph through |
| Pressure element | Whatever sits on the element ledge: a printed pressure-window insert by default, or the optional anti-Newton glass |
| Tenon | One of the four small locating tabs on top of the main-body side walls |
| Notch | One of the four corner sockets in the underside of the cover-stage. The tenons locate into them |
| Tray flange | The raised rim on top of the cover-stage. The film holder sits inside it |
| Pocket | The 51.4 mm square recess in the top of the slide plate. A mounted slide drops into it |
| Finger well | One of the two small blind recesses at the sides of the pocket. They let you lift the mount out |
| Edge notch | One of the two open cuts in the short sides of the sheet plate. They let you lift a sheet out |

> [!CAUTION]
> Two orientation traps, one for the holder bases and one for the holder lids. The holder **bases** print flat face down. Never put the railed side toward the plate. If you do, the lands and ledges hang over air and the channel will not come out. The holder **lids** are the opposite case. Their flat **top** face goes down, so that the shallow recess and the magnet pockets face up. A misoriented holder reached a vendor once already ([design log entry 20](design-log.md)). That is why every card below places its part by a feature you can see.

### [main-body.stl](../stl/white-pla/main-body.stl)

- **White.** 124.8 × 154.8 × 75.6, the biggest part in the set and the one that takes longest to print.
- **On the plate:** the flat floor down. Three walls rise from it. The fourth side is the fully open front, and it has no wall at all. That is the design, and the file is not broken. The four locating tenons ride on top of the side walls.
- **Supports: none.** The open front is a missing wall, so there is no overhang there. Nothing on this part hangs over air.
- **Watch:** the interior faces are optical. No sanding, no paint.

### [cover-stage.stl](../stl/white-pla/cover-stage.stl)

- **White.** 124.8 × 154.8 × 10.0. This single part replaces the prototype's top cover and film stage.
- **On the plate:** the flat face with the four corner notches goes down, and the raised tray flange faces up.
- **Supports: none.** The notch roofs bridge 3.3 mm. They are the longest bridges in the build, and still nothing to worry about.
- **On this part:** the 62 × 95 light window, the recessed seat for the opal acrylic just below the deck surface, four small square counterbores for the steel shims, and the tray flange that locates the film holder.

### [film-holder-135-base.stl](../stl/black-pla/film-holder-135-base.stl)

- **Black.** 94 × 120 × 5.0. Window 25 × 37.
- **On the plate:** flat face down, with the two long rails pointing up. Short guide ribs at each end of the channel lead the film in.
- **Supports: none.** Every magnet pocket and every step opens upward.
- **Watch:** the land and the element ledge on this part define the film plane. This is where 0.2 mm layers pay off, if you use them.

### [film-holder-135-lid.stl](../stl/black-pla/film-holder-135-lid.stl)

- **Black.** 94 × 120 × 3.0. Window 25 × 37.
- **On the plate: top face down.** The flat face with nothing on it but the window goes against the plate. The face with the shallow rectangular recess and the eight magnet pockets points up.
- **Supports: none.** In this orientation the recess and the pockets all open upward.

### [film-holder-120-base.stl](../stl/black-pla/film-holder-120-base.stl)

- **Black.** 94 × 120 × 5.0. Window 57 × 85 (a full 6×9 frame) with a 62 mm wide channel.
- **On the plate:** flat face down, with the two long rails pointing up.
- **Supports: none.**
- **Watch:** same as the 135 base. The land and ledge are the film plane.

### [film-holder-120-lid.stl](../stl/black-pla/film-holder-120-lid.stl)

- **Black.** 94 × 120 × 3.0. Window 57 × 85.
- **On the plate: top face down**, exactly like the 135 lid. Recess and magnet pockets up.
- **Supports: none.**

### [pressure-window-135.stl](../stl/black-pla/pressure-window-135.stl)

- **Black.** 64 × 95 × 2.0, window 25 × 37. The default pressure element for 135 film. It sits on the element ledge of the 135 base.
- **On the plate:** lies flat, flat side down.
- **Supports: none.**

### [pressure-window-120.stl](../stl/black-pla/pressure-window-120.stl)

- **Black.** 64 × 95 × 2.0, window 57 × 85. The default pressure element for 120.
- **On the plate:** lies flat, flat side down.
- **Supports: none.**
- **Note:** the two pressure windows are the format-specific pressure elements, one for each format. The optional anti-Newton glass upgrade is a single 64 × 95 sheet that serves both formats.

### [mask-6x6.stl](../stl/black-pla/mask-6x6.stl) — optional

- **Black.** 94 × 80 × 1.0, window 56.5 × 56.5.
- **On the plate:** lies flat.
- **Supports: none.**
- **Print it only if** you shoot the 6×6 format. It goes into the tray under the 120 base and masks the window down to a square. There is no 6×4.5 mask. Crop 6×4.5 afterwards, when you edit the scan.

### [slide-plate-135.stl](../stl/black-pla/slide-plate-135.stl) — optional

- **Black.** 94 × 120 × 5.0. Square pocket 51.4 × 51.4, 2.0 deep. Window 26 × 38 through the pocket floor. Two finger wells.
- **On the plate:** flat face down, with the pocket and the finger wells opening upward.
- **Supports: none.** Every recess opens upward and the window is a through hole.
- **Print it only if** you have mounted 135 slides. It stands in the tray in place of the 135 holder set, and the mount drops into the pocket. It has no lid, no magnets and no pressure element.

### [cover-stage-4x5.stl](../stl/white-pla/cover-stage-4x5.stl) — optional

- **White.** 124.8 × 154.8 × 10.0 and the cover-stage's outline. It carries a 102 × 126 light window, a recess for a 106 × 130 × 2 opal sheet and a 112.6 × 138.6 tray. No washer pockets.
- **On the plate:** exactly like the cover-stage. The flat face with the four corner notches goes down, and the raised tray flange faces up.
- **Supports: none.** The same notch roofs as the cover-stage.
- **Print it only if** you shoot the 4×5 format. It replaces the cover-stage on the same main body. Its underside faces the cavity, so no sanding and no paint.

### [sheet-plate-4x5.stl](../stl/black-pla/sheet-plate-4x5.stl) — optional

- **Black.** 112 × 138 × 5.0. Pocket 102.2 × 127.6, 2.0 deep. Window 97 × 121 through the pocket floor. Two edge notches on the short sides.
- **On the plate:** flat face down, with the pocket and the notches opening upward.
- **Supports: none.**
- **Print it only if** you shoot the 4×5 format. It stands in the 4×5 cover-stage's tray, and the sheet drops into the pocket. It has no lid, no magnets and no pressure element.

---

## Print one 135 holder first

Print `film-holder-135-base.stl`, `film-holder-135-lid.stl` and `pressure-window-135.stl` before you commit to the rest. They are among the smallest parts in the set, and together they test every fit that matters: the magnet pockets, the element ledge, and the 0.4 mm channel.

Four things to check on that first set:

- **The ledge.** The pressure window drops onto the 4.6 mm element ledge and sits flat, and the lid closes over it. A little play is by design. The lid's recess limits the element's float to 0.4 mm.
- **The channel.** With the insert seated and the lid closed, a strip of film pulls through smoothly, with no binding or scraping.
- **The magnets.** A Ø8 × 2 magnet presses into each pocket. The fit is a designed interference, so it is meant to be tight. Check which way round the base and lid magnets attract *before* you press them home, because they do not come back out easily.
- **Flatness.** The base sits flat with no rocking. It carries the film plane.

If any of these is wrong, fix it here (see [If it came out tight or loose](#if-it-came-out-tight-or-loose)). Then print the remaining black parts, and the two white parts last.

---

## Check each part before you assemble

Run these checks as parts come off the machine, or out of the box from a print service. The first three catch a slicer that scaled a file.

- [ ] `main-body.stl` measures 124.8 × 154.8 on the outside.
- [ ] `cover-stage.stl` measures 124.8 × 154.8, and its four notches settle onto the main body's four tenons under their own weight.
- [ ] Every holder part measures 94 × 120 in outline, base and lid alike.
- [ ] The pressure windows measure 64 × 95 and drop onto the element ledge of their base.
- [ ] Ø8 × 2 magnets press into every pocket in every base and lid.
- [ ] With the insert in and the lid closed, a film strip pulls through each holder you printed.
- [ ] If you printed it: `mask-6x6.stl` measures 94 × 80 and sits in the tray under the 120 base.
- [ ] If you printed it: `slide-plate-135.stl` measures 94 × 120 and sits in the tray. A mounted slide drops into its pocket and lifts out by the finger wells.
- [ ] If you printed them: `cover-stage-4x5.stl` settles onto the four tenons like the cover-stage, and `sheet-plate-4x5.stl` measures 112 × 138 and sits in its tray.
- [ ] Nothing inside the main body has been sanded, polished or painted. The bare white surface is the reflector.

Anything that fails has a remedy below, or in [troubleshooting](troubleshooting.md#printing).

---

## If it came out tight or loose

The fits below are listed from tightest to loosest. XY compensation is called *XY size compensation* in PrusaSlicer and OrcaSlicer, and *Horizontal expansion* in Cura. Change it in small steps. Reprint one part only, and never the whole set.

| Fit | Nominal | Too tight | Too loose |
|---|---|---|---|
| Film channel | 0.4 mm between land and pressure element | Check that the element is fully seated on its ledge. Then trim any burrs (rough edges) off the land edges and the element edges with a hobby knife. If film still binds, reprint the base at 0.2 mm layers (that lands the land and ledge exactly on layer boundaries) before you reach for XY compensation. | A slight rattle is normal. The film is only about 0.12–0.18 mm thick in a 0.4 mm channel, and the channel presses the film flat as it is pulled through. |
| Pressure element on its ledge | 64 × 95 on the ledge | Lightly ease the *element's* edges with fine sandpaper. Sand only the element. Never sand the ledge. | Fine. The lid's recess limits the element's float to 0.4 mm. |
| Cover-stage notches on the tenons | four tenons, 2.4 × 12 | Ease the notch mouths with a knife. If that is not enough, enable [elephant-foot](glossary.md#elephant-foot) compensation on a reprint. | Harmless. The notches locate the cover-stage, and gravity holds it. |
| Magnet pockets | Ø8 × 2 magnets | The interference is designed. Press squarely and firmly. If a magnet genuinely will not start, ease the pocket rim with a knife. Never hammer a neodymium magnet. It chips. | A drop of cyanoacrylate. The pocket locates the magnet, and the glue holds it. |

> [!CAUTION]
> Never sand, file or "clean up" the land or the element ledge to free a tight channel. Those two steps *are* the film plane. Material removed there is a film-flatness error you cannot undo. Fix a tight channel in the slicer (0.2 mm layers, a touch of XY compensation) or on the removable element. Never fix it on the base's steps.

---

## Ordering from a print service

Even with no printer at all, this is now a small order: twelve files (four optional), about 300–350 g of plain PLA, no supports, and every part fits a 160 × 160 mm bed. Send this text as it is. It names every file and places each one by a feature the operator can see.

```text
12 STL files: 8 required + 4 optional (mask-6x6, slide-plate-135, cover-stage-4x5, sheet-plate-4x5). Millimetres, 1:1. DO NOT SCALE.

Plain PLA. Layer height 0.2 mm on every part. Infill 15%. NO SUPPORTS on any part.
Everything fits a 160 x 160 mm bed.

WHITE PLA - 2 parts + 1 optional:
  main-body.stl        124.8 x 154.8 x 75.6. Flat floor on the plate, walls up.
                       One side has no wall - that is the design, not an error.
                       Do not sand, paint or coat the inside faces.
  cover-stage.stl      124.8 x 154.8 x 10. The flat face with the four corner
                       sockets goes on the plate; the raised rectangular frame
                       faces up.
  cover-stage-4x5.stl (OPTIONAL)  Same placement as cover-stage.stl.

BLACK PLA - 6 parts + 3 optional:
  film-holder-135-base.stl  Flat face on the plate, the two long ridges up.
  film-holder-120-base.stl  Same placement.
  film-holder-135-lid.stl   FLAT TOP FACE on the plate. The face with the
  film-holder-120-lid.stl   shallow recess and eight magnet holes faces UP.
  pressure-window-135.stl   Thin flat plate, lies flat.
  pressure-window-120.stl   Thin flat plate, lies flat.
  mask-6x6.stl (OPTIONAL)   Thin flat plate, lies flat.
  slide-plate-135.stl (OPTIONAL)  Flat face on the plate, square pocket up.
  sheet-plate-4x5.stl (OPTIONAL)  Flat face on the plate, pocket up.
```

**Ask three questions before you pay.** Print services take the order first and discover the problem afterwards.

1. Will every file print at 100 % scale, in millimetres, with no "scale to fit"?
2. Is the white filament plain PLA, not silk, not glossy?
3. Will you place the two holder lids top face down, exactly as written?

**If the shop pushes back on the settings,** let them run their default profile. The geometry is quantised so that defaults work. Every horizontal face is on a 0.2 mm grid, and no exposed step is under 0.4 mm. The only instructions that really matter are "do not scale", the orientations, and "no supports".

Versions of this text in the vendor's own language (Chinese for Taobao, Japanese for Japanese services) are in [vendor scripts](bom.md#vendor-scripts). That page also tells you where to buy everything you buy rather than print.

---

← [Bill of materials](bom.md) · [Documentation index](../README.md#documentation) · [Assembly](assembly.md) →
