<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/connectors-ksu-research-extension-src-package-readme
title: connectors/ksu_research_extension/src/ksu_research_extension/ — KSU Research and Extension Compatibility Package Boundary
type: readme
version: v0.1
status: draft
owners: OWNER_TBD — Connector steward · Package maintainer · Kansas source steward · Agriculture steward · Weather steward · Soil steward · Rights reviewer · Sensitivity reviewer · Validation steward · Docs steward
created: 2026-06-19
updated: 2026-06-19
policy_label: public-doctrine; package-boundary; compatibility-lane; noncanonical-path; snake-case-compatibility; no-network-default; fixture-safe; rights-gated; sensitivity-gated; no-publication
proposed_path: connectors/ksu_research_extension/src/ksu_research_extension/README.md
truth_posture: CONFIRMED path exists / NONCANONICAL compatibility package README / MODULE INVENTORY NEEDS VERIFICATION
related:
  - ../../README.md
  - ../../tests/README.md
  - ../../../kansas/README.md
  - ../../../kansas/ksu-research-extension/README.md
  - ../../../../docs/sources/catalog/kansas/ksu-research-extension.md
  - ../../../../docs/sources/catalog/kansas/kansas-mesonet.md
  - ../../../../docs/domains/agriculture/README.md
  - ../../../../docs/domains/weather-atmospheric/README.md
  - ../../../../docs/domains/soil/README.md
  - ../../../../docs/sources/SOURCE_DESCRIPTOR_STANDARD.md
  - ../../../../data/registry/sources/
  - ../../../../fixtures/
  - ../../../../schemas/contracts/v1/source/
  - ../../../../policy/sensitivity/
  - ../../../../policy/rights/
  - ../../../../release/
tags: [kfm, connectors, ksu, k-state, research-extension, package, python, agriculture, weather, soil, compatibility, source-admission, no-network, raw, quarantine, governance]
notes:
  - "This README fills a blank package-boundary README under the top-level KSU R&E compatibility connector path."
  - "The KSU R&E source profile says v0.2 normalizes canonical connector placement to `connectors/kansas/ksu-research-extension/`."
  - "This README describes allowed implementation responsibilities only; it does not prove parser modules, fixtures, tests, endpoint access, or CI wiring exist."
  - "Package code must be no-network by default and may only emit RAW or QUARANTINE handoff envelopes after SourceDescriptor and activation gates are satisfied."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# KSU Research and Extension Compatibility Package Boundary

> Implementation-boundary README for the legacy `ksu_research_extension` package namespace under the top-level snake_case compatibility connector. This package may support source-admission parsing and validation helpers only; it is **not** a live harvester, truth store, release engine, public API, canonical connector home, or publication path.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Canonicality: noncanonical package path" src="https://img.shields.io/badge/canonicality-noncanonical__package-orange">
  <img alt="Network: disabled by default" src="https://img.shields.io/badge/network-disabled__by__default-critical">
  <img alt="Fixtures: required" src="https://img.shields.io/badge/fixtures-required-blue">
  <img alt="Lifecycle: RAW or QUARANTINE only" src="https://img.shields.io/badge/lifecycle-RAW%20%7C%20QUARANTINE%20only-orange">
</p>

> [!IMPORTANT]
> **Status:** `draft` compatibility package README · **Owner:** `OWNER_TBD`  
> **Path:** `connectors/ksu_research_extension/src/ksu_research_extension/README.md`  
> **Truth posture:** `CONFIRMED` file exists · `NONCANONICAL` compatibility package path · `NEEDS VERIFICATION` actual modules, fixtures, and CI wiring  
> **Boundary:** parser/validation helpers only; no live-network default, no source activation, no release artifact, no public claim.

**Quick jumps:** [Scope](#scope) · [Repo fit](#repo-fit) · [Allowed responsibilities](#allowed-responsibilities) · [Forbidden responsibilities](#forbidden-responsibilities) · [Expected module map](#expected-module-map) · [Evidence ledger](#evidence-ledger) · [Runtime posture](#runtime-posture) · [Validation contract](#validation-contract) · [Rollback](#rollback) · [Verification backlog](#verification-backlog)

---

## Scope

`connectors/ksu_research_extension/src/ksu_research_extension/` is a compatibility package namespace for KSU R&E source-admission helpers.

It may contain parser, normalizer, fixture loader, validation, source-role, product identity, rights, sensitivity, cadence/freshness, and handoff-envelope helpers for KSU R&E source metadata after SourceDescriptor and activation gates are satisfied.

It must not become a live ingestion job, public service, canonical connector home, SourceDescriptor authority, schema authority, policy authority, catalog/triplet authority, proof authority, release authority, or publication authority.

[Back to top ↑](#top)

---

## Repo fit

| Surface | Role | Status |
|---|---|---:|
| `connectors/ksu_research_extension/src/ksu_research_extension/` | Compatibility package namespace. | **CONFIRMED path / NEEDS VERIFICATION modules** |
| `connectors/ksu_research_extension/README.md` | Parent compatibility connector README. | **CONFIRMED** |
| `connectors/ksu_research_extension/tests/README.md` | Compatibility-path test contract. | **CONFIRMED** |
| `connectors/kansas/ksu-research-extension/` | Canonical KSU R&E connector path named by source profile. | **CONFIRMED by source profile / NEEDS VERIFICATION implementation depth** |
| `docs/sources/catalog/kansas/ksu-research-extension.md` | KSU R&E umbrella source profile. | **CONFIRMED** |
| `docs/sources/catalog/kansas/kansas-mesonet.md` | Kansas Mesonet sibling per-surface product page. | **CONFIRMED** |
| `release/` | Release and publication controls. | **Out of scope for this package** |

[Back to top ↑](#top)

---

## Allowed responsibilities

Package code may support:

- fixture-only parser tests;
- KSU R&E metadata shape normalization;
- snake_case compatibility helpers;
- source-role preservation;
- product identity helpers;
- umbrella-versus-surface separation helpers;
- source URI and retrieval timestamp preservation;
- rights statement extraction or preservation;
- sensitivity and review-state preservation helpers;
- cadence and freshness preservation helpers;
- SourceDescriptor and activation precondition checks;
- RAW or QUARANTINE handoff-envelope construction;
- deterministic error objects for quarantine or abstention;
- compatibility shims that point toward the canonical `connectors/kansas/ksu-research-extension/` lane.

---

## Forbidden responsibilities

Package code must not:

- fetch live source surfaces by default;
- store credentials, tokens, cookies, or session state;
- decide source activation;
- decide rights, sensitivity, redaction, release class, or public visibility;
- collapse KSU R&E umbrella material into Kansas Mesonet or peer-source records;
- write directly to processed, catalog, triplet, published, proof, receipt, or release roots;
- emit public agriculture, weather, soil, flora, or release claims;
- silently treat `connectors/ksu_research_extension/` as canonical;
- bypass SourceDescriptor, validation, EvidenceBundle, policy, release, correction, or rollback gates.

[Back to top ↑](#top)

---

## Expected module map

The following module map is **PROPOSED**, not confirmed implementation:

```text
connectors/ksu_research_extension/src/ksu_research_extension/
├── README.md              # CONFIRMED — this package-boundary README
├── __init__.py            # NEEDS VERIFICATION
├── descriptors.py         # PROPOSED — SourceDescriptor gate helpers
├── fetch.py               # PROPOSED — opt-in source access only; no-network default
├── parse.py               # PROPOSED — metadata parser helpers
├── normalize.py           # PROPOSED — field normalization without truth upgrade
├── roles.py               # PROPOSED — source-role separation helpers
├── identity.py            # PROPOSED — product and umbrella/surface identity helpers
├── freshness.py           # PROPOSED — cadence/freshness preservation helpers
├── handoff.py             # PROPOSED — RAW/QUARANTINE handoff envelope helpers
└── errors.py              # PROPOSED — deterministic fail-closed errors
```

Do not create these modules from this README alone; verify repo conventions, tests, and migration plan first.

---

## Evidence ledger

| Source | Status | Supports | Limits |
|---|---:|---|---|
| `connectors/ksu_research_extension/src/ksu_research_extension/README.md` | **CONFIRMED** | Target package README exists and was blank before this update. | Does not prove modules, tests, or CI. |
| `connectors/ksu_research_extension/README.md` | **CONFIRMED** | Parent path is documented as noncanonical snake_case compatibility lane. | Does not prove canonical migration status. |
| `connectors/ksu_research_extension/tests/README.md` | **CONFIRMED** | Test posture is no-network by default, fixture-safe, and source-admission only. | Does not prove tests exist or pass. |
| `docs/sources/catalog/kansas/ksu-research-extension.md` | **CONFIRMED** | Source profile says v0.2 normalizes canonical connector placement to `connectors/kansas/ksu-research-extension/` and frames KSU R&E as an umbrella source brief. | Does not prove endpoint availability, rights clearance, activation, or implementation. |
| Package modules below this path | **NEEDS VERIFICATION** | This README defines expected implementation boundaries. | Actual files, behavior, and CI status remain unverified. |

---

## Runtime posture

Default runtime posture for this package:

- no network unless explicitly enabled by reviewed configuration;
- no activation without SourceDescriptor and SourceActivationDecision;
- no public output;
- no direct writes beyond RAW or QUARANTINE handoff envelopes;
- no secrets in source, fixtures, logs, or test outputs;
- deterministic failure when rights, sensitivity, review state, source role, product identity, cadence/freshness, source shape, or activation state is unresolved.

A live-source path, if later approved, must be opt-in, reviewed, credential-safe, terms-reviewed, rate-limited, auditable, and excluded from default tests unless governance explicitly permits it.

---

## Validation contract

The package should provide or support validation for:

- SourceDescriptor and activation preconditions;
- snake_case compatibility versus canonical kebab-case path separation;
- KSU R&E umbrella versus per-surface product separation;
- source-role preservation;
- product identity preservation;
- source URI and retrieval timestamp preservation;
- rights statement presence and preservation;
- sensitivity and review-state preservation;
- cadence and freshness preservation;
- fail-closed quarantine or abstention errors;
- RAW/QUARANTINE-only handoff envelopes;
- refusal to emit release/public artifacts.

Validation must be paired with tests before any implementation maturity is claimed.

[Back to top ↑](#top)

---

## Rollback

Rollback is required if this README is used to justify live harvesting, source activation, canonical status, public release, rights/sensitivity bypass, source-role collapse, umbrella/surface collapse, or implementation maturity without tests.

Rollback target:

```text
commit prior to this update: SHA_TBD_AFTER_GIT_HISTORY_CHECK
```

Because the file was blank before this update, a safe rollback is to restore the blank placeholder or replace this document with a shorter package-compatibility note until canonical placement and implementation are verified.

---

## Verification backlog

| Item | Status | Needed evidence |
|---|---:|---|
| Confirm actual package module inventory. | **NEEDS VERIFICATION** | Repo tree or mounted workspace. |
| Confirm canonical KSU R&E package path. | **NEEDS VERIFICATION** | Directory Rules, ADR, migration note, or repo convention. |
| Confirm SourceDescriptor and activation gate wiring. | **NEEDS VERIFICATION** | Source registry entry, code, and tests. |
| Confirm rights/sensitivity/review-state handling. | **NEEDS VERIFICATION** | Policy references, code, and tests. |
| Confirm RAW/QUARANTINE handoff envelope shape. | **NEEDS VERIFICATION** | Schemas/contracts and tests. |
| Confirm fixture strategy and CI wiring. | **NEEDS VERIFICATION** | Fixture registry, workflow files, and test logs. |

---

## Maintainer note

Keep this package small, deterministic, and reversible. It should parse and preserve KSU R&E source material for governed admission only. Public truth, sensitivity policy decisions, release approval, correction, and rollback live outside this package.

[Back to top ↑](#top)
