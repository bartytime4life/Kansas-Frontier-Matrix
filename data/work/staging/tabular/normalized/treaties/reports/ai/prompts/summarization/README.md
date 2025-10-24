---
title: "🗣️ Kansas Frontier Matrix — AI Summarization Prompt Library"
path: "data/work/staging/tabular/normalized/treaties/reports/ai/prompts/summarization/README.md"
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
  - ISO 9001 / 27001 / 50001
tags: ["ai","prompts","summarization","nlp","treaties","contextualization","ontology","cidoc","fair","ethics"]
---

<div align="center">

# 🗣️ Kansas Frontier Matrix — **AI Summarization Prompt Library**
`data/work/staging/tabular/normalized/treaties/reports/ai/prompts/summarization/`

**Purpose:** Define **contextual and domain-specific prompt templates** used for AI-driven treaty summarization.  
These prompts standardize how large language models generate reproducible, ethical, and semantically grounded summaries for the Kansas Frontier Matrix.

[![Docs · MCP-DL v6.4.3](https://img.shields.io/badge/Docs-MCP--DL%20v6.4.3-blue)]()
[![Prompt Library](https://img.shields.io/badge/AI--Prompts-Summarization-6f42c1)]()
[![FAIR+CARE](https://img.shields.io/badge/FAIR%20%2B%20CARE-Compliant-2ecc71)]()
[![Ethical AI](https://img.shields.io/badge/Ethical-AI%20Explainable-d4af37)]()
[![ISO Standards](https://img.shields.io/badge/ISO-9001%20%7C%202701%20%7C%2050001-229954)]()

</div>

---

## 📚 Overview

The **Summarization Prompt Library** provides **modular AI instruction templates** used to guide language models during treaty analysis.  
These templates are written in plain text (`.txt`) and are FAIR+CARE compliant to ensure transparent and reproducible content generation.

Prompts are versioned, contextualized, and linked to:
- Historical and geographical metadata  
- FAIR+CARE ethical governance rules  
- CIDOC CRM event entities and OWL-Time temporal anchors  
- Provenance tracking via `provenance_links.jsonld`  

> 🧩 *Every generated summary must trace its origin to a prompt defined and versioned in this directory.*

---

## 🗂️ Directory Layout

```
data/work/staging/tabular/normalized/treaties/reports/ai/prompts/summarization/
├── base_summary.txt
├── historical_context.txt
├── comparative_analysis.txt
├── indigenous_perspective.txt
├── sustainability_impact.txt
├── prompt_registry.json
└── provenance_links.jsonld
```

---

## 🧠 Example Prompt Template

**File:** `base_summary.txt`

```
You are an expert in historical treaties and cultural heritage analysis.

Summarize the following treaty document in structured Markdown format:
- Highlight its purpose, date, and primary signatories.
- Explain its geopolitical and social implications within 19th-century Kansas.
- Identify any Indigenous nations involved, along with land-use or sovereignty outcomes.
- Provide a concise, factual overview (max 300 words).

Style:
- Neutral, factual, academic tone.
- Use clear section headers.
- Preserve historical accuracy and data lineage references.

Input: {{treaty_text}}
Output: Markdown-formatted summary.
```

---

## 💡 Specialized Prompts

| Prompt | Focus | Description |
| :------ | :------ | :----------- |
| `historical_context.txt` | Contextual grounding | Adds regional and period-based background using historical GIS data |
| `comparative_analysis.txt` | Cross-document comparison | Aligns treaties chronologically or by thematic similarity |
| `indigenous_perspective.txt` | Ethical inclusion | Highlights Indigenous agency and impact narratives |
| `sustainability_impact.txt` | Environmental insight | Evaluates environmental and land-use outcomes tied to treaty clauses |

---

## 🧩 Prompt Registry Schema

| Field | Description | Example |
| :------ | :------------ | :----------- |
| `prompt_id` | Unique identifier for the prompt | `"summary_v1_1854"` |
| `category` | Context domain | `"summarization"` |
| `model_ref` | Associated model | `"gpt-5-treaty-sum"` |
| `language` | Primary language | `"en"` |
| `context_scope` | Dataset or period scope | `"Kansas Treaties 1850–1870"` |
| `checksum_sha256` | Hash for prompt file verification | `"b19a8d47f9..."` |
| `ethical_rating` | FAIR+CARE compliance grade | `"PASS"` |
| `governance_ref` | Governance linkage file | `"provenance_links.jsonld"` |

---

## 🧾 Example Prompt Registry Entry

```json
{
  "prompt_id": "summary_v1_1854",
  "category": "summarization",
  "model_ref": "gpt-5-treaty-sum",
  "language": "en",
  "context_scope": "Kansas Treaties 1850–1870",
  "checksum_sha256": "b19a8d47f9a4e2...",
  "ethical_rating": "PASS",
  "governance_ref": "provenance_links.jsonld"
}
```

---

## 🔐 Governance & Provenance Linkage

**File:** `provenance_links.jsonld`
```json
{
  "@context": {
    "prov": "http://www.w3.org/ns/prov#",
    "crm": "http://www.cidoc-crm.org/cidoc-crm/",
    "fair": "https://purl.org/fair/"
  },
  "@id": "prov:ai_prompt_summarization_library",
  "prov:wasGeneratedBy": "process:ai-prompt-curation",
  "prov:generatedAtTime": "2025-10-24T14:55:00Z",
  "prov:qualifiedAttribution": {
    "prov:agent": "@kfm-ai",
    "prov:role": "prompt_engineer"
  },
  "fair:ledger_hash": "a93d7c81b5..."
}
```

---

## 🧩 Ethical Standards (FAIR+CARE Integration)

- Prompts are **transparently versioned** and traceable.
- Include **decolonial framing** and respect Indigenous data sovereignty.
- Avoid biasing output tone, sentiment, or interpretation.
- Ensure **consistency in historical representation** using cross-referenced archival metadata.

---

## ✅ Compliance Matrix

| Standard | Domain | Compliance |
| :-------- | :-------- | :----------- |
| **FAIR+CARE** | Ethical + transparent prompt engineering | ✅ |
| **MCP-DL v6.4.3** | Documentation standard alignment | ✅ |
| **CIDOC CRM / PROV-O** | Provenance and contextual ontology | ✅ |
| **ISO 9001 / 27001 / 50001** | Quality + ethical AI governance | ✅ |

---

## 🗓️ Version History

| Version | Date | Changes | Author |
| :------ | :---- | :-------- | :------ |
| v1.0.0 | 2025-10-24 | Created AI Summarization Prompt Library with FAIR+CARE + ethical governance integration. | @kfm-ai |

---

<div align="center">

[![Summarization Prompts](https://img.shields.io/badge/Prompts-Summarization%20Library-6f42c1?style=flat-square)]()
[![Ethical AI](https://img.shields.io/badge/Ethical-AI%20Explainable-d4af37?style=flat-square)]()
[![FAIR+CARE](https://img.shields.io/badge/FAIR%20%2B%20CARE-Compliant-2ecc71?style=flat-square)]()
[![Ontology](https://img.shields.io/badge/Ontology-CIDOC%20CRM%20%7C%20PROV--O-8a2be2?style=flat-square)]()
[![ISO Standards](https://img.shields.io/badge/ISO-9001%20%7C%202701%20%7C%2050001-229954?style=flat-square)]()

</div>

<!-- MCP-FOOTER-BEGIN
MCP-VERSION: v6.4.3
MCP-TIER: Silver · AI Summarization Prompts
DOC-PATH: data/work/staging/tabular/normalized/treaties/reports/ai/prompts/summarization/README.md
MCP-CERTIFIED: true
FAIR-CARE-COMPLIANT: true
ISO-ALIGNED: true
PROVENANCE-LINKED: true
PROMPT-VALIDATED: true
GOVERNANCE-LEDGER-LINKED: true
GENERATED-BY: KFM-Automation/DocsBot
LAST-VALIDATED: 2025-10-24
MCP-FOOTER-END -->