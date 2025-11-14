---
title: "🧪 Kansas Frontier Matrix — Self-Validation Procedures & Automated Data Governance (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/guides/data-governance/self-validation/README.md"
version: "v10.3.1"
last_updated: "2025-11-13"
review_cycle: "Continuous / Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../releases/v10.3.0/sbom.spdx.json"
manifest_ref: "../../../../releases/v10.3.0/manifest.zip"
data_contract_ref: "../../../../docs/contracts/data-contract-v3.json"
telemetry_ref: "../../../../releases/v10.3.0/focus-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/self-validation-v1.json"
governance_ref: "../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 🧪 **Kansas Frontier Matrix — Self-Validation Procedures**  
`docs/guides/data-governance/self-validation/README.md`

**Purpose:**  
Define the **automated self-validation system** used throughout the Kansas Frontier Matrix (KFM) data pipeline.  
These procedures ensure that every dataset, model, contract, and metadata asset is **structurally valid**, **FAIR+CARE-aligned**, **checksum-verified**, and **provenance-registered** before it can advance to staging, processed, or publication layers.

[![Docs · MCP v6.3](https://img.shields.io/badge/Docs%20·%20MCP-v6.3-blue.svg)]()  
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-SelfValidation-gold.svg)]()  
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-green.svg)]()  
[![Status: Automated](https://img.shields.io/badge/Status-Automated-success.svg)]()

</div>

---

## 📘 Overview

Self-validation is the **first line of defense** in KFM’s Diamond⁹ Ω data governance system.  
It acts as an automated, reproducible gate that requires *all* data assets to pass:

- Structural compliance (STAC/DCAT/JSON-LD/ISO schemas)  
- FAIR+CARE governance checks (sensitivity, sovereignty, licensing, consent)  
- Checksum lineage verification (SHA-256 integrity chain)  
- AI ethics validation (bias, drift, explainability)  
- Telemetry extraction (energy, CO₂e, performance metrics)

Self-validation results feed into:

- `data/reports/self-validation/*`  
- `data/reports/audit/*`  
- `releases/*/focus-telemetry.json`  
- Governance ledgers

Only assets that pass self-validation can move to **staging**, **processed**, or **publication**.

---

## 🧭 Self-Validation Workflow (Indented Mermaid)

~~~~~mermaid
flowchart TD
  A["Data / Model / Metadata Submitted"]
    --> B["Schema Validation<br/>(STAC · JSON-Schema · ISO · DCAT)"]
  B --> C["FAIR+CARE Audit<br/>(Ethics · Consent · Sovereignty)"]
  C --> D["Checksum Verification<br/>(SHA-256 Lineage)"]
  D --> E["AI Explainability & Bias Audit<br/>(If Applicable)"]
  E --> F["Self-Validation Record<br/>(Stored in data/reports/self-validation/)"]
  F --> G["Governance Ledger Sync<br/>Telemetry Update"]
~~~~~

---

## 🗂️ Self-Validation Directory Layout

~~~~~text
docs/guides/data-governance/self-validation/
├── README.md
└── examples/
    ├── stac_validation_summary.json
    ├── faircare_validation_report.json
    ├── checksum_manifest.json
    └── ai_validation_ledger.json
~~~~~

---

## 🔍 Validation Components

| Component | Description | Responsible Tool |
|----------|-------------|------------------|
| **Schema Validation** | Ensures dataset metadata, geometry, schema, and contracts match STAC/DCAT/JSON-LD specifications. | `schema_check.py` |
| **FAIR+CARE Audit** | Evaluates cultural sensitivity, licensing, sovereignty, context, and accessibility requirements. | `faircare_validator.py` |
| **Checksum Verification** | Validates file integrity and lineage across transformations. | `checksum_audit.py` |
| **AI Explainability Audit** | For ML outputs: checks bias, drift, explainability, SHAP/LIME panels. | `ai_explainability_audit.py` |
| **Telemetry Extractor** | Captures compute cost, energy, CO₂e, and validation time. | `telemetry-export.yml` |

---

## 🧾 Example Self-Validation Record

~~~~~json
{
  "id": "self_validation_run_v10.3.1_flood_hazards",
  "validated_assets": [
    "data/work/tmp/hazards/flood_1903.geojson",
    "data/work/staging/hazards/flood_1903_schema.json"
  ],
  "schema_passed": true,
  "faircare_compliant": true,
  "checksum_valid": true,
  "ai_bias_index": 0.012,
  "ai_explainability_score": 0.994,
  "energy_wh": 3.1,
  "carbon_gco2e": 4.5,
  "governance_ref": "data/reports/audit/data_provenance_ledger.json",
  "timestamp": "2025-11-13T15:44:00Z"
}
~~~~~

---

## 📊 Minimum Validation Requirements

### A dataset **must** include:
- Valid JSON schema contract (`data/sources/<id>.json`)
- Valid STAC Item / Collection  
- SHA-256 checksums for all assets  
- Explicit license (SPDX-compatible or CC-BY/CC0/Public Domain)  
- FAIR+CARE metadata fields (`care_label`, `sensitivity`, `sovereignty_notes`)  

### A dataset **must pass**:
- Schema validation (`true`)  
- FAIR+CARE validation (`true`)  
- Checksum verification (`true`)  
- No missing required metadata fields  
- Telemetry capture (energy + carbon)

Datasets that fail any requirement are **blocked** from progression.

---

## 🧠 FAIR+CARE Self-Governance Matrix

| Principle | Self-Validation Enforcement |
|----------|------------------------------|
| **Findable** | STAC/DCAT metadata completeness, unique IDs |
| **Accessible** | Valid license, open formats |
| **Interoperable** | STAC 1.0, DCAT 3.0, ISO 19115 alignment |
| **Reusable** | Versioning + provenance + schema completeness |
| **Collective Benefit** | Evaluation of data benefits to communities |
| **Authority to Control** | Sovereignty review, CARE-label checks |
| **Responsibility** | Required sensitivity statements & context |
| **Ethics** | No harmful or culturally restricted materials |

---

## ⚙️ Integration With CI/CD

Self-validation is triggered by:

- **Dataset submissions**  
- **Model updates**  
- **Metadata contract changes**  
- **Pull Requests touching `data/` or `schemas/`**  

Workflows involved:

| Workflow | Purpose |
|----------|---------|
| `stac-validate.yml` | STAC/DCAT compliance |
| `faircare-validate.yml` | FAIR+CARE ethics & licensing |
| `docs-lint.yml` | Documentation/schema consistency |
| `ai-model-audit.yml` | Ethics for AI outputs |
| `telemetry-export.yml` | Sustainability + performance |

Artifacts feed directly into append-only governance ledgers.

---

## 🧹 Self-Validation Retention Policy

| Artifact | Retention | Notes |
|----------|-----------|-------|
| Schema results | 180 days | Used in metadata audits |
| FAIR+CARE reports | 365 days | Reviewed in quarterly governance cycles |
| Checksum manifests | Permanent | Immutable lineage |
| AI fairness/explainability | Permanent | Ethical transparency |
| Telemetry | 365 days | Used for sustainability dashboards |

Cleanup is automated by:  
`validation_cleanup.yml`

---

## 🧩 Cross-References

- **Data Governance Guide:** `docs/guides/data-governance/README.md`  
- **Validation Tools:** `tools/validation/README.md`  
- **Data Architecture:** `data/ARCHITECTURE.md`  
- **FAIR+CARE Standard:** `docs/standards/faircare.md`  
- **Governance Charter:** `docs/standards/governance/ROOT-GOVERNANCE.md`

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|---------|--------|---------|---------|
| v10.3.1 | 2025-11-13 | Data Governance Team | Initial v10.3 release; STAC/DCAT alignment; new explainability/bias rules; sustainability telemetry integration. |

---

<div align="center">

**Kansas Frontier Matrix — Self-Validation Guide**  
Diamond⁹ Ω / Crown∞Ω Ultimate Certified · FAIR+CARE Guaranteed  
© 2025 Kansas Frontier Matrix — CC-BY 4.0  

[Back to Data Governance Guide](../README.md) · [Root Governance Charter](../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

