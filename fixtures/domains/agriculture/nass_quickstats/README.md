<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://fixture/domains/agriculture/nass-quickstats/readme
title: Agriculture NASS QuickStats fixtures README
type: fixture-readme
version: v0.1.0
status: draft
owners: TODO(owner): agriculture domain steward; TODO(owner): source steward; TODO(owner): fixture steward; TODO(owner): validation steward; TODO(owner): policy steward; TODO(owner): docs steward
created: NEEDS VERIFICATION - blank file existed before 2026-07-01 expansion
updated: 2026-07-01
policy_label: public-review
related:
  - ../catalog/README.md
  - ../field_level_attempt/README.md
  - ../golden/README.md
  - ../invalid/README.md
  - ../../../../docs/sources/catalog/usda/usda-nass-quickstats.md
  - ../../../../docs/domains/agriculture/PIPELINE.md
  - ../../../../docs/domains/agriculture/CANONICAL_PATHS.md
  - ../../../../docs/domains/agriculture/DATA_LIFECYCLE.md
  - ../../../../policy/domains/agriculture/README.md
  - ../../../../contracts/domains/agriculture/
  - ../../../../schemas/contracts/v1/domains/agriculture/
  - ../../../../data/registry/sources/agriculture/
  - ../../../../tests/domains/agriculture/
  - ../../../../docs/doctrine/directory-rules.md
tags: [kfm, fixtures, domains, agriculture, nass, quickstats, usda, aggregate, source-role, anti-collapse, field-level-deny, aggregation-receipt, catalog-fixtures, non-authoritative]
notes:
  - "This README replaces a blank file at `fixtures/domains/agriculture/nass_quickstats/README.md`."
  - "This directory is for Agriculture NASS QuickStats fixtures only, not source registry records, source truth, or canonical catalog records."
  - "Repo evidence confirms QuickStats is documented as aggregate source-role data with field-level anti-collapse constraints."
  - "No direct fixture payloads were found or inspected in this directory during this update, so payload inventory remains NEEDS VERIFICATION."
  - "No tests, validators, source admission checks, catalog checks, policy checks, release checks, or CI jobs were run during this documentation update."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Agriculture NASS QuickStats fixtures

Fixture lane for USDA NASS QuickStats-shaped Agriculture examples under `fixtures/domains/agriculture/nass_quickstats/`.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: fixtures" src="https://img.shields.io/badge/root-fixtures%2F-6f42c1">
  <img alt="Domain: agriculture" src="https://img.shields.io/badge/domain-agriculture-success">
  <img alt="Source: NASS QuickStats" src="https://img.shields.io/badge/source-NASS%20QuickStats-blue">
  <img alt="Source role: aggregate" src="https://img.shields.io/badge/source__role-aggregate-orange">
  <img alt="Authority: fixture only" src="https://img.shields.io/badge/authority-fixture%20only-critical">
</p>

**Path:** `fixtures/domains/agriculture/nass_quickstats/README.md`  
**Fixture posture:** Agriculture-domain QuickStats aggregate fixture lane  
**Authority posture:** fixture only; source registry posture, catalog truth, schema authority, policy authority, lifecycle promotion, release approval, and public layer authority remain in their owning roots  
**Quick links:** [Purpose](#purpose) · [Placement basis](#placement-basis) · [QuickStats source-role boundary](#quickstats-source-role-boundary) · [Accepted fixture material](#accepted-fixture-material) · [Authority boundary](#authority-boundary) · [Expected layout](#expected-layout) · [Maintenance checklist](#maintenance-checklist) · [Status notes](#status-notes) · [Evidence ledger](#evidence-ledger)

> [!IMPORTANT]
> Files under this directory are fixtures for aggregate QuickStats-shaped examples. They are not live NASS downloads, source registry records, SourceDescriptors, EvidenceBundles, canonical catalog records, PolicyDecisions, ReleaseManifests, review approval, release approval, or publication authority.

---

## Purpose

This directory is for small, public-safe USDA NASS QuickStats fixtures used by Agriculture tests, validators, catalog helpers, aggregation checks, or policy checks.

QuickStats fixtures should exercise aggregate-statistics handling. They must not normalize aggregate cells into field-level truth. A passing fixture proves only the bounded test expectation for that fixture. It does not prove an agricultural statistic is current, that a source endpoint was reached, that rights were re-verified, or that an output may be published.

---

## Placement basis

Agriculture's canonical path guide includes `fixtures/domains/agriculture/` in the Agriculture responsibility-root lane fan. Agriculture pipeline docs also include `fixtures/domains/agriculture/` in the Agriculture pipeline-related path set.

The governed lifecycle remains separate from this fixture lane:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Real NASS capture belongs in governed source/lifecycle lanes after source admission. Real catalog records belong under governed catalog lanes after validation and promotion. Public use requires policy, release, citation, and rollback posture.

---

## QuickStats source-role boundary

The repo's QuickStats source page documents QuickStats as aggregate agricultural statistics. It identifies QuickStats as a USDA NASS product, marks the product as tabular agricultural statistics aggregated by county, state, year, and other units, and records `aggregate` as the source role.

For fixtures in this lane, preserve these rules:

| Rule | Fixture meaning |
|---|---|
| QuickStats is aggregate data | Fixtures should represent aggregate cells or aggregate-shaped metadata. |
| Aggregate cells are not field observations | Negative fixtures should cover attempts to use a QuickStats cell as field-level truth. |
| Aggregation receipt is required for promoted use | Positive expected outputs should include aggregation support when the test models promotion-like behavior. |
| Geometry scope must match the aggregation unit | Fixtures should make county/state/year or similar scope explicit. |
| AI/public exact exposure must fail closed | Use expected-denial examples for per-field or per-operator interpretations. |

---

## Accepted fixture material

This directory may contain:

| Material | Use |
|---|---|
| `*.input.json` | Small synthetic QuickStats-shaped input examples. |
| `*.expected.json` | Expected aggregate-safe output for deterministic helpers or catalog transformations. |
| `*.snapshot.json` | Snapshot-style expected output for policy or helper tests. |
| `valid/valid_<n>.json` | Positive schema examples when a schema or validator is wired. |
| `invalid/invalid_<n>.json` | Negative examples for source-role collapse, field-level use, missing aggregation support, missing scope, or missing evidence/citation posture. |
| `invalid/invalid_<n>.expected_error.txt` | Expected validation or policy reason text for negative examples. |
| local README files | Fixture intent, inventory, and authority-boundary documentation. |

Fixtures should be synthetic, deterministic, compact, public-safe, and reviewable. Prefer county/state/year aggregate examples. Do not store live source dumps, full query results, private joins, release candidates, published layers, or source credentials in this fixture lane.

---

## Authority boundary

| Responsibility | Owning root | This README posture |
|---|---|---|
| QuickStats fixtures | `fixtures/domains/agriculture/nass_quickstats/` | Documents test/example inputs only. |
| QuickStats source catalog documentation | `docs/sources/catalog/usda/usda-nass-quickstats.md` | Referenced, not replaced. |
| Source registry records | `data/registry/sources/agriculture/` or source registry roots | Out of scope. |
| Agriculture object meaning | `contracts/domains/agriculture/` | Referenced, not replaced. |
| Machine-checkable Agriculture shape | `schemas/contracts/v1/domains/agriculture/` | Referenced, not duplicated. |
| Agriculture policy | `policy/domains/agriculture/` | Out of scope; fixtures may test it but do not define it. |
| Canonical lifecycle data | `data/raw/`, `data/work/`, `data/quarantine/`, `data/processed/`, `data/catalog/`, `data/triplet/`, `data/published/` | Out of scope; do not duplicate as fixtures. |
| Release decisions | `release/` roots | Out of scope. |
| Tests and validation proof | `tests/domains/agriculture/` and validator tooling | Referenced, not claimed as run. |

Do not collapse this fixture lane into source authority, source registry authority, catalog authority, policy authority, release approval, or public-client permission.

---

## Expected layout

Use the smallest structure that matches the actual test need:

```text
fixtures/domains/agriculture/nass_quickstats/
  README.md
  <case_name>.input.json
  <case_name>.expected.json
  <case_name>.snapshot.json
```

For schema-style examples, use:

```text
fixtures/domains/agriculture/nass_quickstats/
  valid/
    README.md
    valid_<n>.json
  invalid/
    README.md
    invalid_<n>.json
    invalid_<n>.expected_error.txt
```

For policy-helper snapshots, document whether the expected output represents a denial, abstention, aggregation obligation, citation obligation, or safe aggregate response.

---

## Maintenance checklist

Before adding or changing NASS QuickStats fixtures:

- [ ] Confirm the consuming test, validator, or helper script.
- [ ] Preserve `aggregate` source-role semantics.
- [ ] Include aggregation unit and period when the fixture represents a QuickStats cell.
- [ ] Keep field-level or per-place interpretations in the negative lane unless a reviewed policy path explicitly permits a transformed output.
- [ ] Preserve source-role, rights, sensitivity, review, receipt, release, citation, and EvidenceBundle expectations in fixture intent.
- [ ] Keep examples synthetic, compact, deterministic, public-safe, and reviewable.
- [ ] Do not include live source dumps, source credentials, private joins, release candidates, published layers, or release-blocked material.
- [ ] Update this README when fixtures, validators, schemas, policy tests, or helper scripts are added.
- [ ] Run the relevant tests or validators before claiming validation success.

---

## Status notes

| Item | Status | Notes |
|---|---:|---|
| Target README | CONFIRMED UPDATED | This path existed as a blank file before this update. |
| Direct fixture payload inventory | NEEDS VERIFICATION | No `valid/`, `invalid/`, input, expected, or snapshot payload files were fetched for this lane during this update. |
| QuickStats source-role basis | CONFIRMED DOC | The source catalog page documents QuickStats as aggregate data and identifies anti-collapse constraints. |
| Placement | CONFIRMED PATH / PROPOSED LANE REALIZATION | The requested path exists; Agriculture path doctrine includes `fixtures/domains/agriculture/` but marks Agriculture-specific lanes as proposed until verified. |
| Test execution | NOT RUN | No validators, pytest, source admission checks, catalog checks, policy checks, release checks, or CI were run during this README update. |

---

## Evidence ledger

| Source | Status | Supports | Limits |
|---|---|---|---|
| Previous target file | CONFIRMED | Target existed as a blank file. | Did not define NASS QuickStats fixture guidance. |
| Repository search for NASS QuickStats | CONFIRMED SEARCH | Found the QuickStats source catalog page and Agriculture pipeline references. | Search is not a full recursive filesystem listing. |
| `../../../../docs/sources/catalog/usda/usda-nass-quickstats.md` | CONFIRMED DOC | QuickStats aggregate source-role, anti-collapse posture, aggregation receipt, geometry-scope guard, and field-level denial rules. | Endpoint, cadence specifics, rights status, and source registry record remain NEEDS VERIFICATION in that doc. |
| `../../../../docs/domains/agriculture/PIPELINE.md` | CONFIRMED DOC / PROPOSED WIRING | Agriculture pipeline path set includes fixtures, connectors, lifecycle data, registry, release, and pipeline paths; watchers/connectors are non-publishers. | The file itself marks path-shaped claims as PROPOSED and was not executed. |
| `../../../../docs/domains/agriculture/CANONICAL_PATHS.md` | CONFIRMED DOC / PROPOSED PATH REALIZATION | Agriculture lane fan includes `fixtures/domains/agriculture/` and separates responsibility roots. | Agriculture-specific path realizations remain proposed until verified. |
| `../../../../docs/doctrine/directory-rules.md` | CONFIRMED doctrine | File placement encodes ownership/governance/lifecycle; `tests/` and `fixtures/` are validate/operate roots. | Specific fixture completeness requires inventory and tests. |

[Back to top](#top)
