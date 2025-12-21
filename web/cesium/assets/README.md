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
This directory contains **frontend-runtime assets** used by the Cesium client under `web/cesium/`.

Assets here exist to support:
- Cesium viewer UX (icons, small UI textures, UI images)
- runtime resources that must ship with the frontend bundle
- optional demo/fixture assets used strictly for UI development and tests (if applicable)

This directory is **not** the canonical home for KFM datasets. Canonical data and derived outputs must follow KFM’s pipeline and catalog rules.

### Scope
| In Scope | Out of Scope |
|---|---|
| UI assets used directly by the Cesium frontend | Canonical datasets or derived data products |
| Small static files that must be served with the app | Anything requiring STAC/DCAT/PROV generation but stored only here |
| Attribution + license documentation for third-party UI assets | Secrets, credentials, tokens, or user-provided uploads |

### Audience
- Primary: Frontend engineers implementing Cesium UI behaviors and layer visuals.
- Secondary: Curators/reviewers validating license, attribution, and sensitivity posture of shipped UI assets.

### Definitions (link to glossary)
- Glossary link: `docs/glossary.md` (not confirmed in repo)
- Terms used in this doc:
  - **UI asset**: static file shipped with the frontend (icons, images, fonts, small textures, small JSON fixtures).
  - **Data asset**: dataset or derived artifact that belongs in `data/` with STAC/DCAT/PROV, even if rendered in the UI.
  - **Attribution bundle**: minimal record of a third-party asset’s origin, license, and required credit.
  - **Asset inventory**: a machine-readable list of shipped assets and their compliance metadata (recommended; not confirmed in repo).

### Key artifacts
| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| This README | `web/cesium/assets/README.md` | Frontend | Directory purpose, constraints, and review gates |
| Cesium adapters README | `web/cesium/adapters/README.md` | Frontend | Adapters should reference assets in a bundler-safe way |
| Cesium layer registry | `web/cesium/layers/` | Frontend | Data-backed layers are registered here; not confirmed in repo |
| Canonical datasets | `data/raw/`, `data/work/`, `data/processed/` | Data/ETL | Do not bypass |
| Catalog outputs | `data/stac/`, `data/catalog/dcat/`, `data/prov/` | Data/Catalog | Provenance-first evidence |
| Schemas | `schemas/` | Platform | Registry schemas + telemetry schemas (if present) |

### Definition of done (for this document)
- [ ] No secrets or tokens stored in this directory
- [ ] Third-party assets have recorded license + attribution (see recommendations below)
- [ ] Assets do not contain sensitive locations or increase restricted precision
- [ ] Anything that is actually a dataset is routed through `data/` + STAC/DCAT/PROV, not committed only here
- [ ] Asset references in code are stable and compatible with the frontend bundler (no fragile runtime paths)
- [ ] Validation steps are listed and repeatable

## 🗂️ Directory Layout

### This document
- `path`: `web/cesium/assets/README.md`

### Related repository paths
| Area | Path | What lives here |
|---|---|---|
| Frontend | `web/` | React + map clients |
| Cesium | `web/cesium/` | Cesium viewer + scene + layer wiring |
| Cesium assets | `web/cesium/assets/` | Static UI runtime assets (this folder) |
| Cesium adapters | `web/cesium/adapters/` | Cesium-specific adapter layer (loads/uses assets) |
| Cesium layers | `web/cesium/layers/` | Declarative layer registry (data-backed) |
| Data | `data/` | Raw/work/processed datasets |
| Catalogs | `data/stac/`, `data/catalog/dcat/`, `data/prov/` | STAC/DCAT/PROV outputs |
| Schemas | `schemas/` | Validation schemas (incl. UI registries if present) |

### Expected file tree for this sub-area
~~~text
📁 web/
└── 📁 cesium/
    └── 📁 assets/
        ├── 📄 README.md                 — this file
        ├── 📁 icons/                    — UI icons (SVG/PNG)
        ├── 📁 textures/                 — small textures used by Cesium materials
        ├── 📁 images/                   — small UI images (optional convention)
        ├── 📁 models/                   — small demo models only (glTF); avoid large binaries
        ├── 📁 fixtures/                 — dev/test fixtures (non-production), if applicable
        ├── 📄 NOTICE.md                 — third-party attribution bundle (recommended)
        └── 📄 assets.manifest.json      — machine-readable asset inventory (recommended)
~~~

Notes:
- Subfolders above are **recommended** conventions; actual contents are not confirmed in repo.
- If large binary assets are required, prefer a governed artifact store and reference via API/CDN (mechanism not confirmed in repo).

## 🧭 Context

### Background
KFM’s canonical ordering is:

ETL → STAC/DCAT/PROV catalogs → Neo4j graph → APIs → React/Map UI → Story Nodes → Focus Mode.

This directory sits in the **UI stage**. Its purpose is to support rendering and UI behavior—not to become an alternate data lake.

### Assumptions
- The frontend build system can bundle or statically serve assets under `web/` (build tooling not confirmed in repo).
- Cesium adapters and UI components can reference assets using bundler-safe paths or imports.
- Public deployments must not ship restricted-precision location material as “UI assets.”

### Constraints and invariants
- **API boundary**: the UI must not access Neo4j directly.
- **Provenance-first**: if the UI renders data derived from real sources, provenance must be present via catalogs and API payloads.
- **No policy bypass**: assets here must not be used as a shortcut around `data/` staging or catalog generation.
- **Security**: do not store credentials, tokens, or private endpoints in committed asset files.
- **Sensitivity**: do not store precise restricted locations or materials that increase sensitive location precision.

### Two classes of assets
1) **UI-only assets (allowed here)**
   - Icons, images, textures, fonts, small static UI helper files.
   - Governed primarily by license/attribution and security constraints.

2) **Data-backed assets (generally not allowed here as canonical)**
   - Raster/tiles, vector layers, 3D Tiles datasets, terrain sets, historical maps as data products.
   - Canonical location must be `data/` with STAC/DCAT/PROV, and the UI should reference them through the API layer (or a governed public asset endpoint served by the system).

If a Cesium feature needs a URL to a data-backed asset, that URL should be produced/served by the system’s catalog + API layer, not hardcoded to an untracked file.

### Open questions
| Question | Why it matters | Owner | Status |
|---|---|---|---|
| Is there an enforced max file size for assets committed under `web/cesium/assets/`? | Prevents repo bloat and slow CI | TBD | TBD |
| Is `assets.manifest.json` required or optional? | Enables auditable licensing + scanning | TBD | TBD |
| Where should large UI binaries live (if needed)? | Prevents “UI assets” becoming a shadow data lake | TBD | TBD |
| What CI checks exist for asset license compliance? | Ensures CC-BY/MIT/etc obligations are met | TBD | TBD |

### Future extensions
- Add a schema for `assets.manifest.json` under `schemas/web/` (not confirmed in repo).
- Add CI gates:
  - file size limits
  - third-party license scan / NOTICE enforcement
  - image metadata scan to prevent accidental sensitive precision or EXIF leakage
- Add “asset hashing” in build output for deterministic caching and reproducibility (implementation not confirmed).

## 🗺️ Diagrams

### UI asset flow (high level)
~~~mermaid
flowchart LR
  A[web/cesium/assets/*] --> B[Frontend build pipeline]
  B --> C[Deployed static assets]
  C --> D[Cesium Viewer + UI Components]
  D --> E[User-visible UI (icons/textures)]
~~~

### Relationship to adapters + data pipeline
~~~mermaid
flowchart LR
  subgraph Data_Pipeline["Data pipeline (canonical)"]
    R[Raw sources] --> ETL[ETL]
    ETL --> Catalogs[STAC/DCAT/PROV]
    Catalogs --> API[API layer]
  end

  subgraph UI["UI (web/)"]
    Assets[web/cesium/assets] --> Build[Build/Bundle]
    API --> Adapters[web/cesium/adapters]
    Build --> Adapters
    Adapters --> Viewer[Cesium Viewer]
  end
~~~

## 📦 Data and Metadata

### Inputs
| Input | Format | Where from | Validation |
|---|---|---|---|
| UI asset files | SVG/PNG/JPG/glTF/JSON/etc. | Repo | Lint + link checks + size checks (if implemented) |
| Third-party attribution | Markdown/JSON | Repo | Review + license check |
| Data-backed layer references | URLs + IDs | API payload | Contract tests |

### Outputs
| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Shipped static assets | Bundled/static served files | Build output | Build-system rules (not confirmed in repo) |
| Attribution surfacing | UI help/about panel content | UI | UI contract (not confirmed in repo) |

### Recommended metadata (not confirmed in repo)
To keep compliance auditable, it is recommended to include one or both:
- `NOTICE.md` listing third-party assets and required attribution
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

### Sensitivity and redaction
- Do not store precise site coordinates, detailed boundary polygons, or sensitive overlays as “static assets.”
- Do not add images/models that materially increase the precision of restricted locations.
- Avoid embedded metadata that could leak sensitive context (e.g., EXIF/GPS) unless explicitly sanitized (sanitization mechanism not confirmed in repo).

### Quality signals
- Deterministic references: stable filenames and stable import paths.
- Asset sizes remain small and reviewable.
- License/attribution coverage for any third-party items.

## 🌐 STAC, DCAT and PROV Alignment

### Rule of thumb
If an asset represents a **dataset** or **derived evidence product**, it must be cataloged:
- STAC: `data/stac/collections/` + `data/stac/items/`
- DCAT: `data/catalog/dcat/`
- PROV: `data/prov/` lineage bundles

### What the UI should do
- Treat STAC/DCAT/PROV identifiers returned by the API as **read-only evidence**.
- Surface these identifiers in audit UI where applicable.
- Avoid client-side “fix ups” to catalog metadata.

## 🧱 Architecture

### Responsibilities
This directory is responsible for:
- small, static, frontend-shipped resources used by Cesium UI
- ensuring third-party assets are attributable and license-compliant
- ensuring asset usage does not violate sensitivity posture (public/open)

This directory is not responsible for:
- hosting or versioning canonical datasets
- serving tiles/3D Tiles/rasters as data products outside catalogs and APIs
- storing secrets, tokens, private endpoints, or user uploads

### How assets should be referenced (guidance)
- Prefer build-system compatible references (imports/URL helpers) so caching and bundling are reliable.
- Avoid hardcoded absolute paths that break under base-path changes.
- Keep runtime references deterministic and reviewable.

Example reference pattern (bundler-dependent; not confirmed in repo):

~~~ts
// Example only — actual loader/import behavior depends on the frontend toolchain.
import markerIconUrl from "../assets/icons/marker.svg";

// ...use markerIconUrl in UI or adapter code
~~~

### What must never live here
- Cesium Ion tokens, API keys, OAuth client secrets
- private endpoints or internal hostnames
- user uploads or raw sensitive records
- large datasets that should be governed through KFM’s pipeline

### Performance notes
- Keep textures and images small; prefer vector icons where possible.
- Avoid committing large binary models; treat `models/` as demo-only unless explicitly governed.
- If a layer needs large textures/models, source them via governed endpoints (API/CDN), not from this folder.

## 🧠 Story Node and Focus Mode Integration

Assets may be used by:
- Story Node rendering UI (icons, small decorative images)
- Focus Mode UI controls (toggle icons, legend icons)

Rules:
- Story Nodes must remain provenance-linked for factual claims; UI assets must not introduce new factual claims.
- Do not embed sensitive location clues in static UI assets used by Story Nodes or Focus Mode.

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