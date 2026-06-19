<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/connectors-ksgs-tests-readme
title: connectors/ksgs/tests/ — KSGS Slug Compatibility Test Boundary
type: readme
version: v0.1
status: draft
owners: OWNER_TBD — Connector steward · Test steward · Kansas source steward · Geology steward · Hydrology steward · Rights reviewer · Sensitivity reviewer · Validation steward · Docs steward
created: 2026-06-19
updated: 2026-06-19
policy_label: public-doctrine; tests; compatibility-lane; noncanonical-path; slug-compatibility; no-network-default; fixture-safe; no-publication
proposed_path: connectors/ksgs/tests/README.md
truth_posture: CONFIRMED path exists / NONCANONICAL compatibility test README / TEST INVENTORY NEEDS VERIFICATION
related:
  - ../README.md
  - ../../kgs/README.md
  - ../../kansas/README.md
  - ../../kansas/kgs/README.md
  - ../../../docs/sources/catalog/kansas/ksgs.md
  - ../../../docs/domains/geology/README.md
  - ../../../docs/domains/hydrology/README.md
  - ../../../docs/sources/SOURCE_DESCRIPTOR_STANDARD.md
  - ../../../data/registry/sources/
  - ../../../fixtures/
  - ../../../schemas/contracts/v1/source/
  - ../../../policy/sensitivity/
  - ../../../policy/rights/
  - ../../../release/
tags: [kfm, connectors, ksgs, kgs, tests, geology, hydrology, slug-compatibility, source-admission, no-network, fixtures, raw, quarantine, governance]
notes:
  - "This README replaces the greenfield stub in the top-level KSGS slug-compatibility test path."
  - "The KGS source profile preserves the `ksgs.md` catalog slug while canonical connector work belongs under `connectors/kansas/kgs/`."
  - "Tests here should verify compatibility and admission boundaries, not public release, source activation, or implementation maturity."
  - "Default test posture is no-network and fixture-safe."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# KSGS Slug Compatibility Test Boundary

> Test-boundary README for `connectors/ksgs/tests/`. This folder exists under a noncanonical top-level KSGS slug-compatibility connector path. Tests here should protect slug/canonical-path separation and source-admission behavior only; canonical implementation and long-term tests should converge under `connectors/kansas/kgs/` unless an ADR says otherwise.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Canonicality: noncanonical test path" src="https://img.shields.io/badge/canonicality-noncanonical__test__path-orange">
  <img alt="Slug: ksgs preserved" src="https://img.shields.io/badge/slug-ksgs__preserved-blue">
  <img alt="Network: disabled by default" src="https://img.shields.io/badge/network-disabled__by__default-critical">
  <img alt="Fixtures: required" src="https://img.shields.io/badge/fixtures-required-blue">
</p>

> [!IMPORTANT]
> **Status:** `draft` compatibility test README · **Owner:** `OWNER_TBD`  
> **Path:** `connectors/ksgs/tests/README.md`  
> **Truth posture:** `CONFIRMED` file exists · `NONCANONICAL` compatibility test path · `NEEDS VERIFICATION` actual tests and CI wiring  
> **Boundary:** fixture-safe source-admission tests only; no live-network default, no source activation, no release approval, no public claim.

**Quick jumps:** [Scope](#scope) · [Repo fit](#repo-fit) · [Required test families](#required-test-families) · [Forbidden test behavior](#forbidden-test-behavior) · [Fixture posture](#fixture-posture) · [Evidence ledger](#evidence-ledger) · [Validation matrix](#validation-matrix) · [Rollback](#rollback) · [Verification backlog](#verification-backlog)

---

## Scope

`connectors/ksgs/tests/` is a compatibility test lane for the existing top-level `connectors/ksgs/` path.

Tests here may validate that the compatibility path remains constrained, source-role-aware, rights-aware, sensitivity-aware, no-network by default, fixture-safe, and RAW/QUARANTINE-only.

Tests here must not claim that KGS-derived records are public-safe, released, canonicalized, complete, or fit for production use without downstream EvidenceBundle, policy, review, and release controls.

[Back to top ↑](#top)

---

## Repo fit

| Surface | Role | Status |
|---|---|---:|
| `connectors/ksgs/tests/` | Existing top-level slug-compatibility test path. | **CONFIRMED path / NONCANONICAL** |
| `connectors/ksgs/README.md` | Parent slug-compatibility README. | **CONFIRMED** |
| `connectors/kgs/README.md` | Sibling top-level KGS compatibility README. | **CONFIRMED** |
| `connectors/kansas/kgs/` | Canonical KGS connector path named by source profile. | **CONFIRMED by source profile / NEEDS VERIFICATION implementation depth** |
| `docs/sources/catalog/kansas/ksgs.md` | KGS source catalog entry using preserved slug. | **CONFIRMED** |
| `fixtures/` | Candidate fixture root. | **NEEDS VERIFICATION for KGS fixtures** |
| `policy/rights/`, `policy/sensitivity/` | Rights and sensitivity authority. | **Outside connector tests** |
| `release/` | Release and publication controls. | **Out of scope for these tests** |

---

## Required test families

The following test families are expected before implementation maturity can be claimed:

1. **Path compatibility tests** — confirm the top-level `connectors/ksgs/` lane does not present itself as canonical.
2. **Slug separation tests** — confirm `ksgs.md` catalog slug and `connectors/kansas/kgs/` canonical connector path remain distinct until an ADR resolves OPEN-KSGS-13.
3. **SourceDescriptor gate tests** — connector code refuses activation without accepted descriptor and activation state.
4. **No-network default tests** — default test runs use fixtures and do not call live sources.
5. **Sub-product identity tests** — KGS data/maps, surficial, oil/gas, WWC5, LAS, and Geoportal-derived material remain distinguishable.
6. **Source-role tests** — source-role fields are explicit and not collapsed.
7. **Rights and sensitivity tests** — unresolved rights or sensitivity state routes to quarantine or abstention.
8. **Geometry and scale tests** — geometry, precision, scale, depth, or datum context is preserved when relevant.
9. **RAW/QUARANTINE boundary tests** — connector code cannot write directly to processed, catalog, triplet, published, proof, receipt, or release stores.
10. **Release-denial tests** — tests assert that connector output is not a public release artifact.

---

## Forbidden test behavior

Tests under this path must not:

- require internet access by default;
- store credentials, cookies, session tokens, or private source exports;
- assert release approval from connector behavior alone;
- collapse KGS sub-products into each other or into peer-source records;
- write directly into processed, catalog, triplet, published, proof, receipt, or release roots;
- create a second schema, policy, source registry, fixture authority, or release authority under `connectors/ksgs/tests/`.

---

## Fixture posture

Fixtures for KSGS compatibility tests should be:

- minimized;
- synthetic or redacted where practical;
- explicit about source role, sub-product identity, geometry/scale/depth context, rights state, sensitivity state, and source vintage;
- stored in a governed fixture root once verified;
- paired with fixture README or metadata explaining why the sample is safe for tests.

When fixture safety is unclear, tests should assert quarantine or abstention behavior rather than carrying forward unsafe examples.

---

## Evidence ledger

| Source | Status | Supports | Limits |
|---|---:|---|---|
| `connectors/ksgs/tests/README.md` | **CONFIRMED** | Target file existed as a greenfield stub before this update. | Does not prove tests exist or pass. |
| `connectors/ksgs/README.md` | **CONFIRMED** | Parent path is documented as noncanonical slug-compatibility lane. | Does not prove canonical migration status. |
| `docs/sources/catalog/kansas/ksgs.md` | **CONFIRMED** | KGS source profile preserves the `ksgs` slug, confirms canonical connector path `connectors/kansas/kgs/`, and defers slug reconciliation to OPEN-KSGS-13. | Does not prove endpoint availability, rights clearance, activation, or test coverage. |
| Actual test files | **NEEDS VERIFICATION** | This README defines required test posture. | Actual test inventory and CI status remain unverified. |

---

## Validation matrix

| Test concern | Expected result | Failure route |
|---|---|---|
| Canonicality | `connectors/ksgs/` remains compatibility-only. | Fail test; require migration/ADR review. |
| Slug separation | `ksgs.md` and `kgs/` distinction is explicit. | Fail test; require OPEN-KSGS-13 handling. |
| SourceDescriptor | Missing descriptor blocks activation. | Fail closed. |
| Network | Default tests do not use live network. | Fail test. |
| Source role | Role is explicit and sub-product-specific. | Fail closed. |
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
| Confirm canonical KGS test home. | **NEEDS VERIFICATION** | Directory Rules, ADR, migration note, or repo convention. |
| Confirm fixture root and fixture safety metadata. | **NEEDS VERIFICATION** | Fixture registry and test fixtures. |
| Confirm no-network default in CI. | **NEEDS VERIFICATION** | Workflow files and test logs. |
| Confirm SourceDescriptor and activation test coverage. | **NEEDS VERIFICATION** | Test code and registry fixtures. |
| Confirm rights/sensitivity and geometry/scale/depth test coverage. | **NEEDS VERIFICATION** | Test code, policy fixtures, and expected failures. |
| Confirm migration plan for top-level `ksgs` path. | **NEEDS VERIFICATION** | ADR or migration note. |

---

## Maintainer note

Use these tests to prevent slug and authority drift. The tests should prove that `connectors/ksgs/` stays a compatibility lane until the repo explicitly resolves whether the preserved `ksgs` slug should remain separate from canonical `connectors/kansas/kgs/`.

[Back to top ↑](#top)
