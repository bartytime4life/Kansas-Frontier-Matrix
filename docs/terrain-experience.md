# Terrain experience refinements — 2026-11-24

The Terrain & elevation card keeps the clean continuous landscape separate from the optional measured cell layer. Base landscape removes both cells and raw points. Ground, Surface and Canopy are direct choices; Fit 3D and Terrain tools remain in the map toolbar. Relief and the existing Kansas 2024 aerial are backdrops for the same location, source values and vertical scale. Advanced lighting, source methods and device budgets remain available in disclosures.

## Framing and acquisition

A steep camera's geographic bounds can include a distant horizon. The cell request now uses a bounded local window at 82% of the unpitched viewport scale, independent of pitch and bearing. Initial terrain framing uses 52° pitch and zoom 14.3. This changes display sampling, never source resolution. The Ground service still returns its validated 96×96 provider-resampled grid.

The inspection camera solves perspective constraints for the footprint's height prism at the target pitch. It fits the measured data, retains altitude clearance above its scaled tops, and preserves the active map's elevation/clamp. Source elevations are not rebased. Display scale is explicitly separate from unscaled readings.

Rotating or tilting retains the same source footprint and prepared geometry. Small cumulative pans within the central 65% of the committed query footprint reuse that exact footprint; the lease anchor is never shifted to follow each small pan. Crossing its core boundary, zooming or genuinely resizing the viewport commits a new request. Explicit Refresh and Follow map can release the lease. Obsolete work remains cancelled and the previous footprint stays georeferenced during handoff. Picking pauses during navigation/handoff. Basemap style replacement suspends drawing and reinstalls the validated held study on the same map without renewing source/cache timestamps. Explicit Refresh still bypasses cached delivery. Native detail zoom keeps its preparation status visible.

## Rendering

The color and exact picking-ID attachments share one rasterization. A cached frame is reused only while camera matrix, geometry, selected record, drawing size and relevant appearance remain identical. Every map frame still composites the overlay over the current base. Matrix mutation, resize, projection/context changes and resource disposal invalidate reuse. Opacity changes only require composition. Uniform locations and the hardware point-size limit are read once per program lifetime.

The shared teal–sage–gold height palette has increasing relative luminance; legends and elevation returns use the same stops. Local relief retains its symmetric domain and neutral zero. This changes presentation, not scientific numbers or classifications.

A mocked WebGL regression over 101 identical-camera map frames produced 101 geometry draws before the repair and one afterward, with 101 composites in both cases. This is command-count evidence, not a measured FPS or device-speed claim. Cell/point limits, vertex budgets, no-data masks and source identities remain unchanged.

## Accuracy and practical limits

Ground remains the mixed-resolution, mixed-date USGS 3DEP mosaic. Surface and Canopy require complete same-survey native support; unsupported cells stay missing. A sufficiently small extent can still exceed the native hierarchy budget and require closer zoom. Solid walls close display cells and are not surveyed cliffs or subsurface observations. DEM registration, vertical datum and independent field accuracy are not established by better rendering.

First-time source preparation still depends on dev and upstream providers. A warm public Ground response observed during this work returned headers in about 0.3 seconds; a newly requested detailed footprint needed source preparation before becoming ready. These observations do not establish a universal render or cold-load time. No added service, subscription, secret or hosting purchase is introduced.

The production destination remains the existing GoDaddy app `urdng3v1vk`, branch `a0-hosted-ai-web-20261017`. Source tests and a loopback preview using public data are separate from publication; verify the live `/api/build` digest and browser behavior after Publish.

Renderer contracts: [MapLibre custom layers](https://maplibre.org/maplibre-gl-js/docs/API/interfaces/CustomLayerInterface/) and [Map camera API](https://maplibre.org/maplibre-gl-js/docs/API/classes/Map/). Existing storage/resource design remains in [terrain-hosting-plan.md](terrain-hosting-plan.md).


### Terrain field repair — 2026-11-24

A live navigation profile identified synchronous GL state reads in the custom
cell renderer as a significant CPU cost. The renderer now reads only the actual
draw/read framebuffer and viewport (3 reads per frame, previously 21). MapLibre
6.9.0 marks its managed state dirty after a custom layer; the renderer preserves
its targets and untracked scissor/dither flags explicitly. Resource teardown,
color/ID correspondence, vertex budgets and cache invalidation remain bounded.
A lost context is rejected before state reads, so a null viewport cannot cause
a second exception in the map workspace. This is a state-read reduction, not a
claim of a particular device frame rate.

The independent 24-bit depth attachment now maps the loaded geometry's depth
range before converting the translated projection to Float32. This keeps small
neighboring height steps distinct at landscape camera distances. Original XY/W,
source heights, IDs, eligibility and original camera clipping remain unchanged.
Bounds crossing the camera retain the original projection rather than applying
an unsafe range remap. Precision improves visibility; it does not imply higher
survey accuracy or resolution.

After Fit 3D, a same-scale pan requests a new window with the accepted Mercator
spacing and native source-selection zoom. It no longer substitutes the wider fitted-camera viewport and abruptly
coarsens the grid. Zoom, resize and explicit Follow/Refresh still acquire from
the current viewport. The previous geometry stays at its original coordinates
and cannot supply readings during the handoff; it is never moved to fill gaps.


Native-detail repair (2026-11-25): the actual Explorer map and shared-link restoration now share the
zoom-20 ceiling with the detail action. Previously the action requested zoom
17.5 while MapLibre clamped every request to 16, leaving users at the same
unsupported footprint. Zooming to detail does not require the independent base
DEM to be available. Source layers keep their own resolution/zoom limits;
overzooming the camera does not create finer observations. The compact card
states when selected native cells are absent and only the base is showing.

For grid-only requests, an incomplete hierarchy now finishes its preflight
without downloading or decoding unusable partial LAZ files. Source-read failures
remain `unavailable` and use the existing bounded retry policy; budget limits
remain `detail-required`. Native support, source masks, transfer/record/time
limits and optional raw-point behavior are unchanged. This worker change needs
the existing dev processing actor to receive the updated source separately from
the GoDaddy application build.
