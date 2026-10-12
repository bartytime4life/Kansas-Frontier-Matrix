# GHCN-Daily pilot: capture, release and local serving

Status: implemented and tested offline. The owner admitted the NOAA GHCN-Daily
source on 2026-10-11 and accepted
[ADR-0045](../../adr/ADR-0045-owner-self-release-for-admitted-public-weather-data.md).
No real package has been captured, released or served yet.

## Scope

Daily precipitation (PRCP, mm), maximum temperature (TMAX, °C) and minimum
temperature (TMIN, °C) for four federally operated first-order stations:
USW00003928 Wichita, USW00013985 Dodge City, USW00013996 Topeka and
USW00023065 Goodland. A capture covers the 30 station-local observation days
ending on a date you choose. Missing and quality-flagged values are withheld
(`value: null`) and never count as zero. The admitted source is
[`noaa_ghcnd.yaml`](../../../data/registry/sources/atmosphere/noaa_ghcnd.yaml);
the record contract is
[`daily_weather_observation.md`](../../../contracts/domains/atmosphere/daily_weather_observation.md).

## Releasing the weather layer

Run on the computer that holds the private data root. Capture needs network
access to `www.ncei.noaa.gov`.

```bash
ROOT=/absolute/private/KFM-data
# 1. Capture the 30 days ending on END and build the WORK candidate.
.venv/bin/python tools/local_data/ghcnd_daily_pilot.py --root $ROOT capture --end 2026-10-10
# 2. Prepare the admitted package, then write your decision (ADR-0045 self-release).
.venv/bin/python tools/release/weather_release.py prepare --root $ROOT --candidate-id sha256:CANDIDATE --admitted-source
.venv/bin/python tools/release/weather_release.py decide --root $ROOT --package-id sha256:PACKAGE \
  --reviewer @bartytime4life --releaser @bartytime4life --valid-days 7
```

`decide` writes the decision only when the weather serving gate would serve
it. A package prepared without `--admitted-source` keeps the rights hold, and
`decide` refuses it. Use `--rollback-target` with the currently active weather
package when you prepare a replacement.

## Local serving

The weather layer shares the private serving store with water but uses its own
tables (`weather_*`) and object directory (`weather-objects/`), so activating
one never changes the other.

```bash
STORE=/absolute/private/KFM-release-serving
.venv/bin/python tools/release/weather_release.py stage --root $ROOT --store $STORE --package-id sha256:PACKAGE --actor @bartytime4life
.venv/bin/python tools/release/weather_release.py activate --root $ROOT --store $STORE \
  --decision release/decisions/atmosphere/HASH/STAMP.json --expected-active none
KFM_RELEASE_STORE=$STORE .venv/bin/kfm-governed-api   # /v1/weather/layers now answers
```

Routes: `/v1/weather/bootstrap`, `/v1/weather/layers` and `/v1/weather/evidence`,
each optionally filtered with `?station_id=` (one of the four stations).
Activation is compare-and-swap (`ACTIVATION_CONFLICT` if the active package
changed). `rollback` reactivates the previous package with its decision. An
expired decision stops the layer from answering. To renew, capture again and
prepare a replacement bound to the active package (`prepare ... --rollback-target
sha256:ACTIVE`), then `decide`, `stage` and `activate --expected-active
sha256:ACTIVE`. Re-activating the package that is already active is refused
(`ROLLBACK_BINDING_MISMATCH`), because a package cannot name itself as its
rollback target.

## Hosted release on the Site

The Site's weather routes accept only weather packages and weather decisions,
and use the Site's existing owner list and staging token
(`KFM_WATER_WORKER_TOKEN`); no new Site setting is needed. Apply the additive
D1 migration `apps/site/source/drizzle/0006_governed_weather.sql` with the Site
version that carries the weather routes.

```bash
export KFM_WATER_WORKER_TOKEN=...          # the Site's staging token
# Capture the 30 days ending yesterday (UTC), package, decide and stage on the Site.
# The rollback target is read from the Site first, so a replacement binds to what is active.
.venv/bin/python tools/release/weather_release.py cycle --root $ROOT --owner @bartytime4life \
  --site-url https://YOUR-SITE
```

`cycle` never activates. It prints the decision path and the release page URL.
Open `/governed/weather-release`, paste the decision file and press
**Activate package**. **Withdraw active package** stops the layer at once.
`stage-hosted --package-id` uploads an already prepared package instead. Run
`cycle` again before the decision expires (default 7 days); the release page
warns two days ahead.

## Validation

All offline: `tests/domains/atmosphere/test_ghcnd_daily_candidate.py`
(capture and candidate), `tests/tools/test_ghcnd_daily_pilot.py` (private
store), `tests/tools/test_weather_release.py` (package, gate, decision and
water/weather isolation), `tests/tools/test_weather_serving.py` (stage,
activate and loopback `/v1/weather/*`), `tests/tools/test_weather_hosted.py`
(hosted staging and `cycle`), and the Site's `tests/governed-weather*.test.mjs`
(parser, gate, Python parity, D1/R2 admin, read route and map control).
