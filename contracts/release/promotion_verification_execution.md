<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/release/promotion-verification-execution
title: Promotion Verification Execution Contract
type: contract
version: v1.0.0
status: implemented; fixture-first; no-network; non-publisher
owners: OWNER_TBD — release steward; security/signing steward; policy steward; evidence steward; validation steward
created: 2026-08-07
updated: 2026-08-07
policy_label: repository-facing; release; promotion; cryptographic-verification; policy; fail-closed
owning_root: contracts/
responsibility: Define the meaning, finite outcomes, evidence bindings, and non-authority boundary of bounded promotion verification execution.
truth_posture: cite-or-abstain; executable claims require current repository evidence
related:
  - ./cosign_attestation_verification_plan.md
  - ./promotion_decision.md
  - ../../schemas/contracts/v1/release/promotion_verification_execution.schema.json
  - ../../schemas/contracts/v1/release/promotion_verification_execution_result.schema.json
  - ../../tools/validators/promotion_gate/execute_promotion_verification.py
  - ../../tools/validators/promotion_gate/README.md
  - ../../tools/validators/release/validate_cosign_attestation_verification_plan.py
  - ../../fixtures/release/promotion_verification_execution/
  - ../../tests/release/test_promotion_verification_execution.py
  - ../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
notes:
  - "This executor composes current readiness and plan validators with exact-byte local references, an explicitly supplied Cosign binary, and an explicitly supplied Conftest binary."
  - "Fixture CI uses deterministic fake tools; it proves adapter behavior, not production cryptography or a current external tool installation."
  - "A PASS means APPROVE_READY for accountable review only. It never emits or implies APPROVE, PROMOTED, RELEASED, DEPLOYED, or PUBLISHED."
[/KFM_META_BLOCK_V2] -->

# Promotion verification execution

> **Purpose.** Execute a bounded, explicit, no-network verification packet that composes the existing A–G readiness validator, the existing Cosign plan validator, exact-byte subject and bundle bindings, policy evaluation, and local EvidenceBundle/catalog/rollback closure—without promoting, releasing, deploying, or publishing anything.

## Status

| Surface | Current status | Boundary |
|---|---|---|
| `PromotionVerificationExecution` | **CONFIRMED schema + fixtures** | Declares every file, digest, reference, policy file, and tool digest explicitly. |
| Executor | **CONFIRMED fixture-tested** | Runs validators and supplied tools without a shell; bounds runtime and output; emits one deterministic result. |
| `PromotionVerificationExecutionResult` | **CONFIRMED schema** | Finite `PASS | ABSTAIN | DENY | ERROR`; all authority flags remain false. |
| Fixture toolchain | **CONFIRMED deterministic fake tools** | Exercises exact command wiring, exit polarity, digest substitution denial, and policy behavior. |
| Production Cosign/Conftest installation | **NEEDS VERIFICATION / not supplied** | A separate security-reviewed workflow must install immutable binaries and verify their digests. |
| Promotion/release/publication | **NOT PERFORMED** | PASS is readiness evidence for review only. |

## Directory Rules basis

Object meaning belongs under `contracts/release/`. Machine shapes belong under `schemas/contracts/v1/release/`. The repository-owned executor remains in the established `tools/validators/promotion_gate/` specialization. Reusable synthetic inputs and fake tools belong under `fixtures/release/`; executable conformance belongs under `tests/release/`; read-only orchestration belongs under `.github/workflows/`; and AI authoring provenance belongs under `data/receipts/generated/`.

No new responsibility root, signing authority, policy authority, proof store, release lane, or publication path is introduced.

## Execution packet

The packet binds:

- one promotion packet and SHA-256;
- one validated `CosignAttestationVerificationPlan` and SHA-256;
- one exact subject file and one exact Sigstore bundle file;
- one policy directory, every policy file digest, and the expected Conftest binary digest;
- local references for `EVIDENCE_BUNDLE`, `STAC`, `DCAT`, `PROV`, and `ROLLBACK`, plus `CORRECTION` when the packet supersedes a prior release;
- a deterministic execution `spec_hash`; and
- explicit no-network, no-write, and no-authority declarations.

All repository paths are relative, traversal-free, inside the selected repository root, non-symlink, and explicitly digest-bound.

## Execution sequence

1. Validate the execution schema and `spec_hash`.
2. Resolve and hash the promotion packet and Cosign plan.
3. Execute the existing promotion gate validator.
4. Execute the existing Cosign-plan validator, including its patched-version and claim-validation floor.
5. Recompute the supplied Cosign binary digest and deny substitution.
6. Recompute subject and bundle digests, then execute the plan's exact offline `verify-blob-attestation` invocation without a shell.
7. Recompute the Conftest binary and policy-file digests, then evaluate the promotion packet with the declared policy directory.
8. Resolve every reference ID to an exact local object; require shared `subject_spec_hash` and release artifact digest closure.
9. Emit a deterministic `PromotionVerificationExecutionResult`.

Tool stdout and stderr are never treated as authority. The executor records only bounded hashes, exit status, exact-byte bindings, existing-validator results, and finite findings.

## Finite outcomes

| Outcome | Meaning | Exit |
|---|---|---:|
| `PASS` | Every bounded readiness, tool, policy, and reference check passed; result is `APPROVE_READY`. | `0` |
| `ABSTAIN` | Required evidence support is unresolved without an unsafe contradiction. | `1` |
| `DENY` | A digest, reference, policy, readiness, binary, subject, bundle, or tool verification condition failed. | `1` |
| `ERROR` | A validator/tool could not execute safely or its result was malformed/oversized. | `2` |

Precedence is `ERROR > DENY > ABSTAIN > PASS`.

## What PASS proves

PASS proves only that the bounded executor ran over the declared bytes and found no failure in its current profile. It does not prove:

- production tool provenance or the current security status of a later-installed binary;
- that the synthetic bundle is a real Sigstore bundle;
- source truth, rights, sensitivity clearance, live reviewer identity, or release authority;
- that referenced evidence is externally authentic rather than fixture-local;
- immutable publication, deployment, public serving, correction propagation, or rollback execution; or
- that a repository workflow is required by branch protection.

## Commands

```bash
python tools/validators/promotion_gate/execute_promotion_verification.py \
  fixtures/release/promotion_verification_execution/valid/pass.json \
  --cosign-bin fixtures/release/promotion_verification_execution/bin/fake_cosign.py \
  --conftest-bin fixtures/release/promotion_verification_execution/bin/fake_conftest.py

python -m pytest tests/release/test_promotion_verification_execution.py -q
```

## Production graduation hold

Before using a real Cosign or Conftest binary, a separate change must recheck current upstream advisories and CLI behavior, install from an immutable source, verify the binary digest, preserve offline verification, validate real bundle fixtures, define trust-root update/retirement behavior, and bind the result into a reviewed promotion decision. That change remains outside this fixture-first PR.

## Rollback

Close the draft PR before merge, or revert the bounded commit after merge. No key, credential, trust root, external service, lifecycle object, release decision, cache, deployment, or public artifact must be revoked.
