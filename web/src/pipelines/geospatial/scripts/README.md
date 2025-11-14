---
title: "🛰️ Kansas Frontier Matrix — Web Geospatial Scripts (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/src/pipelines/geospatial/scripts/README.md"
version: "v10.3.1"
last_updated: "2025-11-13"
review_cycle: "Quarterly / Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../releases/v10.3.0/sbom.spdx.json"
manifest_ref: "../../../../../releases/v10.3.0/manifest.zip"
telemetry_ref: "../../../../../releases/v10.3.0/focus-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/web-geospatial-scripts-v1.json"
governance_ref: "../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "MIT"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 🛰️ **Kansas Frontier Matrix — Web Geospatial Scripts**  
`web/src/pipelines/geospatial/scripts/README.md`

**Purpose:**  
Document all **client-accessible geospatial processing scripts** used by the Kansas Frontier Matrix (KFM) web platform.  
These scripts provide the **in-browser geospatial transformation layer** supporting lightweight processing, validation, and rendering guidance for MapLibre, Cesium, and Focus Mode geospatial objects.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP_v6.3-blue)]()  
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Geospatial-orange)]()  
[![Status](https://img.shields.io/badge/Status-Stable-success)]()  
[![License: MIT](https://img.shields.io/badge/License-MIT-green)]()

</div>

---

## 📘 Overview

While **heavy geoprocessing** is performed server-side (GDAL, GeoParquet, PROJ), the **web platform** includes a set of lightweight geospatial scripts that:

- Normalize GeoJSON/TopoJSON layers  
- Perform client-side clipping, projection hints, mask application  
- Execute quick spatial checks (bounds, nodata-aware extents)  
- Provide interactive blending rules for on-the-fly MapLibre/Cesium rendering  
- Attach CARE-governed masking rules (H3 generalization, coordinate fuzzing)  
- Feed Focus Mode and timeline UIs with validated geospatial structures

All scripts comply with:

- **FAIR+CARE governance**  
- **WCAG 2.1 AA** (map accessibility rules)  
- **STAC 1.0** & **DCAT 3.0**  
- **MCP-DL v6.3** documentation + telemetry requirements

---

## 🗂️ Directory Layout

~~~~~text
web/src/pipelines/geospatial/scripts/
├── README.md                      # This file
│
├── clipGeoJSON.ts                 # Client-side bounding-box clipping
├── maskCoordinates.ts             # CARE-governed coordinate masking (H3, fuzzing)
├── extentCalculator.ts            # Spatial bounds calculator for rasters/GeoJSON
├── blendRules.ts                  # DEM/imagery blending logic for MapLibre/Cesium
├── projectionHints.ts             # CRS hinting layer (client-side fallback)
└── metadata.json                  # Script governance, lineage, telemetry metadata
~~~~~

---

## 🧩 Script Responsibilities

### **1. clipGeoJSON.ts**
- Clips GeoJSON against current map extent  
- Respects CARE masking (no clipping that reveals sensitive coordinates)  
- Ensures performance-safe clipping for client FPS preservation  

### **2. maskCoordinates.ts**
- Applies:
  - H3 r7/r8 generalization  
  - Coordinate fuzzing (random noise within safe thresholds)  
  - Polygon dilation for sovereignty-preserving buffers  
- Ensures sensitive archaeological or heritage locations remain protected  

### **3. extentCalculator.ts**
- Detects bounds of raster footprints and vector geometries  
- Handles nodata regions from alpha-mask operations  
- Supports Focus Mode "zoom-to-entity" behavior  

### **4. blendRules.ts**
- Lightweight DEM/imagery-blending parameters for UI  
- Integrates with Cesium heightmaps and MapLibre hillshade layers  
- Supports visual continuity between historic + modern terrain  

### **5. projectionHints.ts**
- Provides projection fallback hints to MapLibre/Cesium when encountering unknown CRS  
- Warns user if CRS is deprecated or risky  
- Integrates with `projections.json` in configs layer  

---

## 🧭 Geospatial Script Architecture (Indented Mermaid)

~~~~~mermaid
flowchart TD
  A["STAC/DCAT Asset Metadata"] --> B["Lightweight Script Layer<br/>(clip · mask · blend · extent · proj-hint)"]
  B --> C["Validated GeoJSON/Render Props<br/>schemaGuards.ts"]
  C --> D["MapLibre 2D / Cesium 3D Engine"]
  D --> E["Focus Mode · Story Nodes · Timeline Views"]
  E --> F["Telemetry + CARE Governance Logs"]
~~~~~

---

## ⚖️ FAIR+CARE Integration

| Requirement | Implementation |
|------------|----------------|
| **Findable** | Scripts indexed via metadata.json + STAC asset IDs. |
| **Accessible** | WCAG 2.1 AA-compliant map interactions maintained. |
| **Interoperable** | Follows GeoJSON, TopoJSON, COG metadata contracts. |
| **Reusable** | Pure functions with stable behavior across browsers. |
| **CARE – Authority** | Mandatory coordinate-masking logic in `maskCoordinates.ts`. |
| **CARE – Ethics** | Redaction ensures no sensitive heritage data exposed. |

Governance references:

```
../../../../../docs/reports/audit/web-geospatial-script-ledger.json
```

---

## 📡 Telemetry Integration

These scripts emit non-PII metrics such as:

- `clip_runtime_ms`  
- `masking_events_triggered`  
- `blend_profile_selected`  
- `projection_hint_applied`  
- `extent_calc_ms`  

Telemetry stored in:

```
../../../../../releases/v10.3.0/focus-telemetry.json
```

---

## 🧪 CI / QA Requirements

CI validates:

- JSON Schema for metadata files  
- Correct masking enforcement (CARE tests)  
- Stable performance via micro-benchmark tests  
- CRS hinting determinism  
- Accessibility tokens used where required  

Failures block merge.

---

## 🧾 Example Script Metadata Entry

~~~~~json
{
  "id": "geospatial_scripts_v10.3.1",
  "scripts": [
    "clipGeoJSON.ts",
    "maskCoordinates.ts",
    "extentCalculator.ts",
    "blendRules.ts",
    "projectionHints.ts"
  ],
  "masking_enforced": true,
  "a11y_compliant": true,
  "telemetry_linked": true,
  "checksum_verified": true,
  "timestamp": "2025-11-13T20:11:00Z",
  "governance_ref": "docs/reports/audit/web-geospatial-script-ledger.json"
}
~~~~~

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|---------|--------|--------|---------|
| v10.3.1 | 2025-11-13 | Web Geospatial Team | Initial client-side script suite; CARE masking v3; telemetry-connected. |

---

<div align="center">

**Kansas Frontier Matrix — Web Geospatial Scripts**  
Client-Side Spatial Intelligence × Ethical Masking × Provenance-Aware Rendering  
© 2025 Kansas Frontier Matrix — MIT License  

[Back to Geospatial Pipelines](../README.md)

</div>

