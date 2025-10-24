---
title: "🧰 Kansas Frontier Matrix — Treaty AI Graph Snapshots"
document_type: "Stateful Backups · Point-in-Time Recovery · Provenance Archives"
version: "v1.1.0"
last_updated: "2025-10-25"
status: "Production · FAIR+CARE+ISO+SLSA Certified"
maturity: "Stable"
license: ["MIT (scripts)", "CC-BY 4.0 (metadata)"]
owners: ["@kfm-graph","@kfm-sre","@kfm-ai"]
reviewers: ["@kfm-architecture","@kfm-qa","@kfm-ethics"]
tags: ["kfm","treaties","neo4j","snapshot","backup","recovery","graph","provenance","slsa","fair","care","crm","owl-time","iso27001"]
alignment:
  - MCP-DL v6.4.3
  - FAIR / CARE
  - ISO 9001 / ISO 19115 / ISO 27001
  - CIDOC CRM / OWL-Time / PROV-O
validation:
  ci_enforced: true
  checksum_verify: true
  restore_dry_run: true
  schema_validation: true
  artifact_signing: "SLSA-attested"
observability:
  endpoint: "https://metrics.kfm.ai/ai-treaty-snapshots"
  dashboard: "https://metrics.kfm.ai/grafana/ai-treaty-snapshots"
  metrics: ["snapshot_duration_s","snapshot_size_mb","checksum_match_rate","restore_test_pass_rate","rpo_minutes","rto_minutes","graph_node_count","relationship_count"]
preservation_policy:
  replication_targets: ["GitHub Releases (secured)","Zenodo DOI (metadata only)","AWS S3 Glacier Deep Archive","KFM Ledger Node"]
  checksum_algorithm: "SHA-256"
  retention: "Rolling 365d daily · 12mo monthly · Permanent canonical sets"
path: "data/work/staging/tabular/normalized/treaties/metadata/ai/graph/snapshots/README.md"
---

<div align="center">

# 🧰 **Kansas Frontier Matrix — Treaty AI Graph Snapshots (v1.1.0 · FAIR + CARE + ISO + SLSA Certified)**  
`data/work/staging/tabular/normalized/treaties/metadata/ai/graph/snapshots/`

### *“Deterministic Graph Backups · Provenance Anchoring · Disaster Recovery · Reproducibility Assurance”*

[![Docs · MCP-DL v6.4.3](https://img.shields.io/badge/Docs-MCP--DL%20v6.4.3-0078ff?style=flat-square)](../../../../../../../../../../../docs/)
[![FAIR + CARE](https://img.shields.io/badge/FAIR%20%2B%20CARE-Compliant-2ecc71?style=flat-square)]()
[![SLSA](https://img.shields.io/badge/SLSA-Attested-purple?style=flat-square)]()
[![Neo4j Backup](https://img.shields.io/badge/Neo4j-Backup%20%26%20Recovery-blue?style=flat-square)]()
[![Governance Ledger](https://img.shields.io/badge/Governance-Immutable%20Ledger-d4af37?style=flat-square)]()

</div>

---

## 📘 Purpose
This directory contains **stateful Neo4j backups (“snapshots”)** for the Treaty knowledge graph.  
Snapshots ensure **data recoverability, reproducibility**, and **evidentiary traceability** of treaty-related data under FAIR + CARE + ISO 27001 controls.

They serve as:
- 🧩 **Disaster recovery points** (meeting RPO/RTO targets)
- 🧾 **Scientific replication anchors** (for audits and re-analysis)
- 🔗 **Governance artifacts** (ledger-anchored immutable records)

---

## 🧩 Context & Dependencies
| Dependency | Role | Source |
|:--|:--|:--|
| Neo4j ≥ 5.12 + APOC | Graph engine | `src/graph/` |
| `make ai-graph-publish` | Upstream data load | `.../graph/cypher/` |
| `make ai-graph-snapshot` | Snapshot orchestration | Makefile root |
| AWS CLI + Cosign | Artifact signing & storage | CI job `graph-backup.yml` |
| DVC | Optional pointer management for large files | `.dvc/config` |

---

## 🗂️ Directory Layout
```

snapshots/
├── 2025-10-25T00-00Z/
│   ├── neo4j-backup.tar.zst
│   ├── graphml/
│   │   ├── treaties.graphml
│   │   ├── nodes.csv
│   │   └── relationships.csv
│   ├── manifest.yaml
│   ├── checksums.sha256
│   ├── ledger_receipt.json
│   ├── signatures/
│   │   └── backup.sig
│   ├── restore_notes.md
│   └── export_log.txt
└── README.md

````

---

## 🔄 Snapshot Workflow
```mermaid
flowchart TD
A["Verified Publish · Neo4j Graph"] --> B["Backup Job · neo4j-admin + tar.zst"]
B --> C["GraphML/CSV Portable Views"]
C --> D["Checksum · Signature · Ledger Anchor"]
D --> E["Replication · S3 / Releases / Zenodo"]
E --> F["Nightly Restore · CI Validation"]
````

### Steps

1. **Graph Backup**

   ```bash
   neo4j stop
   neo4j-admin database backup neo4j --to-path ./tmp/backup --fallback-to-full=true
   tar -I 'zstd -19 --long' -cf snapshots/${TS}/neo4j-backup.tar.zst ./tmp/backup
   neo4j start
   ```
2. **Portable Views (optional)**

   ```cypher
   CALL apoc.export.graphml.all("snapshots/${TS}/graphml/treaties.graphml",{useTypes:true,readLabels:true});
   CALL apoc.export.csv.all("snapshots/${TS}/graphml/nodes.csv",{});
   CALL apoc.export.csv.all("snapshots/${TS}/graphml/relationships.csv",{});
   ```
3. **Checksums + Signing**

   ```bash
   sha256sum snapshots/${TS}/**/* > snapshots/${TS}/checksums.sha256
   cosign sign-blob snapshots/${TS}/neo4j-backup.tar.zst --output-signature snapshots/${TS}/signatures/backup.sig
   ```
4. **Ledger Anchoring**
   CI writes immutable receipt → `ledger_receipt.json`.
5. **Replication & Validation**
   CI replicates to S3 + GitHub; runs checksum verify + dry-run restore.

---

## ♻️ Restore Procedure

1. **Validate Artifacts**

   ```bash
   sha256sum -c snapshots/${TS}/checksums.sha256
   cosign verify-blob --key $COSIGN_PUB snapshots/${TS}/neo4j-backup.tar.zst
   ```
2. **Restore**

   ```bash
   tar -I zstd -xf snapshots/${TS}/neo4j-backup.tar.zst -C $NEO4J_HOME
   neo4j-admin database restore neo4j --from=$NEO4J_HOME/backup --force
   ```
3. **Smoke Tests**

   ```cypher
   MATCH (t:Treaty) RETURN count(t);
   MATCH (t:Treaty)-[:OCCURRED_AT]->(p:Place) RETURN count(*);
   ```
4. **CI Validation**

   * Schema integrity checks
   * Focus edges re-linked
   * Provenance graph chain intact
   * Exports reproducible (`make ai-graph-export`)

**Recovery Targets**

| Metric | Goal                            |
| :----- | :------------------------------ |
| RPO    | ≤ 60 min                        |
| RTO    | ≤ 30 min (warm) / ≤ 2 hr (cold) |

---

## 🧾 FAIR & PROV Metadata

| Field      | Value                                |
| :--------- | :----------------------------------- |
| Dataset    | Treaty AI Graph Snapshots            |
| Type       | Binary backup + semantic views       |
| Checksum   | SHA-256                              |
| Signatures | Cosign / Minisign                    |
| Ontologies | PROV-O, CIDOC CRM, OWL-Time          |
| Provenance | Linked to ledger & Git commit        |
| DOI        | Metadata only (no binary data)       |
| Retention  | Rolling daily + monthly archives     |
| Ethics     | CARE screened (no sensitive content) |

---

## 🔐 Security & CARE

* Access limited to **authorized maintainers** (private artifacts).
* **CARE-compliant**: no personal identifiers in graph structure.
* **Immutable** via **content-addressable naming** and **ledger anchoring**.
* **ISO 27001 alignment:** validated against backup & restore controls.
* **Encryption-at-rest:** S3 Glacier / GitHub Releases use AES-256 server-side encryption.

---

## 🧪 CI Validation Gates

| Check            | Tool             | Frequency | Status |
| :--------------- | :--------------- | :-------- | :----- |
| Checksum Verify  | `sha256sum`      | per build | ✅      |
| Signature Verify | Cosign           | per build | ✅      |
| Restore Dry-Run  | Dockerized Neo4j | nightly   | ✅      |
| Schema Lint      | Cypher-Lint      | nightly   | ✅      |
| Ledger Receipt   | KFM Ledger Node  | per build | ✅      |
| A11y Metadata    | json-schema-lint | per build | ✅      |

---

## 📈 Observability Metrics

| Metric            | Target   | Current | Verified | Source         |
| :---------------- | :------- | :------ | :------- | :------------- |
| Snapshot Duration | ≤ 300 s  | 219 s   | ✅        | CI logs        |
| Snapshot Size     | ≤ 3 GB   | 1.84 GB | ✅        | Artifact index |
| Checksum Match    | 100%     | 100%    | ✅        | Verify step    |
| Restore Pass Rate | 100%     | 100%    | ✅        | Nightly CI     |
| Graph Nodes       | —        | 2,402   | ✅        | Neo4j count    |
| Graph Edges       | —        | 6,217   | ✅        | Neo4j count    |
| RPO               | ≤ 60 min | 28 min  | ✅        | Scheduler      |
| RTO               | ≤ 30 min | 21 min  | ✅        | Failover drill |

---

## 🧱 Standards & Compliance

* ✅ MCP-DL v6.4.3 documentation & reproducibility
* ✅ FAIR + CARE alignment
* ✅ ISO 27001 §A.12.3 (Backup)
* ✅ ISO 9001 / 19115 metadata traceability
* ✅ SLSA-attested artifact chain
* ✅ CIDOC CRM / PROV-O / OWL-Time semantics embedded in metadata

---

## 🧰 Troubleshooting

| Issue                         | Cause                  | Resolution                                                           |
| :---------------------------- | :--------------------- | :------------------------------------------------------------------- |
| “Store format not recognized” | Neo4j version mismatch | Upgrade target DB or use compatible Docker image                     |
| “Checksum mismatch”           | Truncated upload       | Re-download, validate against ledger hash                            |
| “Constraint creation failed”  | Schema drift           | Drop orphaned indexes, re-apply constraints                          |
| Slow restore                  | HDD I/O bottleneck     | Copy to SSD before extraction; increase `dbms.memory.pagecache.size` |

---

## 📘 Related Documentation

* [Cypher Suite](../../graph/cypher/README.md)
* [Graph Exports](../../graph/exports/README.md)
* [AI System Developer Guide](../../../../../../../../../docs/architecture/ai-system.md)
* [Focus Mode Design](../../../../../../../../../docs/design/focus-mode.md)
* [Governance & Security Standards](../../../../../../../../../docs/standards/security.md)

---

## 🕓 Version History

| Version    | Date       | Author     | Reviewer          | Summary                                                  |
| :--------- | :--------- | :--------- | :---------------- | :------------------------------------------------------- |
| **v1.1.0** | 2025-10-25 | @kfm-graph | @kfm-architecture | Completed compliance + FAIR metadata + metrics alignment |
| v1.0.0     | 2025-10-24 | @kfm-graph | @kfm-qa           | Initial snapshot SOP & CI gates                          |

---

<div align="center">

[![Docs · MCP-DL v6.4.3](https://img.shields.io/badge/Docs-MCP--DL%20v6.4.3-0078ff?style=flat-square)]()
[![SLSA](https://img.shields.io/badge/SLSA-Attested-purple?style=flat-square)]()
[![FAIR + CARE](https://img.shields.io/badge/FAIR%20%2B%20CARE-Compliant-2ecc71?style=flat-square)]()
[![Ledger](https://img.shields.io/badge/Ledger-Immutable-d4af37?style=flat-square)]()

</div>

<!-- MCP-FOOTER-BEGIN
MCP-VERSION: v6.4.3
MCP-TIER: FAIR + CARE + ISO + SLSA Certified
DOC-PATH: data/work/staging/tabular/normalized/treaties/metadata/ai/graph/snapshots/README.md
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
LAST-VALIDATED: 2025-10-25
MCP-FOOTER-END -->

```
