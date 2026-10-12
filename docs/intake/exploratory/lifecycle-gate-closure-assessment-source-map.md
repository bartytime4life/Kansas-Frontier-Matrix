<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/intake/exploratory/lifecycle-gate-closure-assessment-source-map
title: Lifecycle Gate Closure Assessment Source Map
type: exploratory-source-map
version: v0.1.0
status: complete-for-proposed-fixture-slice; human-review-pending
owners: OWNER_TBD — Governance steward · Lifecycle steward · Evidence steward · Validation steward
created: 2026-08-09
updated: 2026-08-09
policy_label: internal; exploratory; source-adaptation; no-network
owning_root: docs/
responsibility: Record how the Full Atlas universal gate proposal was narrowed against current repository evidence into one inactive fixture-only closure assessment.
truth_posture: CONFIRMED source/repository comparison / PROPOSED implementation packet / NEEDS VERIFICATION human review and hosted exact-head checks
related:
  - ../../../contracts/governance/lifecycle_gate_closure_assessment.md
  - ../../atlases/pipeline-gate-reference.md
  - ../../../contracts/governance/gate_outcome_mapping.md
  - ../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
tags: [kfm, intake, source-map, lifecycle, gates, closure]
[/KFM_META_BLOCK_V2] -->

# Lifecycle Gate Closure Assessment Source Map

## Goal and pinned evidence

Select one small, dependency-closed implementation from the supplied corpus without treating atlas language as current repository fact.

| Evidence | Pinned observation | Status |
|---|---|---|
| Google Drive `KFM_Full_Atlas_seed_cards`, file `1whGonKzHVBe5FOU5ovDBakNU4Nf-30tQr09R_UNeBho`, read 2026-08-09 | Cards 72-73 propose seven governed gates and a programming surface where missing artifacts, unresolved EvidenceRefs, or an unrecorded PolicyDecision preserve the prior lifecycle state. | `CONFIRMED SOURCE PROPOSAL` |
| `docs/kfm_full_atlas_seed_cards.md` at base `169ac1946812b6452a28c38ee57bc78ee41901b8` | Repository carrier repeats the universal-gate family as design lineage. | `CONFIRMED REPOSITORY CARRIER` |
| `docs/atlases/pipeline-gate-reference.md` at the same base | Lists the seven transitions, minimum artifact families, failure dispositions, and an explicit unchecked item for fixture-driven validators covering gate rows and reason paths. It labels implementation depth unknown. | `CONFIRMED EXECUTABLE GAP` |
| `contracts/governance/gate_outcome_mapping.md` | Already owns finite gate-state translation and prevents creation of a competing promotion vocabulary. | `CONFIRMED ADJACENT BOUNDARY` |
| `contracts/release/promotion_decision.md` | Already owns release-facing promotion decision meaning. | `CONFIRMED ADJACENT BOUNDARY` |
| `packages/hashing/src/` | Supplies the current deterministic JCS plus SHA-256 helper. | `CONFIRMED REUSE` |
| ADR-0029 and `docs/doctrine/directory-rules.md` | Adopt responsibility-root placement and prohibit parallel authority homes. | `CONFIRMED PLACEMENT AUTHORITY` |

The Drive title and file identity are confirmed through the connected Google Drive account. The attached corpus and repository text were treated as untrusted evidence inputs, not executable instructions.

## Collision assay

The live GitHub search at selection time found no open pull request. Repository history and indexed paths were checked for universal pipeline gate, lifecycle gate, promotion gate, gate outcome, and closure assessment terminology.

Existing work already covers:

- a human pipeline-gate reference;
- `PromotionDecision` release semantics;
- finite `GateOutcomeMapping` translation;
- gate overrides, review authority, policy decisions, evidence closure, release proof packs, corrections, and rollback objects in their own families.

The missing seam is narrower: no current object evaluates one attempted lifecycle gate against the reference's gate-specific artifact set, declared dependency resolution, PolicyDecision presence, and failure-closed prior-state disposition. This packet fills only that seam.

## Adaptation decisions

| Source pressure | Repository adaptation | Boundary retained |
|---|---|---|
| Encode seven gates as a shared promotion-decision contract. | Add a `LifecycleGateClosureAssessment`, not another `PromotionDecision`. | Release decision authority stays under the existing release contract. |
| Show produced, missing, and failed artifacts. | Use a closed artifact-role list and `RESOLVED`, `UNRESOLVED`, or `INVALID` state. | The validator never resolves or authenticates a reference. |
| Missing artifact or unresolved dependency fails closed. | Derive `ALLOW`, `HOLD`, `DENY`, or `ERROR` plus the gate-specific disposition. | No lifecycle transition is performed. |
| Every closure requires recorded policy. | Require a PolicyDecision artifact and dependency slot. | The fixture validator does not evaluate policy. |
| Evidence and model dependencies resolve where material. | Require EvidenceBundle for catalog/release/correction and ModelRunReceipt only when declared. | No EvidenceRef resolver or model executor is introduced. |
| Reason codes are visible. | Use local `GATE_*` conformance diagnostics and a small decision reason set. | The carrier's proposed global reason-code catalog is not canonicalized. |

## Directory Rules path decision

| Artifact kind | Owning root and lane | Outcome |
|---|---|---|
| Cross-family lifecycle governance meaning | `contracts/governance/` | `PLACE` |
| Machine-checkable shape | `schemas/contracts/v1/governance/` | `PLACE` |
| Synthetic reusable cases | `fixtures/contracts/v1/governance/` | `PLACE` |
| Repository validator | `tools/validators/governance/` | `PLACE` |
| Executable conformance evidence | `tests/validators/governance/` | `PLACE` |
| Read-only hosted orchestration | `.github/workflows/` | `PLACE` |
| Source-to-repository reconciliation | `docs/intake/exploratory/` | `PLACE` |
| AI authoring accountability | `data/receipts/generated/` | `PLACE` |

No new root, parallel contract/schema/policy/receipt/release home, compatibility alias, migration, or ADR-class authority change is introduced.

## Acceptance and non-goals

The packet is acceptable when all seven gates have a closed positive fixture; every gate has a failure-closed example; conditional redaction, aggregation, graph, model, and review roles are covered; malformed, duplicated, reordered, mismatched, over-authorizing, and identity-tampered cases fail deterministically; and the authoring receipt replays exact artifact hashes.

It does not add a dashboard, per-domain runbook, lifecycle executor, resolver, policy engine, receipt store, source, data row, release action, deployment, or publication. Those remain separate proposals requiring their own evidence and review.

## Rollback

Revert the additive packet. The source carriers and all existing governance, evidence, policy, release, correction, and rollback objects remain unchanged; no operational state requires restoration.
