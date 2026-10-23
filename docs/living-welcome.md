# Capability welcome · 2026-10-21 candidate

## Transportation scene polish · 2026-10-22 candidate

The illustrative transportation backdrop now sizes vehicles to the road lanes
instead of enlarging them for visibility. Close camera views follow the same
vehicle positions as the overview. Road traffic uses consistent right-hand
lanes, measured model footprints, following gaps, gentle acceleration and
exclusive at-grade junction reservations. Reservations include a train's whole
consist. Dirt roads later paved over share one physical traffic lane. Main-line
trains travel in one direction per track, with passenger traffic on its separate
line; branch rail geometry remains visible without dispatched branch trains.

Road crossings of the synthetic river have raised decks, guardrails and piers.
The freeway interchange has a separate overpass elevation; vehicles and road
geometry use that same height profile. Bridge components are instanced in two
draw batches per span, and duplicate dirt/paved bridge structures are avoided.
Traffic, aircraft, town density, smoke and glow have been reduced. Buildings
are kept clear of transportation corridors and the main river. Horses have
separate bodies, heads, legs and harness traces; train bodies have longer
proportions relative to cars and trucks.

The traffic controller uses fixed 1/120-second steps and reconstructs its state
on rewind. Pause and seek preserve deterministic positions. Its behavior is
illustrative staging, not a road engineering simulation, historical traffic
reconstruction, live transport feed, or evidence of road access or safety. The
existing synthetic-scene caption, source captures and workspace actions remain.

Placement follows accepted ADR-0029 and the inspected canonical
`docs/doctrine/directory-rules.md`: application scene code remains under the
existing `app/living-welcome/scenes/` responsibility, executable regressions
under `tests/`, and this behavior record under `docs/`. No new authority root,
source admission, policy, data lifecycle transition or storage is introduced.
`Directory Rules.pdf` is absent from the supplied local attachment inventory;
the accepted repository doctrine and ADR are the checked placement basis.

The source base is hosted branch `a0-hosted-ai-web-20261017` at
`6a725fe64c0cccefec0a7b474d52b6f8e67d2ed0`. Its complete materialized local
tree was verified against GitHub tree `7f9920d243dc32290ea715d93cc3d6b6ec9d6381`
before editing. Focused regressions cover lane containment, following gaps over
the complete 36-second loop, at-grade exclusion, train-tail clearance, mixed
speeds, stop/resume, pause, seek and rewind. Construction checks do not render
the scene or prove GPU performance.

Browser visual acceptance remains open. The public page was inspected, but
this browser reported WebGL2 unavailable. The supervised local preview built
successfully and then timed out because the Node composition listened on port
3000 while the preview expected 4173. No candidate screenshot, mobile visual
acceptance, smoothness judgment or production publication is claimed. Review
the 1860s, 1910s, 1940s, 1970s and current-era scene in a WebGL2 browser before
merge and deployment. Roll back by reverting the single polish commit; no data
or host configuration needs changing.

The current candidate replaces the welcome's representative footage with animated
captures of the actual Explorer. The legacy footage modules, original recordings
and their rights manifests remain as rollback/authoring inputs; the welcome no
longer imports or mounts their players. It does not deploy a GoDaddy release.

## Navigation and options

All 17 categories and their facets come directly from `app/layer-workspaces.ts`.
There is no second domain taxonomy. Selecting a category or preview does not
activate layers, change map time, request AI output or admit data. The explicit
source-workspace action uses the existing topic callback. Facets describe that
workspace; they are not independent data-activation controls.

## Animations and scope

`CapabilityPreview.jsx` mounts only the chosen animated WebP, or its existing
poster when paused, hidden, reduced-motion or failed. Opening details holds the
background still. Expanded viewing uses the welcome window and retains Return,
Pause and Escape; it does not invoke browser fullscreen. Focus moves to Return
when a detail selection opens expanded viewing.

The 16 animations derive from the source-bound recordings already described in
`scripts/welcome-demos/runtime-assets.json` and `app/living-welcome/map-demos.mjs`.
They show recorded software output, not current observations or a live tutorial.
Source clocks and limitations remain attached. Contextual reuse for geology,
ecology, engineering, people, land and hazards is labeled explicitly. Sky and
Evidence workspaces have no verified capture: they show that limitation and a
working destination instead of invented animation. Capturing those two actual
workflows remains open work.

Use `python3 scripts/welcome-demos/build-animations.py /path/to/ffmpeg` to rebuild
WebPs from the original local recordings. The output manifest binds source and
derivative hashes. No remote source is fetched. At runtime only a selected
capture is requested; the largest animation is about 5.3 MB. This trades video
compression efficiency for the requested image-animation presentation.

## Time instrument

`TimeEmblem` now uses the transparent generated hourglass delivery sprite and
CSS keyframes: ten seconds of sand transfer followed by a 0.8-second half-turn.
The button has no visible border, fill, rounded container or shadow; keyboard
focus remains visible. This is decoration, not a playback timer or data-coverage
claim. Animation preference, hidden-tab and reduced-motion gates retain a still
frame. Hover/focus/tap calendar controls and source-loading states are preserved.
The generation/normalization record is next to the existing time artwork.

## Authority, placement and rollback

ADR-0029 identifies `docs/doctrine/directory-rules.md` as the canonical human
placement authority. Its responsibility protocol and the existing standalone
composition place UI in `app/`, browser delivery images in `public/`, authoring
conversion in `scripts/welcome-demos/`, regression checks in `tests/` and this
behavior record in `docs/`. Directory Rules.pdf was located, but its text/page
reader returned no readable content; the accepted canonical repository doctrine
and ADR were inspected instead. No new root, contract home, lifecycle transition,
source admission, data migration, policy change or Sites synchronization occurs.

Base source is the hosted composition at `a2755f07efe4bd01c2ed89b2cd392dc1d7b27ad9`.
The complete local base tree was verified against GitHub tree
`cc40874d1cfe1253d534af32a9d6564bd0885e0c` before authoring. Roll back by reverting
the candidate commit. Retained original assets make this dependency-closed; no
stored data or home-PC inference setup needs changing.

## Verification boundary

Build, type checking, changed-component lint and targeted component regressions
are engineering evidence only. A local production preview was attempted on port
4187; the environment denied `listen` with EPERM. No rendered candidate, actual
hover/flip smoothness, small-phone geometry or live-provider end-to-end acceptance
is claimed. Keep delivery a draft pending browser acceptance and independent
review; no merge, publish, deploy or promotion is authorized here.
