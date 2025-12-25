---
title: "KFM Cesium UI — Logos (Assets)"
path: "web/cesium/assets/images/logos/README.md"
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

doc_uuid: "urn:kfm:doc:web:cesium:logos:readme:v1.0.0"
semantic_document_id: "kfm-web-cesium-logos-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:web:cesium:logos:readme:v1.0.0"
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

# `web/cesium/assets/images/logos/` — Logos

> **Trademark & licensing notice:** This directory may include logos/marks that are trademarks of their respective owners. Do not add or redistribute third‑party marks unless the license/permission and attribution requirements are documented and satisfied.

## 📘 Overview

### Purpose

This directory contains logo assets used by the **Cesium-based UI surfaces** (e.g., app header branding, credits/attribution UI, and partner/source acknowledgements).  
This README defines the **minimum metadata, naming, and safety rules** for adding and using logo files.

### Scope

| In Scope | Out of Scope |
|---|---|
| Logo image assets (SVG/PNG/WebP), logo variants (dark/light), and the required attribution metadata recorded in this README | UI implementation details, API contracts, map layers, general branding policy outside this directory |

### Audience

- Primary: UI contributors working in `web/cesium/**` who add or reference logos.
- Secondary: reviewers verifying licensing/trademark and accessibility requirements.

### Definitions (link to glossary)

- Link: `docs/glossary.md` *(not confirmed in repo)*
- Terms used in this doc:
  - **Logo asset**: an image file representing an organization/project/partner mark.
  - **Variant**: a logo version for a different background (light/dark) or size.
  - **Attribution metadata**: the license/permission/source details required for lawful use.

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master Guide | `docs/MASTER_GUIDE_v12.md` | TBD | System + pipeline ordering/invariants |
| Universal Doc Template | `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` | TBD | Default governed doc structure |
| UI root | `web/` | TBD | Front-end code and assets live here |
| Cesium UI area | `web/cesium/` | TBD | Cesium client (this directory is a UI asset dependency) |

### Definition of done (for this document)

- [x] Front-matter complete and `path:` matches file location
- [x] Clear rules for licensing/trademark attribution + review triggers
- [x] Naming/format guidance is specific enough to avoid accidental misuse
- [ ] If logos already exist in this folder: metadata table below is filled for each file
- [ ] Validation steps are listed and repeatable (manual or CI)

## 🗂️ Directory Layout

### This document

- `path`: `web/cesium/assets/images/logos/README.md` (must match front-matter)

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| Frontend | `web/` | React + map clients (MapLibre/Cesium) |
| Cesium UI | `web/cesium/` | Cesium application code |
| Documentation | `docs/` | Governed system documentation and standards |
| Governance | `docs/governance/` | Policies: governance, ethics, sovereignty |
| Schemas | `schemas/` | JSON Schemas used by CI and contracts |
| API boundary | `src/server/` | Contracted access layer (UI should not call Neo4j directly) |

### Expected file tree for this sub-area

~~~text
📁 web/cesium/assets/images/logos/
├── 📄 README.md
├── 🖼️ <logo-name>.svg
├── 🖼️ <logo-name>.png
├── 🖼️ <logo-name>@2x.png
└── 📄 <logo-name>.NOTICE.txt   (optional; use when upstream requires explicit notice text)
~~~

## 🧭 Context

### Background

Logos in the UI are a common source of accidental non-compliance (missing attribution, incorrect mark usage, or unclear permissions). This directory README standardizes how we store and document logo assets so the UI remains shippable and auditable.

### Assumptions

- The build system bundles `web/**` static assets into the UI artifact.
- Logos may appear in:
  - header/branding,
  - “about” screens,
  - Cesium credit/attribution panels,
  - partner acknowledgements.

### Constraints / invariants

- Treat any third‑party logo addition as a **governance-sensitive change** until licensing/permission is recorded.
- Frontend consumes data via APIs (no direct graph access). (This README is UI-only; no data access rules are implemented here.)

### Open questions

| Question | Owner | Target date |
|---|---|---|
| Is there a canonical repo-wide location for third-party notices (e.g., `NOTICE.md` or `/licenses/`)? | TBD | TBD |
| Do we want an automated “asset metadata lint” (checks table rows exist for each file)? | TBD | TBD |

### Future extensions

- Add an optional `logos.manifest.json` (or similar) that mirrors the table below for machine validation. *(Not added here; would require schema + tooling decisions.)*

## 🗺️ Diagrams

### Where logo assets sit in the UI build

~~~mermaid
flowchart LR
  A[web/cesium UI code] --> B[assets/images/logos]
  B --> C[Bundled UI artifact]
  C --> D[Rendered UI (branding + credits)]
~~~

## 🧠 Story Node & Focus Mode Integration

- Logos are **UI assets**, not evidence. They must not be presented as “sources.”
- If a logo is displayed alongside provenance-linked content (e.g., a data source credit panel), the **textual attribution and the actual evidence links** must still be preserved in the UI.

## 🧪 Validation & CI/CD

### Validation steps (recommended)

- Verify each new/changed logo has a corresponding row in **Logo registry** below.
- Verify the file has no embedded executable content:
  - SVGs should not contain scripts or external network references.
- Verify size/performance:
  - Prefer SVG for vector marks when possible.
  - Optimize PNG/WebP to avoid unnecessarily large payloads.
- Verify accessibility in UI usage:
  - provide appropriate `alt` text (or empty `alt=""` if purely decorative).

## 📦 Data & Metadata

### Logo registry (required for each file in this folder)

Add one row per logo file present in this directory.

| File | Mark owner | License / permission | Source / provenance | Retrieval date | Intended UI use | Notes |
|---|---|---|---|---:|---|---|
| `<file.ext>` | `<org>` | `<license or written permission>` | `<URL or internal ref>` | `YYYY-MM-DD` | `<header / credits / etc>` | `<dark/light variant? constraints?>` |

### Naming conventions

- Use **kebab-case** filenames: `kfm.svg`, `partner-usgs.svg`, `data-source-blm-dark.svg`
- Use clear variant suffixes:
  - `-light` and `-dark` for background variants
  - `@2x` only for raster resolution variants (PNG)

### Format guidance

- Preferred: **SVG** (clean paths, correct `viewBox`, no embedded raster, no scripts).
- Raster (PNG/WebP):
  - include a 1x and 2x version when the logo is used at small sizes
  - keep transparent background where appropriate

## 🌐 STAC, DCAT & PROV Alignment

Not applicable for this directory by default.

If a logo must be treated as a published “asset” with explicit provenance in a cataloged release, follow the canonical STAC/DCAT/PROV workflow for that release artifact and reference this directory from the release manifest.

## 🧱 Architecture

This directory is part of the **UI layer** (`web/`) and should remain a passive asset store:
- no runtime network fetching of logo content from untrusted domains,
- no coupling to graph internals (UI reads data through API contracts; assets are local).

## ⚖ FAIR+CARE & Governance

### Review gates

Governance review is recommended when:
- adding a new third‑party mark/logo,
- changing an existing logo’s license/permission details,
- adding logos related to culturally sensitive communities or sovereignty-controlled entities (ensure use is appropriate and documented per `SOVEREIGNTY.md`).

### CARE / sovereignty considerations

If a logo relates to an Indigenous nation/community or sovereignty-controlled entity:
- treat it as **high‑risk by default** until permission/use guidance is documented,
- avoid implying endorsement.

### AI usage constraints

- Do not use AI tools to “recreate” or “approximate” third‑party logos.
- Do not use AI tools to infer ownership/permissions if the license is unclear.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-24 | Initial README for Cesium logo assets directory | TBD |

---

Footer refs:
- Master Guide: `docs/MASTER_GUIDE_v12.md`
- Universal template: `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty policy: `docs/governance/SOVEREIGNTY.md`

