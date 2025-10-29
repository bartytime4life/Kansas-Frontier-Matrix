---
title: "📜 Kansas Frontier Matrix — Treaties Dataset v9.3.2 (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "data/archive/treaties/treaties_v9.3.2/README.md"
version: "v9.3.2"
last_updated: "2025-10-28"
review_cycle: "Quarterly / Ethical Stewardship"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../releases/v9.3.2/sbom.spdx.json"
manifest_ref: "../../../../releases/v9.3.2/manifest.zip"
data_contract_ref: "../../../../docs/contracts/data-contract-v3.json"
governance_ref: "../../../../docs/standards/governance/TREATY-GOVERNANCE.md"
ontology_alignment: "../../../../ontologies/CIDOC_CRM-TreatyExt.owl"
---

<div align="center">

# 📜 Kansas Frontier Matrix — **Treaties Dataset v9.3.2**
`data/archive/treaties/treaties_v9.3.2/README.md`

**Purpose:** Official FAIR+CARE-certified archival dataset documenting Indigenous treaties, land cessions, and territorial boundaries across Kansas.  
Integrates spatial treaty data, text metadata, and historical document references under ethical stewardship and Indigenous Data Sovereignty principles.

[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Indigenous%20Data%20Sovereignty%20Certified-gold)](../../../../docs/standards/faircare-validation.md)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../../../LICENSE)
[![Ethics Certified](https://img.shields.io/badge/Ethics-Cultural%20Governance%20Approved-brown)](../../../../docs/standards/governance/TREATY-GOVERNANCE.md)
[![Docs · MCP-DL v6.3](https://img.shields.io/badge/Docs-MCP--DL%20v6.3-blue)](../../../../docs/architecture/repo-focus.md)

</div>

---

## 📚 Overview

**Treaties Dataset v9.3.2** is the most recent, fully FAIR+CARE-certified version of Kansas treaty and land cession data.  
It integrates verified geospatial boundaries with metadata extracted from U.S. government archives and Indigenous governance documentation.  

The dataset includes:
- Digitized treaty boundaries from archival maps (NARA & OHS).  
- Treaty text metadata (signatories, ratification dates, historical notes).  
- FAIR+CARE ethics review and governance sign-off.  
- Permanent archival registration with checksum verification and STAC index.

---

## 🗂️ Directory Layout

```plaintext
data/archive/treaties/treaties_v9.3.2/
├── README.md                            # This file — dataset documentation
│
├── treaties_boundaries_2025.geojson     # Geospatial treaty and cession polygons
├── treaties_metadata_2025.json          # Structured metadata (dates, signatories, tribes)
├── treaty_text_references_2025.csv      # Linked text excerpts from historical sources
├── validation_report.json               # STAC, FAIR+CARE, and schema validation results
├── provenance_record.json               # Provenance and governance metadata
├── checksums.sha256                     # Integrity verification file
└── governance_approval.md               # FAIR+CARE Council approval statement
```

---

## ⚙️ Dataset Composition

| File | Description | Source | Format |
|------|--------------|--------|--------|
| `treaties_boundaries_2025.geojson` | Polygon dataset showing historical treaty boundaries and cession extents. | NARA / OHS | GeoJSON |
| `treaties_metadata_2025.json` | Metadata describing treaty signatories, dates, and jurisdiction. | KFM / FAIR+CARE Council | JSON |
| `treaty_text_references_2025.csv` | Extracted treaty texts and linked archival citations. | Library of Congress / National Archives | CSV |

Spatial Reference: **EPSG:4326 (WGS84)**  
Temporal Range: **1790–1930**

---

## 🧩 Metadata Summary (STAC Extract)

```json
{
  "id": "treaties_v9.3.2",
  "title": "Kansas Treaty and Land Cession Dataset (v9.3.2)",
  "description": "FAIR+CARE-certified dataset representing Indigenous treaties and land cessions in Kansas, including spatial boundaries and treaty metadata.",
  "version": "v9.3.2",
  "created": "2025-10-28T16:45:00Z",
  "license": "CC-BY 4.0",
  "providers": [
    {"name": "National Archives and Records Administration (NARA)", "role": "data-source"},
    {"name": "Oklahoma Historical Society (OHS)", "role": "data-source"},
    {"name": "Kansas Frontier Matrix FAIR+CARE Council", "role": "validator"}
  ],
  "extent": {
    "spatial": {"bbox": [-102.05, 36.99, -94.61, 40.00]},
    "temporal": {"interval": ["1790-01-01T00:00:00Z", "1930-12-31T00:00:00Z"]}
  },
  "keywords": ["treaty", "Indigenous", "land cession", "fair-care", "kansas", "governance"]
}
```

---

## 🧠 FAIR+CARE Integration

| Principle | Implementation |
|------------|----------------|
| **Findable** | Indexed through STAC and searchable by treaty name and date. |
| **Accessible** | Publicly accessible under CC-BY 4.0 license. |
| **Interoperable** | Structured according to STAC 1.0 and CIDOC CRM. |
| **Reusable** | Provenance and metadata fully documented for research reuse. |
| **Collective Benefit** | Serves historical truth, education, and intercultural understanding. |
| **Authority to Control** | Indigenous partners consulted in governance process. |
| **Responsibility** | Council oversight ensures data contextual accuracy. |
| **Ethics** | Data reviewed for sensitivity; only public information included. |

Ethical validation governed by CARE+IDSA (Indigenous Data Sovereignty) guidelines.

---

## 🔍 Provenance Record (Excerpt)

```json
{
  "dataset_id": "treaties_v9.3.2",
  "compiled_by": "@kfm-etl-ops",
  "validated_by": "@kfm-data-lab",
  "ethics_reviewed_by": "@kfm-architecture",
  "sources": [
    "NARA Map Collection M-1655",
    "U.S. Serial Set Vol. 1258 (Treaty of 1854)",
    "OHS Historical Treaty Map Archive"
  ],
  "checksum": "fa58a4a9b92cc2c61d71fbc9ac7edafc7baf8e10b49c6f0f...",
  "archived_on": "2025-10-28T17:15:00Z",
  "fairstatus": {"fair_score": 98, "care_score": 100},
  "governance_decision": "approved"
}
```

---

## ⚙️ Validation & Governance Summary

| Validation Type | Status | Reference |
|------------------|---------|-----------|
| STAC Validation | ✅ Passed | `validation_report.json` |
| Schema Compliance | ✅ Passed | `schemas/treaties_schema_v9.3.2.json` |
| FAIR+CARE Certification | ✅ Approved | `data/reports/fair/data_care_assessment.json` |
| Governance Sign-Off | ✅ Completed | `governance_approval.md` |

Checksum verification completed via `checksums.sha256` and included in `releases/v9.3.2/manifest.zip`.

---

## ⚖️ Cultural and Ethical Stewardship

> The **FAIR+CARE Council**, in collaboration with Indigenous data representatives, confirms that this dataset:  
> - Accurately depicts historical treaty data without misrepresentation.  
> - Contains no restricted or culturally sensitive materials.  
> - Promotes understanding and transparency of historical land agreements.  
> - Upholds Indigenous Data Sovereignty principles through attribution and co-governance.

Full council documentation available in:  
`data/reports/fair/ethics_review_summary.md`

---

## 🧱 Linkages & Dependencies

| Linked File | Description |
|--------------|-------------|
| `data/reports/audit/data_provenance_ledger.json` | Provenance chain and audit record |
| `data/reports/fair/data_care_assessment.json` | FAIR+CARE assessment metrics |
| `data/reports/validation/stac_validation_report.json` | STAC validation log |
| `releases/v9.3.2/manifest.zip` | Global checksum manifest |
| `data/stac/items/treaties_v9.3.2.json` | STAC item reference |

---

## 🧾 Usage & Citation

**Access Path:**  
`data/archive/treaties/treaties_v9.3.2/`

**Citation Example:**
```text
Kansas Frontier Matrix (2025). Kansas Treaties and Land Cessions Dataset (v9.3.2).
FAIR+CARE-certified archival dataset integrating geospatial and textual treaty data.
Available at: https://github.com/bartytime4life/Kansas-Frontier-Matrix/tree/main/data/archive/treaties/treaties_v9.3.2
License: CC-BY 4.0
```

---

## 🧾 Version Notes

- **Release v9.3.2:** Integrated textual and geospatial treaty datasets; added CARE+IDSA cultural governance certification.  
- **Enhancements:** Provenance detail improvements; Indigenous advisory participation added to review process.  
- **Governance:** Approved unanimously by FAIR+CARE Council on 2025-10-28.  

---

<div align="center">

**Kansas Frontier Matrix** · *Historical Treaties × FAIR+CARE Stewardship × Indigenous Data Sovereignty*  
[🔗 Repository](https://github.com/bartytime4life/Kansas-Frontier-Matrix) • [🧭 Docs Portal](../../../../docs/) • [⚖️ Governance Ledger](../../../../docs/standards/governance/)

</div>
