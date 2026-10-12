<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-domains-habitat-test-connectivity-readme
title: Habitat Connectivity Test README
type: test-readme
version: v0.1
status: draft; placeholder-expanded; test-lane; PROPOSED / NEEDS VERIFICATION before promotion
owners:
  - OWNER_TBD — Habitat domain steward
  - OWNER_TBD — Connectivity steward
  - OWNER_TBD — Corridor steward
  - OWNER_TBD — Evidence steward
  - OWNER_TBD — Policy steward
  - OWNER_TBD — Validation steward
  - OWNER_TBD — Release steward
  - OWNER_TBD — QA steward
created: NEEDS VERIFICATION — blank placeholder existed before v0.1 expansion
updated: 2026-07-05
policy_label: public-doc; tests; habitat; connectivity; no-network; derived-stays-derived; evidence-bound; sensitivity-aware; release-gated; public-safe-geometry
tags: [kfm, tests, habitat, connectivity, test_connectivity, ConnectivityEdge, Corridor, derived-product, ModelRunReceipt, UncertaintySurface, public-safe-geometry, source-role, EvidenceRef, EvidenceBundle, PolicyDecision, ReleaseManifest, CorrectionNotice, RollbackCard, ABSTAIN, DENY]
related:
  - ../../../README.md
  - ../README.md
  - ../../../../docs/domains/habitat/sublanes/connectivity.md
  - ../../../../contracts/domains/habitat/connectivity_edge.md
  - ../../../../contracts/domains/habitat/corridor.md
  - ../../../../contracts/domains/habitat/habitat_patch.md
  - ../../../../contracts/domains/habitat/SuitabilityModel.md
  - ../../../../contracts/domains/habitat/land_cover/observation.md
  - ../../../../contracts/domains/habitat/land_cover/model_run_receipt.md
  - ../../../../contracts/domains/habitat/land_cover/uncertainty.md
  - ../../../../schemas/contracts/v1/domains/habitat/connectivity_edge.schema.json
  - ../../../../schemas/contracts/v1/domains/habitat/corridor.schema.json
  - ../../../../fixtures/domains/habitat/connectivity_edge/
  - ../../../../fixtures/domains/habitat/corridor/
  - ../../../../pipelines/domains/habitat/
  - ../../../../pipeline_specs/habitat/
  - ../../../../policy/domains/habitat/
  - ../../../../policy/sensitivity/habitat/
  - ../../../../data/registry/sources/habitat/
  - ../../../../release/manifests/habitat/
notes:
  - "This file replaces a blank placeholder at tests/domains/habitat/test_connectivity/README.md."
  - "This is a test-lane README only. It does not define Habitat connectivity doctrine, semantic contracts, schemas, fixtures, lifecycle records, evidence bundles, receipts, policy rules, release decisions, pipeline code, public API material, public map material, public tiles, or published artifacts."
  - "The tested invariant is that ConnectivityEdge and Corridor are derived Habitat products. They must preserve model-run support, input evidence, uncertainty, source-role posture, sensitivity posture, public-safe geometry, release relationship, correction, and rollback without becoming observed movement, transport corridor, regulatory designation, HabitatPatch, source truth, release authority, public layer truth, or AI/UI truth."
  - "Default posture is deterministic and no-network. Live source checks, real source exports, lifecycle data, public tiles, and sensitive joined records do not belong in this lane."
  - "Rollback target for this replacement is previous blank blob SHA 8b137891791fe96927ad78e64b0aad7bded08bdc."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Habitat connectivity tests

> Deterministic, no-network test documentation for proving that Habitat `ConnectivityEdge` and `Corridor` objects remain evidence-bound, derived, public-safe, source-role-aware, sensitivity-aware, release-gated, correction-aware, and rollback-ready.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: tests" src="https://img.shields.io/badge/root-tests%2F-blue">
  <img alt="Domain: habitat" src="https://img.shields.io/badge/domain-habitat-2e7d32">
  <img alt="Lane: connectivity" src="https://img.shields.io/badge/lane-connectivity-blue">
  <img alt="Network: disabled by default" src="https://img.shields.io/badge/network-disabled__by__default-critical">
  <img alt="Boundary: derived stays derived" src="https://img.shields.io/badge/boundary-derived__stays__derived-success">
</p>

**Path:** `tests/domains/habitat/test_connectivity/README.md`  
**Status:** draft / placeholder-expanded / PROPOSED until executable tests are verified  
**Owning root:** `tests/`  
**Domain segment:** `habitat`  
**Test lane:** `test_connectivity`  
**Default execution posture:** deterministic, synthetic, no-network, public-safe fixtures only  
**Truth posture:** CONFIRMED target was a blank placeholder before this expansion · CONFIRMED `tests/` is the canonical root for enforceability proof · CONFIRMED connectivity doctrine names `ConnectivityEdge` and `Corridor` as Habitat-owned object families with PROPOSED field realization · CONFIRMED connectivity products are derived and never become canonical truth · CONFIRMED `ConnectivityEdge` and `Corridor` contracts exist as semantic contracts with scaffold schemas and NEEDS VERIFICATION field enforcement · NEEDS VERIFICATION for executable test modules, fixture payload inventory, validator behavior, model-run enforcement, policy runtime, release integration, public route/UI behavior, CI coverage, and pass rates.

**Quick jumps:** [Purpose](#purpose) · [Placement basis](#placement-basis) · [Invariant under test](#invariant-under-test) · [Expected scope](#expected-scope) · [Fixture posture](#fixture-posture) · [Assertions](#assertions) · [Finite outcomes](#finite-outcomes) · [Forbidden shortcuts](#forbidden-shortcuts) · [Suggested layout](#suggested-layout) · [Run posture](#run-posture) · [Evidence ledger](#evidence-ledger) · [Validation checklist](#validation-checklist) · [Rollback](#rollback)

---

## Purpose

`tests/domains/habitat/test_connectivity/` is the intended home for Habitat connectivity tests.

This lane should prove that `ConnectivityEdge` and `Corridor` products remain derived Habitat objects whose assumptions, input evidence, model-run support, uncertainty, source roles, sensitivity posture, public-safe geometry, review state, release relationship, correction path, and rollback target remain inspectable.

A passing test here should **not** mean that a real corridor is correct, a movement route is observed, a release is approved, or a public map layer is safe. It should mean only that connectivity guardrails behaved as expected against bounded fixtures.

---

## Placement basis

`tests/` is the canonical root for enforceability proof. Habitat is a domain segment inside that root. `test_connectivity` is a user-requested test lane; it is not a new repo-root domain folder and not a parallel contract, schema, policy, data, release, or proof home.

| Responsibility | Correct home | This lane's relationship |
|---|---|---|
| Connectivity tests | `tests/domains/habitat/test_connectivity/` | This directory. |
| Connectivity doctrine | `docs/domains/habitat/sublanes/connectivity.md` | Referenced doctrine; tests do not redefine it. |
| `ConnectivityEdge` meaning | `contracts/domains/habitat/connectivity_edge.md` | Semantic contract under test. |
| `Corridor` meaning | `contracts/domains/habitat/corridor.md` | Semantic contract under test. |
| Machine schemas | `schemas/contracts/v1/domains/habitat/connectivity_edge.schema.json`, `schemas/contracts/v1/domains/habitat/corridor.schema.json` | Referenced where accepted; scaffold posture must be respected. |
| Fixtures | `fixtures/domains/habitat/connectivity_edge/`, `fixtures/domains/habitat/corridor/` | Preferred toy inputs and expected outcomes if populated. |
| Model-run and uncertainty support | `contracts/domains/habitat/land_cover/model_run_receipt.md`, `contracts/domains/habitat/land_cover/uncertainty.md` or future Habitat-wide equivalents | Required support concepts; exact cross-sublane home remains NEEDS VERIFICATION. |
| Policy and sensitivity homes | `policy/domains/habitat/`, `policy/sensitivity/habitat/` or inherited joined-lane homes where accepted | Referenced by tests, not bypassed here. |
| Release decisions | `release/` and `release/manifests/habitat/` | Publication, correction, and rollback authority; tests cannot replace it. |

---

## Invariant under test

> **Derived stays derived.** `ConnectivityEdge` and `Corridor` are computed Habitat connectivity products. They must never be presented as observed animal movement, transport corridors, regulatory designations, source truth, public-layer truth, release authority, or AI/UI truth.

Core checks:

| Check | Required behavior | Failure outcome |
|---|---|---|
| Derived identity | Edge/corridor identity includes method, inputs, temporal scope, and normalized digest posture. | validation failure / `ERROR`. |
| Input support | Habitat patches, suitability, land cover, resistance/context, and public-safe joined context remain cited and role-typed. | `ABSTAIN` / validation failure. |
| Model-run support | Model/run receipt, config digest, input digest, output digest, method parameters, and run time are attached where material. | validation failure. |
| Uncertainty support | Confidence, weakest-input support, geometry/generalization caveats, and uncertainty posture travel with the product. | review required / `ABSTAIN`. |
| Edge/corridor split | `ConnectivityEdge` as relation and `Corridor` as spatialization remain separate. | validation failure. |
| Public-safe geometry | Internal geometry, generalized geometry, withheld geometry, and aggregate-only posture are explicit. | `DENY` / `RESTRICT`. |
| Sensitivity inheritance | The product inherits restrictive input posture until governed transformation and review say otherwise. | `DENY` / `RESTRICT` / hold. |
| Release boundary | Policy, review, release, correction, and rollback remain separate from test pass state. | promotion block. |
| No authority upgrade | Connectivity output cannot become movement truth, regulatory truth, transport truth, public-layer truth, or AI truth. | validation failure / `ABSTAIN`. |

---

## Expected scope

Tests in this lane may validate:

- required edge/corridor identity and object-family separation;
- rejection of corridors presented as observed movement routes or transport corridors;
- model-run receipt and uncertainty requirements for derived connectivity outputs;
- source-role and sensitivity inheritance from input patches, suitability surfaces, land-cover observations, and public-safe context;
- public-safe geometry posture before map/API/UI/AI carrier use;
- rejection of released/public-facing candidates that lack evidence, policy, review, release relationship, correction, or rollback context;
- finite outcomes when a policy engine, evidence resolver, model-run receipt, uncertainty support, or release manifest is missing.

Live source checks, real source exports, production routes, public tile generation, sensitive joined records, and provider-backed model calls are out of scope for the default suite.

---

## Fixture posture

Use synthetic, public-safe fixtures only.

Fixture requirements:

- deterministic and no-network;
- compact enough for review in a PR;
- explicit expected outcome;
- explicit object family: `ConnectivityEdge`, `Corridor`, invalid, public-safe candidate, or withheld candidate;
- explicit model-run, uncertainty, evidence, policy, review, release relationship, correction, and rollback posture where material;
- no real source exports, lifecycle data, public tiles, sensitive joined records, or published artifacts.

Preferred fixture families:

| Fixture kind | Expected outcome |
|---|---|
| Valid synthetic `ConnectivityEdge` with node pair, method, inputs, receipt, uncertainty, and evidence refs | accepted derived support only. |
| Valid synthetic `Corridor` with generalized/public-safe geometry and release relationship | accepted carrier candidate only. |
| Missing model-run receipt | validation failure / `ABSTAIN`. |
| Missing uncertainty support | review required / `ABSTAIN`. |
| Corridor treated as observed movement route | validation failure / `DENY`. |
| Edge treated as corridor geometry | validation failure. |
| Public output lacks release/correction/rollback posture | promotion block. |
| AI/UI answer treats connectivity as truth | `ABSTAIN` / validation failure. |

---

## Assertions

A useful Habitat connectivity test should make the derived-product boundary obvious.

### Positive path

- object family and identity are explicit;
- input support and source roles are preserved;
- method, model run, config digest, input digest, output digest, and run time are visible where material;
- uncertainty and weakest-input caveats are visible;
- edge relation and corridor spatialization remain separate;
- public-safe geometry and sensitivity posture are explicit;
- evidence, policy, review, release relationship, correction, and rollback references are linkable where material.

### Negative path

- derived output cannot become observed animal movement;
- Habitat corridor cannot become transport corridor or regulatory designation;
- corridor geometry cannot hide provenance, uncertainty, or sensitivity posture;
- test pass cannot become release approval;
- map style, tile, popup, graph edge, Focus Mode answer, or AI text cannot become connectivity authority;
- missing evidence produces `ABSTAIN` rather than a fluent claim.

---

## Finite outcomes

| Condition | Expected outcome |
|---|---|
| Valid synthetic derived object with evidence, model run, uncertainty, policy, review, release relationship, correction, and rollback context | accepted derived support only. |
| Missing object family, method, input support, or model-run receipt | validation failure / `ERROR` / `ABSTAIN`. |
| Missing uncertainty or public-safe geometry posture | review required / `ABSTAIN` / `DENY`. |
| Connectivity product treated as observed movement, transport corridor, regulatory designation, or source truth | validation failure. |
| Public-facing candidate lacks release/correction/rollback posture | promotion-blocking failure. |
| Policy engine unavailable | `ERROR` or `ABSTAIN`, never public exposure. |

---

## Forbidden shortcuts

Do not use this test lane to:

- fetch live upstream source systems;
- store real source exports, lifecycle data, real route/corridor geometry, public tiles, or release artifacts;
- store proof packs, release manifests, or generated public layers;
- redefine Habitat connectivity doctrine, contracts, schemas, fixtures, policy rules, receipts, proofs, release decisions, renderer code, or production code;
- bypass model-run receipt, uncertainty, evidence, validation, policy, review, correction, or rollback checks with a fixture flag;
- infer release state from file existence, test success, layer name, graph edge, map rendering, tile availability, or AI wording;
- publish, promote, or release anything.

Any test that needs real model outputs, source data, or public tile output belongs in a gated integration tier with source admission, lifecycle state, policy, receipts, release controls, and rollback targets.

---

## Suggested layout

The exact test module names remain **NEEDS VERIFICATION** until the runner and existing conventions are inspected.

```text
tests/domains/habitat/test_connectivity/
├── README.md
├── test_connectivity_edge_identity.py
├── test_corridor_spatialization.py
├── test_derived_stays_derived.py
├── test_model_run_and_uncertainty_required.py
├── test_public_safe_geometry.py
├── test_sensitive_input_inheritance.py
└── test_release_correction_rollback.py
```

---

## Run posture

```bash
pytest tests/domains/habitat/test_connectivity
```

Status of the command above: **PROPOSED / NEEDS VERIFICATION**. It assumes `pytest` is the accepted test runner and that executable test modules exist. This README does not claim the command currently passes.

---

## Evidence ledger

| Evidence | Status | Supports | Limits |
|---|---|---|---|
| Previous target file | CONFIRMED | `tests/domains/habitat/test_connectivity/README.md` existed as a blank placeholder before this replacement. | Did not define the lane. |
| `tests/README.md` | CONFIRMED | `tests/` is enforceability proof and failure should block promotion where trust-spine checks fail. | Does not prove this lane's modules or pass rate. |
| `docs/domains/habitat/sublanes/connectivity.md` | CONFIRMED doctrine / PROPOSED implementation | Connectivity products are derived; `ConnectivityEdge` and `Corridor` are Habitat-owned object families; derived outputs do not become canonical truth; sensitive movement detail is denied by default. | Implementation paths, validators, fixtures, schemas, policy runtime, release artifacts, UI, Focus Mode, and CI remain NEEDS VERIFICATION. |
| `contracts/domains/habitat/connectivity_edge.md` | CONFIRMED semantic contract / PROPOSED implementation | Defines `ConnectivityEdge` as derived graph evidence and not observed animal movement, transport corridor, regulatory designation, public layer, management instruction, or release authority. | Schema is a permissive scaffold; field-level enforcement remains NEEDS VERIFICATION. |
| `contracts/domains/habitat/corridor.md` | CONFIRMED semantic contract / PROPOSED implementation | Defines `Corridor` as derived spatialization of connectivity with public-safe geometry, evidence, policy, review, release, correction, and rollback controls. | Schema is a permissive scaffold; field-level enforcement remains NEEDS VERIFICATION. |

---

## Validation checklist

Before treating this README as implemented behavior, verify:

- [ ] Executable test modules exist under this lane.
- [ ] Test runner and import paths match the repo's accepted convention.
- [ ] Synthetic fixtures exist for valid edge, valid corridor, missing receipt, missing uncertainty, sensitive input inheritance, corridor-as-movement, corridor-as-transport, missing public-safe geometry, and missing release/correction/rollback cases.
- [ ] ConnectivityEdge and Corridor schema paths and field expectations are accepted beyond scaffold status.
- [ ] EvidenceRef / EvidenceBundle behavior is available to tests or safely stubbed.
- [ ] ModelRunReceipt and UncertaintySurface behavior is available to tests or safely stubbed.
- [ ] PolicyDecision, ReviewRecord, ReleaseManifest, CorrectionNotice, RedactionReceipt, and RollbackCard expectations are defined before enforcing them.
- [ ] CI runs the no-network Habitat connectivity suite.
- [ ] Failures block public carrier promotion or release candidate approval.

---

## Rollback

Rollback is required if this lane becomes a source export store, route/corridor data store, lifecycle data store, fixture root, contract root, schema authority, policy authority, proof store, release-decision root, public map/API/tile surface, AI surface, renderer implementation, pipeline implementation, or publication shortcut.

Rollback target for this replacement: previous blank blob SHA `8b137891791fe96927ad78e64b0aad7bded08bdc`.

<p align="right"><a href="#top">Back to top</a></p>
