# Design

**English** · [简体中文](design.zh-CN.md) · [日本語](design.ja.md)

> The engineering reference: where every dimension comes from, which numbers are optical and which are structural, what happens if you change one, and how to open, edit, re-export and verify the CAD source.

**Contents:** [1. Light path](#1-light-path) · [2. Dimension chain](#2-dimension-chain) · [3. Optical decisions](#3-optical-decisions) · [4. Cover-stage](#4-cover-stage) · [5. Film holders](#5-film-holders) · [6. Enclosure](#6-enclosure) · [7. Focus light](#7-focus-light) · [8. Flash operation](#8-flash-operation) · [9. Repositioning and repeatability](#9-repositioning-and-repeatability) · [10. 4×5 on the v1 body](#10-45-on-the-v1-body) · [11. Working with the source](#11-working-with-the-source)

Reference flash: a **NEEWER TT560** speedlight with a **ZENIKO T1** 2.4 GHz trigger set. It is a reference, not a requirement. The flash lies on the desk *outside* the box, so no dimension in this document depends on it; any speedlight with manual power control works.

| Convention | What it means here |
|---|---|
| Dimensions | Millimetres, written width × depth × height (X × Y × Z) |
| `z` | Absolute height above the desk. The box stands directly on the desk, so this is also the height above the outer bottom of the main body |
| Part-local z | The layer-quantisation tables in [§2](#2-dimension-chain) measure each part from its own print-bed face instead; stated where used |
| XY positions | Measured from the centre of the box, which is also the centre of the light window |
| STL bounding box | Quoted only where it is labelled as such; it is sorted largest first and is often not in X × Y × Z order |
| Source | Every number below is read from `cad/neobox.blend` or from the exported STL files. [§11](#11-working-with-the-source) explains how to read them yourself |

> [!IMPORTANT]
> The geometry is verified dimensionally in Blender and numerically in the exported STL files. **The box has never been printed, built, photographed or measured.** Every performance figure in this document is a design target, not a result: the mixing margins, the ≤ 0.28 mm flatness bound, the depth-of-field coverage. No evenness has been measured, and nothing here claims otherwise.

---

## 1. Light path

![Cross-section drawing of the NeoBox](../drawings/cross-section.svg)

The stack, desk upward:

**flash lying flat on the desk → the fully open front → white cavity 120 × 150 × 70 → light window 62 × 95 in the cover-stage → opal acrylic 68 × 118 × 2, top face at 78.6 → 4.6 mm of air → film plane at z = 83.2.**

The flash is not inside the box. It lies flat on the same desk the box stands on, its head against the **open front** (the front face of the box has no wall at all) and fires horizontally into the cavity. The TT560's emitting face is 60 × 45 with its centre 31 mm above the desk, well inside the 70 mm-tall opening.

**Nothing is aimed at the film.** The light window is in the ceiling of the cavity, at right angles to the beam, so light reaches it only after several diffuse bounces off the bare white PLA. That is what makes the interior an [integrating cavity](glossary.md#integrating-cavity) rather than a lamp with a shade. It leaves through the 62 × 95 window and gets its final smoothing from one [opal](glossary.md#opal) acrylic sheet recessed into the cover-stage directly above.

The open front is the whole v1 architecture in one move. The printed prototype (internal revision 4) sealed the flash inside the box, and everything difficult about the prototype followed from that: the box height was derived from the flash's thickness, an access panel was needed to reach the power dial, a cable gland to pass wires, and the published STLs fitted one flash model and no other. With the flash outside, all of it disappears: any brand of flash works, the receiver stays on the desk where its radio signal is clean and its batteries are reachable, and there is no panel, gland or ventilation question left to answer ([§6](#6-enclosure)). The price is that ambient light can enter the cavity. That trade is accepted, not ignored: the flash pulse is far brighter than room ambient at sync speed ([§8](#8-flash-operation)).

> [!NOTE]
> **Work in a dim room, and keep ceiling lamps from shining straight into the opening.** The pulse overwhelms ambient light by design, but a bright lamp aimed into the open front is the one geometry that erodes that margin for free.

---

## 2. Dimension chain

In the prototype the box was derived from the flash, and its numbers died with it. v1 severs the link: the flash never enters the box, so the chain no longer starts at a product's datasheet. It starts at the desk and runs upward, part stacked on part, by gravity.

### The printed parts

Twelve STL files, three white and nine black, all printed without supports:

| STL | Colour | Overall (mm) | What it is |
|---|---|---|---|
| `main-body.stl` | white | 124.8 × 154.8 × 75.6 | Main box: 3.0 floor, 2.4 left/right/rear walls, front fully open; four locating tenons 2.4 × 12 × 2.6 on the side-wall tops |
| `cover-stage.stl` | white | 124.8 × 154.8 × 10.0 | Cover-stage: 6 mm plate seated on the walls, with light window, acrylic recess, washer pockets and holder tray ([§4](#4-cover-stage)) |
| `film-holder-135-base.stl` | black | 94 × 120 × 5 | 135 holder base: 25 × 37 window, inner guide rails, outer rails with the 4.6 element ledge ([§5](#5-film-holders)) |
| `film-holder-135-lid.stl` | black | 94 × 120 × 3 | 135 holder lid: 25 × 37 window, element cavity, 8 magnet pockets |
| `film-holder-120-base.stl` | black | 94 × 120 × 5 | 120 holder base: 57 × 85 window (full 6×9), 62 channel, same outer rails and ledge as the 135 |
| `film-holder-120-lid.stl` | black | 94 × 120 × 3 | 120 holder lid: 57 × 85 window, otherwise identical to the 135 lid |
| `pressure-window-135.stl` | black | 64 × 95 × 2 | Pressure-window insert, 135 (window 25 × 37) |
| `pressure-window-120.stl` | black | 64 × 95 × 2 | Pressure-window insert, 120 (window 57 × 85) |
| `mask-6x6.stl` | black | 94 × 80 × 1 | 6×6 mask (window 56.5 × 56.5), laid in the tray under the 120 base |
| `slide-plate-135.stl` | black | 94 × 120 × 5 | Slide plate for mounted 135 slides: 51.4 × 51.4 pocket, 26 × 38 window, two finger wells; a fourth holder set in one piece ([§5](#5-film-holders)) |
| `cover-stage-4x5.stl` | white | 124.8 × 154.8 × 10.0 | 4×5 cover-stage: the cover-stage's outline, plate and four notches with a 102 × 126 light window, a 107 × 131 acrylic recess and a 112.6 × 138.6 tray; no washer pockets ([§10](#10-45-on-the-v1-body)) |
| `sheet-plate-4x5.stl` | black | 112 × 138 × 5 | 4×5 sheet plate: 102.2 × 127.6 pocket, 97 × 121 window, two edge notches; stands in the 4×5 cover-stage's tray |

Every part prints flat face down; the two lids print top face down. The largest part is 154.8 mm long, so a 160 × 160 print bed is enough. Layer heights, orientation cards and slicer settings are in [printing.md](printing.md).

### Height

The whole assembly is one gravity stack. World z, desk = 0:

| Layer | z range | Note |
|---|---|---|
| Desk | 0 | the flash and the box stand on the same surface |
| Main-body floor | 0 – 3.0 | |
| Cavity | 3.0 – 73.0 | interior 120 × 150 × 70, open at the front |
| Cover-stage plate | 73.0 – 79.0 | 6 mm plate seated on the wall tops; deck face at 79.0 |
| Opal acrylic | 76.6 – 78.6 | in its recess, top face 0.4 below the deck |
| Steel washers | 78.0 – 79.0 | in their pockets, flush with the deck |
| Tray flange | 79.0 – 83.0 | rim around the holder seat, 4 high |
| Holder base | 79.0 – 84.0 | stands on the deck inside the flange; the slide plate occupies the same 5 mm |
| **Film plane** | **83.2** | land top; the same height for both formats |
| Slide film plane | ≈ 82.6 – 83.6 | in the slide plate: pocket floor at 82.0 plus about half the mount's thickness; refocus |
| 4×5 film plane | ≈ 82.2 | a sheet lying on the sheet plate's pocket floor at 82.0; refocus |
| Pressure element | 83.6 – 85.6 | insert or AN glass on the 4.6 ledge |
| Holder lid | 84.0 – 87.0 | total assembled height 87 |

### Width and depth

The main body is 124.8 × 154.8 outside; the walls are 2.4, the front is open, so the interior cavity is **120 × 150 × 70** and the open front is the cavity's full 120 × 70 cross-section. The 62 × 95 light window is centred, which leaves **29 mm of white wall in x and 27.5 mm in y** between the window edge and the nearest wall: the mixing margin. It is deliberately generous by design; no minimum has been established, and nothing has been measured.

### Generalising to another flash

There is nothing to re-derive. The prototype-era formulas that turned a flash datasheet into a box height are gone because the input is gone: **no dimension of the v1 box encodes any dimension of any flash.** A substitute flash needs manual power control and a head that can lie flat and fire level into the open front. The TT560's emitting face, 60 × 45 with its centre 31 above the desk, is the reference, not a limit. The receiver stays outside too, so the trigger model is equally free. Swapping flashes touches neither `cad/neobox.blend` nor the STLs ([§11](#11-working-with-the-source)).

### Layer quantisation

**Every printed z-feature in this design is an exact multiple of 0.2 mm, and no exposed horizontal step is under 0.4 mm (two layers).** Each part is quantised in its own print orientation, measured from its own print-bed face:

| Part (datum = print-bed face) | z stations |
|---|---|
| Main body | 0 · 3.0 floor top · 73.0 wall top · 75.6 tenon top |
| Cover-stage | 0 · 2.8 notch ceiling · 3.6 acrylic-recess floor · 5.0 washer-pocket floor · 6.0 deck · 10.0 flange top |
| Holder bases (both formats) | 0 · 2.2 magnet-pocket floor · 3.8 plate face · **4.2 land** · **4.6 element ledge** · 5.0 rail top |
| Holder lids (printed top face down) | 0 · 1.0 element-cavity ceiling · 3.0 lid underside (assembly-local 8.0 / 7.0 / 5.0) |
| Inserts / mask | flat plates, 2.0 / 1.0 |
| Slide plate | 0 · 1.0 finger-well floor · 3.0 pocket floor · 5.0 top |
| 4×5 cover-stage | 0 · 2.8 notch ceiling · 3.6 acrylic-recess floor · 6.0 deck · 10.0 flange top |
| Sheet plate | 0 · 1.0 notch floor · 3.0 pocket floor · 5.0 top |

The point of the grid: at a 0.2 mm [layer height](glossary.md#layer-height) every one of those stations lands exactly on a layer boundary, so a printed 0.4 step is a true 0.4 step, not a slicer rounding. 0.1 mm also divides the grid; 0.12 and 0.16 do not. The reasoning dates from the prototype's holders and carries over unchanged ([design log entry 18](design-log.md#18-layer-quantised-holders)); what is new in v1 is that the whole design obeys it, not just the holders. The print order spec pins every file at 0.2 ([printing.md](printing.md)). The verifier enforces the grid and the minimum step on every export ([§11](#11-working-with-the-source)).

---

## 3. Optical decisions

**One opal sheet, recessed into the cover-stage, is the final diffuser.** The acrylic (a bought part, 68 × 118 × 2) drops into a 69 × 119 recess 2.4 deep: 0.5 mm of side clearance, top face 0.4 below the deck. Because the holder stands on the deck, **nothing ever touches the acrylic**: it is an optical layer, not a structural one, and the film plane is referenced through printed plastic, never through it. To lift it out, take the holder off and push the sheet up through the light window from inside the box.

**Dust on the acrylic does not image.** The acrylic is itself the diffuse emitting surface: a particle sitting on it is part of the source, not an object between the source and the lens, so it cannot project an outline onto the film. Wipe the sheet periodically and move on; no per-session ritual. (Dust on the optional glass is the opposite case; see [§5](#5-film-holders).)

**Mixing margins.** The window-to-wall margins, 29 in x and 27.5 in y, are the numbers that decide how well the cavity fills the window evenly. They are design margins, chosen generous, with no established minimum and no measurement behind them.

**All-white cavity, matte only.** The white PLA *is* the mixing surface. Do not paint the inside, and do not print the white parts in silk or glossy filament: a specular wall reproduces the flash head as a hot spot instead of scattering it.

**Everything above the acrylic is black.** The holders, inserts and mask print in black so stray light above the diffuser is absorbed, not bounced back into the film. An optional A5 black flocking sticker on the deck kills the last of the glare ([bom.md](bom.md)).

**Ambient light is tolerated, not sealed out.** The open front admits room light; the design answer is operational (dim room, no lamp aimed into the opening, camera at sync speed), because the pulse dwarfs what remains ([§8](#8-flash-operation)).

**No internal adjusters.** No reflector plates, no baffles, no levelling hardware anywhere in the light path: the cavity is bare white walls and nothing else. Every internal part would be one more thing to align and one more thing to knock out of place. Verify evenness with a [flat-field-corrected](glossary.md#flat-field-correction) test frame, which separates lens vignetting from real source unevenness ([assembly.md](assembly.md)).

---

## 4. Cover-stage

The cover-stage is the prototype's top cover and film stage merged into a single white plate: one printed part where there used to be a cover, a stage, three studs, six nuts and three heat-set inserts. It seats directly on the wall tops and carries everything optical above the cavity.

What the one part carries:

- **The plate**: 124.8 × 154.8, 10 overall, a 6 mm structural plate whose deck face lands at z = 79.0. Four corner notches, 2.8 deep, drop over the main body's 2.6 tenons with 0.2 of vertical clearance. The plate seats on the wall tops, never on the tenons; the tenons only pin it in XY.
- **The light window**: 62 × 95, centred, straight through the plate.
- **The acrylic recess**: 69 × 119, 2.4 deep, floor at 76.6, open to the deck. The opal sheet drops in from above and sits 0.4 below the deck ([§3](#3-optical-decisions)).
- **The tray**: a flange rim around a 94.6 × 120.6 seat, 4 high, top at 83.0. It locates the holder with 0.3 mm per side and its top face catches the film tail 0.2 below the film plane ([§5](#5-film-holders)).
- **The washer pockets**: four, 10.6 square and 1.0 deep, at (±41, ±12). A 10 × 10 × 1 steel washer (or a Ø10 × 1 disc) drops into each, flush with the deck: ferrous seats for the holder-base magnets, so the holder snaps down onto the tray and stays put. It is the same job the prototype's glued washers did, now without glue.

To move it, pinch the flange and lift; the whole cover-stage comes off the box in one piece.

**There is no levelling hardware, and that is the design, not an omission.** The prototype levelled its film stage against the box on three M6 studs; v1 deletes the studs, the nuts, the inserts and the procedure.

<details>
<summary>Why levelling moved to the camera end</summary>

Plastic never carries a thread in this design. FDM-printed threads are weak and creep under load; the prototype already avoided them with brass inserts and steel studs, and v1 removes the need for even those.

The deeper reason: the only parallelism that matters is **film plane to sensor**, and levelling the stage against the box never delivered that directly; after the prototype's three-nut ritual you still had to square the camera to the stage. v1 keeps only the step that matters. Lay a small mirror on the film stage, look through the viewfinder, and move the camera until the reflection of its own lens is centred: when it is, the sensor is parallel to the mirror, and therefore to the film plane the mirror is lying on ([assembly.md](assembly.md#step-7--level-at-the-camera-the-mirror-method)).

Because the mirror lies on the *result* of the whole printed stack (floor, walls, plate, holder), every print tolerance underneath it is absorbed in that single alignment. The box does not need to be flat to a target; the camera meets the film plane wherever it actually is.

</details>

---

## 5. Film holders

One holder set per format: a base and a lid, both 94 × 120, standing in the cover-stage tray. Changing format means lifting one set off and dropping the other in: the magnets release and re-seat in about five seconds, and nothing else moves. The film is advanced by pulling the strip through the closed holder; it is never opened mid-roll. A fourth set, for mounted 135 slides, is a single plate with no lid ([below](#mounted-slides-the-slide-plate)).

| Feature | 135 holder | 120 holder |
|---|---|---|
| Outline, base and lid | 94 × 120 | 94 × 120 |
| Base / lid thickness | 5 / 3 | 5 / 3 |
| [Window](glossary.md#window) (base, lid and insert) | 25 × 37 | 57 × 85 (covers 6×9) |
| Film guide width | 35.4 between the inner rails | 62.0 between the channel walls |
| Element ledge ([§ below](#the-flattening-system)) | 4.6 high, at x 31 – 32.2 | identical |
| Magnets Ø8 × 2 | 8 in the base + 8 in the lid | same |

**Windows are deliberately about 0.5 mm oversize per side** against the nominal frame (135 is nominally 24 × 36, 120 is nominally 56 × 84) to absorb camera-gate variance between bodies and printer XY tolerance. You crop to the frame in post; see [scanning.md](scanning.md#loading-film).

### The flattening system

The film plane is the top of the [land](glossary.md#land), a ledge framing the window **on all four sides**, at 4.2 above the base bottom. Film is 0.12 – 0.18 thick, so its top face lies at 4.32 – 4.38. The next 0.2-grid station above that is **4.6**, and 4.6 is exactly where the element ledge places the underside of whatever rests on it. Those three numbers are the whole system:

**land 4.2 → film top 4.32 – 4.38 → element underside 4.6.**

That makes a 0.4 mm channel over the land on all four sides of the window, and 0.22 – 0.28 mm of free lift for the film anywhere under the element. The element is whatever 64 × 95 × 2 plate you set on the ledge; that is what makes the system interchangeable:

- **Default: the printed pressure-window insert**, one per format. A hard ceiling all round the window perimeter holds lift to ≤ 0.28 there; over the open window the film is unconstrained, but at 1:1 and f/8 the depth of field is about ±0.4 mm, which covers the residual bow.
- **Upgrade: one anti-Newton glass, 64 × 95 × 2, shared by both formats.** A continuous ceiling over the full frame: ≤ 0.28 mm at any position. Its matte (AN) face goes down, against the glossy film base, so no [Newton rings](glossary.md#newton-rings) form; the emulsion faces the open window below and touches nothing.

**Why a single glass completes the sandwich:** a classical glass carrier needs two glasses because nothing else defines the bottom of the stack. Here the bottom is printed (the land frame supports the film on all four sides at 4.2), so one glass on top closes the sandwich, with half the glass surfaces to keep clean and no glass at all under the emulsion.

**Why one glass fits both formats:** both bases carry an identical outer-rail profile: the element ledge at x 31 – 32.2, 4.6 high, and an outer step at 32.2 – 33.5, 5.0 high, which locates the element sideways. The same 64 × 95 seat therefore exists in both. In the 135 base, the inner guide rails at ±17.7 – 19.7 that steer the narrow strip would foul a 64-wide plate, so their middle is omitted over |y| < 48, leaving 12 mm guide stubs at each end: the glass drops through the gap onto the ledge, and the stubs bracket it lengthwise.

The element is seated once and then never handled. Advancing film means gripping the leader where it protrudes from the holder and pulling; a bowed section is ironed flat as it slides under the element. The lid's cavity (64.8 × 96, ceiling at 7.0) captures the element with 0.4 of float: the lid locates it but never presses on it, so the element's height remains the ledge's printed 4.6, not a force fit. Loading advice: **glass mode, bow up** (the glass flattens it); **insert mode, bow down**. Film that leaves the holder drapes onto the tray flange, whose top sits 0.2 below the film plane: a support, not a pinch. Hand-support the tail of a long strip.

> [!CAUTION]
> **The glass underside sits 0.2 mm from the focal plane, so dust on it lands essentially in focus.** Blow both faces of the glass before seating it; it is the one surface in the box where dust images. The acrylic, by contrast, is self-forgiving ([§3](#3-optical-decisions)).

**Magnets.** Ø8 × 2 N35, press-fitted (no glue anywhere), 8 per part, 32 across both sets. The base magnets stand 0.4 proud of the plate face; the lid magnets sit flush with the lid underside; closed, the faces are 0.8 apart and **never touch**, so the lid always seats on the printed rail tops and the channel height stays a printed number, not a magnet stack-up. Polarity must be paired so that every base–lid position attracts: check each magnet against its mate before pressing it home; a press-fitted magnet does not come back out.

**6×6 and 6×4.5.** For 6×6, lay `mask-6x6.stl` (94 × 80 × 1, window 56.5 × 56.5) in the tray *under* the 120 base: the whole set rides 1 mm higher, which is normal; refocus and carry on. 6×4.5 has no dedicated mask; crop in post.

### Mounted slides: the slide plate

A slide in its mount is about 1.2 – 3.2 mm thick, many times the 0.4 mm channel, so it can never enter the 135 holder; and cutting a pocket for it into the 135 base would remove the land that supports the strip ([design log entry 25](design-log.md#25-mounted-slides-a-plate-of-their-own)). Instead `slide-plate-135.stl` is a fourth holder set in one piece: a 94 × 120 × 5 black plate that stands in the tray in place of the 135 set. It has no lid, no magnets and no pressure element: a mount is rigid and the box is horizontal, so the pocket locates the mount and gravity holds it.

| Feature | Slide plate |
|---|---|
| Outline and thickness | 94 × 120 × 5, the same seat in the tray as a holder base |
| Pocket | 51.4 × 51.4, 2.0 deep; floor at 3.0 above the plate bottom (z = 82.0) |
| Window | 26 × 38, through the pocket floor |
| Finger wells | two, 18 × 12, centred on the pocket's short sides; floor at 1.0, blind |
| Film plane | pocket floor plus about half the mount's thickness: roughly 82.6 (card mounts) to 83.6 (glass mounts); refocus |

**Why 51.4:** mounts are nominally 50 × 50, but card mounts run up to 50.8 (2 inch), so 51.4 leaves 0.3 mm per side on the largest mount and 0.7 on a plastic one: the same clearance the holder bases have in the tray. **Why 2.0 deep:** the thinnest card mount, about 1.2, is still captured by the pocket walls, and the thickest glass mount, about 3.2, stands 1.2 proud, where nothing sits above it to object. **Why 26 × 38, not 25 × 37:** the mount can float up to 0.7 mm in the pocket, and with 1 mm of margin per side against the nominal 24 × 36 frame it is always the mount's own aperture, never the printed edge, that frames the image; every mount still overlaps the window by more than 5 mm on every side, so nothing leaks. **The finger wells** let a fingernail under the edge of a card mount that sits 0.8 below the pocket rim; they are blind, 2.0 below the pocket floor, so they pass no light.

A mount is loaded the way you would hold it up to a window: image reading correctly from above, which puts the emulsion down, the same rule as for strips. A warped card mount or a popped frame is not flattened by anything here, exactly as in a dedicated slide scanner; at 1:1 and f/8 the roughly ±0.4 mm depth of field absorbs most of it.

---

## 6. Enclosure

**Main body** is one printed piece: a 3.0 floor, three 2.4 walls (left, right, rear), and no front wall at all. Four locating tenons, 2.4 × 12 × 2.6, stand on the side-wall tops and engage the cover-stage's corner notches.

**What the open front deleted.** The prototype needed an access panel because the flash's power dial lived inside a sealed box, a cable gland because wires had to cross a light-tight wall, and a ventilation answer because heat had nowhere to go. In v1 there is nothing inside to reach: flash, receiver and their batteries all sit on the desk, a power change is a fingertip away, the focus light's cable simply walks out through the opening, and the cavity is open air. All three problems left with the front wall.

**No screws, no glue, no tools.** No thread engages plastic anywhere in the design. Every joint is a tenon in a notch, gravity, or a magnet: the cover-stage locates on tenons and holds by weight, the holder holds by magnets on washers, the lid by magnets on the base, the element by gravity in its ledge. The magnets press-fit; the washers drop in loose. Assembly is stacking, in order, and is over in minutes ([assembly.md](assembly.md)).

> [!NOTE]
> **The fastener inventory of the entire build is: zero screws, zero adhesive.** Even the prototype's two glue points (holder magnets and steel washers) are gone: v1's magnets are interference-fitted and its washers sit in pockets.

> [!WARNING]
> **A gravity stack must not be carried tilted.** Assembled, the box is aligned, not attached: move it flat across the desk, or move the pieces separately; the cover-stage lifts off by its flange in one motion.

### Feature location schedule

XY from the centre of the box; z from the desk. Read from `cad/neobox.blend`.

| Feature | XY | z | Size |
|---|---|---|---|
| Open front | front face | 3.0 – 73.0 | full cavity cross-section, 120 × 70 |
| Locating tenons, 4 | side-wall tops | 73.0 – 75.6 | 2.4 × 12 × 2.6 |
| Corner notches, 4 | cover-stage underside | 2.8 deep | 0.2 vertical clearance over the tenons |
| Light window | centred | through the plate, 73.0 – 79.0 | 62 × 95 |
| Acrylic recess | centred | floor 76.6, open to the deck at 79.0 | 69 × 119, 2.4 deep |
| Washer pockets, 4 | (±41, ±12) | 78.0 – 79.0 | 10.6 square, 1.0 deep |
| Tray flange | around the 94.6 × 120.6 seat | 79.0 – 83.0 | rim, 4 high |

> [!TIP]
> The tenon-and-notch fit is sized inside normal FDM error: elephant foot, XY expansion and warp all eat into it. If the cover-stage binds or rattles, the remedy is a slicer setting, not a file edit; see [printing.md](printing.md#if-it-came-out-tight-or-loose).

---

## 7. Focus light

There is no built-in focus light, and nothing electrical lives inside the enclosure. Frame and focus with ordinary room light: a dim room shows plenty of film detail, any lamp works as long as it does not shine straight into the open front, and at capture the flash overwhelms whatever the room contributes.

---

## 8. Flash operation

Manual power only, normal sync, shoot [raw](glossary.md#raw). [TTL](glossary.md#ttl) metering is useless here (the scene never changes, so power is set once, manually), and [HSS](glossary.md#hss) solves a problem that does not exist at or below [sync speed](glossary.md#sync-speed). Do not pay for either.

**The pulse is the exposure.** Even with the open front, in a dim room the ambient light a sync-speed exposure collects is negligible next to the pulse, so the flash's own duration acts as the effective shutter, orders of magnitude shorter than any tripod-safe continuous-light exposure. Vibration, shutter shock and floor rumble stop mattering.

**Shutter speed: 1/125 s is the recommendation.** Focal-plane shutters typically sync at 1/160 – 1/250, and a cheap 2.4 GHz trigger's latency costs about one stop of that; hence 1/125. The symptom of pushing past the real limit is unmistakable: a clean-edged dark band across the frame.

> [!IMPORTANT]
> **An electronic shutter will usually not fire a flash at all.** If nothing happens when you press the button, that is the first thing to check. Details in [scanning.md](scanning.md#exposure).

Power changes are a fingertip away: the flash is on the desk in front of you, nothing to open, nothing to disturb. The receiver sits beside it, outside the box, where its radio path is clean and a battery swap touches nothing. In practice power is set once, from a test frame, and left alone; exposure procedure is in [scanning.md](scanning.md#exposure).

---

## 9. Repositioning and repeatability

The film plane is fixed at z = 83.2 for **both** strip formats (the 6×6 mask lifts the 120 set by 1 mm; the slide plate and the sheet plate put their film within a millimetre of it; refocus, nothing else changes). What changes between 135 and 120 is the magnification you need, and therefore the camera height, not the height of the film. Work the camera height out from the film plane plus your lens's [working distance](glossary.md#working-distance); the arithmetic is in [scanning.md](scanning.md#camera-height-and-the-stand).

**Parallelism is one alignment: the mirror method.** Lay a small mirror on the film stage and centre the reflection of your own lens in the viewfinder: the sensor is then parallel to the film plane, and every print tolerance in the stack below has been absorbed in the same move ([assembly.md](assembly.md#step-7--level-at-the-camera-the-mirror-method), and the reasoning in [§4](#4-cover-stage)). This is why the box carries no levelling hardware at all.

Once the camera is set, the box is what moves: slide it on the desk to centre the frame rather than re-aiming the camera; the flash just gets nudged back against the opening. When you are satisfied, make the position repeatable (two locating pins on the baseboard or a pencil outline of the footprint, either works) and write down the column height you used for each format.

**Parallelism first, evenness second.** A flash freezes vibration; it cannot fix a film plane that is not parallel to the sensor. Mirror method first, then a [flat-field-corrected](glossary.md#flat-field-correction) test frame to check evenness.

---

## 10. 4×5 on the v1 body

4×5 rides on the unchanged main body with two optional parts and one larger acrylic: `cover-stage-4x5.stl` replaces the cover-stage, `sheet-plate-4x5.stl` stands in its tray, and a 106 × 130 × 2 opal sheet lies in its recess. Nothing else changes: the same tenons, the same flash at the same open front, the same gravity stack, the same 160 × 160 bed.

| Feature | 4×5 cover-stage | v1 cover-stage |
|---|---|---|
| Outline, plate, notches | 124.8 × 154.8, 6 mm plate, four notches over the tenons | identical |
| Light window | 102 × 126 | 62 × 95 |
| Acrylic recess | 107 × 131, floor at 3.6, for a 106 × 130 × 2 sheet | 69 × 119, for 68 × 118 × 2 |
| Tray inside the flange | 112.6 × 138.6, flange 4 wide, top at 10.0 | 94.6 × 120.6, flange 7 wide |
| Washer pockets | none: the sheet plate has no magnets | four |
| Mixing margin, window edge to wall | 9 in x, 12 in y | 29 in x, 27.5 in y |

| Feature | Sheet plate |
|---|---|
| Outline and thickness | 112 × 138 × 5, standing on the deck inside the 4×5 flange |
| Pocket | 102.2 × 127.6, 2.0 deep; floor at 3.0 above the plate bottom (z = 82.0) |
| Window | 97 × 121, through the pocket floor: the 96 × 120 image area plus the usual 0.5 per side |
| Edge notches | two, 18 wide, on the short sides, running from 3.7 under the sheet edge out through the plate edge; floor at 1.0 |
| Film plane | the sheet lies on the pocket floor: about 82.2 |

**Why the sheet needs no pressure element.** 4×5 on full frame is about 0.25×, and at f/8 the depth of field is then roughly 8 – 10 mm, ten times the 135 case. A sheet's own curl, a millimetre or two, is invisible at that scale, so the plate is a pocket with a land under the sheet edges and nothing on top: no lid, no glass, no magnets. Sheets load one at a time, image reading correctly from above (emulsion down), and lift out by the edge notches.

**What is not known: evenness.** The v1 window sits 29 and 27.5 mm from the walls; the 4×5 window sits 9 and 12. No minimum margin has ever been established and nothing has been measured, so the 4×5 stage is published as an experiment on the same body, not as a figure. Shoot one blank frame first: if it shows a gradient you will not accept, flat-field correction in post is the first remedy ([scanning.md](scanning.md#flat-field-and-inversion)) and a bigger box the second.

<details>
<summary>The bigger-box route, if the margins prove too small</summary>

Derive a bigger box, not a different kind of box: keep the 102 × 126 window and give it v1's margins, which makes the cavity 160 × 181 inside and the main body about 164.8 × 185.8 outside, past a 160 × 160 bed and onto a 220-class one, with the cover-stage, tray, sheet plate and acrylic scaled to match. The open-front architecture, the screwless gravity stack and the layer grid carry over unchanged. The flash may not need to grow: the larger window costs about 1.2 stops, and the drop from 1:1 to 0.25× gives back about 1.3, though that too is unmeasured.
</details>

---

## 11. Working with the source

`cad/neobox.blend` is the only source of geometry in this repository. The twelve STL files are generated from it, and a change that reaches the STLs without going through the blend file is lost the next time anyone re-exports.

### Opening the file

| Property | Value |
|---|---|
| Blender version | **3.0 or newer.** The file is Zstandard-compressed, which pre-3.0 Blender cannot read at all. The file header records **Blender 5.2** as the version it was last saved with |
| Unit system | Metric, unit scale 0.001, length unit millimetres: **one Blender unit is one millimetre** |
| Scene layout | The assembly is modelled in place, on the same z datum this document uses: the desk (the outer bottom of the box) is z = 0. The 120 holder set is parked beside the assembly at x = 200, the 6×6 mask at x = 350, the slide plate at x = 500 and the 4×5 stage at x = 650 |

### The collection tree

```
Scene Collection
├── mock_view-target        an empty, used as a view target
├── Scaffolding             Camera, Light: render scaffolding
├── NeoBox_v1               the enclosure, the cover-stage and the mock-ups
├── Holder_135              the 135 holder set, assembled in place
├── Holder_120              the 120 holder set, parked at x = 200
├── Masks                   the 6×6 mask, parked at x = 350
├── Holder_slide            the slide plate and its mount mock-up, parked at x = 500
└── Stage_4x5               the 4×5 cover-stage and sheet plate with their mock-ups, parked at x = 650
```

### Which objects make each STL

| STL file | Blender object(s) | Gloss |
|---|---|---|
| `main-body.stl` | `main-body_floor`, `main-body_wall-left`, `main-body_wall-right`, `main-body_wall-rear` | **four objects**: floor, left wall, right wall, rear wall; the open front needs no lintel or posts |
| `cover-stage.stl` | `cover-stage` | cover-stage, one piece, window 62 × 95 |
| `film-holder-135-base.stl` | `film-holder-135-base` | 135 holder base, flat-bottomed |
| `film-holder-135-lid.stl` | `film-holder-135-lid` | 135 holder lid |
| `film-holder-120-base.stl` | `film-holder-120-base` | 120 holder base, flat-bottomed |
| `film-holder-120-lid.stl` | `film-holder-120-lid` | 120 holder lid |
| `pressure-window-135.stl` | `pressure-window-135` | pressure-window insert, 135 |
| `pressure-window-120.stl` | `pressure-window-120` | pressure-window insert, 120 |
| `mask-6x6.stl` | `mask-6x6` | 6×6 mask |
| `slide-plate-135.stl` | `slide-plate-135` | slide plate, one piece |
| `cover-stage-4x5.stl` | `cover-stage-4x5` | 4×5 cover-stage, one piece |
| `sheet-plate-4x5.stl` | `sheet-plate-4x5` | 4×5 sheet plate, one piece |

### What is a mock-up and must never be exported

**The name says whether an object is printed.** A printed part carries the name of the STL file it becomes: `cover-stage` is the object that becomes `cover-stage.stl`, and the main body is the four shells sharing the `main-body_` prefix. Everything else in the scene is a mock-up, there to show fit and light path, and takes the `mock_` prefix instead; none of it is printed or exported: the flash body and its emitting face (`mock_flash-body`, `mock_flash-face`), the T1 receiver (`mock_trigger-receiver`), the four light-path arrows (`mock_ray-1-into-cavity` to `mock_ray-4-through-window`), the 135 and 120 film-strip mock-ups (`mock_film-135`, `mock_film-120`), a 50 × 50 × 2 slide mount (`mock_slide-mount-50x50x2`), a 4×5 sheet (`mock_film-4x5`), the two opal acrylics (`mock_diffuser-68x118x2`, `mock_diffuser-106x130x2`), the AN glass (`mock_an-glass-64x95x2`), the four steel washers (`mock_steel-shim-1` to `mock_steel-shim-4`), a text label (`mock_label`), and the view target (`mock_view-target`). `Camera` and `Light` carry no prefix and need none: neither is a mesh, so neither can reach an STL.

The convention is a gate, not a habit. `tools/export_stl.py` fails the whole export when it finds a mesh object that is neither listed in its `MAPPING` table, reproduced above, nor prefixed `mock_`. A printed part added to the scene and forgotten in that table therefore stops the export instead of quietly dropping out of the release.

> [!CAUTION]
> **Material names do not tell you the filament colour.** The eight materials (`NB_white`, `NB_black`, `NB_steel`, `NB_opal`, `NB_film`, `NB_glow`, `NB_ray`, `NB_receiver`) exist for the renders, and each is named for what it is applied to rather than for anything you load into the printer: `NB_black`, for one, covers every black printed part and three mock-ups, the flash body, the label and the slide mount. The prototype-era materials have been deleted, so nothing misleading survives in the list, but colours still come from [printing.md](printing.md#the-twelve-parts), never from the material slot.

### The export convention

Every STL is exported **in assembly world space**: nothing is re-zeroed or re-oriented on the way out.

| File | Where it sits inside the exported file |
|---|---|
| `main-body.stl` | z 0 – 75.6, centred on XY |
| `cover-stage.stl` | z 73 – 83, centred on XY |
| `film-holder-135-base.stl` / `-lid.stl` | z 79 – 84 / 84 – 87, in place on the assembly |
| `pressure-window-135.stl` | z 83.6 – 85.6, in place |
| `film-holder-120-base.stl` / `-lid.stl` | parked at x 153 – 247, z 0 – 5 / 5 – 8 |
| `pressure-window-120.stl` | parked at x 168 – 232, z 4.6 – 6.6 |
| `mask-6x6.stl` | parked at x 303 – 397, z 0 – 1 |
| `slide-plate-135.stl` | parked at x 453 – 547, z 0 – 5 |
| `cover-stage-4x5.stl` | parked at x 587.6 – 712.4, z 0 – 10 |
| `sheet-plate-4x5.stl` | parked at x 594 – 706, z 6 – 11, standing on the 4×5 cover-stage's deck |

A slicer drops each file onto the build plate by its bounding box. Ten of the twelve files arrive lying on their print face already; the two holder lids do not: they print **top face down** and have to be flipped after import. The required rotation is on each part card in [printing.md](printing.md#the-twelve-parts).

### Re-exporting

One command regenerates all twelve files. It is the committed form of the pipeline that produced the published STLs, and it is the only supported way to export:

```
blender --background cad/neobox.blend --python tools/export_stl.py
```

(`blender` is the binary inside your Blender installation; any 4.x/5.x build works. Run it from the repository root, then `python3 tools/verify_stl.py`.)

The script matters because the printable parts are **modelled as overlapping shells**, interpenetrating by 0.2 – 0.5 mm on purpose: the walls sink into the floor, the flange into the cover-stage plate, the rails into the holder bases. That keeps the source parametric and easy to edit. For every output file the script copies the source objects, splits them into shells, boolean-unions the shells into one solid (EXACT solver), welds away the boolean slivers, checks the result is watertight, and exports it in assembly world space; the scene itself is never touched. A naive File → Export → STL of the raw objects produces multi-shell files whose internal faces fail the verifier's layer-grid check.

Regenerated files may differ from the published ones **byte for byte** (triangulation is not stable across Blender versions) while being geometrically identical. The verifier is the referee: bounding box, watertightness, layer grid and minimum step must all pass.

<details>
<summary>Manual export, if you cannot run the script</summary>

1. **Select the objects** for one output file, using the mapping table above. *Checkpoint:* the number of selected objects matches the table: four for the main body, one for everything else.
2. **Make it one solid: every part, not just the main body.** Single-object parts can still be multi-shell inside. Join what needs joining, separate by loose parts, boolean-union the shells, then merge vertices by distance (0.02 mm) and run a limited dissolve (1°) to remove the boolean slivers. *Checkpoint:* the part is one connected shell and the verify script reports no non-manifold edges.
3. **Export.** File → Export → STL, with *Selection Only*, scale 1.00, forward Y, up Z. No axis conversion: the numbers in the file must be the numbers in Blender. *Checkpoint:* re-importing the file puts the part back exactly where it was.
4. **Write it to the same path** under `stl/white-pla/` or `stl/black-pla/`, keeping the filename. *Checkpoint:* `git status` shows a modified file, not a new one.
5. **Verify** before you commit anything. *Checkpoint:* `python3 tools/verify_stl.py` prints `all 12 files pass` and exits 0.

</details>

```mermaid
flowchart LR
  A[Edit cad/neobox.blend] --> B[Export the affected STLs]
  B --> C[python3 tools/verify_stl.py]
  C -->|all 12 files pass| D[Update the docs in all three languages]
  C -->|any FAIL| A
  D --> E[Commit blend, STLs and docs together]
```

### Running the verifier

`tools/verify_stl.py` is plain Python 3 with no dependencies. Run it from the repository root:

```
python3 tools/verify_stl.py
```

It walks every `.stl` under `stl/` and checks four invariants per file:

| Check | What it enforces |
|---|---|
| watertight | Every edge is shared by exactly two triangles: a closed solid, no holes |
| layer grid | Every horizontal face sits on a 0.2 mm multiple above that part's own base |
| minimum step | No exposed horizontal step below 0.4 mm, which is two layers at 0.2 |
| bounding box | The part still measures what the documentation says it measures |

Horizontal faces smaller than 1 mm² are ignored when hunting for steps, so modelling slivers do not raise false alarms. Output is one line per file plus a total, and the exit status is non-zero if anything fails, so the script can gate a commit:

```
ok    film-holder-120-base.stl  [94.0, 120.0, 5.0]  256 triangles
...
all 12 files pass
```

The published bounding boxes live in the `EXPECTED` table at the top of the script, sorted largest first. **If you change a published dimension on purpose, edit `EXPECTED` in the same commit**; otherwise the check fails on the part you meant to change and quietly passes on the part you did not.

### Changing the flash

In the prototype era this heading introduced a re-derivation checklist. In v1 there is nothing to change: **no dimension of the box encodes the flash**, so a different flash (or a different trigger) touches neither `cad/neobox.blend` nor the STLs. The new flash needs manual power control and a head that can lie flat and fire level into the open front; after swapping, redo the metering test frame and carry on ([§8](#8-flash-operation)).

### Other files in `cad/`

- `film-stage-aluminium-3mm.dxf`: the prototype's aluminium film stage, kept for history only. v1 has no film stage: the part was merged into the cover-stage, and nothing in the current design is cut from this file.
- `legacy-plywood/`: DXFs from the plywood revision, kept for history only. Between them the two files do not describe a complete shell, and nothing in the current design is cut from them.

Contribution rules (what is source, what is generated, and the three-language requirement) are in [CONTRIBUTING.md](../CONTRIBUTING.md#source-of-truth-vs-generated-files).

---

← [Glossary](glossary.md) · [Documentation index](../README.md#documentation) · [Design log](design-log.md) →
