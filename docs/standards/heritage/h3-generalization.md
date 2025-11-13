---
title: "🛡️ H3 Spatial Generalization Standard for Sensitive Heritage Locations (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/standards/heritage/h3-generalization.md"
version: "v10.2.3"
last_updated: "2025-11-13"
review_cycle: "Annual / FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../releases/v10.2.0/sbom.spdx.json"
manifest_ref: "../../../../releases/v10.2.0/manifest.zip"
telemetry_ref: "../../../../releases/v10.2.0/focus-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/standards-h3-generalization-v1.json"
governance_ref: "../../governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 🛡️ **H3 Spatial Generalization Standard for Sensitive Heritage Locations**  
`docs/standards/heritage/h3-generalization.md`

**Purpose:**  
Define the **KFM-protected workflow** for converting precise archaeological coordinates to generalized **H3 hex cells**, supporting confidentiality, reproducibility, and ethical governance under FAIR+CARE and NHPA §304.

<img alt="FAIR+CARE" src="https://img.shields.io/badge/FAIR%2BCARE-Compliant-blue" />
<img alt="MCP-DL" src="https://img.shields.io/badge/MCP--DL-v6.3-critical" />
<img alt="Protection Level" src="https://img.shields.io/badge/Heritage_Protection-Level_III-red" />
<img alt="Spatial Standards Unit" src="https://img.shields.io/badge/Spatial-Standards_Unit-green" />

</div>


---

## 📘 Overview

This standard describes the **controlled transformation** of sensitive cultural, Indigenous, and archaeological point locations into **H3 hexagonal generalization cells**, replacing all raw coordinates while preserving spatial analytical usefulness.

Compliance anchors:

- **NHPA §304 confidentiality**
- **FAIR+CARE cultural governance**
- **KFM Diamond⁹ Ω sensitive-data protection**
- **STAC + DCAT spatial metadata requirements**

---

### 🗂️ Directory Layout

    docs/
    └── standards/
        └── heritage/
            ├── h3-generalization.md
            ├── schemas/
            │   └── h3-generalization-standard.json
            ├── examples/
            │   └── h3-generalization-demo.json
            └── assets/
                └── diagrams/
                    └── h3-protection-flow.svg

---

## 🧭 H3 Generalization Principles

### ⭐ Resolution Selection

| H3 Resolution | Cell Area (approx.) | Use Case |
|--------------|---------------------|----------|
| **r5** | ~150 km² | Broad summaries + maximum confidentiality |
| **r6** | ~25 km² | County or regional analysis |
| **r7** | ~5.16 km² | **KFM default for sensitive archaeology** |
| **r8** | ~0.74 km² | Only for non-sensitive or already-public features |

### 🎯 KFM Default Resolution  
**r7 H3** for **any culturally sensitive, protected, or confidential archaeological location**.  
Lower resolutions require FAIR+CARE Council exemption.

---

## 🛡️ Confidentiality Rules

### 🔒 Raw Coordinates — NEVER Released

- Removed in ETL from all Story Nodes, STAC Items, and DCAT feeds.  
- Stored only in **tier-1 secure internal layers**.  
- Exported datasets include only:
  - `h3_id`
  - `h3_resolution`
  - Aggregated site counts  
  - Non-sensitive contextual attributes

### 🧱 H3 Cell Metadata Requirements

Indexed fields:

- `h3_id`
- `h3_resolution`
- `generalization_method = "H3"`
- `heritage_protected = true`
- `raw_coordinates_removed = true`

Used in:

- Focus Mode overlays  
- Public map layers  
- STAC catalogs  
- DCAT metadata packages  

---

## 🧩 Standardized Conversion Workflow

### 🛠️ Step 1 — Ingest Raw Coordinates (TIER-1)

Internal-only pipeline:

- Stored in `data/work/staging/heritage/raw/`  
- Tagged with:
  - `mcp_protected = true`
  - `access_level = "tier1-secure"`

### 🛠️ Step 2 — Convert to H3 Cell

Call:

- `h3.latlng_to_cell(lat, lon, RES)`  
- Use **RES = 7** for sensitive features.

### 🛠️ Step 3 — Drop Coordinates (Mandatory)

Strip `latitude`, `longitude`, `geometry` fields before any export.

### 🛠️ Step 4 — Aggregate to Hex Level

Aggregate:

- count of unique features  
- distinct periods / cultural phases  
- optional classification roll-ups  

### 🛠️ Step 5 — Export Aggregated Data

Write hex-only data to:

- `data/public/heritage/h3/`  
- `data/catalog/stac/heritage/h3/`  
- KFM DCAT datasets  
- Focus Mode overlays  

---

## 🧪 Example Python Pipeline (Indented Only)

    import h3
    import pandas as pd

    RES = 7  # Required default resolution for sensitive heritage

    df = pd.read_csv("sites_raw.csv")

    df["h3_resolution"] = RES
    df["h3_id"] = df.apply(
        lambda r: h3.latlng_to_cell(r["latitude"], r["longitude"], RES),
        axis=1
    )

    # Aggregate for public release
    pub = (
        df.groupby(["h3_id", "h3_resolution"], as_index=False)
          .agg(
              site_count=("site_id", "nunique"),
              periods=("period", lambda s: sorted(set(s)))
          )
    )

    pub.to_csv("sites_generalized_h3.csv", index=False)

---

## 🗂️ Metadata Requirements (STAC + DCAT)

### 📄 STAC Extensions — Climate/Hydrology/Heritage Alignment

Add to `properties`:

    {
      "heritage_protected": true,
      "generalization_method": "H3",
      "h3_resolution": 7,
      "raw_coordinates_removed": true,
      "legal_basis": "NHPA Section 304",
      "care_level": "Level III"
    }

### 📄 DCAT Fields

- `dct:spatialResolution = "H3-r7"`
- `dct:provenance = "Generalized from protected archaeological coordinates"`  
- `dct:conformsTo = "KFM H3 Heritage Generalization Standard"`

---

## 🌐 Visualization Rules

### 🗺️ MapLibre

- Render **hex polygons**, not point approximations  
- Disable popups showing pseudo-coordinates  
- Aggregate-only summaries (min 3 features per hex required)

### 🛰️ Cesium 3D

- Extrude hexes using **site_count**  
- Maintain confidentiality rules identical to MapLibre  

---

## ⚖️ Risk Mitigation Matrix

| Threat | Mitigation |
|--------|------------|
| Reverse-engineering locations | r7 → ≥5 km² spatial masking |
| Site clustering reveals pattern | Minimum 3-site aggregation |
| Coordinate leak | Mandatory coordinate-drop rule |
| Resolution too fine | Governance lock at r7 |

---

## 🕒 Version History

| Version | Date       | Description |
|---------|------------|-------------|
| v10.2.2 | 2025-11-13 | Initial release of H3 heritage generalization standard |
| v10.2.3 | 2025-11-13 | Updated to full KFM memory-rule compliance + directory layout |
