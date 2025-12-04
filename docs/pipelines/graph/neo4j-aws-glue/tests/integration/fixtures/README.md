---
title: "📎 KFM v11.2.3 — Neo4j Glue Integration Test Fixtures (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
description: "Synthetic data and expected graph snapshots for end-to-end Neo4j Connector for AWS Glue integration tests in the Kansas Frontier Matrix."
path: "docs/pipelines/graph/neo4j-aws-glue/tests/integration/fixtures/README.md"
version: "v11.2.3"
last_updated: "2025-12-03"

release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Graph Systems · FAIR+CARE Council"
content_stability: "stable"
backward_compatibility: "v10.x → v11.x graph-ingestion-contract compatible"
status: "Active · Enforced"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256-of-this-file>"

sbom_ref: "../../../../../../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../../../../../../releases/v11.2.3/manifest.zip"
telemetry_ref: "../../../../../../../releases/v11.2.3/graph-ingest-telemetry.json"
telemetry_schema: "../../../../../../schemas/telemetry/graph-ingestion-v1.json"

governance_ref: "../../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.3"

doc_kind: "Test Fixtures Overview"
intent: "graph-ingestion-neo4j-aws-glue-integration-fixtures"

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
  prov_o: "prov:Entity"
  owl_time: "TemporalEntity"
  geosparql: "geo:FeatureCollection"

json_schema_ref: "../../../../../../schemas/json/pipelines-graph-neo4j-aws-glue-tests-integration-fixtures-readme-v1.json"
shape_schema_ref: "../../../../../../schemas/shacl/pipelines-graph-neo4j-aws-glue-tests-integration-fixtures-readme-v1.shape.ttl"

immutability_status: "version-pinned"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"

ttl_policy: "24 Months"
sunset_policy: "Superseded on next major integration fixtures revision"
---

<div align="center">

# 📎 Neo4j Glue Integration Test Fixtures  
`docs/pipelines/graph/neo4j-aws-glue/tests/integration/fixtures/README.md`

**Purpose:**  
Provide **synthetic, governed fixtures** (input data + expected graph snapshots) for the **Neo4j Connector for AWS Glue** integration tests, ensuring that:

- End-to-end graph ingest behavior is **testable and reproducible**  
- Node & relationship contracts can be validated against **known outputs**  
- No real PII, sensitive archaeology, or sovereign data is ever used in tests  

</div>

---

## 🗂️ 1. Directory Layout (Fixtures)

~~~text
docs/pipelines/graph/neo4j-aws-glue/tests/integration/fixtures/
│
├── 📄 README.md                     # This file — fixtures overview & governance rules
│
├── 📄 persons.csv                   # Synthetic Person node input
├── 📄 regions.csv                   # Synthetic Region node input
├── 📄 person_region.csv             # Synthetic Person→Region mapping input
│
└── 📁 expected/                     # Golden graph snapshots (post-ingest)
    ├── 📄 nodes.json                # Expected Person/Region nodes (labels, properties)
    └── 📄 relationships.json        # Expected LIVES_IN/NEIGHBORS relationships & properties
~~~

**Directory contract:**

- All data in this directory is **synthetic** and **non-sensitive**.  
- CSVs under the root are **inputs** to integration jobs.  
- Files under `expected/` are **oracles** for asserting the state of the test Neo4j graph.

---

## 📥 2. Input Fixture Semantics

### 2.1 `persons.csv` — Person Nodes

Represents synthetic **Person** records used to test node ingestion.

Typical columns (illustrative):

- `person_id` — synthetic ID, unique per row  
- `first_name`  
- `last_name`  
- `birth_year`  
- `gender` (if present, use generic, non-sensitive values)

These map to graph properties via:

- `job-config.yaml` under `nodes[]`  
- `node-contract.schema.json` in `schemas/`

### 2.2 `regions.csv` — Region Nodes

Represents synthetic **Region** entities.

Typical columns:

- `region_code` — short, synthetic region identifier  
- `region_name` — e.g., `"Region A"`, `"Region B"`  
- `region_type` — e.g., `"district"`, `"county"`, `"planning-area"`

These map to `:Region` nodes and their properties.

### 2.3 `person_region.csv` — Person→Region Relationships

Represents synthetic **Person → Region** relationships.

Typical columns:

- `person_id` — must match an ID in `persons.csv`  
- `region_code` — must match a code in `regions.csv`  
- `from_year` — relationship start year  
- `to_year` — relationship end year  
- Optional `source` — e.g., `"synthetic-survey"`

These map to relationships of type (for example) `:LIVES_IN` using:

- `relationships[]` entries in `job-config.yaml`  
- `relationship-contract.schema.json` in `schemas/`

---

## 📤 3. Expected Graph Snapshots (`expected/`)

The `expected/` subtree defines **canonical** outcomes for integration tests.

### 3.1 `expected/nodes.json`

Represents the expected set of nodes after ingest.

Suggested structure (conceptual):

~~~json
{
  "Person": [
    {
      "personId": "P001",
      "firstName": "Ada",
      "lastName": "Lovelace",
      "birthYear": 1815
    },
    {
      "personId": "P002",
      "firstName": "Alan",
      "lastName": "Turing",
      "birthYear": 1912
    }
  ],
  "Region": [
    {
      "regionCode": "R001",
      "regionName": "Region A",
      "regionType": "district"
    },
    {
      "regionCode": "R002",
      "regionName": "Region B",
      "regionType": "district"
    }
  ]
}
~~~

Test code is responsible for:

- Exporting nodes from Neo4j (e.g., via Cypher).  
- Normalizing output (ordering, type normalization).  
- Comparing against this structure.

### 3.2 `expected/relationships.json`

Represents the expected set of relationships after ingest.

Suggested structure (conceptual):

~~~json
{
  "LIVES_IN": [
    {
      "start": { "label": "Person", "personId": "P001" },
      "end":   { "label": "Region", "regionCode": "R001" },
      "properties": {
        "fromYear": 2020,
        "toYear": 2024
      }
    },
    {
      "start": { "label": "Person", "personId": "P002" },
      "end":   { "label": "Region", "regionCode": "R002" },
      "properties": {
        "fromYear": 2018,
        "toYear": 2025
      }
    }
  ]
}
~~~

Tests should verify:

- Count of relationships per type.  
- Correct linkage between start and end nodes.  
- Correct relationship properties.  
- Idempotency (re-running jobs does not create duplicates).

---

## 🛡️ 4. Governance & FAIR+CARE Constraints

Even in tests, KFM applies governance:

- Fixtures MUST NOT contain:
  - Real world PII  
  - Real archaeological site IDs or coordinates  
  - Sensitive infrastructure identifiers  

- For governance scenarios (e.g., “restricted-generalized” flows), tests should:
  - Use synthetic values but apply **real governance patterns** in configs (dataset IDs, domains, sensitivity flags).  
  - Validate that ingestion logic adheres to redaction/visibility rules.

Provenance for fixtures-based runs should:

- Use `urn:kfm:dataset:example-*` dataset IDs.  
- Clearly mark environment as `"ci"` or `"test"` in telemetry and provenance logs.

---

## 🧪 5. Using Fixtures in Integration Tests

Typical flow for an integration test harness:

1. **Bring up test Neo4j** (Docker or ephemeral service).  
2. **Make fixtures available**:
   - Upload `persons.csv`, `regions.csv`, `person_region.csv` to a test S3 bucket or mount them locally for Spark.  
3. **Run node ingestion job(s)** against `persons.csv` and `regions.csv`.  
4. **Run relationship ingestion job(s)** against `person_region.csv`.  
5. **Export graph state** from Neo4j.  
6. **Compare** exported graph to `expected/nodes.json` and `expected/relationships.json`.  
7. **Assert idempotency** by re-running jobs and verifying counts remain stable.  
8. **Tear down** test environment.

---

## 📊 6. Telemetry & Observability for Fixture-Based Tests

If integration tests emit telemetry:

- Tag telemetry as **non-production**:

  - `environment = "ci"` or `"test"`  
  - Dataset IDs like `urn:kfm:dataset:example-*`  

Use this telemetry to:

- Track performance characteristics of ingest patterns.  
- Catch regressions (e.g., slower ingest, more constraint violations).  
- Calibrate resource settings for production jobs.

No fixture-based telemetry should be interpreted as actual KFM usage.

---

## 🕰️ 7. Version History

| Version  | Date       | Author                               | Summary                                                                 |
|----------|------------|--------------------------------------|-------------------------------------------------------------------------|
| v11.2.3  | 2025-12-03 | Graph Systems WG · FAIR+CARE Council | Initial fixture overview for Neo4j Glue integration tests; documented synthetic CSV inputs, expected graph snapshots, governance constraints, and usage patterns. |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — MIT**  
FAIR+CARE Certified · MCP-DL v6.3 · KFM-MDP v11.2.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[⬅ Back to Integration Tests](../README.md) · [⬅ Back to Neo4j Glue Tests](../README.md) · [⬅ Back to Neo4j Glue Integration](../../../README.md)

</div>

