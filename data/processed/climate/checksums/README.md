<div align="center">

# 🌦️ Kansas-Frontier-Matrix — Processed Climate Checksums (`data/processed/climate/checksums/`)

**Mission:** Maintain **checksum files (`.sha256`)** verifying the integrity of all processed climate datasets —  
gridded temperature, precipitation, and drought indices — ensuring long-term reproducibility, authenticity,  
and provenance for Kansas Frontier Matrix climate archives.

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

This directory contains **SHA-256 checksum files** used to verify the integrity and authenticity  
of all processed climate data products stored in `data/processed/climate/`.  

Checksums ensure that each temperature, precipitation, or drought raster remains unchanged since  
its creation, supporting **data reproducibility, scientific transparency, and long-term validation**  
as required by the **Master Coder Protocol (MCP)**.

Each checksum file corresponds directly to a processed climate asset and its metadata entry in  
`data/processed/climate/metadata/`.

---

## 🎯 Purpose

- **Integrity Verification:** Detect accidental or unauthorized data modification.  
- **Reproducibility Assurance:** Confirm that scientific analyses reproduce exact results.  
- **Provenance Linking:** Tie file hashes to their `mcp_provenance` entries in metadata and STAC catalogs.  
- **Automation:** Allow continuous integration (CI/CD) to perform automated hash checks during build and release.  

---

## 🧱 Directory Layout

```bash
data/
└── processed/
    └── climate/
        └── checksums/
            ├── temp_mean_annual_1895_2024.tif.sha256
            ├── precip_total_annual_1895_2024.tif.sha256
            ├── drought_spi12_1895_2024.tif.sha256
            ├── climate_normals_1991_2020.parquet.sha256
            └── README.md
````

Each `.sha256` file contains a single SHA-256 hash line referencing its corresponding dataset,
following the GNU Coreutils format.

Example:

```text
9c1a24e3374e6dbfcd3ef11a8a9a5568c4f5f7f2b6c77714569e34138ab7f91b  temp_mean_annual_1895_2024.tif
```

---

## 🧩 Checksum Standards

| Standard    | Algorithm           | Output                             | Description                                 |
| ----------- | ------------------- | ---------------------------------- | ------------------------------------------- |
| **SHA-256** | 256-bit hash        | 64-character hexadecimal string    | Cryptographic fingerprint for file identity |
| **Format**  | GNU `sha256sum`     | `<hash>  <filename>`               | Human- and machine-readable                 |
| **Mode**    | Binary (`--binary`) | Ensures cross-platform consistency | Avoids newline discrepancies                |

All hashes can be verified using Linux, macOS, or Windows CLI tools.

---

## 🔍 Verification Workflow

To confirm dataset integrity locally or in CI environments:

```bash
# Verify a single file
sha256sum -c data/processed/climate/checksums/temp_mean_annual_1895_2024.tif.sha256

# Verify all climate data checksums
find data/processed/climate/checksums -name "*.sha256" -exec sha256sum -c {} \;
```

**Expected output:**

```
temp_mean_annual_1895_2024.tif: OK
precip_total_annual_1895_2024.tif: OK
```

If an error occurs:

```
drought_spi12_1895_2024.tif: FAILED
sha256sum: WARNING: 1 computed checksum did NOT match
```

---

## 🌐 Integration with MCP & STAC

Each checksum is tied directly to the project’s metadata and catalog layers:

1. **MCP Provenance**

   * Every metadata JSON includes an `"mcp_provenance"` field:

     ```json
     "mcp_provenance": "sha256:9c1a24e3374e6dbfcd3ef11a8a9a5568c4f5f7f2b6c77714569e34138ab7f91b"
     ```
   * This connects the dataset’s content to its unique cryptographic signature.

2. **STAC Catalog**

   * STAC items in `data/stac/items/climate_*` include the same SHA-256 hash,
     enabling cross-layer verification and catalog integrity tracking.

---

## ⚙️ Adding or Updating Checksums

1. Generate checksum for a new or modified dataset:

   ```bash
   sha256sum <dataset> > data/processed/climate/checksums/<dataset>.sha256
   ```
2. Validate locally:

   ```bash
   sha256sum -c data/processed/climate/checksums/<dataset>.sha256
   ```
3. Update the corresponding `mcp_provenance` field in the dataset’s metadata JSON.
4. Commit both the dataset and checksum file together.
5. Push and open a Pull Request — GitHub Actions will automatically run validation.

---

## 📖 References

* **GNU Coreutils SHA Utilities:** [https://www.gnu.org/software/coreutils/manual/html_node/sha2-utilities.html](https://www.gnu.org/software/coreutils/manual/html_node/sha2-utilities.html)
* **STAC Specification 1.0:** [https://stacspec.org](https://stacspec.org)
* **JSON Schema Validation:** [https://json-schema.org](https://json-schema.org)
* **Master Coder Protocol (MCP):** [`docs/standards/`](../../../../docs/standards/)
* **NOAA NCEI Climate Data:** [https://www.ncei.noaa.gov/](https://www.ncei.noaa.gov/)
* **PRISM Climate Group:** [https://prism.oregonstate.edu/](https://prism.oregonstate.edu/)

---

<div align="center">

*“Every climate grid, every anomaly — these checksums preserve the integrity of Kansas’s atmospheric memory.”*

</div>
```

