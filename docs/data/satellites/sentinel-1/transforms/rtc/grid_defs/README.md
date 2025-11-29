---
title: "📐 Sentinel-1 RTC — Grid Definition Files (Projection · Resolution · Snap Grid)"
path: "docs/data/satellites/sentinel-1/transforms/rtc/grid_defs/README.md"
version: "v11.2.2"
last_updated: "2025-11-29"

classification: "Internal Technical (Raster Grid Config)"
status: "Active · Enforced"
release_stage: "Stable · Governed"
lifecycle: "LTS"
review_cycle: "Quarterly · Remote Sensing WG · FAIR+CARE Council"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
provenance_profile: "KFM-PROV-O v11.2"

commit_sha: "<latest-commit>"
previous_version_hash: "<prev-sha>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../../../releases/v11.2.2/data-telemetry.json"
telemetry_schema: "../../../../../../../schemas/telemetry/sat-rtc-griddefs-v11.json"

governance_ref: "../../../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

fair_category: "F1-A1-I1-R1"
care_label: "CARE-A"
indigenous_rights_flag: false
sensitivity_level: "Low"
risk_category: "Low"
public_exposure_risk: "Low"
redaction_required: false

data_steward: "Remote Sensing Working Group"

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "DataTransform"
  prov_o: "prov:Entity"
  geosparql: "geo:Feature"
  owl_time: "Instant"

json_schema_ref: "../../../../../../../schemas/json/sentinel1-rtc-griddefs-v11.json"
shape_schema_ref: "../../../../../../../schemas/shacl/sentinel1-rtc-griddefs-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:sentinel1:transform-rtc-griddefs:v11.2.2"
semantic_document_id: "kfm-doc-data-sentinel1-transform-rtc-griddefs"
event_source_id: "ledger:docs/data/satellites/sentinel-1/transforms/rtc/grid_defs/README.md"
immutability_status: "version-pinned"
machine_extractable: true

accessibility_compliance: "WCAG 2.1 AA+"
ttl_policy: "36 months"
sunset_policy: "Superseded on next grid-definition schema update"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 📐 **Sentinel-1 RTC — Grid Definition Directory**  
`docs/data/satellites/sentinel-1/transforms/rtc/grid_defs/`

Grid definition files controlling **pixel alignment**, **resolution**, and  
**projection snap grids** for γ⁰ Radiometric Terrain Correction (RTC).

</div>

---

## 🗂️ 1. Directory Layout (Strict Option-A Emoji Style)

~~~text
docs/data/satellites/sentinel-1/transforms/rtc/grid_defs/
├── 📄 README.md
│
├── 📄 grid_10m.json         # 10-meter resolution snap grid
└── 📄 grid_30m.json         # 30-meter resolution snap grid
~~~

✔ Emoji BEFORE filenames  
✔ Matches RTC → dem/tests/fixtures style  
✔ Zero drift, no missing folders  

---

## 📘 2. Purpose

These grid-definition files define:

- **Output resolution** for RTC γ⁰ rasters  
- **Grid origin and alignment** (snap grid)  
- **Projection** (e.g., EPSG:32614)  
- **Tile size**, **pixel size**, and **extent rules**  
- **Orthorectification consistency across scenes**

They ensure every γ⁰ raster produced by RTC aligns perfectly in:

- pixel boundaries  
- resolution  
- projection  
- map index  
- downstream spatial joins  

---

## 🧩 3. What Each Grid Definition Contains

Each grid definition JSON includes at minimum:

~~~json
{
  "projection": "EPSG:32614",
  "resolution": 10,
  "pixel_size": 10,
  "origin_x": 300000,
  "origin_y": 4300000,
  "tile_width": 10980,
  "tile_height": 10980,
  "no_data_value": -32768
}
~~~

### Key Parameters

- **projection** — CRS used for RTC products  
- **resolution** — pixel size in meters  
- **origin_x / origin_y** — snap grid origin  
- **tile_width / tile_height** — aligned tile dimensions  
- **no_data_value** — raster fill value for missing DEM areas  

All parameters must pass:

- JSON Schema validation  
- SHACL structure validation  
- consistency with DEM tile CRS  

---

## 🔗 4. PROV-O Lineage

Grid-definition files are **prov:Entity** inputs to RTC:

~~~json
{
  "prov:Entity": "rtc_griddef_10m",
  "grid:resolution": 10,
  "grid:projection": "EPSG:32614",
  "kfm:care_label": "CARE-A"
}
~~~

The RTC transform attaches this lineage to the resulting γ⁰ rasters.

---

## 🔐 5. FAIR+CARE Notes

Grid-definition files:

- contain **no sensitive or sovereign data**  
- classified as **CARE-A**  
- require no masking  
- must remain version-pinned for reproducibility  

They **propagate upstream governance metadata** but do not modify it.

---

## 🧪 6. CI Validation

CI checks:

- schema validity  
- pixel size consistency  
- CRS correctness  
- deterministic snap-grid alignment  
- compatibility with DEM tiles  
- provenance registration  

Any inconsistency blocks the RTC transform pipeline.

---

## 🧭 7. Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v11.2.2 | 2025-11-29 | Initial strict, non-drifting RTC grid-definition README. |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅ Back](../README.md) · [🗺️ DEM Directory](../dem/README.md) · [🛡 Governance](../../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

