# Kansas-Frontier-Matrix — Collection Scripts

This folder (`scripts/collections/`) contains **domain-specific helper scripts** that build, validate, and
integrate **STAC collections** for the Kansas Frontier Matrix pipeline.  
Each script focuses on a single **thematic dataset family** (e.g. elevation, hazards, archaeology),
wrapping CLI tools (GDAL, rio-cogeo, ogr2ogr, etc.) and Makefile targets.

Scripts here are **collection-level**:  
- They aggregate multiple STAC Items (e.g. yearly tornado tracks, county boundaries).  
- They register those Items into their parent `stac/collections/*.json`.  
- They ensure provenance, metadata, and reproducibility across the dataset family.

---

## 📂 Current Scripts

| Script | Purpose |
|--------|---------|
| `elevation.sh` | DEMs, LiDAR, terrain derivatives (hillshade, slope, aspect) |
| `overlays.sh` | Historical topo maps, soils, plats, scanned overlays |
| `vectors.sh` | Treaty boundaries, railroads, parcels, hydrology vectors |
| `documents.sh` | OCR + ingestion of treaties, diaries, newspapers into STAC + KG |
| `hazards.sh` | NOAA/SPC/FEMA/USDM/NIFC hazard collections (storms, droughts, wildfires) |
| `deeds.sh` | Kansas Register of Deeds + parcel maps integration |
| `archaeology.sh` | Archaeology sites, surveys, excavation datasets |
| `metadata.sh` | Cross-links, provenance stamping, license checks |
| `validate.sh` | Runs collection-level STAC validation and checksum tests |

---

## 🚧 Planned / Future Scripts

To support the roadmap (see project docs):

- `newspapers_ocr.sh` — Kansas newspaper OCR → STAC + Knowledge Graph  
- `oral_histories.sh` — Tribal narratives and community oral archives  
- `county_boundaries.sh` — Boundary formation timeline (territorial → present)  
- `paleoclimate.sh` — Tree rings, pollen cores, drought proxy data  
- `groundwater_aquifers.sh` — Ogallala aquifer, well logs, water-level maps  
- `fire_ecology.sh` — Prairie fire regimes, Indigenous burn records  
- `photographs.sh` — Geotagged Kansas Memory / LOC photo archives  
- `cemeteries_schools.sh` — County cemeteries, historic schoolhouse datasets  
- `fractals_patterns.sh` — Settlement clustering, river morphology analysis  
- `predictive_models.sh` — Dust Bowl recurrence, alt. infrastructure what-ifs  
- `ontologies_reasoning.sh` — Treaty, law, and land ontologies + symbolic reasoning  

---

## 🛠️ Usage

Each script is CLI-first and reproducible:

```bash
# Example: build elevation collection
./scripts/collections/elevation.sh build

# Validate all collections
./scripts/collections/validate.sh
````

Scripts share common patterns:

* **Fetch** raw data (`make fetch`, curl, ArcGIS REST, or API call).
* **Transform** into web-safe formats (COG, GeoJSON, PMTiles).
* **Load** into STAC (`stac/items/`, `stac/collections/`) with metadata, bbox, and datetime.
* **Validate** against schemas (`stac-validate`, `jq`, checksum tests).

---

## 🔗 Connections

* **Makefile** — orchestrates collection builds (`make elevation`, `make hazards`).
* **STAC catalog** — scripts register outputs into `stac/collections/*.json`.
* **Knowledge Graph** — document/archaeology scripts also push metadata into the KG (Neo4j).
* **Web viewer** — layers become available in `web/app.config.json` via `kgt render-config`.

---

## 📑 Notes for Developers

* Always **log actions and errors**; follow the MCP *Scientific Method* reproducibility ethos.
* Include **source URLs, licenses, temporal coverage, and CRS** in every collection.
* Prefer open formats: **COG** for rasters, **GeoJSON/PMTiles** for vectors.
* Validate before commit: run `make stac-validate`.
* When adding a new collection, create a script here + STAC collection JSON under `stac/collections/`.

---

✦ These scripts make it easy to **grow the Kansas Frontier Matrix library of collections** over time,
scaling from maps → documents → culture → science → predictive analytics.

```
