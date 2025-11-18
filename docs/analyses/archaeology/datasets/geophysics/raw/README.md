---
title: "🔭 Kansas Frontier Matrix — Raw Geophysics Data"
path: "docs/analyses/archaeology/datasets/geophysics/raw/README.md"
version: "v11.0.0"
last_updated: "2025-11-17"
review_cycle: "Annual / Archaeology · Geophysics Leads"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../../../../schemas/telemetry/archaeology-geophysics-raw-v1.json"
governance_ref: "../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 🔭 **Raw Geophysics Data (Archaeology)**
`docs/analyses/archaeology/datasets/geophysics/raw/README.md`

**Purpose:**  
Document storage, provenance, and handling rules for **raw geophysical survey datasets** used  
in Kansas Frontier Matrix archaeological analyses (magnetometry, GPR, EM, resistivity).  
This directory preserves **unaltered, original-format** instrument files for reproducible processing  
in ETL pipelines and Story Node spatial narratives.

</div>

---

## 📘 Overview

This directory contains **raw, unprocessed geophysics data** as collected in the field.  
No cleaning, filtering, correction, coordinate transformation, or interpolation occurs here.

Raw files feed downstream ETL pipelines:

- `import → standardize → clean → georeference → rasterize/vectorize → QA → publish`

These inputs are required for:

- archaeological prospection  
- settlement pattern analysis  
- feature detection modeling  
- 3D subsurface scene generation for Focus Mode  
- provenance-complete Story Node integration  

---

## 🗂 Directory Layout

```text
geophysics/
└── raw/
    ├── magnetometry/
    ├── gpr/
    ├── resistivity/
    ├── electromagnetic/
    ├── metadata/
    ├── provenance/
    └── README.md  ← this file
````

---

## 🧪 Data Types & File Formats

Raw geophysical data may include:

### Magnetometry

* .txt, .dat, .csv
* instrument-native binary formats (G-858, FM256, GEM)
* GPS logs & track files

### Ground Penetrating Radar (GPR)

* .dzt, .rd3/.rad, .sgy
* header files (.hdr, .inf)
* time-zero files

### Electrical Resistivity

* .bin, .dat, .asc
* array configuration files
* voltage/current logs

### Electromagnetic Induction

* .csv, .dat
* multi-frequency instrument logs
* calibration metadata

### Shared Metadata

* field notes (digitized)
* crew logs
* grid layout sketches
* coordinate systems
* environmental conditions

---

## 🧭 Metadata Requirements (STAC / DCAT / PROV-O)

Each raw dataset must include:

* **STAC Item**

  * `id`, `datetime`, `bbox`, `geometry`, `assets`
  * sensor type + frequency + sampling resolution

* **DCAT Dataset**

  * title, description, rights, access constraints
  * distribution formats and file listing

* **PROV-O Lineage**

  * activity: field acquisition event
  * agent: crew, PI, institution
  * entity: raw data files, logs, calibration sheets

* **CARE Review**

  * evaluate culturally sensitive areas
  * confirm allowed resolution & distribution level

Place metadata files in:

```
geophysics/raw/metadata/
```

---

## 🧬 Provenance

Provenance must be recorded in:

```
geophysics/raw/provenance/
```

Include:

* field acquisition logs
* sensor configuration
* GPS conditions
* environmental notes
* operator names/roles
* calibration steps
* any anomalies or missing lines

Downstream processed datasets must reference **these raw files** in their lineage.

---

## ⚠️ Sensitivity & Access Control

Geophysical datasets **often contain information about subsurface features**, which may include:

* burials
* ceremonial spaces
* sacred landscapes
* sensitive cultural features

**Rules:**

* NEVER publish raw datasets publicly without CARE review
* Use generalization when required
* Store restricted data with proper filesystem permissions
* Story Nodes using this data must reference generalized layers only

---

## 🔧 ETL Integration

Raw data is consumed by Python ETL modules in:

```
src/pipelines/geophysics/
```

Typical pipeline flow:

1. Import raw files
2. Parse instrument formats
3. Standardize to project schema
4. Georeference grids
5. Apply corrections (diurnal, drift, gain)
6. Create rasters/vectors
7. QA & repair
8. Export STAC items
9. Record provenance

Raw → Processed → Derived → Final

Each transition must have an entry in the **transformations log**.

---

## 📝 Version History

| Version | Date       | Summary                                            |
| ------- | ---------- | -------------------------------------------------- |
| v11.0.0 | 2025-11-17 | Initial creation of raw geophysics dataset README. |
