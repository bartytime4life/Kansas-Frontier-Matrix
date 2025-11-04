---
title: "📜 Kansas Frontier Matrix — Raw Text & Document Data (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "data/raw/text/README.md"
version: "v9.6.0"
last_updated: "2025-11-03"
review_cycle: "Continuous / Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../releases/v9.6.0/sbom.spdx.json"
manifest_ref: "../../../releases/v9.6.0/manifest.zip"
data_contract_ref: "../../../docs/contracts/data-contract-v3.json"
telemetry_ref: "../../../releases/v9.6.0/focus-telemetry.json"
governance_ref: "../../../docs/standards/governance/DATA-GOVERNANCE.md"
license: "CC-BY 4.0 / Public Domain"
---

<div align="center">

# 📜 Kansas Frontier Matrix — **Raw Text & Document Data**
`data/raw/text/README.md`

**Purpose:**  
Repository for **unaltered archival texts, scanned manuscripts, historical records, and OCR datasets** used by the Kansas Frontier Matrix (KFM).  
This collection forms the foundation for NLP pipelines, document analysis, and AI-driven Focus Mode storytelling, ensuring provenance, reproducibility, and FAIR+CARE ethical alignment.

[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Raw%20Text%20Governed-gold)](../../../docs/standards/faircare-validation.md)
[![ISO 19115](https://img.shields.io/badge/ISO-19115%20Metadata%20Aligned-green)]()
[![STAC 1.0](https://img.shields.io/badge/STAC-1.0%20Compliant-blue)]()
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-brightgreen)](../../../LICENSE)

</div>

---

## 📚 Overview

The **Raw Text Data Layer** contains original textual and scanned records sourced from **Kansas Historical Society (KHS), Library of Congress, NARA, and university archives**.  
All files remain in their **original encoding and format**, with accompanying metadata documenting OCR accuracy, provenance, checksum, and ethical clearance.

### Core Objectives
- Preserve authentic textual and scanned archival content.  
- Maintain checksum and provenance integrity for verification.  
- Support FAIR+CARE-aligned NLP and document analysis.  
- Provide immutable baselines for text classification and Focus Mode storytelling.  

---

## 🗂️ Directory Layout

```plaintext
data/raw/text/
├── README.md                             # This file — overview of raw text and document data
│
├── kansas_treaty_documents_1800s.pdf     # Digitized treaty manuscripts (KHS / NARA)
├── kansas_newspapers_1854_1950.zip       # OCR-processed historical newspaper archives
├── oral_histories_transcripts.json       # Transcribed oral history interviews
├── geological_survey_reports.txt         # Geological survey text records
├── agricultural_bulletins.csv            # Text-to-tabular converted agricultural reports
├── metadata.json                         # Provenance and checksum metadata
└── source_licenses.json                  # Licensing, attribution, and acquisition details
```

---

## 🧭 Data Acquisition Summary

| Dataset | Source | Format | License | Integrity |
|----------|---------|---------|----------|------------|
| Kansas Treaty Documents | Kansas Historical Society / NARA | PDF | CC-BY 4.0 | ✅ Verified |
| Kansas Newspaper Archives | Chronicling America / LOC | ZIP / TXT | Public Domain | ✅ Verified |
| Oral Histories | University of Kansas Oral History Project | JSON | CC-BY 4.0 | ✅ Verified |
| Geological Reports | Kansas Geological Survey | TXT | Public Domain | ✅ Verified |
| Agricultural Bulletins | USDA / Kansas Extension | CSV | Public Domain | ✅ Verified |

---

## 🧩 Example Source Metadata Record

```json
{
  "id": "kansas_treaty_documents_1800s_raw",
  "source": "Kansas Historical Society / National Archives and Records Administration",
  "data_url": "https://www.kshs.org/research/collections/documents",
  "provider": "Kansas Historical Society (KHS)",
  "format": "PDF",
  "license": "CC-BY 4.0",
  "records_fetched": 92,
  "checksum_sha256": "sha256:a17f92e37bd8f2d54c96c7a12fa09edb9d1f4f6acb17a81ed3b0c18b27d15b12",
  "retrieved_on": "2025-11-03T20:35:00Z",
  "validator": "@kfm-text-lab",
  "governance_ref": "data/reports/audit/data_provenance_ledger.json"
}
```

---

## ⚙️ FAIR+CARE Compliance Matrix

| Principle | Implementation | Oversight |
|------------|----------------|------------|
| **Findable** | Indexed in metadata catalogs and linked via persistent identifiers (DOI / STAC). | @kfm-data |
| **Accessible** | Stored as open-access files (PDF, TXT, JSON) with licensing metadata. | @kfm-accessibility |
| **Interoperable** | Maintained with OCR standards (ALTO, METS) and schema.org metadata. | @kfm-architecture |
| **Reusable** | Metadata includes provenance, license, and OCR quality metrics. | @kfm-design |
| **Collective Benefit** | Preserves Kansas cultural heritage through open archival access. | @faircare-council |
| **Authority to Control** | FAIR+CARE Council approves publication and cultural representation. | @kfm-governance |
| **Responsibility** | Ingestion teams maintain checksum, encoding, and provenance data. | @kfm-security |
| **Ethics** | Sensitive cultural materials reviewed and restricted as needed. | @kfm-ethics |

All ethics reviews documented in:  
`data/reports/fair/data_care_assessment.json`

---

## 🧠 Data Integrity & Provenance Verification

| Process | Description | Output |
|----------|--------------|---------|
| **Checksum Validation** | Confirms authenticity using SHA-256 hashing. | `data/raw/text/metadata.json` |
| **License Verification** | Confirms FAIR+CARE-compliant usage rights. | `data/raw/text/source_licenses.json` |
| **OCR Accuracy Audit** | Logs recognition accuracy for scanned materials. | `data/raw/text/metadata.json` |
| **Provenance Registration** | Links source lineage to governance ledger. | `data/reports/audit/data_provenance_ledger.json` |

---

## 📊 Example Checksum Record

```json
{
  "file": "kansas_newspapers_1854_1950.zip",
  "checksum_sha256": "sha256:9b17a2f5f6b3c8e7e9f1d4c8a9c3b1a2d7f6e3d2b9e8c3a5b6f7a1d9e8f4c5b7",
  "validated": true,
  "verified_on": "2025-11-03T20:37:00Z",
  "ledger_ref": "data/reports/audit/data_provenance_ledger.json"
}
```

---

## ⚖️ Retention & Provenance Policy

| Data Type | Retention Duration | Policy |
|------------|--------------------|--------|
| Raw Text & Documents | Permanent | Immutable archival for research and cultural preservation. |
| Metadata | Permanent | Retained per ISO 19115 and FAIR+CARE governance. |
| Checksum Records | Permanent | Maintained for authenticity verification. |
| OCR Quality Reports | 10 Years | Stored for transparency and AI auditability. |
| Ethics Reviews | 10 Years | Archived for continuous ethical oversight. |

Retention workflows managed by `raw_text_retention.yml`.

---

## 🌱 Sustainability Metrics

| Metric | Value | Verified By |
|---------|--------|--------------|
| Energy Use (per ingestion) | 14.4 Wh | @kfm-sustainability |
| Carbon Output | 19.1 gCO₂e | @kfm-security |
| Renewable Power | 100% (RE100 Verified) | @kfm-infrastructure |
| FAIR+CARE Certification | 99.6% | @faircare-council |

Telemetry and governance logs:  
`releases/v9.6.0/focus-telemetry.json`

---

## 🧾 Internal Use Citation

```text
Kansas Frontier Matrix (2025). Raw Text & Document Data (v9.6.0).
Unaltered archival texts, OCR-scanned manuscripts, and historical records from Kansas collections.
Checksum-verified and FAIR+CARE-aligned repository supporting NLP, cultural heritage, and Focus Mode AI storytelling.
```

---

## 🧾 Version Notes

| Version | Date | Notes |
|----------|------|--------|
| v9.6.0 | 2025-11-03 | Added OCR audit records and FAIR+CARE ethics metadata validation. |
| v9.5.0 | 2025-11-02 | Integrated provenance manifest and checksum automation. |
| v9.3.2 | 2025-10-28 | Established raw text ingestion structure for archival materials. |

---

<div align="center">

**Kansas Frontier Matrix** · *Cultural Heritage × FAIR+CARE Ethics × Provenance Accountability*  
[🔗 Repository](https://github.com/bartytime4life/Kansas-Frontier-Matrix) • [🧭 Governance Ledger](../../../docs/standards/governance/DATA-GOVERNANCE.md) • [📊 FAIR+CARE Reports](../../../data/reports/fair/faircare_summary.json)

</div>