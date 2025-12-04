---
title: "🧾 KFM v11.2.3 — Neo4j Connector for AWS Glue · Changelog (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
description: "Version history and governed changes for the Neo4j Connector for AWS Glue graph-ingestion pattern in the Kansas Frontier Matrix."
path: "docs/pipelines/graph/neo4j-aws-glue/changelog.md"
version: "v11.2.3"
last_updated: "2025-12-03"

release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Graph Systems · FAIR+CARE Council"
content_stability: "stable"

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

doc_kind: "Changelog"
intent: "graph-ingestion-neo4j-aws-glue-changelog"
status: "Active · Enforced"

fair_category: "F1-A1-I1-R1"
care_label: "CARE-Compliant"
sensitivity: "General"
sensitivity_level: "Low"
indigenous_data_flag: false
public_benefit_level: "High"
risk_category: "Low"
redaction_required: false

ontology_alignment:
  schema_org: "CreativeWork"
  cidoc: "E29 Design or Procedure"
  prov_o: "prov:Entity"
  owl_time: "TemporalEntity"
  geosparql: "geo:FeatureCollection"

json_schema_ref: "../../../../schemas/json/pipelines-graph-neo4j-aws-glue-changelog-v1.json"
shape_schema_ref: "../../../../schemas/shacl/pipelines-graph-neo4j-aws-glue-changelog-v1.shape.ttl"

immutability_status: "version-pinned"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"

ttl_policy: "24 Months"
sunset_policy: "Superseded on next major Neo4j Glue integration revision"
---

<div align="center">

# 🧾 Neo4j Connector for AWS Glue — Changelog  
`docs/pipelines/graph/neo4j-aws-glue/changelog.md`

**Purpose:**  
Maintain a **governed, auditable history** of changes to the **Neo4j Connector for AWS Glue** graph-ingestion pattern, including:

- Directory layout & documentation updates  
- Contract/schema changes (`schemas/`)  
- Example jobs & config templates (`examples/`)  
- Test harness & fixtures (`tests/`)  
- Behavioral changes to SQL→Cypher ingestion semantics  

</div>

---

## 📚 Change Log Conventions

- Entries are ordered **newest → oldest**.  
- Each entry MUST include:
  - `version` — pipeline spec version (not connector JAR version).  
  - `date` — ISO date in KFM local context.  
  - `change_type` — `add`, `fix`, `refactor`, `deprecate`, `break`, etc.  
  - `summary` — concise explanation.  
  - Optional `notes` — links to PRs, incidents, or governance decisions.

- **Breaking changes** MUST be clearly marked and accompanied by:
  - Migration notes.  
  - Required contract or job-config changes.

---

## 🧬 v11.2.3 — Initial KFM v11 Integration

| Version  | Date       | Change Type | Summary                                                                 | Notes |
|----------|------------|------------|-------------------------------------------------------------------------|-------|
| v11.2.3  | 2025-12-03 | add        | Initial KFM-v11 documentation and contracts for Neo4j Connector for AWS Glue (SQL→Cypher graph ingest). | Parent README, examples, schemas, and tests added. |

### Details

- **Docs & Layout**
  - Added `docs/pipelines/graph/neo4j-aws-glue/README.md` with:
    - High-level overview of SQL→Cypher behavior.  
    - Directory layout (examples, schemas, tests, changelog).  
    - Provenance, CI, and telemetry expectations.

- **Examples**
  - Added `examples/README.md` describing:
    - `glue-job-node-load.py` & `glue-job-relationship-load.py` patterns.  
    - `job-config.yaml` as config-driven ingestion contract.  
  - Introduced `job-config.yaml` template with:
    - `nodes[]` and `relationships[]` sections.  
    - Identity, properties, governance, and provenance blocks.

- **Schemas**
  - Added `schemas/README.md` summarizing:
    - `node-contract.schema.json` and `relationship-contract.schema.json`.  
    - `provenance-mapping.json` for PROV-O alignment.  

- **Tests**
  - Added `tests/README.md` for:
    - `test-sql-to-cypher.yaml` golden translation cases.  
    - `tests/integration/` for end-to-end harness.  
  - Added `tests/integration/README.md` and `fixtures/` docs:
    - Synthetic CSV fixtures (`persons.csv`, `regions.csv`, `person_region.csv`).  
    - Expected graph snapshots (`nodes.json`, `relationships.json`).

- **Telemetry**
  - Wired documentation references to:
    - `graph-ingest-telemetry.json`.  
    - `graph-ingestion-v1.json` telemetry schema.

- **Governance**
  - Confirmed alignment with:
    - KFM governance root (`ROOT-GOVERNANCE.md`).  
    - FAIR+CARE contracts via provenance & domain metadata.

No prior versions of this integration pattern are recorded in this changelog; earlier ad-hoc or non-governed integrations are considered **pre-standard** and must be migrated to v11.2.3 contracts.

---

## 🧭 Future Changes (Template)

When changes occur, add new sections **above** v11.2.3, for example:

~~~text
## 🧬 v11.2.4 — <short summary>

| Version  | Date       | Change Type | Summary | Notes |
|----------|------------|------------|---------|-------|
| v11.2.4  | YYYY-MM-DD | fix        | ...     | ...   |

- Detail bullets here…
~~~

All future changes MUST:

- Update this changelog.  
- Reference the relevant PR/issue or incident where appropriate.  
- Be reviewed by the **Graph Systems WG** and, for governance-impactful changes, the **FAIR+CARE Council**.

---

<div align="center">

**© 2025 Kansas Frontier Matrix — MIT**  
FAIR+CARE Certified · MCP-DL v6.3 · KFM-MDP v11.2.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[⬅ Back to Neo4j Glue Integration](README.md) · [⬅ Back to Graph Pipelines Index](../README.md)

</div>
