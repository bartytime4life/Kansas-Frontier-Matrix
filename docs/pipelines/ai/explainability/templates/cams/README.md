---
title: "🌍 KFM v11 — CAMS Explainability Template (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/pipelines/ai/explainability/templates/cams/README.md"
version: "v11.2.3"
last_updated: "2025-11-29"

release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Climate AI Working Group · FAIR+CARE Council"
content_stability: "stable"
status: "Active / Enforced"

commit_sha: "<latest-commit>"
previous_version_hash: "<previous-version-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../../../../../releases/v11.2.3/manifest.zip"
attestation_ref: "../../../../../../releases/v11.2.3/slsa-attestation.json"
signature_ref: "../../../../../../releases/v11.2.3/signature.sig"

telemetry_ref: "../../../../../../releases/v11.2.3/cams-explainability-telemetry.json"
telemetry_schema: "../../../../../../schemas/telemetry/ai-explainability-cams-template-v11.json"
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
intent: "cams-explainability-template"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Compliant · Climate Transparency"

classification: "Public (Governed)"
sensitivity: "Low/Moderate"
machine_extractable: true
jurisdiction: "United States · Kansas"
accessibility_compliance: "WCAG 2.1 AA+"
---

<div align="center">

# 🌍 **KFM v11 — CAMS Explainability Template**  
`docs/pipelines/ai/explainability/templates/cams/`

**Purpose**  
Provide the **governed v11 template** for explainability artifacts produced from  
**CAMS (Copernicus Atmosphere Monitoring Service)** climate model inputs and AI-driven inference layers.  

This template standardizes:  
- SHAP global/local maps  
- Sensitivity / gradient maps  
- Model-response maps  
- Attribution grids (lat/lon or H3)  
- Temporal influence maps  
- JSON-LD semantic metadata  
- Lineage (PROV-O + OpenLineage)  
- FAIR+CARE alignment  

Used by: climate, air-quality, wildfire/smoke, PM2.5/ozone inference pipelines.

</div>

---

## 📘 1. Overview

CAMS provides global climate & atmospheric fields (ozone, aerosols, PM2.5, wind, humidity, trace gases).  
These fields feed numerous KFM AI pipelines (air quality, hazard modeling, climate downscaling, smoke transport explainers).

Explainability provides insight into:

- **Which CAMS variables influenced predictions?**  
- **Where spatial patterns explain behavior?**  
- **Whether model reasoning changed over time?**  
- **What tradeoffs exist between sensitivity, signal, and geographic risk?**

This template ensures **consistent, provenance-rich, privacy-aware** explainability behavior.

---

## 🗂️ 2. Directory Layout (Emoji-Prefix Standard)

~~~text
docs/pipelines/ai/explainability/templates/cams/
├── 📄 README.md                          # This file
│
├── 🧠 templates/                         # CAMS-specific attribution templates
│   ├── 🌍 shap_global_template.parquet
│   ├── 📍 shap_local_template.parquet
│   ├── 🔬 sensitivity_template.parquet
│   ├── 🧭 h3_attribution_template.parquet
│   └── 🕒 temporal_influence_template.parquet
│
├── 🌐 stac/                              # STAC templates
│   ├── 📄 item-template.json
│   └── 📄 collection-template.json
│
├── 🔗 lineage/                           # PROV-O + OpenLineage binding templates
│   ├── 🧾 prov-template.json
│   └── 📡 ol-template.json
│
├── 🧪 validation/                        # Validation rules + scripts
│   ├── 📄 validate-global.md
│   ├── 📄 validate-local.md
│   ├── 📄 validate-sensitivity.md
│   ├── 📄 validate-h3.md
│   └── 📄 validate-temporal.md
│
└── 📊 examples/                          # Example outputs for CAMS explainability
    ├── 📁 global/
    ├── 📁 local/
    ├── 📁 sensitivity/
    ├── 📁 h3/
    └── 📁 temporal/
~~~

---

## 🧬 3. Explainability Standards (v11)

Each explainability artifact MUST include:

| Field | Requirement | Description |
|-------|-------------|-------------|
| `model:version` | ✔ | CAMS-driven AI model version |
| `kfm:explainability_method` | ✔ | shap-global, shap-local, sensitivity, gradient |
| `kfm:domain` | ✔ | `"climate"` or `"air"` |
| `kfm:input_variables` | ✔ | CAMS variable names used in model training |
| `datetime` | ✔ | Timestamp associated with inference/explainability window |
| `kfm:h3_res` | if H3 | Target hex resolution |
| `kfm:energy_wh` | ✔ | Compute energy consumption |
| `kfm:carbon_gco2e` | ✔ | Environmental impact |
| `kfm:sensitivity_flag` | ✔ | CARE-sensitive areas handled properly |
| CRS/H3 fields | conditional | Required for spatial outputs (EPSG:4326) |

Supported Output Types:

- **Global SHAP** (per-variable influence)  
- **Local SHAP** (per-event explanation)  
- **Sensitivity/Gradient Fields**  
- **Temporal Influence Maps**  
- **H3 Attribution**  

---

## 🧪 4. Validation Requirements

### ✔ Metadata Validation  
- STAC Item completeness  
- Input variable names  
- Explainability method correctness  
- Temporal alignment with CAMS input windows  

### ✔ Spatial Integrity  
- Valid arrays/grids  
- CRS correctness  
- No NaN/inf values  
- H3 resolution consistent with metadata  

### ✔ Governance & CARE  
- Sensitive atmospheric areas masked (if applicable)  
- No disclosure of protected layout regions  
- All outputs carry CARE tags  

### ✔ Sustainability  
- Energy + carbon budget respected  
- Telemetry exported to STAC + OpenLineage  

Failure → rollback (Reliability Layer v11).

---

## 🌐 5. STAC Templates

Templates for STAC Item + Collection MUST contain:

- `datetime`  
- `start_datetime` / `end_datetime`  
- `model:version`  
- `kfm:explainability_method`  
- `kfm:energy_wh`  
- `kfm:carbon_gco2e`  
- Attribution asset links  
- Provenance blocks  

Stored under:

~~~text
stac/item-template.json
stac/collection-template.json
~~~

---

## 🔗 6. Provenance (OpenLineage + PROV-O)

Each CAMS explainability run MUST include:

### PROV-O  
- `prov:Activity` — explainability pipeline  
- `prov:used` — CAMS inputs, model artifact  
- `prov:generated` — explainability outputs  
- `prov:wasAssociatedWith` — actor/agent  

### OpenLineage  
- runId  
- input & output asset pointers  
- timing & hardware metadata  

Stored under:

~~~text
lineage/prov-template.json
lineage/ol-template.json
~~~

---

## 📡 7. Telemetry (OTel v11)

Explainability run MUST emit:

- `kfm.expl_method="cams"`  
- `kfm.expl_energy_wh`  
- `kfm.expl_carbon_gco2e`  
- `kfm.expl_latency_ms`  
- `kfm.rows_processed`  
- GPU/CPU metrics  

Telemetry MUST be linked to STAC + lineage.

---

## 🧭 8. Story Node Integration (Focus Mode v3)

CAMS explainability outputs generate **Story Nodes** describing:

- Spatial + temporal attribution patterns  
- Dominant climate drivers  
- Event-scale and global-scale influences  
- FAIR+CARE notes  
- Evidence trails (lineage + telemetry)  

Enables explainable climate narratives in the KFM UI.

---

## 🧭 9. Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v11.2.3 | 2025-11-29 | Initial v11 CAMS explainability template; CARE, lineage, and STAC alignment. |

---

<div align="center">

🌍 **Kansas Frontier Matrix — CAMS Explainability Template (v11.2.3)**  
Transparent · Explainable · FAIR+CARE · Climate-Sensitive · Provenance-Driven  

[📘 Docs Root](../../../../../..) · [🧠 Explainability Templates](../README.md) · [🛡 Governance](../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>