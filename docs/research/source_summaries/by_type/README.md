---
title: "Research Source Summaries — By Type"
path: "docs/research/source_summaries/by_type/README.md"
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

doc_uuid: "urn:kfm:doc:research:source-summaries-by-type-readme:v1.0.0"
semantic_document_id: "kfm-research-source-summaries-by-type-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:research:source-summaries-by-type-readme:v1.0.0"
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

# Research Source Summaries — By Type

## 📘 Overview

### Purpose
This directory holds short, governed summaries of **external sources** (papers, books, datasets, websites, standards, etc.) that inform KFM design decisions and evidence products.

Summaries are organized **by source type** to make discovery and reuse easier across the pipeline (Catalog/Graph/API/UI/Story).

### Scope
| In Scope | Out of Scope |
|---|---|
| Organizing source summaries by type (`books/`, `papers/`, etc.) | Storing primary datasets or derived data products (use `data/` for those) |
| Linkable summaries that capture KFM relevance + implications | Writing Story Nodes themselves (use `docs/reports/story_nodes/`) |
| Capturing citations, links, and extracted constraints/requirements | Defining or changing API contracts (use API contract template) |

### Audience
- Primary: Contributors writing/maintaining research source summaries.
- Secondary: Pipeline developers, ontology/graph designers, UI/story authors looking for rationale and references.

### Definitions (link to glossary)
- Link: `docs/glossary.md` (if present)
- Terms used in this doc:
  - **Source summary**: A short Markdown doc that captures the key ideas of a single external source and how it is relevant to KFM.
  - **Source type**: The top-level bucket under `by_type/` (e.g., `papers/`, `books/`, `datasets/`).
  - **KFM relevance**: Which part(s) of the KFM pipeline the source informs (Catalog, Graph, API, UI, Story/Focus, etc.).

### Key artifacts (what this doc points to)
| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master Guide | `docs/MASTER_GUIDE_v12.md` | KFM Core | Canonical pipeline ordering + invariants. |
| Universal doc template | `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` | KFM Core | Default doc template when no specialized template exists. |
| Story Node template | `docs/templates/TEMPLATE__STORY_NODE_V3.md` | Story | Use when turning evidence into narrative. |
| API contract template | `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md` | API | Use when a source motivates API changes. |

### Definition of done (for this document)
- [ ] Front-matter complete + valid
- [ ] Directory tree reflects actual or intended `by_type/` layout
- [ ] Clear “how to add a summary” steps
- [ ] Constraints/invariants match the Master Guide
- [ ] Governance + CARE/sovereignty considerations explicitly stated

## 🗂️ Directory Layout

### This document
- `path`: `docs/research/source_summaries/by_type/README.md`

### Related repository paths
| Area | Path | What lives here |
|---|---|---|
| KFM canonical guide | `docs/MASTER_GUIDE_v12.md` | System ordering, invariants, extension matrix |
| Templates | `docs/templates/` | Governed doc/story/API templates |
| Story Nodes | `docs/reports/story_nodes/` | Narrative artifacts with provenance |
| Data lifecycle | `data/` | Raw/work/processed + STAC/DCAT/PROV outputs |

### Expected file tree for this sub-area
~~~text
📁 docs/
├── 📁 research/
│   └── 📁 source_summaries/
│       └── 📁 by_type/
│           ├── 📄 README.md
│           ├── 📁 articles/
│           │   └── 📄 <slug>.md
│           ├── 📁 books/
│           │   └── 📄 <slug>.md
│           ├── 📁 datasets/
│           │   └── 📄 <slug>.md
│           ├── 📁 papers/
│           │   └── 📄 <slug>.md
│           ├── 📁 standards/
│           │   └── 📄 <slug>.md
│           └── 📁 websites/
│               └── 📄 <slug>.md
~~~

> Folder names above are the recommended baseline. Add new type folders as needed, but prefer reusing existing ones when practical.

## 🧭 Context

### Background
KFM is designed as a governed geospatial + historical knowledge system with a canonical pipeline ordering and strict provenance expectations. Source summaries help keep decisions reproducible and prevent unsourced narrative from leaking into Focus Mode contexts.

### Assumptions
- This directory is used for **summaries and rationale**, not for authoritative schemas or dataset catalogs.
- Where a source directly informs a pipeline contract, ontology decision, or story claim, the summary should link to the relevant governed artifact (template-driven doc, schema, Story Node, etc.).

### Constraints / invariants
- Canonical pipeline ordering is preserved: **ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode**.
- UI consumes data through API contracts (no direct Neo4j coupling).
- No unsourced narrative in Focus Mode contexts.

### Open questions
| Question | Owner | Target date |
|---|---|---|
| Do we want a specialized “Source Summary” template? | TBD | TBD |
| Should we enforce a controlled vocabulary for source types? | TBD | TBD |
| Should we generate an index (by tag/topic) automatically? | TBD | TBD |

### Future extensions
- Add a sibling classification view, e.g. `docs/research/source_summaries/by_topic/`.
- Add a lightweight lint check that validates:
  - each summary has a citation and stable identifier
  - each summary declares “KFM relevance”
  - internal links resolve

## 🗺️ Diagrams

### How source summaries relate to the KFM pipeline
~~~mermaid
flowchart LR
  S[External source<br/>(paper/book/dataset)] --> SS[Source summary<br/>docs/research/source_summaries/by_type]
  SS --> D[Governed docs / standards<br/>docs/]
  SS --> SN[Story Nodes<br/>docs/reports/story_nodes]
  D --> P[Implementation work<br/>src/ + schemas/ + data/]
  P --> API[Contracts<br/>src/server + docs]
  P --> UI[React/Map UI<br/>web/]
~~~

## 📝 How to add a new source summary

1. **Pick a type folder** under `by_type/` (e.g., `papers/`, `books/`).
   - If no suitable folder exists, create a new one using a clear plural noun (e.g., `talks/`).
2. **Create a single Markdown file per source**, using a stable, readable slug.
   - Recommended slug pattern: `<year>-<first-author-lastname>-<short-title>.md`
   - Example: `2023-smith-stac-best-practices.md`
3. **Use a governed template**:
   - Default: `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`
   - Narrative artifact: `docs/templates/TEMPLATE__STORY_NODE_V3.md`
4. **Include (at minimum)**:
   - Full citation (authors, title, venue/publisher, year)
   - Link/identifier (DOI/URL) and, if applicable, the in-repo file path where the source is stored
   - “Key takeaways” (bullets)
   - “KFM relevance” (which pipeline stages/components this informs)
   - “Claims / constraints” extracted that could become requirements (clearly labeled)
5. **If the source influences Focus Mode narrative**, ensure the downstream Story Node references the source (directly or via an evidence artifact) to preserve provenance.

## 🔒 Governance, ethics, and sensitivity notes
- If a source includes culturally sensitive content or location data, **do not copy or infer sensitive locations** into summaries.
- Follow repo governance docs referenced in this file’s front matter (CARE/sovereignty, ethics, and classification).
- Prefer summaries that help reviewers trace decisions without embedding sensitive raw content.

## ✅ Validation steps
- Markdown renders without broken fenced blocks.
- Internal links resolve (templates, master guide, story node paths).
- No credentials, secrets, or PII included.
- File path in YAML front matter matches the repo path.

## 📚 References
- `docs/MASTER_GUIDE_v12.md`
- `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`
- `docs/templates/TEMPLATE__STORY_NODE_V3.md`
- `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md`

