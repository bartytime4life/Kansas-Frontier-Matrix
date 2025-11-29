---
title: "⚙️ Kansas Frontier Matrix — GitHub Infrastructure Overview (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: ".github/README.md"
version: "v11.2.2"
last_updated: "2025-11-28"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Autonomous · FAIR+CARE Council Oversight"
backward_compatibility: "Aligned with v10.x → v11.2.2 CI/CD and metadata model"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

signature_ref: "../releases/v11.2.2/signature.sig"
attestation_ref: "../releases/v11.2.2/slsa-attestation.json"
sbom_ref: "../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../releases/v11.2.2/manifest.zip"
telemetry_ref: "../releases/v11.2.2/github-infra-telemetry.json"
telemetry_schema: "../schemas/telemetry/github-readme-v11.json"
energy_schema: "../schemas/telemetry/energy-v2.json"
carbon_schema: "../schemas/telemetry/carbon-v2.json"

governance_ref: "../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11.0"
pipeline_contract_version: "KFM-PDC v11.0"

status: "Active / Enforced"
doc_kind: "Overview"
intent: "github-infrastructure"
role: "infrastructure-hub"
category: "CI/CD · Governance · Automation · Telemetry"

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
  - ".github/README.md@v11.0.0"
  - ".github/README.md@v11.0.1"
  - ".github/README.md@v11.0.2"
  - ".github/README.md@v11.2.2"

prov_profile: "PROV-O Plan + KFM Governance Extensions"
openlineage_profile: "OpenLineage v2.5 · CI/CD and AI pipeline events"

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "CreativeWork"
  owl_time: "TemporalEntity"
  prov_o: "prov:Plan"
  geosparql: "geo:FeatureCollection"

json_schema_ref: "../schemas/json/github-readme-v11.schema.json"
shape_schema_ref: "../schemas/shacl/github-readme-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:github-readme-v11.2.2"
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

**The governed CI/CD, reliability, AI-safety, FAIR+CARE, sovereignty, and supply-chain backbone of the KFM v11.2.2 monorepo.**

[![KFM-MDP v11.2.2](https://img.shields.io/badge/Markdown-KFM--MDP_v11.2.2-informational)](../docs/standards/kfm_markdown_protocol_v11.2.2.md)
· [![FAIR+CARE](https://img.shields.io/badge/Data-FAIR%2BCARE-gold)](../docs/standards/faircare/FAIRCARE-GUIDE.md)
· [![License: MIT](https://img.shields.io/badge/License-MIT-green)](../LICENSE)
· [![Status: Active](https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen)](#-version-history)

</div>

---

## 📘 Overview

The `.github/` subsystem is the **automation, governance, provenance, AI-safety, and supply-chain enforcement layer** of the Kansas Frontier Matrix v11.2.2 repository.

It validates and governs **everything** flowing into KFM:

- deterministic pipelines & governed CI/CD  
- full ontology compliance (STAC, DCAT, JSON-LD, GeoSPARQL, CIDOC-CRM, OWL-Time)  
- FAIR+CARE ethics + sovereignty/H3-masking  
- AI behavior, narrative safety, drift & bias detection  
- supply-chain security (SBOM, attestations, dependency policy)  
- release signing & manifest sealing  
- telemetry export for governance dashboards & Focus Mode system health  

`.github/` is the **policy brain + security perimeter** for the entire monorepo.

---

## 🗂️ Directory Layout (Full v11.2.2)

~~~text
.github/                                           # 🧭 GitHub governance & automation subsystem
│
├── 📄 README.md                                   # Infra overview (this file)
├── 🏗️ ARCHITECTURE.md                             # Deep-governance CI/CD architecture spec
│
├── 🤖 workflows/                                  # GitHub Actions CI/CD + AI + governance pipelines
│   ├── 🧪 ci.yml                                  # Core CI: linting, typing, tests, schema checks
│   ├── 📚 docs_validate.yml                       # KFM-MDP v11.2.2 markdown + YAML validation
│   ├── 🛰️ stac_validate.yml                       # STAC 1.x Item/Collection validation
│   ├── 🗂️ dcat_validate.yml                       # DCAT 3.0 dataset + distribution validation
│   ├── 🧬 jsonld_validate.yml                     # JSON-LD/CIDOC/OWL-Time/GeoSPARQL validation
│   ├── 🛡️ faircare_validate.yml                   # FAIR+CARE, sovereignty, ethics enforcement
│   ├── 🧊 h3_generalization.yml                   # Sensitive-location H3 masking (tribal, archaeology)
│   ├── 🔐 security_audit.yml                      # CVEs, dependency review, secret scanning
│   ├── 📦 sbom_verify.yml                         # SBOM + manifest + SLSA attestation checks
│   ├── 🔁 data_pipeline.yml                       # ETL lineage tests & data contract checking
│   ├── 🌡️ climate_mlops.yml                       # Climate model MLOps governance
│   ├── 💧 hydrology_mlops.yml                     # Hydrology models/indices governance
│   ├── 🌪️ hazards_mlops.yml                       # Tornado/hail/flood/fire model governance
│   ├── 🔡 embeddings_mlops.yml                    # Embeddings (spatial/climate/hydro/etc.)
│   ├── 🎯 focusmode_mlops.yml                     # Focus Mode v3 narrative-safety + fusion checks
│   ├── 🤖 ai_behavior_check.yml                   # LLM behavior, drift, bias, forbidden-output detection
│   ├── 📊 telemetry_export.yml                    # CI/AI telemetry → releases/<version>/github-infra-telemetry.json
│   ├── 🚀 release.yml                             # Signed release packaging + manifest generation
│   ├── 🏷️ labeler.yml                             # Auto-labeling PRs by component/domain
│   └── 🌐 site.yml                                # docs + web build/deploy
│
├── 🧱 actions/                                    # Reusable composite governance actions
│   ├── 📐 markdown-lint/                          # KFM-MDP v11 markdown rules enforcement
│   ├── 🧾 schema-validate/                        # JSON/YAML schema validation
│   ├── 🛰️ stac-validate/                          # STAC validator wrapper
│   ├── 🗂️ dcat-validate/                          # DCAT checker wrapper
│   ├── 🧪 pytest-runner/                          # Unified Python test execution
│   └── 🔍 security-scan/                          # Hardened scanning logic for dependencies/secrets
│
├── 📂 ISSUE_TEMPLATE/                             # Issue governance templates
│   ├── 🐛 bug_report.md                           # Defects (pipelines, AI, datasets, docs)
│   ├── 💡 feature_request.md                      # Enhancements + governance prompts
│   ├── 🗺️ data_issue.md                           # Data lineage/sensitivity/STAC/DCAT/CARE issues
│   └── ⚖️ governance_issue.md                     # Policy, ethics, sovereignty, CARE-related issues
│
├── ⚙️ ISSUE_TEMPLATE/config.yml                   # Routing, required fields, auto-label logic
├── 📜 PULL_REQUEST_TEMPLATE.md                    # Required PR metadata (provenance, SBOM, CARE)
├── 👥 CODEOWNERS                                  # Ownership boundaries for governed domains
├── 🧩 dependabot.yml                              # Supply-chain dependency automation
├── 💸 FUNDING.yml                                 # Repository sponsor options
├── 📏 CODE_OF_CONDUCT.md                          # Community standards
└── 🛡 SECURITY.md                                 # Vulnerability disclosure policy
~~~

---

## 👥 Contribution & Review Governance

PRs MUST include:

- ✔ Provenance metadata (source, lineage, affected entities)  
- ✔ SBOM impact note  
- ✔ Telemetry impact note  
- ✔ FAIR+CARE/sovereignty impact assessment  
- ✔ Schema validation (JSON, YAML, STAC, DCAT, JSON-LD)  
- ✔ Passing AI-behavior + narrative-safety checks  
- ✔ Approval from **all required CODEOWNERS**

**CODEOWNERS** enforce multi-council governance:

| Domain | Owners |
|--------|--------|
| Data | Data Stewardship Council |
| AI/Models | AI Safety & Narrative Governance Board |
| Documentation | FAIR+CARE Council |
| Web/UI | Web Experience Engineering |
| Security | Security Response Group |
| Pipelines | Infrastructure & Provenance Committee |

No merge is allowed without required approvals.

---

## 🛡 Security & Supply-Chain Governance

### security_audit.yml enforces:
- CVE thresholds (block if severity ≥ HIGH)  
- dependency freshness policy  
- secret scanning  
- lockfile integrity  
- SLSA-aligned provenance  

### Dependabot rules:
- Patch bumps auto-merge allowed  
- Minor bumps require CODEOWNER review  
- Major bumps require governance approval  

### SECURITY.md defines:
- vulnerability reporting  
- triage / remediation SLA  
- responsible disclosure  
- embargo procedures  

---

## 📦 Release Artifacts (Manifest, Attestations, Telemetry)

Produced by `release.yml` + `sbom_verify.yml` + `telemetry_export.yml`:

| Artifact | Purpose |
|---------|----------|
| **SBOM (spdx.json)** | full dependency + provenance inventory |
| **Manifest (manifest.zip/json)** | authoritative registry of release assets |
| **Signature (.sig)** | cryptographic authenticity |
| **SLSA Attestation** | supply-chain provenance |
| **Telemetry (OpenTelemetry JSON)** | pipeline behavior, AI governance outcomes, energy/carbon |

These feed downstream:

- Governance dashboards  
- Interpreter-side AI context (Focus Mode system health)  
- Model cards  
- STAC/DCAT dataset catalogs  

---

## 🌉 Branch Protection & Environments

### Required checks for all protected branches:
- ci.yml  
- docs_validate.yml  
- stac_validate.yml  
- dcat_validate.yml  
- jsonld_validate.yml  
- faircare_validate.yml  
- h3_generalization.yml  
- ai_behavior_check.yml  
- security_audit.yml  
- sbom_verify.yml  
- telemetry_export.yml  

### Environments:
- **dev → staging** — auto-promotion  
- **staging → production** — manual review + signing required  

All promotions are auditable via OpenLineage events.

---

## 🧱 Reusable Composite Actions

Composite actions enforce consistency across workflows:

- **markdown-lint/** → KFM-MDP v11.2.2 compliance  
- **schema-validate/** → JSON/YAML schema integrity  
- **stac-validate/** → STAC compliance  
- **dcat-validate/** → DCAT compliance  
- **pytest-runner/** → unified testing  
- **security-scan/** → hardened security scanning  

All new workflows MUST reuse these patterns.

---

## 🤖 AI & Focus Mode Governance

### ai_behavior_check.yml:
- checks for prohibited outputs (speculation, harmful claims, fabricated data)  
- ensures sovereignty rules enforced  
- detects drift, bias, anomalies  
- scores CARE compliance  
- validates grounding + citation for narratives  

### focusmode_mlops.yml:
- validates fusion/routing models  
- ensures model-card & narrative-safety requirements  
- checks explainability artifacts  
- validates adherence to ontology mappings  

---

## ⚖ FAIR+CARE & Sovereignty Enforcement

### FAIR rules enforced through:
- STAC metadata completeness  
- DCAT dataset registration  
- JSON-LD + PROV-O provenance requirements  

### CARE rules enforced through:
- CARE labels  
- contextual sensitivity checks  
- automatic H3 generalization for archaeological/tribal sites  
- refusal mechanisms for disallowed narratives  

A merge is blocked if any CARE/sovereignty violation occurs.

---

## 🔗 Mapping `.github/` → Monorepo Domains

| Path | Validations | Governance Owner |
|------|-------------|-------------------|
| `src/pipelines/` | lineage, schema, FAIR+CARE, security | Infra + Data |
| `data/` | STAC, DCAT, masking, metadata | Data Council |
| `web/` | security, build, telemetry | Web |
| `docs/` | MDP validation, provenance | FAIR+CARE Council |
| `mcp/` | reproducibility, experiments | Research Council |

---

## 🛠 Extending GitHub Infrastructure (Rules)

When adding a new workflow:

1. MUST reuse composite actions (`actions/*`)  
2. MUST produce telemetry  
3. MUST include schema validation  
4. MUST update this README + ARCHITECTURE.md  
5. MUST bump version/last_updated  
6. MUST align with FAIR+CARE & sovereignty policy  
7. MUST be approved by appropriate CODEOWNERS  

---

## ⚙ CI/CD Architecture Summary

Stages:

1. Lint & Style  
2. Schema & Ontology Validation  
3. Testing  
4. FAIR+CARE Enforcement  
5. Security & Supply-Chain Governance  
6. Release Packaging & Signing  

Everything emits OpenLineage v2.5 events.

---

## 🧬 Governance & Lineage

Governance uses **prov:Plan → prov:Activity → prov:Entity** modeling.  
Each workflow, release, dataset, and AI inference is fully traceable.

Artifacts (manifest, SBOM, telemetry, attestations) are all linked back to commits & workflows.

---

## 🛰 Telemetry & Observability

Telemetry captures:

- schema failures  
- FAIR+CARE violations  
- sovereignty/H3 events  
- CVEs/security incidents  
- energy usage + carbon emissions  
- AI narrative-safety metrics  
- pipeline duration & reliability  

Used by:  
- **Governance dashboards**  
- **AI Focus Mode system health**  
- **Release readiness reviews**

---

## 🧭 Role of `.github/` in KFM v11.2.2

`.github/` is the authoritative **policy + automation + provenance plane**.

It controls:

- data integrity  
- AI integrity  
- documentation integrity  
- release integrity  
- security integrity  

Nothing enters production unless:

1. ✔ all CI validations pass  
2. ✔ FAIR+CARE is satisfied  
3. ✔ provenance is complete  
4. ✔ schema compliance is verified  
5. ✔ security is green  

---

## 🕰 Version History

| Version | Date | Summary |
|--------:|------|---------|
| v11.2.2 | 2025-11-28 | Full v11.2 rebuild + governance + AI + security + sovereignty + telemetry expansion |
| v11.0.2 | 2025-11-27 | Governance refinements & supply-chain improvements |
| v11.0.1 | 2025-11-23 | Ontology, metadata, narrative-safety enhancements |
| v11.0.0 | 2025-11-19 | First governed v11 GitHub infrastructure README |
| v10.4.1 | 2025-11-16 | Pre-v11 FAIR+CARE integration expansion |
| v10.4.0 | 2025-11-15 | KFM-MDP v10.4 rewrite |
| v10.3.2 | 2025-11-14 | Telemetry integration |
| v10.0.0 | 2025-11-10 | First infrastructure documentation |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅️ Back to Repository](../README.md) · [📐 Architecture](ARCHITECTURE.md) · [🛡 Security Policy](SECURITY.md)

</div>
