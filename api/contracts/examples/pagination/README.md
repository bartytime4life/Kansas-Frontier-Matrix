---
title: "Pagination Contract Examples"
description: "Cursor + offset pagination examples for KFM REST + GraphQL APIs."
status: "draft"
version: "kfm.pagination.v1"
last_updated: "2026-01-24"
owners:
  - "KFM Platform"
tags:
  - api
  - contracts
  - examples
  - pagination
  - cursor
  - offset
  - graphql
---

<p align="center">
  <img alt="Contract: KFM Pagination v1" src="./_badges/contract-kfm-pagination-v1.svg" />
  <img alt="Status: Draft" src="./_badges/status-draft.svg" />
  <img alt="Layer: API Contracts" src="./_badges/layer-api-contracts.svg" />
</p>

# 🔁 Pagination Contract Examples (KFM API)

These examples define **how list endpoints paginate** across **REST + GraphQL** in Kansas Frontier Matrix (KFM), supporting:
- 🧭 UI “infinite scroll” panels + lazy loading
- 📚 Story Nodes browsers & narrative content lists
- 🔎 Search/cross-filter results (time + map viewport)
- 🤖 Focus Mode evidence lists + traceable retrieval outputs

KFM explicitly leans on **lazy loading + caching** for performance, and exposes **REST + GraphQL** from a governed API boundary.  [oai_citation:0‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC) [oai_citation:1‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi) [oai_citation:2‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

---

## 🧭 Table of contents

- [📍 Location](#-location)
- [✅ Quick rules](#-quick-rules)
- [🗂️ Directory layout](#️-directory-layout)
- [🧩 The KFM list response envelope](#-the-kfm-list-response-envelope)
- [🧷 Pagination modes](#-pagination-modes)
- [🧪 Examples](#-examples)
  - [1) Cursor pagination (default)](#1-cursor-pagination-default)
  - [2) Offset pagination (admin/small lists)](#2-offset-pagination-adminsmall-lists)
  - [3) Since / incremental sync (watchers & realtime)](#3-since--incremental-sync-watchers--realtime)
  - [4) GraphQL connection pagination](#4-graphql-connection-pagination)
- [🛡️ Security, privacy, and governance](#️-security-privacy-and-governance)
- [🧰 Validation & contract tests](#-validation--contract-tests)
- [🧱 Design alignment notes](#-design-alignment-notes)
- [📚 Project docs used](#-project-docs-used)

---

## 📍 Location

This README lives at:

```text
📦 api/contracts/examples/pagination/README.md
```

---

## ✅ Quick rules

### 1) Prefer **cursor pagination** for anything user-facing
Cursor pagination is the default for high-cardinality, frequently updated result sets (search, events, entities, story nodes, AI evidence lists). It plays nicely with **infinite scroll** and avoids deep “page 900” scans.

### 2) Use **offset pagination** only for small, stable lists
Offset paging is acceptable for admin dashboards, exports, or small enumerations where “page N” UX matters more than scale.

### 3) Don’t paginate what should be **tiled** or **range-streamed**
For heavy geospatial/raster delivery, KFM uses:
- 🧩 Vector tiles (e.g., MVT) rather than “return 100k features”
- 🛰️ Cloud-Optimized GeoTIFF (COG) via HTTP range requests  
This is a performance cornerstone.  [oai_citation:3‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj) [oai_citation:4‡KFM- python-geospatial-analysis-cookbook-over-60-recipes-to-work-with-topology-overlays-indoor-routing-and-web-application-analysis-with-python.pdf](file-service://file-2gpiGDZS8iw6EdxGswEdHp)

---

## 🗂️ Directory layout

Recommended structure for pagination contract examples:

```text
📦 api/contracts/examples/pagination/
├─ 📄 README.md
├─ 🧾 cursor/
│  ├─ request.json
│  ├─ response.json
│  └─ errors.json
├─ 🧾 offset/
│  ├─ request.json
│  ├─ response.json
│  └─ errors.json
├─ 🧾 since/
│  ├─ request.json
│  ├─ response.json
│  └─ headers.md
├─ 🧾 graphql/
│  ├─ query.graphql
│  └─ response.json
└─ 🏷️ _badges/
   ├─ contract-kfm-pagination-v1.svg
   ├─ status-draft.svg
   └─ layer-api-contracts.svg
```

> 💡 This folder is “examples-first”: keep them copy/pasteable and usable in contract tests.

---

## 🧩 The KFM list response envelope

### REST list response (generic)

All paginated REST endpoints should return this **envelope shape** (resource-specific fields go in `data[]`):

```json
{
  "data": [],
  "page": {
    "mode": "cursor",
    "limit": 50,
    "cursor": null,
    "next_cursor": null,
    "prev_cursor": null,
    "has_more": false
  },
  "links": {
    "self": "/api/v1/resource?limit=50",
    "next": null,
    "prev": null
  },
  "meta": {
    "request_id": "req_01HTEXAMPLE",
    "generated_at": "2026-01-24T00:00:00Z",
    "as_of": null,
    "total_count": null,
    "approx_total_count": null
  },
  "provenance": {
    "policy_applied": true,
    "prov_refs": []
  }
}
```

### Field notes ✍️

- `page.mode`:
  - `"cursor"` (default)
  - `"offset"` (admin/small lists)
  - `"since"` (incremental sync / realtime watchers)
- `meta.total_count` is **optional** and may be omitted/null for:
  - performance (counts can be expensive), or
  - security (counts can leak information), or
  - policy constraints on restricted datasets.  [oai_citation:5‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)

---

## 🧷 Pagination modes

### Decision matrix 🧠

| Mode | Best for | Query params | Pros | Cons |
|---|---|---|---|---|
| 🔁 Cursor | Search results, entity lists, evidence lists, story nodes | `limit`, `cursor`, (`sort`) | Scales well, stable for infinite scroll | Harder to “jump to page 20” |
| 📄 Offset | Admin lists, small stable lists | `page`, `page_size`, (`sort`) | Familiar UX, easy to jump | Slow for deep pages, drift when data changes |
| ⏱️ Since | Streaming feeds, watcher outputs | `since`, `limit` | Great for polling & append-only feeds | Requires timestamp/sequence semantics |
| 🧩 Tiles / Range | Map rendering, rasters | `z/x/y`, HTTP range | Fast map UX | Not a list contract |

KFM supports real-time monitoring and watcher-style systems, so `"since"` style feeds are first-class in practice.  [oai_citation:6‡Data Mining Concepts & applictions.pdf](file-service://file-2uwEbQAFVKpXaTtWgUirAH)

---

## 🧪 Examples

### 1) Cursor pagination (default)

#### Request

```http
GET /api/v1/story-nodes?query=railroad&time_start=1860-01-01&time_end=1880-12-31&limit=2
```

> 📚 Story Nodes are a first-class KFM concept: narrative markdown + map-state JSON per node, sequenced into guided tours. 

#### Response

```json
{
  "data": [
    {
      "id": "sn_1860_railroads_intro",
      "title": "Railroads in Kansas (1860) — Baseline",
      "time_range": { "start": "1860-01-01", "end": "1860-12-31" },
      "summary": "Pre-expansion baseline conditions.",
      "refs": { "story_markdown": "/stories/railroads/sn_1860_railroads_intro.md" }
    },
    {
      "id": "sn_1870_railroads_growth",
      "title": "Railroads in Kansas (1870) — Expansion",
      "time_range": { "start": "1870-01-01", "end": "1870-12-31" },
      "summary": "New lines appear; trade networks shift.",
      "refs": { "story_markdown": "/stories/railroads/sn_1870_railroads_growth.md" }
    }
  ],
  "page": {
    "mode": "cursor",
    "limit": 2,
    "cursor": null,
    "next_cursor": "eyJ2IjoxLCJzIjoiZGVmYXVsdCIsImxhc3RfaWQiOiJzbl8xODcwX3JhaWxyb2Fkc19ncm93dGgifQ",
    "prev_cursor": null,
    "has_more": true
  },
  "links": {
    "self": "/api/v1/story-nodes?query=railroad&time_start=1860-01-01&time_end=1880-12-31&limit=2",
    "next": "/api/v1/story-nodes?query=railroad&time_start=1860-01-01&time_end=1880-12-31&limit=2&cursor=eyJ2IjoxLCJzIjoiZGVmYXVsdCIsImxhc3RfaWQiOiJzbl8xODcwX3JhaWxyb2Fkc19ncm93dGgifQ",
    "prev": null
  },
  "meta": {
    "request_id": "req_01HTEXAMPLE",
    "generated_at": "2026-01-24T00:00:00Z",
    "as_of": "2026-01-24T00:00:00Z",
    "total_count": null,
    "approx_total_count": 42
  },
  "provenance": {
    "policy_applied": true,
    "prov_refs": [
      { "type": "prov", "id": "prov_bundle_storynodes_20260124", "href": "/api/v1/prov/prov_bundle_storynodes_20260124" }
    ]
  }
}
```

✅ Cursor rules:
- The cursor is **opaque** to clients (don’t parse it; treat as a token).
- The backend must enforce **stable ordering** (always include a deterministic tie-breaker like `id`).  
This aligns with KFM’s “deterministic pipeline” expectations and contract-first discipline.  [oai_citation:7‡KFM- python-geospatial-analysis-cookbook-over-60-recipes-to-work-with-topology-overlays-indoor-routing-and-web-application-analysis-with-python.pdf](file-service://file-2gpiGDZS8iw6EdxGswEdHp) [oai_citation:8‡KFM- python-geospatial-analysis-cookbook-over-60-recipes-to-work-with-topology-overlays-indoor-routing-and-web-application-analysis-with-python.pdf](file-service://file-2gpiGDZS8iw6EdxGswEdHp)

---

### 2) Offset pagination (admin/small lists)

#### Request

```http
GET /api/v1/admin/datasets?page=3&page_size=25&sort=created_at&order=desc&include_total=true
```

#### Response

```json
{
  "data": [
    { "id": "ds_000251", "title": "County Boundaries (1890)", "created_at": "2025-12-10T18:00:00Z" }
  ],
  "page": {
    "mode": "offset",
    "page": 3,
    "page_size": 25,
    "total_pages": 19,
    "has_more": true
  },
  "links": {
    "self": "/api/v1/admin/datasets?page=3&page_size=25&sort=created_at&order=desc&include_total=true",
    "next": "/api/v1/admin/datasets?page=4&page_size=25&sort=created_at&order=desc&include_total=true",
    "prev": "/api/v1/admin/datasets?page=2&page_size=25&sort=created_at&order=desc&include_total=true"
  },
  "meta": {
    "request_id": "req_01HTEXAMPLE2",
    "generated_at": "2026-01-24T00:00:00Z",
    "as_of": null,
    "total_count": 463,
    "approx_total_count": null
  },
  "provenance": { "policy_applied": true, "prov_refs": [] }
}
```

⚠️ Offset guidance:
- Offset paging is easiest to misuse at scale.
- For user-facing results (search, map panels), prefer cursor.

---

### 3) Since / incremental sync (watchers & realtime)

KFM’s ingestion + monitoring concepts include watcher-like flows and realtime endpoints (example: transit).  [oai_citation:9‡Data Mining Concepts & applictions.pdf](file-service://file-2uwEbQAFVKpXaTtWgUirAH)

#### Request

```http
GET /api/v1/transport/buses?since=2026-01-24T00:00:00Z&limit=500
```

#### Response

```json
{
  "data": [
    {
      "id": "evt_bus_1706054401_0001",
      "ts": "2026-01-24T00:05:01Z",
      "type": "vehicle_position",
      "payload": { "vehicle_id": "bus_12", "lat": 39.05, "lon": -95.67 }
    }
  ],
  "page": {
    "mode": "since",
    "limit": 500,
    "since": "2026-01-24T00:00:00Z",
    "next_since": "2026-01-24T00:05:01Z",
    "has_more": true
  },
  "links": {
    "self": "/api/v1/transport/buses?since=2026-01-24T00:00:00Z&limit=500",
    "next": "/api/v1/transport/buses?since=2026-01-24T00:05:01Z&limit=500",
    "prev": null
  },
  "meta": {
    "request_id": "req_01HTEXAMPLE3",
    "generated_at": "2026-01-24T00:05:02Z",
    "as_of": null,
    "total_count": null,
    "approx_total_count": null
  },
  "provenance": { "policy_applied": true, "prov_refs": [] }
}
```

#### Headers (recommended) 🧾

For watcher endpoints, also support cache validators:
- `ETag`
- `Last-Modified`  
This is aligned with proposals for realtime “watchers” patterns. 

---

### 4) GraphQL connection pagination

KFM supports a governed API boundary and uses formal interface contracts (OpenAPI + GraphQL) with contract tests.  [oai_citation:10‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU) [oai_citation:11‡KFM- python-geospatial-analysis-cookbook-over-60-recipes-to-work-with-topology-overlays-indoor-routing-and-web-application-analysis-with-python.pdf](file-service://file-2gpiGDZS8iw6EdxGswEdHp)

#### Query

```graphql
query Search($q: String!, $first: Int!, $after: String) {
  search(q: $q, first: $first, after: $after) {
    totalCount
    edges {
      cursor
      node {
        id
        title
        type
        timeRange { start end }
      }
    }
    pageInfo {
      endCursor
      hasNextPage
    }
  }
}
```

#### Variables

```json
{ "q": "railroad", "first": 2, "after": null }
```

#### Response (example)

```json
{
  "data": {
    "search": {
      "totalCount": 42,
      "edges": [
        {
          "cursor": "eyJ2IjoxLCJsYXN0X2lkIjoic25fMTg2MF9yYWlscm9hZHNfaW50cm8ifQ",
          "node": {
            "id": "sn_1860_railroads_intro",
            "title": "Railroads in Kansas (1860) — Baseline",
            "type": "story_node",
            "timeRange": { "start": "1860-01-01", "end": "1860-12-31" }
          }
        },
        {
          "cursor": "eyJ2IjoxLCJsYXN0X2lkIjoic25fMTg3MF9yYWlscm9hZHNfZ3Jvd3RoIn0",
          "node": {
            "id": "sn_1870_railroads_growth",
            "title": "Railroads in Kansas (1870) — Expansion",
            "type": "story_node",
            "timeRange": { "start": "1870-01-01", "end": "1870-12-31" }
          }
        }
      ],
      "pageInfo": {
        "endCursor": "eyJ2IjoxLCJsYXN0X2lkIjoic25fMTg3MF9yYWlscm9hZHNfZ3Jvd3RoIn0",
        "hasNextPage": true
      }
    }
  }
}
```

---

## 🛡️ Security, privacy, and governance

KFM is explicitly designed to handle **sensitive data** with:
- location generalization (fuzz/coarsen coordinates),
- access controls,
- sensitivity tagging in metadata.  [oai_citation:12‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

Pagination can accidentally leak information. Guardrails:
- Avoid returning `total_count` for restricted queries unless policy explicitly allows it.
- Rate-limit deep paging attempts (offset) and cursor brute forcing.
- Consider “query auditing / inference control” strategies for sensitive outputs and repeated probing patterns.  [oai_citation:13‡Data Mining Concepts & applictions.pdf](file-service://file-2uwEbQAFVKpXaTtWgUirAH)

KFM’s AI and governance stack also references policy gates and OPA-style enforcement patterns.  [oai_citation:14‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)

---

## 🧰 Validation & contract tests

KFM documentation and interfaces are treated as **contract artifacts** and validated in CI (including docs with required sections and front-matter).  [oai_citation:15‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

Recommended checks for this folder:
1. ✅ JSON examples validate against schemas
2. ✅ OpenAPI examples compile + render
3. ✅ GraphQL schema examples validate
4. ✅ Contract tests run for pagination invariants:
   - stable ordering
   - cursor opacity
   - next/prev link correctness
   - policy does not leak counts/sensitive fields

KFM explicitly expects contract tests and versioning discipline for subsystems.  [oai_citation:16‡KFM- python-geospatial-analysis-cookbook-over-60-recipes-to-work-with-topology-overlays-indoor-routing-and-web-application-analysis-with-python.pdf](file-service://file-2gpiGDZS8iw6EdxGswEdHp) [oai_citation:17‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

---

## 🧱 Design alignment notes

This pagination contract supports:
- 🧭 A UI that uses **lazy loading** and **tile caching** for performance.  [oai_citation:18‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)
- 🧩 A backend that exposes **FastAPI REST + GraphQL** and integrates across data stores.  [oai_citation:19‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi) [oai_citation:20‡Scientific Method _ Research _ Master Coder Protocol Documentation.pdf](file-service://file-HTpax4QbDgguDwxwwyiS32)
- 🛰️ Geospatial delivery via **vector tiles (MVT)** and raster streaming instead of over-fetching.  [oai_citation:21‡KFM- python-geospatial-analysis-cookbook-over-60-recipes-to-work-with-topology-overlays-indoor-routing-and-web-application-analysis-with-python.pdf](file-service://file-2gpiGDZS8iw6EdxGswEdHp) [oai_citation:22‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)
- 🤖 AI retrieval that is **evidence-first** and “provenance-aware” (so lists may carry provenance references).  [oai_citation:23‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)

---

## 📚 Project docs used

> 🧷 File citations below are intentionally included so this README stays tied to the project’s source documents.

### Core KFM docs (system-required file cites)
- 🖥️ UI System Overview:  [oai_citation:24‡Kansas Frontier Matrix – Comprehensive UI System Overview.pdf](file-service://file-KcBQruYcoFVDEixzzRHTwt)
- 📥 Data Intake Guide:  [oai_citation:25‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)
- 💡 Innovative Concepts:  [oai_citation:26‡Innovative Concepts to Evolve the Kansas Frontier Matrix (KFM).pdf](file-service://file-G71zNoWKxsoSW44iwZaaCC)
- 🧾 Document Refinement Request:  [oai_citation:27‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)

### Additional KFM docs & libraries (local file cites)
- 🧭 KFM Architecture / Features / Design:  [oai_citation:28‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)
- 📘 KFM Technical Documentation:  [oai_citation:29‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)
- 🤖 KFM AI System Overview:  [oai_citation:30‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)
- 🌟 Latest Ideas & Future Proposals:  [oai_citation:31‡KFM- python-geospatial-analysis-cookbook-over-60-recipes-to-work-with-topology-overlays-indoor-routing-and-web-application-analysis-with-python.pdf](file-service://file-2gpiGDZS8iw6EdxGswEdHp)
- 🧠 Additional Project Ideas:  [oai_citation:32‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)
- 🗺️ Open-Source Geospatial Mapping Hub Design:  [oai_citation:33‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-64djFYQUCmxN1h6L6X7KUw)
- 📚 AI Concepts & more (portfolio):  [oai_citation:34‡AI Concepts & more.pdf](file-service://file-K6BctJjeUwvyCahLf9qdwr)
- 🗃️ Data Management (portfolio):  [oai_citation:35‡Data Managment-Theories-Architures-Data Science-Baysian Methods-Some Programming Ideas.pdf](file-service://file-RrXMFY7cP925exsQYermf2)
- 🗺️ Maps / Virtual Worlds / WebGL (portfolio):  [oai_citation:36‡Maps-GoogleMaps-VirtualWorlds-Archaeological-Computer Graphics-Geospatial-webgl.pdf](file-service://file-RshcX5sNY2wpiNjRfoP6z6)
- 🧰 Programming Languages & Resources (portfolio):  [oai_citation:37‡Various programming langurages & resources 1.pdf](file-service://file-4wp3wSSZs7gk5qHWaJVudi)

---
