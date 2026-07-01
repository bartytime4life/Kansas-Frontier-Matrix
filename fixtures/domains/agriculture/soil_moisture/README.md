<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://fixture/domains/agriculture/soil-moisture/readme
title: Agriculture soil moisture fixtures README
type: fixture-readme
version: v0.1.0
status: draft
owners: TODO(owner): agriculture domain steward; TODO(owner): soil domain steward; TODO(owner): source steward; TODO(owner): fixture steward; TODO(owner): validation steward; TODO(owner): policy steward; TODO(owner): docs steward
created: NEEDS VERIFICATION - blank file existed before 2026-07-01 expansion
updated: 2026-07-01
policy_label: public-review
related:
  - ../catalog/README.md
  - ../golden/README.md
  - ../invalid/README.md
  - ../hls_vi/README.md
  - ../../../../docs/domains/agriculture/SOURCES.md
  - ../../../../docs/sources/catalog/nrcs/scan-soil-climate.md
  - ../../../../docs/domains/agriculture/PIPELINE.md
  - ../../../../docs/domains/agriculture/CANONICAL_PATHS.md
  - ../../../../docs/domains/agriculture/DATA_LIFECYCLE.md
  - ../../../../contracts/domains/agriculture/
  - ../../../../contracts/domains/soil/
  - ../../../../schemas/contracts/v1/domains/agriculture/
  - ../../../../policy/domains/agriculture/
  - ../../../../tests/domains/agriculture/
  - ../../../../docs/doctrine/directory-rules.md
tags: [kfm, fixtures, domains, agriculture, soil-moisture, station-time-series, mesonet, scan, uscrn, smap, source-role, observed, modeled, aggregate, non-authoritative]
notes:
  - "This README replaces a blank file at `fixtures/domains/agriculture/soil_moisture/README.md`."
  - "This directory is for Agriculture soil-moisture-shaped fixtures only, not canonical Soil-domain records, source registry records, station truth, or published layer authority."
  - "Repo evidence identifies Mesonet, SCAN, and USCRN as observed station-series sources and SMAP Level-3/4 as modeled soil-moisture context; fixture examples must preserve those source-role distinctions."
  - "No direct fixture payloads were found or inspected in this directory during this update, so payload inventory remains NEEDS VERIFICATION."
  - "No tests, validators, source admission checks, catalog checks, policy checks, release checks, or CI jobs were run during this documentation update."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Agriculture soil moisture fixtures

Fixture lane for Agriculture soil-moisture-shaped examples under `fixtures/domains/agriculture/soil_moisture/`.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: fixtures" src="https://img.shields.io/badge/root-fixtures%2F-6f42c1">
  <img alt="Domain: agriculture" src="https://img.shields.io/badge/domain-agriculture-success">
  <img alt="Lane: soil moisture" src="https://img.shields.io/badge/lane-soil__moisture-blue">
  <img alt="Source role: preserve" src="https://img.shields.io/badge/source__role-preserve-orange">
  <img alt="Authority: fixture only" src="https://img.shields.io/badge/authority-fixture%20only-critical">
</p>

**Path:** `fixtures/domains/agriculture/soil_moisture/README.md`  
**Fixture posture:** Agriculture-domain soil-moisture fixture lane  
**Authority posture:** fixture only; source registry posture, Soil-domain authority, Hydrology-domain authority, station truth, schema authority, policy authority, lifecycle promotion, release approval, and public layer authority remain in their owning roots  
**Quick links:** [Purpose](#purpose) · [Placement basis](#placement-basis) · [Source-role boundary](#source-role-boundary) · [Accepted fixture material](#accepted-fixture-material) · [Authority boundary](#authority-boundary) · [Expected layout](#expected-layout) · [Maintenance checklist](#maintenance-checklist) · [Status notes](#status-notes) · [Evidence ledger](#evidence-ledger)

> [!IMPORTANT]
> Files under this directory are test inputs or expected-output examples. They are not live station readings, source registry records, SourceDescriptors, EvidenceBundles, canonical Soil-domain records, Agriculture catalog records, PolicyDecisions, ReleaseManifests, review approval, release approval, or publication authority.

---

## Purpose

This directory is for small, public-safe Agriculture soil-moisture fixtures.

Use this lane when Agriculture tests, validators, catalog helpers, stress-indicator helpers, suitability helpers, or policy helpers need soil-moisture-shaped examples without reading live stations, source payloads, lifecycle stores, catalog records, or published layers.

A passing fixture proves only the bounded test expectation for that fixture. It does not prove a sensor reading is current, a station is active, a satellite product is current, a source endpoint was reached, rights were re-verified, or an output may be published.

---

## Placement basis

Agriculture's canonical path guide includes `fixtures/domains/agriculture/` in the Agriculture responsibility-root lane fan. Agriculture source guidance names soil-moisture-related sources as part of the Agriculture source context while preserving cross-domain ownership and source-role discipline.

The governed lifecycle remains separate from this fixture lane:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Real source capture belongs in governed source/lifecycle lanes after source admission. Real catalog records belong under governed catalog lanes after validation and promotion. Public use requires policy, release, citation, and rollback posture.

---

## Source-role boundary

Soil-moisture examples can be easy to collapse because station measurements, modeled satellite products, and aggregated summaries all look similar downstream. Fixtures in this lane must preserve the source role they are testing.

| Source-shaped example | Expected source-role posture | Fixture consequence |
|---|---|---|
| Kansas Mesonet soil-moisture station reading | `observed` station-series context | Preserve station, depth, time, QA, and citation fields when modeled in fixtures. |
| NRCS SCAN soil-moisture reading | `observed` station-series context | Preserve station/time/depth semantics and do not turn a watcher signal into published truth. |
| NOAA USCRN soil/climate reading | `observed` station-series context | Preserve station-series semantics and review domain ownership before Agriculture use. |
| NASA SMAP Level-3/4 soil moisture | `modeled` derived surface | Preserve model/product identity, uncertainty, time, and source role; do not label as observed. |
| Downscaled or period summary | `aggregate` or modeled-plus-aggregate, depending on contract | Include aggregation support, scale, time scope, and evidence/citation expectations. |

When a fixture crosses into Soil or Hydrology semantics, the owning domain must remain visible. Agriculture may cite soil-moisture context for suitability or stress interpretation, but the fixture lane does not re-own canonical soil or water meaning.

---

## Accepted fixture material

This directory may contain:

| Material | Use |
|---|---|
| `*.input.json` | Small synthetic soil-moisture-shaped input examples. |
| `*.expected.json` | Expected aggregate-safe or helper output for deterministic tests. |
| `*.snapshot.json` | Snapshot-style expected output for parser, catalog, stress, suitability, or policy tests. |
| `valid/valid_<n>.json` | Positive schema examples when a schema or validator is wired. |
| `invalid/invalid_<n>.json` | Negative examples for source-role collapse, missing depth/time/QA/source context, missing evidence/citation posture, missing aggregation support, or unsupported public exposure posture. |
| `invalid/invalid_<n>.expected_error.txt` | Expected validation or policy reason text for negative examples. |
| local README files | Fixture intent, inventory, and authority-boundary documentation. |

Fixtures should be synthetic, deterministic, compact, public-safe, and reviewable. Prefer metadata-shaped or small-array examples over large sensor exports or raster payloads. Do not store live source dumps, credentials, source-system side effects, release candidates, published layers, or release-blocked material here.

---

## Authority boundary

| Responsibility | Owning root | This README posture |
|---|---|---|
| Agriculture soil-moisture fixtures | `fixtures/domains/agriculture/soil_moisture/` | Documents test/example inputs only. |
| Agriculture object meaning | `contracts/domains/agriculture/` | Referenced, not replaced. |
| Soil-domain meaning and static soil authority | `contracts/domains/soil/` and Soil-domain roots | Out of scope; do not redefine as Agriculture truth. |
| Machine-checkable Agriculture shape | `schemas/contracts/v1/domains/agriculture/` | Referenced, not duplicated. |
| Source registry records | `data/registry/sources/` and source descriptor roots | Out of scope. |
| Agriculture policy | `policy/domains/agriculture/` | Out of scope; fixtures may test it but do not define it. |
| Canonical lifecycle data | `data/raw/`, `data/work/`, `data/quarantine/`, `data/processed/`, `data/catalog/`, `data/triplet/`, `data/published/` | Out of scope; do not duplicate as fixtures. |
| Published layers and release decisions | `data/published/` and `release/` roots | Out of scope. |
| Tests and validation proof | `tests/domains/agriculture/` and validator tooling | Referenced, not claimed as run. |

Do not collapse this fixture lane into station truth, raster truth, Soil-domain authority, Hydrology-domain authority, source registry authority, catalog authority, policy authority, release approval, or public-client permission.

---

## Expected layout

Use the smallest structure that matches the actual test need:

```text
fixtures/domains/agriculture/soil_moisture/
  README.md
  <case_name>.input.json
  <case_name>.expected.json
  <case_name>.snapshot.json
```

For schema-style examples, use:

```text
fixtures/domains/agriculture/soil_moisture/
  valid/
    README.md
    valid_<n>.json
  invalid/
    README.md
    invalid_<n>.json
    invalid_<n>.expected_error.txt
```

For parser or helper snapshots, document whether the expected output represents a station-series parse, modeled-product parse, aggregation obligation, citation obligation, denial, abstention, or safe aggregate response.

---

## Maintenance checklist

Before adding or changing soil-moisture fixtures:

- [ ] Confirm the consuming test, validator, parser, catalog helper, stress helper, suitability helper, or policy helper.
- [ ] Preserve source-role semantics: observed station series, modeled product, aggregate summary, or candidate signal.
- [ ] Include time, depth, station/product identity, QA, source role, and citation/evidence posture when relevant.
- [ ] Keep examples synthetic, compact, deterministic, public-safe, and reviewable.
- [ ] Do not store credentials, full live source responses, source caches, large rasters, release candidates, published layers, or release-blocked material.
- [ ] Preserve source-role, rights, sensitivity, review, receipt, release, citation, and EvidenceBundle expectations in fixture intent.
- [ ] Update this README when fixtures, validators, schemas, policy tests, parser tests, or helper scripts are added.
- [ ] Run the relevant tests or validators before claiming validation success.

---

## Status notes

| Item | Status | Notes |
|---|---:|---|
| Target README | CONFIRMED UPDATED | This path existed as a blank file before this update. |
| Direct fixture payload inventory | NEEDS VERIFICATION | No `valid/`, `invalid/`, input, expected, or snapshot payload files were fetched for this lane during this update. |
| Source-role basis | CONFIRMED DOC | Agriculture source docs identify station soil-moisture sources and SMAP modeled soil-moisture context with distinct roles. |
| SCAN product context | CONFIRMED DOC / PROPOSED PRODUCT PAGE | SCAN is documented as observed station readings with watcher candidate signals and Agriculture as a secondary context domain. |
| Placement | CONFIRMED PATH / PROPOSED LANE REALIZATION | The requested path exists; Agriculture path doctrine includes `fixtures/domains/agriculture/` but marks Agriculture-specific lanes as proposed until verified. |
| Test execution | NOT RUN | No validators, pytest, source admission checks, catalog checks, policy checks, release checks, or CI were run during this README update. |

---

## Evidence ledger

| Source | Status | Supports | Limits |
|---|---|---|---|
| Previous target file | CONFIRMED | Target existed as a blank file. | Did not define Agriculture soil-moisture fixture guidance. |
| Repository search for soil-moisture evidence | CONFIRMED SEARCH | Found Agriculture source guidance, SCAN source catalog documentation, Soil-domain documents, and no-network runbook context. | Search is not a full recursive filesystem listing. |
| `../../../../docs/domains/agriculture/SOURCES.md` | CONFIRMED DOC | Agriculture source family register names Mesonet, SCAN, USCRN, and SMAP with observed/modeled/aggregate source-role distinctions. | Rights, endpoints, and current terms remain NEEDS VERIFICATION in that doc. |
| `../../../../docs/sources/catalog/nrcs/scan-soil-climate.md` | CONFIRMED DOC / PROPOSED PRODUCT PAGE | SCAN is documented as observed station soil-moisture/temperature readings, with watcher candidate posture and Agriculture as secondary context. | Product page is not a SourceDescriptor, validator, or fixture inventory. |
| `../../../../docs/domains/agriculture/CANONICAL_PATHS.md` | CONFIRMED DOC / PROPOSED PATH REALIZATION | Agriculture lane fan includes `fixtures/domains/agriculture/` and separates responsibility roots. | Agriculture-specific path realizations remain proposed until verified. |
| `../../../../docs/doctrine/directory-rules.md` | CONFIRMED doctrine | File placement encodes ownership/governance/lifecycle; `tests/` and `fixtures/` are validate/operate roots. | Specific fixture completeness requires inventory and tests. |

[Back to top](#top)
