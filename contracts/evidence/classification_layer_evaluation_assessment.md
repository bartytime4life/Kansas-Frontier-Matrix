<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/evidence/classification-layer-evaluation-assessment
title: ClassificationLayerEvaluationAssessmentCandidate Contract
type: semantic-contract
version: v1.0.0
status: proposed-inactive; fixture-only; no-network; non-authoritative
owners: OWNER_TBD — Evidence steward · Model-governance steward · Validation steward · Map-review steward
created: 2026-08-10
updated: 2026-08-10
owning_root: contracts/
policy_label: internal; evidence; classification-evaluation; model-assisted-layer
responsibility: Define a fixture-only assessment that verifies declared confusion-matrix arithmetic or comparable evaluation references without evaluating a live model, selecting a scientific threshold, approving public interpretation, or authorizing release or publication.
truth_posture: "CONFIRMED source-card traceability and repository gap; PROPOSED inactive contract; UNKNOWN scientific fitness and consumer adoption; NEEDS VERIFICATION human review and hosted CI"
related:
  - ./predictive_layer_generalization_assessment.md
  - ./analytic_output_disclosure_assessment.md
  - ./evidence_bundle.md
  - ../governance/model_card_envelope.md
  - ../../schemas/contracts/v1/evidence/classification_layer_evaluation_assessment.schema.json
  - ../../fixtures/contracts/v1/evidence/classification_layer_evaluation_assessment/cases.json
  - ../../tools/validators/evidence/validate_classification_layer_evaluation_assessment.py
  - ../../tests/validators/evidence/test_validate_classification_layer_evaluation_assessment.py
  - ../../docs/intake/exploratory/pass-18-classification-layer-evaluation-source-map.md
[/KFM_META_BLOCK_V2] -->

# ClassificationLayerEvaluationAssessmentCandidate

`ClassificationLayerEvaluationAssessmentCandidate` is an inactive declaration
profile for keeping class-level evaluation evidence attached to one classified
or model-assisted layer. It implements the smallest dependency-closed portion
of Pass 18 card `KFM-P18-INV-432`.

## Boundary

A validator `PASS` proves only that declared references, class labels,
confusion-matrix counts, derived metric arithmetic, disclosure fields,
limitations, deterministic identity, and fixed-false authority claims are
internally coherent under this synthetic profile.

It does not execute or evaluate a model, authenticate ground truth, resolve an
EvidenceBundle, prove dataset independence, select a scientific threshold,
establish fitness for use, decide policy or review, release, deploy, publish, or
authorize consequential public interpretation.

## Evaluation modes

| Mode | Local profile posture |
|---|---|
| `SUPERVISED_CONFUSION_MATRIX` | Requires a labeled evaluation reference, verified-reference declaration, complete square matrix, and recomputable class metrics. |
| `COMPARABLE_EVALUATION` | Requires one or more opaque comparable-evaluation references and explicit limitations; the validator does not authenticate or compare them. |
| `WEAKLY_SUPERVISED` | May describe internal or exploratory review, but public or policy-context use abstains. |
| `UNSUPERVISED` | May describe exploratory cluster review without pretending that cluster labels are ground truth; public or policy-context use abstains. |
| `UNKNOWN` | Abstains. |

The profile defines no universal accuracy, precision, recall, F1, class-support,
or abstention threshold. For a supplied confusion matrix it recomputes arithmetic
only: sample count, diagonal count, overall accuracy, per-class precision,
recall and F1, and their unweighted macro means.

## Finite outcomes

| Outcome | Meaning |
|---|---|
| `PASS` | The declared evaluation and disclosure packet is locally coherent for its stated use. |
| `ABSTAIN` | Evaluation state, references, method, or public-use support remains incomplete, unresolved, or insufficient. |
| `DENY` | Matrix closure, arithmetic, ground-truth posture, comparable-evidence declarations, disclosure, or deterministic identity is incoherent. |
| `ERROR` | Shape or input handling prevents safe evaluation, or the declaration records an evaluation error. |

These are validator outcomes, not scientific conclusions, policy decisions,
review approvals, release states, or runtime answers.

## Directory Rules basis

Accepted ADR-0029 places semantic evidence meaning under `contracts/evidence/`,
machine shape under `schemas/contracts/v1/evidence/`, synthetic replay under
`fixtures/contracts/v1/evidence/`, reusable validation under
`tools/validators/evidence/`, conformance proof under
`tests/validators/evidence/`, read-only orchestration under
`.github/workflows/`, source reconciliation under `docs/intake/exploratory/`,
and authoring accountability under `data/receipts/generated/`.

The profile composes existing EvidenceBundle, model-card, model-run, predictive
generalization, validation-report, review, and Evidence Drawer surfaces by opaque
reference. It creates no model registry, metric registry, ground-truth store,
layer authority, policy rule, release record, or publication path.

## Validation and rollback

```bash
python -m unittest tests.validators.evidence.test_validate_classification_layer_evaluation_assessment -v
python tools/validators/evidence/validate_classification_layer_evaluation_assessment.py --fixtures
```

Rollback is one additive commit revert. No model, dataset, evidence, layer,
policy, lifecycle, review, release, deployment, or public artifact requires
operational restoration.
