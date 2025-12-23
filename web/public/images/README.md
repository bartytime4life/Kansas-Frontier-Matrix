---
title: "KFM Web UI — Public Images (web/public/images)"
path: "web/public/images/README.md"
version: "v1.0.0"
last_updated: "2025-12-23"
status: "draft"
doc_kind: "Guide"
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

doc_uuid: "urn:kfm:doc:web:public-images-readme:v1.0.0"
semantic_document_id: "kfm-web-public-images-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:web:public-images-readme:v1.0.0"
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

# KFM Web UI — Public Images (`web/public/images`)

## 📘 Overview

### Purpose

- Define what belongs in `web/public/images/` and how these assets are referenced by the KFM UI.
- Prevent mixing **UI chrome assets** (logos, icons, illustrations) with **evidence/data images** (historic photos, scanned maps, dataset outputs), which should remain governed by the catalog + provenance pipeline.

### Scope

| In Scope | Out of Scope |
|---|---|
| UI visuals: logos, icons, UI illustrations, decorative/brand images used by the frontend | Evidence imagery (historic photos, scanned maps), dataset-derived rasters/tiles, sensitive imagery requiring redaction rules |
| Lightweight static files served with the web app | Any asset that must be tracked as a STAC/DCAT/PROV evidence product |

### Audience

- Primary: UI developers maintaining `web/`
- Secondary: Designers, reviewers, and maintainers who curate the look/feel of KFM

### Definitions (link to glossary)

- Link: `docs/glossary.md`
- Terms used in this doc:
  - **Public UI image asset:** A static image bundled/served with the frontend (icons/logos/UI illustrations).
  - **Evidence image:** A historical or dataset-derived image that must be provenance-linked and cataloged (STAC/DCAT/PROV) before being surfaced in the UI.
  - **Sidecar metadata (optional):** A small file describing source/license/notes for an image (convention not confirmed in repo).

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| This README | `web/public/images/README.md` | UI maintainers | Conventions + boundary rules |
| Public UI images | `web/public/images/` | UI maintainers | Icons/logos/etc. used by the web app |
| Evidence images (canonical home) | `data/<domain>/processed/` + catalogs | Data + catalog maintainers | Must be provenance-linked and cataloged (do not place in `web/public/images/`) |

### Definition of done (for this document)

- [ ] Front-matter complete + valid
- [ ] The boundary between UI images vs. evidence images is explicit
- [ ] File tree is accurate for this sub-area
- [ ] Validation steps listed and repeatable
- [ ] Governance + CARE/sovereignty considerations explicitly stated (even if “none”)

## 🗂️ Directory Layout

### This document

- `path`: `web/public/images/README.md` (must match front-matter)

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| Data domains | `data/` | Raw/work/processed + catalog outputs |
| Documentation | `docs/` | Canonical governed docs |
| Graph | `src/graph/` | Graph build + ontology bindings |
| Pipelines | `src/pipelines/` | ETL + catalogs + transforms |
| Schemas | `schemas/` | JSON schemas + telemetry schemas |
| Frontend | `web/` | React + map clients |
| Public UI assets | `web/public/` | Static assets served by the frontend |
| MCP | `mcp/` | Experiments, model cards, SOPs |

### Expected file tree for this sub-area

~~~text
📁 web/
└── 📁 public/
    └── 📁 images/
        └── 📄 README.md
~~~

## 🧭 Context

### Background

- The UI needs a simple, cache-friendly place for **static** images that ship with the frontend.
- KFM’s evidence-first architecture requires that **historical or dataset-derived imagery** remain provenance-linked and discoverable via catalogs and APIs (rather than being silently embedded as UI assets).

### Assumptions

- The `web/` build and deploy process serves files under `web/public/` as static assets (verify with the project’s actual web build configuration).
- The frontend references these assets via stable, public paths (for example, `/images/<file>`), subject to the build tool’s conventions.

### Constraints / invariants

- The canonical pipeline ordering is preserved: ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode.
- The UI does not connect to Neo4j directly; it consumes content through the API boundary.
- Do **not** place dataset-derived imagery or evidence images in `web/public/images/`. If it’s evidence, it belongs in `data/<domain>/processed/` and must be cataloged and provenance-linked.

### Open questions

| Question | Owner | Target date |
|---|---|---|
| Do we enforce image size budgets (KB/MB caps) in CI for `web/public/images/`? | UI maintainers | TBD |
| Do we require sidecar metadata for every non-trivial image (source/license/notes)? | Governance + UI | TBD |
| Do we standardize subfolders (e.g., `icons/`, `logos/`) or keep flat? | UI maintainers | TBD |

### Future extensions

- Add an image lint step (naming, file size, basic format checks).
- Add an optional image optimization workflow (build-time compression).
- Add an optional metadata sidecar convention (source/license/provenance pointers).

## 🗺️ Diagrams

### System / dataflow diagram

~~~mermaid
flowchart LR
  A[ETL] --> B[STAC/DCAT/PROV Catalogs]
  B --> C[Neo4j Graph]
  C --> D[APIs]
  D --> E[React/Map UI<br/>+ static assets under web/public/images]
  E --> F[Story Nodes]
  F --> G[Focus Mode]
~~~

### Optional: sequence diagram

~~~mermaid
sequenceDiagram
  participant Browser
  participant UI as Web UI (web/)
  participant API as API boundary (src/server)
  participant Assets as Static assets (web/public/images)

  Browser->>UI: Load app shell
  Browser->>Assets: GET /images/<asset>
  Assets-->>Browser: 200 image bytes

  Browser->>API: GET /api/<contracted-endpoint>
  API-->>Browser: Contracted payload + provenance refs
~~~

## 📦 Data & Metadata

### Inputs

- Image files committed under `web/public/images/` intended for UI use.
- (Recommended) A note of the image’s source and license when not originally created for KFM (process not confirmed in repo).

Recommended conventions (not confirmed in repo):
- Naming: `kebab-case` (e.g., `kfm-logo.svg`, `icon-search.svg`)
- Prefer SVG for icons/logos; use PNG/JPG only when raster is required.
- Avoid embedding sensitive locations or personally identifying information in UI images.

### Outputs

- Static, public assets that the frontend can reference at runtime.

### Sensitivity & redaction

- This directory is **public** (`sensitivity: public`). Do not store:
  - sensitive imagery requiring redaction/generalization
  - content restricted by sovereignty/community rules
- If an image must be shown but requires redaction/generalization, it should be managed as a governed evidence asset surfaced via the API boundary (not placed here).

### Quality signals

- File sizes are reasonable for web delivery (optimize when possible).
- Images render crisply at expected UI sizes (icons vs. high-res).
- Changes are intentional and reviewed (especially for branding).

## 🌐 STAC, DCAT & PROV Alignment

### STAC

- UI assets in `web/public/images/` are **not** STAC Items.
- If an image is an evidence artifact (historic photo, scanned map, dataset output), it should be handled as a data product:
  - stored under `data/<domain>/processed/`
  - cataloged under `data/stac/`
  - referenced by the UI through API/cat endpoints

### DCAT

- UI assets are not DCAT datasets.
- DCAT applies to published datasets/evidence products, not UI chrome.

### PROV-O

- UI assets typically do not require PROV activity bundles.
- Evidence imagery displayed by the UI must be provenance-linked (PROV) through the API boundary.

### Versioning

- Image changes are versioned through the repository history (Git).
- If a major branding change occurs, consider documenting it in a design or release note (location not confirmed in repo).

## 🧱 Architecture

### Components

- `web/public/images/` — static public image assets
- `web/` — UI application (React + map client)
- Deploy target (static hosting/CDN) — serves `/images/...` to browsers (implementation not confirmed in repo)

### Interfaces / contracts

- The UI references these assets as static files (for example, `/images/<file>`), subject to the web build conventions.
- No API contract is required to fetch these images; they are static assets.

### Extension points checklist (for future work)

- [ ] Add CI checks for file size limits and forbidden formats
- [ ] Add a standard subfolder layout (icons/logos/illustrations) if needed
- [ ] Add a metadata sidecar convention (source/license/notes)
- [ ] Add an image optimization step to the web build pipeline

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode

- These assets may be used for UI chrome (buttons, branding, decorative visuals).
- Story Node evidence images should not be stored here; Focus Mode should surface evidence images via provenance-linked APIs/catalogs.

### Provenance-linked narrative rule

- If an image is presented as historical evidence in a narrative context, it must remain provenance-linked and traceable to catalog/provenance identifiers (not embedded as an untracked UI asset).

### Optional structured controls

~~~yaml
# Not typically applicable for UI image assets.
# If you introduce Focus Mode behavior tied to UI assets, document it here.
focus_layers:
  - "TBD"
focus_time: "TBD"
focus_center: [ -98.0000, 38.0000 ]
~~~

## 🧪 Validation & CI/CD

### Validation steps

- [ ] Markdown protocol checks (front-matter present, path matches)
- [ ] No evidence/data imagery incorrectly stored under `web/public/images/`
- [ ] Basic sanity checks for image assets (file names, sizes) (implementation not confirmed in repo)
- [ ] Security and sovereignty checks (as applicable)

### Reproduction

~~~bash
# Example placeholders — replace with repo-specific commands
# 1) run doc lint
# 2) run web build
# 3) (optional) run image lint / size checks
~~~

### Telemetry signals (if applicable)

| Signal | Source | Where recorded |
|---|---|---|
| TBD | TBD | `docs/telemetry/` + `schemas/telemetry/` |

## ⚖ FAIR+CARE & Governance

### Review gates

- UI maintainer review: yes
- Governance review: only if imagery includes external sources, sensitive cultural content, or policy-relevant branding

### CARE / sovereignty considerations

- Avoid using imagery that conflicts with sovereignty/community rules.
- If culturally sensitive imagery is required, follow the governance and sovereignty docs and consider redaction/generalization pathways.

### AI usage constraints

- Ensure this doc’s AI permissions/prohibitions match intended use.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-23 | Initial README for `web/public/images/` | TBD |

---

Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`