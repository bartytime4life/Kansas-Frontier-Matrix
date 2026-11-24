# Kansas native LiDAR relay and processing

The Terrain card requests the current map view. The generic pipeline uses free,
public USGS EPT sources selected by coverage geometry; NEON/Konza remains a
separate optional example. No subscription, paid API or visitor token is added.
Source originals, prepared views, private receipts and credentials stay outside
Git and public assets, on the owner's existing dev data drive.

## Sources and meaning

The hash-pinned catalog contains 127 reachable EPSG:3857 LASzip EPT projects,
including Kansas-prefixed, USGS_LPC_KS-prefixed and intersecting border projects.
126 provider polygons cover KFM's generalized Kansas outline in a discovery
union check. One candidate has bounding-box-only geometry. These polygons show
where to look, not that all native data is installed, or that classification,
acquisition date, accuracy and density are uniform. Project names do not prove
coverage or flight dates. The fixed public bucket excludes requester-pays data.

Ground retains the selected continuous DEM context. Native points are an
additive EPT display selection, cropped to the viewport and bounded to100,000
records. Surface and canopy need complete intersecting hierarchy support from
one survey, independently of point display thinning. All native hierarchy levels
and Z siblings are considered; truncated or failed support cannot produce a
qualified grid. A source budget can leave honest partial/detail-required states.

Native source XYZ and original `(asset, record)` identity are preserved without
coordinate rounding. Encoding precision is not accuracy. Every asset carries
its own acquisition description, vertical reference and raw GPS encoding;
calendar flight dates are not inferred. Local source hashes identify captured
bytes, not provider-published expected digests or browser cache-envelope hashes.

For analysis, a local UTM14/15 rectangle and its curved projected perimeter are
computed with Rasterio/PROJ. The source crop expands the actual rectangle by the
model's neighbor radius plus a1m numerical guard, then projects a densified
perimeter back to EPSG:3857. The same rectangle is used by the decoder.

- Ground is a distance-weighted least-squares plane from at most32 nearby class2
  returns, with radius `min(75m,max(5m,4*largestCellSide))`. Full rank, bounded
  conditioning and source convex-hull support are required; no extrapolation.
- Surface is the maximum valid first-return elevation in each cell; buildings,
  unclassified objects and wires may contribute.
- Canopy is the maximum classified vegetation (3/4/5) return minus the supported
  same-survey ground plane evaluated at that return. Class1 is not vegetation.
- Synthetic/withheld flags and noise classes7/18 are excluded from analysis and
  default measured-point display, while original records remain inspectable.
- NoData remains null; negative normalized heights remain available for review.
  Ground residual is model-fit RMSE, not independent measurement uncertainty.

All review/admission/accuracy flags remain pending/false. Native-to-context DEM
registration is unverified. Rendering uses its own point/cell depth above map
context, not verified terrain occlusion or DEM-difference measurement.

## Requests and reuse

`GET /api/lidar/view?bbox=west,south,east,north&zoom=17&layers=surface,canopy,points`
returns processing/coverage/layer states and a canonical SHA256 request key.
Ground alone does not start a native job. The public API accepts only bounded
Kansas coordinates, zoom and enumerated layers, never URLs, paths or SQL.

A ready receipt links `/api/lidar/view/{key}/{chunkId}` and
`/api/lidar/view/{key}/grid`. V2 point manifests preserve per-asset provenance;
grids preserve native support counts, residuals, projected cell geometry,
methods and nulls. `app/kansas-lidar-view.ts` and `app/native-lidar.ts` export
validated models for other KFM tools; they do not silently ingest into every
science tool. `/labs/terrain` still has its separately verified example adapter.

The website forwards only fixed HMAC-signed POST routes through the existing
home relay. It verifies the signed HTTP status/body before schema validation.
The existing1MB relay limit,22 datasets, water repair, NEON package and example
point package are retained. The processor runs on dev, not inside GoDaddy.

## Local process and limits

Set `KFM_LIDAR_VIEW_ROOT` to an existing owner-private0700 directory outside the
checkout on the data drive and `KFM_LIDAR_VIEW_PYTHON` to an absolute isolated
Python runtime with numpy,laspy,lazrs,rasterio,scipy. Run
`node scripts/local-data/lidar-view-worker.mjs`; `--once` drains one queue pass.
The gateway uses the same view root; the existing network relay worker requires
no provider token. Keep gateway signing keys separate from provider credentials.

One actor serializes work under a private PID lock. Files are owner-only regular
files, disallow symlinks/hardlinks and are checked against size/hash receipts.
The source cache only fetches HTTPS node/hierarchy paths from pinned projects,
with normal certificate verification, redirects rejected and bounded retries.
Cache responses are rechecked before reuse. Storage is not evicted silently.

Budgets:16 queued requests,2048 prepared/failed view directories,128 source nodes,
2million decoded source records,64 hierarchy replies,64MiB read budget per job,
180s job timeout,64×64 analysis cells, at most1.05km² projected grid rectangle,
16 chunks,16MiB native transport and500GiB retained source-cache reservations.
A2GiB disk reserve is checked before storing sources. Reservations are persisted
before source writes so a crash may overcount, but cannot undercount retained
bytes. Failed views preserve receipts and can retry after60s, up to3attempts.
These bounds preserve predictable local storage/CPU; they do not promise full
native-density statewide rendering at one zoom level.

## Reproducible qualification

Run the Node relay tests with `node --test tests/lidar-viewport-relay.test.mjs
 tests/lidar-points-relay.test.mjs tests/local-data.test.mjs
 tests/local-data-acceptance.test.mjs tests/home-relay.test.mjs` (one command).
Run the analytic science checks with the isolated processor runtime:
`python -I -B scripts/local-data/lidar-science-test.py scripts/local-data/lidar-decode.py`.
Synthetic checks establish math/transport behavior, not survey field accuracy.

Owner-device qualification on2026-11-24 processed small western, central and
 eastern Kansas views from three distinct public projects. Each returned100,000
bounded display records and4096 supported surface cells. All300,000 displayed
records were independently compared against their original LAZ XYZ/attributes
and record IDs. No vegetation classes were present in these particular tests;
canopy correctly remained null. This is bounded native/processor evidence,
separate from browser/GPU, public deployment and independent scientific review.
