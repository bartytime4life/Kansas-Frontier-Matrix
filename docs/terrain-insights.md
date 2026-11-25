# Reading a measured Kansas landscape

`Read this landscape` is part of the existing Terrain & elevation measurement
instrument. It is directly below the three layer selectors, before secondary
status/method copy. Select a cell to open its measured row profile; `View map`
closes the dock while retaining a small, noninteractive source-row chart in the
existing identity badge. No new map panel or external service is introduced.

Ground lenses use the existing worker analyses: Elevation, Horn 3 × 3 Slope in
degrees, and 7 × 7 Local relief in metres. The common map legend changes quantity;
the profile always shows the active layer's unscaled source quantity. Surface
is elevation; Canopy is classified vegetation height above same-survey ground,
not ground plus height. Visual relief never changes the readings.

Low, High, Span, count and Find low / Find high / Steepest describe **drawn
eligible samples in one selected source tile**. Before selection the instrument
explicitly labels a loaded source tile. These are not viewport or statewide
statistics. Steepest is available only for supported Ground derivatives. Anchor
actions select an original source index and explicitly recenter without changing
zoom, pitch or bearing. Lightweight and reduced-motion modes use a static move.

The source-row profile contains at most 96 already-loaded samples. Its line
includes supported source samples beyond display LOD; those source-only dots are
subdued. Keyboard range navigation and linked visible-cell highlights use only
the actual prepared eligibility mask. Real NoData/support gaps split the line;
isolated samples remain visible. Negative source elevations, zero and constant
rows are retained. Unsupported/negative Canopy height stays missing in this
profile, consistent with the solid display. Existing source record browsing
continues to retain its full original data.

Ground distances are approximate ellipsoidal eastward distances along a single
EPSG:3857 row. Native distances use source UTM grid metres. They run from the first
to last sample center, not footprint edges; grid-east is not guaranteed true east.
Each source retains its own vertical reference. There is no cross-survey datum
comparison, smoothing, inference of missing support, or scientific-accuracy claim.

An immutable binding comprises tile key, exact grid object, active quantity,
prepared mask and mask offset. Stale actions cannot select replacement source
bytes under a reused query key. Insights pause for inactive/hidden maps, movement,
zero opacity or preparation/mode mismatch. One memoized scan covers at most 96²
cells of one tile; a source-row change scans at most 96 values. Nothing runs per
animation frame. No acquisition, worker/GPU/storage budget or dependency changes.

Focused verification: `node --test tests/terrain-insights.test.mjs
 tests/kansas-lidar-controls.test.mjs tests/terrain-preparation.test.mjs` covers
mask offsets, LOD curves versus selection, scientific quantities, NoData,
negative/flat values, stale bindings, visibility/movement, static Lightweight
camera actions and unchanged acquisition. Browser/render and hosted identity
verification are separate release checks.
