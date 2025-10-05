<div align="center">

# 🕊️ Kansas Frontier Matrix — Treaty & Land Cession Integration  
`docs/integration/treaties.md`

**Mission:** Integrate and contextualize **Kansas’s 19th-century treaties and land cessions** — connecting  
historical agreements, boundary maps, and related documents into the **interactive timeline + map +  
knowledge graph** framework of the **Kansas Frontier Matrix (KFM)**.

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../.github/workflows/site.yml)
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](../../.github/workflows/stac-validate.yml)
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](../../.github/workflows/codeql.yml)
[![Trivy Security](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](../../.github/workflows/trivy.yml)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../LICENSE)

</div>

---

## 📜 Overview

This document explains how **treaty and land-cession data** are incorporated into the Kansas Frontier Matrix.  
It combines historical treaty transcripts, geospatial boundary data, and metadata to represent the  
progressive transformation of Kansas’s lands through the 19th century.  

The result: a **time-aware treaty layer** displayed on the Frontier Matrix map and timeline, with linked
entities (tribes, signatories, forts, rivers) and provenance stored in the knowledge graph.

---

## 🧭 Historical Context

Between 1820 and 1870, dozens of treaties transformed the lands that became Kansas. Key examples:

| Year | Treaty / Act | Involved Nations | Description |
|:----:|:--------------|:----------------|:-------------|
| 1825 | Kansa (Kaw) Treaty | Kaw (Kansa) Nation, U.S. | Ceded most Kaw homelands along the Kansas River. |
| 1825 | Osage Treaty | Great & Little Osage | Established western Missouri & SE Kansas boundary. |
| 1835 | Cherokee Outlet Agreement | Cherokee Nation | Defined the southern “Cherokee Neutral Lands.” |
| 1854 | Kansas-Nebraska Act (contextual) | — | Opened territories to settlement; framed later treaties. |
| 1867 | Medicine Lodge Creek Treaties | Kiowa, Comanche, Apache, Cheyenne, Arapaho | Relocated Plains tribes to Indian Territory (OK). |

Each treaty typically has **textual documentation (Kappler’s _Indian Affairs: Laws and Treaties_)** and  
**mapped boundaries (Royce polygons)** digitized by the U.S. Forest Service and National Archives.

---

## ⚙️ Integration Workflow

```mermaid
flowchart TD
    A["Treaty Texts\nKappler / Avalon / LOC"] --> B["NLP Parsing\nNER · date · tribe · place"]
    A2["Cession Maps\nUSFS / BIA / Royce shapefiles"] --> C["Geospatial Processing\nreproject → GeoJSON"]
    B --> D["Entity Linking\nTribes ↔ Places ↔ Dates"]
    C --> D
    D --> E["Knowledge Graph\nNeo4j · CIDOC CRM"]
    E --> F["STAC Catalog & Layers.json\nTreaties GeoJSON · metadata.json"]
    F --> G["Frontend\nMap overlay · Timeline event nodes"]
````

<!-- END OF MERMAID -->

---

### Step-by-Step

1. **Source Discovery**

   * Texts: Kappler’s *Indian Affairs: Laws and Treaties*, Yale Avalon Project, Oklahoma Historical Society.
   * Maps: U.S. Forest Service *Indian Land Cessions 1784–1894* (Royce polygons) — ArcGIS Feature Layer.

2. **Data Extraction**

   * Filter U.S. Forest Service data by `STATE = 'Kansas'`.
   * Save raw files under `data/raw/treaties/royce_kansas.zip`.
   * Export treaty texts as TXT/PDF and OCR if necessary.

3. **Processing**

   * **Vector conversion**

     ```bash
     ogr2ogr -f GeoJSON -t_srs EPSG:4326 data/processed/treaties/royce_kansas.geojson royce_kansas.shp
     ```
   * Keep attributes: `TREATY`, `YEAR`, `TRIBE`, `ROYCE_NO`, `SOURCE_URL`.
   * Run NLP (spaCy) to extract entities from treaty text (tribes, places, dates, signatories).

4. **Graph Integration**

   ```text
   (Treaty)-[:INVOLVES]->(Tribe)
   (Treaty)-[:CEDES]->(Boundary)
   (Boundary)-[:LOCATED_IN]->(Place)
   (Treaty)-[:SIGNED_AT]->(Place)
   (Treaty)-[:OCCURRED_ON]->(Date)
   ```

   Each relationship includes provenance and confidence attributes.

5. **Catalog & Layer Registration**
   Example STAC item (`data/stac/treaties_royce.json`):

   ```json
   {
     "id": "treaties_royce",
     "title": "Indian Land Cessions in Kansas (Royce Polygons)",
     "temporal": {"start": "1820-01-01", "end": "1875-12-31"},
     "assets": {
       "data": {
         "href": "data/processed/treaties/royce_kansas.geojson",
         "type": "application/geo+json"
       }
     },
     "keywords": ["treaty", "cession", "tribal lands", "Kansas"],
     "license": "Public Domain (US Government)"
   }
   ```

   Layer entry (`web/config/layers.json`):

   ```json
   {
     "id": "treaties",
     "title": "Treaty & Land Cession Boundaries (1820–1870)",
     "type": "vector",
     "source": "data/processed/treaties/royce_kansas.geojson",
     "color": "#c77d02",
     "opacity": 0.6,
     "timeline": true
   }
   ```

6. **Frontend Visualization**

   * Semi-transparent polygons overlay the base map.
   * Timeline slider filters features by `YEAR`.
   * Clicking a polygon opens a side panel with treaty name, tribes, signatories, and AI summary.

---

## 🧩 Knowledge Graph Schema (CIDOC CRM Alignment)

| Entity    | CIDOC Class                | Example                        |
| :-------- | :------------------------- | :----------------------------- |
| Treaty    | E7 Activity / E65 Creation | “Treaty with the Kansa (1825)” |
| Tribe     | E74 Group                  | “Osage Nation”                 |
| Boundary  | E53 Place                  | Royce polygon geometry         |
| Signatory | E39 Actor                  | “William Clark”                |
| Document  | E31 Document               | Scanned treaty text            |
| Date      | E52 Time-Span              | 1825-06-03                     |

---

## 🧮 Validation & Reproducibility

* `.sha256` checksum for every downloaded file.
* JSON Schema + STAC validation in CI.
* Document ETL steps under `docs/experiment/treaty_ingest.md`.
* Treaties and maps are U.S. Government works → Public Domain.

---

## 🌍 Future Enhancements

* Integrate **tribal oral histories** and community datasets.
* Animate **time-lapse treaty boundaries** on the timeline.
* Add **AI-generated narrative summaries** for each treaty.
* Compare **pre/post-cession landscapes** (e.g., 1850 vs 1870).

---

<div align="center">

### 🕰️ “Every boundary tells a story — this layer lets Kansas’s borders speak.”

**— Kansas Frontier Matrix Team**

</div>
