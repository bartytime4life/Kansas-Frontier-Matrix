---
title: "KFM Cesium Frontend — Docs (Layer Registry + Focus Mode Hooks)"
path: "web/cesium/docs/README.md"
version: "v0.1.0"
last_updated: "2025-12-18"
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

doc_uuid: "urn:kfm:doc:web:cesium:readme:v0.1.0"
semantic_document_id: "kfm-web-cesium-readme-v0.1.0"
event_source_id: "ledger:kfm:doc:web:cesium:readme:v0.1.0"
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

# KFM Cesium Frontend — Docs (Layer Registry + Focus Mode Hooks)

## 📘 Overview

### Purpose
- Document how the **Cesium-based map client** fits into the Kansas Frontier Matrix (KFM) UI stack and pipeline.
- Provide **governed, repeatable instructions** for adding/editing map layers using the **declarative layer registry** (instead of ad‑hoc UI code changes).
- Define the **minimum provenance + sensitivity requirements** for any layer that can be toggled or clicked in the UI (including Focus Mode entry points).

### Scope
| In Scope | Out of Scope |
|---|---|
| Cesium UI module expectations (2D/3D map view) | ETL scripts, dataset ingestion logic (see `src/pipelines/` + data SOPs) |
| Layer registry conventions + examples | API schema/contract changes (use `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md`) |
| How map interactions trigger Focus Mode / dossiers | Story Node authoring (use `docs/templates/TEMPLATE__STORY_NODE_V3.md`) |
| Provenance + redaction rules as they apply to map layers | Operating the production deployment (infra/runbooks) |

### Audience
- Primary: Frontend developers working in `web/` (Cesium/Map UI)
- Secondary: Data engineers adding layers/collections, reviewers validating governance + provenance

### Definitions (link to glossary)
- Link: `docs/glossary.md`
- Terms used in this doc:
  - **Layer registry**: A declarative JSON configuration file describing map layers (visibility, zoom limits, provenance pointers, sensitivity behaviors).
  - **Focus Mode**: A narrative/detail view built from provenance‑linked evidence; it must not invent unsupported claims.
  - **STAC / DCAT / PROV**: Catalog + dataset + lineage standards used to keep the UI evidence‑traceable.

### Key artifacts (what this doc points to)
| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Canonical pipeline + invariants | `docs/MASTER_GUIDE_v12.md` | KFM governance | Pipeline ordering + system boundaries |
| Cesium layer registry (declarative) | `web/cesium/layers/regions.json` | Frontend | Add/edit layers here (schema-validated) |
| STAC catalogs | `data/stac/` | Data/pipelines | Layer provenance should resolve to STAC IDs |
| Graph + API boundary | `src/server/` (APIs), `src/graph/` (graph) | Backend | UI must not directly query graph |
| Universal doc template | `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` | Docs governance | This README follows the Universal governed doc structure |

### Definition of done (for this document)
- [ ] Front-matter complete + valid (path/version/status updated)
- [ ] Describes **where** to add a Cesium layer (registry) + **what metadata is required**
- [ ] States **provenance requirements** for layer content + Focus Mode triggers
- [ ] States **sensitivity/redaction expectations** for restricted layers
- [ ] Validation steps listed and repeatable (at minimum: `make test` / schema validation paths)
- [ ] No instructions that bypass the API boundary (no direct graph access from the UI)

## 🗂️ Directory Layout

### This document
- `path`: `web/cesium/docs/README.md` (must match front-matter)

### Related repository paths
| Area | Path | What lives here |
|---|---|---|
| Frontend | `web/` | Map UI(s), including Cesium-based 2D/3D client |
| Cesium layer registry | `web/cesium/layers/` | Declarative layer configs (JSON) |
| Data domains | `data/` | Raw/work/processed/stac outputs (no derived data in `src/`) |
| Catalogs | `data/stac/` | STAC JSON catalogs/items/collections |
| Schemas | `schemas/` | JSON schemas + telemetry schemas (including UI registry schemas if present) |
| APIs | `src/server/` | REST/GraphQL APIs consumed by UI |
| Graph | `src/graph/` | Graph build + ontology bindings (not consumed directly by UI) |
| Governance | `docs/governance/` | ROOT_GOVERNANCE + ethics + sovereignty rules |
| Story Nodes | `docs/story_nodes/` (or governed location) | Narrative nodes consumed by Focus Mode *(path not confirmed in repo)* |

### Expected file tree for this sub-area
~~~text
web/
└── 🗺️ cesium/
    ├── 📁 docs/
    │   └── 📄 README.md                # (this file)
    └── 📁 layers/
        └── 📄 regions.json             # declarative Cesium layer registry (schema-validated)
~~~

## 🧭 Context

### Background
- KFM’s UI includes a map experience (2D and optional 3D) that must stay aligned with governed datasets, catalogs, and provenance so users can trace “what they’re seeing” back to sources.
- CesiumJS is considered/used to support full 3D globe visualization and richer spatial storytelling.

### Assumptions
- The Cesium map client is configured to load layers **only** through the registry (not by hardcoding layers in components).
- Each “layer” corresponds to one or more governed datasets that can be identified via **STAC IDs** (and, where applicable, DCAT dataset identifiers and PROV run/activity IDs).

### Constraints / invariants
- **Canonical pipeline ordering is preserved:** ETL → STAC/DCAT/PROV catalogs → Graph → APIs → UI → Story Nodes → Focus Mode.
- **API boundary:** Frontend consumes contracts via APIs (no direct graph dependency).
- Sensitive layers **must** be governed: default visibility, zoom limits, generalization/redaction behavior, and auditability must be defined.

### Open questions
| Question | Owner | Target date |
|---|---|---|
| Is `web/cesium` deployed as a standalone app, or embedded inside a single `web/` app bundle? *(not confirmed in repo)* | TBD | TBD |
| Where is the canonical JSON schema for `web/cesium/layers/*.json` located? *(not confirmed in repo)* | TBD | TBD |
| What is the preferred runtime data transport for large polygon layers (GeoJSON vs vector tiles vs 3D Tiles)? *(not confirmed in repo)* | TBD | TBD |

### Future extensions
- Support additional registry-backed layer types (e.g., 3D Tilesets for terrain/buildings) with the same provenance/sensitivity requirements.
- Time-enabled layers (timeline slider / time filtering) that remain provenance-traceable.
- Focus Mode deep-links from map features (stable entity IDs and evidence bundles).

## 🗺️ Diagrams

### System / dataflow diagram
~~~mermaid
flowchart LR
  A["ETL and processing"] --> B["Catalogs: STAC • DCAT • PROV"]
  B --> C["Graph and indexes (Neo4j)"]
  C --> D["APIs: REST and GraphQL"]
  D --> E["Web UI"]
  E --> F["Cesium map client"]
  E --> G["Story Nodes"]
  G --> H["Focus Mode narrative"]

  F -->|click or select feature| H
  F -->|toggle layers| F
~~~

### Optional: Layer registry governed flow
~~~mermaid
flowchart TD
  R["web/cesium/layers/regions.json"] -->|schema validated| L["Layer loader"]
  L --> V["Visibility rules\n(default_enabled, zoom, roles)"]
  L --> P["Provenance pointers\n(stac_id, prov_ref)"]
  V --> C["Cesium viewer"]
  P --> U["About this layer panel"]
  C --> FM["Focus Mode trigger"]
  FM -->|API call with provenance IDs| AAPI["Focus Mode API"]
~~~

## 📦 Data & Metadata

### Inputs
| Input | Location | Format | Validation | Notes |
|---|---|---|---|---|
| Cesium layer registry | `web/cesium/layers/regions.json` | JSON | JSON schema (expected) + CI checks | Governs what layers exist and how they behave |
| STAC collection(s)/item(s) | `data/stac/…` | JSON | STAC validation in CI | Used to resolve provenance for a layer’s assets |
| API responses (features, entities, Focus context) | `src/server/…` | JSON | OpenAPI/GraphQL contract tests (expected) | UI must not directly query Neo4j |

### Outputs
| Output | Produced by | Format | Validation | Notes |
|---|---|---|---|---|
| Rendered map scene (2D/3D) | Cesium client | WebGL | Visual regression tests (optional) | Must reflect registry + API responses only |
| Layer “about” / provenance UI | Cesium client | UI components | Snapshot/UI tests (optional) | Must display resolvable provenance pointers |
| Focus Mode deep link | Cesium client → API | JSON payloads | Contract tests | Must request provenance-linked context only |

### Sensitivity considerations
- Registry entries must support “safe by default” behavior:
  - **Off by default** for sensitive layers, or **zoom‑limited** to reduce the risk of exposing precise locations.
  - **Generalization/redaction** requirements for restricted classes (e.g., bounding region vs exact coordinates).
- When a dataset includes a `sensitivity_class` or equivalent label, the layer must enforce gating consistent with governance rules.

### Quality considerations
- Prefer reproducible sources: layers should reference governed assets (STAC) and not “mystery URLs”.
- Prefer stable identifiers: link features to canonical IDs used by the API/graph so Focus Mode can retrieve evidence bundles deterministically.

## 🌐 STAC, DCAT & PROV alignment

### STAC alignment (asset discoverability)
- Every layer should resolve to at least one **STAC Collection ID** (and, when possible, item IDs for time-sliced assets).
- UI should link “About this layer” → STAC metadata for bounding box, temporal extent, license, and asset links.

### DCAT alignment (dataset-level description)
- For layers that represent a dataset collection (not individual assets), reference a DCAT dataset identifier (if KFM publishes/exports one).
- Use DCAT-aligned fields (title, description, publisher, temporal/spatial coverage) to power layer catalog/legend UX.

### PROV-O alignment (lineage & audit)
- Where the layer is derived (processed output), provide a PROV activity/run reference so the UI (and auditors) can trace:
  - inputs used
  - transformation steps
  - producing agent/tool versions
- Do not treat provenance as optional metadata for layers that can influence narrative outputs.

### Versioning
- Layer registry changes are **contract-like** for the UI: update versions/changelog when behavior changes (visibility defaults, data source IDs, redaction rules).

## 🧱 Architecture

### Components
- **Registry loader**: Reads `web/cesium/layers/regions.json`, validates it, and produces layer descriptors.
- **Layer adapters/renderers**: Render supported layer types (e.g., point features, polygons, imagery/tiles).
- **API client**: Fetches contracted data (features, entity metadata, Focus Mode context) through `src/server/` endpoints.
- **Provenance UI**: Provides a consistent “About this layer” surface that shows STAC/DCAT/PROV pointers.

### Interfaces
- **To APIs:** REST/GraphQL calls for:
  - entity lookup by ID
  - Focus Mode context payloads
  - (optional) vector tile / imagery service discovery
- **To catalogs:** STAC metadata references (IDs/URLs) used by UI for “about/provenance” flows.

### Extension points
- Add a new registry layer entry + implement a renderer if a new type is required.
- Add UI affordances (legend, time slider, filter) only when the layer metadata supports it (avoid hardcoded per-layer behavior).

## 🧠 Story Node & Focus Mode Integration

### How this area supports Story Nodes
- Map interactions (clicking a feature, selecting a region) can deep-link users into Story Nodes or Focus Mode narratives for:
  - places
  - events
  - entities discovered via analysis outputs (e.g., candidate sites)

### Provenance-linked evidence flow
- Clicking a map feature should pass a **stable entity ID** (or STAC item ID) to the Focus Mode API.
- Focus Mode responses must contain **provenance references** so downstream narrative generation can cite sources.

### Optional integration points
- “Open dossier” action from a feature tooltip.
- “View sources” panel that enumerates STAC assets + PROV run IDs tied to the layer/feature.

## 🧪 Validation & CI/CD

### Validation steps
Run the repo test suite:
~~~bash
make test
~~~

Run the local site (if supported by repo tooling):
~~~bash
make serve
~~~

Ensure registry JSON passes schema validation *(schema location not confirmed in repo; check `schemas/` or CI logs)*.

### Reproduction checklist
- [ ] Layer registry entry added/updated without breaking existing layer IDs
- [ ] STAC IDs referenced by the layer exist and are resolvable
- [ ] If sensitive: defaults are “off”, zoom-limited, or generalized as required
- [ ] Clicking features triggers Focus Mode with provenance-linked context only
- [ ] Tests pass (`make test`) and any required schema lint steps pass

### Telemetry / logging
- Any user interaction logging must avoid capturing precise sensitive coordinates.
- If telemetry schemas exist under `schemas/`, UI events should conform to those schemas *(not confirmed in repo)*.

## ⚖ FAIR+CARE & Governance

### Review requirements
- Layer registry changes are governed: reviewers should include at least:
  - UI maintainer (frontend)
  - governance/sovereignty reviewer if sensitivity_class is not purely public/open
  - data curator if the layer references a new dataset or STAC collection

### CARE considerations
- Sensitive cultural heritage locations (or restricted archaeological candidates) must be generalized/redacted and not exposed by default.
- Honor sovereignty policy and any required access-control behavior (even in an “open data” UI).

### AI usage
- Any narrative surfaced via Focus Mode must be provenance‑linked (no hallucinated facts).
- If the UI provides “AI summaries” of layer content, it must only summarize evidence present in the returned context bundle.

## 🕰 Version History
| Version | Date | Summary | Author |
|---|---|---|---|
| v0.1.0 | 2025-12-18 | Initial `web/cesium/docs/README.md` using Universal governed doc template | TBD |
