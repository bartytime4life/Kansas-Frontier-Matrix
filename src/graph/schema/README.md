---
title: "🧮 Kansas Frontier Matrix — Graph Schema & Ontology Mapping (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "src/graph/schema/README.md"
version: "v10.1.0"
last_updated: "2025-11-10"
review_cycle: "Continuous / Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../releases/v10.1.0/sbom.spdx.json"
manifest_ref: "../../../releases/v10.1.0/manifest.zip"
data_contract_ref: "../../../docs/contracts/data-contract-v3.json"
governance_ref: "../../../docs/standards/governance/DATA-GOVERNANCE.md"
telemetry_ref: "../../../releases/v10.1.0/focus-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/src-graph-schema-v3.json"
license: "MIT"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 🧮 **Kansas Frontier Matrix — Graph Schema & Ontology Mapping**
`src/graph/schema/README.md`

**Purpose:**  
Define and document the **Neo4j schema, ontology mappings, and constraint definitions** that structure KFM’s knowledge graph.  
Implements FAIR+CARE-aligned data semantics under **CIDOC CRM**, **GeoSPARQL**, **OWL-Time**, **PROV-O**, and **DCAT/STAC** interoperability.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP--DL%20v6.3-blueviolet)](../../../docs/standards/)
[![FAIR+CARE Certified](https://img.shields.io/badge/FAIR%2BCARE-Diamond%E2%81%B9%20%C3%98%20Certified-gold)](../../../docs/standards/faircare-validation.md)
[![License: MIT](https://img.shields.io/badge/License-MIT-green)](../../../LICENSE)
[![ISO 19115](https://img.shields.io/badge/ISO-19115%20Compliant-blue)]()
[![Neo4j Schema](https://img.shields.io/badge/Graph-Neo4j%20v5.x-lightgrey)]()

</div>

---

## 📘 Overview

This schema module defines the **structural backbone of the Kansas Frontier Matrix knowledge graph**, governing how entities and relationships are created, validated, and constrained.  
The design follows **ontology-first modeling**, ensuring interoperability with open standards and reproducibility across systems.

Every entity (node) and relation (edge) is defined according to a **FAIR+CARE ontology mapping**, ensuring clarity in meaning and ethical data representation.

---

## 🧩 Core Node Labels

| Label | Ontology | Description | Key Properties |
|-------|-----------|--------------|----------------|
| **Person** | CIDOC E21 | Individual, historical or modern. | `id`, `name`, `birth`, `death`, `group`, `checksum` |
| **Place** | CIDOC E53 / GeoSPARQL | Geographic location (point, region). | `id`, `name`, `lat`, `lon`, `geometry`, `iso_code` |
| **Event** | CIDOC E5 / OWL-Time | Occurrence at a specific place/time. | `id`, `title`, `type`, `start`, `end`, `description` |
| **Document** | CIDOC E31 | Written or recorded source. | `id`, `title`, `type`, `url`, `checksum`, `language` |
| **Organization** | CIDOC E74 | Entity representing a group or institution. | `id`, `name`, `role`, `founded`, `dissolved` |
| **Dataset** | DCAT / STAC | Structured dataset (raster, vector, tabular). | `id`, `title`, `license`, `spatial`, `temporal`, `url` |
| **Concept** | SKOS | Thematic or classification term. | `id`, `label`, `broader`, `narrower`, `definition` |

---

## 🔗 Relationship Types

| Relation | Source → Target | Ontology / Meaning |
|-----------|----------------|--------------------|
| **ATTENDED** | Person → Event | Participation or attendance of a person at an event. |
| **LOCATED_AT** | Event → Place | The geographical occurrence location of an event. |
| **MENTIONED_IN** | Event/Place → Document | A document references this entity. |
| **CREATED_BY** | Document → Organization | Provenance: who authored or issued the document. |
| **WITHIN** | Place → Region | Spatial containment or hierarchy (GeoSPARQL `sfWithin`). |
| **HAS_TYPE** | Event → Concept | Classification by category or ontology type. |
| **RECORDED_IN** | Event → Dataset | Source dataset containing event data (STAC link). |
| **RELATED_TO** | Any → Any | Generic semantic link (for cross-domain relation). |
| **PROV_WAS_GENERATED_BY** | Dataset/Document → Process | Provenance (PROV-O lineage). |

---

## ⚙️ Schema Constraints & Indexes

### Cypher Definitions (excerpts)
```cypher
// Unique constraints
CREATE CONSTRAINT unique_person_id IF NOT EXISTS
FOR (p:Person) REQUIRE p.id IS UNIQUE;

CREATE CONSTRAINT unique_place_id IF NOT EXISTS
FOR (pl:Place) REQUIRE pl.id IS UNIQUE;

CREATE CONSTRAINT unique_event_id IF NOT EXISTS
FOR (e:Event) REQUIRE e.id IS UNIQUE;

// Index for quick name lookup
CREATE INDEX idx_person_name IF NOT EXISTS FOR (p:Person) ON (p.name);
CREATE INDEX idx_place_name IF NOT EXISTS FOR (pl:Place) ON (pl.name);
CREATE INDEX idx_event_date IF NOT EXISTS FOR (e:Event) ON (e.start);
```

---

## 🧠 Ontology Alignment Matrix

| KFM Entity | CIDOC CRM / Standard | External Reference | Notes |
|-------------|----------------------|--------------------|-------|
| Person | E21 Person | CIDOC CRM | Links to related Events via `ATTENDED`. |
| Place | E53 Place | GeoSPARQL | Includes WKT geometry and CRS metadata. |
| Event | E5 Event | OWL-Time | Has temporal bounds and duration. |
| Document | E31 Document | PROV-O / DCAT | Tracks provenance and FAIR metadata. |
| Organization | E74 Group | FOAF / Schema.org | May create or fund Documents. |
| Dataset | DCAT Dataset / STAC Collection | OGC STAC | Includes metadata from `data/stac/`. |
| Concept | SKOS Concept | SKOS Core | Controlled vocabulary or taxonomy node. |

---

## 🧮 Directory Layout

```plaintext
src/graph/schema/
├── README.md              # Schema overview (this file)
├── ontology_map.ttl       # RDF/OWL ontology mapping file
├── neo4j_schema.cypher    # Graph schema definition scripts
├── constraints.cypher     # Index and uniqueness constraints
└── validations/
    ├── schema_drift.py    # Validates graph vs ontology
    └── checksum_audit.py  # Verifies node/edge integrity
```

---

## 🔍 Validation & Audit Hooks

| Validation Check | Tool / Script | Description |
|------------------|---------------|-------------|
| Schema Drift | `validations/schema_drift.py` | Ensures actual graph matches declared ontology. |
| Constraint Audit | `constraints.cypher` | Verifies indexes and uniqueness constraints. |
| FAIR+CARE Audit | `src/pipelines/validation/graph_ethics.py` | Ensures no missing metadata or attribution. |
| Provenance Sync | `src/graph/ingest/sync_provenance.py` | Updates blockchain & IPFS records. |

Reports generated under `../../../reports/audit/graph_schema_audit.json`.

---

## 🧾 Internal Citation

```text
Kansas Frontier Matrix (2025). Graph Schema & Ontology Mapping (v10.1.0).
Defines Neo4j schema, ontology alignment, and FAIR+CARE constraints for Kansas Frontier Matrix knowledge graph.
```

---

## 🕰️ Version History

| Version | Date | Summary |
|----------|------|----------|
| **v10.1.0** | 2025-11-10 | Updated CIDOC CRM mappings; added PROV-O and DCAT 3.0 interoperability; new schema drift validator. |
| **v10.0.0** | 2025-11-08 | Introduced full Neo4j v5 schema with constraints and FAIR+CARE field alignment. |
| **v9.7.0** | 2025-11-05 | Migrated to STAC/DCAT dataset representation; improved ontology_map.ttl structure. |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — MIT License**  
*Ontology Integration × FAIR+CARE Compliance × Provenance Assurance*  
[Back to Graph README](../README.md) · [Docs Portal](../../../docs/) · [Governance Ledger](../../../docs/standards/governance/DATA-GOVERNANCE.md)

</div>

