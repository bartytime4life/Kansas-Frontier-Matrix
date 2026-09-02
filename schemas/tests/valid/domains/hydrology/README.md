# `schemas/tests/valid/domains/hydrology/` — Hydrology Valid Schema Test Guardrail

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/schemas-tests-valid-domains-hydrology-readme
title: schemas/tests/valid/domains/hydrology/ README
type: readme; compatibility-index; valid-test-placement-guardrail
version: v0.1
status: draft; empty-valid-test-path; hydrology-boundary-sensitive; NEEDS VERIFICATION
updated: 2026-07-04
policy_label: public
tags: [kfm, schemas, tests, valid, domains, hydrology, fixtures, evidence, source-role, release, compatibility]
[/KFM_META_BLOCK_V2] -->

## Purpose

`schemas/tests/valid/domains/hydrology/` is a README-only compatibility guardrail for valid Hydrology schema-test placement.

The inspected Hydrology domain schema lane lives at `schemas/contracts/v1/domains/hydrology/`.

The inspected Hydrology valid fixture lane lives at `fixtures/domains/hydrology/valid/`.

## Status

| Item | Status |
|---|---|
| README | present |
| Direct valid test files found under this path | none found in current search |
| Current role | compatibility guardrail |
| Placement | NEEDS VERIFICATION |
| Hydrology posture | source-role, evidence, citation, rights, policy, release, and trust-membrane boundaries must stay explicit |

## Boundary

This directory is not the Hydrology schema family, Hydrology fixture authority, policy authority, validator implementation, CI configuration, emitted test-result store, data root, proof root, source-registry root, map root, or release root.

It should not contain canonical Hydrology schemas, source records, lifecycle data, SourceDescriptors, actual EvidenceBundles, actual RunReceipts, proof packs, public map payloads, release records, direct model-runtime output, or validator code while accepted homes remain separate.

A passing valid test here would prove only the tested shape behavior. It would not prove evidence truth, source authority, source admission, citation validity, policy approval, rights clearance, release readiness, Hydrology truth, implementation proof, or public-safety.

## Current inventory

| Path | Status | Notes |
|---|---|---|
| `schemas/tests/valid/domains/hydrology/README.md` | present | Empty file expanded by this README. |
| `schemas/tests/valid/domains/hydrology/*` | not found in current search | No direct valid test files were found under this path. |
| `schemas/contracts/v1/domains/hydrology/README.md` | present | Inspected Hydrology domain schema index. |
| `fixtures/domains/hydrology/valid/README.md` | present | Inspected Hydrology valid fixture lane. |
| `fixtures/domains/hydrology/golden/README.md` | present by search | Nearby expected-output fixture lane; not opened in this pass. |
| `fixtures/domains/hydrology/decision_envelope/valid/README.md` | present by fixture README reference | Family-specific valid runtime envelope lane; not opened in this pass. |
| `fixtures/domains/hydrology/evidence_bundle/valid/README.md` | present by fixture README reference | Family-specific valid evidence-support lane; not opened in this pass. |
| `fixtures/domains/hydrology/run_receipt/valid/README.md` | present by fixture README reference | Family-specific valid run receipt lane; not opened in this pass. |

## Correct nearby lanes

| Need | Preferred lane |
|---|---|
| Hydrology schema shape | `schemas/contracts/v1/domains/hydrology/` |
| Hydrology semantic meaning | `contracts/domains/hydrology/` |
| Broad valid Hydrology examples | `fixtures/domains/hydrology/valid/` |
| Decision envelope valid examples | `fixtures/domains/hydrology/decision_envelope/valid/` |
| EvidenceBundle valid examples | `fixtures/domains/hydrology/evidence_bundle/valid/` |
| Run receipt valid examples | `fixtures/domains/hydrology/run_receipt/valid/` |
| Expected outputs or golden cases | `fixtures/domains/hydrology/golden/` |
| Schema test code | `tests/schemas/` or accepted project test root |
| Validator implementation | `tools/validators/` |
| Hydrology policy posture | `policy/domains/hydrology/` and accepted sensitivity/access policy lanes |
| Release, correction, rollback decisions | `release/` |

## What belongs here

- This README.
- Compatibility notes for this valid schema-test path.
- Migration notes if historical valid Hydrology schema tests are discovered here.
- Temporary mirror notes while valid schema-test placement is unresolved.

## What does not belong here

- Canonical `.schema.json` files.
- Valid fixture JSON, YAML, JSONL, SVG, or expected-output files that should live under `fixtures/domains/hydrology/valid/` or a family-specific fixture lane unless an accepted migration says otherwise.
- Real Hydrology records, source-system exports, lifecycle data, SourceDescriptors, actual EvidenceBundles, actual RunReceipts, proof packs, release manifests, public map payloads, public tiles, direct model-runtime output, or generated-answer artifacts.
- Policy rules, policy decisions, rights approvals, sensitivity approvals, source activation decisions, release records, emitted validation reports, validator code, runtime code, package code, or API/UI outputs.
- Claims that Hydrology data is evidence-supported, source-admitted, citation-valid, rights-cleared, policy-approved, released, public-safe, implementation-proven, or domain truth merely because a payload passes a schema test.

## Compatibility rules

| Rule | Requirement |
|---|---|
| Keep schemas versioned | Hydrology schemas belong under `schemas/contracts/v1/domains/hydrology/` unless an accepted migration says otherwise. |
| Keep fixtures in fixtures | Valid examples belong under `fixtures/domains/hydrology/valid/` or a family-specific fixture lane unless an accepted migration says otherwise. |
| Keep source roles separate | Valid cases must preserve observation, regulatory context, model output, derived summary, source-like input, and release-facing derivative boundaries. |
| Evidence remains separate | Passing schema validation does not replace EvidenceBundles, proof records, citation validation, or evidence resolver checks. |
| Shape is not approval | Passing schema validation does not prove source admission, rights, policy, review, release, or trust-membrane safety. |
| Tests are not publication | Test outcomes do not publish data, authorize map display, or approve release. |
| Avoid parallel test roots | Add test files only to accepted test homes unless a migration note explains the exception. |

## Validation

```bash
find schemas/tests/valid/domains/hydrology -maxdepth 4 -type f | sort
find fixtures/domains/hydrology/valid -maxdepth 5 -type f 2>/dev/null | sort
find fixtures/domains/hydrology -path '*/valid/*' -maxdepth 7 -type f 2>/dev/null | sort
find schemas/contracts/v1/domains/hydrology -maxdepth 5 -type f | sort
pytest tests/schemas tests/contract || true
```

Replace `|| true` with fail-closed CI behavior once the relevant test paths are confirmed.

## Open questions

| Question | Status |
|---|---|
| Should `schemas/tests/valid/domains/hydrology/` remain as a compatibility guardrail or be retired? | NEEDS VERIFICATION |
| Are there historical references that expect valid Hydrology schema tests under this path? | NEEDS VERIFICATION |
| Should valid Hydrology tests be generated from `fixtures/domains/hydrology/valid/` manifests? | NEEDS VERIFICATION |
| Which source-role, EvidenceBundle, RunReceipt, decision-envelope, citation-validation, rights, sensitivity, release-readiness, and trust-membrane cases must be represented as valid tests? | NEEDS VERIFICATION |
