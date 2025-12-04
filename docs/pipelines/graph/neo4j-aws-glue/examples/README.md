---
title: "📂 KFM v11.2.3 — Neo4j Glue Job Examples (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
description: "Governed example jobs and configs for the Neo4j Connector for AWS Glue, demonstrating KFM-compliant SQL→Cypher graph ingestion patterns."
path: "docs/pipelines/graph/neo4j-aws-glue/examples/README.md"
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

doc_kind: "Pipeline Examples"
intent: "graph-ingestion-neo4j-aws-glue-examples"

fair_category: "F1-A1-I1-R1"
care_label: "CARE-Compliant"
sensitivity: "General"
sensitivity_level: "Low"
indigenous_data_flag: false
public_benefit_level: "High"
risk_category: "Low"
redaction_required: false

ontology_alignment:
  schema_org: "SoftwareSourceCode"
  cidoc: "E29 Design or Procedure"
  prov_o: "prov:Plan"
  owl_time: "TemporalEntity"
  geosparql: "geo:FeatureCollection"

json_schema_ref: "../../../../../schemas/json/pipelines-graph-neo4j-aws-glue-examples-v1.json"
shape_schema_ref: "../../../../../schemas/shacl/pipelines-graph-neo4j-aws-glue-examples-v1.shape.ttl"

immutability_status: "version-pinned"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"

ttl_policy: "24 Months"
sunset_policy: "Superseded on next major example suite revision"
---

<div align="center">

# 📂 Neo4j Glue Job Examples — SQL→Cypher Graph Ingest  
`docs/pipelines/graph/neo4j-aws-glue/examples/README.md`

**Purpose:**  
Provide **governed, ready-to-adapt example jobs** for the **Neo4j Connector for AWS Glue**, showing how to implement **KFM-compliant SQL→Cypher graph ingestion** for:

- Node loads (entity creation/upsert)  
- Relationship loads (edges with endpoints)  
- Contract-driven configuration via YAML  

</div>

---

## 🗂️ 1. Directory Layout (Examples Suite)

~~~text
docs/pipelines/graph/neo4j-aws-glue/examples/
│
├── 📄 README.md                       # This file — examples overview & usage
│
├── 🧪 glue-job-node-load.py           # Example Glue job for node ingestion
├── 🧪 glue-job-relationship-load.py   # Example Glue job for relationship ingestion
└── 🧾 job-config.yaml                 # Declarative config for both jobs (labels, keys, mappings)
~~~

**Directory contract:**

- `glue-job-node-load.py` and `glue-job-relationship-load.py` are **reference implementations**, not throwaway snippets.  
- `job-config.yaml` is the **single source of truth** for:
  - Node labels / relationship types  
  - Keys & property mappings  
  - Source datasets and paths  
  - Provenance and telemetry tags  

Projects deriving from these examples MUST keep the **config-driven structure** and should not hard-code graph semantics in code.

---

## 🧩 2. Example Config (`job-config.yaml`)

At a high level, `job-config.yaml` expresses **graph contracts** in a way that can be validated against:

- `schemas/node-contract.schema.json`  
- `schemas/relationship-contract.schema.json`  
- `schemas/provenance-mapping.json`

Conceptual structure (illustrative only):

~~~yaml
graph:
  target:
    uri: "jdbc:neo4j://neo4j.kfm.internal:7687"
    database: "kfm"
    connection_name: "kfm-neo4j-glue-connection"

nodes:
  - id: "person_nodes_v1"
    label: "Person"
    source:
      kind: "s3-csv"
      path: "s3://kfm/raw/persons.csv"
    identity:
      keys: ["person_id"]
    properties:
      person_id: "personId"
      first_name: "firstName"
      last_name: "lastName"
      birth_year: "birthYear"
    provenance:
      dataset_id: "urn:kfm:dataset:persons-v1"
      domain: "socioeconomic"

relationships:
  - id: "person_lives_in_region_v1"
    type: "LIVES_IN"
    source:
      kind: "s3-csv"
      path: "s3://kfm/raw/person_region.csv"
    start_node:
      label: "Person"
      match_keys:
        person_id: "personId"
    end_node:
      label: "Region"
      match_keys:
        region_code: "regionCode"
    properties:
      from_year: "fromYear"
      to_year: "toYear"
    provenance:
      dataset_id: "urn:kfm:dataset:person-region-v1"
      domain: "socioeconomic"
~~~

**Key principles:**

- **No Cypher in config.** The SQL→Cypher translator + contract schemas generate Cypher.  
- All semantics are **explicit** and **machine-checkable**.

---

## ⚛️ 3. Node Load Example (`glue-job-node-load.py`)

This job shows how to:

- Read a tabular source from S3.  
- Apply basic transformations in Glue.  
- Write to Neo4j via the connector, guided by `job-config.yaml`.

Conceptual pattern:

~~~python
import sys
import yaml
from awsglue.context import GlueContext
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext

args = getResolvedOptions(sys.argv, ["JOB_NAME", "JOB_CONFIG_S3_URI"])
sc = SparkContext()
glue_context = GlueContext(sc)
spark = glue_context.spark_session

# 1. Load job config
job_config_path = args["JOB_CONFIG_S3_URI"]  # e.g., s3://kfm-config/neo4j/job-config.yaml
job_config = yaml.safe_load(
    spark.read.text(job_config_path).collect()[0]["value"]
)  # simplistic; real code should be more robust

person_cfg = next(n for n in job_config["nodes"] if n["id"] == "person_nodes_v1")

# 2. Read source data
df = spark.read.format("csv").option("header", "true").load(person_cfg["source"]["path"])

# 3. Optional: domain-specific transformations (cleaning, type-casting, etc.)

# 4. Write to Neo4j via JDBC + SQL→Cypher
(
    df.write
      .format("jdbc")
      .option("driver", "org.neo4j.jdbc.Neo4jDriver")
      .option("url", person_cfg["graph"]["target"]["uri"] if "graph" in person_cfg else job_config["graph"]["target"]["uri"])
      .option("dbtable", person_cfg["label"])  # label used by translator / contract
      .save()
)
~~~

> **Note:**  
> Actual KFM code should use **utility functions** to resolve config, handle type casting, and attach provenance; the above is intentionally minimal.

---

## 🧷 4. Relationship Load Example (`glue-job-relationship-load.py`)

This job demonstrates:

- Matching start and end nodes by keys.  
- Creating/updating relationships according to the **relationship contract**.  
- Maintaining deterministic behavior via MERGE semantics.

Conceptual pattern:

~~~python
import sys
import yaml
from awsglue.context import GlueContext
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext

args = getResolvedOptions(sys.argv, ["JOB_NAME", "JOB_CONFIG_S3_URI"])
sc = SparkContext()
glue_context = GlueContext(sc)
spark = glue_context.spark_session

job_config = yaml.safe_load(
    spark.read.text(args["JOB_CONFIG_S3_URI"]).collect()[0]["value"]
)

rel_cfg = next(r for r in job_config["relationships"] if r["id"] == "person_lives_in_region_v1")

df = spark.read.format("csv").option("header", "true").load(rel_cfg["source"]["path"])

(
    df.write
      .format("jdbc")
      .option("driver", "org.neo4j.jdbc.Neo4jDriver")
      .option("url", job_config["graph"]["target"]["uri"])
      .option("dbtable", rel_cfg["type"])     # relationship type consumed by translator/contract
      .save()
)
~~~

The **SQL→Cypher translator + ingest contracts** ensure that:

- `Person` and `Region` nodes are matched using the configured keys.  
- `LIVES_IN` relationships are MERGEd between them with correct properties.  
- No duplicate edges are created if jobs are re-run with the same inputs.

---

## 🧪 5. How to Use These Examples in Your Own Pipelines

1. **Copy & rename** the example scripts into your own job directory (or repo).  
2. **Create a new `job-config.yaml`**:
   - Define new `nodes` and `relationships` entries for your datasets.  
   - Ensure keys, labels/types, and source paths are correct.  
3. **Update schemas** (if needed):
   - Update or extend `node-contract.schema.json` / `relationship-contract.schema.json` to cover new patterns.  
4. **Wire into Glue**:
   - Upload scripts + config to S3 or commit them into a job repository.  
   - Configure Glue jobs to point at the scripts and pass `JOB_CONFIG_S3_URI` as an argument.  
5. **Run tests**:
   - Add or adapt test cases in `tests/test-sql-to-cypher.yaml`.  
   - Ensure CI passes before production use.

---

## 🛡️ 6. Governance, FAIR+CARE & Safety Considerations

Even example jobs must respect KFM governance:

- **No hard-coded sensitive URIs** (use synthetic or non-sensitive sources in examples).  
- **No PII** or sensitive site-level data in example CSVs.  
- Configs should illustrate:
  - Use of KFM dataset IDs, domains, and regions (synthetic examples are fine).  
  - Proper provenance mapping fields.

When adapting examples for real data:

- Confirm that graph nodes/edges align with:
  - PROV-O models.  
  - FAIR+CARE & sovereignty policies.  
  - KFM graph ontology (labels, relationship types, properties).

---

## 🕰️ 7. Version History (Examples)

| Version  | Date       | Author                               | Summary                                                                 |
|----------|------------|--------------------------------------|-------------------------------------------------------------------------|
| v11.2.3  | 2025-12-03 | Graph Systems WG · FAIR+CARE Council | Initial example suite for Neo4j Connector for AWS Glue; added node & relationship job patterns and config-driven contracts aligned with parent pipeline README. |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — MIT**  
FAIR+CARE Certified · MCP-DL v6.3 · KFM-MDP v11.2.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[⬅ Back to Neo4j Glue Integration](../README.md) · [⬅ Back to Graph Pipelines Index](../README.md)

</div>

