---
title: "💥 Kansas Frontier Matrix — Breaking Changes (v9.7 → v10) (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/guides/upgrade/breaking-changes.md"
version: "v10.4.2"
last_updated: "2025-11-16"
review_cycle: "Release / Postmortem"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../releases/v10.4.2/sbom.spdx.json"
manifest_ref: "../../../releases/v10.4.2/manifest.zip"
telemetry_ref: "../../../releases/v10.4.2/pipeline-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/upgrade-breaking-changes-v1.json"
governance_ref: "../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "MIT / CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4.2"
status: "Active / Enforced"
doc_kind: "Upgrade Report"
intent: "breaking-changes-v10"
fair_category: "F1-A1-I1-R1"
care_label: "C2-A2-R2-E1"
sensitivity_level: "None"
machine_extractable: true
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"
semantic_document_id: "kfm-doc-breaking-changes"
doc_uuid: "urn:kfm:doc:breaking-changes-v10.4.2"
---

<div align="center">

# 💥 **Kansas Frontier Matrix — Breaking Changes (v9.7 → v10)**  
`docs/guides/upgrade/breaking-changes.md`

**Purpose**  
Define every *breaking change* introduced in the upgrade from **KFM v9.7.x → v10**, covering:  
- API behavior  
- Directory structure  
- ETL pipelines  
- STAC/DCAT cataloging  
- Focus Mode architecture  
- Neo4j schema  
- Governance & FAIR+CARE enforcement  
- Telemetry requirements  

This ensures all deployments upgrading to **v10.x** can reconcile incompatibilities cleanly.

</div>

---

# 🗂️ Upgrade Directory Context

~~~text
docs/guides/upgrade/
├── README.md
├── v10-readiness.md
├── v10-inventory.md
├── migration-checklist.md
├── repository-refactor-map.md
├── upgrade-validation-suite.md
├── deprecated-features.md
└── breaking-changes.md          # ← THIS FILE
~~~

---

# ⚠️ Overview of Breaking Changes in v10

v10 is a **foundational upgrade** introducing:

- **Streaming ETL** (Kafka/Webhooks)  
- **Predictive pipelines**  
- **Focus Mode v2.5**  
- **STAC/DCAT v3 catalog parity**  
- **Neo4j Schema v2**  
- **Lineage v2**  
- **Telemetry v2 (energy + carbon)**  
- **FAIR+CARE v2 governance**  

These advances require significant structural, interface, and behavioral changes across the entire codebase.

---

# 💥 1. Directory Structure (Breaking)

~~~text
# ──────────────────────────────────────────────────────────────
#  v9.7 → v10 Directory Changes (Breaking)
# ──────────────────────────────────────────────────────────────

v9.7/src/etl/                               →   v10/src/pipelines/ingestion/
v9.7/src/rs/                                →   v10/src/pipelines/remote_sensing/
v9.7/src/ai/focus_mode_v1/                  →   v10/src/ai/focus_transformer_v2/
v9.7/web/src/focus/                         →   v10/web/src/components/FocusMode/
v9.7/web/src/map/                           →   v10/web/src/components/MapView/
v9.7/web/src/timeline/                      →   v10/web/src/components/TimelineView/
v9.7/data/stac/lite/                        →   REMOVED (STAC-lite deprecated)
v9.7/docs/pipelines/                        →   v10/docs/guides/pipelines/ (split)
v9.7/data/lineage/                          →   v10/data/lineage/ (schema upgraded)
~~~

**Impact:**  
Old imports, paths, and CI references **break** until migrated.

---

# 💥 2. Focus Mode v1 → v2.5 (Breaking)

## Removed:
- Prompt-only reasoning  
- Non-deterministic summaries  
- No SHAP/LIME  
- No sovereignty masking  
- No subgraph filtering  
- v1 API endpoints

## Replacement:
- **Focus Transformer v2.5**  
- Graph-anchored reasoning  
- SHAP/LIME explainability  
- CARE-aware content control  
- New REST + GraphQL endpoints

**All clients referencing Focus v1 **WILL BREAK**.

---

# 💥 3. API Changes (Breaking)

| v9.7 Endpoint | v10 Status | Replacement |
|---------------|------------|-------------|
| `/focus/v1/{id}` | ❌ removed | `/focus/v2/entity/{id}` |
| `/etl/release/run` | ❌ removed | `/pipeline/auto-release/run` |
| `/stac/lite/{item}` | ❌ removed | `/stac/v10/items/{id}` |
| `/graph/query` | ❌ changed | GraphQL endpoint |
| `/terrain/hillshade` | ❌ deprecated | `/terrain/svf`, `/terrain/lrm` |

**All v9.7 API responses differ from new v10 schemas.**

---

# 💥 4. STAC & DCAT Changes (Breaking)

## ❌ Removed
- “STAC Lite”  
- Old Item/Collection v9.7 schemas  
- Non-hashed assets  
- Items without provenance  
- Missing DCAT mirror entries  

## ✔ Required in v10
- Full STAC 1.0.0 compliance  
- DCAT 3.0 JSON-LD parity  
- `kfm:*` fields (FAIR+CARE, provenance, lineage)  
- Collection searchability  
- Live STAC↔DCAT mirroring

**Old STAC Items cannot be re-used without migration.**

---

# 💥 5. Neo4j Schema v2 (Breaking)

## Changes:
- New superclasses for datasets, scenes, and entities  
- `:SensorStream`, `:Prediction`, `:EventInterval` added  
- New required relationships:
  - `:DERIVED_FROM`
  - `:HAS_ASSET`
  - `:FEDERATED_WITH`
- Geometry fields require WKT/GeoJSON compliance  
- All nodes must include `kfm:version`

**Old graph schemas fail migrations automatically.**

---

# 💥 6. ETL Changes (Batch → Streaming)

Streaming support is now **mandatory** for certain pipelines.

## Removed:
- Legacy CSV pollers  
- Shell-based ETL scripts  
- v9.7 release ETL  

## Required:
- Streaming ingestion using:
  - Kafka topics  
  - Webhooks  
  - ETag conditional fetch  
- Idempotent pipelines w/ RunContext v2  
- SemVer-based artifact promotion  

**Old ETL must be rebuilt or upgraded.**

---

# 💥 7. Lineage v1 → v2 (Breaking)

Lineage v2 introduces:

- PROV-O Activity modeling  
- CIDOC-CRM semantics  
- GeoSPARQL geometry validation  
- CARE masking evidence  
- Telemetry binding (`lineageRef` and `telemetryRef`)  
- Required SHA-256 signatures  

Lineage v1 files cannot be accepted by CI.

---

# 💥 8. Telemetry v2 (Breaking)

Old telemetry lacked:

- Energy (J)  
- Carbon (gCO₂e)  
- Inference latency  
- Accessibility metrics  
- CARE decision logs  

Telemetry v2 requires:

- NDJSON  
- Required fields (validated by CI)  
- Storage in release bundle  
- Sync to Governance Ledger  

---

# 💥 9. CARE v1 → CARE v2 (Breaking)

New CARE v2 enforcement introduces:

- Sovereignty overlays (required)  
- H3 R7/R5 generalization  
- Masking strategy inclusions  
- Sensitive-site governance controls  
- FAIR+CARE-delimited content in Focus Mode  

Any pipeline using CARE v1 metadata will fail.

---

# 💥 10. CI/CD Validators (Breaking)

v10 requires **11 mandatory validators**, including:

- `stac-validate.yml`  
- `dcat-validate.yml`  
- `lineage-validate.yml`  
- `telemetry-validate.yml`  
- `faircare-validate.yml`  
- `governance-ledger.yml`  
- `docs-lint.yml`  
- `predictive-test.yml`  
- `streaming-etl-test.yml`  

v9.7 CI workflows are incompatible.

---

# 🛠 Summary of Required Developer Actions

- [ ] Migrate all directory imports to v10 structure  
- [ ] Replace all deprecated API endpoints  
- [ ] Rebuild STAC/DCAT Items using v10 schemas  
- [ ] Upgrade graph schema via `migrate_v10.cypher`  
- [ ] Convert pipelines to RunContext v2  
- [ ] Ensure sovereign masking + CARE v2 compliance  
- [ ] Regenerate lineage using v2 export  
- [ ] Ensure telemetry v2 emission  
- [ ] Pass all 11 CI validators  
- [ ] Ensure Governance Ledger entry is signed  

---

# 🕰 Version History

| Version | Date | Summary |
|--------:|-------------|---------------------------------------------|
| v10.4.2 | 2025-11-16 | Full breaking-changes rewrite w/ lined directory style |
| v10.0.0 | 2025-11-08 | Initial breaking changes list |
| v9.7.x | 2025-05-01 | Pre-migration baseline |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
Master Coder Protocol v6.3 · FAIR+CARE v2  
Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[Back to Upgrade Index](./README.md)

</div>
