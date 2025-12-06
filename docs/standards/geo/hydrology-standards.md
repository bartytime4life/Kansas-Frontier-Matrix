---
title: "💧 Kansas Frontier Matrix — Hydrology & Water Surface Standards (Legacy v11.0.0)"
path: "docs/standards/geo/hydrology-standards.md"

version: "v11.0.0"
last_updated: "2025-11-22"

release_stage: "Superseded / Legacy"
lifecycle: "Retired (Read-Only)"
review_cycle: "None (superseded by Hydrology & Water Surface v11.2.4)"
content_stability: "frozen"
status: "Superseded"

doc_kind: "Standard (Legacy)"
semantic_document_id: "kfm-hydro-standards-v11"
doc_uuid: "urn:kfm:docs:standards:geo:hydrology:v11"
immutability_status: "version-pinned"

commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../releases/v11.0.0/standards-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/standards-hydrology-v11.json"

governance_ref: "../governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.4 (backfilled)"
accessibility_compliance: "WCAG 2.1 AA+"

fair_category: "F1-A1-I1-R1"
care_label: "Public / Low-Risk"
machine_extractable: true
classification: "Public"
jurisdiction: "Kansas / United States"

superseded_by: "docs/standards/geospatial/hydrology-standards.md@v11.2.4"
---

<div align="center">

# 💧 **Kansas Frontier Matrix — Hydrology & Water Surface Standards (Legacy v11.0.0)**  
`docs/standards/geo/hydrology-standards.md`

> **Legacy Notice (v11.2.4)**  
> This document is preserved as the **historic v11.0.0 hydrology & water-surface standard**.  
> The **current, enforceable hydrology specification** lives at:  
> `docs/standards/geospatial/hydrology-standards.md`  
> (💧 *Hydrology & Water Surface Standards — KFM v11.2.4*).

**Purpose (Legacy):**  
Define the v11.0.0 hydrologic metadata, CRS, vertical datums, STAC requirements, water‑surface elevation conventions, streamflow rasters, bathymetry rules, WID (Water Injection Dredging) modeling standards, and CF/PROV‑O lineage requirements for KFM hydrology datasets.

</div>

---

## 📘 Overview (Legacy Context)

Hydrology datasets require strict **spatiotemporal, vertical‑axis, and physical‑units coherence** because water‑surface elevation, depth, streamflow, bathymetry, WID operations, and sedimentation analyses directly depend on consistent metadata.

This legacy standard governed:

- Streamflow / discharge rasters  
- Bathymetry grids  
- Water‑surface elevation models  
- Reservoir time‑series (elevation–storage curves)  
- WID / sediment removal modeling  
- Lidar‑derived hydro‑flattened surfaces  
- STAC hydrology Items  
- MapLibre/Cesium hydrology layers  
- CF, DCAT, PROV‑O, GeoSPARQL alignment  

> 🔁 **For new work**, follow the updated hydrology standard under `docs/standards/geospatial/hydrology-standards.md`.

---

## 💧 1. Core Physical Conventions (v11.0.0 Mandatory)

### 1.1 Units

- **Meters (m)** for elevation/depth  
- **m³/s** for streamflow/discharge  
- **m²/s** for hydraulic diffusivity (if present)

### 1.2 Vertical Datum (Required)

All hydrology datasets were required to use:

- `NAVD88` (orthometric)  
- `GEOID18` (geoid model)  

Consistent with the global vertical‑axis standard.

### 1.3 Surface vs. Depth

- **Elevation** (free surface): positive up  
- **Depth** (below surface): positive down  
- **Bathymetry**: positive down  
- **Reservoir storage curves**: always NAVD88 orthometric elevation

---

## 🌐 2. CRS Requirements for Hydrology (Legacy)

Hydrology datasets followed the CRS standard then located at `docs/standards/geo/crs-standard.md` (now superseded).

### Allowed CRSs

- **EPSG:26914 (NAD83 / UTM 14N)** — processing CRS  
- **EPSG:4326 (WGS84)** — STAC, GeoJSON, UI layers  

Bathymetry & WID rasters were required to be processed in a projected CRS (UTM 14N) before export to EPSG:4326 for catalogs and UI.

---

## 🧩 3. Hydrology STAC Metadata Requirements (Legacy)

Each hydrology STAC Item was expected to include:

```json
{
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
  "proj:bbox": [],
  "proj:shape": [],
  "proj:transform": []
}
```

Key expectations:

- Explicit hydrologic typing via `hydro:type`.  
- Clear declaration of vertical datum and geoid model.  
- Linkage to CRS via `proj:*` fields.  

---

## 🔬 4. Streamflow & Discharge Grids (CF Convention – Legacy)

### Required CF Fields (Example)

```text
flow:standard_name = "volume_transport";
flow:units = "m3 s-1";
flow:positive = "unidirectional";
flow:grid_mapping = "crs";
```

Legacy KFM behaviors:

1. Streamflow fields had to represent **centerline‑referenced routing** or distributed flow grids with documented method.  
2. Depth‑integrated flow required explicit Manning or hydraulic parameters when used.  
3. Rasters were expected to align with hydrologic catchments described in STAC/graph.

---

## 🌊 5. Bathymetry Standards (Legacy)

Bathymetric rasters were required to:

- Use **positive down** for depths  
- Use **NAVD88 + GEOID18** as vertical reference  
- Report depth relative to a **static water surface** if applicable  
- Provide `bathymetry:epoch` when multi‑year composites were used  

COG formatting conventions (typical):

```text
COG with internal tiling: 512x512
LZW compression
Overviews at 2×, 4×, 8×, …
```

---

## 🚢 6. Water Injection Dredging (WID) Standards (Legacy)

WID models were expected to include:

### 6.1 Metadata

```json
{
  "wid:method": "jetting|fluidization",
  "wid:power_kw": 0.0,
  "wid:discharge_m3s": 0.0,
  "wid:model": "USACE-WID-v3|KFM-WID-v11",
  "wid:sediment_transport_coeff": 0.0,
  "wid:delta_bed_elevation_units": "m"
}
```

### 6.2 DoD / Bed Elevation Conventions

Difference‑of‑DEM (DoD) sign conventions followed the global rule:

- **Negative = erosion**  
- **Positive = deposition**

Example variable:

```text
dBed:units    = "m";
dBed:positive = "up";  # bed rising = positive
```

---

## 📈 7. Water‑Surface Elevation Models (WSEL) – Legacy

Water‑surface rasters (reservoir stage, floodplain surface, hydraulic models) had to:

- Use orthometric heights (NAVD88)  
- Use CF `positive="up"`  
- Include `hydro:reference_plane="ORTHOMETRIC_NAVD88"`  
- Provide Manning, roughness, or boundary parameters for hydraulic simulations where applicable  
- Include uncertainty where available, for example:

```json
{
  "hydro:uncertainty_m": 0.15
}
```

---

## 🌧 8. Lake / Reservoir Time‑Series (Elevation–Storage) – Legacy

Time‑series were required to:

- Provide both **elevation (m)** and **storage (acre‑ft or m³)**  
- Include conversion tables as attached assets in STAC  
- Use OWL‑Time intervals for temporal coverage  
- Include `prov:activity="hydro-timeseries-v11"` in provenance

Example STAC asset:

```json
{
  "assets": {
    "elev_storage_curve": {
      "href": "storage.csv",
      "type": "text/csv",
      "roles": ["metadata"]
    }
  }
}
```

---

## 🌐 9. UI Rendering Rules (MapLibre/Cesium) – Legacy

### 9.1 Bathymetry

- Render with **positive down** colormap.  
- Legend text (typical):  
  `Depth below NAVD88 (m), positive downward`.

### 9.2 Streamflow

- Graduated line width based on flow volume.  
- Tooltip showing discharge in m³/s.  
- Time slider driving CF‑compliant time dimensions.

### 9.3 WID Layers

- Visually highlight simulated erosion/deposition.  
- Standard legend pattern:  
  `"Blue = erosion (neg), Red = deposition (pos)"`.

---

## 📚 10. PROV‑O Requirements (Legacy)

Every hydrology dataset was expected to record:

```text
prov:used           → source DEM / bathymetry / gauges
prov:activity       → "hydrology-processing-v11"
prov:wasGeneratedBy → tool + version
prov:generatedAtTime → timestamp
prov:wasAssociatedWith → ETL agent
```

Hydrology transformations were logged in the Neo4j lineage graph as:

- Entities for inputs/outputs.  
- Activities for hydrology processing steps.  
- Agents representing pipelines and operators.

---

## ⚙ 11. CI/CD Validation Gates (Legacy)

A PR was **blocked** under v11.0.0 hydrology rules if:

- Vertical datum metadata was missing.  
- CF‑Time metadata was invalid or inconsistent.  
- CRS for STAC/UI was not EPSG:4326.  
- PROV‑O lineage for key transformations was missing.  
- DoD sign conventions were inverted or undocumented.  
- Bathymetry encoded depths with positive up instead of down.  
- Flow rasters lacked explicit `units`.  
- Hydrology STAC extensions were missing or incomplete.  
- Cesium layers were delivered without orthometric heights.

These checks have since been integrated and expanded in the v11.2.4 hydrology and vertical‑axis standards under `docs/standards/geospatial/`.

---

## 🕰️ Version History

| Version | Date       | Status       | Notes                                                                                                     |
|--------:|------------|-------------|-----------------------------------------------------------------------------------------------------------|
| v11.0.0 | 2025-11-22 | Superseded  | Initial v11 hydrology standard with CRS, CF, STAC, WID, DoD, and PROV‑O requirements for water datasets. |

---

<div align="center">

💧 **Kansas Frontier Matrix — Hydrology & Water Surface Standards (Legacy v11.0.0)**  
Hydraulic Accuracy · Datum Discipline · Scientific Integrity (Historical Baseline)  

📌 **Current hydrology rules:** `docs/standards/geospatial/hydrology-standards.md`  

[🌎 Geospatial Standards Index](../geospatial/README.md) · [📐 Vertical Axis & DoD](../geospatial/vertical-axis-and-dod.md) · [📐 CRS & Topology](../geospatial/crs-topology/README.md) · [⚖ Governance](../governance/ROOT-GOVERNANCE.md)

</div>
