# Pass 31 STAC search behavior fixture — source map

Status: **PROPOSED / INACTIVE / FIXTURE-ONLY**  
Implementation date: 2026-08-09

| Source | Stable identifier | Extracted requirement | Implemented surface |
|---|---|---|---|
| `KFM_Domains_v1_1_plus_Pass23_Pass32_Consolidated_Atlas.pdf` | `KFM-P31-PROG-0005` | Build STAC API smoke fixtures for bbox/time search, fields inclusion/exclusion, stable sort paging, and filter/query constraints. | Contract, closed schema, deterministic validator, two positive and thirteen negative cases, unit tests, path-filtered CI, and generated receipt. |
| Same card | `sha256:df00897c204c95a693a4e86012d0ac6e2c57a2866478bfd0f55dce3d4b172db3` | Preserve the source card's specification identity. | Recorded in contract metadata and receipt citation; not substituted for artifact identity. |
| Drive `Directory Rules` | `1uTqdIEFZE2cq3gyISetoRYM6LIlnKqTc3FobtEx7Cbs` | Put semantic meaning, machine shape, fixtures, validators, tests, workflows, and receipts in their established ownership roots. | Paths remain under the existing `contracts/data`, `schemas/contracts/v1/data`, `fixtures/contracts/v1/data`, `tools/validators/stac`, `tests/validators/stac`, `.github/workflows`, and `data/receipts/generated` roots. |

## Deliberate non-effects

- No HTTP client or network call is introduced.
- No live STAC server or extension conformance is asserted.
- No catalog record is created, changed, admitted, promoted, released, or published.
- No policy or human review decision is made.
