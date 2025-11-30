---
title: "🔍 KFM v11 — SHAP Explainability Template (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/pipelines/ai/explainability/templates/shap/README.md"
version: "v11.2.3"
last_updated: "2025-11-29"

release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Explainability WG · FAIR+CARE Council"
content_stability: "stable"
status: "Active / Enforced"

commit_sha: "<latest-commit>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../../../../../releases/v11.2.3/manifest.zip"
attestation_ref: "../../../../../../releases/v11.2.3/slsa-attestation.json"
signature_ref: "../../../../../../releases/v11.2.3/signature.sig"

telemetry_ref: "../../../../../../releases/v11.2.3/shap-explainability-telemetry.json"
telemetry_schema: "../../../../../../schemas/telemetry/ai-explainability-shap-v11.json"
energy_schema: "../../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"

doc_kind: "Explainability Template"
intent: "shap-explainability-template"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Compliant · Sensitivity-Aware"

classification: "Public (Governed)"
sensitivity: "Low/Moderate"
machine_extractable: true
jurisdiction: "United States · Kansas"
accessibility_compliance: "WCAG 2.1 AA+"
---

<div align="center">

# 🔍 **KFM v11 — SHAP Explainability Template**  
`docs/pipelines/ai/explainability/templates/shap/`

**Purpose**  
Provide the **governed v11 template** for producing SHAP-based explainability outputs  
(global SHAP, local SHAP, SHAP summary statistics, feature-importance breakdowns,  
and SHAP-temporal panels) across all KFM AI pipelines.

This template ensures consistent **metadata**, **lineage**, **telemetry**, **validation**,  
and **FAIR+CARE-aware** explainability behaviors.

</div>

---

## 📘 1. Overview

SHAP explainability is the KFM v11 standard for answering:

> **“Which features contributed most to this AI prediction, and in what direction?”**

This template supports:

- **Global SHAP** → variable-level influence across datasets  
- **Local SHAP** → per-row / per-grid-cell explanations  
- **Temporal SHAP** → evolving influence over time  
- **Model-version SHAP** → comparison of how feature importance shifts across updates  
- **Domain-specific SHAP** → climate, soil, hydro, archaeology, ecology, air, wildfire  

All SHAP outputs **must** conform to:

- KFM-MDP v11.2.2  
- KFM Explainability Contract v11  
- STAC/DCAT metadata rules  
- PROV-O lineage  
- OpenLineage event linkage  
- FAIR+CARE ethical constraints  
- Sustainability rules (energy & carbon)

---

## 🗂️ 2. Directory Layout (Emoji-Prefix Standard)

~~~text
docs/pipelines/ai/explainability/templates/shap/
├── 📄 README.md                          # This file
│
├── 🧠 templates/                         # SHAP template artifacts
│   ├── 📊 shap_global_template.parquet
│   ├── 🔍 shap_local_template.parquet
│   ├── 📈 shap_summary_template.json
│   └── 🧬 shap_temporal_template.parquet
│
├── 🌐 stac/                              # STAC templates for SHAP datasets
│   ├── 📄 item-template.json
│   └── 📄 collection-template.json
│
├── 🔗 lineage/                           # PROV-O + OpenLineage template files
│   ├── 🧾 prov-template.json
│   └── 📡 ol-template.json
│
├── 🧪 validation/                        # Validation specs for SHAP outputs
│   ├── 📄 validate-global.md
│   ├── 📄 validate-local.md
│   ├── 📄 validate-summary.md
│   └── 📄 validate-temporal.md
│
└── 📊 examples/                          # Demonstration SHAP outputs
    ├── 📁 global/
    ├── 📁 local/
    ├── 📁 summary/
    └── 📁 temporal/
~~~

---

## 🧬 3. SHAP Explainability Standards (v11)

### Required Attributes for All Outputs

| Field | Required | Description |
|-------|---------|-------------|
| `model:version` | ✔ | Which model produced the SHAP values |
| `kfm:explainability_method` | ✔ | `"shap-global"`, `"shap-local"`, `"shap-summary"`, `"shap-temporal"` |
| `kfm:input_variables` | ✔ | List of input variables used by the model |
| `kfm:energy_wh` | ✔ | Sustainability telemetry |
| `kfm:carbon_gco2e` | ✔ | CO₂ equivalent |
| `kfm:sensitivity_flag` | ✔ | CARE handling on sensitive areas |
| `datetime` | ✔ | For temporal SHAP or inference slices |
| CRS | ✔ | EPSG:4326 unless masked/generalized |
| H3 fields | optional | Required if SHAP outputs mapped to H3 grid |

### Supported Output Types

#### 1. Global SHAP  
Aggregate explanations (mean absolute SHAP, signed mean SHAP, etc.)

#### 2. Local SHAP  
Observation-level explanations, row-by-row or grid-cell–by–grid-cell.

#### 3. SHAP Summary  
Feature importance stacked distributions.

#### 4. SHAP Temporal Panels  
Time-series SHAP values for dynamic modeling.

---

## 🧪 4. Validation Rules (v11)

### ✔ Data Integrity  
- No NaN/inf  
- Correct array shapes  
- Valid CRS/H3 resolution metadata  
- Values within reasonable magnitude (domain-governed)

### ✔ Metadata Completeness  
- STAC item must contain required fields  
- Model version pinned  
- Explainability method correct  
- All input variable names listed  

### ✔ CARE / Sovereignty  
- Sensitive areas masked or generalized  
- CARE flag must be explicit  
- No reverse-engineerable coordinates for protected zones  

### ✔ Sustainability  
- Energy & carbon telemetry within budget  
- Telemetry appended to STAC + lineage  

**Validation failure = fallback → automatic rollback** (Reliability v11).

---

## 🌐 5. STAC Templates

All SHAP explainability datasets MUST publish:

### STAC Item Fields  
- `datetime`  
- `model:version`  
- `kfm:explainability_method`  
- `kfm:input_variables`  
- `kfm:energy_wh`  
- `kfm:carbon_gco2e`  
- `kfm:sensitivity_flag`  
- `assets`: parquet, json, or raster variants  
- `links`: provenance, lineage, governance  

Templates located at:

~~~text
stac/item-template.json
stac/collection-template.json
~~~

---

## 🔗 6. Lineage (PROV-O + OpenLineage)

Each SHAP run must emit:

### PROV-O  
- `prov:Activity` = explainability run  
- `prov:used` = input datasets  
- `prov:generated` = SHAP artifacts  
- `prov:wasAssociatedWith` = pipeline agent  

### OpenLineage  
- Run ID  
- Input dataset references  
- Output SHAP artifact references  
- Duration, rows processed  
- Energy / carbon metadata  

Stored under:

~~~text
lineage/prov-template.json
lineage/ol-template.json
~~~

---

## 📡 7. Telemetry (OTel v11)

Each run MUST export:

- `kfm.expl_energy_wh`  
- `kfm.expl_carbon_gco2e`  
- `kfm.expl_method="shap"`  
- `kfm.expl_cells` (if grid-based)  
- `kfm.expl_latency_ms`  
- CPU/GPU utilization  

Telemetry MUST be included in:

- STAC Item  
- OpenLineage metadata  
- Telemetry release files  

---

## 🎨 8. Rendering Recommendations

- **Global SHAP**: horizontal bar charts, sorted magnitude  
- **Local SHAP**: waterfall charts or cell-wise heatmaps  
- **Temporal SHAP**: multi-panel line series  
- **SHAP Summary**: stacked scatter + violin combos  
- **H3 SHAP**: hexagon tiles (R3–R7) with diverging colormap  

Visualizations should support Focus Mode narrative queries.

---

## 🔮 9. Story Node Integration (Focus Mode v3)

Each SHAP output SHOULD emit a Story Node describing:

- Which variables mattered most  
- How explanations differ across space/time  
- Model evolution and reasoning drift  
- Sensitivity notes for high-risk features  
- FAIR+CARE flags & provenance links  

These power v11 explainability storytelling.

---

## 🧭 10. Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v11.2.3 | 2025-11-29 | Initial v11 explainability template for SHAP outputs; full metadata, lineage, telemetry support. |

---

<div align="center">

🔍 **Kansas Frontier Matrix — SHAP Explainability Template (v11.2.3)**  
Transparent · Reproducible · Ethical · FAIR+CARE-Aligned  

[📘 Docs Root](../../../../../..) · [🧠 Explainability Templates](../README.md) · [🛡 Governance](../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>