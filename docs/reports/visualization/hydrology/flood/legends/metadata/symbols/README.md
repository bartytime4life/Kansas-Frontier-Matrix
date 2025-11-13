---
title: "🔷 Kansas Frontier Matrix — Flood Symbol Metadata Index (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/reports/visualization/hydrology/flood/legends/metadata/symbols/README.md"
version: "v10.2.0"
last_updated: "2025-11-12"
review_cycle: "Quarterly / FAIR+CARE Visualization Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../../../releases/v10.2.0/sbom.spdx.json"
manifest_ref: "../../../../../../../../releases/v10.2.0/manifest.zip"
telemetry_ref: "../../../../../../../../releases/v10.2.0/focus-telemetry.json"
telemetry_schema: "../../../../../../../../schemas/telemetry/reports-visualization-hydrology-flood-symbols-v1.json"
governance_ref: "../../../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 🔷 **Kansas Frontier Matrix — Flood Symbol Metadata Index**
`docs/reports/visualization/hydrology/flood/legends/metadata/symbols/README.md`

**Purpose:**  
Define the **metadata, accessibility rules, symbolic semantics, and FAIR+CARE governance requirements** for all **flood hazard symbols** used across Kansas Frontier Matrix (KFM) hydrological visualizations.

![Docs](https://img.shields.io/badge/Docs·MCP-v6.3-blue)
![License](https://img.shields.io/badge/License-CC--BY--4.0-green)
![FAIR+CARE](https://img.shields.io/badge/FAIR+CARE-Certified-orange)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

</div>

---

## 📘 Overview

Flood symbol metadata governs the **pictographic and glyph-based elements** used in:
- Flood extent maps  
- Flood velocity and depth symbol overlays  
- Hydrological early-warning diagrams  
- Focus Mode hazard renderings  
- STAC-compliant legend packs  

These symbols must follow:
- **WCAG 2.1 AA contrast rules**  
- **FAIR+CARE visualization ethics**  
- **Consistency across dashboards, maps, and 3D renderers**  
- **MCP-DL v6.3 metadata + provenance requirements**  

---

## 🗂️ Directory Layout

```plaintext
docs/reports/visualization/hydrology/flood/legends/metadata/symbols/
├── README.md
├── symbol_flood_point.json
├── symbol_gauge_station.json
├── symbol_high_water_mark.json
├── symbol_risk_zone.json
└── symbol_warning_icon.json
```

---

## 🧱 Required Metadata Fields

| Field | Description |
|-------|-------------|
| `id` | Unique symbol identifier |
| `title` | Human-readable symbol name |
| `description` | What the symbol conveys |
| `shape` | SVG path or symbolic descriptor |
| `color` | Hex or RGBA, WCAG AA compliant |
| `contrast_rating` | WCAG contrast evaluation |
| `size_px` | Default rendered size |
| `care_status` | CARE classification |
| `stac_item` | Optional STAC legend linkage |
| `checksum_sha256` | Integrity hash |
| `created` | ISO timestamp |
| `commit_sha` | Metadata provenance |

---

## 🧪 Example Symbol Metadata (Gauge Station)

```json
{
  "id": "symbol_gauge_station_v10",
  "title": "USGS Gauge Station Marker",
  "description": "Indicates hydrological monitoring stations used for streamflow and flood assessment.",
  "shape": "M10 2 L14 8 L6 8 Z",
  "color": "#0044BB",
  "contrast_rating": "AA",
  "size_px": 18,
  "care_status": "approved",
  "checksum_sha256": "sha256-3fb2a1e48c6a87f1dde35c88...",
  "created": "2025-11-12T12:40:00Z",
  "commit_sha": "<latest-commit-hash>",
  "stac_item": "kfm-flood-symbols-v10"
}
```

---

## ⚙️ FAIR+CARE Visualization Integration

| Principle | Implementation |
|-----------|----------------|
| **Findable** | Metadata indexed in STAC/DCAT visual catalogs |
| **Accessible** | All symbols published under CC-BY 4.0 |
| **Interoperable** | SVG + JSON-LD ready structures |
| **Reusable** | Linked lineage, checksums, and versioning |
| **CARE** | Avoid misleading symbolization in culturally sensitive regions |

Symbols **must not** imply:
- Exact Indigenous sacred site locations  
- Restricted-access hydrology data not meant for general dissemination  

---

## 🔍 Validation Workflows

| Workflow | Purpose |
|----------|----------|
| `visualization-validate.yml` | Schema + SVG syntax + contrast checks |
| `faircare-validate.yml` | Ethical visualization QA |
| `stac-validate.yml` | Catalog linkage validation |
| `telemetry-export.yml` | Governance & sustainability logging |

All reports written to:
```
reports/self-validation/visualization/symbols/
```

---

## 🧭 Accessibility Requirements

All flood symbols must:
- Maintain WCAG AA contrast on **light and dark basemaps**  
- Be differentiable for **color-blind users**  
- Include alternative text (`aria-label`, STAC `description`)  
- Avoid reliance on color alone — shape encoding required  

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|----------|--------|--------|---------|
| v10.2.0 | 2025-11-12 | Hydrology Visualization Board | Created flood symbol metadata index; aligned with FAIR+CARE, WCAG, SVG standards, and STAC/DCAT conventions. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
Master Coder Protocol v6.3 · FAIR+CARE Certified · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[Back to Flood Legend Metadata](../README.md) · [Visualization Index](../../../../README.md)

</div>

