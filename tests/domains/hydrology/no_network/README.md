<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-domains-hydrology-no-network-readme
title: Hydrology No-Network Test README
type: test-readme
version: v0.3
status: draft; bounded-python-process-egress-proof-executable; runner-wide-and-non-python-isolation-held
owners:
  - OWNER_TBD — Hydrology domain steward
  - OWNER_TBD — QA steward
  - OWNER_TBD — Fixture steward
  - OWNER_TBD — Source steward
  - OWNER_TBD — Evidence steward
  - OWNER_TBD — Policy steward
  - OWNER_TBD — Release steward
created: 2026-05-14
updated: 2026-08-28
policy_label: public-doc; tests; hydrology; no-network; fixture-only; source-boundary; evidence-bound; policy-aware; release-gated; rollback-aware
owning_root: tests/
responsibility: Document and route the bounded Hydrology Python-process no-egress proof without claiming runner-wide isolation or broader Hydrology authority.
truth_posture: cite-or-abstain
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
  - ../test_no_network_proof.py
  - ../../../../tools/ci/kfm_no_network/
  - ../../../../.github/workflows/domain-hydrology.yml
notes:
  - "This file replaces a blank placeholder at tests/domains/hydrology/no_network/README.md."
  - "This is a test-lane README only. It does not define Hydrology doctrine, no-network policy, contracts, schemas, fixtures, source descriptors, lifecycle records, EvidenceBundles, policy rules, release decisions, pipeline code, public API material, public map material, public tiles, or published artifacts."
  - "The tested invariant is that default Hydrology tests remain deterministic and no-network: tests use fixtures, mocks, local schema/contract files, and recorded source descriptors rather than live source fetches, real upstream exports, public tiles, or direct lifecycle stores."
  - "The bounded executable proof starts fresh Python interpreters and confirms that the opt-in sitecustomize guard denies 15 named IPv4/IPv6 connection, socket-send, resolver, and URL-open APIs before application imports."
  - "The guard is Python-process enforcement only; it does not establish runner-wide, operating-system, container, namespace, dependency-install, or non-Python isolation."
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
  <img alt="Python egress: guarded" src="https://img.shields.io/badge/python__egress-guarded-critical">
  <img alt="Boundary: fixture only" src="https://img.shields.io/badge/boundary-fixture__only-success">
</p>

**Path:** `tests/domains/hydrology/no_network/README.md`  
**Status:** draft / bounded Python-process egress proof executable / runner-wide and non-Python isolation held
**Owning root:** `tests/`  
**Domain segment:** `hydrology`  
**Test lane:** `no_network`  
**Default execution posture:** deterministic, synthetic, no-network, public-safe fixtures only  
**Truth posture:** CONFIRMED `tests/` is the canonical root for enforceability proof · CONFIRMED `test_no_network_proof.py` starts fresh interpreters and exercises the shared opt-in Python startup guard · CONFIRMED the Hydrology workflow injects that guard into every Python process in its bounded validation step · NEEDS VERIFICATION for exact-head hosted results · runner-wide, non-Python, dependency-install, source, evidence, policy, proof, release, deployment, and publication claims remain held.

---

## Purpose

`tests/domains/hydrology/no_network/` documents the Hydrology no-network lane.
The executable proof is the substantive parent-lane module
`tests/domains/hydrology/test_no_network_proof.py`; the reusable startup helper
is owned by `tools/ci/kfm_no_network/` and workflow injection remains owned by
`.github/workflows/domain-hydrology.yml`.

The accepted bounded workflow path runs from local fixtures, schemas, contracts,
and deterministic stubs. Every Python interpreter in the validation step loads
the startup guard before application imports. The negative proof confirms denial
for 15 named connection, socket-send, resolver, and URL-open APIs.

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
| Python-process network block | Fifteen named IPv4/IPv6 connection, socket-send, resolver, and `urllib` URL-open APIs are denied when the workflow injects the guard. | validation failure / `ERROR`. |
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

## Current bounded layout

```text
tests/domains/hydrology/
├── test_no_network_proof.py
└── no_network/
    └── README.md

tools/ci/kfm_no_network/
├── README.md
└── sitecustomize.py
```

---

## Run posture

```bash
PYTHONDONTWRITEBYTECODE=1 KFM_NO_NETWORK=1 \
python -m pytest -q -p no:cacheprovider \
  tests/domains/hydrology/test_no_network_proof.py
```

This command is executable locally. The authoritative hosted result remains the
exact-head `domain-hydrology` run after a branch is pushed; absent that run,
hosted status is `NOT_RUN`.

---

## Evidence ledger

| Evidence | Status | Supports | Limits |
|---|---|---|---|
| Previous target file | CONFIRMED | `tests/domains/hydrology/no_network/README.md` existed as a blank placeholder before this replacement. | Did not define the lane. |
| `tests/README.md` | CONFIRMED | `tests/` is enforceability proof and failure should block promotion where trust-spine checks fail. | Does not prove this lane's modules or pass rate. |
| `test_no_network_proof.py` | CONFIRMED bounded executable proof | Fresh Python interpreters deny 15 named egress APIs, require explicit activation, and retain Unix-domain routing. | No host firewall, namespace, container, non-Python, runner-wide, or non-named API proof. |
| `tools/ci/kfm_no_network/sitecustomize.py` | CONFIRMED bounded CI helper | Guard loads at interpreter startup when its directory is on `PYTHONPATH` and `KFM_NO_NETWORK=1`. | Not active for commands outside the explicitly injected environment. |
| `.github/workflows/domain-hydrology.yml` | CONFIRMED workflow definition / hosted result pending | Injects the guard into each Python process in the bounded validation step and runs the negative proof first. | Does not cover dependency installation, shell-native clients, actions, or the runner outside that step. |
| Hydrology pipeline docs | CONFIRMED documentation evidence | Existing Hydrology pipeline documentation keeps source linkage, schedules, CI, release wiring, and public behavior as NEEDS VERIFICATION unless implemented and tested. | Pipeline docs are not no-network test implementation. |
| Repo search | CONFIRMED | No Hydrology-specific no-network README was found before this replacement. | Search is not proof of absence or executable coverage. |

---

## Validation checklist

- [x] Executable bounded proof module exists in the Hydrology parent test lane.
- [x] Test runner and import paths match the accepted Hydrology workflow convention.
- [x] Fresh interpreters deny the named Python-process network paths when explicitly guarded.
- [ ] Synthetic fixtures exist for local-only success, accidental HTTP call, tile fetch attempt, source refresh attempt, credential reference, missing local descriptor, and integration-only escape hatch cases.
- [ ] No default test requires production credentials, live source access, or public tiles.
- [ ] EvidenceRef / EvidenceBundle behavior is available to tests or safely stubbed.
- [ ] PolicyDecision, ReleaseManifest, CorrectionNotice, RedactionReceipt, and RollbackCard expectations remain referenced but not bypassed.
- [x] CI runs the no-network proof before the remaining bounded Hydrology modules and validators.
- [ ] Failures block public carrier promotion or release candidate approval where material.

---

## Rollback

Rollback is required if this lane becomes a live source-fetcher, lifecycle data store, source registry, contract root, schema authority, policy authority, proof store, release-decision root, public map/API/tile surface, AI surface, renderer implementation, pipeline implementation, or publication shortcut.

Rollback this slice by reverting the guard, proof, workflow wiring, and this
documentation update together. That restores the prior declared-posture-only
state; it does not authorize live access, source admission, lifecycle mutation,
proof, release, deployment, or publication.

<p align="right"><a href="#top">Back to top</a></p>
