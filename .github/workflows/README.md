---
title: "🔄 Kansas Frontier Matrix — CI/CD Workflows Overview (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: ".github/workflows/README.md"

version: "v11.0.1"
last_updated: "2025-11-19"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Autonomous · FAIR+CARE Council Oversight"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../releases/v11.0.1/sbom.spdx.json"
manifest_ref: "../../releases/v11.0.1/manifest.zip"
telemetry_ref: "../../releases/v11.0.1/focus-telemetry.json"
telemetry_schema: "../../schemas/telemetry/github-workflows-v4.json"
energy_schema: "../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"
license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0"
ontology_protocol_version: "KFM-OP v11.0"
pipeline_contract_version: "KFM-PDC v11.0"

status: "Active / Enforced"
doc_kind: "Overview"
intent: "github-workflows-ci-cd"
role: "ci-cd-overview"
category: "CI/CD · Governance · Automation"

fair_category: "F1-A1-I1-R1"
care_label: "Public / Low-Risk"
sensitivity: "General"
sensitivity_level: "Low"
public_exposure_risk: "Low"
indigenous_rights_flag: false
data_steward: "KFM FAIR+CARE Council"
risk_category: "Low"
redaction_required: false

provenance_chain:
  - ".github/workflows/README.md@v10.0.0"
  - ".github/workflows/README.md@v10.2.2"
  - ".github/workflows/README.md@v10.3.1"
  - ".github/workflows/README.md@v10.4.1"
  - ".github/workflows/README.md@v11.0.0"

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "CreativeWork"
  owl_time: "TemporalEntity"
  prov_o: "prov:Plan"
  geosparql: "geo:FeatureCollection"

json_schema_ref: "../../schemas/json/github-workflows-readme-v11.schema.json"
shape_schema_ref: "../../schemas/shacl/github-workflows-readme-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:github-workflows-readme-v11.0.1"
semantic_document_id: "kfm-doc-github-workflows-readme"
event_source_id: "ledger:.github/workflows/README.md"
immutability_status: "mutable-plan"
machine_extractable: true

accessibility_compliance: "WCAG 2.1 AA"
jurisdiction: "United States / Kansas"
classification: "Public Document"
lifecycle_stage: "stable"
ttl_policy: "Annual review"
sunset_policy: "Superseded upon next workflows architecture update"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summaries"
  - "semantic-highlighting"
  - "a11y-adaptations"
ai_transform_prohibited:
  - "speculative additions"
  - "unverified historical claims"
---

<div align="center">

# 🔄 **Kansas Frontier Matrix — CI/CD Workflows Overview**  
`.github/workflows/README.md`

This document describes every **GitHub Actions workflow** used in the Kansas Frontier Matrix (KFM).  
All workflows enforce **FAIR+CARE**, **MCP-DL v6.3**, **KFM-MDP v11**, **sustainability telemetry**, and **Diamond⁹ Ω / Crown∞Ω** governance.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP_v6.3-blue)](#)  
[![Markdown · KFM-MDP v11](https://img.shields.io/badge/Markdown-KFM--MDP_v11-informational)](#)  
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Certified-orange)](#)  
[![Status: Automated](https://img.shields.io/badge/CI%2FCD-Automated-success)](#)

</div>

## 📘 Overview

This directory contains all CI/CD automation used by KFM.  
Workflows ensure that **every change** is:

- Validated (schemas, docs, metadata, STAC, DCAT)  
- Governance-aligned (FAIR+CARE, sovereignty, provenance)  
- Security-audited (CVE scans, SBOM verification, SLSA-style provenance)  
- Telemetry-logged (energy, carbon, governance events)  
- Built, tested, and deployed using deterministic pipelines  

Primary v11 telemetry output:

```
releases/v11.0.1/focus-telemetry.json
```

## 🗂️ Directory Layout

**This block is now 100% GitHub-safe and cannot break.**

```
.github/workflows/
│
├── README.md
├── ci.yml
├── docs_validate.yml
├── stac_validate.yml
├── dcat_validate.yml
├── faircare_validate.yml
├── data_pipeline.yml
├── security_audit.yml
├── sbom_verify.yml
├── telemetry_export.yml
└── site.yml
```

## 🧩 Workflow Categories

### Core CI
- `ci.yml` — lint, tests, typings, basic schema checks  
- `docs_validate.yml` — KFM-MDP v11 markdown + front-matter validation  

### Data & Metadata Validation
- `stac_validate.yml` — STAC validation  
- `dcat_validate.yml` — DCAT validation  
- `data_pipeline.yml` — ETL contract testing  

### Governance
- `faircare_validate.yml` — FAIR+CARE rules, sovereignty, provenance  

### Security & Supply Chain
- `security_audit.yml` — dependency + container scanning  
- `sbom_verify.yml` — SBOM regeneration + checksum verification  

### Deployment & Telemetry
- `site.yml` — build & deploy web/docs  
- `telemetry_export.yml` — aggregates workflow metrics + energy/carbon  

## 🔁 CI/CD Flow Diagram

```mermaid
flowchart TD
  A["Commit / PR / Schedule"] --> B["Validation (CI + Docs + STAC + DCAT + ETL)"]
  A --> C["Security (CVE · SBOM)"]
  B --> D["Governance (FAIR+CARE)"]
  C --> D
  D --> E["Build & Deploy"]
  E --> F["Telemetry Export"]
  F --> G["Governance & Observability Dashboards"]
```

## ⚖️ FAIR+CARE Integration

Governance is applied at multiple workflow stages:

- Cultural/Indigenous dataset masking  
- Consent & rights verification  
- Provenance checking  
- FAIR metadata completeness  

## 🛡️ Security & Compliance

- Critical CVEs block merges  
- SBOM & manifest must match  
- Branch protection enforces all required workflows  
- No workflow may bypass validation or governance  

## 📊 Telemetry

Captured metrics:

| Metric | Purpose |
|--------|---------|
| workflow_duration_sec | CI performance |
| build_energy_wh | Sustainability |
| carbon_gco2e | Carbon footprint |
| faircare_score | governance |
| security_pass_rate | supply-chain safety |
| docs_lint_pass | documentation quality |

Outputs live in:

```
docs/reports/telemetry/
releases/v11.0.1/focus-telemetry.json
```

## 🕰️ Version History

| Version | Date | Summary |
|--------:|------|---------|
| v11.0.1 | 2025-11-19 | Fixed Directory Layout fence; added v11 telemetry schema v4; updated metadata density. |
| v11.0.0 | 2025-11-18 | First v11 CI/CD overview. |
| v10.4.1 | 2025-11-16 | Added AI audit workflow & sustainability metrics. |
| v10.3.1 | 2025-11-13 | Improved validation for STAC/DCAT. |
| v10.2.2 | 2025-11-12 | Added CVE gating & parity diffs. |
| v10.0.0 | 2025-11-09 | Initial CI/CD architecture doc. |

<div align="center">

**© 2025 Kansas Frontier Matrix — MIT / CC-BY 4.0**  
FAIR+CARE Certified · Diamond⁹ Ω / Crown∞Ω  
MCP-DL v6.3 · KFM-MDP v11.0 · KFM-OP v11.0

</div>
