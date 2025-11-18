---

title: "🧲 Kansas Frontier Matrix — Raw Magnetometry Data"
path: "docs/analyses/archaeology/datasets/geophysics/raw/magnetometry/README.md"
version: "v11.0.0"
last_updated: "2025-11-17"
review_cycle: "Annual / Archaeology · Geophysics Leads"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../../../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../../../../../schemas/telemetry/archaeology-geophysics-magnetometry-raw-v1.json"
governance_ref: "../../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
--------------------------

<div align="center">

# 🧲 **Raw Magnetometry Data (Archaeology)**

`docs/analyses/archaeology/datasets/geophysics/raw/magnetometry/README.md`

**Purpose:**
Define storage, metadata, provenance, QA requirements, and ETL integration rules for **raw magnetometry datasets** used in Kansas Frontier Matrix archaeological geophysics (feature detection, anomaly mapping, settlement analysis, and subsurface modeling).
This directory preserves original instrument outputs for reproducible workflows and complete provenance documentation.

</div>

---

## 📘 Overview

This directory contains **raw, unprocessed magnetometry data** exactly as acquired in the field.
These files serve as authoritative inputs for all downstream ETL operations, including:

* drift and diurnal correction
* coordinate integration
* interpolation and gridding
* noise filtering
* anomaly extraction
* raster/vector conversions
* STAC Item construction
* Story Node subsurface scene generation

Raw files must remain **immutable** to preserve provenance integrity.

---

## 🗂 Directory Layout

```text
magnetometry/
├── <survey-id-1>/
│   ├── raw/                # instrument output files
│   ├── metadata/           # STAC, DCAT, crew logs, survey notes
│   └── provenance/         # PROV-O lineage for the field acquisition
├── <survey-id-2>/
│   └── ...
└── README.md  ← this file
```

Each `<survey-id>` corresponds to a unique magnetometry field collection event.

---

## 🧪 Data Types & File Formats

### Magnetometry Instrument Data

* `.dat`, `.bin`, `.g858` (Geometric G-858/G-859)
* `.dat`, `.raw`, `.txt` (FM256)
* `.xyz`, `.dat` (GEM Systems)
* `.txt`, `.csv` (Bartington)
* Vendor-specific binary formats

### GPS & Spatial Logs

* `.csv`
* `.gpx`
* `.nmea`

### Field Documentation

* `.pdf`, `.jpg`, `.png` (sketches, field notes, grid setup)
* Crew logs with:

  * grid orientation
  * environmental conditions
  * equipment settings
  * anomalies detected during acquisition

---

## 🧭 Metadata Requirements (STAC / DCAT / PROV-O)

Every survey must include:

### **STAC Item**

* `id`, `datetime`, `bbox`, `geometry`
* instrument model, sampling frequency
* complete asset listing pointing to raw files

### **DCAT Dataset**

* title, description
* rights, license, access constraints
* instrument specifications
* distribution metadata

### **PROV-O Lineage**

* **Entity:** raw files, GPS logs, field notes
* **Activity:** magnetometry acquisition event
* **Agent:** field crew, PI, institution

Place all metadata in:

```
magnetometry/<survey-id>/metadata/
```

---

## 🧬 Provenance

Provenance documentation must live in:

```
magnetometry/<survey-id>/provenance/
```

Include:

* acquisition notes
* crew roles
* instrument configuration
* drift/diurnal conditions
* anomalies encountered
* missing or corrupted lines
* GPS/instrument sync notes

Downstream datasets must reference these raw files in their lineage.

---

## ⚠️ Sensitivity & Access Control

Raw magnetometry data may reveal culturally sensitive subsurface features such as:

* burials
* ceremonial structures
* sacred landscape formations
* high-significance occupation features

**Rules:**

* Raw magnetometry data must **never** be publicly released without CARE review
* Spatial generalization may be required
* Restricted surveys must be identified in `metadata/access-control.yml`
* Story Nodes must reference **generalized** derived rasters, not raw data

---

## 🔧 ETL Integration

Raw magnetometry data is processed by:

```
src/pipelines/geophysics/magnetometry/
```

Standard ETL flow:

1. Import raw instrument files
2. Parse sensor headers + GPS logs
3. Merge positional and magnetic data
4. Apply drift and diurnal corrections
5. Interpolate and grid
6. Optional noise reduction
7. Export GeoTIFF rasters and anomaly vectors
8. Generate STAC Items
9. Update PROV-O lineage

Every ETL step must be logged in:

```
provenance/transformations-log.csv
```

---

## 📝 Version History

| Version | Date       | Summary                                              |
| ------- | ---------- | ---------------------------------------------------- |
| v11.0.0 | 2025-11-17 | Initial creation of raw magnetometry dataset README. |

