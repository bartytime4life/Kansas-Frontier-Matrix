---
title: "📊 Kansas Frontier Matrix — Generalization Validation Reports Index"
path: "docs/standards/data-generalization/validation/reports/README.md"
version: "v10.2.2"
last_updated: "2025-11-12"
review_cycle: "Annual / FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../releases/v10.2.0/sbom.spdx.json"
manifest_ref: "../../../../../releases/v10.2.0/manifest.zip"
telemetry_ref: "../../../../../releases/v10.2.0/focus-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/data-generalization-validation-reports-v1.json"
governance_ref: "../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC BY-NC 4.0"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 📊 **Generalization Validation Reports Index**  
`docs/standards/data-generalization/validation/reports/README.md`

**Purpose:**  
Provide the authoritative index for all **generalization validation reports**, including spatial, temporal, and CARE-related compliance audits for sensitive cultural and archaeological datasets within the Kansas Frontier Matrix (KFM).  
These reports document **automated validation**, **manual FAIR+CARE review**, and **Council decisions**, forming part of the governed provenance chain.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP_v6.3-blue)](../../../../README.md)  
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Certified-orange)](../../../faircare.md)  
[![License: CC BY-NC 4.0](https://img.shields.io/badge/License-CC--BY--NC%204.0-green)](../../../../../LICENSE)  
[![Status](https://img.shields.io/badge/Status-Reports_Indexed-brightgreen)]()

</div>

---

## 📘 Overview

This directory aggregates all **validation outputs** generated during the generalization compliance pipeline.  
These artifacts are inspected by the FAIR+CARE Council and referenced in release manifests, provenance ledgers, and quarterly audits.

Validation covers:
- Spatial masking & coordinate generalization  
- Temporal aggregation & precision reduction  
- CARE ethical metadata completeness & sovereignty compliance  
- Combined “generalization bundles” (spatial + temporal + CARE)  
- Manual review overrides and governance notes

Reports are used by:
- `faircare-validate.yml`  
- `stac-validate.yml`  
- `telemetry-export.yml`  
- KFM Governance Dashboard  
- Indigenous data partner review portals

---

## 🗂️ Directory Layout

```plaintext
docs/standards/data-generalization/validation/reports/
├── README.md                            # This file
├── spatial_validation.json              # CI-generated spatial compliance results
├── temporal_validation.json             # Temporal masking audit results
├── care_validation.json                 # CARE metadata validation report
├── bundle_validation.json               # Combined bundle audit results
├── manual_review_notes.md               # Human review notes from FAIR+CARE Council
└── error_logs/                          # Raw stderr/stdout CI logs for debugging
```

---

## 🧪 Validation Output Types

### 1️⃣ Spatial Validation  
Ensures that coordinates have been generalized using approved techniques and minimum-resolution rules.

**Example excerpt**
```json
{
  "dataset_id": "kfm-sensitive-site-15",
  "status": "passed",
  "method": "coordinate_rounding",
  "resolution_m": 1000,
  "violations": []
}
```

---

### 2️⃣ Temporal Validation  
Confirms removal of sensitive dates (ceremonial, burial, restricted events).

**Example excerpt**
```json
{
  "dataset_id": "kfm-archival-ceremony-009",
  "status": "warning",
  "issue": "Temporal window too narrow",
  "recommended_range": "≥ 20 years"
}
```

---

### 3️⃣ CARE Metadata Validation  
Audits cultural sovereignty and consent fields.

**Example excerpt**
```json
{
  "care_status": "approved",
  "authority_to_control": "Prairie Band Potawatomi Nation",
  "reviewer": "FAIR+CARE Council",
  "missing_fields": []
}
```

---

### 4️⃣ Bundle-Level Validation  
Verifies alignment between spatial, temporal, and CARE components as a unified generalization strategy.

**Example excerpt**
```json
{
  "bundle_id": "kfm-sensitive-bundle-001",
  "spatial": "passed",
  "temporal": "passed",
  "care": "approved",
  "overall_status": "certified"
}
```

---

## ⚖️ Governance & Compliance Integration

All validation reports are consumed by:
- **Governance Ledger:** `reports/audit/governance-ledger.json`
- **Publication Clearance Pipeline:** holds or approves release of sensitive datasets
- **Council Quarterly Review:** stored in `docs/reports/telemetry/governance_scorecard.json`
- **Release Artifacts:** included in `manifest.zip` for v10+ releases

---

## 📊 Telemetry Signals

Each report is logged with:
- Validation duration  
- Energy & carbon estimates (ISO 50001 / 14064)  
- FAIR+CARE score  
- CARE sovereignty compliance indicators  

These are merged into:
```
releases/v10.2.0/focus-telemetry.json
```

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|--------:|------|--------|---------|
| v10.2.2 | 2025-11-12 | FAIR+CARE Council | Initial creation of validation report index with spatial/temporal/CARE/bundle integration. |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — CC BY-NC 4.0**  
FAIR+CARE Council · MCP v6.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[Back to Validation Index](../README.md) • [Generalization Standards](../../../README.md)

</div>

