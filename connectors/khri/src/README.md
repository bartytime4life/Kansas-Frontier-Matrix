<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/connectors-khri-src-readme
title: connectors/khri/src/ — KHRI Compatibility Source Layout Boundary
type: readme
version: v0.1
status: draft
owners: OWNER_TBD — Connector steward · Package maintainer · Kansas source steward · KSHS/archives liaison · Rights reviewer · Sensitivity reviewer · Validation steward · Docs steward
created: 2026-06-19
updated: 2026-06-19
policy_label: public-doctrine; src-layout-boundary; compatibility-lane; noncanonical-path; no-network-default; fixture-safe; rights-gated; sensitivity-gated; no-publication
proposed_path: connectors/khri/src/README.md
truth_posture: CONFIRMED path exists / NONCANONICAL compatibility src README / PACKAGE INVENTORY NEEDS VERIFICATION
related:
  - ../README.md
  - ../tests/README.md
  - ./khri/README.md
  - ../../kansas/README.md
  - ../../kansas/khri/README.md
  - ../../../docs/sources/catalog/kansas/khri.md
  - ../../../docs/sources/catalog/kansas/kansas-state-archives.md
  - ../../../docs/sources/SOURCE_DESCRIPTOR_STANDARD.md
  - ../../../data/registry/sources/
  - ../../../fixtures/
  - ../../../schemas/contracts/v1/source/
  - ../../../policy/sensitivity/
  - ../../../policy/rights/
  - ../../../release/
tags: [kfm, connectors, khri, src, package-layout, kshs, kansas, historic-resources, compatibility, source-admission, no-network, raw, quarantine, governance]
notes:
  - "This README fills a blank `src/` layout-boundary README under the top-level KHRI compatibility connector."
  - "The KHRI source dossier says canonical KHRI connector work belongs under `connectors/kansas/khri/`; this top-level `src/` path is compatibility-only."
  - "The child package README at `src/khri/README.md` defines the package implementation boundary; this file defines the broader `src/` layout boundary."
  - "This README does not prove package modules, fixtures, tests, endpoint access, or CI wiring exist."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# KHRI Compatibility Source Layout Boundary

> Layout-boundary README for `connectors/khri/src/`. This folder groups implementation package code for the noncanonical KHRI compatibility connector. It is **not** itself a connector, policy root, schema root, release root, public API, fixture authority, or truth store.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Canonicality: noncanonical src path" src="https://img.shields.io/badge/canonicality-noncanonical__src__path-orange">
  <img alt="Network: disabled by default" src="https://img.shields.io/badge/network-disabled__by__default-critical">
  <img alt="Fixtures: required" src="https://img.shields.io/badge/fixtures-required-blue">
  <img alt="Lifecycle: RAW or QUARANTINE only" src="https://img.shields.io/badge/lifecycle-RAW%20%7C%20QUARANTINE%20only-orange">
</p>

> [!IMPORTANT]
> **Status:** `draft` compatibility source-layout README · **Owner:** `OWNER_TBD`  
> **Path:** `connectors/khri/src/README.md`  
> **Truth posture:** `CONFIRMED` file exists · `NONCANONICAL` compatibility src path · `NEEDS VERIFICATION` package inventory and CI wiring  
> **Boundary:** package-layout guidance only; no live-network default, no source activation, no release artifact, no public claim.

**Quick jumps:** [Scope](#scope) · [Repo fit](#repo-fit) · [Allowed contents](#allowed-contents) · [Forbidden contents](#forbidden-contents) · [Expected layout](#expected-layout) · [Evidence ledger](#evidence-ledger) · [Runtime posture](#runtime-posture) · [Validation expectations](#validation-expectations) · [Rollback](#rollback) · [Verification backlog](#verification-backlog)

---

## Scope

`connectors/khri/src/` is the source-layout container for the legacy KHRI compatibility connector.

It may contain package directories, package-level README files, small helper modules, and implementation-boundary docs for source-admission parsing, normalization, validation, source-role preservation, surface-identity preservation, rights-state preservation, review-state preservation, geometry precision preservation, and RAW/QUARANTINE handoff helpers.

It must not become a second connector root, canonical package root, schema root, policy root, source registry, release root, proof root, fixture dump, live harvester, public API, or publication surface.

[Back to top ↑](#top)

---

## Repo fit

| Surface | Role | Status |
|---|---|---:|
| `connectors/khri/src/` | Compatibility source-layout container. | **CONFIRMED path / NEEDS VERIFICATION package inventory** |
| `connectors/khri/src/khri/` | Compatibility package namespace. | **CONFIRMED README path / NEEDS VERIFICATION modules** |
| `connectors/khri/README.md` | Parent compatibility connector README. | **CONFIRMED** |
| `connectors/khri/tests/README.md` | Compatibility-path test contract. | **CONFIRMED** |
| `connectors/kansas/khri/` | Canonical KHRI connector path named by source dossier. | **CONFIRMED by source dossier / NEEDS VERIFICATION implementation depth** |
| `docs/sources/catalog/kansas/khri.md` | KHRI per-surface source dossier. | **CONFIRMED** |
| `docs/sources/catalog/kansas/kansas-state-archives.md` | KSHS umbrella source-family brief. | **CONFIRMED** |
| `release/` | Release and publication controls. | **Out of scope for this source layout** |

[Back to top ↑](#top)

---

## Allowed contents

Allowed content under `src/`:

- package directories such as `khri/`;
- package-level README files;
- source-admission parsing helpers;
- metadata normalization helpers that do not upgrade truth status;
- validation helpers;
- KHRI/KSHS surface-identity helpers;
- source-role helpers;
- inventory/resource identity helpers;
- rights and review-state preservation helpers;
- geometry precision and uncertainty preservation helpers;
- handoff-envelope helpers for RAW or QUARANTINE candidates;
- deterministic error objects for quarantine or abstention;
- compatibility shims that point toward the canonical `connectors/kansas/khri/` lane;
- lightweight test support modules, if they do not contain fixtures better placed under `fixtures/` or `tests/`.

---

## Forbidden contents

Do not place the following under this `src/` layout:

- canonical schemas;
- policy decisions or policy-as-code unless the repo has a clear connector-local policy-helper convention;
- source registry records;
- release manifests;
- proof or receipt authority records;
- public maps, public APIs, public summaries, or published artifacts;
- bulk harvest dumps or fixture corpora;
- credentials, tokens, cookies, session state, or secrets;
- live-source jobs enabled by default;
- code that treats `connectors/khri/` as canonical without ADR or migration evidence.

[Back to top ↑](#top)

---

## Expected layout

Current-session evidence confirms only this README and the child package README. The rest is **PROPOSED** and must be verified before implementation claims.

```text
connectors/khri/src/
├── README.md                       # CONFIRMED — this layout-boundary README
└── khri/
    └── README.md                   # CONFIRMED — package-boundary README
```

Potential package files are documented in `src/khri/README.md`; do not create them merely because they are listed there.

---

## Evidence ledger

| Source | Status | Supports | Limits |
|---|---:|---|---|
| `connectors/khri/src/README.md` | **CONFIRMED** | Target source-layout README exists and was blank before this update. | Does not prove modules, tests, or CI. |
| `connectors/khri/src/khri/README.md` | **CONFIRMED** | Child package README defines package implementation boundary. | Does not prove modules exist. |
| `connectors/khri/README.md` | **CONFIRMED** | Parent path is documented as noncanonical compatibility lane. | Does not prove canonical migration status. |
| `connectors/khri/tests/README.md` | **CONFIRMED** | Test posture is no-network by default, fixture-safe, and source-admission only. | Does not prove tests exist or pass. |
| `docs/sources/catalog/kansas/khri.md` | **CONFIRMED** | KHRI dossier says canonical connector path is `connectors/kansas/khri/` and frames KHRI as a KSHS-operated per-surface product page. | Does not prove endpoint availability, rights clearance, activation, or implementation. |
| `docs/sources/catalog/kansas/kansas-state-archives.md` | **CONFIRMED** | KSHS umbrella brief says umbrella posture does not replace per-surface descriptors. | Does not define source-layout behavior alone. |
| Package/module files below this layout | **NEEDS VERIFICATION** | This README defines expected layout boundaries. | Actual files, behavior, and CI status remain unverified. |

---

## Runtime posture

Code under this layout should default to:

- no network;
- no source activation;
- no public output;
- no release artifact creation;
- no direct writes beyond RAW or QUARANTINE handoff envelopes;
- no credentials or secrets;
- deterministic failure when SourceDescriptor, activation, rights, review state, source role, surface identity, inventory identity, resource type, geometry precision, source shape, or handoff target is unresolved.

---

## Validation expectations

Any implementation under this layout should be paired with tests that check:

- SourceDescriptor and activation preconditions;
- KHRI/KSHS surface identity preservation;
- source-role preservation;
- inventory/resource identity preservation;
- rights and review-state preservation;
- geometry precision and uncertainty preservation;
- fail-closed quarantine or abstention errors;
- RAW/QUARANTINE-only handoff behavior;
- no default network access;
- no release/public artifact emission;
- no canonicality assumption for `connectors/khri/` without ADR or migration evidence.

[Back to top ↑](#top)

---

## Rollback

Rollback is required if this README is used to justify live harvesting, source activation, canonical status, public release, rights/review bypass, source-role collapse, or implementation maturity without verified modules and tests.

Rollback target:

```text
commit prior to this update: SHA_TBD_AFTER_GIT_HISTORY_CHECK
```

Because the file was blank before this update, a safe rollback is to restore the blank placeholder or replace this document with a shorter layout-compatibility note until canonical placement and implementation are verified.

---

## Verification backlog

| Item | Status | Needed evidence |
|---|---:|---|
| Confirm actual `src/` inventory. | **NEEDS VERIFICATION** | Repo tree or mounted workspace. |
| Confirm canonical KHRI source-layout path. | **NEEDS VERIFICATION** | Directory Rules, ADR, migration note, or repo convention. |
| Confirm package/module inventory. | **NEEDS VERIFICATION** | Repo tree and package metadata. |
| Confirm SourceDescriptor and activation gate wiring. | **NEEDS VERIFICATION** | Source registry entry, code, and tests. |
| Confirm rights and review-state handling. | **NEEDS VERIFICATION** | Policy references, code, and tests. |
| Confirm fixture strategy and CI wiring. | **NEEDS VERIFICATION** | Fixture registry, workflow files, and test logs. |

---

## Maintainer note

Keep `src/` boring. It should organize implementation code only. Governance authority belongs in descriptors, policies, schemas, validation receipts, release records, and reviewed docs outside this layout.

[Back to top ↑](#top)
