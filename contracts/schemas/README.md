<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-schemas-readme
title: contracts/schemas — Schema Compatibility Guard README
type: readme
version: v0.1
status: draft; compatibility-guard; parallel-schema-authority-blocker; no-canonical-schema-home
owners: OWNER_TBD — Contracts steward · Schema steward · Architecture steward · Docs steward · Directory Rules reviewer
created: 2026-06-24
updated: 2026-06-24
policy_label: public; contracts; schemas; compatibility; no-parallel-authority; schema-home-guard
tags: [kfm, contracts, schemas, README, compatibility, schema-home, no-parallel-authority, contract-schema-policy-split, directory-rules]
related:
  - ../README.md
  - ../../schemas/README.md
  - ../../schemas/contracts/v1/
  - ../../policy/
  - ../../fixtures/
  - ../../tests/
  - ../../tools/validators/
  - ../../docs/architecture/contract-schema-policy-split.md
  - ./policy/README.md
notes:
  - "This file replaces a blank placeholder at `contracts/schemas/README.md`."
  - "Canonical schema home verified in this session is top-level `schemas/`, not `contracts/schemas/`."
  - "Contracts root documentation says `contracts/` owns semantic meaning and does not contain JSON Schema or executable validation."
  - "Schemas root documentation says `schemas/` owns machine-checkable shape and excludes semantic prose, policy rules, data, and code."
  - "This README is a guard/pointer only; it must not become a schema root, contract root, policy root, fixture root, validator root, or public API/runtime authority."
  - "Rollback target for this replacement is previous blank blob SHA `8b137891791fe96927ad78e64b0aad7bded08bdc`."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# contracts/schemas

> Compatibility guard for the non-canonical `contracts/schemas/` path. JSON Schemas belong under [`../../schemas/`](../../schemas/). Human-readable semantic contracts belong under [`../`](../). This folder must not become a parallel schema authority.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Path: compatibility guard" src="https://img.shields.io/badge/path-compatibility__guard-lightgrey">
  <img alt="Canonical schema home: schemas" src="https://img.shields.io/badge/canonical__schema-schemas-blue">
  <img alt="Contracts: meaning only" src="https://img.shields.io/badge/contracts-meaning__only-blueviolet">
  <img alt="Posture: no parallel authority" src="https://img.shields.io/badge/posture-no__parallel__authority-critical">
</p>

**Status:** draft compatibility guard  
**Path:** `contracts/schemas/README.md`  
**Canonical schema home:** `schemas/` and `schemas/contracts/v1/`  
**Semantic contract home:** `contracts/`  
**Executable policy home:** `policy/`  
**Validator home:** `tools/validators/` or accepted validator roots  
**Truth posture:** CONFIRMED placeholder was blank · CONFIRMED `contracts/` owns semantic meaning and excludes JSON Schema/executable validation · CONFIRMED `schemas/` owns machine-checkable shape and excludes semantic prose/policy/data/code · CONFIRMED architecture split keeps meaning, shape, admissibility, and proof separate · PROPOSED compatibility guard until this non-canonical path is removed or migrated by steward decision

## Quick jumps

[Purpose](#purpose) · [Authority split](#authority-split) · [Accepted contents](#accepted-contents) · [Exclusions](#exclusions) · [Migration posture](#migration-posture) · [Validation checklist](#validation-checklist) · [Rollback](#rollback)

---

## Purpose

This README exists because the path `contracts/schemas/` exists, but the responsibility it appears to imply is not the accepted KFM responsibility split.

Use this path only as a temporary compatibility guard and navigation pointer.

Do not place JSON Schema files here. Do not place schema-family READMEs here. Do not place validators, fixtures, tests, policy rules, runtime code, or public API behavior here.

---

## Authority split

| Responsibility | Canonical / accepted home | Rule |
|---|---|---|
| Object meaning | `contracts/` | Markdown semantic contracts live under `contracts/`. |
| Machine-checkable shape | `schemas/` and `schemas/contracts/v1/` | JSON Schema and schema-family README files live under `schemas/`. |
| Policy rules / admissibility | `policy/` and policy-family roots | Executable policy belongs under policy roots. |
| Validators | `tools/validators/` or accepted validator roots | Executable validation belongs outside contracts. |
| Fixtures | `fixtures/` and accepted fixture roots | Examples/proof data stay outside contracts. |
| Tests | `tests/` and accepted test roots | Enforceability belongs in tests. |
| This path | `contracts/schemas/` | Compatibility guard only. |

---

## Accepted contents

Only conservative guard material belongs here:

| Accepted item | Purpose |
|---|---|
| `README.md` | Explain that this is not a schema home and point to canonical homes. |
| `MIGRATION.md` | Optional temporary plan to remove or redirect this path. |
| `BACKLINKS.md` | Optional backlink audit for stale links pointing to this path. |
| `VALIDATION_NOTES.md` | Optional note that schema content must live under `schemas/`. |

Any additional content should be temporary, pointer-only, and steward-reviewed.

---

## Exclusions

| Do not put this here | Correct home | Reason |
|---|---|---|
| `*.schema.json` files | `schemas/` and `schemas/contracts/v1/` | Prevents parallel schema authority. |
| Schema-family READMEs | `schemas/` and descendants | Keeps schema documentation with schema root. |
| Semantic contracts | `contracts/<family>/` | Contracts are already organized by object family. |
| Rego/OPA/policy source | `policy/` | Policy owns admissibility. |
| Validators | `tools/validators/` or accepted validator roots | Executable validation belongs outside contracts. |
| Fixtures | `fixtures/` | Fixtures are examples/proof data, not contracts. |
| Tests | `tests/` | Tests prove behavior. |
| Runtime/API/UI behavior | app/UI/web/runtime roots | Public surfaces are downstream. |

---

## Migration posture

Preferred future state:

```text
contracts/schemas/README.md     # removed or retained only as compatibility guard
contracts/                      # semantic contracts
schemas/                        # machine-checkable schemas
policy/                         # executable policy rules/bundles
fixtures/                       # examples/proof data
tests/                          # enforceability
```

Before deleting this guard, check for stale backlinks that still point to `contracts/schemas/`.

---

## Validation checklist

- [ ] Verify no JSON Schema files are added under `contracts/schemas/`.
- [ ] Verify object contracts remain under `contracts/<family>/`.
- [ ] Verify JSON Schemas remain under `schemas/` and `schemas/contracts/v1/`.
- [ ] Verify policy rules remain under `policy/`.
- [ ] Verify validators remain under `tools/validators/` or accepted validator roots.
- [ ] Search for stale references to `contracts/schemas/` before deletion or migration.
- [ ] If this path persists, keep it pointer-only and mark it compatibility/guard status.

---

## Rollback

Rollback is required if this path is used as a canonical schema root, schema-family README root, policy contract root, executable policy authority, fixture/test home, validator home, runtime/API authority, or public-client permission surface.

Rollback target for this replacement: previous blank blob SHA `8b137891791fe96927ad78e64b0aad7bded08bdc`.

<p align="right"><a href="#top">Back to top</a></p>
