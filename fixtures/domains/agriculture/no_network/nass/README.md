<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://fixture/domains/agriculture/no-network/nass/readme
title: Agriculture no-network NASS fixtures README
type: fixture-readme
version: v0.1.0
status: draft
owners: TODO(owner): agriculture domain steward; TODO(owner): source steward; TODO(owner): fixture steward; TODO(owner): validation steward; TODO(owner): policy steward; TODO(owner): docs steward
created: NEEDS VERIFICATION - blank file existed before 2026-07-01 expansion
updated: 2026-07-01
policy_label: public-review
related:
  - ../../nass_quickstats/README.md
  - ../../catalog/README.md
  - ../../golden/README.md
  - ../../invalid/README.md
  - ../../../../../docs/sources/catalog/usda/usda-nass-quickstats.md
  - ../../../../../docs/domains/agriculture/PIPELINE.md
  - ../../../../../docs/domains/agriculture/CANONICAL_PATHS.md
  - ../../../../../docs/domains/agriculture/DATA_LIFECYCLE.md
  - ../../../../../policy/domains/agriculture/README.md
  - ../../../../../contracts/domains/agriculture/
  - ../../../../../schemas/contracts/v1/domains/agriculture/
  - ../../../../../tests/domains/agriculture/
  - ../../../../../docs/doctrine/directory-rules.md
tags: [kfm, fixtures, domains, agriculture, no-network, offline-fixtures, nass, quickstats, usda, aggregate, source-role, anti-collapse, deterministic-tests, non-authoritative]
notes:
  - "This README replaces a blank file at `fixtures/domains/agriculture/no_network/nass/README.md`."
  - "This directory is for deterministic no-network NASS fixtures only; it is not a live downloader, source registry, source cache, or canonical catalog lane."
  - "Repo search did not surface confirmed payload files in this directory during this update, so fixture inventory remains NEEDS VERIFICATION."
  - "NASS QuickStats fixture handling must preserve aggregate source-role semantics and avoid field-level anti-collapse violations."
  - "No tests, validators, network calls, source admission checks, catalog checks, policy checks, release checks, or CI jobs were run during this documentation update."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Agriculture no-network NASS fixtures

Offline fixture lane for NASS-shaped Agriculture examples under `fixtures/domains/agriculture/no_network/nass/`.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: fixtures" src="https://img.shields.io/badge/root-fixtures%2F-6f42c1">
  <img alt="Domain: agriculture" src="https://img.shields.io/badge/domain-agriculture-success">
  <img alt="Lane: no network" src="https://img.shields.io/badge/lane-no__network-blue">
  <img alt="Source: NASS" src="https://img.shields.io/badge/source-NASS-orange">
  <img alt="Authority: fixture only" src="https://img.shields.io/badge/authority-fixture%20only-critical">
</p>

**Path:** `fixtures/domains/agriculture/no_network/nass/README.md`  
**Fixture posture:** deterministic no-network Agriculture/NASS fixture lane  
**Authority posture:** fixture only; source access, source registry posture, catalog truth, schema authority, policy authority, lifecycle promotion, release approval, and public layer authority remain in their owning roots  
**Quick links:** [Purpose](#purpose) · [Placement basis](#placement-basis) · [No-network contract](#no-network-contract) · [NASS source-role boundary](#nass-source-role-boundary) · [Accepted fixture material](#accepted-fixture-material) · [Authority boundary](#authority-boundary) · [Expected layout](#expected-layout) · [Maintenance checklist](#maintenance-checklist) · [Status notes](#status-notes) · [Evidence ledger](#evidence-ledger)

> [!IMPORTANT]
> Files under this directory are offline test fixtures. They are not live NASS downloads, source caches, SourceDescriptors, EvidenceBundles, canonical catalog records, PolicyDecisions, ReleaseManifests, review approval, release approval, or publication authority.

---

## Purpose

This directory is for NASS-shaped Agriculture fixtures that must run without network access.

Use this lane when tests, validators, parsers, catalog helpers, or policy helpers need deterministic NASS-like inputs without reaching an external service. Offline fixtures should be small, synthetic or minimized, and stable enough for repeatable test runs.

A passing no-network test proves only that code handles the fixture as expected. It does not prove a NASS endpoint was reached, a source head is current, a statistic is current, rights were re-verified, or an output may be published.

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

No-network NASS fixtures should support offline tests with these constraints:

| Rule | Fixture meaning |
|---|---|
| No external calls | Tests using this lane should not require a network request. |
| Deterministic content | Fixture payloads should be stable and reviewable. |
| Synthetic or minimized | Use the smallest public-safe sample needed for the test. |
| No credentials | Do not store API keys, tokens, cookies, or private headers. |
| No source-cache authority | A fixture is not a source cache or proof of source freshness. |
| No publication shortcut | Offline success does not authorize catalog promotion or public release. |

---

## NASS source-role boundary

The sibling `nass_quickstats` fixture README and the QuickStats source catalog page document QuickStats as aggregate source-role data. No-network fixtures in this lane should preserve that posture.

| Rule | Fixture consequence |
|---|---|
| NASS QuickStats is aggregate-shaped | Fixtures should represent aggregate cells or aggregate-shaped metadata. |
| Aggregate is not field observation | Negative fixtures should cover attempts to use an aggregate as exact field truth. |
| Aggregation unit matters | Include county/state/year or another aggregation unit when relevant. |
| Promotion-like output needs support | Expected outputs that resemble promoted records should include aggregation/citation/evidence expectations. |
| Public exact exposure fails closed | No-network tests should not normalize aggregate data into exact public claims. |

---

## Accepted fixture material

This directory may contain:

| Material | Use |
|---|---|
| `*.input.json` | Small synthetic NASS-shaped input payloads for offline tests. |
| `*.expected.json` | Expected aggregate-safe output for deterministic helpers. |
| `*.snapshot.json` | Snapshot-style expected output for no-network parser or policy tests. |
| `valid/valid_<n>.json` | Positive schema examples when a schema or validator is wired. |
| `invalid/invalid_<n>.json` | Negative examples for source-role collapse, unsupported exposure posture, missing aggregation support, or missing citation/evidence posture. |
| `invalid/invalid_<n>.expected_error.txt` | Expected validation or policy reason text for negative examples. |
| local README files | Fixture intent, inventory, and authority-boundary documentation. |

Do not store live source dumps, full external responses, private joins, credentials, release candidates, published layers, or source-system side-effect records here.

---

## Authority boundary

| Responsibility | Owning root | This README posture |
|---|---|---|
| Offline NASS fixtures | `fixtures/domains/agriculture/no_network/nass/` | Documents deterministic test inputs only. |
| NASS QuickStats fixture lane | `fixtures/domains/agriculture/nass_quickstats/` | Sibling source-shaped fixture lane. |
| QuickStats source catalog documentation | `docs/sources/catalog/usda/usda-nass-quickstats.md` | Referenced, not replaced. |
| Source registry records | `data/registry/sources/` | Out of scope. |
| Agriculture object meaning | `contracts/domains/agriculture/` | Referenced, not replaced. |
| Machine-checkable Agriculture shape | `schemas/contracts/v1/domains/agriculture/` | Referenced, not duplicated. |
| Agriculture policy | `policy/domains/agriculture/` | Out of scope; fixtures may test it but do not define it. |
| Canonical lifecycle data | `data/raw/`, `data/work/`, `data/quarantine/`, `data/processed/`, `data/catalog/`, `data/triplet/`, `data/published/` | Out of scope; do not duplicate as fixtures. |
| Tests and validation proof | `tests/domains/agriculture/` and validator tooling | Referenced, not claimed as run. |

Do not collapse this fixture lane into source access, source registry authority, source freshness proof, catalog authority, policy authority, release approval, or public-client permission.

---

## Expected layout

Use the smallest structure that matches the actual test need:

```text
fixtures/domains/agriculture/no_network/nass/
  README.md
  <case_name>.input.json
  <case_name>.expected.json
  <case_name>.snapshot.json
```

For schema-style examples, use:

```text
fixtures/domains/agriculture/no_network/nass/
  valid/
    README.md
    valid_<n>.json
  invalid/
    README.md
    invalid_<n>.json
    invalid_<n>.expected_error.txt
```

For parser or helper snapshots, document the consuming test and whether the expected output represents a parsed aggregate cell, a denial, an abstention, an aggregation obligation, a citation obligation, or a safe aggregate response.

---

## Maintenance checklist

Before adding or changing no-network NASS fixtures:

- [ ] Confirm the consuming test, validator, parser, or helper script.
- [ ] Confirm that the test runs without a network request.
- [ ] Preserve aggregate source-role semantics.
- [ ] Include aggregation unit and period when the fixture represents a QuickStats-like cell.
- [ ] Keep examples synthetic, compact, deterministic, public-safe, and reviewable.
- [ ] Do not store credentials, full live source responses, private joins, release candidates, published layers, or release-blocked material.
- [ ] Preserve source-role, rights, sensitivity, review, receipt, release, citation, and EvidenceBundle expectations in fixture intent.
- [ ] Update this README when fixtures, validators, schemas, policy tests, parser tests, or helper scripts are added.
- [ ] Run the relevant no-network tests before claiming validation success.

---

## Status notes

| Item | Status | Notes |
|---|---:|---|
| Target README | CONFIRMED UPDATED | This path existed as a blank file before this update. |
| Direct payload inventory | NEEDS VERIFICATION | Repo search did not surface confirmed payload files in this directory during this update. |
| No-network behavior | NEEDS VERIFICATION / NOT RUN | No test was executed to confirm network isolation. |
| QuickStats source-role basis | CONFIRMED DOC | The sibling fixture README and source catalog page document QuickStats as aggregate source-role data with anti-collapse constraints. |
| Placement | CONFIRMED PATH / PROPOSED LANE REALIZATION | The requested path exists; Agriculture path doctrine includes `fixtures/domains/agriculture/` but marks Agriculture-specific lanes as proposed until verified. |
| Test execution | NOT RUN | No validators, pytest, source admission checks, catalog checks, policy checks, release checks, no-network checks, or CI were run during this README update. |

---

## Evidence ledger

| Source | Status | Supports | Limits |
|---|---|---|---|
| Previous target file | CONFIRMED | Target existed as a blank file. | Did not define no-network NASS fixture guidance. |
| Repository search for no-network NASS fixtures | CONFIRMED SEARCH / NO MATCH | No confirmed payload file was found for this directory in this update. | Search is not a full recursive filesystem listing. |
| `../../nass_quickstats/README.md` | CONFIRMED | Sibling NASS QuickStats fixture lane, aggregate source-role boundary, accepted fixture material, and authority boundary. | Payload inventory is also NEEDS VERIFICATION there. |
| `../../../../../docs/sources/catalog/usda/usda-nass-quickstats.md` | CONFIRMED DOC | QuickStats aggregate source-role, anti-collapse posture, aggregation receipt, geometry-scope guard, and field-level denial rules. | Endpoint, cadence specifics, rights status, and source registry record remain NEEDS VERIFICATION in that doc. |
| `../../../../../docs/domains/agriculture/PIPELINE.md` | CONFIRMED DOC / PROPOSED WIRING | Agriculture pipeline path set includes fixtures, source/lifecycle data, registry, release, and non-publisher connector/watcher posture. | The file marks path-shaped claims as PROPOSED and was not executed. |
| `../../../../../docs/doctrine/directory-rules.md` | CONFIRMED doctrine | File placement encodes ownership/governance/lifecycle; `tests/` and `fixtures/` are validate/operate roots. | Specific fixture completeness requires inventory and tests. |

[Back to top](#top)
