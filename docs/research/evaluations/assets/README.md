---
title: "Research — Evaluations — Assets"
path: "docs/research/evaluations/assets/README.md"
version: "v1.0.0"
last_updated: "2025-12-20"
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

doc_uuid: "urn:kfm:doc:research:evaluations:assets-readme:v1.0.0"
semantic_document_id: "kfm-research-evaluations-assets-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:research:evaluations:assets-readme:v1.0.0"
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

# Research Evaluations Assets

## 📘 Overview

### Purpose
This directory stores *documentation assets* used by evaluation writeups under `docs/research/evaluations/`.
Examples include figures, diagrams, screenshots, and small supporting visuals that are referenced from Markdown reports.

This folder is intentionally **docs-only**: assets here support human-readable documentation and review workflows, and are not intended to be the canonical storage for datasets or pipeline outputs.

### Scope

| In Scope | Out of Scope |
|---|---|
| Figures, charts, screenshots, diagrams referenced by evaluation docs | Raw datasets (use `data/…`) |
| Small, redacted excerpts for documentation purposes | Secrets, tokens, credentials, API keys |
| Visual artifacts derived from evaluation runs (e.g., plots exported from notebooks) | Unredacted PII or sensitive locations |
| UI mock screenshots for evaluation reports | Large binaries that should live in `data/` or artifact storage |

### Audience
- Primary: contributors authoring or reviewing evaluation reports.
- Secondary: maintainers validating governance/CI rules; downstream readers of evaluation documentation.

### Definitions
- Glossary link: `docs/glossary.md` (not confirmed in repo).
- Terms used here: *evaluation*, *artifact*, *asset*, *run_id*, *provenance*.

### Key artifacts

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Evaluation writeups | `docs/research/evaluations/` | Research | Markdown reports that reference assets here |
| Evaluation assets | `docs/research/evaluations/assets/` | Research | This directory |
| Reproducible runs | `mcp/runs/` | MCP | Preferred source of raw evaluation outputs |
| Experiments | `mcp/experiments/` | MCP | Longer-form experiment artifacts |
| Catalog outputs | `data/stac/`, `data/catalog/dcat/`, `data/prov/` | DataOps | Canonical discoverability + provenance |

### Definition of done
- [ ] Front-matter complete and `path` matches this file location.
- [ ] Assets are referenced via relative links from evaluation Markdown.
- [ ] No sensitive information (PII/credentials/restricted locations) is present in assets.
- [ ] Assets are reasonably sized (optimized formats; avoid unnecessary bloat).
- [ ] If an asset represents a *data product* (not just a figure), it is stored under `data/…` and cataloged appropriately (STAC/DCAT/PROV).

## 🗂️ Directory Layout

### This document
- `path`: `docs/research/evaluations/assets/README.md`

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| Evaluation docs | `docs/research/evaluations/` | Reports, protocols, and findings |
| Assets | `docs/research/evaluations/assets/` | Figures/diagrams/screenshots referenced by docs |
| Data lifecycle | `data/raw/` → `data/work/` → `data/processed/` | Canonical datasets + outputs |
| Catalogs | `data/stac/` + `data/catalog/dcat/` + `data/prov/` | Discovery + dataset views + lineage |
| Graph + ontology | `src/graph/` + `docs/graph/` | Graph semantics + constraints |
| APIs | `src/server/` + `docs/` | Contracted access (no direct graph reads from UI) |
| Frontend | `web/` | React + map UI |
| MCP | `mcp/` | Runs, experiments, SOPs, model cards |

### Expected file tree for this sub-area
~~~text
📁 docs/
└── 📁 research/
    └── 📁 evaluations/
        └── 📁 assets/
            ├── 📄 README.md
            ├── 📁 figures/
            │   └── 📄 <evaluation-id>__<figure-name>.png
            ├── 📁 diagrams/
            │   └── 📄 <evaluation-id>__<diagram-name>.svg
            ├── 📁 screenshots/
            │   └── 📄 <evaluation-id>__<screen-name>.png
            └── 📁 tables/
                └── 📄 <evaluation-id>__<table-name>.png
~~~

## 🧭 Context

### Background
Evaluation reports benefit from stable, reviewable assets that render reliably in Markdown viewers and PR diffs.
Keeping these assets in a dedicated folder:
- avoids scattering images throughout prose directories,
- makes review and redaction easier,
- reduces accidental mixing of *docs assets* with *data products*.

### Assumptions
- Evaluation writeups are authored in Markdown and link to assets via relative paths.
- Reproducible/raw outputs remain in `mcp/` and/or `data/` (depending on whether the output is an experiment artifact or a cataloged data product).

### Constraints / invariants
- Canonical pipeline ordering remains unchanged: **ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode**.
- UI consumes data via the API layer (no direct graph dependency).
- Assets here are documentation helpers; canonical data outputs belong under `data/` and should be cataloged when appropriate.

### Open questions

| Question | Owner | Target date |
|---|---|---|
| Should we adopt a lightweight metadata sidecar (e.g., `<asset>.meta.json`) for provenance fields like `run_id`? | TBD | TBD |
| Do we want size limits enforced in CI (e.g., block assets > N MB)? | TBD | TBD |
| Should `docs/research/evaluations/assets/` be Git LFS-backed? | TBD | TBD |

### Future extensions
- Add a small “asset optimization” script (image compression + deterministic naming) under `tools/` (requires human review).
- Add a link checker / orphan-asset detector to CI (requires human review).

## 🗺️ Diagrams

### Documentation asset flow
~~~mermaid
flowchart LR
  A[MCP runs / experiment outputs] --> B[Curate + redact + export figures]
  B --> C[docs/research/evaluations/assets]
  C --> D[docs/research/evaluations/*.md]
  D --> E[PR review + rendered docs]
~~~

## 📦 Data & Metadata

### Inputs

| Input | Format | Where from | Validation |
|---|---|---|---|
| Plots exported from evaluation runs | PNG/SVG/PDF | `mcp/runs/` or notebooks | Visual spot-check; file size sanity |
| Diagrams (architecture, test setup) | SVG/PNG | Diagram tool exports | Ensure text is readable; no secrets |
| Screenshots (UI, API response examples) | PNG | Local capture | Ensure redaction of sensitive fields |

### Outputs

| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Documentation assets | PNG/SVG (preferred), PDF (sparingly) | `docs/research/evaluations/assets/...` | No formal schema; references must be stable |

### Sensitivity & redaction
- Remove/blur:
  - personal identifiers (names, emails, IDs),
  - credentials/tokens,
  - precise sensitive locations (generalize or omit),
  - internal URLs if they expose private infrastructure.
- Prefer “representative” screenshots over raw dumps of sensitive pages.

### Quality signals
- Prefer SVG for diagrams and charts where possible.
- Prefer PNG for plots/screenshots.
- Keep assets as small as practical (optimize before committing).
- Every embedded asset should have descriptive alt text in the referencing Markdown file.

## 🌐 STAC, DCAT & PROV Alignment

### STAC
- Not applicable for most documentation-only assets.
- If an asset is a discoverable spatiotemporal product (map tile, geospatial output, etc.), it should live under `data/` and be cataloged as STAC.

### DCAT
- Not applicable for documentation-only assets.
- Dataset-level descriptions belong in `data/catalog/dcat/`.

### PROV-O
- Documentation assets should reference provenance where practical (e.g., `run_id`, `prov` bundle ID) in the evaluation report text.
- Canonical provenance bundles belong under `data/prov/`.

### Versioning
- Prefer stable filenames; rely on Git history for changes.
- If you must revise an image in a way that could invalidate comparisons, consider a new filename (e.g., suffix `__rev2`) and update the report to clarify.

## 🧱 Architecture

### Components

| Component | Responsibility | Interface |
|---|---|---|
| MCP runs / experiments | Produce evaluation outputs | `mcp/` artifacts + logs |
| Docs assets | Store stable visuals for reports | Relative links from Markdown |
| Evaluation reports | Interpret + summarize findings | Markdown under `docs/research/evaluations/` |
| CI | Validate doc hygiene | Markdown lint, link checks (as configured) |

### Interfaces / contracts
- No API contracts are defined here.
- This folder is documentation support and should not be treated as a system-of-record for data products.

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode
- Evaluation assets may be used *internally* to justify changes to Focus Mode behaviors, but they should not become Focus Mode narrative content unless they:
  - are provenance-linked, and
  - do not disclose restricted/sensitive information.

### Provenance-linked narrative rule
- If evaluation findings are summarized in a Story Node, claims must trace to dataset/record IDs and/or run IDs (and not rely on screenshots alone).

## 🧪 Validation & CI/CD

### Validation steps
- [ ] Markdown protocol checks (front matter + structure).
- [ ] Relative link check: evaluation docs successfully resolve asset paths.
- [ ] Asset hygiene: no secrets/PII; redaction applied where needed.
- [ ] Size check: assets are optimized and not excessively large.
- [ ] Accessibility: images referenced with meaningful alt text.

### Reproduction
~~~bash
# Placeholder — replace with repo-specific commands:
# 1) run markdown lint
# 2) run link checker
# 3) run secret scan
~~~

## ⚖ FAIR+CARE & Governance

### Review gates
- If any asset includes content that could be sensitive (identity, culturally sensitive material, restricted locations), this directory requires **human review** before merging.

### CARE / sovereignty considerations
- Avoid embedding precise coordinates or identifying details for culturally sensitive sites.
- Apply generalization/redaction consistent with `docs/governance/SOVEREIGNTY.md` (not confirmed in repo).

### AI usage constraints
- Do not infer or reconstruct sensitive locations from images.
- Do not add interpretive claims to assets; interpretation belongs in governed evaluation reports with cited evidence.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-20 | Initial README for evaluation assets directory | TBD |

---
Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`

