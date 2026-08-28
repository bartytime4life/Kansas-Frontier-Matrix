<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-domains-habitat-land-cover-observation-readme
title: Habitat Land-Cover Observation Test README
type: test-readme
version: v0.1
status: draft; placeholder-expanded; test-lane; PROPOSED / NEEDS VERIFICATION before promotion
owners:
  - OWNER_TBD — Habitat domain steward
  - OWNER_TBD — Land-cover steward
  - OWNER_TBD — Observation steward
  - OWNER_TBD — Source steward
  - OWNER_TBD — Evidence steward
  - OWNER_TBD — Schema steward
  - OWNER_TBD — Policy steward
  - OWNER_TBD — Validation steward
  - OWNER_TBD — Release steward
  - OWNER_TBD — QA steward
created: NEEDS VERIFICATION — blank placeholder existed before v0.1 expansion
updated: 2026-07-05
policy_label: public-doc; tests; habitat; land-cover; observation; no-network; source-role-aware; source-vintage-aware; valid-pixel-aware; evidence-bound; release-gated
tags: [kfm, tests, habitat, land_cover, observation, LandCoverObservation, class-scheme, source-vintage, source-role, valid-pixel-footprint, categorical-raster, continuous-raster, EvidenceRef, EvidenceBundle, PolicyDecision, ReleaseManifest, CorrectionNotice, RollbackCard, ABSTAIN, DENY]
related:
  - ../../../../README.md
  - ../../../../../contracts/domains/habitat/land_cover/observation.md
  - ../../../../../schemas/contracts/v1/domains/habitat/land_cover/observation.schema.json
  - ../../../../../fixtures/domains/habitat/land_cover/observation/README.md
  - ../../../../../docs/domains/habitat/sublanes/land_cover.md
  - ../../../../../docs/domains/habitat/MODEL_VS_OBSERVATION.md
  - ../../../../../docs/domains/habitat/SOURCE_FAMILIES.md
  - ../../../../../docs/domains/habitat/API_CONTRACTS.md
  - ../../../../../contracts/domains/habitat/land_cover/class_scheme.md
  - ../../../../../contracts/domains/habitat/land_cover/crosswalk.md
  - ../../../../../contracts/domains/habitat/land_cover/change_summary.md
  - ../../../../../contracts/domains/habitat/land_cover/model_run_receipt.md
  - ../../../../../contracts/domains/habitat/land_cover/uncertainty.md
  - ../../../../../pipelines/domains/habitat/land_cover/
  - ../../../../../pipeline_specs/habitat/land_cover/
  - ../../../../../policy/domains/habitat/land_cover/
  - ../../../../../policy/sensitivity/habitat/
  - ../../../../../data/registry/sources/habitat/
  - ../../../../../data/published/layers/habitat/land_cover/README.md
  - ../../../../../release/manifests/habitat/
notes:
  - "This file replaces a blank placeholder at tests/domains/habitat/land_cover/observation/README.md."
  - "This is a test-lane README only. It does not define Habitat land-cover doctrine, semantic contracts, schemas, source descriptors, class-scheme authority, fixtures, lifecycle records, evidence bundles, receipts, proofs, policy rules, release decisions, production code, public layers, or published artifacts."
  - "The tested invariant is that LandCoverObservation records a governed categorical or continuous land-cover classification over a declared spatial and temporal scope with source role, class scheme, CRS, resolution, valid-pixel support, evidence refs, policy posture, correction, and rollback; it must not become a ClassSchemeProfile, CoverClassCrosswalk, LandCoverChangeSummary, ModelRunReceipt, LayerManifest, HabitatPatch, occurrence claim, source activation decision, release authority, public layer, or AI/UI truth."
  - "The default posture is deterministic and no-network. Live source checks, real source exports, real source rasters, public tiles, and sensitive joined records do not belong in this lane."
  - "Rollback target for this replacement is previous blank blob SHA 8b137891791fe96927ad78e64b0aad7bded08bdc."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Habitat land-cover observation tests

> Deterministic, no-network test documentation for proving that Habitat `LandCoverObservation` records preserve source role, class-scheme binding, source vintage, spatial/temporal scope, CRS/resolution, valid-pixel support, evidence posture, correction, and rollback without turning observations into class schemes, crosswalks, change summaries, receipts, release authority, public layers, or AI/UI truth.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: tests" src="https://img.shields.io/badge/root-tests%2F-blue">
  <img alt="Domain: habitat" src="https://img.shields.io/badge/domain-habitat-2e7d32">
  <img alt="Sublane: land cover" src="https://img.shields.io/badge/sublane-land__cover-6a5acd">
  <img alt="Object: LandCoverObservation" src="https://img.shields.io/badge/object-LandCoverObservation-blue">
  <img alt="Network: disabled by default" src="https://img.shields.io/badge/network-disabled__by__default-critical">
  <img alt="Boundary: observation not release" src="https://img.shields.io/badge/boundary-observation__not__release-success">
</p>

**Path:** `tests/domains/habitat/land_cover/observation/README.md`  
**Status:** draft / placeholder-expanded / PROPOSED until paired test files are verified  
**Owning root:** `tests/`  
**Domain segment:** `habitat`  
**Test lane:** `land_cover/observation`  
**Default execution posture:** deterministic, synthetic, no-network, public-safe fixtures only  
**Truth posture:** CONFIRMED target was a blank placeholder before this expansion · CONFIRMED `tests/` is the canonical root for enforceability proof · CONFIRMED `LandCoverObservation` is defined as a governed categorical or continuous land-cover classification over declared spatial and temporal scope with source role, class scheme, CRS, resolution, valid-pixel support, evidence refs, policy posture, correction, and rollback · CONFIRMED the paired fixture README says examples are not source records, lifecycle data, EvidenceBundles, source descriptors, policy decisions, review approvals, release state, public API/map/tile material, Habitat truth, or published artifacts · NEEDS VERIFICATION for executable test modules, fixture payload inventory, schema enforcement, validators, source registry records, policy files, imports, CI coverage, and release-gate integration.

**Quick jumps:** [Purpose](#purpose) · [Placement basis](#placement-basis) · [Invariant under test](#invariant-under-test) · [Expected test scope](#expected-test-scope) · [Fixture posture](#fixture-posture) · [Assertions](#assertions) · [Finite outcomes](#finite-outcomes) · [Forbidden shortcuts](#forbidden-shortcuts) · [Suggested test layout](#suggested-test-layout) · [Run posture](#run-posture) · [Evidence ledger](#evidence-ledger) · [Validation checklist](#validation-checklist) · [Rollback](#rollback)

---

## Purpose

`tests/domains/habitat/land_cover/observation/` is the intended home for tests that prove Habitat land-cover observations stay inside their governed meaning.

This lane should test that a `LandCoverObservation` cannot silently become:

- a `ClassSchemeProfile`;
- a `CoverClassCrosswalk`;
- a `LandCoverChangeSummary`;
- a `ModelRunReceipt`;
- a `LayerManifest`;
- a source activation decision;
- a HabitatPatch or habitat-quality claim;
- an occurrence claim;
- a critical-habitat or regulatory designation;
- a public layer, tile, release manifest, or AI answer.

A passing test here should **not** mean that a real observation is admitted, a source is activated, a public derivative is released, or a downstream habitat claim is proven. It should mean only that observation guardrails behaved as expected against bounded fixtures.

---

## Placement basis

`tests/` is the canonical root for enforceability proof. Habitat appears as a lane segment inside the tests root, not as a repo-root domain folder.

| Responsibility | Correct home | This lane's relationship |
|---|---|---|
| Habitat land-cover observation tests | `tests/domains/habitat/land_cover/observation/` | This directory. |
| Synthetic observation fixtures | `fixtures/domains/habitat/land_cover/observation/` | Preferred toy inputs and expected outcomes. |
| Semantic observation contract | `contracts/domains/habitat/land_cover/observation.md` | Defines meaning; tests do not redefine it. |
| Machine schema | `schemas/contracts/v1/domains/habitat/land_cover/observation.schema.json` | Referenced by tests; current scaffold maturity must be respected. |
| Land-cover doctrine | `docs/domains/habitat/sublanes/land_cover.md` | Referenced doctrine; not test implementation. |
| Class schemes and crosswalks | `contracts/domains/habitat/land_cover/class_scheme.md`, `contracts/domains/habitat/land_cover/crosswalk.md` | Observation dependencies; not owned here. |
| Change summary / model-run / layer consumers | `contracts/domains/habitat/land_cover/change_summary.md`, `contracts/domains/habitat/land_cover/model_run_receipt.md`, layer manifest/descriptor lanes | Downstream consumers; they do not replace observations. |
| Source registry | `data/registry/sources/habitat/` | Source identity, source role, rights, cadence, caveats, and activation state. |
| Policy and sensitivity homes | `policy/domains/habitat/land_cover/`, `policy/sensitivity/habitat/` | Referenced by tests, not bypassed here. |
| Pipeline logic and specs | `pipelines/domains/habitat/land_cover/`, `pipeline_specs/habitat/land_cover/` | Systems under test where accepted; not duplicated here. |
| Release decisions | `release/` and `release/manifests/habitat/` | Publication, correction, and rollback authority; tests cannot replace it. |

---

## Invariant under test

> **Observation is source-role-aware context, not release truth.** `LandCoverObservation` records a categorical or continuous classification over declared space and time. It must preserve source identity, source role, class scheme, source vintage, CRS/resolution, valid-pixel support, evidence refs, validation posture, policy posture, correction lineage, and rollback target without becoming a class scheme, crosswalk, change summary, receipt, source activation, release authority, public layer, or AI/UI truth.

For this test lane, the invariant decomposes into ten checks:

| Check | Required behavior | Failure outcome |
|---|---|---|
| Observation identity | Observation ID, source ID, class scheme, spatial scope, temporal scope, and digest basis are explicit. | validation failure / `ERROR`. |
| Source role | Source role and SourceDescriptor linkage are explicit before use. | `ABSTAIN` / validation failure. |
| Class-scheme binding | Observation cites a reviewed class scheme and version. | validation failure. |
| Spatial scope | Extent, analysis unit, footprint, CRS, resolution, and geometry/raster posture are explicit. | validation failure. |
| Temporal scope | Source vintage, observed/acquisition period, valid period, retrieval time, release time, and correction time remain distinct. | validation failure. |
| Valid-pixel support | Nodata, mask, coverage, footprint, and comparable-area posture are explicit where material. | validation failure / review required. |
| Evidence closure | Consequential use resolves `EvidenceRef -> EvidenceBundle` or produces a finite non-answer. | `ABSTAIN`. |
| Model-vs-observation | Modeled or derived outputs do not silently become observed products. | `ABSTAIN` / validation failure. |
| Release boundary | Public use requires policy, review, release, correction, and rollback linkage where material. | promotion-blocking failure. |
| No authority upgrade | Observation cannot become patch quality, occurrence truth, regulatory truth, public-layer truth, or AI truth. | `DENY` / `ABSTAIN`. |

---

## Expected test scope

Tests in this lane should be small, synthetic, and deterministic. They may validate:

- required source ID, source role, source vintage, class-scheme reference, spatial scope, temporal scope, CRS/resolution, and digest basis;
- valid-pixel and nodata/mask/footprint behavior for raster-like examples;
- class-scheme binding and rejection of observations that silently define their own vocabulary;
- rejection of unreviewed crosswalk or reclassification collapse;
- rejection of modeled output presented as observed product;
- non-answer behavior when evidence, source rights, validation, policy, review, release, correction, or rollback context is unresolved;
- public-carrier failure when an observation is treated as a layer, tile, release approval, HabitatPatch, occurrence proof, or AI answer.

Live source downloads, real source rasters, public tile generation, sensitive occurrence joins, and provider-backed model calls are out of scope for the default suite.

---

## Fixture posture

Use `fixtures/domains/habitat/land_cover/observation/` when possible.

Fixture requirements:

- synthetic and public-safe;
- deterministic and no-network;
- compact enough for review in a PR;
- explicit expected outcome;
- explicit observation ID, source ID, source role, source vintage, class scheme, spatial scope, temporal scope, CRS/resolution, valid-pixel support, evidence state, validation state, policy state, review state, release state, correction state, and rollback state where material;
- no real source exports, real source rasters, real public tiles, sensitive joined records, or published artifacts.

Preferred fixture families:

| Fixture kind | Preferred lane | Example expected outcome |
|---|---|---|
| Valid toy observation | `fixtures/domains/habitat/land_cover/observation/` | accepted as observation support only. |
| Missing source ID or source role | same | validation failure. |
| Missing class-scheme reference | same or invalid lane | validation failure. |
| Missing spatial or temporal scope | same or invalid lane | validation failure. |
| Missing valid-pixel support | same or invalid lane | review required / validation failure. |
| Observation used as class scheme or crosswalk | same or invalid lane | validation failure. |
| Modeled output presented as observed input | same or invalid lane | `ABSTAIN` / validation failure. |
| Observation treated as release approval | same or invalid lane | validation failure. |

---

## Assertions

A useful land-cover observation test should make the observation boundary obvious.

### Positive path

- source identity and source role are explicit;
- class scheme and version are explicit;
- spatial and temporal scopes are explicit;
- CRS, resolution, valid-pixel, nodata, mask, and footprint posture are visible where material;
- evidence, validation, policy, review, release, correction, and rollback references are linkable where material;
- downstream class-scheme, crosswalk, change-summary, model-run, uncertainty, layer, API, renderer, Evidence Drawer, Focus Mode, or AI examples remain carriers or consumers, not observation authority.

### Negative path

- missing source ID, source role, class scheme, spatial scope, or temporal scope fails closed;
- observation cannot define a class scheme or crosswalk by implication;
- modeled/derived output cannot become observed source truth without explicit governed posture;
- observation cannot replace EvidenceBundle proof, PolicyDecision, ReviewRecord, ReleaseManifest, catalog closure, or source activation;
- public layer, legend, popup, tile, graph edge, Focus Mode answer, or AI text cannot become observation authority.

---

## Finite outcomes

This lane should prefer explicit finite outcomes over loose pass/fail text.

| Condition | Expected outcome |
|---|---|
| Valid synthetic observation with source role, class scheme, spatial/temporal scope, valid-pixel support, evidence, policy, review, release relationship, correction, and rollback context | accepted observation support only. |
| Missing source ID, source role, class scheme, spatial scope, or temporal scope | validation failure / `ERROR`. |
| Missing valid-pixel support where material | validation failure / review required. |
| Observation treated as class scheme, crosswalk, change summary, receipt, source activation, or release approval | validation failure. |
| Modeled output presented as observed product | `ABSTAIN` / validation failure. |
| Observation used as habitat quality or occurrence proof | `ABSTAIN`. |
| Policy engine unavailable | `ERROR` or `ABSTAIN`, never public exposure. |

---

## Forbidden shortcuts

Do not use this test lane to:

- fetch live upstream source systems;
- store real source exports, real source rasters, real lifecycle data, or real public tiles;
- store proof packs, release manifests, or generated public layers;
- store sensitive joined records or exact protected-resource geometry;
- redefine observation contracts, Habitat land-cover doctrine, schemas, source descriptors, fixtures, policy rules, receipts, proofs, release decisions, renderer code, or production code;
- bypass `EvidenceRef -> EvidenceBundle` resolution;
- bypass source-role, class-scheme, valid-pixel, evidence, validation, policy, sensitivity, correction, or rollback checks with a fixture flag;
- infer release state from file existence, observation existence, layer name, map rendering, tile availability, or AI wording;
- publish, promote, or release anything.

Any test that needs real source rasters or public tile output belongs in a gated integration tier with source admission, lifecycle state, policy, receipts, release controls, and rollback targets.

---

## Suggested test layout

The exact Python module names remain NEEDS VERIFICATION until the runner and existing test conventions are inspected. A minimal future layout could be:

```text
tests/domains/habitat/land_cover/observation/
├── README.md
├── test_observation_identity_required.py
├── test_source_role_required.py
├── test_class_scheme_binding.py
├── test_spatial_temporal_scope.py
├── test_valid_pixel_support.py
├── test_model_vs_observation.py
└── test_release_correction_rollback.py
```

---

## Run posture

```bash
pytest tests/domains/habitat/land_cover/observation
```

Status of the command above: **PROPOSED / NEEDS VERIFICATION**. It assumes `pytest` is the accepted test runner and that executable test modules exist. This README does not claim the command currently passes.

---

## Evidence ledger

| Evidence | Status | Supports | Limits |
|---|---|---|---|
| Previous target file | CONFIRMED | `tests/domains/habitat/land_cover/observation/README.md` existed as a blank placeholder before this replacement. | Did not define the lane. |
| `tests/README.md` | CONFIRMED | `tests/` is enforceability proof; domain-specific tests belong under `tests/domains/<domain>/`; failures should block promotion. | Does not prove habitat/land_cover/observation modules or pass rate. |
| `contracts/domains/habitat/land_cover/observation.md` | CONFIRMED semantic contract / PROPOSED implementation | Defines `LandCoverObservation` as governed categorical or continuous classification over declared spatial/temporal scope and says it is not a class scheme, crosswalk, change summary, receipt, public layer, release authority, or AI/UI truth. | Paired schema is a permissive scaffold; field-level enforcement remains NEEDS VERIFICATION. |
| `fixtures/domains/habitat/land_cover/observation/README.md` | CONFIRMED | Fixture lane describes toy observation examples and says fixtures are not lifecycle data, EvidenceBundles, source descriptors, policy decisions, review approvals, release state, public map material, public tiles, Habitat truth, or published artifacts. | Does not prove payload inventory or consumer tests. |
| `docs/domains/habitat/sublanes/land_cover.md` | CONFIRMED doctrine / PROPOSED implementation | Land-cover sublane owns `LandCoverObservation` and treats source classifications as interpretive infrastructure rather than habitat assertions. | Specific implementation paths and sublane structure remain PROPOSED. |

---

## Validation checklist

Before treating this README as implemented behavior, verify:

- [ ] Executable test modules exist under this lane.
- [ ] Test runner and import paths match the repo's accepted convention.
- [ ] Synthetic fixtures exist for positive and negative observation cases.
- [ ] Observation schema path and field expectations are accepted beyond scaffold status.
- [ ] SourceDescriptor/source-role behavior is available to tests or safely stubbed.
- [ ] EvidenceRef / EvidenceBundle resolver behavior is available to tests or safely stubbed.
- [ ] PolicyDecision, ReviewRecord, ReleaseManifest, CorrectionNotice, and RollbackCard expectations are defined before enforcing them.
- [ ] CI runs the no-network Habitat land-cover observation suite.
- [ ] Failures block public carrier promotion or release candidate approval.

---

## Rollback

Rollback is required if this lane becomes a source export store, observation store, lifecycle data store, fixture root, semantic-contract root, schema authority, policy authority, proof store, release-decision root, public map/API/tile surface, AI surface, renderer implementation, pipeline implementation, or publication shortcut.

Rollback target for this replacement: previous blank blob SHA `8b137891791fe96927ad78e64b0aad7bded08bdc`.

<p align="right"><a href="#top">Back to top</a></p>
