<div align="center">

# 📦 Kansas-Frontier-Matrix — Source Descriptors (`web/docs/SOURCES.md`)

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../.github/workflows/site.yml)  
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](../../.github/workflows/stac-validate.yml)  
[![Pre-Commit](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/pre-commit.yml/badge.svg)](../../.github/workflows/pre-commit.yml)  
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](../../.github/workflows/codeql.yml)  
[![Trivy Security Scan](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](../../.github/workflows/trivy.yml)

</div>

---

## 📖 Purpose

All **datasets** in the Kansas-Frontier-Matrix project must have a **source descriptor JSON** under `data/sources/`.  
This ensures traceability, provenance, and reproducibility — core to the MCP workflow.

Each descriptor declares:
- **id, title, type** of dataset  
- **endpoint(s)** for retrieval  
- **spatial and temporal metadata**  
- **license / provenance**  
- **expected outputs** (COGs, GeoJSON, etc.)  

---

## 🧱 Schema-Lite

| Field      | Type     | Required | Description                                                                 |
|------------|----------|----------|-----------------------------------------------------------------------------|
| `id`       | string   | ✅        | Unique identifier (lower-hyphen naming)                                     |
| `title`    | string   | ✅        | Human-readable name                                                         |
| `type`     | string   | ✅        | `raster`, `raster-dem`, `vector`, `geojson`, or `document`                  |
| `endpoint` | object   | ✅        | Defines fetch method: `{ "type": "http"|"ftp"|"s3"|"arcgis", "urls": [] }` |
| `spatial`  | object   | opt       | `{ "bbox": [W,S,E,N], "crs": "EPSG:4326" }`                                |
| `temporal` | object   | opt       | `{ "start": "YYYY-MM-DD", "end": "YYYY-MM-DD" }`                           |
| `license`  | string   | ✅        | Dataset license (e.g., `"Public Domain"`, `"CC-BY-4.0"`)                    |
| `outputs`  | object   | opt       | Expected processed artifacts (COG path, GeoJSON path, MBTiles, etc.)        |
| `notes`    | string   | opt       | Freeform description / provenance                                           |

---

## 📝 Example: Historic Soil Map

```json
{
  "id": "usda_soil_1967",
  "title": "Soil Survey Map (1967)",
  "type": "raster",
  "endpoint": {
    "type": "http",
    "urls": ["https://archive.example.org/soils/kansas_1967_map.tif"]
  },
  "spatial": { "bbox": [-101.5, 39.0, -100.8, 39.5], "crs": "EPSG:4326" },
  "temporal": { "start": "1967-01-01", "end": "1967-12-31" },
  "license": "Public Domain",
  "outputs": { "cog": "data/cogs/overlays/soil_map_1967.tif" },
  "notes": "Scanned USDA Soil Survey, archived from Kansas GIS Hub"
}


⸻

🔄 Workflow Integration

flowchart LR
  A["data/sources/*.json"] --> B["make fetch\n(download raw assets)"]
  B --> C["make cogs / make vectors\n(convert to COG/GeoJSON)"]
  C --> D["make stac\n(write STAC items)"]
  D --> E["Viewer Config\n(app.config.json)"]


⸻

✅ Validation

Local checks:

# Syntax check
jq . data/sources/usda_soil_1967.json > /dev/null

# Schema validation
ajv validate -s web/config/source.schema.json -d data/sources/*.json

CI will run:
	•	JSON schema validation
	•	SHA256 checksums of fetched data
	•	STAC item generation/validation

⸻

📌 Conventions
	•	Paths: use relative outputs (e.g., data/cogs/..., data/processed/...).
	•	Licenses: must be declared (Public Domain, CC-BY, etc.).
	•	Bounding boxes: always in EPSG:4326 (WGS84 lon/lat).
	•	Temporal: prefer full ISO dates; year-only allowed if precise dates unavailable.
	•	Notes: capture provenance and caveats.

⸻


<div align="center">


✅ Source descriptors guarantee traceability, reproducibility, and provenance — ensuring Kansas-Frontier-Matrix remains a mission-grade historical GIS hub.

</div>
```
