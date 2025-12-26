---
title: "KFM web/src/ui/map — Map UI Module (README)"
path: "web/src/ui/map/README.md"
version: "v1.0.0"
last_updated: "2025-12-26"
status: "draft"
doc_kind: "README"
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

doc_uuid: "urn:kfm:doc:web:src:ui:map:readme:v1.0.0"
semantic_document_id: "kfm-web-ui-map-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:web:src:ui:map:readme:v1.0.0"
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

# web/src/ui/map — Map UI Module README

## 📘 Overview

### Purpose

- Define what the **Map UI module** owns under `web/src/ui/map/` and how it fits into the KFM pipeline.
- Document the **non‑negotiable UI constraints**:
  - the UI reads data via the **API boundary** (never directly from Neo4j),
  - the map is configured via **layer registries** (schema‑validated),
  - Focus Mode content is **provenance‑linked** (no uncited narrative claims).
- Provide contributor guidance for:
  - adding/updating map layers via the registry,
  - wiring map selection → Focus Mode,
  - synchronizing map state with timeline/time filtering (where implemented).

### Scope

| In Scope | Out of Scope |
|---|---|
| Map rendering + interaction (pan/zoom, selection, hover) | Defining/altering API contracts (belongs at the API boundary; see `src/server/` or repo equivalent) |
| Layer composition driven by a UI layer registry | ETL/catalogn build logic (belongs under `src/pipelines/` and `data/`) |
| Focus Mode integration points that the map triggers/consumes | Story Node authoring workflows (belongs in `docs/reports/story_nodes/`) |
| Displaying provenance/evidence references surfaced by API payloads | Direct graph access from the UI (explicitly disallowed) |

### Audience

- **Primary:** Frontend contributors working in `web/` (MapLibre/Map UI)
- **Secondary:** API/Graph maintainers reviewing UI adherence to contracts (redaction, provenance), and narrative curators validating Focus Mode behavior

### Definitions (link to glossary)

- Link: `docs/glossary.md` (**not confirmed in repo**)
- Terms used in this doc:
  - **API boundary**: the contracted service layer between UI and graph/catalogs
  - **Layer registry**: a declarative registry of map layers (validated against `schemas/ui/` if present)
  - **Focus Mode**: narrative UI state that must be provenance‑linked
  - **Provenance pointers**: stable identifiers that point to STAC/DCAT/PROV records or evidence bundles

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master Guide v12 | `docs/MASTER_GUIDE_v12.md` | TBD | Canonical pipeline ordering + invariants |
| v13 Redesign Blueprint | `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md` | TBD | UI design rules; layer registry + schema expectations (if adopted) |
| Story Node template (v3) | `docs/templates/TEMPLATE__STORY_NODE_V3.md` | Narrative | Provides `focus_layers`, `focus_time`, `focus_center` patterns for Focus Mode |
| Universal governed doc template | `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` | KFM Core | Structure used by this README |
| UI schemas | `schemas/ui/` | TBD | JSON Schemas for UI registries (**path expected; not confirmed in repo**) |
| API boundary code | `src/server/` | TBD | v13 target; legacy may be `src/api/` (**not confirmed in repo**) |
| UI layer registries | `web/**/layers/**` | Frontend | v13 rule: registries live under `web/` and validate against `schemas/ui/` |

### Definition of done (for this document)

- [ ] Front‑matter complete + `path` matches file location
- [ ] Map module responsibilities + boundaries are explicit (especially the API boundary)
- [ ] Layer registry assumptions and schema validation expectations are documented
- [ ] Focus Mode integration points are documented (selection → Focus Mode; Focus Mode → map)
- [ ] Validation steps listed and repeatable (or explicitly marked “not confirmed in repo”)
- [ ] Governance + CARE/sovereignty considerations explicitly stated

## 🗂️ Directory Layout

### This document

- `path`: `web/src/ui/map/README.md` (must match front‑matter)

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| UI root | `web/` | React/Map UI (MapLibre/Cesium or equivalent) |
| Map module | `web/src/ui/map/` | Map rendering, layer orchestration, map↔Focus integration |
| Layer registries | `web/**/layers/**` | Declarative layer configuration (v13 expectation) |
| UI schemas | `schemas/ui/` | JSON Schema validation for registries (expected; not confirmed) |
| API boundary | `src/server/` | UI access to graph/catalog via contracted endpoints |
| Story Nodes | `docs/reports/story_nodes/` | Narrative artifacts that drive Focus Mode (expected; not confirmed) |
| Governance | `docs/governance/` | Sovereignty + ethics constraints for exposure of sensitive locations |

### Expected file tree for this sub‑area

> This is a **recommended** structure. Some directories may not exist yet (**not confirmed in repo**).

~~~text
📁 web/
└── 📁 src/
    └── 📁 ui/
        └── 📁 map/
            ├── 📄 README.md
            ├── 📁 components/                 # map shell, legend, controls (recommended)
            │   ├── 📄 MapView.<ext>           # creates/owns map instance (not confirmed in repo)
            │   ├── 📄 MapLegend.<ext>         # layer toggles + legend UI (not confirmed in repo)
            │   ├── 📄 MapControls.<ext>       # zoom/home/time controls (not confirmed in repo)
            │   └── 📄 FeaturePopup.<ext>      # hover/click popup with provenance (not confirmed in repo)
            ├── 📁 layers/                     # layer registry adapter + layer builders (recommended)
            │   ├── 📄 registryLoader.<ext>    # load/validate registry (not confirmed in repo)
            │   ├── 📄 layerFactory.<ext>      # create map layers from registry entries (not confirmed)
            │   └── 📄 styleTokens.<ext>       # shared paint/layout tokens (optional)
            ├── 📁 hooks/                      # map hooks (recommended)
            │   ├── 📄 useMap.<ext>            # map lifecycle + events (not confirmed in repo)
            │   └── 📄 useLayerRegistry.<ext>  # load/refresh registry (not confirmed in repo)
            ├── 📁 state/                      # map state interface/store (recommended)
            │   └── 📄 mapState.<ext>          # view state + selected feature (not confirmed in repo)
            ├── 📁 adapters/                   # engine abstraction (optional)
            │   ├── 📄 maplibreAdapter.<ext>   # MapLibre implementation (not confirmed in repo)
            │   └── 📄 cesiumAdapter.<ext>     # 3D extension (optional; not confirmed)
            └── 📁 __tests__/                  # unit/integration tests (recommended)
                └── 📄 focusModeSync.test.<ext>
~~~

## 🧭 Context

### Background

KFM’s canonical pipeline ordering is:

**ETL → STAC/DCAT/PROV catalogs → Neo4j graph → APIs → React/Map UI → Story Nodes → Focus Mode**

The map UI is the primary spatial “index” for:
- exploring layers and entities,
- selecting features to open narrative context (Focus Mode),
- and presenting evidence pointers (catalog + provenance identifiers) alongside spatial interactions.

### Constraints / invariants (non‑negotiable)

- **API boundary**: the UI reads only from **contracted APIs** and published catalog endpoints; it must **not** read Neo4j directly.
- **Registry‑driven layers**: map layers are configured declaratively (layer registry), and registries should validate against `schemas/ui/` when present.
- **Provenance‑linked Focus Mode**: Focus Mode narratives and map tooltips/panels should show provenance pointers surfaced by the API (e.g., dataset/item/activity IDs).
- **Sensitive location handling**: restricted or culturally sensitive geometries must be protected via generalization/redaction at the API boundary; the UI must respect sensitivity flags and avoid re‑exposure.

### Assumptions

- Map rendering uses **MapLibre** as the 2D engine (and may optionally support Cesium for 3D) — align this module to be engine‑adaptable if the repo supports both.
- A layer registry pattern exists or is planned under `web/**/layers/**` (v13 expectation). If it does not exist yet, treat this README’s registry guidance as a scaffold.

### Open questions (track and resolve in issues)

| Question | Why it matters | Status |
|---|---|---|
| What is the canonical registry schema path/name under `schemas/ui/`? | Enables CI validation + stable registry contracts | Not confirmed in repo |
| Where is the API client / typed contract for map payloads? | Prevents “stringly‑typed” drift | Not confirmed in repo |
| Does the UI support time filtering today (timeline)? | Impacts how map layers accept time windows | Not confirmed in repo |

## 🗺️ Diagrams

### Map module in the pipeline

~~~mermaid
flowchart LR
  ETL[ETL] --> CATS[STAC/DCAT/PROV]
  CATS --> G[Neo4j Graph]
  G --> API[API Boundary]
  CATS --> API
  API --> UI[web/ UI]
  UI --> SN[Story Nodes]
  SN --> FM[Focus Mode]

  subgraph UI
    MAP[Map module<br/>web/src/ui/map]
    FMUI[Focus Mode UI]
    TL[Timeline (optional)]
  end

  API --> MAP
  API --> FMUI
  MAP <--> TL
  MAP --> FMUI
~~~

### Selection → Focus Mode (conceptual)

~~~mermaid
sequenceDiagram
  participant User
  participant Map as Map UI (MapLibre)
  participant API as API Boundary
  participant Focus as Focus Mode UI

  User->>Map: Click feature
  Map->>API: Request context bundle (by entity/event id)
  API-->>Map: Evidence pointers + display geometry (redacted if needed)
  API-->>Focus: Narrative/context payload (provenance-linked)
  Map->>Focus: Open Focus Mode (with entity/event id)
~~~

## 📦 Data & Metadata

### Inputs (what the map consumes)

| Input | Source | Notes |
|---|---|---|
| Layer registry | `web/**/layers/**` | Declarative set of layers; validate vs `schemas/ui/` if present |
| Map layer payloads (tiles/GeoJSON/features) | API boundary + catalog endpoints | Must honor redaction/generalization rules |
| Focus context bundles | API boundary | Used to highlight/zoom and to render provenance pointers |
| Optional timeline/time window | UI state / Focus Mode hints | Not confirmed in repo |

### Outputs (what the map produces)

| Output | Consumer | Notes |
|---|---|---|
| Map view state (center/zoom/bearing) | UI store / app shell | Use for “return to focus” and permalink behaviors (if implemented) |
| Selection events | Focus Mode / side panels | Selection should emit stable ids, not raw sensitive geometry |
| Layer on/off state | Legend / app state | Persist if app supports it (not confirmed in repo) |
| Telemetry events | Telemetry sink | Not confirmed in repo |

## 🌐 STAC, DCAT & PROV Alignment

The map module does not generate STAC/DCAT/PROV artifacts, but it **must surface** provenance pointers provided by the API/catalog layer.

Recommended practices (align to repo governance):

- Map popups/inspect panels should show **evidence pointers** (dataset/item/prov activity ids) rather than embedding unverifiable narrative.
- When a feature is derived from a catalog record, provide a **“Sources”** affordance that links to:
  - STAC Item / Collection id (if delivered by API),
  - DCAT dataset id (if delivered by API),
  - PROV Activity id(s) (if delivered by API).
- If the API marks an asset as sensitive/restricted, the UI must avoid exposing higher‑precision geometry than allowed.

## 🧱 Architecture

### Responsibilities (what belongs in `web/src/ui/map/`)

- Own the map engine instance lifecycle (mount/unmount, resize handling).
- Translate registry entries into engine layers (with a validation step).
- Normalize map events into app‑level events:
  - hover/click selection,
  - bounding box changes,
  - zoom/extent changes.
- Provide an integration seam for Focus Mode:
  - accept focus hints (center/time/layers),
  - apply highlight styles and viewport changes,
  - emit selection events to open Focus Mode.

### Module boundaries (anti‑patterns)

- ❌ Do not query Neo4j directly (no direct graph reads from the browser).
- ❌ Do not hardcode sensitive coordinates to “work around” redaction or access control.
- ❌ Do not ship unvalidated registries (treat registry JSON as a contract).

### Suggested interfaces (conceptual; not confirmed in repo)

If the codebase benefits from a stable contract between the map module and the rest of the UI, define a small “controller” interface (names TBD) such as:

- `setView({ center, zoom, bearing })`
- `setActiveLayers(layerIds[])`
- `highlightFeatures(featureRefs[])`
- `setTimeWindow({ start, end })` (optional)
- `onSelection(cb)` / `emitSelection(featureRef)`

## 🧠 Story Node & Focus Mode Integration

### Focus hints from Story Nodes

Story Nodes may optionally include structured focus hints such as:

~~~yaml
focus_layers:
  - "TBD-layer-id"
focus_time: "TBD-iso8601"
focus_center: [ -98.0000, 38.0000 ]
~~~

Intended UI behavior:

- **focus_layers**: activate/feature-highlight layers relevant to the story.
- **focus_time**: set the timeline/time filter (if supported) and request time‑appropriate data from the API.
- **focus_center**: pan/zoom the map to the focal location (respecting any redaction/generalization constraints).

### Provenance-linked narrative rule (UI enforcement)

- Focus Mode content should only display narrative claims that include **evidence pointers** delivered by the API boundary.
- For map popups/side panels:
  - show “what this is” (label/title),
  - show “where it comes from” (provenance pointers),
  - and provide navigation to Focus Mode for the full narrative.

> If citations/provenance ids are missing from a payload, treat that as a contract violation (debug in API boundary or catalog), not something the UI should “invent”.

## 🧪 Validation & CI/CD

### Validation steps

- [ ] Markdown protocol checks (KFM‑MDP)
- [ ] UI registry schema validation (validate `web/**/layers/**` against `schemas/ui/` if present)
- [ ] Unit tests for map events (selection, focus sync)
- [ ] Integration tests for “selection → Focus Mode” flow (recommended)
- [ ] Accessibility checks for map controls and legend UI
- [ ] Security/sovereignty checks for any new layer exposure (sensitive geometry)

### Reproduction

~~~bash
# Example placeholders — replace with repo-specific commands (NOT confirmed in repo)

# cd web
# <install-deps>
# <run-lint>
# <run-tests>
# <run-ui-schema-checks>
~~~

### Telemetry signals (if applicable)

| Signal | Source | Where recorded |
|---|---|---|
| UI registry validation result | CI | CI logs + artifacts |
| Layer load failures | Web app | telemetry sink (not confirmed in repo) |
| Focus Mode open events | Web app | telemetry sink (not confirmed in repo) |

## ⚖ FAIR+CARE & Governance

### Review gates

- Changes that add or modify a **public map layer** should trigger review for:
  - schema validity,
  - provenance completeness,
  - sensitivity classification alignment.
- Any change affecting **sensitive/restricted geometries** requires governance review (approver routing not confirmed in repo; defer to `docs/governance/*`).

### CARE / sovereignty considerations

- Treat culturally sensitive layers and restricted locations as **high‑risk by default**.
- Do not increase re‑identification risk via:
  - over‑precise geometry,
  - “nearby” inference,
  - combining datasets in UI in ways that reconstruct restricted sites.
- Ensure UI behavior aligns with redaction/generalization rules implemented at the API boundary.

### AI usage constraints

- This document permits structural extraction, summarization, translation, and keyword indexing.
- Prohibited: generating new policy text or inferring sensitive locations.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-26 | Initial `web/src/ui/map/README.md` scaffold aligned to Master Guide v12 + v13 UI rules | TBD |

---

Footer refs:

- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
- Master Guide: `docs/MASTER_GUIDE_v12.md`
- v13 Blueprint: `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md`
- Story Node template: `docs/templates/TEMPLATE__STORY_NODE_V3.md`
---

