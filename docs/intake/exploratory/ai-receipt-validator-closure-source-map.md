<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/intake/exploratory/ai-receipt-validator-closure-source-map
title: AIReceipt Validator Closure Source Map
type: source-map; exploratory-intake; implementation-lineage
version: v1.0.0
status: proposed; repository-grounded; fixture-only; no-network
owners: OWNER_TBD — Governed AI steward · Runtime steward · Validator steward
created: 2026-08-10
updated: 2026-08-10
policy_label: public; exploratory; governed-ai; validator; no-public-authority
owning_root: docs/
responsibility: Record the evidence, boundary, validation, and rollback for the AIReceipt validator closure slice.
truth_posture: CONFIRMED evidence / PROPOSED implementation / NEEDS VERIFICATION hosted checks and runtime adoption
[/KFM_META_BLOCK_V2] -->

# AIReceipt Validator Closure Source Map

## Goal

Replace the existing `NotImplementedError` AIReceipt validator stub with a deterministic, no-network checker for the repository's strict runtime schema and synthetic fixtures.

## Evidence basis

- Google Drive `New Ideas 5-19-26` supplies proposal pressure for governed-AI accountability, citation validation, finite outcomes, and fail-closed behavior.
- KFM AI doctrine says receipts are accountability objects; they do not replace evidence, policy, review, release, correction, or rollback.
- At `main@ef1ba46a19e4de7c176e9d093c1285e73a0af75a`, the contract, strict Draft 2020-12 schema, two valid fixtures, and three invalid fixtures existed, while `tools/validators/validate_ai_receipt.py` was an executable stub.

## Bounded implementation

The validator performs strict UTF-8 JSON loading, rejects duplicate keys, non-finite numbers, symlinks, oversized inputs, malformed JSON, and non-object roots, applies the existing schema, and rejects blank required references or all-zero digest placeholders. Findings expose codes and JSON-pointer paths rather than receipt payload values.

It does **not** resolve `policy_decision_ref` or `citation_validation_ref`, call a model or network, authorize an answer, settle the separate permissive AI schema, promote lifecycle state, release, deploy, or publish.

## Exact-head repair

The first exact-head run showed that adding AIReceipt to `tools/validators/validator_registry.json` invalidated earlier immutable receipts that bind the registry bytes. This branch therefore restores that registry byte-for-byte and keeps coverage in the dedicated path-scoped workflow. Historical receipts are not rewritten.

## Directory Rules basis

- `tools/validators/validate_ai_receipt.py`: existing same-path validator under `tools/`.
- `tests/validators/test_validate_ai_receipt.py`: focused behavioral proof under `tests/`.
- `.github/workflows/ai-receipt.yml`: read-only hosted orchestration under `.github/`.
- this source map: lineage under `docs/`.
- generated receipt: AI-authoring process memory under `data/receipts/generated/`.

No contract, schema, policy, source, registry, release, proof, or public authority home changes.

## Acceptance and rollback

Existing valid fixtures must pass; existing invalid fixtures and hostile parser cases must fail safely; the shared registry must remain byte-identical to the pinned base. Before merge, close the draft PR and abandon the branch. After an authorized merge, revert the bounded commit, restoring validator blob `76a03f2c81e7e86057e342447f29efdf0f824468` and removing the additive workflow, test, source map, and receipt. No runtime, source, lifecycle, release, deployment, or public state requires restoration.
