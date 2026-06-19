<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/connectors-khri-src-package-readme
title: connectors/khri/src/khri/ — KHRI Compatibility Package Boundary
type: readme
version: v0.1
status: draft
owners: OWNER_TBD — Connector steward · Package maintainer · Kansas source steward · KSHS/archives liaison · Archaeology steward · Settlements steward · Rights reviewer · Sensitivity reviewer · Validation steward · Docs steward
created: 2026-06-19
updated: 2026-06-19
policy_label: public-doctrine; package-boundary; compatibility-lane; noncanonical-path; no-network-default; fixture-safe; rights-gated; sensitivity-gated; no-publication
proposed_path: connectors/khri/src/khri/README.md
truth_posture: CONFIRMED path exists / NONCANONICAL compatibility package README / MODULE INVENTORY NEEDS VERIFICATION
related:
  - ../../README.md
  - ../../tests/README.md
  - ../../../kansas/README.md
  - ../../../kansas/khri/README.md
  - ../../../../docs/sources/catalog/kansas/khri.md
  - ../../../../docs/sources/catalog/kansas/kansas-state-archives.md
  - ../../../../docs/domains/archaeology/README.md
  - ../../../../docs/domains/settlements-infrastructure/README.md
  - ../../../../docs/domains/people-dna-land/README.md
  - ../../../../docs/sources/SOURCE_DESCRIPTOR_STANDARD.md
  - ../../../../data/registry/sources/
  - ../../../../data/raw/archaeology/
  - ../../../../data/quarantine/archaeology/
  - ../../../../data/raw/settlements-infrastructure/
  - ../../../../data/quarantine/settlements-infrastructure/
  - ../../../../fixtures/
  - ../../../../schemas/contracts/v1/source/
  - ../../../../policy/sensitivity/
  - ../../../../policy/rights/
  - ../../../../release/
tags: [kfm, connectors, khri, package, python, kshs, kansas, historic-resources, archaeology, settlements, cultural-resources, compatibility, source-admission, no-network, raw, quarantine, governance]
notes:
  - "This README fills a blank package-boundary README under the top-level KHRI compatibility connector path."
  - "The KHRI source dossier says canonical KHRI connector work belongs under `connectors/kansas/khri/`; this top-level package path is compatibility-only."
  - "This README describes allowed implementation responsibilities only; it does not prove parser modules, fixtures, tests, endpoint access, or CI wiring exist."
  - "Package code must be no-network by default and may only emit RAW or QUARANTINE handoff envelopes after SourceDescriptor and activation gates are satisfied."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# KHRI Compatibility Package Boundary

> Implementation-boundary README for the legacy `khri` package namespace under the top-level compatibility connector. This package may support source-admission parsing and validation helpers only; it is **not** a live harvester, truth store, release engine, public API, canonical connector home, or cultural-resource publication path.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Canonicality: noncanonical package path" src="https://img.shields.io/badge/canonicality-noncanonical__package-orange">
  <img alt="Network: disabled by default" src="https://img.shields.io/badge/network-disabled__by__default-critical">
  <img alt="Fixtures: required" src="https://img.shields.io/badge/fixtures-required-blue">
  <img alt="Lifecycle: RAW or QUARANTINE only" src="https://img.shields.io/badge/lifecycle-RAW%20%7C%20QUARANTINE%20only-orange">
</p>

> [!IMPORTANT]
> **Status:** `draft` compatibility package README · **Owner:** `OWNER_TBD`  
> **Path:** `connectors/khri/src/khri/README.md`  
> **Truth posture:** `CONFIRMED` file exists · `NONCANONICAL` compatibility package path · `NEEDS VERIFICATION` actual modules, fixtures, and CI wiring  
> **Boundary:** parser/validation helpers only; no live-network default, no source activation, no release artifact, no public cultural-resource claim.

**Quick jumps:** [Scope](#scope) · [Repo fit](#repo-fit) · [Allowed responsibilities](#allowed-responsibilities) · [Forbidden responsibilities](#forbidden-responsibilities) · [Expected module map](#expected-module-map) · [Evidence ledger](#evidence-ledger) · [Runtime posture](#runtime-posture) · [Validation contract](#validation-contract) · [Rollback](#rollback) · [Verification backlog](#verification-backlog)

---

## Scope

`connectors/khri/src/khri/` is a compatibility package namespace for KHRI source-admission helpers.

It may contain parser, normalizer, fixture loader, validation, source-role, surface-identity, rights, sensitivity, geometry, and handoff-envelope helpers for KHRI metadata after SourceDescriptor and activation gates are satisfied.

It must not become a live ingestion job, public service, canonical connector home, SourceDescriptor authority, schema authority, policy authority, catalog/triplet authority, proof authority, release authority, or publication authority.

[Back to top ↑](#top)

---

## Repo fit

| Surface | Role | Status |
|---|---|---:|
| `connectors/khri/src/khri/` | Compatibility package namespace. | **CONFIRMED path / NEEDS VERIFICATION modules** |
| `connectors/khri/README.md` | Parent compatibility connector README. | **CONFIRMED** |
| `connectors/khri/tests/README.md` | Compatibility-path test contract. | **CONFIRMED** |
| `connectors/kansas/khri/` | Canonical KHRI connector path named by source dossier. | **CONFIRMED by source dossier / NEEDS VERIFICATION implementation depth** |
| `docs/sources/catalog/kansas/khri.md` | KHRI per-surface source dossier. | **CONFIRMED** |
| `docs/sources/catalog/kansas/kansas-state-archives.md` | KSHS umbrella source-family brief. | **CONFIRMED** |
| `data/raw/archaeology/`, `data/raw/settlements-infrastructure/` | Candidate RAW handoff targets. | **PROPOSED / NEEDS VERIFICATION** |
| `data/quarantine/archaeology/`, `data/quarantine/settlements-infrastructure/` | Candidate quarantine handoff targets. | **PROPOSED / NEEDS VERIFICATION** |
| `release/` | Release and publication controls. | **Out of scope for this package** |

[Back to top ↑](#top)

---

## Allowed responsibilities

Package code may support:

- fixture-only parser tests;
- KHRI metadata shape normalization;
- KHRI/KSHS surface identity preservation;
- source-role preservation;
- inventory/resource identity helpers;
- resource-type preservation helpers;
- rights statement extraction or preservation;
- sensitivity and review-state preservation helpers;
- geometry precision and uncertainty preservation helpers;
- source URI and retrieval timestamp preservation;
- SourceDescriptor and activation precondition checks;
- RAW or QUARANTINE handoff-envelope construction;
- deterministic error objects for quarantine or abstention;
- compatibility shims that point toward the canonical `connectors/kansas/khri/` lane.

---

## Forbidden responsibilities

Package code must not:

- fetch live KHRI/KSHS surfaces by default;
- store credentials, tokens, cookies, or session state;
- decide source activation;
- decide rights, sensitivity, redaction, release class, or public visibility;
- collapse KHRI into Kansas Memory, KSHS State Archives proper, county society holdings, GNIS, parcel/person records, archaeology records, or generated summaries;
- write directly to processed, catalog, triplet, published, proof, receipt, or release roots;
- emit public cultural-resource, archaeology, parcel, owner, occupant, eligibility, designation, planning, or release claims;
- silently treat `connectors/khri/` as canonical;
- bypass SourceDescriptor, validation, EvidenceBundle, policy, release, correction, or rollback gates.

[Back to top ↑](#top)

---

## Expected module map

The following module map is **PROPOSED**, not confirmed implementation:

```text
connectors/khri/src/khri/
├── README.md              # CONFIRMED — this package-boundary README
├── __init__.py            # NEEDS VERIFICATION
├── descriptors.py         # PROPOSED — SourceDescriptor gate helpers
├── fetch.py               # PROPOSED — opt-in source access only; no-network default
├── parse.py               # PROPOSED — metadata parser helpers
├── normalize.py           # PROPOSED — field normalization without truth upgrade
├── roles.py               # PROPOSED — source-role separation helpers
├── identity.py            # PROPOSED — inventory/resource/surface identity helpers
├── sensitivity.py         # PROPOSED — sensitivity/review-state preservation helpers
├── geometry.py            # PROPOSED — geometry precision/uncertainty preservation helpers
├── handoff.py             # PROPOSED — RAW/QUARANTINE handoff envelope helpers
└── errors.py              # PROPOSED — deterministic fail-closed errors
```

Do not create these modules from this README alone; verify repo conventions, tests, and migration plan first.

---

## Evidence ledger

| Source | Status | Supports | Limits |
|---|---:|---|---|
| `connectors/khri/src/khri/README.md` | **CONFIRMED** | Target package README exists and was blank before this update. | Does not prove modules, tests, or CI. |
| `connectors/khri/README.md` | **CONFIRMED** | Parent path is documented as noncanonical compatibility lane. | Does not prove canonical migration status. |
| `connectors/khri/tests/README.md` | **CONFIRMED** | Test posture is no-network by default, fixture-safe, and source-admission only. | Does not prove tests exist or pass. |
| `docs/sources/catalog/kansas/khri.md` | **CONFIRMED** | KHRI dossier says canonical connector path is `connectors/kansas/khri/` and frames KHRI as a KSHS-operated per-surface product page. | Does not prove endpoint availability, rights clearance, activation, or implementation. |
| `docs/sources/catalog/kansas/kansas-state-archives.md` | **CONFIRMED** | KSHS umbrella brief says umbrella posture does not replace per-surface descriptors. | Does not define package behavior alone. |
| Package modules below this path | **NEEDS VERIFICATION** | This README defines expected implementation boundaries. | Actual files, behavior, and CI status remain unverified. |

---

## Runtime posture

Default runtime posture for this package:

- no network unless explicitly enabled by reviewed configuration;
- no activation without SourceDescriptor and SourceActivationDecision;
- no public output;
- no direct writes beyond RAW or QUARANTINE handoff envelopes;
- no secrets in source, fixtures, logs, or test outputs;
- deterministic failure when rights, sensitivity, review state, source role, surface identity, inventory identity, resource type, geometry precision, source shape, or activation state is unresolved.

A live-source path, if later approved, must be opt-in, source-steward reviewed, credential-safe, terms-reviewed, rate-limited, sensitivity-reviewed, auditable, and excluded from default tests unless governance explicitly permits it.

---

## Validation contract

The package should provide or support validation for:

- SourceDescriptor and activation preconditions;
- KHRI/KSHS surface identity preservation;
- source-role preservation;
- inventory/resource identity preservation;
- resource-type preservation;
- source URI and retrieval timestamp preservation;
- rights statement presence and preservation;
- sensitivity and review-state preservation;
- geometry precision and uncertainty preservation;
- fail-closed quarantine or abstention errors;
- RAW/QUARANTINE-only handoff envelopes;
- refusal to emit release/public artifacts.

Validation must be paired with tests before any implementation maturity is claimed.

[Back to top ↑](#top)

---

## Rollback

Rollback is required if this README is used to justify live harvesting, source activation, canonical status, public release, rights/sensitivity bypass, source-role collapse, cultural-resource exposure, or implementation maturity without tests.

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
| Confirm canonical KHRI package path. | **NEEDS VERIFICATION** | Directory Rules, ADR, migration note, or repo convention. |
| Confirm SourceDescriptor and activation gate wiring. | **NEEDS VERIFICATION** | Source registry entry, code, and tests. |
| Confirm current access method and metadata shapes. | **NEEDS VERIFICATION** | Source steward review and current source documentation. |
| Confirm rights/sensitivity/review-state handling. | **NEEDS VERIFICATION** | Policy references, code, and tests. |
| Confirm RAW/QUARANTINE handoff envelope shape. | **NEEDS VERIFICATION** | Schemas/contracts and tests. |
| Confirm fixture strategy and CI wiring. | **NEEDS VERIFICATION** | Fixture registry, workflow files, and test logs. |

---

## Maintainer note

Keep this package small, deterministic, and reversible. It should parse and preserve KHRI source material for governed admission only. Public truth, sensitivity policy decisions, release approval, correction, and rollback live outside this package.

[Back to top ↑](#top)
