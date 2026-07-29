# Assembly, power and calibration

About 15 minutes once the parts are printed. There are no glued structural joints and no screws holding the enclosure together.

## What connects to what

| Interface | Method |
|---|---|
| Main body | One printed piece — nothing to assemble |
| Top cover → body | Skirted lid, drops on. The 10 mm skirt locates it and traps light. No screws. |
| Film stage → cover | Three M6×35 studs into heat-set inserts, stage clamped between two nuts |
| Diffuser → stage | Rests on the aperture, held flat by the holder's weight |
| Holder → stage | Four alignment blocks for X/Y, four magnets onto steel washers |
| Access panel → body | Plug wrapped in EVA foam, friction fit |

## Steps

1. **Heat-set the inserts.** Press three M6 brass inserts into the posts on the underside of the top cover with a soldering iron. Let them cool before loading.
2. **Paint the outside.** Mask the interior and the aperture, then spray the outside of the main body and the top face of the cover matte black. The inside stays bare white filament.
3. **Fit the cover** onto the main body. Add a strip of EVA foam along the wall top first if you want a tighter light seal.
4. **Build the stage.** Screw the three M6×35 studs into the inserts. Run a nut down each one, drop the stage on through its Ø6.5 clearance holes, then add the upper nuts. Start with all three lower nuts at the same thread count, then level against the camera (mirror-on-the-film-plane method): the front nut adjusts pitch, the rear pair adjust roll. Two passes converge; lock the upper nuts. Three points is deliberate — see the note in [design.md](design.md#4-film-stage).
5. **Add the stage furniture.** The alignment blocks are already part of the printed stage; just glue the four steel washers to the top face. (Prototype shortcut: the washers and holder magnets can be skipped if you never stand the box on end. With the aluminium stage, also glue on the printed alignment blocks.)
6. **Diffuser and holder.** Lay the acrylic over the stage aperture; set the film holder on top of it, inside the alignment blocks.
7. **Light source.** Lay the flash on the floor of the box with the head turned 90° toward the far wall, receiver on its foot. Tape a piece of white paper to the top face of the flash body — the black body sits right under the aperture and will otherwise print as a dark patch. Stick the LED strip to the side wall at about 50 mm and run its cable out through the Ø12 gland.
8. **Close up.** Wrap EVA foam around the access panel plug and push it into the opening.

After calibration, draw a line on the floor of the box around the flash so it can be put back in exactly the same place.

## Power

Nothing mains-powered goes inside the enclosure.

| Device | Power |
|---|---|
| TT560 | 4 × AA, no external port. Two sets of NiMH cells in rotation is the practical setup. |
| ZENIKO T1 | Own battery (USB-C or coin cell depending on unit) |
| LED strip | USB 5 V from a power bank or charger, inline dimmer outside the box |
| Camera | Batteries; a dummy battery is worth it for long scanning sessions |

A single two-port USB charger on the desk covers the LED strip and the trigger.

## Calibration

1. Photograph the bare lit surface with no film in the holder, raw, at the aperture you will actually use.
2. Apply flat-field correction in post first — this separates lens vignetting from genuine source unevenness. The target for the source itself is roughly **±0.1 EV corner to corner**.
3. If it does not meet that, in this order:
   - Centre the flash and check the white paper patch on its body.
   - If the far end reads brighter than the near end, stand a white card temporarily at the far wall and change its angle.
   - As a last resort, stick a small translucent attenuating dot at the centre of the underside of the diffuser.
4. When you are satisfied, fit two locating pins to the base of the box and record the column height for each format.

Flash exposure freezes any residual vibration, but it cannot fix a film plane that is not parallel to the sensor. Parallelism is still the first thing to get right — level the stage with the three nuts, and use a small mirror on the film plane to align the camera before worrying about evenness.

## Using the box on end

The design supports standing the enclosure vertically:

- **Holder** — the four base magnets onto the steel washers plus the alignment blocks carry it in any orientation. *If you skipped the magnets during the prototype build, do not use the box on end.*
- **Stage** — studs into inserts with double nuts, rigid in any orientation.
- **Access panel** — add a strip of tape so it cannot fall out, and a piece of foam in the gap beside the flash so it cannot shift.
- **Diffuser** — held by the holder.

## Session routine

Blow both faces of the acrylic and the film gate before starting. The film sits only about 4 mm above the diffuser, so dust there shows as a soft blob about 0.2 mm across — harmless on inverted negatives, visible on slides.
