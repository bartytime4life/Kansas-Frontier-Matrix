<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/release/promotion-receipt/v1
title: PromotionReceipt Contract
type: semantic-contract
version: v1
status: PROPOSED; release-governance-record-shape; fixture-first; no-network; non-publisher
owners: OWNER_TBD — Release steward · Evidence steward · Policy steward · Review steward · Schema steward · Validation steward
created: 2026-08-05
updated: 2026-08-05
policy_label: internal; release; promotion; receipt; evidence-bound; rollback-aware
related:
  - ./README.md
  - ./promotion_decision.md
  - ./release_manifest.md
  - ./rollback_card.md
  - ../../schemas/contracts/v1/release/promotion_receipt.schema.json
  - ../../fixtures/release/promotion_receipt/README.md
  - ../../tools/validators/release/validate_promotion_receipt.py
  - ../../tests/release/test_promotion_receipt.py
  - ../../docs/architecture/publication/release-objects.md
[/KFM_META_BLOCK_V2] -->

# PromotionReceipt contract

> **One-line purpose.** Record the declared inputs, A–G readiness outcomes, integrity binding, decision reference, and lifecycle effect of one promotion attempt without collapsing the receipt into a `PromotionDecision`, `ReleaseManifest`, policy evaluation, review authority, proof pack, or publication event.

## Status and placement

This contract and its paired schema are **PROPOSED**. They add a release-scoped receipt profile under the existing release object family because the record describes a governed lifecycle transition attempt. Emitted instances remain release/data records; this contract stores no operational receipt and performs no transition.

The object is intentionally separate from:

- `PromotionDecision` — the accountable approve/deny/abstain decision;
- the promotion-gate readiness result — bounded validation output;
- `ReleaseManifest` — the authoritative inventory of a released state;
- `RunReceipt` — process memory for a tool or pipeline run;
- `ProofPack` — the assembled support for release;
- `RollbackCard` and `CorrectionNotice` — reversal and correction controls.

## Required content

| Field | Meaning |
|---|---|
| `promotion_id` | Stable identity for one promotion attempt. |
| `receipt_profile` | Exact contract profile: `kfm/promotion-receipt/v1`. |
| `candidate` | Candidate identity, `spec_hash`, and declared artifact digests. |
| `evaluation` | Bounded A–G profile, evaluation instant, finite overall status, and readiness state. |
| `gates` | Exactly seven ordered gate records, A through G, using the current repository gate names. |
| `transition` | Declared `CATALOG`/`TRIPLET` → `PUBLISHED` target and whether the transition was actually applied. |
| `decision_ref` | Optional reference to the separately governed `PromotionDecision`. |
| support refs | Evidence, policy, review, and attestation references used by the attempt. |
| `integrity.receipt_digest` | SHA-256 of canonical JSON after removing the top-level `integrity` member. |
| actor/time | `created_by` and `created_at` for audit lineage. |

## Gate vocabulary

| Gate | Name | Current bounded responsibility |
|:---:|---|---|
| A | `identity_and_closure` | Candidate identity, lifecycle boundary, and manifest closure declarations. |
| B | `asset_integrity` | Candidate, manifest, receipt, and digest-set agreement. |
| C | `geometry_and_crs` | Declared geometry validity, deterministic processing, CRS, and bounds. |
| D | `temporal_semantics` | Valid UTC instants and temporal ordering. |
| E | `rights_and_sensitivity` | Declared rights, sensitivity, policy profile, and finite policy outcome. |
| F | `proof_and_catalog_support` | Evidence, attestation, receipt, and STAC/DCAT/PROV support. |
| G | `review_and_rollback` | Review separation, subject/hash binding, correction lineage, and rollback support. |

Gate status vocabulary is `PASS`, `ABSTAIN`, `DENY`, and `ERROR`. Overall status is derived with the fail-closed precedence:

```text
ERROR > DENY > ABSTAIN > PASS
```

`PASS` maps to `APPROVE_READY`; every other overall status maps to `BLOCKED`.

## Transition rules

A receipt may describe a readiness evaluation without applying a lifecycle transition. `transition.applied: false` is therefore valid even when the result is `PASS` / `APPROVE_READY`.

When `transition.applied: true`, the validator requires all of the following declarations:

1. every gate is `PASS`;
2. overall status is `PASS` and readiness is `APPROVE_READY`;
3. `decision_ref` is present;
4. evidence, policy, review, and attestation reference arrays are non-empty;
5. the receipt digest matches the canonical payload.

These checks validate internal consistency only. They do not dereference or authenticate the referenced objects and do not prove that a transition occurred.

## Digest rule

To calculate `integrity.receipt_digest`:

1. copy the JSON object;
2. remove the top-level `integrity` member;
3. serialize as UTF-8 JSON with keys sorted, no insignificant whitespace, and ASCII escaping enabled;
4. compute SHA-256;
5. prefix the lowercase hexadecimal digest with `sha256:`.

## Validation

```bash
python tools/validators/release/validate_promotion_receipt.py --fixtures
python -m unittest -q tests.release.test_promotion_receipt
```

The validator is deterministic, no-network, read-only, and non-publishing. A passing result proves only schema shape, finite-outcome consistency, declared transition prerequisites, and receipt-digest integrity.

## Non-effects

Neither this contract nor a schema-valid fixture:

- creates evidence or verifies evidence truth;
- evaluates policy or proves rights/sensitivity clearance;
- authenticates actors, reviewers, or authority assignments;
- emits a `PromotionDecision`, `ReleaseManifest`, proof, or operational receipt;
- promotes, releases, deploys, publishes, or changes public state.

## Rollback

Revert the contract, schema, fixtures, validator, tests, workflow, and generated receipt together. No lifecycle data or public surface is mutated by this fixture-first slice.
