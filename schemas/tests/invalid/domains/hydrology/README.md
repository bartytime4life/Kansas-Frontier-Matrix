# `schemas/tests/invalid/domains/hydrology/` — Hydrology Invalid Schema Test Guardrail

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/schemas-tests-invalid-domains-hydrology-readme
title: schemas/tests/invalid/domains/hydrology/ README
type: readme; compatibility-index; invalid-test-placement-guardrail
version: v0.1
status: draft; empty-invalid-test-path; hydrology-boundary-sensitive; NEEDS VERIFICATION
updated: 2026-07-04
policy_label: public
tags: [kfm, schemas, tests, invalid, domains, hydrology, fixtures, evidence, source-role, release, compatibility]
[/KFM_META_BLOCK_V2] -->

## Purpose

`schemas/tests/invalid/domains/hydrology/` is a README-only compatibility guardrail for invalid Hydrology schema-test placement.

The inspected Hydrology domain schema lane lives at `schemas/contracts/v1/domains/hydrology/`.

The inspected Hydrology invalid fixture lane lives at `fixtures/domains/hydrology/invalid/`.

## Status

| Item | Status |
|---|---|
| README | present |
| Direct invalid test files found under this path | none found in current search |
| Current role | compatibility guardrail |
| Placement | NEEDS VERIFICATION |
| Hydrology posture | source-role, evidence, rights, release, and trust-membrane boundaries must stay explicit |

## Boundary

This directory is not the Hydrology schema family, Hydrology fixture authority, policy authority, validator implementation, CI configuration, emitted test-result store, data root, proof root, or release root.

It should not contain canonical Hydrology schemas, source records, lifecycle data, actual EvidenceBundles, proof packs, public map payloads, release records, direct model-runtime output, or validator code while accepted homes remain separate.

A failing or passing test here would prove only the tested shape behavior. It would not prove evidence truth, source authority, policy approval, rights clearance, release readiness, Hydrology truth, or public-safety.

## Current inventory

| Path | Status | Notes |
|---|---|---|
| `schemas/tests/invalid/domains/hydrology/README.md` | present | Empty file expanded by this README. |
| `schemas/tests/invalid/domains/hydrology/*` | not found in current search | No direct invalid test files were found under this path. |
| `schemas/contracts/v1/domains/hydrology/README.md` | present | Inspected Hydrology domain schema index. |
| `fixtures/domains/hydrology/invalid/README.md` | present | Inspected Hydrology invalid fixture lane. |
| `fixtures/domains/hydrology/negative/README.md` | present by search | Nearby negative fixture lane; not opened in this pass. |
| `fixtures/domains/hydrology/decision_envelope/invalid/README.md` | present by search | Family-specific invalid runtime envelope lane; not opened in this pass. |
| `fixtures/domains/hydrology/evidence_bundle/invalid/README.md` | present by search | Family-specific invalid evidence-support lane; not opened in this pass. |
| `fixtures/domains/hydrology/run_receipt/invalid/README.md` | present by search | Family-specific invalid run receipt lane; not opened in this pass. |
| `fixtures/domains/hydrology/golden/README.md` | present by search | Nearby expected-output fixture lane; not opened in this pass. |

## Correct nearby lanes

| Need | Preferred lane |
|---|---|
| Hydrology schema shape | `schemas/contracts/v1/domains/hydrology/` |
| Hydrology semantic meaning | `contracts/domains/hydrology/` |
| Broad invalid Hydrology examples | `fixtures/domains/hydrology/invalid/` |
| Negative-path Hydrology examples | `fixtures/domains/hydrology/negative/` |
| Decision envelope invalid examples | `fixtures/domains/hydrology/decision_envelope/invalid/` |
| EvidenceBundle invalid examples | `fixtures/domains/hydrology/evidence_bundle/invalid/` |
| Run receipt invalid examples | `fixtures/domains/hydrology/run_receipt/invalid/` |
| Expected outputs or golden cases | `fixtures/domains/hydrology/golden/` |
| Schema test code | `tests/schemas/` or accepted project test root |
| Validator implementation | `tools/validators/` |
| Hydrology policy posture | `policy/domains/hydrology/` and accepted sensitivity/access policy roots |
| Release, correction, rollback decisions | `release/` |

## What belongs here

- This README.
- Compatibility notes for this invalid schema-test path.
- Migration notes if historical invalid schema tests are discovered here.
- Temporary mirror notes while placement is unresolved.

## What does not belong here

- Canonical `.schema.json` files.
- Invalid fixture JSON files that should live under `fixtures/domains/hydrology/invalid/` or a family-specific fixture lane unless an accepted migration says otherwise.
- Real Hydrology records, source-system exports, lifecycle data, actual EvidenceBundles, proof packs, source descriptors, release manifests, public map payloads, tiles, direct model runtime output, source authority, policy authority, release authority, AI authority, or published artifacts.
- Policy rules, policy decisions, rights approvals, sensitivity approvals, release records, receipts, proofs, emitted validation reports, validator code, runtime code, or API/UI outputs.
- Claims that Hydrology data is valid, invalid, source-supported, rights-cleared, policy-approved, released, or public-safe merely because this path exists.

## Compatibility rules

| Rule | Requirement |
|---|---|
| Keep schemas versioned | Hydrology schemas belong under `schemas/contracts/v1/domains/hydrology/` unless an accepted migration says otherwise. |
| Keep fixtures in fixtures | Invalid examples belong under `fixtures/domains/hydrology/invalid/` or a family-specific fixture lane unless an accepted migration says otherwise. |
| Keep source roles separate | Invalid cases should preserve observation, regulatory context, model output, derived summary, and candidate boundaries. |
| Evidence remains separate | Test outcomes do not replace EvidenceBundles, proof records, or citation validation. |
| Tests are not publication | Test outcomes do not publish data or approve release. |
| Avoid parallel test roots | Add test files only to accepted test homes unless a migration note explains the exception. |

## Validation

```bash
find schemas/tests/invalid/domains/hydrology -maxdepth 4 -type f | sort
find fixtures/domains/hydrology/invalid -maxdepth 5 -type f 2>/dev/null | sort
find fixtures/domains/hydrology -path '*/invalid/*' -maxdepth 7 -type f 2>/dev/null | sort
find schemas/contracts/v1/domains/hydrology -maxdepth 4 -type f | sort
pytest tests/schemas tests/contract || true
```

Replace `|| true` with fail-closed CI behavior once the relevant test paths are confirmed.

## Open questions

| Question | Status |
|---|---|
| Should `schemas/tests/invalid/domains/hydrology/` remain as a compatibility guardrail or be retired? | NEEDS VERIFICATION |
| Are there historical references that expect invalid Hydrology schema tests under this path? | NEEDS VERIFICATION |
| Should invalid Hydrology tests be generated from `fixtures/domains/hydrology/invalid/` manifests? | NEEDS VERIFICATION |
| Which source-role, evidence-resolution, citation-validation, rights, sensitivity, release-readiness, and trust-membrane cases must be represented as invalid tests? | NEEDS VERIFICATION |
