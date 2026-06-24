<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-soil-readme
title: contracts/soil — Soil Compatibility Guard README
type: readme
version: v0.1
status: draft; compatibility-guard; no-parallel-authority; domain-path-variance
owners: OWNER_TBD — Soil domain steward · Contracts steward · Schema steward · Policy steward · Source steward · Docs steward · Directory Rules reviewer
created: 2026-06-24
updated: 2026-06-24
policy_label: public; contracts; soil; compatibility; no-parallel-authority; domain-placement; source-role-aware; release-gated
tags: [kfm, contracts, soil, compatibility, pointer, domain-placement, no-parallel-authority, semantic-contracts, source-role, support-type, release-gated]
related:
  - ../README.md
  - ../domains/README.md
  - ../domains/soil/README.md
  - ../../docs/domains/soil/README.md
  - ../../docs/domains/soil/CANONICAL_PATHS.md
  - ../../docs/domains/soil/ARCHITECTURE.md
  - ../../docs/domains/soil/DATA_LIFECYCLE.md
  - ../../schemas/contracts/v1/domains/soil/README.md
  - ../../policy/domains/soil/README.md
  - ../../docs/architecture/contract-schema-policy-split.md
notes:
  - "This file replaces a blank placeholder at `contracts/soil/README.md`."
  - "The inspected working Soil contract lane is `contracts/domains/soil/`."
  - "The inspected Soil contract-lane README records path variance between `contracts/domains/soil/` and `contracts/soil/` from Atlas lineage."
  - "This top-level `contracts/soil/` path is a compatibility guard only and must not become a parallel Soil contract root."
  - "Contracts define semantic meaning; schemas, policy, fixtures, tests, packages, pipelines, source registry records, lifecycle data, release artifacts, public APIs, map rendering, and runtime behavior remain in separate roots."
  - "Rollback target for this replacement is previous blank blob SHA `8b137891791fe96927ad78e64b0aad7bded08bdc`."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# contracts/soil

> Compatibility guard for the top-level `contracts/soil/` path. Current inspected Soil contract work belongs under [`../domains/soil/`](../domains/soil/). This folder exists only to prevent stale or lineage-derived references from becoming a parallel Soil contract authority.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Path: compatibility guard" src="https://img.shields.io/badge/path-compatibility__guard-lightgrey">
  <img alt="Canonical lane: contracts/domains/soil" src="https://img.shields.io/badge/canonical-contracts%2Fdomains%2Fsoil-blue">
  <img alt="Root: contracts" src="https://img.shields.io/badge/root-contracts-0a7ea4">
  <img alt="Posture: no parallel authority" src="https://img.shields.io/badge/posture-no__parallel__authority-critical">
</p>

**Status:** draft compatibility guard  
**Path:** `contracts/soil/README.md`  
**Inspected working Soil contract lane:** `contracts/domains/soil/`  
**Schema home:** `schemas/contracts/v1/domains/soil/` or ADR-selected successor  
**Policy home:** `policy/domains/soil/` or ADR-selected successor  
**Truth posture:** CONFIRMED placeholder was blank · CONFIRMED domain contract root is `contracts/domains/` · CONFIRMED Soil working lane exists at `contracts/domains/soil/` · CONFIRMED Soil README records path variance involving `contracts/soil/` · PROPOSED top-level guard until stale links are migrated or an ADR resolves the variance

## Quick jumps

[Purpose](#purpose) · [Authority split](#authority-split) · [Accepted contents](#accepted-contents) · [Exclusions](#exclusions) · [Migration posture](#migration-posture) · [Validation checklist](#validation-checklist) · [Rollback](#rollback)

---

## Purpose

This README exists because `contracts/soil/` exists as a top-level folder, while KFM domain contract placement uses `contracts/domains/<domain>/` for domain-specific semantic contracts.

Use this path only as a compatibility guard and navigation pointer.

Do not add canonical Soil object contracts here unless an ADR changes the domain-placement rule and migrates existing paths with rollback/backlink handling.

---

## Authority split

| Responsibility | Correct home | Rule |
|---|---|---|
| Soil semantic contracts | `contracts/domains/soil/` | Current inspected working lane for Soil object meaning. |
| This top-level path | `contracts/soil/` | Compatibility guard only. |
| Machine shape | `schemas/contracts/v1/domains/soil/` or ADR-selected schema home | JSON Schema belongs under `schemas/`. |
| Policy/admissibility | `policy/domains/soil/` or related policy roots | Policy owns allow/deny/restrict/abstain, sensitivity, rights, and release controls. |
| Fixtures/tests | `fixtures/domains/soil/`, `tests/domains/soil/` or accepted roots | Proof/examples stay outside contracts. |
| Source registry | source registry/data registry roots | SourceDescriptor and source authority metadata stay outside contracts. |
| Pipelines/packages | `pipelines/domains/soil/`, `packages/domains/soil/`, or accepted roots | Executable implementation stays outside contracts. |
| Data lifecycle | `data/raw`, `data/work`, `data/quarantine`, `data/processed`, `data/catalog`, `data/published` | Contracts do not store data. |
| Release/correction/rollback | `release/` and release-candidate roots | Publication is a governed state transition. |
| Public API/UI/map/AI | governed runtime/API/UI/map/AI roots | Downstream consumers only. |

---

## Accepted contents

Only conservative guard material belongs here:

| Accepted item | Purpose |
|---|---|
| `README.md` | Explain that this is not the canonical Soil contract home. |
| `MIGRATION.md` | Optional temporary plan to remove or redirect the top-level path. |
| `BACKLINKS.md` | Optional audit of stale links pointing here. |
| `ADR_POINTER.md` | Optional pointer to an accepted ADR if one resolves Soil path variance. |

Any content here must remain pointer-only and steward-reviewed.

---

## Exclusions

| Do not put this here | Correct home | Reason |
|---|---|---|
| `soil_map_unit.md`, `soil_component.md`, `horizon.md`, `component_horizon_join.md`, `soil_property.md`, `hydrologic_soil_group.md`, `soil_moisture_observation.md`, `pedon.md`, `soil_profile_view.md`, `erosion_risk.md`, `suitability_rating.md`, or `soil_time_caveat.md` | `contracts/domains/soil/` unless ADR selects another home | Avoids duplicate Soil semantic authority. |
| JSON Schemas | `schemas/contracts/v1/domains/soil/` or ADR-selected schema home | Schemas own shape. |
| Policy rules | `policy/domains/soil/` or related policy roots | Policy owns admissibility. |
| Fixtures, tests, validators | `fixtures/`, `tests/`, `tools/validators/` or accepted roots | Enforceability and validation stay separate. |
| Source registry records or SourceDescriptors | source registry/data registry roots | Contracts do not admit sources. |
| RAW/WORK/QUARANTINE/PROCESSED/CATALOG/PUBLISHED data | data lifecycle roots | Contracts do not store lifecycle data. |
| Pipelines, adapters, packages, generated SDKs | pipeline/package/tool roots | Implementation belongs outside contracts. |
| Release manifests, rollback cards, correction notices | `release/` and release contract/release roots | Release state is separate. |
| Public map/API/UI/AI behavior | governed public/runtime roots | Downstream behavior is not contract prose. |

---

## Migration posture

Preferred future state:

```text
contracts/soil/README.md                 # removed or retained only as compatibility guard
contracts/domains/soil/                  # current inspected working semantic contract lane
schemas/contracts/v1/domains/soil/       # machine-checkable schema lane
policy/domains/soil/                     # policy/admissibility lane
fixtures/domains/soil/                   # examples/proof data
tests/domains/soil/                      # enforceability
```

Before deleting this guard, search for stale backlinks that still point to `contracts/soil/`.

---

## Validation checklist

- [ ] Verify no canonical Soil object contracts are added under `contracts/soil/`.
- [ ] Verify Soil-domain semantic contracts are routed to `contracts/domains/soil/` unless ADR says otherwise.
- [ ] Verify schemas remain under `schemas/contracts/v1/domains/soil/` or ADR-selected schema home.
- [ ] Verify policy remains under `policy/domains/soil/` or related policy roots.
- [ ] Verify source registry records, lifecycle data, release artifacts, packages, pipelines, fixtures, tests, and validators remain in their own roots.
- [ ] Search for stale top-level `contracts/soil/` references before deletion or migration.

---

## Rollback

Rollback is required if this path is used as canonical Soil-object meaning, schema authority, policy authority, source registry authority, lifecycle storage, release approval, proof/receipt storage, runtime/API authority, or public map/UI/AI truth.

Rollback target for this replacement: previous blank blob SHA `8b137891791fe96927ad78e64b0aad7bded08bdc`.

<p align="right"><a href="#top">Back to top</a></p>
