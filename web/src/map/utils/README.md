---
title: "KFM Web — Map Utils (README)"
path: "web/src/map/utils/README.md"
version: "v0.1.0-draft"
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

doc_uuid: "urn:kfm:doc:web:map-utils:readme:v0.1.0-draft"
semantic_document_id: "kfm-web-map-utils-readme-v0.1.0-draft"
event_source_id: "ledger:kfm:doc:web:map-utils:readme:v0.1.0-draft"
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

# 🧰🗺️ KFM Web Map Utils

Shared utility functions for the map subsystem (MapLibre/Cesium-facing helpers, geometry helpers, layer-registry helpers, and Focus Mode map-control helpers).

This folder is intentionally **dependency-light** and **test-friendly**.

## 📘 Overview

### Purpose

- Provide **deterministic**, reusable helpers for map rendering and interaction.
- Reduce duplication across map components (layers, sources, time controls, selection, Focus Mode behaviors).
- Enforce KFM UI invariants at a single “choke point” (e.g., safe handling of redacted/sensitive map data).

### Scope

| In Scope | Out of Scope |
|---|---|
| Pure functions (geometry, bbox, coordinate transforms, style helpers) | React components / hooks (place under `web/src/**/components` or `web/src/**/hooks`) |
| Converting validated configs into MapLibre/Cesium-ready config fragments | Network calls (fetch/axios), Neo4j queries, direct DB access |
| Parsing/validating Focus Mode map-control hints (when provided by Story Nodes or API payloads) | Business logic for narrative content (belongs in story rendering / Focus Mode UI) |
| Helpers to interpret a **layer registry** config (if present) | Writing/authoring layer registry data or schemas (belongs under `web/**` config + `schemas/**`) |

### Audience

- Primary: Frontend engineers working in `web/` (map + Focus Mode UX).
- Secondary: API engineers who need to understand what the UI expects from contracts and payload shape.

### Definitions

- **Viewport / ViewState:** Map camera state (center, zoom, bearing, pitch).
- **BBox:** Bounding box `[minLon, minLat, maxLon, maxLat]`.
- **Layer registry:** A JSON configuration describing what layers exist, their sources, attribution, and sensitivity flags (example paths exist in design docs; confirm actual repo path).
- **Focus Mode controls:** Optional structured hints such as `focus_layers`, `focus_time`, `focus_center` that can be embedded in Story Nodes or returned by APIs.

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master Guide v12 (draft) | `docs/MASTER_GUIDE_v12.md` | KFM Core Team | Canonical pipeline + invariants |
| v13 Redesign Blueprint (draft) | `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md` | Architecture Team | “No UI direct-to-graph reads”; canonical roots |
| Story Node Template v3 | `docs/templates/TEMPLATE__STORY_NODE_V3.md` | Narrative Curators | Defines optional `focus_layers`, `focus_time`, `focus_center` controls |
| Layer registry concept (example) | `web/cesium/layers/*.json` | Frontend | Example location referenced in design docs (**not confirmed in repo**) |
| API boundary | `src/server/` | API Team | UI must access graph via contracted APIs |

### Definition of done (for this document)

- [ ] Front-matter complete + valid (path matches this file)
- [ ] Clear **“in scope / out of scope”** boundaries for map utils
- [ ] Explicitly documents the **no direct-to-graph** constraint for UI code
- [ ] Lists expected inputs/outputs + sensitivity handling
- [ ] Validation steps are actionable (even if commands are repo-specific placeholders)
- [ ] Footer references point to the canonical docs/templates

## 🗂️ Directory Layout

### This document

- `path`: `web/src/map/utils/README.md` (must match front-matter)

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| Frontend | `web/` | React UI, MapLibre/Cesium integration, Focus Mode UX |
| APIs | `src/server/` | Contracted access layer (REST/GraphQL); UI must not bypass |
| Schemas | `schemas/` | Machine-validated schemas (including UI config schemas if present) |
| Docs | `docs/` | Canonical governed documentation and templates |
| Story Nodes | `docs/reports/story_nodes/` | Draft/published narratives for Focus Mode (if adopted) |
| Layer registry (example) | `web/cesium/layers/` | JSON registry for map layers (**not confirmed in repo**) |

### Expected file tree for this sub-area

~~~text
web/src/map/utils/
├── 📄 README.md                     # This file (governance + conventions for map utils)
├── 🧩 *.ts / *.js                   # Pure helpers (geometry, style, registry parsing, focus controls)
└── 🧪 *.test.ts / *.spec.ts         # Unit tests (if a JS/TS test runner is configured)
~~~

## 🧭 Context

### How this fits the canonical pipeline

KFM’s canonical flow is:

**ETL → STAC/DCAT/PROV → Graph (Neo4j) → APIs → UI (React/Map) → Story Nodes → Focus Mode**

This directory is strictly within the **UI** stage. It may interpret API payloads and Story Node controls, but must not pull data directly from storage layers.

### Constraints and invariants (UI)

- **No UI direct-to-graph reads:** `web/` must never query Neo4j directly; all graph access is via contracted APIs under `src/server/`.
- **Contracts are canonical:** UI configuration (e.g., layer registry) should be schema-validated when schemas exist.
- **No “inference” of sensitive locations:** if payloads are redacted/generalized upstream, map utils must preserve that and handle reduced precision gracefully.

### What belongs in `map/utils`

Use this directory for:

- Geometry helpers:
  - bbox creation/union/intersection
  - safe coordinate normalization (lon/lat order)
  - GeoJSON feature collection helpers (no mutation)
- Map config helpers:
  - create/update MapLibre sources/layers from **validated** config objects
  - map style expression builders (small, composable, unit tested)
- Layer registry helpers:
  - validate/normalize registry entries (client-side “defensive parse”)
  - filter layers by user permissions / sensitivity flags (policy is upstream, but UI can hide/toggle)
- Focus Mode helpers:
  - parse and validate optional Story Node controls
  - turn controls into map actions (camera moves, layer toggles, time range selection)

### What does NOT belong in `map/utils`

Avoid placing these here:

- `fetch()` / axios / websocket clients (belongs in `web/src/**/api` or `web/src/**/clients`)
- Global state stores (Redux/Context) — pass dependencies in explicitly
- React hooks/components
- Any code that assumes Neo4j/Cypher access (UI boundary violation)

## 🗺️ Diagrams

~~~mermaid
flowchart LR
  subgraph UI["UI (web/)"]
    M[Map components] --> U[map/utils/*]
    U --> R[Map engine adapters<br/>(MapLibre/Cesium)]
  end

  API["API (src/server/)"] -->|contracted payloads| UI

  Note1["Invariant: UI never talks to Neo4j directly"] --- API
~~~

## 📦 Data & Metadata

### Inputs

| Input | Format | Where from | Validation |
|---|---|---|---|
| Map engine events | JS objects | MapLibre/Cesium runtime | Unit tests for handlers (pure where possible) |
| Layer registry entries | JSON | `web/**` config (example path; confirm repo) | Prefer schema validation + defensive parse |
| Feature payloads | GeoJSON / vector tile refs | API responses | Validate shape; handle missing/optional fields safely |
| Focus Mode controls | YAML/JSON fields | Story Node content or Focus API response | Validate types + ranges; safe defaults |

### Outputs

| Output | Format | Used by | Contract / Schema |
|---|---|---|---|
| ViewState updates | JS object | Map components/state | Internal UI contract |
| MapLibre layer/source fragments | JS object | Map engine adapter | MapLibre API types (TS) if available |
| Derived bbox/centroid | arrays/numbers | Camera fit logic | Internal helper contract |
| Layer toggle sets | string arrays/sets | Focus Mode / layer UI | Registry-driven |

### Sensitivity & redaction

- Treat **all upstream data as untrusted** input:
  - never `eval()` style expressions
  - never interpolate untrusted strings into HTML
- If a layer/feature is marked **sensitive** (or data is generalized):
  - do not attempt to “reconstruct” precision
  - prefer showing generalized geometry or omitting the layer (depends on UI policy and permissions)
- If coordinates are missing or intentionally degraded:
  - fail gracefully (no crashes), and prefer “no-op” camera behavior.

## 🌐 STAC, DCAT & PROV Alignment

Although this is UI code, it must respect that KFM’s evidence products and datasets are provenance-backed.

Typical UI touchpoints:

- Displaying **attribution/license** strings for raster/vector sources derived from STAC/DCAT metadata (when provided by APIs or registry config).
- Preserving and surfacing **provenance links** (IDs, not full documents) alongside map selections in Focus Mode.

## 🧱 Architecture

### Components (UI slice)

| Component | Responsibility | Interface |
|---|---|---|
| Map components | Render and interact with the map | Calls into `map/utils/*` |
| `map/utils/*` | Deterministic helpers; parsing/validation; geometry; config building | Pure functions + typed inputs |
| Map engine adapter | MapLibre/Cesium-specific integration | Uses official engine APIs |
| API clients | Fetch contracted payloads | Talks only to `src/server/` endpoints (never DB) |
| Focus Mode UI | Applies story/context to map + timeline | Uses Focus controls + API responses |

### Interfaces / contracts (relevant)

| Contract | Location | Versioning rule |
|---|---|---|
| API schemas | `src/server/` + docs | Contract tests required |
| UI schemas (if present) | `schemas/` | Semver + validation in CI |
| Layer registry (example) | `web/**` JSON config | Schema-validated (when schema exists) |

## 🧠 Story Node & Focus Mode Integration

Story Nodes may optionally include structured controls that help the UI focus the map:

~~~yaml
focus_layers:
  - "TBD"
focus_time: "TBD"
focus_center: [ -98.0000, 38.0000 ]
~~~

`map/utils` should provide helpers that:

- Parse these fields defensively (type checks, range checks).
- Apply safe defaults (e.g., ignore invalid values rather than crashing).
- Return **declarative actions** (e.g., `{type: "SET_CENTER", center, zoom?}`) instead of mutating global state.

## 🧪 Validation & CI/CD

### Validation steps (recommended)

- [ ] Typecheck (if TS is used)
- [ ] Unit tests for pure helpers (geometry, parsers, builders)
- [ ] Lint rules that discourage side effects in utils (where configured)
- [ ] If layer registry is used: schema validation gate (when schema exists)
- [ ] Security scanning: ensure no secrets, tokens, or internal endpoints are committed

### Reproduction

~~~bash
# Example placeholders — replace with repo-specific commands (not confirmed in repo)
# 1) install dependencies
# 2) run unit tests
# 3) run lint + typecheck
~~~

## ⚖ FAIR+CARE & Governance

### Review gates

- Changes that affect how **sensitive/generalized** map data is handled should be reviewed with governance context.
- Changes that introduce or modify **layer registry** fields should be paired with schema updates (if schema exists) and documented.

### CARE / sovereignty considerations

- If a map layer or feature set relates to culturally sensitive knowledge or restricted locations:
  - do not increase spatial precision in UI transformations
  - prefer omission/generalization patterns aligned with upstream policy

### AI usage constraints

- Permitted transformations: summarization, structure extraction, translation, keyword indexing.
- Prohibited: generating new policy text; inferring sensitive locations.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v0.1.0-draft | 2025-12-25 | Initial `web/src/map/utils` README (conventions + boundaries) | TBD |

---

### Footer refs

- Master Guide: `docs/MASTER_GUIDE_v12.md`
- v13 Blueprint (if adopted): `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md`
- Universal template: `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`
- Story Node template: `docs/templates/TEMPLATE__STORY_NODE_V3.md`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty policy: `docs/governance/SOVEREIGNTY.md`

