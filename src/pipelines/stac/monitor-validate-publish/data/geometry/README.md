---
title: "📐 Kansas Frontier Matrix — STAC Orchestrator Geometry Assets (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "src/pipelines/stac/monitor-validate-publish/data/geometry/README.md"
version: "v10.3.1"
last_updated: "2025-11-14"
review_cycle: "Quarterly · FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../releases/v10.3.0/sbom.spdx.json"
manifest_ref: "../../../../../../releases/v10.3.0/manifest.zip"
telemetry_ref: "../../../../../../releases/v10.3.0/focus-telemetry.json"
telemetry_schema: "../../../../../../schemas/telemetry/pipelines-stac-geometry-v1.json"
governance_ref: "../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 📐 **Kansas Frontier Matrix — STAC Orchestrator Geometry Assets**  
`src/pipelines/stac/monitor-validate-publish/data/geometry/README.md`

**Purpose:**  
Document the authoritative spatial geometries used by the **STAC Monitor → Validate → Publish** orchestrator, including the **Kansas AOI**, derivations, tiles, and governance-mandated generalization assets.  
These geometries define **where** STAC polling, validation, masking, and sovereignty checks apply.

<img alt="AOI" src="https://img.shields.io/badge/AOI-Kansas-blue"/>
<img alt="FAIR+CARE" src="https://img.shields.io/badge/FAIR%2BCARE-Geospatial_Governed-orange"/>
<img alt="Spatial" src="https://img.shields.io/badge/CRS-EPSG%3A4326-green"/>
<img alt="Status" src="https://img.shields.io/badge/Status-Authoritative-success"/>

</div>

---

## 📘 Overview

The geometry directory contains:

- The **Kansas Area of Interest (AOI)** used for STAC API Item Search  
- Optional **tilings** (H3 / quadbin) to partition polling workloads  
- Derived geometries for CARE-mandated **spatial masking**  
- Sovereignty-aware polygons for tribal or heritage-sensitive overlays  
- Reprojection or simplification auxiliary files  

All geometries are:

- Required to be **EPSG:4326**  
- Validated geospatially (Shapely / GEOS / JSONSchema)  
- FAIR+CARE compliant  
- Input to multiple STAC-related pipelines  

---

## 🗂️ Directory Layout

~~~~~text
src/pipelines/stac/monitor-validate-publish/data/geometry/
├── README.md                     # This file
├── kansas_aoi.geojson            # Authoritative statewide AOI
├── kansas_aoi_simplified.geojson # Optional simplified AOI for faster polling
├── h3_tiles.geojson              # Optional H3-derived tiles
├── quadbins.geojson              # Optional quadbin grid
└── sovereignty_overlays.geojson  # Optional tribal/cultural governance polygons
~~~~~

---

## 📌 Kansas AOI (Authoritative)

File:  
~~~~~text
kansas_aoi.geojson
~~~~~

Requirements:

- CRS: **EPSG:4326**  
- Valid GeoJSON Feature or FeatureCollection  
- Must represent the complete Kansas state boundary or polling boundary  
- Used directly by `monitor.py` for STAC Item Search  
- Must be kept **stable** unless governance update requires change  

Validation rules:

- Geometry must be **valid** (`is_valid == True`)  
- No self-intersections  
- Bbox must match Kansas extent  

---

## 🔧 Derived AOIs

### `kansas_aoi_simplified.geojson`

Used for performance-sensitive STAC polling.

Rules:

- Must be a topologically valid simplification  
- Must preserve coverage of the authoritative AOI  
- Simplification tolerance documented in metadata  

---

## 🔳 Optional Tiling Assets

### `h3_tiles.geojson`

- H3 hexagons covering Kansas  
- Recommended resolution: r6–r8  
- Used for incremental or parallel polling windows  
- CRS must be EPSG:4326  

### `quadbins.geojson`

- Quadbin-derived grid (WebMercator indexing)  
- Used for tiled ingestion for large-volume STAC providers  
- Must include quadbin IDs + bounding geometry

---

## 🧭 Sovereignty Overlays

### `sovereignty_overlays.geojson`

Contains:

- Tribal land boundaries  
- Cultural heritage sensitivity polygons  
- Archaeologically sensitive regions  

Governance rules:

- If an Item footprint intersects this geometry:  
  - CARE label may be required (`sensitive` or `restricted`)  
  - Additional masking rules apply  
  - Governance pipeline must be invoked  

Validation:

- CRS: EPSG:4326  
- Geometry validity required  
- Metadata must include:  
  - `kfm:sovereignty_source`  
  - `kfm:review_required = true`  

---

## 🧪 Validation Flow (Indented Mermaid)

~~~~~mermaid
flowchart TD
  A["Load Geometry"] --> B["Validate CRS = EPSG:4326"]
  B --> C["Topology Check<br/>is_valid"]
  C --> D["Governance Check<br/>sovereignty overlays"]
  D --> E["Use in STAC Polling / Masking / AOI Filters"]
~~~~~

---

## 📡 Telemetry Integration

During orchestrator runs, geometry contributes to:

- `aoi_area_km2`
- `tiles_used`
- `sovereignty_intersections`
- `masking_required`
- `masking_strategy`
- `energy_wh` / `co2_g` (depend on geometry complexity)

Telemetry appended to:

~~~~~text
../../../../../../releases/v10.3.0/focus-telemetry.json
~~~~~

---

## 🧯 Local Validation Examples

Check geometry validity:

~~~~~bash
geojsonhint src/pipelines/stac/monitor-validate-publish/data/geometry/kansas_aoi.geojson
~~~~~

View polygon area:

~~~~~bash
python - <<'EOF'
from shapely.geometry import shape
import json
g = shape(json.load(open("src/pipelines/stac/monitor-validate-publish/data/geometry/kansas_aoi.geojson"))["geometry"])
print(g.area)
EOF
~~~~~

Inspect sovereignty overlays:

~~~~~bash
jq '.' src/pipelines/stac/monitor-validate-publish/data/geometry/sovereignty_overlays.geojson
~~~~~

---

## 🕰️ Version History

| Version | Date       | Author | Summary |
|---------|------------|--------|---------|
| v10.3.1 | 2025-11-14 | STAC Pipelines Team | Added authoritative documentation for AOI, tiles, sovereignty overlays, and governance rules with KFM Markdown compliance. |

---

<div align="center">

**Kansas Frontier Matrix — STAC Geometry Assets**  
Authoritative AOI × Governance-Aware Geospatial Logic × FAIR+CARE  
© 2025 Kansas Frontier Matrix — CC-BY 4.0  

[Back to STAC Orchestrator Data Layer](../README.md)

</div>
