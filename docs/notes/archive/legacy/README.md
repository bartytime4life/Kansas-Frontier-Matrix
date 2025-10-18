<div align="center">

# 🕰️ Kansas Frontier Matrix — **Legacy Notes Archive**  
`docs/notes/archive/legacy/README.md`

**Purpose:** Curate and preserve **pre-MCP and early prototype documentation** from the formative years of the **Kansas Frontier Matrix (KFM)** project — ensuring that legacy research, scripts, and design discussions remain accessible and historically contextualized, even if superseded by modern MCP-DL v6.3 governance.

This directory serves as the **historical vault** of the KFM system — documenting the project’s evolution from fragmented, pre-standardized efforts to today’s unified, reproducible knowledge ecosystem.

[![Docs · MCP-DL v6.3](https://img.shields.io/badge/Docs-MCP--DL%20v6.3-blue)](../../../standards/documentation.md)
[![Knowledge Graph](https://img.shields.io/badge/Linked-Knowledge%20Graph-green)](../../../architecture/knowledge-graph.md)
[![Archive Integrity](https://img.shields.io/badge/Archive-Legacy-orange)](../README.md)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../../../LICENSE)

</div>

```yaml
---
title: "Kansas Frontier Matrix — Legacy Notes Archive"
document_type: "Legacy Archive"
version: "v1.0.0"
last_updated: "2025-10-18"
created: "2023-01-01"
owners: ["@kfm-docs","@kfm-architecture","@kfm-governance"]
status: "Stable"
scope: "Docs/Notes/Archive/Legacy"
license: "CC-BY 4.0"
tags: ["legacy","archive","pre-MCP","history","provenance","governance"]
audit_framework: "MCP-DL v6.3"
semantic_alignment:
  - PROV-O
  - CIDOC CRM
  - OWL-Time
  - SKOS
  - JSON Schema
  - ISO 8601
  - DCAT 2.0
preservation_policy:
  format_standards: ["Markdown (GFM)","RDF/Turtle"]
  checksum_algorithm: "SHA-256"
  replication_targets: ["GitHub Repository","Local Cold Storage"]
  metadata_standard: "PREMIS 3.0"
  revalidation_cycle: "biennial"
retention_policy:
  archive_after: "immediate"
  purge_after: "never"
fair_alignment:
  findable: true
  accessible: true
  interoperable: true
  reusable: true
access_policy:
  level: "public"
  license: "CC-BY 4.0"
  classification: "low"
period_context:
  id: "perio.do/kfm-pre-standardization-2017-2023"
  label: "Pre-MCP & Early Development Era"
---
```

---

## 📚 Overview

The **Legacy Archive** contains **all pre-MCP and early developmental documents** from the Kansas Frontier Matrix project (2017–2023).  
These records include concept drafts, early GIS integrations, and exploratory data workflows written before the project’s unification under the **Master Coder Protocol (MCP)**.

While not conforming to modern schemas or FAIR principles at creation, these files are preserved for:

* 🧠 **Historical traceability** — capturing the origins of MCP concepts.  
* 🧾 **Provenance linking** — referencing early datasets, ETL prototypes, and GIS experiments.  
* 🔗 **Continuity** — enabling modern documentation to reference original design lineage.  
* 🧱 **Education** — providing insight into how the MCP standard evolved.

---

## 🗂️ Directory Layout

```text
docs/notes/archive/legacy/
├── README.md                                # (this file)
├── 2018_terrain_etl_prototype_notes.md      # Pre-MCP ETL concept
├── 2019_data_ingest_strategy.md             # Early ingestion workflows
├── 2020_archaeological_map_sketches.md      # Field & cartography records
├── 2021_digital_atlas_proposal.md           # Early plan for unified repository
├── 2022_mcp_draft_notes.md                  # First MCP conceptual draft
└── 2023_architecture_briefing_v0.md         # Prototype system diagram
```

---

## 🧩 Legacy Document Classification

| File | Year | Domain | Status | Legacy Type | Successor |
| :-- | :-- | :-- | :-- | :-- | :-- |
| `2018_terrain_etl_prototype_notes.md` | 2018 | Geospatial | archived | Prototype | `data/processed/terrain/README.md` |
| `2019_data_ingest_strategy.md` | 2019 | Data Engineering | archived | Draft | `architecture/data-architecture.md` |
| `2020_archaeological_map_sketches.md` | 2020 | Archaeology | archived | Field Record | `standards/ontologies.md` |
| `2021_digital_atlas_proposal.md` | 2021 | Cartography | archived | Proposal | `architecture/knowledge-graph.md` |
| `2022_mcp_draft_notes.md` | 2022 | Governance | archived | Draft | `standards/documentation.md` |
| `2023_architecture_briefing_v0.md` | 2023 | Systems Design | archived | Concept Brief | `architecture/data-architecture.md` |

---

## 🧾 Example Legacy Metadata

```yaml
---
title: "Digital Atlas Proposal — Pre-MCP Draft"
author: "Frontier Cartography Team"
original_path: "notes/proposals/atlas_plan.md"
status: archived
archived_date: 2021-03-12
reason: legacy
linked_successor:
  - ../../../architecture/knowledge-graph.md
tags: ["legacy","proposal","cartography","atlas","archive"]
---
```

---

## 🧠 Historical Context (2017–2023)

### 📖 Evolution Overview
1. **2017–2018:** Fragmented GIS and archival datasets managed independently.  
2. **2019:** First prototypes for automated ETL and checksum verification (using shell scripts).  
3. **2020:** Archaeological mapping introduced — earliest multi-domain integration test.  
4. **2021:** “Digital Atlas” proposal envisioned a unified time–space system for Kansas history.  
5. **2022:** “Master Coder Protocol” first appears as an internal governance framework.  
6. **2023:** Initial architecture brief introduces modular repo and knowledge graph integration.

---

## 🧩 Provenance Graph Overview

```mermaid
flowchart TD
    A["2018 Terrain ETL Prototype"] --> B["2019 Data Ingest Strategy"]
    B --> C["2021 Digital Atlas Proposal"]
    C --> D["2022 MCP Draft Notes"]
    D --> E["2023 Architecture Briefing v0"]
    E --> F["2024 Initial Design Discussion (Archived)"]
    F --> G["2025 Operational Governance (MCP-DL v6.3)"]
```
<!-- END OF MERMAID -->

---

## 🧮 FAIR & Digital Preservation Compliance

Although pre-MCP documents were not originally FAIR-compliant, they have been **retrofitted** with MCP-DL metadata and preserved in modern formats.

| Principle | Implementation |
| :-- | :-- |
| **Findable** | Indexed under `legacy_manifest.yml` and Neo4j lineage records. |
| **Accessible** | Public access under CC-BY 4.0. |
| **Interoperable** | Retrofitted with YAML and PROV-O metadata. |
| **Reusable** | Retained for historical continuity and academic study. |

---

## 📦 Legacy Manifest Example

```yaml
manifest_version: "1.0"
year_range: "2017–2023"
total_entries: 6
entries:
  - id: L-2018-001
    title: "Terrain ETL Prototype"
    archived_date: "2018-09-02"
    reason: "legacy"
    successor: "../../../data/processed/terrain/README.md"
    hash: "aa13d2b..."
  - id: L-2021-001
    title: "Digital Atlas Proposal"
    archived_date: "2021-03-12"
    reason: "legacy"
    successor: "../../../architecture/knowledge-graph.md"
    hash: "bb19ec7..."
```

> Each entry contains SHA-256 checksums for validation and cross-links to modern equivalents.

---

## 🧾 Governance & Preservation Metadata

```yaml
preservation:
  bagit_package: "bags/kfm_legacy_archive_bagit/"
  checksum_validation: "verified"
  migrated_to_graph: true
  last_verified: "2025-10-18"
  linked_doi: "10.5281/zenodo.1234901"
```

---

## 🧩 Legacy Data Provenance (RDF/Turtle)

```turtle
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix crm:  <http://www.cidoc-crm.org/cidoc-crm/> .
@prefix dc:   <http://purl.org/dc/terms/> .
@prefix kfm:  <https://kfm.org/id/> .

kfm:legacy/digital_atlas_proposal_2021
    a prov:Entity ;
    dc:title "Digital Atlas Proposal — Pre-MCP Draft" ;
    prov:wasAttributedTo kfm:agent/frontier_cartography_team ;
    prov:wasDerivedFrom kfm:legacy/terrain_etl_prototype_2018 ;
    prov:wasInfluencedBy kfm:legacy/data_ingest_strategy_2019 ;
    prov:wasInfluencedBy kfm:legacy/mcp_draft_notes_2022 ;
    dc:description "Proposal that inspired the unified KFM Knowledge Graph." .
```

---

## 🧮 Validation & Governance Metrics

| Validation | Result | Verified By |
| :-- | :-- | :-- |
| YAML Schema | ✅ | `yamllint` + `jsonschema` |
| Checksum Verification | ✅ | `verify_checksums.py` |
| Graph Ingestion | ✅ | `tools/graph_ingest_notes.py` |
| FAIR Retrofitting | ✅ | `scripts/fair_validate.py` |
| Metadata Completeness | ✅ | CI/CD Audit (2025-10-18) |

---

## 🧠 Significance

> “Legacy defines provenance.”  
> These archives connect KFM’s present reproducibility standards to its earliest conceptual origins.

**Legacy themes retained:**
- The transition from **manual ETL** to automated, validated pipelines.  
- The emergence of **documentation-first** culture.  
- The conceptual origin of **MCP and data lineage tracking**.  

These archives serve not just as historical data but as **teaching and governance artifacts**.

---

## 🔮 Future Roadmap

| Milestone | Target | Description |
| :-- | :-- | :-- |
| v1.1 | Q2 2026 | Annotate legacy docs with MCP-DL ontology metadata. |
| v1.2 | Q3 2026 | Add OCR and AI-transcribed versions of scanned documents. |
| v1.3 | Q4 2026 | Integrate legacy document viewer into KFM Web UI. |
| v2.0 | 2027 | Complete migration of legacy lineage into blockchain checksum registry. |

---

## 📎 Related Documentation

| File | Description |
| :-- | :-- |
| `docs/notes/archive/README.md` | Global archive governance and structure. |
| `docs/architecture/knowledge-graph.md` | Graph lineage & semantic ingestion. |
| `docs/standards/documentation.md` | Documentation-first governance principles. |
| `docs/notes/templates/README.md` | Metadata and YAML template examples. |
| `data/work/graph/legacy_lineage.ttl` | RDF record of legacy-to-modern lineage. |

---

## 📅 Version History

| Version | Date | Author | Summary |
| :-- | :-- | :-- | :-- |
| v1.0.0 | 2025-10-18 | @kfm-docs | Established legacy archive under MCP-DL v6.3; added FAIR retrofitting, manifests, and RDF lineage. |

---

<div align="center">

**Kansas Frontier Matrix** — *“Every Origin Recorded. Every Evolution Proven.”*  
📍 `docs/notes/archive/legacy/README.md` · Historical preservation record maintained under MCP-DL v6.3 and FAIR governance standards.

</div>
