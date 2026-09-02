<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/evidence/release-bound-run-receipt
title: ReleaseBoundRunReceipt Proof Profile
type: semantic-contract; proof-object profile
version: v1.0.0
status: proposed-inactive; fixture-only; no-network; non-authoritative
created: 2026-08-09
updated: 2026-08-09
owning_root: contracts/
policy_label: internal; evidence; receipt; attestation; release-candidate
related:
  - ../../schemas/contracts/v1/evidence/release_bound_run_receipt.schema.json
  - ../../fixtures/contracts/v1/evidence/release_bound_run_receipt/cases.json
  - ../../tools/validators/evidence/validate_release_bound_run_receipt.py
  - ../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
[/KFM_META_BLOCK_V2] -->

# ReleaseBoundRunReceipt proof profile

`ReleaseBoundRunReceipt` is an additive proof profile that binds one runtime receipt summary to immutable input and output artifacts, evidence, policy, review, attestation, correction, and rollback references. It addresses the Pass 12 call for machine-parseable proof objects without replacing the existing runtime `RunReceipt` contract.

## Boundary

The profile is `PROPOSED_INACTIVE`, fixture-only, and no-network. Its `PASS` outcome means only that the declaration is internally coherent under this profile. It does **not** resolve evidence, evaluate policy, authenticate review, verify a signature, promote lifecycle state, create a `ReleaseManifest`, release, deploy, publish, or authorize public use.

## Required closure

A passing declaration has:

- one deterministic `profile_spec_hash`;
- immutable runtime receipt, input, output, evidence, policy, review, correction, and rollback references;
- exact input/output URI parity with the bound runtime receipt summary;
- at least one declared verified attestation;
- resolved evidence, allowed policy, approved review, ready correction, and ready rollback posture;
- every authority claim fixed to `false`.

Finite outcomes are `PASS`, `ABSTAIN`, `DENY`, and `ERROR`. Pending evidence, review, or signature state abstains; explicit failure, integrity mismatch, mutable authority reference, or authority overclaim fails closed.

## Directory Rules basis

The accepted Directory Rules v2 place object meaning in `contracts/evidence/`, machine shape in `schemas/contracts/v1/evidence/`, synthetic cases in `fixtures/contracts/v1/evidence/`, executable validation in `tools/validators/evidence/`, tests in `tests/validators/`, CI in `.github/workflows/`, and generated authoring accountability in `data/receipts/generated/`. No new root or parallel receipt, proof, release, or publication authority is created.

## Validation

```bash
python -m unittest tests.validators.test_validate_release_bound_run_receipt -v
python tools/validators/evidence/validate_release_bound_run_receipt.py --fixtures
```

## Rollback

Revert this additive packet. It performs no source, lifecycle, catalog, policy, review, signature, release, cache, or public-route mutation.
