<div align="center">

# 🗓️ Kansas Frontier Matrix — **Meeting Notes Template**  
`docs/notes/templates/meeting_template.md`

**Purpose:** Provide a standardized structure for recording **meetings, governance sessions, sprint reviews, or design discussions** in the **Kansas Frontier Matrix (KFM)**.  
This template ensures every meeting record is **FAIR-compliant**, **MCP-DL v6.3 aligned**, and **automatically ingested** into the KFM **Knowledge Graph** as a `prov:Activity`.

[![Docs · MCP-DL v6.3](https://img.shields.io/badge/Docs-MCP--DL%20v6.3-blue)](../../standards/documentation.md)
[![Docs-Validate](https://img.shields.io/badge/docs-validated-brightgreen?logo=github)](../../../.github/workflows/docs-validate.yml)
[![Policy-as-Code](https://img.shields.io/badge/policy-OPA%2FConftest-purple)](../../../.github/workflows/policy-check.yml)
[![Knowledge Graph](https://img.shields.io/badge/Linked-Knowledge%20Graph-green)](../../architecture/knowledge-graph.md)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../../LICENSE)

</div>

```yaml
---
id: M-YYYY-NNN
title: "<Meeting Title>"
date: 2025-10-18
time: "09:00–10:30 America/Chicago"
type: governance              # governance | technical | design | sprint | research
status: finalized             # draft | in-review | finalized | archived
location: virtual             # or on-site location
facilitator: "@kfm-docs"
note_taker: "@kfm-data"
attendees:
  - "Andy Barta"
  - "@kfm-architecture"
  - "@kfm-research"
linked_commits:
  - a3f29e9
linked_prs:
  - https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/420
linked_docs:
  - ../../standards/documentation.md
  - ../../architecture/knowledge-graph.md
linked_backlog:
  - B-2025-002
linked_ideas:
  - I-2025-003
linked_datasets:
  - ../../data/stac/terrain/ks_1m_dem_2018_2020.json
summary: >
  A concise (2–3 sentence) description of the meeting’s purpose, topics, and outcomes.
  Used for FAIR indexing and AI embedding in the Knowledge Graph.
ai_assist:
  summarize: true
  embed_in_graph: true
  vector_model: "sentence-transformers/all-MiniLM-L6-v2"
license: "CC-BY 4.0"
---
```

---

## 🧭 Context

Summarize the meeting’s **purpose**, **agenda**, and **scope**.  
Explain what stage of project governance or research it relates to, and what overarching goals the team sought to accomplish.

> Example:  
> “This meeting reviewed the MCP-DL v6.3 documentation updates and finalized the ontology integration workflow for the Knowledge Graph.”

---

## 🧩 Agenda

List discussion points in chronological or logical order.

```markdown
1. Review current validation pipeline performance
2. Discuss AI vector search integration with Neo4j
3. Finalize MCP-DL documentation for 2025 release
4. Assign tasks for FAIR data revalidation
```

---

## 🧠 Discussion Summary

Capture the **main insights** or **decisions** made during the meeting.

- Documentation-first strategy reaffirmed for all new datasets  
- FAIR compliance check scheduled for November 2025  
- Decision: integrate STAC validator output with governance dashboards  
- Action item: create unified “notes-validate” CI job for schema + accessibility tests

---

## ⚙️ Decisions

| Decision | Rationale | Assigned To | Due |
| :-- | :-- | :-- | :-- |
| Integrate FAIR checker into workflow | Improve metadata consistency | @kfm-data | 2025-11-10 |
| Publish documentation under MCP-DL v6.3 | Align repository governance | @kfm-docs | 2025-10-25 |
| Prototype semantic vector search | Enable hybrid graph queries | @kfm-ai | 2025-12-01 |

---

## 🗂️ Action Items

| Action | Owner | Status | Notes |
| :-- | :-- | :-- | :-- |
| Validate new MCP-DL schema fields | @kfm-docs | ✅ Complete | Updated `docs/standards/documentation.md` |
| Run STAC validation tests | @kfm-data | 🔄 In Progress | Pending terrain dataset recheck |
| Publish ontology pipeline report | @kfm-ontology | 🗓️ Planned | For next governance meeting |

---

## 🧾 Provenance (RDF/Turtle)

```turtle
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix kfm:  <https://kfm.org/id/> .
@prefix dc:   <http://purl.org/dc/terms/> .

kfm:meeting/M-2025-010
    a prov:Activity ;
    dc:title "Ontology Governance Sync — October 2025" ;
    prov:wasAssociatedWith kfm:agent/kfm-governance ;
    prov:used kfm:document/documentation_standards_v6_3 ;
    prov:generated kfm:decision/ontology_alignment_approval ;
    prov:endedAtTime "2025-10-18T10:30:00-06:00"^^xsd:dateTime ;
    dc:description "Governance meeting finalizing ontology and metadata schema integration for KFM." .
```

---

## 📜 FAIR & MCP Compliance

| Principle | Implementation |
| :-- | :-- |
| **Findable** | Meeting indexed by `id` and timestamp |
| **Accessible** | Public via Git + Zenodo snapshot |
| **Interoperable** | Encoded using PROV-O + DCAT |
| **Reusable** | Licensed under CC-BY 4.0, schema-validated |

---

## ✅ Pre-Commit Checklist

| Validation | Requirement |
| :-- | :-- |
| ✅ YAML syntax valid (`yamllint`) |
| ✅ Required fields populated (ID, title, date, summary) |
| ✅ Linked items resolve to valid repo paths |
| ✅ Schema validated via `meeting.schema.json` |
| ✅ Summary ≤ 3 sentences, plain English |
| ✅ No restricted or private data present |

---

## 🤖 Validation Commands

```bash
make docs-validate
pytest tools/tests/test_templates.py -k meeting
```

---

## 📎 Related Templates

| Template | Purpose |
| :-- | :-- |
| [`note_template.md`](note_template.md) | Use for general documentation or hypotheses |
| [`backlog_template.md`](backlog_template.md) | Use for tracking resulting actions |
| [`archive_template.md`](archive_template.md) | Use when meeting series is deprecated or merged |

---

## 📅 Version History

| Version | Date | Author | Summary |
| :-- | :-- | :-- | :-- |
| v1.0.0 | 2025-10-18 | @kfm-docs | Initial meeting template with YAML schema, FAIR compliance, RDF provenance, and CI validation integration. |

---

<div align="center">

**Kansas Frontier Matrix** — *“Every Discussion Recorded. Every Decision Proven.”*  
📍 `docs/notes/templates/meeting_template.md` · Maintained under MCP-DL v6.3 governance and CI compliance standards.

</div>
