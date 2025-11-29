---
title: "⚙️ Sentinel-1 SAR — ETL Transforms (Orbit · Calibration · RTC · Coherence · InSAR · Flood · Wetlands)"
path: "docs/data/satellites/sentinel-1/transforms/README.md"
version: "v11.2.2"
last_updated: "2025-11-29"

classification: "Internal Technical (Governed Transform Layer)"
status: "Active / Enforced"
release_stage: "Stable · Governed"
lifecycle: "Long-Term Support"
review_cycle: "Quarterly · Remote Sensing WG · FAIR+CARE Council"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
provenance_profile: "KFM-PROV-O v11.2"

commit_sha: "<latest>"
previous_version_hash: "<prev>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../releases/v11.2.2/data-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/sat-sentinel1-transforms-v11.json"

governance_ref: "../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

fair_category: "F3-A1-I2-R5"
care_label: "CARE-B (Sensitive SAR Derivatives)"
indigenous_rights_flag: true
sensitivity_level: "Medium–High"
public_exposure_risk: "Medium–High"
risk_category: "High"
redaction_required: true

data_steward: "Remote Sensing Working Group · FAIR+CARE Council"

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "DataTransform"
  prov_o: "prov:Activity"
  geosparql: "geo:Feature"
  owl_time: "TemporalEntity"

json_schema_ref: "../../../../../schemas/json/sentinel1-transform-v11.json"
shape_schema_ref: "../../../../../schemas/shacl/sentinel1-transform-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:sentinel1:transforms-readme:v11.2.2"
semantic_document_id: "kfm-doc-data-sentinel1-transforms"
event_source_id: "ledger:docs/data/satellites/sentinel-1/transforms/README.md"
immutability_status: "version-pinned"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
ttl_policy: "36 months"
sunset_policy: "Superseded on next ESA processing epoch"
jurisdiction: "Kansas / United States"
---

<div align="center">

# ⚙️ **Sentinel-1 SAR ETL Transform Stack**  
`docs/data/satellites/sentinel-1/transforms/`

**Orbit → Calibration → RTC → Coherence → Flood → Wetlands → InSAR → STAC**  
Fully governed, sovereignty-safe, reproducible SAR processing pipeline for KFM v11.

</div>

---

## 📘 1. Purpose

This directory documents **all ETL transformations** applied to Sentinel-1 SAR data inside KFM:

- ESA SAFE → GRD/GRDH  
- GRD/GRDH → RTC γ⁰  
- Master/slave → Coherence  
- Pair/time-series → InSAR LOS displacement  
- RTC → Flood classifiers  
- RTC + Coherence → Wetlands/saturation maps  

Each transform:

- is **deterministic**  
- produces complete **PROV-O lineage**  
- enforces **FAIR+CARE** & **sovereignty masking**  
- populates **STAC Items** and **Collections**  
- is schema-aligned to **KFM-STAC v11**, **KFM-DCAT v11**, and **KFM-OP v11**

---

## 🗂️ 2. Directory Layout (Complete · Matches Actual Repository)

~~~text
docs/data/satellites/sentinel-1/transforms/
├── 📄 README.md                         # This file
│
├── 🔧 orbit/                            # Orbit correction (aux files, restituted/orbit state vectors)
│   ├── README.md
│   ├── tests/
│   └── fixtures/
│
├── 🛰️ radiometric/                      # Radiometric calibration (σ⁰ generation)
│   ├── README.md
│   ├── calibration_luts/
│   ├── tests/
│   └── fixtures/
│
├── 🏞️ rtc/                              # Radiometric Terrain Correction (γ⁰)
│   ├── README.md
│   ├── dem/                             # DEM tiles used in RTC
│   ├── grid_defs/                       # Snap-to-grid definitions
│   ├── tests/
│   └── fixtures/
│
├── 🔗 coherence/                        # Temporal coherence transforms
│   ├── README.md
│   ├── pairs/                           # Master/slave selection logic
│   ├── tests/
│   └── fixtures/
│
├── 🌍 deformation/                      # InSAR LOS displacement
│   ├── README.md
│   ├── interferograms/                  # Wrapped phase products
│   ├── unwrapped/                       # Unwrapped phase
│   ├── los/                             # Line-of-sight conversion
│   ├── tests/
│   └── fixtures/
│
├── 🌊 flood/                            # Flood mapping transforms
│   ├── README.md
│   ├── classifiers/                     # VH/VV ratio, Otsu, hybrid models
│   ├── qa/                              # Flood QA masking
│   ├── tests/
│   └── fixtures/
│
├── 🌿 wetlands/                         # Wetness / saturation detection
│   ├── README.md
│   ├── seasonal_models/
│   ├── coherence_fusion/
│   ├── tests/
│   └── fixtures/
│
└── 🔐 governance/                       # Sovereignty-masking + CARE enforcement
    ├── README.md
    ├── h3_rules/                        # H3 generalization logic
    ├── masking/
    ├── tests/
    └── fixtures/
~~~

This layout is **exactly aligned** to the screenshot and the STAC family directories you already built.

---

## 🔧 3. Transform Stages (High-Level Summary)

### 3.1 Orbit Correction (🔧 orbit/)
- Load restituted / precise orbit files  
- Align state vectors  
- Apply Doppler centroid corrections  
- Output: **orbit-corrected SLC parameters**

### 3.2 Radiometric Calibration (🛰️ radiometric/)
- Apply calibration LUTs  
- Produce **σ⁰ VV/VH**  
- Border noise corrections  
- Output → **GRD/GRDH Items**

### 3.3 Radiometric Terrain Correction — RTC (🏞️ rtc/)
- Apply DEM (SRTM / Copernicus)  
- Generate **γ⁰**  
- Resample to KFM CRS (EPSG:32614/4326)  
- Output → **RTC STAC Items**

### 3.4 Coherence (🔗 coherence/)
- Master/slave pairing  
- Interferogram coherence calculation  
- Speckle filtering  
- Sovereignty masking if disturbance-sensitive  
- Output → **Coherence STAC Items**

### 3.5 InSAR Deformation (🌍 deformation/)
- Interferogram → unwrap → LOS conversion  
- Apply uncertainty model  
- Always sovereignty-generalized  
- Output → **Deformation STAC Items**

### 3.6 Flood Mapping (🌊 flood/)
- VH/VV ratio  
- Otsu thresholding + hybrid classifiers  
- Coherence-assisted flood detection  
- Mask sovereign hydroscapes  
- Output → **Flood STAC Items**

### 3.7 Wetlands / Saturation (🌿 wetlands/)
- Seasonal hydrological model  
- Coherence-fusion for wetness  
- Sovereignty constraints  
- Output → **Wetlands STAC Items**

### 3.8 Governance Layer (🔐 governance/)
- H3-based sovereignty masking  
- CARE labeling  
- Provenance embedding  
- Ethical review hooks in CI  

---

## 🔐 4. FAIR+CARE & Sovereignty Enforcement

All transform stages enforce:

- `"kfm:care_label"`  
- `"kfm:h3_sensitive"`  
- `"kfm:mask_required"`  
- `"kfm:sovereignty_uncertainty_floor"`  
- `"kfm:governance_notes"`  
- `"kfm:data_steward"`  

Applied at each boundary:

```
SAFE → GRD/GRDH → RTC → Coherence/Deformation/Flood/Wetlands → STAC
```

Generalization occurs at:

- **fine-scale displacement**
- **flood boundaries**
- **wetland/saturation edges**
- **disturbance coherence losses**

---

## 🧪 5. CI Validation Behaviors

Every transform emits telemetry and lineage. CI enforces:

- STAC conformance for outputs  
- DCAT & JSON-LD correctness  
- PROV-O linkage completeness  
- sovereign masking consistency  
- H3 geometry generalization checks  
- metadata schema compliance  
- energy/carbon footprint accounting  

If *any* transform fails governance → **PR blocked**.

---

## 🔁 6. Full Sentinel-1 Transform Pipeline (ETL Graph)

~~~text
ESA SAFE ingest
 → Orbit Correction
 → Radiometric Calibration (σ⁰)
 → GRD / GRDH generation
 → Radiometric Terrain Correction (γ⁰)
 → Temporal Coherence
 → InSAR LOS Deformation
 → Flood Classifiers
 → Wetland / Saturation Modeling
 → Sovereignty Masking & Governance Layer
 → STAC Item generation (family-specific)
 → STAC Collection updates
 → governed release bundle
~~~

---

## 🔮 7. Applications Across KFM

- hydrology & watershed modeling  
- flood risk & severity analytics  
- agricultural transitions  
- disturbance / storm damage  
- ecological saturation cycles  
- cultural-landscape protection overlays  
- Story Node v3 environmental context  
- Focus Mode v3 evidence layers  

---

## 🧭 8. Version History

| Version | Date       | Summary                                                                                                          |
|--------:|------------|------------------------------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-29 | Initial Sentinel-1 transform README; aligned with full STAC ecosystem; complete directory tree; CI/governance.   |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅️ Back](../README.md) · [🗂 STAC Index](../stac/README.md) · [🛡 Governance](../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

