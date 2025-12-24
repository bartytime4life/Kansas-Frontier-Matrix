---
title: "`web/cesium/assets/images/` — Cesium UI image assets"
path: "web/cesium/assets/images/README.md"
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

doc_uuid: "urn:kfm:doc:web:cesium:assets:images:readme:v1.0.0"
semantic_document_id: "kfm-web-cesium-assets-images-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:web:cesium:assets:images:readme:v1.0.0"
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

# `web/cesium/assets/images/` — Cesium UI image assets

## 📘 Overview

### Purpose

This directory holds **static image assets** used by the Cesium-based frontend UI—icons, marker imagery, legends, and other UI visuals that are bundled with the web app.

This folder is intentionally **UI-scoped**:
- assets here should support presentation (icons, logos, UI illustrations),
- not act as a home for “real” datasets or derived pipeline outputs.

### Scope

| In Scope | Out of Scope |
|---|---|
| Small UI images (SVG/PNG/WebP) used by Cesium/React UI | Large geospatial datasets (those belong in `data/**` and are served via catalogs/APIs) |
| Marker artwork used for point features (e.g., billboard sprites) | Any assets containing secrets, PII, or restricted location disclosures |
| Visual assets with clear licensing/permission | Third-party images without a verifiable license/permission trail |
| Branding assets that follow the logo rules (see `logos/README.md`) | “Scraped from the web” imagery without explicit reuse rights |

### Audience

- Primary: UI engineers working in `web/` (Cesium + map UI)
- Secondary: reviewers responsible for governance, licensing, and sensitivity controls

### Definitions

- Glossary: `docs/glossary.md` *(not confirmed in repo — update if the glossary lives elsewhere)*
- **Marker / billboard (Cesium):** an image rendered at a point location (commonly used for POIs)
- **UI asset:** a static file shipped with the frontend build (not fetched from KFM APIs at runtime)

### Key artifacts (what this folder should link to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Logos folder contract | `web/cesium/assets/images/logos/README.md` | UI maintainers | Logo usage + licensing rules |
| UI root | `web/` | UI maintainers | Frontend code + asset bundling |
| Master Guide | `docs/MASTER_GUIDE_v12.md` | KFM Core Team | Canonical pipeline + invariants |

### Definition of done (for changes in this directory)

- [ ] New assets are **small + optimized** (no accidental multi-MB additions).
- [ ] Names are **kebab-case** and describe purpose (no spaces; no “final2.png”).
- [ ] Any third-party asset has documented **license/permission** (in PR description or adjacent docs).
- [ ] UI code references assets via stable paths/imports (no broken links).
- [ ] No content here reveals restricted or sensitive locations.

## 🗂️ Directory Layout

### This document

- `path`: `web/cesium/assets/images/README.md` (must match front-matter)

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| Frontend UI | `web/` | React + map clients, layer registry, UI assets |
| Documentation | `docs/` | Canonical governed docs, standards, templates |
| Data outputs | `data/` | Raw/work/processed + STAC/DCAT/PROV + provenance |
| Schemas | `schemas/` | JSON schemas and validation contracts |

### Expected file tree for this sub-area

~~~text
📁 web/
└── 📁 cesium/
    └── 📁 assets/
        └── 📁 images/
            ├── 📄 README.md
            └── 📁 logos/
                └── 📄 README.md
~~~

## 🧭 Context

### How this fits the canonical pipeline

KFM’s canonical flow is:

**ETL → STAC/DCAT/PROV → Graph → API → UI → Story Nodes → Focus Mode**

This folder sits entirely in the **UI** stage. It must not be used to bypass the API boundary:
- the UI should not read the graph directly,
- location-bearing data should be delivered via contracted APIs and governed datasets,
- static images here are presentation-only.

### When to add an image here

- Marker art for Cesium billboards (e.g., generic pin icons)
- UI legend images (when SVG/HTML alternatives aren’t viable)
- Small UI illustrations that ship with the app
- Approved logos (see `logos/README.md`)

### When NOT to add an image here

- Raster datasets, scans, basemap tiles, or any data that should be cataloged (STAC/DCAT/PROV)
- Screenshots/photos that include sensitive or restricted locations
- Third-party images without explicit permission

## 🧪 Validation & CI/CD

### Validation steps

- [ ] **File size sanity check:** keep assets small; use compression/optimization.
- [ ] **Format sanity check:** prefer SVG for icons/logos; use PNG/WebP for raster.
- [ ] **Licensing sanity check:** ensure the license/permission trail is documented.
- [ ] **A11y check:** ensure the UI provides meaningful alternative text where appropriate.
- [ ] **Secret/PII check:** confirm no sensitive text or embedded metadata was added.

### Reproduction

> Commands below are examples only (actual commands are **not confirmed in repo**). Replace with repo-specific scripts.

~~~bash
# (not confirmed in repo) example ideas:
# 1) run frontend tests / build
# npm test
# npm run build
#
# 2) run repo markdown protocol checks
# python -m tools.lint_markdown_protocol
~~~

## ⚖ FAIR+CARE & Governance

### Review gates

Governance review is recommended/required when changes introduce:
- third-party branding/logos,
- imagery derived from restricted sources,
- assets that could reveal sensitive locations (even indirectly).

### CARE / sovereignty considerations

- Treat UI-shipped assets as effectively **public**.
- Do not commit imagery that exposes restricted locations, culturally sensitive sites, or protected personal data.
- Prefer abstraction (icons, generalized diagrams) over photos or exact map screenshots.

### AI usage constraints

- This document permits structural extraction, summarization, translation, and keyword indexing.
- Prohibited: generating new policy text or inferring sensitive locations.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-24 | Initial README for Cesium UI image assets directory | TBD |

---

Footer refs:

- Master guide: `docs/MASTER_GUIDE_v12.md`
- Template: `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
- Ethics: `docs/governance/ETHICS.md`
