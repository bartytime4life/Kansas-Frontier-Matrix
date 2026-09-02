<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-source-source-descriptor-legacy-case
title: contracts/source/SOURCE_DESCRIPTOR.md — SourceDescriptor Legacy-Case Compatibility Pointer
type: contract-pointer
version: v0.1
status: draft; compatibility; legacy-case-alias; scaffold-replaced; no-parallel-authority
owners: OWNER_TBD — Source steward · Contracts steward · Schema steward · Policy steward · Catalog steward · Docs steward · Directory Rules reviewer
created: NEEDS VERIFICATION — planned-path scaffold existed before compatibility rewrite
updated: 2026-06-24
policy_label: public; contracts; source; source-descriptor; compatibility; legacy-case; no-parallel-authority; source-role-anti-collapse
tags: [kfm, contracts, source, SOURCE_DESCRIPTOR, source_descriptor, compatibility, legacy-case, source-descriptor, source-role, rights, sensitivity, no-parallel-authority]
related:
  - ./README.md
  - ./source_descriptor.md
  - ../../docs/sources/SOURCE_DESCRIPTOR_STANDARD.md
  - ../../schemas/contracts/v1/source/source_descriptor.schema.json
  - ../../packages/source-registry/README.md
  - ../../data/registry/sources/
  - ../../policy/source/
  - ../../policy/rights/
  - ../../policy/sensitivity/
  - ../../docs/architecture/contract-schema-policy-split.md
notes:
  - "This file replaces a planned-path scaffold at `contracts/source/SOURCE_DESCRIPTOR.md`."
  - "The canonical inspected source descriptor contract is the lowercase path `contracts/source/source_descriptor.md`."
  - "The inspected source descriptor schema names `contracts/source/source_descriptor.md` as `x-kfm.contract_doc`."
  - "The uppercase path is retained as a compatibility pointer for inventory/domain references only."
  - "This file must not become a second SourceDescriptor contract, schema authority, source-registry record, policy rule, validator, fixture, release decision, or source truth."
  - "Rollback target for this compatibility rewrite is previous scaffold blob SHA `c311f4b5601afc07ca64944475c431f4c842ae9d`."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# SOURCE_DESCRIPTOR Compatibility Pointer

> Compatibility pointer for the legacy-case path `contracts/source/SOURCE_DESCRIPTOR.md`. The inspected canonical SourceDescriptor contract is [`./source_descriptor.md`](./source_descriptor.md). This file exists to prevent stale uppercase references from becoming a parallel source-governance authority.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Path: compatibility" src="https://img.shields.io/badge/path-compatibility-lightgrey">
  <img alt="Canonical: source_descriptor.md" src="https://img.shields.io/badge/canonical-source__descriptor.md-blue">
  <img alt="Schema: paired to lowercase" src="https://img.shields.io/badge/schema-paired__to__lowercase-green">
  <img alt="Posture: no parallel authority" src="https://img.shields.io/badge/posture-no__parallel__authority-critical">
</p>

**Status:** draft compatibility / legacy-case alias  
**Path:** `contracts/source/SOURCE_DESCRIPTOR.md`  
**Canonical inspected contract:** `contracts/source/source_descriptor.md`  
**Paired schema:** `schemas/contracts/v1/source/source_descriptor.schema.json`  
**Schema-declared contract doc:** `contracts/source/source_descriptor.md`  
**Policy homes:** `policy/source/`, `policy/rights/`, `policy/sensitivity/`  
**Truth posture:** CONFIRMED this path was a planned-path scaffold · CONFIRMED canonical lowercase contract exists · CONFIRMED source descriptor schema exists and points to the lowercase contract doc · CONFIRMED source README treats `contracts/source/` as semantic meaning only · PROPOSED compatibility alias until backlinks are migrated or the path is removed by steward decision

## Quick jumps

[Purpose](#purpose) · [Why this is compatibility only](#why-this-is-compatibility-only) · [Authority split](#authority-split) · [Accepted contents](#accepted-contents) · [Exclusions](#exclusions) · [Migration posture](#migration-posture) · [Validation checklist](#validation-checklist) · [Rollback](#rollback)

---

## Purpose

This file exists because an uppercase planned path was referenced by domain inventory material:

```text
contracts/source/SOURCE_DESCRIPTOR.md
```

Current repo evidence points canonical SourceDescriptor meaning to:

```text
contracts/source/source_descriptor.md
```

Use this uppercase path only as a compatibility pointer. Do not add or maintain canonical field semantics here.

---

## Why this is compatibility only

The uppercase path started as an inventory-derived scaffold. The lowercase `source_descriptor.md` already defines the source descriptor contract, and the source descriptor schema names the lowercase path as its contract document.

Keeping canonical content in both files would create two source-governance authorities. That would weaken source-role anti-collapse, rights review, sensitivity review, citation duties, and source-admission auditability.

---

## Authority split

| Responsibility | Correct home | Rule |
|---|---|---|
| SourceDescriptor semantic meaning | `contracts/source/source_descriptor.md` | Canonical inspected contract. |
| Uppercase legacy-case pointer | `contracts/source/SOURCE_DESCRIPTOR.md` | This file; compatibility only. |
| Source contract family README | `contracts/source/README.md` | Lane boundary and maintainer rules. |
| Machine shape | `schemas/contracts/v1/source/source_descriptor.schema.json` or accepted successor | JSON Schema owns field shape. |
| Source admission / rights / sensitivity policy | `policy/source/`, `policy/rights/`, `policy/sensitivity/` | Policy owns allow/deny/restrict/abstain behavior. |
| Source registry records | `data/registry/sources/` or accepted registry roots | Registry records are not contract prose. |
| Source registry helper code | `packages/source-registry/` or accepted implementation roots | Implementation must not own source truth. |
| Fixtures/tests/validators | `fixtures/`, `tests/`, `tools/validators/` | Proof and execution stay separate. |
| Release/correction/rollback | `release/` and release contract/release roots | Publication and rollback are governed transitions. |

---

## Accepted contents

Only conservative compatibility material belongs here:

| Accepted item | Purpose |
|---|---|
| Pointer to `./source_descriptor.md` | Direct stale references to canonical meaning. |
| Backlink/migration notes | Help remove uppercase references safely. |
| ADR pointer | Explain accepted decision if uppercase path is retained or removed. |

No source fields, schema fragments, policy rules, fixture examples, or source registry records should be added here.

---

## Exclusions

| Do not put this here | Correct home | Reason |
|---|---|---|
| SourceDescriptor field semantics | `contracts/source/source_descriptor.md` | Avoids duplicate contract authority. |
| JSON Schema | `schemas/contracts/v1/source/` or successor | Schemas own shape. |
| SourceDescriptor JSON records | `data/registry/sources/` or accepted registry roots | Contracts do not store source registry records. |
| Source admission, rights, sensitivity policy | `policy/source/`, `policy/rights/`, `policy/sensitivity/` | Policy owns admissibility. |
| Source resolver code | `packages/source-registry/`, connectors, tools, pipelines | Implementation belongs outside contracts. |
| Fixtures/tests/validators | `fixtures/`, `tests/`, `tools/validators/` | Enforceability and execution stay separate. |
| Release manifests or correction records | `release/` roots | Release and correction state remain separate. |
| Public claims or AI summaries | governed evidence/runtime/API roots | EvidenceBundle and released state outrank generated text. |

---

## Migration posture

Preferred future state:

```text
contracts/source/SOURCE_DESCRIPTOR.md    # removed or retained only as compatibility pointer
contracts/source/source_descriptor.md    # canonical SourceDescriptor contract
schemas/contracts/v1/source/            # source schema lane or accepted successor
policy/source/                          # source admission policy
```

Before deleting this pointer, search for stale references to `contracts/source/SOURCE_DESCRIPTOR.md`, especially in domain inventories and generated scaffolds.

---

## Validation checklist

- [ ] Verify no canonical SourceDescriptor content is added to this uppercase path.
- [ ] Verify `contracts/source/source_descriptor.md` remains the canonical semantic contract.
- [ ] Verify schemas point to the canonical lowercase contract or an accepted successor.
- [ ] Search for stale uppercase references before removal or migration.
- [ ] Verify public/runtime/catalog/AI consumers never use this pointer as source authority.
- [ ] Verify source-role, rights, sensitivity, and citation posture remain governed by SourceDescriptor records and policy gates.

---

## Rollback

Rollback is required if this path is used as canonical SourceDescriptor meaning, schema authority, policy authority, source registry record authority, validator home, fixture/test home, release approval, runtime/API permission, public claim truth, or AI source authority.

Rollback target for this compatibility rewrite: previous scaffold blob SHA `c311f4b5601afc07ca64944475c431f4c842ae9d`.

<p align="right"><a href="#top">Back to top</a></p>
