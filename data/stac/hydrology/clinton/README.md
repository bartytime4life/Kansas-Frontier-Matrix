---
title: "🛰️ Kansas Frontier Matrix — Clinton Lake Hydrology STAC Collection (v11 Super-Edition)"
path: "data/stac/hydrology/clinton/README.md"
version: "v11.0.0"
last_updated: "2025-11-21"
review_cycle: "Annual / Hydrology & Hazards Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/data-stac-hydro-clinton-index-v1.json"
governance_ref: "../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active / Enforced"
doc_kind: "STAC Collection Index"
intent: "stac-hydrology-clinton-index"
semantic_document_id: "kfm-stac-hydrology-clinton-index"
doc_uuid: "urn:kfm:stac:hydrology:clinton:index:v11.0.0"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
fair_category: "F1-A1-I1-R1"
care_label: "Public / Low-Risk"
immutability_status: "version-pinned"
---

<div align="center">

# 🛰️ **Clinton Lake Hydrology STAC Collection — v11 Super-Edition**  
`data/stac/hydrology/clinton/README.md`

**Purpose:**  
Provide the authoritative STAC documentation for **Clinton Lake** hydrology datasets, including  
bathymetry, inflows, outflows, sedimentation, turbidity/DO, WQ, downstream effects,  
hydro-climate drivers, and ecosystem-linked hydrologic observations.  
Defines metadata, asset standards, lineage, ontology alignment, ETL/STAC/graph workflows, and  
integration with Focus Mode v3 and Story Nodes.

</div>

---

# 📘 0. Overview

Clinton Lake, located in **Douglas County, Kansas**, is a multi-purpose reservoir serving:

- Flood control  
- Water supply  
- Water quality enhancement  
- Recreation  
- Ecological habitat preservation  

The hydrology datasets for Clinton Lake are cataloged here as **STAC 1.0.0–compliant metadata**, ensuring  
machine discoverability, provenance, spatiotemporal searchability, and full alignment with KFM v11.

---

# 🗂️ 1. Directory Layout (Canonical)

```text
data/
└── stac/
    └── hydrology/
        └── clinton/
            ├── collection.json
            └── items/
                ├── bathymetry-1994.json
                ├── bathymetry-2010.json
                ├── bathymetry-2022.json
                ├── hydrology-inflows.json
                ├── hydrology-outflows.json
                ├── wq-turbidity.json
                ├── wq-do.json
                ├── sediment-cores.json
                ├── sediment-volumes.json
                ├── downstream-do.json
                ├── downstream-turbidity.json
                ├── ecology-fish.json
                └── ecology-mussels.json
```

This structure mirrors **Tuttle Creek**, **Milford**, and **Perry** STAC profiles for cross-reservoir consistency.

---

# 🌍 2. Spatial + Temporal Extents

### Spatial extent (Clinton Lake reservoir polygon bbox):
```
[-95.47, 38.86, -95.27, 38.99]
```

### Temporal extent:
```
1977-01-01T00:00:00Z → present
```

All Items must fall within this spatiotemporal envelope.

---

# 🛰️ 3. Clinton Lake STAC Profile (Hydrology Domain v11)

All Items **must** comply with the KFM hydrology STAC profile:

### ✔ Required STAC fields
- `stac_version = "1.0.0"`
- `type = "Feature"`
- `id`
- `collection = "clinton-lake-hydrology"`
- `geometry`
- `bbox`
- `properties.datetime`
- `assets`

### ✔ Hydrology-specific `kfm:*` metadata (mandatory)
| Field | Meaning |
|-------|---------|
| `kfm:parameter` | hydrologic variable |
| `kfm:units` | SI or hydrology domain units |
| `kfm:site` | Site ID (USGS gauge, WQ station, bathy region) |
| `kfm:provider` | USACE / USGS / KDHE / KWO |
| `kfm:method` | sensor/algorithm/survey type |
| `kfm:lineage` | ETL → STAC provenance |
| `kfm:quality` | QA/QC class |
| `kfm:hydro_region` | `Clinton_Reservoir` or subreach |
| `kfm:project` | e.g., “Hydrology-Core”, “Sedimentation-History” |

---

# 🌊 4. Dataset Themes in This Collection

## ✔ 4.1 Bathymetry (DEM, DoD)
- `bathymetry-1994.json`  
- `bathymetry-2010.json`  
- `bathymetry-2022.json`  
- `dod-1994-2010.json` *(future)*  
- `dod-2010-2022.json` *(future)*  

Bathymetry informs:
- Storage loss  
- Delta position  
- Sediment transport  
- Pre-WID hypothetical modeling  

---

## ✔ 4.2 Hydrology Time-Series (CSVW)
- inflows (USGS)  
- outflows (USACE)  
- reservoir pool elevation  
- storage curves  
- downstream gauge hydrographs  

---

## ✔ 4.3 Water Quality (WQ)
- Turbidity (NTU)  
- DO (mg/L)  
- Nutrients  
- Chlorophyll-a (optional)  

Monitoring sites include:
- Tailwater zone  
- Up-reservoir WQ buoys  
- Downstream reaches  

---

## ✔ 4.4 Sediment & Geomorphic Items
- Sediment cores  
- Grain-size spectra  
- Sediment volume curves  
- Delta/forebay extents  

---

## ✔ 4.5 Downstream Effects
- Tailwater DO & turbidity  
- Transport distances during storms  
- Warm-season biological impacts  

---

## ✔ 4.6 Ecological Observations
- Mussel bed polygons  
- Fish community surveys  
- Riparian vegetation mapping  

---

# 📐 5. Asset Standards (COG, CSVW, GeoJSON, NetCDF)

### ✔ Raster Assets (COG)
Used for:
- Bathymetry  
- DoD  
- Sediment surfaces  

Required metadata:
- `proj:epsg`  
- `proj:shape`  
- `proj:transform`  
- `checksum:sha256`  

### ✔ Vector Assets (GeoJSON)
Used for:
- Ecology  
- Sediment polygons  
- Inflow/outflow structures  
- Delta edges  

### ✔ Tabular Assets (CSVW)
Used for:
- Timeseries hydrology  
- WQ datasets  

### ✔ NetCDF
Used for:
- Climate forcing  
- Hydrodynamic model outputs  

---

# 🗃️ 6. Example STAC Item (Bathymetry)

```json
{
  "stac_version": "1.0.0",
  "type": "Feature",
  "id": "clinton-bathymetry-2022",
  "collection": "clinton-lake-hydrology",
  "geometry": { "type": "Polygon", "coordinates": [...] },
  "bbox": [-95.47, 38.86, -95.27, 38.99],
  "properties": {
    "datetime": "2022-07-15T00:00:00Z",
    "kfm:parameter": "bathymetry",
    "kfm:units": "meters",
    "kfm:provider": "USACE Kansas City District",
    "kfm:method": "multibeam",
    "kfm:lineage": "etl/clinton-bathy-2022-v2",
    "kfm:quality": "A",
    "kfm:hydro_region": "Clinton_Reservoir"
  },
  "assets": {
    "dem": {
      "href": "https://example.org/clinton/bathymetry_2022.tif",
      "type": "image/tiff; application=geotiff; profile=cloud-optimized",
      "roles": ["data"],
      "checksum:sha256": "..."
    }
  }
}
```

---

# 🧬 7. DCAT + PROV-O + CIDOC-CRM Crosswalk

### ✔ DCAT Mapping
| STAC | DCAT |
|------|------|
| `id` | `dct:identifier` |
| `assets[].href` | `dcat:downloadURL` |
| `description` | `dct:description` |
| `extent.spatial` | `dct:spatial` |
| `extent.temporal` | `dct:temporal` |

---

### ✔ PROV-O Mapping
- `prov:Entity` → the dataset  
- `prov:Activity` → ETL pipeline  
- `prov:Agent` → data provider  
- `prov:wasGeneratedBy` → ETL process  
- `prov:used` → raw source  

---

### ✔ CIDOC-CRM Mapping
- `E73 InformationObject` → STAC Item  
- `E53 Place` → geometry entity  
- `E7 Activity` → hydrologic events (e.g., sediment surveys)  
- `E3 ConditionState` → reservoir bed state  

---

# 🛰️ 8. ETL → STAC → Graph Integration

Pipeline:

```
Raw Dataset
    ↓ extract
Schema normalization
    ↓ transform
Raster/vector/table generation
    ↓ asset-create
STAC Item creation
    ↓ stac-validate
Graph loader (Neo4j)
```

All ETL runs must be documented in `mcp/experiments/hydrology/clinton/*`.

---

# 🎯 9. Focus Mode v3 Integration

Focus Mode v3 uses STAC Items for:

- Bathymetry overlays  
- Sedimentation timelines  
- Turbidity/DO charts  
- Delta/forebay changes  
- Ecological impact summaries  
- Flood history timelines  

Selecting **“Clinton Lake”** unlocks structured displays for:

- Long-term storage loss  
- Water quality monitoring  
- Habitat condition summaries  
- Inflow/outflow hydrodynamics  

---

# 📖 10. Story Node Integration

Clinton datasets support Story Nodes such as:

- **“The Hydrologic Life of Clinton Lake”**  
- **“Storage Loss and Sediment Trends Through Time”**  
- **“Downstream of Clinton: A Changing River Corridor”**  

Nodes reference datasets via:

```json
{
  "rel": "uses-dataset",
  "target": "clinton-bathymetry-2010"
}
```

---

# 🚀 11. Expansion Roadmap

Future Clinton Lake STAC Items:

- 2025–2030 annual bathymetry  
- UAV-based photobathymetry  
- Sediment fingerprinting datasets  
- High-frequency WQ sensor network  
- Hydrodynamic model outputs (NetCDF)  
- Watershed sediment attribution grids  

---

# 🕰 Version History

- **v11.0.0 (2025-11-21):** Initial creation of Clinton Lake hydrology STAC Collection (super-edition).

---

[⬅ Back to Hydrology STAC Domain](../README.md) • [📂 Data Home](../../../README.md) • [🏠 KFM Master Guide](../../../../docs/reference/kfm_v11_master_documentation.md)

