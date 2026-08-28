<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-domains-habitat-land-cover-class-scheme-readme
title: Habitat Land-Cover Class-Scheme Test README
type: test-readme
version: v0.1
status: draft; placeholder-expanded; test-lane; PROPOSED / NEEDS VERIFICATION before promotion
owners:
  - OWNER_TBD — Habitat domain steward
  - OWNER_TBD — Land-cover steward
  - OWNER_TBD — Classification-scheme steward
  - OWNER_TBD — Source steward
  - OWNER_TBD — Evidence steward
  - OWNER_TBD — Schema steward
  - OWNER_TBD — Policy steward
  - OWNER_TBD — Validation steward
  - OWNER_TBD — Release steward
  - OWNER_TBD — QA steward
created: NEEDS VERIFICATION — blank placeholder existed before v0.1 expansion
updated: 2026-07-05
policy_label: public-doc; tests; habitat; land-cover; class-scheme; no-network; source-vintage-aware; class-inventory-aware; crosswalk-aware; evidence-bound; release-gated
tags: [kfm, tests, habitat, land_cover, class_scheme, ClassSchemeProfile, land-cover-legend, classification-scheme, class-inventory, source-vintage, crosswalk, EvidenceRef, EvidenceBundle, PolicyDecision, ReleaseManifest, CorrectionNotice, RollbackCard, ABSTAIN, DENY]
related:
  - ../../../../README.md
  - ../../../../../contracts/domains/habitat/land_cover/class_scheme.md
  - ../../../../../schemas/contracts/v1/domains/habitat/land_cover/class_scheme.schema.json
  - ../../../../../fixtures/domains/habitat/land_cover/class_scheme/README.md
  - ../../../../../docs/domains/habitat/sublanes/land_cover.md
  - ../../../../../docs/domains/habitat/MODEL_VS_OBSERVATION.md
  - ../../../../../docs/domains/habitat/SOURCE_FAMILIES.md
  - ../../../../../docs/domains/habitat/API_CONTRACTS.md
  - ../../../../../contracts/domains/habitat/land_cover/observation.md
  - ../../../../../contracts/domains/habitat/land_cover/crosswalk.md
  - ../../../../../contracts/domains/habitat/land_cover/change_summary.md
  - ../../../../../contracts/domains/habitat/land_cover/uncertainty.md
  - ../../../../../pipelines/domains/habitat/land_cover/
  - ../../../../../pipeline_specs/habitat/land_cover/
  - ../../../../../policy/domains/habitat/land_cover/
  - ../../../../../policy/sensitivity/habitat/
  - ../../../../../data/registry/sources/habitat/
  - ../../../../../data/published/layers/habitat/land_cover/README.md
  - ../../../../../release/manifests/habitat/
notes:
  - "This file replaces a blank placeholder at tests/domains/habitat/land_cover/class_scheme/README.md."
  - "This is a test-lane README only. It does not define Habitat land-cover doctrine, semantic contracts, schemas, source descriptors, class-scheme authority, fixtures, lifecycle records, evidence bundles, receipts, proofs, policy rules, release decisions, production code, public layers, or published artifacts."
  - "The tested invariant is that ClassSchemeProfile names, versions, and governs a land-cover classification vocabulary before observations, crosswalks, change summaries, public layers, or downstream Habitat reasoning can use its classes; it must not become a LandCoverObservation, CoverClassCrosswalk, LandCoverChangeSummary, source raster, HabitatPatch, occurrence proof, regulatory designation, policy decision, release artifact, public layer, or AI answer."
  - "The default posture is deterministic and no-network. Live source checks, credentials, real source legends/exports, real source rasters, sensitive occurrence joins, and public tiles do not belong in this lane."
  - "Rollback target for this replacement is previous blank blob SHA 8b137891791fe96927ad78e64b0aad7bded08bdc."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Habitat land-cover class-scheme tests

> Deterministic, no-network test documentation for proving that Habitat `ClassSchemeProfile` records stay vocabulary anchors, preserve source-version/class-inventory/source-role/evidence boundaries, and fail closed when class schemes are misused as observations, crosswalks, source rasters, habitat-quality proof, occurrence proof, regulatory truth, release truth, or AI truth.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: tests" src="https://img.shields.io/badge/root-tests%2F-blue">
  <img alt="Domain: habitat" src="https://img.shields.io/badge/domain-habitat-2e7d32">
  <img alt="Sublane: land cover" src="https://img.shields.io/badge/sublane-land__cover-6a5acd">
  <img alt="Object: ClassSchemeProfile" src="https://img.shields.io/badge/object-ClassSchemeProfile-blue">
  <img alt="Network: disabled by default" src="https://img.shields.io/badge/network-disabled__by__default-critical">
  <img alt="Boundary: scheme not observation" src="https://img.shields.io/badge/boundary-scheme__not__observation-success">
</p>

**Path:** `tests/domains/habitat/land_cover/class_scheme/README.md`  
**Status:** draft / placeholder-expanded / PROPOSED until paired test files are verified  
**Owning root:** `tests/`  
**Domain segment:** `habitat`  
**Test lane:** `land_cover/class_scheme`  
**Default execution posture:** deterministic, synthetic, no-network, public-safe fixtures only  
**Truth posture:** CONFIRMED target was a blank placeholder before this expansion · CONFIRMED `tests/` is the canonical root for enforceability proof · CONFIRMED `ClassSchemeProfile` is defined as a Habitat land-cover object that names, versions, and governs a source classification scheme or legend before observations, crosswalks, change summaries, public layers, or downstream Habitat reasoning can use its classes · CONFIRMED the paired fixture README says fixtures are examples only, not source rasters, lifecycle data, EvidenceBundles, policy decisions, release state, public API/map/tile material, habitat quality proof, occurrence proof, regulatory proof, or published artifacts · NEEDS VERIFICATION for executable test modules, fixture payload inventory, schema enforcement, validators, source registry records, policy files, imports, CI coverage, and release-gate integration.

**Quick jumps:** [Purpose](#purpose) · [Placement basis](#placement-basis) · [Invariant under test](#invariant-under-test) · [Expected test scope](#expected-test-scope) · [Fixture posture](#fixture-posture) · [Assertions](#assertions) · [Finite outcomes](#finite-outcomes) · [Forbidden shortcuts](#forbidden-shortcuts) · [Suggested test layout](#suggested-test-layout) · [Run posture](#run-posture) · [Evidence ledger](#evidence-ledger) · [Validation checklist](#validation-checklist) · [Rollback](#rollback)

---

## Purpose

`tests/domains/habitat/land_cover/class_scheme/` is the intended home for tests that prove Habitat land-cover class schemes stay inside their governed meaning.

This lane should test that a `ClassSchemeProfile` cannot silently become:

- a source raster;
- a `LandCoverObservation`;
- a `CoverClassCrosswalk`;
- a `LandCoverChangeSummary`;
- a source activation decision;
- a HabitatPatch or habitat-quality claim;
- a species or plant occurrence claim;
- a critical-habitat or regulatory designation;
- a public layer, tile, release manifest, or AI answer.

A passing test here should **not** mean that a real source legend is current, a source is activated, a crosswalk is reviewed, a public derivative is released, or a downstream habitat claim is proven. It should mean only that class-scheme guardrails behaved as expected against bounded fixtures.

---

## Placement basis

`tests/` is the canonical root for enforceability proof. Habitat appears as a lane segment inside the tests root, not as a repo-root domain folder.

| Responsibility | Correct home | This lane's relationship |
|---|---|---|
| Habitat land-cover class-scheme tests | `tests/domains/habitat/land_cover/class_scheme/` | This directory. |
| Synthetic class-scheme fixtures | `fixtures/domains/habitat/land_cover/class_scheme/` | Preferred toy inputs and expected outcomes. |
| Semantic class-scheme contract | `contracts/domains/habitat/land_cover/class_scheme.md` | Defines meaning; tests do not redefine it. |
| Machine schema | `schemas/contracts/v1/domains/habitat/land_cover/class_scheme.schema.json` | Referenced by tests; current scaffold maturity must be respected. |
| Land-cover doctrine | `docs/domains/habitat/sublanes/land_cover.md` | Referenced doctrine; not test implementation. |
| Source registry | `data/registry/sources/habitat/` | Source identity, source role, rights, cadence, caveats, and activation state. |
| Crosswalk/change-summary contracts | `contracts/domains/habitat/land_cover/crosswalk.md`, `contracts/domains/habitat/land_cover/change_summary.md` | Related consumers; not owned here. |
| Policy and sensitivity homes | `policy/domains/habitat/land_cover/`, `policy/sensitivity/habitat/` | Referenced by tests, not bypassed here. |
| Pipeline logic and specs | `pipelines/domains/habitat/land_cover/`, `pipeline_specs/habitat/land_cover/` | Systems under test where accepted; not duplicated here. |
| Published layers | `data/published/layers/habitat/land_cover/` | Released artifacts only after governed promotion. |
| Release decisions | `release/` and `release/manifests/habitat/` | Publication, correction, and rollback authority; tests cannot replace it. |

---

## Invariant under test

> **Class scheme is vocabulary authority, not spatial truth.** `ClassSchemeProfile` names and pins a classification vocabulary, version, class inventory, hierarchy, source role, rights posture, evidence support, correction lineage, and release posture. It does not assert land-cover presence anywhere and does not perform crosswalks or publish layers by itself.

For this test lane, the invariant decomposes into nine checks:

| Check | Required behavior | Failure outcome |
|---|---|---|
| Scheme identity | Scheme namespace, ID, version, and title are explicit and stable. | validation failure / `ERROR`. |
| Version immutability | Published scheme versions are not edited in place; changes create correction lineage or a new version. | validation failure. |
| Class inventory | Codes, labels, hierarchy, nodata, unknown, reserved, and deprecated classes are explicit and deterministic. | validation failure. |
| Source role | Source role and SourceDescriptor linkage are explicit before use. | `ABSTAIN` / validation failure. |
| Rights and citation | License, attribution, source artifact digest, and evidence refs are explicit where material. | `ABSTAIN` / review required. |
| Crosswalk boundary | Scheme does not silently map to another scheme; reviewed `CoverClassCrosswalk` is required. | `ABSTAIN` / validation failure. |
| Observation boundary | Scheme does not become `LandCoverObservation`; observations apply schemes to space/time. | `ABSTAIN` / validation failure. |
| Release boundary | Public UI/API/legend/layer use requires release, correction, and rollback posture where material. | promotion-blocking failure. |
| No truth upgrade | Scheme cannot become raster truth, habitat quality, occurrence truth, regulatory truth, public-layer truth, or AI truth. | `DENY` / `ABSTAIN`. |

---

## Expected test scope

Tests in this lane should be small, synthetic, and deterministic. They may validate:

- required scheme namespace, scheme ID, scheme version, title, source family, and source role;
- class inventory uniqueness and deterministic code/label handling;
- nodata, unknown, reserved, deprecated, aggregate, and source-native class handling;
- hierarchy/parent-child class rules where a scheme declares hierarchy;
- source-vintage and source-artifact digest preservation;
- denial when a scheme is treated as a `LandCoverObservation`, crosswalk, change summary, source raster, habitat quality, species/plant occurrence, regulatory designation, or release artifact;
- non-answer behavior when evidence, source rights, policy, review, release, correction, or rollback context is unresolved;
- public legend/API/UI examples that cite a released class-scheme profile without becoming the canonical scheme.

Live source legends, live source downloads, real source rasters, public tile generation, real sensitive occurrence joins, and provider credentials are out of scope for the default suite.

---

## Fixture posture

Use `fixtures/domains/habitat/land_cover/class_scheme/` when possible.

Fixture requirements:

- synthetic and public-safe;
- deterministic and no-network;
- compact enough for review in a PR;
- explicit expected outcome;
- explicit scheme namespace, scheme ID, scheme version, source role, source family, source vintage, and class inventory where material;
- explicit nodata/unknown/reserved/deprecated handling where material;
- explicit evidence, source rights, policy, review, release, correction, and rollback state where material;
- no real source exports, real source rasters, real sensitive occurrence records, rare-species/rare-plant locations, public tiles, or release artifacts.

Preferred fixture families:

| Fixture kind | Preferred lane | Example expected outcome |
|---|---|---|
| Valid toy class scheme | `fixtures/domains/habitat/land_cover/class_scheme/` | accepted as vocabulary anchor. |
| Missing scheme version | same | validation failure / `ERROR`. |
| Duplicate code with conflicting label | same or invalid lane | validation failure. |
| Missing nodata/unknown semantics | same or invalid lane | validation failure / review required. |
| Scheme used as observation | same or invalid lane | `ABSTAIN` / validation failure. |
| Scheme used as crosswalk | same or invalid lane | `ABSTAIN` / validation failure. |
| Scheme version edited in place | same or invalid lane | correction-lineage failure. |
| Source legend treated as release approval | same or invalid lane | `ABSTAIN` / validation failure. |

---

## Assertions

A useful land-cover class-scheme test should make the vocabulary boundary obvious.

### Positive path

- scheme namespace, scheme ID, and scheme version are explicit;
- class inventory is deterministic and reviewable;
- source role, rights, citation, source vintage, and source artifact digest are preserved;
- nodata, unknown, reserved, deprecated, aggregate, and source-native classes are explicit where material;
- crosswalk/change-summary/observation consumers reference the scheme without absorbing its authority;
- public-facing legends cite released scheme/evidence rather than becoming canonical truth.

### Negative path

- missing scheme version fails closed;
- duplicate class code with conflicting label fails;
- unknown or nodata values cannot be silently interpreted;
- NLCD/LANDFIRE/GAP/NWI/CDL/NatureServe/state inventory classes cannot be treated as interchangeable without a reviewed crosswalk;
- class scheme cannot replace `LandCoverObservation`, `CoverClassCrosswalk`, `LandCoverChangeSummary`, threshold policy, or source activation;
- class scheme cannot prove habitat quality, species occurrence, plant occurrence, critical habitat, hydrology truth, soil truth, hazards truth, agriculture truth, or land/title truth;
- public layer, legend, popup, tile, graph edge, or AI answer cannot become class-scheme authority.

---

## Finite outcomes

This lane should prefer explicit finite outcomes over loose pass/fail text.

| Condition | Expected outcome |
|---|---|
| Valid synthetic scheme with class inventory, source role, evidence, policy/review, release, correction, and rollback context | accepted vocabulary support / downstream carrier allowed only if separately release-admitted. |
| Missing scheme namespace, ID, version, or source role | validation failure / `ERROR`. |
| Duplicate class code with conflicting label | validation failure. |
| Unknown/nodata semantics missing | validation failure / review required. |
| Scheme treated as observation, crosswalk, change summary, source raster, or release approval | `ABSTAIN` / validation failure. |
| Scheme used as habitat quality or occurrence proof | `ABSTAIN`. |
| Version edited without correction lineage | promotion-blocking failure. |
| Policy engine unavailable | `ERROR` or `ABSTAIN`, never public exposure. |

---

## Forbidden shortcuts

Do not use this test lane to:

- fetch live upstream source systems;
- store credentials or tokens;
- store real source legends, real source exports, real source rasters, or lifecycle data;
- store real sensitive occurrence joins, rare-species/rare-plant locations, owner/land data, or exact protected-resource geometry;
- store public PMTiles, MVT, COG, GeoParquet, release artifacts, or generated public layers;
- redefine Habitat land-cover doctrine, semantic contracts, schemas, source descriptors, fixtures, policy rules, receipts, proofs, release decisions, or production code;
- bypass `EvidenceRef -> EvidenceBundle` resolution;
- bypass source-vintage, class-inventory, crosswalk, policy, sensitivity, correction, or rollback checks with a fixture flag;
- infer release state from file existence, class name, legend rendering, map rendering, tile availability, or AI wording;
- publish, promote, or release anything.

Any test that needs real source legends, source rasters, or public tile output belongs in a gated integration tier with source admission, lifecycle state, policy, receipts, release controls, and rollback targets.

---

## Suggested test layout

The exact Python module names remain NEEDS VERIFICATION until the runner and existing test conventions are inspected. A minimal future layout could be:

```text
tests/domains/habitat/land_cover/class_scheme/
├── README.md
├── test_scheme_identity_required.py      # namespace/id/version/source role required
├── test_class_inventory.py               # unique codes, labels, hierarchy, nodata/unknown/deprecated handling
├── test_crosswalk_boundary.py            # no silent recode or crosswalk authority
├── test_scheme_not_observation.py        # scheme cannot become raster/observation/habitat/occurrence truth
└── test_release_correction_rollback.py   # public legend/layer use requires release/correction/rollback context
```

Keep helpers local only when they are test-specific. Shared contracts, schemas, source registries, class inventory logic, crosswalk policy, evidence resolvers, fixtures, pipeline behavior, or release behavior belong under their accepted responsibility roots.

---

## Run posture

Default run expectations:

```bash
pytest tests/domains/habitat/land_cover/class_scheme
```

Status of the command above: **PROPOSED / NEEDS VERIFICATION**. It assumes `pytest` is the accepted test runner and that executable test modules exist. This README does not claim the command currently passes.

Expected CI posture:

- default suite: no-network, synthetic fixtures only;
- fail closed on missing scheme identity, missing version, class-inventory conflict, silent nodata/unknown interpretation, crosswalk collapse, observation collapse, unresolved evidence, missing policy, sensitive leakage, or missing release/correction/rollback posture;
- live-source or tile-generation checks: separate gated jobs only;
- release gate: land-cover class-scheme failures should block public catalog/API/map/tile/AI carrier promotion.

---

## Evidence ledger

| Evidence | Status | Supports | Limits |
|---|---|---|---|
| Previous target file | CONFIRMED | `tests/domains/habitat/land_cover/class_scheme/README.md` existed as a blank placeholder before this replacement. | Did not define the lane. |
| `tests/README.md` | CONFIRMED | `tests/` is enforceability proof; domain-specific tests belong under `tests/domains/<domain>/`; default tests should avoid sensitive data and live network calls. | Does not prove habitat/land_cover/class_scheme modules or pass rate. |
| `contracts/domains/habitat/land_cover/class_scheme.md` | CONFIRMED semantic contract / PROPOSED implementation | Defines `ClassSchemeProfile` as the object that names, versions, and governs a source classification scheme or legend before observations, crosswalks, change summaries, public layers, or downstream Habitat reasoning can use its classes. | Paired schema is a permissive scaffold; field-level enforcement remains NEEDS VERIFICATION. |
| `fixtures/domains/habitat/land_cover/class_scheme/README.md` | CONFIRMED | Fixture lane is synthetic/public-safe and not source rasters, lifecycle data, EvidenceBundles, policy decisions, release state, public API/map/tile material, habitat quality proof, occurrence proof, regulatory proof, or published artifacts. | Does not prove payload inventory or consumer tests. |
| `docs/domains/habitat/sublanes/land_cover.md` | CONFIRMED doctrine / PROPOSED implementation | Land-cover sublane treats source classifications as interpretive infrastructure, not habitat assertions, and uses land-cover source artifacts with source role, rights, citation, time, and hash. | Specific implementation paths and sublane structure remain PROPOSED. |
| Search/fetched adjacent contract and fixture lanes | CONFIRMED by repo search and fetched files | Related observation, crosswalk, change-summary, uncertainty, fixture, pipeline, schema, policy, source, and release homes exist or are referenced. | Contents and enforcement remain NEEDS VERIFICATION unless inspected. |

---

## Validation checklist

Before treating this README as implemented behavior, verify:

- [ ] Executable test modules exist under this lane.
- [ ] Test runner and import paths match the repo's accepted convention.
- [ ] Synthetic fixtures exist for valid scheme, missing version, duplicate code conflict, missing nodata/unknown semantics, hierarchy mismatch, deprecated class use, scheme-as-observation, scheme-as-crosswalk, scheme-as-release-approval, and missing release/correction/rollback posture.
- [ ] Class-scheme schema path and field expectations are accepted beyond scaffold status.
- [ ] LandCoverObservation, CoverClassCrosswalk, LandCoverChangeSummary, uncertainty, and source-registry expectations are accepted before enforcing them.
- [ ] SourceDescriptor/source-role behavior is available to tests or safely stubbed.
- [ ] EvidenceRef / EvidenceBundle resolver behavior is available to tests or safely stubbed.
- [ ] PolicyDecision and sensitivity behavior are available to tests or safely stubbed.
- [ ] ReleaseManifest, CorrectionNotice, and RollbackCard expectations are defined before enforcing them.
- [ ] CI runs the no-network Habitat land-cover class-scheme suite.
- [ ] Failures block public carrier promotion or release candidate approval.

---

## Rollback

Rollback is required if this lane becomes a source legend store, source raster store, lifecycle data store, fixture root, semantic-contract root, schema authority, crosswalk authority, threshold-policy authority, source registry, proof store, receipt store, release-decision root, public map/API/tile surface, AI surface, or publication shortcut.

Rollback target for this replacement: previous blank blob SHA `8b137891791fe96927ad78e64b0aad7bded08bdc`.

<p align="right"><a href="#top">Back to top</a></p>
