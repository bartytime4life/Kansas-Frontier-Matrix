---
title: "🧩 Kansas Frontier Matrix — Data Generalization Templates Index"
path: "docs/standards/data-generalization/templates/README.md"
version: "v10.2.2"
last_updated: "2025-11-12"
review_cycle: "Annual / FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../releases/v10.2.0/sbom.spdx.json"
manifest_ref: "../../../../releases/v10.2.0/manifest.zip"
telemetry_ref: "../../../../releases/v10.2.0/focus-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/data-generalization-templates-v1.json"
governance_ref: "../../governance/ROOT-GOVERNANCE.md"
license: "CC BY-NC 4.0"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 🧩 **Kansas Frontier Matrix — Data Generalization Templates Index**
`docs/standards/data-generalization/templates/README.md`

**Purpose:**  
Provide a centralized index of **machine-validated, FAIR+CARE-aligned templates** used for **generalizing sensitive archaeological, cultural, and ecological datasets** within the Kansas Frontier Matrix (KFM).  
These templates ensure reproducibility, ethical compliance, and sovereignty-aligned data handling practices under **MCP-DL v6.3**, **CIDOC CRM**, **DCAT 3.0**, and **FAIR+CARE**.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP_v6.3-blue)](../../../README.md)  
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Governed-orange)](../../faircare.md)  
[![License: CC BY-NC 4.0](https://img.shields.io/badge/License-CC--BY--NC%204.0-green)](../../../../LICENSE)

</div>

---

## 📘 Overview

This directory contains the **official templates** used for:

- Spatial & temporal generalization  
- Metadata declaration for sensitivity levels  
- Sovereignty & CARE compliance blocks  
- Access & restriction statements  
- Masking and grid-aggregation workflows  
- Generalization notices added to dataset manifests  
- STAC/DCAT-compatible generalized dataset descriptors  

All templates are:

- **Version-controlled**  
- **Governance-reviewed**  
- **Telemetry-validated** through `focus-telemetry.json`  
- **Machine-parseable** JSON/Markdown/ YAML structures  

These templates must be used whenever a dataset requires **generalization, masking, suppression, or CARE-derived restrictions**.

---

## 🗂️ Directory Layout

```plaintext
docs/standards/data-generalization/templates/
├── README.md                                   # This file
├── template_generalization_metadata.yaml       # Metadata block for sensitive/generalized datasets
├── template_spatial_masking.json               # Spatial/coordinate masking schema
├── template_temporal_generalization.json       # Temporal aggregation schema
├── template_site_suppression_notice.md         # "Location Withheld" notice template
├── template_care_block.json                    # CARE metadata object for sensitive datasets
├── template_dcat_generalized_dataset.jsonld    # DCAT 3.0 generalized metadata
└── template_generalization_report.md           # Report template for documenting masking decisions
```

---

## 🧾 Template Categories

### 1️⃣ Metadata Templates  
Metadata blocks used in dataset manifests, STAC Items, or DCAT catalogs.

| Template | Purpose |
|----------|----------|
| `template_generalization_metadata.yaml` | Required for all generalized or masked dataset outputs. |
| `template_care_block.json` | CARE ethics + sovereignty metadata block. |
| `template_dcat_generalized_dataset.jsonld` | DCAT-compatible generalized dataset metadata. |

---

### 2️⃣ Spatial Generalization Templates

| Template | Purpose |
|----------|----------|
| `template_spatial_masking.json` | Defines masking algorithm, offsets, and spatial coarsening rules. |
| `template_site_suppression_notice.md` | Template for withholding coordinate precision entirely. |

---

### 3️⃣ Temporal Generalization Templates

| Template | Purpose |
|----------|----------|
| `template_temporal_generalization.json` | Standard schema for date aggregation (decade, century, ranges, rolling periods). |

---

### 4️⃣ Documentation Templates

| Template | Purpose |
|----------|----------|
| `template_generalization_report.md` | Full report of the masking/generalization logic, justification, algorithms used, and CARE approvals. |

---

## 🧩 Example: Generalization Metadata Block (YAML)

```yaml
generalization:
  method: "grid-aggregation"
  spatial_resolution_m: 1000
  temporal_resolution: "10-year-period"
  masking_applied: true
  sensitivity_class: "High"
  authority_to_control: "Prairie Band Potawatomi Nation"
  ethics_statement: "Generalization approved by FAIR+CARE Council."
  review_date: "2025-11-09"
```

---

## 📜 Example: CARE Block (JSON)

```json
{
  "care": {
    "status": "approved",
    "authority_to_control": "Ioway Nation of KS & NE",
    "statement": "Generalization required for publication; full coordinates withheld.",
    "reviewer": "FAIR+CARE Council",
    "date_reviewed": "2025-11-10"
  }
}
```

---

## ⚙️ Governance Integration

All templates in this directory integrate with:

- `faircare-validate.yml` (CARE metadata & ethics rules)  
- `stac-validate.yml` (STAC/DCAT metadata checks)  
- `telemetry-export.yml` (telemetry consolidation)  
- Governance review logs under:  
  ```
  docs/standards/data-generalization/governance/REVIEW_LOGS/
  ```

Using these templates ensures that all generalized datasets:

- Pass automated schema checks  
- Are culturally aligned and sovereignty-aware  
- Produce required governance ledger entries  
- Export correct telemetry signals  

---

## 🧠 When Must These Templates Be Used?

Use these templates **whenever a dataset involves**:

- Tribal cultural heritage  
- Archaeological site features  
- Ecologically sensitive species habitats  
- Sacred or culturally restricted landscapes  
- Confidential land stewardship metadata  
- Historical materials with Indigenous context  
- Treaty or land sovereignty boundaries  

If uncertain, refer dataset to the **FAIR+CARE Council**.

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|--------:|------|--------|---------|
| v10.2.2 | 2025-11-12 | FAIR+CARE Council | Initial template index; aligned to sensitive-site generalization framework; added telemetry schema v1. |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — CC BY-NC 4.0**  
FAIR+CARE Governance · Tribal Sovereignty Compliance · Master Coder Protocol v6.3  
Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[Back to Data Generalization Standard](../README.md) · [Governance Charter](../../governance/ROOT-GOVERNANCE.md)

</div>
