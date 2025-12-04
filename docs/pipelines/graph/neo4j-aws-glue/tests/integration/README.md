---
title: "🧪 KFM v11.2.3 — Neo4j Glue Integration Tests (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
description: "End-to-end integration test harness for the Neo4j Connector for AWS Glue, validating real graph ingest behavior against a test Neo4j instance under KFM contracts."
path: "docs/pipelines/graph/neo4j-aws-glue/tests/integration/README.md"
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

sbom_ref: "../../../../../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../../../../../releases/v11.2.3/manifest.zip"
telemetry_ref: "../../../../../../releases/v11.2.3/graph-ingest-telemetry.json"
telemetry_schema: "../../../../../../schemas/telemetry/graph-ingestion-v1.json"

governance_ref: "../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.3"

doc_kind: "Test Suite Overview"
intent: "graph-ingestion-neo4j-aws-glue-integration-tests"

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

json_schema_ref: "../../../../../../schemas/json/pipelines-graph-neo4j-aws-glue-tests-integration-readme-v1.json"
shape_schema_ref: "../../../../../../schemas/shacl/pipelines-graph-neo4j-aws-glue-tests-integration-readme-v1.shape.ttl"

immutability_status: "version-pinned"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"

ttl_policy: "24 Months"
sunset_policy: "Superseded on next major integration test suite revision"
---

<div align="center">

# 🧪 Neo4j Glue Integration Tests — End-to-End Graph Ingest  
`docs/pipelines/graph/neo4j-aws-glue/tests/integration/README.md`

**Purpose:**  
Define the **end-to-end integration test harness** for the **Neo4j Connector for AWS Glue**:

- Run representative **Glue-style jobs** (or emulations)  
- Exercise **SQL→Cypher translation** against a real Neo4j instance  
- Verify **node/relationship contracts, idempotency, and provenance**  
- Ensure ingestion remains **FAIR+CARE-compliant** and stable across releases

</div>

---

## 🗂️ 1. Directory Layout (Integration Layer)

~~~text
docs/pipelines/graph/neo4j-aws-glue/tests/integration/
│
├── 📄 README.md                           # This file — integration test overview
│
├── 🧪 run-node-ingest-smoke.sh            # (Optional) Script: node-only ingest smoke test
├── 🧪 run-relationship-ingest-smoke.sh    # (Optional) Script: relationship-only ingest test
├── 🧪 docker-compose.neo4j-test.yaml      # (Optional) test Neo4j Docker stack
├── 🧾 test-job-config.yaml                # Example test-only job config (derived from job-config.yaml)
└── 🧩 fixtures/                           # Synthetic test data & expected graph snapshots
    ├── persons.csv
    ├── regions.csv
    ├── person_region.csv
    └── expected/
        ├── nodes.json
        └── relationships.json
~~~

**Directory contract:**

- This directory is for **test harness docs & scripts**, not production jobs.  
- Fixtures MUST use **synthetic, non-sensitive data**.  
- Expected outputs under `fixtures/expected/` serve as **oracles** for integration tests.

(Individual scripts/fixtures are optional but recommended; names above are suggested patterns.)

---

## 🧱 2. Integration Test Goals

Integration tests verify behavior that cannot be fully tested at the unit/translation level:

1. **Connectivity & configuration**  
   - Neo4j test instance reachable via Neo4j JDBC driver.  
   - SQL→Cypher translator active (`enableSQLTranslation=true`).

2. **Node ingest semantics**  
   - Nodes created with correct labels, keys, and properties.  
   - Idempotent MERGE behavior (re-run safe).

3. **Relationship ingest semantics**  
   - Relationships created between correct start/end nodes.  
   - No duplicate edges when jobs re-run with identical input.

4. **Contract & provenance enforcement**  
   - Graph properties match `job-config.yaml` and schema contracts.  
   - Ingestion metadata (job ID, timestamps, dataset IDs) present and correct.

5. **FAIR+CARE compliance (at test scale)**  
   - Test jobs emulate the governance patterns (dataset IDs, domains), even with synthetic data.  
   - No test path encourages bypassing governance hooks.

---

## 🧪 3. Recommended Test Scenarios

### 3.1 Node-Only Ingest Smoke Test

**Scenario:**

- Ingest synthetic `Person` and/or `Region` nodes from small CSV files.  

**Checks:**

- Node count matches number of distinct key rows.  
- Key properties (e.g., `personId`, `regionCode`) present and unique.  
- Re-running job does **not** increase node count or create duplicates.

### 3.2 Relationship-Only Ingest Smoke Test

**Scenario:**

- Pre-populate `Person` and `Region` nodes (either via a pre-job or fixture).  
- Run relationship ingest for `LIVES_IN`, `NEIGHBORS`, etc.

**Checks:**

- Relationship count matches expected number of pairs.  
- Correct start/end labels and keys.  
- Relationship properties (e.g., `fromYear`, `toYear`) accurate.  
- Re-running job is idempotent (no duplicate edges).

### 3.3 Contract & Provenance Assertions

**Scenario:**

- After a test job completes, query Neo4j for:
  - Job-level properties on nodes/relationships (e.g., `ingestJobId`, `ingestVersion`).  
  - Dataset ID and domain attributes (`datasetId`, `domain`).

**Checks:**

- All ingested entities carry expected contract-derived properties.  
- No required governance/provenance attribute is missing according to contracts.

---

## ⚙️ 4. Test Execution Patterns

Integration tests may be run in CI or locally via:

### 4.1 Local Docker-Based Neo4j

- Use `docker-compose.neo4j-test.yaml` to spin up:
  - `neo4j-test` database  
  - Optional sidecar for log/metrics export  

Pattern:

~~~bash
docker compose -f docker-compose.neo4j-test.yaml up -d
./run-node-ingest-smoke.sh
./run-relationship-ingest-smoke.sh
docker compose -f docker-compose.neo4j-test.yaml down -v
~~~

### 4.2 Glue-Emulated Execution

- Use PySpark locally or in CI with environment variables approximating Glue.  
- Set connector options identical to Glue job configuration.

### 4.3 Real AWS Glue (Less Common in CI)

- For staging environments, an integration pipeline may:
  - Trigger a small Glue job targeting a test Neo4j instance.  
  - Run verification scripts via GitHub Actions or similar orchestrators.

---

## 🧬 5. Fixtures & Expected Outputs

`fixtures/` should contain:

- **Input data** (synthetic CSV/JSON/Parquet) representing nodes & relationships.  
- **Expected graph snapshots** (e.g., in JSON) for comparison.

Example check pattern:

- After job run, export nodes/relationships:

  - `MATCH (n:Person) RETURN n ORDER BY n.personId`  
  - `MATCH (p:Person)-[r:LIVES_IN]->(reg:Region) RETURN p.personId, reg.regionCode, r FROM p, reg, r ORDER BY p.personId, reg.regionCode`

- Compare against `fixtures/expected/nodes.json` and `fixtures/expected/relationships.json` using a tolerant comparator (ordering, minimal type coercion).

---

## 🧪 6. CI Integration Expectations

Integration tests complement:

- Unit/translation tests documented in `../README.md`.

CI workflows (indicative):

- `graph-ingest-integration-tests.yml` MUST:

  - Start a test Neo4j (Docker or ephemeral Aura).  
  - Run node & relationship ingest tests.  
  - Fail on:
    - Node/relationship count mismatches.  
    - Missing key properties or provenance tags.  
    - Duplicate entities indicative of non-idempotent MERGEs.

Telemetry for these runs should be marked as **test**:

- `environment = "ci"` or `"test"`  
- Dataset IDs like `urn:kfm:dataset:example-*`

---

## 🛡️ 7. Governance, FAIR+CARE & Safety

Even in integration tests:

- **Data MUST be synthetic**, representing realistic shapes without real PII or sensitive geospatial content.  
- Governance fields in configs (`dataset_id`, `domain`, `release_stage`) should show how **real jobs** must behave, but with non-sensitive IDs.  
- No test should:

  - Encourage bypassing provenance mapping.  
  - Rely on direct, hand-written Cypher that ignores contracts (unless tests explicitly check error handling).

---

## 🕰️ 8. Version History

| Version  | Date       | Author                               | Summary                                                                 |
|----------|------------|--------------------------------------|-------------------------------------------------------------------------|
| v11.2.3  | 2025-12-03 | Graph Systems WG · FAIR+CARE Council | Initial integration test overview for Neo4j Glue graph ingestion; defined directory layout, test scenarios, CI patterns, and governance considerations. |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — MIT**  
FAIR+CARE Certified · MCP-DL v6.3 · KFM-MDP v11.2.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[⬅ Back to Neo4j Glue Tests](../README.md) · [⬅ Back to Neo4j Glue Integration](../../README.md)

</div>

