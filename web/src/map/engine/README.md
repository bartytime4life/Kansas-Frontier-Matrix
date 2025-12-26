---
title: "KFM Map Engine — README"
path: "web/src/map/engine/README.md"
version: "v1.0.0"
last_updated: "2025-12-25"
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

doc_uuid: "urn:kfm:doc:web:map-engine:readme:v1.0.0"
semantic_document_id: "kfm-web-map-engine-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:web:map-engine:readme:v1.0.0"
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

# 🗺️ KFM Map Engine (web UI)

## 📘 Overview

### Purpose

This directory defines the **map runtime “engine”** used by the KFM web application to render:
- 2D map views (MapLibre GL JS),
- optional 3D views (e.g., Cesium),
- layer toggles and time-aware visualization,
- selection, hover, and context panels (including Focus Mode overlays),
while enforcing KFM’s UI invariants: **no direct graph reads** and **provenance-visible UI**.

### Scope

| In Scope | Out of Scope |
|---|---|
| Map engine interfaces, adapters (2D/3D), layer lifecycle, map state, selection/interaction events | ETL, catalog generation, graph ingest, or database queries |
| Consuming layer definitions (registry) and rendering them deterministically | Authoring STAC/DCAT/PROV (belongs in pipeline/catalog stages) |
| UI-side safeguards for sensitive layers (zoom caps, aggregation, hide-on-policy) | Redaction rules (enforced at API boundary), governance policy authoring |

### Audience

- Primary: Frontend engineers working on the KFM map + timeline UI.
- Secondary: API/graph engineers verifying UI/API boundaries; governance reviewers validating “what the UI can reveal.”

### Definitions (link to glossary)

- Link: `docs/glossary.md` *(not confirmed in repo — add/repair link if glossary lives elsewhere)*  
- Terms used in this doc:
  - **Layer registry**: a declarative set of layer definitions (IDs, sources, attribution, time bounds, sensitivity flags).
  - **Evidence artifact**: catalog/provenance-backed outputs (STAC/DCAT/PROV) consumed downstream.
  - **Focus Mode**: UI view that renders story/context **only when provenance is complete**.
  - **Provenance link**: an explicit pointer to the underlying evidence (STAC item, DCAT dataset, PROV activity).

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master pipeline ordering + invariants | `docs/MASTER_GUIDE_v12.md` | KFM Core | Canonical pipeline: ETL → Catalogs → Graph → API → UI → Story → Focus Mode |
| UI/Repo invariants | `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md` | Arch | “UI reads only from APIs”; layer registries validated via `schemas/ui/` |
| API boundary contracts | `src/server/contracts/` | API | UI must only consume contracted endpoints (REST/GraphQL) |
| UI schemas (layer registry, UI config) | `schemas/ui/` | Contracts | Exact filenames not confirmed in repo |
| Focus Mode + Story Nodes | `docs/reports/story_nodes/` | Narrative | UI renders story content from validated Story Nodes (provenance-linked) |

### Definition of done (for this document)

- [ ] Front-matter complete + `path` matches location
- [ ] Directory responsibilities + invariants are explicit (no graph reads; provenance display)
- [ ] Layer-registry contract location and validation expectations are documented
- [ ] Validation steps are listed and repeatable *(commands may be “not confirmed in repo”)*
- [ ] Governance + CARE/sovereignty considerations explicitly stated for UI layer additions

---

## 🗂️ Directory Layout

### This document

- `path`: `web/src/map/engine/README.md` (must match front-matter)

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| UI | `web/` | React application (map + narrative UI) |
| API boundary | `src/server/` | Contracted access layer, redaction/generalization enforcement |
| Contracts | `src/server/contracts/` | OpenAPI/GraphQL and endpoint contracts |
| Schemas | `schemas/` | JSON Schemas (STAC/DCAT/PROV/story/ui/telemetry) |
| Story Nodes | `docs/reports/story_nodes/` | Narrative artifacts rendered in Focus Mode |
| Catalog evidence | `data/stac/` + `data/catalog/dcat/` + `data/prov/` | Evidence artifacts referenced by UI |

### Expected file tree for this sub-area

> This is the recommended structure. Some items may not exist yet (**not confirmed in repo**).

~~~text
web/
└── src/
    └── map/
        └── engine/
            ├── 📄 README.md                  # This document
            ├── 🧠 MapEngine.ts               # Engine facade (recommended; not confirmed in repo)
            ├── 🧩 adapters/                  # Map runtime adapters (recommended)
            │   ├── 🗺️ maplibre/              # 2D MapLibre adapter (recommended)
            │   └── 🌍 cesium/                # Optional 3D adapter (recommended)
            ├── 🧱 layers/                    # Layer lifecycle + registry bindings (recommended)
            ├── ⏱️ time/                      # Time/timeline utilities (recommended)
            ├── 🧭 interaction/               # Click/hover/select handlers (recommended)
            └── 🧪 __tests__/                 # Unit/integration tests for engine behaviors (recommended)
~~~

---

## 🧭 Context

### Background

KFM’s UI is a **map + narrative** exploration surface. The map engine exists so the React UI can:
- render many heterogeneous layers (vector/raster/tiles),
- coordinate map interactions with timeline and story panels,
- support (optional) 3D views without coupling UI components to a specific renderer,
- expose provenance and layer attribution consistently.

### Assumptions

- The UI is a React SPA under `web/`.
- The map runtime uses MapLibre GL JS for 2D, and may support a 3D renderer (e.g., Cesium) behind an adapter boundary.
- Layer configuration is declarative (registry), and registry validation is enforced by schemas under `schemas/ui/` (exact schema filenames not confirmed in repo).
- All entity/context data required for popups and Focus Mode is fetched through the API boundary (`src/server/`).

### Constraints / invariants

- **Canonical pipeline is preserved:** ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode.
- **No UI direct-to-graph reads:** the engine must not call Neo4j (directly or indirectly) — only API endpoints.
- **Provenance-first UI:** Focus Mode and any “story” surfaces must not display orphan facts; provenance links must be available to the user.
- **Layer registries are contract artifacts:** validate against `schemas/ui/` in CI (if configured).

### Open questions

| Question | Owner | Target date |
|---|---|---|
| Do we standardize on one state container for map state (Redux vs Context/Reducers)? | UI | TBD |
| Do we support 3D in v1, or gate it behind feature flags? | UI | TBD |
| What is the minimal layer registry schema set required for “CI green”? | Contracts | TBD |
| How do we encode “time extent” for layers (range vs discrete snapshots)? | UI + Data | TBD |

### Future extensions

- Vector tile / PMTiles support as first-class layer types.
- Offline-capable caching (service worker) with explicit governance controls.
- “Evidence hover” mode: show STAC/DCAT/PROV references directly from the map for any feature.

---

## 🗺️ Diagrams

### System / dataflow diagram

~~~mermaid
flowchart LR
  U[User actions<br/>(pan/zoom/click/time)] --> R[React UI]
  R --> E[Map Engine (this directory)]
  E --> L[Layer Registry<br/>(declarative config)]
  E --> A[API boundary<br/>src/server]
  A --> G[Graph services<br/>(Neo4j behind API)]
  A --> C[Catalog services<br/>(STAC/DCAT/PROV)]
  E --> V[Viewport renderers<br/>(MapLibre / optional 3D)]
  E --> P[Panels<br/>(popups + Focus Mode)]
~~~

### Optional: sequence diagram (feature selection → provenance-backed context)

~~~mermaid
sequenceDiagram
  participant UI as React UI
  participant Engine as Map Engine
  participant API as API boundary (src/server)
  participant Graph as Graph services
  participant Cat as Catalog services (STAC/DCAT/PROV)

  UI->>Engine: onFeatureSelect(feature_id, layer_id)
  Engine->>API: GET /context?feature_id=...&layer_id=...
  API->>Graph: fetch subgraph + entity IDs
  API->>Cat: fetch evidence refs (STAC/DCAT/PROV)
  API-->>Engine: context bundle (facts + provenance refs + redaction flags)
  Engine-->>UI: render popup/panel with provenance links
~~~

---

## 📦 Data & Metadata

### Inputs

| Input | Format | Where from | Validation |
|---|---|---|---|
| Layer registry | JSON/YAML (TBD) | `web/**` (registry location not confirmed) | Validate against `schemas/ui/` |
| Map style/theme | JSON | UI assets | JSON validation + lint |
| Evidence-backed context | JSON | `src/server` endpoints | Contract tests + runtime guards |
| Feature geometries | vector tiles/GeoJSON | API/catalog distribution | Bounds + geometry validity (UI-side sanity checks) |

### Outputs

| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Rendered layers | GPU draw calls | runtime | N/A |
| UI map state (camera, selected feature, active layers) | JS state | runtime | Type checks (TS) |
| Provenance display objects | JSON | runtime | UI contract types (recommended) |
| Telemetry events (optional) | JSON | runtime | `schemas/telemetry/**` *(not confirmed in repo)* |

### Sensitivity & redaction

- Treat any layer flagged “sensitive” as **interaction-risk**:
  - cap max zoom,
  - enforce clustering/aggregation,
  - avoid showing exact coordinates if policy requires generalization,
  - ensure the UI labels restricted content clearly.
- Assume the API boundary enforces core redaction/generalization; the map engine must still honor response flags (e.g., “masked geometry”).

### Quality signals

- Layer load success rate (per layer_id)
- Tile error rate / retry counts
- Time-to-first-render for basemap + first overlay
- Accessibility checks: keyboard reachability for map controls; readable contrast for labels *(implementation not specified here)*

---

## 🌐 STAC, DCAT & PROV Alignment

### STAC

- The map engine should be able to reference STAC identifiers for:
  - layer sources (COGs, vector tiles, GeoJSON),
  - attribution,
  - spatiotemporal extents.
- Prefer to keep STAC parsing/selection in the API boundary; UI consumes a UI-friendly “layer model” derived from STAC.

### DCAT

- If UI exposes dataset “About” panels, prefer DCAT dataset metadata as the canonical summary.
- UI should display license/attribution exactly as provided.

### PROV-O

- Focus Mode and detail panels must provide provenance links (PROV activity/entity references) whenever available.
- UI must not synthesize “facts” that are not tied to evidence references.

### Versioning

- When a layer changes meaningfully (source, extent, schema), treat it as a versioned entity:
  - keep stable layer IDs where possible, and add explicit `version` and `derived_from` references in metadata (exact mechanism depends on registry schema).

---

## 🧱 Architecture

### Components

| Component | Responsibility | Interface |
|---|---|---|
| Engine facade | Provide a single API for map init, layer mount/unmount, events | TypeScript interface (recommended) |
| MapLibre adapter | Own MapLibre instance lifecycle, sources/layers, camera | Adapter API |
| 3D adapter (optional) | Own 3D viewer lifecycle and layer projection | Adapter API |
| Layer manager | Translate registry definitions into renderer-specific layers | `LayerDefinition` model |
| Interaction manager | Click/hover/select; feature query; hit-testing | Events + callbacks |
| Time manager | Time slider bindings; layer time filters | `time_state` model |
| Provenance UI helpers | Render provenance badges/links consistently | UI components/utilities |

### Interfaces / contracts

| Contract | Location | Versioning rule |
|---|---|---|
| Layer registry schema | `schemas/ui/` | Semver + schema validation (filenames not confirmed) |
| API contracts | `src/server/contracts/` | Semver + contract tests |
| Story Node schema | `schemas/` + `docs/templates/` | Semver + validation gates (location depends on repo) |

---

## ⚙️ Validation & CI/CD

### Validation steps (recommended)

> Commands are illustrative; exact scripts/targets are **not confirmed in repo**.

- Type check + lint: `pnpm lint` / `pnpm typecheck`
- Unit tests: `pnpm test`
- Accessibility checks (if configured): `pnpm test:a11y`
- Schema validation (layer registry): run schema-lint against `schemas/ui/**`
- Link/reference checks for this README (front-matter path, referenced docs)

### CI expectations (if configured)

- Markdown protocol validation (front-matter present, required headings)
- Schema validation (UI registry schemas)
- API contract tests (for endpoints consumed by map engine)
- Security + sovereignty scanning gates (sensitive layer additions)

---

## ⚖ FAIR+CARE & Governance

- Adding a new UI layer can change what the public can infer via interaction/zoom.
  - If a layer intersects sensitive locations or restricted knowledge, require governance review and prefer coarser public products.
- The engine must surface:
  - license + attribution,
  - provenance links,
  - “masked/generalized” flags,
  wherever provided by the API/cat layer.

---

## 🧾 Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-25 | Initial README for `web/src/map/engine` (purpose, invariants, contracts, validation) | (you) |

---

## Footer refs (do not remove)

- Master Guide: `docs/MASTER_GUIDE_v12.md`
- v13 Blueprint (if adopted): `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md`
- Universal template: `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty policy: `docs/governance/SOVEREIGNTY.md`
---

