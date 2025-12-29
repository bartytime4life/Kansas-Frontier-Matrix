---
title: "KFM UI Subsystem README"
path: "web/src/ui/README.md"
version: "v1.1.0"
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

doc_uuid: "urn:kfm:doc:web:src:ui:readme:v1.1.0"
semantic_document_id: "kfm-web-src-ui-readme-v1.1.0"
event_source_id: "ledger:kfm:doc:web:src:ui:readme:v1.1.0"
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

This directory is the **UI subsystem surface area** for KFM’s `web/` frontend: reusable UI primitives for **map + timeline + Focus Mode + Story Node rendering**.

This README is **governed**: it encodes constraints from the Master Guide and v13 redesign documents (API boundary, provenance-first narrative, contract-driven configuration). If you change behavior that affects what the user can see (layers, narrative, evidence, classification), treat it as governance-impacting.

> Note: Folder names in this README include a recommended “target” layout. If the current repo layout differs, update this file so documentation matches reality.

## 📘 Overview

### Purpose

- Define what belongs in `web/src/ui/` (and what does not).
- Document the **hard UI invariants**:
  - **API-only data access** (no direct Neo4j/graph reads from the browser).
  - **Evidence-first narrative** (no uncited Story Node / Focus Mode claims).
  - **No hidden data leakage** (redaction/generalization must remain respected at all zoom levels and UI affordances).
- Provide contributor checklists for safely extending map layers, Focus Mode UX, and narrative + provenance rendering.

### Scope

| In Scope | Out of Scope |
|---|---|
| UI components, hooks, state, and utilities used by the KFM React app | ETL implementations, graph migrations, and server-side authorization |
| Map + timeline + Focus Mode UI contracts and patterns | Direct Neo4j access from frontend code |
| Story Node rendering UX and citation/provenance panels | Authoring new governance policy (belongs under `docs/governance/`) |
| Layer registry patterns (config-driven UI) | Storing authoritative data outputs under `web/` or `src/` |

### Audience

- Primary: Frontend contributors implementing map/timeline/Focus Mode UX.
- Secondary: API and data contributors who need to understand how UI consumes contracts and evidence.

### Definitions (link to glossary)

- Link: `docs/glossary.md` *(expected in v13 redesign blueprint; presence not confirmed here)*
- Terms used in this doc include: **API boundary**, **Focus Mode**, **Story Node**, **layer registry**, **provenance panel**, **redaction**, **generalization**, **STAC**, **DCAT**, **PROV**, **stable identifier**, **classification/sensitivity**.

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master pipeline ordering + invariants | `docs/MASTER_GUIDE_v12.md` | KFM Core | Canonical pipeline + invariants |
| v13 redesign constraints | `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md` | Architecture | Canonical subsystem homes + stage mapping |
| Markdown work protocol | `docs/standards/KFM_MARKDOWN_WORK_PROTOCOL.md` *(see repo standards; path may vary)* | Platform | Markdown protocol + doc validation expectations |
| Governed doc template | `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` | Docs/Platform | Template used by this README |
| Story Node template | `docs/templates/TEMPLATE__STORY_NODE_V3.md` | Narrative | Story Node metadata + citation expectations |
| API contract extension template | `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md` | API | Preferred way to add/extend endpoints |
| API boundary home | `src/server/` | API | API boundary is server-only; UI is a client of it |
| API contracts | `src/server/contracts/**` *(if present)* | API | Contract-first specs + tests |
| Focus Mode module README | `web/src/story/focus_mode/README.md` *(if present)* | UI + Narrative | Deeper Focus Mode UX and Story Node binding |
| UI layer registry | `web/**/layers/**` *(v13 target pattern)* | UI | Config-driven layers; schema-validated |
| Schemas | `schemas/` | Platform | Schema validation for STAC/DCAT/PROV/storynodes/ui/telemetry *(subtrees may vary)* |
| Story Nodes | `docs/reports/story_nodes/` | Narrative | Draft + published narrative artifacts |

### Definition of done (for this document)

- [ ] Front-matter complete + `path` matches file location
- [ ] UI invariants match the Master Guide / v13 redesign blueprint
- [ ] Directory tree reflects the **actual** `web/src/ui` layout (or is explicitly marked as recommended)
- [ ] Extension checklists are actionable and do not bypass governance/sensitivity review
- [ ] Mermaid diagrams render (no parse errors)
- [ ] Any build/test commands are repo-accurate or explicitly marked “not confirmed in repo”
- [ ] Governance + CARE/sovereignty considerations explicitly stated (especially for map layers that could reveal sensitive locations)

---

## 🗂️ Directory Layout

### This document

- `path`: `web/src/ui/README.md` (must match front-matter)

### Related repository paths (canonical homes)

| Area | Path | What lives here |
|---|---|---|
| UI app | `web/` | React frontend (map + timeline + Focus Mode) |
| UI subsystem | `web/src/ui/` | Reusable UI modules and feature primitives (this area) |
| API boundary | `src/server/` | Canonical API access layer; mediates graph/data access |
| Graph model + ingest | `src/graph/` | Ontology bindings + graph build/import tooling |
| Pipelines | `src/pipelines/` | ETL and catalog generation code |
| Catalog outputs | `data/stac/` + `data/catalog/dcat/` + `data/prov/` | Evidence + lineage artifacts (outputs) |
| Story Nodes | `docs/reports/story_nodes/` | Draft/published narrative content and assets |
| Schemas | `schemas/` | Schema validation for STAC/DCAT/PROV/storynodes/ui/telemetry |
| MCP runs/experiments | `mcp/` | Model cards, runs, experiments, SOPs (AI work is governed) |

### Expected file tree for this sub-area

> This is the **recommended** structure. Some directories may not exist yet.

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

### Background

KFM’s v12/v13 direction is to keep **one canonical home per subsystem** and to preserve the end-to-end ordering that makes provenance and sovereignty enforceable.

For the UI specifically, the goal is to:

- keep the browser as a **presentation layer** (not a data authority),
- ensure Story Nodes and Focus Mode remain **evidence-driven**,
- make it easy to add new layers/features via **registries + contracts** rather than ad-hoc UI code paths.

### Assumptions

- Frontend is a React map/narrative client under `web/`.
- Primary 2D map engine is MapLibre; Cesium may be present as an advanced option.
- The server (`src/server/`) is the only supported path to the graph and catalog resolvers.
- Story Nodes exist as governed artifacts under `docs/reports/story_nodes/`.

### Constraints / invariants

KFM’s ordering is intentional and enforced:

**ETL → STAC/DCAT/PROV catalogs → Neo4j graph → APIs → React/Map UI → Story Nodes → Focus Mode**

UI constraints (“hard gates” for PR review):

1. **No UI direct-to-graph reads**
   - The frontend must not query Neo4j directly.
   - The frontend must not read from `data/**` outputs as an “API substitute”.
2. **No ad-hoc / hidden data**
   - If a UX requires new fields or aggregations, extend **API contracts** and server logic instead of hardcoding special cases in UI.
3. **No unsourced narrative**
   - Story rendering and Focus Mode must provide citations/provenance links and show warnings when evidence is missing.
4. **Contracts are canonical**
   - UI consumes schemas and API contracts; configuration should validate in CI.
5. **No hidden data leakage**
   - When data is restricted or generalized upstream, UI must not expose it via tooltips, hover cards, exports, deep links, URL params, or high zoom styling.
6. **Sensitive content discipline**
   - UI must support redaction/generalization patterns for restricted locations and culturally sensitive knowledge.

#### UI responsibilities versus API responsibilities

| Concern | UI responsibility | API responsibility |
|---|---|---|
| Data access | Call contract-defined endpoints only | Enforce auth, redaction/generalization, query limits |
| Narrative rendering | Render Story Nodes and citations; show provenance panel | Serve Story Node content + evidence references safely |
| Layer behavior | Toggle layers; map styling; UX | Serve layer tiles/features + metadata; enforce sensitivity rules |
| Provenance UX | Provide “Sources” panel + evidence drilldown | Provide resolvers for STAC/DCAT/PROV IDs + stable IDs |
| AI outputs | Display as **opt-in**, clearly labeled | Generate/serve AI products only when governed; never infer sensitive locations |

### Open questions

| Question | Owner | Target date |
|---|---|---|
| Where are the exact layer registry file(s) in this repo (within `web/**/layers/**`) and what schema validates them? | UI maintainers | Next UI PR |
| Do we generate a typed API client from OpenAPI/GraphQL, or hand-maintain a client module? | UI + API | Next UI/API contract PR |
| Where are telemetry schemas recorded (`schemas/telemetry/**` and/or `docs/telemetry/**`)? | Platform | Next telemetry PR |

### Future extensions

- **Typed client generation** from contract definitions (OpenAPI/GraphQL) to reduce drift.
- **Evidence viewer UX**: richer “Sources” panel that can preview STAC assets and PROV lineage.
- **Layer “safety modes”**: per-layer interaction caps (max zoom, export disabled) when sensitivity requires.
- **Focus Mode audit strip**: visible “what changed” indicator (layers/time/redactions applied) for transparency.

---

## 🗺️ Diagrams

### System / dataflow diagram

~~~mermaid
flowchart LR
  A[ETL] --> B[STAC/DCAT/PROV Catalogs]
  B --> C[Neo4j Graph]
  C --> D[APIs]
  D --> E[React/Map UI]
  E --> F[Story Nodes]
  F --> G[Focus Mode]
~~~

### Optional: sequence diagram (Focus Mode entry)

~~~mermaid
sequenceDiagram
  participant U as User
  participant UI as web/src/ui
  participant API as src/server API
  U->>UI: Select Story Node and enter Focus Mode
  UI->>API: GET Story Node + context bundle
  API-->>UI: Markdown + evidence refs + focus hints + redaction notices
  UI->>UI: Apply focus layers/time/viewport (degrade gracefully if missing)
  UI-->>U: Render story + map + timeline + provenance panel
~~~

---

## 🗺️ Map and layer system

### Map engines

- Primary: **MapLibre** for 2D mapping.
- Optional/advanced: **Cesium** for 3D globe views *(if present in the UI app)*.

### Layer registry

KFM aims to be **config-driven**: adding a new dataset layer should be mostly a registry + contract exercise, not a UI rewrite.

Recommended characteristics:

- A machine-readable registry of layers under `web/**/layers/**` *(v13 target pattern)*.
- A JSON Schema (expected under `schemas/`) that validates:
  - IDs are stable and namespaced (e.g., `air_quality.aqi`, `treaties.tribal_land`, etc.)
  - Attribution is present
  - Sensitivity/classification is present and cannot be silently downgraded
  - API endpoint references match contract IDs (or OpenAPI operation IDs)
  - Evidence pointers exist (DCAT dataset ID and/or STAC collection/item IDs)

Example registry entry shape (illustrative; align to actual schema):

~~~json
{
  "id": "example.layer_id",
  "title": "Example Layer",
  "source": {
    "kind": "api",
    "contract_id": "layers.getExampleLayer",
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
  "evidence": {
    "dcat_dataset_id": "dcat:Example:Dataset",
    "stac_collection_id": "stac:example-collection",
    "prov_activity_id": "prov:run:example"
  },
  "governance": {
    "sensitivity": "public",
    "classification": "open",
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

### Hard rule

- **Focus Mode only consumes provenance-linked content.**
- Any predictive/suggestive/AI content must be:
  - opt-in,
  - uncertainty-annotated,
  - never presented as “fact”,
  - never used to infer or reveal sensitive locations.

### High-level behavior

When a user enters Focus Mode from a Story Node:

- The UI loads the Story Node content.
- The UI loads a **provenance-linked context bundle** (layers, time window, map center, highlighted entities, evidence references).
- The UI updates:
  - layer toggles,
  - map viewport (center/zoom),
  - timeline window,
  - provenance panel with evidence references (STAC/DCAT/PROV IDs).

### Context bundle expectations (illustrative)

Treat these fields as **hints**, not commands:

~~~yaml
story_node_id: "kfm-story:example"
focus_layers:
  - "example.layer_id"
focus_time: "1930-01-01/1939-12-31"
focus_center: [-98.0000, 38.0000]
highlighted_entities:
  - "kfm:Place:example"
evidence_refs:
  - "stac:item:example"
  - "dcat:dataset:example"
  - "prov:activity:example"
redaction_notices:
  - "This view includes generalized geometries for sovereignty safety."
~~~

UI guidance:

- If a referenced layer is missing, show a warning and degrade gracefully.
- If evidence refs do not resolve via API, show an evidence warning and degrade gracefully.
- Never fetch data outside what the API contract permits.

### AI content in Focus Mode

If AI-generated explanations or summaries are shown:

- they must be **opt-in**,
- they must be clearly labeled as AI-generated,
- they must include provenance pointers and must not imply AI created new evidence,
- they must not infer or reveal sensitive locations.

---

## 🧾 Story Node rendering and provenance UX

### Rendering expectations

The UI should render Story Node Markdown with support for:

- headings, lists, tables,
- inline citations,
- “sources” or “evidence” sections,
- a provenance panel that can resolve evidence references (STAC/DCAT/PROV IDs).

### Fact / inference / hypothesis display discipline

When Story Nodes contain interpretation:

- render it with explicit labeling (fact vs inference vs hypothesis),
- keep citations visible,
- avoid UI copy that makes inference sound like verified fact.

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

- Prefer a typed API client generated from contracts *(tooling may vary)*.
- Avoid hardcoding endpoint strings in UI components; centralize under a small “client” module.
- If API shape changes, update the contract first (and bump version / deprecate as required).

### Error handling (user-visible)

Distinguish between:

- **404 Not Found**: missing layer/story ID,
- **403 Forbidden / Redacted**: restricted content (show a redaction notice, not a generic error),
- **Contract mismatch**: schema drift (show “client/server version mismatch”),
- **Network/transient**: retry affordance.

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

## 🧪 Testing and CI expectations

### Minimum CI gates (v12-ready)

These checks are expected at the repo level; UI work should not bypass them:

- Markdown protocol validation (front-matter + required sections)
- Link/reference checks (no orphan pointers)
- JSON schema validation:
  - STAC/DCAT/PROV
  - Story Node schemas *(if present)*
  - UI layer registry schemas *(if present)*
  - Telemetry schemas *(if present)*
- API contract tests (OpenAPI/GraphQL schema + resolver/integration tests)
- Security + sovereignty scanning gates (as applicable):
  - secret scan
  - PII scan
  - sensitive-location leakage checks
  - classification propagation checks (no downgrades without review)

### Telemetry signals (recommended)

These signals are recommended for auditability and “no hidden leakage” verification (storage path may vary):

- `classification_assigned` (dataset_id, sensitivity, classification)
- `redaction_applied` (method, fields_removed, geometry_generalization)
- `focus_mode_redaction_notice_shown` (layer_id, redaction_method)

### UI test mix (recommended)

- Unit tests for utilities/parsers and “pure” components.
- Integration tests for layer registry validation + API client mocks.
- End-to-end tests for Focus Mode flows (enter, apply layers/time, render citations).
- Accessibility checks (static + runtime where possible).

---

## ⚖ FAIR+CARE & Governance

### Governance review triggers

Treat these as governance-impacting and require review:

- New sensitive layers or any content intersecting sovereignty obligations
- New AI narrative behaviors or automated summarization that could be interpreted as “fact”
- New external data sources (license/provenance review)
- New public-facing endpoints or layer interactions that could reveal sensitive locations
- Any classification/sensitivity change or publication derived from restricted inputs

### Sovereignty safety (end-to-end enforcement)

Redaction/generalization must be documented and enforced:

- in datasets (`data/processed/**`),
- in catalogs (STAC/DCAT),
- in API responses (redaction policies),
- and in UI rendering (CARE gating + no hidden leakage).

### AI usage constraints

Ensure this doc’s AI permissions/prohibitions match intended UI behavior:

- Allowed transforms: summarize/structure_extract/translate/keyword_index
- Prohibited: generate_policy, infer_sensitive_locations

---

## 🧩 Common extension workflows

### Add a new map layer

1. Ensure the dataset exists upstream with evidence artifacts (STAC/DCAT/PROV).
2. Ensure the API boundary exposes a contract-defined endpoint for the layer.
3. Add a registry entry for the layer (including attribution + sensitivity/classification + evidence refs).
4. Validate registry against the UI schema (CI gate).
5. Add UI toggles and default styling (avoid leaking restricted detail).
6. Add at least one Story Node that references the layer in Focus Mode metadata.
7. Add tests: registry validation + basic render + redaction notice behavior.

### Add a new Focus Mode capability

1. Define behavior in the Story Node schema and/or context bundle contract (contract-first).
2. Add API response support (versioned; backward compatible where possible).
3. Implement UI behavior behind a feature flag if risky.
4. Add provenance UX updates (warnings, evidence drilldown, redaction notices).
5. Add accessibility and e2e tests.

### Add a new provenance UX element

1. Define the evidence reference shape (IDs + resolver endpoint).
2. Implement UI rendering with stable links to evidence IDs.
3. Add a failure mode UI (unresolved ID → warning, not silent omission).
4. Add tests for rendering and unresolved evidence behavior.

---

## 📚 Project reference library

This UI README aligns to the Master Guide and v13 redesign blueprint. The project also maintains a broader “reference pack” (books/papers) used for implementation context. If these sources are committed, prefer a governed location under `docs/` (e.g., `docs/reference/`) and link from the Master Guide *(path not confirmed in repo)*.

### Core KFM architecture and planning (canonical docs)

- `docs/MASTER_GUIDE_v12.md`
- `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md`
- `docs/standards/KFM_MARKDOWN_WORK_PROTOCOL.md`
- `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`
- `docs/templates/TEMPLATE__STORY_NODE_V3.md`
- `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md`

### Reference pack (external inputs; filenames may vary)

- `Kansas Frontier Matrix_ System Structure and Scope.pdf`
- `Kansas Frontier Matrix (KFM) Implementation Guide.pdf`
- `Kansas Frontier Matrix — v13 Redesign Blueprint.pdf`
- `Kansas Frontier Matrix – Architecture & Design Audit (v12_v13).pdf`
- `Expanding the Kansas Frontier Matrix Knowledge Base.pdf`
- `Expanding the Kansas Frontier Matrix: External Data, Tools, and Frameworks.pdf`
- `Comprehensive Guide to Markdown in Programming and Documentation.pdf`
- `CSS Notes for Professionals - CSSNotesForProfessionals.pdf`

---

## 🕰️ Version History

| Version | Date | Summary | Author |
|---:|---:|---|---|
| v1.0.0 | 2025-12-25 | Initial governed UI README for `web/src/ui/` | TBD |
| v1.1.0 | 2025-12-28 | Align to Master Guide v12 + v13 blueprint: canonical homes, Focus Mode hard gates, CI gates, governance review triggers | TBD |

---

Footer refs:

- Master guide: `docs/MASTER_GUIDE_v12.md`
- Redesign blueprint: `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md`
- Markdown work protocol: `docs/standards/KFM_MARKDOWN_WORK_PROTOCOL.md`
- Universal doc template: `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`
- Story Node template: `docs/templates/TEMPLATE__STORY_NODE_V3.md`
- API contract template: `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`