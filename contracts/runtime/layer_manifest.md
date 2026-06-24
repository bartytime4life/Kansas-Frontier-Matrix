<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-runtime-layer-manifest-compat
title: contracts/runtime/layer_manifest.md — Runtime LayerManifest Compatibility Pointer
type: contract-pointer
version: v0.1
status: draft; compatibility; scaffold-replaced; no-parallel-authority; schema-scaffold
owners: OWNER_TBD — Runtime steward · Layer steward · Data steward · Release steward · Contracts steward · Schema steward · Policy steward · Docs steward · Directory Rules reviewer
created: NEEDS VERIFICATION — file existed before compatibility rewrite
updated: 2026-06-24
policy_label: public; contracts; runtime; layer-manifest; compatibility; no-parallel-authority; governed-runtime; map-layer-boundary
tags: [kfm, contracts, runtime, layer-manifest, compatibility, pointer, data-layer-manifest, release-layer-manifest, schema-scaffold, no-parallel-authority, trust-membrane]
related:
  - ./README.md
  - ./runtime_response_envelope.md
  - ./decision_envelope.md
  - ../data/layer_manifest.md
  - ../data/layer_descriptor.md
  - ../data/layer_catalog_item.md
  - ../release/layer_manifest.md
  - ../release/release_manifest.md
  - ../release/map_release_manifest.md
  - ../../schemas/contracts/v1/runtime/layer_manifest.schema.json
  - ../../schemas/contracts/v1/data/layer_manifest.schema.json
  - ../../policy/runtime/
  - ../../policy/data/
  - ../../policy/release/
  - ../../docs/architecture/contract-schema-policy-split.md
notes:
  - "Compatibility pointer for the requested runtime `layer_manifest.md` path."
  - "The inspected canonical layer-manifest meaning lives at `contracts/data/layer_manifest.md`."
  - "The inspected release-side layer bridge lives at `contracts/release/layer_manifest.md`."
  - "The runtime schema at `schemas/contracts/v1/runtime/layer_manifest.schema.json` is a PROPOSED empty scaffold with `contract_doc: null`; it is not a mature paired schema."
  - "This file must not become a third LayerManifest authority or a runtime map-serving contract."
  - "Rollback target for this compatibility rewrite is previous scaffold blob SHA `05fc119d660e535b6984cd6d6a3c0106d39e6d8a`."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Runtime LayerManifest Compatibility Pointer

> Compatibility pointer for `contracts/runtime/layer_manifest.md`. The inspected canonical `LayerManifest` semantic contract is [`../data/layer_manifest.md`](../data/layer_manifest.md). The release-side bridge is [`../release/layer_manifest.md`](../release/layer_manifest.md). This runtime path must not become a third layer authority.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Path: compatibility" src="https://img.shields.io/badge/path-compatibility-lightgrey">
  <img alt="Canonical: data LayerManifest" src="https://img.shields.io/badge/canonical-data__LayerManifest-blue">
  <img alt="Release: bridge exists" src="https://img.shields.io/badge/release-bridge__exists-0a7ea4">
  <img alt="Runtime schema: scaffold" src="https://img.shields.io/badge/runtime__schema-scaffold-orange">
  <img alt="Posture: no parallel authority" src="https://img.shields.io/badge/posture-no__parallel__authority-critical">
</p>

**Status:** draft compatibility / scaffold replacement  
**Path:** `contracts/runtime/layer_manifest.md`  
**Canonical inspected layer contract:** [`../data/layer_manifest.md`](../data/layer_manifest.md)  
**Release-side layer bridge:** [`../release/layer_manifest.md`](../release/layer_manifest.md)  
**Runtime schema scaffold:** `schemas/contracts/v1/runtime/layer_manifest.schema.json`  
**Runtime schema maturity:** PROPOSED empty scaffold; `contract_doc: null`; no fields  
**Policy authority:** `policy/runtime/`, `policy/data/`, `policy/release/`, not this file  
**Runtime/API/map authority:** implementation/API/UI/map roots, not this file  
**Truth posture:** CONFIRMED runtime target scaffold replaced · CONFIRMED canonical data LayerManifest exists · CONFIRMED release bridge exists · CONFIRMED runtime schema is scaffold-only with no fields and no contract_doc · PROPOSED compatibility alias until ADR/steward review resolves whether runtime needs a separate layer-manifest object

## Quick jumps

[Purpose](#purpose) · [Why this is compatibility only](#why-this-is-compatibility-only) · [Repo fit](#repo-fit) · [Accepted changes here](#accepted-changes-here) · [Exclusions](#exclusions) · [Runtime boundary](#runtime-boundary) · [Validation checklist](#validation-checklist) · [Open questions](#open-questions) · [Rollback](#rollback)

---

## Purpose

This file exists to make the runtime `layer_manifest.md` path safe and unambiguous after it appeared as a planned/inventory-derived scaffold.

It points maintainers to the existing layer authority split:

```text
contracts/data/layer_manifest.md       # canonical inspected layer meaning
contracts/release/layer_manifest.md    # release-side layer bridge
contracts/runtime/layer_manifest.md    # this compatibility pointer
```

Any change to canonical layer meaning belongs in the data contract. Any change to release inclusion/publication semantics belongs in the release bridge. Runtime behavior belongs in implementation/API/UI/map roots and policy roots, not here.

---

## Why this is compatibility only

The runtime file started as a scaffold from a domain API-contract inventory. Current evidence shows:

- the data lane already defines `LayerManifest` as the governed manifest for a versioned layer payload;
- the release lane already defines a narrow bridge for layer participation in releases;
- the runtime schema for `layer_manifest` is an empty PROPOSED scaffold with no fields and `contract_doc: null`.

Therefore this runtime file should not claim canonical meaning. It should either remain a compatibility pointer or be removed/migrated by an accepted ADR.

---

## Repo fit

| Responsibility | Correct home | Relationship to this file |
|---|---|---|
| Canonical layer-manifest semantic meaning | `contracts/data/layer_manifest.md` | Inspected canonical layer contract. |
| Release-side layer inclusion semantics | `contracts/release/layer_manifest.md` | Inspected release bridge. |
| Runtime layer-manifest compatibility path | `contracts/runtime/layer_manifest.md` | This pointer; not canonical. |
| Runtime schema scaffold | `schemas/contracts/v1/runtime/layer_manifest.schema.json` | Empty scaffold; no contract_doc; not mature shape authority. |
| Data layer schema | `schemas/contracts/v1/data/layer_manifest.schema.json` | Current inspected data-layer schema home, with known maturity/conflict notes. |
| Runtime policy | `policy/runtime/` | Runtime admissibility/rule behavior. |
| Data/release policy | `policy/data/`, `policy/release/` | Layer/release admissibility. |
| Runtime/API/map implementation | accepted app/package/UI/map roots | Execution/rendering behavior. |
| Release artifacts | `release/` | Release records/artifacts; not contracts. |

---

## Accepted changes here

Only conservative compatibility maintenance belongs here:

| Accepted change | Purpose |
|---|---|
| Update links to canonical data/release contracts | Keep stale runtime references navigable. |
| Add migration note | Explain future move, deletion, or canonicalization. |
| Add backlink audit | Find stale links to runtime layer-manifest path. |
| Add validation note | Track schema scaffold/drift without defining a new schema. |

Do not add layer field semantics here. Put layer meaning in [`../data/layer_manifest.md`](../data/layer_manifest.md) unless an accepted ADR changes the canonical home.

---

## Exclusions

| Do not put this here | Correct home | Reason |
|---|---|---|
| Canonical LayerManifest fields | `contracts/data/layer_manifest.md` | Avoids duplicate layer authority. |
| Release layer fields | `contracts/release/layer_manifest.md` | Release bridge already exists. |
| Runtime schema fields | `schemas/contracts/v1/runtime/layer_manifest.schema.json` or accepted schema home | Schemas own shape. |
| Map/layer payloads | lifecycle/release artifact roots | Contracts do not store data. |
| Runtime/API/map code | apps/packages/UI/map roots | Runtime implementation belongs outside contracts. |
| Policy rules | `policy/runtime/`, `policy/data/`, `policy/release/` | Policy owns admissibility. |
| Proofs, receipts, validation reports | accepted proof/receipt/test roots | Audit artifacts remain separate. |

---

## Runtime boundary

Runtime surfaces may need to carry or reference layer state, but they should do so by referencing governed layer and release objects rather than redefining them.

A safe runtime path is:

```text
LayerManifest (data)
  -> release-side layer bridge / ReleaseManifest
  -> runtime envelope or response references released layer state
  -> public API/UI/map consumes governed released state
```

Public clients must not treat this compatibility pointer as permission to read raw, work, quarantine, unpublished, canonical/internal, or direct source-system layer stores.

---

## Validation checklist

- [ ] Decide whether the runtime `layer_manifest` path should be kept as compatibility, deleted, or formalized by ADR.
- [ ] If formalized, define why runtime needs a distinct layer object beyond data and release contracts.
- [ ] Resolve or remove `schemas/contracts/v1/runtime/layer_manifest.schema.json` scaffold.
- [ ] Ensure links to `contracts/data/layer_manifest.md` and `contracts/release/layer_manifest.md` remain valid.
- [ ] Verify no runtime/public client uses this file as API permission or layer truth.
- [ ] Verify schema/policy/runtime implementation uses governed released layer refs, not duplicate semantics.

---

## Open questions

- Should `contracts/runtime/layer_manifest.md` remain as a compatibility pointer only?
- Should the runtime schema scaffold be deleted, redirected, or given an explicit compatibility status?
- Should runtime responses reference `LayerManifest` by id, `ReleaseManifest` contents, or `MapReleaseManifest` contents?
- Which runtime envelope carries layer state safely to map/UI clients?

---

## Rollback

Rollback is required if this file is used as canonical layer meaning, release approval, runtime map-serving permission, schema authority, policy authority, artifact storage, or public API/UI/map/AI truth.

Rollback target for this compatibility rewrite: previous scaffold blob SHA `05fc119d660e535b6984cd6d6a3c0106d39e6d8a`.

<p align="right"><a href="#top">Back to top</a></p>
