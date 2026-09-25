<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/runbooks/usgs-earthquake-live-history
title: USGS recent and historical earthquake candidate workflow
type: runbook
version: v0.1.0
status: proposed; offline-implemented; source-activation-held
owners: ["@bartytime4life"]
created: 2026-09-23
updated: 2026-09-25
policy_label: public; context-only; not-alerting; no-source-admission
owning_root: docs/
responsibility: Explain the bounded offline USGS query and snapshot helpers and the remaining transport, reconciliation, source, and Site acceptance gates.
truth_posture: CONFIRMED offline helper behavior; PROPOSED live integration; NEEDS VERIFICATION provider-to-map acceptance
[/KFM_META_BLOCK_V2] -->

# USGS recent and historical earthquake candidate workflow

## Delivery boundary

This change implements [USGS planning and parsing helpers](../../connectors/usgs/src/usgs/earthquake.py),
[synthetic tests](../../connectors/usgs/tests/test_earthquake.py), and a
[dedicated offline CI workflow](../../.github/workflows/usgs-earthquake-offline.yml).
There is no HTTP client, schedule, persistence, active route, source activation,
renderer change, or deployment. A request plan is not a performed request; a
parsed candidate is not an admitted source or a complete catalog.

The existing [USGS product pointer](../sources/catalog/usgs/earthquake-catalog.md)
remains the source-family reference. This runbook neither duplicates nor replaces
SourceDescriptor, SourceActivationDecision, SourceArtifact, IngestReceipt,
EvidenceBundle, policy or release authority. New helpers live in the existing
USGS implementation package; no competing earthquake connector root is created.

The [app-local HTTP 204 decoder](../../apps/kansas-frontier-matrix-explorer/docs/usgs-earthquake-response-candidate.md)
from PR #4667 is a different consumer boundary. Its merge did not wire a live
caller. Neither that TypeScript helper nor the active Site is overwritten here.

## Source selection

Use the USGS [summary feeds](https://earthquake.usgs.gov/earthquakes/feed/v1.0/geojson.php)
for recent context, as recommended by the
[event service](https://earthquake.usgs.gov/fdsnws/event/1/). Use the event service
for explicit older intervals. The map landing page is a human interface, not the
machine API. USGS [ComCat](https://earthquake.usgs.gov/data/comcat/) aggregates
contributor solutions; an origin, magnitude estimate, felt report, ShakeMap or
PAGER product must retain its own role.

The helper supports the documented hour/day/week/month feed windows and the
all/1.0/2.5/4.5/significant feed families. The default is all/day; magnitude and
significance selection must be visible to users. Summary publication cadence
is provider metadata, not a promise of immediate detection or delivery.

[KGS and Berkeley qualification](../intake/exploratory/kgs-berkeley-seismic-source-map.md)
provides the Kansas historical/local and Northern California comparison lanes.
Those payload formats are not accepted by the USGS-only parser.

## Run the code without network access

From the repository root:

```bash
PYTHONDONTWRITEBYTECODE=1 python -m unittest discover \
  -s connectors/usgs/tests -p 'test_earthquake.py' -v
```

Example request planning, with no download or filesystem mutation:

```bash
PYTHONPATH=connectors/usgs/src PYTHONDONTWRITEBYTECODE=1 python - <<'PY'
from usgs.earthquake import history_windows, live_url
print(live_url(period="week", level="all"))
for window in history_windows("1969-12-01T00:00:00Z", "1970-02-01T00:00:00Z"):
    print(window.start, window.end_exclusive, window.count_url, window.query_url)
PY
```

For bytes acquired by a separately authorized transport, call
`parse_snapshot(body, status=..., source_url=..., retrieved_at=...)`.
Record the actual retrieval time; do not replace it with event origin time or
feed generation time. The source URL is an intended-origin check, not
cryptographic authentication of supplied bytes. `parse_snapshot` does not fetch
`source_url`, metadata URLs, event URLs, detail links, or arbitrary product links.

## Implemented behavior

| Helper | Bounded behavior |
|---|---|
| `live_url` | Selects one of 20 fixed HTTPS summary locators; no arbitrary provider URL. |
| `history_windows` | Finite, ascending intervals; explicit location/time/type; count and first-page query plans; 1-31 days per slice, at most 2,400 slices, 1-20,000 events per page. |
| `parse_snapshot` | Byte, cardinality, outer metadata, identity, point, scalar and JSON checks; immutable records; exact response-byte digest; deterministic normalized-feature digest. |
| `select_earthquakes` | Exact earthquake-type selection, context-envelope filter, half-open time ownership; leaves the original snapshot intact. |

The context envelope is `[-102.1, 36.9, -94.5, 40.1]` in
west/south/east/north order. This is a proposed Kansas-area query extent, **not**
a legal state boundary, county assignment, or assertion of complete coverage.
Use separately governed boundary geometry for state/county joins.

Unknown source feature fields remain in `raw_feature_json`; this is internal
candidate content, not public-safe HTML or an export. A separate public
projection must apply disclosure and field controls. Feature hashes describe
this helper's normalized JSON encoding, not a new canonical KFM identifier or
an RFC 8785 claim. Preserve the original body bytes with their SHA-256 externally.

Pre-1970 millisecond timestamps, zero/negative magnitudes, negative depths, and
null optional values are not silently changed to zero or discarded. Magnitude
method, provider review status, event type, update time and aliases survive.
The parser checks representational validity, not scientific accuracy.

Only a USGS event query explicitly requesting `nodata=204` can interpret an
empty 204 body as zero returned records. A 204 summary response, malformed
body, unexpected status, duplicate key, identity collision or count mismatch
fails. Authentication, throttling, network errors and HTML pages never become
an all-clear. A failed snapshot must not replace previous data with an empty success.

## Historical completeness and corrections

USGS requests include both endpoints. Planned neighboring requests therefore
share a boundary timestamp; assign returned records to `[start, end_exclusive)`
before combining windows. Do not subtract arbitrary floating-point epsilons.
Records exactly at the final endpoint belong to the next interval.

A response at the requested page limit sets `query_limit_reached`; it is not
accepted as complete. The count plan deliberately omits `limit` and `offset`.
Count execution, bounded adaptive partitioning, offset pagination, same-time
saturation handling, and before/after mutation checks are **not implemented**
in this slice. Do not activate bulk acquisition until they are tested. A short
page is not by itself proof of historical completeness either.

A live service can change while pages are read. Preserve exact URLs, response
bytes, page/slice boundaries, retrieval intervals, status, provider versions,
counts, missing slices and a terminal outcome. Require a stable reconciliation
pass or mark a changing result partial/held; never loop without a finite budget.

Keep each `(provider, event ID, provider update, body/feature digest)` candidate
version. USGS aliases are evidence of association, not a license to merge KGS
or NCEDC records by proximity. Shared aliases within a response fail for review.
Alias changes, conflicting origins, deleted events and superseded products need
an explicit, retained reconciliation record. Feed expiry is not event deletion.
The parser does not implement tombstone handling or historical reconstruction.

Distinguish two questions: "What is the catalog's current account of an old
event?" and "What was known at that time?" A query executed now only establishes
the former, unless a dated archive provides the earlier state. Observation-rate
plots require catalog/network coverage and magnitude-completeness qualification;
raw counts alone are not a hazard forecast or an induced-seismicity finding.

## Next integration gates

Before live acquisition: bind the existing source descriptor/activation and
rights decisions, exact query policy, request budget, deadlines, allowlisted
redirect/media behavior and existing connectors-core transport/artifact handoff.
Reject unapproved provider changes. Retain immutable RAW/QUARANTINE candidates
and real IngestReceipts through established storage; do not invent parallel
lifecycle, schema or receipt roots. No credentials or requester contact details
belong in these query plans, fixtures, URLs or receipts.

Before a map change: obtain the current Site source and saved predecessor;
prove the governed response to the same event/list selection and Evidence Drawer.
Test populated -> empty -> populated, failure with stale retention, revised IDs,
filter changes, abort/late responses, unsupported history and explicit retry.
Keep observation time, update time, retrieval time, units and actual source
status visible. Test real geometry rendering and selection clearing, not just a
successful response or a list of timestamps. No safety notification or automatic
provider subscription follows from this work.

Before acceptance: run exact-candidate CI, independent source/security review,
authenticated browser/WebGL checks, correction and rollback rehearsal. Keep
the current [contributor guidance](../../CONTRIBUTING.md) and #4228's
Stage 1A accepted / Stage 1B HOLD /
Stage 2 unauthorized boundaries. No merge, release or deployment is authorized
by this runbook.

## Validation and rollback

Local standard-library tests are synthetic. Hosted workflow results must be
read back at the delivered head and actual test-merge commit; a workflow file
alone is not passing evidence. The container could not resolve external hosts,
so no local provider request, complete locked checkout or live replay is claimed.
A web read of the official past-hour feed returned a GeoJSON collection during
research; that is not a connector run, Kansas completeness or active-Site proof.

Rollback before integration is to abandon the draft branch. After a separately
approved integration, review an inverse of the helper/tests/workflow/docs while
retaining generated-receipt history. No source, Site, storage or deployed-state
rollback is exercised by removing this offline candidate slice.
