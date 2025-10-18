<div align="center">

# 🗃️ **Kansas Frontier Matrix — Dataset Documentation Template**  
`docs/templates/dataset.md`

**Mission:** Provide a **structured, reproducible template** for documenting datasets within the  
**Kansas Frontier Matrix (KFM)** — ensuring **provenance, FAIR compliance, MCP alignment, security hardening, and STAC-ready metadata** across the full data lifecycle.

[![Docs · MCP-DL v6.3](https://img.shields.io/badge/Docs-MCP--DL%20v6.3-blue?logo=markdown)](../../docs/)
[![Docs-Validate](https://img.shields.io/badge/docs-validated-brightgreen?logo=github)](../../.github/workflows/docs-validate.yml)
[![STAC 1.0](https://img.shields.io/badge/STAC-1.0.0-blue)](https://stacspec.org/)
[![Policy-as-Code](https://img.shields.io/badge/policy-OPA%2FConftest-purple)](../../.github/workflows/policy-check.yml)
[![Security](https://img.shields.io/badge/security-CodeQL%20%7C%20Trivy%20%7C%20Gitleaks-red)](../../.github/workflows/)
[![SBOM & SLSA](https://img.shields.io/badge/Supply--Chain-SBOM%20%7C%20SLSA-green)](../../.github/workflows/sbom.yml)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-lightgrey)](../../LICENSE)

</div>

---

```yaml
---
title: "Kansas Frontier Matrix — Dataset Documentation Template"
version: "v1.4.0"
last_updated: "2025-10-18"
owners: ["@kfm-data","@kfm-docs","@kfm-architecture","@kfm-security"]
tags: ["dataset","documentation","stac","fair","mcp","provenance","dcat","metadata","ci","ethics","security"]
status: "Template"
license: "CC-BY 4.0"
semantic_alignment:
  - MCP-DL v6.3
  - STAC 1.0
  - DCAT 2.0
  - JSON Schema
  - ISO 19115 / ISO 8601 / EPSG
  - GeoSPARQL
  - FAIR Principles
ci_required_checks:
  - stac-validate
  - checksums
  - docs-validate
  - policy-check
  - pre-commit
  - codeql
  - trivy
  - gitleaks
supply_chain:
  slsa_target: "Level 3"
  sbom_format: "SPDX 2.3 (JSON)"
---
```

---

## 🧭 Dataset Metadata (Front-Matter)

> _Fill this machine-readable block completely; CI will validate required keys._

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
doi: "<optional DOI or URL>"
created: YYYY-MM-DD
updated: YYYY-MM-DD
version: "vX.Y.Z"

domain: "<Terrain|Hydrology|Climate|Landcover|Hazards|Tabular|Text|Mixed>"
data_type: "<Raster|Vector|Tabular|Text|NetCDF|Mixed>"
license: "<CC-BY 4.0|Public Domain|MIT|Government Works|Custom>"
keywords: ["kansas","terrain","dem","example"]

spatial:
  crs: "EPSG:4326"
  bbox: [-102.05,36.99,-94.61,40.00]
temporal:
  start: "YYYY-MM-DD"
  end: "YYYY-MM-DD"

resolution_scale: "e.g., 1 m; 30 m; 1 km; 1:24,000"
coverage_statement: "<brief narrative of area/time coverage>"

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
  access_notes: "<rate limits, auth, throttling>"
  tiles:
    vector: "mbtiles or PBF endpoint (optional)"
    raster:  "COG URL(s) (optional)"

sensitivity: "none|restricted|contains_sensitive_data"
data_ethics: "open|restricted-derivatives|no-public-artifacts"
retention_policy: "retain_3_versions_archive_rest"

sbom:
  path: "artifacts/sbom/<dataset_id>.spdx.json"
slsa:
  attestation: "artifacts/provenance/<dataset_id>.intoto.jsonl"
# --- End metadata ---
```

---

## 🧩 Abstract / Description

> **Purpose:** What the dataset represents, intended use, and KFM relevance.  
> Include **provenance**, **applications**, **limitations**, and **audience**.

**Example**  
This dataset contains a 1 m DEM derived from LiDAR (2018–2020) for Kansas. It supports hydrologic modeling, hazard assessment, and ecological studies.

---

## 🌐 Data Provenance & Sources

| Source | Provider | Access Method | License | Link / API | Notes |
| :----- | :------: | :-----------: | :-----: | :--------: | :---- |
| USGS 3DEP DEM | USGS | REST/HTTPS | Public Domain | https://elevation.nationalmap.gov | Tiles 2018–2020 |
| KS DASC LiDAR | Kansas DASC | FTP/HTTPS | CC-BY 4.0 | https://www.kansasgis.org | County mosaics |

> All sources must have manifests in `data/sources/<domain>/` and be referenced in STAC `providers`.

---

## ⚙️ Processing Workflow (ETL → Products)

| Step | Description | Command / Script | Output |
| :--: | :---------- | :--------------- | :----- |
| 1 | Fetch raw data | `make fetch` | `data/raw/terrain/` |
| 2 | Reproject → EPSG:4326 | `gdalwarp -t_srs EPSG:4326 ...` | GeoTIFF |
| 3 | Mosaic tiles | `gdal_merge.py -o ks_dem.tif ...` | `ks_dem.tif` |
| 4 | Convert → COG | `rio cogeo create ks_dem.tif ks_dem_cog.tif` | `ks_dem_cog.tif` |
| 5 | Derivatives | `python src/pipelines/terrain/derive.py` | `hillshade.tif` / `slope.tif` |
| 6 | Create STAC | `python src/pipelines/load/stac_writer.py` | `data/stac/terrain/*.json` |

**Make targets**
```bash
make fetch && make process && make checksums && make stac-validate
```

---

## 🧮 Specifications & Schema

| Attribute | Description | Value |
| :-------- | :---------- | :---- |
| **Resolution** | Ground sample distance | 1 m |
| **CRS** | Coordinate Reference System | EPSG:4326 (WGS84) |
| **Extent (BBox)** | Spatial bounding box | [-102.05, 36.99, -94.61, 40.00] |
| **Coverage** | Temporal range | 2018-01-01 → 2020-12-31 |
| **Format** | Primary / Aux | GeoTIFF (COG), JSON (STAC) |
| **Size** | Approx total | 12 GB |
| **Encoding** | File encoding | UTF-8 / CSV / GeoTIFF |

**Data Dictionary (if applicable)**

| Field | Type | Units | Allowed Range | Description |
| :---- | :--- | :---- | :------------ | :---------- |
| `elevation` | float32 | meters | ≥ -500 | Elevation above MSL |
| `slope_deg` | float32 | degrees | 0–90 | Derived slope |

---

## 🧾 Outputs & Distribution

| Type | Path / URL | Description |
| :--- | :--------- | :---------- |
| Primary | `data/processed/terrain/ks_1m_dem_2018_2020.tif` | Core raster |
| COG | `data/processed/terrain/ks_1m_dem_2018_2020_cog.tif` | Web-optimized raster |
| Derivatives | `data/processed/terrain/hillshade.tif` | Visualization layer |
| STAC Item | `data/stac/terrain/ks_1m_dem_2018_2020.json` | Catalog entry |
| Checksums | `data/checksums/terrain/ks_1m_dem_2018_2020.manifest.json` | Integrity report |
| Thumbnail | `data/processed/metadata/thumbnails/ks_1m_dem_2018_2020.png` | Web preview |
| DCAT Export (opt) | `data/stac/terrain/ks_1m_dem_2018_2020_dcat.json` | DCAT/JSON-LD snapshot |

---

## ✅ Validation & QA

| Check | Tool / Method | Location | Result |
| :---- | :------------ | :------- | :----- |
| Checksum | `make checksums` | `data/checksums/` | ✅ |
| STAC Schema | `stac-validator` | `_reports/stac/` | ✅ |
| Spatial QA | `gdalinfo`, bounds check | `_reports/spatial/` | ✅ |
| Policy Gates | `.github/workflows/policy-check.yml` | GH Actions | ✅ |
| CI/CD | `.github/workflows/stac-validate.yml` | Actions Logs | ✅ |

> Logs archived under `data/work/logs/<domain>/<dataset_id>/`.

---

## 🔗 Relationships & Dependencies

| Relation | Target | Type | Path / Reference |
| :------: | :----: | :--: | :--------------- |
| Derived From | `usgs_3dep_dem` | Source | `data/sources/terrain/usgs_3dep_dem.json` |
| Feeds | `watersheds_huc12_2019` | Dependent | `data/processed/hydrology/watersheds_huc12_2019.geojson` |
| Referenced In | `ks_hillshade_2018_2020` | Derived | `data/processed/terrain/ks_hillshade_2018_2020.tif` |
| KG Link | `E73_Information_Object` | Graph Node | `graph://dataset/<dataset_id>` |

---

## 🔐 Ethics, Legal & Licensing

- Dataset license: **CC-BY 4.0** (or specify).  
- Attribution required for derivatives.  
- **PII assessment:** none / potential / present (mitigation).  
- **Cultural/Indigenous data:** set `data_ethics` and usage constraints in STAC; consult co-stewardship guidance.  
- Compliance with **USGS / DASC** distribution terms.  
- If licenses differ, document **compatibility matrix** and **exceptions**.

---

## 🧩 Integration with KFM Systems

| Component | Role | Integration Notes |
| :-------- | :--- | :----------------- |
| **Pipelines** | ETL & QA automation | `src/pipelines/<domain>/*` |
| **Metadata** | STAC integration | `data/stac/<domain>/*` |
| **CI/CD** | Validation, checksums, policy | `.github/workflows/stac-validate.yml` |
| **Web Viewer** | Map layer config | `web/config/layers.json` (legend, accessibility alt text) |
| **Knowledge Graph** | Provenance relations | `src/graph/graph_loader.py` |

---

## 🔎 FAIR & Standards Mapping

| FAIR Principle | Implementation |
| :------------- | :------------- |
| **Findable** | STAC entries indexed in catalog/search API |
| **Accessible** | Persistent HTTPS, Git-tracked metadata, API access |
| **Interoperable** | Open formats (COG/GeoJSON/CSV), EPSG codes, DCAT fields |
| **Reusable** | Licensing + citation guidance; full provenance |

**Optional DCAT/JSON-LD export** generated under `data/stac/<domain>/<dataset>_dcat.json`.

---

## 📌 Known Issues & Risks

- Tile seam artifacts (feathering recommended).  
- Sparse LiDAR coverage in `{counties}`.  
- Large files may impact low-bandwidth users; provide tiled views.

---

## 🧯 Rollback, Retention & Deprecation

| Policy | Description |
| :----- | :---------- |
| **Retention** | Maintain last 3 published versions; archive older. |
| **Rollback** | Revert to prior STAC Item + manifest and re-publish. |
| **Deprecation** | Flag with `deprecated: true` and cross-link replacement. |

---

## 📊 Example Queries (Optional)

```bash
# STAC search (by bbox/time)
curl -s "$API/stac/search" -H "Content-Type: application/json" -d '{
  "bbox":[-102.05,36.99,-94.61,40.00],
  "time":"2018-01-01/2020-12-31",
  "collections":["terrain"]
}'
```

---

## ✅ Acceptance Checklist

- [ ] STAC validation (schema + assets) ✅  
- [ ] Checksums verified for all outputs ✅  
- [ ] CRS, bbox, and spatial QA passed ✅  
- [ ] Docs updated + glossary cross-links ✅  
- [ ] CI/CD & policy gates green ✅  
- [ ] SBOM & SLSA artifacts attached (if applicable) ✅  

---

## 🧠 MCP Compliance Summary

| MCP Principle | Implementation |
| :------------ | :------------- |
| **Documentation-first** | Authored prior to publication; front-matter metadata complete. |
| **Reproducibility** | Deterministic pipelines with checksums and container digests. |
| **Open Standards** | STAC 1.0, GeoTIFF (COG), GeoJSON, JSON Schema, DCAT. |
| **Provenance** | Linked source manifests, checksum lineage, PROV-O/KG nodes. |
| **Auditability** | CI logs, QA reports, SBOM/SLSA, version history. |

---

## 📎 Related Documentation

| File | Description |
| :--- | :---------- |
| `docs/architecture/data-architecture.md` | Data model & lineage |
| `docs/templates/experiment.md` | Analytical experiment records |
| `docs/templates/sop.md` | Operational procedures |
| `docs/templates/provenance.md` | Provenance record template |
| `.github/workflows/stac-validate.yml` | CI validation workflow |

---

## 🗓️ Version History

| Version | Date | Author | Summary |
| :------ | :--- | :----- | :------ |
| **v1.4.0** | 2025-10-18 | KFM Docs Team | Added security/ethics fields, policy & supply-chain gates, KG link, example queries, acceptance checklist expanded |
| **v1.3.0** | 2025-10-17 | KFM Docs Team | Metadata YAML header, FAIR mapping, acceptance checklist, DCAT export |
| **v1.2.0** | 2025-10-10 | KFM Engineering | Improved schema table & integration sections |
| **v1.1.0** | 2025-10-05 | KFM Data Team | QA/Validation and lineage relationships |
| **v1.0.0** | 2025-10-04 | Documentation Team | Initial MCP-aligned dataset template |

---

<div align="center">

**Kansas Frontier Matrix © 2025**  
*"Every Dataset Accountable. Every Record Reproducible."*  
📍 `docs/templates/dataset.md` — MCP-compliant dataset documentation template for the Kansas Frontier Matrix.

</div>