# `schemas/tests/invalid/domains/fauna/` — Fauna Invalid Schema Test Guardrail

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/schemas-tests-invalid-domains-fauna-readme
title: schemas/tests/invalid/domains/fauna/ README
type: readme; compatibility-index; invalid-test-placement-guardrail
version: v0.1
status: draft; empty-invalid-test-path; fauna-sensitive; NEEDS VERIFICATION
updated: 2026-07-04
policy_label: public
tags: [kfm, schemas, tests, invalid, domains, fauna, fixtures, geoprivacy, sensitivity, compatibility]
[/KFM_META_BLOCK_V2] -->

## Purpose

`schemas/tests/invalid/domains/fauna/` is a README-only compatibility guardrail for invalid Fauna schema-test placement.

The inspected Fauna domain schema lane lives at `schemas/contracts/v1/domains/fauna/`.

The inspected Fauna invalid fixture lane lives at `fixtures/domains/fauna/invalid/`.

## Status

| Item | Status |
|---|---|
| README | present |
| Direct invalid test files found under this path | none found in current search |
| Current role | compatibility guardrail |
| Placement | NEEDS VERIFICATION |
| Fauna sensitivity posture | fail closed |

## Boundary

This directory is not the Fauna schema family, Fauna fixture authority, policy authority, validator implementation, CI configuration, emitted test-result store, data root, or release root.

It should not contain canonical Fauna schemas, source records, live occurrence data, sensitive exact locations, public map payloads, release records, or validator code while accepted homes remain separate.

A failing or passing test here would prove only the tested shape behavior. It would not prove evidence truth, policy approval, sensitivity approval, release readiness, or public-safety.

## Current inventory

| Path | Status | Notes |
|---|---|---|
| `schemas/tests/invalid/domains/fauna/README.md` | present | Empty file expanded by this README. |
| `schemas/tests/invalid/domains/fauna/*` | not found in current search | No direct invalid test files were found under this path. |
| `schemas/contracts/v1/domains/fauna/README.md` | present | Inspected Fauna domain schema index. |
| `fixtures/domains/fauna/invalid/README.md` | present | Inspected Fauna invalid fixture lane. |
| `fixtures/domains/fauna/sensitive_deny/README.md` | present by search | Nearby negative/sensitivity fixture lane; not opened in this pass. |

## Correct nearby lanes

| Need | Preferred lane |
|---|---|
| Fauna schema shape | `schemas/contracts/v1/domains/fauna/` |
| Fauna semantic meaning | `contracts/domains/fauna/` |
| Invalid Fauna examples | `fixtures/domains/fauna/invalid/` |
| Sensitivity-deny examples | `fixtures/domains/fauna/sensitive_deny/` |
| Schema test code | `tests/schemas/` or accepted project test root |
| Validator implementation | `tools/validators/` |
| Fauna policy and sensitivity posture | `policy/domains/fauna/` and accepted sensitivity policy roots |
| Release, correction, rollback decisions | `release/` |

## What belongs here

- This README.
- Compatibility notes for this invalid schema-test path.
- Migration notes if historical invalid schema tests are discovered here.
- Temporary mirror notes while placement is unresolved.

## What does not belong here

- Canonical `.schema.json` files.
- Invalid fixture JSON files that should live under `fixtures/domains/fauna/invalid/` unless an accepted migration says otherwise.
- Real occurrence data, source-system exports, exact sensitive locations, telemetry, protected-site clues, private-land joins, or public map payloads.
- Policy rules, policy decisions, sensitivity approvals, release records, receipts, proofs, emitted validation reports, validator code, runtime code, or API/UI outputs.
- Claims that Fauna data is valid, invalid, safe, sensitive, approved, or released merely because this path exists.

## Compatibility rules

| Rule | Requirement |
|---|---|
| Keep schemas versioned | Fauna schemas belong under `schemas/contracts/v1/domains/fauna/` unless an accepted migration says otherwise. |
| Keep fixtures in fixtures | Invalid examples belong under `fixtures/domains/fauna/invalid/` unless an accepted migration says otherwise. |
| Fail closed on sensitivity | Missing or ambiguous sensitivity/geoprivacy posture must not be treated as public-safe. |
| Tests are not publication | Test outcomes do not publish data or approve release. |
| Avoid parallel test roots | Add test files only to accepted test homes unless a migration note explains the exception. |

## Validation

```bash
find schemas/tests/invalid/domains/fauna -maxdepth 4 -type f | sort
find fixtures/domains/fauna/invalid -maxdepth 5 -type f 2>/dev/null | sort
find schemas/contracts/v1/domains/fauna -maxdepth 4 -type f | sort
pytest tests/schemas tests/contract || true
```

Replace `|| true` with fail-closed CI behavior once the relevant test paths are confirmed.

## Open questions

| Question | Status |
|---|---|
| Should `schemas/tests/invalid/domains/fauna/` remain as a compatibility guardrail or be retired? | NEEDS VERIFICATION |
| Are there historical references that expect invalid Fauna schema tests under this path? | NEEDS VERIFICATION |
| Should invalid Fauna tests be generated from `fixtures/domains/fauna/invalid/` manifests? | NEEDS VERIFICATION |
| Which sensitivity-deny and geoprivacy cases must be represented as invalid tests? | NEEDS VERIFICATION |
