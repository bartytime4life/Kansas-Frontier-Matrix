# USGS Water API readiness — 2026-10-31

**Status:** CONFIRMED bounded source inspection, offline diagnostic tests and saved-capture replay; NEEDS VERIFICATION fresh provider comparison and installed-runtime acceptance. This checkpoint supports read-only verification of discharge parameter `00060` at Arkansas River at Arkansas City, Kansas, `USGS-07146500`. It grants no source admission, activation, release, deployment, or publication authority.

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

## Offline comparison of retained pages

The [captured-observation comparator](../../../tools/ingest/hydrology_watch/usgs_observation_compare.py) makes the field-level part of the procedure reproducible without network access. It is fixed to station `USGS-07146500`, parameter `00060`, continuous statistic `00011` or daily mean `00003`. This is a diagnostic inspector in the existing watcher-helper lane, not a connector, canonical normalizer, source-admission gate, scheduled job, or release component.

From the monorepo checkout:

```bash
python3 tools/ingest/hydrology_watch/usgs_observation_compare.py \
  /absolute/path/PRIOR.json /absolute/path/CURRENT.json --collection continuous
```

Use `--collection daily` for daily means. Inputs can be raw single-page FeatureCollections or the retained watch export whose `evidence_files` contain `continuous-0.raw` / `daily-0.raw` and matching receipt JSON. For the export, the tool checks the stored entity's SHA-256, byte count, HTTP-200 claim, query and row count against the retained receipt. The comparison uses the original page, not its generated summary. A receipt match establishes local consistency; it does not authenticate USGS transport or approve source admission.

The tool refuses different query windows or filters, foreign stations/parameters, unsupported statistics, pagination, page caps, ambiguous identities, invalid dates/values, incomplete fields, and malformed inputs. It compares numeric values without rounding, retains nulls, separates unit/approval/qualifier/method changes, and reports series changes as additions/removals. Provider `last_modified` refreshes are reported separately and do not alone trigger a measurement-revision signal. Provider response clocks remain separate from observation times; when both response clocks exist, reversed prior/current order is refused. Geometry is neither interpreted nor emitted. Numeric representation changes and feature order do not create value revisions.

Continuous coverage diagnostics include interior and query-edge holes of at least six hours. Daily coverage diagnostics count absent dates over each represented series' requested window, including edges. These are holes in the captured page, not independently established station outages. Null values are counted separately. Source periods of record and expected sampling cadence remain independent verification inputs.

The input bound is 8 MiB per file, 10,000 rows, four represented series and bounded per-record fields. Reports retain full counts and hashes while limiting details to 100 entries. Static symlink ancestors and non-regular files are refused. Files must remain operator-controlled; these checks are not a sandbox against another process racing filesystem changes.

The stdout diagnostic uses `ANSWER` for a completed captured-field comparison, with decision `REVIEW` or `NO_DIFFERENCE_IN_CAPTURED_FIELDS`; this answers only the file-comparison question. Source authority, admission and release remain unevaluated. `ABSTAIN` means incompatible or incomplete evidence; `ERROR` means invalid input. Exit codes are respectively 0, 1 and 2. A `REVIEW` result still exits 0 because comparison completed; consumers must inspect the decision. Matching fields do not mean current conditions, gap-free coverage, hydrologic insignificance, or KFM release approval.

### Capture the identical query on an authorized machine

The helper can print the validated public query without fetching it. This Bash example uses a new private temporary directory; edit only `baseline_path` to select your retained file. It does not overwrite that baseline or any KFM data store.

```bash
baseline_path=/absolute/path/USGS-07146500-watch-baseline-2026-10-31.json
(
  set -euo pipefail
  umask 077
  probe_dir=$(mktemp -d "${TMPDIR:-/tmp}/kfm-usgs.XXXXXX")
  python3 tools/ingest/hydrology_watch/usgs_observation_compare.py \
    "$baseline_path" --collection continuous --print-query > "$probe_dir/query.txt"
  IFS= read -r source_url < "$probe_dir/query.txt"
  curl --proto '=https' --fail --silent --show-error --max-time 30 \
    --max-filesize 8388608 --max-redirs 0 \
    --dump-header "$probe_dir/headers.txt" --output "$probe_dir/current.json" \
    --write-out '%{http_code}\t%{content_type}\n' "$source_url" > "$probe_dir/transfer.tsv"
  IFS=$'\t' read -r http_status content_type < "$probe_dir/transfer.tsv"
  [ "$http_status" = 200 ] || { echo "USGS HTTP status rejected" >&2; exit 1; }
  case "$content_type" in
    application/json|application/json\;*|application/geo+json|application/geo+json\;*) ;;
    *) echo "USGS media type rejected" >&2; exit 1 ;;
  esac
  python3 tools/ingest/hydrology_watch/usgs_observation_compare.py \
    "$baseline_path" "$probe_dir/current.json" --collection continuous > "$probe_dir/comparison.json"
  printf 'Private diagnostic directory: %s\n' "$probe_dir"
)
```

Run a separate invocation with `daily` at both collection arguments for daily values. No redirects are followed. Retain the query, headers, transfer metadata, entity and comparison together; do not commit the observation files or headers. The comparison report hashes its captured entity. HTTP failures, incomplete results and comparison refusals must remain visible. This example performs no retry, key enrollment, source admission, scheduling, data promotion, release or publication. Repeated operational requests still require provider rate-limit and server-side credential discipline.

Focused local verification:

```bash
python3 -m unittest discover -s tests/ingest/hydrology_watch -p test_usgs_observation_compare.py -v
```

The dedicated read-only CI workflow runs synthetic cases and authoring-receipt validation. It does not fetch USGS observations; runner-wide network isolation is not claimed. Saved-capture replay during authoring used the original 2,871 continuous and 400 daily observations and their retained entity digests. That is replay compatibility, not a fresh provider comparison, authenticated capture, or installed-reader acceptance.


## Open verification and next action

**NEEDS VERIFICATION:** live modern responses, station-notice coverage, installed/deployed consumer identity, fresh identical-baseline comparison, installed-runtime error handling, and any external scripts outside the inspected paths. No provider observations were successfully retrieved during this authoring session: direct endpoint retrieval was unavailable, and the shell connectivity check could not resolve raw.githubusercontent.com. No new station-data baseline, absence-of-gap result, or no-change claim is established here.

**PROPOSED next action:** complete the bounded installed-reader and identical-baseline replay above before November 16. If an executable legacy caller is found, make a separate scoped adapter change with query/identity/quality parity, negative response tests, migration evidence, and rollback. The fixed two-station pilot is not expanded by this note.

The older [source-refresh runbook](./SOURCE_REFRESH_RUNBOOK.md) records an August evidence snapshot. Its statements about absent transport or pipeline implementation must not override the later exact-source findings above. Its authority, policy, review, and release prerequisites remain distinct and must be checked against current governing records before an operational transition.

## Placement, validation, and rollback

Owning root: `docs/`. Accepted [ADR-0029](../../adr/ADR-0029-adopt-directory-governance-standard-v2.md) adopts [Directory Rules v2](../../doctrine/directory-rules.md); human operational guidance belongs in the existing `docs/runbooks/hydrology/` lane. This note adds no contract, schema, source registry, policy, proof, receipt authority, release home, or production dependency. The authoring receipt remains in the existing `data/receipts/generated/` lane. The offline helper uses the existing `tools/ingest/hydrology_watch/` implementation precedent, its regressions use `tests/ingest/hydrology_watch/`, and read-only CI uses `.github/workflows/`. The broader watcher-sublane ownership conflict remains PROPOSED / NEEDS VERIFICATION; this bounded addition retains the existing helper lane and does not create a parallel `tools/watchers/` implementation.

The original documentation-only checkpoint used Markdown structure, tracked-path/navigation checks, pinned-source review, and authoring-receipt shape and artifact hashes. The offline extension adds focused executable tests, saved-page replay, and a dedicated CI workflow. Full-suite, provider, installed-runtime, pre-commit and deployment checks remain separate and must not be reported as passing unless run.

Filename correction: the first checkpoint used `USGS_API_READINESS_20261031.md`. Its uppercase spelling introduced `KFM-TOPO-001` drift in PR #5660. The canonical spelling is now `usgs-api-readiness-20261031.md`, under Directory Rules §13.2. The water-pilot navigation is updated with the rename. The original generated receipt is preserved unchanged and binds the original artifacts in merged ancestor `1bdf9c56fc561f637fb7cd54dd17344df62e6d08`; replay it against that ancestor with the native validator's `--artifact-git-ref` option. This spelling correction does not expand the topology baseline or grant operational authority.

The later spelling-correction receipt remains historical as well: its original artifact bytes are in merged ancestor `5aeeadf64f35aedc3467b15b38e546cbf9645804`. Subsequent operator additions preserve both earlier receipts; replay each against its recorded ancestor rather than rebinding it to new text.

Rollback: revert this documentation change and its navigation/authoring receipt. Preserve all earlier data, baseline receipts, approval records, and release artifacts. A documentation rollback does not undo any operator action.
