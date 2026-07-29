# Design log

Why the box ended up this way, and what was tried and rejected on the way there. Useful if you are considering modifying it — several of the obvious "improvements" below were already tested and thrown out.

The design went through three phases: fixing an unbuildable first draft, collapsing a tall vertical box into a flat horizontal one, and then stripping out everything that turned out to be unnecessary.

## Phase 1 — the original draft did not close

The first specification was a vertical box, 320 × 320 × 230 mm, with two diffuser layers.

**1. The height was arithmetically impossible.** The spec called for three air gaps — 70 mm from the flash head to the first diffuser, 90–110 mm of mixing space, 40–50 mm of black chamber — totalling 200–230 mm. The interior height was only about 212–219 mm. There was no room for the flash itself, which needs 110–140 mm standing with the head raised. The rule that came out of this, and that governs everything since: **build the height by adding measured layers, never by fixing an outer dimension and back-calculating.**

**2. Diffusers with no surround leak.** The sheets were 220 × 220 and 160 × 140 in a cavity roughly 300 mm wide. Light would simply pass around them. Each diffuser was given a full-width carrier panel with only the emitting window open.

**3. "Matte white throughout" was wrong above the top diffuser.** White walls in the final chamber bounce stray light back into the film and lower contrast. That section became matte black.

**4–8.** Other corrections to the same draft: a centring stop for the flash head (a speedlight lying down puts its head off-centre, and the hot spot follows); a 9 mm plywood top with metal load points rather than 5.5 mm MDF, which the levelling screws would crush; labyrinth vents instead of straight holes, which leak light; separating lens vignetting from source unevenness by flat-fielding before judging the ±0.1 EV target; and recalculating the 4×5 provision, which had the same missing-flash-height error.

## Phase 2 — from 32 litres to 5

**9. Two diffusers → one.** Testing showed a single opal sheet close to the film already gave satisfactory evenness. The second layer and its 90 mm mixing space came out; height dropped from 364 to 316 mm. The mixing distance below the remaining sheet was *increased* to 120 mm, because the 70 mm figure in the two-layer design existed to feed the second layer, and copying it directly would have printed the flash's hot spot onto the emitting surface.

**10. Vertical → horizontal.** 316 mm was still too tall, and the reason was structural: the height was hostage to the flash standing up (130 mm) plus a vertical mixing distance, while the 320 × 320 footprint was a leftover from the two-diffuser era. Laying the flash flat and firing it sideways at a 45° reflector moved the mixing distance into the length of the box — which the flash body already occupied. 220 × 253 × 161 mm, about 28 % of the volume.

**11. Smaller flashes do not help.** Before committing, four alternatives were checked: Godox TT350, iM30Pro, iT30Pro, and the KEKS KF-01. None of them shrinks the box meaningfully. In a vertical layout the mixing distance is fixed by geometry, not by the flash — a thought experiment with a zero-thickness flash still loses to the horizontal layout. In a horizontal layout the width and depth are set by the film format and the stage, not the flash. A smaller flash only costs power headroom and recycle time. The design was fixed on the flash already owned: NEEWER TT560 + ZENIKO T1.

## Phase 3 — removing everything unnecessary

**12. The mid-level carrier panel and black chamber came out.** The acrylic went directly over the aperture and the interior became uniformly white. Height 156 → 113 mm. The 135 and 120 holders were designed and released in the same revision.

**13. The diffuser moved above the film stage.** Placing it directly under the film holder matches the workflow that had already been validated in practice. Film-to-diffuser distance became about 4 mm, which trades a dust penalty for simplicity — accepted, with cleaning made part of the session routine. The anti-direct-light baffle, its rails, and the KT-board liners were deleted at the same time; white paint straight onto the panels replaced the liners.

**14. Positive connections for vertical use.** For the box to work stood on end, gravity-located parts had to become positively fixed: four magnets in each holder base pulling onto steel washers, and the film stage clamped between two nuts on studs screwed into the enclosure instead of merely resting on them. This is also where a real mistake was caught — the stage holes had been specified as threaded. A threaded plate on a threaded stud of the same pitch is a differential screw and does not adjust at all. They became clearance holes.

**15. Plywood → 3D printing.** A laser-cut plywood shell with tab-and-slot joints was drawn and immediately abandoned when the intent turned out to be a printed box all along. Printing collapsed the wall thickness from 9 to 3 mm (220 × 285 × 113 → 208 × 273 × 96), removed all interior painting, replaced threaded inserts in wood with heat-set brass, and integrated the cable gland and access opening into the print. No internal optical dimension changed. The plywood DXFs are kept in `cad/legacy-plywood/` as a fallback.

**16. Fasteners and internal parts deleted.** Six M3 posts holding the lid down became a skirted lid that simply drops on — the skirt is both the location feature and the light trap. The drawer tray was removed (the flash lies on the floor of the box), then its rails, then the strap that held the flash, then the 45° reflector plate itself: the far wall already performs the turn, and every internal part is one more thing to align. What remains is ten printed parts, one acrylic sheet, and three studs.

**17. The film path itself.** First fit-check of the integrated stage found that two blocks sat centred on the holder ends — exactly across the channel mouths — with their tops 0.2 mm below the film plane. A strip could never be threaded. The same sweep found the front stud at (0, −100) rising to film height in the middle of the run-out corridor. The blocks became four corner Ls (|x| = 40–60, both mouths open) and the front stud moved to (45, −100); a per-vertex corridor scan (|x| < 31.5, both ends, above the stage surface) now runs clean. Lesson: checking part-to-part clearances is not enough — **the moving workpiece needs its own swept corridor treated as a part.**

---

## Things deliberately not done

**A high-CRI LED panel instead of a flash.** This is the only change that would make the box meaningfully smaller — about 100 mm tall, roughly 4 litres — because an LED panel is already an area source and needs almost no mixing distance. It was ruled out by preference for flash: freezing vibration and having power in reserve. The access panel is sized so that an LED panel can be swapped in later without changing the film plane or the camera height.

**A second diffuser for better evenness.** Costs about 43 mm of height. Worth reconsidering only for 4×5, or for slide film if the single-sheet result proves marginal.

**Ventilation.** Omitted in the prototype: a speedlight at low duty cycle produces little heat, and every hole is a potential light leak. Pull the access panel between rolls if a session runs hot.
