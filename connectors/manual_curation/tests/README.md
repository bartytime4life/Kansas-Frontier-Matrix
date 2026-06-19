<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/connectors-manual-curation-tests-readme
title: connectors/manual_curation/tests/ — Manual Curation Connector Test Boundary
type: readme
version: v0.1
status: draft
owners: OWNER_TBD — Connector steward · Test steward · Source steward · Docs steward · Validation steward · Rights reviewer · Sensitivity reviewer
created: 2026-06-19
updated: 2026-06-19
policy_label: public-doctrine; tests; manual-curation; steward-assisted; no-network-default; fixture-safe; no-publication; implementation-depth-needs-verification
proposed_path: connectors/manual_curation/tests/README.md
truth_posture: CONFIRMED path exists / PROPOSED connector test boundary / TEST INVENTORY NEEDS VERIFICATION
related:
  - ../README.md
  - ../../../docs/sources/catalog/manual_curation/README.md
  - ../../../docs/sources/catalog/manual_curation/steward-curation-workflow.md
  - ../../../docs/sources/SOURCE_DESCRIPTOR_STANDARD.md
  - ../../../docs/sources/source-roles.md
  - ../../../docs/doctrine/directory-rules.md
  - ../../../docs/doctrine/trust-membrane.md
  - ../../../docs/doctrine/lifecycle-law.md
  - ../../../docs/doctrine/truth-posture.md
  - ../../../docs/governance/separation-of-duties.md
  - ../../../data/registry/sources/
  - ../../../data/raw/
  - ../../../data/quarantine/
  - ../../../fixtures/
  - ../../../schemas/contracts/v1/source/
  - ../../../policy/sources/
  - ../../../policy/sensitivity/
  - ../../../policy/rights/
  - ../../../release/
tags: [kfm, connectors, manual-curation, tests, source-admission, steward-review, source-descriptor, source-role, quarantine, validation, evidencebundle, catalog-closure, governance]
notes:
  - "This README replaces the greenfield stub in `connectors/manual_curation/tests/`."
  - "The manual-curation catalog README states it is methodology and steward reference, not implementation proof."
  - "Tests here should verify steward-gate and source-admission boundaries, not release approval or implementation maturity."
  - "Default test posture is no-network and fixture-safe."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Manual Curation Connector Test Boundary

> Test-boundary README for `connectors/manual_curation/tests/`. This path tests steward-assisted manual-curation helper behavior only. Tests here must not imply source activation, source-role upgrade, catalog closure, release approval, or public visibility.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Truth: test inventory needs verification" src="https://img.shields.io/badge/truth-test__inventory__needs__verification-orange">
  <img alt="Network: disabled by default" src="https://img.shields.io/badge/network-disabled__by__default-critical">
  <img alt="Fixtures: required" src="https://img.shields.io/badge/fixtures-required-blue">
  <img alt="Lifecycle: RAW or QUARANTINE only" src="https://img.shields.io/badge/lifecycle-RAW%20%7C%20QUARANTINE%20only-orange">
</p>

> [!IMPORTANT]
> **Status:** `draft` connector test README · **Owner:** `OWNER_TBD`  
> **Path:** `connectors/manual_curation/tests/README.md`  
> **Truth posture:** `CONFIRMED` file exists · `PROPOSED` test boundary · `NEEDS VERIFICATION` actual tests and CI wiring  
> **Boundary:** fixture-safe steward-gate tests only; no source activation, no source-role upgrade, no catalog closure, no release approval.

**Quick jumps:** [Scope](#scope) · [Repo fit](#repo-fit) · [Required test families](#required-test-families) · [Forbidden test behavior](#forbidden-test-behavior) · [Fixture posture](#fixture-posture) · [Evidence ledger](#evidence-ledger) · [Validation matrix](#validation-matrix) · [Rollback](#rollback) · [Verification backlog](#verification-backlog)

---

## Scope

`connectors/manual_curation/tests/` is the test lane for the proposed manual-curation connector/helper boundary.

Tests here may verify that helper code preserves steward-review gates, source-role separation, rights and sensitivity routing, evidence references, validation defects, correction handoff notes, rollback handoff notes, and RAW/QUARANTINE-only output behavior.

Tests here must not claim that curated records are released, catalog-closed, authoritative, or production-ready without downstream EvidenceBundle, policy, review, catalog, release, correction, and rollback controls.

[Back to top ↑](#top)

---

## Repo fit

| Surface | Role | Status |
|---|---|---:|
| `connectors/manual_curation/tests/` | Manual-curation helper test path. | **CONFIRMED path / NEEDS VERIFICATION test inventory** |
| `connectors/manual_curation/README.md` | Parent manual-curation connector-boundary README. | **CONFIRMED** |
| `docs/sources/catalog/manual_curation/README.md` | Manual-curation methodology and steward reference. | **CONFIRMED** |
| `docs/sources/catalog/manual_curation/steward-curation-workflow.md` | Steward workflow reference. | **CONFIRMED search result / NEEDS FILE REVIEW** |
| `fixtures/` | Candidate fixture root. | **NEEDS VERIFICATION for manual-curation fixtures** |
| `data/raw/` and `data/quarantine/` | Candidate handoff targets. | **Outside connector tests** |
| `release/` | Release and publication controls. | **Out of scope for these tests** |

---

## Required test families

Expected test families before implementation maturity can be claimed:

1. **Descriptor-reference tests** — helper outputs include SourceDescriptor or descriptor-draft references where required.
2. **Activation-denial tests** — helper code does not approve source activation.
3. **Source-role tests** — helper code preserves explicit source role and does not upgrade role by convenience.
4. **Rights-state tests** — unresolved rights state routes to quarantine, review, or abstention.
5. **Sensitivity-state tests** — unresolved sensitivity state routes to a governed safe outcome.
6. **Evidence-reference tests** — helper code preserves evidence references without treating summaries as proof.
7. **Validation-defect tests** — validation problems remain visible with auditable reasons.
8. **Correction/rollback tests** — correction and rollback handoff notes remain explicit when applicable.
9. **RAW/QUARANTINE boundary tests** — helper code cannot write directly to processed, catalog, triplet, published, proof, receipt, or release stores.
10. **Release-denial tests** — helper output is not treated as catalog closure or public release.

---

## Forbidden test behavior

Tests under this path must not:

- require internet access by default;
- claim source activation from helper output alone;
- claim source-role upgrade from helper output alone;
- treat AI or watcher output as approval;
- write directly into processed, catalog, triplet, published, proof, receipt, or release roots;
- create a second schema, policy, source registry, fixture authority, proof authority, receipt authority, or release authority under `connectors/manual_curation/tests/`.

---

## Fixture posture

Fixtures for manual-curation tests should be:

- minimized;
- synthetic or redacted where practical;
- explicit about source role, rights state, sensitivity state, evidence references, review state, and expected disposition;
- stored in a governed fixture root once verified;
- paired with fixture metadata explaining why the sample is safe for tests.

When fixture safety is unclear, tests should assert quarantine, review routing, or abstention behavior.

---

## Evidence ledger

| Source | Status | Supports | Limits |
|---|---:|---|---|
| `connectors/manual_curation/tests/README.md` | **CONFIRMED** | Target file existed as a greenfield stub before this update. | Does not prove tests exist or pass. |
| `connectors/manual_curation/README.md` | **CONFIRMED** | Parent README defines the helper boundary and forbids activation, source-role upgrade, catalog closure, and publication. | Does not prove implementation maturity. |
| `docs/sources/catalog/manual_curation/README.md` | **CONFIRMED** | Manual curation is steward-led methodology, not implementation proof. | Exact workflow implementation and tooling remain unverified. |
| Actual test files | **NEEDS VERIFICATION** | This README defines required test posture. | Actual test inventory and CI status remain unverified. |

---

## Validation matrix

| Test concern | Expected result | Failure route |
|---|---|---|
| SourceDescriptor reference | Required descriptor reference is present or routed for review. | Fail closed. |
| Activation | Helper output does not approve activation. | Fail test. |
| Source role | Source role remains explicit and not convenience-upgraded. | Fail closed. |
| Rights state | Unknown or unresolved state routes to review/quarantine/abstention. | Fail closed. |
| Sensitivity state | Unresolved risk routes to governed safe outcome. | Fail closed. |
| Evidence references | Evidence refs are preserved; summaries are not proof. | Fail closed. |
| Lifecycle boundary | Output is RAW or QUARANTINE handoff only. | Fail test. |
| Publication | No helper test treats output as catalog-closed or released. | Fail test. |

---

## Rollback

Rollback is required if this README is used to claim test coverage, CI success, source activation, source-role upgrade, catalog closure, release approval, or policy authority without verified test evidence.

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
| Confirm SourceDescriptor and source-role test coverage. | **NEEDS VERIFICATION** | Test code and registry fixtures. |
| Confirm rights/sensitivity and review-routing test coverage. | **NEEDS VERIFICATION** | Test code, policy fixtures, and expected failures. |
| Confirm RAW/QUARANTINE handoff checks. | **NEEDS VERIFICATION** | Test code and contract fixtures. |

---

## Maintainer note

Use these tests to keep manual curation as a gate-preserving helper lane. The test suite should prove that steward review remains visible and that helper output never becomes release approval.

[Back to top ↑](#top)
