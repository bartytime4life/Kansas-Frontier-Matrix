<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/connectors-local-upload-src-readme
title: connectors/local_upload/src/ — Local Upload Source Layout Boundary
type: readme
version: v0.1
status: draft
owners: OWNER_TBD — Connector steward · Package maintainer · Source-intake steward · Rights reviewer · Sensitivity reviewer · Validation steward · Docs steward
created: 2026-06-19
updated: 2026-06-19
policy_label: public-doctrine; src-layout-boundary; connector-family; directory-rules-7-3; local-upload; no-network-default; fixture-safe; deny-by-default; quarantine-first; no-publication
proposed_path: connectors/local_upload/src/README.md
truth_posture: CONFIRMED path exists / CONFIRMED doctrine-level §7.3 connector-family src path / PACKAGE INVENTORY NEEDS VERIFICATION
related:
  - ../README.md
  - ../tests/README.md
  - ./local_upload/README.md
  - ../../../docs/sources/catalog/local_upload/README.md
  - ../../../docs/sources/catalog/local_upload.md
  - ../../../docs/sources/catalog/local_upload/user-file-upload.md
  - ../../../docs/sources/SOURCE_DESCRIPTOR_STANDARD.md
  - ../../../docs/doctrine/directory-rules.md
  - ../../../docs/doctrine/trust-membrane.md
  - ../../../docs/doctrine/lifecycle-law.md
  - ../../../docs/adr/ADR-0012-connector-outputs-to-data-raw-or-data-quarantine-only.md
  - ../../../data/registry/sources/
  - ../../../data/raw/
  - ../../../data/quarantine/
  - ../../../fixtures/
  - ../../../schemas/contracts/v1/source/
  - ../../../policy/sources/local_upload/
  - ../../../policy/sensitivity/
  - ../../../policy/rights/
  - ../../../release/
tags: [kfm, connectors, local-upload, local_upload, src, package-layout, intake, source-admission, descriptor, validation, raw, quarantine, rights, sensitivity, provenance, governance]
notes:
  - "This README fills a blank `src/` layout-boundary README under the canonical local-upload connector family."
  - "The child package README at `src/local_upload/README.md` defines the package implementation boundary; this file defines the broader `src/` layout boundary."
  - "This README does not prove package modules, fixtures, tests, endpoint access, or CI wiring exist."
  - "Code under this layout may only support governed source-admission helpers and RAW/QUARANTINE handoff; policy and release decisions remain outside this layout."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Local Upload Source Layout Boundary

> Layout-boundary README for `connectors/local_upload/src/`. This folder groups implementation package code for the local-upload connector family. It is **not** itself a connector, policy root, schema root, source registry, release root, public API, fixture authority, proof authority, or truth store.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Directory Rules: §7.3 connector" src="https://img.shields.io/badge/directory__rules-%C2%A77.3__connector-success">
  <img alt="Policy: deny by default" src="https://img.shields.io/badge/policy-deny__by__default-red">
  <img alt="Lifecycle: RAW or QUARANTINE only" src="https://img.shields.io/badge/lifecycle-RAW%20%7C%20QUARANTINE%20only-orange">
</p>

> [!IMPORTANT]
> **Status:** `draft` source-layout README · **Owner:** `OWNER_TBD`  
> **Path:** `connectors/local_upload/src/README.md`  
> **Truth posture:** `CONFIRMED` file exists · `CONFIRMED` doctrine-level §7.3 connector-family src path · `NEEDS VERIFICATION` package inventory and CI wiring  
> **Boundary:** package-layout guidance only; no source-role upgrade, no release artifact, no public claim.

**Quick jumps:** [Scope](#scope) · [Repo fit](#repo-fit) · [Allowed contents](#allowed-contents) · [Forbidden contents](#forbidden-contents) · [Expected layout](#expected-layout) · [Evidence ledger](#evidence-ledger) · [Runtime posture](#runtime-posture) · [Validation expectations](#validation-expectations) · [Rollback](#rollback) · [Verification backlog](#verification-backlog)

---

## Scope

`connectors/local_upload/src/` is the source-layout container for the local-upload connector implementation package.

It may contain package directories, package-level README files, small helper modules, and implementation-boundary docs for upload-event metadata, candidate descriptor preparation, file-shape inspection, content fingerprint preservation, validation, quarantine disposition, and RAW/QUARANTINE handoff helpers.

It must not become a second connector root, canonical package root, schema root, policy root, source registry, release root, proof root, fixture dump, public API, or publication surface.

[Back to top ↑](#top)

---

## Repo fit

| Surface | Role | Status |
|---|---|---:|
| `connectors/local_upload/src/` | Local-upload source-layout container. | **CONFIRMED path / NEEDS VERIFICATION package inventory** |
| `connectors/local_upload/src/local_upload/` | Local-upload package namespace. | **CONFIRMED README path / NEEDS VERIFICATION modules** |
| `connectors/local_upload/README.md` | Parent local-upload connector README. | **CONFIRMED** |
| `connectors/local_upload/tests/README.md` | Local-upload test-boundary README. | **CONFIRMED** |
| `docs/sources/catalog/local_upload/README.md` | Human-facing source catalog entry for local uploads. | **CONFIRMED** |
| `data/registry/sources/` | SourceDescriptor authority. | **Outside layout / NEEDS VERIFICATION for entries** |
| `data/raw/` and `data/quarantine/` | Allowed handoff targets. | **Outside layout** |
| `release/` | Release and publication controls. | **Out of scope for this layout** |

---

## Allowed contents

Allowed content under `src/`:

- package directories such as `local_upload/`;
- package-level README files;
- source-admission parsing helpers;
- upload-event metadata helpers;
- candidate SourceDescriptor preparation helpers;
- content fingerprint helpers;
- content and metadata inspection helpers;
- candidate source-role preservation helpers;
- rights and sensitivity state preservation helpers;
- provenance and review-state preservation helpers;
- quarantine disposition helpers;
- RAW or QUARANTINE handoff-envelope helpers;
- deterministic fail-closed errors;
- lightweight test support modules that do not duplicate `fixtures/` or `tests/` responsibilities.

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
- code that upgrades source role, rights, sensitivity, or release state by convenience.

---

## Expected layout

Current-session evidence confirms only this README and the child package README. The rest is **PROPOSED** and must be verified before implementation claims.

```text
connectors/local_upload/src/
├── README.md                       # CONFIRMED — this layout-boundary README
└── local_upload/
    └── README.md                   # CONFIRMED — package-boundary README
```

Potential package files are documented in `src/local_upload/README.md`; do not create them merely because they are listed there.

---

## Evidence ledger

| Source | Status | Supports | Limits |
|---|---:|---|---|
| `connectors/local_upload/src/README.md` | **CONFIRMED** | Target source-layout README exists and was blank before this update. | Does not prove modules, tests, or CI. |
| `connectors/local_upload/src/local_upload/README.md` | **CONFIRMED** | Child package README defines package implementation boundary. | Does not prove modules exist. |
| `connectors/local_upload/README.md` | **CONFIRMED** | Parent path is documented as a §7.3 local-upload connector family. | Does not prove implementation maturity. |
| `connectors/local_upload/tests/README.md` | **CONFIRMED** | Test posture is no-network by default, fixture-safe, and source-admission only. | Does not prove tests exist or pass. |
| `docs/sources/catalog/local_upload/README.md` | **CONFIRMED** | Catalog defines local upload as a high-uncertainty trust-edge intake lane with RAW/QUARANTINE handling. | Does not prove endpoint, fixture, or code coverage. |
| Package/module files below this layout | **NEEDS VERIFICATION** | This README defines expected layout boundaries. | Actual files, behavior, and CI status remain unverified. |

---

## Runtime posture

Code under this layout should default to:

- no publication;
- no source activation decision;
- no source-role upgrade;
- no public output;
- no direct writes beyond RAW or QUARANTINE handoff envelopes;
- deterministic failure when descriptor, rights state, sensitivity state, source role, provenance, or disposition is unresolved.

---

## Validation expectations

Any implementation under this layout should be paired with tests that check:

- upload event metadata preservation;
- source fingerprint preservation;
- SourceDescriptor preparation;
- candidate source-role preservation;
- rights and sensitivity state preservation;
- provenance and review-state preservation;
- quarantine reason preservation;
- RAW/QUARANTINE-only handoff behavior;
- no release/public artifact emission;
- no source-role upgrade by convenience.

---

## Rollback

Rollback is required if this README is used to justify source activation, source-role upgrade, public release, rights/sensitivity bypass, direct publication, or implementation maturity without verified modules and tests.

Rollback target:

```text
commit prior to this update: SHA_TBD_AFTER_GIT_HISTORY_CHECK
```

Because the file was blank before this update, a safe rollback is to restore the blank placeholder or replace this document with a shorter layout-boundary note until implementation files and tests are verified.

---

## Verification backlog

| Item | Status | Needed evidence |
|---|---:|---|
| Confirm actual `src/` inventory. | **NEEDS VERIFICATION** | Repo tree or mounted workspace. |
| Confirm package/module inventory. | **NEEDS VERIFICATION** | Repo tree and package metadata. |
| Confirm SourceDescriptor and candidate-role handling. | **NEEDS VERIFICATION** | Source registry entry, code, and tests. |
| Confirm rights/sensitivity/review-state handling. | **NEEDS VERIFICATION** | Policy references, code, and tests. |
| Confirm RAW/QUARANTINE handoff envelope shape. | **NEEDS VERIFICATION** | Schemas/contracts and tests. |
| Confirm fixture strategy and CI wiring. | **NEEDS VERIFICATION** | Fixture registry, workflow files, and test logs. |

---

## Maintainer note

Keep `src/` boring. It should organize implementation code only. Governance authority belongs in descriptors, policies, schemas, validation receipts, release records, and reviewed docs outside this layout.

[Back to top ↑](#top)
