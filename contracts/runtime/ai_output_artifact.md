<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/runtime/ai-output-artifact
title: AIOutputArtifact Contract
type: contract
version: v1.0.0
status: proposed-inactive
owners: OWNER_TBD — Runtime steward · Governed AI steward · Evidence steward · Policy steward · Citation steward · Validation steward
created: 2026-08-08
updated: 2026-08-08
policy_label: internal; fixture-only; non-authoritative; no-chain-of-thought
related:
  - ../../schemas/contracts/v1/runtime/ai_output_artifact.schema.json
  - ../../fixtures/contracts/v1/runtime/ai_output_artifact/
  - ../../tools/validators/ai/validate_ai_output_artifact.py
  - ../../tests/validators/test_validate_ai_output_artifact.py
  - ai_receipt.md
  - runtime_response_envelope.md
  - ../evidence/evidence_bundle.md
  - ../policy/policy_decision.md
  - ../../docs/adr/ADR-0019-ai-adapter-contract-and-finite-envelopes.md
  - ../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
tags: [kfm, runtime, governed-ai, per-input-artifact, spec-hash, revocation, cite-or-abstain]
notes:
  - "Adapts Pass 7 KFM-P7-IDEA-0001 as an inactive fixture profile."
  - "One artifact binds one input and one detached output result; raw prompts, payloads, chain-of-thought, and credentials are excluded."
  - "The artifact is not EvidenceBundle, AIReceipt, PolicyDecision, review approval, release authority, or publication authority."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# AIOutputArtifact Contract

> **Purpose.** Bind one input to one governed AI output record with deterministic identity, finite outcome, evidence/citation/policy references, and append-only correction state so that one result can be cited, inspected, revoked, or superseded without invalidating unrelated results.

## Status and boundary

| Field | Value |
|---|---|
| Contract status | `PROPOSED_INACTIVE` |
| Execution mode | `FIXTURE_ONLY` |
| Machine shape | `schemas/contracts/v1/runtime/ai_output_artifact.schema.json` |
| Validator | `tools/validators/ai/validate_ai_output_artifact.py` |
| Live model or adapter | None |
| Payload persistence | None; output bytes remain detached and digest-bound |
| Evidence/policy/review resolution | None |
| Promotion, release, publication, public-use effect | None |

A conforming record proves only that one synthetic per-input artifact matches this candidate profile and its deterministic invariants. It does not prove that the model output is true, that references resolve, that a signature or review is authentic, or that the result may be exposed.

## Source-derived design

Pass 7 card `KFM-P7-IDEA-0001` rejects monolithic AI result bundles. It calls for deliberately small artifacts, one per input, each independently gateable, signable, citable, and revocable through its own `spec_hash`. This profile realizes that granularity without changing the existing `AIReceipt`: the artifact references an `AIReceipt`, while the receipt remains execution accountability and `EvidenceBundle` remains factual support.

## Directory Rules basis

ADR-0029 adopts Directory Governance Standard v2. This slice uses existing responsibility roots:

| Responsibility | Path family |
|---|---|
| Runtime-facing semantic meaning | `contracts/runtime/` |
| Machine-checkable shape | `schemas/contracts/v1/runtime/` |
| Synthetic examples | `fixtures/contracts/v1/runtime/` |
| Executable governed-AI validation | `tools/validators/ai/` |
| Behavior proof | `tests/validators/` |
| Read-only orchestration | `.github/workflows/` |
| AI-authoring accountability | `data/receipts/generated/` |

No new root or parallel evidence, policy, receipt, proof, release, catalog, or publication home is created.

## Object meaning

An `AIOutputArtifact` binds:

1. one opaque input reference, input digest, and stable batch index;
2. provider-neutral adapter, model, and prompt-profile references;
3. one run and one separately governed `AIReceipt` reference;
4. one finite outcome: `ANSWER`, `ABSTAIN`, `DENY`, or `ERROR`;
5. a detached output reference and digest, or an explicit no-output negative state;
6. evidence, citation, policy, review, and optional attestation references;
7. append-only `ACTIVE`, `REVOKED`, or `SUPERSEDED` lineage; and
8. RFC 8785 JCS plus SHA-256 deterministic identity.

References are carried, not resolved or authenticated, by this profile.

## Per-input and detached-output rule

The artifact contains no raw input, prompt, output prose, model trace, or chain-of-thought. `input_digest` binds the admitted input projection. `result_ref` and `result_digest` bind detached result bytes. `content_inlined` is fixed to `false`.

This keeps each record small while preserving independent identity and revocation. A later storage profile may define where detached result bytes live; this contract does not create that home.

## Finite outcome rules

| Outcome | Required posture |
|---|---|
| `ANSWER` | Detached result reference and media type exist; evidence and citation reference sets are nonempty; reason code includes `AI_OUTPUT_SUPPORTED`. |
| `ABSTAIN` | No detached result reference or media type; reason code includes `AI_OUTPUT_ABSTAINED`. |
| `DENY` | No detached result reference or media type; reason code includes `AI_OUTPUT_DENIED`. |
| `ERROR` | No detached result reference or media type; reason code includes `AI_OUTPUT_ERROR`. |

A valid `ANSWER` is still not truth, review, release, or public-use authority. The fixed governance flags remain `false` for every fixture.

## Lineage rules

| Status | Required closure |
|---|---|
| `ACTIVE` | No correction, successor, revocation time, or revocation reason. |
| `REVOKED` | Correction reference, revocation time, and reason code; no successor. |
| `SUPERSEDED` | Correction reference and successor artifact reference; no revocation time. |

History is never rewritten. A revoked or superseded artifact remains addressable for audit while normal consumers must consult current lineage before use.

## Deterministic identity

The identity subject is the complete object except `artifact_id` and `spec_hash`.

```text
spec_hash  = SHA-256(RFC8785-JCS(identity subject))
artifact_id = "ai-output-artifact:" + first 24 hex characters of spec_hash
```

Set-like reference and reason-code arrays must be sorted and unique. Floating `latest` references and cross-role reference collapse fail validation.

## Trust boundary

A validator `PASS` does not:

- resolve `EvidenceRef` or authenticate `EvidenceBundle`;
- execute or approve policy;
- validate citations;
- authenticate a reviewer, signature, or attestation;
- run a model or adapter;
- expose detached result bytes;
- mutate canonical or lifecycle state;
- authorize promotion, release, publication, or public use.

## Validation

```bash
python -m unittest discover \
  --start-directory tests/validators \
  --pattern 'test_validate_ai_output_artifact.py' \
  --verbose

python tools/validators/ai/validate_ai_output_artifact.py --fixtures
```

## Rollback

Before merge, close the draft pull request and delete its feature branch. After an authorized merge, revert the additive contract/schema/validator/fixture/test/workflow/receipt packet. Because the profile is inactive and fixture-only, rollback requires no model shutdown, source deactivation, data migration, cache invalidation, correction, or release withdrawal.

## Open verification

- Which accepted runtime component will emit detached result bytes and `AIReceipt` records?
- Which policy object decides whether an `ACTIVE/ANSWER` artifact may be consumed?
- Which signature or attestation profile will bind `spec_hash`?
- Which correction service propagates revocation to indexes, batches, APIs, UI, and caches?

<p align="right"><a href="#top">Back to top</a></p>
