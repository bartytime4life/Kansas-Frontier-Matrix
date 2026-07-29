# `contracts/domains/water_planning/` — Kansas Water-Planning Domain Contracts

> Semantic contracts for the Kansas water-planning and infrastructure-funding domain. All contracts are **PROPOSED** scaffolds. They define object meaning for entities modeled in the water-planning epic (issue #1647, Slice 2). They do not constitute source admission, release approval, or publication authorization.

## Status

**PROPOSED / draft.** Implementation is deferred and blocked by bartytime4life/Kansas-Frontier-Matrix#1675 until platform controls are verified.

## Entity contracts

| Contract | Entity type | Schema |
|---|---|---|
| [`planning_region.md`](./planning_region.md) | `PlanningRegion` | `schemas/contracts/v1/domains/water_planning/planning_region.schema.json` |
| [`public_meeting.md`](./public_meeting.md) | `PublicMeeting` | `schemas/contracts/v1/domains/water_planning/public_meeting.schema.json` |
| [`advisory_committee_meeting.md`](./advisory_committee_meeting.md) | `AdvisoryCommitteeMeeting` | `schemas/contracts/v1/domains/water_planning/advisory_committee_meeting.schema.json` |
| [`program_version.md`](./program_version.md) | `ProgramVersion` | `schemas/contracts/v1/domains/water_planning/program_version.schema.json` |
| [`scoring_matrix_version.md`](./scoring_matrix_version.md) | `ScoringMatrixVersion` | `schemas/contracts/v1/domains/water_planning/scoring_matrix_version.schema.json` |
| [`application_window.md`](./application_window.md) | `ApplicationWindow` | `schemas/contracts/v1/domains/water_planning/application_window.schema.json` |
| [`application.md`](./application.md) | `Application` | `schemas/contracts/v1/domains/water_planning/application.schema.json` |
| [`eligibility_decision.md`](./eligibility_decision.md) | `EligibilityDecision` | `schemas/contracts/v1/domains/water_planning/eligibility_decision.schema.json` |
| [`recommendation.md`](./recommendation.md) | `Recommendation` | `schemas/contracts/v1/domains/water_planning/recommendation.schema.json` |
| [`award.md`](./award.md) | `Award` | `schemas/contracts/v1/domains/water_planning/award.schema.json` |
| [`funding_agreement.md`](./funding_agreement.md) | `FundingAgreement` | `schemas/contracts/v1/domains/water_planning/funding_agreement.schema.json` |
| [`project.md`](./project.md) | `Project` | `schemas/contracts/v1/domains/water_planning/project.schema.json` |
| [`construction_milestone.md`](./construction_milestone.md) | `ConstructionMilestone` | `schemas/contracts/v1/domains/water_planning/construction_milestone.schema.json` |
| [`completion.md`](./completion.md) | `Completion` | `schemas/contracts/v1/domains/water_planning/completion.schema.json` |
| [`correction_or_withdrawal.md`](./correction_or_withdrawal.md) | `CorrectionOrWithdrawal` | `schemas/contracts/v1/domains/water_planning/correction_or_withdrawal.schema.json` |

## Anti-collapse boundaries

A meeting is not an approval. An application is not an award. An award is not a completed project. A scoring matrix is not a project outcome. A recipient list is not proof of payment, construction, or operational benefit.

| Boundary | Entities kept distinct |
|---|---|
| Meeting ≠ decision | `PublicMeeting`, `AdvisoryCommitteeMeeting` vs. `EligibilityDecision`, `Award` |
| Application ≠ award | `Application`, `ApplicationWindow` vs. `Award`, `FundingAgreement` |
| Award ≠ payment | `Award` vs. `FundingAgreement` (paid_amount) |
| Award ≠ project | `Award` vs. `Project` |
| Project ≠ completion | `Project` vs. `Completion` |
| Scoring matrix ≠ outcome | `ScoringMatrixVersion` vs. `Application`, `Award`, `Project` |
| Program version ≠ scoring matrix | `ProgramVersion` vs. `ScoringMatrixVersion` |

## Related

- [`docs/sources/catalog/kansas/kwo.md`](../../../docs/sources/catalog/kansas/kwo.md) — KWO source catalog entry
- [`schemas/contracts/v1/domains/water_planning/`](../../../schemas/contracts/v1/domains/water_planning/) — Schemas
- [`fixtures/domains/water_planning/`](../../../fixtures/domains/water_planning/) — Synthetic fixtures
- [`tests/schemas/test_water_planning_contracts.py`](../../../tests/schemas/test_water_planning_contracts.py) — Tests
