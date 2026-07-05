# `schemas/tests/invalid/domains/flora/` — Flora Invalid Schema Test Guardrail

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/schemas-tests-invalid-domains-flora-readme
title: schemas/tests/invalid/domains/flora/ README
type: readme; compatibility-index; invalid-test-placement-guardrail
version: v0.1
status: draft; empty-invalid-test-path; flora-sensitive; NEEDS VERIFICATION
updated: 2026-07-04
policy_label: public
tags: [kfm, schemas, tests, invalid, domains, flora, fixtures, geoprivacy, rare-plants, sensitivity, compatibility]
[/KFM_META_BLOCK_V2] -->

## Purpose

`schemas/tests/invalid/domains/flora/` is a README-only compatibility guardrail for invalid Flora schema-test placement.

The inspected Flora domain schema lane lives at `schemas/contracts/v1/domains/flora/`.

The inspected Flora invalid fixture lane lives at `fixtures/domains/flora/invalid/`.

## Status

| Item | Status |
|---|---|
| README | present |
| Direct invalid test files found under this path | none found in current search |
| Current role | compatibility guardrail |
| Placement | NEEDS VERIFICATION |
| Flora sensitivity posture | fail closed |

## Boundary

This directory is not the Flora schema family, Flora fixture authority, policy authority, validator implementation, CI configuration, emitted test-result store, data root, or release root.

It should not contain canonical Flora schemas, source records, real occurrence data, rare/protected plant exact locations, public map payloads, release records, or validator code while accepted homes remain separate.

A failing or passing test here would prove only the tested shape behavior. It would not prove evidence truth, policy approval, sensitivity approval, release readiness, or public-safety.

## Current inventory

| Path | Status | Notes |
|---|---|---|
| `schemas/tests/invalid/domains/flora/README.md` | present | Empty file expanded by this README. |
| `schemas/tests/invalid/domains/flora/*` | not found in current search | No direct invalid test files were found under this path. |
| `schemas/contracts/v1/domains/flora/README.md` | present | Inspected Flora domain schema index. |
| `fixtures/domains/flora/invalid/README.md` | present | Inspected Flora invalid fixture lane. |
| `fixtures/domains/flora/golden/README.md` | present by search | Nearby expected-output fixture lane; not opened in this pass. |

## Correct nearby lanes

| Need | Preferred lane |
|---|---|
| Flora schema shape | `schemas/contracts/v1/domains/flora/` |
| Flora semantic meaning | `contracts/domains/flora/` |
| Invalid Flora examples | `fixtures/domains/flora/invalid/` |
| Expected outputs or golden cases | `fixtures/domains/flora/golden/` |
| Schema test code | `tests/schemas/` or accepted project test root |
| Validator implementation | `tools/validators/` |
| Flora policy and sensitivity posture | `policy/domains/flora/` and accepted sensitivity policy roots |
| Release, correction, rollback decisions | `release/` |

## What belongs here

- This README.
- Compatibility notes for this invalid schema-test path.
- Migration notes if historical invalid schema tests are discovered here.
- Temporary mirror notes while placement is unresolved.

## What does not belong here

- Canonical `.schema.json` files.
- Invalid fixture JSON files that should live under `fixtures/domains/flora/invalid/` unless an accepted migration says otherwise.
- Real occurrence data, source-system exports, rare/protected plant exact locations, steward-controlled sensitive knowledge, public map payloads, or reconstructive geoprivacy clues.
- Policy rules, policy decisions, sensitivity approvals, release records, receipts, proofs, emitted validation reports, validator code, runtime code, or API/UI outputs.
- Claims that Flora data is valid, invalid, safe, sensitive, approved, or released merely because this path exists.

## Compatibility rules

| Rule | Requirement |
|---|---|
| Keep schemas versioned | Flora schemas belong under `schemas/contracts/v1/domains/flora/` unless an accepted migration says otherwise. |
| Keep fixtures in fixtures | Invalid examples belong under `fixtures/domains/flora/invalid/` unless an accepted migration says otherwise. |
| Fail closed on sensitivity | Missing or ambiguous sensitivity/geoprivacy posture must not be treated as public-safe. |
| Tests are not publication | Test outcomes do not publish data or approve release. |
| Avoid parallel test roots | Add test files only to accepted test homes unless a migration note explains the exception. |

## Validation

```bash
find schemas/tests/invalid/domains/flora -maxdepth 4 -type f | sort
find fixtures/domains/flora/invalid -maxdepth 5 -type f 2>/dev/null | sort
find schemas/contracts/v1/domains/flora -maxdepth 4 -type f | sort
pytest tests/schemas tests/contract || true
```

Replace `|| true` with fail-closed CI behavior once the relevant test paths are confirmed.

## Open questions

| Question | Status |
|---|---|
| Should `schemas/tests/invalid/domains/flora/` remain as a compatibility guardrail or be retired? | NEEDS VERIFICATION |
| Are there historical references that expect invalid Flora schema tests under this path? | NEEDS VERIFICATION |
| Should invalid Flora tests be generated from `fixtures/domains/flora/invalid/` manifests? | NEEDS VERIFICATION |
| Which rare-plant, geoprivacy, and renderer-unsafe cases must be represented as invalid tests? | NEEDS VERIFICATION |
