---
title: "🟫 Kansas Frontier Matrix — Sediment STAC Collection (Hydrology Domain, v11 Super-Edition)"
path: "data/stac/hydrology/sediment/README.md"
version: "v11.0.0"
last_updated: "2025-11-21"
review_cycle: "Annual • Hydrology & Sediment Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/data-stac-hydro-sediment-index-v1.json"
governance_ref: "../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active • Enforced"
doc_kind: "STAC Collection Index"
intent: "stac-hydrology-sediment-index"
semantic_document_id: "kfm-stac-hydrology-sediment-index"
doc_uuid: "urn:kfm:stac:hydrology:sediment:index:v11.0.0"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
fair_category: "F1-A1-I1-R1"
care_label: "Public / Low-Risk"
immutability_status: "version-pinned"
---

<div align="center">

# 🟫 **Sediment STAC Collection — Hydrology Domain (v11 Super-Edition)**  
`data/stac/hydrology/sediment/README.md`

**Purpose:**  
Provide the authoritative, system-wide **STAC metadata specification** for all sediment datasets  
in the Kansas Frontier Matrix (KFM). Includes reservoir sedimentation history, bathymetry/DoD  
derivations, sediment cores, sediment volume time-series, suspended sediment in rivers,  
watershed erosion indices, delta migration, geomorphology, lab analytics, and climate-driven  
sediment projections — all aligned to KFM v11 metadata, ontology, and governance requirements.

</div>

---

# 📘 0. Overview

Sediment datasets form one of the **central hydrologic pillars** of the KFM architecture.  
This domain integrates:

- Reservoir sedimentation  
- Sediment core stratigraphy  
- Bathymetry → DoD → volume derivations  
- Suspended sediment transport (TSS)  
- Delta migration  
- Watershed-scale erosion  
- Downstream propagation through Kansas River  
- Climate-sediment interactions (storm intensification, loess erosion)  

The Sediment STAC Collection ensures these datasets are:

- FAIR+CARE compliant  
- STAC 1.0.0 aligned  
- Fully machine-indexable  
- Graph-linked (CIDOC-CRM + GeoSPARQL + OWL-Time)  
- Provenance-rich via PROV-O  
- Ready for Focus Mode v3  
- Story Node–composable  

---

# 🗂️ 1. Directory Layout (Canonical)

```text
data/
└── stac/
    └── hydrology/
        └── sediment/
            ├── collection.json
            └── items/
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

---

# 🧭 2. Sediment Dataset Themes

## ✔ 2.1 Reservoir Sedimentation  
- Bathymetry‐derived DEMs  
- Difference-of-DEM surfaces  
- Sediment accumulation rates  
- Delta & forebay evolution  

## ✔ 2.2 Sediment Core Analytics  
- Core locations (GeoJSON)  
- Stratigraphic depth profiles  
- Grain-size spectra (LISST / sieving)  
- Radioisotope markers (Pb-210, Cs-137)  
- Lab metadata (CSVW)

## ✔ 2.3 Suspended Sediment (TSS)  
- Time-series at reservoir tailwaters  
- Kansas River mainstem TSS datasets  
- Storm vs baseflow sediment delivery  

## ✔ 2.4 Sediment Transport  
- Modeled and observed 1D/2D fluxes  
- Flood-driven sediment redistribution  
- Classification of coarse/fine fractions  
- Multi-reservoir sediment routing

## ✔ 2.5 Watershed Erosion  
- Loess erosion indices  
- County-scale sediment yield estimates  
- Watershed-scale erosion rasters  

## ✔ 2.6 Climate–Sediment Datasets  
- Storm-driven sediment response  
- Long-term projected sediment export  
- Hydroclimate correlation datasets  

---

# 📐 3. Required STAC Metadata (Sediment v11 Profile)

### Core STAC 1.0.0 Fields
```
stac_version
type = "Feature"
id
collection = "sediment-hydrology"
geometry
bbox
properties.datetime
assets
```

### Required Sediment `kfm:*` Fields
| Field | Purpose |
|-------|---------|
| `kfm:parameter` | e.g., sediment_core, TSS, dod, delta_position |
| `kfm:units` | meters, mg/L, g/cm3, m3, class index |
| `kfm:provider` | USACE, USGS, KDHE, KWO, KFM |
| `kfm:method` | multibeam, LISST, lab, model |
| `kfm:site` | core ID, transect ID, station ID |
| `kfm:lineage` | ETL → STAC provenance |
| `kfm:quality` | QA tier |
| `kfm:hydro_region` | reservoir, river reach, watershed ID |
| `kfm:project` | Sedimentation-History, SedimentRouting, etc. |

### Recommended Fields  
- `kfm:grain_class`  
- `kfm:habitat_type` (if ecological link)  
- `kfm:core_depth_range`  
- `kfm:dominant_fraction`  

---

# 🧭 4. Asset Standards

## ✔ COG Rasters
Used for:
- Bathymetry → DoD  
- Delta migration rasters  
- Sediment volume grids  
- Erosion rasters  

Must include:
- `proj:*` fields  
- Cloud optimization  
- Checksums  

---

## ✔ GeoJSON
Used for:
- Core locations  
- Delta edges  
- Sediment transport lines  
- Watershed polygons  

---

## ✔ CSVW / CSV
Used for:
- Sediment volume time-series  
- Core lab results  
- TSS datasets  
- Sediment yield tables  

Columns must include:
`timestamp, site_id, parameter, value, units, qc_flag, provenance_id`

---

## ✔ NetCDF
Used for:
- Climate–sediment datasets  
- Hydrodynamic & sediment-transport model outputs  

---

## ✔ MP4
Optional for:
- Underwater video of cores  
- Delta surveys  
- Field sampling documentation  

---

# 🧪 5. Example STAC Items

## ✔ 5.1 Sediment Core Location

```json
{
  "stac_version": "1.0.0",
  "type": "Feature",
  "id": "sediment-core-locations",
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
    "kfm:hydro_region": "Tuttle_Creek_Reservoir",
    "kfm:project": "Sedimentation-History"
  },
  "assets": {
    "geojson": {
      "href": "https://example.org/sediment/core_locations.geojson",
      "type": "application/geo+json",
      "roles": ["data"]
    }
  }
}
```

---

## ✔ 5.2 Suspended Sediment (TSS) Dataset

```json
{
  "stac_version": "1.0.0",
  "type": "Feature",
  "id": "tss-mainstem-2020-2025",
  "collection": "sediment-hydrology",
  "geometry": { "type": "Point", "coordinates": [-96.61, 39.28] },
  "bbox": [-96.62, 39.27, -96.60, 39.29],
  "properties": {
    "datetime": "2025-01-01T00:00:00Z",
    "kfm:parameter": "tss",
    "kfm:units": "mg/L",
    "kfm:provider": "KDHE",
    "kfm:method": "lab",
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

# 🧠 6. Ontology Mapping (CIDOC-CRM + GeoSPARQL + OWL-Time + PROV-O)

## CIDOC-CRM  
- `E73 InformationObject` → dataset  
- `E53 Place` → sediment deposition area or core site  
- `E7 Activity` → field sampling, bathymetry survey, lab analysis  
- `E3 ConditionState` → sedimentation state  
- `E39 Actor` → agency, lab, research team  

## GeoSPARQL  
- `geo:hasGeometry`  
- `geo:sfWithin`  
- `geo:asWKT`  

## OWL-Time  
- `time:hasTime`  
- `time:hasBeginning`, `time:hasEnd`  

## PROV-O  
- `prov:wasGeneratedBy`  
- `prov:used`  
- `prov:wasAttributedTo`  
- `prov:wasDerivedFrom`  

---

# 🛰️ 7. ETL → STAC → Graph Pipeline

```
Raw Data
    ↓ extract
Spatial/temporal harmonization
    ↓ transform
Asset generation (COG, CSVW, GeoJSON, NetCDF)
    ↓ annotate
STAC Item creation
    ↓ stac-validate
Graph ingestion (Neo4j: CIDOC + GeoSPARQL + OWL-Time)
    ↓
Focus Mode + Story Node integration
```

ETL provenance MUST be documented in:

```
mcp/experiments/hydrology/sediment/
```

---

# 🎯 8. Focus Mode v3 Integration

Sediment Items power:

- Sediment accumulation timelines  
- Delta migration & forebay evolution  
- Sediment routing through reservoirs → Kansas River  
- TSS/turbidity anomalies after storms  
- Watershed erosion → reservoir deposition links  
- Story Node environmental context  

Focus Mode queries Items via:

- place  
- parameter (`sediment_core`, `tss`, `dod`, `delta`, `erosion`)  
- time range  
- hydrologic region  

---

# 📖 9. Story Node Integration

Sediment datasets feed narrative nodes such as:

- **“A Reservoir Filling from the Bottom Up”**  
- **“Sediment on the Move”**  
- **“Watershed to Reservoir: Loess Erosion Pathways”**  
- **“Flood Pulses and Sediment Redistribution”**  

Story Nodes reference Items by ID:

```json
{
  "rel": "uses-dataset",
  "target": "sediment-volumes-timeseries"
}
```

---

# 🚀 10. Expansion Roadmap

Future sediment STAC Items:

- Annual multi-reservoir sediment volume grids  
- CMIP6-driven sediment forecasts  
- Machine-learning DoD predictions  
- Real-time turbidity–sediment fusion datasets  
- Sediment fingerprinting datasets (isotope-based)  
- UAV photogrammetry bathymetry for shallow deltas  
- 3D point-cloud sediment layers (`.las/.laz`)  
- Flood-driven sediment redistribution models  

---

# 🕰 Version History

- **v11.0.0 (2025-11-21):** Initial super-edition creation of Sediment STAC Collection.

---

[⬅ Back to Hydrology STAC Domain](../README.md) • [📂 Data Index](../../../README.md) • [🏠 KFM Master Guide](../../../../../docs/reference/kfm_v11_master_documentation.md)

