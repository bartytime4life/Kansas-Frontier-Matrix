---
title: "🗺️ NASA SMAP — Sample Rasters (Synthetic · Miniature · Tutorial-Safe COGs)"
path: "docs/data/satellites/smap/samples/rasters/README.md"
version: "v11.2.2"
last_updated: "2025-11-29"

classification: "Public · Non-Sensitive · Synthetic/Degraded Examples"
status: "Active / Public"
release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Annual · Documentation Systems WG · FAIR+CARE Council"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
provenance_profile: "KFM-PROV-O v11.2"

commit_sha: "<latest-commit>"
previous_version_hash: "<prev-sha>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../releases/v11.2.2/data-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/sat-smap-v11.json"

governance_ref: "../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

fair_category: "F1-A1-I1-R1"
care_label: "CARE-A (Public / Low-Risk)"
indigenous_rights_flag: false
sensitivity_level: "None"
public_exposure_risk: "Low"
risk_category: "Low"
redaction_required: false

data_steward: "Earth Systems Working Group · FAIR+CARE Council"

ontology_alignment:
  cidoc: "E84 Information Carrier"
  prov_o: "prov:Entity"
  schema_org: "Dataset"
  geosparql: "geo:Feature"
  owl_time: "TemporalEntity"

json_schema_ref: "../../../../../schemas/json/smap-sample-rasters-v11.json"
shape_schema_ref: "../../../../../schemas/shacl/smap-sample-rasters-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:smap:sample-rasters-readme:v11.2.2"
semantic_document_id: "kfm-doc-data-smap-sample-rasters"
event_source_id: "ledger:docs/data/satellites/smap/samples/rasters/README.md"
immutability_status: "version-pinned"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
ttl_policy: "72 months"
sunset_policy: "Superseded on next sample dataset refresh"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 🗺️ **NASA SMAP — Sample Raster COGs**  
`docs/data/satellites/smap/samples/rasters/`

**Purpose**  
Provide **small, synthetic, sovereignty-safe raster samples** in Cloud-Optimized GeoTIFF (COG)  
format for:

- mapping tutorials  
- STAC/DCAT examples  
- Story Node v3 demos  
- Focus Mode v3 documentation  
- MapLibre/Cesium example layers  
- CI smoke tests  
- onboarding notebooks  

These are NOT production science rasters.

</div>

---

## 📘 1. Overview

This directory contains *tiny*, *public-safe*, *non-sensitive* geospatial COGs that demonstrate:

- SMAP-like raster structure  
- coordinate system usage  
- tile boundaries and extents  
- geospatial alignment (EPSG:4326 and WebMercator examples)  
- multi-band encoding examples (optional)  
- QA-aware overlays (optional)  
- uncertainty-aware example values  

All rasters are:

- **synthetic**  
- **degraded**  
- **educational-only**  
- **sovereignty-safe** (no H3-sensitive details)  
- **FAIR+CARE vetted**

---

## 🗂️ 2. Directory Layout (Emoji-Rich · Option A)

~~~text
docs/data/satellites/smap/samples/rasters/
├── 📄 README.md                         # This file
│
├── 💧 sm_sample.tif                     # Soil Moisture (synthetic, tiny)
├── 🌡️ ft_sample.tif                     # Freeze–Thaw state sample
├── 🌿 vwc_sample.tif                    # Vegetation Water Content sample
├── 📉 uncertainty_sample.tif            # Uncertainty-scaling sample grid
│
└── 🗺️ thumbnails/                       # Preview PNGs for docs/UI
    ├── sm_preview.png
    ├── ft_preview.png
    ├── vwc_preview.png
    └── uncertainty_preview.png
~~~

---

## 🧩 3. Raster Responsibilities

### 💧 `sm_sample.tif` (Soil Moisture Example)
Demonstrates:

- grid alignment  
- safe synthetic SM values (0–1 range or arbitrary values)  
- STAC “soil-moisture” asset usage  
- doc/tutorial compatibility  

### 🌡️ `ft_sample.tif` (Freeze–Thaw Example)
Demonstrates:

- frozen/thawed categorical state example  
- synthetic seasonal boundaries  
- simple FT colormaps for tutorials  

### 🌿 `vwc_sample.tif` (Vegetation Water Content)
Demonstrates:

- canopy water content example grid  
- synthetic VWC values for QA/uncertainty docs  
- safe cross-dataset overlays  

### 📉 `uncertainty_sample.tif`
Demonstrates:

- uncertainty multipliers  
- QA-derived scaling pattern (synthetic)  
- usage in Focus Mode v3 and docs  
- STAC uncertainty metadata linkage  

---

## 🔐 4. FAIR+CARE & Sovereignty Notes

These sample rasters:

- contain **no real-world SMAP data**  
- contain **no sensitive ecological/cultural features**  
- are **pre-cleared** for unrestricted public demos  
- include optional **CARE/H3 metadata fields** only for tutorial demonstration  
- follow governance rules but **do not require masking**  

They are *safe for distribution*, screenshots, documentation, workshops, and training.

---

## 🧪 5. Validation & CI Integration

CI runs lightweight validation:

- raster integrity checks  
- COG structural validation  
- STAC sample metadata linking  
- GeoJSON footprint matching  
- CRS detection  
- thumbnail availability  
- accessibility metadata (alt-text for thumbnails)  

Failures indicate broken documentation assets.

---

## 🔁 6. Relationship to SMAP ETL Pipeline

These sample rasters **do not participate** in ETL or production data.

They support:

- documentation  
- onboarding  
- examples for Focus Mode & Story Node  
- STAC/DCAT tutorial sections  
- CI smoke tests & unit-test demonstrations  

Production rasters live under:

```
data/satellites/smap/stac/
data/satellites/smap/qa/
data/satellites/smap/transforms/
```

---

## 🔮 7. Applications Across KFM

- 🗺️ Tutorial map layers  
- 🧭 Focus Mode DEMO context  
- 📘 Markdown documentation figures  
- 🧪 Unit-test mocks  
- 🧠 Developer training  
- 📚 Workshops & public presentations  

---

## 🧭 8. Version History

| Version | Date       | Summary                                                                                              |
|--------:|------------|------------------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-29 | Initial sample raster README; public-safe COGs; FAIR+CARE aligned; tutorial-ready; emoji-enhanced.   |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅️ Back](../README.md) · [📦 STAC Samples](../stac/README.md) · [🛡 Governance](../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

