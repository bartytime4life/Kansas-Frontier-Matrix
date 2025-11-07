---
title: "📜 Kansas Frontier Matrix — Raw Text & Document Data (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "data/raw/text/README.md"
version: "v9.7.0"
last_updated: "2025-11-06"
review_cycle: "Continuous / Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../releases/v9.7.0/sbom.spdx.json"
manifest_ref: "../../../releases/v9.7.0/manifest.zip"
data_contract_ref: "../../../docs/contracts/data-contract-v3.json"
telemetry_ref: "../../../releases/v9.7.0/focus-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/data-raw-text-v9.json"
governance_ref: "../../../docs/standards/governance/DATA-GOVERNANCE.md"
license: "CC-BY 4.0 / Public Domain"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 📜 Kansas Frontier Matrix — **Raw Text & Document Data**
`data/raw/text/README.md`

**Purpose:**  
Repository for **unaltered archival texts, scanned manuscripts, historical records, and OCR datasets** used by the Kansas Frontier Matrix (KFM).  
This collection underpins NLP pipelines, document analysis, and **Focus Mode** storytelling with **provenance, reproducibility, and FAIR+CARE** ethical alignment.

[![Docs · MCP](https://img.shields.io/badge/Docs%20·%20MCP-v6.3-blue.svg)](../../../docs/architecture/README.md)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-brightgreen.svg)](../../../LICENSE)
[![FAIR+CARE Ethics](https://img.shields.io/badge/FAIR%2BCARE-Raw%20Text%20Governed-gold.svg)](../../../docs/standards/faircare-validation.md)
[![STAC 1.0](https://img.shields.io/badge/STAC-1.0%20Compliant-0052cc.svg)]()
[![ISO 19115](https://img.shields.io/badge/ISO-19115%20Metadata%20Aligned-green.svg)]()

</div>

---

## 📘 Overview

The **Raw Text Data Layer** contains original textual and scanned records from **KHS, Library of Congress, NARA, and university archives**.  
All files remain in their **original encoding and format**, with accompanying metadata documenting **OCR accuracy**, **provenance**, **checksums**, and **ethical clearance**.

### Core Objectives
- Preserve authentic textual and scanned archival content.  
- Maintain **checksum & provenance** integrity for verification.  
- Support **FAIR+CARE-aligned** NLP and document analysis.  
- Provide **immutable baselines** for text classification and storytelling.

---

## 🗂️ Directory Layout

```plaintext
data/raw/text/
├── README.md
├── kansas_treaty_documents_1800s.pdf     # Digitized treaty manuscripts (KHS / NARA)
├── kansas_newspapers_1854_1950.zip       # OCR-processed historical newspapers
├── oral_histories_transcripts.json       # Transcribed oral history interviews
├── geological_survey_reports.txt         # Geological survey text records
├── agricultural_bulletins.csv            # Text→tabular converted bulletins
├── metadata.json                         # Provenance & checksum manifest (+ OCR stats)
└── source_licenses.json                  # Licensing, attribution, acquisition details
```

---

## 🧭 Data Acquisition Summary

| Dataset                    | Source / Provider                         | Format | License        | Integrity |
|---------------------------|-------------------------------------------|--------|----------------|----------:|
| Kansas Treaty Documents   | KHS / NARA                                 | PDF    | CC-BY 4.0      | ✅ Verified |
| Newspaper Archives        | LOC Chronicling America                    | ZIP/TXT| Public Domain  | ✅ Verified |
| Oral Histories            | Univ. of Kansas Oral History Project       | JSON   | CC-BY 4.0      | ✅ Verified |
| Geological Reports        | Kansas Geological Survey                   | TXT    | Public Domain  | ✅ Verified |
| Agricultural Bulletins    | USDA / Kansas Extension                    | CSV    | Public Domain  | ✅ Verified |

---

## 🧩 Example Source Metadata Record

```json
{
  "id": "kansas_treaty_documents_1800s_raw",
  "domain": "text",
  "source": "Kansas Historical Society / National Archives and Records Administration",
  "data_url": "https://www.kshs.org/research/collections/documents",
  "provider": "Kansas Historical Society (KHS)",
  "format": "PDF",
  "license": "CC-BY 4.0",
  "records_fetched": 92,
  "checksum_sha256": "sha256:a17f92e37bd8f2d54c96c7a12fa09edb9d1f4f6acb17a81ed3b0c18b27d15b12",
  "retrieved_on": "2025-11-06T20:35:00Z",
  "ocr_quality": {"engine": "Tesseract 5.3", "mean_char_acc": 0.984},
  "validator": "@kfm-text-lab",
  "governance_ref": "data/reports/audit/data_provenance_ledger.json"
}
```

---

## ⚙️ FAIR+CARE Compliance Matrix

| Principle | Implementation | Oversight |
|-----------|----------------|-----------|
| **Findable** | Metadata catalogs w/ PIDs (DOI/ARK); STAC for geotagged texts. | `@kfm-data` |
| **Accessible** | Open PDFs/TXT/JSON under clear licenses; alt text & captions. | `@kfm-accessibility` |
| **Interoperable** | OCR standards (ALTO/METS); schema.org & DCAT fields. | `@kfm-architecture` |
| **Reusable** | Provenance, license, OCR quality, and checksums embedded. | `@kfm-design` |
| **Collective Benefit** | Preserves Kansas cultural heritage via open access. | `@faircare-council` |
| **Authority to Control** | Council approves publication & cultural representation. | `@kfm-governance` |
| **Responsibility** | Teams maintain encoding, checksum, and lineage. | `@kfm-security` |
| **Ethics** | Sensitive cultural materials flagged and access-scoped. | `@kfm-ethics` |

---

## 🧠 Integrity, OCR & Cataloging

| Process              | Description                                     | Output                                           |
|---------------------|-------------------------------------------------|--------------------------------------------------|
| **Checksum Verify** | SHA-256 per file; vendor hash comparison.        | `data/raw/text/metadata.json`                    |
| **License Audit**   | FAIR+CARE licensing & attribution review.        | `data/raw/text/source_licenses.json`             |
| **OCR Audit**       | Accuracy metrics (CER/WER) + engine/version.     | `metadata.json`                                  |
| **Catalog Publish** | STAC/DCAT registration & story-node linkage.     | `data/raw/metadata/stac_catalog.json`            |

---

## 📊 Example Checksum Record

```json
{
  "file": "kansas_newspapers_1854_1950.zip",
  "checksum_sha256": "sha256:9b17a2f5f6b3c8e7e9f1d4c8a9c3b1a2d7f6e3d2b9e8c3a5b6f7a1d9e8f4c5b7",
  "validated": true,
  "verified_on": "2025-11-06T20:37:00Z",
  "ledger_ref": "data/reports/audit/data_provenance_ledger.json"
}
```

---

## ⚖️ Retention & Sustainability

| Category                | Retention | Policy                                                  |
|------------------------|----------:|---------------------------------------------------------|
| Raw Text & Documents   | Permanent | Immutable archival for research & cultural preservation.|
| Source Metadata        | Permanent | ISO 19115 lineage retention.                            |
| Checksum Records       | Permanent | Long-term authenticity evidence.                         |
| OCR Quality Reports    | 10 Years  | Stored for transparency & AI auditability.              |
| Ethics Reviews         | 10 Years  | Archived for continuous ethical oversight.              |

**Telemetry reference:** `../../../releases/v9.7.0/focus-telemetry.json`

---

## 🧾 Internal Use Citation

```text
Kansas Frontier Matrix (2025). Raw Text & Document Data (v9.7.0).
Unaltered archival texts, OCR-scanned manuscripts, and historical records from Kansas collections.
Checksum-verified and FAIR+CARE-aligned repository supporting NLP, cultural heritage, and Focus Mode AI storytelling.
```

---

## 🕰️ Version History

| Version | Date       | Author         | Summary |
|--------:|------------|----------------|---------|
| v9.7.0  | 2025-11-06 | `@kfm-text`    | Upgraded to v9.7.0; telemetry/schema refs aligned; OCR audit fields & badges added. |
| v9.6.0  | 2025-11-03 | `@kfm-text`    | Added OCR audit records and FAIR+CARE ethics metadata validation. |
| v9.5.0  | 2025-11-02 | `@kfm-governance` | Integrated provenance manifest and checksum automation. |

---

<div align="center">

**Kansas Frontier Matrix**  
*Cultural Heritage × FAIR+CARE Ethics × Provenance Accountability*  
© 2025 Kansas Frontier Matrix — CC-BY 4.0 / Public Domain · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[Back to Raw Data Index](../README.md) · [Governance Charter](../../../docs/standards/governance/DATA-GOVERNANCE.md)

</div>