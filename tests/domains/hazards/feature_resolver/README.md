<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-domains-hazards-feature-resolver-readme
title: Hazards Feature Resolver Test README
type: test-readme
version: v0.1
status: draft; placeholder-expanded; feature-resolver-test-lane; PROPOSED / NEEDS VERIFICATION before promotion
owners:
  - OWNER_TBD — Hazards domain steward
  - OWNER_TBD — Governed API steward
  - OWNER_TBD — UI steward
  - OWNER_TBD — Evidence steward
  - OWNER_TBD — Policy steward
  - OWNER_TBD — Validation steward
  - OWNER_TBD — Release steward
  - OWNER_TBD — QA steward
created: NEEDS VERIFICATION — blank placeholder existed before v0.1 expansion
updated: 2026-07-05
policy_label: public-doc; tests; hazards; feature-resolver; no-network; governed-api; planning-context; evidence-bound; policy-filtered; release-gated; finite-outcomes; rollback-aware
tags: [kfm, tests, hazards, feature-resolver, governed-api, EvidenceDrawerPayload, EvidenceBundle, EvidenceRef, PolicyDecision, RuntimeResponseEnvelope, ReleaseManifest, CorrectionNotice, RollbackCard, trust-membrane, ABSTAIN, DENY, ERROR]
related:
  - ../../../README.md
  - ../README.md
  - ../drawer/README.md
  - ../../../../docs/domains/hazards/MAP_UI_CONTRACTS.md
  - ../../../../docs/architecture/ui/EVIDENCE_DRAWER.md
  - ../../../../contracts/ui/evidence_drawer_payload.md
  - ../../../../contracts/runtime/runtime_response_envelope.md
  - ../../../../contracts/policy/policy_decision.md
  - ../../../../contracts/release/release_manifest.md
  - ../../../../schemas/contracts/v1/domains/hazards/
  - ../../../../schemas/contracts/v1/ui/evidence_drawer_payload.schema.json
  - ../../../../fixtures/domains/hazards/feature_resolver/
  - ../../../../policy/domains/hazards/
  - ../../../../release/manifests/hazards/
notes:
  - "This file replaces a blank placeholder at tests/domains/hazards/feature_resolver/README.md."
  - "This is a test-lane README only. It does not define Hazards doctrine, governed API routes, resolver contracts, schemas, fixtures, lifecycle records, EvidenceBundles, policy rules, release decisions, public API material, public map material, public tiles, or published artifacts."
  - "The tested invariant is that Hazards feature-resolver tests verify governed click or feature resolution for released or fixture-scoped hazards features: feature identity, layer identity, evidence refs, policy state, freshness state, context labels, release relationship, correction, and rollback remain visible without turning the resolver into source truth, policy authority, release authority, public-layer truth, or AI/UI truth."
  - "Default posture is deterministic and no-network. Live source checks, real source exports, lifecycle data, and public tiles do not belong in this lane."
  - "Rollback target for this replacement is previous blank blob SHA 8b137891791fe96927ad78e64b0aad7bded08bdc."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Hazards feature-resolver tests

> Deterministic, no-network test documentation for proving that Hazards feature resolution preserves feature identity, layer identity, evidence support, policy state, freshness state, release posture, correction paths, and rollback targets before drawer or Focus Mode use.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: tests" src="https://img.shields.io/badge/root-tests%2F-blue">
  <img alt="Domain: hazards" src="https://img.shields.io/badge/domain-hazards-critical">
  <img alt="Lane: feature resolver" src="https://img.shields.io/badge/lane-feature__resolver-blue">
  <img alt="Network: disabled by default" src="https://img.shields.io/badge/network-disabled__by__default-critical">
  <img alt="Boundary: resolver not authority" src="https://img.shields.io/badge/boundary-resolver__not__authority-success">
</p>

**Path:** `tests/domains/hazards/feature_resolver/README.md`  
**Status:** draft / placeholder-expanded / PROPOSED until executable tests are verified  
**Owning root:** `tests/`  
**Domain segment:** `hazards`  
**Test lane:** `feature_resolver`  
**Default execution posture:** deterministic, synthetic, no-network, public-safe fixtures only  
**Truth posture:** CONFIRMED target was a blank placeholder before this expansion · CONFIRMED `tests/` is the canonical root for enforceability proof · CONFIRMED Hazards map/UI contracts describe a governed flow from released layer to governed API to Evidence Drawer and Focus Mode · CONFIRMED Hazards surfaces must carry planning/context boundary labels · NEEDS VERIFICATION for executable test modules, fixture payload inventory, schema enforcement, validator behavior, route behavior, policy runtime, release integration, UI behavior, CI coverage, and pass rates.

---

## Purpose

`tests/domains/hazards/feature_resolver/` is the intended home for Hazards feature-resolver tests.

This lane should prove that a clicked or requested hazards feature is resolved only through governed inputs: released or fixture-scoped feature refs, layer refs, source-role posture, evidence refs, policy state, freshness state, release relationship, correction path, and rollback target.

A passing test here should **not** mean that a real hazards source is current, a public feature is safe, a drawer payload is complete, or a release is approved. It should mean only that feature-resolver guardrails behaved as expected against bounded fixtures.

---

## Placement basis

`tests/` is the canonical root for enforceability proof. Hazards is a domain segment inside that root. `feature_resolver/` is a test lane, not a governed API implementation folder, schema home, policy home, release home, data store, proof store, public API surface, or public map surface.

| Responsibility | Correct home | This lane's relationship |
|---|---|---|
| Hazards feature-resolver tests | `tests/domains/hazards/feature_resolver/` | This directory. |
| Hazards map/UI doctrine | `docs/domains/hazards/MAP_UI_CONTRACTS.md` | Doctrine under test; not redefined here. |
| Drawer tests | `tests/domains/hazards/drawer/` | Downstream payload tests; not replaced here. |
| Evidence Drawer architecture | `docs/architecture/ui/EVIDENCE_DRAWER.md` | Downstream trust-panel doctrine. |
| Runtime finite outcomes | `contracts/runtime/runtime_response_envelope.md` | Expected envelope behavior where accepted. |
| UI drawer payload | `contracts/ui/evidence_drawer_payload.md` | Downstream projection contract; resolver should not duplicate it. |
| Synthetic fixtures | `fixtures/domains/hazards/feature_resolver/` | Preferred toy inputs and expected outcomes if populated. |
| Policy homes | `policy/domains/hazards/` | Referenced by tests, not bypassed here. |
| Release decisions | `release/` and `release/manifests/hazards/` | Publication, correction, and rollback authority; tests cannot replace it. |

---

## Invariant under test

> **The feature resolver is a governed bridge, not a truth source.** It accepts a released or fixture-scoped feature request and returns a finite governed result for downstream drawer or Focus Mode use. It must not infer stronger authority from map rendering or turn a feature ID into a claim without evidence, policy, release, correction, and rollback context.

Core checks:

| Check | Required behavior | Failure outcome |
|---|---|---|
| Feature identity | Feature ID, layer ID, domain, and request context are explicit. | validation failure / `ERROR`. |
| Release posture | Resolver input is released, fixture-scoped, or explicitly denied/abstained. | `DENY` / `ABSTAIN`. |
| Evidence support | Evidence refs or bundle refs are present for consequential claims, or a finite non-answer is returned. | `ABSTAIN`. |
| Policy state | Allow/restrict/deny/abstain/error style decision state remains visible. | validation failure / `ERROR`. |
| Freshness state | Retrieval, validity, stale, no-data, or correction posture is explicit where material. | `DENY` / `ABSTAIN`. |
| Source-role posture | Observed, modeled, regulatory, historical, aggregate, or candidate posture remains visible where material. | validation failure. |
| Trust membrane | Resolver does not expose internal lifecycle, proof, or candidate material as authority. | validation failure. |
| No authority upgrade | Resolver result cannot become source truth, policy authority, release authority, public-layer truth, drawer truth, or AI truth. | validation failure / `ABSTAIN`. |

---

## Expected scope

Tests in this lane may validate:

- valid synthetic feature-resolution request and finite response cases;
- missing feature ID, missing layer ID, missing release posture, missing evidence, missing policy, stale context, and unknown source-role cases;
- blocking of internal or unreleased references;
- preservation of context labels and source-role badges for downstream drawer payloads;
- correction and rollback metadata before downstream UI use.

Live source checks, real source exports, production credentials, public tile generation, and real-world payloads are out of scope for the default suite.

---

## Suggested layout

```text
tests/domains/hazards/feature_resolver/
├── README.md
├── test_feature_request_identity.py
├── test_release_posture_required.py
├── test_evidence_and_policy_required.py
├── test_freshness_state.py
├── test_source_role_preserved.py
├── test_trust_membrane_blocks_internal_refs.py
└── test_release_correction_rollback.py
```

---

## Run posture

```bash
pytest tests/domains/hazards/feature_resolver
```

Status of the command above: **PROPOSED / NEEDS VERIFICATION**. It assumes `pytest` is the accepted test runner and that executable test modules exist. This README does not claim the command currently passes.

---

## Evidence ledger

| Evidence | Status | Supports | Limits |
|---|---|---|---|
| Previous target file | CONFIRMED | `tests/domains/hazards/feature_resolver/README.md` existed as a blank placeholder before this replacement. | Did not define the lane. |
| `tests/README.md` | CONFIRMED | `tests/` is enforceability proof and failure should block promotion where trust-spine checks fail. | Does not prove this lane's modules or pass rate. |
| `docs/domains/hazards/MAP_UI_CONTRACTS.md` | CONFIRMED doctrine | Hazards content reaches public UI through released layer, governed API, EvidenceBundle, Evidence Drawer, and Focus Mode flow with context labeling. | Concrete route names, validators, fixtures, and pass rates remain NEEDS VERIFICATION. |
| `tests/domains/hazards/drawer/README.md` | CONFIRMED adjacent lane | Drawer tests cover downstream EvidenceDrawerPayload projection behavior. | Does not prove resolver behavior. |
| Repo search | CONFIRMED | No dedicated feature-resolver Hazards doc was found in searched terms before this replacement. | Search is not proof of absence. |

---

## Validation checklist

- [ ] Executable test modules exist under this lane.
- [ ] Test runner and import paths match the repo's accepted convention.
- [ ] Synthetic fixtures exist for valid resolver, missing feature ID, missing layer ID, missing evidence, missing policy, stale context, unknown source role, internal-ref block, missing release, and missing rollback cases.
- [ ] Active feature-request/response schema path is accepted or safely stubbed.
- [ ] EvidenceRef / EvidenceBundle behavior is available to tests or safely stubbed.
- [ ] PolicyDecision and RuntimeResponseEnvelope behavior is available to tests or safely stubbed.
- [ ] ReleaseManifest, CorrectionNotice, RedactionReceipt, and RollbackCard expectations are defined before enforcing them.
- [ ] CI runs the no-network Hazards feature-resolver suite.
- [ ] Failures block public carrier promotion or release candidate approval where material.

---

## Rollback

Rollback is required if this lane becomes a live source-fetcher, lifecycle data store, fixture authority, contract root, schema authority, policy authority, proof store, release-decision root, public map/API/tile surface, AI surface, renderer implementation, pipeline implementation, or publication shortcut.

Rollback target for this replacement: previous blank blob SHA `8b137891791fe96927ad78e64b0aad7bded08bdc`.

<p align="right"><a href="#top">Back to top</a></p>
