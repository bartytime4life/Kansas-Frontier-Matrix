# Flowing water — zoom-adaptive repository candidate

A scene effect that animates rivers and streams in the direction the provider
says they flow, draped on the terrain in Terrain 3D and drawn flat on 2D,
tilted and globe maps. Where a USGS stream gauge has a current reading, the
reach it sits on is lit by that reading. It is **presentation only**: nothing
is queryable, reported, exported or stored, and no evidence state, time or
report value changes. Turn it on with **Flowing water** in the Scene panel, or
choose the **Cinematic** or **Natural** look; it starts with a statewide river overview and adds nearby regional and local detail as you zoom in.

<p align="center">
  <img src="images/water-flow-terrain-2026-10-10.jpg" alt="Terrain 3D at dusk over the Flint Hills: a luminous network of streams draped in the valleys, with ridges hiding the channels behind them. Two synthetic test gauges are labelled HARNESS." width="100%" />
</p>

<sub>**Test harness, not provider data.** The sandbox that built this change
cannot reach USGS 3DHP or the USGS Water Data API, so these renders use a
stream network derived from the Mapzen terrain DEM (D8 flow on a filled grid)
in place of 3DHP, and two synthetic gauges labelled HARNESS in place of USGS
readings. The renderer, shaders and data rules are the shipped code; only the
inputs differ. See [Validation](#validation).</sub>

## What moves, and why

| Rule | What the Site does |
|---|---|
| **Direction only where the provider gives it** | Flowlines come from USGS 3D Hydrography Program (3DHP) layer 50. Only reaches with the provider's explicit downstream flag (`flowdirection = 1`, flow follows digitized order) are fetched, and only streams and connectors (`featuretype` 1, 4, 5, 6). The Site never infers direction from elevation, names or shape. Reaches without the flag are not drawn. |
| **One display speed** | Every reach moves at the same on-screen rate (34 CSS px/s). Motion is a direction cue, not water velocity, and is never scaled by discharge. |
| **Measurements stay on the gauged reach** | A USGS streamflow gauge within 250 m of a mapped reach styles that reach only, fading out over 2.5 km either side of the gauge. Discharge is never painted onto ungauged reaches, upstream or downstream. |
| **What a reading changes** | A measured value widens the gauged stretch, adds a soft halo, brightens the streaks with the reading's relative magnitude and tints them by trend (rising: bright cyan; steady: sky blue; falling: deeper blue). A **measured zero** stills the water: the stretch turns slate grey with fixed bank highlights and no streaks. **Missing or stale** readings change nothing. |
| **Time follows the atlas** | Gauge styling reads the same streamflow frame as the gauge points, so it follows the time slider and playback. When the gauge layer is hidden, readings add nothing. |

<p align="center">
  <img src="images/water-flow-gauge-measured-2026-10-10.jpg" alt="Terrain 3D at night: a synthetic gauge labelled HARNESS synthetic gauge A on a meandering channel, the stretch around it wider and brighter cyan with a halo." width="49%" />
  <img src="images/water-flow-gauge-zero-2026-10-10.jpg" alt="Terrain 3D at night: a synthetic gauge labelled HARNESS synthetic gauge B reading zero; the stretch beside it is slate grey and still while the rest of the network flows blue." width="49%" />
</p>

<sub>Left: a measured, rising reading lights its own stretch. Right: a measured
zero stills its stretch (slate grey) while ungauged reaches keep their
direction-only motion. Both gauges and the network are test harness inputs.</sub>

## Sources

| Source | Used for | Notes |
|---|---|---|
| [USGS 3DHP](https://www.usgs.gov/3d-hydrography-program), `usgs_3dhp_all/MapServer/50` | Reach geometry and downstream flag | Fetched through the new `GET /api/hydrology/flowlines?cell=west,south` route, fixed Kansas overview (2°), regional (1°) or local (0.25°) cells, at most 400 reaches per cell. Uses provider `streamorder` for overview selection. Vertex order, and so direction, is kept. Private cache 1 hour. |
| USGS Water Data API, continuous discharge (00060) | Gauge readings | Reuses the Site's existing `usgs-streamflow` official-context frame (value, relative magnitude, trend, reading state). No new request. |
| Mapzen terrain DEM (existing) | Draping | Reach vertices sample the loaded terrain so rivers sit in their valleys; hills in front hide them. |

NOAA NWPS forecasts and National Water Model streamflow are not used for
motion: they are forecasts or modelled values, and the governance rules keep
modelled discharge off ungauged reaches.

## How it works

- **Route.** `app/api/hydrology/flowlines/route.ts` accepts exactly one
  `cell` parameter identifying one fixed Kansas grid cell (anything else is a 400),
  queries 3DHP with `flowdirection=1 AND featuretype IN (1,4,5,6)` and the fixed
  order threshold for that tier, bounds the response at 6 MB and 80,000 vertices,
  rounds coordinates to 1e-5° and returns
  `kfm-3dhp-flowlines-v2` with its exact request key with `evidenceRole: EXTERNAL_CONTEXT_ONLY`, a
  `truncated` flag and the limitation text. Provider failure is a 503.
- **Cells.** The view requests eight overview cells covering the full Kansas envelope;
  from zoom 6.5 it adds up to nine nearest intersecting 1° regional cells, and
  from zoom 8.5 adds up to nine local cells nearest the map centre
  (within ±0.4° longitude and ±0.3° latitude). At most nine requests run at once. Results are kept in a
  per-map cache of 36 cells; a failed cell waits 60 s before retrying. Cell
  completions and gauge updates share one geometry update on the next display
  frame. A ready cell can appear while the others are still loading. Cancelled
  responses cannot replace a newer request for the same cell. Switching off
  cancels queued geometry work; removing the map also aborts requests and
  detaches the synchronizer's listeners.
- **Geometry.** `app/water-flow-motion.ts` turns reaches into segments
  carrying distance along the reach (so streaks run continuously across
  vertices), gauge intensity, a moving/still flag, a trend tint a stable
  phase per reach and a minimum display zoom derived from provider order.
  Reaches are deduplicated by provider ID across grids; finer loaded geometry
  wins, and higher provider order gets the fixed 60,000-segment budget first.
- **Rendering.** `app/water-flow-layer.ts` is one MapLibre custom WebGL2
  layer (`scene-water-flow`) with depth testing against the terrain. Each
  segment is an instanced, screen-space ribbon shaded as a lit tube: bright
  crown, streaks with a bright head leading downstream, a finer ripple layer
  and a moving glint. Terrain heights are sampled up to 1,500 vertices per
  frame, nearest the camera first, and refreshed when the camera settles or
  the DEM loads; ribbons sit 4 m (× exaggeration) above the surface. Palettes
  follow the scene light: deep blue with white streaks by day, luminous cyan
  at dusk and night. The globe uses MapLibre's globe projection prelude.
- **Placement.** The layer sits above the basemap and below labels and data
  overlays, so gauges, labels and selections stay on top.
- **Animation.** Ambient motion runs at about 30 fps only while flowing water
  is visible and the runtime is ready. Battery saver hides the layer; reduced
  motion holds the water still (direction stays readable from the streak
  heads).
- **Status.** The Scene panel switch shows a live reading, for example
  "120 reaches with a USGS flow direction · 1 lit by a gauge reading", or
  "Zoom to 4 or closer", "No mapped flow direction in view" and
  "unavailable" when the provider cannot be reached.

## Boundaries and limits

- Motion shows mapped channel direction. It is not water velocity, wet
  channel extent, depth or flood level. A dry channel with a direction flag
  still animates unless a gauge on it reads zero.
- Ribbon width is a bounded screen-space presentation choice, not measured
  channel width or discharge. Provider order chooses visibility, not physical width.
  Missing or invalid order stays local-only; it never becomes an overview river.
- Each cell returns at most 400 reaches, ordered by `hydrosequence`
  descending as in the existing `api/hydrology/direction` route. A truncated
  cell is reported as "some areas incomplete" in the reading.
- Canals, pipelines, lakes and reaches without a downstream flag are not
  drawn.
- A gauge more than 250 m from any mapped reach styles nothing.

## Validation

### Original 2026-10-10 results (historical)

| Check | Result |
|---|---|
| Production build | PASS |
| TypeScript (`tsc --noEmit`) | PASS |
| Node test suite (`npm test`) | 939 tests: 937 pass, 0 fail, 2 skipped (existing Qwen installer tests that refuse root) |
| New `tests/water-flow-motion.test.mjs` | 9/9 pass: cell parsing and grid, cells for a view, strict payload parsing, gauge cues (missing, stale, zero, measured, trend), gauge snapping and falloff, geometry (continuous distance, dedupe, cue only on the gauged reach) |
| New `tests/water-flow-sync.test.mjs` | 4/4 pass: off makes no requests, zoom gate, placement below labels, gauge lighting, cache reuse, hidden gauge layer, failure state and retry wait, abort on switch-off, add failure isolated |
| Updated `tests/cinematic-scene-effects.test.mjs`, `tests/scene-studio.test.mjs` | New `waterFlow` key, looks, and the 33 ms motion tick |
| ESLint | 0 errors; new files 0 warnings |
| `smoke-local.sh` | New route listed; missing and off-grid cells return 400 |
| `make repository-topology` | PASS, 0 new drift |
| Rendered checks (headless Chromium, SwiftShader WebGL, live Mapzen DEM, harness inputs) | Terrain 3D at dusk and night: rivers drape in valleys and hide behind ridges; motion confirmed by frame differencing (about 78 % of river pixels change between frames 700 ms apart); measured gauge lights its stretch; zero gauge stills its stretch; no page or shader errors. |

**Harness disclosure.** The rendered checks used Playwright request
interception to serve, in place of the two providers the sandbox cannot reach:

- a 401-reach network derived from the Mapzen terrarium z12 DEM around the
  Cottonwood River (epsilon priority-flood fill, D8 flow, downstream vertex
  order); its main stem drains east, as the real river does;
- two synthetic gauges named "HARNESS synthetic gauge A/B" (a rising
  measured value and a measured zero).

Neither input ships with the Site. The flowline route itself was exercised
only through its 400 paths; its 3DHP response handling is covered by unit
tests over fixtures.

## Not covered

- Live USGS 3DHP and USGS gauge data were not seen rendered (blocked by the
  sandbox network policy).
- The standard light basemaps were unreachable, so renders use the offline
  Midnight style; the clear-sky palette was not seen rendered.
- Real GPU performance on phones and laptops.
- Saving, deploying or mirroring this source to the Site project.

### Frame-batching follow-up — 2026-10-10

The initial validation table above describes the original implementation, not
the subsequent Site delivery. A follow-up starts from Site v214 source
`11f1c546d56dcaec08454f99130350ce536328a2` and repository
`033f8466c28e7de32fcac95c441fa9f8cbeade2d`.

A deterministic synthetic Kansas view at zoom 11, centred at −97.2°, 38.1°,
delivers nine cells (1,800 reaches, 27,000 final segments) and gauge callbacks
before one display frame. Previously this rebuilt geometry nine times and
submitted 135,000 cumulative segments. It now builds once and submits 27,000:
80% less repeated geometry work. The test compares the entire final geometry,
including coordinates, downstream distance, gauge cues and terrain vertex
slots, against the unchanged geometry builder.

Five alternating Node trials on the same PC measured median completion work
of 62.97 ms before and 31.96 ms after. This is a synthetic scheduler/geometry
measurement, **not browser FPS, GPU time, provider latency or a general map-load
benchmark**. Timing is reported, not used as a flaky test threshold. The stable
acceptance checks are one update and byte-identical geometry.

The regressions also cover first-cell progressive display, truncated coverage,
failed cells, delayed responses after off/on, and removal with queued work.
The old code fails the burst, stale-success and teardown cases. Source requests,
cache limits, geometry simplification, gauge scope and motion speed are unchanged.
No new data is acquired or approved by these deterministic tests.

Executed follow-up checks: 26 focused tests and the full 990-test Site suite
passed with no failures or skips; TypeScript, the production build and focused
ESLint also passed. A separate browser smoke on the isolated local candidate
rendered Kansas hydrography around 38.48° N, 98.4° W. Its panel reported 2,311
directed reaches, one gauge cue and incomplete coverage, with no observed
console errors. Browser-control calls were sometimes slow during startup;
this is not a sustained responsiveness, mobile-device or hosted-browser pass.
Publication and repository review are recorded separately in delivery receipts.


## Zoom levels and source evidence — 2026-10-15 UTC

**CONFIRMED:** the existing [USGS 3DHP layer 50 metadata](https://3dhp.nationalmap.gov/arcgis/rest/services/usgs_3dhp_all/MapServer/50)
exposes `streamorder`, `flowdirection`, provider identity and network fields.
The earlier statement that this response provided no stream order described the
old route's selected fields; it is not a current limitation of the service schema.
The route now requests `streamorder` explicitly and independently checks it after
provider filtering. These thresholds are **cartographic choices**, not a new
hydrologic ranking, discharge estimate, wet-channel claim or activation decision.
Live query results and actual Kansas coverage remain **NEEDS VERIFICATION**:
the metadata was readable, but this session could not retrieve the live query.

| Selection | Fetch begins | Smooth opacity ramp | Provider filter | Simplification offset in output degrees |
|---|---:|---:|---|---:|
| Statewide overview, eight 2° cells clipped to Kansas envelope | 4 | 4–5 | order 5+ | 0.001 (about 110 m north/south) |
| Nearby regional, at most nine 1° cells | 6.5 | 7–8 | order 3+ | 0.0005 (about 55 m north/south) |
| Nearby local, at most nine 0.25° cells | 8.5 | 9–10 for lower/unknown order | existing directed stream/connector filter | 0.0002 (about 22 m north/south) |

Higher-order reaches remain visible as finer detail arrives. The GPU interpolates
opacity at fractional zoom without rebuilding geometry; request/geometry updates
remain tied to settled views and batched display frames. The half-pixel zoom lead
allows prefetching but cannot hide arbitrary provider latency. The overview stays
as a backing network while detail loads, fails or retires on zoom-out. Fine/coarse
geometry can differ within the provider simplification tolerance; native visual
acceptance is still required. No straight connectors bridge source gaps.

At most 26 cells are wanted, nine requests are in flight, 36 cells are cached,
and 60,000 segments are drawn (3,120,000 instance bytes at 13 float32 values per
segment). Each response retains the 6 MB/400-reach/80,000-vertex bounds; a full
400-record response is conservatively reported incomplete even without a provider
transfer-limit flag. Ordering is not discharge. Sparse order values, omitted
connectors, failed cells and truncation can leave gaps, which are not filled by
inference. Regional/local detail is a nearest-cell selection, not full-view
coverage. Gauge snapping/falloff, measured zero, stale/missing readings, attribution,
reduced motion and Battery saver retain their existing rules. Conservative
  per-reach bounding boxes avoid exact gauge snaps against distant overview
  geometry; the final 250 m nearest-segment rule is unchanged. No new source,
source registry, data store, approval, release or publication state is introduced.

The API's v2 response adds the request identity and nullable order. The parser
still accepts v1 local responses conservatively (unknown order/local visibility),
and original `?cell=west,south` URLs still work. This is application-local display
metadata, not a second canonical hydrology schema.

### Earlier standalone work and repository boundary

The final overlap check found standalone candidates
`codex/statewide-water-effects-20261014@fc8d36a82349347712506bddea25b94499721842`
and `codex/local-statewide-water-effects-20261014@2c8d7fd7136e3b65b2371b0fbf3b1cc077558c5f`.
Their root-level `app/water-flow-motion.ts` already requests provider order and
uses order 6/4 profiles; their synchronizer selects one tier at zoom boundaries.
GitHub reports no common ancestor with this monorepo main. Another standalone
branch, `codex/godaddy-water-flow-pacing@d9b456a87b0b0bf1482d121f2f808748c4b569dc`,
still has the zoom-10 gate. No open PR was returned by the current PR collection.

This main-based candidate preserves the repository's existing application lane
and adds persistent backing geometry, per-reach opacity ramps, a bounded request
queue and exact-snap screening. Its 5/3 thresholds and fixed-grid request-key
format are explicit cartographic/API choices, not a claim of equivalence with
the standalone candidates. Those branches are preserved. Reconciliation with
any owner-private Site source is a separate review before synchronization;
this candidate does not bulk-import, supersede or publish their source.

### Candidate validation and limits

The isolated baseline reproduces the exact GitHub main tree
`d28785c8d6c5a9fa1ea965cbf0b9c0e59bc615ae` at
`9620b21bca3a3da2fd49a5edda05d8a60a842c47`. These results describe repository
implementation only, not the owner-private Site or GoDaddy delivery.

- Focused geometry, route, scheduler, GPU-call, accessibility and scene checks:
  **54 PASS**. The legacy nine-cell burst/gauge tests isolate local planning;
  new integration cases exercise the actual three-grid planner, queue and zooms.
- A deterministic 26-cell burst makes one geometry submission on the next display
  frame, never exceeds nine in-flight requests, deduplicates shared provider IDs,
  and keeps the overview across zoom-out/in without refetching cached detail.
- The renderer-call regression makes one instance-buffer upload across 60 flat-map
  fractional zoom frames; reduced motion holds the clock still. This proves
  avoided upload work, **not browser FPS, actual shader compilation or GPU time**.
- Production build, TypeScript and changed-source ESLint: **PASS**.
- Full 197-file Site suite, executed one Node process per file with four-way
  concurrency after building each tree: candidate **1,355 tests: 1,293 pass,
  38 fail, 24 cancelled, 0 skipped**; exact base **1,347 tests: 1,285 pass,
  38 fail, 24 cancelled, 0 skipped**. The nine nonpassing file outcomes and
  per-file counts match exactly (`api-connections-storage`, `daily-archive`,
  `earth-engine-context-worker`, `intake-worker`, `local-qwen-bridge`,
  `local-worker-runtime`, `qwen-local-eval`, `subsurface-assets`,
  `underground-resources`). Socket `listen EPERM` and pending event-loop failures
  prevent a full-suite PASS in this sandbox. All eight added tests pass.
- `make repository-topology`: **NOT PASS** because the default Python lacks
  PyYAML and pytest. Its diagnostic subcommand reports 0 invariant violations,
  0 new drift and 93 baselined warnings; that is not an aggregate check pass.
- Desktop/mobile native rendering: **BLOCKED / NOT ACCEPTED**. No browser surface
  was available; a local HTTP listener failed with `listen EPERM`. A direct Node
  `vinext start` also cannot load the Cloudflare build's `cloudflare:` import;
  it is not the supported local Worker launcher. No local store was attached.
- Live stream-order queries, provider completeness, sustained 60 FPS, real mobile
  hardware, terrain/globe seams and full keyboard/screen-reader acceptance remain
  **NEEDS VERIFICATION**. Mock inputs exercise semantics; they do not activate or
  certify a provider.

Reproduce from `apps/site/source/` after the normal pinned dependency install:

```sh
npm run build
node_modules/.bin/tsc --noEmit
node_modules/.bin/eslint app/water-flow-motion.ts app/water-flow-sync.ts app/water-flow-layer.ts app/scene-effects.ts app/api/hydrology/flowlines/route.ts
node --test tests/water-flow-motion.test.mjs tests/water-flow-sync.test.mjs tests/scene-studio.test.mjs tests/cinematic-scene-effects.test.mjs
```

This session used `--experimental-test-isolation=none` for the four focused files
because the sandbox refused the normal runner's child communication sockets.
Application docs and tests stay in their existing `apps/` responsibility lane,
per Directory Rules v2 §5/§10 and accepted ADR-0029. No path or lifecycle migration
is needed. Publication, deployment, source activation and independent review are
separate holds.

## Rollback

Switch **Flowing water** off, or choose **Plain**. It is off by default, so
existing preferences are unchanged. To remove it entirely, revert the commit;
no stored data, schema, URL or saved-workspace format is affected.
