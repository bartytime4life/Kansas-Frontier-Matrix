<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-domains-habitat-land-cover-change-summary-readme
title: Habitat Land-Cover Change-Summary Test README
type: test-readme
version: v0.1
status: draft; placeholder-expanded; test-lane; PROPOSED / NEEDS VERIFICATION before promotion
owners:
  - OWNER_TBD — Habitat domain steward
  - OWNER_TBD — Land-cover steward
  - OWNER_TBD — Source steward
  - OWNER_TBD — Evidence steward
  - OWNER_TBD — Schema steward
  - OWNER_TBD — Policy steward
  - OWNER_TBD — Validation steward
  - OWNER_TBD — Release steward
  - OWNER_TBD — QA steward
created: NEEDS VERIFICATION — blank placeholder existed before v0.1 expansion
updated: 2026-07-05
policy_label: public-doc; tests; habitat; land-cover; change-summary; no-network; source-vintage-aware; threshold-governed; evidence-bound; release-gated; public-safe-derivative
tags: [kfm, tests, habitat, land_cover, change_summary, LandCoverChangeSummary, LandCoverObservation, source-vintage, threshold-profile, class-scheme, crosswalk, valid-pixel-footprint, EvidenceRef, EvidenceBundle, PolicyDecision, ReleaseManifest, CorrectionNotice, RollbackCard, ABSTAIN, DENY]
related:
  - ../../../../README.md
  - ../../../../../contracts/domains/habitat/land_cover/change_summary.md
  - ../../../../../schemas/contracts/v1/domains/habitat/land_cover/change_summary.schema.json
  - ../../../../../fixtures/domains/habitat/land_cover/change_summary/README.md
  - ../../../../../docs/domains/habitat/sublanes/land_cover.md
  - ../../../../../docs/domains/habitat/MODEL_VS_OBSERVATION.md
  - ../../../../../docs/domains/habitat/SOURCE_FAMILIES.md
  - ../../../../../docs/domains/habitat/API_CONTRACTS.md
  - ../../../../../contracts/domains/habitat/land_cover/observation.md
  - ../../../../../contracts/domains/habitat/land_cover/crosswalk.md
  - ../../../../../contracts/domains/habitat/land_cover/uncertainty.md
  - ../../../../../contracts/domains/habitat/land_cover/model_run_receipt.md
  - ../../../../../pipelines/domains/habitat/land_cover/
  - ../../../../../pipeline_specs/habitat/land_cover/
  - ../../../../../policy/domains/habitat/land_cover/
  - ../../../../../policy/sensitivity/habitat/
  - ../../../../../data/registry/sources/habitat/
  - ../../../../../data/published/layers/habitat/land_cover/README.md
  - ../../../../../release/manifests/habitat/
notes:
  - "This file replaces a blank placeholder at tests/domains/habitat/land_cover/change_summary/README.md."
  - "This is a test-lane README only. It does not define Habitat land-cover doctrine, semantic contracts, schemas, threshold policy, source descriptors, fixtures, lifecycle records, evidence bundles, receipts, proofs, release decisions, production code, public layers, or published artifacts."
  - "The tested invariant is that LandCoverChangeSummary is a public-safe derived summary comparing two governed LandCoverObservation records over a declared analysis unit; it must not become a source raster, source observation, habitat-quality proof, occurrence proof, regulatory designation, policy decision, release manifest, public layer, or AI answer."
  - "The default posture is deterministic and no-network. Live source checks, credentials, real source rasters, real sensitive occurrence joins, and public tiles do not belong in this lane."
  - "Rollback target for this replacement is previous blank blob SHA 8b137891791fe96927ad78e64b0aad7bded08bdc."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Habitat land-cover change-summary tests

> Deterministic, no-network test documentation for proving that Habitat `LandCoverChangeSummary` outputs remain public-safe derived summaries, preserve observation-pair/source-vintage/class-scheme/threshold/evidence boundaries, and fail closed when change summaries are misused as source rasters, observations, habitat-quality proof, occurrence proof, regulatory truth, release truth, or AI truth.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: tests" src="https://img.shields.io/badge/root-tests%2F-blue">
  <img alt="Domain: habitat" src="https://img.shields.io/badge/domain-habitat-2e7d32">
  <img alt="Sublane: land cover" src="https://img.shields.io/badge/sublane-land__cover-6a5acd">
  <img alt="Object: LandCoverChangeSummary" src="https://img.shields.io/badge/object-LandCoverChangeSummary-blue">
  <img alt="Network: disabled by default" src="https://img.shields.io/badge/network-disabled__by__default-critical">
  <img alt="Boundary: summary not source raster" src="https://img.shields.io/badge/boundary-summary__not__source__raster-success">
</p>

**Path:** `tests/domains/habitat/land_cover/change_summary/README.md`  
**Status:** draft / placeholder-expanded / PROPOSED until paired test files are verified  
**Owning root:** `tests/`  
**Domain segment:** `habitat`  
**Test lane:** `land_cover/change_summary`  
**Default execution posture:** deterministic, synthetic, no-network, public-safe fixtures only  
**Truth posture:** CONFIRMED target was a blank placeholder before this expansion · CONFIRMED `tests/` is the canonical root for enforceability proof · CONFIRMED `LandCoverChangeSummary` is defined as a public-safe summary of change between two `LandCoverObservation` records over an analysis unit · CONFIRMED the paired fixture README says fixtures are examples only, not source rasters, lifecycle data, EvidenceBundles, policy decisions, release state, public API/map/tile material, habitat quality proof, occurrence proof, regulatory proof, or published artifacts · NEEDS VERIFICATION for executable test modules, fixture payload inventory, schema enforcement, threshold policy, validators, source registry records, imports, CI coverage, and release-gate integration.

**Quick jumps:** [Purpose](#purpose) · [Placement basis](#placement-basis) · [Invariant under test](#invariant-under-test) · [Expected test scope](#expected-test-scope) · [Fixture posture](#fixture-posture) · [Assertions](#assertions) · [Finite outcomes](#finite-outcomes) · [Forbidden shortcuts](#forbidden-shortcuts) · [Suggested test layout](#suggested-test-layout) · [Run posture](#run-posture) · [Evidence ledger](#evidence-ledger) · [Validation checklist](#validation-checklist) · [Rollback](#rollback)

---

## Purpose

`tests/domains/habitat/land_cover/change_summary/` is the intended home for tests that prove Habitat land-cover change summaries stay within their governed meaning.

This lane should test that a `LandCoverChangeSummary` cannot silently become:

- a source raster;
- a `LandCoverObservation`;
- a class-scheme crosswalk;
- a threshold policy;
- a HabitatPatch or habitat-quality claim;
- a species or plant occurrence claim;
- a critical-habitat or regulatory designation;
- a public layer, tile, release manifest, or AI answer.

A passing test here should **not** mean that real land-cover change occurred, a public derivative is released, a threshold is scientifically final, or a downstream habitat claim is proven. It should mean only that change-summary guardrails behaved as expected against bounded fixtures.

---

## Placement basis

`tests/` is the canonical root for enforceability proof. Habitat appears as a lane segment inside the tests root, not as a repo-root domain folder.

| Responsibility | Correct home | This lane's relationship |
|---|---|---|
| Habitat land-cover change-summary tests | `tests/domains/habitat/land_cover/change_summary/` | This directory. |
| Synthetic change-summary fixtures | `fixtures/domains/habitat/land_cover/change_summary/` | Preferred toy inputs and expected outcomes. |
| Semantic change-summary contract | `contracts/domains/habitat/land_cover/change_summary.md` | Defines meaning; tests do not redefine it. |
| Machine schema | `schemas/contracts/v1/domains/habitat/land_cover/change_summary.schema.json` | Referenced by tests; current scaffold maturity must be respected. |
| Land-cover doctrine | `docs/domains/habitat/sublanes/land_cover.md` | Referenced doctrine; not test implementation. |
| Source registry | `data/registry/sources/habitat/` | Source identity, source role, rights, cadence, caveats, and activation state. |
| Threshold / policy homes | `policy/domains/habitat/land_cover/`, `policy/sensitivity/habitat/` | Referenced by tests, not bypassed here. |
| Pipeline logic and specs | `pipelines/domains/habitat/land_cover/`, `pipeline_specs/habitat/land_cover/` | Systems under test where accepted; not duplicated here. |
| Published layers | `data/published/layers/habitat/land_cover/` | Released artifacts only after governed promotion. |
| Release decisions | `release/` and `release/manifests/habitat/` | Publication, correction, and rollback authority; tests cannot replace it. |

---

## Invariant under test

> **Change summary is derived context, not source truth.** `LandCoverChangeSummary` compares two governed `LandCoverObservation` records over a declared analysis unit using explicit source vintages, class-scheme/crosswalk posture, valid-pixel support, threshold profile, evidence closure, policy/review state, release state, correction path, and rollback target.

For this test lane, the invariant decomposes into ten checks:

| Check | Required behavior | Failure outcome |
|---|---|---|
| Observation pair | Baseline and comparison observations are explicit, distinct, reviewed `LandCoverObservation` references. | validation failure / `ERROR`. |
| Source vintage | Source, observed/valid, retrieval, release, and correction times remain distinct. | validation failure / `ABSTAIN`. |
| Class scheme | Same-scheme comparison or reviewed crosswalk is explicit; no silent recode. | validation failure / `ABSTAIN`. |
| Analysis unit | County, HUC, ecoregion, grid, project area, or accepted unit has geometry/version support. | validation failure. |
| Valid pixels | Nodata, masks, footprint gaps, source extent, and comparable area are accounted for. | validation failure / quality flag. |
| Threshold profile | Versioned materiality threshold and pass/warn/fail state are explicit. | validation failure / review required. |
| Evidence closure | Claim-bearing outputs resolve `EvidenceRef -> EvidenceBundle` or produce a finite non-answer. | `ABSTAIN`. |
| Public-safe derivative | Public carriers carry aggregate/generalized summary posture and no sensitive leakage. | `DENY` / `RESTRICT`. |
| Release/correction/rollback | Public use requires review, policy, release, correction, and rollback linkage where material. | promotion-blocking failure. |
| No truth upgrade | Summary cannot become raster truth, observation truth, habitat quality, occurrence truth, regulatory truth, public-layer truth, or AI truth. | `DENY` / `ABSTAIN`. |

---

## Expected test scope

Tests in this lane should be small, synthetic, and deterministic. They may validate:

- required observation-pair references and rejection of missing baseline/comparison observations;
- source-vintage separation across baseline, comparison, retrieval, release, and correction times;
- class-scheme compatibility and rejection of unreviewed crosswalks;
- threshold-profile presence, versioning, and materiality pass/warn/fail behavior;
- valid-pixel footprint and comparable-area requirements;
- public-safe aggregate/summary posture for map/API/Evidence Drawer/Focus Mode examples;
- non-answer behavior when evidence, source rights, policy, review, release, correction, or rollback context is unresolved;
- denial when change summaries are presented as source rasters, observations, habitat quality, species/plant occurrence, regulatory truth, hydrology/soil/hazards/land truth, or public release authority.

Live source rasters, live source downloads, public tile generation, real sensitive occurrence joins, and provider credentials are out of scope for the default suite.

---

## Fixture posture

Use `fixtures/domains/habitat/land_cover/change_summary/` when possible.

Fixture requirements:

- synthetic and public-safe;
- deterministic and no-network;
- compact enough for review in a PR;
- explicit expected outcome;
- explicit baseline and comparison observation IDs;
- explicit source vintages, class-scheme/crosswalk posture, analysis-unit geometry/version, valid-pixel posture, threshold profile, and change values where material;
- explicit evidence, source role, source rights, policy, review, release, correction, and rollback state where material;
- no real source rasters, real sensitive occurrence records, rare-species/rare-plant locations, owner/land detail, public tiles, or release artifacts.

Preferred fixture families:

| Fixture kind | Preferred lane | Example expected outcome |
|---|---|---|
| Valid toy change summary | `fixtures/domains/habitat/land_cover/change_summary/` | accepted as public-safe derived summary. |
| Missing observation pair | same | validation failure / `ERROR`. |
| Source vintage collapse | same or invalid lane | `ABSTAIN` / validation failure. |
| Class-scheme mismatch without crosswalk | same or invalid lane | `ABSTAIN` / validation failure. |
| Missing valid-pixel footprint | same or invalid lane | validation failure / quality flag. |
| Missing threshold profile | same or invalid lane | validation failure / review required. |
| Summary treated as raster/observation | same or invalid lane | `ABSTAIN` / validation failure. |
| Summary treated as habitat quality or occurrence proof | same or invalid lane | `ABSTAIN`. |
| Public derivative missing release/correction/rollback | same or invalid lane | promotion block / review required. |

---

## Assertions

A useful land-cover change-summary test should make the derived-summary boundary obvious.

### Positive path

- observation pair is explicit and reviewed;
- source vintage and temporal scope are preserved;
- class scheme or crosswalk posture is explicit;
- valid-pixel and analysis-unit support are explicit;
- threshold profile and materiality state are versioned;
- evidence, policy, review, release, correction, and rollback context are linkable where material;
- public-facing examples remain aggregate/summary carriers, not source truth.

### Negative path

- missing baseline or comparison observation fails closed;
- collapsed source vintages or temporal fields fail closed;
- different class schemes without a reviewed crosswalk fail closed;
- summary cannot replace source raster, source observation, threshold policy, or class-scheme contract;
- summary cannot prove habitat quality, species occurrence, plant occurrence, critical habitat, hydrology truth, soil truth, hazards truth, agriculture truth, or land/title truth;
- public layer, chart, popup, tile, graph edge, or AI answer cannot become root evidence or release authority.

---

## Finite outcomes

This lane should prefer explicit finite outcomes over loose pass/fail text.

| Condition | Expected outcome |
|---|---|
| Valid synthetic summary with observation pair, class scheme/crosswalk, threshold, evidence, policy, review, release, correction, and rollback context | allowed downstream carrier / `ANSWER` only if citation-closed. |
| Missing baseline or comparison observation | validation failure / `ERROR`. |
| Source-vintage or temporal collapse | `ABSTAIN` / validation failure. |
| Class-scheme mismatch without reviewed crosswalk | `ABSTAIN` / validation failure. |
| Missing threshold profile or valid-pixel support | validation failure / review required. |
| Summary used as source raster or LandCoverObservation | `ABSTAIN` / validation failure. |
| Summary used as habitat quality or occurrence proof | `ABSTAIN`. |
| Public derivative lacks release/correction/rollback | promotion-blocking failure. |
| Policy engine unavailable | `ERROR` or `ABSTAIN`, never public exposure. |

---

## Forbidden shortcuts

Do not use this test lane to:

- fetch live upstream source systems;
- store credentials or tokens;
- store real source rasters, real source exports, or lifecycle data;
- store real sensitive occurrence joins, rare-species/rare-plant locations, owner/land data, or exact protected-resource geometry;
- store public PMTiles, MVT, COG, GeoParquet, release artifacts, or generated public layers;
- redefine Habitat land-cover doctrine, semantic contracts, schemas, threshold policy, source descriptors, fixtures, receipts, proofs, release decisions, or production code;
- bypass `EvidenceRef -> EvidenceBundle` resolution;
- bypass source-vintage, class-scheme, threshold, policy, sensitivity, correction, or rollback checks with a fixture flag;
- infer release state from file existence, layer name, chart, map rendering, tile availability, or AI wording;
- publish, promote, or release anything.

Any test that needs real source rasters or public tile output belongs in a gated integration tier with source admission, lifecycle state, policy, receipts, release controls, and rollback targets.

---

## Suggested test layout

The exact Python module names remain NEEDS VERIFICATION until the runner and existing test conventions are inspected. A minimal future layout could be:

```text
tests/domains/habitat/land_cover/change_summary/
├── README.md
├── test_observation_pair_required.py       # baseline/comparison LandCoverObservation refs required
├── test_source_vintage_discipline.py       # source/valid/retrieval/release/correction times stay distinct
├── test_class_scheme_crosswalk.py          # no silent recode across class schemes
├── test_threshold_and_valid_pixels.py      # threshold profile and valid-pixel support required
├── test_summary_not_truth.py               # summary cannot become raster/observation/habitat/occurrence truth
└── test_release_correction_rollback.py     # public derivative requires release/correction/rollback context
```

Keep helpers local only when they are test-specific. Shared contracts, schemas, threshold policy, source registries, evidence resolvers, fixtures, pipeline behavior, or release behavior belong under their accepted responsibility roots.

---

## Run posture

Default run expectations:

```bash
pytest tests/domains/habitat/land_cover/change_summary
```

Status of the command above: **PROPOSED / NEEDS VERIFICATION**. It assumes `pytest` is the accepted test runner and that executable test modules exist. This README does not claim the command currently passes.

Expected CI posture:

- default suite: no-network, synthetic fixtures only;
- fail closed on missing observation pair, source-vintage collapse, class-scheme mismatch, missing crosswalk, missing threshold, missing valid-pixel support, unresolved evidence, missing policy, sensitive leakage, or missing release/correction/rollback posture;
- live-source or tile-generation checks: separate gated jobs only;
- release gate: land-cover change-summary failures should block public catalog/API/map/tile/AI carrier promotion.

---

## Evidence ledger

| Evidence | Status | Supports | Limits |
|---|---|---|---|
| Previous target file | CONFIRMED | `tests/domains/habitat/land_cover/change_summary/README.md` existed as a blank placeholder before this replacement. | Did not define the lane. |
| `tests/README.md` | CONFIRMED | `tests/` is enforceability proof; domain-specific tests belong under `tests/domains/<domain>/`; default tests should avoid sensitive data and live network calls. | Does not prove habitat/land_cover/change_summary modules or pass rate. |
| `contracts/domains/habitat/land_cover/change_summary.md` | CONFIRMED semantic contract / PROPOSED implementation | Defines `LandCoverChangeSummary` as a public-safe summary comparing two governed `LandCoverObservation` records over an analysis unit; excludes source rasters, observations, habitat quality, occurrence proof, policy, release, and public-layer authority. | Paired schema is a permissive scaffold; field-level enforcement remains NEEDS VERIFICATION. |
| `fixtures/domains/habitat/land_cover/change_summary/README.md` | CONFIRMED | Fixture lane is synthetic/public-safe and not source rasters, lifecycle data, EvidenceBundles, policy decisions, release state, public API/map/tile material, habitat quality proof, occurrence proof, regulatory proof, or published artifacts. | Does not prove payload inventory or consumer tests. |
| `docs/domains/habitat/sublanes/land_cover.md` | CONFIRMED doctrine / PROPOSED implementation | Land-cover sublane owns `LandCoverObservation`, emits validation reports/run receipts/public-safe candidates, and treats source classifications as interpretive infrastructure rather than habitat assertions. | Specific implementation paths and sublane structure remain PROPOSED. |
| Search results for schema and adjacent contracts | CONFIRMED by repo search | Paired schema and related land-cover observation/crosswalk/uncertainty/model-run receipt contract paths exist. | Contents and enforcement remain NEEDS VERIFICATION unless inspected. |

---

## Validation checklist

Before treating this README as implemented behavior, verify:

- [ ] Executable test modules exist under this lane.
- [ ] Test runner and import paths match the repo's accepted convention.
- [ ] Synthetic fixtures exist for valid summary, missing observation pair, source-vintage collapse, class-scheme mismatch, missing crosswalk, missing threshold profile, missing valid-pixel footprint, summary-as-raster, summary-as-observation, summary-as-habitat-quality, summary-as-occurrence-proof, and missing release/correction/rollback posture.
- [ ] Change-summary schema path and field expectations are accepted beyond scaffold status.
- [ ] LandCoverObservation, crosswalk, uncertainty, model-run receipt, and threshold-policy expectations are accepted before enforcing them.
- [ ] SourceDescriptor/source-role behavior is available to tests or safely stubbed.
- [ ] EvidenceRef / EvidenceBundle resolver behavior is available to tests or safely stubbed.
- [ ] PolicyDecision and sensitivity behavior are available to tests or safely stubbed.
- [ ] ReleaseManifest, CorrectionNotice, and RollbackCard expectations are defined before enforcing them.
- [ ] CI runs the no-network Habitat land-cover change-summary suite.
- [ ] Failures block public carrier promotion or release candidate approval.

---

## Rollback

Rollback is required if this lane becomes a source raster store, lifecycle data store, fixture root, semantic-contract root, schema authority, threshold-policy authority, source registry, proof store, receipt store, release-decision root, public map/API/tile surface, AI surface, or publication shortcut.

Rollback target for this replacement: previous blank blob SHA `8b137891791fe96927ad78e64b0aad7bded08bdc`.

<p align="right"><a href="#top">Back to top</a></p>
