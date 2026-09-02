<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-domains-habitat-test-habitat-patch-readme
title: HabitatPatch Test README
type: test-readme
version: v0.1
status: draft; placeholder-expanded; test-lane; PROPOSED / NEEDS VERIFICATION before promotion
owners:
  - OWNER_TBD — Habitat domain steward
  - OWNER_TBD — HabitatPatch steward
  - OWNER_TBD — Evidence steward
  - OWNER_TBD — Source steward
  - OWNER_TBD — Policy steward
  - OWNER_TBD — Sensitivity reviewer
  - OWNER_TBD — Validation steward
  - OWNER_TBD — Release steward
  - OWNER_TBD — QA steward
created: NEEDS VERIFICATION — blank placeholder existed before v0.1 expansion
updated: 2026-07-05
policy_label: public-doc; tests; habitat; habitat-patch; no-network; polygonal-unit; public-safe-geometry; source-role-aware; evidence-bound; sensitivity-aware; release-gated; anti-collapse
tags: [kfm, tests, habitat, habitat_patch, test_habitat_patch, HabitatPatch, patch, polygonal-unit, public-safe-geometry, geoprivacy, source-role, LandCoverObservation, EcologicalSystem, SuitabilityModel, ConnectivityEdge, Corridor, EvidenceBundle, PolicyDecision, ReleaseManifest, CorrectionNotice, RollbackCard, ABSTAIN, DENY]
related:
  - ../../../README.md
  - ../README.md
  - ../../../../docs/domains/habitat/sublanes/patch.md
  - ../../../../docs/domains/habitat/sublanes/land_cover.md
  - ../../../../docs/domains/habitat/sublanes/ecological_systems.md
  - ../../../../docs/domains/habitat/sublanes/connectivity.md
  - ../../../../docs/domains/habitat/MODEL_VS_OBSERVATION.md
  - ../../../../docs/domains/habitat/SOURCE_FAMILIES.md
  - ../../../../contracts/domains/habitat/habitat_patch.md
  - ../../../../contracts/domains/habitat/habitat-patch.contract.md
  - ../../../../contracts/domains/habitat/ecological_system.md
  - ../../../../contracts/domains/habitat/SuitabilityModel.md
  - ../../../../contracts/domains/habitat/connectivity_edge.md
  - ../../../../contracts/domains/habitat/corridor.md
  - ../../../../contracts/domains/habitat/domain_feature_identity.md
  - ../../../../contracts/domains/habitat/domain_observation.md
  - ../../../../contracts/domains/habitat/land_cover/observation.md
  - ../../../../contracts/domains/habitat/land_cover/uncertainty.md
  - ../../../../schemas/contracts/v1/domains/habitat/habitat_patch.schema.json
  - ../../../../fixtures/domains/habitat/habitat_patch/
  - ../../../../pipelines/domains/habitat/
  - ../../../../pipeline_specs/habitat/
  - ../../../../policy/domains/habitat/
  - ../../../../policy/sensitivity/habitat/
  - ../../../../data/registry/sources/habitat/
  - ../../../../release/manifests/habitat/
notes:
  - "This file replaces a blank placeholder at tests/domains/habitat/test_habitat_patch/README.md."
  - "This is a test-lane README only. It does not define HabitatPatch doctrine, semantic contracts, schemas, fixtures, lifecycle records, evidence bundles, receipts, policy rules, release decisions, pipeline code, public API material, public map material, public tiles, or published artifacts."
  - "The tested invariant is that HabitatPatch is a governed discrete habitat unit and patch-geometry object. It must preserve patch identity, geometry posture, source support, classification support, temporal support, evidence support, sensitivity posture, public-safe geometry state, release relationship, correction, and rollback without becoming species occurrence truth, Flora vegetation-community ownership, regulatory critical habitat, suitability score, connectivity edge, corridor, management instruction, release authority, public-layer truth, or AI/UI truth."
  - "Default posture is deterministic and no-network. Live source checks, real source exports, lifecycle data, public tiles, and sensitive joined records do not belong in this lane."
  - "Rollback target for this replacement is previous blank blob SHA 8b137891791fe96927ad78e64b0aad7bded08bdc."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# HabitatPatch tests

> Deterministic, no-network test documentation for proving that Habitat `HabitatPatch` records remain governed discrete habitat units with inspectable source support, public-safe geometry, evidence, sensitivity posture, release relationship, correction path, and rollback target.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: tests" src="https://img.shields.io/badge/root-tests%2F-blue">
  <img alt="Domain: habitat" src="https://img.shields.io/badge/domain-habitat-2e7d32">
  <img alt="Lane: habitat patch" src="https://img.shields.io/badge/lane-habitat__patch-blue">
  <img alt="Network: disabled by default" src="https://img.shields.io/badge/network-disabled__by__default-critical">
  <img alt="Boundary: patch not occurrence" src="https://img.shields.io/badge/boundary-patch__not__occurrence-success">
</p>

**Path:** `tests/domains/habitat/test_habitat_patch/README.md`  
**Status:** draft / placeholder-expanded / PROPOSED until executable tests are verified  
**Owning root:** `tests/`  
**Domain segment:** `habitat`  
**Test lane:** `test_habitat_patch`  
**Default execution posture:** deterministic, synthetic, no-network, public-safe fixtures only  
**Truth posture:** CONFIRMED target was a blank placeholder before this expansion · CONFIRMED `tests/` is the canonical root for enforceability proof · CONFIRMED `HabitatPatch` is a Habitat-owned object family for discrete polygonal habitat units · CONFIRMED the HabitatPatch contract says it is not species occurrence truth, Flora vegetation-community ownership, regulatory critical habitat, modeled suitability, connectivity edge/corridor, or release authority · CONFIRMED the paired schema is a scaffold and field-level enforcement remains NEEDS VERIFICATION · NEEDS VERIFICATION for executable test modules, fixture payload inventory, validator behavior, source registry activation, policy runtime, release integration, public route/UI behavior, CI coverage, and pass rates.

**Quick jumps:** [Purpose](#purpose) · [Placement basis](#placement-basis) · [Invariant under test](#invariant-under-test) · [Expected scope](#expected-scope) · [Fixture posture](#fixture-posture) · [Assertions](#assertions) · [Finite outcomes](#finite-outcomes) · [Forbidden shortcuts](#forbidden-shortcuts) · [Suggested layout](#suggested-layout) · [Run posture](#run-posture) · [Evidence ledger](#evidence-ledger) · [Validation checklist](#validation-checklist) · [Rollback](#rollback)

---

## Purpose

`tests/domains/habitat/test_habitat_patch/` is the intended home for HabitatPatch tests.

This lane should prove that `HabitatPatch` records preserve patch identity, source role, geometry posture, classification support, temporal support, evidence, sensitivity, release, correction, and rollback boundaries. It should also prove that patch geometry and patch labels do not collapse into occurrence truth, vegetation-community ownership, regulatory designation, suitability score, connectivity/corridor output, public layer authority, or AI-generated truth.

A passing test here should **not** mean that a real patch is admitted, a public geometry is safe, a sensitive transform is accepted, or a release is approved. It should mean only that HabitatPatch guardrails behaved as expected against bounded fixtures.

---

## Placement basis

`tests/` is the canonical root for enforceability proof. Habitat is a domain segment inside that root. `test_habitat_patch` is a test lane, not a new root and not a parallel contract, schema, policy, data, release, proof, or public-map home.

| Responsibility | Correct home | This lane's relationship |
|---|---|---|
| HabitatPatch tests | `tests/domains/habitat/test_habitat_patch/` | This directory. |
| Patch doctrine | `docs/domains/habitat/sublanes/patch.md` | Referenced doctrine; tests do not redefine it. |
| HabitatPatch meaning | `contracts/domains/habitat/habitat_patch.md` | Schema-aligned semantic contract under test. |
| Expanded sibling contract | `contracts/domains/habitat/habitat-patch.contract.md` | Existing sibling; disposition remains NEEDS VERIFICATION. |
| Machine schema | `schemas/contracts/v1/domains/habitat/habitat_patch.schema.json` | Referenced where accepted; scaffold posture must be respected. |
| Fixtures | `fixtures/domains/habitat/habitat_patch/` | Preferred toy inputs and expected outcomes if populated. |
| Land-cover and ecological-system support | `contracts/domains/habitat/land_cover/observation.md`, `contracts/domains/habitat/ecological_system.md` | May support patch class/vintage/geometry; does not replace patch identity. |
| Policy and sensitivity homes | `policy/domains/habitat/`, `policy/sensitivity/habitat/` or inherited joined-lane homes where accepted | Referenced by tests, not bypassed here. |
| Release decisions | `release/` and `release/manifests/habitat/` | Publication, correction, and rollback authority; tests cannot replace it. |

---

## Invariant under test

> **HabitatPatch is patch identity and geometry, not occurrence or release truth.** A Habitat `HabitatPatch` record represents a discrete habitat unit, declared patch geometry, raster-derived polygon, inventory polygon, stewardship-bounded habitat area, or public-safe generalized habitat unit under source, role, evidence, policy, release, correction, and rollback controls.

Core checks:

| Check | Required behavior | Failure outcome |
|---|---|---|
| Patch identity | Stable ID, source support, object role, temporal scope, spatial scope, geometry fingerprint, and digest basis are explicit. | validation failure / `ERROR`. |
| Geometry posture | Internal, restricted, generalized, withheld, aggregate-only, or public-safe geometry state is explicit. | `DENY` / `RESTRICT` / validation failure. |
| Source role | Observation, model, context, regulatory, aggregate, candidate, synthetic, or derivative posture remains visible. | validation failure / `ABSTAIN`. |
| Classification support | Land-cover, ecological-system, and related class/crosswalk support are cited without replacing patch identity. | validation failure. |
| Evidence and uncertainty | Evidence and uncertainty/caveat refs are attached before consequential use. | `ABSTAIN`. |
| Sensitivity posture | Sensitive inputs or patch detail are generalized, restricted, withheld, or denied before public exposure. | `DENY` / `RESTRICT` / hold. |
| Release boundary | Policy, review, release, correction, and rollback remain separate from test pass state. | promotion block. |
| No authority upgrade | Patch cannot become occurrence truth, regulatory truth, suitability truth, connectivity truth, release authority, public-layer truth, or AI truth. | validation failure / `ABSTAIN`. |

---

## Expected scope

Tests in this lane may validate:

- required patch identity, source role, spatial scope, temporal scope, geometry posture, and digest posture;
- rejection of patch-as-occurrence, patch-as-regulatory-designation, patch-as-suitability-score, patch-as-connectivity-edge, or patch-as-corridor misuse;
- public-safe geometry, generalized geometry, withheld geometry, and aggregate-only posture before map/API/UI/AI carrier use;
- evidence and uncertainty requirements for consequential or public-facing use;
- rejection of public-facing candidates that lack evidence, policy, review, release relationship, correction, or rollback context;
- finite outcomes when evidence resolver, policy engine, source registry activation, uncertainty support, or release manifest is missing.

Live source checks, real source exports, production patch geometry, public tile generation, sensitive joined records, and provider-backed model calls are out of scope for the default suite.

---

## Fixture posture

Use synthetic, public-safe fixtures only.

Fixture requirements:

- deterministic and no-network;
- compact enough for review in a PR;
- explicit expected outcome;
- explicit patch identity, source role, geometry posture, classification support, evidence, uncertainty, policy, review, release relationship, correction, and rollback posture where material;
- no real source exports, lifecycle data, production patch geometry, public tiles, sensitive joined records, or published artifacts.

Preferred fixture families:

| Fixture kind | Expected outcome |
|---|---|
| Valid synthetic HabitatPatch with source role, geometry posture, evidence, uncertainty, and release relationship | accepted patch support only. |
| Missing patch identity or geometry posture | validation failure / `ERROR`. |
| Patch treated as occurrence or regulatory designation | validation failure / `ABSTAIN`. |
| Patch treated as suitability score, connectivity edge, or corridor | validation failure. |
| Public geometry exposed without public-safe posture | `DENY` / `RESTRICT`. |
| Public output lacks release/correction/rollback posture | promotion block. |
| AI/UI answer treats patch as truth | `ABSTAIN` / validation failure. |

---

## Assertions

A useful HabitatPatch test should make the patch boundary obvious.

### Positive path

- patch identity and geometry posture are explicit;
- source role, source support, and temporal support are visible;
- land-cover, ecological-system, context, model-run, and uncertainty support are linkable where material;
- evidence, policy, review, release relationship, correction, and rollback references are linkable where material;
- public-safe geometry and sensitivity posture are explicit where material.

### Negative path

- patch cannot become occurrence truth;
- patch cannot become vegetation-community authority, regulatory designation, suitability score, connectivity edge, corridor, or management instruction;
- patch geometry cannot hide provenance, uncertainty, or sensitivity posture;
- test pass cannot become release approval;
- map style, tile, popup, graph edge, Focus Mode answer, or AI text cannot become HabitatPatch authority;
- missing evidence produces `ABSTAIN` rather than a fluent claim.

---

## Finite outcomes

| Condition | Expected outcome |
|---|---|
| Valid synthetic HabitatPatch with geometry posture, evidence, uncertainty, policy, review, release relationship, correction, and rollback context | accepted patch support only. |
| Missing patch identity, source role, spatial/temporal scope, geometry posture, or digest basis | validation failure / `ERROR`. |
| Patch treated as occurrence, regulatory designation, suitability, connectivity, corridor, or source truth | validation failure. |
| Public-facing geometry lacks public-safe posture | `DENY` / `RESTRICT`. |
| Public-facing candidate lacks release/correction/rollback posture | promotion-blocking failure. |
| Policy engine unavailable | `ERROR` or `ABSTAIN`, never public exposure. |

---

## Forbidden shortcuts

Do not use this test lane to:

- fetch live upstream source systems;
- store real source exports, lifecycle data, production patch geometry, public tiles, or release artifacts;
- store proof packs, release manifests, or generated public layers;
- redefine HabitatPatch doctrine, contracts, schemas, fixtures, policy rules, receipts, proofs, release decisions, renderer code, or production code;
- bypass source role, geometry posture, evidence, uncertainty, validation, policy, review, correction, or rollback checks with a fixture flag;
- infer release state from file existence, test success, layer name, patch label, map rendering, tile availability, or AI wording;
- publish, promote, or release anything.

Any test that needs real patch geometry, source data, or public tile output belongs in a gated integration tier with source admission, lifecycle state, policy, receipts, release controls, and rollback targets.

---

## Suggested layout

The exact test module names remain **NEEDS VERIFICATION** until the runner and existing conventions are inspected.

```text
tests/domains/habitat/test_habitat_patch/
├── README.md
├── test_habitat_patch_identity.py
├── test_geometry_posture.py
├── test_source_role_required.py
├── test_patch_not_occurrence_or_regulatory_truth.py
├── test_patch_not_suitability_or_connectivity.py
├── test_public_safe_geometry.py
└── test_release_correction_rollback.py
```

---

## Run posture

```bash
pytest tests/domains/habitat/test_habitat_patch
```

Status of the command above: **PROPOSED / NEEDS VERIFICATION**. It assumes `pytest` is the accepted test runner and that executable test modules exist. This README does not claim the command currently passes.

---

## Evidence ledger

| Evidence | Status | Supports | Limits |
|---|---|---|---|
| Previous target file | CONFIRMED | `tests/domains/habitat/test_habitat_patch/README.md` existed as a blank placeholder before this replacement. | Did not define the lane. |
| `tests/README.md` | CONFIRMED | `tests/` is enforceability proof and failure should block promotion where trust-spine checks fail. | Does not prove this lane's modules or pass rate. |
| `contracts/domains/habitat/habitat_patch.md` | CONFIRMED semantic contract / PROPOSED implementation | Defines `HabitatPatch` as discrete habitat unit and patch geometry with source role, evidence, sensitivity, release, correction, and rollback constraints. | Schema is a permissive scaffold and sibling contract conflict remains NEEDS VERIFICATION. |
| `docs/domains/habitat/sublanes/patch.md` | CONFIRMED doctrine / PROPOSED implementation | HabitatPatch is a delineated habitat unit, not a raw land-cover tile or species record; public/3D surfaces require generalized geometry, and sensitive habitat is denied. | Implementation paths, validators, fixtures, schemas, policy runtime, release artifacts, UI, Focus Mode, and CI remain NEEDS VERIFICATION. |

---

## Validation checklist

Before treating this README as implemented behavior, verify:

- [ ] Executable test modules exist under this lane.
- [ ] Test runner and import paths match the repo's accepted convention.
- [ ] Synthetic fixtures exist for valid patch, missing identity, missing geometry posture, patch-as-occurrence, patch-as-regulatory, patch-as-suitability, patch-as-connectivity, missing public-safe geometry, and missing release/correction/rollback cases.
- [ ] HabitatPatch schema path and field expectations are accepted beyond scaffold status.
- [ ] The sibling contract conflict between `habitat_patch.md` and `habitat-patch.contract.md` is resolved or explicitly tolerated.
- [ ] EvidenceRef / EvidenceBundle behavior is available to tests or safely stubbed.
- [ ] SourceDescriptor/source-role behavior is available to tests or safely stubbed.
- [ ] PolicyDecision, ReviewRecord, ReleaseManifest, CorrectionNotice, RedactionReceipt, and RollbackCard expectations are defined before enforcing them.
- [ ] CI runs the no-network HabitatPatch suite.
- [ ] Failures block public carrier promotion or release candidate approval.

---

## Rollback

Rollback is required if this lane becomes a source export store, patch-geometry store, lifecycle data store, fixture root, contract root, schema authority, policy authority, proof store, release-decision root, public map/API/tile surface, AI surface, renderer implementation, pipeline implementation, or publication shortcut.

Rollback target for this replacement: previous blank blob SHA `8b137891791fe96927ad78e64b0aad7bded08bdc`.

<p align="right"><a href="#top">Back to top</a></p>
