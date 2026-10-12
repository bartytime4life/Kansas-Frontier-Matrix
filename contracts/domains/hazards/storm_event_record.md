<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/domains/hazards/storm-event-record
title: contracts/domains/hazards/storm_event_record.md — StormEventRecord Contract
type: contract
version: v1.0
status: draft
owners: "@bartytime4life"
created: 2026-10-12
updated: 2026-10-12
policy_label: public; contracts; domains; hazards; storm-event-record; historical-event; not-life-safety
related:
  - ../../../schemas/contracts/v1/domains/hazards/storm_event_record.schema.json
  - ../../../data/registry/sources/hazards/noaa.storm_events.yaml
  - ../../../connectors/noaa/src/noaa/storm_events.py
  - ../../../connectors/noaa/src/noaa/storm_events_capture.py
  - ../../../pipelines/domains/hazards/storm_events_normalize.py
  - ../../../pipelines/domains/hazards/storm_events_validate.py
notes:
  - "Closed v1 record for the NOAA NCEI Storm Events Kansas pilot."
[/KFM_META_BLOCK_V2] -->

# StormEventRecord

One row of a NOAA NCEI Storm Events details file for Kansas (`STATE_FIPS` 20):
a National Weather Service report that an event of one type affected one
county (`C`), forecast zone (`Z`) or marine zone (`M`) over a local-time
window.

The schema is closed:
[`storm_event_record.schema.json`](../../../schemas/contracts/v1/domains/hazards/storm_event_record.schema.json).
It is a flat pipeline record. It is a historical event report, not a
measurement, a hazard footprint, a current warning or a disaster declaration.

## Meaning

| Field | Meaning |
|---|---|
| `event_id`, `episode_id` | NCEI's identifiers. `episode_id` is `null` when the row has none (flag `EPISODE_ID_ABSENT`). |
| `cz_type`, `cz_fips`, `cz_name` | The county or zone the report names. Selection is by NCEI's `STATE_FIPS`, not a spatial join. |
| `cz_timezone` | NCEI's `CZ_TIMEZONE` token verbatim (for example `CST-6`). |
| `begin_local`, `end_local` | Local times as reported (`YYYY-MM-DDTHH:MM`). |
| `begin_utc`, `end_utc` | Local time plus the token's hour offset, or `null` when the token carries none (flag `UTC_OFFSET_UNKNOWN`). |
| `damage_property_source`, `damage_crops_source` | NCEI's damage strings verbatim (`250.00K`, `2.00M`). |
| `damage_property_usd`, `damage_crops_usd` | The strings as exact nominal event-year USD, or `null` when blank. Blank is unreported, never zero. |
| `magnitude_source`, `magnitude_type`, `tor_f_scale` | Source strings, never converted. |
| `begin_lat` … `end_lon` | Report points when present, in pairs. All `null` means county or zone support only (flag `ZONE_OR_COUNTY_SUPPORT_ONLY`). |
| `has_narrative` | Whether NCEI supplied an episode or event narrative. The text itself is never copied. |
| `flags` | Review flags from the parser, in order: `EPISODE_ID_ABSENT`, `EVENT_TYPE_OUTSIDE_DIRECTIVE` (a label outside the NWS Directive 10-1605 list), `UTC_OFFSET_UNKNOWN`, `ZONE_OR_COUNTY_SUPPORT_ONLY`. |
| `source_row_digest` | SHA-256 of the parsed source row, narratives included. |
| `id`, `evidence_ref` | Stable across file vintages: the SHA-256 of the source and `event_id`. |
| `record_digest` | SHA-256 of the record without this field; changes when NCEI revises the row. |

## Withheld rows

Rows the parser routes to quarantine are not records. The candidate counts
them in `withheld_rows`, and counts every blocking reason they carry in
`withheld_counts`: `CASUALTY_UNPARSEABLE`, `DAMAGE_UNPARSEABLE` and
`END_BEFORE_BEGIN`. A row with two defects adds one row and one to each of its
reasons. A missing record does not mean no
hazard occurred.

## Candidate

`pipelines/domains/hazards/storm_events_normalize.py` builds a
`kfm.storm-events-candidate/v1` from one capture: the NCEI `csvfiles/`
listing and the details file it names as the newest creation vintage for the
data year. The candidate records `source_file`, `vintage_created`,
`latest_event_date`, and `freshness_at_capture`, which is `STALE` when the
vintage is more than 45 days older than retrieval. `coverage` stays
`NOT_ESTABLISHED`: a details file does not prove every event was reported.
NCEI reissues a year's file under a new creation date when it corrects
reports; each vintage is a separate source state.

## Authority

A record is a review candidate. It carries no source admission, review,
release or publication authority. The source descriptor
`data/registry/sources/hazards/noaa.storm_events.yaml` is `needs_review`, and
`pipelines/domains/hazards/storm_events_admission.py` refuses it
(`SOURCE_NOT_ADMITTED`) until the repository owner approves it. No owner
self-release ADR covers this source.

## Validation

`pipelines/domains/hazards/storm_events_validate.py` checks every record
against the schema, parses both local times (even when no UTC can be derived),
and re-derives its identity, digest, damage values, UTC times and flags. It also re-derives the candidate's file vintage, latest event
date and freshness. `tests/domains/hazards/test_storm_events_candidate.py`
covers listing selection, schema drift, withholding, the narrative exclusion,
tamper denial and identity stability across vintages.
