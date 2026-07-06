<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-domains-habitat-land-cover-uncertainty-readme
title: Habitat Land-Cover Uncertainty Test README
type: test-readme
version: v0.1
status: draft; placeholder-expanded; test-lane; PROPOSED / NEEDS VERIFICATION before promotion
owners:
  - OWNER_TBD — Habitat domain steward
  - OWNER_TBD — Land-cover steward
  - OWNER_TBD — Uncertainty steward
  - OWNER_TBD — Source steward
  - OWNER_TBD — Evidence steward
  - OWNER_TBD — Schema steward
  - OWNER_TBD — Policy steward
  - OWNER_TBD — Validation steward
  - OWNER_TBD — Release steward
  - OWNER_TBD — QA steward
created: NEEDS VERIFICATION — blank placeholder existed before v0.1 expansion
updated: 2026-07-05
policy_label: public-doc; tests; habitat; land-cover; uncertainty; no-network; accuracy-aware; valid-pixel-aware; source-vintage-aware; evidence-bound; release-gated
tags: [kfm, tests, habitat, land_cover, uncertainty, UncertaintySurface, accuracy, confidence, valid-pixel-footprint, nodata, source-vintage-gap, crosswalk-uncertainty, model-uncertainty, EvidenceRef, EvidenceBundle, PolicyDecision, ReleaseManifest, CorrectionNotice, RollbackCard, ABSTAIN, DENY]
related:
  - ../../../../README.md
  - ../../../../../contracts/domains/habitat/land_cover/uncertainty.md
  - ../../../../../schemas/contracts/v1/domains/habitat/land_cover/uncertainty.schema.json
  - ../../../../../fixtures/domains/habitat/land_cover/uncertainty/README.md
  - ../../../../../docs/domains/habitat/sublanes/land_cover.md
  - ../../../../../docs/domains/habitat/MODEL_VS_OBSERVATION.md
  - ../../../../../docs/domains/habitat/SOURCE_FAMILIES.md
  - ../../../../../docs/domains/habitat/API_CONTRACTS.md
  - ../../../../../contracts/domains/habitat/land_cover/observation.md
  - ../../../../../contracts/domains/habitat/land_cover/class_scheme.md
  - ../../../../../contracts/domains/habitat/land_cover/crosswalk.md
  - ../../../../../contracts/domains/habitat/land_cover/change_summary.md
  - ../../../../../contracts/domains/habitat/land_cover/model_run_receipt.md
  - ../../../../../contracts/domains/habitat/uncertainty_surface.md
  - ../../../../../pipelines/domains/habitat/land_cover/
  - ../../../../../pipeline_specs/habitat/land_cover/
  - ../../../../../policy/domains/habitat/land_cover/
  - ../../../../../policy/sensitivity/habitat/
  - ../../../../../data/processed/habitat/land_cover/uncertainty/README.md
  - ../../../../../data/registry/sources/habitat/
  - ../../../../../release/manifests/habitat/
notes:
  - "This file replaces a blank placeholder at tests/domains/habitat/land_cover/uncertainty/README.md."
  - "This is a test-lane README only. It does not define Habitat land-cover doctrine, semantic contracts, schemas, source descriptors, fixtures, lifecycle records, processed uncertainty artifacts, evidence bundles, proofs, policy rules, release decisions, production code, public layers, or published artifacts."
  - "The tested invariant is that UncertaintySurface carries per-observation accuracy, valid-pixel footprint, source-vintage gap, crosswalk uncertainty, model-output uncertainty, raster or geometry quality, confidence caveats, evidence refs, display obligations, correction state, and rollback context without becoming LandCoverObservation, ClassSchemeProfile, CoverClassCrosswalk, LandCoverChangeSummary, ModelRunReceipt, LayerManifest, PolicyDecision, ReleaseManifest, public layer, or AI/UI evidence."
  - "The default posture is deterministic and no-network. Live source checks, real source exports, real processed artifacts, public tiles, and sensitive joined records do not belong in this lane."
  - "Rollback target for this replacement is previous blank blob SHA 8b137891791fe96927ad78e64b0aad7bded08bdc."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Habitat land-cover uncertainty tests

> Deterministic, no-network test documentation for proving that Habitat `UncertaintySurface` records preserve accuracy, confidence, valid-pixel footprint, nodata, source-vintage gap, crosswalk uncertainty, model uncertainty, geometry/resolution quality, evidence posture, display obligations, correction, and rollback without turning uncertainty into observation truth, proof, policy approval, release authority, public layer truth, or AI/UI evidence.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: tests" src="https://img.shields.io/badge/root-tests%2F-blue">
  <img alt="Domain: habitat" src="https://img.shields.io/badge/domain-habitat-2e7d32">
  <img alt="Sublane: land cover" src="https://img.shields.io/badge/sublane-land__cover-6a5acd">
  <img alt="Object: UncertaintySurface" src="https://img.shields.io/badge/object-UncertaintySurface-blue">
  <img alt="Network: disabled by default" src="https://img.shields.io/badge/network-disabled__by__default-critical">
  <img alt="Boundary: uncertainty not observation" src="https://img.shields.io/badge/boundary-uncertainty__not__observation-success">
</p>

**Path:** `tests/domains/habitat/land_cover/uncertainty/README.md`  
**Status:** draft / placeholder-expanded / PROPOSED until paired test files are verified  
**Owning root:** `tests/`  
**Domain segment:** `habitat`  
**Test lane:** `land_cover/uncertainty`  
**Default execution posture:** deterministic, synthetic, no-network, public-safe fixtures only  
**Truth posture:** CONFIRMED target was a blank placeholder before this expansion · CONFIRMED `tests/` is the canonical root for enforceability proof · CONFIRMED `UncertaintySurface` is defined as the land-cover object carrying per-observation accuracy, valid-pixel footprint, source-vintage gap, crosswalk uncertainty, raster/geometry quality, and confidence caveats alongside a governed `LandCoverObservation` · CONFIRMED the paired fixture README says examples are not source records, lifecycle data, EvidenceBundles, source descriptors, policy decisions, review approvals, release state, public API/map/tile material, Habitat truth, or published artifacts · NEEDS VERIFICATION for executable test modules, fixture payload inventory, schema enforcement, validators, source registry records, policy files, imports, CI coverage, and release-gate integration.

**Quick jumps:** [Purpose](#purpose) · [Placement basis](#placement-basis) · [Invariant under test](#invariant-under-test) · [Expected test scope](#expected-test-scope) · [Fixture posture](#fixture-posture) · [Assertions](#assertions) · [Finite outcomes](#finite-outcomes) · [Forbidden shortcuts](#forbidden-shortcuts) · [Suggested test layout](#suggested-test-layout) · [Run posture](#run-posture) · [Evidence ledger](#evidence-ledger) · [Validation checklist](#validation-checklist) · [Rollback](#rollback)

---

## Purpose

`tests/domains/habitat/land_cover/uncertainty/` is the intended home for tests that prove Habitat land-cover uncertainty stays inside its governed meaning.

This lane should test that an `UncertaintySurface` cannot silently become:

- a `LandCoverObservation`;
- a source raster or source authority;
- a `ClassSchemeProfile`;
- a `CoverClassCrosswalk`;
- a `LandCoverChangeSummary`;
- a `ModelRunReceipt`;
- a validation report, proof object, policy decision, review approval, or release manifest;
- a public layer, tile, renderer style, popup, Focus Mode answer, or AI answer.

A passing test here should **not** mean that a real uncertainty artifact is accepted, processed, released, or sufficient for public display. It should mean only that uncertainty guardrails behaved as expected against bounded fixtures.

---

## Placement basis

`tests/` is the canonical root for enforceability proof. Habitat appears as a lane segment inside the tests root, not as a repo-root domain folder.

| Responsibility | Correct home | This lane's relationship |
|---|---|---|
| Habitat land-cover uncertainty tests | `tests/domains/habitat/land_cover/uncertainty/` | This directory. |
| Synthetic uncertainty fixtures | `fixtures/domains/habitat/land_cover/uncertainty/` | Preferred toy inputs and expected outcomes. |
| Semantic uncertainty contract | `contracts/domains/habitat/land_cover/uncertainty.md` | Defines meaning; tests do not redefine it. |
| Machine schema | `schemas/contracts/v1/domains/habitat/land_cover/uncertainty.schema.json` | Referenced by tests; current scaffold maturity must be respected. |
| Land-cover doctrine | `docs/domains/habitat/sublanes/land_cover.md` | Referenced doctrine; not test implementation. |
| Observation dependency | `contracts/domains/habitat/land_cover/observation.md` | Uncertainty attaches to observations or derived products; it does not replace them. |
| Class-scheme/crosswalk/change-summary/model-run support | `contracts/domains/habitat/land_cover/` | Related support objects; not owned here. |
| Processed uncertainty outputs | `data/processed/habitat/land_cover/uncertainty/` | Lifecycle lane; tests do not create processed-data authority. |
| Policy and sensitivity homes | `policy/domains/habitat/land_cover/`, `policy/sensitivity/habitat/` | Referenced by tests, not bypassed here. |
| Pipeline logic and specs | `pipelines/domains/habitat/land_cover/`, `pipeline_specs/habitat/land_cover/` | Systems under test where accepted; not duplicated here. |
| Release decisions | `release/` and `release/manifests/habitat/` | Publication, correction, and rollback authority; tests cannot replace it. |

---

## Invariant under test

> **Uncertainty is inspectable context, not replacement truth.** `UncertaintySurface` describes accuracy, quality, coverage, confidence, footprint, temporal gap, crosswalk ambiguity, model uncertainty, and public-generalization caveats that must travel with a land-cover observation or derived product. It must not replace the observation, evidence bundle, validation report, policy decision, release manifest, public layer, or generated answer.

For this test lane, the invariant decomposes into ten checks:

| Check | Required behavior | Failure outcome |
|---|---|---|
| Attachment | Linked observation or declared derived product is explicit. | validation failure / `ERROR`. |
| Uncertainty kind | Accuracy, confidence, footprint, nodata, source-vintage gap, crosswalk ambiguity, model uncertainty, geometry quality, resolution quality, or generalization caveat is explicit. | validation failure. |
| Spatial support | Footprint, mask, extent, CRS, resolution, nodata, valid-pixel count, and public geometry posture are explicit where material. | validation failure / review required. |
| Temporal support | Source time, observed time, valid time, retrieval time, release time, and correction time remain distinct where material. | validation failure. |
| Source-role preservation | Uncertainty over observed, modeled, crosswalked, aggregate, or public-derived material remains labeled. | `DENY` / validation failure. |
| Evidence closure | Consequential use resolves `EvidenceRef -> EvidenceBundle` or produces a finite non-answer. | `ABSTAIN`. |
| Model-vs-observation | Modeled uncertainty does not become observed product accuracy. | `ABSTAIN` / validation failure. |
| Display obligations | Map/API/UI/AI-facing carriers show required caveats or finite non-answers. | review required / validation failure. |
| Release boundary | Public use requires policy, review, release, correction, and rollback linkage where material. | promotion-blocking failure. |
| No authority upgrade | Uncertainty cannot become observation truth, proof, policy approval, release approval, or public-layer truth. | `DENY` / `ABSTAIN`. |

---

## Expected test scope

Tests in this lane should be small, synthetic, and deterministic. They may validate:

- required observation or derived-product attachment;
- required uncertainty kind and source-role posture;
- valid-pixel footprint, nodata, mask, confidence, and coverage posture;
- source-vintage gap and temporal alignment checks;
- crosswalk-uncertainty and model-vs-observation labeling;
- evidence closure for uncertainty statements;
- public-carrier failure when uncertainty caveats are missing;
- denial when uncertainty is treated as observation truth, proof closure, policy approval, release authority, public layer truth, or AI/UI evidence.

Live source downloads, real processed artifacts, public tile generation, sensitive joined records, and provider-backed model calls are out of scope for the default suite.

---

## Fixture posture

Use `fixtures/domains/habitat/land_cover/uncertainty/` when possible.

Fixture requirements:

- synthetic and public-safe;
- deterministic and no-network;
- compact enough for review in a PR;
- explicit expected outcome;
- explicit uncertainty ID, observation or derived-product ref, uncertainty kind, source role, source vintage, spatial support, temporal support, evidence state, validation state, policy state, review state, release state, correction state, and rollback state where material;
- no real source exports, real processed artifacts, real public tiles, sensitive joined records, or published artifacts.

Preferred fixture families:

| Fixture kind | Preferred lane | Example expected outcome |
|---|---|---|
| Valid toy uncertainty object | `fixtures/domains/habitat/land_cover/uncertainty/` | accepted as uncertainty support only. |
| Missing observation reference | same | validation failure. |
| Missing uncertainty kind | same or invalid lane | validation failure. |
| Footprint confused with nodata policy | same or invalid lane | validation failure / review required. |
| Modeled uncertainty presented as observed accuracy | same or invalid lane | `ABSTAIN` / validation failure. |
| Uncertainty used as release approval | same or invalid lane | validation failure. |
| Public layer example without required caveat | same or invalid lane | review required / validation failure. |

---

## Assertions

A useful land-cover uncertainty test should make the uncertainty boundary obvious.

### Positive path

- uncertainty attaches to a known observation or derived product;
- uncertainty kind is explicit;
- source role, source vintage, spatial support, temporal support, and artifact support are visible;
- valid-pixel, nodata, coverage, confidence, accuracy, crosswalk, model, and generalization caveats remain distinct where material;
- evidence, validation, policy, review, release, correction, and rollback references are linkable where material;
- downstream API, renderer, Evidence Drawer, Focus Mode, or AI examples remain carriers, not uncertainty authority.

### Negative path

- missing observation ref or uncertainty kind fails closed;
- uncertainty cannot classify land cover;
- missing uncertainty cannot be interpreted as certainty;
- footprint and nodata cannot collapse silently;
- model uncertainty cannot become observed accuracy;
- uncertainty cannot replace EvidenceBundle proof, PolicyDecision, ReviewRecord, ReleaseManifest, catalog closure, or source activation;
- UI uncertainty mode, map legend, popup, tile, graph edge, Focus Mode answer, or AI text cannot become evidence.

---

## Finite outcomes

This lane should prefer explicit finite outcomes over loose pass/fail text.

| Condition | Expected outcome |
|---|---|
| Valid synthetic uncertainty with attachment, kind, spatial/temporal support, evidence, policy, review, release relationship, correction, and rollback context | accepted uncertainty support only. |
| Missing observation or derived-product ref | validation failure / `ERROR`. |
| Missing uncertainty kind | validation failure / `ERROR`. |
| Missing support for consequential uncertainty statement | `ABSTAIN`. |
| Modeled uncertainty presented as observed accuracy | `ABSTAIN` / validation failure. |
| Uncertainty treated as observation truth, proof, policy, review, source activation, or release approval | validation failure. |
| Public-facing output lacks required caveat | review required / promotion block. |
| Policy engine unavailable | `ERROR` or `ABSTAIN`, never public exposure. |

---

## Forbidden shortcuts

Do not use this test lane to:

- fetch live upstream source systems;
- store real source exports, real processed artifacts, real lifecycle data, or real public tiles;
- store proof packs, release manifests, or generated public layers;
- store sensitive joined records or exact protected-resource geometry;
- redefine uncertainty contracts, Habitat land-cover doctrine, schemas, source descriptors, fixtures, policy rules, receipts, proofs, release decisions, renderer code, or production code;
- bypass `EvidenceRef -> EvidenceBundle` resolution;
- bypass attachment, uncertainty-kind, footprint, nodata, evidence, validation, policy, sensitivity, correction, or rollback checks with a fixture flag;
- infer release state from file existence, uncertainty existence, layer name, map rendering, tile availability, or AI wording;
- publish, promote, or release anything.

Any test that needs real processed uncertainty outputs or public tile output belongs in a gated integration tier with source admission, lifecycle state, policy, receipts, release controls, and rollback targets.

---

## Suggested test layout

The exact Python module names remain NEEDS VERIFICATION until the runner and existing test conventions are inspected. A minimal future layout could be:

```text
tests/domains/habitat/land_cover/uncertainty/
├── README.md
├── test_uncertainty_attachment_required.py
├── test_uncertainty_kind_required.py
├── test_footprint_and_nodata.py
├── test_source_vintage_and_temporal_support.py
├── test_model_vs_observation_uncertainty.py
├── test_display_caveats.py
└── test_release_correction_rollback.py
```

---

## Run posture

```bash
pytest tests/domains/habitat/land_cover/uncertainty
```

Status of the command above: **PROPOSED / NEEDS VERIFICATION**. It assumes `pytest` is the accepted test runner and that executable test modules exist. This README does not claim the command currently passes.

---

## Evidence ledger

| Evidence | Status | Supports | Limits |
|---|---|---|---|
| Previous target file | CONFIRMED | `tests/domains/habitat/land_cover/uncertainty/README.md` existed as a blank placeholder before this replacement. | Did not define the lane. |
| `tests/README.md` | CONFIRMED | `tests/` is enforceability proof; domain-specific tests belong under `tests/domains/<domain>/`; failures should block promotion. | Does not prove habitat/land_cover/uncertainty modules or pass rate. |
| `contracts/domains/habitat/land_cover/uncertainty.md` | CONFIRMED semantic contract / PROPOSED implementation | Defines `UncertaintySurface` as carrying per-observation accuracy, valid-pixel footprint, source-vintage gap, crosswalk uncertainty, raster/geometry quality, and caveats; says it is not an observation, proof, policy decision, release manifest, or public layer. | Paired schema is a permissive scaffold; field-level enforcement remains NEEDS VERIFICATION. |
| `fixtures/domains/habitat/land_cover/uncertainty/README.md` | CONFIRMED | Fixture lane describes toy uncertainty examples and says fixtures are not lifecycle data, EvidenceBundles, source descriptors, policy decisions, review approvals, release state, public map material, public tiles, Habitat truth, or published artifacts. | Does not prove payload inventory or consumer tests. |
| `docs/domains/habitat/sublanes/land_cover.md` | CONFIRMED doctrine / PROPOSED implementation | Land-cover sublane includes `UncertaintySurface` when uncertainty is a property of the land-cover artifact itself. | Specific implementation paths and sublane structure remain PROPOSED. |

---

## Validation checklist

Before treating this README as implemented behavior, verify:

- [ ] Executable test modules exist under this lane.
- [ ] Test runner and import paths match the repo's accepted convention.
- [ ] Synthetic fixtures exist for positive and negative uncertainty cases.
- [ ] Uncertainty schema path and field expectations are accepted beyond scaffold status.
- [ ] SourceDescriptor/source-role behavior is available to tests or safely stubbed.
- [ ] EvidenceRef / EvidenceBundle resolver behavior is available to tests or safely stubbed.
- [ ] PolicyDecision, ReviewRecord, ReleaseManifest, CorrectionNotice, and RollbackCard expectations are defined before enforcing them.
- [ ] CI runs the no-network Habitat land-cover uncertainty suite.
- [ ] Failures block public carrier promotion or release candidate approval.

---

## Rollback

Rollback is required if this lane becomes a source export store, processed-artifact store, lifecycle data store, fixture root, semantic-contract root, schema authority, policy authority, proof store, release-decision root, public map/API/tile surface, AI surface, renderer implementation, pipeline implementation, or publication shortcut.

Rollback target for this replacement: previous blank blob SHA `8b137891791fe96927ad78e64b0aad7bded08bdc`.

<p align="right"><a href="#top">Back to top</a></p>
