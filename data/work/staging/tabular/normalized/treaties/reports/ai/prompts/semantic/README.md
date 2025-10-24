---
title: "🧬 Kansas Frontier Matrix — AI Semantic Mapping Prompt Library"
path: "data/work/staging/tabular/normalized/treaties/reports/ai/prompts/semantic/README.md"
version: "v1.0.0"
last_updated: "2025-10-24"
review_cycle: "Continuous / Adaptive"
status: "Active · FAIR+CARE+ISO Aligned"
mcp_version: "MCP-DL v6.4.3"
maintainers: ["@kfm-ai", "@kfm-data", "@kfm-validation"]
approvers: ["@kfm-architecture", "@kfm-ethics", "@kfm-governance"]
license: ["MIT (code)", "CC-BY 4.0 (data/docs)"]
alignment:
  - FAIR / CARE
  - CIDOC CRM / PROV-O / OWL-Time / GeoSPARQL
  - ISO 9001 / 19115 / 27001 / 50001
tags: ["ai","semantic","prompts","ontology","cidoc","prov-o","owl-time","rdf","fair","governance","iso"]
---

<div align="center">

# 🧬 Kansas Frontier Matrix — **AI Semantic Mapping Prompt Library**
`data/work/staging/tabular/normalized/treaties/reports/ai/prompts/semantic/`

**Purpose:** Define **AI-assisted semantic mapping and ontology alignment prompts** that guide large language models in classifying, linking, and contextualizing entities (people, places, events) according to **CIDOC CRM, PROV-O, and OWL-Time** standards.

[![Docs · MCP-DL v6.4.3](https://img.shields.io/badge/Docs-MCP--DL%20v6.4.3-blue)]()
[![Semantic Prompts](https://img.shields.io/badge/AI--Prompts-Semantic%20Mapping-6f42c1)]()
[![FAIR+CARE](https://img.shields.io/badge/FAIR%20%2B%20CARE-Compliant-2ecc71)]()
[![ISO Standards](https://img.shields.io/badge/ISO-9001%20%7C%201915%20%7C%202701-229954)]()
[![Ontology](https://img.shields.io/badge/Ontology-CIDOC%20CRM%20%7C%20PROV--O%20%7C%20OWL--Time-8a2be2)]()

</div>

---

## 📚 Overview

The **AI Semantic Prompt Library** enables structured entity recognition, classification, and temporal reasoning within treaty datasets.  
These prompt templates are designed to ensure:
- Semantic precision across ontology frameworks  
- FAIR+CARE-compliant metadata enrichment  
- Temporal and spatial normalization using OWL-Time and GeoSPARQL  
- Reproducible alignment between unstructured AI outputs and KFM’s knowledge graph  

> 🧩 *All semantic extraction prompts follow CIDOC CRM ontology models to ensure data interoperability and provenance continuity.*

---

## 🗂️ Directory Layout

```
data/work/staging/tabular/normalized/treaties/reports/ai/prompts/semantic/
├── ontology_mapping.txt
├── entity_linking.txt
├── temporal_normalization.txt
├── spatial_contextualization.txt
├── semantic_validation.txt
├── prompt_registry.json
└── provenance_links.jsonld
```

---

## 🧠 Example Prompt: `ontology_mapping.txt`

```
You are an ontology alignment specialist.

Task:
Map the following dataset entities (People, Places, Events, Documents) to their corresponding ontology classes.

Frameworks:
- CIDOC CRM (E21_Person, E53_Place, E5_Event, E31_Document)
- PROV-O (Entity, Activity, Agent)
- OWL-Time (Instant, Interval)

Requirements:
- Preserve entity names and references.
- Ensure temporal consistency using OWL-Time intervals.
- Return mappings in JSON-LD format with "@type" fields defined.
- Include confidence scores between 0 and 1 for each mapping.

Input: {{entity_data}}
Output: JSON-LD structured ontology mappings.
```

---

## 🧩 Example Prompt: `temporal_normalization.txt`

```
Normalize temporal information extracted from treaty documents.

Task:
1. Detect all explicit and implicit time references (dates, durations, eras).
2. Represent temporal data using OWL-Time concepts:
   - time:Instant (for singular dates)
   - time:Interval (for continuous durations)
3. Format output as JSON-LD using:
   "@context": "http://www.w3.org/2006/time#"
   "@type": "time:TemporalEntity"

Ensure all outputs link back to corresponding treaty metadata (via treaty_id).
```

---

## 💡 Prompt Registry Schema

| Field | Description | Example |
| :------ | :------------ | :----------- |
| `prompt_id` | Unique identifier for prompt | `"semantic_map_v1_ontology"` |
| `category` | Functional class of prompt | `"semantic_mapping"` |
| `model_ref` | Associated AI model | `"gpt-5-semantic-mapper"` |
| `ontology_ref` | Ontologies applied | `"CIDOC CRM / PROV-O / OWL-Time"` |
| `language` | Working language | `"en"` |
| `checksum_sha256` | File hash for validation | `"d39b4e2a9c..."` |
| `ethical_rating` | FAIR+CARE compliance | `"PASS"` |
| `governance_ref` | Provenance and ledger reference | `"provenance_links.jsonld"` |

---

## 🧾 Example Prompt Registry Entry

```json
{
  "prompt_id": "semantic_map_v1_ontology",
  "category": "semantic_mapping",
  "model_ref": "gpt-5-semantic-mapper",
  "ontology_ref": "CIDOC CRM / PROV-O / OWL-Time",
  "language": "en",
  "checksum_sha256": "d39b4e2a9c3a7e...",
  "ethical_rating": "PASS",
  "governance_ref": "provenance_links.jsonld"
}
```

---

## 🔐 Provenance Integration

**File:** `provenance_links.jsonld`
```json
{
  "@context": {
    "prov": "http://www.w3.org/ns/prov#",
    "crm": "http://www.cidoc-crm.org/cidoc-crm/",
    "fair": "https://purl.org/fair/"
  },
  "@id": "prov:ai_semantic_prompt_library",
  "prov:wasGeneratedBy": "process:ai-semantic-mapping-pipeline",
  "prov:generatedAtTime": "2025-10-24T15:30:00Z",
  "prov:qualifiedAttribution": {
    "prov:agent": "@kfm-ai",
    "prov:role": "semantic_prompt_engineer"
  },
  "fair:ledger_hash": "b79d4e8c42..."
}
```

---

## 🧬 Ontology Contexts

| Framework | Description | Example Classes |
| :------ | :------------ | :----------- |
| **CIDOC CRM** | Heritage ontology for cultural data | `E21_Person`, `E53_Place`, `E5_Event` |
| **PROV-O** | Provenance ontology for AI processes | `Entity`, `Agent`, `Activity` |
| **OWL-Time** | Temporal reasoning ontology | `Instant`, `Interval` |
| **GeoSPARQL** | Spatial relationships ontology | `Feature`, `Geometry`, `SpatialObject` |

---

## ✅ Ethical & FAIR+CARE Standards

- Prompts are **openly documented** and **reproducible**.
- All model instructions are **ontology-explicit** and **bias-audited**.
- Semantic grounding aligns with **FAIR Principles (Findable, Accessible, Interoperable, Reusable)**.
- Cultural and historical context handled under **CARE (Collective Benefit, Authority, Responsibility, Ethics)**.

---

## ✅ Compliance Matrix

| Standard | Domain | Compliance |
| :-------- | :-------- | :----------- |
| **FAIR+CARE** | Ethical data governance | ✅ |
| **MCP-DL v6.4.3** | Documentation standardization | ✅ |
| **CIDOC CRM / PROV-O / OWL-Time** | Ontology compliance | ✅ |
| **ISO 9001 / 19115 / 27001 / 50001** | Quality, metadata, and energy governance | ✅ |

---

## 🗓️ Version History

| Version | Date | Changes | Author |
| :------ | :---- | :-------- | :------ |
| v1.0.0 | 2025-10-24 | Created AI Semantic Mapping Prompt Library for ontology alignment and FAIR+CARE governance. | @kfm-ai |

---

<div align="center">

[![Semantic Prompts](https://img.shields.io/badge/AI--Prompts-Semantic%20Mapping-6f42c1?style=flat-square)]()
[![Ontology](https://img.shields.io/badge/Ontology-CIDOC%20CRM%20%7C%20PROV--O%20%7C%20OWL--Time-8a2be2?style=flat-square)]()
[![FAIR+CARE](https://img.shields.io/badge/FAIR%20%2B%20CARE-Compliant-2ecc71?style=flat-square)]()
[![Ethical AI](https://img.shields.io/badge/Ethical-AI%20Explainable-d4af37?style=flat-square)]()
[![ISO Standards](https://img.shields.io/badge/ISO-9001%20%7C%201915%20%7C%202701-229954?style=flat-square)]()

</div>

<!-- MCP-FOOTER-BEGIN
MCP-VERSION: v6.4.3
MCP-TIER: Silver · AI Semantic Prompts
DOC-PATH: data/work/staging/tabular/normalized/treaties/reports/ai/prompts/semantic/README.md
MCP-CERTIFIED: true
FAIR-CARE-COMPLIANT: true
ISO-ALIGNED: true
ONTOLOGY-LINKED: true
PROVENANCE-LINKED: true
PROMPT-VALIDATED: true
GOVERNANCE-LEDGER-LINKED: true
GENERATED-BY: KFM-Automation/DocsBot
LAST-VALIDATED: 2025-10-24
MCP-FOOTER-END -->