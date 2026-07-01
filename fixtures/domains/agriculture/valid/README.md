<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://fixture/domains/agriculture/valid/readme
title: Agriculture valid fixtures README
type: fixture-readme
version: v0.1.0
status: draft
owners: TODO(owner): agriculture domain steward; TODO(owner): fixture steward; TODO(owner): validation steward; TODO(owner): policy steward; TODO(owner): sensitivity steward; TODO(owner): docs steward
created: NEEDS VERIFICATION - blank file existed before 2026-07-01 expansion
updated: 2026-07-01
policy_label: public-review
related:
  - ../invalid/README.md
  - ../catalog/README.md
  - ../golden/README.md
  - ../release/README.md
  - ../nass_quickstats/README.md
  - ../soil_moisture/README.md
  - ../ssurgo/README.md
  - ../../../../docs/domains/agriculture/CANONICAL_PATHS.md
  - ../../../../docs/domains/agriculture/DATA_LIFECYCLE.md
  - ../../../../docs/domains/agriculture/POLICY.md
  - ../../../../policy/domains/agriculture/README.md
  - ../../../../contracts/domains/agriculture/
  - ../../../../schemas/contracts/v1/domains/agriculture/
  - ../../../../policy/domains/agriculture/
  - ../../../../tests/domains/agriculture/
  - ../../../../docs/doctrine/directory-rules.md
tags: [kfm, fixtures, domains, agriculture, valid-fixtures, positive-fixtures, schema-fixtures, validator-fixtures, policy-fixtures, aggregation, source-role, evidence, non-authoritative]
notes:
  - "This README replaces a blank file at `fixtures/domains/agriculture/valid/README.md`."
  - "This directory is for Agriculture domain valid fixtures and expected positive examples."
  - "Repo search did not surface confirmed valid payload files in this directory during this update, so payload inventory remains NEEDS VERIFICATION."
  - "A valid fixture is not source truth, catalog authority, policy approval, release approval, or publication authority."
  - "No tests, validators, policy checks, source admission checks, catalog checks, release checks, or CI jobs were run during this documentation update."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Agriculture valid fixtures

Domain-level positive fixture lane for Agriculture examples under `fixtures/domains/agriculture/valid/`.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: fixtures" src="https://img.shields.io/badge/root-fixtures%2F-6f42c1">
  <img alt="Domain: agriculture" src="https://img.shields.io/badge/domain-agriculture-success">
  <img alt="Lane: valid" src="https://img.shields.io/badge/lane-valid-success">
  <img alt="Authority: fixture only" src="https://img.shields.io/badge/authority-fixture%20only-critical">
  <img alt="Inventory: needs verification" src="https://img.shields.io/badge/inventory-NEEDS%20VERIFICATION-orange">
</p>

**Path:** `fixtures/domains/agriculture/valid/README.md`  
**Fixture posture:** Agriculture-domain valid fixture lane  
**Authority posture:** fixture only; schema authority, policy authority, source truth, catalog truth, lifecycle promotion, release approval, and public layer authority remain in their owning roots  
**Quick links:** [Purpose](#purpose) · [Placement basis](#placement-basis) · [What valid means here](#what-valid-means-here) · [Accepted valid material](#accepted-valid-material) · [Authority boundary](#authority-boundary) · [Expected layout](#expected-layout) · [Maintenance checklist](#maintenance-checklist) · [Status notes](#status-notes) · [Evidence ledger](#evidence-ledger)

> [!IMPORTANT]
> Files under this directory are expected to pass a bounded schema, validator, policy-helper, or fixture-specific check. They are not canonical records, EvidenceBundles, PolicyDecisions, ReleaseManifests, published layers, review approval, release approval, or publication authority.

---

## Purpose

This directory is for Agriculture positive fixtures.

Use this lane for small, public-safe examples that should pass Agriculture validators, schema checks, policy helpers, catalog guards, aggregation gates, source-role checks, or release-safety prechecks. The goal is to keep accepted examples explicit and reviewable without letting test examples become normalized domain records.

A passing positive test proves only that the expected shape or helper condition passed. It does not prove a source, crop, field, stress, yield, irrigation, economy, suitability, soil relation, moisture context, or aggregation claim is true.

---

## Placement basis

Agriculture's canonical path guide includes `fixtures/domains/agriculture/` in the Agriculture responsibility-root lane fan. That guide also marks Agriculture-specific path realizations as proposed until verified, so this README documents the observed requested valid fixture lane without claiming complete implementation maturity.

Agriculture lifecycle guidance keeps fixtures separate from lifecycle stores:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Valid fixtures sit outside that lifecycle. They may test that good payloads pass, but they must not hold canonical source exports, promoted catalog records, release candidates, or published artifacts.

---

## What valid means here

`valid` means valid for a **specific test expectation**, not universally true or publishable.

| Valid for | Meaning | Not implied |
|---|---|---|
| Schema | The fixture matches a machine-checkable shape. | The claim is true, sourced, reviewed, or releasable. |
| Validator | The fixture satisfies the validator case being tested. | All domain gates have closed. |
| Policy helper | The fixture produces the expected allow/answer/hold/deny helper output. | Human review or release approval. |
| Catalog helper | The fixture has enough fields for a catalog-shaped transformation. | Canonical catalog admission. |
| Source-role helper | The fixture preserves source-role semantics for the case. | Source admission or source freshness. |
| Release precheck | The fixture has release-shaped fields for a test. | `PUBLISHED` transition or signed release. |

A fixture should document which kind of validity it is testing. If that cannot be stated, keep the fixture out of this lane until the consuming test is known.

---

## Accepted valid material

This directory may contain:

| Material | Use |
|---|---|
| `valid_<n>.json` | Positive Agriculture-domain examples expected to pass a schema, validator, policy helper, or helper check. |
| `*.valid.json` | Named positive cases when the consuming test uses case-specific filenames. |
| `*.input.json` | Positive input payloads for deterministic helper tests. |
| `*.expected.json` | Expected successful output for policy-helper or snapshot-style tests. |
| local README files | Fixture intent, inventory, and authority-boundary documentation. |

Good valid cases include aggregate-safe catalog-shaped examples, source-role-preserving examples, evidence/citation-shaped examples, redacted or generalized public-safe examples, and release-precheck examples that include required review/rollback placeholders without claiming approval.

Use synthetic, minimized examples. Do not include real operational records, source-system exports, large rasters, release candidates, published artifacts, or release-blocked material.

---

## Authority boundary

| Responsibility | Owning root | This README posture |
|---|---|---|
| Agriculture valid fixtures | `fixtures/domains/agriculture/valid/` | Documents expected positive examples only. |
| Agriculture invalid fixtures | `fixtures/domains/agriculture/invalid/` | Sibling negative lane; expected failures live there. |
| Agriculture object meaning | `contracts/domains/agriculture/` | Referenced, not replaced. |
| Machine-checkable Agriculture shape | `schemas/contracts/v1/domains/agriculture/` | Referenced, not duplicated. |
| Agriculture domain policy | `policy/domains/agriculture/` | Out of scope; fixtures may test it but do not define it. |
| Sensitivity and release policy | `policy/sensitivity/`, `policy/release/` | Out of scope. |
| Canonical lifecycle data | `data/raw/`, `data/work/`, `data/quarantine/`, `data/processed/`, `data/catalog/`, `data/triplet/`, `data/published/` | Out of scope; do not duplicate as fixtures. |
| Source registry records | `data/registry/sources/` | Out of scope. |
| Tests and validation proof | `tests/domains/agriculture/` and validator tooling | Referenced, not claimed as run. |

Do not collapse this valid fixture lane into policy authority, sensitivity authority, source truth, catalog authority, release approval, or public-client permission.

---

## Expected layout

Use the smallest structure that matches the actual test need:

```text
fixtures/domains/agriculture/valid/
  README.md
  valid_1.json
```

For grouped cases, prefer subdirectories with local READMEs:

```text
fixtures/domains/agriculture/valid/
  README.md
  aggregate_catalog/
    README.md
    valid_1.json
  source_role_preserved/
    README.md
    valid_1.json
  public_safe_output/
    README.md
    valid_1.json
```

For snapshot-style positive tests, clearly document the consuming test or helper and whether the expected output represents schema success, policy success, helper output, catalog output, or release-precheck output.

---

## Maintenance checklist

Before adding or changing Agriculture valid fixtures:

- [ ] Confirm whether the pass condition is schema-style, validator-style, policy-style, catalog-helper, release-helper, or snapshot-style.
- [ ] Keep each fixture tied to a consuming test, validator, or helper.
- [ ] Keep examples synthetic, small, deterministic, public-safe, and reviewable.
- [ ] Preserve source-role, rights, sensitivity, review, receipt, release, and EvidenceBundle expectations in fixture intent.
- [ ] Keep exact exposure and private-adjacent joins fail-closed unless an explicit reviewed policy path says otherwise.
- [ ] Do not include source-system exports, large rasters, canonical records, release candidates, or release-blocked material.
- [ ] Update this README when fixtures, validators, schemas, policy tests, or helper scripts are added.
- [ ] Run the relevant tests or validators before claiming validation success.

---

## Status notes

| Item | Status | Notes |
|---|---:|---|
| Target README | CONFIRMED UPDATED | This path existed as a blank file before this update. |
| Direct valid payload inventory | NEEDS VERIFICATION | Repo search did not surface confirmed valid payload files in this directory during this update. |
| Sibling invalid lane | CONFIRMED | `../invalid/README.md` exists and documents negative fixture posture. |
| Placement | CONFIRMED PATH / PROPOSED LANE REALIZATION | The requested path exists; Agriculture path doctrine includes `fixtures/domains/agriculture/` but marks Agriculture-specific lanes as proposed until verified. |
| Lifecycle boundary | CONFIRMED DOC | Agriculture lifecycle guidance separates fixtures from governed lifecycle state and public release. |
| Test execution | NOT RUN | No validators, pytest, policy checks, source admission checks, catalog checks, release checks, or CI were run during this README update. |

---

## Evidence ledger

| Source | Status | Supports | Limits |
|---|---|---|---|
| Previous target file | CONFIRMED | Target existed as a blank file. | Did not define Agriculture valid fixture guidance. |
| Repository search for Agriculture valid fixtures | CONFIRMED SEARCH / NO MATCH | No confirmed valid payload file was found for this directory in this update. | Search is not a full recursive filesystem listing. |
| `../invalid/README.md` | CONFIRMED | Sibling negative fixture lane and shared fixture-only authority boundary. | Does not prove valid fixture payloads exist. |
| `../../../../docs/domains/agriculture/CANONICAL_PATHS.md` | CONFIRMED DOC / PROPOSED PATH REALIZATION | Agriculture lane fan includes `fixtures/domains/agriculture/` and separates responsibility roots. | Agriculture-specific path realizations remain proposed until verified. |
| `../../../../docs/domains/agriculture/DATA_LIFECYCLE.md` | CONFIRMED DOC | Agriculture lifecycle invariant, aggregate-default posture, field-level deny-by-default posture, and lifecycle-gate framing. | It is lifecycle guidance, not fixture inventory or validator proof. |
| `../../../../docs/doctrine/directory-rules.md` | CONFIRMED doctrine | File placement encodes ownership/governance/lifecycle; `tests/` and `fixtures/` are validate/operate roots. | Specific fixture completeness requires inventory and tests. |

[Back to top](#top)
