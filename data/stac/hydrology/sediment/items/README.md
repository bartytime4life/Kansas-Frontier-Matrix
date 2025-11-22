---
title: "🟫 Kansas Frontier Matrix — Sediment STAC Items Index (Hydrology Domain, v11 Super-Edition)"
path: "data/stac/hydrology/sediment/items/README.md"
version: "v11.0.0"
last_updated: "2025-11-21"
review_cycle: "Annual • Hydrology & Sediment Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../../../../schemas/telemetry/data-stac-hydro-sediment-items-v1.json"
governance_ref: "../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active • Enforced"
doc_kind: "STAC Items Index"
intent: "stac-hydrology-sediment-items-index"
semantic_document_id: "kfm-stac-hydrology-sediment-items-index"
doc_uuid: "urn:kfm:stac:hydrology:sediment:items:index:v11.0.0"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
fair_category: "F1-A1-I1-R1"
care_label: "Public-Low-Risk"
immutability_status: "version-pinned"
---

<div align="center">

# 🟫 **Sediment STAC Items Index — Hydrology Domain (v11 Super-Edition)**  
`data/stac/hydrology/sediment/items/README.md`

**Purpose:**  
Provide the full, authoritative, domain-level specification for all **sediment-related STAC Items**  
within the Kansas Frontier Matrix (KFM). Covers reservoir sedimentation, bathymetry→DoD,  
sediment cores, TSS, delta migration, sediment routing, watershed erosion, and  
climate-sediment dynamics. Defines metadata rules, asset standards, ontology mapping, provenance,  
and integration into Focus Mode v3 and Story Node v3.

</div>

---

# 📘 0. Overview

Sediment Items represent the **core geospatial & temporal foundation** for:

- Reservoir capacity loss & sedimentation history  
- Density-current transport analysis  
- Delta migration  
- Sediment budget modeling  
- Downstream TSS propagation  
- Climate–sediment correlations  
- Sediment source attribution (loess, basin erosion)  
- WID & dredging feasibility studies  
- Multi-reservoir sediment cascades (Milford → Tuttle → Perry → Clinton → Kansas River)  

This document defines **every metadata requirement and governing rule** for STAC Items in this  
folder and all nested sediment Item directories across KFM.

---

# 🗂️ 1. Directory Layout

```text
data/
└── stac/
    └── hydrology/
        └── sediment/
            ├── README.md                 # Collection-level spec
            └── items/                    # THIS DIRECTORY
                ├── sediment-core-locations.json
                ├── sediment-core-profiles.json
                ├── sediment-volumes-timeseries.json
                ├── dod-1970-1990.json
                ├── dod-1990-2010.json
                ├── dod-2010-2024.json
                ├── delta-migration.json
                ├── tss-mainstem.json
                ├── tss-downstream.json
                ├── sediment-transport.json
                ├── watershed-erosion-index.json
                ├── sediment-yield-county.json
                ├── loess-erosivity.json
                ├── climate-sediment-response.json
                └── sediment-lab-results.json
```

Each file is a **STAC Item** with strict KFM Hydrology–Sediment metadata.

---

# 🟫 2. Item Taxonomy (Sediment Domain)

## ✔ 2.1 Reservoir Sedimentation  
- DoD rasters  
- Sediment volume time-series  
- Delta/forebay geometries  
- Bathymetry-derived sediment accumulation  

## ✔ 2.2 Sediment Cores  
- Core location points  
- Core depth × grain-size profiles  
- Lab results (organic matter, mineral fraction, contaminants)  

## ✔ 2.3 Suspended Sediment (TSS / SSC)  
- Time-series at reservoir tailwaters  
- Kansas River mainstem TSS  
- Storm-pulse sediment waves  

## ✔ 2.4 Sediment Transport  
- Modeled flux vectors (GeoJSON/NetCDF)  
- Flood-driven redistribution  
- Multi-reservoir cascading sediment wave tracking  

## ✔ 2.5 Watershed Erosion  
- Loess erosion indices  
- Sediment yield rasters  
- Basin-scale erosion models (RUSLE/WEPP derivatives)  

## ✔ 2.6 Climate–Sediment Interactions  
- Storm intensity versus TSS  
- Flood frequency × sediment loads  
- CMIP6-based projections  

---

# 📐 3. Required STAC Metadata (Sediment v11 Profile)

## 3.1 Core STAC Fields
```
stac_version: "1.0.0"
type: "Feature"
id: "<unique-id>"
collection: "sediment-hydrology"
geometry: { ... }
bbox: [ ... ]
properties.datetime: "<ISO 8601>"
assets: { ... }
```

## 3.2 Required Sediment `kfm:*` Fields

| Field | Description |
|-------|-------------|
| `kfm:parameter` | sediment_core, dod, tss, delta, erosion, etc. |
| `kfm:units` | m, m³, mg/L, g/cm³, %, index |
| `kfm:provider` | USACE, USGS, KDHE, KWO, KFM, university labs |
| `kfm:method` | multibeam, LISST, lab, ADCP, model |
| `kfm:site` | core ID, transect ID, gauge ID |
| `kfm:lineage` | ETL → STAC provenance chain |
| `kfm:quality` | A/B/C/Provisional |
| `kfm:hydro_region` | reservoir, river, watershed region |
| `kfm:project` | Sedimentation-History, SedimentRouting, etc. |

### Recommended
- `kfm:grain_class`  
- `kfm:dominant_fraction`  
- `kfm:habitat_type` (if ecological link)  
- `kfm:core_depth_range`  
- `kfm:crs`, `kfm:vertical_datum`  

---

# 🌍 4. Asset Standards

## ✔ **COG (Raster)**
For:
- DoD elevation changes  
- Delta movement rasters  
- Sediment volumes  
- Watershed erosion rasters  

Must include:
- `proj:*`  
- internal tiling  
- COG overviews  
- `checksum:sha256`  

---

## ✔ **GeoJSON**
For:
- Core locations  
- Delta outlines  
- Sediment transport flowlines  
- Erosion polygons  

---

## ✔ **CSVW / CSV**
For:
- Core lab results  
- Sediment volumes  
- TSS time-series  
- Sediment yield tables  

Required columns:
`timestamp | parameter | value | units | site_id | qc_flag | provenance_id`

---

## ✔ **NetCDF**
For:
- Climate–sediment models  
- Hydrodynamic sediment-transport model outputs  

---

## ✔ **MP4 (optional)**
For:
- Underwater surveys  
- Delta channel migration documentation  

---

# 🧪 5. Example STAC Items

## 5.1 Sediment Core Locations

```json
{
  "stac_version": "1.0.0",
  "type": "Feature",
  "id": "sediment-core-locations-v1",
  "collection": "sediment-hydrology",
  "geometry": { "type": "MultiPoint", "coordinates": [...] },
  "bbox": [...],
  "properties": {
    "datetime": "2024-01-01T00:00:00Z",
    "kfm:parameter": "sediment_core_locations",
    "kfm:units": "none",
    "kfm:provider": "USACE",
    "kfm:method": "gps_survey",
    "kfm:lineage": "etl/sediment_core_locations_v1",
    "kfm:quality": "A",
    "kfm:hydro_region": "Milford_Reservoir",
    "kfm:project": "Sedimentation-History"
  },
  "assets": {
    "geojson": {
      "href": "https://example.org/sediment/core_locations.geojson",
      "type": "application/geo+json",
      "roles": ["data"],
      "checksum:sha256": "..."
    }
  }
}
```

---

## 5.2 DoD Raster Item

```json
{
  "stac_version": "1.0.0",
  "type": "Feature",
  "id": "dod-2010-2024",
  "collection": "sediment-hydrology",
  "geometry": { "type": "Polygon", "coordinates": [...] },
  "bbox": [...],
  "properties": {
    "datetime": "2024-01-01T00:00:00Z",
    "kfm:parameter": "dod",
    "kfm:units": "meters_difference",
    "kfm:provider": "USACE",
    "kfm:method": "difference_of_dem",
    "kfm:lineage": "etl/dod2010_2024_v1",
    "kfm:quality": "A",
    "kfm:hydro_region": "Tuttle_Creek_Reservoir",
    "kfm:project": "Sedimentation-History"
  },
  "assets": {
    "cog": {
      "href": "https://example.org/sediment/dod_2010_2024.tif",
      "type": "image/tiff; application=geotiff; profile=cloud-optimized",
      "roles": ["data"],
      "checksum:sha256": "..."
    }
  }
}
```

---

## 5.3 TSS (Suspended Sediment) Time-Series Item

```json
{
  "stac_version": "1.0.0",
  "type": "Feature",
  "id": "tss-kansasriver-mainstem-2020-2025",
  "collection": "sediment-hydrology",
  "geometry": { "type": "Point", "coordinates": [-96.61, 39.28] },
  "bbox": [-96.62, 39.27, -96.60, 39.29],
  "properties": {
    "datetime": "2025-01-01T00:00:00Z",
    "kfm:parameter": "tss",
    "kfm:units": "mg/L",
    "kfm:provider": "KDHE",
    "kfm:method": "lab_analysis",
    "kfm:lineage": "etl/tss_mainstem_v4",
    "kfm:quality": "A",
    "kfm:hydro_region": "Kansas_River",
    "kfm:project": "SedimentRouting"
  },
  "assets": {
    "csv": {
      "href": "https://example.org/sediment/tss_mainstem_2020_2025.csv",
      "type": "text/csv",
      "roles": ["data"]
    }
  }
}
```

---

# 🧠 6. Ontology Mapping (CIDOC-CRM • GeoSPARQL • OWL-Time • PROV-O)

## CIDOC-CRM
- `E73 InformationObject` — sediment dataset  
- `E53 Place` — core site, delta polygon, erosion region  
- `E7 Activity` — core sampling, lab analysis, bathymetric survey  
- `E3 ConditionState` — sediment accumulation state  
- `E39 Actor` — provider agencies  

## GeoSPARQL
- `geo:hasGeometry`  
- `geo:sfWithin`  
- `geo:asWKT`  

## OWL-Time
- `time:hasTime`  
- `time:hasBeginning` / `time:hasEnd`  

## PROV-O
- `prov:wasGeneratedBy`  
- `prov:used`  
- `prov:wasAttributedTo`  
- `prov:wasDerivedFrom`  

---

# 🛰️ 7. ETL → STAC → Graph Pipeline

```
Raw Sediment Inputs  
    ↓ extract  
QA / reprojection / units harmonization  
    ↓ transform  
Asset generation (COG / CSVW / GeoJSON / NetCDF)  
    ↓ annotate-stac  
STAC Item creation  
    ↓ stac-validate  
Graph ingestion (Neo4j: CIDOC + GeoSPARQL + OWL-Time)  
    ↓  
Focus Mode v3 + Story Node v3 linkage
```

All ETL runs must be recorded under:

```
mcp/experiments/hydrology/sediment/
```

---

# 🎯 8. Focus Mode v3 Integration

Sediment Items drive:

- DoD evolution maps  
- Sediment volume time-series  
- TSS anomaly detection  
- Reservoir-to-river sediment routing  
- Delta migration analytics  
- Multi-reservoir sediment wave propagation  

Focus Mode filters items by:

- `place`,  
- `kfm:parameter`,  
- `kfm:hydro_region`,  
- time range.

---

# 📖 9. Story Node v3 Integration

Sediment Items support narrative blocks such as:

- **“A Reservoir Filling from the Bottom Up”**  
- **“Sediment on the Move”**  
- **“The 1993 Flood Sediment Pulse”**  
- **“Climate Change and Future Sediment Futures”**  
- **“Density Currents & Delta Growth”**

Example reference:

```json
{
  "rel": "uses-dataset",
  "target": "sediment-volumes-timeseries"
}
```

---

# 🚀 10. Expansion Roadmap

Future Items may include:

- Annual high-resolution sediment volume rasters  
- Climate-projected sediment yields (2030–2100)  
- Deep-learning DoD predictions  
- Sediment provenance via isotopes  
- UAV sediment photogrammetry  
- 3D reservoir sediment meshes (.las/.laz)  
- Spatial sediment connectivity networks  

All new Items must follow this **Sediment STAC Profile v11**.

---

# 🕰 Version History

- **v11.0.0 (2025-11-21)** — Initial creation of Sediment STAC Items Super-Edition.

---

[⬅ Back to Sediment STAC Collection](../README.md) • [⬅ Back to Hydrology STAC Domain](../../README.md) • [🏠 KFM v11 Master Guide](../../../../../docs/reference/kfm_v11_master_documentation.md)

