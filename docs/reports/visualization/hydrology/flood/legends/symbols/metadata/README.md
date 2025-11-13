---
title: "🗂️ Kansas Frontier Matrix — Flood Symbol Metadata Registry (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/reports/visualization/hydrology/flood/legends/symbols/metadata/README.md"
version: "v10.2.0"
last_updated: "2025-11-12"
review_cycle: "Quarterly / FAIR+CARE Visualization Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../../../releases/v10.2.0/sbom.spdx.json"
manifest_ref: "../../../../../../../../releases/v10.2.0/manifest.zip"
telemetry_ref: "../../../../../../../../releases/v10.2.0/focus-telemetry.json"
telemetry_schema: "../../../../../../../../schemas/telemetry/reports-visualization-hydrology-flood-symbols-metadata-v1.json"
governance_ref: "../../../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 🗂️ **Kansas Frontier Matrix — Flood Symbol Metadata Registry**  
`docs/reports/visualization/hydrology/flood/legends/symbols/metadata/README.md`

**Purpose:**  
Provide the **machine-readable metadata registry** for all hydrological flood legend symbols used across Kansas Frontier Matrix (KFM) visualization workflows.  
Each symbol metadata file documents provenance, accessibility scores, FAIR+CARE ethics results, checksum integrity, and STAC/DCAT interoperability.

![Docs](https://img.shields.io/badge/Docs·MCP-v6.3-blue)
![License](https://img.shields.io/badge/License-CC--BY%204.0-green)
![FAIR+CARE](https://img.shields.io/badge/FAIR+CARE-Certified-orange)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

</div>

---

## 📘 Overview

This directory contains **JSON metadata files** describing each flood symbol defined under:

```
docs/reports/visualization/hydrology/flood/legends/symbols/
```

Symbols include:
- Major flood markers  
- Minor flood markers  
- Flash flood indicators  
- Levee failure icons  
- Inundation boundary linework  

Each metadata file undergoes:
- **Checksum validation** (SHA-256)  
- **FAIR+CARE ethics auditing**  
- **WCAG 2.1 AA accessibility scoring**  
- **STAC/DCAT registry mapping**  
- **Sustainability & telemetry logging**

---

## 🗂️ Directory Layout

```plaintext
docs/reports/visualization/hydrology/flood/legends/symbols/metadata/
├── README.md                          # This file
├── flood_marker_major.json
├── flood_marker_minor.json
├── flood_marker_flash.json
├── levee_failure_icon.json
└── inundation_boundary.json
```

---

## 🧩 Required Metadata Fields

| Field | Description | Required |
|------|-------------|---------|
| `id` | Unique symbol identifier | ✅ |
| `title` | Human-readable name | ✅ |
| `symbol_type` | `point` / `line` / `polygon` / `annotation` | ✅ |
| `description` | Purpose & semantic meaning | ✅ |
| `color_profile` | Hex codes + WCAG contrast rating | ⚙️ |
| `shape_description` | Shape semantics & intended meaning | ⚙️ |
| `checksum_sha256` | Integrity hash of symbol file | ⚙️ |
| `accessibility_score` | 0–1 rating based on accessibility tests | ✅ |
| `care_status` | `approved` / `restricted` | ⚙️ |
| `created` | ISO timestamp | ✅ |
| `commit_sha` | Symbol provenance | ⚙️ |
| `stac_item` | Linked STAC Item ID | ⚙️ |

---

## 🧾 Example Metadata Entry (Flash Flood Symbol)

```json
{
  "id": "symbol_flash_flood_v10",
  "title": "Flash Flood Indicator",
  "symbol_type": "point",
  "description": "Represents rapid-onset flood events with high damage potential.",
  "color_profile": {
    "fill": "#B00020",
    "stroke": "#FFFFFF",
    "wcag_contrast_ratio": 5.2
  },
  "shape_description": "Triangle with bold outline for high visibility under emergency contexts.",
  "checksum_sha256": "sha256-12ab34cd56ef7890...",
  "care_status": "approved",
  "accessibility_score": 0.97,
  "created": "2025-11-12T12:20:00Z",
  "commit_sha": "<latest-commit-hash>",
  "stac_item": "kfm-flood-symbols-v10"
}
```

---

## ⚙️ FAIR+CARE Verification

Symbol metadata must pass FAIR+CARE governance checks:

| Principle | Validation Requirement |
|----------|-------------------------|
| **Findable** | STAC/DCAT mapped metadata with stable IDs |
| **Accessible** | CC-BY license, public symbol distribution |
| **Interoperable** | JSON-LD compatible metadata |
| **Reusable** | Versioned metadata with provenance & checksums |
| **CARE** | No culturally sensitive meaning embedded in symbols |

---

## 🧪 Validation Pipelines

| Workflow | Purpose | Output |
|----------|----------|---------|
| `visualization-validate.yml` | Checks metadata completeness, contrast scores | `metadata_validation.json` |
| `faircare-validate.yml` | CARE compliance audit | `symbol_care_audit.json` |
| `stac-validate.yml` | STAC/DCAT mapping verification | `stac_validation.json` |
| `telemetry-export.yml` | Logs events & sustainability metrics | `focus-telemetry.json` |

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|---------|------|---------|---------|
| v10.2.0 | 2025-11-12 | Hydrology Visualization Board | Initial metadata registry created for flood legend symbols. |

---

<div align="center">

© 2025 Kansas Frontier Matrix · CC-BY 4.0  
Master Coder Protocol v6.3 · FAIR+CARE Certified  
Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[Back to Symbol Legends](../README.md) · [Visualization Index](../../../../README.md)

</div>

