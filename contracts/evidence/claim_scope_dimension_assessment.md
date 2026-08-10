<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/evidence/claim-scope-dimension-assessment
title: ClaimScopeDimensionAssessmentCandidate Contract
type: semantic-contract
version: v1.0.0
status: proposed-inactive; fixture-only; no-network; non-authoritative
owners: OWNER_TBD — Evidence steward · Spatial representation steward · Validation steward
created: 2026-08-10
updated: 2026-08-10
owning_root: contracts/
policy_label: internal; evidence; claim-scope; time-space-attribute
responsibility: Define a fixture-only declaration assessment that makes the controlled, measured, and unresolved roles of time, space, and attribute explicit without creating evidence, policy, review, release, or publication authority.
truth_posture: "CONFIRMED supplied-card traceability and repository placement; PROPOSED inactive contract; UNKNOWN consumer adoption; NEEDS VERIFICATION human review and hosted CI"
related:
  - ./measurement_scale_operation_assessment.md
  - ./representation_fitness_assessment.md
  - ../../schemas/contracts/v1/evidence/claim_scope_dimension_assessment.schema.json
  - ../../fixtures/contracts/v1/evidence/claim_scope_dimension_assessment/cases.json
  - ../../tools/validators/evidence/validate_claim_scope_dimension_assessment.py
  - ../../tests/validators/evidence/test_validate_claim_scope_dimension_assessment.py
  - ../../docs/intake/exploratory/pass-18-claim-scope-dimension-assessment-source-map.md
[/KFM_META_BLOCK_V2] -->

# ClaimScopeDimensionAssessmentCandidate

`ClaimScopeDimensionAssessmentCandidate` records how one synthetic claim declaration treats the time, space, and attribute dimensions: each dimension is `CONTROLLED`, `MEASURED`, or `UNRESOLVED`. It implements the smallest reviewable portion of supplied Pass 18 card `KFM-P18-INV-376`.

## Boundary

A validator `PASS` proves only that the candidate's closed shape, deterministic identity, declared EvidenceBundle-scope reference, dimension roles, assessment partition, disclosure obligations, and fixed-false authority declarations are internally coherent.

It does not inspect observations, infer scope, resolve or authenticate an EvidenceBundle, evaluate spatial or temporal fitness, calculate an attribute, approve review, change lifecycle state, release, publish, or authorize a public claim. The profile stores references and digests, not coordinates, observed values, or source payloads.

## Dimension-role declaration

| Role | Local meaning |
|---|---|
| `CONTROLLED` | The declaration says the dimension is fixed or bounded for the claim. |
| `MEASURED` | The declaration says the claim varies or is sampled across the dimension. |
| `UNRESOLVED` | The declaration cannot yet establish the dimension's role and must abstain or remain incomplete. |

A complete assessment requires at least one controlled and one measured dimension. This is a conservative fixture rule for visible scope metadata, not a universal scientific classification.

## Finite validator outcomes

| Outcome | Meaning |
|---|---|
| `PASS` | The declared scope roles, partition, references, and obligations are locally coherent. |
| `ABSTAIN` | The assessment or a declared scope dependency remains incomplete, unknown, or unresolved. |
| `DENY` | A complete declaration has a contradictory role, partition, disclosure, or review posture. |
| `ERROR` | The candidate cannot be evaluated under the closed schema. |

These outcomes are not evidence, policy, review, lifecycle, release, publication, or public-answer decisions.

## Directory Rules basis

Semantic meaning belongs under `contracts/evidence/`; machine shape under `schemas/contracts/v1/evidence/`; synthetic cases under `fixtures/contracts/v1/evidence/`; validation under `tools/validators/evidence/`; executable conformance evidence under `tests/validators/evidence/`; orchestration under `.github/workflows/`; source reconciliation under `docs/intake/exploratory/`; and authoring accountability under `data/receipts/generated/`.

The profile is adjacent to representation-fitness and measurement-scale assessments but does not modify them or create a parallel claim, layer, EvidenceBundle, policy, release, or publication authority.

## Validation

```bash
python -m unittest tests.validators.evidence.test_validate_claim_scope_dimension_assessment -v
python tools/validators/evidence/validate_claim_scope_dimension_assessment.py --fixtures
```

## Rollback

Revert the additive packet. It has no runtime consumer and changes no source value, evidence object, lifecycle state, map, policy, release, deployment, or public artifact.
