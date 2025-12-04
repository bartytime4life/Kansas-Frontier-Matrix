---
title: "📌 KFM v11.2.3 — Expected Graph Snapshots for Neo4j Glue Integration Tests (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
description: "Golden expected node and relationship snapshots used as oracles for Neo4j Connector for AWS Glue integration tests in the Kansas Frontier Matrix."
path: "docs/pipelines/graph/neo4j-aws-glue/tests/integration/fixtures/expected/README.md"
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
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../../../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../../../../../../../releases/v11.2.3/manifest.zip"
telemetry_ref: "../../../../../../../../releases/v11.2.3/graph-ingest-telemetry.json"
telemetry_schema: "../../../../../../../schemas/telemetry/graph-ingestion-v1.json"

governance_ref: "../../../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.3"

doc_kind: "Test Fixtures Overview"
intent: "graph-ingestion-neo4j-aws-glue-integration-expected-snapshots"

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

json_schema_ref: "../../../../../../../schemas/json/pipelines-graph-neo4j-aws-glue-tests-integration-expected-readme-v1.json"
shape_schema_ref: "../../../../../../../schemas/shacl/pipelines-graph-neo4j-aws-glue-tests-integration-expected-readme-v1.shape.ttl"

immutability_status: "version-pinned"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"

ttl_policy: "24 Months"
sunset_policy: "Superseded on next major expected-fixture revision"
---

<div align="center">

# 📌 Expected Graph Snapshots — Neo4j Glue Integration Tests  
`docs/pipelines/graph/neo4j-aws-glue/tests/integration/fixtures/expected/README.md`

**Purpose:**  
Describe the **golden expected node and relationship snapshots** used as **oracles** for Neo4j Connector for AWS Glue integration tests.  
These expected outputs are compared against the actual Neo4j graph after ingest to verify:

- Correct node and relationship creation  
- Contract adherence (labels, keys, properties)  
- Idempotency and governance-safe behavior  

</div>

---

## 🗂️ 1. Directory Layout (Expected Snapshots)

~~~text
docs/pipelines/graph/neo4j-aws-glue/tests/integration/fixtures/expected/
│
├── 📄 README.md              # This file — expected snapshot overview
│
├── 📄 nodes.json             # Expected Person/Region nodes (labels, keys, properties)
└── 📄 relationships.json     # Expected LIVES_IN/NEIGHBORS relationships & properties
~~~

**Directory contract:**

- `nodes.json` and `relationships.json` are considered **canonical expected outputs** for the integration fixture suite.  
- Integration tests MUST treat these files as **read-only oracles**, not as generated artifacts.  
- Any change to these files must be treated as a **governed change in graph behavior**.

---

## 🧱 2. `nodes.json` — Expected Nodes

`nodes.json` encodes the expected node set after running the test ingestion jobs against the synthetic fixture inputs (`persons.csv`, `regions.csv`).

### 2.1 Conceptual Structure

A recommended pattern is a JSON object keyed by label:

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

**Requirements:**

- Each node entry MUST include:
  - The **key properties** defined in `job-config.yaml` (e.g., `personId`, `regionCode`).  
  - Any additional properties that tests rely on (e.g., `firstName`, `regionName`).

- Tests may:
  - Ignore extra properties in the graph that are not present in `nodes.json`.  
  - Or assert strict equality, depending on the chosen comparison strategy.

**Idempotency check:**

- After re-running ingest jobs with identical inputs, the node set should remain **identical** to `nodes.json` (no duplicates, no unexpected deletions).

---

## 🔗 3. `relationships.json` — Expected Relationships

`relationships.json` encodes the expected relationships between nodes.

### 3.1 Conceptual Structure

A recommended pattern is a JSON object keyed by relationship type:

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

**Requirements:**

- Each relationship entry MUST include:
  - `start` — identifying the start node (label + key properties).  
  - `end` — identifying the end node.  
  - `properties` — any relationship properties asserted by tests (e.g., `fromYear`, `toYear`).

- Tests should verify that:
  - The actual graph contains relationships matching all entries in `relationships.json`.  
  - No extra relationships of the same type/keys exist (unless explicitly allowed).  
  - Re-running ingestion jobs does not produce **duplicate relationships**.

---

## 🧪 4. How Tests Use Expected Snapshots

Integration test harnesses typically:

1. **Run node and relationship ingestion jobs** using fixture CSVs.  
2. **Query Neo4j** to extract the actual graph state:
   - Nodes by label and keys.  
   - Relationships by type, start/end keys, and properties.  
3. **Normalize** the output:
   - Sort arrays by key fields.  
   - Normalize property types (e.g., string vs number where appropriate).  
4. **Compare** normalized actual outputs to:
   - `nodes.json` for node snapshots.  
   - `relationships.json` for relationship snapshots.  
5. **Assert idempotency**:
   - Re-run the jobs and ensure the graph still matches the expected snapshots.

All comparison logic should live in test code; this directory only defines **what** is expected, not **how** to compare.

---

## 🛡️ 5. Governance & FAIR+CARE for Expected Snapshots

Even though these snapshots are test artifacts:

- They must represent only **synthetic data**, with no real PII or sensitive identifiers.  
- They should be structurally **realistic** enough to exercise:
  - Multi-label node cases (if needed).  
  - Multiple relationship types (if later extended).  
  - Governance-consistent graph property patterns (e.g., `datasetId`, `domain`), when tests assert them.

If expected snapshots include governance-related properties (e.g., `datasetId`, `domain`):

- Use test-specific identifiers such as `urn:kfm:dataset:example-*`.  
- Do not reuse real production dataset IDs or sensitive domain/region slugs.

---

## 🧭 6. Change Management

Because `nodes.json` and `relationships.json` are **test oracles**:

- Any changes to these files must be treated as a **behavioral change** to the ingestion pattern.  
- Such changes should:
  - Be documented in `docs/pipelines/graph/neo4j-aws-glue/changelog.md`.  
  - Accompany updates to `job-config.yaml`, schemas, or ingestion code.  
  - Be reviewed by the Graph Systems WG for unintended regressions.

---

## 🕰️ 7. Version History

| Version  | Date       | Author                               | Summary                                                                 |
|----------|------------|--------------------------------------|-------------------------------------------------------------------------|
| v11.2.3  | 2025-12-03 | Graph Systems WG · FAIR+CARE Council | Initial expected snapshots overview for Neo4j Glue integration tests; documented structure and governance rules for `nodes.json` and `relationships.json`. |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — MIT**  
FAIR+CARE Certified · MCP-DL v6.3 · KFM-MDP v11.2.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[⬅ Back to Fixtures](../README.md) · [⬅ Back to Integration Tests](../README.md) · [⬅ Back to Neo4j Glue Integration](../../../../README.md)

</div>

