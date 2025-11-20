---
title: "✅ Kansas Frontier Matrix — Climate Validation Workspace (Schema, FAIR+CARE & AI QA Layer · Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "data/work/tmp/climate/validation/README.md"

version: "v11.0.0"
last_updated: "2025-11-20"
release_stage: "Stable · Governed"
review_cycle: "Continuous · Autonomous Quality Assurance"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-README-sha>"
doc_integrity_checksum: "<sha256-of-this-file>"
doc_uuid: "urn:kfm:doc:data-work-tmp-climate-validation-v11.0.0"
semantic_document_id: "kfm-doc-data-work-tmp-climate-validation-readme"
event_id: "urn:kfm:event:tmp-climate-validation-readme-v11"
immutability_status: "version-pinned"

sbom_ref: "../../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.0.0/manifest.zip"
data_contract_ref: "../../../../../docs/contracts/data-contract-v3.json"

telemetry_ref: "../../../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/work-climate-validation-v16.json"
energy_schema: "../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../schemas/telemetry/carbon-gco2e-v2.json"
json_export: "../../../../../releases/v11.0.0/work-climate-validation.meta.json"

validation_reports:
  - "../../../../../reports/self-validation/work-climate-validation.json"
  - "../../../../../reports/fair/climate_validation_summary.json"
  - "../../../../../reports/audit/ai_climate_validation_ledger.json"

governance_ref: "../../../../../docs/standards/governance/DATA-GOVERNANCE.md"
ethics_ref: "../../../../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "CC-BY 4.0 / FAIR+CARE Certified"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0"
ontology_protocol_version: "KFM-OP v11.0"
pipeline_contract_version: "KFM-PDC v11.0"

status: "Active / Enforced"
doc_kind: "Validation Workspace"
intent: "climate-validation-workspace"
role: "climate-domain"
category: "Data · Climate · Validation · Temporary"

fair_category: "F1-A1-I1-R1"
care_label: "Medium — climate risk & impact assessments"
sensitivity_level: "Dataset-dependent"
indigenous_rights_flag: "Dataset-dependent"
redaction_required: true
data_steward: "KFM FAIR+CARE Council"
risk_category: "Medium–High (decision-support relevance)"

ontology_alignment:
  cidoc: "E13 Attribute Assignment"
  schema_org: "Dataset"
  owl_time: "TemporalEntity"
  prov_o: "prov:Activity"
  geosparql: "geo:FeatureCollection"

json_schema_ref: "../../../../../schemas/json/data-work-tmp-climate-validation-v11.json"
shape_schema_ref: "../../../../../schemas/shacl/data-work-tmp-climate-validation-v11-shape.ttl"

ai_training_inclusion: false
ai_focusmode_usage: "Restricted · QA-only context"
ai_transform_permissions:
  - "summaries"
  - "uncertainty-annotations"
ai_transform_prohibited:
  - "direct public-facing predictions from TMP-only outputs"
  - "use of non-certified TMP artifacts as final decision inputs"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
classification: "Internal QA & Governance Data"
jurisdiction: "Kansas / United States"
lifecycle_stage: "transient-validation"
ttl_policy: "7–30 days (post-promotion)"
sunset_policy: "Auto-cleared after promotion to tmp/climate/staging/"
---

<div align="center">

# ✅ **Kansas Frontier Matrix — Climate Validation Workspace (Schema, FAIR+CARE & AI QA Layer)**  
`data/work/tmp/climate/validation/README.md`

**Purpose:**  
Central governance-linked QA hub for **schema validation, FAIR+CARE ethics auditing, checksum verification, telemetry v2, and AI quality assurance** of climate datasets within the TMP pipeline.

This workspace ensures that every climate artifact promoted beyond TMP:

- Meets **schema + metadata requirements** (STAC/DCAT/CF/ISO)  
- Passes **FAIR+CARE ethics checks**  
- Has **verified checksums & documented provenance**  
- Has been **audited for AI model quality & drift**  

[![Docs · MCP](https://img.shields.io/badge/Docs%20·%20MCP-v11.0-blue)](../../../../../docs/architecture/README.md)  
[![FAIR+CARE Validation](https://img.shields.io/badge/FAIR%2FCARE-Validation%20Certified-green)](../../../../../docs/standards/faircare/FAIRCARE-GUIDE.md)  
[![ISO 19115 · 14064](https://img.shields.io/badge/ISO-19115%20%7C%2014064%20Compliant-2e7d32)]()  
[![AI Explainability](https://img.shields.io/badge/AI-Explainability%20Audited-7e57c2)]()  
[![Security Verified](https://img.shields.io/badge/Security-PGP%20%2B%20Ledger-14b8a6)]()

</div>

---

## 1. 📘 Overview

The **Climate Validation Workspace** is the **final QA checkpoint** for all climate data emerging from:

- `data/work/tmp/climate/transforms/`  
- `data/work/tmp/climate/exports/`  

Here we perform:

- Schema & structural validation (KFM data-contract v3, STAC, CF, ISO 19115)  
- FAIR+CARE ethical audits (access, sensitivity, reuse)  
- Checksum verification vs. manifests & registries  
- AI model validation: drift detection, explainability scoring  
- Compilation of validation manifests and governance-ready records  

Only datasets that pass these checks are eligible for promotion to `data/work/tmp/climate/staging/`.

---

## 2. 🗂️ Directory Layout (Mobile-Safe)

```text
data/work/tmp/climate/validation/
├── README.md                      ← this file
├── schema_report.json             # Detailed schema & format checks
├── checksums.json                 # Checksum validation results
├── faircare_report.json           # FAIR+CARE audit outcomes
├── ai_explainability.json         # Model explainability results
├── drift_audit.json               # Model drift & stability analysis
├── validation_manifest.json       # Consolidated validation results
├── governance_review.json         # Council review & sign-off
└── metadata.json                  # Local validation run metadata
```

Additional validation artifacts MAY be added but MUST be referenced in `validation_manifest.json`.

---

## 3. ⚙️ Validation Workflow

```mermaid
flowchart TD
    INPUT["Transformed Climate (tmp/climate/transforms/)"]
      --> SCHEMA["Schema & Metadata Validation"]
    SCHEMA --> FAIR["FAIR+CARE Ethics Verification"]
    FAIR --> HASH["Checksum Integrity Verification"]
    HASH --> AIQA["AI Explainability + Drift Audit"]
    AIQA --> REPORT["Assemble validation_manifest.json"]
    REPORT --> LEDGER["Provenance Registration (Governance Ledger)"]
    REPORT --> STAGING["Eligible → tmp/climate/staging/"]
```

### Step Summary

1. **Schema Validation**  
   - Check variable names, types, ranges, units, CRS, and CF conformance.  

2. **FAIR+CARE Audit**  
   - Validate ethical use, sensitivity flags, and access constraints.  

3. **Checksum Verification**  
   - Compare with `tmp` and domain-level checksum registries.  

4. **AI QA & Drift**  
   - Run explainability methods (LIME/SHAP) on model outputs; detect drift and anomalies.  

5. **Validation Manifest**  
   - Compile results into `validation_manifest.json` with references to all artifact files.  

6. **Governance Registration**  
   - Register validation events in `ai_climate_validation_ledger.json` & provenance logs.  

---

## 4. 🧩 Example Validation Record

```json
{
  "id": "climate_validation_precipitation_v11.0.0",
  "domain": "climate",
  "dataset_ref": "data/work/tmp/climate/transforms/precipitation_harmonized_2025.parquet",
  "schema_status": "passed",
  "fair_care_score": 99.2,
  "ai_explainability_score": 0.991,
  "checksum_integrity": "verified",
  "drift_detected": false,
  "validated_by": "@kfm-climate-lab",
  "created": "2025-11-20T23:59:00Z",
  "telemetry": {
    "energy_wh": 0.8,
    "carbon_gco2e": 1.0,
    "validation_coverage_pct": 100
  },
  "ledger_ref": "reports/audit/ai_climate_validation_ledger.json#climate_validation_2025_11_20_001"
}
```

This record is:

- A **prov:Entity** representing a specific validation event  
- Linked to transformation and export entities and QA activities  

---

## 5. 🧠 FAIR+CARE & ISO Governance Matrix

| Standard / Principle | Description                                      | Result | Oversight              |
|----------------------|--------------------------------------------------|--------|------------------------|
| **FAIR+CARE**        | Ethics, accessibility, reuse, community context  | ✅      | `@faircare-council`    |
| **ISO 19115**        | Metadata structure & lineage                     | ✅      | `@kfm-architecture`    |
| **ISO 14064**        | Carbon reporting for validation compute          | ✅      | `@kfm-sustainability`  |
| **STAC 1.0**         | Spatial/temporal metadata alignment              | ✅      | `@kfm-data`            |
| **CF Conventions**   | Climate variable + unit checks                   | ✅      | `@kfm-climate`         |
| **Provenance Ledger**| Immutable validation audit records               | ✅      | `@kfm-governance`      |

Audit & Governance References:

- `../../../../../reports/audit/ai_climate_validation_ledger.json`  
- `../../../../../reports/fair/climate_validation_summary.json`  

---

## 6. 🧪 AI Explainability Snapshot

```json
{
  "model": "focus-climate-v5",
  "task": "precipitation_anomaly_classification",
  "method": "LIME",
  "top_features": [
    {"feature": "precip_anomaly_3mo", "importance": 0.19},
    {"feature": "soil_moisture_anomaly", "importance": 0.12},
    {"feature": "temperature_anomaly", "importance": 0.10}
  ],
  "drift_detected": false,
  "explanation_score": 0.991,
  "validated_by": "@kfm-ai-review"
}
```

These outputs are stored in `ai_explainability.json` and cross-referenced in `validation_manifest.json`.

---

## 7. 🧾 Validation Artifacts & Automation

Key artifacts in this directory:

| File                        | Description                                  | Format |
|-----------------------------|----------------------------------------------|--------|
| `schema_report.json`        | Detailed schema, CF, and ISO checks          | JSON   |
| `checksums.json`            | Checksum verification results                | JSON   |
| `faircare_report.json`      | FAIR+CARE audit outcomes & notes             | JSON   |
| `ai_explainability.json`    | Model explainability outputs                 | JSON   |
| `drift_audit.json`          | Model drift & stability checks               | JSON   |
| `validation_manifest.json`  | Master summary of validation run             | JSON   |
| `governance_review.json`    | Council decisions & comments                 | JSON   |
| `metadata.json`             | Run-level metadata & telemetry               | JSON   |

Automation Workflow:

- `climate_validation_sync.yml` — orchestrates validation, artifact generation, and ledger sync.

---

## 8. ♻️ Sustainability Metrics (ISO)

Example climate validation run:

| Metric                   | Standard  | Value  | Verified By           |
|--------------------------|-----------|-------:|-----------------------|
| Energy (Wh/run)         | ISO 50001 | 6.8    | `@kfm-sustainability` |
| Carbon (gCO₂e/run)      | ISO 14064 | 8.0    | `@kfm-security`       |
| Renewable Power Share   | RE100     | 100%   | `@kfm-infrastructure` |
| Validation Coverage     | N/A       | 100%   | `@faircare-council`   |

Telemetry is logged in:  
`../../../../../releases/v11.0.0/focus-telemetry.json`

---

## 9. 🕰️ Version History

| Version | Date       | Author           | Summary                                                       |
|--------:|------------|------------------|---------------------------------------------------------------|
| v11.0.0 | 2025-11-20 | `@kfm-climate`   | Upgraded to v11, added governance fields & TMP alignment      |
| v10.0.0 | 2025-11-09 | `@kfm-climate`   | Telemetry v2, drift audit, CF/ISO checks, FAIR+CARE reports   |

<div align="center">

**Kansas Frontier Matrix — Climate Validation Workspace**  
✅ FAIR+CARE Certified · Schema & AI QA Hub · Diamond⁹ Ω / Crown⁹ Ω  

© 2025 Kansas Frontier Matrix — CC-BY 4.0  

[Back to Climate TMP](../README.md) · [Data Architecture](../../../../ARCHITECTURE.md) · [Governance Charter](../../../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>
