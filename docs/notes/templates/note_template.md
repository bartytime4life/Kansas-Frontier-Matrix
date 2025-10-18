<div align="center">

# 🧩 Kansas Frontier Matrix — **General Note Template**  
`docs/notes/templates/note_template.md`

**Purpose:** Serve as the **base Markdown + YAML template** for documenting hypotheses, conceptual notes, design discussions, or narrative reflections.  
Each note created from this template is **MCP-DL v6.3–compliant**, validated through CI, and ingested into the **KFM Knowledge Graph** as a provenance-linked, FAIR-aligned entity.

[![Docs · MCP-DL v6.3](https://img.shields.io/badge/Docs-MCP--DL%20v6.3-blue)](../../standards/documentation.md)
[![Docs-Validate](https://img.shields.io/badge/docs-validated-brightgreen?logo=github)](../../../.github/workflows/docs-validate.yml)
[![Policy-as-Code](https://img.shields.io/badge/policy-OPA%2FConftest-purple)](../../../.github/workflows/policy-check.yml)
[![Knowledge Graph](https://img.shields.io/badge/Linked-Knowledge%20Graph-green)](../../architecture/knowledge-graph.md)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../../LICENSE)

</div>

```yaml
---
id: N-YYYY-NNN
title: "<Concise Note Title>"
author: "@kfm-docs"
date: 2025-10-18
status: draft                # draft | review | stable | archived
tags: ["note","concept","discussion","mcp"]
linked_docs:
  - ../../standards/documentation.md
linked_datasets:
  - ../../data/stac/example_dataset.json
linked_commits:
  - abc1234
linked_meetings:
  - ../../docs/notes/meetings.md#2025-10-18-governance-review
summary: >
  A short abstract (1–3 sentences) summarizing this note’s purpose and scope.
  Used for search, indexing, and AI embedding within the Knowledge Graph.
ai_assist:
  summarize: true
  embed_in_graph: true
  vector_model: "sentence-transformers/all-MiniLM-L6-v2"
period_context:
  id: "perio.do/mcp-note-development"
  label: "MCP-DL Documentation Development Phase"
license: "CC-BY 4.0"
---
```

---

## 🧭 Context

Provide a clear description of *why this note exists*, what problem or idea it addresses, and how it relates to the Kansas Frontier Matrix project.  
Mention if it builds upon previous notes, datasets, or architecture documents.

> Example:  
> “This note explores the integration of FAIR metadata validation logs into the data ingestion pipeline as part of MCP-DL governance alignment.”

---

## 🧩 Objective

Define the **intent** of this note:
- What do you want to document, test, or propose?
- What decisions or hypotheses does it explore?
- What follow-up actions or implications might it have?

> Example:
> “Establish a reproducible note structure template validated via CI and linked to the Knowledge Graph.”

---

## 🧠 Content / Discussion

Provide detailed notes, conceptual reasoning, technical observations, or references.  
Use bullet points or headings for clarity.

### Key Points
- List ideas, observations, or design insights.
- Include rationale for technical or methodological decisions.
- Note dependencies, risks, or unresolved questions.

### Example Code Block
```python
# Example code snippet for note reference
def check_fair_compliance(dataset):
    """Validate FAIR fields."""
    required = ["findable", "accessible", "interoperable", "reusable"]
    return all(field in dataset for field in required)
```

---

## 🔗 References & Related Work

| Type | Reference | Description |
| :-- | :-- | :-- |
| Dataset | `data/stac/example.json` | Example STAC dataset referenced in this note |
| Document | `docs/architecture/data-architecture.md` | Related system design document |
| Commit | `abc1234` | Git change introducing relevant functionality |
| Meeting | `M-2025-005` | Governance discussion linked to this note |

---

## 🧾 Provenance (RDF/Turtle)

```turtle
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix dc:   <http://purl.org/dc/terms/> .
@prefix kfm:  <https://kfm.org/id/> .

kfm:note/N-2025-001
    a prov:Entity ;
    dc:title "LiDAR Pipeline Integration Concept" ;
    prov:wasAttributedTo kfm:agent/kfm-data ;
    prov:wasDerivedFrom kfm:meeting/M-2025-005 ;
    prov:used kfm:dataset/usgs_3dep_dem_2020 ;
    dc:date "2025-10-18"^^xsd:date ;
    dc:description "Concept note on integrating LiDAR data into the ETL pipeline under MCP-DL governance." .
```

---

## ✅ Checklist Before Commit

| Validation | Requirement |
| :-- | :-- |
| ✅ YAML front-matter passes `yamllint` |
| ✅ Tags align with SKOS vocabularies |
| ✅ Links resolve and successors are valid |
| ✅ Schema validated via `note.schema.json` |
| ✅ No sensitive or restricted data included |
| ✅ Summary ≤ 3 sentences, plain English |

---

## 🧮 FAIR Alignment

| Principle | Implementation |
| :-- | :-- |
| **Findable** | Tagged with consistent identifiers; indexed by Neo4j |
| **Accessible** | Stored in Git + Zenodo archives |
| **Interoperable** | Uses PROV-O + CIDOC CRM mappings |
| **Reusable** | Licensed under CC-BY 4.0; schema compliant |

---

## 🤖 Validation Commands

Run the following locally before submitting:

```bash
make docs-validate
make docs-lint
pytest tools/tests/test_templates.py -k note
```

---

## 📎 Related Templates

| Template | Purpose |
| :-- | :-- |
| [`meeting_template.md`](meeting_template.md) | Use for meeting logs or decision records |
| [`research_template.md`](research_template.md) | Use for formal experiments or findings |
| [`archive_template.md`](archive_template.md) | Use for archiving superseded notes |

---

## 📜 Version History

| Version | Date | Author | Summary |
| :-- | :-- | :-- | :-- |
| v1.0.0 | 2025-10-18 | @kfm-docs | Initial note template with FAIR compliance, AI indexing metadata, and schema validation guidance. |

---

<div align="center">

**Kansas Frontier Matrix** — *“Every Note Structured. Every Thought Proven.”*  
📍 `docs/notes/templates/note_template.md` · Maintained under MCP-DL v6.3 documentation governance and CI validation.

</div>
