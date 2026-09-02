<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/runtime/worker-integrity-launch-readiness
title: Worker Integrity Launch Readiness Candidate
type: semantic-contract
version: v0.1.0
status: proposed; inactive; review-pending; non-authoritative
owners: OWNER_TBD — Runtime steward · Security steward · Evidence steward · Contract steward
created: 2026-08-10
updated: 2026-08-10
policy_label: internal; runtime; worker; integrity; fixture-only
owning_root: contracts/
responsibility: Define the deterministic pre-launch readiness meaning for a synthetic worker identity, declared RuntimeVerificationProof outcome, and required browser capabilities.
truth_posture: PROPOSED source-grounded adaptation / CONFIRMED deterministic fixture validation / no worker launch, proof resolution, policy, release, or publication authority
related:
  - ./runtime_verification.md
  - ./verified_rendering_resource_envelope.md
  - ../../schemas/contracts/v1/runtime/worker_integrity_launch_readiness.schema.json
  - ../../fixtures/contracts/v1/runtime/worker_integrity_launch_readiness/cases.json
  - ../../tools/validators/runtime/validate_worker_integrity_launch_readiness.py
  - ../../tests/validators/test_worker_integrity_launch_readiness.py
  - ../../docs/intake/exploratory/worker-integrity-launch-readiness-source-map.md
tags: [kfm, runtime, worker, integrity, isolation, readiness, fixture-only]
notes:
  - "Consumes only a synthetic declaration of RuntimeVerificationProof state; digest equality remains owned by the existing runtime-verification contract."
  - "READY_CANDIDATE is reviewable fixture coherence, never permission to launch a worker."
[/KFM_META_BLOCK_V2] -->

# Worker Integrity Launch Readiness Candidate

> A deterministic, fixture-only preflight that composes a synthetic worker
> identity, a declared runtime-verification outcome, and required browser
> capabilities without starting a worker or resolving a proof.

## Status and purpose

| Field | Value |
|---|---|
| Profile | `kfm.worker-integrity-launch-readiness.v1` |
| State | `PROPOSED` / inactive / review-pending |
| Execution mode | Synthetic fixture validation only |
| Worker launch, policy, release, or publication effect | None |

The Drive source proposes a fail-closed worker-integrity membrane: required
workers must have explicit identity, integrity evidence, and runtime capability
posture before execution. The repository already has a generic
`RuntimeVerificationProof` family for digest outcomes and a separate verified
rendering resource envelope for synthetic trace ordering and budgets. This
candidate fills only the remaining pre-launch composition seam.

It does not copy digests or re-decide verification. It consumes a synthetic
declaration of a `RuntimeVerificationProof` reference and finite outcome, then
derives whether the launch proposal is ready for separate review, must abstain,
or must be denied.

## Readiness inputs

Each candidate declares:

- a synthetic worker identity and synthetic asset reference;
- whether cross-origin isolation, `SharedArrayBuffer`, and WASM are required;
- the observed boolean capability posture;
- a nullable `RuntimeVerificationProof` reference and its declared finite
  outcome; and
- fixed-false execution and authority boundaries.

Real URLs, package coordinates, worker source, executable bytes, digests,
headers, credentials, and remote discovery do not belong in this profile.

## Deterministic outcome precedence

| Condition | Readiness outcome | Reason |
|---|---|---|
| Worker runtime unsupported | `DENY` | `WORKER_UNSUPPORTED` |
| Required isolation unavailable | `DENY` | `RUNTIME_ISOLATION_REQUIRED_BUT_UNAVAILABLE` |
| Required `SharedArrayBuffer` or WASM unavailable | `DENY` | `REQUIRED_RUNTIME_CAPABILITY_UNAVAILABLE` |
| Verification proof declaration absent | `ABSTAIN` | `REQUIRED_WORKER_VERIFICATION_MISSING` |
| Proof declares `MISSING_DECLARATION` | `ABSTAIN` | `REQUIRED_WORKER_MANIFEST_MISSING` |
| Proof declares `INTERRUPTED` | `ABSTAIN` | `WORKER_VERIFICATION_INTERRUPTED` |
| Proof declares `MISMATCH` | `DENY` | `WORKER_INTEGRITY_MISMATCH` |
| Proof declares `ERROR` | `DENY` | `WORKER_VERIFICATION_ERROR` |
| Proof declares `VERIFIED` and capabilities satisfy requirements | `READY_CANDIDATE` | `WORKER_READY_CANDIDATE` |

Capability failures take precedence because the worker cannot safely launch on
the declared runtime even when a separate proof is declared verified.

## Validator outcomes

| Validator outcome | Meaning | Non-effect |
|---|---|---|
| `PASS` | Derived readiness is `READY_CANDIDATE`. | Still review-required; worker launch remains unauthorized. |
| `ABSTAIN` | Required proof or verification completion is unavailable. | No evidence or capability is inferred. |
| `DENY` | Readiness is denied, or shape/identity/derivation fails. | No worker, retry, fallback, or policy action executes. |
| `ERROR` | Input cannot be boundedly read or parsed. | No candidate values are trusted. |

A valid `ABSTAIN` or `DENY` candidate remains useful fixture evidence and is
not a validator failure. Findings are reserved for malformed, contradictory,
stale, or authority-overclaiming candidates.

## Directory Rules basis

| Responsibility | Home |
|---|---|
| Pre-launch runtime composition meaning | `contracts/runtime/` |
| Machine shape | `schemas/contracts/v1/runtime/` |
| Synthetic examples | `fixtures/contracts/v1/runtime/` |
| Deterministic validation | `tools/validators/runtime/` |
| Executable checks | `tests/validators/` |
| Source reconciliation | `docs/intake/exploratory/` |
| Hosted read-only orchestration | `.github/workflows/` |
| AI authoring provenance | `data/receipts/generated/` |

The Drive source's older `contracts/runtime_verification/`,
`schemas/runtime_verification/`, and `tests/e2e/` paths are not reproduced.
The current responsibility roots and existing runtime-verification family are
preserved, and no parallel proof or runtime authority is created.

## Relationship to adjacent contracts

- `RuntimeVerificationProof` owns digest declaration, observation, equality,
  and finite verification outcome semantics.
- `VerifiedRenderingResourceEnvelopeCandidate` owns synthetic verify-before-
  decode trace ordering, resource budgets, cancellation, and worker failure.
- This candidate owns only pre-launch composition of declared proof state and
  runtime capability readiness.

None resolves the others merely by carrying a reference.

## Non-effects and rollback

A green result does not resolve or authenticate a proof, read or hash bytes,
inspect response headers, start or stop a worker, enable cross-origin
isolation, evaluate policy, approve review, release, deploy, publish, or
authorize public use. Before merge, close the draft and delete its branch.
After an authorized merge, revert the additive packet; no worker, data, proof,
runtime, release, deployment, or public state requires restoration.
