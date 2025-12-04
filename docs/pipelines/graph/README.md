---
title: "🕸️ KFM v11.2.3 — Graph Pipelines & Neo4j Ingestion (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
description: "Governed overview of KFM v11 graph pipelines, including Neo4j ingestion patterns, AWS Glue SQL→Cypher integration, contracts, and governance for the Kansas Frontier Matrix knowledge graph."
path: "docs/pipelines/graph/README.md"
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

sbom_ref: "../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../releases/v11.2.3/manifest.zip"
telemetry_ref: "../../releases/v11.2.3/graph-ingest-telemetry.json"
telemetry_schema: "../../schemas/telemetry/graph-ingestion-v1.json"

governance_ref: "../../docs/standards/governance/ROOT-GOVERNANCE.md"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.3"

doc_kind: "Pipeline Index"
intent: "graph-pipelines-overview"

fair_category: "F1-A1-I1-R1"
care_label: "CARE-Compliant"
sensitivity: "General"
sensitivity_level: "Low"
indigenous_data_flag: true
public_benefit_level: "High"
risk_category: "Low"
redaction_required: false

ontology_alignment:
  schema_org: "SoftwareApplication"
  cidoc: "E29 Design or Procedure"
  prov_o: "prov:Plan"
  owl_time: "TemporalEntity"
  geosparql: "geo:FeatureCollection"

json_schema_ref: "../../schemas/json/pipelines-graph-readme-v1.json"
shape_schema_ref: "../../schemas/shacl/pipelines-graph-readme-v1.shape.ttl"

immutability_status: "version-pinned"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"

ttl_policy: "24 Months"
sunset_policy: "Superseded on next major graph pipeline architecture revision"
---

<div align="center">

# 🕸️ Kansas Frontier Matrix — Graph Pipelines & Neo4j Ingestion  
`docs/pipelines/graph/README.md`

**Purpose:**  
Provide the **governed entry point** for all **graph pipelines** in KFM v11 — including:

- Neo4j ingestion via AWS Glue (SQL→Cypher translator)  
- Graph ingestion contracts, schemas, and test harnesses  
- Provenance, FAIR+CARE, and sovereignty enforcement in the KFM knowledge graph  

</div>

---

## 📘 1. Scope

This index covers **pipelines that write into the KFM knowledge graph**, including:

- **Neo4j Connector for AWS Glue** (serverless SQL→Cypher ingestion)  
- Graph ingestion **contracts & schemas** for nodes/relationships  
- **Test suites** and fixtures validating graph behavior  
- Telemetry & governance expectations for graph updates

It complements:

- `docs/pipelines/README.md` — global pipelines index  
- `docs/standards/` — ontology, provenance, FAIR+CARE, and catalog standards  
- `docs/web/` — web & Cesium/MapLibre consumers of the graph

---

## 🗂️ 2. Directory Layout (Graph Pipelines · v11.2.3)

~~~text
docs/pipelines/graph/
│
├── 📄 README.md                               # This file — graph pipelines index
│
└── 🔗 neo4j-aws-glue/                         # Neo4j Connector for AWS Glue integration
    ├── 📄 README.md                           # Pipeline overview (SQL→Cypher, contracts, telemetry)
    │
    ├── 🗂️ examples/                          # Example Glue jobs & config
    │   ├── 📄 README.md                       # Examples overview
    │   ├── glue-job-node-load.py             # Example node ingest job
    │   ├── glue-job-relationship-load.py     # Example relationship ingest job
    │   └── job-config.yaml                   # Config-driven ingest contract (nodes + relationships)
    │
    ├── 🧩 schemas/                           # Ingestion contract schemas
    │   ├── 📄 README.md                      # Schema overview (node, relationship, provenance)
    │   ├── node-contract.schema.json         # Node ingest contract
    │   ├── relationship-contract.schema.json # Relationship ingest contract
    │   └── provenance-mapping.json           # Glue → PROV-O/telemetry mapping
    │
    ├── 🧪 tests/                             # Test harness (translation + integration)
    │   ├── 📄 README.md                      # Test suite overview
    │   ├── test-sql-to-cypher.yaml           # Golden SQL→Cypher translation cases
    │   └── integration/
    │       ├── 📄 README.md                  # End-to-end test harness
    │       └── fixtures/
    │           ├── 📄 README.md              # Input fixtures overview
    │           └── expected/
    │               └── 📄 README.md          # Expected node/edge snapshots overview
    │
    └── 📜 changelog.md                       # Governed change history for this pipeline pattern
~~~

**Directory contract:**

- All graph pipelines MUST live under `docs/pipelines/graph/`.  
- Each sub-pipeline (e.g., `neo4j-aws-glue/`) MUST have:
  - A **parent README** (pipeline overview).  
  - **Schemas** describing graph contracts.  
  - **Examples** and **tests** sufficient for CI and operational handoffs.  
  - A **changelog** tracking governed changes.

---

## 🧱 3. KFM Graph Ingestion Principles

KFM treats the knowledge graph as a **first-class, governed artifact**. All graph pipelines MUST adhere to:

1. **Deterministic ingestion**  
   - Given the same inputs and config, graph state MUST be reproducible.  
   - Idempotent `MERGE` semantics; re-running a job should not create duplicate nodes/edges.

2. **Contract-first design**  
   - Node and relationship shapes are defined in **schemas** (JSON/SHACL), not ad-hoc code.  
   - `job-config.yaml`-style configs must be validated before execution.

3. **Provenance & FAIR+CARE**  
   - Every ingest run emits PROV-O-aligned provenance: inputs, transformations, outputs.  
   - Sensitive data (archaeology, PII) requires additional masking/generalization before graph insertion.  

4. **Separation of concerns**  
   - Glue/AWS jobs handle **IO and transformations**.  
   - Neo4j contracts handle **graph modeling**.  
   - Governance and telemetry logic is handled by shared libraries and standards.

---

## 🔗 4. Neo4j Connector for AWS Glue (SQL→Cypher) — Summary

The `neo4j-aws-glue/` pipeline implements:

- A **custom JDBC driver** for AWS Glue that:
  - Intercepts Glue-generated SQL  
  - Translates SQL into Cypher via a governed translator  
  - Executes Cypher against Neo4j (AuraDB or self-hosted)

- A **contract-driven ingestion model**:
  - Node contracts: labels, keys, property mappings  
  - Relationship contracts: types, endpoints, property mappings  
  - Provenance mapping from Glue runtime into PROV-O

See:

- `docs/pipelines/graph/neo4j-aws-glue/README.md` for full details.

---

## 🧬 5. Contracts & Schemas

Graph ingestion contracts are defined and enforced via:

- `node-contract.schema.json` — Node ingestion:
  - `id`, `label`  
  - `source` (path, kind, options)  
  - `identity.keys[]` for MERGE  
  - `properties` mapping  
  - `governance` (dataset ID, domain, release stage)  
  - `provenance` (source paths, notes)

- `relationship-contract.schema.json` — Relationship ingestion:
  - `id`, `type`  
  - `source`  
  - `start_node` & `end_node` labels + match keys  
  - `properties` mapping  
  - `governance` & `provenance`

- `provenance-mapping.json` — PROV-O & telemetry mapping:
  - Glue Job Name, Run ID → `prov:Activity`  
  - Input S3/JDBC paths → `prov:used` entities  
  - Output graph entity summaries → `prov:Entity` records

Contracts MUST be:

- Validated in CI before deploying or updating jobs.  
- Referenced in operational runbooks and troubleshooting docs.  

---

## 🧪 6. Testing & CI Expectations

All graph pipelines MUST be covered by tests at two levels:

1. **Translation/unit tests**  
   - `test-sql-to-cypher.yaml`:
     - Golden SQL→Cypher cases for translator behavior.  
   - CI workflow ensures translator remains stable across updates.

2. **Integration tests**  
   - Under `tests/integration/`:
     - Run jobs against a **test Neo4j** instance.  
     - Use synthetic CSV fixtures (`persons.csv`, `regions.csv`, etc.).  
     - Compare actual graph to `expected/nodes.json` & `expected/relationships.json`.

CI workflows (indicative):

- `graph-ingest-sql-to-cypher-validate.yml`  
- `graph-ingest-integration-tests.yml`  
- `graph-ingest-contract-validate.yml`  

Builds MUST fail if:

- Contracts or configs violate schemas.  
- Translation or integration tests regress.  
- Provenance or governance expectations are not met.

---

## 📊 7. Telemetry & Observability for Graph Pipelines

Graph ingestion pipelines must emit telemetry for:

- **Performance**:
  - `cypher_execution_latency` (p50/p95/p99)  
  - `node_create_rate`, `relationship_create_rate`  
  - Job durations & retries

- **Reliability**:
  - Translation success/failure counts  
  - Constraint/uniqueness violation counts  
  - Failure categories for ingest jobs

- **Sustainability**:
  - Energy/CO₂ spans for ingestion workloads  
  - Measured via `graph-ingestion-v1.json` schema

Telemetry flows into:

- `graph-ingest-telemetry.json` (referenced above)  
- KFM Reliability and Sustainability dashboards

---

## 🛡️ 8. Governance & FAIR+CARE in Graph Ingest

Graph pipelines must respect the same governance as datasets:

- **Sensitive content** (e.g., archaeological sites, culturally significant locations, PII):
  - Must be generalized/aggregated where required.  
  - May be excluded from shared graph layers used in public-facing UIs.  

- Governance is enforced via:
  - FAIR+CARE metadata (`care_label`, `sensitivity`, sovereignty flags) at dataset level.  
  - Graph ingest contracts that:
    - Filter, mask, or aggregate data as needed.  
    - Attach governance tags to nodes/relationships.  

Auditability:

- All ingest runs must produce:
  - Machine-readable provenance.  
  - Logged decisions about redaction or masking when applied.

---

## 🕰️ 9. Version History (Graph Pipelines Index)

| Version  | Date       | Author                               | Summary                                                                 |
|----------|------------|--------------------------------------|-------------------------------------------------------------------------|
| v11.2.3  | 2025-12-03 | Graph Systems WG · FAIR+CARE Council | Initial graph pipelines index; documented Neo4j Glue integration sub-tree, contracts, tests, telemetry, and governance expectations for KFM v11.2.3. |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — MIT**  
FAIR+CARE Certified · MCP-DL v6.3 · KFM-MDP v11.2.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[⬅ Back to Pipelines Index](../README.md) · [🔗 Neo4j Glue Integration](neo4j-aws-glue/README.md) · [📜 Governance Charter](../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>

