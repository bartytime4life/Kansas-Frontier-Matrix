<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/evidence/participatory-planning-weight-receipt
title: ParticipatoryPlanningWeightReceiptCandidate Contract
type: semantic-contract
version: v1.0.0
status: proposed-inactive; fixture-only; no-network; non-authoritative
owners: OWNER_TBD — Evidence steward · Planning-analysis steward · Participation steward
created: 2026-08-11
updated: 2026-08-11
owning_root: contracts/
policy_label: internal; evidence; planning; participation; weights; deliberation
responsibility: Define fixture-only semantics for separate stakeholder-group planning weights, facilitation, dissent, and sensitivity-analysis declarations without creating evidence, policy, review, planning-decision, release, or publication authority.
truth_posture: "CONFIRMED source-card traceability, current-main gap, and repository placement; PROPOSED inactive contract; UNKNOWN consumer adoption; NEEDS VERIFICATION human review and hosted CI"
related:
  - ./planning_proxy_uncertainty_assessment.md
  - ./indicator_definition.md
  - ../governance/public_participation_submission_assessment.md
  - ../../schemas/contracts/v1/evidence/participatory_planning_weight_receipt.schema.json
  - ../../fixtures/contracts/v1/evidence/participatory_planning_weight_receipt/cases.json
  - ../../tools/validators/evidence/validate_participatory_planning_weight_receipt.py
  - ../../tests/validators/evidence/test_validate_participatory_planning_weight_receipt.py
  - ../../docs/intake/exploratory/pass-18-participatory-planning-weight-receipt-source-map.md
[/KFM_META_BLOCK_V2] -->

# ParticipatoryPlanningWeightReceiptCandidate

ParticipatoryPlanningWeightReceiptCandidate is an additive, fixture-only profile for recording separate stakeholder-group criteria weights, facilitation and consent references, dissent, unresolved conflicts, and sensitivity-analysis posture for one bounded planning exercise.

It implements a dependency-closed portion of supplied Pass 18 cards KFM-P18-INV-060, KFM-P18-INV-203, and KFM-P18-INV-421. The cards require planning weights and criteria to remain inspectable, warn that weights encode policy choices rather than neutral GIS truth, and require facilitation, participant-role, deliberation-context, dissent, and uncertainty records.

## Boundary

The profile is PROPOSED_INACTIVE, deterministic, no-network, synthetic, and non-authoritative. A validator PASS means only that the declaration is closed under its schema, its profile hash replays, criteria and stakeholder groups are canonical, every group supplies one normalized basis-point weight for every criterion, and dissent and conflict declarations are locally coherent.

It does not collect participant identities, store raw notes, resolve evidence, infer preferences, aggregate stakeholder groups, calculate a suitability score, rank a place or route, perform sensitivity analysis, determine consensus, evaluate policy, approve review, authorize a planning decision, promote, release, deploy, publish, or authorize public use.

## Core semantics

| Surface | Required posture |
|---|---|
| Planning scope | Purpose, geography, time, scenario, target-population references, and intended output remain explicit and bounded. |
| Method | Method, facilitation, consent, normalization, and sensitivity-analysis posture are declared by reference. |
| Criteria | Criteria are unique and canonically ordered; the profile stores no criterion values or scores. |
| Stakeholder groups | Each group is an opaque reference with one role, consent/evidence references, a complete 10,000-basis-point weight set, and a dissent posture. |
| Deliberation | Group weights remain separate. False consensus and hidden conflicts fail closed. |
| Privacy | Direct identifiers, raw notes, and exact-location payloads are structurally prohibited. |
| Governance | Evidence, policy, review, release, rollback, and fixed-false authority claims remain visible and separate. |

The profile deliberately does not define a stakeholder-role registry, criteria registry, scoring model, planning recommendation, or public release object.

## Finite validation outcomes

| Outcome | Meaning |
|---|---|
| PASS | Shape, identity, canonical ordering, per-group normalization, consent/facilitation references, dissent, conflict disclosure, and sensitivity declarations are locally coherent. Human review remains pending. |
| ABSTAIN | Evidence, consent, facilitation, dissent, or required sensitivity analysis remains incomplete or unresolved. |
| DENY | Criteria coverage, weight totals, group identity, conflict disclosure, no-consensus posture, or governance boundaries conflict. |
| ERROR | The candidate cannot be evaluated safely under the closed machine schema. |

These outcomes are validator results only. They are not participant consent, evidence closure, planning advice, policy decisions, review approval, or release decisions.

## Directory Rules basis

Accepted Directory Rules place semantic meaning under contracts/, machine shape under schemas/, synthetic replay under fixtures/, executable validation under tools/, conformance checks under tests/, CI orchestration under .github/, source reconciliation under docs/, and authoring accountability under data/receipts/generated/.

Evidence owns this candidate because its one responsibility is preserving how stakeholder-derived planning weights were declared and bounded. It does not create a planning, participation, policy, source, review, release, or publication authority home.

## Validation

    python -m unittest tests.validators.evidence.test_validate_participatory_planning_weight_receipt -v
    python tools/validators/evidence/validate_participatory_planning_weight_receipt.py --fixtures

## Rollback

Revert the additive packet. It has no runtime consumer and mutates no participant record, source, evidence, planning product, policy, review, lifecycle, catalog, release, deployment, cache, or public artifact.
