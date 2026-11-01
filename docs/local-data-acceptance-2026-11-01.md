# Local-data relay production acceptance — 2026-11-01

Status: **PARTIAL ACCEPTANCE; corrections proposed, not deployed.** Read-only
production checks ran about 16:48–16:52 America/Chicago (22:48–22:52 UTC).
No operating service was stopped, no private worker or admin route was probed,
and no database, index, key, dataset record or publication boundary was changed.

## Identity and scope

- Base: hosted composition branch `a0-hosted-ai-web-20261017`, commit
  `188127f3c4130d6aeb20fc5d5fd88c9804d7e5c6`. PR #5691 merged as
  `59dae8776de12ea745e153cdc9dd19021086ce0b`; #5692 is now merged.
- [Production /api/build](https://kansasfrontiermatrix.com/api/build) returned
  application `urdng3v1vk`, 1,180 application files, digest
  `sha256:34d7c85a25726f189ab6b876b8463c87f84e1129d838757cadd6d0233d95b62e`.
  An independent applicationIdentity() computation over the downloaded hosted
  source matched. The six existing files edited here were individually compared
  byte-for-byte with the exact base via GitHub.
- Production reports `sourceCommit: null`, `commitState: WORKTREE_MODIFIED`.
  **CONFIRMED:** application-input equivalence. **UNKNOWN:** literal deployed Git
  commit and clean-checkout provenance. The digest excludes data, settings, models
  and build bytes; it is not release authority. PR #5692 changes documentation only.
- [Catalog](https://kansasfrontiermatrix.com/api/local-data): 17 datasets,
  `online: true`. This is worker connectivity, not per-dataset readiness, complete
  data coverage, scientific validation, or source admission.

## All 17 representative responses

Every endpoint returned 200 with nonempty results. Source objects matched the
public catalog on the repeatable probe. Initial requests were served `live`;
repeats were `fresh`. Counts are returned sample rows / matching total, not
a full-database census. Units apply to scientific values, not every metadata field.

| Dataset | Count / total | Evidence and limits |
|---|---:|---|
| `storm-events` | 2 / 852 | Event begin/end with CST-6; NOAA damage estimates and magnitude type codes retained. |
| `ghcn-stations` | 2 / 57 | Station lat/lon, elevationM, element coverage years and archive date retained. |
| `ghcn-daily` | 2 / 918 | 2025-07-01 PRCP 0 mm and TMAX 31.1 degC; raw values and measurement/quality/source flags retained. |
| `ghcndex-indices` | 26 / 26 | All 26 definitions with units; dictionary has no observation timestamp or pagination. |
| `ghcndex` | 2 / 72 | 1954 annual TXx 45 degC; beta caveat and index/year/period retained. |
| `asos-5min` | 2 / 288 | 2000-12-25 local standard time; raw METAR/UTC token, knots, degC and inHg retained. |
| `wind-stations` | 2 / 4 | Station identity, coordinates and archive interval retained. |
| `wind-daily` | 2 / 30 | 2025-06-01 average/maximum/gust in knots; date retained. |
| `prism-county` | 2 / 12 | Riley 2024-01 mean -0.58655 Degrees C; cell min/max/count and quality flag retained. Modeled cell-center, non-area-weighted and acquisition-date caveats retained. |
| `tiger-features` | 1 / 1 | Riley 20161 attributes; optional Polygon tested separately; NAD83 rounding notes retained. |
| `nwm-reaches` | 2 / 608 | Smoky Hill reach 18883064; optional MultiLineString tested. Geometry/output version mismatch and source not admitted caveats retained. |
| `nws-alerts` | 2 / 78 | Sample advisory sent 2026-10-30, expired 2026-10-31; properties.status Actual is captured provider status. Explicit not-live disclaimer retained. |
| `usgs-earthquakes` | 2 / 3 | Provider epoch-ms event/update times, magnitude type, reviewed status and geometry retained. One sample is near Renfrow, Oklahoma: Kansas label is not a strict state-boundary guarantee. |
| `usgs-streamflow-sites` | 2 / 181 | 181-site total; first/last observation timestamps and parameters retained. |
| `wind-observations` | 2 / 522205 | 1954-01-01T12:00Z; 160 degrees / 4 knots; absent gust remains null. |
| `nwm-streamflow` | 2 / 19 | 2026-10-07 reference/valid times; streamflowM3s, velocityMs, nudgeM3s and per-variable validity status retained; modeled and not-admitted caveats retained. |
| `usgs-streamflow` | 2 / 195 | 2026-10-23T14:45Z sample 31.8 ft^3/s; parameter 00060, statistic 00011, provisional approval and null qualifier retained. |

Provider source attribution, scientific caveats, timestamps, quality/provisional
flags and units survived in these samples. Missing numerical uncertainty is
**UNKNOWN**, not zero: no confidence interval, validation against original raw
files, unit correctness for every element, or statewide completeness was proven.
NWM admission and geometry/version review, GHCNDEX beta status, and PRISM
acquisition-date verification remain outstanding.

## Public behavior and discrepancies

- NWS pagination: limit=1 offsets 0 and 1 match the two-row page, with stable total
  78. Repeats preserved rows, generatedAt and original cache receipt time.
- Unknown dataset: 404. Missing required station, whole-state roads, over-limit
  pages, negative/over-limit offsets, unknown parameters, wide NWM bounding box
  and a malformed county string: 400. Production POST: 405 with an empty body
  (method refusal is established; JSON error-body parity with the service is not).
- **CONFIRMED defect:** GHCN from=2025-02-30 returned 200 and 500 rows instead of
  400. Shared day/minute, Storm Events and PRISM calendar validation corrected in
  the candidate; actual leap days remain accepted.
- **CONFIRMED ambiguity:** repeated limit=1&limit=2 returned 200/count=2. The
  candidate refuses repeated parameters, including identical repeats, before a
  gateway trip.
- **CONFIRMED controlled defect:** an exactly 1,000,000-byte signed gateway body
  acquired extra cache metadata and exceeded the public ceiling. The candidate
  checks the complete outgoing live/fresh/stale envelope and returns 413. No
  oversized production request was used to reproduce this boundary.
- Historical NWS disclaimer and sent/expires timestamps already survive;
  `cache.state: live` and captured provider `status: Actual` do not establish a
  current warning. Candidate source metadata adds `temporalMode:
  historical-capture` for all four capture datasets and explains delivery time
  versus observation time. Provider properties are preserved unchanged.
- Docs said all endpoints paginate; the fixed ghcndex-indices dictionary rejects
  limit and offset. The exception is now documented rather than altering its API.
- **NEEDS VERIFICATION:** ICT June 2025 observations returned total 0 while daily
  summaries returned 30. An open-ended observation query beginning in 2025 returned
  287 readings beginning 2026-10-05. This conflicts with the rollout's description
  of June readings, but does not prove a filter defect or missing local records.
  Read-only owner-side source/export inventory and indexed date-range checks are
  needed; no data were fabricated or changed.
- Earthquake coverage includes a neighboring Oklahoma event. The archive label
  alone must not be interpreted as a strict Kansas polygon filter; geographic
  admission/filter policy needs owner-side confirmation.

## Controlled failure and regression evidence

Node 24.11.1: **92/92 related tests pass** across nine local-data, home-relay
and home-inference test files. The focused relay suites are **22/22**. Six new
acceptance tests cover calendar dates, duplicate parameters, capture labels,
signed metadata through caches, bounded failures and final reply bytes. Before
the correction, four of those six failed (three defects plus the proposed
structured capture-label requirement); outage/expiry and signed-error tests
already passed.

Tests use temporary fixture databases or a signed fake relay and clock. They
exercise 15-minute fresh expiry, offline cached response, uncached 503, stale
response just before the seven-day cutoff, 503 at the exact cutoff, recovery,
signature tampering, missing indexes and gateway 413. Existing integration tests
exercise a local loopback gateway/worker and read-only queries. Seven days is
measured from the cached receipt, not added after the fresh period. These are
controlled checks, not evidence of an actual production outage or recovery.

Initial Node 22.13.1 baseline: 14/16 passed; two fixture setups failed with
`no such module: rtree`. Re-running the unchanged baseline on installed Node
24.11.1 passed 16/16. This is an **ENVIRONMENTAL** SQLite capability difference;
no fixture was weakened. Full npm test/build, browser journeys, actual pipeline
service provenance and production outage behavior: **NOT RUN / NOT ESTABLISHED**.

Reproduce (Node with SQLite RTree support for existing dataset fixtures):

```sh
node --test tests/local-data*.test.mjs tests/home-relay.test.mjs tests/home-inference*.test.mjs
node scripts/verify-local-data.mjs https://kansasfrontiermatrix.com
```

The production probe made 32 sequential GETs and failed on the two expected
production discrepancies (impossible date and repeated parameter); the remaining
checks passed. Its JSON includes request paths, timestamps, safe response headers
and full public bodies. It never invokes worker/admin routes or changes services.
The script is an acceptance probe, not a full schema/scientific validator.

## Placement, review, deployment and rollback

Directory Rules.pdf §§5–8: tests/ owns enforceability; docs/ owns human-facing
reports/runbooks; scripts/ owns operational helpers. Existing gateway modules
stay under scripts/local-data/ and the existing hosted service stays under
server/. This is the standalone GoDaddy composition governed by its AGENTS.md,
not a monorepo topology migration. No applicable ADR was present in this
composition; no new authority root/schema/policy/registry was introduced.

Changes are bounded to five existing runtime modules, the existing relay runbook,
one regression test, one read-only probe and this report. No open PRs were
returned by the repository's open-pulls API during the overlap check.
Independent review, exact-head CI and owner-controlled deployment remain pending.

Update the PC modules first with the existing release installer, then qualify
Preview and repeat public tests after owner-authorized publication. Compare
`source.temporalMode` on both catalog and answers after old in-memory caches
refresh; do not declare a site-only update sufficient for signed gateway notes.
Keep NWM caveats and the original approved public allow-list. Roll back the paired
PC/site runtime revisions if necessary, without restoring or deleting databases.

## Exact representative public requests

- [/api/local-data/storm-events?county=Riley&limit=2](https://kansasfrontiermatrix.com/api/local-data/storm-events?county=Riley&limit=2)
- [/api/local-data/ghcn-stations?name=Wichita&limit=2](https://kansasfrontiermatrix.com/api/local-data/ghcn-stations?name=Wichita&limit=2)
- [/api/local-data/ghcn-daily?station=USW00003928&element=TMAX,PRCP&from=2025-07-01&limit=2](https://kansasfrontiermatrix.com/api/local-data/ghcn-daily?station=USW00003928&element=TMAX,PRCP&from=2025-07-01&limit=2)
- [/api/local-data/ghcndex-indices?](https://kansasfrontiermatrix.com/api/local-data/ghcndex-indices?)
- [/api/local-data/ghcndex?station=USW00003928&index=TXx&period=annual&limit=2](https://kansasfrontiermatrix.com/api/local-data/ghcndex?station=USW00003928&index=TXx&period=annual&limit=2)
- [/api/local-data/asos-5min?station=KTOP&from=2000-12-25T00:00&to=2000-12-25T23:59&limit=2](https://kansasfrontiermatrix.com/api/local-data/asos-5min?station=KTOP&from=2000-12-25T00:00&to=2000-12-25T23:59&limit=2)
- [/api/local-data/wind-stations?name=Wichita&limit=2](https://kansasfrontiermatrix.com/api/local-data/wind-stations?name=Wichita&limit=2)
- [/api/local-data/wind-daily?station=ICT&from=2025-06-01&to=2025-06-30&limit=2](https://kansasfrontiermatrix.com/api/local-data/wind-daily?station=ICT&from=2025-06-01&to=2025-06-30&limit=2)
- [/api/local-data/prism-county?variable=tmax&county=Riley&from=2024-01&to=2024-12&limit=2](https://kansasfrontiermatrix.com/api/local-data/prism-county?variable=tmax&county=Riley&from=2024-01&to=2024-12&limit=2)
- [/api/local-data/tiger-features?layer=county&id=20161&limit=2](https://kansasfrontiermatrix.com/api/local-data/tiger-features?layer=county&id=20161&limit=2)
- [/api/local-data/nwm-reaches?name=Smoky%20Hill&limit=2](https://kansasfrontiermatrix.com/api/local-data/nwm-reaches?name=Smoky%20Hill&limit=2)
- [/api/local-data/nws-alerts?&limit=2](https://kansasfrontiermatrix.com/api/local-data/nws-alerts?&limit=2)
- [/api/local-data/usgs-earthquakes?&limit=2](https://kansasfrontiermatrix.com/api/local-data/usgs-earthquakes?&limit=2)
- [/api/local-data/usgs-streamflow-sites?&limit=2](https://kansasfrontiermatrix.com/api/local-data/usgs-streamflow-sites?&limit=2)
- [/api/local-data/wind-observations?station=ICT&limit=2](https://kansasfrontiermatrix.com/api/local-data/wind-observations?station=ICT&limit=2)
- [/api/local-data/nwm-streamflow?feature=18883064&limit=2](https://kansasfrontiermatrix.com/api/local-data/nwm-streamflow?feature=18883064&limit=2)
- [/api/local-data/usgs-streamflow?site=USGS-06814000&limit=2](https://kansasfrontiermatrix.com/api/local-data/usgs-streamflow?site=USGS-06814000&limit=2)

Implementation sources: [PR #5691](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/5691),
[PR #5692](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/5692),
[base relay runbook](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/188127f3c4130d6aeb20fc5d5fd88c9804d7e5c6/docs/local-data-relay.md).
