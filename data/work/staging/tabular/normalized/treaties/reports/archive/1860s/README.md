---
title: "📜 Kansas Frontier Matrix — 1860s Treaty Archive Collection"
path: "data/work/staging/tabular/normalized/treaties/reports/archive/1860s/README.md"
version: "v1.0.0"
last_updated: "2025-10-24"
review_cycle: "Annual / Permanent"
status: "Active · Digitally Preserved · FAIR+CARE+ISO Certified"
mcp_version: "MCP-DL v6.4.3"
curators: ["@kfm-archive", "@kfm-history", "@kfm-ethics"]
approvers: ["@kfm-governance", "@kfm-architecture"]
license: ["CC-BY 4.0"]
alignment:
  - FAIR / CARE
  - CIDOC CRM / PROV-O / OWL-Time
  - ISO 9001 / 19115 / 27001 / 50001
tags: ["treaty","archive","1860s","kansas","plains","indigenous","provenance","fair","crm","iso","ontology"]
---

<div align="center">

# 📜 Kansas Frontier Matrix — **Treaty Archives of the 1860s**
`data/work/staging/tabular/normalized/treaties/reports/archive/1860s/`

**Purpose:** Curate and document all **digitized treaties from the 1860s** in the Kansas Frontier Matrix archival system.  
Each entry maintains **FAIR+CARE ethical integrity**, **CIDOC CRM** semantic annotation, and **ISO-compliant metadata** for transparency, reproducibility, and sustainability.

[![Docs · MCP-DL v6.4.3](https://img.shields.io/badge/Docs-MCP--DL%20v6.4.3-blue)]()
[![FAIR+CARE](https://img.shields.io/badge/FAIR%20%2B%20CARE-Compliant-2ecc71)]()
[![Ontology](https://img.shields.io/badge/Ontology-CIDOC%20CRM%20%7C%20PROV--O%20%7C%20OWL--Time-8a2be2)]()
[![ISO Standards](https://img.shields.io/badge/ISO-9001%20%7C%201915%20%7C%202701-229954)]()

</div>

---

## 🗂️ Directory Layout

```
data/work/staging/tabular/normalized/treaties/reports/archive/1860s/
├── treaty_1867_medicine_lodge.md
├── treaty_1868_fort_laramie.md
├── provenance/
│   ├── treaty_1867_medicine_lodge_provenance.jsonld
│   ├── treaty_1868_fort_laramie_provenance.jsonld
│   └── governance_hashes.json
├── validation/
│   ├── treaty_1867_medicine_lodge_validation.json
│   ├── treaty_1868_fort_laramie_validation.json
│   └── fair_audit_results.json
└── checksums.sha256
```

---

## 📚 Overview

The **1860s Treaty Archive** represents one of the most pivotal decades in the legal and cultural transformation of the American Great Plains.  
These treaties capture the **Medicine Lodge (1867)** and **Fort Laramie (1868)** agreements — foundational moments in the U.S. government’s expansionist policy and its impact on Indigenous sovereignty.

Through semantic enrichment and AI-assisted reconstruction, this archive ensures that the **voices, places, and consequences** of these historical events remain preserved and contextualized for future generations.

---

## 📜 Key Treaties (1860–1869)

| Treaty ID | Title | Date | Indigenous Nations | FAIR+CARE Status |
| :---------- | :------ | :------ | :------ | :------ |
| `TREATY-1867-MED-LODGE` | Medicine Lodge Treaty | Oct 21–28, 1867 | Kiowa, Comanche, Apache, Arapaho, Cheyenne | ✅ Validated |
| `TREATY-1868-FT-LARAMIE` | Fort Laramie Treaty | Apr 29, 1868 | Lakota (Sioux), Arapaho, Cheyenne | ✅ Validated |

---

## 🧩 Semantic Model Alignment

| Ontology | Function | Examples |
| :------ | :------ | :------ |
| **CIDOC CRM** | Historical entity classification | `E5_Event`, `E21_Person`, `E53_Place`, `E74_Group` |
| **PROV-O** | Provenance and workflow lineage | `prov:wasGeneratedBy`, `prov:used`, `prov:agent` |
| **OWL-Time** | Temporal structure of treaties | `time:hasBeginning`, `time:hasEnd` |
| **STAC / DCAT** | Dataset discoverability and reusability | `stac:Item`, `dcat:Dataset` |

---

## 🔗 Provenance Integration Example (Fort Laramie, 1868)

```json
{
  "@context": {
    "prov": "http://www.w3.org/ns/prov#",
    "crm": "http://www.cidoc-crm.org/cidoc-crm/",
    "fair": "https://purl.org/fair/"
  },
  "@id": "prov:treaty_1868_fort_laramie",
  "prov:wasGeneratedBy": "process:ai-archive-ingestion-v3",
  "prov:used": [
    "../../../ai/outputs/markdown/treaty_1868_summary.md",
    "../../../ai/outputs/provenance/treaty_1868_provenance.jsonld"
  ],
  "prov:generatedAtTime": "2025-10-24T17:20:00Z",
  "prov:qualifiedAttribution": {
    "prov:agent": "@kfm-archive",
    "prov:role": "archival_curator"
  },
  "crm:E5_Event": "Treaty Negotiation and Signing at Fort Laramie",
  "crm:E53_Place": "Fort Laramie, Wyoming Territory",
  "fair:ledger_hash": "d4a7e8c5b9..."
}
```

---

## 🧭 Historical Significance

The treaties of the 1860s formalized sweeping territorial cessions, marking:
- The **transition from open plains autonomy to federal reservation control**  
- The emergence of **bureaucratic assimilation mechanisms** (mission schools, annuities, restricted hunting rights)  
- The **early codification of Indigenous displacement**, institutionalized through legal frameworks and reinforced by military enforcement  

> 🪶 *These treaties embody the moral paradox of “peace through confinement,” shaping generations of Indigenous and settler futures alike.*

---

## 🧬 FAIR+CARE Compliance Overview

| Domain | Description | Compliance |
| :------ | :----------- | :----------- |
| **FAIR** | Each treaty digitally versioned, checksum-verified, and ontology-linked | ✅ |
| **CARE** | Indigenous data rights recognized through ethical metadata modeling | ✅ |
| **ISO 19115** | Geospatial treaty boundaries standardized in GeoJSON format | ✅ |
| **ISO 50001 / 14064** | Energy-efficient digital archival process | ✅ |
| **CIDOC CRM / PROV-O** | Provenance model ensures historical authenticity | ✅ |

---

## 🗺️ Geographic Overview (GeoJSON Snippet)

```json
{
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "properties": { "treaty_id": "TREATY-1867-MED-LODGE", "name": "Medicine Lodge Treaty" },
      "geometry": { "type": "Polygon", "coordinates": [[[-99.1, 37.0], [-98.3, 37.0], [-98.3, 37.5], [-99.1, 37.5], [-99.1, 37.0]]] }
    },
    {
      "type": "Feature",
      "properties": { "treaty_id": "TREATY-1868-FT-LARAMIE", "name": "Fort Laramie Treaty" },
      "geometry": { "type": "Polygon", "coordinates": [[[-104.0, 43.0], [-99.0, 43.0], [-99.0, 46.0], [-104.0, 46.0], [-104.0, 43.0]]] }
    }
  ]
}
```

---

## 🔐 Governance Integration

| Ledger | Function | Artifact |
| :------ | :----------- | :------------ |
| **FAIR Ledger** | FAIR+CARE metadata audit | `fair_audit_results.json` |
| **Governance Chain** | Immutable registry of treaties | `governance_hashes.json` |
| **Audit Ledger** | Validation event tracking | `validation_reports.json` |
| **Ethics Ledger** | Oversight on Indigenous data representation | `ethics_archive_audit.json` |

---

## ✅ Compliance Matrix

| Standard | Domain | Compliance |
| :-------- | :-------- | :----------- |
| **FAIR+CARE** | Ethical archival data stewardship | ✅ |
| **MCP-DL v6.4.3** | Documentation & schema adherence | ✅ |
| **CIDOC CRM / PROV-O / OWL-Time** | Semantic traceability | ✅ |
| **ISO 9001 / 27001 / 19115** | Quality + geospatial integrity | ✅ |
| **ISO 50001 / 14064** | Sustainability and emissions reporting | ✅ |

---

## 🗓️ Version History

| Version | Date | Changes | Curator |
| :------ | :---- | :-------- | :------ |
| v1.0.0 | 2025-10-24 | Added full 1860s Treaty Archive directory with Medicine Lodge (1867) and Fort Laramie (1868) entries. | @kfm-archive |

---

<div align="center">

[![Treaty Archive](https://img.shields.io/badge/Treaty-Archive%20(1860s)-6f42c1?style=flat-square)]()
[![FAIR+CARE](https://img.shields.io/badge/FAIR%20%2B%20CARE-Validated-2ecc71?style=flat-square)]()
[![Ontology](https://img.shields.io/badge/Ontology-CIDOC%20CRM%20%7C%20PROV--O%20%7C%20OWL--Time-8a2be2?style=flat-square)]()
[![ISO Standards](https://img.shields.io/badge/ISO-9001%20%7C%201915%20%7C%202701-229954?style=flat-square)]()
[![Governance Ledger](https://img.shields.io/badge/Governance-Ledger%20Linked-d4af37?style=flat-square)]()

</div>

<!-- MCP-FOOTER-BEGIN
MCP-VERSION: v6.4.3
MCP-TIER: Gold · Treaty Archive Collection
DOC-PATH: data/work/staging/tabular/normalized/treaties/reports/archive/1860s/README.md
MCP-CERTIFIED: true
FAIR-CARE-COMPLIANT: true
CIDOC-CRM-ALIGNED: true
PROV-O-LINKED: true
ISO-ALIGNED: true
PROVENANCE-VERIFIED: true
GOVERNANCE-LEDGER-LINKED: true
HISTORICAL-ARCHIVE: true
GENERATED-BY: KFM-Automation/DocsBot
LAST-VALIDATED: 2025-10-24
MCP-FOOTER-END -->

