# KFM Reddit Elevation API / Corridor Surface Profile Use-Case Intake

- **Date:** 2026-09-14
- **Input:** [Reddit r/LiDAR — “API for elevation data?”](https://www.reddit.com/r/LiDAR/comments/16jnu4k/api_for_elevation_data/)
- **Disposition:** `DISCOVERY_SIGNAL_RETAINED / FEATURE_REQUIREMENTS / NOT_A_SOURCE / HOLD / VALIDATED_BRANCH_ONLY`
- **Scope:** documentation and offline design only
- **Target repository:** `bartytime4life/Kansas-Frontier-Matrix`

> This record incorporates a community problem statement into KFM's governed terrain architecture. It does not treat Reddit, a commenter, or an unverified service suggestion as a data source, engineering authority, endorsement, benchmark, or evidence of fitness.

## Executive decision

Retain the thread as a useful **use-case and failure-mode seed** for a proposed `CorridorSurfaceProfile` capability. The thread describes a real planning need: obtain elevations at regular intervals along a point-to-point path and include possible buildings and trees when considering wireless Fresnel-zone clearance. It also exposes the consequences of stale, incomplete, or ground-only data.

Do not turn the thread into a source connector. KFM should continue to prefer exact, publisher-verifiable USGS 3DEP products for authoritative Kansas terrain work; use LiDAR Atlas only as a discovery or separately governed processing candidate; treat GPXZ as a commercial derived elevation carrier; and keep Google Elevation, May Mobility vehicle LiDAR, and ICESat-2 in their narrower roles.

The proposed capability must keep four things separate:

1. ground/terrain elevation;
2. top-surface or obstruction-candidate elevation;
3. line-of-sight and Fresnel modeling assumptions; and
4. a human or engineering decision.

KFM may display planning context. It must not label a path “clear,” “buildable,” “surveyed,” or suitable for deployment unless a separately authorized engineering workflow establishes that conclusion.

## What the community thread contributes

The thread's original poster describes an application that samples Google Elevation along a straight path, wants LiDAR-derived maximum surface elevations that include buildings and trees, and uses the result to reduce manual Google Earth review for point-to-point wireless planning. The discussion also raises CONUS coverage, storage and compute cost, DSM versus DTM, project/tile discovery, raster sampling, ICESat-2 coverage, and the business impact of stale surface data.

These are valuable requirements and risk signals, but they remain self-reported community statements. They do not establish:

- that any mentioned API is authoritative, licensed for KFM, accurate, current, available, or suitable;
- that a DSM cell is a verified building, tree, tower, or obstruction;
- that a maximum raster value is robust or represents the relevant path clearance;
- that ground elevation plus a fixed margin is a safe substitute for missing surface data;
- that ICESat-2 provides continuous local corridor coverage; or
- that an automated profile can replace site inspection, survey, propagation analysis, or engineering review.

## Source-authority classification

| Item | KFM role | Allowed use now | Boundary |
|---|---|---|---|
| Reddit thread | Community discovery signal | Requirements, terminology, failure cases, offline test design | Not a source, contract, endorsement, benchmark, or technical authority |
| USGS 3DEP / LiDAR Explorer | Preferred official terrain and source-data family for Kansas | Verify exact project/product metadata; design bounded fixtures | Exact product, work unit, dates, quality, CRS/datum, units, rights, and bytes still require admission |
| LiDAR Atlas | Discovery broker; possible managed-processing vendor | Compare candidate coverage and product offerings after authorization | Must cross-check upstream publisher; commissioned DSM/DTM/nDSM remains derived and separately governed |
| GPXZ | Commercial derived elevation carrier and aggregator | Candidate for server-side point/profile comparison after authorization | Not primary terrain truth; source IDs, EGM2008 reference, terms, caching, cost, privacy, and fitness remain gates |
| Google Elevation API | Licensed point/path elevation service | Product comparison and fallback research | Not documented as a LiDAR DSM obstruction source; current storage/display/attribution terms govern use |
| May Mobility Fleet API LiDAR | Restricted partner vehicle telemetry | Separately authorized mobile-reality-capture research | Not public Kansas terrain, not a general elevation API, and not map-ready without pose/frame/calibration closure |
| ICESat-2 | Along-track laser-altimetry science/reference candidate | Independent scientific context where track support is explicit | Sparse tracks are not a continuous local DSM or default corridor-obstruction surface |

## Required semantic separation

| Object | Meaning | May support | Must not imply |
|---|---|---|---|
| `GroundProfile` | Elevation of the modeled bare-earth or terrain surface along a path | Terrain context, slope, baseline line-of-sight inputs | Tree/building tops or current obstruction clearance |
| `SurfaceProfile` | Elevation of a defined top surface such as DSM cells along a path or corridor | Candidate above-ground surface context | Verified object identity, current height, or survey accuracy |
| `PointCloudSlice` | Selected source points with classifications and support metadata | Reprocessing, QA, local evidence about returns | A gridded DSM until a documented derivation is applied |
| `ObstructionCandidate` | A derived local height or surface feature that crosses a declared screening rule | Review queue and map/profile annotation | Confirmed obstruction, ownership, permanence, or regulatory significance |
| `LineOfSightContext` | Geometric sight line under named endpoint and curvature/refraction assumptions | Planning visualization | Radio performance or build approval |
| `FresnelContext` | Frequency-dependent modeled zone under explicit endpoint, antenna, path, and clearance-policy inputs | Screening and comparison | Engineering certification, availability, capacity, interference, or site viability |

“LiDAR,” “DSM,” “DTM,” and “elevation” are not interchangeable. LiDAR is a measurement technology and point cloud may be a source carrier. A DTM is a modeled ground surface. A DSM is a modeled top surface. Each grid value also has spatial support, resolution, interpolation, classification, acquisition-time, and uncertainty semantics.

## Proposed bounded feature contract

### `CorridorSurfaceProfileRequest`

Required fields:

- `path`: two or more WGS 84 coordinates, with coordinate order validated;
- `profile_purpose`: controlled value such as `terrain_context`, `surface_screening`, or `wireless_planning_context`;
- `sampling_interval_m` or an explicitly bounded `sample_count`;
- `corridor_width_m`: zero for centerline sampling or a positive bounded width for screening;
- `source_preference`: an admitted source/product identifier, not a free-form upstream URL;
- `as_of_policy`: acquisition-time and freshness requirements;
- `vertical_output_reference` and output units; and
- `sensitivity_class`: public, restricted, or denied.

Optional model inputs, used only when a separate `FresnelContext` is requested:

- endpoint and antenna heights with reference semantics;
- radio frequency;
- path/geodesy method;
- earth-curvature or effective-earth/refraction model;
- clearance rule and safety margin; and
- model/version identifier.

An omitted model input must produce `ABSTAIN` for the dependent conclusion, not a hidden default.

### `CorridorSurfaceProfileResult`

Return:

- ordered chainage/distance samples;
- `ground_profile` and `surface_profile` as separate nullable series;
- the sample support used: center pixel, interpolated point, corridor maximum, percentile, or another declared reducer;
- optional `obstruction_candidates` with derivation rules, not object assertions;
- source-segment identities, footprints, acquisition/processing dates, resolution, classifications, and quality metadata;
- horizontal CRS/datum and vertical datum/geoid/epoch/units;
- nodata, void, water, seam, boundary, and fallback flags;
- transformations and resampling/interpolation methods;
- uncertainty or an explicit `UNKNOWN`/`NOT_PROVIDED` state;
- retrieval and artifact identities;
- licensing/attribution and export controls; and
- one finite outcome: `READY`, `PARTIAL`, `NO_COVERAGE`, `STALE`, `HOLD`, `DENY`, `ABSTAIN`, or `ERROR`.

`READY` means the bounded profile artifact passed its declared checks. It does not mean the wireless path, construction, sale, or field condition is ready.

## Sampling and computation design

Raster sampling is a normal geospatial operation; it need not require downloading or scanning a statewide raster for every request. A governed implementation should:

1. intersect the path/corridor with admitted product footprints;
2. select only the required source segments or tiles;
3. use bounded Cloud Optimized GeoTIFF range reads, tiled raster windows, EPT/COPC bounds, or a governed server-side profile operation;
4. reproject the path once into each source grid while retaining the original geometry;
5. read only intersecting blocks plus a declared interpolation/kernel halo;
6. treat seams, nodata, differing resolution, and datum boundaries as first-class events;
7. reduce corridor cells with a declared statistic rather than silently taking one extreme pixel;
8. reject or flag isolated spikes, void-fill artifacts, edge effects, and implausible values under a versioned QA rule; and
9. cache only immutable admitted artifacts and derived results that the applicable license and sensitivity policy allow.

A “maximum” requires a support definition. KFM must state whether it means one cell, all cell centers within a buffer, all cells touched by the path, a local window, a percentile, or an object-aware aggregation. A raw maximum is especially vulnerable to noise and isolated high returns.

## Source selection and fallbacks

1. **Preferred source-specific lane:** use an admitted USGS 3DEP DTM/DEM and, where an exact suitable DSM or classified point cloud exists, derive or use a separately admitted surface product.
2. **Discovery lane:** use LiDAR Atlas only to find and compare candidate projects; verify every selected project against the official publisher before admission.
3. **Convenience comparison lane:** use GPXZ server-side only after credential, source-ID, vertical-reference, terms, privacy, quota, and cost closure. Preserve the reported source metadata for every segment.
4. **Licensed path-elevation lane:** Google Elevation can provide sampled path elevations using its documented path-and-samples request, but KFM must not interpret those values as a LiDAR DSM or obstruction tops. Current Google Maps Platform terms and attribution/display rules control any use.
5. **Restricted observation lane:** May Mobility LiDAR is eligible only for an authorized partner/vehicle event with pose, frames, clocks, calibration, location sensitivity, and rights resolved.
6. **Scientific reference lane:** ICESat-2 may contribute along-track terrain/canopy reference where tracks and product semantics support the comparison. It must not silently fill continuous corridor gaps.
7. **No surface coverage:** return `NO_COVERAGE` or `PARTIAL`. A ground-only result may be shown as ground-only; it must not be padded with a hidden constant or relabeled as clearance evidence.

## Vertical reference, time, and coverage gates

Do not compare or combine profiles until every segment has explicit:

- horizontal CRS/datum;
- vertical datum or ellipsoid, geoid model and epoch where applicable;
- units;
- acquisition interval and processing/publication dates;
- grid/pulse support and resolution;
- accuracy or uncertainty status;
- source footprint and gaps; and
- transformation method and residual/error information.

A newer derived composite does not make an older source observation current. Buildings are added or removed, vegetation changes, and surfaces may be interpolated or fused from different dates. The interface must show the acquisition age of each segment and a `STALE` or `PARTIAL` state when the request's freshness rule is not met.

## Google Elevation policy boundary

Google's official documentation supports point and sampled-path requests, returns elevations in meters relative to local mean sea level, and permits up to 512 locations per request. Its current policies also restrict prefetching, caching, and storage except where expressly allowed and impose display/attribution requirements. KFM must review the live agreement for the intended use and account before any activation. Google responses must not be copied into a reusable KFM source archive merely because the API is convenient.

## ICESat-2 boundary

NASA describes ICESat-2 as a six-beam photon-counting laser altimeter with along-track measurements, and ATL08 as along-track terrain and canopy-height products. These data can be scientifically valuable, but the observation geometry is not a wall-to-wall, current, local DSM. A track crossing may support a bounded comparison; absence of a crossing cannot be treated as evidence that a corridor is clear.

## Explorer presentation

The profile view should render four visually distinct series only when each exists:

- admitted ground surface;
- admitted or derived top surface;
- modeled line of sight; and
- modeled Fresnel envelope.

It should also show source-segment bands, acquisition age, resolution changes, datum transformations, nodata gaps, and uncertainty/unknown states. Selecting a chart sample should synchronize a marker on the 2D/3D map and open the Evidence Drawer for the exact source segment and derived artifact.

Numeric samples must come from unexaggerated admitted data. MapLibre terrain exaggeration is a display parameter and must never alter the profile values or calculations. If only ground data exist, the surface series remains absent. Gaps remain gaps. A red crossing can mean “screening threshold crossed under this model”; green must never imply field-certified clearance.

The public wording should be: **planning context only; verify current conditions, rights, structures, vegetation, and engineering assumptions before use.**

## Security, privacy, licensing, and cost

- Keep API keys and provider tokens server-side; never place secrets in browser URLs, TileJSON, logs, evidence, or exports.
- Validate path bounds, coordinate order, request size, interval, sample count, response type, redirects, and content length before network access.
- Deny sensitive infrastructure or exact-location requests when policy requires generalization or restricted handling.
- Pin provider dataset/version metadata when available and record immutable request/response hashes for allowed fixtures.
- Apply per-provider caching, storage, attribution, redistribution, screenshot, and export rules.
- Bound quotas, retries, time, bytes, concurrency, cost, and retention; an exhausted quota is `HOLD` or `ERROR`, not missing terrain.
- Do not let client-selected URLs, source IDs, filenames, or object keys bypass the admitted-source registry.

## Offline fixture and acceptance plan

The first implementation slice should make zero live upstream calls and use small synthetic fixtures that exercise:

1. flat ground with no surface product;
2. flat ground plus one building-like surface block;
3. canopy-like variable top surface;
4. a single extreme outlier inside the corridor;
5. centerline versus corridor-width reducers;
6. a nodata gap and a partial-coverage edge;
7. a project/tile seam with equal datum and resolution;
8. a seam with different resolution;
9. a vertical-datum mismatch that must `ABSTAIN`;
10. a stale DSM over a current DTM;
11. DTM-only fallback that remains explicitly ground-only;
12. endpoint inclusion and equidistant chainage;
13. oversampling relative to raster resolution;
14. reversed coordinates, zero-length path, unsafe width, and excessive sample count;
15. missing frequency or antenna reference in a Fresnel request;
16. MapLibre exaggeration proving no effect on numeric results;
17. restricted-coordinate denial;
18. provider timeout, quota exhaustion, malformed response, and license denial; and
19. deterministic rerun with identical digests and finite receipts.

Acceptance requires source-segment provenance, gap/staleness visibility, explicit vertical-reference handling, stable finite outcomes, accessible 2D presentation, Evidence Drawer linkage, and no “clear path” assertion.

## Promotion gates

- [ ] Product, terrain, wireless-domain, security/privacy, rights, cost, accessibility, and release owners assigned.
- [ ] Exact first product and claim role selected; Reddit is excluded from the source registry.
- [ ] DTM, DSM, point-cloud, obstruction-candidate, line-of-sight, and Fresnel semantics accepted.
- [ ] CRS, horizontal datum, vertical datum/geoid/epoch, units, resolution, accuracy/uncertainty, nodata, and time contracts accepted.
- [ ] Sampling support and corridor reducer are explicit and robust against outliers.
- [ ] USGS product identity and acquisition path are proven with a bounded immutable fixture.
- [ ] Any GPXZ, LiDAR Atlas, Google, or other commercial-service terms, credentials, quotas, cost, privacy, caching, attribution, and export rules accepted.
- [ ] Fresnel model inputs, assumptions, versioning, and abstention behavior independently reviewed.
- [ ] Offline fixtures pass with zero network access by default.
- [ ] Explorer, Evidence Drawer, report/export, correction, withdrawal, rollback, and non-exaggerated numeric parity pass.
- [ ] A separate admission, release, deployment, promotion, and publication decision is recorded.

## Current disposition

`HOLD / VALIDATED_BRANCH_ONLY`

The use case is worth retaining because it clarifies a missing user-facing capability and exposes important failure modes. No source or feature is activated. The next owner decision is whether to authorize a small offline `CorridorSurfaceProfile` contract/fixture slice that reuses the existing USGS 3DEP terrain work and keeps `FresnelContext` optional and separate.

## Non-effects

No Reddit user was contacted; no vendor was contacted; no account, key, subscription, request, response, raster, point cloud, corridor, radio path, source admission, connector, registry entry, contract/schema enum, policy rule, EvidenceBundle, runtime layer, deployment, promotion, publication, PR, merge, engineering conclusion, or incident closure was created.

## Sources

### Community discovery input

- [Reddit r/LiDAR — API for elevation data?](https://www.reddit.com/r/LiDAR/comments/16jnu4k/api_for_elevation_data/)

### Official product documentation

- [Google Maps Platform — Elevation API overview](https://developers.google.com/maps/documentation/elevation/overview)
- [Google Maps Platform — Elevation requests](https://developers.google.com/maps/documentation/elevation/requests-elevation)
- [Google Maps Platform — Elevation API policies](https://developers.google.com/maps/documentation/elevation/policies)
- [USGS — LidarExplorer](https://www.usgs.gov/tools/lidarexplorer)
- [USGS — TNMAccess API documentation](https://tnmaccess.nationalmap.gov/api/v1/docs)
- [NASA — ICESat-2 mission](https://icesat-2.gsfc.nasa.gov/)
- [NASA Earthdata — ATL08 land and vegetation height](https://www.earthdata.nasa.gov/data/catalog/nsidc-daac-atlas-icesat-2-l3a-land-vegetation-height-001)

### Existing KFM research context

- KFM Real-Data Resource Integration — Research Manual & Delivery Hub
- KFM USGS TNMAccess Source Intake
- KFM LiDAR Atlas API Source Intake
- KFM GPXZ Elevation Service Source Intake
- KFM May Mobility Fleet API LiDAR Source Intake
- `KFM_Full_Atlas_seed_cards.md` — transport-corridor evidence-lane design seeds; no terrain/Fresnel implementation assertion found
- `KFM_MapLibre_Operating_Architecture_Governed_UI_AI_Interaction_Manual_REVISED.pdf` — governed MapLibre operating context; no Fresnel implementation assertion found in the inspected text
