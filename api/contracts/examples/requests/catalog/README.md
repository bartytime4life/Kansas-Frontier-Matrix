# 📚 Catalog API — Request Examples (KFM) 🗺️🔎

![Status](https://img.shields.io/badge/status-draft-yellow)
![Style](https://img.shields.io/badge/style-contract--first-blue)
![Interfaces](https://img.shields.io/badge/interfaces-REST%20%2B%20GraphQL-6f42c1)
![Metadata](https://img.shields.io/badge/metadata-STAC%20%2B%20DCAT%20%2B%20PROV-0b7285)
![Geo](https://img.shields.io/badge/geo-PostGIS%20%2B%20Neo4j-2f9e44)

> According to a document from **January 24, 2026**, KFM treats the **catalog as the metadata backbone** (STAC/DCAT/PROV) and serves it through a **FastAPI REST API + GraphQL**, with policy enforcement and provenance-first rules. :contentReference[oaicite:0]{index=0} :contentReference[oaicite:1]{index=1} :contentReference[oaicite:2]{index=2} :contentReference[oaicite:3]{index=3} :contentReference[oaicite:4]{index=4}

---

## 📍 You are here

```text
api/
  contracts/
    examples/
      requests/
        catalog/
          README.md   👈 (this file)
```

This folder is for **copy/pasteable request examples** used in:
- ✅ manual testing (curl / httpie / Postman)
- ✅ contract validation (OpenAPI + GraphQL)
- ✅ UI integration checks (catalog panel, search, timeline, layer toggles) :contentReference[oaicite:5]{index=5} :contentReference[oaicite:6]{index=6}

---

## 🧠 What “Catalog” means in KFM

KFM is built around an **evidence-first, provenance-first** intake and publishing pipeline: data is promoted only when metadata + lineage are present and validated. :contentReference[oaicite:7]{index=7} :contentReference[oaicite:8]{index=8}

### The “metadata triplet” 🧩🧩🧩
KFM models each dataset as a linked set of standards:

- **DCAT** = discovery & human metadata (title, publisher, license, theme)  
- **STAC** = spatiotemporal indexing & assets (files, footprints, dates, links)  
- **W3C PROV** = lineage (what produced it, what inputs were used, who/what ran it)

KFM cross-references these records and uses them to drive Neo4j graph import + UI trust surfaces. :contentReference[oaicite:9]{index=9} :contentReference[oaicite:10]{index=10} :contentReference[oaicite:11]{index=11}

```mermaid
flowchart LR
  DCAT[🗂️ DCAT Dataset] -->|links to| STAC[🛰️ STAC Collection/Items]
  DCAT -->|links to| PROV[🧾 PROV Bundle]
  STAC --> ASSET[📦 Assets (COG/GeoParquet/PMTiles/etc)]
  PROV --> ACT[⚙️ prov:Activity]
  ACT --> IN[⬅️ prov:used (inputs)]
  ACT --> OUT[➡️ prov:generated (outputs)]
```

---

## 🔐 Request conventions

### Base URL
All examples assume:
- REST base: `https://<host>/api`
- Tiles base (commonly unversioned): `https://<host>/tiles`
- GraphQL: `https://<host>/api/graphql` (or `/graphql` depending on deployment)

> KFM’s docs describe FastAPI REST endpoints + a GraphQL endpoint for traversing graph/cross-entity queries. :contentReference[oaicite:12]{index=12} :contentReference[oaicite:13]{index=13}

### Auth (if enabled)
KFM anticipates OAuth/token auth for roles and restricted access paths. :contentReference[oaicite:14]{index=14}

```bash
export KFM_BASE="https://kfm.example.org"
export KFM_TOKEN="…"
```

Typical headers:
- `Authorization: Bearer $KFM_TOKEN`
- `Accept: application/json`

### IDs & naming 🧷
Examples use stable IDs like:

- `kfm.ks.landcover.2020` (dataset)
- `kfm.ks.place.douglas_county` (place)

This matches internal examples where GraphQL queries use `dataset(id:"kfm.ks.landcover.2020")`. :contentReference[oaicite:15]{index=15}

---

## 🧾 REST request examples

> Many endpoints below are explicitly referenced in the design docs (e.g., dataset metadata/data, place→datasets, tiles). Where your deployment differs, keep the **shape** and adjust the **route**. :contentReference[oaicite:16]{index=16} :contentReference[oaicite:17]{index=17} :contentReference[oaicite:18]{index=18}

### 1) Get dataset metadata (DCAT-first wrapper) 🗂️

**GET** `/api/datasets/{id}`  
Used by UI catalog panels + programmatic clients. :contentReference[oaicite:19]{index=19} :contentReference[oaicite:20]{index=20}

```bash
curl -sS "$KFM_BASE/api/datasets/kfm.ks.landcover.2020" \
  -H "Accept: application/json"
```

**Example response (shape)**
```json
{
  "id": "kfm.ks.landcover.2020",
  "title": "Kansas Landcover 2020",
  "description": "…",
  "license": "CC-BY-4.0",
  "classification": "public",
  "links": [
    { "rel": "dcat", "href": "/api/dcat/datasets/kfm.ks.landcover.2020.jsonld" },
    { "rel": "stac", "href": "/api/stac/collections/kfm.ks.landcover.2020" },
    { "rel": "prov", "href": "/api/prov/datasets/kfm.ks.landcover.2020.jsonld" }
  ]
}
```

---

### 2) Download / stream dataset data (authorized) 📦⬇️

**GET** `/api/datasets/{id}/data` :contentReference[oaicite:21]{index=21}

```bash
curl -L "$KFM_BASE/api/datasets/kfm.ks.landcover.2020/data" \
  -H "Authorization: Bearer $KFM_TOKEN"
```

Notes:
- This may return a file, a signed URL, or a format-negotiated stream (GeoJSON / WFS-like / parquet).  
- Policy gates may restrict distributions for sensitive datasets. :contentReference[oaicite:22]{index=22} :contentReference[oaicite:23]{index=23}

---

### 3) List datasets linked to a place 🧭📚

**GET** `/api/graph/places/{placeId}/datasets` :contentReference[oaicite:24]{index=24}

```bash
curl -sS "$KFM_BASE/api/graph/places/kfm.ks.place.douglas_county/datasets" \
  -H "Accept: application/json"
```

Why this exists:
- The graph determines “what data is relevant”, while PostGIS/SQL does heavy counts/spatial slicing. :contentReference[oaicite:25]{index=25}

---

### 4) Catalog search (simple GET) 🔎

**GET** `/api/catalog/search?q=&bbox=&datetime=&theme=&limit=`  
This is a **contract-style** pattern that supports UI search + caching.

```bash
curl -sS "$KFM_BASE/api/catalog/search" \
  --get \
  --data-urlencode "q=landcover" \
  --data-urlencode "bbox=-102.05,36.99,-94.59,40.00" \
  --data-urlencode "datetime=2019-01-01/2021-12-31" \
  --data-urlencode "limit=25"
```

Recommended semantics:
- `bbox` order: `west,south,east,north`
- `datetime` range: `start/end` (ISO8601)
- `theme` aligned with ontology/taxonomy nodes used for tagging and discovery :contentReference[oaicite:26]{index=26}

---

### 5) Catalog search (complex POST) 🧪🧰

**POST** `/api/catalog/search`

```bash
curl -sS "$KFM_BASE/api/catalog/search" \
  -H "Content-Type: application/json" \
  -d '{
    "q": "drought",
    "filters": {
      "places": ["kfm.ks.place.douglas_county"],
      "time": { "start": "1930-01-01", "end": "1940-12-31" },
      "themes": ["drought", "agriculture"],
      "classification_max": "public"
    },
    "include": ["links", "highlights"],
    "page": { "size": 25 }
  }'
```

> The system is designed for governed access: UI should not query the graph directly; API mediates permissions/redaction and query cost controls. :contentReference[oaicite:27]{index=27} :contentReference[oaicite:28]{index=28}

---

## 🛰️ STAC API request examples

> KFM uses STAC to describe geospatial assets and to drive interoperability with external tools; STAC items include links/pointers to provenance and related records. :contentReference[oaicite:29]{index=29}

### 6) STAC root / collections
```bash
curl -sS "$KFM_BASE/api/stac" | jq .
curl -sS "$KFM_BASE/api/stac/collections" | jq .
```

### 7) Get a STAC Collection
```bash
curl -sS "$KFM_BASE/api/stac/collections/kfm.ks.landcover.2020" | jq .
```

### 8) STAC search (standard pattern) 🧭
```bash
curl -sS "$KFM_BASE/api/stac/search" \
  -H "Content-Type: application/json" \
  -d '{
    "collections": ["kfm.ks.landcover.2020"],
    "bbox": [-102.05, 36.99, -94.59, 40.00],
    "datetime": "2020-01-01/2020-12-31",
    "limit": 10
  }' | jq .
```

---

## 🧾 DCAT request examples (JSON-LD)

> DCAT captures high-level dataset metadata for discovery (title/description/license/publisher/distributions). :contentReference[oaicite:30]{index=30}

### 9) Get DCAT catalog export 🧰
```bash
curl -sS "$KFM_BASE/api/dcat/catalog.jsonld" \
  -H "Accept: application/ld+json"
```

### 10) Get DCAT dataset record
```bash
curl -sS "$KFM_BASE/api/dcat/datasets/kfm.ks.landcover.2020.jsonld" \
  -H "Accept: application/ld+json"
```

**What to look for**
- Distributions that link to STAC collections, tile endpoints, and/or downloadable files. :contentReference[oaicite:31]{index=31}

---

## 🧾 PROV request examples (lineage)

> KFM uses W3C PROV to capture lineage and reproducibility (inputs, activities, agents). :contentReference[oaicite:32]{index=32} :contentReference[oaicite:33]{index=33}

### 11) Get PROV record for a dataset
```bash
curl -sS "$KFM_BASE/api/prov/datasets/kfm.ks.landcover.2020.jsonld" \
  -H "Accept: application/ld+json"
```

### 12) DevOps provenance (PR → PROV) 🧑‍💻➡️🧾
KFM proposals include mapping GitHub PR events into PROV (Activity/Entity/Agent) so you can trace “which code change produced this dataset.” :contentReference[oaicite:34]{index=34}

---

## 🧱 Tile request examples (MapLibre/Cesium-friendly)

> UI performance depends on lazy loading + tiles; PostGIS can generate Mapbox Vector Tiles (MVT) using ST_AsMVT patterns. :contentReference[oaicite:35]{index=35} :contentReference[oaicite:36]{index=36}

### 13) Vector tile (example from docs) 🧩
**GET** `/tiles/landcover/{z}/{x}/{y}.pbf` :contentReference[oaicite:37]{index=37}

```bash
curl -I "$KFM_BASE/tiles/landcover/6/16/24.pbf"
```

### 14) Dataset-specific tile convention (recommended contract)
If your catalog includes dataset-driven tile services:

```bash
curl -I "$KFM_BASE/tiles/datasets/kfm.ks.landcover.2020/6/16/24.pbf"
```

> The UI can request XYZ tiles directly (standard pattern) while still showing provenance & source attribution via catalog links. :contentReference[oaicite:38]{index=38}

---

## 🧬 GraphQL request examples (catalog + graph traversal)

> GraphQL is positioned for flexible traversal across entities (Dataset/Place/Event/etc.), backed by Neo4j/PostGIS resolvers with safety limits. :contentReference[oaicite:39]{index=39}

### 15) Dataset lookup (from KFM docs) ✅
```bash
curl -sS "$KFM_BASE/api/graphql" \
  -H "Content-Type: application/json" \
  -d '{
    "query": "query { dataset(id:\"kfm.ks.landcover.2020\") { title description stac { assets { href } } relations { derivedFrom { id } } } }"
  }' | jq .
```
:contentReference[oaicite:40]{index=40}

### 16) Person → events → locations (graph traversal pattern)
```bash
curl -sS "$KFM_BASE/api/graphql" \
  -H "Content-Type: application/json" \
  -d '{
    "query": "{ person(name:\"John Brown\") { name events { title date locations { name } } } }"
  }' | jq .
```
:contentReference[oaicite:41]{index=41} :contentReference[oaicite:42]{index=42}

---

## 🌐 Federation examples (multi-region “Frontier Matrices”)

KFM’s roadmap emphasizes federation: interoperable APIs + ontologies so queries can span regions (e.g., Kansas + Nebraska). :contentReference[oaicite:43]{index=43} :contentReference[oaicite:44]{index=44} :contentReference[oaicite:45]{index=45}

### 17) Federated catalog search (contract proposal)
```bash
curl -sS "$KFM_BASE/api/catalog/search" \
  -H "Accept: application/json" \
  -H "X-KFM-Federate: true" \
  --get \
  --data-urlencode "q=Ogallala Aquifer"
```

---

## 🧿 Sensitivity, redaction, and “differential access”

KFM explicitly considers ethical governance and the need for **tiered access** (e.g., community-only content) and **geo-obfuscation** (e.g., rounding sensitive coordinates). :contentReference[oaicite:46]{index=46} :contentReference[oaicite:47]{index=47}

### 18) Example: restricted dataset response shape
When a dataset is sensitive, API may:
- omit exact geometry,
- generalize bbox,
- suppress sensitive attributes unless authorized.

```json
{
  "id": "kfm.ks.archaeology.sites",
  "classification": "restricted",
  "geometry": null,
  "bbox": [-99.0, 37.0, -95.0, 40.0],
  "links": [
    { "rel": "dcat", "href": "/api/dcat/datasets/kfm.ks.archaeology.sites.jsonld" }
  ]
}
```

---

## ✅ Contract testing tips (why these examples exist)

- FastAPI auto-generates **OpenAPI/Swagger**; treat it as a contract surface for clients and tests. :contentReference[oaicite:48]{index=48} :contentReference[oaicite:49]{index=49}  
- KFM validates STAC/DCAT/PROV outputs in CI (“metadata as code”), so example requests should be kept in sync with schema versions/profiles. :contentReference[oaicite:50]{index=50}  
- Policy enforcement is emphasized (OPA/Rego + Conftest “Policy Pack”), including “no provenance → no publish” invariants. :contentReference[oaicite:51]{index=51} :contentReference[oaicite:52]{index=52}

---

## 🧪 Suggested example files to add (optional)

If you want this folder to be runnable as a test fixture, consider adding:

- [ ] `get-dataset.http` (REST Client / VS Code)
- [ ] `catalog-search.http`
- [ ] `stac-search.json`
- [ ] `graphql-dataset.query.graphql`
- [ ] `graphql-person.query.graphql`

---

## 📚 Project references (used to shape this README)

> These are the source documents that define the KFM architecture, catalog standards, UI needs, and governance philosophy.

### Core KFM docs 🧭
- Kansas Frontier Matrix – Comprehensive UI System Overview :contentReference[oaicite:53]{index=53} :contentReference[oaicite:54]{index=54}  
- 📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide :contentReference[oaicite:55]{index=55} :contentReference[oaicite:56]{index=56}  
- Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design :contentReference[oaicite:57]{index=57} :contentReference[oaicite:58]{index=58}  
- Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation :contentReference[oaicite:59]{index=59} :contentReference[oaicite:60]{index=60} :contentReference[oaicite:61]{index=61}  
- Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖 :contentReference[oaicite:62]{index=62}  
- 🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals :contentReference[oaicite:63]{index=63}  
- Innovative Concepts to Evolve the Kansas Frontier Matrix (KFM) :contentReference[oaicite:64]{index=64} :contentReference[oaicite:65]{index=65} :contentReference[oaicite:66]{index=66}  
- Additional Project Ideas :contentReference[oaicite:67]{index=67}

### Resource portfolios (supporting research) 📦
- AI Concepts & more (PDF portfolio) :contentReference[oaicite:68]{index=68}  
- Maps-GoogleMaps-VirtualWorlds-Archaeological-Computer Graphics-Geospatial-webgl (PDF portfolio) :contentReference[oaicite:69]{index=69}  
- Data Managment-Theories-Architures-Data Science-Baysian Methods-Some Programming Ideas (PDF portfolio) :contentReference[oaicite:70]{index=70}  
- Various programming langurages & resources 1 (PDF portfolio) :contentReference[oaicite:71]{index=71}  

### Internal doc note 🧾
- Document_ Refinement Request_ Comprehensive Markdown Document with All Considerations and Inputs :contentReference[oaicite:72]{index=72}
