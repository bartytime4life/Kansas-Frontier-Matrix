---
title: "🗂️ Kansas Frontier Matrix — Repository Refactor Map (v9.7 → v10) (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/guides/upgrade/repository-refactor-map.md"
version: "v10.4.2"
last_updated: "2025-11-16"
review_cycle: "Release / Continuous · FAIR+CARE Council Oversight"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../releases/v10.4.2/sbom.spdx.json"
manifest_ref: "../../../releases/v10.4.2/manifest.zip"
telemetry_ref: "../../../releases/v10.4.2/pipeline-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/upgrade-repository-refactor-map-v1.json"
governance_ref: "../../../docs/standards/governance/ROOT-GOVERNANCE.md"
data_contract_ref: "../../../docs/contracts/data-contract-v3.json"
license: "MIT / CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4.2"
status: "Active / Enforced"
doc_kind: "Refactor Map"
intent: "v9.7-to-v10-reorganization"
care_label: "C2-A2-R2-E1"
fair_category: "F1-A1-I1-R1"
machine_extractable: true
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"
semantic_document_id: "kfm-doc-repository-refactor-map"
doc_uuid: "urn:kfm:doc:repo-refactor-map-v10.4.2"
---

<div align="center">

# 🗂️ **Kansas Frontier Matrix — Repository Refactor Map (v9.7 → v10)**  
`docs/guides/upgrade/repository-refactor-map.md`

**Purpose**  
Define the **complete, authoritative, FAIR+CARE-aligned** refactor mapping required to migrate the KFM monorepo from **v9.7.x** to the **v10 architecture**.  
This includes directory migrations, file splits, consolidations, deprecations, and updated governance/telemetry boundaries.

</div>

---

# 📘 Overview

The v10 repository reorganizes the entire KFM system into a **clean, modular, pipeline-aligned structure**.  
This refactor enables:

- Streaming ETL (Kafka/webhooks)  
- Predictive pipelines  
- Focus Mode v2.5  
- Lineage v2 (PROV-O · GeoSPARQL · CIDOC CRM)  
- Governance Ledger automation  
- Telemetry v2 (energy · carbon · A11y · CARE)  
- Strict documentation enforcement (KFM-MDP v10.4.2)  

This document provides:

- **Directory-to-directory mapping**  
- **File-level transformations**  
- **Deprecation table**  
- **Refactor-driven CI/CD impacts**  
- **Governance & FAIR+CARE implications**  

---

~~~text
# ──────────────────────────────────────────────────────────────
#  Kansas Frontier Matrix — Directory Mapping Format Standard  
# ──────────────────────────────────────────────────────────────

v9.7/                                          →       v10/
──────────────────────────────────────────────────────────────────────────────
src/                                           →       src/
│   ├── api/                                   →       │   ├── api/                     # same module
│   ├── etl/                                   →       │   ├── pipelines/ingestion/      # moved
│   ├── rs/ (remote sensing)                   →       │   ├── pipelines/remote_sensing/ # renamed
│   ├── ai/                                    →       │   ├── ai/                        # expanded (focus_v2)
│   ├── graph/                                 →       │   ├── graph/                     # same (schema v2)
│   ├── telemetry/                             →       │   ├── telemetry/                 # expanded (Telemetry v2)
│   └── web/                                   →       │   └── web/                       # refactored components/features
│
data/                                          →       data/
│   ├── raw/                                   →       │   ├── raw/                       # same
│   ├── processed/                             →       │   ├── processed/                 # same
│   ├── stac/                                  →       │   ├── stac/                      # enhanced: DCAT mirror
│   └── lineage/                               →       │   └── lineage/                   # Lineage v2 schema
│
docs/                                          →       docs/
│   ├── api/                                   →       │   ├── standards/api/             # merged
│   ├── pipelines/                             →       │   ├── guides/pipelines/          # reorganized
│   ├── rs/                                    →       │   ├── guides/visualization/      # SVF/LRM separated
│   └── governance/                            →       │   └── standards/governance/      # governance v2
│
.github/                                       →       .github/
│   └── workflows/                             →           └── workflows/                  # updated: 11 validators
│
tools/                                         →       tools/                              # same; reorganized
tests/                                         →       tests/                              # hierarchy expanded
Makefile                                       →       Makefile                            # command targets updated
docker-compose.yml                             →       docker-compose.yml                  # Kafka + Neo4j 5.x added
~~~ 


---

# 🏗️ Detailed Subsystem Mapping (Fine-Grained)

## 1. **ETL / Pipelines**

~~~text
v9.7/src/etl/                              →   v10/src/pipelines/ingestion/
v9.7/src/etl/transforms/                   →   v10/src/pipelines/ingestion/transforms/
v9.7/src/etl/validators/                   →   v10/src/pipelines/validation/
v9.7/src/etl/stac/                         →   v10/src/pipelines/publishing/stac/
v9.7/src/etl/release/                      →   v10/src/pipelines/reliable_auto_release/
~~~

Changes:
- Introduces **RunContext v2**, **Idempotency Keys**, and **Telemetry v2 hooks**  
- Publishing split into STAC/DCAT/predictive

---

## 2. **Remote Sensing (RS)**

~~~text
v9.7/src/rs/                                →   v10/src/pipelines/remote_sensing/
v9.7/src/rs/svf.py                          →   v10/src/pipelines/remote_sensing/svf/
v9.7/src/rs/lrm.py                          →   v10/src/pipelines/remote_sensing/lrm/
v9.7/src/rs/bandstack.py                    →   v10/src/pipelines/remote_sensing/bandstack/
~~~

New:
- RTC (SAR)  
- GSD harmonization  
- Cloud/shadow/snow masking  
- CARE v2 geo-generalization pipeline hooks  

---

## 3. **AI / Focus Mode**

~~~text
v9.7/src/ai/focus_mode/                     →   v10/src/ai/focus_transformer_v2/
v9.7/src/ai/explainer/                      →   v10/src/ai/explainability/
v9.7/src/ai/prompts/                        →   v10/src/ai/prompting/
~~~

New features:
- Subgraph explainability  
- Sovereignty-aware reasoning  
- CARE-aware narrative constraints  

---

## 4. **Graph / Neo4j**

~~~text
v9.7/src/graph/schema.cypher                →   v10/src/graph/schema_v2.cypher
v9.7/src/graph/loaders/                     →   v10/src/graph/loaders/
v9.7/src/graph/queries/                     →   v10/src/graph/queries/
~~~

Lineage v2 integration:
- `prov:Activity`, `prov:Entity`, `cidoc:E5_Event`, `geo:Feature` relations  

---

## 5. **Web / UI**

~~~text
v9.7/web/src/components/                    →   v10/web/src/components/ (refactored)
v9.7/web/src/map/                           →   v10/web/src/components/MapView/
v9.7/web/src/focus/                         →   v10/web/src/components/FocusMode/
v9.7/web/src/timeline/                      →   v10/web/src/components/TimelineView/
v9.7/web/src/utils/                         →   v10/web/src/utils/ (same; expanded)
~~~

Enhancements:
- MapLibre v10 runtime theming  
- A11y tokens  
- Focus Mode v2.5 panel model  
- Telemetry v2 UI hooks  

---

## 6. **Documentation (Docs)**

~~~text
v9.7/docs/pipelines/                        →   v10/docs/guides/pipelines/
v9.7/docs/rs/                                →   v10/docs/guides/visualization/
v9.7/docs/governance/                        →   v10/docs/standards/governance/
v9.7/docs/howto/                             →   v10/docs/guides/
v9.7/docs/architecture.md                    →   v10/docs/architecture/ (split by subsystem)
~~~

Significant upgrades:
- Adoption of strict **KFM-MDP v10.4.2**  
- All guides contain full YAML metadata  
- CI enforces documentation validity  

---

## 7. **Telemetry System**

~~~text
v9.7/src/telemetry/                          →   v10/src/telemetry/
v9.7/data/telemetry/                         →   v10/data/work/telemetry/
~~~

Telemetry v2 includes:
- Energy (J)  
- Carbon (gCO₂e)  
- A11y usage  
- CARE masking events  
- Predictive pipeline metrics  

---

## 8. **Governance / FAIR+CARE**

~~~text
v9.7/docs/governance/CARE.md                 →   v10/docs/standards/faircare.md
v9.7/docs/governance/ledger/                 →   v10/docs/standards/governance/LEDGER/
v9.7/src/etl/care/                           →   v10/src/pipelines/governance/
~~~

Upgrades:
- CARE v2  
- Sovereignty overlays  
- Ledger signatures (SHA-256)  

---

# 🗃️ Deprecation Map (v9.7 Removed in v10)

| v9.7 Asset | Status | Replacement |
|------------|--------|-------------|
| `ai/focus_mode_v1` | ❌ Removed | `ai/focus_transformer_v2` |
| `etl/release/` | ❌ Removed | `pipelines/reliable_auto_release/` |
| `rs/hillshade.py` | ❌ Removed | SVF/LRM workflows |
| `docs/pipelines/overview.md` | ❌ Removed | new pipeline guides |
| `docs/rs/methods.md` | ❌ Removed | visualization/svf-lrm guides |
| `stac/lite/` | ❌ Removed | unified STAC/DCAT v3 |

---

# 🔧 CI/CD Impacts

## New Required Workflows (11 Gates)

~~~text
.github/workflows/
├── stac-validate.yml
├── dcat-validate.yml
├── graph-validate.yml
├── lineage-validate.yml
├── telemetry-validate.yml
├── faircare-validate.yml
├── streaming-etl-test.yml
├── predictive-test.yml
├── focus-v2-test.yml
├── docs-lint.yml
└── ledger-validate.yml
~~~

All must pass for merge approval.

---

# ⚖️ FAIR+CARE & Governance Implications

Refactor changes affect:

- **CARE masking boundaries** (new H3-based masking pipeline)  
- **Sovereignty overlays** (moved into governance subsystem)  
- **Lineage requirements** (v2 metadata mandatory)  
- **Telemetry ethics** (A11y, energy, carbon required)  
- **Dataset consent rules** (updated CARE v2 enforcement)  

---

# 🧪 Validation Before Migration Completion

Run the full suite:

```bash
make validate-all
````

Expect 0 failures.

---

# 🕰 Version History

| Version | Date       | Summary                                                              |
| ------: | ---------- | -------------------------------------------------------------------- |
| v10.4.2 | 2025-11-16 | Fully upgraded refactor map with lined style, governance integration |
| v10.0.0 | 2025-11-08 | Initial repository refactor map                                      |
|  v9.7.x | 2025-05-01 | Pre-refactor baseline                                                |

---

<div align="center">

© 2025 Kansas Frontier Matrix
Master Coder Protocol v6.3 · FAIR+CARE v2 Certified
Diamond⁹ Ω / Crown∞Ω Ultimate Certified

[Back to Upgrade Index](./README.md)

</div>
