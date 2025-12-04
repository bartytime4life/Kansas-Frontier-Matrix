---
title: "🧩 KFM v11.2.3 — Neo4j Glue Graph Ingestion Schemas (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
description: "Schema contracts for node, relationship, and provenance mappings used by the Neo4j Connector for AWS Glue graph ingestion pipelines in the Kansas Frontier Matrix."
path: "docs/pipelines/graph/neo4j-aws-glue/schemas/README.md"
version: "v11.2.3"
last_updated: "2025-12-03"

release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Graph Systems · FAIR+CARE Council"
content_stability: "stable"
backward_compatibility: "v10.x → v11.x graph-ingestion-contract compatible"
status: "Active / Enforced"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.2.3/manifest.zip"
telemetry_ref: "../../../../../releases/v11.2.3/graph-ingest-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/graph-ingestion-v1.json"

governance_ref: "../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.3"

doc_kind: "Schema Overview"
intent: "graph-ingestion-neo4j-aws-glue-schemas"

fair_category: "F1-A1-I1-R1"
care_label: "CARE-Compliant"
sensitivity: "General"
sensitivity_level: "Low"
indigenous_data_flag: false
public_benefit_level: "High"
risk_category: "Low"
redaction_required: false

ontology_alignment:
  schema_org: "Dataset"
  cidoc: "E29 Design or Procedure"
  prov_o: "prov:Plan"
  owl_time: "TemporalEntity"
  geosparql: "geo:FeatureCollection"

json_schema_ref: "../../../../../schemas/json/pipelines-graph-neo4j-aws-glue-schemas-readme-v1.json"
shape_schema_ref: "../../../../../schemas/shacl/pipelines-graph-neo4j-aws-glue-schemas-readme-v1.shape.ttl"

immutability_status: "version-pinned"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"

ttl_policy: "24 Months"
sunset_policy: "Superseded on next major schema contract overhaul"
---

<div align="center">

# 🧩 Neo4j Glue Graph Ingestion Schemas  
`docs/pipelines/graph/neo4j-aws-glue/schemas/README.md`

**Purpose:**  
Define the **schema contracts** for KFM’s Neo4j Connector for AWS Glue integration:

- `node-contract.schema.json` — node ingestion contracts  
- `relationship-contract.schema.json` — relationship ingestion contracts  
- `provenance-mapping.json` — PROV-O and telemetry mapping  

These schemas make graph ingestion **deterministic, auditable, and FAIR+CARE-compliant**.

</div>

---

## 📘 1. Scope & Relationship to Parent Pipeline

This document is the schema companion to:

- `../README.md` — Neo4j Connector for AWS Glue integration overview  
- `../examples/README.md` — example job scripts & `job-config.yaml`  

Together they specify:

- **What** must be configured for a Glue → Neo4j ingestion job.  
- **How** configuration must be structured.  
- **How** Glue-generated SQL will be translated into Cypher in a governed way.

The files in this directory are **not sample data**; they are **contracts** that job configs and code must satisfy.

---

## 🗂️ 2. Directory Layout (Schemas)

~~~text
docs/pipelines/graph/neo4j-aws-glue/schemas/
│
├── 📄 README.md                         # This file — schema overview & contracts
│
├── 🧩 node-contract.schema.json         # Node ingestion contract schema (per-node job)
├── 🧩 relationship-contract.schema.json # Relationship ingestion contract schema
└── 🧩 provenance-mapping.json           # Mapping from Glue/runtime context → PROV-O graph fields
~~~

**Directory contract:**

- `node-contract.schema.json` and `relationship-contract.schema.json` MUST be used to validate:
  - `job-config.yaml` node/relationship entries.  
- `provenance-mapping.json` MUST document:
  - Which Glue runtime fields map to which PROV-O properties.  
  - How telemetry dimensions map into graph nodes/edges and/or external stores.

---

## 🧱 3. Node Ingestion Contract (`node-contract.schema.json`)

This schema defines the **required structure** of each `nodes[]` entry in `job-config.yaml`.

### 3.1 Required Concepts (Per Node Job)

Each node job MUST define:

- **Identity**
  - `id` — job identifier (e.g., `person_nodes_v1`).  
  - `label` — Neo4j label (e.g., `Person`, `Region`).  

- **Source**
  - `source.kind` — `s3-csv`, `jdbc`, `glue-catalog`, etc.  
  - `source.path` or connection details (URI, table name).

- **Identity keys**
  - `identity.keys[]` — mapping from source columns → graph properties used as **MERGE keys**.

- **Properties**
  - `properties` — mapping from source columns → graph property names.

- **Governance & provenance**
  - `governance.dataset_id` — KFM dataset ID (`urn:kfm:dataset:...`).  
  - `governance.domain` — KFM domain (e.g., `archaeology`, `hydrology`).  
  - `governance.release_stage` — `experimental`, `beta`, `stable`, `retired`.  
  - Optional `governance.region_slug`.  
  - `provenance` block — source paths, notes, and other provenance hints.

### 3.2 Example Shape (Conceptual)

> Final structure is governed by the JSON Schema; this is for orientation only.

~~~json
{
  "id": "person_nodes_v1",
  "label": "Person",
  "source": {
    "kind": "s3-csv",
    "path": "s3://kfm-example/raw/persons.csv",
    "options": {
      "header": true,
      "inferSchema": false
    }
  },
  "identity": {
    "keys": [
      {
        "source_column": "person_id",
        "graph_property": "personId"
      }
    ]
  },
  "properties": {
    "person_id": "personId",
    "first_name": "firstName",
    "last_name": "lastName"
  },
  "governance": {
    "dataset_id": "urn:kfm:dataset:example-persons-v1",
    "domain": "socioeconomic",
    "release_stage": "stable"
  },
  "provenance": {
    "source_paths": ["s3://kfm-example/raw/persons.csv"],
    "notes": "Synthetic example for Person nodes."
  }
}
~~~

---

## 🔗 4. Relationship Ingestion Contract (`relationship-contract.schema.json`)

This schema defines the structure of each `relationships[]` entry in `job-config.yaml`.

### 4.1 Required Concepts (Per Relationship Job)

Each relationship job MUST define:

- **Identity**
  - `id` — relationship job identifier (e.g., `person_lives_in_region_v1`).  
  - `type` — Neo4j relationship type (e.g., `LIVES_IN`, `NEIGHBORS`).

- **Source**
  - Same pattern as node jobs: `source.kind`, `source.path`, `source.options`.

- **Endpoints**
  - `start_node.label` — label of start node.  
  - `start_node.match_keys[]` — mapping from source columns → start-node key properties.  
  - `end_node.label` — label of end node.  
  - `end_node.match_keys[]` — mapping from source columns → end-node key properties.

- **Properties**
  - `properties` — mapping from source columns → relationship properties.

- **Governance & provenance**
  - `governance.dataset_id`, `governance.domain`, `governance.release_stage`.  
  - Optional `governance.region_slug`.  
  - `provenance` block — data sources, notes, etc.

### 4.2 Example Shape (Conceptual)

~~~json
{
  "id": "person_lives_in_region_v1",
  "type": "LIVES_IN",
  "source": {
    "kind": "s3-csv",
    "path": "s3://kfm-example/raw/person_region.csv",
    "options": {
      "header": true,
      "inferSchema": false
    }
  },
  "start_node": {
    "label": "Person",
    "match_keys": [
      {
        "source_column": "person_id",
        "graph_property": "personId"
      }
    ]
  },
  "end_node": {
    "label": "Region",
    "match_keys": [
      {
        "source_column": "region_code",
        "graph_property": "regionCode"
      }
    ]
  },
  "properties": {
    "from_year": "fromYear",
    "to_year": "toYear"
  },
  "governance": {
    "dataset_id": "urn:kfm:dataset:example-person-region-v1",
    "domain": "socioeconomic",
    "release_stage": "stable"
  },
  "provenance": {
    "source_paths": ["s3://kfm-example/raw/person_region.csv"],
    "notes": "Synthetic example for Person→Region relationships."
  }
}
~~~

---

## 🧬 5. Provenance Mapping (`provenance-mapping.json`)

This file specifies how **Glue runtime context** and **job-config fields** map onto **PROV-O** and KFM provenance structures.

### 5.1 Typical Mappings

Conceptual entries (actual JSON structure is governed by the file):

- `glue.job_name` → `prov:Activity prov:label`  
- `glue.job_run_id` → `prov:Activity prov:identifier`  
- `source_paths[]` → `prov:used` (input entities)  
- `dataset_id` → PROV-O entity representing the dataset  
- `ingested_nodes` / `ingested_relationships` → output entities and their counts

### 5.2 Usage

Downstream processes use `provenance-mapping.json` to:

- Attach ingestion activities to the **KFM provenance graph**.  
- Generate uniform logs/audit records.  
- Drive dashboards summarizing graph ingest lineage.

---

## 🧪 6. Validation & CI Expectations

KFM CI/CD MUST use these schemas to verify:

- **`job-config.yaml` correctness**:
  - Every `nodes[]` entry validates against `node-contract.schema.json`.  
  - Every `relationships[]` entry validates against `relationship-contract.schema.json`.  

- **Provenance coverage**:
  - Required provenance fields are present in each job config.  
  - `provenance-mapping.json` covers all required Glue runtime fields and mapping targets.

Indicative CI workflows:

- `graph-ingest-contract-validate.yml` — JSON Schema validation for contracts & job configs.  
- `graph-ingest-provenance-validate.yml` — checks that provenance mapping covers all required fields for PROV-O logging.

Builds MUST fail if:

- Contracts are missing required fields.  
- Job configs violate contract schemas.  
- Provenance mapping is incomplete or inconsistent.

---

## ✅ 7. Implementation Checklist

Before deploying or updating a Neo4j Glue job:

1. **Define/Update node & relationship entries** in `job-config.yaml`.  
2. **Validate `job-config.yaml`** against:
   - `node-contract.schema.json`  
   - `relationship-contract.schema.json`  
3. **Confirm provenance mapping** in `provenance-mapping.json` is sufficient.  
4. **Run CI**:
   - Contract + config validation jobs.  
   - SQL→Cypher tests using the contracts.  
5. **Record changes** in `../changelog.md` and, if necessary, bump schema versions.

---

## 🕰️ 8. Version History

| Version  | Date       | Author                               | Summary                                                                 |
|----------|------------|--------------------------------------|-------------------------------------------------------------------------|
| v11.2.3  | 2025-12-03 | Graph Systems WG · FAIR+CARE Council | Initial schema overview for Neo4j Glue graph ingestion; documented node, relationship, and provenance mapping contracts for KFM v11.2.3. |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — MIT**  
FAIR+CARE Certified · MCP-DL v6.3 · KFM-MDP v11.2.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[⬅ Back to Neo4j Glue Integration](../README.md) · [⬅ Back to Examples](../examples/README.md)

</div>

