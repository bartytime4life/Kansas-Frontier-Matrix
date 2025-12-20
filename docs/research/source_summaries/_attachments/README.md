---
title: "Research Source Summaries — Attachments README"
path: "docs/research/source_summaries/_attachments/README.md"
version: "v1.0.0"
last_updated: "2025-12-20"
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

doc_uuid: "urn:kfm:doc:research:source-summaries:attachments-readme:v1.0.0"
semantic_document_id: "kfm-research-source-summaries-attachments-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:research:source-summaries:attachments-readme:v1.0.0"
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

# Research Source Summaries Attachments

## 📘 Overview

### Purpose
This folder is reserved for **binary attachments referenced by** Markdown source summaries under `docs/research/source_summaries/`.

Use it to keep source summaries:
- readable in-repo (local rendering),
- stable over time (no link rot),
- governance-compliant (explicit handling of sensitivity and licensing).

### Scope

| In Scope | Out of Scope |
|---|---|
| Images, figures, screenshots, cropped excerpts, small supporting PDFs that are **directly referenced** by one or more source summaries. | Raw datasets for ETL, large media dumps, secrets/credentials, sensitive or restricted location data, files not referenced anywhere, or canonical “data assets” that should live under `data/` and be cataloged. |

### Audience
- Primary: authors/editors of `docs/research/source_summaries/*.md`
- Secondary: reviewers (historian/editor), governance/security reviewers, CI maintainers

### Definitions (link to glossary)
- Link: `docs/glossary.md` (not confirmed in repo)
- Terms used in this doc:
  - **Source summary**: A concise, evidence-led summary of a research source used by KFM.
  - **Attachment**: A file stored in this folder and linked from a source summary.
  - **Sidecar metadata**: An optional small text file that records provenance/license notes for an attachment.

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| This README | `docs/research/source_summaries/_attachments/README.md` | Docs maintainers | Folder contract + conventions |
| Attachments | `docs/research/source_summaries/_attachments/*` | Source summary authors | Must be referenced by at least one source summary |
| Source summaries | `docs/research/source_summaries/` | Research contributors | Markdown files that link to attachments |

### Definition of done (for this document)
- [ ] Folder purpose and “what goes where” boundaries are explicit.
- [ ] Markdown linking examples are provided and correct.
- [ ] Sensitivity + licensing expectations are documented.
- [ ] No prohibited AI actions are implied (especially no inference of sensitive locations).

## 🗂️ Directory Layout

### This document
- `path`: `docs/research/source_summaries/_attachments/README.md`

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| Source summaries | `docs/research/source_summaries/` | Research summaries that may later be promoted into Story Nodes |
| Attachments | `docs/research/source_summaries/_attachments/` | Binary assets referenced by source summaries |
| Documentation | `docs/` | Canonical governed docs |
| Data domains | `data/` | Raw/work/processed datasets and catalog outputs |
| Catalog outputs | `data/stac/` / `data/catalog/dcat/` / `data/prov/` | STAC/DCAT/PROV artifacts for cataloged datasets |
| Graph | `src/graph/` | Ontology + graph build |
| APIs | `src/server/` | Contracted access layer (UI must not read Neo4j directly) |
| UI | `web/` | React/Map UI |

### Expected file tree for this sub-area
~~~text
📁 docs/
└── 📁 research/
    └── 📁 source_summaries/
        ├── 📁 _attachments/
        │   ├── 📄 README.md
        │   ├── 🖼️ <figure-or-screenshot>.<png|jpg|svg>
        │   ├── 📄 <small-supporting-doc>.<pdf>
        │   └── 📝 <optional-sidecar>.<md|json>
        └── 📄 <source_summary>.md
~~~

## 🧭 Context

### Background
Source summaries often need supporting visuals (e.g., a cropped figure, a screenshot of a table, a map inset) to capture evidence that would otherwise be cumbersome to describe in text. Keeping those supporting artifacts alongside the summaries helps preserve meaning and improves reviewability.

### Assumptions
- This directory is intended for **documentation-facing** assets (not pipeline-ingested data).  
- Source summaries reference attachments via **relative links** so they render in typical Markdown viewers.

### Constraints / invariants
- ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode ordering is preserved.
- Frontend/UI consumes contracts via APIs (no direct graph dependency).
- Do **not** store sensitive or restricted information in this public/open folder.
- Do **not** place canonical datasets here. If an asset is part of the data lifecycle, it belongs under `data/` and should be cataloged (STAC/DCAT/PROV) as applicable.

### Open questions

| Question | Owner | Target date |
|---|---|---|
| Should attachments require a sidecar metadata file (provenance/license) by policy? | TBD | TBD |
| Should CI enforce “no orphan attachments” (files not referenced by any `.md`)? | TBD | TBD |
| Are there repo-wide file size limits or LFS rules that should be reflected here? | TBD | TBD |

### Future extensions
- Add a lightweight link-check or manifest generator to detect orphaned attachments.
- Add a recommended sidecar schema (e.g., `*.meta.json`) if governance requires it.

## 🗺️ Diagrams

### System / dataflow diagram
~~~mermaid
flowchart LR
  A[Research source] --> B[Source summary markdown]
  B --> C[_attachments binaries]
  B --> D[Story Nodes promotion]
  D --> E[Focus Mode narrative]
~~~

### Optional: sequence diagram
~~~mermaid
sequenceDiagram
  participant Author
  participant Repo
  Author->>Repo: Add attachment + link it from source summary
  Repo-->>Author: Markdown renders attachment via relative link
~~~

## 📦 Data & Metadata

### Inputs

| Input | Format | Where from | Validation |
|---|---|---|---|
| Figure/screenshot | PNG/JPG/SVG | Manual capture from research sources | Visual review + licensing check |
| Supporting document | PDF | Extracted excerpt or small appendix | Visual review + licensing check |
| Optional sidecar metadata | MD/JSON | Authored by contributor | Review for completeness |

### Outputs

| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Stored attachment | Binary | `docs/research/source_summaries/_attachments/` | Folder rules in this README |
| Renderable links | Markdown | `docs/research/source_summaries/*.md` | Relative links; no broken refs |

### Sensitivity & redaction
- This folder is **public/open** by default.
- Do not store:
  - sensitive locations,
  - restricted cultural knowledge,
  - private personal information (PII),
  - credentials/secrets,
  - anything that would violate sovereignty or ethics constraints.
- If an attachment must exist but contains sensitive material, it should be handled via the project’s governance workflow (location and mechanism not confirmed in repo).

### Quality signals
- File is referenced by at least one source summary.
- Filename is stable (avoid renaming once linked).
- Link renders correctly in a standard Markdown renderer.
- Provenance and licensing notes exist in the source summary (and/or sidecar).

## 🌐 STAC, DCAT & PROV Alignment

### STAC
- Attachments in this folder are **not** assumed to be STAC assets.
- If an artifact is a canonical, discoverable data asset (map, raster, geospatial layer, etc.), it should live under `data/` and be represented via STAC (per the pipeline).

### DCAT
- This folder is documentation support and typically not a DCAT dataset.
- If an attachment set evolves into a distributable dataset, it should be formalized as a DCAT dataset record (location and process governed elsewhere).

### PROV-O
- Attachments should still be provenance-aware:
  - The source summary linking to the attachment should record the originating document/source identifier and retrieval context.
  - Optional: include a sidecar file that records origin URL/citation, retrieval date, and any transformation notes (crop, redact, annotate).

### Versioning
- Prefer stable filenames over frequent renames.
- If a file must change materially, add a new versioned filename rather than overwriting in-place.

## 🧱 Architecture

### Components

| Component | Responsibility | Interface |
|---|---|---|
| Docs (source summaries) | Human-readable summaries with evidence | Markdown + relative links |
| Attachments folder | Stores evidence artifacts referenced by docs | Git-tracked binary files |
| Story Nodes (future) | Curated narrative artifacts | Governed docs + provenance links |

### Interfaces / contracts

| Contract | Location | Versioning rule |
|---|---|---|
| Folder rules | This README | Update with semver + version history |
| Source summary linking | Source summary markdown | Links must remain valid |

### Extension points checklist (for future work)
- [ ] Add a sidecar metadata convention (`*.meta.md` or `*.meta.json`)
- [ ] Add CI rule for orphan attachments
- [ ] Add a lightweight “attachment manifest” generator

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode
- Attachments here are primarily for **research/source summary** readability.
- When a source summary is promoted into a Story Node, any needed visuals should:
  - remain provenance-linked, and
  - be reviewed for public suitability (redaction, sensitivity, licensing).

### Provenance-linked narrative rule
- Every factual claim should trace to a dataset / record / document ID (or a clear citation) in the source summary.

### Optional structured controls
~~~yaml
focus_layers:
  - "TBD"
focus_time: "TBD"
focus_center: [ -98.0000, 38.0000 ]
~~~

## 🧪 Validation & CI/CD

### Validation steps
- [ ] Markdown link check passes (no broken references to `_attachments/`)
- [ ] No obviously sensitive content stored in this folder
- [ ] Licensing/provenance is documented (in the source summary and/or sidecar)
- [ ] Filenames are stable and reasonably descriptive

### Reproduction
~~~bash
# Repo-specific commands not confirmed in repo.
# Suggested checks (adapt to your tooling):
# - markdown lint
# - link checker
# - forbidden-files scan (executables, secrets)
~~~

### Telemetry signals (if applicable)

| Signal | Source | Where recorded |
|---|---|---|
| Orphan attachments count | CI check | `docs/telemetry/` + `schemas/telemetry/` (not confirmed in repo) |

## ⚖ FAIR+CARE & Governance

### Review gates
- Historian/editor review: recommended when attachments are used to support public narrative.
- Security/sovereignty review: required if there is any risk of sensitive or restricted information.

### CARE / sovereignty considerations
- Avoid storing content that could enable harm (e.g., sensitive site locations).
- Respect community data sovereignty constraints (see governance refs in front-matter).

### AI usage constraints
- Do not use attachments to infer sensitive locations.
- Do not “upgrade” attachments into claims without explicit, cited evidence.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-20 | Initial README for source summary attachments folder | TBD |

---
Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`

