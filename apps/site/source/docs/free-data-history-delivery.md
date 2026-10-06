# Free data and historical context delivery — 2026-10-06

This checkpoint records implemented source/UI work and verified local operations.
It does not grant source admission, release, publication, or scientific acceptance.
Kansas is the first acquisition area, with selected full-history datasets intended
for the local PC's existing `Projects/KFM-data` store. Wider regional and global
choices remain available for the owner's volume decision; unknown sizes are not
treated as zero or rejected merely because they may be large.

## Storage and cost boundary

The replaceable acquisition cache is capped at **500 GB: 500,000,000,000 bytes**
(about 465.7 GiB). This is a cache budget, not an assertion of current free disk
space or a cap on remote archives. Existing originals, active PRISM acquisition,
receipts and protected holdings are outside automatic replacement. Selected
Kansas payloads are downloaded into the existing local data store, outside Git
and Site assets. Providers retain their source archives; remote storage is only
temporary processing or transfer staging when needed, followed by local capture
of the selected exports. Unknown compressed/expanded sizes, available local disk,
provider quotas and export capacity must be resolved before selecting payloads.
See [acquisition receipts](acquisition-receipts.md).

No paid subscription, paid fallback, requester-pays bucket or automatic overage
was added. Earth Engine's verified noncommercial Community tier provides 150
EECU-hours per month. The owner confirmed Community verification for the existing
project, and authenticated browser metadata queries succeeded in this session.
Remaining compute quota is unverified; the billing-linked Contributor tier is excluded.
Copernicus openEO lists 10,000 free credits per month, conditional on account and
platform terms; paid extensions are excluded. Published allowances are not proof
that either account is ready. [Earth Engine tiers](https://developers.google.com/earth-engine/guides/noncommercial_tiers),
[Earth Engine usage](https://developers.google.com/earth-engine/guides/usage),
[openEO credits](https://documentation.dataspace.copernicus.eu/APIs/openEO/credit_usage.html).

Verified organization moved **25 directories, 49,749 files and 11,030,136,366
logical bytes**: eighteen Desktop reference collections into the existing
reference home, six inactive recovery packages into the existing recovery home,
and the Earth Engine working collection into the existing external data store's
`data/work/earth-engine`. Every file's SHA-256 and recorded metadata matched after
the move. A Desktop shortcut replaces the eighteen scattered reference folders.
The empty former data container was removed; no payload was deleted. Historical
receipts retain their original bytes and acquire relocation mappings in the
private catalog. Active source, actual D1/R2 storage, PRISM and unresolved or
other-chat checkouts were preserved. Private receipts and absolute workstation
locators remain in the external owner catalog. See [local files](LOCAL_PC_SITE_FILES.md)
and [consolidation](local-pc-consolidation.md).

A separate stopped-writer rehearsal subsequently copied the actual local state
into an immutable backup and isolated rehearsal store: **17,156 files,
872,732,213 bytes and 15,840 R2 blobs**. Original, backup and rehearsal identities
matched before SQLite inspection. Eight SQLite integrity checks passed on the
rehearsal copy; original and backup were rechecked before restarting the existing
services. The source alias, service definitions and protected PRISM process
remained unchanged. This establishes a rollback baseline, not permission to
replace later writes with older backup bytes.

The private catalog records the exact backup/rehearsal locators and unit/source
hashes. The completed backup receipt SHA-256 is
`069d8b70d0bcf0d05638f44ab1391b8de02de860a71863f4878b670d15886bea`.

## Historical source choices and recipes

The companion repository's existing `configs/examples/acquisition-candidates.json`
holds sixteen candidate families and twenty-six geographic choices. Its
`docs/runbooks/free-data-acquisition.md` records source-specific access and cost
limits. These are acquisition examples, not a new canonical source registry.
The private volume review records unknown future payload sizes separately from
already-captured holdings. A provider's first date is never a promise of complete
Kansas coverage, uninterrupted observations, or equivalent sensors and methods.

| Source family | Available historical scope in the candidate review | Delivered Site behavior and limits |
|---|---|---|
| PRISM | Monthly from 1895; daily from 1981; current provider endpoints vary by product | Complete-year precipitation recipes through 2025, with count checks. Existing PRISM transfer continues independently. Station-network changes prevent treating the century-long record as a homogeneous climate trend. |
| Landsat | MSS family from 1972; later sensor families retain their own mission periods | Separate Landsat 4/5/7/8/9 reflectance recipes; Landsat 1 MSS 1972–1978 inventory only. Raw MSS numbers are not harmonized reflectance; Landsat 7 scan-line gaps remain explicit. |
| Annual NLCD and USDA CDL | NLCD C1.2 1985–2025; complete CONUS CDL 2008–2025; earlier Kansas coverage needs individual verification | Candidate inventory extends beyond the existing Site CDL recipe's 2008–2024 range. Newer 10 m CDL must not silently replace the older 30 m recipe. |
| JRC Global Surface Water | Candidate v1.5 spans 1984–2024 | Existing Site recipe remains the v1.4 fixed 1984–2021 summary. No annual/current flood or v1.5 equivalence claim. |
| ERA5 and ERA5-Land | From 1940 and 1950 respectively | Inventory-only recipes through 2025; variables and export size must be chosen before a derived export. Reanalysis is modeled context. |
| TerraClimate and CHIRPS | TerraClimate 1958–2024; CHIRPS from 1981, within 50°S–50°N | Twelve-month mean PDSI and complete-year precipitation recipes respectively. Grids are not local gauges or warnings. |
| Sentinel and Dynamic World | Sentinel-1 from 2014; Sentinel-2 TOA from 2015 and SR from 2017; Dynamic World from 2015 | Existing SR and classification recipes preserve masking and probability limitations. Early SR coverage is incomplete; orbit, polarization, resolution and class meanings require comparison review. |
| GHCN-Daily, USGS Water and 3DEP | Periods belong to individual station/element/workunit records | Discovery retains unknown periods, gaps and datum details; no universal start year or annual elevation history is invented. |

The primary [Earth Engine catalog](https://developers.google.com/earth-engine/datasets)
links each recipe's exact asset and terms. Source dates and masks remain visible
in `app/earth-engine-data.ts`; generated recipes do not authenticate an account,
run an export, approve a source or install imagery. The current partial year is
discoverable at providers while annual preparation defaults to complete years.

## Captured candidate metadata

The 3DEP discovery captured **62 `KS_` provider workunits, 157,117 metadata bytes**
and no point-cloud payload. This is complete for that prefix listing, **not** for
all datasets that spatially intersect Kansas. Provider EPT metadata identifies
horizontal EPSG:3857 for these rows. Acquisition dates and vertical-datum details
remain unknown; years embedded in workunit names are not accepted as dates.
[USGS public LiDAR registry](https://registry.opendata.aws/usgs-lidar/),
[USGS 3DEP](https://www.usgs.gov/3d-elevation-program).

The terrain panel accepts a validated local discovery snapshot. It derives
rectangular geographic extents only from reported EPSG:3857 or EPSG:4326 bounds;
other native coordinate systems remain text. These are **dataset bounding
rectangles**, not surveyed acquisition footprints, actual point coverage or
proof of state membership. The dashed Kansas study rectangle is approximate.
Source links, metadata digests, native bounds and unknown date/datum labels remain
inspectable. Rendering does not fetch or verify the provider payload. A selected
terrain JSON initially remains browser-local. Its separate owner-only save action
stores a verified private Site receipt; saving the acquisition inventory does not
upload terrain metadata. Neither save admits a dataset or fetches point clouds.

USGS Water discovery captured **3,910 time-series metadata records at 711
monitoring-location IDs**, across four pages and 5,526,619 metadata bytes.
The query rectangle was `[-102.052, 36.993, -94.588, 40.003]`; border locations
are possible and Kansas state membership has not been verified. Individual
provider periods span an overall envelope from 1844-06-01T06:00:00+00:00 to
2026-10-06T08:45:00+00:00. This is not a continuous record or a period common to
all stations. Gaps and observation quality remain unverified. **No water
observation payload was downloaded in this discovery.** The owner-side station
period index preserves the per-series distinctions. [USGS API documentation](https://api.waterdata.usgs.gov/docs/).

The initial Kansas review inventory contains 78 jobs: sixteen family choices
and sixty-two EPT metadata candidates. A subsequent local-first inventory adds
one protected PRISM supplement job (79 total). Its 377,822-byte ZIP contains
eleven precipitation frames: September 2026 and ten daily labels from September
24 through October 3, 2026. The accompanying source metadata CSV is 14,160 bytes.
ZIP integrity, all eleven source identities and intervals, float32 values, and
the exact 180-by-73 EPSG:4269 grid passed inspection. The provider supplies no
checksum; local SHA-256 readback proves stored-byte identity only. These clipped
derivatives remain protected WORK candidates, separate from the active PRISM
store and replaceable cache. No new LiDAR or water-observation payload was
downloaded. Every new candidate remains unadmitted, unreleased and unpublished.

Authenticated Earth Engine discovery subsequently returned Kansas-intersecting
metadata for ten collections, including a late Sentinel-2 response. PRISM ANm has 1,581 monthly frames, January 1895
through September 2026; ANd has 16,712 provider-labelled days, January 1, 1981
through October 3, 2026. Timestamp counts found no missing or duplicate periods
inside those observed envelopes; this does not prove complete valid pixels.
Landsat 4's Kansas subset has 111 scenes from November 13, 1982 through December
10, 1991, narrower than its worldwide mission bounds. ERA5 aggregation failed
with the provider's memory limit; the unfinished ERA5-Land result remains
unresolved. A late Sentinel-2 SR response returned 58,120 intersecting scenes
from August 6, 2015 through October 5, 2026. This observed early SR coverage does
not establish a complete archive or equal coverage in every year. The original
partial receipt is retained, with later results recorded separately. Unresolved
queries are not reported as complete.

PRISM's first and latest inspected precipitation images use NAD83 / EPSG:4269,
the native 1/24-degree affine, and a 1,405 by 621 CONUS grid. The Kansas window
is 180 by 73 cells. Source day labels are essential: `ANd/19810101` starts at
1980-12-31T12:00Z. The preparation path uses native source identifiers and keeps
UTC timestamps separately, preventing a one-day annual shift. Every proposed
PRISM export checks each scene's native grid before task creation, and independent
provider queries confirmed the exact CRS/transform predicates on the two first
images. [PRISM dataset guide](https://prism.oregonstate.edu/documents/PRISM_datasets.pdf).

The local completed precipitation catalog already has all 1,580 monthly labels
through August 2026 and all 16,702 daily labels through September 23, 2026.
The provider snapshot adds one monthly and ten daily labels. Existing files are
reused; equal periods alone do not establish equal revisions. The local mask uses
TIGER 2025 while the Earth Engine recipe uses TIGER 2018, and this difference stays
explicit. A full-history one-band float32 bounding-window allocation is
961,480,080 bytes; all seven weather bands would be 6,730,360,560 bytes, excluding
compression, headers, source inventories and processing overhead. These are
calculated allocations, not measured download sizes.

Selected data now targets the local PC. The observed filesystem had about 2.12 TB
available, separately from the 500 GB replacement limit. The connected free Google
storage summary showed 11.59 GB used of 15 GB, approximately 3.41 GB remaining;
those rounded values are not a byte-level reservation. No plan or billing change
was made. Direct bounded provider downloads are preferred where supported.

## Imagery comparison and renderer boundary

The comparison implementation offers synchronized swipe and side-by-side views
for two distinct approved, installed years of the same compatible annual product.
A bounded image mosaic supports the non-WebGL path. It preserves each side's
dates, attribution, legend, grid resolution and immutable identity. Missing years
and missing pixels remain missing; colors do not produce change statistics.
Only the approved **2024** display set is currently installed, so a real temporal
pair remains **HELD** until a second compatible year is prepared and reviewed.
See [comparison controls and limits](history-comparison.md).

The existing MapLibre and Three.js renderer choices are preserved. No Babylon.js,
deck.gl, native/mobile renderer or new paid basemap binding was added. EPT
metadata inspection is separate from point-cloud/3D Tiles streaming. Such a
renderer needs real payload selection, datum/scale provenance, sensitivity review,
device/network budgets and a 2D alternative before implementation or activation.

## Disposition of supplied references

The supplied Google redirect was normalized to its YouTube destination. The
concatenated indoor/Babylon link was separated into its two intended official
examples. “Adopted” below means a bounded idea or discovery source, not copied
application code, provider account approval or source admission. Third-party
articles are inspiration only; technical implementation relies on primary docs
and the installed project's APIs.

| Supplied reference | Disposition | Result |
|---|---|---|
| [Esri 3D GIS articles](https://www.esri.com/arcgis-blog/category/3d-gis) | Reference-only | 3D exploration ideas retained; no ArcGIS subscription dependency. |
| [Earth Engine datasets](https://developers.google.com/earth-engine/datasets) | Adopted | Historical source cards, explicit recipe periods and inventory-only choices. |
| [YouTube E4H6p4IHdJg](https://www.youtube.com/watch?v=E4H6p4IHdJg) | Unavailable for verification | Retrieval failed; no unverified video claims adopted. |
| [MapLibre 3D terrain](https://maplibre.org/maplibre-gl-js/docs/examples/3d-terrain/) | Adopted/reference | Existing terrain carrier pattern retained, with provenance separated from visual relief. |
| [Three.js model example](https://maplibre.org/maplibre-gl-js/docs/examples/add-a-3d-model-using-threejs/) | Reference-only | Existing Three.js preserved; no invented model assets or georeferencing. |
| [awesome-maplibre](https://github.com/maplibre/awesome-maplibre) | Reference-only | Discovery index; listing is not dependency approval. |
| [YouTube LFzk-DfEWmU](https://www.youtube.com/watch?v=LFzk-DfEWmU) | Unavailable for verification | Retrieval failed; no video-derived technical assertions. |
| [dev.to point-cloud example](https://dev.to/hfu/how-to-use-maplibre-gl-js-with-3d-tiles-pnts-g4h) | Reference-only | Historical example; no copied dependency versions or point-cloud activation. |
| [Geomático 3D comparison](https://geomatico.es/en/vector-tiles-mapbox-maplibre-or-deckgl-for-my-3d-map/) | Reference-only | Tradeoff ideas; no new renderer selection from a secondary article. |
| [Atlas API course](https://atlas.co/courses/gis-basics/maplibre-and-mapbox-apis/) | Reference-only | Learning resource; no subscription or Mapbox dependency. |
| [Flutter MapLibre architecture](https://maplibre.org/flutter-maplibre-gl/concepts/architecture/) | Deferred | Native/mobile application outside this browser delivery. |
| [deck.gl with MapLibre](https://deck.gl/docs/developer-guide/base-maps/using-with-maplibre) | Deferred | Reconsider only after an admitted payload need and measured integration budget. |
| [ArcGIS with MapLibre](https://developers.arcgis.com/maplibre-gl-js/) | Deferred | Any future service must establish free account eligibility and hard cost boundaries. |
| [MapTiler terrain guide](https://docs.maptiler.com/guides/maps-apis/maps-platform/how-to-build-a-3d-map-with-maplibre-v2-gl-js/) | Reference-only/deferred | Technique reference; no new key, hosted-provider request or quota assumption. |
| [Three.js 3D Tiles example](https://maplibre.org/maplibre-gl-js/docs/examples/add-3d-tiles-using-threejs/) | Deferred | Payload streaming follows workunit provenance and performance gates. |
| [Indoor polygon extrusion](https://maplibre.org/maplibre-gl-js/docs/examples/extrude-polygons-for-3d-indoor-mapping/) | Deferred | Needs real geometry, height units, rights and scale; no fictional indoor data. |
| [Babylon.js model example](https://maplibre.org/maplibre-gl-js/docs/examples/add-a-3d-model-with-babylonjs/) | Deferred | Additional rendering framework unnecessary for this slice. |
| [Medium 3D discussion](https://medium.com/@geoffhtaylor3d/3d-in-maplibre-shouldnt-be-this-hard-79f39a6fe85b) | Reference-only | Discussion inspiration; no paywall bypass or article-derived API facts. |
| [MapLibre Native](https://maplibre.org/maplibre-native/docs/book/introduction.html) | Deferred | Separate native application architecture outside scope. |
| [MapLibre examples](https://maplibre.org/maplibre-gl-js/docs/examples/) | Adopted/reference | Interaction patterns checked against installed APIs; no arbitrary CDN update. |
| [Infryne overview](https://www.infrynetechworks.com/blog/maplibre-gl-js-guide) | Reference-only | Secondary overview, not implementation authority. |
| [USGS National Map Viewer](https://www.usgs.gov/tools/national-map-viewer) | Adopted | Official terrain discovery/provenance link; no automatic admission. |

## Independent acceptance matrix

The integrated candidate is based on Site **v161**, source commit
`2d378eea9635c5f041af382b7b9f1363cf6013b9`, with the uncommitted history and
acquisition additions. On 2026-10-06, using Node **22.13.1**, its production build,
TypeScript check, **540/540 Node tests**, and **16/16 Python raster tests** passed.
The final build includes the exact aquifer-worker origin guard from monorepo
security commit `59a6b31fbf`, with a regression proving foreign-origin messages
cannot fetch sources or interrupt a trusted view. Full repository lint completed
with **0 errors and 46 warnings**. Both staged and
working-tree whitespace checks passed. The compact validation receipt is
`/tmp/kfm-v161-history-origin-validation.json`, with individual build, type, Node, raster
and lint logs alongside it. These checks cover this integrated working tree;
final saved-source identity and deployment acceptance are recorded separately.
The candidate comparison receipt preserves the separately recorded
`MIRROR_REVIEW_REQUIRED` gate; application checks do not waive mirror review.

Browser checks loaded the real 78-job inventory and 62-unit terrain snapshot,
tested history search, the 1895 boundary, invalid-year feedback, filtering,
keyboard focus and a 390-pixel layout. Chrome is not connected; these checks used
the Codex browser. They do not establish full device/WebGL accessibility or a
real two-year approved-imagery pair. Local/hosted final identity and operational
readback are recorded separately in delivery receipts.

During final checks an external action moved the still-running physical v109
state directory to Trash. Its exact directory was restored atomically with no
overwrite or service restart, preserving inode identity and live writes. Nine
HTTP checks and four database integrity checks passed afterward; the source
alias, service configuration and PRISM process were unchanged. The private
recovery catalog retains the original Trash metadata and restoration receipt,
SHA-256 `6fa1885eb70f1a1c98909544bf29a47678a855d091530453532018de2c7697a3`.

| Gate | This checkpoint | Remaining evidence |
|---|---|---|
| Local organization | Verified SHA-256 preservation of 25 moves; protected stores and checkouts held | Receipt-governed rollback if future paths drift. |
| State backup | Verified stopped-writer backup, rehearsal, SQLite integrity and unchanged old-service restart | Candidate runtime rehearsal and later deployment are separate steps. |
| Candidate discovery | 62 EPT workunits; 711 water-location IDs with 3,910 series; metadata only | Spatial membership, period gaps, rights/fitness and source admission. |
| Acquisition budget | Exact 500 GB replaceable cache contract; selected Kansas histories target the existing local data store | Actual selected payload sizes, available local disk and any required provider processing/transfer capacity. |
| Free service access | Owner-confirmed Community eligibility and successful authenticated metadata queries; no paid fallback | Remaining compute quota and any job-specific export capacity. |
| Terrain UI | Validated metadata parser and truthful bounding-rectangle projection | Browser/device acceptance and any future payload/datum/accuracy review. |
| Comparison UI | Approved-pair checks and reversible controls implemented | Real pair remains held: one installed 2024 set; a second compatible approved year is required. |
| Build/test/type/lint | Recorded by exact revision in the final delivery receipt | This document does not substitute partial or inherited results for final checks. |
| Local deployment | Existing services restored after backup rehearsal | Candidate source switch, HTTP checks and browser acceptance recorded separately. |
| Hosted Site/owner auth | Existing Site identity and owner API boundaries retained | Hosted deployment and authenticated browser acceptance need their own readback. |
| Admission/release/publication | No automatic transition from discovery, import, UI or file move | Independent policy, rights, sensitivity, provenance, review, correction and rollback gates. |

Application behavior stays under `app/`, checks under `tests/`, and delivery notes
under the existing `docs/` root. The monorepo mirrors the Site under
`apps/site/source/`. This follows the adopted Directory Rules and ADR-0029
responsibility boundaries; it creates no parallel canonical contract, source,
policy or release home. The [existing gap register](KFM_SOURCE_GAP_REGISTER.md)
retains future 3D ideas and their unmet evidence requirements.
