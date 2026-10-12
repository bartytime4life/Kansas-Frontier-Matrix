<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/evidence/claim-envelope
title: ClaimEnvelope Contract
class: semantic-contract
version: 0.1.0
status: proposed
truth_posture: cite-or-abstain
responsibility_root: contracts/
related:
  - contracts/evidence/README.md
  - contracts/evidence/evidence_ref.md
  - contracts/evidence/evidence_bundle.md
  - contracts/runtime/decision_envelope.md
  - schemas/contracts/v1/evidence/claim_envelope.schema.json
  - fixtures/contracts/v1/evidence/claim_envelope/
  - tools/validators/validate_claim_envelope.py
  - docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
notes:
  - "PROPOSED semantic contract derived from KFM Components Pass 18 P0 schema-wave pressure."
  - "Validation proves local shape and bounded semantics only; it does not resolve evidence, decide policy, approve review, release, publish, or authorize public use."
[/KFM_META_BLOCK_V2] -->

# ClaimEnvelope Contract

> **PROPOSED:** `ClaimEnvelope` is the smallest shared, inspectable carrier that binds a bounded claim to its spatial and temporal scope, source and evidence references, policy/review/release posture, and correction/rollback path.

## Authority boundary

| Responsibility | Owning surface |
|---|---|
| Object meaning | `contracts/evidence/claim_envelope.md` |
| Machine shape | `schemas/contracts/v1/evidence/claim_envelope.schema.json` |
| Deterministic local validation | `tools/validators/validate_claim_envelope.py` |
| Positive and negative examples | `fixtures/contracts/v1/evidence/claim_envelope/` |
| Evidence closure | `EvidenceBundle` and the governed resolver |
| Admissibility | `PolicyDecision` and review controls |
| Release, correction, rollback | `release/` object families |
| Public rendering | Governed APIs and released, public-safe UI payloads |

A `ClaimEnvelope` is **not** evidence, proof, policy, approval, release, publication, or a public API response by itself.

## Required semantics

A conforming envelope identifies:

- a stable `claim_id` and semantic `version`;
- the bounded claim `statement` and its `knowledge_character`;
- explicit `spatial_scope` and `temporal_scope`;
- sorted, unique `evidence_refs` and `source_refs`;
- finite `support_state`, `policy_state`, `review_state`, and `release_state` values;
- a deterministic `spec_hash`;
- `release_ref`, `correction_path_ref`, and `rollback_ref` where publication is claimed.

## Knowledge character

`knowledge_character` prevents source-role collapse. It distinguishes observation, interpretation, derivation, model output, warning, declaration, OCR extraction, AI proposal, and generalized public view. These labels describe character; they do not establish authority.

## Publication invariant

An envelope may declare `release_state: PUBLISHED` only when all of the following are true:

1. `support_state` is `SUPPORTED`;
2. `policy_state` is `ALLOW`;
3. `review_state` is `APPROVED`;
4. at least one evidence reference and one source reference are present;
5. `release_ref`, `correction_path_ref`, and `rollback_ref` are present;
6. the knowledge character is not `AI_PROPOSAL`;
7. no reference points at RAW, WORK, QUARANTINE, internal, canonical, or model-runtime surfaces.

The validator fails closed when these local conditions do not hold. A local PASS is still only validation evidence; it does not resolve the referenced objects or authorize publication.

## Finite validator outcomes

| Outcome | Meaning |
|---|---|
| `PASS` | The file is schema-valid and satisfies the bounded local semantic rules. |
| `FAIL` | The file is readable, but one or more schema or semantic rules fail. |
| `ERROR` | The file cannot be safely evaluated, such as malformed JSON, duplicate keys, a missing schema, an oversized file, or a denied symlink. |

## Lifecycle and trust membrane

```text
EvidenceRef -> EvidenceBundle resolution -> policy/review -> release decision
          -> ClaimEnvelope projection -> governed API/UI/AI surface
```

The envelope is downstream of evidence and upstream of presentation. It must never create a direct public path to canonical or lifecycle-private stores.

## Validation boundary

The no-network validator checks only:

- Draft 2020-12 schema conformance;
- duplicate keys and non-finite number denial;
- bounded file size and symlink denial;
- canonical sorted/unique reference arrays;
- lifecycle-private reference denial;
- publication completeness;
- temporal ordering;
- `AI_PROPOSAL` non-publication.

It does not fetch references, authenticate reviewers, evaluate policy bundles, verify signatures, assemble releases, or publish.

## Rollback

This additive slice is rolled back by reverting the feature-branch commit. Rollback removes the proposed contract, schema, fixtures, validator, tests, workflow, and generated authoring receipt together; it does not alter any published object or canonical data.
