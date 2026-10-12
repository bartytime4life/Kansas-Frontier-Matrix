<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-domains-hydrology-identity-readme
title: Hydrology Identity Test README
type: test-readme
version: v0.2
status: draft; documentation-only identity-test lane; REMAIN_PROPOSED profile; no executable common-profile coverage
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
updated: 2026-07-31
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
  - "Decision #1886 keeps the four-slot tuple REMAIN_PROPOSED; this README specifies graduation coverage only and does not claim an accepted profile, fixtures, constructor/checker, tests, or CI."
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
**Status:** draft / documentation-only / identity `REMAIN_PROPOSED` / no executable common-profile tests
**Owning root:** `tests/`  
**Domain segment:** `hydrology`  
**Test lane:** `identity`  
**Default execution posture:** deterministic, synthetic, no-network, public-safe fixtures only  
**Truth posture:** CONFIRMED this directory contains documentation only · CONFIRMED decision #1886 records `REMAIN_PROPOSED` · CONFIRMED the paired schema requires only `id`, permits arbitrary properties, and has no dedicated fixture/validator/test lane · PROPOSED tuple is `source_id + object_role + temporal_scope + normalized_digest` · NEEDS VERIFICATION for accepted profiles, executable modules, fixtures, constructor/checker, SourceDescriptor parity, SpecHash behavior, migration, consumers, CI, and pass rates.

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
| Identity decision documentation | `docs/domains/hydrology/IDENTITY_MODEL.md` | `REMAIN_PROPOSED` candidate and graduation boundary; not redefined here. |
| Reach identity contract | `contracts/domains/hydrology/reach_identity.md` | Semantic contract under test for reach-specific cases. |
| Object-family docs | `docs/domains/hydrology/OBJECT_FAMILIES.md` | Object-family context for identities. |
| Machine schemas | `schemas/contracts/v1/domains/hydrology/` | Shape checks where accepted; scaffold posture must be respected. |
| Synthetic fixtures | `fixtures/domains/hydrology/identity/`, `fixtures/domains/hydrology/reach_identity/` | Preferred toy inputs and expected outcomes if populated. |
| Source registry | `data/registry/sources/hydrology/` | SourceDescriptor context; not duplicated here. |
| Policy homes | `policy/domains/hydrology/` | Referenced by tests, not bypassed here. |
| Release decisions | `release/` and `release/manifests/hydrology/` | Publication, correction, and rollback authority; tests cannot replace it. |

---

## Invariant under test

> **Graduation target, not current behavior.** If accepted, Hydrology identity is
> a function of `identity_profile`, source, object role, family-specific time,
> and `spec_hash` as the persisted realization of `normalized_digest`. It is not
> a file path, serializer artifact, UI handle, release timestamp, best guess,
> or model-generated label.

Core checks:

| Check | Required behavior | Failure outcome |
|---|---|---|
| Source binding | `source_id` resolves an immutable/versioned SourceDescriptor; required mirrored `source_role` matches exactly. | `FAIL` / `FAIL_SOURCE_ROLE_MISMATCH`; runtime `ABSTAIN`. |
| Object role | `object_role` prevents collisions between `ReachIdentity`, `HydroFeature`, `HUCUnit`, observations, and derivatives. | validation failure. |
| Temporal scope | Source, observed, valid, retrieval, release, and correction times stay distinct where material. | validation failure. |
| Profile binding | `schema_version`, `identity_profile`, and `family_profile` remain separate; legacy `version` never implies a modern profile. | `FAIL_PROFILE_MISMATCH` / `legacy-profile-unknown`. |
| Normalized digest | The accepted family projection is canonicalized under the accepted common profile; `spec_hash` is the persisted realization of `normalized_digest`. | validation failure. |
| Evidence posture | Public identity claims resolve EvidenceRef/EvidenceBundle support or return a finite non-answer. | `ABSTAIN`. |
| Ambiguity posture | Ambiguous reach/HUC/source-version identity produces `ABSTAIN` or `HOLD`, never a guess. | validation failure. |
| Version discipline | NHDPlus v2.1, NHDPlus HR, 3DHP, WBD, NWIS, NFHL, and successor vintages are not silently mixed. | validation failure / `ABSTAIN`. |
| Release boundary | Test success does not become release approval, public identity authority, or rollback proof. | promotion block. |

---

## Expected scope

Tests in this lane may validate:

- stable identity from identical profile versions, source/version, mirrored role, object role, temporal scope, and family projection;
- identity rotation when source/version, role, object role, identity-bearing time, profile version, or declared family content changes;
- no identity rotation for incidental path movement, JSON key ordering, serializer formatting, or release timestamp changes;
- object-family collision prevention across `ReachIdentity`, `HydroFeature`, `HUCUnit`, `GaugeSite`, observations, and derivatives;
- reach identity ABSTAIN on ambiguity or mixed source vintage;
- NFHL regulatory context remaining distinct from observed flood evidence;
- exact SourceDescriptor/mirror parity, profile mismatch, legacy-profile,
  immutable correction/supersession, migration, consumer, and rollback cases.

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
| Same accepted profiles, logical projection, source/version, role, object role, and temporal scope | same deterministic identity. |
| Identity-bearing source, role, time, profile, or family content changes | identity rotates and correction path records supersession. |
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
├── test_source_role_descriptor_parity.py
├── test_profile_mismatch_and_legacy_unknown.py
├── test_canonical_equivalence_and_transient_stability.py
├── test_reach_identity_abstain_on_ambiguity.py
├── test_version_discipline.py
├── test_correction_supersession_and_link_independence.py
└── test_migration_compatibility_and_rollback.py
```

---

## Run posture

```bash
pytest tests/domains/hydrology/identity
```

Status of the command above: **DOCUMENTATION-ONLY / EXPECTED NO TESTS**. No
executable module in this directory currently proves the common profile. Do not
interpret pytest collection or another Hydrology test pass as identity coverage.

---

## Evidence ledger

| Evidence | Status | Supports | Limits |
|---|---|---|---|
| Previous target file | CONFIRMED | `tests/domains/hydrology/identity/README.md` existed as a blank placeholder before this replacement. | Did not define the lane. |
| `tests/README.md` | CONFIRMED | `tests/` is enforceability proof and failure should block promotion where trust-spine checks fail. | Does not prove this lane's modules or pass rate. |
| `tests/domains/hydrology/README.md` | CONFIRMED | Hydrology test parent currently exists as a greenfield stub. | Parent lane still needs expansion. |
| `docs/domains/hydrology/IDENTITY_MODEL.md` | CONFIRMED decision documentation / `REMAIN_PROPOSED` semantics | Defines the sole candidate, family/profile boundary, immutability, migration, and graduation gates. | No accepted or executable identity behavior. |
| `contracts/domains/hydrology/reach_identity.md` | CONFIRMED semantic contract / PROPOSED schema enforcement | Defines `ReachIdentity`, version discipline, ABSTAIN-on-ambiguity posture, evidence, policy, release, correction, and rollback expectations. | Paired schema remains a permissive scaffold; runtime behavior remains NEEDS VERIFICATION. |

---

## Validation checklist

- [ ] Executable test modules exist under this lane.
- [ ] Test runner and import paths match the repo's accepted convention.
- [ ] Synthetic identity fixtures exist for stable identity, digest stability, content-change rotation, role collision, temporal-scope separation, mixed-vintage failure, ambiguous reach identity, and regulatory/observed flood anti-collapse cases.
- [ ] Active identity schemas and field expectations are accepted beyond scaffold status where tests enforce them.
- [ ] SourceDescriptor behavior is available to tests or safely stubbed.
- [ ] Tests cover exact role parity, missing descriptor/role, profile mismatch,
      legacy-profile-unknown, canonical equivalence, meaningful rotation,
      transient stability, immutable correction lineage, dual-read/single-write
      migration, consumer mapping, and rollback reference resolution.
- [ ] EvidenceRef / EvidenceBundle behavior is available to tests or safely stubbed.
- [ ] PolicyDecision, ReleaseManifest, CorrectionNotice, RedactionReceipt, and RollbackCard expectations are defined before enforcing them.
- [ ] CI runs the no-network Hydrology identity suite or marks it as an expected gap.
- [ ] Failures block public carrier promotion or release candidate approval where material.

---

## Rollback

Rollback is required if this lane becomes a live source-fetcher, lifecycle data store, source registry, contract root, schema authority, policy authority, proof store, release-decision root, public map/API/tile surface, AI surface, renderer implementation, pipeline implementation, or publication shortcut.

Rollback target for this replacement: previous blank blob SHA `8b137891791fe96927ad78e64b0aad7bded08bdc`.

<p align="right"><a href="#top">Back to top</a></p>
