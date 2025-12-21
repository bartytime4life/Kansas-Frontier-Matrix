---
title: "🧮 Kansas Frontier Matrix — Space Mono Typeface Family (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/public/fonts/Space_Mono/README.md"
version: "v9.7.0"
last_updated: "2025-12-21"
status: "stable"
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

doc_uuid: "urn:kfm:doc:web:public:fonts:space-mono:v9.7.0"
semantic_document_id: "kfm-web-public-fonts-space-mono-v9.7.0"
event_source_id: "ledger:kfm:web:public:fonts:space-mono:v9.7.0"
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

# 🧮 Kansas Frontier Matrix — Space Mono Typeface Family

## 📘 Overview

### Purpose
Provide the **Space Mono** typeface family as a self-hosted, governed UI asset for the Kansas Frontier Matrix (KFM) web client—primarily for:
- telemetry and audit panels,
- code / log rendering,
- AI output “explanations” where monospaced alignment is required.

Space Mono is an upstream open font family commonly distributed under **SIL Open Font License 1.1** (font license). This README is documentation (doc license in front-matter).

### Scope

| In Scope | Out of Scope |
|---|---|
| Space Mono WOFF2 assets, basic usage guidance, and local metadata/checksum expectations for this folder | Defining global branding rules, choosing the system-wide typography stack, or adding new font families outside this folder |

### Audience
- Primary: `web/` frontend engineers, UI/UX design maintainers
- Secondary: accessibility reviewers, release managers, governance reviewers

### Definitions (link to glossary)
- Link: `docs/glossary.md`
- Terms used in this doc: WOFF2, `@font-face`, preload, checksum, provenance, telemetry.

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Folder README | `web/public/fonts/Space_Mono/README.md` | @kfm-design | This document |
| Font file | `web/public/fonts/Space_Mono/SpaceMono-Regular.woff2` | @kfm-web | Required for Regular weight |
| Font file | `web/public/fonts/Space_Mono/SpaceMono-Bold.woff2` | @kfm-web | Required for Bold weight |
| Metadata | `web/public/fonts/Space_Mono/metadata.json` | @kfm-web | License + checksums + build notes |
| Telemetry schema (optional) | `schemas/telemetry/web-public-fonts-spacemono-v1.json` | @kfm-telemetry | If present, governs telemetry fields |
| Release SBOM (optional) | `releases/v9.7.0/sbom.spdx.json` | @kfm-release | If present, lists static assets |
| Release manifest (optional) | `releases/v9.7.0/manifest.zip` | @kfm-release | If present, includes file hash manifest |
| Focus telemetry export (optional) | `releases/v9.7.0/focus-telemetry.json` | @kfm-telemetry | If present, contains runtime metrics |

### Definition of done (for this document)
- [ ] Front-matter complete + valid (template keys preserved)
- [ ] Directory tree matches what is actually shipped
- [ ] Usage snippet(s) reference local font assets (no external CDN assumptions)
- [ ] License reference and checksum expectations documented
- [ ] Validation steps listed and repeatable
- [ ] Governance + CARE/sovereignty considerations explicitly stated (even if “not applicable”)

## 🗂️ Directory Layout

### This document
- `path`: `web/public/fonts/Space_Mono/README.md` (must match front-matter)

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| Frontend | `web/` | React + Map UI |
| Public static assets | `web/public/` | Images, fonts, robots.txt, etc. |
| Font families | `web/public/fonts/` | One folder per font family |
| Schemas | `schemas/` | JSON schemas, including telemetry schemas |
| Releases | `releases/` | Versioned manifests / SBOM / exports (if used) |

### Expected file tree for this sub-area
~~~text
📁 web/
└── 📁 public/
    └── 📁 fonts/
        └── 📁 Space_Mono/
            ├── 📄 README.md
            ├── 📄 metadata.json
            ├── 📄 SpaceMono-Regular.woff2
            └── 📄 SpaceMono-Bold.woff2
~~~

## 🧭 Context

### Background
KFM’s UI includes panels and views where fixed-width alignment improves comprehension (telemetry tables, provenance logs, code samples, and structured AI outputs). A locally hosted monospaced font reduces third-party dependency risk and supports consistent rendering across environments.

### Assumptions
- Fonts are stored in **WOFF2** for web delivery efficiency.
- The web app references these assets via CSS `@font-face` (or equivalent framework integration).
- A `metadata.json` exists (or will exist) to record at minimum: license pointer, checksums, and the upstream acquisition note.

### Constraints / invariants
- ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode ordering is preserved.
- This folder is **UI asset storage**; it does not add or bypass any API/graph access.
- No secrets/credentials embedded in any public asset folder.

### Open questions
| Question | Owner | Target date |
|---|---|---|
| Do we require additional weights (Italic) or a constrained subset for glyph coverage? | @kfm-design | TBD |
| Should `metadata.json` conform to a repo-wide schema (and if so, where is it defined)? | @kfm-architecture | TBD |
| Do releases require SBOM + manifest entries for all `web/public/` assets? | @kfm-release | TBD |

### Future extensions
- Optional font subsetting per locale/scripts while preserving accessibility and code glyph needs.
- Optional preload strategy documentation for performance budgets.

## 🗺️ Diagrams

### System / dataflow diagram
~~~mermaid
flowchart TD
  A["Upstream Space Mono source (font license: SIL OFL 1.1)"] --> B["Conversion / packaging (WOFF2, optional subsetting)"]
  B --> C["metadata.json (license pointer + checksums + notes)"]
  C --> D["web/public/fonts/Space_Mono (static assets)"]
  D --> E["web UI uses @font-face / CSS variables"]
  E --> F["Telemetry (font load/render signals, if enabled)"]
~~~

### Optional: sequence diagram
~~~mermaid
sequenceDiagram
  participant Browser
  participant WebServer as Web Static Server
  participant UI as KFM UI
  Browser->>WebServer: GET /fonts/Space_Mono/SpaceMono-Regular.woff2
  WebServer-->>Browser: 200 (cached WOFF2)
  Browser->>UI: Render telemetry/log/code blocks
  UI-->>UI: (Optional) Emit font load/render telemetry
~~~

## 📦 Data & Metadata

### Inputs
| Input | Format | Where from | Validation |
|---|---|---|---|
| Space Mono upstream package | TTF/OTF (upstream) | Upstream distribution | License and source recorded in metadata |
| Packaging config (optional) | build config | repo build system | Reproducible build notes (if applicable) |

### Outputs
| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Space Mono Regular | WOFF2 | `web/public/fonts/Space_Mono/SpaceMono-Regular.woff2` | File hash tracked in `metadata.json` |
| Space Mono Bold | WOFF2 | `web/public/fonts/Space_Mono/SpaceMono-Bold.woff2` | File hash tracked in `metadata.json` |
| Local metadata | JSON | `web/public/fonts/Space_Mono/metadata.json` | (Schema TBD) |

### Sensitivity & redaction
- None expected. Fonts are public UI assets. Do not embed any user- or system-identifying data in `metadata.json`.

### Quality signals
- File sizes are within performance budgets (define at project level).
- Checksum present for each font asset in `metadata.json`.
- Font rendering tested in common target browsers and reduced-motion/accessibility modes (where relevant).

## 🌐 STAC, DCAT & PROV Alignment

### STAC
- Not applicable: this directory stores **UI static assets**, not cataloged spatiotemporal datasets.

### DCAT
- Not applicable: this directory is not a dataset catalog entry.

### PROV-O
- Optional: if your release pipeline tracks UI assets, capture a PROV activity for:
  - font acquisition,
  - conversion/subsetting,
  - checksum generation.
- If present, link release artifacts (manifest/SBOM) to the PROV activity IDs.

### Versioning
- This README uses `version: v9.7.0` to align with the referenced release bundle naming.
- If the font assets change, bump version per repo release/versioning rules and update checksums + manifests.

## 🧱 Architecture

### Components

| Component | Responsibility | Interface |
|---|---|---|
| `web/public/fonts/Space_Mono/` | Store self-hosted font binaries + metadata | Static file serving |
| Web UI styling layer | Defines `@font-face` and assigns font to selectors | CSS / design tokens |
| Telemetry layer (optional) | Records load + render performance | Telemetry schema under `schemas/telemetry/` |

### Interfaces / contracts

| Contract | Location | Versioning rule |
|---|---|---|
| Telemetry schema (optional) | `schemas/telemetry/web-public-fonts-spacemono-v1.json` | Semver bump if fields change |
| Release SBOM/manifest (optional) | `releases/<ver>/...` | Must include updated hashes when assets change |

### Usage example (CSS)

~~~css
/* Example only — adapt to your UI build system */
@font-face {
  font-family: "Space Mono";
  src: url("/fonts/Space_Mono/SpaceMono-Regular.woff2") format("woff2");
  font-weight: 400;
  font-style: normal;
  font-display: swap;
}

@font-face {
  font-family: "Space Mono";
  src: url("/fonts/Space_Mono/SpaceMono-Bold.woff2") format("woff2");
  font-weight: 700;
  font-style: normal;
  font-display: swap;
}

/* Recommended scope: code + telemetry/log presentation */
code, pre, .telemetry, .audit-log {
  font-family: "Space Mono", ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace;
}
~~~

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode
- Space Mono may be used to render:
  - provenance snippets,
  - “AI explanation” blocks that include structured or code-like content,
  - telemetry/audit panels in Focus Mode views.

### Provenance-linked narrative rule
- Unchanged: fonts do not create narrative content; they affect UI presentation only.

## 🧪 Validation & CI/CD

### Validation steps
- [ ] Markdown protocol checks (front-matter keys present, headings follow template)
- [ ] Font files present + loadable (WOFF2)
- [ ] `metadata.json` present and includes checksums for each shipped WOFF2
- [ ] License reference recorded (SIL OFL 1.1 pointer)
- [ ] Build passes for web client and static asset hosting
- [ ] Accessibility review: code/log readability and fallback behavior

### Reproduction
~~~bash
# Example placeholders — replace with repo-specific commands

# 1) doc lint
# <repo-doc-lint-command>

# 2) verify font checksums against metadata.json
# <repo-checksum-verify-command>

# 3) build web client
# <repo-web-build-command>
~~~

### Telemetry signals (if applicable)
| Signal | Source | Where recorded |
|---|---|---|
| font_file_bytes | build artifact scanner | release manifest / telemetry export |
| font_load_duration_ms | browser performance API | `docs/telemetry/` or release telemetry export |
| font_render_swap_count | UI instrumentation | telemetry export governed by schema |

## ⚖ FAIR+CARE & Governance

### Review gates
- Design review: required for any change to typography defaults.
- Accessibility review: required for any change affecting code/log readability.
- Release review: required if fonts ship in versioned release artifacts (SBOM/manifest).

### CARE / sovereignty considerations
- No sovereignty-sensitive content is expected in font assets.
- Ensure the use of this font does not introduce third-party network calls.

### AI usage constraints
- This document should not be used as a basis to infer or add sensitive location information.
- Any “AI explanation” rendering remains subject to KFM provenance rules; typography does not alter evidence requirements.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v9.7.0 | 2025-12-21 | Reformatted into KFM Universal Governed Doc (v12 strict); retained intent and asset expectations | KFM Docs |
| v9.7.0 | 2025-11-05 | Space Mono folder README initial draft (pre-v12 strict formatting) | KFM Core Team |
| v9.6.0 | 2025-11-04 | Draft notes: FAIR+CARE registration + checksum workflow | KFM Core Team |
| v9.3.2 | 2025-10-28 | Draft notes: typography registry for telemetry UIs | KFM Core Team |

---
Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
~~~