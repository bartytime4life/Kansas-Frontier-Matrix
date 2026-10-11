# USCRN daily soil pilot: capture, release and local serving

Status: implemented and tested offline. The owner admitted the NOAA USCRN
source on 2026-10-11 and accepted
[ADR-0046](../../adr/ADR-0046-owner-self-release-for-admitted-public-soil-data.md).
No real package has been captured, released or served yet, and the hosted Site
does not carry the soil layer yet.

## Scope

Daily volumetric soil moisture (`SOIL_MOISTURE`, m³/m³) and soil temperature
(`SOIL_TEMP`, °C) at 5, 10, 20, 50 and 100 cm for the two U.S. Climate
Reference Network stations in Kansas: WBAN 53974 Manhattan 6 SSW and WBAN
03067 Oakley 19 SSW. A capture covers the 30 local-standard-time days ending on
a date you choose. Missing and physically impossible values are withheld
(`value: null`) and never count as zero. The admitted source is
[`noaa-uscrn.yaml`](../../../data/registry/sources/soil/noaa-uscrn.yaml); the
record contract is
[`daily_soil_observation.md`](../../../contracts/domains/soil/daily_soil_observation.md).

Values describe one station point and one day, not a field, county or region.

## Releasing the soil layer

Run on the computer that holds the private data root. Capture needs network
access to `www.ncei.noaa.gov`. If NOAA changes the daily01 column layout, the
capture is refused (`HEADER_PROFILE_MISMATCH`) instead of mislabeling a column.

```bash
ROOT=/absolute/private/KFM-data
# 1. Capture the 30 days ending on END and build the WORK candidate.
.venv/bin/python tools/local_data/uscrn_daily_pilot.py --root $ROOT capture --end 2026-10-10
# 2. Prepare the admitted package, then write your decision (ADR-0046 self-release).
.venv/bin/python tools/release/soil_release.py prepare --root $ROOT --candidate-id sha256:CANDIDATE --admitted-source
.venv/bin/python tools/release/soil_release.py decide --root $ROOT --package-id sha256:PACKAGE \
  --reviewer @bartytime4life --releaser @bartytime4life --valid-days 7
```

`decide` writes the decision only when the soil serving gate would serve it.
Before deciding (and staging) it re-checks that the package's candidate is
exactly what the stored capture normalizes to (`CANDIDATE_CAPTURE_MISMATCH`,
`CAPTURE_NOT_IN_STORE`), so run it against the same `--root` that captured.
A package prepared without `--admitted-source` keeps the rights hold, and
`decide` refuses it. Use `--rollback-target` with the currently active soil
package when you prepare a replacement.

Each package carries one evidence bundle per station and depth (10 bundles).

## Local serving

The soil layer shares the private serving store with water and weather but
uses its own tables (`soil_*`) and object directory (`soil-objects/`), so
activating one never changes the others.

```bash
STORE=/absolute/private/KFM-release-serving
.venv/bin/python tools/release/soil_release.py stage --root $ROOT --store $STORE --package-id sha256:PACKAGE --actor @bartytime4life
.venv/bin/python tools/release/soil_release.py activate --root $ROOT --store $STORE \
  --decision release/decisions/soil/HASH/STAMP.json --expected-active none
KFM_RELEASE_STORE=$STORE .venv/bin/kfm-governed-api   # /v1/soil/layers now answers
```

Routes: `/v1/soil/bootstrap`, `/v1/soil/layers` and `/v1/soil/evidence`, each
optionally filtered with `?station_id=` (`53974` or `03067`). The evidence view
returns the station's five depth bundles. Freshness is `current` while the
latest reported soil moisture value is at most three days before today in
Kansas Central standard time (UTC−6).

Activation is compare-and-swap (`ACTIVATION_CONFLICT` if the active package
changed). `rollback` reactivates the previous package with its decision. An
expired decision stops the layer from answering. To renew, capture again,
prepare a replacement bound to the active package (`prepare ...
--rollback-target sha256:ACTIVE`), then `decide`, `stage` and `activate
--expected-active sha256:ACTIVE`.

## Validation

All offline: `tests/domains/soil/test_uscrn_daily_candidate.py` (capture and
candidate), `tests/tools/test_uscrn_daily_pilot.py` (private store),
`tests/tools/test_soil_release.py` (package, depth bundles, gate, decision,
capture binding and family isolation) and `tests/tools/test_soil_serving.py`
(stage, activate and loopback `/v1/soil/*`). The soil CI lane runs them.
