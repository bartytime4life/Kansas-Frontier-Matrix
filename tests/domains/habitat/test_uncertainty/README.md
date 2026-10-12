<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-domains-habitat-test-uncertainty-readme
title: Habitat UncertaintySurface Test README
type: test-readme
version: v0.1
status: draft; placeholder-expanded; test-lane; PROPOSED / NEEDS VERIFICATION before promotion
owners:
  - OWNER_TBD — Habitat domain steward
  - OWNER_TBD — Uncertainty steward
  - OWNER_TBD — Suitability steward
  - OWNER_TBD — Evidence steward
  - OWNER_TBD — Source steward
  - OWNER_TBD — Policy steward
  - OWNER_TBD — Validation steward
  - OWNER_TBD — Release steward
  - OWNER_TBD — QA steward
created: NEEDS VERIFICATION — blank placeholder existed before v0.1 expansion
updated: 2026-07-05
policy_label: public-doc; tests; habitat; uncertainty; uncertainty-surface; no-network; uncertainty-required; evidence-bound; source-role-aware; release-gated; display-obligations; anti-collapse
tags: [kfm, tests, habitat, uncertainty, test_uncertainty, UncertaintySurface, uncertainty_surface, model-uncertainty, spatial-uncertainty, accuracy, confidence, valid-pixel-footprint, source-vintage, public-generalization, SuitabilityModel, HabitatQualityScore, HabitatPatch, RestorationOpportunity, Corridor, LandCoverObservation, EvidenceBundle, PolicyDecision, ReleaseManifest, CorrectionNotice, RollbackCard, ABSTAIN, DENY]
related:
  - ../../../README.md
  - ../README.md
  - ../land_cover/uncertainty/README.md
  - ../../../../contracts/domains/habitat/uncertainty_surface.md
  - ../../../../contracts/domains/habitat/land_cover/uncertainty.md
  - ../../../../contracts/domains/habitat/suitability_model.md
  - ../../../../contracts/domains/habitat/SuitabilityModel.md
  - ../../../../contracts/domains/habitat/habitat_quality_score.md
  - ../../../../contracts/domains/habitat/habitat_patch.md
  - ../../../../contracts/domains/habitat/restoration_opportunity.md
  - ../../../../contracts/domains/habitat/connectivity_edge.md
  - ../../../../contracts/domains/habitat/corridor.md
  - ../../../../contracts/domains/habitat/land_cover/observation.md
  - ../../../../contracts/domains/habitat/land_cover/model_run_receipt.md
  - ../../../../schemas/contracts/v1/domains/habitat/uncertainty_surface.schema.json
  - ../../../../schemas/contracts/v1/domains/habitat/land_cover/uncertainty.schema.json
  - ../../../../fixtures/domains/habitat/uncertainty_surface/
  - ../../../../fixtures/domains/habitat/land_cover/uncertainty/
  - ../../../../policy/domains/habitat/uncertainty_label.rego
  - ../../../../policy/sensitivity/habitat/
  - ../../../../data/registry/sources/habitat/
  - ../../../../release/manifests/habitat/
notes:
  - "This file replaces a blank placeholder at tests/domains/habitat/test_uncertainty/README.md."
  - "This is a Habitat-wide test-lane README only. It does not define UncertaintySurface doctrine, semantic contracts, schemas, fixtures, lifecycle records, evidence bundles, policy rules, release decisions, pipeline code, public API material, public map material, public tiles, or published artifacts."
  - "The tested invariant is that UncertaintySurface is required inspectable context for Habitat products that need uncertainty to be interpreted safely. It must preserve product attachment, uncertainty kind, source-role posture, spatial/temporal scope, model/run support, evidence support, display obligations, release relationship, correction, and rollback without becoming observation truth, model truth, proof closure, policy approval, release authority, public-layer truth, or AI/UI truth."
  - "The land-cover uncertainty lane remains the specialization for land-cover-specific accuracy, valid-pixel, nodata, source-vintage, crosswalk, and raster-quality checks."
  - "Default posture is deterministic and no-network. Live source checks, real source exports, lifecycle data, public tiles, and restricted joined records do not belong in this lane."
  - "Rollback target for this replacement is previous blank blob SHA 8b137891791fe96927ad78e64b0aad7bded08bdc."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Habitat UncertaintySurface tests

> Deterministic, no-network test documentation for proving that Habitat `UncertaintySurface` records remain required inspectable context, not replacement truth, proof, policy approval, release authority, public-layer truth, or AI/UI evidence.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: tests" src="https://img.shields.io/badge/root-tests%2F-blue">
  <img alt="Domain: habitat" src="https://img.shields.io/badge/domain-habitat-2e7d32">
  <img alt="Lane: uncertainty" src="https://img.shields.io/badge/lane-uncertainty-blue">
  <img alt="Network: disabled by default" src="https://img.shields.io/badge/network-disabled__by__default-critical">
  <img alt="Boundary: uncertainty not truth" src="https://img.shields.io/badge/boundary-uncertainty__not__truth-success">
</p>

**Path:** `tests/domains/habitat/test_uncertainty/README.md`  
**Status:** draft / placeholder-expanded / PROPOSED until executable tests are verified  
**Owning root:** `tests/`  
**Domain segment:** `habitat`  
**Test lane:** `test_uncertainty`  
**Specialized sibling lane:** `tests/domains/habitat/land_cover/uncertainty/`  
**Default execution posture:** deterministic, synthetic, no-network, public-safe fixtures only  
**Truth posture:** CONFIRMED target was a blank placeholder before this expansion · CONFIRMED `tests/` is the canonical root for enforceability proof · CONFIRMED the top-level `UncertaintySurface` contract treats uncertainty as a Habitat-wide object family, with land-cover uncertainty as a specialization · CONFIRMED the contract states uncertainty is not an observation, model, proof object, policy decision, release authority, or display detail that can be hidden for simplicity · CONFIRMED the paired schema is a scaffold and field-level enforcement remains NEEDS VERIFICATION · NEEDS VERIFICATION for executable test modules, fixture payload inventory, validator behavior, policy runtime, release integration, public route/UI behavior, CI coverage, and pass rates.

**Quick jumps:** [Purpose](#purpose) · [Placement basis](#placement-basis) · [Relationship to land-cover uncertainty](#relationship-to-land-cover-uncertainty) · [Invariant under test](#invariant-under-test) · [Expected scope](#expected-scope) · [Fixture posture](#fixture-posture) · [Finite outcomes](#finite-outcomes) · [Forbidden shortcuts](#forbidden-shortcuts) · [Suggested layout](#suggested-layout) · [Run posture](#run-posture) · [Evidence ledger](#evidence-ledger) · [Validation checklist](#validation-checklist) · [Rollback](#rollback)

---

## Purpose

`tests/domains/habitat/test_uncertainty/` is the intended Habitat-wide uncertainty test lane.

This lane should prove that `UncertaintySurface` records preserve product attachment, uncertainty kind, source-role posture, spatial and temporal scope, model/run support, evidence support, display obligations, policy posture, release relationship, correction path, and rollback target.

A passing test here should **not** mean that a real uncertainty surface is admitted, a model is validated, a public display is safe, or a release is approved. It should mean only that uncertainty guardrails behaved as expected against bounded fixtures.

---

## Placement basis

`tests/` is the canonical root for enforceability proof. Habitat is a domain segment inside that root. `test_uncertainty` is a Habitat-wide object-family test lane, not a new root and not a replacement for the detailed land-cover uncertainty specialization.

| Responsibility | Correct home | This lane's relationship |
|---|---|---|
| Habitat-wide uncertainty tests | `tests/domains/habitat/test_uncertainty/` | This directory. |
| Land-cover uncertainty tests | `tests/domains/habitat/land_cover/uncertainty/` | Specialized child/sibling lane for land-cover accuracy, valid-pixel, nodata, source-vintage, crosswalk, and raster-quality checks. |
| Habitat-wide uncertainty meaning | `contracts/domains/habitat/uncertainty_surface.md` | Semantic contract under test. |
| Land-cover uncertainty meaning | `contracts/domains/habitat/land_cover/uncertainty.md` | Specialization under test elsewhere. |
| Machine schemas | `schemas/contracts/v1/domains/habitat/uncertainty_surface.schema.json`, `schemas/contracts/v1/domains/habitat/land_cover/uncertainty.schema.json` | Referenced where accepted; scaffold posture must be respected. |
| Fixtures | `fixtures/domains/habitat/uncertainty_surface/`, `fixtures/domains/habitat/land_cover/uncertainty/` | Preferred toy inputs and expected outcomes if populated. |
| Policy homes | `policy/domains/habitat/uncertainty_label.rego`, `policy/sensitivity/habitat/` | Referenced by tests, not bypassed here. |
| Release decisions | `release/` and `release/manifests/habitat/` | Publication, correction, and rollback authority; tests cannot replace it. |

---

## Relationship to land-cover uncertainty

Use this lane for Habitat-wide uncertainty behavior across object families such as `SuitabilityModel`, `HabitatQualityScore`, `HabitatPatch`, `Corridor`, `RestorationOpportunity`, and public-safe derivatives.

Use `tests/domains/habitat/land_cover/uncertainty/` for land-cover-specific uncertainty behavior tied to `LandCoverObservation`, class schemes, crosswalks, valid-pixel support, nodata masks, source-vintage gaps, and raster or geometry quality.

This lane may smoke-test that the specialization exists and stays no-network, but it should not duplicate all land-cover-specific assertions.

---

## Invariant under test

> **Uncertainty is inspectable context, not replacement truth.** `UncertaintySurface` describes what is known, unknown, weakly supported, modeled, generalized, incomplete, stale, or display-limited about a Habitat product. It must travel with the product where material and must not be hidden to simplify a public story.

Core checks:

| Check | Required behavior | Failure outcome |
|---|---|---|
| Product attachment | The product, score, patch, surface, corridor, candidate, or public-safe derivative being described is explicit. | validation failure / `ERROR`. |
| Uncertainty kind | Model confidence, class accuracy, source-vintage gap, footprint, nodata, crosswalk loss, geometry quality, resolution quality, public-generalization caveat, or accepted kind is explicit. | validation failure. |
| Source-role posture | Uncertainty over observed, modeled, derived, aggregate, crosswalked, or public-derived material remains labeled. | validation failure / `ABSTAIN`. |
| Spatial and temporal support | Footprint, mask, extent, CRS, resolution, source time, valid time, run time, release time, and correction time stay distinct where material. | validation failure. |
| Evidence support | EvidenceRef/EvidenceBundle support resolves for consequential claims or produces a finite non-answer. | `ABSTAIN`. |
| Display obligations | Public carriers show modeled status, caveats, correction/stale state, and uncertainty labels where material. | review required / validation failure. |
| Release boundary | Policy, review, release, correction, and rollback remain separate from test pass state. | promotion block. |
| No authority upgrade | Uncertainty cannot become product truth, proof, policy approval, release authority, public-layer truth, or AI truth. | validation failure / `ABSTAIN`. |

---

## Expected scope

Tests in this lane may validate:

- required uncertainty identity, product attachment, uncertainty kind, source-role posture, spatial scope, temporal scope, evidence posture, and digest basis;
- rejection of uncertainty-as-observation, uncertainty-as-model, uncertainty-as-proof, uncertainty-as-policy, uncertainty-as-release, or uncertainty-as-public-layer-truth misuse;
- required uncertainty support for modeled suitability, habitat quality scores, corridors, restoration candidates, public-safe derivatives, and other Habitat products where material;
- display obligations for map/API/UI/AI carriers;
- rejection of public-facing candidates that drop caveats, correction state, release relationship, or rollback context;
- finite outcomes when evidence resolver, policy engine, model-run receipt, uncertainty schema, or release manifest is missing.

Live source checks, real source exports, production uncertainty rasters, public tile generation, restricted joined records, and provider-backed model calls are out of scope for the default suite.

---

## Fixture posture

Use synthetic, public-safe fixtures only.

Fixture requirements:

- deterministic and no-network;
- compact enough for review in a PR;
- explicit expected outcome;
- explicit product attachment, uncertainty kind, source-role posture, spatial/temporal scope, evidence, policy, review, release relationship, correction, and rollback posture where material;
- no real source exports, lifecycle data, production uncertainty rasters, public tiles, restricted joined records, or published artifacts.

---

## Finite outcomes

| Condition | Expected outcome |
|---|---|
| Valid synthetic UncertaintySurface with product attachment, kind, evidence, policy, review, release relationship, correction, and rollback context | accepted uncertainty support only. |
| Missing product attachment, uncertainty kind, source-role posture, spatial/temporal scope, or digest basis | validation failure / `ERROR` / `ABSTAIN`. |
| Uncertainty treated as product truth, proof, policy approval, release authority, or public-layer truth | validation failure. |
| Public-facing candidate hides material uncertainty | review required / `ABSTAIN` / promotion block. |
| Public-facing candidate lacks release/correction/rollback posture | promotion-blocking failure. |
| Policy engine unavailable | `ERROR` or `ABSTAIN`, never public exposure. |

---

## Forbidden shortcuts

Do not use this test lane to:

- fetch live upstream source systems;
- store real source exports, lifecycle data, production uncertainty rasters, public tiles, or release artifacts;
- store proof packs, release manifests, or generated public layers;
- redefine Habitat uncertainty doctrine, contracts, schemas, fixtures, policy rules, receipts, proofs, release decisions, renderer code, or production code;
- bypass product attachment, evidence, source role, uncertainty kind, display obligations, validation, policy, review, correction, or rollback checks with a fixture flag;
- infer release state from file existence, test success, layer name, uncertainty label, map rendering, tile availability, or AI wording;
- publish, promote, approve, or release anything.

Any test that needs real uncertainty outputs, source data, or public tile output belongs in a gated integration tier with source admission, lifecycle state, policy, receipts, release controls, and rollback targets.

---

## Suggested layout

The exact test module names remain **NEEDS VERIFICATION** until the runner and existing conventions are inspected.

```text
tests/domains/habitat/test_uncertainty/
├── README.md
├── test_uncertainty_surface_identity.py
├── test_product_attachment_required.py
├── test_uncertainty_kind_required.py
├── test_uncertainty_not_truth_authority.py
├── test_display_obligations.py
├── test_land_cover_specialization_boundary.py
└── test_release_correction_rollback.py
```

---

## Run posture

```bash
pytest tests/domains/habitat/test_uncertainty
```

For the land-cover specialization:

```bash
pytest tests/domains/habitat/land_cover/uncertainty
```

Status of both commands above: **PROPOSED / NEEDS VERIFICATION**. They assume `pytest` is the accepted test runner and that executable test modules exist. This README does not claim either command currently passes.

---

## Evidence ledger

| Evidence | Status | Supports | Limits |
|---|---|---|---|
| Previous target file | CONFIRMED | `tests/domains/habitat/test_uncertainty/README.md` existed as a blank placeholder before this replacement. | Did not define the lane. |
| `tests/README.md` | CONFIRMED | `tests/` is enforceability proof and failure should block promotion where trust-spine checks fail. | Does not prove this lane's modules or pass rate. |
| `contracts/domains/habitat/uncertainty_surface.md` | CONFIRMED semantic contract / PROPOSED implementation | Defines Habitat-wide `UncertaintySurface` and states land-cover uncertainty is a specialization, not a competing authority. | Schema is a permissive scaffold and field-level enforcement remains NEEDS VERIFICATION. |
| `tests/domains/habitat/land_cover/uncertainty/README.md` | CONFIRMED specialization README | Documents the existing land-cover uncertainty test lane and its boundary that uncertainty is not observation truth, proof, policy approval, release authority, public-layer truth, or AI/UI evidence. | Does not prove executable tests or pass rate. |

---

## Validation checklist

Before treating this README as implemented behavior, verify:

- [ ] Executable test modules exist under this lane.
- [ ] Test runner and import paths match the repo's accepted convention.
- [ ] Synthetic fixtures exist for valid uncertainty, missing attachment, missing uncertainty kind, missing source role, uncertainty-as-product-truth, hidden-public-uncertainty, missing policy/review, and missing release/correction/rollback cases.
- [ ] UncertaintySurface schema path and field expectations are accepted beyond scaffold status.
- [ ] Land-cover uncertainty specialization remains discoverable and separate.
- [ ] EvidenceRef / EvidenceBundle behavior is available to tests or safely stubbed.
- [ ] ModelRunReceipt and product-specific support behavior is available to tests or safely stubbed.
- [ ] PolicyDecision, ReviewRecord, ReleaseManifest, CorrectionNotice, RedactionReceipt, and RollbackCard expectations are defined before enforcing them.
- [ ] CI runs the no-network Habitat uncertainty suite.
- [ ] Failures block public carrier promotion or release candidate approval.

---

## Rollback

Rollback is required if this lane becomes a source export store, uncertainty-output store, lifecycle data store, fixture root, contract root, schema authority, policy authority, proof store, release-decision root, public map/API/tile surface, AI surface, renderer implementation, pipeline implementation, or publication shortcut.

Rollback target for this replacement: previous blank blob SHA `8b137891791fe96927ad78e64b0aad7bded08bdc`.

<p align="right"><a href="#top">Back to top</a></p>
