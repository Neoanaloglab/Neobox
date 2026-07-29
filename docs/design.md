# Design

**English** · [简体中文](design.zh-CN.md) · [日本語](design.ja.md)

Reference build: **NEEWER TT560** speedlight + **ZENIKO T1** 2.4 GHz receiver.
All dimensions in millimetres. Everything here is derived from `cad/neobox.blend`, which is the authoritative source.

## 1. Light path

```
                    film plane  ≈ 120.3
   ┌───────────────────────────────────────────┐
   │  film holder (135 or 120), flat-bottomed  │  116 – 124
   ├───────────────────────────────────────────┤
   │  opal acrylic diffuser 110 × 130 × 2      │  114 – 116
   ├───────────────────────────────────────────┤
   │  film stage 200 × 230, aperture 100 × 120 │  109 – 114  (integral blocks rise to 120)
   │           ↑ 3 × M6 studs, double-nutted   │
   ├═══════════════════════════════════════════┤
   │  top cover 4 mm, aperture 100 × 120       │   92 –  96   ← box height 96
   │                                           │
   │  white cavity, 33 mm headroom             │   59 –  92
   │                                           │
   │  ← ← ←  flash fires horizontally  ← ← ←   │    4 –  59
   │  [T1] [ TT560 lying flat ]  → far wall    │
   └───────────────────────────────────────────┘
      floor 4 mm                                     0 –   4
```

The flash head is turned 90° so it points along the length of the box at the far wall. Nothing is aimed at the film. Light fills the cavity by repeated diffuse reflection off the white PLA, exits through the 100 × 120 aperture in the top cover, and is smoothed by a single opal acrylic sheet resting on the film stage.

**Do not fit the wide-angle diffuser panel** and do not point the head upward. Set the flash zoom to 35–50 mm so the beam lands on the far wall rather than spilling directly toward the aperture.

## 2. Dimension chain

### Height (from the outer bottom)

| Layer | z range | Height |
|---|---|---|
| Floor | 0 – 4 | 4 |
| Flash lying flat (TT560) | 4 – 59 | 55 |
| White cavity headroom | 59 – 92 | 33 |
| Top cover plate | 92 – 96 | 4 |
| M6 studs (into inserts at 86) | 86 – 120 | 35 |
| Lower nut (sets stage height) | 105 – 109 | 4 |
| Film stage plate (integral blocks to 120) | 109 – 114 | 5 |
| Upper nut (clamps stage) | 114 – 118 | 4 |
| Diffuser | 114 – 116 | 2 |
| Holder base / lid | 116 – 121 / 120.6 – 124 | |
| **Film plane** | **≈ 120.3** | |

Box height is therefore **96 mm**, and the exposed height above it — studs, stage, diffuser, holder — is set by the stage geometry, not by the flash.

### Depth (267 interior + 2 × 3 walls = 273)

```
2.5  clearance at the access panel
30   ZENIKO T1 receiver, sitting on the flash foot
190  TT560 body
44.5 reflection zone between the flash head and the far wall
```

### Width (202 interior + 2 × 3 walls = 208)

The width is set by the 100 mm aperture plus the white-wall margin needed on either side for the cavity to fill evenly — roughly 50 mm per side. It is independent of the flash.

### Generalising to another flash

```
height = flash thickness  + 41
depth  = flash length + receiver length + 53
width  = 208 (unchanged)
```

Measure the flash **lying flat with the head rotated to 90°**, not standing. Do not fix the enclosure height first and back-calculate the layers; that is exactly the mistake that made the first draft of this design physically unbuildable (see [design-log.md](design-log.md), entry 1).

## 3. Optical decisions

**One diffuser, not two.** A two-layer stack (scatter + mix + final surface) gives better uniformity but costs about 160 mm of height, because each layer needs its own mixing distance. Since a single sheet close to the film already produced satisfactory evenness in practice, the second layer and its cavity were removed. If a future 4×5 version needs more uniformity, restoring the mid-level diffuser and black chamber adds roughly 43 mm.

**The diffuser sits above the film stage, not below the top cover.** It rests on the stage over the 100 × 120 aperture and is held flat by the weight of the film holder — no fixings at all. Lifting the holder exposes both faces for cleaning.

**Film-to-diffuser distance is ≈ 4.3 mm.** This is the one deliberate compromise. At 0.43× and f/8 a dust particle on the diffuser projects as a soft blob roughly 0.2 mm across at the film plane: essentially invisible on inverted negatives, but noticeable on slides. The mitigation is procedural rather than mechanical — **blow off both faces of the acrylic and the film gate at the start of every session.** Increasing the gap would help, but only by re-introducing the height the design just eliminated.

**Aperture margins.** The 100 × 120 aperture clears a 6×9 frame (56 × 84) by 22 mm on the short axis and 18 mm on the long axis, so no vignetting from the opening itself. A larger opening is not better: it lets more oblique stray light through the film base and lowers contrast.

**All-white interior, matte only.** The white PLA *is* the mixing chamber; do not paint the inside and do not use glossy or silk filament — a specular surface reproduces the flash head as a hot spot instead of scattering it. The black flash body sits directly under the aperture and absorbs light, so **tape a piece of white paper to its top face** (not over the head).

**No internal adjusters.** Earlier revisions included a 45° reflector plate and an anti-direct-light baffle. Both were removed: the far wall already performs the turn, and every internal part is one more thing to align. Evenness is trimmed from outside instead — see [assembly.md](assembly.md#calibration).

## 4. Film stage

Printed version: 200 × 230 × 5 solid plate with the four holder-alignment blocks printed directly on its top face (plate 109 – 114, blocks to 120) — one part, one flat print orientation, nothing to glue. Production upgrade: 3 mm 5052 aluminium, black anodised, from `cad/film-stage-aluminium-3mm.dxf`. Both present their top face at z = 114, so they are interchangeable.

**Three-point levelling, positively connected.** Fully-threaded M6×35 studs screw into M6 heat-set inserts in the top cover posts. The stage drops onto the studs through **Ø6.5 clearance holes** and is clamped between a lower nut (which sets the height) and an upper nut. Levelling means loosening the upper nut and turning the lower one.

> **Why three points and not four.** Three points define a plane exactly: whatever the three nut heights, the stage is fully determined, all three studs carry load, and nothing rocks. A fourth point over-constrains it — unless all four are perfectly coplanar (they never are), a rigid plate touches only three of them, and forcing contact means bending the plate, which is exactly the flatness you are trying to protect. Four-legged tables wobble; tripods do not. Symmetry is irrelevant to the adjustment itself: the front nut sets pitch (rotation about the rear pair), the rear pair set roll differentially. The off-centre front stud only adds a little cross-coupling when a single rear nut is turned — one more pass and it converges. And because the stage is clamped, not resting, hand pressure anywhere on it while threading film cannot tip it.

> **Do not tap the stage holes.** A threaded stage plus a threaded insert of the same pitch is a differential screw: turning the stud advances the stage and retracts it by the same amount, and the height never changes. The holes must be clearance holes.

**Stud positions** (relative to stage centre): front `(45, −100)`, rear `(±70, +65)`. All three studs and their nuts clear the 110 × 170 holder outline by at least 9 mm, and — just as important — they stay outside the **film run-out corridor**: film slides out through both open ends of the holder, so nothing may rise near film height inside |x| < 31 (the width of 120 film) beyond the holder ends. The front stud originally sat at (0, −100), dead centre in that corridor; it was moved sideways for exactly this reason. The holders need no cut-outs for any of the hardware.

On top of the stage: four **corner L-blocks** locating the holder in X and Y — integral on the printed stage — plus four Ø12 steel washers acting as magnet seats. (The aluminium upgrade has no printed-in blocks; re-export them from the corner features in `cad/neobox.blend`, or cut four L-pieces from any 5 mm scrap and glue them on.) The blocks sit only at the corners (|x| = 40–60) so both channel mouths stay completely open; an earlier layout with a block centred on each end blocked the film path entirely.

## 5. Film holders

Sliding-channel sandwich, two printed parts. Film sits in a 0.4 mm channel and is advanced by pulling it sideways — the holder is never opened mid-roll. Only the non-image edges are supported; the image area floats with 0.4 mm of clearance below and about 0.25 mm above. The strip overhangs the open ends of the holder while scanning, passing over the stage with about 6 mm of clearance; the corridor beyond both ends is kept free of hardware (see §4). The windows are cut about 0.5 mm oversize per side — 25 × 37 against 135's nominal 24 × 36 frame — so the full image survives both camera-gate variance and printer XY tolerance; exact framing happens in post, by cropping.

| | 135 | 120 |
|---|---|---|
| Outline (both parts) | 110 × 170 | 110 × 170 |
| Channel width | 35.4 | 62.0 |
| Window | 25 × 37 | 57 × 85 (covers 6×9) |
| Edge support each side | 4.7 | 2.25 |
| Channel height | 0.4 | 0.4 |
| Base / lid plate thickness | 3.8 / 3 | 3.8 / 3 |
| Magnets Ø6 × 2 | 12 per holder: 4+4 closure, 4 base-to-stage | same |

The base is flat — it presses directly on the acrylic. X/Y location comes from the stage blocks; the four base magnets pull down onto the steel washers, which is what allows the box to be used stood on end. For 6×4.5 and 6×6, add the printed mask (`stl/black-pla/mask-6x6.stl`) over the 120 window.

Every holder z-feature is an exact multiple of 0.2 mm and no exposed step is under two layers — land relief 0.4, rail step 0.8, channel 0.4 — so the parts print true at the default 0.2 mm layer height (0.1 also divides them; 0.12 and 0.16 do not — avoid). Print the base with the channel face down on the plate. Print one holder first and check that film slides without slop before committing to the rest.

## 6. Enclosure

**Main body** — one piece: 4 mm floor, 3 mm walls, Ø12 cable gland hole in the right wall, 190 × 76 access opening at the front. No fasteners, no glued joints.

**Top cover** — a skirted lid, 214.6 × 279.6, that drops over the walls with a 10 mm skirt and a nominal 0.3 mm side clearance. The skirt is the location feature *and* the light trap; there are no screws. Three posts underneath carry the M6 inserts.

**Access panel** — face 200 × 78 with a 186 × 72 × 4 plug behind it and a handle. The plug enters the 190 × 76 opening with about 2 mm of clearance all round, which is taken up by a strip of EVA foam wrapped around it: friction holds it, foam blocks the light. Pull it to reach the flash for power changes or batteries. Its top edge clears the cover skirt by 2 mm, so the cover does not have to come off.

**Ventilation** — none in the prototype. A speedlight at low duty cycle produces little heat; if a session runs hot, pull the access panel between rolls. (Why the lid is not fused into the body — a closed hollow box is unprintable on FDM — is in the [design log](design-log.md#things-deliberately-not-done).)

## 7. Focus light

A dimmable 5 V USB LED strip is stuck to the side wall at about z = 50, below the aperture and out of direct line to the film. Its inline dimmer stays outside the box; the cable exits through the Ø12 gland. Run it at low brightness continuously — flash exposure overwhelms it — and switch off at the end of a roll. Nothing mains-powered goes inside the enclosure.

## 8. Flash operation

Manual power only, fixed zoom, normal sync — no TTL, no HSS, shoot raw. Start metering at ISO 100, f/5.6–f/8 and adjust power for the enclosure's loss, empirically 3–5 stops. Trigger with the T1 receiver rather than a cable; a sync cable can use the same Ø12 gland if needed. The camera sits at or below sync speed, but the *effective* exposure is the pulse itself — far shorter than any real shutter speed a continuous light would allow at these settings.

The TT560 has eight full-stop steps, so fine exposure adjustment is done with the aperture in 1/3 stops. The T1 does not remote-control power, so a power change means pulling the access panel — in practice this is set once during calibration and left alone.

## 9. Repositioning and repeatability

The whole box moves ±20–30 mm in X and Y to centre the frame after the camera is levelled. Once satisfied, fit two locating pins to the base so it returns to the same place after being moved, and record the column height for each format.

## 10. 4×5 reservation

A 4×5 version needs an illuminated window around 180 × 230 and an enclosure around 400 × 400, with the height recalculated layer by layer from the flash used. At that frame size the single-diffuser structure is under real strain; plan on restoring the two-layer stack and consider two flashes or a bare-tube head.
