<div align="center">

# 🗓️ Kansas Frontier Matrix — Meeting Records & Collaboration Log

`docs/notes/meetings.md`

**Purpose:** Maintain an official, versioned record of **meetings, decisions, and action items**
related to the **Kansas Frontier Matrix (KFM)** project — ensuring transparent governance,
traceable provenance, and reproducible documentation under **Master Coder Protocol (MCP)** standards.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../)
[![Governance](https://img.shields.io/badge/Governance-Structured-purple)](../../standards/documentation.md)
[![Knowledge Graph](https://img.shields.io/badge/Linked-Knowledge%20Graph-green)](../../architecture/knowledge-graph.md)

</div>

---

## 🎯 Purpose

This file serves as the **official, living record** of KFM coordination meetings, design discussions,
and sprint reviews. Each entry documents **who met**, **what decisions were made**, **why changes occurred**,
and **how those decisions connect** to datasets, code modules, or architectural components.

Meeting logs are:

* 🧾 **Versioned** — every update is Git-tracked.
* 🔗 **Linked** — cross-referenced with commits, datasets, and documents.
* 🧠 **Searchable** — structured YAML headers allow automatic indexing into the Knowledge Graph.
* ✅ **Auditable** — validated by CI workflows (`make docs-validate`).

---

## 🧱 Structure & Workflow

```text
docs/notes/meetings.md        ← Central index of all meeting entries (this file)
docs/notes/archive/meetings/  ← Archived meeting logs (auto-moved quarterly)
```

**Workflow Overview**

1. Record each meeting using the template below.
2. Include YAML metadata and date/time in ISO 8601 format.
3. Cross-link related backlog or ideas entries (IDs like `B-2025-003`, `I-2025-002`).
4. After 3 months, move older meetings to `/archive/meetings/` and retain index links.
5. CI validates metadata structure and cross-links.

---

## 🧩 YAML Metadata Header

Each meeting record starts with a **front-matter block**:

```yaml
---
id: meeting-2025-10-05
title: "Q4 Planning & Ontology Integration Review"
date: 2025-10-05
time: "09:00-10:30 CST"
type: governance           # governance | sprint | technical | review | outreach
location: virtual          # physical | virtual | hybrid
attendees:
  - Andy Barta
  - Data Integration Team
  - KFM Ontology Working Group
linked_commits:
  - a3f29e9
linked_docs:
  - ../../standards/ontologies.md
  - ../../architecture/knowledge-graph.md
linked_backlog:
  - B-2025-004
linked_ideas:
  - I-2025-001
status: finalized          # draft | finalized | archived
tags: ["ontology", "timeline", "ETL", "MCP"]
summary: >
  Discussed integration of OWL-Time + CIDOC CRM with Neo4j schema; assigned data tasks.
---
```

---

## 🗓️ Example Meeting Entry

### 🧩 Meeting — Q4 Planning & Ontology Integration Review

*Date:* 2025-10-05
*Time:* 09:00–10:30 CST
*Location:* Virtual
*Type:* Governance & Technical
*Attendees:* Andy Barta, Data Engineering Team, Ontology Group

---

#### 🧭 Agenda

1. Align ontology (CIDOC CRM + OWL-Time) with Neo4j schema.
2. Review AI/ML enrichment pipeline progress.
3. Validate historical period mappings with PeriodO dataset.
4. Assign documentation upgrades (`docs/standards/ontologies.md`).

---

#### 🧠 Discussion Summary

* Adopted **CIDOC CRM E5_Event** and **E53_Place** classes as core graph nodes.
* Decided on **OWL-Time intervals** for temporal reasoning in API queries.
* Confirmed cross-linking of event timelines to **PeriodO JSON-LD** references.
* Planned integration of **AI-extracted events** from historical texts into Neo4j with
  confidence scores for curator review.
* Approved continuous ingestion schedule for NOAA and USGS datasets.

---

#### ⚙️ Decisions

| Decision                                              | Rationale                | Assigned To    | Due        |
| :---------------------------------------------------- | :----------------------- | :------------- | :--------- |
| Integrate OWL-Time schema in graph backend            | Align with W3C standards | @ontology-team | 2025-10-20 |
| Add validation step to ETL (`make validate-ontology`) | Prevent schema drift     | @data-team     | 2025-10-25 |
| Draft README for ontology layer                       | Documentation-first rule | @docs-team     | 2025-10-30 |

---

#### 📋 Action Items

* [x] Update ontology graph schema documentation (`docs/standards/ontologies.md`)
* [ ] Add STAC schema links to each event entity in data/stac/
* [ ] Merge CI validation for OWL-Time into `.github/workflows/site.yml`
* [ ] Publish follow-up meeting report to archive after 30 days

---

#### 🧩 Linked Materials

* Related Documents: `docs/standards/ontologies.md`, `docs/architecture/knowledge-graph.md`
* Related Backlog: `docs/notes/backlog.md` → Item `B-2025-004`
* Related Ideas: `docs/notes/ideas.md` → Item `I-2025-001`

---

#### 🧮 Provenance Entry (RDF Triple Example)

```turtle
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix kfm: <https://kfm.org/id/> .
@prefix dc: <http://purl.org/dc/terms/> .

kfm:meeting/2025_10_05
    a prov:Activity ;
    dc:title "Q4 Planning & Ontology Integration Review" ;
    prov:wasAssociatedWith kfm:agent/ontology_team ;
    prov:generated kfm:document/ontologies_v2_spec ;
    prov:atTime "2025-10-05T09:00:00-06:00"^^xsd:dateTime ;
    prov:used kfm:document/knowledge_graph_architecture ;
    dc:description "Adopted CIDOC CRM and OWL-Time schema updates." .
```

---

## 📊 Meeting Log Index (2025)

| ID         | Date       | Title                              | Type       | Status      | Linked Docs            |
| :--------- | :--------- | :--------------------------------- | :--------- | :---------- | :--------------------- |
| M-2025-001 | 2025-10-05 | Q4 Planning & Ontology Integration | Governance | ✅ Finalized | Ontologies.md          |
| M-2025-002 | 2025-09-20 | Web UI Architecture Sync           | Technical  | ✅ Finalized | Web UI Docs            |
| M-2025-003 | 2025-08-15 | Historical Dataset Integration     | Sprint     | 🟡 Draft    | Data Integration Guide |

---

## 🧰 CI Validation Hooks

| Validation            | Tool                               | Description                                                  |
| :-------------------- | :--------------------------------- | :----------------------------------------------------------- |
| **YAML Header Check** | `yamllint`                         | Ensures all required fields exist (id, title, date, status). |
| **Link Validation**   | `remark-lint`                      | Checks linked documents and backlog IDs are resolvable.      |
| **Graph Sync**        | `scripts/graph_ingest_meetings.py` | Ingests meetings as `prov:Activity` into Neo4j.              |
| **Tag Consistency**   | `scripts/parse_tags.py`            | Updates SKOS vocab for semantic search.                      |

Run locally:

```bash
make docs-validate
```

---

## 🧠 MCP Compliance Summary

| MCP Principle           | Implementation                                                         |
| :---------------------- | :--------------------------------------------------------------------- |
| **Documentation-first** | All meeting outcomes recorded and versioned here.                      |
| **Reproducibility**     | YAML metadata ensures machine-parsable history.                        |
| **Open Standards**      | RDF/PROV-O integration for knowledge graph ingestion.                  |
| **Provenance**          | Each decision linked to commits, docs, and datasets.                   |
| **Auditability**        | Quarterly reviews archive finalized meetings for traceable governance. |

---

## 📎 Related Documentation

| File                                   | Description                                |
| :------------------------------------- | :----------------------------------------- |
| `docs/notes/README.md`                 | Notes workspace overview.                  |
| `docs/notes/templates/README.md`       | Templates for notes and meetings.          |
| `docs/standards/documentation.md`      | Documentation and writing standards.       |
| `docs/architecture/knowledge-graph.md` | Graph and ontology architecture reference. |

---

## 📅 Version History

| Version | Date       | Author                              | Summary                                                                                           |
| :------ | :--------- | :---------------------------------- | :------------------------------------------------------------------------------------------------ |
| v1.0    | 2025-10-05 | KFM Documentation & Governance Team | Initial release — formalized meeting log structure with YAML metadata and RDF provenance support. |

---

<div align="center">

**Kansas Frontier Matrix** — *“Every Decision Recorded. Every Conversation Proven.”*
📍 [`docs/notes/meetings.md`](.) · Official MCP-compliant meeting log for the Kansas Frontier Matrix.

</div>
