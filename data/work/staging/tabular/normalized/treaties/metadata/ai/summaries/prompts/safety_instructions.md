---
title: "🛡️ Kansas Frontier Matrix — AI Safety & Ethical Instructions for Treaty Summarization"
path: "data/work/staging/tabular/normalized/treaties/metadata/ai/summaries/prompts/safety_instructions.md"
document_type: "AI Safety Policy · Ethical Prompt Specification"
version: "v2.0.0"
last_updated: "2025-10-25"
review_cycle: "Semi-Annual / Ethics Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "releases/v2.0.0/sbom.spdx.json"
manifest_ref: "releases/v2.0.0/manifest.zip"
license: ["MIT (code)", "CC-BY 4.0 (docs/data)"]
owners: ["@kfm-ai-lab", "@kfm-ethics"]
approvers: ["@kfm-governance", "@kfm-accessibility", "@kfm-validation"]
status: "Production · FAIR+CARE+ISO Aligned"
maturity: "Stable"
mcp_version: "MCP-DL v6.3"
tags: ["AI", "Ethics", "Safety", "Treaty Summarization", "Fairness", "Bias Mitigation", "Cultural Sensitivity"]
---

<div align="center">

# 🛡️ Kansas Frontier Matrix — **AI Safety & Ethical Instructions for Treaty Summarization**  
`data/work/staging/tabular/normalized/treaties/metadata/ai/summaries/prompts/safety_instructions.md`

**Purpose:** Define the ethical, safety, transparency, and fairness guardrails governing AI-driven summarization and validation of historical treaty texts within the **Kansas Frontier Matrix (KFM)**.

[![Docs · MCP-DL v6.3](https://img.shields.io/badge/Docs-MCP--DL%20v6.3-blue)](../../../../../../../../../../../docs/architecture/repo-focus.md)
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Data%20Ethics%20Aligned-lightblue)]()
[![Ethics Council](https://img.shields.io/badge/Review-By%20Ethics%20Council-purple)]()
[![ISO 19115](https://img.shields.io/badge/ISO--19115-Metadata%20Aligned-orange)]()
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-brightgreen)]()

</div>

---

## 🗂️ Directory Layout

```plaintext
prompts/
├── summarization_prompt.md      # Core summarization template (instruction prompt)
├── safety_instructions.md       # Ethical and cultural safeguards ← you are here
├── reviewer_prompts.md          # Prompts for human-in-the-loop validation
├── bias_tests.yaml              # Bias-triggering phrases and exclusion rules
├── config.json                  # Token length, max context, safety parameters
├── metrics.json                 # Prompt performance telemetry
└── README.md                    # Directory index, metadata schema, and CI validation notes
```

---

## 🧭 Overview

The **Safety and Ethics Instructions** define immutable behavioral constraints for any AI system that generates, validates, or summarizes treaty-related data under the Kansas Frontier Matrix.  
This ensures **cultural preservation**, **data sovereignty**, **contextual fairness**, and **historical accuracy**.

This protocol extends the **Master Coder Protocol (MCP-DL v6.3)** and aligns with:
- FAIR + CARE principles for ethical data management  
- ISO 25012 (Data Quality Model) & ISO 19115 (Geospatial Metadata)  
- CIDOC CRM for cultural-heritage semantics  
- PROV-O for provenance and traceability  
- The KFM Ethics Council charter on responsible automation  

---

## ⚖️ Foundational Ethical Principles

| Category | Directive | Enforcement Mechanism |
|-----------|------------|------------------------|
| **Truthfulness** | Maintain factual alignment with canonical treaty records. | Cross-verify all generated text with OCR and verified transcripts. |
| **Cultural Integrity** | Represent Indigenous nations, leaders, and perspectives accurately and respectfully. | Automatic lexical validation and human review approval. |
| **Non-Harm** | Exclude offensive, colonial, or harmful phrasing. | Bias lexicon filters + post-generation human ethics gate. |
| **Transparency** | Document all AI decisions, weights, and context. | Store prompt input/output metadata with rationale in logs. |
| **Traceability** | Attach unique provenance references for every factual claim. | Generate PROV-O links to data sources and reviewer chain. |
| **Accountability** | Ensure human reviewers approve public outputs. | Require at least one validation signature from @kfm-ethics. |
| **Data Sovereignty** | Protect Indigenous intellectual and cultural property rights. | Follow CARE + Local Contexts labeling and consent structures. |
| **Reproducibility** | Deterministic prompts and frozen model seeds for each generation. | Containerized inference logged via MCP job manifest. |

---

## 🧩 AI Safety Configuration (Embedded in Prompts)

Every AI summarization prompt under this module must append these universal safety guards:

```yaml
# === AI Safety Directives (required by KFM Ethics Council) ===
ethical_constraints:
  - "Do not alter, reinterpret, or editorialize any treaty clauses or text."
  - "Avoid speculative or emotional commentary; use verifiable evidence only."
  - "Maintain cultural neutrality and contextual awareness."
  - "Use official tribal names and identifiers per KFM canonical lexicon."
  - "Do not infer or simplify Indigenous governance structures."
  - "Cite provenance for all factual claims using source_id or treaty_ref."
  - "Avoid summarizing sacred or ceremonial information."
  - "Flag content with confidence < 0.85 as 'uncertain'."
  - "Never output personal or culturally restricted data without permission."
  - "Log all reasoning metadata (prompt_id, model_id, seed, checksum)."
```

---

## 🧠 Bias Mitigation Framework

### 1️⃣ Lexical Safety
- Maintain an updatable **“Cultural Lexicon Register”** of historically valid tribal, geographic, and event terms.  
- Filter deprecated, colonial, or biased expressions.  
- Use inclusive phrasing per **KFM Style & Ethics Standard v4.2**.  

### 2️⃣ Narrative Equity
- Balance representation of all treaty participants.  
- Present Indigenous nations as active agents, not passive recipients.  
- Include Indigenous outcomes, not solely U.S. administrative impacts.  

### 3️⃣ Contextual Sensitivity
- Recognize ceremonial, legal, and territorial contexts.  
- Do not abstract or generalize sacred or religious content.  
- Encourage consultative review from Indigenous advisory members.

---

## 🔒 Secure AI Deployment Controls

| Control Layer | Implementation | Monitoring |
|----------------|----------------|-------------|
| **Model Governance** | Model versioning via `ai_registry_ref` in `releases/v*.json`. | SHA-256 checksum verification. |
| **Prompt Integrity** | YAML schemas validated via pre-commit CI. | `make prompts-validate` workflow. |
| **Inference Logging** | All AI runs generate trace files in `/reports/telemetry/logs/`. | AI ethics audit script checks for anomalies. |
| **Human Verification** | Validation via @kfm-ethics before merge to `main`. | Audit metadata stored in Governance Ledger. |

---

## 🧾 Governance & Audit Chain

- **Ethics Council Oversight:** Biannual peer review of AI summaries for adherence to ethical standards.  
- **Governance Ledger Registration:** Each AI inference run emits a `ledger_entry.jsonld` under `/governance/ledger/ai/`.  
- **CI/CD Integration:** Safety validation gates are part of `ai-review.yml` workflow before production deployment.  
- **Incident Escalation:** Any flagged ethical breach triggers automatic rollback and human incident review via `/governance/reports/ethics_incidents/`.

---

## 📈 Validation Metrics

| Metric | Description | Target | Enforcement |
|--------|--------------|---------|-------------|
| **Bias-Free Score** | % of AI outputs without flagged colonial language. | ≥ 98% | `bias_tests.yaml` auto-scan |
| **Cultural Lexicon Accuracy** | Correct tribal/place usage. | ≥ 97% | NLP lexicon check |
| **Factual Integrity** | Alignment with source documents. | ≥ 95% | NER comparison vs. OCR base |
| **Transparency Rate** | AI runs with full logs and provenance links. | 100% | Governance CI validation |
| **Human Review Compliance** | % of summaries with human approval. | 100% | Governance Ledger signatures |

---

## 🧮 Example Safety Log (AI Run Metadata)

```json
{
  "treaty_id": "KS_TREATY_1867_03_MEDICINE_LODGE",
  "model_id": "hf:kfm-summarizer-v3.2",
  "prompt_version": "v6.3.1",
  "safety_checks": ["BiasScanOK", "CulturalLexiconOK", "SourceTraceOK"],
  "human_reviewed": true,
  "confidence": 0.92,
  "governance_ledger_entry": "ledger/ai/2025/10/25/KS_TREATY_1867.jsonld"
}
```

---

## 🧾 Version History

| Version | Date | Author | Reviewer | Notes |
|----------|------|---------|-----------|--------|
| v2.0.0 | 2025-10-25 | @kfm-ai-lab | @kfm-ethics | Full FAIR+CARE schema, ISO alignment, extended governance and audit structure. |
| v1.1.0 | 2025-10-24 | @kfm-ai-lab | @kfm-ethics | Added bias and fairness sections, integrated into reviewer CI. |
| v1.0.0 | 2025-10-23 | @kfm-ai-lab | — | Initial ethical framework for treaty summarization AI. |

---

<div align="center">

[![Docs · MCP-DL v6.3](https://img.shields.io/badge/Docs-MCP--DL%20v6.3-blue)]()
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Compliant-lightblue)]()
[![ISO 25012](https://img.shields.io/badge/ISO--25012-Data%20Quality%20Model-orange)]()
[![Human-in-the-Loop](https://img.shields.io/badge/Review-Human%20Validated-green)]()
[![AI Audit Trail](https://img.shields.io/badge/AI_Audit-Logged-yellow)]()

</div>
