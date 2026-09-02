<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/runtime/runtime-verification/v1
title: Runtime Verification Receipt and Proof Contract
type: semantic-contract
version: 1.0.0
status: PROPOSED
owners:
  - OWNER_TBD — Runtime steward
  - OWNER_TBD — Evidence steward
  - OWNER_TBD — Validation steward
created: 2026-08-06
updated: 2026-08-06
policy_label: repository-facing; runtime; verification; fail-closed; no-publication-effect
related:
  - ../../docs/doctrine/directory-rules.md
  - ../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../schemas/contracts/v1/runtime/runtime_verification/README.md
  - ../../tools/validators/runtime_verification/README.md
  - ../../data/receipts/README.md
  - ../../data/proofs/README.md
notes:
  - "Derived from New Ideas 4-12-26.pdf and reconciled to current repository placement."
  - "This contract creates no evidence closure, policy decision, release state, deployment, or publication authority."
[/KFM_META_BLOCK_V2] -->

# Runtime Verification Receipt and Proof Contract

> **One-line rule.** Runtime verification records progress as receipts and final digest evaluation as proof-ready output; the two objects remain separate, finite, deterministic, and fail closed.

## Goal

Define a narrow contract family for checking a declared digest while bytes are streamed outside the map-rendering path. The family supports large released-artifact carriers such as PMTiles, COG, GeoParquet, and other immutable bundles without turning the browser UI, worker, receipt, or validator into release authority.

This first slice is fixture-first and no-network. It defines object meaning, machine shape, deterministic validation, and negative cases. It does **not** implement a browser worker, fetch live bytes, persist operational records, evaluate policy, or authorize promotion.

## Directory Rules basis

The accepted Directory Governance Standard v2 and ADR-0029 route each responsibility independently:

| Responsibility | Home used by this slice |
|---|---|
| Semantic meaning | `contracts/runtime/runtime_verification.md` |
| Machine shape | `schemas/contracts/v1/runtime/runtime_verification/` |
| Static examples | `fixtures/contracts/v1/runtime/runtime_verification/` |
| Deterministic validator | `tools/validators/runtime_verification/` |
| Tests | `tests/validators/` |
| CI orchestration | `.github/workflows/` |
| Emitted progress records | `data/receipts/` — not created by this slice |
| Release-grade proof records | `data/proofs/` — not created by this slice |

No new repository root or parallel schema, receipt, proof, policy, or release authority is introduced.

## Object roles

### `RuntimeVerificationReceipt`

A receipt is process memory for an in-progress or resumable verification run.

It may record:

- stable receipt and job identities;
- artifact and optional manifest references;
- byte count and checkpoint index;
- an optional partial digest;
- current progress state;
- prior receipt linkage for a resumed run;
- verifier surface and version;
- recording time.

It must not contain a final verification outcome, proof identity, expected-versus-observed conclusion, policy decision, or release decision.

### `RuntimeVerificationProof`

A proof is the final finite result of one verification attempt.

It may record:

- stable proof and job identities;
- artifact and manifest references;
- the declared and observed digests where applicable;
- one finite outcome;
- a bounded reason;
- verifier identity and verification time;
- a reference to the progress receipt.

A schema-valid proof is **proof-ready output**, not automatically an admitted `EvidenceBundle`, release proof, policy approval, promotion decision, or published fact.

### `RuntimeVerificationDigest`

A digest is an explicit SHA-256 value with an encoding declaration. This slice admits hexadecimal and RFC 4648 padded Base64 representations. Validators compare decoded bytes, not presentation strings.

### `RuntimeVerificationOutcome`

The finite outcome vocabulary is:

| Outcome | Meaning | Minimum requirement |
|---|---|---|
| `VERIFIED` | Observed SHA-256 equals the declared SHA-256. | Manifest declaration, expected digest, observed digest, and receipt reference. |
| `MISMATCH` | Observed SHA-256 differs from the declaration. | Manifest declaration, both digests, bounded reason, and receipt reference. |
| `MISSING_DECLARATION` | No declared digest or manifest was available. | Expected digest and manifest reference are absent; bounded reason is present. |
| `INTERRUPTED` | Processing stopped before a final observed digest existed. | Observed digest is absent; bounded reason is present. |
| `ERROR` | A bounded transport, runtime, parser, or verifier failure prevented completion. | Bounded reason is present. |

## Cross-object invariants

1. Receipts and proofs use the same `job_id` when they describe one attempt.
2. Receipts never carry `outcome` or `proof_id`.
3. Proofs never carry receipt progress fields or `receipt_id`.
4. A declared expected digest requires a non-null `manifest_ref`.
5. `VERIFIED` requires both digests and byte equality.
6. `MISMATCH` requires both digests and byte inequality.
7. `MISSING_DECLARATION` requires `manifest_ref = null` and `expected_digest = null`.
8. `INTERRUPTED` must not claim an observed final digest.
9. Unknown object kinds, outcomes, digest formats, or contradictory outcome/digest combinations fail closed.
10. Diagnostics expose stable codes and JSON Pointer fields; they do not echo untrusted payload values.

## Canonical validator codes

```text
SCHEMA_INVALID
INVALID_OUTCOME
RECEIPT_HAS_OUTCOME
RECEIPT_HAS_PROOF_ID
RECEIPT_MISSING_BYTES
PROOF_HAS_RECEIPT_ID
PROOF_HAS_PROGRESS_FIELD
DIGEST_INVALID
PROOF_MISSING_DIGEST
DIGEST_MISMATCH
DIGEST_EQUAL_WHEN_MISMATCH
FABRICATED_EXPECTED_DIGEST
AMBIGUOUS_INTERRUPTED_PROOF
UNKNOWN_KIND
```

Parser, file-boundary, and complexity failures use additional explicit codes documented beside the validator.

## Runtime boundary

The follow-up runtime worker should stream bytes and emit checkpoint events off the main render thread. The UI may display progress and finite status, but it must not compute or manufacture trust, silently treat download completion as verification, or expose a governed claim when the result is missing, contradictory, interrupted, or erroneous.

## Validation and acceptance

This contract is satisfied for the initial slice when:

- all four schemas pass Draft 2020-12 meta-validation;
- valid receipt and proof fixtures pass;
- invalid fixtures fail with reviewed code sets;
- duplicate keys, non-finite numbers, unknown kinds, and untrusted-value echo fail closed;
- the dedicated no-network workflow runs the focused tests and fixture profile;
- no emitted receipt, proof, EvidenceBundle, policy decision, release manifest, or public artifact is claimed.

## Rollback

Rollback is an ordinary revert of the contract, schema, fixture, validator, test, workflow, and authoring-receipt files. Because this slice activates no live source, worker, public route, release, or publication state, rollback requires no data migration. A later implementation that persists receipts or proofs must add its own migration and correction plan.
