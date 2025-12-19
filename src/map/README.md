---
title: "KFM — src/map (Map Subsystem) README"
path: "src/map/README.md"
version: "v0.1.0"
last_updated: "2025-12-19"
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

doc_uuid: "urn:kfm:doc:src:map:readme:v0.1.0"
semantic_document_id: "kfm-src-map-readme-v0.1.0"
event_source_id: "ledger:kfm:doc:src:map:readme:v0.1.0"
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

# src/map

## 📘 Overview

### Purpose
`src/map/` is the **code + contracts hub** for *map-related domain logic* that supports the KFM pipeline end-to-end—especially anything that turns cataloged assets into **map-ready artifacts** (styles, layer manifests, time-slicing helpers, projection utilities, validation).

This README is intentionally conservative: the exact internal module layout of `src/map/` is **not confirmed in repo** from the available materials. Treat this as the **governed intent** for the folder; update it once concrete packages/files exist.

### Scope

| In Scope | Out of Scope |
|---|---|
| Map-domain utilities (CRS/projection helpers, bbox/time window helpers) | Rendering UI components (those belong in `web/`) |
| Layer/layer-manifest modeling + validation (schema-first) | Direct UI access to Neo4j (must go via APIs) |
| Packaging map-ready artifacts from cataloged assets (e.g., style JSON, TileJSON pointers) | “Undocumented” layers that cannot be traced to STAC/DCAT/PROV |
| Guardrails for sensitive layers (redaction/generalization hooks) | Any policy generation (governed elsewhere) |

### Audience
- Primary: engineers working on map-related backend/shared logic (layer manifests, validation, map contracts)
- Secondary: data/geo engineers producing STAC assets that must render correctly in the UI
- Tertiary: QA and governance reviewers validating provenance + sensitivity controls

### Definitions (link to glossary)
- Link: `docs/glossary.md` (**not confirmed in repo**)
- Terms used in this doc: layer registry, style JSON, TileJSON, bbox, CRS, MapLibre, Cesium, time-slicing

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Canonical pipeline order | `docs/MASTER_GUIDE_v12.md` | Core maintainers | ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode |
| Map UI implementation | `web/` | UI team | UI uses contracts via APIs (no direct graph reads) |
| Layer registry (example) | `web/cesium/layers/regions.json` | UI team | Referenced in governed template; actual location may differ (**verify**) |
| Map contracts/schemas | `schemas/` | Platform team | Add JSON schemas here (if/when defined) |
| STAC catalogs | `data/stac/` | DataOps | Map-visible assets must resolve to STAC items/collections |
| Provenance bundles | `data/prov/` | DataOps | Map-ready artifacts should be traceable via PROV |

### Definition of done (for this document)
- [ ] Front-matter complete + valid
- [ ] Any claims about paths/components are either verified or marked “not confirmed in repo”
- [ ] Explicitly preserves: ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode
- [ ] Mentions API boundary (UI never reads Neo4j directly)
- [ ] Validation steps listed and repeatable
- [ ] Sensitivity and redaction hooks are acknowledged

## 🗂️ Directory Layout

### This document
- `path`: `src/map/README.md`

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| Data domains | `data/` | Raw/work/processed/stac outputs |
| Catalogs | `data/stac/` + `data/catalog/dcat/` | STAC Items/Collections + DCAT |
| Provenance | `data/prov/` | PROV lineage bundles |
| Graph | `src/graph/` | Ontology + graph build/migrations |
| APIs | `src/api/` or `src/server/` (**not confirmed in repo**) | Contracted access layer |
| Frontend | `web/` | React + MapLibre/Cesium UI |
| Story Nodes | `docs/reports/.../story_nodes/` | Narrative artifacts w/ provenance |

### Expected file tree for this sub-area
~~~text
📁 src/
└── 📁 map/
    ├── 📄 README.md
    ├── 📁 contracts/            # (optional) map payload types + validators (not confirmed in repo)
    ├── 📁 layers/               # (optional) layer manifest builders / resolvers (not confirmed in repo)
    ├── 📁 styles/               # (optional) style JSON generators/linters (not confirmed in repo)
    ├── 📁 time/                 # (optional) time filtering helpers (not confirmed in repo)
    ├── 📁 projection/           # (optional) CRS/projection utilities (not confirmed in repo)
    └── 📁 __tests__/            # (optional) unit tests for utilities (not confirmed in repo)
~~~

## 🧭 Context

### Background
KFM is a geospatial + historical knowledge system where users explore places and time on a map UI. The canonical system ordering is governed (ETL → catalogs → graph → APIs → UI → story/focus). Any map-facing content must be provenance-linked and contract-served through APIs.

### Assumptions
- The map UI is implemented in `web/` (React + MapLibre/Cesium are referenced in governed materials).
- `src/map/` exists to keep **non-UI map logic** cohesive and testable (e.g., schema validation, layer manifests, temporal slicing).
- Exact file layout is **not confirmed in repo** yet.

### Constraints / invariants
- Canonical pipeline ordering is preserved.
- Frontend consumes contracts via APIs (**no direct graph dependency**).
- Anything rendered on the map should be traceable to STAC/DCAT/PROV references.
- Determinism: if `src/map/` builds artifacts, outputs should be reproducible from the same inputs + config.

### Open questions

| Question | Owner | Target date |
|---|---|---|
| Does `src/map/` primarily support backend/API, pipelines, or shared libs consumed by `web/`? | TBD | TBD |
| Where is the authoritative layer registry in this repo (e.g., `web/.../layers.json`)? | TBD | TBD |
| Are map contracts defined in OpenAPI/GraphQL, JSON schema, or both? | TBD | TBD |

### Future extensions
- Extension point A: schema-validated “layer manifests” that bind a UI layer to STAC item(s)/collection(s) and PROV run IDs.
- Extension point B: reusable time-slicing utilities (global timeline ↔ layer availability).
- Extension point C: sensitivity gating helpers (public vs restricted layers; generalized geometry outputs).

## 🗺️ Diagrams

### System / dataflow diagram
~~~mermaid
flowchart LR
  A[Cataloged assets<br/>STAC/DCAT] --> B[src/map<br/>manifest + validation]
  B --> C[API payloads<br/>contracted]
  C --> D[web/ UI<br/>MapLibre/Cesium]
  D --> E[Story Nodes + Focus Mode<br/>provenance-linked]
~~~

### Optional: sequence diagram
~~~mermaid
sequenceDiagram
  participant UI as web/ UI
  participant API as API Layer
  participant Catalog as STAC/DCAT
  UI->>API: request layers for (bbox, time)
  API->>Catalog: resolve STAC items/collections + provenance refs
  Catalog-->>API: asset refs + metadata
  API-->>UI: contracted layer payload + provenance
~~~

## 📦 Data & Metadata

### Inputs

| Input | Format | Where from | Validation |
|---|---|---|---|
| Catalog references | STAC JSON, DCAT | `data/stac/`, `data/catalog/dcat/` | STAC/DCAT validators |
| Map assets | GeoJSON, COG/GeoTIFF, MBTiles, images | `data/processed/` + assets referenced by STAC | Geometry validity, link checks |
| Time metadata | ISO timestamps/ranges | STAC properties, dataset metadata | Range sanity + ordering |

### Outputs

| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Layer manifest(s) | JSON | `data/processed/` or `web/` (**not confirmed**) | JSON schema (define under `schemas/`) |
| Style configs | JSON | `web/` or `src/map/styles/` (**not confirmed**) | Style schema / lints |
| API payloads | JSON | served | OpenAPI/GraphQL contracts |

### Sensitivity & redaction
- Some layers may require:
  - generalized geometry (reduce precision / aggregate regions)
  - time window generalization
  - access gating (RBAC) at the API layer
- Never leak restricted layers via “hidden but fetchable” endpoints.

### Quality signals
- Geometry validity: no self-intersections where invalid, valid bbox extents, consistent CRS.
- Temporal consistency: time ranges valid and comparable across layers.
- Link integrity: no broken STAC asset links for map-visible layers.
- Determinism: same inputs/config → same outputs (hashable artifacts).

## 🌐 STAC, DCAT & PROV Alignment

### STAC
- Collections involved: TBD
- Items involved: TBD
- Extension(s): TBD

### DCAT
- Dataset identifiers: TBD
- License mapping: TBD
- Contact / publisher mapping: TBD

### PROV-O
- `prov:wasDerivedFrom`: source item IDs (STAC/DCAT)
- `prov:wasGeneratedBy`: pipeline activity/run ID
- Activity / Agent identities: pipeline runner + versioned configs

### Versioning
- Use STAC Versioning links and graph predecessor/successor relationships as applicable.

## 🧱 Architecture

### Components

| Component | Responsibility | Interface |
|---|---|---|
| `src/map` utilities | Map-domain logic (bbox/time/CRS), manifest validation | Imported by pipelines/APIs |
| Catalogs | Provide asset metadata + time/space coverage | STAC/DCAT/PROV JSON |
| APIs | Serve contracted payloads for UI | REST/GraphQL |
| UI (`web/`) | Render layers, timeline, narrative affordances | API calls only |

### Interfaces / contracts

| Contract | Location | Versioning rule |
|---|---|---|
| JSON schemas | `schemas/` | Semver + changelog |
| API schemas | `src/server/` + docs (**not confirmed**) | Contract tests required |
| Layer registry | `web/cesium/layers/regions.json` (**verify**) | Schema-validated |

### Extension points checklist (for future work)
- [ ] Data: new domain added under `data/<domain>/...`
- [ ] STAC: new collection + item schema validation
- [ ] PROV: activity + agent identifiers recorded
- [ ] Graph: new labels/relations mapped + migration plan
- [ ] APIs: contract version bump + tests
- [ ] UI: layer registry entry + access rules
- [ ] Focus Mode: provenance references enforced
- [ ] Telemetry: new signals + schema version bump

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode
- Map interactions in Focus Mode should only show layers and evidence that have resolvable provenance references (STAC/DCAT/PROV and/or document IDs).
- If `src/map` contributes layer manifests, it should ensure every layer is mappable back to catalog IDs.

### Provenance-linked narrative rule
- Every claim must trace to a dataset / record / asset ID.

### Optional structured controls
~~~yaml
focus_layers:
  - "TBD"
focus_time: "TBD"
focus_center: [ -98.0000, 38.0000 ]
~~~

## 🧪 Validation & CI/CD

### Validation steps
- [ ] Markdown protocol checks
- [ ] Schema validation (STAC/DCAT/PROV) for any map-visible assets
- [ ] Link integrity checks for STAC assets used by map layers
- [ ] Geometry validity checks (GeoJSON validity, CRS sanity)
- [ ] API contract tests (payload shape + redaction rules)
- [ ] UI layer registry schema checks (if applicable)
- [ ] Security + sovereignty checks (if applicable)

### Reproduction
~~~bash
# Example placeholders — replace with repo-specific commands
# 1) validate catalogs (STAC/DCAT/PROV)
# 2) run map contract/manifest tests
# 3) run API contract tests
# 4) run doc lint
~~~

### Telemetry signals (if applicable)

| Signal | Source | Where recorded |
|---|---|---|
| Map layer load failures | UI logs / integration tests | `docs/telemetry/` + `schemas/telemetry/` |
| Broken asset links | CI link-check job | CI logs + report artifact |
| Redaction/gating enforcement | API audit logs | `docs/telemetry/` (aggregated) |

## ⚖ FAIR+CARE & Governance

### Review gates
- Map layers that change public-facing narratives or add new external data sources require governance review (per repo governance docs).
- Sensitive layers require explicit sovereignty handling and approval.

### CARE / sovereignty considerations
- Identify any culturally sensitive locations and apply generalization/redaction rules.
- Ensure restricted access is enforced at the API layer and reflected in UI affordances.

### AI usage constraints
- This README does not authorize new AI behaviors.
- Ensure any AI-derived “map evidence artifacts” remain provenance-linked and opt-in where predictive.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v0.1.0 | 2025-12-19 | Initial scaffold for `src/map` README | TBD |

---
Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
