---
title: "KFM Web Map Components — README"
path: "web/src/map/components/README.md"
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

doc_uuid: "urn:kfm:doc:web:map:components:readme:v1.0.0"
semantic_document_id: "kfm-web-map-components-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:web:map:components:readme:v1.0.0"
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

# KFM Web Map Components — README

> **Purpose (required):** Define the responsibilities, constraints, and integration expectations for **map-related React components** living under `web/src/map/components/`, including **Focus Mode** behavior and **provenance-first rendering**.

## 📘 Overview

### Purpose

- Provide a single, governed place to document:
  - what belongs in `web/src/map/components/`,
  - the **UI/API boundary** rules (no direct graph access),
  - how map components participate in **Focus Mode** and **Story Node** rendering,
  - how we keep map interactions **evidence-led** (citations, provenance, sensitivity controls).

### Scope

| In Scope | Out of Scope |
|---|---|
| Map UI components (MapLibre/Cesium views, controls, overlays, legends, tooltips, layer toggles) | Implementing Neo4j access, Cypher queries, or graph migrations |
| Focus Mode map/timeline sync behaviors | Defining/altering API contracts (use API Contract Extension template) |
| Rendering provenance/citations surfaced from the API | ETL/catalog/graph build logic |
| Consuming the layer registry config and reflecting validation expectations | Styling standards for the entire web app (document elsewhere) |

### Audience

- **Primary:** UI engineers working in `web/` building map + narrative experiences.
- **Secondary:** API/graph engineers and governance reviewers validating boundary compliance, provenance visibility, and sensitivity handling.

### Definitions

- Link: `docs/glossary.md` (**not confirmed in repo**)
- Terms used in this doc include: **MapLibre**, **Cesium**, **Focus Mode**, **Story Node**, **layer registry**, **context bundle**, **provenance**, **redaction/generalization**.

### Key artifacts

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master pipeline ordering + invariants | `docs/MASTER_GUIDE_v12.md` | KFM Core | Canonical pipeline (ETL → catalogs → graph → API → UI → story nodes → focus mode) |
| v13 redesign blueprint | `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md` | Architecture | Reinforces UI/API boundary + schema validation expectations |
| Implementation guide (UI section) | `docs/architecture/KFM_IMPLEMENTATION_GUIDE.md` (**not confirmed in repo**) | Dev Team | Frontend patterns: state sync, MapLibre integration, layer registry, Focus Mode |
| Story Node template | `docs/templates/TEMPLATE__STORY_NODE_V3.md` | Narrative | Includes optional Focus Mode control metadata (e.g., `focus_center`, `focus_time`, `focus_layers`) |
| Universal doc template | `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` | Governance | Structure and required footer refs |

### Definition of done

- [x] Front-matter complete + valid, and `path:` matches file location
- [x] Directory responsibilities + boundary rules documented
- [x] Focus Mode + Story Node integration expectations documented
- [ ] Directory tree reviewed against actual code (update if this README drifts)
- [ ] Validation steps listed and repeatable
- [ ] Maintainer review

---

## 🗂️ Directory Layout

### This document

- `path`: `web/src/map/components/README.md` (must match front-matter)

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| UI root | `web/` | React app + map clients + layer registry config |
| Map feature area | `web/src/map/` (**not confirmed in repo**) | Map-specific state, services, and routes |
| API boundary | `src/server/` | API implementations + redaction, contract enforcement |
| API contracts | `src/server/contracts/` | OpenAPI / GraphQL contracts (validated in CI) |
| Schemas | `schemas/` | JSON schemas (including UI config schemas such as layer registry) |
| Story Nodes | `docs/reports/story_nodes/` | Narrative content rendered in Focus Mode |
| Evidence + lineage | `data/stac/` + `data/catalog/dcat/` + `data/prov/` | Canonical catalogs and provenance artifacts |

### Expected file tree for this sub-area

> This tree describes **intended organization** for map components. Update to match actual code if the directory structure differs.

~~~text
📁 web/
├── 📁 src/
│   ├── 📁 map/
│   │   ├── 📁 components/
│   │   │   ├── 📄 README.md
│   │   │   ├── 📁 controls/        (map UI controls: toggles, sliders, nav)
│   │   │   ├── 📁 overlays/        (tooltips, popovers, inspect panels)
│   │   │   ├── 📁 legends/         (legends, attribution panels)
│   │   │   ├── 📁 focus_mode/      (Focus Mode map-side components)
│   │   │   ├── 📁 provenance/      (citation widgets, audit indicators)
│   │   │   └── 📁 __tests__/       (component-level tests)
~~~ 

---

## 🧭 Context

### Background

KFM’s UI layer is the user-facing map + narrative experience. The front end is expected to be a SPA under `web/` composed of React components (map view, timelines, story panels, search, etc.). Map rendering is expected to use **MapLibre GL** for 2D, and may optionally support a 3D mode (e.g., Cesium) as an extension. The map must display base maps and multiple overlays (points/polygons/rasters). A **layer registry** (config-driven) enables adding new layers without code changes, and should be schema-validated.  

Focus Mode is a dedicated UI state where a user explores a story/entity “in detail” while still retaining context (map/timeline). The UI enters Focus Mode with an entity/story ID, requests a **context bundle** from the API, and then renders narrative + map/timeline adjustments based on the returned bundle and story metadata.

### Non-negotiable constraints

- **No UI direct-to-graph reads:** web code must never bypass the API to query Neo4j.  
  - Do not import Neo4j drivers into `web/`.
  - Do not embed connection strings (e.g., `neo4j://...`) or Cypher anywhere in UI code.
- **Contracts and schemas are canonical:** UI should consume only stable contracts and schema-validated configs (e.g., layer registry validated against `schemas/ui/`).
- **Provenance-linked narrative only:** Focus Mode should only show narrative/data with traceable provenance (citations + identifiers), and should not display uncited narrative by default.

---

## 🗺️ Diagrams

### Map UI high-level dataflow

~~~mermaid
flowchart LR
  U[User interactions] --> S[UI state container]
  S --> A[API client]
  A --> B[API boundary src/server]
  B --> C[Graph + catalogs]
  A --> F[Context bundle response]
  F --> M[Map components]
  F --> N[Narrative components]
  F --> P[Provenance/Audit components]
~~~

### Focus Mode component composition (conceptual)

~~~mermaid
flowchart TB
  FM[FocusMode Shell] --> SP[Story Panel]
  FM --> MP[Map Panel]
  FM --> AP[Audit / Provenance Panel]
  MP --> LC[Layer Controls]
  MP --> IN[Inspect / Tooltip Overlay]
  SP --> CR[Citation Renderer]
~~~

---

## 🧱 Architecture

### What belongs in `web/src/map/components/`

Components in this directory should focus on **rendering** and **interaction**, not on data acquisition business logic.

Use a “thin component, thick services” pattern:

- **Components:** render map UI, controls, panels, legends, and Focus Mode map behavior.
- **Hooks/services (preferred outside this folder):** API calls, caching, parsing, and data normalization.
- **State container:** holds shared state (selected entity, active layers, timeline window, user settings) so map + story panel remain synchronized.

### Core responsibilities

| Component category | Responsibility | Interfaces / inputs |
|---|---|---|
| Map view shell | Owns MapLibre instance lifecycle and map container layout | Map style settings, active layer list, viewport state |
| Layer controls | Toggle/adjust available layers (from registry) | Layer registry entries + per-layer permissions |
| Legends + attribution | Render per-layer attribution + legend keys | Layer registry metadata + API-provided attributions |
| Inspect overlays | Hover/click inspect tooltips/popovers with provenance hints | Feature payload + provenance refs |
| Focus Mode map integration | Apply focus hints: center/time/layers and keep back navigation | Focus context bundle + focus metadata |
| Provenance widgets | Render citations, audit warnings, sensitivity notices | Citation tokens + evidence identifiers |

### Layer registry expectations

- KFM uses a **layer registry** (JSON config or TS definition) to define:
  - layer ids, names, sources/URLs, styling, attribution,
  - sensitivity flags (e.g., whether this layer requires redaction/generalization).
- The registry should be validated against a schema under `schemas/ui/` (schema path/name **not confirmed in repo**).

> Implementation note: prefer building UI layer toggles from the registry at runtime so adding a layer is “config-only” where possible.

### Focus Mode: map + timeline synchronization

Story Nodes may include optional structured controls that help Focus Mode configure the map/timeline. The Story Node template supports fields like `focus_center`, `focus_time`, and `focus_layers`. In UI, these hints are expected to arrive as part of the API-provided Focus Mode context (or be embedded in the story node content the API returns).

Example (from Story Node conventions):

~~~yaml
focus_layers:
  - "TBD"
focus_time: "TBD"
focus_center: [ -98.0000, 38.0000 ]
~~~

### Citation rendering (provenance-first UX)

Story Nodes are Markdown and include inline citation tokens (project convention). The UI should:

- Render Markdown safely.
- Convert citation tokens into interactive UI elements (footnotes, popovers, or links) that display the referenced source metadata.
- Ensure that uncited narrative is not presented as fact in Focus Mode.

---

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode

When a user selects a feature on the map (or clicks an entity link in narrative):

1. UI dispatches “enter Focus Mode” with entity/story id.
2. UI calls the Focus API to fetch a **context bundle** (narrative + related entities + provenance refs + map/timeline hints).
3. Focus Mode renders:
   - Story panel (Markdown + citations),
   - Map panel (filtered/activated layers; focused extent),
   - Audit/provenance panel (citations, flags, sensitivity notices),
   - Optional timeline state adjustments.

### Behavior expectations

- **Back navigation:** Provide a clear exit from Focus Mode and preserve prior map state where possible.
- **Focus hints:** If `focus_center` / `focus_time` are present, apply them predictably (and reversibly).
- **Provenance visibility:** citations should be visible and inspectable; provide a “Sources” view or equivalent.

### AI content rules (if present)

- Any AI-generated insight must be:
  - clearly labeled,
  - opt-in (collapsed behind a user action),
  - accompanied by referenced sources and confidence/uncertainty metadata where applicable.

---

## 🧪 Validation & CI/CD

### Validation steps (recommended)

- UI lint/format checks (repo standard; **not confirmed in repo**)
- Unit tests for map components and Focus Mode rendering
- Integration tests for critical flows:
  - enter/exit Focus Mode,
  - apply focus hints (center/time/layers),
  - citation rendering behaviors.
- E2E tests (Cypress/Playwright; framework **not confirmed in repo**) for:
  - layer toggling,
  - inspect overlays,
  - Focus Mode navigation.

### CI expectations (recommended)

- **API boundary enforcement:** fail if UI imports Neo4j drivers or contains forbidden connection strings.
- **Schema checks:** validate the layer registry against `schemas/ui/`.

### Reproduction

~~~bash
# Example placeholders — replace with repo-specific commands

# Run UI unit tests
# npm test

# Run e2e tests
# npm run e2e

# Validate UI schemas (layer registry)
# npm run validate:ui-schemas
~~~

---

## 📦 Data & Metadata

### Inputs

| Input | Source | Notes |
|---|---|---|
| Focus context bundle | API responses | Narrative + map/timeline hints + provenance refs |
| Layer registry config | `web/**/layers/**` (location varies; not confirmed) | Drives layer toggles and attribution |
| Story Node Markdown | `docs/reports/story_nodes/**` | Rendered by Focus Mode story panel |

### Outputs

| Output | Format | Notes |
|---|---|---|
| Rendered map + overlays | UI state | Must not leak sensitive locations |
| Rendered citations/audit indicators | UI state | Must remain traceable to evidence IDs |
| Optional telemetry | Events | If implemented, avoid logging sensitive coordinates |

---

## 🌐 STAC, DCAT & PROV Alignment

The UI does not generate STAC/DCAT/PROV, but it should **surface** evidence and provenance where available:

- Show layer attributions (from registry metadata).
- Display dataset/item identifiers (when returned in the context bundle).
- Provide UX affordances that let users inspect “what is this claim based on?” (citations, sources panel).
- Respect redaction/generalization decisions already enforced by the API.

---

## ⚖ FAIR+CARE & Governance

- Treat any map layer or interaction that could expose sensitive locations (e.g., high zoom + click-to-reveal exact coordinates) as **high risk** and subject to governance review.
- Never implement “client-side reconstruction” of redacted data (e.g., inferring exact points from coarse areas).
- Ensure Focus Mode can render sovereignty/sensitivity notices delivered by the API (and does not suppress them).

---

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-25 | Initial `web/src/map/components/` README (responsibilities, boundaries, Focus Mode integration) | (you) |

---

## Footer refs (do not remove)

- Master guide: `docs/MASTER_GUIDE_v12.md`
- v13 blueprint (if adopted): `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md`
- Universal template: `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`
- Story Node template: `docs/templates/TEMPLATE__STORY_NODE_V3.md`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
- Ethics: `docs/governance/ETHICS.md`
---

