<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/domains/soil/daily-soil-observation
title: contracts/domains/soil/daily_soil_observation.md — DailySoilObservation Contract
type: contract
version: v1.0
status: draft
owners: "@bartytime4life"
created: 2026-10-11
updated: 2026-10-11
policy_label: public; contracts; domains; soil; daily-soil-observation; reference-station
related:
  - ../../../schemas/contracts/v1/domains/soil/daily_soil_observation.schema.json
  - ../../../data/registry/sources/soil/noaa-uscrn.yaml
  - ../../../connectors/noaa/src/noaa/uscrn_daily.py
  - ../../../pipelines/domains/soil/uscrn_daily_normalize.py
  - ../../../pipelines/domains/soil/uscrn_daily_validate.py
notes:
  - "Closed v1 record for the USCRN daily01 Kansas reference-station soil pilot."
[/KFM_META_BLOCK_V2] -->

# DailySoilObservation

One NOAA U.S. Climate Reference Network (USCRN) daily01 soil value for the
Kansas reference-station pilot: volumetric soil moisture (`SOIL_MOISTURE`,
m³/m³) or soil temperature (`SOIL_TEMP`, °C) at one sensor depth (5, 10, 20, 50
or 100 cm), at WBAN 53974 (Manhattan 6 SSW) or WBAN 03067 (Oakley 19 SSW).

The schema is closed:
[`daily_soil_observation.schema.json`](../../../schemas/contracts/v1/domains/soil/daily_soil_observation.schema.json).
It is a flat pipeline record, separate from the `soil_moisture_observation`
assessment envelope, which it does not change. In that vocabulary it is a
`VOLUMETRIC_WATER_CONTENT` (or soil temperature) reading with
`SENSOR_DEPTH` support at an exact public station point.

## Meaning

| Field | Meaning |
|---|---|
| `observation_date` | The station's local-standard-time day (`YYYY-MM-DD`), not a UTC instant. |
| `source_token` | NOAA's daily value verbatim. `-99.000` (moisture) and `-9999.0` (temperature) mean missing. |
| `value` | The token as a number in `m3/m3` or `degC`, or `null` when withheld. |
| `withheld` | `MISSING` for a missing sentinel; `OUT_OF_RANGE` for moisture outside 0–1 or temperature outside −50–60 °C; otherwise `null`. |
| `datalogger_version` | The row's `CRX_VN`, verbatim: provenance for the station's logger program. |
| `id`, `evidence_ref` | Stable across revisions: the SHA-256 of station, variable, depth and observation date. |
| `record_digest` | SHA-256 of the record without this field; changes when a value is revised. |

A withheld value never counts as zero, and a candidate never presents an
impossible value as a reading. Values describe one station point and one day,
not a field, county or region.

## Source layout

`connectors/noaa/src/noaa/uscrn_daily.py` reads rows only through its pinned
28-field daily01 profile. Every capture also fetches NOAA's `headers.txt` and
is refused (`HEADER_PROFILE_MISMATCH`) unless it lists exactly those fields in
that order, and every row must carry the expected WBAN number, so an upstream
layout change fails closed instead of mislabeling a column.

## Authority

A record is a review candidate. It carries no source admission, review,
release or publication authority. The source descriptor
`data/registry/sources/soil/noaa-uscrn.yaml` is proposed until the repository
owner admits it, and releasing any package still requires a release decision
that passes the serving gate.

## Validation

`pipelines/domains/soil/uscrn_daily_validate.py` checks every record against
the schema and re-derives its identity, digest and value from the source
token. `tests/domains/soil/test_uscrn_daily_candidate.py` covers the header
check, sentinel and range rules, tamper denial and identity stability.
