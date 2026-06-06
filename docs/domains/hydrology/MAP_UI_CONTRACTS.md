<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/domains/hydrology/map-ui-contracts
title: Hydrology — Map UI Contracts
type: standard
version: v2
status: draft
owners: <hydrology lane steward> + <map shell owner> + <governance reviewer>   # placeholders — resolve via CODEOWNERS
created: 2026-05-18
updated: 2026-06-06
policy_label: public
contract_version: "3.0.0"   # pinned per ai-build-operating-contract.md v3.0
related:
  - ai-build-operating-contract.md
  - directory-rules.md
  - Master_MapLibre_Components-Functions-Features_v2_1_FULL.md
  - docs/architecture/whole-ui-governed-ai-expansion.md
  - docs/domains/hydrology/README.md
  - docs/domains/hydrology/INDEX.md
  - docs/domains/hydrology/DATA_LIFECYCLE.md
  - docs/domains/hydrology/identity-model.md
  - docs/domains/hydrology/GLOSSARY.md
tags: [kfm, hydrology, map, ui, contracts, governed-api, evidence, layer-manifest]
notes:
  - All implementation-layer paths (schema URIs, routes, repo locations) are PROPOSED pending mounted-repo verification (none mounted this session).
  - Trust-state enum is CONFLICTED — the corpus renderer-boundary status vocabulary is released/stale/degraded/denied/unverified (+ candidate); the granted/narrowed/bounded/denied/candidate enum and the KFM-IDX-MAP-005 id are NEEDS VERIFICATION. See §10 + OQ.
  - NFHL role-separation is a CONFIRMED doctrinal invariant for this domain (Atlas §24.1.2).
  - SourceDescriptor schema home schemas/contracts/v1/source/source-descriptor.json (ADR-0001); source/ vs sources/ CONFLICTED.
  - v2 pins CONTRACT_VERSION, fixes doc_id to lane slug, reconciles the trust-state vocabulary, aligns finite-outcome sets, and adds companion cross-links. See Changelog (§18).
[/KFM_META_BLOCK_V2] -->

# 💧 Hydrology — Map UI Contracts

> The contract surface between the Hydrology lane and the public Map UI: which objects cross the trust membrane, in which shape, with which outcomes, and under which guards.

<!-- Badges: replace TODO targets when CI, schema-home, and release routes are verified in a mounted repo. -->
[![Status: draft](https://img.shields.io/badge/status-draft-yellow)]()
[![CONTRACT_VERSION: 3.0.0](https://img.shields.io/badge/CONTRACT__VERSION-3.0.0-1f6feb)]()
[![Doc type: standard](https://img.shields.io/badge/doc--type-standard-blue)]()
[![Authority: lane-profile](https://img.shields.io/badge/authority-lane--profile-informational)]()
[![Domain: hydrology](https://img.shields.io/badge/domain-hydrology-1f9eda)]()
[![Policy label: public](https://img.shields.io/badge/policy--label-public-success)]()
[![Build/CI: TODO](https://img.shields.io/badge/CI-TODO-lightgrey)]()

**Status:** `draft` · **Owners:** `<hydrology lane steward>` · `<map shell owner>` · `<governance reviewer>` (placeholders) · **Contract:** `CONTRACT_VERSION = "3.0.0"` · **Last updated:** `2026-06-06`

---

## Mini-TOC

1. [Purpose & scope](#1-purpose--scope)
2. [Position in KFM doctrine](#2-position-in-kfm-doctrine)
3. [Contract surface — at a glance](#3-contract-surface--at-a-glance)
4. [Object families crossing the membrane](#4-object-families-crossing-the-membrane)
5. [Hydrology `LayerManifest` profile](#5-hydrology-layermanifest-profile)
6. [Hydrology `StyleManifest` profile](#6-hydrology-stylemanifest-profile)
7. [Hydrology `EvidenceDrawerPayload` projection](#7-hydrology-evidencedrawerpayload-projection)
8. [`MapContextEnvelope` for hydrology](#8-mapcontextenvelope-for-hydrology)
9. [Focus Mode behavior in hydrology context](#9-focus-mode-behavior-in-hydrology-context)
10. [Trust-state vocabulary](#10-trust-state-vocabulary)
11. [Source-role separation (the NFHL invariant)](#11-source-role-separation-the-nfhl-invariant)
12. [Freshness, staleness, and the gauge timeline](#12-freshness-staleness-and-the-gauge-timeline)
13. [Finite outcomes per surface](#13-finite-outcomes-per-surface)
14. [Validators & tests](#14-validators--tests)
15. [Anti-patterns](#15-anti-patterns)
16. [Open questions & verification backlog](#16-open-questions--verification-backlog)
17. [Related docs](#17-related-docs)
18. [Changelog](#18-changelog-v1--v2)

[Back to top](#-hydrology--map-ui-contracts)

---

## 1. Purpose & scope

**CONFIRMED doctrine / PROPOSED implementation.** This document specifies the **map-UI-facing contract surface** for the Hydrology lane: which Hydrology objects may appear in the public map shell, in what shape they appear, what outcomes the governed API may return for them, what the renderer is permitted to do with them, and what guards prevent misuse. It is a **profile** that specializes the cross-cutting MapLibre object families — `LayerManifest`, `StyleManifest`, `TileArtifactManifest`, `MapReleaseManifest`, `EvidenceDrawerPayload`, `MapContextEnvelope`, `FocusModeRequest/Response`, `AIReceipt`, `CitationValidationReport`, `PolicyDecision` — for the Hydrology lane. [MAP-MASTER §7.M]

It is a companion to [`INDEX.md`](./INDEX.md) (lane navigation), [`identity-model.md`](./identity-model.md) (feature identity), and [`DATA_LIFECYCLE.md`](./DATA_LIFECYCLE.md) (gates). It is **not**:

- A connector or pipeline specification (see hydrology pipeline specs).
- A schema home (schemas live under `schemas/contracts/v1/...`; PROPOSED).
- A release manifest (release decisions live under `release/`).
- A policy authority (policy decisions live under `policy/domains/hydrology/`).

### Scope summary

| In scope | Out of scope |
|---|---|
| What hydrology objects may surface in the map UI | How hydrology objects are ingested or normalized |
| Shape of UI-bound DTOs (profile of cross-cutting families) | Field-level schema definitions (live in `schemas/`) |
| Outcomes the governed API may return | Backend implementation of those routes |
| Trust-state vocabulary applied to hydrology layers | Renderer code in `packages/maplibre/` |
| Source-role separation rules at the UI boundary | Source rights and licensing (live in `policy/`) |

> [!IMPORTANT]
> This session exposed doctrine documents only, not a mounted repo. Every route name, schema URI, and repo path here is **PROPOSED** until verified.

[Back to top](#-hydrology--map-ui-contracts)

---

## 2. Position in KFM doctrine

> [!IMPORTANT]
> **CONFIRMED doctrinal invariant.** The map renderer is **downstream** of trust. MapLibre, tiles, popups, and badges are **carriers**, never **authorities**. Anything the map shows must trace, via governed API, to an `EvidenceBundle`, a `LayerManifest`, and a `MapReleaseManifest` — or else it must be rendered in an explicit denied, degraded, or unverified state. [MAP-MASTER §10; ML-061-002 "checksums do not prove origin or process"]

The Hydrology Map UI Contract sits at the intersection of four invariants:

```mermaid
flowchart LR
    subgraph TRUST[Trust spine — CONFIRMED doctrine]
        EB[EvidenceBundle]
        SD[SourceDescriptor]
        LM[LayerManifest]
        MRM[MapReleaseManifest]
        PD[PolicyDecision]
    end

    subgraph LANE[Hydrology lane — PROPOSED implementation]
        HUC[HUC / Watershed]
        REACH[HydroFeature / Reach]
        GAUGE[GaugeSite plus FlowObservation]
        NFHL[NFHLZone — regulatory context]
        FLOOD[Observed Flood Event]
    end

    subgraph MEMBRANE[Governed API — PROPOSED routes]
        FEAT[features resolver]
        EVR[evidence resolver]
        LMR[layer manifest resolver]
        FOC[focus mode]
    end

    subgraph UI[Map UI — apps/explorer-web/]
        SHELL[Map shell plus time strip]
        DRAW[Evidence Drawer]
        FOCUS[Focus Mode panel]
    end

    LANE --> TRUST
    TRUST --> MEMBRANE
    MEMBRANE --> UI
    UI -. click or focus request .-> MEMBRANE
    MEMBRANE -. ANSWER or ABSTAIN or DENY or ERROR .-> UI
```

> [!NOTE]
> **Truth label.** The trust spine and invariants are **CONFIRMED doctrine**. The hydrology lane, governed-API routes, and UI components shown are **PROPOSED implementation** until checked against a mounted repository.

[Back to top](#-hydrology--map-ui-contracts)

---

## 3. Contract surface — at a glance

The hydrology map UI exchanges five **kinds** of payloads across the membrane. Each payload is a profile of a cross-cutting family.

| Direction | Trigger | Inbound payload (UI → API) | Outbound payload (API → UI) | Outcomes |
|---|---|---|---|---|
| Bootstrap | Map shell load | `MapContextEnvelope` (initial) | `LayerCatalogItem[]` (hydrology subset) + `LayerManifest` refs | `ANSWER` / `DENY` / `ERROR` |
| Layer load | Layer toggle | `layer_id` + `release_id?` | `LayerManifest` + `StyleManifest` ref + `TileArtifactManifest` ref | `ANSWER` / `DENY` / `ERROR` |
| Feature click | Pointer / keyboard select | `feature_id` + `layer_id` + `MapContextEnvelope` | `EvidenceDrawerPayload` (hydrology projection) | `ANSWER` / `ABSTAIN` / `DENY` / `ERROR` |
| Timeline change | Time slider | `MapContextEnvelope` (with `time_window`) | New `LayerManifest` snapshot refs + stale/degraded flags | `ANSWER` / `DENY` / `ERROR` |
| Focus Mode | User question | `FocusModeRequest` + `MapContextEnvelope` | `FocusModeResponse` + `AIReceipt` + `CitationValidationReport` | `ANSWER` / `ABSTAIN` / `DENY` / `ERROR` |

> [!CAUTION]
> The renderer **MUST NOT** call canonical stores (`data/processed/`, `data/catalog/`, `data/published/` raw paths) directly. The only browser network paths permitted for trust-bearing content are the governed API routes named above. This is the no-public-RAW-path / no-direct-canonical-fetch rule. [MAP-MASTER §10, CONFIRMED]

[Back to top](#-hydrology--map-ui-contracts)

---

## 4. Object families crossing the membrane

The Hydrology lane uses the cross-cutting Map UI object families. Below is the **profile binding** — which hydrology object identities and which fields participate in each family.

| Cross-cutting family | Hydrology profile (PROPOSED) | Bound hydrology objects |
|---|---|---|
| `SourceDescriptor` | One per hydrology source family. Carries `source_role` (one of the canonical seven, fixed at admission). | USGS WBD/HUC, NHDPlus HR / 3DHP, USGS Water Data / NWIS, FEMA NFHL/MSC, 3DEP terrain, water-quality programs, groundwater wells, historical flood evidence |
| `LayerManifest` | One per public-safe hydrology layer. Carries layer identity, source/evidence bindings, sensitivity label, attribution, release/trust state. | HUC12 watershed layer, NHDPlus flowline / catchment layer, gauge site point layer, NFHL regulatory zones layer (**context only**), observed-flood-event layer, terrain-derived hydrology context, water-quality / groundwater context layers |
| `StyleManifest` | One per released hydrology style set. Carries color ramps, output units, uncertainty cues, legends. | HUC12 boundary style, flow-magnitude ramp, gauge symbology with stale/degraded variants, NFHL regulatory style (visually distinct from observed inundation), trust-state badges |
| `TileArtifactManifest` | One per PMTiles / MVT / COG artifact serving a hydrology layer. Carries digest, `spec_hash`, byte-range / sidecar manifest, expected media type (`application/vnd.pmtiles`). | HUC12 PMTiles, flowline PMTiles, gauge points (GeoJSON or PMTiles), NFHL contextual tiles, optional terrain COG |
| `MapReleaseManifest` | Binds the hydrology layer set, style, and tile artifacts to a release decision, rollback target, cache keys, and provenance/SBOM referrers. | Hydrology release bundle (PROPOSED) |
| `EvidenceDrawerPayload` | Click-resolution payload that surfaces `EvidenceBundle` refs, source roles, valid time, review state, rights, sensitivity, correction links. | One projection variant per hydrology object family (HUC, reach, gauge, NFHL zone, observed flood, water-quality observation, groundwater well) |
| `MapContextEnvelope` | Map state envelope: camera, bounds, zoom, time window, visible layers, selected feature(s), version locks. | Same shape; carries hydrology layer ids and selected feature ids |
| `FocusModeRequest / Response` | Bounded AI surface over released Hydrology `EvidenceBundle`s. | Hydrology-scoped questions only; cite-or-abstain enforced |
| `AIReceipt` | Audit trail for any Focus Mode answer over hydrology evidence. | One per Focus call; never stores private reasoning |
| `CitationValidationReport` | Proof that every cited `EvidenceRef` resolves and is admissible. | One per Focus answer or governed export |
| `PolicyDecision` | Decision record gating layer admission, drawer payload composition, and Focus responses. | One per gate evaluation |

> [!NOTE]
> **Schema homes.** The schemas for the cross-cutting families above are **PROPOSED** to live under `schemas/contracts/v1/...` (e.g., `schemas/contracts/v1/layers/layer_manifest.schema.json`, `schemas/contracts/v1/ui/evidence_drawer_payload.schema.json`). The shared `SourceDescriptor` schema home is `schemas/contracts/v1/source/source-descriptor.json` per ADR-0001 — though `source/` vs `sources/` is itself **CONFLICTED** (Atlas §24.1.3 vs Operating Contract §46). The Hydrology lane does **not** maintain a parallel schema home — only domain fixtures and lane documentation. [DIRRULES §12/§13.1, CONFIRMED]

[Back to top](#-hydrology--map-ui-contracts)

---

## 5. Hydrology `LayerManifest` profile

**Authority:** `LayerManifest` is owned by the cross-cutting Map family; the Hydrology lane supplies a **profile** — required fields, allowed values, and admission rules.

### 5.1 Required fields (PROPOSED profile)

| Field | Hydrology profile rule | Source authority |
|---|---|---|
| `layer_id` | Stable, lane-prefixed (PROPOSED convention: `hydrology.<object>.<source_family>.<vintage>`). | this profile |
| `title` | Human-readable; must distinguish **regulatory** vs **observed** vs **model-derived** layers verbatim. | NFHL invariant (§11) |
| `geometry_type` | Polygon (HUC, NFHL), line (flowline/reach), point (gauge, well), or raster (terrain-derived). | per object family |
| `source_id` | Must resolve to a registered `SourceDescriptor`. | source registry |
| `source_role` | One of the canonical seven (`observed` / `regulatory` / `modeled` / `aggregate` / `administrative` / `candidate` / `synthetic`). **Must not be elided.** | Atlas §24.1 |
| `source_layer` | Tile/source layer name (PMTiles/MVT). | TileArtifactManifest |
| `evidence_ref_field` | Field on the tile feature carrying `EvidenceRef` (or a feature_id resolvable to one). | EvidenceDrawerPayload |
| `temporal_fields` | Names of source-time / valid-time / observed-time / retrieval-time / release-time fields. | time discipline |
| `policy_label` | `public` for HUC, flowlines, NFHL context, gauge points; `restricted` or `review` where applicable. | policy/domains/hydrology/ |
| `release_state` | The released-layer status (see §10 — vocabulary CONFLICTED). | MAP-MASTER §10 / KFM-IDX-MAP-005 (NEEDS VERIFICATION) |
| `attribution` | Source attribution string (e.g., USGS, FEMA), exposed to the UI. | rights doctrine |
| `release_id` | Foreign key to `MapReleaseManifest`. | release authority |

> [!IMPORTANT]
> The renderer **MUST** refuse to load a layer source URL that does not appear in a **released** `MapReleaseManifest`. `addSource` / `addLayer` is blocked unless `LayerManifest`, `TileArtifactManifest`, `MapReleaseManifest`, and `PolicyDecision` all allow it — the no-unreleased-tile-load test. [MAP-MASTER §10, CONFIRMED]

### 5.2 Per-object admission rules

| Hydrology layer | `source_role` | Default release state | Special admission rule |
|---|---|---|---|
| HUC12 watershed | `regulatory` / authority-geometry | released (when promoted) | Must carry HUC12 fingerprint (PROPOSED validation). |
| NHDPlus HR flowline / catchment | authority network (VAAs are `modeled` lineage) | released (when promoted) | Identity ambiguity → `ABSTAIN` at drawer; do not render contested reach identity as canonical. |
| Gauge sites (USGS NWIS / Water Data API) | `observed` | released (when fresh); degraded/stale (when stale-window applies) | Stale-source rule applies (§12). |
| `FlowObservation` time-series | `observed` | degraded/bounded (operational freshness limit) | Never implies emergency or live authority unless current-cadence verification is recorded. |
| NFHL regulatory zones | `regulatory` (only) | released (when promoted) | **MUST** be styled and labeled distinctly from observed inundation. See §11. |
| Observed Flood Event | `observed` (historic) or `modeled` (reconstructed) | released or narrowed (precision) | Never collapsed with NFHL regulatory layer. |
| 3DEP terrain-derived hydrology context | `modeled` | released or degraded | Model lineage must be visible in drawer. |
| Water-quality / groundwater wells | `observed` | released → restricted per source-family | Private-property and well-owner sensitivity is a gate. |

<details>
<summary><strong>PROPOSED <code>LayerManifest</code> illustrative shape (hydrology HUC12 layer)</strong></summary>

```json
{
  "$schema": "https://kfm.example/schemas/contracts/v1/layers/layer_manifest.schema.json",
  "layer_id": "hydrology.huc12.wbd.2023q4",
  "title": "WBD HUC12 Subwatersheds (Kansas)",
  "geometry_type": "polygon",
  "source_id": "src:usgs:wbd:huc12",
  "source_role": "regulatory",
  "source_layer": "huc12",
  "evidence_ref_field": "evidence_ref",
  "temporal_fields": {
    "source_time": "src_time",
    "valid_time": "valid_time",
    "release_time": "rel_time"
  },
  "policy_label": "public",
  "release_state": "released",
  "attribution": "U.S. Geological Survey, Watershed Boundary Dataset",
  "release_id": "rel:hydrology:2026-05:001",
  "tile_artifact_ref": "tar:hydrology:huc12:pmtiles:<digest>",
  "style_ref": "sty:hydrology:base:v1",
  "sensitivity_label": "T0",
  "tags": ["hydrology", "watershed", "huc12"]
}
```

**Status:** PROPOSED illustrative. Field names trace to cross-cutting `LayerManifest` doctrine; `source_role` value (`regulatory` vs an authority/observation label) and the `release_state` enum both depend on the source-role-vocabulary and trust-state ADRs; exact field set requires the mounted-repo schema for confirmation.
</details>

[Back to top](#-hydrology--map-ui-contracts)

---

## 6. Hydrology `StyleManifest` profile

The hydrology style set has two non-negotiables: **role-distinct styling** and **trust-state visibility**.

| Style concern | Hydrology profile rule | Rationale |
|---|---|---|
| Regulatory vs observed | NFHL zones MUST use a visually distinct palette/pattern from observed-flood-event layers; legends MUST name the source role. | NFHL invariant (CONFIRMED) |
| Flow magnitude | Ramps carry units (cfs / m³·s⁻¹) and uncertainty banding; styles document the ramp in the `StyleManifest`. | ML-M-107 (PROPOSED) |
| Gauge state | Fresh / stale / degraded / denied each render with a distinct, accessible symbol — not by hidden style filters. | MAP-MASTER §10, trust-visible states |
| Sensitivity | Sensitive geometry MUST be **transformed** (generalized / redacted) upstream; styles MUST NOT be used as the only sensitivity mechanism. | sensitive-geometry deny rule (CONFIRMED) |
| Accessibility | Color choices meet WCAG contrast; legend text and badges have keyboard-reachable focus order and accessible names. | MAP-MASTER §12 a11y tests |
| Color, units, uncertainty, legend | Documented in `StyleManifest`, not inferred by the renderer. | ML-M-107 |

> [!WARNING]
> **Style filters are not a sensitivity control.** Hiding sensitive geometry behind a layout/paint expression is a recognized anti-pattern: the tile still ships the geometry and a curious client can read it. Sensitive transforms are upstream; style enforces visual discipline only. [MAP-MASTER §10, CONFIRMED]

[Back to top](#-hydrology--map-ui-contracts)

---

## 7. Hydrology `EvidenceDrawerPayload` projection

When a user clicks (or keyboard-activates) a hydrology feature, the governed API returns an `EvidenceDrawerPayload` — the **drawer is the inspection surface**. Popups and badges do not substitute for it.

### 7.1 Minimum payload contract (PROPOSED profile)

| Field | Purpose | Hydrology-specific note |
|---|---|---|
| `feature_id` | Stable identifier for the clicked feature | Provider-based where possible (e.g., gauge `site_no`, HUC12 code, NHDPlus permanent identifier). Identity rule: see [`identity-model.md`](./identity-model.md). |
| `layer_id` | The `LayerManifest` the feature belongs to | — |
| `evidence_bundle_refs` | One or more `EvidenceBundle` IDs | Always required for consequential claims. |
| `source_summary` | Source descriptor projection (name, role, authority, attribution) | Must name the source role. |
| `citations` | Citations resolving to authoritative source records | Resolved by `CitationValidationReport`. |
| `policy_state` | `PolicyDecision` summary | Includes deny reason where applicable. |
| `release_state` | The trust state (see §10) | Drawer MUST visibly show this. |
| `valid_time` / `observed_time` / `source_time` / `retrieval_time` / `release_time` | Time fields kept distinct | Hydrology must not collapse these. |
| `limitations` | Plain-language caveats | E.g., "NFHL is regulatory; not observed inundation." |
| `correction_link` | URL for the correction path | Must always be present, even when no correction exists. |
| `transforms` | Generalization / redaction record (where applicable) | Required when sensitive geometry has been transformed. |

### 7.2 Per-object drawer notes

| Hydrology object | Required drawer content |
|---|---|
| HUC12 watershed | HUC code, area, parent HUC, source descriptor (WBD), valid time, attribution. |
| NHDPlus flowline / reach | Permanent identifier, VAAs *labeled as model-derived*, identity-ambiguity flag if present. |
| Gauge site | Site number, parameter list, freshness state, **non-emergency caveat** if hydrologic risk is implied. |
| `FlowObservation` time series | Provider, parameter, units, no-data qualifiers, observation time, retrieval time. |
| NFHL zone | DFIRM_ID, VERSION_ID, EFFECTIVE_DATE, zone code, **role label: regulatory context**, NFHL-not-observed warning. |
| Observed Flood Event | Event identity, source-role, geometry vintage, public-safe transform record. |
| Water-quality observation | Method, detection limits, qualifiers, provenance. |
| Groundwater well | Owner-sensitivity check, restricted-geometry transform record if applicable. |

> [!CAUTION]
> **Required denial.** Drawer composition MUST `DENY` direct exposure of `Pre-RAW` / `RAW` / `WORK` / `QUARANTINE` references or canonical-store paths, even via link. The drawer is a release-state-aware surface only.

[Back to top](#-hydrology--map-ui-contracts)

---

## 8. `MapContextEnvelope` for hydrology

The `MapContextEnvelope` is the bounded scope sent to the governed API for clicks, timeline changes, and Focus Mode requests. The hydrology profile reuses the cross-cutting envelope without modification, with these usage notes:

- `visible_layers` MUST include only released hydrology layers (no candidate or watcher-only layers).
- `time_window` is the **valid-time** window the user selected, distinct from retrieval time. Snapshot resolution uses `LayerManifest` temporal metadata.
- `selected_features` carries hydrology feature ids resolvable through the drawer route.
- `evidence_refs` carries explicit `EvidenceRef`s when the click already resolved one; the API still re-resolves before answering.

> [!NOTE]
> **No raw features to model.** The envelope MUST NOT carry raw geometry payloads or unreleased model outputs. Its job is to bound scope, not to substitute for evidence. [MAP-MASTER §10, CONFIRMED]

[Back to top](#-hydrology--map-ui-contracts)

---

## 9. Focus Mode behavior in hydrology context

Focus Mode is the **bounded AI surface** over released hydrology `EvidenceBundle`s. Its outputs are finite, cited, and policy-checked.

| Question shape | Permitted outcome | Required guards |
|---|---|---|
| "Summarize this gauge's last 7 days of flow." | `ANSWER` over released observation `EvidenceBundle`, with citations | Time-window admissibility; gauge release state. |
| "Compare HUC12 X and Y by historical record." | `ANSWER` if both released; otherwise `ABSTAIN` with reason | Both HUC12 fingerprints validate; evidence closure passes. |
| "Is this property in a flood zone?" | `ABSTAIN` (regulatory-context interpretation) **or** `DENY` (out of scope: property-level claim) | NFHL invariant; never collapse regulatory and observed. |
| "Should I evacuate?" | `DENY` with safety reason and external-authority redirect | Emergency-use boundary — KFM is not an emergency authority. |
| "What is the reach identity here?" | `ABSTAIN` if NHDPlus identity is ambiguous | NHDPlus HR identity ambiguity tests (PROPOSED). |
| Any question lacking released evidence | `ABSTAIN` | Cite-or-abstain. |

> [!IMPORTANT]
> **Absolute prohibitions for Focus Mode in hydrology context** (CONFIRMED doctrine):
> - MUST NOT replace emergency alerting or official forecasts.
> - MUST NOT present NFHL regulatory zones as observed inundation or forecast.
> - MUST NOT answer uncited; if `CitationValidationReport` fails, `ABSTAIN`.
> - MUST NOT call a model runtime directly from the browser.

Every Focus call MUST emit an `AIReceipt` (provider, model, context, evidence refs, citation report id, finite outcome) and a `CitationValidationReport`. [MAP-MASTER §10, CONFIRMED]

[Back to top](#-hydrology--map-ui-contracts)

---

## 10. Trust-state vocabulary

> [!CAUTION]
> **CONFLICTED — trust-state enum.** This doc's v1 used a five-state enum `granted / narrowed / bounded / denied / candidate` attributed to `KFM-IDX-MAP-005`. The MapLibre Master corpus instead describes a renderer-boundary status vocabulary of **`released / stale / degraded / denied / unverified`** (plus `candidate` for watcher-emitted, never-public artifacts). The `KFM-IDX-MAP-005` id and the exact five-word `granted/narrowed/bounded` enum could **not** be confirmed in the corpus this session. Until an ADR settles the canonical enum, treat the mapping below as PROPOSED and surface both vocabularies; do not assert one as doctrine.

| State (PROPOSED) | Corpus analog | When a hydrology layer is in this state | Renderer behavior | Drawer behavior |
|---|---|---|---|---|
| `released` / granted | `released` | Layer released, fresh, all gates passed. | Render normally. | Full drawer payload. |
| `narrowed` | (transform of `released`) | Geometry generalized, attributes restricted, or coverage subset for sensitivity (e.g., restricted-geometry groundwater wells). | Render with narrowed-state indicator. | Drawer explains the transform; `transforms` field populated. |
| `bounded` / degraded / stale | `degraded` / `stale` | Confidence or freshness limit applies (e.g., stale gauge data within tolerance; modeled flow with uncertainty band). | Render with bounded/degraded indicator. | Drawer explains limits, including `valid_time` boundary. |
| `denied` | `denied` / `unverified` | Rights / sensitivity / release / review gate fails, or artifact unverified. | Layer absent or denied-state placeholder. | Drawer returns `DENY` with reason code; no feature payload. |
| `candidate` | `candidate` | Watcher emitted; not yet promoted. | **MUST NOT** render in public path. | n/a (not a public surface). |

> [!TIP]
> Mixed-trust-state scenes are an **open question**. Until an ADR settles composition rules, the recommended posture is **worst-state-per-frame** for hydrology scenes that mix layers, with per-layer indicators in the legend.

[Back to top](#-hydrology--map-ui-contracts)

---

## 11. Source-role separation (the NFHL invariant)

> [!WARNING]
> **CONFIRMED doctrine / non-negotiable.** NFHL regulatory flood zones are **regulatory context**, not observed inundation, not forecasts, not real-time hydraulic model output. The Hydrology lane MUST keep these source roles separated at every surface — schema, layer, style, drawer, Focus answer, citation, and policy decision. NFHL-as-observed-flood is a recognized DENY case. [Atlas §24.1.2]

| Source role | Hydrology objects | UI guarantees |
|---|---|---|
| `regulatory` | NFHL zones, WBD HUC boundary | Distinct style; legends say *regulatory*; drawer says *regulatory*. |
| authority network identity | NHDPlus HR / 3DHP | VAAs labeled as `modeled`; identity ambiguity → `ABSTAIN`. |
| `observed` | USGS gauge sites + `FlowObservation`, water-quality observations, groundwater wells, historical observed flood evidence | Time fields exposed; freshness state visible; never implies emergency authority. |
| context | Terrain-derived hydrology context (3DEP) | Drawer marks as derived; lineage visible. |
| `modeled` | Reconstructed flood evidence, hydraulic-model derivatives | Lineage visible; uncertainty banded in style; renderer must not present as observed. |

### 11.1 Collapsing failure modes

| Collapse | Why it fails | Required outcome |
|---|---|---|
| NFHL → observed inundation | Confuses regulatory determination with hydrologic event | `DENY` at drawer composition; `ABSTAIN` at Focus. |
| NFHL → forecast | Confuses regulation with prediction | `DENY` at drawer composition. |
| Gauge observation → emergency authority | KFM is not an emergency authority | `DENY` at Focus with redirect to official source. |
| NHDPlus model VAAs → observation | Confuses derived value with observed measurement | `ABSTAIN`; drawer labels model lineage. |

[Back to top](#-hydrology--map-ui-contracts)

---

## 12. Freshness, staleness, and the gauge timeline

Hydrology observations are **operationally current** but the map UI is not an emergency-grade surface. The contract:

- Every gauge-bound layer has a **declared cadence** in the `SourceDescriptor`.
- The `LayerManifest` carries the **stale window** beyond which the release state shifts from released to degraded/stale (visible badge) and then to denied (no public claim).
- The timeline shows **source time** vs **valid time** vs **retrieval time** vs **release time** distinctly.
- A no-change (304 / no-update) poll does **not** mint a new catalog entry or invalidate caches. [ML-062-020, CONFIRMED evidence / PROPOSED implementation]
- Stale state and degraded state are **separate** from denied state in the UI.

> [!NOTE]
> The exact freshness thresholds for KFM hydrology are **NEEDS VERIFICATION**. The hydrology source families (USGS Water Data / NWIS, NFHL, etc.) have their own cadences; KFM's stale-window policy must be set per source-family and recorded in `SourceDescriptor` + `LayerManifest`.

[Back to top](#-hydrology--map-ui-contracts)

---

## 13. Finite outcomes per surface

Every governed surface returns a finite outcome. The canonical sets are distinct by surface class: **governed-API / Focus** returns `ANSWER / ABSTAIN / DENY / ERROR`; the **promotion/release** decision returns `ALLOW / DENY / HOLD / ERROR`; **validators** return `PASS / FAIL / ERROR`. [Atlas §24.3]

| Surface | Outcomes | Forbidden behavior |
|---|---|---|
| Layer manifest resolver (per layer) | `ANSWER` / `DENY` / `ERROR` | Returning a layer without a `MapReleaseManifest`; serving `WORK` / `CATALOG` layers to the public path. |
| Hydrology feature / detail resolver | `ANSWER` / `ABSTAIN` / `DENY` / `ERROR` | Returning unreleased candidate features as `ANSWER`; exposing internal store identifiers; returning raw source bytes. |
| Evidence Drawer payload resolver | `ANSWER` / `ABSTAIN` / `DENY` / `ERROR` | Drawer payload without resolved `EvidenceBundle`; drawer that fronts an unreleased candidate. |
| Focus Mode (hydrology context) | `ANSWER` / `ABSTAIN` / `DENY` / `ERROR` | Uncited answers; safety/emergency advisory; collapsing NFHL with observed. |
| Promotion / release decision | `ALLOW` / `DENY` / `HOLD` / `ERROR` | Promotion without separation of duties for sensitive sub-domains; release without rollback target. |
| Correction submit (hydrology surface) | `ACCEPTED` / `DENY` / `ERROR` (PROPOSED surface-specific set) | Silent acceptance without review state. |

> [!NOTE]
> `ACCEPTED` for correction submission is a PROPOSED surface-specific label, not one of the three canonical KFM finite-outcome sets; it should be reconciled to a canonical set (or ratified as a distinct surface contract) by ADR.

[Back to top](#-hydrology--map-ui-contracts)

---

## 14. Validators & tests

The following test families apply to this contract. They mirror the MapLibre Master validation suite (§12) as it applies to hydrology; all are **PROPOSED** until mounted-repo evidence confirms implementation.

| Test family | Hydrology specialization | Status |
|---|---|---|
| Schema validation | Validate `LayerManifest`, `StyleManifest`, `TileArtifactManifest`, `MapReleaseManifest`, `EvidenceDrawerPayload`, `MapContextEnvelope`, `FocusModeRequest/Response`, `AIReceipt`, `CitationValidationReport`, `PolicyDecision` against hydrology fixtures. | PROPOSED |
| HUC12 fingerprint validation | One HUC12 fixture; geometry fingerprint regression. | PROPOSED |
| NHDPlus HR identity ambiguity | Force-ambiguity fixture; assert `ABSTAIN` at drawer / Focus. | PROPOSED |
| USGS Water Data normalization | Parameter / unit / qualifier / no-data tests over the gauge fixture. | PROPOSED |
| NFHL role-separation | Negative case: NFHL feature presented as observed → `DENY`. | PROPOSED |
| EvidenceBundle closure | Click resolves to a bundle; missing bundle → `ABSTAIN`. | PROPOSED |
| No public raw path | Browser cannot reach `Pre-RAW` / `RAW` / `WORK` / `QUARANTINE` / internal store. | PROPOSED |
| No unreleased tile load | Layer source URL appears in a released `MapReleaseManifest`; `addSource` blocked otherwise. | PROPOSED |
| Tile artifact integrity | `TileArtifactManifest` digest / `spec_hash` / sidecar (e.g., BAO root) checks; reject `invalid_spec_hash`, `unverified_tile_chunk`, `rollback_root_mismatch`. | PROPOSED |
| Stale source badge / abstain | Gauge cadence exceeded → degraded/stale state with badge; further → denied. | PROPOSED |
| Sensitive geometry deny | Style-only hiding insufficient; transforms required upstream; redaction receipt present. | PROPOSED |
| Citation validation | Focus answers cite resolvable `EvidenceRef`s or `ABSTAIN`. | PROPOSED |
| Focus Mode finite outcomes | `ANSWER` / `ABSTAIN` / `DENY` / `ERROR` over fixture answers. | PROPOSED |
| No-network hydrology proof fixture | End-to-end PR-safe test: HUC12 + one gauge + one NFHL context + one EvidenceBundle + one layer manifest + drawer payload. | PROPOSED |
| Rollback drill | A hydrology release manifest has a documented rollback target; replay restores prior state and old cache. | PROPOSED |
| Cache invalidation record | Old/new release ids + artifact digests recorded on rollback. | PROPOSED |
| Accessibility / a11y | Keyboard navigation, color contrast, alt text for legend and badges, screen-reader labels on trust-state indicators. | PROPOSED |
| Tile load budget / resource timing | p95 tile fetch within the declared SLO; PMTiles Range latency. | PROPOSED |

[Back to top](#-hydrology--map-ui-contracts)

---

## 15. Anti-patterns

> [!CAUTION]
> Each of the following is a recognized failure mode. The Hydrology lane MUST guard against them at the UI contract surface. [MAP-MASTER §13 Anti-Patterns Register]

| Anti-pattern | Why it fails | Required fix |
|---|---|---|
| Treating MapLibre, tiles, screenshots, or AI answers as sovereign truth | Renderer is downstream of trust. | Drawer + Focus Mode + governed routes. |
| Using popups in place of the Evidence Drawer | Popups cannot carry the full evidence + policy + release context. | Click resolves through governed API; drawer is the inspection surface. |
| Using badges as proof | A badge is a UI annotation; it does not replace receipts. | Badges link into drawer / receipt artifacts; never substitute for them. |
| Treating a checksum as publication proof | Checksums prove byte integrity, not origin or process. | Require `MapReleaseManifest` + provenance/SBOM referrers + signature/attestation. [ML-061-002] |
| Style-only sensitivity (paint/layout filters hiding geometry) | Tile still carries the geometry. | Upstream transforms in `data/processed/` and `data/published/`; receipts in `data/receipts/`. |
| Collapsing NFHL with observed flood | Regulatory context ≠ event evidence. | Source-role separation invariant (§11). |
| Implying emergency or live authority from a hydrology layer | KFM is not an emergency authority. | Non-emergency caveats; `DENY` at Focus; redirect to official sources. |
| Letting a candidate (watcher-emitted) layer appear in the public path | Watcher-as-non-publisher invariant. | Candidate stays out of public; only released enters the map. |
| Direct `addSource` on unverified PMTiles | Bypasses release & integrity gates. | Tile artifacts must appear in the released `MapReleaseManifest` and pass digest / sidecar checks. |
| Pretending docs are the authority | Docs explain; ADRs decide. | Promote authority claims to ADR / `control_plane/`. |

[Back to top](#-hydrology--map-ui-contracts)

---

## 16. Open questions & verification backlog

ADR-linked rows reference the open-ADR backlog (Atlas §24.12, Directory Rules §18).

| Item | What would settle it | Status |
|---|---|---|
| Trust-state enum: `granted/narrowed/bounded/denied/candidate` vs corpus `released/stale/degraded/denied/unverified (+candidate)`; existence of `KFM-IDX-MAP-005` | Mounted-repo `MAP_TRUST_STATES` standard + ADR | **CONFLICTED** |
| Exact governed-API routes for hydrology (feature, evidence, layer manifest, focus) | Mounted-repo `apps/governed-api/src/routes/*` and OpenAPI fixture. | NEEDS VERIFICATION |
| Schema home for the cross-cutting Map families (`layers/`, `ui/`, etc.) | `schemas/contracts/v1/...` files in a mounted repo. | NEEDS VERIFICATION |
| `SourceDescriptor` schema path: `source/source-descriptor.json` vs `sources/source_descriptor.schema.json` | ADR-0001 + DRIFT_REGISTER | **CONFLICTED** |
| `source_role` vocabulary (`authority/observation/context/model` used in v1 vs canonical seven `observed/regulatory/modeled/aggregate/administrative/candidate/synthetic`) | **ADR-S-04** + `SourceDescriptor` schema | **CONFLICTED** |
| Hydrology source-family freshness thresholds (USGS Water Data / NWIS, NFHL, NHDPlus HR vintages) | `SourceDescriptor` + `LayerManifest` cadence fields in fixtures. | NEEDS VERIFICATION |
| Mixed-trust-state scene composition rule (worst-state vs per-layer indicator vs composite) | Accepted ADR | OPEN |
| Layer naming convention (`hydrology.<object>.<source_family>.<vintage>`) | Confirmed in the source-registry / control-plane register. | PROPOSED |
| Provider-based `feature_id` rules for gauges and HUCs (see identity-model deterministic basis) | ADR + fixture. | PROPOSED |
| `ACCEPTED` correction-submit outcome vs canonical finite-outcome sets | ADR (surface-contract reconciliation) | PROPOSED |
| `PROV.md` vs `PROVENANCE.md` naming | Directory Rules **OPEN-DR-01** (PROV.md is the live artifact) | OPEN |
| `tools/` validator exit-code contract for hydrology fixtures | Validator README + exit-code matrix (DIRRULES OPEN-DR-03) | OPEN |
| Crosswalk/feature validator home (if reused at the UI boundary) | **ADR-S-CWV-01** | CONFLICTED |

[Back to top](#-hydrology--map-ui-contracts)

---

## 17. Related docs

> Many of these are PROPOSED paths; replace with actual repo paths once verified. Inbound links from these docs SHOULD point to this contract.

- [`ai-build-operating-contract.md`](../../../ai-build-operating-contract.md) — operating contract; `CONTRACT_VERSION = "3.0.0"`
- [`directory-rules.md`](../../../directory-rules.md) — placement law (§12), compatibility roots, OPEN-DR-01/03
- [`docs/domains/hydrology/INDEX.md`](./INDEX.md) — hydrology lane index (companion)
- [`docs/domains/hydrology/README.md`](./README.md) — hydrology lane landing page (PROPOSED)
- [`docs/domains/hydrology/identity-model.md`](./identity-model.md) — feature identity (companion)
- [`docs/domains/hydrology/DATA_LIFECYCLE.md`](./DATA_LIFECYCLE.md) — gates and lifecycle (companion)
- [`docs/domains/hydrology/GLOSSARY.md`](./GLOSSARY.md) — ubiquitous-language glossary (companion)
- `docs/architecture/map-shell.md` — map shell architecture (PROPOSED)
- `docs/architecture/governed-api.md` — governed API trust membrane (PROPOSED)
- `docs/standards/MAP_TRUST_STATES.md` — trust-state vocabulary and composition rules (PROPOSED; resolves the §10 CONFLICTED enum)
- [`docs/standards/PROV.md`](../../standards/PROV.md) — provenance standard profile
- [`docs/standards/PMTILES.md`](../../standards/PMTILES.md) — PMTiles standard profile
- [`docs/standards/OGC-API-TILES.md`](../../standards/OGC-API-TILES.md) — OGC API · Tiles profile
- `docs/runbooks/hydrology/SOURCE_REFRESH_RUNBOOK.md` — hydrology source-refresh runbook (PROPOSED; analog of the fauna runbook, Pattern A pending ADR-S-13)
- `schemas/contracts/v1/layers/layer_manifest.schema.json` — `LayerManifest` schema (PROPOSED home)
- `schemas/contracts/v1/ui/evidence_drawer_payload.schema.json` — `EvidenceDrawerPayload` schema (PROPOSED home)
- `schemas/contracts/v1/source/source-descriptor.json` — shared `SourceDescriptor` schema (`source/` vs `sources/` CONFLICTED)
- `policy/domains/hydrology/` — hydrology policy lane (PROPOSED home)
- `tests/domains/hydrology/` · `fixtures/domains/hydrology/` — hydrology tests / fixtures (PROPOSED homes)

[Back to top](#-hydrology--map-ui-contracts)

---

## 18. Changelog v1 → v2

| Change | Type (per contract §37) | Reason |
|---|---|---|
| Pinned `CONTRACT_VERSION = "3.0.0"` in meta block, badge row, status line, footer | conformance | Doctrine-adjacent standard doc must pin per AIBOC v3.0. |
| Fixed `doc_id` from `kfm://doc/hydrology-map-ui-contracts-v1` to slug `kfm://doc/domains/hydrology/map-ui-contracts` | reconciliation | Match sibling-doc id style; remove version from the id. |
| Reclassified the trust-state enum to **CONFLICTED** (§10, OQ): surfaced both the v1 `granted/narrowed/bounded/denied/candidate` and the corpus `released/stale/degraded/denied/unverified (+candidate)`; flagged `KFM-IDX-MAP-005` as NEEDS VERIFICATION | reconciliation | The corpus renderer-boundary status words differ from v1's enum; the cited id could not be confirmed. Surfaced, not smoothed. |
| Reconciled `source_role` to the canonical seven (`observed/regulatory/modeled/aggregate/administrative/candidate/synthetic`); flagged the v1 `authority/observation/context/model` set as CONFLICTED (ADR-S-04) | reconciliation | v1 used a four-value set; the Atlas source-role register is the canonical seven, fixed at admission. |
| Distinguished the three finite-outcome sets (API `ANSWER/ABSTAIN/DENY/ERROR`; promotion `ALLOW/DENY/HOLD/ERROR`; validator `PASS/FAIL/ERROR`); flagged `ACCEPTED` as a PROPOSED surface-specific label | clarification | v1 §13 mixed a review-queue `ALLOW/RESTRICT/DENY/HOLD` row and `ACCEPTED` with the API set. [Atlas §24.3] |
| Surfaced `SourceDescriptor` schema-home `source/` vs `sources/` as CONFLICTED (§4 note, §17, OQ) | gap closure | Consistent with the lane suite; v1 named only `schemas/contracts/v1/...` generically. |
| Added `Pre-RAW` to the no-public-path drawer denial and test family | gap closure | Pre-RAW is a CONFIRMED lifecycle phase; the membrane must deny it too. |
| Added tile-integrity test row (digest / `spec_hash` / BAO sidecar; `invalid_spec_hash`, `unverified_tile_chunk`, `rollback_root_mismatch`) and a checksum-≠-proof anti-pattern | clarification | Aligns with MAP-MASTER PMTiles publication gates (ML-058-016/017/018) and ML-061-002. |
| Added companion cross-links (INDEX, identity-model, DATA_LIFECYCLE, GLOSSARY) and the operating contract to `related` | clarification | Aligns the seven-doc hydrology suite. |
| Rewrote both Mermaid diagrams to remove reserved characters (`( ) / + -`) that break GitHub rendering | housekeeping | KFM Mermaid label discipline. |
| Split Changelog out as §18 | housekeeping | Companion-section pattern. |

> **Backward compatibility.** Section anchors `#1`–`#17` and the page anchor are preserved; a new §18 (Changelog) is appended. The meta-block `doc_id` changed (slug normalization, version removed from id) — any consumer referencing `kfm://doc/hydrology-map-ui-contracts-v1` must repoint. No in-document heading anchors changed.

[Back to top](#-hydrology--map-ui-contracts)

---

<!-- footer -->

> Hydrology Map UI Contracts · profile of cross-cutting Map UI families for the Hydrology lane.
>
> _**Authority basis.**_ Cross-cutting object families and the governed-API outcome envelope are **CONFIRMED doctrine** in the KFM corpus (MapLibre Master §7.M, §10, §12–§13). Hydrology lane object definitions and NFHL source-role separation are **CONFIRMED doctrine** (Atlas §24.1.2). The trust-state enum is **CONFLICTED** (§10). All repo paths, route names, and schema homes named here are **PROPOSED** until verified against a mounted repository. Bend an invariant only via ADR.

**Related:** [`directory-rules.md`](../../../directory-rules.md) · [`docs/domains/hydrology/INDEX.md`](./INDEX.md) · `docs/standards/MAP_TRUST_STATES.md` · [`docs/standards/PROV.md`](../../standards/PROV.md)

**Status:** draft · **Version:** v2 · **Contract:** `CONTRACT_VERSION = "3.0.0"` · **Last updated:** 2026-06-06 · **Maintainers:** hydrology lane steward, map shell owner, governance reviewer (placeholders) · **Review cadence:** quarterly or on any change to cross-cutting Map UI families.

[Back to top](#-hydrology--map-ui-contracts)
