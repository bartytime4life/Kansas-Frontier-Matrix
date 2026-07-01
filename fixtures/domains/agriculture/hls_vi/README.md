<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://fixture/domains/agriculture/hls-vi/readme
title: Agriculture HLS VI fixtures README
type: fixture-readme
version: v0.1.0
status: draft
owners: TODO(owner): agriculture domain steward; TODO(owner): remote-sensing steward; TODO(owner): fixture steward; TODO(owner): validation steward; TODO(owner): policy steward; TODO(owner): docs steward
created: NEEDS VERIFICATION - blank file existed before 2026-07-01 expansion
updated: 2026-07-01
policy_label: public-review
related:
  - ../catalog/README.md
  - ../golden/README.md
  - ../field_level_attempt/README.md
  - ../../../../docs/domains/agriculture/CANONICAL_PATHS.md
  - ../../../../docs/domains/agriculture/DATA_LIFECYCLE.md
  - ../../../../docs/domains/agriculture/atmosphere-stress.md
  - ../../../../docs/domains/agriculture/POLICY.md
  - ../../../../contracts/domains/agriculture/
  - ../../../../schemas/contracts/v1/domains/agriculture/
  - ../../../../policy/domains/agriculture/
  - ../../../../tests/domains/agriculture/
  - ../../../../data/catalog/agriculture/
  - ../../../../data/published/layers/agriculture/
  - ../../../../docs/doctrine/directory-rules.md
tags: [kfm, fixtures, domains, agriculture, hls-vi, vegetation-index, remote-sensing, stress-indicator, golden-fixtures, catalog-fixtures, aggregation, lifecycle, non-authoritative]
notes:
  - "This README replaces a blank file at `fixtures/domains/agriculture/hls_vi/README.md`."
  - "Repo search did not find a confirmed `hls_vi` contract, schema, validator, or payload in this update; exact HLS/VI expansion and implementation binding remain NEEDS VERIFICATION."
  - "This directory is documented as an Agriculture vegetation-index / remote-sensing fixture lane, not as source truth or published layer authority."
  - "The lane is bounded by Agriculture's aggregate-default, field-level deny-by-default, source-role, evidence, and lifecycle posture."
  - "No tests, validators, catalog checks, policy checks, release checks, or CI jobs were run during this documentation update."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Agriculture HLS VI fixtures

Fixture lane for Agriculture `hls_vi` examples under `fixtures/domains/agriculture/hls_vi/`.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: fixtures" src="https://img.shields.io/badge/root-fixtures%2F-6f42c1">
  <img alt="Domain: agriculture" src="https://img.shields.io/badge/domain-agriculture-success">
  <img alt="Lane: hls_vi" src="https://img.shields.io/badge/lane-hls__vi-blue">
  <img alt="Implementation: needs verification" src="https://img.shields.io/badge/implementation-NEEDS%20VERIFICATION-orange">
  <img alt="Authority: fixture only" src="https://img.shields.io/badge/authority-fixture%20only-critical">
</p>

**Path:** `fixtures/domains/agriculture/hls_vi/README.md`  
**Fixture posture:** Agriculture-domain remote-sensing / vegetation-index fixture lane  
**Authority posture:** fixture only; source truth, raster truth, catalog truth, schema authority, policy authority, lifecycle promotion, release approval, and public layer authority remain in their owning roots  
**Quick links:** [Purpose](#purpose) · [Placement basis](#placement-basis) · [Accepted fixture material](#accepted-fixture-material) · [Authority boundary](#authority-boundary) · [Expected layout](#expected-layout) · [Maintenance checklist](#maintenance-checklist) · [Status notes](#status-notes) · [Evidence ledger](#evidence-ledger)

> [!IMPORTANT]
> Files under this directory are test inputs or expected-output examples. They are not source imagery, canonical rasters, catalog records, vegetation-stress truth, EvidenceBundles, SourceDescriptors, PolicyDecisions, ReleaseManifests, published layers, review approval, release approval, or publication authority.

---

## Purpose

This directory is for small, public-safe Agriculture `hls_vi` fixtures.

The filename suggests a vegetation-index fixture lane. Repo evidence inspected during this update did not confirm the exact expansion of `hls_vi`, the schema name, the validator name, or the consuming test. Therefore this README treats the lane as **NEEDS VERIFICATION** until a contract, schema, fixture payload, or test consumer is confirmed.

Use this lane for synthetic, minimized examples that help test Agriculture vegetation-index or stress-indicator handling without reading canonical source rasters, lifecycle stores, catalog records, or published layers.

A passing fixture proves only the bounded test expectation for that fixture. It does not prove a crop, field, stress, yield, source, raster, or vegetation-index claim is true.

---

## Placement basis

Agriculture's canonical path guide includes `fixtures/domains/agriculture/` in the Agriculture responsibility-root lane fan. That guide also marks Agriculture-specific path realizations as proposed until verified, so this README documents the observed requested fixture lane without claiming complete implementation maturity.

Agriculture lifecycle guidance keeps fixtures separate from lifecycle stores:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Remote-sensing or vegetation-index fixtures must not be used to bypass this lifecycle. Real source imagery belongs in governed source/lifecycle lanes after source admission. Derived catalog products belong under catalog lanes after validation and promotion. Public layers require release posture, policy review, citations, and rollback paths.

---

## Accepted fixture material

This directory may contain:

| Material | Use |
|---|---|
| `*.input.json` | Small synthetic input describing a vegetation-index test case. |
| `*.expected.json` | Expected output for deterministic index, masking, aggregation, or catalog-helper logic. |
| `*.snapshot.json` | Snapshot-style expected output when the consuming test documents snapshot semantics. |
| `valid/valid_<n>.json` | Positive schema examples if a schema or validator is wired. |
| `invalid/invalid_<n>.json` | Negative examples for missing evidence, invalid band/index metadata, unsafe resolution, missing aggregation receipt, or unsupported exposure posture. |
| `invalid/invalid_<n>.expected_error.txt` | Expected validation or policy reason text for negative examples. |
| local README files | Fixture intent, inventory, and authority-boundary documentation. |

Fixtures should be synthetic, deterministic, compact, public-safe, and reviewable. Prefer aggregate-safe or metadata-shaped examples over raster-sized payloads. Store only the minimum fixture content required for tests.

---

## Authority boundary

| Responsibility | Owning root | This README posture |
|---|---|---|
| `hls_vi` fixtures | `fixtures/domains/agriculture/hls_vi/` | Documents test/example inputs only. |
| Agriculture object meaning | `contracts/domains/agriculture/` | Referenced, not replaced. |
| Machine-checkable Agriculture shape | `schemas/contracts/v1/domains/agriculture/` | Referenced, not duplicated. |
| Agriculture remote-sensing policy | `policy/domains/agriculture/` and sensitivity/release policy roots | Out of scope. |
| Canonical source/lifecycle data | `data/raw/`, `data/work/`, `data/quarantine/`, `data/processed/`, `data/catalog/`, `data/triplet/`, `data/published/` | Out of scope; do not duplicate as fixtures. |
| Source registry records | `data/registry/sources/` | Out of scope. |
| Published layers | `data/published/layers/agriculture/` | Out of scope. |
| Release candidates and manifests | `release/candidates/agriculture/` and release roots | Out of scope. |
| Tests and validation proof | `tests/domains/agriculture/` and validator tooling | Referenced, not claimed as run. |

Do not collapse this fixture lane into raster truth, stress-indicator truth, catalog authority, schema authority, policy authority, EvidenceBundle authority, release approval, or public-client permission.

---

## Expected layout

Use the smallest structure that matches the actual test need:

```text
fixtures/domains/agriculture/hls_vi/
  README.md
  <case_name>.input.json
  <case_name>.expected.json
  <case_name>.snapshot.json
```

For schema-style examples, use the common valid/invalid convention:

```text
fixtures/domains/agriculture/hls_vi/
  valid/
    README.md
    valid_<n>.json
  invalid/
    README.md
    invalid_<n>.json
    invalid_<n>.expected_error.txt
```

For raster-derived tests, prefer small metadata fixtures or compact array snippets rather than production-sized image data. Large source rasters belong in governed data/source lanes, not fixture documentation lanes.

---

## Maintenance checklist

Before adding or changing `hls_vi` fixtures:

- [ ] Confirm what `hls_vi` means in the repo and document the contract, schema, validator, or test consumer.
- [ ] Confirm whether the fixture is schema-style, validator-style, helper-output, or snapshot-style.
- [ ] Keep examples synthetic, deterministic, compact, public-safe, and reviewable.
- [ ] Preserve source-role, rights, sensitivity, review, receipt, and EvidenceBundle expectations in fixture intent.
- [ ] Avoid real field geometries, operator records, person-parcel joins, raw source imagery, large raster payloads, or release-blocked material.
- [ ] Use aggregate-safe or generalized outputs for any public-facing expected result.
- [ ] Keep negative examples for unsafe exact exposure, missing evidence, missing aggregation, missing source provenance, or unsupported public release posture.
- [ ] Update this README when fixtures, validators, schemas, policy tests, or helper scripts are added.
- [ ] Run the relevant tests or validators before claiming validation success.

---

## Status notes

| Item | Status | Notes |
|---|---:|---|
| Target README | CONFIRMED UPDATED | This path existed as a blank file before this update. |
| Direct `hls_vi` contract/schema/validator evidence | NEEDS VERIFICATION | Repo search did not return a confirmed `hls_vi` contract, schema, validator, or payload. |
| Direct fixture payload inventory | NEEDS VERIFICATION | No `valid/`, `invalid/`, input, expected, or snapshot payload files were fetched for this lane during this update. |
| Placement | CONFIRMED PATH / PROPOSED LANE REALIZATION | The requested path exists; Agriculture path doctrine includes `fixtures/domains/agriculture/` but marks Agriculture-specific lanes as proposed until verified. |
| Agriculture stress context | CONFIRMED DOC / IMPLEMENTATION PROPOSED | Agriculture cross-lane docs identify vegetation-stress products and source-role discipline as relevant Agriculture context, but this does not confirm `hls_vi` implementation. |
| Test execution | NOT RUN | No validators, pytest, policy checks, catalog checks, release checks, or CI were run during this README update. |

---

## Evidence ledger

| Source | Status | Supports | Limits |
|---|---|---|---|
| Previous target file | CONFIRMED | Target existed as a blank file. | Did not define `hls_vi` fixture guidance. |
| Repository search for `hls_vi` | CONFIRMED SEARCH / NO MATCH | No confirmed repo evidence for a named `hls_vi` contract, schema, validator, or payload was found in this update. | Search is not a full recursive filesystem listing. |
| `../../../../docs/domains/agriculture/atmosphere-stress.md` | CONFIRMED DOC | Agriculture owns stress-indicator interpretation and vegetation-stress context while preserving source-role discipline. | Cross-lane reference only; does not confirm `hls_vi` implementation. |
| `../../../../docs/domains/agriculture/CANONICAL_PATHS.md` | CONFIRMED DOC / PROPOSED PATH REALIZATION | Agriculture lane fan includes `fixtures/domains/agriculture/` and separates responsibility roots. | Agriculture-specific path realizations remain proposed until verified. |
| `../../../../docs/domains/agriculture/DATA_LIFECYCLE.md` | CONFIRMED DOC | Agriculture lifecycle invariant, aggregate-default posture, field-level deny-by-default posture, and load-bearing aggregation framing. | It is lifecycle guidance, not fixture inventory or validator proof. |
| `../../../../docs/doctrine/directory-rules.md` | CONFIRMED doctrine | File placement encodes ownership/governance/lifecycle; `tests/` and `fixtures/` are validate/operate roots. | Specific fixture completeness requires inventory and tests. |

[Back to top](#top)
