# USGS earthquake pilot: capture, release and local serving

Status: implemented and tested offline. The owner admitted the USGS ComCat
earthquake source on 2026-10-12 and accepted
[ADR-0049](../../adr/ADR-0049-owner-self-release-for-admitted-public-earthquake-data.md).
No real package has been captured, released or served yet.

## Scope

USGS ANSS Comprehensive Catalog (ComCat) earthquakes whose epicenter lies in
the Kansas context envelope (-102.1 to -94.5 longitude, 36.9 to 40.1 latitude)
in one data year. The capture asks the FDSN event service for each calendar
month separately. The envelope is not the state boundary: records in its
Oklahoma, Missouri, Nebraska and Colorado margins carry `CONTEXT_MARGIN`.
Deleted solutions are withheld and counted. Felt reports, ShakeMap and PAGER
products are never fetched. The admitted source is
[`usgs.earthquakes.yaml`](../../../data/registry/sources/hazards/usgs.earthquakes.yaml);
the record contract is
[`earthquake_record.md`](../../../contracts/domains/hazards/earthquake_record.md).

A record is a catalog solution (origin time, epicenter, depth, magnitude), not
a shaking estimate, damage report, alert or attribution of cause. KFM is not an
earthquake alerting or life-safety service, and the absence of a record does
not mean no earthquake occurred.

## Releasing the layer

Run on the computer that holds the private data root. Capture needs network
access to `earthquake.usgs.gov`. A month whose query returns 5000 events (the
page may be truncated), or an event outside its month, the envelope or the
earthquake type, quarantines the capture instead of releasing a partial year.

```bash
ROOT=/absolute/private/KFM-data
# 1. Capture the twelve months of the year and build the WORK candidate.
.venv/bin/python tools/local_data/earthquake_pilot.py --root $ROOT capture --year 2025
# 2. Prepare the admitted package, then write your decision (ADR-0049 self-release).
.venv/bin/python tools/release/earthquake_release.py prepare --root $ROOT --candidate-id sha256:CANDIDATE --admitted-source
.venv/bin/python tools/release/earthquake_release.py decide --root $ROOT --package-id sha256:PACKAGE \
  --reviewer @bartytime4life --releaser @bartytime4life --valid-days 7
```

`decide` writes the decision only when the earthquake serving gate would serve
it. Before deciding (and staging) it re-checks that the package's candidate is
exactly what the stored capture normalizes to (`CANDIDATE_CAPTURE_MISMATCH`,
`CAPTURE_NOT_IN_STORE`), so run it against the same `--root` that captured. A
package prepared without `--admitted-source` keeps the rights hold, and
`decide` refuses it. Use `--rollback-target` with the currently active
earthquake package when you prepare a replacement.

A package covers one calendar year. Evidence is one bundle per UTC origin month
with events, split into numbered parts of 127 records. A year with more than
6000 events is refused (`OBSERVATION_LIMIT`). The year is `OPEN` while the
capture falls inside it and `CLOSED` afterwards; ComCat still revises closed
years.

## Local serving

The layer shares the private serving store with water, weather, soil and storm
events but uses its own tables (`earthquakes_*`) and object directory
(`earthquakes-objects/`), so activating one never changes the others.

```bash
STORE=/absolute/private/KFM-release-serving
.venv/bin/python tools/release/earthquake_release.py stage --root $ROOT --store $STORE --package-id sha256:PACKAGE --actor @bartytime4life
.venv/bin/python tools/release/earthquake_release.py activate --root $ROOT --store $STORE \
  --decision release/decisions/earthquakes/HASH/STAMP.json --expected-active none
KFM_RELEASE_STORE=$STORE .venv/bin/kfm-governed-api   # /v1/earthquakes/layers now answers
```

Routes: `/v1/earthquakes/bootstrap`, `/v1/earthquakes/layers` and
`/v1/earthquakes/evidence`, each optionally filtered with `?month=` (`1` to
`12`, by UTC origin month). A month with no events answers
`EVIDENCE_NOT_FOUND`. `/layers` carries the year summary (`dataset`, labeled
`scope: data_year`) and a `selection` describing exactly the returned records.
Freshness is `current` for 30 days after the capture; after that the layer
still answers as `stale-accepted`, because ComCat may have revised solutions.

Activation is compare-and-swap (`ACTIVATION_CONFLICT` if the active package
changed). `rollback` reactivates the previous package with its decision. An
expired decision stops the layer from answering. To renew, capture again,
prepare a replacement bound to the active package (`prepare ...
--rollback-target sha256:ACTIVE`), then `decide`, `stage` and `activate
--expected-active sha256:ACTIVE`.

## Validation

All offline: `tests/domains/hazards/test_earthquake_candidate.py` (capture and
candidate), `tests/tools/test_earthquake_pilot.py` (private store),
`tests/tools/test_earthquake_release.py` (package, month bundles, gate,
decision, capture binding and family isolation) and
`tests/tools/test_earthquake_serving.py` (stage, activate and loopback
`/v1/earthquakes/*`). The domain-hazards CI lane runs them.
