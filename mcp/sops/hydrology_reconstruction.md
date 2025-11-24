---
title: "💧 KFM SOP — Hydrology Time-Series Reconstruction & Multi-Source Fusion (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "mcp/sops/hydrology_reconstruction.md"
version: "v11.0.0"
last_updated: "2025-11-23"
review_cycle: "Quarterly · Hydrology Working Group · FAIR+CARE Council"
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
intent: "hydrology-reconstruction"
semantic_document_id: "kfm-sop-hydrology-reconstruction"
doc_uuid: "urn:kfm:mcp:sop:hydrology-reconstruction:v11.0.0"
machine_extractable: true
classification: "Scientific Procedure"
sensitivity: "Mixed"
fair_category: "F1-A1-I2-R2"
care_label: "Responsibility · Ethics · Stewardship"
immutability_status: "version-pinned"
accessibility_compliance: "WCAG 2.1 AA+"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 💧 **KFM Standard Operating Procedure — Hydrology Time-Series Reconstruction (v11 LTS)**  
`mcp/sops/hydrology_reconstruction.md`

**Purpose:**  
Define the **deterministic, multi-source, reproducible procedure** for reconstructing hydrologic time-series (flows, inflows, storage, sedimentation-adjusted series) using observed data, AI inference, climate-forcings, and geospatial constraints, aligned with FAIR+CARE and KFM-PDC v11.

</div>

---

## 📘 1. Scope

This SOP applies to:

- Reservoir inflow/outflow reconstruction  
- Daily streamflow gap-fills (e.g., missing USGS periods)  
- Sedimentation-adjusted reservoir histories  
- Pre-instrumental hydrology inference  
- Multi-source fusion of:
  - USGS gauges  
  - USACE reservoir operations  
  - Kansas Mesonet precipitation/ET data  
  - Climate hindcasts / reanalysis (ERA5, PRISM)  
  - AI-generated hydrologic surfaces  

It governs:

- ETL ingestion  
- Temporal harmonization  
- Gap-filling  
- Bias correction  
- Uncertainty quantification  
- STAC/DCAT metadata generation  
- OpenLineage + PROV-O lineage capture  
- CARE/Sovereignty masking rules  

---

## 🧩 2. Preconditions

Before starting:

- Confirm **Data Contracts v11**:  
  `docs/contracts/hydrology.json`
- Validate CRS alignment (EPSG:4326 required)
- Validate FAIR+CARE classification for datasets
- Ensure:

  | Requirement | Location |
  |-------------|----------|
  | Raw gauge data | `data/raw/hydrology/usgs/` |
  | Reservoir ops | `data/raw/hydrology/usace/` |
  | Climate forcings | `data/raw/climate/` |
  | DEM/terrain | `data/processed/terrain/` |
  | STAC metadata | `data/stac/hydrology/` |
  | Config file | `src/pipelines/hydrology/config/*.yaml` |

- All inputs must specify:
  - **time coverage**  
  - **spatial bounding box**  
  - **units**  
  - **sampling frequency**  
  - **provenance reference**

---

## 🛠️ 3. Procedure — Deterministic Reconstruction Pipeline

### 3.1 Step 1 — Load Datasets & Validate Metadata

Load:

- USGS gauge time-series  
- USACE operations (inflows/outflows/storage)  
- Mesonet precipitation / ET  
- Climate reanalysis (ERA5, PRISM)  
- DEM + watershed boundaries  

Validate:

- Timestamp alignment  
- Unit consistency (cfs, cms, AF, mm/day, etc.)  
- Missing data intervals  
- Ensure metadata → Data Contract v11 fields  

Reject data if:

- Station discontinuity > allowed gap  
- Unit mismatch inconsistent with contract  
- Spatial misalignment  

---

### 3.2 Step 2 — Temporal Harmonization

- Resample all series to common timestep (daily or sub-daily)  
- Apply timezone normalization (UTC recommended)  
- Identify:

  - Short gaps (1–7 days)  
  - Mid gaps (week–month)  
  - Long gaps (months–years)  

Mark gaps in a **gap mask**.

---

### 3.3 Step 3 — Gap-Filling (Deterministic)

#### A) Short Gaps (1–7 days)
Use:

- Linear interpolation  
- Kalman filtering  
- Bias-aware spline fill  

#### B) Mid Gaps (week–1 month)
Use:

- Climate-driven regression  
- Nearest-neighbor station imputation  
- Watershed similarity weighting  

#### C) Long Gaps (>1 month)
Use:

- Climate → hydrology model (CrewAI cooperative worker)  
- Basin-transfer models  
- AI inference (seq2seq model)  
- Uncertainty bounds (± CI)  

All fills must include metadata tags:

```
"fill_method": "<method>",
"fill_confidence": <0.0–1.0>,
"fill_flags": [...]
```

---

### 3.4 Step 4 — Sedimentation Adjustment (Reservoirs)

For sedimentation-affected storage:

- Load bathymetry (processed)  
- Load WID/dredging logs (if available)  
- Reconstruct historical Elevation–Area–Volume curves  
- Adjust inflow/outflow → storage via:

  - Volume correction  
  - Area-weighted adjustment  
  - Multi-decadal trend correction  

Produce:

```
<reservoir>_adjusted_storage_timeseries.csv
```

---

### 3.5 Step 5 — Multi-Source Fusion

Combine:

- Gauge data  
- Climate-driven inference  
- Watershed weights  
- Terrain-based runoff estimates  
- AI reconstruction outputs  

Fusion method:

- Weighted ensemble  
- Bayesian model averaging  
- Error-minimizing regression  

Outputs:

- Final fused time-series  
- Confidence intervals  
- Fusion weights  

---

### 3.6 Step 6 — Validation

Run:

- Bias metrics (MAE, RMSE)  
- Hydrograph comparison  
- Autocorrelation analysis  
- Seasonal cycle validation  
- Climate-forcing response tests  
- Spatial comparison vs. nearby basins  

Series must pass:

- **Bias threshold:** <10%  
- **RMSE threshold:** domain-specific  
- **Autocorrelation match:** ±5%  

If not → re-run fusion with tuned parameters.

---

## 🛡️ 4. Governance & FAIR+CARE Compliance

### 4.1 CARE Review Requirements

Required if:

- Reconstruction touches tribal watersheds  
- Hazard outputs based on reconstructed hydrology  
- Data could imply culturally sensitive water-use patterns  

Rules:

- Apply sovereignty flags  
- Use H3 generalization for sensitive basins  
- Mask results where required  

### 4.2 FAIR Requirements

Must include:

- Findable STAC Items  
- DCAT Dataset records  
- Full provenance (PROV-O)  
- Accessible formats (CSV, Parquet, NetCDF)  
- Interoperable CRS and units  
- Reusable metadata + licensing  

---

## 🔗 5. STAC / DCAT Metadata Generation

Generate:

- STAC Item for each reconstructed series  
- STAC Collection for broader hydrology products  
- DCAT record with temporal coverage, spatial extent, lineage  

Save to:

```
data/stac/hydrology/<basin>/items/
data/stac/hydrology/<basin>/collection.json
```

Add fields:

- `processing: hydrology_reconstruction_v11`  
- `lineage: [...]`  
- `care_classification: [...]`  
- `provenance: [...]`  

---

## 🧬 6. Lineage (PROV-O + OpenLineage v2.5)

Record for each run:

- Inputs (datasets + versions)  
- Activities (gap fill, fusion, adjustments)  
- Agents (pipeline, CrewAI workers)  
- Outputs (series, metadata)  
- Seeds and configs  
- Execution environment  

Write:

```
data/provenance/experiments/hydrology/<timestamp>.json
```

Emit OpenLineage event:

```
hydrology.reconstruction
```

---

## 📊 7. Telemetry Logging

Record:

- Runtime duration  
- Energy Wh  
- Carbon gCO₂e  
- I/O volume  
- Memory footprint  

Stored in:

```
releases/<version>/mcp-sops-telemetry.json
```

---

## 🧯 8. Failure Modes & Recovery

### Common Failures
- Climate mismatch  
- Negative flow artifacts  
- Unrealistic sedimentation corrections  
- Fusion instability  
- Sovereignty flag violations  

### Recovery Actions
- Re-run with alternative climate-forcing regression  
- Recompute watershed weights  
- Use fallback fusion model  
- Adjust smoothing or anomaly thresholds  
- Re-validate CARE flags; escalate if needed  

---

## 🕰 9. Version History

| Version | Date | Summary |
|--------:|------|---------|
| v11.0.0 | 2025-11-23 | Initial hydrology reconstruction SOP for KFM-MCP v11 (governed, deterministic). |

---

<div align="center">

© 2025 Kansas Frontier Matrix — MCP-DL v6.3  
FAIR+CARE · Hydrology Governance · Diamond⁹ Ω / Crown∞Ω Certified

</div>
