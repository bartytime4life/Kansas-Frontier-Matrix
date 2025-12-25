---
title: "KFM UI Subsystem README"
path: "web/src/ui/README.md"
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

doc_uuid: "urn:kfm:doc:web:src:ui:readme:v1.0.0"
semantic_document_id: "kfm-web-src-ui-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:web:src:ui:readme:v1.0.0"
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

# web/src/ui

This directory is the **UI subsystem surface area** for KFM’s `web/` frontend: reusable UI primitives for **map + timeline + Focus Mode + Story Node rendering**, designed to enforce KFM’s core invariants (API boundary, provenance-first narrative, contract-driven configuration).

> Note: Folder names in this README include a recommended “target” layout. If the current repo layout differs, update this file so documentation matches reality.

## 📘 Overview

### Purpose

- Explain what belongs in `web/src/ui/` and what does not.
- Document the **non-negotiable UI invariants**: the UI never reads Neo4j directly, and Focus Mode/Story Nodes must not present unsourced narrative.
- Provide contributor checklists for adding layers, Focus Mode UX, and narrative rendering safely.

### Scope

| In Scope | Out of Scope |
|---|---|
| UI components, hooks, state, and utilities used by the KFM React app | ETL implementations, graph migrations, and server-side authorization |
| Map + timeline + Focus Mode UI contracts and patterns | Direct Neo4j access from frontend code |
| Story Node rendering UX and citation/provenance panels | Authoring new governance policy (belongs under `docs/governance/`) |
| Layer registry patterns (config-driven UI) | Storing data outputs under `web/` or `src/` |

### Audience

- Primary: Frontend contributors implementing map/timeline/Focus Mode UX.
- Secondary: API and data contributors who need to understand how UI consumes contracts and evidence.

### Definitions

- Link: `docs/glossary.md` *(not confirmed in repo)*
- Terms used in this doc include: **API boundary**, **Focus Mode**, **Story Node**, **layer registry**, **provenance panel**, **redaction**, **generalization**, **STAC**, **DCAT**, **PROV**, **stable identifier**.

### Key artifacts

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master pipeline ordering + invariants | `docs/MASTER_GUIDE_v12.md` | KFM Core | Canonical pipeline + invariants |
| v13 redesign constraints | `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md` | Architecture | “No UI direct-to-graph reads”, “No unsourced narrative”, “Contracts are canonical” |
| Roadmap + directory responsibilities | `docs/architecture/KFM_NEXT_STAGES_BLUEPRINT.md` | Architecture | Confirms `web/` as UI home and MapLibre/Cesium UI scope |
| Governed Markdown template | `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` | Docs/Platform | Template used by this README |
| Story Node template | `docs/templates/TEMPLATE__STORY_NODE_V3.md` | Narrative | Story Node + Focus Mode metadata expectations |
| API contract extension template | `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md` | API | Preferred way to add/extend endpoints |
| UI config schema | `schemas/ui/` | Platform | JSON Schemas for UI registry/config *(not confirmed in repo)* |
| API contracts | `src/server/contracts/` | API | Canonical contract location *(v13 target; not confirmed in repo)* |
| Story Nodes | `docs/reports/story_nodes/` | Narrative | Draft + published narrative artifacts |

### Definition of done

- [ ] Front-matter complete + `path` matches file location
- [ ] UI invariants match the Master Guide / architecture blueprints
- [ ] Directory tree reflects the **actual** `web/src/ui` layout (or is explicitly marked as recommended)
- [ ] Extension checklists are actionable and do not bypass governance/sensitivity review
- [ ] Mermaid diagrams render (no parse errors)
- [ ] Any build/test commands are either repo-accurate or explicitly marked “not confirmed in repo”
- [ ] Governance + CARE/sovereignty considerations explicitly stated (especially for map layers that could reveal sensitive locations)

## 🗂️ Directory Layout

### This document

- `path`: `web/src/ui/README.md` (must match front-matter)

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| UI app | `web/` | React frontend (map + timeline + Focus Mode) |
| UI subsystem | `web/src/ui/` | Reusable UI modules and feature primitives (this area) |
| API boundary | `src/server/` | Canonical API access layer *(v13 target; not confirmed in repo)* |
| API contracts | `src/server/contracts/` | Contract-first API specs *(v13 target; not confirmed in repo)* |
| Graph model + ingest | `src/graph/` | Ontology bindings + graph build/import tooling |
| Pipelines | `src/pipelines/` | ETL and catalog generation code |
| Catalog outputs | `data/stac/` + `data/catalog/dcat/` + `data/prov/` | Evidence + lineage artifacts (outputs) |
| Story Nodes | `docs/reports/story_nodes/` | Draft/published narrative content and assets |
| Schemas | `schemas/` | Schema validation for STAC/DCAT/PROV/storynodes/ui/telemetry |
| Tests | `tests/` | Unit/integration/contract/e2e tests *(split may vary)* |
| MCP | `mcp/` | Model cards, experiments, SOPs (AI work is governed) |

### Expected file tree for this sub-area

> This is the **recommended** structure. Some directories may not exist yet (**not confirmed in repo**).

~~~text
📁 web/
└── 📁 src/
    └── 📁 ui/
        ├── 📄 README.md
        ├── 📁 components/
        │   ├── 📁 map/
        │   │   ├── 📁 layers/
        │   │   ├── 📁 controls/
        │   │   └── 📁 widgets/
        │   ├── 📁 timeline/
        │   ├── 📁 focus_mode/
        │   ├── 📁 story/
        │   ├── 📁 provenance/
        │   └── 📁 common/
        ├── 📁 hooks/
        ├── 📁 state/
        ├── 📁 registry/
        ├── 📁 types/
        ├── 📁 utils/
        └── 📁 assets/
~~~

---

## 🧭 Context

### Canonical placement in the KFM pipeline

KFM’s ordering is intentional and enforced:

**ETL → STAC/DCAT/PROV → Graph → API → UI → Story Nodes → Focus Mode**

This directory participates at the **UI stage** only. UI must not short-circuit earlier stages or fabricate narrative without evidence.

### UI non-negotiables

The UI must enforce the following constraints:

1. **No UI direct-to-graph reads**
   - The frontend must not query Neo4j directly. UI reads only through the API boundary.
2. **No unsourced narrative**
   - Story rendering and Focus Mode must provide citations/provenance links and show warnings when evidence is missing.
3. **Contracts are canonical**
   - UI consumes schemas and API contracts; configuration should validate in CI.
4. **Sensitive content discipline**
   - UI must support redaction/generalization patterns for restricted locations and culturally sensitive knowledge.

### UI responsibilities versus API responsibilities

| Concern | UI responsibility | API responsibility |
|---|---|---|
| Data access | Call contract-defined endpoints only | Enforce auth, redaction/generalization, query limits |
| Narrative rendering | Render Story Nodes and citations; show provenance panel | Serve Story Node content and evidence references safely |
| Layer behavior | Toggle layers; map styling; UX | Serve layer tiles/features and metadata; enforce sensitivity rules |
| Provenance UX | Provide “sources” panel and evidence drilldown | Provide STAC/DCAT/PROV resolvers and stable IDs |
| AI outputs | Display as **opt-in**, clearly labeled, provenance-annotated | Generate/serve AI products only when governed; never infer sensitive locations |

---

## 🗺️ Map and layer system

### Map engines

- Primary: **MapLibre** for 2D mapping.
- Optional/advanced: **Cesium** for 3D globe views (if present in the UI app).

### Layer registry

KFM aims to be **config-driven**: adding a new dataset layer should be mostly a registry + contract exercise, not a UI rewrite.

Recommended characteristics:

- A machine-readable registry of layers (JSON/YAML) under `web/` *(exact path not confirmed in repo)*.
- A JSON Schema under `schemas/ui/` that validates:
  - IDs are stable and namespaced (e.g., `air-quality.aqi`, `treaties.tribal_land`, etc.)
  - Attribution is present
  - Sensitivity classification is present
  - API endpoint references match contract IDs

Example registry entry shape (illustrative only; adjust to actual schema):

~~~json
{
  "id": "example.layer_id",
  "title": "Example Layer",
  "source": {
    "kind": "api",
    "endpoint": "/v1/layers/example/layer_id"
  },
  "render": {
    "type": "vector",
    "minZoom": 4,
    "maxZoom": 12
  },
  "time": {
    "supported": false
  },
  "governance": {
    "sensitivity": "public",
    "requires_review": true,
    "notes": "Set true if interaction/zoom could reveal restricted locations."
  },
  "attribution": "TBD"
}
~~~

### Timeline coupling

If a layer is time-aware, the UI should:

- expose a global time window selector (and/or per-layer time filters),
- keep map + timeline interactions consistent,
- avoid implying precision beyond the evidence resolution (e.g., don’t present daily precision if evidence is monthly).

---

## 🧠 Focus Mode

Focus Mode is the UI feature that synchronizes narrative, map, and timeline into a guided analytic “lens”.

### High-level behavior

When a user enters Focus Mode from a Story Node:

- The UI loads the Story Node content.
- The UI loads a **context bundle** (layers, time window, map center, highlighted entities) from Story Node metadata and/or API response.
- The UI updates:
  - layer toggles,
  - map viewport (center/zoom),
  - timeline window,
  - provenance panel with evidence references.

### Story Node Focus Mode controls

Story Nodes may include Focus Mode hints. Example (illustrative):

~~~yaml
focus_layers:
  - "example.layer_id"
focus_time: "1930-01-01/1939-12-31"
focus_center: [-98.0000, 38.0000]
~~~

UI guidance:

- Treat these fields as **hints**, not commands.
- If a referenced layer is missing, show a warning and degrade gracefully.
- Never fetch data outside what the API contract permits.

### Focus Mode sequence

~~~mermaid
sequenceDiagram
  participant U as User
  participant UI as web/src/ui
  participant API as src/server API
  U->>UI: Select Story Node and enter Focus Mode
  UI->>API: GET Story Node + context bundle
  API-->>UI: Markdown + evidence refs + focus hints
  UI->>UI: Apply focus layers, time window, map center
  UI-->>U: Render story + map + timeline + provenance panel
~~~

### AI content in Focus Mode

If AI-generated explanations or summaries are shown:

- They must be **opt-in**.
- They must be clearly labeled as AI-generated.
- They must include provenance pointers and must not imply that AI created new evidence.
- The UI must not present outputs that would infer or reveal sensitive locations.

---

## 🧾 Story Node rendering and provenance UX

### Rendering expectations

The UI should render Story Node Markdown with support for:

- headings, lists, tables,
- inline citations,
- “sources” or “evidence” sections,
- a provenance panel that can resolve evidence references (STAC/DCAT/PROV IDs).

### Citation and evidence rules

UI should surface warnings if:

- a Story Node lacks evidence references,
- citations reference IDs that do not resolve via API,
- a narrative section makes claims without citations.

Recommended UX:

- Inline citation chips that open a drawer/popup.
- “Sources” sidebar that lists evidence artifacts with stable IDs.
- A “Provenance” tab that shows STAC/DCAT/PROV lineage pointers at a high level.

---

## 🔌 API consumption patterns

### Contract-first consumption

- Prefer a typed API client generated from contracts *(approach and tooling not confirmed in repo)*.
- Avoid hardcoding endpoint strings in UI components; centralize under a small “client” module.

### Error handling

- Distinguish between:
  - “not found” (missing layer/story ID),
  - “forbidden” (redacted/restricted),
  - “contract mismatch” (schema drift),
  - “network/transient”.

### Performance expectations

- Cache layer metadata and story metadata where safe.
- Virtualize large lists (layers, entities, citations).
- Defer expensive rendering in Focus Mode until evidence metadata resolves.

---

## ♿ Accessibility

Minimum expectations:

- Keyboard navigation for map controls, layer toggles, timeline, and Focus Mode drawer panels.
- Visible focus indicators and correct tab order.
- ARIA labels for icon-only controls.
- Avoid color-only encodings for meaning; provide patterns/labels/tooltips.
- Respect reduced-motion preferences for animated transitions.

---

## 🔐 Security, ethics, and sovereignty

UI changes can be governance-impacting. Treat the following as high-risk:

- adding a new layer that can reveal sensitive locations by zoom/interaction,
- changing classification/sensitivity labels,
- adding new imagery/documents without review gates.

Minimum safeguards:

- No secrets in the repo (no API keys, tokens, credentials).
- Prefer generalized/coarse public products when data intersects with sensitive/restricted contexts.
- Ensure AI usage constraints match front-matter permissions/prohibitions.

---

## 🧪 Testing and CI expectations

Recommended test mix (tooling not confirmed in repo):

- Unit tests for utilities/parsers and “pure” components.
- Integration tests for layer registry validation + API client mocks.
- End-to-end tests for Focus Mode flows (enter, apply layers/time, render citations).
- Accessibility checks (static + runtime where possible).

---

## 🧩 Common extension workflows

### Add a new map layer

1. Ensure the dataset exists upstream with evidence artifacts (STAC/DCAT/PROV).
2. Ensure the API boundary exposes a contract-defined endpoint for the layer.
3. Add a registry entry for the layer (and attribution + sensitivity).
4. Validate registry against `schemas/ui/` (CI gate).
5. Add UI toggles and default styling.
6. Add at least one Story Node that references the layer in Focus Mode metadata.
7. Add tests: registry validation + basic render.

### Add a new Focus Mode capability

1. Define behavior in a Story Node contract field (or context bundle schema).
2. Add API response support (contract-first).
3. Implement UI behavior behind a feature flag if risky.
4. Add provenance UX updates (warnings, evidence drilldown).
5. Add accessibility and e2e tests.

---

## 📚 Project reference library

This UI README was informed by the project’s current “reference pack”. These are **inputs** (not necessarily committed to the repo); if stored in-repo, prefer a governed location under `docs/` *(exact placement not confirmed in repo)*.

### Core KFM architecture and planning

- `MASTER_GUIDE_v12.md.pdf`
- `Kansas Frontier Matrix — v13 Redesign Blueprint.pdf`
- `KFM Next Stages Planning.pdf`
- `Kansas Frontier Matrix_ System Structure and Scope.pdf`
- `Kansas Frontier Matrix (KFM) Implementation Guide.pdf`
- `Comprehensive vision draft.pdf`
- `Expanding the Kansas Frontier Matrix Knowledge Base.pdf`
- `Expanding the Kansas Frontier Matrix: External Data, Tools, and Frameworks.pdf`
- `README Information.docx`

### Governed templates and Markdown protocol

- `TEMPLATE__KFM_UNIVERSAL_DOC.md.docx`
- `TEMPLATE__STORY_NODE_V3.md.docx`
- `TEMPLATE__API_CONTRACT_EXTENSION.md.docx`
- `Universal Markdown templates.docx`
- `Comprehensive Guide to Markdown in Programming and Documentation.pdf`

### Web UI, rendering, and visual systems

- `CSS Notes for Professionals - CSSNotesForProfessionals.pdf`
- `KFM-responsive-web-design-with-html5-and-css3.pdf`
- `KFM-webgl-programming-guide-interactive-3d-graphics-programming-with-webgl.pdf`
- `DesigningVirtualWorlds.pdf`
- `KFM- Computer Graphics using JAVA 2D & 3D.pdf`

### Spatial analysis and geospatial tooling references

- `An Introduction to Spatial Data Analysis and Visualisation in R - An Introduction to Spatial Data Analysis in R.pdf`
- `KFM- python-geospatial-analysis-cookbook-over-60-recipes-to-work-with-topology-overlays-indoor-routing-and-web-application-analysis-with-python.pdf`

### Data science, modeling, and uncertainty references

- `Scientific Modeling and Simulation_ A Comprehensive NASA-Grade Guide.pdf`
- `KFM- Bayesian computational methods.pdf`
- `KFM- Understanding Statistics & Experimental Design.pdf`
- `KFM-regression-analysis-with-python.pdf`
- `KFM- Data Science &-  Machine Learning (Mathematical & Statistical Methods).pdf`
- `KFM- Data Mining Concepts & applictions.pdf`
- `KFM- Artificial-neural-networks-an-introduction.pdf`
- `KFM- deep-learning-in-python-prerequisites.pdf`
- `KFM- AI Foundations of Computational Agents 3rd Ed.pdf`
- `KFM- Spectral Geometry of Graphs.pdf`
- `KFM- Scalable Data Management for Future Hardware.pdf`
- `KFM- Generalized Topology Optimization for Structural Design.pdf`

### Data reference documents

- `KFM data Refrences.docx`
- `KFM data References 2.docx`
- `KFM DATA Refrences 3.docx`

---

## 🕰️ Version History

| Version | Date | Summary | Author |
|---:|---:|---|---|
| v1.0.0 | 2025-12-25 | Initial governed UI README for `web/src/ui/` | TBD |

---

## Footer refs

- Master guide: `docs/MASTER_GUIDE_v12.md`
- Redesign blueprint: `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md`
- Next stages blueprint: `docs/architecture/KFM_NEXT_STAGES_BLUEPRINT.md`
- Universal doc template: `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`
- Story Node template: `docs/templates/TEMPLATE__STORY_NODE_V3.md`
- API contract template: `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
