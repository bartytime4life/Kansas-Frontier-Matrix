---
title: "✅ Kansas Frontier Matrix — Validation & FAIR+CARE Compliance Tools (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "tools/validation/README.md"
version: "v11.0.1"
last_updated: "2025-11-24"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Continuous · Autonomous · FAIR+CARE Council Oversight"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-commit-hash>"
doc_guid: "urn:kfm:doc:tools-validation-readme-v11.0.1"
doc_kind: "Operational Specification"
intent: "tools-validation"
role: "validation-registry"
category: "Validation · Governance · FAIR+CARE · Sovereignty"
semantic_document_id: "kfm-doc-tools-validation"
immutability_status: "mutable-plan"

sbom_ref: "../../../releases/v11.0.1/sbom.spdx.json"
manifest_ref: "../../../releases/v11.0.1/manifest.zip"
data_contract_ref: "../../../docs/contracts/data-contract-v3.json"

telemetry_ref: "../../../releases/v11.0.1/focus-telemetry.json"
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
  - "tools/validation/README.md@v11.0.0"

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "CreativeWork"
  owl_time: "TemporalDuration"
  prov_o: "prov:Activity"
  geosparql: "geo:FeatureCollection"

json_schema_ref: "../../../schemas/json/tools-validation-readme-v11.json"
shape_schema_ref: "../../../schemas/shacl/tools-validation-readme-v11.shape.ttl"

event_source_id: "ledger:tools/validation/README.md"
ai_training_allowed: false
ai_training_guidance: "Do not use validation logs as training input."
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

**The authoritative validation suite for structural correctness, governance safety, ethics, sovereignty, explainability,
and sustainability compliance across the Kansas Frontier Matrix.**

[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Validation%20Certified-gold)](#)
[![License: MIT](https://img.shields.io/badge/License-MIT-green)](#)
[![ISO 19115](https://img.shields.io/badge/ISO--19115%20Aligned-blue)](#)
[![DCAT 3.0](https://img.shields.io/badge/DCAT--3.0-Integrated-green)](#)
[![MCP-DL v6.3](https://img.shields.io/badge/MCP--DL-v6.3-blue)](#)

</div>

---

# 📘 1. Overview

The **Validation & FAIR+CARE Compliance Suite** enforces the **governed correctness** of:

- Data (raw → processed → published)
- STAC Collections & Items
- DCAT 3.0 datasets and distributions
- JSON-LD metadata (Story Nodes, Telemetry, Governance)
- Pipeline outputs (ETL, AI, Inference)
- Explainability + bias/demographic fairness metrics
- Lineage, integrity, and checksum chains
- CARE, sovereignty, and ethical rules
- Energy, carbon, and sustainability telemetry

This is the **single source of truth** for validation behavior across:

- Tools Platform (`tools/**`)
- CI/CD workflows (`.github/workflows/*`)
- Data pipeline DAGs (`src/pipelines/*`)
- Governance sync engines
- Focus Mode v3 explainability and safety screens

---

# 🗂️ 2. Directory Layout (KFM-MDP v11 Safe Tilde Fence)

~~~~text
tools/
└── validation/
    ├── README.md                   # This file
    │
    ├── faircare_validator.py       # CARE, sovereignty, A11y, licensing, ethics
    ├── schema_check.py             # STAC, DCAT, JSON-LD, Contracts
    ├── ai_explainability_audit.py  # SHAP/LIME attribution + drift + fairness metrics
    ├── checksum_audit.py           # SHA-256 lineage, tamper detection
    │
    ├── validator_manifest.json     # Aggregated results + signing + telemetry
    └── metadata.json               # JSON-LD validation profile config
~~~~

---

# 🧩 3. Tools Platform Context in KFM v11

**Deterministic governance pipeline:**

~~~~text
CI / Operator
   ↓
tools/cli
   ↓
tools/validation
   ↓
tools/governance
   ↓
tools/telemetry
   ↓
tools/ai
   ↓
Release Artifacts
(STAC/DCAT · Ledgers · Telemetry · SBOM · Contracts)
~~~~

This ensures **every promoted artifact is structurally valid, ethically safe, explainable, and fully governed.**

---

# ⚙️ 4. Validation Workflow (Safe Mermaid)

~~~~mermaid
flowchart TD
  A["Dataset / Model / Metadata"]
    --> B["Schema Check\n(STAC · DCAT · JSON-LD · Contracts)"]
  B --> C["FAIR+CARE Validator\n(Sovereignty · A11y · Ethics)"]
  C --> D["Checksum Audit\n(sha256 integrity chains)"]
  D --> E["Explainability & Bias Audit\n(SHAP/LIME · Drift)"]
  E --> F["validator_manifest.json\nTelemetry · Governance Sync"]
~~~~

---

# 🧬 5. Stage Specifications

## 5.1 Schema Validation (`schema_check.py`)
- Validates STAC v11 profiles (Raster, EO, PROJ, KFM extensions)
- DCAT 3.0 JSON-LD datasets (+ distributions)
- Story Node v3 schema
- Telemetry v4 schema
- KFM Data Contracts (PDC v11)

## 5.2 FAIR+CARE Validator (`faircare_validator.py`)
- CARE label propagation checks
- Sovereignty conflicts + Indigenous protection overlays
- Licensing, attribution, usage rights
- Accessibility metadata

## 5.3 Checksum Audit (`checksum_audit.py`)
- sha256 calculation + comparison
- Ledger-based tamper detection
- PROV-O lineage emission

## 5.4 AI Explainability Audit (`ai_explainability_audit.py`)
- SHAP/LIME validity tests
- Bias/fairness scoring
- Drift detection (feature distribution + model output shift)
- Explainability metadata conformance for Focus Mode v3

---

# 📄 6. Example Validation Metadata Record

~~~~json
{
  "id": "validation_session_v11.0.1",
  "schema_passed": true,
  "checksum_verified": true,
  "faircare_compliant": true,
  "ai_explainability_score": 0.998,
  "bias_index": 0.017,
  "energy_wh": 2.4,
  "carbon_gco2e": 2.8,
  "validated_entities": [
    "data/processed/hydrology/streamflow.parquet"
  ],
  "signing_hash": "sha256:5a8b883f9...",
  "governance_registered": true,
  "timestamp": "2025-11-24T15:22:00Z",
  "validator": "@kfm-validation-core"
}
~~~~

---

# 🧠 7. FAIR+CARE Governance Matrix

| Principle | Enforcement | Oversight |
|----------|-------------|-----------|
| Findable | JSON-LD lineage, stable IDs | @kfm-data |
| Accessible | A11y metadata, open formats | @kfm-accessibility |
| Interoperable | STAC/DCAT/ISO/JSON-LD | @kfm-architecture |
| Reusable | Versioned configs + schemas | @kfm-design |
| Collective Benefit | Governance-led checks | @faircare-council |
| Authority to Control | CARE labels + sovereignty | @kfm-governance |
| Responsibility | Sustainability + ethics logs | @kfm-security |
| Ethics | Bias + sensitive content audits | @kfm-ethics |

---

# 🧰 8. Validation Tool Summary

| Tool | Purpose |
|------|---------|
| `schema_check.py` | Structural + semantic correctness |
| `faircare_validator.py` | CARE + ethics + sovereignty checks |
| `checksum_audit.py` | Integrity + lineage |
| `ai_explainability_audit.py` | Transparency + drift + fairness |
| `validator_manifest.json` | Aggregated results, telemetry, signing |

---

# 📦 9. Retention & Provenance Policy

| Artifact | Retention |
|----------|-----------|
| Schema Reports | 180 days |
| FAIR+CARE Logs | 365 days |
| Lineage (sha256) | Permanent |
| Signed Manifests | Permanent |

Rotation: automated via CI (`validation_cleanup.yml`)

---

# 🌱 10. Sustainability Metrics (v11 Targets)

| Metric | Target |
|--------|--------|
| Energy/run | ≤ 2.5 Wh |
| Carbon/run | ≤ 3.0 gCO₂e |
| Renewable energy | 100% |
| FAIR+CARE compliance | 100% |

---

# 🕰 11. Version History

| Version | Date | Summary |
|--------:|------|---------|
| v11.0.1 | 2025-11-24 | Cross-toolchain upgrade; v11 telemetry; sovereignty gates; stable tilde fences |
| v11.0.0 | 2025-11-19 | Initial v11 rewrite |
| v10.x | 2023–2025 | Earlier validation pipeline versions |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — MIT License**  
**Validation & FAIR+CARE Tools · MCP-DL v6.3 · KFM-MDP v11 · Diamond⁹ Ω / Crown∞Ω**  
[Back to Tools Index](../README.md) · [Docs Portal](../../../docs/) · [Governance Charter](../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>