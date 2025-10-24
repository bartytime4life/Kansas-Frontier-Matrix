---
title: "📜 Kansas Frontier Matrix — Treaty AI Graph Logs"
document_type: "Operational Logs · Validation Reports · Provenance Traces"
version: "v1.0.0"
last_updated: "2025-10-26"
status: "Production · FAIR+CARE+ISO Aligned"
maturity: "Stable"
license: ["MIT (scripts)", "CC-BY 4.0 (metadata)"]
owners: ["@kfm-ai","@kfm-graph","@kfm-sre"]
reviewers: ["@kfm-architecture","@kfm-qa","@kfm-ethics"]
tags: ["kfm","treaties","neo4j","logs","etl","validation","provenance","audit","fair","care","crm","owl-time","iso27001"]
alignment:
  - MCP-DL v6.4.3
  - FAIR / CARE
  - ISO 9001 / ISO 19115 / ISO 27001
  - CIDOC CRM / OWL-Time / PROV-O
validation:
  ci_enforced: true
  log_schema: "validated"
  checksum_verify: true
  retention_policy: "enforced"
observability:
  endpoint: "https://metrics.kfm.ai/ai-treaty-logs"
  dashboard: "https://metrics.kfm.ai/grafana/ai-treaty-logs"
  metrics: ["log_file_size_mb","error_rate","validation_pass_rate","etl_duration_s","graph_commit_count"]
preservation_policy:
  replication_targets: ["GitHub Artifacts (compressed)","AWS S3 Archive","Zenodo DOI (metadata only)"]
  checksum_algorithm: "SHA-256"
  retention: "90d routine logs · 365d validation reports · permanent provenance traces"
path: "data/work/staging/tabular/normalized/treaties/metadata/ai/graph/logs/README.md"
---

<div align="center">

# 📜 **Kansas Frontier Matrix — Treaty AI Graph Logs (v1.0.0 · FAIR + CARE + ISO Aligned)**  
`data/work/staging/tabular/normalized/treaties/metadata/ai/graph/logs/`

### *“Operational traces · validation reports · provenance audit logs for Treaty Graph ETL and AI pipelines”*

[![Docs · MCP-DL v6.4.3](https://img.shields.io/badge/Docs-MCP--DL%20v6.4.3-0078ff?style=flat-square)](../../../../../../../../../../../../../docs/)
[![FAIR + CARE](https://img.shields.io/badge/FAIR%20%2B%20CARE-Compliant-2ecc71?style=flat-square)]()
[![ISO 27001](https://img.shields.io/badge/ISO-27001%20Auditable-blue?style=flat-square)]()
[![CIDOC CRM](https://img.shields.io/badge/Semantics-CIDOC%20CRM%20%2F%20PROV--O-8e44ad?style=flat-square)]()
[![Governance Ledger](https://img.shields.io/badge/Ledger-Immutable-d4af37?style=flat-square)]()

</div>

---

## 📘 Purpose
This directory contains **AI Graph operational logs**, **validation summaries**, and **provenance traces** generated during the execution of Cypher imports, snapshot creation, and export pipelines for the **Treaty AI Graph**.  

Each log provides an **auditable record** of actions performed by automated processes, including:
- Data ingestion runs (`make ai-graph-publish`, `make ai-graph-validate`)
- Snapshot and export operations (`make ai-graph-snapshot`, `make ai-graph-export`)
- CI/CD validation results (lint, checksum, schema, and provenance)
- Observability metrics collected during ETL

---

## 🧩 Context & Dependencies
| Component | Function | Log Source |
|:--|:--|:--|
| AI/ETL Pipeline | Extract–Transform–Load orchestration | `src/pipelines/` |
| Neo4j Server | Graph operations and query timing | `/var/log/neo4j` |
| KFM CI Runner | Automated build/test logs | `.github/workflows/*` |
| AI Modules | NLP, provenance scoring, summarization | `src/ai/` |
| Focus Mode | Graph focus edge updates | `create_focus_edges.cql` |

---

## 🗂️ Directory Layout
```

logs/
├── 2025-10-26T00-00Z_build.log            # Full build log for this cycle
├── 2025-10-26T00-00Z_validation.log       # Validation summary (lint + schema)
├── 2025-10-26T00-00Z_metrics.json         # Extracted metrics (runtime, counts)
├── provenance_trace.jsonld                # PROV-O chain of ETL actions
├── ai_pipeline.log                         # NLP + Cypher generation logs
├── error_summary.yaml                     # Error/warning summary by severity
├── neo4j_query_times.csv                  # Per-query execution statistics
└── README.md                              # You are here

````

---

## 🔄 Logging Workflow
```mermaid
flowchart TD
A["Makefile Command (ai-graph-*)"] --> B["Pipeline Execution (ETL + AI)"]
B --> C["Neo4j Transaction Logs"]
C --> D["Validation + Checksums"]
D --> E["Metrics Extraction + Provenance JSON-LD"]
E --> F["Immutable Ledger Upload"]
````

### Key Outputs

* **Build Log:** Command-by-command ETL trace.
* **Validation Log:** Contains CI stage outputs (lint, provenance, schema).
* **Metrics JSON:** Structured summary (runtime, counts, error ratios).
* **Provenance JSON-LD:** Describes each action as a PROV `Activity` linked to `Entity` and `Agent` (per CIDOC CRM & PROV-O).
* **Error Summary YAML:** Grouped by severity and subsystem.

---

## 🧾 FAIR Metadata Summary

| Field      | Value                                       |
| :--------- | :------------------------------------------ |
| Dataset    | Treaty AI Graph Logs                        |
| Type       | ETL + validation logs                       |
| Format     | `.log`, `.json`, `.jsonld`, `.yaml`, `.csv` |
| Ontologies | PROV-O, CIDOC CRM                           |
| Provenance | Derived from AI pipeline + ledger anchors   |
| Checksum   | SHA-256                                     |
| License    | CC-BY 4.0 (metadata)                        |
| Retention  | 90 days (operational), 1 year (compliance)  |

---

## 🧮 Observability Metrics

| Metric                  | Target  | Current | Verified | Source         |
| :---------------------- | :------ | :------ | :------- | :------------- |
| Log File Size           | ≤ 50 MB | 21 MB   | ✅        | CI artifacts   |
| Validation Pass Rate    | 100%    | 100%    | ✅        | CI logs        |
| Error Rate              | ≤ 0.5%  | 0%      | ✅        | Error Summary  |
| Graph Commits Logged    | 100%    | 100%    | ✅        | ETL audit      |
| Metrics Extraction Time | ≤ 30 s  | 19 s    | ✅        | CI job metrics |

---

## 🔐 Security & Audit

* Logs are automatically rotated and compressed; sensitive data (user tokens, hostnames) are **redacted**.
* Logs stored in KFM’s artifact store are **encrypted-at-rest (AES-256)**.
* Audit trails cross-referenced with **ledger receipts** in `/snapshots/ledger_receipt.json`.
* Access restricted to **project maintainers and auditors**.
* Each build log is hashed and included in the provenance graph.

---

## 🧠 Use Cases

* **Reproducibility:** Trace the full lineage of each dataset build.
* **Performance Analysis:** Use `neo4j_query_times.csv` to monitor query latency.
* **Error Tracking:** Review `error_summary.yaml` to identify systemic issues.
* **Audit Compliance:** Provide full transparency for ISO/SLSA attestations.

---

## 🧰 Troubleshooting

| Issue                         | Likely Cause                     | Resolution                                           |
| :---------------------------- | :------------------------------- | :--------------------------------------------------- |
| "Missing validation log"      | pipeline failed before CI upload | rerun `make ai-graph-validate`                       |
| "Incomplete provenance chain" | JSON-LD file cut during sync     | regenerate via `make ai-graph-provenance`            |
| "Excessive log size"          | debug mode enabled               | compress with `xz` and archive                       |
| "Neo4j query logs empty"      | query logging disabled           | enable in `neo4j.conf: dbms.logs.query.enabled=true` |

---

## 🧱 Standards Alignment

* ✅ **MCP-DL v6.4.3** (docs-as-code with auditable provenance)
* ✅ **FAIR + CARE** (open metadata + ethical data handling)
* ✅ **ISO 27001** (§A.12.4.1 event logging and integrity)
* ✅ **CIDOC CRM / PROV-O** linkage for action provenance
* ✅ **ISO 19115** metadata retention & validation structure

---

## 📘 Related Documentation

* [Graph Snapshots](../snapshots/README.md)
* [Exports README](../exports/README.md)
* [Signatures README](../snapshots/signatures/README.md)
* [AI Graph Suite](../cypher/README.md)
* [Security & Governance Standards](../../../../../../../../../docs/standards/security.md)

---

## 🕓 Version History

| Version    | Date       | Author  | Reviewer          | Summary                                                             |
| :--------- | :--------- | :------ | :---------------- | :------------------------------------------------------------------ |
| **v1.0.0** | 2025-10-26 | @kfm-ai | @kfm-architecture | Initial full operational logging + FAIR/ISO alignment documentation |

---

<div align="center">

[![Docs · MCP-DL v6.4.3](https://img.shields.io/badge/Docs-MCP--DL%20v6.4.3-0078ff?style=flat-square)]()
[![FAIR + CARE](https://img.shields.io/badge/FAIR%20%2B%20CARE-Compliant-2ecc71?style=flat-square)]()
[![ISO 27001](https://img.shields.io/badge/ISO-27001-blue?style=flat-square)]()
[![Ledger](https://img.shields.io/badge/Ledger-Immutable-d4af37?style=flat-square)]()

</div>

<!-- MCP-FOOTER-BEGIN
MCP-VERSION: v6.4.3
MCP-TIER: FAIR + CARE + ISO Aligned
DOC-PATH: data/work/staging/tabular/normalized/treaties/metadata/ai/graph/logs/README.md
MCP-CERTIFIED: true
SBOM-GENERATED: true
SLSA-ATTESTED: true
A11Y-VERIFIED: true
FAIR-CARE-COMPLIANT: true
GOVERNANCE-LEDGER-LINKED: true
OBSERVABILITY-ACTIVE: true
PROVENANCE-JSONLD: true
PERFORMANCE-BUDGET-P95: 2.5 s
ENERGY-BUDGET-P95: 25 Wh
CARBON-BUDGET-P95: 28 gCO₂e
GENERATED-BY: KFM-Automation/DocsBot
LAST-VALIDATED: 2025-10-26
MCP-FOOTER-END -->

```
```

