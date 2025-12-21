---
title: "🗺️ KFM v12 — Cesium Layer Registry & Mappings"
path: "web/cesium/layers/README.md"
version: "v12.0.0-draft"
last_updated: "2025-12-21"
status: "draft"
doc_kind: "Subsystem Registry"
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

doc_uuid: "urn:kfm:doc:web:cesium:layers:registry:v12.0.0-draft"
semantic_document_id: "kfm-web-cesium-layers-registry-v12.0.0-draft"
event_source_id: "ledger:kfm:doc:web:cesium:layers:registry:v12.0.0-draft"
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

# 🗺️ Cesium Layer Registry & Mappings

## 📘 Overview

### Purpose
This directory is the **governed, declarative registry** that defines which Kansas Frontier Matrix (KFM) datasets, regions, and sensors appear as **CesiumJS layers**, and how they must behave under **provenance**, **auditability**, and **FAIR+CARE / sovereignty** constraints.

KFM’s implementation guidance explicitly anticipates a **JSON layer registry** under `web/cesium/layers/*.json` (or similar) that includes layer definitions such as source URLs, attributions, and sensitivity flags. This README governs the **contract and authoring rules** for that registry.

> **Non-negotiable invariant:** The UI must have “no hidden data leakage.” The registry exists to make what is shown explicit, reviewable, and enforceable.

### Scope

| In Scope | Out of Scope |
|---|---|
| Declarative Cesium layer definitions (tilesets, overlays, sensors, imagery pointers) | Canonical datasets or derived data products (these belong in `data/` with STAC/DCAT/PROV) |
| Layer-level governance metadata: CARE gating, masking strategy, allowed modes | Secrets, tokens, credentials, private endpoints |
| Provenance pointers: dataset IDs, STAC refs, PROV lineage refs | Direct UI access to Neo4j (UI must not read graph directly) |
| CI-validation expectations for registry integrity | Ad-hoc layer creation in app code with no registry entry |

### Audience
- Primary: Frontend engineers implementing Cesium scene + layer toggles.
- Secondary: Reviewers validating governance posture (CARE/sovereignty), provenance surfacing, and attribution compliance.

### Definitions
- Glossary link: `docs/glossary.md` (**not confirmed in repo**)
- Terms used in this doc:
  - **Layer Registry**: declarative JSON that describes what the UI is allowed to render and how it is constrained.
  - **UI asset**: static frontend resources (icons/textures) that ship with the bundle (see `web/cesium/assets/README.md`).
  - **Data-backed asset**: tiles, rasters, vectors, 3D Tiles, etc. produced by the pipeline and served via governed endpoints.
  - **CARE gating**: explicit constraints that prevent sensitive location precision or restricted materials from being exposed.

### Key artifacts

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| This README | `web/cesium/layers/README.md` | Frontend | Registry contract + authoring rules |
| Layer registries | `web/cesium/layers/*.json` | Frontend | Declarative layer entries; CI validated |
| Cesium adapters | `web/cesium/adapters/` (**not confirmed in repo**) | Frontend | Code that maps registry entries → Cesium primitives |
| Cesium runtime assets | `web/cesium/assets/` (**not confirmed in repo**) | Frontend | Icons/textures used by layers and UI |
| Catalog outputs | `data/stac/`, `data/catalog/dcat/`, `data/prov/` (**not confirmed in repo**) | Data/Catalog | Evidence + lineage; referenced by IDs/links |

### Definition of done (for this document)
- [ ] Front-matter complete + valid
- [ ] Registry contract is explicit (fields, invariants, and what must be validated)
- [ ] Governance + CARE/sovereignty behaviors are stated and review-triggering changes are defined
- [ ] Validation expectations are listed and repeatable (schema + cross-link checks)
- [ ] Clear separation between UI config vs. canonical data products (`data/` + catalogs)

---

## 🗂️ Directory Layout

### This document
- `path`: `web/cesium/layers/README.md`

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| Web root | `web/` | React + map clients |
| Cesium root | `web/cesium/` | Cesium viewer + scene orchestration |
| Layer registry | `web/cesium/layers/` | Declarative layer definitions + schemas (this area) |
| Assets | `web/cesium/assets/` | UI runtime assets (icons/textures); not datasets |
| Adapters | `web/cesium/adapters/` | Registry → Cesium mapping layer (**not confirmed in repo**) |
| Data pipeline outputs | `data/` | Raw/work/processed datasets (**not confirmed in repo**) |
| Catalogs + lineage | `data/stac/`, `data/catalog/dcat/`, `data/prov/` | STAC/DCAT/PROV (**not confirmed in repo**) |
| Schemas | `schemas/` | JSON schemas and validators (**not confirmed in repo**) |

### Expected file tree for this sub-area (recommended; not confirmed in repo)
~~~text
📁 web/
└── 📁 cesium/
    └── 📁 layers/
        ├── 📄 README.md                      # This file — registry contract + rules
        ├── 🧱 tilesets.json                  # 3D Tiles layer entries (sites/buildings/terrain tiles)
        ├── 🗺️ regions.json                   # Region overlays (cultural regions, basins, masks)
        ├── 📡 sensors.json                   # Sensor glyphs + telemetry overlays
        ├── 🛰️ imagery.json                   # Optional imagery layers (WMTS/XYZ/COG proxies) (optional)
        └── 🧩 schemas/                       # Optional local schemas (or link to global schemas/)
            ├── 📄 tilesets.schema.v1.json
            ├── 📄 regions.schema.v1.json
            ├── 📄 sensors.schema.v1.json
            └── 📄 imagery.schema.v1.json     # optional
~~~

---

## 🧭 Context

### Background
KFM’s canonical ordering is:

**ETL → STAC/DCAT/PROV → Neo4j → APIs → React/Map UI → Story Nodes → Focus Mode**

This layer registry sits in the **UI stage**, but it must remain **catalog- and provenance-aligned**. The registry should not become an alternate data store.

### Constraints and invariants
- **API boundary:** UI must not access Neo4j directly.
- **No hidden data leakage:** layer visibility and constraints must be explicit and reviewable.
- **Provenance-first:** layer entries must point to dataset/cat/prov identifiers; the UI should surface provenance affordances where applicable.
- **No policy bypass:** registry entries must not be used to bypass catalog + governance by pointing at untracked files.
- **No secrets:** do not commit Cesium Ion tokens, API keys, or private endpoints into registry JSON.

### What gets combined from `assets/README.md`
The layer registry is *configuration*, not *content*:
- UI-only assets (icons/textures) may live under `web/cesium/assets/`.
- Data-backed assets (3D Tiles, rasters, vectors) must be produced and governed in `data/` and served via governed endpoints (exact serving mechanism **not confirmed in repo**).
- Layer entries may reference UI-only assets (icons) but must not embed sensitive or identifying location precision.

---

## 🗺️ Diagrams

### Where the registry sits in KFM
~~~mermaid
flowchart LR
  A[ETL Pipelines] --> B[STAC / DCAT / PROV]
  B --> C[Neo4j Graph]
  C --> D[APIs]
  D --> E[UI: React + Cesium]
  E --> F[Layer Registry JSON]
  F --> G[Cesium Adapters]
  G --> H[Cesium Primitives / Layers]
  E --> I[Story Nodes]
  I --> J[Focus Mode]
~~~

---

## 📦 Data and Metadata

### Inputs
| Input | Format | Where from | Validation |
|---|---|---|---|
| Layer registries | JSON | `web/cesium/layers/*.json` | JSON schema + cross-link checks |
| Provider/source refs | IDs/URLs | Provider config and/or API payloads (**not confirmed in repo**) | Existence + allowlist rules |
| Governance annotations | JSON fields | Layer entries + dataset governance | Review triggers + CI lint |
| UI asset references | relative paths | `web/cesium/assets/` | Link checks + license/NOTICE review |

### Outputs
| Output | Format | Produced by | Notes |
|---|---|---|---|
| Runtime layer menu | in-memory model | UI/adapters | Deterministic ordering + stable IDs |
| Cesium layer objects | CesiumJS primitives | UI/adapters | Must follow registry constraints |
| Audit hooks | UI affordances | UI | Provenance + attribution visibility |

---

## 🌐 STAC, DCAT and PROV Alignment

### Rule of thumb
If a layer corresponds to a real dataset or derived product, it must be traceable to:
- **STAC** collection/item identifiers
- **DCAT** dataset mapping (at least title/description/license/keywords)
- **PROV** lineage bundle/activity for the transform that produced it

### What the registry must capture
Each layer entry must include:
- A **KFM dataset identifier** (or region identifier) suitable for cross-linking
- At least one provenance pointer:
  - `stac_id` (item/collection) or equivalent
  - `prov_ref` (path/URN to PROV bundle) (exact path conventions **not confirmed in repo**)
- An attribution/credit mechanism (either:
  - embedded `attribution` fields, or
  - `attribution_ref` pointing to a NOTICE/credits file) (**not confirmed in repo**)

---

## 🧱 Architecture

### “One fact, one place” for layers
- **Registry JSON** is the single source of truth for *what layers exist and what constraints apply*.
- **Adapters** are the single translation point for *how a registry entry becomes CesiumJS objects*.
- **Catalog/APIs** are the single source of truth for *data, provenance, and redaction rules*.

### Common Layer Entry Contract (v12 conceptual)
The exact schema is enforced by CI (schema location **not confirmed in repo**). This section defines the *intended* shared structure.

~~~json
{
  "id": "flint-hills-region-overlay",
  "kind": "region",
  "title": "Flint Hills Region (Generalized)",
  "kfm_data_id": "urn:kfm:data:region:flint-hills:v1",
  "source": {
    "provider_id": "kfm-public-geo",
    "resource": "regions/flint-hills",
    "url": null
  },
  "ui": {
    "group": "Regions",
    "default_enabled": true,
    "min_zoom": 4,
    "max_zoom": 12,
    "order": 20,
    "icon_ref": "../assets/icons/region.svg"
  },
  "care": {
    "sensitivity": "generalized",
    "visibility_rules": [
      "polygon-generalized",
      "no-exact-boundaries"
    ],
    "notes": "Region overlay only; no site-level detail."
  },
  "provenance": {
    "stac_id": "kfm-region-flint-hills-v1",
    "prov_ref": "data/prov/regions/flint-hills/v1/prov.json"
  },
  "telemetry": {
    "tag": "region:flint-hills",
    "perf_expectation": "low"
  }
}
~~~

> Notes:
> - `source.url` should be optional; prefer provider-based resolution to avoid hardcoding environment-specific endpoints.
> - Any path under `data/` is shown as an example and is **not confirmed in repo**.

### Registry categories
Recommended registries:
- `tilesets.json` — 3D Tiles layers (heritage models, structures, volumetric/environment tiles)
- `regions.json` — region overlays (cultural/hydrologic/admin), masks, boundary generalizations
- `sensors.json` — sensor layers (gauges, stations), including aggregation/anonymization behavior
- `imagery.json` (optional) — imagery providers, time-sliced rasters (if Cesium imagery is used)

### ID stability and backward compatibility
- `id` is a **stable public identifier** for UI state, bookmarks, Story Nodes, and Focus Mode.
- Never rename an existing `id` without a deprecation plan (add alias support in adapters if needed).
- If the schema changes incompatibly, bump schema version and provide a migration path.

---

## 🧠 Story Node & Focus Mode Integration

### Layer registry ↔ Story Nodes
Story Nodes may request map context (e.g., “turn these layers on”) via an adapter-safe mechanism:
- A Story Node should reference layers **by `id`**, not by URLs.
- The UI resolves these `id`s through the registry and applies governance constraints before display.

### Focus Mode rule
Focus Mode must only consume **provenance-linked** content, and any predictive content must be opt-in with uncertainty metadata. The layer registry supports this by requiring provenance pointers and CARE gating on every layer entry.

---

## 🧪 Validation and CI/CD

### Minimum CI expectations (v12-ready)
The Master Guide calls out **UI layer registry schema checks** and **security + sovereignty scanning gates** as minimum CI requirements.

### Registry validation checklist
- [ ] JSON schema validation passes for all `web/cesium/layers/*.json`
- [ ] No duplicate `id`s within or across registries (unless explicit aliasing rules exist)
- [ ] All referenced providers exist (provider config location **not confirmed in repo**)
- [ ] All referenced UI assets exist (icons/textures) and have attribution/NOTICE coverage (recommended)
- [ ] No secrets in registry files (token/key scans)
- [ ] CARE/sovereignty flags do not conflict with dataset governance (enforced either in CI or API contract tests)
- [ ] Provenance refs are present and resolvable (at minimum: non-empty + path/URN format checks)

### “Do not break” rule for this subsystem
- **No hidden data leakage**: any newly visible layer must be explicit in the registry and pass governance review triggers.

---

## ⚖ FAIR+CARE and Governance

### Governance review triggers
Human review is required when changes:
- add a new layer that might expose sensitive locations
- change `care.sensitivity` or `care.visibility_rules`
- introduce a new external provider or endpoint
- add any layer behavior that could increase precision of restricted locations

### CARE and sovereignty considerations
- Prefer **generalization** at the serving layer (API/catalog-governed), not client-side “masking after the fact.”
- If a layer is sensitive:
  - do not ship exact boundaries
  - enforce `min_zoom` / aggregation rules
  - ensure it is disabled in public modes unless explicitly approved
- Do not embed inferred sensitive locations or speculative claims into static registry content.

---

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v12.0.0-draft | 2025-12-21 | v12 rewrite of Cesium layer registry README: registry contract, governance/Care gating, provenance alignment, CI expectations, and adapter boundaries. | TBD |

---
Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`