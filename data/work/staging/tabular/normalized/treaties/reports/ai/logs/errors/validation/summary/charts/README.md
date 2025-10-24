---
title: "📈 Kansas Frontier Matrix — AI Error Validation Charts"
path: "data/work/staging/tabular/normalized/treaties/reports/ai/logs/errors/validation/summary/charts/README.md"
version: "v1.0.0"
last_updated: "2025-10-24"
review_cycle: "Continuous / Automated"
status: "Active · FAIR+CARE+ISO Visualized"
mcp_version: "MCP-DL v6.4.3"
maintainers: ["@kfm-validation", "@kfm-ai", "@kfm-observability"]
approvers: ["@kfm-architecture", "@kfm-governance", "@kfm-accessibility"]
license: ["MIT (code)", "CC-BY 4.0 (data/docs)"]
alignment:
  - FAIR / CARE
  - STAC / DCAT
  - CIDOC CRM / PROV-O / OWL-Time
  - ISO 9001 / 27001 / 50001 / 14064
tags: ["ai","errors","validation","charts","visualization","observability","wcag","telemetry","governance"]
---

<div align="center">

# 📈 Kansas Frontier Matrix — **AI Error Validation Charts**  
`data/work/staging/tabular/normalized/treaties/reports/ai/logs/errors/validation/summary/charts/`

**Purpose:** Store **rendered charts** and **exported datasets** that visualize error-log validation results (pass rates, severity mix, trend lines, governance sync) for treaty-report pipelines. All visuals are **audit-ready**, **accessible (WCAG 2.1 AA)**, and **provenance-linked**.

[![Docs · MCP-DL v6.4.3](https://img.shields.io/badge/Docs-MCP--DL%20v6.4.3-blue)]()
[![Validation Charts](https://img.shields.io/badge/Validation-Charts%20%26%20Datasets-6f42c1)]()
[![FAIR+CARE](https://img.shields.io/badge/FAIR%20%2B%20CARE-Visualized-2ecc71)]()
[![ISO](https://img.shields.io/badge/ISO-9001%20%7C%202701%20%7C%2050001%20%7C%2014064-229954)]()

</div>

---

## 📚 Overview

This directory is the **visual layer** of error validation summaries. It houses:
- **Static images** (PNG/SVG) of charts used in READMEs and dashboards,
- **Source datasets** (CSV/JSON) used to render the charts,
- **Alt-text metadata** for accessibility,
- **Provenance** and **checksum** files to ensure integrity and reproducibility.

> **Note:** Every chart must have a **matching dataset** and an **alt-text description**.

---

## 🗂️ Directory Layout

```
data/work/staging/tabular/normalized/treaties/reports/ai/logs/errors/validation/summary/charts/
├── data/                             # Source data used to render charts
│   ├── error_trend_YYYY-MM.csv
│   ├── severity_breakdown_YYYY-MM.csv
│   └── validation_success_rate.csv
├── images/                           # Exported charts (PNG/SVG)
│   ├── error_trend_YYYY-MM.png
│   ├── severity_breakdown_YYYY-MM.png
│   └── validation_success_rate.png
├── alt/                              # Accessibility text for each chart
│   ├── error_trend_YYYY-MM.alt.txt
│   ├── severity_breakdown_YYYY-MM.alt.txt
│   └── validation_success_rate.alt.txt
├── provenance/                       # JSON-LD provenance & checksum manifests
│   ├── charts_provenance.jsonld
│   └── checksums.sha256
└── specs/                            # Rendering specs / chart configs
    ├── error_trend.spec.json
    ├── severity_breakdown.spec.json
    └── validation_success_rate.spec.json
```

---

## 🎨 Chart Specifications

| Chart | File (img) | Data (src) | Encodings | Purpose |
| :---- | :--------- | :--------- | :-------- | :------ |
| Error Trend | `images/error_trend_YYYY-MM.png` | `data/error_trend_YYYY-MM.csv` | X: date, Y: validations, line | Rolling count of validations and errors |
| Severity Breakdown | `images/severity_breakdown_YYYY-MM.png` | `data/severity_breakdown_YYYY-MM.csv` | X: severity, Y: count, bars | Distribution of error severities |
| Validation Success Rate | `images/validation_success_rate.png` | `data/validation_success_rate.csv` | X: date, Y: pass %, line | Pass/fail rate over time |

**Rendering rules**
- Font: system default; size ≥ 12px in images.  
- Axes labeled; units included (%, counts).  
- Legend required if ≥2 series.  
- Colors: high-contrast, color-blind safe palette.  
- Titles concise; subtitles optional for context.

---

## ♿ Accessibility (WCAG 2.1 AA)

- Provide **alt text** in `/alt/*.alt.txt` for each image.  
- Ensure contrast ratio ≥ 4.5:1 for text overlays.  
- Avoid color-only encodings; use shapes/markers for multi-series lines.  
- Include **data table** (CSV) to support non-visual analysis.

---

## 🧩 Example Datasets

**`data/error_trend_2025-10.csv`**
```csv
date,validations,errors,critical,major,minor
2025-10-01,218,3,1,1,1
2025-10-08,231,2,0,1,1
2025-10-15,244,2,0,1,1
2025-10-22,260,1,0,0,1
```

**`data/validation_success_rate.csv`**
```csv
date,pass_rate_pct
2025-10-01,98.7
2025-10-08,99.2
2025-10-15,99.5
2025-10-22,99.6
```

**`data/severity_breakdown_2025-10.csv`**
```csv
severity,count
critical,2
major,5
minor,8
```

---

## 🧪 Rendering Workflow

```mermaid
flowchart TD
    A[Summary JSON/CSV] --> B[Chart Spec (specs/*.spec.json)]
    B --> C[Renderer (CLI/Notebook)]
    C --> D[PNG/SVG Export (images/)]
    C --> E[Alt Text (alt/)]
    A --> F[Provenance + Checksums]
    D --> F
    E --> F
```

---

## ⚙️ Chart Spec Schema (Excerpt)

```json
{
  "chart_id": "error_trend_2025-10",
  "title": "AI Error Validation — Trend (Oct 2025)",
  "data": "data/error_trend_2025-10.csv",
  "encoding": {
    "x": {"field": "date", "type": "temporal"},
    "y": {"field": "validations", "type": "quantitative"},
    "y2": {"field": "errors", "type": "quantitative", "optional": true}
  },
  "export": {"format": "png", "dpi": 192, "width": 1280, "height": 720},
  "a11y": {"alt_text": "Line chart showing weekly validations increasing and errors decreasing through Oct 2025."}
}
```

---

## 🔐 Integrity & Provenance

- All artifacts hashed via SHA-256 and recorded in `provenance/checksums.sha256`.  
- A JSON-LD provenance record (`provenance/charts_provenance.jsonld`) links:  
  - **Source summaries** → `../validation_summary_*.json`  
  - **Specs** → `specs/*.spec.json`  
  - **Outputs** → `images/*.png`  
  - **Alt text** → `alt/*.alt.txt`  
- CI blocks merge if any artifact is missing or checksum fails.

---

## 📊 Quality Gates

| Gate | Requirement | Enforced By |
| :--- | :---------- | :---------- |
| Data present | CSV/JSON dataset exists for each image | docs-validate |
| Alt text | `.alt.txt` per image | a11y-check |
| Checksums | SHA-256 match for all artifacts | checksum-verify |
| Provenance | JSON-LD links resolve | pyshacl |
| Readability | Axis labels + ≥12px text | chart-lint |

---

## ✅ Compliance Matrix

| Standard | Scope | Status |
| :-------- | :---- | :----- |
| **FAIR+CARE** | Discoverability & ethics | ✅ |
| **MCP-DL v6.4.3** | Docs-as-Code visuals | ✅ |
| **WCAG 2.1 AA** | Accessibility of images | ✅ |
| **ISO 9001 / 27001** | Quality & security | ✅ |
| **ISO 50001 / 14064** | Energy & carbon metrics | ✅ |
| **STAC/DCAT** | Dataset descriptors | ✅ |

---

## 🗓️ Version History

| Version | Date | Changes | Author |
| :------ | :---- | :------ | :----- |
| v1.0.0 | 2025-10-24 | Initial charts module with data/specs/alt/provenance structure. | @kfm-validation |

---

<div align="center">

[![Validation Charts](https://img.shields.io/badge/Validation-Charts-6f42c1?style=flat-square)]()
[![WCAG 2.1 AA](https://img.shields.io/badge/Accessibility-WCAG%202.1%20AA-1f6feb?style=flat-square)]()
[![FAIR%20%26%20CARE](https://img.shields.io/badge/FAIR%20%26%20CARE-Compliant-2ecc71?style=flat-square)]()
[![Provenance](https://img.shields.io/badge/Provenance-CIDOC%20CRM%20%7C%20PROV--O-8a2be2?style=flat-square)]()
[![ISO](https://img.shields.io/badge/ISO-9001%20%7C%202701%20%7C%2050001%20%7C%2014064-229954?style=flat-square)]()

</div>

<!-- MCP-FOOTER-BEGIN
MCP-VERSION: v6.4.3
MCP-TIER: Silver · Validation Charts
DOC-PATH: data/work/staging/tabular/normalized/treaties/reports/ai/logs/errors/validation/summary/charts/README.md
MCP-CERTIFIED: true
FAIR-CARE-COMPLIANT: true
WCAG-ALIGNED: true
DATA-LINKED: true
PROVENANCE-RECORDED: true
CHECKSUM-VERIFIED: true
GOVERNANCE-LEDGER-LINKED: true
GENERATED-BY: KFM-Automation/DocsBot
LAST-VALIDATED: 2025-10-24
MCP-FOOTER-END -->