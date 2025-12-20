---
title: "Research — Source Summaries by Type (README)"
path: "docs/research/source_summaries/by_type/README.md"
version: "v1.0.0"
last_updated: "2025-12-20"
status: "draft"
doc_kind: "Readme"
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

# Research — Source Summaries by Type

## 📘 Overview

### Purpose
- This folder organizes research-facing summaries of external sources (papers, books, datasets, web pages) by **source type**.
- Source summaries help KFM contributors decide **what to ingest**, **how to map content to KFM standards/ontology**, and **what downstream artifacts to build** (catalog entries, graph mappings, story nodes).

### Scope
| In Scope | Out of Scope |
|---|---|
| Writing concise summaries of external sources relevant to KFM | Copying large portions of copyrighted texts |
| Capturing bibliographic + licensing metadata for later ingestion | Implementing ETL/crawlers/parsers (belongs in `src/pipelines/`) |
| Extracting candidate entities/fields/geometry/time ranges to inform modeling | Publishing narrative claims in Focus Mode without provenance |
| Recording “next actions” (tickets/PRs) to move a source into the pipeline | Replacing STAC/DCAT/PROV as the system-of-record |

### Audience
- Primary: Researchers, curators, and contributors authoring summaries and planning new data domains.
- Secondary: ETL/catalog/graph/API/UI maintainers who use summaries as input to implementation decisions.

### Definitions (link to glossary)
- Link: `docs/glossary.md`
- Terms used in this doc: **source summary**, **STAC**, **DCAT**, **PROV**, **Story Node**, **Focus Mode**.

### Key artifacts (what this doc points to)
| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Source summary (Markdown) | `docs/research/source_summaries/by_type/<type>/<source>.md` | Curator / contributor | Grouped by source type; each file summarizes one source |
| This README | `docs/research/source_summaries/by_type/README.md` | Docs / governance | Folder rules + pipeline relationship |
| Ingestion tickets / PRs | (repo issue tracker) | Maintainers | Link from each summary to the work that operationalizes it |

### Definition of done (for a source summary)
- [ ] **Citation-ready metadata**: author(s), year, title, publisher/venue, URL/DOI (if applicable), and license or usage restrictions
- [ ] **Relevance**: what KFM use case(s) the source supports (data domain, story theme, method, etc.)
- [ ] **Extractable signals**: candidate entities/fields, spatial/temporal coverage, and any expected data product(s)
- [ ] **Sensitivity check**: note any culturally sensitive content, restricted locations, or personal data risks
- [ ] **Next step**: link to the ticket/PR for ETL/catalog/graph/story work (or mark as “research only”)

## 🗂️ Directory Layout

### This document
- `path`: `docs/research/source_summaries/by_type/README.md`

### Related repository paths
| Area | Path | What lives here |
|---|---|---|
| Research docs | `docs/research/` | Background research, notes, source summaries |
| Data domains | `data/` | Raw/work/processed/stac outputs (when sources are ingested) |
| Pipelines | `src/pipelines/` | ETL + catalog build + transforms |
| Graph | `src/graph/` | Ontology, graph build, mappings |
| Schemas | `schemas/` | JSON schemas + validators |
| Story Nodes | `docs/reports/.../story_nodes/` | Provenance-linked narrative nodes |
| Master pipeline guide | `docs/MASTER_GUIDE_v12.md` | Canonical pipeline + invariants |

### Expected file tree for this sub-area
~~~text
📁 docs/research/source_summaries/
└── 📁 by_type/
    ├── 📄 README.md
    ├── 📁 books/        (example — not confirmed in repo)
    ├── 📁 papers/       (example — not confirmed in repo)
    ├── 📁 datasets/     (example — not confirmed in repo)
    └── 📁 web/          (example — not confirmed in repo)
~~~

## 🧭 Context

### How source summaries relate to the KFM pipeline
Source summaries are **upstream research artifacts** that sit *before* ETL. They are not catalog records and they are not served directly to the UI. They exist to convert “a thing we found” into an actionable, governed plan for KFM’s canonical pipeline:

1. **Research (this folder)**: summarize the source and identify what KFM could extract or learn from it.
2. **ETL**: ingest the source (or derived dataset) into `data/raw/ → data/work/ → data/processed/`.
3. **STAC/DCAT/PROV catalogs**: produce machine-validated metadata records under `data/stac/…`, `data/catalog/dcat/…`, and `data/prov/…`.
4. **Graph (Neo4j)**: map extracted entities to the ontology and load relationships with provenance.
5. **API layer**: expose only contracted, redacted, provenance-linked outputs (UI never reads Neo4j directly).
6. **UI + Story Nodes + Focus Mode**: publish narratives and interactive exploration features that cite the underlying evidence.

Put differently: **source summaries inform what we build**, while **catalogs/graph/APIs are what we run**.

### Background
KFM integrates heterogeneous sources (historical texts, maps, datasets, scholarly methods). Without a “research intake” step, teams risk:
- duplicating ingestion work,
- missing license/sensitivity constraints,
- or designing schemas and ontology mappings without clear evidence requirements.

### Assumptions
- A source may be **research-only** (never ingested) or **pipeline-bound** (intended for ingestion).
- Some summaries will describe **methods** (e.g., statistical, ML, geospatial) rather than datasets; those should still record how the method could create KFM “evidence artifacts” (e.g., derived layers, uncertainty fields).

### Constraints / invariants
- ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode ordering is preserved.
- Frontend consumes contracts via APIs (no direct graph dependency).
- Provenance is mandatory for anything that reaches Story Nodes or Focus Mode.

### Open questions
| Question | Owner | Target date |
|---|---|---|
| Do we standardize a source-summary front-matter schema? | TBD | TBD |
| Do we require stable `source_id` identifiers for cross-linking into STAC/DCAT/PROV? | TBD | TBD |
| Should “method summaries” live alongside “source summaries,” or in a separate folder? | TBD | TBD |

### Future extensions
- Add per-type mini-templates (book vs paper vs dataset) to reduce variance.
- Generate an index page (by theme, time period, geography) from summary metadata.

## 🗺️ Diagrams

### Source summaries in relation to pipeline artifacts
~~~mermaid
flowchart LR
  S["External source\n(paper, book, dataset, web)"] --> SS["Source summary\n(docs/research/source_summaries/by_type)"]

  SS --> D["Governed docs / standards\n(docs/)"]
  SS --> W["Work planning\n(issues, tickets, PRs)"]

  D --> P["Implementation work\n(src/ + schemas/ + data/)"]
  W --> P

  P --> C["Catalogs\n(STAC/DCAT/PROV)"]
  C --> G["Neo4j graph"]
  G --> API["API layer\n(contracts)"]
  API --> UI["React/Map UI"]
  UI --> SN["Story Nodes"]
  SN --> FM["Focus Mode"]
~~~

## 📦 Data & Metadata

### Inputs
| Input | Format | Where from | Validation |
|---|---|---|---|
| External source | PDF / book / website / dataset | Outside repo | License + basic metadata captured in summary |
| Research notes | Markdown | Contributor | Markdown lint + link checks (where configured) |

### Outputs
| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Source summary | Markdown | `docs/research/source_summaries/by_type/<type>/...` | (not confirmed in repo — consider adding a schema if needed) |
| Implementation plan | Issues / PRs | repo tracker | Must reference STAC/DCAT/PROV + provenance needs |

### Sensitivity & redaction
- If a source includes sensitive locations, personally identifying data, or culturally restricted knowledge:
  - summarize at a higher level,
  - avoid reproducing sensitive details,
  - and flag the needed governance review before ingestion.

### Quality signals
- Clear “what KFM can extract” statements (entities, fields, geometry, time range).
- License clarity (what can be redistributed, what must remain internal).

## 🌐 STAC, DCAT & PROV Alignment

### STAC
- Source summaries may reference STAC IDs *after* ingestion (e.g., “this dataset is now `stac:item:<id>`”).
- Do not treat a summary as a substitute for STAC Item/Collection metadata.

### DCAT
- When a source becomes a published dataset in KFM, add a DCAT dataset entry and back-link it from the summary.

### PROV-O
- If a source summary informs a derived artifact (e.g., a cleaned dataset or extracted entity set), link the eventual PROV activity/run ID back to the summary for traceability.

### Versioning
- If a source changes (new edition, updated dataset release), prefer:
  - a new summary file (or a clear “version” section),
  - plus predecessor/successor links in any downstream STAC/DCAT records.

## 🧱 Architecture

### Components
| Component | Responsibility | Interface |
|---|---|---|
| Source summaries | Research intake + planning | Markdown + links to work items |
| ETL | Ingest + normalize sources | `src/pipelines/` configs + run logs |
| Catalogs | Machine-validated metadata | STAC/DCAT/PROV files + validators |
| Graph | Semantic linkage | Neo4j (behind API boundary) |
| APIs | Contracted access | REST/GraphQL + tests |
| UI | Exploration + narrative UX | API calls only |
| Story Nodes | Curated narrative | Markdown + provenance refs |
| Focus Mode | Contextual synthesis | Provenance-linked context bundle |

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode
- Source summaries **do not automatically surface** in Focus Mode.
- A source’s content surfaces only after it is:
  1) ingested + cataloged, and
  2) connected to entities/layers via graph + API contracts, and/or
  3) curated into Story Nodes with citations.

### Provenance-linked narrative rule
- Story Nodes must cite **primary evidence** (datasets/documents/assets), not just a secondary summary.
- Source summaries can be used as curator notes, context, or method rationale, but not as the sole evidentiary anchor.

## 🧪 Validation & CI/CD

### Validation steps
- [ ] Markdown protocol checks (lint/format)
- [ ] No secrets/credentials
- [ ] No prohibited AI actions implied (e.g., inferring sensitive locations)
- [ ] External links are stable where possible (prefer DOI/permalink)
- [ ] Licensing notes present (redistribution allowed vs restricted)

### Reproduction
~~~bash
# (optional) If your repo has doc tooling, add the commands here.
# Examples:
# 1) markdown lint
# 2) link checker
# 3) spell check
~~~

## ⚖ FAIR+CARE & Governance

### Review gates
- New external sources intended for ingestion should trigger:
  - license review,
  - sensitivity review (CARE/sovereignty),
  - and (if applicable) security review for automated downloads/parsers.

### CARE / sovereignty considerations
- Some materials may require redaction/generalization before public release.
- When in doubt: document the concern in the summary and route through governance refs below.

### AI usage constraints
- Follow `ai_transform_permissions` / `ai_transform_prohibited` in the front-matter.
- Do not add speculative claims; distinguish facts vs interpretations.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-20 | Initial README for `source_summaries/by_type` | TBD |

---
Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`

