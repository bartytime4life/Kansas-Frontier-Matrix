# Capability welcome · 2026-10-21 candidate

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
