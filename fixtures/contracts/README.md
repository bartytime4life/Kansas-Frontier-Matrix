<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://fixture/contracts/readme
title: contract fixtures README
type: fixture-readme
version: v0.1.0
status: draft
owners: TODO(owner): schema steward; TODO(owner): contract steward; TODO(owner): fixture steward; TODO(owner): validator steward; TODO(owner): policy steward; TODO(owner): docs steward
created: NEEDS VERIFICATION - blank file existed before 2026-07-01 expansion
updated: 2026-07-01
policy_label: public-review
related:
  - v1/README.md
  - ../../schemas/contracts/
  - ../../contracts/
  - ../../policy/
  - ../../tests/schemas/test_common_contracts.py
  - ../../docs/doctrine/directory-rules.md
tags: [kfm, fixtures, contracts, schema-fixtures, valid-fixtures, invalid-fixtures, snapshot-fixtures, json-schema, contract-tests, non-authoritative]
notes:
  - "This README replaces a blank file at `fixtures/contracts/README.md`."
  - "This directory is the parent index for contract fixture versions under `fixtures/contracts/`."
  - "The currently confirmed child index is `v1/README.md`."
  - "This README is not a complete recursive fixture inventory; version and family completeness require a separate listing or test run."
  - "No tests, validators, policy checks, source admission checks, runtime checks, release checks, or CI jobs were run during this documentation update."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Contract fixtures

Parent index for KFM contract fixtures under `fixtures/contracts/`.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: fixtures" src="https://img.shields.io/badge/root-fixtures%2F-6f42c1">
  <img alt="Subtree: contracts" src="https://img.shields.io/badge/subtree-contracts-blue">
  <img alt="Authority: fixture only" src="https://img.shields.io/badge/authority-fixture%20only-critical">
  <img alt="Inventory: partial" src="https://img.shields.io/badge/inventory-partial-orange">
</p>

**Path:** `fixtures/contracts/README.md`  
**Root posture:** parent index for versioned contract fixture roots  
**Authority posture:** fixture only; contract meaning, schema shape, policy, registry records, lifecycle data, runtime behavior, release decisions, receipts, and proofs remain in their owning roots  
**Quick links:** [Purpose](#purpose) · [Observed version roots](#observed-version-roots) · [Harness relationship](#harness-relationship) · [Authority boundary](#authority-boundary) · [Known limits](#known-limits) · [Maintenance checklist](#maintenance-checklist) · [Status notes](#status-notes) · [Evidence ledger](#evidence-ledger)

> [!IMPORTANT]
> Files under this root are fixture inputs or expected-output snapshots. They are not semantic contracts, schema authority, executable policy, source truth, evidence closure, runtime truth, review approval, release approval, or publication authority.

---

## Purpose

This directory groups versioned contract fixture roots.

Use this parent index to navigate fixture versions without confusing fixtures with the contracts and schemas they test. A fixture can show that a schema accepts a positive example, rejects a negative example, or that a policy-oriented snapshot matches expected output. It cannot make a claim true, approve a source, execute policy, certify runtime behavior, resolve evidence, admit a release, or authorize publication.

---

## Observed version roots

| Version root | Current role | Status |
|---|---|---|
| [`v1/`](v1/README.md) | Top-level v1 contract fixture index. | CONFIRMED |

The current `v1/` index covers observed fixture family roots for `common`, `evidence`, `governance`, `policy`, `runtime`, and `source`, with known limits and drift notes preserved in that child README.

Future version roots should follow this pattern only after their schema homes, contract homes, fixture layout, and test harness behavior are known enough to document truthfully:

```text
fixtures/contracts/<version>/
  README.md
  <family>/
    README.md
    <schema_name>/
      README.md
      valid/
      invalid/
```

---

## Harness relationship

The current common schema fixture harness derives versioned contract fixtures from schema families under:

```text
schemas/contracts/v1/<family>/*.schema.json
```

and pairs each schema with a fixture directory under:

```text
fixtures/contracts/v1/<family>/<schema_name>/
```

Expected schema-fixture behavior:

| Fixture pattern | Expected result |
|---|---|
| `valid/valid_*.json` | no JSON Schema errors |
| `invalid/invalid_*.json` | at least one JSON Schema error |
| `invalid/invalid_*.expected_error.txt` | expected text appears in combined schema error messages |

This README documents the parent organization only. It does not claim that the harness, validators, CI, policy checks, source admission checks, runtime checks, evidence checks, release checks, or dedicated validators were run during this update.

---

## Authority boundary

| Responsibility | Owning root | This README posture |
|---|---|---|
| Versioned contract fixture examples | `fixtures/contracts/` | Indexes observed version roots only. |
| Machine-checkable schema shape | `schemas/contracts/` | Referenced, not duplicated. |
| Semantic contract meaning | `contracts/` | Referenced, not replaced. |
| Executable policy and admissibility rules | `policy/` | Out of scope. |
| Source registry records | `data/registry/` | Out of scope. |
| Lifecycle source/material data | `data/raw/`, `data/work/`, `data/quarantine/`, `data/processed/`, `data/catalog/`, `data/triplet/`, `data/published/` | Out of scope. |
| Runtime/API behavior | `runtime/`, `apps/`, `packages/`, and governed API surfaces | Out of scope. |
| Release decisions and manifests | `release/` | Out of scope. |
| Enforceability proof | `tests/` and validator tooling | Referenced, not claimed as run. |

Do not collapse this fixture root into contract authority, schema authority, policy authority, operational truth, source truth, EvidenceBundle authority, runtime truth, release approval, or public-client permission.

---

## Known limits

| Item | Status | Notes |
|---|---:|---|
| Version inventory | PARTIAL | This README confirms `v1/README.md`; it is not a full recursive listing of every possible version root. |
| `v1/` family coverage | PARTIAL | The `v1/` README indexes observed family roots and explicitly preserves known limits. |
| Snapshot-style fixtures | CONFIRMED IN CHILD | The `source` v1 family includes a snapshot-style provenance-check fixture family. |
| Release fixture coverage | NEEDS VERIFICATION IN CHILD | The `v1/` README notes that the harness names `release`, but `fixtures/contracts/v1/release/README.md` was not found during that update. |
| Test execution | NOT RUN | No tests, validators, policy checks, runtime checks, source checks, evidence checks, release checks, or CI were run during this update. |

---

## Maintenance checklist

Before changing this parent root:

- [ ] Keep version roots explicit, such as `v1/`, rather than mixing versions in one unversioned family directory.
- [ ] Keep schema-style fixtures under `fixtures/contracts/<version>/<family>/<schema_name>/` when aligned with the harness.
- [ ] Keep passing examples under `valid/valid_<n>.json`.
- [ ] Keep failing examples under `invalid/invalid_<n>.json`.
- [ ] Keep expected-error text beside the invalid fixture it describes.
- [ ] Mark snapshot-style fixture families explicitly when they do not use the common schema-fixture pattern.
- [ ] Preserve the split between fixtures, schemas, contracts, policy, source registry records, lifecycle data, runtime behavior, release decisions, and tests.
- [ ] Keep fixture examples public-safe and limited to metadata-shaped examples or expected-output snapshots.
- [ ] Avoid private, unpublished, source-system, prompt-like, or policy-restricted content.
- [ ] Do not embed full source payloads or release-blocked material in fixtures.
- [ ] Update this README when a contract fixture version is added, retired, renamed, migrated, or converted.
- [ ] Run the relevant schema or policy tests before claiming validation success.

---

## Status notes

| Item | Status | Notes |
|---|---:|---|
| Target README | CONFIRMED UPDATED | This path existed as a blank file before this update. |
| `v1/` index | CONFIRMED | `fixtures/contracts/v1/README.md` exists and indexes observed v1 fixture family roots. |
| Additional version roots | UNKNOWN | Not verified by a full recursive repository listing during this update. |
| Harness behavior | CONFIRMED / NOT RUN | The schema fixture harness currently derives v1 fixture directories from schema names and family roots. |
| Test execution | NOT RUN | No validators, pytest, policy checks, source admission checks, runtime checks, evidence checks, release checks, or CI were run during this README update. |

---

## Evidence ledger

| Source | Status | Supports | Limits |
|---|---|---|---|
| Previous target file | CONFIRMED | Target existed as a blank file. | Did not define contract fixture parent guidance. |
| [`v1/README.md`](v1/README.md) | CONFIRMED | Current v1 contract fixture index and observed family-root coverage. | Its own inventory is partial and preserves known drift notes. |
| `../../tests/schemas/test_common_contracts.py` | CONFIRMED / NOT RUN | Harness family list and fixture discovery behavior for `fixtures/contracts/v1/<family>/<schema_name>/`. | Tests were not run during this update. |
| `../../docs/doctrine/directory-rules.md` | CONFIRMED doctrine | `fixtures/` is the validate/operate root for test inputs while contracts, schemas, policy, registry, lifecycle data, and release decisions remain separate roots. | Specific fixture completeness requires inventory and tests. |

[Back to top](#top)
