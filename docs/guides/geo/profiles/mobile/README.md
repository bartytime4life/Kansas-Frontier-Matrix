---
title: "📱 Kansas Frontier Matrix — Mobile Rendering Profiles (Performance & Accessibility Benchmarks)"
path: "docs/guides/geo/profiles/mobile/README.md"
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

# 📱 **Kansas Frontier Matrix — Mobile Rendering Profiles**
`docs/guides/geo/profiles/mobile/README.md`

**Purpose:**  
Capture and document **MapLibre GL performance benchmarks** on **mobile and tablet hardware** (Android, iOS, iPadOS).  
Profiles in this directory help evaluate **accessibility**, **energy efficiency**, and **render consistency** under mobile GPU constraints.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP_v6.3-blue)](../../../README.md)
[![License: MIT](https://img.shields.io/badge/License-MIT-green)](../../../../../LICENSE)
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Mobile_Compliance-orange)](../../../../../docs/standards/README.md)
[![Status](https://img.shields.io/badge/Status-Benchmark_Validated-brightgreen)](../../../../../releases/)
</div>

---

## 📘 Overview

This directory contains **mobile render performance profiles** for MapLibre-based layers in the Kansas Frontier Matrix (KFM).  
Each profile represents a benchmark session run under controlled conditions (offline tiles, consistent cache, reduced motion enabled).  
Mobile testing ensures smooth **timeline animations**, **gesture interactions**, and **Focus Mode overlays** on constrained devices.

Profiles are validated via FAIR+CARE-aligned telemetry pipelines and stored for future regression comparison.

---

## 🗂️ Directory Layout

```plaintext
docs/guides/geo/profiles/mobile/
├── README.md                            # This documentation
├── android_pixel7_12z.json              # Android baseline (Pixel 7)
├── ipad_air_10z.json                    # iPad Air (A14 Bionic) profile
└── iphone_13_12z.json                   # Optional iPhone profile
```

---

## ⚙️ Test Environment Summary

| Platform | GPU / Renderer | OS | Browser / Runtime | Cache | Display | Accessibility |
|-----------|----------------|----|-------------------|--------|----------|----------------|
| **Android Pixel 7** | Adreno 730 | Android 14 | Chrome 130 | 512 tiles | 1080×2400 | Prefers reduced motion |
| **iPad Air (A14)** | Apple GPU | iPadOS 18 | Safari WebView | 512 tiles | 1640×2360 | TrueTone + text scaling |
| **iPhone 13** | Apple GPU | iOS 18 | Safari PWA | 512 tiles | 1170×2532 | VoiceOver verified |

All tests run in **offline mode** using **PMTiles** datasets (`roads.pmtiles`, `terrain.pmtiles`) with identical MapLibre GL v3.6.0 configurations.

---

## 🧩 Telemetry Schema Example

```json
{
  "scene": "timeline_overlay_mobile",
  "zoom": 10,
  "hardware": "Android Pixel 7",
  "os": "Android 14",
  "renderer": "Adreno 730 / Vulkan",
  "fps": 57,
  "memoryMB": 275,
  "energy_mWh": 32,
  "accessibility": {
    "reducedMotion": true,
    "textScale": 1.2,
    "colorContrastAA": true
  },
  "frameMetrics": {
    "p50_ms": 15.9,
    "p90_ms": 22.4,
    "p99_ms": 30.7
  },
  "maplibreVersion": "3.6.0",
  "timestamp": "2025-11-09T12:00:00Z"
}
```

> Energy metrics (mWh) are estimated using system telemetry APIs and integrated into KFM’s sustainability tracking.

---

## 📈 Performance Highlights (v10 Baselines)

| Scene | Zoom | Platform | P50 (ms) | P90 (ms) | FPS | Energy (mWh) | Notes |
|--------|------|-----------|----------|----------|-----|---------------|-------|
| Focus Mode Overlay | 12 | Android Pixel 7 | 15.9 | 22.4 | 57 | 32 | Smooth scrolling, minor label thrash |
| Timeline View | 10 | iPad Air (A14) | 14.1 | 21.2 | 59 | 29 | Stable with multiple vector layers |
| Regional Overview | 8 | iPhone 13 | 12.7 | 18.8 | 60 | 28 | Excellent stability, minimal stutter |

---

## 🧮 Benchmark Methodology

1. Use `docs/guides/geo/snippets/benchmark.ts` with preloaded offline tiles.  
2. Run 60-second session (panning, zoom, time-slider motion).  
3. Record FPS, energy (if available), and frame latency metrics.  
4. Save JSON output and compare with desktop baseline.  
5. Upload metrics to CI artifacts → Governance Ledger.  

> Threshold for acceptable variance: **P90 ≤ 25 ms**, **Energy Δ ≤ 10% from baseline**.

---

## ⚖️ FAIR+CARE Integration

| Principle | Implementation | Validation Artifact |
|------------|----------------|--------------------|
| **Findable** | Profiles stored in structured directories | `/profiles/mobile/` |
| **Accessible** | Shared via public repo | `LICENSE` |
| **Interoperable** | JSON schema validation | `geo-profile-validate.yml` |
| **Reusable** | Same test path across devices | `benchmark.ts` |
| **Collective Benefit** | Promotes energy-efficient map design | FAIR+CARE Council audit |
| **Authority to Control** | Accessibility test sign-offs | `ledger/mobile-accessibility.json` |
| **Responsibility** | Sustainability telemetry captured | `focus-telemetry.json` |
| **Ethics** | Device data anonymized | `reports/ledger/mobile.json` |

---

## 🧾 Validation Workflows

| Workflow | Purpose | Key Outputs |
|-----------|----------|-------------|
| `geo-profile-validate.yml` | Schema validation + P90 checks | `reports/geo/mobile-validate.json` |
| `ledger-sync.yml` | FAIR+CARE telemetry + accessibility ledger | `docs/standards/governance/LEDGER/mobile-access.json` |
| `energy-metrics.yml` | Sustainability trace comparison | `reports/energy/mobile-energy-delta.json` |

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|----------|------|--------|----------|
| v10.0.0 | 2025-11-09 | Core Team | Added structured mobile benchmark suite with FAIR+CARE sustainability hooks |
| v9.7.0 | 2025-11-03 | A. Barta | Prototype energy telemetry and mobile performance tracking |

---

<div align="center">

© 2025 Kansas Frontier Matrix Project  
Master Coder Protocol v6.3 · FAIR+CARE Certified · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[Back to Profiles Index](../README.md) · [Governance Charter](../../../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>

