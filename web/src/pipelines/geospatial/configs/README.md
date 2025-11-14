---
title: "🗺️ Kansas Frontier Matrix — Geospatial Pipeline Configurations (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/src/pipelines/geospatial/configs/README.md"
version: "v10.3.1"
last_updated: "2025-11-13"
review_cycle: "Quarterly / Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../releases/v10.3.0/sbom.spdx.json"
manifest_ref: "../../../../../releases/v10.3.0/manifest.zip"
telemetry_ref: "../../../../../releases/v10.3.0/focus-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/web-geospatial-configs-v1.json"
governance_ref: "../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "MIT"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 🗺️ **Kansas Frontier Matrix — Geospatial Pipeline Configurations**  
`web/src/pipelines/geospatial/configs/README.md`

**Purpose:**  
Define the **client-side geospatial configuration registry** for the Kansas Frontier Matrix (KFM) Web Platform.  
These configuration assets support ethical, deterministic, and FAIR+CARE-governed rendering of geospatial layers in **MapLibre**, **Cesium**, and **timeline-based** visualizations.  
All configs enforce **MCP-DL v6.3**, **WCAG 2.1 AA**, **GeoJSON/COG standards**, and **CARE protective masking**.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP_v6.3-blue)]()  
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Geospatial-orange)]()  
[![Status](https://img.shields.io/badge/Status-Stable-success)]()  
[![License](https://img.shields.io/badge/License-MIT-green)]()

</div>

---

## 📘 Overview

This directory provides **configuration objects** used by the Web Geospatial Pipeline (`web/src/pipelines/geospatial/*`) to normalize:

- **CRS / projection mappings**
- **Layer metadata and styling rules**
- **CARE-governed masking definitions (H3 generalization, redaction zones)**
- **Elevation, terrain, and DEM-blending profiles**
- **Raster/Vector ingestion parameters for STAC/DCAT-backed assets**
- **Temporal bands for predictive overlays (2030–2100)**

These configurations define *how the web-tier transforms raw geospatial metadata into safe, accessible, consistent map layers*.

---

## 🗂️ Directory Layout

~~~~~text
web/src/pipelines/geospatial/configs/
├── README.md                       # This file
│
├── projections.json                # CRS definitions and Kansas-specific projection profiles
├── layers.json                     # Layer registry (hydrology, climate, hazards, treaties, ecology)
├── masking.json                    # CARE-governed redaction masks (H3, buffers, coordinate rules)
├── terrain.json                    # DEM blending rules, COG elevation settings, Cesium terrain profiles
├── symbology.json                  # Legend & style tokens for map layers
├── temporal_bands.json             # Predictive time windows (2030–2100 SSPs, drought cycles)
└── metadata.json                   # Telemetry, governance, and configuration lineage
~~~~~

Each JSON file is validated in CI using schema guards and FAIR+CARE governance rules.

---

## 🧭 Configuration Architecture (Indented Mermaid)

~~~~~mermaid
flowchart TD
  A["STAC/DCAT Metadata"] --> B["Config Loader<br/>(projections · layers · masking)"]
  B --> C["Geospatial Pipeline<br/>(focus · stac · layers)"]
  C --> D["Map/Terrain Engine<br/>(MapLibre · Cesium)"]
  D --> E["Focus Mode / StoryNodes<br/>Temporal + Spatial Sync"]
  E --> F["Telemetry + Governance Logs"]
~~~~~

---

## 🧩 Configuration Modules

### **1. projections.json**
Defines CRS mappings for all supported layers.

**Includes:**
- EPSG codes for Kansas (4326, 3857, 26914, custom GRIDs)  
- Fallback CRS for legacy historic datasets  
- Cesium terrain projection hints  
- Reprojection safety flags

---

### **2. layers.json**
Defines metadata for all web-facing layer groups.

**Examples:**
- `hydrology_streamflow`, `climate_anomalies`, `treaty_boundaries`, `ecology_biomes`, `historic_plats`  
- Attribution tokens  
- COG/GeoJSON ingestion rules  
- Recommended opacity & elevation settings  
- Category mapping to legends

---

### **3. masking.json**
Implements CARE-governed geospatial protections.

**Features:**
- H3 r7/r8 generalization for archaeology & heritage  
- Buffer-based coordinate redaction  
- Sovereignty boundary filters  
- UI-level masking cues (passed to Focus Mode & MapView)

Outputs feed both:

```
web/src/hooks/useGovernance.ts
web/src/pipelines/layerPipeline.ts
```

---

### **4. terrain.json**
Defines topographic + 3D rendering parameters.

**Contains:**
- DEM blending presets (LiDAR + historic contour stacks)  
- Cesium terrain provider configurations  
- Slope/relief exaggeration rules  
- Motion-safe elevation transitions

---

### **5. symbology.json**
Defines legend and style tokens for all layers.

- Color scales (WCAG-checked)
- Iconography tokens for map markers  
- Classification rules (quantile, natural breaks, thresholds)  
- Pattern fills for predictive bands  
- CARE-warning symbol mappings

---

### **6. temporal_bands.json**
Defines predictive and historical windows used in timeline + Focus Mode.

Examples:
- 2030–2050 drought projections  
- 2050–2100 hydrology shift windows  
- Historic migration windows (1854–1890)  
- Paleo-ecological overlays (deep time layers using Cesium)

---

### **7. metadata.json**
Tracks:

- Version + checksum  
- Provenance  
- Schema compatibility  
- Telemetry fields  
- Governance enforcement history

Example reference:

```
docs/reports/audit/web-geospatial-config-ledger.json
```

---

## ⚖️ FAIR+CARE Compliance

| Requirement | Implementation |
|------------|----------------|
| **Findable** | All config entries indexed in metadata.json + telemetry. |
| **Accessible** | JSON schemas + human-readable docs. |
| **Interoperable** | CRS/STAC/DCAT interoperability guaranteed. |
| **Reusable** | Versioned tokens reused across all pipelines. |
| **CARE – Authority** | Masking.json enforces tribal/heritage governance. |
| **CARE – Ethics** | Prevents sensitive coordinate disclosure. |

---

## 📡 Telemetry Integration

Values emitted when configs load:

- `config_load_time_ms`  
- `masking_triggers`  
- `terrain_profile_applied`  
- `layer_registry_hits`  
- `predictive_bands_enabled`  

Telemetry stored in:

```
../../../../../releases/v10.3.0/focus-telemetry.json
```

---

## 🧪 CI Validation

CI ensures:

- JSON Schema correctness  
- CRS validity  
- Token consistency across layers  
- Masking rules applied before render  
- Symbology contrast checks ≥ WCAG 2.1 AA  
- Predictive bands correctly aligned with STAC temporal fields  

Any validation failure → merge blocked.

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|---------|--------|--------|---------|
| v10.3.1 | 2025-11-13 | Web Geospatial Team | Initial v10 configs module; added predictive bands + CARE masking v3. |

---

<div align="center">

**Kansas Frontier Matrix — Web Geospatial Configurations**  
Spatial Integrity × Ethical Governance × Predictive Insight  
© 2025 Kansas Frontier Matrix — MIT License  

[Back to Geospatial Pipelines](../README.md) · [Web Source Index](../../README.md)

</div>

