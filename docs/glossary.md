# Glossary

**English** · [简体中文](glossary.zh-CN.md) · [日本語](glossary.ja.md)

> One line for every term the NeoBox documents use as if you already knew it, and one line on why it matters in this project. Other pages link straight to the entry they need.

**Contents:** [Base ISO](#base-iso) · [Bed size](#bed-size) · [Bridging](#bridging) · [Camera scanning](#camera-scanning) · [Channel](#channel) · [Clearance hole vs tapped hole](#clearance-hole-vs-tapped-hole) · [Copy stand](#copy-stand) · [Differential screw](#differential-screw) · [Diffuser](#diffuser) · [EFCS](#efcs) · [Elephant foot](#elephant-foot) · [EV](#ev) · [Film gate](#film-gate) · [Flat-field correction](#flat-field-correction) · [Guide number](#guide-number) · [Heat-set insert](#heat-set-insert) · [HSS](#hss) · [Infill](#infill) · [Integrating cavity](#integrating-cavity) · [Inversion](#inversion) · [Land](#land) · [Layer height](#layer-height) · [Magnification ratio](#magnification-ratio) · [Manual power fraction](#manual-power-fraction) · [Newton rings](#newton-rings) · [Opal](#opal) · [Perimeters](#perimeters) · [Rail](#rail) · [Raw](#raw) · [Run-out corridor](#run-out-corridor) · [Supports](#supports) · [Sync speed](#sync-speed) · [TTL](#ttl) · [Window](#window) · [Working distance](#working-distance)

## A–Z

Three vocabularies meet in this project — film photography, 3D printing and mechanical fastening — and a reader is rarely fluent in all three. Every entry below is written for someone fluent in none of them.

> [!TIP]
> Part names are a separate matter. Every part is named once and never renamed. Printed: **main body**, **top cover**, **access panel**, **film stage** with its **corner blocks**, **film holder** (**holder base** / **holder lid**). Bought: **diffuser**, **stud**, **lower nut** / **upper nut**. If you cannot match a name to a shape in front of you, see [Part vocabulary](printing.md#part-vocabulary), which ties each one to a feature you can see.

### Base ISO

The lowest true sensitivity of a camera's sensor — usually ISO 100 — where it has the most dynamic range and the least noise.

**Why it matters:** the flash has power to spare inside the box, so there is no reason ever to leave base ISO. Metering starts at ISO 100 and f/5.6–f/8. See [Exposure](scanning.md#exposure).

### Bed size

The printable area of an FDM printer's build plate, quoted as X × Y.

**Why it matters:** it is a go/no-go, not a preference. The largest part is the top cover at 214.6 × 279.6 mm, so the main body and the top cover need a bed of at least 280 × 300 mm; everything else fits a 220 × 220 bed, except the printed film stage at 230 × 200 mm, which needs its long axis checked against your usable area. See [Will it fit your printer?](printing.md#will-it-fit-your-printer).

### Bridging

Extruding filament straight across an unsupported gap between two anchored points, so it spans in air and cools before it can droop.

**Why it matters:** the lintel over the 190 × 76 mm access opening in the main body is far too wide to bridge, which is why that part is one of only two printed with [supports](#supports).

### Camera scanning

Photographing a negative with a digital camera on a stand, instead of feeding it through a flatbed or drum scanner. Also called DSLR scanning, whatever camera you use.

**Why it matters:** NeoBox is the light source for this method and nothing else. It does not hold a camera, and the camera, lens and stand are yours to provide. See [What camera scanning is](getting-started.md#what-camera-scanning-is).

### Channel

The 0.4 mm high slot the film strip slides along inside the film holder — 35.4 mm wide in the 135 holder, 62.0 mm in the 120 holder. Its floor is the [lands](#land), its sides are the [rails](#rail), its ceiling is the pressure strips on the holder lid.

**Why it matters:** film is loaded and advanced by sliding it sideways through the channel; the holder is never opened mid-roll. A 0.4 mm feature is two printed layers at 0.2 mm, which is why the [layer height](#layer-height) is not free to change.

### Clearance hole vs tapped hole

A clearance hole is larger than the fastener and lets it pass straight through — the film stage has three Ø6.5 mm clearance holes for M6 studs. A tapped hole carries a thread, and the fastener screws into it.

**Why it matters:** the stage rides up and down its studs on nuts, so its holes must be clearance holes.

> [!CAUTION]
> Never tap the three stage holes. A threaded plate on a stud already threaded into a same-pitch insert becomes a [differential screw](#differential-screw), and the stage height then cannot be adjusted at all. Ø6.5 mm clearance holes are mandatory.

### Copy stand

A vertical column on a baseboard that holds a camera pointing straight down at an adjustable height. A tripod with a horizontal or reversible centre column does the same job.

**Why it matters:** the film plane sits about 120.3 mm above the base of the box, and the stand must clear that plus the [working distance](#working-distance) of your lens while holding the sensor parallel to the film. See [Camera height and the stand](scanning.md#camera-height-and-the-stand).

### Differential screw

Two threads acting in series on the same axis, so that turning them moves the load by the *difference* between their pitches — which is zero when the pitches are equal.

**Why it matters:** it is the trap that a tapped film stage would fall into. With an M6 thread in the stage and the same M6 thread in the [heat-set insert](#heat-set-insert) below it, turning the stud moves the stage nowhere and levelling becomes impossible.

### Diffuser

A translucent sheet that scatters light passing through it into an even glow. In NeoBox there is exactly one: an [opal](#opal) acrylic diffuser, 110 × 130 × 2 mm, resting loose on the film stage over the aperture and held flat by the weight of the holder.

**Why it matters:** it is the last optical surface before the film, about 4.3 mm below the film plane. Nothing fixes it in place, so nothing can bend it — but dust on it projects as a soft blob about 0.2 mm across at the film plane, invisible on inverted negatives and visible on slides, which is why both faces get blown clean every session.

### EFCS

Electronic first-curtain shutter: the exposure begins electronically at the sensor and ends with the mechanical rear curtain.

**Why it matters:** EFCS still fires a flash, and it removes the shock of the opening curtain. A *fully* electronic (silent) shutter is a different setting and usually will not fire a flash at all. See [Exposure](scanning.md#exposure).

### Elephant foot

The slight outward bulge of the first few layers of a print, squashed wider by the nozzle and the heated bed.

**Why it matters:** it lands on two fits that have almost no room — the top cover's 10 mm downstand rim, designed with a nominal 0.3 mm side clearance, and the access-panel plug. Turn on your slicer's elephant-foot compensation. See [If it came out tight or loose](printing.md#if-it-came-out-tight-or-loose).

### EV

Exposure value. One EV is one stop: a doubling or halving of the light reaching the sensor.

**Why it matters:** it is the unit the evenness target is written in. NeoBox aims at ±0.1 EV corner to corner — a tenth of a stop — judged after [flat-field correction](#flat-field-correction).

### Film gate

The rectangular opening that defines the exposed area of a frame: the metal aperture in a film camera, and by extension the [window](#window) in the film holder that you photograph through here.

**Why it matters:** camera gates vary slightly between bodies, so the holder windows are cut about 0.5 mm oversize per side to swallow that variation and printer XY tolerance. It also names the surface you must blow clean every session, along with both faces of the diffuser.

### Flat-field correction

Photographing the evenly lit surface on its own, with no film in place, and then dividing your real frames by that reference so that lens vignetting and any unevenness in the light cancel out.

**Why it matters:** it comes first, before any judgement about the box. It is the only way to separate lens vignetting from real unevenness in the source, and the ±0.1 [EV](#ev) target applies to what is left afterwards. See [Calibration](assembly.md#calibration) and [Flat-field and inversion](scanning.md#flat-field-and-inversion).

### Guide number

A flash's power rating: guide number = aperture × distance for a correct exposure at ISO 100. The reference NEEWER TT560 is GN38, in metres.

**Why it matters:** it is the figure printed on the box, and inside NeoBox it tells you almost nothing, because light reaches the film only after several diffuse bounces. Start metering at ISO 100 and f/5.6–f/8, then add an estimated 3–5 stops of flash power for enclosure loss.

### Heat-set insert

A knurled brass sleeve pressed into a printed hole with a soldering iron; the plastic melts around the knurls, cools, and leaves a real metal thread in the part.

**Why it matters:** three M6 inserts in the top cover's posts anchor the three studs that carry the film stage. Setting them is the only step in the whole build that needs a hot tool — a soldering iron at 200–250 °C for PLA. See [Tools and consumables](bom.md#tools-and-consumables).

### HSS

High-speed sync: the flash fires a rapid train of small pulses so it can be used at shutter speeds above the camera's [sync speed](#sync-speed).

**Why it matters:** it is useless here, and you may be asked to pay for it. In a closed dark box you shoot at or below sync speed by choice.

### Infill

The internal lattice that fills the space between a part's [perimeters](#perimeters), given as a percentage of solid.

**Why it matters:** 15–25 % is enough for every part except the film stage, which carries the levelling nuts and must stay flat, so give it at least 30 %. See [Print settings](printing.md#print-settings).

### Integrating cavity

A closed volume with matte white walls in which light bounces many times until its direction and brightness even out. The laboratory version is the integrating sphere.

**Why it matters:** NeoBox is one. The flash lies on the floor firing horizontally at the far wall, and nothing is aimed at the film — the evenness comes from the bounces, not from the diffuser alone. This is also why the interior is left as bare white filament and must not be painted. See [How the light works](../README.md#how-the-light-works).

### Inversion

Turning a captured negative into a positive image: inverting the tones, removing the orange mask of colour negative film, and setting contrast and colour.

**Why it matters:** it is the last step of the workflow, and it is where a constant light source pays off — every frame on the roll gets the same flash output, so one inversion profile fits the whole roll. See [Flat-field and inversion](scanning.md#flat-field-and-inversion).

### Land

The narrow ledge inside the holder base that the edge of the film rests on: 4.7 mm wide on each side in the 135 holder, 2.25 mm in the 120 holder.

**Why it matters:** the top face of the land *is* the film plane. Only the outer edges of the strip touch anything — the image area floats, with 0.4 mm of clearance below it and about 0.25 mm above.

### Layer height

The thickness of one printed layer. It quantises every horizontal feature in the part: a feature that is not a whole number of layers cannot be printed at its designed size.

**Why it matters:** print everything at 0.2 mm. 0.1 mm also divides every feature in the design. 0.12 and 0.16 do **not** divide the holder features — avoid them. See [Print settings](printing.md#print-settings).

### Magnification ratio

How large the subject appears on the sensor, divided by its real size. 1:1 — written 1.0× — means the frame is projected onto the sensor at life size.

**Why it matters:** it decides which lens you need. A 135 frame on full frame needs 1.0×; a 6×6 frame on full frame needs 0.43×. Any 1:1 macro lens covers every format NeoBox handles, because the larger formats need *less* magnification. See [Magnification and lens choice](scanning.md#magnification-and-lens-choice).

### Manual power fraction

The flash's output set by hand as a fraction of full power — 1/1, 1/2, 1/4 and so on down to 1/128 — with each step exactly one stop.

**Why it matters:** manual power control is one of only two things that matter when choosing a flash for this box. The TT560 gives 8 full-stop steps, which is coarse, so fine exposure adjustment is done with the aperture in 1/3 stops instead.

### Newton rings

Irregular coloured interference fringes that appear where film is pressed against a smooth surface such as glass or acrylic.

**Why it matters:** the holder is built so they cannot happen. Nothing touches the image area — the film floats in the [channel](#channel) with 0.4 mm of clearance below it, and the diffuser is a separate sheet about 4.3 mm below the film plane.

### Opal

Milky-white translucent acrylic that scatters light through its whole thickness, rather than at a textured surface.

**Why it matters:** opal is not the same product as frosted, which is clear sheet with a matte face, and ordering the wrong one is an easy mistake. NeoBox needs one 2 mm opal sheet cut to 110 × 130 mm. See [Getting the right part](bom.md#getting-the-right-part).

### Perimeters

The solid outlines the printer traces around the edge of every layer, also called walls or shells.

**Why it matters:** use at least 3 everywhere. The enclosure walls are only 3 mm thick and their job is to be opaque — a wall that is mostly [infill](#infill) leaks light.

### Rail

The raised side wall in the holder base that guides the film strip, standing 0.8 mm above the [land](#land).

**Why it matters:** the rails set the width of the [channel](#channel) — 35.4 mm for 135 film, 62.0 mm for 120 — and the lid's pressure strips drop between them with 0.3 mm of side clearance. Deburr their mouths with a hobby knife before loading film.

### Raw

The camera's unprocessed sensor data, saved before any in-camera white balance, contrast curve or JPEG conversion.

**Why it matters:** shoot raw, always. Both [flat-field correction](#flat-field-correction) and [inversion](#inversion) work on linear data, and a JPEG has already thrown away the headroom they need.

### Run-out corridor

The clear strip along the film's path — everything within 31 mm either side of the centre line — where nothing may rise anywhere near film height, including beyond the ends of the holder.

**Why it matters:** film longer than the 170 mm holder has to run out across the stage on both sides. Anything standing in that corridor stops the strip, so the corner blocks are placed only between 40 and 60 mm from the centre line and the front stud is deliberately offset. The 31 mm is a half-width; 120 film is about 62 mm wide.

### Supports

Sacrificial printed scaffolding under an overhang, snapped off after the print.

**Why it matters:** only two of the nine parts need them — the main body, for the lintel over the 190 mm access opening, and the access panel, under the rim of its face plate, a 3–7 mm overhang. Everything else prints support-free, and enabling supports on the holders will scar surfaces the film slides against. See [The nine parts](printing.md#the-nine-parts).

### Sync speed

The fastest shutter speed at which the sensor is fully uncovered at one instant, so a flash can expose the whole frame rather than a band of it.

Most modern mirrorless and DSLR bodies sync at **1/160 – 1/250 s**; many older and medium-format bodies at 1/125 s or slower; a leaf shutter syncs at any speed. Your camera's own figure is in its manual and spec sheet, usually written "X-sync" or "flash sync".

**Why it matters:** **set 1/125 s and leave it.** That is at or below almost every camera's limit, and it leaves margin for the delay a cheap 2.4 GHz radio trigger adds — the *usable* sync speed with one is often a step below the rated one. Going slower costs nothing here, because inside the closed box ambient light contributes nothing and the pulse is the whole exposure. Get it wrong and part of the frame is exposed while the rest is a clean dark band: the curtain was still crossing the sensor when the flash fired.

Do not rely on the camera capping the shutter for you. Many bodies only do that when they recognise a flash on the hot shoe, and a radio transmitter often is not recognised as one.

### TTL

Through-the-lens flash metering: the camera fires a pre-flash, measures it and sets the flash power automatically.

**Why it matters:** it is the wrong tool here and you should not pay for it. You want *identical* output on every frame so that one [inversion](#inversion) profile fits the whole roll — which means manual power, set once during calibration.

### Window

The hole in the holder base and lid that you photograph through: 25 × 37 mm in the 135 holder, 57 × 85 mm in the 120 holder.

**Why it matters:** each window is deliberately about 0.5 mm oversize per side against the nominal frame, to absorb [film gate](#film-gate) variation between cameras and printer tolerance. You will see a sliver of film edge around the image — crop it in post.

### Working distance

The gap between the front of the lens and the subject, at a given [magnification ratio](#magnification-ratio). It shrinks as magnification rises.

**Why it matters:** it sets how tall your stand has to be. The film plane sits about 120.3 mm above the base of the box, and the camera must sit that far up plus the working distance of your lens, still square to the film. See [Camera height and the stand](scanning.md#camera-height-and-the-stand).

---

← [Troubleshooting](troubleshooting.md) · [Documentation index](../README.md#documentation) · [Design](design.md) →
