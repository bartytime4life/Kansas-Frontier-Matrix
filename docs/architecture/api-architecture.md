<div align="center">

# 🔌 Kansas Frontier Matrix — API Architecture  
`docs/architecture/api-architecture.md`

**Mission:** Describe the **API subsystem architecture** for the Kansas Frontier Matrix (KFM) —  
how data, metadata, and visualization assets are exposed, queried, and validated through  
standardized endpoints, ensuring **reproducibility, provenance, and interoperability**.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../docs/)
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](../../.github/workflows/stac-validate.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue)](../../LICENSE)

</div>

---

## 📚 Overview

The **KFM API Architecture** provides a **programmatic interface** to access the project’s  
datasets, STAC metadata, checksums, and visualization endpoints.  

It is designed around:
- 🌐 **Open standards** — STAC 1.0.0, REST, JSON Schema  
- 🧠 **Reproducible data lineage** — every response traceable to a checksum + metadata source  
- ⚙️ **Lightweight & stateless** — static API design for maximum reliability  
- 🔒 **Immutable versioning** — dataset URLs never change across releases  

This enables external applications, researchers, and web systems to query Kansas datasets  
directly from the KFM repository or associated GitHub Pages deployment.

---

## 🏗️ API Architecture Overview

```mermaid
flowchart TD
  A["🧩 STAC Catalog\n(data/stac/)"] --> B["🌐 API Gateway\n(api.kansasfrontiermatrix.org)"]
  B --> C["📦 Data Assets\n(data/processed/, data/tiles/)"]
  B --> D["📜 Metadata Responses\n(STAC Items & Collections)"]
  B --> E["📊 Statistics & Provenance\n(checksums/, sources/, logs/)"]
  B --> F["🧭 Web UI & External Clients\n(web/, MapLibre, Research APIs)"]

  style A fill:#fffbea,stroke:#e8a500
  style B fill:#eef7ff,stroke:#0077cc
  style C fill:#e8fff0,stroke:#33aa33
  style D fill:#f8f0ff,stroke:#8844cc
  style E fill:#f5f5f5,stroke:#888
  style F fill:#f0f8ff,stroke:#0088cc
````

<!-- END OF MERMAID -->

---

## 🧩 API Design Principles

| Principle               | Implementation                                                               |
| :---------------------- | :--------------------------------------------------------------------------- |
| **RESTful Structure**   | All endpoints follow predictable, versioned paths (`/api/v1/...`).           |
| **STAC-Driven**         | Catalog and search endpoints fully compatible with STAC 1.0.0 specification. |
| **Immutable URLs**      | Dataset URIs and STAC assets are permanent and versioned.                    |
| **Stateless Requests**  | No persistent sessions or cookies — every request is self-contained.         |
| **Schema Validation**   | All responses validated via JSON Schema and STAC validators.                 |
| **Provenance-Enforced** | Metadata responses include links to checksum and source manifests.           |

---

## ⚙️ API Endpoint Structure

```bash
/api/
├── v1/
│   ├── stac/                    # STAC-compliant endpoints
│   │   ├── catalog.json         # Root STAC catalog
│   │   ├── collections/         # List of all domain collections
│   │   │   ├── terrain.json
│   │   │   ├── hydrology.json
│   │   │   └── climate.json
│   │   └── search               # STAC API: /api/v1/stac/search?bbox=&datetime=
│   │
│   ├── data/                    # Direct dataset asset endpoints
│   │   ├── terrain/
│   │   │   └── ks_1m_dem_2018_2020.tif
│   │   ├── hydrology/
│   │   │   └── watersheds_huc12_2019.geojson
│   │   └── landcover/
│   │       └── nlcd_1992_2021.tif
│   │
│   ├── checksums/               # SHA-256 validation API
│   │   ├── terrain/
│   │   │   └── ks_1m_dem_2018_2020.tif.sha256
│   │   └── hydrology/
│   │       └── watersheds_huc12_2019.geojson.sha256
│   │
│   ├── sources/                 # Source manifest lookups
│   │   ├── terrain/usgs_3dep_dem.json
│   │   └── climate/noaa_daymet.json
│   │
│   ├── metadata/                # Aggregated metadata summary API
│   │   ├── terrain.json
│   │   ├── hydrology.json
│   │   └── climate.json
│   │
│   └── stats/                   # Statistical & diagnostic summaries
│       ├── counts.json
│       ├── domains.json
│       └── checksum_report.json
│
└── v2/                          # Reserved for future expansion (graph queries, OGC API)
```

---

## 🧾 Example Endpoints

| Function            | Endpoint                                                      | Description                                   |
| :------------------ | :------------------------------------------------------------ | :-------------------------------------------- |
| **STAC Catalog**    | `/api/v1/stac/catalog.json`                                   | Returns root catalog linking all collections. |
| **STAC Search**     | `/api/v1/stac/search?bbox=-102,36.9,-94.5,40.0&datetime=2020` | Spatial + temporal query for Kansas datasets. |
| **Dataset Access**  | `/api/v1/data/terrain/ks_1m_dem_2018_2020.tif`                | Direct file access via static endpoint.       |
| **Checksum**        | `/api/v1/checksums/terrain/ks_1m_dem_2018_2020.tif.sha256`    | Verifies data integrity for reproducibility.  |
| **Source Manifest** | `/api/v1/sources/terrain/usgs_3dep_dem.json`                  | Returns original data source metadata.        |
| **Stats Summary**   | `/api/v1/stats/domains.json`                                  | Lists all dataset categories and counts.      |

---

## 🔍 Example STAC Search Response

```json
{
  "type": "FeatureCollection",
  "features": [
    {
      "stac_version": "1.0.0",
      "id": "ks_1m_dem_2018_2020",
      "properties": {
        "title": "Kansas LiDAR DEM (1m)",
        "datetime": "2020-01-01T00:00:00Z",
        "license": "Public Domain (USGS 3DEP)",
        "themes": ["terrain", "elevation"],
        "providers": [
          {"name": "USGS 3DEP", "roles": ["producer"]},
          {"name": "Kansas DASC", "roles": ["processor"]}
        ]
      },
      "assets": {
        "data": {
          "href": "/api/v1/data/terrain/ks_1m_dem_2018_2020.tif",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized"
        },
        "checksum": {
          "href": "/api/v1/checksums/terrain/ks_1m_dem_2018_2020.tif.sha256"
        },
        "metadata": {
          "href": "/api/v1/sources/terrain/usgs_3dep_dem.json"
        }
      },
      "bbox": [-102.05, 36.99, -94.59, 40.00]
    }
  ]
}
```

---

## 🧮 Internal Validation & Logging

| Validation Layer    | Description                                                           | Workflow                                    |
| :------------------ | :-------------------------------------------------------------------- | :------------------------------------------ |
| **STAC Validation** | Confirms all API metadata complies with STAC schema.                  | `.github/workflows/stac-validate.yml`       |
| **Checksum Sync**   | Verifies that all API checksum files match processed datasets.        | `.github/workflows/checksums.yml`           |
| **Link Integrity**  | Tests all `/api/v1/data/` and `/api/v1/stac/` URLs for 200 responses. | `make api-validate`                         |
| **Usage Logging**   | Tracks request counts, timestamps, and response status for auditing.  | Logged to `data/work/logs/api_requests.log` |

---

## 🧠 Security & Access

| Feature                      | Description                                                         |
| :--------------------------- | :------------------------------------------------------------------ |
| **Rate Limiting**            | Static APIs throttle large bulk requests to prevent abuse.          |
| **HTTPS Only**               | All endpoints are served via secure HTTPS on production.            |
| **No Authentication Needed** | All data is open-access under CC-BY 4.0 / Public Domain.            |
| **Immutable Assets**         | Data files are versioned and cannot be modified retroactively.      |
| **CORS Enabled**             | Allows open web clients (e.g., MapLibre) to load datasets directly. |

---

## 🧩 Integration with Other Systems

| System                   | Integration Type                        | Description                                                   |
| :----------------------- | :-------------------------------------- | :------------------------------------------------------------ |
| **Web Viewer**           | Tile + metadata endpoints               | Loads map tiles + STAC data dynamically.                      |
| **ETL Pipelines**        | Source manifests + validation endpoints | Fetches and verifies datasets programmatically.               |
| **External Researchers** | REST API                                | Provides direct dataset access for reproducible research.     |
| **STAC Federation**      | Linked catalogs                         | Compatible with external STAC aggregators (NASA, NOAA, USGS). |

---

## 🧠 MCP Compliance Summary

| MCP Principle           | Implementation                                                                   |
| :---------------------- | :------------------------------------------------------------------------------- |
| **Documentation-first** | Every endpoint defined and documented in this architecture file.                 |
| **Reproducibility**     | Deterministic API structure; versioned static data ensures consistent responses. |
| **Open Standards**      | STAC 1.0.0, JSON Schema, RESTful design principles.                              |
| **Provenance**          | Every API response includes direct links to checksums and source manifests.      |
| **Auditability**        | All API requests logged in `data/work/logs/` for traceability.                   |

---

## 📎 Related Documentation

| Path                                       | Description                                  |
| :----------------------------------------- | :------------------------------------------- |
| `docs/architecture/architecture.md`        | Full system and CI/CD architecture overview. |
| `docs/architecture/data-architecture.md`   | Data and STAC subsystem architecture.        |
| `docs/architecture/web-ui-architecture.md` | Web and visualization architecture.          |
| `data/stac/README.md`                      | STAC catalog schema and metadata design.     |
| `.github/workflows/stac-validate.yml`      | STAC compliance workflow for API endpoints.  |

---

## 📅 Version History

| Version | Date       | Summary                                                         |
| :------ | :--------- | :-------------------------------------------------------------- |
| v1.0    | 2025-10-04 | Initial API architecture documentation (STAC + REST endpoints). |

---

<div align="center">

**Kansas Frontier Matrix** — *“Every Endpoint Proven. Every Response Reproducible.”*
📍 [`docs/architecture/api-architecture.md`](.) · API design and metadata access documentation for the Kansas Frontier Matrix.

</div>
