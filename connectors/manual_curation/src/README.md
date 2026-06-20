<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/connectors-manual-curation-src-readme
title: connectors/manual_curation/src/ — Manual Curation Source Layout Boundary
type: readme
version: v0.1
status: draft
owners: OWNER_TBD — Connector steward · Package maintainer · Source steward · Docs steward · Validation steward · Rights reviewer · Sensitivity reviewer
created: 2026-06-19
updated: 2026-06-19
policy_label: public-doctrine; src-layout-boundary; manual-curation; steward-assisted; no-publication; quarantine-aware; implementation-depth-needs-verification
proposed_path: connectors/manual_curation/src/README.md
truth_posture: CONFIRMED path exists / PROPOSED source-layout boundary / PACKAGE INVENTORY NEEDS VERIFICATION
related:
  - ../README.md
  - ../tests/README.md
  - ./manual_curation/README.md
  - ../../../docs/sources/catalog/manual_curation/README.md
  - ../../../docs/sources/catalog/manual_curation/steward-curation-workflow.md
  - ../../../docs/sources/SOURCE_DESCRIPTOR_STANDARD.md
  - ../../../docs/sources/source-roles.md
  - ../../../docs/doctrine/directory-rules.md
  - ../../../docs/doctrine/trust-membrane.md
  - ../../../docs/doctrine/lifecycle-law.md
  - ../../../docs/doctrine/truth-posture.md
  - ../../../docs/governance/separation-of-duties.md
  - ../../../data/registry/sources/
  - ../../../data/raw/
  - ../../../data/quarantine/
  - ../../../fixtures/
  - ../../../schemas/contracts/v1/source/
  - ../../../policy/sources/
  - ../../../policy/sensitivity/
  - ../../../policy/rights/
  - ../../../release/
tags: [kfm, connectors, manual-curation, src, package-layout, steward-review, source-admission, source-descriptor, source-role, quarantine, validation, evidencebundle, rollback, governance]
notes:
  - "This README fills a blank `src/` layout-boundary README under the proposed manual-curation helper lane."
  - "The child package README at `src/manual_curation/README.md` defines the package implementation boundary; this file defines the broader `src/` layout boundary."
  - "The manual-curation catalog README states it is methodology and steward reference, not implementation proof."
  - "Code under this layout may only support steward-gate helpers and RAW/QUARANTINE handoff; policy, approval, catalog closure, and release decisions remain outside this layout."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Manual Curation Source Layout Boundary

> Layout-boundary README for `connectors/manual_curation/src/`. This folder groups implementation package code for the proposed manual-curation helper lane. It is **not** itself a connector, policy root, schema root, source registry, release root, public API, fixture authority, proof authority, catalog-closure authority, or truth store.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Truth: package inventory needs verification" src="https://img.shields.io/badge/truth-package__inventory__needs__verification-orange">
  <img alt="Policy: cite or abstain" src="https://img.shields.io/badge/posture-cite__or__abstain-success">
  <img alt="Lifecycle: RAW or QUARANTINE only" src="https://img.shields.io/badge/lifecycle-RAW%20%7C%20QUARANTINE%20only-orange">
</p>

> [!IMPORTANT]
> **Status:** `draft` source-layout README · **Owner:** `OWNER_TBD`  
> **Path:** `connectors/manual_curation/src/README.md`  
> **Truth posture:** `CONFIRMED` file exists · `PROPOSED` source-layout boundary · `NEEDS VERIFICATION` package inventory and CI wiring  
> **Boundary:** package-layout guidance only; no source activation, no source-role upgrade, no catalog closure, no release artifact.

**Quick jumps:** [Scope](#scope) · [Repo fit](#repo-fit) · [Allowed contents](#allowed-contents) · [Forbidden contents](#forbidden-contents) · [Expected layout](#expected-layout) · [Evidence ledger](#evidence-ledger) · [Runtime posture](#runtime-posture) · [Validation expectations](#validation-expectations) · [Rollback](#rollback) · [Verification backlog](#verification-backlog)

---

## Scope

`connectors/manual_curation/src/` is the source-layout container for manual-curation helper implementation code.

It may contain package directories, package-level README files, small helper modules, and implementation-boundary docs for candidate intake packets, descriptor-draft references, source-role review routing, rights and sensitivity routing, evidence-reference preservation, validation-defect summaries, quarantine disposition notes, correction handoff notes, rollback handoff notes, and RAW/QUARANTINE handoff preparation.

It must not become a second connector root, canonical package root, schema root, policy root, source registry, release root, proof root, fixture dump, public API, catalog-closure authority, or publication surface.

[Back to top ↑](#top)

---

## Repo fit

| Surface | Role | Status |
|---|---|---:|
| `connectors/manual_curation/src/` | Manual-curation source-layout container. | **CONFIRMED path / NEEDS VERIFICATION package inventory** |
| `connectors/manual_curation/src/manual_curation/` | Manual-curation helper package namespace. | **CONFIRMED README path / NEEDS VERIFICATION modules** |
| `connectors/manual_curation/README.md` | Parent manual-curation connector-boundary README. | **CONFIRMED** |
| `connectors/manual_curation/tests/README.md` | Manual-curation test-boundary README. | **CONFIRMED** |
| `docs/sources/catalog/manual_curation/README.md` | Manual-curation methodology and steward reference. | **CONFIRMED** |
| `data/registry/sources/` | SourceDescriptor authority. | **Outside layout / NEEDS VERIFICATION for entries** |
| `data/raw/` and `data/quarantine/` | Candidate handoff targets. | **Outside layout** |
| `release/` | Release and publication controls. | **Out of scope for this layout** |

---

## Allowed contents

Allowed content under `src/`:

- package directories such as `manual_curation/`;
- package-level README files;
- candidate intake packet helpers;
- descriptor-draft helper modules;
- source-role review helper modules;
- rights and sensitivity routing helpers;
- evidence-reference preservation helpers;
- validation-defect summary helpers;
- quarantine disposition helpers;
- correction and rollback handoff helpers;
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
- catalog-closure records;
- public maps, public APIs, public summaries, or published artifacts;
- bulk source dumps or fixture corpora;
- code that approves source activation, source-role upgrade, catalog closure, release state, or public visibility by convenience.

---

## Expected layout

Current-session evidence confirms only this README and the child package README. The rest is **PROPOSED** and must be verified before implementation claims.

```text
connectors/manual_curation/src/
├── README.md                       # CONFIRMED — this layout-boundary README
└── manual_curation/
    └── README.md                   # CONFIRMED — package-boundary README
```

Potential package files are documented in `src/manual_curation/README.md`; do not create them merely because they are listed there.

---

## Evidence ledger

| Source | Status | Supports | Limits |
|---|---:|---|---|
| `connectors/manual_curation/src/README.md` | **CONFIRMED** | Target source-layout README exists and was blank before this update. | Does not prove modules, tests, or CI. |
| `connectors/manual_curation/src/manual_curation/README.md` | **CONFIRMED** | Child package README defines package implementation boundary. | Does not prove modules exist. |
| `connectors/manual_curation/README.md` | **CONFIRMED** | Parent README defines the helper boundary and forbids activation, source-role upgrade, catalog closure, and publication. | Does not prove implementation maturity. |
| `connectors/manual_curation/tests/README.md` | **CONFIRMED** | Test README defines gate-preserving test posture. | Does not prove tests exist or pass. |
| `docs/sources/catalog/manual_curation/README.md` | **CONFIRMED** | Manual curation is steward-led methodology, not implementation proof. | Exact workflow implementation and tooling remain unverified. |
| Package/module files below this layout | **NEEDS VERIFICATION** | This README defines expected layout boundaries. | Actual files, behavior, and CI status remain unverified. |

---

## Runtime posture

Code under this layout should default to:

- no source activation decision;
- no source-role upgrade;
- no public output;
- no catalog closure;
- no release artifact creation;
- no direct writes beyond RAW or QUARANTINE handoff envelopes;
- deterministic failure when descriptor, rights, sensitivity, source role, evidence, validation, review, correction, or rollback state is unresolved.

---

## Validation expectations

Any implementation under this layout should be paired with tests that check:

- descriptor or descriptor-draft reference preservation;
- explicit source-role preservation;
- rights-state and sensitivity-state routing;
- evidence-reference preservation;
- validation-defect visibility;
- quarantine reason preservation;
- correction and rollback handoff preservation;
- RAW/QUARANTINE-only handoff behavior;
- no release/public artifact emission;
- no source activation, source-role upgrade, or catalog closure by convenience.

---

## Rollback

Rollback is required if this README is used to justify source activation, source-role upgrade, catalog closure, public release, rights/sensitivity bypass, direct publication, or implementation maturity without verified modules and tests.

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
| Confirm descriptor and source-role support. | **NEEDS VERIFICATION** | Registry entries, code, and tests. |
| Confirm rights/sensitivity/review-state routing. | **NEEDS VERIFICATION** | Policy references, code, and tests. |
| Confirm RAW/QUARANTINE handoff envelope shape. | **NEEDS VERIFICATION** | Schemas/contracts and tests. |
| Confirm fixture strategy and CI wiring. | **NEEDS VERIFICATION** | Fixture registry, workflow files, and test logs. |

---

## Maintainer note

Keep `src/` boring. It should organize helper code only. Governance authority belongs in descriptors, policies, schemas, validation receipts, EvidenceBundles, release records, correction paths, and rollback targets outside this layout.

[Back to top ↑](#top)
