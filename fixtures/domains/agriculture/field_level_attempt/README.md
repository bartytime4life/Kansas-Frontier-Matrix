<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://fixture/domains/agriculture/field-level-attempt/readme
title: Agriculture field-level attempt fixtures README
type: fixture-readme
version: v0.1.0
status: draft
owners: TODO(owner): agriculture domain steward; TODO(owner): fixture steward; TODO(owner): policy steward; TODO(owner): sensitivity steward; TODO(owner): validation steward; TODO(owner): docs steward
created: NEEDS VERIFICATION - blank file existed before 2026-07-01 expansion
updated: 2026-07-01
policy_label: public-review
related:
  - ../../../../docs/domains/agriculture/DATA_LIFECYCLE.md
  - ../../../../docs/domains/agriculture/CANONICAL_PATHS.md
  - ../../../../docs/domains/agriculture/POLICY.md
  - ../../../../policy/domains/agriculture/README.md
  - ../../../../policy/sensitivity/
  - ../../../../policy/release/
  - ../../../../schemas/contracts/v1/domains/agriculture/
  - ../../../../contracts/domains/agriculture/
  - ../../../../tests/domains/agriculture/
  - ../../../../docs/doctrine/directory-rules.md
tags: [kfm, fixtures, domains, agriculture, field-level-attempt, negative-fixtures, policy-fixtures, sensitivity, deny-by-default, exact-exposure, aggregate-default, fail-closed, non-authoritative]
notes:
  - "This README replaces a blank file at `fixtures/domains/agriculture/field_level_attempt/README.md`."
  - "This directory is for field-level Agriculture attempt fixtures, especially negative or fail-closed examples for exact exposure and private-adjacent joins."
  - "No direct fixture payloads were found or inspected in this directory during this update, so fixture inventory remains NEEDS VERIFICATION."
  - "The README is grounded in Agriculture's aggregate-default and field-level deny-by-default posture."
  - "No tests, validators, policy checks, source admission checks, release checks, or CI jobs were run during this documentation update."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Agriculture field-level attempt fixtures

Fixture lane for Agriculture field-level attempt examples under `fixtures/domains/agriculture/field_level_attempt/`.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: fixtures" src="https://img.shields.io/badge/root-fixtures%2F-6f42c1">
  <img alt="Domain: agriculture" src="https://img.shields.io/badge/domain-agriculture-success">
  <img alt="Lane: field-level attempt" src="https://img.shields.io/badge/lane-field__level__attempt-blue">
  <img alt="Default: deny exact exposure" src="https://img.shields.io/badge/default-deny__exact__exposure-critical">
  <img alt="Authority: fixture only" src="https://img.shields.io/badge/authority-fixture%20only-critical">
</p>

**Path:** `fixtures/domains/agriculture/field_level_attempt/README.md`  
**Fixture posture:** Agriculture-domain policy/sensitivity fixture lane  
**Authority posture:** fixture only; executable policy, sensitivity classification, catalog truth, release approval, and public rendering authority remain in their owning roots  
**Quick links:** [Purpose](#purpose) · [Placement basis](#placement-basis) · [Accepted fixture material](#accepted-fixture-material) · [Authority boundary](#authority-boundary) · [Expected layout](#expected-layout) · [Maintenance checklist](#maintenance-checklist) · [Status notes](#status-notes) · [Evidence ledger](#evidence-ledger)

> [!IMPORTANT]
> Files under this directory are test inputs or expected-output examples for field-level Agriculture handling. They are not source truth, field records, parcel records, operator records, SourceDescriptors, EvidenceBundles, PolicyDecisions, ReleaseManifests, release approval, review approval, or publication authority.

---

## Purpose

This directory is for Agriculture fixtures that exercise field-level or exact-exposure attempts.

Use this lane for small, public-safe examples that prove field-level Agriculture attempts fail closed unless an explicitly reviewed policy path allows a transformed, aggregated, redacted, generalized, delayed, or restricted output. The expected default is conservative: aggregate-safe public products may be allowed after the correct gates, but exact field/operator/parcel-adjacent exposure must not be normalized by fixture examples.

A passing fixture proves only the bounded test expectation for that fixture. It does not prove that any field, crop, owner/operator, parcel, source, or yield claim is true.

---

## Placement basis

Agriculture's canonical path guide includes `fixtures/domains/agriculture/` in the Agriculture responsibility-root lane fan. That same guide marks Agriculture-specific path realizations as proposed until verified, so this README documents the observed requested fixture lane without claiming broader implementation maturity.

Agriculture lifecycle guidance states the governed lifecycle as:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

It also highlights public-safe aggregation discipline and field-level deny-by-default posture. This fixture lane lives outside the lifecycle stores. It may test failure-closed behavior, but it must not hold canonical field data, raw source exports, catalog records, or published artifacts.

---

## Accepted fixture material

This directory may contain:

| Material | Use |
|---|---|
| `invalid/invalid_<n>.json` | Negative examples where field-level exact exposure should be rejected. |
| `invalid/invalid_<n>.expected_error.txt` | Expected validation or policy reason text for negative examples. |
| `valid/valid_<n>.json` | Positive examples only when the payload is transformed, aggregate-safe, redacted, generalized, restricted, or otherwise explicitly policy-allowed. |
| snapshot files | Expected-output snapshots for policy helpers, if clearly marked as snapshots and tied to a test. |
| local README files | Fixture intent, inventory, and authority-boundary documentation. |

Good fixture subjects include metadata-shaped attempts such as:

- exact field geometry requested for public display;
- operator- or parcel-adjacent join attempted without policy clearance;
- row-level crop/yield observation requested as public output;
- aggregate output with a missing aggregation receipt;
- public map/API request missing required sensitivity or release disposition.

Avoid real private records, precise production field geometry, source dumps, personally identifying data, or release-blocked material. Use synthetic, minimized examples.

---

## Authority boundary

| Responsibility | Owning root | This README posture |
|---|---|---|
| Field-level attempt fixtures | `fixtures/domains/agriculture/field_level_attempt/` | Documents test/example inputs only. |
| Agriculture object meaning | `contracts/domains/agriculture/` | Referenced, not replaced. |
| Machine-checkable Agriculture shape | `schemas/contracts/v1/domains/agriculture/` | Referenced, not duplicated. |
| Agriculture executable policy | `policy/domains/agriculture/` | Out of scope; fixtures may test it but do not define it. |
| Sensitivity policy | `policy/sensitivity/` | Out of scope. |
| Release policy | `policy/release/` | Out of scope. |
| Canonical lifecycle data | `data/raw/`, `data/work/`, `data/quarantine/`, `data/processed/`, `data/catalog/`, `data/triplet/`, `data/published/` | Out of scope; do not duplicate as fixtures. |
| Tests and validation proof | `tests/domains/agriculture/` and validator tooling | Referenced, not claimed as run. |

Do not collapse this fixture lane into policy authority, sensitivity authority, source truth, catalog authority, release approval, or public-client permission.

---

## Expected layout

Use the smallest structure that matches the actual fixture need:

```text
fixtures/domains/agriculture/field_level_attempt/
  README.md
  invalid/
    README.md
    invalid_<n>.json
    invalid_<n>.expected_error.txt
  valid/
    README.md
    valid_<n>.json
```

For this lane, `invalid/` will usually be the primary lane because the fixture purpose is to preserve fail-closed behavior for exact exposure attempts. A `valid/` example should be added only when it demonstrates a policy-allowed transformed or aggregate-safe output.

---

## Maintenance checklist

Before adding or changing field-level attempt fixtures:

- [ ] Confirm whether the fixture is schema-style, policy-style, or snapshot-style.
- [ ] Prefer negative fixtures for exact exposure attempts.
- [ ] Use positive fixtures only for transformed, aggregate-safe, redacted, generalized, delayed, or restricted examples.
- [ ] Keep examples synthetic, small, deterministic, public-safe, and reviewable.
- [ ] Do not include real field geometries, operator records, person-parcel joins, raw source dumps, or release-blocked material.
- [ ] Make expected policy outcomes finite and explicit where a policy helper consumes the fixture.
- [ ] Preserve source-role, rights, sensitivity, review, receipt, and EvidenceBundle expectations in fixture intent.
- [ ] Update this README when fixtures, validators, schemas, policy tests, or helper scripts are added.
- [ ] Run the relevant tests or validators before claiming validation success.

---

## Status notes

| Item | Status | Notes |
|---|---:|---|
| Target README | CONFIRMED UPDATED | This path existed as a blank file before this update. |
| Direct fixture payload inventory | NEEDS VERIFICATION | No `valid/` or `invalid/` payload files were fetched for this lane during this update. |
| Placement | CONFIRMED PATH / PROPOSED LANE REALIZATION | The requested path exists; Agriculture path doctrine includes `fixtures/domains/agriculture/` but marks Agriculture-specific lanes as proposed until verified. |
| Policy posture | CONFIRMED DOC / RUNTIME UNKNOWN | Agriculture policy README states exact exposure must fail closed unless a reviewed policy path allows a transformed output; runtime enforcement was not tested. |
| Test execution | NOT RUN | No validators, pytest, policy checks, source admission checks, release checks, or CI were run during this README update. |

---

## Evidence ledger

| Source | Status | Supports | Limits |
|---|---|---|---|
| Previous target file | CONFIRMED | Target existed as a blank file. | Did not define field-level attempt fixture guidance. |
| `../../../../docs/domains/agriculture/DATA_LIFECYCLE.md` | CONFIRMED DOC | Agriculture lifecycle invariant, aggregate-default posture, and field-level deny-by-default framing. | It is lifecycle guidance, not fixture inventory or policy-runtime proof. |
| `../../../../docs/domains/agriculture/CANONICAL_PATHS.md` | CONFIRMED DOC / PROPOSED PATH REALIZATION | Agriculture lane fan includes `fixtures/domains/agriculture/` and separates responsibility roots. | Agriculture-specific path realizations remain proposed until verified. |
| `../../../../policy/domains/agriculture/README.md` | CONFIRMED DOC / RUNTIME UNKNOWN | Agriculture policy lane scope includes field/operator exposure, aggregate-only gates, and failure-closed exact exposure posture. | Concrete policy files, tests, fixtures, CI binding, and runtime enforcement remain NEEDS VERIFICATION in that README. |
| `../../../../docs/doctrine/directory-rules.md` | CONFIRMED doctrine | File placement encodes ownership/governance/lifecycle; `tests/` and `fixtures/` are validate/operate roots. | Specific fixture completeness requires inventory and tests. |

[Back to top](#top)
