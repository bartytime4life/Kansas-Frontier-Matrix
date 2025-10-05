<div align="center">

# 🕊️ Kansas Frontier Matrix — Treaty & Land Cession Integration  
`docs/integration/treaties.md`

**Mission:** Integrate **treaty, land cession, and reservation boundary data** into the  
**Kansas Frontier Matrix (KFM)** — ensuring historical accuracy, STAC compliance, and  
semantic linkage between textual treaty sources and geospatial boundaries.

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../.github/workflows/site.yml)  
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](../../.github/workflows/stac-validate.yml)  
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](../../.github/workflows/codeql.yml)  
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../)  
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../LICENSE)

</div>

---

## 📜 Overview

The **Treaty & Land Cession Integration Module** connects textual treaty data  
(e.g., *Kappler’s Indian Affairs: Laws and Treaties*, Yale Avalon Project, National Archives*)  
with **geospatial polygon layers** representing historical boundaries and cession areas.  
These datasets form the foundation for understanding **territorial change and Indigenous land history**  
within Kansas and the wider Great Plains.

The goal is to synchronize:
- **Textual sources** → treaty names, signatories, dates, and clauses.  
- **Spatial data** → cession polygons, reservation boundaries, and place names.  
- **Semantic structure** → relationships (Tribe ↔ Treaty ↔ Land Area ↔ Modern County).

All layers are fully **FAIR** (Findable, Accessible, Interoperable, Reproducible) and linked  
to the knowledge graph (Neo4j / CIDOC CRM ontology).

---

## 🗺️ Data Sources

| Dataset | Description | Format | Coverage | License |
|:--------|:-------------|:--------|:----------|:----------|
| **Indian Land Cessions (Royce Maps)** | Digitized boundaries of all U.S. Indian land cessions (1784–1911) published in *U.S. Bureau of Ethnology Annual Report, Vol. 18* (1899). | Shapefile, GeoJSON | Continental U.S. (includes all Kansas treaties) | Public Domain |
| **Kappler’s Indian Affairs: Laws & Treaties** | Texts of treaties (1778–1883). Full searchable corpus available via Oklahoma State University Digital Library and Avalon Project. | HTML, PDF, TXT | National (multi-tribal) | Public Domain |
| **National Atlas / USFS Land Cession GIS Dataset** | Federal digitization of the Royce Maps by the U.S. Forest Service. Includes attributes: `tribe`, `treaty_date`, `cession_id`, `royce_num`. | Feature Layer (ArcGIS, WMS, GeoJSON) | U.S., Kansas subset used | CC0 |
| **Tribal Nations Boundaries (BIA / TIGER)** | Modern federally recognized tribal lands for reference and overlay comparison. | Shapefile / GeoJSON | U.S. (CONUS) | Public Domain |
| **Kansas Historical Society Treaties Index** | Local index of treaties relevant to Kansas tribes (Kansa, Osage, Pawnee, Shawnee, etc.). | CSV / Web | Kansas | CC-BY 4.0 |

---

## 🧩 Integration Workflow

## 1️⃣ Extract

- Download or access the USFS Indian Land Cessions GIS layer via ArcGIS REST:
  ```bash
  ogr2ogr -f GeoJSON kansas_treaties.json \
    "https://services.arcgis.com/P3ePLMYs2RVChkJx/arcgis/rest/services/Indian_Land_Cessions/FeatureServer/0"
````

* Fetch treaty texts from Kappler/Avalon:

  ```bash
  python scripts/fetch_treaties.py --source "avalon" --year 1867
  ```

---

## 2️⃣ Transform

* Normalize fields → `treaty_name`, `tribe`, `date_signed`, `royce_id`, `geometry`.
* Convert geometries to **EPSG:4326** and output as **GeoJSON** or **COG GeoTIFFs** (for raster overlays).
* Use `data/sources/treaties.json` as a **manifest** with metadata:

  ```json
  {
    "id": "ks_treaties_1850_1870",
    "title": "Kansas Treaties and Land Cessions (1850–1870)",
    "type": "vector",
    "spatial": { "bbox": [-102.05, 36.99, -94.6, 40.0], "crs": "EPSG:4326" },
    "temporal": { "start": "1850-01-01", "end": "1870-12-31" },
    "license": "Public Domain",
    "source": "USFS Indian Land Cessions, Kappler's Indian Affairs",
    "outputs": { "geojson": "data/processed/ks_treaties_1850_1870.geojson" }
  }
  ```

---

## 3️⃣ Load

* Run ETL:

  ```bash
  make treaties
  ```

  This task:

  * Imports polygons into the Neo4j knowledge graph.
  * Links treaty text entries to spatial polygons.
  * Writes STAC metadata under `data/stac/treaties/`.

---

## 🕸️ Knowledge Graph Mapping

| Concept                     | CIDOC CRM Class                  | Example                         |
| :-------------------------- | :------------------------------- | :------------------------------ |
| **Treaty**                  | `E7_Activity`                    | “Treaty of Fort Laramie (1851)” |
| **Tribe / Nation**          | `E74_Group`                      | “Osage Nation”                  |
| **Land Cession**            | `E53_Place` + geometry           | Royce Area 257                  |
| **Signatory**               | `E39_Actor`                      | “Chief Pawhuska”                |
| **Date Signed**             | `E52_Time-Span`                  | 1867-10-21                      |
| **Text Reference**          | `E33_Linguistic_Object`          | Treaty article text             |
| **Modern County / Overlay** | `E53_Place` (`P89_falls_within`) | Douglas County, KS              |

These mappings enable semantic linking between textual, spatial, and temporal data in the knowledge graph.

---

## 🧠 AI / NLP Integration

## Named Entity Recognition (NER)

* Detect entities: `PERSON`, `ORG`, `DATE`, `LOC`, `LAW`.
* Example Input:

  ```
  "Articles of a treaty made and concluded at the Osage Agency, Kansas, October 29, 1865"
  ```

  Output Entities:

  * `Treaty`: *Osage Agency Treaty (1865)*
  * `Place`: *Osage Agency, Kansas*
  * `Date`: *1865-10-29*

## Entity Linking & Summarization

* Automatically link mentions to the correct treaty node in Neo4j using context scoring.
* Generate 2–3 sentence treaty abstracts (BART/T5 transformers) for map UI popups and timeline.

---

## 🌐 STAC Catalog Example

```json
{
  "stac_version": "1.0.0",
  "type": "Feature",
  "id": "treaty_royce_257",
  "properties": {
    "title": "Treaty of Fort Laramie (1851) — Royce 257",
    "datetime": "1851-09-17",
    "tribe": ["Cheyenne", "Arapaho", "Sioux"],
    "license": "Public Domain"
  },
  "assets": {
    "data": {
      "href": "https://data.kansasfrontier.org/processed/royce_257.geojson",
      "type": "application/geo+json",
      "roles": ["data"]
    }
  },
  "bbox": [-102.05, 36.99, -94.6, 40.0],
  "geometry": { "type": "Polygon", "coordinates": [...] }
}
```

---

## 🧭 Visualization in Web UI

## MapLibre Layer Definition

```json
{
  "id": "treaties",
  "type": "fill",
  "source": "data/stac/treaties/index.json",
  "paint": { "fill-color": "#de8f5f", "fill-opacity": 0.5 },
  "layout": { "visibility": "visible" }
}
```

## Timeline & Popups

* Each treaty’s date appears as a timeline marker.
* Hover tooltips: treaty name + tribes involved.
* Popup contents:

  * AI-generated summary
  * Linked text excerpt (Kappler or Avalon)
  * Links: *View full treaty text* / *Compare boundary change*

---

## ⚙️ Validation & Quality Control

| Check                   | Method                         | Tool              |
| :---------------------- | :----------------------------- | :---------------- |
| **Geometry validity**   | `ogrinfo`, `geojsonhint`       | GDAL, geojsonhint |
| **STAC compliance**     | `stac-validator`               | GitHub CI         |
| **CRS consistency**     | `gdalinfo`                     | GDAL              |
| **Metadata schema**     | JSON Schema validation         | MCP Rules         |
| **Semantic link check** | Graph query for orphaned nodes | Neo4j Cypher      |

---

## 🪶 Future Enhancements

* Integrate **oral history records** from tribes linked to each treaty.
* Add **treaty impact analysis**: visualize land lost / retained over time.
* Connect **signatories → biographies** for network visualization.
* Enable **AI Q&A**: *“Show all treaties involving the Kansa Nation after 1850.”*

---

## 📚 References

* U.S. Forest Service — *Indian Land Cessions in the United States, 1784–1911 (GIS Dataset)*
* Kappler, Charles J. — *Indian Affairs: Laws and Treaties*, Vols. I–II (1904)
* Yale Avalon Project — *Treaties Between the U.S. and Native Americans*
* Kansas Historical Society Digital Archives
* CIDOC CRM / OWL-Time Ontologies
* [PeriodO Gazetteer of Historical Periods](https://perio.do/)

---

<div align="center">

**Kansas Frontier Matrix** — *Documenting the intersections of history, land, and culture.*
🧭 *“Every boundary tells a story.”*

</div>
