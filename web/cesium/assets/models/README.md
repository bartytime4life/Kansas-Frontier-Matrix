---
title: "Cesium — Model Assets"
path: "web/cesium/assets/models/README.md"
version: "v1.0.0"
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

doc_uuid: "urn:kfm:doc:web:cesium:assets:models:readme:v1.0.0"
semantic_document_id: "kfm-web-cesium-assets-models-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:web:cesium:assets:models:readme:v1.0.0"
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

# Cesium Model Assets

> **Purpose (required):** This folder holds **static 3D model assets** (or pointers to them) intended for the `web/` Cesium front-end, with clear **licensing, attribution, and provenance expectations**.  
> It is **not** the canonical home for datasets; KFM’s canonical pipeline remains: **ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode**.

---

## 📘 Overview

### What this directory is for
- Small, **license-cleared** 3D assets used by the Cesium UI (e.g., demo scenes, UI fixtures, icons-as-models, reference geometry).
- **Pointers** to larger hosted assets (e.g., a 3D Tiles tileset hosted outside Git) when needed.

### What this directory is not for
- Authoritative, large, or frequently-updated geospatial datasets (those belong under `data/<domain>/{raw,work,processed}/` with catalogs + provenance).
- Any asset that would violate governance constraints (restricted cultural knowledge, precise sensitive locations, PII, embargoed material).

### Minimum rules
- **Every third‑party model MUST carry attribution + license text** in-repo (see “Licensing & Attribution” below).
- **Avoid large binaries in Git**: if a model is too large for the repo, store a *pointer* here (see “External pointers”).
- **No UI direct-to-graph reads**: this folder must not become a backdoor for bypassing the API boundary. UI behavior stays contract-driven.

### Audience
- Frontend contributors working in `web/cesium/**`
- Maintainers reviewing licenses, provenance linkage, and governance compliance

### Definition of done for this document
- [x] Front-matter complete and `path` matches file location
- [x] Directory responsibilities and placement rules documented
- [ ] Any “recommended” subfolders are either created or explicitly treated as optional
- [ ] Maintainer review (license/governance expectations)

---

## 🗂️ Directory Layout

### This document
- `path`: `web/cesium/assets/models/README.md` (must match front-matter)

### Related repository paths (orientation)
| Area | Path | What lives here |
|---|---|---|
| UI | `web/` | React/MapLibre/Cesium front-end |
| UI assets | `web/**/assets/**` | Static assets consumed by the UI build/runtime |
| Layer registry | `web/**/layers/**` | UI layer definitions (schema-validated where applicable) |
| Catalog outputs | `data/stac/` + `data/catalog/dcat/` + `data/prov/` | Canonical STAC/DCAT/PROV artifacts |
| Story Nodes | `docs/reports/story_nodes/` | Governed narrative artifacts that may reference UI assets |

### Expected file tree for this sub-area
> This is a **recommended** structure. Some directories may not exist yet (**not confirmed in repo**).

~~~text
📁 web/
└── 📁 cesium/
    └── 📁 assets/
        └── 📁 models/
            ├── 📄 README.md
            ├── 📁 demo/                         # small, repo-safe fixtures (recommended)
            │   └── 📁 <model_id>/               # one model per folder (recommended)
            │       ├── 📄 model.glb             # preferred: single-file GLB
            │       ├── 📄 model.meta.json       # sidecar metadata (recommended)
            │       └── 📄 LICENSE.md            # required if 3rd-party or non-trivial provenance
            └── 📁 external/                     # pointers to hosted assets (recommended)
                ├── 📄 <model_id>.link.json
                └── 📄 README.md                 # optional notes on hosting/location
~~~

---

## 🧭 Context

### Background
KFM’s UI is downstream of the contract-governed pipeline. Models committed here are treated as **UI assets** (fixtures, demos, or curated visual complements) and should not replace canonical datasets, catalogs, or provenance.

### Assumptions
- Not all subfolders in the “expected tree” exist yet; this README defines a safe baseline structure.
- The Cesium UI may load models either:
  - as static files served from `web/**`, or
  - via API-provided URLs resolved from catalogs (preferred for data-driven assets).

### Constraints / invariants
- **API boundary remains mandatory:** UI must not query Neo4j directly; graph and catalog access is mediated by contracted APIs.
- **No sensitive leakage:** models must not embed restricted locations/knowledge or PII; if the model is derived from sensitive source data, store only an appropriately generalized artifact (or none at all).
- **Stable IDs:** choose stable, non-semantic `model_id` values where possible (avoid IDs that encode sensitive details).

### Open questions
| Question | Owner | Target date |
|---|---|---|
| Do we standardize a `model.meta.json` schema under `schemas/ui/`? | TBD | TBD |
| Do we add a CI check to ensure every model folder includes `LICENSE.md` and no external texture URLs? | TBD | TBD |
| Do we want a single `models.manifest.json` registry for discoverability? | TBD | TBD |

### Future extensions
- Add a build step that **validates** models (glTF validation, size budgets) and optionally emits a UI registry entry.
- Prefer 3D assets to be served as **catalog-linked** resources (STAC assets resolved via API), keeping this directory focused on fixtures/demos.

---

## 🗺️ Diagrams

### Where model assets sit in the KFM flow
~~~mermaid
flowchart LR
  A[ETL] --> B[STAC/DCAT/PROV]
  B --> C[Graph]
  C --> D[APIs]
  D --> E[UI<br/>web + Cesium]

  subgraph StaticAssets[Static UI assets]
    M[web/cesium/assets/models]
  end

  E --> M
~~~

---

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode
- Models in this folder can be used as **visual companions** in UI views (e.g., a Cesium scene that supplements a Story Node).
- Any Story Node that references a model should also reference the **evidence IDs** that justify it (STAC/DCAT/PROV IDs and/or graph entity IDs).

### Provenance-linked narrative rule
- If a model represents a real place/event/asset in KFM, the narrative should be traceable to:
  - a graph entity ID, and
  - a STAC Item (or other catalog artifact), and
  - a PROV activity describing lineage (where applicable).

### Optional structured controls
> These keys are **recommended** conventions only (**not confirmed in repo**). If adopted, formalize via schema under `schemas/ui/`.

~~~yaml
# Example Story Node front-matter additions (illustrative only)
ui:
  viewer: "cesium"
  model_asset_id: "<model_id>"
  model_mode: "static-asset"   # or "api-resolved"
~~~

---

## 🧪 Validation & CI/CD

### Validation steps
Recommended checks before merging new assets:
- [ ] **License present** for every third‑party or non-trivial source model (`LICENSE.md`)
- [ ] **No external fetches** embedded inside the model (textures/URIs should be local or API-resolved)
- [ ] **Size sanity** (keep repo-committed demo models small; prefer external pointers for large assets)
- [ ] **Load test in Cesium** (basic render + expected orientation/scale)

### Local reproduction
> Commands are placeholders (**not confirmed in repo**). Replace with repo-approved tooling.

~~~bash
# 1) optional: run a glTF validator (if available in tooling)
# 2) run UI build / dev server and load the model in Cesium
# 3) run any asset lint checks (file size / license presence) if implemented
~~~

### Telemetry signals
If UI telemetry exists (not confirmed in repo), watch for:
- model load failures (404s, CORS, decode errors)
- frame time regressions
- memory spikes when loading/unloading models

---

## 📦 Data & Metadata

### Inputs
| Input | Format | Notes |
|---|---|---|
| Model geometry | `.glb` / `.gltf` (+ textures) | Prefer `.glb` for simplicity |
| Attribution + license | `LICENSE.md` | Required for third-party models |
| Sidecar metadata | `model.meta.json` | Recommended for discoverability + provenance |

### Outputs
| Output | Format | Notes |
|---|---|---|
| Repo-safe demo assets | `.glb` | Keep small and deterministic |
| External pointer files | `.link.json` | Point to hosted assets instead of committing large binaries |

### Sidecar metadata conventions
> This JSON is a **recommended** shape (**not confirmed in repo**). If adopted, create a schema under `schemas/ui/`.

~~~json
{
  "model_id": "<stable-id>",
  "display_name": "<human-readable name>",
  "asset_type": "glb",
  "relative_url": "./demo/<model_id>/model.glb",
  "license": "<SPDX or text>",
  "attribution": "<required attribution text>",
  "source": {
    "url_or_citation": "<where the model came from>",
    "notes": "<optional>"
  },
  "provenance": {
    "stac_item_id": "<optional>",
    "prov_activity_id": "<optional>",
    "graph_entity_id": "<optional>"
  },
  "placement_hint": {
    "crs": "EPSG:4326",
    "longitude": "<float>",
    "latitude": "<float>",
    "height_m": "<float>",
    "heading_deg": "<float>",
    "pitch_deg": "<float>",
    "roll_deg": "<float>",
    "scale": "<float>"
  }
}
~~~

### Sensitivity & redaction
- Do not embed precise sensitive sites or restricted cultural knowledge in 3D models without explicit governance approval.
- If a model’s placement implies a sensitive location, prefer generalized placement hints (or omit placement hints entirely).

### Quality signals
- Deterministic files (no “mystery” binaries; know the source and license)
- Small footprint for repo-committed demos
- Clean render in Cesium without warnings/errors

---

## 🌐 STAC, DCAT & PROV Alignment

### STAC
- This folder does not automatically emit STAC.
- If a model corresponds to a real dataset/evidence product, the **canonical** STAC Item/Collection should live under:
  - `data/stac/collections/`
  - `data/stac/items/`
- Prefer to reference the STAC Item ID in `model.meta.json` (recommended).

### DCAT
- If the model is part of a published dataset, ensure a DCAT mapping exists under `data/catalog/dcat/`.

### PROV-O
- If the model is derived from raw/processed data, capture lineage via PROV under `data/prov/` (activity linking inputs → outputs).

### Versioning
- For externally hosted assets, version URLs or include immutable identifiers (hash/version) in `.link.json`.
- When models change, update:
  - `version`/`last_updated` here (doc)
  - model-specific metadata (sidecar)
  - any downstream Story Nodes that reference the asset

---

## 🧱 Architecture

### Components
| Component | Responsibility | Notes |
|---|---|---|
| `web/cesium/**` | Cesium UI + scene composition | UI consumes data via API boundary |
| `web/cesium/assets/models/**` | Static models and pointers | Fixtures/demos + curated assets |
| API boundary (`src/server/**`) | Resolve dataset-driven assets | Preferred for STAC-linked assets |

### Interfaces / contracts
- If model assets become discoverable via a UI registry, define a schema in `schemas/ui/` (**not confirmed in repo**).
- If the UI loads models via API, the API contract must specify stable fields (URL, license/attribution, provenance IDs).

### Extension points checklist
- [ ] Add schema for `model.meta.json` (if adopted)
- [ ] Add CI check: license + no external URIs + optional size budget
- [ ] Add registry/manifest for available demo models (if needed)
- [ ] Add Story Node integration pattern with provenance IDs

---

## ⚖ FAIR+CARE & Governance

### Review gates
Changes that typically require elevated review:
- Adding third-party assets with complex licensing
- Adding models derived from sensitive sources (restricted locations, cultural knowledge, PII)
- Any UI behavior that could expose data outside the API boundary

### CARE / sovereignty considerations
- Treat culturally sensitive content as high-risk by default.
- When in doubt, prefer:
  - not committing the model,
  - using generalized or synthetic demo geometry, or
  - gating access behind API-driven redaction controls.

### AI usage constraints
- Do not “invent” provenance or licensing details.
- AI may assist with **documentation** and **metadata structuring**, but the asset’s source, license, and attribution must be human-verified.

---

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---:|---|---|
| v1.0.0 | 2025-12-24 | Initial README for `web/cesium/assets/models/` directory. | TBD |

---

Footer refs (do not remove):
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
