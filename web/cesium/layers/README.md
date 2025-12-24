---
title: "KFM Web Cesium Layer Registry"
path: "web/cesium/layers/README.md"
version: "v0.1.0"
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

doc_uuid: "urn:kfm:doc:web:cesium:layers:readme:v0.1.0"
semantic_document_id: "kfm-web-cesium-layers-readme-v0.1.0"
event_source_id: "ledger:kfm:doc:web:cesium:layers:readme:v0.1.0"
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

# KFM Web Cesium Layer Registry

This directory contains **Cesium layer registry files**: declarative, schema-valid JSON that defines which map layers are available in the KFM 3D experience and how those layers are surfaced in the UI.

The layer registry is a **UI contract surface**. It must preserve KFM invariants:
- UI consumes governed data via the **API boundary** (no direct Neo4j access).
- Sensitive material is controlled via **redaction/generalization** at the API boundary.
- Focus Mode remains **provenance-linked** and auditable.

## 📘 Overview

### Purpose

- Define what belongs in `web/cesium/layers/` (registry/config only).
- Establish **stable layer IDs** for:
  - Cesium rendering,
  - Focus Mode `focus_layers`,
  - cross-mode parity with the 2D map experience (if applicable).
- Make schema-validation and governance expectations explicit.

### Scope

| In Scope | Out of Scope |
|---|---|
| Layer registry JSON files used by Cesium mode | ETL pipelines (`src/pipelines/`) and catalog generation (`data/stac/`, `data/catalog/dcat/`, `data/prov/`) |
| UI-facing metadata: display names, groups, icons, attribution, licensing | Dataset storage or derived products (tiles, COGs, 3D Tiles datasets) |
| Registry validation expectations and “what fields mean” at a high level | API endpoint implementation and contract authoring (`src/server/`) |
| Governance notes for sensitive layers and public release posture | Story Node authoring (canonical home: `docs/reports/story_nodes/`) |

### Audience

- Primary: frontend engineers working on Cesium mode under `web/cesium/`.
- Secondary: API/contract owners and governance reviewers auditing exposure, attribution, and sensitivity flags.

### Definitions

- Glossary: `docs/glossary.md` *(not confirmed in repo — add or repair link if the glossary lives elsewhere)*
- Terms used in this doc:
  - **Layer registry**: declarative JSON that defines UI-available layers (IDs, labels, sources, attribution, sensitivity flags).
  - **Layer ID**: stable identifier used by UI state, Focus Mode controls, and telemetry.
  - **Evidence identifiers**: references to STAC/DCAT/PROV objects supporting traceability.
  - **API boundary**: contracted access layer under `src/server/` mediating graph + catalog content.

### Key artifacts

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master Guide v12 | `docs/MASTER_GUIDE_v12.md` | TBD | Canonical pipeline ordering and invariants |
| Cesium overview | `web/cesium/README.md` | UI | Cesium mode scope and rules |
| Cesium adapters | `web/cesium/adapters/README.md` | UI | Adapter layer consumes registry entries |
| UI schemas | `schemas/ui/` | Schemas + UI | Schema source of truth for registry validation *(not confirmed in repo)* |
| API contracts | `src/server/contracts/` | API | UI consumes contracted endpoints *(not confirmed in repo)* |
| Story Nodes | `docs/reports/story_nodes/` | Curators | Focus Mode narratives reference layer IDs |

### Definition of done

- [ ] Front-matter complete + valid; `path` matches `web/cesium/layers/README.md`
- [ ] Registry files (if present) validate against the canonical UI schema in `schemas/ui/` *(not confirmed in repo)*
- [ ] Layer IDs are stable and documented (no breaking renames without migration notes)
- [ ] Registry entries do not embed datasets or secrets
- [ ] Attribution and licensing fields are present where required by schema
- [ ] Sensitive layers are flagged and gated (do not increase restricted precision)
- [ ] Validation steps are listed and repeatable

## 🗂️ Directory Layout

### This document

- `path`: `web/cesium/layers/README.md` (must match front-matter)

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| Cesium mode | `web/cesium/` | Cesium wiring, adapters, runtime config |
| Cesium registries | `web/cesium/layers/` | This directory: layer registry JSON files |
| Cesium adapters | `web/cesium/adapters/` | Code that translates registry entries into Cesium primitives |
| Cesium runtime assets | `web/cesium/assets/` | UI-only assets used by Cesium mode (icons/textures) |
| API boundary | `src/server/` | Contracted endpoints, redaction/generalization |
| Schemas | `schemas/` | JSON Schemas for catalogs/story/UI/telemetry |
| Story Nodes | `docs/reports/story_nodes/` | Narrative artifacts rendered in Focus Mode |
| Evidence catalogs | `data/stac/` + `data/catalog/dcat/` + `data/prov/` | STAC/DCAT/PROV evidence artifacts |

### Expected file tree for this sub-area

> This is a recommended shape. Keep it synchronized with whatever JSON files actually exist in this directory.

~~~text
📁 web/
└── 📁 cesium/
    └── 📁 layers/
        ├── 📄 README.md
        ├── 📄 regions.json                 # example registry filename (if present)
        ├── 📄 imagery.json                 # optional: raster/imagery entries (if present)
        ├── 📄 tilesets.json                # optional: 3D Tiles entries (if present)
        └── 📄 <other-registry>.json
~~~

## 🧭 Context

### Background

KFM’s canonical pipeline ordering is preserved end-to-end:

**ETL → STAC/DCAT/PROV → Graph → API → UI → Story Nodes → Focus Mode**

The Cesium layer registry is part of the **UI stage**. It exists to provide deterministic, reviewable control over what the UI can render and how it is labeled, attributed, and governed.

### Constraints and invariants

Non-negotiables:

- **No UI direct-to-graph reads**  
  The UI must never query Neo4j directly; all graph and evidence access is mediated by the API boundary.

- **Contract-first behavior**  
  Registry files are validated against schemas (when present). The schema is the source of truth for required fields and allowed values.

- **Provenance-first UX**  
  Where a layer represents real data, the UI should be able to show evidence identifiers (STAC/DCAT/PROV IDs) as “audit affordances”.

- **Sensitivity posture**  
  Registry entries must not encode or reveal restricted-precision locations. If a layer is sensitive, it must be flagged and gated.

### What does not belong here

- Raw or processed datasets (GeoJSON, COGs, Parquet, 3D Tiles datasets, terrain sets)
- STAC/DCAT/PROV JSON outputs (canonical homes are under `data/`)
- Cached API responses
- Secrets or tokens (e.g., Cesium Ion tokens)

## 🧩 Layer registry contract

### Source of truth

- The canonical registry schema should live under `schemas/ui/` *(not confirmed in repo)*.
- This README documents **intent and invariants**, not the authoritative field list.

### Recommended file-level structure

Registry files are typically either:

1) A root object with metadata + `layers[]`, or  
2) A plain JSON array of layer objects.

Prefer a shape that supports schema validation and versioning.

Illustrative example only (confirm exact schema fields under `schemas/ui/`):

~~~json
{
  "registry_version": "v0.1.0",
  "layers": [
    {
      "id": "kfm-example-layer",
      "name": "Example Layer",
      "kind": "imagery",
      "source": {
        "type": "api",
        "ref": "/v1/layers/kfm-example-layer"
      },
      "attribution": "TBD",
      "license": "TBD",
      "sensitivity": {
        "classification": "public",
        "requires_auth": false
      },
      "provenance": {
        "stac_item_id": "TBD",
        "dcat_dataset_id": "TBD",
        "prov_activity_id": "TBD"
      }
    }
  ]
}
~~~

### Stable layer ID rules

- `id` must be globally unique within the registry set.
- IDs must be:
  - deterministic,
  - stable across releases,
  - safe for inclusion in URLs and Story Node Focus controls.
- If an ID must change, provide a migration mapping (location and mechanism not confirmed in repo).

### Provenance fields

If a layer is derived from or backed by governed evidence, prefer including evidence identifiers returned by the API (or resolvable through it):

- STAC Item/Collection IDs
- DCAT dataset IDs
- PROV activity/run IDs

The UI should surface these in an audit panel rather than burying them in tooltips.

### Governance and sensitivity fields

Registry entries should support (and the UI should enforce) at least:

- classification / sensitivity
- access gating (auth required, role required)
- redaction/generalization flags (authoritative at API boundary)
- disclaimers for preliminary/unverified sources (if applicable)

Do not attempt to “implement policy” client-side. The registry provides hints; the API boundary enforces rules.

## 🧠 Story Node and Focus Mode Integration

### Focus Mode controls

Story Nodes may include optional structured controls that reference layer IDs:

~~~yaml
focus_layers:
  - "kfm-example-layer"
focus_time: "1854-01-01/1854-12-31"
focus_center: [ -98.0000, 38.0000 ] # lon, lat (example only)
~~~

Rules:

- Layer IDs in Story Nodes should resolve to a registry entry.
- If a referenced layer is sensitive or access-controlled, the Focus Mode UI must respect gating and avoid leaking restricted detail.

### Cross-mode parity

If the UI supports both 2D and 3D modes, prefer reusing stable IDs and mapping each ID to its 2D/3D implementation via adapters rather than inventing separate “Cesium IDs” and “Map IDs”.

## 🗺️ Diagrams

### Registry-driven rendering flow

~~~mermaid
flowchart LR
  A["web/cesium/layers/*.json"] --> B["Schema validation (schemas/ui)"]
  B --> C["Layer loader"]
  C --> D["Cesium adapters"]
  D --> E["Cesium viewer"]
  F["API boundary (src/server)"] --> D
  F --> G["Audit panel (provenance)"]
~~~

### Focus Mode sequence with layers

~~~mermaid
sequenceDiagram
  participant UI as Web UI
  participant API as API boundary
  participant Graph as Graph and catalogs

  UI->>API: GET /focus?entity_id=...
  API->>Graph: fetch context + evidence refs (apply redaction)
  Graph-->>API: context bundle + provenance IDs
  API-->>UI: focus bundle (narrative + focus_layers + citations)
  UI->>UI: resolve focus_layers -> registry entries
  UI->>UI: render layers via Cesium adapters
~~~

## 📦 Data and Metadata

### Inputs

| Input | Format | Source | Validation |
|---|---|---|---|
| Layer registry files | JSON | `web/cesium/layers/` | JSON Schema in `schemas/ui/` *(if present)* |
| Layer data endpoints | JSON/tile streams | API boundary | Contract tests + runtime guards |
| Evidence identifiers | IDs | API payload | Must be renderable and auditable |

### Outputs

| Output | Format | Where | Notes |
|---|---|---|---|
| 3D layer render | runtime | browser | driven by registry + adapters |
| Audit/provenance view | runtime | browser | driven by API evidence identifiers |

## 🌐 STAC, DCAT and PROV Alignment

The registry does not replace catalogs. It points to governed sources:

- STAC/DCAT/PROV artifacts live under canonical `data/` roots.
- The UI accesses those artifacts via API endpoints (or governed public endpoints) so that governance and redaction remain enforceable.
- Prefer propagating evidence identifiers into UI surfaces (sources panels, audit chips, provenance drawers).

## 🧪 Validation and CI

### Validation checklist

- [ ] JSON registry validates against schema (if schema exists)
- [ ] No secrets or tokens in registry files
- [ ] No internal-only hostnames or private endpoints
- [ ] Attribution/license fields present where required
- [ ] Sensitive layers flagged and gated
- [ ] Focus Mode layer IDs resolve (no orphan `focus_layers` references)

### Reproduction

~~~bash
# Example placeholders — replace with repo-specific commands

# validate layer registries against UI schemas
# make validate-ui-layers

# run web lint/tests
# cd web && (npm|pnpm|yarn) test
~~~

## ⚖ FAIR+CARE and Governance

### Review triggers

Changes in this directory require elevated review when they:

- add a new public-facing layer
- modify sensitivity/gating fields
- point at a new data source or endpoint
- change provenance/attribution fields

### CARE and sovereignty considerations

- Do not add layers that reveal culturally sensitive or restricted locations.
- Do not “upgrade precision” client-side by combining multiple partial signals.
- Prefer API-enforced redaction/generalization and treat it as authoritative.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v0.1.0 | 2025-12-24 | Initial README for Cesium layer registry directory | TBD |

---

Footer refs:
- Master guide: `docs/MASTER_GUIDE_v12.md`
- Cesium overview: `web/cesium/README.md`
- Cesium adapters: `web/cesium/adapters/README.md`
- UI schemas: `schemas/ui/` (not confirmed in repo)
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`