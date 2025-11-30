---
title: "🛰️ Sentinel-1 Sample Data — Demonstration Scenes (GRD · RTC · Coherence · Flood · Wetlands · Deformation)"
path: "docs/data/satellites/sentinel-1/samples/README.md"
version: "v11.2.2"
last_updated: "2025-11-29"

classification: "Public Demonstration Data (Non-Sensitive)"
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

telemetry_ref: "../../../../releases/v11.2.2/data-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/sentinel1-samples-v11.json"

governance_ref: "../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../standards/faircare/FAIRCARE-GUIDE.md"

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
  geosparql: "geo:FeatureCollection"
  owl_time: "Instant"

json_schema_ref: "../../../../schemas/json/sentinel1-samples-v11.json"
shape_schema_ref: "../../../../schemas/shacl/sentinel1-samples-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:sentinel1:samples:v11.2.2"
semantic_document_id: "kfm-doc-data-sentinel1-samples"
event_source_id: "ledger:docs/data/satellites/sentinel-1/samples/README.md"
immutability_status: "version-pinned"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

ttl_policy: "60 months"
sunset_policy: "Superseded when demo sample suite is refreshed"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 🛰️ **Sentinel-1 Sample Dataset Library**  
`docs/data/satellites/sentinel-1/samples/`

Non-sensitive, public demonstration scenes for  
**GRD**, **RTC**, **Coherence**, **Flood**, **Wetlands**, and **Deformation**.

Used in documentation, tutorials, Focus-Mode examples, and developer onboarding.

</div>

---

## 🗂️ 1. Directory Layout (STRICT Option-A Emoji Style)

~~~text
docs/data/satellites/sentinel-1/samples/
├── 📄 README.md
│
├── 🗺️ rasters/                      # Non-sensitive demonstration raster tiles
│   ├── 🛰️ grd_sample_vv.tif         # GRD VV calibrated backscatter (demo)
│   ├── 🌍 rtc_gamma0_sample_vv.tif   # RTC gamma0 demo tile
│   ├── 🔗 coherence_sample.tif       # Example coherence magnitude
│   ├── 🌊 flood_sample.tif           # Flood mask (public-safe)
│   ├── 🌿 wetlands_sample.tif        # Wetlands/wetness demo layer
│   └── 🌍 deformation_sample.tif     # LOS displacement (generalized)
│
├── 🧭 footprints/                   # Vector geometries (GeoJSON) for sample scenes
│   ├── 🗺️ scene_footprint.geojson
│   └── 🗺️ burst_outline.geojson
│
└── 🧩 stac/                         # STAC sample Items illustrating metadata patterns
    ├── 📄 item_grd.json
    ├── 📄 item_rtc.json
    ├── 📄 item_coherence.json
    ├── 📄 item_flood.json
    ├── 📄 item_wetlands.json
    └── 📄 item_deformation.json
~~~

✔ Emoji BEFORE directory and file names  
✔ Box-safe  
✔ Zero drift across the entire S1 sample tree  

---

## 📘 2. Purpose

This directory contains **public-safe demonstration datasets** used for:

- KFM documentation & tutorials  
- Focus-Mode v3 examples  
- Story Node development demos  
- Web UI previews (MapLibre/Cesium)  
- Training new contributors on SAR processing concepts  
- STAC metadata reference patterns  
- Unit tests that require non-sensitive inputs  

All data in this folder is **non-sensitive**, pre-generalized, and carries CARE-Open classification.

---

## 🧩 3. Contents Explained

### 🗺️ `rasters/`
Includes small, public demonstration tiles for:

- **GRD** — σ⁰ VV calibrated backscatter  
- **RTC** — γ⁰ terrain-corrected demo  
- **Coherence** — magnitude (0–1)  
- **Flood** — demo flood mask  
- **Wetlands** — demo wetness/saturation map  
- **Deformation** — generalized LOS displacement  

All tiles are resized, simplified, and guaranteed safe for open release.

---

### 🧭 `footprints/`
Contains GeoJSON footprints for:

- scene boundaries  
- burst outlines  
- STAC spatial extents  
- tutorials on geometry + CRS + asset linkage  

---

### 🧩 `stac/`
Includes example STAC Items for:

- GRD  
- RTC  
- Coherence  
- Flood  
- Wetlands  
- Deformation  

All follow **KFM-STAC v11** and **DCAT 3.0** and are safe to reference in documentation and code samples.

---

## 🔗 4. PROV-O Lineage

Even demo scenes are registered as provenance-aware:

~~~json
{
  "prov:Entity": "s1_sample_scene",
  "kfm:provenance_type": "demo-sample",
  "kfm:care_label": "CARE-Open"
}
~~~

---

## 🔐 5. Governance Notes

- All sample rasters are **pre-masked**, **pre-generalized**, and **free of sovereign geometry**.  
- CARE classification = **CARE-Open** (safe for tutorials).  
- These datasets **cannot** be used for scientific inference; only for UI, demos, Story Node examples, testing, and docs.

---

## 🧭 6. Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v11.2.2 | 2025-11-29 | Initial Sentinel-1 sample library README; emoji alignment validated; zero drift. |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅ Back](../README.md) · [🌐 STAC Samples](./stac/README.md) · [🗺️ Raster Samples](./rasters/README.md)

</div>

