<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-domains-habitat-ecoregions-readme
title: Habitat Ecoregions Test README
type: test-readme
version: v0.1
status: draft; placeholder-expanded; test-lane; PROPOSED / NEEDS VERIFICATION before promotion
owners:
  - OWNER_TBD — Habitat domain steward
  - OWNER_TBD — Ecoregions steward
  - OWNER_TBD — Spatial Foundation reviewer
  - OWNER_TBD — Source steward
  - OWNER_TBD — Evidence steward
  - OWNER_TBD — Policy steward
  - OWNER_TBD — Validation steward
  - OWNER_TBD — Release steward
  - OWNER_TBD — QA steward
created: NEEDS VERIFICATION — blank placeholder existed before v0.1 expansion
updated: 2026-07-05
policy_label: public-doc; tests; habitat; ecoregions; regionalization-context; no-network; public-safe; source-role-aware; release-gated
tags: [kfm, tests, habitat, ecoregions, regionalization, ecological-system, ecoregion-framework, ecoregion-snapshot, context-join, source-role, EvidenceBundle, PolicyDecision, PMTiles, geoprivacy, ABSTAIN, DENY]
related:
  - ../../../README.md
  - ../../../../fixtures/domains/habitat/ecoregions/README.md
  - ../../../../fixtures/domains/habitat/README.md
  - ../../../../docs/domains/habitat/sublanes/ecoregions.md
  - ../../../../docs/domains/habitat/README.md
  - ../../../../docs/domains/habitat/SOURCE_FAMILIES.md
  - ../../../../docs/domains/habitat/API_CONTRACTS.md
  - ../../../../contracts/domains/habitat/ecoregions/README.md
  - ../../../../pipeline_specs/habitat/ecoregions/README.md
  - ../../../../pipelines/domains/habitat/ecoregions/README.md
  - ../../../../data/registry/sources/habitat/ecoregions/README.md
  - ../../../../data/catalog/domain/habitat/ecoregions/README.md
  - ../../../../data/published/layers/habitat/ecoregions/README.md
  - ../../../../release/candidates/habitat/ecoregions/README.md
notes:
  - "This file replaces a blank placeholder at tests/domains/habitat/ecoregions/README.md."
  - "This is a test-lane README only. It does not define Habitat ecoregion doctrine, semantic contracts, schemas, source descriptors, pipeline logic, policy rules, fixtures, lifecycle records, public tiles, release decisions, or published artifacts."
  - "The tested invariant is that ecoregions are regionalization context: they classify places by named framework, source version, hierarchy level, and boundary version; they do not prove species occurrence, plant occurrence, habitat-patch quality, regulatory designation, hydrology truth, soil truth, hazards truth, agriculture truth, land/title truth, or release state."
  - "The default posture is deterministic and no-network. Live source checks, credentials, real source exports, sensitive occurrence records, and public tiles do not belong in this lane."
  - "Rollback target for this replacement is previous blank blob SHA 8b137891791fe96927ad78e64b0aad7bded08bdc."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Habitat ecoregions tests

> Deterministic, no-network test documentation for proving that Habitat ecoregion records remain regionalization context, preserve framework/version/hierarchy/source-role/evidence boundaries, and fail closed when context is misused as occurrence, habitat quality, regulatory, or release truth.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: tests" src="https://img.shields.io/badge/root-tests%2F-blue">
  <img alt="Domain: habitat" src="https://img.shields.io/badge/domain-habitat-2e7d32">
  <img alt="Sublane: ecoregions" src="https://img.shields.io/badge/sublane-ecoregions-1b5e20">
  <img alt="Network: disabled by default" src="https://img.shields.io/badge/network-disabled__by__default-critical">
  <img alt="Truth: context not occurrence" src="https://img.shields.io/badge/truth-context__not__occurrence-success">
</p>

**Path:** `tests/domains/habitat/ecoregions/README.md`  
**Status:** draft / placeholder-expanded / PROPOSED until paired test files are verified  
**Owning root:** `tests/`  
**Domain segment:** `habitat`  
**Test lane:** `ecoregions`  
**Default execution posture:** deterministic, synthetic, no-network, public-safe fixtures only  
**Truth posture:** CONFIRMED target was a blank placeholder before this expansion · CONFIRMED `tests/` is the canonical root for enforceability proof · CONFIRMED Habitat ecoregions doctrine treats ecoregion polygons as regionalization context, not occurrence or species truth · CONFIRMED ecoregion fixture and contract README files exist and keep fixtures/contracts separate from tests, schemas, policy, source registries, lifecycle data, and release decisions · NEEDS VERIFICATION for actual test modules, fixtures, validators, schemas, source descriptors, policy engine wiring, CI coverage, release-gate integration, and pass rates.

**Quick jumps:** [Purpose](#purpose) · [Placement basis](#placement-basis) · [Invariant under test](#invariant-under-test) · [Expected test scope](#expected-test-scope) · [Fixture posture](#fixture-posture) · [Assertions](#assertions) · [Finite outcomes](#finite-outcomes) · [Forbidden shortcuts](#forbidden-shortcuts) · [Suggested test layout](#suggested-test-layout) · [Run posture](#run-posture) · [Evidence ledger](#evidence-ledger) · [Validation checklist](#validation-checklist) · [Rollback](#rollback)

---

## Purpose

`tests/domains/habitat/ecoregions/` is the intended home for tests that prove Habitat ecoregion and biophysical regionalization behavior stays inside its governed meaning.

This lane should test that ecoregion objects, joins, layer descriptors, renderer envelopes, catalog entries, Focus Mode payloads, and public-safe release candidates preserve:

- framework identity;
- source version and source role;
- hierarchy level and parent/child relationship;
- boundary version and geometry lineage;
- evidence and citation posture;
- context-join boundaries;
- public-safe geometry posture;
- policy, review, release, correction, and rollback state where material.

A passing test here should **not** mean that a real ecoregion source is current, a public layer is released, a species occurs in a region, a plant record is safe to expose, a habitat patch is high quality, or a regulatory designation exists. It should mean only that ecoregion-context guardrails behaved as expected against bounded fixtures.

---

## Placement basis

`tests/` is the canonical root for enforceability proof. Habitat appears as a lane segment inside the tests root, not as a repo-root domain folder.

| Responsibility | Correct home | This lane's relationship |
|---|---|---|
| Habitat ecoregion tests | `tests/domains/habitat/ecoregions/` | This directory. |
| Synthetic ecoregion fixtures | `fixtures/domains/habitat/ecoregions/` | Preferred toy inputs and expected outputs. |
| Ecoregion doctrine | `docs/domains/habitat/sublanes/ecoregions.md` | Referenced doctrine; not test implementation. |
| Semantic contracts | `contracts/domains/habitat/ecoregions/` | Defines meaning; tests do not redefine it. |
| Machine schemas | `schemas/contracts/v1/domains/habitat/ecoregions/` or accepted ADR alternative | Referenced by tests, not duplicated here. |
| Pipeline specs | `pipeline_specs/habitat/ecoregions/` | Declarative run/spec home; tests do not own specs. |
| Pipeline logic | `pipelines/domains/habitat/ecoregions/` | Executable processing under test; not duplicated here. |
| Source registry | `data/registry/sources/habitat/ecoregions/` and parent habitat registry | Source identity, role, rights, cadence, caveats, and activation state. |
| Catalog records | `data/catalog/domain/habitat/ecoregions/` | Catalog system under test; not duplicated here. |
| Published layers | `data/published/layers/habitat/ecoregions/` | Released artifacts only after governed promotion. |
| Release decisions | `release/` and `release/candidates/habitat/ecoregions/` | Promotion authority; tests cannot replace it. |

---

## Invariant under test

> **Ecoregions are regionalization context.** They classify places by a named framework, source version, hierarchy level, and boundary version. They do not become occurrence truth, habitat quality truth, regulatory truth, source truth, evidence truth, or release truth.

For this lane, the invariant decomposes into eight checks:

| Check | Required behavior | Failure outcome |
|---|---|---|
| Framework identity | Ecoregion records identify a named framework and source version. | validation failure / `ERROR`. |
| Hierarchy | Level and parent/child relation are explicit and internally consistent. | validation failure. |
| Source role | Source role is preserved through pipeline, catalog, API, renderer, and release-candidate output. | `DENY` / validation failure. |
| Evidence closure | Claim-bearing outputs resolve `EvidenceRef -> EvidenceBundle` or produce a finite non-answer. | `ABSTAIN`. |
| Context-join boundary | Joins to Fauna, Flora, Hydrology, Soil, Hazards, Agriculture, Spatial Foundation, or People/Land preserve owner authority. | `DENY` / `ABSTAIN`. |
| Public-safe geometry | Public derivatives include permitted geometry, CRS, simplification/generalization, and attribute include-list posture. | validation failure / `RESTRICT`. |
| Release gating | Public layer/catalog/API/UI carriers require policy, review, release, correction, and rollback linkage where material. | promotion-blocking failure. |
| No truth upgrade | Ecoregion context is never upgraded into species occurrence, plant occurrence, habitat patch quality, critical habitat, or regulatory designation truth. | `DENY` / `ABSTAIN`. |

---

## Expected test scope

Tests in this lane should be small, synthetic, and deterministic. They may validate:

- schema-like checks for toy `EcoregionFramework`, `EcoregionSnapshot`, `EcoregionLevel`, `EcoregionBoundaryVersion`, and `EcoregionContextJoin` payloads;
- hierarchy checks for missing framework, missing level, invalid parent/child chain, duplicate region identity, or inconsistent boundary version;
- source-role checks for context/authority/model/aggregate/candidate separation;
- evidence closure for claim-bearing catalog/API/Evidence Drawer/Focus Mode examples;
- public-safe geometry and attribute include-list checks for PMTiles or map-layer candidates;
- cross-lane join denial when ecoregion context is used as fauna/flora occurrence proof or habitat patch quality proof;
- release-candidate failure when policy, review, proof, correction, or rollback references are missing;
- finite non-answer behavior when source, evidence, policy, sensitivity, or release posture is unresolved.

Live ecoregion source downloads, public tile generation, real sensitive occurrence joins, and provider credentials are out of scope for the default suite.

---

## Fixture posture

Use `fixtures/domains/habitat/ecoregions/` when possible.

Fixture requirements:

- synthetic and public-safe;
- deterministic and no-network;
- compact enough for review in a PR;
- explicit expected outcome;
- explicit framework, source version, hierarchy level, region ID, and boundary version where material;
- explicit source-role, rights, evidence, policy, review, release, correction, and rollback state where material;
- no real sensitive occurrence records, rare-plant locations, private land/owner detail, or protected habitat exposure;
- no live source exports, credentials, public tiles, or generated release artifacts.

Preferred fixture families:

| Fixture kind | Preferred lane | Example expected outcome |
|---|---|---|
| Valid synthetic ecoregion snapshot | `fixtures/domains/habitat/ecoregions/` | Accepted as regionalization context. |
| Missing framework or level | `fixtures/domains/habitat/ecoregions/` | validation failure / `ERROR`. |
| Invalid hierarchy chain | `fixtures/domains/habitat/ecoregions/` | validation failure. |
| Ecoregion used as species/plant occurrence proof | `fixtures/domains/habitat/ecoregions/` or habitat invalid lane | `ABSTAIN` / validation failure. |
| Ecoregion used as habitat patch quality proof | `fixtures/domains/habitat/ecoregions/` | `ABSTAIN`. |
| Public layer without release/generalization posture | `fixtures/domains/habitat/ecoregions/` | validation failure / review required. |
| Cross-lane join without EvidenceBundle support | `fixtures/domains/habitat/ecoregions/` | `ABSTAIN`. |

---

## Assertions

A useful Habitat ecoregions test should make the context boundary obvious.

### Positive path

- framework and source version are explicit;
- hierarchy level and parent/child relations are valid;
- source role and evidence posture are preserved;
- geometry lineage, CRS, and public-safe transform posture are recorded where relevant;
- context joins preserve the owning lane's authority;
- public-facing candidates cite evidence and carry policy/release/correction/rollback references where material.

### Negative path

- missing framework, source version, hierarchy level, or source role fails closed;
- ecoregion polygons cannot prove species occurrence, plant occurrence, habitat patch quality, critical habitat, hydrology truth, soil truth, hazards truth, agriculture truth, or land/title truth;
- sensitive occurrence joins cannot leak through regionalization context;
- public layer candidates without include-list, generalization, release, or rollback posture fail;
- generated summaries, map tiles, graph edges, catalog summaries, or README text cannot become root evidence.

---

## Finite outcomes

This lane should prefer explicit finite outcomes over loose pass/fail text.

| Condition | Expected outcome |
|---|---|
| Valid synthetic ecoregion context with evidence, policy, review, release, and rollback context | allowed downstream carrier / `ANSWER` only if citation-closed. |
| Missing framework, level, source role, or boundary version | validation failure / `ERROR`. |
| Ecoregion context used as occurrence or patch-quality proof | `ABSTAIN` / validation failure. |
| Cross-lane join lacks EvidenceBundle support | `ABSTAIN`. |
| Sensitive occurrence context would be exposed | `DENY` / `RESTRICT`. |
| Public layer lacks release/generalization/include-list posture | validation failure / promotion block. |
| Policy engine unavailable | `ERROR` or `ABSTAIN`, never public exposure. |

---

## Forbidden shortcuts

Do not use this test lane to:

- fetch live upstream source systems;
- store credentials or tokens;
- store real ecoregion source exports;
- store sensitive fauna/flora occurrence records or rare-plant locations;
- store public PMTiles, MVT, GeoParquet, release artifacts, or lifecycle data;
- redefine Habitat ecoregion doctrine, contracts, schemas, policy, source descriptors, fixtures, or release decisions;
- bypass `EvidenceRef -> EvidenceBundle` resolution;
- bypass geoprivacy or sensitivity review with a fixture flag;
- infer release state from file existence, layer name, map rendering, or AI wording;
- publish, promote, or release anything.

Any test that needs real source data or public tile output belongs in a gated integration tier with source admission, lifecycle state, policy, receipts, release controls, and rollback targets.

---

## Suggested test layout

The exact Python module names remain NEEDS VERIFICATION until the runner and existing test conventions are inspected. A minimal future layout could be:

```text
tests/domains/habitat/ecoregions/
├── README.md
├── test_framework_and_hierarchy.py       # framework/version/level/parent-child checks
├── test_context_not_occurrence_truth.py  # ecoregion context cannot prove fauna/flora occurrence
├── test_context_join_boundaries.py       # cross-lane owner/evidence/source-role preservation
├── test_public_layer_release_gate.py     # include-list/generalization/release/rollback required
└── test_finite_outcomes.py               # ABSTAIN/DENY/ERROR for unresolved evidence/policy/release
```

Keep helpers local only when they are test-specific. Shared ecoregion contracts, schemas, pipeline behavior, policy behavior, fixtures, source registries, evidence resolvers, or release behavior belong under their accepted responsibility roots.

---

## Run posture

Default run expectations:

```bash
pytest tests/domains/habitat/ecoregions
```

Status of the command above: **PROPOSED / NEEDS VERIFICATION**. It assumes `pytest` is the accepted test runner and that executable test modules exist. This README does not claim the command currently passes.

Expected CI posture:

- default suite: no-network, synthetic fixtures only;
- fail closed on missing framework, missing hierarchy, source-role collapse, missing evidence, sensitive-context exposure, unsupported cross-lane join, missing policy, missing release state, or tile/layer leakage;
- live-source or tile-generation checks: separate gated jobs only;
- release gate: ecoregion failures should block public catalog/API/map/tile/AI carrier promotion.

---

## Evidence ledger

| Evidence | Status | Supports | Limits |
|---|---|---|---|
| Previous target file | CONFIRMED | `tests/domains/habitat/ecoregions/README.md` existed as a blank placeholder before this replacement. | Did not define the lane. |
| `tests/README.md` | CONFIRMED | `tests/` is enforceability proof; domain-specific tests belong under `tests/domains/<domain>/`; default tests should avoid sensitive data and live network calls. | Does not prove habitat/ecoregions modules or pass rate. |
| `docs/domains/habitat/sublanes/ecoregions.md` | CONFIRMED doctrine / PROPOSED implementation | Ecoregions are regionalization context, not species occurrence or habitat-patch truth; cross-lane joins fail closed when sensitive context is involved. | Does not prove executable tests, schemas, policy, or CI. |
| `fixtures/domains/habitat/ecoregions/README.md` | CONFIRMED | Fixture lane is synthetic/public-safe and explicitly not source truth, lifecycle data, public tiles, release proof, species truth, plant truth, or publication state. | Does not prove payload inventory or consumer tests. |
| `contracts/domains/habitat/ecoregions/README.md` | CONFIRMED | Semantic contracts define ecoregion meaning, source role, evidence posture, public-safe geometry, correction, and rollback while excluding schemas, policy, lifecycle data, and release decisions. | Contract README is draft/PROPOSED and does not prove implementation. |
| Habitat source/catalog/published/release candidate lanes | CONFIRMED by repo search results | Adjacent responsibility homes exist for registry, catalog, published layers, and release candidates. | Contents and enforcement remain NEEDS VERIFICATION unless inspected. |

---

## Validation checklist

Before treating this README as implemented behavior, verify:

- [ ] Executable test modules exist under this lane.
- [ ] Test runner and import paths match the repo's accepted convention.
- [ ] Synthetic fixtures exist for valid snapshot, missing framework, missing level, invalid hierarchy, context-as-occurrence, context-as-patch-quality, public-layer-without-release, sensitive-context exposure, and cross-lane EvidenceBundle failure.
- [ ] Ecoregion contract/schema paths are accepted.
- [ ] SourceDescriptor/source-role behavior is available to tests or safely stubbed.
- [ ] EvidenceRef / EvidenceBundle resolver behavior is available to tests or safely stubbed.
- [ ] PolicyDecision and geoprivacy behavior are available to tests or safely stubbed.
- [ ] Public layer include-list, CRS, generalization, and release/rollback expectations are defined before enforcing them.
- [ ] CI runs the no-network habitat ecoregions suite.
- [ ] Failures block public carrier promotion or release candidate approval.

---

## Rollback

Rollback is required if this lane becomes a source registry, fixture root, lifecycle data store, semantic-contract root, schema authority, policy authority, proof store, receipt store, release-decision root, public map/API/tile surface, AI surface, or publication shortcut.

Rollback target for this replacement: previous blank blob SHA `8b137891791fe96927ad78e64b0aad7bded08bdc`.

<p align="right"><a href="#top">Back to top</a></p>
