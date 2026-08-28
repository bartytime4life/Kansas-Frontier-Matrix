<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://fixture/domains/agriculture/readme
title: Agriculture domain fixtures README
type: fixture-readme
version: v0.1.0
status: draft
owners: TODO(owner): agriculture domain steward; TODO(owner): fixture steward; TODO(owner): validation steward; TODO(owner): policy steward; TODO(owner): source steward; TODO(owner): docs steward
created: NEEDS VERIFICATION - greenfield stub existed before 2026-07-01 expansion
updated: 2026-07-01
policy_label: public-review
related:
  - ../../../docs/domains/agriculture/CANONICAL_PATHS.md
  - ../../../docs/domains/agriculture/DATA_LIFECYCLE.md
  - ../../../docs/domains/agriculture/POLICY.md
  - ../../../docs/domains/agriculture/SOURCES.md
  - ../../../policy/domains/agriculture/README.md
  - ../../../contracts/domains/agriculture/
  - ../../../schemas/contracts/v1/domains/agriculture/
  - ../../../tests/domains/agriculture/
  - ../../../data/registry/sources/agriculture/
  - ../../../data/catalog/agriculture/
  - ../../../data/published/layers/agriculture/
  - ../../../release/candidates/agriculture/
  - ../../../docs/doctrine/directory-rules.md
tags: [kfm, fixtures, domains, agriculture, fixture-index, domain-fixtures, catalog-fixtures, source-fixtures, valid-fixtures, invalid-fixtures, no-network, release-fixtures, non-authoritative]
notes:
  - "This README replaces the greenfield stub at `fixtures/domains/agriculture/README.md`."
  - "This directory is an Agriculture fixture root, not a canonical data, source registry, catalog, policy, release, or public-client authority root."
  - "Child README coverage is PARTIAL and based on files updated in this documentation sequence; payload inventory and test wiring remain NEEDS VERIFICATION unless a child README says otherwise."
  - "A fixture passing a check proves only the bounded test expectation for that fixture; it does not prove source truth, catalog truth, policy approval, release approval, or publication authorization."
  - "No tests, validators, source admission checks, catalog checks, policy checks, release checks, network-isolation checks, or CI jobs were run during this documentation update."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Agriculture fixtures

Fixture root for Agriculture-domain examples under `fixtures/domains/agriculture/`.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: fixtures" src="https://img.shields.io/badge/root-fixtures%2F-6f42c1">
  <img alt="Domain: agriculture" src="https://img.shields.io/badge/domain-agriculture-success">
  <img alt="Inventory: partial" src="https://img.shields.io/badge/inventory-partial-orange">
  <img alt="Tests: not run" src="https://img.shields.io/badge/tests-NOT%20RUN-red">
  <img alt="Authority: fixture only" src="https://img.shields.io/badge/authority-fixture%20only-critical">
</p>

**Path:** `fixtures/domains/agriculture/README.md`  
**Fixture posture:** Agriculture-domain fixture index  
**Authority posture:** fixture only; source truth, catalog truth, schema authority, policy authority, lifecycle promotion, release approval, and public layer authority remain in their owning roots  
**Quick links:** [Purpose](#purpose) · [Placement basis](#placement-basis) · [Observed child lanes](#observed-child-lanes) · [Common fixture rules](#common-fixture-rules) · [Authority boundary](#authority-boundary) · [Expected layout](#expected-layout) · [Maintenance checklist](#maintenance-checklist) · [Status notes](#status-notes) · [Evidence ledger](#evidence-ledger)

> [!IMPORTANT]
> Files under this directory are test inputs, expected-output examples, snapshots, or local fixture documentation. They are not source records, SourceDescriptors, EvidenceBundles, canonical catalog records, PolicyDecisions, ReleaseManifests, published layers, review approval, release approval, or publication authority.

---

## Purpose

`fixtures/domains/agriculture/` groups Agriculture-domain examples used by tests, validators, parsers, catalog helpers, source-role checks, policy helpers, release helpers, and no-network test cases.

Fixtures here should be synthetic, minimized, deterministic, public-safe, and tied to a stated test expectation. They are downstream examples, not truth stores. A passing fixture proves only the bounded expectation attached to that fixture. It does not prove a crop, field, soil, moisture, stress, yield, suitability, source, catalog, release, or map-layer claim is true.

---

## Placement basis

Agriculture's canonical path guide includes `fixtures/domains/agriculture/` in the Agriculture responsibility-root lane fan. That guide treats responsibility roots as stable authority boundaries and marks Agriculture-specific path realizations as proposed until verified.

Agriculture lifecycle guidance keeps fixtures separate from lifecycle stores:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Fixtures may model lifecycle-shaped payloads, but they do not participate in lifecycle state. Real source captures, processed candidates, catalog records, release candidates, and published layers belong in their owning roots after governed validation, promotion, policy, review, and release gates.

---

## Observed child lanes

The following child README files are documented in this fixture root. Payload coverage is not assumed from README presence.

| Lane | Purpose | Status |
|---|---|---|
| [`catalog/`](catalog/README.md) | Catalog-shaped Agriculture examples. | CONFIRMED README / PAYLOAD INVENTORY NEEDS VERIFICATION |
| [`field_level_attempt/`](field_level_attempt/README.md) | Fail-closed examples for exact or field-level exposure attempts. | CONFIRMED README / PAYLOAD INVENTORY NEEDS VERIFICATION |
| [`golden/`](golden/README.md) | Stable expected inputs or outputs for regression-style tests. | CONFIRMED README / PAYLOAD INVENTORY NEEDS VERIFICATION |
| [`hls_vi/`](hls_vi/README.md) | Vegetation-index / remote-sensing shaped examples. | CONFIRMED README / IMPLEMENTATION BINDING NEEDS VERIFICATION |
| [`invalid/`](invalid/README.md) | Domain-level negative examples expected to fail a bounded check. | CONFIRMED README / PAYLOAD INVENTORY NEEDS VERIFICATION |
| [`nass_quickstats/`](nass_quickstats/README.md) | NASS QuickStats-shaped aggregate examples. | CONFIRMED README / PAYLOAD INVENTORY NEEDS VERIFICATION |
| [`no_network/`](no_network/README.md) | Parent lane for deterministic offline Agriculture examples. | CONFIRMED README / NETWORK ISOLATION NOT RUN |
| [`no_network/nass/`](no_network/nass/README.md) | Offline NASS-shaped examples. | CONFIRMED README / NETWORK ISOLATION NOT RUN |
| [`release/`](release/README.md) | Release-shaped examples for release-helper or policy tests. | CONFIRMED README / RELEASE AUTHORITY NOT GRANTED |
| [`soil_moisture/`](soil_moisture/README.md) | Soil-moisture-shaped examples preserving source-role boundaries. | CONFIRMED README / PAYLOAD INVENTORY NEEDS VERIFICATION |
| [`ssurgo/`](ssurgo/README.md) | SSURGO/SDA-shaped examples for Agriculture use while preserving Soil authority. | CONFIRMED README / PAYLOAD INVENTORY NEEDS VERIFICATION |
| [`valid/`](valid/README.md) | Domain-level positive examples expected to pass a bounded check. | CONFIRMED README / PAYLOAD INVENTORY NEEDS VERIFICATION |

Add new child lanes only when there is a real test, validator, parser, source-helper, catalog-helper, policy-helper, release-helper, or documentation need. Avoid creating topic folders that duplicate a source registry, policy root, release root, or lifecycle data root.

---

## Common fixture rules

| Rule | Meaning |
|---|---|
| Fixture-only authority | Fixtures are examples for bounded tests, not canonical records. |
| Public-safe by default | Examples should be synthetic, minimized, and safe to review in the repository. |
| Source-role preserved | Observed, modeled, aggregate, administrative, candidate, and synthetic examples must not silently change role. |
| Evidence expectations visible | Fixtures that model claims should include evidence/citation expectations or explicitly state why evidence is out of scope. |
| Lifecycle boundary preserved | Fixture success does not move material through `RAW -> PUBLISHED`. |
| Release boundary preserved | Fixture success does not authorize release, signing, rollback, or public rendering. |
| Tests must be named | A fixture should identify the consuming test, validator, parser, or helper as soon as that consumer exists. |
| Results must be reproducible | Expected outputs should be deterministic and reviewable. |

---

## Authority boundary

| Responsibility | Owning root | This README posture |
|---|---|---|
| Agriculture fixtures | `fixtures/domains/agriculture/` | Indexes and bounds test/example inputs only. |
| Agriculture object meaning | `contracts/domains/agriculture/` | Referenced, not replaced. |
| Machine-checkable Agriculture shape | `schemas/contracts/v1/domains/agriculture/` | Referenced, not duplicated. |
| Agriculture policy | `policy/domains/agriculture/` and policy roots | Out of scope; fixtures may test it but do not define it. |
| Source registry records | `data/registry/sources/` and source descriptor roots | Out of scope. |
| Canonical lifecycle data | `data/raw/`, `data/work/`, `data/quarantine/`, `data/processed/`, `data/catalog/`, `data/triplet/`, `data/published/` | Out of scope; do not duplicate as fixtures. |
| Release candidates and decisions | `release/` roots | Out of scope; fixtures may model shape but do not decide release. |
| Published layers and public clients | `data/published/`, governed APIs, and app roots | Out of scope. |
| Tests and validation proof | `tests/domains/agriculture/` and validator tooling | Referenced, not claimed as run. |

Do not collapse this fixture root into source authority, catalog authority, schema authority, policy authority, release authority, EvidenceBundle authority, or public-client permission.

---

## Expected layout

Use source-, family-, or behavior-specific child lanes with local READMEs:

```text
fixtures/domains/agriculture/
  README.md
  catalog/
    README.md
  valid/
    README.md
  invalid/
    README.md
  no_network/
    README.md
    nass/
      README.md
```

For schema-style examples inside a child lane, use:

```text
fixtures/domains/agriculture/<lane>/
  valid/
    README.md
    valid_<n>.json
  invalid/
    README.md
    invalid_<n>.json
    invalid_<n>.expected_error.txt
```

For snapshot or helper tests, use compact, named cases:

```text
fixtures/domains/agriculture/<lane>/
  <case_name>.input.json
  <case_name>.expected.json
```

---

## Maintenance checklist

Before adding or changing Agriculture fixtures:

- [ ] Confirm the consuming test, validator, parser, source helper, catalog helper, policy helper, release helper, or no-network test.
- [ ] Confirm whether the fixture is schema-style, validator-style, parser-style, policy-style, catalog-helper, release-helper, or snapshot-style.
- [ ] Keep examples synthetic, compact, deterministic, public-safe, and reviewable.
- [ ] Preserve source-role, rights, sensitivity, review, receipt, release, citation, and EvidenceBundle expectations in fixture intent.
- [ ] Keep field-level and private-adjacent exposure fail-closed unless a reviewed policy path explicitly permits a transformed output.
- [ ] Do not store credentials, full live source responses, source caches, canonical records, release candidates, published layers, or release-blocked material.
- [ ] Pair negative examples with expected error text or expected policy/helper output.
- [ ] Update the child README and this parent index when adding a new lane.
- [ ] Run the relevant tests or validators before claiming validation success.

---

## Status notes

| Item | Status | Notes |
|---|---:|---|
| Target README | CONFIRMED UPDATED | Replaced the greenfield stub at this path. |
| Child README coverage | PARTIAL | Child lanes listed above have README files, but this is not a complete filesystem inventory. |
| Direct payload inventory | NEEDS VERIFICATION | This update did not fetch or validate every payload file under this fixture root. |
| Placement | CONFIRMED PATH / PROPOSED LANE REALIZATION | The requested path exists; Agriculture path doctrine includes `fixtures/domains/agriculture/` but marks Agriculture-specific lanes as proposed until verified. |
| Lifecycle boundary | CONFIRMED DOC | Agriculture lifecycle guidance separates fixtures from governed lifecycle state and public release. |
| Test execution | NOT RUN | No validators, pytest, source admission checks, catalog checks, policy checks, release checks, no-network checks, or CI were run during this README update. |

---

## Evidence ledger

| Source | Status | Supports | Limits |
|---|---|---|---|
| Previous target file | CONFIRMED | Target existed as a greenfield stub. | Did not define fixture governance or child-lane index. |
| Repository search for Agriculture fixture index | CONFIRMED SEARCH / LIMITED RESULT | Search surfaced planning documentation but did not provide a complete fixture payload inventory. | Search is not a full recursive filesystem listing. |
| `catalog/README.md` | CONFIRMED | Catalog child lane and fixture-only boundary. | Does not prove catalog payload inventory or validator wiring. |
| `valid/README.md` | CONFIRMED | Positive child lane and definition of bounded fixture validity. | Does not prove valid payload inventory or test success. |
| `no_network/README.md` | CONFIRMED | Parent offline lane and no-network constraints. | No network-isolation test was run. |
| `../../../docs/domains/agriculture/CANONICAL_PATHS.md` | CONFIRMED DOC / PROPOSED PATH REALIZATION | Agriculture lane fan includes `fixtures/domains/agriculture/` and separates responsibility roots. | Agriculture-specific path realizations remain proposed until verified. |
| `../../../docs/domains/agriculture/DATA_LIFECYCLE.md` | CONFIRMED DOC | Agriculture lifecycle invariant, aggregate-default posture, field-level deny-by-default posture, and lifecycle-gate framing. | It is lifecycle guidance, not fixture inventory or validator proof. |
| `../../../docs/doctrine/directory-rules.md` | CONFIRMED doctrine | File placement encodes ownership/governance/lifecycle; `tests/` and `fixtures/` are validate/operate roots. | Specific fixture completeness requires inventory and tests. |

[Back to top](#top)
