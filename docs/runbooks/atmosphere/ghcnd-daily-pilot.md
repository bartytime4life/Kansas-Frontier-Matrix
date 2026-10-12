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

## Private archive review from an existing capture

The operator [`ghcnd_archive_review.py`](../../../tools/local_data/ghcnd_archive_review.py)
reuses the five immutable objects of a staged fixed-cohort capture. It performs
no network request. Unlike the 30-day pilot, it retains every available
PRCP/TMAX/TMIN record in those four captured station files, preserving raw
tenths, normalized units, dates, flags, missing/withheld values, trace status,
source-page digests and deterministic record identities. Full captured history
does not establish statewide coverage or a complete calendar series. Current
station coordinates do not establish historical location stability.

```bash
PYTHONPATH=packages/connectors-core/src:packages/hashing/src:packages/policy-runtime/src:packages/evidence-resolver/src:packages/release/src \
  .venv/bin/python tools/local_data/ghcnd_archive_review.py \
  --root /absolute/private/KFM-data --capture-id sha256:CAPTURE
```

The external, initialized owner-private store remains mandatory. This operator
belongs to `tools/` under Directory Rules §7.2; its negative and recovery tests
belong to `tests/`. Review data belongs to the existing external WORK lane, not
repository history or the rebuildable code-distribution lane. Outputs are
`data/work/atmosphere/noaa-ghcnd-archive-review/<review-id>/observations.csv`,
station/year/element coverage, current-provider station metadata, a manifest
and a deterministic ZIP. Receipts use the existing
`data/receipts/curation/noaa-ghcnd-archive-review/<review-id>/` lane. Identity binds
the capture, operator/normalizer source hashes, cohort and selected byte cap.

The default maximum is 512 MiB for each output, with a two-million selected-row
limit and the canonical parser's 128 MiB expansion limit for each station.
The operator checks free space for two selected byte caps plus a 1 GiB reserve,
takes the existing nonblocking store lock and rejects static filesystem links.
Owner-controlled directory ancestry remains a prerequisite; these helpers do
not sandbox a hostile process replacing ancestors. No ZIP is extracted.

A completed replay rehashes the source objects and exact output members, checks
pending review/unreleased flags, and validates ZIP member sizes, digests and CRC.
A changed output, missing receipt, extra member, collision, busy writer or
incomplete run is held. Partial outputs and failure receipts remain inspectable;
they are not overwritten or automatically repaired. A changed generator or
byte cap produces a new identity, leaving the previous review untouched.

`usable` in the count tables means unwithheld by the retained missing/quality
flag policy. It is not scientific validity or proof of station homogeneity.
The review package remains WORK/PENDING, does not replace the pilot candidate,
and is not accepted by the weather release operator as a pilot candidate.
Its false authority fields describe this package, not the current source
registry. Existing source admission or ADR-0045 does not authorize uploading,
serving, activating or releasing this separate full-history package. Current
rights, sensitivity, source-role and release review remain independent.

Validate with `tests/local_data/test_ghcnd_archive_review.py`, which covers
historical records outside the pilot window, missing/QC/trace semantics,
duplicate identities, changed input bytes, damaged outputs/receipts, unsafe ZIP
members, links, busy writers, insufficient space and retained partial failures.
