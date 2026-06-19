<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/connectors-kansas-memory-src-readme
title: connectors/kansas_memory/src/ — Kansas Memory Compatibility Source Layout Boundary
type: readme
version: v0.1
status: draft
owners: OWNER_TBD — Connector steward · Kansas source steward · Archives steward · Package maintainer · Test steward · Validation steward · Docs steward
created: 2026-06-19
updated: 2026-06-19
policy_label: public-doctrine; src-layout-boundary; compatibility-lane; no-network-default; no-publication
proposed_path: connectors/kansas_memory/src/README.md
truth_posture: CONFIRMED path exists / NONCANONICAL compatibility src README / PACKAGE INVENTORY NEEDS VERIFICATION
related:
  - ../README.md
  - ../tests/README.md
  - ./kansas_memory/README.md
  - ../../kansas/README.md
  - ../../kansas/kansas-memory/README.md
  - ../../../docs/sources/catalog/kansas/kansas-memory.md
  - ../../../docs/sources/SOURCE_DESCRIPTOR_STANDARD.md
  - ../../../data/registry/sources/archives/kansas-memory/
  - ../../../data/raw/archives/
  - ../../../data/quarantine/archives/
  - ../../../fixtures/
  - ../../../schemas/contracts/v1/source/
  - ../../../policy/sensitivity/
  - ../../../policy/rights/
  - ../../../release/
tags: [kfm, connectors, kansas-memory, src, package-layout, compatibility, no-network, source-admission, raw, quarantine, governance]
notes:
  - "This README fills a blank `src/` layout-boundary README under the legacy-style Kansas Memory compatibility connector."
  - "The parent connector README documents `connectors/kansas_memory/` as a noncanonical compatibility path; canonical connector work should converge under `connectors/kansas/kansas-memory/` unless an ADR says otherwise."
  - "The child package README at `src/kansas_memory/README.md` defines the package implementation boundary; this file defines the broader `src/` layout boundary."
  - "This README does not prove package modules, fixtures, tests, endpoint access, or CI wiring exist."
  - "Code under this layout must be no-network by default and may only support RAW or QUARANTINE handoff after SourceDescriptor and activation gates are satisfied."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Kansas Memory Compatibility Source Layout Boundary

> Layout-boundary README for `connectors/kansas_memory/src/`. This folder groups implementation package code for the noncanonical Kansas Memory compatibility connector. It is **not** itself a connector, policy root, schema root, release root, public API, or truth store.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Canonicality: noncanonical src path" src="https://img.shields.io/badge/canonicality-noncanonical__src__path-orange">
  <img alt="Network: disabled by default" src="https://img.shields.io/badge/network-disabled__by__default-critical">
  <img alt="Lifecycle: RAW or QUARANTINE only" src="https://img.shields.io/badge/lifecycle-RAW%20%7C%20QUARANTINE%20only-orange">
  <img alt="Publication: none" src="https://img.shields.io/badge/publication-none-critical">
</p>

> [!IMPORTANT]
> **Status:** `draft` compatibility source-layout README · **Owner:** `OWNER_TBD`  
> **Path:** `connectors/kansas_memory/src/README.md`  
> **Truth posture:** `CONFIRMED` file exists · `NONCANONICAL` compatibility src path · `NEEDS VERIFICATION` package inventory and CI wiring  
> **Boundary:** package-layout guidance only; no live-network default, no source activation, no release artifact, no public archive claim.

**Quick jumps:** [Scope](#scope) · [Repo fit](#repo-fit) · [Allowed contents](#allowed-contents) · [Forbidden contents](#forbidden-contents) · [Expected layout](#expected-layout) · [Evidence ledger](#evidence-ledger) · [Runtime posture](#runtime-posture) · [Validation expectations](#validation-expectations) · [Rollback](#rollback) · [Verification backlog](#verification-backlog)

---

## Scope

`connectors/kansas_memory/src/` is the source-layout container for the legacy Kansas Memory compatibility connector.

It may contain package directories, package-level README files, small helper modules, and implementation-boundary docs for source-admission parsing, normalization, validation, and RAW/QUARANTINE handoff helpers.

It must not become a second connector root, canonical package root, schema root, policy root, source registry, release root, proof root, fixture dump, live harvester, public API, or publication surface.

[Back to top ↑](#top)

---

## Repo fit

| Surface | Role | Status |
|---|---|---:|
| `connectors/kansas_memory/src/` | Compatibility source-layout container. | **CONFIRMED path / NEEDS VERIFICATION package inventory** |
| `connectors/kansas_memory/src/kansas_memory/` | Compatibility package namespace. | **CONFIRMED README path / NEEDS VERIFICATION modules** |
| `connectors/kansas_memory/README.md` | Parent compatibility connector README. | **CONFIRMED** |
| `connectors/kansas_memory/tests/README.md` | Compatibility-path test contract. | **CONFIRMED** |
| `connectors/kansas/` | Canonical Kansas connector-family lane. | **CONFIRMED** |
| `connectors/kansas/kansas-memory/` | Proposed canonical Kansas Memory connector home. | **PROPOSED / NEEDS VERIFICATION** |
| `docs/sources/catalog/kansas/kansas-memory.md` | Human-facing Kansas Memory source profile. | **CONFIRMED** |
| `data/raw/archives/`, `data/quarantine/archives/` | Candidate handoff targets. | **PROPOSED / NEEDS VERIFICATION** |
| `release/` | Release and publication controls. | **Out of scope for this source layout** |

[Back to top ↑](#top)

---

## Allowed contents

Allowed content under `src/`:

- package directories such as `kansas_memory/`;
- package-level README files;
- source-admission parsing helpers;
- metadata normalization helpers that do not upgrade truth status;
- validation helpers;
- handoff-envelope helpers for RAW or QUARANTINE candidates;
- deterministic error objects for quarantine/abstention;
- compatibility shims that point toward the canonical Kansas connector lane;
- lightweight test support modules, if they do not contain fixtures better placed under `fixtures/` or `tests/`.

---

## Forbidden contents

Do not place the following under this `src/` layout:

- canonical schemas;
- policy decisions or policy-as-code unless the repo has a clear connector-local policy-helper convention;
- source registry records;
- release manifests;
- proof/receipt authority records;
- public map tiles, public APIs, public summaries, or published artifacts;
- bulk archive dumps or fixture corpora;
- credentials, tokens, cookies, session state, or secrets;
- live-source jobs enabled by default;
- code that treats `connectors/kansas_memory/` as canonical without ADR/migration evidence.

[Back to top ↑](#top)

---

## Expected layout

Current-session evidence confirms only this README and the child package README. The rest is **PROPOSED** and must be verified before implementation claims.

```text
connectors/kansas_memory/src/
├── README.md                 # CONFIRMED — this layout-boundary README
└── kansas_memory/
    └── README.md             # CONFIRMED — package-boundary README
```

Potential package files are documented in `src/kansas_memory/README.md`; do not create them merely because they are listed there.

---

## Evidence ledger

| Source | Status | Supports | Limits |
|---|---:|---|---|
| `connectors/kansas_memory/src/README.md` | **CONFIRMED** | Target source-layout README exists and was blank before this update. | Does not prove modules, tests, or CI. |
| `connectors/kansas_memory/src/kansas_memory/README.md` | **CONFIRMED** | Child package README defines package implementation boundary. | Does not prove modules exist. |
| `connectors/kansas_memory/README.md` | **CONFIRMED** | Parent path is documented as noncanonical compatibility lane. | Does not prove canonical migration status. |
| `connectors/kansas_memory/tests/README.md` | **CONFIRMED** | Test posture is no-network by default and source-admission only. | Does not prove tests exist or pass. |
| `docs/sources/catalog/kansas/kansas-memory.md` | **CONFIRMED** | Kansas Memory source profile identifies rights/access/item-count verification needs and proposed canonical connector home under `connectors/kansas/`. | Does not prove endpoint availability or implementation. |
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
- deterministic failure when SourceDescriptor, activation, rights, sensitivity, CARE review, item identity, source role, metadata shape, or handoff target is unresolved.

---

## Validation expectations

Any implementation under this layout should be paired with tests that check:

- SourceDescriptor and activation preconditions;
- collection identity and item identity preservation;
- source URI and retrieval timestamp preservation;
- rights statement preservation;
- sensitivity and CARE/cultural review flag preservation;
- fail-closed quarantine/abstention errors;
- RAW/QUARANTINE-only handoff behavior;
- no default network access;
- no release/public artifact emission;
- no canonicality assumption for `connectors/kansas_memory/` without ADR/migration evidence.

[Back to top ↑](#top)

---

## Rollback

Rollback is required if this README is used to justify live harvesting, source activation, canonical status, public release, rights/sensitivity/CARE bypass, or implementation maturity without verified modules and tests.

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
| Confirm canonical Kansas Memory source-layout path. | **NEEDS VERIFICATION** | Directory Rules, ADR, migration note, or repo convention. |
| Confirm package/module inventory. | **NEEDS VERIFICATION** | Repo tree and package metadata. |
| Confirm SourceDescriptor and activation gate wiring. | **NEEDS VERIFICATION** | Source registry entry, code, and tests. |
| Confirm rights/sensitivity/CARE handling. | **NEEDS VERIFICATION** | Policy references, code, and tests. |
| Confirm fixture strategy and CI wiring. | **NEEDS VERIFICATION** | Fixture registry, workflow files, and test logs. |

---

## Maintainer note

Keep `src/` boring. It should organize implementation code only. Governance authority belongs in descriptors, policies, schemas, validation receipts, release records, and reviewed docs outside this layout.

[Back to top ↑](#top)
