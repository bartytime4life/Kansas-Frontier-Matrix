# KFM GISHub USGS LiDAR Viewer Reference Intake

- **Date:** 2026-09-14
- **Input:** [Search, Visualize, and Download US LiDAR Data in Seconds](https://gishub.org/blog/usgs-lidar-search/)
- **Disposition:** `REFERENCE_IMPLEMENTATION_RETAINED / NO_SOURCE_ADMISSION / NO_DEPENDENCY_ADMISSION / NO_RUNTIME_BINDING / HOLD / VALIDATED_BRANCH_ONLY`
- **Scope:** research, architecture mapping, and offline evaluation design only
- **Target repository:** `bartytime4life/Kansas-Frontier-Matrix`
- **KFM evaluation pin:** `main@6c5be18cf8448654be95a6db688d98546cd5276e`
- **Viewer code pin:** `opengeos/maplibre-gl-usgs-lidar@5266c8461fb05b5d87b9c272fc32b91d1bba4eb1`
- **Point-cloud plugin pin:** `opengeos/maplibre-gl-lidar@682ea9a9aba856b8d5c4f9bd52734af47c012167`

> The corrected input URL is `https://gishub.org/blog/usgs-lidar-search/`. This record treats the article and its code as a reference implementation and interaction-pattern source. Neither the blog nor the viewer becomes a KFM data source, source authority, dependency admission, runtime layer, or release decision.

## Executive decision

Retain the GISHub viewer as the strongest current reference for a **USGS 3DEP point-cloud discovery and preview workflow inside MapLibre**. Its useful ideas are:

1. search by current extent or a drawn area of interest;
2. show coverage and individual point-cloud footprints;
3. stage one or more COPC/EPT items;
4. stream visible point-cloud detail instead of loading complete datasets;
5. inspect elevation, intensity, classification, RGB, and individual point attributes; and
6. make download/export an explicit user action.

KFM should adopt those interaction and performance patterns only behind its existing `MapRuntimePort`, source-admission, evidence, sensitivity, finite-outcome, and release boundaries. KFM should not embed the application unchanged, import its packages through feature code, or enable its direct-browser network and download behavior.

The first safe slice is an **offline, fixture-backed discovery-and-preview contract** with one tiny local COPC/EPT fixture and a deterministic point-cloud adapter evaluation. Live search, signed URLs, public cloud range access, raw downloads, and external clipping remain separate decisions.

## What the article and repositories establish

The January 14, 2026 article demonstrates a serverless viewer built around `maplibre-gl-usgs-lidar` and `maplibre-gl-lidar`. It describes a USGS 3DEP coverage index, search footprints, dynamic COPC streaming from Microsoft Planetary Computer, elevation/intensity/classification/RGB display, point picking, direct downloads, and temporary signed URLs.

The currently inspected viewer repository is newer than the article. At the pinned head it declares package version `0.11.5`, MIT licensing, Planetary Computer COPC/STAC support, AWS Open Data EPT support, and a newer clipped-COPC export path. The underlying point-cloud plugin is pinned here at version `0.17.0`, MIT licensed, and uses deck.gl, loaders.gl, COPC decoding, and `proj4`.

These facts establish upstream capabilities and implementation behavior at the stated commits. They do not prove KFM compatibility, secure network behavior, accessibility, public-data fitness, source completeness, browser performance, or release readiness.

## Authority and carrier separation

| Item | Role | What KFM may retain | What KFM must not infer |
|---|---|---|---|
| GISHub article | Tutorial and UX pattern | Search/select/load/inspect workflow | Current code identity, data authority, or fitness |
| `maplibre-gl-usgs-lidar` | Open-source search/control package | Candidate adapter behavior and tests | Source admission, dependency approval, or runtime authority |
| `maplibre-gl-lidar` | Open-source point-cloud renderer plugin | Candidate COPC/EPT streaming and visualization | Evidence truth, point-class correctness, or KFM compatibility |
| USGS 3DEP | Original public program/product family | Preferred source identity and official metadata | That every cloud mirror/item is complete or current |
| Microsoft Planetary Computer | STAC/COPC access carrier | Candidate discovery and byte-range delivery | Replacement for USGS product authority |
| AWS Open Data / `hobuinc/usgs-lidar` | EPT and raw-LAZ access carrier | Candidate streamable mirror with public-domain statement | Complete 3DEP coverage or complete CRS metadata |
| `usalidar.io` | Third-party processing/download service used by current viewer code | Separate vendor/service intake only | USGS authority, approved KFM processor, privacy clearance, or allowed export |

The AWS Open Data registry explicitly says the public EPT realization covers most resources, while the raw Requester Pays bucket is more complete but still not a complete 3DEP mirror; some sources lack usable CRS information. A successful viewer search therefore cannot be interpreted as complete national coverage, and an empty result cannot be interpreted as no LiDAR.

## KFM repository grounding

At the KFM evaluation pin:

- `packages/maplibre/package.json` declares private `@kfm/maplibre` version `0.0.0`, exact `maplibre-gl` **6.7.0**, and `vitest` 5.0.0.
- `MapRuntimePort`, `NullMapRuntime`, the package-owned MapLibre adapter, and a bounded inline-style browser candidate exist.
- external source/layer/plugin/protocol behavior remains held or absent from the governed runtime path;
- the Explorer's normal trust surfaces keep rendering, selection, evidence, policy, review, release, and publication authority separate; and
- the inspected MapLibre architecture prose still contains multiple **6.6.0** claims. That documentation is stale relative to the current package manifest and must be reconciled before any plugin compatibility decision.

The GISHub pattern fits the attached `maplibre3d.md` planning lineage, which already names `maplibre-gl-lidar` for LAS/LAZ/COPC/EPT, requires plugins to be pinned and supply-chain reviewed, keeps feature code behind the renderer adapter, and preserves 2D evidence parity. That planning file is not proof that the dependency, point-cloud schema, runtime, or public layer exists.

## Logical Explorer mapping

| Reference behavior | KFM placement | Required adaptation |
|---|---|---|
| Coverage index | Layer Catalog / Source Observatory | Released, versioned public-safe coverage artifact with acquisition/currentness labels |
| Extent or drawn-bbox search | AOI tool → governed discovery request | Reject invalid geometry; cap area, vertices, pages, items, time, and bytes |
| Result footprints | Candidate overlay | Candidate styling and source identity; never a released layer by search alone |
| Select multiple items | Staging queue | Explicit preview/commit/undo; deduplicate by stable item and asset identity |
| Load selected point clouds | MapRuntimePort point-cloud capability | Only admitted plugin plus admitted immutable carrier; no feature-module import |
| Dynamic COPC/EPT streaming | Renderer adapter | Range/CORS/content validation, point/memory/request budgets, cancellation, teardown |
| Elevation/intensity/classification/RGB | View controls | Styling only; preserve original attributes and missing-value states |
| Point picking | Renderer selection candidate | Strict safe projection into Evidence Drawer; picked values are not citations |
| Z offset | Visible display transform | Never change source Z, profile values, measurements, exports, or evidence |
| Copy/download URLs | Acquisition/export workflow | Exclude from preview; use authorized server-side acquisition and receipt path |
| Clipped COPC service | Separate processor/vendor decision | No call from first slice; require terms, privacy, deterministic recipe, lineage, and QA |

## Exact code behaviors KFM must not inherit unchanged

### 1. Invalid bounding boxes are silently widened

The viewer's `StacSearcher` replaces non-finite west/south/east/north values with global defaults and clamps them to world bounds. A malformed request can therefore become much broader than intended. KFM must reject NaN, infinity, reversed axes, zero-area geometry, out-of-policy extents, and excessive AOIs with a finite error or denial. It must never repair invalid coordinates into a global search.

### 2. Search bounds are incomplete

The viewer caps a STAC request limit at 1,000 but does not establish the KFM-required AOI, page, response-byte, geometry-complexity, or total-item budgets. KFM requires independent caps and cancellation across the entire request, not just one page.

### 3. Pagination follows provider links directly

`fetchNextPage` follows the STAC response's `next` link. KFM must validate scheme, host, port, path, method, body, collection, cursor, page count, redirect chain, response type, and byte budget before every continuation. A provider response cannot expand the allowlist.

### 4. Signed URLs are browser-visible and copyable

The current code requests a Planetary Computer SAS token, caches it in memory, appends it to each COPC asset URL, and offers a “Copy Signed URLs” action. KFM must not place bearer material in share state, clipboard output, telemetry, evidence, reports, screenshots, or persisted browser storage. Any live COPC design must separately prove whether a short-lived signed range URL can be used without violating KFM's credential and reproducibility rules; otherwise use a governed static edge or public EPT carrier.

### 5. Token failure silently changes behavior

If SAS signing fails, `getCopcUrl` logs an error and returns the unsigned asset URL. KFM must fail closed with `ERROR` or `HOLD`; it must not silently switch authentication mode or return a URL that is likely to fail later with a different, less attributable error.

### 6. The EPT index is mutable browser state

The EPT searcher defaults to a `raw.githubusercontent.com/.../master/.../boundaries.topojson` URL and caches parsed features in `localStorage` for three days. KFM must use an immutable commit/blob or admitted release artifact, record its digest and retrieval/currentness times, and keep browser cache subordinate to the active release. `master`, local storage, and a three-day TTL cannot be release authority.

### 7. EPT asset URLs originate in fetched metadata

`getEptUrl` returns the feature's URL directly. KFM must validate every carrier URL against the admitted source/item record, HTTPS requirements, host/path allowlist, expected format, and immutable identity. A catalog property cannot authorize network access.

### 8. Result ordering is not source selection

The EPT searcher sorts intersecting projects by point count before applying a limit. Point count may be useful for UI order, but it is not a quality, recency, datum, classification, coverage, or fitness decision. KFM source selection must use explicit product and claim rules and expose truncation.

### 9. Clipped export calls an external processor

The current export code posts AOI geometry, EPT source URLs, a PDAL pipeline, and processing options to `https://usalidar.io`, polls an order token, then constructs a download URL. This is a material external disclosure and processing action not described by the original January tutorial. KFM must exclude it from the first slice. A later proposal needs a separate service identity, operator/terms/privacy/retention/rights review, request and output schemas, quotas/cost/SLA, deterministic processing recipe, source-byte lineage, output digest, QA, correction, and withdrawal handling.

### 10. Browser download and output identity need hardening

The viewer starts cross-origin downloads through a hidden iframe and generates a time-based filename. KFM exports require an allowlisted response, validated content disposition/type/length, bounded streaming to quarantine, deterministic content/recipe identity, hostile-container checks, provenance, and an explicit user-authorized save. A timestamped name is not an artifact identity.

### 11. Constructors accept alternate endpoints

The reference classes allow custom STAC, SAS, collection, EPT-boundary, and clipping-service URLs. KFM feature code must not accept arbitrary endpoints. Configuration must resolve through admitted, versioned provider profiles and a server-side allowlist.

### 12. Visualization attributes remain non-authoritative

Classification colors, intensity, RGB, point tooltips, and Z offsets are useful views. They do not prove that a class was assigned correctly, that a point is current, or that its vertical reference matches another layer. Missing CRS, vertical datum, geoid, epoch, units, classification profile, acquisition time, or quality requires `HOLD` or `ABSTAIN` for dependent interpretations.

## Proposed bounded contract family

### `PointCloudDiscoveryRequest`

Required fields:

- validated public-safe AOI geometry and CRS;
- exact admitted provider/profile and collection ID;
- product/source role;
- acquisition-time/freshness criteria;
- bounded page and item limits;
- requested representation (`COPC` or `EPT`);
- sensitivity class and intended purpose; and
- request schema/version.

The browser must not provide a raw upstream URL.

### `PointCloudDiscoveryResult`

Each item carries:

- stable provider, collection, item, project/work-unit, and asset identities;
- official USGS/source reference and carrier identity as separate fields;
- footprint and intersection relation;
- acquisition and processing/publication times;
- point count/density or spacing when supplied;
- classifications and point format when supplied;
- horizontal CRS/datum, vertical datum/geoid/epoch, and units;
- quality/accuracy metadata or explicit unknown values;
- asset type, size, checksum/ETag or explicit missing identity;
- rights, attribution, redistribution, and export posture;
- retrieval/currentness time and pagination/truncation state; and
- finite outcome: `READY`, `HOLD`, `DENY`, `ABSTAIN`, `NO_RESULTS`, `PARTIAL`, `STALE`, or `ERROR`.

`READY` means discovery metadata passed its bounded validation. It does not admit, download, render, release, or publish the asset.

### `PointCloudPreviewManifest`

A preview manifest references only an admitted local fixture or released public-safe carrier and declares:

- exact asset and digest/ETag identity;
- format and parser/plugin pins;
- CRS/datum/units and declared display transformation;
- point, memory, range-request, concurrency, timeout, and retry budgets;
- allowed attributes and classification labels;
- camera/AOI, level-of-detail, and point-size defaults;
- evidence references and selection projection;
- 2D/table fallback and accessibility behavior;
- correction/withdrawal/currentness state; and
- rollback/disposal behavior.

The manifest cannot activate a plugin or source by itself.

## Dependency and adapter posture

Do not add either package yet.

The viewer currently declares lower-bounded peer/dependency ranges rather than KFM-style exact selections. Its point-cloud plugin brings deck.gl, loaders.gl, COPC parsing, LAZ decompression, projection, workers/WebGL, and transitive browser code. KFM must evaluate:

- exact package/version/integrity and lock closure;
- compatibility with the **actual current** KFM `maplibre-gl@6.7.0`;
- license/SBOM/provenance and registry-to-repository identity;
- known vulnerabilities and maintenance cadence;
- worker, CSP, CORS, range request, and cross-origin isolation behavior;
- WebGL2/GPU/browser support and graceful fallback;
- point-budget enforcement, cancellation, memory release, long-session stability, and context loss;
- React lifecycle behavior without making React own the MapLibre instance; and
- an adapter that exports KFM-owned types only.

If admitted later, all imports belong behind the accepted `packages/maplibre/` acquisition seam or another directory-rules-approved child of that seam. Explorer feature modules receive only KFM-owned `MapRuntimePort` capability types and serializable finite events.

## First implementation slice

### Phase A — offline discovery contract

1. Define the bounded request/result contracts and finite outcomes.
2. Create tiny immutable STAC and EPT boundary fixtures with Kansas-shaped synthetic/non-sensitive AOIs.
3. Prove strict AOI, URL, pagination, source-role, time, rights, CRS/datum, and truncation validation.
4. Project result footprints through the existing candidate-layer and Evidence Drawer pathways without network calls.

### Phase B — isolated point-cloud preview

1. Pin one tiny public-safe local COPC or EPT fixture and its metadata/digest.
2. Evaluate the exact point-cloud plugin version behind a test-only package adapter.
3. Prove load, level-of-detail, point budget, attribute styling, picking, cancellation, teardown, context loss, and 2D fallback.
4. Prove that Z offset and color/filter choices do not alter source coordinates, numeric samples, evidence, or exported metadata.

### Phase C — separately authorized live discovery

Only after A and B pass, decide between:

- a server-side KFM discovery adapter for Planetary Computer STAC;
- a pinned, KFM-hosted/released EPT boundary catalog plus allowlisted public EPT range access; or
- another admitted carrier.

No live phase should add “Copy Signed URLs,” arbitrary URL loading, direct external clip orders, or bulk download.

## Explorer presentation

- Add a Layer Catalog entry such as **USGS 3DEP Point Clouds — discovery candidate**.
- Use AOI draw/search as a bounded request, not an automatic fetch on pan.
- Show the coverage index separately from returned item footprints.
- Put results in a stage/preview/commit queue with counts, truncation, acquisition year, spacing/density, CRS/datum, quality, and carrier.
- Require an explicit **Preview selected** action and show current point/memory budgets.
- Offer elevation, intensity, classification, and RGB as presentation controls only.
- Route point picks to a safe Evidence Drawer projection containing item/asset identity and source attributes.
- Keep an accessible 2D footprint/table fallback with keyboard selection and text equivalents.
- Label source acquisition time, carrier retrieval time, KFM release/currentness, gaps, partial coverage, and unknown metadata separately.
- When WebGL, range requests, CORS, workers, or the plugin fail, keep the catalog and evidence available and return a visible finite state.

## Offline fixture and negative-test matrix

The first test suite should include:

1. valid small AOI with zero, one, and multiple intersecting items;
2. NaN, infinity, reversed axes, zero area, out-of-range latitude/longitude, dateline crossing, and excessive AOI;
3. excessive item limit, page limit, response bytes, geometry complexity, and decompressed size;
4. pagination loop, repeated cursor, host/path/scheme escape, redirect escape, and unexpected HTTP method;
5. missing collection/item/project/asset ID and duplicate/conflicting identities;
6. missing or invalid footprint, CRS, vertical reference, units, acquisition time, classification, and accuracy;
7. mutable `master` index rejected when immutable identity is required;
8. asset URL host/path escape, non-HTTPS URL, query token persistence, and unexpected content type;
9. signing failure producing `ERROR` rather than unsigned fallback;
10. empty response versus provider error versus partial/truncated response;
11. range server without `206`, invalid `Content-Range`, oversize chunk, CORS failure, timeout, retry exhaustion, and cancellation;
12. point budget, memory budget, concurrency, and long-session cleanup;
13. worker load failure, WebGL2 absence, context loss, reduced motion, and keyboard-only operation;
14. point picking with unsafe/oversized attributes and evidence-reference mismatch;
15. classification/RGB missing values and isolated elevation outliers;
16. Z offset proving source-Z and numeric-elevation invariance;
17. sensitive-geometry denial before discovery or network construction;
18. third-party clip service, arbitrary endpoint, signed-URL clipboard, and bulk download denied in the first slice;
19. deterministic replay with identical item order, hashes, finite result, and receipts; and
20. rollback to `NullMapRuntime` with no persistent plugin, worker, source, or cache state.

## Promotion gates

- [ ] Reconcile KFM's current `maplibre-gl@6.7.0` manifest with stale 6.6.0 architecture claims.
- [ ] Assign product, terrain/3D, renderer, dependency/security, privacy/sensitivity, accessibility, data-rights, operations, and release owners.
- [ ] Select one exact USGS project/product and one carrier; preserve source authority separately from carrier.
- [ ] Accept request/result/preview contracts, finite outcomes, and source/layer/evidence roles.
- [ ] Pin exact viewer/plugin evaluation commits, packages, lock closure, licenses, SBOM, and vulnerability evidence.
- [ ] Prove MapLibre 6.7.0 compatibility and package-seam confinement.
- [ ] Prove strict AOI, URL, pagination, range, redirect, size, timeout, retry, cancellation, and decompression bounds.
- [ ] Resolve SAS/signed-URL, CORS, browser cache, telemetry, share-state, and attribution behavior.
- [ ] Replace mutable EPT boundaries with an immutable admitted artifact and currentness rule.
- [ ] Keep `usalidar.io` and all external clipping/download processing excluded or complete a separate service intake.
- [ ] Close CRS, vertical datum/geoid/epoch, units, acquisition time, quality/accuracy, classification, nodata, and coverage semantics.
- [ ] Pass offline fixtures, isolated real-browser/GPU/accessibility/performance/long-session checks, and 2D fallback.
- [ ] Bind selection to Evidence Drawer without treating picked properties as evidence.
- [ ] Prove correction, withdrawal, cache invalidation, report/export, disposal, and rollback.
- [ ] Record separate dependency admission, source admission, runtime, release, deployment, promotion, and publication decisions.

## Current disposition

`HOLD / VALIDATED_BRANCH_ONLY`

The reference is logically incorporated as a concrete discovery-and-preview design pattern and a code-level risk inventory. It is not activated. The safest next owner decision is whether to authorize the Phase A offline `PointCloudDiscoveryRequest`/`Result` contract and fixture slice. That work can proceed without installing the plugin, contacting providers, exposing an AOI, or making any network request.

## Non-effects

No package was installed; no dependency or lockfile changed; no API/STAC/SAS/EPT request was made; no signed URL, bearer token, AOI, project ID, source item, point cloud, cache entry, download, clip order, PDAL job, external-service disclosure, source admission, plugin admission, registry entry, runtime source/layer, EvidenceBundle, release, deployment, promotion, publication, PR, merge, or incident closure was created.

## Sources

### Reference implementation

- [GISHub tutorial — Search, Visualize, and Download US LiDAR Data in Seconds](https://gishub.org/blog/usgs-lidar-search/)
- [`opengeos/maplibre-gl-usgs-lidar`](https://github.com/opengeos/maplibre-gl-usgs-lidar/tree/5266c8461fb05b5d87b9c272fc32b91d1bba4eb1)
- [`StacSearcher.ts` at the evaluation pin](https://github.com/opengeos/maplibre-gl-usgs-lidar/blob/5266c8461fb05b5d87b9c272fc32b91d1bba4eb1/src/lib/stac/StacSearcher.ts)
- [`EptSearcher.ts` at the evaluation pin](https://github.com/opengeos/maplibre-gl-usgs-lidar/blob/5266c8461fb05b5d87b9c272fc32b91d1bba4eb1/src/lib/ept/EptSearcher.ts)
- [`clipService.ts` at the evaluation pin](https://github.com/opengeos/maplibre-gl-usgs-lidar/blob/5266c8461fb05b5d87b9c272fc32b91d1bba4eb1/src/lib/export/clipService.ts)
- [`opengeos/maplibre-gl-lidar`](https://github.com/opengeos/maplibre-gl-lidar/tree/682ea9a9aba856b8d5c4f9bd52734af47c012167)

### Data programs and carriers

- [USGS LidarExplorer](https://www.usgs.gov/tools/lidarexplorer)
- [USGS 3DEP products and services](https://www.usgs.gov/3d-elevation-program/about-3dep-products-services)
- [Microsoft Planetary Computer — 3DEP LiDAR COPC](https://planetarycomputer.microsoft.com/dataset/3dep-lidar-copc)
- [AWS Open Data — USGS 3DEP LiDAR Point Clouds](https://registry.opendata.aws/usgs-lidar/)

### KFM context inspected

- `packages/maplibre/package.json`
- `docs/architecture/maplibre-master.md`
- `docs/architecture/map-master/RENDERER_BOUNDARY.md`
- `apps/explorer-web/src/site/README.md`
- `maplibre3d.md`
- `Master MapLibre Components-Functions-Features.pdf`
- KFM Real-Data Resource Integration — Research Manual & Delivery Hub
- KFM USGS TNMAccess Source Intake
- KFM Reddit Elevation API / Corridor Surface Profile Use-Case Intake
