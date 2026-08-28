<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/connectors-ksu-research-extension-tests-readme
title: connectors/ksu_research_extension/tests/ — KSU Research and Extension Compatibility Test Boundary
type: readme
version: v0.1
status: draft
owners: OWNER_TBD — Connector steward · Test steward · Kansas source steward · Agriculture steward · Weather steward · Soil steward · Rights reviewer · Sensitivity reviewer · Validation steward · Docs steward
created: 2026-06-19
updated: 2026-06-19
policy_label: public-doctrine; tests; compatibility-lane; noncanonical-path; snake-case-compatibility; no-network-default; fixture-safe; no-publication
proposed_path: connectors/ksu_research_extension/tests/README.md
truth_posture: CONFIRMED path exists / NONCANONICAL compatibility test README / TEST INVENTORY NEEDS VERIFICATION
related:
  - ../README.md
  - ../../kansas/README.md
  - ../../../docs/sources/catalog/kansas/ksu-research-extension.md
  - ../../../docs/sources/catalog/kansas/kansas-mesonet.md
  - ../../../docs/domains/agriculture/README.md
  - ../../../docs/domains/weather-atmospheric/README.md
  - ../../../docs/domains/soil/README.md
  - ../../../docs/sources/SOURCE_DESCRIPTOR_STANDARD.md
  - ../../../data/registry/sources/
  - ../../../fixtures/
  - ../../../schemas/contracts/v1/source/
  - ../../../policy/sensitivity/
  - ../../../policy/rights/
  - ../../../release/
tags: [kfm, connectors, ksu, k-state, research-extension, tests, agriculture, weather, soil, compatibility, source-admission, no-network, fixtures, raw, quarantine, governance]
notes:
  - "This README replaces the greenfield stub in the top-level KSU R&E compatibility test path."
  - "The KSU R&E source profile says v0.2 normalizes canonical connector placement to `connectors/kansas/ksu-research-extension/`."
  - "Tests here should verify compatibility and source-admission boundaries, not source activation, release approval, or implementation maturity."
  - "Default test posture is no-network and fixture-safe."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# KSU Research and Extension Compatibility Test Boundary

> Test-boundary README for `connectors/ksu_research_extension/tests/`. This folder exists under a noncanonical top-level snake_case compatibility connector path. Tests here should protect migration and source-admission behavior only; canonical implementation and long-term tests should converge under `connectors/kansas/ksu-research-extension/` unless an ADR says otherwise.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Canonicality: noncanonical test path" src="https://img.shields.io/badge/canonicality-noncanonical__test__path-orange">
  <img alt="Network: disabled by default" src="https://img.shields.io/badge/network-disabled__by__default-critical">
  <img alt="Fixtures: required" src="https://img.shields.io/badge/fixtures-required-blue">
</p>

> [!IMPORTANT]
> **Status:** `draft` compatibility test README · **Owner:** `OWNER_TBD`  
> **Path:** `connectors/ksu_research_extension/tests/README.md`  
> **Truth posture:** `CONFIRMED` file exists · `NONCANONICAL` compatibility test path · `NEEDS VERIFICATION` actual tests and CI wiring  
> **Boundary:** fixture-safe source-admission tests only; no live-network default, no source activation, no release approval, no public claim.

**Quick jumps:** [Scope](#scope) · [Repo fit](#repo-fit) · [Required test families](#required-test-families) · [Forbidden test behavior](#forbidden-test-behavior) · [Fixture posture](#fixture-posture) · [Evidence ledger](#evidence-ledger) · [Validation matrix](#validation-matrix) · [Rollback](#rollback) · [Verification backlog](#verification-backlog)

---

## Scope

`connectors/ksu_research_extension/tests/` is a compatibility test lane for the existing top-level `connectors/ksu_research_extension/` path.

Tests here may validate that the compatibility path remains constrained, source-role-aware, rights-aware, no-network by default, fixture-safe, and RAW/QUARANTINE-only.

Tests here must not claim that KSU R&E-derived records are public-safe, released, canonicalized, complete, or fit for production use without downstream EvidenceBundle, policy, review, and release controls.

[Back to top ↑](#top)

---

## Repo fit

| Surface | Role | Status |
|---|---|---:|
| `connectors/ksu_research_extension/tests/` | Existing top-level snake_case compatibility test path. | **CONFIRMED path / NONCANONICAL** |
| `connectors/ksu_research_extension/README.md` | Parent compatibility README. | **CONFIRMED** |
| `connectors/kansas/ksu-research-extension/` | Canonical KSU R&E connector path named by source profile. | **CONFIRMED by source profile / NEEDS VERIFICATION implementation depth** |
| `docs/sources/catalog/kansas/ksu-research-extension.md` | KSU R&E umbrella source profile. | **CONFIRMED** |
| `docs/sources/catalog/kansas/kansas-mesonet.md` | Kansas Mesonet sibling per-surface product page. | **CONFIRMED** |
| `fixtures/` | Candidate fixture root. | **NEEDS VERIFICATION for KSU R&E fixtures** |
| `policy/rights/`, `policy/sensitivity/` | Rights and sensitivity authority. | **Outside connector tests** |
| `release/` | Release and publication controls. | **Out of scope for these tests** |

---

## Required test families

The following test families are expected before implementation maturity can be claimed:

1. **Path compatibility tests** — confirm the top-level `connectors/ksu_research_extension/` lane does not present itself as canonical.
2. **Canonical redirect tests** — confirm long-term placement points toward `connectors/kansas/ksu-research-extension/`.
3. **SourceDescriptor gate tests** — connector code refuses activation without accepted descriptor and activation state.
4. **No-network default tests** — default test runs use fixtures and do not call live sources.
5. **Umbrella-versus-surface tests** — KSU R&E remains an umbrella source brief and Kansas Mesonet remains a sibling per-surface product page.
6. **Source-role tests** — product-level source-role fields are explicit and not collapsed.
7. **Rights and sensitivity tests** — unresolved rights or sensitivity state routes to quarantine or abstention.
8. **Freshness and cadence tests** — product cadence and freshness metadata are preserved where applicable.
9. **RAW/QUARANTINE boundary tests** — connector code cannot write directly to processed, catalog, triplet, published, proof, receipt, or release stores.
10. **Release-denial tests** — tests assert that connector output is not a public release artifact.

---

## Forbidden test behavior

Tests under this path must not:

- require internet access by default;
- store credentials, cookies, session tokens, or private source exports;
- assert release approval from connector behavior alone;
- collapse KSU R&E umbrella material into Mesonet, peer Kansas sources, or generated summaries;
- write directly into processed, catalog, triplet, published, proof, receipt, or release roots;
- create a second schema, policy, source registry, fixture authority, or release authority under `connectors/ksu_research_extension/tests/`.

---

## Fixture posture

Fixtures for KSU R&E compatibility tests should be:

- minimized;
- synthetic or redacted where practical;
- explicit about source role, product identity, cadence/freshness, rights state, sensitivity state, and source vintage;
- stored in a governed fixture root once verified;
- paired with fixture README or metadata explaining why the sample is safe for tests.

When fixture safety is unclear, tests should assert quarantine or abstention behavior rather than carrying forward unsafe examples.

---

## Evidence ledger

| Source | Status | Supports | Limits |
|---|---:|---|---|
| `connectors/ksu_research_extension/tests/README.md` | **CONFIRMED** | Target file existed as a greenfield stub before this update. | Does not prove tests exist or pass. |
| `connectors/ksu_research_extension/README.md` | **CONFIRMED** | Parent path is documented as noncanonical snake_case compatibility lane. | Does not prove canonical migration status. |
| `docs/sources/catalog/kansas/ksu-research-extension.md` | **CONFIRMED** | Source profile says the canonical Kansas family placement was already correct and v0.2 normalizes the slug to `connectors/kansas/ksu-research-extension/`; it also frames KSU R&E as an umbrella source brief. | Does not prove endpoint availability, rights clearance, activation, or test coverage. |
| `docs/sources/catalog/kansas/kansas-mesonet.md` | **CONFIRMED** | Kansas Mesonet is treated as a sibling per-surface product page with its own admission posture. | Does not replace the KSU R&E umbrella profile. |
| Actual test files | **NEEDS VERIFICATION** | This README defines required test posture. | Actual test inventory and CI status remain unverified. |

---

## Validation matrix

| Test concern | Expected result | Failure route |
|---|---|---|
| Canonicality | `connectors/ksu_research_extension/` remains compatibility-only. | Fail test; require migration/ADR review. |
| Canonical placement | Canonical work points to `connectors/kansas/ksu-research-extension/`. | Fail test; require placement review. |
| SourceDescriptor | Missing descriptor blocks activation. | Fail closed. |
| Network | Default tests do not use live network. | Fail test. |
| Umbrella/surface split | KSU R&E and Kansas Mesonet remain distinct surfaces. | Fail test. |
| Source role | Product-level source role is explicit. | Fail closed. |
| Rights/sensitivity | Unknown or unresolved state routes to quarantine/abstention. | Fail closed. |
| Lifecycle boundary | Connector output is RAW or QUARANTINE only. | Fail test. |
| Publication | No connector test treats output as released/public. | Fail test. |

---

## Rollback

Rollback is required if this README is used to claim test coverage, CI success, live-source access approval, canonical path status, release approval, or policy authority without verified test evidence.

Rollback target:

```text
commit prior to this update: SHA_TBD_AFTER_GIT_HISTORY_CHECK
```

A safe rollback is to restore the prior greenfield stub or replace this file with a shorter compatibility-test note until canonical placement and test inventory are verified.

---

## Verification backlog

| Item | Status | Needed evidence |
|---|---:|---|
| Confirm actual test files under this path. | **NEEDS VERIFICATION** | Repo tree or mounted workspace. |
| Confirm canonical KSU R&E test home. | **NEEDS VERIFICATION** | Directory Rules, ADR, migration note, or repo convention. |
| Confirm fixture root and fixture safety metadata. | **NEEDS VERIFICATION** | Fixture registry and test fixtures. |
| Confirm no-network default in CI. | **NEEDS VERIFICATION** | Workflow files and test logs. |
| Confirm SourceDescriptor and activation test coverage. | **NEEDS VERIFICATION** | Test code and registry fixtures. |
| Confirm rights/sensitivity and cadence/freshness test coverage. | **NEEDS VERIFICATION** | Test code, policy fixtures, and expected failures. |
| Confirm migration plan for top-level snake_case path. | **NEEDS VERIFICATION** | ADR or migration note. |

---

## Maintainer note

Use these tests to prevent path, source-role, and umbrella/surface drift. The tests should prove that `connectors/ksu_research_extension/` stays a compatibility lane until the repo explicitly migrates or preserves the path by ADR.

[Back to top ↑](#top)
