# NOAA Storm Events pilot: capture, release and local serving

Status: implemented and tested offline. The owner admitted the NOAA Storm
Events source on 2026-10-12 and accepted
[ADR-0047](../../adr/ADR-0047-owner-self-release-for-admitted-public-storm-events-data.md).
No real package has been captured, released or served yet.

## Scope

The Kansas (`STATE_FIPS` 20) rows of one data year's NCEI Storm Events details
file: National Weather Service reports of hail, wind, tornado, flood, winter
and other events by county or forecast zone. The capture reads the NCEI
`csvfiles/` listing and fetches the newest file it names for the year.
Narratives are never copied, the fatalities and locations files are never
fetched, and rows with unreadable damage or casualty values, or an end before
the begin, are withheld and counted. The admitted source is
[`noaa.storm_events.yaml`](../../../data/registry/sources/hazards/noaa.storm_events.yaml);
the record contract is
[`storm_event_record.md`](../../../contracts/domains/hazards/storm_event_record.md).

A record is a historical event report, not a measurement, footprint, warning or
declaration. KFM is not a warning or life-safety service, and the absence of a
record does not mean no hazard occurred.

## Releasing the layer

Run on the computer that holds the private data root. Capture needs network
access to `www.ncei.noaa.gov`. If NCEI drops a column the parser needs, the
capture is quarantined (`DETAILS_FILE_SCHEMA_DRIFT`) instead of mislabeling a
value.

```bash
ROOT=/absolute/private/KFM-data
# 1. Capture the newest details file NCEI lists for the year and build the WORK candidate.
.venv/bin/python tools/local_data/storm_events_pilot.py --root $ROOT capture --year 2025
# 2. Prepare the admitted package, then write your decision (ADR-0047 self-release).
.venv/bin/python tools/release/storm_events_release.py prepare --root $ROOT --candidate-id sha256:CANDIDATE --admitted-source
.venv/bin/python tools/release/storm_events_release.py decide --root $ROOT --package-id sha256:PACKAGE \
  --reviewer @bartytime4life --releaser @bartytime4life --valid-days 7
```

`decide` writes the decision only when the storm events serving gate would
serve it. Before deciding (and staging) it re-checks that the package's
candidate is exactly what the stored capture normalizes to
(`CANDIDATE_CAPTURE_MISMATCH`, `CAPTURE_NOT_IN_STORE`), so run it against the
same `--root` that captured. A package prepared without `--admitted-source`
keeps the rights hold, and `decide` refuses it. Use `--rollback-target` with
the currently active storm events package when you prepare a replacement.

A package covers one calendar year. Evidence is one bundle per month with
events, split into numbered parts of 127 records. A year with more than 5000
Kansas events is refused (`OBSERVATION_LIMIT`).

## Local serving

The layer shares the private serving store with water, weather and soil but
uses its own tables (`storm_events_*`) and object directory
(`storm-events-objects/`), so activating one never changes the others.

```bash
STORE=/absolute/private/KFM-release-serving
.venv/bin/python tools/release/storm_events_release.py stage --root $ROOT --store $STORE --package-id sha256:PACKAGE --actor @bartytime4life
.venv/bin/python tools/release/storm_events_release.py activate --root $ROOT --store $STORE \
  --decision release/decisions/storm-events/HASH/STAMP.json --expected-active none
KFM_RELEASE_STORE=$STORE .venv/bin/kfm-governed-api   # /v1/storm-events/layers now answers
```

Routes: `/v1/storm-events/bootstrap`, `/v1/storm-events/layers` and
`/v1/storm-events/evidence`, each optionally filtered with `?month=` (`1` to
`12`). A month with no events answers `EVIDENCE_NOT_FOUND`. Freshness is
`current` while the NCEI file vintage is at most 45 days old; after that the
layer still answers as `stale-accepted`, because NCEI may have reissued the
year.

Activation is compare-and-swap (`ACTIVATION_CONFLICT` if the active package
changed). `rollback` reactivates the previous package with its decision. An
expired decision stops the layer from answering. To renew, capture again,
prepare a replacement bound to the active package (`prepare ...
--rollback-target sha256:ACTIVE`), then `decide`, `stage` and `activate
--expected-active sha256:ACTIVE`.

## Validation

All offline: `tests/domains/hazards/test_storm_events_candidate.py` (capture
and candidate), `tests/tools/test_storm_events_pilot.py` (private store),
`tests/tools/test_storm_events_release.py` (package, month bundles, gate,
decision, capture binding and family isolation) and
`tests/tools/test_storm_events_serving.py` (stage, activate and loopback
`/v1/storm-events/*`). The domain-hazards CI lane runs them.
