---
title: "🗺️ Kansas Frontier Matrix — Map & Layer Utilities (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/src/utils/map/README.md"

version: "v11.2.6"
last_updated: "2025-12-15"
review_cycle: "Quarterly · FAIR+CARE Council & Web Architecture Board"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
content_stability: "stable"

status: "Active / Enforced"
doc_kind: "Architecture"
header_profile: "standard"
footer_profile: "standard"
diagram_profiles:
  - "mermaid-flowchart-v1"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../releases/v11.2.6/sbom.spdx.json"
manifest_ref: "../../../../releases/v11.2.6/manifest.zip"
telemetry_ref: "../../../../releases/v11.2.6/focus-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/web-utils-map-v11.json"
energy_schema: "../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11.0"
pipeline_contract_version: "KFM-PDC v11.0"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

intent: "web-map-utilities"
role: "frontend-map-layer-logic"
category: "Web · Utilities · MapLibre · Layers"

classification: "Public Document"
fair_category: "F1-A1-I1-R1"
care_label: "Public · Governed"
sensitivity_level: "Low"
public_exposure_risk: "Low"
indigenous_rights_flag: true
risk_category: "Low"
redaction_required: false
data_steward: "KFM FAIR+CARE Council"

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "SoftwareSourceCode"
  owl_time: "TemporalEntity"
  prov_o: "prov:Plan"
  geosparql: "geo:FeatureCollection"

provenance_chain:
  - "web/src/utils/map/README.md@v10.4.1"
provenance_requirements:
  versions_required: true
  newest_first: true

json_schema_ref: "../../../../schemas/json/web-utils-map-readme-v11.schema.json"
shape_schema_ref: "../../../../schemas/shacl/web-utils-map-readme-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:web-utils-map-readme:v11.2.6"
semantic_document_id: "kfm-doc-web-utils-map-readme"
event_source_id: "ledger:web/src/utils/map/README.md"
immutability_status: "version-pinned"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "semantic-highlighting"
  - "a11y-adaptations"
ai_transform_prohibited:
  - "summaries"
  - "speculative-additions"
  - "unverified-historical-claims"
  - "relationship-fabrication"
  - "governance-override"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
ttl_policy: "Annual review"
sunset_policy: "Superseded on next map-utils revision"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 🗺️ **Kansas Frontier Matrix — Map & Layer Utilities (v11.2.6)**
`web/src/utils/map/README.md`

**Purpose**  
Define the **MapLibre-focused utility layer** that transforms KFM catalog + graph outputs into
**deterministic, governance-safe map layers** and stable interaction primitives used by the Web Platform.

These utilities are intentionally **pure** (data → data), **TypeScript-strict**, and **FAIR+CARE + sovereignty aware**:
they preserve licenses/attribution, prevent precision leaks (masked/restricted sites), and keep map/timeline/Focus Mode
synchronization consistent across devices.

</div>

---

## 📘 Overview

`web/src/utils/map/**` is the **front-end mapping utility layer** that sits between:

- **Catalog + graph metadata** (STAC/DCAT, graph entities, Story Nodes, Focus Mode payloads), and
- **MapLibre runtime configuration** (sources, layers, filters, legends, and selection logic).

Primary responsibilities:

- Convert **STAC Items/Collections** (and DCAT-derived metadata) into **MapLibre source + layer descriptors**
  without mutating MapLibre state directly.
- Provide a **single visual language** via shared style tokens (colors/opacities/zoom thresholds) for KFM layers
  (historic maps, environmental layers, settlements/places, documents/media overlays).
- Provide deterministic **bbox and viewport math** (merge/pad/fit) for:
  - “Zoom to layer”
  - “Zoom to Focus Mode context”
  - Timeline-driven camera updates
- Provide safe **feature selection and time filtering** (by ID, properties, temporal windows) and return stable
  “clicked entity” descriptors for Focus Mode + Story Nodes.
- Preserve and propagate **FAIR+CARE + sovereignty metadata** so the UI can:
  - display license/attribution
  - label restricted/generalized geometries correctly
  - avoid exposing disallowed precision (e.g., culturally sensitive locations)

Hard constraints:

- No network calls, no file I/O, no DOM access, no global state.
- Framework-agnostic: no React imports.
- Same input → same output (deterministic; no `Date.now()`, no randomness).
- Never sharpen uncertain or masked geometry/time into a “more precise” representation.

---

## 🗂️ Directory Layout

~~~text
📁 web/src/utils/map/                                  — MapLibre + layer utilities (pure functions)
├── 📄 README.md                                       — This document (architecture + rules)
├── 📄 stacToMaplibre.ts                               — STAC Item/Collection → MapLibre source/layer descriptors
├── 📄 layerStyles.ts                                  — Shared style tokens (colors, widths, opacities, zoom thresholds)
├── 📄 bboxUtils.ts                                    — BBox + viewport helpers (merge, pad, fit; antimeridian-safe)
├── 📄 featureSelectors.ts                             — Feature selection/filtering (IDs, properties, time windows)
├── 📄 interactions.ts                                 — Hit-test interpretation helpers (click/hover → stable selection)
└── 📄 legends.ts                                      — Legend/value mapping helpers (categorical + continuous ramps)
~~~

---

## 🧭 Context

KFM’s web map is designed to render **historical and modern geospatial layers** using MapLibre as the primary renderer
(with optional Leaflet usage for lighter-weight or specialized cases). Layers and map behavior are driven by:

- **Data catalogs (STAC/DCAT)**: layer availability, temporal extent, spatial footprint, licenses, attribution
- **Knowledge graph entities**: Places/Events/Story Nodes and their linked geometries
- **Focus Mode & timeline**: synchronized “what / when / where” context windows

This utility layer exists to keep mapping behavior:

- **Declarative** (derived descriptors, not ad-hoc mutations)
- **Governed** (CA(R)E labels and masking behavior preserved)
- **Consistent** (timeline ↔ map synchronization does not drift across pages/components)
- **Performant** (large data pushed to tiles when possible; avoid giant GeoJSON in UI)

---

## 🧱 Architecture

### 1) `stacToMaplibre.ts` — Catalog → Runtime Layer Descriptors

Goal: transform catalog records into a stable “map layer descriptor” that the UI can mount/unmount predictably.

Typical inputs:

- STAC Item/Collection metadata (assets, roles, bbox/geometry, datetime / extent)
- Optional DCAT metadata (license text, publisher, distribution hints)
- Optional KFM governance overlays (CARE label, sensitivity, masking policy)
- Optional style options (layer kind, category, default visibility)

Typical outputs:

- MapLibre `source` definition (raster tiles, vector tiles, GeoJSON source, etc.)
- One or more MapLibre `layer` specs (fill/line/symbol/raster/hillshade/etc.)
- A stable `id` namespace usable across:
  - map layers
  - legends
  - telemetry events
  - URL-safe references (when allowed)

Design rule: if an asset is restricted or generalized, the output must reflect that restriction in:
- layer metadata (labels / flags)
- geometry resolution (generalized tiles or aggregated geometry)
- attribution text (rights-holder / restriction notice)

### 2) `layerStyles.ts` — Single Visual Language

Goal: centralize all map styling so the UI never hardcodes styles in components.

Expected contents:

- Palette + contrast-safe tokens (including high-contrast mode)
- Opacity and blending rules (historic basemap overlays, hillshade, raster transparency)
- Category mapping for KFM layer families (examples: “Maps”, “Environment”, “Settlements”, “Documents”)
- Zoom thresholds and symbol density rules
- Focus Mode highlight styles (selected / hovered / related / suppressed)

Governance rule: styles may signal “restricted/generalized” via patterns (e.g., hatch, dashed outline), but must not
imply exact precision when the data is generalized.

### 3) `bboxUtils.ts` — Spatial Extents, Safely

Goal: deterministic bbox math for map camera controls and UI framing.

Must handle:

- Merging multiple bboxes
- Padding bboxes for better framing
- Clamping to valid world bounds
- Edge cases:
  - antimeridian crossing
  - tiny extents (point-like layers)
  - mixed geometry precision (points + polygons)
  - invalid/inverted bboxes (repair or reject deterministically)

Sovereignty rule: for generalized or restricted entities, the bbox returned must not defeat masking (e.g., do not
compute a tight bbox from a restricted point geometry).

### 4) `featureSelectors.ts` — Selection + Filtering (IDs, Props, Time)

Goal: deterministic feature selection and filtering primitives used by Focus Mode, Story Nodes, and timeline.

Must support:

- Select by stable IDs (graph IDs, dataset IDs, feature IDs)
- Filter by property predicates (category, layer flags, governance labels)
- Filter by temporal window (timeline start/end → MapLibre filter or GeoJSON filter)
- Return stable ordering for UI lists and consistent “top hit” selection

Governance rule: filtering must not “reconstruct” hidden features (e.g., by intersecting multiple filters to infer
restricted locations).

### 5) `interactions.ts` — Map Event Interpretation Without UI State

Goal: interpret MapLibre event payloads into stable, typed selection outputs:

- click/hover event → `{ layerId, featureId, lngLat?, properties?, entityRef? }`
- prioritization rules for overlapping features (e.g., focus highlights > selected layer > basemap)
- safe fallbacks (no crash when properties missing)
- consistent hit resolution across devices

No DOM dependencies: MapLibre objects may be passed in by the caller, but not created here.

### 6) `legends.ts` — Legends From Styles + Metadata

Goal: build legend models for UI components using:

- style tokens from `layerStyles.ts`
- STAC asset metadata (bands, units, nodata, value ranges)
- layer category/type hints (categorical vs continuous)

Legend outputs must include:

- labels
- color/ramp descriptors
- units (when known)
- attribution hooks (license/source) where displayed alongside legends

---

## 📦 Data & Metadata

KFM map utilities should exchange **explicit, typed descriptors** rather than raw MapLibre objects scattered across UI.

Recommended descriptor shape (conceptual):

~~~ts
export type KfmCareLabel = "Public" | "Public · Governed" | "Restricted" | "Restricted · Generalized";

export interface KfmGovernanceMeta {
  careLabel: KfmCareLabel;
  sensitivityLevel?: "None" | "Low" | "Moderate" | "High";
  indigenousRightsFlag?: boolean;
  masking?: { strategy: "none" | "generalized" | "suppressed"; note?: string };
  license?: string;
  rightsHolder?: string;
}

export interface KfmProvenanceMeta {
  sourceId?: string;              // dataset/stac/dcat id (stable)
  provWasDerivedFrom?: string[];  // PROV links (ids or paths)
  manifestRef?: string;           // release manifest reference (path)
  sbomRef?: string;               // SBOM reference (path)
}

export interface MapLayerDescriptor {
  id: string;                     // stable, deterministic
  title: string;                  // UI label
  kind: "raster" | "vector" | "geojson";
  temporal?: { start?: string; end?: string; precision?: string; approx?: boolean };
  bbox?: [number, number, number, number] | null;

  source: unknown;                // MapLibre source spec (kept structural + serializable where possible)
  layers: unknown[];              // MapLibre layer specs

  governance: KfmGovernanceMeta;
  provenance?: KfmProvenanceMeta;
  attribution?: { text: string; url?: string };
}
~~~

Notes:

- Keep descriptors serializable where possible (helps telemetry, caching, snapshot export).
- Carry governance/provenance through every transformation; never drop them “for convenience”.
- Any “unknown” types above should map to MapLibre style spec types in implementation; docs remain renderer-agnostic.

---

## 🌐 STAC, DCAT & PROV Alignment

Map utilities must treat STAC/DCAT/PROV as first-class inputs/outputs:

- STAC:
  - Interpret Item/Collection `bbox`, `geometry`, `datetime` / temporal extent
  - Prefer explicit `assets` roles + media types for source selection
  - Respect projection/metadata extensions when present (do not guess CRS details)
- DCAT:
  - Surface license/rights/publisher as attribution metadata and UI disclosure
  - Use DCAT distribution hints to choose “best” render pathway (tiles vs files) without inventing data
- PROV:
  - Preserve provenance links so the UI can show “where this layer came from”
  - Never claim an entity was derived from a source unless provided by the API/catalog

Governance rules apply across all three:
- if an asset is marked restricted/generalized, the rendered representation must not undermine that policy.

---

## 🧠 Story Node & Focus Mode Integration

Map utilities are a critical bridge for:

- **Focus Mode v3**: highlight focal entity geometry, related clusters, and evidence-linked places/events
- **Story Node v3**: show story geography, related layers, and the story’s temporal window on the map
- **Timeline ↔ Map sync**:
  - timeline window → map filters / opacity gates
  - selected story/event → bbox fit + focus highlight layer

Required behaviors:

- Selecting a Story Node must produce:
  - a safe bbox (never defeats masking)
  - stable layer/feature IDs for highlights
  - deterministic “related entities” selection ordering
- Time filters must:
  - preserve uncertainty (approx/decade/century)
  - avoid “pinpointing” a range to a specific day/year when the source is fuzzy

---

## 🗺️ Diagrams

~~~mermaid
flowchart TD
  A["STAC / DCAT Catalog Records"] --> B["stacToMaplibre.ts<br/>descriptor build"]
  C["Graph Entities<br/>(Place/Event/StoryNode)"] --> D["featureSelectors.ts<br/>id + time filtering"]
  B --> E["MapLayerDescriptor[]"]
  D --> E
  E --> F["React Map Components<br/>(MapLibre runtime)"]
  F --> G["interactions.ts<br/>click/hover interpretation"]
  G --> H["Focus Mode v3 / Story Node v3<br/>selection + highlighting"]
  H --> I["bboxUtils.ts<br/>fit + clamp"]
  I --> F
  J["layerStyles.ts<br/>tokens"] --> B
  J --> F
  K["legends.ts<br/>legend models"] --> F
~~~

---

## 🧪 Validation & CI/CD

Minimum expectations:

- Unit tests for:
  - STAC → MapLibre descriptor determinism
  - bbox math (including antimeridian and tiny extents)
  - selection and time filtering semantics
  - legend generation correctness
  - governance retention (license/careLabel/masking flags never dropped)
- Integration tests for:
  - Focus Mode selection → highlight layer outputs
  - timeline window → filter expression generation (where implemented)
- Lint / format:
  - TypeScript strict mode; no implicit any
  - stable sorting rules for any collection outputs
- Governance gates:
  - any coordinate-precision leak or sovereignty violation must be CI-blocking
  - telemetry emission (if any upstream) must be schema-valid and PII-free

Expected test locations:

~~~text
📁 tests/
├── 📁 unit/web/utils/map/            — unit tests for each module
└── 📁 integration/web/utils/map/     — Focus/Story/Timeline integration cases
~~~

---

## ⚖ FAIR+CARE & Governance

Map utilities are a high-risk surface because they handle geometry and interaction.

Non-negotiable rules:

- No precise coordinates for restricted content:
  - if input is generalized, do not “tighten” bbox/geometry
  - if input is suppressed, do not render a proxy that reveals location
- No inference-by-intersection:
  - do not allow UI filters to reconstruct restricted location by combining public layers
- Always preserve:
  - `careLabel`
  - sensitivity flags
  - license/rights-holder attribution
  - provenance pointers (when provided)

Recommended safety patterns:

- Default to generalized extents for any entity with `indigenousRightsFlag: true` unless explicitly public-safe.
- Prefer aggregation layers (grid/hex/H3) for sensitive point sets.
- Ensure style tokens for restricted layers communicate “generalized” without implying exactness.

---

## 🕰️ Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v11.2.6 | 2025-12-15 | Upgraded to KFM-MDP v11.2.6; standardized headings/order/fences; expanded architecture for STAC/DCAT/PROV alignment, Focus Mode v3 + Story Node v3 integration, governance-safe bbox/selection rules, and CI expectations. |
| v10.4.1 | 2025-11-15 | Initial creation under legacy v10.4 documentation patterns; introduced STAC→MapLibre transforms, style tokens, bbox helpers, selection, interactions, and legend utilities. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — MIT License  
FAIR+CARE Aligned · Public Document · Version-Pinned · Sovereignty-Safe

[⬅️ Back to Web Utils](../README.md) ·
[🧭 Web Source Overview](../../README.md) ·
[🌐 Web Platform Overview](../../../README.md) ·
[🛡 Governance Charter](../../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>
