# `schemas/tests/valid/domains/flora/` — Flora Valid Schema Test Guardrail

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/schemas-tests-valid-domains-flora-readme
title: schemas/tests/valid/domains/flora/ README
type: readme; compatibility-index; valid-test-placement-guardrail
version: v0.1
status: draft; empty-valid-test-path; flora-sensitive; NEEDS VERIFICATION
updated: 2026-07-04
policy_label: public
tags: [kfm, schemas, tests, valid, domains, flora, fixtures, geoprivacy, rare-plants, sensitivity, compatibility]
[/KFM_META_BLOCK_V2] -->

## Purpose

`schemas/tests/valid/domains/flora/` is a README-only compatibility guardrail for valid Flora schema-test placement.

The inspected Flora domain schema lane lives at `schemas/contracts/v1/domains/flora/`.

The inspected Flora valid fixture lane lives at `fixtures/domains/flora/valid/`.

## Status

| Item | Status |
|---|---|
| README | present |
| Direct valid test files found under this path | none found in current search |
| Current role | compatibility guardrail |
| Placement | NEEDS VERIFICATION |
| Flora sensitivity posture | fail closed |

## Boundary

This directory is not the Flora schema family, Flora fixture authority, policy authority, sensitivity authority, validator implementation, CI configuration, emitted test-result store, data root, proof root, or release root.

It should not contain canonical Flora schemas, source records, lifecycle data, real occurrence data, rare/protected plant exact locations, culturally sensitive plant knowledge, steward-controlled details, public map payloads, release records, or validator code while accepted homes remain separate.

A passing valid test here would prove only the tested shape behavior. It would not prove evidence truth, source authority, sensitivity approval, rights clearance, release readiness, public-safe geometry, implementation proof, or public-safety.

## Current inventory

| Path | Status | Notes |
|---|---|---|
| `schemas/tests/valid/domains/flora/README.md` | present | Empty file expanded by this README. |
| `schemas/tests/valid/domains/flora/*` | not found in current search | No direct valid test files were found under this path. |
| `schemas/contracts/v1/domains/flora/README.md` | present | Inspected Flora domain schema index. |
| `fixtures/domains/flora/valid/README.md` | present | Inspected Flora valid fixture lane. |
| `fixtures/domains/flora/golden/README.md` | present by search | Nearby expected-output fixture lane; not opened in this pass. |

## Correct nearby lanes

| Need | Preferred lane |
|---|---|
| Flora schema shape | `schemas/contracts/v1/domains/flora/` |
| Flora semantic meaning | `contracts/domains/flora/` |
| Valid Flora examples | `fixtures/domains/flora/valid/` |
| Expected outputs or golden cases | `fixtures/domains/flora/golden/` |
| Schema test code | `tests/schemas/` or accepted project test root |
| Validator implementation | `tools/validators/` |
| Flora policy and sensitivity posture | `policy/domains/flora/` and `policy/sensitivity/flora/` |
| Release, correction, rollback decisions | `release/` |

## What belongs here

- This README.
- Compatibility notes for this valid schema-test path.
- Migration notes if historical valid schema tests are discovered here.
- Temporary mirror notes while valid schema-test placement is unresolved.

## What does not belong here

- Canonical `.schema.json` files.
- Valid fixture JSON, YAML, or GeoJSON files that should live under `fixtures/domains/flora/valid/` unless an accepted migration says otherwise.
- Real taxon, occurrence, specimen, range, botanical survey, phenology, vegetation community, invasive-plant, restoration, rare-plant, sensitive-site, steward-controlled, or source-system records.
- RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, PUBLISHED, EvidenceBundle, proof, receipt, source descriptor, registry, release, correction, rollback, public API, public map, tile, dashboard, or generated-answer artifacts.
- Policy rules, sensitivity approvals, rights approvals, release records, emitted validation reports, validator code, runtime code, package code, or API/UI outputs.
- Claims that Flora data is evidence-supported, sensitivity-approved, rights-cleared, released, public-safe, implementation-proven, or domain truth merely because a payload passes a schema test.

## Compatibility rules

| Rule | Requirement |
|---|---|
| Keep schemas versioned | Flora schemas belong under `schemas/contracts/v1/domains/flora/` unless an accepted migration says otherwise. |
| Keep fixtures in fixtures | Valid examples belong under `fixtures/domains/flora/valid/` unless an accepted migration says otherwise. |
| Keep valid cases public-safe | Valid examples must not reveal rare/protected plant locations or reconstructive geoprivacy clues. |
| Shape is not approval | Passing schema validation does not prove sensitivity, rights, review, release, evidence closure, or renderer safety. |
| Tests are not publication | Test outcomes do not publish data, authorize map display, or approve release. |
| Avoid parallel test roots | Add test files only to accepted test homes unless a migration note explains the exception. |

## Validation

```bash
find schemas/tests/valid/domains/flora -maxdepth 4 -type f | sort
find fixtures/domains/flora/valid -maxdepth 5 -type f 2>/dev/null | sort
find schemas/contracts/v1/domains/flora -maxdepth 5 -type f | sort
pytest tests/schemas tests/contract || true
```

Replace `|| true` with fail-closed CI behavior once the relevant test paths are confirmed.

## Open questions

| Question | Status |
|---|---|
| Should `schemas/tests/valid/domains/flora/` remain as a compatibility guardrail or be retired? | NEEDS VERIFICATION |
| Are there historical references that expect valid Flora schema tests under this path? | NEEDS VERIFICATION |
| Should valid Flora tests be generated from `fixtures/domains/flora/valid/` manifests? | NEEDS VERIFICATION |
| Which plant taxon, public-safe occurrence, generalized range, phenology, EvidenceBundle closure, renderer-safe geometry, and redaction-visible cases must be represented as valid tests? | NEEDS VERIFICATION |
