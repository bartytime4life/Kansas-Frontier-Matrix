# `schemas/tests/invalid/domains/habitat/` — Habitat Invalid Schema Test Guardrail

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/schemas-tests-invalid-domains-habitat-readme
title: schemas/tests/invalid/domains/habitat/ README
type: readme; compatibility-index; invalid-test-placement-guardrail
version: v0.1
status: draft; empty-invalid-test-path; habitat-sensitive; NEEDS VERIFICATION
updated: 2026-07-04
policy_label: public
tags: [kfm, schemas, tests, invalid, domains, habitat, fixtures, land-cover, ecoregions, compatibility]
[/KFM_META_BLOCK_V2] -->

## Purpose

`schemas/tests/invalid/domains/habitat/` is a README-only compatibility guardrail for invalid Habitat schema-test placement.

The inspected Habitat domain schema lane lives at `schemas/contracts/v1/domains/habitat/`.

The inspected Habitat invalid fixture lane lives at `fixtures/domains/habitat/invalid/`.

## Status

| Item | Status |
|---|---|
| README | present |
| Direct invalid test files found under this path | none found in current search |
| Current role | compatibility guardrail |
| Placement | NEEDS VERIFICATION |
| Habitat posture | model/context/evidence boundaries must stay explicit |

## Boundary

This directory is not the Habitat schema family, Habitat fixture authority, policy authority, validator implementation, CI configuration, emitted test-result store, data root, or release root.

It should not contain canonical Habitat schemas, source records, lifecycle data, real EvidenceBundles, public map payloads, release records, or validator code while accepted homes remain separate.

A failing or passing test here would prove only the tested shape behavior. It would not prove evidence truth, habitat quality, regulatory status, policy approval, release readiness, or public-safety.

## Current inventory

| Path | Status | Notes |
|---|---|---|
| `schemas/tests/invalid/domains/habitat/README.md` | present | Empty file expanded by this README. |
| `schemas/tests/invalid/domains/habitat/*` | not found in current search | No direct invalid test files were found under this path. |
| `schemas/contracts/v1/domains/habitat/README.md` | present | Inspected Habitat domain schema index. |
| `fixtures/domains/habitat/invalid/README.md` | present | Inspected Habitat invalid fixture lane. |
| `fixtures/domains/habitat/golden/README.md` | present by search | Nearby expected-output fixture lane; not opened in this pass. |
| `fixtures/domains/habitat/ecoregions/README.md` | present by search | Nearby ecoregions fixture lane; not opened in this pass. |

## Correct nearby lanes

| Need | Preferred lane |
|---|---|
| Habitat schema shape | `schemas/contracts/v1/domains/habitat/` |
| Habitat semantic meaning | `contracts/domains/habitat/` |
| Invalid Habitat examples | `fixtures/domains/habitat/invalid/` |
| Expected outputs or golden cases | `fixtures/domains/habitat/golden/` |
| Ecoregion examples | `fixtures/domains/habitat/ecoregions/` |
| Schema test code | `tests/schemas/` or accepted project test root |
| Validator implementation | `tools/validators/` |
| Habitat policy posture | `policy/domains/habitat/` and accepted sensitivity policy roots |
| Release, correction, rollback decisions | `release/` |

## What belongs here

- This README.
- Compatibility notes for this invalid schema-test path.
- Migration notes if historical invalid schema tests are discovered here.
- Temporary mirror notes while placement is unresolved.

## What does not belong here

- Canonical `.schema.json` files.
- Invalid fixture JSON files that should live under `fixtures/domains/habitat/invalid/` unless an accepted migration says otherwise.
- Real Habitat records, source-system exports, lifecycle data, EvidenceBundles, proof packs, release manifests, public map payloads, tiles, regulatory truth, habitat quality claims, or cross-domain occurrence truth.
- Policy rules, policy decisions, sensitivity approvals, release records, receipts, proofs, emitted validation reports, validator code, runtime code, or API/UI outputs.
- Claims that Habitat data is valid, invalid, safe, approved, released, or regulatory truth merely because this path exists.

## Compatibility rules

| Rule | Requirement |
|---|---|
| Keep schemas versioned | Habitat schemas belong under `schemas/contracts/v1/domains/habitat/` unless an accepted migration says otherwise. |
| Keep fixtures in fixtures | Invalid examples belong under `fixtures/domains/habitat/invalid/` unless an accepted migration says otherwise. |
| Keep model and observation separate | Invalid cases should preserve model/observation/context/release boundaries. |
| Tests are not publication | Test outcomes do not publish data or approve release. |
| Avoid parallel test roots | Add test files only to accepted test homes unless a migration note explains the exception. |

## Validation

```bash
find schemas/tests/invalid/domains/habitat -maxdepth 4 -type f | sort
find fixtures/domains/habitat/invalid -maxdepth 5 -type f 2>/dev/null | sort
find schemas/contracts/v1/domains/habitat -maxdepth 4 -type f | sort
pytest tests/schemas tests/contract || true
```

Replace `|| true` with fail-closed CI behavior once the relevant test paths are confirmed.

## Open questions

| Question | Status |
|---|---|
| Should `schemas/tests/invalid/domains/habitat/` remain as a compatibility guardrail or be retired? | NEEDS VERIFICATION |
| Are there historical references that expect invalid Habitat schema tests under this path? | NEEDS VERIFICATION |
| Should invalid Habitat tests be generated from `fixtures/domains/habitat/invalid/` manifests? | NEEDS VERIFICATION |
| Which land-cover, ecoregion, model-vs-observation, context-join, and renderer-unsafe cases must be represented as invalid tests? | NEEDS VERIFICATION |
