<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/evidence/correlation-claim-boundary-assessment
title: CorrelationClaimBoundaryAssessmentCandidate Contract
type: semantic-contract
version: v1.0.0
status: proposed-inactive; fixture-only; no-network; non-authoritative
owners: OWNER_TBD — Evidence steward · Analytics steward · Scientific-review steward · Validation steward
created: 2026-08-11
updated: 2026-08-11
owning_root: contracts/
policy_label: internal; evidence; analytics; correlation; causality-boundary; disclosure
responsibility: Define a fixture-only claim-language assessment that keeps one correlation statistic in a relationship-evidence role and routes stronger contribution, exposure, or causal wording to abstention or denial without creating causal, evidence, policy, review, release, or publication authority.
truth_posture: "CONFIRMED supplied-card traceability and repository placement; PROPOSED inactive contract; UNKNOWN consumer adoption and causal-design sufficiency rules; NEEDS VERIFICATION human review and hosted CI"
related:
  - ./analytic_output_disclosure_assessment.md
  - ../common/condition_relation.md
  - ../../schemas/contracts/v1/evidence/correlation_claim_boundary_assessment.schema.json
  - ../../fixtures/contracts/v1/evidence/correlation_claim_boundary_assessment/cases.json
  - ../../tools/validators/evidence/validate_correlation_claim_boundary_assessment.py
  - ../../tests/validators/evidence/test_validate_correlation_claim_boundary_assessment.py
  - ../../docs/intake/exploratory/pass-18-correlation-claim-boundary-assessment-source-map.md
[/KFM_META_BLOCK_V2] -->

# CorrelationClaimBoundaryAssessmentCandidate

`CorrelationClaimBoundaryAssessmentCandidate` is an additive, fixture-only profile for assessing how one correlation statistic may be described. It keeps the statistic in a `RELATIONSHIP_EVIDENCE` role and prevents a coefficient from silently becoming a claim of contribution, exposure, or cause.

It implements the smallest reviewable portion of supplied Pass 18 card `KFM-P18-INV-158`: correlation aggregates should support relationship language, while stronger wording must be denied or held for a separate causal-design review.

## Composition, not parallel authority

The repository already has two adjacent boundaries:

- `AnalyticOutputDisclosureAssessment` binds a statistic to method, assumptions, uncertainty, validation, citations, and `NO_CAUSAL_CLAIM`; and
- `ConditionRelation` carries a typed contextual relation and denies causal requests.

This profile does not replace either object. It pins both by reference and adds only the missing correlation-specific seam: registered method kind, requested claim role, wording class, causal-design posture, caveats, and finite handoff outcome. A local `resolution: RESOLVED` value is candidate metadata, not proof that the referenced object exists or is valid; this no-network validator performs no resolution.

## Boundary

The profile is `PROPOSED_INACTIVE`, no-network, and non-authoritative. A validator `PASS` means only that:

- the candidate is closed under this schema and its canonical profile hash replays;
- the statistic is explicitly labeled `RELATIONSHIP_EVIDENCE`;
- analytic-output, condition-relation, method-registry, and uncertainty bindings carry resolved candidate states;
- a correlation method kind is named without embedding observations or recomputing a coefficient;
- the requested role, wording class, and permitted role agree;
- association caveats include correlation/causation, confounding, and scope boundaries;
- public or release-review candidates carry the required review-reference prerequisites; and
- caveat, evidence, and review references are canonically ordered.

It does **not** calculate a statistic, inspect raw observations, resolve any reference, determine whether confounding is controlled, decide whether a causal design is sufficient, establish relationship or causal truth, approve evidence, policy, or review, promote, release, deploy, publish, or authorize public use.

## Claim-role matrix

| Requested role | Wording class | Local outcome boundary |
|---|---|---|
| `ASSOCIATION` | `ASSOCIATIONAL` | May `PASS` when composition bindings and caveats are complete. |
| `CONTRIBUTION` | `CONTRIBUTION_OR_EXPOSURE` | Always `ABSTAIN`; missing, unresolved, or resolved design evidence still requires a separate stronger-claim review. |
| `EXPOSURE` | `CONTRIBUTION_OR_EXPOSURE` | Always `ABSTAIN` under the same stronger-claim boundary. |
| `CAUSE` | `CAUSAL` | `DENY` when no design is supplied or only an observational design is declared; `ABSTAIN` when design identity is unresolved or a stronger design awaits review. |
| Any role | `AMBIGUOUS` | `ABSTAIN`; wording must be classified before use. |

No causal request can `PASS` in version 1. A `RESOLVED` quasi-experimental, randomized, mechanistic, or other design reference still yields `CAUSAL_DESIGN_REVIEW_REQUIRED`. The profile deliberately does not define “sufficient causal evidence,” because Pass 18 marks that question `NEEDS VERIFICATION` and the repository has no accepted causal-design authority for this composition.

## Method and design vocabularies

The correlation method kinds are `PEARSON_R`, `SPEARMAN_RHO`, `KENDALL_TAU`, and `OTHER_REGISTERED`. They name the method family only. The candidate stores no coefficient, p-value, sample, row, coordinate, predictor, response, or real-world claim text.

Causal-design classes are `OBSERVATIONAL`, `QUASI_EXPERIMENTAL`, `RANDOMIZED_EXPERIMENT`, `MECHANISTIC`, and `OTHER`, plus explicit `NOT_PROVIDED` and `UNKNOWN` states. Classification does not validate design quality or transfer scientific-review authority to this profile.

## Finite validation outcomes

| Outcome | Meaning |
|---|---|
| `PASS` | A bounded association disclosure is internally coherent and all fixed authority claims remain false. |
| `ABSTAIN` | A composition reference, disclosure, wording class, or stronger-design review prerequisite is unresolved. |
| `DENY` | Unsupported causal wording, an observational cause claim, missing required caveat/review prerequisite, identity drift, or canonicalization failure occurs. |
| `ERROR` | The candidate cannot be evaluated safely under the closed machine schema. |

These outcomes are language-boundary validator states. They are not statistical findings, evidence decisions, causal conclusions, policy decisions, review decisions, or release states.

## Directory Rules basis

This object assesses the evidence and interpretation limits of a derived statistic, so meaning belongs under `contracts/evidence/`; shape under `schemas/contracts/v1/evidence/`; synthetic cases under `fixtures/contracts/v1/evidence/`; reusable validation under `tools/validators/evidence/`; executable checks under `tests/validators/evidence/`; read-only orchestration under `.github/workflows/`; source reconciliation under `docs/intake/exploratory/`; and authoring accountability under `data/receipts/generated/`.

These are existing responsibility roots adopted by ADR-0029. No analytics root, method registry, causal-design authority, evidence store, policy home, release lane, API, UI surface, or publication path is created.

## Validation

```bash
python -m unittest tests.validators.evidence.test_validate_correlation_claim_boundary_assessment -v
python tools/validators/evidence/validate_correlation_claim_boundary_assessment.py --fixtures
```

## Rollback

Revert the additive profile packet. It has no consumer and mutates no observation, analytic output, condition relation, evidence, policy, review, lifecycle, catalog, release, cache, route, deployment, or public artifact.
