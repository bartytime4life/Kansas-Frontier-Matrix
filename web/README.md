---
title: "KFM Web UI (web/)"
path: "web/README.md"
version: "v0.1.0-draft"
last_updated: "2025-12-31"
status: "draft"
doc_kind: "component_readme"
license: "TBD (inherit repo root LICENSE)"
markdown_protocol_version: "KFM-MDP v11.2.6"

# Contract + profile alignment (fill from canonical standards/templates)
mcp_version: "TBD"
ontology_protocol_version: "TBD"
pipeline_contract_version: "TBD"
stac_profile_version: "TBD"
dcat_profile_version: "TBD"
prov_profile_version: "TBD"

governance_ref: "docs/governance/ROOT_GOVERNANCE.md"
ethics_ref: "docs/governance/ETHICS.md"
sovereignty_policy: "docs/governance/SOVEREIGNTY.md"

fair_category: "FAIR+CARE"
care_label: "Public · Low-Risk (TBD)"
sensitivity: "low"
classification: "public"
jurisdiction: "US-KS"

doc_uuid: "TBD"
semantic_document_id: "kfm:web:readme"
event_source_id: "TBD"
commit_sha: "TBD"
doc_integrity_checksum: "TBD"

ai_assistance:
  used: true
  tool: "ChatGPT (GPT-5.2 Pro)"
  notes: "Drafted from KFM project docs; requires human review before merge."
---

# 🌐 KFM Web UI

The `web/` directory contains the **user-facing frontend** for Kansas Frontier Matrix (KFM): an interactive, map-based narrative interface (React + MapLibre) that consumes governed APIs and presents Story Nodes and Focus Mode experiences.

> **Non-negotiable invariant:** the UI is *downstream* of ETL → Catalogs → Graph → API.  
> The UI must never bypass contracts by reading the graph or raw data directly.

---

## 📘 Overview

### Purpose
Provide a modern, map-first web interface that:
- Renders KFM geospatial layers (MapLibre GL) with time filtering (timeline slider).
- Displays Story Nodes (governed narrative Markdown) with citations.
- Provides **Focus Mode**: an evidence-only “truth audit” view that shows only provenance-linked content.

### Scope
In scope:
- Web app code, UI state, map configuration, rendering Story Nodes and citations, Focus Mode UX.
- Consuming API endpoints and honoring API schema + classification/redaction fields.

Out of scope:
- ETL pipelines, metadata catalog generation, graph construction, and API implementation.

### Audience
- Frontend engineers, UI/UX contributors, and reviewers validating “evidence-first” UI behavior.
- Backend/API contributors who need to understand UI expectations at the contract boundary.

---

## 🗂️ Directory Layout

### This document
- 📄 `web/README.md` (this file)

### Repo context (expected top-levels)
> This is the **v13 “one canonical home per subsystem”** layout (trimmed to what matters for UI work).

~~~text
📁 data/
├── 📁 raw/                      # Immutable originals (by domain)
├── 📁 work/                     # Intermediates
├── 📁 processed/                # Published/derived outputs
├── 📁 stac/                     # STAC collections/items
├── 📁 catalog/
│   └── 📁 dcat/                 # DCAT metadata
└── 📁 prov/                     # PROV lineage bundles

📁 docs/
├── 📄 MASTER_GUIDE_v13.md
├── 📁 standards/
├── 📁 templates/
└── 📁 reports/
    └── 📁 story_nodes/          # Story Node content (draft/published)

📁 schemas/                      # JSON Schemas (STAC/DCAT/PROV/storynodes/ui/telemetry)
📁 src/
├── 📁 pipelines/                # ETL jobs
├── 📁 graph/                    # Graph build code
└── 📁 server/                   # API implementation + contracts (OpenAPI/GraphQL)

📁 web/                          # ✅ Frontend UI (you are here)
~~~

### `web/` internal layout (project-specific)
The exact file tree under `web/` depends on whether the repo stores:
1) **built static site assets** (e.g., `index.html`, bundled JS/CSS), or  
2) **source + bundler** (React/TypeScript + `package.json`), or both.

If your repo is using a typical SPA + bundler pattern, an **expected** (but **not confirmed in repo**) layout is:

~~~text
📁 web/
├── 📄 README.md
├── 📄 index.html                 # SPA entrypoint (if static build output lives here)
├── 📁 public/                    # Static assets (favicons, images)
├── 📁 src/                       # React/TS source
│   ├── 📁 components/
│   ├── 📁 features/
│   │   ├── 📁 map/
│   │   ├── 📁 story/
│   │   └── 📁 focus_mode/
│   ├── 📁 styles/
│   ├── 📁 lib/
│   └── 📄 main.tsx
├── 📄 package.json               # Node toolchain (if applicable)
└── 📄 (build config files)       # e.g., vite/webpack configs (if applicable)
~~~

If instead `web/` is deployed as a **pure static folder** (e.g., GitHub Pages builds from `web/`), then the key expectation is:
- `web/` contains **only UI assets** (or build outputs),
- it does **not** become a “hidden data storage” location.

---

## 🧭 Context

### Where `web/` fits in the canonical pipeline
KFM’s pipeline ordering is strict:

ETL → STAC/DCAT/PROV catalogs → Neo4j graph → APIs → UI → Story Nodes → Focus Mode

`web/` is the **UI** stage. It must never:
- read Neo4j directly,
- read raw/processed data files directly,
- “smuggle” uncataloged evidence into the interface.

### API boundary rule (hard requirement)
The frontend is contract-driven:
- The API is the sole integration boundary for KFM data access.
- UI features must be implementable using API responses + their governed schemas.

### Evidence-first UI behavior
UI behaviors must reinforce provenance:
- Citations are visible and actionable (clickable markers, evidence popovers/panels).
- Focus Mode is an evidence-only view:
  - Anything not linked to a source is hidden or flagged.
  - Missing citations are surfaced as a quality control signal (and should be caught by CI earlier).

### Stateless frontend principle
The UI should not maintain its own persistent database.  
Caching is allowed for performance, but the API remains the source of truth.

### Sensitive / sovereign data handling
If source data is restricted, derivatives and UI presentation must **not** reduce that restriction level.
Map presentations may need safeguards (e.g., generalized/blurred locations) depending on policy.

---

## 🧩 Key UI Capabilities

### 🗺️ Interactive Map Viewer (MapLibre)
Expected map UX:
- Layer toggles (forts, trails, boundaries, ecological zones, etc.)
- Timeline slider / time filter to show changes over time
- Click/hover identify for features → fetch entity details via API

Implementation notes:
- Prefer vector tiles or bounded-viewport GeoJSON fetches for performance.
- Keep map rendering logic separate from API client logic (contract-first).

### 📖 Story Node Reader
Story Nodes are governed narrative Markdown that:
- embed citations to datasets/documents via identifiers
- may define map sync behavior (highlight/zoom as user scrolls)

Reader UX expectations:
- Render Markdown with citation markers.
- Clicking a citation reveals evidence (doc snippet, dataset excerpt, map highlight, etc.).
- Story scroll ↔ map context synchronization.

### 🔎 Focus Mode (Evidence-Only)
Focus Mode is a dedicated layout for verification:
- Story text pane shows citations explicitly
- Evidence pane/tab view shows each cited item
- Evidence retrieval is API-driven (possibly via a convenience “citations bundle” endpoint)

Performance:
- Cache repeated cited items within a session.
- Prefer “bundle” APIs when available to avoid N+1 requests.

### 🏷️ Provenance & uncertainty indicators
UI should communicate data quality and provenance:
- Badge/icon for AI-assisted content
- Badge/icon for generalized/blurred locations
- UI affordances for uncertainty (±, tooltip explaining confidence, etc.)

### ♿ Accessibility & inclusive design
Baseline expectations:
- Keyboard operability
- Screen-reader-friendly narrative content
- Sufficient contrast and scalable text
- Content warnings / context notices when appropriate

---

## 🔌 API Integration

### Contract source of truth
The contract definitions live under:
- `src/server/` (and possibly `src/server/contracts/`) *(path is canonical for API code; subpath is project-specific)*

Frontend work should treat API schemas as first-class:
- generate types (if TS) from OpenAPI/GraphQL
- validate response shapes for critical flows (Story Node, citations, map layers)

### Example endpoints (illustrative; confirm in API contracts)
- Story Nodes:
  - `GET /api/v1/storynodes/{id}`
  - `GET /api/v1/storynodes/{id}/citations` (bundle convenience endpoint)
- Search:
  - `GET /api/v1/search?q=...`
- Map data:
  - `GET /api/v1/tiles/{layer}/{z}/{x}/{y}`
  - or `GET /api/v1/features?layer=...&bbox=...&time=...`

> Do not “invent” endpoints in the UI. Confirm names/paths in the API contract docs/schemas.

---

## 🧪 Local Development

Because the exact build toolchain is project-specific, use one of the patterns below:

### Option A: Static folder dev (no bundler)
If `web/` contains a plain `index.html` + JS/CSS assets:
~~~bash
cd web
python -m http.server 8000
# open http://localhost:8000
~~~

### Option B: Bundler-based dev (React/TS)
If `web/package.json` exists (not confirmed in repo):
~~~bash
cd web
npm install
npm run dev
~~~

### Environment configuration
- Prefer `.env.example` at repo root for required variables.
- UI must allow API base URL configuration (name is project-specific).

---

## 🚦 Validation & Quality Gates

UI contributions should pass:
- Frontend linting and formatting checks (tooling is project-specific)
- Any UI schema validation (if `schemas/ui/` exists)
- End-to-end “evidence-first” checks:
  - citations resolve via API
  - Focus Mode hides/flags uncited content
  - classification/sensitivity indicators render correctly

---

## ⚖️ FAIR+CARE & Governance Notes

- The UI must propagate classification and sensitivity labels returned by the API.
- Never expose sensitive locations/details that were not already approved and contractually permitted.
- If a UI feature changes how restricted data is rendered, flag for governance review.

---

## 🕰️ Version History

- v0.1.0-draft — 2025-12-31 — Initial `web/README.md` draft aligned to KFM v13 pipeline and UI principles.

---

## 📚 References (project docs)

- `docs/MASTER_GUIDE_v13.md` — canonical pipeline order + subsystem homes
- `docs/standards/` — markdown work protocol, repo structure standard, STAC/DCAT/PROV profiles
- `docs/templates/` — Universal Doc, Story Node v3, API Contract Extension templates
- **KFM Architecture Document** — Focus Mode and end-to-end contract layering
- **KFM Unified Technical Plan** — UI component behaviors (map viewer, story reader, Focus Mode)
- **KFM Master Documentation** — UI ↔ API separation, React/MapLibre overview, stateless UI notes
- **Open-Source Geospatial Historical Mapping Hub Design** — repo structure and Pages deployment concept
