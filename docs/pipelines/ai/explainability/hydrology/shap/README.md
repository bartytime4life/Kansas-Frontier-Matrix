---
title: "💧🔍 KFM v11 — Hydrology SHAP Explainability Template (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/pipelines/ai/explainability/hydrology/shap/README.md"
version: "v11.2.3"
last_updated: "2025-11-29"

release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Hydrology AI WG · FAIR+CARE Council"
content_stability: "stable"
status: "Active / Enforced"

commit_sha: "<latest-commit>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../../../../../releases/v11.2.3/manifest.zip"
attestation_ref: "../../../../../../releases/v11.2.3/slsa-attestation.json"
signature_ref: "../../../../../../releases/v11.2.3/signature.sig"

telemetry_ref: "../../../../../../releases/v11.2.3/hydro-shap-explainability-telemetry.json"
telemetry_schema: "../../../../../../schemas/telemetry/ai-explainability-hydrology-shap-v11.json"
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

doc_kind: "Explainability Module"
intent: "hydrology-shap-explainability"
fair_category: "F1-A1-I1-R2"
care_label: "CARE-Compliant · Watershed-Sensitive · Explainability-Safe"

classification: "Public (Governed)"
sensitivity: "Low/Moderate (Hydrology + watershed sensitivity)"
machine_extractable: true
jurisdiction: "United States · Kansas"
accessibility_compliance: "WCAG 2.1 AA+"
---

<div align="center">

# 💧🔍 **Hydrology SHAP Explainability (KFM v11)**  
`docs/pipelines/ai/explainability/hydrology/shap/`

**Purpose**  
Establish the **v11 SHAP explainability template** for all hydrology AI pipelines relying on  
CAMS/climate drivers, soil moisture, DEM/terrain layers, hydric soils, landcover, and watershed-level features.

This provides governed, reproducible, FAIR+CARE-aligned attribution for watershed modeling and flood, runoff,  
and infiltration predictions.

</div>

---

## 📘 1. Overview

Hydrology SHAP explainability answers:

> **“Which variables most influenced this hydrologic prediction, and where?”**

Hydrology models often depend on climate + soil + terrain + hydrodynamic inputs:

- CAMS precipitation/PM2.5/aerosols  
- Soil moisture / hydric soils  
- DEM + slope/aspect/TPI  
- Landcover transitions  
- Watershed properties (HUC-structured metadata)

SHAP maps reveal watershed-scale drivers, climate contributions, and sensitivity patterns.

---

## 🗂️ 2. Directory Layout (Emoji-Prefix Standard)

~~~text
docs/pipelines/ai/explainability/hydrology/shap/
├── 📄 README.md
│
├── 🧠 templates/
│   ├── 🌍 shap_global_template.parquet
│   ├── 📍 shap_local_template.parquet
│   ├── 📈 shap_summary_template.json
│   └── 🧭 shap_h3_template.parquet
│
├── 🌐 stac/
│   ├── 📄 item-template.json
│   └── 📄 collection-template.json
│
├── 🔗 lineage/
│   ├── 🧾 prov-template.json
│   └── 📡 ol-template.json
│
├── 🧪 validation/
│   ├── 📄 validate-global.md
│   ├── 📄 validate-local.md
│   ├── 📄 validate-summary.md
│   ├── 📄 validate-h3.md
│   └── 📄 validate-watershed.md
│
└── 📊 examples/
    ├── 📁 global/
    ├── 📁 local/
    ├── 📁 summary/
    └── 📁 h3/
~~~

---

## 🧬 3. SHAP Explainability Standards (v11)

Each hydrology SHAP output MUST include:

| Field | Required | Description |
|-------|----------|-------------|
| `model:version` | ✔ | Hydrology AI model version |
| `kfm:domain` | ✔ | `"hydrology"` |
| `kfm:explainability_method` | ✔ | shap-global, shap-local, shap-summary |
| `kfm:input_variables` | ✔ | Climate + soil + terrain + hydrology inputs |
| `watershed_id` | ✔ | HUC-level watershed identifier |
| `datetime` | ✔ | Event/inference timestamp |
| `kfm:h3_res` | conditional | Required for hex attribution |
| `kfm:sensitivity_flag` | ✔ | CARE/sovereignty handling |
| `kfm:energy_wh` | ✔ | Energy usage |
| `kfm:carbon_gco2e` | ✔ | Carbon footprint |
| CRS | ✔ | EPSG:4326 unless H3 |

Supported outputs:

- **Global SHAP** — watershed-scale influence  
- **Local SHAP** — event-scale prediction explanations  
- **SHAP Summary** — feature-importance distributions  
- **H3 Attribution** — spatially safe hex tiling  

---

## 🧪 4. Validation Requirements (v11)

### ✔ Hydrologic Integrity  
- SHAP grids must align with watershed geometry  
- CAMS→hydrology variable linkage validated  
- No NaN/inf values  
- H3 metadata consistent

### ✔ Metadata Completeness  
- All STAC-required fields populated  
- Model + method version pinned  
- Variable list complete  
- Watershed identifiers correct  

### ✔ CARE & Sovereignty  
- Sensitive tribal waters masked/generalized (H3 R7–R9)  
- No reversible coordinates for protected hydrology/heritage areas  
- CARE flags required  

### ✔ Sustainability  
- Energy & carbon telemetry included  
- Below hydrology explainability budget  
- Linked into STAC + OpenLineage  

Failures → rollback via Reliability Layer v11.

---

## 🌐 5. STAC Templates

Hydrology SHAP outputs MUST include:

- `datetime`  
- `model:version`  
- `watershed_id`  
- `kfm:explainability_method`  
- `kfm:energy_wh`  
- `kfm:carbon_gco2e`  
- Attribution assets (.parquet/.json/.png)  
- Provenance links  

Stored under:

~~~text
stac/item-template.json
stac/collection-template.json
~~~

---

## 🔗 6. Provenance (PROV-O + OpenLineage)

Hydrology SHAP runs MUST emit:

### PROV-O  
- `prov:Activity` = SHAP computation  
- `prov:used` = CAMS + hydrology datasets  
- `prov:generated` = SHAP artifacts  
- `prov:wasAssociatedWith` = exec agent  

### OpenLineage  
- runId  
- input/output pointers  
- execution metadata  

Templates under:

~~~text
lineage/prov-template.json
lineage/ol-template.json
~~~

---

## 📡 7. Telemetry (OTel v11)

Every hydrology SHAP run MUST output:

- `kfm.expl_method="hydrology-shap"`  
- `kfm.expl_energy_wh`  
- `kfm.expl_carbon_gco2e`  
- `kfm.rows_processed`  
- `kfm.expl_latency_ms`  
- GPU/CPU usage  

Telemetry is included in release-level bundles.

---

## 🔮 8. Story Node Integration (Focus Mode v3)

Hydrology SHAP outputs generate Story Nodes that describe:

- Main hydrologic drivers  
- Watershed sensitivity  
- Climate interaction signals  
- Temporal evolution  
- CARE notes  
- Provenance + sustainability metadata  

These power explainable hydrology narratives throughout KFM.

---

## 🧭 9. Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v11.2.3 | 2025-11-29 | Initial v11 hydrology SHAP explainability template; CARE + lineage aligned. |

---

<div align="center">

💧🔍 **Kansas Frontier Matrix — Hydrology SHAP Explainability Template (v11.2.3)**  
Watershed-Aware · Explainable · FAIR+CARE · Provenance-Driven  

[📘 Docs Root](../../../../../..) · [🧠 Hydrology Explainability](../README.md) · [🛡 Governance](../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>