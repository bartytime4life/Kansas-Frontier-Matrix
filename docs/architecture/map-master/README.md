<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/architecture-map-master-readme
title: Map Master — Renderer Architecture
type: standard
version: v0.2
status: draft
owners: <ARCHITECTURE-DOCTRINE-OWNER> · <MAP-SURFACE-STEWARD> · NEEDS VERIFICATION
created: 2026-05-24
updated: 2026-05-24
policy_label: public
related:
  - directory-rules.md#7
  - directory-rules.md#12
  - Master_MapLibre_Components-Functions-Features_v2_1_FULL.md
  - Master_MapLibre_Components-Functions-Features_v2_1_FULL.md#10
  - Kansas_Frontier_Matrix_-_Domains_v1_1___Pass_23_32_Consolidated_Atlas.md#19
  - Kansas_Frontier_Matrix_-_Domains_v1_1___Pass_23_32_Consolidated_Atlas.md#2492
  - ai-build-operating-contract.md#22
  - kfm_unified_doctrine_synthesis.md#11
  - connected-dots-architecture-brief.md#8
  - docs/adr/ADR-0007-maplibre-is-the-sole-browser-renderer.md
  - docs/architecture/maplibre-3d.md
  - docs/architecture/governed-api/README.md
  - docs/architecture/governed-ai/ROUTE_MAP.md
  - docs/architecture/cross-domain/README.md
tags: [kfm, architecture, map-master, maplibre, maplibre-3d, single-renderer, renderer, tile-artifacts, trust-membrane]
notes:
  - v0.2 (2026-05-24) — Material revision. Renderer architecture realigned to a single MapLibre GL JS renderer (native + admitted plugin set) per ADR-0007 (PROPOSED). Multi-renderer framing removed throughout.
  - PROPOSED. Fourth folder pattern under docs/architecture/; same OPEN-DR-12 META family as cross-domain/, governed-ai/, governed-api/.
  - Canonical doctrinal anchor is the "Master MapLibre Components-Functions-Features" body of work (v1.4 → v2.0+ accumulating; CONFIRMED through v2.1). Category W entries that previously assumed multi-renderer artifacts/overlay-sync are flagged for refresh per ADR-0007 §11 step 4.
  - "Renderer is downstream of trust" posture preserved verbatim from Master MapLibre executive determinations across versions.
  - No mounted repo evidence in this session; all repo-shaped claims labeled PROPOSED.
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Map Master — Renderer Architecture

> *Architecture lane for the KFM map and renderer surface — **MapLibre GL JS** as the disciplined **sole** browser-side renderer for 2D, 2.5D, true-3D, globe, point-cloud, and visualization-overlay surfaces; PMTiles/MVT/COG as released artifact carriers; the Evidence Drawer as the click-to-truth resolution point. The renderer is downstream of trust; tiles, popups, screenshots, scenes, and AI answers are downstream carriers, never sovereign truth.*

![status](https://img.shields.io/badge/status-draft-yellow)
![doctrine](https://img.shields.io/badge/doctrine-CONFIRMED%20(spine)-blue)
![role](https://img.shields.io/badge/role-downstream%20renderer-success)
![renderer](https://img.shields.io/badge/renderer-MapLibre%20GL%20JS%20(sole)-blueviolet)
![aligned-with](https://img.shields.io/badge/aligned%20with-ADR--0007-blue)
![master-maplibre](https://img.shields.io/badge/Master%20MapLibre-v2.1%2B%20cumulative-informational)
![path-status](https://img.shields.io/badge/path-PROPOSED-orange)
![open-dr-12](https://img.shields.io/badge/OPEN--DR--12-family-orange)
![ci](https://img.shields.io/badge/CI-TODO-lightgrey)

**Status:** draft · **Doc version:** v0.2 · **Owners:** `<ARCHITECTURE-DOCTRINE-OWNER>` · `<MAP-SURFACE-STEWARD>` *(NEEDS VERIFICATION)* · **Last updated:** 2026-05-24

> [!IMPORTANT]
> **Core determination — verbatim from doctrine.** *"MapLibre remains a downstream renderer and interaction runtime. Tiles, PMTiles, MVT, MLT, COGs, style JSON, sprites, glyphs, popups, screenshots, Story Nodes, 3D scenes, graph projections, catalog records, and AI answers remain downstream carriers, not sovereign truth."* *(`Master_MapLibre_Components-Functions-Features_v2.1_FULL.md`, **CONFIRMED** across executive determinations from v1.4 onward.)*

> [!IMPORTANT]
> **Single-renderer commitment (per ADR-0007, PROPOSED).** MapLibre GL JS is KFM's **default and sole** browser-side renderer. Every 2D, 2.5D, true-3D, globe, point-cloud, and visualization-overlay surface lives inside MapLibre's API surface — native capabilities plus an explicitly admitted plugin set governed by a `PluginAdmission` PolicyDecision. The prior dual-renderer card `KFM-P2-FEAT-0012` is **superseded** by ADR-0007. Any introduction of a browser-side rendering technology beyond the admitted plugin set requires an accepted **exception-ADR**.

> [!CAUTION]
> **Path placement diverges from Directory Rules v1.2 §12 — same OPEN-DR-12 family.** This is the **fourth** folder pattern under `docs/architecture/` *(after `cross-domain/`, `governed-ai/`, `governed-api/`)*. The systemic divergence is consolidated in **OPEN-DR-12 (PROPOSED META amendment)** — see [`docs/architecture/governed-api/README.md` §2.2](../governed-api/README.md). Resolution lands once; this folder is one more application of the same pattern.

> [!NOTE]
> **What this README is and is not.** It is the **architectural landing** for the map / renderer lane — orientation, scope, sibling map. It is **not** the canonical authority for any one map-surface concept *(that is the Master MapLibre document)*; **not** the canonical decision for sole-renderer status *(that is [`docs/adr/ADR-0007-maplibre-is-the-sole-browser-renderer.md`](../../adr/ADR-0007-maplibre-is-the-sole-browser-renderer.md), PROPOSED)*; **not** the route inventory *(that is [`ROUTE_MAP.md`](../governed-ai/ROUTE_MAP.md))*; **not** schemas, policies, or app code. It points to them and consolidates the architecture view.

---

## Table of contents

1. [Scope](#1-scope)
2. [Repo fit — OPEN-DR-12 family](#2-repo-fit--open-dr-12-family)
3. [The canonical posture — renderer is downstream of trust](#3-the-canonical-posture--renderer-is-downstream-of-trust)
4. [The seven negative authorities](#4-the-seven-negative-authorities)
5. [Relationship to other architecture lanes](#5-relationship-to-other-architecture-lanes)
6. [The click-to-truth flow](#6-the-click-to-truth-flow)
7. [Map object families](#7-map-object-families)
8. [2D default · 3D conditional · tile artifact discipline](#8-2d-default--3d-conditional--tile-artifact-discipline)
9. [Viewer-side verification fails closed · UI negative states](#9-viewer-side-verification-fails-closed--ui-negative-states)
10. [Reality Boundary Note — synthetic vs observed](#10-reality-boundary-note--synthetic-vs-observed)
11. [What lives here · What does not live here](#11-what-lives-here--what-does-not-live-here)
12. [Directory tree (PROPOSED)](#12-directory-tree-proposed)
13. [Anti-patterns](#13-anti-patterns)
14. [Open questions and ADR triggers](#14-open-questions-and-adr-triggers)
15. [Related docs](#15-related-docs)
16. [Appendix — glossary and reference](#16-appendix--glossary-and-reference)

---

## 1. Scope

This lane covers the **map and renderer surface as an architectural concern** — every aspect of how KFM presents released, governed evidence on a 2D plan view, a 3D terrain or globe view, or a hybrid surface, **all rendered by MapLibre GL JS** (native APIs + the admitted plugin set). The lane covers:

- **Renderer discipline** — what MapLibre is and is not allowed to do; what an admitted plugin is and is not.
- **Tile and artifact lifecycle** — PMTiles, MVT, COG, MBTiles, Zarr; release manifests, sidecars, BAO proofs, signatures.
- **The Evidence Drawer** — the canonical click-to-truth resolution point on the map.
- **Cross-mode parity (2D ↔ 3D / globe)** — when each mode is admissible and how all modes preserve evidence identity across one renderer.
- **UI negative states** — `MISSING_EVIDENCE`, `SOURCE_STALE`, `DENIED_BY_POLICY`, etc.
- **Performance budgets** — runtime probes, mobile-first tile playbook, decode/heap budgets.
- **Plugin admission** — the `PluginAdmission` PolicyDecision that gates every non-native rendering path *(per ADR-0007 §3.2 / §3.4)*.

> [!TIP]
> **When to read this lane.** Read it when your change touches the map shell, tile pipeline, style discipline, cross-mode parity, viewer-side verification, plugin admission, or Evidence Drawer rendering. Per-route work *(governed-API contract for a tile endpoint, AI surface behavior, cross-lane invariants)* lives in the other architecture lanes.

[↑ Back to top](#top)

---

## 2. Repo fit — OPEN-DR-12 family

### 2.1 Four folder patterns under `docs/architecture/`

| # | Folder | Introduced | Status |
|---|---|---|---|
| 1 | `docs/architecture/cross-domain/` | Earlier session *(README)* | OPEN-DR-10 *(rolled into OPEN-DR-12)* |
| 2 | `docs/architecture/governed-ai/` | Earlier session *(3 siblings — BOUNDARIES, CONTINUITY_NOTES, ROUTE_MAP)* | OPEN-DR-11 *(rolled into OPEN-DR-12; 3-sibling threshold reached)* |
| 3 | `docs/architecture/governed-api/` | Earlier session *(README + 6 PROPOSED siblings)* | OPEN-DR-12 *(META amendment proposed)* |
| 4 | `docs/architecture/map-master/` *(this lane)* | This turn *(README + PROPOSED siblings)* | OPEN-DR-12 family |

Four folders, one systemic question. **OPEN-DR-12 (PROPOSED META amendment)** consolidates all four; filing per-folder OPEN-DRs is no longer productive.

### 2.2 What this README assumes

Pending OPEN-DR-12, this README **assumes the folder pattern will be accepted** *(because the systemic pattern argues for it, and this lane warrants multiple siblings — see §12)* but labels every sibling path PROPOSED so flattening remains reversible.

> [!IMPORTANT]
> **The case for the `map-master/` folder is straightforward.** The Master MapLibre document is itself a multi-hundred-page body of doctrine accumulated across versions *(v1.4 → v1.5 → v1.6 → v1.8 → v1.9 → v2.0 → v2.1+)*. The lane has a clearly enumerable set of sub-concerns *(renderer boundary, tile artifacts, layer lifecycle, Evidence Drawer, cross-mode parity, performance budgets, viewer verification, plugin admission)*. This satisfies **two of three** OPEN-DR-12 criteria for folder admission. See §12.

[↑ Back to top](#top)

---

## 3. The canonical posture — renderer is downstream of trust

> **Evidence basis:** `Master_MapLibre_Components-Functions-Features_v2.1_FULL.md` *(executive determinations preserved verbatim across v1.4–v2.0+)*; `Kansas_Frontier_Matrix_-_Domains_v1_1___Pass_23_32_Consolidated_Atlas.md` §19 *(Cross-Domain Systems)*; `ai-build-operating-contract.md` §22 *(map, UI, renderer contract)*; idea card `KFM-P1-FEAT-0039` *(MapLibre as downstream renderer)*; `docs/adr/ADR-0007-maplibre-is-the-sole-browser-renderer.md` *(PROPOSED — single-renderer commitment)*. **CONFIRMED doctrine throughout.**

The KFM map shell exists **inside** the trust membrane, never astride it.

| Direction | What flows | Authority |
|---|---|---|
| **Trust → renderer** | Released layers, tile artifacts, evidence bundles, evidence drawer payloads, Focus Mode envelopes — all **governed**, all **post-promotion**. | The governed API *(`apps/governed-api/`)* and `ReleaseManifest`. |
| **Renderer → trust** | User clicks, viewport state, time selections, feature IDs — bounded `MapContextEnvelope`. Receipts emitted by every consequential interaction. | The renderer carries no authority of its own; it carries context. |

> [!IMPORTANT]
> **The posture is unidirectional.** Public surfaces use **governed APIs, released artifacts, catalog records, tile services, `EvidenceBundle` resolution, and release manifests** *(`Master_MapLibre_Components-Functions-Features_v2.1_FULL.md` verbatim)*. The renderer does not author truth, does not register sources, does not run policy, does not validate citations, does not approve reviews, does not publish releases, does not generate AI answers.

> [!IMPORTANT]
> **One renderer, one trust membrane.** Per ADR-0007 (PROPOSED), MapLibre GL JS is the sole renderer; this means **one** `ViewState` model, **one** `CameraPath`, **one** `RepresentationReceipt` stream, **one** supply chain, **one** `PluginAdmission` surface, **one** reviewer burden. The single-renderer posture is what upholds evidence identity across all view modes by construction.

[↑ Back to top](#top)

---

## 4. The seven negative authorities

> **Evidence basis:** `Master_MapLibre_Components-Functions-Features_v2.1_FULL.md` *(executive determinations — verbatim seven-item list preserved across every version from v1.4 onward)*; `KFM-P1-FEAT-0039`. **CONFIRMED enumeration** *(not a synthesis; the list is doctrinal verbatim)*.

The Master MapLibre document explicitly enumerates **seven authorities** the renderer is **not**. The list appears verbatim, in this order, across every executive determination:

| # | Authority the renderer is NOT | What does carry that authority | If the renderer tried to | The DENY surface |
|---|---|---|---|---|
| 1 | **Canonical truth store** | `EvidenceBundle` + `ReleaseManifest` | Read from canonical/internal stores directly to render. | `apps/governed-api/`; layer manifest resolver. |
| 2 | **Source registry** | `SourceDescriptor` registry | Treat tile metadata as source provenance. | Source admission gate. |
| 3 | **Policy engine** | OPA/Rego policy under `policy/` | Apply visibility rules client-side as a substitute for `PolicyDecision`. | Policy precheck/postcheck. |
| 4 | **Citation authority** | `CitationValidationReport` | Treat a popup or feature label as a citation. | Focus Mode citation validator. |
| 5 | **Review authority** | Steward review via `apps/review-console/` | Mark a layer as "reviewed" through a UI toggle. | Review queue surface. |
| 6 | **Publication authority** | `ReleaseManifest` + release authority | Toggle visibility = release the layer. | Release queue; release authority. |
| 7 | **AI authority** | Focus Mode runtime *(governed)* | Render generated text as authoritative answer. | Focus Mode; AI surface steward. |

> [!CAUTION]
> **The seven are not negotiable.** A change that would let the renderer assume any of these roles is a contract-level violation and ADR-class *(per `directory-rules.md` §2.4)*. The seven are also the **anti-pattern register for this lane** — see §13.

[↑ Back to top](#top)

---

## 5. Relationship to other architecture lanes

```mermaid
flowchart TB
  subgraph ARCH["docs/architecture/  ✅ canonical (directory-rules §12)"]
    XD["cross-domain/<br/><i>cross-lane invariants</i>"]
    GAI["governed-ai/<br/><i>AI surface — spatial · temporal · structural</i>"]
    GAPI["governed-api/<br/><i>API surface as a whole</i>"]
    MM["map-master/  (this lane)<br/><i>map & renderer surface</i>"]
  end
  subgraph SURFACES["The four governed surfaces of KFM"]
    A["Data lifecycle<br/><i>(governed via cross-domain)</i>"]
    B["AI runtime<br/><i>(governed via governed-ai)</i>"]
    C["API endpoints<br/><i>(governed via governed-api)</i>"]
    D["Map / renderer<br/><i>(governed via map-master)</i>"]
  end
  XD -. governs .-> A
  GAI -. governs .-> B
  GAPI -. governs .-> C
  MM -. governs .-> D
  D -. consumes .-> C
  D -. embeds .-> B
  D -. respects .-> A
  classDef arch fill:#e1f5fe,stroke:#01579b;
  classDef surface fill:#c8e6c9,stroke:#1b5e20;
  class XD,GAI,GAPI,MM arch;
  class A,B,C,D surface;
```

| Lane | Owns | Relationship to `map-master/` |
|---|---|---|
| `docs/architecture/cross-domain/` | Cross-lane invariants *(source role, ownership, sensitivity, EvidenceBundle support)* | The map MUST preserve all four invariants at every render. The renderer is a consumer of cross-lane discipline, not its author. |
| `docs/architecture/governed-ai/` | AI surface — boundaries, continuity, route map for AI | Focus Mode is rendered **on the map**; the map embeds the AI surface but does not own it. AI-specific concerns live in `governed-ai/`; map-specific concerns *(how Focus Mode integrates with the Evidence Drawer, tile click flow, etc.)* live here. |
| `docs/architecture/governed-api/` | API surface as a whole — membrane, envelopes, audience classes, threat model | The map shell **consumes** the governed API; never bypasses it. `apps/explorer-web/` reads via `apps/governed-api/` only *(directory-rules §7.1)*. |
| **`docs/architecture/map-master/`** *(this lane)* | The map shell, renderer discipline, tile artifacts, Evidence Drawer, cross-mode parity, viewer-side verification, plugin admission. | This lane. |

> [!NOTE]
> **The four lanes together cover the four governed surfaces of KFM** — data lifecycle, AI runtime, API endpoints, map/renderer. A reviewer auditing the trust path end-to-end consults all four.

[↑ Back to top](#top)

---

## 6. The click-to-truth flow

> **Evidence basis:** `Master_MapLibre_Components-Functions-Features_v2.1_FULL.md` §10 *(Governance and Trust-Membrane Chapter)*; `ai-build-operating-contract.md` §22.1 *(click-to-truth path)*; `connected-dots-architecture-brief.md` §8.1. **CONFIRMED doctrine** *(flow preserved verbatim across carriers)*.

```mermaid
flowchart LR
  L["released layer<br/>(via Layer manifest resolver)"] --> CLK["user click<br/>or time selection"]
  CLK --> ENV["MapContextEnvelope assembled<br/>(camera · layers · features · time · evidence refs)"]
  ENV --> API["governed-api/<br/>(trust membrane)"]
  API --> EB["EvidenceBundle resolution<br/>(via Evidence resolver)"]
  EB --> DRW["EvidenceDrawerPayload<br/>(sensitivity-redacted projection)"]
  DRW --> FM{"Focus Mode<br/>requested?"}
  FM -->|no| DONE["display drawer"]
  FM -->|yes| FMR["FocusModeResponse:<br/>ANSWER · ABSTAIN · DENY · ERROR"]
  FMR --> RCPT["AIReceipt + RunReceipt"]
  RCPT -.->|"if correction needed"| ROLL["correction /<br/>rollback lineage"]
  classDef map fill:#c8e6c9,stroke:#1b5e20;
  classDef gov fill:#e1f5fe,stroke:#01579b;
  class L,CLK,ENV,DONE map;
  class API,EB,DRW,FMR,RCPT gov;
```

> [!IMPORTANT]
> **No step is skippable.** A "click → answer" interaction is **never one route call** — it composes layer resolution + envelope admission + evidence resolution + drawer projection + optional Focus Mode + receipt emission. Per `ai-build-operating-contract.md` §22.1: *"If any step relies only on rendered feature properties, popup text, or model output, the trust membrane has been bypassed."*

[↑ Back to top](#top)

---

## 7. Map object families

> **Evidence basis:** `Master_MapLibre_Components-Functions-Features_v2.1_FULL.md` §9 *(component table)*; idea cards `KFM-P1-FEAT-0040` *(layer metadata)*, `KFM-P1-FEAT-0042` *(viewer-side verification fails closed)*; ADR-0007 *(PROPOSED — adds `PluginAdmission` family and pins `LayerManifest.plugin_dependencies`)*. **CONFIRMED doctrine for the object families; PROPOSED for schema homes pending mounted-repo verification.**

The map surface has its own object vocabulary. All schema homes below are PROPOSED — verify at next mounted-repo session.

| Object | Role | Schema home *(PROPOSED)* |
|---|---|---|
| **`SourceDescriptor`** | Defines admissible source identity and role *(used across all lanes; consumed by the map for source-of-source resolution)*. | `schemas/contracts/v1/sources/source_descriptor.schema.json` |
| **`LayerManifest`** | Binds a UI layer to governed source/evidence semantics. Carries `layer_id`, `title`, `geometry_type`, `geometry_label` *(2D / 2.5D / 3D)*, `source_id`, `source_layer`, `evidence_ref_field`, `temporal_fields`, `policy_label`, `release_state`, `plugin_dependencies[]` *(per ADR-0007)*. | `schemas/contracts/v1/map/layer_manifest.schema.json` |
| **`StyleManifest`** | Controls style identity and dependencies. Carries `style_id`, `version`, `style_json_url`, `sprites`, `glyphs`, `style_digest`, `layer_ids`, `release_id`. | `schemas/contracts/v1/map/style_manifest.schema.json` |
| **`TileArtifactManifest`** | Controls PMTiles/MVT/COG/MBTiles release artifacts. Carries `artifact_id`, `type`, `url`, `digest`, `zooms`, `bounds`, `format`, `source_layers`, `metadata`, `range_required`, `cors_required`. | `schemas/contracts/v1/map/tile_artifact_manifest.schema.json` |
| **`MapReleaseManifest`** | Defines a complete published map release. Links `LayerManifest`, `StyleManifest`, tile artifacts, `EvidenceBundle`, `PolicyDecision`, `PromotionDecision`, cache keys, rollback target. Per ADR-0007, default `layers[*].renderer == "maplibre"`. | `schemas/contracts/v1/map/map_release_manifest.schema.json` |
| **`PluginAdmission`** *(PROPOSED — ADR-0007 §3.2)* | Per-plugin, per-version `PolicyDecision` that gates non-native rendering paths. Required for `3d-tiles-renderer`, `maplibre-three-plugin`, `maplibre-gl-lidar`, `maplibre-cog-protocol`, `pmtiles`, `maplibre-gl-vector-text-protocol`, `maplibre-contourmap`, `deck.gl` interleaved, three.js, and any other admitted plugin. | `schemas/contracts/v1/policy/plugin_admission.schema.json` |
| **`SceneManifest`** *(Atlas §18)* | Governs assembly of native + plugin-hosted layers into a render-ready scene; carries `view_state`, `layers[]`, `plugin_versions[]`, `representation_receipt_ref`. | `schemas/contracts/v1/maplibre/scene_manifest.schema.json` *(PROPOSED)* |
| **`TerrainModel`** *(Atlas §18)* | Governs the `raster-dem` source used by `Map.setTerrain`; carries CRS, encoding, checksum, provenance, source vintage, processing pipeline, bbox, temporal extent, license. | `schemas/contracts/v1/3d/terrain_model.schema.json` *(PROPOSED)* |
| **`ViewState` / `CameraPath`** *(Atlas §18)* | View-mode and cinematic motion as governed assets; JSON-validated, spec-hashed. | `schemas/contracts/v1/maplibre/view_state.schema.json`, `.../camera_path.schema.json` |
| **`EvidenceBundle`** | Truth-bearing evidence object that outranks generated language and rendered state. | `schemas/contracts/v1/evidence/evidence_bundle.schema.json` |
| **`EvidenceDrawerPayload`** | UI-side projection shown after click / selection. Includes feature context, source/citation display, caveats, conflicts. | `schemas/contracts/v1/ui/evidence_drawer_payload.schema.json` |
| **`MapContextEnvelope`** | Bounded map context sent to governed API / Focus Mode. | `schemas/contracts/v1/ui/map_context_envelope.schema.json` |
| **PMTiles sidecar** *(`.pmtiles.attest.json`)* | Per-artifact integrity proof — `spec_hash`, `pmtiles_filename`, `root_hash` *(BLAKE3)*, `size_bytes`, `delta`, `byte_ranges_manifest`, signature/attestation. | Co-located with the tile artifact; schema PROPOSED. |
| **`VerifyReceipt`** | Records digest, bounds, schema verification *(per SRC-058)*. | `schemas/contracts/v1/proofs/verify_receipt.schema.json` *(PROPOSED)* |
| **`RuntimeProbeResult`** | Reviewable report from runtime probes *(decode, heap, token stability)*; emitted into promotion gates; does not decide truth. | `schemas/contracts/v1/proofs/runtime_probe_result.schema.json` *(PROPOSED)* |
| **`RepresentationReceipt`** *(Atlas §18)* | Records what was rendered, when, with which `spec_hashes` and plugin versions. | `schemas/contracts/v1/maplibre/representation_receipt.schema.json` *(PROPOSED)* |
| **`Reality Boundary Note`** *(Atlas §18)* | Required marker distinguishing synthetic / reconstructed / AI-generated content from observed reality. | `schemas/contracts/v1/3d/reality_boundary_note.schema.json` *(PROPOSED)* |

[↑ Back to top](#top)

---

## 8. 2D default · 3D conditional · tile artifact discipline

> **Evidence basis:** `KFM-P2-FEAT-0013` *(mobile-first tile playbook)*; `KFM-P1-FEAT-0042` *(viewer-side verification fails closed)*; SRC-058 *(PMTiles BAO sidecars, runtime probes, ReleaseRuntimeGate)*; SRC-066 *(PMTiles operational governance)*; `docs/adr/ADR-0007-maplibre-is-the-sole-browser-renderer.md` *(PROPOSED — single-renderer 2D ↔ 3D ↔ globe across MapLibre)*; `docs/architecture/maplibre-3d.md` *(PROPOSED — companion architecture document)*. **CONFIRMED doctrine throughout; the prior dual-renderer card `KFM-P2-FEAT-0012` is superseded by ADR-0007.**

### 8.1 2D default; 3D conditional — all within MapLibre

KFM presents three view modes, **all rendered by MapLibre GL JS**. They are governed view-state transformations of the same underlying tiles and `LayerManifest` set; switching modes is a `ViewState` change, not a renderer change.

| Mode | When it wins | When it fails | Trust consequence |
|---|---|---|---|
| **2D plan-view MapLibre** *(default)* | Inspection, accessibility, low-bandwidth, sensitive-context parity with Evidence Drawer. | — | Canonical inspection path. |
| **3D terrain MapLibre** *(conditional)* | Terrain context, viewshed reasoning, line-of-sight evidence, draped imagery, Story Node scenes. Native via `raster-dem` + `Map.setTerrain` + `hillshade`; admitted plugins host OGC 3D Tiles *(via `3d-tiles-renderer` + three.js)*, glTF *(via `maplibre-three-plugin` or three.js)*, LiDAR point clouds *(via `maplibre-gl-lidar`)*, and `deck.gl` interleaved overlays. | 3D admission gate may DENY *(missing `Scene Manifest`, missing `Reality Boundary Note`, generalization not applied, plugin admission missing, evidence non-parity)*. Failure falls back to 2D with a visible reason. | 2D MapLibre remains canonical; 3D adds visualization value but never substitutes for the 2D evidence path. |
| **Globe MapLibre** *(conditional — MapLibre 5.0+)* | Kansas-in-context overview, atmospheric/day-night context. Native via `setProjection({type:'globe'})` + `sky` + `light`. | Older runtimes: graceful failure to mercator. Sensitive layers: globe inherits 2D admission *(no projection-driven loosening)*. | Globe is a `ViewState` transformation; same tiles, evidence parity by construction. |

> [!IMPORTANT]
> **Switching between view modes preserves active layer set, filter set, and Focus Mode.** Because all three modes run on the same renderer over the same tiles, evidence identity is upheld **by construction** *(per ADR-0007 §6.1)* — no cross-renderer drift can occur.

> [!CAUTION]
> **3D admission gate is real.** Per Atlas §18 / SRC-057, 3D layers require `Scene Manifest`, `Reality Boundary Note` *(where applicable)*, plugin admission *(where applicable)*, and 3D admission closure before publication. A layer with `geometry_label: '2.5D'` and `requested_mode: 'true_3d_evidence'` is DENIED *(Atlas §18 invariant `I-3D-4`)*. **PROPOSED implementation; CONFIRMED doctrine.**

### 8.2 Tile artifact discipline

KFM tile artifacts *(PMTiles, MVT, MLT, COG, MBTiles, Zarr)* are **derived release artifacts**, never sovereign data. Every public tile artifact carries:

1. **A signed `TileArtifactManifest`** linking to `MapReleaseManifest`.
2. **A sidecar** *(e.g., `.pmtiles.attest.json`)* with `spec_hash`, `root_hash` *(BLAKE3)*, `byte_ranges_manifest`, optional `bao_proof_ref`.
3. **A DSSE/cosign signature** transparency-logged in Rekor.
4. **A `VerifyReceipt`** recording digest, bounds, and schema verification.
5. **A rollback target** *(prior release manifest + cache invalidation record)*.

> [!IMPORTANT]
> **The publication flow is fixed** *(per SRC-058 p.49)*: *"Delta PMTiles built → BAO root → manifest → cosign signature → range verify → all gates → publish candidate → RunReceipt → released."* **No step is skippable.**

### 8.3 PMTiles publication gates *(CONFIRMED — SRC-058 pp.48–49)*

The PMTiles publication gates DENY on:

- `invalid_spec_hash`
- `unsigned_release_manifest`
- `unverified_tile_chunk`
- `public_unsigned_delta`
- `rollback_root_mismatch`
- `missing_run_receipt`

### 8.4 Plugin admission gates *(PROPOSED — ADR-0007 §3.4)*

Beyond tile artifact gates, the renderer enforces plugin admission gates against the `LayerManifest`, `SceneManifest`, and `MapReleaseManifest`:

- `unadmitted_plugin` — a plugin identifier in `LayerManifest.plugin_dependencies` not present in the admitted set.
- `unpinned_plugin_version` — admitted plugin without a pinned version.
- `drifted_plugin_version` — pinned version does not match the lockfile entry.
- `non_maplibre_renderer_without_exception_adr` — `MapReleaseManifest.layers[*].renderer != "maplibre"` without an accepted exception-ADR id.
- `cross_renderer_bridge_field` — appearance of any cross-renderer bridge field in `SceneManifest` *(structurally disallowed under single-renderer commitment)*.

[↑ Back to top](#top)

---

## 9. Viewer-side verification fails closed · UI negative states

> **Evidence basis:** `KFM-P1-FEAT-0042` *(viewer-side verification fails closed)*; SRC-058 pp.190–214 *(MapLibre verify-before-addSource)*; `ai-build-operating-contract.md` §22.2 *(UI negative states)*. **CONFIRMED doctrine.**

### 9.1 Viewer-side fails-closed flow

```text
MapLibre app init
  → fetch sidecar
  → verify DSSE/cosign signature
  → check spec_hash / tiling_scheme / tile_format
  → sample byte ranges
  → verify plugin admissions for required plugin set (per LayerManifest)
  → IF all pass → addSource (and instantiate admitted plugin layers)
  → IF any fail → DENY (post status = chunk_verification_failed
                        or unadmitted_plugin; no tile / layer exposed)
```

> [!CAUTION]
> **The renderer fails CLOSED.** Per `KFM-P1-FEAT-0042` *(PROPOSED, EXPANDED across passes)*: *"A viewer should fail closed or degrade visibly when artifact signatures, sidecars, hashes, policy state, or release manifests cannot be verified."* A renderer that silently falls back to unverified content has bypassed the trust membrane. Plugin-hosted layers are admitted to the same fails-closed flow *(per ADR-0007)*.

### 9.2 UI negative states *(CONFIRMED — AIBOC §22.2)*

The UI surfaces **nine negative states as first-class**, not as error toasts or missing content:

| State | Meaning |
|---|---|
| `MISSING_EVIDENCE` | `EvidenceRef` did not resolve. |
| `SOURCE_STALE` | `SourceDescriptor.cadence` passed without re-admission. |
| `DENIED_BY_POLICY` | `PolicyDecision = DENY`. |
| `GENERALIZED_GEOMETRY` | Sensitivity-redacted projection applied. |
| `RESTRICTED_ACCESS` | Audience class does not match required tier. |
| `CONFLICTED_SUPPORT` | Multiple `EvidenceRef`s with material disagreement. |
| `CITATION_FAILED` | `CitationValidationReport.verdict = FAIL`. |
| `RELEASE_WITHDRAWN` | `ReleaseManifest` superseded; rollback target active. |
| `RUNTIME_ERROR` | Governed API cannot evaluate. |

[↑ Back to top](#top)

---

## 10. Reality Boundary Note — synthetic vs observed

> **Evidence basis:** `Kansas_Frontier_Matrix_-_Domains_v1_1___Pass_23_32_Consolidated_Atlas.md` §24.1.1 *(source-role table — "Synthetic" row)*; §24.9.2 *(anti-pattern: "Synthetic surface presented without Reality Boundary Note → Reconstruction read as observation")*. **CONFIRMED doctrine.**

When the map presents synthetic / reconstructed / AI-generated content *(reconstructed historical scenes, AI-summary outputs, smoothed/interpolated rasters, 3D meshes derived from sparse evidence, glTF reconstructions, point-cloud-derived surfaces)*, the surface MUST carry a **`Reality Boundary Note`** plus a **`Representation Receipt`** recording the transform.

| Content class | Marker required | DENY if missing |
|---|---|---|
| Synthetic terrain surface | `Reality Boundary Note` + `Representation Receipt` | ✅ |
| Reconstructed historical scene *(glTF or 3D Tiles)* | `Reality Boundary Note` + `Representation Receipt` | ✅ |
| AI-summary output rendered as map annotation | `Reality Boundary Note` + `AIReceipt` cross-reference | ✅ |
| Interpolated raster *(suitability surface, smoke trajectory, etc.)* labeled and presented as observed | — *(deny entirely — source-role anti-collapse, see [`cross-domain/README.md` §6.2](../cross-domain/README.md))* | ✅ |
| Point-cloud-derived shaded surface *(LiDAR slope/hillshade derivative)* presented as observation rather than as a visibility-aid context layer | `Reality Boundary Note` + clear labeling as "context layer" | ✅ |

> [!IMPORTANT]
> **The renderer is the last line of defense.** A synthetic raster or 3D mesh could pass through ingestion, validation, and release if the `Reality Boundary Note` is malformed but present. The renderer MUST verify the note exists *and* renders, and MUST refuse to display the surface as observed reality without it.

[↑ Back to top](#top)

---

## 11. What lives here · What does not live here

### 11.1 What lives here

| Content | Why it belongs in `docs/architecture/map-master/` |
|---|---|
| Renderer-discipline doctrine *(MapLibre is the sole downstream renderer)* | This is the canonical scope of the Master MapLibre document; the lane consolidates its architectural posture. |
| Tile artifact lifecycle architecture *(PMTiles, MVT, COG, MBTiles, Zarr — release, sidecars, BAO proofs, signatures)* | Cross-format discipline applies to all tile types; per-format specifics live in the contracts/schemas, but the cross-format posture lives here. |
| Layer / Style / TileArtifact / MapRelease / PluginAdmission manifest **architectural** concerns | The schemas live under `schemas/contracts/v1/map/` and `.../policy/`; the discipline that connects them lives here. |
| Evidence Drawer architecture *(click-to-truth flow, negative-state surfacing)* | The drawer composes API outputs into a UI surface; the composition rules live here. |
| Cross-mode parity discipline *(2D plan ↔ 3D terrain ↔ globe)* within MapLibre | View-mode discipline is renderer-internal but cross-cutting across layer/style/evidence concerns. |
| Reality Boundary Note enforcement at the renderer | The renderer is the last gate before display; the rule belongs here as well as in cross-domain doctrine. |
| Plugin admission discipline *(per ADR-0007)* | What it means for a plugin to be admitted; how `PluginAdmission` composes with `LayerManifest`, `SceneManifest`, and `MapReleaseManifest`. |
| Performance budgets, runtime probes, mobile-first playbook | Cross-cutting performance discipline; per-format implementations live with each format's manifest. |
| Anti-pattern register scoped to map / renderer concerns | E.g., map shell consuming canonical store, popup-as-citation, style-only sensitivity hiding. |

### 11.2 What does NOT live here

| Excluded | Canonical home |
|---|---|
| The Master MapLibre document itself *(the cumulative doctrine)* | `Master_MapLibre_Components-Functions-Features_v2.1_FULL.md` *(at project knowledge root or `docs/lineage/`)* |
| ADR-0007 *(the single-renderer decision itself)* | `docs/adr/ADR-0007-maplibre-is-the-sole-browser-renderer.md` |
| The MapLibre 3D implementation reference *(native APIs, plugin paths, examples)* | `docs/architecture/maplibre-3d.md` |
| Per-layer / per-style / per-tile schema files *(`.schema.json`)* | `schemas/contracts/v1/map/...`, `schemas/contracts/v1/3d/...`, `schemas/contracts/v1/policy/...` |
| Style JSON, sprites, glyphs | `data/published/styles/...` *(per directory-rules.md)*; or `apps/explorer-web/src/styles/` for app-local |
| Tile artifacts *(PMTiles, MVT, COG)* themselves | `data/published/tiles/<area>/...` *(per lifecycle invariant)* |
| Rego policy enforcing renderer-side gates | `policy/map/...`, `policy/maplibre/...`, `policy/release/...` |
| App-level code *(`apps/explorer-web/`, MapLibre integration; plugin host code under `packages/maplibre-runtime/`)* | `apps/explorer-web/src/...`, `packages/maplibre-runtime/src/...` |
| Per-area Focus Mode UI | `apps/explorer-web/src/focus-modes/<area>/...` *(per directory-rules §6.7)* |
| Domain-specific layer designs | `docs/domains/<domain>/` |
| AI surface boundaries / continuity / route map | `docs/architecture/governed-ai/{BOUNDARIES,CONTINUITY_NOTES,ROUTE_MAP}.md` |

> [!WARNING]
> **Do not let this lane absorb implementation.** Same rule as every other architecture lane: schemas, policies, validators, and app code live under their canonical responsibility roots, **never** inside `docs/architecture/`.

[↑ Back to top](#top)

---

## 12. Directory tree (PROPOSED)

**PROPOSED — assumes OPEN-DR-12 resolves to "permit folder pattern".** If OPEN-DR-12 is rejected, all siblings below flatten to `docs/architecture/map-master-<topic>.md` or merge into a single `docs/architecture/map-master.md`.

```text
docs/architecture/map-master/          ⚠ PROPOSED · OPEN-DR-12 family
├── README.md                          ◄── this file (landing + navigation)
├── RENDERER_BOUNDARY.md               ◄── seven negative authorities expanded; renderer-as-downstream contract; single-renderer commitment per ADR-0007 (PROPOSED; expands §4)
├── TILE_ARTIFACTS.md                  ◄── PMTiles / MVT / COG / MBTiles / Zarr; sidecars; BAO; signatures; publication gates (PROPOSED; expands §8.2, §8.3)
├── LAYER_LIFECYCLE.md                 ◄── LayerManifest · StyleManifest · TileArtifactManifest · MapReleaseManifest · PluginAdmission composition (PROPOSED; expands §7)
├── EVIDENCE_DRAWER.md                 ◄── click-to-truth flow; drawer composition; conflict/caveat surfaces (PROPOSED; expands §6, §9)
├── 2D_3D_PARITY.md                    ◄── plan-view ↔ terrain ↔ globe parity within MapLibre; Reality Boundary Note discipline; 3D admission gate (PROPOSED; expands §8.1, §10)
├── PLUGIN_ADMISSION.md                ◄── PluginAdmission contract; admitted plugin set; pinning, attestation, lockfile guardrails (PROPOSED; expands §8.4)
├── PERFORMANCE_BUDGETS.md             ◄── runtime probes; decode/heap budgets; mobile-first tile playbook; per-mode budgets (2D / terrain / globe / 3D Tiles / point clouds) (PROPOSED)
└── VIEWER_VERIFICATION.md             ◄── verify-before-addSource; fails-closed semantics; chunk verification; plugin-admission verification (PROPOSED; expands §9.1)
```

> [!NOTE]
> **Eight PROPOSED siblings expand eight distinct sub-concerns.** The pattern matches `governed-ai/` *(three siblings on three axes)* and the proposed `governed-api/` siblings *(six sub-concerns)*. Each sibling owns its sub-topic; the README orients. The added `PLUGIN_ADMISSION.md` sibling reflects the new governance surface introduced by ADR-0007.

[↑ Back to top](#top)

---

## 13. Anti-patterns

> **Evidence basis:** `Kansas_Frontier_Matrix_-_Domains_v1_1___Pass_23_32_Consolidated_Atlas.md` §24.9.2 *(trust-membrane anti-patterns)*; `ai-build-operating-contract.md` §22.3 *(denied map behaviors)*; `Master_MapLibre_Components-Functions-Features_v2.1_FULL.md` §10 *(governance and trust-membrane chapter)*; ADR-0007 *(single-renderer anti-patterns)*. **CONFIRMED doctrine.**

Each row maps a violation back to one of the seven negative authorities of §4 *(or to the single-renderer commitment of ADR-0007)*.

| Anti-pattern | Negative authority violated | Counter-rule |
|---|---|---|
| **Map shell consumes canonical / internal store directly.** | #1 truth store | Public clients read via `apps/governed-api/` only; never directly from `data/raw\|work\|quarantine` or canonical stores. |
| **Tile metadata treated as source provenance** *(skipping `SourceDescriptor`)*. | #2 source registry | Source provenance lives in the source registry; the tile carries `source_id` references, not source identity. |
| **Style filter used to "hide" sensitive geometry.** | #3 policy engine | Generalization / redaction happens **before** public tile release with a `RedactionReceipt`; style-only hiding is a leak waiting to happen. |
| **Popup text treated as a citation.** | #4 citation authority | Popups are non-authoritative; the Evidence Drawer carries the `EvidenceBundle` with validated citations. |
| **UI toggle marks a layer as "reviewed".** | #5 review authority | Review state lives in `ReviewRecord`; UI displays the state but does not author it. |
| **Layer visibility toggle = layer publication.** | #6 publication authority | Publication requires `ReleaseManifest` + rollback target + promotion gate; visibility is post-publication only. |
| **Generated AI text rendered as authoritative answer.** | #7 AI authority | Focus Mode answers are bounded by envelope and citation validation; the renderer displays the envelope, not the raw model output. |
| **Public RAW tile path** *(loading unreleased tiles directly)*. | #1, #6 | Tile load only when `release_state`, policy, rights, sensitivity, evidence refs, hashes, and rollback are all valid *(Master MapLibre §10)*. |
| **Direct browser → model traffic.** | #7 | Model adapters live behind the governed membrane *(`BOUNDARIES.md` §10)*. |
| **Renderer falls back silently on signature verification failure.** | #1 | Fail closed; DENY on `chunk_verification_failed` *(`KFM-P1-FEAT-0042`)*. |
| **3D scene presented as observed reality without `Reality Boundary Note`.** | #1 | Admission gate requires `Reality Boundary Note` + `Representation Receipt` *(Atlas §24.9.2)*. |
| **Synthetic AI-summary annotation overlaid as map feature** *(no marker)*. | #7, #1 | `Reality Boundary Note` + `AIReceipt` cross-reference; visible badge. |
| **Mutating published tile artifacts in place.** | #6 | Tile artifacts are immutable by release ID; new release = new manifest + new digest. |
| **No range-verification before tile add.** | #1 | `MapLibre verify-before-addSource` is doctrinal *(SRC-058 pp.190–194, 208–211)*. |
| **Adding a second browser-side renderer to the default path.** | ADR-0007 single-renderer commitment | DENY at `policy/release/renderer-boundary.rego` unless an accepted exception-ADR is referenced *(ADR-0007 §3.4)*. |
| **Unadmitted plugin in `LayerManifest.plugin_dependencies`.** | ADR-0007 / `PluginAdmission` | DENY at `policy/maplibre/plugin-admission.rego`; plugin must transit `PluginAdmission` first *(ADR-0007 §3.2)*. |
| **Unpinned or drifted plugin version.** | ADR-0007 / `PluginAdmission` | DENY at lockfile validator; pin in `packages/maplibre-runtime/src/plugin-registry.ts` and CI lockfile guardrail *(ADR-0007 §8.4)*. |
| **`fill-extrusion` height pulled from generated attribute** *(not evidence-bearing)*. | Atlas §18 invariant `I-3D-4` | DENY at `policy/maplibre/3d-admission.rego`; `height_m` / `base_m` must be evidence-bearing per `LayerManifest`. |
| **`geometry_label: '2.5D'` layer cited as true-3D evidence.** | Atlas §18 invariant `I-3D-4` | DENY — the 2.5D label is not a 3D claim; cite a `'3D'`-labeled layer or abstain. |

[↑ Back to top](#top)

---

## 14. Open questions and ADR triggers

| Open item | Class | Suggested ADR title *(PROPOSED)* |
|---|---|---|
| **OPEN-DR-12** *(carried)* — META amendment to `directory-rules.md` §12 permitting folder-with-README pattern; covers `cross-domain/`, `governed-ai/`, `governed-api/`, `map-master/`. | Directory Rules §12 *(structural)* | "docs/architecture/ — folder-with-README pattern admission". |
| Which MapLibre GL JS target version *(and plugin allowlist)* is approved for the first release? | Tool selection / version pin | "MapLibre GL JS version pin and admitted plugin set v1". |
| `PluginAdmission` schema home — `schemas/contracts/v1/policy/plugin_admission.schema.json` vs `schemas/contracts/v1/maplibre/plugin_admission.schema.json`. | Schema home *(intersects ADR-S-03)* | "PluginAdmission schema home". |
| Admitted plugin licensing inventory — `3d-tiles-renderer`, `maplibre-three-plugin`, `maplibre-gl-lidar`, `maplibre-cog-protocol`, `pmtiles`, `maplibre-gl-vector-text-protocol`, `maplibre-contourmap`. | Licensing inventory | "Admitted plugin licensing baseline". |
| MLT *(MapLibre Tiles)* implementation status and rollout plan. | Tool selection / format | "MLT format admission". |
| Server-side raster fallback policy *(when MapLibre vector runtime gates fail, when to fall back to server-rasterized tiles)*. | Renderer-internal fallback | "Vector vs server-rasterized fallback policy within MapLibre". |
| Tile-host conventions *(CDN, signed URLs, Range header requirements, CORS configuration)*. | Operations | "Tile artifact hosting conventions". |
| 3D admission gate composition — what objects compose a `Scene Manifest` and which reviewers approve. | Object family / governance | "3D Scene Manifest composition and admission". |
| three.js custom-layer host pattern — single `custom-layer-host.ts` base class vs per-asset (3D Tiles / glTF / volumetric) host. | Implementation pattern | "three.js custom layer host architecture". |
| `freestiler` / `tipmtiles` / `tippecanoe` / `go-pmtiles` tooling readiness; build pipeline placement. | Tooling | "Tile build toolchain selection". |
| Renderer-side telemetry — what is sent, with what consent, and where it lands. | Privacy / operations | "Renderer telemetry contract". |
| Style asset homes — `data/published/styles/` vs `apps/explorer-web/src/styles/`. | Schema home | "Style asset placement". |

> [!NOTE]
> **Closed by ADR-0007 (PROPOSED).** The prior open question on "which secondary renderer edition is sanctioned" is closed by ADR-0007's single-renderer commitment. Any future need for a browser-side rendering technology outside the admitted plugin set transits the §3.5 exception-ADR path of ADR-0007.

> [!IMPORTANT]
> **OPEN-DR-12 is the unblocker** for the four architecture folders. Other map-specific OPEN questions can proceed in parallel ADR streams once the structural pattern is settled.

[↑ Back to top](#top)

---

## 15. Related docs

| Reference | Role | Truth label |
|---|---|---|
| `Master_MapLibre_Components-Functions-Features_v2.1_FULL.md` *(cumulative doctrine, v1.4 → v2.0+)* | **Canonical** map-surface doctrine; this lane consolidates its architectural posture | CONFIRMED doctrine |
| `Master_MapLibre_Components-Functions-Features_v2.1_FULL.md` §9 *(component table)* | Object families and schema homes | CONFIRMED doctrine |
| `Master_MapLibre_Components-Functions-Features_v2.1_FULL.md` §10 *(Governance and Trust-Membrane Chapter)* | Trust-membrane rules for the map surface | CONFIRMED doctrine |
| `docs/adr/ADR-0007-maplibre-is-the-sole-browser-renderer.md` | **Canonical** decision: MapLibre GL JS is KFM's sole browser-side renderer; defines `PluginAdmission` and exception-ADR path | PROPOSED *(per ADR-0007 §1)*; CONFIRMED at doctrine rank |
| `docs/architecture/maplibre-3d.md` | Companion architecture document: MapLibre 3D features and implementation across KFM domains | PROPOSED placement; CONFIRMED doctrine |
| `Kansas_Frontier_Matrix_-_Domains_v1_1___Pass_23_32_Consolidated_Atlas.md` §18 *(Planetary/3D Domain)* | 3D object families, invariants `I-3D-1` through `I-3D-7` | CONFIRMED doctrine |
| `Kansas_Frontier_Matrix_-_Domains_v1_1___Pass_23_32_Consolidated_Atlas.md` §19 *(Cross-Domain Systems — MapLibre UI + Evidence Drawer + Focus Mode)* | Renderer guardrails | CONFIRMED doctrine |
| `Kansas_Frontier_Matrix_-_Domains_v1_1___Pass_23_32_Consolidated_Atlas.md` §24.9.2 *(trust-membrane anti-patterns)* | Anti-pattern register | CONFIRMED doctrine |
| `ai-build-operating-contract.md` §22 *(map, UI, renderer contract; §22.1 click-to-truth; §22.2 negative states; §22.3 denied map behaviors)* | Builder-side rules for map / UI / renderer | CONFIRMED doctrine |
| `kfm_unified_doctrine_synthesis.md` §11 *(finite outcome envelope)* | Outcome semantics that the drawer and Focus Mode honor | CONFIRMED doctrine |
| `connected-dots-architecture-brief.md` §8 *(MapLibre, Evidence Drawer, and Focus Mode)* | Runtime flow + surface table | CONFIRMED doctrine |
| `directory-rules.md` §7.1 *(apps roles — `apps/explorer-web/` reads via `apps/governed-api/`)* | App-to-route mapping | CONFIRMED doctrine |
| `docs/architecture/governed-api/README.md` | API surface lane | PROPOSED placement; CONFIRMED doctrine |
| `docs/architecture/governed-ai/ROUTE_MAP.md` | Route inventory *(including Focus Mode runtime)* | PROPOSED placement; CONFIRMED doctrine |
| `docs/architecture/cross-domain/README.md` | Cross-lane invariants | PROPOSED placement; CONFIRMED doctrine |
| Atlas seed cards: `KFM-P1-FEAT-0038` *(Governed API as trust membrane)*, `KFM-P1-FEAT-0039` *(MapLibre as downstream renderer)*, `KFM-P1-FEAT-0040` *(layer metadata carries trust state)*, `KFM-P1-FEAT-0042` *(viewer-side verification fails closed)*, `KFM-P2-FEAT-0013` *(mobile-first tile playbook)* | Lineage for the doctrine in this README | PROPOSED *(seed cards)* |
| Atlas seed card: `KFM-P2-FEAT-0012` *(prior dual-renderer posture)* | **Superseded by ADR-0007 (PROPOSED).** Retained in the register with `superseded_by: ADR-0007` and forward link; not deleted. | SUPERSEDED |

[↑ Back to top](#top)

---

## 16. Appendix — glossary and reference

<details>
<summary><strong>16.1 Glossary of map-master vocabulary</strong></summary>

| Term | Definition *(CONFIRMED doctrine unless noted)* |
|---|---|
| **MapLibre GL JS** | Open-source map renderer with native support for 2D vector/raster, 3D terrain *(via `raster-dem` + `Map.setTerrain`)*, `hillshade`, globe projection *(5.0+)*, sky/atmosphere, 2.5D `fill-extrusion`, and custom WebGL layers. In KFM: **disciplined sole browser-side renderer inside a governed shell** *(per ADR-0007; aligned with Master MapLibre executive determinations)*. Not a truth authority. |
| **MapLibre 3D** | The set of MapLibre native APIs and admitted plugins that together provide 3D capability: `raster-dem` + `setTerrain`, `hillshade`, globe projection, `fill-extrusion`, `3d-tiles-renderer` via three.js custom layers, glTF via `maplibre-three-plugin` or direct three.js, point clouds via `maplibre-gl-lidar`, and `deck.gl` interleaved overlays. See `docs/architecture/maplibre-3d.md`. |
| **Admitted plugin set** | The plugins explicitly admitted via `PluginAdmission` and pinned in `packages/maplibre-runtime/src/plugin-registry.ts` *(per ADR-0007 §3.2)*. Membership is per-plugin, per-version. |
| **`PluginAdmission`** | Per-plugin, per-version `PolicyDecision` that gates non-native rendering paths. Required for every plugin entry in `LayerManifest.plugin_dependencies` *(per ADR-0007)*. |
| **three.js** | WebGL 3D library used as the foundation for MapLibre's plugin-hosted 3D paths *(OGC 3D Tiles, glTF, custom volumetric layers)*. Admitted via `PluginAdmission` per ADR-0007. |
| **`3d-tiles-renderer`** | Three.js-based renderer for OGC 3D Tiles *(b3dm, i3dm, pnts)*. Hosted inside a MapLibre custom layer; the path confirmed by MapLibre's official example dated 2026-03-03. |
| **`maplibre-three-plugin`** | Bridge plugin between MapLibre and three.js for 3D model rendering and animation. |
| **`maplibre-gl-lidar`** | LiDAR point cloud plugin supporting LAS 1.0–1.4, COPC, EPT streaming *(deck.gl-based)*. |
| **`deck.gl` interleaved** | `MapboxOverlay` with `interleaved: true` over MapLibre's WebGL2 context; supports MapLibre ≥ 3. |
| **OGC 3D Tiles** | Open standard for streaming 3D geographic content. In KFM: rendered inside MapLibre via the `3d-tiles-renderer` + three.js custom layer path. |
| **glTF** | Royalty-free 3D scene/asset format. In KFM: rendered inside MapLibre via `maplibre-three-plugin` or a direct three.js custom layer. |
| **PMTiles** | Single-file tile archive format; KFM's primary released tile artifact carrier. |
| **MVT** | Mapbox Vector Tile format; embedded in PMTiles for vector layers. |
| **MLT** | MapLibre Tiles — newer tile format under evaluation *(version pinning pending; PROPOSED)*. |
| **COG** | Cloud Optimized GeoTIFF; primary raster release format. |
| **MBTiles** | SQLite-based tile format; secondary / legacy. |
| **Zarr** | Cloud-native array format; emerging in KFM for multidimensional data *(per SRC-064/SRC-066)*. |
| **Style JSON** | MapLibre style document; governed under `StyleManifest`. |
| **Evidence Drawer** | UI surface that displays `EvidenceBundle` for a feature click; canonical click-to-truth resolution. |
| **`Reality Boundary Note`** | Marker distinguishing synthetic / reconstructed / AI-generated content from observed reality. |
| **`Representation Receipt`** | Companion to `Reality Boundary Note`; records the transform that produced a synthetic or rendered surface. |
| **`SceneManifest`** | Governs assembly of native + plugin-hosted layers into a render-ready scene *(Atlas §18)*. |
| **`TerrainModel`** | Governed `raster-dem` source for `Map.setTerrain` *(Atlas §18)*. |
| **`ViewState` / `CameraPath`** | View-mode and cinematic motion as governed JSON assets *(Atlas §18)*. |
| **BAO** | Streaming hash tree algorithm used in PMTiles outboard proofs *(per SRC-058, SRC-066)*. |
| **Sidecar** | Companion file *(e.g., `.pmtiles.attest.json`)* carrying integrity proof metadata for a primary artifact. |
| **`spec_hash`** | Hash of the canonical spec string / tag fixing the format version. |
| **`root_hash`** | BLAKE3 hash of the full artifact / Bao root; integrity anchor. |
| **`byte_ranges_manifest`** | List of `z/x/y, start, end, range_hash, optional bao_proof_ref` for tile-range proofs. |
| **`RuntimeProbeResult`** | Reviewable report from runtime probes; emitted into promotion gates; does not decide truth. |
| **`VerifyReceipt`** | Records digest, bounds, and schema verification at viewer-side. |
| **Story Node** | Narrative/scene unit composed of layers + camera + time + evidence; subject to its own admission gate. |
| **3D admission gate** | Gate requiring `Scene Manifest`, `Reality Boundary Note` *(where applicable)*, plugin admission *(where applicable)*, and admission closure before 3D publication. |
| **`geometry_label`** | Layer-level label declaring `'2D'`, `'2.5D'`, or `'3D'`. A `'2.5D'`-labeled layer cannot be cited as true-3D evidence *(Atlas §18 `I-3D-4`)*. |

</details>

<details>
<summary><strong>16.2 The seven negative authorities — quick reference card</strong></summary>

```text
The renderer is NOT:

  1. Canonical truth store          — EvidenceBundle is
  2. Source registry                 — SourceDescriptor registry is
  3. Policy engine                   — OPA/Rego policy is
  4. Citation authority              — CitationValidationReport is
  5. Review authority                — apps/review-console/ + ReviewRecord is
  6. Publication authority           — ReleaseManifest + release authority is
  7. AI authority                    — Focus Mode runtime (governed) is

If a renderer behavior would assume any of these roles, the change is ADR-class.

Additionally (per ADR-0007 PROPOSED):
  - MapLibre GL JS is the sole browser-side renderer.
  - Any rendering technology outside the admitted plugin set
    requires an accepted exception-ADR.
```

*(Verbatim seven-item enumeration preserved from Master MapLibre executive determinations across v1.4–v2.0+; eighth posture added per ADR-0007.)*

</details>

<details>
<summary><strong>16.3 PMTiles publication gates — quick reference</strong></summary>

```text
PMTiles publication DENIES on (CONFIRMED — SRC-058 pp.48–49):

  · invalid_spec_hash
  · unsigned_release_manifest
  · unverified_tile_chunk
  · public_unsigned_delta
  · rollback_root_mismatch
  · missing_run_receipt

Publication flow (verbatim — SRC-058 p.49):

  Delta PMTiles built
    → BAO root
    → manifest
    → cosign signature
    → range verify
    → all gates
    → publish candidate
    → RunReceipt
    → released

No step is skippable.
```

</details>

<details>
<summary><strong>16.4 Plugin admission gates — quick reference (PROPOSED — ADR-0007 §3.4)</strong></summary>

```text
Plugin admission DENIES on:

  · unadmitted_plugin
  · unpinned_plugin_version
  · drifted_plugin_version
  · non_maplibre_renderer_without_exception_adr
  · cross_renderer_bridge_field

Admission flow (per ADR-0007):

  License clearance
    → version pin in plugin-registry.ts
    → supply-chain attestation
    → schema-checked round-trip in LayerManifest.plugin_dependencies
    → PluginAdmission PolicyDecision = allow
    → lockfile entry verified
    → CI bundle-analyzer guardrail pass
    → admitted

Per-release re-verification is required (admissions do not auto-roll forward).
```

</details>

<details>
<summary><strong>16.5 UI negative states — quick reference</strong></summary>

```text
The UI MUST distinguish (CONFIRMED — AIBOC §22.2):

  · MISSING_EVIDENCE
  · SOURCE_STALE
  · DENIED_BY_POLICY
  · GENERALIZED_GEOMETRY
  · RESTRICTED_ACCESS
  · CONFLICTED_SUPPORT
  · CITATION_FAILED
  · RELEASE_WITHDRAWN
  · RUNTIME_ERROR

Negative states are first-class: surfaced explicitly, not as error toasts or
missing content. A RuntimeResponseEnvelope with outcome=ABSTAIN and a defined
reason code is a valid, finite, successful response.
```

</details>

<details>
<summary><strong>16.6 Truth-label legend</strong></summary>

- **CONFIRMED** — verified this session from attached docs, workspace evidence, tests, logs, or generated artifacts.
- **PROPOSED** — design, recommendation, file path, placement, or inference not yet verified in implementation.
- **INFERRED** — reasonably derivable from visible evidence but not directly stated.
- **NEEDS VERIFICATION** — checkable, but not yet checked strongly enough to act as fact.
- **UNKNOWN** — not resolvable without more evidence.
- **EXTERNAL** — sourced from authoritative external research. *(Used here only via ADR-0007's MapLibre 5.x capability evidence, which is itself externally verified against MapLibre's published documentation and examples.)*

</details>

<details>
<summary><strong>16.7 Changelog</strong></summary>

| Version | Date | Change |
|---|---|---|
| **v0.2** | 2026-05-24 | Material revision. Renderer architecture realigned to **single MapLibre GL JS renderer (native + admitted plugin set)** per **ADR-0007 (PROPOSED)**. Multi-renderer framing removed throughout. Prior dual-renderer card `KFM-P2-FEAT-0012` marked superseded *(retained in the register with `superseded_by: ADR-0007` per directory-rules §17)*. Added `PluginAdmission` object family to §7. Expanded §8 with view-mode table and plugin-admission gates (§8.4). Added `PLUGIN_ADMISSION.md` sibling to §12 directory tree. Added single-renderer anti-patterns (§13). Closed the "secondary renderer edition" open question via §14 note. Added ADR-0007 and `docs/architecture/maplibre-3d.md` to §15 related docs. Updated glossary (§16.1) and added quick-reference card for plugin admission (§16.4). |
| **v0.1** | 2026-05-24 | Initial draft. |

</details>

---

**Related (mini)** · [`docs/adr/ADR-0007-maplibre-is-the-sole-browser-renderer.md`](../../adr/ADR-0007-maplibre-is-the-sole-browser-renderer.md) · [`docs/architecture/maplibre-3d.md`](../maplibre-3d.md) · [`Master_MapLibre_Components-Functions-Features_v2.1_FULL.md`](../../../Master_MapLibre_Components-Functions-Features_v2.1_FULL.md) · [`Kansas_Frontier_Matrix_-_Domains_v1_1___Pass_23_32_Consolidated_Atlas.md` §§18, 19, 24.9.2](../../../Kansas_Frontier_Matrix_-_Domains_v1_1___Pass_23_32_Consolidated_Atlas.md) · [`ai-build-operating-contract.md` §22](../../../ai-build-operating-contract.md) · [`directory-rules.md` §7.1](../../../directory-rules.md) · [`docs/architecture/governed-api/README.md`](../governed-api/README.md) · [`docs/architecture/governed-ai/ROUTE_MAP.md`](../governed-ai/ROUTE_MAP.md) · [`docs/architecture/cross-domain/README.md`](../cross-domain/README.md)

**Last updated:** 2026-05-24 · **Doc version:** v0.2 · **Doc status:** draft · **Path status:** PROPOSED *(OPEN-DR-12 family)*

[↑ Back to top](#top)
