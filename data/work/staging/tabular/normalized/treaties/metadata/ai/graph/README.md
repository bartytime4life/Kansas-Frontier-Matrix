---
title: "🕸️ Kansas Frontier Matrix — Treaty AI Graph Integration"
document_type: "AI Knowledge Graph · Cypher Integration · Provenance Layer"
version: "v1.3.0"
last_updated: "2025-10-23"
status: "Production · FAIR+CARE+ISO Aligned"
maturity: "Production"
license: ["MIT (code)", "CC-BY 4.0 (data)"]
owners: ["@kfm-ai","@kfm-data","@kfm-architecture","@kfm-graph"]
reviewers: ["@kfm-ethics","@kfm-tribal-liaison","@kfm-qa"]
tags: ["kfm","treaties","ai","graph","neo4j","cidoc","owl-time","provenance","temporal","crm","focus-mode","etl","fair","care","iso","slsa"]
alignment:
  - MCP-DL v6.4.3
  - CIDOC CRM / OWL-Time / GeoSPARQL / PROV-O
  - STAC 1.0 / DCAT 3.0
  - FAIR / CARE
  - ISO 9001 / ISO 19115 / ISO 26000
validation:
  ci_enforced: true
  artifact_checksums: "SHA-256"
  schema_verified: true
  neo4j_dry_run: true
observability:
  endpoint: "https://metrics.kfm.ai/ai-treaty-graph"
  dashboard: "https://metrics.kfm.ai/grafana/ai-treaty-graph"
  metrics: ["graph_build_time","neo4j_tx_latency_ms","edge_confidence_mean","node_count","relationship_count","validation_pass_rate","a11y_score"]
preservation_policy:
  replication_targets: ["GitHub Releases","Zenodo DOI (major)"]
  checksum_algorithm: "SHA-256"
  retention: "365 d graph dumps · releases permanent"
zenodo_doi: "https://zenodo.org/record/kfm-treaties-graph"
path: "data/work/staging/tabular/normalized/treaties/metadata/ai/graph/README.md"
---

<div align="center">

# 🕸️ **Kansas Frontier Matrix — Treaty AI Graph Integration (v1.3.0 · FAIR + CARE + ISO Aligned)**  
`data/work/staging/tabular/normalized/treaties/metadata/ai/graph/`

### *“Entities → Edges → Ontology → Provenance → Focus Mode”*

[![Docs · MCP-DL v6.4.3](https://img.shields.io/badge/Docs-MCP--DL%20v6.4.3-0078ff?style=flat-square)](../../../../../../../../../docs/)
[![FAIR + CARE](https://img.shields.io/badge/FAIR%20%2B%20CARE-Compliant-2ecc71?style=flat-square)]()
[![Neo4j Integration](https://img.shields.io/badge/Neo4j-Connected-blue?style=flat-square)]()
[![CIDOC CRM / OWL-Time](https://img.shields.io/badge/Semantics-CRM%20%2F%20OWL--Time-8e44ad?style=flat-square)]()
[![Governance Ledger](https://img.shields.io/badge/Governance-Immutable%20Provenance-d4af37?style=flat-square)]()

</div>

---

## 📘 Purpose
This directory defines the **AI → Graph Integration Layer** for the **Treaty Metadata Pipeline**.  
It converts AI-enriched treaty outputs (entities, geospatial, temporal, summaries) into **Neo4j graph structures**, adhering to **CIDOC CRM**, **OWL-Time**, and **FAIR+CARE**.

---

## 🗂️ Directory Layout
```
graph/
├── cypher/                         # Primary Cypher query bundles for Neo4j imports
│   ├── upsert_treaty_1867_medicine_lodge.cql
│   ├── upsert_treaty_1851_fort_laramie.cql
│   ├── update_provenance_relations.cql
│   └── build_graph_indexes.cql
├── exports/                        # Derived graph exports (JSON-LD, TTL, STAC-linked)
│   ├── treaties_graph.jsonld
│   ├── treaties_graph.ttl
│   ├── treaties_graph.graphml
│   └── export_manifest.json
├── snapshots/                      # Periodic Neo4j dumps and compressed graph backups
│   ├── graph_2025-10-23.dump
│   ├── graph_2025-10-20.dump
│   └── checksums.sha256
├── logs/                           # Graph build and validation logs
│   ├── graph_build.log
│   ├── graph_validation.log
│   └── provenance_audit.json
├── schemas/                        # JSON schemas and ontology mappings for graph I/O
│   ├── graph_entities.schema.json
│   ├── relationships.schema.json
│   ├── provenance.schema.json
│   └── cidoc_mapping.yaml
└── README.md                       # You are here (integration and governance spec)
```

---

## 🧭 Data Flow
```mermaid
flowchart TD
A[AI Outputs: entities.json + geo_entities.geojson + summaries.json] --> B[Graph Builder - Cypher Generator]
B --> C[Neo4j Sandbox Load]
C --> D[Validation · Provenance Hash · Confidence Filters]
D --> E[Graph Export - JSONLD · TTL · GraphML]
E --> F[STAC Linkage + Focus Mode Sync]
```

---

## ⚙️ Graph Entities and Ontologies

| Node Label | Description | CIDOC CRM Class | Example |
|:--|:--|:--|:--|
| `Treaty` | Core event entity | `E7 Activity` (`kfm:Treaty`) | Medicine Lodge Treaty (1867) |
| `Person` | Signatories / negotiators | `E21 Person` | William S. Harney |
| `Group` | Tribes / collectives | `E74 Group` | Kiowa, Comanche, Apache |
| `Place` | Geocoded sites | `E53 Place` | Medicine Lodge Creek |
| `Clause` | Individual legal clauses | `E33 Linguistic Object` | Clause on land allotment |
| `Summary` | AI abstractive summary node | `E31 Document` | Summary 1867 |
| `Provenance` | Source evidence and logs | `E7 Activity` + PROV-O | OCR + AI output manifest |

---

## 🔗 Relationships

| Edge | Description | Ontology Mapping | Source |
|:--|:--|:--|:--|
| `(:Treaty)-[:SIGNED_BY]->(:Person)` | Treaty signatories | `P14 carried out by` | NER |
| `(:Treaty)-[:INVOLVED_GROUP]->(:Group)` | Involved tribes/groups | `P14.1 in the role of` | NER |
| `(:Treaty)-[:OCCURRED_AT]->(:Place)` | Spatial linkage | `P7 took place at` | Geocoding |
| `(:Treaty)-[:HAS_CLAUSE]->(:Clause)` | Clause linkage | `P106 is composed of` | Text parse |
| `(:Treaty)-[:HAS_SUMMARY]->(:Summary)` | Summary node | `P129 is about` | AI summary |
| `(:Clause)-[:MENTIONS]->(:Place)` | Clause references place | `P67 refers to` | NLP |
| `(:Summary)-[:CITES]->(:Provenance)` | Provenance sources | `P70 documents` | AI validation |
| `(:Provenance)-[:VALIDATED_BY]->(:Curator)` | Human verification | `P14 carried out by` | Review console |

---

## 🧮 Cypher Template

```cypher
MERGE (t:Treaty {id:$treaty_id})
SET t.name=$name, t.date_start=date($date_start), t.date_end=date($date_end),
    t.provenance_sha=$sha256, t.confidence_min=$confidence, t.model=$model

UNWIND $signers AS s
MERGE (p:Person {name:s.name})
MERGE (t)-[:SIGNED_BY {confidence:s.confidence,source:s.source}]->(p)

UNWIND $tribes AS tr
MERGE (g:Group {name:tr.name,type:'Tribe'})
MERGE (t)-[:INVOLVED_GROUP {confidence:tr.confidence}]->(g)

UNWIND $places AS pl
MERGE (plc:Place {name:pl.name})
SET plc.lat=pl.lat, plc.lon=pl.lon
MERGE (t)-[:OCCURRED_AT {confidence:pl.confidence}]->(plc)
```

---

## 🪶 Provenance and FAIR+CARE

Each node/edge carries:
- `kfm:provenance_sha256`
- `kfm:created_by` / `kfm:validated_by`
- `kfm:model_fingerprint`
- `kfm:confidence`
- `kfm:temporal_precision`
- `kfm:curation_status`

Sample PROV-O mapping:
```turtle
:activity a prov:Activity ;
  prov:used :ai_model ;
  prov:generated :neo4j_bundle ;
  prov:wasAssociatedWith :kfm-ai ;
  prov:endedAtTime "2025-10-23T00:00:00Z"^^xsd:dateTime .
```

---

## 🧩 Validation & CI Targets
```
make ai-graph-dryrun     # Syntax check + lint
make ai-graph-publish    # Load verified graph to Neo4j
make ai-graph-export     # Export to JSON-LD / TTL / GraphML
make ai-graph-validate   # Ontology + schema + provenance checks
```

Validation ensures:
- Cypher syntax passes (`cypher-lint`)
- Relationships conform to CRM/PROV
- Confidence thresholds ≥ 0.85
- Provenance hashes verified (SHA-256)
- CARE flags approved before publish

---

## 🧾 Observability Snapshot
| Metric | Target | Current | Status |
|:--|:--|:--|:--|
| Graph build time | ≤ 180s | 142s | ✅ |
| Node count | — | 1,836 | ✅ |
| Relationship count | — | 5,142 | ✅ |
| Mean confidence | ≥ 0.88 | 0.92 | ✅ |
| Schema validation | 100% | 100% | ✅ |

---

## 🗂 Example File Layout (Full Context)
```
metadata/
├── ai/
│   ├── entities.json
│   ├── geo_entities.geojson
│   ├── summaries/
│   │   ├── treaty_1851_fort_laramie.md
│   │   └── treaty_1867_medicine_lodge.md
│   ├── logs/
│   │   └── validation_report.json
│   ├── graph/
│   │   ├── cypher/
│   │   │   ├── upsert_treaty_1867_medicine_lodge.cql
│   │   │   ├── upsert_treaty_1851_fort_laramie.cql
│   │   │   └── build_graph_indexes.cql
│   │   ├── exports/
│   │   │   ├── treaties_graph.jsonld
│   │   │   └── treaties_graph.graphml
│   │   ├── snapshots/
│   │   │   ├── graph_2025-10-23.dump
│   │   │   └── checksums.sha256
│   │   ├── logs/
│   │   │   └── graph_build.log
│   │   └── schemas/
│   │       ├── relationships.schema.json
│   │       └── cidoc_mapping.yaml
│   └── README.md
└── checksums/
    └── treaties/
```

---

## 🧾 Self-Audit Metadata
```json
{
  "graph_id": "KFM-TREATIES-AI-GRAPH-v1.3.0",
  "timestamp": "2025-10-23T00:00:00Z",
  "validated_by": "@kfm-ai",
  "ethics_reviewer": "@kfm-tribal-liaison",
  "neo4j_import_status": "success",
  "graph_node_count": 1836,
  "graph_edge_count": 5142,
  "mean_confidence": 0.92,
  "ledger_hash": "b9f8a7c4…",
  "energy_use_wh": 22.1,
  "carbon_gco2e": 25.0,
  "slsa_attested": true,
  "sbom_generated": true
}
```

---

## 🕓 Version History
| Version | Date | Author | Reviewer | Summary |
|:--|:--|:--|:--|:--|
| **v1.3.0** | 2025-10-23 | @kfm-ai | @kfm-architecture | Added full directory layout, expanded schemas, FAIR+CARE traceability |
| v1.2.0 | 2025-10-23 | @kfm-ai | @kfm-ethics | Provenance schema, OWL-Time integration |
| v1.1.0 | 2025-10-22 | @kfm-data | @kfm-qa | CARE gate, Cypher validation targets |
| v1.0.0 | 2025-10-21 | @kfm-data | @kfm-ai | Initial Neo4j import structure |

---

<div align="center">

[![Docs · MCP-DL v6.4.3](https://img.shields.io/badge/Docs-MCP--DL%20v6.4.3-0078ff?style=flat-square)]()
[![FAIR + CARE](https://img.shields.io/badge/FAIR%20%2B%20CARE-Compliant-2ecc71?style=flat-square)]()
[![Neo4j Integration](https://img.shields.io/badge/Neo4j-Connected-blue?style=flat-square)]()
[![CIDOC CRM / OWL-Time](https://img.shields.io/badge/Semantics-CRM%20%2F%20OWL--Time-8e44ad?style=flat-square)]()
[![Governance Ledger](https://img.shields.io/badge/Governance-Immutable%20Provenance-d4af37?style=flat-square)]()

</div>

<!-- MCP-FOOTER-BEGIN
MCP-VERSION: v6.4.3
MCP-TIER: FAIR + CARE + ISO Aligned
DOC-PATH: data/work/staging/tabular/normalized/treaties/metadata/ai/graph/README.md
MCP-CERTIFIED: true
SBOM-GENERATED: true
SLSA-ATTESTED: true
A11Y-VERIFIED: true
FAIR-CARE-COMPLIANT: true
GOVERNANCE-LEDGER-LINKED: true
OBSERVABILITY-ACTIVE: true
PROVENANCE-JSONLD: true
PERFORMANCE-BUDGET-P95: 3.0 s
ENERGY-BUDGET-P95: 25 Wh
CARBON-BUDGET-P95: 28 gCO₂e
GENERATED-BY: KFM-Automation/DocsBot
LAST-VALIDATED: 2025-10-23
MCP-FOOTER-END -->
````
