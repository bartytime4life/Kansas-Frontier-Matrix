---
title: "🛰️ ESA Sentinel-1 — Radar Observation Layer (SAR · Interferometry · Flood/Hydrology · Soil/Surface)"
path: "docs/data/satellites/sentinel-1/README.md"
version: "v11.2.2"
last_updated: "2025-11-29"

classification: "Public · Earth Observation"
status: "Active / Enforced"
release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Remote Sensing WG · FAIR+CARE Council"

license: "CC-BY 4.0 (ESA Open Data)"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
provenance_profile: "KFM-PROV-O v11.2"

commit_sha: "<latest-commit>"
previous_version_hash: "<prev-sha>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../releases/v11.2.2/data-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/sat-sentinel1-v11.json"

governance_ref: "../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

fair_category: "F2-A1-I2-R4"
care_label: "CARE-A / CARE-B (depending on downstream derivative usage)"
indigenous_rights_flag: true
sensitivity_level: "Low–Medium"
public_exposure_risk: "Low"
risk_category: "Low–Medium"
redaction_required: true

data_steward: "Remote Sensing WG · FAIR+CARE Council"

ontology_alignment:
  cidoc: "E84 Information Carrier"
  schema_org: "Dataset"
  prov_o: "prov:Entity"
  geosparql: "geo:FeatureCollection"
  owl_time: "TemporalEntity"

json_schema_ref: "../../../../schemas/json/satellite-sentinel1-v11.json"
shape_schema_ref: "../../../../schemas/shacl/satellite-sentinel1-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:sentinel-1:overview:v11.2.2"
semantic_document_id: "kfm-doc-data-sentinel1-overview"
event_source_id: "ledger:docs/data/satellites/sentinel-1/README.md"
immutability_status: "version-pinned"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

ttl_policy: "48 months"
sunset_policy: "Superseded on next ESA major Sentinel-1 reprocessing cycle"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 🛰️ **ESA Sentinel-1 — Synthetic Aperture Radar (SAR) Observation Layer**  
`docs/data/satellites/sentinel-1/`

**C-band SAR for all-weather Earth observation:**  
Flood mapping · Soil moisture proxies · Surface roughness · Ground deformation ·  
Land change · Wetland detection · Snowmelt · Infrastructure & hazard monitoring.

</div>

---

## 📘 1. Overview

Sentinel-1 (A, B, and upcoming C/D units) provides **C-band Synthetic Aperture Radar (SAR)**  
capable of imaging the Earth in **all weather, day/night**, making it a core pillar of the  
KFM v11 remote-sensing stack.

Sentinel-1 supports:

- 🌊 **Flood detection** and flood-extent dynamics  
- 💧 **Hydrology**: inundation, wetlands, soil saturation proxies  
- 🌾 **Agricultural monitoring**  
- 🏔 **Snowmelt & freeze–thaw transitions**  
- 🏚 **Disaster mapping** (storm, tornado, wind damage detection via coherence loss)  
- 🛰 **Interferometry (InSAR)** for deformation, subsidence, landslide analysis  
- 🗺 **Land change detection** (coherence/time-series SAR)  

All Sentinel-1 data ingested into KFM v11 is governed, reproducible, and linked to  
**STAC/DCAT/PROV-O lineage** with sovereignty and CARE compliance.

---

## 🗂️ 2. Directory Layout (Emoji-Rich · Option A)

~~~text
docs/data/satellites/sentinel-1/
├── 📄 README.md                          # This file
│
├── 🗂️ stac/                               # STAC Collections / Items for Sentinel-1
│   ├── grdh/                             # Ground Range Detected (High-Res)
│   ├── grd/                              # Standard GRD scenes
│   ├── coherence/                        # Coherence / InSAR coherence tiles
│   ├── deformation/                      # InSAR deformation (LOS displacement, trends)
│   ├── flood/                            # Floodwater detection STAC items
│   ├── wetlands/                         # SAR-derived wetland proxies
│   └── metadata/                         # Collection-level metadata (JSON-LD/DCAT)
│
├── 🛠️ transforms/                         # SAR preprocessing / harmonization
│   ├── orbit/                            # Precise orbit files (POD) ingest
│   ├── radiometric/                      # Radiometric calibration → sigma0/gamma0/beta0
│   ├── speckle/                          # Speckle filtering (Lee, Refined Lee, Gamma-MAP)
│   ├── terrain/                          # Terrain correction (RTC)
│   ├── coherence/                        # Coherence computation workflows
│   ├── flood/                            # Flood mapping (VH/VV ratio, thresholding)
│   └── utils/                            # Shared SAR math utilities
│
├── 🧪 qa/                                # QA/validation outputs
│   ├── radiometry/                       # Radiometric QA
│   ├── coherence/                        # Coherence quality & change QA
│   └── flood/                            # Flood classification QA
│
└── 📎 samples/                           # Tutorial-safe synthetic SAR examples
    ├── rasters/                          # Example sigma0, gamma0, coherence tiles
    ├── stac/                             # Mini STAC Items for docs/tutorials
    └── qa/                               # Synthetic QA examples (SAR-specific)
~~~

---

## 🧩 3. Data Products Integrated in KFM v11

### 3.1 Radiometrically Calibrated Backscatter (σ⁰, γ⁰)
- Surface roughness  
- Soil moisture sensitivity (context, not direct SM)  
- Wetland & inundation indicators  

### 3.2 Coherence Products
- Flood damage detection  
- Agricultural disturbance  
- Land cover dynamics  
- Structure collapse mapping  

### 3.3 InSAR Deformation (Optional / Masked)
- LOS displacement  
- Long-term subsidence  
- Seasonal ground movement  

Sovereignty note:  
Deformation products may intersect sensitive lands → **automatically H3-generalized**  
where required.

### 3.4 Flood & Wetland Detection
- Threshold-based (VH/VV)  
- Otsu or clustering  
- Regression models (if enabled)

---

## 🔐 4. FAIR+CARE & Sovereignty Controls

Sentinel-1 radar products often intersect **tribal territories, sensitive ecological zones,  
 archaeologically significant surfaces**, or locations whose dynamic monitoring requires  
special governance handling.

KFM v11 enforces:

- `"kfm:h3_sensitive"` propagation  
- `"kfm:mask_required"` for sensitive hydrology and deformation layers  
- `"kfm:care_label"` for SAR derivatives  
- `"kfm:sovereignty_uncertainty_floor"` for inferred products (InSAR, flood, wetlands)  
- generalization of deformation patterns where risk exists  
- PROV-O lineage for every transform step  

Sovereignty enforcement validated via:

- `faircare_validate.yml`  
- `jsonld_validate.yml`  
- `stac_validate.yml`

---

## 🧪 5. QA & Validation

SAR-specific QA includes:

- Radiometric calibration QA  
- Orbit offset/geometry QA  
- Coherence quality  
- Flood classification QA  
- Terrain correction alignment QA  
- Sovereignty-sensitive masking QA  
- Pixel/grid CRS integrity  
- Raster orientation ↔ footprint consistency  

All outputs **must** pass CI before inclusion in STAC Collections.

---

## 🔁 6. Position in the KFM ETL Pipeline

~~~text
ingest (ESA SciHub / COG mirrors)
 → orbit correction
 → radiometric calibration
 → terrain correction (RTC)
 → speckle filtering
 → optional: coherence / InSAR
 → flood/wetland detection
 → sovereignty masking
 → STAC generation
 → QA validation
 → governed release bundle
~~~

---

## 🔮 7. Applications Inside KFM

- 🌊 Flood mapping & hydrology  
- 🌱 Ecology & wetland modeling  
- 🏛 Archaeological landscape context (sovereignty-generalized)  
- 🏙 Infrastructure deformation (sovereignty-protected)  
- 🧭 Focus Mode v3 environmental evidence  
- 📖 Story Node v3 context (governance-bounded)  
- 🗺 MapLibre/Cesium multi-layer rendering  

---

## 🧭 8. Version History

| Version | Date       | Summary                                                                                                        |
|--------:|------------|----------------------------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-29 | Initial Sentinel-1 dataset overview; STAC/DCAT/PROV integrated; FAIR+CARE/H3 aligned; emoji-rich; CI-safe.     |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅️ Back](../../README.md) · [🗂 STAC Collections](./stac/README.md) · [🛡 Governance](../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

