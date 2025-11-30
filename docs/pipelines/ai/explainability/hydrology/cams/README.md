---
title: "💧 KFM v11 — Hydrology Explainability (CAMS-Driven Models · SHAP · Gradients · H3 Attribution)"
path: "docs/pipelines/ai/explainability/hydrology/cams/README.md"
version: "v11.2.3"
last_updated: "2025-11-29"

release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Hydrology AI WG · FAIR+CARE Council"
content_stability: "stable"
status: "Active / Enforced"

commit_sha: "<latest-commit>"
previous_version_hash: "<previous-version-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../../../../../releases/v11.2.3/manifest.zip"
attestation_ref: "../../../../../../releases/v11.2.3/slsa-attestation.json"
signature_ref: "../../../../../../releases/v11.2.3/signature.sig"

telemetry_ref: "../../../../../../releases/v11.2.3/hydro-cams-explainability-telemetry.json"
telemetry_schema: "../../../../../../schemas/telemetry/ai-explainability-hydrology-cams-v11.json"
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
intent: "hydrology-cams-explainability"
fair_category: "F1-A1-I1-R2"
care_label: "CARE-Compliant · Watershed-Sensitive"

classification: "Public (Governed)"
sensitivity: "Low/Moderate (Localized hydrology sensitivity)"
machine_extractable: true
jurisdiction: "United States · Kansas"
accessibility_compliance: "WCAG 2.1 AA+"
---

<div align="center">

# 💧 **KFM v11 — Hydrology Explainability (CAMS-Driven Models)**  
`docs/pipelines/ai/explainability/hydrology/cams/`

**Purpose**  
Provide the authoritative v11 explainability standard for **hydrology AI models that use CAMS atmospheric fields**,  
including runoff predictors, flood-risk surrogates, soil-moisture response models, and water-balance inference.

Explainability maps + JSON-LD + STAC metadata clarify **why** CAMS-driven hydrologic predictions occur,  
and ensure ethical, FAIR+CARE-compliant watershed modeling.

</div>

---

## 📘 1. Overview

Many hydrology AI pipelines in KFM use CAMS variables:

- Precipitation proxies  
- PM2.5 / aerosol deposition inputs  
- Humidity, temperature, pressure  
- Wind fields used in evaporation models  
- CAMS smoke → infiltration / drought interaction models  

Explainability layers ensure hydrologic predictions are:

- **Transparent** — which climate drivers mattered most  
- **Spatially coherent** — explainability per watershed/HUC/H3  
- **Governed** — sovereignty & CARE compliance  
- **Reproducible** — full STAC/DCAT + lineage recordings  

This module defines how hydrology-specific CAMS explainability must be produced.

---

## 🗂️ 2. Directory Layout (Emoji-Prefix Standard)

~~~text
docs/pipelines/ai/explainability/hydrology/cams/
├── 📄 README.md                          # This file
│
├── 🧠 templates/                         # Hydrology-specific attribution templates
│   ├── 🌧️ shap_precip_template.parquet
│   ├── 💨 shap_evap_template.parquet
│   ├── 🔬 sensitivity_template.parquet
│   ├── 🧭 h3_attribution_template.parquet
│   └── 🕒 temporal_influence_template.parquet
│
├── 🌐 stac/                              # STAC templates for hydrologic explainability
│   ├── 📄 item-template.json
│   └── 📄 collection-template.json
│
├── 🔗 lineage/                           # PROV-O + OpenLineage specs
│   ├── 🧾 prov-template.json
│   └── 📡 ol-template.json
│
├── 🧪 validation/                        # Hydrology-focused explainability checks
│   ├── 📄 validate-watershed-integrity.md
│   ├── 📄 validate-cams-hydro-linkage.md
│   ├── 📄 validate-h3.md
│   ├── 📄 validate-temporal.md
│   └── 📄 validate-metadata.md
│
└── 📊 examples/                          # Example hydrology explainability outputs
    ├── 📁 global/
    ├── 📁 local/
    ├── 📁 h3/
    └── 📁 temporal/
~~~

---

## 🌍 3. Hydrology-CAMS Explainability Standards (v11)

### Required Metadata

| Field | Description | Required |
|------|-------------|----------|
| `model:version` | Hydrology AI model version | ✔ |
| `kfm:domain` | `"hydrology"` | ✔ |
| `kfm:explainability_method` | shap-global/local, sensitivity, gradient | ✔ |
| `kfm:input_variables` | CAMS variables used by model | ✔ |
| `datetime` | Inference or event timestamp | ✔ |
| `watershed_id` | HUC or model-specific watershed ID | ✔ |
| `kfm:h3_res` | Required for H3 attribution | conditional |
| `kfm:energy_wh` | Compute energy cost | ✔ |
| `kfm:carbon_gco2e` | CO₂ equivalent | ✔ |
| `kfm:sensitivity_flag` | CARE/sensitivity tag | ✔ |
| CRS | Must be EPSG:4326 | ✔ |

### Supported Output Types

- **Hydrology Global SHAP** (watershed-level importance)  
- **Local SHAP** (per-grid or per-H3 hydrology prediction)  
- **Temporal influence** (storm window → watershed sensitivity)  
- **H3 hydrology attribution** (privacy-aware)  
- **Gradient/sensitivity maps** for runoff, infiltration, evapotranspiration  

---

## 🧪 4. Validation Requirements (v11)

### ✔ Hydrologic Integrity

- Attribution must align with watershed boundaries  
- No NaN/inf values  
- CAMS variable linkage validated (e.g., precipitation → runoff)  
- H3 resolution consistent across hydrologic region  

### ✔ Metadata Completeness

- STAC required fields  
- Model version, explainability method  
- CAMS variables correctly listed  
- Watershed identifiers consistent with hydrology pipeline  

### ✔ CARE / Sovereignty

- Masking of sensitive tribal waters, springs, wetlands  
- H3 R7–R9 for sensitive areas  
- No reverse-engineerable high-risk hydrologic regions  

### ✔ Sustainability

- IG/SHAP computation stays below budget  
- Metrics exported to OTel + STAC  
- Energy/carbon recorded for governance review  

---

## 🌐 5. STAC Templates

Hydrology explainability maps must include:

- `datetime`  
- `model:version`  
- `watershed_id`  
- `kfm:explainability_method`  
- `kfm:energy_wh`  
- `kfm:carbon_gco2e`  
- `kfm:sensitivity_flag`  
- Spatial attribution asset links  
- Provenance pointers (OpenLineage + PROV-O)

Stored under:

~~~text
stac/item-template.json
stac/collection-template.json
~~~

---

## 🔗 6. Provenance (PROV-O + OpenLineage)

Each explainability run MUST include:

### PROV-O  
- `prov:Activity` = explainability run  
- `prov:used` = CAMS inputs + hydrology base data  
- `prov:generated` = hydrologic attribution maps  
- `prov:wasAssociatedWith` = CI runner / pipeline agent  

### OpenLineage  
- `runId`  
- Input CAMS asset references  
- Output explainability maps  
- Timing + compute attributes  

All stored under:

~~~text
lineage/prov-template.json
lineage/ol-template.json
~~~

---

## 📡 7. Telemetry (OTel v11)

Every explainability run MUST emit:

- `kfm.expl_method="hydrology-cams"`  
- `kfm.expl_energy_wh`  
- `kfm.expl_carbon_gco2e`  
- `kfm.rows_processed`  
- `kfm.expl_latency_ms`  
- CPU/GPU metrics  
- H3 cell count if applicable  

Telemetry must be attached to STAC + lineage.

---

## 🔮 8. Story Node Integration (Focus Mode v3)

Explainability outputs MUST generate a Story Node summarizing:

- Dominant watersheds & hydrologic sensitivities  
- CAMS climate drivers (e.g., humidity → infiltration, ozone → stomatal response)  
- Spatial risk regions  
- Temporal storm evolution  
- FAIR+CARE and sensitivity treatment  
- Full provenance chain  

These nodes power explainable hydrology storytelling in KFM.

---

## 🧭 9. Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v11.2.3 | 2025-11-29 | Initial v11 hydrology explainability template; CAMS-driven maps; governance + lineage aligned. |

---

<div align="center">

💧 **Kansas Frontier Matrix — Hydrology Explainability (CAMS v11.2.3)**  
Watershed-Aware · Climate-Coupled · FAIR+CARE · Provenance-Driven  

[📘 Docs Root](../../../../../..) · [🧠 AI Explainability](../../README.md) · [🛡 Governance](../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>