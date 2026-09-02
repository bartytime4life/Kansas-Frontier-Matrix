<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-domains-habitat-thin-slice-habitat-fauna-test-readme
title: Habitat Fauna Thin-Slice Test README
type: test-readme
version: v0.1
status: draft; placeholder-expanded; thin-slice-test-lane; PROPOSED / NEEDS VERIFICATION before promotion
owners:
  - OWNER_TBD — Habitat domain steward
  - OWNER_TBD — Fauna domain steward
  - OWNER_TBD — Cross-domain steward
  - OWNER_TBD — Evidence steward
  - OWNER_TBD — Policy steward
  - OWNER_TBD — Validation steward
  - OWNER_TBD — Release steward
  - OWNER_TBD — QA steward
created: NEEDS VERIFICATION — blank placeholder existed before v0.1 expansion
updated: 2026-07-05
policy_label: public-doc; tests; habitat-fauna; thin-slice; no-network; fixture-only; cross-domain; evidence-bound; policy-aware; release-gated; anti-collapse
tags: [kfm, tests, habitat, fauna, thin-slice, cross-domain, fixture-only, EvidenceBundle, PolicyDecision, ReviewRecord, ReleaseManifest, CorrectionNotice, RollbackCard, ABSTAIN, DENY]
related:
  - ../../../README.md
  - ../README.md
  - ../../../../pipelines/proofs/habitat_fauna_thin_slice/README.md
  - ../../../../docs/architecture/ecology-cross-domain.md
  - ../../../../fixtures/ecology/README.md
  - ../../../../fixtures/fauna/README.md
  - ../../../../pipelines/cross_lane/README.md
  - ../../../../data/proofs/evidence_bundle/
  - ../../../../data/receipts/pipeline/
  - ../../../../release/manifests/habitat/
  - ../../../../release/manifests/fauna/
notes:
  - "This file replaces a blank placeholder at tests/domains/habitat/thin-slice.habitat-fauna.test/README.md."
  - "This is a test-lane README only. It does not define Habitat doctrine, Fauna doctrine, cross-domain doctrine, proof-pipeline code, schemas, fixtures, EvidenceBundles, policy rules, release decisions, public API material, public map material, public tiles, or published artifacts."
  - "The tested invariant is that this lane verifies cross-domain boundary discipline with deterministic fixtures: Habitat context and Fauna evidence remain separately owned, evidence support is required for claims, policy gates return finite outcomes, and test success does not become proof closure, release authority, public-layer truth, or AI/UI truth."
  - "Executable proof orchestration belongs under pipelines/proofs/habitat_fauna_thin_slice/ and emitted proof or receipt artifacts belong in accepted proof/receipt homes."
  - "Default posture is deterministic and no-network. Live source checks, real source exports, lifecycle data, and public tiles do not belong in this lane."
  - "Rollback target for this replacement is previous blank blob SHA 8b137891791fe96927ad78e64b0aad7bded08bdc."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Habitat Fauna thin-slice tests

> Deterministic, no-network test documentation for proving that the Habitat Fauna thin slice preserves cross-domain ownership, evidence requirements, policy posture, release boundaries, correction paths, and rollback targets.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: tests" src="https://img.shields.io/badge/root-tests%2F-blue">
  <img alt="Scope: Habitat Fauna" src="https://img.shields.io/badge/scope-habitat__fauna-2e7d32">
  <img alt="Lane: thin slice" src="https://img.shields.io/badge/lane-thin__slice-blue">
  <img alt="Network: disabled by default" src="https://img.shields.io/badge/network-disabled__by__default-critical">
  <img alt="Boundary: test not proof" src="https://img.shields.io/badge/boundary-test__not__proof-success">
</p>

**Path:** `tests/domains/habitat/thin-slice.habitat-fauna.test/README.md`  
**Status:** draft / placeholder-expanded / PROPOSED until executable tests are verified  
**Owning root:** `tests/`  
**Cross-domain slice:** Habitat and Fauna  
**Paired proof harness:** `pipelines/proofs/habitat_fauna_thin_slice/`  
**Default execution posture:** deterministic, synthetic, no-network, public-safe fixtures only  
**Truth posture:** CONFIRMED target was a blank placeholder before this expansion · CONFIRMED `tests/` is the canonical root for enforceability proof · CONFIRMED a Habitat Fauna proof-harness README exists under `pipelines/proofs/habitat_fauna_thin_slice/` · CONFIRMED cross-domain ecology doctrine says ecology is a composition pattern, not a domain, and atomic facts stay in owning domains · NEEDS VERIFICATION for executable test modules, fixture payload inventory, proof-runner behavior, policy runtime, release integration, public route/UI behavior, CI coverage, and pass rates.

---

## Purpose

`tests/domains/habitat/thin-slice.habitat-fauna.test/` is the test lane for the Habitat Fauna thin slice.

This lane should prove that a bounded cross-domain flow can join Habitat context with Fauna evidence while preserving ownership, source roles, evidence requirements, policy decisions, review posture, release boundaries, correction paths, and rollback targets.

A passing test here should **not** mean the proof pipeline is complete, live data is admitted, an EvidenceBundle is closed, public release is approved, or a public layer is safe. It should mean only that the thin-slice guardrails behaved as expected against bounded fixtures.

---

## Placement basis

`tests/` is the canonical root for enforceability proof. This dotted directory is a test lane name, not a new domain, not a proof store, and not a pipeline implementation root.

| Responsibility | Correct home | This lane's relationship |
|---|---|---|
| Thin-slice tests | `tests/domains/habitat/thin-slice.habitat-fauna.test/` | This directory. |
| Executable proof harness | `pipelines/proofs/habitat_fauna_thin_slice/` | System under test; not duplicated here. |
| Cross-domain doctrine | `docs/architecture/ecology-cross-domain.md` | Doctrine basis; tests do not redefine it. |
| Synthetic fixtures | `fixtures/ecology/`, `fixtures/fauna/`, and accepted Habitat fixture homes | Preferred toy inputs and expected outcomes. |
| Proof and receipt outputs | `data/proofs/evidence_bundle/`, `data/receipts/pipeline/`, or accepted successors | Outputs referenced by tests; not written here by default. |
| Release decisions | `release/` and domain release manifests | Publication, correction, and rollback authority; tests cannot replace it. |

---

## Invariant under test

> **Cross-domain composition is not authority collapse.** Habitat context and Fauna evidence may be composed only through governed joins that preserve source roles, domain ownership, evidence support, policy posture, review state, release relationship, correction path, and rollback target.

Core checks:

| Check | Required behavior | Failure outcome |
|---|---|---|
| Domain ownership | Habitat and Fauna object families remain separately owned. | validation failure. |
| Source-role preservation | Source roles remain visible where material. | validation failure / `ABSTAIN`. |
| Evidence support | Claims resolve evidence support or produce a finite non-answer. | `ABSTAIN`. |
| Policy posture | Material policy checks return finite outcomes. | `DENY` / `ABSTAIN` / `ERROR`. |
| Trust membrane | Public-facing examples do not read internal or candidate state as authority. | validation failure. |
| Proof boundary | Test pass does not become proof closure, release approval, or public artifact authority. | promotion block. |
| Release boundary | Review, release, correction, and rollback remain separate objects and gates. | promotion block. |
| AI/UI boundary | Generated summaries and UI carriers remain downstream of evidence and policy. | `ABSTAIN` / validation failure. |

---

## Expected scope

Tests in this lane may validate:

- fixture-only Habitat Fauna join behavior;
- domain ownership and source-role anti-collapse;
- proof-harness invocation contracts at a smoke-test level;
- evidence resolution requirements;
- policy finite outcomes;
- public-client trust-membrane checks;
- correction and rollback readiness for released derivatives;
- rejection of shortcuts that treat fixture output, proof receipts, graph projections, map layers, or AI text as truth.

Live source checks, live downloads, production credentials, public tile generation, and real source records are out of scope for the default suite.

---

## Suggested layout

```text
tests/domains/habitat/thin-slice.habitat-fauna.test/
├── README.md
├── test_fixture_join_contract.py
├── test_domain_ownership_preserved.py
├── test_source_role_anti_collapse.py
├── test_evidence_and_policy_required.py
├── test_public_trust_membrane.py
└── test_release_correction_rollback.py
```

---

## Run posture

```bash
pytest tests/domains/habitat/thin-slice.habitat-fauna.test
```

Status of the command above: **PROPOSED / NEEDS VERIFICATION**. It assumes `pytest` is the accepted test runner and that executable test modules exist. This README does not claim the command currently passes.

---

## Evidence ledger

| Evidence | Status | Supports | Limits |
|---|---|---|---|
| Previous target file | CONFIRMED | `tests/domains/habitat/thin-slice.habitat-fauna.test/README.md` existed as a blank placeholder before this replacement. | Did not define the lane. |
| `tests/README.md` | CONFIRMED | `tests/` is enforceability proof and failure should block promotion where trust-spine checks fail. | Does not prove this lane's modules or pass rate. |
| `pipelines/proofs/habitat_fauna_thin_slice/README.md` | CONFIRMED proof-harness README | Defines the proof harness as cross-domain executable proof orchestration, not EvidenceBundle storage, not a new domain root, and not a shortcut around Habitat or Fauna ownership. | Concrete executable behavior, CI coverage, fixture coverage, release wiring, and public API/map behavior remain NEEDS VERIFICATION. |
| `docs/architecture/ecology-cross-domain.md` | CONFIRMED doctrine | Ecology is cross-domain composition; atomic facts remain in contributing domain lanes. | The document itself marks many concrete paths as PROPOSED unless separately verified. |

---

## Validation checklist

- [ ] Executable test modules exist under this lane.
- [ ] Test runner and import paths support the dotted directory name.
- [ ] Synthetic fixtures exist for positive join, missing owner, missing source role, missing evidence, policy hold/deny/abstain, public-trust-membrane failure, proof-receipt misuse, and missing release/correction/rollback cases.
- [ ] The proof harness can be invoked or safely stubbed without live source access.
- [ ] EvidenceRef / EvidenceBundle behavior is available to tests or safely stubbed.
- [ ] PolicyDecision, ReviewRecord, ReleaseManifest, CorrectionNotice, RedactionReceipt, and RollbackCard expectations are defined before enforcing them.
- [ ] CI runs the no-network Habitat Fauna thin-slice suite or explicitly excludes it until implemented.
- [ ] Failures block public carrier promotion or release candidate approval where material.

---

## Rollback

Rollback is required if this lane becomes a live source-fetcher, lifecycle data store, proof store, fixture authority, contract root, schema authority, policy authority, release-decision root, public map/API/tile surface, AI surface, renderer implementation, pipeline implementation, or publication shortcut.

Rollback target for this replacement: previous blank blob SHA `8b137891791fe96927ad78e64b0aad7bded08bdc`.

<p align="right"><a href="#top">Back to top</a></p>
