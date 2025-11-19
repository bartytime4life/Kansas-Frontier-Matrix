---
title: "✅ Kansas Frontier Matrix — Validation & FAIR+CARE Compliance Tools (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "tools/validation/README.md"

version: "v11.0.0"
last_updated: "2025-11-19"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Continuous · Autonomous · FAIR+CARE Council Oversight"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-previous-commit-hash>"
doc_guid: "urn:kfm:doc:tools-validation-readme-v11.0.0"
doc_kind: "Overview"
intent: "tools-validation"
role: "validation-registry"
category: "Validation · Governance · FAIR+CARE"

sbom_ref: "../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../releases/v11.0.0/manifest.zip"
data_contract_ref: "../../../docs/contracts/data-contract-v3.json"

telemetry_ref: "../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/tools-validation-registry-v4.json"
energy_schema: "../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0"
ontology_protocol_version: "KFM-OP v11.0"
pipeline_contract_version: "KFM-PDC v11.0"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"
sensitivity: "General"
sensitivity_level: "Low"
public_benefit_level: "High"
indigenous_data_flag: false
risk_category: "Low"
redaction_required: false

provenance_chain:
  - "tools/validation/README.md@v10.0.0"
  - "tools/validation/README.md@v10.2.2"
  - "tools/validation/README.md@v10.3.0"
  - "tools/validation/README.md@v10.3.1"

ontology_alignment:
  cidoc: "E29 Event / Procedure"
  schema_org: "CreativeWork"
  owl_time: "TemporalDuration"
  prov_o: "prov:Activity"
  geosparql: "geo:FeatureCollection"

json_schema_ref: "../../../schemas/json/tools-validation-readme-v11.json"
shape_schema_ref: "../../../schemas/shacl/tools-validation-readme-v11.shape.ttl"

event_source_id: "ledger:tools/validation/README.md"
immutability_status: "mutable-plan"

ai_training_guidance: "Do not use validation logs as model training data."
ai_training_allowed: false
ai_outputs_require_explainability: true
ai_outputs_require_bias_audit: true

machine_readable: true
accessibility_compliance: "WCAG 2.1 AA"
jurisdiction: "United States · Kansas"
lifecycle_stage: "operational"
ttl_policy: "Annual review"
sunset_policy: "Superseded upon next validation-tools architecture update"
---

<div align="center">

# ✅ **Kansas Frontier Matrix — Validation & FAIR+CARE Compliance Tools**  
`tools/validation/README.md`

Central registry of **validation and governance tools** that protect:

- Structural and semantic correctness of data and metadata  
- FAIR+CARE, ethical, and sovereignty alignment  
- Cryptographic integrity and provenance of all assets  
- AI fairness, explainability, and drift monitoring  
- Sustainability telemetry (energy, carbon, resource use)  

All tooling is aligned with **MCP-DL v6.3**, **KFM-MDP v11**, **FAIR+CARE**, **ISO 19115**, and **DCAT 3.0**.

[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Validation%20Certified-gold)](#)
[![License: MIT](https://img.shields.io/badge/License-MIT-green)](#)
[![ISO 19115/DCAT 3.0](https://img.shields.io/badge/ISO--19115%20%2F%20DCAT--3.0-Aligned-green)](#)
[![MCP-DL v6.3](https://img.shields.io/badge/MCP--DL-v6.3-blue)](#)

</div>

## 📘 Overview

The **Validation & FAIR+CARE Compliance Suite** is responsible for:

- Verifying that all KFM datasets, catalogs, and models meet structural and semantic expectations  
- Enforcing FAIR+CARE, sovereignty, and ethical rules before promotion to production  
- Checking cryptographic integrity and lineage for every materialized asset  
- Producing machine-readable telemetry and audit trails that feed the governance and sustainability dashboards  

Validation runs are executed from CI/CD (`tools/validation/*` and `.github/workflows/*`) and from interactive Focus Mode primitives.

Key outputs:

- Governance ledgers: `docs/reports/audit/*.json`  
- Telemetry: `releases/*/focus-telemetry.json`, `docs/reports/telemetry/*.json`  
- Per-dataset validation reports: `data/reports/self-validation/*`  

## 🗂️ Directory Layout

The following layout description is rendered using a **tilde-fenced block** to avoid interfering with outer markdown fences.

~~~~text
tools/
└── validation/
    ├── README.md                   ← this file
    ├── faircare_validator.py       ← FAIR+CARE & accessibility validator
    ├── schema_check.py             ← STAC/DCAT/JSON-LD/contract schema validator
    ├── ai_explainability_audit.py  ← explainability, fairness & drift analysis
    ├췍 checksum_audit.py           ← SHA-256 lineage & integrity verifier
    ├── validator_manifest.json     ← aggregated validation + signatures + scores
    └── metadata.json               ← JSON-LD config for validation profiles & lineage
~~~~

Each Python tool is designed to be:

- Deterministic and idempotent  
- Safe for CI/CD and offline re-runs  
- Configurable via `metadata.json` and data contracts  

## ⚙️ Validation Workflow

The validation workflow is expressed using a **Mermaid** diagram, fenced with tildes for ChatGPT safety.

~~~~mermaid
flowchart TD
  A["Dataset / Model / Metadata"]
    --> B["schema_check.py\nStructural Validation"]
  B --> C["faircare_validator.py\nFAIR+CARE · A11y · Sovereignty"]
  C --> D["checksum_audit.py\nIntegrity & Lineage"]
  D --> E["ai_explainability_audit.py\nTransparency & Bias"]
  E --> F["validator_manifest.json\nResults · Telemetry · Governance Sync"]
~~~~

### Stage 1 — Schema Validation (`schema_check.py`)

- Validates STAC Items and Collections against KFM-STAC v11 schemas  
- Validates DCAT 3.0 JSON-LD datasets and distributions  
- Enforces KFM data contracts (`data_contract_ref`) for internal tables and tilesets  

### Stage 2 — FAIR+CARE & Sovereignty (`faircare_validator.py`)

- Checks CARE labels for Indigenous and culturally sensitive content  
- Validates licensing, usage restrictions, and consent flags  
- Ensures required accessibility metadata and context (e.g., descriptions, language tags)  

### Stage 3 — Checksum & Lineage (`checksum_audit.py`)

- Computes and verifies SHA-256 checksums for all configured artifacts  
- Compares against `metadata.json` and ledger entries to detect tampering  
- Emits lineage edges in PROV-O / JSON-LD for graph ingestion  

### Stage 4 — Explainability & Bias (`ai_explainability_audit.py`)

- Computes SHAP/LIME or model-specific attribution scores  
- Tracks bias metrics (e.g., demographic parity, equalized odds)  
- Detects shifts in feature distributions and model behavior across releases  

### Stage 5 — Manifest & Governance Sync (`validator_manifest.json`)

- Aggregates all stage results into a single JSON document  
- Signs the manifest and updates governance & telemetry references  
- Provides a machine-readable summary for Focus Mode and dashboards  

## 🧾 Example Validation Metadata Record

~~~~json
{
  "@context": "https://schema.org/",
  "@type": "Dataset",
  "id": "validation_session_v11.0.0",
  "validated_assets": [
    "data/processed/hydrology/hydro_streamflow.geojson",
    "data/processed/ecology/vegetation_index.parquet"
  ],
  "schema_passed": true,
  "checksum_verified": true,
  "faircare_compliant": true,
  "ai_explainability_score": 0.998,
  "bias_index": 0.015,
  "energy_wh": 2.3,
  "carbon_gco2e": 2.9,
  "signing_hash": "sha256:a4d56d71d93fe123abc998e77c11...",
  "governance_registered": true,
  "validator": "@kfm-validation-core",
  "timestamp": "2025-11-19T14:20:00Z",
  "governance_ref": "docs/reports/audit/data_provenance_ledger.json"
}
~~~~

**Required boolean signals**

- `schema_passed`  
- `checksum_verified`  
- `faircare_compliant`  

**Example extended metrics**

- `ai_explainability_score` — normalized score between 0 and 1  
- `bias_index` — lower is better; thresholds defined in `metadata.json`  
- `energy_wh`, `carbon_gco2e` — per-run sustainability signals  

## 🧠 FAIR+CARE Governance Matrix

| Principle               | Implementation                                                   | Oversight              |
|-------------------------|------------------------------------------------------------------|------------------------|
| **Findable**            | Stable IDs, JSON-LD lineage, search indexes                     | @kfm-data              |
| **Accessible**          | Open license metadata, clear access URLs, A11y checks           | @kfm-accessibility     |
| **Interoperable**       | STAC/DCAT/ISO/JSON-LD compliance                                | @kfm-architecture      |
| **Reusable**            | Reproducible configs, versioned schemas, pinned dependencies    | @kfm-design            |
| **Collective Benefit**  | Validations consider community priorities and risk/benefit      | @faircare-council      |
| **Authority to Control**| Sovereignty and consent flags enforced before publication       | @kfm-governance        |
| **Responsibility**      | Ethical review, error budgets, remediation tracking             | @kfm-security          |
| **Ethics**              | Bias audits, cultural sensitivity checks, contextual metadata   | @kfm-ethics            |

## 🧰 Validation Tool Summary

| Tool                       | Function                               | Primary Purpose          |
|----------------------------|----------------------------------------|--------------------------|
| `faircare_validator.py`    | FAIR+CARE & accessibility checks       | Ethical compliance       |
| `schema_check.py`          | STAC/DCAT/JSON-LD/contract validation  | Structural correctness   |
| `checksum_audit.py`        | SHA-256 lineage verification           | Integrity assurance      |
| `ai_explainability_audit.py` | Explainability & fairness analysis  | AI ethics & transparency |
| `validator_manifest.json`  | Aggregated results & telemetry bundle  | Governance & observability |

Standard run order:

1. `schema_check.py`  
2. `faircare_validator.py`  
3. `checksum_audit.py`  
4. `ai_explainability_audit.py`  
5. Manifest creation and signing  

## ⚖️ Retention & Provenance Policy

| Artifact               | Retention | Policy                                  |
|------------------------|----------:|-----------------------------------------|
| Schema Reports         | 180 days  | QA and release verification             |
| FAIR+CARE Audit Logs   | 365 days  | Recertification & governance review     |
| Checksum Lineage Data  | Permanent | Immutable provenance                    |
| Validation Manifests   | Permanent | Signed; treated as governance records   |

Cleanup automation retains only:

- Signed manifests  
- Summary reports  
- Key telemetry slices  

while rotating raw execution logs.

## 🌱 Sustainability Metrics

| Metric               | Target (per run) | Verified By           |
|----------------------|-----------------:|-----------------------|
| Energy (Wh)          | ≤ 2.5            | telemetry collectors  |
| Carbon (gCO₂e)       | ≤ 3.0            | sustainability audits |
| Renewable Power Use  | 100% (where possible) | infra attestations |
| FAIR+CARE Compliance | 100% of promoted assets | `faircare_validator.py` |

Telemetry is exported to:

~~~~text
../../../releases/11.0.0/focus-telemetry.json
docs/reports/telemetry/tools-validation-*.json
~~~~

## 🧾 Citation

~~~~text
Kansas Frontier Matrix (2025). Validation & FAIR+CARE Compliance Tools (v11.0.0).
A reproducible validation suite for structural schema checks, lineage integrity,
FAIR+CARE governance, AI transparency, and sustainability telemetry under MCP-DL v6.3.
~~~~

## 🕰️ Version History

| Version | Date       | Summary                                                                                               |
|--------:|------------|-------------------------------------------------------------------------------------------------------|
| v11.0.0 | 2025-11-19 | Upgraded to v11; added energy/carbon schemas, telemetry v4, sovereignty hooks, and enriched metadata. |
| v10.3.1 | 2025-11-13 | Expanded XAI & sustainability signals; aligned to telemetry v3.                                       |
| v10.3.0 | 2025-11-12 | Added validator registry and JSON-LD lineage bundles.                                                |
| v10.2.2 | 2025-11-12 | Introduced checksum lineage and AI transparency metrics.                                             |
| v10.0.0 | 2025-11-10 | Initial validation tools README with FAIR+CARE integration.                                          |

<div align="center">

**© 2025 Kansas Frontier Matrix — MIT License**  
Validation & FAIR+CARE Compliance Tools · FAIR+CARE Certified  
MCP-DL v6.3 · KFM-MDP v11.0 · KFM-OP v11.0 · Diamond⁹ Ω / Crown∞Ω  

[Back to Tools Index](../README.md) · [Docs Portal](../../../docs/) · [Governance Charter](../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>
