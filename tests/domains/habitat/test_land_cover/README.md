<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-domains-habitat-test-land-cover-readme
title: Habitat Land-Cover Aggregate Test README
type: test-readme
version: v0.1
status: draft; placeholder-expanded; compatibility-test-lane; PROPOSED / NEEDS VERIFICATION before promotion
owners:
  - OWNER_TBD — Habitat domain steward
  - OWNER_TBD — Land-cover steward
  - OWNER_TBD — Evidence steward
  - OWNER_TBD — Source steward
  - OWNER_TBD — Schema steward
  - OWNER_TBD — Policy steward
  - OWNER_TBD — Validation steward
  - OWNER_TBD — Release steward
  - OWNER_TBD — QA steward
created: NEEDS VERIFICATION — blank placeholder existed before v0.1 expansion
updated: 2026-07-05
policy_label: public-doc; tests; habitat; land-cover; aggregate-lane; compatibility-lane; no-network; evidence-bound; policy-aware; release-gated; anti-collapse
tags: [kfm, tests, habitat, land_cover, test_land_cover, compatibility-lane, aggregate-test, LandCoverObservation, ClassSchemeProfile, CoverClassCrosswalk, LandCoverChangeSummary, ModelRunReceipt, LayerManifest, UncertaintySurface, watcher, EvidenceBundle, PolicyDecision, ReleaseManifest, CorrectionNotice, RollbackCard, ABSTAIN, DENY]
related:
  - ../../../README.md
  - ../README.md
  - ../land_cover/README.md
  - ../land_cover/observation/README.md
  - ../land_cover/class_scheme/README.md
  - ../land_cover/crosswalk/README.md
  - ../land_cover/change_summary/README.md
  - ../land_cover/model_run/README.md
  - ../land_cover/uncertainty/README.md
  - ../land_cover/layer_manifest/README.md
  - ../land_cover/watcher/README.md
  - ../../../../docs/domains/habitat/sublanes/land_cover.md
  - ../../../../contracts/domains/habitat/land_cover/
  - ../../../../fixtures/domains/habitat/land_cover/
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
  - "This file replaces a blank placeholder at tests/domains/habitat/test_land_cover/README.md."
  - "This is an aggregate / compatibility test-lane README only. The detailed Habitat land-cover child test tree is tests/domains/habitat/land_cover/."
  - "This README does not define Habitat land-cover doctrine, contracts, schemas, fixtures, source descriptors, lifecycle records, evidence bundles, receipts, proofs, policy rules, release decisions, pipeline code, public API material, public map material, public tiles, or published artifacts."
  - "The tested invariant is that test_land_cover may coordinate or smoke-test Habitat land-cover boundary checks, but it must not become a parallel home for object-specific tests already assigned to observation, class_scheme, crosswalk, change_summary, model_run, uncertainty, layer_manifest, and watcher lanes."
  - "Default posture is deterministic and no-network. Live source checks, real source exports, lifecycle data, public tiles, and sensitive joined records do not belong in this lane."
  - "Rollback target for this replacement is previous blank blob SHA 8b137891791fe96927ad78e64b0aad7bded08bdc."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Habitat land-cover aggregate tests

> Compatibility and aggregate test-lane README for Habitat land-cover checks. This lane may coordinate high-level smoke tests, but the authoritative child test documentation lives under [`tests/domains/habitat/land_cover/`](../land_cover/README.md).

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: tests" src="https://img.shields.io/badge/root-tests%2F-blue">
  <img alt="Domain: habitat" src="https://img.shields.io/badge/domain-habitat-2e7d32">
  <img alt="Lane: test land cover" src="https://img.shields.io/badge/lane-test__land__cover-blue">
  <img alt="Network: disabled by default" src="https://img.shields.io/badge/network-disabled__by__default-critical">
  <img alt="Boundary: aggregate not authority" src="https://img.shields.io/badge/boundary-aggregate__not__authority-success">
</p>

**Path:** `tests/domains/habitat/test_land_cover/README.md`  
**Status:** draft / placeholder-expanded / compatibility test lane / PROPOSED until executable tests are verified  
**Owning root:** `tests/`  
**Domain segment:** `habitat`  
**Test lane:** `test_land_cover`  
**Canonical detailed lane:** `tests/domains/habitat/land_cover/`  
**Default execution posture:** deterministic, synthetic, no-network, public-safe fixtures only  
**Truth posture:** CONFIRMED target was a blank placeholder before this expansion · CONFIRMED `tests/` is the canonical root for enforceability proof · CONFIRMED the detailed Habitat land-cover child-lane README exists under `tests/domains/habitat/land_cover/` and names observation, class_scheme, crosswalk, change_summary, model_run, uncertainty, layer_manifest, and watcher lanes · CONFIRMED the parent land-cover invariant says land-cover is interpretive infrastructure, not a truth root · NEEDS VERIFICATION for executable test modules, fixture payload inventory, schema enforcement, validators, source activation records, policy runtime, pipeline integration, CI coverage, and pass rates.

**Quick jumps:** [Purpose](#purpose) · [Placement basis](#placement-basis) · [Relationship to child lanes](#relationship-to-child-lanes) · [Aggregate invariant](#aggregate-invariant) · [Expected scope](#expected-scope) · [Finite outcomes](#finite-outcomes) · [Forbidden shortcuts](#forbidden-shortcuts) · [Suggested layout](#suggested-layout) · [Run posture](#run-posture) · [Evidence ledger](#evidence-ledger) · [Validation checklist](#validation-checklist) · [Rollback](#rollback)

---

## Purpose

`tests/domains/habitat/test_land_cover/` is a compatibility and aggregate test lane for Habitat land-cover checks.

This lane should be used only when a test needs to verify cross-lane behavior across the full Habitat land-cover subtree. Object-specific assertions belong in the child lanes under `tests/domains/habitat/land_cover/`.

A passing test here should **not** mean that a real source is activated, a real source record is admitted, a real raster is processed, a public layer is released, or a habitat claim is proven. It should mean only that aggregate land-cover boundary checks behaved as expected against bounded fixtures.

---

## Placement basis

`tests/` is the canonical root for enforceability proof. Habitat is a domain segment inside that root. `test_land_cover` is a compatibility lane, not a new root and not a replacement for `tests/domains/habitat/land_cover/`.

| Responsibility | Correct home | This lane's relationship |
|---|---|---|
| Aggregate land-cover smoke tests | `tests/domains/habitat/test_land_cover/` | This directory. |
| Detailed land-cover tests | `tests/domains/habitat/land_cover/` | Canonical child test tree. |
| Synthetic land-cover fixtures | `fixtures/domains/habitat/land_cover/` | Preferred toy inputs and expected outputs. |
| Land-cover doctrine | `docs/domains/habitat/sublanes/land_cover.md` | Referenced doctrine; tests do not redefine it. |
| Semantic contracts | `contracts/domains/habitat/land_cover/` | Object meanings under test. |
| Machine schemas | `schemas/contracts/v1/domains/habitat/land_cover/` | Shape checks where accepted. |
| Policy gates | `policy/domains/habitat/land_cover/`, `policy/sensitivity/habitat/` | Policy behavior under test; not owned here. |
| Pipeline behavior | `pipelines/domains/habitat/land_cover/`, `pipeline_specs/habitat/land_cover/` | Executable behavior and specs under test where accepted. |
| Source registry | `data/registry/sources/habitat/` | Source identity, role, rights, cadence, and activation. |
| Lifecycle and release | `data/raw|work|quarantine|processed|published/...`, `release/` | Tested boundaries only; not owned here. |

---

## Relationship to child lanes

Use the child lanes for object-specific tests:

| Detailed lane | Owns checks for |
|---|---|
| [`land_cover/observation/`](../land_cover/observation/README.md) | `LandCoverObservation` identity, source role, class scheme, valid-pixel support, evidence, correction, and rollback. |
| [`land_cover/class_scheme/`](../land_cover/class_scheme/README.md) | `ClassSchemeProfile` vocabulary identity, versioning, class inventory, nodata/unknown handling, and role posture. |
| [`land_cover/crosswalk/`](../land_cover/crosswalk/README.md) | `CoverClassCrosswalk` directionality, lossiness, mapping coverage, and no-silent-recode behavior. |
| [`land_cover/change_summary/`](../land_cover/change_summary/README.md) | `LandCoverChangeSummary` comparison between governed observations. |
| [`land_cover/model_run/`](../land_cover/model_run/README.md) | Model-run receipts, input closure, config closure, output inventory, and receipt-not-proof checks. |
| [`land_cover/uncertainty/`](../land_cover/uncertainty/README.md) | `UncertaintySurface` support, caveats, valid-pixel context, confidence, and display obligations. |
| [`land_cover/layer_manifest/`](../land_cover/layer_manifest/README.md) | Layer identity, artifact integrity, source-role badges, freshness, correction, supersession, and rollback. |
| [`land_cover/watcher/`](../land_cover/watcher/README.md) | Source-head comparison, checkpoints, materiality thresholds, no-op/proposed-work, and watcher-not-publisher checks. |

This lane should not duplicate those assertions unless a parent-level smoke test is intentionally checking that the child lanes remain discoverable, no-network, and trust-boundary preserving.

---

## Aggregate invariant

> **Aggregate checks coordinate; they do not become authority.** `test_land_cover` may verify that land-cover tests run together and preserve the KFM trust spine, but it must not become a parallel semantic contract, schema, fixture, source registry, policy, lifecycle, release, proof, or public-serving home.

This lane should protect these system-level boundaries:

1. `RAW -> WORK/QUARANTINE -> PROCESSED -> CATALOG/TRIPLET -> PUBLISHED` remains intact.
2. Public clients never read RAW, WORK, QUARANTINE, candidate, watcher, fixture, or unpublished internal state.
3. `EvidenceRef -> EvidenceBundle` resolution is required for consequential claims.
4. Policy and sensitivity checks fail closed where material.
5. Review, release, correction, and rollback remain governed state transitions.
6. Source roles and object families do not collapse.
7. Tiles, styles, popups, Focus Mode, Evidence Drawer, graph projections, and AI text are downstream carriers, not sovereign truth.

---

## Expected scope

This compatibility lane may contain:

- aggregate smoke tests for child-lane discovery;
- no-network guard tests for the whole Habitat land-cover subtree;
- import-boundary checks that prevent default tests from fetching live sources or writing lifecycle artifacts;
- high-level checks that public-surface examples use released/gated carriers rather than fixtures, watchers, candidates, or internal records;
- run documentation for older or external references that expect a `test_land_cover` path.

Most object-level assertions belong under `tests/domains/habitat/land_cover/` child lanes.

---

## Finite outcomes

| Condition | Expected outcome |
|---|---|
| Child lanes are discoverable and remain no-network by default | accepted aggregate test support only. |
| Default suite attempts live source or public-tile access | validation failure / `ERROR`. |
| Source role, object family, evidence, policy, review, or release boundary collapses | validation failure / `DENY` / `ABSTAIN` as appropriate. |
| Watcher output treated as publication | validation failure. |
| Layer manifest, tile, style, popup, or AI text treated as truth | validation failure / `ABSTAIN`. |
| Evidence missing for consequential claim | `ABSTAIN`. |
| Policy engine unavailable | `ERROR` or `ABSTAIN`, never public exposure. |
| Public-facing candidate lacks correction or rollback posture | promotion-blocking failure. |

---

## Forbidden shortcuts

Do not use this compatibility lane to:

- replace `tests/domains/habitat/land_cover/` child lanes;
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

The exact test module names remain **NEEDS VERIFICATION** until the runner and existing conventions are inspected.

```text
tests/domains/habitat/test_land_cover/
├── README.md
├── test_child_lane_discovery.py
├── test_no_network_default.py
├── test_lifecycle_boundary.py
├── test_public_surface_blockers.py
└── test_release_correction_rollback.py
```

The canonical detailed tree remains:

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

---

## Run posture

```bash
pytest tests/domains/habitat/test_land_cover
```

For the detailed subtree:

```bash
pytest tests/domains/habitat/land_cover
```

Status of both commands above: **PROPOSED / NEEDS VERIFICATION**. They assume `pytest` is the accepted test runner and that executable test modules exist. This README does not claim either command currently passes.

---

## Evidence ledger

| Evidence | Status | Supports | Limits |
|---|---|---|---|
| Previous target file | CONFIRMED | `tests/domains/habitat/test_land_cover/README.md` existed as a blank placeholder before this replacement. | Did not define the lane. |
| `tests/README.md` | CONFIRMED | `tests/` is enforceability proof and failures should block promotion where trust-spine checks fail. | Does not prove this lane's modules or pass rate. |
| `tests/domains/habitat/land_cover/README.md` | CONFIRMED | The canonical detailed Habitat land-cover test tree is already documented with child lanes for observation, class_scheme, crosswalk, change_summary, model_run, uncertainty, layer_manifest, and watcher. | Executable tests and fixture payloads remain NEEDS VERIFICATION. |
| `docs/domains/habitat/sublanes/land_cover.md` | CONFIRMED doctrine / PROPOSED implementation | Land-cover is interpretive infrastructure, not a truth root; source classifications and derived products require governed joins and release gates. | Concrete validators, fixtures, CI, source activation, and pass rates remain NEEDS VERIFICATION. |

---

## Validation checklist

Before treating this README as implemented behavior, verify:

- [ ] Executable aggregate test modules exist under this lane.
- [ ] The aggregate lane does not duplicate object-specific child-lane assertions unnecessarily.
- [ ] Test runner and import paths match the repo's accepted convention.
- [ ] Synthetic fixtures exist and are referenced from the correct child fixture lanes.
- [ ] Schema paths and field expectations are accepted beyond scaffold status.
- [ ] SourceDescriptor/source-role behavior is available to tests or safely stubbed.
- [ ] EvidenceRef / EvidenceBundle behavior is available to tests or safely stubbed.
- [ ] PolicyDecision, ReviewRecord, ReleaseManifest, CorrectionNotice, and RollbackCard expectations are defined before enforcing them.
- [ ] CI runs the no-network Habitat land-cover aggregate suite or explicitly redirects to the detailed child subtree.
- [ ] Failures block public carrier promotion or release candidate approval.

---

## Rollback

Rollback is required if this lane becomes a live source-fetcher, source export store, lifecycle data store, fixture root, source registry, contract root, schema authority, policy authority, proof store, release-decision root, public map/API/tile surface, AI surface, renderer implementation, pipeline implementation, or publication shortcut.

Rollback target for this replacement: previous blank blob SHA `8b137891791fe96927ad78e64b0aad7bded08bdc`.

<p align="right"><a href="#top">Back to top</a></p>
