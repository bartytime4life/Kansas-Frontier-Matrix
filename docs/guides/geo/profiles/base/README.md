---
title: "🧩 Kansas Frontier Matrix — Baseline MapLibre Rendering Profiles (Reference Hardware)"
path: "docs/guides/geo/profiles/base/README.md"
version: "v10.0.0"
last_updated: "2025-11-09"
review_cycle: "Quarterly / Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../releases/v10.0.0/sbom.spdx.json"
manifest_ref: "../../../../../releases/v10.0.0/manifest.zip"
telemetry_ref: "../../../../../releases/v10.0.0/focus-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/web-render-profiles-v1.json"
governance_ref: "../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "MIT"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 🧩 **Kansas Frontier Matrix — Baseline MapLibre Rendering Profiles**
`docs/guides/geo/profiles/base/README.md`

**Purpose:**  
Document and maintain **reference benchmark results** for MapLibre GL performance on controlled, reproducible hardware environments.  
These baselines provide comparison metrics for validating improvements or regressions across future releases of KFM.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP_v6.3-blue)](../../../README.md)
[![License: MIT](https://img.shields.io/badge/License-MIT-green)](../../../../../LICENSE)
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Active-orange)](../../../../../docs/standards/README.md)
[![Status](https://img.shields.io/badge/Status-Reference_Baseline-brightgreen)](../../../../../releases/)
</div>

---

## 📘 Overview

This directory contains **baseline benchmark profiles** used for performance regression testing of **MapLibre GL rendering** in the Kansas Frontier Matrix.  
Each file represents an official frame-time, tile I/O, and memory profile captured from **reference hardware** under identical test conditions.

These baselines serve as:
- Validation anchors for **CI/CD rendering regression checks**
- Inputs for the **FAIR+CARE Telemetry Ledger**
- Control datasets to measure the efficiency of map rendering optimizations in subsequent versions

---

## 🗂️ Directory Layout

```plaintext
docs/guides/geo/profiles/base/
├── README.md                       # This reference documentation
├── kansas_full_8z.json             # Full state overview benchmark
├── kansas_focus_12z.json           # High-detail Focus Mode profile
└── timeline_overlay_10z.cpuprofile # Timeline overlay CPU trace
```

---

## 🧾 Benchmark Methodology

| Parameter | Value | Description |
|------------|--------|-------------|
| **MapLibre Version** | 3.6.0 | Baseline rendering engine |
| **Dataset** | PMTiles (vector + raster) | Cached offline in `/data/tiles` |
| **Scene** | Kansas (statewide) | 38.5°–40°N, 94°–102°W |
| **Zoom Range** | z = 8, 10, 12 | Common operational zooms |
| **Hardware** | MacBook Pro M1 (16GB RAM) | Official baseline platform |
| **Environment** | Electron & Chromium v128 | Consistent GPU stack |
| **Cache Size** | 1024 tiles | Uniform across runs |
| **Telemetry Mode** | Focus Telemetry (render-perf) | Recorded with FAIR+CARE schema |

All runs are executed with consistent browser/system settings, identical tilesets, and clean caches between trials.

---

## ⚙️ File Schema (Extract)

Each `.json` or `.cpuprofile` adheres to `schemas/telemetry/web-render-profiles-v1.json`:

```json
{
  "scene": "kansas_full",
  "zoom": 8,
  "hardware": "MacBook Pro M1",
  "tileSource": "pmtiles://roads.pmtiles",
  "frameMetrics": {
    "p50_ms": 11.8,
    "p90_ms": 15.6,
    "p99_ms": 21.9
  },
  "memoryMB": 360,
  "fps": 62,
  "maplibreVersion": "3.6.0",
  "timestamp": "2025-11-09T12:00:00Z"
}
```

> All artifacts include SHA-256 hashes and provenance records linked in the governance ledger for reproducibility.

---

## 🧮 Current Baseline Metrics (v10.0.0)

| Scene | Zoom | P50 (ms) | P90 (ms) | P99 (ms) | FPS | Notes |
|--------|------|----------|----------|----------|-----|-------|
| Kansas Full | 8 | 11.8 | 15.6 | 21.9 | 62 | Statewide overview |
| Timeline Overlay | 10 | 13.9 | 18.4 | 23.7 | 60 | Moderate symbol density |
| Focus Mode (Detail) | 12 | 14.7 | 19.2 | 26.3 | 57 | High vector load & labels |

---

## 🧩 FAIR+CARE Telemetry Mapping

| Field | Description | Source |
|-------|--------------|--------|
| `sbom_ref` | Records MapLibre & GPU driver versions | SPDX manifest |
| `telemetry_ref` | Aggregated benchmark metrics | `releases/v10.0.0/focus-telemetry.json` |
| `governance_ref` | Audit & FAIR+CARE compliance | Governance Ledger |
| `maplibreVersion` | Semantic version control for rendering engine | Benchmark metadata |

---

## ⚖️ Governance & Validation

All baseline profiles are validated in CI by `geo-profile-validate.yml`:

- **Schema conformity** → `web-render-profiles-v1.json`
- **Reproducibility** → P90 deviation ≤ ±2.5 ms across reruns
- **Provenance** → SHA-256 match against ledger
- **Ethics audit** → CARE flagging for sacred / sensitive regions

**Governance Ledger Path:**  
`docs/standards/governance/LEDGER/geo-render-baselines-v10.json`

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|----------|------|--------|----------|
| v10.0.0 | 2025-11-09 | Core Team | Established baseline profiles and FAIR+CARE telemetry schema for render benchmarking |
| v9.7.0  | 2025-11-03 | A. Barta | Initial CPU and frame-timing captures for MapLibre optimization testing |

---

<div align="center">

© 2025 Kansas Frontier Matrix Project  
Master Coder Protocol v6.3 · FAIR+CARE Certified · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[Back to Profiles Index](../README.md) · [Governance Charter](../../../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>
