---
title: "🌡🧠 KFM v11 — Climate AI Training Explainability Framework (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/pipelines/ai/training/climate/explainability/README.md"
version: "v11.2.3"
last_updated: "2025-11-29"

release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Climate AI Working Group · FAIR+CARE Council"
content_stability: "stable"
status: "Active / Enforced"

commit_sha: "<latest-commit>"
previous_version_hash: "<previous-version-hash>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../../../../../releases/v11.2.3/manifest.zip"
attestation_ref: "../../../../../../releases/v11.2.3/slsa-attestation.json"
signature_ref: "../../../../../../releases/v11.2.3/signature.sig"

telemetry_ref: "../../../../../../releases/v11.2.3/climate-training-explainability-telemetry.json"
telemetry_schema: "../../../../../../schemas/telemetry/ai-training-climate-explainability-v11.json"
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
intent: "climate-training-explainability"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Compliant · Climate-Sensitive"

classification: "Public (Governed)"
sensitivity: "Moderate (Climate hazards + exposure sensitivity)"
machine_extractable: true
jurisdiction: "United States · Kansas"
accessibility_compliance: "WCAG 2.1 AA+"
---

<div align="center">

# 🌡🧠 **Climate AI Training Explainability Framework (KFM v11)**  
`docs/pipelines/ai/training/climate/explainability/`

**Purpose**  
Provide the **governed, reproducible v11 explainability framework** for *climate AI training pipelines*,  
supporting SHAP, Integrated Gradients, Sensitivity Maps, Spatial Attribution, H3 attribution grids,  
and JSON-LD semantic metadata.  

Explainability ensures model behavior is **transparent**, **testable**, **energy-aware**, and  
**FAIR+CARE-compliant** across PM2.5, ozone, smoke, heat, fire danger, and climate-surface response models.

</div>

---

## 📘 1. Overview

Climate training explainability is used to diagnose:

- **Which variables** influence model predictions (CAMS, ERA5, HRRR, landcover, soils, DEM).  
- **Where on the landscape** those influences occur (spatial attribution).  
- **How influence shifts across versions** (temporal SHAP/IG drift).  
- **Whether climate models behave safely** in sensitive regions (CARE rules).  
- **How energy/carbon-heavy the training explainability steps are**.

This framework provides:

- Explainability templates (SHAP, IG, CAMS explainability, spatial attribution, JSON-LD)  
- Validation + sovereignty screening  
- Provenance emission (OpenLineage + PROV-O)  
- STAC/DCAT metadata alignment  
- Telemetry + sustainability recording  
- Story Node v3 integration for Focus Mode narratives  

---

## 🗂️ 2. Directory Layout (Emoji-Prefix Standard)

~~~text
docs/pipelines/ai/training/climate/explainability/
├── 📄 README.md
│
├── 🔍 shap/                            # SHAP explainability (global/local/summary/H3)
│   ├── 📄 README.md
│   ├── 🧠 templates/
│   ├── 🌐 stac/
│   ├── 🔗 lineage/
│   ├── 🧪 validation/
│   └── 📊 examples/
│
├── ⚡ integrated-gradients/            # Integrated Gradients explainability
│   ├── 📄 README.md
│   ├── ⚡ templates/
│   ├── 🌐 stac/
│   ├── 🔗 lineage/
│   ├── 🧪 validation/
│   └── 📊 examples/
│
├── 🌍 cams/                            # CAMS-driven climate explainability modules
│   ├── 📄 README.md
│   ├── 🧠 templates/
│   ├── 🌐 stac/
│   ├── 🔗 lineage/
│   ├── 🧪 validation/
│   └── 📊 examples/
│
├── 🗺️ spatial-attribution/             # Spatial/H3 attribution maps
│   ├── 📄 README.md
│   ├── 🧠 templates/
│   ├── 🌐 stac/
│   ├── 🔗 lineage/
│   ├── 🧪 validation/
│   └── 📊 examples/
│
└── 📚 jsonld/                          # JSON-LD explainability metadata templates
    ├── 📄 README.md
    ├── 📁 context/
    ├── 🧠 templates/
    ├── 🔗 lineage/
    ├── 🧪 validation/
    └── 📊 examples/
~~~

---

## 🧬 3. Explainability Output Standards (v11)

All explainability outputs MUST include:

### Required Metadata

| Field | Required | Description |
|-------|---------|-------------|
| `model:version` | ✔ | Model version during training |
| `kfm:domain` | ✔ | `"climate"` |
| `kfm:explainability_method` | ✔ | shap / ig / sensitivity / spatial / cams |
| `kfm:input_variables` | ✔ | Variables used during training |
| `datetime` | ✔ | Timestamp or epoch window |
| `crs` | ✔ | EPSG:4326 or declared spatial grid |
| `kfm:h3_res` | conditional | For H3 attribution |
| `kfm:sensitivity_flag` | ✔ | FAIR+CARE classification |
| `kfm:energy_wh` | ✔ | Computation energy |
| `kfm:carbon_gco2e` | ✔ | Sustainability metric |
| `prov:*` | ✔ | PROV-O lineage |
| `openlineage:*` | recommended | Upstream/downstream linkage |

### Required Assets

- Attribution map(s) (parquet, zarr, json, png)  
- STAC Item + STAC Collection  
- JSON-LD explainability metadata  
- Provenance bundle (OpenLineage + PROV-O)  
- Validation logs  

---

## 🧪 4. Validation Requirements (v11)

Climate explainability outputs MUST pass:

### ✔ Spatial Validation  
- Attribution grid aligns with climate training grid/H3  
- CRS correctness  
- No NaN/inf  
- Land/water masks consistent  

### ✔ Temporal Validation  
- Attribution window matches training window  
- Lead-time consistency for forecast-based training  

### ✔ FAIR+CARE Validation  
- Sensitive regions masked or generalized  
- Sovereignty compliance enforced  
- Metadata includes CARE flags  

### ✔ Sustainability Validation  
- Energy/carbon < explainability budget  
- Logged into telemetry + STAC  

### ✔ Provenance Validation  
- Complete PROV-O chain  
- OpenLineage run with all inputs/outputs  
- Model version pinned unambiguously  

Validation failures → rollback via Reliability Framework v11.

---

## 🌐 5. STAC + JSON-LD Integration

Each explainability output MUST produce:

### STAC Item  
- `datetime`  
- `model:version`  
- `kfm:explainability_method`  
- Energy/carbon fields  
- Assets (attribution maps, JSON-LD, provenance bundle)  
- Collection-level metadata  

### JSON-LD Explainability  
- Semantic metadata for variables, units, spatial contexts  
- PROV-O structure  
- Alignment with KFM-Ontology v11  

---

## 🔗 6. Provenance (PROV-O + OpenLineage)

Each explainability run MUST capture:

- `prov:Activity` — explainability computation  
- `prov:used` — climate training datasets + model artifacts  
- `prov:generated` — attribution outputs  
- `prov:wasAssociatedWith` — executing agent  
- OpenLineage:
  - runId  
  - inputs + outputs  
  - resource usage  
  - energy/carbon metrics  

---

## 📡 7. Telemetry (OTel v11)

Every explainability run MUST export:

- `kfm.expl_method`  
- `kfm.expl_energy_wh`  
- `kfm.expl_carbon_gco2e`  
- `kfm.expl_latency_ms`  
- Rows/cells processed  
- CPU/GPU/memory usage  

Telemetry flows into:

- `releases/v11.2.3/climate-training-explainability-telemetry.json`  
- Reliability dashboards  
- Sustainability analytics  

---

## 🔮 8. Story Node Integration (Focus Mode v3)

Each explainability artifact SHOULD generate a Story Node summarizing:

- **Influential climate variables**  
- **Spatial attribution hotspots**  
- **Temporal behavior changes (IG/SHAP drift)**  
- **CARE handling of sensitive regions**  
- **Model reasoning narratives**  
- **Provenance & sustainability impact**

These nodes enrich the Climate Explainability Explorer in Focus Mode v3.

---

## 🧭 9. Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v11.2.3 | 2025-11-29 | Initial v11 climate training explainability framework; fully aligned with SHAP/IG/CAMS/spatial/JSON-LD templates. |

---

<div align="center">

🌡🧠 **Kansas Frontier Matrix — Climate Training Explainability Framework (v11.2.3)**  
Transparent · Explainable · FAIR+CARE · Provenance-Driven · Sustainable  

[📘 Docs Root](../../../../../..) · [🌡 Training Pipelines](../README.md) · [🛡 Governance](../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>