# NOAA NCEI Access Data Service for KFM

Status: **IMPLEMENTED CAPTURE / PRODUCT ADMISSION AND RELEASE PENDING**.
The [owner-supplied NOAA documentation](https://www.ncei.noaa.gov/access/search/documentation/data-service/)
defines the fixed endpoint `https://www.ncei.noaa.gov/access/services/data/v1`.
Six small Kansas live captures succeeded without an API key on 2026-10-14 UTC:
12,462 source bytes, 30 rows, with exact stored-byte readback and offline replay.
This service is separate from the token-based Climate Data Online API.

## Responsibility and configuration

[Directory Rules v2](../doctrine/directory-rules.md), adopted by
[ADR-0029](../adr/ADR-0029-adopt-directory-governance-standard-v2.md), §10.1 and
`DIR-SOURCE-003` assign acquisition to `connectors/`, operators to `tools/`,
guidance to `docs/`, and lifecycle instances/receipts to private `data/`.
Existing roots are used; no new schema, policy, registry or release authority.

- `connectors/noaa/src/noaa/ncei_access.py`: fixed profiles, bounded transport,
  product-specific inspection and replayable capture identity.
- `tools/local_data/noaa_ncei_access.py`: offline planning, explicit live capture,
  immutable quarantine, failure receipts and offline replay.
- `connectors/noaa/tests/test_ncei_access.py` and
  `tests/tools/test_ncei_access_operator.py`: boundary regressions.
- `.github/workflows/noaa-connector-offline.yml`: existing Python 3.11/3.12 gate.

The operator needs only Python 3.11+ and the verified repository: it imports
connectors-core from its existing source home. No package installation, API
secret, account provisioning, Sites setting or GoDaddy DNS record is needed
for acquisition. Do not copy the operator away from its dependencies.

## Products and interpretation

| Dataset | Role and period | Configured elements |
| --- | --- | --- |
| `daily-summaries` | Daily station observation summary | PRCP, TMAX, TMIN, SNOW, SNWD |
| `global-summary-of-the-month` | NOAA monthly aggregate (GSOM) | PRCP, TMAX, TMIN, TAVG, SNOW |
| `global-summary-of-the-year` | NOAA yearly aggregate (GSOY) | PRCP, TMAX, TMIN, TAVG, SNOW |
| `normals-daily-1991-2020` | Cyclic daily normal | DLY-TMAX-NORMAL, DLY-TMIN-NORMAL |
| `normals-monthly-1991-2020` | Monthly normal | MLY-PRCP-NORMAL, MLY-TMAX-NORMAL, MLY-TMIN-NORMAL |
| `normals-annualseasonal-1991-2020` | Annual normal only | ANN-PRCP-NORMAL, ANN-TMAX-NORMAL, ANN-TMIN-NORMAL |

All normals carry the explicit 1991–2020 baseline. The annual/seasonal profile
selects annual variables; no seasonal values are inferred. GSOM/GSOY are not
bias-corrected GHCN-Monthly. Their temperature statistics have product-specific
aggregate meanings; monthly/yearly TMAX is not a day's measured extreme.
Normals describe climatology, not conditions in the query year or a forecast.
Daily-normal dates select calendar days. Monthly/annual normals omit dates;
the verified annual-normal response has no DATE field.

Provider references: [GSOM](https://www.ncei.noaa.gov/access/search/datasets/global-summary-of-the-month/),
[GSOY](https://www.ncei.noaa.gov/access/search/datasets/global-summary-of-the-year/),
[daily normals](https://www.ncei.noaa.gov/access/search/datasets/normals-daily-1991-2020/),
[monthly normals](https://www.ncei.noaa.gov/access/search/datasets/normals-monthly-1991-2020/),
[annual/seasonal normals](https://www.ncei.noaa.gov/access/search/datasets/normals-annualseasonal-1991-2020/).

## Plan, capture, replay

```bash
python tools/local_data/noaa_ncei_access.py products
python tools/local_data/noaa_ncei_access.py plan \
  --dataset daily-summaries --start 2024-01-01 --end 2024-01-02 --max-bytes 1048576
python tools/local_data/noaa_ncei_access.py capture \
  --root /tmp/kfm-ncei-review-store --dataset daily-summaries \
  --stations USW00003928 --start 2024-01-01 --end 2024-01-02 --max-bytes 65536
```

`plan` and `products` perform no network or storage operation. Expected bytes
remain unknown. Mandatory `--max-bytes` is a stop limit, not a size estimate or
completeness promise. Default selection is Wichita, Dodge City, Topeka and
Goodland. Override `--stations` with at most 25 exact comma-separated US IDs.
Returned IDs, `, KS US` names and coordinates in the Kansas border envelope
are checked; a rectangle alone is not proof of administrative membership.

Choose `--elements` from the product list and `--units metric` or `standard`.
Original strings, attributes, flags and metadata stay in the exact payload.
Missing/flagged values are not repaired, zero-filled or quality-cleared. Normal
station metadata can differ from observation metadata; never silently replace
either location. Inspection does not normalize domain values or certify units.

For GSOM/GSOY, use `--start 2024-01-01 --end 2024-12-31` for a bounded example.
For daily normals, use `--start 2000-01-01 --end 2000-12-31` to select the full
leap-year calendar, with `--max-bytes 1048576`. For monthly/annual normals,
omit `--start`/`--end`; use the corresponding dataset name and a chosen byte cap.

Use the literal returned `capture_id` for offline replay:

```text
python tools/local_data/noaa_ncei_access.py replay --root <absolute-private-store> --capture-id <returned-sha256-id>
```

The absolute private-store path must be outside the repository. Directory
chains, permissions, symlinks, special files and immutable conflicts are checked
by existing file/store helpers. Choose a durable private location for history;
the `/tmp` example is disposable. Existing stores/captures remain intact.

Below that store, bytes live at
`data/quarantine/noaa-ncei-access/objects/sha256/<digest>/payload.json`, manifests
at `data/quarantine/noaa-ncei-access/runs/<capture-digest>/manifest.json`, and
receipts at `data/receipts/ingest/noaa-ncei-access/<capture-digest>/receipt.json`.
Payloads/manifests are read back before the receipt. Replay rebuilds the entire
manifest and inspection from exact bytes. SHA-256 proves locally captured byte
identity, not agreement with a provider checksum or approval.

Successful intake, including an empty result, returns
`QUARANTINED / REVIEW_REQUIRED`. Counts, periods and omissions never certify
coverage. Bounded structurally invalid responses are retained with failure
receipts; failed requests have no fabricated payload. Exit 0 means planned,
stored or replayed; exit 1 means an operation failed. Neither means admitted.

## Limits and failures

One request per capture; no automatic retry, redirect, paging or eviction.
JSON and identity encoding are required. Present Content-Length must match;
unknown lengths are streamed with one extra byte for overflow detection.
Maximum payload: 16 MiB, 10,000 rows. Socket timeout: 15 seconds. Checked wall
budget: 60 seconds; a socket read may finish beyond it before rejection.
Daily windows span at most 366 days; daily normals stay in one calendar year.

For long daily history, choose separate year/window captures and a cumulative
storage budget. This operator bounds each request, not total disk usage or a
scheduled collection. Older availability is not promised. There is no silent
splitting, truncated-result continuation or empty-as-complete fallback. HTTP
400/404/429 and other HTTP/network failures yield finite reasons without body
leakage. Stop on rate limiting/outage and retry later explicitly.
`KFM_NO_NETWORK=1` disables live transport and is enabled in CI.

## Admission, Site, and rollback

The approved `data/registry/sources/atmosphere/noaa_ghcnd.yaml` covers four
stations, PRCP/TMAX/TMIN and **by_station files**. It does not approve this API,
snow elements, normals or GSOM/GSOY. Existing NCEI templates do not clear those
product-specific reviews. Capture IDs use `noaa.ncei-access.<dataset>` without
changing active source descriptors.

Before these captures reach WORK/domain candidates or the map, require reviewed
endpoint/product descriptors, rights/sensitivity, units and native quality
semantics, station-history/time/coverage validation, exact normalization,
EvidenceBundle closure, release package/decision, serving conformance, owner
activation, correction and rollback. Existing daily-weather release tooling
does not accept these captures; API-to-map availability is not claimed.

The owner-private Site already has reviewed-weather read/admin routes. Preserve
its identity, audience, D1/R2 and water records. Browsers must read released
artifacts through governed APIs; never expose this private intake store or an
arbitrary URL proxy. No Site deployment or GoDaddy DNS mutation is required for
this connector setup.

```bash
KFM_NO_NETWORK=1 PYTHONDONTWRITEBYTECODE=1 python -m unittest discover -s connectors/noaa/tests -p 'test_*.py'
KFM_NO_NETWORK=1 PYTHONDONTWRITEBYTECODE=1 python -m unittest discover -s tests/tools -p 'test_ncei_access_operator.py'
```

Rollback: stop invoking capture and revert the reviewed connector/operator,
tests, CI and documentation commit. Retain immutable evidence/receipts. There
is no active pointer, admitted source, released package, DNS or storage migration
to undo. Evidence removal is a separate retention decision.
