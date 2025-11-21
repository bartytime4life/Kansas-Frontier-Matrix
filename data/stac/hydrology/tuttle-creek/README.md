---
title: "🛰️ Kansas Frontier Matrix — STAC Collection Index: Tuttle Creek Hydrology (v11 Super-Edition)"
path: "data/stac/hydrology/tuttle-creek/README.md"
version: "v11.0.0"
last_updated: "2025-11-21"
review_cycle: "Annual / Hydrology & Hazards Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/data-stac-hydrology-tc-index-v1.json"
governance_ref: "../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active / Enforced"
doc_kind: "STAC Index"
intent: "stac-hydrology-tuttle-creek-index"
semantic_document_id: "kfm-stac-hydrology-tuttle-creek-index"
doc_uuid: "urn:kfm:stac:hydrology:tuttle-creek:index:v11.0.0"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
fair_category: "F1-A1-I1-R1"
care_label: "Public / Low-Risk"
immutability_status: "version-pinned"
---

<div align="center">

# 🛰️ **STAC Collection Index — Tuttle Creek Hydrology**  
`data/stac/hydrology/tuttle-creek/README.md`

**Purpose:**  
Provide the **complete STAC (SpatioTemporal Asset Catalog) documentation** for all Tuttle Creek  
hydrology, sedimentation, bathymetry, WID 2025, ecological, and downstream datasets.  
Defines Collection structure, Item templates, metadata fields, provenance, STAC/DCAT/PROV-O  
alignment, ETL lineage, and integration with the KFM v11 knowledge graph and Focus Mode v3.

</div>

---

# 📘 0. Overview

This directory hosts the **authoritative STAC metadata** for all Tuttle Creek–related hydrologic datasets.  
STAC serves as the **machine-readable catalog layer**, enabling:

- Dataset discovery  
- Search by time & space  
- Asset linking (COG, GeoJSON, CSV, NetCDF)  
- FAIR+CARE metadata enforcement  
- Direct ingestion into KFM’s Neo4j knowledge graph  
- Real-time data binding for Focus Mode v3  
- Dataset provenance tracking (PROV-O)  

This README explains how every dataset is cataloged, referenced, validated, and consumed.

---

# 🗂️ 1. Directory Layout (Canonical)

```text
data/
└── stac/
    └── hydrology/
        └── tuttle-creek/
            ├── collection.json
            └── items/
                ├── bathymetry-1962.json
                ├── bathymetry-1993.json
                ├── bathymetry-2010.json
                ├── bathymetry-2024.json
                ├── hydrology-inflows-usgs.json
                ├── hydrology-outflows.json
                ├── wid-2025-turbidity-b1.json
                ├── wid-2025-density-current.json
                ├── sediment-core-locations.json
                ├── sediment-volumes-timeseries.json
                ├── downstream-do.json
                ├── downstream-turbidity.json
                ├── ecology-fish-2025.json
                └── ecology-mussels.json
```

---

# 🛰️ 2. STAC Collection Specification (Tuttle Creek Hydrology)

The root `collection.json` must define:

### ✔ Required Fields
- `stac_version` = "1.0.0" (strict)  
- `type` = "Collection"  
- `id` = "tuttle-creek-hydrology"  
- `description`  
- `license`  
- `extent.spatial` (reservoir polygon or bbox)  
- `extent.temporal` (1962 → present)  
- `providers`  
- `links` (self, parent, items)  

### ✔ Recommended Fields
- `keywords`  
- `summaries`  
- `msft:storage_account` (if cloud-hosted)  
- `kfm:*` extended metadata  
- `dcat:*` crosswalks  
- `prov:*` lineage references  

---

# 🧭 3. Spatial & Temporal Extents

### Spatial extent (bbox)
```
[-96.74, 39.17, -96.51, 39.47]
```

### Temporal extent
```
1962-01-01T00:00:00Z → present
```

These extents MUST be included in the Collection.

---

# 📁 4. Item Categories in This Collection

### 4.1 Hydrology Time-Series
- Inflows (USGS NWIS)  
- Dam releases (USACE)  
- Stage & storage curves  
- Hydroclimate inputs  

### 4.2 Bathymetry DEMs (1962–2024)
- Historical single-beam digitized  
- Multibeam survey rasters  
- Differencing (DoD) rasters  

### 4.3 Sediment Data
- Sediment cores  
- Grain-size spectra  
- Sediment volume estimates  
- Delta position datasets  

### 4.4 WID 2025
- Turbidity sensors (1–5 min)  
- DO sensors  
- ADCP transects  
- Jet-flow operations metadata  
- Density-current plume assets  

### 4.5 Downstream Effects
- Tailwater DO  
- Tailwater turbidity  
- Downstream biotic surveys  
- Plume propagation polygons  

### 4.6 Ecology
- Mussel bed polygons  
- Fish assemblage surveys  
- Macroinvertebrate data  

---

# 🗃️ 5. Required Metadata for All Items

Every STAC Item **must** include:

### ✔ Properties
| Field | Description |
|-------|-------------|
| `datetime` | Timestamp or representative time |
| `start_datetime` | Beginning of coverage |
| `end_datetime` | End of coverage |
| `kfm:parameter` | Hydrologic/water-quality variable |
| `kfm:units` | SI or domain-appropriate units |
| `kfm:provider` | USACE, USGS, KWO, KDHE, etc. |
| `kfm:project` | e.g., “WID-2025”, “Sedimentation-History” |
| `kfm:method` | Sensor type, survey type, algorithm |
| `kfm:lineage` | ETL → STAC provenance |
| `kfm:quality` | QA flags |

### ✔ Assets
Allowed formats:

- **COG** → bathymetry DEM, DoD rasters  
- **GeoJSON** → vector surveys (ecology, geomorphology)  
- **CSV / CSVW** → timeseries  
- **NetCDF** → hydroclimate rasters  
- **MP4** (optional) → ADCP plume videos  

---

# 🛰️ 6. STAC Item Template (Hydrology, Example)

```json
{
  "stac_version": "1.0.0",
  "type": "Feature",
  "id": "tuttle-creek-usgs-inflow-2020",
  "collection": "tuttle-creek-hydrology",
  "geometry": { "type": "Point", "coordinates": [-96.6005, 39.2758] },
  "bbox": [-96.601, 39.275, -96.600, 39.276],
  "properties": {
    "datetime": "2020-01-01T00:00:00Z",
    "kfm:parameter": "inflow",
    "kfm:units": "cfs",
    "kfm:provider": "USGS NWIS",
    "kfm:lineage": "etl/usgs_nwis_ingest_v4",
    "kfm:project": "hydrology-core"
  },
  "assets": {
    "timeseries": {
      "href": "https://example.org/tc/inflow_2020.csv",
      "type": "text/csv",
      "roles": ["data"]
    }
  }
}
```

---

# 🌫️ 7. STAC Item Template (WID Density-Current ADCP)

```json
{
  "stac_version": "1.0.0",
  "type": "Feature",
  "id": "wid2025-density-current-adcp-transect-03",
  "collection": "tuttle-creek-hydrology",
  "geometry": { "type": "LineString", "coordinates": [...] },
  "properties": {
    "datetime": "2025-09-22T17:00:00Z",
    "kfm:parameter": "density-current-velocity",
    "kfm:units": "m/s",
    "kfm:method": "ADCP",
    "kfm:provider": "USACE Kansas City District",
    "kfm:project": "WID-2025",
    "kfm:lineage": "etl/wid-adcp-v2"
  },
  "assets": {
    "adcp_raw": {
      "href": "https://example.org/wid/adcp/transect03.bin",
      "type": "application/octet-stream",
      "roles": ["data"]
    },
    "adcp_processed": {
      "href": "https://example.org/wid/adcp/transect03.csv",
      "type": "text/csv",
      "roles": ["derived"]
    }
  }
}
```

---

# 🧬 8. DCAT 3.0 Crosswalk

Required mappings:

| STAC Field | DCAT Equivalent |
|------------|------------------|
| `id` | `dct:identifier` |
| `assets[].href` | `dcat:downloadURL` |
| `license` | `dct:license` |
| `extent.spatial` | `dct:spatial` |
| `extent.temporal` | `dct:temporal` |
| `keywords` | `dcat:keyword` |

---

# 🕸️ 9. Ontology Integration (CIDOC-CRM + GeoSPARQL + OWL-Time)

### Entities Created Per STAC Item
- `E73 InformationObject` — dataset  
- `ObservationSeries` — if time-series  
- `E53 Place` — from geometry  
- `E7 Activity` — if dataset represents an event  
- `E3 ConditionState` — states of reservoir or river corridor  

### Relationships
- `P7_took_place_at` → geometry  
- `geo:hasGeometry` → spatial object  
- `time:hasTime` → datetime / interval  
- `prov:wasGeneratedBy` → ETL process  
- `P70_documents` → source documents  

---

# 🧪 10. ETL → STAC → Graph Ingestion Rules

Pipeline:

```
Raw Dataset
    ↓  (extract)
Normalize & QA
    ↓  (transform)
Processed Dataset
    ↓  (stac-create)
STAC Item
    ↓  (graph-load)
Neo4j Entity + Relationships
```

All STAC creation steps recorded in:

`mcp/experiments/hydrology/stac_creation_<id>.md`

---

# 🎯 11. Focus Mode v3 Integration

Focus Mode uses STAC metadata to:

- Load time-series plots  
- Highlight plume extents  
- Render bathymetry overlays  
- Summarize dataset provenance  
- Dynamically attach datasets to Story Nodes  
- Auto-create event-context panels for WID 2025  

---

# 📖 12. Story Node v3 Integration

Story Nodes link to STAC Items using:

```json
{
  "rel": "uses-dataset",
  "target": "tuttle-creek-bathymetry-2010"
}
```

Downstream nodes (e.g., *“Downstream of the Dam”*) require:

- tailwater DO  
- tailwater turbidity  
- plume polygons  
- biological surveys  

---

# 🚀 13. Expansion Roadmap

Future STAC additions:

- 2D/3D hydrodynamic model outputs (HEC-RAS, Delft3D)  
- CMIP6 hydroclimate-downscaled rasters (NetCDF)  
- High-frequency streaming sensors (MQTT → STAC)  
- Sentinel-2 water-quality rasters  
- Automated bathymetry differencing pipeline  
- Multi-decade sediment core archive (as STAC Items)  

---

# 🕰 Version History

- **v11.0.0 (2025-11-21):** Initial creation of Tuttle Creek hydrology STAC super-index.

---

[⬅️ Back to Hydrology Datasets](../../../hydrology/README.md) • [🏠 KFM v11 Master Guide](../../../../../docs/reference/kfm_v11_master_documentation.md)

