---
title: "💬 Kansas Frontier Matrix — AI Treaty Report Prompts"
path: "data/work/staging/tabular/normalized/treaties/reports/ai/prompts/README.md"
version: "v1.0.0"
last_updated: "2025-10-24"
review_cycle: "Continuous / Autonomous"
status: "Active · FAIR+CARE+ISO Aligned"
mcp_version: "MCP-DL v6.4.3"
maintainers: ["@kfm-ai", "@kfm-data", "@kfm-treaties"]
approvers: ["@kfm-architecture", "@kfm-ethics", "@kfm-governance"]
license: ["MIT (code)", "CC-BY 4.0 (data/docs)"]
alignment:
  - FAIR / CARE
  - STAC / DCAT
  - CIDOC CRM / OWL-Time / PROV-O
  - ISO 9001 / ISO 27001 / ISO 50001 / ISO 14064
tags: ["ai","prompts","treaties","nlp","llm","summarization","contextualization","cidoc","ontology","fair"]
---

<div align="center">

# 💬 Kansas Frontier Matrix — **AI Treaty Report Prompts**
`data/work/staging/tabular/normalized/treaties/reports/ai/prompts/README.md`

**Purpose:** Define and document the **prompt templates, configurations, and contextual schemas** used by the AI inference pipelines for generating **treaty summaries, entity extractions, and semantic analyses**.

[![Docs · MCP-DL v6.4.3](https://img.shields.io/badge/Docs-MCP--DL%20v6.4.3-blue)]()
[![AI Prompts](https://img.shields.io/badge/AI-Prompt%20Library-6f42c1)]()
[![FAIR+CARE](https://img.shields.io/badge/FAIR%20%2B%20CARE-Compliant-2ecc71)]()
[![ISO Standards](https://img.shields.io/badge/ISO-9001%20%7C%202701%20%7C%2050001-229954)]()
[![Ethics](https://img.shields.io/badge/Ethics-Transparent%20AI%20Generation-d4af37)]()

</div>

---

## 📚 Overview

The **AI Treaty Report Prompts Module** defines the controlled **instruction sets and contextual templates** used during AI generation.  
Prompts are versioned, reproducible, and linked to their corresponding **model configurations**, ensuring consistent and explainable AI output across treaty reports.

> ⚖️ *All prompts must adhere to KFM’s ethical guidelines for AI explainability, neutrality, and historical fidelity.*

---

## 🗂️ Directory Layout

```
data/work/staging/tabular/normalized/treaties/reports/ai/prompts/
├── summarization/                   # Treaty summary prompt templates
│   ├── base_summary.txt
│   ├── historical_context.txt
│   └── comparative_analysis.txt
├── ner_extraction/                  # Entity recognition and linking prompts
│   ├── person_extraction.txt
│   ├── place_extraction.txt
│   └── event_mapping.txt
├── semantic/                        # CIDOC/OWL-Time contextual prompts
│   ├── ontology_mapping.txt
│   └── temporal_normalization.txt
├── governance/                      # FAIR/CARE compliance and bias evaluation
│   ├── ethics_review.txt
│   └── governance_summary.txt
└── metadata/                        # Model-to-prompt linkage records
    └── prompt_registry.json
```

---

## 🧩 Prompt Registry Schema

| Field | Type | Description |
| :------ | :------ | :------------ |
| `prompt_id` | string | Unique identifier for the prompt |
| `category` | string | Type of prompt (e.g., summarization, NER, semantic) |
| `model_ref` | string | Model using this prompt (from `ai/models/registry/`) |
| `language` | string | Natural language used for instructions |
| `version` | string | Prompt schema version |
| `contextual_scope` | string | Scope of use (treaty, entity, region, era) |
| `checksum_sha256` | string | Checksum for reproducibility |
| `ethical_rating` | string | AI ethics evaluation (PASS / REVIEW / FAIL) |
| `governance_ref` | string | Link to audit/governance record |

---

## 💡 Example Prompt Template (Summarization)

**File:** `summarization/base_summary.txt`

```
You are a historical analysis assistant specializing in 19th-century treaties of the Central Plains region.

Summarize the following treaty document:
- Focus on its geopolitical context, primary signatories, and long-term effects.
- Include key events, locations, and Indigenous nations involved.
- Maintain a neutral and factual tone.
- Conclude with the treaty’s significance in Kansas territorial development.

Input Data: {{treaty_text}}
Output Format: Markdown
```

---

## 🧠 Example NER Extraction Prompt

**File:** `ner_extraction/place_extraction.txt`

```
Identify all places and geographic references mentioned in the following treaty text.
Return a list of objects in JSON format, each including:
{
  "place_name": "",
  "geographic_type": "territory | river | settlement | boundary",
  "linked_identifier": "GNIS or GeoNames ID",
  "context_excerpt": ""
}
```

---

## 🧾 Metadata Linkage Example (`prompt_registry.json`)

```json
{
  "prompt_id": "summary_v1_1854",
  "category": "summarization",
  "model_ref": "gpt-5-treaty-sum",
  "language": "en",
  "version": "1.0.0",
  "contextual_scope": "Kansas Treaties 1850–1870",
  "checksum_sha256": "9f3b4f17b6...4df8a",
  "ethical_rating": "PASS",
  "governance_ref": "data/governance/audits/prompt_1854_audit.json"
}
```

---

## 🧪 Validation Process

| Validation Type | Description | Tool | Output |
| :---------------- | :------------ | :---------- | :----------- |
| Schema Validation | Checks JSON registry compliance | `jsonschema-cli` | `prompt_schema_validation.json` |
| Ethics Review | Evaluates neutrality and inclusivity | `ai-ethics-linter` | `ethics_audit.json` |
| Provenance Validation | Confirms linkage to model + ledger | `pyshacl` | `prompt_provenance.jsonld` |
| Checksum Verification | Validates immutability | `sha256sum` | `prompt_checksums.log` |

---

## 🧬 Ethical Prompt Design Rules

- Prompts must:
  - Avoid subjective or politically charged phrasing.  
  - Reference primary data sources directly (no inferred facts).  
  - Provide explicit structure for model outputs.  
  - Include historical disambiguation (dates, signatories, geography).  
  - Contain embedded fairness statements where applicable.  

- All updates to prompt text must be reviewed by:
  - `@kfm-ethics`
  - `@kfm-architecture`
  - `@kfm-ai`

---

## 🧩 Governance Integration

| System | Description | Artifact |
| :-------- | :------------ | :----------- |
| FAIR Ledger | Tracks prompt lineage and provenance | `prompt_fair_manifest.json` |
| Ethics Ledger | Logs AI fairness and neutrality audits | `prompt_ethics_audit.json` |
| Governance Ledger | Records prompt updates and versioning | `prompt_manifest.json` |
| Model Registry | Cross-links prompt to model metadata | `ai/models/registry/*.json` |

---

## ✅ Compliance Matrix

| Standard | Area | Compliance |
| :-------- | :-------- | :----------- |
| **FAIR+CARE** | Ethical data and AI governance | ✅ |
| **MCP-DL v6.4.3** | Documentation alignment | ✅ |
| **CIDOC CRM / PROV-O** | Provenance model | ✅ |
| **ISO 9001** | Quality management | ✅ |
| **ISO 27001** | Security baseline | ✅ |
| **ISO 50001 / 14064** | Sustainability & ethics | ✅ |

---

## 🗓️ Version History

| Version | Date | Changes | Author |
| :------ | :---- | :-------- | :------ |
| v1.0.0 | 2025-10-24 | Created AI Treaty Report Prompts module with FAIR+CARE and ethics linkage. | @kfm-ai |

---

<div align="center">

[![AI Prompts](https://img.shields.io/badge/AI--Prompts-Versioned%20%26%20Validated-6f42c1?style=flat-square)]()
[![Ethical AI](https://img.shields.io/badge/Ethics-Transparent%20AI%20Design-d4af37?style=flat-square)]()
[![FAIR+CARE](https://img.shields.io/badge/FAIR%20%2B%20CARE-Compliant-2ecc71?style=flat-square)]()
[![ISO Standards](https://img.shields.io/badge/ISO-9001%20%7C%202701%20%7C%2050001-229954?style=flat-square)]()
[![Governance Ledger](https://img.shields.io/badge/Governance-Immutable%20Linked-d4af37?style=flat-square)]()

</div>

<!-- MCP-FOOTER-BEGIN
MCP-VERSION: v6.4.3
MCP-TIER: Silver · AI Prompts
DOC-PATH: data/work/staging/tabular/normalized/treaties/reports/ai/prompts/README.md
MCP-CERTIFIED: true
FAIR-CARE-COMPLIANT: true
ISO-ALIGNED: true
ETHICAL-AI-VERIFIED: true
PROVENANCE-LINKED: true
PROMPTS-VERSIONED: true
MODEL-REGISTRY-LINKED: true
GOVERNANCE-LEDGER-LINKED: true
GENERATED-BY: KFM-Automation/DocsBot
LAST-VALIDATED: 2025-10-24
MCP-FOOTER-END -->