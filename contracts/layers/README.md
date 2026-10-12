<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-layers-readme
title: contracts/layers — Layer Semantic Contract Compatibility README
type: readme
version: v0.1
status: draft
owners: OWNER_TBD — Layer steward · Contract steward · Data steward · UI steward · Evidence steward · Policy steward · Release steward · Docs steward · Directory Rules reviewer
created: 2026-06-24
updated: 2026-06-24
policy_label: public-with-gates; contracts; layers; semantic-contracts; compatibility; map-first; renderer-boundary; release-gated; schema-home-conflicted
related:
  - ../README.md
  - ../data/layer_manifest.md
  - ../data/layer_descriptor.md
  - ../data/layer_catalog_item.md
  - ../../docs/architecture/ui/LAYERING.md
  - ../../docs/architecture/map-master/LAYER_LIFECYCLE.md
  - ../../docs/architecture/map-shell.md
  - ../../docs/architecture/ui/MAP_RUNTIME_BOUNDARY.md
  - ../../docs/architecture/contract-schema-policy-split.md
  - ../../docs/standards/MAP_TRUST_STATES.md
  - ../../docs/standards/OGC-API-TILES.md
  - ../../schemas/contracts/v1/layers/
  - ../../schemas/contracts/v1/data/
  - ../../policy/layers/
  - ../../policy/data/
  - ../../tests/fixtures/layers/
  - ../../data/registry/layers/
  - ../../data/published/layers/
  - ../../release/
tags: [kfm, contracts, layers, layer-manifest, layer-descriptor, layer-catalog-item, maplibre, map-first, renderer-boundary, evidence-bundle, policy-decision, release-manifest, rollback, schema-home-conflicted]
notes:
  - "Directory README for the `contracts/layers/` compatibility/orientation path."
  - "Layer object contracts currently verified in this session live under `contracts/data/` (`layer_manifest.md`, `layer_descriptor.md`, `layer_catalog_item.md`); UI layering doctrine proposes a `schemas/contracts/v1/layers/` schema home."
  - "This README preserves the schema/contract placement conflict instead of treating the requested path as resolved canonical authority."
  - "A layer is a derived surface and renderer boundary carrier, not source truth, policy approval, release approval, EvidenceBundle, AI output, or runtime implementation."
  - "Previous file content was a short stub; rollback target is blob SHA `5a9510af8c9a4386a5d738788c63697627ad0ee5`."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# contracts/layers

> Compatibility and orientation README for KFM layer semantic contracts: layer catalog items, renderer-facing descriptors, layer manifests, legends, tile/asset manifests, and map-trust carriers that remain downstream of evidence, policy, review, release, correction, and rollback.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: contracts" src="https://img.shields.io/badge/root-contracts-blue">
  <img alt="Family: layers" src="https://img.shields.io/badge/family-layers-0a7ea4">
  <img alt="Authority: semantic meaning" src="https://img.shields.io/badge/authority-semantic__meaning-blueviolet">
  <img alt="Schema home: conflicted" src="https://img.shields.io/badge/schema__home-CONFLICTED-red">
  <img alt="Renderer: downstream" src="https://img.shields.io/badge/renderer-downstream__of__trust-green">
</p>

**Status:** draft compatibility/orientation README  
**Owners:** `OWNER_TBD` — Layer steward · Contract steward · Data steward · UI steward · Evidence steward · Policy steward · Release steward · Docs steward · Directory Rules reviewer  
**Path:** `contracts/layers/README.md`  
**Verified adjacent contracts:** `contracts/data/layer_manifest.md`, `contracts/data/layer_descriptor.md`, `contracts/data/layer_catalog_item.md`  
**Truth posture:** CONFIRMED stub replaced · CONFIRMED layer contracts exist under `contracts/data/` · CONFIRMED UI layering doctrine proposes `schemas/contracts/v1/layers/` · CONFLICTED schema/contract home until ADR or migration resolves it

## Quick jumps

[Scope](#scope) · [Repo fit](#repo-fit) · [Current contract surface](#current-contract-surface) · [Object family meanings](#object-family-meanings) · [Anti-collapse rules](#anti-collapse-rules) · [Accepted inputs](#accepted-inputs) · [Exclusions](#exclusions) · [Layer trust rules](#layer-trust-rules) · [Migration checklist](#migration-checklist) · [Rollback](#rollback)

---

## Scope

`contracts/layers/` is a compatibility and orientation path for layer-related semantic contracts.

It exists because KFM has two inspected layer placement signals:

1. object-level semantic contracts for `LayerManifest` and `LayerDescriptor` are currently under `contracts/data/`; and
2. UI layering doctrine names a proposed `schemas/contracts/v1/layers/` schema family and describes layer objects as a map-shell object family.

This README must not pretend that the conflict is solved. Until an ADR or migration resolves the contract/schema home, this path should be used as a **lane guide and compatibility pointer**, not as an uncontrolled duplicate of the `contracts/data/` layer contracts.

> [!IMPORTANT]
> A KFM layer is a derived map/display surface. It can carry release, proof, policy, rights, freshness, sensitivity, and rollback references at point of use, but it is not source truth, not an EvidenceBundle, not policy, not release approval, not a tile renderer, and not an AI answer.

---

## Repo fit

| Responsibility | Expected or related path | Relationship to this README |
|---|---|---|
| Contracts root | [`../README.md`](../README.md) | Defines semantic contract meaning and separates schemas, policy, validation, and source data. |
| Layer compatibility/orientation path | `contracts/layers/` | This directory; does not resolve schema/contract home conflict alone. |
| Verified layer manifest contract | [`../data/layer_manifest.md`](../data/layer_manifest.md) | Current semantic contract for governed layer-version manifests. |
| Verified layer descriptor contract | [`../data/layer_descriptor.md`](../data/layer_descriptor.md) | Current semantic contract for renderer-facing layer descriptors. |
| Verified layer catalog item contract | `../data/layer_catalog_item.md` | Current catalog/discovery companion; not reverified in this task. |
| UI layer doctrine | `../../docs/architecture/ui/LAYERING.md` | Defines layer doctrine and proposed `schemas/contracts/v1/layers/` homes. |
| Machine schemas — proposed layer home | `../../schemas/contracts/v1/layers/` | PROPOSED by UI layering doctrine; not verified as canonical. |
| Machine schemas — current data home | `../../schemas/contracts/v1/data/` | Current paired schema home named by inspected layer contracts; conflict remains. |
| Layer policy | `../../policy/layers/`, `../../policy/data/` | Admissibility and layer trust gates; behavior NEEDS VERIFICATION. |
| Tests and fixtures | `../../tests/fixtures/layers/`, `../../fixtures/data/` | Proof and examples; not contract authority. |
| Layer registry | `../../data/registry/layers/` | Append-only layer registry; not contract prose. |
| Published artifacts | `../../data/published/layers/`, `../../data/published/pmtiles/`, `../../data/published/geoparquet/` | Released carriers; not semantic truth. |
| Release and rollback | `../../release/` | Promotion, manifests, correction, withdrawal, and rollback authority. |
| Runtime/UI code | `../../apps/`, `../../packages/`, `../../pipelines/` | Downstream rendering/execution; not semantic authority. |

---

## Current contract surface

| Object or lane | Current verified contract path | Meaning | Placement posture |
|---|---|---|---|
| `LayerManifest` | `contracts/data/layer_manifest.md` | Governed manifest for a versioned layer payload and its source-role, evidence, integrity, lifecycle, policy, review, release, freshness, sensitivity, correction, and rollback context. | CONFIRMED path; schema home CONFLICTED / NEEDS VERIFICATION. |
| `LayerDescriptor` | `contracts/data/layer_descriptor.md` | Renderer-facing descriptor boundary that lets an adapter reference a released or candidate layer while carrying trust references. | CONFIRMED path; schema home CONFLICTED / NEEDS VERIFICATION. |
| `LayerCatalogItem` | `contracts/data/layer_catalog_item.md` | Catalog/list metadata companion for discovery and trust badges. | Search-confirmed; not re-fetched in this task. |
| `LegendDescriptor` | PROPOSED | Evidence-aware legend semantics: classes, ramps, units, trust state, scale dependencies, and sensitivity constraints. | PROPOSED. |
| `StyleManifest` | PROPOSED | Style, sprites, glyphs, class styling, sensitive styling constraints, and renderer-safe presentation. | PROPOSED. |
| `TileArtifactManifest` | PROPOSED | PMTiles, MVT, COG, GeoParquet, 3D Tiles, or related asset digest/signature semantics. | PROPOSED. |
| `MapReleaseManifest` | `release/` family | Binds layer, style, tile assets, evidence, policy, promotion, and rollback. | Release root; not this folder. |

---

## Object family meanings

Layer contracts may define meanings for:

- **catalog discovery** — what a user or API can see about an available layer;
- **renderer handoff** — what a MapLibre or map adapter may safely render;
- **layer manifesting** — what exact version of a layer payload exists and what it is backed by;
- **legend and style safety** — what symbology means and whether it exposes sensitive precision;
- **tile/asset integrity** — which artifacts were built, signed, checked, released, superseded, corrected, or withdrawn;
- **feature interaction trust** — what happens when a user selects a feature and requests an EvidenceBundle, Evidence Drawer view, export, or Focus Mode handoff.

All of those meanings remain downstream of evidence and policy. None of them create underlying domain truth.

---

## Anti-collapse rules

| Do not collapse layers into | Why |
|---|---|
| Source data | Layers are derived carriers, not RAW or canonical source records. |
| EvidenceBundle | Layers may reference EvidenceBundle; they are not proof closure. |
| SourceDescriptor | Layers may cite sources; they do not define source identity, rights, cadence, or authority. |
| PolicyDecision | Layer meaning does not decide allow/deny/restrict/abstain. |
| ReleaseManifest | A layer manifest/descriptor is not publication approval by itself. |
| Renderer implementation | MapLibre style/source config is downstream execution, not semantic authority. |
| Public tile artifact | PMTiles, COG, GeoParquet, MVT, or 3D Tiles are emitted carriers, not contracts. |
| AI answer | Generated language can explain released layer evidence but cannot create evidence or release state. |
| Domain object truth | Flora, fauna, geology, hydrology, hazards, people, settlement, and other domains own their object meanings. |

---

## Accepted inputs

Until the placement conflict is resolved, durable content under `contracts/layers/` should be conservative:

| Accepted item | Purpose | Required posture |
|---|---|---|
| `README.md` | Compatibility/orientation guide and migration boundary. | Accepted. |
| Short migration notes | Explain movement between `contracts/data/` and `contracts/layers/` if an ADR selects a home. | Temporary; preserve rollback. |
| Backlink audit notes | List inbound references to old layer contract paths during cleanup. | Temporary. |
| Future layer object contracts | Only after ADR/migration confirms this path as canonical. | PROPOSED until schema/policy/test-linked. |

---

## Exclusions

| Do not put this here | Correct home | Reason |
|---|---|---|
| RAW, WORK, QUARANTINE, PROCESSED, CATALOG, or PUBLISHED data | `../../data/<phase>/...` | Lifecycle data is not contract meaning. |
| PMTiles, COG, GeoParquet, MVT, 3D Tiles, sprites, glyphs, or style JSON artifacts | `../../data/published/`, style/runtime roots | Emitted carriers and runtime assets are not contracts. |
| JSON Schema | `../../schemas/contracts/v1/layers/` or `../../schemas/contracts/v1/data/` after ADR | Schemas own machine shape. |
| Policy rules | `../../policy/layers/`, `../../policy/data/`, `../../policy/sensitivity/` | Policy owns admissibility and exposure. |
| Fixtures, validators, tests | `../../fixtures/`, `../../tests/`, `../../tools/validators/` | Proof and execution live outside contracts. |
| Release manifests, rollback cards, correction notices | `../../release/` | Publication is a governed state transition. |
| Map UI code, adapters, SDKs, pipelines | `../../apps/`, `../../packages/`, `../../pipelines/` | Runtime delivery is downstream of contracts. |

---

## Layer trust rules

Minimum rules for any KFM layer surface:

- the renderer is downstream of trust, never upstream of it;
- every public or semi-public layer must point to release, evidence, policy, freshness, rights, sensitivity, review, correction, and rollback support;
- unresolved EvidenceRef, missing PolicyDecision, missing release state, stale/degraded freshness, unclear rights, or sensitive exposure should surface as `ABSTAIN`, `DENY`, `ERROR`, generalized output, or withheld output according to policy;
- feature clicks must resolve through governed APIs, not direct canonical/internal stores;
- a layer can be visually persuasive and still not be authoritative;
- screenshots, exports, legends, tiles, styles, cached vectors, and AI summaries are downstream carriers and must preserve trust state.

---

## Migration checklist

If `contracts/layers/` becomes canonical through ADR or migration:

- [ ] Decide whether `contracts/data/layer_manifest.md`, `contracts/data/layer_descriptor.md`, and `contracts/data/layer_catalog_item.md` move here or remain data-family contracts.
- [ ] Decide matching schema home: `schemas/contracts/v1/layers/` versus `schemas/contracts/v1/data/`.
- [ ] Preserve redirects or compatibility notes from old paths.
- [ ] Update docs, schema `$id`s, fixture paths, validator references, policy imports, and tests.
- [ ] Keep release, data registry, published artifacts, and runtime code out of contracts.
- [ ] Record the change in ADR / migration notes and rollback plan.
- [ ] Prove with tests that public UI and APIs still use governed released layer envelopes.

---

## Rollback

Rollback is required if this README is used to treat `contracts/layers/` as resolved canonical authority without ADR, or if layer contracts are used to bypass source evidence, policy, sensitivity, review, release, correction, or rollback gates.

Rollback target for this replacement: previous stub blob SHA `5a9510af8c9a4386a5d738788c63697627ad0ee5`.

<p align="right"><a href="#top">Back to top</a></p>
