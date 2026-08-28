<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-domains-hazards-source-role-anti-collapse-test-readme
title: Hazards Source-Role Anti-Collapse Test README
type: test-readme
version: v0.1
status: draft; placeholder-expanded; source-role-test-lane; PROPOSED / NEEDS VERIFICATION before promotion
owners:
  - OWNER_TBD — Hazards domain steward
  - OWNER_TBD — Source steward
  - OWNER_TBD — Evidence steward
  - OWNER_TBD — Policy steward
  - OWNER_TBD — Validation steward
  - OWNER_TBD — Release steward
  - OWNER_TBD — QA steward
created: NEEDS VERIFICATION — blank placeholder existed before v0.1 expansion
updated: 2026-07-05
policy_label: public-doc; tests; hazards; source-role; anti-collapse; no-network; evidence-bound; policy-aware; release-gated; finite-outcomes; rollback-aware
tags: [kfm, tests, hazards, source-role, source_role_anti_collapse_test, anti-collapse, observed, regulatory, modeled, aggregate, administrative, candidate, synthetic, LayerManifest, EvidenceDrawerPayload, FocusModeResponse, EvidenceBundle, PolicyDecision, ReleaseManifest, CorrectionNotice, RollbackCard, ABSTAIN, DENY, ERROR]
related:
  - ../../../README.md
  - ../README.md
  - ../layer_manifest/README.md
  - ../drawer/README.md
  - ../feature_resolver/README.md
  - ../focus/README.md
  - ../../../../docs/domains/hazards/MAP_UI_CONTRACTS.md
  - ../../../../docs/domains/hazards/SOURCE_REGISTRY.md
  - ../../../../docs/domains/hazards/IDENTITY_MODEL.md
  - ../../../../docs/domains/hazards/DATA_LIFECYCLE.md
  - ../../../../contracts/evidence/evidence_bundle.md
  - ../../../../contracts/policy/policy_decision.md
  - ../../../../contracts/release/release_manifest.md
  - ../../../../schemas/contracts/v1/domains/hazards/
  - ../../../../fixtures/domains/hazards/source_role_anti_collapse_test/
  - ../../../../policy/domains/hazards/
  - ../../../../release/manifests/hazards/
notes:
  - "This file replaces a blank placeholder at tests/domains/hazards/source_role_anti_collapse_test/README.md."
  - "This is a test-lane README only. It does not define Hazards doctrine, source-role vocabulary, schemas, fixtures, lifecycle records, EvidenceBundles, policy rules, release decisions, public API material, public map material, public tiles, or published artifacts."
  - "The tested invariant is that Hazards source roles remain first-class identity attributes: observed, regulatory, modeled, aggregate, administrative, candidate, and synthetic roles must not collapse into each other across LayerManifest, feature resolver, Evidence Drawer, Focus Mode, release, correction, or rollback contexts."
  - "Default posture is deterministic and no-network. Live source checks, real source exports, lifecycle data, public tiles, and restricted records do not belong in this lane."
  - "Rollback target for this replacement is previous blank blob SHA 8b137891791fe96927ad78e64b0aad7bded08bdc."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Hazards source-role anti-collapse tests

> Deterministic, no-network test documentation for proving that Hazards source roles remain visible, fixed, and non-interchangeable across map, drawer, resolver, Focus Mode, evidence, policy, release, correction, and rollback paths.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: tests" src="https://img.shields.io/badge/root-tests%2F-blue">
  <img alt="Domain: hazards" src="https://img.shields.io/badge/domain-hazards-critical">
  <img alt="Lane: source role" src="https://img.shields.io/badge/lane-source__role-blue">
  <img alt="Network: disabled by default" src="https://img.shields.io/badge/network-disabled__by__default-critical">
  <img alt="Boundary: no role collapse" src="https://img.shields.io/badge/boundary-no__role__collapse-success">
</p>

**Path:** `tests/domains/hazards/source_role_anti_collapse_test/README.md`  
**Status:** draft / placeholder-expanded / PROPOSED until executable tests are verified  
**Owning root:** `tests/`  
**Domain segment:** `hazards`  
**Test lane:** `source_role_anti_collapse_test`  
**Default execution posture:** deterministic, synthetic, no-network, public-safe fixtures only  
**Truth posture:** CONFIRMED target was a blank placeholder before this expansion · CONFIRMED `tests/` is the canonical root for enforceability proof · CONFIRMED Hazards map/UI doctrine says source role is a first-class identity attribute fixed at admission and never upgraded by promotion · CONFIRMED the Hazards map/UI contract reconciles the canonical seven-role register for `source_role` and defines anti-collapse validator obligations · NEEDS VERIFICATION for executable test modules, fixture payload inventory, schema enforcement, validator behavior, policy runtime, release integration, UI behavior, CI coverage, and pass rates.

---

## Purpose

`tests/domains/hazards/source_role_anti_collapse_test/` is the intended home for Hazards source-role anti-collapse tests.

This lane should prove that Hazards records, manifests, drawer payloads, resolver outputs, and Focus Mode responses preserve canonical source-role posture. A modeled, regulatory, aggregate, administrative, observed, candidate, or synthetic fixture must not be silently rewritten as another role because it is easier to render, compare, summarize, or publish.

A passing test here should **not** mean that a real source is admitted, a public layer is safe, or a release is approved. It should mean only that source-role guardrails behaved as expected against bounded fixtures.

---

## Placement basis

`tests/` is the canonical root for enforceability proof. Hazards is a domain segment inside that root. `source_role_anti_collapse_test/` is a test lane, not a source registry, schema home, policy home, release home, data store, proof store, public API surface, or public map surface.

| Responsibility | Correct home | This lane's relationship |
|---|---|---|
| Source-role anti-collapse tests | `tests/domains/hazards/source_role_anti_collapse_test/` | This directory. |
| Hazards map/UI doctrine | `docs/domains/hazards/MAP_UI_CONTRACTS.md` | Source-role and anti-collapse doctrine under test. |
| Source registry docs | `docs/domains/hazards/SOURCE_REGISTRY.md` and `data/registry/sources/hazards/` | Source admission/reference context; not duplicated here. |
| Layer manifest tests | `tests/domains/hazards/layer_manifest/` | Upstream public-layer metadata checks. |
| Drawer / resolver / Focus tests | `tests/domains/hazards/drawer/`, `feature_resolver/`, `focus/` | Downstream consumer checks. |
| Synthetic fixtures | `fixtures/domains/hazards/source_role_anti_collapse_test/` | Preferred toy inputs and expected outcomes if populated. |
| Policy homes | `policy/domains/hazards/` | Referenced by tests, not bypassed here. |
| Release decisions | `release/` and `release/manifests/hazards/` | Publication, correction, and rollback authority; tests cannot replace it. |

---

## Invariant under test

> **Source role is identity, not decoration.** Hazards `source_role` values must preserve the canonical role of the source or derived product. Promotion, rendering, summarization, graph projection, and AI wording cannot upgrade or flatten a role.

Canonical roles under test:

| Canonical role | Test posture |
|---|---|
| `observed` | Real-world observation or event fixture; not regulatory, modeled, or aggregate. |
| `regulatory` | Legal or regulatory context fixture; not observed event truth. |
| `modeled` | Model or derived surface fixture; not observed measurement. |
| `aggregate` | Aggregated index or summary fixture; not per-place observation. |
| `administrative` | Compiled administrative record fixture; not regulatory unless explicitly so. |
| `candidate` | Candidate or unreviewed fixture; not released truth. |
| `synthetic` | Toy fixture or generated test material; never source truth. |

Core checks:

| Check | Required behavior | Failure outcome |
|---|---|---|
| Role presence | `source_role` is explicit where material. | validation failure / `ABSTAIN`. |
| Role immutability | Promotion or release cannot silently change source role. | validation failure. |
| Layer manifest parity | `LayerManifest.source_role` matches admitted role and object family. | validation failure. |
| Drawer visibility | Source-role chip/label remains visible in drawer payloads where material. | validation failure. |
| Focus wording | Focus Mode comparisons retain source-role caveats and do not flatten roles. | `ABSTAIN` / validation failure. |
| Context vs role | Contextual usage posture does not replace the canonical role field. | validation failure / NEEDS VERIFICATION where open questions remain. |
| No authority upgrade | Source role cannot become evidence closure, policy authority, release authority, public-layer truth, or AI truth. | validation failure / `ABSTAIN`. |

---

## Expected scope

Tests in this lane may validate:

- modeled material rejected when labeled `observed`;
- regulatory context rejected when rendered as observed event truth;
- aggregate summaries rejected when cited as per-place observation;
- candidate material blocked from release-style public claims unless reviewed and promoted through governed flow;
- synthetic fixtures clearly labeled as synthetic and never treated as source truth;
- drawer, layer, resolver, and Focus outputs preserving role labels;
- finite outcomes when source role is missing, conflicted, unresolved, or outside the accepted enum.

Live source checks, real source exports, production credentials, public tile generation, and real-world incident payloads are out of scope for the default suite.

---

## Fixture posture

Use synthetic, public-safe fixtures only.

Fixture requirements:

- deterministic and no-network;
- compact enough for review in a PR;
- explicit expected outcome;
- explicit object family, source role, evidence posture, policy state, release relationship, correction, and rollback posture where material;
- no real source exports, lifecycle data, public tiles, credentials, or published artifacts.

---

## Finite outcomes

| Condition | Expected outcome |
|---|---|
| Valid synthetic fixture preserves canonical source role across layer/drawer/resolver/Focus path | accepted role support only. |
| Missing source role | validation failure / `ABSTAIN`. |
| Modeled source labeled observed | validation failure. |
| Regulatory context rendered as observed event truth | validation failure. |
| Aggregate cited as per-place observation | validation failure / `ABSTAIN`. |
| Candidate or synthetic material treated as released source truth | validation failure / `DENY`. |
| Source role conflicted or unresolved | hold / `ABSTAIN` / NEEDS VERIFICATION. |
| Policy engine unavailable | `ERROR` or `ABSTAIN`, never public exposure. |

---

## Suggested layout

```text
tests/domains/hazards/source_role_anti_collapse_test/
├── README.md
├── test_source_role_required.py
├── test_modeled_not_observed.py
├── test_regulatory_not_observed_event.py
├── test_aggregate_not_per_place_observation.py
├── test_candidate_and_synthetic_boundaries.py
├── test_role_visible_in_drawer_and_focus.py
└── test_release_correction_rollback.py
```

---

## Run posture

```bash
pytest tests/domains/hazards/source_role_anti_collapse_test
```

Status of the command above: **PROPOSED / NEEDS VERIFICATION**. It assumes `pytest` is the accepted test runner and that executable test modules exist. This README does not claim the command currently passes.

---

## Evidence ledger

| Evidence | Status | Supports | Limits |
|---|---|---|---|
| Previous target file | CONFIRMED | `tests/domains/hazards/source_role_anti_collapse_test/README.md` existed as a blank placeholder before this replacement. | Did not define the lane. |
| `tests/README.md` | CONFIRMED | `tests/` is enforceability proof and failure should block promotion where trust-spine checks fail. | Does not prove this lane's modules or pass rate. |
| `docs/domains/hazards/MAP_UI_CONTRACTS.md` | CONFIRMED doctrine | Source role is first-class, fixed at admission, bound to the canonical seven-role register, rendered in drawer/legend/Focus surfaces, and has proposed validator obligations. | Concrete validators, fixtures, source registry activation, schema enforcement, and pass rates remain NEEDS VERIFICATION. |
| Repo search | CONFIRMED | Found Hazards source-role anti-collapse doctrine in `MAP_UI_CONTRACTS.md`. | Search is not proof of executable tests or fixtures. |

---

## Validation checklist

- [ ] Executable test modules exist under this lane.
- [ ] Test runner and import paths match the repo's accepted convention.
- [ ] Synthetic fixtures exist for each canonical source-role case and anti-collapse failure case.
- [ ] Active source-role enum/schema path is accepted or safely stubbed.
- [ ] EvidenceRef / EvidenceBundle behavior is available to tests or safely stubbed.
- [ ] PolicyDecision behavior is available to tests or safely stubbed.
- [ ] ReleaseManifest, CorrectionNotice, RedactionReceipt, and RollbackCard expectations are defined before enforcing them.
- [ ] CI runs the no-network Hazards source-role anti-collapse suite.
- [ ] Failures block public carrier promotion or release candidate approval where material.

---

## Rollback

Rollback is required if this lane becomes a live source-fetcher, lifecycle data store, fixture authority, source registry, contract root, schema authority, policy authority, proof store, release-decision root, public map/API/tile surface, AI surface, renderer implementation, pipeline implementation, or publication shortcut.

Rollback target for this replacement: previous blank blob SHA `8b137891791fe96927ad78e64b0aad7bded08bdc`.

<p align="right"><a href="#top">Back to top</a></p>
