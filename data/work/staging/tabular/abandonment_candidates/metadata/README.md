---
title: "🧾 Abandonment Candidate Metadata — Schema, Governance & AI Annotations (KFM-Ready)"
path: "data/work/staging/tabular/abandonment_candidates/metadata/README.md"
version: "v9.9.0"
last_updated: "2025-11-08"
review_cycle: "Continuous / Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../releases/v9.9.0/sbom.spdx.json"
manifest_ref: "../../../../../releases/v9.9.0/manifest.zip"
data_contract_ref: "../../../../../docs/contracts/data-contract-v3.json"
telemetry_ref: "../../../../../releases/v9.9.0/focus-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/abandonment-candidates-metadata-v1.json"
governance_ref: "../../../../../docs/standards/governance/DATA-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 🧾 Kansas Frontier Matrix — **Abandonment Candidate Metadata**
`data/work/staging/tabular/abandonment_candidates/metadata/README.md`

**Purpose:**  
Define the **metadata schema**, **governance manifest**, and **AI annotation protocols** associated with the **abandonment candidate datasets** in the KFM staging environment.  
Ensures traceability, interoperability, and FAIR+CARE-aligned provenance for all flagged or remediated datasets.

[![Docs · MCP](https://img.shields.io/badge/Docs·MCP-v6.3-blue)](../../../../../docs/)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY--4.0-green)](../../../../../LICENSE)
[![FAIR+CARE](https://img.shields.io/badge/FAIR+CARE-Validated-orange)](../../../../../docs/standards/FAIRCARE.md)
[![Status: Maintained](https://img.shields.io/badge/Status-Maintained-success)](#)

</div>

---

## 📘 Overview

This **metadata workspace** consolidates all descriptive, structural, and ethical information tied to **abandonment candidate datasets**.  
Metadata records are used to:
- Define **data schemas** and **validation contracts** for remediated datasets.  
- Store **FAIR+CARE governance manifests** and audit histories.  
- Maintain **AI summarization and drift analysis artifacts** for explainability.  
- Facilitate dataset recovery, redaction, or permanent archival decisions.

All files conform to **JSON Schema Draft 2020-12** and **DCAT 3.0** standards.

---

## 🗂️ Directory Layout

```plaintext
data/work/staging/tabular/abandonment_candidates/metadata/
├── README.md                        # This documentation file
├── abandonment-schema.json           # Data schema & field definitions
├── governance_manifest.json          # Governance tags, CARE classification
├── remediation_log.json              # Restaged datasets & resolutions
└── ai/
    ├── summarization_prompt.md       # AI narrative summary prompt template
    ├── model_drift_report.json       # AI bias/drift telemetry
    └── explainability_audit.json     # SHAP/LIME interpretability outputs
```

---

## ⚙️ Metadata Schema (`abandonment-schema.json`)

Defines the **expected structure** of each record within `abandonment_candidates.csv`.  
It serves as a validation reference for automated QA and FAIR+CARE certification.

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://schemas.kfm.dev/abandonment-candidates.schema.json",
  "title": "Abandonment Candidate Record",
  "type": "object",
  "required": ["id", "county_name", "score", "status"],
  "properties": {
    "id": {
      "type": "string",
      "description": "Unique identifier for the candidate feature."
    },
    "county_name": {
      "type": "string",
      "description": "County of detected abandonment candidate."
    },
    "score": {
      "type": "number",
      "description": "Composite abandonment likelihood score (0–1)."
    },
    "status": {
      "type": "string",
      "enum": ["pending_review", "remediated", "archived"],
      "description": "Governance review status."
    },
    "review_date": {
      "type": "string",
      "format": "date-time"
    },
    "governance": {
      "type": "object",
      "properties": {
        "care_tag": { "type": "string", "enum": ["public", "restricted", "sensitive"] },
        "reviewer": { "type": "string" },
        "decision": { "type": "string" }
      }
    }
  }
}
```

---

## ⚖️ Governance Manifest (`governance_manifest.json`)

Tracks FAIR+CARE classification, council decision records, and provenance.

```json
{
  "dataset_id": "abandonment_2025q4_treaty_records",
  "classification": "restricted",
  "governance": {
    "council_reviewer": "@faircare-council",
    "decision_date": "2025-11-08T15:00:00Z",
    "decision": "redact_sensitive_features",
    "notes": "Dataset contains unredacted Indigenous territorial polygons requiring anonymization."
  },
  "lineage": {
    "source_files": [
      "data/raw/noaa/drought_monitor_2025.csv",
      "data/raw/fema/buyouts_2020.csv"
    ],
    "checksum_sha256": "sha256:b8a7e3c6f4d2a9b5c3f8e9a7d6b2f5a4..."
  },
  "metadata_status": "certified"
}
```

---

## 🧩 AI Annotation Submodule (`ai/`)

This submodule stores explainability and summarization assets used to describe or remediate datasets flagged under abandonment governance.

### `summarization_prompt.md`
Prompt used by **Focus Transformer v2** for automated summary generation.

```markdown
Summarize this dataset in one paragraph:
- Highlight key environmental and demographic indicators.
- Flag any ethical considerations or potential biases.
- Provide a high-level explanation suitable for FAIR+CARE Council reporting.
```

### `model_drift_report.json`
Tracks model stability across review cycles.

```json
{
  "model": "focus_transformer_v2",
  "last_reviewed": "2025-11-08T15:30:00Z",
  "bias_score": 0.03,
  "concept_drift": "none",
  "explainability_summary": "SHAP features stable; minor variance in rural population features."
}
```

### `explainability_audit.json`
Summarizes AI model interpretability and fairness metrics.

```json
{
  "model_id": "focus_transformer_v2",
  "audit_date": "2025-11-08T16:00:00Z",
  "metrics": {
    "feature_importance_stability": 0.97,
    "bias_drift": 0.05
  },
  "findings": [
    "No systemic bias detected in environmental datasets.",
    "Ensure balanced representation of rural vs. urban census blocks."
  ]
}
```

---

## 🧠 FAIR+CARE Governance Matrix

| Principle | Implementation | Oversight |
|-----------|----------------|-----------|
| **Findable** | Metadata indexed in STAC/DCAT catalog and Neo4j graph. | `@kfm-data` |
| **Accessible** | Public metadata, restricted data by CARE tag. | `@kfm-accessibility` |
| **Interoperable** | Schema aligns with DCAT 3.0 and JSON-LD FAIR vocabularies. | `@kfm-architecture` |
| **Reusable** | CC-BY 4.0 licensed with validation references. | `@kfm-design` |
| **CARE — Responsibility** | Council-certified ethical decision workflow. | `@faircare-council` |
| **CARE — Ethics** | Metadata retains anonymization and review history. | `@kfm-ethics` |

---

## 📊 Telemetry & Validation

| Artifact | Description | Schema |
|-----------|-------------|---------|
| `governance_manifest.json` | Council-approved decisions, classification tags | `faircare-governance-v2.json` |
| `remediation_log.json` | Record of all restaged datasets | `data-work-staging-tabular-v9.json` |
| `model_drift_report.json` | AI explainability and drift monitoring | `telemetry_schema` |

Telemetry records for metadata updates are appended to  
`releases/v9.9.0/focus-telemetry.json`.

---

## 🧾 Internal Citation

```text
Kansas Frontier Matrix (2025). Abandonment Candidate Metadata — Schema, Governance & AI Annotations (v9.9.0).
Defines FAIR+CARE-compliant metadata schema, governance manifest, and AI annotation submodule for ethical dataset triage and remediation within the KFM data staging system.
```

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|----------|------|--------|----------|
| v9.9.0 | 2025-11-08 | `@kfm-governance` | Added AI explainability audit submodule and expanded governance manifest for FAIR+CARE Council tracking. |
| v9.8.0 | 2025-11-06 | `@kfm-data` | Introduced schema and remediation log. |
| v9.7.0 | 2025-11-02 | `@faircare-council` | Established metadata and ethical classification baseline. |

---

<div align="center">

**Kansas Frontier Matrix**  
*Metadata Integrity × FAIR+CARE Governance × Explainable AI Stewardship*  
© 2025 Kansas Frontier Matrix · Master Coder Protocol v6.3 · FAIR+CARE Certified · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[Back to Abandonment Candidates](../README.md) · [Governance Charter](../../../../../docs/standards/governance/DATA-GOVERNANCE.md)

</div>

