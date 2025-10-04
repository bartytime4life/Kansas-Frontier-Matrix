<div align="center">

# 💧 Kansas-Frontier-Matrix — Processed Hydrology Checksums (`data/processed/hydrology/checksums/`)

**Mission:** Store and maintain **checksum files (`.sha256`)** that verify the integrity of all processed hydrology datasets —  
sink-filled DEMs, flow direction and accumulation grids, and water masks — ensuring accuracy, reproducibility,  
and data provenance throughout the Kansas Frontier Matrix hydrologic modeling system.

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../../../.github/workflows/site.yml)
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](../../../../.github/workflows/stac-validate.yml)
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](../../../../.github/workflows/codeql.yml)
[![Trivy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](../../../../.github/workflows/trivy.yml)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../../docs/)
[![License: Data](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../../../LICENSE)
[![License: Code](https://img.shields.io/badge/License-MIT-yellow)](../../../../LICENSE)

</div>

---

## 📚 Table of Contents
- [Overview](#overview)
- [Purpose](#purpose)
- [Directory Layout](#directory-layout)
- [Checksum Standards](#checksum-standards)
- [Verification Workflow](#verification-workflow)
- [Integration with MCP & STAC](#integration-with-mcp--stac)
- [Adding or Updating Checksums](#adding-or-updating-checksums)
- [References](#references)

---

## 🧠 Overview

This folder contains **SHA-256 checksum files** for all processed hydrology products stored in  
`data/processed/hydrology/`. Each checksum ensures the **data integrity** of hydrologic rasters  
and vector datasets that form the foundation of flow modeling and watershed delineation pipelines  
in the Kansas Frontier Matrix project.

Checksums are essential for maintaining a **verifiable lineage** between raw source DEMs,  
processed hydrologic layers, and their corresponding metadata and STAC catalog entries.

---

## 🎯 Purpose

- **Integrity Verification:** Ensure hydrology datasets are not corrupted or modified after generation.  
- **Reproducibility:** Confirm datasets can be regenerated to match their original cryptographic signature.  
- **Provenance Tracking:** Link every dataset to its corresponding `mcp_provenance` record in metadata.  
- **Automation:** Support automated checksum verification in CI/CD workflows and `make validate-hydro`.  

---

## 🧱 Directory Layout

```bash
data/
└── processed/
    └── hydrology/
        └── checksums/
            ├── dem_filled_1m_ks.tif.sha256
            ├── flow_dir_d8_1m_ks.tif.sha256
            ├── flow_accum_base_1m_ks.tif.sha256
            ├── watermask_ks.tif.sha256
            ├── stream_seed_points.geojson.sha256
            └── README.md
````

Each `.sha256` file corresponds to one dataset in the parent directory and contains a
cryptographic hash in GNU Coreutils format:

```text
2ef54c72b13c6a4e9c1acdb3b3e2dfae4d6cfbe85c51b38e9d1e278c66a4ff4a  flow_dir_d8_1m_ks.tif
```

---

## 🧩 Checksum Standards

| Standard    | Algorithm                   | Output                         | Description                                  |
| ----------- | --------------------------- | ------------------------------ | -------------------------------------------- |
| **SHA-256** | 256-bit secure hash         | 64-character hex               | Cryptographic fingerprint for file integrity |
| **Format**  | GNU Coreutils (`sha256sum`) | `<hash>  <filename>`           | Machine- and human-readable format           |
| **Mode**    | Binary (`--binary`)         | Prevents newline discrepancies | Platform-independent reproducibility         |

Each checksum acts as a **digital fingerprint**, uniquely identifying each processed file version.

---

## 🔍 Verification Workflow

To verify hydrology datasets locally:

```bash
# Verify a single dataset
sha256sum -c data/processed/hydrology/checksums/flow_dir_d8_1m_ks.tif.sha256

# Verify all hydrology checksums
find data/processed/hydrology/checksums -name "*.sha256" -exec sha256sum -c {} \;
```

**Expected output:**

```
flow_dir_d8_1m_ks.tif: OK
watermask_ks.tif: OK
```

If discrepancies exist:

```
dem_filled_1m_ks.tif: FAILED
sha256sum: WARNING: 1 computed checksum did NOT match
```

### CI/CD Integration

Checksum verification is built into the repository’s automated testing pipeline via
`.github/workflows/stac-validate.yml`, which ensures every commit maintains verified integrity.

---

## 🌐 Integration with MCP & STAC

Checksums provide the **link between file integrity and semantic metadata** layers.

1. **MCP Provenance**
   Each metadata record includes a corresponding checksum reference:

   ```json
   "mcp_provenance": "sha256:2ef54c72b13c6a4e9c1acdb3b3e2dfae4d6cfbe85c51b38e9d1e278c66a4ff4a"
   ```

   This connects physical data files to their documented lineage.

2. **STAC Catalog Integration**
   Each hydrology STAC item (`data/stac/items/hydro_*`) embeds the same checksum hash
   for cross-layer verification and discoverability.

This integration ensures every hydrologic product remains scientifically verifiable and machine-traceable.

---

## ⚙️ Adding or Updating Checksums

1. Generate new checksum:

   ```bash
   sha256sum <dataset> > data/processed/hydrology/checksums/<dataset>.sha256
   ```
2. Verify file integrity:

   ```bash
   sha256sum -c data/processed/hydrology/checksums/<dataset>.sha256
   ```
3. Update metadata (`data/processed/hydrology/metadata/<dataset>.json`)
   with the new `mcp_provenance` value.
4. Run validation:

   ```bash
   make validate-hydro
   ```
5. Commit both the dataset and checksum file together, then open a Pull Request.

Automated CI/CD will verify integrity before merging.

---

## 📖 References

* **WhiteboxTools Hydrology Suite:** [https://www.whiteboxgeo.com/manual/wbt_book/hydro.html](https://www.whiteboxgeo.com/manual/wbt_book/hydro.html)
* **GDAL DEM Processing Utilities:** [https://gdal.org/programs/gdaldem.html](https://gdal.org/programs/gdaldem.html)
* **USGS National Hydrography Dataset (NHD):** [https://www.usgs.gov/national-hydrography](https://www.usgs.gov/national-hydrography)
* **Kansas DASC GIS Hub:** [https://hub.kansasgis.org](https://hub.kansasgis.org)
* **STAC Specification 1.0:** [https://stacspec.org](https://stacspec.org)
* **Master Coder Protocol (MCP):** [`docs/standards/`](../../../../docs/standards/)

---

<div align="center">

*“Every flowline and basin boundary is secured — these checksums protect the hydrologic truth of Kansas’s terrain.”*

</div>
```

