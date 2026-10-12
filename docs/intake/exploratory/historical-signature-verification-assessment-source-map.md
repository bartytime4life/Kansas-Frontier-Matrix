<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/intake/historical-signature-verification-assessment-source-map
title: Historical Signature Verification Assessment - Source Map and Implementation Boundary
type: exploratory-intake-source-map
version: v0.1.0
status: promoted-to-fixture-candidate; non-authoritative; repository-grounded
owners: OWNER_TBD — Intake steward · Security steward · Release steward · affected domain stewards
created: 2026-08-10
updated: 2026-08-10
policy_label: public; intake; release; security; signature; cite-or-abstain
owning_root: docs/
responsibility: Preserve traceability from supplied Full Atlas historical-signature cards to one bounded repository candidate without adopting cryptographic tools, trust roots, policy, key status, or release authority.
truth_posture: CONFIRMED source-card traceability and inspected-tree collision review / PROPOSED bounded adaptation / NEEDS VERIFICATION security and release review, cryptographic integration, trust policy, and later-main collisions
related:
  - ../../kfm_full_atlas_seed_cards.md
  - ../../doctrine/directory-rules.md
  - ../../adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../security/KEY_ROTATION.md
  - ../../standards/SIGNING.md
  - ../../../contracts/release/historical_signature_verification_assessment.md
  - ../../../contracts/release/release_manifest.md
tags: [kfm, intake, full-atlas, trust-root, signature, rotation, revocation, historical-verification]
notes:
  - "Repository security and signing prose is treated as dated guidance, not proof of active keys, accepted cadence, verifier behavior, or released signatures."
  - "The candidate consumes synthetic verification summaries and never claims cryptographic conformance."
[/KFM_META_BLOCK_V2] -->

# Historical signature verification assessment - source map

> **Outcome:** `KFM-TRIAD-056` and `KFM-CAND-0166` through `KFM-CAND-0168` are adapted into one synthetic, no-cryptography contract packet. It keeps trust status at signing separate from current trust status and fixes every operational authority effect to false.

## Source lineage

| Source | Relevant proposal | Posture used here |
|---|---|---|
| Supplied/Drive `KFM_Full_Atlas_seed_cards.md` | `KFM-TRIAD-056`, `KFM-CAND-0166` through `KFM-CAND-0168` | Design lineage for versioned trust status and historical verification. |
| `docs/security/KEY_ROTATION.md` | Draft key lifecycle, overlap, retirement, revocation, compromise, and receipt guidance | Adjacent prose only; proposed cadences and operational claims are not adopted. |
| `docs/standards/SIGNING.md` and release contracts | Signing and release-boundary documentation | Existing responsibility boundaries retained without modification. |
| Directory Rules plus accepted ADR-0029 | Responsibility-root placement and no-parallel-authority rules | Placement authority. |

## Current-main collision review

Bounded repository and pull-request searches found substantial rotation, signing, attestation, release-manifest, reviewer-signature, and incident-response prose. No common machine contract named `TrustRootRecord`, `KeyStatusEvent`, `HistoricalVerificationReceipt`, or `HistoricalSignatureVerificationAssessment` was found that derives key status at two clocks and prevents current status from silently rewriting historical evidence. This is **CONFIRMED for the inspected tree**, not a timeless repository claim.

The candidate deliberately lives in `contracts/release/` because it assesses a declared artifact-signature result for later release review. It does not create `contracts/security/`, a trust store, key register, signing service, identity authority, policy bundle, or release record.

## Bounded adaptation

The candidate keeps:

- artifact digest, signature reference, signer identity, and key identity separate;
- signing time and later verification time separate;
- trust-profile version at signing and verification;
- ordered effective-dated key-status events;
- derived status snapshots at both clocks;
- active, verify-only, expired, revoked, compromised, superseded, and unknown states;
- online/offline posture and explicit offline-material completeness;
- a declared cryptographic-verification summary that this validator does not produce; and
- deterministic identity, exact fixture polarity, and fixed false authority flags.

It excludes keys, certificates, signature bytes, tokens, credentials, cryptographic verification, transparency-log resolution, trust-store access, network calls, policy evaluation, incident adjudication, signing, re-signing, key mutation, release, correction, withdrawal, deployment, publication, and public use.

## Directory Rules placement

| Artifact responsibility | Path |
|---|---|
| Release-facing semantic meaning | `contracts/release/historical_signature_verification_assessment.md` |
| Canonical machine shape | `schemas/contracts/v1/release/historical_signature_verification_assessment.schema.json` |
| Reusable synthetic cases | `fixtures/contracts/v1/release/historical_signature_verification_assessment/cases.json` |
| Repository validator | `tools/validators/release/validate_historical_signature_verification_assessment.py` |
| Executable evidence | `tests/validators/test_validate_historical_signature_verification_assessment.py` |
| Hosted orchestration | `.github/workflows/historical-signature-verification-assessment.yml` |
| Human source adaptation | This file under `docs/intake/exploratory/` |
| AI-authoring process memory | `data/receipts/generated/` |

No new root or parallel security, key, identity, schema, policy, evidence, receipt, proof, release, or publication home is created.

## Verification still required

Security and release stewards must separately decide trust-profile ownership, signer authorization, revocation and compromise semantics, incident duties, verifier software, cryptographic formats, transparency evidence, offline trust-material packaging, correction/withdrawal triggers, and release integration. Any operational implementation requires current primary-source verification and a threat model.

## Validation and rollback

Validation covers Draft 2020-12 schema validity, exact `PASS/ABSTAIN/DENY/ERROR` fixture polarity, two-clock status derivation, event ordering, authorization, offline-material, trust-profile, deterministic identity, parser bounds, no-cryptography imports, workflow parsing, documentation metadata, and generated-receipt hashes.

Rollback is an ordinary revert of the additive packet. Because no key, trust store, signature, artifact, release, correction, withdrawal, runtime, cache, or publication state is created, no operational data migration is required.
