<div align="center">

# 📝 Kansas Frontier Matrix — Notes Workspace  
`docs/notes/README.md`

**Mission:** Maintain a **lightweight, versioned knowledge workspace** for  
working notes, research logs, and early drafts that evolve into formal  
MCP documentation and structured knowledge graph entries.

[![Docs · MCP-DL v6.2](https://img.shields.io/badge/Docs-MCP--DL%20v6.2-blue)](../standards/markdown_guide.md)
[![Knowledge Graph](https://img.shields.io/badge/Linked-Knowledge%20Graph-green)](../architecture/knowledge-graph.md)
[![Versioned Notes](https://img.shields.io/badge/Notes-Versioned-orange)](README.md)
[![Git Provenance](https://img.shields.io/badge/Provenance-Git%20Tracked-blueviolet)](../../data/work/logs/docs/)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-lightgrey)](../../LICENSE)
[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../.github/workflows/site.yml)
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](../../.github/workflows/stac-validate.yml)
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](../../.github/workflows/codeql.yml)
[![Trivy Security](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](../../.github/workflows/trivy.yml)

</div>

---

## 📚 Table of Contents

- [🎯 Purpose](#-purpose)  
- [🧩 MCP Note Lifecycle](#-mcp-note-lifecycle)  
- [🧱 Directory Layout](#-directory-layout)  
- [🗂️ Note Types](#️-note-types)  
- [📋 Recommended Note Structure (YAML Front-Matter)](#-recommended-note-structure-yaml-front-matter)  
- [🧭 Metadata Schema](#-metadata-schema)  
- [🧾 Suggested Workflow](#-suggested-workflow)  
- [🧠 Linking Notes to the Knowledge Graph](#-linking-notes-to-the-knowledge-graph)  
- [📦 Example Note Templates](#-example-note-templates)  
- [🏷️ Tagging & Discovery](#️-tagging--discovery)  
- [🗄️ Archiving & Filenames](#️-archiving--filenames)  
- [🤖 AI Assistant & Automation](#-ai-assistant--automation)  
- [✅ Contributor Checklist](#-contributor-checklist)  
- [🤖 CI Integration & Validation](#-ci-integration--validation)  
- [📎 Related Documentation](#-related-documentation)  
- [🚀 Roadmap](#-roadmap)  
- [📅 Version History](#-version-history)

---

## 🎯 Purpose

The `/docs/notes/` directory is a **sandbox for thinking in public** —  
an **idea incubator** where concepts, discussions, and discoveries are captured  
before formalization into architecture, design, or integration documents.

Notes serve as:

* 🧠 **Working drafts** — capture ideas fast before structure hardens.  
* 🔍 **Research digests** — summaries of archives, datasets, and oral histories.  
* 🗓️ **Meeting & sprint logs** — record decisions, blockers, and insights.  
* ⚙️ **Technical backlogs** — track pending work or experimental prototypes.  
* 🧾 **Idea provenance** — keep “why we thought this” context in Git forever.

> **MCP Principle:** *Write fast. Preserve context. Promote when reproducible.*

---

## 🧩 MCP Note Lifecycle

```mermaid
flowchart LR
    A["✍️ Draft Note<br>(/docs/notes/research.md, ideas.md)"] --> B["🧭 Review / Discussion<br>(team + Git comments)"]
    B --> C["🧱 Stabilize Insight<br>(cross-linked to data, commits, and sources)"]
    C --> D["🚀 Promote to Formal Doc<br>(/architecture /design /integration)"]
    D --> E["🗂️ Archive Note<br>(/docs/notes/archive/)"]

    style A fill:#f9fbff,stroke:#0077cc
    style B fill:#f7f0ff,stroke:#9966cc
    style C fill:#f3fcf3,stroke:#33aa33
    style D fill:#fffbea,stroke:#e8a500
    style E fill:#f9f9f9,stroke:#888888
```
<!-- END OF MERMAID -->

---

## 🧱 Directory Layout

```text
docs/notes/
├── README.md          # Index (this file)
├── research.md        # Ad-hoc research notes & references
├── meetings.md        # Meeting logs, retrospectives, decisions
├── ideas.md           # Early brainstorms, experimental concepts
├── backlog.md         # Pending tasks, technical debt, blockers
├── templates/         # Optional note + meeting templates
└── archive/           # Deprecated or closed notes (retained for provenance)
```

---

## 🗂️ Note Types

| File | Purpose |
| :--- | :------- |
| `research.md` | Scratchpad for datasets, literature, references. |
| `meetings.md` | Agile retrospectives, agenda logs, team updates. |
| `ideas.md` | Experimental ideas, hypotheses, technical sketches. |
| `backlog.md` | Short-term tasks, tech debt tracking, feature backlog. |
| `templates/` | Prebuilt YAML & Markdown templates for uniform structure. |
| `archive/` | Long-term record of finalized or deprecated notes. |

> **Tip:** If a note becomes foundational, promote it to `/docs/architecture/` or `/docs/design/`.

---

## 📋 Recommended Note Structure (YAML Front-Matter)

```yaml
---
title: "Hydrology Dataset Crosswalk — Early Draft"
author: "KFM Hydrology Team"
date: 2025-10-05
status: draft          # draft | review | stable | archived
tags: ["hydrology", "dataset", "integration"]
linked_datasets:
  - data/stac/hydro/usgs_streamflow_ks_1900_2020.json
linked_commits:
  - a3f29e9
linked_docs:
  - ../architecture/data-architecture.md
period:
  id: "perio.do/dust-bowl-1930s"
  label: "Dust Bowl Era"
ai_assist:
  summarize: true
  embed_in_graph: true
  vector_model: "sentence-transformers/all-MiniLM-L6-v2"
---
```

---

## 🧭 Metadata Schema

| Field | Description | Example |
| :-- | :-- | :-- |
| `title` | Concise subject line | “LiDAR DEM Pipeline – Draft Hypothesis” |
| `author` | Individual or team | `"KFM Hydrology Team"` |
| `date` | ISO 8601 date | `2025-10-05` |
| `status` | Lifecycle stage | `draft`, `review`, `stable`, `archived` |
| `tags` | Keywords / ontology concepts | `["terrain","LiDAR","ETL"]` |
| `linked_*` | Crosslinks to artifacts | Dataset paths, commits, docs |
| `period` | Historical period (from PeriodO) | `"Dust Bowl Era"` |
| `ai_assist` | AI workflow flags | Summarization / embedding settings |
| `references` | Optional bibliography | `["doi:10.123/abc","url:https://example.org"]` |

> Schema defined at: `docs/schemas/note.schema.json` and validated by CI.

---

## 🧾 Suggested Workflow

| Stage | Action | Description |
| :-- | :-- | :-- |
| **1️⃣ Capture** | Add note or section to `research.md`. | Minimal viable capture of ideas. |
| **2️⃣ Link** | Cross-reference datasets, commits, or external docs. | Maintain provenance. |
| **3️⃣ Review** | Open PR for comments. | Team discussion or validation. |
| **4️⃣ Promote** | Move to `/architecture/`, `/design/`, or `/integration/`. | When reproducible or validated. |
| **5️⃣ Archive** | Move into `/archive/<year>/`. | Lock history, mark `status: archived`. |

> **Golden Rule:** *Nothing is deleted — all knowledge is preserved through Git + Archive.*

---

## 🧠 Linking Notes to the Knowledge Graph

Each note is ingested as an entity in the **Neo4j / RDF knowledge graph**, aligning with **CIDOC-CRM**, **PROV-O**, and **OWL-Time** ontologies.

```turtle
@prefix kfm: <https://kfm.org/id/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix dc:   <http://purl.org/dc/terms/> .

kfm:note/hydrology_crosswalk
    a prov:Entity ;
    dc:title "Hydrology Dataset Crosswalk — Early Draft" ;
    prov:wasDerivedFrom kfm:dataset/usgs_streamflow_ks_1900_2020 ;
    prov:wasGeneratedBy kfm:process/research_sprint_oct2025 ;
    dc:creator "KFM Hydrology Team" ;
    dc:date "2025-10-05"^^xsd:date .
```

> Notes are then vectorized for semantic search and queryable via the KFM web UI.

---

## 📦 Example Note Templates

**Quick Idea Template**

```markdown
# 💡 Idea: [Short Title]
*Date:* YYYY-MM-DD  
*Author:* Your Name  
*Status:* draft  

## Context
Origin or trigger of the idea.

## Hypothesis
If X → then Y.

## Linked Data
- `data/sources/...`
- Commit: `<hash>`
- STAC: `<item>.json`

## Next Steps
1. Validate concept.
2. Add to backlog.md if actionable.
```

**Meeting Log Template**

```markdown
# 🗓️ Meeting – [Topic]
*Date:* YYYY-MM-DD  
*Participants:* …  
*Recording:* link (if applicable)

## Agenda
1. …

## Notes & Decisions
- …

## Action Items
- [ ] Owner — Task
```

---

## 🏷️ Tagging & Discovery

Tags map into a **controlled SKOS vocabulary** in `data/vocabularies/tags.skos.ttl`.  
Each note’s tags are converted into RDF triples and indexed for federated search.

| Tag Type | Example | Used For |
| :-- | :-- | :-- |
| **Domain** | `#climate`, `#archaeology` | Thematic grouping |
| **Phase** | `#draft`, `#review`, `#archived` | Workflow stage |
| **Concept** | `#ontology`, `#timeline`, `#LiDAR` | Conceptual linkage |
| **Process** | `#etl`, `#qa`, `#stac-validation` | Pipeline cross-references |

---

## 🗄️ Archiving & Filenames

- **When to archive:** After promotion or project phase end.  
- **Where:** `docs/notes/archive/<year>/`  
- **Pattern:** `YYYY-MM-DD_<kebab-title>.md`  
  Example → `2025-10-05_hydrology-dataset-crosswalk.md`

### Archival Log Example

```markdown
### Change Log
- 2025-10-17: Promoted to `/docs/architecture/hydrology.md`
- 2025-10-17: Archived original note (status: archived)
```

> Archiving maintains full traceability for every decision or draft.

---

## 🤖 AI Assistant & Automation

- **Summarization:** Each note can trigger summarization for AI dashboards.  
- **Embedding:** Notes auto-embed via `vector_index_notes.py` for semantic retrieval.  
- **Graph Sync:** Automated ingestion into Neo4j and Elastic/VectorDB nightly.  
- **Web Search:** Accessible via KFM web frontend search bar.

**Pipeline Summary**

```mermaid
flowchart TD
    A["note.md"] --> B["YAML Parser"]
    B --> C["Knowledge Graph (Neo4j/RDF)"]
    C --> D["Vector DB (Embeddings)"]
    D --> E["Web UI / API Search"]
```
<!-- END OF MERMAID -->

---

## ✅ Contributor Checklist

| ✅ Item | Description |
| :-- | :-- |
| [ ] Front-matter passes schema validation (`make docs-validate`) |
| [ ] Tags follow controlled vocabulary |
| [ ] Links to datasets, docs, or commits verified |
| [ ] Markdown style passes lint (`remark-lint`) |
| [ ] Added to `research.md` index or linked in related docs |
| [ ] Sensitive/PII-free content (open data only) |

---

## 🤖 CI Integration & Validation

| Validation | Tool | Description |
| :-- | :-- | :-- |
| **Front-matter check** | `yamllint` | Validates YAML structure. |
| **Schema validation** | `jsonschema` | Enforces metadata schema. |
| **Link integrity** | `remark-lint` | Detects broken/relative links. |
| **Tag parsing** | `scripts/parse_tags.py` | Updates SKOS vocabularies. |
| **Graph ingestion** | `scripts/graph_ingest_notes.py` | Loads notes into Neo4j RDF. |
| **Embedding** | `scripts/vector_index_notes.py` | Builds semantic embeddings. |

> Run locally before PR: `make docs-validate && make docs-lint`

---

## 📎 Related Documentation

| Path | Description |
| :-- | :-- |
| `docs/architecture/knowledge-graph.md` | How notes map into Neo4j/RDF. |
| `docs/templates/provenance.md` | Provenance & lineage capture. |
| `docs/standards/markdown_guide.md` | Markdown styling & components. |
| `docs/standards/markdown_rules.md` | Official MCP-DL v6.2 doc rules. |
| `docs/standards/documentation.md` | Writing & versioning standards. |
| `docs/standards/ontologies.md` | CIDOC-CRM · OWL-Time · SKOS alignment. |

---

## 🚀 Roadmap

| Milestone | Target | Description |
| :-- | :-- | :-- |
| v1.3 | Q1 2026 | Integrate vector search + AI summaries in web UI |
| v1.4 | Q2 2026 | Auto-generate STAC/graph sync nightly |
| v1.5 | Q3 2026 | Add web-based note creation + promotion workflow |

---

## 📅 Version History

| Version | Date | Author | Summary |
| :-- | :-- | :-- | :-- |
| v1.3 | 2025-10-17 | KFM Documentation Team | Added AI assist, schema validation, contributor checklist, roadmap. |
| v1.2 | 2025-10-16 | KFM Documentation Team | Updated tagging, ontology links, automation details. |
| v1.1 | 2025-10-05 | KFM Documentation Team | Added YAML schema, tag vocabularies, graph linkage, CI validation. |
| v1.0 | 2025-10-04 | KFM Documentation Team | Initial workspace for research and drafts. |

---

<div align="center">

**Kansas Frontier Matrix** — *“Ideas Recorded. Knowledge Preserved. Insight Proven.”*  
📍 [`docs/notes/README.md`](.) · Official MCP-compliant workspace for versioned notes and early research.

</div>
