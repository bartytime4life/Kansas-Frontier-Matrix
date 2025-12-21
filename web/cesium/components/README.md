---
title: "KFM UI — Cesium Components README"
path: "web/cesium/components/README.md"
version: "v1.0.0"
last_updated: "2025-12-21"
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

doc_uuid: "urn:kfm:doc:web:cesium:components-readme:v1.0.0"
semantic_document_id: "kfm-web-cesium-components-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:web:cesium:components-readme:v1.0.0"
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

# web/cesium/components — README

## 📘 Overview

### Purpose

This README governs **frontend conventions** for Cesium-based UI components in KFM, with special emphasis on:

- maintaining the **API boundary** (UI consumes API contracts; UI does not query Neo4j directly)
- maintaining **provenance visibility** in Focus Mode and map interactions
- keeping Cesium usage compatible with the broader map UI architecture (e.g., 2D/3D switching)

### Scope

| In Scope | Out of Scope |
|---|---|
| Cesium UI component responsibilities, boundaries, patterns | Backend ETL, STAC/DCAT/PROV generation, graph modeling |
| Focus Mode mapping behaviors that Cesium components must support | Authoring Story Nodes themselves (see story node template) |
| UI safety rules: provenance display, opt-in predictive content behaviors | Defining new API endpoints/contracts (use API Contract Extension template) |

### Audience

- Primary: Frontend engineers working on `web/` map UI and Cesium integration
- Secondary: API engineers verifying UI contract expectations, reviewers checking governance/a11y

### Definitions (link to glossary)

- Link: `docs/glossary.md`
- Terms used in this doc: Cesium, Viewer, DataSource, Layer, Focus Mode, Provenance, STAC, PROV

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master guide (pipeline + invariants) | `docs/MASTER_GUIDE_v12.md` | Maintainers | Canonical ordering + “do not break” rules |
| Universal governed doc template | `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` | Maintainers | Structure + CI expectations |
| Story node template (Focus hints) | `docs/templates/TEMPLATE__STORY_NODE_V3.md` | Maintainers | `focus_center`, `focus_time`, optional focus layers |
| API contract template | `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md` | API owners | Use when changing endpoints/contracts |

### Definition of done (for this document)

- [ ] Front-matter complete + valid
- [ ] No repo-claims beyond what is verified (unknowns marked “not confirmed in repo”)
- [ ] Constraints/invariants listed (API boundary, pipeline ordering, provenance rules)
- [ ] Validation steps listed (lint + UI tests guidance)
- [ ] Governance + CARE/sovereignty considerations explicitly stated

## 🗂️ Directory Layout

### This document

- `path`: `web/cesium/components/README.md`

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| Data domains | `data/` | Raw/work/processed/stac outputs |
| Documentation | `docs/` | Canonical governed docs |
| Graph | `src/graph/` | Graph build + ontology bindings |
| Pipelines | `src/pipelines/` | ETL + catalogs + transforms |
| Schemas | `schemas/` | JSON schemas + telemetry schemas |
| Frontend | `web/` | React + map clients |
| MCP | `mcp/` | Experiments, model cards, SOPs |

### Expected file tree for this sub-area

~~~text
📁 web/
└── 📁 cesium/
    └── 📁 components/
        └── 📄 README.md
~~~

## 🧭 Context

### Background

KFM’s frontend is a map + narrative UI (React) that may render geospatial content in 2D and/or 3D.
Cesium components exist to support 3D use cases (e.g., terrain, globe, time-dynamic visualization)
while preserving the same governance constraints used across the app.

### Assumptions

- Cesium usage is encapsulated in components that can be mounted/unmounted cleanly without memory leaks.
- Data shown in Cesium is sourced through the same API layer used by the rest of the UI.
- If a 2D/3D toggle exists, it should preserve user state (selected entity, active layers) across modes.

### Constraints / invariants

- Canonical pipeline ordering is preserved:
  **ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode**
- Frontend consumes contracts via APIs (no direct graph dependency).
- Focus Mode must only present provenance-linked content; any predictive content must be opt-in and carry uncertainty/confidence metadata.

### Open questions

| Question | Owner | Target date |
|---|---|---|
| Where is the canonical layer registry/config for Cesium layers? (not confirmed in repo) | UI | TBD |
| What is the chosen state management approach (Redux vs Context/Reducers)? (not confirmed in repo) | UI | TBD |
| How are Cesium access tokens/keys managed (if needed)? (not confirmed in repo) | UI/Security | TBD |

### Future extensions

- Add adapter components for Cesium-native formats (e.g., CZML / 3D Tiles) when the data catalog provides them.
- Add richer provenance overlays (hover/click reveals STAC asset + PROV run ID) when API contracts expose these fields.

## 🗺️ Diagrams

### System / dataflow diagram

~~~mermaid
flowchart LR
  A["API Responses<br/>(context bundle + layers + provenance refs)"] --> B["Cesium Components"]
  B --> C["Viewer Render<br/>(3D layers + entities)"]
  C --> D["UI Events<br/>(select / hover / time)"]
  D --> A
~~~


### Optional: sequence diagram (Focus Mode + map focus)

> Note: Some Mermaid renderers throw runtime errors on `sequenceDiagram` (e.g., “reading 'x' / t is undefined”).
> When that happens, use this **sequence-style flowchart** instead (it is more portable across renderers). :contentReference[oaicite:0]{index=0}

~~~mermaid
flowchart TB
  U["User"] -->|Select entity / story| UI["React UI"]
  UI -->|Fetch focus context bundle (entityId)| API["API Layer"]
  API -->|Return: narrative + focus hints + provenance refs| UI
  UI -->|Apply focus center/time; activate focus layers| C["Cesium Components"]
  C -->|Selection/hover events + provenance pointers| UI
~~~

## 📦 Data & Metadata

### Inputs

| Input | Format | Where from | Validation |
|---|---|---|---|
| Focus context bundle | JSON | API layer | Contract tests + runtime guards |
| Layer registry/config | JSON | UI config (not confirmed in repo) | Schema validation |
| User settings | UI state | Local state/store | Type checks + defaults |

### Outputs

| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Rendered 3D view | DOM/WebGL | `web/` runtime | N/A |
| UI interaction events | JS events/state | `web/` runtime | N/A |
| Telemetry events (if any) | JSON | `docs/telemetry/` + `schemas/telemetry/` | Telemetry schema (if present) |

### Sensitivity & redaction

- Components must respect any “sensitive layer” flags conveyed via API/config.
- If a layer/entity is marked restricted, Cesium components must not reveal precise geometry beyond what policy allows.

### Quality signals

- Avoid blocking the main thread with large parsing; prefer incremental loading.
- Ensure deterministic rendering given the same inputs (where possible) to support reproducibility in demos/tests.
- Provide clean unmount behavior (detach handlers, destroy viewer/resources).

## 🌐 STAC, DCAT & PROV Alignment

### STAC

- Cesium UI should be able to link visualized layers back to **STAC Item / Asset IDs** when provided by the API.

### DCAT

- Where dataset-level metadata is shown in UI (layer info panels), prefer DCAT-aligned fields (title/description/license).

### PROV-O

- When showing derived or transformed layers, surface a **PROV activity/run identifier** if available in the API payload.
- In Focus Mode, provenance references should be visible and usable (audit panel / sources panel pattern).

### Versioning

- UI should tolerate versioned datasets and prefer stable identifiers (e.g., predecessor/successor links) when present.

## 🧱 Architecture

### Components

Recommended component boundary map (names are illustrative; not confirmed in repo):

| Component type | Responsibility | Interface |
|---|---|---|
| Viewer host | Own Cesium viewer lifecycle (mount/unmount) | Props: initial camera, clock/time, imagery/terrain flags |
| Layer bridge | Translate “layer config” to Cesium primitives | Input: layer registry + API layer metadata |
| Data adapters | Convert API payloads to Cesium entities/data sources | Input: GeoJSON-like data, time series hints |
| Interaction handlers | Click/hover/select → dispatch UI actions | Emits: selected entity ID + provenance pointers |
| Focus helpers | Apply focus hints (`focus_center`, `focus_time`, layer toggles) | Input: Focus Mode bundle |

### Interfaces / contracts

- Cesium components **must not** query Neo4j or catalogs directly.
- Cesium components consume:
  - API responses (contracted JSON)
  - local UI configuration (schema-validated)
  - user state

### Extension points checklist (for future work)

- [ ] UI: add new 3D layer entry in registry/config (if used) with attribution + sensitivity flags
- [ ] API: ensure contract exposes provenance refs (STAC/PROV IDs) for the layer
- [ ] UI: implement adapter for the new layer type (CZML/3D Tiles/etc.)
- [ ] Focus Mode: support focus hints for the layer (auto-enable when relevant)
- [ ] Tests: add unit/integration coverage for rendering + provenance display
- [ ] Governance: confirm redaction/generalization behavior for sensitive geometries

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode

- When Focus Mode activates, Cesium components should:
  - center/zoom camera to `focus_center` (if provided)
  - align time controls to `focus_time` (if provided)
  - enable/disable specific layers (if provided)
  - preserve provenance affordances (“Sources/Audit” UI patterns)

### Provenance-linked narrative rule

- Any story/narrative UI rendered alongside Cesium must be provenance-linked.
- If AI/predictive content appears, it must be clearly labeled and opt-in, with uncertainty/confidence metadata.

### Optional structured controls (example)

~~~yaml
focus_layers:
  - "TBD"
focus_time: "TBD"
focus_center: [ -98.0000, 38.0000 ]
~~~

## 🧪 Validation & CI/CD

### Validation steps

- [ ] Markdown protocol checks (front-matter + structure)
- [ ] UI lint/typecheck (tooling not confirmed in repo)
- [ ] Unit tests for component lifecycle + focus hint application (tooling not confirmed in repo)
- [ ] Integration test for Focus Mode → Cesium: provenance visible + no restricted leaks
- [ ] Accessibility review for any Cesium-linked UI controls (keyboard/focus/labels)

### Reproduction

~~~bash
# Replace with repo-specific commands (not confirmed in repo)

# 1) run UI lint/typecheck
# 2) run UI unit/integration tests
# 3) run markdown/doc lint
~~~

### Telemetry signals (if applicable)

| Signal | Source | Where recorded |
|---|---|---|
| FocusModeEntered | UI routing/state | `docs/telemetry/` + `schemas/telemetry/` |
| LayerToggled3D | Cesium layer bridge | `docs/telemetry/` + `schemas/telemetry/` |

## ⚖ FAIR+CARE & Governance

### Review gates

- UI maintainers review for lifecycle/perf correctness and contract alignment
- Governance/ethics review required if:
  - new sensitive layers are introduced
  - new AI narrative behaviors are added
  - new public-facing endpoints/contracts are added

### CARE / sovereignty considerations

- If layers contain culturally sensitive locations or community-restricted knowledge:
  - ensure generalization/redaction rules are implemented at the API boundary and respected in UI
  - avoid “precision by default” (e.g., exact coordinates) unless explicitly approved

### AI usage constraints

- Ensure this doc’s AI permissions/prohibitions match intended use.
- Do not represent policy decisions as AI-generated content; defer to governed docs under `docs/governance/`.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-21 | Initial Cesium components README (governed) | TBD |

---

Footer refs:

- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
