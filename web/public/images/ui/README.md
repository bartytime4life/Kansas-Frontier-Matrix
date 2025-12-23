---
title: "KFM Web UI Image Assets — README"
path: "web/public/images/ui/README.md"
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

doc_uuid: "urn:kfm:doc:web:public-images-ui-readme:v1.0.0"
semantic_document_id: "kfm-web-public-images-ui-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:web:public-images-ui-readme:v1.0.0"
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

# KFM Web UI image assets

## 📘 Overview

### Purpose

This directory stores **UI-only image assets** (icons, logos, UI illustrations, map UI markers, etc.) that are served as static files by the web frontend.

It is intentionally **not** a home for dataset imagery or evidence artifacts; those belong in KFM’s governed data pipeline (STAC/DCAT/PROV + provenance).

### Scope

| In Scope | Out of Scope |
|---|---|
| UI icons (SVG/PNG), UI illustrations, UI brand marks/logos used in navigation and chrome | Dataset/evidence images (historic maps, scans, photos), model outputs, charts used as evidence, sensitive imagery requiring restricted handling |
| Small map UI markers used for the interface (not the data) | Any image that “asserts a fact” in a Story Node without provenance (store as governed data asset instead) |
| Static assets that are safe to be publicly served | Anything requiring redaction/generalization rules (handle via governed data + UI redaction logic) |

### Audience

- Primary: UI/frontend contributors maintaining the web app assets.
- Secondary: Designers, Story Node authors, reviewers checking provenance/attribution.

### Definitions (link to glossary)

- Link: `docs/glossary.md`
- Terms used in this doc:
  - **UI asset:** An image used for interface presentation (controls, decoration, navigation).
  - **Evidence asset:** An image that supports a factual claim (requires provenance).
  - **Attribution record:** The source + license notes required for third-party assets.

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master Guide | `docs/MASTER_GUIDE_v12.md` | Project maintainers | Canonical pipeline + invariants |
| Universal doc template | `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` | Docs maintainers | Governance format used here |
| UI layer registry | `web/cesium/layers/regions.json` | UI maintainers | Not confirmed in repo; referenced as a typical KFM UI contract artifact |

### Definition of done (for this document)

- [ ] Front-matter complete + valid
- [ ] Folder purpose is clear: “UI assets only”
- [ ] Attribution/licensing guidance included
- [ ] Sensitivity + sovereignty cautions stated (public directory implies public exposure)
- [ ] Validation steps listed and repeatable

## 🗂️ Directory Layout

### This document

- `path`: `web/public/images/ui/README.md` (must match front-matter)

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| Web frontend | `web/` | UI source + static assets |
| Static public assets | `web/public/` | Publicly served files (this directory is under here) |
| UI images (this folder) | `web/public/images/ui/` | Icons/logos/illustrations used by UI |
| Data domains | `data/` | Raw/work/processed datasets (not UI assets) |
| STAC catalogs | `data/stac/` | STAC Collections/Items for governed assets |
| Documentation | `docs/` | Governed docs (master guide, architecture, standards) |
| Schemas | `schemas/` | JSON schemas for contracts (if applicable) |

### Recommended sub-structure (create as needed)

The subfolders below are **recommendations** (not confirmed in repo). Use them if/when the asset set grows.

~~~text
📁 web/
├── 📁 public/
│   └── 📁 images/
│       └── 📁 ui/
│           ├── 📄 README.md
│           ├── 📁 icons/               # UI control icons (prefer SVG)
│           ├── 📁 logos/               # Project/partner marks (ensure license)
│           ├── 📁 markers/             # UI-only map markers (avoid “data assertions”)
│           ├── 📁 illustrations/       # Onboarding/help/empty-state art
│           └── 📁 sprites/             # Sprite sheets + manifests (if used)
~~~

## 🧭 Context

### Background

KFM’s architecture distinguishes between:
- **UI presentation assets** (this folder), and
- **governed evidence/data assets** (tracked via STAC/DCAT/PROV + provenance and surfaced through APIs/Story Nodes).

This separation reduces the risk of “silent evidence” being shipped in a static folder with no provenance or sensitivity controls.

### Assumptions

- `web/public/` is treated as a static public root by the web stack (not confirmed in repo).
- Anything placed here should be assumed **publicly accessible** once deployed.

### Constraints / invariants

- **No hidden data leakage:** do not embed sensitive locations, unredacted maps, or restricted imagery into a static/public folder.
- **Evidence must be governed:** if an image is used to support a factual claim, it should be stored and referenced as a governed asset (STAC/DCAT/PROV + provenance), not as a UI-only static file.

### Open questions (not confirmed in repo)

- Do we want a required `ATTRIBUTION.md` in this directory (or per subfolder)?
- Do we have (or want) automated CI checks for:
  - max file size
  - required attribution metadata for third-party assets
  - SVG sanitization and optimization

### Future extensions

- Add a lightweight asset manifest (e.g., `manifest.json`) for cache busting and automated inventory (not confirmed in repo).
- Add CI policy to ensure third-party assets always ship with attribution/license notes.

## 🗺️ Diagrams

~~~mermaid
sequenceDiagram
  participant Dev as Dev/Designer
  participant Repo as Repo (web/public/images/ui)
  participant Web as Web server/build
  participant Browser as Browser

  Dev->>Repo: Add/update UI image (+ attribution notes)
  Browser->>Web: GET /images/ui/<asset>
  Web-->>Browser: 200 (static asset bytes)
~~~

## 📦 Data & Metadata

### Inputs

| Input | Format | Where from | Validation |
|---|---|---|---|
| UI asset file | `.svg`, `.png`, `.webp` (as appropriate) | Designed internally or sourced with license | Manual review: naming + size + safety |
| Attribution info | Text in PR/notes (or an attribution file) | Required for third-party assets | Review gate: license compatibility |

### Outputs

| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Public UI images | Static files | `web/public/images/ui/**` | Folder contract defined by this README |
| Optional asset inventory | JSON (optional) | `web/public/images/ui/manifest.json` | Not confirmed in repo |

### Sensitivity & redaction

- Treat this directory as **public**:
  - Do **not** place restricted or culturally sensitive imagery here.
  - Do **not** place screenshots/maps that reveal precise sensitive locations here.
- If an image requires generalization/redaction, handle it via governed data + UI redaction logic (not via a raw static file).

### Quality signals

- Prefer **SVG** for simple icons (scales cleanly).
- Keep bitmaps as small as possible (dimensions + compression) without harming readability.
- Avoid embedding external references inside SVG (scripts, remote links).
- Naming: use lowercase + hyphens, no spaces (example: `zoom-in.svg`, `kfm-logo-mark.svg`).

## 🌐 STAC, DCAT & PROV Alignment

### STAC

- UI-only assets in this folder typically do **not** belong in STAC.
- If an image is a **data/evidence artifact** (historic map, scanned document, aerial image, model output), store it under the governed data structure and reference it from a STAC Item.

### DCAT

- Not applicable for UI-only images.
- If the asset is part of a published dataset, ensure DCAT mapping exists alongside that dataset’s docs.

### PROV-O

- Not applicable for UI-only images.
- If an image is generated by a pipeline/model and used as evidence, it should have a PROV activity/run identity in the governed data pipeline.

### Versioning

- UI assets can be versioned via normal git history.
- Evidence assets should use the governed STAC/DCAT/PROV versioning approach (predecessor/successor links, provenance identities).

## 🧱 Architecture

### Components

| Component | Responsibility | Interface |
|---|---|---|
| ETL | Ingest + normalize data | Config + run logs |
| Catalogs | STAC/DCAT/PROV | JSON + validator |
| Graph | Neo4j | Cypher + API layer |
| APIs | Serve contracts | REST/GraphQL |
| UI | Map + narrative | API calls + static assets |
| Story Nodes | Curated narrative | Graph + docs |
| Focus Mode | Contextual synthesis | Provenance-linked |

### Interfaces / contracts

| Contract | Location | Versioning rule |
|---|---|---|
| UI asset path convention | `web/public/images/ui/**` | Changes are breaking only if referenced paths change |
| UI layer registry | `web/cesium/layers/regions.json` | Not confirmed in repo; schema-validated when present |
| Attribution practice | This README (+ any added attribution files) | Must remain consistent and discoverable |

### Extension points checklist (for future work)

- [ ] Data: new domain added under `data/<domain>/...` (N/A for UI-only images)
- [ ] STAC: new collection + item schema validation (only if images are evidence assets)
- [ ] PROV: activity + agent identifiers recorded (only if images are generated evidence)
- [ ] Graph: new labels/relations mapped + migration plan (N/A for UI-only images)
- [ ] APIs: contract version bump + tests (N/A for UI-only images)
- [ ] UI: add images under this directory + update code references
- [ ] Focus Mode: provenance references enforced (only if images are used as evidence)
- [ ] Telemetry: new signals + schema version bump (optional; not confirmed in repo)

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode

- UI images here should be treated as **presentation-only**.
- If a Story Node needs to present an image as evidence (e.g., “this 1854 map shows…”), that image must be a **governed asset** with provenance (not stored here).

### Provenance-linked narrative rule

- Every claim must trace to a dataset / record / asset ID.
- UI-only images do not substitute for provenance.

### Optional structured controls

~~~yaml
focus_layers:
  - "TBD"
focus_time: "TBD"
focus_center: [ -98.0000, 38.0000 ]
~~~

## 🧪 Validation & CI/CD

### Validation steps

- [ ] Markdown protocol checks (if enforced for README-style docs)
- [ ] Asset naming conventions (lowercase + hyphens; no spaces)
- [ ] Attribution confirmed for third-party images (source + license)
- [ ] SVG safety review (no scripts/external references)
- [ ] UI build/test runs (repo-specific)

### Reproduction

~~~bash
# Example placeholders — replace with repo-specific commands

# 1) run doc lint (if any)
# 2) run UI tests
# 3) run UI build
~~~

### Telemetry signals (if applicable)

| Signal | Source | Where recorded |
|---|---|---|
| TBD (e.g., "UIImageLoadError") | Frontend UI event | `docs/telemetry/` + `schemas/telemetry/` (not confirmed in repo) |

## ⚖ FAIR+CARE & Governance

### Review gates

- Adding third-party logos/graphics: verify license + attribution requirements.
- Adding culturally sensitive imagery: requires review under sovereignty/ethics policies.
- Any asset that could reveal restricted locations must not be placed here.

### CARE / sovereignty considerations

- Treat this directory as “public distribution.”
- Avoid imagery that could harm communities or disclose protected information.
- If unsure: do not add here; route through governed data + redaction/generalization rules.

### AI usage constraints

- This doc allows summarization/translation/extraction but prohibits:
  - generating policy
  - inferring sensitive locations
- Do not use AI tooling to “reconstruct” or enhance imagery in ways that could reveal sensitive sites or imply provenance that does not exist.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-23 | Initial UI images README | TBD |

---

Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`