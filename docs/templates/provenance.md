<div align="center">

# 🔗 Kansas Frontier Matrix — Provenance Record Template  
`docs/templates/provenance.md`

**Purpose:** Provide a structured and reproducible template for documenting the **lineage and transformation history**  
of datasets, models, and derived products in the **Kansas Frontier Matrix (KFM)** — ensuring provenance, traceability,  
and accountability throughout all stages of data and workflow lifecycle.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../docs/)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../LICENSE)

</div>

---

## 🧭 Provenance Record Metadata

| Field | Description |
|:------|:-------------|
| **Provenance ID** | Unique identifier (e.g., `PROV-2025-001-TERRAIN`) |
| **Entity Type** | Dataset / Model / Experiment / Document |
| **Associated ID(s)** | Link to corresponding dataset, model, or experiment (`DATASET-2025-001-TERRAIN-DEM`) |
| **Author(s)** | Responsible curator or pipeline engineer |
| **Date Created** | YYYY-MM-DD |
| **Last Updated** | YYYY-MM-DD |
| **Version** | v1.0, v1.1, etc. |
| **Domain** | Terrain / Hydrology / Climate / Landcover / Hazards / Tabular / Text |
| **Status** | Active / Archived / Superseded |
| **License** | CC-BY 4.0 / Public Domain / MIT (as applicable) |

---

## 📜 Provenance Overview

Provide a short description summarizing the origin, lineage, and transformations leading to the current state  
of the dataset, model, or experiment.

> Example:  
> *This provenance record traces the lineage of the Kansas LiDAR-derived 1m DEM, processed from USGS 3DEP and KS DASC LiDAR data (2018–2020).  
> The dataset was reprojected, mosaicked, validated, and integrated into the terrain analysis pipeline under MCP reproducibility standards.*

---

## 🧩 Lineage Chain

Document the stepwise chain of data sources, transformations, and derived products.

| Step | Type | Description | Input(s) | Output(s) | Tool / Script |
|:------|:------|:-------------|:-------------|:-------------|:-------------|
| 1 | Source | Raw input acquisition | `usgs_3dep_dem` | `data/raw/terrain/ks_3dep_tiles.zip` | `make fetch-raw` |
| 2 | Transform | Reprojection & cleaning | `data/raw/terrain/ks_3dep_tiles.zip` | `data/processed/terrain/ks_1m_dem_2018_2020.tif` | `terrain_pipeline.py` |
| 3 | Derive | Hillshade & slope calculation | `data/processed/terrain/ks_1m_dem_2018_2020.tif` | `data/processed/terrain/ks_hillshade_2018_2020.tif` | `GDAL hillshade` |
| 4 | Validate | Schema and checksum verification | Processed rasters | `data/checksums/terrain/*.sha256` | `make checksums` |
| 5 | Document | Metadata creation | Processed files | `data/stac/terrain/*.json` | `stac-generator.py` |

---

## 🧾 Source Provenance

List all original data sources and manifests that initiated this lineage.

| Source | Provider | Access Method | License | Source Manifest Path |
|:-----------|:-----------|:----------------|:-----------|:-----------|
| **USGS 3DEP DEM** | U.S. Geological Survey | REST API | Public Domain | `data/sources/terrain/usgs_3dep_dem.json` |
| **KS DASC LiDAR** | Kansas Data Access & Support Center | FTP | CC-BY 4.0 | `data/sources/terrain/ks_dasc_lidar.json` |

> Each source file must have a corresponding entry in the **Source Registry** (`data/sources/<domain>/`).

---

## 🧮 Derived Products

Document the outputs generated through transformation or analysis steps.

| Product | Type | Description | File Path |
|:-----------|:-----------|:-------------|:-----------|
| `ks_1m_dem_2018_2020.tif` | Raster | Processed LiDAR-based DEM | `data/processed/terrain/` |
| `ks_hillshade_2018_2020.tif` | Raster | Hillshade visualization layer | `data/processed/terrain/` |
| `ks_1m_dem_2018_2020.json` | Metadata | STAC-compliant record | `data/stac/terrain/` |
| `ks_1m_dem_2018_2020.tif.sha256` | Checksum | Integrity verification | `data/checksums/terrain/` |

---

## 🧪 Validation & Verification

Detail the validation methods and evidence confirming data integrity and reproducibility.

| Validation Type | Description | Tool / Workflow | Result |
|:------------------|:-------------|:------------------|:----------|
| **Checksum Validation** | Confirms data integrity | `make checksums` | ✅ Passed |
| **STAC Validation** | Ensures metadata compliance | `.github/workflows/stac-validate.yml` | ✅ Passed |
| **Spatial QA/QC** | Validates projection, extent, and CRS | `gdalinfo` | ✅ Passed |
| **Automated CI/CD Audit** | Ensures build consistency and completeness | `site.yml`, `checksums.yml` | ✅ Passed |
| **Manual Review** | Peer validation by maintainers | Governance log | ✅ Approved |

---

## 🧩 Provenance Graph (Optional)

Visual representation of relationships between data, tools, and outputs.

```mermaid
graph LR
  A["Raw LiDAR Tiles\n(usgs_3dep_dem)"] --> B["Reproject & Merge\n(terrain_pipeline.py)"]
  B --> C["DEM Output\n(ks_1m_dem_2018_2020.tif)"]
  C --> D["Derived Layers\n(hillshade, slope, aspect)"]
  D --> E["STAC Metadata + Checksums"]
````

<!-- END OF MERMAID -->

---

## 🔍 Responsible Parties

| Role                    | Name / Team | Responsibility                      |
| :---------------------- | :---------- | :---------------------------------- |
| **Data Engineer**       | (Name)      | Data ingestion and processing       |
| **Metadata Curator**    | (Name)      | STAC and provenance documentation   |
| **Quality Assurance**   | (Name)      | Validation and CI/CD verification   |
| **Reviewer / Approver** | (Name)      | Final sign-off on provenance record |

---

## 🧠 Change History

Record updates and modifications to this lineage record.

| Version | Date       | Author                   | Change Summary                      |
| :------ | :--------- | :----------------------- | :---------------------------------- |
| v1.0    | 2025-10-04 | KFM Data Governance Team | Initial provenance record template. |
| v1.1    | TBD        |                          |                                     |

---

## 🧠 MCP Compliance Summary

| MCP Principle           | Implementation                                            |
| :---------------------- | :-------------------------------------------------------- |
| **Documentation-first** | Provenance recorded before dataset publication.           |
| **Reproducibility**     | Workflow steps deterministic and logged.                  |
| **Open Standards**      | Metadata follows STAC 1.0.0 and PROV-O ontologies.        |
| **Provenance**          | Full lineage captured from raw data to processed outputs. |
| **Auditability**        | CI/CD workflows validate provenance files and references. |

---

## 📎 Related Documentation

| File                                     | Description                                 |
| :--------------------------------------- | :------------------------------------------ |
| `docs/templates/dataset.md`              | Template for dataset documentation.         |
| `docs/architecture/data-architecture.md` | Data lineage and flow description.          |
| `docs/architecture/knowledge-graph.md`   | RDF/semantic provenance integration.        |
| `data/ARCHITECTURE.md`                   | Directory and metadata hierarchy reference. |
| `.github/workflows/stac-validate.yml`    | Automated STAC provenance validation.       |

---

## 🧾 References

1. **W3C PROV-O Ontology** — [https://www.w3.org/TR/prov-o/](https://www.w3.org/TR/prov-o/)
2. **STAC Specification v1.0.0** — [https://stacspec.org](https://stacspec.org)
3. **Master Coder Protocol (MCP)** — Kansas Frontier Matrix Documentation Framework
4. **FAIR Principles** — Wilkinson et al., 2016 (Findable, Accessible, Interoperable, Reusable)

---

## 📅 Version History

| Version | Date       | Author                 | Summary                                                     |
| :------ | :--------- | :--------------------- | :---------------------------------------------------------- |
| v1.0    | 2025-10-04 | KFM Documentation Team | Initial provenance record template for datasets and models. |

---

<div align="center">

**Kansas Frontier Matrix** — *“Every Dataset Has a Story. Every Step Leaves a Trace.”*
📍 [`docs/templates/provenance.md`](.) · Template for recording data lineage and provenance in MCP-compliant workflows.

</div>
