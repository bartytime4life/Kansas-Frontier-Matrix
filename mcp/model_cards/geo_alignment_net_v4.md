---
title: "🗺️ Model Card — Geo Alignment Net v4 (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "mcp/model_cards/geo_alignment_net_v4.md"
version: "v11.0.0"
last_updated: "2025-11-23"
review_cycle: "Quarterly · Geospatial Working Group · FAIR+CARE Council · AI Governance Board"
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
intent: "geo-alignment-net-v4"
semantic_document_id: "kfm-modelcard-geo-alignment-net-v4"
doc_uuid: "urn:kfm:modelcard:geo-alignment-net-v4:v11.0.0"
machine_extractable: true
classification: "AI Model Documentation"
sensitivity: "Mixed"
fair_category: "F1-A1-I2-R2"
care_label: "Collective Benefit · Ethics · Responsibility"
immutability_status: "version-pinned"
accessibility_compliance: "WCAG 2.1 AA+"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 🗺️ **Geo Alignment Net v4 — Model Card (v11 LTS)**  
`mcp/model_cards/geo_alignment_net_v4.md`

**Purpose:**  
Document architecture, evaluation, governance, and provenance for **Geo Alignment Net v4** — KFM's geospatial harmonization and alignment model used for coordinate correction, shape adjustment, vertical-datum normalization, raster alignment, and multi-source GIS integration.

</div>

---

## 📘 1. Model Summary

**Geo Alignment Net v4 (GAN-v4)** is a hybrid deep geospatial alignment model combining:

- CNN-based spatial feature detectors  
- Coordinate residual regression heads  
- Multigrid cross-scale attention  
- Vertical datum adjustment nets (NAVD88 ↔ NGVD29 ↔ EGM96)  
- H3-aware spatial correction logic  

GAN-v4 assists with:

- Aligning historical maps to modern basemaps  
- Correcting scanned GIS layers  
- Harmonizing multi-source geospatial datasets  
- Detecting and fixing raster/feature offsets  
- Aligning hydrology, climate, landcover, and archaeology layers  
- Improving map accuracy for Story Nodes & Focus Mode v3  

GAN-v4 **does not** create or hallucinate new geometries — it only refines existing ones.

---

## 🧠 2. Intended Use

### ✔ Approved Use Cases
- GIS dataset alignment (vector + raster)  
- Vertical datum harmonization for elevation surfaces  
- Geospatial coherence checks  
- Feature correction for historical maps  
- Basemap deformation analysis  
- Automated ETL alignment step in LangGraph v11  

### ❌ Restricted Use Cases
- Creating new archaeological geometries  
- Inferring sensitive cultural site locations  
- Precision elevation corrections on sovereign lands without approval  
- Generating maps for governance-critical decisions without human review  

---

## 🌍 3. Training Data

### Datasets Used
| Dataset | ID | Notes |
|---------|--------------|-------|
| USGS 3DEP DEM | `stac:terrain/3dep` | Training vertical-datum corrections |
| NAIP Imagery | `stac:imagery/naip_kansas` | Used for ground-truth alignment |
| Kansas Historical Maps | `stac:archives/maps_public` | Public-domain, digitized & cleaned |
| Hydrology basins | `stac:hydrology/basins_core` | Used to learn watershed alignment bounds |
| Climate rasters | `stac:climate/core_rasters` | For raster/hybrid alignment learning |

### Governance
- All datasets are **FAIR-compliant**.  
- Sensitive heritage datasets **NOT included**.  
- No tribal or restricted sites used.

### Bias Considerations
- Historical maps vary heavily in accuracy  
- Western KS lacks high-resolution basemap diversity  
- Cloud coverage in NAIP sometimes biases alignment  

Mitigations:

- Domain-balanced sampling  
- Raster augmentation  
- Focal-region equalization  

---

## 🧬 4. Model Architecture

GAN-v4 architecture:

- **Tiered CNN encoder** for spatial edge/feature extraction  
- **Transformer-based spatial attention** for global alignment  
- **Residual regression heads** for X/Y offset prediction  
- **Vertical datum subnetwork** for Z-alignment  
- **H3 correction layer** for grid-based constraints  
- **GeoSPARQL alignment validator**  

Outputs:

- Offset vectors (dx, dy, dz)  
- Rotation angle (optional)  
- Scale correction  
- Confidence map  

---

## ⚙️ 5. Training Procedure

### Environment
- Framework: PyTorch 2.2  
- Container: `kfm/geo-align-env:v11`  
- Hardware: A100 80GB  

### Hyperparameters
- Epochs: 160  
- Batch: 8 (high-res raster windows)  
- Loss: Weighted MSE + Huber on rotation terms  
- LR: 3e-4 → cosine decay  
- Optimizer: AdamW  
- Seed: **221917**

### Reproducibility
- Training run logged at:  
  `mcp/experiments/2025-11-14_GEO-EXP-009.md`

- All inputs/outputs hashed in provenance bundle.

---

## 📊 6. Evaluation

### Key Metrics
| Metric | Score |
|--------|-------|
| RMSE (dx/dy offset) | 0.38 m |
| RMSE (dz) | 0.27 m |
| Rotation error | <0.15° |
| Scale drift | <0.3% |
| H3 grid alignment accuracy | 0.93 |
| GeoSPARQL validity | 100% |

### Validation Methods
- Hand-checked georeferencing points  
- Raster cross-correlation maps  
- Vertical-datum cross-check vs 3DEP  

GAN-v4 consistently reduces misalignment in historical maps by **60–85%**, depending on era and scan quality.

---

## 🛡️ 7. FAIR+CARE & Sovereignty Governance

### FAIR Compliance
- STAC/DCAT metadata included  
- PROV-O lineage complete  
- JSON-LD context applied  

### CARE Compliance
Even though GAN-v4 itself does not use sensitive cultural datasets, its *outputs may interact* with them.

Thus:

- Never output refined coordinates for **archaeological** or **sacred** sites  
- Only apply alignment to such layers when:
  - Data is generalized (H3 R7–R9)  
  - Sovereignty approval exists  
  - CARE metadata is fully populated  

### Sovereignty Notes
- Vertical-datum alignment of tribal lands requires opt-in review  
- Sensitive cultural sites must remain masked  

---

## ⚠️ 8. Limitations

GAN-v4 may be less accurate when:

- Input rasters are heavily distorted  
- Features lack clear edges  
- Historical maps use inconsistent cartographic projections  
- Very sparse control points exist  
- Imagery mismatch (seasonal differences)  

Model is **not** suitable for:

- Archaeological precision mapping  
- High-stakes legal boundary corrections  
- Hydrologic enforcement (use hydrology pipelines instead)  

---

## 🚀 9. Deployment & Usage Boundaries

### Allowed:
- ETL alignment stages  
- Preprocessing for climate/hydrology rasters  
- Story Node map-context alignment (non-sensitive datasets)  
- Focus Mode map reasoning (non-sensitive datasets)  

### Restricted:
- Sensitive cultural datasets  
- Tribal geographies requiring sovereignty review  
- Precision cadastral boundary correction  

### Integration Points
- `src/pipelines/geo_alignment/`  
- `src/pipelines/climate/`  
- `src/pipelines/hydrology/`  
- Focus Mode v3 map context renderer  

---

## 🔗 10. Provenance & Lineage

### PROV-O Example

```
{
  "prov:entity": "geo_alignment_net_v4",
  "prov:wasGeneratedBy": "training:2025-11-14_GEO-EXP-009",
  "prov:used": [
    "stac:terrain/3dep",
    "stac:imagery/naip_kansas",
    "stac:archives/maps_public",
    "stac:hydrology/basins_core"
  ],
  "prov:wasAssociatedWith": "kfm-ai-training-service-v11"
}
```

### OpenLineage Events

Stored under:

```
data/provenance/experiments/geo_alignment_net_v4/<timestamp>.json
```

---

## ♻️ 11. Telemetry

Logged under:

```
releases/<version>/mcp-modelcards-telemetry.json
```

Approximate training footprint:

- Energy: **7.9 kWh**  
- Carbon: **370 gCO₂e**  
- GPU-hours: **5.2**  

---

## 🕰 12. Version History

| Version | Date | Summary |
|--------:|------|---------|
| v11.0.0 | 2025-11-23 | Initial model card for Geo Alignment Net v4, aligned with FAIR+CARE and KFM-MDP v11. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — MCP-DL v6.3  
Diamond⁹ Ω / Crown∞Ω Certified · FAIR+CARE · Sovereignty-Aware  
Geospatial Accuracy · Ethical AI · Full Governance

</div>
