<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-domains-hydrology-no-network-readme
title: Hydrology No-Network Test README
type: test-readme
version: v0.1
status: draft; placeholder-expanded; no-network-test-lane; PROPOSED / NEEDS VERIFICATION before promotion
owners:
  - OWNER_TBD — Hydrology domain steward
  - OWNER_TBD — QA steward
  - OWNER_TBD — Fixture steward
  - OWNER_TBD — Source steward
  - OWNER_TBD — Evidence steward
  - OWNER_TBD — Policy steward
  - OWNER_TBD — Release steward
created: NEEDS VERIFICATION — blank placeholder existed before v0.1 expansion
updated: 2026-07-05
policy_label: public-doc; tests; hydrology; no-network; fixture-only; source-boundary; evidence-bound; policy-aware; release-gated; rollback-aware
tags: [kfm, tests, hydrology, no-network, fixture-only, source-admission, SourceDescriptor, EvidenceBundle, PolicyDecision, ReleaseManifest, CorrectionNotice, RollbackCard, ABSTAIN, DENY, ERROR]
related:
  - ../../../README.md
  - ../README.md
  - ../identity/README.md
  - ../continuity_inventory_check/README.md
  - ../../../../docs/domains/hydrology/README.md
  - ../../../../docs/domains/hydrology/DATA_LIFECYCLE.md
  - ../../../../docs/domains/hydrology/BOUNDARY.md
  - ../../../../docs/domains/hydrology/SOURCE_REGISTRY.md
  - ../../../../docs/domains/hydrology/IDENTITY_MODEL.md
  - ../../../../docs/domains/hydrology/CONTINUITY_INVENTORY.md
  - ../../../../pipelines/domains/hydrology/README.md
  - ../../../../pipelines/domains/hydrology/ingest_3dep_terrain/README.md
  - ../../../../data/registry/sources/hydrology/
  - ../../../../fixtures/domains/hydrology/no_network/
  - ../../../../contracts/domains/hydrology/
  - ../../../../schemas/contracts/v1/domains/hydrology/
  - ../../../../policy/domains/hydrology/
  - ../../../../release/manifests/hydrology/
notes:
  - "This file replaces a blank placeholder at tests/domains/hydrology/no_network/README.md."
  - "This is a test-lane README only. It does not define Hydrology doctrine, no-network policy, contracts, schemas, fixtures, source descriptors, lifecycle records, EvidenceBundles, policy rules, release decisions, pipeline code, public API material, public map material, public tiles, or published artifacts."
  - "The tested invariant is that default Hydrology tests remain deterministic and no-network: tests use fixtures, mocks, local schema/contract files, and recorded source descriptors rather than live source fetches, real upstream exports, public tiles, or direct lifecycle stores."
  - "Live network behavior, source-admission refresh, upstream watcher checks, and real ingest should belong only in separately gated integration lanes with explicit receipts, policy posture, review state, correction path, and rollback targets."
  - "Rollback target for this replacement is previous blank blob SHA 8b137891791fe96927ad78e64b0aad7bded08bdc."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Hydrology no-network tests

> Deterministic, fixture-only test documentation for proving that default Hydrology tests do not fetch live sources, call upstream services, read lifecycle stores as authority, write public artifacts, or infer release state from network availability.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: tests" src="https://img.shields.io/badge/root-tests%2F-blue">
  <img alt="Domain: hydrology" src="https://img.shields.io/badge/domain-hydrology-2aa1c6">
  <img alt="Lane: no network" src="https://img.shields.io/badge/lane-no__network-blue">
  <img alt="Network: disabled" src="https://img.shields.io/badge/network-disabled-critical">
  <img alt="Boundary: fixture only" src="https://img.shields.io/badge/boundary-fixture__only-success">
</p>

**Path:** `tests/domains/hydrology/no_network/README.md`  
**Status:** draft / placeholder-expanded / PROPOSED until executable tests are verified  
**Owning root:** `tests/`  
**Domain segment:** `hydrology`  
**Test lane:** `no_network`  
**Default execution posture:** deterministic, synthetic, no-network, public-safe fixtures only  
**Truth posture:** CONFIRMED target was a blank placeholder before this expansion · CONFIRMED `tests/` is the canonical root for enforceability proof · CONFIRMED current Hydrology test-parent README remains a greenfield stub · CONFIRMED Hydrology pipeline docs state concrete executable behavior, source linkage, schedules, CI coverage, release wiring, and public API/map behavior remain NEEDS VERIFICATION where not implemented and tested · NEEDS VERIFICATION for executable no-network guards, monkeypatch behavior, fixture payload inventory, CI wiring, and pass rates.

---

## Purpose

`tests/domains/hydrology/no_network/` is the intended home for Hydrology tests that prove the default suite is isolated from live source systems.

This lane should make sure Hydrology tests run from local fixtures, local schemas/contracts, recorded SourceDescriptor-like inputs, and deterministic stubs. It should block accidental network calls, direct upstream fetches, implicit watcher refreshes, real source exports, public tile access, and direct use of lifecycle stores as authority.

A passing test here should **not** mean that source admission is current, real hydrology data is refreshed, a watcher ran, a pipeline is complete, or a release is approved. It should mean only that the default Hydrology test path stayed deterministic and offline.

---

## Placement basis

`tests/` is the canonical root for enforceability proof. Hydrology is a domain segment inside that root. `no_network/` is a test lane, not a pipeline implementation folder, source connector, source registry, lifecycle store, policy home, release home, public API surface, or public map surface.

| Responsibility | Correct home | This lane's relationship |
|---|---|---|
| No-network Hydrology tests | `tests/domains/hydrology/no_network/` | This directory. |
| Hydrology source registry | `data/registry/sources/hydrology/` | Source metadata context; not fetched live here. |
| Hydrology fixtures | `fixtures/domains/hydrology/no_network/` | Preferred toy and recorded inputs if populated. |
| Hydrology pipelines | `pipelines/domains/hydrology/` | Systems under integration test elsewhere; not executed live by default here. |
| Hydrology contracts/schemas | `contracts/domains/hydrology/`, `schemas/contracts/v1/domains/hydrology/` | Local files under check where accepted. |
| Hydrology policy | `policy/domains/hydrology/` | Referenced by tests, not bypassed here. |
| Release decisions | `release/` and `release/manifests/hydrology/` | Publication, correction, and rollback authority; tests cannot replace it. |

---

## Invariant under test

> **Default Hydrology tests are offline and deterministic.** They may validate contracts, schemas, fixtures, source-role metadata, evidence posture, policy envelopes, lifecycle boundaries, release requirements, correction, and rollback, but they must not contact live sources or treat network success as proof.

Core checks:

| Check | Required behavior | Failure outcome |
|---|---|---|
| Network block | HTTP, object-store, remote API, tile, and source-download calls are blocked by default. | validation failure / `ERROR`. |
| Fixture-only inputs | Tests use local fixtures or deterministic stubs. | validation failure. |
| Source boundary | SourceDescriptor metadata may be inspected locally; upstream refresh belongs to gated integration lanes. | validation failure / `ABSTAIN`. |
| Lifecycle boundary | Tests do not read RAW / WORK / QUARANTINE / PROCESSED / PUBLISHED as authority unless a scoped fixture explicitly models it. | validation failure. |
| Evidence posture | Evidence-dependent claims use local fixture EvidenceRefs/EvidenceBundles or return a finite non-answer. | `ABSTAIN`. |
| Policy posture | Missing local policy support produces finite hold/deny/abstain/error behavior. | `DENY` / `ABSTAIN` / `ERROR`. |
| Release boundary | Test pass does not become release approval, public artifact authority, or source freshness proof. | promotion block. |
| Auditability | Any allowed integration escape hatch must be explicit, separately named, receipt-backed, and excluded from the default suite. | validation failure. |

---

## Expected scope

Tests in this lane may validate:

- monkeypatch or fixture-based blocking of outbound network clients;
- failure on accidental calls to HTTP libraries, cloud object stores, source APIs, map-tile URLs, package downloaders, or live catalog endpoints;
- local-only use of source descriptors, schema files, contract files, fixture files, and recorded manifests;
- no direct reads from `data/raw/`, `data/work/`, `data/quarantine/`, `data/processed/`, or `release/` as authority in default unit tests;
- finite `ABSTAIN`, `DENY`, or `ERROR` outcomes when live freshness or source support is unavailable;
- separation between default unit tests and explicitly gated integration tests.

Live source checks, real source exports, production credentials, public tile generation, and real hydrology payloads are out of scope for the default suite.

---

## Fixture posture

Use synthetic, public-safe fixtures only.

Fixture requirements:

- deterministic and no-network;
- compact enough for review in a PR;
- explicit expected outcome;
- explicit source, object role, evidence posture, policy state, release relationship, correction, and rollback posture where material;
- no real source exports, credentials, live endpoints, public tiles, restricted records, or published artifacts.

---

## Finite outcomes

| Condition | Expected outcome |
|---|---|
| Test attempts HTTP/source/tile/cloud/network access in default suite | validation failure / `ERROR`. |
| Test uses local synthetic fixture and local contract/schema files | accepted no-network support only. |
| Live source freshness is required but unavailable | `ABSTAIN` / NEEDS VERIFICATION. |
| SourceDescriptor is missing from local fixture context | `ABSTAIN` or validation failure. |
| Production credential is referenced | validation failure / `DENY`. |
| Public tile or release artifact is treated as proof of source state | validation failure. |
| Integration-only behavior is run in the default lane | validation failure. |

---

## Suggested layout

```text
tests/domains/hydrology/no_network/
├── README.md
├── test_network_clients_blocked.py
├── test_fixtures_are_local.py
├── test_source_refresh_not_default.py
├── test_no_lifecycle_store_authority.py
├── test_no_public_tile_dependency.py
├── test_missing_live_support_abstains.py
└── test_integration_escape_hatches_are_explicit.py
```

---

## Run posture

```bash
pytest tests/domains/hydrology/no_network
```

Status of the command above: **PROPOSED / NEEDS VERIFICATION**. It assumes `pytest` is the accepted test runner and that executable test modules exist. This README does not claim the command currently passes.

---

## Evidence ledger

| Evidence | Status | Supports | Limits |
|---|---|---|---|
| Previous target file | CONFIRMED | `tests/domains/hydrology/no_network/README.md` existed as a blank placeholder before this replacement. | Did not define the lane. |
| `tests/README.md` | CONFIRMED | `tests/` is enforceability proof and failure should block promotion where trust-spine checks fail. | Does not prove this lane's modules or pass rate. |
| `tests/domains/hydrology/README.md` | CONFIRMED | Hydrology test parent currently exists as a greenfield stub. | Parent lane still needs expansion. |
| Hydrology pipeline docs | CONFIRMED documentation evidence | Existing Hydrology pipeline documentation keeps source linkage, schedules, CI, release wiring, and public behavior as NEEDS VERIFICATION unless implemented and tested. | Pipeline docs are not no-network test implementation. |
| Repo search | CONFIRMED | No Hydrology-specific no-network README was found before this replacement. | Search is not proof of absence or executable coverage. |

---

## Validation checklist

- [ ] Executable test modules exist under this lane.
- [ ] Test runner and import paths match the repo's accepted convention.
- [ ] Network clients are actually blocked or monkeypatched by the test harness.
- [ ] Synthetic fixtures exist for local-only success, accidental HTTP call, tile fetch attempt, source refresh attempt, credential reference, missing local descriptor, and integration-only escape hatch cases.
- [ ] No default test requires production credentials, live source access, or public tiles.
- [ ] EvidenceRef / EvidenceBundle behavior is available to tests or safely stubbed.
- [ ] PolicyDecision, ReleaseManifest, CorrectionNotice, RedactionReceipt, and RollbackCard expectations remain referenced but not bypassed.
- [ ] CI runs the no-network Hydrology suite before any integration suite.
- [ ] Failures block public carrier promotion or release candidate approval where material.

---

## Rollback

Rollback is required if this lane becomes a live source-fetcher, lifecycle data store, source registry, contract root, schema authority, policy authority, proof store, release-decision root, public map/API/tile surface, AI surface, renderer implementation, pipeline implementation, or publication shortcut.

Rollback target for this replacement: previous blank blob SHA `8b137891791fe96927ad78e64b0aad7bded08bdc`.

<p align="right"><a href="#top">Back to top</a></p>
