<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/governance/responsibility-layer-impact-assessment
title: ResponsibilityLayerImpactAssessment Candidate Contract
type: semantic-contract
version: v1.0.0
status: proposed-inactive; fixture-only; no-network; non-authoritative
owners: OWNER_TBD — Architecture steward · Governance steward · Contract steward · Validation steward
created: 2026-08-11
updated: 2026-08-11
owning_root: contracts/
policy_label: internal; governance; responsibility-layer; change-impact; directory-rules
responsibility: Define a fixture-only assessment of responsibility-layer impacts and seams without placing artifacts, assigning owners, deciding policy or review, mutating data, executing runtime work, or granting lifecycle authority.
truth_posture: "CONFIRMED supplied Pass 18 card, existing responsibility-layer architecture, connected Drive corroboration, accepted Directory Rules, and bounded repository gap; PROPOSED inactive assessment; UNKNOWN layer-model adoption and steward ownership; NEEDS VERIFICATION architecture, governance, contract, release, and validation review plus hosted exact-head CI"
related:
  - ../../docs/architecture/cross-domain/responsibility-layers.md
  - ../../docs/doctrine/directory-rules.md
  - ../../schemas/contracts/v1/governance/responsibility_layer_impact_assessment.schema.json
  - ../../fixtures/contracts/v1/governance/responsibility_layer_impact_assessment/cases.json
  - ../../tools/validators/governance/validate_responsibility_layer_impact_assessment.py
  - ../../tests/validators/governance/test_validate_responsibility_layer_impact_assessment.py
  - ../../docs/intake/exploratory/pass-18-responsibility-layer-impact-assessment-source-map.md
[/KFM_META_BLOCK_V2] -->

# ResponsibilityLayerImpactAssessment Candidate

`ResponsibilityLayerImpactAssessmentCandidate` is an additive, fixture-only
declaration of which KFM responsibility layers a proposed change touches, which
repository roots own its artifacts, and which cross-layer seams require review.
It implements the smallest unfilled portion of supplied Pass 18 card
`KFM-P18-INV-396`: make responsibility layers explicit in change-impact work and
tie them to decisions, validation, and rollback.

The repository already has an eight-layer architecture document. This contract
does not repeat or canonize that model. It binds to the draft model by opaque ref
and assesses one synthetic change under the model's current vocabulary.

## Assessment declaration

| Concern | Required declaration | Local check |
|---|---|---|
| Artifact placement | Canonical relative paths, existing responsibility-root labels, one primary layer, and zero or more related layers. | The declared root must prefix the path; layers are analysis labels, never new folders. |
| Layer coverage | One canonical impact row for every primary or related layer. | Direct vs related impact must match the artifact declarations. |
| Public-surface closure | Any `API`, `UI`, or `AI` impact includes `EVIDENCE`, `POLICY`, and `RELEASE`. | Missing closure is denied; no policy or release decision is inferred. |
| Cross-layer seams | Canonical connected seam declarations across all impacted layers. | Unknown endpoints, self-edges, and disconnected graphs are denied; unresolved seams abstain. |
| Decisions, validation, rollback | Policy carries a decision ref; each layer carries validation refs; release carries a rollback ref. | Refs remain opaque and are never resolved or executed. |
| Review | Complete, pending, or unknown with canonical record refs. | Pending or unknown review abstains; complete review without a record is denied. |

## Finite outcomes

| Outcome | Meaning |
|---|---|
| `PASS` | The synthetic artifact, root, layer, seam, decision-ref, validation-ref, rollback-ref, review, timestamp, and content-identity declarations are locally coherent. |
| `ABSTAIN` | A seam or review state remains unresolved. |
| `DENY` | Placement, coverage, impact kind, public closure, seam graph, decision, validation, rollback, review, time, or content identity contradicts the profile. |
| `ERROR` | The candidate cannot be safely parsed or evaluated under the closed schema. |

`PASS` is fixture coherence only. It is not approval of the proposed change or
evidence that referenced decisions, validations, reviews, or rollbacks exist.

## Authority boundary

A validator result does not:

- create a new root or place, move, rename, or delete any artifact;
- assign a code owner, steward, bounded context, domain, or responsibility;
- adopt the eight-layer model or add, remove, merge, or split a layer;
- resolve a contract, decision, validation, review, rollback, or change ref;
- execute policy, mutate data, run an application, or change runtime state;
- approve review or authorize promotion, release, deployment, publication, or
  public use.

## Directory Rules basis

Cross-family change-impact meaning belongs under `contracts/governance/`.
Machine shape, synthetic replay, executable validation, conformance evidence,
read-only CI, source lineage, and authoring provenance remain in their existing
responsibility roots. The layer enum does not create eight new folders, and this
packet does not amend Directory Rules, CODEOWNERS, a register, or the draft
responsibility-layer architecture.

## Validation and rollback

```bash
python -m unittest tests.validators.governance.test_validate_responsibility_layer_impact_assessment -v
python tools/validators/governance/validate_responsibility_layer_impact_assessment.py --fixtures
```

Rollback is one additive commit revert. The inactive packet creates no placement,
ownership, policy, review, data, runtime, release, deployment, publication, or
public state that requires restoration.
