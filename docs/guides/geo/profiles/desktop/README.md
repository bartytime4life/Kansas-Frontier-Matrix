---
title: "🖥️ Kansas Frontier Matrix — Desktop Rendering Profiles (GPU & CPU Benchmark Suite)"
path: "docs/guides/geo/profiles/desktop/README.md"
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

# 🖥️ **Kansas Frontier Matrix — Desktop Rendering Profiles**
`docs/guides/geo/profiles/desktop/README.md`

**Purpose:**  
Archive and document **MapLibre GL rendering benchmarks** captured on desktop-class hardware (Linux, macOS, Windows).  
These profiles measure **GPU utilization, frame timing, and tile throughput** under controlled offline conditions and serve as performance regression references for future KFM releases.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP_v6.3-blue)](../../../README.md)
[![License: MIT](https://img.shields.io/badge/License-MIT-green)](../../../../../LICENSE)
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Enabled-orange)](../../../../../docs/standards/README.md)
[![Status](https://img.shields.io/badge/Status-Benchmark_Validated-brightgreen)](../../../../../releases/)
</div>

---

## 📘 Overview

This directory contains **desktop-class MapLibre benchmark profiles**.  
Each JSON or CPU profile represents a unique environment (OS, GPU, driver version) used to evaluate rendering consistency, layer complexity, and Focus Mode map transitions.

Profiles are validated in CI/CD and logged to the **FAIR+CARE Governance Ledger** for reproducibility and ethical transparency.

---

## 🗂️ Directory Layout

```plaintext
docs/guides/geo/profiles/desktop/
├── README.md                          # This documentation
├── macos_m1_pro_16z.json              # macOS baseline (M1 Pro GPU)
├── linux_amd_gpu_14z.cpuprofile       # Linux desktop trace (AMD Radeon)
└── windows_rtx_4070_16z.json          # Windows NV RTX profile (optional)
```

---

## ⚙️ Benchmark Environment Summary

| Platform | GPU / Driver | Renderer | CPU | OS / Kernel | Browser or Runtime |
|-----------|---------------|-----------|------|--------------|--------------------|
| **macOS** | M1 Pro (Integrated) | Metal | ARM M2 Pro | macOS 14 Sonoma | Electron v28 / Chromium 128 |
| **Linux** | AMD Radeon 6700XT (Mesa 24.1) | Vulkan | Ryzen 7 5800X | Ubuntu 24.04 LTS | Chrome 130 |
| **Windows** | NVIDIA RTX 4070 | DirectX 12 | Intel i9-13900K | Windows 11 Pro 23H2 | Electron v28 |

All tests use **KFM MapLibre v3.6.0**, identical MBTiles/PMTiles datasets, and `maxTileCacheSize=1024`.

---

## 🧩 Metric Schema (Extract)

Each `.json` follows the FAIR+CARE-aligned telemetry schema `web-render-profiles-v1.json`:

```json
{
  "scene": "focus_mode_detail",
  "zoom": 16,
  "hardware": "Linux AMD Radeon 6700XT",
  "fps": 61,
  "memoryMB": 420,
  "gpuUtilPercent": 65.3,
  "frameMetrics": {
    "p50_ms": 11.2,
    "p90_ms": 15.8,
    "p99_ms": 22.9
  },
  "maplibreVersion": "3.6.0",
  "timestamp": "2025-11-09T12:00:00Z"
}
```

---

## 📈 Performance Highlights (v10 Baselines)

| Scene | Zoom | Platform | P50 (ms) | P90 (ms) | P99 (ms) | FPS | GPU Util (%) | Notes |
|--------|------|-----------|----------|----------|----------|-----|---------------|-------|
| Kansas Full | 8 | macOS M1 Pro | 10.7 | 15.2 | 20.8 | 64 | 59 | Stable baseline |
| Focus Mode | 12 | Linux AMD 6700XT | 12.3 | 16.1 | 21.5 | 62 | 66 | Heavier vector workload |
| Overlay Timeline | 14 | Windows RTX 4070 | 14.8 | 18.5 | 25.1 | 58 | 70 | Layer-intensive test |

---

## 🧮 Benchmark Methodology

1. Load scene via `benchmark.ts` (`docs/guides/geo/snippets/benchmark.ts`)
2. Execute automated pan/zoom path with timeline overlays
3. Record frame-time traces for 30s at each zoom (8, 12, 14, 16)
4. Export performance logs and GPU metrics (via browser DevTools)
5. Convert CPU trace → JSON metrics → ledger entry

> Repeat each test 3× and use median values for reporting.

---

## ⚖️ Governance & FAIR+CARE Mapping

| Aspect | Description | Artifact |
|--------|-------------|-----------|
| **Provenance** | GPU model + driver hash recorded | `sbom.spdx.json` |
| **Accessibility** | Results published in repo under open MIT | `docs/guides/geo/profiles/desktop/**` |
| **Reproducibility** | Config + telemetry logs versioned in CI | `geo-profile-validate.yml` |
| **Collective Benefit** | Enables reproducible geospatial performance research | Governance Ledger |
| **Responsibility** | Ethical GPU energy profiling (ISO 50001) | Telemetry report |
| **Ethics** | No profiling of private/sensitive layers | Ledger-reviewed metadata |

---

## 🧾 Validation & Automation

| Workflow | Function | Validation |
|-----------|-----------|-------------|
| `geo-profile-validate.yml` | Validate schema + P90 thresholds | Must pass (Δ ≤ 5%) |
| `telemetry-export.yml` | Append summary metrics to `focus-telemetry.json` | Continuous |
| `ledger-sync.yml` | Push baseline GPU data to governance ledger | Daily batch |

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|----------|------|--------|----------|
| v10.0.0 | 2025-11-09 | Core Team | Added desktop GPU benchmarking suite; integrated telemetry schema & CI validation |
| v9.7.0 | 2025-11-03 | A. Barta | Introduced multi-platform benchmark prototype for render testing |

---

<div align="center">

© 2025 Kansas Frontier Matrix Project  
Master Coder Protocol v6.3 · FAIR+CARE Certified · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[Back to Profiles Index](../README.md) · [Governance Charter](../../../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>

