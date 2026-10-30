# Field view: IEM source verification — 2026-10-30

**Status:** confirmed real upstream contract and two historical computations;
corrective source candidate. Hosted release acceptance remains incomplete.

## Scope and source identity

Inspected hosted branch `a0-hosted-ai-web-20261017` at
`372c052a97a975b8b3401f9230e97da522cffda3`, including merged PRs
[#5618](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/5618),
[#5619](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/5619),
[#5621](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/5621),
[#5622](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/5622), and
[#5623](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/5623).
The last adds frost dates and extracts shared station discovery; those dependent
paths were included in regression validation. No open PR targeting the hosted
branch appeared in the initial overlap check.

The shell executor could not resolve upstream hosts. The alternate Node runtime
retrieved HTTP 200 responses from IEM: the 69-feature Kansas ASOS catalog,
Salina's 214 daily rows for April–October 2024, Goodland's corresponding 214 rows,
and a three-day all-missing sample for retired Benton station `1K1`. These are
actual source responses, not mocked acquisitions. Tests replay these captured
bytes deterministically; their transport stubs are not live-provider evidence.
See [fixture receipts](../tests/fixtures/iem/provenance.json) for exact URLs,
retrieval times, byte sizes and SHA-256 digests.

## Confirmed contract

- [Daily form](https://mesonet.agron.iastate.edu/request/daily.phtml?network=KS_ASOS)
  and [backend documentation](https://mesonet.agron.iastate.edu/cgi-bin/request/daily.py?help):
  inclusive start/end dates; `network=KS_ASOS`; station identifiers such as
  `SLN` and `GLD`, not assumed ICAO-prefixed identifiers; Fahrenheit temperatures
  and inches of liquid-equivalent precipitation. Query `var` explicitly selects
  `max_temp_f,min_temp_f,precip_in`; station/day/network columns accompany them.
  Default missing values are `None`; `na=M` is supported. Empty and `M` cells
  also represent missing observations.
- [Station GeoJSON](https://mesonet.agron.iastate.edu/geojson/network/KS_ASOS.geojson):
  `sid`, `sname`, point geometry, `network`, `state`, `tzname`, `archive_begin`,
  `archive_end`; closed stations are included. Salina is `America/Chicago`,
  Goodland `America/Denver`. `1K1` ended 2022-12-29, yet its 2024 query still
  returns dated rows whose observation fields are all `M`.
- Trace precipitation is numeric `0.0001`, a categorical sentinel rather than
  measured depth. The captured Salina and Goodland rows contain this value.
- IEM combines local-calendar calculations and explicit reported totals.
  Airport daily totals typically cover local standard-time days, 01:00–01:00
  during daylight time. Dates cannot be interpreted as UTC midnight boundaries.
- IEM asks clients to request sequentially with a two-second gap. The official
  [implementation](https://github.com/akrherz/iem/blob/main/pylib/iemweb/request/daily.py)
  documents this policy, the column mapping and inclusive query predicate.

## Independent historical comparison

`python3 tests/iem_reference_totals.py` uses Python's CSV reader and Decimal
arithmetic, without importing application calculation code. The heat method is
also checked against the three worked examples in
[Purdue Extension's modified corn GDD explanation](https://www.agry.purdue.edu/ext/corn/news/timeless/HeatUnits.html).

| April 1–October 31, 2024 | Valid days | Unrounded °F-days | App display | Measured precipitation | Trace days |
|---|---:|---:|---:|---:|---:|
| Salina (`SLN`) | 214 | 4426.4 | 4426 | 15.81 in | 28 |
| Goodland (`GLD`) | 214 | 3748.6 | 3749 | 8.28 in | 17 |

The built local candidate's HTTP routes fetched live IEM responses and returned
these same displayed heat totals, measured precipitation and trace counts, with
zero missing/pending days and the correct station timezones. The original GDD
arithmetic was correct for these samples and remains unchanged. Degree days
are rounded only after summation. Trace counts are not added to measured inches.

## Corrections and limits

1. Exclude station archives that do not overlap the requested interval; retain
   retired stations when querying their historical years. Validate network,
   Kansas identity, finite point coordinates, timezone and archive bounds.
2. Bind CSV records to the requested station/network/date range. Refuse duplicate
   dates, malformed columns and invalid calendar dates. Missing/nonfinite values,
   negative precipitation and inverted temperature pairs cannot become readings.
3. Preserve trace days, use the label precipitation instead of rain, and show
   partial totals explicitly. Temperature absence does not suppress valid
   precipitation. Neither absent rainfall fields nor failed requests imply zero.
4. Distinguish missing due dates from dates not yet due. Conservatively include
   yesterday only after 02:00 station-local time. This guards incomplete days,
   but does not certify upstream arrival, subdaily completeness or quality control.
5. Cache only complete elapsed seasons, for one day in browser and shared caches.
   `v=2` avoids older cached calculations; old responses without rainfall remain
   readable and say precipitation is unavailable. Validate response consistency.
6. Share a bounded sequential daily-request queue between GDD, frost and precipitation-comparison routes,
   coalescing identical in-flight requests and recovering after errors. This is
   per-process protection; multiple processes behind one egress address require
   an egress-wide rate limiter. No distributed-rate compliance is claimed.

The fixed season is a comparative corn-method heat index, not an accumulation
from planting, a maturity forecast for arbitrary USDA classes, or a field sensor.
A nearby airport can differ substantially from a field. The archive-overlap
filter does not prove usable observations; the app reports missing coverage
rather than silently switching to a farther station. Two verified stations do
not establish statewide climatological quality. IEM historical data may change.

## Validation and deployment boundary

The unmodified base passed 21 focused GDD/frost tests. Corrective validation
includes captured-source fixtures, independent Decimal arithmetic, malformed
identity/date cases, missing and trace values, station eligibility, incomplete
seasons, DST cutoffs, legacy caches, request throttling, errors and dock states.
Exact candidate build/type/full-suite results belong in the accompanying PR;
unrun browser/hosted checks must not be inferred from unit or component tests.

On 2026-10-30, GoDaddy app `urdng3v1vk` separately reported **Preview** and
**Published** at `7b27ffaaf66b29d4ba0761f335135855109d8f9e` (PR #5619), with
Preview out of sync with GitHub. Preview startup and its Explorer homepage were
observed. Direct Preview API navigation was blocked by the browser client. A
subsequent normal Field-view click at 38.073 N, 98.537 W for 2024 displayed
4,321 GDD from Lyons, 40 km away, with 214 days read and no precipitation line.
That live rendered result was observed but not independently recomputed; it
confirms the older interface, not acceptance of this candidate. The public Salina API request
returned HTTP 200, 4426 degree days, 214 read and zero missing, with **no rainfall
fields**. This confirms the earlier published implementation, not this candidate.
The verification agent performed no merge, Preview update or public publication.

## Placement, risk and rollback

Directory Rules.pdf was inspected as source lineage. Accepted
[ADR-0029](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/main/docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md)
and its adopted `docs/doctrine/directory-rules.md` govern responsibility placement.
This standalone hosted composition retains its existing `app/` implementation,
`tests/` verification and `docs/` explanatory homes; public weather fixtures use
its established `tests/fixtures/` convention. They are test inputs, not catalog,
release or published-data authority. No new root, policy, registry or lifecycle
store is created; no main-repository migration or source admission is implied.

Risk: stricter validation can turn provider drift into an unavailable reading;
that is preferable to misattribution. Conservative day closure delays readings.
Revert the bounded application/test/docs commit to roll back; retain the evidence
record. Reverting `v=2` can expose prior cached results until their TTL expires,
so a rollback should use a new cache generation if calculations change again.
Deployment requires separate owner authorization and exact deployed-head checks.

## Concurrent branch advance and reconciliation

PR #5624 landed as `a4ed9d23660717fe610f3c343a44d9109a7353c2` while this
candidate was being opened for review. It adds a ten-year precipitation
comparison and another consumer of the shared helpers. Its station mocks,
parallel requests and indefinite station-year cache conflicted with the verified
contract. The follow-up incorporates that change and routes its requests
through the same station eligibility, CSV identity checks, day cutoff and
sequential queue. Complete cache entries expire after a day; all-missing
observations produce no value, and trace counts remain separate. The interface
calls the comparison an earlier-year average and explicitly distinguishes it
from a standard 30-year climate normal. This dependency reconciliation does not
claim live acceptance of an eleven-year historical comparison; that remains a
separate scientific sampling requirement. Original-snapshot results above are
not evidence that the later merge candidate passed; see the PR for the final
integration checks and any environment limits.


PR #5626 was merged externally as `439f5d4de3a9b462ddcf6d92af11eea3cea01d00`
before reconciliation finished. The follow-up is based on that exact commit,
including the intervening unrelated welcome-screen PR #5627. It changes only
precipitation-comparison integration, its shared-source description, tests and
behavior-linked documentation. The earlier candidate's review does not approve
these new changes.

The initial `512f16c` candidate passed 2,328 tests with 24 skipped and no failures.
The subsequent full-suite attempt in a newly restricted executor was not green:
2,232 passes, 72 reported failures, 24 skips, plus files that could not start or
timed out. A frost-message regression found in that attempt was corrected and
its nine tests passed; two built-route failures disappeared after the concurrent
build completed. Socket-based failures explicitly report `listen EPERM`.
Seven other process-related failing/timed-out files were replayed against the
unmodified #5624 content and reproduced the same failures/timeouts. This does
not establish a passing full suite on the follow-up. Its final changed-area,
build, type and lint results are recorded in the accompanying PR. Hosted
integration and multi-process request limiting remain open verification.


Final follow-up changed-area verification on source based on `439f5d4`:
46 weather tests, 14 crop tests and 37 welcome-screen tests passed (97 total,
zero failures/skips); production build and TypeScript check passed; changed
application-file ESLint had zero errors and one existing image warning. The
independent Decimal reference passed again. These bounded results do not
supersede the full-suite and hosted limitations above.
