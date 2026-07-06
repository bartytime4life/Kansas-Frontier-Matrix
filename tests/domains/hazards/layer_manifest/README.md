<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-domains-hazards-layer-manifest-readme
title: Hazards LayerManifest Test README
type: test-readme
version: v0.1
status: draft; placeholder-expanded; layer-manifest-test-lane; PROPOSED / NEEDS VERIFICATION before promotion
owners:
  - OWNER_TBD — Hazards domain steward
  - OWNER_TBD — Map shell steward
  - OWNER_TBD — Evidence steward
  - OWNER_TBD — Policy steward
  - OWNER_TBD — Release steward
  - OWNER_TBD — Validation steward
  - OWNER_TBD — QA steward
created: NEEDS VERIFICATION — blank placeholder existed before v0.1 expansion
updated: 2026-07-05
policy_label: public-doc; tests; hazards; layer-manifest; no-network; planning-context; evidence-bound; policy-filtered; release-gated; freshness-aware; rollback-aware
tags: [kfm, tests, hazards, layer-manifest, LayerManifest, TileArtifactManifest, MapReleaseManifest, EvidenceBundle, EvidenceRef, PolicyDecision, ReleaseManifest, CorrectionNotice, RollbackCard, freshness, source-role, ABSTAIN, DENY, ERROR]
related:
  - ../../../README.md
  - ../README.md
  - ../drawer/README.md
  - ../feature_resolver/README.md
  - ../../../../docs/domains/hazards/MAP_UI_CONTRACTS.md
  - ../../../../docs/domains/hazards/LIFE_SAFETY_BOUNDARY.md
  - ../../../../contracts/release/release_manifest.md
  - ../../../../contracts/policy/policy_decision.md
  - ../../../../contracts/evidence/evidence_bundle.md
  - ../../../../schemas/contracts/v1/map/
  - ../../../../schemas/contracts/v1/domains/hazards/
  - ../../../../fixtures/domains/hazards/layer_manifest/
  - ../../../../policy/domains/hazards/
  - ../../../../release/manifests/hazards/
notes:
  - "This file replaces a blank placeholder at tests/domains/hazards/layer_manifest/README.md."
  - "This is a test-lane README only. It does not define Hazards doctrine, map/UI contracts, LayerManifest schemas, fixtures, lifecycle records, EvidenceBundles, policy rules, release decisions, public API material, public map material, public tiles, or published artifacts."
  - "The tested invariant is that Hazards LayerManifest tests verify released-layer metadata before public map use: object family, source role, evidence ref field, temporal fields, policy label, release state, planning/context label, freshness fields, official-source referral posture where required, correction, and rollback remain visible without turning the manifest into source truth, policy authority, release authority, public-layer truth, or AI/UI truth."
  - "Default posture is deterministic and no-network. Live source checks, real source exports, lifecycle data, and public tiles do not belong in this lane."
  - "Rollback target for this replacement is previous blank blob SHA 8b137891791fe96927ad78e64b0aad7bded08bdc."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Hazards LayerManifest tests

> Deterministic, no-network test documentation for proving that Hazards `LayerManifest` records preserve source-role, evidence, policy, freshness, release, correction, and rollback posture before map/UI use.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: tests" src="https://img.shields.io/badge/root-tests%2F-blue">
  <img alt="Domain: hazards" src="https://img.shields.io/badge/domain-hazards-critical">
  <img alt="Lane: layer manifest" src="https://img.shields.io/badge/lane-layer__manifest-blue">
  <img alt="Network: disabled by default" src="https://img.shields.io/badge/network-disabled__by__default-critical">
  <img alt="Boundary: manifest not authority" src="https://img.shields.io/badge/boundary-manifest__not__authority-success">
</p>

**Path:** `tests/domains/hazards/layer_manifest/README.md`  
**Status:** draft / placeholder-expanded / PROPOSED until executable tests are verified  
**Owning root:** `tests/`  
**Domain segment:** `hazards`  
**Test lane:** `layer_manifest`  
**Default execution posture:** deterministic, synthetic, no-network, public-safe fixtures only  
**Truth posture:** CONFIRMED target was a blank placeholder before this expansion · CONFIRMED `tests/` is the canonical root for enforceability proof · CONFIRMED Hazards map/UI doctrine routes public UI through released layer → governed API → EvidenceBundle → Evidence Drawer → Focus Mode and requires a planning/context boundary label before render · CONFIRMED Hazards LayerManifest doctrine requires hazards-specific fields for object family, source role, evidence refs, temporal fields, policy label, release state, freshness, and rollback · NEEDS VERIFICATION for executable test modules, fixture payload inventory, schema enforcement, validator behavior, policy runtime, release integration, UI behavior, CI coverage, and pass rates.

---

## Purpose

`tests/domains/hazards/layer_manifest/` is the intended home for Hazards layer-manifest tests.

This lane should prove that a hazards layer can enter public map/UI flow only with governed layer metadata: object family, source role, evidence reference field, temporal fields, policy label, release state, freshness fields where material, planning/context label, correction posture, and rollback target.

A passing test here should **not** mean that a real hazards source is current, a public layer is safe, tiles are published, or a release is approved. It should mean only that layer-manifest guardrails behaved as expected against bounded fixtures.

---

## Placement basis

`tests/` is the canonical root for enforceability proof. Hazards is a domain segment inside that root. `layer_manifest/` is a test lane, not a map implementation folder, schema home, policy home, release home, data store, proof store, public API surface, or public map surface.

| Responsibility | Correct home | This lane's relationship |
|---|---|---|
| Hazards layer-manifest tests | `tests/domains/hazards/layer_manifest/` | This directory. |
| Hazards map/UI doctrine | `docs/domains/hazards/MAP_UI_CONTRACTS.md` | Doctrine under test; not redefined here. |
| Drawer tests | `tests/domains/hazards/drawer/` | Downstream trust projection tests. |
| Feature resolver tests | `tests/domains/hazards/feature_resolver/` | Downstream feature-resolution tests. |
| Machine schemas | `schemas/contracts/v1/map/`, `schemas/contracts/v1/domains/hazards/` | Shape checks where accepted. |
| Synthetic fixtures | `fixtures/domains/hazards/layer_manifest/` | Preferred toy manifests and expected outcomes if populated. |
| Policy homes | `policy/domains/hazards/` | Referenced by tests, not bypassed here. |
| Release decisions | `release/` and `release/manifests/hazards/` | Publication, correction, and rollback authority; tests cannot replace it. |

---

## Invariant under test

> **The layer manifest is a release-gated map contract, not truth authority.** A Hazards `LayerManifest` may describe a public-safe layer only when source role, evidence, policy, time, release, correction, and rollback posture are explicit. It must not infer authority from a layer name, map style, tile availability, or test success.

Core checks:

| Check | Required behavior | Failure outcome |
|---|---|---|
| Layer identity | Layer ID, title, domain, object family, geometry type, and version/digest posture are explicit. | validation failure / `ERROR`. |
| Source role | Canonical source role is explicit and never silently upgraded. | validation failure / `ABSTAIN`. |
| Context label | Hazards planning/context boundary label is present where required. | `DENY` / validation failure. |
| Evidence field | Manifest names the evidence reference field needed for downstream click resolution. | validation failure / `ABSTAIN`. |
| Time fields | Source, observed, valid, retrieval, release, correction, issue, expiry, stale, or accepted temporal fields are explicit where material. | validation failure. |
| Policy and release | Policy label, release state, review/release relationship, and rollback target are visible. | promotion block. |
| Freshness gate | Operational-context fixtures include freshness and expiry posture where material. | `DENY` / validation failure. |
| No authority upgrade | Manifest cannot become source truth, policy authority, release authority, public-layer truth, drawer truth, or AI truth. | validation failure / `ABSTAIN`. |

---

## Expected scope

Tests in this lane may validate:

- valid synthetic Hazards `LayerManifest` fixture shape;
- missing object family, source role, evidence-ref field, temporal fields, policy label, release state, context label, freshness field, or rollback target;
- stale/expired operational-context denial behavior where material;
- source-role anti-collapse for observed, regulatory, modeled, aggregate, historical, administrative, and candidate fixtures;
- rejection of manifests that point to internal lifecycle data, unreleased candidates, public tiles without release, or missing rollback context;
- preservation of correction and rollback metadata before downstream feature resolver or drawer use.

Live source checks, real source exports, production credentials, public tile generation, and real-world incident payloads are out of scope for the default suite.

---

## Fixture posture

Use synthetic, public-safe fixtures only.

Fixture requirements:

- deterministic and no-network;
- compact enough for review in a PR;
- explicit expected outcome;
- explicit layer ID, object family, source role, evidence field, time fields, policy state, release relationship, correction, and rollback posture where material;
- no real source exports, lifecycle data, public tiles, credentials, or published artifacts.

---

## Finite outcomes

| Condition | Expected outcome |
|---|---|
| Valid synthetic hazards manifest with source role, evidence field, policy, release, correction, and rollback context | accepted manifest support only. |
| Missing object family or source role | validation failure / `ABSTAIN`. |
| Missing evidence-ref field | validation failure / `ABSTAIN`. |
| Missing context label where required | `DENY` / validation failure. |
| Stale or expired context presented as current | `DENY` / validation failure. |
| Release state is not published or rollback target is missing | promotion-blocking failure. |
| Manifest treated as source truth, policy decision, release authority, or public-layer truth | validation failure. |
| Policy engine unavailable | `ERROR` or `ABSTAIN`, never public exposure. |

---

## Suggested layout

```text
tests/domains/hazards/layer_manifest/
├── README.md
├── test_layer_manifest_identity.py
├── test_source_role_required.py
├── test_evidence_ref_field_required.py
├── test_temporal_and_freshness_fields.py
├── test_context_label_required.py
├── test_release_and_rollback_required.py
└── test_manifest_not_authority.py
```

---

## Run posture

```bash
pytest tests/domains/hazards/layer_manifest
```

Status of the command above: **PROPOSED / NEEDS VERIFICATION**. It assumes `pytest` is the accepted test runner and that executable test modules exist. This README does not claim the command currently passes.

---

## Evidence ledger

| Evidence | Status | Supports | Limits |
|---|---|---|---|
| Previous target file | CONFIRMED | `tests/domains/hazards/layer_manifest/README.md` existed as a blank placeholder before this replacement. | Did not define the lane. |
| `tests/README.md` | CONFIRMED | `tests/` is enforceability proof and failure should block promotion where trust-spine checks fail. | Does not prove this lane's modules or pass rate. |
| `docs/domains/hazards/MAP_UI_CONTRACTS.md` | CONFIRMED doctrine | Hazards public flow starts from released layer and requires hazards-specific `LayerManifest` fields, context labels, temporal fields, evidence refs, release state, and rollback target. | Concrete validators, fixtures, route behavior, and pass rates remain NEEDS VERIFICATION. |
| Repo search | CONFIRMED | No dedicated Hazards layer-manifest test README was found in searched terms before this replacement. | Search is not proof of absence. |

---

## Validation checklist

- [ ] Executable test modules exist under this lane.
- [ ] Test runner and import paths match the repo's accepted convention.
- [ ] Synthetic fixtures exist for valid manifest, missing object family, missing source role, missing evidence field, missing time fields, missing context label, stale context, missing release, and missing rollback cases.
- [ ] Active LayerManifest schema path is accepted or safely stubbed.
- [ ] EvidenceRef / EvidenceBundle behavior is available to tests or safely stubbed.
- [ ] PolicyDecision behavior is available to tests or safely stubbed.
- [ ] ReleaseManifest, CorrectionNotice, RedactionReceipt, and RollbackCard expectations are defined before enforcing them.
- [ ] CI runs the no-network Hazards layer-manifest suite.
- [ ] Failures block public carrier promotion or release candidate approval where material.

---

## Rollback

Rollback is required if this lane becomes a live source-fetcher, lifecycle data store, fixture authority, contract root, schema authority, policy authority, proof store, release-decision root, public map/API/tile surface, AI surface, renderer implementation, pipeline implementation, or publication shortcut.

Rollback target for this replacement: previous blank blob SHA `8b137891791fe96927ad78e64b0aad7bded08bdc`.

<p align="right"><a href="#top">Back to top</a></p>
