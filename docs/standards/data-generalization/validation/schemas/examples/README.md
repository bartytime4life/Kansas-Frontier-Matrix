---
title: "📁 Kansas Frontier Matrix — Generalization Schema Examples Index"
path: "docs/standards/data-generalization/validation/schemas/examples/README.md"
version: "v10.2.2"
last_updated: "2025-11-12"
review_cycle: "Annual / FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../releases/v10.2.0/sbom.spdx.json"
manifest_ref: "../../../../../releases/v10.2.0/manifest.zip"
telemetry_ref: "../../../../../releases/v10.2.0/focus-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/data-generalization-schema-examples-v1.json"
governance_ref: "../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC BY-NC 4.0"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 📁 **Generalization Schema Examples Index**  
`docs/standards/data-generalization/validation/schemas/examples/README.md`

**Purpose:**  
Provide curated, machine-valid examples for **spatial**, **temporal**, and **CARE governance** generalization schemas used across the Kansas Frontier Matrix (KFM).  
These examples support CI/CD validation, FAIR+CARE auditing, and governance reviews for sensitive-site generalization.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP_v6.3-blue)](../../../../README.md)  
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Validated-orange)](../../../faircare.md)  
[![License](https://img.shields.io/badge/License-CC--BY--NC%204.0-green)](../../../../../LICENSE)  
[![Status](https://img.shields.io/badge/Status-Examples_Complete-brightgreen)]()

</div>

---

## 📘 Overview

This directory provides JSON example payloads demonstrating **correct** and **incorrect** implementations of:

- Spatial generalization  
- Temporal masking  
- CARE governance metadata  
- Full generalization bundles (combined schemas)  

These examples are consumed by:
- `faircare-validate.yml`  
- `stac-validate.yml`  
- `data-generalization` rule validators  
- Governance Council review tooling  
- Automated schema regression tests  

---

## 🗂️ Directory Layout

```plaintext
docs/standards/data-generalization/validation/schemas/examples/
├── README.md                        # This file
├── spatial_valid.json               # Valid spatial generalization example
├── spatial_invalid.json             # Invalid spatial example (CI should reject)
├── temporal_valid.json              # Correct time masking example
├── temporal_invalid.json            # Incorrect temporal precision example
├── care_valid.json                  # Fully compliant CARE metadata example
├── care_invalid.json                # Missing or insufficient ethics metadata
└── bundle_valid.json                # Combined "generalization bundle" example
```

---

## 🧭 Example: Valid Spatial Generalization

```json
{
  "precision": "rounded",
  "coordinates": [38.91, -95.26],
  "method": "coordinate_rounding",
  "resolution_m": 1000,
  "grid": "1km",
  "confidence": 0.92
}
```

---

## ❌ Example: Invalid Spatial Generalization

```json
{
  "precision": "exact",
  "coordinates": [38.912345, -95.258937],
  "method": "none",
  "reason": "FAIL — spatial precision too high for sensitive sites"
}
```

---

## 🕰️ Example: Valid Temporal Masking

```json
{
  "temporal_class": "range",
  "start": "1850-01-01T00:00:00Z",
  "end": "1900-12-31T23:59:59Z",
  "method": "coarse_range",
  "note": "Temporal precision masked for cultural sensitivity."
}
```

---

## ⚠️ Example: Invalid Temporal Masking

```json
{
  "temporal_class": "specific_date",
  "date": "1863-06-04",
  "error": "FAIL — exact ceremony date is not permitted under CARE masking rules."
}
```

---

## 🌱 Example: Valid CARE Metadata Record

```json
{
  "status": "approved",
  "reviewer": "FAIR+CARE Council",
  "statement": "Dataset cleared for generalized public release.",
  "authority_to_control": "Prairie Band Potawatomi Nation",
  "date_reviewed": "2025-11-10",
  "notes": "Generalization methods verified as non-harmful."
}
```

---

## 🚫 Example: Invalid CARE Metadata Record

```json
{
  "status": "approved",
  "error": "Missing authority_to_control and reviewer fields."
}
```

---

## 🧩 Full Generalization Bundle (Valid Example)

```json
{
  "spatial": {
    "precision": "rounded",
    "coordinates": [38.91, -95.26],
    "method": "coordinate_rounding",
    "resolution_m": 1000
  },
  "temporal": {
    "temporal_class": "range",
    "start": "1850-01-01T00:00:00Z",
    "end": "1900-12-31T23:59:59Z"
  },
  "care": {
    "status": "approved",
    "authority_to_control": "Prairie Band Potawatomi Nation",
    "reviewer": "FAIR+CARE Council",
    "date_reviewed": "2025-11-10"
  }
}
```

---

## 🧮 Validation Integration

These examples are tested in:

- `faircare-validate.yml`  
- `stac-validate.yml`  
- `data-generalization` compliance workflows  

Failed examples generate:
- `reports/faircare/generalization_errors.json`
- `ci/logs/schema_failures.log`

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|--------:|------|--------|---------|
| v10.2.2 | 2025-11-12 | FAIR+CARE Council | Added valid/invalid samples for spatial/temporal/CARE/bundle schemas + schema v10 alignment. |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — CC BY-NC 4.0**  
FAIR+CARE Generalization Framework · MCP v6.3  
Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[Back to Schema Index](../README.md) • [Generalization Standards](../../../README.md)

</div>

