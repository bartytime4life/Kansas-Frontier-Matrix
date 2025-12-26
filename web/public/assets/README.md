---
title: "KFM Web UI — Public Assets"
path: "web/public/assets/README.md"
version: "v1.0.0"
last_updated: "2025-12-26"
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

doc_uuid: "urn:kfm:doc:web:public-assets:readme:v1.0.0"
semantic_document_id: "kfm-web-public-assets-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:web:public-assets:readme:v1.0.0"
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

# KFM Web UI — Public Assets

Static, publicly-served assets used by the KFM web application UI.

> **Public exposure note:** Anything committed under `web/public/assets/` is assumed to be publicly reachable by the deployed web app. Treat every file here as **world-readable**.

---

## 📘 Overview

### Purpose

- Define what is allowed to live in `web/public/assets/` and how it should be organized.
- Prevent pipeline leakage (datasets, provenance artifacts, secrets) into the public UI asset surface.
- Ensure every asset is **licensed**, **attributed**, and **safe to expose**.

### Scope

| In Scope | Out of Scope |
|---|---|
| UI imagery (icons, logos, UI illustrations), fonts, map UI static resources (sprites/glyphs if used), and other *static* frontend assets that must be served “as-is” | Raw/work/processed datasets (`data/**`), catalog artifacts (STAC/DCAT/PROV), graph export/import artifacts, API payload caches, secrets/tokens/credentials, and any file that should not be publicly distributed |
| Small, UI-only reference files (e.g., static copy blocks, UI help images) | Narrative evidence products for Story Nodes (should live with Story Node artifacts under `docs/reports/story_nodes/` unless explicitly required in the UI) |

### Audience

- Primary: UI contributors maintaining the web app (`web/`) and its map/narrative experiences.
- Secondary: Reviewers performing security, licensing, and governance checks for public content.

### Definitions (link to glossary)

- Link: `docs/glossary.md` *(not confirmed in repo)*
- Terms used in this doc:
  - **Public asset**: a static file served by the web app without an API call.
  - **Third-party asset**: any asset sourced externally (icons, fonts, imagery, basemap style snippets, etc.).
  - **Sensitive location signal**: any content that could reveal restricted/sensitive locations (including image EXIF GPS metadata, screenshots with pinpoint markers, or detailed coordinates embedded in JSON).

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| This README | `web/public/assets/README.md` | UI maintainers | Responsibilities + rules for this folder |
| Web UI root | `web/` | UI maintainers | UI reads through API boundary only |
| API boundary | `src/server/` | API maintainers | Enforces redaction/generalization and contracts |
| Canonical governance | `docs/governance/*` | Governance owners | Overrides any local guidance |
| Story Nodes | `docs/reports/story_nodes/` | Narrative curators | Narrative assets generally belong with Story Nodes |

### Definition of done (for this document)

- [x] Front-matter complete + `path` matches file location
- [x] Folder purpose and “what belongs here” rules documented
- [x] Public exposure + sensitivity constraints explicit
- [x] Attribution mechanism defined for third‑party assets
- [ ] Validation steps listed and repeatable (repo-specific commands linked when available)
- [ ] Maintainer/governance review completed (as applicable)

---

## 🗂️ Directory Layout

### This document

- `path`: `web/public/assets/README.md` (must match front-matter)

### Related repository paths (orientation)

| Area | Path | What lives here |
|---|---|---|
| Data domains | `data/` | Raw/work/processed domain data; catalog outputs by stage |
| Catalog outputs | `data/stac/` + `data/catalog/dcat/` + `data/prov/` | STAC/DCAT/PROV artifacts (canonical evidence + lineage) |
| Graph | `src/graph/` (+ `data/graph/` if present) | Ontology bindings, graph build, import fixtures |
| Pipelines | `src/pipelines/` | Deterministic transforms and catalog builders |
| API boundary | `src/server/` *(v13 target)* or `src/api/` *(if legacy; not confirmed in repo)* | Contracts, redaction, access controls, query services |
| UI | `web/` | React/Map UI (must not read Neo4j directly) |
| Story Nodes | `docs/reports/story_nodes/` | Curated narrative artifacts and supporting assets |
| Schemas | `schemas/` | JSON Schemas, contract validation, UI validation schemas |
| Tests | `tests/` | Unit/integration/contract tests |

### Expected file tree for this sub-area

> Note: Subfolders are **recommended**. Keep this tree synchronized with what actually exists in-repo.

~~~text
📁 web/
└── 📁 public/
    └── 📁 assets/
        ├── 📄 README.md
        ├── 📁 brand/              # optional; not confirmed in repo (logos, marks, favicon sources)
        ├── 📁 icons/              # optional; not confirmed in repo (svg/png icons)
        ├── 📁 images/             # optional; not confirmed in repo (UI illustrations, screenshots)
        ├── 📁 fonts/              # optional; not confirmed in repo (self-hosted fonts, woff2 preferred)
        ├── 📁 map/                # optional; not confirmed in repo (sprites/glyphs/style JSON if used)
        └── 📁 third_party/        # optional; not confirmed in repo (vendor assets; keep minimal)
~~~

---

## 🧭 Context

KFM is intentionally staged (ETL → catalogs → graph → API → UI → narratives) to keep the system modular, testable, and auditable.

This folder is part of the **UI stage**. It must not become a “shadow data store” that bypasses catalogs, provenance, governance review, or the API boundary.

### Constraints / invariants

- **No UI direct-to-graph reads:** the web UI must never query Neo4j directly; access must be mediated by API contracts.
- **Public exposure:** any committed asset here may be distributed publicly; do not place restricted, private, or sensitive materials here.
- **No datasets in assets:** raw/work/processed datasets belong under `data/**`, not under `web/**`.
- **No secrets:** never commit tokens, credentials, private URLs, or internal endpoints inside assets (including inside JSON).
- **No sensitive-location inference:** avoid shipping assets that reveal sensitive locations (including embedded EXIF GPS metadata).

---

## ✅ What belongs here

### Common allowed asset types

- UI chrome:
  - logos, wordmarks, branding assets
  - icons (SVG/PNG), UI illustrations
- Fonts (self-hosted only when licensing permits)
- Map UI static resources (only if used by the web app):
  - sprite sheets / glyph ranges
  - static style fragments without secrets/tokens
- Documentation-like UI assets that must be served from the app:
  - onboarding images
  - feature walkthrough screenshots (redacted if needed)

### Strongly discouraged (use only with explicit review)

- Any asset that looks like a dataset (GeoJSON, CSV, shapefiles, large JSON blobs).
- Any map screenshot that could expose precise coordinates, sensitive infrastructure, or culturally sensitive locations.
- Any third-party media without clear license + attribution.

---

## 🚫 What must NOT be committed here

- **Data pipeline outputs**:
  - `data/**` artifacts (raw/work/processed)
  - STAC/DCAT/PROV outputs
  - graph import/export artifacts
- **Secrets / credentials**:
  - `.env*`, API keys, access tokens, private endpoints
- **Restricted content**:
  - content covered by sovereignty restrictions
  - content that reveals sensitive/restricted locations
  - content that includes PII or identifying information about individuals (unless explicitly approved and governed)

---

## 🧾 Attribution & third-party assets

If you add **any** third-party asset, you must record:
- source authority (where it came from),
- retrieval date,
- license and any attribution requirements,
- and any modification you performed (resize, recolor, optimize, etc.).

### Third-party asset registry (update when adding external assets)

| Asset path | Source authority | Retrieval date | License | Notes / modifications |
|---|---|---|---|---|
| *(none yet)* |  |  |  |  |

---

## 🧼 Asset hygiene checklist

### Images (PNG/JPG/WebP/SVG)

- Strip metadata (especially EXIF GPS) before committing.
- Prefer smaller/optimized variants (keep page-load cost low).
- Avoid embedding text that makes factual claims unless that claim is provenance-linked elsewhere (Story Nodes / catalogs).

### Fonts

- Only self-host fonts with explicit redistribution rights.
- Prefer `woff2` when possible.
- Keep font families minimal.

### JSON / config files placed here

- Must not include secrets (tokens, keys).
- Must not embed detailed coordinates if avoidable.
- Must not duplicate canonical catalog or graph content.

---

## 🧪 Validation & CI/CD

### Validation steps (repo-specific commands not confirmed)

- [ ] Markdown protocol checks (front matter present, path correct)
- [ ] Security scanning (secrets, tokens, private URLs)
- [ ] License/attribution review for new third-party assets
- [ ] UI build checks (assets resolve, paths correct, no 404s)
- [ ] Accessibility checks for any UI usage of assets (alt text, contrast, etc.)

~~~bash
# Example placeholders — replace with repo-specific commands

# 1) markdown lint / protocol checks
# <not confirmed in repo>

# 2) secret scanning
# <not confirmed in repo>

# 3) UI build
# <not confirmed in repo>
~~~

---

## ⚖ FAIR+CARE & Governance

### Review gates

- Any new third-party asset requires a license + attribution entry in this README (table above).
- Any asset that could expose sensitive locations, sovereignty-controlled information, or culturally sensitive context requires governance review (see `docs/governance/*`).

### CARE / sovereignty considerations

- Treat culturally sensitive content as high-risk by default.
- If an asset depicts places, artifacts, or communities subject to sovereignty rules:
  - do not publish the asset here unless allowed by policy,
  - apply redaction/generalization as required,
  - document the decision trail in the appropriate governance process.

### AI usage constraints

- Allowed: structural extraction, summarization, translation, keyword indexing.
- Prohibited: generating new policy text or inferring sensitive locations from assets.

---

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-26 | Initial README for `web/public/assets/` (rules, attribution registry, hygiene checklist) | TBD |

---

Footer refs:

- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`

