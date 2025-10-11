<div align="center">

# ⚠️ Kansas Frontier Matrix — Hazards Metadata  
`data/processed/metadata/hazards/`

**Mission:** Curate, document, and standardize all **processed natural hazard datasets**  
used in Kansas Frontier Matrix — including tornadoes, floods, droughts, wildfires, and severe weather events —  
to build a reproducible spatiotemporal understanding of risk and resilience across Kansas.

<!-- Badges (use relative links to your workflows; swap to shields.io variants if preferred) -->
[![Build & Deploy](https://img.shields.io/badge/CI-Build%20%26%20Deploy-blue)](../../../.github/workflows/site.yml)
[![STAC Validate](https://img.shields.io/badge/STAC-validate-green)](../../../.github/workflows/stac-validate.yml)
[![CodeQL](https://img.shields.io/badge/CodeQL-security-yellow)](../../../.github/workflows/codeql.yml)
[![Trivy](https://img.shields.io/badge/Container-Scan-informational)](../../../.github/workflows/trivy.yml)
[![Pre-Commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen.svg)](https://pre-commit.com/)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../docs/)
[![License: Data](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../../LICENSE)

</div>

---

**Version:** v1.1.0  
**Status:** Stable  
**Last updated:** 2025-10-11

> This README follows the **MCP** documentation-first pattern and includes **SemVer**, **CHANGELOG**, **Mermaid-safe diagrams**, **STAC hooks**, **checksums**, and **AI/Graph** bindings for hazards.

---

## 📚 Overview

This directory contains **metadata and provenance documentation** for all **hazard-related processed datasets** in KFM.

Datasets include **tornado tracks, flood zones, wildfire perimeters, drought indices, and storm records**, aligned to Kansas’s spatiotemporal framework.

Each dataset provides:
- **STAC 1.0** metadata (`.json`)
- **SHA-256** checksum sidecars for reproducibility
- **Open license + provenance** fields
- **JSON Schema** + **STAC** validation in CI

---

## 🗂️ Directory Layout

```bash
data/processed/metadata/hazards/
├── README.md
├── CHANGELOG.md
├── schema/
│   ├── hazards-item.schema.json
│   └── hazards-collection.schema.json
├── cards/                         # human-friendly dataset cards (one per dataset)
│   ├── tornado_tracks_1950_2024.md
│   ├── flood_events_1900_2025.md
│   └── wildfire_perimeters_2000_2024.md
├── stac/                          # canonical STAC metadata (items/collections)
│   ├── hazards-collection.json
│   ├── tornado_tracks_1950_2024.json
│   ├── flood_events_1900_2025.json
│   └── wildfire_perimeters_2000_2024.json
├── thumbnails/                    # map/UI preview images
│   ├── tornado_tracks_1950_2024.png
│   ├── flood_events_1900_2025.png
│   └── wildfire_perimeters_2000_2024.png
└── checksums/
    ├── tornado_tracks_1950_2024.geojson.sha256
    ├── flood_events_1900_2025.geojson.sha256
    └── wildfire_perimeters_2000_2024.geojson.sha256
````

> Each STAC item references its **processed dataset** under `data/processed/hazards/` and its **thumbnail** here for UI previews.

---

## 🌪️ Hazard Layers (Processed Assets)

| Layer                               | Source(s)                  | Format        | Spatial Unit  | Temporal Coverage | Output                                                         |
| :---------------------------------- | :------------------------- | :------------ | :------------ | :---------------- | :------------------------------------------------------------- |
| **Tornado Tracks (1950–2024)**      | NOAA SPC                   | GeoJSON       | Line          | 1950–2024         | `data/processed/hazards/tornado_tracks_1950_2024.geojson`      |
| **Flood Events (1900–2025)**        | NOAA / USGS / FEMA         | GeoJSON + CSV | Point/Polygon | 1900–2025         | `data/processed/hazards/flood_events_1900_2025.geojson`        |
| **Wildfire Perimeters (2000–2024)** | USGS / USDA Forest Service | GeoJSON       | Polygon       | 2000–2024         | `data/processed/hazards/wildfire_perimeters_2000_2024.geojson` |
| **Drought Severity Index**          | USDA/NOAA (USDM)           | GeoTIFF (COG) | ~5 km grid    | 2000–2025         | `data/processed/hazards/drought_index_2000_2025.tif`           |

**CRS:** EPSG:4326 (WGS84) for all vector assets.
**STAC registry:** `data/stac/hazards/`

---

## 💾 STAC Item (Example)

```json
{
  "stac_version": "1.0.0",
  "type": "Feature",
  "id": "tornado_tracks_1950_2024",
  "collection": "hazards",
  "properties": {
    "title": "Kansas Tornado Tracks (1950–2024)",
    "description": "All recorded tornado tracks in Kansas from the NOAA Storm Prediction Center database.",
    "start_datetime": "1950-01-01T00:00:00Z",
    "end_datetime": "2024-12-31T23:59:59Z",
    "proj:epsg": 4326,
    "kfm:themes": ["hazards", "tornado", "severe_weather"],
    "license": "Public Domain",
    "providers": [
      {"name": "NOAA Storm Prediction Center", "roles": ["producer", "licensor"]},
      {"name": "Kansas Frontier Matrix", "roles": ["processor", "curator"]}
    ]
  },
  "geometry": null,
  "bbox": [-102.05, 36.99, -94.59, 40.00],
  "assets": {
    "data": {
      "href": "../../processed/hazards/tornado_tracks_1950_2024.geojson",
      "type": "application/geo+json",
      "roles": ["data"]
    },
    "thumbnail": {
      "href": "../thumbnails/tornado_tracks_1950_2024.png",
      "type": "image/png",
      "roles": ["thumbnail"]
    },
    "checksum": {
      "href": "../checksums/tornado_tracks_1950_2024.geojson.sha256",
      "type": "text/plain",
      "roles": ["metadata"]
    }
  },
  "links": [
    {"rel": "collection", "href": "./hazards-collection.json", "type": "application/json"}
  ]
}
```

---

## 🧩 Semantic & Ontological Alignment

| Entity        | Mapping (CIDOC CRM / OWL-Time)        | Example                            |
| :------------ | :------------------------------------ | :--------------------------------- |
| Tornado Track | `E5_Event` @ `E53_Place` (path)       | EF-4 near Greensburg, 2007         |
| Flood Event   | `E5_Event` + `P7_took_place_at`       | 1951 Kansas River Flood            |
| Wildfire      | `E5_Event` + `E26_Physical_Feature`   | 2022 Clark County wildfire         |
| Drought Index | `E16_Measurement` + OWL-Time Interval | USDM 2012 statewide severe drought |

These mappings allow direct **entity linking in Neo4j** and temporal reasoning across hazards ↔ hydrology ↔ climate.

---

## ⚙️ ETL & Processing Workflow

**Entry point:** `make hazards` → `src/pipelines/hazards/hazards_pipeline.py`

**Dependencies:** `geopandas`, `pandas`, `numpy`, `rasterio`, `rio-cogeo`, `pyproj`, `requests`

**Steps:**

1. **Fetch** from NOAA/FEMA/USGS/USDM APIs or source archives
2. **Normalize** attributes (date, type, intensity, area)
3. **Reproject** to EPSG:4326; vectors → **GeoJSON**, rasters → **COG**
4. **Summarize** per-event stats (EF scale, flood stage, burn area, drought class)
5. **Generate** thumbnails (static PNGs) for UI previews
6. **Emit** STAC items/collection under `data/processed/metadata/hazards/stac/`
7. **Compute** SHA-256 checksums under `checksums/`
8. **Validate** JSON Schema + STAC in CI (failing builds block merges)

---

## 🧮 Provenance & Validation

* **Checksums:** `.sha256` accompany all processed assets
* **Licensing:** Upstream data typically **Public Domain** (NOAA/USGS). Derived composites default **CC-BY 4.0**
* **Validation:** JSON Schema + STAC 1.0 via CI (see workflow badges)
* **Provenance Manifests:** `data/sources/hazards/*.json` (URL, license, version, retrieved_at)

---

## 🔗 Integration Points

| Component                    | Role                                                  |
| :--------------------------- | :---------------------------------------------------- |
| `data/stac/hazards/`         | Discoverable STAC Items/Collections for hazards       |
| `web/config/layers.json`     | Frontend layer configuration (opacity, style, legend) |
| `src/graph/hazards_nodes.py` | Neo4j bindings (People/Places/Events, time intervals) |
| `docs/architecture.md`       | System diagrams & pipeline narratives                 |
| `data/processed/hydrology/`  | Hydrologic context (floodplains, flow acc/dir)        |

---

## 🧠 MCP Compliance Summary

| MCP Principle           | Implementation                                     |
| :---------------------- | :------------------------------------------------- |
| **Documentation-first** | This README + dataset **cards** and **STAC** items |
| **Reproducibility**     | Deterministic `make hazards` + pinned env          |
| **Open Standards**      | GeoJSON, GeoTIFF (COG), CSV, STAC                  |
| **Provenance**          | Source manifests + SHA-256 checksums               |
| **Auditability**        | CI checks (STAC/Schema), reviewable PR templates   |

---

## 🧭 Architecture (Mermaid-safe)

```mermaid
flowchart TD
  A["Sources\n(NOAA · USGS · FEMA · USDM)"] --> B["ETL\n(fetch · normalize · reproj)"]
  B --> C["Processed\nGeoJSON · COG + checksums"]
  C --> D["STAC\nitems · collection"]
  D --> E["Graph/API\nNeo4j · FastAPI"]
  E --> F["Web UI\nMapLibre layers · Thumbnails"]
<!-- END OF MERMAID -->
```

```mermaid
sequenceDiagram
  participant S as Sources
  participant P as Pipeline
  participant V as Validators
  participant G as Graph/API
  participant W as Web UI

  S->>P: Pull hazards (NOAA/USGS/FEMA/USDM)
  P->>P: Normalize + EPSG:4326 + GeoJSON/COG
  P->>V: STAC + JSON Schema validate
  P->>G: Upsert entities (Events, Places, Intervals)
  W->>G: Query items + entities for map & timeline
<!-- END OF MERMAID -->
```

> **Mermaid rules:** quote labels with punctuation, use `\n` for line breaks, and always end with `<!-- END OF MERMAID -->`.

---

## 📦 AI/Graph Bindings (Examples)

* **Entity IDs (Graph):**
  `event:Tornado_2007_Greensburg` · `place:Kansas_River` · `interval:1951-Flood`
* **API patterns (FastAPI):**
  `/events?type=tornado&start=1950-01-01&end=2024-12-31&bbox=<...>`
  `/entity/{id}` → returns node + linked STAC items
* **NLP enrichment:** summaries per event; entity linking to counties/places; severity bucketing for UI legends.

---

## 📅 Version History (Summary)

| Version | Date       | Summary                                                                                                      |
| :------ | :--------- | :----------------------------------------------------------------------------------------------------------- |
| v1.1.0  | 2025-10-11 | Added **schema/**, **cards/**, **checksums/** folders; expanded **STAC example**; added **Mermaid sequence** |
| v1.0.0  | 2025-10-04 | Initial hazards metadata release (tornado, flood, wildfire, drought)                                         |

> Full details in [`CHANGELOG.md`](./CHANGELOG.md).

---

## 📎 References

* NOAA Storm Events Database — [https://www.ncei.noaa.gov/stormevents/](https://www.ncei.noaa.gov/stormevents/)
* FEMA Disaster Declarations Summaries — [https://www.fema.gov/openfema-data-page/disaster-declarations-summaries-v2](https://www.fema.gov/openfema-data-page/disaster-declarations-summaries-v2)
* USGS Wildland Fire Science Program — [https://www.usgs.gov/programs/wildland-fire-science-program](https://www.usgs.gov/programs/wildland-fire-science-program)
* U.S. Drought Monitor (USDM) — [https://droughtmonitor.unl.edu/](https://droughtmonitor.unl.edu/)
* MCP Templates — `docs/templates/`

---

<div align="center">

**Kansas Frontier Matrix** — *“Mapping the footprints of disaster across time.”*
📍 [`data/processed/metadata/hazards/`](.)

</div>
```
