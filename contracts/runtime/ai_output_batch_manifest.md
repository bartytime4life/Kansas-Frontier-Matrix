<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/runtime/ai-output-batch-manifest
title: AIOutputBatchManifest Contract
type: contract
version: v1.0.0
status: proposed-inactive
owners: OWNER_TBD — Runtime steward · Governed AI steward · Evidence steward · Correction steward · Validation steward
created: 2026-08-08
updated: 2026-08-08
policy_label: internal; fixture-only; non-authoritative
related:
  - ../../schemas/contracts/v1/runtime/ai_output_batch_manifest.schema.json
  - ../../fixtures/contracts/v1/runtime/ai_output_artifact/
  - ../../tools/validators/ai/validate_ai_output_artifact.py
  - ../../tests/validators/test_validate_ai_output_artifact.py
  - ai_output_artifact.md
  - ai_receipt.md
  - ../release/release_manifest.md
  - ../../docs/adr/ADR-0019-ai-adapter-contract-and-finite-envelopes.md
  - ../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
tags: [kfm, runtime, governed-ai, batch-manifest, partial-revocation, spec-hash]
notes:
  - "Implements the batch-level meta-bundle direction in Pass 7 KFM-P7-IDEA-0001."
  - "The manifest names per-input artifacts; it does not merge their truth, evidence, policy, review, or release authority."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# AIOutputBatchManifest Contract

> **Purpose.** Name a canonical set of independently identified `AIOutputArtifact` records so batch membership, finite outcomes, and partial revocation are inspectable without turning the batch into one indivisible authority object.

## Status and boundary

| Field | Value |
|---|---|
| Contract status | `PROPOSED_INACTIVE` |
| Execution mode | `FIXTURE_ONLY` |
| Machine shape | `schemas/contracts/v1/runtime/ai_output_batch_manifest.schema.json` |
| Validator | `tools/validators/ai/validate_ai_output_artifact.py` |
| Artifact resolution | None |
| Release-manifest equivalence | Explicitly denied |
| Promotion, release, publication, public-use effect | None |

The manifest is an index over artifact identities and status snapshots. It is not an `EvidenceBundle`, `AIReceipt`, proof pack, `ReleaseManifest`, or publication record.

## Source-derived design

Pass 7 asks whether a batch-level meta-bundle should name a classification batch and proposes a release-manifest analog at the AI-output level. This contract adopts only the naming and integrity pattern. It deliberately excludes release authority and keeps each per-input artifact independently revocable.

## Manifest contents

A manifest carries:

- stable batch identity and source-batch reference;
- canonical artifact entries containing input ref, artifact ID, artifact `spec_hash`, outcome, and lineage status;
- exact counts for outcome and lineage dimensions;
- manifest status: `ACTIVE`, `PARTIALLY_REVOKED`, `SUPERSEDED`, or `WITHDRAWN`;
- append-only prior-manifest and correction references;
- run-receipt references; and
- fixed false governance-effect flags.

The manifest does not carry model output bytes, prompts, reasoning traces, evidence payloads, policy rules, signatures, or release decisions.

## Partial revocation behavior

A later manifest revision may mark one item `REVOKED` while retaining unchanged IDs and hashes for unaffected artifacts. The manifest receives a new `spec_hash` and links to the prior manifest plus correction record. Unaffected artifacts are not regenerated and are not bulk-invalidated.

Status is derived deterministically:

| Artifact-status composition | Manifest status |
|---|---|
| Every item `REVOKED` | `WITHDRAWN` |
| Every item `SUPERSEDED` | `SUPERSEDED` |
| At least one `REVOKED`, but not every item | `PARTIALLY_REVOKED` |
| Otherwise | `ACTIVE` |

## Canonicalization and identity

Artifact entries must be sorted by `input_ref`. Input refs, artifact IDs, and artifact hashes must each be unique.

```text
spec_hash  = SHA-256(RFC8785-JCS(manifest except manifest_id/spec_hash))
manifest_id = "ai-output-batch-manifest:" + first 24 hex characters of spec_hash
```

Recorded counts and `batch_status` must equal a fresh deterministic reduction of the artifact list.

## Trust boundary

A validator `PASS` proves only closed local shape, deterministic manifest identity, canonical membership, exact counts, and visible partial-revocation state. It does not resolve artifact records, verify output bytes, authenticate references, execute policy, approve review, sign a batch, authorize release, or publish anything.

## Validation

```bash
python tools/validators/ai/validate_ai_output_artifact.py --fixtures
```

## Rollback

Rollback is repository-only because the profile has no runtime registration, model execution, lifecycle write, cache, API, release, or public artifact.

## Open verification

- Which runtime or offline builder owns manifest assembly?
- Should batch manifests later support Merkle membership proofs?
- Which correction object records a per-input revocation decision?
- Should released AI-derived products reference this manifest from `ReleaseManifest`, or reference only approved individual artifacts?

<p align="right"><a href="#top">Back to top</a></p>
