<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/evidence/temporal-coalescing-receipt
title: TemporalCoalescingReceiptCandidate Contract
type: semantic-contract; receipt-profile
version: v1.0.0
status: proposed-inactive; fixture-only; no-network; non-authoritative
created: 2026-08-10
updated: 2026-08-10
owning_root: contracts/
policy_label: internal; evidence; temporal; receipt; provenance
related:
  - ../../schemas/contracts/v1/evidence/temporal_coalescing_receipt.schema.json
  - ../../fixtures/contracts/v1/evidence/temporal_coalescing_receipt/cases.json
  - ../../tools/validators/evidence/validate_temporal_coalescing_receipt.py
  - ../common/temporal_window.md
  - ../data/temporal_slice.md
  - ./temporal_support_assessment.md
  - ./spatial_transform_receipt.md
  - ../runtime/run_receipt.md
  - ../../docs/intake/exploratory/pass-18-temporal-coalescing-receipt-source-map.md
[/KFM_META_BLOCK_V2] -->

# TemporalCoalescingReceiptCandidate

`TemporalCoalescingReceiptCandidate` is an additive, fixture-only receipt profile for one interval transformation. It records whether source temporal facts were coalesced, split, or preserved and binds every output interval back to its input interval identifiers and evidence references.

It implements the smallest reviewable portion of supplied Pass 18 card `KFM-P18-INV-414` and its connected-Drive carrier pressure: temporal simplification must remain visible because it can change event counts, duration summaries, and the apparent continuity of a public claim.

## Boundary

The profile is `PROPOSED_INACTIVE`, no-network, and non-authoritative. A validator `PASS` means only that:

- the candidate is closed under this schema;
- its declared input and output interval digests replay;
- half-open UTC coverage is preserved per exact `fact_key`;
- lineage names every input and output interval; and
- the declared operation is coherent with the interval transformation.

It does **not** resolve an EvidenceRef, authenticate a RunReceipt, decide whether facts are semantically continuous, choose a duration policy, execute a transform, approve review, promote lifecycle state, create a release manifest, release, deploy, publish, or authorize public use.

## Profile fields

| Field | Meaning |
|---|---|
| `profile_spec_hash` | RFC 8785-style canonical JSON plus SHA-256 binding of the complete candidate except this field. |
| `run_receipt_ref` / `run_receipt_digest` | Reference and digest for the separate execution receipt; this profile does not replace it. |
| `method_ref` / `method_digest` / `method_resolution` | Pinned transform-method identity and whether that reference resolved for this review. |
| `operation` | `COALESCE`, `SPLIT`, or `PRESERVE`; it records transformation meaning rather than release status. |
| `interval_policy` | Half-open UTC bounds, overlap handling, adjacency handling, and exact fact-key equivalence. |
| `input_set` / `output_set` | Digest-bound interval declarations. Intervals contain identifiers, exact fact keys, and UTC valid-time bounds only. |
| `lineage` | Output-to-input identifier mapping; split operations may repeat an input across multiple output rows. |
| `evidence_refs` | Sorted references retained for downstream evidence resolution. They are not resolved by this validator. |
| `authority_claims` | Fixed-false declaration preventing the receipt candidate from claiming evidence, policy, review, promotion, release, or publication authority. |

## Deterministic interval semantics

All intervals use `[valid_from, valid_to)` UTC semantics. Coverage comparison uses the mathematical union of spans, so adjacent split outputs cover the same time as their unsplit input; operation-specific checks separately enforce the declared representation. The validator rejects zero or negative duration, non-UTC timestamps, duplicate or non-canonical interval order, unknown lineage identifiers, fact-key collapse, coverage loss or addition, and digest drift.

- `COALESCE` must reduce interval count and emit the canonical union defined by the declared overlap and adjacency policy.
- `SPLIT` must increase interval count without overlapping outputs or changing covered time.
- `PRESERVE` must retain the exact interval values and one-to-one lineage, even if output identifiers differ.

The profile deliberately uses exact `fact_key` equality. Deciding that differently attributed facts are equivalent is a separate domain/evidence decision and cannot be inferred by this validator.

## Finite validation outcomes

| Outcome | Meaning |
|---|---|
| `PASS` | Schema, digests, lineage, coverage, and operation semantics are internally coherent. |
| `ABSTAIN` | The transform method reference remains unresolved. |
| `DENY` | A declared digest, interval, lineage, coverage, or operation invariant fails. |
| `ERROR` | The candidate does not satisfy the closed machine schema. |

These are validator outcomes only. They are not KFM runtime answers, policy decisions, review decisions, promotion states, or release states.

## Directory Rules basis

The accepted responsibility-root model places receipt meaning under `contracts/evidence/`, machine shape under `schemas/contracts/v1/evidence/`, wholly synthetic cases under `fixtures/contracts/v1/evidence/`, executable validation under `tools/validators/evidence/`, tests under `tests/validators/`, CI under `.github/workflows/`, and authoring accountability under `data/receipts/generated/`. Existing temporal-window, temporal-slice, temporal-support, RunReceipt, and release authorities remain separate.

## Validation

```bash
python -m unittest tests.validators.test_validate_temporal_coalescing_receipt -v
python tools/validators/evidence/validate_temporal_coalescing_receipt.py --fixtures
```

## Rollback

Revert the additive profile packet. It executes no transform and mutates no source, interval store, evidence, policy, review, lifecycle, catalog, release, cache, route, deployment, or public artifact.
