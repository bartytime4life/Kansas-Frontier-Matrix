---
title: "KFM Web — Cesium"
path: "web/cesium/README.md"
version: "v1.0.2"
last_updated: "2025-12-26"
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

doc_uuid: "urn:kfm:doc:web:cesium:readme:v1.0.2"
semantic_document_id: "kfm-web-cesium-readme-v1.0.2"
event_source_id: "ledger:kfm:doc:web:cesium:readme:v1.0.2"
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

Cesium support for the KFM web client.

This sub-area defines the **governed boundary** for an optional **3D rendering mode** (globe/terrain/3D tiles) that can be toggled alongside the primary **2D map** experience (e.g., MapLibre), **without breaking** KFM’s pipeline invariants: API boundary, provenance-first Focus Mode, and sensitivity/redaction rules.

> **Purpose (required):** Define what belongs in `web/cesium/`, how Cesium integrates into the `web/` UI, and what invariants must be enforced (API boundary, provenance-first Focus Mode, sensitivity/redaction, schema-validated layer registries, and secret-safe configuration).

## 📘 Overview

### Purpose

- Provide a governed home for **Cesium-related UI integration** (documentation, configuration conventions, and optional adapter patterns).
- Ensure 3D rendering participates in KFM’s map UI + Focus Mode **without introducing new “data authority” paths**:
  - the **UI remains a consumer** (never an author) of data products,
  - the **API boundary remains canonical** for KFM-owned data access,
  - and **provenance/sensitivity** remain intact in 3D as they are in 2D.

### Scope

| In Scope | Out of Scope |
|---|---|
| Cesium viewer/scene integration used by the `web/` UI | ETL, catalog generation (STAC/DCAT/PROV), graph ingest, server/API implementation |
| Translating **UI layer registry** entries into Cesium renderables (3D Tiles, terrain, imagery, entities) | Defining authoritative data products (those belong under `data/**` + catalogs) |
| Focus Mode map synchronization in 3D (camera/time/layer hints) | Story Node authoring workflows (canonical home is `docs/reports/story_nodes/`) |
| Governance for 3D rendering: provenance, sensitive layers, redaction expectations | Any attempt to query Neo4j directly from `web/` |

### Audience

- Primary: Frontend developers working on KFM’s map UI (React / MapLibre / Cesium).
- Secondary:
  - API/contract owners ensuring UI consumption stays within the `src/server/` boundary.
  - Governance reviewers for sensitive layers and redaction behavior.

### Definitions

- Glossary: `docs/glossary.md` *(expected canonical location; if missing, treat as **not confirmed in repo** and repair link)*

Terms used in this document:
- **Layer registry** — declarative JSON (or equivalent) listing UI-available layers, sources, attribution, licensing, and sensitivity flags (schema-validated under `schemas/ui/` if present).
- **Focus Mode** — an immersive UI view that renders a provenance-linked “context bundle” (narrative + evidence + map/time hints).
- **Context bundle** — API response that includes narrative, structured map/timeline hints, and evidence identifiers.
- **Story Node** — curated narrative artifact (Markdown + citations) that can drive Focus Mode (canonical home: `docs/reports/story_nodes/`).
- **Provenance-linked** — narrative content includes evidence identifiers/citations and audit affordances (sources panel, warnings, lineage links).
- **3D mode** — Cesium-based rendering path inside `web/` (optional; 2D remains complete and primary).

### Key artifacts

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master guide | `docs/MASTER_GUIDE_v12.md` | KFM Core | Canonical pipeline + invariants |
| v13 redesign blueprint (if adopted) | `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md` | Arch | Canonical paths + minimum contract set |
| Universal doc template | `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` | Docs | Governing template applied by this README |
| Story Node template | `docs/templates/TEMPLATE__STORY_NODE_V3.md` | Curators | Defines optional Focus Mode controls (`focus_center`, `focus_time`, `focus_layers`) |
| Web UI entry README | `web/README.md` | UI | UI boundary + build/run conventions *(not confirmed here)* |
| Cesium sub-area README | `web/cesium/README.md` | UI | This document |
| UI layer registries | `web/**/layers/**` | UI + Governance | Canonical UI registry location (per v13 blueprint) |
| UI schemas | `schemas/ui/` | Schemas/Contracts | JSON Schemas for layer registries (minimum contract set, if present) |
| API contracts | `src/server/contracts/**` | API | Contract-first boundary; UI consumes via typed clients |
| Story Nodes (canonical) | `docs/reports/story_nodes/**` | Curators | Served to UI via API context bundles |

### Definition of done (for this document)

- [ ] Front-matter complete + valid; `path` matches file location
- [ ] Constraints/invariants explicit (API boundary; provenance + sensitivity rules)
- [ ] Layer registry guidance references canonical paths (`web/**/layers/**`, `schemas/ui/**`) and marks uncertainties as **not confirmed in repo**
- [ ] Focus Mode integration notes include Story Node controls and provenance-linked requirements
- [ ] Validation steps are listed and repeatable (commands may be placeholders)
- [ ] Footer includes governance links (ROOT_GOVERNANCE / ETHICS / SOVEREIGNTY)

## 🗂️ Directory Layout

### This document

- `path`: `web/cesium/README.md` (must match front-matter)

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| Frontend (UI) | `web/` | React app, MapLibre map, optional Cesium 3D globe, Focus Mode UI |
| Cesium sub-area | `web/cesium/` | Cesium integration notes/config/adapters (this area) |
| Frontend runtime source | `web/src/` | React runtime: API clients, state, Focus Mode rendering *(not confirmed here)* |
| UI layer registry | `web/**/layers/**` | Declarative layer entries consumed by UI runtime |
| Schemas | `schemas/` | JSON Schemas (STAC/DCAT/PROV/storynodes/ui/telemetry) |
| UI schemas | `schemas/ui/` | Layer registry schema(s) |
| API boundary | `src/server/` | REST/GraphQL services, redaction, provenance linking |
| API contracts | `src/server/contracts/**` | Contract definitions + tests |
| Graph build/ingest | `src/graph/` | Ontology bindings + graph build/ingest code |
| Evidence catalogs | `data/stac/**` + `data/catalog/dcat/**` + `data/prov/**` | STAC/DCAT/PROV artifacts for traceability |
| Story Nodes | `docs/reports/story_nodes/**` | Draft/published narrative artifacts |
| CI | `.github/workflows/` | Markdown/schema/secret scanning and other gates |

### Expected file tree for this sub-area

> Target/typical layout. Keep this section updated if your actual tree differs.

~~~text
📁 web/
├── 📁 cesium/
│   ├── 📄 README.md
│   ├── 📁 layers/                    # optional (Cesium-specific registry overlays)
│   │   ├── 📄 <registry>.json         # example only — not confirmed in repo
│   ├── 📁 adapters/                  # optional (registry → Cesium mapping helpers)
│   ├── 📁 assets/                    # optional (presentation-only, public-safe assets)
│   └── 📁 test/                      # optional (fixtures/unit tests for adapters)
└── 📁 src/                           # main app runtime (React) — not confirmed here
~~~

## 🧭 Context

### Background

KFM’s canonical flow is preserved end-to-end:

**ETL → STAC/DCAT/PROV → Graph (Neo4j) → API → UI (web/) → Story Nodes → Focus Mode**

Cesium, if enabled, is a **UI-only rendering mode**. It must not introduce new “data authority” paths: all authoritative data remains produced upstream (ETL/catalog/graph) and delivered through contracted APIs and governed layer registries.

### Assumptions

- `web/` is a single-page application (SPA) that can toggle between:
  - a primary **2D map** mode (MapLibre or equivalent),
  - and an optional **3D** mode (Cesium).
- 2D ↔ 3D switching preserves user intent using deterministic state:
  - focused entity/story,
  - active layers,
  - time window (if applicable).
- Layer availability is configured via a registry (`web/**/layers/**` as canonical target), ideally schema-validated (`schemas/ui/**` if present).
- Focus Mode content arrives via an API “context bundle” that includes narrative + provenance links + structured map/timeline hints.

### Constraints / invariants

Non-negotiables:

- **No UI direct-to-graph reads:** `web/` must never query Neo4j directly; graph access is only via `src/server/`.
- **Contracts are canonical:**
  - API contracts live under `src/server/contracts/**`.
  - UI registry schemas live under `schemas/ui/**` (if present).
- **No duplicate homes for UI/API:** do not create/restore alternate top-level UI/API folders (e.g., legacy `src/map/` or `src/api/`); `web/` and `src/server/` are the canonical homes.
- **Provenance-first Focus Mode:** the UI must not present uncited narrative as fact. Focus Mode consumes only provenance-linked context.
- **Sensitive layers are governed:** the UI must respect sensitivity/redaction flags delivered by the API and/or registry, including “do not show”, “generalize geometry”, and “avoid precision tooltips”.
- **No secrets in repo:** Cesium Ion tokens, API keys, and provider credentials must not be committed. Use environment/runtime configuration patterns.

Implementation safety expectations:

- UI must not “reconstruct” restricted location detail client-side from generalized values.
- Any third-party tiles/terrain/assets must be:
  - declared in registries (not hard-coded in UI code),
  - attributed/licensed,
  - and reviewed for governance + data export risks.

### Open questions

| Question | Owner | Target date |
|---|---|---|
| Where is the canonical layer registry in this repo (target: `web/**/layers/**`)? | UI Team | TBD |
| Which schema files under `schemas/ui/**` validate the layer registry? | UI + Schemas | TBD |
| What is the canonical “Focus API” contract location/version used by the UI (target: `src/server/contracts/**`)? | API Team | TBD |
| Where does the Cesium runtime implementation live (under `web/src/**` vs `web/cesium/**`)? | UI Team | TBD |

### Future extensions

- Time-dynamic 3D layers (only if contracts + provenance are preserved).
- Story-driven camera tours that reference provenance-linked Story Nodes.
- Progressive enhancement: browsers without adequate WebGL still get a complete 2D experience.

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

  UI->>API: Focus query (entity_id, time_window)
  API->>Graph: Fetch subgraph + evidence refs (STAC/DCAT/PROV IDs)
  Graph-->>API: Context bundle + provenance identifiers
  API-->>UI: Contracted payload (narrative + citations + map/timeline hints)
  UI-->>UI: Optionally apply hints to Cesium camera + layers
~~~

## 📦 Data & Metadata

### Inputs

| Input | Format | Where from | Validation |
|---|---|---|---|
| UI layer registry entries | JSON | `web/**/layers/**` | JSON Schema under `schemas/ui/**` (if present) |
| Focus Mode context bundle | JSON | API boundary (`src/server/`) | API contract tests + runtime guards |
| Story Node optional focus controls | YAML/Front-matter | Story Nodes served via API | Template + schema validation (if present) |
| Evidence identifiers | IDs/URLs | STAC/DCAT/PROV artifacts via API | ID integrity + link validation at source |

### Outputs

| Output | Format | Path | Notes |
|---|---|---|---|
| Interactive 3D map experience | Runtime UI | `web/` | Presentation only; no authoritative data is authored here |
| Layer visibility/camera state | Runtime UI state | (runtime) | Must be deterministic; must not leak restricted detail |

### Sensitivity and redaction

- Treat registry + API-delivered sensitivity flags as authoritative.
- Do not encode restricted coordinates in client-side logs/telemetry.
- Avoid UI interactions that enable triangulation of redacted sites (e.g., repeated “center to feature” on generalized points).
- Prefer “coarse” UI affordances for restricted layers: bounding boxes, gridded heatmaps, or region-level labels.

### Quality signals

- Layer registries validate against `schemas/ui/**` (CI gate, if implemented).
- Focus Mode narrative renders with citations + audit affordances intact.
- 2D ↔ 3D toggling does not drop provenance context (sources/audit panel remains available).
- Performance budgets are respected (acceptable frame rate; reasonable tile/3D asset weight).

## 🌐 STAC, DCAT & PROV Alignment

This UI sub-area does **not** author catalogs; it consumes catalog and provenance artifacts.

Expected linkage for 3D-enabled assets:

- **STAC**: 3D tilesets / terrain / derived rasters should be cataloged as STAC Items with assets.
  - Canonical output paths (v13 target): `data/stac/collections/**` and `data/stac/items/**`.
- **DCAT**: dataset-level metadata and licensing remain accessible; UI surfaces attribution.
  - Canonical output path (v13 target): `data/catalog/dcat/**`.
- **PROV**: Focus Mode should be able to show “how this was made” (activity/run identifiers).
  - Canonical output path: `data/prov/**`.

If a 3D visualization depends on derived products, those products must live upstream (under `data/**`) and be referenced via catalogs and the API boundary.

## 🧱 Architecture

### Components

| Component | Responsibility | Interface |
|---|---|---|
| Cesium scene wrapper | Create/own Cesium Viewer/Scene lifecycle | UI state + runtime config |
| Layer registry loader | Load + validate registries | `web/**/layers/**` + `schemas/ui/**` |
| Cesium layer adapter(s) | Map registry entry → Cesium primitive(s) | Typed adapter per `kind` |
| Camera/time synchronizer | Keep Focus Mode intent consistent across 2D/3D | Focus hints (center/time/layers) |
| API client | Fetch focus bundles + layer metadata | Contracted REST/GraphQL |

### Interfaces / contracts

| Contract | Location | Versioning rule |
|---|---|---|
| UI layer registry schema | `schemas/ui/**` | Semver + schema validation |
| API contracts | `src/server/contracts/**` | Semver + contract tests |
| Story Node template/schema | `docs/templates/TEMPLATE__STORY_NODE_V3.md` + `schemas/storynodes/**` | Validate before publish *(schema path may be missing in repo)* |
| Focus bundle payload | API contract | Backward compatible or version bump |

### Network boundary rules for Cesium

To preserve the API boundary and governance controls:

- **Do not hard-code** data URLs in Cesium components.
- All network sources used by 3D mode must be declared via:
  1) UI layer registries (`web/**/layers/**`), and/or  
  2) API-delivered layer manifests / context bundles.
- Any third-party providers must include:
  - attribution + license metadata,
  - a sensitivity classification,
  - and (where possible) an allowlist/CSP entry at the app level.

### Cesium configuration & secrets

- Treat Cesium Ion tokens (and any imagery/terrain provider keys) as secrets:
  - do not commit tokens,
  - do not embed tokens in registries committed to git.
- Prefer KFM-owned 3D assets and endpoints where access, attribution, and redaction can be enforced consistently.
- If a client-visible token is unavoidable, restrict it by domain and scope, and treat it as environment-specific configuration.

### Layer type mapping (conceptual)

> Illustrative only — confirm the canonical `kind` values in `schemas/ui/**`.

| Registry `kind` | Cesium primitive(s) | Notes |
|---|---|---|
| `3dtiles` | `Cesium3DTileset` | For 3D Tiles tilesets (buildings, meshes, point clouds) |
| `terrain` | `TerrainProvider` | Prefer governed terrain endpoints; avoid leaking precision where restricted |
| `imagery` | `ImageryProvider` + `ImageryLayer` | Include attribution and licensing |
| `entities` | `EntityCollection` | For simple points/lines/polygons with governance constraints |
| `czml` | `CzmlDataSource` | For time-dynamic narratives; requires careful provenance linkage |

### Adding a new Cesium-capable layer (checklist)

1) Add/modify a layer entry in the canonical registry (`web/**/layers/**`).
2) Validate the registry entry against `schemas/ui/**` (if present).
3) Ensure the underlying data source is served via the API boundary (or other governed endpoints), with redaction/sensitivity applied.
4) Ensure attribution and licensing metadata are present (registry and/or API payload).
5) Add/extend the Cesium adapter to support the layer type (if new).
6) Add tests:
   - registry parsing + schema validation (unit),
   - adapter mapping (unit),
   - Focus Mode + 2D/3D toggle (E2E).

Illustrative example only (confirm exact schema fields under `schemas/ui/**`):

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

### Focus Mode flow (UI behavior)

A typical Focus Mode flow is:

1) user selects an entity or Story Node,
2) UI enters Focus Mode with that entity ID,
3) UI requests a **context bundle** from the API (“Focus API”),
4) UI renders narrative + citations + provenance panel,
5) UI optionally applies map/timeline hints to 2D or 3D mode.

### Optional Focus Mode controls from Story Nodes

The Story Node template supports optional controls that can assist map/timeline synchronization:

~~~yaml
focus_layers:
  - "TBD"
focus_time: "TBD"
focus_center: [-98.0000, 38.0000] # lon, lat (example only)
~~~

Rules for consuming these hints:

- Treat them as **hints**, not mandates (users can override).
- Respect sensitivity/redaction constraints (do not “zoom to” restricted detail).
- Preserve intent when toggling 2D ↔ 3D (do not drop Focus Mode context or sources panel).

### Rendering Story Node citations

Story Nodes are Markdown and may embed citations in the `【source†Lx-Ly】` style. The UI should render these as interactive references (links/popovers/sources panel), not as plain text.

### AI-derived content (if present)

If AI-generated explanations are exposed in the UI:

- they must be **opt-in**,
- clearly labeled as AI-generated,
- accompanied by uncertainty/confidence metadata,
- and never presented as unmarked fact.

## 🧪 Validation & CI/CD

### Validation steps (recommended)

- [ ] Markdown protocol checks (front-matter + required sections)
- [ ] UI schema checks (layer registries validate against `schemas/ui/**`, if present)
- [ ] Frontend unit tests for:
  - registry parsing,
  - Cesium adapter mapping,
  - Focus Mode rendering (narrative + citations)
- [ ] E2E flow tests:
  - enter/exit Focus Mode,
  - toggle 2D/3D,
  - enable/disable Cesium layers,
  - verify sources panel remains present and correct
- [ ] Security checks:
  - secret scan (tokens/keys),
  - link/reference checks (no orphan pointers),
  - telemetry redaction checks (no sensitive coordinates)

### Reproduction (placeholders)

~~~bash
# Replace with repo-specific commands (see web/README.md or web/package.json scripts)

# validate ui schemas
# run unit tests
# run e2e tests
# run markdown lint / protocol checks
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
- Any UI change that could enable inference of restricted locations through interaction/zoom.

### CARE / sovereignty considerations

- Do not expose restricted locations or culturally sensitive knowledge.
- Enforce generalization/redaction at the API layer; ensure the UI respects gating flags in registry entries and payloads.
- If uncertain, treat the layer as higher sensitivity until governance review resolves classification.

### Third-party services & licensing

- Ensure registries or UI copy surface required attributions.
- Do not “bake in” third-party data products into UI artifacts without catalog/provenance.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-21 | Initial `web/cesium/README.md` | TBD |
| v1.0.1 | 2025-12-24 | Clarified optional 3D role; strengthened invariants; tightened registry guidance | TBD |
| v1.0.2 | 2025-12-26 | Aligned with Universal template wording; clarified canonical paths (`web/**/layers/**`, `schemas/ui/**`); added network-boundary rules and Story Node focus controls | TBD |

---

### Footer refs (do not remove)

- Master guide: `docs/MASTER_GUIDE_v12.md`
- v13 blueprint (if adopted): `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md`
- Universal template: `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`
- Story Node template: `docs/templates/TEMPLATE__STORY_NODE_V3.md`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
