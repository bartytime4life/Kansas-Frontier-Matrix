# `schemas/tests/invalid/hazards/` — Hazards Invalid Schema Test Guardrail

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/schemas-tests-invalid-hazards-readme
title: schemas/tests/invalid/hazards/ README
type: readme; compatibility-index; invalid-test-placement-guardrail
version: v0.1
status: draft; empty-invalid-test-path; non-domain-test-path; hazards-life-safety-boundary; NEEDS VERIFICATION
updated: 2026-07-04
policy_label: public
tags: [kfm, schemas, tests, invalid, hazards, fixtures, freshness, evidence, trust-membrane, life-safety-boundary, compatibility]
[/KFM_META_BLOCK_V2] -->

## Purpose

`schemas/tests/invalid/hazards/` is a README-only compatibility guardrail for invalid Hazards schema-test placement.

The inspected Hazards schema lane lives at `schemas/contracts/v1/domains/hazards/`.

The inspected Hazards invalid fixture lane lives at `fixtures/domains/hazards/invalid/`.

## Status

| Item | Status |
|---|---|
| README | present |
| Direct invalid test files found under this path | none found in current search |
| Current role | compatibility guardrail |
| Placement | NEEDS VERIFICATION |
| Path posture | non-`domains/` test path; keep Hazards schema-home conflict visible |
| Hazards boundary | not life-safety, emergency-alert, or operational-instruction authority |

## Boundary

This directory is not the Hazards schema family, Hazards fixture authority, policy authority, validator implementation, CI configuration, emitted test-result store, data root, proof root, alerting root, or release root.

It should not contain canonical Hazards schemas, source records, lifecycle data, EvidenceBundles, proof packs, public map payloads, release records, operational alerts, life-safety instructions, direct model-runtime output, or validator code while accepted homes remain separate.

A failing or passing test here would prove only the tested shape behavior. It would not prove evidence truth, source authority, freshness, policy approval, sensitivity approval, release readiness, emergency-alert authority, life-safety authority, or public-safety.

## Current inventory

| Path | Status | Notes |
|---|---|---|
| `schemas/tests/invalid/hazards/README.md` | present | Empty file expanded by this README. |
| `schemas/tests/invalid/hazards/*` | not found in current search | No direct invalid test files were found under this path. |
| `schemas/contracts/v1/domains/hazards/README.md` | present | Inspected Hazards domain schema index. |
| `schemas/contracts/v1/domains/hazards/receipts/README.md` | present by search | Draft Hazards receipts schema index; not reopened in this pass. |
| `fixtures/domains/hazards/invalid/README.md` | present | Inspected Hazards invalid fixture lane. |
| `fixtures/domains/hazards/invalid/drawer_missing_disclaimer/README.md` | present by search | Child invalid fixture lane. |
| `fixtures/domains/hazards/invalid/expired_warning_as_current/README.md` | present by search | Child invalid fixture lane. |
| `fixtures/domains/hazards/invalid/focus_mode_as_alert/README.md` | present by search | Child invalid fixture lane. |
| `fixtures/domains/hazards/invalid/modeled_labeled_observed/README.md` | present by search | Child invalid fixture lane. |
| `fixtures/domains/hazards/invalid/regulatory_labeled_observed/README.md` | present by search | Child invalid fixture lane. |
| `fixtures/domains/hazards/invalid/temporal_role_swap/README.md` | present by search | Child invalid fixture lane. |
| `fixtures/domains/hazards/invalid/ui_reads_raw_directly/README.md` | present by search | Child invalid fixture lane. |
| `fixtures/domains/hazards/invalid/unresolved_evidence_ref/README.md` | present by search | Child invalid fixture lane. |

## Correct nearby lanes

| Need | Preferred lane |
|---|---|
| Hazards schema shape | `schemas/contracts/v1/domains/hazards/` |
| Hazards semantic meaning | `contracts/domains/hazards/` |
| Hazards invalid examples | `fixtures/domains/hazards/invalid/` |
| Expected outputs or golden cases | `fixtures/domains/hazards/golden/` where present |
| Schema test code | `tests/schemas/` or accepted project test root |
| Validator implementation | `tools/validators/` |
| Hazards policy posture | `policy/domains/hazards/` or accepted freshness/sensitivity/access policy lane |
| Release, correction, rollback decisions | `release/` |

## What belongs here

- This README.
- Compatibility notes for this invalid schema-test path.
- Migration notes if historical Hazards invalid schema tests are discovered here.
- Temporary mirror notes while Hazards schema-home and test-placement questions remain unresolved.

## What does not belong here

- Canonical `.schema.json` files.
- Invalid fixture JSON files that should live under `fixtures/domains/hazards/invalid/` unless an accepted migration assigns them here.
- Real hazard records, source-system exports, lifecycle data, EvidenceBundles, proof packs, release manifests, public map payloads, public tiles, operational alerts, emergency instructions, or direct model-runtime output.
- Policy rules, policy decisions, rights approvals, sensitivity approvals, freshness approvals, release records, receipts, proofs, emitted validation reports, validator code, runtime code, package code, or API/UI outputs.
- Claims that Hazards data is valid, invalid, source-supported, current, policy-approved, released, alert-authoritative, life-safety-authoritative, or public-safe merely because this path exists.

## Compatibility rules

| Rule | Requirement |
|---|---|
| Keep schema-home conflict visible | Do not hide unresolved Hazards schema-home drift while using this compatibility path. |
| Keep schemas in schema lanes | Hazards schemas belong in accepted schema homes, not in this test guardrail. |
| Keep fixtures in fixtures | Invalid examples should live in `fixtures/domains/hazards/invalid/` unless an accepted migration says otherwise. |
| Preserve source roles | Invalid tests must not collapse observed events, regulatory context, modeled detections, warning context, and public derivatives. |
| Preserve freshness | Invalid tests must keep issue, expiry, retrieval, release, and correction time separate where material. |
| Tests are not publication | Test outcomes do not publish data, authorize map display, provide alerts, or approve release. |
| Avoid parallel test roots | Add test files only to accepted test homes unless a migration note explains the exception. |

## Validation

```bash
find schemas/tests/invalid/hazards -maxdepth 4 -type f | sort
find schemas/contracts/v1/domains/hazards -maxdepth 5 -type f 2>/dev/null | sort
find fixtures/domains/hazards/invalid -maxdepth 5 -type f 2>/dev/null | sort
pytest tests/schemas tests/contract || true
```

Replace `|| true` with fail-closed CI behavior once the relevant test paths are confirmed.

## Open questions

| Question | Status |
|---|---|
| Should `schemas/tests/invalid/hazards/` remain as a compatibility guardrail or be retired? | NEEDS VERIFICATION |
| Should invalid Hazards schema tests live under `schemas/tests/invalid/domains/hazards/` instead? | NEEDS VERIFICATION |
| Should invalid Hazards tests be generated from `fixtures/domains/hazards/invalid/` manifests? | NEEDS VERIFICATION |
| Which freshness, source-role, EvidenceBundle, drawer, Focus Mode, trust-membrane, release-readiness, and life-safety-boundary cases must be represented as invalid tests? | NEEDS VERIFICATION |
