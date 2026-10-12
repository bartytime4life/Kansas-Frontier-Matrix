# `schemas/tests/valid/hazards/` — Hazards Valid Schema Test Guardrail

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/schemas-tests-valid-hazards-readme
title: schemas/tests/valid/hazards/ README
type: readme; compatibility-index; valid-test-placement-guardrail
version: v0.1
status: draft; empty-valid-test-path; non-domain-test-path; hazards-life-safety-boundary; NEEDS VERIFICATION
updated: 2026-07-04
policy_label: public
tags: [kfm, schemas, tests, valid, hazards, fixtures, freshness, evidence, trust-membrane, life-safety-boundary, compatibility]
[/KFM_META_BLOCK_V2] -->

## Purpose

`schemas/tests/valid/hazards/` is a README-only compatibility guardrail for valid Hazards schema-test placement.

The inspected Hazards schema lane lives at `schemas/contracts/v1/domains/hazards/`.

The inspected Hazards valid fixture lane lives at `fixtures/domains/hazards/valid/`.

## Status

| Item | Status |
|---|---|
| README | present |
| Direct valid test files found under this path | none found in current search |
| Current role | compatibility guardrail |
| Placement | NEEDS VERIFICATION |
| Path posture | non-`domains/` test path; keep Hazards schema-home conflict visible |
| Hazards boundary | not life-safety, emergency-alert, or operational-instruction authority |

## Boundary

This directory is not the Hazards schema family, Hazards fixture authority, policy authority, validator implementation, CI configuration, emitted test-result store, data root, proof root, alerting root, map root, or release root.

It should not contain canonical Hazards schemas, source records, lifecycle data, EvidenceBundles, proof packs, public map payloads, release records, operational alerts, life-safety instructions, direct model-runtime output, or validator code while accepted homes remain separate.

A passing valid test here would prove only the tested shape behavior. It would not prove evidence truth, source authority, freshness, citation validity, policy approval, sensitivity approval, release readiness, emergency-alert authority, life-safety authority, implementation proof, or public-safety.

## Current inventory

| Path | Status | Notes |
|---|---|---|
| `schemas/tests/valid/hazards/README.md` | present | Empty file expanded by this README. |
| `schemas/tests/valid/hazards/*` | not found in current search | No direct valid test files were found under this path. |
| `schemas/contracts/v1/domains/hazards/README.md` | present | Inspected Hazards domain schema index. |
| `schemas/contracts/v1/domains/hazards/receipts/README.md` | present by search | Draft Hazards receipts schema index; not reopened in this pass. |
| `fixtures/domains/hazards/valid/README.md` | present | Inspected Hazards valid fixture lane. |
| `fixtures/domains/hazards/golden/README.md` | present by search | Nearby expected-output fixture lane; not opened in this pass. |

## Correct nearby lanes

| Need | Preferred lane |
|---|---|
| Hazards schema shape | `schemas/contracts/v1/domains/hazards/` |
| Hazards semantic meaning | `contracts/domains/hazards/` |
| Valid Hazards examples | `fixtures/domains/hazards/valid/` |
| Expected outputs or golden cases | `fixtures/domains/hazards/golden/` |
| Schema test code | `tests/schemas/` or accepted project test root |
| Validator implementation | `tools/validators/` |
| Hazards policy posture | `policy/domains/hazards/` or accepted freshness/sensitivity/access policy lane |
| Release, correction, rollback decisions | `release/` |

## What belongs here

- This README.
- Compatibility notes for this valid schema-test path.
- Migration notes if historical Hazards valid schema tests are discovered here.
- Temporary mirror notes while Hazards schema-home and test-placement questions remain unresolved.

## What does not belong here

- Canonical `.schema.json` files.
- Valid fixture JSON, YAML, JSONL, SVG, or expected-output files that should live under `fixtures/domains/hazards/valid/` or `fixtures/domains/hazards/golden/` unless an accepted migration assigns them here.
- Real hazard records, source-system exports, lifecycle data, EvidenceBundles, proof packs, release manifests, public map payloads, public tiles, operational alerts, emergency instructions, or direct model-runtime output.
- Policy rules, policy decisions, rights approvals, sensitivity approvals, freshness approvals, release records, receipts, proofs, emitted validation reports, validator code, runtime code, package code, or API/UI outputs.
- Claims that Hazards data is evidence-supported, source-admitted, citation-valid, current, policy-approved, released, alert-authoritative, life-safety-authoritative, implementation-proven, or public-safe merely because this path exists or because a payload passes schema validation.

## Compatibility rules

| Rule | Requirement |
|---|---|
| Keep schema-home conflict visible | Do not hide unresolved Hazards schema-home drift while using this compatibility path. |
| Keep schemas in schema lanes | Hazards schemas belong in accepted schema homes, not in this test guardrail. |
| Keep fixtures in fixtures | Valid examples should live in `fixtures/domains/hazards/valid/` unless an accepted migration says otherwise. |
| Preserve source roles | Valid tests must not collapse observed events, regulatory context, modeled detections, warning context, and public derivatives. |
| Preserve freshness | Valid tests must keep source time, issue time, expiry time, retrieval time, release time, and correction time separate where material. |
| Life-safety boundary stays visible | Valid tests must not turn Hazards into emergency-alert, routing, evacuation, or operational-instruction authority. |
| Shape is not approval | Passing schema validation does not prove evidence closure, citation validation, rights, policy, review, release, or trust-membrane safety. |
| Tests are not publication | Test outcomes do not publish data, authorize map display, provide alerts, or approve release. |
| Avoid parallel test roots | Add test files only to accepted test homes unless a migration note explains the exception. |

## Validation

```bash
find schemas/tests/valid/hazards -maxdepth 4 -type f | sort
find schemas/contracts/v1/domains/hazards -maxdepth 5 -type f 2>/dev/null | sort
find fixtures/domains/hazards/valid -maxdepth 5 -type f 2>/dev/null | sort
find fixtures/domains/hazards/golden -maxdepth 5 -type f 2>/dev/null | sort
pytest tests/schemas tests/contract || true
```

Replace `|| true` with fail-closed CI behavior once the relevant test paths are confirmed.

## Open questions

| Question | Status |
|---|---|
| Should `schemas/tests/valid/hazards/` remain as a compatibility guardrail or be retired? | NEEDS VERIFICATION |
| Should valid Hazards schema tests live under `schemas/tests/valid/domains/hazards/` instead? | NEEDS VERIFICATION |
| Should valid Hazards tests be generated from `fixtures/domains/hazards/valid/` manifests? | NEEDS VERIFICATION |
| Which freshness, source-role, EvidenceBundle, citation-validation, drawer, Focus Mode, trust-membrane, release-readiness, and life-safety-boundary cases must be represented as valid tests? | NEEDS VERIFICATION |
