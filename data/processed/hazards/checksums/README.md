<div align="center">

# ⚠️ Kansas-Frontier-Matrix — Processed Hazards Checksums (`data/processed/hazards/checksums/`)

**Mission:** Maintain **checksum files (`.sha256`)** verifying the integrity of all processed hazard datasets —  
drought indices, tornado tracks, flood polygons, wildfire detections, and FEMA disaster summaries —  
ensuring scientific reproducibility, authenticity, and transparent provenance for Kansas hazard data.

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

## 🌪️ Overview

This directory stores **SHA-256 checksum files** for all processed hazard datasets  
contained in `data/processed/hazards/`. These checksums ensure that all hazard products  
(tornado, flood, drought, and wildfire datasets) remain unaltered from their validated versions.  

Checksum verification forms the backbone of **data integrity** within the  
**Master Coder Protocol (MCP)** and integrates directly with **STAC metadata**  
for cross-referenced provenance tracking.

---

## 🎯 Purpose

- **Integrity Validation:** Ensure each hazard dataset (GeoTIFF/GeoJSON) remains identical post-build.  
- **Transparency:** Provide verifiable hashes linked to STAC and MCP provenance records.  
- **Reproducibility:** Enable third-party researchers to independently confirm data consistency.  
- **Automation:** Integrate with continuous integration (CI/CD) for auto-validation of all hazard layers.  

---

## 🧱 Directory Layout

```bash
data/
└── processed/
    └── hazards/
        └── checksums/
            ├── tornado_tracks_1950_2024.geojson.sha256
            ├── fema_disasters_1953_2024.geojson.sha256
            ├── drought_spi12_1950_2024.tif.sha256
            ├── wildfire_points_2000_2023.geojson.sha256
            ├── flood_events_1900_2020.geojson.sha256
            └── README.md
````

Each `.sha256` file corresponds directly to its associated dataset and metadata entry
found under `data/processed/hazards/metadata/`.

Example content:

```text
1b5a7f129bc0cde23c18da63b32b17e6b12a926a9b92b57975db5ef938c3f142  tornado_tracks_1950_2024.geojson
```

---

## 🧩 Checksum Standards

| Property      | Value                                                                |
| ------------- | -------------------------------------------------------------------- |
| **Algorithm** | SHA-256 (Secure Hash Algorithm, 256-bit)                             |
| **Format**    | GNU Coreutils `sha256sum` (`<hash>  <filename>`)                     |
| **Encoding**  | Binary mode (`--binary`) for OS-independent consistency              |
| **Purpose**   | Reproducible cryptographic fingerprint ensuring dataset immutability |

---

## 🔍 Verification Workflow

### Manual Verification

```bash
# Verify a single dataset checksum
sha256sum -c data/processed/hazards/checksums/tornado_tracks_1950_2024.geojson.sha256

# Verify all hazard checksums
find data/processed/hazards/checksums -name "*.sha256" -exec sha256sum -c {} \;
```

### Example Output

```
tornado_tracks_1950_2024.geojson: OK
flood_events_1900_2020.geojson: OK
drought_spi12_1950_2024.tif: OK
```

If mismatches are detected:

```
fema_disasters_1953_2024.geojson: FAILED
sha256sum: WARNING: 1 computed checksum did NOT match
```

### Automated CI Verification

GitHub Actions (`.github/workflows/stac-validate.yml`) automatically validates these checksums
on every commit and Pull Request, ensuring the project repository remains trustworthy.

---

## 🌐 Integration with MCP & STAC

Checksums serve as the **cryptographic glue** between file-level integrity and semantic metadata.

1. **MCP Provenance**
   Each dataset’s metadata JSON includes:

   ```json
   "mcp_provenance": "sha256:1b5a7f129bc0cde23c18da63b32b17e6b12a926a9b92b57975db5ef938c3f142"
   ```

   This binds the file’s identity to its metadata.

2. **STAC Catalog Linkage**
   STAC Items in `data/stac/items/hazards_*` reference these hashes, ensuring that catalog entries
   reflect verified and validated datasets.

Together, this ensures **end-to-end verification** across all layers of the Kansas Frontier Matrix data architecture.

---

## ⚙️ Adding or Updating Checksums

1. Generate a checksum for a new or modified file:

   ```bash
   sha256sum <dataset> > data/processed/hazards/checksums/<dataset>.sha256
   ```

2. Verify integrity:

   ```bash
   sha256sum -c data/processed/hazards/checksums/<dataset>.sha256
   ```

3. Update the corresponding `mcp_provenance` field in metadata and STAC entries.

4. Commit both dataset and `.sha256` file together.

5. Validate using Make:

   ```bash
   make validate-hazards
   ```

6. Submit a Pull Request — automated CI will re-verify all checksums.

---

## 📖 References

* **NOAA Storm Events Database:** [https://www.ncei.noaa.gov/stormevents/](https://www.ncei.noaa.gov/stormevents/)
* **FEMA Disaster Declarations Open Data:** [https://www.fema.gov/openfema-data-page/disaster-declarations-summaries-v2](https://www.fema.gov/openfema-data-page/disaster-declarations-summaries-v2)
* **NASA FIRMS Fire Data:** [https://firms.modaps.eosdis.nasa.gov/](https://firms.modaps.eosdis.nasa.gov/)
* **US Drought Monitor:** [https://droughtmonitor.unl.edu/](https://droughtmonitor.unl.edu/)
* **USGS Flood Science:** [https://www.usgs.gov/mission-areas/water-resources/science/floods](https://www.usgs.gov/mission-areas/water-resources/science/floods)
* **STAC Specification 1.0:** [https://stacspec.org](https://stacspec.org)
* **Master Coder Protocol (MCP):** [`docs/standards/`](../../../../docs/standards/)

---

<div align="center">

*“Every storm, every fire, every flood — these checksums ensure the history of Kansas hazards remains untampered and true.”*

</div>
```

