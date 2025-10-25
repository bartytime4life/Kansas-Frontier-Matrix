---
title: "🤖 Kansas Frontier Matrix — AI Reviewer Prompts for Treaty Summaries"
path: "data/work/staging/tabular/normalized/treaties/metadata/ai/summaries/prompts/reviewer_prompts.md"
document_type: "AI Validation · Reviewer Prompt Specification"
version: "v1.2.0"
last_updated: "2025-10-25"
review_cycle: "Quarterly / Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "releases/v1.2.0/sbom.spdx.json"
manifest_ref: "releases/v1.2.0/manifest.zip"
license: ["MIT (code)", "CC-BY 4.0 (data/docs)"]
owners: ["@kfm-ai-lab", "@kfm-architecture"]
approvers: ["@kfm-validation", "@kfm-governance"]
status: "Production · FAIR+CARE+ISO Aligned"
mcp_version: "MCP-DL v6.3"
tags: ["AI", "Treaties", "Validation", "Reviewer Prompts", "MCP-DL", "Knowledge Graph", "NLP"]
---

<div align="center">

# 🤖 Kansas Frontier Matrix — **AI Reviewer Prompts for Treaty Summaries**  
`data/work/staging/tabular/normalized/treaties/metadata/ai/summaries/prompts/reviewer_prompts.md`

**Purpose:** Define and version the official **AI Reviewer Prompt Framework** used to validate AI-generated treaty summaries for factual, semantic, and ethical integrity in the **Kansas Frontier Matrix (KFM)** system.

[![Docs · MCP-DL v6.3](https://img.shields.io/badge/Docs-MCP--DL%20v6.3-blue)](../../../../../../../../../../../docs/architecture/repo-focus.md)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../../../../../../../../../../LICENSE)
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Compliant-lightblue)]()
[![AI Validation](https://img.shields.io/badge/AI_Validation-Active-orange)]()
[![Status: Stable](https://img.shields.io/badge/Status-Stable-brightgreen)]()

</div>

---

## 🗂️ Directory Layout

```plaintext
prompts/
├── summarization_prompt.md      # Core summarization template (instruction prompt)
├── safety_instructions.md       # Ethical and cultural safeguards
├── reviewer_prompts.md          # Prompts for human-in-the-loop validation ← you are here
├── bias_tests.yaml              # Bias-triggering phrases and exclusion rules
├── config.json                  # Prompt structure + token control config
├── metrics.json                 # Prompt performance data (token efficiency, scores)
└── README.md                    # Overview and schema index for AI prompt set
```

---

## 🧭 Overview

The **Reviewer Prompt Framework** standardizes both AI and human validation of treaty summaries across KFM datasets. It ensures every machine-generated text undergoes consistent factual verification, semantic clarity checks, and fairness evaluation under **MCP-DL v6.3**.  
These prompts govern **automated batch validation**, **human review sessions**, and **CI-integrated AI report audits**.

---

## ⚙️ Workflow Integration

```mermaid
flowchart TD
    A["Generate Treaty Summary – NLP"] --> B["Apply Reviewer Prompts"]
    B --> C["AI Validation Engine – src/nlp/reviewer_agent.py"]
    C --> D["Structured JSON Review Output"]
    D --> E["Human Validator Cross-Check"]
    E --> F["Reports → data/work/staging/tabular/normalized/treaties/reports/validation/reports/"]
    F --> G["Governance Ledger / FAIR+CARE Council"]

%% END OF MERMAID %%
---

## 🧠 Reviewer Prompts

### 1️⃣ Factual Accuracy
Verify extracted facts against source text.

- Ensure treaty names, parties, and dates are correct.  
- Confirm numerical and geographic data.  
- Flag missing or fabricated content.

**Verdict:** `{PASS | PARTIAL | FAIL}`  
**Confidence:** Float (0.0–1.0)

---

### 2️⃣ Semantic Clarity
Assess readability and structural coherence.

- Clear summary flow (intro–context–impact).  
- Minimal ambiguity; balanced tone.  
- Assign a clarity score (1–5).

---

### 3️⃣ Entity Linking
Cross-check all named entities with the Neo4j graph index.

- Link `PERSON`, `PLACE`, `TRIBE`, `TREATY` nodes.  
- Report unresolved or ambiguous references.  
- Log missing graph IDs.

---

### 4️⃣ Historical Alignment
Match events to temporal and spatial ontology.

- Validate date ranges with **OWL-Time** intervals.  
- Compare geographic references with historical maps.  
- Ensure no anachronisms (e.g., modern terms for 19th-century treaties).

---

### 5️⃣ Bias & Representation
Evaluate tone neutrality and representation balance.

- Detect colonial bias or omission of Indigenous perspectives.  
- Verify equal weight to all negotiating parties.  
- Verdict: `{Balanced | Skewed | Inadequate}`.

---

## 📊 Example Output

```json
{
  "treaty_id": "KS_TREATY_1867_03_MEDICINE_LODGE",
  "review": {
    "accuracy": {"verdict": "PASS", "confidence": 0.95},
    "clarity": {"score": 4.8},
    "linkage": {"verdict": "PARTIAL", "missing_entities": ["Osage Nation"]},
    "historicity": {"verdict": "PASS"},
    "bias": {"verdict": "Balanced"}
  },
  "reviewed_by": ["AI Validator", "Human Reviewer"],
  "timestamp": "2025-10-25T15:22:00Z"
}
```

---

## 🧾 Governance & Provenance

| Artifact | Type | Path | Description |
|-----------|------|------|--------------|
| Reviewer Prompts | Markdown | `/metadata/ai/summaries/prompts/reviewer_prompts.md` | Current specification (this file). |
| AI Validation Logs | JSON | `/reports/validation/reports/` | Outputs from automated AI review runs. |
| Human Review Logs | CSV | `/reports/validation/logs/human/` | Annotated feedback and overrides. |
| Governance Ledger | JSON-LD | `/governance/ledger/` | Immutable audit trail with checksum and provenance. |

All validation events are **SHA-256 signed** and cross-referenced in the **FAIR+CARE Governance Ledger** for traceability.

---

## 📈 Performance Metrics

| Metric | Target | CI Threshold |
|--------|---------|---------------|
| Accuracy Agreement | ≥ 95% | 0.93 |
| Entity Linking Precision | ≥ 0.90 | 0.88 |
| Temporal Consistency | ≥ 0.92 | 0.90 |
| Bias Detection Recall | ≥ 0.85 | 0.80 |
| Readability Mean | ≥ 4.5 / 5 | 4.3 |

All metrics feed into automated validation dashboards under  
`data/work/staging/tabular/normalized/treaties/reports/telemetry/dashboards/`.

---

## 🔍 FAIR+CARE Alignment

| Principle | Implementation |
|------------|----------------|
| **Findable** | Indexed via STAC/DCAT metadata. |
| **Accessible** | Publicly available under CC-BY 4.0. |
| **Interoperable** | JSON schema aligns with DCAT + PROV-O. |
| **Reusable** | Parameterized prompt templates, versioned in repo. |
| **CARE – Collective Benefit** | Built-in fairness evaluation and Indigenous data sovereignty tagging. |

---

## 📚 References

- **CIDOC CRM / OWL-Time Ontologies** – Temporal & semantic grounding.  
- **MCP-DL v6.3** – Scientific documentation framework for reproducibility.  
- **AI Validation Pipeline** – `src/nlp/reviewer_agent.py`.  
- **Ethical AI Standards** – `docs/standards/ethics.md`.  
- **STAC Schema** – `data/stac/treaties.json`.

---

## 🧾 Version History

| Version | Date | Author | Reviewer | Notes |
|----------|------|---------|-----------|-------|
| v1.2.0 | 2025-10-25 | @kfm-ai-lab | @kfm-governance | Updated directory layout, added final badges, harmonized FAIR+CARE schema. |
| v1.1.0 | 2025-10-24 | @kfm-ai-lab | @kfm-validation | Rebuilt layout for clarity, metrics table added. |
| v1.0.0 | 2025-10-23 | @kfm-ai-lab | — | Initial creation. |

---

<div align="center">

[![Docs · MCP-DL v6.3](https://img.shields.io/badge/Docs-MCP--DL%20v6.3-blue)]()
[![STAC Validated](https://img.shields.io/badge/STAC-Validated-success)]()
[![ISO 19115](https://img.shields.io/badge/ISO--19115-Geospatial%20Metadata%20Aligned-purple)]()
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Compliant-lightblue)]()
[![AI Review Logs](https://img.shields.io/badge/AI_Review-Tracked-yellow)]()

</div>
