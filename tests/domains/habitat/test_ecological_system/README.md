<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-domains-habitat-test-ecological-system-readme
title: Habitat EcologicalSystem Test README
type: test-readme
version: v0.1
status: draft; placeholder-expanded; test-lane; PROPOSED / NEEDS VERIFICATION before promotion
owners:
  - OWNER_TBD — Habitat domain steward
  - OWNER_TBD — Ecological systems steward
  - OWNER_TBD — Evidence steward
  - OWNER_TBD — Source steward
  - OWNER_TBD — Policy steward
  - OWNER_TBD — Validation steward
  - OWNER_TBD — Release steward
  - OWNER_TBD — QA steward
created: NEEDS VERIFICATION — blank placeholder existed before v0.1 expansion
updated: 2026-07-05
policy_label: public-doc; tests; habitat; ecological-system; no-network; source-role-aware; modeled-vs-observed; advisory-crosswalk-aware; evidence-bound; release-gated; anti-collapse
tags: [kfm, tests, habitat, ecological_system, test_ecological_system, EcologicalSystem, classification, source-role, modeled-vs-observed, advisory-crosswalk, LandCoverObservation, ClassSchemeProfile, CoverClassCrosswalk, HabitatPatch, EvidenceBundle, PolicyDecision, ReleaseManifest, CorrectionNotice, RollbackCard, ABSTAIN, DENY]
related:
  - ../../../README.md
  - ../README.md
  - ../../../../docs/domains/habitat/sublanes/ecological_systems.md
  - ../../../../docs/domains/habitat/sublanes/land_cover.md
  - ../../../../docs/domains/habitat/MODEL_VS_OBSERVATION.md
  - ../../../../contracts/domains/habitat/ecological_system.md
  - ../../../../contracts/domains/habitat/habitat_patch.md
  - ../../../../contracts/domains/habitat/domain_observation.md
  - ../../../../contracts/domains/habitat/domain_feature_identity.md
  - ../../../../contracts/domains/habitat/land_cover/observation.md
  - ../../../../contracts/domains/habitat/land_cover/class_scheme.md
  - ../../../../contracts/domains/habitat/land_cover/crosswalk.md
  - ../../../../contracts/domains/habitat/land_cover/uncertainty.md
  - ../../../../schemas/contracts/v1/domains/habitat/ecological_system.schema.json
  - ../../../../fixtures/domains/habitat/ecological_system/
  - ../../../../pipelines/domains/habitat/
  - ../../../../pipeline_specs/habitat/
  - ../../../../policy/domains/habitat/
  - ../../../../release/manifests/habitat/
notes:
  - "This file replaces a blank placeholder at tests/domains/habitat/test_ecological_system/README.md."
  - "This is a test-lane README only. It does not define Habitat ecological-system doctrine, semantic contracts, schemas, fixtures, lifecycle records, evidence bundles, receipts, policy rules, release decisions, pipeline code, public API material, public map material, public tiles, or published artifacts."
  - "The tested invariant is that EcologicalSystem is a governed, source-role-bounded ecological classification object. It must preserve classifier identity, native class, classification scheme, source role, source vintage, spatial and temporal scope, evidence support, uncertainty, release relationship, correction, and rollback without becoming another object family, release authority, public-layer truth, or AI/UI truth."
  - "Default posture is deterministic and no-network. Live source checks, real source exports, lifecycle data, and public tiles do not belong in this lane."
  - "Rollback target for this replacement is previous blank blob SHA 8b137891791fe96927ad78e64b0aad7bded08bdc."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Habitat ecological-system tests

> Deterministic, no-network test documentation for proving that Habitat `EcologicalSystem` records remain source-role-bounded ecological classifications with visible classifier identity, source vintage, evidence, uncertainty, release relationship, correction path, and rollback target.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: tests" src="https://img.shields.io/badge/root-tests%2F-blue">
  <img alt="Domain: habitat" src="https://img.shields.io/badge/domain-habitat-2e7d32">
  <img alt="Lane: ecological system" src="https://img.shields.io/badge/lane-ecological__system-blue">
  <img alt="Network: disabled by default" src="https://img.shields.io/badge/network-disabled__by__default-critical">
  <img alt="Boundary: classification not release" src="https://img.shields.io/badge/boundary-classification__not__release-success">
</p>

**Path:** `tests/domains/habitat/test_ecological_system/README.md`  
**Status:** draft / placeholder-expanded / PROPOSED until executable tests are verified  
**Owning root:** `tests/`  
**Domain segment:** `habitat`  
**Test lane:** `test_ecological_system`  
**Default execution posture:** deterministic, synthetic, no-network, public-safe fixtures only  
**Truth posture:** CONFIRMED target was a blank placeholder before this expansion · CONFIRMED `tests/` is the canonical root for enforceability proof · CONFIRMED `EcologicalSystem` is a Habitat-owned object family with PROPOSED field realization · CONFIRMED the EcologicalSystem contract defines it as a source-role-bounded classification object and not release authority · CONFIRMED the paired schema is a scaffold and field-level enforcement remains NEEDS VERIFICATION · NEEDS VERIFICATION for executable test modules, fixture payload inventory, validator behavior, source registry activation, policy runtime, release integration, public route/UI behavior, CI coverage, and pass rates.

---

## Purpose

`tests/domains/habitat/test_ecological_system/` is the intended home for Habitat ecological-system classification tests.

This lane should prove that `EcologicalSystem` records preserve source role, classifier, scheme, evidence, uncertainty, time, release, correction, and rollback boundaries.

A passing test here should **not** mean that a real ecological-system record is admitted, a classifier is authoritative for all uses, a crosswalk is lossless, a public map layer is safe, or a release is approved. It should mean only that ecological-system guardrails behaved as expected against bounded fixtures.

---

## Placement basis

`tests/` is the canonical root for enforceability proof. Habitat is a domain segment inside that root. `test_ecological_system` is a test lane, not a new root and not a parallel contract, schema, policy, data, release, proof, or public-map home.

| Responsibility | Correct home | This lane's relationship |
|---|---|---|
| EcologicalSystem tests | `tests/domains/habitat/test_ecological_system/` | This directory. |
| Ecological-system doctrine | `docs/domains/habitat/sublanes/ecological_systems.md` | Referenced doctrine; tests do not redefine it. |
| EcologicalSystem meaning | `contracts/domains/habitat/ecological_system.md` | Semantic contract under test. |
| Machine schema | `schemas/contracts/v1/domains/habitat/ecological_system.schema.json` | Referenced where accepted; scaffold posture must be respected. |
| Fixtures | `fixtures/domains/habitat/ecological_system/` | Preferred toy inputs and expected outcomes if populated. |
| Land-cover support | `contracts/domains/habitat/land_cover/observation.md`, `class_scheme.md`, `crosswalk.md`, `uncertainty.md` | May support classification; does not own synthesized EcologicalSystem truth. |
| Release decisions | `release/` and `release/manifests/habitat/` | Publication, correction, and rollback authority; tests cannot replace it. |

---

## Invariant under test

> **EcologicalSystem is classification context, not release truth.** A Habitat `EcologicalSystem` record classifies a place, patch, cell, polygon, raster unit, or public-safe aggregate under a declared source, classification scheme, source role, source vintage, temporal scope, spatial scope, evidence basis, uncertainty posture, release relationship, correction path, and rollback target.

Core checks:

| Check | Required behavior | Failure outcome |
|---|---|---|
| Classification identity | Stable ID, source, class scheme, native class, object role, temporal scope, spatial scope, and digest basis are explicit. | validation failure / `ERROR`. |
| Source role | Observed, modeled, regulatory, aggregate, administrative, candidate, synthetic, derivative, or context posture is explicit. | validation failure / `ABSTAIN`. |
| Native classifier preservation | Native classes remain visible and versioned. | validation failure. |
| Advisory crosswalk | Cross-classifier mappings are advisory unless reviewed; native class is not overwritten. | review required / validation failure. |
| Spatial and temporal scope | Spatial scope and relevant time kinds remain distinct where material. | validation failure. |
| Evidence and uncertainty | Evidence and uncertainty/caveat refs are attached before consequential use. | `ABSTAIN`. |
| Release boundary | Policy, review, release, correction, and rollback remain separate from test pass state. | promotion block. |
| No authority upgrade | EcologicalSystem cannot become another object family, public-layer truth, release authority, or AI truth. | validation failure / `ABSTAIN`. |

---

## Expected scope

Tests in this lane may validate:

- required ecological-system identity, native class, classification scheme, scheme version, source role, source vintage, spatial scope, temporal scope, and digest posture;
- rejection of modeled classification presented with stronger authority than its support allows;
- preservation of native classifier labels and rejection of silent crosswalk substitution;
- evidence and uncertainty requirements for consequential or public-facing use;
- rejection of public-facing candidates that lack evidence, policy, review, release relationship, correction, or rollback context;
- finite outcomes when evidence resolver, policy engine, uncertainty support, source registry activation, or release manifest is missing.

Live source checks, real source exports, production classifier data, public tile generation, and provider-backed model calls are out of scope for the default suite.

---

## Fixture posture

Use synthetic, public-safe fixtures only.

Fixture requirements:

- deterministic and no-network;
- compact enough for review in a PR;
- explicit expected outcome;
- explicit source role, classifier, source vintage, classification scheme, native class, evidence, uncertainty, policy, review, release relationship, correction, and rollback posture where material;
- no real source exports, lifecycle data, public tiles, or published artifacts.

---

## Finite outcomes

| Condition | Expected outcome |
|---|---|
| Valid synthetic EcologicalSystem with native class, source role, evidence, uncertainty, policy, review, release relationship, correction, and rollback context | accepted classification support only. |
| Missing classification identity, source role, source vintage, scheme, native class, or spatial/temporal scope | validation failure / `ERROR`. |
| Modeled classification presented with unsupported authority | `ABSTAIN` / validation failure. |
| Crosswalk treated as authoritative replacement for native class | validation failure. |
| Public-facing candidate lacks release/correction/rollback posture | promotion-blocking failure. |
| Policy engine unavailable | `ERROR` or `ABSTAIN`, never public exposure. |

---

## Suggested layout

```text
tests/domains/habitat/test_ecological_system/
├── README.md
├── test_ecological_system_identity.py
├── test_source_role_required.py
├── test_native_classifier_preserved.py
├── test_advisory_crosswalk_not_authority.py
├── test_modeled_not_overstated.py
└── test_release_correction_rollback.py
```

---

## Run posture

```bash
pytest tests/domains/habitat/test_ecological_system
```

Status of the command above: **PROPOSED / NEEDS VERIFICATION**. It assumes `pytest` is the accepted test runner and that executable test modules exist. This README does not claim the command currently passes.

---

## Evidence ledger

| Evidence | Status | Supports | Limits |
|---|---|---|---|
| Previous target file | CONFIRMED | `tests/domains/habitat/test_ecological_system/README.md` existed as a blank placeholder before this replacement. | Did not define the lane. |
| `tests/README.md` | CONFIRMED | `tests/` is enforceability proof and failure should block promotion where trust-spine checks fail. | Does not prove this lane's modules or pass rate. |
| `contracts/domains/habitat/ecological_system.md` | CONFIRMED semantic contract / PROPOSED implementation | Defines `EcologicalSystem` as a Habitat-owned classification object with source role, evidence, time, release, correction, and rollback constraints. | Schema is a permissive scaffold; field-level enforcement remains NEEDS VERIFICATION. |
| `docs/domains/habitat/sublanes/ecological_systems.md` | CONFIRMED doctrine / PROPOSED implementation | EcologicalSystem classifications are source-role-bounded; model-vs-observation labels remain visible; cross-classifier crosswalks are advisory and native classifications are preserved. | Implementation paths, validators, fixtures, schemas, policy runtime, release artifacts, UI, Focus Mode, and CI remain NEEDS VERIFICATION. |
| `docs/domains/habitat/sublanes/land_cover.md` | CONFIRMED doctrine / PROPOSED implementation | Land-cover can supply cover-class inputs and crosswalk material, but synthesized EcologicalSystem belongs to ecological systems / biotopes. | Does not prove executable ecological-system tests. |

---

## Validation checklist

- [ ] Executable test modules exist under this lane.
- [ ] Test runner and import paths match the repo's accepted convention.
- [ ] Synthetic fixtures exist for positive and negative ecological-system cases.
- [ ] EcologicalSystem schema path and field expectations are accepted beyond scaffold status.
- [ ] EvidenceRef / EvidenceBundle behavior is available to tests or safely stubbed.
- [ ] SourceDescriptor/source-role behavior is available to tests or safely stubbed.
- [ ] PolicyDecision, ReviewRecord, ReleaseManifest, CorrectionNotice, RedactionReceipt, and RollbackCard expectations are defined before enforcing them.
- [ ] CI runs the no-network Habitat ecological-system suite.
- [ ] Failures block public carrier promotion or release candidate approval.

---

## Rollback

Rollback is required if this lane becomes a source export store, classifier-payload store, lifecycle data store, fixture root, contract root, schema authority, policy authority, proof store, release-decision root, public map/API/tile surface, AI surface, renderer implementation, pipeline implementation, or publication shortcut.

Rollback target for this replacement: previous blank blob SHA `8b137891791fe96927ad78e64b0aad7bded08bdc`.

<p align="right"><a href="#top">Back to top</a></p>
