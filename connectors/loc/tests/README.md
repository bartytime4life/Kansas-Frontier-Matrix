<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/connectors-loc-tests-readme
title: connectors/loc/tests/ — Library of Congress Connector Candidate Test Boundary
type: readme
version: v0.1
status: draft
owners: OWNER_TBD — Connector steward · Test steward · Source steward for LOC · Rights reviewer · Validation steward · Docs steward
created: 2026-06-19
updated: 2026-06-19
policy_label: public-doctrine; tests; connector-family-candidate; beyond-directory-rules-7-3; open-dsc-14; no-network-default; fixture-safe; no-publication
proposed_path: connectors/loc/tests/README.md
truth_posture: CONFIRMED path exists / PROPOSED beyond §7.3 connector-family test path / TEST INVENTORY NEEDS VERIFICATION
related:
  - ../README.md
  - ../../../docs/sources/catalog/loc/README.md
  - ../../../docs/sources/catalog/loc/loc-iiif-presentations.md
  - ../../../docs/sources/catalog/loc/loc-historic-maps.md
  - ../../../docs/sources/catalog/loc/lcnaf-name-authority.md
  - ../../../docs/sources/catalog/loc/lcsh-subject-headings.md
  - ../../../docs/sources/catalog/loc/chronicling-america.md
  - ../../../docs/sources/SOURCE_DESCRIPTOR_STANDARD.md
  - ../../../data/registry/sources/
  - ../../../fixtures/
  - ../../../schemas/contracts/v1/source/
  - ../../../policy/rights/
  - ../../../policy/sources/
  - ../../../release/
tags: [kfm, connectors, loc, library-of-congress, tests, lcnaf, lcsh, iiif, chronicling-america, maps, archives, linked-data, source-admission, no-network, fixtures, open-dsc-14, raw, quarantine, governance]
notes:
  - "This README replaces the greenfield stub in `connectors/loc/tests/`."
  - "The LOC catalog README says `connectors/loc/` is proposed beyond Directory Rules §7.3 and awaits OPEN-DSC-14 ADR ratification."
  - "Tests here should verify candidate-family and source-admission boundaries, not source activation, release approval, or implementation maturity."
  - "Default test posture is no-network and fixture-safe."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Library of Congress Connector Candidate Test Boundary

> Test-boundary README for `connectors/loc/tests/`. This path belongs to the proposed LOC connector-family candidate, which is beyond the nine Directory Rules §7.3 connector families until `OPEN-DSC-14` is resolved. Tests here protect source-admission behavior only; they do not ratify `loc/` as canonical infrastructure.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Family status: beyond §7.3" src="https://img.shields.io/badge/family-beyond__%C2%A77.3-orange">
  <img alt="Open item: OPEN-DSC-14" src="https://img.shields.io/badge/open-OPEN--DSC--14-orange">
  <img alt="Network: disabled by default" src="https://img.shields.io/badge/network-disabled__by__default-critical">
  <img alt="Fixtures: required" src="https://img.shields.io/badge/fixtures-required-blue">
</p>

> [!IMPORTANT]
> **Status:** `draft` connector-candidate test README · **Owner:** `OWNER_TBD`  
> **Path:** `connectors/loc/tests/README.md`  
> **Truth posture:** `CONFIRMED` file exists · `PROPOSED` beyond §7.3 test path · `NEEDS VERIFICATION` actual tests and CI wiring  
> **Boundary:** fixture-safe source-admission tests only; no live-network default, no source activation, no release approval, no canonical-family claim.

**Quick jumps:** [Scope](#scope) · [Repo fit](#repo-fit) · [Required test families](#required-test-families) · [Forbidden test behavior](#forbidden-test-behavior) · [Evidence ledger](#evidence-ledger) · [Validation matrix](#validation-matrix) · [Rollback](#rollback) · [Verification backlog](#verification-backlog)

---

## Scope

`connectors/loc/tests/` is a test-boundary lane for the proposed LOC connector-family candidate.

Tests here may validate that LOC source-admission remains SourceDescriptor-gated, no-network by default, fixture-safe, sub-source-aware, provenance-preserving, and RAW/QUARANTINE-only.

Tests here must not claim that LOC-derived records are public-safe, released, canonicalized, complete, or production-ready without downstream EvidenceBundle, policy, review, and release controls.

[Back to top ↑](#top)

---

## Repo fit

| Surface | Role | Status |
|---|---|---:|
| `connectors/loc/tests/` | LOC connector-candidate test path. | **CONFIRMED path / PROPOSED beyond §7.3** |
| `connectors/loc/README.md` | Parent LOC connector-family candidate README. | **CONFIRMED** |
| `docs/sources/catalog/loc/README.md` | LOC source-family catalog README. | **CONFIRMED** |
| `docs/sources/catalog/loc/loc-iiif-presentations.md` | LOC IIIF product/source page. | **CONFIRMED search result / NEEDS FILE REVIEW** |
| `docs/sources/catalog/loc/loc-historic-maps.md` | LOC historic maps product/source page. | **CONFIRMED search result / NEEDS FILE REVIEW** |
| `docs/sources/catalog/loc/lcnaf-name-authority.md` | LCNAF authority product/source page. | **CONFIRMED search result / NEEDS FILE REVIEW** |
| `docs/sources/catalog/loc/lcsh-subject-headings.md` | LCSH product/source page. | **CONFIRMED search result / NEEDS FILE REVIEW** |
| `docs/sources/catalog/loc/chronicling-america.md` | Chronicling America product/source page. | **CONFIRMED search result / NEEDS FILE REVIEW** |
| `fixtures/` | Candidate fixture root. | **NEEDS VERIFICATION for LOC fixtures** |
| `release/` | Release and publication controls. | **Out of scope for these tests** |

---

## Required test families

Expected test families before implementation maturity can be claimed:

1. **Candidate-family tests** — confirm `connectors/loc/` remains proposed beyond §7.3 until `OPEN-DSC-14` is resolved.
2. **SourceDescriptor gate tests** — connector code refuses activation without accepted descriptor and activation state.
3. **No-network default tests** — default test runs use fixtures and do not call live sources.
4. **Sub-source identity tests** — LOC surfaces remain distinguishable.
5. **Source-role tests** — source roles stay explicit and surface-specific.
6. **Rights-state tests** — unresolved rights state routes to quarantine or abstention.
7. **Provenance tests** — source URI, retrieval timestamp, source fingerprint, and derivation metadata are preserved where applicable.
8. **Uncertainty tests** — OCR, georeferencing, identity-link, and linked-data uncertainty remain explicit.
9. **RAW/QUARANTINE boundary tests** — connector code cannot write directly to processed, catalog, triplet, published, proof, receipt, or release stores.
10. **Release-denial tests** — connector output is not treated as a public release artifact.

---

## Forbidden test behavior

Tests under this path must not:

- require internet access by default;
- store credentials, cookies, session tokens, or restricted exports;
- assert release approval from connector behavior alone;
- collapse LOC sub-sources into each other or into generated summaries;
- write directly into processed, catalog, triplet, published, proof, receipt, or release roots;
- create a second schema, policy, source registry, fixture authority, proof authority, receipt authority, or release authority under `connectors/loc/tests/`.

---

## Evidence ledger

| Source | Status | Supports | Limits |
|---|---:|---|---|
| `connectors/loc/tests/README.md` | **CONFIRMED** | Target file existed as a greenfield stub before this update. | Does not prove tests exist or pass. |
| `connectors/loc/README.md` | **CONFIRMED** | Parent path is documented as proposed beyond §7.3 under OPEN-DSC-14. | Does not prove ADR resolution or implementation maturity. |
| `docs/sources/catalog/loc/README.md` | **CONFIRMED** | LOC catalog README says `connectors/loc/` is proposed beyond §7.3 and lists LOC sub-sources and admission concerns. | Does not prove endpoint availability, rights clearance, activation, or test coverage. |
| LOC per-sub-source catalog pages | **CONFIRMED search results / NEEDS FILE REVIEW** | Search found IIIF, maps, LCNAF, LCSH, and Chronicling America pages. | This README did not inspect each file body. |
| Actual test files | **NEEDS VERIFICATION** | This README defines required test posture. | Actual test inventory and CI status remain unverified. |

---

## Validation matrix

| Test concern | Expected result | Failure route |
|---|---|---|
| Candidate-family status | `connectors/loc/` remains proposed beyond §7.3 until ADR resolution. | Fail test; require OPEN-DSC-14 review. |
| SourceDescriptor | Missing descriptor blocks activation. | Fail closed. |
| Network | Default tests do not use live network. | Fail test. |
| Sub-source identity | LOC surfaces remain distinct. | Fail test. |
| Source role | Source role is explicit and surface-specific. | Fail closed. |
| Rights state | Unknown or unresolved state routes to quarantine/abstention. | Fail closed. |
| Provenance | Source URI, timestamp, and fingerprint are preserved where applicable. | Fail closed. |
| Uncertainty | OCR, map, identity, and linked-data uncertainty remain explicit. | Fail closed. |
| Lifecycle boundary | Connector output is RAW or QUARANTINE only. | Fail test. |
| Publication | No connector test treats output as released/public. | Fail test. |

---

## Rollback

Rollback is required if this README is used to claim test coverage, CI success, live-source access approval, canonical-family status, release approval, or policy authority without verified test evidence.

Rollback target:

```text
commit prior to this update: SHA_TBD_AFTER_GIT_HISTORY_CHECK
```

A safe rollback is to restore the prior greenfield stub or replace this file with a shorter connector-candidate test note until `OPEN-DSC-14` and test inventory are verified.

---

## Verification backlog

| Item | Status | Needed evidence |
|---|---:|---|
| Confirm actual test files under this path. | **NEEDS VERIFICATION** | Repo tree or mounted workspace. |
| Resolve `OPEN-DSC-14` for LOC connector-family placement. | **NEEDS VERIFICATION** | ADR or migration decision. |
| Confirm fixture root and fixture safety metadata. | **NEEDS VERIFICATION** | Fixture registry and test fixtures. |
| Confirm no-network default in CI. | **NEEDS VERIFICATION** | Workflow files and test logs. |
| Confirm SourceDescriptor and activation test coverage. | **NEEDS VERIFICATION** | Test code and registry fixtures. |
| Confirm provenance and uncertainty test coverage. | **NEEDS VERIFICATION** | Test code, fixtures, and expected failures. |

---

## Maintainer note

Use these tests to prevent connector-family drift, sub-source collapse, and release leakage. The tests should prove that `connectors/loc/` stays a governed candidate-family lane until ADR and implementation evidence say otherwise.

[Back to top ↑](#top)
