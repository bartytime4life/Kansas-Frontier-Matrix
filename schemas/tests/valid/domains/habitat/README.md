# `schemas/tests/valid/domains/habitat/` — Habitat Valid Schema Test Guardrail

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/schemas-tests-valid-domains-habitat-readme
title: schemas/tests/valid/domains/habitat/ README
type: readme; compatibility-index; valid-test-placement-guardrail
version: v0.1
status: draft; empty-valid-test-path; habitat-boundary-sensitive; NEEDS VERIFICATION
updated: 2026-07-04
policy_label: public
tags: [kfm, schemas, tests, valid, domains, habitat, fixtures, land-cover, ecoregions, context-join, compatibility]
[/KFM_META_BLOCK_V2] -->

## Purpose

`schemas/tests/valid/domains/habitat/` is a README-only compatibility guardrail for valid Habitat schema-test placement.

The inspected Habitat domain schema lane lives at `schemas/contracts/v1/domains/habitat/`.

No dedicated `fixtures/domains/habitat/valid/README.md` was confirmed in current search. The closest inspected fixture anchor is `fixtures/domains/habitat/golden/`, with related land-cover and ecoregion fixture lanes present by search.

## Status

| Item | Status |
|---|---|
| README | present |
| Direct valid test files found under this path | none found in current search |
| Current role | compatibility guardrail |
| Placement | NEEDS VERIFICATION |
| Dedicated Habitat valid fixture lane | not confirmed in current search |
| Habitat posture | model, observation, evidence, context-join, policy, and release boundaries must stay explicit |

## Boundary

This directory is not the Habitat schema family, Habitat fixture authority, policy authority, validator implementation, CI configuration, emitted test-result store, data root, proof root, model-output root, map root, or release root.

It should not contain canonical Habitat schemas, source records, lifecycle data, real EvidenceBundles, model outputs, suitability claims, habitat-quality proof, regulatory designation truth, public map payloads, release records, or validator code while accepted homes remain separate.

A passing valid test here would prove only the tested shape behavior. It would not prove evidence truth, source authority, habitat quality, model validity, regulatory status, context-join validity, policy approval, rights clearance, release readiness, renderer safety, or public-safety.

## Current inventory

| Path | Status | Notes |
|---|---|---|
| `schemas/tests/valid/domains/habitat/README.md` | present | Empty file expanded by this README. |
| `schemas/tests/valid/domains/habitat/*` | not found in current search | No direct valid test files were found under this path. |
| `schemas/contracts/v1/domains/habitat/README.md` | present | Inspected Habitat domain schema index. |
| `schemas/contracts/v1/domains/habitat/land_cover/README.md` | present by search | Draft Habitat Land Cover schema index. |
| `schemas/contracts/v1/domains/habitat/ecoregions/README.md` | present by search | Draft Habitat Ecoregions schema index. |
| `fixtures/domains/habitat/valid/README.md` | not found in current search | Dedicated valid fixture lane NEEDS VERIFICATION. |
| `fixtures/domains/habitat/golden/README.md` | present | Inspected expected-output fixture lane. |
| `fixtures/domains/habitat/land_cover/class_scheme/README.md` | present by search | Nearby land-cover fixture lane; not opened in this pass. |
| `fixtures/domains/habitat/land_cover/change_summary/README.md` | present by search | Nearby land-cover fixture lane; not opened in this pass. |

## Correct nearby lanes

| Need | Preferred lane |
|---|---|
| Habitat schema shape | `schemas/contracts/v1/domains/habitat/` |
| Habitat land-cover schema shape | `schemas/contracts/v1/domains/habitat/land_cover/` |
| Habitat ecoregion schema shape | `schemas/contracts/v1/domains/habitat/ecoregions/` |
| Habitat semantic meaning | `contracts/domains/habitat/` |
| Valid Habitat examples | fixture lane NEEDS VERIFICATION |
| Expected outputs or golden cases | `fixtures/domains/habitat/golden/` |
| Ecoregion examples | `fixtures/domains/habitat/ecoregions/` where present |
| Land-cover examples | `fixtures/domains/habitat/land_cover/` where present |
| Schema test code | `tests/schemas/` or accepted project test root |
| Validator implementation | `tools/validators/` |
| Habitat policy posture | `policy/domains/habitat/` and accepted sensitivity/access policy lanes |
| Release, correction, rollback decisions | `release/` |

## What belongs here

- This README.
- Compatibility notes for this valid schema-test path.
- Migration notes if historical valid schema tests are discovered here.
- Temporary mirror notes while valid schema-test and Habitat fixture placement are unresolved.

## What does not belong here

- Canonical `.schema.json` files.
- Valid fixture JSON, YAML, GeoJSON, or expected-output files that should live under an accepted Habitat fixture lane unless an accepted migration says otherwise.
- Real Habitat records, land-cover observations, ecoregion records, source-system exports, lifecycle data, EvidenceBundles, proof packs, model outputs, suitability outputs, release manifests, public map payloads, public tiles, or generated-answer artifacts.
- Policy rules, policy decisions, rights approvals, sensitivity approvals, release records, emitted validation reports, validator code, runtime code, package code, or API/UI outputs.
- Claims that Habitat data is evidence-supported, topology-valid, hierarchy-valid, context-join-valid, policy-approved, released, renderer-safe, public-safe, or domain truth merely because a payload passes a schema test.

## Compatibility rules

| Rule | Requirement |
|---|---|
| Keep schemas versioned | Habitat schemas belong under `schemas/contracts/v1/domains/habitat/` and accepted child lanes unless an accepted migration says otherwise. |
| Keep fixtures in fixtures | Valid examples should live under an accepted Habitat fixture lane, not under this guardrail. |
| Keep model and observation separate | Valid cases must not collapse model output, observation, context, evidence, and release state. |
| Keep joins bounded | A valid Habitat context join does not become Fauna, Flora, Hydrology, Soil, Hazards, land/title, or regulatory truth. |
| Shape is not approval | Passing schema validation does not prove evidence closure, rights, policy, review, release, topology, hierarchy, or renderer safety. |
| Tests are not publication | Test outcomes do not publish data, authorize map display, or approve release. |
| Avoid parallel test roots | Add test files only to accepted test homes unless a migration note explains the exception. |

## Validation

```bash
find schemas/tests/valid/domains/habitat -maxdepth 4 -type f | sort
find fixtures/domains/habitat -maxdepth 5 -type f 2>/dev/null | sort
find schemas/contracts/v1/domains/habitat -maxdepth 5 -type f | sort
pytest tests/schemas tests/contract || true
```

Replace `|| true` with fail-closed CI behavior once the relevant test paths are confirmed.

## Open questions

| Question | Status |
|---|---|
| Should `schemas/tests/valid/domains/habitat/` remain as a compatibility guardrail or be retired? | NEEDS VERIFICATION |
| Are there historical references that expect valid Habitat schema tests under this path? | NEEDS VERIFICATION |
| Should a dedicated `fixtures/domains/habitat/valid/` lane exist, or should valid cases stay in object-family fixture lanes? | NEEDS VERIFICATION |
| Should valid Habitat tests be generated from fixture manifests instead of maintained under `schemas/tests/valid/`? | NEEDS VERIFICATION |
| Which land-cover, ecoregion, topology, hierarchy, context-join, model-vs-observation, EvidenceBundle, renderer-safe, and release-visible cases must be represented as valid tests? | NEEDS VERIFICATION |
