<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-domains-hydrology-policy-readme
title: Hydrology Policy Test README
type: test-readme
version: v0.1
status: draft; placeholder-expanded; policy-test-lane; PROPOSED / NEEDS VERIFICATION before promotion
owners:
  - OWNER_TBD — Hydrology domain steward
  - OWNER_TBD — Policy steward
  - OWNER_TBD — Source steward
  - OWNER_TBD — Evidence steward
  - OWNER_TBD — Validation steward
  - OWNER_TBD — Release steward
  - OWNER_TBD — QA steward
created: NEEDS VERIFICATION — blank placeholder existed before v0.1 expansion
updated: 2026-07-05
policy_label: public-doc; tests; hydrology; policy; no-network; deny-by-default; evidence-bound; source-role-aware; sensitivity-aware; release-gated; rollback-aware
tags: [kfm, tests, hydrology, policy, PolicyDecision, source-role, permitted-claims, not-authoritative-for, EvidenceBundle, ReleaseManifest, CorrectionNotice, RollbackCard, ABSTAIN, DENY, ERROR]
related:
  - ../../../README.md
  - ../README.md
  - ../identity/README.md
  - ../no_network/README.md
  - ../continuity_inventory_check/README.md
  - ../../../../docs/domains/hydrology/PUBLICATION_POSTURE.md
  - ../../../../docs/domains/hydrology/SOURCE_ROLE_MATRIX.md
  - ../../../../docs/domains/hydrology/SOURCE_REGISTRY.md
  - ../../../../docs/domains/hydrology/SOURCE_FAMILIES.md
  - ../../../../docs/domains/hydrology/DATA_LIFECYCLE.md
  - ../../../../docs/domains/hydrology/BOUNDARY.md
  - ../../../../docs/domains/hydrology/IDENTITY_MODEL.md
  - ../../../../docs/architecture/sensitivity-tiers.md
  - ../../../../docs/standards/SENSITIVITY_RUBRIC.md
  - ../../../../policy/domains/hydrology/
  - ../../../../policy/sensitivity/hydrology/
  - ../../../../contracts/policy/policy_decision.md
  - ../../../../contracts/evidence/evidence_bundle.md
  - ../../../../contracts/release/release_manifest.md
  - ../../../../contracts/domains/hydrology/
  - ../../../../schemas/contracts/v1/domains/hydrology/
  - ../../../../fixtures/domains/hydrology/policy/
  - ../../../../data/registry/sources/hydrology/
  - ../../../../release/manifests/hydrology/
notes:
  - "This file replaces a blank placeholder at tests/domains/hydrology/policy/README.md."
  - "This is a test-lane README only. It does not define Hydrology doctrine, policy rules, sensitivity rules, contracts, schemas, fixtures, source descriptors, lifecycle records, EvidenceBundles, release decisions, pipeline code, public API material, public map material, public tiles, or published artifacts."
  - "The tested invariant is that Hydrology policy checks preserve fail-closed behavior for publication posture, source-role anti-collapse, evidence closure, rights/sensitivity posture, emergency/life-safety boundaries, release relationship, correction, and rollback."
  - "Default posture is deterministic and no-network. Live source checks, real source exports, lifecycle data, public tiles, and restricted records do not belong in this lane."
  - "Rollback target for this replacement is previous blank blob SHA 8b137891791fe96927ad78e64b0aad7bded08bdc."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Hydrology policy tests

> Deterministic, no-network test documentation for proving that Hydrology policy gates fail closed when evidence, source role, rights, sensitivity, lifecycle, release, correction, or rollback posture is unresolved.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: tests" src="https://img.shields.io/badge/root-tests%2F-blue">
  <img alt="Domain: hydrology" src="https://img.shields.io/badge/domain-hydrology-2aa1c6">
  <img alt="Lane: policy" src="https://img.shields.io/badge/lane-policy-blue">
  <img alt="Network: disabled by default" src="https://img.shields.io/badge/network-disabled__by__default-critical">
  <img alt="Boundary: fail closed" src="https://img.shields.io/badge/boundary-fail__closed-success">
</p>

**Path:** `tests/domains/hydrology/policy/README.md`  
**Status:** draft / placeholder-expanded / PROPOSED until executable tests are verified  
**Owning root:** `tests/`  
**Domain segment:** `hydrology`  
**Test lane:** `policy`  
**Default execution posture:** deterministic, synthetic, no-network, public-safe fixtures only  
**Truth posture:** CONFIRMED target was a blank placeholder before this expansion · CONFIRMED `tests/` is the canonical root for enforceability proof · CONFIRMED Hydrology publication posture blocks public promotion for unclear rights, unresolved source role, missing EvidenceBundle closure, absent ReleaseManifest, and NFHL-as-observed-flood collapse · CONFIRMED Hydrology source-role doctrine says role is fixed at admission, preserved through promotion, and fails closed when conflated · NEEDS VERIFICATION for executable policy tests, fixture payload inventory, OPA/runtime wiring, schema enforcement, source registry activation, release integration, CI coverage, and pass rates.

---

## Purpose

`tests/domains/hydrology/policy/` is the intended home for Hydrology policy tests.

This lane should prove that policy checks around Hydrology claims remain finite, auditable, and fail-closed. Policy tests should verify that unresolved rights, sensitivity, source role, evidence closure, lifecycle state, publication posture, correction state, or rollback target produce `DENY`, `ABSTAIN`, `ERROR`, `HOLD`, or another explicit non-publishing outcome instead of silent promotion.

A passing test here should **not** mean that a real hydrology source is admitted, a public layer is safe, policy rules are complete, or a release is approved. It should mean only that policy guardrails behaved as expected against bounded fixtures.

---

## Placement basis

`tests/` is the canonical root for enforceability proof. Hydrology is a domain segment inside that root. `policy/` is a test lane, not the policy-authority home, schema home, source registry, lifecycle store, proof store, release home, public API surface, or public map surface.

| Responsibility | Correct home | This lane's relationship |
|---|---|---|
| Hydrology policy tests | `tests/domains/hydrology/policy/` | This directory. |
| Policy rules | `policy/domains/hydrology/`, `policy/sensitivity/hydrology/` | Systems under test where populated; not redefined here. |
| Publication posture | `docs/domains/hydrology/PUBLICATION_POSTURE.md` | Doctrine under test; not policy runtime. |
| Source-role matrix | `docs/domains/hydrology/SOURCE_ROLE_MATRIX.md` | Human-readable source-role guardrail under test. |
| Source descriptors | `data/registry/sources/hydrology/` | Canonical source-role and rights context; not duplicated here. |
| Machine schemas | `schemas/contracts/v1/domains/hydrology/` | Shape checks where accepted. |
| Synthetic fixtures | `fixtures/domains/hydrology/policy/` | Preferred toy inputs and expected outcomes if populated. |
| Release decisions | `release/` and `release/manifests/hydrology/` | Publication, correction, and rollback authority; tests cannot replace it. |

---

## Invariant under test

> **Hydrology policy gates fail closed.** When rights, sensitivity, source role, evidence, lifecycle, release, correction, rollback, or emergency-boundary posture is unresolved, Hydrology policy returns a finite non-publishing outcome. Policy tests do not approve publication; they prove blocked and allowed paths are distinguishable.

Core checks:

| Check | Required behavior | Failure outcome |
|---|---|---|
| Source-role gate | Observed, regulatory, modeled, aggregate, administrative, candidate, and synthetic roles remain distinct. | validation failure / `DENY` / `ABSTAIN`. |
| Permitted-claim gate | A source family may prove only claims allowed by its SourceDescriptor / role matrix. | `DENY` / validation failure. |
| Evidence gate | Evidence-dependent public claims require EvidenceRef / EvidenceBundle closure. | `ABSTAIN`. |
| Rights gate | Unknown or changed rights block public promotion. | `DENY` / `HOLD`. |
| Sensitivity gate | Sensitive joins, infrastructure/private-property implications, or unclear exposure posture require review/generalization/denial. | `DENY` / `HOLD` / `ABSTAIN`. |
| Flood-role gate | NFHL/regulatory flood context cannot be presented as observed inundation. | `DENY`. |
| Lifecycle gate | Non-published, raw, work, quarantine, processed, catalog-only, or candidate material cannot be public authority. | validation failure / `DENY`. |
| Release gate | ReleaseManifest, correction path, and rollback target are required before public carriers. | promotion-blocking failure. |

---

## Expected scope

Tests in this lane may validate:

- allow/deny/abstain/error behavior for synthetic Hydrology policy decisions;
- unresolved source role blocking public promotion;
- missing EvidenceBundle closure producing `ABSTAIN`;
- missing or unclear rights producing `DENY` or `HOLD`;
- NFHL regulatory context rejected as observed flood evidence;
- candidate or synthetic material blocked from public claims;
- missing ReleaseManifest or rollback target blocking public carrier promotion;
- policy-version drift and correction-state fixtures where material.

Live source checks, real source exports, production credentials, public tile generation, and real hydrology payloads are out of scope for the default suite.

---

## Fixture posture

Use synthetic, public-safe fixtures only.

Fixture requirements:

- deterministic and no-network;
- compact enough for review in a PR;
- explicit expected outcome;
- explicit source role, permitted claim, evidence posture, rights posture, sensitivity posture, lifecycle state, policy state, release relationship, correction, and rollback posture where material;
- no real source exports, lifecycle data, public tiles, credentials, restricted records, or published artifacts.

---

## Finite outcomes

| Condition | Expected outcome |
|---|---|
| Public-safe fixture has source role, evidence, rights, policy, release, correction, and rollback support | accepted policy support only. |
| Source role unresolved or conflated | `DENY` / `ABSTAIN` / validation failure. |
| Missing EvidenceBundle closure | `ABSTAIN`. |
| Rights or terms unclear | `DENY` / `HOLD`. |
| Sensitive join or infrastructure/private-property implication unresolved | `DENY` / `HOLD` / `ABSTAIN`. |
| NFHL regulatory context asserted as observed flood event | `DENY`. |
| Missing ReleaseManifest or rollback target | promotion-blocking failure. |
| Policy runtime unavailable | `ERROR` or `ABSTAIN`, never public exposure. |

---

## Suggested layout

```text
tests/domains/hydrology/policy/
├── README.md
├── test_policy_decision_shape.py
├── test_source_role_gate.py
├── test_permitted_claims_gate.py
├── test_evidence_closure_required.py
├── test_rights_and_sensitivity_fail_closed.py
├── test_flood_role_collapse_denied.py
├── test_lifecycle_publication_gate.py
└── test_release_correction_rollback_required.py
```

---

## Run posture

```bash
pytest tests/domains/hydrology/policy
```

Status of the command above: **PROPOSED / NEEDS VERIFICATION**. It assumes `pytest` is the accepted test runner and that executable test modules exist. This README does not claim the command currently passes.

---

## Evidence ledger

| Evidence | Status | Supports | Limits |
|---|---|---|---|
| Previous target file | CONFIRMED | `tests/domains/hydrology/policy/README.md` existed as a blank placeholder before this replacement. | Did not define the lane. |
| `tests/README.md` | CONFIRMED | `tests/` is enforceability proof and failure should block promotion where trust-spine checks fail. | Does not prove this lane's modules or pass rate. |
| `tests/domains/hydrology/README.md` | CONFIRMED | Hydrology test parent currently exists as a greenfield stub. | Parent lane still needs expansion. |
| `docs/domains/hydrology/PUBLICATION_POSTURE.md` | CONFIRMED doctrine / PROPOSED realization | Defines Hydrology publish/hold/generalize/deny posture, promotion gate to PUBLISHED, release artifacts, correction, stale-state, rollback, and flood-role collapse denial. | It is documentation evidence, not policy runtime proof. |
| `docs/domains/hydrology/SOURCE_ROLE_MATRIX.md` | CONFIRMED doctrine / PROPOSED implementation | Defines source-role matrix, permitted/cannot-prove posture, anti-collapse DENY conditions, and notes registry wins if docs drift. | Concrete policy rules, validators, fixtures, CI, and pass rates remain NEEDS VERIFICATION. |
| Repo search | CONFIRMED | Found Hydrology publication posture and source-role policy docs. | Search is not proof of executable tests or full policy coverage. |

---

## Validation checklist

- [ ] Executable test modules exist under this lane.
- [ ] Test runner and import paths match the repo's accepted convention.
- [ ] Synthetic policy fixtures exist for allow, deny, abstain, error, missing evidence, unresolved source role, unclear rights, sensitive join, NFHL-as-observed-flood, missing release, and missing rollback cases.
- [ ] PolicyDecision shape is accepted or safely stubbed.
- [ ] SourceDescriptor permitted-claims and not-authoritative-for fields are available to tests or safely stubbed.
- [ ] EvidenceRef / EvidenceBundle behavior is available to tests or safely stubbed.
- [ ] ReleaseManifest, CorrectionNotice, RedactionReceipt, and RollbackCard expectations are defined before enforcing them.
- [ ] CI runs the no-network Hydrology policy suite or marks it as an expected gap.
- [ ] Failures block public carrier promotion or release candidate approval where material.

---

## Rollback

Rollback is required if this lane becomes a live source-fetcher, lifecycle data store, source registry, contract root, schema authority, policy authority, proof store, release-decision root, public map/API/tile surface, AI surface, renderer implementation, pipeline implementation, or publication shortcut.

Rollback target for this replacement: previous blank blob SHA `8b137891791fe96927ad78e64b0aad7bded08bdc`.

<p align="right"><a href="#top">Back to top</a></p>
