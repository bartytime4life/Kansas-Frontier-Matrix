<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-domains-hydrology-identity-readme
title: Hydrology Identity Test README
type: test-readme
version: v0.1
status: draft; placeholder-expanded; identity-test-lane; PROPOSED / NEEDS VERIFICATION before promotion
owners:
  - OWNER_TBD — Hydrology domain steward
  - OWNER_TBD — Identity steward
  - OWNER_TBD — Source steward
  - OWNER_TBD — Evidence steward
  - OWNER_TBD — Policy steward
  - OWNER_TBD — Validation steward
  - OWNER_TBD — Release steward
  - OWNER_TBD — QA steward
created: NEEDS VERIFICATION — blank placeholder existed before v0.1 expansion
updated: 2026-07-05
policy_label: public-doc; tests; hydrology; identity; no-network; deterministic-identity; evidence-bound; source-version-aware; ABSTAIN-on-ambiguity; release-gated; rollback-aware
tags: [kfm, tests, hydrology, identity, deterministic-identity, source_id, object_role, temporal_scope, normalized_digest, ReachIdentity, HUCUnit, HydroFeature, GaugeSite, FlowObservation, NFHLZone, EvidenceBundle, PolicyDecision, ReleaseManifest, CorrectionNotice, RollbackCard, ABSTAIN, DENY, ERROR]
related:
  - ../../../README.md
  - ../README.md
  - ../../../../docs/domains/hydrology/IDENTITY_MODEL.md
  - ../../../../docs/domains/hydrology/OBJECT_FAMILIES.md
  - ../../../../docs/domains/hydrology/GLOSSARY.md
  - ../../../../docs/domains/hydrology/BOUNDARY.md
  - ../../../../docs/domains/hydrology/SOURCE_ROLE_MATRIX.md
  - ../../../../docs/domains/hydrology/CONTINUITY_INVENTORY.md
  - ../../../../contracts/domains/hydrology/reach_identity.md
  - ../../../../contracts/domains/hydrology/domain_feature_identity.md
  - ../../../../contracts/domains/hydrology/hydro_feature.md
  - ../../../../contracts/domains/hydrology/huc_unit.md
  - ../../../../contracts/domains/hydrology/upstream_trace.md
  - ../../../../schemas/contracts/v1/domains/hydrology/
  - ../../../../fixtures/domains/hydrology/identity/
  - ../../../../fixtures/domains/hydrology/reach_identity/
  - ../../../../policy/domains/hydrology/
  - ../../../../data/registry/sources/hydrology/
  - ../../../../release/manifests/hydrology/
notes:
  - "This file replaces a blank placeholder at tests/domains/hydrology/identity/README.md."
  - "This is a test-lane README only. It does not define Hydrology doctrine, identity doctrine, contracts, schemas, fixtures, source descriptors, lifecycle records, EvidenceBundles, policy rules, release decisions, pipeline code, public API material, public map material, public tiles, or published artifacts."
  - "The tested invariant is that Hydrology identity remains deterministic, evidence-bounded, source-version-aware, temporal-scope-aware, and object-role-specific. Identity must not be derived from file path, UI handle, incidental serialization, guessed crosswalk, mixed source vintage, release timestamp, or generated text."
  - "Default posture is deterministic and no-network. Live source checks, real source exports, lifecycle data, public tiles, and restricted records do not belong in this lane."
  - "Rollback target for this replacement is previous blank blob SHA 8b137891791fe96927ad78e64b0aad7bded08bdc."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Hydrology identity tests

> Deterministic, no-network test documentation for proving that Hydrology object identity remains source-bound, role-bound, time-bound, digest-bound, evidence-bound, correction-aware, and rollback-ready.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: tests" src="https://img.shields.io/badge/root-tests%2F-blue">
  <img alt="Domain: hydrology" src="https://img.shields.io/badge/domain-hydrology-2aa1c6">
  <img alt="Lane: identity" src="https://img.shields.io/badge/lane-identity-blue">
  <img alt="Network: disabled by default" src="https://img.shields.io/badge/network-disabled__by__default-critical">
  <img alt="Boundary: deterministic identity" src="https://img.shields.io/badge/boundary-deterministic__identity-success">
</p>

**Path:** `tests/domains/hydrology/identity/README.md`  
**Status:** draft / placeholder-expanded / PROPOSED until executable tests are verified  
**Owning root:** `tests/`  
**Domain segment:** `hydrology`  
**Test lane:** `identity`  
**Default execution posture:** deterministic, synthetic, no-network, public-safe fixtures only  
**Truth posture:** CONFIRMED target was a blank placeholder before this expansion · CONFIRMED `tests/` is the canonical root for enforceability proof · CONFIRMED Hydrology identity doctrine defines identity as `source_id + object_role + temporal_scope + normalized_digest` · CONFIRMED Hydrology owns identity for watersheds, HUC units, hydro features, reach identities, gauges, observations, groundwater, flood context, observed flood evidence, hydrographs, and upstream traces · CONFIRMED `ReachIdentity` contract requires ABSTAIN on ambiguity and marks field-level schema enforcement as NEEDS VERIFICATION · NEEDS VERIFICATION for executable test modules, fixture payload inventory, validators, schema enforcement, source registry activation, policy runtime, release integration, CI coverage, and pass rates.

---

## Purpose

`tests/domains/hydrology/identity/` is the intended home for Hydrology identity tests.

This lane should prove that Hydrology object identity is deterministic and governed by evidence, source role, source version, object family, temporal scope, normalized content, correction lineage, and rollback posture.

A passing test here should **not** mean that real hydrology sources are admitted, schemas are complete, public layers are safe, or releases are approved. It should mean only that identity guardrails behaved as expected against bounded fixtures.

---

## Placement basis

`tests/` is the canonical root for enforceability proof. Hydrology is a domain segment inside that root. `identity/` is a test lane, not a docs authority root, source registry, schema home, policy home, release home, proof store, public API surface, or public map surface.

| Responsibility | Correct home | This lane's relationship |
|---|---|---|
| Hydrology identity tests | `tests/domains/hydrology/identity/` | This directory. |
| Identity doctrine | `docs/domains/hydrology/IDENTITY_MODEL.md` | Doctrine under test; not redefined here. |
| Reach identity contract | `contracts/domains/hydrology/reach_identity.md` | Semantic contract under test for reach-specific cases. |
| Object-family docs | `docs/domains/hydrology/OBJECT_FAMILIES.md` | Object-family context for identities. |
| Machine schemas | `schemas/contracts/v1/domains/hydrology/` | Shape checks where accepted; scaffold posture must be respected. |
| Synthetic fixtures | `fixtures/domains/hydrology/identity/`, `fixtures/domains/hydrology/reach_identity/` | Preferred toy inputs and expected outcomes if populated. |
| Source registry | `data/registry/sources/hydrology/` | SourceDescriptor context; not duplicated here. |
| Policy homes | `policy/domains/hydrology/` | Referenced by tests, not bypassed here. |
| Release decisions | `release/` and `release/manifests/hydrology/` | Publication, correction, and rollback authority; tests cannot replace it. |

---

## Invariant under test

> **Hydrology identity is deterministic and evidence-bounded.** Identity is a function of source, role, temporal scope, and normalized digest. It is not a file path, serializer artifact, UI handle, release timestamp, best guess, or model-generated label.

Core checks:

| Check | Required behavior | Failure outcome |
|---|---|---|
| Source binding | `source_id` or equivalent SourceDescriptor reference is explicit where material. | validation failure / `ABSTAIN`. |
| Object role | `object_role` prevents collisions between `ReachIdentity`, `HydroFeature`, `HUCUnit`, observations, and derivatives. | validation failure. |
| Temporal scope | Source, observed, valid, retrieval, release, and correction times stay distinct where material. | validation failure. |
| Normalized digest | Identity-bearing content is canonicalized before digesting; incidental path/order/format changes do not rotate identity. | validation failure. |
| Evidence posture | Public identity claims resolve EvidenceRef/EvidenceBundle support or return a finite non-answer. | `ABSTAIN`. |
| Ambiguity posture | Ambiguous reach/HUC/source-version identity produces `ABSTAIN` or `HOLD`, never a guess. | validation failure. |
| Version discipline | NHDPlus v2.1, NHDPlus HR, 3DHP, WBD, NWIS, NFHL, and successor vintages are not silently mixed. | validation failure / `ABSTAIN`. |
| Release boundary | Test success does not become release approval, public identity authority, or rollback proof. | promotion block. |

---

## Expected scope

Tests in this lane may validate:

- stable identity from identical source, role, temporal scope, and normalized digest;
- identity rotation when evidentiary content changes;
- no identity rotation for incidental path movement, JSON key ordering, serializer formatting, or release timestamp changes;
- object-family collision prevention across `ReachIdentity`, `HydroFeature`, `HUCUnit`, `GaugeSite`, observations, and derivatives;
- reach identity ABSTAIN on ambiguity or mixed source vintage;
- NFHL regulatory context remaining distinct from observed flood evidence;
- source-role and temporal-scope preservation through release/correction/rollback fixtures.

Live source checks, real source exports, production credentials, public tile generation, and real hydrology payloads are out of scope for the default suite.

---

## Fixture posture

Use synthetic, public-safe fixtures only.

Fixture requirements:

- deterministic and no-network;
- compact enough for review in a PR;
- explicit expected outcome;
- explicit source, object role, temporal scope, digest basis, evidence posture, policy state, release relationship, correction, and rollback posture where material;
- no real source exports, lifecycle data, public tiles, credentials, restricted records, or published artifacts.

---

## Finite outcomes

| Condition | Expected outcome |
|---|---|
| Same logical content, same source/version, same object role, same temporal scope | same deterministic identity. |
| Evidentiary content changes | identity rotates or correction path records supersession. |
| Path moves, release time changes, JSON order changes | identity remains stable. |
| Source/version ambiguity cannot be resolved | `ABSTAIN` / `HOLD`. |
| Mixed NHDPlus/WBD/NWIS/NFHL vintages without explicit crosswalk support | validation failure / `ABSTAIN`. |
| Regulatory context treated as observed event evidence | validation failure / `DENY`. |
| Public identity claim lacks evidence, release, correction, or rollback posture | promotion-blocking failure. |
| Policy engine unavailable | `ERROR` or `ABSTAIN`, never public exposure. |

---

## Suggested layout

```text
tests/domains/hydrology/identity/
├── README.md
├── test_identity_rule_shape.py
├── test_digest_stability.py
├── test_content_change_rotates_identity.py
├── test_object_role_collision_prevention.py
├── test_temporal_scope_distinctness.py
├── test_reach_identity_abstain_on_ambiguity.py
├── test_version_discipline.py
└── test_release_correction_rollback.py
```

---

## Run posture

```bash
pytest tests/domains/hydrology/identity
```

Status of the command above: **PROPOSED / NEEDS VERIFICATION**. It assumes `pytest` is the accepted test runner and that executable test modules exist. This README does not claim the command currently passes.

---

## Evidence ledger

| Evidence | Status | Supports | Limits |
|---|---|---|---|
| Previous target file | CONFIRMED | `tests/domains/hydrology/identity/README.md` existed as a blank placeholder before this replacement. | Did not define the lane. |
| `tests/README.md` | CONFIRMED | `tests/` is enforceability proof and failure should block promotion where trust-spine checks fail. | Does not prove this lane's modules or pass rate. |
| `tests/domains/hydrology/README.md` | CONFIRMED | Hydrology test parent currently exists as a greenfield stub. | Parent lane still needs expansion. |
| `docs/domains/hydrology/IDENTITY_MODEL.md` | CONFIRMED doctrine / PROPOSED field realization | Defines deterministic Hydrology identity rule and object-family identity posture. | Concrete field names, validators, fixtures, CI, and pass rates remain NEEDS VERIFICATION. |
| `contracts/domains/hydrology/reach_identity.md` | CONFIRMED semantic contract / PROPOSED schema enforcement | Defines `ReachIdentity`, version discipline, ABSTAIN-on-ambiguity posture, evidence, policy, release, correction, and rollback expectations. | Paired schema remains a permissive scaffold; runtime behavior remains NEEDS VERIFICATION. |

---

## Validation checklist

- [ ] Executable test modules exist under this lane.
- [ ] Test runner and import paths match the repo's accepted convention.
- [ ] Synthetic identity fixtures exist for stable identity, digest stability, content-change rotation, role collision, temporal-scope separation, mixed-vintage failure, ambiguous reach identity, and regulatory/observed flood anti-collapse cases.
- [ ] Active identity schemas and field expectations are accepted beyond scaffold status where tests enforce them.
- [ ] SourceDescriptor behavior is available to tests or safely stubbed.
- [ ] EvidenceRef / EvidenceBundle behavior is available to tests or safely stubbed.
- [ ] PolicyDecision, ReleaseManifest, CorrectionNotice, RedactionReceipt, and RollbackCard expectations are defined before enforcing them.
- [ ] CI runs the no-network Hydrology identity suite or marks it as an expected gap.
- [ ] Failures block public carrier promotion or release candidate approval where material.

---

## Rollback

Rollback is required if this lane becomes a live source-fetcher, lifecycle data store, source registry, contract root, schema authority, policy authority, proof store, release-decision root, public map/API/tile surface, AI surface, renderer implementation, pipeline implementation, or publication shortcut.

Rollback target for this replacement: previous blank blob SHA `8b137891791fe96927ad78e64b0aad7bded08bdc`.

<p align="right"><a href="#top">Back to top</a></p>
