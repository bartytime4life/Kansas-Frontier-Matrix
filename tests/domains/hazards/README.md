<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-domains-hazards-readme
title: Hazards Domain Tests README
type: test-index-readme
version: v0.1
status: draft; stub-expanded; parent-index; PROPOSED / NEEDS VERIFICATION before promotion
owners:
  - OWNER_TBD — Hazards domain steward
  - OWNER_TBD — Evidence steward
  - OWNER_TBD — Source steward
  - OWNER_TBD — Policy steward
  - OWNER_TBD — Validation steward
  - OWNER_TBD — Release steward
  - OWNER_TBD — QA steward
created: NEEDS VERIFICATION — greenfield stub existed before v0.1 expansion
updated: 2026-07-05
policy_label: public-doc; tests; hazards; parent-index; no-network; evidence-bound; source-role-aware; policy-filtered; finite-outcomes; release-gated; rollback-aware
tags: [kfm, tests, hazards, parent-index, enforceability, no-network, fixtures, LayerManifest, EvidenceDrawerPayload, FocusModeResponse, EvidenceBundle, PolicyDecision, ReleaseManifest, CorrectionNotice, RollbackCard, ABSTAIN, DENY, ERROR]
related:
  - ../../README.md
  - ../README.md
  - drawer/README.md
  - feature_resolver/README.md
  - focus/README.md
  - focus/emergency_alert_denial/README.md
  - layer_manifest/README.md
  - source_role_anti_collapse_test/README.md
  - ../../../docs/domains/hazards/README.md
  - ../../../docs/domains/hazards/MAP_UI_CONTRACTS.md
  - ../../../docs/domains/hazards/LIFE_SAFETY_BOUNDARY.md
  - ../../../docs/domains/hazards/DATA_LIFECYCLE.md
  - ../../../docs/domains/hazards/IDENTITY_MODEL.md
  - ../../../docs/domains/hazards/SOURCE_REGISTRY.md
  - ../../../contracts/domains/hazards/
  - ../../../schemas/contracts/v1/domains/hazards/
  - ../../../schemas/contracts/v1/map/
  - ../../../schemas/contracts/v1/ui/
  - ../../../schemas/contracts/v1/runtime/
  - ../../../fixtures/domains/hazards/
  - ../../../policy/domains/hazards/
  - ../../../release/manifests/hazards/
notes:
  - "This file replaces the greenfield stub at tests/domains/hazards/README.md."
  - "This is a parent test index only. It does not define Hazards doctrine, contracts, schemas, fixtures, source descriptors, lifecycle records, EvidenceBundles, policy rules, release decisions, public API material, public map material, public tiles, or published artifacts."
  - "The tested parent invariant is that Hazards tests prove enforceable trust boundaries across layer manifests, feature resolution, Evidence Drawer payloads, Focus Mode outcomes, source-role anti-collapse, freshness/context state, policy posture, release relationship, correction, and rollback."
  - "Default posture is deterministic and no-network. Live source checks, real source exports, live feeds, lifecycle data, public tiles, and restricted records do not belong in default Hazards tests."
  - "Rollback target for this replacement is previous stub blob SHA 1e4180a3df4bffeeb38324b7806b583e6104a725."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Hazards domain tests

> Parent index for Hazards test lanes. These tests should prove that Hazards contracts, schemas, policies, fixtures, source roles, freshness states, public-surface gates, release relationships, correction paths, and rollback targets are enforceable without turning tests into a source feed, release authority, public surface, or generated truth source.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: tests" src="https://img.shields.io/badge/root-tests%2F-blue">
  <img alt="Domain: hazards" src="https://img.shields.io/badge/domain-hazards-critical">
  <img alt="Network: disabled by default" src="https://img.shields.io/badge/network-disabled__by__default-critical">
  <img alt="Boundary: tests not release" src="https://img.shields.io/badge/boundary-tests__not__release-success">
</p>

**Path:** `tests/domains/hazards/README.md`  
**Status:** draft / stub-expanded / parent index / PROPOSED until executable tests are verified  
**Owning root:** `tests/`  
**Domain segment:** `hazards`  
**Default execution posture:** deterministic, synthetic, no-network, public-safe fixtures only  
**Truth posture:** CONFIRMED target was a greenfield stub before this expansion · CONFIRMED `tests/` is the canonical root for enforceability proof · CONFIRMED documented child lanes now exist for drawer payloads, feature resolution, Focus Mode, boundary denial, layer manifests, and source-role anti-collapse · CONFIRMED Hazards map/UI doctrine requires governed public flow, context labeling, source-role visibility, finite outcomes, release relationship, freshness state, correction, and rollback · NEEDS VERIFICATION for executable test modules, fixture payload inventory, validators, policy runtime, release integration, public route/UI behavior, CI coverage, and pass rates.

---

## Purpose

`tests/domains/hazards/` is the Hazards segment of the KFM test tree.

Its job is to prove Hazards boundary discipline. A Hazards test should show that object meaning, source role, machine shape, evidence resolution, policy checks, time/freshness state, review state, release posture, correction path, and rollback target are preserved through a bounded fixture or implementation path.

A passing test in this subtree should **not** mean that a real source is admitted, a real Hazards claim is proven, a public layer is safe, current conditions are validated, or a release is approved. It should mean only that the scoped guardrail behaved as expected.

---

## Parent invariant

> **Hazards tests prove enforceability; they do not become Hazards authority.** The subtree may validate Hazards contracts, schemas, fixtures, policies, source roles, layer manifests, resolver outputs, drawer payloads, Focus outcomes, and release readiness, but it must not become a source registry, lifecycle store, proof store, policy root, release root, public API/map/tile surface, or generated truth surface.

Core checks:

| Check | Required behavior | Failure outcome |
|---|---|---|
| Source-role preservation | Observed, regulatory, modeled, aggregate, administrative, candidate, and synthetic roles remain visible where material. | validation failure / `ABSTAIN`. |
| Evidence support | Evidence-dependent claims resolve support or return a finite non-answer. | `ABSTAIN`. |
| Policy posture | Material policy checks return finite outcomes and fail closed where unresolved. | `DENY` / `ABSTAIN` / `ERROR`. |
| Freshness posture | Time, stale, expiry, retrieval, release, and correction state remain visible where material. | validation failure / `DENY`. |
| Lifecycle boundary | Tests do not read or write raw/work/quarantine/processed/published material as authority unless explicitly in a gated integration tier. | validation failure. |
| Release boundary | Test success does not become release approval, release manifest, correction notice, or rollback card. | promotion block. |
| Public membrane | Public examples use governed, released, public-safe carriers rather than internal stores or fixtures. | validation failure. |
| AI/UI boundary | Generated text and UI carriers remain downstream of evidence, policy, finite outcome, and release posture. | `ABSTAIN` / validation failure. |

---

## Lane index

| Lane | Primary responsibility | Boundary |
|---|---|---|
| [`drawer/`](drawer/README.md) | Hazards `EvidenceDrawerPayload` trust-state tests. | Drawer payload is a projection, not evidence, policy, release, source, public-layer, or AI authority. |
| [`feature_resolver/`](feature_resolver/README.md) | Governed click/feature resolution tests. | Resolver is a bridge to governed evidence and policy, not source truth or release authority. |
| [`focus/`](focus/README.md) | Hazards Focus Mode finite-outcome parent lane. | Focus answers are downstream of evidence and policy; generated wording is not KFM authority. |
| [`focus/emergency_alert_denial/`](focus/emergency_alert_denial/README.md) | Boundary-crossing prompt denial/referral tests. | KFM remains planning/context posture and returns finite denial/referral where required. |
| [`layer_manifest/`](layer_manifest/README.md) | Hazards `LayerManifest` metadata tests. | Manifest is release-gated metadata, not source truth, policy decision, release approval, or public-layer truth. |
| [`source_role_anti_collapse_test/`](source_role_anti_collapse_test/README.md) | Canonical source-role preservation tests. | Roles remain first-class identity attributes and cannot collapse across map, drawer, resolver, Focus, release, or AI paths. |

---

## Expected test families

The documented lanes support these Hazards trust families:

| Family | Expected proof point |
|---|---|
| Layer admission | Public-layer candidates expose object family, source role, evidence refs, policy label, release state, temporal state, correction, and rollback. |
| Feature resolution | Clicked or requested features resolve through governed refs and finite outcomes before downstream UI use. |
| Evidence Drawer | Drawer payloads display evidence, source summaries, policy state, release state, caveats, freshness state, correction, and rollback. |
| Focus Mode | Prompt/response fixtures preserve finite outcome semantics and do not turn generated text into authority. |
| Source-role anti-collapse | Observed, regulatory, modeled, aggregate, administrative, candidate, and synthetic roles remain separate. |
| Freshness and stale state | Stale, expired, time-out-of-support, review-aged, rights-changed, and policy-version states are trust-visible where material. |
| Release/correction/rollback | Public candidates remain blocked unless release state and rollback target are present where required. |

---

## What belongs here

Appropriate contents include:

- deterministic no-network tests;
- compact synthetic fixtures or fixture pointers;
- import and schema smoke checks;
- contract/schema/policy parity checks;
- source-role anti-collapse checks;
- evidence, policy, release, correction, and rollback gate checks;
- public-surface trust-membrane checks;
- child-lane README files that explain scope, limits, and validation posture.

---

## Forbidden shortcuts

Do not use this subtree to:

- fetch live upstream source systems by default;
- store real source exports, lifecycle data, public tiles, proof artifacts, release artifacts, or generated public layers;
- redefine Hazards doctrine, contracts, schemas, fixtures, source registries, policy rules, release decisions, renderer code, or production pipeline code;
- infer release state from file existence, test success, source role label, layer name, map rendering, tile availability, drawer text, Focus answer text, or AI wording;
- publish, promote, approve, or release anything.

Any test that needs live source access, production source data, or public tile output belongs in a gated integration tier with explicit source admission, lifecycle state, policy, receipts, release controls, correction path, and rollback targets.

---

## Run posture

Parent subtree smoke command:

```bash
pytest tests/domains/hazards
```

Selected child-lane examples:

```bash
pytest tests/domains/hazards/layer_manifest
pytest tests/domains/hazards/feature_resolver
pytest tests/domains/hazards/drawer
pytest tests/domains/hazards/focus
pytest tests/domains/hazards/source_role_anti_collapse_test
```

Status of these commands: **PROPOSED / NEEDS VERIFICATION**. They assume `pytest` is the accepted runner and that executable test modules exist. This README does not claim any command currently passes.

---

## Evidence ledger

| Evidence | Status | Supports | Limits |
|---|---|---|---|
| Previous target file | CONFIRMED | `tests/domains/hazards/README.md` existed as a greenfield stub before this replacement. | Did not define the parent lane. |
| `tests/README.md` | CONFIRMED | `tests/` is enforceability proof, canonical, trust-bearing, and failure should block promotion where trust-spine checks fail. | Does not prove Hazards executable modules or pass rate. |
| Child README files under this subtree | CONFIRMED for files updated in this documentation pass | Provide lane-specific scope and boundary statements. | Do not prove executable tests, fixtures, validators, CI, or release wiring. |
| `docs/domains/hazards/MAP_UI_CONTRACTS.md` | CONFIRMED doctrine | Provides governed public flow, layer-manifest obligations, drawer obligations, Focus finite outcomes, source-role anti-collapse, and trust-visible UI states. | Concrete validators, fixtures, routes, policy runtime, and pass rates remain NEEDS VERIFICATION. |
| `docs/domains/hazards/LIFE_SAFETY_BOUNDARY.md` | CONFIRMED doctrine | Defines the Hazards life-safety boundary and referral/denial posture. | Enforcement mechanics remain PROPOSED until routes, flags, validators, policy bundles, fixtures, and tests are verified. |

---

## Validation checklist

Before treating this parent README as implemented behavior, verify:

- [ ] Executable test modules exist for each documented lane or the lane is explicitly documentation-only.
- [ ] Test runner and import paths match the repo's accepted convention.
- [ ] Synthetic fixtures exist in accepted fixture homes and are not source payloads.
- [ ] Schema paths and field expectations are accepted beyond scaffold status where tests enforce them.
- [ ] EvidenceRef / EvidenceBundle behavior is available to tests or safely stubbed.
- [ ] SourceRole/source registry behavior is available to tests or safely stubbed.
- [ ] PolicyDecision, RuntimeResponseEnvelope, ReleaseManifest, CorrectionNotice, RedactionReceipt, and RollbackCard expectations are defined before enforcing them.
- [ ] CI runs the no-network Hazards suite or marks incomplete lanes as expected gaps.
- [ ] Failures block public carrier promotion or release candidate approval where material.

---

## Rollback

Rollback is required if this parent lane becomes a live source-fetcher, lifecycle data store, fixture authority, source registry, contract root, schema authority, policy authority, proof store, release-decision root, public map/API/tile surface, AI surface, renderer implementation, pipeline implementation, or publication shortcut.

Rollback target for this replacement: previous stub blob SHA `1e4180a3df4bffeeb38324b7806b583e6104a725`.

<p align="right"><a href="#top">Back to top</a></p>
