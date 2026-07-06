<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-domains-settlements-infrastructure-identity-readme
title: Settlements Infrastructure Identity Tests README
type: test-lane-readme
version: v0.1
status: draft; empty-placeholder-replaced; identity-test-lane; PROPOSED / NEEDS VERIFICATION before promotion
owners:
  - OWNER_TBD - Settlements/Infrastructure domain steward
  - OWNER_TBD - Identity steward
  - OWNER_TBD - QA steward
  - OWNER_TBD - Contracts steward
  - OWNER_TBD - Evidence steward
  - OWNER_TBD - Policy steward
  - OWNER_TBD - Release steward
created: 2026-07-06
updated: 2026-07-06
policy_label: public-doc; tests; settlements-infrastructure; identity; deterministic-id; source-role-aware; temporal-scope-aware; evidence-bound; policy-gated; release-gated; rollback-aware; no-network
tags: [kfm, tests, settlements-infrastructure, identity, deterministic-identity, spec_hash, jcs-sha256, source-role, temporal-scope, Settlement, Municipality, CensusPlace, Townsite, GhostTown, Fort, Mission, ReservationCommunity, InfrastructureAsset, Facility, Operator, EvidenceBundle, EvidenceRef, PolicyDecision, ReviewRecord, ReleaseManifest, RollbackCard, ABSTAIN, DENY, ERROR]
related:
  - ../README.md
  - ../../README.md
  - ../../../README.md
  - ../../../../docs/domains/settlements-infrastructure/IDENTITY_MODEL.md
  - ../../../../docs/domains/settlements-infrastructure/README.md
  - ../../../../docs/domains/settlements-infrastructure/CANONICAL_PATHS.md
  - ../../../../docs/domains/settlements-infrastructure/DATA_LIFECYCLE.md
  - ../../../../docs/domains/settlements-infrastructure/sublanes/settlements.md
  - ../../../../contracts/domains/settlements-infrastructure/domain_feature_identity.md
  - ../../../../contracts/domains/settlements-infrastructure/place-identity.md
  - ../../../../contracts/domains/settlement/README.md
  - ../../../../schemas/contracts/v1/domains/settlements-infrastructure/
  - ../../../../schemas/contracts/v1/domains/settlement/README.md
  - ../../../../fixtures/domains/settlements-infrastructure/identity/
  - ../../../../policy/domains/settlements-infrastructure/
  - ../../../../release/candidates/settlements-infrastructure/
notes:
  - "This README replaces the empty placeholder content at tests/domains/settlements-infrastructure/identity/README.md."
  - "Directory Rules place enforceability proof under tests/. This directory is an identity-focused test lane; it is not the identity doctrine home, contract home, schema home, evidence store, policy home, or release authority."
  - "The parent tests/domains/settlements-infrastructure/README.md was observed as a greenfield stub during authoring. This child lane is self-contained until the parent domain test index is expanded."
  - "Canonical-path docs identify settlements-infrastructure as the working domain slug and record settlement as a path variance requiring ADR-class resolution. This README uses the canonical hyphenated domain segment."
  - "Executable tests, fixture shapes, schema bindings, CI jobs, validators, release integration, and pass rates remain NEEDS VERIFICATION."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Settlements Infrastructure identity tests

> Deterministic, no-network test documentation for proving that Settlements/Infrastructure identifiers remain source-role-aware, object-role-aware, temporal-scope-aware, evidence-bound, policy-gated, release-gated, and rollback-aware.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: tests" src="https://img.shields.io/badge/root-tests%2F-blue">
  <img alt="Domain: settlements infrastructure" src="https://img.shields.io/badge/domain-settlements--infrastructure-blue">
  <img alt="Lane: identity tests" src="https://img.shields.io/badge/lane-identity__tests-purple">
  <img alt="Network: disabled by default" src="https://img.shields.io/badge/network-disabled__by__default-critical">
  <img alt="Boundary: tests not identity authority" src="https://img.shields.io/badge/boundary-tests__not__identity__authority-success">
</p>

**Path:** `tests/domains/settlements-infrastructure/identity/README.md`  
**Status:** draft / empty placeholder replaced / identity test lane / PROPOSED until executable tests are verified  
**Owning root:** `tests/`  
**Domain segment:** `settlements-infrastructure`  
**Test lane:** `identity`  
**Default execution posture:** deterministic, synthetic, no-network, public-safe fixtures only  
**Truth posture:** CONFIRMED target file existed as an empty placeholder before replacement; CONFIRMED parent `tests/domains/settlements-infrastructure/README.md` exists as a greenfield stub; CONFIRMED domain identity docs define deterministic identity as `source_id + object_role + temporal_scope + normalized_digest`; CONFIRMED canonical-path docs treat `settlements-infrastructure` as the working domain segment and singular `settlement` as conflicted variance; NEEDS VERIFICATION for executable tests, accepted fixtures, schemas, validators, CI coverage, and pass rates.

---

## Purpose

`tests/domains/settlements-infrastructure/identity/` is the identity-focused test lane for the Settlements/Infrastructure domain.

This lane should prove that settlement, place, community, and infrastructure identifiers are stable, reproducible, source-scoped, object-role-scoped, time-scoped, and evidence-bound. It should also prove that identity tests do not become the authority for meaning, schema shape, public release, policy approval, or source truth.

A passing test here should not mean that a settlement boundary is legally current, a municipality is incorporated, a census place is official, a townsite location is precise, a fort or mission claim is public, a reservation-community claim is culturally cleared, an infrastructure asset is safe to expose, or a release is approved. It should mean only that the scoped identity guardrail behaved as expected against bounded synthetic fixtures and local files.

[Back to top](#top)

---

## Placement Basis

Directory Rules classify `tests/` as the root that proves rules are enforceable. This directory is therefore an identity-test lane under the canonical domain segment `settlements-infrastructure`.

| Responsibility | Correct home | This lane's relationship |
|---|---|---|
| Identity tests | `tests/domains/settlements-infrastructure/identity/` | This directory. |
| Domain test parent | `tests/domains/settlements-infrastructure/README.md` | Confirmed greenfield stub. |
| Identity doctrine | `docs/domains/settlements-infrastructure/IDENTITY_MODEL.md` | Defines identity rules; not owned here. |
| Canonical path posture | `docs/domains/settlements-infrastructure/CANONICAL_PATHS.md` | Defines slug variance and working canonical segment. |
| Semantic contracts | `contracts/domains/settlements-infrastructure/` or ADR-selected alternate | Defines object meaning; not owned here. |
| Machine schemas | `schemas/contracts/v1/domains/settlements-infrastructure/` or ADR-selected alternate | Defines accepted shape; not owned here. |
| Compatibility variant | `settlement/` paths | CONFLICTED compatibility surfaces; not canonicalized by this README. |
| Evidence, proofs, receipts | `data/proofs/`, `data/receipts/`, and accepted roots | Not owned here. |
| Policy authority | `policy/domains/settlements-infrastructure/` or ADR-selected alternate | Not owned here. |
| Release decisions | `release/` roots | Not owned here. |

> [!IMPORTANT]
> This README documents a test lane. It cannot authorize path migration, decide the `settlement` versus `settlements-infrastructure` slug conflict, define schema shape, approve release, or make sensitive infrastructure/place details public.

---

## Invariant Under Test

> **Identity is a deterministic evidence carrier, not a truth upgrade.** Settlements/Infrastructure identity is composed from source, object role, temporal scope, and normalized content digest. Tests must preserve those boundaries and fail closed when identity inputs collapse.

Core checks:

| Check | Required behavior | Failure outcome |
|---|---|---|
| Deterministic composition | Identity includes `source_id`, `object_role`, `temporal_scope`, and `normalized_digest`. | validation failure. |
| Digest boundary | Normalized digest is reproducible from canonical identity-bearing payload; hash is not treated as secrecy. | validation failure / `ERROR`. |
| Object-role boundary | Settlement, Municipality, CensusPlace, Townsite, GhostTown, Fort, Mission, ReservationCommunity, InfrastructureAsset, Facility, Operator, and related families do not silently merge. | validation failure. |
| Source-role boundary | Source role is set at admission and cannot be edited in place or upcast by normalization, map display, AI wording, graph projection, or release assembly. | `DENY` / `ABSTAIN`. |
| Temporal boundary | Source, observed, valid, retrieval, release, and correction times remain distinct where material. | validation failure / `ABSTAIN`. |
| Correction boundary | Corrections issue new reviewed state and references; tests do not silently rewrite identity history. | promotion block. |
| Infrastructure boundary | Place/community identity does not become asset, dependency, facility, utility, operator, condition, or security-sensitive truth. | `DENY` / `ABSTAIN`. |
| Cultural and sovereignty boundary | ReservationCommunity, mission, fort, townsite, sacred, burial-adjacent, and archaeology-adjacent joins fail closed without policy and review support. | `DENY` / `ABSTAIN`. |
| Evidence boundary | Consequential identity claims require EvidenceRef-to-EvidenceBundle support or fail closed. | `ABSTAIN`. |
| Release boundary | Identity-test success does not become public release approval. | promotion block. |
| No-network boundary | Default tests do not call live source feeds, census APIs, geocoders, cadastral systems, utility systems, map services, public APIs, or AI runtimes. | validation failure / `ERROR`. |

---

## Expected Test Families

| Family | Purpose | Boundary |
|---|---|---|
| Deterministic hash tests | Prove the same normalized identity payload produces the same digest and changed identity-bearing fields produce a new digest. | Hash proves reproducibility, not truth. |
| Object-role separation tests | Prove same-name Settlement, Municipality, CensusPlace, Townsite, and GhostTown carriers do not collapse. | Name match is not identity merge. |
| Temporal-scope tests | Prove valid, observed, retrieval, release, and correction times are not substituted for one another. | Time is load-bearing. |
| Source-role tests | Prove candidate/context/administrative/model/aggregate sources cannot be upcast into authority. | Source role stays fixed. |
| Cross-lane boundary tests | Prove settlement identity does not absorb roads, rail, hydrology, hazards, archaeology, people, land, parcel, or infrastructure truth. | Joins cite other lanes. |
| Sensitive geometry tests | Prove public-safe identity carriers generalize or withhold precise geometry where risk requires it. | Identity does not publish sensitive location. |
| Correction and rollback tests | Prove identity corrections, tombstones, supersession, and rollback refs remain auditable. | No silent edit. |
| Public-surface tests | Prove map, API, tile, export, Focus Mode, and AI carriers cannot bypass evidence, policy, review, or release state. | Public carriers stay release-gated. |
| No-network tests | Prove local deterministic execution. | Integration requires separate gates. |

---

## Accepted Inputs

Only bounded, synthetic, reviewable inputs belong in this lane:

- synthetic identity fixtures with fake source refs, object refs, temporal scopes, normalized payloads, digests, evidence refs, policy refs, review refs, release refs, correction refs, withdrawal refs, and rollback refs
- synthetic object-family cases for Settlement, Municipality, CensusPlace, Townsite, GhostTown, Fort, Mission, ReservationCommunity, InfrastructureAsset, NetworkNode, NetworkSegment, Facility, ServiceArea, Operator, ConditionObservation, and Dependency
- synthetic source-role cases for observed, regulatory, modeled, aggregate, administrative, candidate, and synthetic posture where accepted vocabulary supports those roles
- synthetic temporal cases for source time, observed time, valid time, retrieval time, release time, correction time, supersession, tombstone, withdrawal, and rollback
- canary values that make source-role collapse, object-role collapse, time collapse, geometry overprecision, infrastructure leakage, cultural sensitivity leakage, map-truth leakage, AI leakage, logging, or public export obvious
- local validation envelopes emitted by test helpers

Safe outputs may include public-safe references and operational fields such as fixture ID, object family, source role, temporal scope, digest ref, validator name, finite outcome, reason code, evidence ref, policy decision ID, review record ID, release ref, correction ref, withdrawal ref, and rollback ref.

---

## Exclusions

Do not place these materials in this identity test lane:

| Excluded material | Why it does not belong here |
|---|---|
| Real source exports, census payloads, geocoder responses, utility records, cadastral records, critical-facility records, or public payloads | Default tests must stay synthetic, deterministic, and no-network. |
| Secrets, credentials, private endpoints, or production logs | Security and exposure risk. |
| Real EvidenceBundles, ProofPacks, production receipts, release manifests, rollback cards, correction notices, withdrawal notices, public artifacts, or audit ledgers | These are governed trust records or release artifacts. |
| Binding policy rules, schema definitions, contract prose, source descriptors, release procedures, graph implementation, map implementation, API implementation, or AI runtime implementation | Authority and implementation belong in their own roots. |
| Precise sensitive facility geometry, private dependency graphs, living-person details, ownership assertions, burial/sacred-site associations, or culturally sensitive community details | Sensitive joins require governed policy, review, redaction, generalization, and release controls. |
| Public map layers, tiles, screenshots, exports, Focus Mode outputs, AI context packets, or public API payloads | Publication requires governed release. |

---

## Suggested Layout

```text
tests/domains/settlements-infrastructure/identity/
|-- README.md
|-- test_identity_composition_requires_source_object_time_digest.py
|-- test_object_role_separation.py
|-- test_source_role_no_upcast.py
|-- test_temporal_scope_separation.py
|-- test_correction_does_not_rewrite_identity_history.py
|-- test_sensitive_geometry_not_public_identity.py
|-- test_cross_lane_identity_boundaries.py
|-- test_public_surfaces_require_release_state.py
`-- test_identity_no_network.py
```

This layout is PROPOSED until executable files exist in the repository.

---

## Run Posture

No executable runner was verified while authoring this README. Once tests exist, the expected local command should be documented and verified here.

```bash
: "PROPOSED / NEEDS VERIFICATION"
pytest tests/domains/settlements-infrastructure/identity
```

Required run posture: no network access, no live service calls, no real secrets, no production logs, no production trust artifacts, no public artifact writes, deterministic fixture inputs, and finite outcomes only: `PASS`, `DENY`, `ABSTAIN`, or `ERROR`.

---

## Minimal Identity Fixture

Synthetic fixtures should make identity boundaries inspectable without carrying real settlement, infrastructure, cultural, land, utility, or release data.

```json
{
  "fixture_id": "settlements-infrastructure-identity-example",
  "domain": "settlements-infrastructure",
  "object_family": "Municipality",
  "source_descriptor_id": "source-descriptor-fixture-si-identity-001",
  "source_role": "administrative",
  "identity_components": {
    "source_id": "source-fixture-admin-001",
    "object_role": "Municipality",
    "temporal_scope": {
      "valid_from": "1881-04-12",
      "valid_to": null
    },
    "normalized_digest": "jcs:sha256:fixture-only-not-a-real-digest"
  },
  "evidence_ref": "evidence-ref-fixture-si-identity-001",
  "policy_decision_ref": "policy-decision-fixture-si-identity-001",
  "review_record_ref": null,
  "release_manifest_ref": null,
  "rollback_card_ref": "rollback-card-fixture-si-identity-001",
  "expected_outcome": "ABSTAIN",
  "reason_code": "IDENTITY_TEST_DOES_NOT_AUTHORIZE_PUBLICATION",
  "must_not_claim": [
    "LEGAL_STATUS_CURRENT_CANARY",
    "CURRENT_BOUNDARY_CANARY",
    "CRITICAL_INFRASTRUCTURE_CANARY",
    "OWNERSHIP_CANARY",
    "CULTURAL_CLEARANCE_CANARY",
    "MAP_TRUTH_CANARY",
    "AI_TRUTH_CANARY",
    "RELEASE_APPROVAL_CANARY"
  ]
}
```

The JSON above is illustrative. Accepted schema, field names, fixture homes, source-role vocabulary, time-kind vocabulary, reason codes, and CI wiring remain NEEDS VERIFICATION.

---

## Evidence Ledger

| Source | Status | Supports | Limits |
|---|---|---|---|
| `Directory Rules.pdf` | CONFIRMED doctrine | `tests/` is the enforceability root; domain tests belong under `tests/domains/<domain>/`; authority roots remain separate. | Does not prove executable tests or make this lane implemented. |
| `docs/domains/settlements-infrastructure/IDENTITY_MODEL.md` | CONFIRMED repo evidence | Defines identity composition as source id + object role + temporal scope + normalized digest, with JCS/SHA-256 digest posture, object-family separation, source-role posture, and time separation. | Field names and schema bindings remain PROPOSED / NEEDS VERIFICATION where the doc says so. |
| `docs/domains/settlements-infrastructure/CANONICAL_PATHS.md` | CONFIRMED repo evidence | Identifies `settlements-infrastructure` as the working domain slug and records `settlement` as conflicted variance. | Does not prove every path exists or is implemented. |
| `docs/domains/settlements-infrastructure/sublanes/settlements.md` | CONFIRMED repo evidence | Documents place/community object families and explicit non-ownership of infrastructure, roads/rail, hydrology, hazards, people/land, archaeology, and cross-cutting receipts. | Sublane pattern is PROPOSED / NEEDS VERIFICATION. |
| `docs/domains/settlements-infrastructure/DATA_LIFECYCLE.md` | CONFIRMED repo evidence | Defines RAW to PUBLISHED lifecycle, source-role discipline, quarantine, evidence refs, receipts, public-safe surfaces, correction path, and rollback target. | Implementation-layer paths and artifact IDs remain PROPOSED. |
| `tests/domains/settlements-infrastructure/README.md` | CONFIRMED repo evidence | Parent test path exists as a greenfield stub. | Does not provide mature identity-test guidance or executable coverage. |
| GitHub target file before update | CONFIRMED repo evidence | `tests/domains/settlements-infrastructure/identity/README.md` existed as an empty placeholder before replacement. | Placeholder proves path existence only. |

---

## Validation Checklist

- [ ] Confirm accepted identity-test indexing convention for `tests/domains/settlements-infrastructure/identity/`.
- [ ] Confirm accepted fixture home and naming convention for identity fixtures.
- [ ] Confirm accepted contract and schema homes, including unresolved `settlement` versus `settlements-infrastructure` variance.
- [ ] Confirm accepted vocabulary for object roles, source roles, time kinds, temporal scope, normalized digest, spec hash, finite outcomes, and reason codes.
- [ ] Add executable tests for identity composition, digest determinism, object-role separation, source-role preservation, temporal separation, correction history, sensitive geometry, cross-lane boundaries, release gate, and no-network behavior.
- [ ] Confirm tests do not use real source feeds, live systems, secrets, production logs, production trust artifacts, sensitive geometry, or public artifact writes.
- [ ] Wire this lane into CI only after executable tests and safe fixtures exist.

---

## Rollback

Rollback is required if this identity test lane starts to store real source data, trust-bearing records, release records, public artifacts, secrets, production logs, binding policy, contract/schema authority, graph implementation, map implementation, API implementation, or AI runtime behavior.

Rollback is also required if this lane treats a test pass as settlement truth, legal status, current boundary proof, asset exposure approval, cultural clearance, infrastructure dependency disclosure, map truth, AI truth, release approval, correction approval, withdrawal approval, or rollback approval.

Rollback target: restore the previous safe README revision or remove this lane until parent index placement, fixtures, schemas, identity vocabulary, source-role handling, evidence expectations, policy expectations, release relationship, correction behavior, rollback behavior, and CI integration are reverified.

[Back to top](#top)