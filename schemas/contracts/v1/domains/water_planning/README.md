# `schemas/contracts/v1/domains/water_planning/` — Kansas Water-Planning Domain Schemas

> Schema files for the Kansas water-planning and infrastructure-funding domain. All schemas are **PROPOSED** scaffolds for issue #1647. No source admission, release, or publication is authorized by these schemas.

## Status

**PROPOSED / draft.** Slice 4 adds bounded RAC identity and region/project reference coherence checks. The schemas remain unpromoted, and broader implementation remains blocked by bartytime4life/Kansas-Frontier-Matrix#1675 except for an exact recorded candidate-PR authorization.

## Schemas

| Schema | Entity | Title |
|---|---|---|
| [`planning_region.schema.json`](./planning_region.schema.json) | `PlanningRegion` | Exact 14-record RAC ID shape plus explicit geometry/county-crosswalk states |
| [`public_meeting.schema.json`](./public_meeting.schema.json) | `PublicMeeting` | KWO public meeting events |
| [`advisory_committee_meeting.schema.json`](./advisory_committee_meeting.schema.json) | `AdvisoryCommitteeMeeting` | RAC advisory meeting events |
| [`program_version.schema.json`](./program_version.schema.json) | `ProgramVersion` | Versioned grant program (HB 2462 creates new version) |
| [`scoring_matrix_version.schema.json`](./scoring_matrix_version.schema.json) | `ScoringMatrixVersion` | Digest-linked scoring matrix versions |
| [`application_window.schema.json`](./application_window.schema.json) | `ApplicationWindow` | Open/close window with Central Time (FY2027: 2026-09-15T23:59:00-05:00) |
| [`application.schema.json`](./application.schema.json) | `Application` | Grant application with explicit unresolved geometry/identity state |
| [`eligibility_decision.schema.json`](./eligibility_decision.schema.json) | `EligibilityDecision` | Finite eligibility outcome (eligible/ineligible/pending) |
| [`recommendation.schema.json`](./recommendation.schema.json) | `Recommendation` | Advisory recommendation (distinct from award) |
| [`award.schema.json`](./award.schema.json) | `Award` | Grant award (distinct from payment and project) |
| [`funding_agreement.schema.json`](./funding_agreement.schema.json) | `FundingAgreement` | Agreement with paid_amount (distinct from awarded_amount) |
| [`project.schema.json`](./project.schema.json) | `Project` | Separate explicit RAC-membership and project-location resolution states |
| [`construction_milestone.schema.json`](./construction_milestone.schema.json) | `ConstructionMilestone` | Construction progress milestone |
| [`completion.schema.json`](./completion.schema.json) | `Completion` | Project completion (distinct from payment and benefit) |
| [`correction_or_withdrawal.schema.json`](./correction_or_withdrawal.schema.json) | `CorrectionOrWithdrawal` | Digest-linked correction/withdrawal records |

## Slice 4 authority boundary

- `PlanningRegion.region_id` and `Project.planning_region_ref` admit only `kwo-rac-01` through `kwo-rac-14`.
- `rac_number` is a KFM stable ordinal pinned by the identity inventory; it is not represented as a KWO-native number.
- Unresolved geometry requires a null reference. Approximate or confirmed geometry requires a non-null reference.
- County-crosswalk and project-region resolution states are explicit and coherent with their nullable references.
- Referential integrity, authority version/digest/correction metadata, exact source-grounded names, GMD/RAC separation, inline-geometry denial, and non-echoing findings are enforced by the deterministic validator rather than JSON Schema alone.
- No real geometry or county membership is included. CI wiring is not part of this slice.

```bash
python tools/validators/domains/water_planning/validate_geometry_authority.py \
  fixtures/domains/water_planning/geometry_authority/valid/valid_1.json

python -m unittest discover \
  --start-directory tests/domains/water_planning \
  --pattern 'test_geometry_authority.py' \
  --verbose
```

## Related

- [`contracts/domains/water_planning/`](../../../../../contracts/domains/water_planning/) — Contract documents
- [`fixtures/domains/water_planning/`](../../../../../fixtures/domains/water_planning/) — Synthetic fixtures
- [`fixtures/domains/water_planning/geometry_authority/`](../../../../../fixtures/domains/water_planning/geometry_authority/) — Slice 4 authority fixtures
- [`tools/validators/domains/water_planning/validate_geometry_authority.py`](../../../../../tools/validators/domains/water_planning/validate_geometry_authority.py) — Slice 4 validator
- [`tests/domains/water_planning/test_geometry_authority.py`](../../../../../tests/domains/water_planning/test_geometry_authority.py) — Slice 4 tests
- [`tests/schemas/test_water_planning_contracts.py`](../../../../../tests/schemas/test_water_planning_contracts.py) — Schema tests
- [`docs/sources/catalog/kansas/kwo.md`](../../../../../docs/sources/catalog/kansas/kwo.md) — KWO source catalog entry
