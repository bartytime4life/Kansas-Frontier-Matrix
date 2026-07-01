<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://fixture/domains/agriculture/catalog/readme
title: Agriculture catalog fixtures README
type: fixture-readme
version: v0.1.0
status: draft
owners: TODO(owner): agriculture domain steward; TODO(owner): catalog steward; TODO(owner): fixture steward; TODO(owner): validation steward; TODO(owner): policy steward; TODO(owner): docs steward
created: NEEDS VERIFICATION - blank file existed before 2026-07-01 expansion
updated: 2026-07-01
policy_label: public-review
related:
  - ../../../../docs/domains/agriculture/CANONICAL_PATHS.md
  - ../../../../docs/domains/agriculture/DATA_LIFECYCLE.md
  - ../../../../docs/domains/agriculture/SOURCE_REGISTRY.md
  - ../../../../docs/domains/agriculture/RELEASE_INDEX.md
  - ../../../../contracts/domains/agriculture/
  - ../../../../schemas/contracts/v1/domains/agriculture/
  - ../../../../policy/domains/agriculture/
  - ../../../../data/catalog/agriculture/
  - ../../../../data/published/layers/agriculture/
  - ../../../../tests/domains/agriculture/
  - ../../../../docs/doctrine/directory-rules.md
tags: [kfm, fixtures, domains, agriculture, catalog, catalog-fixtures, domain-fixtures, valid-fixtures, invalid-fixtures, aggregation, lifecycle, non-authoritative]
notes:
  - "This README replaces a blank file at `fixtures/domains/agriculture/catalog/README.md`."
  - "This directory is for Agriculture catalog-shaped fixture examples only, not canonical catalog records."
  - "Agriculture-specific fixture paths are consistent with the Agriculture lane fan, but this README does not prove broader fixture coverage or validator wiring."
  - "Catalog truth, lifecycle state, release state, source registry posture, and public layer authority remain in their owning roots."
  - "No tests, validators, catalog promotion checks, source admission checks, policy checks, release checks, or CI jobs were run during this documentation update."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Agriculture catalog fixtures

Fixture lane for Agriculture catalog-shaped examples under `fixtures/domains/agriculture/catalog/`.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: fixtures" src="https://img.shields.io/badge/root-fixtures%2F-6f42c1">
  <img alt="Domain: agriculture" src="https://img.shields.io/badge/domain-agriculture-success">
  <img alt="Lane: catalog" src="https://img.shields.io/badge/lane-catalog-blue">
  <img alt="Authority: fixture only" src="https://img.shields.io/badge/authority-fixture%20only-critical">
  <img alt="Inventory: partial" src="https://img.shields.io/badge/inventory-partial-orange">
</p>

**Path:** `fixtures/domains/agriculture/catalog/README.md`  
**Fixture posture:** Agriculture-domain catalog fixture lane  
**Authority posture:** fixture only; catalog truth, schema authority, policy authority, lifecycle promotion, release approval, and public layer authority remain in their owning roots  
**Quick links:** [Purpose](#purpose) · [Placement basis](#placement-basis) · [Accepted fixture material](#accepted-fixture-material) · [Authority boundary](#authority-boundary) · [Expected layout](#expected-layout) · [Maintenance checklist](#maintenance-checklist) · [Status notes](#status-notes) · [Evidence ledger](#evidence-ledger)

> [!IMPORTANT]
> Files under this directory are catalog-shaped test inputs or examples. They are not canonical catalog records, source truth, EvidenceBundles, SourceDescriptors, PolicyDecisions, ReleaseManifests, published layers, review approval, release approval, or publication authority.

---

## Purpose

This directory is for small, public-safe Agriculture catalog fixtures.

Use this lane when tests, examples, or validators need Agriculture catalog-shaped inputs without reading from canonical lifecycle stores. A fixture here may demonstrate catalog envelope shape, aggregate-only field posture, expected identifiers, or failure cases. It must not be treated as a real catalog record, a promoted lifecycle artifact, a source-admission result, a release candidate, or a public client payload.

A passing fixture proves only the bounded test expectation attached to that fixture. It does not prove crop, field, suitability, stress, irrigation, economy, or aggregation claims are true.

---

## Placement basis

Directory Rules makes file location part of ownership, governance, and lifecycle posture. It also groups `tests/` and `fixtures/` inside the validate/operate authority surface.

Agriculture's canonical path guide includes `fixtures/domains/agriculture/` in the Agriculture lane fan. The same guide states that Agriculture-specific paths are proposed realizations until verified in the repository. This README is therefore narrow: it documents the observed fixture path requested here, not full Agriculture fixture coverage.

Agriculture lifecycle doctrine keeps the data flow separate from fixtures:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

This fixture lane sits outside that lifecycle. Real catalog records belong under the appropriate `data/catalog/...` root after governed promotion; published map or API artifacts belong under governed release and published-data paths.

---

## Accepted fixture material

This directory may contain:

| Material | Use |
|---|---|
| `valid/valid_<n>.json` | Positive catalog-shaped Agriculture examples expected to pass a validator or schema when one is wired. |
| `invalid/invalid_<n>.json` | Negative catalog-shaped Agriculture examples expected to fail validation. |
| `invalid/invalid_<n>.expected_error.txt` | Expected text or pattern for negative validation errors. |
| small snapshot files | Expected-output snapshots for catalog helpers, when clearly marked as snapshots. |
| local README files | Fixture intent, inventory, and authority-boundary documentation. |

Fixture examples should prefer aggregate-safe, metadata-shaped examples. They should avoid precise field-level exposure, person-parcel joins, private source payloads, raw source dumps, release-blocked content, and any payload that would blur test data with governed catalog truth.

---

## Authority boundary

| Responsibility | Owning root | This README posture |
|---|---|---|
| Agriculture catalog fixtures | `fixtures/domains/agriculture/catalog/` | Documents test/example inputs only. |
| Agriculture object meaning | `contracts/domains/agriculture/` | Referenced, not replaced. |
| Machine-checkable domain shape | `schemas/contracts/v1/domains/agriculture/` | Referenced, not duplicated. |
| Agriculture domain policy | `policy/domains/agriculture/` | Out of scope. |
| Source registry posture | `data/registry/sources/agriculture/` | Out of scope. |
| Canonical catalog records | `data/catalog/agriculture/` | Out of scope; do not duplicate as fixtures. |
| Published layers | `data/published/layers/agriculture/` | Out of scope. |
| Release candidates and manifests | `release/candidates/agriculture/` and release roots | Out of scope. |
| Tests and validation proof | `tests/domains/agriculture/` and validator tooling | Referenced, not claimed as run. |

Do not collapse this fixture lane into catalog authority, schema authority, policy authority, source truth, EvidenceBundle authority, release approval, or public-client permission.

---

## Expected layout

Use the smallest structure that matches the actual fixture need:

```text
fixtures/domains/agriculture/catalog/
  README.md
  valid/
    README.md
    valid_<n>.json
  invalid/
    README.md
    invalid_<n>.json
    invalid_<n>.expected_error.txt
```

When the lane contains snapshot fixtures rather than schema fixtures, mark the family clearly and document the script or test that consumes the snapshot. Do not imply schema validation when the fixture is actually a policy-test or helper-output snapshot.

---

## Maintenance checklist

Before adding or changing Agriculture catalog fixtures:

- [ ] Confirm whether the fixture is schema-style, validator-style, or snapshot-style.
- [ ] Keep positive cases under `valid/` and negative cases under `invalid/` when applicable.
- [ ] Keep expected-error text beside the invalid fixture it describes.
- [ ] Keep examples small, deterministic, public-safe, and reviewable.
- [ ] Preserve aggregate-safe Agriculture posture; do not introduce field-level or person-linked examples unless explicitly authorized by policy and tests.
- [ ] Keep source-role, rights, sensitivity, and EvidenceBundle requirements visible in test intent when claims depend on evidence.
- [ ] Do not copy canonical catalog records, raw source payloads, release candidates, or published layers into this fixture lane.
- [ ] Update this README when fixtures, validators, schemas, or test consumers are added.
- [ ] Run the relevant tests or validators before claiming validation success.

---

## Status notes

| Item | Status | Notes |
|---|---:|---|
| Target README | CONFIRMED UPDATED | This path existed as a blank file before this update. |
| Agriculture fixture lane | CONFIRMED PATH / PARTIAL INVENTORY | `fixtures/domains/agriculture/catalog/README.md` exists; no recursive fixture inventory was performed. |
| Agriculture lane fan | CONFIRMED DOC / PROPOSED PATH REALIZATION | Agriculture canonical paths document names `fixtures/domains/agriculture/` as the fixture lane, while stating Agriculture path claims remain proposed until verified. |
| Catalog fixtures | NEEDS VERIFICATION | No `valid/` or `invalid/` catalog fixture files were fetched during this update. |
| Validators and tests | NEEDS VERIFICATION / NOT RUN | No Agriculture catalog validator or test was verified or executed in this update. |
| Public release posture | NOT AUTHORIZED BY THIS README | Fixtures do not approve publication, release, public rendering, or downstream AI use. |

---

## Evidence ledger

| Source | Status | Supports | Limits |
|---|---|---|---|
| Previous target file | CONFIRMED | Target existed as a blank file. | Did not define Agriculture catalog fixture guidance. |
| `../../../../docs/domains/agriculture/CANONICAL_PATHS.md` | CONFIRMED DOC / PROPOSED PATH REALIZATION | Agriculture lane fan includes `fixtures/domains/agriculture/` and separates responsibility roots. | The document marks Agriculture-specific paths as proposed until verified. |
| `../../../../docs/domains/agriculture/DATA_LIFECYCLE.md` | CONFIRMED DOC | Lifecycle invariant, Agriculture scope, aggregation emphasis, and lifecycle-gate posture. | It is lifecycle guidance, not fixture inventory or validator proof. |
| `../../../../docs/doctrine/directory-rules.md` | CONFIRMED doctrine | File placement encodes ownership/governance/lifecycle; `tests/` and `fixtures/` are validate/operate roots. | Specific fixture completeness requires inventory and tests. |

[Back to top](#top)
