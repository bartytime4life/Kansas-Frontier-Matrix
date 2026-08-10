<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/source/source-activation-portfolio-assessment
title: Source Activation Portfolio Assessment Candidate Contract
type: semantic-contract
version: v0.1.0
status: proposed; inactive; fixture-only; review-required
owners: OWNER_TBD - Source steward; Rights steward; Sensitivity steward; Review steward; Contract steward; Validation steward
created: 2026-08-10
updated: 2026-08-10
policy_label: public; source; portfolio; review-planning; fail-closed; no-activation
owning_root: contracts/
responsibility: Define a bounded assessment that preserves source-specific rights, role, sensitivity, reviewer, dependency, acceptance-test, correction, and rollback posture across a small cross-domain review portfolio without activating or ranking a source.
truth_posture: CONFIRMED synthetic validator behavior / PROPOSED inactive portfolio profile / NEEDS VERIFICATION source and governance steward adoption, real source records, qualified reviewer policy, and hosted exact-head execution
related:
  - ./source_activation_decision.md
  - ./source_rights_currentness_assessment.md
  - ../governance/verification_convergence_plan.md
  - ../../schemas/contracts/v1/source/source_activation_portfolio_assessment.schema.json
  - ../../fixtures/contracts/v1/source/source_activation_portfolio_assessment/cases.json
  - ../../tools/validators/source/validate_source_activation_portfolio_assessment.py
  - ../../tests/validators/test_validate_source_activation_portfolio_assessment.py
  - ../../docs/intake/exploratory/source-activation-portfolio-assessment-source-map.md
tags: [kfm, source, portfolio, review-readiness, rights, sensitivity, correction, rollback, fixture-only]
notes:
  - "Adapts the bounded source-review portfolio proposal retained from the Comprehensive Research and Verification Report."
  - "All candidates and references are synthetic and non-joinable; no endpoint, credential, private record, or exact sensitive location is present."
[/KFM_META_BLOCK_V2] -->

# Source Activation Portfolio Assessment Candidate

> A deterministic, fixture-only profile for composing two or three source-review candidates without turning portfolio order, completeness, or validator success into source authority.

## Purpose

`SourceActivationDecision` evaluates one operation for one source. `VerificationConvergencePlan` selects a small set of general verification tasks. This candidate owns a narrower missing responsibility: determine whether a small cross-domain set of source-specific review packets is internally ready to be reviewed while preserving every hold, denied class, qualified-review requirement, dependency, acceptance test, correction path, and rollback path.

It is not a scorecard, source registry, admission decision, scheduler, connector plan, policy decision, review approval, or release object.

## Finite outcomes

| Outcome | Validator result | Meaning |
|---|---|---|
| `READY_FOR_REVIEW` | `PASS` | Every synthetic candidate is complete for human review; no source is activated. |
| `CONDITIONAL` | `ABSTAIN` | At least one candidate retains an explicit upstream or risk-class review condition. |
| `HOLD` | `ABSTAIN` | At least one denied, unknown, or unresolved source condition must remain held. |
| `ERROR` | `ERROR` | A trustworthy portfolio assessment was not produced. |
| malformed or contradictory packet | `DENY` | Shape, identity, ordering, reference, partition, derived-outcome, or authority invariants failed. |

The portfolio outcome is the least permissive candidate outcome: `ERROR`, then `HOLD`, then `CONDITIONAL`, then `READY_FOR_REVIEW`. A lower-risk source cannot override a held or denied class.

## Invariants

1. A portfolio contains two or three synthetic sources sorted by stable source ID; it does not assign a numeric score or hidden weight.
2. Source descriptor, role, rights/currentness, sensitivity, reviewer, dependency, acceptance-test, correction, and rollback references remain distinct.
3. `DENIED_CLASS` always remains `HOLD`.
4. `HIGH_RISK` always remains at least `CONDITIONAL`, even when its packet is complete.
5. A held or denied readiness declaration cannot be overridden by candidate order or another source's readiness.
6. Candidate outcome and reason code are derived mechanically from risk class and readiness states.
7. Ready, conditional, and held partitions are exact, sorted, and complete.
8. All admission, activation, network, scheduling, mutation, promotion, release, publication, and public-use permissions are fixed false.
9. No result authenticates a reference, reviewer, source, endpoint, terms record, or policy decision.
10. Correction creates a new assessment; this fixture performs no write or external effect.

## Deterministic identity

The validator computes RFC 8785 JCS plus SHA-256 over the complete candidate after removing only `portfolio_id` and `spec_hash`.

```text
spec_hash    = SHA-256(JCS(identity subject))
portfolio_id = kfm:source-portfolio:<first 24 digest hex>
```

## Existing-family boundary

- `SourceActivationDecision` remains the per-source, operation-specific pre-RAW decision family.
- `SourceRightsCurrentnessAssessment` remains the dated rights and currentness assessment family.
- `VerificationConvergencePlan` remains the bounded general verification-task selection family.
- SourceDescriptor, source role, policy, review, registry, receipts, evidence, release, correction, and rollback retain their own authority.

This candidate only composes declared review-readiness posture. It resolves none of those references and creates no new authority.

## Directory Rules basis

The primary authority owner is source-review planning, so semantic meaning belongs under `contracts/source/`; machine shape under `schemas/contracts/v1/source/`; synthetic cases under `fixtures/contracts/v1/source/`; reusable validation under `tools/validators/source/`; enforceability under `tests/validators/`; source adaptation under `docs/intake/exploratory/`; orchestration under `.github/workflows/`; and authoring accountability under `data/receipts/generated/`. No new root, domain lane, source registry, policy home, lifecycle state, or release family is created.

## Validation

```bash
python -m unittest -v tests.validators.test_validate_source_activation_portfolio_assessment
python tools/validators/source/validate_source_activation_portfolio_assessment.py --fixtures
```

## Rollback

Before merge, close the draft pull request and abandon its branch. After an authorized merge, revert this additive packet. No source, registry, connector, data, review assignment, schedule, release, deployment, or public artifact requires operational cleanup.
