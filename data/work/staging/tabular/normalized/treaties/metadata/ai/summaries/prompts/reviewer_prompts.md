---
title: "🤖 Kansas Frontier Matrix — AI Reviewer Prompts for Treaty Summaries"
path: "data/work/staging/tabular/normalized/treaties/metadata/ai/summaries/prompts/reviewer_prompts.md"
document_type: "AI Prompt Definition · Validation Workflow"
version: "v1.0.1"
last_updated: "2025-10-25"
review_cycle: "Quarterly / Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "releases/v1.0.1/sbom.spdx.json"
manifest_ref: "releases/v1.0.1/manifest.zip"
license: ["MIT (code)", "CC-BY 4.0 (data/docs)"]
owners: ["@kfm-ai-lab", "@kfm-architecture"]
approvers: ["@kfm-validation", "@kfm-governance"]
status: "Production · FAIR+CARE+ISO Aligned"
maturity: "Stable"
mcp_version: "MCP-DL v6.3"
tags: ["AI", "Treaties", "Reviewer Prompts", "Validation", "MCP-DL", "NLP", "Knowledge Graph"]
---

<div align="center">

# 🤖 Kansas Frontier Matrix — **AI Reviewer Prompts for Treaty Summaries**  
`data/work/staging/tabular/normalized/treaties/metadata/ai/summaries/prompts/reviewer_prompts.md`

**Purpose:** Define, version, and maintain the official **AI Reviewer Prompt Set** used to validate machine-generated treaty summaries within the *Kansas Frontier Matrix (KFM)* knowledge ecosystem.

[![Docs · MCP-DL v6.3](https://img.shields.io/badge/Docs-MCP--DL%20v6.3-blue)](../../../../../../../../../../../docs/architecture/repo-focus.md)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../../../../../../../../../../LICENSE)
[![Status: Production](https://img.shields.io/badge/Status-Production-brightgreen)]()
[![AI Validation](https://img.shields.io/badge/AI_Validation-Enabled-orange)]()
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Data%20Ethics%20Aligned-lightblue)]()

</div>

---

## 🧭 Overview

The **AI Reviewer Prompt Framework** defines all *automated and human-assisted validation instructions* for treaty summary assessment.  
It ensures summaries meet high scientific and ethical standards of **accuracy, interpretive neutrality, and provenance traceability**, consistent with MCP-DL v6.3.  
Prompts are applied in both *automated batch validation* and *manual human review* to guarantee robust audit trails.

---

## 🧱 Directory Layout

```plaintext
data/
 └── work/
     └── staging/
         └── tabular/
             └── normalized/
                 └── treaties/
                     └── metadata/
                         └── ai/
                             └── summaries/
                                 └── prompts/
                                     ├── reviewer_prompts.md      ← this file
                                     ├── generator_prompts.md      ← generation guidance
                                     └── scoring_schema.json       ← structured evaluation weights
```

---

## 🧩 Purpose and Scope

| Category | Description |
|-----------|-------------|
| **Objective** | Define the structure and semantics of prompts guiding AI models and human reviewers to assess treaty summaries. |
| **Scope** | All normalized treaty metadata under `data/work/staging/tabular/normalized/treaties/` generated via AI summarization pipelines. |
| **Primary Users** | AI validators, human historians, MCP compliance reviewers, and continuous integration bots (`stac-validate.yml`, `ai-review.yml`). |
| **Output Target** | `data/work/staging/tabular/normalized/treaties/reports/validation/reports/summary_reviews/*.json` |
| **Dependencies** | CIDOC CRM ontology, OWL-Time alignment, Neo4j graph schema (`src/graph/schema.cql`) |
| **Review Frequency** | Every 90 days or post-model-update. |

---

## ⚙️ AI Reviewer Workflow Integration

```mermaid
flowchart TD
    A[Generate Treaty Summary (NLP)] --> B[Apply Reviewer Prompts]
    B --> C[AI Validation Engine (src/nlp/reviewer_agent.py)]
    C --> D[Generate JSON Review Artifacts]
    D --> E[Human Validator Cross-Check]
    E --> F[Reports → data/work/staging/tabular/normalized/treaties/reports/validation/reports/]
    F --> G[Governance Ledger Registration]
```
%% END OF MERMAID %%

---

## 🧠 Core Reviewer Prompt Set

### 1️⃣ Factual Accuracy Review
```text
Compare the AI-generated treaty summary to canonical text and metadata.

Check:
- Major facts (date, signatories, parties) are preserved.
- No fabricated or omitted content.
- Chronology is accurate and consistent.

Output: reasoning, verdict {PASS|FAIL|PARTIAL}, confidence score.
```

### 2️⃣ Semantic Clarity Review
```text
Assess clarity, readability, and logical flow of the summary.

Ask:
- Is the text coherent and accessible to a general academic audience?
- Are clauses and cause–effect relationships logically ordered?
- Rate clarity on 1–5 scale and provide one improvement note.
```

### 3️⃣ Entity Linking Validation
```text
Verify named entities correspond to canonical graph nodes.

- Each PERSON, PLACE, or TRIBE entity must link to a Neo4j node ID.
- Identify missing or mislinked entities.
- Return verdict {PASS|PARTIAL|FAIL}.
```

### 4️⃣ Historical Alignment
```text
Validate the temporal and geographic alignment.

- Check that described events fall within verified OWL-Time intervals.
- No anachronisms or geographical inconsistencies.
- Ensure CIDOC CRM alignment for Event → Place → Time relationships.
```

### 5️⃣ Bias and Representation
```text
Evaluate tone and representation for historical neutrality.

- Does the summary treat all parties equitably?
- Detect colonial bias, omission of Indigenous agency, or loaded phrasing.
- Verdict: "Balanced" | "Skewed" | "Inadequate".
```

---

## 🧾 Example JSON Output

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
  "reviewed_by": "AI + Human Validator",
  "timestamp": "2025-10-25T12:30:00Z"
}
```

---

## 📈 Validation Metrics & Thresholds

| Metric | Description | Target |
|--------|--------------|---------|
| **Accuracy Agreement Rate** | % of summaries validated as factually correct | ≥ 95% |
| **Entity Linking Precision** | Correctly linked entities / total | ≥ 0.90 |
| **Temporal Alignment Score** | Agreement with OWL-Time chronology | ≥ 0.92 |
| **Bias Detection Recall** | Biased samples correctly flagged | ≥ 0.85 |
| **Clarity Rating Mean** | Avg. human readability score | ≥ 4.5 / 5 |

---

## 🧩 Data Provenance & Governance

All reviewer prompts, results, and verdicts are logged under the **Governance Ledger** with SHA-256 checksums and contributor attribution.  
This supports **traceable AI validation**, in line with MCP-DL’s **Scientific Method Chain**:

| Step | Artifact | Format | Location |
|------|-----------|---------|----------|
| Prompt Definition | `reviewer_prompts.md` | Markdown | `/metadata/ai/summaries/prompts/` |
| Model Output | `summary.json` | JSON | `/summaries/output/` |
| Validation Result | `review.json` | JSON | `/reports/validation/reports/` |
| Audit Record | `ledger.json` | JSON-LD | `/governance/ledger/` |

---

## 🔍 FAIR+CARE Alignment

| Principle | Implementation |
|------------|----------------|
| **Findable** | All prompts indexed in STAC metadata and searchable via MCP API. |
| **Accessible** | Public under CC-BY 4.0; linked to treaty metadata catalog. |
| **Interoperable** | Structured YAML/JSON schema aligns with DCAT and schema.org/CreativeWork. |
| **Reusable** | Prompts parameterized for reuse in other datasets. |
| **Collective Benefit (CARE)** | Ensures Indigenous representation is ethically reviewed. |

---

## 📚 References

- **CIDOC CRM & OWL-Time** — Temporal ontology and event alignment standards:contentReference[oaicite:0]{index=0}  
- **MCP-DL v6.3** — Documentation-first scientific workflow standard:contentReference[oaicite:1]{index=1}  
- **AI Validation Pipeline** — `src/nlp/reviewer_agent.py` & `stac-validate.yml`  
- **Ethical AI & CARE Guidelines** — `docs/standards/ethics.md`  
- **STAC/DCAT Schema** — Metadata standard for FAIR dataset indexing.

---

## 🧾 Version History

| Version | Date | Author | Reviewer | Description |
|----------|------|---------|-----------|--------------|
| v1.0.1 | 2025-10-25 | @kfm-ai-lab | @kfm-validation | Added architecture, governance, FAIR+CARE, and directory layout. |
| v1.0.0 | 2025-10-24 | @kfm-ai-lab | — | Initial creation of reviewer prompt templates for treaty summary validation. |

---

<div align="center">

**Kansas Frontier Matrix — Master Coder Protocol Certified**  
📘 *All AI documentation follows MCP-DL v6.3 and FAIR+CARE compliance rules.*  
💾 *Validated via CI: `ai-review.yml` + `docs-validate.yml`.*

</div>

