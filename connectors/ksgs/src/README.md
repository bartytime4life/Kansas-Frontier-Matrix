<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/connectors-ksgs-src-readme
title: connectors/ksgs/src/ — KSGS Slug Compatibility Source Layout Boundary
type: readme
version: v0.1
status: draft
owners: OWNER_TBD — Connector steward · Package maintainer · Kansas source steward · Geology steward · Hydrology steward · Rights reviewer · Sensitivity reviewer · Validation steward · Docs steward
created: 2026-06-19
updated: 2026-06-19
policy_label: public-doctrine; src-layout-boundary; compatibility-lane; noncanonical-path; slug-compatibility; no-network-default; fixture-safe; rights-gated; sensitivity-gated; no-publication
proposed_path: connectors/ksgs/src/README.md
truth_posture: CONFIRMED path exists / NONCANONICAL compatibility src README / PACKAGE INVENTORY NEEDS VERIFICATION
related:
  - ../README.md
  - ../tests/README.md
  - ./ksgs/README.md
  - ../../kgs/README.md
  - ../../kansas/README.md
  - ../../kansas/kgs/README.md
  - ../../../docs/sources/catalog/kansas/ksgs.md
  - ../../../docs/domains/geology/README.md
  - ../../../docs/domains/hydrology/README.md
  - ../../../docs/sources/SOURCE_DESCRIPTOR_STANDARD.md
  - ../../../data/registry/sources/
  - ../../../fixtures/
  - ../../../schemas/contracts/v1/source/
  - ../../../policy/sensitivity/
  - ../../../policy/rights/
  - ../../../release/
tags: [kfm, connectors, ksgs, kgs, src, package-layout, geology, hydrology, slug-compatibility, source-admission, no-network, raw, quarantine, governance]
notes:
  - "This README fills a blank `src/` layout-boundary README under the top-level KSGS slug-compatibility connector."
  - "The KGS source profile preserves the `ksgs.md` catalog slug while canonical connector work belongs under `connectors/kansas/kgs/`."
  - "The child package README at `src/ksgs/README.md` defines the package implementation boundary; this file defines the broader `src/` layout boundary."
  - "This README does not prove package modules, fixtures, tests, endpoint access, or CI wiring exist."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# KSGS Slug Compatibility Source Layout Boundary

> Layout-boundary README for `connectors/ksgs/src/`. This folder groups implementation package code for the noncanonical KSGS slug-compatibility connector. It is **not** itself a connector, policy root, schema root, release root, public API, fixture authority, or truth store.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Canonicality: noncanonical src path" src="https://img.shields.io/badge/canonicality-noncanonical__src__path-orange">
  <img alt="Slug: ksgs preserved" src="https://img.shields.io/badge/slug-ksgs__preserved-blue">
  <img alt="Network: disabled by default" src="https://img.shields.io/badge/network-disabled__by__default-critical">
  <img alt="Fixtures: required" src="https://img.shields.io/badge/fixtures-required-blue">
</p>

> [!IMPORTANT]
> **Status:** `draft` compatibility source-layout README · **Owner:** `OWNER_TBD`  
> **Path:** `connectors/ksgs/src/README.md`  
> **Truth posture:** `CONFIRMED` file exists · `NONCANONICAL` compatibility src path · `NEEDS VERIFICATION` package inventory and CI wiring  
> **Boundary:** package-layout guidance only; no live-network default, no source activation, no release artifact, no public claim.

**Quick jumps:** [Scope](#scope) · [Repo fit](#repo-fit) · [Allowed contents](#allowed-contents) · [Forbidden contents](#forbidden-contents) · [Expected layout](#expected-layout) · [Evidence ledger](#evidence-ledger) · [Runtime posture](#runtime-posture) · [Validation expectations](#validation-expectations) · [Rollback](#rollback) · [Verification backlog](#verification-backlog)

---

## Scope

`connectors/ksgs/src/` is the source-layout container for the legacy KSGS slug-compatibility connector.

It may contain package directories, package-level README files, small helper modules, and implementation-boundary docs for source-admission parsing, normalization, validation, source-role preservation, KGS sub-product identity preservation, rights-state preservation, review-state preservation, geometry/scale/depth preservation, and RAW/QUARANTINE handoff helpers.

It must not become a second connector root, canonical package root, schema root, policy root, source registry, release root, proof root, fixture dump, live harvester, public API, or publication surface.

[Back to top ↑](#top)

---

## Repo fit

| Surface | Role | Status |
|---|---|---:|
| `connectors/ksgs/src/` | Compatibility source-layout container. | **CONFIRMED path / NEEDS VERIFICATION package inventory** |
| `connectors/ksgs/src/ksgs/` | Compatibility package namespace. | **CONFIRMED README path / NEEDS VERIFICATION modules** |
| `connectors/ksgs/README.md` | Parent slug-compatibility connector README. | **CONFIRMED** |
| `connectors/ksgs/tests/README.md` | Compatibility-path test contract. | **CONFIRMED** |
| `connectors/kgs/README.md` | Sibling top-level KGS compatibility README. | **CONFIRMED** |
| `connectors/kansas/kgs/` | Canonical KGS connector path named by source profile. | **CONFIRMED by source profile / NEEDS VERIFICATION implementation depth** |
| `docs/sources/catalog/kansas/ksgs.md` | KGS source catalog entry using preserved slug. | **CONFIRMED** |
| `release/` | Release and publication controls. | **Out of scope for this source layout** |

[Back to top ↑](#top)

---

## Allowed contents

Allowed content under `src/`:

- package directories such as `ksgs/`;
- package-level README files;
- source-admission parsing helpers;
- metadata normalization helpers that do not upgrade truth status;
- validation helpers;
- `ksgs` slug compatibility helpers;
- source-role helpers;
- KGS sub-product identity helpers;
- rights and review-state preservation helpers;
- geometry, scale, depth, or datum context preservation helpers;
- handoff-envelope helpers for RAW or QUARANTINE candidates;
- deterministic error objects for quarantine or abstention;
- compatibility shims that point toward the canonical `connectors/kansas/kgs/` lane;
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
- code that treats `connectors/ksgs/` as canonical without ADR or migration evidence.

[Back to top ↑](#top)

---

## Expected layout

Current-session evidence confirms only this README and the child package README. The rest is **PROPOSED** and must be verified before implementation claims.

```text
connectors/ksgs/src/
├── README.md                       # CONFIRMED — this layout-boundary README
└── ksgs/
    └── README.md                   # CONFIRMED — package-boundary README
```

Potential package files are documented in `src/ksgs/README.md`; do not create them merely because they are listed there.

---

## Evidence ledger

| Source | Status | Supports | Limits |
|---|---:|---|---|
| `connectors/ksgs/src/README.md` | **CONFIRMED** | Target source-layout README exists and was blank before this update. | Does not prove modules, tests, or CI. |
| `connectors/ksgs/src/ksgs/README.md` | **CONFIRMED** | Child package README defines package implementation boundary. | Does not prove modules exist. |
| `connectors/ksgs/README.md` | **CONFIRMED** | Parent path is documented as noncanonical slug-compatibility lane. | Does not prove canonical migration status. |
| `connectors/ksgs/tests/README.md` | **CONFIRMED** | Test posture is no-network by default, fixture-safe, and source-admission only. | Does not prove tests exist or pass. |
| `docs/sources/catalog/kansas/ksgs.md` | **CONFIRMED** | KGS source profile preserves the `ksgs` slug, confirms canonical connector path `connectors/kansas/kgs/`, and defers slug reconciliation to OPEN-KSGS-13. | Does not prove endpoint availability, rights clearance, activation, or implementation. |
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
- deterministic failure when SourceDescriptor, activation, rights, review state, source role, sub-product identity, geometry/scale/depth context, source shape, or handoff target is unresolved.

---

## Validation expectations

Any implementation under this layout should be paired with tests that check:

- SourceDescriptor and activation preconditions;
- `ksgs` slug versus canonical `kgs/` path separation;
- source-role preservation;
- KGS sub-product identity preservation;
- rights and review-state preservation;
- geometry, scale, depth, or datum context preservation;
- fail-closed quarantine or abstention errors;
- RAW/QUARANTINE-only handoff behavior;
- no default network access;
- no release/public artifact emission;
- no canonicality assumption for `connectors/ksgs/` without ADR or migration evidence.

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
| Confirm canonical KGS source-layout path. | **NEEDS VERIFICATION** | Directory Rules, ADR, migration note, or repo convention. |
| Confirm package/module inventory. | **NEEDS VERIFICATION** | Repo tree and package metadata. |
| Confirm SourceDescriptor and activation gate wiring. | **NEEDS VERIFICATION** | Source registry entry, code, and tests. |
| Resolve or retain `ksgs.md` versus `kgs/` slug discrepancy. | **NEEDS VERIFICATION** | OPEN-KSGS-13, ADR, or repo convention. |
| Confirm rights and review-state handling. | **NEEDS VERIFICATION** | Policy references, code, and tests. |
| Confirm fixture strategy and CI wiring. | **NEEDS VERIFICATION** | Fixture registry, workflow files, and test logs. |

---

## Maintainer note

Keep `src/` boring. It should organize implementation code only. Governance authority belongs in descriptors, policies, schemas, validation receipts, release records, and reviewed docs outside this layout.

[Back to top ↑](#top)
