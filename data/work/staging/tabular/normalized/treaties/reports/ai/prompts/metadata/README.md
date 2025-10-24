---
title: "🗂️ Kansas Frontier Matrix — AI Metadata Prompt Library"
path: "data/work/staging/tabular/normalized/treaties/reports/ai/prompts/metadata/README.md"
version: "v1.0.0"
last_updated: "2025-10-24"
review_cycle: "Continuous / Adaptive"
status: "Active · FAIR+CARE+ISO Metadata Verified"
mcp_version: "MCP-DL v6.4.3"
maintainers: ["@kfm-ai", "@kfm-data", "@kfm-validation"]
approvers: ["@kfm-architecture", "@kfm-governance", "@kfm-ethics"]
license: ["MIT (code)", "CC-BY 4.0 (data/docs)"]
alignment:
  - FAIR / CARE
  - STAC / DCAT
  - CIDOC CRM / PROV-O / OWL-Time
  - ISO 9001 / 19115 / 27001 / 50001
tags: ["ai","prompts","metadata","fair","care","provenance","cidoc","ontology","governance","iso"]
---

<div align="center">

# 🗂️ Kansas Frontier Matrix — **AI Metadata Prompt Library**
`data/work/staging/tabular/normalized/treaties/reports/ai/prompts/metadata/`

**Purpose:** Define and curate **AI prompt templates** responsible for generating and verifying metadata aligned with **FAIR+CARE**, **CIDOC CRM**, and **ISO 19115** standards for all treaty datasets and reports.

[![Docs · MCP-DL v6.4.3](https://img.shields.io/badge/Docs-MCP--DL%20v6.4.3-blue)]()
[![AI Metadata Prompts](https://img.shields.io/badge/AI--Prompts-Metadata-6f42c1)]()
[![FAIR+CARE](https://img.shields.io/badge/FAIR%20%2B%20CARE-Compliant-2ecc71)]()
[![ISO Standards](https://img.shields.io/badge/ISO-9001%20%7C%201915%20%7C%202701-229954)]()
[![Governance Ledger](https://img.shields.io/badge/Governance-Ledger%20Linked-d4af37)]()

</div>

---

## 📚 Overview

The **AI Metadata Prompt Library** governs the automated generation of metadata from AI-derived treaty outputs.  
These prompts instruct models to produce **complete, machine-validated, and semantically rich** metadata following FAIR+CARE and ISO quality standards.

Prompts cover:
- Metadata field extraction  
- STAC/DCAT record generation  
- Provenance embedding (PROV-O / CIDOC CRM)  
- FAIR+CARE ethical metadata verification  

> 🧩 *Every dataset, output, or report in the KFM system must be accompanied by metadata generated through these standardized AI prompts.*

---

## 🗂️ Directory Layout

```
data/work/staging/tabular/normalized/treaties/reports/ai/prompts/metadata/
├── stac_metadata.txt
├── dcat_record_generation.txt
├── provenance_embedding.txt
├── faircare_audit_prompt.txt
├── iso_quality_metadata.txt
├── prompt_registry.json
└── provenance_links.jsonld
```

---

## 🧠 Example Prompt: `stac_metadata.txt`

```
You are a data catalog specialist using the FAIR and STAC 1.0 frameworks.

Generate a STAC-compliant metadata record for the provided dataset.

Include:
- id, title, description
- license, keywords, datetime
- bbox, geometry, CRS
- providers (author, organization)
- links (provenance, data, documentation)

Ensure all metadata follows JSON schema validation and includes:
- FAIR and CARE compliance annotations
- CIDOC CRM provenance references
- ISO 19115 geographic descriptors
```

---

## 🧩 Example Prompt: `faircare_audit_prompt.txt`

```
Perform a FAIR+CARE metadata audit on the following dataset record.

For each metadata field, provide:
- FAIR assessment: F, A, I, R (0–1 score)
- CARE assessment: C, A, R, E (0–1 score)
- Compliance comment and improvement suggestion

Return output as JSON with fields:
{
  "field": "",
  "fair_score": 0.95,
  "care_score": 0.97,
  "comment": "Metadata is accessible and ethically described."
}
```

---

## 🧾 Prompt Registry Schema

| Field | Description | Example |
| :------ | :------------ | :----------- |
| `prompt_id` | Unique prompt identifier | `"metadata_stac_v1"` |
| `category` | Type of metadata operation | `"metadata_generation"` |
| `model_ref` | AI model reference | `"gpt-5-metadata-engine"` |
| `standard_alignment` | Referenced standards | `"STAC 1.0 / DCAT 3.0 / ISO 19115"` |
| `checksum_sha256` | SHA-256 hash for integrity | `"f9b4a13e9d..."` |
| `ethical_rating` | FAIR+CARE compliance grade | `"PASS"` |
| `governance_ref` | Link to provenance metadata | `"provenance_links.jsonld"` |

---

## 🧾 Example Prompt Registry Entry

```json
{
  "prompt_id": "metadata_stac_v1",
  "category": "metadata_generation",
  "model_ref": "gpt-5-metadata-engine",
  "standard_alignment": "STAC 1.0 / DCAT 3.0 / ISO 19115",
  "checksum_sha256": "f9b4a13e9d72...",
  "ethical_rating": "PASS",
  "governance_ref": "provenance_links.jsonld"
}
```

---

## 🔗 Provenance Integration

**File:** `provenance_links.jsonld`
```json
{
  "@context": {
    "prov": "http://www.w3.org/ns/prov#",
    "crm": "http://www.cidoc-crm.org/cidoc-crm/",
    "fair": "https://purl.org/fair/"
  },
  "@id": "prov:ai_metadata_prompt_library",
  "prov:wasGeneratedBy": "process:ai-metadata-pipeline",
  "prov:generatedAtTime": "2025-10-24T15:45:00Z",
  "prov:qualifiedAttribution": {
    "prov:agent": "@kfm-ai",
    "prov:role": "metadata_prompt_engineer"
  },
  "fair:ledger_hash": "c8d9e17b3a..."
}
```

---

## 📊 Metadata Standards Integration

| Standard | Description | Key Components |
| :------ | :------------ | :----------- |
| **STAC 1.0** | Spatial and temporal asset cataloging | `bbox`, `datetime`, `geometry`, `assets` |
| **DCAT 3.0** | Dataset and service metadata model | `distribution`, `publisher`, `theme`, `license` |
| **ISO 19115** | Geographic information metadata | `extent`, `CRS`, `responsibleParty` |
| **FAIR+CARE** | Ethical data stewardship | `findable`, `accessible`, `collective_benefit` |
| **CIDOC CRM / PROV-O** | Provenance and knowledge ontology | `wasGeneratedBy`, `used`, `agent`, `entity` |

---

## ⚖️ FAIR+CARE & Ethical Metadata Rules

- Metadata must explicitly state **provenance** (source → activity → agent).  
- Ensure **licensing transparency** and ethical credit attribution.  
- Follow FAIR accessibility scoring (≥ 0.9 required for publication).  
- Audit reports stored in `/reports/fair_audit_results.json`.  

---

## ✅ Compliance Matrix

| Standard | Domain | Compliance |
| :-------- | :-------- | :----------- |
| **FAIR+CARE** | Metadata transparency and governance | ✅ |
| **MCP-DL v6.4.3** | Documentation and prompt structure | ✅ |
| **CIDOC CRM / PROV-O / OWL-Time** | Ontology-based metadata | ✅ |
| **STAC / DCAT / ISO 19115** | Catalog + spatial standards | ✅ |
| **ISO 9001 / 27001 / 50001** | Quality, security, energy governance | ✅ |

---

## 🗓️ Version History

| Version | Date | Changes | Author |
| :------ | :---- | :-------- | :------ |
| v1.0.0 | 2025-10-24 | Created AI Metadata Prompt Library with FAIR+CARE integration, STAC/DCAT alignment, and CIDOC CRM linkage. | @kfm-ai |

---

<div align="center">

[![Metadata Prompts](https://img.shields.io/badge/AI--Prompts-Metadata-6f42c1?style=flat-square)]()
[![FAIR+CARE](https://img.shields.io/badge/FAIR%20%2B%20CARE-Compliant-2ecc71?style=flat-square)]()
[![Ethical AI](https://img.shields.io/badge/Ethical-Metadata%20Governance-d4af37?style=flat-square)]()
[![Ontology](https://img.shields.io/badge/Ontology-CIDOC%20CRM%20%7C%20PROV--O-8a2be2?style=flat-square)]()
[![ISO Standards](https://img.shields.io/badge/ISO-19115%20%7C%202701%20%7C%2050001-229954?style=flat-square)]()

</div>

<!-- MCP-FOOTER-BEGIN
MCP-VERSION: v6.4.3
MCP-TIER: Silver · AI Metadata Prompts
DOC-PATH: data/work/staging/tabular/normalized/treaties/reports/ai/prompts/metadata/README.md
MCP-CERTIFIED: true
FAIR-CARE-COMPLIANT: true
ISO-ALIGNED: true
PROVENANCE-LINKED: true
PROMPT-VALIDATED: true
STAC-DCAT-ALIGNED: true
GOVERNANCE-LEDGER-LINKED: true
GENERATED-BY: KFM-Automation/DocsBot
LAST-VALIDATED: 2025-10-24
MCP-FOOTER-END -->