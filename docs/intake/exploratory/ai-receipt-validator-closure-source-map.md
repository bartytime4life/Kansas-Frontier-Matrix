<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/intake/exploratory/ai-receipt-validator-closure-source-map
title: AIReceipt Validator Closure Source Map
type: source-map; exploratory-intake; implementation-lineage
version: v1.0.0
status: proposed; repository-grounded; fixture-only; no-network
owners: OWNER_TBD — Governed AI steward · Runtime steward · Validator steward · Evidence steward · Policy steward · Citation steward
created: 2026-08-10
updated: 2026-08-10
policy_label: public; exploratory; governed-ai; validator; no-public-authority
owning_root: docs/
responsibility: Record the source-to-repository basis, bounded implementation decision, exclusions, validation, and rollback for the AIReceipt validator closure slice.
truth_posture: CONFIRMED source and repository evidence / PROPOSED implementation pending review / NEEDS VERIFICATION hosted checks and runtime adoption
related:
  - ../../../contracts/runtime/ai_receipt.md
  - ../../../schemas/contracts/v1/runtime/ai_receipt.schema.json
  - ../../../fixtures/contracts/v1/runtime/ai_receipt/
  - ../../../tools/validators/validate_ai_receipt.py
  - ../../../tools/validators/validator_registry.json
  - ../../../tests/validators/test_validate_ai_receipt.py
  - ../../../.github/workflows/ai-receipt.yml
notes:
  - "This source map is lineage and review context, not AI truth, policy, citation validation, review approval, release authority, or publication authority."
  - "The slice replaces one executable stub and reuses the existing strict runtime schema and existing synthetic fixtures; it does not resolve the separate permissive AI-family schema conflict."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# AIReceipt Validator Closure Source Map

## Goal

Replace the current `NotImplementedError` AIReceipt validator stub with a deterministic, no-network checker that validates the already-present strict runtime schema and synthetic fixture polarity, then wire that checker into the existing validator registry and a read-only workflow.

## Source basis

| Source | Status | Contribution | Limit |
|---|---|---|---|
| Google Drive `New Ideas 5-19-26` | `CONFIRMED` discovery source | Repeated pressure for governed-AI accountability receipts, citation validation, finite outcomes, and fail-closed public behavior. | Proposal pressure; not repository implementation evidence. |
| KFM AI Build Operating Contract v3.0 | `CONFIRMED` doctrine | AI remains interpretive; receipts are accountability objects; generated language cannot replace evidence, policy, review, release, correction, or rollback. | Does not prove validator implementation. |
| KFM Pipeline Living Implementation Manual v0.3 | `CONFIRMED` doctrine / `PROPOSED` realization | Receipts are process memory and finite outcomes remain explicit. | Proposed paths and runtime depth require repo evidence. |
| KFM MapLibre Operating Architecture | `CONFIRMED` doctrine / `PROPOSED` realization | Focus Mode and map-facing AI must remain downstream of EvidenceBundle, policy, citation validation, release state, and governed APIs. | Does not authorize a model or public answer. |
| `contracts/runtime/ai_receipt.md` | `CONFIRMED` repository evidence | Defines AIReceipt as an accountability trace, not truth, EvidenceBundle, PolicyDecision, RuntimeResponseEnvelope, chain-of-thought storage, or publication authority. | Contract remains draft/PROPOSED. |
| `schemas/contracts/v1/runtime/ai_receipt.schema.json` | `CONFIRMED` repository evidence | Strict Draft 2020-12 field shape with finite `ANSWER`, `ABSTAIN`, `DENY`, and `ERROR` outcomes. | Shape alone does not resolve referenced policy or citation objects. |
| `fixtures/contracts/v1/runtime/ai_receipt/` | `CONFIRMED` repository evidence | Two positive and three negative synthetic fixtures already exist. | Existing fixtures prove only declared shape polarity. |
| `tools/validators/validate_ai_receipt.py@main` | `CONFIRMED` repository evidence | Current file is a greenfield stub that raises `NotImplementedError`. | No validation behavior exists at the pinned baseline. |

## Pinned repository finding

Baseline: `main@ef1ba46a19e4de7c176e9d093c1285e73a0af75a`.

| Surface | Blob / state | Finding |
|---|---|---|
| Dedicated validator | `76a03f2c81e7e86057e342447f29efdf0f824468` | Stub; cannot validate any candidate. |
| Strict runtime schema | `2e0bebdb3a38acbc3c58a919db46970c6e829b4a` | Existing paired candidate shape. |
| Semantic contract | `f4d8183dbed38f83144f6d9dbde30ae02a01edb8` | Existing boundary and field semantics. |
| Validator registry | `12517f368cb1c8b850d3a7138a968cee889875ba` | AIReceipt is not registered in `focused` or `full`. |
| Open overlap | none found | No open pull request matched the exact validator or object family at preflight. |

## Bounded implementation decision

The slice will:

1. replace the dedicated stub in place;
2. use strict UTF-8 JSON loading with duplicate-key, non-finite-number, symlink, file-size, and root-object guards;
3. apply the existing Draft 2020-12 schema;
4. add only two local semantic checks not expressed by the current schema: no blank required references/adapter identifiers and no all-zero digest placeholders;
5. replay the existing valid/invalid fixtures;
6. add focused tests, registry wiring, and read-only CI; and
7. emit a generated authoring receipt.

The slice will not:

- resolve `policy_decision_ref` or `citation_validation_ref`;
- decide whether an AI answer is true, cited, reviewed, released, or public-safe;
- call a model, provider, network, evidence resolver, policy engine, or public API;
- store prompts, raw outputs, secrets, sensitive payloads, or private chain-of-thought;
- resolve the separate strict-runtime versus permissive-AI schema authority conflict;
- implement evidence-before-model orchestration or runtime policy;
- create lifecycle, release, deployment, or publication state.

## Directory Rules basis

| Path | Owning root | Outcome | Basis |
|---|---|---|---|
| `tools/validators/validate_ai_receipt.py` | `tools/` | `PLACE` | Existing same-path executable validator target; `tools/` owns reusable validation. |
| `tests/validators/test_validate_ai_receipt.py` | `tests/` | `PLACE` | Deterministic proof of changed validator behavior. |
| `.github/workflows/ai-receipt.yml` | `.github/` | `PLACE` | Read-only hosted orchestration for the bounded fixture profile. |
| `tools/validators/validator_registry.json` | `tools/` | `PLACE` | Existing machine registry for validator discovery and profiles. |
| this source map | `docs/` | `PLACE` | Human-readable source reconciliation and non-effects. |
| generated receipt | `data/receipts/generated/` | `PLACE` | Existing immutable generated-work provenance lane. |

No root, contract home, schema home, policy home, receipt home, or public path is created or moved.

## Acceptance and validation

- existing valid fixtures pass;
- existing invalid fixtures fail;
- hostile duplicate-key, non-finite, symlink, blank-reference, and placeholder-digest cases fail safely;
- serialized findings expose codes and field paths, not receipt payload values;
- the validator is registered in `focused` and `full`, but not `release-dry-run`;
- workflow permissions remain read-only and no-network;
- generated receipt hashes bind every AI-authored artifact except the receipt itself;
- hosted exact-head checks and independent human review remain separate `NEEDS VERIFICATION` states.

## Rollback

Before merge, close the draft pull request and abandon the branch. After an authorized merge, revert the bounded files, restore validator blob `76a03f2c81e7e86057e342447f29efdf0f824468`, restore the prior registry blob, and remove the additive test, workflow, source map, and generated receipt. No model, source, evidence, lifecycle, release, deployment, or public state requires restoration.

[Back to top](#top)
