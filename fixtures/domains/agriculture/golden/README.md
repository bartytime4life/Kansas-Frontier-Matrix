<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://fixture/domains/agriculture/golden/readme
title: Agriculture golden fixtures README
type: fixture-readme
version: v0.1.0
status: draft
owners: TODO(owner): agriculture domain steward; TODO(owner): fixture steward; TODO(owner): validation steward; TODO(owner): catalog steward; TODO(owner): policy steward; TODO(owner): docs steward
created: NEEDS VERIFICATION - blank file existed before 2026-07-01 expansion
updated: 2026-07-01
policy_label: public-review
related:
  - ../catalog/README.md
  - ../field_level_attempt/README.md
  - ../../../../docs/domains/agriculture/CANONICAL_PATHS.md
  - ../../../../docs/domains/agriculture/DATA_LIFECYCLE.md
  - ../../../../docs/domains/agriculture/POLICY.md
  - ../../../../contracts/domains/agriculture/
  - ../../../../schemas/contracts/v1/domains/agriculture/
  - ../../../../policy/domains/agriculture/
  - ../../../../tests/domains/agriculture/
  - ../../../../data/catalog/agriculture/
  - ../../../../data/published/layers/agriculture/
  - ../../../../docs/doctrine/directory-rules.md
tags: [kfm, fixtures, domains, agriculture, golden-fixtures, expected-output, regression-fixtures, aggregation, catalog, lifecycle, public-safe, non-authoritative]
notes:
  - "This README replaces a blank file at `fixtures/domains/agriculture/golden/README.md`."
  - "This directory is for Agriculture golden fixtures: stable expected inputs or outputs used by tests, validators, or snapshot comparisons."
  - "No direct golden payloads were found or inspected in this directory during this update, so fixture inventory remains NEEDS VERIFICATION."
  - "Golden fixtures are not canonical Agriculture catalog records, release artifacts, source truth, or public-client authority."
  - "No tests, validators, catalog checks, policy checks, release checks, or CI jobs were run during this documentation update."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Agriculture golden fixtures

Golden fixture lane for stable Agriculture expected inputs or outputs under `fixtures/domains/agriculture/golden/`.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: fixtures" src="https://img.shields.io/badge/root-fixtures%2F-6f42c1">
  <img alt="Domain: agriculture" src="https://img.shields.io/badge/domain-agriculture-success">
  <img alt="Lane: golden" src="https://img.shields.io/badge/lane-golden-blue">
  <img alt="Authority: fixture only" src="https://img.shields.io/badge/authority-fixture%20only-critical">
  <img alt="Inventory: needs verification" src="https://img.shields.io/badge/inventory-NEEDS%20VERIFICATION-orange">
</p>

**Path:** `fixtures/domains/agriculture/golden/README.md`  
**Fixture posture:** Agriculture-domain golden fixture lane  
**Authority posture:** fixture only; catalog truth, schema authority, policy authority, lifecycle promotion, release approval, and public layer authority remain in their owning roots  
**Quick links:** [Purpose](#purpose) · [Placement basis](#placement-basis) · [Accepted golden material](#accepted-golden-material) · [Authority boundary](#authority-boundary) · [Expected layout](#expected-layout) · [Maintenance checklist](#maintenance-checklist) · [Status notes](#status-notes) · [Evidence ledger](#evidence-ledger)

> [!IMPORTANT]
> Files under this directory are golden test fixtures or expected-output snapshots. They are not canonical catalog records, source truth, EvidenceBundles, SourceDescriptors, PolicyDecisions, ReleaseManifests, published layers, review approval, release approval, or publication authority.

---

## Purpose

This directory is for Agriculture golden fixtures: stable examples used by tests, validators, or snapshot comparisons.

Use this lane when Agriculture tests need a known-good expected output or a stable input/output pair. Golden fixtures may help detect accidental changes in aggregation behavior, catalog envelope generation, public-safe generalization, identifier normalization, or policy-helper output. A golden fixture must not become the canonical Agriculture record it resembles.

A passing golden comparison proves only that an implementation still matches the expected fixture for that test. It does not prove crop, field, suitability, stress, irrigation, economy, source, or aggregation claims are true.

---

## Placement basis

Agriculture's canonical path guide includes `fixtures/domains/agriculture/` in the Agriculture responsibility-root lane fan. That guide also marks Agriculture-specific path realizations as proposed until verified, so this README documents the observed requested fixture lane without claiming complete implementation maturity.

Agriculture lifecycle guidance keeps fixtures separate from lifecycle stores:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Golden fixtures sit outside that lifecycle. Real catalog records belong under governed `data/catalog/...` paths after promotion, and published map/API artifacts belong under governed release and published-data paths.

---

## Accepted golden material

This directory may contain:

| Material | Use |
|---|---|
| `*.expected.json` | Expected JSON output for deterministic helpers, validators, or policy checks. |
| `*.input.json` | Small synthetic input paired with an expected output. |
| `*.snapshot.json` | Snapshot-style expected output when the consuming test clearly documents snapshot semantics. |
| `valid/valid_<n>.json` | Positive examples if a validator treats golden fixtures as schema inputs. |
| `README.md` files | Fixture intent, inventory, and authority-boundary documentation. |

Golden fixtures should be synthetic, deterministic, compact, public-safe, and reviewable. Prefer aggregate-safe and metadata-shaped examples. Do not use real field-level data, raw source dumps, source-system exports, private joins, release candidates, or published artifacts as golden fixtures.

---

## Authority boundary

| Responsibility | Owning root | This README posture |
|---|---|---|
| Agriculture golden fixtures | `fixtures/domains/agriculture/golden/` | Documents expected test inputs/outputs only. |
| Agriculture catalog fixtures | `fixtures/domains/agriculture/catalog/` | Sibling fixture lane; not canonical catalog. |
| Field-level attempt fixtures | `fixtures/domains/agriculture/field_level_attempt/` | Sibling fail-closed fixture lane. |
| Agriculture object meaning | `contracts/domains/agriculture/` | Referenced, not replaced. |
| Machine-checkable domain shape | `schemas/contracts/v1/domains/agriculture/` | Referenced, not duplicated. |
| Agriculture domain policy | `policy/domains/agriculture/` | Out of scope. |
| Canonical catalog records | `data/catalog/agriculture/` | Out of scope; do not duplicate as fixtures. |
| Published layers | `data/published/layers/agriculture/` | Out of scope. |
| Release candidates and manifests | `release/candidates/agriculture/` and release roots | Out of scope. |
| Tests and validation proof | `tests/domains/agriculture/` and validator tooling | Referenced, not claimed as run. |

Do not collapse this fixture lane into catalog authority, schema authority, policy authority, source truth, EvidenceBundle authority, release approval, or public-client permission.

---

## Expected layout

Use the smallest structure that matches the actual test need:

```text
fixtures/domains/agriculture/golden/
  README.md
  <case_name>.input.json
  <case_name>.expected.json
  <case_name>.snapshot.json
```

For schema-style golden examples, use a conventional nested layout:

```text
fixtures/domains/agriculture/golden/
  valid/
    README.md
    valid_<n>.json
```

For policy-helper snapshots, document the consuming script or test and the meaning of every expected output field.

---

## Maintenance checklist

Before adding or changing Agriculture golden fixtures:

- [ ] Confirm the consuming test, validator, or helper script.
- [ ] Keep golden files deterministic and compact.
- [ ] Prefer synthetic aggregate-safe examples.
- [ ] Preserve source-role, rights, sensitivity, review, receipt, and EvidenceBundle expectations in fixture intent.
- [ ] Do not use golden fixtures as a substitute for canonical catalog records or release artifacts.
- [ ] Do not include real field geometries, operator records, person-parcel joins, raw source dumps, or release-blocked material.
- [ ] Update snapshots intentionally and document why expected output changed.
- [ ] Update this README when fixtures, validators, schemas, policy tests, or helper scripts are added.
- [ ] Run the relevant tests or validators before claiming validation success.

---

## Status notes

| Item | Status | Notes |
|---|---:|---|
| Target README | CONFIRMED UPDATED | This path existed as a blank file before this update. |
| Direct golden payload inventory | NEEDS VERIFICATION | No golden payload files were fetched for this lane during this update. |
| Placement | CONFIRMED PATH / PROPOSED LANE REALIZATION | The requested path exists; Agriculture path doctrine includes `fixtures/domains/agriculture/` but marks Agriculture-specific lanes as proposed until verified. |
| Sibling fixture lane | CONFIRMED | `../catalog/README.md` exists and defines Agriculture catalog fixtures as fixture-only, not catalog authority. |
| Test execution | NOT RUN | No validators, pytest, policy checks, catalog checks, release checks, or CI were run during this README update. |

---

## Evidence ledger

| Source | Status | Supports | Limits |
|---|---|---|---|
| Previous target file | CONFIRMED | Target existed as a blank file. | Did not define golden fixture guidance. |
| `../catalog/README.md` | CONFIRMED | Sibling Agriculture catalog fixture lane and fixture-only boundary. | Does not prove golden fixture payloads exist. |
| `../../../../docs/domains/agriculture/CANONICAL_PATHS.md` | CONFIRMED DOC / PROPOSED PATH REALIZATION | Agriculture lane fan includes `fixtures/domains/agriculture/` and separates responsibility roots. | Agriculture-specific path realizations remain proposed until verified. |
| `../../../../docs/domains/agriculture/DATA_LIFECYCLE.md` | CONFIRMED DOC | Agriculture lifecycle invariant, aggregate-default posture, field-level deny-by-default posture, and load-bearing aggregation framing. | It is lifecycle guidance, not fixture inventory or validator proof. |
| `../../../../docs/doctrine/directory-rules.md` | CONFIRMED doctrine | File placement encodes ownership/governance/lifecycle; `tests/` and `fixtures/` are validate/operate roots. | Specific fixture completeness requires inventory and tests. |

[Back to top](#top)
