<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://fixture/domains/agriculture/no-network/readme
title: Agriculture no-network fixtures README
type: fixture-readme
version: v0.1.0
status: draft
owners: TODO(owner): agriculture domain steward; TODO(owner): fixture steward; TODO(owner): validation steward; TODO(owner): source steward; TODO(owner): policy steward; TODO(owner): docs steward
created: NEEDS VERIFICATION - blank file existed before 2026-07-01 expansion
updated: 2026-07-01
policy_label: public-review
related:
  - nass/README.md
  - ../nass_quickstats/README.md
  - ../catalog/README.md
  - ../golden/README.md
  - ../invalid/README.md
  - ../../../../docs/domains/agriculture/PIPELINE.md
  - ../../../../docs/domains/agriculture/CANONICAL_PATHS.md
  - ../../../../docs/domains/agriculture/DATA_LIFECYCLE.md
  - ../../../../policy/domains/agriculture/README.md
  - ../../../../contracts/domains/agriculture/
  - ../../../../schemas/contracts/v1/domains/agriculture/
  - ../../../../tests/domains/agriculture/
  - ../../../../docs/doctrine/directory-rules.md
tags: [kfm, fixtures, domains, agriculture, no-network, offline-fixtures, deterministic-tests, source-fixtures, catalog-fixtures, aggregate, non-authoritative]
notes:
  - "This README replaces a blank file at `fixtures/domains/agriculture/no_network/README.md`."
  - "This directory is the parent index for Agriculture fixtures that must run without network access."
  - "The currently confirmed child README is `nass/README.md`; broader no-network fixture coverage remains PARTIAL / NEEDS VERIFICATION."
  - "No-network fixtures are not live source downloads, source caches, source registry records, catalog authority, release approval, or publication authority."
  - "No tests, validators, network-isolation checks, source admission checks, catalog checks, policy checks, release checks, or CI jobs were run during this documentation update."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Agriculture no-network fixtures

Parent fixture lane for deterministic offline Agriculture examples under `fixtures/domains/agriculture/no_network/`.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: fixtures" src="https://img.shields.io/badge/root-fixtures%2F-6f42c1">
  <img alt="Domain: agriculture" src="https://img.shields.io/badge/domain-agriculture-success">
  <img alt="Lane: no network" src="https://img.shields.io/badge/lane-no__network-blue">
  <img alt="Inventory: partial" src="https://img.shields.io/badge/inventory-partial-orange">
  <img alt="Authority: fixture only" src="https://img.shields.io/badge/authority-fixture%20only-critical">
</p>

**Path:** `fixtures/domains/agriculture/no_network/README.md`  
**Fixture posture:** parent index for deterministic no-network Agriculture fixtures  
**Authority posture:** fixture only; source access, source registry posture, catalog truth, schema authority, policy authority, lifecycle promotion, release approval, and public layer authority remain in their owning roots  
**Quick links:** [Purpose](#purpose) · [Observed child lanes](#observed-child-lanes) · [Placement basis](#placement-basis) · [No-network contract](#no-network-contract) · [Authority boundary](#authority-boundary) · [Expected layout](#expected-layout) · [Maintenance checklist](#maintenance-checklist) · [Status notes](#status-notes) · [Evidence ledger](#evidence-ledger)

> [!IMPORTANT]
> Files under this directory are offline test fixtures. They are not live source downloads, source caches, SourceDescriptors, EvidenceBundles, canonical catalog records, PolicyDecisions, ReleaseManifests, review approval, release approval, or publication authority.

---

## Purpose

This directory groups Agriculture fixture lanes that must support deterministic tests without network access.

Use this parent lane when tests, validators, parsers, catalog helpers, source helpers, or policy helpers need stable local examples instead of reaching external systems. Offline fixtures should be small, synthetic or minimized, stable, and reviewable.

A passing no-network test proves only that code handled a local fixture as expected. It does not prove an external source was reached, a source head is current, rights were re-verified, a catalog record was promoted, or an output may be published.

---

## Observed child lanes

| Child lane | Role | Status |
|---|---|---|
| [`nass/`](nass/README.md) | Deterministic offline NASS-shaped fixtures. | CONFIRMED README / PAYLOAD INVENTORY NEEDS VERIFICATION |

Broader no-network coverage is not claimed here. Add new child lanes only when a real offline fixture need exists and the source/domain boundary is documented.

---

## Placement basis

Agriculture's canonical path guide includes `fixtures/domains/agriculture/` in the Agriculture responsibility-root lane fan. Agriculture pipeline docs also include `fixtures/domains/agriculture/` in the Agriculture pipeline-related path set.

The governed lifecycle remains separate from this fixture lane:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Real source capture belongs in governed source/lifecycle lanes after source admission. Real catalog records belong under governed catalog lanes after validation and promotion. Public use requires policy, release, citation, and rollback posture.

---

## No-network contract

No-network Agriculture fixtures should preserve these constraints:

| Rule | Fixture meaning |
|---|---|
| No external calls | Tests using this lane should not require a network request. |
| Deterministic content | Fixture payloads should be stable and reviewable. |
| Synthetic or minimized | Use the smallest public-safe sample needed for the test. |
| No credentials | Do not store API keys, tokens, cookies, or private headers. |
| No source-cache authority | A fixture is not a source cache or proof of source freshness. |
| No publication shortcut | Offline success does not authorize catalog promotion or public release. |

For aggregate source fixtures, preserve source-role semantics and do not normalize aggregate examples into exact field-level truth.

---

## Authority boundary

| Responsibility | Owning root | This README posture |
|---|---|---|
| Agriculture no-network fixtures | `fixtures/domains/agriculture/no_network/` | Indexes deterministic offline fixture lanes only. |
| Child offline fixture lanes | `fixtures/domains/agriculture/no_network/<source_or_family>/` | Documented by child READMEs. |
| Agriculture object meaning | `contracts/domains/agriculture/` | Referenced, not replaced. |
| Machine-checkable Agriculture shape | `schemas/contracts/v1/domains/agriculture/` | Referenced, not duplicated. |
| Agriculture policy | `policy/domains/agriculture/` | Out of scope; fixtures may test it but do not define it. |
| Source registry records | `data/registry/sources/` | Out of scope. |
| Canonical lifecycle data | `data/raw/`, `data/work/`, `data/quarantine/`, `data/processed/`, `data/catalog/`, `data/triplet/`, `data/published/` | Out of scope; do not duplicate as fixtures. |
| Tests and validation proof | `tests/domains/agriculture/` and validator tooling | Referenced, not claimed as run. |

Do not collapse this parent fixture lane into source access, source registry authority, source freshness proof, catalog authority, policy authority, release approval, or public-client permission.

---

## Expected layout

Use child directories for source- or family-specific offline fixtures:

```text
fixtures/domains/agriculture/no_network/
  README.md
  nass/
    README.md
    <case_name>.input.json
    <case_name>.expected.json
```

For schema-style examples inside a child lane, use:

```text
fixtures/domains/agriculture/no_network/<source_or_family>/
  valid/
    README.md
    valid_<n>.json
  invalid/
    README.md
    invalid_<n>.json
    invalid_<n>.expected_error.txt
```

For parser or helper snapshots, document the consuming test and whether the expected output represents a parsed source-shaped object, a denial, an abstention, an aggregation obligation, a citation obligation, or a safe aggregate response.

---

## Maintenance checklist

Before adding or changing no-network Agriculture fixtures:

- [ ] Confirm the consuming test, validator, parser, or helper script.
- [ ] Confirm that the test runs without a network request.
- [ ] Keep examples synthetic, compact, deterministic, public-safe, and reviewable.
- [ ] Preserve source-role, rights, sensitivity, review, receipt, release, citation, and EvidenceBundle expectations in fixture intent.
- [ ] Do not store credentials, full live source responses, source caches, release candidates, published layers, or release-blocked material.
- [ ] Keep child README files updated when adding source-specific offline lanes.
- [ ] Run the relevant no-network tests before claiming validation success.

---

## Status notes

| Item | Status | Notes |
|---|---:|---|
| Target README | CONFIRMED UPDATED | This path existed as a blank file before this update. |
| Observed child README | CONFIRMED | `nass/README.md` exists and documents deterministic offline NASS fixtures. |
| Broader no-network payload inventory | NEEDS VERIFICATION | Repo search did not surface additional confirmed no-network fixture payloads during this update. |
| No-network behavior | NEEDS VERIFICATION / NOT RUN | No test was executed to confirm network isolation. |
| Placement | CONFIRMED PATH / PROPOSED LANE REALIZATION | The requested path exists; Agriculture path doctrine includes `fixtures/domains/agriculture/` but marks Agriculture-specific lanes as proposed until verified. |
| Test execution | NOT RUN | No validators, pytest, source admission checks, catalog checks, policy checks, release checks, no-network checks, or CI were run during this README update. |

---

## Evidence ledger

| Source | Status | Supports | Limits |
|---|---|---|---|
| Previous target file | CONFIRMED | Target existed as a blank file. | Did not define no-network parent fixture guidance. |
| Repository search for no-network fixtures | CONFIRMED SEARCH / NO MATCH | No additional confirmed no-network payload file was found for this parent lane in this update. | Search is not a full recursive filesystem listing. |
| [`nass/README.md`](nass/README.md) | CONFIRMED | Child offline NASS fixture lane, no-network constraints, aggregate source-role boundary, accepted fixture material, and authority boundary. | Payload inventory and no-network execution remain NEEDS VERIFICATION there. |
| `../../../../docs/domains/agriculture/PIPELINE.md` | CONFIRMED DOC / PROPOSED WIRING | Agriculture pipeline path set includes fixtures, source/lifecycle data, registry, release, and non-publisher connector/watcher posture. | The file marks path-shaped claims as PROPOSED and was not executed. |
| `../../../../docs/domains/agriculture/CANONICAL_PATHS.md` | CONFIRMED DOC / PROPOSED PATH REALIZATION | Agriculture lane fan includes `fixtures/domains/agriculture/` and separates responsibility roots. | Agriculture-specific path realizations remain proposed until verified. |
| `../../../../docs/doctrine/directory-rules.md` | CONFIRMED doctrine | File placement encodes ownership/governance/lifecycle; `tests/` and `fixtures/` are validate/operate roots. | Specific fixture completeness requires inventory and tests. |

[Back to top](#top)
