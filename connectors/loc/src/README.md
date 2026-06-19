<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/connectors-loc-src-readme
title: connectors/loc/src/ — Library of Congress Connector Candidate Source Layout Boundary
type: readme
version: v0.1
status: draft
owners: OWNER_TBD — Connector steward · Package maintainer · Source steward for LOC · Rights reviewer · Validation steward · Docs steward
created: 2026-06-19
updated: 2026-06-19
policy_label: public-doctrine; src-layout-boundary; connector-family-candidate; beyond-directory-rules-7-3; open-dsc-14; no-network-default; fixture-safe; no-publication
proposed_path: connectors/loc/src/README.md
truth_posture: CONFIRMED path exists / PROPOSED beyond §7.3 connector-family src path / PACKAGE INVENTORY NEEDS VERIFICATION
related:
  - ../README.md
  - ../tests/README.md
  - ./loc/README.md
  - ../../../docs/sources/catalog/loc/README.md
  - ../../../docs/sources/SOURCE_DESCRIPTOR_STANDARD.md
  - ../../../data/registry/sources/
  - ../../../fixtures/
  - ../../../schemas/contracts/v1/source/
  - ../../../policy/rights/
  - ../../../policy/sources/
  - ../../../release/
tags: [kfm, connectors, loc, library-of-congress, src, package-layout, source-admission, open-dsc-14, no-network, raw, quarantine, governance]
notes:
  - "This README fills a blank `src/` layout-boundary README under the proposed LOC connector-family candidate."
  - "The LOC catalog README says `connectors/loc/` is proposed beyond Directory Rules §7.3 and awaits OPEN-DSC-14 ADR ratification."
  - "The child package README at `src/loc/README.md` defines the package implementation boundary; this file defines the broader `src/` layout boundary."
  - "This README does not prove package modules, fixtures, tests, endpoint access, or CI wiring exist."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Library of Congress Connector Candidate Source Layout Boundary

> Layout-boundary README for `connectors/loc/src/`. This folder groups implementation package code for the proposed LOC connector-family candidate. It is **not** itself a connector, policy root, schema root, source registry, release root, public API, fixture authority, proof authority, or truth store.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Family status: beyond §7.3" src="https://img.shields.io/badge/family-beyond__%C2%A77.3-orange">
  <img alt="Open item: OPEN-DSC-14" src="https://img.shields.io/badge/open-OPEN--DSC--14-orange">
  <img alt="Network: disabled by default" src="https://img.shields.io/badge/network-disabled__by__default-critical">
  <img alt="Lifecycle: RAW or QUARANTINE only" src="https://img.shields.io/badge/lifecycle-RAW%20%7C%20QUARANTINE%20only-orange">
</p>

> [!IMPORTANT]
> **Status:** `draft` connector-candidate source-layout README · **Owner:** `OWNER_TBD`  
> **Path:** `connectors/loc/src/README.md`  
> **Truth posture:** `CONFIRMED` file exists · `PROPOSED` beyond §7.3 src path · `NEEDS VERIFICATION` package inventory and CI wiring  
> **Boundary:** package-layout guidance only; no live-network default, no source activation, no release artifact, no canonical-family claim.

**Quick jumps:** [Scope](#scope) · [Repo fit](#repo-fit) · [Allowed contents](#allowed-contents) · [Forbidden contents](#forbidden-contents) · [Expected layout](#expected-layout) · [Evidence ledger](#evidence-ledger) · [Runtime posture](#runtime-posture) · [Validation expectations](#validation-expectations) · [Rollback](#rollback) · [Verification backlog](#verification-backlog)

---

## Scope

`connectors/loc/src/` is the source-layout container for the proposed Library of Congress connector-family candidate.

It may contain package directories, package-level README files, small helper modules, and implementation-boundary docs for source-admission parsing, normalization, validation, source-role preservation, source-surface identity preservation, rights-state preservation, provenance preservation, source fingerprint preservation, uncertainty preservation, and RAW/QUARANTINE handoff helpers.

It must not become a second connector root, canonical package root, schema root, policy root, source registry, release root, proof root, fixture dump, live harvester, public API, or publication surface.

[Back to top ↑](#top)

---

## Repo fit

| Surface | Role | Status |
|---|---|---:|
| `connectors/loc/src/` | LOC connector-candidate source-layout container. | **CONFIRMED path / NEEDS VERIFICATION package inventory** |
| `connectors/loc/src/loc/` | LOC connector-candidate package namespace. | **CONFIRMED README path / NEEDS VERIFICATION modules** |
| `connectors/loc/README.md` | Parent LOC connector-family candidate README. | **CONFIRMED** |
| `connectors/loc/tests/README.md` | LOC candidate-family test contract. | **CONFIRMED** |
| `docs/sources/catalog/loc/README.md` | LOC source-family catalog README. | **CONFIRMED** |
| `release/` | Release and publication controls. | **Out of scope for this source layout** |

---

## Allowed contents

Allowed content under `src/`:

- package directories such as `loc/`;
- package-level README files;
- source-admission parsing helpers;
- metadata normalization helpers that do not upgrade truth status;
- validation helpers;
- LOC source-surface identity helpers;
- source-role helpers;
- source URI and retrieval timestamp preservation helpers;
- source fingerprint helpers;
- rights and provenance preservation helpers;
- uncertainty metadata helpers;
- handoff-envelope helpers for RAW or QUARANTINE candidates;
- deterministic error objects for quarantine or abstention;
- compatibility shims that keep `connectors/loc/` marked as proposed until `OPEN-DSC-14` is resolved.

---

## Forbidden contents

Do not place the following under this `src/` layout:

- canonical schemas;
- policy decisions;
- source registry records;
- release manifests;
- proof or receipt authority records;
- public maps, public APIs, public summaries, or published artifacts;
- bulk source dumps or fixture corpora;
- live-source jobs enabled by default;
- code that treats `connectors/loc/` as canonical without ADR or migration evidence.

---

## Expected layout

Current-session evidence confirms only this README and the child package README. The rest is **PROPOSED** and must be verified before implementation claims.

```text
connectors/loc/src/
├── README.md                       # CONFIRMED — this layout-boundary README
└── loc/
    └── README.md                   # CONFIRMED — package-boundary README
```

Potential package files are documented in `src/loc/README.md`; do not create them merely because they are listed there.

---

## Evidence ledger

| Source | Status | Supports | Limits |
|---|---:|---|---|
| `connectors/loc/src/README.md` | **CONFIRMED** | Target source-layout README exists and was blank before this update. | Does not prove modules, tests, or CI. |
| `connectors/loc/src/loc/README.md` | **CONFIRMED** | Child package README defines package implementation boundary. | Does not prove modules exist. |
| `connectors/loc/README.md` | **CONFIRMED** | Parent path is documented as proposed beyond §7.3 under OPEN-DSC-14. | Does not prove ADR resolution or implementation maturity. |
| `connectors/loc/tests/README.md` | **CONFIRMED** | Test posture is no-network by default, fixture-safe, and source-admission only. | Does not prove tests exist or pass. |
| `docs/sources/catalog/loc/README.md` | **CONFIRMED** | LOC catalog README says `connectors/loc/` is proposed beyond §7.3. | Does not prove endpoint availability, rights clearance, activation, or implementation. |
| Package/module files below this layout | **NEEDS VERIFICATION** | This README defines expected layout boundaries. | Actual files, behavior, and CI status remain unverified. |

---

## Runtime posture

Code under this layout should default to:

- no network;
- no source activation;
- no public output;
- no release artifact creation;
- no direct writes beyond RAW or QUARANTINE handoff envelopes;
- deterministic failure when SourceDescriptor, activation, rights state, source role, source-surface identity, provenance, uncertainty, source shape, or handoff target is unresolved.

---

## Validation expectations

Any implementation under this layout should be paired with tests that check:

- SourceDescriptor and activation preconditions;
- candidate-family status under `OPEN-DSC-14`;
- LOC source-surface identity preservation;
- source-role preservation;
- source URI and retrieval timestamp preservation;
- source fingerprint preservation where applicable;
- rights and provenance preservation;
- uncertainty metadata preservation;
- fail-closed quarantine or abstention errors;
- RAW/QUARANTINE-only handoff behavior;
- no default network access;
- no release/public artifact emission;
- no canonicality assumption for `connectors/loc/` without ADR or migration evidence.

---

## Rollback

Rollback is required if this README is used to justify live harvesting, source activation, canonical-family status, public release, rights/provenance bypass, source-surface collapse, or implementation maturity without verified modules and tests.

Rollback target:

```text
commit prior to this update: SHA_TBD_AFTER_GIT_HISTORY_CHECK
```

Because the file was blank before this update, a safe rollback is to restore the blank placeholder or replace this document with a shorter layout-candidate note until `OPEN-DSC-14` and implementation are verified.

---

## Verification backlog

| Item | Status | Needed evidence |
|---|---:|---|
| Confirm actual `src/` inventory. | **NEEDS VERIFICATION** | Repo tree or mounted workspace. |
| Resolve `OPEN-DSC-14` for LOC connector-family placement. | **NEEDS VERIFICATION** | ADR or migration decision. |
| Confirm package/module inventory. | **NEEDS VERIFICATION** | Repo tree and package metadata. |
| Confirm SourceDescriptor and activation gate wiring. | **NEEDS VERIFICATION** | Source registry entry, code, and tests. |
| Confirm rights and provenance handling. | **NEEDS VERIFICATION** | Policy references, code, and tests. |
| Confirm fixture strategy and CI wiring. | **NEEDS VERIFICATION** | Fixture registry, workflow files, and test logs. |

---

## Maintainer note

Keep `src/` boring. It should organize implementation code only. Governance authority belongs in descriptors, policies, schemas, validation receipts, release records, and reviewed docs outside this layout.

[Back to top ↑](#top)
