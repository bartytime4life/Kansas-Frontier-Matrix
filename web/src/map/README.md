---
title: "KFM Web Map Module README"
path: "web/src/map/README.md"
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

# `web/src/map/` — Map module

> **Purpose (required):** This folder is the UI “map engine + map rendering” module. It owns the React-facing integration with MapLibre, renders schema-driven data layers, and coordinates map interactions with Focus Mode and Story Node rendering **without** crossing the API boundary.

## 📘 Overview

### Purpose

This module exists to provide a consistent, testable place for:

- instantiating and managing the map engine (MapLibre GL JS, and any adapter code),
- loading and rendering map layers defined in the UI layer registry,
- handling map interactions (hover/select) and forwarding selections to Focus Mode orchestration,
- enforcing UI-side governance behaviors (provenance visibility, redaction cues, and interaction constraints),
- keeping map state synchronized with narrative panels (Story Nodes) and other UI components.

### Scope

| In scope | Out of scope |
|---|---|
| Map engine integration, view state, layer rendering, interaction/selection plumbing | API endpoints, database/graph access, ETL/catalog generation, Story Node authoring |
| Parsing/using layer registry configs and mapping them into rendered layers | Defining the canonical layer registry schema itself (belongs in `schemas/ui/`) |
| UI-side affordances: legends, attribution, provenance links, redaction notices | Redaction/generalization logic as a policy decision (must be enforced at API boundary) |

### Audience

- UI engineers working in `web/`
- API engineers needing to understand what the map expects to consume
- Reviewers validating governance and “no leakage” behavior

### Definitions

- **Map engine:** The underlying rendering and interaction library (e.g., MapLibre GL JS).
- **Layer registry:** A JSON configuration set describing available map layers, their data sources, styling, attribution, and sensitivity.
- **Focus Mode:** A UI mode showing provenance-linked context for a selected entity (map highlight + narrative panel).
- **Story Node:** Governed narrative artifact with citations and entity references (rendered in the UI; authored elsewhere).
- **Provenance:** Evidence links (STAC/DCAT/PROV identifiers) that allow auditing “why this appears in the UI.”

> Glossary reference: `docs/glossary.md` (not confirmed in repo; add if missing).

### Key artifacts

| Artifact | Path | Notes |
|---|---|---|
| Master Guide | `docs/MASTER_GUIDE_v12.md` | Canonical pipeline + invariants |
| Redesign blueprint | `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md` | Canonical roots + minimum contract set |
| UI registry schemas | `schemas/ui/` | Layer registry and other UI config schemas |
| UI layer registries | `web/**/layers/**` | JSON configs describing layers (exact subpath may vary) |
| API boundary | `src/server/` | Map consumes all graph/catalog content through APIs |
| Story Nodes | `docs/reports/story_nodes/` | Focus Mode narrative artifacts |

### Definition of done

A change in this folder is “done” when:

- [ ] Map renders without runtime errors and does not degrade baseline performance.
- [ ] Layer registry entries used by the map validate against `schemas/ui/` (CI or local validation).
- [ ] All map-driven data access flows through the API boundary (no direct graph/DB usage in `web/`).
- [ ] Focus Mode selection shows provenance/citations and respects redaction cues.
- [ ] Sensitive layers have explicit interaction constraints (e.g., max zoom, aggregation, limited tooltips) and clear user messaging.
- [ ] Tests (unit/integration/e2e as applicable) pass deterministically, including accessibility checks.

## 🗂️ Directory Layout

### This document

- `path`: `web/src/map/README.md` (must match front‑matter)

### Related repository paths

| Area | Path | Why it matters to the map |
|---|---|---|
| UI boundary | `web/` | This module lives inside the canonical UI home |
| UI schemas | `schemas/ui/` | Layer registry and UI config validation |
| API boundary | `src/server/` | All data access must flow through contracted APIs |
| Catalogs | `data/stac/`, `data/catalog/dcat/`, `data/prov/` | Map consumes evidence IDs and metadata via APIs |
| Story Nodes | `docs/reports/story_nodes/` | Narrative payloads rendered alongside map context |
| CI workflows | `.github/workflows/` | Contract/schema lint and “forbidden patterns” checks |

### Expected file tree for this sub-area

> Note: The exact filenames and subfolders under `web/src/map/` are **not confirmed in repo**. Use this as the **target shape**. If the actual module structure differs, update this README to match.

~~~text
📁 web/src/map/
├── 📄 README.md
├── 📁 components/               — Map React components (containers + UI primitives)
├── 📁 engine/                   — MapLibre adapter / lifecycle management
├── 📁 layers/                   — Layer constructors and render helpers
├── 📁 registry/                 — Layer registry loaders + validators (runtime)
├── 📁 styles/                   — Style helpers (MapLibre style fragments, legends)
├── 📁 hooks/                    — React hooks (view state, selection, layer toggles)
├── 📁 state/                    — Map-related state slice (if applicable)
└── 📁 utils/                    — Projection, bbox, formatting, safety helpers
~~~

## 🧭 Context

KFM is contract-first and provenance-first. The UI must:

- treat **APIs** as the only access point to graph + catalog content,
- render **provenance** and **citations** as first-class UI elements,
- avoid “hidden leakage” by respecting redaction/generalization signals.

This module sits at the UI stage of the canonical flow:

**ETL → STAC/DCAT/PROV → Graph → API → UI → Story Nodes → Focus Mode**

Implications for map code:

- The map is a **consumer** of contracts and evidence artifacts, not a producer.
- “What layers exist” should be registry-driven, not hard-coded.
- “What can be shown” is constrained by governance; sensitive geometry must not be revealed by UI affordances.

## 🗺️ Diagrams

### Map module interaction flow

~~~mermaid
flowchart TB
  subgraph UI[web UI]
    Map[Map module<br/>web/src/map]
    Panel[Story panel<br/>Story Node renderer]
    Controls[Layer controls<br/>toggles/legend]
  end

  subgraph Contracts[Contracts]
    UISchema[schemas/ui<br/>registry schema]
    LayerReg[web/**/layers/**<br/>layer registry JSON]
  end

  subgraph API[API boundary<br/>src/server]
    Focus[Focus Mode endpoint]
    Layers[Layer data endpoints<br/>tiles/geojson/queries]
  end

  Map --> Controls
  Controls --> Map
  LayerReg --> Map
  UISchema -. validate .-> LayerReg

  Map -->|select/hover| Focus
  Focus -->|entity + story + sources| Panel
  Map -->|load layer data| Layers
~~~

## 🧠 Story Node & Focus Mode Integration

### What the map must do

When a user selects an entity/feature on the map:

1. The map emits a stable **selection event** (entity id, feature id, layer id).
2. Focus Mode orchestration requests provenance-linked context via the API boundary.
3. The map highlights geometry (if permitted) and the Story panel renders narrative + citations.
4. The UI must show provenance/citations consistently (not as optional decoration).

### Expected Focus Mode payload shape

The exact contract is defined under `src/server/contracts/` (not confirmed in repo for this file), but the UI should expect a response that contains:

- the selected **entity**,
- the associated **Story Node** narrative,
- **related entities** for additional context,
- a **sources** list enabling citation rendering (dataset IDs, evidence links).

~~~json
{
  "entity": { "id": "…", "label": "…", "type": "…" },
  "storyNode": { "id": "…", "content": "…", "citations": ["…"] },
  "relatedEntities": [{ "id": "…", "type": "…" }],
  "sources": [{ "id": "…", "kind": "stac|dcat|prov|doc", "ref": "…" }]
}
~~~

### Map-specific Focus Mode rules

- Never display facts without a corresponding citation link in the Story panel.
- If a layer or feature is sensitive/redacted, the map must:
  - avoid exposing raw coordinates through tooltips/debug panels,
  - respect max zoom constraints (or other UI restrictions),
  - show a redaction notice that explains why detail is limited.

## 🧪 Validation & CI/CD

Minimum expectations for map-related changes:

### Static checks

- Typecheck and lint the map module.
- Run dependency/security scanning (no secrets; no unsafe eval).
- Validate that UI layer registries pass schema checks (`schemas/ui/`).

### Forbidden pattern checks

- Ensure `web/` does not contain direct graph/DB drivers or direct Neo4j calls.
- Ensure map module only calls the API boundary using the approved client/utilities.

### Runtime checks

- E2E test: layer toggles on/off; selection triggers Focus Mode; citations render.
- Accessibility: keyboard navigation for map controls; focus management; ARIA labels for non-map controls; avoid focus traps.

> If CI includes “forbidden pattern lint” (recommended), map changes must remain compliant.

## 📦 Data & Metadata

### What the map consumes

Typical map inputs include:

- basemap tiles (public sources, or KFM-hosted tiles),
- vector overlays (points, lines, polygons),
- raster overlays (historical scans, heatmaps),
- evidence metadata (STAC/DCAT/PROV IDs surfaced by APIs),
- layer registry config for defaults, attribution, and sensitivity classification.

### What the map must never assume

- The map must not assume raw geometry is always safe to display.
- The map must not assume a dataset exists “because it’s in the registry”; it must handle missing/unavailable endpoints gracefully.
- The map must not treat styling as “purely visual” if it affects interpretability or could leak detail.

## 🌐 STAC, DCAT & PROV Alignment

This UI module does not emit STAC/DCAT/PROV. Instead, it must:

- preserve and display evidence identifiers returned by APIs,
- link layers/features back to their evidence artifacts (directly or via the Focus Mode response),
- render provenance affordances in a way that is usable (not hidden behind developer tooling).

Recommended UI practices:

- For any layer toggle, provide attribution and evidence links (when available).
- For any selected feature, provide a “Why am I seeing this?” affordance that routes to provenance/citations.

## 🧱 Architecture

### Core responsibilities

1. **Map container**
   - Owns map lifecycle and viewport state
   - Coordinates subcomponents: controls, overlays, selection

2. **Engine adapter**
   - Wraps MapLibre GL JS lifecycle (create map, set style, add/remove layers)
   - Handles cleanup and event binding

3. **Layer system**
   - Converts registry entries into rendered layers
   - Handles dynamic updates (filtering, time slider hooks, visibility toggles)

4. **Interaction layer**
   - Hover/select behavior
   - Feature identification and selection normalization
   - Event emission to Focus Mode orchestration

### Layer registry integration

KFM expects layer availability to be registry-driven. A layer registry entry should minimally include:

- stable `id`
- user-facing `name`
- data `source` reference (API endpoint, tiles, etc.)
- attribution/credits
- sensitivity classification and interaction constraints
- styling reference

The canonical schema for this belongs in `schemas/ui/`.

#### Example registry entry

> Example only; fields must match the actual schema in `schemas/ui/`.

~~~json
{
  "id": "example-layer",
  "name": "Example Layer",
  "type": "vector",
  "source": {
    "kind": "api",
    "endpoint": "/api/layers/example-layer"
  },
  "attribution": "…",
  "sensitivity": "public",
  "constraints": { "maxZoom": 12 },
  "styleRef": "example-style"
}
~~~

### Adding a new map layer

Use this checklist to keep the pipeline consistent:

1. **Evidence exists**
   - Dataset outputs live under `data/<domain>/processed/`
   - STAC/DCAT/PROV artifacts exist and validate

2. **API exists**
   - There is a contracted API endpoint that serves the layer’s data
   - Redaction/generalization happens at the API boundary

3. **Registry entry exists**
   - Add the layer to a registry JSON under `web/**/layers/**`
   - Ensure it validates against `schemas/ui/`

4. **Map rendering exists**
   - Implement or reuse a layer renderer in this module
   - Add legend/attribution handling

5. **Governance checks**
   - If layer detail could reveal sensitive locations by interaction or zoom, request review before release
   - Ensure redaction cues are visible in the UI

6. **Tests**
   - Add/extend tests for registry validation, toggles, and selection → Focus Mode flow

## ⚖ FAIR+CARE & Governance

### Non-negotiables

- The UI must not connect to Neo4j directly; all graph access is via the API boundary.
- Focus Mode must show provenance-linked context only.
- New UI layers that could reveal sensitive locations via interaction or zoom require review.

### Practical map UI safeguards

- Default to conservative tooltips for sensitive layers (no raw coordinates).
- Limit max zoom or geometry detail for sensitive layers (as signaled by the API and registry).
- Always show attribution and provenance where available.
- Log or surface governance signals as defined by telemetry conventions (if adopted).

### AI assistance

If any AI-assisted UI features exist in the future, they must be:

- opt-in,
- clearly marked,
- uncertainty-annotated,
- never presented as unmarked fact.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-25 | Initial `web/src/map/` README scaffold | TBD |

---

Footer refs:

- Master Guide: `docs/MASTER_GUIDE_v12.md`
- Redesign blueprint: `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md`
- Universal template: `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`

