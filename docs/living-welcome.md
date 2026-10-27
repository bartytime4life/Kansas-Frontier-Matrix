# Capability welcome · 2026-10-21 candidate

## Category layer glimpses · 2026-10-27 candidate

**CONFIRMED source behavior and local checks; hosted acceptance is a separate gate.**
The owner selected the existing real-map welcome as the visual direction and
requested more thoughtful category demonstrations with performance first. The
shared nineteen-category taxonomy and its map looks stay in place. Each topic
now has its own short demonstration: what the map previews, something to look
for, the next available tool, and the relevant source/display limitation.
A shared desktop brief describes the selected category; phones get the same
material in the existing category dialog. Preview is presentation only and does
not activate an investigation layer or admit a source.

The default statewide map is static. Camera drift runs only while a category is
engaged or explicitly expanded, and stops on ordinary departure, modal opening,
global pause, hidden tabs or reduced motion. An interrupted category flight lands
on its intended view before holding, so resuming cannot strand the map between
category destinations. There is still one welcome map,
loaded after paint, and one selected capture at most. No new renderer, font,
image, model, dependency or large media asset is added. Existing map-resolution
preferences are retained rather than reducing cartographic label quality.

Recorded Explorer captures start with a lazy still. A requested native video
plays once, with pause/replay, hidden-tab/global-pause handling, failure recovery
and decoder cleanup on replacement or dismissal. Opening a category no longer
starts an animated WebP decoder. Science no longer reuses a terrain recording
as a satellite demonstration; Geology no longer reuses groundwater footage as
an earthquake demonstration. Those categories use the real map glimpse and
explicitly disclose the absence of a verified matching recorded tour. Other
reused recordings keep their original context label, time and limitations.

Science's preview now reads the existing fixed NOAA satellite-frame adapter and
selects one checked current catalog frame. GeoColor and the separately dated
visible-band fallback remain distinct. The existing 90-minute source freshness
bound is reapplied before drawing; stale or failed frames stay absent. Radar
retains its own freshness rule. Held previews do not poll either manifest;
expiry checks still clear stale frames. Style reads have a 15-second deadline,
provider JSON/manifest reads 12 seconds, and pending reads are coalesced locally.
Loaded, empty, unavailable, closer-zoom and provider-tile states are distinct.
A count describes returned source records, not a claim that every record is
visible or that a tile loaded successfully. A failed style can be retried by
reselecting its category. The full River Pulse network remains behind the
opened map's controls; it is not fetched on hover just to decorate the welcome.

The supplied Living Atlas v0.1 design (a PROPOSED design, not runtime evidence)
and Google Earth Patterns reference informed the persistent map, purposeful
views, visible source clocks and bounded motion. Current category/source modules
govern the actual behavior. Placement reuses this standalone composition's
existing app/, tests/ and docs/ responsibilities under adopted Directory Rules
and accepted ADR-0029; no schema, contract, registry, lifecycle or proof home is
created. The preserved Site and read-only sources/ references are untouched.

Local qualification: 61 focused welcome, map-engine, playback and satellite
checks passed; production build and TypeScript passed. Changed-file lint has
zero errors and one inherited unused terrain-destructuring warning. The reused
local dependency installation is not an exact-lock qualification. A local
production server could not listen (EPERM), so actual hydration, layout and native
video acceptance run in the existing isolated CI browser suite. That suite now
checks category-specific content, poster-only opening, native requested video
play/pause and source limits, and retains welcome screenshots with the existing
14-day workspace artifact. Provider APIs are unavailable fixtures and off-origin
traffic is blocked: this is not hosted provider-health acceptance.

The first exact-head delivery run, [40559833962](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/runs/40559833962)
at `9b0dc07f83f231628d696d95a16419b7146c3546`, passed exact-lock install,
build, types and both MySQL checks. The Node suite reported 1,960 cases:
1,940 passed, one failed, 19 skipped. The old capability-preview test still
expected automatic image animation and lacked the new playback-helper import.
This patch-caused test migration was omitted from the initial focused run; it
is not attributed to the environment. The follow-up checks poster-only behavior
across pause, visibility and category changes, retaining archive/provenance and
uncaptured-domain checks. Explicit native playback/error cleanup remains covered
by the new demo tests and the required browser cases. Browser stages were skipped
after the suite failure; only the follow-up exact-head result can qualify them.

Performance protection is bounded to idle motion, decoder admission, polling,
request deadlines and source reuse. No production FPS, energy, memory or Core
Web Vitals gain is claimed without measurement. Exact-head CI, manual rendering,
physical/other-engine checks, real upstream imagery and long-session behavior
remain separate evidence. Roll back by reverting this source change; no browser
storage migration, data reset, host-setting change or publication is included.

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

## Synthetic scenes removed · 2026-10-26

The three.js scenes that stood behind the categories (`app/living-welcome/scenes/`,
including the transportation traffic staging recorded here on 2026-10-22), their
smoke script and their tests are removed. The welcome now shows each category's
real map instead; see "Live map behind the categories" below. The removed code
remains in the repository history.

The current candidate replaces the welcome's representative footage with animated
captures of the actual Explorer. The legacy footage modules, original recordings
and their rights manifests remain as rollback/authoring inputs; the welcome no
longer imports or mounts their players. It does not deploy a GoDaddy release.

## Navigation and options

All 19 categories and their facets come directly from `app/layer-workspaces.ts`.
There is no second domain taxonomy. The welcome groups them under the four
`TOPIC_GROUPS` headings, and each card carries a three-colour sketch and the name
of its map look from `app/category-maps.ts`.

Hovering, opening details or previewing a category does not activate layers,
change map time, request AI output or admit data. Two explicit actions do:

- **Open the {map look}** (primary) calls `onMap`, which runs `openCategoryMap`.
  It applies that category's basemap, renderer (2D, 3D terrain or globe) and
  camera, switches on its few starter provider-context layers additively, and
  filters the Layers catalogue to the category. Nothing the visitor already
  switched on is turned off, and map time is unchanged. A small dock on the map
  then names the map look and offers 2D/3D/Globe, relief, sun direction, reset
  and the category's layers.
- **Explore {category} sources** keeps the existing topic callback and opens the
  Layers catalogue without changing the map.

Facets describe the workspace; they are not independent data-activation
controls. Aviation and Government have their own specialized basemaps (an
aviation chart and a civic map; see `docs/category-maps.md`) and their own
illustrative scenes.

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
ecology, engineering, people, government, land and hazards is labeled explicitly.
Aviation, Sky and Evidence have no verified capture: they show that limitation and a
working destination instead of invented animation. Capturing those three actual
workflows remains open work.

Use `python3 scripts/welcome-demos/build-animations.py /path/to/ffmpeg` to rebuild
WebPs from the original local recordings. The output manifest binds source and
derivative hashes. No remote source is fetched. At runtime only a selected
capture is requested; the largest animation is about 5.3 MB. This trades video
compression efficiency for the requested image-animation presentation.

### Live map behind the categories

The domain stage is a live map, not an illustration. `DomainStage.jsx` lazily
loads `app/living-welcome/map-engine.mjs`, which keeps one non-interactive
MapLibre map behind the welcome (provider credits stay on it in the compact
attribution control).

- **Which map.** `app/welcome-map-view.ts` takes each topic's basemap, view
  (2D, 3D terrain or globe) and camera from `CATEGORY_MAPS`, the same look the
  category opens with in the Explorer. The base map choice decides the preview.
  3D terrain looks get their own Terrarium DEM source; globe looks the globe
  projection.
- **Before a choice.** Until a visitor points at, focuses or pins a category,
  the stage shows the Explorer's default vector map over the whole state. So
  providers that are off by default (Esri imagery, the Kansas aerials, USGS
  topo and the Terrarium DEM) are requested only for a category the visitor
  chose to preview.
- **Its data.** A previewed category also shows its starter layers. The engine
  calls the Explorer's own `applyOfficialContextState` with only those
  starters visible, so tiles and GeoJSON are styled exactly as in the
  Explorer; GeoJSON starters (counties, earthquakes, alerts) are read from the
  same `/api/live-context` adapters and shared between previews for five
  minutes. Radar shows its newest advertised scan from `/api/noaa-radar/frames`
  (`setNoaaRadarObservationTime`), only while that scan passes the Explorer's
  freshness rule; the caption gives the scan time, and a stale or unavailable
  frame list shows no radar and claims none. The rule is applied again on every
  draw, and a selected radar preview is re-checked every minute (a new frame list
  every two), so a scan that ages past it leaves the map and the caption. GOES imagery and river gauges need
  live controls (the satellite frame list or the River Pulse adapter) and are
  left out of previews (`WELCOME_PREVIEW_SKIPPED_STARTERS`); they appear when
  the map is opened. The caption names the map, its view, the data drawn at the
  preview's zoom and its basemap credits.
- **Motion.** While the welcome plays, tilted and globe views turn slowly about
  their centre and flat maps ease gently in and out (`welcomeDriftLeg`). Pause,
  reduced motion, a hidden tab and open details hold the camera still.
- **Switching.** A pointer sweep across the cards restyles once it settles
  (220 ms). A preview with the same basemap and view only moves the camera.
  Styles are resolved by the engine and passed whole to `setStyle`, because
  `setStyle`'s `transformStyle` waits for the previous style to load and would
  stall every later preview after one provider failure.
  The style applied or pending is tracked by basemap and view, apart from the
  selected topic, so topics that share a style (Science and Sky, or Evidence
  and the default map) can take turns while it loads and it still applies.
- **Ready.** The map fades in on its first frame after a real style has loaded
  with its tiles settled. MapLibre's `idle` would also wait for the camera to
  stop, which the drift never does.

`tests/welcome-map.test.mjs` covers the views, the terrain and globe styles and
the drift; `tests/welcome-map-engine.test.mjs` drives the real engine against a
stand-in map for shared pending styles, superseded styles and readiness; `tests/living-welcome.test.mjs` covers the
default-map rule. Provider tiles cannot be reached from the development
container, so the rendered maps were checked by their provider requests, not by
eye.

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
