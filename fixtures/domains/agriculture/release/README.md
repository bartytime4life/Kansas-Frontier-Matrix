<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://fixture/domains/agriculture/release/readme
title: Agriculture release fixtures README
type: fixture-readme
version: v0.1.0
status: draft
owners: TODO(owner): agriculture domain steward; TODO(owner): release steward; TODO(owner): fixture steward; TODO(owner): validation steward; TODO(owner): policy steward; TODO(owner): docs steward
created: NEEDS VERIFICATION - blank file existed before 2026-07-01 expansion
updated: 2026-07-01
policy_label: public-review
related:
  - ../catalog/README.md
  - ../golden/README.md
  - ../invalid/README.md
  - ../field_level_attempt/README.md
  - ../../../../docs/runbooks/agriculture/PROMOTION_RUNBOOK.md
  - ../../../../docs/domains/agriculture/RELEASE_INDEX.md
  - ../../../../docs/domains/agriculture/CANONICAL_PATHS.md
  - ../../../../docs/domains/agriculture/DATA_LIFECYCLE.md
  - ../../../../policy/domains/agriculture/README.md
  - ../../../../contracts/domains/agriculture/
  - ../../../../schemas/contracts/v1/domains/agriculture/
  - ../../../../release/candidates/agriculture/
  - ../../../../release/manifests/
  - ../../../../data/published/layers/agriculture/
  - ../../../../tests/domains/agriculture/
  - ../../../../docs/doctrine/directory-rules.md
tags: [kfm, fixtures, domains, agriculture, release-fixtures, release-candidate, release-manifest, promotion-decision, rollback, correction, policy-gate, non-authoritative]
notes:
  - "This README replaces a blank file at `fixtures/domains/agriculture/release/README.md`."
  - "This directory is for Agriculture release-shaped fixtures only, not release decisions, release manifests, published layers, or public authorization."
  - "Repo search did not surface confirmed payload files in this directory during this update, so fixture inventory remains NEEDS VERIFICATION."
  - "Agriculture release fixtures must preserve promotion as a governed state transition, not a file move."
  - "No tests, validators, policy checks, release checks, signing checks, catalog checks, or CI jobs were run during this documentation update."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Agriculture release fixtures

Fixture lane for Agriculture release-shaped examples under `fixtures/domains/agriculture/release/`.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: fixtures" src="https://img.shields.io/badge/root-fixtures%2F-6f42c1">
  <img alt="Domain: agriculture" src="https://img.shields.io/badge/domain-agriculture-success">
  <img alt="Lane: release" src="https://img.shields.io/badge/lane-release-blue">
  <img alt="Authority: fixture only" src="https://img.shields.io/badge/authority-fixture%20only-critical">
  <img alt="Inventory: needs verification" src="https://img.shields.io/badge/inventory-NEEDS%20VERIFICATION-orange">
</p>

**Path:** `fixtures/domains/agriculture/release/README.md`  
**Fixture posture:** Agriculture-domain release-shaped fixture lane  
**Authority posture:** fixture only; release decisions, release manifests, signatures, rollback targets, policy authority, lifecycle promotion, and published artifacts remain in their owning roots  
**Quick links:** [Purpose](#purpose) · [Placement basis](#placement-basis) · [Release boundary](#release-boundary) · [Accepted fixture material](#accepted-fixture-material) · [Authority boundary](#authority-boundary) · [Expected layout](#expected-layout) · [Maintenance checklist](#maintenance-checklist) · [Status notes](#status-notes) · [Evidence ledger](#evidence-ledger)

> [!IMPORTANT]
> Files under this directory are test inputs or expected-output examples. They are not `ReleaseManifest` authority, `PromotionDecision` authority, signatures, rollback authority, published layers, review approval, release approval, or publication authority.

---

## Purpose

This directory is for small, public-safe Agriculture release fixtures.

Use this lane when tests, validators, policy helpers, catalog helpers, or release-helper code need release-shaped Agriculture examples without reading actual release manifests, promotion decisions, published artifacts, or lifecycle stores. A fixture may exercise expected manifest shape, policy-gate input, rollback target shape, signed-output expectations, or failure cases.

A passing fixture proves only the bounded test expectation for that fixture. It does not prove an Agriculture object is ready to publish, a release manifest was approved, a signature is valid, or a public layer may be rendered.

---

## Placement basis

Agriculture's canonical path guide includes `fixtures/domains/agriculture/` in the Agriculture responsibility-root lane fan. Agriculture promotion guidance states that promotion is a governed state transition, not a file move, and release-shaped objects must pass evidence, policy, catalog, review, signature, and rollback gates before publication.

The governed lifecycle remains separate from this fixture lane:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Release fixtures sit outside that lifecycle. Actual release decisions live under release roots. Actual published Agriculture artifacts live under governed published-data roots. This fixture lane may model release-shaped payloads for tests, but it cannot authorize release.

---

## Release boundary

Agriculture promotion guidance identifies a release stage with public-safe artifacts, `ReleaseManifest`, signatures, and rollback target. It also identifies a release gate that checks proof, correction path, rollback target, and review state.

For fixtures in this lane, preserve these rules:

| Rule | Fixture meaning |
|---|---|
| Promotion is governed | Fixture success is not promotion. |
| Release manifest is authority-bearing elsewhere | Fixture examples may model shape but do not approve release. |
| Evidence and catalog closure matter | Release-shaped examples should include evidence and catalog expectations when relevant. |
| Policy gates can deny or hold | Negative fixtures should cover missing rights, evidence, review, rollback, or sensitivity disposition. |
| Signatures are integrity, not authorization | A signature-shaped fixture does not override missing governance fields. |
| Published artifacts live elsewhere | Do not copy published layers or release candidates into this fixture lane. |

---

## Accepted fixture material

This directory may contain:

| Material | Use |
|---|---|
| `*.input.json` | Small release-shaped Agriculture input examples for validators or policy helpers. |
| `*.expected.json` | Expected policy, validation, or release-helper output. |
| `*.snapshot.json` | Snapshot-style expected output when the consuming test documents snapshot semantics. |
| `valid/valid_<n>.json` | Positive schema examples when a release-shaped schema or validator is wired. |
| `invalid/invalid_<n>.json` | Negative examples for missing evidence, missing review, missing rollback target, unresolved rights, unresolved sensitivity, or catalog-closure failure. |
| `invalid/invalid_<n>.expected_error.txt` | Expected validation or policy reason text for negative examples. |
| local README files | Fixture intent, inventory, and authority-boundary documentation. |

Fixtures should be synthetic, deterministic, compact, public-safe, and reviewable. Prefer manifest-shaped metadata examples over real release payloads. Do not store actual release manifests, signing material, release candidates, published layers, private source data, or release-blocked material here.

---

## Authority boundary

| Responsibility | Owning root | This README posture |
|---|---|---|
| Agriculture release fixtures | `fixtures/domains/agriculture/release/` | Documents test/example inputs only. |
| Release candidates | `release/candidates/agriculture/` | Out of scope. |
| Release manifests and promotion decisions | `release/` roots | Out of scope; fixtures may model shape but do not decide release. |
| Published Agriculture layers | `data/published/layers/agriculture/` | Out of scope; do not duplicate as fixtures. |
| Agriculture object meaning | `contracts/domains/agriculture/` | Referenced, not replaced. |
| Machine-checkable Agriculture shape | `schemas/contracts/v1/domains/agriculture/` | Referenced, not duplicated. |
| Agriculture policy | `policy/domains/agriculture/` | Out of scope; fixtures may test it but do not define it. |
| Canonical lifecycle data | `data/raw/`, `data/work/`, `data/quarantine/`, `data/processed/`, `data/catalog/`, `data/triplet/`, `data/published/` | Out of scope. |
| Tests and validation proof | `tests/domains/agriculture/` and validator tooling | Referenced, not claimed as run. |

Do not collapse this fixture lane into release authority, policy authority, catalog authority, source truth, EvidenceBundle authority, signature authority, rollback authority, or public-client permission.

---

## Expected layout

Use the smallest structure that matches the actual test need:

```text
fixtures/domains/agriculture/release/
  README.md
  <case_name>.input.json
  <case_name>.expected.json
  <case_name>.snapshot.json
```

For schema-style examples, use:

```text
fixtures/domains/agriculture/release/
  valid/
    README.md
    valid_<n>.json
  invalid/
    README.md
    invalid_<n>.json
    invalid_<n>.expected_error.txt
```

For policy-helper snapshots, document whether the expected output represents pass, deny, hold, abstain, release obligation, review obligation, correction obligation, or rollback obligation.

---

## Maintenance checklist

Before adding or changing Agriculture release fixtures:

- [ ] Confirm the consuming test, validator, policy helper, or release helper.
- [ ] Confirm whether the fixture is schema-style, validator-style, policy-style, release-helper, or snapshot-style.
- [ ] Keep examples synthetic, compact, deterministic, public-safe, and reviewable.
- [ ] Preserve evidence, catalog closure, rights, sensitivity, review, receipt, release, correction, signature, and rollback expectations in fixture intent.
- [ ] Do not store signing material, actual release manifests, release candidates, published layers, source-system exports, or release-blocked material.
- [ ] Pair negative fixtures with expected error text or expected policy/release-helper output.
- [ ] Update this README when fixtures, validators, schemas, policy tests, release tests, or helper scripts are added.
- [ ] Run the relevant tests or validators before claiming validation success.

---

## Status notes

| Item | Status | Notes |
|---|---:|---|
| Target README | CONFIRMED UPDATED | This path existed as a blank file before this update. |
| Direct release payload inventory | NEEDS VERIFICATION | Repo search did not surface confirmed release fixture payload files in this directory during this update. |
| Placement | CONFIRMED PATH / PROPOSED LANE REALIZATION | The requested path exists; Agriculture path doctrine includes `fixtures/domains/agriculture/` but marks Agriculture-specific lanes as proposed until verified. |
| Release authority | NOT AUTHORIZED BY THIS README | This README does not approve release, publication, signing, rollback, or public rendering. |
| Test execution | NOT RUN | No validators, pytest, policy checks, release checks, signing checks, catalog checks, or CI were run during this README update. |

---

## Evidence ledger

| Source | Status | Supports | Limits |
|---|---|---|---|
| Previous target file | CONFIRMED | Target existed as a blank file. | Did not define Agriculture release fixture guidance. |
| Repository search for Agriculture release fixtures | CONFIRMED SEARCH / NO PAYLOAD MATCH | Search surfaced planning documentation, not confirmed payload files under this fixture lane. | Search is not a full recursive filesystem listing. |
| `../../../../docs/runbooks/agriculture/PROMOTION_RUNBOOK.md` | CONFIRMED DOC / PROPOSED WIRING | Promotion is governed, not a file move; release needs manifest, proof, policy gate, signatures, rollback, and review posture. | The runbook marks repo-state items as PROPOSED / NEEDS VERIFICATION and was not executed. |
| `../../../../docs/domains/agriculture/CANONICAL_PATHS.md` | CONFIRMED DOC / PROPOSED PATH REALIZATION | Agriculture lane fan includes `fixtures/domains/agriculture/` and separates responsibility roots. | Agriculture-specific path realizations remain proposed until verified. |
| `../../../../docs/doctrine/directory-rules.md` | CONFIRMED doctrine | File placement encodes ownership/governance/lifecycle; `tests/` and `fixtures/` are validate/operate roots. | Specific fixture completeness requires inventory and tests. |

[Back to top](#top)
