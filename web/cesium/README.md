---
title: "KFM Web — Cesium"
path: "web/cesium/README.md"
version: "v1.0.1"
last_updated: "2025-12-24"
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

doc_uuid: "urn:kfm:doc:web:cesium:readme:v1.0.1"
semantic_document_id: "kfm-web-cesium-readme-v1.0.1"
event_source_id: "ledger:kfm:doc:web:cesium:readme:v1.0.1"
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

Cesium support for the KFM web client. This area provides an optional **3D rendering mode** (globe/terrain/3D tiles) that can be toggled alongside the primary 2D map experience, while preserving KFM’s pipeline invariants, API boundary, and provenance rules.

> **Purpose (required):** Define what belongs in `web/cesium/`, how Cesium integrates into the `web/` UI, and what invariants must be enforced (API boundary, provenance-first Focus Mode, sensitivity/redaction, schema-validated layer registries).

## 📘 Overview

### Purpose

- Provide a governed home for Cesium-related UI code/config and integration notes.
- Document how 3D rendering participates in KFM’s map UI + Focus Mode without breaking:
  - the **API boundary**,
  - **provenance-linked narrative** rules,
  - **sensitivity / sovereignty** constraints,
  - and **contract-first** validation expectations.

### Scope

| In Scope | Out of Scope |
|---|---|
| Cesium viewer/scene integration used by the `web/` UI | ETL, catalog generation (STAC/DCAT/PROV), graph ingest, server/API implementation |
| Translating UI layer registries into Cesium-renderable layers (3D Tiles, terrain, imagery, entities) | Defining authoritative data products (those belong under `data/**` + catalogs) |
| Focus Mode map synchronization behavior (camera/time/layer hints) | Story Node authoring workflows (canonical home is `docs/reports/story_nodes/`) |
| Governance notes for 3D rendering: provenance, sensitive layers, redaction expectations | Any attempt to query Neo4j directly from `web/` |

### Audience

- Primary: Frontend developers working on KFM’s map UI (React / MapLibre / Cesium).
- Secondary: API/contract owners ensuring UI consumption stays within the `src/server/` boundary; governance reviewers for sensitive layers.

### Definitions (link to glossary)

- Glossary: `docs/glossary.md` *(not confirmed in repo — add or repair link if glossary lives elsewhere)*

Terms used here:
- **Layer registry** — declarative JSON (or equivalent) listing UI-available layers, sources, attribution, and sensitivity flags (schema-validated if `schemas/ui/` exists).
- **Focus Mode** — an immersive UI view that renders a provenance-linked “context bundle”.
- **Context bundle** — API response that includes narrative + structured map/timeline hints + evidence identifiers.
- **Story Node** — curated narrative artifact (Markdown + citations) that can drive Focus Mode (canonical home: `docs/reports/story_nodes/`).
- **Provenance-linked** — content includes evidence identifiers/citations and audit affordances.

### Key artifacts

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Web UI README | `web/README.md` | UI | Entry point for UI boundaries + invariants |
| Web source README | `web/src/README.md` | UI | Runtime implementation boundaries (API clients, Focus Mode rendering) |
| Cesium sub-area README | `web/cesium/README.md` | UI | This document |
| Cesium layer registries | `web/cesium/layers/` | UI + Governance | **If present:** schema-validated registry files for 3D layers |
| UI schema(s) | `schemas/ui/` | Schemas/Contracts | **If present:** JSON Schemas for layer registries and UI contracts |
| API boundary | `src/server/` + `src/server/contracts/` | API | UI consumes via contracts; no direct graph access |
| Story Nodes (canonical) | `docs/reports/story_nodes/` | Curators | Served to UI via API context bundles |

### Definition of done (for this document)

- [ ] Front-matter complete + valid; `path` matches file location
- [ ] Constraints/invariants explicit (no direct-to-graph; provenance + sensitivity rules)
- [ ] Layer registry guidance includes schema validation expectations (and marks paths “not confirmed” if uncertain)
- [ ] Focus Mode integration notes include provenance + sensitive-layer handling
- [ ] Validation steps are repeatable (commands may be placeholders)

## 🗂️ Directory Layout

### This document

- `path`: `web/cesium/README.md` (must match front-matter)

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| Frontend root | `web/` | UI app root (MapLibre + Focus Mode; Cesium is optional) |
| Frontend source | `web/src/` | React runtime: API clients, state, Focus Mode rendering |
| Cesium sub-area | `web/cesium/` | Cesium integration notes/config (this area) |
| UI layer registries | `web/**/layers/**` | Layer registry files (repo-specific) |
| UI schemas | `schemas/ui/` | JSON Schemas for UI registries (if present) |
| API boundary | `src/server/` | REST/GraphQL services + redaction + provenance linking |
| Story Nodes | `docs/reports/story_nodes/` | Draft/published narrative artifacts (served via API) |
| Evidence catalogs | `data/stac/` + `data/catalog/dcat/` + `data/prov/` | Evidence artifacts for traceability |

### Expected file tree for this sub-area

> Target/typical layout. Keep this section updated if your actual tree differs.

~~~text
📁 web/
├── 📁 cesium/
│   ├── 📄 README.md
│   ├── 📁 layers/                    # optional (3D-focused layer registries)
│   │   ├── 📄 regions.json            # example only — not confirmed in repo
│   │   └── 📄 <registry>.json
│   ├── 📁 adapters/                  # optional (Cesium layer adapters/translators)
│   ├── 📁 assets/                    # optional (presentation-only, public-safe assets)
│   └── 📁 test/                      # optional (fixtures/unit tests for adapters)
└── 📁 src/                           # main app runtime (React)
~~~

## 🧭 Context

### Background

KFM’s canonical flow is preserved end-to-end:

**ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode**

Cesium, if enabled, is a **UI-only rendering mode**. It must not introduce new “data authority” paths; all authoritative data remains produced upstream (ETL/catalog/graph) and delivered through contracted APIs.

### Assumptions

- `web/` is a single-page application (SPA) that can toggle between:
  - a primary **2D map** mode (e.g., MapLibre),
  - and an optional **3D** mode (Cesium).
- 2D ↔ 3D switching preserves user intent (selected entity, active layers, time window) using deterministic state.
- Layer availability is configured via a registry (repo-specific location), ideally schema-validated (`schemas/ui/` if present).
- Focus Mode content arrives via an API “context bundle” that includes narrative + provenance links + structured map/timeline hints.

### Constraints / invariants

Non-negotiables:

- **No UI direct-to-graph reads:** `web/` must never query Neo4j directly; graph access is only via `src/server/`.
- **Contracts are canonical:**
  - API contracts live under `src/server/contracts/` (or repo-defined equivalent).
  - UI schemas live under `schemas/` (e.g., `schemas/ui/`).
- **Provenance-first Focus Mode:** the UI must not present uncited narrative as fact.
- **Sensitive layers are governed:** the UI must respect sensitivity/redaction flags delivered by the API and/or registry.
- **No secrets in repo:** Cesium Ion tokens, API keys, and provider credentials must not be committed. Use runtime configuration patterns (repo-specific).

Implementation safety expectations:

- UI must not “reconstruct” restricted location detail client-side from generalized values.
- Any third-party tile/asset service must be vetted for licensing + data export risks.

### Open questions

| Question | Owner | Target date |
|---|---|---|
| Where is the canonical layer registry stored in this repo (`web/**/layers/**`)? | UI Team | TBD |
| What schema file(s) under `schemas/ui/` validate Cesium layer registry entries? | UI + Schemas | TBD |
| What is the canonical “Focus API” contract location/version used by the UI? | API Team | TBD |
| Does Cesium integration live as a separate module under `web/cesium/` or inside `web/src/**`? | UI Team | TBD |

### Future extensions

- Time-dynamic 3D layers (only if contracts + provenance are preserved).
- Story-driven camera tours (scripted views) that reference provenance-linked Story Nodes.
- Progressive enhancement: browsers without WebGL2 still get a complete 2D experience.

## 🗺️ Diagrams

### System and dataflow

~~~mermaid
flowchart LR
  A["ETL (src/pipelines)"] --> B["STAC/DCAT/PROV (data/stac · data/catalog/dcat · data/prov)"]
  B --> C["Graph (Neo4j via src/graph)"]
  C --> D["API Boundary (src/server + contracts)"]
  D --> E["UI (web/)"]
  E --> F["2D Map (MapLibre)"]
  E --> G["3D Map (Cesium)"]
  E --> H["Story Nodes / Focus Mode"]
~~~

### Focus Mode sequence (3D-enabled path)

~~~mermaid
sequenceDiagram
  participant UI as UI (web)
  participant API as API (src/server)
  participant Graph as Graph (Neo4j + catalogs)

  UI->>API: GET /focus?entity_id=...
  API->>Graph: Fetch subgraph + evidence refs (STAC/DCAT/PROV IDs)
  Graph-->>API: Context bundle + provenance identifiers
  API-->>UI: Contracted payload (narrative + citations + map/timeline hints)
  UI-->>UI: Optionally apply hints to Cesium camera + layers
~~~

## 📦 Data & Metadata

### Inputs

| Input | Format | Where from | Validation |
|---|---|---|---|
| Layer registry entries | JSON | `web/**/layers/**` (repo-specific) | JSON Schema under `schemas/ui/` (if present) |
| Focus Mode context bundle | JSON | API boundary (`src/server/`) | API contract tests + runtime guards |
| Evidence identifiers | IDs/URLs | STAC/DCAT/PROV artifacts via API | ID integrity + link validation at source |

### Outputs

| Output | Format | Path | Notes |
|---|---|---|---|
| Interactive 3D map experience | Runtime UI | `web/` | Presentation only; no authoritative data is authored here |
| Layer visibility/camera state | Runtime UI state | (runtime) | Deterministic behavior; must not leak restricted detail |

### Sensitivity and redaction

- Treat registry + API-delivered sensitivity flags as authoritative.
- Do not encode restricted coordinates in client-side logs/telemetry.
- Avoid UI interactions that enable triangulation of redacted sites (e.g., repeated “center to feature” on generalized points).

### Quality signals

- Layer registry validates against `schemas/ui/` (CI gate, if implemented).
- Focus Mode narrative renders with citations + audit affordances intact.
- 2D ↔ 3D toggling does not drop provenance context (sources panel remains available).
- Performance budgets are respected (acceptable frame rate; reasonable tile/3D asset weight).

## 🌐 STAC, DCAT & PROV Alignment

This UI sub-area does **not** author catalogs; it consumes catalog and provenance artifacts.

Expected linkage for 3D-enabled assets:

- **STAC**: 3D tilesets / terrain / derived rasters should be cataloged as STAC Items with assets (e.g., COG, 3D Tiles).
- **DCAT**: dataset-level metadata and licensing should remain accessible (UI surfaces attribution).
- **PROV**: Focus Mode should be able to show “how this was made” (activity/run identifiers).

If a 3D visualization depends on derived products, those products must live upstream (under `data/**`) and be referenced via catalogs and the API boundary.

## 🧱 Architecture

### Components

| Component | Responsibility | Interface |
|---|---|---|
| Cesium adapter | Translate KFM layer registry → Cesium primitives | Registry entries + typed adapters |
| Camera synchronizer | Keep Focus Mode state consistent across 2D/3D | Focus hints (center/time/layers) |
| Layer registry loader | Load/validate registries | `schemas/ui/` (if present) |
| API client | Fetch focus bundles + layer metadata | Contracted REST/GraphQL |

### Interfaces / contracts

| Contract | Location | Versioning rule |
|---|---|---|
| UI registry schemas | `schemas/ui/` | Semver + schema validation (if adopted) |
| API schemas/contracts | `src/server/contracts/` | Contract tests required |
| Story Node schema/template | `schemas/storynodes/` + `docs/templates/` | Must validate before publish |
| Focus bundle payload | API contract | Backward compatible or version bump |

### Cesium configuration rules

- Any Cesium Ion usage (if adopted) must treat tokens as secrets:
  - do not commit tokens,
  - do not embed tokens in registries committed to git,
  - do not expose privileged tokens to the browser.
- Prefer serving KFM-owned 3D assets via governed endpoints where access, attribution, and redaction can be enforced consistently.

### Adding a new Cesium-capable layer (checklist)

1) Add/modify a layer entry in the canonical registry location (repo-specific; may be `web/**/layers/**`).
2) Validate the registry entry against `schemas/ui/` (if present).
3) Ensure the underlying data source is served via the API boundary (or other governed endpoints), with redaction/sensitivity applied.
4) Ensure attribution and licensing metadata are present (registry and/or API payload).
5) Add/extend the Cesium adapter to support the layer type (if new).

Illustrative example only (confirm exact schema fields under `schemas/ui/`):

~~~json
{
  "id": "kfm-example-3dtiles",
  "name": "Example 3D Tiles Layer",
  "kind": "3dtiles",
  "source": {
    "href": "https://api.example.invalid/v1/tilesets/example-tileset",
    "format": "3dtiles"
  },
  "attribution": "TBD",
  "license": "TBD",
  "sensitivity": "public",
  "requires_auth": false
}
~~~

## 🧠 Story Node & Focus Mode Integration

### How this surfaces in Focus Mode

- Focus Mode is entered when the user selects a focusable entity (Place/Person/Event/Organization/Story Node).
- The UI requests a **Focus Mode context bundle** from the API.
- The UI may apply optional structured hints to Cesium:
  - camera center/heading/pitch/range,
  - enabled layers,
  - time range / timeline window.

Optional structured controls (returned by API and/or embedded in Story Nodes):

~~~yaml
focus_layers:
  - "TBD"
focus_time: "TBD"
focus_center: [-98.0000, 38.0000] # lon, lat (example only)
~~~

### Rendering Story Node citations

Story Nodes are Markdown and may embed citations in the `【source†Lx-Ly】` style. The UI should render these as interactive references (links/popovers/sources panel), not as plain text.

### AI-derived content (if present)

If AI-generated explanations are exposed in the UI:
- they must be opt-in,
- clearly labeled,
- accompanied by uncertainty/confidence metadata,
- and never presented as unmarked fact.

## 🧪 Validation & CI/CD

### Validation steps

- [ ] Markdown protocol checks (front-matter + required sections)
- [ ] UI schema checks (layer registry validates against `schemas/ui/`, if present)
- [ ] Frontend unit tests for:
  - layer registry parsing,
  - Cesium adapter mapping,
  - Focus Mode rendering (narrative + citations)
- [ ] E2E flow tests:
  - enter/exit Focus Mode,
  - toggle 2D/3D,
  - enable/disable Cesium layers,
  - verify sources panel remains present and correct
- [ ] Security checks:
  - secret scan (tokens/keys),
  - telemetry redaction checks (no sensitive coordinates)

### Reproduction

~~~bash
# Example placeholders — replace with repo-specific commands
# (typically driven by web/package.json scripts)

# 1) validate UI layer registry schemas
# 2) run UI unit/integration tests
# 3) run E2E tests for Focus Mode and map interactions
# 4) run doc lint / markdown checks
~~~

### Telemetry signals (if applicable)

- Cesium render loop performance (frame time / dropped frames)
- 3D asset load failures (tileset/terrain)
- Focus Mode load failures (context bundle fetch errors)

## ⚖ FAIR+CARE & Governance

### Governance review triggers

- Adding a new sensitive 3D layer or exposing location-precise datasets in the UI.
- Any change that alters how provenance/citations are displayed or enforced.
- Any new third-party 3D tile/terrain service integration.
- Any change that could enable inference of restricted locations (camera snapping, precision tooltips).

### Sovereignty safety

- Do not expose restricted locations or culturally sensitive knowledge.
- Enforce generalization/redaction at the API layer; ensure the UI respects gating flags in registry entries and payloads.

### Third-party services & licensing

- Ensure registries or UI copy surface required attributions.
- Do not “bake in” third-party data products into UI artifacts without catalog/provenance.

## 🕰️ Version history

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-21 | Initial `web/cesium/README.md` | TBD |
| v1.0.1 | 2025-12-24 | Clarified optional 3D role, strengthened invariants (API boundary, provenance, sensitivity), added cross-links and tightened registry guidance | TBD |

---

Footer refs:
- Master guide: `docs/MASTER_GUIDE_v12.md`
- Redesign blueprint: `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md`
- Web UI: `web/README.md`
- Web source: `web/src/README.md`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`