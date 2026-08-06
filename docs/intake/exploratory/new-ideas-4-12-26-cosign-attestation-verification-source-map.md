<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/intake/new-ideas-4-12-cosign-attestation-verification-source-map
title: New Ideas 4-12-26 — Cosign Attestation Verification Source Map
type: exploratory-source-map
version: v1.0.0
status: PROPOSED; source adaptation; non-authoritative
created: 2026-08-06
updated: 2026-08-06
policy_label: repository-facing; exploratory; security
related:
  - ../../../contracts/release/cosign_attestation_verification_plan.md
  - ../../../tools/validators/promotion_gate/README.md
  - ../../../docs/standards/SIGNING.md
  - ../../../docs/doctrine/directory-rules.md
[/KFM_META_BLOCK_V2] -->

# New Ideas 4-12-26 — Cosign attestation verification source map

## Source pressure

The supplied packet proposes a fail-closed promotion membrane that combines explicit release inputs, strict Cosign/DSSE verification, Rekor transparency material, exact subject and predicate binding, catalog closure, and policy checks. It specifically warns that affected Cosign versions could report malformed or mismatched attestations as verified and names patched release floors.

The same packet separates receipts from proofs and says public or promotion decisions must not be inferred from console output, file presence, or unchecked declaration flags.

## Current authoritative verification

Current official/NVD verification performed for this implementation establishes:

- advisory `CVE-2026-39395` / `GHSA-w6c6-c85g-mmv6` concerns malformed payload or mismatched predicate acceptance in `verify-blob-attestation`;
- patched version floors are Cosign `2.6.3` and `3.0.6`;
- disabling claim checks weakens the verification boundary and is not admitted by this profile.

These are version-sensitive facts. A future runtime integration must recheck the advisory and currently supported releases rather than assuming this fixture baseline is permanent.

## Repository assay

Current repository evidence shows:

- a seven-gate promotion readiness validator already exists;
- Gate F accepts declared evidence, attestation, and STAC/DCAT/PROV references;
- the validator explicitly does not dereference those references or verify DSSE/Cosign cryptography;
- release semantics, schemas, validators, fixtures, tests, workflows, and generated receipts already have established responsibility roots.

Therefore the smallest dependency-closed adaptation is not another promotion gate or catalog matrix. It is a fixture-only Cosign invocation preflight that freezes the security-sensitive inputs and non-authority boundary before a later executor is admitted.

## Implemented adaptation

This slice adds:

- `CosignAttestationVerificationPlan` semantic meaning;
- a strict Draft 2020-12 schema;
- patched-version, subject/predicate/bundle, trust-mode, transparency, offline-material, network, insecure-registry, finite-outcome, governance, and deterministic-hash checks;
- public-safe positive and negative fixtures;
- exact finding-code tests;
- a no-network path-scoped workflow; and
- generated authoring provenance.

## Deferred work

A later separately reviewed change must execute a pinned Cosign binary over exact artifact and bundle bytes and emit an authenticated result. Integration into promotion Gate F remains deferred until that runtime boundary, result object, negative cryptographic fixtures, tool installation provenance, and current advisory review exist.

No source activation, signing key, trust root, cryptographic verification, policy evaluation, release, deployment, promotion, publication, or public route is introduced here.
