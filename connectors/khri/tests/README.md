<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/connectors-khri-tests-readme
title: connectors/khri/tests/ — KHRI Compatibility Test Boundary
type: readme
version: v0.1
status: draft
owners: OWNER_TBD — Connector steward · Test steward · Kansas source steward · KSHS/archives liaison · Archaeology steward · Settlements steward · Rights reviewer · Sensitivity reviewer · Validation steward · Docs steward
created: 2026-06-19
updated: 2026-06-19
policy_label: public-doctrine; tests; compatibility-lane; noncanonical-path; no-network-default; fixture-safe; sensitivity-gated; no-publication
proposed_path: connectors/khri/tests/README.md
truth_posture: CONFIRMED path exists / NONCANONICAL compatibility test README / TEST INVENTORY NEEDS VERIFICATION
related:
  - ../README.md
  - ../../kansas/README.md
  - ../../kansas/khri/README.md
  - ../../../docs/sources/catalog/kansas/khri.md
  - ../../../docs/sources/catalog/kansas/kansas-state-archives.md
  - ../../../docs/domains/archaeology/README.md
  - ../../../docs/domains/settlements-infrastructure/README.md
  - ../../../docs/domains/people-dna-land/README.md
  - ../../../docs/sources/SOURCE_DESCRIPTOR_STANDARD.md
  - ../../../data/registry/sources/
  - ../../../fixtures/
  - ../../../schemas/contracts/v1/source/
  - ../../../policy/sensitivity/
  - ../../../policy/rights/
  - ../../../release/
tags: [kfm, connectors, khri, tests, kshs, kansas, historic-resources, archaeology, settlements, cultural-resources, compatibility, source-admission, no-network, fixtures, quarantine, governance]
notes:
  - "This README replaces the greenfield stub in the top-level KHRI compatibility test path."
  - "The KHRI source dossier says the correct connector path was already `connectors/kansas/khri/`; this top-level test path is therefore compatibility-only."
  - "Tests here should verify source-admission boundaries, not public release, public cultural-resource claims, or policy decisions."
  - "Default test posture is no-network and fixture-safe. Live-source tests require explicit source-steward review and must be excluded from default CI unless approved."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# KHRI Compatibility Test Boundary

> Test-boundary README for `connectors/khri/tests/`. This folder exists under a noncanonical top-level KHRI compatibility connector path. Tests here should protect migration and source-admission behavior only; canonical implementation and long-term tests should converge under `connectors/kansas/khri/` unless an ADR says otherwise.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Canonicality: noncanonical test path" src="https://img.shields.io/badge/canonicality-noncanonical__test__path-orange">
  <img alt="Network: disabled by default" src="https://img.shields.io/badge/network-disabled__by__default-critical">
  <img alt="Fixtures: required" src="https://img.shields.io/badge/fixtures-required-blue">
  <img alt="Lifecycle: RAW or QUARANTINE only" src="https://img.shields.io/badge/lifecycle-RAW%20%7C%20QUARANTINE%20only-orange">
</p>

> [!IMPORTANT]
> **Status:** `draft` compatibility test README · **Owner:** `OWNER_TBD`  
> **Path:** `connectors/khri/tests/README.md`  
> **Truth posture:** `CONFIRMED` file exists · `NONCANONICAL` compatibility test path · `NEEDS VERIFICATION` actual tests and CI wiring  
> **Boundary:** fixture-safe source-admission tests only; no live-network default, no release approval, no public cultural-resource claim.

**Quick jumps:** [Scope](#scope) · [Repo fit](#repo-fit) · [Required test families](#required-test-families) · [Forbidden test behavior](#forbidden-test-behavior) · [Fixture posture](#fixture-posture) · [Evidence ledger](#evidence-ledger) · [Validation matrix](#validation-matrix) · [Rollback](#rollback) · [Verification backlog](#verification-backlog)

---

## Scope

`connectors/khri/tests/` is a compatibility test lane for the existing top-level `connectors/khri/` path.

Tests here may validate that the compatibility path remains constrained, source-role-aware, rights-aware, sensitivity-aware, no-network by default, fixture-safe, and RAW/QUARANTINE-only.

Tests here must not claim that KHRI records are public-safe, released, canonicalized, complete, or fit for public cultural-resource, archaeology, parcel, person, eligibility, designation, or planning use.

[Back to top ↑](#top)

---

## Repo fit

| Surface | Role | Status |
|---|---|---:|
| `connectors/khri/tests/` | Existing top-level compatibility test path. | **CONFIRMED path / NONCANONICAL** |
| `connectors/khri/README.md` | Parent compatibility README. | **CONFIRMED** |
| `connectors/kansas/khri/` | Canonical KHRI connector path named by source dossier. | **CONFIRMED by source dossier / NEEDS VERIFICATION implementation depth** |
| `docs/sources/catalog/kansas/khri.md` | KHRI per-surface source dossier. | **CONFIRMED** |
| `docs/sources/catalog/kansas/kansas-state-archives.md` | KSHS umbrella source-family brief. | **CONFIRMED** |
| `fixtures/` | Candidate fixture root. | **NEEDS VERIFICATION for KHRI fixtures** |
| `policy/rights/`, `policy/sensitivity/` | Rights and sensitivity authority. | **Outside connector tests** |
| `release/` | Release and publication controls. | **Out of scope for these tests** |

---

## Required test families

The following test families are expected before implementation maturity can be claimed:

1. **Path compatibility tests** — confirm the top-level `connectors/khri/` lane does not present itself as canonical.
2. **SourceDescriptor gate tests** — connector code refuses activation without accepted descriptor and activation state.
3. **No-network default tests** — default test runs use fixtures and do not call live KHRI/KSHS surfaces.
4. **Surface-identity tests** — KHRI remains distinct from Kansas Memory, KSHS State Archives proper, county society holdings, GNIS, parcel/person records, and generated summaries.
5. **Source-role tests** — administrative/authority/source-role fields are explicit and not collapsed.
6. **Rights and sensitivity tests** — unresolved rights or sensitivity state routes to quarantine or abstention.
7. **Geometry precision tests** — geometry precision and uncertainty are preserved and cannot be silently upgraded.
8. **RAW/QUARANTINE boundary tests** — connector code cannot write directly to processed, catalog, triplet, published, proof, receipt, or release stores.
9. **Release-denial tests** — tests assert that connector output is not a public release artifact.
10. **Migration-safety tests** — compatibility path points toward `connectors/kansas/khri/` without creating a parallel authority.

---

## Forbidden test behavior

Tests under this path must not:

- require internet access by default;
- store credentials, cookies, session tokens, or private source exports;
- publish or expose precise sensitive cultural-resource locations;
- assert release approval from connector behavior alone;
- treat KHRI records as parcel/person, ownership, eligibility, designation, archaeology, or public planning truth without downstream evidence and review;
- collapse KHRI into Kansas Memory, KSHS State Archives proper, GNIS, parcel datasets, archaeology records, or generated summaries;
- write directly into processed, catalog, triplet, published, proof, receipt, or release roots;
- create a second schema, policy, source registry, fixture authority, or release authority under `connectors/khri/tests/`.

---

## Fixture posture

Fixtures for KHRI tests should be:

- minimized;
- synthetic or redacted where cultural-resource sensitivity may apply;
- stripped of unnecessary owner/person/parcel details;
- explicit about source role, surface identity, geometry precision, review state, rights state, sensitivity state, and source vintage;
- stored in a governed fixture root once verified;
- paired with fixture README or metadata explaining why the sample is safe for tests.

When fixture safety is unclear, tests should assert quarantine or abstention behavior rather than carrying forward unsafe examples.

---

## Evidence ledger

| Source | Status | Supports | Limits |
|---|---:|---|---|
| `connectors/khri/tests/README.md` | **CONFIRMED** | Target file existed as a greenfield stub before this update. | Does not prove tests exist or pass. |
| `connectors/khri/README.md` | **CONFIRMED** | Parent path is documented as noncanonical compatibility lane. | Does not prove canonical migration status. |
| `docs/sources/catalog/kansas/khri.md` | **CONFIRMED** | KHRI dossier says canonical connector path is `connectors/kansas/khri/` and frames KHRI as a KSHS-operated per-surface product page. | Does not prove endpoint availability, rights clearance, activation, or test coverage. |
| `docs/sources/catalog/kansas/kansas-state-archives.md` | **CONFIRMED** | KSHS umbrella brief says umbrella posture does not replace KHRI per-surface descriptors. | Does not define KHRI-specific test behavior alone. |
| Actual test files | **NEEDS VERIFICATION** | This README defines required test posture. | Actual test inventory and CI status remain unverified. |

---

## Validation matrix

| Test concern | Expected result | Failure route |
|---|---|---|
| Canonicality | `connectors/khri/` remains compatibility-only. | Fail test; require migration/ADR review. |
| SourceDescriptor | Missing descriptor blocks activation. | Fail closed. |
| Network | Default tests do not use live network. | Fail test. |
| Surface identity | KHRI remains distinct from sibling KSHS surfaces and peer authorities. | Fail test. |
| Rights/sensitivity | Unknown or unresolved state routes to quarantine/abstention. | Fail closed. |
| Geometry precision | Precision and uncertainty are preserved. | Fail closed. |
| Lifecycle boundary | Connector output is RAW or QUARANTINE only. | Fail test. |
| Publication | No connector test treats output as released/public. | Fail test. |

---

## Rollback

Rollback is required if this README is used to claim test coverage, CI success, live-source access approval, canonical path status, release approval, public cultural-resource safety, or policy authority without verified test evidence.

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
| Confirm canonical KHRI test home. | **NEEDS VERIFICATION** | Directory Rules, ADR, migration note, or repo convention. |
| Confirm KHRI fixture root and fixture safety metadata. | **NEEDS VERIFICATION** | Fixture registry and test fixtures. |
| Confirm no-network default in CI. | **NEEDS VERIFICATION** | Workflow files and test logs. |
| Confirm SourceDescriptor and activation test coverage. | **NEEDS VERIFICATION** | Test code and registry fixtures. |
| Confirm rights/sensitivity and geometry precision test coverage. | **NEEDS VERIFICATION** | Test code, policy fixtures, and expected failures. |
| Confirm migration plan for top-level path. | **NEEDS VERIFICATION** | ADR or migration note. |

---

## Maintainer note

Use these tests to prevent trust-boundary drift. The tests should prove that KHRI connector behavior stays constrained until source descriptors, rights, sensitivity, EvidenceBundle closure, review state, and release state are all available through governed channels.

[Back to top ↑](#top)
