<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-domains-habitat-test-quality-score-readme
title: Habitat Quality Score Test README
type: test-readme
version: v0.1
status: draft; placeholder-expanded; test-lane; PROPOSED / NEEDS VERIFICATION before promotion
owners:
  - OWNER_TBD — Habitat domain steward
  - OWNER_TBD — Suitability steward
  - OWNER_TBD — Habitat Quality Score steward
  - OWNER_TBD — Evidence steward
  - OWNER_TBD — Source steward
  - OWNER_TBD — Policy steward
  - OWNER_TBD — Sensitivity reviewer
  - OWNER_TBD — Validation steward
  - OWNER_TBD — Release steward
  - OWNER_TBD — QA steward
created: NEEDS VERIFICATION — blank placeholder existed before v0.1 expansion
updated: 2026-07-05
policy_label: public-doc; tests; habitat; habitat-quality-score; quality-score; no-network; descriptive-not-prescriptive; source-role-aware; uncertainty-bound; evidence-bound; sensitivity-aware; release-gated; anti-collapse
tags: [kfm, tests, habitat, quality_score, test_quality_score, HabitatQualityScore, habitat-quality-score, descriptive-score, suitability, score, model-card, ModelRunReceipt, UncertaintySurface, HabitatPatch, SuitabilityModel, EvidenceBundle, PolicyDecision, ReleaseManifest, CorrectionNotice, RollbackCard, ABSTAIN, DENY]
related:
  - ../../../README.md
  - ../README.md
  - ../../../../contracts/domains/habitat/habitat_quality_score.md
  - ../../../../contracts/domains/habitat/habitat_patch.md
  - ../../../../contracts/domains/habitat/SuitabilityModel.md
  - ../../../../contracts/domains/habitat/suitability_model.md
  - ../../../../contracts/domains/habitat/land_cover/model_run_receipt.md
  - ../../../../contracts/domains/habitat/land_cover/uncertainty.md
  - ../../../../contracts/domains/habitat/domain_feature_identity.md
  - ../../../../contracts/domains/habitat/domain_observation.md
  - ../../../../docs/domains/habitat/MODEL_VS_OBSERVATION.md
  - ../../../../docs/domains/habitat/SOURCE_FAMILIES.md
  - ../../../../docs/domains/habitat/sublanes/patch.md
  - ../../../../docs/domains/habitat/sublanes/suitability.md
  - ../../../../schemas/contracts/v1/domains/habitat/habitat_quality_score.schema.json
  - ../../../../fixtures/domains/habitat/habitat_quality_score/
  - ../../../../pipelines/domains/habitat/
  - ../../../../pipeline_specs/habitat/
  - ../../../../policy/domains/habitat/
  - ../../../../policy/sensitivity/habitat/
  - ../../../../data/registry/sources/habitat/
  - ../../../../release/manifests/habitat/
notes:
  - "This file replaces a blank placeholder at tests/domains/habitat/test_quality_score/README.md."
  - "This is a test-lane README only. It does not define Habitat Quality Score doctrine, semantic contracts, schemas, fixtures, lifecycle records, evidence bundles, receipts, policy rules, release decisions, pipeline code, public API material, public map material, public tiles, or published artifacts."
  - "The tested invariant is that HabitatQualityScore is a governed descriptive score over a declared Habitat subject. It must preserve scored subject, score meaning, scoring method, source role, source support, evidence support, uncertainty support, sensitivity posture, release relationship, correction, and rollback without becoming management instruction, regulatory designation, occurrence truth, raw model surface, HabitatPatch identity, release authority, public-layer truth, or AI/UI truth."
  - "Default posture is deterministic and no-network. Live source checks, real source exports, lifecycle data, public tiles, and sensitive joined records do not belong in this lane."
  - "Rollback target for this replacement is previous blank blob SHA 8b137891791fe96927ad78e64b0aad7bded08bdc."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Habitat Quality Score tests

> Deterministic, no-network test documentation for proving that Habitat `HabitatQualityScore` records remain descriptive, evidence-bound, source-role-aware, uncertainty-bound, release-gated, correction-aware, and rollback-ready.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: tests" src="https://img.shields.io/badge/root-tests%2F-blue">
  <img alt="Domain: habitat" src="https://img.shields.io/badge/domain-habitat-2e7d32">
  <img alt="Lane: quality score" src="https://img.shields.io/badge/lane-quality__score-blue">
  <img alt="Network: disabled by default" src="https://img.shields.io/badge/network-disabled__by__default-critical">
  <img alt="Boundary: descriptive not prescriptive" src="https://img.shields.io/badge/boundary-descriptive__not__prescriptive-success">
</p>

**Path:** `tests/domains/habitat/test_quality_score/README.md`  
**Status:** draft / placeholder-expanded / PROPOSED until executable tests are verified  
**Owning root:** `tests/`  
**Domain segment:** `habitat`  
**Test lane:** `test_quality_score`  
**Default execution posture:** deterministic, synthetic, no-network, public-safe fixtures only  
**Truth posture:** CONFIRMED target was a blank placeholder before this expansion · CONFIRMED `tests/` is the canonical root for enforceability proof · CONFIRMED `HabitatQualityScore` is a Habitat object-family term with PROPOSED field realization · CONFIRMED the Habitat Quality Score contract defines it as a descriptive scalar or categorical measure and not management instruction, regulatory critical habitat, occurrence truth, raw model surface, HabitatPatch identity, or release authority · CONFIRMED the paired schema is a scaffold and field-level enforcement remains NEEDS VERIFICATION · NEEDS VERIFICATION for executable test modules, fixture payload inventory, validator behavior, source registry activation, policy runtime, release integration, public route/UI behavior, CI coverage, and pass rates.

**Quick jumps:** [Purpose](#purpose) · [Placement basis](#placement-basis) · [Invariant under test](#invariant-under-test) · [Expected scope](#expected-scope) · [Fixture posture](#fixture-posture) · [Assertions](#assertions) · [Finite outcomes](#finite-outcomes) · [Forbidden shortcuts](#forbidden-shortcuts) · [Suggested layout](#suggested-layout) · [Run posture](#run-posture) · [Evidence ledger](#evidence-ledger) · [Validation checklist](#validation-checklist) · [Rollback](#rollback)

---

## Purpose

`tests/domains/habitat/test_quality_score/` is the intended home for Habitat Quality Score tests.

This lane should prove that `HabitatQualityScore` records preserve scored subject, score meaning, scoring method, source role, source support, evidence, uncertainty, sensitivity, release, correction, and rollback boundaries. It should also prove that score values do not collapse into management instructions, regulatory designations, occurrence truth, raw model surfaces, patch identity, release approval, public layer authority, or AI-generated truth.

A passing test here should **not** mean that a real score is admitted, a model is validated for all uses, a public layer is safe, or a release is approved. It should mean only that quality-score guardrails behaved as expected against bounded fixtures.

---

## Placement basis

`tests/` is the canonical root for enforceability proof. Habitat is a domain segment inside that root. `test_quality_score` is a test lane, not a new root and not a parallel contract, schema, policy, data, release, proof, or public-map home.

| Responsibility | Correct home | This lane's relationship |
|---|---|---|
| Habitat Quality Score tests | `tests/domains/habitat/test_quality_score/` | This directory. |
| Habitat Quality Score meaning | `contracts/domains/habitat/habitat_quality_score.md` | Semantic contract under test. |
| Machine schema | `schemas/contracts/v1/domains/habitat/habitat_quality_score.schema.json` | Referenced where accepted; scaffold posture must be respected. |
| Fixtures | `fixtures/domains/habitat/habitat_quality_score/` | Preferred toy inputs and expected outcomes if populated. |
| Patch support | `contracts/domains/habitat/habitat_patch.md` | Score may attach to patch or public-safe aggregate; it does not become patch identity. |
| Suitability support | `contracts/domains/habitat/SuitabilityModel.md`, `contracts/domains/habitat/suitability_model.md` | Score may derive from or support a suitability model; it does not become model definition. |
| Receipt and uncertainty support | `contracts/domains/habitat/land_cover/model_run_receipt.md`, `contracts/domains/habitat/land_cover/uncertainty.md` or future Habitat-wide equivalents | Required when modeled/derived score support is material. |
| Policy and sensitivity homes | `policy/domains/habitat/`, `policy/sensitivity/habitat/` or inherited joined-lane homes where accepted | Referenced by tests, not bypassed here. |
| Release decisions | `release/` and `release/manifests/habitat/` | Publication, correction, and rollback authority; tests cannot replace it. |

---

## Invariant under test

> **HabitatQualityScore is descriptive, not prescriptive.** A Habitat quality score records a quality value, class, band, index, or score over a declared Habitat scope. It must stay bounded by score meaning, method, source role, evidence, uncertainty, policy, release, correction, and rollback context.

Core checks:

| Check | Required behavior | Failure outcome |
|---|---|---|
| Scored subject | Patch, aggregate, grid cell, model output, stewardship unit, or public-safe scope is explicit. | validation failure / `ERROR`. |
| Score value and meaning | Numeric value, class, band, rank, confidence category, enum, and metric meaning are explicit. | validation failure. |
| Scoring method | Field review, rule set, model, weighted index, crosswalk, expert assessment, or aggregate method is recorded. | validation failure. |
| Source role | Observed/reviewed, model, derivative, aggregate, context, candidate, synthetic, or accepted posture remains visible. | validation failure / `ABSTAIN`. |
| Evidence and uncertainty | Evidence and uncertainty/caveat refs are attached before consequential use. | `ABSTAIN`. |
| Sensitivity posture | Score exposure does not reveal restricted context or overstate weak inputs. | `DENY` / `RESTRICT` / hold. |
| Release boundary | Policy, review, release, correction, and rollback remain separate from test pass state. | promotion block. |
| No authority upgrade | Score cannot become instruction, regulatory truth, occurrence truth, raw model truth, patch identity, release authority, public-layer truth, or AI truth. | validation failure / `ABSTAIN`. |

---

## Expected scope

Tests in this lane may validate:

- required scored subject, score value, score class, score meaning, method profile, source role, source support, temporal scope, and digest posture;
- rejection of scores presented as management instruction, regulatory designation, occurrence proof, raw model surface, or patch identity;
- model-run receipt and uncertainty requirements where the score is model-derived;
- public-safe scope and sensitivity posture before map/API/UI/AI carrier use;
- evidence and uncertainty requirements for consequential or public-facing use;
- rejection of public-facing candidates that lack evidence, policy, review, release relationship, correction, or rollback context;
- finite outcomes when evidence resolver, policy engine, model-run receipt, uncertainty support, source registry activation, or release manifest is missing.

Live source checks, real source exports, production score payloads, public tile generation, sensitive joined records, and provider-backed model calls are out of scope for the default suite.

---

## Fixture posture

Use synthetic, public-safe fixtures only.

Fixture requirements:

- deterministic and no-network;
- compact enough for review in a PR;
- explicit expected outcome;
- explicit scored subject, score value, score meaning, scoring method, source role, source support, evidence, uncertainty, policy, review, release relationship, correction, and rollback posture where material;
- no real source exports, lifecycle data, production score payloads, public tiles, sensitive joined records, or published artifacts.

Preferred fixture families:

| Fixture kind | Expected outcome |
|---|---|
| Valid synthetic HabitatQualityScore with subject, value, method, evidence, uncertainty, and release relationship | accepted descriptive score support only. |
| Missing scored subject or score meaning | validation failure / `ERROR`. |
| Score treated as management instruction or regulatory designation | validation failure. |
| Score treated as occurrence proof, raw model surface, or patch identity | validation failure / `ABSTAIN`. |
| Model-derived score missing receipt or uncertainty | review required / `ABSTAIN`. |
| Public output lacks release/correction/rollback posture | promotion block. |
| AI/UI answer treats score as truth | `ABSTAIN` / validation failure. |

---

## Assertions

A useful Habitat Quality Score test should make the descriptive-score boundary obvious.

### Positive path

- scored subject and score meaning are explicit;
- scoring method, source role, and source support are visible;
- model-run, model-card, uncertainty, and validation support are linkable where material;
- evidence, policy, review, release relationship, correction, and rollback references are linkable where material;
- public-safe scope and sensitivity posture are explicit where material.

### Negative path

- score cannot become management instruction;
- score cannot become regulatory critical habitat or occurrence truth;
- score cannot become raw model surface, HabitatPatch identity, or release authority;
- score cannot drop uncertainty for simplified public display;
- test pass cannot become release approval;
- map style, tile, popup, graph edge, Focus Mode answer, or AI text cannot become quality-score authority;
- missing evidence produces `ABSTAIN` rather than a fluent claim.

---

## Finite outcomes

| Condition | Expected outcome |
|---|---|
| Valid synthetic HabitatQualityScore with subject, method, evidence, uncertainty, policy, review, release relationship, correction, and rollback context | accepted descriptive score support only. |
| Missing scored subject, score value, score meaning, source role, method, temporal scope, or digest basis | validation failure / `ERROR`. |
| Score treated as instruction, regulatory designation, occurrence truth, raw model truth, patch identity, or release authority | validation failure. |
| Model-derived score lacks receipt or uncertainty | review required / `ABSTAIN`. |
| Public-facing candidate lacks release/correction/rollback posture | promotion-blocking failure. |
| Policy engine unavailable | `ERROR` or `ABSTAIN`, never public exposure. |

---

## Forbidden shortcuts

Do not use this test lane to:

- fetch live upstream source systems;
- store real source exports, lifecycle data, production score payloads, public tiles, or release artifacts;
- store proof packs, release manifests, or generated public layers;
- redefine Habitat Quality Score doctrine, contracts, schemas, fixtures, policy rules, receipts, proofs, release decisions, renderer code, or production code;
- bypass source role, score meaning, method profile, evidence, uncertainty, validation, policy, review, correction, or rollback checks with a fixture flag;
- infer release state from file existence, test success, layer name, score label, map rendering, tile availability, or AI wording;
- publish, promote, or release anything.

Any test that needs real score payloads, source data, or public tile output belongs in a gated integration tier with source admission, lifecycle state, policy, receipts, release controls, and rollback targets.

---

## Suggested layout

The exact test module names remain **NEEDS VERIFICATION** until the runner and existing conventions are inspected.

```text
tests/domains/habitat/test_quality_score/
├── README.md
├── test_quality_score_identity.py
├── test_scored_subject_required.py
├── test_score_meaning_and_method.py
├── test_descriptive_not_prescriptive.py
├── test_model_run_and_uncertainty_required.py
├── test_score_not_patch_or_occurrence_truth.py
└── test_release_correction_rollback.py
```

---

## Run posture

```bash
pytest tests/domains/habitat/test_quality_score
```

Status of the command above: **PROPOSED / NEEDS VERIFICATION**. It assumes `pytest` is the accepted test runner and that executable test modules exist. This README does not claim the command currently passes.

---

## Evidence ledger

| Evidence | Status | Supports | Limits |
|---|---|---|---|
| Previous target file | CONFIRMED | `tests/domains/habitat/test_quality_score/README.md` existed as a blank placeholder before this replacement. | Did not define the lane. |
| `tests/README.md` | CONFIRMED | `tests/` is enforceability proof and failure should block promotion where trust-spine checks fail. | Does not prove this lane's modules or pass rate. |
| `contracts/domains/habitat/habitat_quality_score.md` | CONFIRMED semantic contract / PROPOSED implementation | Defines `HabitatQualityScore` as a governed scalar or categorical measure attached to a declared Habitat scope; descriptive and evidence-bound, not management instruction, regulatory critical habitat, occurrence truth, raw model surface, HabitatPatch identity, or release authority. | Schema is a permissive scaffold and field-level enforcement remains NEEDS VERIFICATION. |
| `docs/domains/habitat/sublanes/patch.md` and suitability references | CONFIRMED doctrine / PROPOSED implementation | Quality scores attach to or contextualize patches/suitability; they remain separate object families and require governed release posture. | Suitability sublane implementation details, validators, fixtures, CI, and pass rates remain NEEDS VERIFICATION. |

---

## Validation checklist

Before treating this README as implemented behavior, verify:

- [ ] Executable test modules exist under this lane.
- [ ] Test runner and import paths match the repo's accepted convention.
- [ ] Synthetic fixtures exist for valid score, missing subject, missing method, score-as-instruction, score-as-regulatory, score-as-occurrence, score-as-patch-identity, missing receipt, missing uncertainty, missing public-safe scope, and missing release/correction/rollback cases.
- [ ] HabitatQualityScore schema path and field expectations are accepted beyond scaffold status.
- [ ] EvidenceRef / EvidenceBundle behavior is available to tests or safely stubbed.
- [ ] ModelRunReceipt, model-card, and UncertaintySurface behavior is available to tests or safely stubbed.
- [ ] PolicyDecision, ReviewRecord, ReleaseManifest, CorrectionNotice, RedactionReceipt, and RollbackCard expectations are defined before enforcing them.
- [ ] CI runs the no-network Habitat Quality Score suite.
- [ ] Failures block public carrier promotion or release candidate approval.

---

## Rollback

Rollback is required if this lane becomes a source export store, score-payload store, lifecycle data store, fixture root, contract root, schema authority, policy authority, proof store, release-decision root, public map/API/tile surface, AI surface, renderer implementation, pipeline implementation, or publication shortcut.

Rollback target for this replacement: previous blank blob SHA `8b137891791fe96927ad78e64b0aad7bded08bdc`.

<p align="right"><a href="#top">Back to top</a></p>
