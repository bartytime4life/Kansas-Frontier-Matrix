---
title: "KFM Web Fonts — README"
path: "web/public/fonts/README.md"
version: "v1.0.0"
last_updated: "2025-12-21"
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

doc_uuid: "urn:kfm:doc:web:public:fonts:readme:v1.0.0"
semantic_document_id: "kfm-web-public-fonts-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:web:public:fonts:readme:v1.0.0"
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

# KFM Web Fonts

## 📘 Overview

### Purpose
This directory contains **redistributable webfont files** used by the KFM web UI. The intent is to:
- keep font assets **local to the repo** (no runtime CDN dependency),
- make **licensing explicit** per font family, and
- support **repeatable builds** for the frontend UI.

### Scope
| In Scope | Out of Scope |
|---|---|
| Webfont binaries served as static assets (e.g., `.woff2`, `.woff`) | Font fetching from third-party CDNs at runtime |
| Per-font licensing files and attribution | Fonts without a clear redistribution license |
| Optional font manifest(s) used by UI build/runtime | Any data pipeline artifacts (ETL/Catalog/Graph/API) |

### Audience
- Primary: Frontend developers maintaining the KFM UI
- Secondary: Designers / content curators selecting typography

### Definitions (link to glossary)
- Link: `docs/glossary.md` (not confirmed in repo)
- Terms used in this doc: “webfont”, “WOFF2”, “subsetting”, “fallback stack”

### Key artifacts (what this doc points to)
| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Font binaries | `web/public/fonts/<family>/*.(woff2|woff)` | UI | Prefer WOFF2 for production payload size |
| Font license | `web/public/fonts/<family>/LICENSE*` or `OFL.txt` | UI | Must be included for each font family |
| Font attribution | `web/public/fonts/<family>/ATTRIBUTION.md` (optional) | UI | Recommended when license requires attribution |
| Optional manifest | `web/public/fonts/fonts.manifest.json` (optional) | UI | Only if the UI needs it (not required by this doc) |

### Definition of done (for this document)
- [ ] Front-matter complete + valid
- [ ] Directory tree + conventions documented
- [ ] Clear “how to add a font” checklist
- [ ] License/attribution requirements stated
- [ ] Validation steps listed and repeatable

## 🗂️ Directory Layout

### This document
- `path`: `web/public/fonts/README.md`

### Related repository paths
| Area | Path | What lives here |
|---|---|---|
| Frontend | `web/` | React/Map UI code + static assets |
| Static assets | `web/public/` | Files served as-is (static hosting) |
| Fonts | `web/public/fonts/` | Webfont binaries + licenses |

### Expected file tree for this sub-area
~~~text
📁 web/
└── 📁 public/
    └── 📁 fonts/
        ├── 📄 README.md
        ├── 📁 <font-family-slug>/
        │   ├── 📄 LICENSE.txt        (or OFL.txt / Apache-2.0.txt / etc.)
        │   ├── 📄 ATTRIBUTION.md     (optional)
        │   ├── 📄 <family>-regular.woff2
        │   ├── 📄 <family>-italic.woff2
        │   ├── 📄 <family>-bold.woff2
        │   └── 📄 <family>-bolditalic.woff2
        └── 📄 fonts.manifest.json     (optional)
~~~

## 🧭 Context

### Background
Web UIs commonly bundle font assets as static files. Without explicit conventions, font files tend to drift:
- unclear licensing/redistribution rights,
- inconsistent naming (hard to reference in CSS),
- bloated payload sizes (e.g., shipping TTF/OTF instead of WOFF2),
- missing attribution.

This README establishes conventions so font assets are traceable and legally distributable.

### Assumptions
- `web/public/` is treated as a static asset root by the frontend build/dev server (not confirmed in repo).
- Font usage is wired through CSS `@font-face` (exact CSS entrypoint not confirmed in repo).

### Constraints / invariants
- This is a **UI-layer** asset area; it must not introduce coupling that bypasses the API boundary.
- Any third-party font added must have a license compatible with redistribution in this repository.

### Open questions
| Question | Owner | Target date |
|---|---|---|
| Where is the canonical CSS entrypoint for `@font-face` rules? | UI | TBD |
| Do we need a `fonts.manifest.json`, or is direct CSS usage sufficient? | UI | TBD |

### Future extensions
- Extension point A: Add font-subsetting workflow (build step) to reduce payload sizes.
- Extension point B: Add CI lint to ensure each `<family>/` includes a license file.

## 🗺️ Diagrams

### System / dataflow diagram
~~~mermaid
flowchart LR
  Browser["Browser"] -->|GET /fonts/...| Static["Static host (web/public)"]
  Static --> FontFiles["WOFF2/WOFF files"]
  Browser -->|CSS @font-face| UI["KFM UI"]
~~~

## 📦 Data & Metadata

### Inputs
| Input | Format | Where from | Validation |
|---|---|---|---|
| Font source package | zip/ttf/otf/woff/woff2 | Vendor/foundry distribution | License must allow redistribution |
| License text | txt/md | Provided by font author | Must be present in repo next to fonts |

### Outputs
| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Webfont(s) | `.woff2` (preferred), `.woff` (optional) | `web/public/fonts/<family>/` | Naming + license conventions (this doc) |

### Sensitivity & redaction
- Fonts in this directory are expected to be **public** and **redistributable**.
- Do not include any font files embedded with sensitive/closed terms.

### Quality signals
- Prefer `.woff2` (smaller, web-optimized).
- Keep file sizes reasonable; avoid shipping unnecessary weights/styles.
- If subsetting is used, document it in `ATTRIBUTION.md` (optional).

## 🌐 STAC, DCAT & PROV Alignment

### STAC
- Not applicable (UI static asset, not a cataloged geospatial asset).

### DCAT
- Not applicable.

### PROV-O
- Not applicable, unless a font-subsetting pipeline is introduced later (in which case capture the transformation activity and inputs).

### Versioning
- Treat changes to font binaries as versioned assets. If a font file changes materially (subset, new version), note it in `ATTRIBUTION.md` and/or a changelog (optional).

## 🧱 Architecture

### Components
| Component | Responsibility | Interface |
|---|---|---|
| UI Static Assets | Serve font files | HTTP GET (static hosting) |
| UI Styling Layer | Reference fonts | CSS `@font-face` + font-family stacks |

### Interfaces / contracts

**CSS `@font-face` example (adjust paths to match actual filenames):**
~~~css
@font-face {
  font-family: "ExampleFont";
  src: url("/fonts/examplefont/examplefont-regular.woff2") format("woff2");
  font-weight: 400;
  font-style: normal;
  font-display: swap;
}
~~~

**Naming convention (recommended):**
- directory: `web/public/fonts/<font-family-slug>/`
- files: `<family>-<style>.woff2` (lowercase, hyphenated)
- include `LICENSE*` in each family folder

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode
- Not applicable directly. Fonts are UI presentation assets.

### Provenance-linked narrative rule
- Not applicable.

## 🧪 Validation & CI/CD

### Validation steps
- [ ] Each `<family>/` folder contains a license file (`LICENSE*` or `OFL.txt`, etc.)
- [ ] Font files are referenced by CSS without 404s (check browser network panel)
- [ ] No runtime dependency on third-party font CDNs unless explicitly approved
- [ ] Filenames are stable and predictable (avoid renaming without updating references)

### Reproduction
~~~bash
# Placeholder — replace with repo-specific UI dev/build commands
# 1) run the UI locally
# 2) load a page that uses the font
# 3) verify the browser requests /fonts/... and receives 200
~~~

### Telemetry signals (if applicable)
| Signal | Source | Where recorded |
|---|---|---|
| (optional) font payload size | build output | `docs/telemetry/` (not confirmed in repo) |

## ⚖ FAIR+CARE & Governance

### Review gates
- License review for any new font family (required).
- UI review to confirm font is actually used and not dead weight.

### CARE / sovereignty considerations
- Not applicable (typography assets), except ensuring no restricted content is embedded in asset metadata.

### AI usage constraints
- Ensure any AI-assisted edits do not fabricate license terms. Licenses must be copied from the font author’s distribution.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-21 | Initial README for web font assets | TBD |

---
Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`