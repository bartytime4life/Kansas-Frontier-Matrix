<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-domains-habitat-test-corridor-readme
title: Habitat Corridor Test README
type: test-readme
version: v0.1
status: draft; placeholder-expanded; test-lane; PROPOSED / NEEDS VERIFICATION before promotion
owners:
  - OWNER_TBD — Habitat domain steward
  - OWNER_TBD — Connectivity steward
  - OWNER_TBD — Corridor steward
  - OWNER_TBD — Evidence steward
  - OWNER_TBD — Policy steward
  - OWNER_TBD — Sensitivity reviewer
  - OWNER_TBD — Validation steward
  - OWNER_TBD — Release steward
  - OWNER_TBD — QA steward
created: NEEDS VERIFICATION — blank placeholder existed before v0.1 expansion
updated: 2026-07-05
policy_label: public-doc; tests; habitat; corridor; no-network; derived-stays-derived; public-safe-geometry; geoprivacy-aware; evidence-bound; sensitivity-aware; release-gated
tags: [kfm, tests, habitat, corridor, test_corridor, Corridor, ConnectivityEdge, derived-product, corridor-geometry, public-safe-geometry, geoprivacy, RedactionReceipt, ModelRunReceipt, UncertaintySurface, EvidenceRef, EvidenceBundle, PolicyDecision, ReleaseManifest, CorrectionNotice, RollbackCard, ABSTAIN, DENY, RESTRICT]
related:
  - ../../../README.md
  - ../README.md
  - ../test_connectivity/README.md
  - ../../../../docs/domains/habitat/sublanes/connectivity.md
  - ../../../../contracts/domains/habitat/corridor.md
  - ../../../../contracts/domains/habitat/connectivity_edge.md
  - ../../../../contracts/domains/habitat/habitat_patch.md
  - ../../../../contracts/domains/habitat/SuitabilityModel.md
  - ../../../../contracts/domains/habitat/land_cover/observation.md
  - ../../../../contracts/domains/habitat/land_cover/model_run_receipt.md
  - ../../../../contracts/domains/habitat/land_cover/uncertainty.md
  - ../../../../schemas/contracts/v1/domains/habitat/corridor.schema.json
  - ../../../../schemas/contracts/v1/domains/habitat/connectivity_edge.schema.json
  - ../../../../fixtures/domains/habitat/corridor/
  - ../../../../fixtures/domains/habitat/connectivity_edge/
  - ../../../../pipelines/domains/habitat/
  - ../../../../pipeline_specs/habitat/
  - ../../../../policy/domains/habitat/
  - ../../../../policy/sensitivity/habitat/
  - ../../../../data/registry/sources/habitat/
  - ../../../../release/manifests/habitat/
notes:
  - "This file replaces a blank placeholder at tests/domains/habitat/test_corridor/README.md."
  - "This is a test-lane README only. It does not define Habitat corridor doctrine, semantic contracts, schemas, fixtures, lifecycle records, evidence bundles, receipts, policy rules, release decisions, pipeline code, public API material, public map material, public tiles, or published artifacts."
  - "The tested invariant is that Corridor is a derived Habitat spatialization of connectivity. It must preserve connectivity-edge linkage, derivation method, model-run support, input evidence, uncertainty, source-role posture, sensitivity posture, geoprivacy/public-safe geometry state, release relationship, correction, and rollback without becoming observed animal movement, transport corridor, regulatory designation, management instruction, source truth, release authority, public-layer truth, or AI/UI truth."
  - "Default posture is deterministic and no-network. Live source checks, real source exports, lifecycle data, public tiles, and sensitive joined records do not belong in this lane."
  - "Rollback target for this replacement is previous blank blob SHA 8b137891791fe96927ad78e64b0aad7bded08bdc."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Habitat corridor tests

> Deterministic, no-network test documentation for proving that Habitat `Corridor` objects remain derived spatializations of connectivity with inspectable provenance, uncertainty, sensitivity, public-safe geometry, release relationship, correction path, and rollback target.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: tests" src="https://img.shields.io/badge/root-tests%2F-blue">
  <img alt="Domain: habitat" src="https://img.shields.io/badge/domain-habitat-2e7d32">
  <img alt="Lane: corridor" src="https://img.shields.io/badge/lane-corridor-blue">
  <img alt="Network: disabled by default" src="https://img.shields.io/badge/network-disabled__by__default-critical">
  <img alt="Boundary: corridor not observed route" src="https://img.shields.io/badge/boundary-corridor__not__observed__route-success">
</p>

**Path:** `tests/domains/habitat/test_corridor/README.md`  
**Status:** draft / placeholder-expanded / PROPOSED until executable tests are verified  
**Owning root:** `tests/`  
**Domain segment:** `habitat`  
**Test lane:** `test_corridor`  
**Default execution posture:** deterministic, synthetic, no-network, public-safe fixtures only  
**Truth posture:** CONFIRMED target was a blank placeholder before this expansion · CONFIRMED `tests/` is the canonical root for enforceability proof · CONFIRMED connectivity doctrine names `Corridor` as a Habitat-owned object family with PROPOSED field realization · CONFIRMED the Corridor contract defines Corridor as derived Habitat spatialization and not an observed animal route, transport corridor, regulatory designation, management instruction, public layer, or release manifest by itself · CONFIRMED the Corridor schema is a scaffold and field-level enforcement remains NEEDS VERIFICATION · NEEDS VERIFICATION for executable test modules, fixture payload inventory, validator behavior, geoprivacy enforcement, model-run enforcement, policy runtime, release integration, public route/UI behavior, CI coverage, and pass rates.

**Quick jumps:** [Purpose](#purpose) · [Placement basis](#placement-basis) · [Invariant under test](#invariant-under-test) · [Expected scope](#expected-scope) · [Fixture posture](#fixture-posture) · [Assertions](#assertions) · [Finite outcomes](#finite-outcomes) · [Forbidden shortcuts](#forbidden-shortcuts) · [Suggested layout](#suggested-layout) · [Run posture](#run-posture) · [Evidence ledger](#evidence-ledger) · [Validation checklist](#validation-checklist) · [Rollback](#rollback)

---

## Purpose

`tests/domains/habitat/test_corridor/` is the intended home for Habitat corridor tests.

This lane should prove that `Corridor` objects preserve their derived meaning and never lose the assumptions, input support, model-run receipt, uncertainty, public-safe geometry state, sensitivity posture, release relationship, correction path, or rollback target that make them inspectable and reversible.

A passing test here should **not** mean that a real corridor is correct, a movement route is observed, a public geometry is safe, or a release is approved. It should mean only that corridor guardrails behaved as expected against bounded fixtures.

---

## Placement basis

`tests/` is the canonical root for enforceability proof. Habitat is a domain segment inside that root. `test_corridor` is a test lane, not a new root and not a parallel contract, schema, policy, data, release, proof, or public-map home.

| Responsibility | Correct home | This lane's relationship |
|---|---|---|
| Corridor tests | `tests/domains/habitat/test_corridor/` | This directory. |
| Connectivity/corridor doctrine | `docs/domains/habitat/sublanes/connectivity.md` | Referenced doctrine; tests do not redefine it. |
| Corridor meaning | `contracts/domains/habitat/corridor.md` | Semantic contract under test. |
| Connectivity relation | `contracts/domains/habitat/connectivity_edge.md` | Corridor may spatialize one or more edges; it is not the edge relation itself. |
| Machine schemas | `schemas/contracts/v1/domains/habitat/corridor.schema.json`, `schemas/contracts/v1/domains/habitat/connectivity_edge.schema.json` | Referenced where accepted; scaffold posture must be respected. |
| Fixtures | `fixtures/domains/habitat/corridor/`, `fixtures/domains/habitat/connectivity_edge/` | Preferred toy inputs and expected outcomes if populated. |
| Model-run and uncertainty support | `contracts/domains/habitat/land_cover/model_run_receipt.md`, `contracts/domains/habitat/land_cover/uncertainty.md` or future Habitat-wide equivalents | Required support concepts; exact cross-sublane home remains NEEDS VERIFICATION. |
| Policy and sensitivity homes | `policy/domains/habitat/`, `policy/sensitivity/habitat/` or inherited joined-lane homes where accepted | Referenced by tests, not bypassed here. |
| Release decisions | `release/` and `release/manifests/habitat/` | Publication, correction, and rollback authority; tests cannot replace it. |

---

## Invariant under test

> **Corridor is derived spatialization, not observed route.** A Habitat `Corridor` spatializes derived connectivity into a line, polygon, swath, least-cost path, resistance corridor, generalized public corridor, or candidate corridor. It must not become observed animal movement, a transport route, a regulatory designation, a management instruction, public-layer truth, release authority, or AI/UI truth.

Core checks:

| Check | Required behavior | Failure outcome |
|---|---|---|
| Corridor identity | Identity includes role, geometry fingerprint or digest posture, method profile, temporal scope, and support refs. | validation failure / `ERROR`. |
| Connectivity linkage | Source `ConnectivityEdge`, patch pair, node group, or run linkage is explicit where material. | validation failure. |
| Geometry posture | Internal, generalized, withheld, aggregate-only, or public-safe geometry state is explicit. | `DENY` / `RESTRICT` / validation failure. |
| Derivation method | Least-cost, resistance/circuit, graph-to-geometry, expert/steward rule, scenario method, or other method is recorded. | validation failure. |
| Input support | Patches, suitability, land-cover, resistance/context, public-safe joined context, and source vintages remain cited and role-typed. | `ABSTAIN` / validation failure. |
| Model-run support | Model-run receipt, config digest, input digest, output digest, method parameters, CRS/resolution, and run time are attached where material. | validation failure. |
| Uncertainty support | Confidence, geometry generalization caveats, and weakest-input support travel with the corridor. | review required / `ABSTAIN`. |
| Sensitivity posture | Sensitive or protected-resource context is generalized, restricted, withheld, or denied before public exposure. | `DENY` / `RESTRICT` / hold. |
| Release boundary | Policy, review, release, correction, and rollback remain separate from test pass state. | promotion block. |
| No authority upgrade | Corridor cannot become movement truth, regulatory truth, transport truth, public-layer truth, or AI truth. | validation failure / `ABSTAIN`. |

---

## Expected scope

Tests in this lane may validate:

- required corridor identity and geometry posture;
- required connectivity-edge linkage or derivation-run linkage where material;
- rejection of corridor-as-observed-movement, corridor-as-transport, corridor-as-regulatory-designation, or corridor-as-management-instruction misuse;
- model-run receipt and uncertainty requirements for derived corridor outputs;
- public-safe geometry, geoprivacy, redaction/generalization, withheld, and aggregate-only states;
- source-role and sensitivity inheritance from input patches, suitability surfaces, land-cover observations, and public-safe context;
- rejection of public-facing candidates that lack evidence, policy, review, release relationship, correction, or rollback context;
- finite outcomes when evidence resolver, policy engine, model-run receipt, uncertainty support, or release manifest is missing.

Live source checks, real source exports, production route/corridor geometry, public tile generation, sensitive joined records, and provider-backed model calls are out of scope for the default suite.

---

## Fixture posture

Use synthetic, public-safe fixtures only.

Fixture requirements:

- deterministic and no-network;
- compact enough for review in a PR;
- explicit expected outcome;
- explicit object family and geometry posture: internal, generalized, withheld, aggregate-only, public-safe candidate, or invalid;
- explicit connectivity linkage, derivation method, model-run, uncertainty, evidence, policy, review, release relationship, correction, and rollback posture where material;
- no real source exports, lifecycle data, real route/corridor geometry, public tiles, sensitive joined records, or published artifacts.

Preferred fixture families:

| Fixture kind | Expected outcome |
|---|---|
| Valid synthetic corridor with linkage, method, receipt, uncertainty, and generalized public-safe geometry | accepted derived support only. |
| Corridor missing connectivity linkage or derivation run | validation failure / `ABSTAIN`. |
| Corridor missing geometry posture | validation failure / `DENY`. |
| Corridor treated as observed animal movement | validation failure / `DENY`. |
| Corridor treated as transport corridor or regulatory designation | validation failure. |
| Missing uncertainty support | review required / `ABSTAIN`. |
| Public output lacks release/correction/rollback posture | promotion block. |
| AI/UI answer treats corridor as truth | `ABSTAIN` / validation failure. |

---

## Assertions

A useful Habitat corridor test should make the derived-spatialization boundary obvious.

### Positive path

- corridor identity and role are explicit;
- connectivity-edge linkage, patch-pair refs, node/edge group refs, or model-run linkage is explicit;
- geometry posture is visible and public-safe state is explicit;
- method, model run, config digest, input digest, output digest, CRS/resolution, and run time are visible where material;
- uncertainty and weakest-input caveats are visible;
- source roles and sensitivity posture are preserved;
- evidence, policy, review, release relationship, correction, and rollback references are linkable where material.

### Negative path

- corridor cannot become observed animal movement;
- corridor cannot become transport corridor, regulatory designation, or management instruction;
- corridor geometry cannot hide provenance, uncertainty, or sensitivity posture;
- test pass cannot become release approval;
- map style, tile, popup, graph edge, Focus Mode answer, or AI text cannot become corridor authority;
- missing evidence produces `ABSTAIN` rather than a fluent claim.

---

## Finite outcomes

| Condition | Expected outcome |
|---|---|
| Valid synthetic derived corridor with linkage, evidence, model run, uncertainty, policy, review, release relationship, correction, and rollback context | accepted derived support only. |
| Missing corridor identity, geometry posture, derivation method, input support, or model-run receipt | validation failure / `ERROR` / `ABSTAIN`. |
| Missing uncertainty or public-safe geometry posture | review required / `ABSTAIN` / `DENY`. |
| Corridor treated as observed movement, transport corridor, regulatory designation, management instruction, or source truth | validation failure. |
| Public-facing candidate lacks release/correction/rollback posture | promotion-blocking failure. |
| Policy engine unavailable | `ERROR` or `ABSTAIN`, never public exposure. |

---

## Forbidden shortcuts

Do not use this test lane to:

- fetch live upstream source systems;
- store real source exports, lifecycle data, real route/corridor geometry, public tiles, or release artifacts;
- store proof packs, release manifests, or generated public layers;
- redefine Habitat corridor doctrine, contracts, schemas, fixtures, policy rules, receipts, proofs, release decisions, renderer code, or production code;
- bypass model-run receipt, uncertainty, evidence, validation, policy, review, correction, or rollback checks with a fixture flag;
- infer release state from file existence, test success, layer name, graph edge, map rendering, tile availability, or AI wording;
- publish, promote, or release anything.

Any test that needs real model outputs, source data, or public tile output belongs in a gated integration tier with source admission, lifecycle state, policy, receipts, release controls, and rollback targets.

---

## Suggested layout

The exact test module names remain **NEEDS VERIFICATION** until the runner and existing conventions are inspected.

```text
tests/domains/habitat/test_corridor/
├── README.md
├── test_corridor_identity.py
├── test_connectivity_linkage_required.py
├── test_geometry_posture.py
├── test_derived_not_observed_route.py
├── test_model_run_and_uncertainty_required.py
├── test_public_safe_geometry.py
├── test_sensitive_input_inheritance.py
└── test_release_correction_rollback.py
```

---

## Run posture

```bash
pytest tests/domains/habitat/test_corridor
```

Status of the command above: **PROPOSED / NEEDS VERIFICATION**. It assumes `pytest` is the accepted test runner and that executable test modules exist. This README does not claim the command currently passes.

---

## Evidence ledger

| Evidence | Status | Supports | Limits |
|---|---|---|---|
| Previous target file | CONFIRMED | `tests/domains/habitat/test_corridor/README.md` existed as a blank placeholder before this replacement. | Did not define the lane. |
| `tests/README.md` | CONFIRMED | `tests/` is enforceability proof and failure should block promotion where trust-spine checks fail. | Does not prove this lane's modules or pass rate. |
| `docs/domains/habitat/sublanes/connectivity.md` | CONFIRMED doctrine / PROPOSED implementation | Connectivity products are derived; `ConnectivityEdge` and `Corridor` are Habitat-owned object families; derived outputs do not become canonical truth; sensitive movement detail is denied by default. | Implementation paths, validators, fixtures, schemas, policy runtime, release artifacts, UI, Focus Mode, and CI remain NEEDS VERIFICATION. |
| `contracts/domains/habitat/corridor.md` | CONFIRMED semantic contract / PROPOSED implementation | Defines `Corridor` as derived Habitat spatialization with geometry posture, model-run support, uncertainty, sensitivity, public-safe geometry, release, correction, and rollback controls; not observed movement, transport corridor, regulatory designation, management instruction, public layer, or release manifest by itself. | Schema is a permissive scaffold; field-level enforcement remains NEEDS VERIFICATION. |
| `contracts/domains/habitat/connectivity_edge.md` | CONFIRMED semantic contract / PROPOSED implementation | Defines `ConnectivityEdge` as the relation that a corridor may spatialize; edge and corridor must remain separate object families. | Schema is a permissive scaffold; field-level enforcement remains NEEDS VERIFICATION. |

---

## Validation checklist

Before treating this README as implemented behavior, verify:

- [ ] Executable test modules exist under this lane.
- [ ] Test runner and import paths match the repo's accepted convention.
- [ ] Synthetic fixtures exist for valid corridor, missing linkage, missing geometry posture, missing receipt, missing uncertainty, sensitive input inheritance, corridor-as-movement, corridor-as-transport, corridor-as-regulatory, missing public-safe geometry, and missing release/correction/rollback cases.
- [ ] Corridor schema path and field expectations are accepted beyond scaffold status.
- [ ] EvidenceRef / EvidenceBundle behavior is available to tests or safely stubbed.
- [ ] ModelRunReceipt and UncertaintySurface behavior is available to tests or safely stubbed.
- [ ] PolicyDecision, ReviewRecord, ReleaseManifest, CorrectionNotice, RedactionReceipt, and RollbackCard expectations are defined before enforcing them.
- [ ] CI runs the no-network Habitat corridor suite.
- [ ] Failures block public carrier promotion or release candidate approval.

---

## Rollback

Rollback is required if this lane becomes a source export store, route/corridor data store, lifecycle data store, fixture root, contract root, schema authority, policy authority, proof store, release-decision root, public map/API/tile surface, AI surface, renderer implementation, pipeline implementation, or publication shortcut.

Rollback target for this replacement: previous blank blob SHA `8b137891791fe96927ad78e64b0aad7bded08bdc`.

<p align="right"><a href="#top">Back to top</a></p>
