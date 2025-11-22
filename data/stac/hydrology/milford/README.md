---
title: "🌊 Kansas Frontier Matrix — Milford Lake Hydrology STAC Collection (v11 Super-Edition)"
path: "data/stac/hydrology/milford/README.md"
version: "v11.0.0"
last_updated: "2025-11-21"
review_cycle: "Annual • Hydrology & Reservoir Systems Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/data-stac-hydro-milford-index-v1.json"
governance_ref: "../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active • Enforced"
doc_kind: "STAC Collection Index"
intent: "stac-hydrology-milford-index"
semantic_document_id: "kfm-stac-hydrology-milford-index"
doc_uuid: "urn:kfm:stac:hydrology:milford:index:v11.0.0"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
fair_category: "F1-A1-I1-R1"
care_label: "Public-Low-Risk"
immutability_status: "version-pinned"
---

<div align="center">

# 🌊 **Milford Lake Hydrology STAC Collection (v11 Super-Edition)**  
`data/stac/hydrology/milford/README.md`

**Purpose:**  
Serve as the **authoritative STAC documentation hub** for all Milford Lake hydrological,  
bathymetric, sedimentation, WQ, ecological, flood, hydroclimate, and system-interaction datasets  
within the Kansas Frontier Matrix.  
Defines metadata, asset schemas, lineage structures, ontology integration, and Focus Mode v3  
linkages for all Milford STAC Items and Collections.

</div>

---

# 📘 0. Reservoir Overview

**Milford Lake**, completed in 1967, is the **largest reservoir in Kansas**. It is the **first control point** in a  
multi-reservoir chain:

```
Milford → Tuttle Creek → Perry → Clinton → Kansas River → Missouri River
```

Milford influences:

- Big Blue River inflow patterns into Tuttle Creek  
- Flood control and drought augmentation  
- Nutrient & sediment export  
- Downstream ecological conditions  
- Regional hydrology and hydroclimate feedbacks  

This STAC Collection captures **all spatiotemporal assets** describing that behavior.

---

# 🗂️ 1. Directory Layout

```text
data/
└── stac/
    └── hydrology/
        └── milford/
            ├── collection.json
            └── items/
                ├── bathymetry-1970.json
                ├── bathymetry-1990.json
                ├── bathymetry-2010.json
                ├── bathymetry-2023.json
                ├── hydrology-inflows.json
                ├── hydrology-outflows.json
                ├── wq-turbidity.json
                ├── wq-do.json
                ├── wq-nutrients.json
                ├── sediment-cores.json
                ├── sediment-volumes.json
                ├── delta-migration.json
                ├── downstream-effects.json
                ├── ecological-corridors.json
                ├── fish-assemblages.json
                ├── macroinv-surveys.json
                ├── riparian-zones.json
                ├── hydroclimate.json
                └── flood-history.json
```

Identical structure to Tuttle Creek, Clinton, Perry, and Kansas River STAC domains.

---

# 🌍 2. Spatial & Temporal Extents

### Spatial bbox  
```
[-96.99, 39.03, -96.73, 39.22]
```

### Temporal extent  
```
1967-01-01T00:00:00Z → present
```

---

# 🌊 3. Milford Dataset Themes

## ✔ 3.1 Bathymetry / DoD  
- Historic surveys (1970, 1990, 2010, 2023)  
- DEM rasters  
- DoD rasters showing sediment accumulation  

## ✔ 3.2 Hydrology  
- Inflow from Republican River & tributaries  
- Dam releases  
- Reservoir stage/storage curves  
- Hydrodynamic signatures  

## ✔ 3.3 Water Quality  
- Turbidity  
- DO  
- Nutrients  
- Stratification profiles  

## ✔ 3.4 Sedimentation  
- Sediment cores (grain-size, deposition rate)  
- Sediment volume curves  
- Delta migration  

## ✔ 3.5 Downstream Effects  
- Big Blue River tailwater DO & turbidity  
- Nutrient fluxes  
- Sediment pulses  

## ✔ 3.6 Ecology  
- Mussel communities  
- Fish assemblages  
- Macroinvertebrate scores  
- Riparian vegetation  

## ✔ 3.7 Flood & Hydroclimate  
- Flood hydrographs  
- Mesonet precipitation  
- NOAA COOP climate normals  
- Drought index (SPI/PDSI)

---

# 📐 4. Required STAC Metadata (Milford Hydrology Profile)

Each Milford STAC Item must include both **core STAC 1.0.0** fields and the **KFM hydrology extensions**.

### Core fields
```
stac_version
type = "Feature"
id
collection = "milford-lake-hydrology"
geometry
bbox
properties.datetime
assets
```

### Hydrology-specific (`kfm:*`) fields

| Field | Description |
|--------|-------------|
| `kfm:parameter` | bathymetry, inflow, DO, turbidity, etc. |
| `kfm:units` | SI or domain units |
| `kfm:provider` | USACE, USGS, KDHE, KWO |
| `kfm:method` | multibeam, gauge, lab, model |
| `kfm:site` | station ID / transect ID |
| `kfm:lineage` | ETL → STAC provenance |
| `kfm:quality` | QA tier |
| `kfm:hydro_region` | `Milford_Reservoir`, `Big_Blue_Tailwater`, etc. |
| `kfm:project` | Hydrology-Core, Sedimentation-History, Ecology-202X |

Recommended fields:
- `kfm:dominant_species`  
- `kfm:habitat_type`  
- `kfm:crs`  
- `kfm:processing_history`  

---

# 🧭 5. Asset Schema Requirements

## ✔ Raster Assets (COG)
Used for bathymetry, DoD, sediment surfaces, inundation.
Must include:
- `proj:epsg` or `proj:wkt2`
- tiling + overviews  
- `checksum:sha256`  
- `roles: ["data"]`

## ✔ GeoJSON
Used for:
- habitat polygons  
- transects  
- riparian zones  

## ✔ CSVW / CSV
Used for:
- inflow/outflow hydrographs  
- WQ time-series  
- sediment measurements  
- ecological survey outputs  

## ✔ NetCDF
Used for:
- climate/interpolation datasets  
- hydrodynamic modeling outputs  

## ✔ MP4
Used for:
- drone surveys  
- underwater habitat scans  

---

# 🧪 6. Example STAC Items

## 6.1 Bathymetry DEM (2023)

```json
{
  "stac_version": "1.0.0",
  "type": "Feature",
  "id": "milford-bathymetry-2023",
  "collection": "milford-lake-hydrology",
  "geometry": { "type": "Polygon", "coordinates": [...] },
  "bbox": [-96.99, 39.03, -96.73, 39.22],
  "properties": {
    "datetime": "2023-08-14T00:00:00Z",
    "kfm:parameter": "bathymetry",
    "kfm:units": "meters",
    "kfm:provider": "USACE Kansas City District",
    "kfm:method": "multibeam",
    "kfm:lineage": "etl/milford_bathy2023_v1",
    "kfm:quality": "A",
    "kfm:hydro_region": "Milford_Reservoir",
    "kfm:project": "Sedimentation-History"
  },
  "assets": {
    "cog": {
      "href": "https://example.org/milford/bathy_2023.tif",
      "type": "image/tiff; application=geotiff; profile=cloud-optimized",
      "roles": ["data"],
      "checksum:sha256": "..."
    }
  }
}
```

---

## 6.2 Hydrology Time-Series (Inflow)

```json
{
  "stac_version": "1.0.0",
  "type": "Feature",
  "id": "milford-inflow-2024",
  "collection": "milford-lake-hydrology",
  "geometry": { "type": "Point", "coordinates": [-97.02, 39.05] },
  "bbox": [-97.03, 39.04, -97.01, 39.06],
  "properties": {
    "datetime": "2024-01-01T00:00:00Z",
    "kfm:parameter": "inflow",
    "kfm:units": "cfs",
    "kfm:provider": "USGS",
    "kfm:method": "stream_gauge",
    "kfm:lineage": "etl/milford_inflows2024_v1",
    "kfm:quality": "A",
    "kfm:hydro_region": "Milford_Reservoir",
    "kfm:project": "Hydrology-Core"
  },
  "assets": {
    "csv": {
      "href": "https://example.org/milford/inflows_2024.csv",
      "type": "text/csv",
      "roles": ["data"]
    }
  }
}
```

---

# 🧬 7. Ontology Mapping (CIDOC-CRM + GeoSPARQL + OWL-Time)

## CIDOC-CRM Entities
- `E73 InformationObject` (bathymetry, inflows, WQ datasets)  
- `E53 Place` (Milford Reservoir polygon, tailwater reaches)  
- `E7 Activity` (hydrologic events, surveys)  
- `E3 ConditionState` (sedimentation states, ecological conditions)  
- `E39 Actor` (USACE, USGS, KDHE, KFM)

## CRM Properties
- `P7_took_place_at`  
- `P70_documents`  
- `P1_is_identified_by`  

## GeoSPARQL
- `geo:hasGeometry`  
- `geo:sfWithin`  
- `geo:asWKT`  

## OWL-Time
- `time:hasTime`  
- `time:hasBeginning`  
- `time:hasEnd`

---

# 🔬 8. DCAT 3.0 & PROV-O Mapping

## DCAT
| STAC | DCAT |
|-------|-------|
| `id` | `dct:identifier` |
| `description` | `dct:description` |
| `extent.spatial` | `dct:spatial` |
| `extent.temporal` | `dct:temporal` |
| `assets[].href` | `dcat:downloadURL` |

## PROV-O
- `prov:Entity` → STAC Item  
- `prov:Activity` → ETL process  
- `prov:Agent` → USACE/USGS/KDHE  
- Links: `prov:wasGeneratedBy`, `prov:used`, `prov:wasAttributedTo`  

---

# 🛰️ 9. ETL → STAC → Graph Ingestion Pipeline

```
Raw Data
  ↓ extract
Schema harmonization & QA
  ↓ transform
Asset Production (COG / CSVW / GeoJSON / NetCDF)
  ↓ annotate-stac
STAC Item JSON creation
  ↓ stac-validate
Graph ingestion (Neo4j)
  ↓
Focus Mode v3 + Story Node v3 integration
```

All ETL runs must be logged under:

```
mcp/experiments/hydrology/milford/
```

---

# 🎯 10. Focus Mode v3 Integration

Focus Mode retrieves Milford datasets by:

- `place = Milford_Reservoir`  
- `kfm:hydro_region = Milford_Reservoir`  
- Parameter filters: `bathymetry`, `inflow`, `DO`, `turbidity`, `sediment`, etc.  
- Time-window slicing for sediment history, flood events, etc.

Examples of Focus panels:

- **Bathymetry evolution (1970–2023)**  
- **Inflow/outflow comparative curves**  
- **Water quality anomalies**  
- **Tailwater DO & turbidity wave propagation**  

---

# 📖 11. Story Node Integration

Milford Lake supports numerous hydrology-centered Story Nodes:

- **“Milford: The Headwaters Gatekeeper”**  
- **“Sediment Movements from Milford to Tuttle Creek”**  
- **“Flood Operations: Protecting the Kansas River Basin”**  
- **“Ecology in the Milford System”**

Items referenced through:

```json
{
  "rel": "uses-dataset",
  "target": "milford-bathymetry-2023"
}
```

---

# 🚀 12. Expansion Roadmap

Future Milford STAC Items (2026–2032):

- Photobathymetry (UAS)  
- Sediment fingerprinting datasets  
- Machine-learning hydrologic anomaly rasters  
- Ecological multi-year monitoring  
- 2D/3D model results (NetCDF)  
- Multi-reservoir sediment routing  
- WID feasibility scenario datasets  

---

# 🕰 Version History

- **v11.0.0 (2025-11-21):** Initial creation of Milford Lake Hydrology STAC Collection (super-edition).

---

[⬅ Back to Hydrology STAC Domain](../README.md) • [📂 Data Home](../../../README.md) • [🏠 KFM Master Guide](../../../../../docs/reference/kfm_v11_master_documentation.md)

