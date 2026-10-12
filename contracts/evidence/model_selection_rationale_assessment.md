<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/evidence/model-selection-rationale-assessment
title: ModelSelectionRationaleAssessment Candidate Contract
type: semantic-contract
version: v1.0.0
status: proposed-inactive; fixture-only; no-network; non-authoritative
owners: OWNER_TBD — Evidence steward · Model-governance steward · Policy steward · Validation steward
created: 2026-08-11
updated: 2026-08-11
owning_root: contracts/
policy_label: internal; evidence; model-selection; interpretability; consequence; review-required
responsibility: Define a fixture-only assessment that links a model-assisted layer's problem, data characteristics, interpretability requirement, policy consequence, compared candidates, evaluation references, and selection rationale without executing or approving a model or granting evidence, policy, review, release, or publication authority.
truth_posture: "CONFIRMED supplied Pass 18 card, companion supplied AI reference, connected interpretive-analytics doctrine, accepted Directory Rules, adjacent repository contracts, and bounded gap; PROPOSED inactive assessment; UNKNOWN domain thresholds and consumer adoption; NEEDS VERIFICATION steward review and hosted exact-head CI"
related:
  - ./analytic_output_disclosure_assessment.md
  - ./model_evaluation_split_receipt.md
  - ./predictive_layer_generalization_assessment.md
  - ../governance/model_card_envelope.md
  - ../../schemas/contracts/v1/evidence/model_selection_rationale_assessment.schema.json
  - ../../fixtures/contracts/v1/evidence/model_selection_rationale_assessment/cases.json
  - ../../tools/validators/evidence/validate_model_selection_rationale_assessment.py
  - ../../tests/validators/evidence/test_validate_model_selection_rationale_assessment.py
  - ../../docs/intake/exploratory/pass-18-model-selection-rationale-assessment-source-map.md
[/KFM_META_BLOCK_V2] -->

# ModelSelectionRationaleAssessment Candidate

`ModelSelectionRationaleAssessmentCandidate` makes one model choice inspectable.
It implements the smallest reviewable portion of supplied Pass 18 card
`KFM-P18-INV-159`, corroborated by the companion supplied AI reference's model
selection section and the connected Full Atlas interpretive-analytics pattern.

## Required comparison

The candidate binds:

- one bounded problem type and claim role;
- declared data-characteristic references;
- interpretability and consequence levels;
- at least two candidate models, including a distinct selected candidate and
  baseline, with evaluation-receipt references for every eligible candidate;
- problem-fit, data-fit, decision-reason, policy-consequence, model-card,
  training-receipt, evaluation-split, evidence, and review references; and
- a declaration that performance was not the sole selection basis.

No universal accuracy, loss, calibration, interpretability, or eligibility
threshold is introduced. Candidate evaluation values remain in their referenced
records; this profile checks linkage and coherence only.

## Finite outcomes

| Outcome | Meaning |
|---|---|
| `PASS` | The declared comparison, selection, rationale, governance references, content identity, and non-authority boundary are locally coherent. |
| `ABSTAIN` | The problem, consequence, interpretability, sensitive-data posture, selection, or review remains unresolved. |
| `DENY` | The choice is uncomparative, unsupported, ineligible, task-incoherent, performance-only, insufficiently interpretable for its declared need, consequence-blind, trust-membrane-crossing, or identity-tampered. |
| `ERROR` | The candidate cannot be safely evaluated under the closed schema. |

`PASS` does not mean the selected model is accurate, fair, calibrated,
generalizable, scientifically valid, policy-suitable, approved, or deployable.

## Conservative rules

- The selected and baseline candidates must both exist, be eligible, differ,
  and carry evaluation-receipt references.
- A clustering family cannot stand in for a non-clustering task, or vice versa.
- High interpretability requires an interpretability-method reference for
  neural-network, ensemble, or kernel selections.
- High consequence requires a policy-consequence reference and completed
  review; sensitive-data presence also requires a policy-consequence reference.
- Causal and regulatory claims are outside this local assessment and deny.
- Reference arrays and candidates are sorted and duplicate-free.
- RAW, WORK, QUARANTINE, direct-store, and embedded-query references deny.
- Every authority claim remains fixed to `false`.

## Authority boundary

The validator does not train, execute, tune, compare, rank, evaluate, approve,
register, release, deploy, or publish a model. It does not authenticate a
dataset, metric, model card, training receipt, split receipt, evaluation
receipt, evidence bundle, policy consequence, or review record. It creates no
runtime selection mechanism, policy rule, model registry, layer authority, or
public interpretation permission.

## Directory Rules basis

Evidence-side selection meaning belongs under `contracts/evidence/`; machine
shape, fixtures, validation, tests, read-only orchestration, source
reconciliation, and generated provenance remain in their established
responsibility roots. Referenced model-governance objects are composed by
opaque reference rather than duplicated. No parallel authority is introduced.

## Validation and rollback

```bash
python -m unittest tests.validators.evidence.test_validate_model_selection_rationale_assessment -v
python tools/validators/evidence/validate_model_selection_rationale_assessment.py --fixtures
```

Rollback is one additive commit revert. The inactive packet has no runtime
consumer and creates no external state.
