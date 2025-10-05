<div align="center">

# 💡 Kansas Frontier Matrix — Ideas & Concepts

`docs/notes/ideas.md`

**Purpose:** Provide a structured, version-controlled space for **brainstorming, experiments, and exploratory hypotheses**
within the **Kansas Frontier Matrix (KFM)** — ensuring that creative thinking remains **documented, searchable, and linked**
to datasets, discussions, and future design documents.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../)
[![Knowledge Graph](https://img.shields.io/badge/Linked-Knowledge%20Graph-green)](../../architecture/knowledge-graph.md)
[![Versioned Ideas](https://img.shields.io/badge/Ideas-Versioned-orange)](README.md)

</div>

---

## 🎯 Purpose

The `/docs/notes/ideas.md` document captures **the earliest stages of innovation** —
rough concepts, potential features, data models, or integrations — before they are formalized.

Ideas are:

* 🧠 **Open-ended** — encourage creativity, exploration, and hypothesis testing.
* 🔗 **Interconnected** — linked to datasets, code, and meetings for context.
* 🧾 **Traceable** — each idea includes metadata, tags, and linked provenance.
* 🧩 **Promotable** — once reproducible, ideas graduate into `/docs/design/` or `/docs/architecture/`.

---

## 🧱 Structure

```text
docs/notes/ideas.md
├── Active Ideas         # Draft or in review
├── In Review            # Under discussion or testing
├── Promoted             # Accepted → Design/Architecture
└── Archived             # Declined or deprecated concepts
```

Each idea block should follow the **YAML metadata + Markdown body** format below.

---

## 🧩 YAML Metadata Schema

```yaml
---
id: idea-2025-001
title: "Integrating PeriodO Historical Periods into Timeline Slider"
author: "Ontology Team"
status: draft            # draft | review | promoted | archived
priority: medium         # high | medium | low
date_created: 2025-10-05
last_updated: 2025-10-05
tags: ["timeline","ontology","PeriodO"]
linked_commits:
  - 9a4bced
linked_docs:
  - ../../standards/ontologies.md
linked_datasets:
  - ../../data/stac/events/periodo_era_catalog.json
linked_meetings:
  - meetings.md#2025-10-05-ontology-sync
---
```

---

## 💭 Active Ideas

### 💡 *Idea 001 — Integrating PeriodO Historical Periods into Timeline Slider*

**Goal:**
Enhance the KFM web UI’s timeline with dynamic historical period data from the [PeriodO dataset](https://perio.do/).

**Motivation:**
Users should be able to explore Kansas events relative to recognized scholarly periods (“Territorial Kansas,” “Dust Bowl,” etc.)
for context-aware storytelling and data correlation.

**Approach:**

* Pull the PeriodO JSON-LD API (`https://perio.do/api/periods/`) nightly.
* Parse and map periods to internal KFM time ontology (`OWL-Time` + `mcp:timeNote`).
* Add a toggle in the MapLibre timeline slider for “Historical Context Layers.”

**Dependencies:**

* `docs/standards/ontologies.md`
* `docs/architecture/web-ui-architecture.md`

**Next Steps:**

* [ ] Validate integration feasibility (mock data).
* [ ] Draft STAC schema extension for `periodo:` fields.
* [ ] Design UI toggle and tooltip layout.

---

### 💡 *Idea 002 — Automated Provenance Graph Visualizer*

**Goal:**
Generate live, interactive diagrams (Mermaid or Neo4j Bloom) for provenance tracking.

**Description:**

* Use `prov:` and `mcp:` relationships to auto-generate dynamic data flow diagrams from graph exports.
* Integrate output into documentation builds (`make site`).

**Potential Tools:**

* `rdflib`, `py2neo`, or `graphviz`.
* Custom Jinja2 + Mermaid templates.

**Linked Docs:**

* `docs/architecture/knowledge-graph.md`
* `docs/standards/ontologies.md`

**Status:** draft
**Owner:** @graph-engineering-team

---

### 💡 *Idea 003 — AI-Powered STAC Metadata Reviewer*

**Concept:**
Use an AI-assisted validation service to detect missing fields or inconsistencies in STAC metadata files.

**Implementation Thoughts:**

* Fine-tune an LLM on valid STAC examples from `data/stac/**`.
* Integrate as a GitHub Action comment bot that suggests corrections.
* Output recommendations as `stac_ai_review_<item>.json` under `data/work/logs/qa/`.

**Challenges:**

* Avoid hallucination — strict schema enforcement via `jsonschema`.
* Data privacy when processing metadata externally.

**Linked Docs:**

* `docs/standards/metadata.md`
* `.github/workflows/stac-validate.yml`

---

## 🧭 In Review

| ID           | Title                       | Reviewer    | Status    |
| :----------- | :-------------------------- | :---------- | :-------- |
| `I-2025-002` | Provenance Graph Visualizer | @graph-team | 🟡 review |
| `I-2025-003` | AI STAC Reviewer            | @data-team  | 🟡 review |

---

## 🚀 Promoted Ideas

| ID           | Title               | Promoted To                                    | Date       | Reviewer       |
| :----------- | :------------------ | :--------------------------------------------- | :--------- | :------------- |
| `I-2025-001` | PeriodO Integration | [ontologies.md](../../standards/ontologies.md) | 2025-10-05 | @ontology-lead |

---

## 🗃️ Archived Ideas

| ID           | Title                            | Reason                             | Archived Date |
| :----------- | :------------------------------- | :--------------------------------- | :------------ |
| `I-2024-004` | Historical DEM Resampling Method | Superseded by new terrain pipeline | 2025-03-10    |

---

## 🔗 Linking Ideas to the Knowledge Graph

Each idea is ingested as a **`prov:Plan`** entity in the KFM Knowledge Graph.

**Example RDF:**

```turtle
@prefix kfm: <https://kfm.org/id/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix dc: <http://purl.org/dc/terms/> .

kfm:idea/periodo_integration
    a prov:Plan ;
    dc:title "Integrating PeriodO Historical Periods into Timeline Slider" ;
    prov:wasAttributedTo kfm:agent/ontology_team ;
    prov:wasDerivedFrom kfm:dataset/periodo_era_catalog ;
    prov:generated kfm:feature/timeline_period_overlay ;
    dc:date "2025-10-05"^^xsd:date .
```

> Ideas evolve into `prov:Activity` entities when work begins,
> and ultimately `prov:Entity` when implemented as a real artifact.

---

## 🧠 CI Validation Hooks

| Validation            | Tool                            | Description                               |
| :-------------------- | :------------------------------ | :---------------------------------------- |
| **Front-matter YAML** | `yamllint`                      | Ensures valid metadata fields             |
| **Link Validation**   | `remark-lint`                   | Confirms internal paths resolve           |
| **Tag Parser**        | `scripts/parse_tags.py`         | Updates SKOS vocabularies for idea topics |
| **Graph Sync**        | `scripts/graph_ingest_ideas.py` | Inserts ideas into Neo4j graph            |

Run locally:

```bash
make docs-validate
```

---

## 🧩 Governance & Review Policy

* All new ideas require **peer review** or discussion in `meetings.md`.
* Accepted ideas get a `status: promoted` and are copied into relevant directories.
* Deprecated or declined ideas are archived (`status: archived`) and tagged accordingly.
* The Documentation Lead reviews this file during each sprint planning cycle.

---

## 🧠 MCP Compliance Summary

| MCP Principle           | Implementation                                                  |
| :---------------------- | :-------------------------------------------------------------- |
| **Documentation-first** | Ideas documented and versioned before implementation.           |
| **Reproducibility**     | Metadata and provenance ensure concept traceability.            |
| **Open Standards**      | Uses YAML, Markdown, and PROV-O for interoperability.           |
| **Provenance**          | Every idea maps to a `prov:Plan` entity in the knowledge graph. |
| **Auditability**        | Reviewed and logged through Git commits and CI validation.      |

---

## 📎 Related Documentation

| File                                   | Description                       |
| :------------------------------------- | :-------------------------------- |
| `docs/notes/README.md`                 | Overview of the notes workspace.  |
| `docs/notes/templates/README.md`       | Note & backlog templates.         |
| `docs/architecture/knowledge-graph.md` | Semantic mapping for ideas.       |
| `docs/standards/documentation.md`      | Writing standards and governance. |

---

## 📅 Version History

| Version | Date       | Author                 | Summary                                                                                       |
| :------ | :--------- | :--------------------- | :-------------------------------------------------------------------------------------------- |
| v1.0    | 2025-10-05 | KFM Documentation Team | Initial version of ideas log with YAML metadata, provenance linkage, and governance workflow. |

---

<div align="center">

**Kansas Frontier Matrix** — *“Every Idea Captured. Every Insight Proven.”*
📍 [`docs/notes/ideas.md`](.) · Official MCP-compliant idea log for Kansas Frontier Matrix.

</div>
