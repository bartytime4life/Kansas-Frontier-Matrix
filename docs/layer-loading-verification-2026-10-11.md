# Layer loading and interaction verification — October 11, 2026

## Source and scope

Existing owner-private Explorer: `appgprj_6aa0b1c41bc08191bfd86003920f1631`.
Started from Site v246 source `7f3f89e9b181f213ce3a32080cc1c4cdda672f52`.
Reconciled the patch with v248 source `5c493b9011ffeb35fd6765581c69625bd9222de2`, preserving its tool-entry focus repairs and documentation changes. A final reconciliation with v249 source `439c767eea791cbcaac84912c305e53c9128078d` also retains the immediate tool-opening visibility correction.

Changes are limited to display-read lifecycle, overlay ordering, pointer sampling,
and hydration-safe render-efficiency presentation. Source assets, observation
values, units, dates, admission status, hosting identity, storage bindings, access
settings, request byte limits, concurrency cap, and cache limits are unchanged.

## Reproduced defects and repairs

- An uncached read immediately after awaiting a successful read could join a
  completed job before its finally callback removed it. The new consumer would
  remain pending. Jobs now retire before delivering success or failure.
- Adding one raster to 25 settled overlays caused 26 moveLayer calls. Composition
  now retains the longest already ordered subsequence and moves only displaced
  overlays. The identical test takes one move; repeated composition takes zero.
  The full six-layer permutation test covers 720 starting orders, including
  basemap and custom WebGL layers, without moving either of those layer types.
- Leading-only hover throttling dropped the final pointer event inside its
  80 ms interval. Sampling now coalesces a trailing event, retaining that final
  position. Pointer exit, camera movement, style replacement, and teardown cancel
  pending work. Existing overlap ownership and opacity filtering are retained.
- Embedded Balanced rendering could disagree with server HTML about night-sky
  visibility. Browser efficiency is now published through state after hydration,
  keeping the initial server and browser markup consistent.

## Verification

The production build, TypeScript, whitespace checks, and all 1,113 Node tests
passed before packaging. Tests execute the actual request pool and pointer
callback, cover immediate refresh/retry, cancellation, superseded dates, empty
and partial snapshots, overlapping hits, custom layer order, and raster budgets.
The daylight test double now implements MapLibre's beforeId argument; its original
ordering assertions are retained.

Browser rehearsal used real provider responses with ten selected layers:
Census counties, USGS River Pulse, USGS 3DHP, NASA thermal detections, NIFC reports,
NOAA NWPS gauges, USGS earthquakes, NWS alerts, USGS hillshade, and KDOT roads.
Repeated hillshade toggles retained all ten selections. Zoom and keyboard panning
returned to the ready state. Empty, partial, unavailable, and zoom-held source
states remain visible; ten selected layers does not mean ten populated overlays.

A temporary same-origin diagnostic sampled parent-window requestAnimationFrame
intervals while dispatching 24 arrow-key steps over six seconds. It was removed
from release source and deployment assets. This measures browser frame scheduling,
not GPU draw time or an independently verified map-render FPS.

| Browser workload | Mean interval | 95th percentile | Main-thread long tasks |
| --- | ---: | ---: | ---: |
| Empty diagnostic, no map | 17.29 ms | 16.8 ms | Not collected |
| Development build, five selected layers | 305.30 ms | 1033.4 ms | 9, maximum 712 ms |
| Production build, ten selected layers, 1248 × 1251 iframe | 40.54 ms | 66.7 ms | 0 |
| Production build, ten selected layers, 790 × 461 iframe | 40.27 ms | 66.7 ms | 0 |

The production samples used a visible Chrome page on an NVIDIA RTX 5080, preserved
Balanced embedded rendering, completed all 24 key steps, and kept the map ready.
These are environment-specific samples, not controlled before/after frame-rate
comparisons. The reproducible before/after improvement is 26 versus one overlay
move for the same insertion. Sustained 60 FPS, touch hardware, and all possible
layer combinations remain unverified. Provider availability also remains separate
from renderer health.

A camera-state debounce was explored but removed because it did not improve the
sample. Camera history, source semantics, and navigation timing therefore retain
the current Site behavior. Local checks, production publication, source admission,
and owner acceptance remain separate outcomes.
