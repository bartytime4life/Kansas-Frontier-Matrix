---
title: "Web Layers — Registry, Styles, and Governance"
path: "web/layers/README.md"
version: "v1.0.1"
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

doc_uuid: "urn:kfm:doc:web:layers:readme:v1.0.1"
semantic_document_id: "kfm-web-layers-readme-v1.0.1"
event_source_id: "ledger:kfm:doc:web:layers:readme:v1.0.1"
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

This directory defines:

- **What map layers exist** in the Web UI (MapLibre; optionally Cesium if present),
- **Where each layer’s data comes from** (contracted APIs and/or immutable, cataloged artifacts),
- **How each layer is styled** (style fragments + legends + icons), and
- **How each layer is governed** (license, attribution, sensitivity/classification, redaction).

It is the Web/UI-side contract within the canonical pipeline ordering:

**ETL → STAC/DCAT/PROV catalogs → Neo4j graph → APIs → React/Map UI → Story Nodes → Focus Mode**

---

## 📘 Overview

### Purpose
- Provide a **schema-validated layer registry** the Web UI can load deterministically (runtime or build-time) to render MapLibre layers (and optional Cesium layers).
- Centralize **styles, legends, and icons** so map rendering is reviewable, versioned, and reproducible.
- Ensure every public-facing layer can surface **audit affordances** (license, attribution, provenance pointers, vintage) and comply with **FAIR+CARE / sovereignty** constraints.

### Scope

| In Scope | Out of Scope |
|---|---|
| Layer registry structure + semantics (IDs, required fields, evolution rules) | Implementing ETL/pipelines that generate artifacts |
| UI styling fragments + legends + icons | Defining/altering the graph ontology (labels/edges) |
| Provenance pointers surfaced to UI (STAC/DCAT/PROV IDs/refs) | API implementation internals beyond the published contract |
| Validation expectations for registry/style changes (CI gates) | Cloud deployment specifics (CDN/object storage/proxy configs) |

### Audience
- Primary: Web UI developers (React + MapLibre; optional Cesium)
- Secondary: API developers (tiles/features), catalog maintainers (STAC/DCAT/PROV), governance reviewers

### Definitions
Glossary: `docs/glossary.md` (**not confirmed in repo**; create under `docs/` if missing).

Key terms used in this README:
- **Layer registry**: One or more JSON documents enumerating available layers and how to load/style/govern them.
- **Layer entry**: A single layer definition with stable `id`, data source(s), style/legend refs, and governance metadata.
- **Style fragment**: A MapLibre layer snippet (or equivalent) composed into a base map style.
- **Audit affordances**: UI-visible license/attribution/provenance/vintage details for review and traceability.
- **Redaction/generalization**: Controls that prevent sensitive location leakage through geometry, zoom, queries, or UI interactions.

### Key artifacts

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master guide | `docs/MASTER_GUIDE_v12.md` | Core maintainers | Canonical pipeline ordering + invariants |
| v13 redesign blueprint | `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md` | Core maintainers | Canonical subsystem homes + CI gates |
| Universal doc template | `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` | Docs maintainers | Required sections + front-matter keys |
| Story Node template | `docs/templates/TEMPLATE__STORY_NODE_V3.md` | Narrative/curation | Evidence-linked narrative patterns |
| API contract extension template | `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md` | API maintainers | Use when layers require new endpoints/contracts |
| UI schemas | `schemas/ui/` (**not confirmed in repo**) | Web + Platform | JSON schemas for registries/styles/legends |

### Definition of done
- [ ] Front-matter complete + valid (path, IDs, versions)
- [ ] Registry contract documented (minimum required fields + evolution rules)
- [ ] Styling/legend/icon conventions documented (including accessibility notes)
- [ ] Provenance mapping described (STAC/DCAT/PROV pointers, vintage)
- [ ] Validation steps listed and repeatable
- [ ] Governance + CARE/sovereignty considerations explicitly stated

---

## 🗂️ Directory Layout

### This document
- `path`: `web/layers/README.md` *(must match front-matter)*

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| UI | `web/` | React app + MapLibre components; optional Cesium |
| Layer registries + assets | `web/layers/` | Registries, styles, legends, icons for map layers |
| Legacy layer registries | `web/cesium/layers/` (**if present**) | Legacy registry home referenced by templates |
| Schemas | `schemas/` (**not confirmed in repo**) | JSON Schemas (STAC/DCAT/PROV/story/ui/telemetry) |
| API boundary | `src/server/` | Versioned REST/GraphQL endpoints; enforcement/redaction |
| Graph | `src/graph/` | Ontology bindings + graph build/migrations |
| ETL/pipelines | `src/pipelines/` | ETL + catalog generation code |
| STAC outputs | `data/stac/` | STAC collections + items for datasets/artifacts |
| DCAT outputs | `data/catalog/dcat/` | DCAT dataset/distribution metadata |
| PROV outputs | `data/prov/` | Lineage bundles linking raw→work→processed→published |
| Story Nodes | `docs/reports/story_nodes/` | Draft + published Story Nodes (if split exists) |

### Expected file tree for this sub-area
Target layout (align with current repo if it differs; do not relocate without explicit deprecation markers):

~~~text
📁 web/
└── 📁 layers/
    ├── 📄 README.md
    ├── 📁 registries/
    │   ├── 📄 layers.public.json
    │   ├── 📄 layers.overlays.json
    │   └── 📄 layers.restricted.json
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
- If `web/cesium/layers/*.json` exists in the repo, treat it as a supported legacy location. Prefer explicit `deprecated` markers and migration notes over silent moves/removals.

---

## 🧭 Context

### Background
The KFM Web UI must remain **contract-driven and audit-ready**. Map layers are one of the highest-risk surfaces for:
- provenance drift (“where did this geometry come from?”),
- licensing/attribution mistakes, and
- sensitive-location leakage (through zoom, clicks, filters, or export).

A layer registry makes behavior deterministic and reviewable, and it creates a single place to enforce: **every layer is attributable + traceable + governed**.

### Assumptions
- The Web UI consumes the API boundary (`src/server/`) and does not query Neo4j directly.
- Layers are backed by either:
  - versioned API endpoints (tiles/features), and/or
  - immutable artifacts (e.g., PMTiles/MBTiles/COGs/GeoParquet) referenced by STAC.
- Layer metadata required for UI audit panels is available via registries and/or catalog lookups.

### Constraints / invariants
1. **Canonical ordering is preserved**: ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode.
2. **No UI direct-to-graph reads**: all graph access is via contracted APIs.
3. **Fail closed on sensitivity**: if a layer’s classification/sensitivity is unresolved, it must not ship in public registries/builds.
4. **Provenance-first**: a layer intended for Story Nodes / Focus Mode must provide STAC/DCAT/PROV pointers (directly or resolvable).
5. **Backward-compatible evolution**: adding optional registry fields is non-breaking; breaking changes require a schema/version bump and migration notes.
6. **No hidden data leakage**: redaction/generalization must be enforced at the API boundary and reflected in UI behavior (zoom limits, interaction limits, export rules).

### Open questions

| Question | Owner | Target date |
|---|---|---|
| Where is the JSON Schema for layer registries (`schemas/ui/…`)? | Platform + Web | TBD |
| Do we load registries at runtime (fetch) or compile-time (bundle)? | Web | TBD |
| Do we need separate public vs restricted registries beyond filename conventions? | Governance + Web | TBD |
| Do we support Cesium/3D layer registries in this area or keep them isolated under `web/cesium/`? | Web | TBD |

### Future extensions
- Time-enabled layers (temporal filters + “vintage” UI)
- Per-layer access control (RBAC/policy gating reflected in the registry)
- Multi-language layer titles/legends (localization bundles)
- Map style composition tooling (validate fragments against a base style in CI)

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

### Optional: sequence diagram for toggling a layer

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
  UI->>API: Request tiles/features per layer contract
  API-->>UI: Tile data / feature payload (redaction enforced)
  UI->>Cat: Resolve provenance pointers for audit panel
  Cat-->>UI: STAC/DCAT/PROV refs (IDs and/or resolvable links)
  UI-->>User: Render layer + show attribution/audit affordances
~~~

---

## 📦 Data & Metadata

### Inputs

| Input | Format | Where from | Validation |
|---|---|---|---|
| Layer registry | JSON | `web/layers/registries/*.json` | JSON schema (if present under `schemas/ui/`) + referential integrity |
| Style fragments | JSON | `web/layers/styles/**` | File exists + MapLibre style validation (as configured) |
| Legends | JSON | `web/layers/legends/**` | File exists + legend schema (if present) |
| Icons | SVG/PNG | `web/layers/icons/**` | File exists + size/a11y conventions |
| Tiles/features | HTTP | `src/server/` endpoints | API contract tests + policy/redaction enforcement |
| Catalog refs | HTTP/file | `data/stac/`, `data/catalog/dcat/`, `data/prov/` | STAC/DCAT/PROV validators |

### Outputs

| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Rendered map layers | Runtime | Web UI | Registry + styles must be deterministic |
| Attribution + license display | UI panel | Web UI | Must match upstream license/attribution |
| Provenance panel content | UI panel | Web UI | Must resolve to STAC/DCAT/PROV IDs/links |
| Layer-toggle telemetry (optional) | Events/logs | `docs/telemetry/` (**not confirmed**) | Telemetry schema (if present) |

### Sensitivity & redaction
Every layer entry MUST document:
- `sensitivity` and `classification`,
- redaction/generalization summary (including zoom-level or interaction limits),
- the enforcement plane: **dataset**, **catalog**, **API**, and/or **UI**.

Do not rely on UI-only masking for sensitive layers; UI is not a security boundary.

### Quality signals
- Registry completeness: required fields present for each layer.
- Link integrity: referenced local assets and API endpoints exist.
- Render integrity: style fragments don’t reference missing sources/source-layers.
- Audit completeness: license + attribution + provenance pointers are consistent.
- Performance sanity: min/max zoom and tile endpoints avoid pathological over-fetching.

---

## 🌐 STAC, DCAT & PROV Alignment

### STAC
- Collections: referenced via `data.stac.collection_id` (or equivalent).
- Items: referenced via `data.stac.item_id` (or equivalent).
- Assets: for immutable artifacts, prefer referencing the STAC asset key/href (and digest) over “latest” URLs.

### DCAT
- Dataset identifiers: referenced via `data.dcat.dataset_id` (or URI).
- License mapping: registry `license` / `attribution` SHOULD match DCAT dataset/distribution metadata.
- Publisher/contact: sourced from DCAT when available; surface in UI audit panels as needed.

### PROV-O
- `prov:wasDerivedFrom`: represented by the published lineage bundle; registry stores pointers (IDs/refs) rather than copying full graphs.
- `prov:wasGeneratedBy`: `data.prov.activity_id` identifies the run/activity that produced the layer artifact.
- Activity/Agent identities: include pipeline IDs, tool versions, and run IDs where available.

### Versioning
- Prefer explicit predecessor/successor linkages in STAC and PROV; the graph mirrors version lineage where modeled.
- Avoid unversioned “latest” sources unless explicitly intended and governed.

### Recommended registry fields for evidence linkage
A layer entry SHOULD include:
- STAC: `data.stac.collection_id`, `data.stac.item_id`
- DCAT: `data.dcat.dataset_id` (and optional distribution identifier)
- PROV: `data.prov.activity_id` (and optional agent reference)

### Mapping table

| Layer registry field | Maps to | Purpose |
|---|---|---|
| `id` | Stable UI contract key | Toggles, ordering, telemetry, Story Nodes |
| `data.api.*` | API endpoints | Where tiles/features come from |
| `data.stac.*` | STAC collection/item IDs | Artifact traceability |
| `data.dcat.*` | DCAT dataset/distribution | Licensing + publisher + discovery |
| `data.prov.*` | PROV activity/entity IDs | Lineage + reproducibility |
| `license` + `attribution` | DCAT + upstream manifest | Legal/ethical display + reuse rules |
| `governance.*` | Governance policy | Prevent sensitive location leakage |

---

## 🧱 Architecture

### Components
High-level KFM contract boundary (for context):

| Component | Responsibility | Interface |
|---|---|---|
| ETL | Ingest + normalize | Config + run logs |
| Catalogs | STAC/DCAT/PROV | JSON + validator |
| Graph | Neo4j | Cypher + API layer |
| APIs | Serve contracts | REST/GraphQL |
| UI | Map + narrative | API calls |
| Story Nodes | Curated narrative | Graph + docs |
| Focus Mode | Contextual synthesis | Provenance-linked |

Web-layer module components (this directory):

| Component | Responsibility | Interface |
|---|---|---|
| Registry loader | Load + validate registries | JSON schema (if present) |
| Style composer | Compose base style + fragments | MapLibre style JSON |
| Legend renderer | Render legends + icons | Legend JSON + SVG/PNG |
| Audit/provenance panel | Surface license/attribution + STAC/DCAT/PROV refs | Registry + catalog fetch |
| API clients | Fetch tiles/features | Versioned API endpoints |

### Interfaces / contracts

| Contract | Location | Versioning rule |
|---|---|---|
| UI registry schemas | `schemas/ui/` (**not confirmed**) | Semver + changelog |
| API schemas | `src/server/` + docs | Contract tests required |
| Layer registries | `web/layers/registries/` (or legacy `web/cesium/layers/`) | Schema-validated |
| Style fragments | `web/layers/styles/**` | Validate against base style + MapLibre spec |
| Legends | `web/layers/legends/**` | Schema-validated (if schema exists) |

### Registry contract
If a UI schema exists under `schemas/ui/`, it is the source of truth. Until then, treat the following as the minimum contract for each layer entry:

**Stable identifiers**
- `id` (kebab-case; stable across releases)
- `title` (UI display name)
- `kind` (e.g., `vector-tiles`, `raster-tiles`, `features`, `3d`)

**UI behavior**
- `ui.order` (layer ordering)
- `ui.default_visible` (boolean)
- `ui.minzoom` / `ui.maxzoom`
- `ui.style_ref` / `ui.legend_ref` (local path refs)
- optional: `ui.interactive`, `ui.queryable_fields`, `ui.exportable`

**Data source**
- `data.api.tilejson` and/or `data.api.tiles` and/or `data.api.features`
- optional: immutable artifact pointer (prefer via STAC asset)

**Evidence pointers**
- `data.stac.collection_id`, `data.stac.item_id`
- `data.dcat.dataset_id`
- `data.prov.activity_id`

**Governance**
- `governance.sensitivity`, `governance.classification`
- `governance.redaction` summary + enforcement plane
- `governance.care_notes` (required when sensitivity is anything other than public/open)

### Example minimal registry file

~~~json
{
  "schema_version": "KFM-UI-LAYER-REGISTRY v1",
  "generated_at": "2025-12-28T00:00:00Z",
  "layers": [
    {
      "id": "surficial-geology",
      "title": "Surficial Geology",
      "kind": "vector-tiles",
      "ui": {
        "order": 100,
        "default_visible": false,
        "minzoom": 4,
        "maxzoom": 12,
        "legend_ref": "../legends/surficial-geology.legend.json",
        "style_ref": "../styles/fragments/surficial-geology.style.json"
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
          "activity_id": "prov:activity:geology:2025-10-01:abc123"
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

### Extension points checklist (for future work)
- [ ] Data: new domain added under `data/<domain>/...`
- [ ] STAC: new collection + item schema validation
- [ ] PROV: activity + agent identifiers recorded
- [ ] Graph: new labels/relations mapped + migration plan
- [ ] APIs: contract version bump + tests
- [ ] UI: layer registry entry + access rules
- [ ] Focus Mode: provenance references enforced
- [ ] Telemetry: new signals + schema version bump

---

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode
Layers may be referenced as evidence by `layer_id` and used to pre-configure the map for a story/focus view.

For any enabled layer, Focus Mode SHOULD be able to surface:
- license/attribution,
- data vintage (updated-at or version),
- STAC/DCAT/PROV identifiers,
- sensitivity/redaction notes (and an explicit “why” if a layer is blocked).

### Provenance-linked narrative rule
- Focus Mode consumes provenance-linked content only.
- Any derived/aggregated layer must include uncertainty metadata and a resolvable provenance chain.

### Optional structured controls

~~~yaml
focus_layers:
  - "surficial-geology"
  - "hydro-network"
focus_time: "2025-10-01"
focus_center: [-98.0000, 38.0000]
~~~

---

## 🧪 Validation & CI/CD

### Validation steps
- [ ] Markdown protocol checks (front-matter + required sections)
- [ ] Registry schema validation (if `schemas/ui/` exists)
- [ ] Style/legend referential integrity (files exist; fragments compile)
- [ ] STAC/DCAT/PROV validation (for referenced artifacts)
- [ ] API contract tests (tiles/features endpoints)
- [ ] Security + sovereignty checks (PII, sensitive-location leakage, classification propagation)
- [ ] Accessibility checks (legend readability, icon a11y, keyboard navigation for layer toggles)

### Reproduction

~~~bash
# Example placeholders — replace with repo-specific commands

# 1) validate schemas (UI registries, STAC/DCAT/PROV, etc.)

# 2) run web lint/tests

# 3) run link-check / markdown lint (if configured)
~~~

### Telemetry signals (if applicable)

| Signal | Source | Where recorded |
|---|---|---|
| `ui.layer.toggle` | Layer toggle UI | `docs/telemetry/` + `schemas/telemetry/` (**not confirmed**) |
| `ui.layer.load_error` | Registry loader / API client | `docs/telemetry/` |
| `ui.audit_panel.open` | Audit/provenance panel | `docs/telemetry/` |

---

## ⚖ FAIR+CARE & Governance

### Governance review triggers
A review is required when:
- A layer is new and/or changes sensitivity/classification.
- A layer is derived from restricted inputs or could reveal sensitive locations.
- A layer introduces a new external data source (license/provenance review).
- A layer requires a new public-facing endpoint or interaction pattern.

### CARE and sovereignty considerations
- Identify impacted communities and applicable protection rules.
- Prefer coarse/aggregate public products when sovereignty/sensitivity is uncertain.
- Redaction/generalization must be documented and enforced across datasets, catalogs, APIs, and UI.
- Fail closed: do not publish public layers when sensitivity is unresolved.

### AI usage constraints
- Allowed: summarization, structure extraction, translation, keyword indexing.
- Prohibited: generating new policy, inferring sensitive locations.

---

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.1 | 2025-12-28 | Refined structure + clarified registry contract, validation, governance | TBD |
| v1.0.0 | 2025-12-27 | Initial `web/layers` README draft | TBD |

---

Footer refs:
- Master guide: `../../docs/MASTER_GUIDE_v12.md`
- v13 blueprint: `../../docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md`
- Universal template: `../../docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`
- Story Node template: `../../docs/templates/TEMPLATE__STORY_NODE_V3.md`
- API contract extension template: `../../docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md`
- Governance: `../../docs/governance/ROOT_GOVERNANCE.md`
- Sovereignty: `../../docs/governance/SOVEREIGNTY.md`
- Ethics: `../../docs/governance/ETHICS.md`
