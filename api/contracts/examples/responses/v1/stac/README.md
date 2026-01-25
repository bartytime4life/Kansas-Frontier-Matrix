# 🛰️ STAC Response Examples (v1) — Kansas Frontier Matrix (KFM)

![API](https://img.shields.io/badge/API-v1-blue)
![STAC](https://img.shields.io/badge/STAC-1.0.0-blueviolet)
![Contracts](https://img.shields.io/badge/Contract--First-✅-brightgreen)
![Provenance](https://img.shields.io/badge/Provenance--First-🔍-orange)
![Policy](https://img.shields.io/badge/Policy--Gated-🛡️-informational)

> 📦 This folder contains **canonical response examples** for the **STAC API** surface of KFM (version `v1`).
> These fixtures are designed for **contract testing**, **OpenAPI documentation snapshots**, and **UI/client integration**. 🧪🗺️

---

## 🎯 What’s in this folder?

✅ **Response examples only** (JSON / GeoJSON) for STAC routes (typically) under:

- `GET  /api/v1/stac`
- `GET  /api/v1/stac/conformance`
- `GET  /api/v1/stac/collections`
- `GET  /api/v1/stac/collections/{collectionId}`
- `GET  /api/v1/stac/collections/{collectionId}/items`
- `GET  /api/v1/stac/collections/{collectionId}/items/{itemId}`
- `POST /api/v1/stac/search`

> ⚠️ The **path prefix** can be adjusted to match routing (`/stac`, `/api/stac`, etc.).  
> What matters is the **shape** and **policy behavior** of the responses. ✅

---

## 🧭 How this fits KFM (context map)

KFM treats catalogs as **boundary artifacts**. STAC is the spatial/temporal index ✅, DCAT is discovery/publishing ✅, and PROV is lineage ✅.

```mermaid
flowchart LR
  A[🧱 ETL + Normalization] --> B[🛰️ STAC Items + Collections]
  B --> C[📚 DCAT Dataset Views]
  B --> D[🧬 PROV Lineage Bundles]
  B --> E[🧠 Graph Index]
  E --> F[🛡️ API Layer (contracts + redaction)]
  F --> G[🗺️ UI (MapLibre / Cesium)]
  G --> H[📖 Story Nodes]
  H --> I[🤖 Focus Mode]
```

---

## 🗂️ Expected layout (suggested)

> This README is the contract “front door.” The actual response fixtures can live alongside it.

```text
api/
└─ contracts/
   └─ examples/
      └─ responses/
         └─ v1/
            └─ stac/
               ├─ README.md                 👈 you are here
               ├─ root.get.json             (optional)
               ├─ conformance.get.json      (optional)
               ├─ collections.get.json      (optional)
               ├─ collection.get.json       (optional)
               ├─ items.get.json            (optional)
               ├─ item.get.json             (optional)
               ├─ search.post.json          (optional)
               └─ errors.problem+json       (optional)
```

✅ If you keep fixtures as separate files, prefer **stable naming** and **stable IDs** so snapshot tests don’t churn.

---

## 🔗 Endpoint coverage matrix

| Route | Shape | Media type | Notes |
|---|---|---:|---|
| `GET /stac` | STAC Catalog | `application/json` | Root catalog + discovery links |
| `GET /stac/conformance` | Conformance | `application/json` | OGC + STAC conformance URIs |
| `GET /stac/collections` | Collections list | `application/json` | Wrapper `{ collections: [...] }` |
| `GET /stac/collections/{collectionId}` | STAC Collection | `application/json` | Includes `extent`, `license`, `links` |
| `GET /stac/collections/{collectionId}/items` | Item list | `application/geo+json` | GeoJSON FeatureCollection of Items |
| `GET /stac/collections/{collectionId}/items/{itemId}` | STAC Item | `application/geo+json` | Single Item (GeoJSON Feature) |
| `POST /stac/search` | Search results | `application/geo+json` | FeatureCollection + pagination links |

---

## 🧩 KFM STAC Profile extensions (namespace: `kfm:`)

KFM extends STAC where needed, but keeps extensions **explicit**, **typed**, and **governed**.

### ✅ Required in KFM-STAC (practical minimum)

- `properties.kfm:dataset_id`  
  Canonical dataset identifier used across catalogs + graph + API.
- `properties.kfm:classification`  
  Policy label (e.g., `public`, `internal`, `restricted`, `confidential`) used for redaction/authorization.
- One or more **links** connecting to:
  - DCAT dataset metadata (discovery + attribution)
  - PROV bundle or activity (lineage + reproducibility)

### ⭐ Recommended (high value, low risk)

- `kfm:profiles` (root/collection/item): explicit profile versions used to validate
- `assets[*].kfm:hashes` (or checksums): deterministic integrity
- `assets[*].kfm:oci` (optional): OCI artifact reference, digest, signature info
- `links[*].rel = "license"` and/or `license` on Collection
- `links[*].rel = "cite-as"` (optional): stable citation handle / DOI / snapshot ref

---

## 📦 Canonical example responses

> 🧪 These are **reference fixtures**: small, readable, and deterministic.  
> Use `{{baseUrl}}` placeholders so they can run in CI + local dev.

---

<details>
<summary><strong>🛰️ 1) Root Catalog — <code>GET /api/v1/stac</code></strong></summary>

```json
{
  "stac_version": "1.0.0",
  "type": "Catalog",
  "id": "kfm.ks",
  "title": "Kansas Frontier Matrix (KFM) — STAC API",
  "description": "Catalog-driven STAC API over published KFM collections and items.",
  "links": [
    { "rel": "self", "href": "{{baseUrl}}/api/v1/stac", "type": "application/json" },
    { "rel": "root", "href": "{{baseUrl}}/api/v1/stac", "type": "application/json" },

    { "rel": "conformance", "href": "{{baseUrl}}/api/v1/stac/conformance", "type": "application/json" },
    { "rel": "data", "href": "{{baseUrl}}/api/v1/stac/collections", "type": "application/json" },

    { "rel": "search", "href": "{{baseUrl}}/api/v1/stac/search", "type": "application/geo+json", "method": "POST" },

    { "rel": "service-desc", "href": "{{baseUrl}}/api/v1/openapi.json", "type": "application/vnd.oai.openapi+json;version=3.0" },
    { "rel": "service-doc", "href": "{{baseUrl}}/api/docs", "type": "text/html" }
  ],

  "kfm:api_version": "v1",
  "kfm:profiles": {
    "stac": "KFM-STAC-Profile@v1",
    "dcat": "KFM-DCAT-Profile@v1",
    "prov": "KFM-PROV-Profile@v11.0.0"
  }
}
```

</details>

---

<details>
<summary><strong>📜 2) Conformance — <code>GET /api/v1/stac/conformance</code></strong></summary>

```json
{
  "conformsTo": [
    "http://www.opengis.net/spec/ogcapi-common-1/1.0/conf/core",
    "http://www.opengis.net/spec/ogcapi-common-1/1.0/conf/json",
    "http://www.opengis.net/spec/ogcapi-common-1/1.0/conf/oas30",
    "http://www.opengis.net/spec/ogcapi-features-1/1.0/conf/core",
    "http://www.opengis.net/spec/ogcapi-features-1/1.0/conf/geojson",
    "https://api.stacspec.org/v1.0.0/core",
    "https://api.stacspec.org/v1.0.0/collections",
    "https://api.stacspec.org/v1.0.0/item-search"
  ]
}
```

</details>

---

<details>
<summary><strong>📚 3) Collections list — <code>GET /api/v1/stac/collections</code></strong></summary>

```json
{
  "collections": [
    {
      "stac_version": "1.0.0",
      "type": "Collection",
      "id": "kfm.ks.landcover.1990_2020.v1",
      "title": "Kansas Landcover 1990–2020",
      "description": "Annual landcover classifications for Kansas (1990–2020).",
      "license": "CC-BY-4.0",
      "extent": {
        "spatial": {
          "bbox": [[-102.051744, 36.993016, -94.588413, 40.003166]]
        },
        "temporal": {
          "interval": [["1990-01-01T00:00:00Z", "2020-12-31T23:59:59Z"]]
        }
      },
      "links": [
        { "rel": "self", "href": "{{baseUrl}}/api/v1/stac/collections/kfm.ks.landcover.1990_2020.v1", "type": "application/json" },
        { "rel": "root", "href": "{{baseUrl}}/api/v1/stac", "type": "application/json" },
        { "rel": "items", "href": "{{baseUrl}}/api/v1/stac/collections/kfm.ks.landcover.1990_2020.v1/items", "type": "application/geo+json" },

        { "rel": "describedby", "href": "{{baseUrl}}/api/v1/catalog/dcat/datasets/kfm.ks.landcover.1990_2020.v1", "type": "application/ld+json", "title": "DCAT Dataset (discovery + attribution)" },
        { "rel": "via", "href": "{{baseUrl}}/api/v1/prov/bundles/kfm.ks.landcover.1990_2020.v1", "type": "application/ld+json", "title": "PROV Bundle (lineage)" }
      ],
      "kfm:classification": "public"
    }
  ],
  "links": [
    { "rel": "self", "href": "{{baseUrl}}/api/v1/stac/collections", "type": "application/json" },
    { "rel": "root", "href": "{{baseUrl}}/api/v1/stac", "type": "application/json" }
  ]
}
```

</details>

---

<details>
<summary><strong>🧱 4) Single Collection — <code>GET /api/v1/stac/collections/{collectionId}</code></strong></summary>

```json
{
  "stac_version": "1.0.0",
  "type": "Collection",
  "id": "kfm.ks.landcover.1990_2020.v1",
  "title": "Kansas Landcover 1990–2020",
  "description": "Annual landcover classifications for Kansas (1990–2020).",
  "license": "CC-BY-4.0",

  "extent": {
    "spatial": { "bbox": [[-102.051744, 36.993016, -94.588413, 40.003166]] },
    "temporal": { "interval": [["1990-01-01T00:00:00Z", "2020-12-31T23:59:59Z"]] }
  },

  "links": [
    { "rel": "self", "href": "{{baseUrl}}/api/v1/stac/collections/kfm.ks.landcover.1990_2020.v1", "type": "application/json" },
    { "rel": "root", "href": "{{baseUrl}}/api/v1/stac", "type": "application/json" },
    { "rel": "parent", "href": "{{baseUrl}}/api/v1/stac", "type": "application/json" },

    { "rel": "items", "href": "{{baseUrl}}/api/v1/stac/collections/kfm.ks.landcover.1990_2020.v1/items", "type": "application/geo+json" },

    { "rel": "describedby", "href": "{{baseUrl}}/api/v1/catalog/dcat/datasets/kfm.ks.landcover.1990_2020.v1", "type": "application/ld+json" },
    { "rel": "via", "href": "{{baseUrl}}/api/v1/prov/bundles/kfm.ks.landcover.1990_2020.v1", "type": "application/ld+json" }
  ],

  "kfm:classification": "public",
  "kfm:profiles": {
    "stac": "KFM-STAC-Profile@v1"
  }
}
```

</details>

---

<details>
<summary><strong>🧩 5) Items list — <code>GET /api/v1/stac/collections/{collectionId}/items</code></strong></summary>

```json
{
  "type": "FeatureCollection",
  "features": [
    {
      "stac_version": "1.0.0",
      "type": "Feature",
      "id": "kfm.ks.landcover.2020.v1",
      "collection": "kfm.ks.landcover.1990_2020.v1",
      "bbox": [-102.051744, 36.993016, -94.588413, 40.003166],
      "geometry": {
        "type": "Polygon",
        "coordinates": [[
          [-102.051744, 36.993016],
          [-94.588413, 36.993016],
          [-94.588413, 40.003166],
          [-102.051744, 40.003166],
          [-102.051744, 36.993016]
        ]]
      },
      "properties": {
        "datetime": "2020-01-01T00:00:00Z",

        "kfm:dataset_id": "kfm.ks.landcover.1990_2020.v1",
        "kfm:classification": "public",

        "kfm:prov_activity_id": "kfm.prov.activity.merge_nlcd@2025-01-02"
      },
      "links": [
        { "rel": "self", "href": "{{baseUrl}}/api/v1/stac/collections/kfm.ks.landcover.1990_2020.v1/items/kfm.ks.landcover.2020.v1", "type": "application/geo+json" },
        { "rel": "collection", "href": "{{baseUrl}}/api/v1/stac/collections/kfm.ks.landcover.1990_2020.v1", "type": "application/json" },
        { "rel": "root", "href": "{{baseUrl}}/api/v1/stac", "type": "application/json" },

        { "rel": "describedby", "href": "{{baseUrl}}/api/v1/catalog/dcat/datasets/kfm.ks.landcover.1990_2020.v1", "type": "application/ld+json" },
        { "rel": "via", "href": "{{baseUrl}}/api/v1/prov/bundles/kfm.ks.landcover.1990_2020.v1", "type": "application/ld+json" }
      ],
      "assets": {
        "cog": {
          "href": "{{baseUrl}}/api/v1/artifacts/kfm.ks.landcover.2020.v1/cog",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": ["data"],
          "title": "Landcover 2020 (COG)",
          "kfm:hashes": {
            "sha256": "3f2a9b7d4a1c0d5e7f00e11b2a4f8c1d00000000000000000000000000000000"
          }
        },
        "tiles_pmtiles": {
          "href": "{{baseUrl}}/api/v1/artifacts/kfm.ks.landcover.2020.v1/pmtiles",
          "type": "application/vnd.pmtiles",
          "roles": ["tiles"],
          "title": "Offline/portable tiles (PMTiles)"
        },
        "thumbnail": {
          "href": "{{baseUrl}}/api/v1/artifacts/kfm.ks.landcover.2020.v1/thumbnail.png",
          "type": "image/png",
          "roles": ["thumbnail"]
        },
        "provenance": {
          "href": "{{baseUrl}}/api/v1/prov/bundles/kfm.ks.landcover.1990_2020.v1",
          "type": "application/ld+json",
          "roles": ["metadata"],
          "title": "PROV bundle (lineage)"
        }
      }
    }
  ],
  "links": [
    { "rel": "self", "href": "{{baseUrl}}/api/v1/stac/collections/kfm.ks.landcover.1990_2020.v1/items?limit=1", "type": "application/geo+json" },
    { "rel": "next", "href": "{{baseUrl}}/api/v1/stac/collections/kfm.ks.landcover.1990_2020.v1/items?limit=1&cursor=eyJvZmZzZXQiOjF9", "type": "application/geo+json" }
  ],
  "numberReturned": 1
}
```

</details>

---

<details>
<summary><strong>🎯 6) Single Item — <code>GET /api/v1/stac/collections/{collectionId}/items/{itemId}</code></strong></summary>

```json
{
  "stac_version": "1.0.0",
  "type": "Feature",
  "id": "kfm.ks.landcover.2020.v1",
  "collection": "kfm.ks.landcover.1990_2020.v1",
  "bbox": [-102.051744, 36.993016, -94.588413, 40.003166],
  "geometry": {
    "type": "Polygon",
    "coordinates": [[
      [-102.051744, 36.993016],
      [-94.588413, 36.993016],
      [-94.588413, 40.003166],
      [-102.051744, 40.003166],
      [-102.051744, 36.993016]
    ]]
  },
  "properties": {
    "datetime": "2020-01-01T00:00:00Z",

    "kfm:dataset_id": "kfm.ks.landcover.1990_2020.v1",
    "kfm:classification": "public",
    "kfm:prov_activity_id": "kfm.prov.activity.merge_nlcd@2025-01-02"
  },
  "links": [
    { "rel": "self", "href": "{{baseUrl}}/api/v1/stac/collections/kfm.ks.landcover.1990_2020.v1/items/kfm.ks.landcover.2020.v1", "type": "application/geo+json" },
    { "rel": "collection", "href": "{{baseUrl}}/api/v1/stac/collections/kfm.ks.landcover.1990_2020.v1", "type": "application/json" },
    { "rel": "root", "href": "{{baseUrl}}/api/v1/stac", "type": "application/json" },

    { "rel": "describedby", "href": "{{baseUrl}}/api/v1/catalog/dcat/datasets/kfm.ks.landcover.1990_2020.v1", "type": "application/ld+json" },
    { "rel": "via", "href": "{{baseUrl}}/api/v1/prov/bundles/kfm.ks.landcover.1990_2020.v1", "type": "application/ld+json" }
  ],
  "assets": {
    "cog": {
      "href": "{{baseUrl}}/api/v1/artifacts/kfm.ks.landcover.2020.v1/cog",
      "type": "image/tiff; application=geotiff; profile=cloud-optimized",
      "roles": ["data"],
      "title": "Landcover 2020 (COG)",
      "kfm:hashes": {
        "sha256": "3f2a9b7d4a1c0d5e7f00e11b2a4f8c1d00000000000000000000000000000000"
      },
      "kfm:oci": {
        "ref": "ghcr.io/kansas-frontier-matrix/artifacts/landcover-2020:v1",
        "digest": "sha256:aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
        "cosign": {
          "bundle_href": "{{baseUrl}}/api/v1/artifacts/kfm.ks.landcover.2020.v1/signature"
        }
      }
    }
  }
}
```

</details>

---

<details>
<summary><strong>🔎 7) Search results — <code>POST /api/v1/stac/search</code></strong></summary>

```json
{
  "type": "FeatureCollection",
  "features": [
    {
      "stac_version": "1.0.0",
      "type": "Feature",
      "id": "kfm.ks.landcover.2020.v1",
      "collection": "kfm.ks.landcover.1990_2020.v1",
      "bbox": [-102.051744, 36.993016, -94.588413, 40.003166],
      "geometry": {
        "type": "Polygon",
        "coordinates": [[
          [-102.051744, 36.993016],
          [-94.588413, 36.993016],
          [-94.588413, 40.003166],
          [-102.051744, 40.003166],
          [-102.051744, 36.993016]
        ]]
      },
      "properties": {
        "datetime": "2020-01-01T00:00:00Z",
        "kfm:dataset_id": "kfm.ks.landcover.1990_2020.v1",
        "kfm:classification": "public"
      },
      "links": [
        { "rel": "self", "href": "{{baseUrl}}/api/v1/stac/collections/kfm.ks.landcover.1990_2020.v1/items/kfm.ks.landcover.2020.v1", "type": "application/geo+json" },
        { "rel": "collection", "href": "{{baseUrl}}/api/v1/stac/collections/kfm.ks.landcover.1990_2020.v1", "type": "application/json" },
        { "rel": "root", "href": "{{baseUrl}}/api/v1/stac", "type": "application/json" }
      ],
      "assets": {
        "cog": {
          "href": "{{baseUrl}}/api/v1/artifacts/kfm.ks.landcover.2020.v1/cog",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": ["data"]
        }
      }
    }
  ],
  "links": [
    { "rel": "self", "href": "{{baseUrl}}/api/v1/stac/search", "type": "application/geo+json" }
  ],
  "numberReturned": 1
}
```

</details>

---

<details>
<summary><strong>🧯 8) Error shape — <code>application/problem+json</code> (recommended)</strong></summary>

```json
{
  "type": "about:blank",
  "title": "Not Found",
  "status": 404,
  "detail": "STAC collection not found: kfm.ks.nope",
  "instance": "/api/v1/stac/collections/kfm.ks.nope",
  "kfm:request_id": "req_01J2ZV4YJ3KQ0V9S6C9A7B8C9D"
}
```

</details>

---

## 🔒 Policy & redaction notes 🛡️

KFM responses must remain **governed**:

- If `kfm:classification` is not `public`, the API may:
  - omit records entirely, or
  - return a redacted geometry (`geometry: null`) and/or generalized bbox, or
  - require auth scopes and return `403` otherwise.

✅ The example fixtures in this folder should be **safe-by-default** (public data, no precise sensitive sites).

---

## 🧪 Contract testing checklist (keep fixtures stable)

When adding/updating response examples:

- ✅ **Keep IDs deterministic** (`collectionId`, `itemId`) so snapshots don’t churn.
- ✅ Prefer **fixed timestamps** (don’t use `now()` in examples).
- ✅ Validate:
  - STAC core + STAC API shapes
  - KFM-STAC required fields (`kfm:dataset_id`, `kfm:classification`)
- ✅ Ensure catalog-linkage exists (DCAT + PROV linkage via `links` and/or assets metadata)
- ✅ If response shape changes: **version bump** (`v2/…`) rather than breaking clients.

---

## 🚀 Future-friendly extensions (non-breaking) 🌱

These are “safe to add later” without breaking clients:

- 📦 **Offline Packs**: add `assets.tiles_pmtiles` or `assets.mbtiles` (portable packages).
- 🧵 **Pulse Threads / streaming**: treat live feeds as append-only STAC Items (time-indexed).
- 🧊 **4D / simulations**: add `kfm:scenario_id`, `kfm:run_id`, `kfm:time_step`, or a `kfm:state` block.
- 🧭 **UI extras**: add rendering hints (colormaps, legends, story hooks) under a `kfm:ui` block.

---

## 📚 Reference library (included in project files)

These project docs informed the expectations for **catalog-driven**, **contract-first**, **policy-gated**, and **provenance-first** STAC responses:

- 📘 KFM Data Intake (STAC/DCAT/PROV + profiles)
- 🧱 KFM Architecture & Design (UI transparency, offline packs)
- 🤖 KFM AI System Overview (Focus Mode citations + governance)
- 🗺️ KFM UI System Overview (client behaviors + provenance surfacing)
- 🧰 KFM Technical Documentation (FastAPI, OpenAPI, GraphQL, geospatial formats)
- 🧠 Idea packs & concept docs (Pulse Threads, OCI artifacts, future expansions)
- 📦 PDF portfolios (AI concepts, programming resources, data management, geospatial/webgl)

✅ Keep this README “contract-first”: it should tell future devs exactly what “good STAC responses” mean in KFM.
