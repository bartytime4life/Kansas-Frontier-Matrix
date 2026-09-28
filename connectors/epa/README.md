<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/connectors-epa-readme
title: connectors/epa/ README
type: readme
version: v0.1
status: draft
owners: OWNER_TBD
created: 2026-06-16
updated: 2026-06-16
policy_label: public
related:
  - ../README.md
  - ../../docs/sources/catalog/epa/README.md
  - ../../data/raw/
  - ../../data/quarantine/
tags: [kfm, connectors, epa, source-admission]
notes:
  - "Source intake lane only."
  - "Outputs are limited to raw or quarantine admission lanes."
[/KFM_META_BLOCK_V2] -->

# EPA Connector

> Source-specific intake and admission lane for EPA source programs used by KFM.

`connectors/epa/`

> [!NOTE]
> **Descriptor resolved (2026-09-28).** `src/epa/descriptor.yaml` now sets `role: aggregate` and `rights: public-domain-us-government-work` (U.S. federal works, 17 U.S.C. 105), as chosen by the repository owner. `admit.admit()` therefore returns its provisional `RAW_CANDIDATE` or `QUARANTINE_CANDIDATE` route instead of `HOLD`; an unresolved descriptor still holds every route. Routing remains no write, no admission, and no coverage claim. This is not a SourceDescriptor, source activation, sensitivity review, or release, and earlier notes that say routes end at `HOLD` describe the unresolved state.

> [!NOTE]
> **AQS AirData daily-summary retrieval and routing (2026-09-28; supersedes the placeholder statements for `fetch.py`, `admit.py`, and `pyproject.toml`; family placement (`OPEN-DSC-09`), the `connectors/epa_aqs/` relationship, and activation are still open).**
> - **`aqs_airdata.daily_url(parameter, year)`:** plans one pre-generated `https://aqs.epa.gov/aqsweb/airdata/daily_<parameter>_<year>.zip` GET, for criteria-pollutant parameter codes only (`42101`, `42401`, `42602`, `44201`, `81102`, `88101`, `88502`) from 1980 on. The AQS API is not planned, because it needs an account e-mail and key in the query string.
> - **`aqs_airdata.parse_daily_file(...)`:** parses a *supplied* archive:
>   - the archive must hold exactly one unencrypted `daily_<parameter>_<year>.csv` member, within decompressed-size and compression-ratio bounds;
>   - the national CSV is streamed, every row must match the file's parameter code, and only rows EPA attributes to Kansas (`State Code` `20`) are classified;
>   - numbers stay exact `Decimal`s with every source column kept verbatim, and a blank AQI stays blank, never zero;
>   - event treatment (`No Events`/`Events Included`/`Events Excluded`/`Concurred Events Excluded`, or the short forms `None`/`Included`/`Excluded`/`Concurred`) and a blank AQI are flags; an unreadable number or coordinate, or an unknown event type, makes that row a quarantine candidate;
>   - a bad archive, header, identity, date outside the file year, or duplicate row identity rejects the whole file.
>
>   The archive layout, column set, event-type vocabulary and row identity are **NEEDS VERIFICATION** against current AirData documentation.
> - **`fetch.retrieve(url)`:** accepts only the planner's exact URL (`application/zip` or `application/x-zip-compressed`), runs through `connectors_core.transport` with caller-injected effects, and records under `epa.aqs-airdata-daily`.
> - **`admit.admit()`:** re-applies the URL rule, then routes:
>   - a parsed archive becomes `RAW_CANDIDATE`, flagged `RECORD_QUARANTINE_CANDIDATES`, `EVENT_TREATED_ROWS_PRESENT`, `AQI_NOT_REPORTED_PRESENT` or `NO_KANSAS_ROWS` when they apply;
>   - parser rejections become `QUARANTINE_CANDIDATE`;
>   - uncaptured retrievals become `HOLD`.
> - **Holds:** the final route is `HOLD` while `role` or `rights` is unresolved. A daily summary is a monitor statistic, never area truth, exposure, or attainment.
> - **Scope:** no network library, write, or admission. Tests: `connectors/epa/tests/test_aqs_airdata.py`, `test_fetch_admit.py`, run by `.github/workflows/epa-connector-offline.yml`.

## Scope

This folder may contain connector-local documentation and source-admission helpers for EPA source material.

It must not become source truth, domain doctrine, policy authority, schema authority, catalog authority, triplet authority, proof authority, release authority, pipeline authority, or publication authority.

## Repo fit

```text
connectors/
└── epa/
    └── README.md
```

Related roots:

```text
connectors/              # source-specific fetch and admission code
docs/sources/catalog/epa/# source-family documentation
data/raw/                # raw staged outputs
data/quarantine/         # held material requiring review
policy/                  # policy rules
release/                 # release decisions
```

## Authority boundary

```text
OUTPUT LIMIT:
  data/raw/
  data/quarantine/

NOT HERE:
  processed data
  catalog records
  triplet records
  proof authority
  release decisions
  published artifacts
  policy rules
  schemas/contracts
  source registry rows
  generated reports
```

## Inputs

| Accepted item | Required posture |
|---|---|
| Source adapter | Preserve source identity and review posture. |
| Admission helper | Prepare raw or quarantine admission output only. |
| Connector docs | Do not claim admission or release state unless verified. |

## Exclusions

| Do not store here | Correct home |
|---|---|
| Source-family documentation | `docs/sources/catalog/epa/` |
| Source descriptors | `data/registry/sources/` |
| Processed records | `data/processed/` |
| Catalog or triplet records | `data/catalog/`, `data/triplets/` |
| Release decisions | `release/` |
| Policy rules | `policy/` |
| Generated reports | `artifacts/` |

## Validation

Before relying on this connector, verify source descriptors, endpoint assumptions, tests, fixtures, output paths, and downstream receipt/proof/release ownership.

## Status summary

`connectors/epa/` is for source-admission code only. It is not source truth, policy authority, schema authority, catalog/triplet authority, proof closure, release authority, publication authority, or pipeline authority.
