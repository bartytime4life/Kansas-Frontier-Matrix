# `schemas/tests/` — Schema Test Compatibility Index

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/schemas-tests-readme
title: schemas/tests/ README
type: readme; compatibility-index; schema-test-parent-index
version: v0.1
status: draft; schema-test-parent-index; valid-invalid-indexes-present; NEEDS VERIFICATION
updated: 2026-07-04
policy_label: public
tags: [kfm, schemas, tests, valid, invalid, fixtures, validation, compatibility]
[/KFM_META_BLOCK_V2] -->

## Purpose

`schemas/tests/` is the parent compatibility index for schema-test placement under the `schemas/` root.

The root `schemas/README.md` states that `schemas/` owns machine-checkable shape, pairs one-to-one with `contracts/`, and that tests live under `schemas/tests/valid` and `schemas/tests/invalid`. This README keeps that placement visible while preserving the boundary that executable validators, implementation code, fixtures, data, proof, policy, and release records remain separate.

## Status

| Item | Status |
|---|---|
| README | present |
| Direct child indexes confirmed | `valid/`, `invalid/` |
| Current role | parent compatibility index |
| Placement | CONFIRMED present / NEEDS VERIFICATION for long-term authority |
| Test execution | NOT RUN |
| Executable test owner | NEEDS VERIFICATION; use accepted project test root unless this path is formally adopted |

## Boundary

This directory is not a schema family, fixture authority, policy authority, validator implementation, CI configuration, emitted test-result store, data root, proof root, receipt root, graph root, map root, alerting root, or release root.

It should not contain canonical schemas, semantic contracts, real domain records, source-system exports, lifecycle data, EvidenceBundles, SourceDescriptors, proof packs, receipts, release records, public map payloads, direct model-runtime output, package code, runtime code, or validator code while accepted homes remain separate.

A passing or failing schema test proves only the tested shape behavior. It does not prove evidence truth, source authority, semantic truth, policy approval, rights clearance, sensitivity approval, release readiness, implementation proof, public-safety, or publication.

## Current child inventory

| Child path | Status | Notes |
|---|---|---|
| `valid/README.md` | present | Parent compatibility index for valid schema-test placement. |
| `valid/domains/README.md` | present | Domain valid schema-test parent index. |
| `valid/domains/fauna/README.md` | present | Valid Fauna schema-test guardrail. |
| `valid/domains/flora/README.md` | present | Valid Flora schema-test guardrail. |
| `valid/domains/habitat/README.md` | present | Valid Habitat schema-test guardrail. |
| `valid/domains/hydrology/README.md` | present | Valid Hydrology schema-test guardrail. |
| `valid/domains/transport/README.md` | present | Valid Transport schema-test guardrail with path-conflict note. |
| `valid/hazards/README.md` | present | Non-`domains/` Hazards valid schema-test guardrail; placement NEEDS VERIFICATION. |
| `valid/roads-rail-trade/README.md` | present | Non-`domains/` Roads / Rail / Trade valid schema-test guardrail; placement NEEDS VERIFICATION. |
| `invalid/README.md` | present | Parent compatibility index for invalid schema-test placement. |
| `invalid/domains/README.md` | present | Domain invalid schema-test parent index. |
| `invalid/domains/fauna/README.md` | present | Invalid Fauna schema-test guardrail. |
| `invalid/domains/flora/README.md` | present | Invalid Flora schema-test guardrail. |
| `invalid/domains/habitat/README.md` | present | Invalid Habitat schema-test guardrail. |
| `invalid/domains/hydrology/README.md` | present | Invalid Hydrology schema-test guardrail. |
| `invalid/domains/transport/README.md` | present | Invalid Transport schema-test guardrail with path-conflict note. |
| `invalid/hazards/README.md` | present | Non-`domains/` Hazards invalid schema-test guardrail; placement NEEDS VERIFICATION. |
| `invalid/roads-rail-trade/README.md` | present | Non-`domains/` Roads / Rail / Trade invalid schema-test guardrail; placement NEEDS VERIFICATION. |

## Correct nearby lanes

| Need | Preferred lane |
|---|---|
| Schema shape | `schemas/contracts/v1/` and accepted child lanes |
| Domain schema shape | `schemas/contracts/v1/domains/<domain>/` or accepted versioned schema lane |
| Semantic meaning | `contracts/` |
| Valid or invalid examples | `fixtures/` under the accepted domain or object-family fixture lane |
| Expected outputs or golden cases | `fixtures/` under an accepted golden/expected-output lane |
| Executable schema test code | `tests/schemas/` or accepted project test root unless this path is formally adopted |
| Validator implementation | `tools/validators/` |
| Policy rules and access posture | `policy/` |
| Lifecycle records and source outputs | `data/` under governed lifecycle roots |
| Release, correction, rollback decisions | `release/` |

## What belongs here

- This README.
- README-only compatibility guardrails for valid and invalid schema-test placement.
- Small schema-test examples only if maintainers formally confirm this path as an accepted schema-test home.
- Migration notes if historical schema tests are discovered here.
- Temporary mirror notes while test, fixture, and path placement is unresolved.

## What does not belong here

- Canonical `.schema.json` files.
- Semantic contract prose.
- Fixture payloads that belong under `fixtures/` unless an accepted migration assigns them here.
- Real source data, source-system exports, lifecycle data, EvidenceBundles, SourceDescriptors, proof packs, receipts, release manifests, public map payloads, public tiles, dashboards, screenshots, generated summaries, or direct model-runtime output.
- Policy rules, policy decisions, rights approvals, sensitivity approvals, release records, emitted validation reports, validator code, runtime code, package code, or API/UI outputs.
- Claims that any object is valid, invalid, evidence-supported, source-admitted, policy-approved, rights-cleared, released, public-safe, implementation-proven, or domain truth merely because this path exists or because a payload passes schema validation.

## Compatibility rules

| Rule | Requirement |
|---|---|
| Keep schemas versioned | Schema definitions belong in accepted schema lanes, not in this test index. |
| Keep fixtures in fixtures | Valid and invalid examples belong in fixture roots unless an accepted migration says otherwise. |
| Keep executable tests in accepted test roots | Do not add runnable test code here unless this path is formally adopted. |
| Preserve evidence boundaries | Schema tests must not replace EvidenceBundles, proof records, citation validation, source-role checks, or release gates. |
| Preserve policy boundaries | Schema validation does not approve policy, sensitivity, rights, release, or public display. |
| Tests are not publication | Test outcomes do not publish data, authorize display, or approve release. |
| Avoid parallel roots | Do not create duplicate schema, fixture, validator, policy, proof, receipt, graph, map, or release homes under this path. |

## Validation

```bash
find schemas/tests -maxdepth 5 -type f | sort
find schemas/contracts/v1 -maxdepth 5 -type f 2>/dev/null | sort
find fixtures -maxdepth 5 -type f 2>/dev/null | sort
pytest tests/schemas tests/contract || true
```

Replace `|| true` with fail-closed CI behavior once the relevant test paths are confirmed.

## Open questions

| Question | Status |
|---|---|
| Should `schemas/tests/` remain a compatibility index, or should executable schema-test ownership move entirely to `tests/schemas/`? | NEEDS VERIFICATION |
| Should valid and invalid examples be generated from fixture manifests rather than maintained under this path? | NEEDS VERIFICATION |
| Should non-`domains/` child paths such as `hazards/` and `roads-rail-trade/` move under `domains/`? | NEEDS VERIFICATION |
| Which CI workflow, if any, consumes `schemas/tests/valid` and `schemas/tests/invalid` today? | NEEDS VERIFICATION |
| Which accepted validator command should replace the provisional `pytest tests/schemas tests/contract || true` line? | NEEDS VERIFICATION |
