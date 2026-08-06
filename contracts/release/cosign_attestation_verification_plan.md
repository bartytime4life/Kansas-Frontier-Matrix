<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/release/cosign-attestation-verification-plan
title: CosignAttestationVerificationPlan Contract
type: contract
version: v1.0.0
status: PROPOSED_INACTIVE; fixture-only; no-network; non-authoritative
owners: OWNER_TBD — release steward; security steward; signing steward; validation steward
created: 2026-08-06
updated: 2026-08-06
policy_label: repository-facing; security; release; attestation; fail-closed
related:
  - ./README.md
  - ./promotion_decision.md
  - ../../docs/standards/SIGNING.md
  - ../../docs/architecture/publication/promotion-gates.md
  - ../../schemas/contracts/v1/release/cosign_attestation_verification_plan.schema.json
  - ../../tools/validators/release/validate_cosign_attestation_verification_plan.py
  - ../../fixtures/contracts/v1/release/cosign_attestation_verification_plan/
  - ../../tests/release/test_cosign_attestation_verification_plan.py
  - ../../docs/doctrine/directory-rules.md
notes:
  - "This contract defines a preflight plan, not a cryptographic verification result."
  - "The profile records the security floor for CVE-2026-39395 / GHSA-w6c6-c85g-mmv6: Cosign 2.x >= 2.6.3 or 3.x >= 3.0.6."
  - "A later runtime adapter must execute Cosign against exact bytes and emit a separately governed result object."
[/KFM_META_BLOCK_V2] -->

# CosignAttestationVerificationPlan

> **One-line purpose.** Define a deterministic, explicit, security-baselined plan for a future `cosign verify-blob-attestation` execution without running Cosign or claiming that any signature, predicate, subject, transparency entry, reviewer, release, or public artifact is authentic.

## Status and source-derived need

**CONFIRMED repository gap.** The implemented promotion-gate readiness validator checks that attestation references are declared but explicitly does not dereference them or verify DSSE/Cosign cryptography. This profile supplies the smallest prerequisite boundary: a plan that a later runtime verifier can consume without inventing version, subject, predicate, bundle, trust-root, or network behavior.

**CONFIRMED security baseline.** The source packet calls for strict claim checking, bundled transparency material, explicit predicate and subject binding, and patched Cosign releases. Current authoritative advisory evidence identifies patched floors of `2.6.3` and `3.0.6` for CVE-2026-39395 / GHSA-w6c6-c85g-mmv6.

**PROPOSED implementation.** This contract and its schema/validator/fixtures are inactive fixture infrastructure. They are not wired into Gate F and do not install or execute Cosign.

## Directory Rules basis

The object explains release-verification intent, so semantic meaning belongs under `contracts/release/`. Machine shape belongs under `schemas/contracts/v1/release/`; reusable fixture inputs under `fixtures/contracts/v1/release/`; executable validation under `tools/validators/release/`; tests under `tests/release/`; orchestration under `.github/workflows/`; and AI authoring provenance under `data/receipts/generated/`.

No new root or parallel signing, release, proof, receipt, policy, or evidence authority is created.

## Meaning

A `CosignAttestationVerificationPlan` is an immutable candidate description of **how** a future verifier must execute. It binds:

- a supported, patched Cosign version and declared binary digest;
- one exact subject artifact reference and SHA-256 digest;
- one exact predicate type with claim validation enabled;
- one digest-addressed Sigstore bundle carrying subject binding and required transparency material;
- exactly one trust mode: keyless certificate identity plus OIDC issuer, or a keyed public-key reference;
- an explicit `verify-blob-attestation` invocation with no implicit discovery, insecure registry allowances, or fixture-time network access;
- finite runtime outcomes `VERIFIED`, `DENIED`, and `ERROR`; and
- non-authority declarations proving that this plan itself performed no verification and authorized nothing.

## Security invariants

1. **Patched verifier floor.** Cosign major version 2 must be at least `2.6.3`; major version 3 must be at least `3.0.6`. Unknown major tracks are held until a reviewed baseline update.
2. **Claim validation cannot be disabled.** `check_claims` must be true. A future adapter must not pass `--check-claims=false` or an equivalent bypass.
3. **Subject binding is exact.** `artifact_ref`, `subject.digest`, bundle subject digest, and invocation subject digest must agree.
4. **Predicate binding is exact.** The requested predicate type and invocation argument must agree.
5. **Bundle binding is exact.** The planned bundle reference and invocation bundle argument must agree, and the bundle itself has a declared SHA-256 digest.
6. **Transparency support is mandatory.** Rekor inclusion and a signed entry timestamp are required, and offline verification material must be embedded for the no-network profile.
7. **Trust mode is exclusive.** Keyless uses certificate identity and OIDC issuer; keyed uses a public key. Mixed or incomplete trust declarations fail closed.
8. **No implicit or insecure discovery.** Inputs are explicit; fixture validation has no network; insecure/HTTP registry flags remain false.
9. **Output text is not authority.** A future runtime may return `VERIFIED` only on a zero exit code plus exact subject/predicate/bundle checks. Console text is never evidence by itself.
10. **The plan grants no authority.** All governance effects remain false and `runtime_result_ref` remains null.

## Deterministic identity

`plan_id` is `cosign-attestation-plan:` plus the first 24 lowercase hexadecimal characters of the subject SHA-256 digest. `spec_hash` is SHA-256 over the UTF-8 JSON object after removing `spec_hash`, sorting object keys, and serializing without insignificant whitespace. This is a profile-local deterministic identity rule; it does not amend the repository-wide canonicalization standard.

## Finite validator findings

The validator emits stable, non-echoing codes including:

- `COSIGN_VERSION_VULNERABLE`
- `COSIGN_VERSION_TRACK_UNSUPPORTED`
- `CLAIM_VALIDATION_DISABLED`
- `SUBJECT_BINDING_MISMATCH`
- `PREDICATE_BINDING_MISMATCH`
- `BUNDLE_BINDING_MISMATCH`
- `TRANSPARENCY_REQUIREMENT_MISSING`
- `KEYLESS_TRUST_INCOMPLETE` / `KEYED_TRUST_INCOMPLETE`
- `NETWORK_POSTURE_UNSAFE`
- `INSECURE_REGISTRY_ALLOWED`
- `GOVERNANCE_BOUNDARY_VIOLATION`
- `SPEC_HASH_MISMATCH`

A passing plan means only that the plan is internally admissible for later execution. It is not `VERIFIED`.

## Future runtime integration

A separate, security-reviewed change may:

1. install Cosign from an immutable source and verify its binary digest;
2. resolve exact subject and bundle bytes;
3. execute `verify-blob-attestation` without weakening claim checks;
4. parse exit status and structured results without trusting console prose;
5. emit a signed `CosignAttestationVerificationResult` or equivalent receipt;
6. bind that result into promotion Gate F; and
7. preserve correction, tool-version retirement, and rollback behavior.

That later change must recheck the then-current Cosign advisory state and must not treat this fixture profile as cryptographic proof.

## Trust boundary and non-effects

This profile does not:

- install or run Cosign;
- verify a signature, certificate, key, DSSE envelope, predicate, subject digest, Rekor entry, or timestamp;
- authenticate a publisher, workflow, reviewer, or release steward;
- resolve an EvidenceRef or EvidenceBundle;
- evaluate rights, sensitivity, policy, review, or release readiness;
- write RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, PUBLISHED, receipt, proof, or release state;
- authorize promotion, release, deployment, publication, or public use.

## Rollback

Revert the bounded implementation commit. The profile introduces no live dependency, signing key, trust root, external service, source activation, lifecycle data, release object, cache, deployment, or public artifact.
