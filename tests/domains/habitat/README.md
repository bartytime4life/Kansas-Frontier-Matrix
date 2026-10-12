<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-domains-habitat-readme
title: Habitat Domain Tests README
type: test-index-readme
version: v0.2
status: draft; stub-expanded; parent-index; PROPOSED / NEEDS VERIFICATION before promotion
owners:
  - OWNER_TBD — Habitat domain steward
  - OWNER_TBD — Evidence steward
  - OWNER_TBD — Policy steward
  - OWNER_TBD — Validation steward
  - OWNER_TBD — Release steward
  - OWNER_TBD — QA steward
created: NEEDS VERIFICATION — greenfield stub existed before v0.2 expansion
updated: 2026-07-05
policy_label: public-doc; tests; habitat; parent-index; no-network; evidence-bound; policy-aware; release-gated; rollback-aware
tags: [kfm, tests, habitat, parent-index, enforceability, no-network, fixtures, EvidenceBundle, PolicyDecision, ReleaseManifest, CorrectionNotice, RollbackCard, ABSTAIN, DENY]
related:
  - ../../README.md
  - ../README.md
  - land_cover/README.md
  - land_cover/observation/README.md
  - land_cover/class_scheme/README.md
  - land_cover/crosswalk/README.md
  - land_cover/change_summary/README.md
  - land_cover/model_run/README.md
  - land_cover/uncertainty/README.md
  - land_cover/layer_manifest/README.md
  - land_cover/watcher/README.md
  - ecoregions/README.md
  - identity/README.md
  - policy/README.md
  - test_connectivity/README.md
  - test_corridor/README.md
  - test_ecological_system/README.md
  - test_habitat_patch/README.md
  - test_land_cover/README.md
  - test_quality_score/README.md
  - test_restoration/README.md
  - test_source_descriptors/README.md
  - test_stewardship_zone/README.md
  - test_suitability_model/README.md
  - test_uncertainty/README.md
  - thin-slice.habitat-fauna.test/README.md
  - ../../../docs/domains/habitat/README.md
  - ../../../docs/domains/habitat/ARCHITECTURE.md
  - ../../../docs/domains/habitat/SOURCE_FAMILIES.md
  - ../../../contracts/domains/habitat/README.md
  - ../../../schemas/contracts/v1/domains/habitat/
  - ../../../fixtures/domains/habitat/
  - ../../../policy/domains/habitat/
  - ../../../release/manifests/habitat/
notes:
  - "This file replaces the greenfield stub at tests/domains/habitat/README.md."
  - "This is a parent test index only. It does not define Habitat doctrine, contracts, schemas, fixtures, source descriptors, lifecycle records, evidence bundles, policy rules, release decisions, pipeline code, public API material, public map material, public tiles, or published artifacts."
  - "The tested parent invariant is that Habitat tests prove boundary discipline across Habitat object families while preserving source roles, EvidenceBundle requirements, policy posture, release relationship, correction, and rollback."
  - "Default posture is deterministic and no-network. Live source checks, real source exports, lifecycle data, public tiles, and restricted joined records do not belong in default Habitat tests."
  - "Rollback target for this replacement is previous stub blob SHA 407ee9fe7c6662c8ecd68b461a3fd9d9f3d5c5c8."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Habitat domain tests

> Parent index for Habitat test lanes. These tests should prove that Habitat contracts, schemas, policy, fixtures, pipelines, evidence resolution, release gates, correction paths, and rollback targets are enforceable without turning tests into a data store, release authority, public layer, or AI truth source.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: tests" src="https://img.shields.io/badge/root-tests%2F-blue">
  <img alt="Domain: habitat" src="https://img.shields.io/badge/domain-habitat-2e7d32">
  <img alt="Network: disabled by default" src="https://img.shields.io/badge/network-disabled__by__default-critical">
  <img alt="Boundary: tests not release" src="https://img.shields.io/badge/boundary-tests__not__release-success">
</p>

**Path:** `tests/domains/habitat/README.md`  
**Status:** draft / stub-expanded / parent index / PROPOSED until executable tests are verified  
**Owning root:** `tests/`  
**Domain segment:** `habitat`  
**Default execution posture:** deterministic, synthetic, no-network, public-safe fixtures only  
**Truth posture:** CONFIRMED target was a greenfield stub before this expansion · CONFIRMED `tests/` is the canonical root for enforceability proof · CONFIRMED this subtree now has documented Habitat lanes for land cover, policy, identity, ecoregions, object-family tests, source-descriptor tests, Habitat-wide uncertainty tests, and a Habitat/Fauna thin-slice test lane · NEEDS VERIFICATION for executable test modules, fixture payload inventory, validators, source registry activation, policy runtime, release integration, public route/UI behavior, CI coverage, and pass rates.

**Quick jumps:** [Purpose](#purpose) · [Parent invariant](#parent-invariant) · [Lane index](#lane-index) · [Land-cover child tree](#land-cover-child-tree) · [Object-family lanes](#object-family-lanes) · [Cross-domain lane](#cross-domain-lane) · [What belongs here](#what-belongs-here) · [Forbidden shortcuts](#forbidden-shortcuts) · [Run posture](#run-posture) · [Evidence ledger](#evidence-ledger) · [Validation checklist](#validation-checklist) · [Rollback](#rollback)

---

## Purpose

`tests/domains/habitat/` is the Habitat segment of the KFM test tree.

Its job is to prove Habitat boundary discipline, not merely to prove code imports. A Habitat test should show that object meaning, machine shape, evidence resolution, policy checks, review state, release posture, correction path, and rollback target are preserved through a bounded fixture or implementation path.

A passing test in this subtree should **not** mean that a real source is admitted, a real Habitat claim is proven, a public geometry is safe, a layer is published, or a release is approved. It should mean only that the scoped guardrail behaved as expected.

---

## Parent invariant

> **Habitat tests prove enforceability; they do not become Habitat authority.** The subtree may validate Habitat contracts, schemas, fixtures, policies, pipelines, source descriptors, public-surface gates, and release readiness, but it must not become a parallel source registry, lifecycle store, proof store, policy root, release root, public API/map/tile surface, or generated truth surface.

Core checks:

| Check | Required behavior | Failure outcome |
|---|---|---|
| Source-role preservation | Observed, modeled, regulatory, aggregate, administrative, candidate, and synthetic roles remain visible where material. | validation failure / `ABSTAIN`. |
| Evidence support | Evidence-dependent claims resolve support or return a finite non-answer. | `ABSTAIN`. |
| Policy posture | Material policy checks return finite outcomes and fail closed where unresolved. | `DENY` / `ABSTAIN` / `ERROR`. |
| Lifecycle boundary | Tests do not read or write raw/work/quarantine/processed/published material as authority unless explicitly in a gated integration tier. | validation failure. |
| Release boundary | Test success does not become release approval, release manifest, correction notice, or rollback card. | promotion block. |
| Public membrane | Public examples use governed, released, public-safe carriers rather than internal stores or fixtures. | validation failure. |
| AI/UI boundary | Generated text and UI carriers remain downstream of evidence, policy, and release posture. | `ABSTAIN` / validation failure. |

---

## Lane index

| Lane | Primary responsibility | Boundary |
|---|---|---|
| [`ecoregions/`](ecoregions/README.md) | Ecoregion/context-fabric test orientation. | Ecoregions are context, not occurrence, patch, regulatory, or release truth. |
| [`identity/`](identity/README.md) | Habitat identity and deterministic object identity tests. | Identity does not become truth, policy, release, UI, or AI authority. |
| [`policy/`](policy/README.md) | Habitat policy behavior and policy parity tests. | Tests verify policy behavior; they do not own policy authority. |
| [`land_cover/`](land_cover/README.md) | Canonical detailed Habitat land-cover test tree. | Land-cover is interpretive infrastructure, not a truth root. |
| [`test_land_cover/`](test_land_cover/README.md) | Aggregate/compatibility smoke lane for land-cover tests. | Coordinates child lanes; does not replace them. |
| [`test_source_descriptors/`](test_source_descriptors/README.md) | Habitat SourceDescriptor admission metadata tests. | Descriptors are not payloads, proof closure, policy decisions, release authority, or public output. |
| [`test_uncertainty/`](test_uncertainty/README.md) | Habitat-wide `UncertaintySurface` tests. | Uncertainty is required context, not replacement truth. |
| [`thin-slice.habitat-fauna.test/`](thin-slice.habitat-fauna.test/README.md) | Habitat/Fauna thin-slice boundary tests. | Test pass does not become proof closure or release authority. |

---

## Land-cover child tree

The detailed land-cover child tree lives under [`land_cover/`](land_cover/README.md):

| Child lane | Primary responsibility |
|---|---|
| [`land_cover/observation/`](land_cover/observation/README.md) | `LandCoverObservation` identity, source role, class scheme, evidence, correction, and rollback. |
| [`land_cover/class_scheme/`](land_cover/class_scheme/README.md) | `ClassSchemeProfile` vocabulary identity, versioning, nodata/unknown handling, and role posture. |
| [`land_cover/crosswalk/`](land_cover/crosswalk/README.md) | `CoverClassCrosswalk` directionality, lossiness, mapping coverage, and no-silent-recode behavior. |
| [`land_cover/change_summary/`](land_cover/change_summary/README.md) | `LandCoverChangeSummary` comparison between governed observations. |
| [`land_cover/model_run/`](land_cover/model_run/README.md) | Model-run receipts, input closure, config closure, output inventory, and receipt-not-proof checks. |
| [`land_cover/uncertainty/`](land_cover/uncertainty/README.md) | Land-cover uncertainty specialization for accuracy, valid pixels, nodata, source-vintage, crosswalk, and raster/geometry quality. |
| [`land_cover/layer_manifest/`](land_cover/layer_manifest/README.md) | Layer identity, artifact integrity, source-role badges, freshness, correction, supersession, and rollback. |
| [`land_cover/watcher/`](land_cover/watcher/README.md) | Source-head comparison, checkpoints, materiality thresholds, no-op/proposed-work, and watcher-not-publisher checks. |

---

## Object-family lanes

| Lane | Object family or behavior | Boundary summary |
|---|---|---|
| [`test_connectivity/`](test_connectivity/README.md) | `ConnectivityEdge` / `Corridor` derived connectivity. | Derived connectivity is not observed movement, release authority, public-layer truth, or AI truth. |
| [`test_corridor/`](test_corridor/README.md) | `Corridor` geometry and method support. | Corridor is derived spatialization, not source truth or release authority. |
| [`test_ecological_system/`](test_ecological_system/README.md) | `EcologicalSystem` classification. | Classification context does not become release truth or another object family. |
| [`test_habitat_patch/`](test_habitat_patch/README.md) | `HabitatPatch` identity and patch geometry. | Patch geometry does not become occurrence, regulatory, suitability, connectivity, release, or AI truth. |
| [`test_quality_score/`](test_quality_score/README.md) | `HabitatQualityScore`. | Quality score is descriptive, not prescriptive or release authority. |
| [`test_restoration/`](test_restoration/README.md) | `RestorationOpportunity`. | Opportunity is a candidate/evidence object, not a decision or release authority. |
| [`test_stewardship_zone/`](test_stewardship_zone/README.md) | `StewardshipZone`. | Stewardship zone is context, not decision authority. |
| [`test_suitability_model/`](test_suitability_model/README.md) | `SuitabilityModel`. | Suitability is modeled support, not observed or regulatory truth. |

---

## Cross-domain lane

[`thin-slice.habitat-fauna.test/`](thin-slice.habitat-fauna.test/README.md) is the Habitat/Fauna thin-slice test lane.

It should verify that Habitat context and Fauna evidence can be composed while retaining domain ownership, source roles, evidence support, policy posture, release relationship, correction path, and rollback target. Executable proof orchestration belongs under `pipelines/proofs/habitat_fauna_thin_slice/`; proof and receipt outputs belong in accepted proof/receipt homes.

---

## What belongs here

Appropriate contents include:

- deterministic no-network tests;
- compact synthetic fixtures or fixture pointers;
- import and schema smoke checks;
- contract/schema/policy parity checks;
- object-family anti-collapse checks;
- evidence, policy, release, correction, and rollback gate checks;
- public-surface trust-membrane checks;
- child-lane README files that explain scope, limits, and validation posture.

---

## Forbidden shortcuts

Do not use this subtree to:

- fetch live upstream source systems by default;
- store real source exports, lifecycle data, public tiles, proof artifacts, release artifacts, or generated public layers;
- redefine Habitat doctrine, contracts, schemas, fixtures, source registries, policy rules, release decisions, renderer code, or production pipeline code;
- infer release state from file existence, test success, watcher output, proof-run output, layer name, map rendering, tile availability, or AI wording;
- publish, promote, approve, or release anything.

Any test that needs live source access, production source data, or public tile output belongs in a gated integration tier with explicit source admission, lifecycle state, policy, receipts, release controls, correction path, and rollback targets.

---

## Run posture

Parent subtree smoke command:

```bash
pytest tests/domains/habitat
```

Selected child-lane examples:

```bash
pytest tests/domains/habitat/land_cover
pytest tests/domains/habitat/test_suitability_model
pytest tests/domains/habitat/thin-slice.habitat-fauna.test
```

Status of these commands: **PROPOSED / NEEDS VERIFICATION**. They assume `pytest` is the accepted runner and that executable test modules exist. This README does not claim any command currently passes.

---

## Evidence ledger

| Evidence | Status | Supports | Limits |
|---|---|---|---|
| Previous target file | CONFIRMED | `tests/domains/habitat/README.md` existed as a greenfield stub before this replacement. | Did not define the parent lane. |
| `tests/README.md` | CONFIRMED | `tests/` is enforceability proof, canonical, trust-bearing, and failure should block promotion where trust-spine checks fail. | Does not prove Habitat executable modules or pass rate. |
| Child README files under this subtree | CONFIRMED for files updated in this documentation pass | Provide lane-specific scope and boundary statements. | Do not prove executable tests, fixtures, validators, CI, or release wiring. |
| Habitat contracts, schemas, policy, fixture, source-registry, and release paths | PARTLY CONFIRMED / NEEDS VERIFICATION | Referenced as systems under test. | Field-level schema enforcement, runtime behavior, and pass rates remain NEEDS VERIFICATION. |

---

## Validation checklist

Before treating this parent README as implemented behavior, verify:

- [ ] Executable test modules exist for each documented lane or the lane is explicitly documentation-only.
- [ ] Test runner and import paths match the repo's accepted convention.
- [ ] Dotted directory names are supported by the runner or explicitly excluded until wired.
- [ ] Synthetic fixtures exist in accepted fixture homes and are not source payloads.
- [ ] Schema paths and field expectations are accepted beyond scaffold status where tests enforce them.
- [ ] EvidenceRef / EvidenceBundle behavior is available to tests or safely stubbed.
- [ ] PolicyDecision, ReviewRecord, ReleaseManifest, CorrectionNotice, RedactionReceipt, and RollbackCard expectations are defined before enforcing them.
- [ ] CI runs the no-network Habitat suite or marks incomplete lanes as expected gaps.
- [ ] Failures block public carrier promotion or release candidate approval where material.

---

## Rollback

Rollback is required if this parent lane becomes a source export store, lifecycle data store, fixture authority, contract root, schema authority, policy authority, proof store, release-decision root, public map/API/tile surface, AI surface, renderer implementation, pipeline implementation, or publication shortcut.

Rollback target for this replacement: previous stub blob SHA `407ee9fe7c6662c8ecd68b461a3fd9d9f3d5c5c8`.

<p align="right"><a href="#top">Back to top</a></p>
