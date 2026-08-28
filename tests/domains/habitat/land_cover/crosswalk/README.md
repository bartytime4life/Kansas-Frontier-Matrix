<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-domains-habitat-land-cover-crosswalk-readme
title: Habitat Land-Cover Crosswalk Test README
type: test-readme
version: v0.1
status: draft; placeholder-expanded; test-lane; PROPOSED / NEEDS VERIFICATION before promotion
owners:
  - OWNER_TBD — Habitat domain steward
  - OWNER_TBD — Land-cover steward
  - OWNER_TBD — Crosswalk steward
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
policy_label: public-doc; tests; habitat; land-cover; crosswalk; no-network; class-scheme-aware; source-vintage-aware; evidence-bound; no-silent-recode; release-gated
tags: [kfm, tests, habitat, land_cover, crosswalk, CoverClassCrosswalk, ClassSchemeProfile, class-scheme, no-silent-recode, directionality, mapping-coverage, lossiness, EvidenceRef, EvidenceBundle, PolicyDecision, ReleaseManifest, CorrectionNotice, RollbackCard, ABSTAIN, DENY]
related:
  - ../../../../README.md
  - ../../../../../contracts/domains/habitat/land_cover/crosswalk.md
  - ../../../../../schemas/contracts/v1/domains/habitat/land_cover/crosswalk.schema.json
  - ../../../../../fixtures/domains/habitat/land_cover/crosswalk/README.md
  - ../../../../../docs/domains/habitat/sublanes/land_cover.md
  - ../../../../../docs/domains/habitat/MODEL_VS_OBSERVATION.md
  - ../../../../../docs/domains/habitat/SOURCE_FAMILIES.md
  - ../../../../../docs/domains/habitat/API_CONTRACTS.md
  - ../../../../../contracts/domains/habitat/land_cover/class_scheme.md
  - ../../../../../contracts/domains/habitat/land_cover/observation.md
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
  - "This file replaces a blank placeholder at tests/domains/habitat/land_cover/crosswalk/README.md."
  - "This is a test-lane README only. It does not define Habitat land-cover doctrine, semantic contracts, schemas, source descriptors, class-scheme authority, crosswalk authority, fixtures, lifecycle records, evidence bundles, receipts, proofs, policy rules, release decisions, production code, public layers, or published artifacts."
  - "The tested invariant is that CoverClassCrosswalk records a reviewed, versioned, citable mapping between two ClassSchemeProfile records so observations, summaries, layers, and downstream Habitat products never rely on silent recodes; it must not become a ClassSchemeProfile, LandCoverObservation, LandCoverChangeSummary, source raster, renderer style, public layer, policy decision, release manifest, source truth, or AI answer."
  - "The default posture is deterministic and no-network. Live source checks, credentials, real source legends/exports, real source rasters, sensitive occurrence joins, and public tiles do not belong in this lane."
  - "Rollback target for this replacement is previous blank blob SHA 8b137891791fe96927ad78e64b0aad7bded08bdc."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Habitat land-cover crosswalk tests

> Deterministic, no-network test documentation for proving that Habitat `CoverClassCrosswalk` records stay explicit, reviewed, versioned, citable mappings between class schemes and fail closed when crosswalks are hidden inside renderers, notebooks, summaries, observations, public layers, or AI text.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: tests" src="https://img.shields.io/badge/root-tests%2F-blue">
  <img alt="Domain: habitat" src="https://img.shields.io/badge/domain-habitat-2e7d32">
  <img alt="Sublane: land cover" src="https://img.shields.io/badge/sublane-land__cover-6a5acd">
  <img alt="Object: CoverClassCrosswalk" src="https://img.shields.io/badge/object-CoverClassCrosswalk-blue">
  <img alt="Network: disabled by default" src="https://img.shields.io/badge/network-disabled__by__default-critical">
  <img alt="Boundary: no silent recode" src="https://img.shields.io/badge/boundary-no__silent__recode-success">
</p>

**Path:** `tests/domains/habitat/land_cover/crosswalk/README.md`  
**Status:** draft / placeholder-expanded / PROPOSED until paired test files are verified  
**Owning root:** `tests/`  
**Domain segment:** `habitat`  
**Test lane:** `land_cover/crosswalk`  
**Default execution posture:** deterministic, synthetic, no-network, public-safe fixtures only  
**Truth posture:** CONFIRMED target was a blank placeholder before this expansion · CONFIRMED `tests/` is the canonical root for enforceability proof · CONFIRMED `CoverClassCrosswalk` is defined as a reviewed, versioned, citable mapping between two `ClassSchemeProfile` records so observations, summaries, layers, and downstream Habitat products never rely on silent recodes · CONFIRMED the paired fixture README says fixtures are examples only, not source records, lifecycle data, EvidenceBundles, source descriptors, review approvals, release state, public API/map/tile material, Habitat truth, or published artifacts · NEEDS VERIFICATION for executable test modules, fixture payload inventory, schema enforcement, validators, source registry records, policy files, imports, CI coverage, and release-gate integration.

**Quick jumps:** [Purpose](#purpose) · [Placement basis](#placement-basis) · [Invariant under test](#invariant-under-test) · [Expected test scope](#expected-test-scope) · [Fixture posture](#fixture-posture) · [Assertions](#assertions) · [Finite outcomes](#finite-outcomes) · [Forbidden shortcuts](#forbidden-shortcuts) · [Suggested test layout](#suggested-test-layout) · [Run posture](#run-posture) · [Evidence ledger](#evidence-ledger) · [Validation checklist](#validation-checklist) · [Rollback](#rollback)

---

## Purpose

`tests/domains/habitat/land_cover/crosswalk/` is the intended home for tests that prove Habitat land-cover crosswalks stay inside their governed meaning.

This lane should test that a `CoverClassCrosswalk` cannot silently become:

- a `ClassSchemeProfile`;
- a `LandCoverObservation`;
- a `LandCoverChangeSummary`;
- a source raster;
- a renderer style or UI legend shortcut;
- an ecological-system synthesis;
- a HabitatPatch or habitat-quality claim;
- a species or plant occurrence claim;
- a public layer, tile, release manifest, policy decision, or AI answer.

A passing test here should **not** mean that a real crosswalk is accepted, a reverse mapping is allowed, a many-to-one mapping is lossless, a public derivative is released, or a downstream habitat claim is proven. It should mean only that crosswalk guardrails behaved as expected against bounded fixtures.

---

## Placement basis

`tests/` is the canonical root for enforceability proof. Habitat appears as a lane segment inside the tests root, not as a repo-root domain folder.

| Responsibility | Correct home | This lane's relationship |
|---|---|---|
| Habitat land-cover crosswalk tests | `tests/domains/habitat/land_cover/crosswalk/` | This directory. |
| Synthetic crosswalk fixtures | `fixtures/domains/habitat/land_cover/crosswalk/` | Preferred toy inputs and expected outcomes. |
| Semantic crosswalk contract | `contracts/domains/habitat/land_cover/crosswalk.md` | Defines meaning; tests do not redefine it. |
| Machine schema | `schemas/contracts/v1/domains/habitat/land_cover/crosswalk.schema.json` | Referenced by tests; current scaffold maturity must be respected. |
| Land-cover doctrine | `docs/domains/habitat/sublanes/land_cover.md` | Referenced doctrine; not test implementation. |
| Source and target schemes | `contracts/domains/habitat/land_cover/class_scheme.md` | Crosswalk depends on reviewed schemes; does not replace them. |
| Change-summary consumer | `contracts/domains/habitat/land_cover/change_summary.md` | May cite crosswalks; does not define them. |
| Source registry | `data/registry/sources/habitat/` | Source identity, source role, rights, cadence, caveats, and activation state. |
| Policy and sensitivity homes | `policy/domains/habitat/land_cover/`, `policy/sensitivity/habitat/` | Referenced by tests, not bypassed here. |
| Pipeline logic and specs | `pipelines/domains/habitat/land_cover/`, `pipeline_specs/habitat/land_cover/` | Systems under test where accepted; not duplicated here. |
| Published layers | `data/published/layers/habitat/land_cover/` | Released artifacts only after governed promotion. |
| Release decisions | `release/` and `release/manifests/habitat/` | Publication, correction, and rollback authority; tests cannot replace it. |

---

## Invariant under test

> **Crosswalk is reviewed mapping, not silent recode.** `CoverClassCrosswalk` records an explicit, versioned, citable mapping between two `ClassSchemeProfile` records. It must preserve directionality, class coverage, lossiness, uncertainty, evidence support, allowed use, denied use, review state, policy state, correction lineage, and rollback target.

For this test lane, the invariant decomposes into ten checks:

| Check | Required behavior | Failure outcome |
|---|---|---|
| Source and target schemes | Both scheme IDs, versions, and roles are explicit. | validation failure / `ERROR`. |
| Directionality | Forward, bidirectional-reviewed, inverse-derived, symmetric, or unknown posture is explicit. | review required / validation failure. |
| Version immutability | Crosswalk versions are not edited in place; changes create correction lineage or a new version. | validation failure. |
| Mapping inventory | Source classes are mapped, held, denied, unknown, nodata, partial, aggregate, or explicitly unmapped. | validation failure. |
| Lossiness | Many-to-one, one-to-many, partial, probabilistic, conditional, or advisory mappings carry visible caveats. | validation failure / `ABSTAIN`. |
| Source-role preservation | Mapping does not upgrade modeled, observed, regulatory, aggregate, adjacency, candidate, or synthetic posture. | `DENY` / validation failure. |
| Evidence closure | Claim-bearing outputs resolve `EvidenceRef -> EvidenceBundle` or produce a finite non-answer. | `ABSTAIN`. |
| Allowed/denied use | Use in observations, change summaries, layers, ecological-system synthesis, Focus Mode, exports, or research-only modes is explicit. | validation failure / review required. |
| Release/correction/rollback | Public use requires review, policy, release, correction, and rollback linkage where material. | promotion-blocking failure. |
| No authority upgrade | Crosswalk cannot become scheme truth, observation truth, renderer truth, source raster truth, public-layer truth, habitat/occurrence truth, or AI truth. | `DENY` / `ABSTAIN`. |

---

## Expected test scope

Tests in this lane should be small, synthetic, and deterministic. They may validate:

- required source/target scheme IDs and versions;
- directionality and rejection of unreviewed reverse use;
- class coverage, unmapped classes, unknown/nodata handling, and denied mappings;
- lossiness and uncertainty visibility for many-to-one, one-to-many, partial, conditional, probabilistic, or advisory mappings;
- rejection of crosswalks hidden in renderer styles, notebooks, UI legends, change summaries, or downstream model code;
- source-role preservation across mapping use;
- evidence closure for citable mapping methods, reviewer notes, source legends, and artifact digests;
- denial when a crosswalk is treated as a class scheme, observation, change summary, source raster, ecological-system synthesis, HabitatPatch, occurrence proof, public layer, release manifest, or AI answer;
- public carrier failure when release, correction, rollback, policy, or review posture is missing.

Live source legends, live source downloads, real source rasters, public tile generation, real sensitive occurrence joins, and provider credentials are out of scope for the default suite.

---

## Fixture posture

Use `fixtures/domains/habitat/land_cover/crosswalk/` when possible.

Fixture requirements:

- synthetic and public-safe;
- deterministic and no-network;
- compact enough for review in a PR;
- explicit expected outcome;
- explicit source and target class-scheme references;
- explicit mapping version, directionality, mapping kind, class coverage, lossiness, confidence, allowed use, and denied use where material;
- explicit evidence, source role, source rights, review, policy, release, correction, and rollback state where material;
- no real source exports, real source rasters, real sensitive occurrence records, rare-species/rare-plant locations, public tiles, or release artifacts.

Preferred fixture families:

| Fixture kind | Preferred lane | Example expected outcome |
|---|---|---|
| Valid toy crosswalk | `fixtures/domains/habitat/land_cover/crosswalk/` | accepted as reviewed mapping support. |
| Missing source or target scheme | same | validation failure / `ERROR`. |
| Missing directionality | same or invalid lane | review required / validation failure. |
| Reverse mapping used without review | same or invalid lane | `ABSTAIN` / validation failure. |
| Many-to-one mapping marked lossless | same or invalid lane | validation failure. |
| Unmapped class silently dropped | same or invalid lane | validation failure. |
| Crosswalk used as class scheme | same or invalid lane | validation failure. |
| Crosswalk used as observation or renderer transform | same or invalid lane | `ABSTAIN` / validation failure. |
| Missing release/correction/rollback for public carrier | same or invalid lane | promotion block / review required. |

---

## Assertions

A useful land-cover crosswalk test should make the no-silent-recode boundary obvious.

### Positive path

- source and target schemes are explicit and version-pinned;
- directionality and review state are explicit;
- mapping table and digest are stable;
- unmapped, denied, unknown, nodata, aggregate, and ambiguous classes are visible;
- mapping lossiness and confidence are visible;
- source role and evidence posture are preserved;
- allowed and denied use cases are explicit;
- public-facing examples cite released crosswalk/evidence rather than becoming transform authority.

### Negative path

- missing source or target scheme fails closed;
- reverse mapping is not implied;
- many-to-one mappings cannot be treated as lossless;
- unmapped classes cannot disappear silently;
- crosswalk cannot replace class scheme, observation, change summary, source raster, renderer style, threshold policy, or source activation;
- crosswalk cannot prove habitat quality, species occurrence, plant occurrence, critical habitat, hydrology truth, soil truth, hazards truth, agriculture truth, or land/title truth;
- public layer, legend, popup, tile, graph edge, notebook, or AI answer cannot become crosswalk authority.

---

## Finite outcomes

This lane should prefer explicit finite outcomes over loose pass/fail text.

| Condition | Expected outcome |
|---|---|
| Valid synthetic crosswalk with source/target schemes, directionality, mapping coverage, evidence, review, policy, release, correction, and rollback context | accepted mapping support / downstream carrier allowed only if separately release-admitted. |
| Missing source or target scheme | validation failure / `ERROR`. |
| Missing directionality | review required / validation failure. |
| Reverse mapping requested without explicit reviewed posture | `ABSTAIN` / validation failure. |
| Many-to-one mapping presented as lossless | validation failure. |
| Crosswalk treated as scheme, observation, renderer, source raster, or release approval | `ABSTAIN` / validation failure. |
| Crosswalk used as habitat quality or occurrence proof | `ABSTAIN`. |
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
- hide recode logic in renderer styles, notebooks, charts, UI legends, AI prompts, or downstream summaries;
- bypass `EvidenceRef -> EvidenceBundle` resolution;
- bypass source/target scheme validation, directionality, coverage, lossiness, policy, sensitivity, correction, or rollback checks with a fixture flag;
- infer release state from file existence, class name, legend rendering, map rendering, tile availability, or AI wording;
- publish, promote, or release anything.

Any test that needs real source legends, source rasters, or public tile output belongs in a gated integration tier with source admission, lifecycle state, policy, receipts, release controls, and rollback targets.

---

## Suggested test layout

The exact Python module names remain NEEDS VERIFICATION until the runner and existing test conventions are inspected. A minimal future layout could be:

```text
tests/domains/habitat/land_cover/crosswalk/
├── README.md
├── test_source_target_scheme_required.py  # source/target scheme IDs and versions required
├── test_directionality.py                 # reverse use is not automatic
├── test_mapping_inventory.py              # coverage, unmapped, nodata, denied, ambiguous rows
├── test_lossiness_and_uncertainty.py       # lossy mappings must be visible
├── test_crosswalk_not_renderer.py          # no hidden recode in style/UI/notebook/summary
└── test_release_correction_rollback.py    # public use requires release/correction/rollback context
```

Keep helpers local only when they are test-specific. Shared contracts, schemas, source registries, class inventory logic, crosswalk policy, evidence resolvers, fixtures, pipeline behavior, or release behavior belong under their accepted responsibility roots.

---

## Run posture

Default run expectations:

```bash
pytest tests/domains/habitat/land_cover/crosswalk
```

Status of the command above: **PROPOSED / NEEDS VERIFICATION**. It assumes `pytest` is the accepted test runner and that executable test modules exist. This README does not claim the command currently passes.

Expected CI posture:

- default suite: no-network, synthetic fixtures only;
- fail closed on missing source/target schemes, missing directionality, reverse-use collapse, class-coverage gaps, lossiness collapse, silent renderer recode, unresolved evidence, missing policy, sensitive leakage, or missing release/correction/rollback posture;
- live-source or tile-generation checks: separate gated jobs only;
- release gate: land-cover crosswalk failures should block public catalog/API/map/tile/AI carrier promotion.

---

## Evidence ledger

| Evidence | Status | Supports | Limits |
|---|---|---|---|
| Previous target file | CONFIRMED | `tests/domains/habitat/land_cover/crosswalk/README.md` existed as a blank placeholder before this replacement. | Did not define the lane. |
| `tests/README.md` | CONFIRMED | `tests/` is enforceability proof; domain-specific tests belong under `tests/domains/<domain>/`; default tests should avoid sensitive data and live network calls. | Does not prove habitat/land_cover/crosswalk modules or pass rate. |
| `contracts/domains/habitat/land_cover/crosswalk.md` | CONFIRMED semantic contract / PROPOSED implementation | Defines `CoverClassCrosswalk` as a reviewed, versioned, citable mapping between two `ClassSchemeProfile` records so observations, summaries, layers, and downstream Habitat products never rely on silent recodes. | Paired schema is a permissive scaffold; field-level enforcement remains NEEDS VERIFICATION. |
| `fixtures/domains/habitat/land_cover/crosswalk/README.md` | CONFIRMED | Fixture lane is synthetic and not source records, lifecycle data, EvidenceBundles, source descriptors, review approvals, release state, public API/map/tile material, Habitat truth, or published artifacts. | Does not prove payload inventory or consumer tests. |
| `docs/domains/habitat/sublanes/land_cover.md` | CONFIRMED doctrine / PROPOSED implementation | Land-cover sublane treats source classifications as interpretive infrastructure, not habitat assertions, and requires governed joins rather than direct file reach-around. | Specific implementation paths and sublane structure remain PROPOSED. |
| Adjacent class-scheme and change-summary lanes | CONFIRMED by fetched files / repo search | Crosswalk fixtures depend on class-scheme fixtures, and change-summary fixtures may cite crosswalk fixtures. | Contents and enforcement remain NEEDS VERIFICATION unless inspected. |

---

## Validation checklist

Before treating this README as implemented behavior, verify:

- [ ] Executable test modules exist under this lane.
- [ ] Test runner and import paths match the repo's accepted convention.
- [ ] Synthetic fixtures exist for valid crosswalk, missing source scheme, missing target scheme, missing directionality, reverse mapping without review, many-to-one marked lossless, unmapped class dropped, crosswalk-as-scheme, crosswalk-as-observation, crosswalk-as-renderer, and missing release/correction/rollback posture.
- [ ] Crosswalk schema path and field expectations are accepted beyond scaffold status.
- [ ] ClassSchemeProfile, LandCoverObservation, LandCoverChangeSummary, uncertainty, and source-registry expectations are accepted before enforcing them.
- [ ] SourceDescriptor/source-role behavior is available to tests or safely stubbed.
- [ ] EvidenceRef / EvidenceBundle resolver behavior is available to tests or safely stubbed.
- [ ] PolicyDecision and sensitivity behavior are available to tests or safely stubbed.
- [ ] ReleaseManifest, CorrectionNotice, and RollbackCard expectations are defined before enforcing them.
- [ ] CI runs the no-network Habitat land-cover crosswalk suite.
- [ ] Failures block public carrier promotion or release candidate approval.

---

## Rollback

Rollback is required if this lane becomes a source legend store, source raster store, lifecycle data store, fixture root, semantic-contract root, schema authority, crosswalk authority, threshold-policy authority, source registry, proof store, receipt store, release-decision root, public map/API/tile surface, AI surface, renderer transform authority, or publication shortcut.

Rollback target for this replacement: previous blank blob SHA `8b137891791fe96927ad78e64b0aad7bded08bdc`.

<p align="right"><a href="#top">Back to top</a></p>
