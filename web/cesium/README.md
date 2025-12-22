---
title: "KFM Web — Cesium"
path: "web/cesium/README.md"
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

doc_uuid: "urn:kfm:doc:web:cesium:readme:v1.0.0"
semantic_document_id: "kfm-web-cesium-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:web:cesium:readme:v1.0.0"
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

# KFM Web — Cesium

Cesium support for the KFM web client. This area is intended to provide a 3D rendering mode (terrain / globe / immersive views) that can be toggled alongside the primary 2D map experience, while preserving KFM’s pipeline invariants and provenance rules.

## 📘 Overview

### Purpose
- Provide a governed home for Cesium-related UI code and configuration.
- Document how Cesium participates in KFM’s map UI + Focus Mode experiences without breaking the API boundary.

### Scope

| In Scope | Out of Scope |
|---|---|
| Cesium scene/viewer integration used by the `web/` UI | ETL, STAC/DCAT/PROV generation, graph ingest, server/API implementation |
| Mapping “layer registry” entries into Cesium-renderable layers | Defining authoritative data products (those belong in `data/` + catalogs) |
| Focus Mode map synchronization behavior (camera/time/layer hints) | Story Node authoring and curation workflows (those live under `docs/`) |
| UI governance notes: provenance, sensitive layers, redaction expectations | Any attempt to query Neo4j directly from `web/` |

### Audience
- Primary: Frontend developers working on the KFM map UI (React / MapLibre / Cesium).
- Secondary: API/contract owners validating that UI consumption stays within the `src/server/` boundary.

### Definitions
- Glossary: `docs/glossary.md`
- Terms used here:
  - **Layer Registry** — JSON config enumerating UI-available map layers (schema-validated).
  - **Focus Mode** — a UI mode that renders a provenance-linked “context bundle”.
  - **Context Bundle** — API response that includes narrative + structured map/timeline data.
  - **Story Node** — curated narrative artifact (Markdown + citations) that can drive Focus Mode.
  - **Provenance-linked** — content includes evidence identifiers/citations and audit affordances.

### Key artifacts

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Cesium sub-area README | `web/cesium/README.md` | UI | This document |
| Layer registry | `web/cesium/layers/regions.json` | UI + Governance | Schema-validated; add layers here (and/or other files in `layers/`) |
| UI schema(s) | `schemas/ui/` | Contracts owners | Validates layer registries |
| API boundary | `src/server/` | API | UI must consume graph/catalog via API (no direct Neo4j reads) |
| Story Nodes (canonical) | `docs/reports/story_nodes/` | Curators | Served to UI via API context bundles |

### Definition of done
- [ ] Front-matter complete + valid; `path` matches file location.
- [ ] Constraints/invariants explicitly stated (no direct-to-graph; provenance rules).
- [ ] Layer registry guidance includes schema validation expectations.
- [ ] Focus Mode integration notes include provenance and sensitive-layer handling.
- [ ] Validation steps are repeatable (even if commands are placeholders).

## 🗂️ Directory Layout

### This document
- `path`: `web/cesium/README.md` (must match front-matter)

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| Frontend | `web/` | React + map clients (MapLibre + Cesium) |
| UI layer registries | `web/cesium/layers/` | JSON layer catalogs for the map UI |
| UI schemas | `schemas/ui/` | JSON Schemas for layer registries and UI contracts |
| API boundary | `src/server/` | REST/GraphQL; contract enforcement + redaction |
| Story Nodes | `docs/reports/story_nodes/` | Curated narrative artifacts that drive Focus Mode |

### Expected file tree for this sub-area
~~~text
📁 web/
├── 📁 cesium/
│   ├── 📄 README.md
│   └── 📁 layers/
│       ├── 📄 regions.json
│       └── 📄 <other-layer-registry>.json
~~~

## 🧭 Context

### Background
KFM’s canonical flow is preserved end-to-end:
**ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode**.

The map UI is React-based and may support switching between 2D (MapLibre) and 3D (Cesium) without losing UI state. Cesium is used when 3D terrain / immersive visualization is required.

### Assumptions
- The `web/` app is an SPA with predictable state management for selected entity, active layers, and user settings.
- Layer availability is primarily configured via JSON “layer registry” files under `web/cesium/layers/`.
- Focus Mode content arrives via an API “context bundle” that includes narrative + provenance links.

### Constraints and invariants
Non-negotiables:
- **No UI direct-to-graph reads:** `web/` must never query Neo4j directly; graph access is only via `src/server/`.
- **Contracts are canonical:** schemas live under `schemas/` and API contracts under `src/server/contracts/` (with CI validation).
- **Layer registry is schema-validated:** layer registry JSON files must validate against `schemas/ui/`.
- **Focus Mode is provenance-linked only:** do not show uncited narrative by default; any AI-derived content must be opt-in and clearly labeled.

### Open questions

| Question | Owner | Target date |
|---|---|---|
| What is the canonical schema filename(s) under `schemas/ui/` for layer registry validation? | UI + Contracts | TBD |
| What is the canonical “Focus API” contract location/version used by the UI? | API | TBD |
| What is the expected directory structure for Cesium code (components/adapters) under `web/cesium/`? | UI | TBD |

### Future extensions
- Additional 3D experiences (e.g., story-driven camera tours, time-dynamic layers) as long as the pipeline and provenance constraints remain intact.
- Optional integration patterns for richer visualization modes (WebXR, etc.)—only if contracts and sensitivity rules are preserved.

## 🗺️ Diagrams

### System and dataflow
~~~mermaid
flowchart LR
  A[ETL] --> B[STAC/DCAT/PROV Catalogs]
  B --> C[Neo4j Graph]
  C --> D[API boundary src/server]
  D --> E[UI web]
  E --> F[Focus Mode UI state]
  G[Story Nodes docs/reports/story_nodes] --> D
  D --> F
~~~

### Focus Mode sequence
~~~mermaid
sequenceDiagram
  participant UI as UI (web)
  participant API as API (src/server)
  participant Graph as Graph (Neo4j)
  UI->>API: Focus query(entity_id)
  API->>Graph: fetch subgraph + provenance refs
  Graph-->>API: subgraph + evidence IDs
  API-->>UI: context bundle (narrative + citations + map/timeline hints)
~~~

## 📦 Data and Metadata

### Inputs

| Input | Format | Where from | Validation |
|---|---|---|---|
| Layer registry | JSON | `web/cesium/layers/*.json` | JSON Schema under `schemas/ui/` |
| Focus Mode context bundle | JSON | API boundary (`src/server/`) | API contract tests + runtime guards |
| Catalog endpoints | JSON | STAC/DCAT/PROV endpoints | Schema validation at source |

### Outputs

| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Interactive 3D map experience | Runtime UI | `web/` | UI invariants + a11y + audit affordances |
| Layer toggles/visibility state | Runtime UI state | (runtime) | Deterministic behavior; no data leakage |

### Sensitivity and redaction
- Layer registries may include sensitivity flags; sensitive layers must be gated by access rules.
- Redaction/generalization is enforced at the API boundary; the UI must not “reconstruct” restricted detail client-side.
- Any sensitive locations must not be inferred or exposed via UI interactions.

### Quality signals
- Layer registry validates against `schemas/ui/` (CI gate).
- No orphan layer references (registry entries reference reachable endpoints/assets).
- Focus Mode narrative renders with citations and audit affordances intact.

## 🌐 STAC, DCAT, and PROV alignment

This UI area does not author catalogs; it consumes catalog and provenance artifacts via APIs/endpoints.

- STAC: consumed for map-ready assets and evidence references.
- DCAT: consumed for dataset-level metadata and attribution surfaces.
- PROV: consumed for audit/provenance panels in Focus Mode.

## 🧱 Architecture

### Components

| Component | Responsibility | Interface |
|---|---|---|
| ETL | Ingest + normalize | Config + run logs |
| Catalogs | STAC/DCAT/PROV artifacts | JSON + validators |
| Graph | Neo4j knowledge graph | API boundary only |
| APIs | Serve contracts + redaction | REST/GraphQL |
| UI | Map + narrative | API calls + catalog endpoints |
| Story Nodes | Curated narrative | Served through API context bundles |
| Focus Mode | Provenance-linked synthesis | Context bundle only |

### Interfaces and contracts

| Contract | Location | Versioning rule |
|---|---|---|
| JSON schemas | `schemas/` | Semver + changelog |
| API schemas | `src/server/` + `docs/api/` | Contract tests required |
| Layer registry | `web/cesium/layers/regions.json` | Schema-validated; additive changes preferred |

### Adding a new layer
1) Add a new entry to an existing registry (or add a new registry file) under `web/cesium/layers/`.
2) Ensure the entry validates against the schema in `schemas/ui/`.
3) Ensure the data source is served via the API boundary (and any needed redaction/sensitivity rules are applied there).
4) Confirm attribution and licensing fields are present as required by the schema.

Illustrative example only (confirm exact schema fields under `schemas/ui/`):
~~~json
{
  "id": "kfm-example-layer",
  "name": "Example Layer",
  "source_url": "https://example.invalid/data.geojson",
  "attribution": "TBD",
  "sensitive": false
}
~~~

## 🧠 Story Node and Focus Mode integration

### How this surfaces in Focus Mode
- Focus Mode is entered when the user selects a focusable entity (place/person/event/story).
- The UI requests a Focus Mode context bundle from the API.
- The UI:
  - updates the map camera/center,
  - enables relevant layers,
  - renders the narrative (Markdown) with citations and an audit/provenance panel.

Optional structured controls are commonly provided by Story Nodes:
~~~yaml
focus_layers:
  - "TBD"
focus_time: "TBD"
focus_center: [-98.0000, 38.0000]
~~~

### Rendering Story Node citations
Story Nodes are Markdown and may embed citations in the `【source†Lx-Ly】` style. The UI should render these as interactive references (e.g., hyperlinks or popovers) rather than plain text.

### AI-derived content
If AI-generated explanations are exposed in the UI:
- they must be opt-in,
- clearly labeled,
- and accompanied by source references and uncertainty metadata.

## 🧪 Validation and CI/CD

### Validation steps
- [ ] Markdown protocol checks (front-matter + structure)
- [ ] UI schema checks (layer registry validates against `schemas/ui/`)
- [ ] Frontend component tests for Focus Mode rendering (narrative + citations)
- [ ] E2E flow tests (enter/exit Focus Mode; 2D/3D toggle; layer toggles)

### Reproduction
~~~bash
# Example placeholders — replace with repo-specific commands

# 1) validate UI layer registry schemas
# 2) run UI unit/integration tests
# 3) run E2E tests for Focus Mode and map interactions
# 4) run doc lint / markdown checks
~~~

### Telemetry signals
- TBD (not confirmed in repo): performance and error telemetry for Cesium render loop, layer load failures, and Focus Mode load failures.

## ⚖ FAIR+CARE and governance

### Governance review triggers
- Adding a new sensitive layer or exposing a new location-precise dataset in the UI.
- Any change that alters how provenance/citations are displayed or enforced.
- Any new public-facing endpoint required for 3D assets.

### Sovereignty safety
- Do not expose restricted locations or culturally sensitive knowledge.
- Enforce generalization/redaction at the API layer; ensure the UI respects gating flags in layer registries and payloads.

## 🕰️ Version history

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-21 | Initial `web/cesium/README.md` | TBD |
