---
title: "Cesium Assets — README"
path: "web/cesium/assets/README.md"
version: "v0.1.0"
last_updated: "2025-12-21"
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

doc_uuid: "urn:kfm:doc:web:cesium:assets:readme:v0.1.0"
semantic_document_id: "kfm-web-cesium-assets-readme-v0.1.0"
event_source_id: "ledger:kfm:doc:web:cesium:assets:readme:v0.1.0"
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

# Cesium Assets

## 📘 Overview

### Purpose
This directory contains **frontend-runtime assets** used by the Cesium client in `web/cesium/`.

Assets in this directory are intended to support:
- Cesium viewer UX (icons, UI textures, small static resources)
- Cesium runtime configuration needs that must ship with the frontend bundle
- Optional demo or fixture assets used strictly for UI development and tests (if applicable)

This directory is **not** the canonical home for KFM datasets. KFM datasets and derived outputs must follow the canonical pipeline staging and cataloging rules.

### Scope
| In Scope | Out of Scope |
|---|---|
| UI assets used directly by the Cesium frontend | Canonical datasets or derived data products |
| Small static files that must be served with the app | Anything requiring STAC/DCAT/PROV generation but stored only here |
| Attribution + license documentation for third-party UI assets | Secrets, credentials, tokens, or user-provided uploads |

### Audience
- Primary: Frontend engineers implementing Cesium UI behaviors and layers.
- Secondary: Curators and reviewers validating license, attribution, and sensitivity posture for shipped UI assets.

### Definitions
- Glossary link: `docs/glossary.md` (not confirmed in repo)
- Terms used in this doc:
  - **UI asset**: a static file shipped with the frontend for rendering or UI behavior (icons, images, fonts, small JSON fixtures).
  - **Data asset**: a dataset or derived artifact that belongs in `data/` with catalog + provenance, even if rendered in the UI.
  - **Attribution bundle**: a minimal record of a third-party asset’s origin, license, and required credit.

### Key artifacts
| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| This README | `web/cesium/assets/README.md` | Frontend | Directory purpose + rules |
| Cesium client root | `web/cesium/` | Frontend | Viewer + adapter wiring |
| Canonical dataset staging | `data/raw/`, `data/work/`, `data/processed/` | Data/ETL | Do not bypass |
| Catalog outputs | `data/stac/`, `data/catalog/dcat/`, `data/prov/` | Data/Catalog | Provenance-first |

### Definition of done
- [ ] No secrets or tokens stored in this directory
- [ ] Third-party assets have a recorded license + attribution (see recommendations below)
- [ ] Assets do not contain sensitive locations or reconstruct restricted precision
- [ ] Anything that is actually a dataset is routed through `data/` + STAC/DCAT/PROV, not committed only here
- [ ] Asset references in code are stable and compatible with the frontend bundler (no fragile runtime paths)

## 🗂️ Directory Layout

### This document
- `path`: `web/cesium/assets/README.md`

### Related repository paths
| Area | Path | What lives here |
|---|---|---|
| Frontend | `web/` | React + map clients |
| Cesium | `web/cesium/` | Cesium viewer + scene + layer wiring |
| Cesium adapters | `web/cesium/adapters/` | Cesium-specific adapter layer |
| Data | `data/` | Raw/work/processed datasets |
| Catalogs | `data/stac/`, `data/catalog/dcat/`, `data/prov/` | STAC/DCAT/PROV outputs |
| Schemas | `schemas/` | Validation schemas (incl. UI registries if present) |

### Expected file tree for this sub-area
~~~text
📁 web/
└── 📁 cesium/
    └── 📁 assets/
        ├── 📄 README.md
        ├── 📁 icons/                 — UI icons (SVG/PNG)
        ├── 📁 textures/              — small textures used by Cesium materials
        ├── 📁 models/                — small demo models only (glTF); avoid large binaries
        ├── 📁 fixtures/              — test/dev fixtures (non-production), if applicable
        ├── 📄 NOTICE.md              — third-party attribution bundle (recommended)
        └── 📄 assets.manifest.json   — machine-readable asset inventory (recommended)
~~~

Notes:
- Subfolders above are **recommended** conventions; actual contents are not confirmed in repo.
- If large binary assets are required, prefer a governed artifact store and reference via API or CDN, not direct repo commits (exact mechanism not confirmed in repo).

## 🧭 Context

### Background
KFM’s canonical ordering is:

ETL → STAC/DCAT/PROV catalogs → Neo4j graph → APIs → React/Map UI → Story Nodes → Focus Mode.

This directory sits in the **UI stage**. Its purpose is to support rendering and UI behavior—not to become an alternate data lake.

### Constraints and invariants
- **API boundary**: the UI must not access Neo4j directly.
- **Provenance-first**: if the UI renders data derived from real sources, provenance must be present via catalogs and API payloads.
- **No policy bypass**: assets in this directory must not be used as a shortcut around `data/` staging or catalog generation.
- **Security**: do not store credentials, tokens, or private endpoints in committed asset files.
- **Sensitivity**: do not store precise restricted locations or materials that increase sensitive location precision.

### Two classes of assets
1) **UI-only assets (allowed here)**
   - Icons, images, textures, small static UI helper files.
   - These are governed primarily by license/attribution and security constraints.

2) **Data-backed assets (generally not allowed here as canonical)**
   - Raster/tiles, vector layers, 3D Tiles datasets, terrain sets, historical maps as data products.
   - Canonical location must be `data/` with STAC/DCAT/PROV, and the UI should reference them through the API layer (or a governed public asset endpoint served by the system).

If a Cesium layer needs a URL to a data-backed asset, that URL should be produced/served by the system’s catalog + API layer, not hardcoded to an untracked file.

## 📦 Data and Metadata

### Inputs
| Input | Format | Where from | Validation |
|---|---|---|---|
| UI asset files | SVG/PNG/JPG/JSON/etc. | Repo | Lint + link checks |
| Third-party attribution | Markdown/JSON | Repo | Review + license check |
| Data-backed layer references | URLs + IDs | API payload | Contract tests |

### Outputs
| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Shipped static assets | Bundled/static served files | Build output | Build-system rules |
| Attribution surfacing | Rendered notice/help UI | UI | UI contract (not confirmed in repo) |

### Recommended metadata
To keep compliance auditable, it is recommended (not confirmed in repo) to include one of:
- `NOTICE.md` listing third-party assets and their required attribution
- `assets.manifest.json` with per-asset metadata

Example manifest shape (reference only):

~~~json
{
  "version": "1.0",
  "assets": [
    {
      "path": "icons/example.svg",
      "type": "ui-icon",
      "source": "TBD",
      "license": "TBD",
      "attribution": "TBD",
      "notes": "UI-only asset"
    }
  ]
}
~~~

## 🌐 STAC, DCAT and PROV Alignment

### Rule of thumb
- If an asset represents a **dataset** or **derived evidence product**, it must be cataloged:
  - STAC: `data/stac/collections/` + `data/stac/items/`
  - DCAT: `data/catalog/dcat/`
  - PROV: `data/prov/` lineage bundles

### What the UI should do
- Treat STAC/DCAT/PROV identifiers returned by the API as **read-only evidence**.
- Surface these identifiers in audit UI where applicable.
- Avoid client-side “fix ups” to catalog metadata.

## 🧱 Architecture

### How assets should be referenced
- Prefer build-system compatible references (import/URL helpers) so caching and bundling are reliable.
- Avoid hardcoded absolute paths that break under base path changes.
- Keep runtime references deterministic and reviewable.

### What must never live here
- Cesium Ion tokens, API keys, OAuth client secrets, private endpoints
- User uploads or raw sensitive records
- Large datasets that should be governed through KFM’s pipeline

## 🧪 Validation and CI

### Validation checklist
- [ ] All third-party assets have license and attribution recorded
- [ ] No secrets committed (scan for tokens/keys)
- [ ] Asset filenames are stable and do not imply PII
- [ ] No restricted/sensitive location precision is introduced by static assets
- [ ] Any data-backed assets are referenced via API/catalog outputs, not only via `web/cesium/assets/`

### Reproduction
~~~bash
# Example placeholders — replace with repo-specific commands
# 1) frontend lint/typecheck
# 2) static asset link check
# 3) secret scan
# 4) license/notice validation (if implemented)
~~~

## ⚖ FAIR+CARE and Governance

### Review gates
Changes here require human review if they:
- add new third-party assets (license/compliance)
- add assets that could reveal sensitive locations
- introduce new patterns for loading data outside the API/catalog pipeline

### CARE and sovereignty considerations
- Do not add assets that increase the resolution of protected cultural or sensitive sites.
- Prefer server-side generalization and governed access controls where necessary.

### AI usage constraints
- Static assets must not embed inferred sensitive locations or speculative claims.
- AI assistance may summarize and structure asset documentation, but must not invent licenses or provenance.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v0.1.0 | 2025-12-21 | Initial Cesium assets README | TBD |

---
Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
