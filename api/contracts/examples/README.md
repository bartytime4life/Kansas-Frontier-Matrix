---
title: "KFM API Contract Examples"
version: "v1.0.0"
status: "active"
doc_kind: "Developer Guide"
last_updated: "2026-01-12"
license: "CC-BY-4.0"
fair_category: "FAIR+CARE"
care_label: "Public"
sensitivity: "public"
classification: "open"
doc_uuid: "urn:kfm:doc:api:contracts:examples:v1.0.0"
---

# 🧾 KFM API Contract Examples

![contract-first](https://img.shields.io/badge/contract--first-%E2%9C%94-brightgreen)
![openapi](https://img.shields.io/badge/OpenAPI-3.x-blue)
![graphql](https://img.shields.io/badge/GraphQL-enabled-ff69b4)
![metadata](https://img.shields.io/badge/metadata-STAC%20%7C%20DCAT%20%7C%20PROV-orange)
![governance](https://img.shields.io/badge/FAIR%2BCARE-governed-purple)

> [!IMPORTANT]
> This folder contains **golden example payloads** (fixtures) used to validate **API contracts** and **metadata profiles** in CI.
> If you change a response shape, add a new endpoint, or adjust metadata rules — **update the contract** *and* update at least one example here. ✅

---

<details>
<summary>📚 Table of Contents</summary>

- [Why this folder exists](#-why-this-folder-exists)
- [Directory layout](#-directory-layout)
- [Golden-example rules](#-golden-example-rules)
- [KFM-wide conventions these examples must follow](#-kfm-wide-conventions-these-examples-must-follow)
  - [Identifiers](#identifiers)
  - [CRS and geometry](#crs-and-geometry)
  - [Provenance-first (PROV) and catalogs (STAC/DCAT)](#provenance-first-prov-and-catalogs-stacdcat)
  - [Focus Mode safety + transparency rules](#focus-mode-safety--transparency-rules)
  - [Versioning](#versioning)
- [Example catalog](#-example-catalog)
- [Example payload snippets](#-example-payload-snippets)
  - [1) STAC Item](#1-stac-item)
  - [2) DCAT Dataset](#2-dcat-dataset)
  - [3) PROV Bundle](#3-prov-bundle)
  - [4) Focus Mode ask/answer](#4-focus-mode-askanswer)
  - [5) Async job status (analysis/simulation)](#5-async-job-status-analysissimulation)
  - [6) Error envelope](#6-error-envelope)
  - [7) Cursor pagination](#7-cursor-pagination)
- [How validation typically works](#-how-validation-typically-works)
- [Adding a new example](#-adding-a-new-example)
- [Glossary](#-glossary)
- [Project library references](#-project-library-references)

</details>

---

## 🎯 Why this folder exists

KFM is built around **clear, stable, and testable contracts**:

- REST endpoints are **OpenAPI-documented** (Swagger) and return **JSON** (GeoJSON for geodata).  
- Graph access is also available via **GraphQL** for flexible retrieval.  
- Published datasets are discoverable via **open standards**:
  - **STAC** (SpatioTemporal Asset Catalog) records per dataset
  - **DCAT** feed for discovery
  - **PROV-O JSON-LD** for lineage and accountability  
- Outputs use common geospatial formats like **GeoJSON** (vector) and **COG** (Cloud-Optimized GeoTIFF) for rasters.

These examples are the **shared “truth snapshots”** that keep implementation, docs, and clients aligned as the system evolves.

---

## 🗂️ Directory layout

> [!NOTE]
> The exact subfolders may evolve, but the intent stays the same: **examples mirror contracts**.

Recommended structure inside `api/contracts/examples/`:

```text
api/
└── 📜 contracts/
    ├── 📘 openapi/                 # OpenAPI specs (source of truth for REST endpoints)
    ├── 🧬 graphql/                 # GraphQL schema (source of truth for GraphQL surface)
    ├── 📐 schemas/                 # JSON Schemas (STAC/DCAT/PROV + KFM-specific object contracts)
    └── 🧪 examples/                # ✅ You are here 📌 Canonical example payloads (docs + tests; must validate)
        ├── 🛰️ stac/                # STAC examples (Collections/Items/Assets; profile-compliant)
        ├── 🗂️ dcat/                # DCAT examples (Dataset/Distribution JSON-LD; license/access correct)
        ├── 🧬 prov/                # PROV examples (PROV-O JSON-LD bundles; linkage to runs/artifacts)
        ├── 🗺️ geojson/             # GeoJSON examples (features, bbox, CRS assumptions; small fixtures)
        ├── 🔎 focus/               # Focus Mode examples (request/answer envelopes; citations + redaction notices)
        ├── 🧵 jobs/                # Async job examples (job refs, status/progress, result pointers)
        ├── 🚨 errors/              # Error examples (Problem Details, validation errors, policy denials)
        ├── 📑 pagination/          # Pagination examples (cursor requests/responses, sorting, limits)
        └── 🧬 graphql/             # GraphQL examples (operations + expected response shapes)
```

**Naming convention (recommended):**

- `type__id__variant.json` (double underscores make grep-friendly filenames)
- Prefer `snake_case` for variants  
- Example:
  - `stac/item__kfm.ks.landcover.2000_2020.v1__public.json`
  - `errors/error__not_found__dataset.json`
  - `focus/answer__explain_layer__with_citations.json`

---

## 🧪 Golden-example rules

Golden examples should be:

- ✅ **Minimal but complete** (include required fields + representative optional fields)
- ✅ **Deterministic** (avoid “now” timestamps, random UUIDs, nondeterministic ordering)
- ✅ **Sanitized** (no secrets, no personal data, no sensitive locations)
- ✅ **Cross-linked** (IDs align across STAC/DCAT/PROV/Graph)
- ✅ **Machine-validatable** against the relevant schema/contract

> [!TIP]
> Use obviously fake but valid values:
> - UUID: `00000000-0000-4000-8000-000000000000`
> - Hostnames: `https://api.kfm.example/...`
> - Hashes: `sha256:deadbeef...` (correct length if the schema checks it)

---

## 🧩 KFM-wide conventions these examples must follow

### Identifiers

Dataset IDs should follow the documented pattern:

`kfm.<state|region>.<theme>.<year_range>.v<version>`

Example: `kfm.ks.landcover.2000_2020.v1`

**Why it matters:** the same ID often appears in:

- STAC `id`
- DCAT `dct:identifier`
- PROV entity identifiers
- database keys / layer registry / graph edges

---

### CRS and geometry

- **Web delivery default:** WGS84 / EPSG:4326  
- **Original CRS must be preserved in metadata**, and any reprojection should be recorded in provenance.

> [!IMPORTANT]
> If an example contains geometry, keep it **simple** and **valid**:
> - polygons must be closed
> - bbox must match geometry bounds
> - prefer Kansas bounding boxes for KS-wide layers

---

### Provenance-first (PROV) and catalogs (STAC/DCAT)

**Expectation:** Every “published” dataset should have:

- **STAC record** (spatial + temporal extent, license, assets/links)
- **PROV record** (how it was produced, by whom/what, from which sources)
- **DCAT entry** (discovery + distributions)

This repo treats provenance as a **first-class contract** — not an afterthought.

---

### Focus Mode safety + transparency rules

Focus Mode is a governed AI assistant:

- AI content is **opt-in** and **clearly labeled**
- responses include **citations** (no new claims without sources)
- **no sensitive location leaks** — coordinates may be generalized/blurred/omitted
- include a **confidence / uncertainty indicator** where applicable

---

### Versioning

Contracts are **versioned** and changes must be explicit:

- **Breaking API changes** require a version bump (e.g., `/v2/...`), or a documented negotiation strategy.
- **Graph/ontology changes** require migration scripts and integrity checks.
- The repository itself follows semantic versioning for large structural shifts.

---

## 🧾 Example catalog

| Folder 📂 | What it demonstrates ✅ | Typical formats |
|---|---|---|
| `stac/` | STAC Items + Collections + assets for vector/raster | `.json` |
| `dcat/` | Dataset discovery (JSON-LD), distributions | `.jsonld` |
| `prov/` | Lineage bundles (ETL runs, PR events, model runs) | `.jsonld` |
| `geojson/` | FeatureCollections, Feature properties conventions | `.json` |
| `focus/` | Ask payload + answer w/ citations + redactions | `.json` |
| `jobs/` | async job create/status + output dataset linking | `.json` |
| `errors/` | standard error envelope shapes | `.json` |
| `pagination/` | cursor + link patterns for large responses | `.json` |
| `graphql/` | query docs + expected response shapes | `.graphql`, `.json` |

---

## 🧩 Example payload snippets

> [!NOTE]
> These are **snippets** to show “shape” and conventions. The real examples in this folder should match the current schemas and contracts.

### 1) STAC Item

```json
{
  "type": "Feature",
  "stac_version": "1.0.0",
  "id": "kfm.ks.landcover.2000_2020.v1",
  "collection": "kfm.ks.landcover.v1",
  "bbox": [-102.051, 36.993, -94.588, 40.003],
  "geometry": {
    "type": "Polygon",
    "coordinates": [
      [
        [-102.051, 36.993],
        [-94.588, 36.993],
        [-94.588, 40.003],
        [-102.051, 40.003],
        [-102.051, 36.993]
      ]
    ]
  },
  "properties": {
    "datetime": "2020-01-01T00:00:00Z",
    "start_datetime": "2000-01-01T00:00:00Z",
    "end_datetime": "2020-12-31T23:59:59Z",
    "license": "CC-BY-4.0",
    "proj:epsg": 4326,

    "kfm:dataset_id": "kfm.ks.landcover.2000_2020.v1",
    "kfm:theme": "landcover",
    "kfm:provenance_bundle": "urn:kfm:prov:etl:kfm.ks.landcover.2000_2020.v1:run:00000000-0000-4000-8000-000000000000"
  },
  "assets": {
    "cog": {
      "href": "https://api.kfm.example/assets/kfm.ks.landcover.2000_2020.v1/cog.tif",
      "type": "image/tiff; application=geotiff; profile=cloud-optimized",
      "roles": ["data"],
      "title": "COG raster"
    },
    "vector": {
      "href": "https://api.kfm.example/assets/kfm.ks.landcover.2000_2020.v1/features.geojson",
      "type": "application/geo+json",
      "roles": ["data"],
      "title": "Vectorized polygons (if applicable)"
    },
    "metadata": {
      "href": "https://api.kfm.example/stac/items/kfm.ks.landcover.2000_2020.v1",
      "type": "application/json",
      "roles": ["metadata"]
    }
  },
  "links": [
    { "rel": "self", "href": "https://api.kfm.example/stac/items/kfm.ks.landcover.2000_2020.v1" },
    { "rel": "collection", "href": "https://api.kfm.example/stac/collections/kfm.ks.landcover.v1" }
  ]
}
```

---

### 2) DCAT Dataset

```json
{
  "@context": {
    "dcat": "http://www.w3.org/ns/dcat#",
    "dct": "http://purl.org/dc/terms/",
    "prov": "http://www.w3.org/ns/prov#",
    "xsd": "http://www.w3.org/2001/XMLSchema#"
  },
  "@id": "urn:kfm:dataset:kfm.ks.landcover.2000_2020.v1",
  "@type": "dcat:Dataset",
  "dct:identifier": "kfm.ks.landcover.2000_2020.v1",
  "dct:title": "Kansas Land Cover (2000–2020)",
  "dct:description": "Land cover classification for Kansas; public example fixture.",
  "dct:license": "CC-BY-4.0",
  "dct:temporal": {
    "@type": "dct:PeriodOfTime",
    "dcat:startDate": { "@value": "2000-01-01", "@type": "xsd:date" },
    "dcat:endDate": { "@value": "2020-12-31", "@type": "xsd:date" }
  },
  "dcat:distribution": [
    {
      "@type": "dcat:Distribution",
      "dct:title": "STAC Item",
      "dcat:downloadURL": "https://api.kfm.example/stac/items/kfm.ks.landcover.2000_2020.v1",
      "dcat:mediaType": "application/json"
    },
    {
      "@type": "dcat:Distribution",
      "dct:title": "Cloud-Optimized GeoTIFF",
      "dcat:downloadURL": "https://api.kfm.example/assets/kfm.ks.landcover.2000_2020.v1/cog.tif",
      "dcat:mediaType": "image/tiff"
    }
  ],
  "prov:wasGeneratedBy": {
    "@id": "urn:kfm:prov:etl:kfm.ks.landcover.2000_2020.v1:run:00000000-0000-4000-8000-000000000000"
  }
}
```

---

### 3) PROV Bundle

```json
{
  "@context": {
    "prov": "http://www.w3.org/ns/prov#",
    "dct": "http://purl.org/dc/terms/",
    "kfm": "urn:kfm:ns:",
    "xsd": "http://www.w3.org/2001/XMLSchema#"
  },
  "@id": "urn:kfm:prov:etl:kfm.ks.landcover.2000_2020.v1:run:00000000-0000-4000-8000-000000000000",
  "@type": "prov:Bundle",
  "prov:activity": {
    "urn:kfm:activity:etl:landcover:00000000-0000-4000-8000-000000000000": {
      "@type": "prov:Activity",
      "prov:startedAtTime": "2026-01-12T00:00:00Z",
      "prov:endedAtTime": "2026-01-12T00:05:00Z",
      "prov:wasAssociatedWith": "urn:kfm:agent:ci:runner",
      "kfm:git_sha": "deadbeefdeadbeefdeadbeefdeadbeefdeadbeef",
      "kfm:openlineage_run_uuid": "00000000-0000-4000-8000-000000000000"
    }
  },
  "prov:entity": {
    "urn:kfm:entity:stac:item:kfm.ks.landcover.2000_2020.v1": {
      "@type": "prov:Entity",
      "dct:identifier": "kfm.ks.landcover.2000_2020.v1",
      "kfm:content_type": "application/json",
      "kfm:sha256": "deadbeefdeadbeefdeadbeefdeadbeefdeadbeefdeadbeefdeadbeefdeadbeef"
    }
  },
  "prov:agent": {
    "urn:kfm:agent:ci:runner": {
      "@type": "prov:Agent",
      "prov:label": "KFM CI Runner (example)",
      "kfm:agent_kind": "service"
    }
  },
  "prov:wasGeneratedBy": [
    {
      "prov:entity": "urn:kfm:entity:stac:item:kfm.ks.landcover.2000_2020.v1",
      "prov:activity": "urn:kfm:activity:etl:landcover:00000000-0000-4000-8000-000000000000"
    }
  ]
}
```

> [!TIP]
> PROV examples should be good enough to answer: “**Which code version produced this dataset, and who/what ran it?**”

---

### 4) Focus Mode ask/answer

**Request (`focus/ask__...json`)**

```json
{
  "question": "Explain what this layer shows and how trustworthy it is.",
  "context": {
    "selected_dataset_ids": ["kfm.ks.landcover.2000_2020.v1"],
    "map_view": {
      "mode": "2d",
      "center": [-98.0, 38.5],
      "zoom": 6,
      "time": "2020-01-01"
    },
    "selection": {
      "type": "bbox",
      "bbox": [-99.0, 38.0, -97.0, 39.0]
    }
  },
  "options": {
    "citations": true,
    "response_format": "markdown",
    "ai_opt_in": true
  }
}
```

**Response (`focus/answer__...json`)**

```json
{
  "ai_generated": true,
  "confidence": 0.73,
  "answer_markdown": "This layer summarizes land cover classes for Kansas from 2000–2020…",
  "citations": [
    {
      "kind": "dataset",
      "dataset_id": "kfm.ks.landcover.2000_2020.v1",
      "stac_item": "https://api.kfm.example/stac/items/kfm.ks.landcover.2000_2020.v1",
      "prov_bundle": "urn:kfm:prov:etl:kfm.ks.landcover.2000_2020.v1:run:00000000-0000-4000-8000-000000000000"
    }
  ],
  "redactions": [
    {
      "rule": "no_sensitive_location_leaks",
      "applied": false,
      "note": "No sensitive features detected for this request."
    }
  ],
  "meta": {
    "request_id": "req_00000000-0000-4000-8000-000000000000",
    "trace_id": "trace_00000000-0000-4000-8000-000000000000"
  }
}
```

---

### 5) Async job status (analysis/simulation)

> [!IMPORTANT]
> Long-running work (ETL, analytics, model runs) should produce:
> - a **job record**
> - a **published output dataset** (STAC/DCAT)
> - **VVUQ-style evidence** (verification, validation, uncertainty)

```json
{
  "job_id": "job_00000000-0000-4000-8000-000000000000",
  "kind": "simulation",
  "status": "succeeded",
  "submitted_at": "2026-01-12T00:00:00Z",
  "started_at": "2026-01-12T00:00:05Z",
  "completed_at": "2026-01-12T00:04:59Z",

  "inputs": {
    "model_id": "urn:kfm:model:example:hydrology:v1",
    "scenario": "baseline",
    "parameters": {
      "time_step_seconds": 60,
      "duration_seconds": 86400
    }
  },

  "outputs": {
    "dataset_id": "kfm.ks.hydrology.simulation.baseline.2026_01_12.v1",
    "stac_item": "https://api.kfm.example/stac/items/kfm.ks.hydrology.simulation.baseline.2026_01_12.v1"
  },

  "vv": {
    "verification": {
      "summary": "Numerical solver regression tests passed.",
      "evidence_uri": "https://api.kfm.example/evidence/verification/job_00000000-0000-4000-8000-000000000000.json"
    },
    "validation": {
      "summary": "Compared against historical observations; within acceptable bounds for public example.",
      "evidence_uri": "https://api.kfm.example/evidence/validation/job_00000000-0000-4000-8000-000000000000.json"
    }
  },

  "uq": {
    "method": "monte_carlo",
    "trials": 500,
    "seed_range": [1, 500],
    "summary": {
      "metric": "peak_flow",
      "unit": "m3/s",
      "confidence_interval_95": [120.1, 156.7]
    }
  },

  "provenance": {
    "prov_bundle_id": "urn:kfm:prov:simulation:job_00000000-0000-4000-8000-000000000000",
    "openlineage_run_uuid": "00000000-0000-4000-8000-000000000000",
    "git_sha": "deadbeefdeadbeefdeadbeefdeadbeefdeadbeef"
  }
}
```

---

### 6) Error envelope

> [!TIP]
> Use a consistent error shape across REST endpoints to improve SDK ergonomics and observability.

```json
{
  "error": {
    "code": "NOT_FOUND",
    "message": "Dataset not found.",
    "details": {
      "dataset_id": "kfm.ks.landcover.1999_2001.v1"
    }
  },
  "meta": {
    "request_id": "req_00000000-0000-4000-8000-000000000000",
    "trace_id": "trace_00000000-0000-4000-8000-000000000000"
  }
}
```

---

### 7) Cursor pagination

```json
{
  "data": [
    { "dataset_id": "kfm.ks.example.1900_1910.v1" },
    { "dataset_id": "kfm.ks.example.1910_1920.v1" }
  ],
  "page": {
    "limit": 2,
    "next_cursor": "cursor_eyJvZmZzZXQiOjJ9"
  },
  "links": [
    { "rel": "self", "href": "https://api.kfm.example/v1/datasets?limit=2" },
    { "rel": "next", "href": "https://api.kfm.example/v1/datasets?limit=2&cursor=cursor_eyJvZmZzZXQiOjJ9" }
  ],
  "meta": {
    "request_id": "req_00000000-0000-4000-8000-000000000000"
  }
}
```

---

## ✅ How validation typically works

A contract-first repo usually enforces gates like:

- **OpenAPI validation** (spec lint + breaking-change detection)
- **GraphQL schema validation** (schema checks + query/response fixtures)
- **JSON Schema validation** for STAC/DCAT/PROV + KFM-specific objects
- **Policy gates** (FAIR/CARE, sensitivity rules, redaction rules)
- **Contract tests** (examples must match real API behavior)
- **Graph integrity checks** (ontology constraints, fixture graph tests)

> [!NOTE]
> Your repo may implement these checks via `pytest`, `conftest` (OPA/Rego), JSON-schema tooling, and CI workflows.
> The exact command entrypoints can vary — the *goal* is non-negotiable: **examples must stay in lockstep with contracts.**

---

## ➕ Adding a new example

**Checklist ✅**

- [ ] Update the contract first (`api/contracts/openapi/` or `api/contracts/graphql/` or `api/contracts/schemas/`)
- [ ] Add at least one example fixture in this folder
- [ ] Ensure IDs are consistent (`kfm.<region>.<theme>.<year_range>.v#`)
- [ ] Ensure geometry is valid and CRS is declared
- [ ] Add provenance links (STAC ↔ DCAT ↔ PROV)
- [ ] Strip/replace nondeterministic fields (timestamps, UUIDs) with stable fixtures
- [ ] Confirm **no sensitive data** is present (coordinates, PII, credentials)
- [ ] Run the validators/tests locally (or verify CI gate output in the PR)

**Recommended workflow (pattern):**

1) Call local API (or build payload)  
2) Normalize JSON (stable formatting)  
3) Save into the appropriate folder  
4) Ensure it validates against the relevant schema

---

## 📘 Glossary

- **STAC**: SpatioTemporal Asset Catalog (dataset metadata + asset links)
- **DCAT**: Data Catalog Vocabulary (discovery metadata, often JSON-LD)
- **PROV(-O)**: W3C provenance ontology (lineage + accountability, often JSON-LD)
- **GeoJSON**: Standard JSON format for vector geometries and features
- **COG**: Cloud-Optimized GeoTIFF (raster optimized for HTTP range requests)
- **VVUQ**: Verification, Validation, and Uncertainty Quantification
- **FAIR+CARE**: Findable/Accessible/Interoperable/Reusable + Collective Benefit/Authority/Responsibility/Ethics

---

## 📚 Project library references

<details>
<summary>🧠 Why the project “book shelf” influences API contracts</summary>

This folder’s examples are shaped by project-wide priorities: **reproducibility, provenance, interoperability, and safe delivery**.  
The reference library supports that by informing what “good contracts” look like across disciplines:

- 🛰️ **Remote sensing & geospatial delivery:** vector vs raster patterns, asset formats, and metadata expectations  
- 🧭 **Cartography & UI:** what the front-end needs to render correctly (legends, layer metadata, time navigation)  
- 🧪 **Statistics & modeling:** how to report results credibly (effect sizes, uncertainty, replication-minded outputs)  
- 🧠 **AI & governance:** transparency, opt-in AI, sovereignty, compliance, and auditability  
- 🔐 **Security & resilience:** safe error envelopes, policy gates, and supply-chain integrity  
- ⚙️ **Scalability:** pagination, caching hints, query ergonomics, and traceability fields

</details>
