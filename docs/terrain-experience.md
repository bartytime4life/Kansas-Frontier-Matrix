# Terrain experience refinements — 2026-11-24

The Terrain & elevation card keeps the clean continuous landscape separate from the optional measured cell layer. Base landscape removes both cells and raw points. Ground, Surface and Canopy are direct choices; Fit 3D and Terrain tools remain in the map toolbar. Relief and the existing Kansas 2024 aerial are backdrops for the same location, source values and vertical scale. Advanced lighting, source methods and device budgets remain available in disclosures.

## Framing and acquisition

A steep camera's geographic bounds can include a distant horizon. The cell request now uses a bounded local window at 82% of the unpitched viewport scale, independent of pitch and bearing. Initial terrain framing uses 52° pitch and zoom 14.3. This changes display sampling, never source resolution. The Ground service still returns its validated 96×96 provider-resampled grid.

The inspection camera solves perspective constraints for the footprint's height prism at the target pitch. It fits the measured data, retains altitude clearance above its scaled tops, and preserves the active map's ground-clamp preference. When the context reference lies more than 100 m outside the supported height prism, explicit Fit 3D targets the prism midpoint in one atomic camera move; nearby-reference fits remain animated. Source elevations are not rebased. Display scale is explicitly separate from unscaled readings.

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


The fallback-reference fit changes only the camera target, never cell elevations,
closure geometry, source metadata or registration claims. It uses MapLibre's
public zero-duration camera operation because animated terrain elevation can
replace an explicit height target during easing. Native and base data remain
scientifically separate; this display fit does not align their vertical datums.

### Measurement instrument and truthful empty states — 2026-11-25

The Terrain & elevation dock now presents the three measurement choices as one
compact instrument: **Ground** follows bare earth, **Surface** includes supported
vegetation and structures, and **Canopy height** measures classified vegetation
above same-survey ground. The small cross-section is explicitly illustrative;
it is not a rendered survey, a height scale or evidence of local coverage. The
main map remains the landscape. Base landscape turns cells and raw points off
in one action; relief and aerial backdrops remain available in Display & backdrop.

The full dock and compact layer switch use one status function. Native receipts
with no grid remain available as coverage evidence for the current measurement
mode. Optional raw-point receipts and previous-mode receipts cannot supply cell
coverage. Pending work is separate from final missing support, failures offer
Retry unavailable tiles, and only detail-required results offer native zoom.
Supported partial tiles remain readable; absent cells never receive a click-to-
read invitation. Hidden, inactive, zero-opacity and preparation-failure states
explain why measurements are not drawn. The inspection action is enabled only
for drawn cells, while Base landscape stays independently available.

The visible science note separates visual relief and display sampling from
source metres. Full acquisition dates, vertical references, cache times, source
assets, NoData treatment, derivation limits, raw-point controls, sample navigation
and study downloads remain in the existing disclosures. No acquisition policy,
source arithmetic, cell masks, geometry, camera behavior, resource budget or
provider permissions change in this refinement.

A selected cell is bound to its exact grid object and source tile. A refresh that
replaces that grid retires the reading and typed record draft; it cannot silently
reuse the same row index for replacement source values. Refreshing another tile
retains the unchanged selected grid. These are component/source guarantees,
not field accuracy, provider admission or deployed browser acceptance. This is
an isolated authoring candidate; publication remains on hold.


### Keyboard cross-sections — 2026-11-28

During **Draw a cross-section**, **Add map center to line** places the current
camera center as a browser-local line vertex. **Pan map with arrow keys** moves
focus to the actual map canvas. Use its arrow keys to pan; Enter adds the settled
center and returns focus to the placement action. One reverse Tab reaches
**Finish profile**. Pointer clicks and keyboard placement share the same line,
point count and map rendering; Undo, Clear and cancellation remain available.

The quiet center crosshair is a placement aid, never a height observation.
Repeated consecutive positions and invalid map coordinates leave the line
unchanged with an explanation. Source-profile lines stop at 64 vertices; finish
or undo at that bound. Generic point/area/distance measurements keep their
existing behavior. Finishing pauses placement; Undo can resume that same source
line. Cancel, Clear, saved-workspace restoration and a new generic tool retire
source-profile input, so a retained callback cannot revive it.

Placement reads no provider data and does not sample height. Deliberate panning
retains the normal bounded tile-loading lifecycle. Once finished, the existing
profile samples already loaded source cells: source metres remain unscaled,
missing stations remain gaps, vertical references are not harmonized, and
privacy still denies report/download export. Source accuracy, admission,
publication and physical-device acceptance remain separate from this UI change.

### Phone announcement clearance — 2026-11-28

Temporary status messages sit above the phone's Map layers, Topics, Time, Style
and Science & Labs actions, including the status-row and safe-area clearance.
The shared announcement stays pointer-inert and politely announced; its lifetime
and desktop position are unchanged. This keeps terrain completion feedback
readable while the map navigation remains visible.

The existing built-page terrain journeys check the announcement's actual
rectangles alongside both native profile disclosures. Enter, Space and phone
touches near a summary's edge retain its open/closed behavior, visible keyboard
focus, source metadata and scientific limits. The selected source-cell height,
camera and source-request counts remain unchanged by disclosure input. These
synthetic checks are separate from physical-device, full accessibility, provider
accuracy or deployed acceptance. Publication remains on hold.
