# `schemas/tests/valid/` — Valid Schema Test Compatibility Index

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/schemas-tests-valid-readme
title: schemas/tests/valid/ README
type: readme; compatibility-index; valid-test-parent-index
version: v0.1
status: draft; valid-schema-test-parent-index; guardrail-readmes-present; NEEDS VERIFICATION
updated: 2026-07-04
policy_label: public
tags: [kfm, schemas, tests, valid, fixtures, validation, compatibility]
[/KFM_META_BLOCK_V2] -->

## Purpose

`schemas/tests/valid/` is a compatibility index for valid schema-test placement.

This path is intended to point maintainers toward valid schema-test guardrails and nearby fixture lanes. It is not itself a fixture authority or schema authority.

## Status

| Item | Status |
|---|---|
| README | present |
| Previous README wording | `Valid schema fixtures`; replaced with test-placement boundary wording |
| Direct child guardrail lanes confirmed | `domains/`, `hazards/`, `roads-rail-trade/` |
| Current role | parent compatibility index |
| Placement | NEEDS VERIFICATION |
| Test execution | NOT RUN |

## Boundary

This directory is not a schema family, fixture authority, policy authority, validator implementation, CI configuration, emitted test-result store, data root, proof root, alerting root, graph root, map root, or release root.

It should not contain canonical schemas, real domain records, source-system exports, lifecycle data, EvidenceBundles, proof packs, release records, public map payloads, direct model-runtime output, or validator code while accepted homes remain separate.

A passing valid schema test proves only the tested shape behavior. It does not prove evidence truth, source authority, semantic truth, policy approval, rights clearance, sensitivity approval, release readiness, public-safety, implementation proof, or publication.

## Current child inventory

| Child path | Status | Notes |
|---|---|---|
| `domains/README.md` | present | Parent index for domain-specific valid schema-test guardrails. |
| `domains/fauna/README.md` | present | Fauna valid schema-test guardrail. |
| `domains/flora/README.md` | present | Flora valid schema-test guardrail. |
| `domains/habitat/README.md` | present | Habitat valid schema-test guardrail. |
| `domains/hydrology/README.md` | present | Hydrology valid schema-test guardrail. |
| `domains/transport/README.md` | present | Transport valid schema-test guardrail with slug/path conflict note. |
| `hazards/README.md` | present | Non-`domains/` Hazards valid schema-test guardrail; placement NEEDS VERIFICATION. |
| `roads-rail-trade/README.md` | present | Non-`domains/` Roads / Rail / Trade valid schema-test guardrail; placement NEEDS VERIFICATION. |

## Correct nearby lanes

| Need | Preferred lane |
|---|---|
| Schema shape | `schemas/contracts/v1/` and accepted child lanes |
| Domain schema shape | `schemas/contracts/v1/domains/<domain>/` or accepted versioned schema lane |
| Semantic meaning | `contracts/` |
| Valid examples | `fixtures/` under the accepted domain or object-family fixture lane |
| Expected outputs or golden cases | `fixtures/` under an accepted golden/expected-output lane |
| Schema test code | `tests/schemas/` or accepted project test root |
| Validator implementation | `tools/validators/` |
| Policy rules and access posture | `policy/` |
| Release, correction, rollback decisions | `release/` |

## What belongs here

- This README.
- README-only compatibility guardrails for valid schema-test placement.
- Migration notes if historical valid schema tests are discovered here.
- Temporary mirror notes while test, fixture, and path placement is unresolved.

## What does not belong here

- Canonical `.schema.json` files.
- Fixture payloads that belong under `fixtures/` unless an accepted migration assigns them here.
- Real source data, source-system exports, lifecycle data, EvidenceBundles, proof packs, receipts, release manifests, public map payloads, public tiles, dashboards, screenshots, generated summaries, or direct model-runtime output.
- Policy rules, policy decisions, rights approvals, sensitivity approvals, release records, emitted validation reports, validator code, runtime code, package code, or API/UI outputs.
- Claims that any object is evidence-supported, source-admitted, policy-approved, rights-cleared, released, public-safe, implementation-proven, or domain truth merely because this path exists or because a payload passes schema validation.

## Compatibility rules

| Rule | Requirement |
|---|---|
| Keep schemas versioned | Schema definitions belong in accepted schema lanes, not in this valid-test index. |
| Keep fixtures in fixtures | Valid examples belong in fixture roots unless an accepted migration says otherwise. |
| Keep executable tests in accepted test roots | Do not add runnable test code here unless this path is formally adopted. |
| Preserve evidence boundaries | Valid tests must not replace EvidenceBundles, proof records, citation validation, source-role checks, or release gates. |
| Shape is not approval | Passing schema validation does not prove rights, sensitivity, review, release, policy, evidence closure, or renderer safety. |
| Tests are not publication | Test outcomes do not publish data, authorize display, or approve release. |
| Avoid parallel roots | Do not create duplicate schema, fixture, validator, policy, proof, receipt, graph, map, or release homes under this path. |

## Validation

```bash
find schemas/tests/valid -maxdepth 4 -type f | sort
find schemas/contracts/v1 -maxdepth 5 -type f 2>/dev/null | sort
find fixtures -maxdepth 5 -type f 2>/dev/null | sort
pytest tests/schemas tests/contract || true
```

Replace `|| true` with fail-closed CI behavior once the relevant test paths are confirmed.

## Open questions

| Question | Status |
|---|---|
| Should `schemas/tests/valid/` remain as a compatibility index or be retired after migration? | NEEDS VERIFICATION |
| Should non-`domains/` child paths such as `hazards/` and `roads-rail-trade/` move under `domains/`? | NEEDS VERIFICATION |
| Should valid schema tests be generated from fixture manifests rather than maintained under this path? | NEEDS VERIFICATION |
| Which accepted test root should own executable valid schema-test code? | NEEDS VERIFICATION |
