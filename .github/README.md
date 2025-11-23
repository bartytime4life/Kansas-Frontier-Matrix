---
title: "⚙️ Kansas Frontier Matrix — GitHub Infrastructure Overview (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: ".github/README.md"
version: "v11.0.0"
last_updated: "2025-11-19"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Autonomous · FAIR+CARE Council Oversight"
backward_compatibility: "Aligned with v10.x → v11.x CI/CD model"
commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"
signature_ref: "../releases/v11.0.0/signature.sig"
attestation_ref: "../releases/v11.0.0/slsa-attestation.json"
sbom_ref: "../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../releases/v11.0.0/manifest.zip"
telemetry_ref: "../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../schemas/telemetry/github-readme-v11.json"
energy_schema: "../schemas/telemetry/energy-v2.json"
carbon_schema: "../schemas/telemetry/carbon-v2.json"
governance_ref: "../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"
license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
ontology_protocol_version: "KFM-OP v11.0"
pipeline_contract_version: "KFM-PDC v11.0"
status: "Active / Enforced"
doc_kind: "Overview"
intent: "github-infrastructure"
role: "infrastructure-hub"
category: "CI/CD · Governance · Automation"
classification: "Public Document"
sensitivity: "General (non-sensitive)"
sensitivity_level: "None"
public_exposure_risk: "Low"
risk_category: "Low"
redaction_required: false
indigenous_rights_flag: false
care_label: "Collective Benefit · Authority to Control · Responsibility · Ethics"
fair_category: "F1-A1-I1-R1"
data_steward: "KFM FAIR+CARE Council"
provenance_chain:
  - ".github/README.md@v10.0.0"
  - ".github/README.md@v10.3.2"
  - ".github/README.md@v10.4.0"
  - ".github/README.md@v10.4.1"
prov_profile: "PROV-O Plan + KFM Governance Extensions"
openlineage_profile: "OpenLineage v2.5 · CI/CD events only"
ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "CreativeWork"
  owl_time: "TemporalEntity"
  prov_o: "prov:Plan"
  geosparql: "geo:FeatureCollection"
json_schema_ref: "../schemas/json/github-readme-v11.schema.json"
shape_schema_ref: "../schemas/shacl/github-readme-v11-shape.ttl"
doc_uuid: "urn:kfm:doc:github-readme-v11.0.0"
semantic_document_id: "kfm-doc-github-readme"
event_source_id: "ledger:.github/README.md"
immutability_status: "mutable-plan"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
jurisdiction: "United States / Kansas"
lifecycle_stage: "stable"
ttl_policy: "Annual review"
sunset_policy: "Superseded upon next infrastructure update"
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

# ⚙️ **Kansas Frontier Matrix — GitHub Infrastructure Overview**  
`.github/README.md`

**The governed CI/CD, validation, and automation backbone of the Kansas Frontier Matrix monorepo.**

[![KFM-MDP v11](https://img.shields.io/badge/Markdown-KFM--MDP_v11.0.0-informational)](../docs/standards/kfm_markdown_protocol_superstandard.md)  
[![FAIR+CARE](https://img.shields.io/badge/Data-FAIR%2BCARE-gold)](../docs/standards/faircare/FAIRCARE-GUIDE.md)  
[![License: MIT](https://img.shields.io/badge/License-MIT-green)](../LICENSE)  
[![Status: Active](https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen)](#-version-history)

</div>

---

# 🧭 Purpose

The `.github/` directory implements the **GitHub infrastructure plane** of the Kansas Frontier Matrix (KFM):

- CI/CD pipelines that build, test, validate, and deploy the system  
- FAIR+CARE and governance enforcement for **every change**  
- STAC/DCAT, ontology, and JSON-LD schema validation  
- Security & supply-chain hardening (SBOM, SLSA-style attestations, vulnerability scanning)  
- Telemetry capture for Focus Mode, governance dashboards, and sustainability metrics  
- Issue / PR templates encoding documentation-first and ethics-first rules  

Nothing reaches:

- Protected branches (`main`, `release/*`)  
- The **Neo4j knowledge graph**  
- The **published STAC/DCAT catalogs**  

without successfully passing through `.github/` workflows.

---

# 🗂️ Directory Layout

```text
.github/                               # GitHub infrastructure plane
│
├── README.md                          # This overview document
├── ARCHITECTURE.md                    # (Optional) CI/CD & governance deep-dive
│
├── workflows/                         # GitHub Actions automation
│   ├── ci.yml                         # Core CI: lint, typecheck, test, build, schemas
│   ├── docs_validate.yml              # Markdown + YAML + KFM-MDP v11 validation
│   ├── stac_validate.yml              # STAC collection/item validation
│   ├── dcat_validate.yml              # DCAT dataset validation
│   ├── faircare_validate.yml          # FAIR+CARE & ethics checks
│   ├── data_pipeline.yml              # ETL/data workflows & lineage checks
│   ├── telemetry_export.yml           # Telemetry bundling for releases
│   ├── sbom_verify.yml                # SBOM + checksum + SLSA provenance
│   ├── site.yml                       # Docs + web build and deployment
│   └── security_audit.yml             # Dependency & workflow security scanning
│
├── ISSUE_TEMPLATE/                    # Issue templates (governance-aware)
│   ├── bug_report.md                  # For defects in code or data behavior
│   ├── feature_request.md             # New features / enhancements
│   └── data_issue.md                  # Dataset issues + CARE classification
│
├── PULL_REQUEST_TEMPLATE.md           # Required metadata: CARE, provenance, a11y, telemetry
├── CODEOWNERS                         # Module ownership & review boundaries
├── dependabot.yml                     # Automated dependency updates
└── SECURITY.md                        # Security & vulnerability disclosure policy
````

---

# 🧬 Role in the KFM Stack

```mermaid
flowchart TB
  subgraph Dev ["Developer & Data Contributor Space"]
    A["Code & Data Changes<br/>src · web · data · docs"] --> B["Pull Request"]
  end

  subgraph Hub ["GitHub Infrastructure Plane (.github)"]
    B --> C["Workflows<br/>.github/workflows/*"]
    C --> D["Validation & Governance<br/>Lint · Tests · Schemas · FAIR+CARE · Security"]
    D --> E["Artifacts & Telemetry<br/>SBOM · Reports · Focus Telemetry"]
  end

  E --> F["Protected Branches<br/>main · release/*"]
  F --> G["Deployments<br/>Graph · Web · Docs · Data Releases"]
```

The `.github/` directory is a **first-class subsystem**. It:

* Encodes the **policies and standards** described in `ARCHITECTURE.md` and `docs/standards/*`
* Enforces **FAIR+CARE**, sovereignty, and reliability rules at the CI/CD level
* Guards the **software and data supply chain**
* Produces **telemetry and governance artifacts** used across the platform

---

# 🧪 CI/CD Stages (v11)

All workflows together implement a **multi-stage, governance-aware CI/CD pipeline**.

## 1️⃣ Lint & Style

* **Code**: ESLint, Prettier, TypeScript checks
* **CSS/Styles**: Stylelint and design-token lints
* **Markdown**:

  * KFM-MDP v11 conformance
  * YAML front-matter validation (required keys, valid paths)
  * Fence integrity (no broken boxes, valid inner code blocks)

Any lint failure → **PR blocked**.

## 2️⃣ Schema & Metadata Validation

Ensures all persisted artifacts are **schema-conformant**:

* STAC Items & Collections (`schemas/stac/*`)
* DCAT Datasets (`schemas/dcat/*`)
* Telemetry payloads (`schemas/telemetry/*`)
* JSON-LD contexts (`schemas/jsonld/*`)
* Story Node v3 & Focus Mode schemas
* GitHub-doc JSON/SHACL shapes (including this file’s schema)

Any schema violation → **no merge**.

## 3️⃣ Testing (Unit → Integration → E2E)

* Unit tests (backend, frontend, pipelines)
* Integration tests (API↔graph↔data)
* E2E tests for key flows
* Accessibility tests (where configured)
* Data validation tests for ETL outputs

No green test matrix → **no merges**.

## 4️⃣ Governance & Ethics Enforcement

Via `faircare_validate.yml` and linked standards:

* FAIR metrics (F1–A1–I1–R1)
* CARE classification and enforcement for sensitive data
* Coordinate masking and generalization rules (H3 standards)
* License & usage rights checks
* Provenance completeness and integrity

Governance failures require FAIR+CARE Council or delegate review.

## 5️⃣ Security & Supply Chain

Using `security_audit.yml`, `dependabot.yml`, `sbom_verify.yml`:

* Dependency vulnerability scanning
* SBOM generation and signature verification
* SLSA-style provenance for releases
* Workflows scanned for:

  * Unsafe permissions
  * Secret exposures
  * Dangerous patterns

Security is baked into the CI/CD process, not bolted on later.

## 6️⃣ Build, Package & Deploy

* Web client build (React + MapLibre + Cesium)
* Documentation site build
* Packaging:

  * `manifest.zip`
  * `sbom.spdx.json`
  * `focus-telemetry.json`

Only artifacts passing all previous stages may be deployed or published.

---

# 🧩 Governance & Policy Hooks

## Issue Templates (`ISSUE_TEMPLATE/`)

Each template encodes governance prompts:

* **Bug Report**:

  * Impacted subsystem (src, web, data, docs, pipelines)
  * Severity and potential data/UX impact

* **Feature Request**:

  * User story and beneficiaries
  * A11y, performance, and governance implications

* **Data Issue**:

  * Dataset identifiers (STAC/DCAT IDs)
  * CARE classification and sovereignty notes
  * Requested changes (masking, removal, correction)

## PR Template (`PULL_REQUEST_TEMPLATE.md`)

Pull requests must capture:

* CARE / sensitivity classification
* Provenance & licensing for data / narrative content
* Schema & ontology impacts
* Accessibility impacts
* Telemetry / Observability changes
* Required reviewers (CODEOWNERS + governance delegates as needed)

This enforces **documentation-first** and **governance-first** development.

---

# 🔒 Security Model

Core controls:

* Protected branches (`main`, `release/*`) with required checks
* CODEOWNERS for critical directories (e.g., `.github/**`, `schemas/**`, `data/**`)
* Restricted permissions for workflow tokens and environment secrets
* Security scanning and SBOM verification integrated into CI
* A documented **security and disclosure policy** in `.github/SECURITY.md`

Security issues are handled per that policy, with coordinated disclosure when appropriate.

---

# 📊 Telemetry & Observability

`.github` workflows feed telemetry into the KFM observability layer:

* CI duration and flakiness
* Validation and test failure patterns
* Governance violation counts and resolution times
* Energy and carbon estimates for workflow runs
* A11y and performance signal summaries

Telemetry is consolidated into:

```text
releases/<version>/focus-telemetry.json
```

and used to power:

* FAIR+CARE governance dashboards
* Reliability & sustainability reports
* System-level Story Nodes for Focus Mode v3

---

# 🕰 Version History

| Version |       Date | Summary                                                                                               |
| ------: | ---------: | ----------------------------------------------------------------------------------------------------- |
| v11.0.0 | 2025-11-19 | v11 upgrade; aligned with KFM-MDP v11, extended metadata, telemetry hooks, and CI/CD governance docs. |
| v10.4.1 | 2025-11-16 | Extended governance/AI metadata and refined directory overview.                                       |
| v10.4.0 | 2025-11-15 | Rewrote for KFM-MDP v10.4; clarified CI/CD + governance + telemetry architecture.                     |
| v10.3.2 | 2025-11-14 | Added STAC, DCAT, governance, and telemetry integration.                                              |
| v10.0.0 | 2025-11-10 | Initial GitHub infrastructure overview.                                                               |

---

[Root README](../README.md) · [Architecture](../ARCHITECTURE.md) · [Security Policy](./SECURITY.md)

```
