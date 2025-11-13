---
title: "🗂️ Kansas Frontier Matrix — Flood Legend Colorbar Metadata Registry (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/reports/visualization/hydrology/flood/legends/colorbars/metadata/README.md"
version: "v10.2.0"
last_updated: "2025-11-12"
review_cycle: "Quarterly / FAIR+CARE Visualization Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../../releases/v10.2.0/sbom.spdx.json"
manifest_ref: "../../../../../../../releases/v10.2.0/manifest.zip"
telemetry_ref: "../../../../../../../releases/v10.2.0/focus-telemetry.json"
telemetry_schema: "../../../../../../../schemas/telemetry/reports-visualization-hydrology-flood-colorbars-v1.json"
governance_ref: "../../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 🗂️ **Flood Legend Colorbar Metadata Registry**  
`docs/reports/visualization/hydrology/flood/legends/colorbars/metadata/README.md`

**Purpose:**  
Define and maintain the **metadata registry** for all flood-layer colorbars used in Kansas Frontier Matrix (KFM) hydrology visualizations.  
Ensures that every legend is **FAIR+CARE-aligned**, **WCAG 2.1 AA accessible**, and **STAC/DCAT-registered** for provenance, reproducibility, and ethical visualization governance.

![Docs MCP](https://img.shields.io/badge/Docs·MCP-v6.3-blue)
![License](https://img.shields.io/badge/License-CC--BY--4.0-green)
![FAIR+CARE](https://img.shields.io/badge/FAIR+CARE-Certified-orange)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

</div>

---

## 📘 Overview

This registry documents the **metadata JSON records** for every hydrology flood visualization colorbar.  
Each metadata file includes:
- Provenance & lineage  
- Accessibility scoring  
- CARE sensitivity classification  
- Dataset linkage (which maps/animations use the colorbar)  
- STAC/DCAT reference metadata  
- Versioning and checksum integrity  

These metadata artifacts guarantee that flood visualizations remain **consistent, ethically governed, and reproducible** across KFM releases.

---

## 🗂️ Directory Layout

```plaintext
docs/reports/visualization/hydrology/flood/legends/colorbars/metadata/
├── README.md                                 # This file
├── flood_depth_viridis.json                  # Depth ramp metadata (0–6m)
├── flood_depth_cividis.json                  # Cividis depth alternative
├── flood_severity_cb.json                    # Colorblind-safe severity scale
├── recurrence_heatmap.json                   # Recurrence interval ramp
└── uncertainty_bluepurple.json               # Confidence/uncertainty ramp
```

---

## 🧩 Required Metadata Fields (Per Colorbar)

| Field | Description | Required |
|--------|-------------|----------|
| `id` | Unique colorbar identifier | ✅ |
| `title` | Human-readable legend name | ✅ |
| `type` | Must be `"colorbar"` | ✅ |
| `description` | What the gradient encodes | ✅ |
| `license` | SPDX/CC license identifier | ✅ |
| `stac_item` | Linked STAC Item ID | ⚙️ |
| `accessibility_score` | WCAG 2.1 AA color contrast score (0–1) | ✅ |
| `care_status` | `approved` / `restricted` | ⚙️ |
| `created` | ISO timestamp | ✅ |
| `commit_sha` | Provenance of generation | ⚙️ |
| `used_in` | Array of visualizations referencing this colorbar | ⚙️ |
| `checksum_sha256` | Integrity protection | ⚙️ |

---

## 📊 Example Metadata Record (Depth Legend)

```json
{
  "id": "legend_flood_depth_viridis_v10",
  "title": "Flood Depth (Viridis) – 0–6m",
  "type": "colorbar",
  "description": "A perceptually uniform, colorblind-safe depth gradient for Kansas hydrology maps.",
  "license": "CC-BY-4.0",
  "accessibility_score": 0.99,
  "care_status": "approved",
  "created": "2025-11-12T12:00:00Z",
  "commit_sha": "<latest-commit-hash>",
  "checksum_sha256": "sha256-abc123...def456",
  "used_in": [
    "kfm_flood_depth_2025_v10",
    "kfm_hydrology_composite_depth_v10"
  ],
  "stac_item": "kfm-flood-depth-colorbars-v10"
}
```

---

## ⚙️ Validation Workflows

| Workflow | Purpose | Output |
|----------|----------|---------|
| `visualization-validate.yml` | Validates metadata completeness & schema conformance | `reports/visualization/metadata_validation.json` |
| `faircare-validate.yml` | Ensures colorbar ethics and sensitivity alignment | `reports/faircare/colorbar_faircare.json` |
| `stac-validate.yml` | Confirms STAC/DCAT compliance for legend assets | `reports/stac_validation.json` |
| `telemetry-export.yml` | Logs sustainability & governance metrics | `focus-telemetry.json` |

---

## 🎨 Metadata Quality Requirements

- **Colorblind Safe:** Must pass CB-Safe palette validation.  
- **Contrast Verified:** WCAG AA contrast ratio ≥ 4.5:1 between critical steps.  
- **Ethical Masking:** Color schemes must not radiometrically expose sensitive tribal or archaeological features.  
- **Stable IDs:** All colorbars are versioned (e.g., `_v10`, `_v10.1`).  
- **Checksum Integrity:** All metadata files must include SHA-256 values.

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|---------|------|---------|---------|
| v10.2.0 | 2025-11-12 | Hydrology Visualization Board | Created metadata registry for flood colorbars with FAIR+CARE + STAC integration. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
Master Coder Protocol v6.3 · FAIR+CARE Certified · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[Back to Colorbars Index](../README.md) · [Flood Legends](../../README.md)

</div>

