<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/runtime/verified-rendering-resource-envelope
title: VerifiedRenderingResourceEnvelope Candidate Contract
type: semantic-contract
version: v1.0.0
status: proposed-inactive; fixture-only; non-authoritative
owners: OWNER_TBD — Map runtime steward · UI steward · Evidence steward · Security steward
created: 2026-08-09
updated: 2026-08-09
policy_label: internal; runtime; rendering; verification-order; resource-budget; fail-closed
owning_root: contracts/
responsibility: Validate a synthetic worker trace and declared budgets for verify-before-decode rendering composition without fetching, hashing, verifying, decoding, rendering, or selecting a renderer.
truth_posture: CONFIRMED synthetic fixture behavior / PROPOSED semantic contract pending steward review / NEEDS VERIFICATION hosted exact-head execution and any future worker integration
related:
  - ../ui/renderer_capability_profile.md
  - ../evidence/verifier_capability_portability.md
  - ../../docs/standards/pmtiles/PMTILES_ATTESTATION_STANDARD.md
  - ../../schemas/contracts/v1/runtime/verified_rendering_resource_envelope.schema.json
  - ../../fixtures/contracts/v1/runtime/verified_rendering_resource_envelope/cases.json
  - ../../tools/validators/runtime/validate_verified_rendering_resource_envelope.py
  - ../../tests/validators/test_validate_verified_rendering_resource_envelope.py
  - ../../docs/intake/exploratory/verified-rendering-resource-envelope-source-map.md
tags: [kfm, runtime, rendering, verification, worker, budget, fixture]
notes:
  - "Adapts Full Atlas KFM-TRIAD-052 / KFM-CAND-0154..0156 as one bounded trace-assessment candidate."
  - "Synthetic PASS never means that bytes, proofs, signers, or releases were actually verified."
[/KFM_META_BLOCK_V2] -->

# VerifiedRenderingResourceEnvelope Candidate Contract

`VerifiedRenderingResourceEnvelopeCandidate` records a synthetic release binding, resource limits, chunk-accounting declaration, and governed worker-message trace. Its validator reproduces whether the trace declares verification completion before decode and render stages while staying within explicit fetch, hash-chunk, decode, heap, CPU, queue, and concurrency budgets.

## Authority boundary

This is a composition and conformance candidate, not a worker. It never fetches a URL, reads an artifact, hashes bytes, parses a proof, authenticates a signer, loads trust material, decodes a tile, initializes MapLibre, renders content, or shows a frame. Stage names and `PASS` message results are synthetic declarations only.

The candidate composes but does not replace:

- the renderer capability profile, which declares adapter compatibility but admits no renderer;
- verifier capability portability, which compares environment declarations but performs no cryptography; and
- the PMTiles attestation standard and validator, which own artifact-integrity semantics outside this packet.

## Worker trace and chunk accounting

Normal traces declare `QUEUED`, fetch start and completion, hash completion, proof check, signer check, verification completion, decode start, and render readiness in contiguous sequence order. Chunk records must be contiguous, stay within `hash_chunk_bytes`, and sum to the declared hashed bytes. A syntactically valid trace can still produce a blocked, cancelled, or failed state.

## Finite states

| State | Meaning | Non-effect |
|---|---|---|
| `READY_FOR_SEPARATE_EXECUTION` | The synthetic trace is ordered, complete, and within declared budgets. | No verification, decode, render, or execution is authorized. |
| `DEGRADED` | A lower-detail or evidence-summary fallback is declared. | The fallback is not selected or rendered. |
| `BLOCKED` | Corruption, truncation, replay, timeout, budget exhaustion, failed declaration, missing stage, or unsafe ordering is declared. | No partial or unverified content is permitted. |
| `CANCELLED` | Cancellation is declared and bound to a worker message. | No worker is stopped by this validator. |
| `ERROR` | Worker failure is declared and bound to a worker message. | No retry or fallback is executed. |

Worker failure outranks cancellation; cancellation outranks other blocked findings. Validator `PASS` means the assessment exactly matches the declaration, including a blocked or failed declaration.

## Deterministic identity and validation

The validator requires contiguous trace and chunk indexes, fault-to-message binding, exact finite-state derivation, resource and chunk closure, verify-before-decode ordering, and RFC 8785 JCS plus SHA-256 identity. `spec_hash` excludes only `envelope_id` and `spec_hash`; the identifier uses the first 24 digest characters.

## Directory Rules basis

This object concerns bounded runtime process composition, so semantic meaning belongs under `contracts/runtime/`. Renderer compatibility stays under `contracts/ui/`, verification meaning stays under `contracts/evidence/` and PMTiles standards, and release decisions stay under `contracts/release/`. Machine shape, fixtures, validation, tests, CI, source adaptation, and authoring provenance remain in their established roots.

## Non-effects and rollback

A green result cannot resolve bytes, verify a digest, proof, signature, signer, trust root, or release; select a renderer; permit network use; decode or render; show unverified content; resolve evidence; evaluate policy; approve review; release; deploy; publish; or authorize public use. Before merge, close the draft PR and retire its branch. After an authorized merge, revert the additive packet; it has no live worker or external state.
