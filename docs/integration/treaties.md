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

This module describes how **treaty and land-cession data** is integrated into the Kansas Frontier Matrix.  
It links textual treaty transcripts, spatial boundaries, and associated entities (tribes, signatories, forts, rivers)  
into the **knowledge graph** and **map-timeline viewer**.

Treaty data bridges **historical documentation** and **geospatial representation**, forming a temporal layer  
that shows how land ownership and sovereignty evolved from pre-statehood to modern Kansas.

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

flowchart TD
  A["Treaty Texts<br/>Kappler / Avalon / LOC"] --> B["NLP Parsing<br/>NER · date · tribe · place"]
  A2["Cession Maps<br/>USFS / BIA / Royce shapefiles"] --> C["Geospatial Processing<br/>reproject → GeoJSON"]
  B --> D["Entity Linking<br/>Tribes ↔ Places ↔ Dates"]
  C --> D
  D --> E["Knowledge Graph<br/>Neo4j · CIDOC CRM"]
  E --> F["STAC Catalog & Layers.json<br/>treaties.geojson · metadata.json"]
  F --> G["Frontend<br/>Map overlay · Timeline event nodes"]

<!-- END OF MERMAID -->

### Step-by-Step

1. **Source Discovery**
   - Texts: Kappler’s *Indian Affairs: Laws and Treaties*, Yale Avalon Project, Oklahoma Historical Society.  
   - Maps: USFS *Indian Land Cessions 1784–1894* (Royce polygons) — available as ArcGIS Feature Layer.

2. **Data Extraction**
   - Download GIS layer for Kansas region (filter by `STATE = 'Kansas'` in USFS dataset).  
   - Save under `data/raw/treaties/royce_kansas.zip` (or similar).  
   - Fetch textual treaties via API or manual archive export; convert to text/PDF.

3. **Processing**
   - **Vector conversion:**  
     ```bash
     ogr2ogr -f GeoJSON -t_srs EPSG:4326 data/processed/treaties/royce_kansas.geojson royce_kansas.shp
     ```
   - **Attribute cleaning:** retain key fields:
     `TREATY`, `YEAR`, `TRIBE`, `ROYCE_NO`, `SOURCE_URL`.
   - **Text NLP:** use spaCy NER to extract entities from treaty text (tribes, places, dates, signatories).  
     Each recognized entity is stored in the graph with provenance links.

4. **Graph Integration**
   - Create nodes: `Treaty`, `Tribe`, `Place`, `Boundary`.  
   - Relationships:
     ```
     (Treaty)-[:INVOLVES]->(Tribe)
     (Treaty)-[:CEDES]->(Boundary)
     (Boundary)-[:LOCATED_IN]->(Place)
     (Treaty)-[:SIGNED_AT]->(Place)
     (Treaty)-[:OCCURRED_ON]->(Date)
     ```
   - Provenance and confidence values are stored on each edge.

5. **Catalog + Layer Registration**
   - Add a STAC Item under `data/stac/treaties_royce.json`:
     ```json
     {
       "id": "treaties_royce",
       "type": "FeatureCollection",
       "title": "Indian Land Cessions in Kansas (Royce Polygons)",
       "temporal": {"start": "1820-01-01", "end": "1875-12-31"},
       "assets": {"data": {"href": "data/processed/treaties/royce_kansas.geojson"}},
       "keywords": ["treaty", "cession", "tribal lands", "Kansas"],
       "license": "Public Domain (US Government)",
       "links": [{"rel": "source", "href": "https://data.fs.usda.gov/geodata/otherprojects/indianlands/"}]
     }
     ```
   - Reference this item in `web/config/layers.json`:
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
   - Boundaries appear as semi-transparent polygons over the base map.  
   - Timeline slider filters polygons by `YEAR` attribute.  
   - Clicking a polygon opens a side panel with treaty name, signatories, linked tribes, and AI summary.  
   - Optional: overlay treaty text excerpts or scanned signatures.

---

## 🧩 Knowledge Graph Schema (CIDOC CRM Alignment)

| Entity | CIDOC Class | Example |
|:-------|:-------------|:---------|
| Treaty | E7 Activity / E65 Creation | “Treaty with the Kansa (1825)” |
| Tribe | E74 Group | “Osage Nation” |
| Boundary | E53 Place | Polygon geometry from Royce map |
| Signatory | E39 Actor | “William Clark” |
| Document | E31 Document | Scanned treaty text |
| Date | E52 Time-Span | 1825-06-03 |

Relationships align with CIDOC CRM semantics (e.g., `P94 has_created`, `P7 took_place_at`).  
This enables semantic interoperability and linkage to external heritage databases.

---

## 🧮 Validation & Reproducibility

- **Checksum verification:** `.sha256` sidecar for each downloaded file.  
- **Schema validation:** JSON Schema + STAC validation CI step ensures correct metadata.  
- **Documentation:** Every ETL step is logged under `docs/experiment/treaty_ingest.md` per MCP.  
- **Licensing:** All US Government datasets are public domain; cite original archival sources.

---

## 🌍 Future Enhancements

- Integrate **oral histories and tribal archives** for Indigenous perspectives on treaty impacts.  
- Add **interactive treaty timeline animations** (boundary dissolves and shifts).  
- Connect **AI narrative summaries** to each treaty for public storytelling.  
- Explore **comparative layers** (e.g., “pre- and post-cession lands,” “reservation boundaries 1870s”).

---

<div align="center">

### 🕰️ “Every boundary tells a story — this layer lets Kansas’s borders speak.”  
**— Kansas Frontier Matrix Team**

</div>
