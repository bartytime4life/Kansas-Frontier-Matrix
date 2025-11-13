---
title: "📘 Kansas Frontier Matrix — Generalization Report Template"
path: "docs/standards/data-generalization/templates/template_generalization_report.md"
version: "v10.2.2"
last_updated: "2025-11-12"
review_cycle: "Annual / FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../releases/v10.2.0/sbom.spdx.json"
manifest_ref: "../../../../releases/v10.2.0/manifest.zip"
telemetry_ref: "../../../../releases/v10.2.0/focus-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/data-generalization-report-v1.json"
governance_ref: "../../governance/ROOT-GOVERNANCE.md"
license: "CC BY-NC 4.0"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 📘 **Generalization Report Template — Sensitive & CARE-Governed Data**
`docs/standards/data-generalization/templates/template_generalization_report.md`

**Purpose:**  
Provide a **FAIR+CARE-aligned, reproducible, machine-validatable** template for documenting **spatial/temporal generalization decisions**, required governance approvals, masking algorithms, and cultural/ethical rationale applied to sensitive or sovereignty-protected datasets.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP_v6.3-blue)](../../../README.md)  
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Governed-orange)](../../faircare.md)  
[![License: CC BY-NC 4.0](https://img.shields.io/badge/License-CC--BY--NC%204.0-green)](../../../../LICENSE)

</div>

---

## 📘 Overview

This report template is required for **any dataset** whose spatial, temporal, or cultural sensitivity necessitates **generalization, masking, suppression, or CARE-restricted handling**.  
It is automatically validated by:

- `faircare-validate.yml` (ethics & CARE rules)  
- `stac-validate.yml` (metadata conformance)  
- `telemetry-export.yml` (energy + governance metrics)  
- Governance ledger integrations under:  
  ```
  docs/standards/data-generalization/governance/REVIEW_LOGS/
  ```

All completed reports must be stored under:

```
data/processed/generalization_reports/<dataset_id>.md
```

---

## 🧱 1. Dataset Metadata

```yaml
dataset_id: "<dataset-identifier>"
dataset_title: "<human-readable title>"
source_provenance: "<original provider / institution>"
license: "<SPDX ID or CC license>"
sensitivity_class: "<Low | Medium | High>"
care_status: "<approved | restricted | revision>"
authority_to_control: "<community / tribe / council>"
report_author: "<name + affiliation>"
report_date: "YYYY-MM-DD"
```

---

## 🎯 2. Purpose of Generalization

Explain **why** masking/generalization was required.

- Cultural protection  
- Ecological risk  
- Archaeological sensitivity  
- Legal/MOU restrictions  
- Community request  
- Tribal sovereignty requirements  

> _Example_:  
> High-resolution site coordinates risk exposing sacred burial mound locations; dataset must be generalized to prevent disturbance or unauthorized access.

---

## 🧭 3. Original Data Characteristics

| Property | Description |
|----------|-------------|
| Spatial precision | e.g., ±1m GNSS, digitized coordinates, inferred |
| Temporal precision | e.g., exact dates, ranges, uncertain periods |
| Feature types | points, polygons, rasters, site attributes |
| Cultural context | Indigenous, archaeological, ecological |
| Consent / agreements | Links to MOU or CARE agreements |

---

## ⚙️ 4. Generalization Methods Applied

Describe each transformation in detail.

### 4.1 Spatial Generalization

| Method | Applied | Parameters | Notes |
|--------|---------|------------|-------|
| Coordinate rounding | yes/no | precision (e.g., 2 decimals) | — |
| Grid aggregation | yes/no | cell size (e.g., 1 km) | — |
| Random offset masking | yes/no | ± distance | seed logged |
| Site suppression | yes/no | reason | “location withheld” |
| Geometry replacement | yes/no | centroids / hulls | — |

**JSON Example**
```json
{
  "spatial_generalization": {
    "method": "grid-aggregation",
    "resolution_m": 1000,
    "masking_offset_m": 0,
    "site_suppression": false
  }
}
```

---

### 4.2 Temporal Generalization

| Method | Applied | Parameters |
|--------|---------|------------|
| Year-binning | yes/no | 5/10/25-year bins |
| Decade aggregation | yes/no | "1870s" |
| Century aggregation | yes/no | 1800–1900 |
| Suppression | yes/no | "Date withheld" |

**JSON Example**
```json
{
  "temporal_generalization": {
    "method": "decade",
    "range": "1870s"
  }
}
```

---

## 🧩 5. Ethical & CARE Review Summary

### 5.1 CARE Review Details

```yaml
care_review:
  status: "<approved | restricted | revision>"
  reviewer: "<council or tribal authority>"
  review_date: "YYYY-MM-DD"
  notes: "<ethics notes>"
```

### 5.2 Community / Tribal Consultation Notes

- Names or departments consulted  
- MOU references  
- Conditions for publication  
- Review cycle expectations  

---

## 🔐 6. Access Restrictions & Publication Controls

| Policy | Requirement |
|--------|-------------|
| Access level | public / restricted / council-only |
| License constraints | CC BY-NC / MOU-defined |
| Required notices | land acknowledgment, cultural context |
| Distribution notes | masking must be preserved; no reverse-engineering |

---

## 🧮 7. Validation & Governance Artifacts

Attach or reference:

- `faircare_summary.json`
- `provenance_trace.json`
- Generalization workflow logs  
- CARE approval form  
- Any MOU or sovereign-use document  
- STAC/DCAT metadata for the **generalized** dataset  
- Telemetry entry from `focus-telemetry.json`

---

## 📊 8. Generalization Impact Assessment

Describe **how the masking affected**:

- Spatial accuracy  
- Analytical usefulness  
- Scientific validity  
- Cultural protections  
- Ecological risk mitigation  
- Public value  

Optionally include maps or statistical comparisons.

---

## 🏁 9. Final Generalized Dataset Description

Provide an explicit dataset metadata block:

```yaml
generalized_dataset:
  id: "<dataset-id-generalized>"
  spatial_resolution_m: 1000
  temporal_resolution: "10-year"
  masking_applied: true
  justification: "<summary>"
  license: "<license>"
  care_status: "<approved>"
```

If publishing STAC/DCAT metadata, include link:

```
data/stac/generalized/<dataset-id>.json
```

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|--------:|------|--------|--------|
| v10.2.2 | 2025-11-12 | FAIR+CARE Council | Initial release of generalization documentation template; aligned to v10 sensitive-site governance policies. |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — CC BY-NC 4.0**  
FAIR+CARE Sovereignty Governance · Cultural Protection · MCP v6.3  
Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[Back to Template Index](README.md) · [Generalization Standard](../README.md)

</div>

