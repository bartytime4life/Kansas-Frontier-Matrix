# Public Explorer frame pacing: test protocol and held acceptance

Status: focused upload correction verified by executable tests; matched full-map
GPU/browser acceptance remains **NEEDS VERIFICATION**. A test result is not a
release, source-admission, preview, deployment, or publication decision.

## Evidence and scope

PR #5157 merged on October 14 at 06:39 UTC, at
`e972d5d780d1c75e5c839797c3689cc650e640bb`. Its automated review completed and
raised two non-rendering findings. Its 14-layer interrupted-navigation samples
(29.25/39.25 FPS) still hold acceptance. The exact 14 selected IDs, camera, and
flow geometry were not retained in its v1 pacing records, so that workload cannot
be claimed reconstructed from those records. The native Chrome 1.42/1.33 FPS
records have unequal canvases/features and remain non-comparable.

The current standalone GoDaddy base is
`40ca2b10c91ae7eed84aeea3906e741bfdddb766`, which merged #5166. Its tree is
`b7a0002b00e05bf712b691feb6e3b2d887c0ffdc`; the locally available #5166 head
`15f3b4523163be899c29f08a447609f2a65ad020` has that identical tree. This source
repair preserves those mobile/Underground/Compare changes. It is not a change
to monorepo main or to the owner-private Sites Explorer.

The linked Drive implementation prompt is historical deployment evidence,
modified October 13. The hosting dashboard's exact current published revision
was not independently retrieved in this session. Fresh anonymous browser
inspection verified the public Explorer and its existing v1 frame diagnostic.
A five-layer continuous-pan run on RTX 5080 at 1280×576 CSS and backing pixels
measured browser/map 59.9895 FPS, map p95 18.9 ms, zero >25 ms intervals, and
unchanged data. A preceding run at 1761×1148 CSS / 2641×1722 backing pixels
measured 43.0736 FPS during interrupted navigation, with 486 visible data
features and unchanged data. These workloads differ and are not a comparative
acceptance pair. Neither measures the 14-layer case or this correction's FPS.

The diagnostic-only baseline commit is 7be342616a0908a6fcfd1fefef187b4b424cf7bf (tree
a10b879099ec5185090e732397f587a413343925). Its water sampler retains the
base's upload behavior. The following correction commit changes only that
sampler and adds its regression test and this protocol.

## Reproduced operation and correction

The actual flowing-water layer's terrain sampler previously returned dirty
for every batch of up to 1,500 vertices, including unchanged, null, and nonfinite
samples. That caused a full instance-buffer `bufferData` on every sampling batch.
The correction compares Float32 height values, uploads only changed buffers,
and independently schedules the remaining sampling work. Switching to 2D clears
the obsolete sample queue and retains the existing all-zero-height reset.

An exact-source before/after test with 60,000 synthetic segments, 60,000 terrain
queries, and 41 render calls records 40 uploads / 115,200,000 bytes before and
one upload / 2,880,000 bytes after. Geometry bytes and per-frame segment counts
are identical. All queries remain; the ribbon shader, instancing count, source
coordinates/direction, gauge cues, feature budgets, and animation cadence are
unchanged. The test uses a mocked GL command sink, not a real GPU. This confirms
redundant transfer elimination; it does **not** identify the dominant cause of
the earlier 2D FPS results or prove a 60 FPS improvement.

Run the upload test directly (direct execution retains individual TAP results
in restricted runtimes):

```sh
node tests/water-flow-upload.test.mjs
# Optional exact-source comparison: provide a separate baseline checkout.
KFM_FLOW_BASELINE=/absolute/path/to/baseline node tests/water-flow-upload.test.mjs
```

## Reproducible browser protocol

1. Use separate disposable source checkouts. Record the exact published source
   SHA from read-only hosting evidence, the candidate SHA, and dependency versions.
   Serve production builds, not Vite development builds. Do not change hosting,
   DNS, private stores, source admission, or capture configuration. For a local
   published-source replay, label it as a replay rather than hosted acceptance.
2. Use the same diagnostic code on both source variants. This PR separates the
   diagnostic-only commit from the upload correction, so the diagnostic parent
   and correction child provide a controlled operation comparison. To compare
   the actual published composition, apply only the diagnostic changes to an
   isolated checkout of its verified source revision. Existing hosted v1 records
   lack required identity and cannot be upgraded by inventing missing fields.
3. One foreground test map at a time, the same browser/GPU, 1280×720 browser
   viewport and 1280×576 map CSS viewport. Verify backing canvas pixels and
   device ratio too. Choose the same explicit quality; keep reduced-motion and
   ambient-motion preferences identical. Leave other test maps closed.
4. Pin camera to longitude -98.38, latitude 38.48, zoom 10.5, bearing 0, pitch 0;
   north-up Mercator. Record the basemap, year, exact temporal query, selected IDs,
   opacity, all scene effects, and source states. For the proposed reproducible
   public-14 scenario, use the `streets` basemap (detailed roads), 2026 present
   context, Balanced quality, default source opacities, and the existing default
   scene settings with flowing water enabled. Freeze these 14 verified catalog IDs:
   `census-counties`, `usgs-streamflow`, `noaa-nwps-gauges`,
   `usgs-3dhp-hydrography`, `usgs-wbd-watersheds`, `usgs-earthquakes`,
   `noaa-hms-smoke`, `nasa-firms-active-fire`, `nasa-gibs-fire-points`,
   `nifc-fire-reports`, `nws-alerts`, `blm-plss-townships`, `blm-plss-sections`,
   and `blm-plss-intersected`. This is a newly specified workload, not a claim
   to reconstruct #5157's unknown list. A count of 14 alone is insufficient.
   Keep provider-declared empty coverage truthful; partial/unavailable coverage
   holds acceptance. Add a separate Terrain 3D scenario at pitch 45 with the
   same source/selection settings, terrain source, and 1× exaggeration for this fix.
5. Keep flowing water on, with the same ready 3DHP cells and gauge observations.
   Use the same provider responses/source dates on both variants. A bounded,
   read-only local replay may retain provider bytes and attribution, but is
   context material, not a KFM released dataset. Do not substitute synthetic
   data for the real-map acceptance scenario. Do not hide selected layers,
   lower fidelity, change source values, or disable features to reach the target.
6. Open `?frameCheck=1`, wait until selected source states, tiles, and terrain
   sampling are ready, then run continuous and interrupted samples separately.
   Each lasts 12 seconds. Interrupted input is exactly 48 right/down/left/up
   commands at 250 ms spacing, starting at time zero. The original camera is
   restored after completion or cancellation. Idle is an additional diagnostic,
   not a 60 FPS navigation test: ambient water intentionally redraws near 30 FPS.
7. Download each v2 record. It includes camera, selection/time/effects, visible
   layer/filter/layout identity, source and rendered-feature digests, custom
   flowline geometry/direction and gauge-cue digest, flow segment count, browser
   and canvas dimensions, renderer, readiness, focus, timing, and data stability.
   Downloads are local and explicit; no diagnostic telemetry is transmitted.
8. Alternate baseline/candidate order for at least three warm pairs per scenario.
   Record cold-loading separately. Preserve all runs and screenshots of layers,
   attribution, scene settings, and the visible map. Verify visual parity, keyboard
   controls, reduced-motion behavior, and attribution separately from frame rates.

```sh
node scripts/compare-frame-pacing.mjs published.json candidate.json
```

The comparison returns `INCONCLUSIVE` and exits nonzero for legacy/incomplete
records, unequal workloads, changed data or controls, incomplete 48-command
input, a duration outside 11.9–12.5 seconds, unready sources/tiles, or interrupted
foreground focus. Ready equivalent pairs return `HOLD` if candidate browser or
map FPS is below 58.8, p95 exceeds 20 ms, or more than 1% of intervals exceed
25 ms. The 2% FPS tolerance accounts for sample-edge frames and timer rounding;
it does not redefine the 60 FPS target. Passing one pair is not overall acceptance:
all three pairs and separate parity/accessibility checks remain required.

Full style paint/shader visual equivalence and network delivery are not proved
by the comparator. Source signatures include source definitions and GeoJSON,
plus custom-flow provider geometry/cues; external raster/vector tile bytes are
not hashed by this browser diagnostic. Use one frozen tile snapshot or a verified
immutable provider edition for strict delivery equivalence and document its
identity. Live-provider changes or unverifiable tile identity hold acceptance.

## Placement, validation, limits, and rollback

The supplied reference set has no `Directory Rules.pdf`. The accepted canonical
`docs/doctrine/directory-rules.md` (blob `fd49a0b83e55cef52c1124281f093e263526898d`)
and accepted ADR-0029 were read; they explicitly supersede that PDF and keep one
human-authoritative doctrine home. In this existing standalone application,
`app/` owns renderer/display diagnostics, `tests/` owns executable validation,
`scripts/` provides the thin comparator entrypoint, and `docs/` owns this protocol.
No root, source registry, contract, policy, release, or proof authority is added.

Final source validation: production build and TypeScript passed; 42 focused
checks passed across upload, workload comparison, source signatures, geometry,
flow synchronization and mapped canvas trails. Changed-area lint: zero errors,
41 inherited page warnings. The comparator rejects both prior native Chrome
records as INCONCLUSIVE because they lack workload identity. No other check is
called passing.

Candidate HTTP/browser serving is blocked in this session: a fresh local TCP
listener returned `EPERM`. Repository build/types/unit evidence is therefore
separate from candidate browser, hosted preview, and production acceptance.
The actual candidate 14-layer matched GPU runs, changed-area visual/browser
acceptance, and full provider/tile equivalence remain unrun. No full-suite pass,
security clearance, independent approval, or deployment is claimed.

Revert the performance-correction commit to retain diagnostics with prior water
rendering behavior; revert the diagnostic commit too to return to the exact base.
No database migration, configuration change, source promotion, or production
rollback operation is part of this PR. The remaining bottleneck may be GPU draw
cost, terrain queries, navigation/tile work, or other animations; profile those
under the pinned workload before making another optimization.

Sources: [#5157](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/5157),
[#5166](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/5166),
[implementation record](https://docs.google.com/document/d/18cMIBCuaK3Tp68ER5AqbyFCXte6EpcuioTH7sTPe4sw/edit).
