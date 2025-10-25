---
title: "🧾 Kansas Frontier Matrix — AI Treaty Log Archive (2025)"
path: "data/work/staging/tabular/normalized/treaties/logs/ai/archive/2025/README.md"
version: "v1.0.0"
last_updated: "2025-10-25"
maintainers: ["@kfm-data", "@kfm-ai", "@kfm-governance"]
license: "CC-BY 4.0"
status: "Stable · Archive · Read-Only"
---

<div align="center">

# 🧾 Kansas Frontier Matrix — **AI Treaty Log Archive (2025)**  
`data/work/staging/tabular/normalized/treaties/logs/ai/archive/2025/`

**Purpose:** Immutable, FAIR+CARE-compliant archival of all AI treaty-processing pipeline logs, provenance data, and validation artifacts generated during 2025.  
**Scope:** AI summaries, validation chains, reviewer prompts, model metadata, and ledger-linked reports.  

[![Docs · MCP-DL v6.3](https://img.shields.io/badge/Docs-MCP--DL%20v6.3-blue)](../../../../../../../../../docs/architecture/repo-focus.md)  
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../../../../../../../../LICENSE)  
[![Status: Archived](https://img.shields.io/badge/Status-Archive%20%E2%80%A2%20Read--Only-orange)](../../../../../../../../../docs/governance.md)

</div>

---

## 🧭 Overview

This directory contains **AI-generated and human-validated log artifacts** for the **treaty normalization and summarization pipelines** within the Kansas Frontier Matrix (KFM).  
All records adhere to MCP-DL v6.3 documentation principles — ensuring reproducibility, transparency, and verifiability of every AI-assisted process conducted during **2025**.

Artifacts in this archive represent finalized and sealed outputs from:
- Treaty text summarization (`src/nlp/summary_generator.py`)
- Reviewer prompt validation (`src/nlp/reviewer_agent.py`)
- Ethical and safety checks (`safety_instructions.md`)
- FAIR+CARE governance logging and ledger linkage.

---

## 🗂️ Directory Layout

```

data/work/staging/tabular/normalized/treaties/logs/ai/archive/2025/
├── run-YYYY-MM-DD-HHMMSS.json                  # Primary AI run log (inputs, outputs, metadata)
├── provenance_chain-YYYY-MM-DD-HHMMSS.json     # PROV-O structured provenance graph
├── performance_metrics-YYYY-MM-DD-HHMMSS.csv   # Metrics: latency, drift, token usage, errors
├── validation_report-YYYY-MM-DD.json            # Human + AI validation summary
├── redaction_notice-YYYY-MM-DD.json             # Optional — if data removed post-review
├── ai_archive_manifest.json                     # Manifest of all runs (hashes, IDs, ledger links)
└── README.md                                   # This file

````

Each artifact follows deterministic naming conventions to support automated indexing and STAC/DCAT catalog inclusion.

---

## ⚙️ Data Flow Overview

```mermaid
flowchart TD
    A["Raw Treaty Text · OCR / Transcribed"] --> B["AI Summarization Engine · src/nlp/summary_generator.py"]
    B --> C["Reviewer Prompts · review_prompts.md"]
    C --> D["AI Validation Engine · src/nlp/reviewer_agent.py"]
    D --> E["Structured JSON Outputs · validation_report.json"]
    E --> F["Governance Ledger · FAIR+CARE Council"]
    F --> G["Archive Storage · data/work/staging/tabular/normalized/treaties/logs/ai/archive/2025/"]

%% END OF MERMAID %%
````

---

## 🧩 Purpose and Compliance

### 🎯 Goals

1. **Reproducibility:** Capture all AI model parameters, environment hashes, and validation metadata.
2. **Traceability:** Maintain PROV-O–linked provenance across data sources, models, and outputs.
3. **Governance:** Enforce FAIR + CARE standards in AI-driven treaty summarization.
4. **Auditability:** Allow third-party reviewers to cross-verify historical AI decisions through immutable logs.

### 🧾 Standards

| Standard               | Compliance | Description                          |
| ---------------------- | ---------- | ------------------------------------ |
| **MCP-DL v6.3**        | ✅          | Documentation-first architecture     |
| **PROV-O / CIDOC CRM** | ✅          | Provenance and ontology mapping      |
| **FAIR + CARE**        | ✅          | Ethical data stewardship             |
| **STAC / DCAT 3.0**    | ✅          | Dataset discoverability and metadata |
| **ISO 19115 / 19157**  | ✅          | Geospatial & metadata standards      |

---

## 🔍 Usage Guidelines

### For Developers

* Use these archives to retrace any AI or NLP process run during 2025.
* All timestamps correspond to UTC and are logged with SHA-256 checksums.
* Use `ai_archive_manifest.json` for dataset programmatic discovery or STAC ingestion.

### For Reviewers

* Validate the **provenance_chain** files for data source traceability.
* Cross-reference with governance ledger entries located at:
  `data/work/staging/tabular/normalized/treaties/reports/ai/outputs/provenance/`.

### For Governance Council

* Use this archive for oversight audits, verifying ethical adherence, reproducibility, and transparency.
* Redactions or corrections must follow the SOP in `docs/sop/ai-log-archival.md`.

---

## 🧮 Example Record Structure

```json
{
  "run_id": "2025-08-21-143022",
  "model": "gpt-5-treaty-summarizer-v2",
  "inputs": ["Treaty_of_Pawnee_1857.txt"],
  "outputs": ["Treaty_of_Pawnee_1857_summary.json"],
  "reviewer_agent": "src/nlp/reviewer_agent.py",
  "safety_check": "passed",
  "metrics": {
    "latency_s": 42.6,
    "token_usage": 13245,
    "validation_score": 0.97
  },
  "governance_ledger": {
    "ledger_entry_id": "AI-LOG-2025-08-21-143022",
    "fair_care_compliance": true
  },
  "checksum": "f47ac10b58cc4372a5670e02b2c3d479"
}
```

---

## 🧾 Governance and Integrity Policy

All files within this directory are **immutable once archived**.
If any correction or data redaction is required:

1. Generate a new file: `redaction_notice-YYYY-MM-DD.json`.
2. Include justification, approver credentials, and affected file references.
3. Append the notice to the governance ledger (do not overwrite or delete existing logs).

---

## 🧱 Validation & Automation

| Validation Type  | Tool / Schema                      | Trigger               |
| ---------------- | ---------------------------------- | --------------------- |
| JSON Schema      | `/schemas/logs/ai_run.schema.json` | On every CI commit    |
| STAC Validation  | `/tools/stac-validate.yml`         | Nightly GitHub Action |
| Provenance Check | `/tools/prov-check.py`             | Manual or scheduled   |
| FAIR+CARE Audit  | `/tools/faircare-audit.py`         | Quarterly review      |

---

## 🕰️ Version History

| Version | Date       | Author    | Change                                             |
| ------- | ---------- | --------- | -------------------------------------------------- |
| v1.0.0  | 2025-10-25 | @kfm-data | Initial release of AI Archive for 2025 treaty logs |

---

> *Maintained by the **Kansas Frontier Matrix (KFM)** Data + AI Systems Team*
> Refer to:
> `docs/sop/ai-log-archival.md`,
> `docs/architecture/repo-focus.md`,
> and the **Governance Ledger** at `data/work/staging/tabular/normalized/treaties/reports/ai/outputs/provenance/`.

```
```
