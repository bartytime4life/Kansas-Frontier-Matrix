---
title: "📊 Kansas Frontier Matrix — Rendering Benchmark Reports & FAIR+CARE Telemetry Summaries"
path: "docs/guides/geo/profiles/reports/README.md"
version: "v10.0.0"
last_updated: "2025-11-09"
review_cycle: "Quarterly / Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../releases/v10.0.0/sbom.spdx.json"
manifest_ref: "../../../../../releases/v10.0.0/manifest.zip"
telemetry_ref: "../../../../../releases/v10.0.0/focus-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/web-render-reports-v1.json"
governance_ref: "../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "MIT"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 📊 **Kansas Frontier Matrix — Rendering Benchmark Reports & FAIR+CARE Telemetry Summaries**
`docs/guides/geo/profiles/reports/README.md`

**Purpose:**  
Aggregate and document **MapLibre rendering benchmarks** and **telemetry comparisons** across hardware tiers, software versions, and ethical validation checkpoints.  
These reports synthesize all frame-time, FPS, energy, and accessibility metrics into FAIR+CARE auditable summaries for v10 and later.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP_v6.3-blue)](../../../README.md)
[![License: MIT](https://img.shields.io/badge/License-MIT-green)](../../../../../LICENSE)
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Integrated-orange)](../../../../../docs/standards/README.md)
[![Status](https://img.shields.io/badge/Status-Audited-brightgreen)](../../../../../releases/)
</div>

---

## 📘 Overview

This directory contains **aggregated benchmark reports** automatically generated from the  
`docs/guides/geo/profiles/base/`, `desktop/`, and `mobile/` subdirectories.  
Reports summarize:

- Frame-time performance (P50, P90, P99 ms)  
- Average FPS and GPU utilization  
- Energy efficiency (mWh/session)  
- FAIR+CARE compliance checks (accessibility, sustainability, ethics)  

All data are validated against the **telemetry schema**  
`schemas/telemetry/web-render-reports-v1.json` and cross-linked to the **Governance Ledger**.

---

## 🗂️ Directory Layout

```plaintext
docs/guides/geo/profiles/reports/
├── README.md                          # This documentation
├── summary-table.json                 # Unified report (base + desktop + mobile)
├── deltas-v10-v9.7.json               # Performance delta comparison
├── energy-summary.json                # Aggregated energy consumption
├── accessibility-report.json          # Accessibility test coverage and results
└── faircare-audit.json                # FAIR+CARE compliance artifacts
```

---

## 🧾 Summary Schema Example (`summary-table.json`)

```json
{
  "version": "v10.0.0",
  "generated": "2025-11-09T12:00:00Z",
  "metrics": [
    {
      "scene": "kansas_full",
      "zoom": 8,
      "hardware": "Mac M1 Pro",
      "p50_ms": 11.8,
      "p90_ms": 15.6,
      "p99_ms": 21.9,
      "fps": 62,
      "energy_mWh": 34,
      "device": "desktop"
    },
    {
      "scene": "timeline_overlay",
      "zoom": 10,
      "hardware": "Android Pixel 7",
      "p50_ms": 15.9,
      "p90_ms": 22.4,
      "p99_ms": 30.7,
      "fps": 57,
      "energy_mWh": 32,
      "device": "mobile"
    }
  ],
  "governance": {
    "ledger_entry": "docs/standards/governance/LEDGER/geo-render-v10.json",
    "reviewed_by": ["FAIR+CARE Council", "Core Dev Team"]
  }
}
```

> Each summary includes provenance hashes and versioned ledger entries for transparency.

---

## 🧩 Delta Comparison (`deltas-v10-v9.7.json`)

| Metric | Δ (v10 – v9.7) | Improvement | Notes |
|--------|----------------|--------------|--------|
| **P90 Frame Time** | −1.8 ms | ✅ Faster | Optimized layer ordering |
| **Average FPS** | +3.2 FPS | ✅ Higher | Cache increase to 1024 |
| **Energy Use** | −7 % | ✅ Improved | GPU throttling reduced |
| **Accessibility Score** | +0.1 | ✅ Better | Higher text contrast |

All deltas below ±5 % trigger no action; larger variances are flagged for regression analysis.

---

## ⚙️ Validation Workflows

| Workflow | Purpose | Output Artifact |
|-----------|----------|----------------|
| `geo-profile-validate.yml` | Ensures JSON schema validity across devices | `reports/geo/profile-validation.json` |
| `geo-benchmark.yml` | Aggregates benchmarks + computes deltas | `deltas-v10-v9.7.json` |
| `energy-metrics.yml` | Tracks energy use trends vs prior release | `energy-summary.json` |
| `accessibility-audit.yml` | Verifies WCAG 2.1 AA conformance | `accessibility-report.json` |
| `ledger-sync.yml` | Pushes verified summaries to governance ledger | `faircare-audit.json` |

---

## ⚖️ FAIR+CARE & Governance Mapping

| Principle | Implementation | Evidence |
|------------|----------------|-----------|
| **Findable** | Summary tables published in repo | `summary-table.json` |
| **Accessible** | Public benchmarks open under MIT | Repo visibility |
| **Interoperable** | Schema-based JSON (telemetry v1) | Validation reports |
| **Reusable** | Deltas and profiles archived per release | `releases/v*/` |
| **Collective Benefit** | Transparency in performance & energy metrics | FAIR+CARE report |
| **Authority to Control** | Ledger-approved publication of benchmarks | Governance ledger |
| **Responsibility** | Sustainability telemetry + WCAG audits | `energy-summary.json` |
| **Ethics** | Inclusive performance evaluation for accessibility | `accessibility-report.json` |

---

## 📈 Example FAIR+CARE Audit Extract (`faircare-audit.json`)

```json
{
  "version": "v10.0.0",
  "review_date": "2025-11-09",
  "auditors": ["FAIR+CARE Council"],
  "criteria": {
    "FAIR": "Pass",
    "CARE": "Pass"
  },
  "notes": "Mobile accessibility verified; all datasets meet transparency thresholds."
}
```

---

## 🧮 Interpretation Guidelines

- **P90 < 20 ms** = target achieved for smooth render  
- **Energy ≤ 35 mWh / session** = sustainable threshold (ISO 50001)  
- **Accessibility ≥ 95 % compliance** = passes FAIR+CARE audit  
- **Variance > ±5 %** from baseline = trigger regression workflow  

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|----------|------|--------|----------|
| v10.0.0 | 2025-11-09 | Core Team | Established unified reporting layer with FAIR+CARE and governance ledger sync |
| v9.7.0 | 2025-11-03 | A. Barta | Added JSON summary and delta comparison prototype |

---

<div align="center">

© 2025 Kansas Frontier Matrix Project  
Master Coder Protocol v6.3 · FAIR+CARE Certified · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[Back to Profiles Index](../README.md) · [Governance Charter](../../../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>

