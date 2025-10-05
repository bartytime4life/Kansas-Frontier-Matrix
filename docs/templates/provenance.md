<div align="center">

# 🔗 Kansas Frontier Matrix — **Provenance Record Template**

`docs/templates/provenance.md`

**Purpose:** A **structured, MCP- and FAIR-aligned** template to capture the **lineage and transformation history** of datasets, models, and derived products in the **Kansas Frontier Matrix (KFM)** — ensuring **traceability**, **accountability**, and **reproducibility** across the full data lifecycle.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../docs/)
[![FAIR](https://img.shields.io/badge/FAIR-Findable·Accessible·Interoperable·Reusable-2ea44f)](https://www.go-fair.org/fair-principles/)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../LICENSE)
[![STAC](https://img.shields.io/badge/Metadata-STAC%201.0.0-blue)](https://stacspec.org/)
[![PROV-O](https://img.shields.io/badge/Ontology-W3C%20PROV--O-8a2be2)](https://www.w3.org/TR/prov-o/)

</div>

---

## 🧭 Provenance Record Metadata

| Field                      | Description                                                                 |
| :------------------------- | :-------------------------------------------------------------------------- |
| **Provenance ID**          | Unique identifier (e.g., `PROV-2025-001-TERRAIN`)                           |
| **Entity Type**            | Dataset / Model / Experiment / Document                                     |
| **Associated ID(s)**       | Link to dataset/model/experiment IDs (e.g., `DATASET-2025-001-TERRAIN-DEM`) |
| **Author(s)**              | Responsible curator / pipeline engineer                                     |
| **Affiliation**            | Team or organization                                                        |
| **Date Created / Updated** | YYYY-MM-DD / YYYY-MM-DD                                                     |
| **Version**                | v1.0, v1.1, etc.                                                            |
| **Domain**                 | Terrain / Hydrology / Climate / Landcover / Hazards / Tabular / Text        |
| **Status**                 | Active / Archived / Superseded / Deprecated                                 |
| **PID / DOI (optional)**   | Persistent identifier if minted (e.g., Zenodo DOI)                          |
| **License**                | CC-BY 4.0 / Public Domain / MIT (as applicable)                             |
| **Sensitivity**            | Public / Restricted / Contains redactions                                   |

> **PROV-O mapping:** *prov:Entity* (this record) attributed to *prov:Agent* (author) via *prov:wasAttributedTo*; creation via *prov:generatedAtTime*.

---

## 📜 Provenance Overview

Provide a concise narrative of origins and transformations leading to current state.

> **Example:**
> Processed Kansas LiDAR-derived 1 m DEM (2018–2020) from USGS 3DEP + KS DASC sources. Steps: acquisition → QA → reprojection → mosaicking → void-fill → hillshade derivation → STAC/checksum → publication to `data/processed/terrain/`. Reproducible via `make terrain`.

---

## 🧩 Lineage Chain (Stepwise)

| Step | Type      | Description                    | Input(s)          | Output(s)                                        | Tool / Script                    | PROV-O                     |
| :--: | :-------- | :----------------------------- | :---------------- | :----------------------------------------------- | :------------------------------- | :------------------------- |
|   1  | Source    | Raw tile acquisition           | `usgs_3dep_dem`   | `data/raw/terrain/ks_3dep_tiles.zip`             | `make fetch-raw`                 | *prov:wasDerivedFrom*      |
|   2  | Transform | Reproject & mosaic (EPSG:4326) | Raw tiles         | `data/processed/terrain/ks_1m_dem_2018_2020.tif` | `terrain_pipeline.py`            | *prov:wasGeneratedBy*      |
|   3  | Derive    | Hillshade / slope / aspect     | DEM GeoTIFF       | `ks_hillshade_2018_2020.tif`                     | `gdal_dem` / `gdaldem hillshade` | *prov:wasGeneratedBy*      |
|   4  | Validate  | CRS, extent, nodata QA         | Processed rasters | QA report                                        | `gdalinfo`, custom checks        | *prov:used*                |
|   5  | Verify    | SHA-256 checksums              | Outputs           | `.sha256` files                                  | `make checksums`                 | *prov:wasInfluencedBy*     |
|   6  | Describe  | STAC item(s)                   | Outputs           | `data/stac/terrain/*.json`                       | `stac-generator.py`              | *prov:qualifiedGeneration* |

<details>
<summary><b>📦 Extended lineage attributes (click to expand)</b></summary>

* **Temporal extent:** 2018-01-01 → 2020-12-31
* **Spatial extent (WGS84 bbox):** `[-102.05, 36.99, -94.59, 40.00]`
* **Nodata policy:** `-9999` propagated; masked in derivatives
* **Resampling:** bilinear (mosaic); cubic (hillshade)
* **Tiling:** internal overviews built at {2,4,8,16}
* **Compression:** COG / DEFLATE / overviews: JPEG

</details>

---

## 🧾 Source Provenance

| Source            | Provider               | Access Method | License       | Source Manifest                           |
| :---------------- | :--------------------- | :------------ | :------------ | :---------------------------------------- |
| **USGS 3DEP DEM** | U.S. Geological Survey | REST / HTTPS  | Public Domain | `data/sources/terrain/usgs_3dep_dem.json` |
| **KS DASC LiDAR** | Kansas DASC            | FTP / HTTPS   | CC-BY 4.0     | `data/sources/terrain/ks_dasc_lidar.json` |

> Each **source file** must exist in the **Source Registry** and include retrieval time, original filename, size, and original checksum (if provided).

---

## 🧮 Derived Products

| Product                          | Type     | Description                    | File Path                 |
| :------------------------------- | :------- | :----------------------------- | :------------------------ |
| `ks_1m_dem_2018_2020.tif`        | Raster   | Reprojected statewide DEM      | `data/processed/terrain/` |
| `ks_hillshade_2018_2020.tif`     | Raster   | Hillshade visualization layer  | `data/processed/terrain/` |
| `ks_1m_dem_2018_2020.json`       | Metadata | STAC item (assets, bbox, time) | `data/stac/terrain/`      |
| `ks_1m_dem_2018_2020.tif.sha256` | Checksum | SHA-256 integrity              | `data/checksums/terrain/` |

---

## 🧪 Validation & Verification

| Validation          | Description                  | Tool / Workflow                       | Result     |
| :------------------ | :--------------------------- | :------------------------------------ | :--------- |
| **Checksum**        | File integrity (SHA-256)     | `make checksums`                      | ✅ Passed   |
| **STAC Validation** | Item/collection schema       | `.github/workflows/stac-validate.yml` | ✅ Passed   |
| **Spatial QA/QC**   | CRS, bbox, nodata            | `gdalinfo`, `rio info`                | ✅ Passed   |
| **COG Compliance**  | Internal tiling & overviews  | `cog_validate`                        | ✅ Passed   |
| **CI/CD Audit**     | Build & artifact consistency | `site.yml`, `checksums.yml`           | ✅ Passed   |
| **Manual Review**   | Curator sign-off             | Governance log / PR                   | ✅ Approved |

> Store logs under: `data/work/logs/provenance/<provenance_id>.log`

---

## 🗂️ Environment & Supply Chain Capture

| Aspect                | Capture                                                                |
| :-------------------- | :--------------------------------------------------------------------- |
| **Container**         | Image + digest (e.g., `ghcr.io/org/kfm:terrain-1.0 @ sha256:<digest>`) |
| **Env Lockfile**      | `environment.yml` / `requirements.txt` / `poetry.lock`                 |
| **SBOM**              | `sbom-<provenance_id>.spdx.json` (SPDX)                                |
| **SLSA Level (opt.)** | Build provenance attestation (if configured)                           |

> **Repro tip:** include `conda env export --from-history` or `pip freeze` snapshots in artifacts.

---

## 🔐 Access, Retention & Governance

| Policy                  | Setting                                                                  |
| :---------------------- | :----------------------------------------------------------------------- |
| **Access Level**        | Public (read) / Restricted (explain constraints)                         |
| **Embargo / Redaction** | If redacted, document fields & rationale                                 |
| **Retention**           | Minimum N years; archival target (e.g., S3 Glacier / institutional repo) |
| **Steward**             | Role/team responsible for ongoing maintenance                            |

---

## 🧠 Change History

| Version | Date       | Author                   | Summary                                           |
| :-----: | :--------- | :----------------------- | :------------------------------------------------ |
|   v1.0  | 2025-10-04 | KFM Data Governance Team | Initial provenance template                       |
|   v1.1  | 2025-10-05 | (You)                    | Clarified QA steps; added SBOM/SLSA & env capture |

---

## 🧩 PROV Graph (Optional)

```mermaid
graph LR
  A["Raw Tiles<br/>(USGS/DASC)"] -->|prov:wasDerivedFrom| B["Reproject & Mosaic<br/>(terrain_pipeline.py)"]
  B -->|prov:wasGeneratedBy| C["DEM (COG)"]
  C -->|prov:wasGeneratedBy| D["Derived Layers<br/>(hillshade, slope, aspect)"]
  C -->|prov:qualifiedDerivation| E["STAC + Checksums"]
```

---

## 👥 Responsible Parties

| Role                    | Name / Team | Responsibility          |
| :---------------------- | :---------- | :---------------------- |
| **Data Engineer**       | …           | Ingestion & transforms  |
| **Metadata Curator**    | …           | STAC/PROV documentation |
| **Quality Assurance**   | …           | QA/QC & CI validations  |
| **Reviewer / Approver** | …           | Final sign-off          |

---

## 🧰 Reproducibility Quickstart

```bash
# 1) Fetch sources and verify
make fetch-raw && make checksums

# 2) Build terrain artifacts
make terrain

# 3) Validate outputs & metadata
make stac-validate && make qa-terrain

# 4) Publish artifacts (internal)
make publish-terrain
```

> **Containerized run:** `docker run --rm -v $PWD:/work -w /work ghcr.io/org/kfm:terrain-1.0 make terrain`

---

## 🧠 MCP Compliance Summary

| MCP Principle           | Implementation                                     |
| :---------------------- | :------------------------------------------------- |
| **Documentation-first** | Provenance authored & versioned with data/pipeline |
| **Reproducibility**     | Deterministic steps + env & container capture      |
| **Open Standards**      | STAC 1.0.0, PROV-O, COG, GeoJSON, SPDX             |
| **Provenance**          | Full lineage chain from sources to products        |
| **Auditability**        | CI logs, checksums, SBOM, build attestations       |

---

## 📎 Related Documentation

| File                                     | Description                           |
| :--------------------------------------- | :------------------------------------ |
| `docs/templates/dataset.md`              | Dataset documentation (public-facing) |
| `docs/templates/experiment.md`           | Experiment protocol & metrics         |
| `docs/templates/model_card.md`           | Model transparency & evaluation       |
| `docs/architecture/data-architecture.md` | Repository data layout & flows        |
| `.github/workflows/stac-validate.yml`    | Automated STAC checks                 |

---

## 📚 References

1. **W3C PROV-O Ontology** — [https://www.w3.org/TR/prov-o/](https://www.w3.org/TR/prov-o/)
2. **STAC Specification v1.0.0** — [https://stacspec.org](https://stacspec.org)
3. **MCP Guidelines** — KFM Documentation Framework
4. **FAIR Principles** — Wilkinson et al., 2016
5. **SPDX** — [https://spdx.dev](https://spdx.dev) (Software Bill of Materials)

---

## 📅 Version History

| Version | Date       | Author                 | Summary                                        |
| :-----: | :--------- | :--------------------- | :--------------------------------------------- |
|   v1.0  | 2025-10-04 | KFM Documentation Team | Initial provenance record template             |
|   v1.1  | 2025-10-05 | KFM Engineering        | Expanded PROV-O mapping + supply-chain section |

---

<div align="center">

**Kansas Frontier Matrix** — *“Every Dataset Has a Story. Every Step Leaves a Trace.”*
📍 [`docs/templates/provenance.md`](.) · MCP-compliant provenance template for KFM.

</div>
