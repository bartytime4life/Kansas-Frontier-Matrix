<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-domains-geology-test-public-safe-geometry-readme
title: Geology Public-Safe Geometry Test README
type: test-readme
version: v0.1
status: draft; placeholder-expanded; test-lane; PROPOSED / NEEDS VERIFICATION before promotion
owners:
  - OWNER_TBD — Geology domain steward
  - OWNER_TBD — Geometry steward
  - OWNER_TBD — Policy steward
  - OWNER_TBD — Evidence steward
  - OWNER_TBD — Validation steward
  - OWNER_TBD — Release steward
  - OWNER_TBD — QA steward
created: NEEDS VERIFICATION — blank placeholder existed before v0.1 expansion
updated: 2026-07-05
policy_label: public-doc; tests; geology; public-safe-geometry; no-network; deny-by-default; release-gated; source-role-aware
tags: [kfm, tests, geology, geometry, public-safe-geometry, redaction, generalization, sensitivity, EvidenceBundle, PolicyDecision, RedactionReceipt, ReleaseManifest, DENY, RESTRICT, ABSTAIN]
related:
  - ../../../../tests/README.md
  - ../../../../fixtures/domains/geology/README.md
  - ../../../../packages/domains/geology/geometry/README.md
  - ../../../../policy/domains/geology/public_safe_geometry.policy.json
  - ../../../../release/public_safe_geometry.rego
  - ../../../../docs/domains/geology/README.md
  - ../../../../docs/domains/geology/POLICY.md
  - ../../../../docs/domains/geology/PRESERVATION_MATRIX.md
  - ../../../../contracts/domains/geology/
  - ../../../../schemas/contracts/v1/domains/geology/
  - ../../../../policy/domains/geology/
  - ../../../../data/registry/sources/geology/
  - ../../../../data/proofs/
  - ../../../../data/receipts/
  - ../../../../release/
notes:
  - "This file replaces a blank placeholder at tests/domains/geology/test_public_safe_geometry/README.md."
  - "This is a test-lane README only. It does not define geometry helper implementation, public-safe geometry policy, schemas, source descriptors, redaction receipts, proof objects, release decisions, or published artifacts."
  - "The tested invariant is that exact/internal geology geometry must not reach public API, map, tile, AI, catalog-release, or UI surfaces unless an approved public-safe transform, policy decision, evidence support, review state, release state, and rollback path exist."
  - "The default posture is deterministic and no-network. Live source checks, credentials, and real exact geology/resource locations do not belong in this lane."
  - "Rollback target for this replacement is previous blank blob SHA 8b137891791fe96927ad78e64b0aad7bded08bdc."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Geology public-safe geometry tests

> Deterministic, no-network test documentation for proving that Geology and Natural Resources geometry is generalized, masked, denied, restricted, or abstained before it can become a public-facing map, API, tile, catalog-release, Evidence Drawer, or Focus Mode carrier.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: tests" src="https://img.shields.io/badge/root-tests%2F-blue">
  <img alt="Domain: geology" src="https://img.shields.io/badge/domain-geology%2Fnatural__resources-brown">
  <img alt="Invariant: public safe geometry" src="https://img.shields.io/badge/invariant-public__safe__geometry-critical">
  <img alt="Network: disabled by default" src="https://img.shields.io/badge/network-disabled__by__default-critical">
  <img alt="Exposure: deny by default" src="https://img.shields.io/badge/exposure-deny__by__default-success">
</p>

**Path:** `tests/domains/geology/test_public_safe_geometry/README.md`  
**Status:** draft / placeholder-expanded / PROPOSED until paired test files are verified  
**Owning root:** `tests/`  
**Domain segment:** `geology`  
**Test lane:** `test_public_safe_geometry`  
**Default execution posture:** deterministic, synthetic, no-network, public-safe fixtures only  
**Truth posture:** CONFIRMED target was a blank placeholder before this expansion · CONFIRMED KFM testing doctrine places domain-specific tests under `tests/domains/<domain>/` · CONFIRMED Geology geometry package doctrine separates exact/internal geometry from public-safe geometry · CONFIRMED a proposed public-safe geometry policy placeholder exists under `policy/domains/geology/` · NEEDS VERIFICATION for actual test modules, fixtures, geometry helpers, schemas, validators, policy engine wiring, redaction receipt emission, CI coverage, and release-gate integration.

**Quick jumps:** [Purpose](#purpose) · [Placement basis](#placement-basis) · [Invariant under test](#invariant-under-test) · [Expected test scope](#expected-test-scope) · [Fixture posture](#fixture-posture) · [Assertions](#assertions) · [Finite outcomes](#finite-outcomes) · [Forbidden shortcuts](#forbidden-shortcuts) · [Suggested test layout](#suggested-test-layout) · [Run posture](#run-posture) · [Evidence ledger](#evidence-ledger) · [Validation checklist](#validation-checklist) · [Rollback](#rollback)

---

## Purpose

`tests/domains/geology/test_public_safe_geometry/` is the intended home for tests that prove Geology geometry cannot cross the public trust membrane unless it has been transformed, reviewed, policy-admitted, evidence-bound, and release-linked.

This lane should test that geometry-bearing Geology outputs preserve the distinction between:

- source-native geometry;
- internal exact geometry;
- interpreted boundaries;
- derived generalized geometry;
- public-safe geometry;
- masked or suppressed geometry;
- centroid, bounding-box, grid-cell, county, watershed, quad, or other generalized discovery geometry.

A passing test here should **not** mean that a public geometry product is released or scientifically authoritative. It should mean only that the public-safe geometry boundary behaved as expected against bounded fixtures.

---

## Placement basis

`tests/` is the canonical root for enforceability proof. Geology appears as a lane segment inside the tests root, not as a repo-root domain folder.

| Responsibility | Correct home | This lane's relationship |
|---|---|---|
| Domain public-safe geometry tests | `tests/domains/geology/test_public_safe_geometry/` | This directory. |
| Synthetic geometry fixtures and expected outcomes | `fixtures/domains/geology/` | Preferred source for toy inputs and expected envelopes. |
| Geometry helper code | `packages/domains/geology/geometry/` | System under test where helper behavior exists. |
| Public-safe geometry policy | `policy/domains/geology/public_safe_geometry.policy.json`, `release/public_safe_geometry.rego` if accepted | Referenced by tests, not redefined here. |
| Semantic geometry meaning | `contracts/domains/geology/` | Referenced by tests, not duplicated here. |
| Machine shape | `schemas/contracts/v1/domains/geology/` | Referenced by tests, not duplicated here. |
| Receipts and proofs | `data/receipts/`, `data/proofs/` | Expected references; not authored as test truth here. |
| Release decisions | `release/` | Required before public delivery; tests cannot replace it. |

---

## Invariant under test

> **Public-safe geometry before exposure.** Exact/internal geology geometry must not reach public map, API, tile, catalog-release, Evidence Drawer, Focus Mode, export, or AI surfaces unless policy, evidence, review, release, and rollback controls allow a public-safe representation.

For this test lane, the invariant decomposes into nine checks:

| Check | Required behavior | Failure outcome |
|---|---|---|
| Geometry role | Input and output geometry roles are explicit. | validation failure / `ERROR`. |
| CRS and scale | CRS, source scale, uncertainty, and simplification context are explicit. | validation failure / `ABSTAIN`. |
| Sensitivity | Borehole, private-well, sample, mineral, extraction, reclamation, and resource-location geometry defaults restricted until cleared. | `DENY` / `RESTRICT`. |
| Transform metadata | Generalization, masking, gridding, rounding, aggregation, suppression, or bounding-box output carries method and parameters. | validation failure. |
| Evidence context | Geometry-bearing claim still points to evidence support; geometry alone is not evidence closure. | `ABSTAIN`. |
| Policy decision | Public exposure has a PolicyDecision or accepted policy result. | `DENY` / `RESTRICT` / `ABSTAIN`. |
| Release state | Public-safe geometry is release-linked before public use. | `ABSTAIN (not_yet_released)` or promotion failure. |
| Leakage prevention | Output does not leak exact/internal coordinates through centroids, bboxes, precision, IDs, hashes, tiles, logs, or metadata. | test failure. |
| Rollback | Release-linked public-safe geometry has correction and rollback references where material. | promotion-blocking failure. |

---

## Expected test scope

Tests in this lane should be small, synthetic, and deterministic. They may validate:

- public-safe transform behavior for toy point, line, polygon, bbox, centroid, and grid-cell examples;
- denial or restriction of exact/internal borehole, sample, mineral occurrence, private-well, extraction, production, reclamation, or sensitive resource geometry;
- preservation of geometry-role metadata through transform output;
- CRS, scale, uncertainty, and simplification tolerance checks;
- detection of precision leakage in supposedly public-safe coordinates;
- rejection of public outputs that lack transform metadata or policy decision;
- rejection of public outputs that use `RAW`, `WORK`, `QUARANTINE`, or internal exact geometry directly;
- linkage between public-safe output, evidence support, receipt-ready transform metadata, release state, correction path, and rollback target.

Live source systems and real exact locations are out of scope for the default suite.

---

## Fixture posture

Use fixture material from `fixtures/domains/geology/` when possible.

Fixture requirements:

- synthetic and public-safe;
- no real coordinates for sensitive geology/resource features;
- no live source calls;
- compact enough for review in a PR;
- explicit expected outcome;
- explicit geometry role;
- explicit source scale, uncertainty, and CRS state where relevant;
- explicit sensitivity posture;
- explicit policy/release state;
- explicit transform metadata for positive public-safe examples.

Preferred fixture families:

| Fixture kind | Preferred lane | Example expected outcome |
|---|---|---|
| Safe generalized polygon | `fixtures/domains/geology/valid/` or `golden/` | Public-safe output allowed with transform metadata. |
| Exact restricted point | `fixtures/domains/geology/invalid/` or `tier-transitions/` | `DENY` / `RESTRICT`. |
| Missing transform metadata | `fixtures/domains/geology/invalid/` | validation failure. |
| Source-role geometry mismatch | `fixtures/domains/geology/source_role/` | `DENY`, `RESTRICT`, or closure failure. |
| Map/UI geometry envelope | `fixtures/domains/geology/map-ui/` | No exact geometry leaks to UI/runtime payload. |
| Public-safe release candidate | `fixtures/domains/geology/golden/` | Requires release/correction/rollback references before public use. |

---

## Assertions

A good public-safe-geometry test should make the exposure decision auditable.

### Positive path

- input geometry role is explicit and not public by default;
- output geometry role is `public_safe`, `masked_or_suppressed`, `derived_generalized`, `centroid_or_bbox`, or `grid_cell` only when policy allows it;
- CRS, scale, uncertainty, transform method, transform version, and parameter values are recorded;
- input and output digests or fixture IDs are available for receipt-ready metadata;
- evidence and source references remain attached where the geometry supports a claim;
- public output links to policy, review, release, correction, and rollback context where material.

### Negative path

- exact/internal geometry cannot be emitted as public-safe by renaming the role;
- missing CRS, scale, geometry role, or sensitivity context fails closed;
- public-safe output without transform metadata fails;
- restricted geometry without policy clearance returns `DENY` or `RESTRICT`;
- unreleased public-safe geometry returns `ABSTAIN` or blocks promotion;
- centroids, bboxes, tile coordinates, IDs, hashes, logs, and metadata must not leak exact sensitive coordinates;
- AI, map, graph, tile, or catalog summaries cannot substitute for geometry policy.

---

## Finite outcomes

This lane should prefer explicit finite outcomes over loose pass/fail text.

| Condition | Expected outcome |
|---|---|
| Safe generalized geometry with evidence, policy, review, and release context | allow public-safe carrier / `ANSWER` only downstream if citation-closed. |
| Exact/internal restricted geometry requested for public exposure | `DENY` or `RESTRICT`. |
| Missing geometry role, CRS, source scale, or sensitivity context | validation failure, `ABSTAIN`, or `ERROR`. |
| Missing public-safe transform metadata | validation failure. |
| Geometry not yet released | `ABSTAIN (not_yet_released)` or promotion failure. |
| Sensitive coordinate leakage detected | test failure / `DENY`. |
| Policy engine unavailable | `ERROR` or `ABSTAIN`, never public exposure. |

---

## Forbidden shortcuts

Do not use this test lane to:

- fetch live upstream source systems;
- store credentials or tokens;
- store real source exports;
- store real exact borehole, sample, private-well, mineral, extraction, reclamation, or resource-location coordinates;
- redefine public-safe geometry policy;
- redefine schemas, contracts, source descriptors, receipts, proofs, evidence bundles, or release decisions;
- bypass policy with a fixture flag;
- treat generalized geometry as proof of the underlying geology claim;
- treat map tiles, vector tiles, MapLibre layers, screenshots, AI summaries, or graph edges as sovereign truth;
- publish, promote, or release anything.

Any test that requires real source geometry belongs in a gated integration tier with explicit quarantine, redaction, policy, audit, and rollback controls.

---

## Suggested test layout

The exact Python module names remain NEEDS VERIFICATION until the runner and existing test conventions are inspected. A minimal future layout could be:

```text
tests/domains/geology/test_public_safe_geometry/
├── README.md
├── test_geometry_role_required.py              # no implicit public geometry role
├── test_restricted_exact_geometry_denied.py    # exact/internal sensitive geometry fails closed
├── test_public_safe_transform_metadata.py      # method, params, digest, reason codes required
├── test_no_coordinate_leakage.py               # centroid/bbox/tile/log/metadata leakage checks
└── test_release_link_required.py               # release/correction/rollback before public carrier
```

Keep helpers local only when they are test-specific. Shared geometry, policy, redaction, runtime-envelope, or release behavior belongs under its accepted implementation root, not duplicated here.

---

## Run posture

Default run expectations:

```bash
pytest tests/domains/geology/test_public_safe_geometry
```

Status of the command above: **PROPOSED / NEEDS VERIFICATION**. It assumes `pytest` is the accepted test runner and that the test modules exist. This README does not claim the command currently passes.

Expected CI posture:

- default suite: no-network, synthetic fixtures only;
- fail closed on missing geometry role, CRS, sensitivity context, transform metadata, evidence support, policy decision, release state, or leakage checks;
- live-source checks: separate gated job only;
- release gate: public-safe-geometry failures should block public map/API/tile/AI carrier promotion.

---

## Evidence ledger

| Evidence | Status | Supports | Limits |
|---|---|---|---|
| Previous target file | CONFIRMED | `tests/domains/geology/test_public_safe_geometry/README.md` existed as a blank placeholder before this replacement. | Did not define the lane. |
| `tests/README.md` | CONFIRMED | `tests/` is enforceability proof; domain-specific tests belong under `tests/domains/<domain>/`; default suite should avoid sensitive data and live network calls. | Does not prove this lane's modules or pass rate. |
| `packages/domains/geology/geometry/README.md` | CONFIRMED doctrine / PROPOSED implementation | Geology geometry helpers must separate exact/internal geometry from public-safe geometry, preserve CRS/scale/uncertainty, and return finite outcomes for missing public-safe context. | Does not prove imports, helper code, tests, policy enforcement, or runtime behavior. |
| `policy/domains/geology/public_safe_geometry.policy.json` | CONFIRMED placeholder | A proposed policy placeholder exists for Geology public-safe geometry. | It is only a placeholder and does not prove enforced policy. |
| `docs/domains/geology/README.md` | CONFIRMED doctrine / PROPOSED implementation | Geology scope, anti-collapse rules, lifecycle invariant, public trust path, and exact-location deny-by-default posture. | Does not prove public-safe geometry tests exist. |
| `fixtures/domains/geology/README.md` | CONFIRMED | Synthetic, public-safe fixture posture and child fixture lanes for Geology. | Does not prove all fixture payloads or consumers. |

---

## Validation checklist

Before treating this README as implemented behavior, verify:

- [ ] Test modules exist under this lane.
- [ ] Test runner and import paths match the repo's accepted convention.
- [ ] Synthetic fixtures exist for public-safe positive output, exact restricted input, missing transform metadata, missing CRS, missing sensitivity context, coordinate leakage, and release-linked carrier checks.
- [ ] Geometry helper behavior is available to tests or safely stubbed.
- [ ] PolicyDecision behavior is available to tests or safely stubbed.
- [ ] Public-safe geometry policy is implemented beyond placeholder status before enforcing policy-specific expectations.
- [ ] RedactionReceipt or receipt-ready transform metadata expectations are defined before enforcing them.
- [ ] ReleaseManifest, CorrectionNotice, and RollbackCard expectations are defined before enforcing release-linked public geometry.
- [ ] CI runs the no-network public-safe-geometry suite.
- [ ] Failures block public geometry carrier promotion or release candidate approval.

---

## Rollback

Rollback is required if this lane becomes a geometry implementation root, source registry, fixture root, lifecycle data store, proof store, receipt store, release-decision root, schema authority, policy authority, public map/API/tile surface, AI surface, or publication shortcut.

Rollback target for this replacement: previous blank blob SHA `8b137891791fe96927ad78e64b0aad7bded08bdc`.

<p align="right"><a href="#top">Back to top</a></p>
