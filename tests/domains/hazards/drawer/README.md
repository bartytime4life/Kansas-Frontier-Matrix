<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-domains-hazards-drawer-readme
title: Hazards Evidence Drawer Test README
type: test-readme
version: v0.2
status: draft; documentation-only Hazards drawer lane; adjacent general UI projection proof is not Hazards-specific proof
owners:
  - OWNER_TBD — Hazards domain steward
  - OWNER_TBD — UI steward
  - OWNER_TBD — Evidence steward
  - OWNER_TBD — Policy steward
  - OWNER_TBD — Validation steward
  - OWNER_TBD — Release steward
  - OWNER_TBD — QA steward
created: 2026-07-05
updated: 2026-08-30
policy_label: public-doc; tests; hazards; evidence-drawer; no-network; planning-context; evidence-bound; policy-filtered; release-gated; finite-outcomes; rollback-aware
owning_root: tests/
responsibility: Document the Hazards drawer test lane and its verified non-executable state without creating contract, schema, policy, release, runtime, or publication authority.
truth_posture: "CONFIRMED documentation-only Hazards lane; CONFIRMED separate PROPOSED bounded-executable general UI EvidenceDrawerPayload profile; NEEDS VERIFICATION Hazards-specific fixtures, validator, executable tests, stewardship, runtime coupling, and promotion enforcement"
tags: [kfm, tests, hazards, drawer, evidence-drawer, EvidenceDrawerPayload, EvidenceBundle, EvidenceRef, PolicyDecision, RuntimeResponseEnvelope, ReleaseManifest, CorrectionNotice, RollbackCard, trust-membrane, ABSTAIN, DENY, ERROR]
related:
  - ../../../README.md
  - ../README.md
  - ../../../../docs/domains/hazards/MAP_UI_CONTRACTS.md
  - ../../../../docs/domains/hazards/LIFE_SAFETY_BOUNDARY.md
  - ../../../../docs/architecture/ui/EVIDENCE_DRAWER.md
  - ../../../../contracts/ui/evidence_drawer_payload.md
  - ../../../../contracts/evidence/evidence_bundle.md
  - ../../../../contracts/evidence/evidence_ref.md
  - ../../../../contracts/runtime/runtime_response_envelope.md
  - ../../../../contracts/policy/policy_decision.md
  - ../../../../contracts/release/release_manifest.md
  - ../../../../schemas/contracts/v1/ui/evidence_drawer_payload.schema.json
  - ../../../../schemas/contracts/v1/domains/hazards/
  - ../../../../fixtures/domains/hazards/drawer/
  - ../../../../fixtures/ui/evidence_drawer_payload/
  - ../../../../tools/validators/ui/validate_evidence_drawer_payload.py
  - ../../../validators/test_validate_evidence_drawer_payload.py
  - ../../../../policy/domains/hazards/
  - ../../../../release/manifests/hazards/
  - ../../../../.github/workflows/evidence-drawer-payload.yml
notes:
  - "This file replaces a blank placeholder at tests/domains/hazards/drawer/README.md."
  - "This is a test-lane README only. It does not define Hazards doctrine, UI architecture, EvidenceDrawerPayload contracts, schemas, fixtures, lifecycle records, EvidenceBundles, policy rules, release decisions, public API material, public map material, public tiles, or published artifacts."
  - "The tested invariant is that Hazards drawer tests verify trust-visible EvidenceDrawerPayload behavior for released or fixture-scoped hazards claims: planning-context labels, finite outcomes, evidence refs, policy state, freshness state, release relationship, correction, and rollback remain visible without turning the drawer into source truth, policy authority, release authority, public-layer truth, or AI/UI truth."
  - "Default posture is deterministic and no-network. Live source checks, real source exports, lifecycle data, and public tiles do not belong in this lane."
  - "Current Hazards inventory is documentation-only: this test directory and its paired fixture directory each contain only a README and .gitkeep; the documented pytest command collects zero tests and exits 5."
  - "A separate general UI EvidenceDrawerPayload profile has a closed schema, synthetic fixtures, a deterministic validator, tests, and CI; it remains PROPOSED and does not prove Hazards-specific drawer behavior."
  - "Rollback target for this replacement is previous blank blob SHA 8b137891791fe96927ad78e64b0aad7bded08bdc."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Hazards Evidence Drawer tests

> Deterministic, no-network test documentation for proving that Hazards drawer payloads preserve evidence support, policy state, release posture, freshness state, context labels, correction paths, and rollback targets.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: tests" src="https://img.shields.io/badge/root-tests%2F-blue">
  <img alt="Domain: hazards" src="https://img.shields.io/badge/domain-hazards-critical">
  <img alt="Lane: drawer" src="https://img.shields.io/badge/lane-drawer-blue">
  <img alt="Network: disabled by default" src="https://img.shields.io/badge/network-disabled__by__default-critical">
  <img alt="Boundary: drawer not authority" src="https://img.shields.io/badge/boundary-drawer__not__authority-success">
</p>

**Path:** `tests/domains/hazards/drawer/README.md`  
**Status:** draft / DOCUMENTATION_ONLY / NOT_VALIDATION
**Owning root:** `tests/`  
**Domain segment:** `hazards`  
**Test lane:** `drawer`  
**Default execution posture:** deterministic, synthetic, no-network, public-safe fixtures only  
**Truth posture:** CONFIRMED target was a blank placeholder before its v0.1 expansion · CONFIRMED this lane currently contains no executable tests and its paired fixture lane contains no payloads · CONFIRMED a separate general UI `EvidenceDrawerPayload` profile has a closed schema, synthetic fixtures, deterministic validation, tests, and CI · CONFIRMED that profile remains PROPOSED and does not establish Hazards-specific behavior · NEEDS VERIFICATION for Hazards-specific executable tests, fixture payloads, validator behavior, policy runtime, release integration, UI route behavior, CI coverage, and promotion enforcement.

---

## Purpose

`tests/domains/hazards/drawer/` is the intended home for Hazards Evidence Drawer tests.

This lane should prove that a clicked hazards feature, badge, layer assertion, or fixture-scoped hazards claim resolves into a governed drawer payload with evidence refs, source summaries, policy state, release state, freshness or stale-state explanation, correction path, rollback target, and the required hazards context label.

A passing test here should **not** mean that a real hazards source is current, a public layer is safe, or a release is approved. It should mean only that drawer guardrails behaved as expected against bounded fixtures.

---

## Placement basis

`tests/` is the canonical root for enforceability proof. Hazards is a domain segment inside that root. `drawer/` is a test lane, not a UI implementation folder, schema home, policy home, release home, data store, proof store, public API surface, or public map surface.

| Responsibility | Correct home | This lane's relationship |
|---|---|---|
| Hazards drawer tests | `tests/domains/hazards/drawer/` | This directory. |
| Hazards map/UI doctrine | `docs/domains/hazards/MAP_UI_CONTRACTS.md` | Doctrine under test; not redefined here. |
| Evidence Drawer architecture | `docs/architecture/ui/EVIDENCE_DRAWER.md` | UI trust-panel doctrine under test. |
| UI payload meaning | `contracts/ui/evidence_drawer_payload.md` | Projection contract under test. |
| Machine schemas | `schemas/contracts/v1/ui/`, `schemas/contracts/v1/domains/hazards/` | Shape checks where accepted. |
| Synthetic fixtures | `fixtures/domains/hazards/drawer/` | Preferred toy payloads and expected outcomes if populated. |
| Policy homes | `policy/domains/hazards/` | Referenced by tests, not bypassed here. |
| Release decisions | `release/` and `release/manifests/hazards/` | Publication, correction, and rollback authority; tests cannot replace it. |

---

## Invariant under test

> **The hazards drawer is a trust projection.** A Hazards drawer payload may explain a released or fixture-scoped hazards claim only after evidence, policy, release, freshness, correction, and rollback state are visible. It must not upgrade UI text into truth.

Core checks:

| Check | Required behavior | Failure outcome |
|---|---|---|
| Payload identity | Drawer payload ID, source feature/layer ref, domain, and payload version are explicit. | validation failure / `ERROR`. |
| Context label | Hazards context is clearly labeled with the required planning/context boundary. | `DENY` / validation failure. |
| Evidence support | Evidence refs or bundle refs are present for consequential claims, or a finite non-answer is returned. | `ABSTAIN`. |
| Policy state | Allow/restrict/deny/abstain/error style decision state remains visible. | validation failure / `ERROR`. |
| Freshness state | Time state, expiry, retrieval, validity, stale, or no-data posture is explicit where material. | `DENY` / `ABSTAIN`. |
| Source-role posture | Observed, modeled, regulatory, historical, aggregate, or candidate posture remains visible where material. | validation failure. |
| Release boundary | Review, release, correction, and rollback remain separate from drawer rendering and test pass state. | promotion block. |
| No authority upgrade | Drawer payload cannot become source truth, policy authority, release authority, public-layer truth, or AI truth. | validation failure / `ABSTAIN`. |

---

## Expected scope

Tests in this lane may validate:

- valid Hazards `EvidenceDrawerPayload` fixture shape and trust-state rendering requirements;
- required planning/context label for hazards surfaces;
- finite outcomes for missing evidence, missing policy, stale time state, unknown source role, missing release relationship, or missing rollback target;
- source-role preservation across observed, modeled, regulatory, historical, aggregate, candidate, and synthetic fixture cases;
- rejection of payloads that read internal lifecycle data, proof stores, source feeds, or unreleased candidates directly;
- preservation of correction and rollback metadata for public-facing drawer content.

Live source checks, real source exports, production credentials, public tile generation, and real-world incident payloads are out of scope for the default suite.

---

## Fixture posture

Use synthetic, public-safe fixtures only.

Fixture requirements:

- deterministic and no-network;
- compact enough for review in a PR;
- explicit expected outcome;
- explicit payload ID, feature/layer ref, source role, evidence posture, policy state, freshness state, release relationship, correction, and rollback posture where material;
- no real source exports, lifecycle data, public tiles, credentials, or published artifacts.

---

## Finite outcomes

| Condition | Expected outcome |
|---|---|
| Valid synthetic hazards drawer payload with evidence, policy, freshness, release, correction, and rollback context | accepted drawer support only. |
| Missing evidence for consequential claim | `ABSTAIN`. |
| Missing required context label | `DENY` / validation failure. |
| Stale context presented as current | `DENY` / validation failure. |
| Unknown source role | hold / `ABSTAIN` / validation failure. |
| Drawer payload treated as EvidenceBundle, policy decision, release manifest, or source truth | validation failure. |
| Public-facing candidate lacks release/correction/rollback posture | promotion-blocking failure. |
| Policy engine unavailable | `ERROR` or `ABSTAIN`, never public exposure. |

---

## Suggested layout

```text
tests/domains/hazards/drawer/
├── README.md
├── test_drawer_payload_identity.py
├── test_context_label_required.py
├── test_evidence_and_policy_required.py
├── test_freshness_state.py
├── test_source_role_preserved.py
├── test_payload_not_authority.py
└── test_release_correction_rollback.py
```

---

## Run posture

```bash
pytest tests/domains/hazards/drawer
```

Status of the command above: **DOCUMENTATION_ONLY / NOT_VALIDATION**. The directory contains only `.gitkeep` and this README; pytest collects zero tests and exits `5`.

---

## Evidence ledger

| Evidence | Status | Supports | Limits |
|---|---|---|---|
| Previous target file | CONFIRMED | `tests/domains/hazards/drawer/README.md` existed as a blank placeholder before this replacement. | Did not define the lane. |
| `tests/README.md` | CONFIRMED | `tests/` is enforceability proof and failure should block promotion where trust-spine checks fail. | Does not prove this lane's modules or pass rate. |
| `tests/domains/hazards/README.md` | CONFIRMED | The parent distinguishes passing executable Hazards tests from documentation-only child lanes. | Does not prove this lane's future behavior or ownership. |
| Hazards lane inventory | CONFIRMED | This directory contains only `.gitkeep` and this README; the paired fixture directory also contains only `.gitkeep` and its README. | Establishes documentation-only status, not future ownership or behavior. |
| `docs/domains/hazards/MAP_UI_CONTRACTS.md` | CONFIRMED doctrine | Hazards UI surfaces are context material and must use governed API, EvidenceBundle, Evidence Drawer, Focus Mode, and finite deny/abstain/error states where needed. | Concrete routes, validators, fixtures, and pass rates remain NEEDS VERIFICATION. |
| `docs/architecture/ui/EVIDENCE_DRAWER.md` | CONFIRMED doctrine / PROPOSED implementation | Evidence Drawer is a trust panel that resolves clicked claims to evidence and does not create truth. | Implementation maturity and schema fields remain NEEDS VERIFICATION. |
| General UI `EvidenceDrawerPayload` profile | CONFIRMED bounded executable / PROPOSED profile | The UI contract, closed schema, 11 valid and nine invalid synthetic fixtures, deterministic validator, ten focused tests, and dedicated workflow provide separate projection-shape proof. | It is not Hazards-specific test or fixture proof; final object-family home, upstream evidence/policy authenticity, runtime coupling, release enforcement, deployment, and publication remain unverified. |

---

## Validation checklist

- [ ] Executable test modules exist under this lane.
- [ ] Test runner and import paths match the repo's accepted convention.
- [ ] Synthetic fixtures exist for valid payload, missing evidence, missing context label, stale context, unknown source role, missing policy, missing release, and missing rollback cases.
- [ ] Active EvidenceDrawerPayload schema path and Hazards drawer fixture shape are accepted.
- [ ] EvidenceRef / EvidenceBundle behavior is available to tests or safely stubbed.
- [ ] PolicyDecision and RuntimeResponseEnvelope behavior is available to tests or safely stubbed.
- [ ] ReleaseManifest, CorrectionNotice, RedactionReceipt, and RollbackCard expectations are defined before enforcing them.
- [ ] CI runs the no-network Hazards drawer suite.
- [ ] Failures block public carrier promotion or release candidate approval where material.

---

## Rollback

Rollback is required if this lane becomes a live source-fetcher, lifecycle data store, fixture authority, contract root, schema authority, policy authority, proof store, release-decision root, public map/API/tile surface, AI surface, renderer implementation, pipeline implementation, or publication shortcut.

Rollback target for this replacement: previous blank blob SHA `8b137891791fe96927ad78e64b0aad7bded08bdc`.

<p align="right"><a href="#top">Back to top</a></p>
