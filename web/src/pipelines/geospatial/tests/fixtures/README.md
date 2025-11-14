---
title: "📦 Kansas Frontier Matrix — Geospatial Test Fixtures (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/src/pipelines/geospatial/tests/fixtures/README.md"
version: "v10.3.1"
last_updated: "2025-11-13"
review_cycle: "Quarterly / Autonomous / FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../releases/v10.3.0/sbom.spdx.json"
manifest_ref: "../../../../../../releases/v10.3.0/manifest.zip"
telemetry_ref: "../../../../../../releases/v10.3.0/focus-telemetry.json"
telemetry_schema: "../../../../../../schemas/telemetry/web-geospatial-fixtures-v1.json"
governance_ref: "../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "MIT"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 📦 **Kansas Frontier Matrix — Geospatial Test Fixtures**  
`web/src/pipelines/geospatial/tests/fixtures/README.md`

**Purpose:**  
Provide a **controlled, FAIR+CARE-governed set of geospatial test fixtures** used across the KFM web geospatial pipeline test suite.  
These datasets (synthetic + curated real-world samples) ensure **deterministic**, **ethically safe**, and **reproducible** validation of coordinate masking, CRS handling, temporal banding, GeoJSON normalization, and geospatial rendering logic.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP_v6.3-blue)]()  
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Test-Fixtures-orange)]()  
[![Status](https://img.shields.io/badge/Status-Stable-success)]()  
[![License: MIT](https://img.shields.io/badge/License-MIT-green)]()

</div>

---

## 📘 Overview

The **Fixtures Module** contains representative geospatial data prepared for:

- H3-based masking tests  
- CRS projection mismatch tests  
- Raster/GeoJSON extent validation  
- DEM/imagery blending heuristics  
- Predictive temporal band exercises (e.g. 2030–2100 SSP layers)  
- CARE-governed coordinate redaction  
- Synthetic cases mirroring Kansas hydrology, hazards, ecology, and treaties  
- Multi-resolution geometry edge cases (dense lines, multi-polygons, large rasters)

Fixtures obey:

- **FAIR+CARE** (no sensitive or precise Indigenous/archaeological coordinates)  
- **WCAG 2.1 AA** (contrast-safe symbology metadata)  
- **STAC 1.0** (metadata-mapped test items)  
- **MCP-DL v6.3** (documentation + reproducibility requirements)

---

## 🗂️ Directory Layout

~~~~~text
web/src/pipelines/geospatial/tests/fixtures/
├── README.md                          # This file
│
├── sample_geojson.json                # Synthetic + simplified Kansas geometries
├── sample_raster_bounds.json          # Expected extents for DEM/raster test cases
├── sample_masking_cases.json          # H3 + fuzzing + sovereignty masking tests
├── sample_projection_mismatch.json    # CRS mismatch + fallback projection samples
└── metadata.json                      # Fixture lineage, provenance & telemetry metadata
~~~~~

---

## 🧩 Fixture Types & Purposes

### **1. sample_geojson.json**
Includes:

- Streams, tributaries, and simplified watershed boundaries  
- County outlines + buffered treaty boundaries  
- Multi-resolution geometry tests (dense → simplified)  
- Ensures `clipGeoJSON` and `extentCalculator` handle realistic shapes  

### **2. sample_raster_bounds.json**
Stores:

- Raster footprints  
- Alpha-masked nodata regions  
- Boundaries for DEM blending tests  
- Used to validate `extentCalculator` + blend/terrain scripts  

### **3. sample_masking_cases.json**
Contains CARE-governed synthetic examples:

- Archaeological point clusters → H3 r7/r8 generalization  
- Polygon dilation for sovereignty boundaries  
- Fuzzed coordinates applied to test safety logic  
- Ensures `maskCoordinates.ts` enforces governance rules  

### **4. sample_projection_mismatch.json**
Provides:

- EPSG mismatches  
- Deprecated CRS examples  
- Custom Kansas projection samples  
- Tests fallback logic in `projectionHints.ts`  

### **5. metadata.json**
Tracks:

- Fixture checksums  
- Provenance source (synthetic / curated)  
- Schema validity  
- Telemetry fields  
- CARE governance evaluation  

---

## 🔐 FAIR+CARE Alignment

| Principle | Implementation |
|----------|----------------|
| **Findable** | Fixtures indexed with stable IDs in metadata.json. |
| **Accessible** | Human-readable JSON with documented structures. |
| **Interoperable** | GeoJSON, STAC-like, and CRS metadata aligned. |
| **Reusable** | Versioned, deterministic fixtures usable across pipelines. |
| **CARE — Authority** | No real-world sensitive coordinates; all synthetic or generalized. |
| **CARE — Ethics** | Guarantees no test inadvertently reveals protected information. |

Governance reference:

```
../../../../../docs/reports/audit/web-geospatial-fixtures-ledger.json
```

---

## 📡 Telemetry Integration

Every fixture load registers metrics:

- `fixture_load_time_ms`  
- `masking_case_evaluations`  
- `crs_mismatch_triggered`  
- `raster_bounds_checks`  
- `geojson_validation_passed`  

Telemetry exported via:

```
../../../../../releases/v10.3.0/focus-telemetry.json
```

---

## 🧪 CI Validation Rules

CI enforces:

- JSON Schema correctness  
- CRS validity in `sample_projection_mismatch.json`  
- No sensitive coordinates (automated H3-based scan)  
- Raster-bound correctness  
- Predictive temporal alignment where relevant  
- All fixtures checksum-verified  

Any violations block merge.

---

## 🧾 Example Fixture Metadata Entry

~~~~~json
{
  "fixture_id": "geospatial_fixtures_v10.3.1",
  "files": [
    "sample_geojson.json",
    "sample_raster_bounds.json",
    "sample_masking_cases.json",
    "sample_projection_mismatch.json"
  ],
  "checksum_verified": true,
  "care_compliant": true,
  "schema_valid": true,
  "timestamp": "2025-11-13T20:55:00Z",
  "governance_ref": "docs/reports/audit/web-geospatial-fixtures-ledger.json"
}
~~~~~

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|---------|--------|--------|---------|
| v10.3.1 | 2025-11-13 | Web Geospatial Team | Initial v10 fixture suite; validated synthetic datasets; CARE masking v3; CRS invalidation tests. |

---

<div align="center">

**Kansas Frontier Matrix — Geospatial Fixtures**  
Deterministic Testing × Ethical Redaction × Provenance Integrity  
© 2025 Kansas Frontier Matrix — MIT License  

[Back to Test Suite](../README.md)

</div>

