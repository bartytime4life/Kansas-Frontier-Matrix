---
title: "🔍 Kansas Frontier Matrix — AI NER Extraction Prompt Library"
path: "data/work/staging/tabular/normalized/treaties/reports/ai/prompts/ner_extraction/README.md"
version: "v1.0.0"
last_updated: "2025-10-24"
review_cycle: "Continuous / Adaptive"
status: "Active · FAIR+CARE+ISO Aligned"
mcp_version: "MCP-DL v6.4.3"
maintainers: ["@kfm-ai", "@kfm-data", "@kfm-treaties"]
approvers: ["@kfm-architecture", "@kfm-ethics", "@kfm-governance"]
license: ["MIT (code)", "CC-BY 4.0 (data/docs)"]
alignment:
  - FAIR / CARE
  - STAC / DCAT
  - CIDOC CRM / PROV-O / OWL-Time
  - ISO 9001 / 19115 / 27001 / 50001
tags: ["ai","nlp","ner","entity-extraction","prompts","ontology","cidoc","prov-o","fair","iso"]
---

<div align="center">

# 🔍 Kansas Frontier Matrix — **AI Named Entity Recognition (NER) Prompt Library**
`data/work/staging/tabular/normalized/treaties/reports/ai/prompts/ner_extraction/`

**Purpose:** Define and document **prompt templates** that guide AI models to perform **Named Entity Recognition (NER)** and classification for treaty documents, with semantic linkage to **CIDOC CRM**, **PROV-O**, and **OWL-Time** frameworks.

[![Docs · MCP-DL v6.4.3](https://img.shields.io/badge/Docs-MCP--DL%20v6.4.3-blue)]()
[![NER Prompts](https://img.shields.io/badge/AI--Prompts-NER%20Extraction-6f42c1)]()
[![FAIR+CARE](https://img.shields.io/badge/FAIR%20%2B%20CARE-Compliant-2ecc71)]()
[![Ethical AI](https://img.shields.io/badge/Ethical-AI%20Explainable-d4af37)]()
[![ISO Standards](https://img.shields.io/badge/ISO-9001%20%7C%202701%20%7C%2050001-229954)]()

</div>

---

## 📚 Overview

The **NER Prompt Library** provides standardized **prompt instructions** for entity extraction and classification across Kansas Frontier Matrix treaty datasets.  
These templates ensure that all entity recognition aligns with **FAIR+CARE**, **CIDOC CRM ontology**, and **ethical AI** standards.

Entities include:
- **People (E21_Person)**  
- **Places (E53_Place)**  
- **Events (E5_Event)**  
- **Documents (E31_Document)**  
- **Organizations / Authorities**

> 🧩 *All recognized entities are linked to ontology identifiers and include provenance metadata for validation and reproducibility.*

---

## 🗂️ Directory Layout

```
data/work/staging/tabular/normalized/treaties/reports/ai/prompts/ner_extraction/
├── person_extraction.txt
├── place_extraction.txt
├── event_mapping.txt
├── organization_identification.txt
├── treaty_reference_extraction.txt
├── prompt_registry.json
└── provenance_links.jsonld
```

---

## 🧠 Example Prompt: `person_extraction.txt`

```
Extract all personal names mentioned in the following treaty text.

Return each entry as a JSON object including:
- "person_name": string
- "role": string (e.g., negotiator, signatory, representative)
- "affiliation": string (organization or nation)
- "linked_identifier": string (e.g., VIAF, Wikidata, or local ID)
- "confidence_score": float (0–1)
- "context_excerpt": string (relevant text snippet)

Output Format:
[
  {
    "person_name": "Franklin Pierce",
    "role": "President of the United States",
    "affiliation": "United States Government",
    "linked_identifier": "wikidata:Q11812",
    "confidence_score": 0.98,
    "context_excerpt": "Signed on behalf of the United States by President Franklin Pierce..."
  }
]
```

---

## 🧭 Example Prompt: `place_extraction.txt`

```
Identify all geographic references within the treaty text.

Classify each place according to CIDOC CRM and GeoSPARQL:
- "place_name": string
- "geographic_type": string (territory | river | region | settlement)
- "linked_identifier": string (GNIS, GeoNames, or internal reference)
- "coordinates": string (latitude, longitude if available)
- "context_excerpt": string (text surrounding mention)

Return JSON format suitable for knowledge graph ingestion.
```

---

## 🧩 Example Prompt: `event_mapping.txt`

```
Map all events mentioned in the treaty (negotiations, ratifications, conflicts, enactments).

Each event must follow the CIDOC CRM model:
{
  "event_label": "",
  "@type": "E5_Event",
  "time:hasBeginning": "",
  "time:hasEnd": "",
  "location": "",
  "participants": [],
  "related_documents": [],
  "context": ""
}

Ensure consistency with OWL-Time and CIDOC temporal structure.
```

---

## 🧾 Prompt Registry Schema

| Field | Description | Example |
| :------ | :------------ | :----------- |
| `prompt_id` | Unique prompt identifier | `"ner_place_extraction_v1"` |
| `category` | Task category | `"entity_extraction"` |
| `model_ref` | Model used | `"gpt-5-ner-treaty"` |
| `language` | Working language | `"en"` |
| `ontology_ref` | Ontology frameworks applied | `"CIDOC CRM / GeoSPARQL / OWL-Time"` |
| `checksum_sha256` | Prompt file hash | `"a57d4b3e2f..."` |
| `ethical_rating` | FAIR+CARE compliance grade | `"PASS"` |
| `governance_ref` | Governance linkage | `"provenance_links.jsonld"` |

---

## 🧾 Example Registry Entry

```json
{
  "prompt_id": "ner_place_extraction_v1",
  "category": "entity_extraction",
  "model_ref": "gpt-5-ner-treaty",
  "language": "en",
  "ontology_ref": "CIDOC CRM / GeoSPARQL / OWL-Time",
  "checksum_sha256": "a57d4b3e2fb4c9...",
  "ethical_rating": "PASS",
  "governance_ref": "provenance_links.jsonld"
}
```

---

## 🔗 Provenance Metadata

**File:** `provenance_links.jsonld`
```json
{
  "@context": {
    "prov": "http://www.w3.org/ns/prov#",
    "crm": "http://www.cidoc-crm.org/cidoc-crm/",
    "fair": "https://purl.org/fair/"
  },
  "@id": "prov:ai_prompt_ner_library",
  "prov:wasGeneratedBy": "process:ai-ner-prompt-engineering",
  "prov:generatedAtTime": "2025-10-24T15:40:00Z",
  "prov:qualifiedAttribution": {
    "prov:agent": "@kfm-ai",
    "prov:role": "ner_prompt_engineer"
  },
  "fair:ledger_hash": "e5b9d71a3b..."
}
```

---

## ⚖️ Ethical & FAIR+CARE Principles

- Prompts ensure **data neutrality** and factual representation.  
- Entity extraction prioritizes **cultural sensitivity** and **ethical grounding**.  
- Outputs are **traceable, reproducible, and machine-interpretable**.  
- All derived entities carry **provenance metadata and confidence scores**.

---

## ✅ Compliance Matrix

| Standard | Domain | Compliance |
| :-------- | :-------- | :----------- |
| **FAIR+CARE** | Ethical AI + provenance traceability | ✅ |
| **MCP-DL v6.4.3** | Documentation and schema governance | ✅ |
| **CIDOC CRM / PROV-O / OWL-Time** | Ontology + temporal alignment | ✅ |
| **ISO 9001 / 19115 / 27001 / 50001** | Quality, security, and sustainability | ✅ |

---

## 🗓️ Version History

| Version | Date | Changes | Author |
| :------ | :---- | :-------- | :------ |
| v1.0.0 | 2025-10-24 | Created AI NER Extraction Prompt Library for entity-level semantic extraction and ontology linking. | @kfm-ai |

---

<div align="center">

[![NER Prompts](https://img.shields.io/badge/AI--Prompts-NER%20Extraction-6f42c1?style=flat-square)]()
[![Ontology](https://img.shields.io/badge/Ontology-CIDOC%20CRM%20%7C%20PROV--O%20%7C%20OWL--Time-8a2be2?style=flat-square)]()
[![FAIR+CARE](https://img.shields.io/badge/FAIR%20%2B%20CARE-Compliant-2ecc71?style=flat-square)]()
[![Ethical AI](https://img.shields.io/badge/Ethical-AI%20Explainable-d4af37?style=flat-square)]()
[![ISO Standards](https://img.shields.io/badge/ISO-9001%20%7C%201915%20%7C%202701-229954?style=flat-square)]()

</div>

<!-- MCP-FOOTER-BEGIN
MCP-VERSION: v6.4.3
MCP-TIER: Silver · AI NER Extraction Prompts
DOC-PATH: data/work/staging/tabular/normalized/treaties/reports/ai/prompts/ner_extraction/README.md
MCP-CERTIFIED: true
FAIR-CARE-COMPLIANT: true
ISO-ALIGNED: true
PROVENANCE-LINKED: true
PROMPT-VALIDATED: true
GOVERNANCE-LEDGER-LINKED: true
GENERATED-BY: KFM-Automation/DocsBot
LAST-VALIDATED: 2025-10-24
MCP-FOOTER-END -->