---
title: "GitHub App Assets — Attribution Register"
path: ".github/apps/<app_slug>/assets/attribution.md"
version: "v1.0.0"
last_updated: "2025-12-29"
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

doc_uuid: "urn:kfm:doc:github:app-assets-attribution:<app_slug>:v1.0.0"
semantic_document_id: "kfm-github-app-assets-attribution-<app_slug>-v1.0.0"
event_source_id: "ledger:kfm:doc:github:app-assets-attribution:<app_slug>:v1.0.0"
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

# GitHub App Assets — Attribution Register

## 📘 Overview

### Purpose

- Provide a single, repo-versioned **attribution register** for all non-text assets stored in `.github/apps/<app_slug>/assets/`.
- Ensure assets are **public-safe** and have traceable provenance (source + license) before they are referenced by:
  - `.github/apps/<app_slug>/README.md`
  - `.github/apps/<app_slug>/assets/README.md`
  - `.github/apps/README.md`
- Reduce review friction by standardizing the minimum attribution fields required for each asset.

### Scope

| In Scope | Out of Scope |
|---|---|
| Images (PNG/JPG/SVG/WebP), diagrams (exported images), screenshots, PDFs, icons, other binary assets in this folder | GitHub App manifests, permissions docs, workflow docs, code, secrets/credentials, third-party libraries |

### Audience

- Primary: GitHub App owners, repo maintainers, contributors adding documentation assets
- Secondary: security reviewers, governance reviewers, CI/CD owners

### Definitions

- Glossary link: `docs/glossary.md` *(expected canonical location; if missing, mark “not confirmed in repo” and point to the correct glossary path)*
- Terms used in this doc:
  - **Asset**: a file in `assets/` that is used for documentation (image/diagram/etc.).
  - **Attribution**: the minimum provenance + license record required to reuse an asset.
  - **Source**: origin of the asset (URL, publication, repo path, internal authoring tool output).
  - **Derived asset**: asset created by modifying or exporting from another source (must record modifications).
  - **Public-safe**: does not disclose secrets, tokens, private infrastructure details, or sensitive locations.

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| This attribution register | `.github/apps/<app_slug>/assets/attribution.md` | App owner | Required for asset provenance + licensing |
| Assets folder README | `.github/apps/<app_slug>/assets/README.md` | App owner | Explains what assets exist + how they are used |
| App documentation | `.github/apps/<app_slug>/README.md` | App owner | References assets and explains intended usage |
| GitHub Apps hub README | `.github/apps/README.md` | Repo maintainers | Cross-app governance + folder contract |
| Master Guide | `docs/MASTER_GUIDE_v12.md` | KFM maintainers | Canonical invariants + subsystem homes |

### Definition of done (for this document)

- [ ] Front-matter complete + valid (path/version/last_updated)
- [ ] Every non-markdown file in `assets/` has an entry in the register
- [ ] Each entry contains **source + license + author/owner + modifications**
- [ ] Public-safe check completed (no secrets, no sensitive locations, no private URLs in screenshots)
- [ ] If license/provenance is unclear, entry is flagged and the asset is **not used** until resolved
- [ ] Validation steps below are repeatable
- [ ] Governance + CARE/sovereignty considerations explicitly stated

## 🗂️ Directory Layout

### This document

- `path`: `.github/apps/<app_slug>/assets/attribution.md` *(must match front-matter)*

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| CI | `.github/` | Workflows + policy gates |
| GitHub Apps docs | `.github/apps/` | App manifests + permission/runbook docs (secret-free) |
| This app | `.github/apps/<app_slug>/` | App-specific documentation + manifest (secret-free) |
| This app assets | `.github/apps/<app_slug>/assets/` | Diagrams/images used by app docs |
| Documentation | `docs/` | Canonical governed docs (architecture, standards, runbooks) |
| Schemas | `schemas/` *(if present)* | JSON Schemas (STAC/DCAT/PROV/story/ui/telemetry) |

### Expected file tree for this sub-area

~~~text
📁 .github/
└── 📁 apps/
    └── 📁 <app_slug>/
        └── 📁 assets/
            ├── 📄 README.md
            ├── 📄 attribution.md
            ├── 📄 <diagram_or_image>.<ext>
            └── 📁 <optional_subdir>/
                └── 📄 <asset_file>.<ext>
~~~

## 🧭 Context

### Background

- KFM repositories may be public; anything committed in `.github/apps/**` must be safe to disclose.
- Documentation assets can introduce **license obligations** or **sensitive leakage** if added without provenance review.
- This register makes asset provenance **diffable** and **reviewable** in the same PR that introduces the asset.

### Assumptions

- Assets stored here are intended for documentation use only (not runtime dependencies).
- Asset additions will be accompanied by register updates in the same PR.
- If an asset is derived from a dataset or external publication, the contributor can provide a stable reference.

### Constraints / invariants

- Never store secrets, tokens, or private keys in this folder.
- Do not infer, reveal, or embed sensitive locations in assets (including screenshots/maps).
- If an asset is reused in narratives (Story Nodes / Focus Mode), it must remain provenance-linked and public-safe.
- Canonical pipeline ordering remains preserved; assets must not “shortcut” contractual boundaries by embedding restricted data that bypasses API redaction.

### Open questions

| Question | Owner | Target date |
|---|---|---|
| Do we allow third-party logos or UI screenshots under this app’s assets folder? | TBD | TBD |
| Are any assets generated from governed datasets (STAC/DCAT/PROV) and therefore require dataset IDs in the register? | TBD | TBD |
| Should CI enforce a “no-unattributed-assets” gate for `.github/apps/**/assets/**`? | TBD | TBD |

### Future extensions

- Add a CI check that:
  - enumerates files in `assets/` and verifies each is present in the table below,
  - blocks merge when a non-markdown asset is missing attribution.
- Add a lightweight license scanner and link checker for source references.
- Add a “generated-from” convention for exported mermaid diagrams (see Register fields).

## 🗺️ Diagrams

### Asset intake + attribution flow

~~~mermaid
flowchart LR
  A[Add asset file to assets/] --> B[Record attribution in attribution.md]
  B --> C[Public-safe check: no secrets/sensitive locations]
  C --> D[Review: maintainers + security/governance if needed]
  D --> E[Merge + asset can be referenced by app docs]
~~~

## 📦 Data & Metadata

### Attribution record schema (minimum required fields)

For each asset file (excluding `README.md` and `attribution.md`), record:

- **Asset file**: relative path from repo root
- **Type**: png/jpg/svg/pdf/etc.
- **Description / Usage**: what the asset represents and where it is referenced
- **Source / Origin**: URL / publication / internal authoring note
- **License**: name and/or SPDX identifier (if known)
- **Author / Rights holder**: person/org (or “KFM contributors” for original work)
- **Modifications**: “none” or description of edits (crop, annotate, recolor, redact)
- **Added in PR/commit**: PR number or commit SHA (when known)
- **Notes**: any caveats, required credit line text, restrictions, or review flags

### Register

> Fill one row per asset file in this folder (excluding markdown docs).

| Asset file | Type | Description / usage | Source / origin | License | Author / rights holder | Modifications | Added in PR/commit | Notes |
|---|---|---|---|---|---|---|---|---|
| `.github/apps/<app_slug>/assets/<asset_file>.<ext>` | `<ext>` | TBD | TBD | TBD | TBD | none / TBD | TBD | TBD |

### Sensitivity & redaction

- If an asset includes:
  - screenshots of workflow logs,
  - screenshots of settings pages,
  - maps/locations,
  - or any data excerpt,
  ensure the asset contains **no secret values** and does **not** reveal sensitive locations.
- If redaction/generalization is required, record the method in **Modifications** (e.g., “blurred secret names”, “removed coordinates”, “cropped private URLs”).

### Quality signals

- Asset list matches folder contents.
- License/provenance is explicit for every third-party asset.
- “Generated” assets include the generator source (e.g., mermaid source path) where applicable.
- No sensitive leakage is present (secrets, PII, restricted location detail).

## 🌐 STAC, DCAT & PROV Alignment

This document does not directly produce STAC/DCAT/PROV outputs.

If an asset is derived from a governed dataset or evidence artifact, add the relevant pointers in the **Notes** column (examples):

- `dataset_id: <kfm_dataset_id>`
- `stac_item_id: <stac_item_id>`
- `prov_bundle: data/prov/<bundle_id>.jsonld` *(or equivalent)*

## 🧱 Architecture

### Components (high level)

| Component | Responsibility | Notes |
|---|---|---|
| `assets/` folder | Stores documentation assets | Must remain secret-free and public-safe |
| `attribution.md` | Source + license register | Reviewable, diffable provenance |
| CI policy gates | Prevent secret leakage; enforce standards | Secret scan and doc checks are expected |

### Interfaces / contracts

- Folder contract:
  - Assets must be referenced by relative path from app docs.
  - Assets must have an attribution row in this file.
- Governance contract:
  - If an asset’s provenance is unclear, treat it as **blocked** until resolved (review required).

## 🧠 Story Node & Focus Mode Integration

This is an operational documentation folder; it is not a Story Node.

However, if any asset from this folder is reused in:
- `docs/reports/story_nodes/**`
- Focus Mode context bundles
- UI documentation tied to datasets

…then that reuse must continue to respect provenance-linked narrative rules (no unsourced claims; no sensitive location inference).

## 🧪 Validation & CI/CD

### Validation steps

- [ ] Confirm every non-markdown asset in this folder has an entry in the Register table
- [ ] Confirm source/license fields are complete for third-party assets
- [ ] Confirm modifications/redaction are described when performed
- [ ] Run repo secret scan / leakage checks (no tokens/keys in screenshots or files)
- [ ] Run markdown lint / link checks (where the repo provides them)

### Reproduction (high level)

If an asset is generated (exported from another source), record the generator input in **Source / origin** or **Notes**.

Examples:
- “Exported from `docs/diagrams/<name>.mmd`”
- “Rendered from mermaid block in `.github/apps/<app_slug>/README.md`”
- “Derived from `<dataset_id>` with visualization tool `<tool_name>` (settings recorded in Notes)”

### Telemetry signals (optional; if telemetry subsystem exists)

| Signal | Source | Where recorded |
|---|---|---|
| `asset_added` | PR | `docs/telemetry/` *(if present)* |
| `license_review_required` | PR review label | `docs/telemetry/` *(if present)* |
| `promotion_blocked` | CI gate | CI logs / telemetry (if present) |

## ⚖ FAIR+CARE & Governance

### Review gates

- Third-party assets require a provenance + license review before reuse.
- If an asset intersects sovereignty obligations or risks sensitive disclosure, elevate to governance review per the referenced governance docs.

### CARE / sovereignty considerations

- Treat culturally sensitive imagery or location-revealing maps as high-risk by default.
- Apply redaction/generalization as needed and record the method in this register.

### AI usage constraints

- Do not use AI tooling to infer sensitive locations from assets.
- Do not add “policy text” here; this file is an attribution register and pointer list.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-29 | Initial attribution register template for app assets | TBD |
