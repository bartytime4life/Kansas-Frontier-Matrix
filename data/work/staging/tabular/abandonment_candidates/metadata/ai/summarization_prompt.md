---
title: "🧠 Abandonment Candidate AI Summarization Prompt — FAIR+CARE-Aligned Narrative Generation"
path: "data/work/staging/tabular/abandonment_candidates/metadata/ai/summarization_prompt.md"
version: "v9.9.0"
last_updated: "2025-11-08"
review_cycle: "Continuous / Autonomous"
commit_sha: "<latest-commit-hash>"
governance_ref: "../../../../../../docs/standards/governance/DATA-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
---

# 🧠 **Abandonment Candidate AI Summarization Prompt**

**Purpose:**  
Provide the official **prompt template** used by KFM’s **Focus Transformer v2** to generate ethical, explainable, and FAIR+CARE-certified summaries of **abandonment candidate datasets**.  
This template standardizes how AI narratively contextualizes historical, environmental, and socio-cultural patterns of land abandonment or relocation.

---

## 📋 Prompt Objective

- Generate **concise, factual summaries** of datasets flagged for potential abandonment.  
- Capture the **environmental, demographic, and governance** context driving candidate classification.  
- Highlight **ethical considerations**—especially cultural sensitivity, Indigenous data, and land ownership.  
- Maintain **explainability and neutrality** by referencing data sources and avoiding inference beyond the dataset scope.

---

## 🧾 Prompt Template

```markdown
You are the FAIR+CARE AI Reviewer for the Kansas Frontier Matrix (KFM).

Your task is to summarize a dataset representing potential abandonment or relocation patterns.  
Use the following structured format:

1. **Dataset Summary:**  
   - Describe what the dataset contains (e.g., census loss, drought severity, FEMA buyouts).  
   - Indicate geographic scope (counties, coordinates, or regions) and temporal coverage (e.g., 1930–1940, 1993 flood).

2. **Environmental & Social Context:**  
   - Identify key environmental or socioeconomic pressures (drought, floods, policy, migration).  
   - Mention relationships to other datasets (e.g., parcel history, railroads, flood extents).

3. **Governance & Ethics:**  
   - Note any CARE or FAIR+CARE implications, including data sensitivity or ethical use restrictions.  
   - Identify whether the dataset required remediation, anonymization, or redaction.  

4. **AI Confidence & Explainability:**  
   - Summarize SHAP or LIME explainability findings (if available).  
   - Note model confidence and bias checks.

5. **Conclusion:**  
   - Provide a one-paragraph, neutral narrative describing the dataset’s relevance to Kansas’s historical and environmental landscape.
```

---

## 🧩 Example Output

```markdown
**Dataset:** `abandonment_2025q4_treaty_records`  
**Scope:** Central and southern Kansas; 1850–1930 historical cadastral and treaty data.  

This dataset identifies potential abandonment or relocation events derived from treaty-era land transfers and subsequent demographic decline.  
Key indicators include a 55% population loss between 1930–1940, correlation with Dust Bowl drought severity indices, and proximity to historically contested parcels.  
FAIR+CARE governance requires redaction of specific Indigenous boundary references before public release.  
Focus Transformer v2 reports high model confidence (0.91) with minimal bias drift (0.04).  
Overall, this dataset provides valuable context for understanding early land dispossession and environmental migration patterns in Kansas’s frontier history.
```

---

## ⚖️ FAIR+CARE Integration

| Principle | Implementation |
|------------|----------------|
| **Findable** | Each generated summary embeds dataset ID and version. |
| **Accessible** | AI summaries stored in governance-ledger metadata (JSON-LD). |
| **Interoperable** | Output format aligns with DCAT 3.0 and schema.org/description. |
| **Reusable** | CC-BY 4.0 licensed text for integration into FAIR+CARE dashboards. |
| **CARE – Responsibility** | AI explicitly flags ethical and cultural considerations. |
| **CARE – Ethics** | Summaries reviewed by FAIR+CARE Council before publication. |

---

## 🧠 Best Practices

- Maintain neutrality and cultural respect—no speculation beyond data evidence.  
- Include **citations or provenance** wherever available (dataset source, council decision ID).  
- Prefer **clear, human-readable** summaries; avoid technical jargon in final output.  
- Ensure summaries are **auditable and reproducible** using telemetry logs from Focus Transformer v2.  

---

## 🧾 Internal Citation

```text
Kansas Frontier Matrix (2025). Abandonment Candidate AI Summarization Prompt — FAIR+CARE-Aligned Narrative Generation (v9.9.0).
Defines the structured AI prompt used for ethical, explainable summarization of abandonment candidate datasets in the KFM data governance pipeline.
```

---

<div align="center">

**Kansas Frontier Matrix**  
*Explainable AI × FAIR+CARE Ethics × Sustainable Storytelling*  
© 2025 Kansas Frontier Matrix · Master Coder Protocol v6.3 · FAIR+CARE Certified · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[Back to AI Metadata](../README.md) · [Governance Charter](../../../../../../docs/standards/governance/DATA-GOVERNANCE.md)

</div>

