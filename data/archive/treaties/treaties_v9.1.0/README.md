---
title: "📜 Kansas Frontier Matrix — Treaties Dataset v9.1.0 (FAIR+CARE Certified)"
path: "data/archive/treaties/treaties_v9.1.0/README.md"
version: "v9.1.0"
last_updated: "2024-06-01"
review_cycle: "Quarterly / Historical"
commit_sha: "<legacy-commit-hash>"
sbom_ref: "../../../../releases/v9.1.0/sbom.spdx.json"
manifest_ref: "../../../../releases/v9.1.0/manifest.zip"
data_contract_ref: "../../../../docs/contracts/data-contract-v3.json"
governance_ref: "../../../../docs/standards/governance/TREATY-GOVERNANCE.md"
ontology_alignment: "../../../../ontologies/CIDOC_CRM-TreatyExt.owl"
---

<div align="center">

# 📜 Kansas Frontier Matrix — **Treaties Dataset v9.1.0**
`data/archive/treaties/treaties_v9.1.0/README.md`

**Purpose:** Archival release of Kansas Frontier Matrix’s integrated treaty and land cession dataset for the 2023–2024 governance cycle.  
Precedes the fully Indigenous Data Sovereignty-certified v9.3.2 release. FAIR+CARE validated and historically verified.

[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Certified-gold)](../../../../docs/standards/faircare-validation.md)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../../../LICENSE)
[![STAC Validation](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](../../../../.github/workflows/stac-validate.yml)
[![Docs · MCP-DL v6.3](https://img.shields.io/badge/Docs-MCP--DL%20v6.3-blue)](../../../../docs/architecture/repo-focus.md)

</div>

---

## 📚 Overview

**Treaties Dataset v9.1.0** represents the 2024 FAIR+CARE-compliant archival dataset documenting Indigenous treaties, land cessions, and jurisdictional transformations across Kansas.  
It builds upon early digitizations from NARA and OHS sources while introducing complete metadata alignment with the FAIR+CARE governance model.

This version includes:
- Treaty boundary geospatial layers (GeoJSON).  
- Metadata linking treaty names, signatories, and effective years.  
- Basic provenance records and validation reports.  
- FAIR+CARE certification prior to CARE+IDSA integration in v9.3.2.

---

## 🗂️ Directory Layout

```plaintext
data/archive/treaties/treaties_v9.1.0/
├── README.md                            # This file — dataset overview
│
├── treaties_boundaries.geojson          # Treaty boundary polygons and cession extents
├── metadata.json                        # Dataset-level metadata and provenance
├── validation_report.json               # Validation summary
├── provenance_record.json               # Governance and lineage information
└── checksums.sha256                     # SHA-256 checksum verification file
```

---

## ⚙️ Dataset Composition

| File | Description | Source | Format |
|------|--------------|---------|--------|
| `treaties_boundaries.geojson` | Polygon dataset showing territorial boundaries based on treaty and cession maps. | NARA / OHS | GeoJSON |
| `metadata.json` | Metadata describing treaties, signatories, and archival source references. | KFM FAIR+CARE Review | JSON |
| `provenance_record.json` | Provenance and FAIR+CARE governance record. | FAIR+CARE Council | JSON |

Spatial Reference: **EPSG:4326 (WGS84)**  
Temporal Range: **1790–1930**

---

## 🧩 Metadata Summary (Excerpt)

```json
{
  "id": "treaties_v9.1.0",
  "title": "Kansas Treaty and Land Cession Dataset (v9.1.0)",
  "description": "FAIR+CARE-certified dataset representing Indigenous treaties and land cessions in Kansas. Data compiled from NARA and OHS archives.",
  "version": "v9.1.0",
  "created": "2024-06-01T10:30:00Z",
  "license": "CC-BY 4.0",
  "providers": [
    {"name": "NARA", "role": "data-source"},
    {"name": "Oklahoma Historical Society", "role": "data-source"},
    {"name": "Kansas Frontier Matrix FAIR+CARE Council", "role": "validator"}
  ],
  "extent": {
    "spatial": {"bbox": [-102.05, 36.99, -94.61, 40.00]},
    "temporal": {"interval": ["1790-01-01T00:00:00Z", "1930-12-31T00:00:00Z"]}
  }
}
```

---

## 🧠 FAIR+CARE Validation Summary

| Validation Type | Status | Reference |
|------------------|---------|------------|
| STAC Schema Validation | ✅ Passed | `validation_report.json` |
| FAIR+CARE Ethical Review | ✅ Approved | `data/reports/fair/data_care_assessment.json` |
| Governance Audit | ✅ Logged | `data/reports/audit/data_provenance_ledger.json` |

**Composite FAIR+CARE Score:**  
FAIR = 97 / 100, CARE = 99 / 100

---

## 🔍 Provenance Record (Excerpt)

```json
{
  "dataset_id": "treaties_v9.1.0",
  "compiled_by": "@kfm-etl-ops",
  "validated_by": "@kfm-data-lab",
  "checksum": "6b84f9a1a26c5e897b03e4c7e2b12b0e6bb23741...",
  "archived_on": "2024-06-01T15:10:00Z",
  "etl_pipeline": "src/pipelines/etl/treaties/treaties_pipeline.py",
  "sources": [
    "NARA Map Collection M-1655",
    "OHS Land Cession Atlas (Digital)",
    "U.S. Serial Set Vol. 1258 (Treaty of 1854)"
  ],
  "governance_status": "approved"
}
```

---

## ⚙️ Governance & Integrity Verification

All dataset governance and validation steps verified by:
- `data/reports/audit/data_provenance_ledger.json` — Provenance ledger entry.  
- `data/reports/fair/data_care_assessment.json` — FAIR+CARE scoring record.  
- `data/reports/validation/stac_validation_report.json` — Metadata and schema compliance.  
- `releases/v9.1.0/manifest.zip` — Checksum and manifest validation record.  

---

## ⚖️ Ethical Stewardship Statement

> This dataset was reviewed by the **FAIR+CARE Council** in partnership with external historians and Indigenous cultural liaisons.  
> The dataset was approved for public dissemination under the following conditions:
> - Attribution of Indigenous nations and treaty partners required.  
> - Derived works must maintain historical context and citation integrity.  
> - Culturally sensitive materials were excluded from this release.  

Council approval documented in:  
`data/reports/fair/ethics_review_summary.md`

---

## 🧱 Governance Linkages

| Linked File | Purpose |
|--------------|----------|
| `data/reports/audit/data_provenance_ledger.json` | Provenance tracking and governance log |
| `data/reports/fair/data_fair_summary.json` | FAIR assessment |
| `data/reports/fair/data_care_assessment.json` | CARE ethical assessment |
| `releases/v9.1.0/manifest.zip` | Checksum and manifest record |

---

## 🧾 Citation

**Access Path:**  
`data/archive/treaties/treaties_v9.1.0/`

**Citation Example:**
```text
Kansas Frontier Matrix (2024). Kansas Treaties Dataset (v9.1.0).
FAIR+CARE-certified dataset integrating historical treaty and land cession records.
Available at: https://github.com/bartytime4life/Kansas-Frontier-Matrix/tree/main/data/archive/treaties/treaties_v9.1.0
License: CC-BY 4.0
```

---

## 🧾 Version Notes

| Version | Date | Notes |
|----------|------|--------|
| v9.3.2 | 2025-10-28 | Added Indigenous Data Sovereignty (CARE+IDSA) compliance. |
| v9.1.0 | 2024-06-01 | FAIR+CARE-certified; included first ethics council review. |
| Legacy | Pre-2023 | Early digitized treaty datasets compiled without full governance. |

---

<div align="center">

**Kansas Frontier Matrix** · *Historical Governance × FAIR+CARE Ethics × Cultural Stewardship*  
[🔗 Repository](https://github.com/bartytime4life/Kansas-Frontier-Matrix) • [🧭 Docs Portal](../../../../docs/) • [⚖️ Governance Ledger](../../../../docs/standards/governance/)

</div>
