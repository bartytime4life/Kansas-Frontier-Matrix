<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/domains/atmosphere/forecast-context-compatibility-note
title: contracts/domains/atmosphere/forecast-context.md — ForecastContext Compatibility Pointer
type: compatibility-note
version: v0.2
status: draft
owners: OWNER_TBD — Atmosphere steward · Forecast/model steward · Contract steward · Schema steward · Docs steward
created: 2026-06-21
updated: 2026-06-21
policy_label: public; contracts; domains; atmosphere; forecast-context; compatibility; scaffold-resolution
tags: [kfm, contracts, atmosphere, forecast-context, compatibility, scaffold, canonical-pointer, governance]
related:
  - ./ForecastContext.md
  - ../../../schemas/contracts/v1/domains/atmosphere/ForecastContext.schema.json
  - ../../../docs/domains/atmosphere/FILE_SYSTEM_PLAN.md
  - ../../../docs/domains/atmosphere/CANONICAL_PATHS.md
  - ../../../docs/domains/atmosphere/OBJECT_FAMILY_MAP.md
  - ../../../docs/domains/atmosphere/POLICY.md
  - ../../../docs/domains/atmosphere/PUBLICATION_POSTURE.md
notes:
  - "This lowercase file was a planned-path scaffold generated from docs/domains/atmosphere/FILE_SYSTEM_PLAN.md."
  - "The canonical semantic contract is ./ForecastContext.md."
  - "The paired schema metadata points to contracts/domains/atmosphere/ForecastContext.md, not this lowercase compatibility pointer."
  - "Do not duplicate full ForecastContext semantics here or create a parallel lowercase schema without an ADR/migration note."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# ForecastContext Compatibility Pointer

> This file preserves the lowercase planned path `contracts/domains/atmosphere/forecast-context.md` as a compatibility and lineage note. The authoritative Atmosphere/Air semantic contract for this object is [`ForecastContext.md`](./ForecastContext.md).

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Owner: OWNER_TBD" src="https://img.shields.io/badge/owner-OWNER__TBD-lightgrey">
  <img alt="Canonical: ForecastContext.md" src="https://img.shields.io/badge/canonical-ForecastContext.md-green">
  <img alt="Role: compatibility pointer" src="https://img.shields.io/badge/role-compatibility__pointer-blue">
  <img alt="Schema: canonical CamelCase" src="https://img.shields.io/badge/schema-ForecastContext.schema.json-orange">
</p>

**Path:** `contracts/domains/atmosphere/forecast-context.md`  
**Canonical contract:** [`./ForecastContext.md`](./ForecastContext.md)  
**Canonical schema:** `../../../schemas/contracts/v1/domains/atmosphere/ForecastContext.schema.json`

## Quick jumps

[Canonical authority](#canonical-authority) · [Why this file exists](#why-this-file-exists) · [Rules for maintainers](#rules-for-maintainers) · [Schema posture](#schema-posture) · [Evidence basis](#evidence-basis) · [Rollback](#rollback)

---

## Canonical authority

The controlling contract is:

```text
contracts/domains/atmosphere/ForecastContext.md
```

That file defines `ForecastContext` as the Atmosphere/Air-domain object representing a governed modeled atmospheric field, forecast context, model-run context, or forecast-derived explanatory layer. Use the canonical contract for object meaning, recommended fields, invariants, lifecycle expectations, validation expectations, and evidence/policy/release/correction/rollback posture.

---

## Why this file exists

This lowercase path existed as a **planned-path scaffold** sourced from:

```text
docs/domains/atmosphere/FILE_SYSTEM_PLAN.md
```

That plan explicitly warns that concrete paths are proposed until verified against the mounted repository. In the live repository, the full semantic contract already exists at the CamelCase path:

```text
contracts/domains/atmosphere/ForecastContext.md
```

Keeping this file as a pointer avoids two competing contract authorities while preserving discoverability for users, scripts, or notes that still reference the lowercase planned path.

---

## Rules for maintainers

| Rule | Required action |
|---|---|
| Do not duplicate the full contract here. | Edit [`./ForecastContext.md`](./ForecastContext.md) instead. |
| Do not point validators here. | Use the canonical schema metadata and canonical contract path. |
| Do not create a lowercase parallel schema by default. | Use `ForecastContext.schema.json` unless an ADR or migration note accepts a casing change. |
| Do not treat this file as release authority. | Release, correction, supersession, and rollback remain separate. |
| Do not treat this file as evidence or policy authority. | EvidenceBundle/proof and policy decisions remain in their own roots. |
| If this pointer becomes obsolete. | Remove it only with a migration note and link-update sweep. |

---

## Schema posture

The canonical schema is:

```text
schemas/contracts/v1/domains/atmosphere/ForecastContext.schema.json
```

The schema metadata points to:

```text
contracts/domains/atmosphere/ForecastContext.md
```

Current machine-shape posture remains `PROPOSED`: the schema has empty properties and allows additional properties. This pointer does not strengthen or weaken that schema; it only prevents a second Markdown authority from forming at the lowercase path.

---

## Evidence basis

| Source | Status | Supports | Limits |
|---|---|---|---|
| Prior `contracts/domains/atmosphere/forecast-context.md` scaffold | `CONFIRMED repo evidence` | Lowercase path existed as a planned-path scaffold sourced from `FILE_SYSTEM_PLAN.md`. | It was not a completed contract. |
| `contracts/domains/atmosphere/ForecastContext.md` | `CONFIRMED repo evidence` | Canonical full semantic contract exists and defines object meaning, boundaries, lifecycle, validation, rollback, and evidence basis. | Does not prove validator/runtime enforcement. |
| `schemas/contracts/v1/domains/atmosphere/ForecastContext.schema.json` | `CONFIRMED repo evidence` | Schema points to `contracts/domains/atmosphere/ForecastContext.md` and is currently `PROPOSED`. | Empty properties; does not enforce full semantics. |
| `docs/domains/atmosphere/FILE_SYSTEM_PLAN.md` | `CONFIRMED plan-class doc` | Explains why planned paths may appear and warns paths are proposed until verified. | Not implementation proof. |
| `docs/domains/atmosphere/OBJECT_FAMILY_MAP.md` | `CONFIRMED doctrine-adjacent doc` | Lists Forecast Context as an Atmosphere object with model-field character. | Does not resolve lowercase vs. CamelCase filename on its own. |

---

## Rollback

Rollback if this pointer is used as a second contract authority, if validators or schemas start pointing to the lowercase file without an accepted migration, or if the canonical `ForecastContext.md` contract is removed without a documented casing migration.

Rollback target: prior lowercase scaffold blob SHA `5c9e96298174f3a97f8e45b3bbdb8a02fe40794c`.

<p align="right"><a href="#top">Back to top</a></p>
