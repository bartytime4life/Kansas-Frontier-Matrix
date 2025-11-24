---
title: "🌦️ KFM SOP — Climate Downscaling & Bias Correction Workflow (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "mcp/sops/climate_downscaling.md"
version: "v11.0.0"
last_updated: "2025-11-23"
review_cycle: "Quarterly · Climate Working Group · FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../releases/v11.0.0/mcp-sops-telemetry.json"
telemetry_schema: "../../schemas/telemetry/mcp-sops-v11.json"
governance_ref: "../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
ontology_protocol_version: "KFM-OP v11.0"
pipeline_contract_version: "KFM-PDC v11.0"
status: "Active / Enforced"
doc_kind: "SOP"
intent: "climate-downscaling"
semantic_document_id: "kfm-sop-climate-downscaling"
doc_uuid: "urn:kfm:mcp:sop:climate-downscaling:v11.0.0"
machine_extractable: true
classification: "Scientific Procedure"
sensitivity: "Low"
fair_category: "F1-A1-I2-R2"
care_label: "Responsible · Ethics · Stewardship"
immutability_status: "version-pinned"
accessibility_compliance: "WCAG 2.1 AA+"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 🌦️ **SOP — Climate Downscaling & Bias Correction Workflow (v11 LTS)**  
`mcp/sops/climate_downscaling.md`

**Purpose:**  
Define the **deterministic, reproducible, fairness-aware** procedure for downscaling climate datasets (e.g., PRISM, ERA5, NOAA NCEI, CMIP projections) into high-resolution, Kansas-ready environmental layers used across the Kansas Frontier Matrix.

</div>

---

## 📘 1. Scope

This SOP governs all climate downscaling operations executed within:

- **LangGraph v11 pipelines**  
- **CrewAI climate inference workers**  
- **Hydrology and hazard models requiring climate forcing**  
- **Climate-index reconstruction pipelines**  
- **STAC/DCAT dataset generation for climate layers**  

It covers:

- Spatial downscaling  
- Temporal downscaling  
- Bias correction  
- Harmonization  
- Validation  
- FAIR+CARE & sovereignty checks  
- PROV-O & OpenLineage lineage requirements  

---

## 🔧 2. Preconditions

Before executing this SOP, ensure:

- Required data is present in `data/raw/` or via DVC/LFS pointers  
- Data Contracts v11 (`docs/contracts/climate.json`) are satisfied  
- STAC/DCAT metadata is prepared  
- Seeds, configs, and hyperparameters are declared  
- FAIR+CARE classification for datasets is validated  
- Sovereignty-sensitive models (e.g., those impacting tribal land narratives) are screened  

### Required Inputs
| Input | Description |
|-------|-------------|
| Climate datasets | e.g., PRISM, ERA5, NCEI, CMIP5/6 |
| Metadata | STAC/DCAT JSON files |
| Config | Downscaling YAML config |
| Seeds | Reproducibility seeds |
| Spatial masks | Kansas bounds + optional tribal geographies |
| Scripts | Located in `src/pipelines/climate/` |

---

## 🧩 3. Procedure — Deterministic Downscaling Pipeline

### 3.1 Step 1 — Load Raw Climate Data

- Load raw multiband rasters / NetCDF grids  
- Confirm alignment with CF-Conventions  
- Verify CRS integrity (typically EPSG:4326 or dataset-native)  
- Validate temporal metadata (OWl-Time conformity)  

**Reject dataset** if:

- Timestamps are inconsistent  
- CRS tags are missing  
- Units do not meet data contract (temp, precipitation, etc.)

---

### 3.2 Step 2 — Spatial Downscaling

Perform:

- Bilinear / bicubic interpolation (for temperature/anomalies)  
- Conservative remapping (for precipitation)  
- Terrain-sensitive adjustment using:
  - Elevation lapse rates  
  - DEM from `data/processed/terrain/`  
- Convert units (e.g., Kelvin → °C)

Output:

- High-resolution raster (e.g., 800m or 1km)  
- GeoTIFF or NetCDF  

Record:

- Method  
- Parameters  
- Seed  
- CRS  
- Terrain model version  

---

### 3.3 Step 3 — Temporal Downscaling

For monthly → daily or hourly → daily:

- Apply statistical decomposition  
- Use rolling climatologies for correction  
- Interpolate using spline or Gaussian kernel methods  
- Validate with historical station datasets (NCEI, Mesonet)

Store intermediate:

```
data/work/climate_downscaled/
```

---

### 3.4 Step 4 — Bias Correction

Use:

- Quantile Mapping  
- Delta Method  
- CDF-based scaling  
- LOESS-based bias correction  
- Hybrid Bias-Correction/Spatial-Downscaling (BCSD)

Validate bias reduction with:

- RMSE  
- MAE  
- Skill scores  
- Regional subsets (east/west Kansas)

Apply safeguards to **avoid hallucinated climatology**:

- Enforce physical constraints  
- Clip to observed ranges  
- Reject unrealistic trends  

---

### 3.5 Step 5 — Harmonization & Data Contracts

Validate against:

- **Data Contracts v11**  
- CF-Conventions  
- CRS rules  
- Variable naming rules (`tas`, `pr`, `anom_tas`)  
- Required units  

Generate:

- **STAC Item** (`data/stac/climate/...json`)  
- **DCAT Dataset** entry  

---

### 3.6 Step 6 — Governance, FAIR+CARE & Sovereignty Checks

- Apply CARE classification  
- Ensure climate projections for tribal land overlays are masked/generalized where appropriate  
- Add sovereignty notes to metadata  
- Validate governance metadata is complete  

If in doubt → escalate to **FAIR+CARE Council**.

---

### 3.7 Step 7 — Lineage Logging (PROV-O + OpenLineage)

Record:

- `prov:used` (datasets, scripts, configs)  
- `prov:wasGeneratedBy` (pipeline run)  
- `prov:wasAssociatedWith` (agent)  
- Input/output checksums  
- Runtime, seeds, intermediate files  

Write lineage to:

```
data/provenance/experiments/climate/<timestamp>.json
```

Emit OpenLineage events tagged:

- `climate.downscaling`  
- STAC Item references  
- Data Contract version  

---

### 3.8 Step 8 — Export & Publish

Write final output:

```
data/processed/climate/downscaled/
```

And publish to release directory:

```
data/releases/v11.x/climate/downscaling/
```

Attach:

- STAC Item  
- DCAT Dataset  
- Lineage JSON  
- Telemetry (energy/carbon)  

Once validated by CI, output is ready for integration into:

- Web maps  
- Hydrology models  
- Focus Mode v3  
- Story Node environmental context  

---

## 🧭 4. Verification

To confirm SOP completion:

- All validation steps pass CI (`mcp-validate.yml`, `schema-lint-v11`)  
- Downscaled outputs match expected spatial/temporal resolution  
- Bias corrected trends align with historical reference datasets  
- Metadata validates under STAC / DCAT / CF / PDC v11 schemas  
- Lineage and telemetry records exist  
- Care/Sovereignty fields are populated  

Failures require reprocessing or FAIR+CARE review.

---

## 🧯 5. Failure Modes & Recovery

### Failure Modes
- CRS mismatch  
- Temporal drift  
- Statistical artifacts in extremum values  
- Uncertain projections near tribal lands  
- Bias correction instability in arid regions  

### Recovery Steps
- Re-run with alternative interpolation  
- Use fallback BCSD pipeline  
- Tighten constraints on anomalies  
- Segment downscaling by sub-region  
- Rebuild pipeline DAG with corrected inputs  

Serious governance issues → escalate to FAIR+CARE Council.

---

## 🌱 6. Telemetry & Sustainability

Record:

- Wh consumed  
- gCO₂e emitted  
- Runtime duration  
- Compute node type  
- I/O volume  

Stored in:

```
releases/<version>/mcp-sops-telemetry.json
```

Used for:

- Sustainability dashboards  
- Climate pipeline optimization  
- Governance energy auditing  

---

## 🕰 7. Version History

| Version | Date | Summary |
|--------:|------|---------|
| v11.0.0 | 2025-11-23 | Initial climate downscaling SOP for KFM-MCP v11. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — MCP-DL v6.3  
FAIR+CARE · Climate Ethics · Diamond⁹ Ω / Crown∞Ω  

</div>
