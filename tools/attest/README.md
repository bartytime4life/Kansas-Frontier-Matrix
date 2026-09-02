<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-attest-readme
title: Attestation Tools README
type: tool-readme
version: v0.1
status: draft; blank-placeholder-replaced; attest-tooling-lane; PROPOSED / NEEDS VERIFICATION
owners:
  - OWNER_TBD - Tooling steward
  - OWNER_TBD - Security steward
  - OWNER_TBD - Release steward
  - OWNER_TBD - Proof steward
  - OWNER_TBD - CI steward
created: 2026-07-07
updated: 2026-07-07
policy_label: public-doc; tools; attest; signing; verification; receipts; proofs; no-secrets-in-repo; release-gated
tags: [kfm, tools, attest, attestation, signing, verification, receipts, proofs, release, provenance, integrity, no-secrets, NEEDS_VERIFICATION]
related:
  - ../README.md
  - ../../docs/security/SECRETS.md
  - ../../docs/security/KEY_ROTATION.md
  - ../../docs/standards/PROVENANCE.md
  - ../../data/receipts/
  - ../../data/proofs/
  - ../../release/
  - ../../tests/validators/README.md
  - ../../tests/release/README.md
notes:
  - "This README replaces blank placeholder content at tools/attest/README.md."
  - "tools/README.md lists tools/attest/ as PROPOSED-to-create for signing, attestation packaging, and offline verification helpers."
  - "This lane contains executable helper code only. It is not a secret store, key store, receipt store, proof store, release authority, policy authority, or publication authority."
  - "No private keys, credentials, tokens, passphrases, production certificates, or signing secrets belong in this repository path."
  - "Executable inventory, CLI names, signing backend, CI wiring, verification bundle shape, tests, and pass rates remain NEEDS VERIFICATION."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Attestation tools

> Tooling lane for KFM attestation helpers under `tools/attest/`. Use this directory for executable helpers that package, verify, or prepare attestation metadata for receipts, proofs, and release gates without becoming the trust artifact itself.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: tools" src="https://img.shields.io/badge/root-tools%2F-blue">
  <img alt="Lane: attest" src="https://img.shields.io/badge/lane-attest-purple">
  <img alt="Secrets: not in repo" src="https://img.shields.io/badge/secrets-not__in__repo-critical">
  <img alt="Verification: needs verification" src="https://img.shields.io/badge/verification-NEEDS__VERIFICATION-yellow">
</p>

**Path:** `tools/attest/README.md`  
**Status:** draft / blank placeholder replaced / PROPOSED tooling lane  
**Owning root:** `tools/`  
**Lane family:** `attest`  
**Default posture:** deterministic helper code, no embedded secrets, explicit inputs, auditable outputs  
**Truth posture:** CONFIRMED target file existed as blank placeholder content before replacement; CONFIRMED `tools/README.md` lists `tools/attest/` as PROPOSED-to-create; CONFIRMED security docs say real secrets do not belong in the repository; NEEDS VERIFICATION for actual helper files, CLI names, signing backend, tests, CI integration, verification bundle shape, and pass rates.

---

## Scope

Use `tools/attest/` for long-lived, repo-wide executable helpers that support attestation and integrity verification.

In scope:

- attestation packaging helpers;
- signature or digest verification helpers;
- offline verification bundle builders;
- receipt/proof integrity preflight helpers;
- release-gate attestation checks;
- CI helpers that verify attestation metadata without publishing.

Out of scope:

- private keys or production signing secrets;
- receipt, proof, release, policy, schema, contract, or source authority;
- release approval or publication decisions;
- generated attestation bundles as permanent records;
- one-off operational scripts.

---

## Repo fit

| Responsibility | Correct home | Relationship |
|---|---|---|
| Attestation helper code | `tools/attest/` | This lane. |
| General tool boundary | `tools/README.md` | Parent authority and placement rules. |
| Receipts | `data/receipts/` | Output records; not stored here. |
| Proof bundles | `data/proofs/` | Proof authority; not stored here. |
| Release records | `release/` | Publication decisions and rollback authority. |
| Tests | `tests/validators/`, `tests/release/`, or dedicated accepted test lanes | Tests call tools; tools are not tests. |
| Security standards | `docs/security/` and `docs/standards/` | Security and provenance doctrine. |
| Small one-off helpers | `scripts/` | Holding pen until trust-bearing and long-lived. |
| Reusable libraries | `packages/` | Importable library code, not CLI-only tooling. |

> [!IMPORTANT]
> `tools/attest/` must not become a key store, secret store, proof store, receipt store, release store, schema home, policy home, contract home, generated artifact store, or public-truth surface.

---

## Attestation-tool rule

Attestation tools help prove integrity; they do not create truth by themselves.

| Expectation | Required posture |
|---|---|
| Explicit inputs | Helpers should receive paths, refs, digests, manifests, or receipt IDs explicitly. |
| No embedded secrets | Keys, credentials, tokens, and passphrases are never committed here. |
| Deterministic output | Verification results and bundle manifests should be reproducible from the same inputs. |
| Fail closed | Missing input, digest mismatch, signature failure, unsupported format, or stale attestation fails visibly. |
| Separate authority | A successful attestation check does not equal release approval, policy allow, evidence closure, or publication. |
| Auditable reason | Failure and success states should be machine-readable enough for CI and reviewers. |

---

## Expected helper families

| Family | Purpose | Status |
|---|---|---|
| `verify_digest` | Check a file, manifest, or receipt digest against an expected value. | PROPOSED. |
| `verify_signature` | Verify a signature or signing certificate chain using configured trust policy. | PROPOSED. |
| `bundle_attestation` | Package receipts, digests, signer metadata, and verification instructions. | PROPOSED. |
| `offline_verify_bundle` | Build or verify an offline bundle without network access. | PROPOSED. |
| `release_attestation_preflight` | Check release candidate attestation support before release review. | PROPOSED. |
| `ci_attestation_summary` | Emit a CI-readable summary for reviewer inspection. | PROPOSED. |

---

## Suggested layout

```text
tools/attest/
|-- README.md
|-- verify_digest.PROPOSED
|-- verify_signature.PROPOSED
|-- bundle_attestation.PROPOSED
|-- offline_verify_bundle.PROPOSED
|-- release_attestation_preflight.PROPOSED
`-- ci_attestation_summary.PROPOSED
```

The layout is schematic. Actual filenames, language, CLI shape, package manager, and CI wiring remain NEEDS VERIFICATION.

---

## Inputs and outputs

Accepted inputs:

- release manifests, receipt references, proof references, artifact digests, and expected signer metadata;
- local fixture or test paths for no-network verification;
- non-secret configuration templates or references by name.

Expected outputs:

- verification result objects;
- CI summaries;
- candidate attestation bundle manifests;
- reason codes suitable for release review or QA inspection.

Final receipt, proof, and release records belong in their owning roots, not in `tools/attest/`.

---

## Run posture

No executable command was verified while authoring this README.

```bash
: "PROPOSED / NEEDS VERIFICATION"
python -m tools.attest --help
```

Default checks should be local and no-network unless a specific release or security workflow explicitly enables a network-backed verification step.

---

## Maintenance checklist

- [ ] Keep secrets, private keys, credentials, and tokens out of this path.
- [ ] Keep generated receipts, proofs, and release records in their owning roots.
- [ ] Keep helper behavior deterministic and reviewable.
- [ ] Add tests before making any attestation helper release-gating.
- [ ] Document CLI inputs, outputs, exit codes, and failure reasons once implemented.
- [ ] Update `tools/README.md`, test lanes, and release docs if this lane becomes operational.

---

## Verification status

| Item | Status |
|---|---|
| Target README path | CONFIRMED; blank placeholder replaced. |
| Parent `tools/` boundary | CONFIRMED in `tools/README.md`. |
| `tools/attest/` placement | CONFIRMED as PROPOSED-to-create in `tools/README.md`. |
| Secret exclusion rule | CONFIRMED in `docs/security/SECRETS.md`. |
| Executable helper inventory | NEEDS VERIFICATION. |
| CLI shape and language/runtime | NEEDS VERIFICATION. |
| Signing backend and trust policy | NEEDS VERIFICATION. |
| Tests and CI wiring | NEEDS VERIFICATION. |
| Tests and validators | NOT RUN. |
