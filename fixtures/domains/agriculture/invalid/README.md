<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://fixture/domains/agriculture/invalid/readme
title: Agriculture invalid fixtures README
type: fixture-readme
version: v0.1.0
status: draft
owners: TODO(owner): agriculture domain steward; TODO(owner): fixture steward; TODO(owner): validation steward; TODO(owner): policy steward; TODO(owner): sensitivity steward; TODO(owner): docs steward
created: NEEDS VERIFICATION - blank file existed before 2026-07-01 expansion
updated: 2026-07-01
policy_label: public-review
related:
  - ../catalog/README.md
  - ../field_level_attempt/README.md
  - ../golden/README.md
  - ../hls_vi/README.md
  - ../../../../docs/domains/agriculture/CANONICAL_PATHS.md
  - ../../../../docs/domains/agriculture/DATA_LIFECYCLE.md
  - ../../../../docs/domains/agriculture/POLICY.md
  - ../../../../policy/domains/agriculture/README.md
  - ../../../../contracts/domains/agriculture/
  - ../../../../schemas/contracts/v1/domains/agriculture/
  - ../../../../policy/domains/agriculture/
  - ../../../../tests/domains/agriculture/
  - ../../../../docs/doctrine/directory-rules.md
tags: [kfm, fixtures, domains, agriculture, invalid-fixtures, negative-fixtures, expected-error, validation, policy-fixtures, sensitivity, aggregate-default, fail-closed, non-authoritative]
notes:
  - "This README replaces a blank file at `fixtures/domains/agriculture/invalid/README.md`."
  - "This directory is for Agriculture domain invalid fixtures and expected failure examples."
  - "Repo search did not surface confirmed invalid payload files in this directory during this update, so payload inventory remains NEEDS VERIFICATION."
  - "Invalid fixtures are not policy decisions, source truth, catalog authority, release approval, or publication authority."
  - "No tests, validators, policy checks, source admission checks, catalog checks, release checks, or CI jobs were run during this documentation update."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Agriculture invalid fixtures

Domain-level negative fixture lane for Agriculture examples under `fixtures/domains/agriculture/invalid/`.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: fixtures" src="https://img.shields.io/badge/root-fixtures%2F-6f42c1">
  <img alt="Domain: agriculture" src="https://img.shields.io/badge/domain-agriculture-success">
  <img alt="Lane: invalid" src="https://img.shields.io/badge/lane-invalid-critical">
  <img alt="Posture: fail closed" src="https://img.shields.io/badge/posture-fail__closed-critical">
  <img alt="Authority: fixture only" src="https://img.shields.io/badge/authority-fixture%20only-critical">
</p>

**Path:** `fixtures/domains/agriculture/invalid/README.md`  
**Fixture posture:** Agriculture-domain invalid fixture lane  
**Authority posture:** fixture only; schema authority, policy authority, source truth, catalog truth, lifecycle promotion, release approval, and public layer authority remain in their owning roots  
**Quick links:** [Purpose](#purpose) · [Placement basis](#placement-basis) · [Accepted invalid material](#accepted-invalid-material) · [Authority boundary](#authority-boundary) · [Expected layout](#expected-layout) · [Maintenance checklist](#maintenance-checklist) · [Status notes](#status-notes) · [Evidence ledger](#evidence-ledger)

> [!IMPORTANT]
> Files under this directory are expected to fail validation, policy, safety, or fixture-specific checks. They are not canonical records, EvidenceBundles, PolicyDecisions, ReleaseManifests, published layers, review approval, release approval, or publication authority.

---

## Purpose

This directory is for Agriculture negative fixtures.

Use this lane for small, public-safe examples that should be rejected by Agriculture validators, schema checks, policy helpers, catalog guards, aggregation gates, source-role checks, or release-safety checks. The goal is to keep failure cases explicit and reviewable without letting rejected examples become normalized domain records.

A passing negative test proves only that the expected failure was detected. It does not prove a source, crop, field, stress, yield, irrigation, economy, suitability, or aggregation claim is true.

---

## Placement basis

Agriculture's canonical path guide includes `fixtures/domains/agriculture/` in the Agriculture responsibility-root lane fan. That guide also marks Agriculture-specific path realizations as proposed until verified, so this README documents the observed requested invalid fixture lane without claiming complete implementation maturity.

Agriculture lifecycle guidance keeps fixtures separate from lifecycle stores:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Invalid fixtures sit outside that lifecycle. They may test that bad payloads fail, but they must not hold canonical source exports, promoted catalog records, release candidates, or published artifacts.

---

## Accepted invalid material

This directory may contain:

| Material | Use |
|---|---|
| `invalid_<n>.json` | Negative Agriculture-domain examples expected to fail a schema, validator, policy, or helper check. |
| `invalid_<n>.expected_error.txt` | Expected error text, reason code, or pattern for the paired invalid fixture. |
| `*.invalid.json` | Named negative cases when the consuming test uses case-specific filenames. |
| `*.expected.json` | Expected failure payloads for policy-helper or snapshot-style tests. |
| local README files | Fixture intent, inventory, and authority-boundary documentation. |

Good invalid cases include missing required Agriculture identity, unsafe exact exposure posture, missing aggregation support, missing evidence support, missing sensitivity or release disposition, missing source-role context, or catalog-shaped examples that try to behave like canonical records.

Use synthetic, minimized examples. Do not include real operational records, source-system exports, large rasters, release candidates, or published artifacts.

---

## Authority boundary

| Responsibility | Owning root | This README posture |
|---|---|---|
| Agriculture invalid fixtures | `fixtures/domains/agriculture/invalid/` | Documents expected failure examples only. |
| Agriculture object meaning | `contracts/domains/agriculture/` | Referenced, not replaced. |
| Machine-checkable Agriculture shape | `schemas/contracts/v1/domains/agriculture/` | Referenced, not duplicated. |
| Agriculture domain policy | `policy/domains/agriculture/` | Out of scope; fixtures may test it but do not define it. |
| Sensitivity and release policy | `policy/sensitivity/`, `policy/release/` | Out of scope. |
| Canonical lifecycle data | `data/raw/`, `data/work/`, `data/quarantine/`, `data/processed/`, `data/catalog/`, `data/triplet/`, `data/published/` | Out of scope; do not duplicate as fixtures. |
| Source registry records | `data/registry/sources/` | Out of scope. |
| Tests and validation proof | `tests/domains/agriculture/` and validator tooling | Referenced, not claimed as run. |

Do not collapse this invalid fixture lane into policy authority, sensitivity authority, source truth, catalog authority, release approval, or public-client permission.

---

## Expected layout

Use the smallest structure that matches the actual test need:

```text
fixtures/domains/agriculture/invalid/
  README.md
  invalid_1.json
  invalid_1.expected_error.txt
```

For grouped cases, prefer subdirectories with local READMEs:

```text
fixtures/domains/agriculture/invalid/
  README.md
  missing_evidence/
    README.md
    invalid_1.json
    invalid_1.expected_error.txt
  unsafe_public_output/
    README.md
    invalid_1.json
    invalid_1.expected_error.txt
```

For snapshot-style negative tests, clearly document the consuming test or helper and whether the expected output represents schema errors, policy decisions, reason codes, or helper payloads.

---

## Maintenance checklist

Before adding or changing Agriculture invalid fixtures:

- [ ] Confirm whether the failure is schema-style, validator-style, policy-style, or snapshot-style.
- [ ] Pair each invalid fixture with expected error text or an expected failure payload.
- [ ] Keep examples synthetic, small, deterministic, public-safe, and reviewable.
- [ ] Keep exact exposure and private-adjacent joins fail-closed unless an explicit reviewed policy path says otherwise.
- [ ] Preserve source-role, rights, sensitivity, review, receipt, release, and EvidenceBundle expectations in fixture intent.
- [ ] Do not include source-system exports, large rasters, canonical records, release candidates, or release-blocked material.
- [ ] Update this README when fixtures, validators, schemas, policy tests, or helper scripts are added.
- [ ] Run the relevant tests or validators before claiming validation success.

---

## Status notes

| Item | Status | Notes |
|---|---:|---|
| Target README | CONFIRMED UPDATED | This path existed as a blank file before this update. |
| Direct invalid payload inventory | NEEDS VERIFICATION | Repo search did not surface confirmed invalid payload files in this directory during this update. |
| Placement | CONFIRMED PATH / PROPOSED LANE REALIZATION | The requested path exists; Agriculture path doctrine includes `fixtures/domains/agriculture/` but marks Agriculture-specific lanes as proposed until verified. |
| Policy posture | CONFIRMED DOC / RUNTIME UNKNOWN | Agriculture policy and lifecycle docs support fail-closed exact exposure and aggregate-safe public posture; runtime enforcement was not tested. |
| Test execution | NOT RUN | No validators, pytest, policy checks, source admission checks, catalog checks, release checks, or CI were run during this README update. |

---

## Evidence ledger

| Source | Status | Supports | Limits |
|---|---|---|---|
| Previous target file | CONFIRMED | Target existed as a blank file. | Did not define Agriculture invalid fixture guidance. |
| Repository search for Agriculture invalid fixtures | CONFIRMED SEARCH / NO MATCH | No confirmed invalid payload file was found for this directory in this update. | Search is not a full recursive filesystem listing. |
| `../../../../docs/domains/agriculture/CANONICAL_PATHS.md` | CONFIRMED DOC / PROPOSED PATH REALIZATION | Agriculture lane fan includes `fixtures/domains/agriculture/` and separates responsibility roots. | Agriculture-specific path realizations remain proposed until verified. |
| `../../../../docs/domains/agriculture/DATA_LIFECYCLE.md` | CONFIRMED DOC | Agriculture lifecycle invariant, aggregate-default posture, field-level deny-by-default posture, and load-bearing aggregation framing. | It is lifecycle guidance, not fixture inventory or validator proof. |
| `../../../../policy/domains/agriculture/README.md` | CONFIRMED DOC / RUNTIME UNKNOWN | Agriculture policy lane scope includes field/operator exposure, aggregate-only gates, and failure-closed exact exposure posture. | Concrete policy files, tests, fixtures, CI binding, and runtime enforcement remain NEEDS VERIFICATION in that README. |
| `../../../../docs/doctrine/directory-rules.md` | CONFIRMED doctrine | File placement encodes ownership/governance/lifecycle; `tests/` and `fixtures/` are validate/operate roots. | Specific fixture completeness requires inventory and tests. |

[Back to top](#top)
