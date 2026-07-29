# `schemas/contracts/v1/domains/water_planning/` — Kansas Water-Planning Domain Schemas

> Schema files for the Kansas water-planning and infrastructure-funding domain. All schemas are **PROPOSED** scaffolds that define the data model for the water-planning modeling epic (issue #1647, Slice 2). No source admission, release, or publication is authorized by these schemas.

## Status

**PROPOSED / draft.** Implementation is deferred and blocked by bartytime4life/Kansas-Frontier-Matrix#1675 until platform controls are verified.

## Schemas

| Schema | Entity | Title |
|---|---|---|
| [`planning_region.schema.json`](./planning_region.schema.json) | `PlanningRegion` | 14 RAC planning areas |
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
| [`project.schema.json`](./project.schema.json) | `Project` | Infrastructure project with explicit geometry confidence |
| [`construction_milestone.schema.json`](./construction_milestone.schema.json) | `ConstructionMilestone` | Construction progress milestone |
| [`completion.schema.json`](./completion.schema.json) | `Completion` | Project completion (distinct from payment and benefit) |
| [`correction_or_withdrawal.schema.json`](./correction_or_withdrawal.schema.json) | `CorrectionOrWithdrawal` | Digest-linked correction/withdrawal records |

## Related

- [`contracts/domains/water_planning/`](../../../../../contracts/domains/water_planning/) — Contract documents
- [`fixtures/domains/water_planning/`](../../../../../fixtures/domains/water_planning/) — Synthetic fixtures
- [`tests/schemas/test_water_planning_contracts.py`](../../../../../tests/schemas/test_water_planning_contracts.py) — Tests
- [`docs/sources/catalog/kansas/kwo.md`](../../../../../docs/sources/catalog/kansas/kwo.md) — KWO source catalog entry
