<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-settlement-readme
title: contracts/settlement — Settlement Compatibility Guard README
type: readme
version: v0.1
status: draft; compatibility-guard; no-parallel-authority; domain-path-variance
owners: OWNER_TBD — Settlements/Infrastructure domain steward · Contracts steward · Schema steward · Policy steward · Docs steward · Directory Rules reviewer
created: 2026-06-24
updated: 2026-06-24
policy_label: public; contracts; settlement; compatibility; settlements-infrastructure; no-parallel-authority; domain-placement; release-gated
tags: [kfm, contracts, settlement, settlements-infrastructure, compatibility, pointer, domain-placement, no-parallel-authority, semantic-contracts, release-gated]
related:
  - ../README.md
  - ../domains/README.md
  - ../domains/settlement/README.md
  - ../domains/settlements-infrastructure/README.md
  - ../../docs/domains/settlements-infrastructure/README.md
  - ../../docs/domains/settlements-infrastructure/CANONICAL_PATHS.md
  - ../../docs/domains/settlements-infrastructure/sublanes/settlements.md
  - ../../schemas/contracts/v1/domains/settlements-infrastructure/
  - ../../policy/domains/settlements-infrastructure/
  - ../../docs/architecture/contract-schema-policy-split.md
notes:
  - "This file replaces a blank placeholder at `contracts/settlement/README.md`."
  - "The inspected canonical working contract lane is `contracts/domains/settlements-infrastructure/`."
  - "The inspected singular domain path `contracts/domains/settlement/` is already marked as a CONFLICTED compatibility / variance surface."
  - "This top-level `contracts/settlement/` path is a guard/pointer only and must not become a new settlement contract root."
  - "Contracts define semantic meaning; schemas, policy, fixtures, tests, data lifecycle, release artifacts, and runtime/API behavior remain in separate roots."
  - "Rollback target for this replacement is previous blank blob SHA `8b137891791fe96927ad78e64b0aad7bded08bdc`."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# contracts/settlement

> Compatibility guard for the top-level `contracts/settlement/` path. Current inspected settlement-domain contract work belongs under [`../domains/settlements-infrastructure/`](../domains/settlements-infrastructure/), while [`../domains/settlement/`](../domains/settlement/) is already marked as a conflicted compatibility surface. This folder must not become another settlement authority.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Path: compatibility guard" src="https://img.shields.io/badge/path-compatibility__guard-lightgrey">
  <img alt="Canonical lane: settlements-infrastructure" src="https://img.shields.io/badge/canonical-settlements--infrastructure-blue">
  <img alt="Root: contracts" src="https://img.shields.io/badge/root-contracts-0a7ea4">
  <img alt="Posture: no parallel authority" src="https://img.shields.io/badge/posture-no__parallel__authority-critical">
</p>

**Status:** draft compatibility guard  
**Path:** `contracts/settlement/README.md`  
**Canonical inspected working lane:** `contracts/domains/settlements-infrastructure/`  
**Singular domain compatibility lane:** `contracts/domains/settlement/`  
**Schema home:** `schemas/contracts/v1/domains/settlements-infrastructure/` or ADR-selected successor  
**Policy home:** `policy/domains/settlements-infrastructure/` or ADR-selected successor  
**Truth posture:** CONFIRMED placeholder was blank · CONFIRMED domain contract root is `contracts/domains/` · CONFIRMED current working lane is `contracts/domains/settlements-infrastructure/` · CONFIRMED singular `contracts/domains/settlement/` is conflicted compatibility surface · PROPOSED top-level guard until stale links are migrated or this path is removed

## Quick jumps

[Purpose](#purpose) · [Authority split](#authority-split) · [Accepted contents](#accepted-contents) · [Exclusions](#exclusions) · [Migration posture](#migration-posture) · [Validation checklist](#validation-checklist) · [Rollback](#rollback)

---

## Purpose

This README exists because `contracts/settlement/` exists as a top-level folder, but KFM domain contract placement uses `contracts/domains/<domain>/` for domain-specific semantic contracts.

Use this path only as a compatibility guard and navigation pointer.

Do not add canonical settlement object contracts here unless an ADR changes the domain-placement rule and migrates existing paths with rollback/backlink handling.

---

## Authority split

| Responsibility | Correct home | Rule |
|---|---|---|
| Domain-specific settlement/infrastructure semantic contracts | `contracts/domains/settlements-infrastructure/` | Current inspected working lane. |
| Singular settlement domain variance | `contracts/domains/settlement/` | Existing conflicted compatibility surface. |
| This top-level path | `contracts/settlement/` | Compatibility guard only. |
| Machine shape | `schemas/contracts/v1/domains/settlements-infrastructure/` or ADR-selected schema home | JSON Schema belongs under `schemas/`. |
| Policy/admissibility | `policy/domains/settlements-infrastructure/` or ADR-selected policy home | Policy owns allow/deny/restrict/abstain, rights, sensitivity, release gating. |
| Fixtures/tests | `fixtures/domains/settlements-infrastructure/`, `tests/domains/settlements-infrastructure/` or accepted roots | Proof/examples stay outside contracts. |
| Data lifecycle | `data/raw`, `data/work`, `data/quarantine`, `data/processed`, `data/catalog`, `data/published` | Contracts do not store data. |
| Release/correction/rollback | `release/` and release-candidate roots | Publication is a governed state transition. |
| Public API/UI/map/AI | governed runtime/API/UI/map/AI roots | Downstream consumers only. |

---

## Accepted contents

Only conservative guard material belongs here:

| Accepted item | Purpose |
|---|---|
| `README.md` | Explain that this is not the canonical settlement contract home. |
| `MIGRATION.md` | Optional temporary plan to remove or redirect the top-level path. |
| `BACKLINKS.md` | Optional audit of stale links pointing here. |
| `ADR_POINTER.md` | Optional pointer to an accepted ADR if one resolves settlement path variance. |

Any content here must remain pointer-only and steward-reviewed.

---

## Exclusions

| Do not put this here | Correct home | Reason |
|---|---|---|
| `Settlement`, `Municipality`, `CensusPlace`, `Townsite`, `GhostTown`, `Fort`, `Mission`, or `ReservationCommunity` contracts | `contracts/domains/settlements-infrastructure/` unless ADR selects another home | Avoids a third settlement authority. |
| Infrastructure object contracts | `contracts/domains/settlements-infrastructure/` | Settlements and infrastructure are currently combined in the inspected domain lane. |
| JSON Schemas | `schemas/contracts/v1/domains/settlements-infrastructure/` or ADR-selected schema home | Schemas own shape. |
| Policy rules | `policy/domains/settlements-infrastructure/` or related policy roots | Policy owns admissibility. |
| Fixtures, tests, validators | `fixtures/`, `tests/`, `tools/validators/` or accepted roots | Enforceability and validation stay separate. |
| Source registry records | source registry/data registry roots | Contracts do not admit sources. |
| RAW/WORK/QUARANTINE/PROCESSED/CATALOG/PUBLISHED data | data lifecycle roots | Contracts do not store lifecycle data. |
| Release manifests, rollback cards, correction notices | `release/` and release contract/release roots | Release state is separate. |
| Public map/API/UI/AI behavior | governed public/runtime roots | Downstream behavior is not contract prose. |

---

## Migration posture

Preferred future state:

```text
contracts/settlement/README.md                       # removed or retained only as compatibility guard
contracts/domains/settlements-infrastructure/         # current working semantic contract lane
contracts/domains/settlement/README.md                # existing conflicted compatibility surface until resolved
schemas/contracts/v1/domains/settlements-infrastructure/
policy/domains/settlements-infrastructure/
```

Before deleting this guard, search for stale backlinks that still point to `contracts/settlement/`.

---

## Validation checklist

- [ ] Verify no canonical object contracts are added under `contracts/settlement/`.
- [ ] Verify settlement-domain semantic contracts are routed to `contracts/domains/settlements-infrastructure/` unless ADR says otherwise.
- [ ] Verify singular `contracts/domains/settlement/` remains compatibility-only until ADR resolution.
- [ ] Verify schemas remain under `schemas/contracts/v1/domains/settlements-infrastructure/` or ADR-selected schema home.
- [ ] Verify policy remains under `policy/domains/settlements-infrastructure/` or related policy roots.
- [ ] Search for stale top-level `contracts/settlement/` references before deletion or migration.

---

## Rollback

Rollback is required if this path is used as canonical settlement-object meaning, schema authority, policy authority, data lifecycle storage, source registry authority, release approval, proof/receipt storage, runtime/API authority, or public map/UI/AI truth.

Rollback target for this replacement: previous blank blob SHA `8b137891791fe96927ad78e64b0aad7bded08bdc`.

<p align="right"><a href="#top">Back to top</a></p>
