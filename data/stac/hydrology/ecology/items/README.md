---
title: "🧬 Kansas Frontier Matrix — Hydrology–Ecology STAC Items Index (v11 Super-Edition)"
path: "data/stac/hydrology/ecology/items/README.md"
version: "v11.0.0"
last_updated: "2025-11-21"
review_cycle: "Annual • Hydrology–Ecology Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/data-stac-hydro-ecology-items-v1.json"
governance_ref: "../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active • Enforced"
doc_kind: "STAC Items Index"
intent: "stac-hydrology-ecology-items-index"
semantic_document_id: "kfm-stac-hydrology-ecology-items-index"
doc_uuid: "urn:kfm:stac:hydrology:ecology:items:index:v11.0.0"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
fair_category: "F1-A1-I1-R1"
care_label: "Public-Low-Risk"
immutability_status: "version-pinned"
---

<div align="center">

# 🧬 **Hydrology–Ecology STAC Items Index (v11 Super-Edition)**  
`data/stac/hydrology/ecology/items/README.md`

**Purpose:**  
Serve as the **authoritative, domain-wide index and specification** for all hydrology-linked  
ecological STAC Items in the Kansas Frontier Matrix. This includes mussel, fish, macroinvertebrate,  
riparian, and habitat datasets directly influenced by hydrologic and geomorphic processes at  
Tuttle Creek, Clinton, Milford, Perry, the Kansas River, and statewide aquatic corridors.

</div>

---

# 📘 0. Overview

The **Hydrology–Ecology STAC Items** directory is the **atomic metadata layer** for ecological datasets  
that are explicitly coupled to hydrology. Each JSON file in this directory (and subdirectories) is a  
**STAC Item** describing:

- A single **ecological dataset** (e.g., mussel bed survey, fish community sample, macroinvertebrate index)  
- Its **spatial footprint** (Point/LineString/Polygon) in **GeoSPARQL-ready coordinates**  
- Its **temporal coverage** (instantaneous sampling or multi-day campaigns)  
- One or more **assets** (GeoJSON, CSVW, NetCDF, MP4) with standardized metadata  
- **Hydrology–ecology semantics** via `kfm:*` fields (group, parameter, units, habitat type)  
- **Provenance and lineage** via PROV-O (`prov:wasGeneratedBy`, `prov:used`, `prov:wasAttributedTo`)  

These Items feed the entire KFM stack:

```text
Ecology STAC Item
  → Hydrology–Ecology STAC Collection
  → Neo4j Graph (CIDOC-CRM + GeoSPARQL)
  → KFM APIs (GraphQL/REST)
  → Focus Mode v3 (Ecology Context)
  → Story Node v3 (Ecological Narratives)
```

---

# 🗂️ 1. Directory Layout (Domain-Level Ecology Items)

This directory indexes Items for ecology datasets under the hydrology domain.

```text
data/
└── stac/
    └── hydrology/
        └── ecology/
            ├── README.md                 # Collection-level documentation
            └── items/
                ├── mussels-tc-tailwater.json
                ├── mussels-clinton.json
                ├── fish-tc-2025.json
                ├── fish-clinton.json
                ├── macroinv-tc.json
                ├── riparian-zones.json
                ├── habitat-polygons.json
                ├── downstream-biotic-response.json
                └── wid-2025-biological-summary.json
```

Reservoir- or basin-specific STAC Items (e.g., `tuttle-creek`, `clinton`) may also define their own nested  
ecology Items, but all ecology Items share the **same hydrology–ecology STAC profile** specified here.

---

# 🧾 2. Item Naming Conventions

To guarantee **global uniqueness** and predictable ingestion, each Item `id` should follow:

```text
<region-or-reservoir>-<ecology-group>-<theme>-<time-scope>-<version>

Examples:
- tc-mussels-tailwater-2024-v1
- clinton-fish-mainstem-2023-v1
- kansas-river-macroinv-2019-2021-v1
- tc-wid2025-bio-response-v1
```

Where:

- `region-or-reservoir` → `tc`, `clinton`, `milford`, `perry`, `kansas-river`, etc.  
- `ecology-group` → `mussels`, `fish`, `macroinv`, `riparian`, `habitat`, etc.  
- `theme` → `tailwater`, `delta`, `mainstem`, `corridor`, `wid`, etc.  
- `time-scope` → `YYYY`, `YYYY-YYYY`, or explicit event timestamps if needed.  
- `version` → `v1`, `v2`, etc., tied to ETL pipeline version.

This `id` is mapped to **CIDOC `E42 Identifier`** and **DCAT `dct:identifier`**.

---

# 🛰️ 3. Required STAC Metadata Fields (Hydrology–Ecology Profile)

Every STAC Item in this directory **must** satisfy both the **core STAC 1.0.0** and **KFM hydrology–ecology extension**.

## 3.1 Core STAC Fields

```json
{
  "stac_version": "1.0.0",
  "type": "Feature",
  "id": "tc-mussels-tailwater-2024-v1",
  "collection": "hydrology-ecology",
  "geometry": { "type": "Polygon", "coordinates": [...] },
  "bbox": [...],
  "properties": {
    "datetime": "2024-07-15T00:00:00Z"
  },
  "assets": { ... }
}
```

## 3.2 Hydrology–Ecology `kfm:*` Fields (Mandatory)

| Field | Description |
|-------|-------------|
| `kfm:parameter` | Ecological variable (e.g., `mussels`, `fish`, `macroinvertebrates`, `riparian_veg`) |
| `kfm:units` | Units (e.g., `individuals_per_m2`, `count`, `index_score`) |
| `kfm:ecology_group` | High-level group (`mussels`, `fish`, `macroinvertebrates`, `vegetation`) |
| `kfm:site` | Survey site ID (e.g., transect code, station ID) |
| `kfm:provider` | Data owner (e.g., `KDWPT`, `USACE`, `USGS`, tribal nation) |
| `kfm:method` | Sampling method (`quadrat`, `electrofishing`, `kick_net`, `visual_transect`) |
| `kfm:lineage` | ETL pipeline identifier (e.g., `etl/ecology_mussels_tc_v1`) |
| `kfm:quality` | QA tier (`A`, `B`, `C`, `Provisional`) |
| `kfm:hydro_region` | Linked hydrologic region (e.g., `Tuttle_Creek_Tailwater`) |
| `kfm:project` | Associated project (`Downstream-Effects`, `WID-2025`, etc.) |

## 3.3 Recommended Fields

- `kfm:habitat_type` (riffle, pool, backwater, shoal)  
- `kfm:dominant_species` (e.g., `Lampsilis cardium`)  
- `kfm:survey_protocol` (e.g., SOP ID)  
- `kfm:ecological_index` (e.g., HBI, EPT, IBI score)  

---

# 🌍 4. Asset Types & Schemas

## 4.1 GeoJSON (Primary for Ecology)

Used for:

- Mussel bed polygons  
- Fish and invertebrate sample points  
- Riparian/habitat polygons  
- Ecological corridor layers  

GeoJSON schema:

- `type`: `"FeatureCollection"`  
- `features[].geometry`: `Point`, `LineString`, `Polygon`  
- `features[].properties`:

  - `survey_id`  
  - `parameter`  
  - `value` (if point-based)  
  - `units`  
  - `species` (where applicable)  
  - `method`  
  - `timestamp` or `start_time` / `end_time`  
  - `kfm:*` fields  

---

## 4.2 CSV / CSVW (Tabular Survey Data)

Used when:

- Data is numerically oriented (e.g., species counts, index scores).  

Required columns:

| Column | Description |
|--------|-------------|
| `survey_id` | Unique survey identifier |
| `timestamp` | Sample datetime (ISO 8601) |
| `site_id` | Spatial site key (link to Place) |
| `parameter` | e.g., `mussels`, `fish_abundance`, `EPT_index` |
| `value` | Numeric or categorical |
| `units` | Measurement units |
| `qc_flag` | QA/QC code |
| `provenance_id` | Link to ETL/Document |

CSVW metadata files must be defined in `data/hydrology` per the hydrology data domain rules.

---

## 4.3 Raster (COG) — Optional

Used for:

- Ecological suitability surfaces  
- Habitat-quality rasters  
- Vegetation classification grids  

Metadata must include:

- `proj:*` (EPSG, transform, shape)  
- `kfm:parameter`, `kfm:units`, `kfm:method`, `kfm:lineage`  
- `roles`: `[ "data" ]`  
- `checksum:sha256`  

---

## 4.4 Media (MP4) — Optional

Used for:

- Underwater video transects  
- Drone-based riparian mapping  

Linked as:

```json
"video": {
  "href": "https://example.org/ecology/tc_mussels_video_2024.mp4",
  "type": "video/mp4",
  "roles": ["overview", "visual"]
}
```

---

# 🧬 5. Example STAC Items

## 5.1 Mussel Bed Polygon (Tuttle Creek Tailwater)

```json
{
  "stac_version": "1.0.0",
  "type": "Feature",
  "id": "tc-mussels-tailwater-2024-v1",
  "collection": "hydrology-ecology",
  "geometry": { "type": "Polygon", "coordinates": [...] },
  "bbox": [-96.6005, 39.275, -96.598, 39.278],
  "properties": {
    "datetime": "2024-07-15T00:00:00Z",
    "kfm:parameter": "mussels",
    "kfm:units": "individuals_per_m2",
    "kfm:ecology_group": "mussels",
    "kfm:provider": "KDWPT",
    "kfm:method": "quadrat",
    "kfm:lineage": "etl/mussels_tc_tailwater_v1",
    "kfm:quality": "A",
    "kfm:hydro_region": "Tuttle_Creek_Tailwater",
    "kfm:project": "Downstream-Effects"
  },
  "assets": {
    "data": {
      "href": "https://example.org/ecology/tc/mussels/tailwater_2024.geojson",
      "type": "application/geo+json",
      "roles": ["data"],
      "checksum:sha256": "..."
    }
  }
}
```

---

## 5.2 Fish Assemblage Survey (Clinton Lake)

```json
{
  "stac_version": "1.0.0",
  "type": "Feature",
  "id": "clinton-fish-mainstem-2023-v1",
  "collection": "hydrology-ecology",
  "geometry": { "type": "Point", "coordinates": [-95.37, 38.94] },
  "bbox": [-95.371, 38.939, -95.369, 38.941],
  "properties": {
    "datetime": "2023-06-20T15:00:00Z",
    "kfm:parameter": "fish_assemblage",
    "kfm:units": "count",
    "kfm:ecology_group": "fish",
    "kfm:provider": "Clinton_Reservoir_Biologist",
    "kfm:method": "boat_electrofishing",
    "kfm:lineage": "etl/fish_clinton_2023_v1",
    "kfm:quality": "A",
    "kfm:hydro_region": "Clinton_Reservoir",
    "kfm:project": "Hydrology-Core"
  },
  "assets": {
    "table": {
      "href": "https://example.org/ecology/clinton/fish_survey_2023.csv",
      "type": "text/csv",
      "roles": ["data"]
    }
  }
}
```

---

# 🧠 6. DCAT, PROV-O, and CIDOC-CRM Mapping

## 6.1 DCAT Crosswalk

| STAC | DCAT |
|------|------|
| `id` | `dct:identifier` |
| `description` | `dct:description` |
| `assets.*.href` | `dcat:downloadURL` |
| `kfm:provider` | `dct:publisher` or `dct:creator` |
| `properties.datetime` | `dct:issued` / `dct:temporal` |
| `bbox` | `dct:spatial` |

## 6.2 PROV-O Lineage

Each survey dataset (Item) is:

- `prov:Entity` with `prov:wasGeneratedBy` → sampling or modeling `prov:Activity`  
- `prov:wasAttributedTo` → `prov:Agent` (agency, research team, tribe)  
- `prov:used` → hydrology datasets (e.g., DO, turbidity, flow) used as covariates  

## 6.3 CIDOC-CRM & GeoSPARQL

### Entities
- `E53 Place` — habitat polygon, survey reach, station location  
- `E7 Activity` — ecological survey event  
- `E39 Actor` — field crew, agency, tribal partners  
- `E73 InformationObject` — survey dataset  
- `E3 ConditionState` — ecological condition of a place (e.g., mussel density at time `t`)  

### Relationships
- `P7_took_place_at` → Place (reach, bed, habitat polygon)  
- `P14_carried_out_by` → Actor (survey team, biologist)  
- `P70_documents` → Document (survey report)  
- `geo:hasGeometry` → WKT/GeoJSON geometry  
- `time:hasTime` → sampling date/time  

---

# 🧪 7. QA/QC & FAIR+CARE Requirements

Every ecological STAC Item must:

- Include **QA fields** (`kfm:quality`, `qc_flag`)  
- Reference **calibration procedures** (if instrument-based)  
- Respect **Indigenous data sovereignty** (if tribal data are present)  
- Use **clear licensing** (e.g., CC-BY 4.0, CC-BY-NC if required)  
- Encode **provenance** via PROV-O  

For sensitive ecological locations (e.g., rare or endangered species):

- Use **generalized geometries** (H3 cell or coarse polygon)  
- Include flag `kfm:sensitivity = "high"`  
- Coordinate exact locations are stored only under governed access (outside public STAC)

---

# 🎯 8. Focus Mode v3 Integration

Ecological STAC Items power Focus Mode in several ways:

- When a user focuses on a **reach or reservoir**, relevant ecology Items are retrieved via:  
  - `kfm:hydro_region`  
  - `kfm:parameter` or `kfm:ecology_group`  
  - Temporal filters  

- Panels can show:

  - **Mussel density over time** under different hydrologic regimes  
  - **Fish assemblage shifts** pre/post major floods  
  - **Macroinvertebrate indices** vs DO/turbidity patterns  
  - **Ecological responses to WID 2025**  

---

# 📖 9. Story Node v3 Integration

Ecological Items are essential for narrative depth in Story Nodes:

- **“Downstream of the Dam”** — tailwater biota vs DO/turbidity  
- **“Mussel Corridors of the Big Blue & Kansas Rivers”** — connectivity & disturbance  
- **“After the Pulse” (WID 2025)** — short-term vs long-term ecological response  

Story Nodes reference Item IDs via:

```json
{
  "rel": "uses-dataset",
  "target": "tc-mussels-tailwater-2024-v1"
}
```

This enables clickable, time-aware visualization of biological responses.

---

# 🚀 10. Expansion Roadmap — Ecology Items

Future Items may include:

- Annual monitoring campaigns (2025–2035) for mussels, fish, macroinvertebrates  
- eDNA-based biodiversity surveys  
- High-resolution riparian vegetation rasters  
- Habitat connectivity networks (graph-based corridors)  
- Scenario-based ecological response models  

All future Items must adhere to this **Hydrology–Ecology STAC profile**.

---

# 🕰 Version History

- **v11.0.0 (2025-11-21):** Initial creation of Hydrology–Ecology STAC Items super-index.

---

[⬅ Back to Hydrology–Ecology STAC Collection](../README.md) • [⬅ Back to Hydrology STAC Domain](../../README.md) • [🏠 KFM Master Guide](../../../../../docs/reference/kfm_v11_master_documentation.md)

