<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/domains/atmosphere/daily-weather-observation
title: contracts/domains/atmosphere/daily_weather_observation.md — DailyWeatherObservation Contract
type: contract
version: v1.0
status: draft
owners: "@bartytime4life"
created: 2026-10-11
updated: 2026-10-11
policy_label: public; contracts; domains; atmosphere; daily-weather-observation; observed-station
related:
  - ../../../schemas/contracts/v1/domains/atmosphere/daily_weather_observation.schema.json
  - ../../../data/registry/sources/atmosphere/noaa_ghcnd.yaml
  - ../../../pipelines/domains/atmosphere/ghcnd_daily_normalize.py
  - ../../../pipelines/domains/atmosphere/ghcnd_daily_validate.py
  - ./PrecipitationObservation.md
notes:
  - "Closed v1 record for the GHCN-Daily Kansas first-order station pilot."
[/KFM_META_BLOCK_V2] -->

# DailyWeatherObservation

One GHCN-Daily station-day element for the Kansas first-order station pilot:
daily precipitation (`PRCP`), maximum temperature (`TMAX`) or minimum
temperature (`TMIN`) at USW00003928 (Wichita), USW00013985 (Dodge City),
USW00013996 (Topeka) or USW00023065 (Goodland).

The schema is closed:
[`daily_weather_observation.schema.json`](../../../schemas/contracts/v1/domains/atmosphere/daily_weather_observation.schema.json).
It is separate from the open `PrecipitationObservation` scaffold, which it does
not change.

## Meaning

| Field | Meaning |
|---|---|
| `observation_date` | The station's local observation day (`YYYY-MM-DD`), not a UTC instant. |
| `raw_value` | The source integer in tenths, kept verbatim. `-9999` means missing. |
| `value` | `raw_value / 10` in `mm` (PRCP) or `degC` (TMAX, TMIN), or `null` when withheld. |
| `measurement_flag`, `quality_flag`, `source_flag` | The GHCN-Daily M, Q and S flags, verbatim (empty when blank). |
| `trace` | `true` when M=`T`; `value` is then `0`. |
| `withheld` | `MISSING` for `-9999` or M=`P` ("presumed zero"), `QUALITY_FLAG` for any Q flag, otherwise `null`. |
| `preliminary` | Always `true`: NCEI rebuilds the files daily and recent values may be revised. |
| `id`, `evidence_ref` | Stable across revisions: the SHA-256 of station, element and observation date. |
| `record_digest` | SHA-256 of the record without this field; changes when a value is revised. |

A withheld value never counts as zero, and a candidate never presents a
quality-flagged value as a reading.

## Authority

A record is a review candidate. It carries no source admission, review,
release or publication authority. The source descriptor
`data/registry/sources/atmosphere/noaa_ghcnd.yaml` is proposed until the
repository owner admits it, and releasing any package still requires a release
decision that passes the serving gate.

## Validation

`pipelines/domains/atmosphere/ghcnd_daily_validate.py` checks every record
against the schema and re-derives its identity, digest and value from the raw
value and flags. `tests/domains/atmosphere/test_ghcnd_daily_candidate.py`
covers the flag rules, tamper denial and identity stability.
