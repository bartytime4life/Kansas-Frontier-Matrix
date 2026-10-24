# Capability welcome · 2026-10-21 candidate

## Chat mode follow-up · 2026-10-24

GoDaddy Preview was independently verified at clean commit
`7ee04f68c55b8dd450ebaf1df6c43ee0fa428b2c`, application digest
`sha256:c5a1d14b49b71d97126dadb5f8334834cb7aefd92763678cff4df8d4e24e9b99`.
Its header tips measured 1,331px across a 1,363px desktop viewport; Previous,
Pause/Resume, Next, Find focus and Escape return worked. Production still
reported `934766fdfadbfd96f14e094f0301f9a34b981dd4` at this checkpoint.

The Preview sequence Find → close → header Chat exposed a remaining mode bug:
Chat reopened discovery. The header now explicitly selects Ask through the
existing composer handoff, preserving the unsent draft and explicit return
control. It sends no request. A focused callback regression and all five
existing responsive browser cases cover this sequence and draft preservation.

The available acceptance browser reports WebGL2 unavailable and offers no
device or reduced-motion emulation. Desktop composer/geometry observations
are separate from the isolated CI matrix; actual hosted phone, reduced-motion,
source-credit and River Pulse acceptance remain unverified in this browser.
No source data, evidence controls, settings or private stores change.

## Header, Chat and first paint · 2026-10-24 candidate

**CONFIRMED in the isolated candidate; production publication is not established.**
The current public page still displayed All questions & tools during this review,
even though PR #5447 removed it from the hosted source. Do not infer a deployed
revision from that observation. This change builds on that removal.

The information carousel now occupies the full second header row. Its text is
unmasked and unclamped, with separate 44px Previous, Pause/Resume and Next
controls. Hover, keyboard focus, hidden tabs, reduced motion and the shared
animation preference still suspend automatic rotation. Explicit pause survives
those temporary interruptions. The offscreen item is inert. Manual navigation
does not activate a layer until the current tip is chosen. The duplicate
carousel inside the phone welcome and its exclusive styles are removed.

Chat retains one header home, uses a conversation symbol, and opens the existing
composer with keyboard focus. It reveals the map workspace when opened from a
retained Reports or Stories workspace without discarding their drafts. Opening Chat dismisses the welcome and its source
strip; Escape/Close returns focus to the triggering control. Find shares this
handoff. Explicit kfm-chat=1 links bypass the welcome. No question is sent merely
by opening Chat, and evidence selection, source policies and inference settings
are unchanged. In the isolated preview inference correctly reported Awaiting
owner setup; successful answers were not tested.

The initial guide state is unresolved until URL/history and device preferences
are restored. Server markup and the identical first client render show an opaque
Opening the atlas cover and hide the map shell. The decision then removes the
cover in the same commit that mounts the graphical welcome or reveals an
intentional destination. This avoids exposing the underlying map while waiting
for the decision, without reintroducing an alternate chooser. Existing explicit
opt-out and destination handling remain; device storage is not cleared.

Geometry is owned by the Explorer's existing globals.css lane: 110px desktop
header, 126px phone header, shared by map, welcome and panel offsets. Below 1000px,
Time/Layers/Places remain in the Map menu. Find stays a visible 44px search icon
below 1100px (short landscape uses the existing Find tab in Chat); below 500px Effects uses its labelled
icon button, and at 380px or less Chat keeps a shorter visible label and full
accessible name. The tradeoff is less vertical map space for a readable tip row. Short landscape
(501px or wider, at most 480px high) instead fits tips into the command row and
uses a 54px header with a labelled chat icon. This preserves the space required
by River Pulse’s sticky heading and touch controls.

Placement basis: Directory Rules.pdf responsibility protocol and compatibility
handling, accepted ADR-0029 v1.5 and canonical docs/doctrine/directory-rules.md,
plus the verified GoDaddy composition's existing app/, tests/ and docs/ lanes.
No root, policy, contract, source registry or data lifecycle changes. The original
Sites composition and synced project reference files are untouched.

Source base: a0-hosted-ai-web-20261017 at
291cbf394209520b38af72fcad91d7dfc5da1aee; all 1,537 source blobs matched remote
Git identities before editing. No open PRs were returned during overlap checks.

Validation before the landscape follow-up: production build, TypeScript and whitespace checks passed;
full Node suite: 1,757 PASS, 19 SKIP, zero failures. Fifty-five focused navigation,
welcome, pause and focus regressions passed. Existing tests that still extracted
the retired guide's callbacks/styles now exercise the retained graphical welcome.
A new Chat dependency was added to its existing navigation harness.

Native browser inspection of the candidate covered 320, 390, 768 and 1280px
widths, all six tip texts on the narrow phone, 44px tip targets, Chat from the
welcome, composer focus and Escape return. Server HTML returned status 200,
data-startup=pending and the cover, with no retired chooser text. These checks do
not prove a frame-by-frame slow-network startup. The existing CI browser suite
now includes first-frame sampling, SSR cover checks and five responsive Chat
cases; that automated browser execution and independent review remain open.
The first terminal suite attempt was constrained by EPERM on listening sockets;
the reported complete result is the subsequent preview-capable runtime run.

The first exact-head CI run passed build, TypeScript, the full Node suite,
disposable MySQL and fire browser acceptance, then exposed River Pulse clipping
at 568×320 before startup browser tests could run. The follow-up compacts the
landscape header and adds that viewport and full text bounds to acceptance.
That failed run is not a passing acceptance result. The next CI run passed all
five River Pulse layouts, then caught hidden phone Find triggers in county-search
acceptance. Find is restored as a visible, named search icon on normal phone and
tablet layouts; the existing county-search cases remain unchanged. PR #5454 was
merged externally at head 201c462c7d828b25a2cfb489075f04f410efbb29 while
acceptance was still running. The Find correction is a separate follow-up based
on hosted 63fb2ac9795251d16837f6a817b3c7b0b73d0d82, not part of that merge.
The first follow-up run passed all county-search layouts, then found an aviation
test still clicking the former direct Layers button on compact screens. Its
navigation helper now chooses the rendered direct/mobile entry or the actual
Map-menu Layers entry, retaining strict native pointer reachability checks.
The next run passed that suite, first-frame startup sampling and all five new
Chat/tip layouts, then found source credits overlapping time at 911×600. The
existing horizontal native-control arrangement now applies through 640px height,
keeping the information button stable and its scrollable credits above time.
The original credit/time clearance assertion remains unchanged.

Rollback: revert the candidate commits. No migration, storage deletion, host
configuration, merge or publication is part of this change.


## Single welcome surface · 2026-10-23 candidate

**CONFIRMED source change; candidate browser appearance NEEDS VERIFICATION.**
The animated “Kansas is full of stories” surface is now the only startup chooser.
The older “What would you like to explore?” dialog, its All questions & tools
entry, duplicate checkbox/exit controls, mission-only question catalogue and
exclusive CSS have been removed. Six layer recipes remain in the existing
Layers controls. Search, Ask, topic destinations, source notes and map help keep
their existing owners and evidence boundaries.

The lightweight welcome component loads with the Explorer; only its WebGL scene
engine remains deferred. There is no second dialog during a delayed download.
Escape, explicit device-local opt-out, manual reopening and destination-link
bypass remain supported. Existing storage keys are retained to honor user
preferences; unrelated device storage is never cleared. A blocked storage write
cannot persist a preference across unmount/reopen.

Graphical changes keep the heading and every topic readable during previews,
move the search focus outline to the rounded field boundary, use 44px toolbar
and Scene notes targets, and stack cards on screens at or below 420px for longer
labels. The scene remains illustrative, with its synthetic-terrain caption and
source limitations. The tradeoff is a slightly larger initial UI module and a
longer phone scroll, while the heavy engine stays deferred.

Placement: inspected Directory Rules.pdf and current main ADR-0029 v1.5
(accepted) / docs/doctrine/directory-rules.md. Changes stay in the verified
hosted composition's existing app/, tests/ and docs/ responsibility lanes;
no roots, source registries, contracts or release homes are added. This does
not change the original Sites composition or any dataset lifecycle state.

Source base: hosted a0-hosted-ai-web-20261017 at
1f9c2a83b0963734ee84b6e83be3e8127bb0bdfd. The isolated source snapshot was
verified against every remote Git blob before editing. No open PRs were
returned by the GitHub pulls API during the overlap check.

Validation: production build, TypeScript checking, and five focused test files
(startup, welcome, layer recipes, demos and playback) passed locally. Candidate browser acceptance is not claimed: the production
server could not bind a listening socket (EPERM) in this execution environment.
The existing CI startup browser suite is updated to hold the deferred scene
engine, check there is no alternate chooser, preserve keyboard/storage checks,
and require readable headings/cards during hover. CI results are separate
from these local checks. Review narrow phone, landscape, desktop, source-strip
access, Escape/reopen, reduced motion, all topic destinations and delayed scene
loading before merge. No deployment or publication is performed here.

Rollback: revert the cleanup commit. No data migration, storage deletion or
host configuration change is needed.

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
