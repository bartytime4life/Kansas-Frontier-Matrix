---
title: "KFM Web Map Layers — README"
path: "web/src/map/layers/README.md"
version: "v1.0.0"
last_updated: "2025-12-25"
status: "draft"
doc_kind: "Guide"
license: "CC-BY-4.0"

markdown_protocol_version: "KFM-MDP v11.2.6"
mcp_version: "MCP-DL v6.3"
ontology_protocol_version: "KFM-ONTO v4.1.0"
pipeline_contract_version: "KFM-PPC v11.0.0"

stac_profile: "KFM-STAC v11.0.0"
dcat_profile: "KFM-DCAT v11.0.0"
prov_profile: "KFM-PROV v11.0.0"

governance_ref: "docs/governance/ROOT_GOVERNANCE.md"
ethics_ref: "docs/governance/ETHICS.md"
sovereignty_policy: "docs/governance/SOVEREIGNTY.md"

fair_category: "FAIR+CARE"
care_label: "TBD"

sensitivity: "public"
classification: "open"
jurisdiction: "US-KS"

doc_uuid: "urn:kfm:doc:web:map:layers:readme:v1.0.0"
semantic_document_id: "kfm-web-map-layers-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:web:map:layers:readme:v1.0.0"
commit_sha: "<latest-commit-hash>"

ai_transform_permissions:
  - "summarize"
  - "structure_extract"
  - "translate"
  - "keyword_index"
ai_transform_prohibited:
  - "generate_policy"
  - "infer_sensitive_locations"

doc_integrity_checksum: "sha256:<calculate-and-fill>"
---

<div align="center">

# 🗺️ KFM Web Map Layers

`web/src/map/layers/`

</div>

> **Purpose (required):** Define how **map layers** are registered, validated, and rendered in the KFM web UI
> (MapLibre-first; optionally Cesium), while enforcing the **UI→API boundary**, provenance visibility, and
> governance constraints.

## 📘 Overview

### Purpose

This README governs:

- how we represent a “layer” in the KFM web UI,
- how layer metadata connects back to **catalogs (STAC/DCAT/PROV)** and **API contracts**,
- how layers behave in **Focus Mode** (story-driven map context),
- what must be validated (schemas, contracts, forbidden patterns) before a layer is considered “integrated.”

### Scope

| In Scope | Out of Scope |
|---|---|
| Layer registry conventions (IDs, metadata, sensitivity flags, provenance pointers) | Writing ETL, generating STAC/DCAT/PROV artifacts |
| Map renderer integration patterns (MapLibre; optional Cesium parity) | Defining new ontology classes/relationships |
| Focus Mode layer toggles + map/timeline sync expectations | UI styling system choices (CSS framework, etc.) |
| Validation & CI expectations for layers | Non-map UI features |

### Audience

- **Primary:** Frontend contributors implementing/maintaining map layers and Focus Mode UX.
- **Secondary:** API contributors ensuring map layers have stable, contract-first endpoints.

### Definitions

- Link: `docs/glossary.md`
- Terms used here: **Layer registry**, **LayerSpec**, **Source**, **Provenance**, **Context bundle**, **Focus Mode**.

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| This README | `web/src/map/layers/README.md` | UI | Governed layer conventions |
| Master pipeline + invariants | `docs/MASTER_GUIDE_v12.md` | KFM Core | Canonical ordering + invariants |
| Story Node template | `docs/templates/TEMPLATE__STORY_NODE_V3.md` | Narrative | Focus Mode hints: `focus_layers`, `focus_center`, `focus_time` |
| API contracts | `src/server/contracts/**` | API | Map-visible data should have contracts |
| UI schema (if present) | `schemas/ui/**` | Platform/UI | Validates layer registry/config (**not confirmed in repo**) |

### Definition of done (for this document)

- [ ] Front-matter complete + valid (`path` matches file location)
- [ ] “LayerSpec” contract is explicit (required fields + prohibited patterns)
- [ ] Focus Mode integration rules are described (layer toggles + provenance visibility)
- [ ] Validation steps are repeatable (even if commands are placeholders)
- [ ] Governance considerations explicitly called out (sensitive locations, sovereignty)

## 🗂️ Directory Layout

### This document

- `path`: `web/src/map/layers/README.md` (must match front-matter)

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| Data domains | `data/` | Raw/work/processed + published artifacts |
| Catalog outputs | `data/stac/`, `data/catalog/dcat/`, `data/prov/` | Machine-readable discovery + lineage |
| Graph build | `src/graph/` | Ontology bindings + graph build scripts |
| API boundary | `src/server/` | Contract-first access layer (REST/GraphQL) |
| UI | `web/` | React map UI; layer registry lives under `web/**/layers/**` |
| Story Nodes | `docs/reports/story_nodes/` | Governed narrative artifacts |

### Expected file tree for this sub-area

> Note: Keep this tree synchronized with the actual files present. If the registry implementation differs, update this README.

~~~text
📁 web/
└── 📁 src/
    └── 📁 map/
        └── 📁 layers/
            ├── 📄 README.md
            ├── 📄 <layer-registry-implementation> (not confirmed in repo)
            ├── 📄 <layer-types-or-specs> (not confirmed in repo)
            └── 📁 <layer-assets> (icons/legends) (not confirmed in repo)
~~~

## 🧭 Context

### Why layers are governed in KFM

KFM’s UI is not a “freeform map.” It is the final stage of a governed pipeline:

**ETL → STAC/DCAT/PROV → Graph → API → UI → Story Nodes → Focus Mode**

Layers are the UI’s **most common “contract surface”**:

- a layer that renders data implies a backing dataset and/or API contract,
- a layer can unintentionally reveal sensitive locations through zoom/interaction,
- a layer is often used by Focus Mode as part of narrative context.

### Non-negotiable UI constraints

- **No UI direct-to-graph reads:** the web client must never bypass the API to query Neo4j.
- **Provenance-first rendering:** whenever the UI shows factual content in Focus Mode, it must be traceable to sources, and any AI-derived content (if present) must be opt-in and clearly labeled.

(If these constraints evolve, the authoritative source is the Master Guide and governance docs.)

## 🗺️ Diagrams

### Layer dataflow in the canonical pipeline

~~~mermaid
flowchart LR
  A[STAC/DCAT/PROV<br/>data/stac + data/catalog/dcat + data/prov] --> B[Graph<br/>src/graph]
  B --> C[API Boundary<br/>src/server]
  C --> D[UI Layer Registry<br/>web/**/layers/**]
  D --> E[Map Renderers<br/>MapLibre (2D) / Cesium (3D optional)]
  E --> F[User Interactions<br/>toggle / hover / click / filter]
~~~

### Focus Mode layer activation (story-driven)

~~~mermaid
sequenceDiagram
  participant U as User
  participant UI as Web UI (Map + Panels)
  participant API as API Boundary
  participant S as Story Node Content

  U->>UI: Open story/entity (Focus Mode)
  UI->>API: Fetch context bundle (entity_id, time_window)
  API-->>UI: Narrative + citations + map hints + data refs
  UI->>S: Render story markdown + citations
  UI->>UI: Apply focus_layers / focus_center / focus_time
~~~

## 📦 Data & Metadata

### What is a “Layer” in KFM UI?

A KFM layer should be representable as a **LayerSpec** (JSON or TS), registered in a **layer registry** that can drive:

- toggle controls,
- renderer construction (MapLibre layer + source; optional Cesium equivalent),
- legends and attributions,
- provenance / audit panel links,
- sensitivity / redaction behaviors.

> Implementation note: the implementation guide describes a layer registry as a JSON configuration listing layer name, source URL, attributions, and sensitivity; new layers can be added by updating the config (extensible without code changes). If our implementation differs, align this README to the actual approach.

### Recommended LayerSpec fields

This is the **minimum** we recommend for stable governance and Focus Mode integration:

- **Identity**
  - `id` (stable, unique; used by Focus Mode `focus_layers`)
  - `title` (human readable)
  - `description` (what it represents; what it’s *not*)
- **Type & rendering**
  - `kind` (e.g., `vector`, `raster`, `terrain`, `reference`)
  - `rendererTargets` (e.g., `maplibre`, `cesium`, `both`)
  - `defaultVisibility` (boolean)
  - `minZoom` / `maxZoom` (optional)
- **Source binding**
  - `sourceType` (e.g., `api`, `stac-asset`, `tile-service`)
  - `sourceRef` (API route name / STAC item/collection ID / tile URL)
  - `attribution` (license + provider)
- **Provenance & catalogs**
  - `stac_collection_ids` / `stac_item_ids` (optional)
  - `dcat_dataset_ids` / `dcat_distribution_ids` (optional)
  - `prov_activity_ids` (optional)
- **Governance**
  - `sensitivity` / `classification` (mirror front-matter vocabulary)
  - `redactionPolicy` (e.g., aggregation level, geometry generalization) (optional)
  - `accessTier` (e.g., public/internal) (**not confirmed in repo**)

### Suggested ID conventions

- Prefer **stable IDs** that do not change when titles/labels change.
- If versioning is needed, version the **layer spec** without breaking `id` (or adopt a stable “alias” mapping).

(**Not confirmed in repo** — adopt the project’s established naming standard if one exists.)

## 🌐 STAC, DCAT & PROV Alignment

### Principle: layers should point back to evidence

When a layer is backed by a dataset, it should be possible to trace:

- UI layer → API response → provenance refs → catalog entries (STAC/DCAT) → raw sources (via PROV).

### Practical expectations

- If a layer uses **static artifacts** (GeoJSON/COG/tiles), prefer that those artifacts are registered in STAC/DCAT and have PROV lineage.
- If a layer uses **API endpoints**, the API should return provenance references (or IDs) sufficient for the UI to show audit links.

### Graph alignment

The graph should store identifiers linking back to STAC/DCAT records (for round-trip traceability), but the UI still consumes graph-derived data only via the API boundary.

## 🧱 Architecture

### Renderer model

- **MapLibre (2D)** is the default renderer for the map UI.
- **Cesium (3D)** may be used when 3D is required (terrain/immersive views) and should share conceptual layer IDs with 2D where feasible.

### Layer registry pattern

A typical pattern is:

1. Define LayerSpec entries in a registry (JSON or TS).
2. On app load, the UI reads the registry and builds:
   - layer toggles (UI controls),
   - renderer layers/sources (MapLibre),
   - legends/attribution,
   - audit panel links.

### Adding a new layer (checklist)

1. **Layer registry**
   - Add a new LayerSpec entry (stable `id`, title, description, attribution).
2. **Data binding**
   - If API-backed: ensure a contract exists under `src/server/contracts/**` and implementation exists under `src/server/**`.
   - If static: ensure catalog references exist (STAC/DCAT/PROV) for the artifact(s).
3. **Governance fields**
   - Set sensitivity/classification.
   - If sensitive, document redaction/generalization expectations.
4. **Focus Mode integration (optional but recommended)**
   - Ensure `id` can be referenced by story nodes via `focus_layers`.
5. **Validation**
   - Ensure layer config passes UI schema validation (if present).
   - Ensure no forbidden patterns exist (e.g., any direct graph access from UI).
6. **Tests**
   - Add/extend tests for toggling, rendering, and Focus Mode application of layer hints.

> Note: The exact test tools/commands are repo-specific (**not confirmed in repo**). The intent is to keep layer behavior deterministic and reviewable.

## 🧠 Story Node & Focus Mode Integration

### Focus Mode “map hint” fields

Story Nodes can include optional Focus Mode controls such as:

- `focus_layers` (list of layer IDs)
- `focus_center` (lon/lat)
- `focus_time` (time focus / range)

The UI should treat these as **hints** that drive:

- map camera movement,
- layer activation,
- timeline focus.

### Example: focus layers and center

~~~yaml
focus_layers:
  - "treaty-boundaries"
  - "historic-basemap-1860s"
focus_time: "1867-10-21"
focus_center: [ -98.0000, 38.0000 ]
~~~

### Provenance display expectations

- In Focus Mode, narrative content must be provenance-linked (no orphan facts).
- If an “AI Insight” or summary is introduced, it must be opt-in and clearly labeled as AI-derived.

## 🧪 Validation & CI/CD

### Validation steps (recommended)

- Markdown protocol check (front-matter + required sections)
- Link/reference checks (no orphan internal pointers)
- UI schema validation for layer registry/config (if `schemas/ui/**` exists)
- Forbidden-pattern scan in `web/` for direct graph access (e.g., Neo4j driver usage)
- Contract tests for any layer that relies on API endpoints (ensure responses include needed data + provenance refs)

### CI expectations (if configured)

- CI is a pipeline-contract enforcement layer (not just “unit tests”).
- Rules should be enforceable automatically where practical (lint jobs, schema validation, contract tests).

(**Workflow names and exact commands are intentionally not enumerated unless they exist in-repo.**)

## ⚖ FAIR+CARE & Governance

### When governance review is required

Governance review is required when adding a UI layer that could reveal sensitive locations **by interaction or zoom**, or when changes expand access to restricted information.

### CARE / sovereignty considerations

- If a layer intersects with sovereignty-controlled knowledge or culturally sensitive locations:
  - prefer aggregation/generalization,
  - document the decision and redaction approach,
  - ensure UI does not “reconstruct” sensitive coordinates via styling or tooltips.

### AI usage constraints

- AI may help with summarization/structure extraction for docs, but must not be used to infer sensitive locations or invent policy.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---:|---|---|
| v1.0.0 | 2025-12-25 | Initial governed README for web map layer registry conventions | TBD |

---

## Footer refs (do not remove)

- Master guide: `docs/MASTER_GUIDE_v12.md`
- Template: `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`
- Story Node template: `docs/templates/TEMPLATE__STORY_NODE_V3.md`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
- Ethics: `docs/governance/ETHICS.md`
---

