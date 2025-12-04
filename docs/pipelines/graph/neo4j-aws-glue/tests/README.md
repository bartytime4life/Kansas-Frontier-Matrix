---
title: "🧪 KFM v11.2.3 — Neo4j Glue Graph Ingestion Tests (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
description: "Test suite overview for the Neo4j Connector for AWS Glue integration, validating SQL→Cypher translation, graph contracts, and provenance for KFM graph ingestion."
path: "docs/pipelines/graph/neo4j-aws-glue/tests/README.md"
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

sbom_ref: "../../../../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.2.3/manifest.zip"
telemetry_ref: "../../../../../releases/v11.2.3/graph-ingest-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/graph-ingestion-v1.json"

governance_ref: "../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.3"

doc_kind: "Test Suite Overview"
intent: "graph-ingestion-neo4j-aws-glue-tests"

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

json_schema_ref: "../../../../../schemas/json/pipelines-graph-neo4j-aws-glue-tests-readme-v1.json"
shape_schema_ref: "../../../../../schemas/shacl/pipelines-graph-neo4j-aws-glue-tests-readme-v1.shape.ttl"

immutability_status: "version-pinned"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"

ttl_policy: "24 Months"
sunset_policy: "Superseded on next major test suite revision"
---

<div align="center">

# 🧪 Neo4j Glue Graph Ingestion Tests  
`docs/pipelines/graph/neo4j-aws-glue/tests/README.md`

**Purpose:**  
Define the **governed test suite** for the **Neo4j Connector for AWS Glue** graph ingestion pipelines, ensuring:

- SQL→Cypher translation is **stable and deterministic**  
- Node & relationship ingestion **honors contracts**  
- Provenance and telemetry are present and correct  
- Ingestion remains **FAIR+CARE-compliant** across updates

</div>

---

## 🗂️ 1. Directory Layout (Test Suite)

~~~text
docs/pipelines/graph/neo4j-aws-glue/tests/
│
├── 📄 README.md                       # This file — test overview & expectations
│
├── 🧪 test-sql-to-cypher.yaml         # Golden SQL→Cypher translation fixtures
└── 🧪 integration/                    # (Optional) end-to-end / integration tests
    ├── 📄 README.md                   # (Optional) integration-test specifics
    └── …                              # Scripts/configs for running real jobs vs test Neo4j
~~~

**Directory contract:**

- `test-sql-to-cypher.yaml` MUST exist and contain at least one **golden translation** case.  
- `integration/` is optional but recommended for full-stack tests.  
- CI workflows must reference this directory explicitly when validating the Glue → Neo4j integration.

---

## 🔁 2. SQL→Cypher Translation Tests (`test-sql-to-cypher.yaml`)

These tests ensure the JDBC SQL→Cypher translator behaves as expected.

### 2.1 Conceptual Structure

Each case in `test-sql-to-cypher.yaml` should define:

- `id` — test case identifier  
- `description` — human-readable explanation  
- `input_sql` — the SQL statement Glue is expected to emit  
- `expected_cypher` — the Cypher the translator MUST produce (modulo whitespace)  
- Optional `notes` — edge cases or constraints

Illustrative pattern (not normative schema):

~~~yaml
cases:
  - id: "simple-node-insert"
    description: "INSERT into Person becomes MERGE/SET on :Person nodes"
    input_sql: >
      INSERT INTO Person (personId, firstName, lastName)
      VALUES ('123', 'Ada', 'Lovelace');
    expected_cypher: >
      MERGE (p:Person { personId: '123' })
      SET p.firstName = 'Ada', p.lastName = 'Lovelace';
    notes: "Identity key is personId; additional properties are updates."
~~~

### 2.2 Coverage Expectations

The fixture should cover at least:

- Basic INSERT → MERGE patterns  
- UPDATE → SET patterns  
- DELETE → MATCH/DELETE patterns (if used)  
- Relationship loads (e.g., pseudo tables for relationships)  
- Error/unsupported patterns (if the translator uses explicit error cases)

CI SHOULD:

- Run translation logic against these cases.  
- Fail builds if any `input_sql` yields a different Cypher than `expected_cypher` (modulo normalized formatting).

---

## 🔗 3. Integration Tests (`integration/`)

Integration tests validate the **end-to-end** behavior:

- Glue-style jobs (or emulated jobs)  
- SQL→Cypher translation  
- Neo4j execution  
- Contract + provenance enforcement

### 3.1 Recommended Coverage

Integration tests MAY include:

- **Node-only load** test:
  - Loads a tiny synthetic CSV into Neo4j.  
  - Verifies:
    - Node count.  
    - Key properties.  
    - Idempotency (re-running job is safe).

- **Relationship-only load** test:
  - Pre-populates nodes in test Neo4j.  
  - Runs relationship job via translation.  
  - Verifies:
    - Relationship count and properties.  
    - No duplicate edges on re-run.

- **Provenance presence**:
  - Asserts ingestion metadata (job run ID, dataset ID, etc.) is set on nodes/relationships or logged to provenance.

Integration tests may run:

- In a local Docker-based Neo4j (via CI).  
- Against a small ephemeral AuraDB instance (where allowed).

---

## 🧪 4. CI Workflow Expectations

KFM CI/CD must include at least one workflow dedicated to these tests, e.g.:

- `graph-ingest-sql-to-cypher-validate.yml`  
- `graph-ingest-integration-tests.yml`

### 4.1 SQL→Cypher Validation (Required)

Workflow responsibilities:

- Load `test-sql-to-cypher.yaml` fixtures.  
- For each case:
  - Run translation function.  
  - Normalize whitespace and compare with `expected_cypher`.  
- Fail if:
  - Any case does not match.  
  - Translator throws unhandled errors for supported patterns.

### 4.2 Integration Tests (Recommended)

Workflow responsibilities:

- Spin up test Neo4j.  
- Apply node & relationship jobs using example `job-config.yaml`.  
- Verify:
  - Node/relationship counts.  
  - Presence of key properties.  
  - Absence of duplicate nodes/edges.  
- Clean up or reset database between tests.

---

## 📐 5. Governance, FAIR+CARE & Safety Considerations

Even tests must:

- Use **synthetic or non-sensitive data**.  
- Avoid real PII, sensitive archaeological sites, or confidential infrastructure details.  
- Ensure schemas and configs in tests mirror **real-world governance patterns**:

  - Ingestion contracts for dataset IDs and domains.  
  - Provenance mapping for Glue job IDs and sources.  
  - No tests that rely on bypassing governance logic.

---

## 📊 6. Telemetry & Test Observability

When tests run in CI:

- They MAY emit telemetry to the same graph-ingestion telemetry stream:

  - Tagged as `environment = "ci"` or `environment = "test"`  
  - With safe, synthetic dataset IDs (e.g., `urn:kfm:dataset:example-*`)

Metrics may include:

- Number of translation tests run & passed.  
- Integration test durations.  
- Counts of nodes/relationships ingested in test runs.  
- Failures by category (translation vs graph vs provenance).

This telemetry helps:

- Detect regression trends.  
- Estimate cost of ingestion patterns at small scale before production rollout.

---

## 🧭 7. Implementation Checklist (Tests)

Before merging changes to Neo4j Glue integration:

1. **Add or update SQL→Cypher cases** in `test-sql-to-cypher.yaml` for new patterns.  
2. **Update integration tests** to cover relevant new job types or contracts.  
3. **Run tests locally** (if feasible) and in CI:
   - Ensure 100% pass rate.  
4. **Update docs**:
   - If new patterns or constraints are introduced, update:
     - `../README.md` (overview).  
     - `../examples/README.md` and `job-config.yaml`.  
     - `../schemas/README.md` where relevant.  
5. **Monitor telemetry** from CI test runs over time.

---

## 🕰️ 8. Version History

| Version  | Date       | Author                               | Summary                                                                 |
|----------|------------|--------------------------------------|-------------------------------------------------------------------------|
| v11.2.3  | 2025-12-03 | Graph Systems WG · FAIR+CARE Council | Initial test suite overview for Neo4j Glue graph ingestion; defined SQL→Cypher fixture expectations, integration test patterns, CI workflow requirements, and governance considerations. |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — MIT**  
FAIR+CARE Certified · MCP-DL v6.3 · KFM-MDP v11.2.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[⬅ Back to Neo4j Glue Integration](../README.md) · [⬅ Back to Schemas](../schemas/README.md) · [⬅ Back to Examples](../examples/README.md)

</div>

