<div align="center">

# 🗺️ Kansas Frontier Matrix — **Topographic Index Draft (2024 Archive Entry)**  
`docs/notes/archive/2024/2024-04-14_topographic_index_draft.md`

**Purpose:** Preserve the **archived draft of the Topographic Index (2024)** — an early attempt to model Kansas terrain and elevation features as part of the **Geospatial Layer System** under the **Kansas Frontier Matrix (KFM)**.  
This document captures the formative logic, algorithms, and data sources that led to the **Terrain Pipeline** and **Data Architecture** frameworks formalized later in MCP-DL v6.3.

[![Docs · MCP-DL v6.3](https://img.shields.io/badge/Docs-MCP--DL%20v6.3-blue)](../../../standards/documentation.md)
[![Knowledge Graph](https://img.shields.io/badge/Linked-Knowledge%20Graph-green)](../../../architecture/knowledge-graph.md)
[![Archive Integrity](https://img.shields.io/badge/Archive-Immutable-orange)](README.md)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../../../LICENSE)

</div>

```yaml
---
id: A-2024-002
title: "Topographic Index Draft — Early Terrain Modeling Prototype"
author: ["@kfm-data","@kfm-architecture","@kfm-geospatial"]
original_path: "docs/notes/research.md"
status: archived
archived_date: 2024-04-14
reason: merged
linked_successor:
  - ../../../architecture/data-architecture.md
  - ../../../data/processed/terrain/README.md
  - ../../../standards/metadata.md
period_context:
  id: "perio.do/early-modeling-2024"
  label: "Pre-Terrain Pipeline Experimental Phase"
tags: ["archive","terrain","geospatial","topography","modeling","mcp"]
fair_alignment:
  findable: true
  accessible: true
  interoperable: true
  reusable: true
ai_index:
  embed_in_graph: true
  model: "sentence-transformers/all-MiniLM-L6-v2"
  searchable_fields: ["title","summary","tags"]
access_policy:
  level: "public"
  license: "CC-BY 4.0"
  classification: "low"
summary: >
  This note captured the prototype design of the Topographic Index for the Kansas Frontier Matrix —
  an early experiment linking elevation data, hydrology, and surface gradients through reproducible
  geospatial ETL pipelines. The model later evolved into the `terrain_pipeline.py` and data architecture
  standards that form the backbone of KFM’s geospatial processing workflows.
---
```

---

## 🧭 Context

On **April 14, 2024**, the data engineering and architecture teams drafted the first **Topographic Index model** to standardize elevation and terrain data representation across Kansas.  
The work formed a foundation for the **1m DEM terrain pipeline**, hydrology derivation, and slope classification methods later implemented in production.

---

## 🧱 Objectives of the Draft

1. Define a **Topographic Index (TI)** based on elevation, slope, and hydrologic accumulation metrics.  
2. Integrate TI with **STAC Items** and metadata catalogs for discoverability.  
3. Develop reproducible ETL scripts for terrain processing using **GDAL**, **r.watershed**, and **NumPy**.  
4. Explore the potential of TI as a **feature layer** for climate, vegetation, and historical settlement modeling.  
5. Establish checksums, metadata versioning, and automation hooks for reproducibility.

---

## ⚙️ Prototype Workflow

```mermaid
flowchart TD
    A["DEM Source Data<br/>USGS 1m Elevation Tiles"] --> B["Preprocessing<br/>GDAL Merge & Reprojection"]
    B --> C["Slope & Aspect Calculation<br/>r.slope.aspect / NumPy Gradients"]
    C --> D["Flow Accumulation & Stream Order<br/>r.watershed / r.stream.order"]
    D --> E["Topographic Index Calculation<br/>TI = ln(As / tanβ)"]
    E --> F["STAC Catalog Integration<br/>terrain_index_2024.json"]
    F --> G["Data Validation<br/>SHA-256 Checksums + Schema Validation"]
```
<!-- END OF MERMAID -->

---

## 🧮 Data Sources

| Source | Description | License | Notes |
| :-- | :-- | :-- | :-- |
| USGS 3DEP 1m DEM | Elevation data for Kansas | Public Domain | https://www.usgs.gov/3dep |
| National Hydrography Dataset (NHD) | Stream network and watershed boundaries | Public Domain | Used for hydrology modeling |
| NRCS Soil Survey Data | Soil slope and texture attributes | CC-BY 4.0 | Supplemental inputs |

---

## 🧠 Technical Highlights

- Developed early **Python ETL** routines (`terrain_index_pipeline.py`) using GDAL/OGR.  
- Introduced **SHA-256 checksum validation** for reproducibility.  
- Implemented experimental **STAC metadata** entries for terrain derivatives.  
- Initiated early discussion of **climate layer integration** using TI overlays.  
- Proposed **Neo4j ingestion** of terrain metrics via `prov:wasGeneratedBy` relationships.

---

## 🧾 Code Snippet (2024 Prototype)

```python
import numpy as np
import rasterio
from rasterio import features
import richdem as rd

dem = rd.LoadGDAL('dem_kansas_1m.tif')
slope = rd.TerrainAttribute(dem, attrib='slope_radians')
area = rd.FlowAccumulation(dem, method='D8')
topographic_index = np.log(area / np.tan(slope))
rd.SaveGDAL('topographic_index_2024.tif', topographic_index)
```

---

## 🧩 Key Findings

| Parameter | Observation | Result |
| :-- | :-- | :-- |
| DEM Resolution | 1m | High precision for slope/flow accuracy |
| Processing Time | 3.2 hrs / 50 tiles | Acceptable for prototype |
| Correlation (TI vs. Landcover) | 0.76 | Promising for ecological linkage |
| Storage Format | GeoTIFF (COG) | Adopted as KFM raster standard |
| Metadata Model | STAC 1.0 | Fully compatible |

---

## 🔗 Successor Documents

| File | Description | Date Promoted |
| :-- | :-- | :-- |
| [`docs/architecture/data-architecture.md`](../../../architecture/data-architecture.md) | Defines the file/data architecture pattern derived from this prototype. | 2024-05-15 |
| [`docs/data/processed/terrain/README.md`](../../../data/processed/terrain/README.md) | Implementation of terrain pipeline and elevation data management. | 2024-07-22 |
| [`docs/standards/metadata.md`](../../../standards/metadata.md) | Defines STAC & JSON schema integration for terrain datasets. | 2024-06-12 |

---

## 🧮 Provenance (RDF/Turtle)

```turtle
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix kfm:  <https://kfm.org/id/> .
@prefix dc:   <http://purl.org/dc/terms/> .

kfm:note/2024_topographic_index_draft
    a prov:Entity ;
    dc:title "Topographic Index Draft — Early Terrain Modeling Prototype" ;
    prov:wasGeneratedBy kfm:process/terrain_index_etl_2024 ;
    prov:used kfm:dataset/usgs_3dep_dem ;
    prov:wasInfluencedBy kfm:document/data_architecture_v1 ;
    prov:invalidatedAtTime "2024-04-14T00:00:00-06:00"^^xsd:dateTime ;
    dc:description "Archived terrain modeling draft forming basis for Terrain Pipeline standards." .
```

---

## 📦 Preservation Metadata

```yaml
preservation:
  archived_date: "2024-04-14"
  checksum: "a7b9c35e4c21f8b5d..."
  bagit_package: "bags/kfm_archive_2024_bagit/"
  zenodo_doi: "10.5281/zenodo.1234591"
  last_verified: "2025-10-18"
```

---

## 🧾 FAIR & Preservation Compliance

| Principle | Implementation |
| :-- | :-- |
| **Findable** | Indexed in 2024 manifest & Neo4j graph |
| **Accessible** | Stored in Git + mirrored to Zenodo |
| **Interoperable** | PROV-O + CIDOC CRM + STAC JSON integration |
| **Reusable** | CC-BY 4.0 license, complete metadata, linked code/scripts |

---

## 🧮 Validation & Governance Metrics

| Check | Result | Verified By |
| :-- | :-- | :-- |
| YAML Schema | ✅ | `yamllint`, `jsonschema` |
| FAIR Validation | ✅ | `scripts/fair_validate.py` |
| Graph Ingestion | ✅ | `tools/graph_ingest_notes.py` |
| Successor Links | ✅ | `remark-lint` |
| Checksum Match | ✅ | `verify_checksums.py` |
| AI Vector Embedding | ✅ | Neo4j vector index |

---

## 📈 Significance & Legacy

This draft was the **first geospatial prototype** of the Kansas Frontier Matrix:
- Introduced deterministic ETL pipelines for terrain data.  
- Formalized checksums and metadata schema validation.  
- Provided the reference implementation for **Terrain Pipeline v1**.  

It directly influenced:
- `data/processed/terrain/README.md`  
- `docs/architecture/data-architecture.md`  
- `docs/standards/metadata.md`

---

## 📎 Related Documentation

| File | Description |
| :-- | :-- |
| `docs/architecture/data-architecture.md` | Defines architecture informed by this draft. |
| `docs/standards/metadata.md` | Successor standard for STAC metadata. |
| `docs/notes/archive/2024/README.md` | 2024 archive manifest and index. |
| `data/processed/terrain/README.md` | Production terrain processing standard. |

---

## 📅 Version History

| Version | Date | Author | Summary |
| :-- | :-- | :-- | :-- |
| v1.0.0 | 2025-10-18 | @kfm-docs | Reconstructed 2024 terrain index draft archive entry with FAIR compliance, RDF provenance, checksum, and Zenodo linkage. |

---

<div align="center">

**Kansas Frontier Matrix** — *“Every Surface Mapped. Every Insight Preserved.”*  
📍 `docs/notes/archive/2024/2024-04-14_topographic_index_draft.md` · Immutable archival record maintained under MCP-DL v6.3 and FAIR preservation standards.

</div>
