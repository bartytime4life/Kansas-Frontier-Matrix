# Water-flow paths and terrain context

## Local rendering repair — 2026-10-05

River trails retain every mapped vertex between their endpoints, rather than
sampling every seven screen pixels and cutting across tight bends. A trailing
segment remains drawable when its arrowhead leaves the viewport. Missing/zero
readings, reduced motion, and illustrative-speed labels remain unchanged.

The 3DHP image layer requests 512-pixel images with a matching renderer tile size,
reducing four image requests to one for an equivalent aligned area at the same
ground pixel resolution. USGS layers 50 and 60 advertise a 1:300,000 minimum
scale; the layer now starts at map zoom 10 and uses the existing zoom guidance
and controls. Both zoom buttons use the selected source minimum. Other sources
retain their tile sizes. No new source, geometry simplification, data activation,
or provider cache freshness claim is introduced.

A local provider probe near Ellsworth compared four concurrent 256-pixel images
with one 512-pixel image over the same area: 1.206 s versus 0.831 s, with valid
PNG dimensions. This single sample demonstrates compatibility, not a sustained
performance guarantee. Provider details: https://3dhp.nationalmap.gov/arcgis/rest/services/usgs_3dhp_all/MapServer?f=pjson

These edits belong to the existing Site application, tests, and documentation
responsibilities. Browser visual acceptance remains unverified because browser
access was rejected by the admin security check. Hosted deployment is separate.
Rollback is the preceding local candidate aa10a86 and its retained build; no
DB/R2 data changes are required.

## Progressive direction loading — 2026-10-05

The selected-gauge map now requests a bounded NDJSON stream from the existing
direction route. The first event contains only a verified path traced from the
1,200 m USGS 3DHP gauge search. It is visibly labeled as a nearby preview while
the same request continues to the 25 km levelpath expansion and 3DEP terrain
samples. The final event replaces the preview with the existing v2 guide and
analysis. Map fitting waits for the final path. A failed or interrupted stream
clears the preview instead of treating it as a complete route; malformed,
out-of-order, and oversized events are rejected. The original JSON route remains
available to existing clients. Neither route changes the provider geometry,
connection rules, 40 km limit, source status, or release authority.

The client keys retrieval to station identity and coordinates rather than the
whole observation bundle, so new readings at the same station do not restart a
geometry request. A completed guide is reused within the same browser page for
15 minutes, for at most 24 stations. This is a display cache, not a governed
release or a new provider observation; it disappears on page reload. Streaming
responses are not stored by HTTP caches.

In a local live-provider timing check at USGS-06864500 on 2026-10-05, the nearby
verified segment arrived in 1.64 s, while the full 40 km path and terrain arrived
in 10.65 s. A preceding unmodified JSON request took 8.70 s, with 1.74 s on
the nearby query, 5.95 s on expansion, and 0.99 s on elevation. These are
sample timings, not a latency guarantee. The longer path still depends on USGS
service time; browser rendering and hosted streaming remain separate checks.

October 4, 2026 UTC: the selected-gauge direction adapter now returns `kfm-3dhp-direction-v2`; the browser retains v1 parsing for compatibility. This change stays within the preserved standalone Site and does not activate or admit governed water data.

The earlier adapter searched within 1,200 m of a gauge, kept the first 20 river features, and discarded individual lines with more than 300 vertices. That excluded detailed reaches and 3DHP waterbody connectors representing much of the Smoky Hill River. The updated adapter finds the nearest explicit downstream line within 1,200 m, then requests the same provider levelpath within 25 km. It follows `dnhydrosequence` to a unique `hydrosequence` and requires adjacent endpoints within 10 m. The line starts at the nearest point on the mapped feature, without drawing a gauge-to-channel connector. The gauge offset is disclosed; matching by proximity is not an authoritative gauge/network association.

Only flowdirection=1 and feature types 1 (river), 4 (surface connector), 5 (waterbody connector), and 6 (elevation breaching connector) are accepted. The returned path stops at missing or ambiguous topology, a geometric gap, a cycle, 40 km, 80 reaches, or 5,000 output vertices. No downhill shortcut or invented channel joins are supplied. Routes containing abstract connectors have a dashed guide and a visible connector count. Their mapped centerlines are not a wetted-channel footprint. The provider definitions are at https://www.usgs.gov/ngp-standards-and-specifications/3d-hydrography-program-3dhpall-flowline.

The fixed upstream requests permit at most 400 features and 4 MiB per hydrography response, 80,000 accepted input vertices, 25 elevation points and 128 KiB of elevation response. The total request has a 35-second deadline and propagates client cancellation. A truncated initial gauge inventory fails rather than claiming the nearest candidate; a limited or failed extension is disclosed. No provider URL is accepted from the client. Successful responses are private-cacheable for one hour. No DB/R2 writes, background job or new external account is introduced.

The 25 samples are equally spaced along geodesic path length. USGS 3DEP `getSamples` uses multipoint EPSG:4326 coordinates, `rasterFunction: None`, bilinear interpolation, and reported vertical datum metadata. Sample identity/location is checked; null, empty and NoData values remain missing. Endpoint fall is start elevation minus end elevation; mean terrain slope is 100 × fall / path distance. These two quantities require valid endpoint values and equal, non-unknown reported datums. The chart breaks at missing samples or datum changes. It reports sample counts, terrain range and provider resolution. Elevation failure preserves the mapped direction and marks terrain values unavailable.

Terrain elevation is not channel-bed bathymetry, river depth, water-surface elevation, hydraulic grade or a velocity model. Provider flow direction remains authoritative for display; terrain rises at dams or from mixed survey sources do not reverse arrows. Existing gauge discharge and timeline provenance are retained.

Canvas trails now extend up to 240 screen pixels (previously 136), with layered shorter highlights. Precomputed cumulative screen distances and binary search replace repeated full-line scans for each trail point. Positive reported gauge discharge enables illustrative motion; zero or missing readings retain still direction guides. Reduced motion and hidden-tab behavior remain respected. Paths and terrain are keyed to the selected station so a previous gauge's geometry is not rendered for a new selection. The zoom action fits the full loaded path.

Validation: live adapter readback at USGS-06864500 (Smoky Hill River at Ellsworth; provider coordinate -98.2336683810657, 38.7266758875074) returned 40,000 m, 30 linked waterbody-connector reaches, 436 vertices, a 7.3 m gauge offset and 25/25 valid terrain samples. Endpoint fall was approximately 13.8 m, mean terrain fall approximately 0.035%. Another central-Kansas sample returned 2.77 km and stopped at missing downstream metadata. These dated checks do not establish statewide completeness or physical flow velocity. Regression coverage checks network gaps/ambiguity/cycles, long geometries, sample identity/NoData/datums, connector disclosure, upstream truncation, elevation-service failure and canvas direction/trail behavior. Rendered-browser acceptance is separate.

## River Pulse coverage and motion repair — 2026-10-04

The network now discovers Kansas USGS stream gauges with discharge reports in the
past 30 days, including recently silent gauges, then requests the selected last
24 hours in batches of 48 (three concurrent groups). The old 72-gauge sampling
limit is replaced by a 512-gauge safety cap and 100,000 returned-observation cap.
Provider next-page flags and missing metadata/series remain disclosed. A full
metadata batch is complete when all explicitly requested IDs have returned,
even when the provider emits a next link at the exact page size. Failed series
batches retain their verified station locations and no invented measurements.
This is not an inventory of every historical or non-USGS gauge.

Missing/null/out-of-tolerance samples use stationary dashed cross markers;
measured zero uses a stationary amber ring and bar. Neither produces downstream
arrows or trails. An all-empty observation window can still display known gauge
locations at the request end time; that cursor is not an invented observation.
Missing-value opacity is preserved through slider updates. Gauges retain exact
source timestamps, qualifiers, and provisional/approved status. Trend comparisons
require matching units and statistic IDs as well as the existing time tolerance.

Rings use staggered phases with eased travel and a smooth fade. Direction follows
provider-mapped geometry at illustrative screen speed; no velocity is derived
from discharge. Motion uses animation frames capped at 30 draws/second and
pauses while hidden, reduced-motion is enabled, or the feed is loading, stale,
or failed. The canvas now follows the River Pulse opacity control.

Validation includes batched retrieval beyond 72 gauges, partial batch failures,
retained silent locations, measured zero, missing/no-arrow drawing, and the full
Site regression suite. A live adapter request loaded 181 gauges and 17,165
observations, with no truncation or partial-response flag; this is a dated check, not a guaranteed live count. Browser/WebGL
visual acceptance remains unavailable because the required preview browser skill
is not available in this session.

## River observatory presentation — 2026-10-04

The River Pulse dock now has a six-part network dial and gauge-condition buttons.
Each category is mutually exclusive: measured zero is separate from rising,
falling, steady and uncompared measurements; missing/stale values remain separate.
Clicking a condition cycles through its station IDs. The dial reports the fraction
with a value at the selected frame, not basin coverage or real-time availability.

The selected-station view emphasizes discharge, source time, quality and the
loaded range. Expand details increases the scrollable dock, and channel/terrain
information remains available in a disclosure. Follow a river collapses the dock,
selects a nearby gauge when needed, and fits the provider route after it arrives;
ordinary station selection does not trigger an unsolicited camera move.

Hydrographs retain unsmoothed, gap-separated source paths and add area shading
only within each valid segment. Pointer inspection and a keyboard/touch range
control select an actual sample, including null values. The readout is explicitly
separate from map time. No value is interpolated across a data gap. Stale frame
values do not receive the active-observation marker.

Mapped motion now uses tapered bands along the path and a selected-gauge beacon.
Projected paths are cached until geometry or camera state changes. Existing
positive-value, missing/zero, provider-failure and reduced-motion gates remain.
Colors are consistent across network categories and gauge symbols: cyan rising,
lavender falling, mint steady, amber measured zero, slate unavailable.

Validation: 376 automated tests, TypeScript and production build pass. The required
control-browser skill is absent from the available skill catalog, so browser
visual acceptance remains unverified; no alternate browser path was used.

## Missing station dots during USGS rate limiting — 2026-10-05

A local network request returned 502; a direct USGS check confirmed HTTP 429
with OVER_RATE_LIMIT. This is independent of the 3DHP image zoom threshold.
The adapter now exposes HTTP 429 and Retry-After and holds further calls within
that worker for the bounded provider cooldown (five minutes by default, up to
one day). Other failures retain their existing handling.

Successful recent-network loads now save only validated station locations in
optional device-local storage. On a failed fresh load, locations captured within
seven days may return as missing-value markers; observations are stripped,
original retrieval time retained, and motion remains stopped. Malformed, future,
expired, or oversized saved data is rejected. There is no bundled synthetic
inventory and no recovery promise for browsers that never saved a successful
load. A provider recovery is still required for fresh readings and animation.

Regression tests cover cooldown request suppression and retained station dots
without values. This does not change source admission or hosted data storage.
Rollback: preceding local source fb6bd1e and its retained build; optional key
`kfm-river-station-locations-v1` may be removed without affecting source data.

## USGS request capacity and local key setup

The same worker now reuses a validated network bundle for 15 minutes, retaining
its original query and retrieval times. Multiple page reloads no longer repeat
statewide acquisition during that interval. A bounded in-memory cache is neither
a new observation nor durable storage. This reduces load but cannot override
an existing provider rate limit or guarantee capacity across worker instances.

Free key registration: https://api.waterdata.usgs.gov/signup/
The local launcher optionally reads `~/.config/kfm/usgs-water-api-key` as an
owner-only regular file (0600), at most 256 bytes, outside the application.
The key is injected into the worker binding `USGS_WATER_API_KEY` and sent only
in the `X-Api-Key` header to fixed USGS URLs. Redirects remain refused. Do not
commit the file, paste its contents into chat, or put it in a request URL.
Restart the local service after saving the emailed key. Hosted secret setup is
separate. Missing keys retain anonymous behavior; invalid files fail startup.
No key has been provisioned or authenticated as part of this change.

## Bidirectional mapped corridor — 2026-10-05

The v3 direction response adds up to 100 km upstream and 100 km downstream
within the existing Kansas-adjacent coordinate bounds. The 100 km radius query
selects the seed's provider levelpath; it is not an entire watershed or all
tributaries. Returned topology, endpoint gaps, cycles, 200 reaches per direction,
5,000 vertices per direction, 400 features per upstream response, 4 MiB per
response, and the 35-second deadline can stop it sooner. Truncated acquisition
is disclosed. V1/v2 parsing remains supported; v3 checks separate distances and
their sum. The response format and progressive network phase are versioned.

Upstream tracing uses uphydrosequence only with reciprocal dnhydrosequence;
without an explicit mainstem it follows only a unique returned incoming reach.
Ambiguity stops the path. All output coordinates remain ordered downstream,
including the part before the gauge. A gauge reading is not propagated as a
measurement at every point along the corridor. Zero/missing readings and stale
feeds retain the existing no-motion rules. Official topology definitions:
https://www.usgs.gov/3d-hydrography-program/3dhp-flow-network-derivatives

Terrain remains 25 samples of the existing USGS 3DEP product, with reported
resolution and datum. No new raw LiDAR dataset is acquired; no assumption is
made that every sample is LiDAR-derived. Terrain does not invent a channel,
reverse provider direction, or establish depth, wetted extent or water velocity.
The profile marks the gauge and reports separate upstream/downstream extents.

Loading emits nearby, network, then terrain-complete events. The extended line
can animate and fit the map before terrain finishes. Cancellation aborts provider
work; malformed or incomplete streams still fail closed. The existing per-page
15-minute/24-station cache remains. Canvas projection caches clipped distance
intervals so zoomed-in rendering skips off-screen particle heads while retaining
visible tails and exact mapped bends.

Live Ellsworth check (USGS-06864500): nearby 1.432 s, 200 km corridor with 5,874
vertices 7.112 s, terrain ready 17.068 s. Both sides reached the 100 km cap.
These are single-run source timings, not browser performance guarantees.
396 automated tests, TypeScript and production build passed before local
installation. Visual/browser acceptance remains blocked by the admin browser
security check. Hosted deployment is separate. Rollback uses local 5e87610 and
its retained build; no DB/R2 changes. Placement reuses existing Site app/tests/
docs responsibilities under the repository's ADR-0029 directory rules.
