---
title: "🏞️ Sentinel-1 RTC — Radiometric Terrain Correction Transform (γ⁰ Backscatter · DEM · Projection · Geometry)"
path: "docs/data/satellites/sentinel-1/transforms/rtc/README.md"
version: "v11.2.2"
last_updated: "2025-11-29"

classification: "Internal Technical (SAR Preprocessing Layer)"
status: "Active · Enforced"
release_stage: "Stable · Governed"
lifecycle: "LTS"
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
telemetry_schema: "../../../../../schemas/telemetry/sat-rtc-transform-v11.json"

governance_ref: "../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

fair_category: "F1-A1-I1-R2"
care_label: "CARE-A"
indigenous_rights_flag: false
sensitivity_level: "Low"
risk_category: "Low"
redaction_required: false

data_steward: "Remote Sensing Working Group"

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "DataTransform"
  prov_o: "prov:Activity"
  geosparql: "geo:Geometry"
  owl_time: "Instant"

json_schema_ref: "../../../../../schemas/json/sentinel1-rtc-transform-v11.json"
shape_schema_ref: "../../../../../schemas/shacl/sentinel1-rtc-transform-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:sentinel1:transform-rtc:v11.2.2"
semantic_document_id: "kfm-doc-data-sentinel1-transform-rtc"
event_source_id: "ledger:docs/data/satellites/sentinel-1/transforms/rtc/README.md"
immutability_status: "version-pinned"
machine_extractable: true

accessibility_compliance: "WCAG 2.1 AA+"
ttl_policy: "36 months"
sunset_policy: "Superseded on next ESA RTC model update"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 🏞️ **Sentinel-1 Radiometric Terrain Correction (RTC) Transform**  
`docs/data/satellites/sentinel-1/transforms/rtc/`

Generates **γ⁰ terrain-corrected backscatter**, aligned to KFM CRS & terrain geometry.  
RTC is required for downstream **coherence**, **flood**, **wetlands**, and **deformation** ETL chains.

</div>

---

## 🗂️ 1. Directory Layout (Strict Option-A Emoji Style)

~~~text
docs/data/satellites/sentinel-1/transforms/rtc/
├── 📄 README.md
│
├── 🗺️ dem/                       # DEM tiles for terrain correction
│   ├── 🗺️ dem_32614_tile_01.tif
│   └── 🗺️ dem_32614_tile_02.tif
│
├── 📐 grid_defs/                # Grid alignment definitions for RTC projection
│   ├── 📄 grid_10m.json
│   └── 📄 grid_30m.json
│
├── 🧪 tests/                    # Unit + integration RTC tests
│   ├── 🏞️ test_rtc_core.py
│   ├── 🏞️ test_projection.py
│   └── 🏞️ test_dem_alignment.py
│
└── 📁 fixtures/                 # DEM samples, SAFE subset, reference gamma0 tiles
    ├── 🗺️ dem_sample.tif
    ├── 🛰️ SAFE_annotation_subset.xml
    └── 📄 rtc_reference_gamma0.tif
~~~

---

## 📘 2. Purpose

Radiometric Terrain Correction (RTC) converts calibrated **σ⁰** into **γ⁰** by removing:

- terrain-induced radiometric distortions  
- incidence-angle dependencies  
- topographic relief effects  

This produces spatially consistent, analysis-ready backscatter.

γ⁰ is the **required foundation** for:

- flood detection  
- wetland/saturation modeling  
- temporal coherence  
- InSAR deformation preconditioning  
- multi-temporal SAR analysis  

---

## 🧩 3. Inputs & Outputs

### Inputs

- σ⁰ VV/VH calibrated backscatter  
- DEM tiles (SRTM / Copernicus-30)  
- orbit geometry + slant-range parameters  
- SAFE annotation metadata  
- grid definitions (10m/30m etc.)  

### Outputs

- `gamma0_vv.tif`  
- `gamma0_vh.tif`  
- optional incidence-angle band  
- RTC metadata:

~~~json
{
  "rtc": {
    "product": "gamma0",
    "projection": "EPSG:32614",
    "grid_definition": "10m",
    "dem_source": "Copernicus-30",
    "terrain_normalization": true
  }
}
~~~

Outputs feed **coherence**, **flood**, **wetlands**, and **deformation**.

---

## 🧬 4. Processing Steps

### 1️⃣ DEM Preparation
- Mosaic / warp DEM to the fixed KFM CRS  
- Hydrologically-aware gap filling  
- Clip to burst/footprint geometry  

### 2️⃣ Local Incidence Angle Calculation
Derived from:
- slant-range geometry  
- orbit metadata  
- DEM slope/aspect  

### 3️⃣ Terrain Normalization (σ⁰ → γ⁰)

Gamma-naught uses the standard model:

~~~text
γ⁰ = σ⁰ * (cos(θ_local) / cos(θ_incident))
~~~

### 4️⃣ Projection to KFM Grid
- Snap to fixed grid (`grid_defs/`)  
- Orthorectify to ground geometry  
- Output per-polarization γ⁰ tiles  

### 5️⃣ Metadata & QA
- DEM provenance  
- grid definition version  
- terrain-correction method  
- radiometric lineage  

---

## 🔗 5. PROV-O Lineage

RTC transform contributes:

~~~json
{
  "prov:Activity": "s1_rtc_generation",
  "prov:used": ["sigma0_vv", "sigma0_vh", "dem", "orbit_metadata"],
  "prov:generated": ["gamma0_vv", "gamma0_vh"],
  "prov:wasAssociatedWith": "KFM-S1-ETL"
}
~~~

This lineage is attached to all RTC-dependent STAC Items.

---

## 🔐 6. FAIR+CARE & Sovereignty Rules

RTC is classified **CARE-A**, but must propagate upstream governance fields:

- `"kfm:care_label"`  
- `"kfm:h3_sensitive"`  
- `"kfm:governance_notes"`  

Sovereignty masking **does not** occur in RTC itself,  
but RTC output feeds transforms where masking **is mandatory**,  
such as **flood**, **wetlands**, and **deformation**.

---

## 🧪 7. Testing Requirements

Tests validate:

- DEM alignment and CRS consistency  
- projection fidelity  
- γ⁰ numerical stability  
- correct local incidence angle computation  
- match against reference `rtc_reference_gamma0.tif`  
- deterministic (bit-exact) output stability  

Failures → **CI block**.

---

## 🧭 8. Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v11.2.2 | 2025-11-29 | Fully regenerated RTC transform README; strict emoji Option-A style; fixed box-safe formatting; zero drift. |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅ Back](../README.md) · [🧪 RTC Tests](../tests/README.md) · [📁 Fixtures](../fixtures/README.md)

</div>

