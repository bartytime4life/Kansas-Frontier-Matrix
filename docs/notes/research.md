<div align="center">

# 🔬 Kansas Frontier Matrix — Research Notes & Findings

`docs/notes/research.md`

**Purpose:** Serve as a **living research log** documenting ongoing discoveries, literature reviews,
and exploratory analyses supporting the **Kansas Frontier Matrix (KFM)** project —
ensuring that all intellectual work is transparent, reproducible, and linked to data provenance.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../)
[![Knowledge Graph](https://img.shields.io/badge/Linked-Knowledge%20Graph-green)](../../architecture/knowledge-graph.md)
[![Research Integrity](https://img.shields.io/badge/Research-Versioned-orange)](README.md)

</div>

---

## 🎯 Purpose

The `/docs/notes/research.md` file acts as the **central ledger of research and analysis**
within the Kansas Frontier Matrix. It captures hypotheses, literature summaries, field data integration,
and experimental notes before they are formalized into SOPs, datasets, or published documentation.

Research notes are:

* 🧠 **Contextualized** — every finding links to datasets, experiments, or publications.
* 🧾 **Reproducible** — YAML metadata ensures traceability to scripts and sources.
* 🧩 **Collaborative** — formatted for Git-based version control and peer contribution.
* 🔗 **Interoperable** — ingested into the Knowledge Graph as `prov:Entity` records.

---

## 🧱 File Structure

```text
docs/notes/research.md        ← Main log of current and past research
docs/notes/archive/research/  ← Archived or superseded entries (by year)
```

**Workflow:**

1. Capture findings in this document using the YAML + Markdown template below.
2. Cross-link to related experiments, datasets, and meetings.
3. After publication or promotion, move entries to `archive/research/`.
4. CI validation ensures links, metadata, and citations are consistent.

---

## 🧩 YAML Metadata Header (Required)

Each research entry begins with metadata for indexing and provenance tracking:

```yaml
---
id: research-2025-001
title: "Mapping Kansas Frontier Treaties — CIDOC CRM Application"
author: "Historical Data Integration Team"
date: 2025-10-05
status: draft             # draft | in-review | published | archived
category: "Data Modeling" # Archaeology | Ontology | Geospatial | Climate | NLP | AI
linked_commits:
  - 1f2acb8
linked_docs:
  - ../../standards/ontologies.md
  - ../../architecture/data-architecture.md
linked_datasets:
  - ../../data/stac/collections/treaties.json
linked_experiments:
  - ../../docs/experiments/treaty_alignment_experiment.md
tags: ["treaties", "ontology", "provenance", "CIDOC_CRM"]
summary: >
  Exploratory mapping of Kansas land cession treaties to CIDOC CRM event and place classes.
---
```

---

## 🧠 Research Entry Example

### 🔬 *Research-2025-001 — Mapping Kansas Frontier Treaties to CIDOC CRM*

**Category:** Ontology & Cultural Heritage
**Date:** 2025-10-05
**Author:** KFM Ontology Working Group
**Status:** 🧩 In Review
**Keywords:** `ontology`, `treaties`, `spatial data`, `provenance`, `CRM`

---

#### 🧭 Objective

To model **Kansas treaty data (1854–1870)** as `crm:E7_Activity` (treaty signing events)
and link to corresponding `crm:E53_Place` (cession areas) and `crm:E21_Person` (signatories).
This approach ensures semantic consistency with other cultural heritage datasets and allows
integration into the knowledge graph for querying treaty events geographically and temporally.

---

#### 📚 Background & Literature

* CIDOC CRM defines **events** (`E5_Event`) as core constructs linking actors, times, and places.
* PeriodO provides authoritative temporal boundaries for the **“Territorial Kansas Period” (1854–1861)**.
* Prior work: *Digital Atlas of Indian Land Cessions* (USFS, 2019) digitized Royce Maps with polygonal treaty areas.
* By representing each treaty as an event with spatial extent, the system can connect to:

  * Indigenous nation nodes (`crm:E74_Group`)
  * Affected regions (`geo:hasGeometry`)
  * Associated documents (`crm:E31_Document`).

---

#### ⚙️ Methods

1. **Data Acquisition:** Treaty text and cession boundaries from USFS and Kappler’s *Indian Affairs*.
2. **Parsing:** Extracted entities with spaCy NER (keywords: “Treaty”, “Tribe”, “Reservation”).
3. **Semantic Mapping:**

   * Event → `crm:E7_Activity` (Treaty signing)
   * Actor → `crm:E74_Group` (Tribal entity)
   * Place → `crm:E53_Place` (Cession boundary)
   * Document → `crm:E31_Document` (Primary source)
4. **Graph Integration:**

   * Ingested as Neo4j nodes with properties `{title, date, geometry, source}`.
   * Linked via `prov:wasDerivedFrom` (Kappler/USFS).

**Sample Cypher Query**

```cypher
MATCH (t:Event {type:'Treaty'})-[r:OCCURRED_AT]->(p:Place)
RETURN t.title, t.date, p.name, p.geometry;
```

---

#### 🧮 Findings

* Successfully mapped 37 treaty events with spatial polygons.
* Confidence threshold (NER + spatial join) achieved >92%.
* CIDOC CRM structure enabled alignment with historical maps (via `stac:collection`).
* Cross-links added to ontology schema in `docs/standards/ontologies.md`.

---

#### 🧩 Discussion

This model improves **semantic interoperability** by merging textual, spatial, and archival data.
Future work:

* Incorporate **OWL-Time intervals** for treaty enforcement periods.
* Extend model to post-treaty events (e.g., relocations, reservations).
* Test integration with PeriodO-defined temporal labels for user timeline filters.

---

#### 📜 References

1. CIDOC CRM Specification v7.1 (2023).
2. Kappler, *Indian Affairs: Laws and Treaties*, Vol. 2 (1904).
3. U.S. Forest Service, *Indian Land Cessions Map Digitization Project* (2019).
4. PeriodO Gazetteer, *Territorial Kansas Period* entry (2020).

---

#### 🧾 Provenance (RDF Example)

```turtle
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix crm:  <http://www.cidoc-crm.org/cidoc-crm/> .
@prefix kfm:  <https://kfm.org/id/> .

kfm:research/treaty_mapping_2025_001
    a prov:Entity, crm:E7_Activity ;
    prov:wasGeneratedBy kfm:process/treaty_mapping_etl ;
    prov:used kfm:dataset/treaties_usfs_2019 ;
    prov:wasAttributedTo kfm:agent/ontology_team ;
    prov:wasDerivedFrom <https://perio.do/territorial-kansas> ;
    prov:generatedAtTime "2025-10-05T10:00:00-06:00"^^xsd:dateTime .
```

---

## 📚 Current Research Log (2025)

| ID         | Date       | Title                               | Category   | Status       | Linked Docs          |
| :--------- | :--------- | :---------------------------------- | :--------- | :----------- | :------------------- |
| R-2025-001 | 2025-10-05 | Mapping Kansas Treaties — CIDOC CRM | Ontology   | 🧩 In Review | ontologies.md        |
| R-2025-002 | 2025-09-18 | NLP for Frontier Newspaper Corpus   | NLP / AI   | 🧠 Draft     | metadata.md          |
| R-2025-003 | 2025-08-25 | LiDAR Elevation Validation (1m DEM) | Geospatial | ✅ Published  | data-architecture.md |

---

## 🧠 CI Validation & Provenance Integration

| Validation              | Tool                               | Description                                              |
| :---------------------- | :--------------------------------- | :------------------------------------------------------- |
| **Front-matter Syntax** | `yamllint`                         | Validates metadata structure and required fields.        |
| **Link Verification**   | `remark-lint`                      | Confirms referenced documents/datasets exist.            |
| **Graph Sync**          | `scripts/graph_ingest_research.py` | Adds research entries as `prov:Entity` to Neo4j.         |
| **Tag Vocabulary**      | `scripts/parse_tags.py`            | Updates `data/vocabularies/tags.skos.ttl` for discovery. |

Run:

```bash
make docs-validate
```

---

## 🧩 Governance Rules

* Research notes require **at least one linked dataset** and **one related document**.
* Peer review (via PR) required for “published” status.
* All finalized research entries archived quarterly under `/docs/notes/archive/research/YYYY/`.
* RDF provenance auto-ingested into the Neo4j knowledge graph for discovery and reasoning.

---

## 🧠 MCP Compliance Summary

| MCP Principle           | Implementation                                                     |
| :---------------------- | :----------------------------------------------------------------- |
| **Documentation-first** | Each research entry records methods, sources, and findings.        |
| **Reproducibility**     | Metadata, scripts, and graph ingestion maintain full traceability. |
| **Open Standards**      | Uses YAML, RDF/PROV-O, CIDOC CRM, and STAC metadata.               |
| **Provenance**          | Every entry linked to datasets, commits, and entities.             |
| **Auditability**        | Logs validated by CI and stored in `data/work/logs/research/`.     |

---

## 📎 Related Documentation

| File                                     | Description                               |
| :--------------------------------------- | :---------------------------------------- |
| `docs/notes/README.md`                   | Notes workspace overview.                 |
| `docs/notes/templates/README.md`         | Templates for research and meeting notes. |
| `docs/standards/documentation.md`        | Writing and formatting standards.         |
| `docs/standards/ontologies.md`           | Ontology and semantic model reference.    |
| `docs/architecture/data-architecture.md` | Data ingestion and normalization schema.  |

---

## 📅 Version History

| Version | Date       | Author                       | Summary                                                                                      |
| :------ | :--------- | :--------------------------- | :------------------------------------------------------------------------------------------- |
| v1.0    | 2025-10-05 | KFM Research & Ontology Team | Initial release — standard format for research notes, with provenance and CIDOC CRM linkage. |

---

<div align="center">

**Kansas Frontier Matrix** — *“Every Hypothesis Logged. Every Discovery Proven.”*
📍 [`docs/notes/research.md`](.) · Official MCP-compliant research ledger for the Kansas Frontier Matrix.

</div>
