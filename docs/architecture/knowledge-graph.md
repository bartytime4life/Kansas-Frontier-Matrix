---
title: "🧠 Kansas Frontier Matrix — Knowledge Graph Architecture (Tier-Ω+∞ Certified)"
path: "docs/architecture/knowledge-graph.md"
version: "v2.1.1"
last_updated: "2025-11-16"
review_cycle: "Quarterly / Graph & Governance Council"
commit_sha: "<latest-commit-hash>"
license: "MIT (code) · CC-BY 4.0 (docs)"
owners: ["@kfm-architecture","@kfm-graph","@kfm-docs","@kfm-ai","@kfm-governance"]
maturity: "Production"
status: "Stable"
tags: ["knowledge-graph","neo4j","ontology","cidoc","owl-time","geosparql","graph","governance","fair","care"]
sbom_ref: "../../releases/v2.1.1/sbom.spdx.json"
manifest_ref: "../../releases/v2.1.1/manifest.zip"
data_contract_ref: "../../docs/contracts/data-contract-v3.json"
governance_ref: "../../docs/standards/governance/ROOT-GOVERNANCE.md"
alignment:
  - MCP-DL v6.4.3
  - CIDOC CRM v7.1.1 / OWL-Time / GeoSPARQL 1.1
  - STAC / DCAT / PROV-O
  - FAIR / CARE
  - ISO 19115 Metadata Standard
validation:
  frontmatter_required: ["title","version","last_updated","owners","license"]
  docs_ci_required: true
  mermaid_end_marker: "<!-- END OF MERMAID -->"
preservation_policy:
  retention: "graph schema permanent · lineage metadata 1 year"
  checksum_algorithm: "SHA-256"
---

<div align="center">

# 🧠 **Kansas Frontier Matrix — Knowledge Graph Architecture (v2.1.1 · Tier-Ω+∞ Certified)**  
`docs/architecture/knowledge-graph.md`

**Mission:** Define the **semantic knowledge graph architecture** of the **Kansas Frontier Matrix (KFM)** —  
linking datasets, entities, events, places, and documents into a unified, FAIR+CARE-compliant ontology ecosystem.

[![Docs · MCP-DL v6.4.3](https://img.shields.io/badge/Docs-MCP--DL%20v6.4.3-blue?logo=markdown)](../../docs/)
[![Neo4j Graph Validation](https://img.shields.io/badge/Graph%20Validation-Neo4j%20PASS-brightgreen?logo=neo4j)](../../src/graph/)
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Certified-gold)](../../docs/standards/faircare-validation.md)
[![License: MIT · CC-BY 4.0](https://img.shields.io/badge/License-MIT%20%7C%20CC--BY%204.0-green)](../../LICENSE)

</div>

---

## 📚 Overview

The **KFM Knowledge Graph** is the semantic backbone of the system — enabling data integration, temporal reasoning, and  
cross-domain discovery across historical, environmental, and cultural datasets.  

It harmonizes **spatial, temporal, and cultural semantics** using a unified ontology composed of:
- **CIDOC CRM** — Cultural heritage ontology for entities, events, and documents.  
- **OWL-Time** — Temporal ontology for event intervals and instants.  
- **GeoSPARQL** — Geospatial ontology for spatial reasoning and geometry handling.  
- **PROV-O** — Provenance ontology for dataset derivations and AI pipelines.  

---

## 🧩 Graph Architecture Overview

```mermaid
flowchart TD
  subgraph Graph["Neo4j Graph Schema"]
    P["E53 Place"]
    E["E5 Event"]
    D["E31 Document"]
    A["E21 Actor / Person"]
    O["E22 Man-Made Object"]
  end

  subgraph Temporal["Temporal Ontology (OWL-Time)"]
    T1["time:Interval"]
    T2["time:Instant"]
  end

  subgraph Spatial["Spatial Ontology (GeoSPARQL)"]
    S1["geo:Feature"]
    S2["geo:hasGeometry (WKT / GeoJSON)"]
  end

  subgraph Provenance["Provenance (PROV-O)"]
    PR1["prov:Activity"]
    PR2["prov:Entity"]
    PR3["prov:wasDerivedFrom"]
  end

  E -->|P7 took place at| P
  E -->|P14 carried out by| A
  D -->|P70 documents| E
  O -->|P108 has produced| D
  E -->|time:hasTimeSpan| T1
  P -->|geo:hasGeometry| S1
  PR2 -->|prov:wasDerivedFrom| D
```
<!-- END OF MERMAID -->

---

## 🧱 Graph Schema Definition

| Entity Type | CIDOC CRM Class | Description | Example |
|:--|:--|:--|:--|
| **Person / Actor** | `E21_Person` | Individual or group associated with an event. | “Surveyor John Wesley Powell” |
| **Place** | `E53_Place` | Geospatial location (county, watershed, or site). | “Douglas County, KS” |
| **Event** | `E5_Event` | Occurrence in space and time. | “Flood of 1951” |
| **Document** | `E31_Document` | Text or map describing an event. | “FEMA Damage Assessment Report” |
| **Dataset** | `E73_Information_Object` | Digital dataset or collection. | “NOAA Storm Events Database” |
| **Object** | `E22_Man-Made_Object` | Physical or digital artifact. | “Topographic Map (1905)” |
| **Geometry** | `geo:Feature` | Spatial geometry object (point, line, polygon). | GeoJSON geometry |
| **Time Interval** | `time:Interval` | Start and end date span. | `1951-07-01` to `1951-07-10` |

---

## 🧮 Ontology Alignment

| Ontology | Domain | Integration Role |
|:--|:--|:--|
| **CIDOC CRM** | Cultural / Historical data | Primary schema backbone |
| **OWL-Time** | Temporal reasoning | Event duration and sequencing |
| **GeoSPARQL** | Geospatial semantics | Geometry and topology linking |
| **PROV-O** | Data provenance | Derivation and workflow lineage |
| **STAC/DCAT** | Metadata exchange | Crosswalk from datasets to graph nodes |

---

## ⚙️ Graph Implementation (Neo4j)

| Aspect | Implementation | Validation |
|:--|:--|:--|
| **Database** | Neo4j 5.x (property graph model) | Schema constraints in `schema.cypher` |
| **Modeling Language** | Cypher + APOC procedures | Validated in CI via `graph-validate.yml` |
| **Ontology Import** | RDF → Property Graph ETL | `src/graph/load_ontology.py` |
| **Exports** | JSON-LD, TTL, GraphML | FAIR+CARE compliance export tests |
| **Visualization** | Neo4j Bloom + D3.js | Governance-approved schemas |

---

## 🧠 Semantic Data Flow

```mermaid
flowchart LR
  A["STAC / DCAT Dataset Metadata"] --> B["ETL: Convert to Graph JSON-LD"]
  B --> C["Neo4j Import (CIDOC CRM Schema)"]
  C --> D["Ontology Validation (SHACL + FAIR+CARE)"]
  D --> E["Query / API (GraphQL + SPARQL)"]
  E --> F["Linked Data Publication (JSON-LD / TTL)"]
```
<!-- END OF MERMAID -->

---

## 🔍 Example Cypher Patterns

### Entity and Event Relationship
```cypher
MATCH (p:E21_Person)-[:PARTICIPATED_IN]->(e:E5_Event)
RETURN p.name, e.label, e.start_date, e.end_date
LIMIT 10;
```

### Provenance Chain
```cypher
MATCH (d:E31_Document)-[:PROV_WAS_DERIVED_FROM]->(src:E73_Information_Object)
RETURN d.title, src.title, src.source_url;
```

### Temporal Query
```cypher
MATCH (e:E5_Event)-[:HAS_TIME_SPAN]->(t:TimeInterval)
WHERE t.start >= date("1950-01-01") AND t.end <= date("1951-12-31")
RETURN e.label, t.start, t.end;
```

---

## ⚖️ FAIR + CARE Alignment

| Principle | Implementation | Artifact |
|:--|:--|:--|
| **Findable** | Indexed via Neo4j full-text and STAC IDs. | `src/graph/schema.cypher` |
| **Accessible** | JSON-LD + REST/GraphQL endpoints. | `/api/v1/graph/` |
| **Interoperable** | RDF mapping via CIDOC CRM, OWL-Time, GeoSPARQL. | `docs/architecture/ontology/` |
| **Reusable** | Versioned graph exports + checksums. | `releases/v*/manifest.zip` |
| **Collective Benefit (CARE)** | Ontology designed with cultural stewardship and transparency. | `data/stac/*properties.data_ethics` |

---

## 🧩 Governance Integration

| Workflow | Purpose | Output |
|:--|:--|:--|
| `ontology-validate.yml` | Verifies RDF → Neo4j mapping conformance. | `reports/validation/ontology_validation_report.json` |
| `faircare-validate.yml` | Assesses ethical ontology alignment. | `reports/fair/data_care_assessment.json` |
| `governance-ledger.yml` | Registers ontology version and checksum. | `data/reports/audit/data_provenance_ledger.json` |

---

## 🧾 Version History

| Version | Date | Author | Summary |
|:--|:--|:--|:--|
| **v2.1.1** | 2025-11-16 | @kfm-architecture | Added detailed ontology alignment, FAIR+CARE governance mapping, and CI workflows. |
| v2.0.0 | 2025-10-25 | @kfm-graph | Introduced Neo4j ontology schema and CIDOC CRM adoption. |
| v1.0.0 | 2025-10-04 | @kfm-architecture | Initial graph documentation and ontology integration plan. |

---

<div align="center">

**Kansas Frontier Matrix © 2025**  
*“Knowledge is Context — Provenance is Trust.”*  
📍 `docs/architecture/knowledge-graph.md` — Semantic knowledge graph architecture for the Kansas Frontier Matrix.

</div>

