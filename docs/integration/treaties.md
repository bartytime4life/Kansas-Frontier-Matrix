<div align="center">

# 🕊️ Kansas Frontier Matrix — Treaty & Land Cession Integration  
`docs/integration/treaties.md`

**Mission:** Integrate, visualize, and contextualize **Kansas’s 19th-century treaties and land cessions**, connecting  
archival treaty texts, scanned maps, and geospatial boundary data into the **interactive timeline · map · knowledge graph**  
of the **Kansas Frontier Matrix (KFM)** — ensuring these historical land transformations are **searchable, reproducible, and narratively accessible**.

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../.github/workflows/site.yml)
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](../../.github/workflows/stac-validate.yml)
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](../../.github/workflows/codeql.yml)
[![Trivy Security](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](../../.github/workflows/trivy.yml)
[![Docs · MCP-DL v6.3](https://img.shields.io/badge/Docs-MCP--DL%20v6.3-blue)](../)
[![Ontology · CIDOC CRM](https://img.shields.io/badge/Ontology-CIDOC%20CRM%20%7C%20OWL--Time%20%7C%20DCAT-orange)](../../docs/standards/ontologies.md)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../LICENSE)

</div>

---

## 📚 Overview

This document defines how **treaty and land-cession datasets** are discovered, standardized, and integrated into the  
Kansas Frontier Matrix. It merges **treaty transcripts**, **Royce-polygon boundary data**, and **AI-extracted metadata**  
to reconstruct how Indigenous territories were ceded or transformed through 19th-century negotiations.  

The result: a **dynamic, time-aware treaty layer** rendered on KFM’s map and timeline — each polygon, document, and date  
linked semantically in the **Neo4j knowledge graph** and discoverable via **AI Focus Mode** (tribe, treaty, or place-centered queries).

---

## 🧭 Historical Context

From the early 1820s to the late 1870s, Kansas’s land changed dramatically through a series of treaties.  

| Year | Treaty / Act | Involved Nations | Description |
|:----:|:--------------|:----------------|:-------------|
| 1825 | Treaty with the Kansa (Kaw) | Kaw (Kansa) Nation, U.S. | Ceded most Kaw homelands along the Kansas River. |
| 1825 | Treaty with the Great & Little Osage | Osage Nations, U.S. | Established western Missouri & SE Kansas boundary. |
| 1835 | Cherokee Outlet Agreement | Cherokee Nation | Defined southern “Cherokee Neutral Lands.” |
| 1854 | Kansas–Nebraska Act (contextual) | — | Opened the territory to settlers; catalyzed new treaties. |
| 1867 | Medicine Lodge Creek Treaties | Kiowa, Comanche, Apache, Cheyenne, Arapaho | Relocated Plains tribes to Indian Territory (Oklahoma). |

Each treaty is tied to:
- **Textual records** — Kappler’s *Indian Affairs: Laws and Treaties*; Yale Avalon Project; NARA and LOC archives.  
- **Mapped cessions** — *Royce polygons* digitized by the U.S. Forest Service and Bureau of Indian Affairs.  
- **Contextual events** — migrations, forts, trails, ecological shifts, and legislation connected to these agreements.

---

## ⚙️ Integration Workflow

```mermaid
flowchart TD
    A["Treaty Texts\nKappler / Avalon / NARA / OHS"] --> B["NLP Parsing\nspaCy · HuggingFace · Entity Linking"]
    A2["Royce / USFS Cession Maps\n(ArcGIS / GeoJSON)"] --> C["Geospatial Processing\nReproject → GeoJSON / COG"]
    B --> D["Entity Alignment\nTribes ↔ Places ↔ Dates ↔ Signatories"]
    C --> D
    D --> E["Knowledge Graph\nNeo4j · CIDOC CRM · OWL-Time"]
    E --> F["STAC & DCAT Catalog\nMetadata + Provenance"]
    F --> G["Frontend\nMapLibre · Timeline · Focus Mode"]
````

<!-- END OF MERMAID -->

---

### 🧩 Step-by-Step Process

#### 1. 🧭 Source Discovery

* **Textual Treaties:** Kappler’s *Indian Affairs*, Avalon Project (Yale Law), Oklahoma Historical Society, and NARA.
* **Geospatial Layers:** U.S. Forest Service *Indian Land Cessions 1784–1894* ArcGIS Feature Layer (Royce polygons).
* **Supplemental Sources:** Native Land Digital API (modern boundaries), LandMark Global Portal (community lands).

#### 2. 🧾 Data Extraction

* Filter USFS dataset by `STATE = 'Kansas'`.
* Download shapefiles → `data/raw/treaties/royce_kansas.zip`.
* Export treaty texts (TXT/PDF), apply OCR using Tesseract if scanned.
* Normalize attribute fields: `TREATY`, `YEAR`, `TRIBE`, `ROYCE_NO`, `SOURCE_URL`.

#### 3. 🧮 Processing & Standardization

* Convert shapefiles to GeoJSON in WGS84 projection:

  ```bash
  ogr2ogr -f GeoJSON -t_srs EPSG:4326 data/processed/treaties/royce_kansas.geojson royce_kansas.shp
  ```
* Generate Cloud-Optimized GeoTIFF overlays (COG) for archival map visualization.
* Apply **NLP (spaCy + transformers)** to extract structured data:

  * `ORG` → tribal nations
  * `GPE` → geographic references
  * `DATE` → treaty signing and ratification dates
  * `PERSON` → signatories and negotiators

#### 4. 🧠 Graph Integration

The knowledge graph connects treaties, tribes, places, and temporal events:

```text
(Treaty)-[:INVOLVES]->(Tribe)
(Treaty)-[:CEDES]->(Boundary)
(Boundary)-[:LOCATED_IN]->(Place)
(Treaty)-[:SIGNED_AT]->(Place)
(Treaty)-[:OCCURRED_ON]->(Date)
(Document)-[:MENTIONS]->(Treaty)
```

Each edge carries provenance metadata (source, confidence, date of extraction).
CIDOC CRM classes and OWL-Time entities ensure temporal precision and semantic reasoning.

#### 5. 🗂️ Catalog & Layer Registration

**STAC Item:** `data/stac/treaties_royce.json`

```json
{
  "id": "treaties_royce",
  "title": "Indian Land Cessions in Kansas (Royce Polygons)",
  "temporal": {"start": "1820-01-01", "end": "1875-12-31"},
  "assets": {
    "data": {"href": "data/processed/treaties/royce_kansas.geojson", "type": "application/geo+json"}
  },
  "keywords": ["treaty","cession","tribal lands","Kansas"],
  "license": "Public Domain (U.S. Government)",
  "provenance": "U.S. Forest Service · Kappler · Avalon · KFM ETL v6.3"
}
```

**Layer Entry:** `web/config/layers.json`

```json
{
  "id": "treaties",
  "title": "Treaty & Land Cession Boundaries (1820–1870)",
  "type": "vector",
  "source": "data/processed/treaties/royce_kansas.geojson",
  "color": "#c77d02",
  "opacity": 0.6,
  "timeline": true,
  "focusable": true
}
```

#### 6. 🗺️ Frontend Visualization

* MapLibre renders translucent polygons overlaying the modern basemap.
* Timeline slider filters polygons by treaty year.
* Clicking a polygon triggers the **AI Focus Mode**:

  * Displays treaty summary, participating tribes, signatories, and linked events.
  * Offers “Before/After” overlays (pre-cession vs post-cession lands).
* Optional layer blending with **Native Land Digital** or **LandMark Global** data for comparative context.

---

## 🧩 Knowledge Graph Schema (CIDOC CRM Alignment)

| Entity       | CIDOC Class                | Example                             |
| :----------- | :------------------------- | :---------------------------------- |
| Treaty       | E7 Activity / E65 Creation | “Treaty with the Kansa (1825)”      |
| Tribe        | E74 Group                  | “Osage Nation”                      |
| Boundary     | E53 Place                  | Royce polygon geometry              |
| Signatory    | E39 Actor                  | “William Clark”                     |
| Document     | E31 Document               | Kappler’s *Treaty No. 116*          |
| Date         | E52 Time-Span              | 1825-06-03                          |
| Fort / Place | E53 Place                  | “Fort Larned” (location of signing) |

---

## 🧪 Validation & Reproducibility

| Validation Step     | Tool/Standard        | Description                                                   |
| :------------------ | :------------------- | :------------------------------------------------------------ |
| File Integrity      | SHA-256              | Every raw/processed file hashed for verification.             |
| Schema Compliance   | JSON Schema / STAC   | CI checks metadata and format.                                |
| Provenance Tracking | DCAT 2.0             | Dataset lineage recorded in catalog entries.                  |
| Ontology Check      | CIDOC CRM + OWL-Time | Validates semantic structure of relationships.                |
| Documentation       | MCP Experiment Log   | `docs/experiment/treaty_ingest.md` documents reproducibility. |

---

## 🌍 Future Enhancements

* **Oral Histories Integration:** Link tribal oral history datasets and Indigenous community archives.
* **Animated Timeline:** Temporal morphing of cession boundaries (e.g., 1820 → 1870 playback).
* **AI Narrative Generator:** Summarize each treaty’s context and aftermath in plain language.
* **Comparative Layers:** Overlay pre-treaty ecological maps or settlement data to visualize impacts.
* **Ethical Framework:** Collaborate with tribal nations to review representation and data use.

---

## 🔗 References & Data Sources

* Kappler, *Indian Affairs: Laws and Treaties* (1904–1979).
* U.S. Forest Service – *Indian Land Cessions in the United States, 1784–1894* (Royce polygons).
* Yale Law Avalon Project – *Treaties between the U.S. and Native Nations*.
* Native Land Digital (CC0 API) – Indigenous territories, languages, and treaties.
* LandMark Global Platform (CC-BY-SA 4.0).
* National Archives, Kansas Historical Society digital collections, and Library of Congress.

---

<div align="center">

### 🕰️ “Every boundary tells a story — this layer lets Kansas’s borders speak.”

**— Kansas Frontier Matrix Team · MCP-DL v6.3**

</div>
