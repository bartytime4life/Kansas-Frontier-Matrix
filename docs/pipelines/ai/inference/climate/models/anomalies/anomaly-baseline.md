---
title: "🌡️📉📘 KFM v11.2.2 — Baseline Climatology Model (Anomaly Reference · Deterministic · FAIR+CARE)"
path: "docs/pipelines/ai/inference/climate/models/anomalies/anomaly-baseline.md"
version: "v11.2.2"
last_updated: "2025-11-28"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Climate Working Group · FAIR+CARE Council"
status: "Active / Enforced"
content_stability: "stable"
doc_kind: "Model Component · Baseline Climatology"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../../../../releases/v11.2.2/climate-inference-telemetry.json"
telemetry_schema: "../../../../../../../../schemas/telemetry/ai-climate-inference-v11.2.2.json"
energy_schema: "../../../../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"
data_contract_ref: "../../../../../contracts/data-contract-v3.json"

license: "CC-BY 4.0"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Medium-Risk"
sensitivity: "Climate-Anomaly-Baseline"
sensitivity_level: "Low"
public_exposure_risk: "Low"
immutability_status: "version-pinned"

semantic_intent:
  - "baseline-climatology"
  - "climatology-model"
  - "anomaly-baseline"
  - "normals-reference"
  - "distribution-centering"
  - "deterministic-seed"
  - "xai-compatible"
  - "stac-xai"

scope:
  domain: "pipelines/ai/inference/climate/models/anomalies"
  applies_to:
    - "anomaly-baseline.md"
    - "anomaly-diff-model.md"
    - "anomaly-generation"
    - "climate-normals"
    - "historical-baseline"

layout_profiles:
  - "immediate-one-branch-with-descriptions-and-emojis"

requires_purpose_block: true
requires_version_history: true
requires_governance_links_in_footer: true
diagram_profiles:
  - "mermaid-flowchart-v1"
---

<div align="center">

# 🌡️📉📘 **Baseline Climatology Model**  
`docs/pipelines/ai/inference/climate/models/anomalies/anomaly-baseline.md`

**Purpose**  
Define the authoritative **baseline climatology model** used to compute climate anomalies  
(Δ = realtime − baseline).  
This baseline establishes long-term reference values for temperature, dewpoint, wind fields,  
precipitation metrics, and derived variables.  
Supports deterministic anomaly generation, hazard chains, XAI attribution, FAIR+CARE safeguards,  
and STAC-XAI compliant metadata.

</div>

---

## 📘 Overview

The baseline model provides **static or slow-moving climatological reference fields**, enabling:

- Temperature, dewpoint, wind, humidity anomaly computation  
- Multi-decadal distribution anchoring  
- Hazard driver centering (CAPE/CIN biases reduced)  
- Stability for statewide anomaly maps  
- Integration with anomaly-diff models  
- Consistent XAI explainability for deviations  
- Deterministic reproduction via seed-locked generation  

A valid baseline MUST include:

- Temporal window (e.g. **1991–2020 NOAA/NCEI normals**)  
- Spatial grid definition + CRS  
- Variables included  
- Distribution centers (means, medians, moments)  
- Metadata: provenance, lineage, CARE, license  
- STAC-XAI compliant asset declarations  

---

## 🗂 Variables Supported

- **Temperature** (t2m, t850, t700, etc.)  
- **Dewpoint** (td2m)  
- **Winds** (u10, v10, u-level, v-level)  
- **Humidity**  
- **Precipitation climatology**  
- **Surface pressure baseline**  
- **Soil moisture climatology** (optional)  

Each variable MUST declare units, CRS, vertical axis, and data source.

---

## 🧱 Data Sources

Baseline climatology may derive from:

- **NOAA NCEI 1991–2020 Climate Normals**  
- **PRISM** monthly/daily averages (800m)  
- **ERA5-Historical** long-term climatology  
- **Downscaled climatology** (U-Net or Transformer downscalers)  

All sources MUST include licensing and provenance blocks.

---

## 🧬 Baseline Model Architecture

```mermaid
flowchart TD
    A[Climatology Dataset] --> B[Ingest And Normalize]
    B --> C[CRS And Vertical Reprojection]
    C --> D[Compute Mean Fields]
    C --> E[Compute Optional Higher Moments]
    D --> F[Assemble Baseline Grid]
    E --> F
    F --> G[STAC XAI Metadata Packaging]
    G --> H[Provide Baseline To Anomaly Engine]
```

---

## 🔍 Baseline Structure Requirements

The baseline MUST define:

### **Spatial Structure**
```
crs: "EPSG:4326"
grid:
  lat_res: 0.01
  lon_res: 0.01
vertical_axis:
  type: pressure
  units: hPa
```

### **Temporal Structure**
- Period: 1991–2020 (standard)  
- Optionally: rolling 30-year windows  
- Include `precision` and raw source metadata  

### **Statistical Structure**
For each variable:

```
mean
stddev
median
skew
kurtosis
```

### **Metadata**
- License  
- FAIR summary  
- CARE applicability  
- Provenance (source datasets + timestamps)  
- Checksums for reproducibility  

---

## 🎛 Outputs

The baseline MUST output:

- `baseline_grid.tif` (COG)  
- `baseline_metadata.json`  
- `baseline_summary.json`  
- Optional: `baseline_moments.json`  
- STAC Item for catalog integration  
- Distribution plots (if added to CI artifacts)

---

## 🧪 CI Requirements

CI MUST validate:

- Missing or malformed metadata → ❌ fail  
- CRS/vertical definitions present  
- Temporal windows valid  
- Deterministic baseline generation  
- STAC-XAI schema conformity  
- Baseline checksum stable  
- Units and attributes present for all variables  
- FAIR+CARE tags included  

CI failure → merge blocked.

---

## 🕰 Version History

| Version  | Date       | Notes                                              |
|----------|------------|----------------------------------------------------|
| v11.2.2  | 2025-11-28 | Initial baseline climatology model documentation.  |

---

<div align="center">

### 🔗 Footer  
[⬅ Back to Anomaly Models](../README.md) ·  
[🌡️ Climate Inference Root](../../README.md) ·  
[🏛 Governance](../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

