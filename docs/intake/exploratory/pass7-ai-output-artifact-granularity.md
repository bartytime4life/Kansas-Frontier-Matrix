<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/intake/exploratory/pass7-ai-output-artifact-granularity
title: Pass 7 AI Output Artifact Granularity — Source Adaptation Record
type: source-adaptation-record
version: v1.0.0
status: proposed
owners: OWNER_TBD — Governed AI steward · Evidence steward · Runtime steward · Docs steward
created: 2026-08-08
updated: 2026-08-08
policy_label: internal; exploratory; no-adoption-effect
related:
  - ../../../contracts/runtime/ai_output_artifact.md
  - ../../../contracts/runtime/ai_output_batch_manifest.md
  - ../../../docs/adr/ADR-0019-ai-adapter-contract-and-finite-envelopes.md
  - ../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
tags: [kfm, intake, pass7, governed-ai, artifact-granularity, partial-revocation]
notes:
  - "This record adapts KFM-P7-IDEA-0001; it is not an accepted architecture decision or implementation authority."
[/KFM_META_BLOCK_V2] -->

# Pass 7 AI Output Artifact Granularity — Source Adaptation Record

## Source

| Field | Value |
|---|---|
| Atlas | `KFM_Pass_7_Idea_Index_Category_Atlas_and_Expansion_Dossier.pdf` |
| Stable card | `KFM-P7-IDEA-0001` |
| Source statement | Small AI artifacts should be independently gateable, signable, citable, and revocable; a batch should decompose into per-input identities. |
| Open direction | A batch-level manifest should name artifacts without making one monolithic result object. |

## Admission decision

**ADMITTED AS PROPOSED / INACTIVE FIXTURE PROFILE.** The current repository already has `AIReceipt`, `RuntimeResponseEnvelope`, evidence, policy, correction, and deterministic hashing families. The smallest non-duplicative adaptation is therefore:

1. keep `AIReceipt` as execution accountability;
2. add one detached per-input `AIOutputArtifact` that references the receipt;
3. add one `AIOutputBatchManifest` that references artifact IDs and hashes;
4. preserve per-input correction, revocation, and supersession;
5. add no model execution, result store, live policy, API, release, or public surface.

## Deferred

- live adapter integration;
- output byte storage and retrieval;
- signature and attestation verification;
- evidence, policy, citation, and review reference resolution;
- release-manifest integration;
- correction propagation to indexes, APIs, UI, caches, and published products;
- Merkle or membership-proof support.

## Rejected interpretations

- **Rejected:** treating one batch as one indivisible truth object.
- **Rejected:** storing raw prompts, raw evidence payloads, credentials, or chain-of-thought in the artifact.
- **Rejected:** treating `spec_hash`, a validator PASS, a signature reference, or a batch manifest as evidence or release authority.
- **Rejected:** invalidating unrelated item identities when one output is revoked.

## Verification boundary

Repository implementation is confined to synthetic fixtures and deterministic no-network validation. Hosted exact-head CI and human review remain separate checks. The source PDF is planning evidence; current repository behavior controls implementation claims.
