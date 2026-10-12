<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-domains-habitat-land-cover-readme
title: Habitat Land-Cover Tests README
type: test-readme
version: v0.1
status: draft; placeholder-expanded; parent-test-lane; PROPOSED / NEEDS VERIFICATION before promotion
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
policy_label: public-doc; tests; habitat; land-cover; parent-lane; no-network; evidence-bound; policy-aware; release-gated; public-safe-derivative; watcher-not-publisher
tags: [kfm, tests, habitat, land_cover, LandCoverObservation, ClassSchemeProfile, CoverClassCrosswalk, LandCoverChangeSummary, ModelRunReceipt, LayerManifest, UncertaintySurface, watcher, EvidenceRef, EvidenceBundle, PolicyDecision, ReleaseManifest, CorrectionNotice, RollbackCard, ABSTAIN, DENY]
related:
  - ../../../README.md
  - ../README.md
  - ./observation/README.md
  - ./class_scheme/README.md
  - ./crosswalk/README.md
  - ./change_summary/README.md
  - ./model_run/README.md
  - ./uncertainty/README.md
  - ./layer_manifest/README.md
  - ./watcher/README.md
  - ../../../../docs/domains/habitat/sublanes/land_cover.md
  - ../../../../fixtures/domains/habitat/land_cover/
  - ../../../../contracts/domains/habitat/land_cover/
  - ../../../../schemas/contracts/v1/domains/habitat/land_cover/
  - ../../../../pipelines/domains/habitat/land_cover/
  - ../../../../pipeline_specs/habitat/land_cover/
  - ../../../../policy/domains/habitat/land_cover/
  - ../../../../policy/sensitivity/habitat/
  - ../../../../data/registry/sources/habitat/
  - ../../../../data/processed/habitat/land_cover/
  - ../../../../data/published/layers/habitat/land_cover/
  - ../../../../release/manifests/habitat/
notes:
  - "This file replaces a blank placeholder at tests/domains/habitat/land_cover/README.md."
  - "This is a parent test-lane README only. It does not define Habitat land-cover doctrine, contracts, schemas, fixtures, source descriptors, lifecycle records, evidence bundles, receipts, proofs, policy rules, release decisions, pipeline code, public API material, public map material, public tiles, or published artifacts."
  - "The tested parent invariant is that land-cover test lanes prove boundary discipline across observations, class schemes, crosswalks, change summaries, model runs, uncertainty, layer manifests, and watchers without turning source classifications, tiles, watchers, fixtures, or generated text into Habitat truth."
  - "Default posture is deterministic and no-network. Live source checks, real source exports, lifecycle data, public tiles, and sensitive joined records do not belong in this parent lane."
  - "Rollback target for this replacement is previous blank blob SHA 8b137891791fe96927ad78e64b0aad7bded08bdc."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Habitat land-cover tests

> Parent test-lane README for Habitat land-cover enforceability checks. This lane proves that land-cover source classifications become governed evidence and public-safe derivatives only through evidence, policy, validation, review, release, correction, and rollback gates.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: tests" src="https://img.shields.io/badge/root-tests%2F-blue">
  <img alt="Domain: habitat" src="https://img.shields.io/badge/domain-habitat-2e7d32">
  <img alt="Sublane: land cover" src="https://img.shields.io/badge/sublane-land__cover-6a5acd">
  <img alt="Network: disabled by default" src="https://img.shields.io/badge/network-disabled__by__default-critical">
  <img alt="Boundary: evidence not truth root" src="https://img.shields.io/badge/boundary-evidence__not__truth__root-success">
</p>

**Path:** `tests/domains/habitat/land_cover/README.md`  
**Status:** draft / placeholder-expanded / parent test lane / PROPOSED until executable tests are verified  
**Owning root:** `tests/`  
**Domain segment:** `habitat`  
**Sublane segment:** `land_cover`  
**Default execution posture:** deterministic, synthetic, no-network, public-safe fixtures only  
**Truth posture:** CONFIRMED target was a blank placeholder before this expansion · CONFIRMED `tests/` is the canonical root for enforceability proof · CONFIRMED Habitat land-cover doctrine treats land-cover as interpretive infrastructure, not a truth root · CONFIRMED the land-cover docs name `tests/domains/habitat/land_cover/` as the proposed tests home · NEEDS VERIFICATION for executable test modules, fixture payload inventory, schema enforcement, validators, source activation records, policy runtime, pipeline integration, CI coverage, and pass rates.

**Quick jumps:** [Purpose](#purpose) · [Placement basis](#placement-basis) · [Child test lanes](#child-test-lanes) · [Parent invariant](#parent-invariant) · [Expected scope](#expected-scope) · [Fixture posture](#fixture-posture) · [Finite outcomes](#finite-outcomes) · [Forbidden shortcuts](#forbidden-shortcuts) · [Suggested layout](#suggested-layout) · [Run posture](#run-posture) · [Evidence ledger](#evidence-ledger) · [Validation checklist](#validation-checklist) · [Rollback](#rollback)

---

## Purpose

`tests/domains/habitat/land_cover/` is the parent lane for Habitat land-cover tests.

The lane exists to prove that land-cover source material and land-cover-derived products do not cross KFM trust boundaries. In particular, tests here should show that land-cover source classifications, class schemes, crosswalks, observations, summaries, receipts, uncertainty records, layer manifests, and watcher outputs remain separate from one another and from proof, policy, release, public UI, and AI-generated language.

A passing suite here should **not** mean that a real source is activated, a real source record is admitted, a real raster is processed, a public layer is released, or a habitat claim is proven. It should mean only that the land-cover trust-spine checks behaved as expected against bounded fixtures.

---

## Placement basis

`tests/` is the canonical root for enforceability proof. Habitat is a domain segment inside that root. `land_cover` is a sublane segment under the Habitat test lane, not a repo-root domain folder and not a parallel authority root.

| Responsibility | Correct home | This lane's relationship |
|---|---|---|
| Parent land-cover tests | `tests/domains/habitat/land_cover/` | This directory. |
| Domain parent tests | `tests/domains/habitat/` | Parent domain test lane; currently a greenfield stub when last inspected. |
| Synthetic land-cover fixtures | `fixtures/domains/habitat/land_cover/` | Preferred toy inputs and expected outputs. |
| Land-cover doctrine | `docs/domains/habitat/sublanes/land_cover.md` | Referenced doctrine; tests do not redefine it. |
| Semantic contracts | `contracts/domains/habitat/land_cover/` | Object meanings under test. |
| Machine schemas | `schemas/contracts/v1/domains/habitat/land_cover/` | Shape checks where accepted. |
| Policy gates | `policy/domains/habitat/land_cover/`, `policy/sensitivity/habitat/` | Policy behavior under test; not owned here. |
| Pipelines and specs | `pipelines/domains/habitat/land_cover/`, `pipeline_specs/habitat/land_cover/` | Executable behavior and declarative run specs under test. |
| Source registry | `data/registry/sources/habitat/` | Source identity, role, rights, cadence, and activation. |
| Lifecycle and publication | `data/raw|work|quarantine|processed|published/...`, `release/` | Tested boundaries only; not owned here. |

---

## Child test lanes

| Child lane | Intended responsibility | Boundary to preserve |
|---|---|---|
| [`observation/`](./observation/README.md) | `LandCoverObservation` checks for source role, class scheme, source vintage, spatial/temporal scope, valid-pixel support, evidence, correction, and rollback. | Observation is not class scheme, crosswalk, change summary, receipt, release authority, public layer, or AI/UI truth. |
| [`class_scheme/`](./class_scheme/README.md) | `ClassSchemeProfile` checks for classification vocabulary identity, versioning, class inventory, nodata/unknown handling, and source-role posture. | Scheme is not observation, crosswalk, source raster, habitat quality, release approval, or AI answer. |
| [`crosswalk/`](./crosswalk/README.md) | `CoverClassCrosswalk` checks for reviewed, versioned, citable mapping between class schemes. | Crosswalk is not a silent renderer/notebook recode and not observation, scheme, release, public-layer, or truth authority. |
| [`change_summary/`](./change_summary/README.md) | `LandCoverChangeSummary` checks for governed comparison of two observations over an analysis unit. | Summary is not source raster, source observation, habitat quality, occurrence proof, policy, release, public layer, or AI answer. |
| [`model_run/`](./model_run/README.md) | Model-run and receipt checks for input closure, config closure, output inventory, validation posture, and receipt-not-proof separation. | Receipt is process memory, not proof, policy, release, observed product, or public layer approval. |
| [`uncertainty/`](./uncertainty/README.md) | `UncertaintySurface` checks for accuracy, confidence, valid-pixel, nodata, source-vintage, crosswalk, model, geometry, and display caveats. | Uncertainty is inspectable context, not observation truth, proof, policy, release, public layer truth, or AI/UI evidence. |
| [`layer_manifest/`](./layer_manifest/README.md) | Layer-manifest and descriptor checks for layer identity, artifact integrity, source-role badges, evidence posture, freshness, correction, supersession, and rollback. | Manifest/descriptor is not raw data, renderer implementation, proof closure, policy approval, release approval, tile truth, or AI truth. |
| [`watcher/`](./watcher/README.md) | Watcher checks for source-head comparison, checkpoints, materiality thresholds, no-op/proposed-work outcomes, and review gates. | Watcher observes and records; watcher does not activate sources, publish, approve release, or feed public UI directly. |

---

## Parent invariant

> **Land-cover is interpretive infrastructure, not a truth root.** Habitat land-cover tests must prove that source classifications, observations, derived summaries, receipts, uncertainty records, layer carriers, and watcher outputs remain evidence-bound, source-role-aware, policy-aware, reviewable, release-gated, correction-aware, and rollback-ready.

This parent lane should protect these system-level boundaries:

1. `RAW -> WORK/QUARANTINE -> PROCESSED -> CATALOG/TRIPLET -> PUBLISHED` remains intact.
2. Public clients never read RAW, WORK, QUARANTINE, candidate, watcher, fixture, or unpublished internal state.
3. `EvidenceRef -> EvidenceBundle` resolution is required for consequential claims.
4. Policy and sensitivity checks fail closed where material.
5. Review, release, correction, and rollback remain governed state transitions.
6. Source roles and object families do not collapse.
7. Tiles, styles, popups, Focus Mode, Evidence Drawer, graph projections, and AI text are downstream carriers, not sovereign truth.

---

## Expected scope

This parent lane may contain:

- README and index material;
- shared no-network test helpers only when they are strictly local to this test lane;
- parent-level smoke tests that verify child-lane fixture discovery and boundary posture;
- tests that make sure child lanes do not import live sources, write lifecycle data, or bypass policy/release gates;
- run documentation for the whole land-cover test subtree.

Most object-specific assertions belong in the child lanes. Shared contracts, schemas, source registries, policies, pipelines, fixtures, receipts, proofs, release manifests, public map code, and public API code belong under their own responsibility roots.

---

## Fixture posture

Use `fixtures/domains/habitat/land_cover/` and its child lanes for synthetic examples.

Parent-level fixtures, if any, should be:

- synthetic and public-safe;
- deterministic and no-network;
- compact enough for review in a PR;
- explicit about expected finite outcome;
- free of real source exports, lifecycle data, public tiles, sensitive joined records, and published artifacts;
- paired to child-lane expected outputs where behavior is stable.

---

## Finite outcomes

| Condition | Expected outcome |
|---|---|
| Child lane passes with synthetic fixtures and no boundary violations | accepted test support only. |
| Live source or public tile access attempted in default suite | validation failure / `ERROR`. |
| Source role, object family, evidence, policy, review, or release boundary collapses | validation failure / `DENY` / `ABSTAIN` as appropriate. |
| Watcher output treated as publication | validation failure. |
| Layer manifest, tile, style, popup, or AI text treated as truth | validation failure / `ABSTAIN`. |
| Evidence missing for consequential claim | `ABSTAIN`. |
| Policy engine unavailable | `ERROR` or `ABSTAIN`, never public exposure. |
| Public-facing candidate lacks correction or rollback posture | promotion-blocking failure. |

---

## Forbidden shortcuts

Do not use this parent test lane to:

- fetch live upstream source systems;
- store real source exports, lifecycle data, real source records, processed artifacts, public tiles, or release artifacts;
- store proof packs, release manifests, source descriptors, policy decisions, or generated public layers;
- redefine Habitat land-cover doctrine, contracts, schemas, fixtures, policy rules, receipts, proofs, release decisions, renderer code, or production code;
- bypass source activation, source role, evidence, validation, policy, review, correction, or rollback checks with a fixture flag;
- infer release state from file existence, test success, watcher output, layer name, map rendering, tile availability, or AI wording;
- publish, promote, or release anything.

Any test that needs live source checking, real source rasters, or public tile output belongs in a gated integration tier with source admission, lifecycle state, policy, receipts, release controls, and rollback targets.

---

## Suggested layout

The child README files below have been documented as test lanes. Executable modules remain **NEEDS VERIFICATION** until inspected.

```text
tests/domains/habitat/land_cover/
├── README.md
├── observation/
├── class_scheme/
├── crosswalk/
├── change_summary/
├── model_run/
├── uncertainty/
├── layer_manifest/
└── watcher/
```

Potential parent-level tests, if needed:

```text
tests/domains/habitat/land_cover/
├── test_no_network_default.py
├── test_child_lane_boundaries.py
└── test_public_surface_blockers.py
```

---

## Run posture

```bash
pytest tests/domains/habitat/land_cover
```

Status of the command above: **PROPOSED / NEEDS VERIFICATION**. It assumes `pytest` is the accepted test runner and that executable test modules exist. This README does not claim the command currently passes.

---

## Evidence ledger

| Evidence | Status | Supports | Limits |
|---|---|---|---|
| Previous target file | CONFIRMED | `tests/domains/habitat/land_cover/README.md` existed as a blank placeholder before this replacement. | Did not define the parent lane. |
| `tests/README.md` | CONFIRMED | `tests/` is enforceability proof and should demonstrate source admission through release/correction/rollback without forbidden boundary crossings. | Does not prove this lane's modules or pass rate. |
| `docs/domains/habitat/sublanes/land_cover.md` | CONFIRMED doctrine / PROPOSED implementation | Land-cover is interpretive infrastructure, not a truth root; it owns land-cover observations and public-safe derivatives through governed joins; specific implementation paths remain proposed. | Concrete runners, validators, CI, source activation, and pass rates remain NEEDS VERIFICATION. |
| Child test-lane READMEs | CONFIRMED by recent edits in this session | Observation, class-scheme, crosswalk, change-summary, model-run, uncertainty, layer-manifest, and watcher test-lane READMEs now exist as documentation. | Executable tests and fixture payloads remain NEEDS VERIFICATION. |
| `tests/domains/habitat/README.md` | CONFIRMED greenfield stub when last inspected | Domain parent exists but is not yet expanded. | Parent domain test policy/index remains incomplete. |

---

## Validation checklist

Before treating this README as implemented behavior, verify:

- [ ] Executable child test modules exist under the documented child lanes.
- [ ] Parent-level test modules exist only where useful and do not duplicate child-lane assertions.
- [ ] Test runner and import paths match the repo's accepted convention.
- [ ] Synthetic fixtures exist and are referenced from the correct fixture lanes.
- [ ] Schema paths and field expectations are accepted beyond scaffold status.
- [ ] SourceDescriptor/source-role behavior is available to tests or safely stubbed.
- [ ] EvidenceRef / EvidenceBundle behavior is available to tests or safely stubbed.
- [ ] PolicyDecision, ReviewRecord, ReleaseManifest, CorrectionNotice, and RollbackCard expectations are defined before enforcing them.
- [ ] CI runs the no-network Habitat land-cover test suite.
- [ ] Failures block public carrier promotion or release candidate approval.

---

## Rollback

Rollback is required if this parent lane becomes a live source-fetcher, source export store, lifecycle data store, fixture root, source registry, contract root, schema authority, policy authority, proof store, release-decision root, public map/API/tile surface, AI surface, renderer implementation, pipeline implementation, or publication shortcut.

Rollback target for this replacement: previous blank blob SHA `8b137891791fe96927ad78e64b0aad7bded08bdc`.

<p align="right"><a href="#top">Back to top</a></p>
