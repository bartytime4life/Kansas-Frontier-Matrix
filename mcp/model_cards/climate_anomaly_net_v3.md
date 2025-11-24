---
title: "🌡️ Model Card — Climate Anomaly Net v3 (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "mcp/model_cards/climate_anomaly_net_v3.md"
version: "v11.0.0"
last_updated: "2025-11-23"
review_cycle: "Quarterly · Climate Working Group · FAIR+CARE Council · AI Governance Board"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../releases/v11.0.0/mcp-modelcards-telemetry.json"
telemetry_schema: "../../schemas/telemetry/mcp-modelcards-v11.json"
governance_ref: "../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
ontology_protocol_version: "KFM-OP v11.0"
pipeline_contract_version: "KFM-PDC v11.0"
status: "Active / Enforced"
doc_kind: "Model Card"
intent: "climate-anomaly-net-v3"
semantic_document_id: "kfm-modelcard-climate-anomaly-net-v3"
doc_uuid: "urn:kfm:modelcard:climate-anomaly-net-v3:v11.0.0"
machine_extractable: true
classification: "AI Model Documentation"
sensitivity: "Low"
fair_category: "F1-A1-I2-R2"
care_label: "Responsible · Ethics · Stewardship"
immutability_status: "version-pinned"
accessibility_compliance: "WCAG 2.1 AA+"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 🌡️ **Climate Anomaly Net v3 — Model Card (v11 LTS)**  
`mcp/model_cards/climate_anomaly_net_v3.md`

**Purpose:**  
Document the architecture, training, evaluation, governance, ethics, provenance, and usage boundaries of the **Climate Anomaly Net v3** model — used for anomaly detection, historical climate reconstruction, and bias-correction support within Kansas Frontier Matrix v11.

</div>

---

## 📘 1. Model Summary

**Climate Anomaly Net v3 (CAN-v3)** is a hybrid CNN+Transformer model designed to:

- Detect climate anomalies (temperature, precipitation, drought indices)  
- Reconstruct missing climate sequences  
- Support bias-correction (BCSD/QM pipelines)  
- Produce anomaly surfaces for:
  - Hydrology models  
  - Climate reconstructions  
  - Hazard overlays  
  - Story Node environmental context  
  - Focus Mode v3 contextual narratives  

This model **does not** generate forward climate projections; it reconstructs past anomalies using historical forcings, spatial features, and multi-source fusion.

---

## 🌦️ 2. Intended Use

### Primary Uses
- Downscaling support for SOP: `climate_downscaling.md`  
- Climate anomaly surface generation  
- Hydrology reconstruction (“forcing inputs”)  
- Environmental Story Node v3 context  
- Historical climate queries (Focus Mode v3)  
- Spatial anomaly map production  

### Out-of-Scope Uses
- Predictive climate modeling beyond its training range  
- Emergency alerting  
- Cultural or historical narrative interpretation  
- Extrapolation to high-risk or policy decision contexts without expert oversight  

---

## 🧬 3. Training Data

### Datasets Used
| Dataset | Version | STAC/DCAT ID | Notes |
|--------|---------|---------------|-------|
| PRISM Climate Normals | 1981–2010 | `stac:climate/prism_normals` | Baseline climatology |
| NOAA NCEI Daily | v2025 | `stac:climate/ncei_daily` | Ground-truth observations |
| ERA5 Reanalysis | 1979–2024 | `stac:climate/era5` | Spatial/temporal context |
| Kansas Mesonet | 1980–2024 | `stac:climate/mesonet` | High-res microclimate |
| Terrain DEM | v11 | `stac:terrain/dem` | Used for lapse rate corrections |

### Data Governance
- All datasets classified as **FAIR-compliant**  
- CARE-sensitive agricultural data masked at H3-R6  
- No Indigenous-sensitive datasets were used  

### Bias Considerations
- Western KS sparse station density  
- Dry-year overrepresentation in 1930s/1950s  
- Urban heat island heterogeneity around Wichita/KC  

Mitigation applied via:

- Reweighting  
- Temporal stratification  
- Ensemble debiasing  

---

## ⚙️ 4. Training Procedure

### Architecture
- **CNN encoder** for spatial features  
- **Transformer decoder** for temporal sequence reconstruction  
- **Hybrid attention** for anomaly signals  
- **Graph-enhanced features** from watershed & ecoregion vectors  

### Hyperparameters
- Epochs: 200  
- Batch: 32  
- Optimizer: AdamW  
- LR: 1e-4 (warmup + cosine decay)  
- Loss: Hybrid RMSE + anomaly-weighted loss  

### Reproducibility
- Seed: **223487**  
- Framework: PyTorch 2.2  
- Hardware: A100 40GB  
- Experiment file:  
  `mcp/experiments/2025-11-02_CLIMATE-EXP-003.md`  

### Training Environment
- Docker image: `kfm/climate-env:v11`  
- Dependencies defined in SBOM  
- Exact environment hashed in `.hash.env`  

---

## 📊 5. Evaluation

### Metrics
| Metric | Score |
|--------|-------|
| RMSE (temperature anomaly) | 0.42°C |
| RMSE (precip anomaly) | 1.7 mm |
| Spatial coherence index | 0.91 |
| Seasonal retention score | 0.97 |
| Bias-correction support score | 0.94 |

### Spatial Validation
- Verified against Kansas Mesonet & NOAA stations  
- Moran’s I confirms spatial anomaly coherence  

### Temporal Validation
- Autocorrelation and seasonal-cycle recovery validated  
- Good performance on drought/flood signature detection  

---

## 🧠 6. Explainability (XAI)

XAI artifacts are stored under:

```
mcp/experiments/2025-11-14_CLIMATE-EXP-006/
```

### SHAP Highlights
- Terrain elevation strongly influences temperature anomalies  
- Mesonet station density correlates with confidence scores  

### LIME Highlights
- Precip anomalies heavily driven by synoptic-scale features  
- Heatwave anomalies most dependent on ERA5 reanalysis inputs  

### Narrative Safety (LLM components)
CAN-v3 is **not** a text generator but feeds climate context into Focus Mode:  
→ All narrative claims derived from CAN-v3 outputs require citation of source datasets.

---

## 🛡️ 7. FAIR+CARE & Sovereignty Compliance

### FAIR Compliance
- STAC/DCAT metadata complete  
- PROV-O lineage preserved  
- Reusable via open licensing (CC-BY)  

### CARE Compliance
- No culturally sensitive datasets used  
- No disallowed spatial precision  
- Model does not produce or infer culturally sensitive patterns  
- Model outputs masked when integrated into Story Nodes  

### Sovereignty Notes
CAN-v3 cannot be used to:
- Reconstruct climate patterns involving sensitive tribal lands without applying **H3-R7 masking**  
- Make policy inferences affecting indigenous communities without council review  

---

## ⚠️ 8. Limitations

- Reduced accuracy in:
  - Sparse-station regions of western Kansas  
  - Extreme precipitation events  
  - Long pre-instrumental reconstructions  
- Possible drift in anomaly magnitude under multi-variable forcing  
- Not suitable for climate projections → reconstruction/hindcast only  
- Outputs require careful human review when used in narrative contexts  

---

## 🚀 9. Deployment & Usage Boundaries

CAN-v3 is **allowed** in:

- Climate downscaling pipelines  
- Hydrologic forcing generation  
- Hazard scenario layers  
- Focus Mode v3 (contextual climate facts, non-narrative)  
- Story Node environmental facts (with citations)

CAN-v3 is **restricted** in:

- Automated narrative or historical interpretation  
- Direct decision-making or forecasting use  
- High-risk modeling without expert oversight  

---

## 🔗 10. Provenance & Lineage

### PROV-O Block (Simplified)

```
{
  "prov:entity": "climate_anomaly_net_v3",
  "prov:wasGeneratedBy": "training:2025-11-02_CLIMATE-EXP-003",
  "prov:used": [
    "stac:climate/prism_normals",
    "stac:climate/ncei_daily",
    "stac:climate/era5",
    "stac:climate/mesonet",
    "stac:terrain/dem"
  ],
  "prov:wasAssociatedWith": "kfm-ai-training-service-v11"
}
```

### OpenLineage
OpenLineage events stored at:

```
data/provenance/experiments/climate_anomaly_net_v3/<timestamp>.json
```

---

## 📊 11. Telemetry (Energy & Carbon)

Stored in:

```
releases/<version>/mcp-modelcards-telemetry.json
```

Approximate training footprint:

- Energy: **14.2 kWh**  
- Carbon: **680 gCO₂e**  
- GPU-hours: **9.6**  

---

## 🕰 12. Version History

| Version | Date | Summary |
|--------:|------|---------|
| v11.0.0 | 2025-11-23 | Initial model card for Climate Anomaly Net v3, aligned with MCP v6.3 and KFM-MDP v11. |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
MCP-DL v6.3 · FAIR+CARE · Sovereignty-Aware  
Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

</div>
