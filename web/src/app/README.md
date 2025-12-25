---
title: "KFM Web UI — web/src/app (Route + Layout Layer) README"
path: "web/src/app/README.md"
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

doc_uuid: "urn:kfm:doc:web:src-app:readme:v1.0.0"
semantic_document_id: "kfm-web-src-app-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:web:src-app:readme:v1.0.0"
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

> **Purpose (required):** Define what belongs in `web/src/app/` (the **route + layout layer** of the KFM web UI), and document the *non-negotiable* rules for how route-level UI code consumes KFM data: **API boundary only**, **provenance-linked narrative only**, and **redaction/sensitivity respected end-to-end**.

# `web/src/app/` — Route + layout layer (UI)

This folder is the **entry layer** for the KFM web UI’s route tree and top-level layouts.

It is where we define:
- what pages exist (route segments),
- how global layout/providers are wired,
- how errors/not-found states are surfaced,
- and how route-level components request data **through the API boundary** (never directly from the graph).

> If your routing framework differs (not confirmed in repo), keep this README but update the “Expected file tree” and route conventions accordingly.

---

## 📘 Overview

### Purpose
- Provide a **governed contract** for what belongs in `web/src/app/`.
- Keep route-level UI aligned with KFM’s canonical pipeline:
  **ETL → STAC/DCAT/PROV → Graph → API → UI → Story Nodes → Focus Mode**.
- Prevent architectural drift by enforcing:
  - **no UI direct-to-graph reads**, and
  - **Focus Mode / narrative views only surface provenance-linked claims**.

### Scope

| In scope | Out of scope |
|---|---|
| Route tree, layout shells, route-level loading/error boundaries, route-level data-fetch patterns | Implementing the API itself (belongs in `src/server/`), graph logic (belongs in `src/graph/`), or ETL/catalog output generation (belongs in `src/pipelines/` + `data/**`) |
| Where to add new UI routes for map, timeline, Story Nodes, and Focus Mode | Pixel-level design system details (belongs under UI/design docs if present) |
| Rules for displaying provenance, citations, and redaction notices in route-level pages | Governance policy authoring (belongs in governed governance docs) |

### Audience
- **Primary:** Frontend maintainers and contributors working under `web/`.
- **Secondary:** API maintainers and narrative curators who need to know how the UI consumes contracts and story artifacts.

### Definitions (link to glossary)
- Glossary: `docs/glossary.md` *(not confirmed in repo — update if the glossary lives elsewhere)*

Terms used here:
- **API boundary:** The contracted REST/GraphQL layer that mediates all graph/catalog access for clients.
- **Story Node:** A governed narrative artifact (markdown + metadata) that links every claim to evidence.
- **Focus Mode:** A UI view that renders a story/analysis with map/timeline context and requires provenance-linked content.
- **Layer registry:** The UI’s schema-validated list of map layers/toggles/legends used by the map client.

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master pipeline ordering + invariants | `docs/MASTER_GUIDE_v12.md` | KFM Core | Canonical pipeline + extension matrix |
| v13 redesign blueprint (if adopted) | `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md` | Architecture | Canonical roots + minimum contract set |
| Web UI root | `web/` | Frontend | React/MapLibre/Cesium UI surface |
| UI layer registry instances | `web/**/layers/**` | Frontend | Layer registries must validate against `schemas/ui/` |
| UI registry schemas | `schemas/ui/**` | Platform | Schema contract for layers/legends/toggles |
| API boundary | `src/server/**` | API | UI consumes contracts only |
| API contracts | `src/server/contracts/**` | API | UI should treat these as source-of-truth payload definitions |
| Story Nodes | `docs/reports/story_nodes/**` | Narrative | Focus Mode consumes governed story artifacts |
| Story Node template | `docs/templates/TEMPLATE__STORY_NODE_V3.md` | Narrative | Standard structure for provenance-linked narratives |
| Universal doc template | `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` | Docs | Governed Markdown requirements (this README follows it) |

### Definition of done (for this document)
- [ ] Front-matter complete and `path` matches `web/src/app/README.md`
- [ ] States the UI invariants clearly:
  - [ ] UI never reads Neo4j directly
  - [ ] Focus Mode surfaces provenance-linked content only
  - [ ] AI-generated/predictive content (if any) is opt-in and labeled
- [ ] Directory responsibilities + placement rules are explicit
- [ ] “Add a route” pattern is described and repeatable
- [ ] Mentions layer registry + schema validation expectations
- [ ] Governance/sensitivity constraints are stated for UI interactions (zoom/filter/export)
- [ ] Version history updated for changes

---

## 🗂️ Directory Layout

### This document
- `path`: `web/src/app/README.md` (must match front-matter)

### Related repository paths (orientation)

| Area | Path | What lives here |
|---|---|---|
| UI root | `web/` | Front-end application code (map + narrative UI) |
| Layer registry | `web/**/layers/**` | Schema-valid layer toggles/legends/metadata used by the map |
| UI schemas | `schemas/ui/**` | JSON Schemas for UI registries |
| API boundary | `src/server/**` | Contracted access layer; redaction/generalization enforced here |
| API contracts | `src/server/contracts/**` | OpenAPI/GraphQL schemas/contracts |
| Graph | `src/graph/**` + `data/graph/**` | Ontology + ingest fixtures (clients must not connect directly) |
| Catalog outputs | `data/stac/**` + `data/catalog/dcat/**` + `data/prov/**` | Evidence + discovery + lineage |
| Story Nodes | `docs/reports/story_nodes/**` | Governed narrative artifacts consumed by Focus Mode |

### Expected file tree for this sub-area

> This is the **recommended** structure for an “app router” style UI. Some filenames/routes may differ (**not confirmed in repo**). Keep this README synchronized with the actual files present.

~~~text
📁 web/
└── 📁 src/
    └── 📁 app/
        ├── 📄 README.md
        ├── 📄 layout.<ext>                  # global app shell + providers (not confirmed in repo)
        ├── 📄 page.<ext>                    # root route entry (not confirmed in repo)
        ├── 📄 error.<ext>                   # route error boundary (not confirmed in repo)
        ├── 📄 not-found.<ext>               # 404 boundary (not confirmed in repo)
        ├── 📄 globals.<ext>                 # global styles (not confirmed in repo)
        │
        ├── 📁 (routes)/                     # optional route groups (not confirmed in repo)
        │   ├── 📁 <map-or-explore>/          # map/timeline exploration pages
        │   ├── 📁 <stories>/                 # Story Node index + browsing
        │   └── 📁 <focus>/                   # Focus Mode route(s)
        │
        ├── 📁 _components/                  # route-local components (optional; not confirmed in repo)
        └── 📁 _lib/                         # route-local helpers (optional; not confirmed in repo)
~~~

---

## 🧭 Context

### How this fits the canonical pipeline
KFM’s UI layer is **downstream** of the API boundary:

- Upstream evidence + lineage is produced as **STAC/DCAT/PROV**.
- The graph references those identifiers and is accessed through the **API boundary**.
- The UI consumes:
  - contracted API responses, and
  - catalog endpoints (as published),
  and renders them as map layers, timelines, and narrative views.

### Constraints / invariants (non-negotiables)
- **No UI direct-to-graph reads.**
  - Do not import Neo4j drivers in the UI.
  - Do not embed Cypher or graph credentials in `web/`.
- **API boundary is mandatory.**
  - Route-level UI code calls **only** API endpoints (and/or catalog endpoints), never the database.
- **Focus Mode is provenance-linked only.**
  - If a story element cannot provide evidence identifiers, it must not render as fact.
- **AI-generated or predictive content (if present)**
  - is **opt-in**,
  - shows uncertainty metadata,
  - and must never appear as unmarked fact.

### Practical placement rule
Keep `web/src/app/` **thin**:
- Routes/layouts compose screens from UI components that live elsewhere in the UI codebase (e.g., `web/src/components/**` or `web/src/features/**` — not confirmed in repo).
- Data shaping rules belong at the API boundary; UI should not “reconstruct” redacted fields.

---

## 🗺️ Diagrams

### System boundary (UI perspective)

~~~mermaid
flowchart TB
  subgraph UI["UI (web)"]
    A["Routes + Layout (web/src/app)"]
    L["Layer registry (web/**/layers/**)"]
    S["Story views (Story Nodes + Focus Mode)"]
  end

  subgraph API["API Boundary (src/server)"]
    C["Contracts (src/server/contracts)"]
    E["Endpoints (REST/GraphQL)"]
    R["Redaction / generalization enforcement"]
  end

  subgraph Graph["Graph + Evidence"]
    G["Neo4j graph (src/graph + loader)"]
    P["STAC/DCAT/PROV (data/stac + data/catalog/dcat + data/prov)"]
  end

  A --> E
  A --> L
  A --> S
  E --> R
  E --> G
  E --> P
  C --> E
~~~

---

## 🧠 Story Node & Focus Mode Integration

### What Focus Mode must guarantee
- Every factual claim displayed in Focus Mode must be traceable to evidence identifiers (dataset/document IDs).
- The UI must be able to present evidence context (e.g., citations, source popovers, “view dataset” links) rather than hiding it.

### Recommended rendering contract (UI-side)
When rendering a Story Node (or a Focus Mode view derived from one), ensure the UI can display:
- **Graph entity references** (canonical IDs; resolved via API),
- **Evidence identifiers**:
  - STAC Item/Collection IDs,
  - DCAT dataset IDs,
  - PROV activity IDs,
- **Attribution/licensing** for any local assets.

> If the Story Node includes optional Focus Mode controls (e.g., “focus layers” or “focus time”), treat them as *inputs* to the UI view — never as evidence by themselves.

### Sensitivity handling
If a Story Node or a layer touches sensitive/restricted locations:
- Prefer generalized geometry or coarse regions (enforced at the API boundary).
- The UI must not “undo” redaction by recombining fields, correlating overlays, or encouraging precision zoom.
- Show a clear **redaction/generalization notice** when the API indicates redaction was applied.

---

## 🧪 Validation & CI/CD

### Validation expectations (recommended)
Even if the exact CI workflow names differ (not confirmed in repo), route-level UI changes should pass:
- Typecheck + lint (TS/JS)
- UI layer registry schema validation against `schemas/ui/**`
- Accessibility checks (keyboard navigation, focus order, semantic headings, contrast)
- “Forbidden dependency” checks to prevent Neo4j direct access strings/imports in `web/`
- Secrets/PII scanning (no tokens, no credentials, no sensitive data embedded)

### Reproduction (placeholders)
~~~bash
# Example placeholders — replace with repo-specific commands (not confirmed in repo)

# UI checks
# <package-manager> lint
# <package-manager> typecheck
# <package-manager> test

# Schema validation (UI registries)
# <validator> schemas/ui/** web/**/layers/**

# Security regression check: ensure no Neo4j client usage in web/
# <grep-tool> "neo4j://" web/
~~~

---

## 📦 Data & Metadata

### What the route layer consumes
Route-level UI code should consume:
- **API responses** (contracted payloads),
- **catalog endpoints** (STAC/DCAT/PROV, as published),
- **Story Nodes** (via API or a governed content pipeline — implementation detail not specified here).

### What the route layer must not consume
- Neo4j directly
- raw/work/processed datasets from `data/**` via filesystem shortcuts
- unvetted narrative text without evidence identifiers

---

## 🌐 STAC, DCAT & PROV Alignment

When the UI displays:
- a dataset layer,
- an evidence panel,
- or a story claim,

it should be possible (through the UI) to trace to:
- a STAC Item/Collection,
- a DCAT dataset record (if applicable),
- and a PROV activity describing lineage.

This is the UI-facing expression of the “provenance-linked narrative rule”:
**no orphan facts, and no orphan datasets.**

---

## 🧱 Architecture

### Route responsibilities
`web/src/app/` should primarily contain:
- route folders/files,
- layout + provider wiring,
- error/not-found boundaries,
- and minimal route-level composition.

Move reusable logic into:
- components, features, and services under `web/src/**` (exact paths not confirmed in repo).

### Data access pattern (required)
Routes and route-composed screens:
1) call a typed API client / fetch wrapper (implementation-specific),
2) receive contract-shaped payloads,
3) render UI with provenance and redaction indicators.

They must not:
- query the graph directly,
- “join” graph + catalog payloads in an unreviewed manner,
- bypass classification or redaction flags.

---

## ⚖ FAIR+CARE & Governance

### Review gates (UI)
Governance review is required when UI changes:
- could expand access to sensitive/restricted location detail,
- add export/download affordances for potentially sensitive layers,
- change how provenance/citations are displayed (or remove them),
- introduce AI-generated narrative text into user-visible surfaces.

### CARE / sovereignty considerations
- Treat culturally sensitive locations as **high-risk** by default.
- Ensure any interaction patterns (filters, clustering, zoom thresholds, tooltips) do not undermine generalization/redaction.

### AI usage constraints
- Allowed: UI summarization / formatting / accessibility adaptations.
- Prohibited: presenting generated content as fact, inferring sensitive locations, or “policy override” behaviors.

---

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---:|---|---|
| v1.0.0 | 2025-12-25 | Initial `web/src/app/` README establishing route-layer responsibilities and invariants | (you) |

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
