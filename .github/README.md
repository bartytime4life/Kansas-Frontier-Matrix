---
title: "⚙️ Kansas Frontier Matrix — GitHub Infrastructure Overview (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: ".github/README.md"
version: "v11.0.2"
last_updated: "2025-11-27"
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
markdown_protocol_version: "KFM-MDP v11.2.2"
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
  - ".github/README.md@v11.0.0"
  - ".github/README.md@v11.0.1"
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
doc_uuid: "urn:kfm:doc:github-readme-v11.0.2"
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

**The governed CI/CD, reliability, FAIR+CARE, supply-chain, and automation backbone of the Kansas Frontier Matrix monorepo.**

[![KFM-MDP v11.2.2](https://img.shields.io/badge/Markdown-KFM--MDP_v11.2.2-informational)](../docs/standards/kfm_markdown_protocol_v11.2.2.md) · [![FAIR+CARE](https://img.shields.io/badge/Data-FAIR%2BCARE-gold)](../docs/standards/faircare/FAIRCARE-GUIDE.md) · [![License: MIT](https://img.shields.io/badge/License-MIT-green)](../LICENSE) · [![Status: Active](https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen)](#-version-history)

</div>

---

## 📘 Overview

This document defines the **GitHub Infrastructure Plane** for KFM v11—governing all CI/CD, metadata validation, supply-chain hardening, and compliance automation.

The `.github/` subsystem enforces:

- Documentation-first (MCP-DL v6.3)  
- FAIR+CARE & sovereignty  
- STAC 1.x / DCAT 3.0 / JSON-LD schema compliance  
- OpenLineage provenance injection  
- Accessibility & ethics screening  
- Reliability/SLO gates  
- Security governance  
- Release integrity & attestations  
- Telemetry export for Focus Mode v3 & governance dashboards  

This is the **single automated gatekeeper** between contributions and the governed production system.

---

## 🗂 Directory Layout

```text
.github/                               # GitHub governance & automation subsystem
│
├── README.md                          # This document
├── ARCHITECTURE.md                    # Extended CI/CD & standards deep-dive
│
├── workflows/                         # GitHub Actions pipelines
│   ├── ci.yml                         # Full pipeline: lint, tests, build, schema-validate
│   ├── docs_validate.yml              # KFM-MDP v11 structural validation
│   ├── stac_validate.yml              # STAC 1.x validation of Items/Collections
│   ├── dcat_validate.yml              # DCAT 3.0 dataset validation
│   ├── jsonld_validate.yml            # JSON-LD, schema.org, PROV-O, ontology validation
│   ├── faircare_validate.yml          # FAIR+CARE ethics & sovereignty validation
│   ├── h3_generalization.yml          # Dynamic H3 generalization for sensitive coordinates
│   ├── security_audit.yml             # Dependency + secret scanning
│   ├── sbom_verify.yml                # SBOM verification (SLSA-style integrity)
│   ├── data_pipeline.yml              # ETL + metadata pipeline tests + lineage validation
│   ├── ai_behavior_check.yml          # AI compliance: explainability, drift, forbidden outputs
│   ├── telemetry_export.yml           # Telemetry → releases/<version>/focus-telemetry.json
│   └── site.yml                       # Docs + web build & deploy
│
├── ISSUE_TEMPLATE/                    # Governance-aware issue templates
│   ├── bug_report.md                  # Defects in code/data/narrative
│   ├── feature_request.md             # Enhancements (with CARE/a11y/perf prompts)
│   └── data_issue.md                  # Dataset lineage/sensitivity reporting
│
├── PULL_REQUEST_TEMPLATE.md           # Required metadata: CARE, provenance, SBOM impact
├── CODEOWNERS                         # Ownership boundaries for reviews
├── dependabot.yml                     # Supply-chain update automation
└── SECURITY.md                        # Vulnerability disclosure & responsible reporting
```

---

## ⚙️ CI/CD Architecture (Governed v11 Pipeline)

KFM v11 uses a **multi-stage, ontology-aware, FAIR+CARE-enforced CI/CD engine.**  
Every workflow feeds **OpenLineage v2.5** events for governance and reproducibility.

### 🧩 Stage 1 — Lint & Style

- Prettier / ESLint / TypeScript  
- Stylelint  
- Markdown/Docs (**KFM-MDP v11.2.2**) structure enforcement  
- YAML front-matter validation  
- Fence integrity checker  
- No-tabs-no-trailing-whitespace auditor  

Any violation blocks merge.

---

### 📐 Stage 2 — Schema, Ontology & Metadata Validation

Covers:

- JSON Schema  
- STAC (Item/Collection)  
- DCAT Dataset  
- Story Node v3  
- Focus Mode v3 narrative schema  
- GeoSPARQL geometry validity  
- PROV-O lineage completeness  
- JSON-LD contexts: CIDOC/OWL-Time alignment  

KFM v11 requires *all* schemas to validate before PR acceptance.

---

### 🧪 Stage 3 — Testing

- Unit tests (src, pipelines, web, graph)  
- Integration tests (graph, API, ETL nodes)  
- E2E tests  
- a11y (WCAG 2.1 AA+) automated screening  
- Data validation tests (e.g., metadata contract tests)  

Any failed stage halts the pipeline.

---

### 🛡️ Stage 4 — FAIR+CARE & Sovereignty Enforcement

Implements rules defined in:

- `FAIRCARE-GUIDE.md`  
- `INDIGENOUS-DATA-PROTECTION.md`  
- Dynamic H3 Generalization Standard v11  

Enforces:

- CARE classification  
- Coordinate masking for sensitive datasets  
- Sovereignty restrictions  
- Ethical filters for AI/narrative generation  
- License validation  

Governance violations → escalated to CARE Council.

---

### 🔒 Stage 5 — Security & Supply-Chain Integrity

Includes:

- SBOM verification  
- SLSA-style attestation checks  
- Vulnerability scanning  
- Secret scanning  
- Workflow hardening & permission minimization  
- Dependency update automation (Dependabot)  

Security failures → PR blocked.

---

### 📦 Stage 6 — Build, Package & Release

Outputs:

- Web client build (React + MapLibre + Cesium)  
- Docs site  
- `manifest.zip`  
- `sbom.spdx.json` (signed)  
- `focus-telemetry.json`  
- Release artifacts with provenance  

Only green builds and governance-approved changes deploy.

---

## 🧬 Integration with Governance, Ontologies & Lineage

`.github/` enforces alignment with:

- **CIDOC-CRM** (events, documents, procedures)  
- **OWL-Time** (temporal validity of changes)  
- **GeoSPARQL** (geometry validity in spatial datasets)  
- **PROV-O** (plan → activity → entity lineage)  
- **DCAT/JSON-LD** (dataset discoverability)  
- **OpenLineage** (pipeline event emission)  

Each CI stage drops lineage entries to the governance ledger.

---

## 🛰 Telemetry, Reporting & Observability

Workflows emit:

- CI duration & reliability  
- Governance event summaries  
- FAIR+CARE enforcement metrics  
- Schema violation statistics  
- a11y reports  
- Energy/carbon estimates  
- Build/test flakiness metrics  

Stored in:

```text
releases/<version>/focus-telemetry.json
```

Used for:

- Governance dashboards  
- SLO/SLI/Reliability scoring  
- Sustainability analysis  
- Focus Mode v3 reasoning context  

---

## 🧭 How `.github/` Connects with the Larger KFM Stack

`.github` is the **policy and enforcement layer** controlling:

- Data ingestion  
- ETL + metadata pipelines  
- Graph schema evolution  
- Document standards  
- Web app deployment  
- Story Node/Focus Mode narrative safety  

It ensures that **nothing unsafe or non-compliant enters the system.**

---

## 🕰 Version History

| Version | Date       | Summary                                                                                                                        |
|--------:|------------|--------------------------------------------------------------------------------------------------------------------------------|
| v11.0.2 | 2025-11-27 | Upgraded to KFM-MDP v11.2.2, corrected inline badge layout and footer, and aligned CI references with current markdown rules. |
| v11.0.1 | 2025-11-23 | Semantic + structural v11 upgrade; enriched ontology, governance, lineage, AI behavior, telemetry, and security integration.   |
| v11.0.0 | 2025-11-19 | Initial v11 migration with baseline metadata and CI/CD alignment.                                                             |
| v10.4.1 | 2025-11-16 | Extended governance/AI metadata and refined directory overview.                                                               |
| v10.4.0 | 2025-11-15 | KFM-MDP v10.4 rewrite; clarified CI/CD + governance + telemetry architecture.                                                |
| v10.3.2 | 2025-11-14 | Added STAC, DCAT, governance, and telemetry integration.                                                                     |
| v10.0.0 | 2025-11-10 | Initial GitHub infrastructure overview.                                                                                      |

---

<div align="center">

[Root README](../README.md) · [CI/CD Architecture](ARCHITECTURE.md) · [Security Policy](SECURITY.md)

</div>
