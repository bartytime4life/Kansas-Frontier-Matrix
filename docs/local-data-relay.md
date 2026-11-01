# Local SQL data relay

The owner decided on 2026-11-01 that pipeline data stays on the pipeline PC (dev)
and that the hosting SQL database is not used for it. This relay lets the public
site answer fixed, read-only questions from the PC's local SQL databases without
copying them to hosting and without any inbound route to the PC.

- **Phase 1** (PR #5688, live since 2026-11-01 21:02 UTC): Kansas Storm Events.
- **Phase 2**: every other dataset the owner approved for public release on
  2026-11-01, listed below, through one shared query engine.

## How it works

```
visitor ──GET /api/local-data/{dataset}──▶ site (cache, 15 min fresh / 7 days stale)
                                            │ in-memory queue, signed with the gateway key
PC worker ──POST /api/local-data-worker/v1/lease (long poll, worker key)──▶ site
PC worker ──▶ 127.0.0.1:8788 gateway (verifies request, reads SQLite read-only, signs reply)
PC worker ──POST /api/local-data-worker/v1/result──▶ site (verifies the gateway signature)
```

- It is the same outbound-only relay as home inference (`server/home-relay.mjs`),
  run as a second, separate instance with its own routes, keys, limits and
  global (`Symbol.for('kfm.local-data')`). Neither relay can carry the other's
  routes, and neither worker key is accepted by the other relay.
- The worker holds no gateway key. It cannot create, change or replay a request
  or a reply; the site checks the gateway's signature over the exact request,
  status and bytes before parsing anything.
- The gateway listens on loopback only and opens a database with
  `readOnly: true` for each question. It answers only `GET /v1/health` and one
  `POST /v1/data/{dataset}` route per dataset in
  `scripts/local-data/datasets.mjs`.
- Every question is normalized by the dataset's `parse()` on the site and again
  on the PC: unknown parameters, malformed values and unbounded requests are
  `400 QUERY_INVALID`. Only values, never names, reach SQL as parameters.
- Each dataset names the indexes it relies on. Until they exist the gateway
  refuses the dataset (`DATASET_NOT_READY`) rather than scan a large table: the
  gateway's SQLite calls are synchronous, so a long scan would stall every
  question.
- If the worker has not polled for 30 s the PC is treated as away: a visitor gets
  the last cached answer marked `"cache":{"state":"stale"}`, or
  `503 {"state":"local-data-offline"}`. A job handed to a poll whose connection
  had already died still waits out its 15 s lease once.
- The site's cache holds at most 500 answers and 64 MB.

## Public API

`GET /api/local-data` lists every dataset with its parameters and source, and
whether the PC is connected (`online`). It is answered by the site alone.

`GET /api/local-data/{dataset}?…` answers one question. Replies carry `format`
(`kfm-local-data-v1`), `dataset`, the normalized `query`, `total`, `count`,
`rows`, `source` (provider, URL, coverage, notes), `generatedAt` and `cache`
(`live`, `fresh` or `stale`, with its time). Storm Events keeps its phase 1 shape
(`kfm-local-data-storm-events-v1`, `events`). A page over 1,000,000 bytes is
`413 REPLY_TOO_LARGE`; ask for fewer rows.

| Dataset | Source | Required | Other parameters | Rows per page |
|---|---|---|---|---|
| `storm-events` | NOAA NCEI Storm Events | — | `county`, `from`, `to`, `type` | 1–200 (50) |
| `ghcn-stations` | NOAA GHCN-Daily, 2,519 stations | — | `name`, `bbox`, `element` | 1–500 (100) |
| `ghcn-daily` | NOAA GHCN-Daily, 51.5M values | `station` | `from`, `to`, `element` (list) | 1–2000 (500) |
| `ghcndex-indices` | NOAA GHCNDEX (beta) | — | — | 26 |
| `ghcndex` | NOAA GHCNDEX (beta), 2.6M values | `station` | `index`, `from`, `to` (years), `period` | 1–2000 (500) |
| `asos-5min` | NOAA ASOS 5-minute, 5 airports, 2000 | `station` | `from`, `to` (local standard time) | 1–2000 (288) |
| `wind-stations` | IEM, 68 stations | — | `name` | 1–100 (100) |
| `wind-observations` | IEM, 10.4M readings, 1932–2026 | `station` | `from`, `to` (UTC) | 1–2000 (500) |
| `wind-daily` | IEM daily summaries | `station` | `from`, `to` | 1–2000 (366) |
| `prism-county` | PRISM (Oregon State), 37.9M county rows | `variable` | `county`, `step`, `resolution`, `product`, `from`, `to` | 1–2000 (500) |
| `tiger-features` | Census TIGER/Line 2025, 34 layers | `layer` | `id`, `name`, `county`, `bbox`, `geometry` | 1–200 (50); 1–20 (5) with shapes |
| `nwm-reaches` | NWM v3.0 reaches, 101,599 | one of `feature`, `name`, `huc6`, `bbox` | `geometry` | 1–200 (50); 1–50 (10) with shapes |
| `nwm-streamflow` | NWM v3.1, 2026-10-07 run | `feature` | `product` | 1–100 (100) |
| `nws-alerts` | captured NWS alerts | — | `event`, `area` | 1–50 (20) |
| `usgs-earthquakes` | captured USGS earthquakes | — | — | 1–50 (50) |
| `usgs-streamflow-sites` | captured USGS gauges, 181 | — | — | 1–500 (500) |
| `usgs-streamflow` | captured USGS readings, 35k | `site` | `parameter`, `from`, `to` (UTC) | 1–1000 (500) |

All take `limit` and `offset`. `GET /api/local-data` gives each parameter's exact
form. Notes that travel with each dataset's `source`:

- **GHCN-Daily:** values are converted from native units where the unit is
  known (PRCP mm, TMAX/TMIN °C, …); `raw` keeps the delivered value; −9999 is
  null.
- **GHCNDEX:** a beta product; period 1–12 is a month, `annual` the year.
- **IEM wind:** `M`/`None` are missing (null), not zero; the same reading captured
  in two exports appears once.
- **PRISM:** modeled cell-center county summaries, not observations or
  area-weighted statistics; citation required; per-file acquisition dates are not
  yet verified. Without `county`, one time-series period for every county.
- **TIGER:** NAD83 longitude/latitude rounded to 6 decimals. Large per-county
  layers (`block`, `block-suffix`, `roads`, `area-water`, `linear-water`,
  `address-ranges`, `edges`, `faces`) need `id`, `county` or `bbox`.
- **NWM:** model output, not gauge observations; values with a non-valid status
  are null. The pipeline has not admitted the source, and the review of v3.0
  reach geometry against v3.1 output is pending. Both caveats travel in the
  public source notes.
- **Captures:** provider properties as captured in October 2026; not live feeds.
  USGS values are mostly provisional.

**Publication approvals (owner, 2026-11-01):**

- **Storm Events:** each event's NCEI identifiers, type, county/zone, office,
  begin/end date and time with time zone, direct/indirect injuries and deaths,
  property/crop damage strings as published, magnitude, flood cause, category,
  tornado scale/length/width, begin/end location and coordinates, source,
  episode and event narratives, and data source. The fatalities table (age, sex,
  location of each death) is not exposed.
- **Phase 2:** GHCN-Daily, GHCNDEX (beta), ASOS 5-minute, IEM wind, TIGER 2025,
  NWM streamflow (its record says "source not admitted"), PRISM county climate
  (acquisition dates unverified), and the captured alerts, earthquakes and
  streamflow. Approved knowing those notes.

## Indexes

`scripts/local-data/indexes.mjs check|apply [INDEX]` lists or adds the indexes the
datasets name. They are additive, with no row changes.
`pc-pipeline-data/run/add-local-data-indexes.sh SOURCE_CHECKOUT` builds the
missing ones one at a time, each under `run/pipeline.lock`. Captures skip, as
designed, while an index is being built.

## Site settings

Off unless all are set. `KFM_LOCAL_DATA_ORIGIN` must be one of the controlled
hosting origins in `server/hosted-ai-origins.mjs`; Live is
`https://kansasfrontiermatrix.com` (`www` redirects there, so a worker polling
`www` would never connect).

| Variable | Value |
|---|---|
| `KFM_LOCAL_DATA` | `1` |
| `KFM_LOCAL_DATA_ORIGIN` | exact origin the worker polls |
| `KFM_LOCAL_DATA_GATEWAY_KEY_ID` / `KFM_LOCAL_DATA_GATEWAY_SECRET` | the PC gateway key |
| `KFM_LOCAL_DATA_WORKER_KEY_ID` / `KFM_LOCAL_DATA_WORKER_SECRET` | the PC worker key; must differ |

## PC services (dev)

`pc-pipeline-data/run/install-local-data.sh SOURCE_CHECKOUT [WORKER_SITE]`:

- copies every `scripts/local-data/*.mjs` file, plus the four shared
  home-inference modules, into
  `pc-pipeline-data/runtime/releases/local-data-<digest>/`, with a
  `release.json` (source commit, branch, whether the source was uncommitted,
  file digests);
- makes the two owner-only keys once, in `pc-pipeline-data/transfer-access/`;
- writes `pc-pipeline-data/runtime/local-data.env`: the observations database,
  the TIGER and NWM GeoPackages, the key files and the worker's site;
- installs two user units:
  - `kfm-local-data-gateway.service`, enabled; it mounts the data disk first;
  - `kfm-local-data-worker.service`, enabled since Live was switched on.

`node pc-pipeline-data/run/check-local-data.mjs` makes a signed health check
(datasets ready, and any that are not, with the reason) and one sample query. It
prints only the result.

The site and the PC must agree on the routes. Update the PC first: a phase 1
site never asks the new routes, but a phase 2 site's new datasets would be
refused by a phase 1 worker.

## Verification

### Phase 1 — 2026-11-01

- **Tests:** `tests/local-data.test.mjs` with the home-relay and home-inference
  suites, 73/73. Full `npm test`: 2,454 pass, 24 skipped, 0 fail.
- **Local production build** behind a stand-in proxy:
  - live answers in 0.2–0.3 s and cached answers in 7 ms;
  - a 407 KB page passed;
  - the offline, stale and reconnect behavior was checked.
- **Live, 2026-11-01 21:02–21:07 UTC** (`53d527d` published; the dev worker
  polling `https://kansasfrontiermatrix.com`):
  - Sedgwick tornadoes: 91 events, live in 1.0 s, then from cache in 0.4 s;
  - Sedgwick since 2020: 200 events, 261 KB, in 1.3 s;
  - blizzards: 200 events, 407 KB, in 2.7 s;
  - a bad query was refused (400);
  - `www` returned 308 to the apex.

  So the long poll works through Cloudflare and the GoDaddy proxy, and the
  worker key and gateway key on Live match the PC's.

### Phase 2 — 2026-11-01

- **Indexes:** 24 indexes added on dev, one at a time under the pipeline lock;
  captures kept running in between. The ASOS index already existed.

  | Index | Time to build |
  |---|---|
  | GHCN-Daily, 51.5M rows | 74 s |
  | PRISM, 37.9M rows | 58 s |
  | IEM wind, 10.4M rows | 23 s |
  | every other index | under 8 s each |

  `observations.sqlite` grew from 5.3 GB to 7.4 GB; the TIGER GeoPackage grew
  by 0.1 GB.
- **Tests:** `tests/local-data-datasets.test.mjs` uses fixture databases shaped
  like the PC's. It covers:
  - every dataset's answers;
  - refusal until indexes exist;
  - parameter refusal;
  - GeoPackage geometry decoding;
  - PRISM path parsing;
  - the site's catalog and dataset routing.

  With `tests/local-data.test.mjs`, 16/16 pass. Full `npm test` (build and
  2,495 tests): 2,471 pass, 24 skipped, 0 fail.
- **Real databases, through the gateway:** all 17 datasets ready.
  - Most first answers took 0.02–0.4 s.
  - A few cold-disk first reads took 2.5–4 s; PRISM's first question also loads
    its 361k-grid catalog. The gateway's limit is 10 s.
  - The largest pages:

    | Page | Size |
    |---|---|
    | 2,000 PRISM daily rows | 399 KB |
    | the state outline | 307 KB |
    | 2,000 GHCN-Daily values | 284 KB |
    | 2,000 wind readings | 283 KB |
- **Local production build** behind the stand-in proxy, with a phase 2 gateway
  and worker on dev:
  - the catalog listed 17 datasets with `online: true`;
  - every dataset answered live, most in 0.02–0.3 s, and PRISM's first in 3.1 s;
  - a repeated question was served from cache in 18 ms;
  - a whole-state query of the roads layer, an unknown dataset and an
    over-limit page were refused.
