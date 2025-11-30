---
title: "🗺️ Sentinel-1 Sample Rasters — Demonstration Tiles (GRD · RTC · Coherence · Flood · Wetlands · Deformation)"
path: "docs/data/satellites/sentinel-1/samples/rasters/README.md"
version: "v11.2.2"
last_updated: "2025-11-29"

classification: "Public Demonstration Data (CARE-Open · Non-Sensitive)"
status: "Active · Stable"
release_stage: "Stable"
lifecycle: "LTS"

review_cycle: "Annual · Remote Sensing WG"
license: "CC-BY 4.0"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
provenance_profile: "KFM-PROV-O v11.2"

commit_sha: "<latest>"
previous_version_hash: "<prev>"
doc_integrity_checksum: "<sha256>"

telemetry_ref: "../../../../../releases/v11.2.2/data-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/sentinel1-samples-rasters-v11.json"

governance_ref: "../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../standards/faircare/FAIRCARE-GUIDE.md"

fair_category: "F1-A1-I2-R1"
care_label: "CARE-Open"
indigenous_rights_flag: false
sensitivity_level: "None"
public_exposure_risk: "Low"
risk_category: "Low"

data_steward: "Remote Sensing Working Group"

ontology_alignment:
  cidoc: "E84 Information Carrier"
  schema_org: "Dataset"
  prov_o: "prov:Entity"
  geosparql: "geo:Feature"
  owl_time: "Instant"

json_schema_ref: "../../../../../schemas/json/sentinel1-samples-rasters-v11.json"
shape_schema_ref: "../../../../../schemas/shacl/sentinel1-samples-rasters-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:sentinel1:samples-rasters:v11.2.2"
semantic_document_id: "kfm-doc-data-sentinel1-samples-rasters"
event_source_id: "ledger:docs/data/satellites/sentinel-1/samples/rasters/README.md"
immutability_status: "version-pinned"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

ttl_policy: "60 months"
sunset_policy: "Superseded when sample demo tiles are refreshed"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 🗺️ **Sentinel-1 Sample Raster Tiles**  
`docs/data/satellites/sentinel-1/samples/rasters/`

Public-safe example Sentinel-1 raster tiles used in  
tutorials, documentation, notebooks, Story Node demos,  
and Focus Mode v3 development.

</div>

---

## 🗂️ 1. Directory Layout (STRICT Option-A Emoji Style)

~~~text
docs/data/satellites/sentinel-1/samples/rasters/
├── 📄 README.md
│
├── 🛰️ grd_sample_vv.tif          # GRD VV calibrated backscatter (σ⁰)
├── 🌍 rtc_gamma0_sample_vv.tif    # RTC gamma0 terrain-normalized backscatter (γ⁰)
├── 🔗 coherence_sample.tif        # Coherence magnitude sample (0–1)
├── 🌊 flood_sample.tif            # Flood mask (public-safe demonstration)
├── 🌿 wetlands_sample.tif         # Wetlands/wetness demo layer (γ⁰ + seasonal model)
└── 🌍 deformation_sample.tif      # Generalized LOS displacement (sovereignty-safe)
~~~

✔ Emoji BEFORE filenames  
✔ Identical style to sentinel-1 QA fixture directories  
✔ Zero drift, no fence breaks  

---

## 📘 2. Purpose

This directory contains **non-sensitive, public demonstration rasters** supporting:

- documentation pages  
- tutorials & examples  
- Focus Mode v3 UI demos  
- Story Node v3 environmental narratives  
- developer onboarding  
- STAC examples  
- web/MapLibre/Cesium rendering demos  
- quick-start testing without using sensitive datasets  

All sample rasters are **pre-generalized** and carry **CARE-Open** classification.

---

## 🧩 3. Raster Descriptions

### 🛰️ `grd_sample_vv.tif`
- Demonstration GRD calibrated (σ⁰) tile  
- Used for reflectivity tutorials  
- Pre-clipped and safe for public release  

### 🌍 `rtc_gamma0_sample_vv.tif`
- Example terrain-corrected γ⁰ backscatter  
- Shows DEM-corrected illumination patterns  

### 🔗 `coherence_sample.tif`
- Sample coherence magnitude raster (0–1)  
- Useful for explaining stable vs decorrelated surfaces  

### 🌊 `flood_sample.tif`
- Public-safe flood mask  
- Small, downsampled tile for demos  

### 🌿 `wetlands_sample.tif`
- Demonstration wetness/wetland probability layer  
- Based on γ⁰ + seasonal priors (safe pseudo-data)  

### 🌍 `deformation_sample.tif`
- Generalized LOS displacement tile  
- Opposite of sensitive InSAR data: pre-blurred & sovereignty-safe  
- Useful for showing deformation overlays in Focus Mode  

---

## 🔗 4. PROV-O Lineage for Demo Tiles

Even demo samples carry provenance:

~~~json
{
  "prov:Entity": "s1_demo_raster_sample",
  "kfm:provenance_type": "demo-sample",
  "kfm:care_label": "CARE-Open"
}
~~~

Ensuring clarity for documentation and reproducibility.

---

## 🔐 5. Governance Notes

- All datasets here are **non-sensitive**, **generalized**, **safe for open use**.  
- No raw sovereign geometries are included.  
- Raster values are for **demonstration only**, not valid for analysis.  

---

## 🧭 6. Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v11.2.2 | 2025-11-29 | Initial Sentinel-1 sample raster README; emoji alignment validated; zero drift. |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅ Back](../README.md) · [🧭 Footprints](../footprints/README.md) · [🧩 STAC Samples](../stac/README.md)

</div>

