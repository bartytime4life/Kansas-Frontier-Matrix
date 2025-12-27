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

This directory defines **what map layers exist in the Web UI**, **where their data comes from (via APIs and/or versioned artifacts)**, and **how they are styled and governed**.

It is the UI-side contract within the canonical pipeline:

**ETL → STAC/DCAT/PROV → Graph → API → UI → Story Nodes → Focus Mode**

---

## 📘 Overview

### Purpose
- Provide a **schema-validated layer registry** that the Web UI can load at runtime to render MapLibre layers (and, if present in the repo, Cesium layers).
- Centralize **layer styling and legends** so that map rendering is deterministic, reviewable, and versioned.
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

### Definitions (link to glossary)
- Link: `docs/glossary.md` (**not confirmed in repo**)
- Terms used in this doc:
  - **Layer registry**: JSON configs enumerating what layers exist and how to load/style them.
  - **Layer entry**: A layer definition with stable `id`, data source, style references, and governance metadata.
  - **Audit affordances**: UI-visible metadata (license/attribution/provenance/vintage) that supports review and traceability.
  - **Redaction/generalization**: Measures that prevent sensitive locations or restricted knowledge from being exposed by geometry, zoom, or interaction.

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master guide | `docs/MASTER_GUIDE_v12.md` | Core maintainers | Canonical pipeline ordering + invariants |
| Redesign blueprint | `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md` | Core maintainers | Canonical homes + CI gates + repo lint |
| Universal doc template | `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` | Docs maintainers | This README conforms to the Universal governed doc template |
| Story Node template | `docs/templates/TEMPLATE__STORY_NODE_V3.md` | Narrative/curation | Story/Focus-mode linkage patterns |
| API contract extension template | `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md` | API maintainers | Use when a layer requires new endpoints/contracts |
| UI schemas | `schemas/ui/**` (**not confirmed in repo**) | UI + platform | JSON schema(s) for layer registries and related UI artifacts |

### Definition of done (for this document)
- [ ] Front-matter complete + valid
- [ ] Layer registry contract described with examples (required + optional fields)
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
| Web UI | `web/` | React app + MapLibre components, plus optional Cesium UI |
| UI layer registries | `web/**/layers/**` | Layer registry JSON configs + related UI assets |
| Schemas | `schemas/` | JSON schemas (STAC/DCAT/PROV/story/UI/telemetry) if adopted |
| API contracts | `src/server/contracts/` | OpenAPI/GraphQL contracts; contract tests |
| API implementation | `src/server/` | Versioned REST/GraphQL endpoints |
| STAC outputs | `data/stac/` | STAC collections + items for datasets/artifacts |
| DCAT outputs | `data/catalog/dcat/` | DCAT dataset/distribution metadata |
| PROV outputs | `data/prov/` | Lineage bundles linking raw→work→processed→published |
| Story Nodes | `docs/reports/story_nodes/` | Draft + published Story Nodes (if split exists) |

### Expected structure in this directory (recommended target)

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
- The above is a **recommended target**; align with the repo’s existing layout if it differs.
- Some project documents cite `web/cesium/layers/regions.json` as an example registry location. If that exists in your repo, treat it as compatible and consolidate with explicit deprecation markers if you relocate it.

---

## 🧭 Context

### Canonical pipeline + UI boundary
KFM is contract-first and evidence-first. The UI must be a consumer of **versioned artifacts and contracted APIs**.

Layer-related invariants:
1. **UI → API only** (no direct graph/DB calls; UI is not a data store).
2. **Provenance-first**: every layer can surface STAC/DCAT/PROV references.
3. **No hidden data leakage**: layers can reveal sensitive locations via zoom/interaction; this must be governed.
4. **Backward-compatible evolution**: adding layer entries should not break older clients (ignore unknown fields gracefully).

### Why a layer registry exists
A single registry provides:
- Deterministic layer behavior (ordering, default visibility, min/max zoom).
- A consistent place to attach governance metadata (license, attribution, sensitivity).
- A reliable UI surface for audit panels and Focus Mode “evidence” linkage.
- A CI target: validate registries against schemas and ensure referenced assets/endpoints exist.

### Layer lifecycle (end-to-end)
Adding a layer usually spans multiple subsystems:

1. **Data artifact exists** (processed + published form)
   - Example: PMTiles / MBTiles, COG, GeoParquet, or a PostGIS-backed service.
2. **Catalog metadata exists**
   - STAC item(s) + DCAT dataset + PROV run bundle.
3. **API surface exists**
   - Tile/feature endpoints are versioned and contract-tested.
4. **UI registry entry exists**
   - Registry points to API endpoints (and/or immutable artifacts) + style fragment + legend.
5. **Governance gate passes**
   - Sensitivity classification, redaction notes, sovereignty rules, and licensing are reviewed.
6. **Story Nodes (optional) reference the layer**
   - Story Nodes cite evidence IDs; Focus Mode enforces provenance-only context.

### Naming + versioning conventions
- **Layer `id` must be stable** (contract key referenced by UI state, Story Nodes, telemetry).
- Prefer **kebab-case** IDs and filenames: `surficial-geology`, `hydro-network`, `air-sensors`.
- Prefer **versioned sources** (immutable URLs or STAC asset hrefs with digests) over “latest” URLs.
- Adding a layer should be backward compatible; breaking changes require a coordinated front-end release bump.

---

## 🗺️ Diagrams

### System / dataflow diagram (where layers fit)

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

### Sequence: toggling a layer in the UI

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
  UI->>Cat: (Optional) Resolve provenance pointers for audit panel
  Cat-->>UI: STAC/DCAT/PROV metadata links
  UI-->>User: Render layer + show attribution/audit affordances
~~~

---

## 🧠 Story Node & Focus Mode Integration

### What layers provide to Story Nodes
Story Nodes should be able to reference a layer by `layer_id` as evidence, alongside STAC/DCAT/PROV identifiers.

Recommended (optional) structured controls (field names may differ; follow the Story Node template if present):

~~~yaml
focus_layers:
  - "surficial-geology"
  - "hydro-network"
focus_time: "2025-10-01"
focus_center: [-98.0000, 38.0000]
~~~

### Focus Mode rule
Focus Mode only consumes provenance-linked content. For layers this implies:
- A layer can be used as evidence only if it carries provenance pointers (STAC/DCAT/PROV IDs or resolvable links).
- Any derived/inferred layer must carry uncertainty metadata and a clear provenance chain.

### UI audit affordances (minimum)
For any displayed layer, the UI should be able to show:
- License + attribution
- Data vintage / “last updated”
- Provenance references (STAC item ID, DCAT dataset ID, PROV activity ID)
- Sensitivity classification + redaction notes (if any)

---

## 🧪 Validation & CI/CD

### Minimum CI expectations for layer changes
Any PR that changes `web/**/layers/**` should:
- Validate registry JSON against the UI layer registry schema (if present).
- Validate required fields (id/name/source/style_ref/attribution/license/sensitivity).
- Validate referenced local files exist (style fragments, legends, icons).
- Validate referenced API endpoints are versioned/contracted and do not bypass the UI→API boundary.
- Run security + sovereignty scanning gates where applicable.

### Local reproduction (placeholders)
~~~bash
# Replace these with repo-specific commands

# 1) Validate JSON schemas (UI registries, STAC/DCAT/PROV, etc.)
# <repo command here>

# 2) Run web lint/tests
# <repo command here>

# 3) Run link-check / markdown lint (if configured)
# <repo command here>
~~~

---

## 📦 Data & Metadata

### Layer types the registry should support
At minimum, the registry should be able to describe:
- **Vector tiles (MVT)**: UI renders geometry + labels via style rules.
- **Raster tiles / rasters (COG-backed services)**: UI renders imagery with colormaps.
- **Feature services**: UI queries features for popups, filters, and charts.
- Optional: WMS/WMTS, 3D tiles, time-enabled layers.

### Provenance requirements
For published layers, treat STAC/DCAT/PROV as mandatory:
- STAC Item representing the layer artifact (tileset/raster) or a stable reference to an API-distributed product.
- DCAT Dataset record for discoverability and licensing/publisher metadata.
- PROV bundle linking source → processing activity → published artifact.

### Performance notes (UI-facing)
- For point layers, prefer doing clustering in the UI style/client rather than baking clustering into tiles.
- Prefer pre-generated, CDNable artifacts for layers that update daily/weekly/monthly.
- For versioned artifact URLs, set long-lived caching headers and treat paths as immutable.

---

## 🌐 STAC, DCAT & PROV Alignment

### Recommended registry fields for evidence linkage
A layer entry should include:
- STAC: `stac_collection_id` and `stac_item_id` (or equivalent resolvable references)
- DCAT: `dcat_dataset_id` (or URI)
- PROV: `prov_activity_id` (run/lineage ID) and (if possible) an agent reference

### Mapping table

| Layer registry field | Maps to | Purpose |
|---|---|---|
| `id` | Stable UI contract key | Used by toggles, telemetry, story nodes |
| `data.api` | API endpoint(s) | Where tiles/features come from |
| `data.stac.*` | STAC collection/item IDs | Artifact traceability |
| `data.dcat.*` | DCAT dataset/distribution | Licensing + publisher + discovery |
| `data.prov.*` | PROV activity/entity IDs | Lineage + reproducibility |
| `license` + `attribution` | DCAT + upstream manifest | Legal/ethical display + reuse rules |
| `governance.*` | Governance policy | Prevent sensitive location leakage |

---

## 🧱 Architecture

### Subsystem contracts (layer-related)
The UI subsystem contract includes:
- **Layer registry + a11y + audit affordances**
- “Do not break” rule: **no hidden data leakage**

Layer registry changes are treated as interface contract changes: schema-validated and versioned with front-end releases.

### Components

| Component | Responsibility | Interface |
|---|---|---|
| Layer registry loader | Load and validate registry JSON | JSON schema (`schemas/ui/**`) |
| Style composer | Compose MapLibre style from base + fragments | MapLibre style spec JSON |
| Legend renderer | Render legend + icons consistently | Legend JSON + SVG/PNG assets |
| Layer toggle UI | Toggle visibility, ordering, filters | React components + state |
| Audit/provenance panel | Show license/attribution + STAC/DCAT/PROV refs | Registry fields + catalog fetch |
| API clients | Fetch tiles/features | Versioned REST endpoints |

### Example: minimal layer registry entry (illustrative)
~~~json
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
~~~

### Example: MapLibre style fragment (illustrative)
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

---

## ⚖ FAIR+CARE & Governance

### Review gates (layer-specific)
Governance review is required when:
- A layer is new and/or changes classification/sensitivity.
- A layer is derived from sensitive/restricted inputs.
- A new UI layer could reveal sensitive locations through interaction/zoom.
- A layer introduces a new public-facing endpoint or a new external data source.

### Sovereignty safety
- Document redaction/generalization rules for any restricted locations.
- Prefer coarse/aggregate public products when sovereignty or sensitivity is uncertain.
- “Fail closed”: if a layer’s sensitivity cannot be determined, do not publish it to the public UI.

### AI usage constraints (for docs + metadata)
- Allowed: summarization, structure extraction, translation, keyword indexing.
- Prohibited: generating new policy, inferring sensitive locations (directly or indirectly).

---

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-27 | Initial `web/layers` README (layer registry + styles + governance contract) | TBD |

---

## Footer refs (do not remove)

- Master guide: `../../docs/MASTER_GUIDE_v12.md`
- Template: `../../docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`
- Story Node template: `../../docs/templates/TEMPLATE__STORY_NODE_V3.md`
- API contract extension template: `../../docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md`
- Governance: `../../docs/governance/ROOT_GOVERNANCE.md`
- Sovereignty: `../../docs/governance/SOVEREIGNTY.md`
- Ethics: `../../docs/governance/ETHICS.md`
--- 

