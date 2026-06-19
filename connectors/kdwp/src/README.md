<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/connectors-kdwp-src-readme
title: connectors/kdwp/src/ — KDWP Compatibility Source Layout Boundary
type: readme
version: v0.1
status: draft
owners: OWNER_TBD — Connector steward · Kansas source steward · Fauna steward · Flora steward · Habitat steward · Package maintainer · Test steward · Validation steward · Docs steward
created: 2026-06-19
updated: 2026-06-19
policy_label: public-doctrine; src-layout-boundary; compatibility-lane; no-network-default; sensitivity-gated; no-publication
proposed_path: connectors/kdwp/src/README.md
truth_posture: CONFIRMED path exists / NONCANONICAL compatibility src README / PACKAGE INVENTORY NEEDS VERIFICATION
related:
  - ../README.md
  - ../tests/README.md
  - ./kdwp/README.md
  - ../../kansas/README.md
  - ../../kansas/kdwp/README.md
  - ../../kansas/kdwp_flora/README.md
  - ../../kansas/kdwp_ert/README.md
  - ../../../docs/sources/catalog/kansas/kdwp.md
  - ../../../docs/domains/fauna/README.md
  - ../../../docs/domains/flora/README.md
  - ../../../docs/domains/habitat/README.md
  - ../../../docs/sources/SOURCE_DESCRIPTOR_STANDARD.md
  - ../../../data/registry/sources/
  - ../../../data/raw/fauna/
  - ../../../data/quarantine/fauna/
  - ../../../data/raw/flora/
  - ../../../data/quarantine/flora/
  - ../../../data/raw/habitat/
  - ../../../data/quarantine/habitat/
  - ../../../fixtures/
  - ../../../schemas/contracts/v1/source/
  - ../../../schemas/contracts/v1/biodiversity/
  - ../../../policy/sensitivity/
  - ../../../policy/rights/
  - ../../../release/
tags: [kfm, connectors, kdwp, src, package-layout, kansas, wildlife, parks, fauna, flora, habitat, compatibility, no-network, source-admission, raw, quarantine, governance]
notes:
  - "This README fills a blank `src/` layout-boundary README under the top-level KDWP compatibility connector."
  - "The parent connector README documents `connectors/kdwp/` as a noncanonical compatibility path; canonical KDWP work belongs under `connectors/kansas/kdwp/` unless an ADR says otherwise."
  - "The child package README at `src/kdwp/README.md` defines the package implementation boundary; this file defines the broader `src/` layout boundary."
  - "This README does not prove package modules, fixtures, tests, endpoint access, or CI wiring exist."
  - "Code under this layout must be no-network by default and may only support RAW or QUARANTINE handoff after SourceDescriptor and activation gates are satisfied."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# KDWP Compatibility Source Layout Boundary

> Layout-boundary README for `connectors/kdwp/src/`. This folder groups implementation package code for the noncanonical KDWP compatibility connector. It is **not** itself a connector, policy root, schema root, release root, public API, or truth store.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Canonicality: noncanonical src path" src="https://img.shields.io/badge/canonicality-noncanonical__src__path-orange">
  <img alt="Network: disabled by default" src="https://img.shields.io/badge/network-disabled__by__default-critical">
  <img alt="Lifecycle: RAW or QUARANTINE only" src="https://img.shields.io/badge/lifecycle-RAW%20%7C%20QUARANTINE%20only-orange">
  <img alt="Publication: none" src="https://img.shields.io/badge/publication-none-critical">
</p>

> [!IMPORTANT]
> **Status:** `draft` compatibility source-layout README · **Owner:** `OWNER_TBD`  
> **Path:** `connectors/kdwp/src/README.md`  
> **Truth posture:** `CONFIRMED` file exists · `NONCANONICAL` compatibility src path · `NEEDS VERIFICATION` package inventory and CI wiring  
> **Boundary:** package-layout guidance only; no live-network default, no source activation, no release artifact, no public claim.

**Quick jumps:** [Scope](#scope) · [Repo fit](#repo-fit) · [Allowed contents](#allowed-contents) · [Forbidden contents](#forbidden-contents) · [Expected layout](#expected-layout) · [Evidence ledger](#evidence-ledger) · [Runtime posture](#runtime-posture) · [Validation expectations](#validation-expectations) · [Rollback](#rollback) · [Verification backlog](#verification-backlog)

---

## Scope

`connectors/kdwp/src/` is the source-layout container for the legacy KDWP compatibility connector.

It may contain package directories, package-level README files, small helper modules, and implementation-boundary docs for source-admission parsing, normalization, validation, source-role preservation, taxonomy preservation, geometry/uncertainty preservation, and RAW/QUARANTINE handoff helpers.

It must not become a second connector root, canonical package root, schema root, policy root, source registry, release root, proof root, fixture dump, live harvester, public API, or publication surface.

[Back to top ↑](#top)

---

## Repo fit

| Surface | Role | Status |
|---|---|---:|
| `connectors/kdwp/src/` | Compatibility source-layout container. | **CONFIRMED path / NEEDS VERIFICATION package inventory** |
| `connectors/kdwp/src/kdwp/` | Compatibility package namespace. | **CONFIRMED README path / NEEDS VERIFICATION modules** |
| `connectors/kdwp/README.md` | Parent compatibility connector README. | **CONFIRMED** |
| `connectors/kdwp/tests/README.md` | Compatibility-path test contract. | **CONFIRMED** |
| `connectors/kansas/kdwp/` | Canonical KDWP connector lane. | **CONFIRMED README path** |
| `connectors/kansas/kdwp_flora/` | KDWP flora/listed-species compatibility or sublane. | **CONFIRMED README path / PLACEMENT NEEDS VERIFICATION** |
| `connectors/kansas/kdwp_ert/` | KDWP Ecological Review Tool compatibility or sublane. | **CONFIRMED README path / PLACEMENT NEEDS VERIFICATION** |
| `docs/sources/catalog/kansas/kdwp.md` | Human-facing KDWP source catalog entry. | **CONFIRMED** |
| `data/raw/fauna/`, `data/raw/flora/`, `data/raw/habitat/` | Candidate RAW handoff targets. | **PROPOSED / NEEDS VERIFICATION** |
| `data/quarantine/fauna/`, `data/quarantine/flora/`, `data/quarantine/habitat/` | Candidate quarantine handoff targets. | **PROPOSED / NEEDS VERIFICATION** |
| `release/` | Release and publication controls. | **Out of scope for this source layout** |

[Back to top ↑](#top)

---

## Allowed contents

Allowed content under `src/`:

- package directories such as `kdwp/`;
- package-level README files;
- source-admission parsing helpers;
- metadata normalization helpers that do not upgrade truth status;
- validation helpers;
- KDWP source-role separation helpers;
- taxonomy and listed-status context helpers;
- sensitivity and review-state preservation helpers;
- geometry and uncertainty preservation helpers;
- handoff-envelope helpers for RAW or QUARANTINE candidates;
- deterministic error objects for quarantine or abstention;
- compatibility shims that point toward the canonical `connectors/kansas/kdwp/` lane;
- lightweight test support modules, if they do not contain fixtures better placed under `fixtures/` or `tests/`.

---

## Forbidden contents

Do not place the following under this `src/` layout:

- canonical schemas;
- policy decisions or policy-as-code unless the repo has a clear connector-local policy-helper convention;
- source registry records;
- release manifests;
- proof or receipt authority records;
- public maps, public APIs, public summaries, public range or habitat claims, or published artifacts;
- bulk harvest dumps or fixture corpora;
- credentials, tokens, cookies, session state, or secrets;
- live-source jobs enabled by default;
- code that treats `connectors/kdwp/` as canonical without ADR or migration evidence.

[Back to top ↑](#top)

---

## Expected layout

Current-session evidence confirms only this README and the child package README. The rest is **PROPOSED** and must be verified before implementation claims.

```text
connectors/kdwp/src/
├── README.md                       # CONFIRMED — this layout-boundary README
└── kdwp/
    └── README.md                   # CONFIRMED — package-boundary README
```

Potential package files are documented in `src/kdwp/README.md`; do not create them merely because they are listed there.

---

## Evidence ledger

| Source | Status | Supports | Limits |
|---|---:|---|---|
| `connectors/kdwp/src/README.md` | **CONFIRMED** | Target source-layout README exists and was blank before this update. | Does not prove modules, tests, or CI. |
| `connectors/kdwp/src/kdwp/README.md` | **CONFIRMED** | Child package README defines package implementation boundary. | Does not prove modules exist. |
| `connectors/kdwp/README.md` | **CONFIRMED** | Parent path is documented as noncanonical compatibility lane. | Does not prove canonical migration status. |
| `connectors/kdwp/tests/README.md` | **CONFIRMED** | Test posture is no-network by default, fixture-safe, and source-admission only. | Does not prove tests exist or pass. |
| `docs/sources/catalog/kansas/kdwp.md` | **CONFIRMED** | KDWP source profile identifies canonical `connectors/kansas/kdwp/`, source-role separation, and rights/sensitivity gates. | Does not prove endpoint availability or implementation. |
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
- deterministic failure when SourceDescriptor, activation, rights, sensitivity, review state, source role, taxon identity, listed-status context, observation identity, geometry, source shape, or handoff target is unresolved.

---

## Validation expectations

Any implementation under this layout should be paired with tests that check:

- SourceDescriptor and activation preconditions;
- KDWP source-role separation;
- taxon identity preservation;
- listed-status and sensitivity context preservation;
- observation identity preservation;
- source URI and retrieval timestamp preservation;
- rights statement presence and preservation;
- sensitivity and review-state preservation;
- geometry and uncertainty preservation;
- fail-closed quarantine or abstention errors;
- RAW/QUARANTINE-only handoff behavior;
- no default network access;
- no release/public artifact emission;
- no canonicality assumption for `connectors/kdwp/` without ADR or migration evidence.

[Back to top ↑](#top)

---

## Rollback

Rollback is required if this README is used to justify live harvesting, source activation, canonical status, public release, rights/sensitivity bypass, source-role collapse, or implementation maturity without verified modules and tests.

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
| Confirm canonical KDWP source-layout path. | **NEEDS VERIFICATION** | Directory Rules, ADR, migration note, or repo convention. |
| Confirm package/module inventory. | **NEEDS VERIFICATION** | Repo tree and package metadata. |
| Confirm SourceDescriptor and activation gate wiring. | **NEEDS VERIFICATION** | Source registry entry, code, and tests. |
| Confirm rights/sensitivity handling. | **NEEDS VERIFICATION** | Policy references, code, and tests. |
| Confirm fixture strategy and CI wiring. | **NEEDS VERIFICATION** | Fixture registry, workflow files, and test logs. |

---

## Maintainer note

Keep `src/` boring. It should organize implementation code only. Governance authority belongs in descriptors, policies, schemas, validation receipts, release records, and reviewed docs outside this layout.

[Back to top ↑](#top)
