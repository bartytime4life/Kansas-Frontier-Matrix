<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-domains-habitat-identity-readme
title: Habitat Identity Test README
type: test-readme
version: v0.1
status: draft; placeholder-expanded; test-lane; PROPOSED / NEEDS VERIFICATION before promotion
owners:
  - OWNER_TBD — Habitat domain steward
  - OWNER_TBD — Identity steward
  - OWNER_TBD — Source steward
  - OWNER_TBD — Evidence steward
  - OWNER_TBD — Schema steward
  - OWNER_TBD — Policy steward
  - OWNER_TBD — Validation steward
  - OWNER_TBD — Release steward
  - OWNER_TBD — QA steward
created: NEEDS VERIFICATION — blank placeholder existed before v0.1 expansion
updated: 2026-07-05
policy_label: public-doc; tests; habitat; identity; deterministic-identity; no-network; source-role-aware; temporal-scope-aware; evidence-bound; release-gated; anti-collapse
tags: [kfm, tests, habitat, identity, deterministic-identity, DomainFeatureIdentity, spec_hash, source-role, object-role, temporal-scope, EvidenceRef, EvidenceBundle, PolicyDecision, ReleaseManifest, CorrectionNotice, RollbackCard, ABSTAIN, DENY]
related:
  - ../../../README.md
  - ../../../../docs/domains/habitat/IDENTITY_MODEL.md
  - ../../../../contracts/domains/habitat/domain_feature_identity.md
  - ../../../../docs/domains/habitat/README.md
  - ../../../../docs/domains/habitat/HABITAT_DOMAIN_MODEL.md
  - ../../../../docs/domains/habitat/MODEL_VS_OBSERVATION.md
  - ../../../../docs/domains/habitat/SOURCE_FAMILIES.md
  - ../../../../fixtures/domains/habitat/README.md
  - ../../../../fixtures/domains/habitat/domain_feature_identity/
  - ../../../../contracts/domains/habitat/
  - ../../../../schemas/contracts/v1/domains/habitat/domain_feature_identity.schema.json
  - ../../../../schemas/contracts/v1/domains/habitat/
  - ../../../../policy/domains/habitat/
  - ../../../../policy/sensitivity/habitat/
  - ../../../../data/registry/sources/habitat/
  - ../../../../data/proofs/habitat/
  - ../../../../data/receipts/
  - ../../../../release/
notes:
  - "This file replaces a blank placeholder at tests/domains/habitat/identity/README.md."
  - "This is a test-lane README only. It does not define Habitat identity doctrine, semantic contracts, schemas, source descriptors, policy rules, fixtures, evidence bundles, receipts, proofs, release decisions, production code, or published artifacts."
  - "The tested invariant is deterministic Habitat identity: source id + source role + object role/family + temporal scope + normalized digest/spec_hash must remain stable, evidence-bound, correction-aware, rollback-aware, and separate from truth, policy, review, release, map, tile, and AI surfaces."
  - "The default posture is deterministic and no-network. Live source checks, credentials, real sensitive occurrence records, and live model/provider calls do not belong in this lane."
  - "Rollback target for this replacement is previous blank blob SHA 8b137891791fe96927ad78e64b0aad7bded08bdc."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Habitat identity tests

> Deterministic, no-network test documentation for proving that Habitat object identity stays reproducible, source-role-aware, temporal-scope-aware, evidence-bound, sensitivity-aware, correction-aware, and release-gated.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: tests" src="https://img.shields.io/badge/root-tests%2F-blue">
  <img alt="Domain: habitat" src="https://img.shields.io/badge/domain-habitat-2e7d32">
  <img alt="Lane: identity" src="https://img.shields.io/badge/lane-identity-6f42c1">
  <img alt="Network: disabled by default" src="https://img.shields.io/badge/network-disabled__by__default-critical">
  <img alt="Boundary: identity not truth" src="https://img.shields.io/badge/boundary-identity__not__truth-success">
</p>

**Path:** `tests/domains/habitat/identity/README.md`  
**Status:** draft / placeholder-expanded / PROPOSED until paired test files are verified  
**Owning root:** `tests/`  
**Domain segment:** `habitat`  
**Test lane:** `identity`  
**Default execution posture:** deterministic, synthetic, no-network, public-safe fixtures only  
**Truth posture:** CONFIRMED target was a blank placeholder before this expansion · CONFIRMED `tests/` is the canonical root for enforceability proof · CONFIRMED Habitat identity doctrine uses `source id + object role + temporal scope + normalized digest` as the identity basis · CONFIRMED the Habitat `DomainFeatureIdentity` contract exists and states that identity is not proof, policy, review, release, public layer, tile, popup, or AI answer · NEEDS VERIFICATION for executable test modules, fixture payloads, schema enforcement, validators, imports, CI coverage, receipt emission, and release-gate integration.

**Quick jumps:** [Purpose](#purpose) · [Placement basis](#placement-basis) · [Invariant under test](#invariant-under-test) · [Expected test scope](#expected-test-scope) · [Fixture posture](#fixture-posture) · [Assertions](#assertions) · [Finite outcomes](#finite-outcomes) · [Forbidden shortcuts](#forbidden-shortcuts) · [Suggested test layout](#suggested-test-layout) · [Run posture](#run-posture) · [Evidence ledger](#evidence-ledger) · [Validation checklist](#validation-checklist) · [Rollback](#rollback)

---

## Purpose

`tests/domains/habitat/identity/` is the intended home for tests that prove Habitat identity remains deterministic and bounded across sources, versions, object families, evidence bundles, release candidates, corrections, and rollback targets.

This lane should test that identity-bearing Habitat objects cannot silently change meaning when they move through:

- source admission;
- validation;
- evidence resolution;
- policy checks;
- catalog/proof closure;
- release-candidate shaping;
- governed API/UI payloads;
- Evidence Drawer and Focus Mode carriers;
- correction and rollback flows.

A passing test here should **not** mean that a Habitat claim is true, policy-admitted, released, scientifically complete, or safe for public display. It should mean only that identity construction and identity-boundary guardrails behaved as expected against bounded fixtures.

---

## Placement basis

`tests/` is the canonical root for enforceability proof. Habitat appears as a lane segment inside the tests root, not as a repo-root domain folder.

| Responsibility | Correct home | This lane's relationship |
|---|---|---|
| Habitat identity tests | `tests/domains/habitat/identity/` | This directory. |
| Synthetic identity fixtures | `fixtures/domains/habitat/domain_feature_identity/` if present, otherwise `fixtures/domains/habitat/` | Preferred toy inputs and expected outcomes. |
| Identity doctrine | `docs/domains/habitat/IDENTITY_MODEL.md` | Referenced doctrine; not test implementation. |
| Semantic identity contract | `contracts/domains/habitat/domain_feature_identity.md` | Defines meaning; tests do not redefine it. |
| Machine schema | `schemas/contracts/v1/domains/habitat/domain_feature_identity.schema.json` or accepted ADR alternative | Referenced by tests, not duplicated here. |
| Source registry | `data/registry/sources/habitat/` | Source identity, source role, rights, cadence, caveats, and activation state. |
| Policy and sensitivity | `policy/domains/habitat/`, `policy/sensitivity/habitat/` | Referenced by tests, not bypassed here. |
| Receipts and proofs | `data/receipts/`, `data/proofs/habitat/` | Expected references; tests do not own trust objects. |
| Release decisions | `release/` | Publication, correction, and rollback authority; tests cannot replace it. |

---

## Invariant under test

> **Identity is deterministic support, not truth.** Habitat identity must preserve source identity, source role, object role, temporal scope, normalized digest, evidence linkage, correction lineage, and rollback target. It must not become evidence, policy, review approval, release authority, public map truth, or AI truth.

For this test lane, the invariant decomposes into nine checks:

| Check | Required behavior | Failure outcome |
|---|---|---|
| Deterministic digest | Same canonical identity-bearing content yields the same `spec_hash`; changed identity-bearing content yields a changed digest. | validation failure. |
| Source identity | `source_id` or SourceDescriptor reference is explicit and stable. | `ABSTAIN` / validation failure. |
| Source role | Observed, modeled, regulatory, aggregate, administrative, candidate, synthetic, derivative, or context posture is preserved. | `DENY` / validation failure. |
| Object role/family | HabitatPatch, LandCoverObservation, EcologicalSystem, SuitabilityModel, ConnectivityEdge, Corridor, RestorationOpportunity, StewardshipZone, or other reviewed family stays distinct. | validation failure / `ABSTAIN`. |
| Temporal scope | Source, observed, valid, retrieval, release, and correction time are distinct where material. | validation failure. |
| Evidence linkage | Identity-bearing consequential claims resolve `EvidenceRef -> EvidenceBundle` or produce a finite non-answer. | `ABSTAIN`. |
| Sensitivity and geoprivacy | Identity does not expose sensitive occurrence, rare-species, rare-plant, owner/land, or exact-location detail by ID, hash, key, or metadata. | `DENY` / `RESTRICT`. |
| Correction lineage | Renames, merges, splits, supersessions, and hash migrations preserve correction trail and rollback target. | promotion-blocking failure. |
| No authority upgrade | Identity never substitutes for policy, review, release, proof, public layer, tile, graph edge, or AI answer. | test failure. |

---

## Expected test scope

Tests in this lane should be small, synthetic, and deterministic. They may validate:

- canonicalization and stable `spec_hash` behavior against toy payloads;
- failure when identity changes because source role, object role, temporal scope, or digest inputs change;
- failure when identity ignores source role or temporal scope;
- failure when modeled, observed, regulatory, aggregate, candidate, synthetic, derivative, or context identities collapse;
- failure when a HabitatPatch, SuitabilityModel, Corridor, ConnectivityEdge, EcologicalSystem, LandCoverObservation, or StewardshipZone identity is reused across incompatible object families;
- failure when identity-bearing payloads omit evidence, source, policy, or release context required for consequential public use;
- correction and rollback behavior for rename, merge, split, supersession, schema-version migration, or digest-algorithm migration examples;
- denial or restriction when an identity key leaks sensitive coordinates, occurrence IDs, owner/land links, or protected-resource detail.

Live source systems, real sensitive occurrence records, real rare-species/rare-plant locations, real owner/land identifiers, and live model/provider calls are out of scope for the default suite.

---

## Fixture posture

Use `fixtures/domains/habitat/domain_feature_identity/` when present. If that lane is absent, use clearly labeled synthetic fixtures under the accepted Habitat fixture root.

Fixture requirements:

- synthetic and public-safe;
- deterministic and no-network;
- compact enough for review in a PR;
- explicit expected outcome;
- explicit source ID, source role, object family, object role, temporal scope, schema version, and digest basis where material;
- explicit evidence, policy, review, release, correction, and rollback state where public or consequential use is tested;
- no real sensitive occurrence IDs, rare-species coordinates, rare-plant locations, owner/parcel identifiers, exact protected habitat locations, or source exports;
- no credentials, live network calls, generated release artifacts, public tiles, or live model/provider calls.

Preferred fixture families:

| Fixture kind | Preferred lane | Example expected outcome |
|---|---|---|
| Stable identity pair | `fixtures/domains/habitat/domain_feature_identity/` | identical canonical content -> same `spec_hash`. |
| Changed source role | same | changed identity / validation failure if collapsed. |
| Changed temporal scope | same | changed identity / no silent reuse. |
| Object-family collision | same or `fixtures/domains/habitat/invalid/` | validation failure / `DENY`. |
| Missing evidence for consequential claim | same or invalid lane | `ABSTAIN`. |
| Sensitive ID leakage | same or invalid lane | `DENY` / `RESTRICT`. |
| Correction lineage | same or golden lane | correction/supersession/rollback chain preserved. |
| Candidate public exposure | same or invalid lane | `DENY`. |

---

## Assertions

A useful Habitat identity test should make the identity basis and boundary failure obvious.

### Positive path

- canonical content is normalized before hashing;
- identity-bearing fields are explicit;
- source role, object role, and temporal scope are included in the identity basis;
- the same canonical identity yields the same digest across runs;
- correction lineage and rollback references survive identity changes;
- evidence, policy, review, release, and sensitivity context remain separate but linkable;
- public-facing carriers reference released identity/evidence rather than becoming identity authority.

### Negative path

- missing source ID, source role, object role, temporal scope, or digest basis fails closed;
- changing source role or object role cannot preserve the same identity unless a governed correction/migration says so;
- changing temporal scope cannot silently reuse the same identity;
- identity cannot collapse observed/model/regulatory/aggregate/candidate/synthetic/context records;
- identity cannot transform a model into an observation, a land-cover observation into a species occurrence, a corridor into observed animal movement, or a tile into truth;
- identity cannot expose sensitive coordinates, occurrence detail, owner/land links, or protected-resource detail;
- AI summaries cannot generate, repair, or upgrade identity authority.

---

## Finite outcomes

This lane should prefer explicit finite outcomes over loose pass/fail text.

| Condition | Expected outcome |
|---|---|
| Valid synthetic identity with source role, object role, temporal scope, digest, evidence, policy, review, and release context | accepted support object / downstream carrier allowed only if separately release-admitted. |
| Missing source ID, role, temporal scope, or digest basis | validation failure / `ERROR`. |
| Evidence missing for consequential claim | `ABSTAIN`. |
| Source-role or object-family collapse detected | validation failure / `DENY`. |
| Sensitive identity leakage detected | `DENY` / `RESTRICT`. |
| Candidate identity requested for public exposure | `DENY`. |
| Correction lineage missing after rename/merge/split/supersession | promotion-blocking failure. |
| Policy engine unavailable | `ERROR` or `ABSTAIN`, never public exposure. |

---

## Forbidden shortcuts

Do not use this test lane to:

- fetch live upstream source systems;
- store credentials or tokens;
- store real source exports;
- store real sensitive occurrence records, rare-species/rare-plant locations, protected habitat locations, owner/parcel records, or exact sensitive geometry;
- redefine Habitat identity doctrine, semantic contracts, schemas, source descriptors, policy rules, fixtures, receipts, proofs, release decisions, or production code;
- treat `spec_hash`, `id`, or `DomainFeatureIdentity` as evidence, policy, review, release, or public truth;
- infer release state from file existence, layer name, map rendering, graph edge, or AI wording;
- bypass evidence, policy, sensitivity, correction, or rollback checks with a fixture flag;
- publish, promote, or release anything.

Any test that needs real source IDs, real source payloads, or real public tiles belongs in a gated integration tier with source admission, lifecycle state, policy, receipts, release controls, and rollback targets.

---

## Suggested test layout

The exact Python module names remain NEEDS VERIFICATION until the runner and existing test conventions are inspected. A minimal future layout could be:

```text
tests/domains/habitat/identity/
├── README.md
├── test_spec_hash_determinism.py          # canonical content -> stable digest
├── test_identity_basis_required.py        # source role/object role/temporal scope required
├── test_source_role_anti_collapse.py      # observed/model/regulatory/candidate/synthetic separation
├── test_sensitive_identity_leakage.py     # IDs/hashes/metadata cannot leak protected detail
└── test_correction_lineage.py             # rename/merge/split/supersession/rollback references
```

Keep helpers local only when they are test-specific. Shared identity contracts, schemas, source registries, policy behavior, evidence resolvers, fixtures, release behavior, or package logic belong under their accepted responsibility roots.

---

## Run posture

Default run expectations:

```bash
pytest tests/domains/habitat/identity
```

Status of the command above: **PROPOSED / NEEDS VERIFICATION**. It assumes `pytest` is the accepted test runner and that executable test modules exist. This README does not claim the command currently passes.

Expected CI posture:

- default suite: no-network, synthetic fixtures only;
- fail closed on missing identity basis, source-role collapse, object-family collapse, missing evidence, missing policy, sensitive identity leakage, missing correction lineage, or unreleased public carrier;
- live-source or provider checks: separate gated jobs only;
- release gate: Habitat identity failures should block public catalog/API/map/tile/AI carrier promotion.

---

## Evidence ledger

| Evidence | Status | Supports | Limits |
|---|---|---|---|
| Previous target file | CONFIRMED | `tests/domains/habitat/identity/README.md` existed as a blank placeholder before this replacement. | Did not define the lane. |
| `tests/README.md` | CONFIRMED | `tests/` is enforceability proof; domain-specific tests belong under `tests/domains/<domain>/`; default tests should avoid sensitive data and live network calls. | Does not prove habitat/identity modules or pass rate. |
| `docs/domains/habitat/IDENTITY_MODEL.md` | CONFIRMED doctrine / PROPOSED implementation | Habitat identity basis is source id + object role + temporal scope + normalized digest, with `spec_hash`, EvidenceRef/EvidenceBundle linkage, temporal separation, and sensitivity fail-closed posture. | Notes schema homes and implementation details are PROPOSED / CONFLICTED / NEEDS VERIFICATION. |
| `contracts/domains/habitat/domain_feature_identity.md` | CONFIRMED semantic contract / PROPOSED implementation | `DomainFeatureIdentity` records deterministic identity, source role, object role, temporal scope, digest basis, evidence linkage, correction lineage, and anti-collapse posture; identity is not truth or release. | The paired schema is a scaffold and field-level enforcement remains NEEDS VERIFICATION. |
| Habitat docs, source, fixture, policy, proof, and release roots | PARTIALLY CONFIRMED by repo search and fetched docs | Adjacent responsibility homes exist or are referenced for doctrine, contracts, source registry, fixtures, schemas, policy, proofs, and release. | Contents and enforcement remain NEEDS VERIFICATION unless inspected. |

---

## Validation checklist

Before treating this README as implemented behavior, verify:

- [ ] Executable test modules exist under this lane.
- [ ] Test runner and import paths match the repo's accepted convention.
- [ ] Synthetic fixtures exist for stable digest, changed source role, changed object role, changed temporal scope, missing evidence, sensitive leakage, candidate public exposure, and correction lineage.
- [ ] DomainFeatureIdentity schema path and field expectations are accepted.
- [ ] SourceDescriptor/source-role behavior is available to tests or safely stubbed.
- [ ] EvidenceRef / EvidenceBundle resolver behavior is available to tests or safely stubbed.
- [ ] PolicyDecision and sensitivity behavior are available to tests or safely stubbed.
- [ ] CorrectionNotice, RollbackCard, ReleaseManifest, and migration expectations are defined before enforcing them.
- [ ] CI runs the no-network Habitat identity suite.
- [ ] Failures block public carrier promotion or release candidate approval.

---

## Rollback

Rollback is required if this lane becomes a source registry, fixture root, lifecycle data store, semantic-contract root, schema authority, policy authority, proof store, receipt store, release-decision root, public map/API/tile surface, AI surface, or publication shortcut.

Rollback target for this replacement: previous blank blob SHA `8b137891791fe96927ad78e64b0aad7bded08bdc`.

<p align="right"><a href="#top">Back to top</a></p>
