---
title: "KFM Web Map Module README"
path: "web/src/map/README.md"
version: "v1.0.0"
last_updated: "2025-12-28"
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

doc_uuid: "urn:kfm:doc:web:src:map:readme:v1.0.0"
semantic_document_id: "kfm-web-src-map-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:web:src:map:readme:v1.0.0"
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

# web/src/map — Map module

> **Purpose (required):** This folder is the UI **map engine + map rendering** module. It owns the React-facing integration with **MapLibre**, renders **schema-driven layers** from UI registries, and coordinates map interactions with **Focus Mode** and **Story Node** rendering **without** crossing the API boundary.

## 📘 Overview

### Purpose

This module exists to provide a consistent, testable place for:

- instantiating and managing the map engine lifecycle (MapLibre GL JS and adapter code),
- loading and rendering map layers defined in a UI layer registry (schema-validated),
- handling user interactions (hover/select) and emitting **stable selection events**,
- coordinating with Focus Mode orchestration so that map selections drive provenance-linked context,
- surfacing governance signals in the UI (attribution, provenance links, redaction cues),
- keeping map state synchronized with narrative panels and other UI components.

### Scope

| In Scope | Out of Scope |
|---|---|
| Map engine lifecycle, view state, rendering of registry-defined layers, interaction/selection plumbing | ETL/catalog generation, graph ingest/migrations, API implementation, Story Node authoring |
| Using layer registry configs and mapping them into rendered layers | Defining canonical schemas for registries (belongs in `schemas/ui/`) |
| UI affordances: legend, attribution/provenance links, redaction notices, interaction constraints | Policy decisions and enforcement logic for redaction/generalization (must be enforced at API boundary) |
| Defensive UI behaviors to prevent leakage (e.g., tooltip discipline, zoom constraints) | Bypassing API boundary or directly querying Neo4j/DB from the UI |

### Audience

- UI engineers working in `web/`
- API engineers validating “what the map expects” and ensuring contracts support it
- Governance reviewers validating “no hidden data leakage” behaviors
- Domain stewards reviewing how evidence/provenance is surfaced in the map UI

### Definitions

- **Map engine:** The rendering and interaction library (MapLibre GL JS).
- **Layer registry:** JSON configuration describing available layers, data sources, attribution, styling hooks, sensitivity, and interaction constraints.
- **Focus Mode:** A UI experience that consumes **only provenance-linked** context bundles for a selected entity/feature.
- **Story Node:** A governed narrative artifact with explicit citations and entity references, rendered in the UI.
- **Provenance:** Evidence identifiers/links (STAC/DCAT/PROV + doc IDs) that support “why this appears in the UI.”
- **Redaction cues:** API/registry-provided signals that constrain interaction/zoom/tooltips to prevent disclosure of sensitive locations.

> Glossary reference: `docs/glossary.md` *(not confirmed in repo; recommended)*.

### Key artifacts

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master Guide v12 | `docs/MASTER_GUIDE_v12.md` | TBD | Canonical pipeline + invariants |
| Universal doc template | `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` | Docs | Required structure for governed Markdown |
| v13 redesign blueprint (draft) | `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md` | Architecture | Canonical homes + contract-first + evidence-first |
| UI registry schemas | `schemas/ui/` | UI + Docs | Layer registry and other UI config schemas |
| API boundary | `src/server/` | API | All map data must flow through APIs (no direct graph/DB) |
| Story Nodes | `docs/reports/story_nodes/` | Story | Governed narratives; rendered in Focus Mode |

### Definition of done

A change in this folder is “done” when:

- [ ] Map renders without runtime errors and does not degrade baseline performance.
- [ ] Any layer registry entries used by the map validate against `schemas/ui/` (CI or local validation).
- [ ] All map-driven data access flows through the API boundary (no direct graph/DB calls or drivers in `web/`).
- [ ] Focus Mode selection shows provenance/citations and respects redaction cues.
- [ ] Sensitive layers have explicit interaction constraints (e.g., max zoom, aggregation, limited tooltips) and clear user messaging.
- [ ] Tests (unit/integration/e2e as applicable) pass deterministically, including accessibility checks.

## 🗂️ Directory Layout

### This document

- `path`: `web/src/map/README.md` (must match front-matter)

### Related repository paths

| Area | Path | Why it matters to the map |
|---|---|---|
| UI boundary | `web/` | This module lives inside the canonical UI home |
| UI schemas | `schemas/ui/` | Layer registry and UI config validation |
| API boundary | `src/server/` | All data access must flow through contracted APIs |
| Catalog outputs | `data/stac/`, `data/catalog/dcat/`, `data/prov/` | Evidence IDs and metadata are surfaced via APIs |
| Story Nodes | `docs/reports/story_nodes/` | Narrative payloads rendered alongside map context |
| CI workflows | `.github/workflows/` | Schema lint, forbidden patterns, security/a11y gates |

### Expected file tree for this sub-area

> Note: Filenames and subfolders under `web/src/map/` are **not confirmed in repo**. Treat this as the **target shape**; align to the actual tree if different.

~~~text
📁 web/src/map/
├── 📄 README.md
├── 📁 components/              — React components (map container, controls, overlays)
├── 📁 engine/                  — MapLibre adapter + lifecycle management
├── 📁 layers/                  — Layer constructors/renderers (vector/raster helpers)
├── 📁 registry/                — Registry loaders + runtime validators/adapters
├── 📁 hooks/                   — React hooks (view state, selection, layer toggles)
├── 📁 state/                   — Map state slice (if used; store integration)
├── 📁 events/                  — Selection event types + emitters (stable payloads)
├── 📁 styles/                  — Style helpers (fragments, legend helpers)
├── 📁 types/                   — Shared TS types (registry model, constraints)
└── 📁 utils/                   — bbox, projection, formatting, safety helpers
~~~

## 🧭 Context

### Background

KFM is **contract-first** and **provenance-first**. The UI must treat **APIs** as the only access point to graph + catalogs, and must render **provenance/citations** as first-class UI elements. The map is a key surface where “hidden leakage” can happen (via zoom, tooltips, debug panels, or geometry detail), so it must be conservative-by-default and respect governance signals.

Canonical pipeline ordering is non-negotiable:

**ETL → STAC/DCAT/PROV → Graph → API → UI → Story Nodes → Focus Mode**

### Assumptions

- The UI uses React, and MapLibre is the primary 2D map engine for this module.
- Layer availability is registry-driven (schema-validated) rather than hard-coded.
- Focus Mode consumes a provenance-linked context bundle returned from the API boundary.
- Redaction/generalization decisions are enforced at the API boundary and surfaced to the UI as explicit cues/constraints.

### Constraints and invariants

| Constraint / Invariant | Why it exists | How the map must comply |
|---|---|---|
| Pipeline ordering is fixed | Evidence must be cataloged before UI/narrative surfacing | UI consumes only APIs that surface evidence IDs |
| API boundary is hard | Prevent policy bypass and ensure consistent enforcement | No direct Neo4j/DB calls or drivers in `web/` |
| Provenance-first rendering | User trust depends on traceable sources | Always show attribution + evidence links where available |
| No sensitive-location leakage | Interactive maps can reveal protected details | Respect constraints (zoom/tooltips/aggregation); never expose raw coords when redacted |
| Stable identifiers | Focus Mode + citations require stable references | Emit selection events with stable IDs (entity/layer/feature refs) |
| Accessibility | Map controls must be usable beyond mouse/touch | Provide keyboard + ARIA for all non-map controls; manage focus safely |

### Open questions

| Question | Owner | Target date | Notes |
|---|---:|---:|---|
| Where is the canonical layer registry root in `web/`? | UI | TBD | Expected pattern: `web/**/layers/**` (exact path not confirmed) |
| What is the canonical selection event schema and where is it defined? | UI + API | TBD | Recommend a shared TS type under `web/src/map/events/` |
| What API endpoints are used for layers (tiles vs GeoJSON vs queries)? | API | TBD | Requires contract documentation under `src/server/` |
| How are redaction cues signaled (flags, constraints, metadata fields)? | API + Governance | TBD | UI must interpret cues consistently across layers |
| Is there a global time slider contract the map must honor? | UI | TBD | Coordinate with Story/Focus mode expectations |

### Future extensions

- Time-aware layers (timeline slider hooks) driven by contracted API params.
- 3D/altitude visualization (if Cesium/3D is adopted elsewhere, keep API boundary unchanged).
- Offline/provenance snapshots for Story Node “published” bundles.
- Performance enhancements (vector tile-first, clustering, request cancellation) without relaxing governance.
- Stronger UI-side “Why am I seeing this?” affordances routed to evidence bundles.

## 🗺️ Diagrams

~~~mermaid
flowchart TB
  subgraph UI[web UI]
    Map[Map module<br/>web/src/map]
    Controls[Layer controls<br/>toggles/legend]
    Panel[Story panel<br/>Story Node renderer]
    State[UI state<br/>selection + viewport]
  end

  subgraph Contracts[Contracts]
    UISchema[schemas/ui<br/>registry schema]
    LayerReg[Layer registry JSON<br/>web/**/layers/**]
  end

  subgraph API[API boundary<br/>src/server]
    Layers[Layer data endpoints<br/>tiles/geojson/query]
    Focus[Focus Mode endpoint<br/>context bundle]
  end

  LayerReg --> Map
  UISchema -. validate .-> LayerReg

  Controls --> Map
  Map --> State
  State --> Controls

  Map -->|load layer data| Layers
  Map -->|select/hover| Focus
  Focus -->|story + sources| Panel
~~~

## 📦 Data & Metadata

### Inputs

| Input | Source | Notes |
|---|---|---|
| Layer registry JSON | `web/**/layers/**` *(path not confirmed)* | Declarative list of layers + constraints |
| UI registry schema | `schemas/ui/` | Validates registry shape and required fields |
| Layer data payloads | API responses | Vector tiles / GeoJSON / query results as contracted |
| Focus Mode context bundle | API responses | Entity + story node + sources + redaction signals |
| Basemap/style config | UI config / environment | MapLibre style URL and source attribution |
| User interaction events | Browser | Hover/select/zoom/pan; must be governed by constraints |

### Outputs

| Output | Destination | Notes |
|---|---|---|
| Rendered layers and highlights | UI canvas/DOM | Must respect constraints and redaction cues |
| Selection events | UI state / Focus Mode orchestration | Use stable IDs and registry layer IDs |
| Provenance/attribution UI | UI controls/panels | Evidence links + credits should be visible/usable |
| Redaction notices | UI panels/tooltips | Explain limited detail when applicable |
| Telemetry signals | Telemetry system *(if adopted)* | Should never include sensitive raw geometry |

### Sensitivity and redaction

- The map must **not assume** raw geometry is safe to display, even if the layer exists in a registry.
- Redaction/generalization is enforced at the API boundary, but the UI must:
  - respect explicit constraints (max zoom, aggregation, disabled inspection),
  - avoid exposing raw coordinates in tooltips/debug UIs,
  - present clear user messaging when detail is limited.
- No output may be less restrictive than any upstream input in its lineage.

### Quality signals

- Registry validation errors are treated as defects (schema mismatch, missing attribution).
- Layer load failures must degrade gracefully (visible error state; no silent empty layers).
- Focus Mode must never render uncited narrative.
- Accessibility: non-map controls must be keyboard navigable and screen-reader friendly.
- Performance: avoid giant client-side GeoJSON loads when tiles/aggregation are available.

## 🌐 STAC, DCAT & PROV Alignment

This UI module does not emit STAC/DCAT/PROV. Instead, it must:

- preserve and display evidence identifiers returned by APIs,
- link layers/features back to evidence artifacts (STAC/DCAT/PROV IDs where applicable),
- render provenance affordances that are visible and usable (not hidden in developer tooling).

Recommended UI practices:

- Layer toggles should show attribution and evidence links (when available).
- Feature selection should show “Why am I seeing this?” with sources/citations.
- If evidence is missing, present it as “not yet linked” rather than implying certainty.

## 🧱 Architecture

### Core components

| Component | Responsibility | Notes |
|---|---|---|
| Map container | Own map lifecycle + viewport state | React-facing entry point |
| Engine adapter | Wrap MapLibre lifecycle, style, event binding | Must clean up deterministically |
| Registry loader | Load registry JSON + validate/normalize | Schema-driven behavior |
| Layer system | Convert registry entries into rendered layers | Supports toggles, filters, updates |
| Interaction manager | Hover/select behavior and feature identification | Normalizes selection payloads |
| Focus Mode bridge | Calls Focus Mode API endpoint on selection | Must handle redaction cues |
| Provenance UI | Attribution, evidence links, redaction notices | Visible and consistent |

### Interfaces and contracts

| Interface | Canonical home | Notes |
|---|---|---|
| UI layer registry schema | `schemas/ui/` | JSON Schema; must validate registries |
| Layer registry configs | `web/**/layers/**` *(path not confirmed)* | Declarative layer list; includes constraints + attribution |
| Focus Mode contract | `src/server/` *(contracts path not confirmed)* | Response must include sources/citations |
| Layer data contracts | `src/server/` | Tile/GeoJSON/query endpoints must carry evidence IDs |
| Telemetry schema | `schemas/telemetry/` *(if present)* | Signals must avoid sensitive geometry |

### Extension points checklist

- [ ] Data: evidence exists and is cataloged (STAC/DCAT/PROV)
- [ ] APIs: contracted endpoint exists for the layer (and enforces redaction)
- [ ] UI registry: new layer entry added + schema-valid + includes attribution/sensitivity
- [ ] Map renderer: renderer exists for layer type (vector/raster/etc.)
- [ ] Focus Mode: selection → context bundle works and citations render
- [ ] Tests: toggles + selection flow + a11y checks pass deterministically
- [ ] Telemetry: optional signals added (no sensitive leakage)

## 🧠 Story Node and Focus Mode Integration

### How this work surfaces in Focus Mode

When a user selects an entity/feature on the map:

1. The map emits a stable selection event: `layer_id`, `feature_ref`, and/or `entity_id`.
2. Focus Mode orchestration requests provenance-linked context via the API boundary.
3. The map highlights geometry (only as permitted) and the Story panel renders narrative + citations.
4. Provenance and citations must be first-class UI elements (not optional decoration).

### Provenance-linked narrative rule

- The Story panel must not display factual claims without corresponding citation links.
- If AI-assisted content is ever included, it must be opt-in and clearly labeled with uncertainty metadata.

### Optional structured controls

~~~yaml
focus_layers:
  - "TBD"          # registry layer IDs
focus_time: "TBD"  # ISO-8601 or domain-specific time key
focus_center: [-98.0000, 38.0000]
focus_zoom: 7
~~~

## 🧪 Validation & CI/CD

### Validation steps

- [ ] Markdown protocol checks (front-matter + required sections)
- [ ] UI lint/typecheck for this module
- [ ] UI registry schema validation (`schemas/ui/`)
- [ ] Forbidden pattern checks (no direct Neo4j/DB drivers in `web/`)
- [ ] API contract tests for endpoints the map consumes (if applicable)
- [ ] E2E selection → Focus Mode → citations render
- [ ] Accessibility checks for map controls and narrative panels
- [ ] Security/sovereignty scans as applicable (PII + sensitive-location leakage)

### Reproduction

~~~bash
# Example placeholders — replace with repo-specific commands
# 1) validate UI schemas (layer registry)
# 2) run UI lint/typecheck/tests
# 3) run e2e tests for Focus Mode selection flow
# 4) run doc lint / markdown protocol validation
~~~

### Telemetry signals (if applicable)

| Signal | Source | Where recorded |
|---|---|---|
| `layer_registry_validated` | UI runtime | `schemas/telemetry/` + telemetry store (if adopted) |
| `layer_data_request_failed` | UI runtime | error log/telemetry (no sensitive payloads) |
| `focus_mode_requested` | UI runtime | telemetry (entity/layer IDs only) |
| `focus_mode_redaction_notice_shown` | UI runtime | telemetry (layer_id, redaction_method) |
| `redaction_applied` | API | server logs + PROV/telemetry (preferred) |

## ⚖ FAIR+CARE & Governance

### Review gates

- Changes that add or modify **layers** should be reviewed by UI maintainers.
- Any change that could reveal sensitive locations via interaction/zoom requires governance review.
- Contract changes (registry schema or API responses) require compatibility review and versioning discipline.

### CARE and sovereignty considerations

- Identify impacted communities and any special handling requirements (CARE).
- Treat sensitive locations as high-risk by default; do not “reverse engineer” detail from aggregates.
- Ensure classification and sensitivity propagate consistently across data → catalogs → API → UI.

### AI usage constraints

- This document allows AI transformations for summarize/structure/translate/index only.
- Prohibited: generating policy or inferring sensitive locations.
- Any AI-driven UI features must be opt-in, clearly labeled, and uncertainty-annotated.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-28 | Remade to align with Universal template structure; clarified API boundary, provenance-first rendering, and redaction-safe UI behavior | TBD |

---

Footer refs:
- Master Guide: `docs/MASTER_GUIDE_v12.md`
- v13 redesign blueprint (draft reference): `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md`
- Universal template: `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
