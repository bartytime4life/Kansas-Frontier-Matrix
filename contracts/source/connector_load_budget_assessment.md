<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/source/connector-load-budget-assessment
title: ConnectorLoadBudgetAssessment Candidate Contract
type: semantic-contract
version: v1.0.0
status: proposed-inactive; fixture-only; no-network; non-authoritative
owners: OWNER_TBD — Source steward · Connector steward · Acquisition steward · Validation steward
created: 2026-08-11
updated: 2026-08-11
owning_root: contracts/
policy_label: internal; source; connector; load-budget; rate-limit; stewardship
responsibility: Define fixture-only coherence checks for a requested connector concurrency level against one declared per-source load budget without contacting a source or granting activation, scheduling, lifecycle, policy, review, release, or publication authority.
truth_posture: "CONFIRMED supplied-card traceability and repository placement; PROPOSED inactive assessment; UNKNOWN consumer adoption; NEEDS VERIFICATION steward review and hosted exact-head CI"
related:
  - ./web_acquisition_conduct_assessment.md
  - ./source_descriptor.md
  - ../../docs/standards/connector-rate-limits.md
  - ../../schemas/contracts/v1/source/connector_load_budget_assessment.schema.json
  - ../../fixtures/contracts/v1/source/connector_load_budget_assessment/cases.json
  - ../../tools/validators/source/validate_connector_load_budget_assessment.py
  - ../../tests/validators/test_validate_connector_load_budget_assessment.py
  - ../../docs/intake/exploratory/pass-18-connector-load-budget-assessment-source-map.md
[/KFM_META_BLOCK_V2] -->

# ConnectorLoadBudgetAssessment Candidate

`ConnectorLoadBudgetAssessmentCandidate` is an additive, fixture-only profile for checking whether one proposed connector execution is bounded by a shared per-source load budget.

It adapts the smallest reviewable intersection of supplied Pass 18 cards `KFM-P18-INV-217`, `KFM-P18-INV-372`, `KFM-P18-INV-422`, and `KFM-P18-INV-447`: concurrency is a source-stewardship constraint, and threaded or distributed acquisition must not multiply a per-worker allowance into an undeclared source-wide load.

## Boundary

A validator `PASS` means only that the candidate declaration is closed, content-addressed, internally coherent, and that its requested concurrency does not exceed its declared per-source ceiling. It does not resolve the referenced source, conduct assessment, policy, terms, review, or activation record.

The profile performs no DNS lookup, network request, sleep, retry, scheduling, connector execution, source admission, payload capture, lifecycle write, evidence or policy decision, review approval, release, deployment, publication, or public-use authorization.

`WebAcquisitionConductAssessmentCandidate` continues to own route, terms, robots, identity, proxy, and distribution-conduct declarations. This profile composes that result by opaque reference and adds only the source-wide execution-budget relationship.

## Closed budget axes

| Axis | Required declaration |
|---|---|
| Execution | Single-worker, threaded, or distributed mode; worker count; and requested concurrency. |
| Scope | A declared budget applies to the source as a whole. Per-worker scope is denied. |
| Pace | Maximum concurrency, minimum inter-request delay, and request-window capacity. |
| Retry | Strategy, attempt cap, bounded backoff, and mandatory `Retry-After` compliance. |
| Coordination | Distributed execution carries one shared coordination key; non-distributed execution carries none. |
| Stop posture | Canonically ordered stop conditions include budget exhaustion, manual cancellation, source throttling, and terms change. |
| Dependencies | The referenced conduct assessment and human review are declared as `PASS`/complete, unresolved, or denied states. |

`SOURCE_POLICY` and `UNRESOLVED` budget states intentionally abstain. A referenced policy is not silently dereferenced or converted into local numeric authority by this validator.

## Finite outcomes

| Outcome | Meaning |
|---|---|
| `PASS` | The declared request fits a closed per-source budget and its dependency declarations are complete. |
| `ABSTAIN` | Budget values, conduct posture, or review remain unresolved. |
| `DENY` | The declaration exceeds the budget, uses per-worker scope, omits shared coordination, weakens retry/stop controls, reports denied conduct, or is internally contradictory. |
| `ERROR` | The candidate cannot be evaluated safely under the closed schema. |

These are fixture validation outcomes only. They are not source, legal, activation, scheduling, policy, review, promotion, release, or publication decisions.

## Directory Rules basis

Source-acquisition budget meaning belongs under `contracts/source/`; machine shape, synthetic cases, repository validation, executable tests, CI orchestration, source reconciliation, and generated accountability remain in their established responsibility roots.

No connector, scheduler, source registry, policy surface, lifecycle lane, receipt authority, release lane, or public route is created.

## Validation

```bash
python -m unittest tests.validators.test_validate_connector_load_budget_assessment -v
python tools/validators/source/validate_connector_load_budget_assessment.py --fixtures
```

## Rollback

Revert the additive packet. It has no runtime consumer and mutates no source, connector, schedule, registry, payload, lifecycle state, evidence, policy, review, release, deployment, or public artifact.
