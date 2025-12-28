---
title: "Web Layers — Registry, Styles, and Governance"
path: "web/layers/README.md"
version: "v1.0.0"
last_updated: "2025-12-27"
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

doc_uuid: "urn:kfm:doc:web:layers:readme:v1.0.0"
semantic_document_id: "kfm-web-layers-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:web:layers:readme:v1.0.0"
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

# Web Layers — Registry, Styles, and Governance

This directory defines **what map layers exist in the Web UI**, **where their data comes from (via contracted APIs and/or versioned artifacts)**, and **how they are styled and governed**.

It is the UI-side contract within the canonical pipeline ordering:

**ETL → STAC/DCAT/PROV catalogs → Neo4j graph → APIs → React/Map UI → Story Nodes → Focus Mode**

---

## 📘 Overview

### Purpose
- Provide a **schema-validated layer registry** that the Web UI can load at runtime to render MapLibre layers (and, if present, Cesium layers).
- Centralize **layer styling and legends** so map rendering is deterministic, reviewable, and versioned.
- Ensure each layer can surface **audit affordances** (license, attribution, provenance pointers) and comply with **FAIR+CARE / sovereignty** constraints.

### Scope

| In Scope | Out of Scope |
|---|---|
| Layer registry format + semantics (IDs, required fields, evolution rules) | Building ETL/pipelines that generate artifacts |
| Style fragments, legends, icons used by the UI | Defining ontology labels/edges (graph design) |
| Provenance pointers (STAC/DCAT/PROV refs) exposed to the UI | API implementation details beyond the UI contract |
| Validation expectations for layer changes (CI gates) | Cloud deployment specifics (CDN, object storage configs) |

### Audience
- Primary: Web UI developers (React/MapLibre; optional Cesium)
- Secondary: API developers (tiles/features), catalog maintainers (STAC/DCAT/PROV), governance reviewers

### Definitions
Glossary: `docs/glossary.md` (if missing, treat as a repo gap to be resolved under `docs/`).  
Terms used in this doc:
- **Layer registry**: JSON configs enumerating what layers exist and how to load/style them.
- **Layer entry**: A layer definition with stable `id`, data source, style references, and governance metadata.
- **Audit affordances**: UI-visible metadata (license/attribution/provenance/vintage) that supports review and traceability.
- **Redaction/generalization**: Measures that prevent sensitive locations or restricted knowledge from being exposed by geometry, zoom, or interaction.

### Key artifacts

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master guide | `docs/MASTER_GUIDE_v12.md` | Core maintainers | Canonical pipeline ordering + invariants |
| Redesign blueprint | `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md` | Core maintainers | Canonical homes + CI gates + repo lint |
| Universal doc template | `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` | Docs maintainers | This README follows the Universal governed structure |
| Story Node template | `docs/templates/TEMPLATE__STORY_NODE_V3.md` | Narrative/curation | Story/Focus-mode linkage patterns |
| API contract extension template | `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md` | API maintainers | Use when a layer requires new endpoints/contracts |
| UI schemas | `schemas/ui/` (**not confirmed in repo**) | UI + platform | v13 blueprint expects schema validation for layer registries |

### Definition of done
- [ ] Front-matter complete + valid
- [ ] Layer registry contract described (minimum required fields + evolution rules)
- [ ] Styling + legend + accessibility guidance included
- [ ] Provenance mapping (STAC/DCAT/PROV) described
- [ ] Validation steps listed and repeatable
- [ ] Governance + CARE/sovereignty considerations explicitly stated

---

## 🗂️ Directory Layout

### This document
- `path`: `web/layers/README.md` (must match front-matter)

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| Web UI | `web/` | React app + MapLibre components; optional Cesium |
| UI layer registries | `web/**/layers/**` | Layer registry JSON configs + related UI assets |
| Schemas | `schemas/` (**not confirmed in repo**) | JSON schemas (STAC/DCAT/PROV/story/UI/telemetry) |
| API boundary | `src/server/` | Versioned REST/GraphQL endpoints; policy enforcement |
| API contracts | `src/server/contracts/` (**not confirmed in repo**) | OpenAPI/GraphQL contracts; contract tests |
| STAC outputs | `data/stac/` | STAC collections + items for datasets/artifacts |
| DCAT outputs | `data/catalog/dcat/` | DCAT dataset/distribution metadata |
| PROV outputs | `data/prov/` | Lineage bundles linking raw→work→processed→published |
| Story Nodes | `docs/reports/story_nodes/` | Draft + published Story Nodes (if split exists) |

### Expected structure in this directory
Recommended target (align with the repo’s existing layout if it differs):

~~~text
📁 web/
└── 📁 layers/
    ├── 📄 README.md
    ├── 📁 registries/
    │   ├── 📄 layers.base.json
    │   ├── 📄 layers.overlays.json
    │   └── 📄 layers.sensitive.json
    ├── 📁 styles/
    │   ├── 📄 base.style.json
    │   └── 📁 fragments/
    │       └── 📄 <layer_id>.style.json
    ├── 📁 legends/
    │   ├── 📄 <layer_id>.legend.json
    │   └── 📁 icons/
    │       └── 📄 <icon>.svg
    └── 📁 icons/
        └── 📄 <layer_id>.svg
~~~

Notes:
- Some KFM docs cite `web/cesium/layers/regions.json` (or `web/cesium/layers/*.json`) as an example registry home. If those paths exist in your repo, treat them as **supported legacy locations** and use explicit deprecation markers if you relocate or consolidate.

---

## 🧭 Context

### Canonical pipeline and UI boundary
KFM is contract-first and evidence-first. The UI must be a consumer of **versioned artifacts** and **contracted APIs**.

Non-negotiable invariants for layers:
1. **No UI direct-to-graph reads**: the UI must never query Neo4j directly; all graph access is via the API boundary (`src/server/`).  
2. **UI reads only from API endpoints and catalog endpoints**: tiles/features and catalog/provenance references are served through governed interfaces.  
3. **Provenance-first**: a layer must be able to surface STAC/DCAT/PROV references for audit and Focus Mode evidence linking.
4. **No hidden data leakage**: sensitivity and redaction must be enforced at the API boundary and reflected in UI presentation; UI must not enable re-identification via interaction/zoom.
5. **Backward-compatible evolution**: adding registry fields should be non-breaking; breaking changes require a coordinated version bump.

### Why a layer registry exists
A single registry provides:
- Deterministic layer behavior (ordering, default visibility, min/max zoom).
- A consistent place to attach governance metadata (license, attribution, sensitivity).
- A reliable UI surface for audit panels and Focus Mode evidence linkage.
- A CI target: validate registries against schemas and ensure referenced assets/endpoints exist.

### Layer lifecycle
Adding a layer usually spans multiple subsystems:

1. **Data artifact exists** (processed + published form)  
   Examples: PMTiles/MBTiles, COG, GeoParquet, or a service-backed product.
2. **Catalog metadata exists**  
   STAC item(s) + DCAT dataset + PROV activity bundle.
3. **API surface exists**  
   Tile/feature endpoints are versioned and contract-tested; policy enforcement occurs here.
4. **UI registry entry exists**  
   Registry points to API endpoints (and/or immutable artifacts) + style fragment + legend.
5. **Governance gate passes**  
   Sensitivity classification, redaction notes, sovereignty rules, and licensing are reviewed.
6. **Story Nodes reference the layer** (optional)  
   Story Nodes cite evidence IDs; Focus Mode enforces provenance-only context.

### Naming and versioning conventions
- **Layer `id` must be stable** (referenced by UI state, Story Nodes, telemetry).
- Prefer **kebab-case** IDs and filenames: `surficial-geology`, `hydro-network`, `air-sensors`.
- Prefer **versioned sources** (immutable URLs or STAC asset hrefs with digests) over “latest” URLs.
- Deprecate layers explicitly (for example, a `deprecated: true` marker or an `end_of_life` date) rather than removing entries silently.

---

## 🗺️ Diagrams

### System dataflow diagram

~~~mermaid
flowchart LR
  subgraph Data
    A["Raw sources"] --> B["ETL + Normalization"]
    B --> C["Processed datasets"]
    C --> D["STAC Items + Collections"]
    C --> E["DCAT Dataset Views"]
    C --> F["PROV Lineage Bundles"]
  end

  D --> G["Neo4j Graph"]
  G --> H["API Layer (REST/GraphQL)"]
  H --> I["Web UI (React/MapLibre/Cesium)"]
  I --> J["Story Nodes"]
  J --> K["Focus Mode"]
~~~

### Sequence diagram for toggling a layer

~~~mermaid
sequenceDiagram
  participant User
  participant UI as Web UI
  participant Reg as Layer Registry (JSON)
  participant API as API (tiles/features)
  participant Cat as Catalog refs (STAC/DCAT/PROV)

  User->>UI: Toggle layer ON
  UI->>Reg: Load layer entry by id
  Reg-->>UI: source + style + governance metadata
  UI->>API: Request tiles/features per layer source
  API-->>UI: Tile data / feature payload
  UI->>Cat: Resolve provenance pointers for audit panel
  Cat-->>UI: STAC/DCAT/PROV refs (IDs and/or resolvable links)
  UI-->>User: Render layer + show attribution/audit affordances
~~~

---

## 📦 Data & Metadata

### Layer types supported by the registry
At minimum, the registry should be able to describe:
- **Vector tiles (MVT)**: UI renders geometry + labels via style rules.
- **Raster tiles / rasters**: UI renders imagery with colormaps (when applicable).
- **Feature services**: UI queries features for popups, filters, and charts.
- Optional (if present in repo): WMS/WMTS, 3D tiles, time-enabled layers.

### Inputs

| Input | Format | Where from | Validation |
|---|---|---|---|
| Layer registry | JSON | `web/**/layers/**` | JSON schema in `schemas/ui/` (if present) |
| Style fragments | JSON | `web/layers/styles/**` | File exists + MapLibre style spec validation (as configured) |
| Legends | JSON | `web/layers/legends/**` | File exists + legend schema (if present) |
| Icons | SVG/PNG | `web/layers/icons/**` | File exists + size/a11y conventions (as configured) |
| Tiles/features | HTTP | `src/server/` endpoints | API contract tests + policy/redaction enforcement |

### Outputs

| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Rendered map layers | Runtime | Web UI | Registry + styles must be deterministic |
| Attribution + license display | UI panel | Web UI | Must match registry fields and upstream licensing |
| Provenance panel content | UI panel | Web UI | Must resolve to STAC/DCAT/PROV IDs/links |
| Telemetry events | Events/logs | `docs/telemetry/` + `schemas/telemetry/` (**not confirmed in repo**) | Schema validated if adopted |

### Sensitivity and redaction
- Any layer that could reveal restricted or culturally sensitive locations must document:
  - what is redacted/generalized,
  - at what zoom levels or interactions risk exists,
  - which enforcement layer applies the protection (API, catalog, UI).
- “Fail closed”: if a layer’s sensitivity cannot be determined, do not include it in public registries.

### Quality signals
- Registry completeness: required fields present for each layer.
- Link integrity: referenced local assets and API endpoints exist.
- Geometry/render integrity: style fragments do not reference missing sources or layers.
- Audit completeness: license, attribution, and provenance pointers are present and consistent.

### Performance notes
- Prefer CDN-cacheable, versioned artifacts for layers that update daily/weekly/monthly.
- Prefer TileJSON endpoints for tileset discovery and consistent attribution surfaces.
- For point layers, prefer UI-driven clustering (where appropriate) rather than baking clusters into tiles.

---

## 🌐 STAC, DCAT & PROV Alignment

### STAC
- Collections involved: referenced via `data.stac.collection_id` (or equivalent)
- Items involved: referenced via `data.stac.item_id` (or equivalent)
- Assets: if a layer is backed by an immutable artifact, reference the asset key/href in STAC where feasible

### DCAT
- Dataset identifiers: referenced via `data.dcat.dataset_id` (or URI)
- License mapping: registry `license` and `attribution` should align with DCAT dataset/distribution metadata
- Publisher/contact mapping: sourced from DCAT where available; surface in the UI audit panel as needed

### PROV-O
- `prov:wasDerivedFrom`: implied by catalog lineage; registry stores pointers to PROV activity/entity IDs
- `prov:wasGeneratedBy`: `data.prov.activity_id` should identify the run/activity that produced the layer artifact
- Activity/Agent identities: include agent identifiers when available (e.g., pipeline ID, contributor ID)

### Versioning
- Prefer explicit version lineage:
  - STAC versioning links (predecessor/successor)
  - Graph predecessor/successor relationships (when modeled)
- Avoid unversioned “latest” layer sources unless explicitly intended and governed.

### Recommended registry fields for evidence linkage
A layer entry should include:
- STAC: `data.stac.collection_id`, `data.stac.item_id`
- DCAT: `data.dcat.dataset_id`
- PROV: `data.prov.activity_id` (and optional agent reference)

### Mapping table

| Layer registry field | Maps to | Purpose |
|---|---|---|
| `id` | Stable UI contract key | Used by toggles, telemetry, Story Nodes |
| `data.api.*` | API endpoints | Where tiles/features come from |
| `data.stac.*` | STAC collection/item IDs | Artifact traceability |
| `data.dcat.*` | DCAT dataset/distribution | Licensing + publisher + discovery |
| `data.prov.*` | PROV activity/entity IDs | Lineage + reproducibility |
| `license` + `attribution` | DCAT + upstream manifest | Legal/ethical display + reuse rules |
| `governance.*` | Governance policy | Prevent sensitive location leakage |

---

## 🧱 Architecture

### Subsystem contracts

| Subsystem | Contract artifacts | Do not break rule |
|---|---|---|
| ETL | configs + run logs + validation | deterministic, replayable |
| Catalogs | STAC/DCAT/PROV schemas + validators | machine-validated |
| Graph | ontology + migrations + constraints | stable labels/edges |
| APIs | OpenAPI/GraphQL schema + tests | backward compat or version bump |
| UI | layer registry + a11y + audit affordances | no hidden data leakage |
| Focus Mode | provenance-linked context bundle | no hallucinated sources |

### Components

| Component | Responsibility | Interface |
|---|---|---|
| Layer registry loader | Load and validate registry JSON | JSON schema in `schemas/ui/` (if present) |
| Style composer | Compose MapLibre style from base + fragments | MapLibre style spec JSON |
| Legend renderer | Render legend + icons consistently | Legend JSON + SVG/PNG assets |
| Layer toggle UI | Toggle visibility, ordering, filters | React components + state |
| Audit/provenance panel | Show license/attribution + STAC/DCAT/PROV refs | Registry fields + catalog fetch |
| API clients | Fetch tiles/features | Versioned REST endpoints |

### Interfaces and contracts

| Contract | Location | Versioning rule |
|---|---|---|
| JSON schemas | `schemas/` | Semver + changelog |
| API schemas | `src/server/` + docs | Contract tests required |
| Layer registry | `web/**/layers/**` (or legacy `web/cesium/layers/**`) | Schema-validated |

### Registry format
The schema in `schemas/ui/` is the source of truth when present. Until then, treat the following as the minimum contract expectations for each layer entry:
- Stable identifiers: `id`, `title`, `kind`
- UI controls: default visibility, zoom constraints, ordering, legend/style references
- Data source: versioned API endpoints (tiles/features) and/or immutable artifact pointers
- Evidence pointers: STAC/DCAT/PROV identifiers
- Governance metadata: sensitivity/classification/redaction notes and CARE notes

### Example minimal registry file

~~~json
{
  "schema_version": "KFM-UI-LAYER-REGISTRY v1",
  "generated_at": "2025-12-27T00:00:00Z",
  "layers": [
    {
      "id": "surficial-geology",
      "title": "Surficial Geology",
      "kind": "vector-tiles",
      "ui": {
        "default_visible": false,
        "minzoom": 4,
        "maxzoom": 12,
        "legend_ref": "legends/surficial-geology.legend.json",
        "style_ref": "styles/fragments/surficial-geology.style.json"
      },
      "data": {
        "api": {
          "tilejson": "/api/v1/tiles/surficial-geology/tilejson.json"
        },
        "stac": {
          "collection_id": "soils-and-geology",
          "item_id": "surficial-geology-v2025-10"
        },
        "dcat": {
          "dataset_id": "dcat:surficial-geology"
        },
        "prov": {
          "activity_id": "prov-geology-2025-10-01-abc123"
        },
        "license": "CC-BY-4.0",
        "attribution": "Source: <publisher>; Processed by KFM"
      },
      "governance": {
        "sensitivity": "public",
        "classification": "open",
        "redaction": "none",
        "care_notes": "TBD"
      }
    }
  ]
}
~~~

### Example MapLibre style fragment

~~~json
{
  "id": "surficial-geology-fill",
  "type": "fill",
  "source": "surficial-geology",
  "source-layer": "surficial_geology",
  "minzoom": 4,
  "maxzoom": 12,
  "paint": {
    "fill-opacity": 0.6
  }
}
~~~

### Example legend file

~~~json
{
  "layer_id": "surficial-geology",
  "title": "Surficial Geology",
  "items": [
    { "label": "Unit A", "symbol": { "type": "swatch", "value": "TBD" } },
    { "label": "Unit B", "symbol": { "type": "swatch", "value": "TBD" } }
  ],
  "notes": "Legend symbols should be accessible and match style rules."
}
~~~

### Extension points checklist
- [ ] Data: new domain added under `data/<domain>/...`
- [ ] STAC: new collection + item schema validation
- [ ] PROV: activity + agent identifiers recorded
- [ ] Graph: new labels/relations mapped + migration plan
- [ ] APIs: contract version bump + tests
- [ ] UI: layer registry entry + access rules
- [ ] Focus Mode: provenance references enforced
- [ ] Telemetry: new signals + schema version bump

---

## 🧠 Story Node and Focus Mode Integration

### How this work surfaces in Focus Mode
- Layers can be referenced as evidence by `layer_id` and used to pre-configure the map for a story.
- Focus Mode should be able to surface, for any enabled layer:
  - license/attribution,
  - data vintage/updated-at,
  - STAC/DCAT/PROV identifiers,
  - sensitivity/redaction notes.

### Provenance-linked narrative rule
- Focus Mode only consumes provenance-linked content.
- Any derived or inferred layer must include uncertainty metadata and a clear provenance chain.

### Optional structured controls

~~~yaml
focus_layers:
  - "surficial-geology"
  - "hydro-network"
focus_time: "2025-10-01"
focus_center: [-98.0000, 38.0000]
~~~

---

## 🧪 Validation and CI/CD

### Validation steps
- [ ] Markdown protocol checks
- [ ] Schema validation (STAC/DCAT/PROV)
- [ ] Graph integrity checks
- [ ] API contract tests
- [ ] UI schema checks (layer registry)
- [ ] Security and sovereignty checks (as applicable)

### Reproduction

~~~bash
# Example placeholders — replace with repo-specific commands

# 1) validate schemas (UI registries, STAC/DCAT/PROV, etc.)

# 2) run web lint/tests

# 3) run link-check / markdown lint (if configured)
~~~

### Telemetry signals
If telemetry is implemented, consider recording (schema-versioned) signals such as:

| Signal | Source | Where recorded |
|---|---|---|
| `ui.layer.toggle` | UI toggle component | `docs/telemetry/` + `schemas/telemetry/` |
| `ui.layer.load_error` | Registry/API client | `docs/telemetry/` + `schemas/telemetry/` |
| `ui.audit_panel.open` | Audit panel | `docs/telemetry/` + `schemas/telemetry/` |

---

## ⚖ FAIR+CARE and Governance

### Review gates
Governance review is required when:
- A layer is new and/or changes classification/sensitivity.
- A layer is derived from sensitive or restricted inputs.
- A new UI layer could reveal sensitive locations through interaction/zoom.
- A layer introduces a new public-facing endpoint or a new external data source.

### CARE and sovereignty considerations
- Identify communities impacted and applicable protection rules.
- Document redaction/generalization rules for any restricted locations.
- Prefer coarse/aggregate public products when sovereignty or sensitivity is uncertain.
- Fail closed for public outputs when sensitivity is unresolved.

### AI usage constraints
- Allowed: summarization, structure extraction, translation, keyword indexing.
- Prohibited: generating new policy, inferring sensitive locations.

---

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-27 | Initial `web/layers` README (layer registry + styles + governance contract) | TBD |

---

Footer refs:
- Master guide: `../../docs/MASTER_GUIDE_v12.md`
- Template: `../../docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`
- Story Node template: `../../docs/templates/TEMPLATE__STORY_NODE_V3.md`
- API contract extension template: `../../docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md`
- Governance: `../../docs/governance/ROOT_GOVERNANCE.md`
- Sovereignty: `../../docs/governance/SOVEREIGNTY.md`
- Ethics: `../../docs/governance/ETHICS.md`
