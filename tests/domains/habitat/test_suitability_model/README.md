<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-domains-habitat-test-suitability-model-readme
title: Habitat SuitabilityModel Test README
type: test-readme
version: v0.1
status: draft; placeholder-expanded; test-lane; PROPOSED / NEEDS VERIFICATION before promotion
owners:
  - OWNER_TBD — Habitat domain steward
  - OWNER_TBD — Suitability steward
  - OWNER_TBD — Model steward
  - OWNER_TBD — Evidence steward
  - OWNER_TBD — Source steward
  - OWNER_TBD — Policy steward
  - OWNER_TBD — Validation steward
  - OWNER_TBD — Release steward
  - OWNER_TBD — QA steward
created: NEEDS VERIFICATION — blank placeholder existed before v0.1 expansion
updated: 2026-07-05
policy_label: public-doc; tests; habitat; suitability-model; no-network; modeled-not-observed; model-card-required; uncertainty-bound; evidence-bound; release-gated; anti-collapse
tags: [kfm, tests, habitat, suitability_model, test_suitability_model, SuitabilityModel, modeled-habitat, model-card, ModelRunReceipt, UncertaintySurface, HabitatQualityScore, HabitatPatch, LandCoverObservation, EvidenceBundle, PolicyDecision, ReleaseManifest, CorrectionNotice, RollbackCard, ABSTAIN, DENY]
related:
  - ../../../README.md
  - ../README.md
  - ../../../../contracts/domains/habitat/SuitabilityModel.md
  - ../../../../contracts/domains/habitat/suitability_model.md
  - ../../../../contracts/domains/habitat/habitat_quality_score.md
  - ../../../../contracts/domains/habitat/habitat_patch.md
  - ../../../../contracts/domains/habitat/land_cover/observation.md
  - ../../../../contracts/domains/habitat/land_cover/model_run_receipt.md
  - ../../../../contracts/domains/habitat/land_cover/uncertainty.md
  - ../../../../docs/domains/habitat/sublanes/suitability.md
  - ../../../../docs/domains/habitat/MODEL_VS_OBSERVATION.md
  - ../../../../docs/domains/habitat/SOURCE_FAMILIES.md
  - ../../../../schemas/contracts/v1/domains/habitat/suitability_model.schema.json
  - ../../../../fixtures/domains/habitat/suitability_model/
  - ../../../../policy/domains/habitat/
  - ../../../../policy/sensitivity/habitat/
  - ../../../../pipelines/domains/habitat/
  - ../../../../pipeline_specs/habitat/
  - ../../../../data/registry/sources/habitat/
  - ../../../../release/manifests/habitat/
notes:
  - "This file replaces a blank placeholder at tests/domains/habitat/test_suitability_model/README.md."
  - "This is a test-lane README only. It does not define SuitabilityModel doctrine, semantic contracts, schemas, fixtures, lifecycle records, evidence bundles, receipts, policy rules, release decisions, pipeline code, public API material, public map material, public tiles, or published artifacts."
  - "The tested invariant is that SuitabilityModel remains governed modeled Habitat. It must preserve model identity, modeled source role, intended use, spatial scope, temporal scope, input support, run support, uncertainty support, model-card support, evidence support, display obligations, release relationship, correction, and rollback without becoming observed land-cover truth, occurrence truth, regulatory designation, HabitatPatch truth, release authority, public-layer truth, or AI/UI truth."
  - "Default posture is deterministic and no-network. Live source checks, real source exports, lifecycle data, public tiles, and restricted joined records do not belong in this lane."
  - "Rollback target for this replacement is previous blank blob SHA 8b137891791fe96927ad78e64b0aad7bded08bdc."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Habitat SuitabilityModel tests

> Deterministic, no-network test documentation for proving that Habitat `SuitabilityModel` records remain modeled, evidence-bound, model-card-backed, uncertainty-bound, release-gated, correction-aware, and rollback-ready.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: tests" src="https://img.shields.io/badge/root-tests%2F-blue">
  <img alt="Domain: habitat" src="https://img.shields.io/badge/domain-habitat-2e7d32">
  <img alt="Lane: suitability model" src="https://img.shields.io/badge/lane-suitability__model-blue">
  <img alt="Network: disabled by default" src="https://img.shields.io/badge/network-disabled__by__default-critical">
  <img alt="Boundary: modeled not observed" src="https://img.shields.io/badge/boundary-modeled__not__observed-success">
</p>

**Path:** `tests/domains/habitat/test_suitability_model/README.md`  
**Status:** draft / placeholder-expanded / PROPOSED until executable tests are verified  
**Owning root:** `tests/`  
**Domain segment:** `habitat`  
**Test lane:** `test_suitability_model`  
**Default execution posture:** deterministic, synthetic, no-network, public-safe fixtures only  
**Truth posture:** CONFIRMED target was a blank placeholder before this expansion · CONFIRMED `tests/` is the canonical root for enforceability proof · CONFIRMED `SuitabilityModel` is a Habitat object-family term with PROPOSED field realization · CONFIRMED the SuitabilityModel contract defines it as modeled Habitat and not observed land cover, occurrence truth, regulatory critical habitat, HabitatPatch truth, release authority, or a public layer by itself · CONFIRMED the paired snake-case schema is a scaffold and field-level enforcement remains NEEDS VERIFICATION · NEEDS VERIFICATION for executable test modules, fixture payload inventory, validator behavior, model-card requirements, model-run receipt checks, policy runtime, release integration, public route/UI behavior, CI coverage, and pass rates.

---

## Purpose

`tests/domains/habitat/test_suitability_model/` is the intended home for Habitat suitability-model tests.

This lane should prove that `SuitabilityModel` records preserve model identity, modeled source role, intended use, input support, run support, uncertainty, model-card obligations, evidence, policy, review, release, correction, and rollback boundaries.

A passing test here should **not** mean that a real model is validated for all uses, a public model layer is safe, a habitat claim is proven, or a release is approved. It should mean only that suitability-model guardrails behaved as expected against bounded fixtures.

---

## Placement basis

`tests/` is the canonical root for enforceability proof. Habitat is a domain segment inside that root. `test_suitability_model` is a test lane, not a new root and not a parallel contract, schema, policy, data, release, proof, or public-map home.

| Responsibility | Correct home | This lane's relationship |
|---|---|---|
| SuitabilityModel tests | `tests/domains/habitat/test_suitability_model/` | This directory. |
| SuitabilityModel meaning | `contracts/domains/habitat/SuitabilityModel.md` | Semantic contract under test. |
| Lower-case alias | `contracts/domains/habitat/suitability_model.md` | Existing alias/scaffold; disposition remains NEEDS VERIFICATION. |
| Machine schema | `schemas/contracts/v1/domains/habitat/suitability_model.schema.json` | Referenced where accepted; scaffold posture must be respected. |
| Fixtures | `fixtures/domains/habitat/suitability_model/` | Preferred toy inputs and expected outcomes if populated. |
| Run and uncertainty support | `contracts/domains/habitat/land_cover/model_run_receipt.md`, `contracts/domains/habitat/land_cover/uncertainty.md` or future Habitat-wide equivalents | Required companion concepts; exact cross-sublane home remains NEEDS VERIFICATION. |
| Policy homes | `policy/domains/habitat/`, `policy/sensitivity/habitat/` | Referenced by tests, not bypassed here. |
| Release decisions | `release/` and `release/manifests/habitat/` | Publication, correction, and rollback authority; tests cannot replace it. |

---

## Invariant under test

> **SuitabilityModel is modeled support, not observed or regulatory truth.** A Habitat suitability model defines a modeled suitability surface, score family, index, class, or related model product under stated assumptions. It must stay visibly modeled through API, map, report, Focus Mode, and AI surfaces.

Core checks:

| Check | Required behavior | Failure outcome |
|---|---|---|
| Model identity | Stable model ID, version, target concept, object role, and normalized digest are explicit. | validation failure / `ERROR`. |
| Source role | Output role remains modeled and is not relabeled observed or regulatory. | validation failure / `ABSTAIN`. |
| Intended use | What the model is for and not for is visible. | validation failure. |
| Input support | Source descriptors, source roles, input refs, source vintages, and authority limits are preserved. | validation failure / `ABSTAIN`. |
| Run support | Run receipt, code/config/input/output digests, and environment summary are attached where material. | validation failure. |
| Uncertainty support | Uncertainty or caveat support is paired with modeled outputs. | review required / `ABSTAIN`. |
| Model-card burden | Intended use, validation metrics, known limits, failure modes, and fitness caveats are visible before public use. | promotion block. |
| Release boundary | Policy, review, release, correction, and rollback remain separate from test pass state. | promotion block. |
| No authority upgrade | Model cannot become observation truth, regulatory truth, occurrence truth, patch truth, release authority, public-layer truth, or AI truth. | validation failure / `ABSTAIN`. |

---

## Expected scope

Tests in this lane may validate:

- required model identity, version, target concept, source role, intended use, spatial scope, temporal scope, and digest posture;
- rejection of model-as-observation, model-as-regulatory-designation, model-as-occurrence-proof, or model-as-patch-truth misuse;
- model-run receipt, input closure, config closure, output inventory, uncertainty, model-card, and validation-summary requirements;
- public-surface display obligations for modeled status, uncertainty, stale/correction state, and evidence posture;
- rejection of public-facing candidates that lack evidence, policy, review, release relationship, correction, or rollback context;
- finite outcomes when evidence resolver, policy engine, model-run receipt, uncertainty support, model card, source registry activation, or release manifest is missing.

Live source checks, real source exports, production model outputs, public tile generation, restricted joined records, and provider-backed model calls are out of scope for the default suite.

---

## Fixture posture

Use synthetic, public-safe fixtures only.

Fixture requirements:

- deterministic and no-network;
- compact enough for review in a PR;
- explicit expected outcome;
- explicit model identity, source role, intended use, input support, run support, uncertainty, model-card, evidence, policy, review, release relationship, correction, and rollback posture where material;
- no real source exports, lifecycle data, production model outputs, public tiles, restricted joined records, or published artifacts.

---

## Finite outcomes

| Condition | Expected outcome |
|---|---|
| Valid synthetic SuitabilityModel with model card, run receipt, uncertainty, evidence, policy, review, release relationship, correction, and rollback context | accepted modeled support only. |
| Missing model identity, source role, intended use, input support, run support, or digest basis | validation failure / `ERROR` / `ABSTAIN`. |
| Model treated as observed, regulatory, occurrence, patch, source, public-layer, or release truth | validation failure. |
| Modeled output lacks uncertainty or model-card support | review required / `ABSTAIN` / promotion block. |
| Public-facing candidate lacks release/correction/rollback posture | promotion-blocking failure. |
| Policy engine unavailable | `ERROR` or `ABSTAIN`, never public exposure. |

---

## Suggested layout

```text
tests/domains/habitat/test_suitability_model/
├── README.md
├── test_suitability_model_identity.py
├── test_modeled_source_role_required.py
├── test_model_card_required.py
├── test_model_run_and_uncertainty_required.py
├── test_model_not_observed_or_regulatory_truth.py
└── test_release_correction_rollback.py
```

---

## Run posture

```bash
pytest tests/domains/habitat/test_suitability_model
```

Status of the command above: **PROPOSED / NEEDS VERIFICATION**. It assumes `pytest` is the accepted test runner and that executable test modules exist. This README does not claim the command currently passes.

---

## Evidence ledger

| Evidence | Status | Supports | Limits |
|---|---|---|---|
| Previous target file | CONFIRMED | `tests/domains/habitat/test_suitability_model/README.md` existed as a blank placeholder before this replacement. | Did not define the lane. |
| `tests/README.md` | CONFIRMED | `tests/` is enforceability proof and failure should block promotion where trust-spine checks fail. | Does not prove this lane's modules or pass rate. |
| `contracts/domains/habitat/SuitabilityModel.md` | CONFIRMED semantic contract / PROPOSED implementation | Defines `SuitabilityModel` as modeled Habitat and not observed land cover, occurrence truth, regulatory critical habitat, HabitatPatch truth, release authority, or public layer by itself. | Path alias conflict and scaffold schema mean field-level enforcement remains NEEDS VERIFICATION. |

---

## Validation checklist

- [ ] Executable test modules exist under this lane.
- [ ] Test runner and import paths match the repo's accepted convention.
- [ ] Synthetic fixtures exist for valid model, missing identity, missing source role, missing model card, missing run receipt, missing uncertainty, model-as-observed, model-as-regulatory, model-as-occurrence, missing policy/review, and missing release/correction/rollback cases.
- [ ] SuitabilityModel schema path and field expectations are accepted beyond scaffold status.
- [ ] The path alias between `SuitabilityModel.md` and `suitability_model.md` is resolved or explicitly tolerated.
- [ ] EvidenceRef / EvidenceBundle behavior is available to tests or safely stubbed.
- [ ] ModelRunReceipt, model-card, and UncertaintySurface behavior is available to tests or safely stubbed.
- [ ] PolicyDecision, ReviewRecord, ReleaseManifest, CorrectionNotice, RedactionReceipt, and RollbackCard expectations are defined before enforcing them.
- [ ] CI runs the no-network Habitat suitability-model suite.
- [ ] Failures block public carrier promotion or release candidate approval.

---

## Rollback

Rollback is required if this lane becomes a source export store, model-output store, lifecycle data store, fixture root, contract root, schema authority, policy authority, proof store, release-decision root, public map/API/tile surface, AI surface, renderer implementation, pipeline implementation, or publication shortcut.

Rollback target for this replacement: previous blank blob SHA `8b137891791fe96927ad78e64b0aad7bded08bdc`.

<p align="right"><a href="#top">Back to top</a></p>
