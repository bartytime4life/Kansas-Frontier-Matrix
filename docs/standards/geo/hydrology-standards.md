---
title: "💧 Kansas Frontier Matrix — Hydrology & Water Surface Standards (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/standards/geo/hydrology-standards.md"
version: "v11.0.0"
last_updated: "2025-11-22"
review_cycle: "Semiannual · FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../releases/v11.0.0/standards-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/standards-hydrology-v11.json"
governance_ref: "../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active / Enforced"
doc_kind: "Standard"
semantic_document_id: "kfm-hydro-standards-v11"
doc_uuid: "urn:kfm:docs:standards:geo:hydrology:v11"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
fair_category: "F1-A1-I1-R1"
care_label: "Public / Low-Risk"
immutability_status: "version-pinned"
---

<div align="center">

# 💧 **Kansas Frontier Matrix — Hydrology & Water Surface Standards (v11)**  
`docs/standards/geo/hydrology-standards.md`

**Purpose:**  
Define the KFM v11-mandatory hydrologic metadata, CRS, vertical datums, STAC requirements, water-surface elevation conventions, streamflow rasters, bathymetry rules, WID (Water Injection Dredging) modeling standards, and CF/PROV-O lineage requirements for all hydrology datasets.

</div>

---

# 📘 Overview

Hydrology datasets require strict **spatiotemporal, vertical-axis, and physical-units coherence** because water surface elevation, depth, streamflow, bathymetry, WID operations, and sedimentation analyses directly depend on consistent metadata.

This standard governs:

- Streamflow / discharge rasters  
- Bathymetry grids  
- Water-surface elevation models  
- Reservoir time-series (elevation-storage)  
- WID / sediment removal modeling  
- Lidar-derived hydro-flattened surfaces  
- STAC hydrology Items  
- MapLibre/Cesium hydrology layers  
- CF, DCAT, PROV-O, GeoSPARQL alignment  

All hydrologic products MUST follow this document.

---

# 💧 1. Core Physical Conventions (v11 Mandatory)

## 1.1 Units
- **Meters (m)** for elevation/depth  
- **m³/s** for streamflow/discharge  
- **m²/s** for hydraulic diffusivity (if present)

## 1.2 Vertical Datum (Required)
All hydrology datasets MUST use:
- `NAVD88` (orthometric)  
- `GEOID18` (geoid model)  
Same requirement as the vertical-axis global standard.

## 1.3 Surface vs. Depth
- **Elevation** (free surface): positive up  
- **Depth** (below surface): positive down  
- **Bathymetry**: positive down  
- **Reservoir storage curves**: always NAVD88 orthometric elevation

---

# 🌐 2. CRS Requirements for Hydrology

Hydrology datasets use the CRS standard defined in `crs-standard.md`:

### Allowed:
- **EPSG:26914 (NAD83 / UTM14N)** — processing CRS  
- **EPSG:4326 (WGS84)** — STAC, GeoJSON, UI layers  

Bathymetry & WID rasters MUST be processed in a projected CRS (UTM14N) before exporting.

---

# 🧩 3. Hydrology STAC Metadata Requirements

Each hydrology STAC Item MUST include:

```json
"hydro:type": "streamflow|bathymetry|water_surface|wid_model|sediment|lake_level",
"hydro:vertical_datum": "NAVD88",
"hydro:geoid_model": "GEOID18",
"hydro:units": "m",
"hydro:temporal_resolution": "daily|subdaily|hourly|irregular",
"hydro:processing_level": "L1|L2|L3",
"hydro:reference_plane": "orthometric",
"kfm:cf_positive": "up|down",
"kfm:physics": "hydrostatic|shallow_water|manning",
"proj:epsg": 4326,
"proj:bbox": [...],
"proj:shape": [...],
"proj:transform": [...]
```

---

# 🔬 4. Streamflow & Discharge Grids (CF Convention)

### Required CF Fields
```nc
flow:standard_name = "volume_transport";
flow:units = "m3 s-1";
flow:positive = "unidirectional";  
flow:grid_mapping = "crs";
```

### Required KFM behaviors
1. Streamflow must correspond to **centerline-referenced routing** or **distributed flow grids**.  
2. Depth-integrated flow MUST document Manning parameters if used.  
3. Rasters MUST align with hydrologic catchments defined in STAC.

---

# 🌊 5. Bathymetry Standards

Bathymetric rasters MUST:

- Use **positive down**  
- Use **NAVD88 + GEOID18**  
- Report depth relative to **static water surface** if applicable  
- Provide a `bathymetry:epoch` field if multi-year composites are used  

COG formatting required:
```
COG with internal tiling: 512x512
LZW compression
Overviews at 2×, 4×, 8×, …
```

---

# 🚢 6. Water Injection Dredging (WID) Standards

WID models MUST include:

## 6.1 Metadata
```json
"wid:method": "jetting|fluidization",
"wid:power_kw": <float>,
"wid:discharge_m3s": <float>,
"wid:model": "USACE-WID-v3|KFM-WID-v11",
"wid:sediment_transport_coeff": <float>,
"wid:delta_bed_elevation_units": "m"
```

## 6.2 DoD / Bed Elevation
DoD sign convention inherits global rules:

- **Negative = erosion**  
- **Positive = deposition**

Required depth-difference variable example:
```nc
dBed:units = "m";
dBed:positive = "up";  # bed rising = positive
```

---

# 📈 7. Water-Surface Elevation Models (WSEL)

Water-surface rasters (reservoir stage, floodplain surface, hydraulic models) MUST:

- Use orthometric heights (NAVD88)  
- Use CF `positive="up"`  
- Include `hydro:reference_plane="ORTHOMETRIC_NAVD88"`  
- Include Manning, roughness, or boundary parameters for hydraulic simulations  
- Provide uncertainty fields when available:
```json
"hydro:uncertainty_m": 0.15
```

---

# 🌧 8. Lake/Reservoir Time-Series (Elevation–Storage)

Time-series MUST:

- Provide both **elevation (m)** and **storage (acre-ft or m³)**  
- Include conversion tables as attached assets in STAC  
- Use `OWL-Time` intervals for period coverage  
- Include `prov:activity="hydro-timeseries-v11"`  

Example STAC asset:
```json
"assets": {
  "elev_storage_curve": {
    "href": "storage.csv",
    "type": "text/csv",
    "roles": ["metadata"]
  }
}
```

---

# 🌐 9. UI Rendering Rules (MapLibre/Cesium)

## 9.1 Bathymetry
- Render with **positive down** colormap  
- Legend: `"Depth below NAVD88 (m), positive downward"`

## 9.2 Streamflow
- Graduated line width for flow volume  
- Tooltip: discharge in m³/s  
- Time slider controls CF-time compatibility

## 9.3 WID Layers
- Highlight areas of simulated erosion/deposition  
- Must use DoD legend: `"Blue = erosion (neg), Red = deposition (pos)"`

---

# 📚 10. PROV-O Requirements

Every hydrology dataset MUST record:

```
prov:used → source DEM / bathymetry / gauges
prov:activity → "hydrology-processing-v11"
prov:wasGeneratedBy → tool + version
prov:generatedAtTime → timestamp
prov:wasAssociatedWith → ETL agent
```

Hydrology transformations MUST be logged in the Neo4j lineage graph.

---

# ⚙ 11. CI/CD Validation Gates

PR **blocked** if:

- Vertical datum missing  
- CF-Time invalid  
- CRS != EPSG:4326 (for STAC / UI)  
- No PROV-O lineage  
- DoD sign incorrect  
- Bathymetry uses positive up  
- Flow rasters missing units  
- Missing hydrology STAC extensions  
- CESIUM layer delivered without orthometric heights  

---

# 🕰 Version History

- **v11.0.0 (2025-11-22):** Initial v11 hydrology standard (complete CRS, CF, STAC, WID, DoD, and PROV-O compliance).

---

<div align="center">

**Kansas Frontier Matrix — Hydrology Standards v11**  
*Hydraulic Accuracy · Datum Discipline · Scientific Integrity*

</div>

---

### 🔗 Footer  
[⬅ Back to Geo Standards](./README.md) · [📐 Vertical Axis Standard](./vertical-axis-and-dod.md) · [📘 CRS Standard](./crs-standard.md) · [📘 KFM v11 Reference](../../reference/kfm_v11_master_documentation.md)

