<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-domains-habitat-policy-readme
title: Habitat Policy Test README
type: test-readme
version: v0.1
status: draft; placeholder-expanded; policy-test-lane; PROPOSED / NEEDS VERIFICATION before promotion
owners:
  - OWNER_TBD — Habitat domain steward
  - OWNER_TBD — Policy steward
  - OWNER_TBD — Sensitivity steward
  - OWNER_TBD — Evidence steward
  - OWNER_TBD — Validation steward
  - OWNER_TBD — Release steward
  - OWNER_TBD — QA steward
created: NEEDS VERIFICATION — blank placeholder existed before v0.1 expansion
updated: 2026-07-05
policy_label: public-doc; tests; habitat; policy; no-network; deny-by-default; policy-as-code-parity; inherited-sensitivity-aware; release-gated
tags: [kfm, tests, habitat, policy, sensitivity, deny-by-default, PolicyDecision, RedactionReceipt, ReviewRecord, ReleaseManifest, AIReceipt, EvidenceBundle, ABSTAIN, DENY, RESTRICT, ALLOW]
related:
  - ../../../README.md
  - ../README.md
  - ../../../../docs/domains/habitat/SENSITIVITY_POLICY.md
  - ../../../../docs/domains/habitat/HABITAT_SENSITIVITY_PROFILE.md
  - ../../../../docs/domains/habitat/MODEL_VS_OBSERVATION.md
  - ../../../../docs/domains/habitat/sublanes/land_cover.md
  - ../../../../docs/domains/habitat/sublanes/ecoregions.md
  - ../../../../docs/architecture/cross-lane-join-policy.md
  - ../../../../docs/doctrine/policy-aware.md
  - ../../../../docs/doctrine/sensitivity.md
  - ../../../../policy/domains/habitat/README.md
  - ../../../../policy/sensitivity/
  - ../../../../policy/runtime/
  - ../../../../policy/promotion/
  - ../../../../policy/release/
  - ../../../../policy/rights/
  - ../../../../schemas/contracts/v1/policy/
  - ../../../../release/manifests/habitat/
notes:
  - "This file replaces a blank placeholder at tests/domains/habitat/policy/README.md."
  - "This is a test-lane README only. It does not define Habitat policy, sensitivity rules, Rego bundles, schemas, fixtures, evidence bundles, receipts, release decisions, runtime behavior, public API material, public map material, or published artifacts."
  - "The tested invariant is that Habitat policy tests verify allow/restrict/deny/abstain behavior and policy-as-code parity without relocating policy authority into tests or docs."
  - "Habitat sensitivity may be inherited from joined lanes such as fauna or flora; Habitat-owned rules require verified policy homes or an ADR."
  - "Rollback target for this replacement is previous blank blob SHA 8b137891791fe96927ad78e64b0aad7bded08bdc."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Habitat policy tests

> Deterministic, no-network test documentation for Habitat policy and sensitivity enforcement checks. This lane verifies policy behavior; it does not own policy authority.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: tests" src="https://img.shields.io/badge/root-tests%2F-blue">
  <img alt="Domain: habitat" src="https://img.shields.io/badge/domain-habitat-2e7d32">
  <img alt="Lane: policy" src="https://img.shields.io/badge/lane-policy-blue">
  <img alt="Network: disabled by default" src="https://img.shields.io/badge/network-disabled__by__default-critical">
  <img alt="Boundary: tests not policy" src="https://img.shields.io/badge/boundary-tests__not__policy-success">
</p>

**Path:** `tests/domains/habitat/policy/README.md`  
**Status:** draft / placeholder-expanded / PROPOSED until executable tests are verified  
**Owning root:** `tests/`  
**Domain segment:** `habitat`  
**Test lane:** `policy`  
**Default execution posture:** deterministic, synthetic, no-network, public-safe fixtures only  
**Truth posture:** CONFIRMED target was a blank placeholder before this expansion · CONFIRMED `tests/` is the canonical root for enforceability proof · CONFIRMED Habitat sensitivity documentation is an index that points into `policy/` and does not own enforceable rules · CONFIRMED `policy/domains/habitat/README.md` exists as a proposed greenfield scaffold · NEEDS VERIFICATION for executable test modules, policy bundle shape, policy fixtures, policy runtime, schema enforcement, CI coverage, and pass rates.

**Quick jumps:** [Purpose](#purpose) · [Placement basis](#placement-basis) · [Invariant under test](#invariant-under-test) · [Expected scope](#expected-scope) · [Fixture posture](#fixture-posture) · [Finite outcomes](#finite-outcomes) · [Forbidden shortcuts](#forbidden-shortcuts) · [Suggested layout](#suggested-layout) · [Run posture](#run-posture) · [Evidence ledger](#evidence-ledger) · [Validation checklist](#validation-checklist) · [Rollback](#rollback)

---

## Purpose

`tests/domains/habitat/policy/` is the intended home for Habitat policy tests.

This lane should prove that Habitat-facing policy behavior is enforceable, deterministic, and consistent across CI and runtime expectations. It should also prove that policy authority remains under `policy/`, while docs index policy and tests verify policy behavior.

A passing test here should **not** mean that a Habitat record is publishable, that a release is approved, or that a docs page owns a rule. It should mean only that tested policy fixtures produced the expected finite outcome and did not cross trust boundaries.

---

## Placement basis

`tests/` is the canonical root for enforceability proof. Habitat is a domain segment inside that root. `policy` is a test lane, not a policy root.

| Responsibility | Correct home | This lane's relationship |
|---|---|---|
| Habitat policy tests | `tests/domains/habitat/policy/` | This directory. |
| Habitat policy authority | `policy/domains/habitat/` where verified or accepted by ADR | Tests verify behavior; they do not own rules. |
| Inherited sensitivity rules | `policy/sensitivity/<owning-domain>/` where verified | Habitat joins may inherit rules from joined lanes. |
| Runtime policy | `policy/runtime/` | Runtime allow/restrict/deny/abstain behavior under test. |
| Promotion/release policy | `policy/promotion/`, `policy/release/` | Publication gates under test. |
| Rights policy | `policy/rights/` | Rights and license gates under test. |
| Policy schemas | `schemas/contracts/v1/policy/` | Shape checks where accepted. |
| Habitat policy navigation | `docs/domains/habitat/SENSITIVITY_POLICY.md` | Index only; not a rule source. |
| Release records | `release/manifests/habitat/` | Release authority; tests cannot replace it. |

---

## Invariant under test

> **Policy tests verify policy; they do not become policy.** Habitat policy tests must check finite policy outcomes, inherited sensitivity posture, evidence requirements, rights posture, review state, release gates, correction paths, and rollback expectations without defining rules in tests or docs.

Core checks:

| Check | Required behavior | Failure outcome |
|---|---|---|
| Policy home | Rule authority is under `policy/`, not `docs/` or `tests/`. | validation failure. |
| Finite outcomes | Policy returns explicit `ALLOW`, `RESTRICT`, `DENY`, `ABSTAIN`, `HOLD`, or `ERROR` posture as accepted by the policy contract. | validation failure. |
| Inherited sensitivity | Habitat joins preserve the most restrictive joined-lane policy where applicable. | `DENY` / `RESTRICT` / `ABSTAIN`. |
| Evidence gate | Consequential public answers require evidence support. | `ABSTAIN`. |
| Rights gate | Rights-unclear or restricted-source contexts do not pass as public-safe. | `DENY` / `RESTRICT` / `HOLD`. |
| Review gate | Review-required contexts do not publish by fixture success. | promotion block. |
| Release gate | Release state remains separate from policy test pass state. | validation failure. |
| Runtime parity | CI and runtime policy expectations remain aligned where verified. | validation failure / NEEDS VERIFICATION. |
| Correction/rollback | Public-facing cases retain correction and rollback expectations. | promotion block. |

---

## Expected scope

Tests in this lane may validate:

- policy fixture loading for Habitat-owned and inherited policy cases;
- allow/restrict/deny/abstain finite outcomes;
- denial when public clients attempt to read unreleased, candidate, fixture, proposed-work, or internal state;
- abstention when evidence support is unresolved;
- restriction or denial when joined-lane sensitivity applies;
- rights and source-role gates for Habitat-derived records;
- promotion/release gates for public map/API/AI carriers;
- correction and rollback obligations for public-facing cases;
- failure when docs text or tests attempt to become policy authority.

Live source checks, public tile generation, production credentials, and real sensitive records are out of scope for the default suite.

---

## Fixture posture

Use synthetic policy fixtures only.

Fixture requirements:

- deterministic and no-network;
- public-safe and compact;
- explicit expected finite outcome;
- explicit evidence, source role, rights, sensitivity, review, release, correction, and rollback posture where material;
- no real sensitive records, real source exports, lifecycle data, public tiles, release artifacts, credentials, or production policy secrets.

Preferred fixture families:

| Fixture kind | Expected outcome |
|---|---|
| Public-safe Habitat summary with evidence and release relationship | `ALLOW` or accepted public-safe outcome. |
| Missing evidence for a consequential claim | `ABSTAIN`. |
| Rights unclear | `HOLD`, `RESTRICT`, or `DENY`. |
| Joined-lane sensitivity present | most-restrictive finite outcome. |
| Candidate or proposed-work object requested by public UI | `DENY`. |
| Release state missing for public carrier | promotion-blocking failure. |
| Docs text treated as policy rule | validation failure. |
| Test fixture success treated as release approval | validation failure. |

---

## Finite outcomes

This lane should avoid ambiguous pass/fail language where a policy disposition is required.

| Condition | Expected outcome |
|---|---|
| Valid public-safe fixture with evidence, policy, review, release relationship, correction, and rollback context | `ALLOW` or accepted public-safe carrier outcome. |
| Evidence missing | `ABSTAIN`. |
| Joined-lane sensitivity unresolved | `RESTRICT`, `DENY`, `HOLD`, or `ABSTAIN` according to policy. |
| Rights unclear | `HOLD`, `RESTRICT`, or `DENY`. |
| Candidate/proposed-work/internal state requested by public surface | `DENY`. |
| Policy bundle unavailable | `ERROR` or `ABSTAIN`, never public exposure. |
| Docs or tests define a concrete rule | validation failure. |
| Policy test pass treated as release approval | validation failure. |

---

## Forbidden shortcuts

Do not use this test lane to:

- define or restate enforceable policy rules;
- store policy bundles as test files;
- store real sensitive records, source exports, lifecycle data, public tiles, or release artifacts;
- store credentials, tokens, or production policy secrets;
- bypass evidence, rights, sensitivity, review, release, correction, or rollback checks;
- infer release state from test success, fixture success, file existence, layer name, map rendering, tile availability, or AI wording;
- publish, promote, or release anything.

Any live policy bundle or runtime parity check should be in a gated CI/integration tier with explicit fixtures and rollback expectations.

---

## Suggested layout

The exact test module names remain **NEEDS VERIFICATION** until the runner and existing test conventions are inspected.

```text
tests/domains/habitat/policy/
├── README.md
├── test_policy_home_boundary.py
├── test_finite_outcomes.py
├── test_inherited_sensitivity.py
├── test_evidence_and_rights_gates.py
├── test_public_surface_denials.py
└── test_release_correction_rollback.py
```

---

## Run posture

```bash
pytest tests/domains/habitat/policy
```

Status of the command above: **PROPOSED / NEEDS VERIFICATION**. It assumes `pytest` is the accepted test runner and that executable test modules exist. This README does not claim the command currently passes.

---

## Evidence ledger

| Evidence | Status | Supports | Limits |
|---|---|---|---|
| Previous target file | CONFIRMED | `tests/domains/habitat/policy/README.md` existed as a blank placeholder before this replacement. | Did not define the lane. |
| `tests/README.md` | CONFIRMED | `tests/` is enforceability proof and failure should block promotion where trust-spine checks fail. | Does not prove this lane's modules or pass rate. |
| `docs/domains/habitat/SENSITIVITY_POLICY.md` | CONFIRMED docs-side index | Habitat sensitivity policy documentation is an index only; enforceable rules live under `policy/`; docs must not restate concrete policy logic. | Specific Habitat policy paths are partly PROPOSED and require verification. |
| `policy/domains/habitat/README.md` | CONFIRMED greenfield scaffold | Habitat domain policy home exists as a proposed scaffold. | Does not prove real policy bundles, fixtures, validators, or runtime wiring. |
| Repo search | CONFIRMED | Related sensitivity, release, rights, runtime, and Habitat policy docs exist or are referenced. | Search results do not prove enforcement. |

---

## Validation checklist

Before treating this README as implemented behavior, verify:

- [ ] Executable test modules exist under this lane.
- [ ] Policy fixture locations are accepted and populated with synthetic cases.
- [ ] Test runner and policy runner are known and documented.
- [ ] Habitat-owned policy homes are accepted or marked PROPOSED/UNKNOWN.
- [ ] Inherited sensitivity policy behavior is available to tests or safely stubbed.
- [ ] EvidenceRef / EvidenceBundle behavior is available to tests or safely stubbed.
- [ ] PolicyDecision, RedactionReceipt, ReviewRecord, ReleaseManifest, CorrectionNotice, AIReceipt, and RollbackCard expectations are defined before enforcing them.
- [ ] CI runs the no-network Habitat policy suite.
- [ ] Failures block public carrier promotion or release candidate approval.

---

## Rollback

Rollback is required if this lane becomes a policy authority, source of rules, policy bundle home, source export store, lifecycle data store, fixture root, schema authority, proof store, release-decision root, public map/API/tile surface, AI surface, renderer implementation, pipeline implementation, or publication shortcut.

Rollback target for this replacement: previous blank blob SHA `8b137891791fe96927ad78e64b0aad7bded08bdc`.

<p align="right"><a href="#top">Back to top</a></p>
