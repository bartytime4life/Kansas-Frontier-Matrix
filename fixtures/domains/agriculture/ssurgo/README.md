<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://fixture/domains/agriculture/ssurgo/readme
title: Agriculture SSURGO fixtures README
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
  - ../soil_moisture/README.md
  - ../../../../docs/sources/catalog/nrcs/ssurgo.md
  - ../../../../docs/domains/agriculture/SOURCES.md
  - ../../../../docs/domains/agriculture/PIPELINE.md
  - ../../../../docs/domains/agriculture/CANONICAL_PATHS.md
  - ../../../../docs/domains/agriculture/DATA_LIFECYCLE.md
  - ../../../../contracts/domains/agriculture/
  - ../../../../contracts/domains/soil/
  - ../../../../schemas/contracts/v1/domains/agriculture/
  - ../../../../policy/domains/agriculture/
  - ../../../../tests/domains/agriculture/
  - ../../../../docs/doctrine/directory-rules.md
tags: [kfm, fixtures, domains, agriculture, ssurgo, sda, nrcs, soil, mukey, source-role, observed, aggregate, soil-crop-suitability, non-authoritative]
notes:
  - "This README replaces a blank file at `fixtures/domains/agriculture/ssurgo/README.md`."
  - "This directory is for Agriculture SSURGO-shaped fixtures only, not canonical Soil-domain records, source registry records, SSURGO source truth, or published layer authority."
  - "Repo evidence identifies SSURGO as Soil-domain source-of-record context and Agriculture source guidance admits SSURGO/SDA with observed source-role and aggregate MUKEY summaries."
  - "No direct fixture payloads were found or inspected in this directory during this update, so payload inventory remains NEEDS VERIFICATION."
  - "No tests, validators, source admission checks, catalog checks, policy checks, release checks, or CI jobs were run during this documentation update."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Agriculture SSURGO fixtures

Fixture lane for SSURGO-shaped Agriculture examples under `fixtures/domains/agriculture/ssurgo/`.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: fixtures" src="https://img.shields.io/badge/root-fixtures%2F-6f42c1">
  <img alt="Domain: agriculture" src="https://img.shields.io/badge/domain-agriculture-success">
  <img alt="Source: SSURGO" src="https://img.shields.io/badge/source-SSURGO-blue">
  <img alt="Boundary: Soil authority" src="https://img.shields.io/badge/boundary-Soil%20authority-orange">
  <img alt="Authority: fixture only" src="https://img.shields.io/badge/authority-fixture%20only-critical">
</p>

**Path:** `fixtures/domains/agriculture/ssurgo/README.md`  
**Fixture posture:** Agriculture-domain SSURGO/SDA fixture lane  
**Authority posture:** fixture only; Soil-domain source authority, source registry posture, SSURGO truth, schema authority, policy authority, lifecycle promotion, release approval, and public layer authority remain in their owning roots  
**Quick links:** [Purpose](#purpose) · [Placement basis](#placement-basis) · [SSURGO boundary](#ssurgo-boundary) · [Accepted fixture material](#accepted-fixture-material) · [Authority boundary](#authority-boundary) · [Expected layout](#expected-layout) · [Maintenance checklist](#maintenance-checklist) · [Status notes](#status-notes) · [Evidence ledger](#evidence-ledger)

> [!IMPORTANT]
> Files under this directory are test inputs or expected-output examples. They are not live SSURGO downloads, SDA query results, source registry records, SourceDescriptors, EvidenceBundles, canonical Soil-domain records, Agriculture catalog records, PolicyDecisions, ReleaseManifests, review approval, release approval, or publication authority.

---

## Purpose

This directory is for small, public-safe Agriculture SSURGO fixtures.

Use this lane when Agriculture tests, validators, catalog helpers, soil-crop-suitability helpers, source-role checks, or policy helpers need SSURGO-shaped examples without reading live source systems, source registry records, lifecycle stores, catalog records, or published layers.

A passing fixture proves only the bounded test expectation for that fixture. It does not prove a soil map unit, soil component, MUKEY join, suitability output, source endpoint, source vintage, rights posture, or public release state is current or true.

---

## Placement basis

Agriculture's canonical path guide includes `fixtures/domains/agriculture/` in the Agriculture responsibility-root lane fan. Agriculture source guidance admits SSURGO / Soil Data Access as Agriculture source context while preserving source-role discipline and adjacent Soil-domain ownership.

The governed lifecycle remains separate from this fixture lane:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Real SSURGO capture belongs in governed source/lifecycle lanes after source admission. Real Soil-domain and Agriculture catalog records belong under governed catalog lanes after validation and promotion. Public use requires policy, release, citation, and rollback posture.

---

## SSURGO boundary

SSURGO is Soil-domain authoritative context that Agriculture may cite for suitability or agronomic interpretation. This fixture lane must not re-own soil truth.

| Boundary | Fixture consequence |
|---|---|
| SSURGO is Soil-domain source-of-record context | Agriculture fixtures may model inputs or joins, but canonical soil meaning remains with Soil-domain roots. |
| MUKEY and related joins are identifiers, not proof by themselves | Fixtures should include evidence/citation expectations when testing join behavior. |
| SSURGO/SDA is admitted with source-role discipline | Preserve observed survey/source posture or aggregate MUKEY-summary posture as appropriate. |
| gSSURGO is a gridded derivative | Do not relabel gridded derivative examples as observed SSURGO records. |
| Agriculture may derive suitability context | Suitability-shaped outputs should preserve model/aggregation receipts, evidence references, and release constraints. |
| Public products remain governed | A fixture cannot authorize map rendering, API release, or publication. |

---

## Accepted fixture material

This directory may contain:

| Material | Use |
|---|---|
| `*.input.json` | Small synthetic SSURGO/SDA-shaped input examples. |
| `*.expected.json` | Expected helper output for deterministic join, suitability, catalog, or policy tests. |
| `*.snapshot.json` | Snapshot-style expected output when the consuming test documents snapshot semantics. |
| `valid/valid_<n>.json` | Positive schema examples when a schema or validator is wired. |
| `invalid/invalid_<n>.json` | Negative examples for bad MUKEY joins, missing source role, missing evidence/citation posture, missing rights/sensitivity posture, unsupported field-level use, or Soil/Agriculture boundary collapse. |
| `invalid/invalid_<n>.expected_error.txt` | Expected validation or policy reason text for negative examples. |
| local README files | Fixture intent, inventory, and authority-boundary documentation. |

Fixtures should be synthetic, deterministic, compact, public-safe, and reviewable. Prefer metadata-shaped examples and small join cases. Do not store live source dumps, full SDA responses, source credentials, release candidates, published layers, or release-blocked material here.

---

## Authority boundary

| Responsibility | Owning root | This README posture |
|---|---|---|
| Agriculture SSURGO fixtures | `fixtures/domains/agriculture/ssurgo/` | Documents test/example inputs only. |
| SSURGO product documentation | `docs/sources/catalog/nrcs/ssurgo.md` | Referenced, not replaced. |
| Soil-domain object meaning | `contracts/domains/soil/` and Soil-domain roots | Out of scope; do not redefine as Agriculture truth. |
| Agriculture object meaning | `contracts/domains/agriculture/` | Referenced, not replaced. |
| Source registry records | `data/registry/sources/` and source descriptor roots | Out of scope. |
| Machine-checkable Agriculture shape | `schemas/contracts/v1/domains/agriculture/` | Referenced, not duplicated. |
| Agriculture policy | `policy/domains/agriculture/` | Out of scope; fixtures may test it but do not define it. |
| Canonical lifecycle data | `data/raw/`, `data/work/`, `data/quarantine/`, `data/processed/`, `data/catalog/`, `data/triplet/`, `data/published/` | Out of scope; do not duplicate as fixtures. |
| Published layers and release decisions | `data/published/` and `release/` roots | Out of scope. |
| Tests and validation proof | `tests/domains/agriculture/` and validator tooling | Referenced, not claimed as run. |

Do not collapse this fixture lane into Soil-domain authority, source registry authority, source freshness proof, catalog authority, policy authority, EvidenceBundle authority, release approval, or public-client permission.

---

## Expected layout

Use the smallest structure that matches the actual test need:

```text
fixtures/domains/agriculture/ssurgo/
  README.md
  <case_name>.input.json
  <case_name>.expected.json
  <case_name>.snapshot.json
```

For schema-style examples, use:

```text
fixtures/domains/agriculture/ssurgo/
  valid/
    README.md
    valid_<n>.json
  invalid/
    README.md
    invalid_<n>.json
    invalid_<n>.expected_error.txt
```

For parser or helper snapshots, document whether the expected output represents a parsed source-shaped object, MUKEY join result, aggregation obligation, suitability obligation, citation obligation, denial, abstention, or safe aggregate response.

---

## Maintenance checklist

Before adding or changing SSURGO fixtures:

- [ ] Confirm the consuming test, validator, parser, catalog helper, suitability helper, or policy helper.
- [ ] Preserve Soil-domain authority and do not redefine canonical soil object meaning in Agriculture fixtures.
- [ ] Preserve source-role semantics: observed survey/source posture, aggregate MUKEY summary, candidate, or modeled suitability output.
- [ ] Include MUKEY, component/table scope, time/vintage, source role, rights, sensitivity, and citation/evidence posture when relevant.
- [ ] Keep examples synthetic, compact, deterministic, public-safe, and reviewable.
- [ ] Do not store credentials, full live SDA responses, source caches, release candidates, published layers, or release-blocked material.
- [ ] Update this README when fixtures, validators, schemas, policy tests, parser tests, or helper scripts are added.
- [ ] Run the relevant tests or validators before claiming validation success.

---

## Status notes

| Item | Status | Notes |
|---|---:|---|
| Target README | CONFIRMED UPDATED | This path existed as a blank file before this update. |
| Direct fixture payload inventory | NEEDS VERIFICATION | No `valid/`, `invalid/`, input, expected, or snapshot payload files were fetched for this lane during this update. |
| SSURGO product basis | CONFIRMED DOC / PROPOSED PRODUCT PAGE | The SSURGO source catalog page documents SSURGO as Soil-domain source-of-record context and separates source descriptor authority from docs. |
| Agriculture source-role basis | CONFIRMED DOC | Agriculture source docs admit SSURGO/SDA and gSSURGO while preserving observed/aggregate source-role distinctions. |
| Placement | CONFIRMED PATH / PROPOSED LANE REALIZATION | The requested path exists; Agriculture path doctrine includes `fixtures/domains/agriculture/` but marks Agriculture-specific lanes as proposed until verified. |
| Test execution | NOT RUN | No validators, pytest, source admission checks, catalog checks, policy checks, release checks, or CI were run during this README update. |

---

## Evidence ledger

| Source | Status | Supports | Limits |
|---|---|---|---|
| Previous target file | CONFIRMED | Target existed as a blank file. | Did not define Agriculture SSURGO fixture guidance. |
| Repository search for SSURGO evidence | CONFIRMED SEARCH | Found SSURGO source catalog documentation, Agriculture source guidance, Soil pipeline docs, and Agriculture policy/docs. | Search is not a full recursive filesystem listing. |
| `../../../../docs/sources/catalog/nrcs/ssurgo.md` | CONFIRMED DOC / PROPOSED PRODUCT PAGE | SSURGO product meaning, Soil-domain source-of-record posture, MUKEY-related context, and SourceDescriptor authority boundary. | Product page is not a SourceDescriptor, validator, or fixture inventory. |
| `../../../../docs/domains/agriculture/SOURCES.md` | CONFIRMED DOC | Agriculture source family register names SSURGO/SDA and gSSURGO with observed/aggregate role distinctions and source-role discipline. | Rights, endpoints, and current terms remain NEEDS VERIFICATION in that doc. |
| `../../../../docs/domains/agriculture/CANONICAL_PATHS.md` | CONFIRMED DOC / PROPOSED PATH REALIZATION | Agriculture lane fan includes `fixtures/domains/agriculture/` and separates responsibility roots. | Agriculture-specific path realizations remain proposed until verified. |
| `../../../../docs/doctrine/directory-rules.md` | CONFIRMED doctrine | File placement encodes ownership/governance/lifecycle; `tests/` and `fixtures/` are validate/operate roots. | Specific fixture completeness requires inventory and tests. |

[Back to top](#top)
