---
title: "🛰️ Kansas Frontier Matrix — Web Geospatial Scripts Architecture (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/src/pipelines/geospatial/scripts/README.md"
version: "v10.3.2"
last_updated: "2025-11-14"
review_cycle: "Quarterly / Autonomous + FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../releases/v10.3.2/sbom.spdx.json"
manifest_ref: "../../../../../releases/v10.3.2/manifest.zip"
telemetry_ref: "../../../../../releases/v10.3.2/focus-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/web-geospatial-scripts-v2.json"
governance_ref: "../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "MIT"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 🛰️ **Kansas Frontier Matrix — Web Geospatial Scripts Architecture**  
`web/src/pipelines/geospatial/scripts/README.md`

**Purpose:**  
Define the **deep technical architecture** for all client-side geospatial scripts powering the KFM v10.3.2 web platform.  
These scripts form the **lightweight in-browser geospatial engine**, enabling safe, performant, FAIR+CARE-certified spatial transformations directly in the user’s environment.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP_v6.3-blue)]()
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Geospatial-orange)]()
[![Status](https://img.shields.io/badge/Status-Stable-success)]()
[![License](https://img.shields.io/badge/License-MIT-green)]()

</div>

---

# 📘 Executive Summary

The **Web Geospatial Script Layer** provides:

- **Client-side GeoJSON/TopoJSON processing**  
- **Realtime masking and redaction** (H3 r7, fuzzing, sovereignty buffers)  
- **Projection fallback & CRS hinting**  
- **Raster/imagery blending rules** for MapLibre & Cesium  
- **Nodata-aware extent detection**  
- **Provenance & JSON-LD enrichment**  
- **FAIR+CARE-driven spatial governance**  
- **Telemetry emission** (ethics, masking, render cost, projection fixes)  

This layer acts **between** pipelines and rendering engines:

```text
services → pipelines → geospatial scripts → UI → telemetry/governance
```

It is intentionally **lightweight**, **sandboxed**, **deterministic**, and **fully auditable**.

---

# 🗂️ Directory Layout (Authoritative v10.3.2)

```text
web/src/pipelines/geospatial/scripts/
├── README.md
│
├── clipGeoJSON.ts                 # Extent-clipped GeoJSON with CARE masking
├── maskCoordinates.ts             # H3 generalization + fuzzing engine
├── extentCalculator.ts            # Nodata-aware bounds extraction
├── blendRules.ts                  # DEM/imagery blending rules for UI
├── projectionHints.ts             # CRS fallback + projection warning system
└── metadata.json                  # Script-level lineage + governance metadata
```

---

# 🧩 Deep Architecture Overview

```mermaid
flowchart TD
    STAC[STAC DCAT Asset Metadata] --> SCRIPTS[Geospatial Script Layer<br/>clip · mask · blend · extent · projhint]
    SCRIPTS --> VALID[Validation Layer<br/>schemaGuards]
    VALID --> RENDER[Render Engines<br/>MapLibre 2D · Cesium 3D]
    RENDER --> UI[Focus Mode · Story Nodes · Timeline Views]
    UI --> TEL[Telemetry + Governance Logs]
```

Each script must satisfy:

- deterministic output  
- pure function semantics  
- zero side-effects  
- full CARE compliance  
- reproducible transformations  

---

# 🧠 Script-Level Deep Specifications

## 1️⃣ `clipGeoJSON.ts` — Deterministic, CARE-Aware Clipping Engine

### Purpose  
Perform **in-browser bounding-box clipping** for vector layers while maintaining:

- no coordinate exposure for sensitive sites  
- H3-governed generalizations  
- performance budget for 60 FPS rendering  

### Architecture

```mermaid
flowchart LR
    CG1[Input GeoJSON] --> CG2[BBox Intersection]
    CG2 --> CG3[Polygon Splitter]
    CG3 --> CG4[CARE Filter]
    CG4 --> CG5[Output GeoJSON]
```

### Governance Constraints
- If clipping reveals sensitive geometry → **mask** instead  
- If layer is restricted → return only generalized envelope  
- Full provenance injection via JSON-LD after final stage  

---

## 2️⃣ `maskCoordinates.ts` — CARE Masking + Territorial Sovereignty Engine

### Purpose  
Protect culturally sensitive or sovereign areas.

### Masking Stack
- **H3 r7 generalization**  
- **Coordinate fuzzing** (secure RNG noise)  
- **Polygon dilation** (sovereignty buffers)  
- **Site obfuscation** using convex hull bounding  

### Masking Architecture

```mermaid
flowchart TD
    M1[Input Geometry] --> M2[Site Classification<br/>sensitive · restricted]
    M2 --> M3[H3 Generalizer]
    M3 --> M4[Coordinate Fuzzer]
    M4 --> M5[Polygon Buffer]
    M5 --> M6[Governance Stamp]
```

---

## 3️⃣ `extentCalculator.ts` — Nodata-Aware Extent Engine

### Purpose  
Determine robust spatial bounds for:

- GeoJSON / TopoJSON  
- Raster footprints  
- Imagery masks  

### Architecture

```mermaid
flowchart LR
    E1[Geometry or Raster Info] --> E2[Nodata Detector]
    E2 --> E3[Extent Builder]
    E3 --> E4[Outlier Pruner]
    E4 --> E5[Final Extent]
```

This powers:

- “Zoom to entity”  
- “Zoom to dataset”  
- Story Node context previews  

---

## 4️⃣ `blendRules.ts` — UI-Safe DEM + Imagery Blending

### Purpose  
Provide blending logic for terrain, hillshade, historical imagery, and DEM composites.

### Features
- Non-destructive visual masks  
- DEM-first elevation precedence  
- Dynamic opacity curve based on camera height  
- Time-sensitive blends (historic vs modern)  

### Architecture

```mermaid
flowchart TD
    B1[DEM Layer] --> B3[Blend Core]
    B2[Imagery Layer] --> B3
    B3 --> B4[Opacity Curve]
    B4 --> B5[Output Style Props]
```

---

## 5️⃣ `projectionHints.ts` — Projection Resolver & Fallback System

### Purpose  
Enable the browser to handle unknown or exotic CRS definitions gracefully.

### Capabilities
- Detect deprecated CRS  
- Suggest best-fit CRS for Kansas datasets  
- Provide MapLibre/Cesium with numeric projection hints  
- Warn user about projection misalignment  

### Architecture

```mermaid
flowchart LR
    P1[Incoming CRS Tag] --> P2[CRS Knowledge Base]
    P2 --> P3[Fallback Resolver]
    P3 --> P4[UI Warning + Hint Return]
```

---

# 🧭 End-to-End Client-Side Geospatial Flow

```mermaid
flowchart TD
    ASSET[STAC Asset<br/>raster · vector] --> PIPE[Web Pipelines]
    PIPE --> SCRIPT[Geospatial Scripts]
    SCRIPT --> GUARD[schemaGuards]
    GUARD --> RENDER[Rendering Engines<br/>MapLibre · Cesium]
    RENDER --> UI[Focus Mode · Timeline · Story Nodes]
    UI --> GOVLOG[Governance Telemetry]
```

---

# 🔐 FAIR+CARE Governance Rules (Required)

| Requirement | Implementation |
|------------|----------------|
| No sensitive location exposure | H3 masking + fuzzing + polygon dilation |
| Geometries always redacted before render | `maskCoordinates.ts` mandatory |
| CARE labels stored in metadata.json | Script-level governance metadata |
| User cannot disable CARE masking | Hard-coded in scripts, not toggleable |
| Provenance attached to all outputs | JSON-LD stamping in each script |

Governance ledger:

```
../../../../../docs/reports/audit/web-geospatial-script-ledger.json
```

---

# 📡 Telemetry & Sustainability

Scripts emit:

- `clip_runtime_ms`  
- `masking_events`  
- `projection_hint_used`  
- `blend_compute_ms`  
- Estimated energy & CO₂e (UI event model)  

Telemetry target:

```
../../../../../releases/v10.3.2/focus-telemetry.json
```

---

# ⚙️ CI/CD & MCP-DL Compliance

| Area | Enforcement |
|------|-------------|
| Shape validation | schemaGuards.ts |
| Governance | CARE filters + sovereignty rules |
| Security | CodeQL + Trivy |
| A11y | Accessible spatial interactions verified |
| Telemetry | telemetry-export.yml |
| Docs | docs-lint.yml |
| Behavior determinism | deterministic tests in Jest |

Scripts may **not** be merged if any governance or schema guard fails.

---

# 🧾 Example Script Metadata Entry

```json
{
  "id": "web_geospatial_scripts_v10.3.2",
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
  "timestamp": "2025-11-14T16:32:00Z",
  "governance_ref": "docs/reports/audit/web-geospatial-script-ledger.json"
}
```

---

# 🕰️ Version History

| Version | Date | Summary |
|---------|--------|---------|
| v10.3.2 | 2025-11-14 | Full deep-architecture rebuild; added masking engine, projection hint system, telemetry path upgrades, predictive blending logic. |
| v10.3.1 | 2025-11-13 | Previous version. |

---

<div align="center">

**Kansas Frontier Matrix — Web Geospatial Scripts Layer**  
🛰️ Client-Side Spatial Intelligence · 🌐 FAIR+CARE · 🔐 Ethical Masking · 🔗 Provenance by Design  
© 2025 Kansas Frontier Matrix — MIT License  

[Back to Geospatial Pipelines](../README.md)

</div>
