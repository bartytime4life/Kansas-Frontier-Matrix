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

This directory defines the **UI-side contract** for map layers rendered in the KFM web application (React + MapLibre; optional Cesium if present):

- **Which layers exist** (stable IDs and user-facing metadata),
- **Where layer data comes from** (contracted API endpoints and/or cataloged, immutable artifacts),
- **How layers are styled** (MapLibre style assets, legends, icons), and
- **How layers are governed** (license, attribution, sensitivity/classification, redaction/generalization).

This module sits in the canonical pipeline ordering:

**ETL → STAC/DCAT/PROV catalogs → Neo4j graph → APIs → React/Map UI → Story Nodes → Focus Mode**

---

## 📘 Overview

### Purpose
- Provide a **deterministic, schema-validated layer registry** the Web UI can load (build-time or runtime) to render map layers.
- Make styling **reviewable and reproducible** by versioning style assets, legends, and icons alongside their layer definitions.
- Ensure every layer can surface **audit affordances** (license, attribution, provenance pointers, vintage) and comply with **FAIR+CARE / sovereignty** constraints.

### Scope

| In Scope | Out of Scope |
|---|---|
| Layer registry semantics (IDs, required fields, versioning, deprecation rules) | Implementing ETL jobs that generate datasets/artifacts |
| Style assets, legends, icons (reviewable map rendering inputs) | Defining/altering the graph ontology (labels/edges) |
| Provenance pointers surfaced to UI (STAC/DCAT/PROV identifiers/refs) | API implementation internals beyond the published contract |
| Validation expectations for registry/style changes (CI gates) | Cloud deployment specifics (CDN/object storage/proxy configs) |

### Audience
- Primary: Web UI developers (React + MapLibre; optional Cesium)
- Secondary: API developers (tiles/features endpoints), catalog maintainers (STAC/DCAT/PROV), governance reviewers

### Definitions
Glossary: `docs/glossary.md` (**not confirmed in repo**; create under `docs/` if missing).

Key terms used in this README:
- **Layer registry**: JSON document enumerating available layers, how to load them, and how they are governed.
- **Layer entry**: A single layer definition with stable `id`, source(s), style/legend refs, and governance metadata.
- **Style asset**: Either a complete MapLibre style JSON or a fragment used to compose the final style.
- **Audit affordances**: UI-visible license/attribution/provenance/vintage details.
- **Redaction/generalization**: Controls that prevent sensitive location leakage through geometry, zoom, queries, or export.

### Key artifacts

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master guide | `docs/MASTER_GUIDE_v12.md` | Core maintainers | Canonical pipeline ordering + invariants |
| v13 redesign blueprint | `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md` | Core maintainers | “One canonical home”, contract-first, evidence-first |
| Universal doc template | `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` | Docs maintainers | Required sections + front-matter keys |
| Story Node template | `docs/templates/TEMPLATE__STORY_NODE_V3.md` | Story maintainers | Evidence-linked narrative patterns |
| API contract extension template | `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md` | API maintainers | Use when layers require new endpoints/contracts |
| UI registry schemas | `schemas/ui/` (**not confirmed in repo**) | Web + Platform | JSON Schemas for registries/styles/legends |
| Governance root | `docs/governance/ROOT_GOVERNANCE.md` (**not confirmed in repo**) | Governance | Policy source of truth |
| Sovereignty policy | `docs/governance/SOVEREIGNTY.md` (**not confirmed in repo**) | Governance | CARE and sovereignty gates |
| Ethics | `docs/governance/ETHICS.md` (**not confirmed in repo**) | Governance | Ethical constraints |

### Definition of done
- [ ] Front-matter complete + valid (path, IDs, versions)
- [ ] Registry contract documented (required fields + evolution/deprecation rules)
- [ ] Style/legend/icon conventions documented (including accessibility notes)
- [ ] Provenance mapping described (STAC/DCAT/PROV pointers + vintage)
- [ ] Validation steps listed and repeatable
- [ ] Governance + CARE/sovereignty considerations explicitly stated

---

## 🗂️ Directory Layout

### This document
- `path`: `web/layers/README.md` *(must match front-matter)*

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| UI app | `web/` | React app + MapLibre; optional Cesium |
| Web layer contract | `web/layers/` | Registries, style assets, legends, icons, README (this doc) |
| Map engine internals | `web/src/map/engine/` (**not confirmed in repo**) | Registry loader + style composition logic |
| Focus Mode UI | `web/src/story/focus_mode/` (**not confirmed in repo**) | Provenance-first narrative + map context |
| Schemas | `schemas/` | JSON Schemas (STAC/DCAT/PROV/story/ui/telemetry) |
| API boundary | `src/server/` | Versioned endpoints; redaction/generalization enforcement |
| Graph | `src/graph/` | Ontology bindings + graph ingest/migrations |
| ETL/pipelines | `src/pipelines/` | Ingest + transformations + catalog builds |
| STAC outputs | `data/stac/` | STAC collections + items for datasets/artifacts |
| DCAT outputs | `data/catalog/dcat/` | DCAT dataset/distribution metadata |
| PROV outputs | `data/prov/` | Lineage bundles linking raw→work→processed→published |
| Story Nodes | `docs/reports/story_nodes/` | Draft + published Story Nodes (if split exists) |
| Legacy Cesium registries | `web/cesium/layers/` (**if present**) | Legacy registry location; migrate with deprecation markers |

### Expected file tree for this sub-area
Target layout (adjust to current repo if it differs; do not relocate without explicit deprecation markers):

~~~text
📁 web/
└── 📁 layers/
    ├── 📄 README.md
    ├── 📁 registries/
    │   ├── 📄 layers.public.json
    │   ├── 📄 layers.overlays.json
    │   ├── 📄 layers.experimental.json
    │   └── 📄 layers.restricted.json
    ├── 📁 styles/
    │   ├── 📄 base.style.json
    │   └── 📁 fragments/
    │       ├── 📄 <layer_id>.style.json
    │       └── 📄 <layer_id>.hover.style.json
    ├── 📁 legends/
    │   ├── 📄 <layer_id>.legend.json
    │   └── 📁 icons/
    │       └── 📄 <icon>.svg
    ├── 📁 icons/
    │   └── 📄 <layer_id>.svg
    └── 📁 sprites/                          # optional; if used by MapLibre style
        ├── 📄 sprite.json
        └── 📄 sprite.png
~~~

Notes:
- Prefer **additive evolution**: add files/fields rather than moving or renaming.
- If `web/cesium/layers/*.json` exists, treat it as supported legacy. Use explicit `deprecated` markers and a migration note rather than silent moves/removals.

---

## 🧭 Context

### Background
Map layers are a high‑risk surface for:
- provenance drift (“where did this geometry come from?”),
- licensing/attribution mistakes, and
- sensitive-location leakage (through zoom, click queries, filters, exports, or screenshots).

A registry makes behavior deterministic and reviewable, and it creates a single place to enforce:

**every layer is attributable + traceable + governed**

### Assumptions
- The Web UI consumes **contracted APIs** and does not query Neo4j directly.
- Layers are backed by either:
  - versioned API endpoints (tiles/features), and/or
  - immutable artifacts (e.g., PMTiles/MBTiles/COGs/GeoParquet) referenced by STAC and served through governed endpoints.
- Layer metadata required for UI audit panels is available via registries and/or catalog lookups.

### Constraints and invariants
1. **Canonical ordering is preserved**: ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode.
2. **No UI direct-to-graph reads**: all graph access is via contracted APIs.
3. **Fail closed on sensitivity**: if a layer’s classification/sensitivity is unresolved, it must not ship in public registries/builds.
4. **Provenance-first UI**: public layers must expose license + attribution + provenance pointers (STAC/DCAT/PROV) and a data vintage.
5. **Backward-compatible evolution**: adding optional registry fields is non-breaking; breaking changes require a schema/version bump and migration notes.
6. **UI is not a security boundary**: redaction/generalization must be enforced at the API boundary; UI may add safeguards but cannot be the only control.

### Open questions

| Question | Owner | Target date |
|---|---|---|
| Where is the JSON Schema for layer registries (`schemas/ui/…`)? | Platform + Web | TBD |
| Do we load registries at runtime (fetch) or compile-time (bundle)? | Web | TBD |
| What is the canonical split between public vs restricted registries (filenames vs auth gating)? | Governance + Web | TBD |
| Do we support Cesium/3D registries in `web/layers/` or keep them isolated under `web/cesium/`? | Web | TBD |

### Future extensions
- Time-enabled layers (temporal filters + “vintage” UI)
- Per-layer access control (RBAC/policy gating reflected in the registry)
- Multi-language layer titles/legends (localization bundles)
- Map style composition tooling (validate fragments against a base style in CI)

---

## 🗺️ Diagrams

### System dataflow diagram

~~~mermaid
flowchart LR
  A[ETL] --> B[STAC/DCAT/PROV Catalogs]
  B --> C[Neo4j Graph]
  C --> D[APIs]
  D --> E[React/Map UI]
  E --> F[Story Nodes]
  F --> G[Focus Mode]
~~~

### Sequence toggling a layer

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
| Layer registries | JSON | `web/layers/registries/*.json` | JSON schema (if present under `schemas/ui/`) + referential integrity |
| Style assets | JSON | `web/layers/styles/**` | File exists + MapLibre style validation (as configured) |
| Legends | JSON | `web/layers/legends/**` | File exists + legend schema (if present) |
| Icons/sprites | SVG/PNG | `web/layers/icons/**`, `web/layers/sprites/**` | File exists + accessibility conventions |
| Tiles/features | HTTP | `src/server/` endpoints | API contract tests + policy/redaction enforcement |
| Catalog refs | JSON/HTTP | `data/stac/`, `data/catalog/dcat/`, `data/prov/` | STAC/DCAT/PROV validators |

### Outputs

| Output | Format | Where | Contract / Schema |
|---|---|---|---|
| Rendered map layers | Runtime | Web UI | Registry + style assets must be deterministic |
| Attribution/license panel | UI | Web UI | Must match upstream license/attribution |
| Provenance panel | UI | Web UI | Must resolve to STAC/DCAT/PROV identifiers/refs |
| Layer-toggle telemetry | Events/logs | `docs/telemetry/` (**not confirmed**) | Telemetry schema (if present) |

### Sensitivity and redaction
Every layer entry MUST document:
- `sensitivity` and `classification`,
- a redaction/generalization summary (including zoom/interaction/export limits),
- the enforcement plane: **dataset**, **catalog**, **API**, and/or **UI**.

Do not rely on UI-only masking for sensitive layers; UI is not a security boundary.

### Quality signals
- Registry completeness: required fields present for each layer.
- Referential integrity: referenced local assets and API endpoints exist.
- Render integrity: style assets don’t reference missing sources/source-layers.
- Audit completeness: license + attribution + provenance pointers are consistent.
- Performance sanity: min/max zoom and tile endpoints avoid pathological over-fetching.

---

## 🌐 STAC, DCAT & PROV Alignment

### STAC
- Prefer referencing **collection + item IDs** and (for immutable artifacts) **asset keys + digests** rather than unversioned “latest” URLs.
- Layers that are derived products should point to the STAC item representing the published artifact (e.g., PMTiles, GeoParquet).

### DCAT
- Registry `license` / `attribution` SHOULD match DCAT dataset/distribution metadata.
- Publisher/contact metadata should be sourced from DCAT when available and surfaced in UI audit panels.

### PROV-O
- Registry stores pointers to PROV bundles/activities rather than copying full lineage graphs.
- `data.prov.activity_id` identifies the run that produced the layer artifact.

### Recommended evidence pointer fields
A layer entry SHOULD include:
- STAC: `data.stac.collection_id`, `data.stac.item_id`
- DCAT: `data.dcat.dataset_id` (and optional distribution identifier)
- PROV: `data.prov.activity_id` (and optional agent reference)
- Vintage: `data.vintage` (date or version string shown to users)

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
KFM contract boundary context:

| Component | Responsibility | Interface |
|---|---|---|
| ETL | Ingest + normalize | Config + run logs |
| Catalogs | STAC/DCAT/PROV | JSON + validators |
| Graph | Neo4j | Queried only via API |
| APIs | Serve contracts + enforce policy | REST/GraphQL (as implemented) |
| UI | Map + narrative | API calls + catalog reads |
| Story Nodes | Curated narrative | Provenance-linked docs |
| Focus Mode | Contextual synthesis | Provenance-linked bundles only |

Web-layer module components:

| Component | Responsibility | Interface |
|---|---|---|
| Registry loader | Load + validate registries | JSON schema (if present) |
| Style composer | Compose base style + fragments | MapLibre style JSON |
| Legend renderer | Render legends + icons | Legend JSON + SVG/PNG |
| Audit panel | Surface license/attribution + STAC/DCAT/PROV refs | Registry + catalog refs |
| API clients | Fetch tiles/features | Versioned API endpoints |

### Interfaces and contracts

| Contract | Location | Versioning rule |
|---|---|---|
| UI registry schemas | `schemas/ui/` (**not confirmed**) | Semver + changelog |
| API contracts | `src/server/contracts/` (**if present**) | Contract tests required |
| Layer registries | `web/layers/registries/` | Schema-validated JSON |
| Style assets | `web/layers/styles/**` | Validate against MapLibre spec |
| Legends | `web/layers/legends/**` | Schema-validated (if schema exists) |

### Registry contract minimum draft
If `schemas/ui/` exists, it is the source of truth. Until then, treat the following as the minimum contract for each layer entry.

**Stable identifiers**
- `id` (kebab-case; stable across releases; referenced by Story Nodes and Focus Mode)
- `title` (UI display name)
- `kind` (e.g., `vector-tiles`, `raster-tiles`, `features`, `3d`)

**UI behavior**
- `ui.order` (numeric ordering)
- `ui.default_visible` (boolean)
- `ui.minzoom` / `ui.maxzoom`
- `ui.style_ref` / `ui.legend_ref` (local path refs)
- optional: `ui.interactive`, `ui.queryable_fields`, `ui.exportable`

**Data sources**
- API: `data.api.tilejson` and/or `data.api.tiles` and/or `data.api.features`
- optional: immutable artifact pointer via STAC (`data.stac.*`) rather than hardcoded “latest” URLs

**Evidence pointers**
- STAC: `data.stac.collection_id`, `data.stac.item_id`
- DCAT: `data.dcat.dataset_id`
- PROV: `data.prov.activity_id`
- Vintage: `data.vintage`

**Governance**
- `governance.sensitivity`, `governance.classification`
- redaction/generalization summary + enforcement plane(s)
- `governance.care_notes` (required when sensitivity is anything other than public/open)

### Evolution rules
- Do not rename `id`. If the public name needs to change, change `title`, not `id`.
- Prefer additive fields; breaking changes require:
  - a schema/version bump, and
  - a migration note (including any `replaced_by` mapping).
- Removal: mark a layer as deprecated first; keep it for at least one release window unless it is an emergency governance takedown.

### Example minimal registry file

~~~json
{
  "schema_version": "KFM-UI-LAYER-REGISTRY v1.0.0-draft",
  "registry_id": "layers.public",
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
        "interactive": true,
        "legend_ref": "../legends/surficial-geology.legend.json",
        "style_ref": "../styles/fragments/surficial-geology.style.json"
      },
      "data": {
        "vintage": "2025-10-01",
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
        }
      },
      "license": "CC-BY-4.0",
      "attribution": "Source: <publisher>; Processed by KFM",
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

### MapLibre style assets
Two supported patterns are allowed. Choose one and document the rule in code and schema.

1. Full style ref: `ui.style_ref` points to a complete MapLibre style JSON.
2. Fragment ref: `ui.style_ref` points to one or more MapLibre `layer` objects appended to a base style.

If fragments are used, ensure the runtime has a consistent rule for where `sources` are defined (e.g., base style or a dedicated `sources.json`).

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

---

## 🛠️ Layer lifecycle workflow

### Add a new layer checklist
- [ ] Dataset exists as processed output (`data/processed/<domain>/...`) and has stable IDs.
- [ ] STAC collection + item exist under `data/stac/` for the published artifact (or resolvable catalog endpoint).
- [ ] DCAT dataset/distribution exist under `data/catalog/dcat/` and license + attribution were reviewed.
- [ ] PROV bundle exists under `data/prov/` and includes the generating activity/run.
- [ ] API endpoint(s) exist for tiles/features and enforce redaction/generalization as required.
- [ ] Add layer entry to the correct registry (`layers.public.json` vs `layers.restricted.json`).
- [ ] Add style fragment(s), legend, and icon assets; ensure accessibility (contrast, keyboard toggles, readable legend).
- [ ] Run validations (schema checks, referential integrity, API contract tests).
- [ ] If the layer can affect sovereignty/sensitivity, trigger governance review.

### Change an existing layer checklist
- [ ] Keep `id` stable; update `title` and metadata as needed.
- [ ] If data changed, update `data.vintage` and provenance pointers (STAC/DCAT/PROV).
- [ ] If style changed, update fragments and confirm legend remains accurate.
- [ ] If sensitivity changed, fail closed until governance approves publication.

### Deprecate or remove a layer
- [ ] Mark deprecated (and `replaced_by` if applicable).
- [ ] Keep compatibility for at least one release window unless emergency takedown.
- [ ] Update Story Nodes / Focus Mode references that include the layer id.

---

## 🧠 Story Node & Focus Mode Integration

### How this surfaces in Focus Mode
Layers may be referenced as evidence by `layer_id` and used to pre-configure the map for a Story Node or Focus Mode view.

For any enabled layer, Focus Mode SHOULD be able to surface:
- license/attribution,
- data vintage,
- STAC/DCAT/PROV identifiers/refs,
- sensitivity/redaction notes (and an explicit “why” if a layer is blocked).

### Provenance-linked narrative rule
- Focus Mode consumes provenance-linked content only.
- Any derived or aggregated layer must include uncertainty metadata and a resolvable provenance chain.

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
- [ ] Style and legend referential integrity (files exist; fragments compile)
- [ ] STAC/DCAT/PROV validation (for referenced artifacts)
- [ ] API contract tests (tiles/features endpoints)
- [ ] Security and sovereignty checks (PII, sensitive-location leakage, classification propagation)
- [ ] Accessibility checks (legend readability, icon accessibility, keyboard navigation for layer toggles)

### Reproduction

~~~bash
# Placeholders — replace with repo-specific commands.

# 1) validate schemas (UI registries, STAC/DCAT/PROV, etc.)
# 2) run web lint/tests
# 3) run link-check / markdown lint (if configured)
~~~

### Telemetry signals if applicable

| Signal | Source | Where recorded |
|---|---|---|
| `ui.layer.toggle` | Layer toggle UI | `docs/telemetry/` + `schemas/telemetry/` (**not confirmed**) |
| `ui.layer.load_error` | Registry loader / API client | `docs/telemetry/` |
| `ui.audit_panel.open` | Audit/provenance panel | `docs/telemetry/` |

---

## ⚖ FAIR+CARE & Governance

### Governance review triggers
A review is required when:
- A layer is new and or changes sensitivity/classification.
- A layer is derived from restricted inputs or could reveal sensitive locations.
- A layer introduces a new external data source and needs license/provenance review.
- A layer requires a new public-facing endpoint or interaction pattern.

### CARE and sovereignty considerations
- Identify impacted communities and applicable protection rules.
- Prefer coarse and aggregate public products when sovereignty/sensitivity is uncertain.
- Redaction/generalization must be documented and enforced across datasets, catalogs, APIs, and UI.
- Fail closed: do not publish public layers when sensitivity is unresolved.

### AI usage constraints
- Allowed: summarization, structure extraction, translation, keyword indexing.
- Prohibited: generating new policy, inferring sensitive locations.

---

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.1 | 2025-12-28 | Refined registry contract, lifecycle workflow, validation and governance notes | TBD |
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
