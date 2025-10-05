<div align="center">

# 🌦️ Kansas Frontier Matrix — Climate & Hazard Data Integration

`docs/integration/climate-hazards.md`

**Purpose:** Define how **climate, weather, and natural hazard datasets**
(NOAA, FEMA, USGS, NASA) are integrated into the **Kansas Frontier Matrix (KFM)** system —
standardized for **reproducibility, interoperability, and semantic linkage** across history, geography, and ecology.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../)
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](../../.github/workflows/stac-validate.yml)
[![Climate Data](https://img.shields.io/badge/Data-NOAA%20%7C%20NASA%20%7C%20FEMA-green)](../../docs/standards/metadata.md)
[![Ontology](https://img.shields.io/badge/Ontology-CIDOC%20CRM%20%7C%20PROV--O%20%7C%20OWL--Time-orange)](../../docs/standards/ontologies.md)

</div>

---

## 🎯 Integration Objective

Integrate **historical and modern climate datasets** — including **temperature, precipitation, drought indices, floods, tornadoes, and disasters** — into KFM’s unified spatiotemporal knowledge system.
Each dataset becomes a **time-aware STAC item** and an **ontology-linked entity** within the Neo4j knowledge graph.

**Goals:**

* 🧩 Standardize climate & hazard data into **STAC-compliant GeoJSON and NetCDF metadata**.
* 🌍 Link events to **spatial regions (counties, watersheds)** and **temporal intervals (OWL-Time)**.
* 🧠 Enable **cross-domain reasoning** — e.g., linking droughts to migration, or tornadoes to county losses.
* 🧾 Maintain complete **provenance** via MCP logging, including file hashes and data source lineage.

---

## 🗂 Primary Data Sources

| Source                         | Type                                      | Coverage      | Access                                                        | License       |
| :----------------------------- | :---------------------------------------- | :------------ | :------------------------------------------------------------ | :------------ |
| **NOAA NCEI GHCN-Daily**       | Station weather (precip, temp, snowfall)  | 1880s–present | CSV/API ([NCEI](https://www.ncei.noaa.gov))                   | Public Domain |
| **NASA Daymet V4**             | Gridded daily climate data (1 km)         | 1980–present  | NetCDF ([Daymet API](https://daac.ornl.gov/DAYMET/))          | Public Domain |
| **NOAA Storm Events Database** | Storms, tornadoes, hail, floods, droughts | 1950–present  | CSV ([StormEvents](https://www.ncei.noaa.gov/stormevents/))   | Public Domain |
| **FEMA Disaster Declarations** | County-level disaster records             | 1953–present  | OpenFEMA API ([data.fema.gov](https://www.fema.gov/openfema)) | Public Domain |
| **USGS Flood Data (NWIS)**     | River gauge & flood discharge             | 1900–present  | API ([waterdata.usgs.gov](https://waterdata.usgs.gov/nwis))   | Public Domain |

---

## 🔄 Integration Workflow

```mermaid
flowchart TD
    A["🌐 Download Data<br/>NOAA • NASA • FEMA • USGS"] --> B["🧮 Normalize & Reproject<br/>CSV → GeoJSON → STAC"]
    B --> C["🧾 Generate Metadata<br/>License, temporal extent, variables"]
    C --> D["🧠 Ingest to Graph<br/>CIDOC CRM + PROV-O + OWL-Time"]
    D --> E["🗺️ Publish<br/>Interactive layers (timeline + map)"]
    style A fill:#eef7ff,stroke:#0077cc
    style B fill:#fff0f5,stroke:#cc0088
    style C fill:#ecf9f0,stroke:#33aa33
    style D fill:#fffbea,stroke:#e8a500
    style E fill:#f0e8ff,stroke:#8844cc
```

<!-- END OF MERMAID -->

---

## 🧩 Dataset Integration Procedures

### 1️⃣ NOAA NCEI GHCN-Daily (Station Weather)

* **Data:** Daily precipitation, min/max temp, snow, and wind.
* **Access:** NOAA API (`https://www.ncei.noaa.gov/cdo-web/api/v2/data`)
* **Transformation:**

  ```bash
  curl -o ks_ghcn_1880_2025.csv "https://www.ncei.noaa.gov/access/services/data/v1?dataset=ghcn-daily&startDate=1880-01-01&endDate=2025-01-01&stations=USW00003928"
  csvjson ks_ghcn_1880_2025.csv > data/processed/climate/ks_ghcn_1880_2025.json
  ```
* **Output:** CSV → GeoJSON point layer (station-based).
* **Ontology:**

  * `crm:E7_Activity` = Weather observation
  * `crm:E53_Place` = Station location
  * `time:Interval` = Observation period

---

### 2️⃣ NASA Daymet V4 (Gridded Climate)

* **Data:** Daily grids (1 km) for temp, precip, radiation.
* **Access:** ORNL DAAC API (`https://daac.ornl.gov/DAYMET/`)
* **Transformation:**

  ```bash
  nccopy -d5 -c "time/1,lat/240,lon/240" daymet_v4_daily_na_1980.nc data/processed/climate/daymet_ks_1980.nc
  gdalwarp -t_srs EPSG:4326 daymet_ks_1980.nc daymet_ks_1980.tif
  ```
* **Output:** NetCDF → GeoTIFF (COG).
* **Ontology:**

  * `crm:E73_Information_Object` = Raster dataset
  * `crm:E53_Place` = Kansas bounding box
  * `time:Interval` = Daily timeslices 1980–present

---

### 3️⃣ NOAA Storm Events Database

* **Data:** CSV of events with date, location, type, injuries, damages.
* **Transformation:**

  ```bash
  unzip StormEvents_1950_2025.zip -d data/raw/storms/
  csvcut -c BEGIN_YEARMONTH,STATE,EVENT_TYPE,INJURIES_DIRECT,DEATHS_DIRECT,BEGIN_LAT,BEGIN_LON \
  data/raw/storms/StormEvents_1950_2025.csv | csvjson > data/processed/hazards/storms_1950_2025.json
  ```
* **Graph Mapping:**

  * Each record → `crm:E5_Event`
  * Event location → `crm:E53_Place`
  * Date → `time:Instant`
  * Source → `prov:wasDerivedFrom NOAA StormEvents`

---

### 4️⃣ FEMA Disaster Declarations

* **Data:** County-level disaster history.
* **Access:** `https://www.fema.gov/api/open/v2/DisasterDeclarationsSummaries`
* **Transformation:**

  ```bash
  jq '.DisasterDeclarationsSummaries[] | select(.state=="KS")' disasters.json > ks_disasters.json
  ```
* **Graph Mapping:**

  * Disaster → `crm:E5_Event` (subclass: `HazardEvent`)
  * County → `crm:E53_Place`
  * Federal agency → `crm:E39_Actor` (FEMA)

---

### 5️⃣ USGS NWIS Flood Data

* **Data:** Streamflow & flood peaks (station-based).
* **Access:** `https://waterservices.usgs.gov/nwis/peak`
* **Output:** CSV → GeoJSON line geometry per river segment.
* **Ontology:**

  * `crm:E7_Activity` = Measurement
  * `crm:E53_Place` = Stream segment
  * `prov:wasGeneratedBy` = USGS instrumentation

---

## 🧾 Example STAC Item — Tornado Events (NOAA StormEvents)

```json
{
  "stac_version": "1.0.0",
  "id": "ks_tornado_1950_2025",
  "type": "Feature",
  "properties": {
    "datetime": "1950-01-01T00:00:00Z",
    "description": "NOAA Storm Events — Tornado occurrences in Kansas (1950–2025).",
    "license": "Public Domain",
    "keywords": ["tornado","storm","NOAA","Kansas","hazard"],
    "providers": [{"name":"NOAA NCEI","roles":["producer","licensor"]}]
  },
  "assets": {
    "data": {
      "href": "data/processed/hazards/ks_tornado_1950_2025.json",
      "type": "application/geo+json",
      "roles": ["data"],
      "title": "Kansas Tornado Events"
    },
    "checksum": {
      "href": "data/checksums/hazards/ks_tornado_1950_2025.json.sha256",
      "type": "text/plain",
      "roles": ["checksum"]
    }
  },
  "bbox": [-102.05,36.99,-94.59,40.00],
  "links": [
    {"rel": "collection", "href": "../collection.json"},
    {"rel": "documentation", "href": "../../../docs/integration/climate-hazards.md"}
  ]
}
```

Validate:

```bash
stac-validator data/stac/hazards/ks_tornado_1950_2025.json
```

---

## 🧮 Provenance (RDF/PROV-O Example)

```turtle
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix crm:  <http://www.cidoc-crm.org/cidoc-crm/> .
@prefix kfm:  <https://kfm.org/id/> .

kfm:event/ks_tornado_1955_001
    a crm:E5_Event ;
    crm:P4_has_time-span kfm:time/1955-05-25 ;
    crm:P7_took_place_at kfm:place/Sumner_County ;
    prov:wasDerivedFrom <https://www.ncei.noaa.gov/stormevents/> ;
    prov:wasAttributedTo kfm:agent/noaa_ncei ;
    prov:generatedAtTime "1955-05-25T19:20:00Z"^^xsd:dateTime .
```

---

## 🧠 Ontology Alignment Summary

| Entity Type                            | CIDOC CRM Class              | Example                     |
| :------------------------------------- | :--------------------------- | :-------------------------- |
| Weather Observation                    | `crm:E7_Activity`            | NOAA GHCN daily temp/precip |
| Hazard Event (Tornado, Flood, Drought) | `crm:E5_Event`               | 1955 Udall Tornado          |
| Dataset / Raster / Table               | `crm:E73_Information_Object` | Daymet V4 NetCDF            |
| Location                               | `crm:E53_Place`              | Sedgwick County             |
| Agency                                 | `crm:E39_Actor`              | NOAA / FEMA / USGS          |
| Time Period                            | `time:Interval`              | “1930–1940 Dust Bowl”       |

---

## 🔗 Cross-Domain Connections

| Linked Dataset               | Relationship         | Purpose                                          |
| :--------------------------- | :------------------- | :----------------------------------------------- |
| **Treaties & Land Cessions** | `prov:influencedBy`  | Correlate floods/droughts with settlement shifts |
| **Deeds & Homesteads**       | `crm:P70_documents`  | Link climate anomalies to agricultural expansion |
| **Oral Histories**           | `crm:P67_refers_to`  | Attach narratives about storms & droughts        |
| **GIS Archive (Hydrology)**  | `geo:hasGeometry`    | Link event footprints to river basins            |
| **Research Notes**           | `prov:wasInformedBy` | Feed datasets into climate reconstruction models |

---

## 🧩 CI Validation Hooks

| Validation                | Tool                              | Description                             |
| :------------------------ | :-------------------------------- | :-------------------------------------- |
| **STAC Schema Check**     | `stac-validator`                  | Confirms valid JSON schema and metadata |
| **Checksum Verification** | `sha256sum -c`                    | Verifies data integrity                 |
| **Geo Validation**        | `ogrinfo`                         | Ensures CRS and geometry validity       |
| **Ontology Mapping**      | `scripts/check_cidoc_links.py`    | Confirms proper entity mapping          |
| **Graph Ingestion**       | `scripts/graph_ingest_hazards.py` | Inserts hazard events into Neo4j        |

Run:

```bash
make stac-validate
make docs-validate
```

---

## 🧠 MCP Compliance Summary

| MCP Principle           | Implementation                                                   |
| :---------------------- | :--------------------------------------------------------------- |
| **Documentation-first** | All climate and hazard integrations documented before ingestion. |
| **Reproducibility**     | ETL steps scripted and versioned under Makefile targets.         |
| **Open Standards**      | Uses STAC, GeoJSON, NetCDF, PROV-O, CIDOC CRM, OWL-Time.         |
| **Provenance**          | SHA-256 + RDF provenance recorded for every dataset.             |
| **Auditability**        | Logs in `data/work/logs/hazards/` ensure transparent lineage.    |

---

## 📎 Related Documentation

| File                                     | Description                               |
| :--------------------------------------- | :---------------------------------------- |
| `docs/integration/gis-archive.md`        | GIS Archive & terrain integration guide   |
| `docs/integration/deeds.md`              | Homestead and deeds data integration      |
| `docs/standards/metadata.md`             | Metadata, checksum, and STAC standards    |
| `docs/architecture/data-architecture.md` | Pipeline, storage, and data catalog       |
| `docs/notes/research.md`                 | Research applications of climate datasets |

---

## 📅 Version History

| Version | Date       | Author                              | Summary                                                              |
| :------ | :--------- | :---------------------------------- | :------------------------------------------------------------------- |
| v1.1    | 2025-10-05 | KFM Climate & Data Integration Team | Added FEMA + USGS workflows, RDF provenance, and ontology mappings.  |
| v1.0    | 2025-10-04 | KFM Documentation Team              | Initial integration of NOAA/NASA datasets under STAC + CIDOC schema. |

---

<div align="center">

**Kansas Frontier Matrix** — *“Every Storm Recorded. Every Climate Proven.”*
📍 [`docs/integration/climate-hazards.md`](.) · Official MCP-compliant integration guide for climate and hazard datasets.

</div>
