---
title: "📋 Kansas Frontier Matrix — v10 Migration Checklist (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/guides/upgrade/migration-checklist.md"
version: "v10.4.2"
last_updated: "2025-11-16"
review_cycle: "Release / Continuous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../releases/v10.4.2/sbom.spdx.json"
manifest_ref: "../../../releases/v10.4.2/manifest.zip"
telemetry_ref: "../../../releases/v10.4.2/pipeline-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/upgrade-migration-checklist-v1.json"
governance_ref: "../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "MIT / CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4.2"
status: "Active / Enforced"
doc_kind: "Checklist"
intent: "v9.7-to-v10-migration"
fair_category: "F1-A1-I1-R1"
care_label: "C2-A2-R2-E1"
sensitivity_level: "None"
machine_extractable: true
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"
semantic_document_id: "kfm-doc-v10-migration-checklist"
doc_uuid: "urn:kfm:doc:v10-migration-checklist-v10.4.2"
---

<div align="center">

# 📋 **Kansas Frontier Matrix — v10 Migration Checklist**  
`docs/guides/upgrade/migration-checklist.md`

**Purpose**  
Provide the complete, authoritative, FAIR+CARE-aligned checklist for upgrading any Kansas Frontier Matrix (KFM) deployment from **v9.7.x → v10.x**.  
This ensures every upgraded environment meets **FAIR+CARE v2**, **Lineage v2**, **Streaming ETL**, **Predictive Pipelines**, **Focus Mode v2.5**, **STAC/DCAT v3**, and **MCP-DL v6.3** requirements.

</div>

---

# 🧭 How to Use This Checklist

- Complete each section **in order**.  
- Every “BLOCKER ❌” item **must be resolved before proceeding**.  
- After all categories pass, run the **Upgrade Validation Suite**.  
- Final confirmation requires **Governance Ledger approval**.

---

# 🗂️ Directory Context (v10 Upgrade)

~~~text
docs/guides/upgrade/
├── README.md
├── v10-readiness.md
├── v10-inventory.md
├── migration-checklist.md     # ← THIS FILE
├── breaking-changes.md
├── repository-refactor-map.md
├── upgrade-validation-suite.md
└── deprecated-features.md
~~~

---

# ✅ Phase 1 — Pre-Migration Requirements

## 🔐 1. System & Environment Baseline
- [ ] Python **3.12+**
- [ ] Node.js **20+**
- [ ] Docker **26+**
- [ ] Docker Compose **v2**
- [ ] Neo4j **5.x Enterprise or Community**
- [ ] Kafka **3.x** (if using streaming ETL)
- BLOCKER ❌: Any environment below minimum version.

---

## 🗄 2. Backups & Snapshots
- [ ] Run `neo4j-admin dump` and store off-box  
- [ ] Archive the following directories:
  - `data/raw/`
  - `data/processed/`
  - `data/stac/`
  - `data/work/lineage/`
- [ ] Export `.env` and secrets  
- BLOCKER ❌: Missing Neo4j dump.

---

## 📚 3. Documentation Compliance
- [ ] All existing Markdown files pass `make docs-lint`  
- [ ] All READMEs contain valid YAML front matter  
- BLOCKER ❌: Any doc failing KFM-MDP v10.4.2 rules.

---

# 🔧 Phase 2 — Code & Pipeline Migration

## 🏗 4. Directory Refactor (v9.7 → v10)
- [ ] Apply full mapping from `repository-refactor-map.md`  
- [ ] Move legacy ETL to `src/pipelines/ingestion/`  
- [ ] Move Focus v1 → `src/ai/focus_transformer_v2/`  
- [ ] Restructure web client into components/features architecture  
- BLOCKER ❌: Any legacy folder still referenced.

---

## 🛰 5. STAC/DCAT Catalog Migration
- [ ] Rebuild STAC Items using v10 schemas  
- [ ] Regenerate DCAT v3 datasets  
- [ ] Sync STAC↔DCAT mirrors  
- [ ] Validate Item → Collection references  
- BLOCKER ❌: Any STAC validation failure.

---

## 🌐 6. API Migration
- [ ] Enable new REST + GraphQL hybrid  
- [ ] Apply new JWT/OAuth2 config  
- [ ] Update all client calls to new endpoints  
- BLOCKER ❌: Any endpoint returning 400/500.

---

## 🔁 7. ETL Migration (Batch + Streaming)
### Batch (Existing)
- [ ] Confirm all batch pipelines produce v10 STAC  
- [ ] Migrate to new `RunContext v2`  

### Streaming (New)
- [ ] Configure Kafka topics  
- [ ] Configure streaming watchers  
- [ ] Test ETag-based conditional fetch  
- BLOCKER ❌: Streaming ingestion not producing STAC Items.

---

## 🤖 8. Focus Mode v2.5 Migration
- [ ] Replace all v1 prompt logic  
- [ ] Enable SHAP/LIME explainability  
- [ ] Validate subgraph-aware reasoning  
- BLOCKER ❌: Any hallucination or ungrounded narrative.

---

# 🔬 Phase 3 — Data Integrity & Governance

## 🧬 9. Lineage v2 Enforcement
- [ ] PROV-O Activities  
- [ ] CIDOC CRM alignment  
- [ ] GeoSPARQL geometries  
- [ ] CARE metadata  
- [ ] Telemetry references  
- BLOCKER ❌: Missing provenance link.

---

## 🛡 10. FAIR+CARE v2 Governance
- [ ] CARE masking for sensitive AOIs  
- [ ] Sovereignty overlays applied  
- [ ] Masking strategies declared  
- [ ] No sensitive coordinates leaked  
- [ ] Ethical content validated  
- BLOCKER ❌: Any CARE violation.

---

## 📡 11. Telemetry v2 Compliance
- [ ] Energy (J)  
- [ ] Carbon (gCO₂e)  
- [ ] A11y usage  
- [ ] CARE decision logs  
- [ ] Inference latency  
- BLOCKER ❌: Any missing telemetry field.

---

# 🧪 Phase 4 — Full Test & CI Validation

## 🧰 12. Required CI Pipelines
- [ ] `stac-validate.yml`
- [ ] `dcat-validate.yml`
- [ ] `graph-validate.yml`
- [ ] `streaming-etl-test.yml`
- [ ] `predictive-test.yml`
- [ ] `focus-v2-test.yml`
- [ ] `lineage-validate.yml`
- [ ] `telemetry-validate.yml`
- [ ] `faircare-validate.yml`
- [ ] `docs-lint.yml`
- [ ] `ledger-validate.yml`
- BLOCKER ❌: Any failing workflow.

---

# 🧾 Final Approval — Governance Ledger

## 📜 13. Governance Ledger Requirements
- [ ] Ledger entry generated  
- [ ] SHA-256 signature verified  
- [ ] Telemetry references included  
- [ ] Lineage references included  
- [ ] FAIR+CARE status = Pass  
- BLOCKER ❌: Ledger entry missing or unsigned.

---

# 🎉 Final Confirmation

Once **all** items above pass:

👉 The system is **officially certified as v10 compliant**  
👉 All pipelines may resume scheduled production  
👉 FAIR+CARE Council receives audit bundle  

---

# 🕰 Version History

| Version | Date | Summary |
|--------:|-------------|---------------------------------------------|
| v10.4.2 | 2025-11-16 | Full v10 migration checklist with 40+ validators |
| v10.0.0 | 2025-11-08 | Initial migration checklist |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
Master Coder Protocol v6.3 · FAIR+CARE v2 · Diamond⁹ Ω / Crown∞Ω Certified  
[Back to Upgrade Index](./README.md)

</div>
