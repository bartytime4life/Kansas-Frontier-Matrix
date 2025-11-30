---
title: "🧠 KFM v11 — Spatial Attribution Explainability Template (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/pipelines/ai/explainability/templates/spatial-attribution/README.md"
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

telemetry_ref: "../../../../../../releases/v11.2.3/spatial-attribution-telemetry.json"
telemetry_schema: "../../../../../../schemas/telemetry/ai-explainability-spatial-attribution-v11.json"
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
intent: "spatial-attribution-template"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Compliant · Spatial Sensitivity Aware"

classification: "Public (Governed)"
sensitivity: "Low/Moderate"
machine_extractable: true
jurisdiction: "United States · Kansas"
accessibility_compliance: "WCAG 2.1 AA+"
---

<div align="center">

# 🧠 **Spatial Attribution Explainability Template (KFM v11)**  
`docs/pipelines/ai/explainability/templates/spatial-attribution/`

**Purpose**  
Provide a **governed, reusable v11 template** for creating **spatial attribution maps**  
(SHAP maps, sensitivity fields, gradient-based explainability surfaces, H3 attribution grids)  
across any KFM AI domain (climate, hydrology, archaeology, ecology, soils, wildfire, air quality).

This template ensures **uniform metadata**, **validation**, **lineage**, **governance**,  
and **FAIR+CARE-compliant** explainability outputs.

</div>

---

## 📘 1. Overview

Spatial attribution explainability maps answer:

> **“Where does the model pay attention?”**  
> **“Which geographic patterns influence the prediction?”**

This template standardizes:

- How spatial SHAP/attribution maps are generated  
- Required metadata + STAC items  
- Provenance linking via OpenLineage + PROV-O  
- Local & global attribution formats  
- H3-based transformations for privacy & sensitivity  
- Validation + sustainability telemetry  
- Story Node integration (Focus Mode v3)

This folder can be cloned into any domain-specific explainability module.

---

## 🗂️ 2. Directory Layout (Emoji-Prefix Standard)

~~~text
docs/pipelines/ai/explainability/templates/spatial-attribution/
├── 📄 README.md                       # This file
│
├── 🧠 templates/                      # Core attribution templates
│   ├── 🌍 global-shap-template.parquet
│   ├── 📍 local-shap-template.parquet
│   ├── 🔬 sensitivity-template.parquet
│   └── 🧭 h3-attribution-template.parquet
│
├── 🌐 stac/                           # STAC Item/Collection templates
│   ├── 📄 item-template.json
│   └── 📄 collection-template.json
│
├── 🔗 lineage/                        # Provenance templates (PROV-O + OpenLineage)
│   ├── 🧾 prov-template.json
│   └── 📡 ol-template.json
│
├── 🧪 validation/                     # Explainability validation blocks
│   ├── 📄 validate-spatial-integrity.md
│   ├── 📄 validate-metadata.md
│   └── 📄 validate-sensitivity-screening.md
│
└── 📊 examples/                       # Example attribution outputs
    ├── 📁 global/
    ├── 📁 local/
    ├── 📁 h3/
    └── 📁 sensitivity/
~~~

---

## 🧬 3. Attribution Standards (v11)

### Supported explainability techniques

| Method | Description | Use Case |
|--------|-------------|----------|
| **SHAP (global)** | Variable-level attribution aggregated spatially | Feature importance distribution |
| **SHAP (local)** | Per-cell explanations | Event-level reasoning |
| **Gradient Surfaces** | ∂Y/∂X sensitivity | Downscalers, CNNs |
| **Perturbation Maps** | Model output change after input perturbations | Climate & hazard simulations |
| **H3 Attribution** | Attribution mapped to H3 grid | Privacy-preserving & fast |

### Required attributes

All outputs MUST include:

- `model:version`  
- `kfm:explainability_method`  
- `kfm:input_variables`  
- `kfm:energy_wh`  
- `kfm:carbon_gco2e`  
- `kfm:sensitivity_flag` (CARE-sensitive area handling)  
- CRS = **EPSG:4326** unless intentionally generalized  
- For H3: `kfm:h3_res`  

---

## 🧪 4. Validation Rules (v11)

Explainability maps MUST pass:

### ✔ Spatial Integrity Checks
- No NaN/inf  
- Valid bounding extents  
- Dimensionally consistent arrays  
- H3 indices valid for declared resolution  

### ✔ Metadata Completeness
- STAC-required fields present  
- Model version pinned  
- Explainability method correct  
- Temporal extent aligns with underlying dataset  

### ✔ CARE / Sovereignty Checks
- Sensitive regions masked or generalized  
- No exposure of restricted tribal/heritage landscapes  
- CARE flag must be explicit  

### ✔ Sustainability Checks
- Energy & carbon metrics within budget  
- Logged to telemetry and lineage  

Validation failure → rollback (Reliability Layer v11).

---

## 🌐 5. STAC Templates

Both *item* and *collection* templates must include:

- `datetime`  
- `start_datetime` / `end_datetime`  
- `model:version`  
- `kfm:explainability_method`  
- `kfm:h3_res` (if applicable)  
- Energy/Carbon metrics  
- PROV-O + OpenLineage references  
- Attribution asset pointer: `.parquet`, `.png`, or `.json`  

Stored under:

~~~text
stac/item-template.json
stac/collection-template.json
~~~

---

## 🔗 6. Lineage (OpenLineage + PROV-O)

Each explainability build MUST emit:

- **OpenLineage Run ID**  
- Input datasets (climate/soil/etc.)  
- Model artifact version  
- Explainability code version  
- Output attribution assets  

PROV-O MUST include:

- `prov:Activity` = explainability run  
- `prov:used` = input datasets  
- `prov:generated` = attribution maps  
- `prov:wasAssociatedWith` = pipeline agent  

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
- `kfm.expl_method`  
- `kfm.expl_cells`  
- `kfm.expl_latency_ms`  
- Hardware telemetry (CPU/GPU usage)  

Telemetry MUST be attached to the OpenLineage event and the STAC Item.

---

## 🧩 8. Rendering Guidance (Optional)

Explainability visual layers SHOULD follow:

- Diverging colors (for signed SHAP)  
- Per-cell normalization  
- Multi-scale (H3, lat/lon, tile pyramids)  
- Regional aggregation (H3 ring ops)  
- Downsampling for public or CARE-restricted releases  

---

## 🔮 9. Story Node Integration (Focus Mode v3)

Each attribution output SHOULD create a Story Node summarizing:

- Major drivers of prediction  
- Spatial influence hotspots  
- Sensitivity vs. model configuration  
- CARE notes (masking, generalization, fuzzing)  
- Temporal evolution/context  

Focus Mode v3 uses this to narrate how model reasoning changes across time & regions.

---

## 🧭 10. Version History

| Version | Date | Summary |
|--------:|------|---------|
| v11.2.3 | 2025-11-29 | Initial v11-aligned template for spatial explainability across AI pipelines. |

---

<div align="center">

🧠 **Kansas Frontier Matrix — Spatial Attribution Explainability Template (v11.2.3)**  
Explainable · Ethical · Spatially Aware · FAIR+CARE-Compliant  

[📘 Docs Root](../../../../../..) · [🤖 AI Explainability Index](../../README.md) · [🛡 Governance](../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>