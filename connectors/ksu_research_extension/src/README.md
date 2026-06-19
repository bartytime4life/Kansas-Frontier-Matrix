<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/connectors-ksu-research-extension-src-readme
title: connectors/ksu_research_extension/src/ — KSU Research and Extension Compatibility Source Layout Boundary
type: readme
version: v0.1
status: draft
owners: OWNER_TBD — Connector steward · Package maintainer · Kansas source steward · Agriculture steward · Weather steward · Soil steward · Rights reviewer · Sensitivity reviewer · Validation steward · Docs steward
created: 2026-06-19
updated: 2026-06-19
policy_label: public-doctrine; src-layout-boundary; compatibility-lane; noncanonical-path; snake-case-compatibility; no-network-default; fixture-safe; rights-gated; sensitivity-gated; no-publication
proposed_path: connectors/ksu_research_extension/src/README.md
truth_posture: CONFIRMED path exists / NONCANONICAL compatibility src README / PACKAGE INVENTORY NEEDS VERIFICATION
related:
  - ../README.md
  - ../tests/README.md
  - ./ksu_research_extension/README.md
  - ../../kansas/README.md
  - ../../kansas/ksu-research-extension/README.md
  - ../../../docs/sources/catalog/kansas/ksu-research-extension.md
  - ../../../docs/sources/catalog/kansas/kansas-mesonet.md
  - ../../../docs/domains/agriculture/README.md
  - ../../../docs/domains/weather-atmospheric/README.md
  - ../../../docs/domains/soil/README.md
  - ../../../docs/sources/SOURCE_DESCRIPTOR_STANDARD.md
  - ../../../data/registry/sources/
  - ../../../fixtures/
  - ../../../schemas/contracts/v1/source/
  - ../../../policy/sensitivity/
  - ../../../policy/rights/
  - ../../../release/
tags: [kfm, connectors, ksu, k-state, research-extension, src, package-layout, agriculture, weather, soil, compatibility, source-admission, no-network, raw, quarantine, governance]
notes:
  - "This README fills a blank `src/` layout-boundary README under the top-level KSU R&E compatibility connector."
  - "The KSU R&E source profile says v0.2 normalizes canonical connector placement to `connectors/kansas/ksu-research-extension/`."
  - "The child package README at `src/ksu_research_extension/README.md` defines the package implementation boundary; this file defines the broader `src/` layout boundary."
  - "This README does not prove package modules, fixtures, tests, endpoint access, or CI wiring exist."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# KSU Research and Extension Compatibility Source Layout Boundary

> Layout-boundary README for `connectors/ksu_research_extension/src/`. This folder groups implementation package code for the noncanonical KSU Research and Extension compatibility connector. It is **not** itself a connector, policy root, schema root, release root, public API, fixture authority, or truth store.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Canonicality: noncanonical src path" src="https://img.shields.io/badge/canonicality-noncanonical__src__path-orange">
  <img alt="Network: disabled by default" src="https://img.shields.io/badge/network-disabled__by__default-critical">
  <img alt="Fixtures: required" src="https://img.shields.io/badge/fixtures-required-blue">
  <img alt="Lifecycle: RAW or QUARANTINE only" src="https://img.shields.io/badge/lifecycle-RAW%20%7C%20QUARANTINE%20only-orange">
</p>

> [!IMPORTANT]
> **Status:** `draft` compatibility source-layout README · **Owner:** `OWNER_TBD`  
> **Path:** `connectors/ksu_research_extension/src/README.md`  
> **Truth posture:** `CONFIRMED` file exists · `NONCANONICAL` compatibility src path · `NEEDS VERIFICATION` package inventory and CI wiring  
> **Boundary:** package-layout guidance only; no live-network default, no source activation, no release artifact, no public claim.

**Quick jumps:** [Scope](#scope) · [Repo fit](#repo-fit) · [Allowed contents](#allowed-contents) · [Forbidden contents](#forbidden-contents) · [Expected layout](#expected-layout) · [Evidence ledger](#evidence-ledger) · [Runtime posture](#runtime-posture) · [Validation expectations](#validation-expectations) · [Rollback](#rollback) · [Verification backlog](#verification-backlog)

---

## Scope

`connectors/ksu_research_extension/src/` is the source-layout container for the legacy KSU R&E compatibility connector.

It may contain package directories, package-level README files, small helper modules, and implementation-boundary docs for source-admission parsing, normalization, validation, source-role preservation, product identity preservation, umbrella-versus-surface separation, rights-state preservation, review-state preservation, cadence/freshness preservation, and RAW/QUARANTINE handoff helpers.

It must not become a second connector root, canonical package root, schema root, policy root, source registry, release root, proof root, fixture dump, live harvester, public API, or publication surface.

[Back to top ↑](#top)

---

## Repo fit

| Surface | Role | Status |
|---|---|---:|
| `connectors/ksu_research_extension/src/` | Compatibility source-layout container. | **CONFIRMED path / NEEDS VERIFICATION package inventory** |
| `connectors/ksu_research_extension/src/ksu_research_extension/` | Compatibility package namespace. | **CONFIRMED README path / NEEDS VERIFICATION modules** |
| `connectors/ksu_research_extension/README.md` | Parent compatibility connector README. | **CONFIRMED** |
| `connectors/ksu_research_extension/tests/README.md` | Compatibility-path test contract. | **CONFIRMED** |
| `connectors/kansas/ksu-research-extension/` | Canonical KSU R&E connector path named by source profile. | **CONFIRMED by source profile / NEEDS VERIFICATION implementation depth** |
| `docs/sources/catalog/kansas/ksu-research-extension.md` | KSU R&E umbrella source profile. | **CONFIRMED** |
| `docs/sources/catalog/kansas/kansas-mesonet.md` | Kansas Mesonet sibling per-surface product page. | **CONFIRMED** |
| `release/` | Release and publication controls. | **Out of scope for this source layout** |

[Back to top ↑](#top)

---

## Allowed contents

Allowed content under `src/`:

- package directories such as `ksu_research_extension/`;
- package-level README files;
- source-admission parsing helpers;
- metadata normalization helpers that do not upgrade truth status;
- validation helpers;
- snake_case compatibility helpers;
- source-role helpers;
- product identity helpers;
- umbrella-versus-surface separation helpers;
- rights and review-state preservation helpers;
- cadence and freshness preservation helpers;
- handoff-envelope helpers for RAW or QUARANTINE candidates;
- deterministic error objects for quarantine or abstention;
- compatibility shims that point toward the canonical `connectors/kansas/ksu-research-extension/` lane;
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
- bulk source dumps or fixture corpora;
- credentials, tokens, cookies, session state, or secrets;
- live-source jobs enabled by default;
- code that treats `connectors/ksu_research_extension/` as canonical without ADR or migration evidence.

[Back to top ↑](#top)

---

## Expected layout

Current-session evidence confirms only this README and the child package README. The rest is **PROPOSED** and must be verified before implementation claims.

```text
connectors/ksu_research_extension/src/
├── README.md                       # CONFIRMED — this layout-boundary README
└── ksu_research_extension/
    └── README.md                   # CONFIRMED — package-boundary README
```

Potential package files are documented in `src/ksu_research_extension/README.md`; do not create them merely because they are listed there.

---

## Evidence ledger

| Source | Status | Supports | Limits |
|---|---:|---|---|
| `connectors/ksu_research_extension/src/README.md` | **CONFIRMED** | Target source-layout README exists and was blank before this update. | Does not prove modules, tests, or CI. |
| `connectors/ksu_research_extension/src/ksu_research_extension/README.md` | **CONFIRMED** | Child package README defines package implementation boundary. | Does not prove modules exist. |
| `connectors/ksu_research_extension/README.md` | **CONFIRMED** | Parent path is documented as noncanonical snake_case compatibility lane. | Does not prove canonical migration status. |
| `connectors/ksu_research_extension/tests/README.md` | **CONFIRMED** | Test posture is no-network by default, fixture-safe, and source-admission only. | Does not prove tests exist or pass. |
| `docs/sources/catalog/kansas/ksu-research-extension.md` | **CONFIRMED** | Source profile says v0.2 normalizes canonical connector placement to `connectors/kansas/ksu-research-extension/` and frames KSU R&E as an umbrella source brief. | Does not prove endpoint availability, rights clearance, activation, or implementation. |
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
- deterministic failure when SourceDescriptor, activation, rights, review state, source role, product identity, cadence/freshness, source shape, or handoff target is unresolved.

---

## Validation expectations

Any implementation under this layout should be paired with tests that check:

- SourceDescriptor and activation preconditions;
- snake_case compatibility versus canonical kebab-case path separation;
- KSU R&E umbrella versus per-surface product separation;
- source-role preservation;
- product identity preservation;
- rights and review-state preservation;
- cadence and freshness preservation;
- fail-closed quarantine or abstention errors;
- RAW/QUARANTINE-only handoff behavior;
- no default network access;
- no release/public artifact emission;
- no canonicality assumption for `connectors/ksu_research_extension/` without ADR or migration evidence.

[Back to top ↑](#top)

---

## Rollback

Rollback is required if this README is used to justify live harvesting, source activation, canonical status, public release, rights/review bypass, source-role collapse, umbrella/surface collapse, or implementation maturity without verified modules and tests.

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
| Confirm canonical KSU R&E source-layout path. | **NEEDS VERIFICATION** | Directory Rules, ADR, migration note, or repo convention. |
| Confirm package/module inventory. | **NEEDS VERIFICATION** | Repo tree and package metadata. |
| Confirm SourceDescriptor and activation gate wiring. | **NEEDS VERIFICATION** | Source registry entry, code, and tests. |
| Confirm rights and review-state handling. | **NEEDS VERIFICATION** | Policy references, code, and tests. |
| Confirm fixture strategy and CI wiring. | **NEEDS VERIFICATION** | Fixture registry, workflow files, and test logs. |

---

## Maintainer note

Keep `src/` boring. It should organize implementation code only. Governance authority belongs in descriptors, policies, schemas, validation receipts, release records, and reviewed docs outside this layout.

[Back to top ↑](#top)
