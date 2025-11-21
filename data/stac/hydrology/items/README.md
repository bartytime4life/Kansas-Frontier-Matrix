---
title: "🛰️ Kansas Frontier Matrix — Hydrology STAC Items Index (v11 Super-Edition)"
path: "data/stac/hydrology/items/README.md"
version: "v11.0.0"
last_updated: "2025-11-21"
review_cycle: "Annual / Hydrology & Hazards Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../../schemas/data-stac-hydrology-items-index-v1.json"
governance_ref: "../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v11.0.0"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active / Enforced"
doc_kind: "STAC Items Index"
intent: "stac-hydrology-items-domain-index"
semantic_document_id: "kfm-stac-hydrology-items-domain-index"
doc_uuid: "urn:kfm:stac:hydrology:items:index:v11.0.0"
machine_extractable: true
accessibility_compliance: "W3C-WCAG-2.1-AA"
fair_category: "F1-A1-I1-R1"
care_label: "Public / Low-Risk"
immutability_status: "version-pinned"
---

<div align="center">

# 🛰️ **Hydrology STAC Items Index — Kansas Frontier Matrix (Domain-Level)**  
`data/stac/hydrology/items/README.md`

**Purpose:**  
Serve as the **canonical domain-level index and specification** for all hydrology-related STAC  
Items in the Kansas Frontier Matrix, spanning all reservoirs, rivers, hydroclimatic datasets,  
sedimentation products, WID (Water Injection Dredging) experiments, bathymetry, and  
downstream ecological observations. This document defines Item-level metadata, naming,  
asset standards, lineage, and ontology integration for KFM v11.

</div>

---

# 📘 0. Overview

The **Hydrology STAC Items domain** is the **atomic metadata layer** for all hydrology-related datasets  
in KFM. Each STAC Item in `data/stac/hydrology/**/items/` describes:

- A **single dataset instance**: a time-series, raster, vector survey, or media artifact  
- Its **spatial footprint** (Point/Line/Polygon/Extent)  
- Its **temporal coverage** (instant or interval)  
- Its **assets** (COG, CSVW, GeoJSON, NetCDF, MP4, etc.)  
- Its **provenance and processing history**  
- Its **hydrologic and ecological semantics** via `kfm:*` fields  

This index provides:

- A **domain-wide view** of hydrology STAC Items  
- **Standard naming conventions and metadata expectations**  
- **Crosswalks** to DCAT, PROV-O, CIDOC-CRM, and GeoSPARQL  
- Guidance for **ETL → STAC → Graph** ingestion and Focus Mode v3 integration  

---

# 🗂️ 1. Directory Layout (Domain-Level Items)

At the domain level, STAC Items are physically stored under their respective Collections, but this  
directory serves as a **logical index** and may host:

- **Global hydrology Items** not tied to a single Collection  
- **Cross-cutting Items** (e.g., statewide summaries, multi-reservoir composites)  
- **Symlinks or references** to Items in reservoir-/basin-level `items/` folders  

Canonical structure:

```text
data/
└── stac/
    └── hydrology/
        ├── collection.json              # (optional hydrology-wide collection)
        ├── items/                       # this directory (domain-wide Items / index)
        │   ├── hydrology-statewide-timeseries.json
        │   ├── flood-events-kansas.json
        │   ├── sediment-budget-statewide.json
        │   ├── reservoirs-system-capacity.json
        │   └── ...
        ├── tuttle-creek/
        │   └── items/
        ├── milford/
        │   └── items/
        ├── per/
        │   └── items/
        ├── clinton/
        │   └── items/
        ├── kansas-river/
        │   └── items/
        └── ...                         # additional basin/reservoir folders
```

Per-Collection Items have their own `README.md` (e.g.  
`data/stac/hydrology/tuttle-creek/items/README.md`). This domain-level README catalogs Item  
classes and cross-collection conventions.

---

# 🧾 2. Item Naming Conventions

Hydrology STAC Item `id` values must be:

- **Globally unique** within the hydrology domain  
- **Deterministic** (stable across ETL runs)  
- **Slug-safe** (no spaces; use `-` or `_`)  

### 2.1 Recommended ID Pattern

```text
<site-or-area>-<theme>-<parameter>-<time_range>-<version>

Examples:
- tuttle-creek-bathymetry-2019-v1
- big-blue-inflow-2020-2025-v1
- kansas-river-flood-1993-hydrograph
- wid-2025-turbidity-b1-15min-v1
- tc-downstream-do-2025-09-22-v1
```

`id` is mapped to CIDOC `E42 Identifier` and DCAT `dct:identifier`.

---

# 🛰️ 3. Hydrology STAC Item Classes (Domain-Wide)

Hydrology Items across all Collections share a common conceptual taxonomy:

## 3.1 Hydrologic Time-Series Items

Represent continuous or event-based time-series:

- **Inflow/Outflow** (USGS NWIS, USACE)  
- **Stage & Storage**  
- **Precipitation / Temperature / Snowpack / Soil moisture**  
- **Hydraulic parameters** (velocity, discharge, water surface elevation)

Typical assets: `text/csv` or `application/x-netcdf` (CF-compliant).

---

## 3.2 Bathymetry & Morphology Items

- **Bathymetry DEMs** (COG)  
- **Difference of DEMs (DoD)** for sediment volume changes  
- **Channel cross-sections (GeoJSON/CSV)**  
- **Delta front extents** (Polygon GeoJSON)

---

## 3.3 Sediment & Water-Quality Items

- **Turbidity timeseries**  
- **TSS lab samples**  
- **Sediment core profiles** (depth vs grain-size, radionuclide markers)  
- **Nutrient concentrations** (N, P)  
- **Metals & contaminants**

---

## 3.4 WID (Water Injection Dredging) Items

- **ADCP transects** (LineString geometry + CSV/NetCDF)  
- **Jet operations logs** (CSV)  
- **Plume extent polygons** (GeoJSON)  
- **High-frequency turbidity / DO Items**

---

## 3.5 Downstream Effects & Ecology Items

- **Tailwater & downstream DO, turbidity**  
- **Biological survey datasets** (fish, mussels, macroinvertebrates)  
- **Habitat mapping polygons**  
- **Channel width, depth, slope measurements**

---

## 3.6 Statewide Hydroclimate & Flood Items

- **Statewide runoff indices**  
- **Flood event hydrographs** (Kansas River)  
- **Precipitation frequency grids (e.g., NOAA Atlas)**  
- **Drought severity indices (SPI, PDSI)**  

---

# 📐 4. Required STAC Fields & KFM Hydrology Extensions

Every hydrology STAC Item must satisfy:

## 4.1 Core STAC Fields

```json
{
  "stac_version": "1.0.0",
  "type": "Feature",
  "id": "string",
  "collection": "hydrology-collection-id",
  "geometry": { "type": "Point", "coordinates": [...] },
  "bbox": [...],
  "properties": {
    "datetime": "2025-09-17T00:00:00Z"
  },
  "assets": {
    "asset-key": {
      "href": "https://...",
      "type": "text/csv",
      "roles": ["data"]
    }
  }
}
```

## 4.2 Required `properties` fields (Hydrology Profile)

| Field | Description |
|-------|-------------|
| `datetime` | Representative timestamp or mid-interval |
| `start_datetime` | Start of coverage (for intervals) |
| `end_datetime` | End of coverage (for intervals) |
| `kfm:parameter` | Hydrologic/water-quality parameter name |
| `kfm:units` | Units (ft, m³/s, NTU, mg/L, etc.) |
| `kfm:site` | KFM site identifier (e.g., USGS gauge ID, WID station code) |
| `kfm:provider` | Data provider (USGS, USACE, KDHE, KWO, etc.) |
| `kfm:method` | Sensor type, sampling method, or model name |
| `kfm:project` | Associated project (e.g., “WID-2025”) |
| `kfm:lineage` | ETL pipeline identifier / provenance string |
| `kfm:quality` | QA/QC category (A/B/C, or “provisional”, “final”) |
| `kfm:hydro_region` | e.g., `Big_Blue_Basin`, `Kansas_River`, `Tuttle_Creek_Reservoir` |

---

# 🌍 5. Asset Standards (COG, GeoJSON, CSVW, NetCDF, MP4)

## 5.1 Raster Assets (COG)

- **Format:** `image/tiff; application=geotiff; profile=cloud-optimized`  
- **Use cases:** Bathymetry, DoD, gridded hydrologic variables  
- **Metadata:**

  - `proj:epsg` or `proj:wkt2`  
  - `kfm:dataset_type = "bathymetry" | "dod" | "hydrogrid"`  
  - `kfm:processing_history`  

## 5.2 Vector Assets (GeoJSON)

- **Geometry types:** `Point`, `LineString`, `Polygon`  
- **Properties include:** `parameter`, `value`, `units`, `site_id`, `survey_date`  

## 5.3 Tabular Assets (CSV / CSVW)

- Must include: `timestamp`, `value`, `units`, `parameter`, `site_id`, `qc_flag`  
- Optional: `min_value`, `max_value`, `std_dev`, `sample_method`  

## 5.4 NetCDF Assets

- CF-compliant with `time`, `lat`, `lon` dimensions  
- Suitable for climate and hydrodynamic models  

## 5.5 Media Assets (Optional)

- `video/mp4` for ADCP plume or drone flyover videos  
- Linked as `roles: ["overview", "thumbnail", "visual"]`  

---

# 🧬 6. DCAT, PROV-O, and CIDOC-CRM Crosswalk (Per Item)

Each STAC Item should be convertible into:

- A **DCAT Dataset & Distribution**  
- A **CIDOC-CRM Information Object (E73)**  
- A set of **Observation** entities (e.g., `ObservationSeries`)  
- A **PROV-O** graph linking ETL processes and Agents  

### 6.1 Example Cross-Entity Mapping (Conceptual)

```text
STAC Item (id=tuttle-creek-wid-2025-turbidity-b1)
   ↓ E73_Information_Object
   ↓ prov:wasGeneratedBy → etl:Hydro_WID_Turbidity_Import_v1
   ↓ P70i_is_documented_in → Document:USACE_WID_EA_2024
   ↓ P67_refers_to → Event:WID_2025_Phase1
   ↓ P1_is_identified_by → Identifier: "wid-2025-turbidity-b1"
   ↓ hasObservationSeries → ObservationSeries:WID_Turbidity_B1
      → time:hasTime → [2025-09-17T00Z, 2025-09-27T23Z]
      → geo:hasGeometry → Place:Tailwater_Station_B1
```

---

# 🔬 7. ETL → STAC → Graph Ingestion (Domain Rules)

For each dataset:

```text
1. Ingest raw data from source (USGS / USACE / KDHE / etc.).
2. Normalize to schema (CSVW / GeoJSON / COG / NetCDF).
3. Run QA/QC checks (range, flags, completeness).
4. Attach metadata (kfm:*, DCAT fields).
5. Generate STAC Item JSON.
6. Validate against STAC 1.0.0 + hydrology profile.
7. Ingest into Neo4j with CIDOC-CRM/GeoSPARQL mapping.
8. Update Focus Mode caches and Story Node references.
```

All ETL runs must be documented in `mcp/` experiment files with:

- Inputs (raw datasets, version, checksums)  
- Scripts & container images used  
- Outputs (STAC Item IDs, dataset paths)  
- Energy & carbon metrics (per MCP)  

---

# 🎯 8. Focus Mode v3 Integration

Focus Mode uses STAC Items to dynamically populate:

- **Time-series panels** (e.g., tailwater DO, inflows, turbidity)  
- **Map overlays** (bathymetry, plumes, delta extent, habitat polygons)  
- **Contextual metadata** (provenance, methods, quality)  
- **Event-centric views** (e.g., WID 2025, 1993 flood at Tuttle Creek)  

Dataset IDs and `kfm:parameter` fields are critical for:

- **Auto-discovery** based on Place + Time + Parameter  
- **Thematic queries** (e.g., “show all turbidity datasets downstream of Tuttle Creek in 2025”)  

---

# 📖 9. Story Node v3 Dataset Linkage Patterns

Story Nodes reference hydrology STAC Items using the `relations` block:

```json
{
  "id": "story-tuttle-creek-wid-2025-downstream-effects",
  "type": "Feature",
  "properties": {
    "title": "Downstream of the Dam",
    "relations": [
      {
        "rel": "uses-dataset",
        "target": "wid-2025-turbidity-b1"
      },
      {
        "rel": "uses-dataset",
        "target": "downstream-do-2025-09-22"
      }
    ]
  }
}
```

This enables Focus Mode to **jump from narrative** → **underlying data** seamlessly.

---

# ✅ 10. Quality Assurance & Validation

Every hydrology STAC Item must:

- Pass JSON schema validation (STAC 1.0.0 + hydrology extension profile)  
- Include QA/QC results where applicable  
- Include `kfm:quality` classification  
- Be linked to at least one source document or ETL description via `prov:wasDerivedFrom`  

Suggested automation:

- GitHub Actions pipeline to run `stac-validator` on all Items in `data/stac/hydrology/**/items/*.json`  
- A domain-specific Python validator to ensure hydrology-specific `kfm:*` fields  

---

# 🚀 11. Expansion Roadmap for Hydrology STAC Items

Planned additions:

- **Multi-reservoir Items** combining Tuttle, Milford, Perry, Clinton  
- **High-frequency streaming Items** (near real-time sensors)  
- **Model ensemble outputs** for long-term hydrologic forecasts  
- **Flood-inundation polygon Items** for key events (1951, 1993, 2019)  
- **Statewide hydroclimate anomaly grids** as STAC Items (NetCDF/GeoTIFF)  
- **Sediment source-area attribution datasets**  

All new Items must follow this domain profile.

---

# 🕰️ 12. Version History

- **v11.0.0 (2025-11-21):** Initial creation of domain-level Hydrology STAC Items index (super-edition).

---

[⬅️ Back to Hydrology STAC Domain](../README.md) • [⬅️ Back to Hydrology Data Index](../../../hydrology/README.md) • [🏠 KFM v11 Master Guide](../../../../docs/reference/kfm_v11_master_documentation.md)

