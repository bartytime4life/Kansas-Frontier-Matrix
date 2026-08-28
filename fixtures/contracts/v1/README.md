<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://fixture/contracts/v1/readme
title: contract fixtures v1 README
type: fixture-readme
version: v0.1.0
status: draft
owners: TODO(owner): schema steward; TODO(owner): contract steward; TODO(owner): fixture steward; TODO(owner): validator steward; TODO(owner): policy steward; TODO(owner): docs steward
created: NEEDS VERIFICATION - blank file existed before 2026-07-01 expansion
updated: 2026-07-01
policy_label: public-review
related:
  - common/README.md
  - evidence/README.md
  - governance/README.md
  - policy/README.md
  - runtime/README.md
  - source/README.md
  - ../../../schemas/contracts/v1/
  - ../../../contracts/
  - ../../../policy/
  - ../../../tests/schemas/test_common_contracts.py
  - ../../../docs/doctrine/directory-rules.md
tags: [kfm, fixtures, contracts, v1, schema-fixtures, valid-fixtures, invalid-fixtures, snapshot-fixtures, json-schema, common, evidence, governance, policy, runtime, source, non-authoritative]
notes:
  - "This README replaces a blank file at `fixtures/contracts/v1/README.md`."
  - "This directory groups observed v1 contract fixture family roots under `fixtures/contracts/v1/`."
  - "Observed README-covered family roots in this documentation pass are `common`, `evidence`, `governance`, `policy`, `runtime`, and `source`."
  - "The common schema harness also names a `release` family, but a `fixtures/contracts/v1/release/README.md` file was not found during this update, so release fixture coverage remains NEEDS VERIFICATION."
  - "Some child families are partial inventories or have known drift notes; this parent index preserves those limits instead of flattening them."
  - "No tests, validators, policy checks, source admission checks, runtime checks, release checks, or CI jobs were run during this documentation update."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Contract fixtures v1

Top-level index for KFM v1 contract fixtures under `fixtures/contracts/v1/`.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: fixtures" src="https://img.shields.io/badge/root-fixtures%2F-6f42c1">
  <img alt="Contracts: v1" src="https://img.shields.io/badge/contracts-v1-blue">
  <img alt="Authority: fixture only" src="https://img.shields.io/badge/authority-fixture%20only-critical">
  <img alt="Inventory: partial" src="https://img.shields.io/badge/inventory-partial-orange">
  <img alt="Harness: schema fixtures" src="https://img.shields.io/badge/harness-schema__fixtures-informational">
</p>

**Path:** `fixtures/contracts/v1/README.md`  
**Root posture:** v1 contract fixture-family index  
**Authority posture:** fixture only; contract meaning, schema shape, policy, registry records, lifecycle data, runtime behavior, release decisions, receipts, and proofs remain in their owning roots  
**Quick links:** [Purpose](#purpose) · [Observed family roots](#observed-family-roots) · [Harness behavior](#harness-behavior) · [Authority boundary](#authority-boundary) · [Known exceptions and drift](#known-exceptions-and-drift) · [Maintenance checklist](#maintenance-checklist) · [Status notes](#status-notes) · [Evidence ledger](#evidence-ledger)

> [!IMPORTANT]
> Files under this root are fixture inputs or expected-output snapshots. They are not semantic contracts, schema authority, executable policy, source truth, evidence closure, runtime truth, review approval, release approval, or publication authority.

---

## Purpose

This directory groups KFM v1 contract fixtures by contract family.

Use this root to keep fixture families discoverable, reviewable, and aligned with the common schema fixture harness. A fixture can show that a schema accepts a positive example or rejects a negative example. It cannot make a claim true, approve a source, execute policy, certify a runtime response, resolve evidence, admit a release, or authorize public publication.

---

## Observed family roots

| Family root | Current child coverage | Style | Status |
|---|---|---|---|
| [`common/`](common/README.md) | `spec_hash/` verified by the family README. | JSON Schema valid/invalid fixtures. | PARTIAL / CONFIRMED WHERE FETCHED |
| [`evidence/`](evidence/README.md) | `evidence_bundle/` and `evidence_ref/` verified by the family README. | JSON Schema valid/invalid fixtures. | PARTIAL / CONFIRMED WHERE FETCHED |
| [`governance/`](governance/README.md) | `review_record/` populated; `promotion_decision/` and `redaction_receipt/` not confirmed as populated there. | JSON Schema valid/invalid fixtures. | PARTIAL / NEEDS VERIFICATION FOR UNPOPULATED SCHEMAS |
| [`policy/`](policy/README.md) | `policy_decision/`; `sensitivity_label/` also has a child README but the policy parent may need refresh to reflect it. | JSON Schema valid/invalid fixtures. | PARTIAL / PARENT REFRESH NEEDED |
| [`runtime/`](runtime/README.md) | `ai_receipt/`, `decision_envelope/`, `run_receipt/`, and `runtime_response_envelope/` README-covered. | JSON Schema valid/invalid fixtures. | PARTIAL / CONFIRMED WHERE FETCHED |
| [`source/`](source/README.md) | Five observed child families including one snapshot-style provenance family. | Mixed: schema fixtures and policy-test snapshots. | PARTIAL / NONSTANDARD CHILD STYLE PRESENT |
| `release/` | No `fixtures/contracts/v1/release/README.md` was found by direct fetch during this update. | UNKNOWN. | NEEDS VERIFICATION |

---

## Harness behavior

The common schema fixture harness currently names these families:

```text
evidence, runtime, common, policy, source, governance, release
```

For each schema discovered under:

```text
schemas/contracts/v1/<family>/*.schema.json
```

it derives a fixture directory at:

```text
fixtures/contracts/v1/<family>/<schema_name>/
```

Expected schema-fixture behavior:

| Fixture pattern | Expected result |
|---|---|
| `valid/valid_*.json` | no JSON Schema errors |
| `invalid/invalid_*.json` | at least one JSON Schema error |
| `invalid/invalid_*.expected_error.txt` | expected text appears in combined schema error messages |

This README documents organization and known limits only. It does not claim that the harness, validators, CI, policy checks, source admission checks, runtime checks, evidence checks, release checks, or dedicated validators were run during this update.

---

## Authority boundary

| Responsibility | Owning root | This README posture |
|---|---|---|
| Fixture examples and expected-output snapshots | `fixtures/contracts/v1/` | Indexes observed fixture roots only. |
| Machine-checkable schema shape | `schemas/contracts/v1/` | Referenced, not duplicated. |
| Semantic contract meaning | `contracts/` | Referenced, not replaced. |
| Executable policy and admissibility rules | `policy/` | Out of scope. |
| Source registry records | `data/registry/` | Out of scope. |
| Lifecycle source/material data | `data/raw/`, `data/work/`, `data/quarantine/`, `data/processed/`, `data/catalog/`, `data/triplet/`, `data/published/` | Out of scope. |
| Runtime/API behavior | `runtime/`, `apps/`, `packages/`, and governed API surfaces | Out of scope. |
| Release decisions and manifests | `release/` | Out of scope. |
| Enforceability proof | `tests/` and validator tooling | Referenced, not claimed as run. |

Do not collapse this fixture root into contract authority, schema authority, policy authority, operational truth, source truth, EvidenceBundle authority, runtime truth, release approval, or public-client permission.

---

## Known exceptions and drift

| Item | Status | Notes |
|---|---:|---|
| Top-level inventory | PARTIAL | This README indexes family roots observed through fetched family READMEs and direct checks, not a full recursive repository listing. |
| `source/doctrine_artifact_provenance_check/` | NONSTANDARD STYLE | This child family is documented as policy-test expected-output snapshots rather than conventional JSON Schema fixtures. |
| `source/source_descriptor/` fixture root | NEEDS VERIFICATION | The source family README notes the schema metadata points to `tests/fixtures/sources/source_descriptor/` while observed fixtures live under `fixtures/contracts/v1/source/source_descriptor/`. |
| `policy/README.md` vs `policy/sensitivity_label/README.md` | PARENT REFRESH NEEDED | The policy parent still records `sensitivity_label` as not confirmed, while a child README for `sensitivity_label/` was fetched and confirms populated fixtures. |
| `release/` family | NEEDS VERIFICATION | The harness names `release`, but a parent release fixture README was not found by direct fetch in this update. |
| Validator status | NEEDS VERIFICATION | Family READMEs may reference validator paths, but validators were not run here. |

---

## Maintenance checklist

Before changing this root:

- [ ] Keep family roots aligned with the harness family names where practical.
- [ ] Keep schema-style fixtures under `fixtures/contracts/v1/<family>/<schema_name>/`.
- [ ] Keep passing examples under `valid/valid_<n>.json`.
- [ ] Keep failing examples under `invalid/invalid_<n>.json`.
- [ ] Keep expected-error text beside the invalid fixture it describes.
- [ ] Mark snapshot-style fixture families explicitly when they do not use the common schema-fixture pattern.
- [ ] Preserve the split between fixtures, schemas, contracts, policy, source registry records, lifecycle data, runtime behavior, release decisions, and tests.
- [ ] Keep fixture examples public-safe and limited to metadata-shaped examples or expected-output snapshots.
- [ ] Avoid private, unpublished, source-system, prompt-like, or policy-restricted content.
- [ ] Do not embed full source payloads or release-blocked material in fixtures.
- [ ] Update this parent README when a fixture family is added, retired, renamed, migrated, or converted between schema and snapshot styles.
- [ ] Run the relevant schema or policy tests before claiming validation success.

---

## Status notes

| Item | Status | Notes |
|---|---:|---|
| Target README | CONFIRMED UPDATED | This path existed as a blank file before this update. |
| Observed family roots | PARTIALLY CONFIRMED | `common`, `evidence`, `governance`, `policy`, `runtime`, and `source` have fetched family README evidence. |
| Harness family list | CONFIRMED / NOT RUN | The common schema fixture harness includes `evidence`, `runtime`, `common`, `policy`, `source`, `governance`, and `release`. |
| Release fixture root | NEEDS VERIFICATION | Direct fetch of `fixtures/contracts/v1/release/README.md` returned not found during this update. |
| Test execution | NOT RUN | No validators, pytest, policy checks, source admission checks, runtime checks, evidence checks, release checks, or CI were run during this README update. |

---

## Evidence ledger

| Source | Status | Supports | Limits |
|---|---|---|---|
| Previous target file | CONFIRMED | Target existed as a blank file. | Did not define v1 fixture-root guidance. |
| [`common/README.md`](common/README.md) | CONFIRMED | Common fixture parent and `spec_hash/` inventory posture. | Inventory is partial per its own README. |
| [`evidence/README.md`](evidence/README.md) | CONFIRMED | Evidence fixture parent and `evidence_bundle/` / `evidence_ref/` inventory posture. | Inventory is partial per its own README. |
| [`governance/README.md`](governance/README.md) | CONFIRMED | Governance fixture parent and `review_record/` populated-family posture. | Some governance schemas are not confirmed as populated there. |
| [`policy/README.md`](policy/README.md) | CONFIRMED | Policy fixture parent and `policy_decision/` inventory posture. | Parent appears stale for `sensitivity_label/` based on fetched child README. |
| [`policy/sensitivity_label/README.md`](policy/sensitivity_label/README.md) | CONFIRMED | `sensitivity_label/` child fixture family exists and is populated. | Parent policy README may need refresh. |
| [`runtime/README.md`](runtime/README.md) | CONFIRMED | Runtime fixture parent and four README-covered child families. | It does not claim every runtime schema has complete coverage. |
| [`source/README.md`](source/README.md) | CONFIRMED | Source fixture parent, five observed child families, snapshot-style exception, and source descriptor fixture-root mismatch. | Inventory is partial and includes a nonstandard child style. |
| `../../../tests/schemas/test_common_contracts.py` | CONFIRMED / NOT RUN | Harness family list and fixture discovery behavior. | Tests were not run during this update. |
| `../../../docs/doctrine/directory-rules.md` | CONFIRMED doctrine | `fixtures/` is the validate/operate root for test inputs while contracts, schemas, policy, registry, lifecycle data, and release decisions remain separate roots. | Specific fixture completeness requires inventory and tests. |

[Back to top](#top)
