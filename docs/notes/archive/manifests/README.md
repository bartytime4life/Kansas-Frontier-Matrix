<div align="center">

# 🗂️ Kansas Frontier Matrix — **Archive Manifests & Provenance Index**  
`docs/notes/archive/manifests/README.md`

**Purpose:** Maintain a centralized **index and manifest system** for all archived documentation within the  
**Kansas Frontier Matrix (KFM)** — linking file-level provenance, checksum validation, FAIR compliance, and cross-repository archival exports (BagIt + Zenodo).  
This directory acts as the **metadata backbone** for verifying, reproducing, and tracing historical document lineage across all project eras (Legacy → MCP-DL v6.3+).

[![Docs · MCP-DL v6.3](https://img.shields.io/badge/Docs-MCP--DL%20v6.3-blue)](../../../standards/documentation.md)
[![Docs-Validate](https://img.shields.io/badge/docs-validated-brightgreen?logo=github)](../../../.github/workflows/docs-validate.yml)
[![Policy-as-Code](https://img.shields.io/badge/policy-OPA%2FConftest-purple)](../../../.github/workflows/policy-check.yml)
[![Knowledge Graph](https://img.shields.io/badge/Linked-Knowledge%20Graph-green)](../../../architecture/knowledge-graph.md)
[![Archive Integrity](https://img.shields.io/badge/Archive-Manifests-orange)](../README.md)
[![FAIR Validation](https://img.shields.io/badge/FAIR-Data%20Compliant-brightgreen)](../../../standards/documentation.md)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../../../LICENSE)

</div>

```yaml
---
title: "Kansas Frontier Matrix — Archive Manifests & Provenance Index"
document_type: "Archive Manifest Directory"
version: "v1.3.0"
last_updated: "2025-10-18"
created: "2024-01-01"
owners: ["@kfm-docs","@kfm-governance","@kfm-data","@kfm-security"]
status: "Stable"
maturity: "Production"
scope: "Docs/Notes/Archive/Manifests"
license: "CC-BY 4.0"
semver_policy: "MAJOR.MINOR.PATCH"
tags: ["archive","manifest","checksum","provenance","governance","fair","mcp","bagit","policy"]
audit_framework: "MCP-DL v6.3"
semantic_alignment:
  - PROV-O
  - CIDOC CRM
  - OWL-Time
  - JSON Schema
  - ISO 8601
  - DCAT 2.0
  - PREMIS 3.0
preservation_policy:
  format_standards: ["YAML","JSON","RDF/Turtle"]
  checksum_algorithm: "SHA-256"
  replication_targets: ["GitHub","Zenodo","OSF","Local Cold Storage"]
  revalidation_cycle: "quarterly"
retention_policy:
  archive_after: "immediate"
  purge_after: "never"
automation:
  - name: "Manifest Generator"
    schedule: "0 4 1 * *"
    action: "tools/generate_archive_manifests.py"
  - name: "Checksum Verifier"
    schedule: "0 6 * * SUN"
    action: "tools/verify_checksums.py"
  - name: "FAIR Revalidator"
    schedule: "0 7 1 */3 *"
    action: "tools/fair_validate_archive.py"
ai_index:
  embed_in_graph: true
  model: "sentence-transformers/all-MiniLM-L6-v2"
  store: "Neo4j Vector Index"
  searchable_fields: ["title","summary","tags"]
---
```

---

## 📚 Overview

The `/docs/notes/archive/manifests/` directory provides **machine-readable metadata manifests**  
for every KFM archival collection — including **Legacy Archives (2017–2023)**, **2024–2025 Annual Archives**,  
and all subsequent **MCP-DL validated documentation exports**.

These manifests ensure that every archived document, note, or dataset:

- 🧩 Is **FAIR-compliant** and checksum-verified.  
- 🧾 Retains **complete provenance** through PROV-O & CIDOC CRM lineage.  
- 🔗 Connects to **graph ingestion scripts** for Neo4j + RDF indexing.  
- 📦 Is packaged into **BagIt exports** for Zenodo or external repositories.  

---

## 🧱 Directory Layout

```text
docs/notes/archive/manifests/
├── README.md                        # (this file)
├── manifest_2024.yml                # Yearly archive manifest (2024)
├── manifest_2025.yml                # Yearly archive manifest (2025)
├── manifest_legacy.yml              # Consolidated legacy (2017–2023)
├── archive_index.json               # Master provenance index across years
├── fair_validation_report.json      # FAIR and checksum status per file
└── lineage_graph.ttl                # RDF/Turtle provenance exports
```

> 🧠 Each manifest follows a consistent schema and is validated by CI before merge.

---

## 🧩 Manifest Schema Definition

Each manifest YAML/JSON document follows the schema at `docs/schemas/archive_manifest.schema.json`.

**Schema Summary:**

| Field              | Type    | Description                       | Example                                   |
| :----------------- | :------ | :-------------------------------- | :---------------------------------------- |
| `manifest_version` | string  | Semantic version of manifest fmt  | `"1.0"`                                   |
| `year`/`year_range`| string  | Year or range covered             | `"2025"` or `"2017–2023"`                 |
| `total_entries`    | integer | Number of archived items          | `8`                                       |
| `entries`          | array   | Object list of archive entries    | see below                                 |

**Example Entry**
```yaml
- id: L-2023-001
  title: "Architecture Briefing v0 — Pre-MCP-DL System Design"
  archived_date: "2023-06-28"
  reason: "legacy"
  file: "../../../docs/notes/archive/legacy/2023_architecture_briefing_v0.md"
  successor: "../../../architecture/data-architecture.md"
  checksum: "de3b5f6ca9d7e42b..."
  doi: "10.5281/zenodo.1234993"
  verified: true
  graph_ingested: true
```

---

## 🧮 Example Manifests

### 🗃️ Legacy Archive (2017–2023)
```yaml
manifest_version: "1.0"
year_range: "2017–2023"
total_entries: 8
entries:
  - id: L-2018-002
    title: "Terrain ETL Prototype — Kansas Elevation Workflow (2018)"
    archived_date: "2018-11-20"
    successor: "../../../architecture/data-architecture.md"
    checksum: "e47bcd9..."
    doi: "10.5281/zenodo.1234912"
    verified: true
  - id: L-2021-001
    title: "Digital Atlas Proposal — Conceptual Blueprint (2021)"
    archived_date: "2021-03-12"
    successor: "../../../architecture/knowledge-graph.md"
    checksum: "f1c5a8b..."
    verified: true
```

### 📜 2024 Archive
```yaml
manifest_version: "1.0"
year: 2024
entries:
  - id: A-2024-001
    title: "Initial Design Discussion"
    archived_date: "2024-02-10"
    successor: "../../../architecture/data-architecture.md"
    checksum: "bb2aa12..."
    doi: "10.5281/zenodo.1234922"
```

### 🧾 2025 Archive
```yaml
manifest_version: "1.0"
year: 2025
entries:
  - id: A-2025-001
    title: "January 2025 Governance & Infrastructure Sync"
    archived_date: "2025-01-10"
    successor: "../../../architecture/knowledge-graph.md"
    checksum: "9b7a6e14d4ccf821..."
    verified: true
```

---

## 🧠 Master Provenance Index (`archive_index.json`)

A machine-parsable JSON catalog that merges all manifest data into a single graph-ready structure for AI search and lineage visualization.

```json
{
  "archives": [
    {
      "id": "A-2025-001",
      "title": "January 2025 Governance & Infrastructure Sync",
      "archived_date": "2025-01-10",
      "year": 2025,
      "checksum": "9b7a6e14d4ccf821...",
      "successor": "docs/architecture/knowledge-graph.md",
      "graph_ingested": true,
      "verified": true
    }
  ],
  "last_compiled": "2025-10-18",
  "generator": "tools/generate_archive_manifests.py"
}
```

---

## 🧾 FAIR Validation Report

Each CI/CD cycle generates a FAIR + checksum compliance report under  
`docs/notes/archive/manifests/fair_validation_report.json`.

```json
{
  "timestamp": "2025-10-18T08:00:00Z",
  "total_checked": 37,
  "valid": 37,
  "invalid": 0,
  "fair_compliance": {
    "findable": true,
    "accessible": true,
    "interoperable": true,
    "reusable": true
  },
  "issues": []
}
```

---

## 🧩 Provenance Graph Export (`lineage_graph.ttl`)

Each manifest contributes RDF triples describing document lineage, used by Neo4j and external semantic tools.

```turtle
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix dc:   <http://purl.org/dc/terms/> .
@prefix kfm:  <https://kfm.org/id/> .

kfm:archive/A-2025-001
    a prov:Entity ;
    dc:title "January 2025 Governance & Infrastructure Sync" ;
    prov:wasGeneratedBy kfm:activity/meeting_governance_2025_01_10 ;
    prov:used kfm:document/standards_documentation ;
    prov:wasAttributedTo kfm:agent/kfm-governance ;
    prov:wasDerivedFrom kfm:archive/A-2024-001 ;
    dc:date "2025-01-10"^^xsd:date .
```

---

## ⚙️ Validation & CI/CD Integration

| Validation            | Tool / Workflow                 | Purpose                           |
| :-------------------- | :------------------------------ | :-------------------------------- |
| **Schema Validation** | `jsonschema`                    | Ensures manifest compliance       |
| **Checksum Verify**   | `tools/verify_checksums.py`     | Confirms files’ integrity         |
| **FAIR Validation**   | `scripts/fair_validate.py`      | Confirms FAIR data principles     |
| **Graph Sync**        | `tools/graph_ingest_legacy.py`  | Ingests provenance to Neo4j       |
| **AI Embedding**      | `scripts/vector_embed.py`       | Adds to Neo4j Vector Index        |

> **Local run**
```bash
make docs-validate && make docs-lint
```

---

## 📈 Governance Dashboard Metrics

| Metric              | Current | Target | Notes                     |
| :------------------ | :------ | :----- | :------------------------ |
| Manifest Coverage   | 100%    | 100%   | All archives indexed      |
| FAIR Compliance     | ✅       | 100%   | Verified by CI            |
| Graph Ingestion     | ✅       | 100%   | All manifests synced      |
| Zenodo DOI Export   | 5       | ≥ 5    | Annual release snapshots  |
| BagIt Validations   | ✅       | Quarterly | Retention policy enforced |

---

## 🔗 External Integration

| Service     | Role                                   | Status |
| :---------- | :-------------------------------------- | :----- |
| **Zenodo**  | Public preservation & DOI issuance      | ✅ Active |
| **OSF**     | Mirror for institutional archive        | 🟡 Pending 2026 |
| **Neo4j Aura** | Knowledge graph storage & search     | ✅ Synced |
| **GitHub Pages** | Hosting of manifests & reports     | ✅ Published |

---

## 🧩 Future Roadmap

| Milestone | Target | Description                                                |
| :-------- | :----- | :--------------------------------------------------------- |
| v1.3      | Q2 2026| Blockchain-based manifest hashing for authenticity         |
| v1.4      | Q3 2026| Interactive “Archive Browser” dashboard in KFM Web UI     |
| v2.0      | 2027   | Federated FAIR registry for manifests                     |
| v2.1      | 2028   | Automatic ontology crosswalk export for SKOS vocabularies |

---

## 📎 Related Documentation

| File                                           | Description                              |
| :--------------------------------------------- | :--------------------------------------- |
| `../README.md`                                 | Global archive governance                 |
| `../../../architecture/knowledge-graph.md`     | Provenance ingestion and ontology schema  |
| `../../../standards/documentation.md`          | MCP-DL documentation governance           |
| `../../../schemas/archive_manifest.schema.json`| JSON schema for manifest validation       |
| `../../../../data/work/logs/docs/archive_summary_<YYYY_QN>.json` | Quarterly validation report |
| `../../../../data/work/graph/archive_lineage.ttl` | RDF lineage export from manifests      |

---

## 📅 Version History

| Version | Date       | Author      | Summary                                                                                 |
| :------ | :--------- | :---------- | :-------------------------------------------------------------------------------------- |
| **v1.3.0** | 2025-10-18 | @kfm-docs   | Added policy badge, clarified CI gates, expanded FAIR/PROV exports and governance KPIs. |
| v1.2.0  | 2025-10-18 | @kfm-docs   | FAIR reports, RDF export, governance metrics; aligned with MCP-DL automation.           |
| v1.1.0  | 2024-11-30 | @kfm-data   | Integrated archive_index.json and Neo4j vector embeddings.                              |
| v1.0.0  | 2024-01-01 | @kfm-docs   | Initial manifest system for annual and legacy archives.                                  |

---

<div align="center">

**Kansas Frontier Matrix** — *“Every Record Indexed. Every Checksum Proven.”*  
📍 `docs/notes/archive/manifests/README.md` · Maintained under MCP-DL v6.3 with full FAIR, PREMIS, and PROV-O compliance.

</div>