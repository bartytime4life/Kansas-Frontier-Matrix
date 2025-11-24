---
title: "💧 Model Card — Hydrology Seq2Seq v11 (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "mcp/model_cards/hydrology_seq2seq_v11.md"
version: "v11.0.0"
last_updated: "2025-11-23"
review_cycle: "Quarterly · Hydrology Working Group · FAIR+CARE Council · AI Governance Board"
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
intent: "hydrology-seq2seq-v11"
semantic_document_id: "kfm-modelcard-hydrology-seq2seq-v11"
doc_uuid: "urn:kfm:modelcard:hydrology-seq2seq-v11:v11.0.0"
machine_extractable: true
classification: "AI Model Documentation"
sensitivity: "Mixed"
fair_category: "F1-A1-I2-R3"
care_label: "Collective Benefit · Responsibility · Ethics"
immutability_status: "version-pinned"
accessibility_compliance: "WCAG 2.1 AA+"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 💧 **Hydrology Seq2Seq v11 — Model Card (v11 LTS)**  
`mcp/model_cards/hydrology_seq2seq_v11.md`

**Purpose:**  
Document model architecture, evaluation, governance, provenance, and usage boundaries for the **Hydrology Seq2Seq v11** model — the KFM system’s primary engine for hydrologic reconstruction (daily streamflow, reservoir inflow/outflow, sediment-adjusted series, historical backfilling).

</div>

---

## 📘 1. Model Summary

**Hydrology Seq2Seq v11 (HS2S-v11)** is a **sequence-to-sequence hydrology reconstruction model** trained to:

- Reconstruct missing streamflow/inflow/outflow values  
- Extend incomplete USGS time series  
- Model hydrologic response to climate forcings (precip, ET, anomalies)  
- Provide inputs to:
  - Reservoir storage adjustments  
  - Multi-source hydrology fusion  
  - Flood/drought analysis  
  - Climate-driven hydrology pipelines  
- Support Focus Mode v3 and Story Node v3 environmental narratives (with citations)

HS2S-v11 does **not** produce forecasts.  
It reconstructs historical or gap-filled sequences strictly within training-window coverage.

---

## 🌊 2. Intended Use

### ✔ Approved Use
- Daily hydrologic gap-fill  
- Multi-source hydrology fusion  
- Reservoir reconstruction pipelines  
- Sedimentation-adjusted inflow series  
- Extreme-event recovery (drought/flood periods)  
- Climate-driven reconstructions using:
  - Precipitation  
  - Temperature anomalies  
  - Evapotranspiration  
  - Snow metrics (if available)

### ❌ Restricted Use
- Regulatory water-rights adjudication  
- Tribal water-use inference without approval  
- High-resolution ecological impact modeling without domain review  
- Predictive release operations or emergency forecasting  
- Historical claims involving cultural sites or tribal watersheds

---

## 🗂 3. Training Data

### Core Datasets
| Dataset | STAC/DCAT ID | Notes |
|---------|--------------|-------|
| USGS Daily Streamflow | `stac:hydrology/usgs_daily` | Ground truth |
| USACE Reservoir Ops | `stac:hydrology/usace_ops` | Reservoir inflow/outflow |
| Kansas Mesonet Climate | `stac:climate/mesonet` | ET, precip, temp |
| ERA5 Reanalysis | `stac:climate/era5` | Climate forcing |
| DEM / Watershed Data | `stac:terrain/dem` | Basin-based hydrology features |

### Governance
- All data is FAIR compliant  
- Tribal watershed data is masked at **H3-R7** unless permissions granted  
- No sensitive cultural datasets used  

### Bias Considerations
- Western KS sparse gauge density  
- Seasonal imbalance (wet-season dominance)  
- Drought-heavy training windows (1930s/1950s)  

Mitigations:

- Stratified sampling  
- Data augmentation by regime type  
- Seasonal balancing  

---

## 🧬 4. Model Architecture

HS2S-v11 architecture:

- **Encoder:**  
  - Multi-channel climate + hydrology + watershed embeddings  
  - 1D CNN + temporal attention  

- **Decoder:**  
  - GRU/Transformer hybrid  
  - Residual prediction heads  
  - Uncertainty channel output  

- **Auxiliary modules:**  
  - Sedimentation factor estimator  
  - Basin similarity embedding  
  - Elevation & terrain-aware correction  

Outputs:

- Reconstructed hydrologic series  
- Confidence intervals  
- Fill-flag masks  
- Metadata including anomaly alignment  

---

## ⚙️ 5. Training Procedure

### Environment
- PyTorch 2.2  
- GPU: A100 80GB  
- Docker: `kfm/hydro-env:v11`  

### Hyperparameters
- Epochs: 150  
- Batch size: 64  
- LR: 2e-4 (warmup → cosine)  
- Loss: Weighted RMSE + drought-event penalty + uncertainty loss  
- Seed: **882134**  

### Provenance
Training experiment:

```
mcp/experiments/2025-11-06_HYDRO-EXP-011.md
```

Includes:

- Data splits  
- Preprocessing scripts  
- Climate forcing configuration  
- Feature engineering pipeline  

---

## 📊 6. Evaluation

### Metrics
| Metric | Score |
|--------|-------|
| RMSE (daily flow) | 14.2 cfs |
| MAE (daily flow) | 7.9 cfs |
| Drought period accuracy | 0.93 |
| High-flow event reconstruction | 0.87 |
| Seasonal stability | 0.95 |
| Sedimentation-adjusted storage match | 0.90 |

### Validation Studies
- 20 basins across Kansas  
- Flood/drought signature detection  
- Watersheds with differing physiography  
- Comparison to observed USGS time series  

### Uncertainty Estimation
Decoder outputs a **±CI** range representing model uncertainty.  
Stored in metadata under:

```
"uncertainty_bounds": { ... }
```

---

## 🛡️ 7. FAIR+CARE & Sovereignty Governance

### FAIR Compliance
- STAC/DCAT metadata complete  
- Provenance (PROV-O + OpenLineage) preserved  
- Reusable via CC-BY license  
- Dataset references embedded in output metadata  

### CARE Compliance
- No unrestricted tribal watershed data accepted  
- Outputs must be masked/generalized for cultural regions  
- Never infer or expose sensitive water-use patterns  
- Tier A datasets require Council review  

### Sovereignty Notes
- Cannot reconstruct flows for restricted tribal basins unless permissions included  
- Territorial hydrology must be masked to **H3-R7 → R9** resolution  

---

## ⚠️ 8. Limitations

- Lower accuracy for:
  - Sparse data basins  
  - High-flow extreme events  
  - Snow-driven hydrology (rare in KS)  
  - Periods with missing climate forcings  

- Not suitable for:
  - Fine-scale ecological modeling  
  - Legal water-rights estimation  
  - Emergency flood forecasting  
  - Tribal water modeling without explicit authorization  

Human oversight is required for all uses influencing planning or policy.

---

## 🚀 9. Deployment & Usage Boundaries

HS2S-v11 is **authorized** for:

- Hydrology reconstruction pipelines  
- Sedimentation-adjusted reservoir modeling  
- Climate-driven multi-source fusion  
- Story Node environmental context  
- Focus Mode quantitative hydrology background  

Restricted for:

- High-risk or sovereign basin modeling  
- Narratives involving cultural water-use  
- Direct decision-making systems  

Integrated into pipelines:

```
src/pipelines/hydrology/reconstruction/
src/pipelines/hydrology/multisource_fusion/
```

---

## 🔗 10. Provenance & Lineage

### PROV-O Block (Simplified)

```
{
  "prov:entity": "hydrology_seq2seq_v11",
  "prov:wasGeneratedBy": "training:2025-11-06_HYDRO-EXP-011",
  "prov:used": [
    "stac:hydrology/usgs_daily",
    "stac:hydrology/usace_ops",
    "stac:climate/era5",
    "stac:climate/mesonet",
    "stac:terrain/dem"
  ],
  "prov:wasAssociatedWith": "kfm-ai-training-service-v11"
}
```

### OpenLineage

Results stored under:

```
data/provenance/experiments/hydrology_seq2seq_v11/<timestamp>.json
```

Includes:

- Dataset mappings  
- Training/validation alignment  
- Model fingerprint  
- Metrics + XAI artifacts  

---

## 📈 11. Telemetry

Energy/Carbon footprint:

- Energy: **10.5 kWh**  
- Carbon: **520 gCO₂e**  
- GPU-hours: **7.2**  

Stored in:

```
releases/<version>/mcp-modelcards-telemetry.json
```

---

## 🕰 12. Version History

| Version | Date | Summary |
|--------:|------|---------|
| v11.0.0 | 2025-11-23 | Initial hydrology Seq2Seq model card for KFM-MCP v11 (full governance & lineage). |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
Diamond⁹ Ω / Crown∞Ω Ultimate Certified  
FAIR+CARE · Hydrology Governance · MCP-DL v6.3  

</div>
