---
title: "🗺️ KFM — Graph Documentation: Neo4j, Ontologies, Mappings, Provenance"
path: "docs/graph/README.md"

version: "v11.2.6"
last_updated: "2025-12-14"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Graph Board · FAIR+CARE Council"
content_stability: "stable"
status: "Active / Enforced"

doc_kind: "Index"
header_profile: "standard"
footer_profile: "standard"

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

intent: "graph-docs-index"
audience:
  - "Graph Engineering"
  - "Data Engineering"
  - "Search Engineering"
  - "Reliability Engineering"
  - "Governance Reviewers"
  - "API Engineering"

classification: "Public"
sensitivity: "General (non-sensitive)"
sensitivity_level: "None"
public_exposure_risk: "Low"
fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"
jurisdiction: "Kansas / United States"
indigenous_rights_flag: true
data_steward: "Graph Board · FAIR+CARE Council"

governance_ref: "../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

commit_sha: "<latest-commit-hash>"
doc_uuid: "urn:kfm:doc:graph:index:v11.2.6"
semantic_document_id: "kfm-graph-docs-index"
event_source_id: "ledger:docs/graph/README.md"
provenance_chain:
  - "initial:v11.2.6"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summary"
  - "semantic-highlighting"
  - "metadata-extraction"
ai_transform_prohibited:
  - "speculative-additions"
  - "fabricated-claims"
  - "unverified-architectural-claims"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
---

<div align="center">

# 🗺️ **KFM — Graph Documentation**
`docs/graph/README.md`

**Purpose**  
Index and governance anchor for KFM’s graph layer: **Neo4j modeling**, **ontology alignment**, **ingest mappings**,
**query patterns**, and **provenance-first** graph operations.

</div>

---

## 📘 Overview

The KFM graph layer provides:

- a queryable representation of People, Places, Events, Documents, Datasets, Runs, and Story Nodes,
- explicit relationships that power navigation, search expansion, and provenance traceability,
- governance-aware access patterns that respect FAIR+CARE constraints.

Pipeline placement:

- ETL produces governed assets and catalogs
- Catalogs and provenance are ingested into the graph
- The API is the only supported boundary for the frontend
- The frontend does not query Neo4j directly

---

## 🗂️ Directory Layout

~~~text
📁 docs/graph/                                         — Graph documentation root (this directory)
├── 📄 README.md                                       — This index (you are here)
└── 📁 cypher/                                         — Cypher docs and governed query patterns
    ├── 📄 README.md                                   — Cypher index
    └── 📁 patterns/                                   — Pattern library
        ├── 📄 README.md                               — Pattern library index
        └── 📄 change-windows.md                       — Ops change windows and diffs
~~~

---

## 🧭 Quick links

- Cypher index: [`docs/graph/cypher/README.md`](cypher/README.md)
- Cypher patterns: [`docs/graph/cypher/patterns/README.md`](cypher/patterns/README.md)
- Ops change windows and diffs: [`docs/graph/cypher/patterns/change-windows.md`](cypher/patterns/change-windows.md)

---

## 🧩 Graph layer principles

### Typed nodes and relationships

- Prefer strong labels and explicit relationship types over unstructured blobs.
- Store key fields as properties that can be indexed and filtered.

### Stable identifiers

- Prefer stable URNs for core entities:
  - `urn:kfm:place:…`
  - `urn:kfm:event:…`
  - `urn:kfm:dataset:…`
  - `urn:kfm:run:…`
- Store source identifiers in provenance-aware properties so lineage remains queryable.

### Ontology alignment

KFM graph modeling SHOULD align with:

- CIDOC-CRM for cultural and historical entities and events
- GeoSPARQL for geometries and spatial relations
- OWL-Time for instants and intervals
- PROV-O for lineage and activities

### Provenance and rights are queryable

At minimum, graph entities SHOULD carry:

- source reference and license posture
- sensitivity and governance labels
- provenance links to generating activities and upstream entities

---

## 🧱 Ingestion and change management

### Idempotent ingestion

Graph ingestion MUST be:

- incremental
- idempotent
- version-aware

### Constraints and indexes

Graph schemas SHOULD define:

- uniqueness constraints for stable ids
- indexes for common retrieval paths
- dedupe and merge rules with tests

### Drift and diffs

Operational drift is managed by:

- time-window rollups over versions and items
- property diffs for changed entities
- provenance comparisons between runs

See the ops patterns here:

- [`cypher/patterns/change-windows.md`](cypher/patterns/change-windows.md)

---

## 🛡️ FAIR+CARE and sovereignty

Graph queries and exports MUST avoid leakage.

Default posture:

- avoid returning raw sensitive geometry where policy requires generalization
- filter or aggregate restricted entities by governance label
- record policy decisions in provenance for auditability

If sovereignty labels conflict or are unknown, systems SHOULD fail closed:

- deny or return aggregated counts only
- require manual review under governance policy

---

## 🧪 Validation and CI/CD

Recommended checks for graph docs and query patterns:

- `markdown-lint` for KFM-MDP v11.2.6 structure and fence style
- `diagram-check` for Mermaid blocks when present
- `query-smoke-test` against a staging graph snapshot for pattern queries
- governance leakage checks for dashboards and public-facing outputs

---

## 🕰️ Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v11.2.6 | 2025-12-14 | Initial governed graph documentation index; linked Cypher docs and ops query patterns. |

---

<div align="center">

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />

[🧾 Cypher](cypher/README.md) ·
[🧩 Cypher Patterns](cypher/patterns/README.md) ·
[🏛️ Governance Charter](../standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md) ·
[⬅ Docs Index](../README.md)

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
MCP-DL v6.3 · KFM-MDP v11.2.6 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>
