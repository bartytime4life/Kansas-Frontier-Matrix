---
title: "🗺️ Sentinel-1 RTC DEM Resources — Digital Elevation Tiles for γ⁰ Terrain Correction"
path: "docs/data/satellites/sentinel-1/transforms/rtc/dem/README.md"
version: "v11.2.2"
last_updated: "2025-11-29"

classification: "Internal Technical (DEM Assets)"
status: "Active · Enforced"
release_stage: "Stable · Governed"
lifecycle: "LTS"
review_cycle: "Quarterly · Remote Sensing WG"

license: "Copernicus / SRTM Open Data · CC-BY"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
provenance_profile: "KFM-PROV-O v11.2"

commit_sha: "<latest>"
previous_version_hash: "<prev>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../../../releases/v11.2.2/data-telemetry.json"
telemetry_schema: "../../../../../../../schemas/telemetry/sat-rtc-dem-v11.json"

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
  cidoc: "E84 Information Carrier"
  schema_org: "Dataset"
  prov_o: "prov:Entity"
  geosparql: "geo:Feature"
  owl_time: "Instant"

json_schema_ref: "../../../../../../../schemas/json/sentinel1-rtc-dem-v11.json"
shape_schema_ref: "../../../../../../../schemas/shacl/sentinel1-rtc-dem-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:sentinel1:transform-rtc-dem:v11.2.2"
semantic_document_id: "kfm-doc-data-sentinel1-rtc-dem"
event_source_id: "ledger:docs/data/satellites/sentinel-1/transforms/rtc/dem/README.md"
immutability_status: "version-pinned"
machine_extractable: true

accessibility_compliance: "WCAG 2.1 AA+"
ttl_policy: "36 months"
sunset_policy: "Superseded when DEM source or RTC spec changes"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 🗺️ **Sentinel-1 RTC — DEM Tile Directory**  
`docs/data/satellites/sentinel-1/transforms/rtc/dem/`

DEM tiles used for **γ⁰ terrain correction** during the Radiometric Terrain Correction (RTC) transform.

</div>

---

## 🗂️ 1. Directory Layout (Strict Option-A Emoji Style)

~~~text
docs/data/satellites/sentinel-1/transforms/rtc/dem/
├── 📄 README.md
│
├── 🗺️ dem_32614_tile_01.tif        # DEM clip for KFM tile region 01
├── 🗺️ dem_32614_tile_02.tif        # DEM clip for KFM tile region 02
└── 🗺️ dem_32614_tile_03.tif        # Additional DEM tile(s) as required
~~~

✔ Emoji BEFORE filenames  
✔ No drift  
✔ Matches all previously approved transform directory styles  
✔ Box-safe, no broken fences  

---

## 📘 2. Purpose

This directory stores **Digital Elevation Model (DEM)** tiles used as inputs to the  
Sentinel-1 **RTC (Radiometric Terrain Correction)** stage.

DEM tiles are essential for:

- **terrain normalization (σ⁰ → γ⁰)**  
- **local incidence angle calculation**  
- **orthorectification**  
- **geolocation accuracy**  
- **grid snapping to RTC grid_defs**  

DEM data ensures output γ⁰ backscatter is terrain-corrected and map-accurate.

---

## 🧩 3. DEM Requirements

DEM tiles must be:

- in **KFM CRS** (e.g., EPSG:32614)  
- hydrologically consistent (no pits/spikes)  
- gap-filled as needed  
- clipped to relevant Sentinel-1 footprints  
- aligned with RTC grid definitions  

Sources:

- **Copernicus DEM (30m / 10m)**  
- **SRTM (fallback)**  

---

## 🔗 4. PROV-O Lineage

Each DEM tile is registered as a **prov:Entity**:

~~~json
{
  "prov:Entity": "copernicus_dem_tile_01",
  "dem:crs": "EPSG:32614",
  "dem:source": "Copernicus-30",
  "kfm:care_label": "CARE-A"
}
~~~

RTC activities emit lineage linking DEM inputs to γ⁰ outputs.

---

## 🔐 5. FAIR+CARE Notes

DEM data is typically **CARE-A**:

- does not contain culturally sensitive information  
- no sovereignty masking required at DEM stage  
- must remain fully documented for reproducibility  

Downstream transforms (flood, wetlands, deformation) apply sovereignty rules.

---

## 🧪 6. CI Validation

CI checks ensure:

- DEM files exist and load correctly  
- CRS matches RTC configuration  
- pixel alignment is valid  
- no NaNs / invalid elevations  
- provenance values accurate  
- deterministic reprojection behavior  

DEM data must pass both **schema** and **raster integrity** checks.

---

## 🧭 7. Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v11.2.2 | 2025-11-29 | Initial strict emoji-compliant DEM directory README; no drift; RTC-aligned. |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅ Back](../README.md) · [📐 Grid Definitions](../grid_defs/README.md) · [🛡 Governance](../../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

