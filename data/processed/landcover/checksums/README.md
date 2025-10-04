<div align="center">

# 🌾 Kansas-Frontier-Matrix — Processed Landcover Checksums (`data/processed/landcover/checksums/`)

**Mission:** Store and manage **checksum files (`.sha256`)** that verify the integrity of all processed landcover datasets —  
NLCD rasters, vegetation masks, spectral composites, and water indices — ensuring reproducibility, authenticity,  
and long-term data fidelity within the Kansas Frontier Matrix ecosystem.

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

## 🌍 Overview

This directory holds **SHA-256 checksum files** corresponding to all processed landcover products  
in `data/processed/landcover/`.  

Checksums guarantee that every raster and vector file — from NLCD classifications to vegetation and  
water masks — remains unchanged and verifiable, supporting transparent data lineage and open-science reproducibility.

All `.sha256` files link directly to the **MCP provenance chain** and **STAC catalog metadata**,  
ensuring end-to-end file integrity across the Kansas Frontier Matrix data system.

---

## 🎯 Purpose

- **Integrity:** Verify that landcover datasets (GeoTIFFs/GeoJSONs) remain unchanged post-processing.  
- **Reproducibility:** Ensure that derivative landcover analyses (NDVI, classification change maps)  
  are verifiable using hash-based validation.  
- **Automation:** Provide hash validation for CI/CD workflows (`make validate-landcover`).  
- **Traceability:** Link data files to their `mcp_provenance` values in metadata and STAC records.  

---

## 🧱 Directory Layout

```bash
data/
└── processed/
    └── landcover/
        └── checksums/
            ├── nlcd_2021_ks.tif.sha256
            ├── vegetation_mask_ks.tif.sha256
            ├── water_mask_ks.tif.sha256
            ├── landsat_2021_ks.tif.sha256
            ├── sentinel_2021_ks.tif.sha256
            └── README.md
````

Each checksum file corresponds 1:1 to a processed dataset in the parent directory.
Checksum files contain 64-character hexadecimal hashes in GNU Coreutils format:

```text
d3f74e5c8b3e921f1e834d4b39d723d43a71d02fcecb69ab23b2df7b7cc10ad9  nlcd_2021_ks.tif
```

---

## 🧩 Checksum Standards

| Parameter     | Description                                                       |
| ------------- | ----------------------------------------------------------------- |
| **Algorithm** | SHA-256 (Secure Hash Algorithm, 256-bit)                          |
| **Output**    | 64-character hexadecimal hash                                     |
| **Format**    | `<hash>  <filename>` (GNU `sha256sum` format)                     |
| **Encoding**  | Binary (`--binary`) for platform consistency                      |
| **Purpose**   | Immutable fingerprint linking data, metadata, and catalog entries |

These hashes are recognized as **canonical identifiers** in the MCP system and used for
provenance verification during ETL rebuilds or archival audits.

---

## 🔍 Verification Workflow

### Manual Verification

To confirm dataset integrity locally:

```bash
# Verify one landcover dataset
sha256sum -c data/processed/landcover/checksums/nlcd_2021_ks.tif.sha256

# Verify all checksums in this directory
find data/processed/landcover/checksums -name "*.sha256" -exec sha256sum -c {} \;
```

**Expected Output:**

```
nlcd_2021_ks.tif: OK
vegetation_mask_ks.tif: OK
water_mask_ks.tif: OK
```

If mismatched:

```
sentinel_2021_ks.tif: FAILED
sha256sum: WARNING: 1 computed checksum did NOT match
```

### CI/CD Integration

GitHub Actions automatically verifies all checksums via `.github/workflows/stac-validate.yml`
on every push and Pull Request, ensuring data integrity at every stage of the pipeline.

---

## 🌐 Integration with MCP & STAC

Checksums bridge the **data layer** and **metadata layer** within the Kansas Frontier Matrix.

1. **MCP Provenance Links**

   * Each metadata JSON includes an `"mcp_provenance"` field:

     ```json
     "mcp_provenance": "sha256:d3f74e5c8b3e921f1e834d4b39d723d43a71d02fcecb69ab23b2df7b7cc10ad9"
     ```
   * Ensures immutable linkage between datasets and metadata.

2. **STAC Catalog Synchronization**

   * STAC items in `data/stac/items/landcover_*` reference the same hash for
     cross-verification across the system.

This cross-linkage guarantees consistent integrity validation across both semantic and file-based records.

---

## ⚙️ Adding or Updating Checksums

1. Generate a checksum for a dataset:

   ```bash
   sha256sum <dataset> > data/processed/landcover/checksums/<dataset>.sha256
   ```
2. Validate:

   ```bash
   sha256sum -c data/processed/landcover/checksums/<dataset>.sha256
   ```
3. Add the checksum reference to the dataset’s metadata JSON under `mcp_provenance`.
4. Run:

   ```bash
   make validate-landcover
   ```
5. Commit both the dataset and `.sha256` file together.
6. Push and open a Pull Request — CI/CD will re-run full validation.

---

## 📖 References

* **USGS National Land Cover Database (NLCD):** [https://www.mrlc.gov/data](https://www.mrlc.gov/data)
* **Landsat Science:** [https://landsat.gsfc.nasa.gov](https://landsat.gsfc.nasa.gov)
* **Sentinel-2 (ESA) Documentation:** [https://scihub.copernicus.eu/](https://scihub.copernicus.eu/)
* **GDAL Utilities:** [https://gdal.org/](https://gdal.org/)
* **STAC Specification 1.0:** [https://stacspec.org](https://stacspec.org)
* **GNU Coreutils (sha256sum):** [https://www.gnu.org/software/coreutils/manual/html_node/sha2-utilities.html](https://www.gnu.org/software/coreutils/manual/html_node/sha2-utilities.html)
* **Master Coder Protocol (MCP):** [`docs/standards/`](../../../../docs/standards/)

---

<div align="center">

*“From fields of grass to pixels of code — these checksums keep Kansas’s living landcover immutable and verified.”*

</div>
```

