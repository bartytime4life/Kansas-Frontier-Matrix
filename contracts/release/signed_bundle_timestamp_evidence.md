<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/release/signed-bundle-timestamp-evidence
title: SignedBundleTimestampEvidence Candidate Contract
type: contract
version: v1.0.0
status: proposed-inactive
owners: OWNER_TBD - Release steward; Security steward; Contracts steward; Validation steward
created: 2026-08-09
updated: 2026-08-09
policy_label: internal; fixture-only; non-authoritative
related:
  - ../../schemas/contracts/v1/release/signed_bundle_timestamp_evidence.schema.json
  - ../../fixtures/contracts/v1/release/signed_bundle_timestamp_evidence/cases.json
  - ../../tools/validators/release/validate_signed_bundle_timestamp_evidence.py
  - ../../tests/release/test_signed_bundle_timestamp_evidence.py
  - ../../docs/intake/exploratory/pass-22-signed-bundle-timestamp-evidence-source-map.md
  - ./cosign_attestation_verification_plan.md
  - ../common/spec_hash.md
  - ../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
tags: [kfm, release, security, timestamp, rfc3161, sigstore, cosign, rekor, fixture]
notes:
  - "The profile records declared timestamp material and deterministic assessment only; it performs no cryptographic verification."
  - "Timestamp material supports a later governed decision but is not evidence closure, review approval, or release authority."
[/KFM_META_BLOCK_V2] -->

# SignedBundleTimestampEvidence Candidate Contract

> **Purpose.** Preserve inspectable timestamp-evidence references for a signed promotion bundle, including RFC 3161 material or Sigstore signed-entry timestamp material when available, without turning capture metadata into cryptographic proof or release authority.

## Status and authority

`PROPOSED_INACTIVE`. The contract defines a fixture-only release-support record. It does not execute a timestamp authority, Cosign, Rekor, signature verification, policy engine, release process, or publication process.

The record may point to a promotion bundle, Cosign bundle, policy context, RFC 3161 token, or Rekor entry. A reference does not prove that the target exists, is authentic, was verified, satisfies policy, or authorizes release.

## Responsibility signature

| Axis | Value |
|---|---|
| Artifact kind | Semantic release-support contract |
| Authority owner | Release stewardship, with security review |
| Lifecycle stage | Proof-support candidate; no release decision |
| Execution role | Declarative spec with repository validator |
| Scope | Shared signed-bundle timestamp evidence |
| Exposure | Internal, synthetic fixtures only |
| Mutability | Content-addressed candidate replacement |
| Retention | Review-bound; later policy may define release retention |
| Physical storage | Git for contract and fixtures; external material remains by reference |

Directory Rules basis: this object is owned by the release-support contract family, so meaning belongs in `contracts/release/`; shape in `schemas/contracts/v1/release/`; reusable synthetic inputs in `fixtures/contracts/v1/release/`; repository validation in `tools/`; conformance in `tests/`; read-only CI in `.github/`; and source adaptation in `docs/intake/exploratory/`.

## Required record surfaces

| Surface | Required meaning |
|---|---|
| Identity | Content-derived `evidence_id` and RFC 8785 JCS plus SHA-256 `spec_hash` |
| Subject | Digest-bound promotion-bundle and Cosign-bundle references, plus nullable Rekor UUID |
| Requirement | `REQUIRED`, `OPTIONAL`, or `UNKNOWN` with explicit nullable policy reference |
| Evidence state | `PRESENT`, `ABSENT`, or `UNREADABLE` |
| Evidence items | Canonically ordered RFC 3161, Sigstore signed-entry timestamp, or other signer-timestamp references |
| Assessment | Finite `PASS`, `ABSTAIN`, `DENY`, or `ERROR` outcome with stable reason codes |
| Governance | Capture-only and all verification, policy, review, promotion, release, and publication authority flags false |

## Deterministic assessment

| Requirement | Evidence state | Outcome | Reason code |
|---|---|---|---|
| Any | `PRESENT` | `PASS` | `TIMESTAMP_EVIDENCE_PRESENT` |
| `REQUIRED` | `ABSENT` | `DENY` | `TIMESTAMP_EVIDENCE_REQUIRED_MISSING` |
| `OPTIONAL` | `ABSENT` | `ABSTAIN` | `TIMESTAMP_EVIDENCE_OPTIONAL_ABSENT` |
| `UNKNOWN` | `ABSENT` | `ABSTAIN` | `TIMESTAMP_REQUIREMENT_UNKNOWN` |
| Any | `UNREADABLE` | `ERROR` | `TIMESTAMP_EVIDENCE_UNREADABLE` |

This mapping checks only the record's internal declaration. It does not evaluate or authenticate the referenced policy.

## Binding rules

1. Every evidence item declares whether it binds the promotion bundle or the Cosign bundle and must repeat the corresponding subject digest.
2. An RFC 3161 item requires a declared timestamp-policy object identifier.
3. A Sigstore signed-entry timestamp item requires a Rekor UUID and binds the Cosign bundle.
4. `PRESENT` requires at least one item and no absence code; `ABSENT` or `UNREADABLE` requires no item and at least one bounded absence code.
5. Evidence items and reason-code arrays are unique and lexicographically canonical.
6. `UNKNOWN` requirement state carries no policy-bundle reference; `REQUIRED` and `OPTIONAL` carry one.

These rules preserve traceability only. Token signatures, certificate chains, timestamp-authority trust, Rekor inclusion, integrated time, checkpoint consistency, and cryptographic payload binding remain outside this slice.

## Deterministic identity

Remove `evidence_id` and `spec_hash`, canonicalize the complete remaining record with RFC 8785 JCS, compute SHA-256, and set `evidence_id` to `kfm:signed-bundle-timestamp-evidence:<first 24 digest hex characters>`.

## Explicit non-effects

The slice does not:

- contact or operate an RFC 3161 timestamp authority, Fulcio, Rekor, an OCI registry, or any network service;
- execute Cosign, verify a signature, validate a certificate, verify a transparency log, or authenticate timestamp material;
- resolve evidence, evaluate policy, authenticate review, close a catalog, or decide source truth;
- authorize promotion, release, rollback, alias mutation, deployment, publication, or public use;
- create a release signature or replace the existing Cosign verification-plan boundary.

## Acceptance boundary

- Draft 2020-12 schema meta-validation passes.
- Exact fixture outcomes cover present, required-missing, optional-missing, unknown-requirement, unreadable, binding mismatch, identity drift, and authority overclaim.
- Duplicate keys, non-finite numbers, malformed inputs, and symlinks fail closed.
- Tests and workflow are deterministic and no-network.
- The generated authoring receipt binds final non-receipt artifact bytes; human review remains pending.

## Rollback

Revert the additive slice. It creates no timestamp, signature, release decision, external state, or published carrier.

## Source basis

- `KFM-P22-PROG-0033`: promotion bundles should record RFC 3161 timestamp material when available alongside Rekor UUID and Cosign proof references.
- `KFM-P22-PROG-0052`: signed promotion bundles should preserve RFC 3161 or equivalent signer timestamp evidence when available and policy-relevant.
- Both cards remain `UNCHANGED` in the Pass 23/32 consolidated atlas.

