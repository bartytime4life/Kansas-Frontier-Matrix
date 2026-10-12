<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/domains/hazards/earthquake-record
title: contracts/domains/hazards/earthquake_record.md — EarthquakeRecord Contract
type: contract
version: v1.0
status: draft
owners: "@bartytime4life"
created: 2026-10-12
updated: 2026-10-12
owning_root: contracts/
responsibility: "Meaning of the closed kfm.earthquake-record/v1 pipeline record and its candidate"
truth_posture: "cite-or-abstain; describes a review candidate with no admission, release or life-safety authority"
policy_label: public; contracts; domains; hazards; earthquake-record; catalog-solution; not-life-safety
related:
  - ../../../schemas/contracts/v1/domains/hazards/earthquake_record.schema.json
  - ../../../data/registry/sources/hazards/usgs.earthquakes.yaml
  - ../../../connectors/usgs/src/usgs/earthquake.py
  - ../../../connectors/usgs/src/usgs/earthquake_capture.py
  - ../../../pipelines/domains/hazards/earthquake_normalize.py
  - ../../../pipelines/domains/hazards/earthquake_validate.py
  - ../../../pipelines/domains/hazards/earthquake_package.py
  - ../../../docs/adr/ADR-0049-owner-self-release-for-admitted-public-earthquake-data.md
notes:
  - "Closed v1 record for the USGS ComCat Kansas earthquake pilot."
[/KFM_META_BLOCK_V2] -->

# EarthquakeRecord

One USGS ANSS Comprehensive Catalog (ComCat) earthquake whose epicenter lies in
the Kansas context envelope (-102.1 to -94.5 longitude, 36.9 to 40.1
latitude): the preferred catalog solution at retrieval.

The schema is closed:
[`earthquake_record.schema.json`](../../../schemas/contracts/v1/domains/hazards/earthquake_record.schema.json).
It is a flat pipeline record. A solution is an estimate of where and when an
earthquake began and how large it was. It is not a shaking estimate, a damage
or felt report, an alert, a forecast or an attribution of cause.

## Meaning

| Field | Meaning |
|---|---|
| `event_id` | ComCat's preferred event id. It can change when contributing solutions are associated. |
| `aliases` | `event_id` first, then every other id ComCat lists for the event (`ids`). No alias names two records. |
| `origin_utc`, `updated_utc` | Origin time and ComCat's last update, UTC to the millisecond. `updated_utc` may be `null`. |
| `longitude`, `latitude`, `depth_km`, `magnitude` | Source values rounded to four decimal places, written as integers when whole, so the JSON text is the same in Python and JavaScript. `depth_km` and `magnitude` may be `null`. |
| `magnitude_type` | ComCat's `magType` verbatim (`ml`, `md`, `mb_lg`, `mww`, ...). Magnitudes of different types are not interchangeable. |
| `review_status` | ComCat's `status` verbatim: `automatic` or `reviewed`. |
| `net`, `place` | The preferred solution's network code and ComCat's place text verbatim (a distance and direction from a named place). Either may be `null`. |
| `flags` | Review flags, in order: `MAGNITUDE_ABSENT`, `DEPTH_ABSENT`, `REVIEW_AUTOMATIC`, `REVIEW_STATUS_UNKNOWN` (status neither `automatic` nor `reviewed`), `CONTEXT_MARGIN` (epicenter outside the rectangle 102.0517°W–94.5884°W, 37°N–40°N). |
| `feature_sha256` | SHA-256 of the source GeoJSON feature, unrounded, every field included. The feature itself is not copied. |
| `page_digest`, `retrieved_at` | The captured month page and when it was fetched. |
| `id`, `evidence_ref` | The SHA-256 of the source and `event_id`. |
| `record_digest` | SHA-256 of the record without this field; changes when ComCat revises the solution. |

The envelope is not the state boundary. It takes in margins of Oklahoma,
Missouri, Nebraska and Colorado, which `CONTEXT_MARGIN` marks. Inside the
rectangle is not proof of Kansas: the Missouri River bounds the northeast
corner.

## Months and withheld events

The capture asks ComCat for each calendar month of the data year separately
(`limit=5000`, `orderby=time-asc`, `nodata=204`). An FDSN query includes both
endpoints, so an event at exactly midnight on the first of a month is returned
twice; the month that starts there owns it. Any other returned event outside
its month, the envelope or the `earthquake` type is upstream drift and refuses
the capture, as does a page that reaches the 5000-event limit (it may be
truncated). Events ComCat marks `deleted` are not records; the candidate
counts them in `withheld_counts.STATUS_DELETED`. `months` lists each month's
query status (`200` or `204`) and kept event count.

## Candidate

`pipelines/domains/hazards/earthquake_normalize.py` builds a
`kfm.earthquake-candidate/v1` from one capture. It records `latest_event_date`
and `year_state`: `OPEN` when the capture falls inside the data year,
`CLOSED` after it. ComCat revises solutions for weeks to months, so a closed
year can still change and each capture is a separate source state. `coverage`
stays `NOT_ESTABLISHED`: the catalog's detection threshold varies with time
and place, and an event revised across a month boundary between two month
queries can be missed. The absence of a record does not mean no earthquake
occurred.

## Authority

A record is a review candidate. It carries no source admission, review,
release or publication authority. The source descriptor
`data/registry/sources/hazards/usgs.earthquakes.yaml` was admitted by the
repository owner on 2026-10-12; releasing a package still requires a
`kfm.earthquake-release-decision/v1` record that passes the earthquake serving
gate
([ADR-0049](../../../docs/adr/ADR-0049-owner-self-release-for-admitted-public-earthquake-data.md)).

`pipelines/domains/hazards/earthquake_package.py` packages a candidate under
the `kfm.earthquake-snapshot/v1` profile. The manifest interval is the data
year (`YYYY-01-01` to `YYYY-12-31`). Evidence is one bundle per UTC origin
month that has events, split into numbered parts of 127 records so each
bundle stays inside the resolver's 128-member limit; records are `record`
members. A year with more than 6000 events is refused (`OBSERVATION_LIMIT`);
6000 events of typical size package to about 7 MiB, and a package whose texts
push it past the 8 MiB limit is refused (`JSON_BYTE_LIMIT`). A year with no
events has nothing to package (`NO_EVENTS_TO_PACKAGE`).

## Validation

`pipelines/domains/hazards/earthquake_validate.py` checks every record against
the schema and re-derives its identity, digest, number form, origin year,
order, alias uniqueness and flags. It also re-derives the month summary,
latest event date and year state. `tests/domains/hazards/test_earthquake_candidate.py`
covers the monthly plan, boundary ownership, truncation, drift, withholding,
tamper denial and identity stability across revisions.
