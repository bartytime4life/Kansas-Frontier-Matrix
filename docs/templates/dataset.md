<div align="center">

# 🗃️ **Kansas Frontier Matrix — Dataset Documentation Template**  
`docs/templates/dataset.md`

**Mission:** Provide a **structured, reproducible template** for documenting datasets within the  
**Kansas Frontier Matrix (KFM)** — ensuring **provenance, FAIR compliance, MCP alignment, and STAC-ready metadata** across the full data lifecycle.

[![Docs · MCP-DL v6.3](https://img.shields.io/badge/Docs-MCP--DL%20v6.3-blue?logo=markdown)](../../docs/)
[![FAIR Principles](https://img.shields.io/badge/FAIR-Findable·Accessible·Interoperable·Reusable-brightgreen)](https://www.go-fair.org/fair-principles/)
[![STAC 1.0](https://img.shields.io/badge/STAC-1.0.0-blue)](https://stacspec.org/)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-lightgrey)](../../LICENSE)

</div>

---

```yaml
---
title: "Kansas Frontier Matrix — Dataset Documentation Template"
version: "v1.3.0"
last_updated: "2025-10-17"
owners: ["@kfm-data","@kfm-docs","@kfm-architecture"]
tags: ["dataset","documentation","stac","fair","mcp","provenance","dcat","metadata","ci"]
status: "Template"
license: "CC-BY 4.0"
semantic_alignment:
  - MCP-DL v6.3
  - STAC 1.0
  - DCAT 2.0
  - JSON Schema
  - ISO 19115 / ISO 8601
ci_required_checks:
  - stac-validate
  - checksums
  - docs-validate
  - pre-commit
  - codeql
  - trivy
---
```

---

## 🧭 Dataset Metadata (Front-Matter)

```yaml
# --- Machine-readable metadata block ---
dataset_id: DATASET-YYYY-NNN-<DOMAIN>-<NAME>
title: "<Full Descriptive Title>"
summary: "<Short abstract for site/catalog cards>"
authors:
  - name: "<Full Name>"
    role: "<Author / Engineer / Curator>"
curators:
  - name: "<Data Steward Team>"
contacts:
  - name: "<Primary Contact>"
    email: "<contact@org>"
doi: "<optional DOI>"
created: YYYY-MM-DD
updated: YYYY-MM-DD
version: "vX.Y.Z"
domain: "<Terrain|Hydrology|Climate|Landcover|Hazards|Tabular|Text|Mixed>"
data_type: "<Raster|Vector|Tabular|Text|Mixed>"
license: "<CC-BY 4.0|Public Domain|MIT|Custom>"
keywords: ["kansas","terrain","dem","example"]
spatial:
  crs: "EPSG:4326"
  bbox: [-102.05,36.99,-94.61,40.00]
temporal:
  start: "YYYY-MM-DD"
  end: "YYYY-MM-DD"
source_manifests:
  - path: data/sources/<domain>/<source>.json
checksums_manifest: data/checksums/<domain>/<dataset>.manifest.json
stac_items:
  - path: data/stac/<domain>/<dataset>.json
distribution:
  api_endpoints:
    - type: "stac-item"
      href: "/api/stac/items/<dataset_id>"
    - type: "download"
      href: "https://<host>/<path>/<file>"
sensitivity: "none|restricted|contains_sensitive_data"
retention_policy: "retain_3_versions_archive_rest"
# --- End metadata ---
```

---

## 🧩 Abstract / Description

> **Purpose:** Describe what this dataset represents, its intended use, and relevance to KFM.  
> Include **provenance**, **applications**, **limitations**, and **expected audience**.

**Example:**  
This dataset contains a 1m resolution Digital Elevation Model (DEM) derived from LiDAR (2018–2020) for Kansas.  
It supports hydrologic modeling, hazard assessment, and ecological studies.

---

## 🌐 Data Provenance & Sources

| Source | Provider | Access Method | License | Link / API | Notes |
| :------ | :-------- | :------------- | :-------- | :------------ | :------ |
| USGS 3DEP DEM | USGS | REST / HTTPS | Public Domain | https://elevation.nationalmap.gov | Tiles 2018–2020 |
| KS DASC LiDAR | Kansas DASC | FTP / HTTPS | CC-BY 4.0 | https://www.kansasgis.org | County mosaics |

> All sources must have corresponding manifests in `data/sources/<domain>/`.

---

## ⚙️ Processing Workflow (ETL → Products)

| Step | Description | Command / Script | Output |
| :---- | :------------ | :---------------- | :------ |
| 1 | Fetch raw data | `make fetch` | `data/raw/terrain/` |
| 2 | Reproject to EPSG:4326 | `gdalwarp -t_srs EPSG:4326` | GeoTIFF |
| 3 | Mosaic tiles | `gdal_merge.py -o ks_dem.tif ...` | `ks_dem.tif` |
| 4 | Convert to COG | `rio cogeo create ks_dem.tif ks_dem_cog.tif` | `ks_dem_cog.tif` |
| 5 | Derive hillshade/slope | `python src/pipelines/terrain/derive.py` | `hillshade.tif` |
| 6 | Create STAC | `python src/pipelines/load/stac_writer.py` | `data/stac/terrain/*.json` |

**Make targets**
```bash
make fetch && make process && make checksums && make stac-validate
```

---

## 🧮 Specifications & Schema

| Attribute | Description | Value |
| :---------- | :----------- | :----- |
| **Resolution** | Ground sample distance | 1 m |
| **CRS** | Coordinate Reference System | EPSG:4326 (WGS84) |
| **Extent (BBox)** | Spatial bounding box | [-102.05, 36.99, -94.61, 40.00] |
| **Coverage** | Temporal range | 2018-01-01 → 2020-12-31 |
| **Format** | Primary / Aux | GeoTIFF (COG), JSON (STAC) |
| **Size** | Approx total | 12 GB |
| **Encoding** | File encoding | UTF-8 / CSV / GeoTIFF |

**Data Dictionary (if applicable)**

| Field | Type | Units | Allowed Range | Description |
| :----- | :---- | :---- | :-------------- | :----------- |
| `elevation` | float32 | meters | ≥ -500 | Elevation above MSL |
| `slope_deg` | float32 | degrees | 0–90 | Derived slope |

---

## 🧾 Outputs & Distribution

| Type | Path / URL | Description |
| :----- | :----------- | :------------ |
| Primary | `data/processed/terrain/ks_1m_dem_2018_2020.tif` | Core raster |
| COG | `data/processed/terrain/ks_1m_dem_2018_2020_cog.tif` | Web-optimized raster |
| Derivatives | `data/processed/terrain/hillshade.tif` | Visualization layer |
| STAC Item | `data/stac/terrain/ks_1m_dem_2018_2020.json` | Catalog entry |
| Checksums | `data/checksums/terrain/ks_1m_dem_2018_2020.manifest.json` | Integrity report |
| Thumbnail | `data/processed/metadata/thumbnails/ks_1m_dem_2018_2020.png` | Web preview |

---

## ✅ Validation & QA

| Check | Tool / Method | Location | Result |
| :------ | :-------------- | :----------- | :------ |
| Checksum | `make checksums` | `data/checksums/` | ✅ |
| STAC Schema | `stac-validator` | `_reports/stac/` | ✅ |
| Spatial QA | `gdalinfo`, bounds check | `_reports/spatial/` | ✅ |
| CI/CD | `.github/workflows/stac-validate.yml` | Actions Logs | ✅ |

> Logs archived under `data/work/logs/<domain>/<dataset_id>/`.

---

## 🔗 Relationships & Dependencies

| Relation | Target | Type | Path / Reference |
| :-------- | :------- | :------ | :---------------- |
| Derived From | `usgs_3dep_dem` | Source | `data/sources/terrain/usgs_3dep_dem.json` |
| Feeds | `watersheds_huc12_2019` | Dependent | `data/processed/hydrology/watersheds_huc12_2019.geojson` |
| Referenced In | `ks_hillshade_2018_2020` | Derived | `data/processed/terrain/ks_hillshade_2018_2020.tif` |

---

## 🔐 Ethics, Legal & Licensing

- Dataset license: **CC-BY 4.0** (or specify).  
- Attribution required in derivative products.  
- No PII or sensitive data present.  
- Compliance with **USGS / DASC** distribution terms.  
- If licenses differ, describe **compatibility** and **exceptions**.

---

## 🧩 Integration with KFM Systems

| Component | Role | Integration Notes |
| :----------- | :------ | :---------------- |
| **Pipelines** | ETL & QA automation | `src/pipelines/<domain>/*` |
| **Metadata** | STAC integration | `data/stac/<domain>/*` |
| **CI/CD** | Validation, deploy, checksum | `.github/workflows/stac-validate.yml` |
| **Web Viewer** | Map layer config | `web/config/layers.json` |
| **Knowledge Graph** | Provenance relations | `src/graph/graph_loader.py` |

---

## 🔎 FAIR & Standards Mapping

| FAIR Principle | Implementation |
| :--------------- | :---------------- |
| **Findable** | STAC entries indexed and discoverable via search API |
| **Accessible** | Persistent URLs, Git-tracked metadata, API access |
| **Interoperable** | Open formats (COG, GeoJSON, CSV), EPSG codes, DCAT fields |
| **Reusable** | Licensing + citation guidance; full provenance |

**Optional DCAT/JSON-LD export:**  
Generated under `data/stac/<domain>/<dataset>_dcat.json`.

---

## 📌 Known Issues & Risks

- Tile seam artifacts (corrected via feathering).  
- Sparse LiDAR coverage in `{counties}`.  
- Large file sizes may limit low-bandwidth access.

---

## 🧯 Rollback & Retention

| Policy | Description |
| :------ | :------------- |
| **Retention** | Maintain last 3 published versions; archive older. |
| **Rollback** | Revert to prior STAC item + manifest. |
| **Deprecation** | Flag in STAC (`deprecated: true`) and cross-link replacement. |

---

## ✅ Acceptance Checklist

- [ ] STAC validation (schema + assets) ✅  
- [ ] Checksums verified for all outputs ✅  
- [ ] CRS, bbox, and QA passed ✅  
- [ ] Documentation updated + glossary links ✅  
- [ ] CI/CD workflows green ✅  

---

## 🧠 MCP Compliance Summary

| MCP Principle | Implementation |
| :--------------- | :--------------- |
| **Documentation-first** | Authored prior to publication. |
| **Reproducibility** | Deterministic pipelines with checksums. |
| **Open Standards** | STAC 1.0, GeoTIFF (COG), GeoJSON, JSON Schema. |
| **Provenance** | Linked source manifests, checksum lineage, graph nodes. |
| **Auditability** | CI/CD logs, QA reports, version history. |

---

## 📎 Related Documentation

| File | Description |
| :---- | :------------ |
| `docs/architecture/data-architecture.md` | Data model & lineage |
| `docs/templates/experiment.md` | Analytical experiment records |
| `docs/templates/sop.md` | Operational procedures |
| `.github/workflows/stac-validate.yml` | CI validation workflow |

---

## 🗓️ Version History

| Version | Date | Author | Summary |
| :------- | :----- | :-------- | :-------- |
| v1.3.0 | 2025-10-17 | KFM Docs Team | Added metadata YAML header, FAIR mapping, acceptance checklist, DCAT integration |
| v1.2.0 | 2025-10-10 | KFM Engineering | Improved schema table & integration sections |
| v1.1.0 | 2025-10-05 | KFM Data Team | Added QA/Validation and lineage relationships |
| v1.0.0 | 2025-10-04 | Documentation Team | Initial MCP-aligned dataset template |

---

<div align="center">

**Kansas Frontier Matrix © 2025**  
*"Every Dataset Accountable. Every Record Reproducible."*  
📍 `docs/templates/dataset.md` — MCP-compliant dataset documentation template for the Kansas Frontier Matrix.

</div>
