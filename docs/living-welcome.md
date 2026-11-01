# Capability welcome · 2026-10-21 candidate

Current navigation is described in [Direct workspace entry · 2026-10-31](#direct-workspace-entry--2026-10-31).
It supersedes the historical click-to-preview and automatic hover transition
described below. Earlier implementation and validation records are retained.

## Responsive quality follow-up · 2026-10-31 candidate

**CONFIRMED CI finding; PROPOSED correction.** The browser job for hosted commit
`3b1b41b81a0622cb5c685a24a2250f542cb04556` passed all four new wheel/scroll
journeys but failed full-card reachability at 320×568 and 640×360. Compact panels
now use at most 24% of the viewport height. At widths up to 1100px and heights up
to 480px, the panel follows the page's normal scroll flow: this deliberately
trades persistent context for enough room to operate a complete category card.
Desktop and taller compact windows retain the sticky context panel. The existing
all-category geometry checks remain strict; a 320×568 wheel journey is added.

The same CI run found three draft-persistence journeys selecting a title field
while Reports was in its current default dashboard view. Those journeys now
activate the visible **Edit report** control before editing. The assertions for
independent report/story storage, immediate navigation and reload remain intact.
This corrects the acceptance journey, not the report persistence implementation.

Evidence: [browser job 124719634568](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/runs/41262905561/job/124719634568).
Rendered acceptance of this follow-up remains NEEDS VERIFICATION until its own
browser job completes. Local build/type checks cannot establish browser geometry.
Placement uses the same existing presentation, test and documentation roots
described below. Rollback reverts this three-file follow-up together; no data,
provider, settings or publication change is involved.

## Welcome scrolling repair · 2026-10-31 candidate

**PROPOSED release; not published.** The ordinary chooser now keeps its category
information beside the scrolling cards. Desktop uses a reserved sticky column;
tablets and phones use a compact sticky panel above the cards. The panel's own
long content remains scrollable, with normal gesture handoff at its boundaries.
Responsive scroll padding leaves room for keyboard-focused cards below it.

The fixed decorative map no longer takes pointer input while browsing categories.
Previously, scrolling the heading away exposed a fixed map canvas outside the
normal scroll chain: wheel gestures there could stop moving the chooser. The
panel also left the viewport with that heading. The single renderer, category
selection, source clocks and attribution remain separate from these layout rules.
Expanded previews retain their own controls and hide the chooser's context panel.

Validation records must distinguish the public reproduction from the candidate:
real browser wheel input reproduced the disappearing panel and the exposed-map
scroll trap. The candidate's production build, project TypeScript check and 39
existing welcome-component cases pass locally. Added hydrated browser regressions
cover desktop, tablet and phone geometry, wheel input below the panel, and nested
scroll handoff. Local rendered candidate acceptance is NEEDS VERIFICATION because
the executor refused its preview listener with EPERM; hosted CI and independent
visual review remain separate. No live correction or provider-data claim follows
from those source checks.

Placement follows the adopted Directory Rules/ADR-0029 and this standalone
composition's AGENTS instructions: existing application presentation, conformance
and human-guidance files only. Rollback reverts the two presentation files,
browser regressions and this note together; no data or settings migration is
involved. Merge and publication remain separate owner-controlled transitions.

## Cinematic category stage · 2026-10-30 candidate

**PROPOSED release; implemented candidate, not published.** Starting evidence:
hosted branch `a0-hosted-ai-web-20261017` at
`372c052a97a975b8b3401f9230e97da522cffda3`, tree
`e390e2bde30ed60799d6e39ad2e9c8575f70736f`. The local validation snapshot was
reconstructed from the connector's exact commit files and verified to that
entire Git tree; its local snapshot commit is not the upstream commit.

A single click/tap or Enter on a category now opens its existing map preview
across the welcome window. A fine-pointer hover previews immediately and enters
the same stage after 650 ms of continued interest. Leaving before that deadline
cancels it. Tab focus alone keeps the grid in place. Once the stage opens, moving
into the map does not make the cards reappear underneath the pointer.

The active category has a compact edge panel. All 22 categories remain in a
horizontal bottom rail, derived from the existing shared taxonomy. Click/tap,
Left/Right (wrapping), Home and End select another category. The rail scrolls
without creating a second renderer or loading unselected category scenes.
Selecting the current rail item preserves the layer-comparison setting.
Return/Escape restores the original card and grid scroll position; another
Escape dismisses the welcome. Source notes remain a separately dismissible
modal, recorded tours remain opt-in, and the category-map action still enters
the existing Explorer workspace. Pause and reduced motion retain still scenes.

The rail is included in geology spotlight obstruction measurements. Controls
remain at least 44px; short landscape layouts use two independently scrollable
edge panels. Provider attribution keeps its reserved bottom strip. Source clocks,
missing/unavailable states, limits, and publication status are unchanged.

### Placement, validation and rollback

This edits only existing presentation files in `app/living-welcome/`, existing
`tests/`, and this `docs/` file in the separately governed hosted composition.
The placement basis is accepted [ADR-0029](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/main/docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md)
and the [adopted Directory Rules](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/main/docs/doctrine/directory-rules.md): responsibility before subject,
no parallel authority home, no lifecycle or compatibility-root migration.
The supplied unversioned Directory Rules PDF was not available locally; the ADR
identifies it as a superseded lineage artifact, not the current placement authority.
The supplied Living Atlas interface PDF was consulted as proposed design lineage,
particularly persistent-map, source-clock and presentation-versus-evidence boundaries.

The component suite exercises settled/cancelled hover, touch and keyboard entry,
all category choices, modal/visibility/disposal cancellation, rail wrapping,
paused scrolling and restored focus/scroll. The existing browser journeys are
updated for the new explicit stage-to-notes flow and include rail geometry,
actual pointer/touch input and screenshots. Deterministic tests and build checks
do not establish rendered browser acceptance, GPU performance or live-provider
correctness. This session's sandbox refused a loopback listener (`EPERM`), so
local Chrome candidate acceptance remains **NEEDS VERIFICATION**. Exact-head CI
results and visual review must be attached separately; no unrun browser check is
claimed passing.

Risk: an incorrect responsive layout could obscure a control or map feature;
a hover/focus race could move a visitor unexpectedly. The deadlines, explicit
exit, modal handling and focused regressions constrain those risks. Performance
savings and frame rates are not claimed. Rollback is a focused revert of this
presentation change; no data, credentials, schemas, release recipes, dependencies,
stores, hosting settings or migrations change. Merge and publication are separate
owner-controlled steps.


## Fauna and public-safety entries · 2026-10-29

The welcome now derives 21 entries from the existing shared topic taxonomy.
**Fauna & wildlife** appears in Earth & environment and **Crime &
public safety** in People & place. Both reuse the existing card, dialog,
keyboard navigation, category-map entry and Layers catalogue controls.

The two previews use landscape and civic reference geography with no provider
starters or verified footage. Their dedicated glimpses and source limitations
explain that animal observations, crime reports, court records and live
emergency incidents are not connected. Existing Observatory occurrence context
is linked separately; optional DeFlock plate-reader reports retain their own
meaning and are never automatically switched on. Neither a wildlife inventory
nor a crime/safety score is inferred from these maps.

The welcome count says to explore each map's coverage and source limits so a
category's presence does not promise a connected feed. Details, classification,
placement and rollback are recorded in [Category maps](category-maps.md#fauna-and-crime-justice--public-safety).
These entries change navigation and presentation; governed Fauna evidence,
source admission and publication require their existing separate checks.

## Start-page rendering repair · 2026-10-28

This follow-up starts from public composition
`bd562032da270cab2ffc7dfc70ec30a730b7214e`, preserving the nineteen categories,
their map looks, recordings, source clocks, entry controls and chosen pixel density.

The preview now becomes visible on the first rendered frame after its selected
style loads. Previously it also waited for `map.loaded()`, which includes
optional provider and terrain sources: a source that remained pending could
leave a usable map permanently transparent, including with reduced motion.
Renderer readiness is not a claim that all tiles or observations have loaded.
Existing loading, empty, unavailable and dated-source disclosures remain
independent. A rejected style installation reports unavailable without exposing
its exception and a deliberate category retry re-reads that style document.
WebGL context loss hides the preview and marks its parent status unavailable;
source refreshes cannot clear that renderer failure. A new rendered frame
restores both visibility and parent status. The context/status regression failed
before that follow-up correction.

A welcome opened in a hidden tab defers its idle renderer startup until visible.
Queued startup is cancelled on hide/dismissal, visibility changes reuse the same
engine, and an already-running asynchronous operation retains its cancellation
guard. This does not suspend or replace the installed Explorer service.
Pointer highlights retain one owned animation-frame callback, stop during
pause/reduced motion, and cancel pending writes when the welcome closes.

Deterministic regressions cover a styled frame with unresolved optional sources,
style rejection/retry, context loss, hidden startup, duplicate visibility events,
pointer bursts and cleanup. The pending-source regression failed before the
renderer repair. These are behavior/operation-count checks, not physical GPU,
FPS, live-provider, field-INP or long-duration memory qualification. Rendered
browser and exact-head CI results belong to their separately recorded run.

Placement reuses existing `app/living-welcome/`, `tests/` and this `docs/`
responsibility under accepted ADR-0029 / Directory Rules. No source data,
geometry, dependency lockfile, AI model/database, account, DNS, access policy or
release control is changed. Rollback reverts this focused source change; no
store migration is required. Public publication remains on hold.

## Preview performance follow-up · 2026-10-27

This follow-up starts from hosted-branch commit
`d38a574f8ece9cba4fe210f6bec3631a1042d8c0` (tree
`d65636b0935ed1aecbcb441f750cce86c645d494`), including #5516/#5517.
The nineteen category glimpses and real-map identity are reused.

A deterministic counterexample confirmed that selecting A, B, then A while A's
style document is pending rebuilt A twice. A generation check now gives only
the latest application ownership of the shared promise and style-load callback.
The new regression fails against the base engine and passes against the fix.
The welcome retains at most 48 tiles (32 for touch-first, 24 in Battery saver),
or the existing smaller budget. Selected pixel density stays intact. Battery
saver uses still category cameras; intentional category navigation still works.
These are configured limits, not measured RAM savings or production FPS gains.
The first measurement attempt exposed a 40px expanded Pause control (and the
Return control was configured at 36px). Both now have 44px minimum hit areas,
checked by the responsive browser matrix as well as the performance journeys.
The next rendered journey caught Escape from Pause/Resume removing the focused
button and leaving focus on the document body. Returning from an expanded view
now focuses its persistent Expand control in the layout commit; a second Escape
can dismiss the welcome. Both the component regression and native-key journeys
cover this exact sequence.
The same first run also exposed an older source-text assertion coupled to the
replaced style-key guard. It now checks only the style-loading boundary; the
existing supersession/retry and new A→B→A tests execute those behaviors instead.

The first slow-network run at `5bdbb193eac9831bc60eff7ed3e562172c1e3b9a`
observed first content paint near 9.7 seconds and hydration near 15.5 seconds on
the emulated phone. That journey failed at the undersized Pause control, so it
is a partial diagnostic, not acceptance. Build inspection found no compressed
JS/CSS siblings, although the pinned server already negotiates them. The
existing postbuild asset-staging script now creates deterministic Brotli and
gzip siblings for hashed JS/CSS of at least 1 KiB, verifies immutable destinations
and stages those variants with their original files. Only smaller variants are
kept. Original content and filenames stay unchanged; source datasets, HTML,
API responses, media and private/reflected content are outside this operation.
No runtime/dependency replacement or provider/cache-policy change is required.
Unit checks decode the variants byte-for-byte and exercise repeat/conflict
handling. The existing real HTTP asset tests now cover Brotli/gzip/identity
negotiation, exact decoded content, HEAD, Vary and hidden variant URLs. Build-byte
savings are not substituted for remeasured network, paint or interaction times.

An independent CI job measures the actual built/hydrated application at desktop
1440×960 and emulated phone 390×844 at 2× density, including 4× CPU slowdown,
80 ms network latency and 200,000 bytes/second throughput. The phone is also
tested with reduced motion. JSON reports and screenshots are retained in the
`welcome-performance` Actions artifact for 14 days. Reports bind to the exact
checked-out source and browser version. They contain first paint, observed LCP,
time to hydrated welcome, request bytes, input event delays/durations, automation
readiness times, long tasks, animation-frame callback gaps, main-thread task,
script/layout/style time and three post-GC reopen-cycle heap samples. The test
also verifies one shared preview canvas, no automatic tour decoder, teardown,
pause/resume, reduced motion and entry into the real aviation category map.

The 15-second readiness and 32 MiB retained-renderer-heap checks are coarse
failure guards, not production service objectives. Frame callback cadence is
not rendered FPS. Input observations are not field INP, the short-run LCP is
not a Core Web Vitals population result, and GC samples exclude workers,
native/GPU allocation and thermal effects. Empty style documents and unavailable
provider APIs deliberately isolate UI/resource handling; these measurements
cannot qualify realistic provider-tile rendering, provider health, physical
mobile performance or long-session leaks. Live-provider and physical-device
acceptance remain NEEDS VERIFICATION. The local sandbox denied listeners and
Chrome execution, so rendered claims must come from CI, not local syntax checks.

The preceding #5517 run
[40561242835](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/runs/40561242835)
passed install/build/types, the Node suite, MySQL and fire browser checks, but
failed one welcome row-position assertion and two workspace navigation cases.
The row test mixed native focus scrolling with layout movement; it now prevents
scroll for that assertion, while separate native keyboard/scroll journeys stay
in place. The workspace failures remain unresolved evidence until a new run;
they are not declared inherited or passing. No timeout or functional assertion
is removed to hide these failures.

Placement remains within existing `app/`, build-owning `scripts/`, `tests/`,
`docs/`, the existing package manifest and platform `.github/workflows/`
responsibilities under adopted Directory Rules / ADR-0029.
No new source, release/proof home, storage format, dependency or host setting is
introduced. Rollback reverts this follow-up commit. Review and exact-head CI are
separate from merge, deployment and publication authority.

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
category destinations. The expanded map hides the entire grouped category field;
its later grid rule no longer overrides the fullscreen visibility rule. There is
still one welcome map,
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


## Guided category glimpses — 2026-10-27

Status: proposed implementation; changed-build visual and production-performance acceptance remain NEEDS VERIFICATION.

The starting page keeps its single real MapLibre preview and the existing 19-topic taxonomy. Each card now names a category-specific glimpse and indicates whether recorded tours or guided starting points are available. This is presentation of existing provider context, not admission or release of new records. Reused recorded captures retain their context labels and original clocks; no new footage is invented.

The shared glimpse is available below 1,100 pixels instead of disappearing there. Selecting a category still opens its source-aware details. Entering the expanded map adds a compact guide with a look-for prompt, limitations, source-notes access and a direct entry into that category’s map. Categories with starter overlays offer Hide/Show starter layers for a before/after comparison; this hides the starter overlays and population prisms while retaining the basemap and elevation. Categories without previewable starter overlays use their map and guided starting point; the UI does not offer a comparison that would do nothing. River gauges remain excluded from hover previews; aviation volumes and calculated sky tools still require the opened workspace.

Performance constraints: one preview map, no additional media assets, no automatic video download, no style rebuild for comparison. Hidden overlays do not initiate new payload requests or radar/satellite refreshes. A request already in flight may complete into the cache, but cannot reveal a hidden overlay. Restoring loaded data reuses the cache. Motion/pause updates no longer call show(topic); only a topic change selects a new preview. Existing pointer settling, render budget, cache limits, hidden-tab pause and reduced-motion behavior remain in force. These are implementation constraints, not measured production-speed claims.

Placement: existing app/living-welcome owns welcome presentation and preview behavior; tests owns its behavior checks; this existing docs narrative owns explanation and acceptance limits. Directory Rules responsibility-based placement and accepted ADR-0029 apply; no new root, data store, schema, policy or release home is created.

Validation: regression tests exercise every category’s guide and destination, reduced-motion comparison and category resets, late payload completion while hidden, deferred provider requests and cached restore without style rebuild. Production build and TypeScript checking completed locally. Browser acceptance of this candidate remains blocked by local listen EPERM; do not transfer observations of the older public page to this candidate.

Before release: inspect 1280×800, 390×844 and 568×320; keyboard Return/Escape/Tab and nested details; guide scrolling without obscuring map navigation; all 19 correct destinations; unavailable/empty/stale source captions; hiding/restoring overlays while a request resolves; provider attribution. Measure cold/warm startup, long tasks, network bytes, category-switch latency and memory on representative mobile hardware against the exact base. Check that the new card copy and responsive guide do not push essential entry controls out of reach. No universal frame-rate or Core Web Vitals result is claimed.

Rollback: revert this bounded welcome change; no provider, store, hosting configuration, DNS or published data rollback is involved.

## Expanded preview failure handling — 2026-10-28

The expanded demonstration checks map unavailability before category identity,
loading and comparison copy. A failure without a category identifier is global
preview failure, including when starter overlays are hidden. Initial loading and
reports from a previous category still show “Preparing the category map…” until
the selected category reports readiness. A failed provider remains separate from
a failed map. Both callback failures and rejected engine initialization notify
the welcome owner. A later successful preview replaces the failure message.

The existing status region, design, source notes and full-category-map action
are retained. Component and engine regressions cover missing/stale identifiers,
disabled WebGL, failed initialization, provider failure, switching, recovery,
comparison and both map-entry callbacks. The hydrated browser suite additionally
exercises WebGL/construction failure, keyboard notes/return/map entry, readable
scrolling guidance and comparison recovery at 1280×800, 390×844 and 568×320.
These isolated provider fixtures establish UI behavior, not live provider health.
Repository integration targets the existing hosted source branch; production
publication remains a separate operation. Rollback is a revert of this correction.


## Flora and vegetation

The 22-category starting page includes **Flora & vegetation**. Its map opens
NLCD 2021 land cover, offers annual GBIF plant-record hexagons and USDA crop
layers, and keeps source dates, rights and occurrence limits explicit. See
[Flora data, controls and boundaries](flora-map.md).

## Cinematic keyboard navigation — 2026-10-30

The demonstration actions immediately precede Return in native DOM focus order.
From Return, Shift+Tab reaches Source notes & demonstrations, then the category's
map action. Tab follows the same path forward. The category rail follows the
scene controls in DOM order; its existing absolute positioning preserves the
visual composition. No positive tabindex, page-wide Tab handler or focus trap
is introduced for the non-modal welcome.

The category buttons form a named horizontal toolbar with one Tab stop: the
currently selected category. Left/Right select and focus adjacent categories,
wrapping at either end; Home/End select the first/last. An accessible description
explains these keys. The two scroll buttons remain independently tabbable, and
mouse selection, settled hover and touch use their existing handlers.

Only entering the cinematic stage moves focus to Return. Closing source notes
restores their exact opening action before paint. Return and Escape still restore
the original chooser card and scroll position, even after selecting another
category in the rail. Reduced motion can disable Pause without adding a dead
keyboard stop.

Placement follows the inspected Directory Rules.pdf responsibility rule and
ADR-0029: the existing standalone hosted composition owns presentation in
`app/`, regression checks in `tests/`, and this behavior record in `docs/`.
No root or lifecycle boundary changes. The authoring baseline is hosted commit
`7a4ea2c4a9cc20903214fd8a6f6a0215f69a67c1`; its complete tree was matched locally
to `f1ffd0fd2822c5c7255e03efc816f069a6495512` before editing.

Regression coverage includes native forward/backward navigation, rail re-entry,
arrow/Home/End selection, nested-dialog focus restoration by Escape and pointer,
Return/Escape restoration, primary map entry, and desktop, tablet, narrow phone
and landscape reduced-motion layouts. Local and CI acceptance results belong
to the pull request's exact-head evidence. Isolated provider fixtures establish
UI behavior, not live source availability, physical-device or screen-reader
qualification. GitHub review, source integration, hosted Preview acceptance and
public publication remain separate. Rollback is a revert of the correction;
no provider, data, hosting configuration or stored preference migration occurs.


## Direct workspace entry · 2026-10-31

Selecting a category card now opens its actual map and its category-filtered
Layers panel in one action. Keyboard focus enters that panel after welcome
dismissal; users can toggle sources, change opacity, inspect data and clear the
topic filter immediately. Existing category starter sets and source boundaries
remain authoritative. Water animation defaults are unchanged.

Hover and keyboard focus retain the map glimpse and card highlight while the
card grid stays in place. They never schedule the former 650 ms transition into
a full-window demonstration. Each card has a separate **Preview** action for
that optional stage, preserving Aviation zone modes, the Geology recorded log,
source notes, comparison controls, pause/reduced-motion behavior and the category
rail. Return/Escape restores the Preview button and chooser scroll position.

Placement stays in the existing standalone `app/`, `tests/` and `docs/` roots
under the accepted Directory Rules / ADR-0029 responsibility boundaries. This is
navigation and focus behavior, with no dataset, dependency, model, database or
release-policy change. Revert the source commit to roll back; no store operation
is needed. Public publication remains on hold. Browser and CI results are
recorded separately from authoring and do not establish release authority.
