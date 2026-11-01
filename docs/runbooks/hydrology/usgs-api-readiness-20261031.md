# USGS Water API readiness — 2026-10-31

**Status:** CONFIRMED bounded source inspection; NEEDS VERIFICATION live and installed-runtime acceptance. This checkpoint supports read-only verification of discharge parameter `00060` at Arkansas River at Arkansas City, Kansas, `USGS-07146500`. It grants no source admission, activation, release, deployment, or publication authority.

## What the service notice changes

The official [USGS WaterServices degradation notice](https://waterdata.usgs.gov/blog/wdfn-waterservices-degradation/) was checked on October 31, 2026. It reports an October 27 update and the following schedule:

| USGS calendar date | Announced WaterServices behavior |
|---|---|
| 2026-11-16 | Two-second delay per request |
| 2027-01-11 | Ten-second delay per request |
| 2027-01-25 | Thirty-second delay per request |
| 2027-01-27 | Redirect to the notice for approximately 24 hours; regular service expected January 28 |
| 2027-02-01 | Sixty-second delay per request |
| 2027-02-15 | Redirect to the notice for approximately 48 hours; regular service expected February 17 |
| 2027-02-22 | Permanent retirement; redirect to the earlier decommissioning notice |

These are announced dates, without exact activation times or time zones. USGS says delay timing and duration may change. Recheck the notice before relying on the schedule. This is an API-change checkpoint, not evidence of a new discharge revision, quality change, or reporting gap.

The [USGS migration guide](https://api.waterdata.usgs.gov/docs/ogcapi/migration/) maps latest readings to `latest-continuous`, historical instantaneous readings to `continuous`, daily aggregates to `daily`, and station metadata to `monitoring-locations`. All are under `https://api.waterdata.usgs.gov/ogcapi/v1/collections/`. Modern responses contain one feature per observation; they are not a drop-in replacement for legacy grouped WaterServices JSON. Approval status and other qualifiers are distinct fields. Missing values remain null.

## Bounded repository findings

The two compositions were inspected separately. No deployment or current PC checkout was inferred from either branch.

| Composition and exact source | CONFIRMED in the inspected bytes | Limit |
|---|---|---|
| [main pilot capture](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/5af905d8bd94773ab43fcf7a137b0484c450edf2/connectors/usgs/water_data/pilot_capture.py) | Fixed modern `monitoring-locations` and `continuous` requests; bounded transport; allowlisted host and scoped pagination | The fixed pilot stations are `USGS-06892518` and `USGS-07156900`, not the watched station |
| [main period-of-record discovery](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/5af905d8bd94773ab43fcf7a137b0484c450edf2/tools/local_data/discover_water.py) | Modern `time-series-metadata` requests; metadata discovery only | Period envelopes do not establish uninterrupted observations |
| [main historical-water replay](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/5af905d8bd94773ab43fcf7a137b0484c450edf2/tools/local_data/historical_water.py) | Reads pinned captured material and replays normalization offline | Cannot establish current provider availability |
| [hosted Explorer streamflow route](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/8cf26ab5fceed437652641f6091cd9ea4b28a045/app/api/hydrology/streamflow/route.ts) | Modern station, latest, continuous, and daily collections; fixed upstream origin and path allowlist; manual redirects; approval and qualifier parsing | Source inspection does not establish deployed behavior |
| [hosted ingestion source](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/8cf26ab5fceed437652641f6091cd9ea4b28a045/server/ingestion-sources.mjs) | Modern `latest-continuous` capture; manual redirects; HTTP 200 and JSON media-type checks; original entity digest | Hourly Kansas latest-value capture is not a full station-history comparison |
| [main cutover assessment contract](../../../contracts/domains/hydrology/usgs_water_api_cutover.md) | Explicitly fixture-only, no-network assessment | A `CUTOVER_CANDIDATE` does not prove a live migration, activation, or release |

**Conclusion:** No WaterServices runtime dependency was found in these inspected paths. A replacement adapter is not justified by this evidence. This is not a repository-wide absence claim. Legacy URLs in documentation or synthetic SourceDescriptor fixtures are not, by themselves, executable dependencies. Preserve historical evidence rather than bulk-rewriting those URLs.

The main snapshot is `5af905d8bd94773ab43fcf7a137b0484c450edf2`; the hosted development snapshot is `8cf26ab5fceed437652641f6091cd9ea4b28a045`. Neither implies parity with the other composition or the deployed site.

## Read-only verification procedure

1. Record the actual installed and deployed commit, the called route or capture entry point, and the provider URL from its existing receipt. Keep the two compositions separate. Search that exact checkout for `waterservices.usgs.gov`, `waterdata.usgs.gov/nwis`, `readNWIS`, and `dataretrieval.nwis`; classify executable callers separately from docs, fixtures, and preserved captures. Stop a cutover claim if the actual consumer is unknown.
2. Read the official [station page](https://waterdata.usgs.gov/monitoring-location/USGS-07146500/) and record any notice with its retrieval date. Failure to retrieve the page leaves notice coverage UNKNOWN; it does not mean no notice exists.
3. From an authorized network, make bounded GET requests to the three modern probes below. Preserve the exact request URL, HTTP status, media type, retrieval time, entity bytes, and SHA-256 in a new private diagnostic location. Do not overwrite existing receipts or captures. Refuse redirects, non-200 responses, non-JSON media types, malformed payloads, excessive bodies, or unexpected identity. A successful HTTP request alone is insufficient.
4. Check station and parameter identity, units, time-series identity, statistic, timestamps or date convention, approval status, qualifiers, nulls, duplicates, record counts, and paging. A `next` link means incomplete coverage; do not infer no gaps or complete parity from one page. Keep retrieval time separate from observation and provider-revision time.
5. To detect revisions, re-fetch the **exact original query interval and filters recorded by the existing baseline**, and compare all corresponding records. New rolling-window records are not revisions. Added filters create a different query scope; establish a separate baseline rather than treating it as an identical replay.
6. Report material differences with old and new receipt references, affected records, and KFM validation impact. Distinguish first-seen qualifiers from changed qualifiers, null values from absent records, provider gaps from failed acquisition, and provisional-to-approved transitions from value revisions. Do not overwrite the earlier evidence.
7. Exercise the installed KFM reader with the watched station and the same interval, within its supported query contract. Retain the resulting provenance and compare it to the provider response. Source-code inspection and direct provider probes cannot substitute for this installed-runtime check.

### Small fixed probes

These deliberately short intervals are new diagnostic scopes. They are not replacements for the previously retained watch baseline. The continuous and daily intervals have different temporal meanings; never compare daily means to instantaneous samples as if they were the same observations.

| Purpose | Fixed modern GET |
|---|---|
| Station identity | [monitoring-locations](https://api.waterdata.usgs.gov/ogcapi/v1/collections/monitoring-locations/items?f=json&agency_code=USGS&monitoring_location_number=07146500&limit=2) |
| One hour of discharge samples | [continuous](https://api.waterdata.usgs.gov/ogcapi/v1/collections/continuous/items?f=json&monitoring_location_id=USGS-07146500&parameter_code=00060&limit=100&datetime=2026-10-30T12%3A00%3A00Z%2F2026-10-30T13%3A00%3A00Z) |
| Three daily mean dates, statistic `00003` | [daily](https://api.waterdata.usgs.gov/ogcapi/v1/collections/daily/items?f=json&monitoring_location_id=USGS-07146500&parameter_code=00060&statistic_id=00003&limit=10&datetime=2026-10-28%2F2026-10-30) |

Use the existing client's response-size and timeout limits. Honor provider throttling and `Retry-After`; do not retry in a tight loop. See [USGS API-key guidance](https://api.waterdata.usgs.gov/docs/ogcapi/keys/) before repeated operational queries. Credentials, if needed, remain server-side and outside URLs, committed evidence, and logs.

### Acceptance and stop conditions

| Condition | Disposition |
|---|---|
| Installed consumer and successful modern response agree on identity, temporal meaning, values, units, quality fields, and bounded completeness | Record a bounded verification result for that exact consumer, query, and retrieval |
| Redirect, HTML, timeout, throttle, schema change, ambiguous series, or incomplete paging | Record failed or incomplete acquisition; no zero, stale, legacy, or synthetic substitution |
| Value, unit, approval, qualifier, series, or coverage difference against an identical prior query | Hold affected validation conclusions for review; preserve both versions |
| First retrieval or inaccessible earlier receipt | Establish only a first-seen baseline; no revision claim |
| Source approval changes | Preserve USGS status verbatim; independently evaluate affected KFM evidence and release gates |

A six-hour gap threshold, if used by the watch, is an operational alert rule, not a promise that this station samples on a fixed schedule. Daily-gap checks must examine the requested date window and the intended statistic. Neither a provider's Approved status nor a passing fixture assessment approves a KFM release.

## Open verification and next action

**NEEDS VERIFICATION:** live modern responses, station-notice coverage, installed/deployed consumer identity, full baseline replay, runtime error handling, and any external scripts outside the inspected paths. No provider observations were successfully retrieved during this authoring session: direct endpoint retrieval was unavailable, and the shell connectivity check could not resolve raw.githubusercontent.com. No new station-data baseline, absence-of-gap result, or no-change claim is established here.

**PROPOSED next action:** complete the bounded installed-reader and identical-baseline replay above before November 16. If an executable legacy caller is found, make a separate scoped adapter change with query/identity/quality parity, negative response tests, migration evidence, and rollback. The fixed two-station pilot is not expanded by this note.

The older [source-refresh runbook](./SOURCE_REFRESH_RUNBOOK.md) records an August evidence snapshot. Its statements about absent transport or pipeline implementation must not override the later exact-source findings above. Its authority, policy, review, and release prerequisites remain distinct and must be checked against current governing records before an operational transition.

## Placement, validation, and rollback

Owning root: `docs/`. Accepted [ADR-0029](../../adr/ADR-0029-adopt-directory-governance-standard-v2.md) adopts [Directory Rules v2](../../doctrine/directory-rules.md); human operational guidance belongs in the existing `docs/runbooks/hydrology/` lane. This note adds no contract, schema, source registry, policy, proof, receipt authority, release home, or production dependency. The authoring receipt remains in the existing `data/receipts/generated/` lane.

Validation for a documentation change is limited to Markdown structure, tracked-path/navigation checks, pinned-source review, and authoring-receipt shape and artifact hashes. Runtime, provider, full-suite, pre-commit, and deployment checks are separate and must not be reported as passing unless run.

Filename correction: the first checkpoint used `USGS_API_READINESS_20261031.md`. Its uppercase spelling introduced `KFM-TOPO-001` drift in PR #5660. The canonical spelling is now `usgs-api-readiness-20261031.md`, under Directory Rules §13.2. The water-pilot navigation is updated with the rename. The original generated receipt is preserved unchanged and binds the original artifacts in merged ancestor `1bdf9c56fc561f637fb7cd54dd17344df62e6d08`; replay it against that ancestor with the native validator's `--artifact-git-ref` option. This spelling correction does not expand the topology baseline or grant operational authority.

Rollback: revert this documentation change and its navigation/authoring receipt. Preserve all earlier data, baseline receipts, approval records, and release artifacts. A documentation rollback does not undo any operator action.
