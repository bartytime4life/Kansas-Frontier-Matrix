# Underground Explorer

The current area-first flow is described in **Area underlay and record-time navigation — 2026-10-07** below. Earlier sections retain the progression of probe, cutaway and individual-log behavior.

This addition starts from owner-private Site v155, source `d8f2db1ee6e0fedd495ed538a85ad23b3302e2ae`. It preserves the existing Map Library, place dossiers, Evidence Drawer, reports, Earth Engine controls, DB/R2 bindings, and Site audience. GitHub PR #4899 merged during implementation; the feature review starts from `8c955317117e53fa93ece5d0af4455d86fad17b3`, retaining its separate CodeQL test correction. The dirty owner maintenance checkout is not used as an import source.

## Original probe and workbench behavior

Open **Underground** directly from the map dock. The surface map remains above a resizable panel. Hover for nearby recorded columns; click to pin. The fixed surface crosshair, directional buttons, and **Inspect here · map center** provide keyboard/touch navigation. A pin survives map movement. The probe is a search location, not a claim that the nearest borehole describes that precise location.

County navigation and an on-demand statewide ID/county locator cover 314,844 mapped WWC5 records and 6,598 core locations. Well/core chips change the underground query only. Results cover up to eight spatial tiles around a 25 km probe/section corridor, return up to 50 records, and show up to 20 columns. Long sections, missing tiles, invalid records, and truncation are explicitly reported. Empty results mean none in the available data. Provider point markers and the selected interval remain linked without replacing existing map sources.

**Draw a section** uses the existing distance drawing interaction. Finish that line, then choose **Use drawn section**. Distances along the route and offsets use spherical segment projection with endpoint clamping. The chart shows each record's own reference depth, not a common elevation section. Enable the existing surface DEM and sample it separately to see a surface profile; missing DEM samples remain gaps. The DEM is not used to invent sea-level alignment for boreholes.

Original log descriptions remain separate from KGS standardized interpretation codes. Invalid depths are excluded and accounted for by the preparer; valid gaps and overlaps remain. Core start/end values describe inventory envelopes, not recovered material throughout the range. Available photographs open the original KGS per-well pages; the display does not invent photographic coverage. Selecting a source interval opens its original description, unit, depth reference, source time, location method, limitations, source link, and photo link in the existing Evidence Drawer.

**Aquifer shape** is the default for a new underground investigation; an explicitly saved view is restored. **4D material explorer** is the dynamically loaded Three.js recorded-column view. It extrudes one selected record into a textured block whose horizontal width is illustrative and has no geographical footprint. Original depths and unknown gaps are preserved. Unambiguous original material descriptions receive deterministic soil, clay, sand, gravel, shale, sandstone, limestone, dolomite, salt, gypsum, coal or ore-mineral display textures; these are not photographs or measured grain sizes. Mixed, qualified and fluid descriptions stay neutral. Core inventory envelopes stay violet even if a title names a rock. No interpolated seams, fluid volumes, mineral reserves or mine tunnels are invented.

Orbit/zoom, front/top/reset camera buttons, layer selection, description/material isolation, opacity, separated layers and depth slicing support inspection. Canvas clicks open the original interval in the existing inspector. The bounded list below the canvas offers keyboard and low-resource inspection. Separate-layer spacing is illustrative; slicing temporarily suppresses separation to retain recorded depths. Vertical scale is labeled, while horizontal scale is explicitly unknown. Changes to clipping, opacity and material isolation reuse geometry and the camera. The renderer draws only on interactions/resize, caps pixel ratio at 1.5 and meshes at 500 intervals, disposes textures/geometries/controls on teardown, and offers retry plus the list after WebGL failure.

The fourth dimension is **record time**, not geological evolution. Choose an available year or play discrete years among the loaded well/core records. Cumulative dated records through that year qualify; undated records are withheld until All available records is selected. The bounded spatial subset is clearly identified: this does not claim every Kansas well in every year. Surface-map year eligibility still applies first. Playback stops at the last year, during location/source/tab changes, in a hidden document, and under reduced motion. Manual year stepping remains available. The optional validated `recordCutoff` persists in investigations and captured report context. Camera orientation, opacity, separation and material isolation are temporary inspection controls; exports remain source-labeled 2D columns, not screenshots of illustrative textures.

**Geophysical surveys** distinguishes electrical, electromagnetic, GPR, and seismic methods. Four qualified KGS electrical collections provide 21 measured conductivity profiles and 25,479 original samples, shown in mS/m against depth below local land surface. The trace is decimated to at most approximately 600 display points without changing the retained source values. Approximate Google Earth positions do not establish a surveyed horizontal or elevation datum. Duplicate-series and invalid-location profiles remain held. GPR/tTEM entries remain reference links; no radar time is converted to depth without a qualified velocity model, and conductivity is never relabeled as lithology.

**Soil horizons** queries the existing public USDA Soil Data Access service through a bounded, read-only Site route. It retains separate soil-map components, proportions, centimetre depth units, retrieval time, and the 100-horizon response limit. These alternatives do not establish the exact soil beneath the pointer. Browser-location privacy suppresses this external coordinate lookup.

## Persistence and exports

The optional validated `SubsurfaceContext` extends existing workspaces/reports without changing storage keys or the database. Workspaces retain settings, source hashes/editions, and record IDs, then reload eligible current assets. Missing records and changed source versions are labelled; captured rows never masquerade as a fresh response. Old workspaces/reports remain readable and quota/storage errors follow existing handling.

Reports capture bounded KGS source rows and source editions with a capture timestamp. Provider context remains separate from included evidence and does not create EvidenceRefs or an EvidenceBundle. Reports provide a source-labelled interval CSV and a self-contained SVG column diagram with explicit depth/reference/spacing limits. CSV formula prefixes and SVG metacharacters are escaped. The image is a recorded-column diagram, not a geological reconstruction. Current geophysical, live soil, and display-DEM views are separately labelled and are not included in this first KGS column snapshot.

Browser-location redaction removes the entire underground context from saved/exported state, including coordinates, transects, record IDs, and section images. It also suppresses direct interval/image downloads. The underground privacy flag remains sticky during an investigation. No screenshot of the unrestricted canvas is used as a redaction shortcut.

Source archive editions, observation/record dates, interpretation editions, and retrieval times remain distinct. In historical map frames, WWC5/core records with later or unknown record dates are held; the archive is still a current source edition, not a reconstructed historical inventory. Soil and geophysical views explicitly retain their own source editions.

## Data and path ownership

See [subsurface-data.md](subsurface-data.md) and [subsurface-geophysics.md](subsurface-geophysics.md) for receipts, rights, transformations, exclusions, and reproducibility. Compressed KGS assets total 22.9 MB and are spatially partitioned, hashed, and fetched in a worker with request cancellation and a bounded tile cache. The statewide locator is loaded only for a search. Asset hashes provide immutable edition identity even though the display URLs remain stable across Site deployments.

Placement follows the adopted Directory Rules and accepted ADR-0029: application behavior, display assets, source preparation, regression tests, and behavior documentation remain in this standalone application's existing `app/`, `public/`, `scripts/`, `tests/`, and `docs/` responsibilities. The GitHub mirror remains under `apps/site/source`. These are provider display derivatives, not a new registry, evidence store, governed processed-data root, or database migration. No source admission, promotion, or independent evidence acceptance is implied.

## Delivery and remaining qualification

Review is separated into source assets/contracts, linked sections/persistence, and qualified pilot field profiles/optional 3D presentation. The full Kansas River sediment-model cutaway is **blocked**: native numerical model geometry and redistribution qualification remain unavailable. Published pictures are not numeric depth surfaces. GPR/tTEM raw numerical assets remain unverified. These holds do not prevent the statewide recorded-column viewer from working.

Validation covers full asset integrity and field exclusions, original workbook sample bounds, coordinate/depth/radar handling, gaps/overlaps, duplicate identity, section offsets, historical holds, canceled responses, unavailable/corrupt sources, legacy storage, quota failure, source-labelled exports, redaction, and bounded soil requests. Type check, production build, and full Site regressions run before packaging. Browser access still fails the admin policy security check; visual, keyboard-flow, mobile, and WebGL acceptance are pending and must not be inferred from unit/build success. Runtime UI controls and CSS have been implemented, but no browser performance or smoothness acceptance is claimed.

Rollback retains saved v155 (`appgprj_6aa0b1c41bc08191bfd86003920f1631~appgver_769352625ae8819192b37861a2d0bc12`) and its source. No DB migration or binding change is required. The inherited repository `MIRROR_REVIEW_REQUIRED` receipt gate remains separate; feature checks cannot waive it.


## Material-view delivery, 2026-10-06

The material-view update starts from private Site v157 / `363f769aed44198c5f73da3cc4e2ef48b1bb6372`, whose then-live compact HUD was later superseded by the shared map dock. It adds `app/subsurface-materials.ts` within the existing application display responsibility and regression coverage under `tests/`; no source, registry or data-store root is added. No new remote acquisition, dependency, storage migration or source-admission operation is introduced. Revert to saved v157 to roll back this presentation update without changing DB/R2. The previous v155 rollback above is historical to the initial underground implementation.

Material tests cover qualified/negative/mixed descriptions, inventory separation, fluid words, deterministic bounded textures, date eligibility, persistence and privacy. Build/type/tests do not establish visual, WebGL, touch or performance acceptance; browser access remains unavailable. Continuous extrapolation remains held for missing common elevation/trajectory registration and qualified numerical correlation surfaces. KGS describes correlation as a separate inference step: https://www.kgs.ku.edu/Publications/OFR/2002/OFR02_51/index.html. WWC5 originals and standardized interpretations are distinct: https://apps.kgs.ku.edu/web/Waterwell/index.

## Linked locator and aquifer ranges — 2026-10-06

This update starts from saved private Site v158, source `4fe2e09326dfcd88f0e6117a7474aad9908af262`. Rollback uses that saved version; no storage/binding migration is involved.

Entering Underground selects a flat, north-up map and reserves at least a 300 px surface/header region above the panel. The locator remains outside the underground scroll area. Its marker selection, map-center action, find-selection action and 2D reset control point to the same loaded well/core records. Panel height can change without eliminating the locator. Resize observation keeps MapLibre's canvas synchronized during the 380 ms entry transition; reduced motion removes it. Mouse/touch rotation is constrained to keep this locator flat, and prior gesture availability is restored on exit. Floating weather docks are temporarily concealed without changing selected sources.

**Aquifer shape** builds a browser-local possible depth envelope for the High Plains aquifer using existing, hash-pinned KGS depth-to-water and saturated-thickness snapshots for 2022–2024. Polygon intersection preserves source outlines and holes. At each overlap, the shallow outer bound is the lower depth-to-water class bound; the deep outer bound is the upper depth-to-water bound plus the upper saturated-thickness bound, converted from feet to metres. This is an uncertainty envelope, not evidence that its entire volume is occupied by groundwater. No class midpoint, hydraulic gradient, storage quantity or groundwater flow is inferred. Open-ended and missing classes remain withheld. These are regional classified estimates, with the original 0.0005-degree display generalization.

The 3D scene includes a captured image of the flat locator at the same bounds as the clipped polygons. The surface plane stays at zero and all envelope depths below it under orbit; opacity controls are independent. This is a **flattened local-ground reference**, not surveyed surface terrain or an elevation-registered geological model. Snapshot capture is local to the browser, bounded to 1,024 pixels on its long side, and only accepted after locator tiles are complete. It is not uploaded, saved, or exported. View changes invalidate the prior locator identity; geometry can render over a neutral extent plane while a same-view image completes and attaches later. The linked 2D map remains available if 3D or capture fails.

Loaded records are plotted at recorded horizontal positions, with approximate locations and their separate record-depth references. They are not verified vertical well trajectories. Logs use up to 50 records/400 intervals and clip 50 m below the deepest envelope (500 m if no envelope). No inferred strata connect them. The timeline changes eligible well/core records; the aquifer remains a single dated 2022–2024 surface pair. There is no historical aquifer-volume animation. Soil components and electrical survey measurements remain separate, rather than being converted into aquifer boundaries.

Acquisition stays with existing groundwater snapshots; new `app/aquifer-volume*` files are application display/model derivatives in the existing Site root, with tests in `tests/`. The dedicated worker verifies digests, caps each input at 800,000 bytes, deadlines at 12 seconds, accepts views at most one degree wide/high in Kansas, and caps output at 64 overlaps, 256 polygons and 20,000 vertices. Rendering is on demand and GPU resources/listeners are disposed. Preparation adds no server endpoint, database, new provider query or dependency. Reports/save contexts state that aquifer geometry and surface images are not captured; the existing KGS column snapshot/export remains unchanged.

Open qualification: historical numerical surfaces, precise vertical registration, other aquifer shapes, soil/core correlation models, and browser visual/touch/WebGL acceptance. Structural and data tests cannot certify seamless browser animation. The KGS Atlas and existing `docs/aquifers-groundwater.md` document source roles and units.


## Rendering repair — 2026-10-06

Repair baseline: saved/deployed private Site v159, source
`2e03afb186fa8a5a934c72d8dccd678c24bc03b3`. The previous source made water/wind
canvases span the entire map stage after Underground shortened the map canvas.
Their dots could therefore stretch across the underground interface. Both effects
and their hover label now share a clipped, isolated surface at exactly the
locator's desktop/mobile bounds, below panels and controls. Reduced-motion
behavior remains consistent. The geographic drawing functions and selected
layers are unchanged.

Aquifer geometry preparation now begins independently of locator tile completion.
Previously, one incomplete weather/source tile could prevent all geometry from
being prepared. Verified geometry can now appear while imagery is unavailable;
the neutral outlined plane is explicitly labeled as an extent, not a basemap.
A later complete image attaches without rebuilding the aquifer geometry or
resetting the camera. Capture failure and an eight-second image timeout do not
hide eligible shapes. Map movement cancels the previous display/request identity;
late worker results cannot mix locations. No old geometry is relabeled as the
current location. Source verification and bounded class/geometry limits are unchanged.

A new investigation opens Aquifer shape, with **High Plains example** at the top
and the scene before extended controls and record time. Saved view choices remain
respected. The probe starts at the current map center; pointer movement does not
continually replace well records while orbiting the aquifer view. Click, map-center,
and explicit location actions still select records. **Fit recorded depths** lets
the column view show deeper logged intervals outside its initial 0–100 m window.
The aquifer remains a fixed 2022–2024 class-derived envelope, not a historical
water-occupancy reconstruction. Other resource shapes remain subject to source
qualification.

The application-only session/mesh helpers remain in `app/`, regression checks in
`tests/`, and this behavior record in `docs/`, following the responsibility basis
above. No new datasets, source admission, database, credentials, or storage bindings
are introduced. Tests exercise incomplete imagery, failed readback, late results,
movement, teardown, real source meshes at two extents, holes, depth registration,
and desktop/mobile effect containment. These are automated source/runtime-unit
checks, not browser acceptance. The v160 repair session's browser attempt was denied because
its admin-enforced security check was unavailable; visual, touch and device WebGL
acceptance remain unverified. Rollback is the saved v159 application version;
no data or schema rollback is required.

## Immersive cutaway presentation — 2026-10-06

This presentation starts from saved private Site v166, source
`a4d6b3dc69721fbfb270906a9ff3e44dd941d5c0`. The **3D cutaway** label replaces
Aquifer shape while its saved `aquifer` value remains compatible. The single
54 px toolbar is preserved. A full-height charcoal workspace puts the scene
before location forms, record time, source rights, and export controls. The
live, north-up 2D locator is an inset with its original attribution disclosure;
map effects retain the same inset bounds. The inset withdraws while scrolling
to lower controls. Alternate underground displays keep their resizable locator
and panel arrangement.

**Explore this area** focuses the current map center at zoom 12; **High Plains
example** provides the existing western Kansas example. Source-colored record
columns descend from a captured, flat locator plane into a dark inspection
frame. Copper frame edges and metre depth guides describe display extent, not
geology. Columns use a readable screen-space diagram width (not a physical
well diameter), preserve original interval heights, and highlight the picked
record. Projected depth labels retain readable text size as the camera moves.
The caption and camera controls occupy a separate band outside the renderer. Dark space is explicitly unobserved; no continuous layers or cave
geometry are inferred. The current basemap supplies the optional map image.
The compact appearance console exposes independent surface/aquifer opacity,
vertical exaggeration, record visibility, source-range inspection, and refresh.
Camera presets, rotation and zoom have button alternatives. Selecting a log
continues to open its original interval in the Evidence Drawer.

The renderer measures its actual scene container. Camera fitting includes both
plotted log depths and aquifer depths, accounts for mobile aspect ratios, and
updates its near/far planes when resized or vertically rescaled. Record plotting
retains source interval objects and measured units, gaps and overlaps, existing
50-record/400-interval budgets, and the existing aquifer-plus-50-metre / 500-metre
clipping limits. A pure helper in `app/cutaway-model.ts` supplies these bounded
display intervals and camera fitting; tests cover depth-only scenes, invalid or
out-of-extent rows, clipping without source mutation, budgets and extreme camera
fits. This is an application display responsibility under the same Directory
Rules / ADR-0029 basis above, with regressions under `tests/` and the monorepo
mirror under `apps/site/source`.

No ground elevation datum, deviation survey, continuous lithology or qualified
cave model has been introduced. Aquifer geometry remains fixed to 2022–2024;
record-time controls filter eligible records only. Geometry still renders when
an optional surface image fails. No new dataset, admission, external request,
storage key, schema, dependency or binding is introduced. Saved v166 is the
application rollback point. Production and browser validation are recorded by
the delivery review; this authoring record does not claim deployment or browser
acceptance. Older browser-blocked statements above describe their dated sessions.

## Larger selector and fluid camera — 2026-10-07

This update starts from saved private Site v168, source
`c74ca07a33f742eecef5461f13769167df3e1d9d`. The cutaway now places its live
2D selector in a dedicated column beside the 3D scene. Wide desktop map areas
are 352–420 px wide and at least 230 px high; phones use the available width
and a 240 px map height. Full probe coordinates, map-center and zoom actions
remain beside the map. A measured DOM slot positions the existing MapLibre
canvas and effects together and clips them to the workspace while scrolling;
no second map instance is created. Attribution stays available through its
native disclosure. Alternate Underground views retain their existing layout.
The slot conversion includes ancestor scroll offsets, including browser focus
scrolling, so the map remains clipped below the workspace header on phones.

Camera buttons sit above the scene. Short orbit damping and interruptible
preset/rotate/zoom transitions stop when direct manipulation starts. Reduced
motion uses immediate changes. Transitions stop on tab hiding or disposal,
and no permanent rendering loop is introduced. Rotation fits the new viewing
direction and preserves zoom relative to a full fit, preventing the shallow
frame and depth labels from clipping after repeated turns. Opacity, log
visibility and source selection reuse the scene. Vertical scale retains the
viewing direction and zoom while moving the camera with the depth center;
container resizing retains the pose. A record-filter geometry rebuild restores
the pose for the same map extent and retains a picked record if it still has
plotted intervals. Reset, preset selection, or a new locator extent can fit a
new view.
Opening the Evidence Drawer skips the global layout effect's redundant
MapLibre resize when the cutaway canvas dimensions already match. This avoids
MapLibre's synthetic movement events clearing the selected source. Real
dimension changes and locator movement still invalidate old bounds immediately.

The selector distinguishes columns actually plotted within its extent from
loaded records eligible after the record-time filter. The record timeline
explicitly distinguishes its filter from the map's global Time sweep. Neither
changes the fixed 2022–2024 aquifer source period or reconstructs past geology.

`app/cutaway-camera.ts` owns this small application camera controller under the
existing application responsibility root; `tests/cutaway-camera.test.mjs`
covers actual transition timing, interruption, reduced motion, disposal, and
repeated Three.js projection fits. Directory Rules and accepted ADR-0029
remain the placement basis. `app/cutaway-locator.ts` owns the same display's
measured placement and layout-resize guard; focused tests cover scroll clipping,
both drawer resize callbacks and genuine size/extent invalidation in the actual
aquifer session. There are no new data assets, requests, source
roles, dependencies, storage formats, bindings, or acquisition permissions.
Saved v168 is the application rollback point. Build, browser and deployment
results belong to delivery evidence, not this authoring record.

## Direct 3D slice access — 2026-10-07

Starting from private Site v169 / `82c73327119909f9b034976bbf7cfb5f727b6caf`,
**3D slice & materials** replaces the ambiguous material-view tab label while
retaining the saved `3d` display value. The 3D cutaway now offers **Open 3D slice**
above the map/model workspace, alongside a named loaded-source picker. Selecting
a cutaway column retains its record and original interval for this continuation.
Empty, invalid or out-of-window records show a reason rather than an invented
column. Core choices remain explicitly inventory envelopes.

A deliberate slice fits valid recorded depths within the existing 0–12,000 m
window and starts inside an actual interval. A useful existing interior depth is
retained; a picked interval takes priority. Otherwise entry chooses an interval
near the fitted middepth so a thin topsoil does not leave the cut visually at the
surface. Gaps remain gaps, and source intervals are never rewritten. A selected
record change keeps slicing active and fits the new record when needed. Ordinary
tab entry and saved view restoration retain general material browsing without
forcing clipping; slicing itself remains temporary presentation state.

The slice model leads its workspace, before record-time and location controls.
One **Slice depth** slider, metre readout and **Show whole column** control sit
immediately above the model; its amber horizontal outline is a UI cut guide, not
a geological surface. Material above the chosen recorded depth is hidden.
Opacity, slider and slice toggles reuse the renderer and preserve the camera,
including toggling from separated layers. Ray selection ignores clipped hits and
the cut guide; the interval list and Evidence Drawer preserve original source
identity. Inspection no longer moves the cut plane. Depth-window, scale and
original-description controls remain in a named disclosure. **Geographic columns
& section** is a distinct action; this is a one-log diagram, not a regional model.

Placement reuses application helpers, tests and behavior docs under the existing
`app/`, `tests/`, and `docs/` roots and the repository `apps/site/source` mirror,
following the Directory Rules / ADR-0029 responsibility basis above. No source
assets, acquisition, dependency, data admission, binding or saved-schema change is
introduced. Rollback is the saved v169 application; existing data is retained.
Focused callback and Three geometry/lifecycle tests verify the entry, clipping,
source selection and restoration behavior. Browser visual/touch/WebGL acceptance
is separate and remains unavailable during this change because the browser admin
security check could not complete.

In-place whole/slice toggling preserves the current depth-window object,
description filter and useful interior cursor; it never silently refits the
record. If that window/filter contains no drawn interval, **Start 3D slice** is
disabled and **Fit recorded depths** remains an explicit recovery action.
Deliberate **Open 3D slice** transfers focus once to the named slice workspace,
with its controls next in tab order. Restoring a workspace, switching tabs or
records, and adjusting appearance do not trigger this focus transfer.


## Area underlay and record-time navigation — 2026-10-07

This revision starts from owner-private Site v170, source
`54e3f661d3dcede372ef8ae90dee99cd0798e3b9`. A new investigation opens **Area
underlay**. Frame a local Kansas area in the large 2D selector and choose **Show
this area**. Pan and zoom in the selector are previews: the underlay retains its
last applied area and image until another explicit application. The status says
when the preview has moved away from that selected frame. A High Plains example
and keyboard map movement remain available in **Map navigation & example**.
The accepted frame must be flat/north-up Mercator, stopped, inside the existing
Kansas display envelope and no wider or taller than one degree. A moving,
unavailable or out-of-scope frame is held with guidance; it is not substituted
with the old pin or a default probe.

One accepted rectangle drives both the source query and clipped aquifer
geometry. Source loading chooses at most eight intersecting spatial tiles,
verifies their pinned hashes, filters selected sources and the exact rectangle,
then applies the existing atlas-year eligibility gate. Date-held counts describe
that frame's loaded tiles. Duplicate records are removed and ranked
reproducibly by distance to the frame center, then ID/source ID, before the
50-record cap. Unlike the secondary probe workbench, this query has no 25 km
radius around a pin or section. Outside-frame records cannot use its display
budget. Failed/missing tiles, an eight-tile truncation or a 50-record truncation
are reported as partial coverage. A selected frame is therefore a **bounded
loaded subset**, never a claim of exhaustive coverage. The 12-tile cache and
400 drawn-interval budget are retained. The drawing model also filters the
rectangle before its defensive 50-record cap.

Applying a frame cancels record playback and makes old worker results ineligible
immediately. A render-time query identity guard also withholds prior rows and
captured context immediately when the selected sources or atlas year changes,
before the 140 ms request debounce. The next accepted response must belong to
that identity; the debounce cannot expose old rows under new eligibility labels. The parent checks the echoed frame as well as request identity;
the geometry session checks its own response bounds. Imagery remains optional:
it attaches only when the map is stopped, its tiles are complete, and its current
bounds still exactly match the selected frame. Preview movement invalidates a
pending capture and geometry reply. A completed underlay remains labeled as the
selected area while the selector changes. If an unannounced bounds change is
detected during capture, geometry may remain but the image is withheld.

The dominant model retains the oblique flat map, independent record columns and
fixed blue uncertainty ranges. Compact **Orbit**, **Move**, **Reset view** and
zoom buttons sit with the model. Move changes the primary pointer and one-finger
gesture to pan; orbit restores rotation. Keyboard controls and the alternate
camera presets remain available. Appearance, vertical exaggeration, column
visibility and presets move into **View settings**; the legend and provenance
remain in **Aquifer legend & evidence**. Unknown ground stays empty. Camera pose
survives appearance/navigation changes and same-frame record-time membership
changes; a valid picked source remains selected, while a time-filtered-out
source is cleared. If aquifer geometry arrives before the first records, that
first settled record set fits its actual depth once, unless the user has already
manipulated the camera. Later record-time/source changes preserve the view. A
different geographic frame may fit a new view.

**Record time** sits directly below the model. Its final slider position and
select option are explicitly **All loaded records**, distinct from the latest
dated year, so moving to the end can restore loaded undated records. Earlier
positions show cumulative dated records through the selected year. The count
states visible versus loaded records. **Time & sources** contains playback
speed, source filters and the eligibility explanation. Atlas year still applies
first: a historic atlas frame has already withheld later and undated rows;
All loaded records does not bypass that gate. Aquifer ranges remain fixed to
2022–2024 and never animate as past groundwater or changing material. Manual
scrubbing and playback operate on the loaded subset, not a new statewide query.
Reduced motion prevents automatic playback; hidden documents and source,
area and tab changes stop it. The global Time sweep is folded away in the
primary area view when it is not explicitly open. Toolbar **Time** restores it,
and entering/restoring Underground pauses global playback without changing its
committed atlas year.

**Inspect an individual log** is a closed secondary disclosure below the scene.
Selecting a plotted source can still open evidence; **Open selected log** then
continues to the source-specific depth slice. The always-available **Individual
log** tab retains the saved `3d` enum; Area underlay retains `aquifer`. Deliberate
legacy saved `3d` views restore without a forced transition, and Area underlay
provides the return path. Existing custom depth windows, description filters,
original interval identity, source units and focus handoff for deliberate log
entry remain intact. Probe/search/transect workbenches keep their existing
secondary behavior.

The applied frame and 3D camera/image are temporary display state. Workspace
saves retain record IDs, source editions, the existing anchor, record cutoff and
coverage text, with captured rows stripped by the existing settings-only path.
Reports and source-labeled CSV exports can retain their bounded captured rows;
coverage text includes the applied frame, and CSV rows retain source coordinates.
No dedicated applied-rectangle field or surface image is serialized. A workspace
may restore the selector's later preview while its earlier applied frame is not
restored; choose and **Show this area** again before exploring an underlay. Source data assets/hashes, saved schema/storage keys, DB/BUCKET
bindings, privacy/redaction, source-labeled CSV/SVG exports and owner-only
audience are unchanged. There is no source acquisition, interpolation, common
elevation registration or admission change.

Implementation stays in the existing `app/` responsibility, callback/worker/model
regressions in `tests/`, and this explanation in `docs/`, following Directory
Rules and ADR-0029 as above. Tests exercise exact-bound filtering before caps,
frame-local time holds, bounded requests, cancellation and echoed identity,
manual preview/application, stale or mismatched images, compact composition,
explicit All time, real component camera retention and legacy log controls.
The component harness executes hooks and callbacks with real Three geometry and
camera math while substituting the WebGL renderer; it does not certify browser
rendering, touch, layout or accessibility. Browser review remains blocked by the
admin-enforced security check. Build/test success, source publication and visual
acceptance remain separate. Rollback is saved v170 with no storage migration.

### Cutaway interaction repair after v171

The v171 delivery above is historical. Its five-tab navigation and initial
empty stage did not establish user acceptance. The current repair replaces
those with one area-selection workspace and a closed **Other tools** picker.
**Back to cutaway** retains the applied rectangle, surface capture and camera
within the open Underground panel. Inactive cutaways release their worker and
renderer; their source request/geometry state resumes without applying a later
map preview. If an optional aquifer request was interrupted, the retained frame
and independent records remain usable and the status offers another explicit
apply to retry it. Closing the entire panel still discards this temporary scene;
workspace saves and report/export meanings remain as described above.

**Show this area** skips the global 2D animation when the map is already flat.
When normalization or other movement is underway, it retains the user's request
and continues after the map settles; resize events do not silently cancel that
intent. An oversized Kansas frame offers **Zoom in & explore**, which keeps the
current center, narrows the frame and applies it. The High Plains example remains
an explicit choice. Accepted bounds still drive both record and aquifer queries;
a selector preview cannot relabel a selected frame or its image.

Accepting an eligible frame immediately permits independent well/core loading.
The neutral reference plane contains no inferred geology or aquifer envelopes.
Aquifer failure, construction failure or a 14-second timeout leaves those
records usable. Image capture has its own 8-second bound; missing, tainted or
mismatched imagery is labeled as unavailable while recorded columns remain
visible. First settled records can fit the camera before optional aquifer data
arrives. First aquifer settlement can fit separately; either respects prior
user navigation, and later record-time/source changes retain the camera.
Terminal record-worker failure clears records and keeps loading false across
later apply/source/year changes, with a visible close-and-reopen recovery path.

Before applying an area, the workspace shows the larger selector and a compact
instruction, without an empty canvas, camera buttons or disabled timeline. A
settled frame without logs or aquifer ranges shows recovery actions instead of
a blank 3D stage. Once evidence is present, the cutaway offers Orbit, Move, zoom
and adjacent record time. **All** still means all eligible loaded records;
atlas-year source eligibility applies first. This is cumulative record
availability, never simulated material change. Source bounds, uncertainty and
partial coverage remain available in disclosures.

Individual-log appearance/material controls and keyboard interval lists are
closed disclosures (the keyboard list opens on WebGL failure). Section depth
settings and source record lists, survey filters and interpretation limits,
location/source tools, and export controls are also disclosed. Survey and soil
views do not show unrelated record-time or depth controls. Existing display
enums and deliberate legacy saved-view restoration are unchanged.

This repair uses the existing `app/`, `tests/` and `docs/` responsibility roots;
it changes no data assets, dependencies, schemas, storage or audience. The
8-tile request limit, 12-tile cache, 50-record cap, source integrity checks,
privacy/export boundaries and fixed 2022–2024 aquifer period are unchanged.
Rollback is the v171 source commit
`71bfe886b03b05ba142bdeafa1fd479f1f141b00`, without a storage migration.

Callback regressions execute the actual page representation function, including
its 420 ms animation and reduced-motion path, together with the area component
and session. They cover one-click completion, resize/preview identity,
independent records on optional-source failures, oversized-frame recovery,
initial depth fitting, tool round trips and failed record workers. Real Three
geometry and camera calculations are used with a substituted renderer. Browser
visual, touch, device WebGL and full keyboard acceptance remain unverified
because the supported browser interface is blocked by its administrative
security check; these tests do not replace that acceptance.
