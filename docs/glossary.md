# Glossary

**English** · [简体中文](glossary.zh-CN.md) · [日本語](glossary.ja.md)

> One line for every term the NeoBox documents use as if you already knew it, and one line on why it matters in this project. Other pages link straight to the entry they need.

**Contents:** [Anti-Newton glass](#anti-newton-glass) · [Base ISO](#base-iso) · [Bed size](#bed-size) · [Bridging](#bridging) · [Camera scanning](#camera-scanning) · [Channel](#channel) · [Copy stand](#copy-stand) · [Cover-stage](#cover-stage) · [Diffuser](#diffuser) · [EFCS](#efcs) · [Element ledge](#element-ledge) · [Elephant foot](#elephant-foot) · [EV](#ev) · [Film gate](#film-gate) · [Flat-field correction](#flat-field-correction) · [Guide number](#guide-number) · [HSS](#hss) · [Infill](#infill) · [Integrating cavity](#integrating-cavity) · [Inversion](#inversion) · [Land](#land) · [Layer height](#layer-height) · [Locating tenon and notch](#locating-tenon-and-notch) · [Magnification ratio](#magnification-ratio) · [Manual power fraction](#manual-power-fraction) · [Mirror alignment](#mirror-alignment) · [Newton rings](#newton-rings) · [Opal](#opal) · [Open front](#open-front) · [Perimeters](#perimeters) · [Pressure window insert](#pressure-window-insert) · [Rail](#rail) · [Raw](#raw) · [Run-out corridor](#run-out-corridor) · [Supports](#supports) · [Sync speed](#sync-speed) · [TTL](#ttl) · [Window](#window) · [Working distance](#working-distance)

## A–Z

Two vocabularies meet in this project — film photography and 3D printing — and a reader is rarely fluent in both. Every entry below is written for someone fluent in neither.

> [!TIP]
> Part names are a separate matter. Every part is named once and never renamed. Printed: **main body**, **cover-stage**, **film holder** (**holder base** / **holder lid**, one pair per format), **pressure window inserts**, **6×6 mask**. Bought: **diffuser**, **magnets**, **steel shims**, and optionally **anti-Newton glass**. The v4 **top cover** and **film stage** are merged into the cover-stage since v5, and the **access panel**, **studs** and **nuts** are gone — v5 has no fasteners at all. If you cannot match a name to a shape in front of you, see [Part vocabulary](printing.md#part-vocabulary), which ties each one to a feature you can see.

### Anti-Newton glass

Glass with one finely matted face, made so that film pressed against it cannot form [Newton rings](#newton-rings). NeoBox's optional flatness upgrade is one 64 × 95 × 2 mm single-side AN sheet, shared by both formats.

**Why it matters:** dropped onto the [element ledge](#element-ledge) in place of the printed [pressure window insert](#pressure-window-insert), it caps the whole frame continuously and holds every point of the film within 0.28 mm of flat. Matte face down, against the glossy base side of the film; the emulsion side faces the open window below and touches nothing. Its underside sits only 0.2 mm from the focal plane, so dust on it lands in the picture — blow it clean before loading.

### Base ISO

The lowest true sensitivity of a camera's sensor — usually ISO 100 — where it has the most dynamic range and the least noise.

**Why it matters:** the flash has power to spare inside the box, so there is no reason ever to leave base ISO. Metering starts at ISO 100 and f/5.6–f/8. See [Exposure](scanning.md#exposure).

### Bed size

The printable area of an FDM printer's build plate, quoted as X × Y.

**Why it matters:** it is a go/no-go, not a preference — but in v5 an easy one. The largest parts, the main body and the cover-stage, are 124.8 × 154.8 mm, so a 160 × 160 mm bed prints everything; the old v4 warnings about 280 mm beds are obsolete. See [Will it fit your printer?](printing.md#will-it-fit-your-printer).

### Bridging

Extruding filament straight across an unsupported gap between two anchored points, so it spans in air and cools before it can droop.

**Why it matters:** v5 has nothing to bridge. The front of the main body is not a spanned opening but a missing wall — the [open front](#open-front) — and every one of the nine parts prints flat face down without [supports](#supports).

### Camera scanning

Photographing a negative with a digital camera on a stand, instead of feeding it through a flatbed or drum scanner. Also called DSLR scanning, whatever camera you use.

**Why it matters:** NeoBox is the light source for this method and nothing else. It does not hold a camera, and the camera, lens and stand are yours to provide. See [What camera scanning is](getting-started.md#what-camera-scanning-is).

### Channel

The 0.4 mm high slot the film strip slides along inside the film holder — 35.4 mm wide in the 135 holder, 62.0 mm in the 120 holder. Its floor is the [lands](#land), its sides are the [rails](#rail), and its ceiling is the underside of the pressure element — the [pressure window insert](#pressure-window-insert) or the [anti-Newton glass](#anti-newton-glass) — sitting on its [ledge](#element-ledge).

**Why it matters:** film is loaded and advanced by pulling the strip sideways through the channel; the holder is never opened and the pressure element never moves mid-roll. A bowed frame is pressed flat against the ceiling as it slides in. The 0.4 mm figure is also why the holder parts are the ones worth printing at the finer [layer height](#layer-height).

### Copy stand

A vertical column on a baseboard that holds a camera pointing straight down at an adjustable height. A tripod with a horizontal or reversible centre column does the same job.

**Why it matters:** the film plane sits 83.2 mm above the desk, and the stand must clear that plus the [working distance](#working-distance) of your lens while holding the sensor parallel to the film. See [Camera height and the stand](scanning.md#camera-height-and-the-stand).

### Cover-stage

The single white part that closes the top of the box — the v4 top cover and film stage merged into one 124.8 × 154.8 × 10 mm piece. Its 6 mm plate rests on the box walls, located by four notches over the body's [tenons](#locating-tenon-and-notch); a raised flange rings the 94.6 × 120.6 mm holder seat, and the plate carries the 62 × 95 mm light window, a hidden slot for the [diffuser](#diffuser) and four flush steel shims for the holder's magnets to grab.

**Why it matters:** merging cover and stage removed a whole stack of parts and the tolerances between them — nothing to level, nothing to bolt. The whole piece lifts off by its flange, holders snap on and off it magnetically in seconds, and the flange top runs 0.2 mm below the film plane, so film running out of the holder rides over it instead of jamming against it.

### Diffuser

A translucent sheet that scatters light passing through it into an even glow. In NeoBox there is exactly one: an [opal](#opal) acrylic sheet, 68 × 118 × 2 mm, sitting in a shallow slot inside the [cover-stage](#cover-stage) beneath the light window.

**Why it matters:** it is the glowing surface itself — the last diffuse stage before 4.6 mm of air and the film. Because it emits diffusely, dust on it does not image: wipe it now and then rather than ritually. To take it out, lift the holder off and push the sheet up through the light window from inside the box.

### EFCS

Electronic first-curtain shutter: the exposure begins electronically at the sensor and ends with the mechanical rear curtain.

**Why it matters:** EFCS still fires a flash, and it removes the shock of the opening curtain. A *fully* electronic (silent) shutter is a different setting and usually will not fire a flash at all. See [Exposure](scanning.md#exposure).

### Element ledge

The 4.6 mm high step on the outer rails of each holder base that carries the pressure element — the [pressure window insert](#pressure-window-insert) or the [anti-Newton glass](#anti-newton-glass) — with an outer lip standing 0.4 mm higher to keep it from wandering. The ledge is identical in the 135 and 120 holders, which is why one sheet of glass serves both.

**Why it matters:** it fixes the element's underside at exactly 4.6 mm — 0.4 mm above the 4.2 mm [land](#land) the film rides on — and that difference *is* the film [channel](#channel). The element is set on the ledge once and never handled again; frames advance by pulling the strip underneath it.

### Elephant foot

The slight outward bulge of the first few layers of a print, squashed wider by the nozzle and the heated bed.

**Why it matters:** it lands on the fits with the least room — the notch mouths on the underside of the [cover-stage](#cover-stage) that drop over the body's [tenons](#locating-tenon-and-notch), and the footprint of the pressure window insert where it seats inside its [ledge](#element-ledge). Turn on your slicer's elephant-foot compensation. See [If it came out tight or loose](printing.md#if-it-came-out-tight-or-loose).

### EV

Exposure value. One EV is one stop: a doubling or halving of the light reaching the sensor.

**Why it matters:** it is the unit the evenness of the light and the consistency of exposure are judged in, corner to corner and frame to frame — always after [flat-field correction](#flat-field-correction).

### Film gate

The rectangular opening that defines the exposed area of a frame: the metal aperture in a film camera, and by extension the [window](#window) in the film holder that you photograph through here.

**Why it matters:** camera gates vary slightly between bodies, so the holder windows are cut about 0.5 mm oversize per side to swallow that variation and printer XY tolerance. It also names the surface you blow clean every session — along with the [anti-Newton glass](#anti-newton-glass), if you shoot with one.

### Flat-field correction

Photographing the evenly lit surface on its own, with no film in place, and then dividing your real frames by that reference so that lens vignetting and any unevenness in the light cancel out.

**Why it matters:** it comes first, before any judgement about the box. It is the only way to separate lens vignetting from real unevenness in the source, and the box's evenness is judged on what is left afterwards. See [Flat-field and inversion](scanning.md#flat-field-and-inversion).

### Guide number

A flash's power rating: guide number = aperture × distance for a correct exposure at ISO 100. The reference NEEWER TT560 is GN38, in metres.

**Why it matters:** it is the figure printed on the box, and inside NeoBox it tells you almost nothing, because the flash fires from the [open front](#open-front) and light reaches the film only after several diffuse bounces. Start metering at ISO 100 and f/5.6–f/8, and expect to give back several stops to the enclosure.

### HSS

High-speed sync: the flash fires a rapid train of small pulses so it can be used at shutter speeds above the camera's [sync speed](#sync-speed).

**Why it matters:** it is useless here, and you may be asked to pay for it. Working by flash in a dim room, you shoot at or below sync speed by choice.

### Infill

The internal lattice that fills the space between a part's [perimeters](#perimeters), given as a percentage of solid.

**Why it matters:** 15 % is the spec for all nine parts — nothing in v5 hangs a load on infill any more. What keeps the walls opaque is perimeters, not infill. See [Print settings](printing.md#print-settings).

### Integrating cavity

A closed volume with matte white walls in which light bounces many times until its direction and brightness even out. The laboratory version is the integrating sphere.

**Why it matters:** NeoBox is one — a 120 × 150 × 70 mm white cavity with one open side. The flash lies on the desk at the [open front](#open-front), firing horizontally into it, and nothing is aimed at the film: the evenness comes from the bounces off the white walls and ceiling, not from the diffuser alone. This is also why the interior is left as bare white filament and must not be painted. See [How the light works](../README.md#how-the-light-works).

### Inversion

Turning a captured negative into a positive image: inverting the tones, removing the orange mask of colour negative film, and setting contrast and colour.

**Why it matters:** it is the last step of the workflow, and it is where a constant light source pays off — every frame on the roll gets the same flash output, so one inversion profile fits the whole roll. See [Flat-field and inversion](scanning.md#flat-field-and-inversion).

### Land

The raised seat inside the holder base that the edges of the film rest on, standing 0.4 mm proud of the surrounding floor at a height of 4.2 mm.

**Why it matters:** the top face of the land *is* the film plane. Only the edges of the strip touch it — the image area floats over the open window, capped 0.4 mm overhead by the pressure element on its [ledge](#element-ledge).

### Layer height

The thickness of one printed layer. It quantises every horizontal feature in the part: a feature that is not a whole number of layers cannot be printed at its designed size.

**Why it matters:** every height in the design sits on a 0.2 mm grid, and every exposed step is 0.4 mm or more. The print spec is 0.2 mm on every part, so each height lands exactly on a layer boundary. See [Print settings](printing.md#print-settings).

### Locating tenon and notch

A tenon is a small raised block, a notch its matching recess. Four tenons, 2.4 × 12 × 2.6 mm, stand on the top edges of the main body's side walls and engage four notches in the underside of the [cover-stage](#cover-stage).

**Why it matters:** they are the only alignment feature in the box — v5 has no fasteners of any kind, so gravity holds the stack and the tenons stop it shifting, registering the light window over the cavity every time. It is also why the assembled box is lifted straight up and never carried tilted, and why [elephant foot](#elephant-foot) compensation matters at the notch mouths.

### Magnification ratio

How large the subject appears on the sensor, divided by its real size. 1:1 — written 1.0× — means the frame is projected onto the sensor at life size.

**Why it matters:** it decides which lens you need. A 135 frame on full frame needs 1.0×; a 6×6 frame on full frame needs 0.43×. Any 1:1 macro lens covers every format NeoBox handles, because the larger formats need *less* magnification. See [Magnification and lens choice](scanning.md#magnification-and-lens-choice).

### Manual power fraction

The flash's output set by hand as a fraction of full power — 1/1, 1/2, 1/4 and so on down to 1/128 — with each step exactly one stop.

**Why it matters:** manual power control is one of only two things that matter when choosing a flash for this box. The TT560 gives 8 full-stop steps, which is coarse, so fine exposure adjustment is done with the aperture in 1/3 stops instead.

### Mirror alignment

Squaring the camera to the film by eye: lay a small mirror flat at the film position, look through the viewfinder, and move the camera until the reflection of its own lens sits centred. A centred reflection means the sensor is parallel to the film plane.

**Why it matters:** it replaced every piece of levelling hardware in v4 — rods, nuts, all of it. Aligning at the camera also absorbs the printed box's tolerances, because you square up to the film plane that actually exists, not to the box that ought to be under it. See [Camera height and the stand](scanning.md#camera-height-and-the-stand).

### Newton rings

Irregular coloured interference fringes that appear where film is pressed against a smooth surface such as glass or acrylic.

**Why it matters:** the design gives them nothing to form on. With the printed [insert](#pressure-window-insert), nothing smooth touches the image area at all; with the glass upgrade, the face against the film is deliberately matted — that is the "anti-Newton" in [anti-Newton glass](#anti-newton-glass) — and the emulsion side faces an open window.

### Opal

Milky-white translucent acrylic that scatters light through its whole thickness, rather than at a textured surface.

**Why it matters:** opal is not the same product as frosted, which is clear sheet with a matte face, and ordering the wrong one is an easy mistake. NeoBox needs one 2 mm opal sheet cut to 68 × 118 mm — a v4 110 × 130 sheet can be cut down to it. See [Getting the right part](bom.md#getting-the-right-part).

### Open front

The main body has no front wall at all: the whole front of the box is open, and the flash lies flat on the desk outside with its head at the opening, firing horizontally into the cavity.

**Why it matters:** it decouples the box from any particular flash — any brand and size fits, the TT560 is only the reference — and the radio receiver stays outside, where its signal is clean and its batteries reachable without opening anything. Ambient light does get in: work in a dim room and keep ceiling light off the opening, and the flash pulse dwarfs whatever remains.

### Perimeters

The solid outlines the printer traces around the edge of every layer, also called walls or shells.

**Why it matters:** use at least 3 everywhere. The box walls are only 2.4 mm thick and their job is to be opaque — a wall that is mostly [infill](#infill) leaks light.

### Pressure window insert

A printed frame, 64 × 95 × 2 mm, with a film-gate window in it — 25 × 37 mm in the 135 version, 57 × 85 mm in the 120 version. It sits on the [element ledge](#element-ledge), and its underside is the ceiling of the film [channel](#channel). The default pressure element.

**Why it matters:** it hard-limits the film around all four sides of the window, holding any bow inside the window to 0.28 mm — comfortably within the roughly ±0.4 mm depth of field at 1:1 and f/8. It goes in once and stays; frames advance by pulling the strip underneath it. The insert is the only pressure element that comes in two formats — the [glass](#anti-newton-glass) is one sheet for both.

### Rail

The raised guiding walls in the holder base, standing 0.8 mm above the [land](#land). The inner rails set the width of the [channel](#channel) — 35.4 mm for 135 film, with a short 12 mm guide at each end, and 62.0 mm for 120 — while the outer rails, further out, carry the [element ledge](#element-ledge).

**Why it matters:** the inner rails steer the strip as you pull it through; the outer ones never touch film — they hold the pressure element. Deburr the channel mouths with a hobby knife before loading film.

### Raw

The camera's unprocessed sensor data, saved before any in-camera white balance, contrast curve or JPEG conversion.

**Why it matters:** shoot raw, always. Both [flat-field correction](#flat-field-correction) and [inversion](#inversion) work on linear data, and a JPEG has already thrown away the headroom they need.

### Run-out corridor

The clear strip along the film's path — everything within 31 mm either side of the centre line — where nothing may rise anywhere near film height, including beyond the ends of the holder.

**Why it matters:** film longer than the 120 mm holder leaves it at both ends. Inside the holder the corridor is guaranteed by the [rails](#rail); outside it, the [cover-stage](#cover-stage)'s flange top runs 0.2 mm below the film plane, so the tail rides over it — supported, not blocked. Steady the far end of a long strip by hand. The 31 mm is a half-width; 120 film is about 62 mm wide.

### Supports

Sacrificial printed scaffolding under an overhang, snapped off after the print.

**Why it matters:** none of the nine parts needs them — every one prints support-free, flat face down, with the two holder lids printed top face down. Enabling supports anyway will scar the surfaces the film slides against. See [The nine parts](printing.md#the-nine-parts).

### Sync speed

The fastest shutter speed at which the sensor is fully uncovered at one instant, so a flash can expose the whole frame rather than a band of it.

Most modern mirrorless and DSLR bodies sync at **1/160 – 1/250 s**; many older and medium-format bodies at 1/125 s or slower; a leaf shutter syncs at any speed. Your camera's own figure is in its manual and spec sheet, usually written "X-sync" or "flash sync".

**Why it matters:** **set 1/125 s and leave it.** That is at or below almost every camera's limit, and it leaves margin for the delay a cheap 2.4 GHz radio trigger adds — the *usable* sync speed with one is often a step below the rated one. Going slower costs nothing here, because in the dim room you shoot in, the pulse is effectively the whole exposure. Get it wrong and part of the frame is exposed while the rest is a clean dark band: the curtain was still crossing the sensor when the flash fired.

Do not rely on the camera capping the shutter for you. Many bodies only do that when they recognise a flash on the hot shoe, and a radio transmitter often is not recognised as one.

### TTL

Through-the-lens flash metering: the camera fires a pre-flash, measures it and sets the flash power automatically.

**Why it matters:** it is the wrong tool here and you should not pay for it. You want *identical* output on every frame so that one [inversion](#inversion) profile fits the whole roll — which means manual power, set once during calibration.

### Window

The hole in the holder base and lid that you photograph through: 25 × 37 mm in the 135 holder, 57 × 85 mm in the 120 holder. The slide-in 6×6 mask narrows the 120 view to 56.5 × 56.5 mm.

**Why it matters:** each window is deliberately about 0.5 mm oversize per side against the nominal frame, to absorb [film gate](#film-gate) variation between cameras and printer tolerance. You will see a sliver of film edge around the image — crop it in post.

### Working distance

The gap between the front of the lens and the subject, at a given [magnification ratio](#magnification-ratio). It shrinks as magnification rises.

**Why it matters:** it sets how tall your stand has to be. The film plane sits 83.2 mm above the desk, and the camera must sit that far up plus the working distance of your lens, still square to the film. See [Camera height and the stand](scanning.md#camera-height-and-the-stand).

---

← [Troubleshooting](troubleshooting.md) · [Documentation index](../README.md#documentation) · [Design](design.md) →
