<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://fixture/contracts/v1/source/readme
title: source contract fixtures README
type: fixture-readme
version: v0.1.0
status: draft
owners: TODO(owner): source steward; TODO(owner): schema steward; TODO(owner): fixture steward; TODO(owner): validator steward; TODO(owner): policy steward; TODO(owner): docs steward
created: NEEDS VERIFICATION - blank file existed before 2026-07-01 expansion
updated: 2026-07-01
policy_label: public-review
related:
  - doctrine_artifact_descriptor/README.md
  - doctrine_artifact_preflight_summary/README.md
  - doctrine_artifact_provenance_check/README.md
  - ingest_receipt/README.md
  - source_descriptor/README.md
  - ../../../../schemas/contracts/v1/source/
  - ../../../../contracts/source/
  - ../../../../policy/source/
  - ../../../../tests/schemas/test_common_contracts.py
  - ../../../../docs/doctrine/directory-rules.md
tags: [kfm, fixtures, contracts, v1, source, source-fixtures, valid-fixtures, invalid-fixtures, snapshot-fixtures, json-schema, source-admission, source-descriptor, ingest-receipt, doctrine-artifacts, provenance, preflight, non-authoritative]
notes:
  - "This README replaces a blank file at `fixtures/contracts/v1/source/README.md`."
  - "This directory groups observed source-family contract fixtures under `fixtures/contracts/v1/source/`."
  - "Most child directories are JSON Schema valid/invalid fixture families; `doctrine_artifact_provenance_check` is currently a policy-test snapshot fixture family."
  - "The `source_descriptor` schema currently declares `fixtures_root` as `tests/fixtures/sources/source_descriptor/`; the observed/requested fixture family lives under `fixtures/contracts/v1/source/source_descriptor/`, so fixture-root reconciliation remains NEEDS VERIFICATION."
  - "No tests, validators, source admission workflows, policy checks, release checks, or CI jobs were run during this documentation update."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Source contract fixtures

Source-family fixture index for KFM contract samples under `fixtures/contracts/v1/source/`.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: fixtures" src="https://img.shields.io/badge/root-fixtures%2F-6f42c1">
  <img alt="Family: source" src="https://img.shields.io/badge/family-source-blue">
  <img alt="Authority: fixture only" src="https://img.shields.io/badge/authority-fixture%20only-critical">
  <img alt="Schema fixtures" src="https://img.shields.io/badge/schema__fixtures-valid%2Finvalid-success">
  <img alt="Snapshot fixtures" src="https://img.shields.io/badge/snapshot__fixtures-present-informational">
</p>

**Path:** `fixtures/contracts/v1/source/README.md`  
**Root posture:** source-family contract fixtures  
**Authority posture:** fixtures only; contract meaning, schema shape, policy, registry records, lifecycle data, release decisions, and runtime behavior live in their owning roots  
**Quick links:** [Purpose](#purpose) · [Observed fixture families](#observed-fixture-families) · [Authority boundary](#authority-boundary) · [Harness behavior](#harness-behavior) · [Known exceptions and drift](#known-exceptions-and-drift) · [Maintenance checklist](#maintenance-checklist) · [Status notes](#status-notes) · [Evidence ledger](#evidence-ledger)

> [!IMPORTANT]
> Files under this root are fixture inputs or expected-output snapshots. They are not source registry records, source truth, rights decisions, sensitivity decisions, source admission decisions, EvidenceBundles, PolicyDecisions, ReleaseManifests, release approval, review approval, or publication authority.

---

## Purpose

This directory groups source-family fixtures used to test or snapshot KFM source-contract behavior.

The source fixture families help check whether source-related contract shapes accept valid examples and reject invalid examples without allowing examples to become authoritative source records. A passing fixture proves only the bounded test expectation for that fixture family. It does not prove source claims are true, source material is admitted, rights are settled, sensitivity policy allows public use, lifecycle transitions are approved, or release gates passed.

---

## Observed fixture families

| Fixture family | Style | Current coverage | Status |
|---|---|---|---|
| [`doctrine_artifact_descriptor/`](doctrine_artifact_descriptor/README.md) | JSON Schema valid/invalid fixtures | One valid descriptor-shaped case and one invalid integrity/date case. | CONFIRMED |
| [`doctrine_artifact_preflight_summary/`](doctrine_artifact_preflight_summary/README.md) | JSON Schema valid/invalid fixtures | One valid preflight-summary case and one invalid return-code enum case. | CONFIRMED |
| [`doctrine_artifact_provenance_check/`](doctrine_artifact_provenance_check/README.md) | Policy-test snapshot fixtures | One failing placeholder-source-url snapshot and two provenance-status sync snapshots. | CONFIRMED / NONSTANDARD STYLE |
| [`ingest_receipt/`](ingest_receipt/README.md) | JSON Schema valid/invalid fixtures | One valid ingest receipt case and one invalid missing-required-field case. | CONFIRMED |
| [`source_descriptor/`](source_descriptor/README.md) | JSON Schema valid/invalid fixtures | One valid SourceDescriptor case and one invalid missing-`source_id` case. | CONFIRMED / FIXTURE-ROOT RECONCILIATION NEEDED |

### Schema-style fixture families

The following observed child directories follow the common valid/invalid schema-fixture pattern:

```text
doctrine_artifact_descriptor/
doctrine_artifact_preflight_summary/
ingest_receipt/
source_descriptor/
```

Their expected lane pattern is:

```text
<fixture_family>/
  README.md
  valid/
    README.md
    valid_*.json
  invalid/
    README.md
    invalid_*.json
    invalid_*.expected_error.txt
```

### Snapshot-style fixture family

`doctrine_artifact_provenance_check/` currently behaves as a policy-test snapshot fixture family, not a conventional JSON Schema fixture family. Its child README identifies expected JSON snapshots for doctrine artifact provenance maintenance checks and notes that a directly named schema was not found during its documentation sequence.

---

## Authority boundary

| Responsibility | Home | Status in this check |
|---|---|---|
| Source-family fixtures | `fixtures/contracts/v1/source/` | CONFIRMED parent README update |
| Machine-readable source contract schemas | `schemas/contracts/v1/source/` | REFERENCED / PARTIALLY CONFIRMED through child READMEs |
| Human semantic source contracts | `contracts/source/` | REFERENCED / PARTIALLY CONFIRMED through child READMEs |
| Source registry records | `data/registry/sources/` | OUT OF SCOPE FOR THIS README |
| Source policy | `policy/source/` | OUT OF SCOPE FOR THIS README |
| Rights and sensitivity policy | `policy/rights/`, `policy/sensitivity/` | OUT OF SCOPE FOR THIS README |
| Source validators | `tools/validators/` | NEEDS VERIFICATION unless a child README confirmed a script and whether it was run |
| Common schema fixture harness | `tests/schemas/test_common_contracts.py` | CONFIRMED / NOT RUN |
| Release decisions | `release/` and release manifests | OUT OF SCOPE FOR THIS README |

Do not collapse source fixtures into:

| Do not collapse fixtures into | Why |
|---|---|
| Source truth | Fixtures are examples, not claims that source records are true. |
| SourceDescriptor registry records | Registry records require their own governed home and review posture. |
| IngestReceipt runtime facts | Ingest receipts describe capture events; a fixture does not prove an ingest ran. |
| EvidenceBundle | Evidence supports claims; fixtures test shapes or expected output snapshots. |
| PolicyDecision | Policy decides admissibility; fixtures do not decide policy. |
| ReleaseManifest | Release manifests bind released artifacts; fixtures do not publish. |
| Public-client permission | Public clients still require governed APIs, release state, policy checks, citations, and rollback posture. |

---

## Harness behavior

The common schema fixture harness includes `source` in its contract fixture families and discovers schemas from:

```text
schemas/contracts/v1/source/*.schema.json
```

For each discovered schema, the harness derives the fixture directory as:

```text
fixtures/contracts/v1/source/<schema_name>/
```

Observed test expectations:

| Fixture pattern | Expected result |
|---|---|
| `valid/valid_*.json` | no JSON Schema errors |
| `invalid/invalid_*.json` | at least one JSON Schema error |
| `invalid/invalid_*.expected_error.txt` | expected text appears in combined schema error messages |

This parent README documents expected fixture organization only. It does not claim that pytest, CI, validators, source admission policy, source registry resolution, rights/sensitivity checks, doctrine artifact maintenance scripts, release checks, or dedicated validators were run during this update.

---

## Known exceptions and drift

| Item | Status | Notes |
|---|---:|---|
| `doctrine_artifact_provenance_check/` | NONSTANDARD STYLE | Current files are expected-output snapshots used by policy tests, not conventional `valid_*.json` / `invalid_*.json` schema fixtures. |
| `source_descriptor/` fixture root | NEEDS VERIFICATION | The inspected schema declares `fixtures_root` as `tests/fixtures/sources/source_descriptor/`, while the observed/requested fixtures live under `fixtures/contracts/v1/source/source_descriptor/`. |
| Dedicated validators | NEEDS VERIFICATION | Child READMEs reference validator paths where available, but validators were not run in this documentation pass. |
| Completeness of source fixture coverage | NEEDS VERIFICATION | This README indexes observed README-covered families, not a full repository inventory or coverage report. |

---

## Maintenance checklist

Before changing this source fixture root:

- [ ] Keep source contract fixtures under the governed `fixtures/contracts/v1/source/` root unless an ADR or migration note changes the convention.
- [ ] Keep schema-style fixture families aligned with their schema names where practical.
- [ ] Keep passing examples under `valid/valid_<n>.json`.
- [ ] Keep failing examples under `invalid/invalid_<n>.json`.
- [ ] Keep expected-error text beside the invalid fixture it describes.
- [ ] Keep snapshot-style fixtures clearly marked when a family does not use the common schema-fixture pattern.
- [ ] Preserve the split between fixtures, schemas, contracts, policy, source registry records, and release decisions.
- [ ] Keep fixture examples public-safe and limited to metadata-shaped examples or expected-output snapshots.
- [ ] Avoid private, unpublished, source-system, prompt-like, or policy-restricted content.
- [ ] Do not embed full source payloads or release-blocked material in fixtures.
- [ ] Update this parent README when a source fixture family is added, retired, renamed, migrated, or converted between schema and snapshot styles.
- [ ] Run the relevant schema or policy tests before claiming validation success.

---

## Status notes

| Item | Status | Notes |
|---|---:|---|
| Target README | CONFIRMED UPDATED | This path existed as a blank file before this update. |
| Source fixture children | PARTIALLY CONFIRMED | Five README-covered child families are indexed here. |
| Schema-style families | CONFIRMED OBSERVED | `doctrine_artifact_descriptor`, `doctrine_artifact_preflight_summary`, `ingest_receipt`, and `source_descriptor` have valid/invalid fixture-family READMEs. |
| Snapshot-style family | CONFIRMED OBSERVED | `doctrine_artifact_provenance_check` is documented as expected-output snapshots. |
| Harness | CONFIRMED / NOT RUN | `tests/schemas/test_common_contracts.py` includes `source` and derives fixture directories from schema names. |
| Fixture-root drift | NEEDS VERIFICATION | `source_descriptor` has an observed/requested fixture path under `fixtures/contracts/v1/source/` while its schema metadata names `tests/fixtures/sources/source_descriptor/`. |
| Test execution | NOT RUN | No validators, pytest, source policy checks, source registry checks, doctrine maintenance checks, steward review checks, release checks, or CI were run during this README update. |

---

## Evidence ledger

| Source | Status | Supports | Limits |
|---|---|---|---|
| Previous target file | CONFIRMED | Target existed as a blank file. | Did not define source fixture root guidance. |
| [`doctrine_artifact_descriptor/README.md`](doctrine_artifact_descriptor/README.md) | CONFIRMED | Doctrine artifact descriptor valid/invalid fixture-family purpose and inventory. | Does not prove tests were run. |
| [`doctrine_artifact_preflight_summary/README.md`](doctrine_artifact_preflight_summary/README.md) | CONFIRMED | Preflight summary valid/invalid fixture-family purpose and inventory. | Does not prove tests were run. |
| [`doctrine_artifact_provenance_check/README.md`](doctrine_artifact_provenance_check/README.md) | CONFIRMED | Snapshot-style provenance check/sync fixture-family purpose and inventory. | Nonstandard fixture style; not a direct schema fixture family. |
| [`ingest_receipt/README.md`](ingest_receipt/README.md) | CONFIRMED | IngestReceipt valid/invalid fixture-family purpose and inventory. | Does not prove tests were run. |
| [`source_descriptor/README.md`](source_descriptor/README.md) | CONFIRMED | SourceDescriptor valid/invalid fixture-family purpose, inventory, and fixture-root mismatch note. | Fixture-root reconciliation remains open. |
| `../../../../tests/schemas/test_common_contracts.py` | CONFIRMED / NOT RUN | Common schema fixture discovery and valid/invalid fixture behavior for the `source` family. | Tests were not run during this update. |
| `../../../../docs/doctrine/directory-rules.md` | CONFIRMED doctrine | `fixtures/` is within the validate/operate authority surface and supports test inputs while contracts, schemas, policy, registry, lifecycle data, and release decisions remain separate roots. | Specific fixture completeness requires inventory and tests. |

[Back to top](#top)
