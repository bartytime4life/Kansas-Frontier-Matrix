<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/connectors-local-upload-tests-readme
title: connectors/local_upload/tests/ — Local Upload Connector Test Boundary
type: readme
version: v0.1
status: draft
owners: OWNER_TBD — Connector steward · Test steward · Source-intake steward · Rights reviewer · Sensitivity reviewer · Validation steward · Docs steward
created: 2026-06-19
updated: 2026-06-19
policy_label: public-doctrine; tests; connector-family; directory-rules-7-3; local-upload; no-network-default; fixture-safe; deny-by-default; quarantine-first; no-publication
proposed_path: connectors/local_upload/tests/README.md
truth_posture: CONFIRMED path exists / CONFIRMED doctrine-level §7.3 connector-family test path / TEST INVENTORY NEEDS VERIFICATION
related:
  - ../README.md
  - ../../../docs/sources/catalog/local_upload/README.md
  - ../../../docs/sources/catalog/local_upload.md
  - ../../../docs/sources/catalog/local_upload/user-file-upload.md
  - ../../../docs/sources/SOURCE_DESCRIPTOR_STANDARD.md
  - ../../../docs/doctrine/directory-rules.md
  - ../../../docs/doctrine/trust-membrane.md
  - ../../../docs/doctrine/lifecycle-law.md
  - ../../../docs/adr/ADR-0012-connector-outputs-to-data-raw-or-data-quarantine-only.md
  - ../../../data/registry/sources/
  - ../../../data/raw/
  - ../../../data/quarantine/
  - ../../../fixtures/
  - ../../../schemas/contracts/v1/source/
  - ../../../policy/sources/local_upload/
  - ../../../policy/sensitivity/
  - ../../../policy/rights/
  - ../../../release/
tags: [kfm, connectors, local-upload, local_upload, tests, intake, source-admission, no-network, fixtures, raw, quarantine, rights, sensitivity, provenance, governance]
notes:
  - "This README replaces the greenfield stub in `connectors/local_upload/tests/`."
  - "The local-upload source catalog states that `connectors/local_upload/` is named in Directory Rules §7.3 and is a highest-uncertainty trust-edge intake lane."
  - "Tests here should verify source-admission and lifecycle boundaries, not release approval or implementation maturity."
  - "Default test posture is no-network and fixture-safe."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Local Upload Connector Test Boundary

> Test-boundary README for `connectors/local_upload/tests/`. This folder tests the governed local-upload connector lane, where user-supplied material enters KFM as candidate evidence only. Tests here must protect trust-edge admission, deny-by-default posture, SourceDescriptor gates, and RAW/QUARANTINE-only handoff.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Directory Rules: §7.3 connector" src="https://img.shields.io/badge/directory__rules-%C2%A77.3__connector-success">
  <img alt="Network: disabled by default" src="https://img.shields.io/badge/network-disabled__by__default-critical">
  <img alt="Fixtures: required" src="https://img.shields.io/badge/fixtures-required-blue">
  <img alt="Lifecycle: RAW or QUARANTINE only" src="https://img.shields.io/badge/lifecycle-RAW%20%7C%20QUARANTINE%20only-orange">
</p>

> [!IMPORTANT]
> **Status:** `draft` connector test README · **Owner:** `OWNER_TBD`  
> **Path:** `connectors/local_upload/tests/README.md`  
> **Truth posture:** `CONFIRMED` file exists · `CONFIRMED` doctrine-level §7.3 connector-family test path · `NEEDS VERIFICATION` actual tests and CI wiring  
> **Boundary:** fixture-safe source-admission tests only; no live-network default, no release approval, no source-role upgrade, no public claim.

**Quick jumps:** [Scope](#scope) · [Repo fit](#repo-fit) · [Required test families](#required-test-families) · [Forbidden test behavior](#forbidden-test-behavior) · [Fixture posture](#fixture-posture) · [Evidence ledger](#evidence-ledger) · [Validation matrix](#validation-matrix) · [Rollback](#rollback) · [Verification backlog](#verification-backlog)

---

## Scope

`connectors/local_upload/tests/` is the test lane for the local-upload connector.

Tests here may verify that local uploads remain candidate material until governed review, that descriptors and policy gates are required, and that connector outputs remain limited to RAW or QUARANTINE handoff.

Tests here must not claim that upload-derived records are public-safe, released, authoritative, complete, or production-ready without downstream EvidenceBundle, policy, review, and release controls.

[Back to top ↑](#top)

---

## Repo fit

| Surface | Role | Status |
|---|---|---:|
| `connectors/local_upload/tests/` | Local-upload connector test path. | **CONFIRMED path / NEEDS VERIFICATION test inventory** |
| `connectors/local_upload/README.md` | Parent local-upload connector README. | **CONFIRMED** |
| `docs/sources/catalog/local_upload/README.md` | Local-upload source catalog entry. | **CONFIRMED** |
| `docs/sources/catalog/local_upload/user-file-upload.md` | Product/surface-level upload profile. | **CONFIRMED search result / NEEDS FILE REVIEW** |
| `fixtures/` | Candidate fixture root. | **NEEDS VERIFICATION for local-upload fixtures** |
| `data/raw/` and `data/quarantine/` | Allowed connector handoff targets. | **Outside connector tests** |
| `release/` | Release and publication controls. | **Out of scope for these tests** |

---

## Required test families

Expected test families before implementation maturity can be claimed:

1. **Descriptor gate tests** — uploads cannot become activated source records without a SourceDescriptor and review state.
2. **Candidate-role tests** — the default source role remains candidate until steward review changes it.
3. **No-network default tests** — default tests use local fixtures and do not require network access.
4. **Content-classification tests** — file handling uses content and metadata checks, not filename extension alone.
5. **Rights-state tests** — unresolved rights state routes to quarantine or abstention.
6. **Sensitivity-state tests** — unresolved or high-risk sensitivity state routes to quarantine, redaction, generalization, staged access, or denial.
7. **Provenance tests** — upload event, source fingerprint, and review metadata are preserved where applicable.
8. **Quarantine-reason tests** — failed admission produces auditable reasons.
9. **RAW/QUARANTINE boundary tests** — connector code cannot write directly to processed, catalog, triplet, published, proof, receipt, or release stores.
10. **Release-denial tests** — connector output is not treated as a public release artifact.

---

## Forbidden test behavior

Tests under this path must not:

- require internet access by default;
- rely on sensitive real-world upload examples where synthetic or minimized fixtures are sufficient;
- store credentials, tokens, or private material;
- assert release approval from connector behavior alone;
- write directly into processed, catalog, triplet, published, proof, receipt, or release roots;
- create a second schema, policy, source registry, fixture authority, proof authority, receipt authority, or release authority under `connectors/local_upload/tests/`.

---

## Fixture posture

Fixtures for local-upload tests should be:

- minimized;
- synthetic or redacted where practical;
- explicit about file class, source role, rights state, sensitivity state, source fingerprint, and expected disposition;
- stored in a governed fixture root once verified;
- paired with fixture metadata explaining why the sample is safe for tests.

When fixture safety is unclear, tests should assert quarantine or abstention behavior rather than carrying forward unsafe examples.

---

## Evidence ledger

| Source | Status | Supports | Limits |
|---|---:|---|---|
| `connectors/local_upload/tests/README.md` | **CONFIRMED** | Target file existed as a greenfield stub before this update. | Does not prove tests exist or pass. |
| `connectors/local_upload/README.md` | **CONFIRMED** | Parent path is documented as a §7.3 local-upload connector family. | Does not prove implementation maturity. |
| `docs/sources/catalog/local_upload/README.md` | **CONFIRMED** | Catalog defines local upload as highest-uncertainty trust-edge intake with deny-by-default posture and RAW/QUARANTINE handling. | Does not prove endpoint, fixture, or test coverage. |
| Actual test files | **NEEDS VERIFICATION** | This README defines required test posture. | Actual test inventory and CI status remain unverified. |

---

## Validation matrix

| Test concern | Expected result | Failure route |
|---|---|---|
| SourceDescriptor | Missing descriptor blocks activation. | Fail closed. |
| Source role | Default role remains candidate. | Fail closed. |
| Network | Default tests do not use live network. | Fail test. |
| Content classification | Classification is content- and metadata-aware. | Fail closed. |
| Rights state | Unknown or unresolved state routes to quarantine/abstention. | Fail closed. |
| Sensitivity state | Unresolved risk routes to governed safe outcome. | Fail closed. |
| Provenance | Upload event and fingerprint are preserved where applicable. | Fail closed. |
| Lifecycle boundary | Connector output is RAW or QUARANTINE only. | Fail test. |
| Publication | No connector test treats output as released/public. | Fail test. |

---

## Rollback

Rollback is required if this README is used to claim test coverage, CI success, release approval, source-role upgrade, public visibility, or policy authority without verified test evidence.

Rollback target:

```text
commit prior to this update: SHA_TBD_AFTER_GIT_HISTORY_CHECK
```

A safe rollback is to restore the prior greenfield stub or replace this file with a shorter test-boundary note until test inventory and fixture posture are verified.

---

## Verification backlog

| Item | Status | Needed evidence |
|---|---:|---|
| Confirm actual test files under this path. | **NEEDS VERIFICATION** | Repo tree or mounted workspace. |
| Confirm fixture root and fixture safety metadata. | **NEEDS VERIFICATION** | Fixture registry and test fixtures. |
| Confirm no-network default in CI. | **NEEDS VERIFICATION** | Workflow files and test logs. |
| Confirm SourceDescriptor and candidate-role test coverage. | **NEEDS VERIFICATION** | Test code and registry fixtures. |
| Confirm rights/sensitivity and quarantine-reason test coverage. | **NEEDS VERIFICATION** | Test code, policy fixtures, and expected failures. |
| Confirm RAW/QUARANTINE handoff checks. | **NEEDS VERIFICATION** | Test code and ADR-linked fixtures. |

---

## Maintainer note

Use these tests to keep local upload conservative. The test suite should prove that user-supplied material stays behind the trust membrane until descriptor, policy, review, and release evidence permit downstream use.

[Back to top ↑](#top)
