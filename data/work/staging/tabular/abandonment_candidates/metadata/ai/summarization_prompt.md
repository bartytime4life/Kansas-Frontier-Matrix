---
title: "🧠 Abandonment Candidate AI Summarization Prompt — FAIR+CARE-Aligned Narrative Generation"
path: "data/work/staging/tabular/abandonment_candidates/metadata/ai/summarization_prompt.md"
version: "v10.0.0"
last_updated: "2025-11-09"
review_cycle: "Continuous / Autonomous"
commit_sha: "<latest-commit-hash>"
governance_ref: "../../../../../../docs/standards/governance/DATA-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
---

# 🧠 **Abandonment Candidate AI Summarization Prompt**

**Purpose:**  
Provide the official **prompt template** used by KFM’s **Focus Transformer v2** to generate ethical, explainable, and FAIR+CARE-certified summaries of **abandonment candidate datasets**.  
This version (v10.0.0) incorporates **telemetry-linked confidence tracking**, **ethics tokenization**, and **governance registry hooks** for transparency and reproducibility.

---

## 📋 Prompt Objective

- Generate **concise, factual summaries** of datasets flagged for potential abandonment or relocation.  
- Capture the **environmental, demographic, and governance** context behind abandonment classification.  
- Highlight **ethical and cultural dimensions**—particularly Indigenous territories, ownership transitions, and historical equity concerns.  
- Maintain **explainability and neutrality**, citing governance logs, datasets, and council outcomes.

---

## 🧾 Prompt Template

```markdown
You are the FAIR+CARE AI Reviewer for the Kansas Frontier Matrix (KFM).

Your goal is to summarize a dataset representing potential abandonment or relocation patterns.  
Use the following structure to ensure compliance with FAIR+CARE and ISO 19115 ethics standards:

1. **Dataset Overview:**  
   - Identify dataset title and version (e.g., `abandonment_2025q4_treaty_records`).  
   - Summarize content, including themes (census, flood, drought, buyouts).  
   - Specify geographic scope and time span (e.g., “Central Kansas, 1930–1950”).

2. **Environmental & Social Context:**  
   - Explain driving factors (e.g., drought index, economic depression, migration).  
   - Link correlated layers (climate indices, parcel history, transportation).  

3. **Governance & Ethics:**  
   - Indicate ethical sensitivity or CARE classification (e.g., “restricted” or “public”).  
   - Note FAIR+CARE Council decisions and any data redaction steps.  

4. **AI Confidence & Explainability:**  
   - Reference SHAP/LIME summaries or Focus Transformer telemetry outputs.  
   - Include confidence intervals and bias checks.  

5. **Concluding Summary:**  
   - Provide a 5–6 sentence narrative describing how the dataset supports the study of abandonment phenomena in Kansas.  
   - Maintain neutrality, historical context, and transparency.
```

---

## 🧩 Example Output

```markdown
**Dataset:** `abandonment_2025q4_treaty_records`  
**Scope:** Central and southern Kansas · 1850–1930 · Land transfers and settlement decline.  

This dataset documents spatial and demographic patterns of land abandonment derived from treaty-era cadastral records, correlated with 1930s Dust Bowl drought indices and census loss.  
Key features include 54% rural population reduction between 1930–1940 and proximity to formerly contested parcels.  
FAIR+CARE governance classified this dataset as “restricted,” mandating anonymization of Indigenous boundary data before republication.  
Focus Transformer v2 audit shows high explainability (SHAP = 0.89) with minimal bias drift (0.03).  
This summary provides contextual clarity for understanding historical land dispossession and climate-driven retreat in Kansas.
```

---

## ⚖️ FAIR+CARE Integration

| Principle | Implementation |
|------------|----------------|
| **Findable** | Each summary embeds dataset ID, CRS, and version hash. |
| **Accessible** | Generated summaries published in JSON-LD linked governance manifests. |
| **Interoperable** | Aligned with DCAT 3.0 and schema.org/description vocabularies. |
| **Reusable** | CC-BY 4.0 licensed text compatible with FAIR dashboards. |
| **CARE – Responsibility** | Explicitly flags ethical and cultural data contexts. |
| **CARE – Ethics** | Reviewed and approved by FAIR+CARE Council before release. |

---

## 🧠 Best Practices

- Preserve **neutral tone** and avoid extrapolation beyond data evidence.  
- Include **governance IDs** (from `data/reports/audit/data_provenance_ledger.json`).  
- Explicitly reference **telemetry confidence metrics** when available.  
- Prioritize **readability and transparency** for policy and community audiences.  
- Store generated outputs alongside validation logs and provenance manifests.  

---

## 🧩 v10 Enhancements

- Integration of **telemetry hooks** for explainability tracking (`focus-telemetry.json`).  
- Support for **AI ethics tags** embedded via JSON-LD annotations.  
- Expansion of prompt syntax to include **governance citation templates**.  
- Harmonized narrative length control via Focus Transformer v2 config parameters.

---

## 🧾 Internal Citation

```text
Kansas Frontier Matrix (2025). Abandonment Candidate AI Summarization Prompt — FAIR+CARE-Aligned Narrative Generation (v10.0.0).
Defines the standardized AI summarization prompt with telemetry v2, governance ID linking, and ethical oversight integration for abandonment candidate datasets in the Kansas Frontier Matrix.
```

---

<div align="center">

**Kansas Frontier Matrix**  
*Explainable AI × FAIR+CARE Ethics × Sustainable Storytelling*  
© 2025 Kansas Frontier Matrix · Master Coder Protocol v6.3 · FAIR+CARE Certified · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[Back to AI Metadata](../README.md) · [Governance Charter](../../../../../../docs/standards/governance/DATA-GOVERNANCE.md)

</div>