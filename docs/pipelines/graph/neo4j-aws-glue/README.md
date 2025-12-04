---
title: "🔗 KFM v11.2.3 — Neo4j Connector for AWS Glue (SQL→Cypher Translation · Serverless Graph Ingest) (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
description: "Governed integration pattern for using AWS Glue as a serverless SQL→Cypher translator to ingest relational and tabular data into Neo4j for the Kansas Frontier Matrix."
path: "docs/pipelines/graph/neo4j-aws-glue/README.md"
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
doc_integrity_checksum: "<sha256-of-this-file>"

sbom_ref: "../../../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../../../releases/v11.2.3/manifest.zip"
telemetry_ref: "../../../../releases/v11.2.3/graph-ingest-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/graph-ingestion-v1.json"

governance_ref: "../../../../docs/standards/governance/ROOT-GOVERNANCE.md"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.3"

doc_kind: "Pipeline Overview"
intent: "graph-ingestion-neo4j-aws-glue"

fair_category: "F1-A1-I1-R1"
care_label: "CARE-Compliant"
sensitivity: "General"
sensitivity_level: "Low"
indigenous_data_flag: false
public_benefit_level: "High"
risk_category: "Low"
redaction_required: false

ontology_alignment:
  schema_org: "SoftwareApplication"
  cidoc: "E29 Design or Procedure"
  prov_o: "prov:Plan"
  owl_time: "TemporalEntity"
  geosparql: "geo:FeatureCollection"

json_schema_ref: "../../../../schemas/json/pipelines-graph-neo4j-aws-glue-readme-v1.json"
shape_schema_ref: "../../../../schemas/shacl/pipelines-graph-neo4j-aws-glue-readme-v1.shape.ttl"

immutability_status: "version-pinned"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"

ttl_policy: "24 Months"
sunset_policy: "Superseded on next major Neo4j Glue integration revision"
---

<div align="center">

# 🔗 Neo4j Connector for AWS Glue  
**Serverless SQL→Cypher Translator · KFM v11 Graph Ingestion**  
`docs/pipelines/graph/neo4j-aws-glue/README.md`

**Purpose:**  
Define the **KFM-governed integration pattern** for using the **Neo4j Connector for AWS Glue** as a **serverless SQL→Cypher translator**, enabling deterministic, FAIR+CARE-compliant ingestion of relational and tabular data into Neo4j (AuraDB or self-hosted).

</div>

---

## 🧭 1. Overview & Purpose

KFM ingests large, heterogeneous datasets across:

- Archaeology & heritage  
- Hydrology & rivers  
- Climate & atmosphere  
- Remote sensing & imagery  
- State archives and tabular reference data  

Many of these originate in:

- JDBC-accessible databases (RDS, Aurora, Redshift, Snowflake, PostgreSQL, MySQL)  
- S3 objects (CSV, Parquet, JSON) via Glue Data Catalog  
- NoSQL sources (DynamoDB) via Glue DynamicFrames  

The **AWS Glue → Neo4j Connector** enables KFM v11 pipelines to:

- Build **nodes and relationships** from tabular/relational data using Glue transformations.  
- Translate Glue-generated SQL into **Cypher MERGE/CREATE** via a Neo4j JDBC SQL translator.  
- Enforce **graph ingestion contracts**, provenance, and reproducibility.  
- Use **managed, serverless ETL** instead of bespoke ingestion code.

This document governs:

- Directory layout & artifacts  
- How SQL→Cypher translation works  
- Graph modeling contracts  
- Deployment, provenance, CI, and telemetry expectations

---

## 🗂️ 2. Directory Layout (Emoji-Prefix Standard · v11.2.3)

~~~text
docs/pipelines/graph/neo4j-aws-glue/
│
├── 📄 README.md                                  # This document (governed integration overview)
│
├── 🗂️ examples/                                  # Fully governed sample Glue job definitions
│   ├── glue-job-node-load.py                     # Example: node ingestion job
│   ├── glue-job-relationship-load.py             # Example: relationship ingestion job
│   └── job-config.yaml                           # Declarative job configuration (per KFM contract)
│
├── 🧩 schemas/                                   # Graph ingestion contracts & mappings
│   ├── node-contract.schema.json                 # Node ingestion contract (labels, keys, props)
│   ├── relationship-contract.schema.json         # Relationship contract (types, endpoints, props)
│   └── provenance-mapping.json                   # Mapping from Glue context → PROV-O graph fields
│
├── 🧪 tests/                                     # SQL→Cypher translation & ingest validation
│   ├── test-sql-to-cypher.yaml                   # Golden test cases for SQL↔Cypher expectations
│   └── integration/                              # Integration harnesses (optional)
│
└── 📜 changelog.md                               # Version history for this pipeline pattern
~~~

**Directory contract:**

- `examples/` and `schemas/` are **normative** for how jobs must be structured.  
- `tests/` MUST contain at least one CI-driven translation test before pipeline activation.  
- `changelog.md` tracks **breaking and non-breaking** changes to the integration pattern.

---

## ⚙️ 3. How the Connector Works (SQL→Cypher Translation)

### 3.1 Core Mechanism

The connector provides a **custom JDBC driver** for AWS Glue:

1. Glue jobs operate over **DynamicFrames/DataFrames**.  
2. Glue generates **SQL** (internally or via `.format("jdbc")` writes).  
3. The **Neo4j JDBC driver** intercepts SQL statements.  
4. A **SQL→Cypher translator** rewrites SQL into Cypher.  
5. Neo4j executes Cypher (`MERGE`/`CREATE`/`MATCH`) against the configured database.

High-level flow:

~~~text
Glue Transformations → SQL → Neo4j JDBC → SQL→Cypher Translation → Cypher → Neo4j Graph
~~~

### 3.2 Supported SQL Operations

The translator supports a constrained SQL subset:

- `SELECT`  
- `INSERT`  
- `UPDATE`  
- `DELETE`  
- UPSERT/`MERGE`-equivalent patterns (implemented via `MERGE` + `ON MATCH/CREATE` in Cypher)

**KFM requirement:**  
- Unsupported SQL constructs MUST produce **fail-fast** Glue job errors, not partial graph updates.

---

## 🧱 4. KFM Graph Modeling & Ingestion Contracts

KFM mandates **explicit, deterministic graph modeling** for every ingestion job.

### 4.1 Required Contract Fields (per Job)

Each ingestion job (node or relationship) MUST specify, at minimum:

- **Identity & Topology**
  - `node_label` or `relationship_type`  
  - Deterministic ID or natural primary key(s)  
  - Source table/columns → graph ID mapping

- **Schema Mapping**
  - Column → property mapping  
  - Type conversions (numeric, string, temporal, spatial)  
  - Null-handling rules

- **Provenance & Governance**
  - Ingestion timestamp  
  - Glue Job Name + Job Run ID / UUID  
  - Source system and data paths (JDBC URL, S3 URIs)  
  - KFM dataset IDs / region slugs (where applicable)  
  - Versioning metadata (e.g., `graph_ingest_version`, `schema_version`)

These MUST be captured in:

- `schemas/node-contract.schema.json`  
- `schemas/relationship-contract.schema.json`  
- `schemas/provenance-mapping.json`

and materialized as **graph properties** + **PROV-O entities/activities**.

### 4.2 Idempotency & Determinism

- Node and relationship MERGEs MUST be **idempotent** given the same inputs.  
- Contracts must specify:
  - Which field(s) form the **graph identity**.  
  - How updates are applied (e.g., overwrite vs append semantics).

---

## 🚀 5. Deployment & Configuration Overview

### 5.1 Connector JAR Placement (S3)

Upload the Neo4j Glue connector JAR into KFM artifacts bucket:

~~~text
s3://kfm-artifacts/connectors/neo4j-glue-driver.jar
~~~

### 5.2 Register as a Glue Connection

In **AWS Glue Studio**:

- Connection type: `Custom JDBC`  
- Driver class: `org.neo4j.jdbc.Neo4jDriver`  
- JDBC URL example:

  ~~~text
  jdbc:neo4j://neo4j.kfm.internal:7687
  ~~~

- Additional connection options:

  ~~~text
  enableSQLTranslation=true
  ~~~

(Option names may differ by driver version; follow connector docs and KFM schemas.)

### 5.3 Minimal Glue Job Pattern (Conceptual)

~~~python
# examples/glue-job-node-load.py (conceptual pattern)
nodes = spark.read.format("csv") \
    .option("header", "true") \
    .load("s3://kfm/raw/nodes.csv")

nodes.write \
    .format("jdbc") \
    .option("driver", "org.neo4j.jdbc.Neo4jDriver") \
    .option("url", "jdbc:neo4j://neo4j.kfm.internal:7687") \
    .option("dbtable", "Person") \
    .save()
~~~

Glue emits SQL → Neo4j JDBC translates → Neo4j runs Cypher according to the configured contracts.

> **KFM note:**  
> Real jobs MUST pull `node_label`, keys, and property mappings from **job-config.yaml** and **schema contracts**, not hard-code them.

---

## 📐 6. Provenance, FAIR+CARE & PROV-O Alignment

Graph ingestion is a **governed activity** in KFM:

- Every Glue → Neo4j job must produce PROV-O records capturing:
  - Input entities (tables, S3 objects, source datasets).  
  - Activities (Glue job runs, transformation steps).  
  - Output entities (graph nodes/relationships, summaries).

### 6.1 Required Provenance Data

For each job run, record:

- Glue Job Name, Run ID, version/commit.  
- Input source URIs (JDBC URLs, S3 prefixes).  
- Checksums or manifest hashes of input data (where feasible).  
- Node/relationship counts created/updated/deleted.  
- Timestamps (start, end, duration).  
- Error/failure summaries (if any).  
- Graph target (Neo4j host/db, AuraDB vs self-hosted).

### 6.2 FAIR+CARE Alignment

- Graph representation must be consistent with:
  - Dataset-level FAIR+CARE metadata.  
  - Sovereignty constraints for sensitive data (e.g., site-level or personal data).

- If a dataset is flagged as sensitive:
  - Jobs must apply **filtering, aggregation, or masking** before inserting into shared graphs.  
  - Redaction rules must be captured in provenance (PROV-O) and job-config metadata.

---

## 🧪 7. Validation & CI/CD

KFM CI/CD MUST validate the integration pattern before jobs are allowed in production.

### 7.1 SQL→Cypher Translation Tests

- `tests/test-sql-to-cypher.yaml` contains **golden pairs**:
  - Input SQL  
  - Expected Cypher  
- CI runs translation tests to ensure:
  - Stable, deterministic mappings.  
  - No unexpected SQL patterns slip through untested.

### 7.2 Graph Contract Validation

Before deploying or updating jobs:

- Validate `node-contract.schema.json` and `relationship-contract.schema.json`:
  - Required fields present (labels/types, keys, mappings).  
  - No ambiguous IDs.  
  - Provenance mapping is complete.

### 7.3 Integration Tests (Optional but Recommended)

Under `tests/integration/`:

- Smoke tests that:
  - Run a small Glue job against a **test Neo4j database**.  
  - Assert node/relationship counts and key properties.

---

## 📊 8. Telemetry & Monitoring

All Glue → Neo4j jobs must emit telemetry to:

- **OpenTelemetry (OTLP)**  
- **KFM Reliability Spans** (graph-ingest spans)  
- Neo4j query logs / metrics  
- Carbon/Energy telemetry streams

### 8.1 Key Metrics

- `translation_success_rate` — SQL→Cypher translation success ratio.  
- `cypher_execution_latency` — p50/p95/p99 execution times.  
- `node_create_rate`, `relationship_create_rate`.  
- Unique/constraint violation counts.  
- Job-level status (success/failure) and retry counts.

These metrics support:

- Capacity planning for Neo4j.  
- Early detection of ingest regressions.  
- Carbon/energy accounting for graph workloads.

---

## 🔄 9. Refresh & Auto-Update Patterns

KFM supports multiple refresh patterns driven by Glue triggers:

- **Nightly rebuilds** — periodic re-materialization of graph subsets from source systems.  
- **Weekly partial updates** — incremental refresh of frequently changing entities.  
- **Monthly full re-index** — deeper recomputation of graph structures for analytical workloads.  
- **Redaction-safe increments** — targeted updates honoring new governance rules (e.g., remove or generalize sensitive nodes/edges).

**Best practice:**

- Encode schedule and refresh strategy in job metadata and provenance.  
- Ensure that jobs are **idempotent** and safe to re-run within the same time window.

---

## 🕰️ 10. Version History

| Version  | Date       | Author                               | Summary                                                                 |
|----------|------------|--------------------------------------|-------------------------------------------------------------------------|
| v11.2.3  | 2025-12-03 | Graph Systems WG · FAIR+CARE Council | Initial KFM-aligned Neo4j Connector for AWS Glue integration; defined directory layout, SQL→Cypher behavior, graph ingestion contracts, provenance, CI, and telemetry expectations. |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — MIT**  
FAIR+CARE Certified · MCP-DL v6.3 · KFM-MDP v11.2.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[⬅ Back to Graph Pipelines Index](../README.md) · [📜 Governance Charter](../../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>

