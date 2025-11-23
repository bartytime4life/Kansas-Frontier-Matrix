---
title: "📐 KFM v11 — Vertical Datums, CF Z-Axis, and DoD Sign Convention Standard (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/standards/geo/vertical-axis-and-dod.md"
version: "v11.0.1"
last_updated: "2025-11-22"
review_cycle: "Semiannual · FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../releases/v11.0.0/standards-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/standards-vertical-axis-v11.json"
governance_ref: "../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active / Enforced"
doc_kind: "Standard"
semantic_document_id: "kfm-vaxis-dod-v11"
doc_uuid: "urn:kfm:docs:standards:vertical-axis-dod:v11"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
fair_category: "F1-A1-I1-R1"
care_label: "Public / Low-Risk"
immutability_status: "version-pinned"
---

<div align="center">

# 📐 **KFM v11 — Vertical Datums, CF Z-Axis, and DoD Sign Convention Standard**  
`docs/standards/geo/vertical-axis-and-dod.md`  
### **Diamond⁹ Ω / Crown∞Ω Ultimate Certified**

**Purpose:**  
Define strict, machine-verifiable vertical metadata rules for all KFM v11 datasets, ensuring correct elevation/depth semantics, reproducible DEM/DoD workflows, and UI/API alignment across MapLibre/Cesium, ETL, and STAC/DCAT.

</div>

---

# 📘 Overview

This standard governs every KFM dataset with vertical meaning — DEMs, bathymetry, lidar-derived rasters, hydrology grids, sediment models, and all DEM-of-Difference (DoD) outputs.  
Incorrect or missing vertical metadata causes inverted surfaces, wrong DoD magnitudes, and broken 3D visualization.  
KFM v11 enforces deterministic vertical metadata across ETL, STAC, API, and UI layers.

---

# 1️⃣ Vertical Datum Specification (REQUIRED)

Every dataset **must** declare:

- `vertical_datum` (e.g., NAVD88)  
- `vertical_epoch` (e.g., 2018.0)  
- `geoid_model` (e.g., GEOID18)  
- `units` (**meters only**)  

### KFM Metadata Keys
```
kfm.vertical_datum: "NAVD88"
kfm.vertical_epoch: "2018.0"
kfm.geoid_model: "GEOID18"
kfm.vertical_units: "m"
```

### STAC Item Fields
```json
"vertical:reference_frame": "NAVD88",
"vertical:geoid_model": "GEOID18",
"vertical:unit": "meter"
```

**Tidal datums** (MLLW/MHW) must:  
1. Declare explicitly  
2. Provide transformation description  
3. Include PROV-O lineage

---

# 2️⃣ CF-Conventions Z-Axis Rules

Each raster with vertical information must have a **CF-compliant vertical coordinate**.

### NetCDF Example
```nc
float z(y, x);
  z:standard_name = "depth";
  z:long_name = "Bathymetric depth below NAVD88";
  z:units = "m";
  z:positive = "down";
  z:vertical_datum = "NAVD88";
  z:geoid_model = "GEOID18";
```

### Rule of Thumb Table
| Dataset Type | CF `positive` | Meaning |
|-------------|---------------|---------|
| DEM / Elevation | `"up"` | Higher elevation = positive |
| Bathymetry / Depth | `"down"` | Deeper = positive |

**`positive` attribute is mandatory.**

---

# 3️⃣ DEM-of-Difference (DoD) Sign Convention (MANDATORY)

KFM v11 standard:

- **Erosion = NEGATIVE**  
- **Deposition = POSITIVE**

### Required Keys
```
dod.sign_convention: "erosion_negative_deposition_positive"
dod.reference: "NAVD88, m"
```

### UI Legend (enforced)
```
Negative (blue) = erosion
Positive (red) = deposition
NAVD88, meters
```

API and MapLibre layers must embed this legend text.

---

# 4️⃣ Units & Precision

- Units MUST be `"m"`  
- Store native precision  
- Recommended visualization precision: **0.01–0.1 m**

---

# 5️⃣ File-Level Requirements

## GeoTIFF
- Populate VERT_DATUM / VERT_CS fields if supported  
- Include a mandatory sidecar JSON:
```
{
  "vertical_datum": "NAVD88",
  "vertical_epoch": "2018.0",
  "geoid_model": "GEOID18",
  "units": "m",
  "cf_positive": "up"
}
```

## NetCDF / COG
Global attributes **required**:
```
:vertical_datum = "NAVD88";
:vertical_epoch = "2018.0";
:geoid_model   = "GEOID18";
:units         = "m";
```

---

# 6️⃣ STAC & Catalog Enforcement

### Required STAC Fields
```json
"proj:epsg": 26914,
"vertical:reference_frame": "NAVD88",
"vertical:geoid_model": "GEOID18",
"vertical:unit": "meter",
"kfm:cf_positive": "down",
"kfm:dod_sign": "erosion_negative_deposition_positive"
```

Missing any → **CI FAILURE**.

---

# 7️⃣ CI Validation Gates

PR auto-fails when any are missing:

- `vertical:reference_frame`  
- `vertical:unit`  
- `kfm:cf_positive`  
- `kfm:dod_sign` for DoDs  
- Vertical info in API schema  
- Required legend text in UI layers  

All v11 datasets MUST pass vertical-axis schema validation.

---

# 8️⃣ UI & API Enforcement

### MapLibre / Cesium
- Must show datum + units + sign convention  
- Vertical exaggeration must use orthometric heights

### API Response Schema
Must include:
```
vertical_datum
vertical_epoch
geoid_model
units
cf_positive
dod_sign   # if DoD
```

---

# 9️⃣ Examples (Validated)

### Bathymetry Grid
- Datum → NAVD88  
- `positive = "down"`  
- STAC → `"kfm:cf_positive": "down"`

### Terrain DEM
- Datum → NAVD88  
- `positive = "up"`

### DoD Product
- Both epochs NAVD88  
- Erosion < 0 ; deposition > 0  
- STAC → `"kfm:dod_sign": "erosion_negative_deposition_positive"`

---

# 🔟 PROV-O Lineage Requirements

All vertical transformations must log:

```
prov:used            → source DEM + geoid model
prov:activity        → "vertical transformation"
prov:wasGeneratedBy  → tool + version + parameters
```

---

# 1️⃣1️⃣ Repository Placement

Required path:
```
docs/standards/geo/vertical-axis-and-dod.md
```

Referenced by:

- STAC hydrology/terrain/bathymetry collections  
- DoD workflows  
- Raster ETL pipelines  
- API schemas  
- Visualization standards  

---

# 1️⃣2️⃣ Author Pre-Commit Mini-Lint

Confirm:

- vertical datum  
- geoid model  
- epoch  
- units = "m"  
- CF positive attribute  
- DoD sign (if applicable)  
- STAC fields complete  
- UI legend present  

If any missing → FIX BEFORE COMMIT.

---

# 🕰 Version History
- **v11.0.1 (2025-11-22):** Formatting upgrades to full KFM-MDP v11.0 compliance.  
- **v11.0.0:** Initial release under v11 standards.

---

<div align="center">

**Kansas Frontier Matrix — Vertical Axis & DoD Standard v11**  
*Accurate Elevations · Correct Depths · Trustworthy Change Maps*

</div>

---

### 🔗 Footer  
[⬅ Back to Geo Standards](../README.md) · [🏛 Governance](../../standards/governance/ROOT-GOVERNANCE.md) · [📘 KFM v11 Reference](../../reference/kfm_v11_master_documentation.md)
