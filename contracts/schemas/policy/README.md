<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-schemas-policy-readme
title: contracts/schemas/policy — Policy Schema Compatibility Guard README
type: readme
version: v0.1
status: draft; compatibility-guard; parallel-schema-authority-blocker; no-canonical-schema-home
owners: OWNER_TBD — Contracts steward · Schema steward · Policy steward · Docs steward · Directory Rules reviewer
created: 2026-06-24
updated: 2026-06-24
policy_label: public; contracts; schemas; policy; compatibility; no-parallel-authority; schema-home-guard
tags: [kfm, contracts, schemas, policy, README, compatibility, schema-home, no-parallel-authority, contract-schema-policy-split]
related:
  - ../../README.md
  - ../../policy/README.md
  - ../../../schemas/contracts/v1/policy/README.md
  - ../../../schemas/contracts/v1/policy/
  - ../../../policy/
  - ../../../fixtures/contracts/v1/policy/
  - ../../../tests/contracts/policy/
  - ../../../docs/architecture/contract-schema-policy-split.md
notes:
  - "This file replaces a blank placeholder at `contracts/schemas/policy/README.md`."
  - "Canonical policy schema home verified in this session is `schemas/contracts/v1/policy/`, not `contracts/schemas/policy/`."
  - "Contracts root documentation says `contracts/` owns semantic meaning and does not contain JSON Schema or executable validation."
  - "Policy contracts root documentation says machine schemas belong under `schemas/contracts/v1/policy/` and executable policy belongs under `policy/`."
  - "This README is a guard/pointer only; it must not become a schema root, policy-contract root, policy-rule root, fixture root, validator root, or public API/runtime authority."
  - "Rollback target for this replacement is previous blank blob SHA `8b137891791fe96927ad78e64b0aad7bded08bdc`."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# contracts/schemas/policy

> Compatibility guard for the non-canonical `contracts/schemas/policy/` path. Policy schemas belong under [`../../../schemas/contracts/v1/policy/`](../../../schemas/contracts/v1/policy/). Policy semantic contracts belong under [`../../policy/`](../../policy/). This folder must not become a parallel schema authority.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Path: compatibility guard" src="https://img.shields.io/badge/path-compatibility__guard-lightgrey">
  <img alt="Canonical schema home: schemas/contracts/v1/policy" src="https://img.shields.io/badge/canonical__schema-schemas%2Fcontracts%2Fv1%2Fpolicy-blue">
  <img alt="Contracts: meaning only" src="https://img.shields.io/badge/contracts-meaning__only-blueviolet">
  <img alt="Posture: no parallel authority" src="https://img.shields.io/badge/posture-no__parallel__authority-critical">
</p>

**Status:** draft compatibility guard  
**Path:** `contracts/schemas/policy/README.md`  
**Canonical policy schema home:** `schemas/contracts/v1/policy/`  
**Policy semantic contract home:** `contracts/policy/`  
**Executable policy home:** `policy/`  
**Truth posture:** CONFIRMED placeholder was blank · CONFIRMED contracts root owns meaning and excludes JSON Schema/executable validation · CONFIRMED policy contract README points machine schemas to `schemas/contracts/v1/policy/` · CONFIRMED canonical policy schema README exists at `schemas/contracts/v1/policy/README.md` · PROPOSED compatibility guard until this non-canonical path is removed or migrated by steward decision

## Quick jumps

[Purpose](#purpose) · [Authority split](#authority-split) · [Accepted contents](#accepted-contents) · [Exclusions](#exclusions) · [Migration posture](#migration-posture) · [Validation checklist](#validation-checklist) · [Rollback](#rollback)

---

## Purpose

This README exists because the path `contracts/schemas/policy/` exists, but the responsibility it appears to imply is not the accepted KFM responsibility split.

Use this path only as a temporary compatibility guard and navigation pointer.

Do not place JSON Schema files here. Do not place policy rules here. Do not place policy-object semantic contracts here.

---

## Authority split

| Responsibility | Canonical / accepted home | Rule |
|---|---|---|
| Policy object meaning | `contracts/policy/` | Markdown semantic contracts live under `contracts/`. |
| Policy object machine shape | `schemas/contracts/v1/policy/` | JSON Schema and schema-family READMEs live under `schemas/`. |
| Policy rules / admissibility | `policy/` and policy-family roots | Executable policy belongs under policy roots. |
| Policy runtime helpers | `packages/policy-runtime/` or accepted implementation roots | Runtime helpers do not own policy meaning or schema authority. |
| Fixtures | `fixtures/contracts/v1/policy/` and accepted fixture roots | Examples/proof data stay outside contracts. |
| Tests | `tests/contracts/policy/` and accepted policy test roots | Enforceability belongs in tests. |
| This path | `contracts/schemas/policy/` | Compatibility guard only. |

---

## Accepted contents

Only conservative guard material belongs here:

| Accepted item | Purpose |
|---|---|
| `README.md` | Explain that this is not a schema home and point to the canonical homes. |
| `MIGRATION.md` | Optional temporary plan to remove or redirect this path. |
| `BACKLINKS.md` | Optional backlink audit for stale links pointing to this path. |
| `VALIDATION_NOTES.md` | Optional note that schema content must live under `schemas/contracts/v1/policy/`. |

Any additional content should be temporary, pointer-only, and steward-reviewed.

---

## Exclusions

| Do not put this here | Correct home | Reason |
|---|---|---|
| `*.schema.json` files | `schemas/contracts/v1/policy/` | Prevents parallel schema authority. |
| Policy semantic contracts | `contracts/policy/` | Contracts are already organized by object family. |
| Rego/OPA/policy source | `policy/` | Policy rules own admissibility. |
| Validators | `tools/validators/` or accepted validator roots | Executable validation belongs outside contracts. |
| Fixtures | `fixtures/contracts/v1/policy/` | Fixtures are examples/proof data, not docs. |
| Tests | `tests/contracts/policy/` | Tests prove behavior. |
| Runtime envelopes | `contracts/runtime/` and runtime schemas | Runtime objects are not schema homes. |
| Public API/UI behavior | app/UI/web/runtime roots | Public surfaces are downstream. |

---

## Migration posture

Preferred future state:

```text
contracts/schemas/policy/README.md      # removed or retained only as compatibility guard
contracts/policy/                       # policy semantic contracts
schemas/contracts/v1/policy/            # policy JSON Schemas
policy/                                 # executable policy rules/bundles
```

Before deleting this guard, check for stale backlinks that still point to `contracts/schemas/policy/`.

---

## Validation checklist

- [ ] Verify no JSON Schema files are added under `contracts/schemas/policy/`.
- [ ] Verify policy object contracts remain under `contracts/policy/`.
- [ ] Verify policy schemas remain under `schemas/contracts/v1/policy/`.
- [ ] Verify policy rules remain under `policy/`.
- [ ] Search for stale references to `contracts/schemas/policy/` before deletion or migration.
- [ ] If this path persists, keep it pointer-only and mark it compatibility/guard status.

---

## Rollback

Rollback is required if this path is used as a canonical schema root, a policy contract root, executable policy authority, fixture/test home, validator home, runtime/API authority, or public-client permission surface.

Rollback target for this replacement: previous blank blob SHA `8b137891791fe96927ad78e64b0aad7bded08bdc`.

<p align="right"><a href="#top">Back to top</a></p>
