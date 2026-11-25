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
