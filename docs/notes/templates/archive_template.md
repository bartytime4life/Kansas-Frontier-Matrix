<div align="center">

# 🗃️ Kansas Frontier Matrix — **Archive Entry Template**  
`docs/notes/templates/archive_template.md`

**Purpose:** Provide a standardized format for archiving **superseded, merged, or finalized documentation** in the **Kansas Frontier Matrix (KFM)**.  
This template ensures every retired document remains **machine-readable, provenance-linked, and FAIR-compliant**, preserving its lineage under the **Master Coder Protocol – Documentation Language v6.3 (MCP-DL)**.

[![Docs · MCP-DL v6.3](https://img.shields.io/badge/Docs-MCP--DL%20v6.3-blue)](../../standards/documentation.md)
[![Docs Validated](https://img.shields.io/badge/docs-validated-brightgreen?logo=github)](../../../.github/workflows/docs-validate.yml)
[![Policy-as-Code](https://img.shields.io/badge/policy-OPA%2FConftest-purple)](../../../.github/workflows/policy-check.yml)
[![Knowledge Graph](https://img.shields.io/badge/Linked-Knowledge%20Graph-green)](../../architecture/knowledge-graph.md)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../../LICENSE)

</div>

```yaml
---
id: A-YYYY-NNN
title: "<Archived Note or Discussion Title>"
author: "@kfm-docs"
original_path: "docs/notes/<source>.md"
status: archived
archived_date: 2025-10-18
reason: superseded          # superseded | merged | complete | reference | duplicate
linked_successor:
  - ../../architecture/data-architecture.md
  - ../../standards/documentation.md
period_context:
  id: "perio.do/transition-2025"
  label: "MCP-DL Transition Period"
tags: ["archive","provenance","documentation","mcp","governance"]
fair_alignment:
  findable: true
  accessible: true
  interoperable: true
  reusable: true
ai_index:
  embed_in_graph: true
  model: "sentence-transformers/all-MiniLM-L6-v2"
  searchable_fields: ["title","summary","tags"]
access_policy:
  level: "public"          # public | internal
  license: "CC-BY 4.0"
  classification: "low"
summary: >
  A concise (1–3 sentence) summary of the document being archived,
  why it was superseded or retired, and how it connects to its successor(s).
---
```

---

## 🧭 Context

Briefly explain **why this note or document was archived**:
- What newer file replaced or merged it?
- Why was it important to preserve?
- How does it contribute to the project’s evolution and provenance?

> Example:  
> “This early design draft was archived following the publication of the MCP-DL v6.3 architecture document. It remains preserved for historical traceability and provenance verification.”

---

## 🧾 Archival Record

| Field | Value | Description |
| :-- | :-- | :-- |
| **Archived On** | 2025-10-18 | Date the document was formally archived |
| **Reason** | superseded | Cause for archival (superseded, merged, complete, duplicate) |
| **Successor(s)** | `docs/architecture/data-architecture.md` | File(s) that replace this entry |
| **Original Path** | `docs/notes/ideas.md` | Where this file originally lived |
| **Preservation Class** | permanent | As per retention policy |
| **License** | CC-BY 4.0 | Retained open-access terms |

---

## 🧩 Summary of Archived Content

Summarize the key insights or ideas retained in this archive.

- Capture the **major outcomes or rationale** behind the document.
- Explain **what has been inherited** by successor standards or workflows.
- Identify **why this record matters** for provenance or educational purposes.

> Example:  
> “The archived terrain pipeline prototype provided the foundational structure for KFM’s modern ETL and metadata validation processes.”

---

## 🧬 Provenance (RDF/Turtle)

```turtle
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix dc:   <http://purl.org/dc/terms/> .
@prefix kfm:  <https://kfm.org/id/> .

kfm:archive/A-2025-010
    a prov:Entity ;
    dc:title "Early Terrain Pipeline Draft — Superseded" ;
    prov:invalidatedAtTime "2025-10-18T00:00:00-06:00"^^xsd:dateTime ;
    prov:wasDerivedFrom kfm:document/ideas_terrain_pipeline ;
    prov:wasInfluencedBy kfm:document/data_architecture_v6_3 ;
    prov:wasAttributedTo kfm:agent/kfm-docs ;
    dc:description "Archived draft replaced by MCP-DL data architecture standards." .
```

---

## 🧠 FAIR & Digital Preservation Compliance

| Principle | Implementation |
| :-- | :-- |
| **Findable** | Indexed in yearly manifest & Knowledge Graph |
| **Accessible** | Archived in GitHub + mirrored to Zenodo |
| **Interoperable** | Mapped to PROV-O + CIDOC CRM |
| **Reusable** | Retains metadata, license, and context |

---

## 🧮 Governance Checklist

| Validation | Description | Status |
| :-- | :-- | :-- |
| YAML Metadata | Complete and validated via `yamllint` | ✅ |
| Successor Links | Resolved & verified by `remark-lint` | ✅ |
| FAIR Validation | Passes schema + accessibility tests | ✅ |
| Graph Ingestion | Synced via CI to Neo4j Knowledge Graph | ✅ |
| Checksum | Verified via `scripts/verify_checksums.py` | ✅ |
| License & Access | Correct CC-BY metadata present | ✅ |

---

## ⚙️ Preservation Metadata

```yaml
preservation:
  archived_date: "2025-10-18"
  checksum: "b9ac8d4f1a2c7e3..."
  bagit_package: "bags/kfm_archive_2025_bagit/"
  zenodo_doi: "10.5281/zenodo.1234789"
  last_verified: "2025-10-18"
```

---

## 🧩 Example FAIR Query

```sparql
SELECT ?note ?successor ?archivedDate
WHERE {
  ?note a prov:Entity ;
        prov:invalidatedAtTime ?archivedDate ;
        prov:wasInfluencedBy ?successor .
}
ORDER BY DESC(?archivedDate)
```

---

## 🧠 Educational Significance

Explain what this archive demonstrates historically or technically.

> Example:  
> “This document marks the completion of KFM’s pre-production design phase and the transition into automated MCP-DL governance.”

---

## 🧾 Related Templates

| Template | Purpose |
| :-- | :-- |
| [`meeting_template.md`](meeting_template.md) | For meeting summaries that lead to archival decisions |
| [`note_template.md`](note_template.md) | For general notes eventually archived here |
| [`backlog_template.md`](backlog_template.md) | For tasks that result in archival or migration actions |

---

## 📅 Version History

| Version | Date | Author | Summary |
| :-- | :-- | :-- | :-- |
| v1.0.0 | 2025-10-18 | @kfm-docs | Initial archive template with FAIR schema, RDF provenance, and BagIt/Zenodo metadata integration. |

---

<div align="center">

**Kansas Frontier Matrix** — *“Every Record Retained. Every Line Proven.”*  
📍 `docs/notes/templates/archive_template.md` · Maintained under MCP-DL v6.3 governance, FAIR principles, and preservation standards.

</div>
