# `schemas/tests/valid/domains/fauna/` — Fauna Valid Schema Test Guardrail

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/schemas-tests-valid-domains-fauna-readme
title: schemas/tests/valid/domains/fauna/ README
type: readme; compatibility-index; valid-test-placement-guardrail
version: v0.1
status: draft; empty-valid-test-path; fauna-sensitive; NEEDS VERIFICATION
updated: 2026-07-04
policy_label: public
tags: [kfm, schemas, tests, valid, domains, fauna, fixtures, geoprivacy, sensitivity, compatibility]
[/KFM_META_BLOCK_V2] -->

## Purpose

`schemas/tests/valid/domains/fauna/` is a README-only compatibility guardrail for valid Fauna schema-test placement.

The inspected Fauna domain schema lane lives at `schemas/contracts/v1/domains/fauna/`.

The inspected Fauna valid fixture lane lives at `fixtures/domains/fauna/valid/`.

## Status

| Item | Status |
|---|---|
| README | present |
| Direct valid test files found under this path | none found in current search |
| Current role | compatibility guardrail |
| Placement | NEEDS VERIFICATION |
| Fauna sensitivity posture | fail closed |

## Boundary

This directory is not the Fauna schema family, Fauna fixture authority, policy authority, sensitivity authority, validator implementation, CI configuration, emitted test-result store, data root, proof root, or release root.

It should not contain canonical Fauna schemas, source records, lifecycle data, real occurrence data, sensitive exact locations, telemetry, steward-controlled details, public map payloads, release records, or validator code while accepted homes remain separate.

A passing valid test here would prove only the tested shape behavior. It would not prove evidence truth, source authority, sensitivity approval, rights clearance, release readiness, public-safe geometry, or public-safety.

## Current inventory

| Path | Status | Notes |
|---|---|---|
| `schemas/tests/valid/domains/fauna/README.md` | present | Empty file expanded by this README. |
| `schemas/tests/valid/domains/fauna/*` | not found in current search | No direct valid test files were found under this path. |
| `schemas/contracts/v1/domains/fauna/README.md` | present | Inspected Fauna domain schema index. |
| `schemas/contracts/v1/domains/fauna/receipts/README.md` | present by search | Fauna receipts schema index; not reopened in this pass. |
| `fixtures/domains/fauna/valid/README.md` | present | Inspected Fauna valid fixture lane. |
| `fixtures/domains/fauna/golden/README.md` | present by search | Nearby expected-output fixture lane; not opened in this pass. |

## Correct nearby lanes

| Need | Preferred lane |
|---|---|
| Fauna schema shape | `schemas/contracts/v1/domains/fauna/` |
| Fauna semantic meaning | `contracts/domains/fauna/` |
| Valid Fauna examples | `fixtures/domains/fauna/valid/` |
| Expected outputs or golden cases | `fixtures/domains/fauna/golden/` |
| Schema test code | `tests/schemas/` or accepted project test root |
| Validator implementation | `tools/validators/` |
| Fauna policy and sensitivity posture | `policy/domains/fauna/` and `policy/sensitivity/fauna/` |
| Release, correction, rollback decisions | `release/` |

## What belongs here

- This README.
- Compatibility notes for this valid schema-test path.
- Migration notes if historical valid schema tests are discovered here.
- Temporary mirror notes while valid schema-test placement is unresolved.

## What does not belong here

- Canonical `.schema.json` files.
- Valid fixture JSON or GeoJSON files that should live under `fixtures/domains/fauna/valid/` unless an accepted migration says otherwise.
- Real taxon, occurrence, range, monitoring, mortality, disease, invasive-species, sensitive-site, telemetry, steward-controlled, or source-system records.
- RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, PUBLISHED, EvidenceBundle, proof, receipt, source descriptor, registry, release, correction, rollback, public API, public map, tile, dashboard, or generated-answer artifacts.
- Policy rules, sensitivity approvals, rights approvals, release records, emitted validation reports, validator code, runtime code, package code, or API/UI outputs.
- Claims that Fauna data is evidence-supported, sensitivity-approved, rights-cleared, released, public-safe, or domain truth merely because a payload passes a schema test.

## Compatibility rules

| Rule | Requirement |
|---|---|
| Keep schemas versioned | Fauna schemas belong under `schemas/contracts/v1/domains/fauna/` unless an accepted migration says otherwise. |
| Keep fixtures in fixtures | Valid examples belong under `fixtures/domains/fauna/valid/` unless an accepted migration says otherwise. |
| Keep valid cases public-safe | Valid examples must not reveal sensitive exact locations or reconstructive geoprivacy clues. |
| Shape is not approval | Passing schema validation does not prove sensitivity, rights, review, release, or evidence closure. |
| Tests are not publication | Test outcomes do not publish data, authorize map display, or approve release. |
| Avoid parallel test roots | Add test files only to accepted test homes unless a migration note explains the exception. |

## Validation

```bash
find schemas/tests/valid/domains/fauna -maxdepth 4 -type f | sort
find fixtures/domains/fauna/valid -maxdepth 5 -type f 2>/dev/null | sort
find schemas/contracts/v1/domains/fauna -maxdepth 5 -type f | sort
pytest tests/schemas tests/contract || true
```

Replace `|| true` with fail-closed CI behavior once the relevant test paths are confirmed.

## Open questions

| Question | Status |
|---|---|
| Should `schemas/tests/valid/domains/fauna/` remain as a compatibility guardrail or be retired? | NEEDS VERIFICATION |
| Are there historical references that expect valid Fauna schema tests under this path? | NEEDS VERIFICATION |
| Should valid Fauna tests be generated from `fixtures/domains/fauna/valid/` manifests? | NEEDS VERIFICATION |
| Which non-sensitive occurrence, public-safe range, public-safe seasonal-range, redaction, freshness, and release-visible cases must be represented as valid tests? | NEEDS VERIFICATION |
