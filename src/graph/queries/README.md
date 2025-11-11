---
title: "🔍 Kansas Frontier Matrix — Graph Queries & Analytical Patterns (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "src/graph/queries/README.md"
version: "v10.1.0"
last_updated: "2025-11-10"
review_cycle: "Continuous / Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../releases/v10.1.0/sbom.spdx.json"
manifest_ref: "../../../releases/v10.1.0/manifest.zip"
data_contract_ref: "../../../docs/contracts/data-contract-v3.json"
governance_ref: "../../../docs/standards/governance/DATA-GOVERNANCE.md"
telemetry_ref: "../../../releases/v10.1.0/focus-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/src-graph-queries-v3.json"
license: "MIT"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 🔍 **Kansas Frontier Matrix — Graph Queries & Analytical Patterns**
`src/graph/queries/README.md`

**Purpose:**  
Provide a library of **Cypher query templates and analytical patterns** used to retrieve, analyze, and visualize knowledge graph data for Focus Mode, AI reasoning, and governance reports.  
Implements FAIR+CARE-aligned querying principles for transparency, reproducibility, and explainable insight generation.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP--DL%20v6.3-blueviolet)](../../../docs/standards/)
[![FAIR+CARE Certified](https://img.shields.io/badge/FAIR%2BCARE-Diamond%E2%81%B9%20%C3%98%20Certified-gold)](../../../docs/standards/faircare-validation.md)
[![License: MIT](https://img.shields.io/badge/License-MIT-green)](../../../LICENSE)
[![Neo4j Cypher](https://img.shields.io/badge/Language-Cypher%20v5.x-lightgrey)]()
[![Explainable AI](https://img.shields.io/badge/AI-Focus%20Transformer%20v2-blue)]()

</div>

---

## 📘 Overview

This module houses **reusable Cypher query templates** and **analytics routines** for the Neo4j knowledge graph.  
Each query supports one of the major functions of KFM:

- Focus Mode subgraph retrieval and context expansion  
- Historical pattern analysis (temporal, spatial, or semantic)  
- Provenance and ethics audits  
- FAIR+CARE compliance verification  
- Dataset-level lineage tracing and AI validation  

All queries conform to **MCP documentation standards**, including explicit parameters, comments, and testable outputs.

---

## 🧩 Query Categories

| Category | Description | Example File |
|-----------|-------------|---------------|
| **Focus Mode Queries** | Retrieve contextual subgraphs centered on a selected entity (person, place, event). | `focus_mode.cql` |
| **Analytical Queries** | Compute statistics and correlations across graph relationships. | `analytics.cql` |
| **Governance Queries** | Verify provenance, lineage, and ledger synchronization. | `governance.cql` |
| **FAIR+CARE Compliance Queries** | Validate ethical metadata fields (authority, attribution). | `faircare_audit.cql` |
| **Temporal/Spatial Queries** | Detect chronological or geographical patterns (e.g. migration paths). | `spatiotemporal.cql` |

---

## 🧠 Focus Mode Query Templates

### 1️⃣ Retrieve subgraph for a given entity
```cypher
// Get all directly connected nodes and edges for an entity
MATCH (n {id:$entity_id})-[r*1..2]-(m)
RETURN n, r, m
LIMIT 250;
```

### 2️⃣ Fort or site dossier for Focus Mode
```cypher
MATCH (p:Place {name:$place})
OPTIONAL MATCH (p)<-[:LOCATED_AT]-(e:Event)
OPTIONAL MATCH (e)-[:ATTENDED]->(x:Person)
OPTIONAL MATCH (e)-[:MENTIONED_IN]->(d:Document)
RETURN p, collect(DISTINCT e) AS events,
       collect(DISTINCT x) AS participants,
       collect(DISTINCT d) AS documents;
```

### 3️⃣ Generate contextual summary (used by Focus Transformer v2)
```cypher
MATCH (n {id:$entity_id})-[r*1..2]-(m)
WITH n, collect(DISTINCT m.name) AS context
RETURN n.name AS entity, size(context) AS context_count,
       apoc.text.join(context, ", ") AS context_summary;
```

---

## 📊 Analytical Query Patterns

### Event frequency by decade
```cypher
MATCH (e:Event)
WITH toInteger(e.start.year / 10) * 10 AS decade, count(e) AS events
RETURN decade, events
ORDER BY decade ASC;
```

### People connected through common events
```cypher
MATCH (a:Person)-[:ATTENDED]->(e:Event)<-[:ATTENDED]-(b:Person)
WHERE a <> b
RETURN a.name AS person1, b.name AS person2, count(e) AS shared_events
ORDER BY shared_events DESC LIMIT 25;
```

### Cross-domain correlation: floods & migrations
```cypher
MATCH (f:Event {type:"Flood"})-[:LOCATED_AT]->(r:Region)
MATCH (m:Event {type:"Migration"})-[:LOCATED_AT]->(r)
WHERE abs(duration.inDays(date(f.start), date(m.start)).days) < 730
RETURN r.name, f.title, m.title, f.start, m.start;
```

---

## ⚖️ Governance & FAIR+CARE Queries

### Provenance completeness check
```cypher
MATCH (d:Document)
WHERE d.checksum IS NULL OR d.source IS NULL
RETURN d.id AS missing_provenance, d.title LIMIT 100;
```

### Blockchain ledger validation
```cypher
MATCH (n)
WHERE n.ledger_tx IS NULL
RETURN labels(n)[0] AS type, count(n) AS missingLedgerEntries;
```

### Ethics audit (Authority to Control)
```cypher
MATCH (n)
WHERE n.authority_to_control IS NULL OR n.authority_to_control = ""
RETURN labels(n)[0] AS entityType, count(n) AS missingFieldCount;
```

---

## 🌎 Temporal & Spatial Exploration Queries

### Migration path by tribe or group
```cypher
MATCH (p:Person {group:$tribe})-[:ATTENDED]->(e:Event)-[:LOCATED_AT]->(pl:Place)
RETURN pl.name AS location, e.start AS date
ORDER BY date ASC;
```

### Time-overlap of major drought and settlement expansion
```cypher
MATCH (d:Event {type:"Drought"})-[:LOCATED_AT]->(r:Region)
MATCH (s:Event {type:"Settlement Expansion"})-[:LOCATED_AT]->(r)
WHERE d.start <= s.start <= d.end
RETURN r.name, d.title, s.title;
```

### Spatial clustering of events
```cypher
MATCH (e:Event)
WHERE e.lat IS NOT NULL AND e.lon IS NOT NULL
RETURN e.type, avg(e.lat) AS centroid_lat, avg(e.lon) AS centroid_lon, count(e) AS count
ORDER BY count DESC;
```

---

## 🧩 Directory Layout

```plaintext
src/graph/queries/
├── README.md                # This documentation
├── focus_mode.cql           # Focus Mode subgraph templates
├── analytics.cql            # Statistical and network analytics queries
├── governance.cql           # Provenance and ledger verification
├── faircare_audit.cql       # FAIR+CARE compliance validation
└── spatiotemporal.cql       # Chronological and spatial pattern detection
```

---

## 🧪 Validation & Telemetry

| Metric | Description | Verified By |
|--------|--------------|-------------|
| **Query Execution Time** | Mean runtime for standard queries | @kfm-ops |
| **Focus Retrieval Coverage** | % of entities with valid subgraph output | @kfm-ai |
| **Governance Completeness** | % of nodes with checksum + ledger hash | @kfm-governance |
| **FAIR+CARE Field Integrity** | Missing ethical metadata fields | @faircare-council |
| **Query Schema Drift** | Detected outdated labels/relations | @kfm-validation |

Telemetry output → `../../../reports/audit/graph_query_metrics.json`

---

## 🧾 Internal Citation

```text
Kansas Frontier Matrix (2025). Graph Queries & Analytical Patterns (v10.1.0).
Template library of Cypher queries enabling explainable AI, Focus Mode reasoning, FAIR+CARE audits, and governance verification.
```

---

## 🕰️ Version History

| Version | Date | Summary |
|----------|------|----------|
| **v10.1.0** | 2025-11-10 | Added temporal correlation queries, Focus Transformer v2 summary integration, and FAIR+CARE audit patterns. |
| **v10.0.0** | 2025-11-08 | Refined analytics suite and governance queries; aligned Cypher with Neo4j 5.x. |
| **v9.7.0** | 2025-11-05 | Initial template set for Focus Mode and graph exploration. |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — MIT License**  
*Explainable AI × FAIR+CARE Analytics × Ethical Knowledge Retrieval*  
[Back to Graph README](../README.md) · [Docs Portal](../../../docs/) · [Governance Ledger](../../../docs/standards/governance/DATA-GOVERNANCE.md)

</div>

