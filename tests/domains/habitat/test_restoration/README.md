<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-domains-habitat-test-restoration-readme
title: Habitat Restoration Test README
type: test-readme
version: v0.1
status: draft; placeholder-expanded; test-lane; PROPOSED / NEEDS VERIFICATION before promotion
owners:
  - OWNER_TBD — Habitat domain steward
  - OWNER_TBD — Restoration steward
  - OWNER_TBD — Evidence steward
  - OWNER_TBD — Source steward
  - OWNER_TBD — Policy steward
  - OWNER_TBD — Sensitivity reviewer
  - OWNER_TBD — Validation steward
  - OWNER_TBD — Release steward
  - OWNER_TBD — QA steward
created: NEEDS VERIFICATION — blank placeholder existed before v0.1 expansion
updated: 2026-07-05
policy_label: public-doc; tests; habitat; restoration; no-network; candidate-not-directive; evidence-bound; policy-aware; source-role-aware; release-gated; rollback-aware
tags: [kfm, tests, habitat, restoration, test_restoration, RestorationOpportunity, candidate-site, opportunity-surface, HabitatPatch, HabitatQualityScore, SuitabilityModel, ConnectivityEdge, Corridor, StewardshipZone, ModelRunReceipt, UncertaintySurface, EvidenceBundle, PolicyDecision, ReviewRecord, ReleaseManifest, CorrectionNotice, RollbackCard, ABSTAIN, DENY]
related:
  - ../../../README.md
  - ../README.md
  - ../../../../contracts/domains/habitat/restoration_opportunity.md
  - ../../../../contracts/domains/habitat/habitat_patch.md
  - ../../../../contracts/domains/habitat/habitat_quality_score.md
  - ../../../../contracts/domains/habitat/SuitabilityModel.md
  - ../../../../contracts/domains/habitat/connectivity_edge.md
  - ../../../../contracts/domains/habitat/corridor.md
  - ../../../../contracts/domains/habitat/stewardship_zone.md
  - ../../../../contracts/domains/habitat/ecological_system.md
  - ../../../../contracts/domains/habitat/land_cover/observation.md
  - ../../../../contracts/domains/habitat/land_cover/model_run_receipt.md
  - ../../../../contracts/domains/habitat/land_cover/uncertainty.md
  - ../../../../schemas/contracts/v1/domains/habitat/restoration_opportunity.schema.json
  - ../../../../fixtures/domains/habitat/restoration_opportunity/
  - ../../../../policy/domains/habitat/restoration.rego
  - ../../../../policy/sensitivity/habitat/
  - ../../../../pipelines/domains/habitat/
  - ../../../../pipeline_specs/habitat/
  - ../../../../data/registry/sources/habitat/
  - ../../../../release/manifests/habitat/
notes:
  - "This file replaces a blank placeholder at tests/domains/habitat/test_restoration/README.md."
  - "This is a test-lane README only. It does not define Habitat restoration doctrine, semantic contracts, schemas, fixtures, lifecycle records, evidence bundles, receipts, policy rules, release decisions, pipeline code, public API material, public map material, public tiles, or published artifacts."
  - "The tested invariant is that RestorationOpportunity is a governed candidate/evidence object. It must preserve candidate identity, spatial scope, opportunity rationale, supporting evidence, method support, source-role lineage, temporal scope, policy posture, review state, release relationship, correction, and rollback without becoming restoration approval, management order, land-access clearance, funding eligibility, regulatory designation, source truth, release authority, public-layer truth, or AI/UI truth."
  - "Default posture is deterministic and no-network. Live source checks, real source exports, lifecycle data, public tiles, and restricted joined records do not belong in this lane."
  - "Rollback target for this replacement is previous blank blob SHA 8b137891791fe96927ad78e64b0aad7bded08bdc."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Habitat restoration tests

> Deterministic, no-network test documentation for proving that Habitat `RestorationOpportunity` records remain candidate/evidence objects with inspectable evidence, source-role lineage, policy posture, review state, release relationship, correction path, and rollback target.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: tests" src="https://img.shields.io/badge/root-tests%2F-blue">
  <img alt="Domain: habitat" src="https://img.shields.io/badge/domain-habitat-2e7d32">
  <img alt="Lane: restoration" src="https://img.shields.io/badge/lane-restoration-blue">
  <img alt="Network: disabled by default" src="https://img.shields.io/badge/network-disabled__by__default-critical">
  <img alt="Boundary: candidate not directive" src="https://img.shields.io/badge/boundary-candidate__not__directive-success">
</p>

**Path:** `tests/domains/habitat/test_restoration/README.md`  
**Status:** draft / placeholder-expanded / PROPOSED until executable tests are verified  
**Owning root:** `tests/`  
**Domain segment:** `habitat`  
**Test lane:** `test_restoration`  
**Default execution posture:** deterministic, synthetic, no-network, public-safe fixtures only  
**Truth posture:** CONFIRMED target was a blank placeholder before this expansion · CONFIRMED `tests/` is the canonical root for enforceability proof · CONFIRMED `RestorationOpportunity` is a Habitat object-family term with PROPOSED field realization · CONFIRMED the Restoration Opportunity contract defines it as a candidate/evidence object and not restoration approval, management order, land-access clearance, funding eligibility, regulatory designation, or release authority · CONFIRMED the paired schema is a scaffold and field-level enforcement remains NEEDS VERIFICATION · NEEDS VERIFICATION for executable test modules, fixture payload inventory, validator behavior, source registry activation, policy runtime, release integration, public route/UI behavior, CI coverage, and pass rates.

**Quick jumps:** [Purpose](#purpose) · [Placement basis](#placement-basis) · [Invariant under test](#invariant-under-test) · [Expected scope](#expected-scope) · [Fixture posture](#fixture-posture) · [Assertions](#assertions) · [Finite outcomes](#finite-outcomes) · [Forbidden shortcuts](#forbidden-shortcuts) · [Suggested layout](#suggested-layout) · [Run posture](#run-posture) · [Evidence ledger](#evidence-ledger) · [Validation checklist](#validation-checklist) · [Rollback](#rollback)

---

## Purpose

`tests/domains/habitat/test_restoration/` is the intended home for Habitat restoration-opportunity tests.

This lane should prove that `RestorationOpportunity` records preserve candidate identity, spatial scope, evidence, source role, method, uncertainty, policy, review, release, correction, and rollback boundaries. It should also prove that opportunity candidates do not collapse into approval, directive, eligibility, access, regulatory, public-layer, or AI-generated truth.

A passing test here should **not** mean that a real opportunity is admitted, a restoration action is authorized, a public geometry is safe, or a release is approved. It should mean only that restoration-opportunity guardrails behaved as expected against bounded fixtures.

---

## Placement basis

`tests/` is the canonical root for enforceability proof. Habitat is a domain segment inside that root. `test_restoration` is a test lane, not a new root and not a parallel contract, schema, policy, data, release, proof, or public-map home.

| Responsibility | Correct home | This lane's relationship |
|---|---|---|
| Restoration tests | `tests/domains/habitat/test_restoration/` | This directory. |
| RestorationOpportunity meaning | `contracts/domains/habitat/restoration_opportunity.md` | Semantic contract under test. |
| Machine schema | `schemas/contracts/v1/domains/habitat/restoration_opportunity.schema.json` | Referenced where accepted; scaffold posture must be respected. |
| Fixtures | `fixtures/domains/habitat/restoration_opportunity/` | Preferred toy inputs and expected outcomes if populated. |
| Supporting Habitat objects | `habitat_patch`, `habitat_quality_score`, `SuitabilityModel`, `connectivity_edge`, `corridor`, `stewardship_zone`, `ecological_system` | Inputs or context; they do not become restoration approval. |
| Policy homes | `policy/domains/habitat/restoration.rego`, `policy/sensitivity/habitat/` | Referenced by tests, not bypassed here. |
| Release decisions | `release/` and `release/manifests/habitat/` | Publication, correction, and rollback authority; tests cannot replace it. |

---

## Invariant under test

> **RestorationOpportunity is a candidate, not a decision.** A Habitat restoration opportunity records where restoration may be worth review, why it may be worth review, which evidence supports that interpretation, and which policy/review/release gates must resolve before public or operational use.

Core checks:

| Check | Required behavior | Failure outcome |
|---|---|---|
| Candidate identity | Stable ID, object role, spatial scope, temporal scope, method/config digest, and candidate digest are explicit. | validation failure / `ERROR`. |
| Candidate scope | Patch, polygon, corridor segment, grid cell, watershed, generalized area, or analysis unit is explicit with exposure posture. | validation failure / `DENY`. |
| Opportunity rationale | Evidence-supported reason for candidacy is declared and bounded. | validation failure / `ABSTAIN`. |
| Supporting evidence | Input observations, scores, models, patches, corridors, stewardship context, and source artifacts are cited where material. | `ABSTAIN`. |
| Method support | Model/run receipt, thresholds, weights, method card, and uncertainty refs are attached where material. | validation failure / review required. |
| Source-role lineage | Observed, modeled, regulatory, derivative, context, and candidate roles remain visible and do not collapse. | validation failure. |
| Policy and review | Review state and policy decision are explicit before public use. | hold / promotion block. |
| Release boundary | Release, correction, and rollback remain separate from test pass state. | promotion block. |
| No authority upgrade | Candidate cannot become approval, directive, eligibility, access clearance, regulatory truth, public-layer truth, or AI truth. | validation failure / `ABSTAIN`. |

---

## Expected scope

Tests in this lane may validate:

- required candidate identity, spatial scope, opportunity rationale, source role, evidence, method, uncertainty, temporal scope, and digest posture;
- rejection of opportunity-as-approval, opportunity-as-instruction, opportunity-as-eligibility, opportunity-as-access, or opportunity-as-regulatory-designation misuse;
- model-run receipt and uncertainty requirements where the candidate is model-derived;
- public-safe scope and policy posture before map/API/UI/AI carrier use;
- rejection of public-facing candidates that lack evidence, policy, review, release relationship, correction, or rollback context;
- finite outcomes when evidence resolver, policy engine, model-run receipt, uncertainty support, source registry activation, or release manifest is missing.

Live source checks, real source exports, production candidate geometry, public tile generation, restricted joined records, and provider-backed model calls are out of scope for the default suite.

---

## Fixture posture

Use synthetic, public-safe fixtures only.

Fixture requirements:

- deterministic and no-network;
- compact enough for review in a PR;
- explicit expected outcome;
- explicit candidate identity, candidate role, spatial scope, rationale, method, source-role lineage, evidence, uncertainty, policy, review, release relationship, correction, and rollback posture where material;
- no real source exports, lifecycle data, production candidate geometry, public tiles, restricted joined records, or published artifacts.

Preferred fixture families:

| Fixture kind | Expected outcome |
|---|---|
| Valid synthetic RestorationOpportunity with rationale, evidence, method, uncertainty, review, and release relationship | accepted candidate support only. |
| Missing candidate identity or rationale | validation failure / `ERROR`. |
| Candidate treated as approval or directive | validation failure. |
| Candidate treated as eligibility, access clearance, or regulatory designation | validation failure / `ABSTAIN`. |
| Model-derived candidate missing receipt or uncertainty | review required / `ABSTAIN`. |
| Public output lacks release/correction/rollback posture | promotion block. |
| AI/UI answer treats candidate as decision truth | `ABSTAIN` / validation failure. |

---

## Assertions

A useful Habitat restoration test should make the candidate-not-decision boundary obvious.

### Positive path

- candidate identity, role, scope, and rationale are explicit;
- supporting evidence, method, source-role lineage, and temporal support are visible;
- model-run, method-card, uncertainty, and validation support are linkable where material;
- policy, review, release relationship, correction, and rollback references are linkable where material;
- public-safe scope and exposure posture are explicit where material.

### Negative path

- opportunity cannot become approval or directive;
- opportunity cannot become funding/program eligibility, access clearance, regulatory designation, or release authority;
- candidate geometry cannot hide provenance, uncertainty, or exposure posture;
- test pass cannot become release approval;
- map style, tile, popup, graph edge, Focus Mode answer, or AI text cannot become restoration authority;
- missing evidence produces `ABSTAIN` rather than a fluent claim.

---

## Finite outcomes

| Condition | Expected outcome |
|---|---|
| Valid synthetic RestorationOpportunity with rationale, evidence, method, uncertainty, policy, review, release relationship, correction, and rollback context | accepted candidate support only. |
| Missing candidate identity, rationale, source role, spatial/temporal scope, method, or digest basis | validation failure / `ERROR`. |
| Candidate treated as approval, directive, eligibility, access clearance, regulatory designation, or release authority | validation failure. |
| Model-derived candidate lacks receipt or uncertainty | review required / `ABSTAIN`. |
| Public-facing candidate lacks release/correction/rollback posture | promotion-blocking failure. |
| Policy engine unavailable | `ERROR` or `ABSTAIN`, never public exposure. |

---

## Forbidden shortcuts

Do not use this test lane to:

- fetch live upstream source systems;
- store real source exports, lifecycle data, production candidate geometry, public tiles, or release artifacts;
- store proof packs, release manifests, or generated public layers;
- redefine Habitat restoration doctrine, contracts, schemas, fixtures, policy rules, receipts, proofs, release decisions, renderer code, or production code;
- bypass source role, candidate rationale, method support, evidence, uncertainty, validation, policy, review, correction, or rollback checks with a fixture flag;
- infer release state from file existence, test success, layer name, candidate label, map rendering, tile availability, or AI wording;
- publish, promote, approve, direct, or release anything.

Any test that needs real candidate outputs, source data, or public tile output belongs in a gated integration tier with source admission, lifecycle state, policy, receipts, release controls, and rollback targets.

---

## Suggested layout

The exact test module names remain **NEEDS VERIFICATION** until the runner and existing conventions are inspected.

```text
tests/domains/habitat/test_restoration/
├── README.md
├── test_restoration_candidate_identity.py
├── test_candidate_scope_and_rationale.py
├── test_candidate_not_decision.py
├── test_method_evidence_and_uncertainty.py
├── test_policy_review_required.py
└── test_release_correction_rollback.py
```

---

## Run posture

```bash
pytest tests/domains/habitat/test_restoration
```

Status of the command above: **PROPOSED / NEEDS VERIFICATION**. It assumes `pytest` is the accepted test runner and that executable test modules exist. This README does not claim the command currently passes.

---

## Evidence ledger

| Evidence | Status | Supports | Limits |
|---|---|---|---|
| Previous target file | CONFIRMED | `tests/domains/habitat/test_restoration/README.md` existed as a blank placeholder before this replacement. | Did not define the lane. |
| `tests/README.md` | CONFIRMED | `tests/` is enforceability proof and failure should block promotion where trust-spine checks fail. | Does not prove this lane's modules or pass rate. |
| `contracts/domains/habitat/restoration_opportunity.md` | CONFIRMED semantic contract / PROPOSED implementation | Defines `RestorationOpportunity` as a candidate/evidence object and not restoration approval, management order, land-access decision, funding eligibility, regulatory designation, or release authority. | Schema is a permissive scaffold and field-level enforcement remains NEEDS VERIFICATION. |
| Repo search | CONFIRMED | No specific README result for restoration-opportunity fixtures/tests was found in the searched terms before this replacement. | Search is not proof of absence; fixture payload inventory remains NEEDS VERIFICATION. |

---

## Validation checklist

Before treating this README as implemented behavior, verify:

- [ ] Executable test modules exist under this lane.
- [ ] Test runner and import paths match the repo's accepted convention.
- [ ] Synthetic fixtures exist for valid candidate, missing identity, missing rationale, candidate-as-approval, candidate-as-directive, candidate-as-eligibility, missing receipt, missing uncertainty, missing policy/review, and missing release/correction/rollback cases.
- [ ] RestorationOpportunity schema path and field expectations are accepted beyond scaffold status.
- [ ] EvidenceRef / EvidenceBundle behavior is available to tests or safely stubbed.
- [ ] ModelRunReceipt, method-card, and UncertaintySurface behavior is available to tests or safely stubbed.
- [ ] PolicyDecision, ReviewRecord, ReleaseManifest, CorrectionNotice, RedactionReceipt, and RollbackCard expectations are defined before enforcing them.
- [ ] CI runs the no-network Habitat restoration suite.
- [ ] Failures block public carrier promotion or release candidate approval.

---

## Rollback

Rollback is required if this lane becomes a source export store, candidate-output store, lifecycle data store, fixture root, contract root, schema authority, policy authority, proof store, release-decision root, public map/API/tile surface, AI surface, renderer implementation, pipeline implementation, or publication shortcut.

Rollback target for this replacement: previous blank blob SHA `8b137891791fe96927ad78e64b0aad7bded08bdc`.

<p align="right"><a href="#top">Back to top</a></p>
