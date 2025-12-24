---
title: "Cesium Assets — README"
path: "web/cesium/assets/README.md"
version: "v0.1.1"
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

doc_uuid: "urn:kfm:doc:web:cesium:assets:readme:v0.1.1"
semantic_document_id: "kfm-web-cesium-assets-readme-v0.1.1"
event_source_id: "ledger:kfm:doc:web:cesium:assets:readme:v0.1.1"
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

This directory contains **frontend runtime assets** used by the Cesium client under `web/cesium/`.

Assets here exist to support:
- Cesium viewer UX (icons, small UI textures, small UI images)
- runtime resources that must ship with (or be referenced by) the frontend bundle
- optional **demo/fixture** assets used strictly for UI development and tests (if applicable)

This directory is **not** the canonical home for KFM datasets. Canonical data and derived outputs must follow KFM’s governed pipeline and catalog rules.

**Canonical ordering (non‑negotiable):**  
**ETL → STAC/DCAT/PROV → Graph → API → UI → Story Nodes → Focus Mode**

### Scope

| In Scope | Out of Scope |
|---|---|
| UI-only assets used directly by the Cesium frontend (icons, textures, small images) | Canonical datasets or derived evidence products (tilesets, rasters, vectors, historical map scans as data products) |
| Small static files that must ship with the UI build | Anything that *should* be cataloged (STAC/DCAT/PROV) but is committed only here |
| Attribution + license documentation for third-party UI assets | Secrets, credentials, tokens (e.g., Cesium Ion tokens), or user-provided uploads |
| Dev/test fixtures that contain no sensitive locations and no real evidence content | Cached API responses, catalog JSON outputs, or any “evidence bundles” |

### Audience
- Primary: Frontend engineers implementing Cesium UI behaviors, adapters, and layer visuals.
- Secondary: Reviewers validating license/attribution and sensitivity posture of shipped UI assets.

### Definitions

- Glossary: `docs/glossary.md` *(not confirmed in repo — add or repair link if glossary lives elsewhere)*

Terms used in this doc:
- **UI asset**: Static file shipped with or referenced by the frontend (icons, images, fonts, small textures, small JSON fixtures).
- **Data asset**: Dataset or derived artifact that belongs in `data/**` with STAC/DCAT/PROV, even if rendered in the UI.
- **Attribution bundle**: Minimal record of a third-party asset’s origin, license, and required credit.
- **Asset inventory**: A machine-readable list of shipped assets and their compliance metadata (recommended; not confirmed in repo).

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Cesium area README | `web/cesium/README.md` | UI | 3D mode scope + invariants |
| Cesium adapters README | `web/cesium/adapters/README.md` | UI | Adapter conventions + lifecycle |
| Web public assets README | `web/public/README.md` | UI | Rules for assets served **verbatim** |
| UI schemas | `schemas/ui/` | Schemas/Contracts | Layer registry + UI contract validation (if present) |
| Catalog outputs | `data/stac/`, `data/catalog/dcat/`, `data/prov/` | Data/Catalog | Canonical evidence artifacts |
| Governance refs | `docs/governance/*` | Governance | Review gates + sovereignty policy |

### Definition of done (for this document)

- [ ] No secrets or tokens stored in this directory
- [ ] Third-party assets have recorded license + attribution (see “Attribution & licensing” below)
- [ ] Assets do not contain sensitive locations or increase restricted precision
- [ ] Anything that is actually a dataset is routed through `data/**` + STAC/DCAT/PROV, not committed only here
- [ ] Asset references in code are stable and compatible with the frontend bundler (no fragile runtime paths)
- [ ] Validation steps are listed and repeatable (even if commands are placeholders)

## 🗂️ Directory Layout

### This document
- `path`: `web/cesium/assets/README.md` (must match front-matter)

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| Frontend | `web/` | React + map clients |
| Cesium | `web/cesium/` | Cesium viewer + scene + adapters + registries |
| Cesium assets | `web/cesium/assets/` | Static UI runtime assets (this folder) |
| Cesium adapters | `web/cesium/adapters/` | Cesium-specific adapter layer (loads/uses assets) |
| Cesium layers | `web/cesium/layers/` | Declarative layer registry (data-backed) |
| Data | `data/` | Canonical raw/work/processed datasets (not UI assets) |
| Catalogs | `data/stac/`, `data/catalog/dcat/`, `data/prov/` | Evidence metadata + provenance bundles |
| Schemas | `schemas/` | Validation schemas (incl. UI registries if present) |
| Story Nodes | `docs/reports/story_nodes/` | Narrative artifacts (rendered in UI via API) |

### Expected file tree for this sub-area

Recommended conventions (update to match actual contents):

~~~text
📁 web/
└── 📁 cesium/
    └── 📁 assets/
        ├── 📄 README.md                 # this file
        ├── 📁 icons/                    # UI icons (SVG/PNG)
        ├── 📁 textures/                 # small textures used by Cesium materials
        ├── 📁 images/                   # small UI images (optional convention)
        ├── 📁 models/                   # demo models only (glTF); avoid large binaries
        ├── 📁 fixtures/                 # dev/test fixtures (non-production), if applicable
        ├── 📄 NOTICE.md                 # third-party attribution bundle (recommended)
        └── 📄 assets.manifest.json      # machine-readable asset inventory (recommended)
~~~

Notes:
- Subfolders/files above are **recommended** conventions; actual contents are not confirmed in repo.
- If large binary assets are required, prefer a governed artifact store and reference via API/CDN (mechanism not confirmed in repo).

## 🧭 Context

### Background

KFM’s pipeline is **evidence-first** and **provenance-linked**:

**ETL → STAC/DCAT/PROV → Graph → API → UI → Story Nodes → Focus Mode**

This directory is in the **UI stage**. Its purpose is to support rendering and UI behavior — not to become an alternate data lake.

### Assumptions
- The frontend build toolchain can bundle or statically serve assets under `web/` (exact tooling not confirmed in repo).
- Cesium adapters and UI components reference assets using bundler-safe paths/imports.
- Public deployments must not ship restricted-precision location material as “UI assets.”

### Constraints and invariants

- **API boundary:** the UI must not access Neo4j directly (graph access is via `src/server/`).
- **Provenance-first:** if the UI renders data derived from real sources, provenance must be present via catalogs and API payloads.
- **No policy bypass:** assets here must not be used as a shortcut around `data/**` staging or catalog generation.
- **Security:** do not store credentials, tokens, or private endpoints in committed asset files.
- **Sensitivity:** do not store assets that encode or increase the precision of restricted locations.

## ✅ What belongs here

### Allowed UI-only assets (examples)
- Icons (SVG/PNG) used by the Cesium UI chrome (buttons, legends, markers)
- Small textures used for Cesium materials (patterns, alpha masks) that carry no sensitive meaning
- Placeholder images (generic; not dataset-derived)
- Demo models used only for local development (non-sensitive and properly licensed)

### Not allowed as canonical content (examples)
- 3D Tiles datasets, terrain sets, orthomosaics, rasters, vector layers, historic map scans as data products
- STAC/DCAT/PROV outputs
- Cached API responses or “prebaked” evidence bundles
- Any asset that materially increases restricted location precision (annotated maps, site diagrams, labeled boundaries under restriction)

### Quick decision rule
If the file is used to communicate **evidence** (what happened/where/when) rather than **presentation** (how it looks), it does **not** belong here; route it through `data/**` + catalogs + API.

## 📦 Data and Metadata

### Inputs

| Input | Format | Where from | Validation |
|---|---|---|---|
| UI asset files | SVG/PNG/JPG/glTF/JSON/etc. | Repo | Review + size checks + secret scan (if implemented) |
| Third-party attribution | Markdown/JSON | Repo | Review + license check |
| Data-backed layer references | URLs + IDs | API payload | Contract tests + runtime guards |

### Outputs

| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Shipped static assets | Bundled/static served files | Build output | Build-system rules (not confirmed in repo) |
| Attribution surfacing | UI help/about panel content | UI | UI contract (not confirmed in repo) |

### Recommended metadata (not confirmed in repo)

To keep compliance auditable, it is recommended to include one or both:
- `NOTICE.md` listing third-party assets and required attribution
- `assets.manifest.json` with per-asset metadata

Reference-only manifest shape:

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
      "reviewed_by": "TBD",
      "notes": "UI-only asset"
    }
  ]
}
~~~

### Sensitivity and redaction
- Do not store precise site coordinates, detailed boundary polygons, or sensitive overlays as static assets.
- Avoid embedded metadata that could leak sensitive context (e.g., EXIF/GPS) unless explicitly sanitized (sanitization mechanism not confirmed in repo).

### Quality signals
- Deterministic references: stable filenames and stable import paths
- Assets are optimized for web delivery (reasonable file sizes)
- License/attribution coverage for any third-party items

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

### Secrets and tokens (non-negotiable)
- Do not commit Cesium Ion tokens, API keys, OAuth client secrets, or private endpoints.
- If Cesium Ion is used (not confirmed in repo), tokens must be injected via approved secret management at build/deploy time.

### Performance notes
- Keep textures and images small; prefer vector icons where possible.
- Treat `models/` as demo-only unless explicitly governed.
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
- [ ] Large binaries are reviewed (and avoided unless explicitly governed)

### Reproduction (placeholders)
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
| v0.1.1 | 2025-12-24 | Clarified allowed vs disallowed asset classes; added secret/token and evidence-vs-presentation rules; strengthened validation gates | TBD |

---
Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`