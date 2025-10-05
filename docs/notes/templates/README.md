<div align="center">

# 🧩 Kansas Frontier Matrix — Notes Templates

`docs/notes/templates/README.md`

**Purpose:** Provide reusable **Markdown + YAML templates** for research notes,
meeting summaries, brainstorming ideas, and backlog entries — ensuring all informal
work within `/docs/notes/` remains **structured, searchable, and MCP-compliant**.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../)
[![Knowledge Graph](https://img.shields.io/badge/Linked-Knowledge%20Graph-green)](../../architecture/knowledge-graph.md)
[![Template Validated](https://img.shields.io/badge/Templates-Validated-orange)](README.md)

</div>

---

## 📚 Overview

This directory contains **ready-to-use templates** for note types used in
the Kansas Frontier Matrix documentation ecosystem.

Templates provide:

* 🧱 **Consistent structure** across informal documents
* 🧾 **Metadata front-matter** for traceability & graph integration
* 🧩 **Tags and links** for discovery and provenance tracking
* 🔗 **Cross-linking** to datasets, commits, and formal docs

All templates adhere to the **Master Coder Protocol (MCP)**
and are automatically validated by CI for completeness and YAML syntax.

---

## 🗂️ Directory Layout

```text
docs/notes/templates/
├── README.md                  # (this file)
├── note_template.md            # Generic research or idea note
├── meeting_template.md         # Meeting & decision log template
├── backlog_template.md         # To-do or technical debt tracking
├── research_template.md        # Research summary template
└── archive_template.md         # Legacy or closed note archival format
```

---

## 🧱 Template Structure

All templates share a **YAML front-matter block** followed by Markdown content.

```yaml
---
title: "Short Descriptive Title"
author: "Your Name or Team"
date: 2025-10-05
status: draft            # draft | review | stable | archived
tags: ["idea", "dataset", "discussion"]
linked_datasets:
  - data/stac/terrain/ks_1m_dem_2018_2020.json
linked_commits:
  - f3a91b2
linked_docs:
  - ../../architecture/data-architecture.md
---
```

**Front-matter rules**

| Field      | Description                          | Example                                 |
| :--------- | :----------------------------------- | :-------------------------------------- |
| `title`    | Concise human-readable summary       | “LiDAR Pipeline Hypothesis”             |
| `author`   | Note owner(s) or team                | “Data Integration Team”                 |
| `status`   | Note lifecycle                       | `draft`, `review`, `stable`, `archived` |
| `tags`     | Searchable keywords / ontology links | `["hydrology","qa","ETL"]`              |
| `linked_*` | Permalinks to related entities       | Datasets, commits, docs                 |
| `date`     | ISO 8601                             | `2025-10-05`                            |

---

## 📄 Available Templates

### 1️⃣ `note_template.md`

Use for general notes, hypotheses, or concept development.

```markdown
# 💡 [Note Title]
*Date:* YYYY-MM-DD  
*Author:* [Your Name]  
*Status:* draft  

## Context
Brief summary of how this idea or issue arose.

## Hypothesis / Insight
What is being tested, designed, or discussed?

## Linked Data & References
- Dataset: `data/stac/...`
- Document: `docs/...`
- Commit: `<hash>`

## Next Steps
1. …
2. …

## Change Log
| Date | Author | Summary |
|:--|:--|:--|
| YYYY-MM-DD | You | Created note |
```

---

### 2️⃣ `meeting_template.md`

Used to record **discussions, decisions, and action items**.

```markdown
# 🗓️ Meeting — [Topic or Sprint Name]
*Date:* YYYY-MM-DD  
*Participants:* Alice, Bob, Carol  

## Agenda
1. …

## Notes
- …

## Decisions
- ✅ Adopt new data schema for hydrology.
- 🕒 Follow up on DEM tile gaps.

## Action Items
- [ ] Alice — Update metadata template.
- [ ] Bob — Verify pipeline output.
```

---

### 3️⃣ `research_template.md`

Used to capture **research summaries, references, or literature reviews**.

```markdown
# 🧠 Research Summary — [Topic]
*Date:* YYYY-MM-DD  
*Author:* [Your Name]  

## Objective
Describe the goal or research question.

## Key Findings
- …

## References
1. Source citation
2. DOI or dataset link

## Integration Notes
How can this be merged into KFM’s data or knowledge graph?
```

---

### 4️⃣ `backlog_template.md`

For **technical debt, pending work, or roadmap tasks**.

```markdown
# 🧩 Backlog Entry — [Task]
*Created:* YYYY-MM-DD  
*Owner:* [Team or Person]  
*Priority:* High | Medium | Low  
*Status:* open  

## Description
Briefly describe the issue or need.

## Related Issues / Notes
- GitHub Issue #123
- `docs/notes/ideas.md`

## Dependencies
- STAC metadata updates  
- ETL script changes

## Acceptance Criteria
- [ ] Validation passes  
- [ ] Checksum verified  
- [ ] Documentation updated
```

---

### 5️⃣ `archive_template.md`

For **closing or retiring notes** while maintaining provenance.

```markdown
# 🗃️ Archived Note — [Original Title]
*Archived:* YYYY-MM-DD  
*Reason:* superseded | duplicate | merged | complete  
*Original Path:* docs/notes/[filename].md  

## Summary
What this note covered and why it was archived.

## Linked Successor
- Promoted to: `docs/architecture/...`  
- Superseded by: `docs/notes/...`
```

---

## 🔍 Linking to the Knowledge Graph

Every note template supports metadata ingestion into the KFM Knowledge Graph.
On commit, CI parses YAML headers and generates triples such as:

```turtle
kfm:note/meeting_oct05 a prov:Entity ;
    dc:title "October Sprint Meeting" ;
    prov:wasGeneratedBy kfm:process/team_meeting_2025_10 ;
    prov:wasAttributedTo kfm:agent/kfm_team ;
    dc:date "2025-10-05"^^xsd:date .
```

---

## 🧩 Validation & CI Integration

| Validation   | Tool                            | Purpose                         |
| :----------- | :------------------------------ | :------------------------------ |
| YAML syntax  | `yamllint`                      | Ensures valid front-matter      |
| Link check   | `remark-lint`                   | Verifies relative links         |
| Tag parsing  | `scripts/parse_tags.py`         | Updates SKOS vocab for search   |
| Graph ingest | `scripts/graph_ingest_notes.py` | Adds notes to Neo4j / RDF graph |

Run manually:

```bash
make docs-validate
```

---

## 🧠 MCP Compliance Summary

| MCP Principle           | Implementation                                             |
| :---------------------- | :--------------------------------------------------------- |
| **Documentation-first** | Templates provided for all informal writing.               |
| **Reproducibility**     | Front-matter enables deterministic metadata ingestion.     |
| **Open Standards**      | YAML, Markdown, RDF, SKOS for semantic linkage.            |
| **Provenance**          | Notes are versioned + ingested into the knowledge graph.   |
| **Auditability**        | CI validation ensures every note meets metadata standards. |

---

## 📎 Related Documentation

| File                              | Description                                 |
| :-------------------------------- | :------------------------------------------ |
| `docs/notes/README.md`            | Overview of the notes workspace.            |
| `docs/standards/documentation.md` | Writing & formatting standards.             |
| `docs/standards/ontologies.md`    | Semantic vocabularies used in note linkage. |
| `docs/templates/provenance.md`    | Provenance record format.                   |

---

## 📅 Version History

| Version | Date       | Author                 | Summary                                                                            |
| :------ | :--------- | :--------------------- | :--------------------------------------------------------------------------------- |
| v1.0    | 2025-10-05 | KFM Documentation Team | Initial release of note templates with YAML metadata, linking, and CI integration. |

---

<div align="center">

**Kansas Frontier Matrix** — *“Every Idea Structured. Every Note Traceable.”*
📍 [`docs/notes/templates/README.md`](.) · Official MCP-compliant templates for the Notes subsystem.

</div>
