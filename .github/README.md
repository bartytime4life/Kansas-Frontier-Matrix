---
title: "⚙️ Kansas Frontier Matrix — GitHub Infrastructure Overview (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: ".github/README.md"
version: "v11.2.2"
last_updated: "2025-11-27"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Autonomous · FAIR+CARE Council Oversight"
backward_compatibility: "Aligned with v10.x → v11.x CI/CD model"
commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

signature_ref: "../releases/v11.2.2/signature.sig"
attestation_ref: "../releases/v11.2.2/slsa-attestation.json"
sbom_ref: "../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../releases/v11.2.2/manifest.zip"
telemetry_ref: "../releases/v11.2.2/focus-telemetry.json"
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
  - ".github/README.md@v11.0.2"

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

This document defines the **GitHub Infrastructure Plane** for KFM v11—governing all CI/CD, metadata validation, supply-chain hardening, and compliance automation wired into the `.github/` subsystem.

The `.github/` layer enforces:

- **Documentation-first (MCP-DL v6.3)**  
- **FAIR+CARE & sovereignty policies**  
- **STAC 1.x / DCAT 3.0 / JSON-LD schema compliance**  
- **OpenLineage-based pipeline provenance**  
- **Accessibility and ethics screening**  
- **Reliability/SLO gates & error budgets**  
- **Security governance & supply-chain integrity**  
- **Release integrity (SBOM, attestations)**  
- **Telemetry export** for Focus Mode v3 and governance dashboards  

`.github/` is the **single automated gatekeeper** between contributions and the governed production system.

---

## 🗂 Directory Layout

~~~text
.github/                             # GitHub governance & automation subsystem
│
├── 📄 README.md                     # This document
├── 🏗️ ARCHITECTURE.md               # CI/CD & standards deep-dive
│
├── 🤖 workflows/                    # GitHub Actions pipelines
│   ├── 🧪 ci.yml                    # Lint, tests, build, schema validation
│   ├── 📚 docs_validate.yml         # KFM-MDP v11.2.2 markdown & front-matter
│   ├── 🛰️ stac_validate.yml         # STAC Item/Collection validation
│   ├── 🗂️ dcat_validate.yml         # DCAT dataset validation
│   ├── 🧬 jsonld_validate.yml       # JSON-LD/ontology checks (CIDOC/OWL-Time/PROV-O)
│   ├── 🛡️ faircare_validate.yml     # FAIR+CARE & sovereignty enforcement
│   ├── 🧊 h3_generalization.yml     # Dynamic H3 generalization for sensitive coordinates
│   ├── 🔐 security_audit.yml        # Dependency & secret scanning, CVE checks
│   ├── 📦 sbom_verify.yml           # SBOM + manifest verification (SLSA-style)
│   ├── 🔁 data_pipeline.yml         # ETL, metadata pipeline tests, lineage validation
│   ├── 🤖 ai_behavior_check.yml     # AI behavior, drift, forbidden outputs
│   ├── 📊 telemetry_export.yml      # Telemetry → releases/<version>/focus-telemetry.json
│   └── 🌐 site.yml                  # Docs/web build & deploy
│
├── 📂 ISSUE_TEMPLATE/               # Governance-aware issue templates
│   ├── 🐛 bug_report.md             # Defects in code/data/narrative
│   ├── 💡 feature_request.md        # Enhancements (with CARE/a11y/perf prompts)
│   └── 🗺️ data_issue.md             # Dataset lineage/sensitivity reporting
│
├── 📜 PULL_REQUEST_TEMPLATE.md      # Required metadata: CARE, provenance, SBOM impact
├── 👥 CODEOWNERS                    # Ownership + review boundaries
├── 🧩 dependabot.yml                # Supply-chain and dependency automation
└── 🛡 SECURITY.md                   # Vulnerability disclosure & responsible reporting
~~~

This structure is normative for `.github` in v11.

---

## ⚙ CI/CD Architecture (Governed v11 Pipeline)

KFM v11 uses a **multi-stage, ontology-aware, FAIR+CARE-enforced CI/CD engine**.  
Every workflow emits **OpenLineage v2.5** events for provenance and audit trails.

### 🧩 Stage 1 — Lint & Style

- Prettier / ESLint / TypeScript  
- Stylelint  
- Python linters (ruff/flake8)  
- Markdown/Docs (**KFM-MDP v11.2.2**) structural checks  
- YAML front-matter & fenced-block integrity  
- Whitespace & no-tab enforcement  

Any violation → PR blocked.

---

### 📐 Stage 2 — Schema, Ontology & Metadata Validation

Validates:

- JSON Schema (all schemas in `schemas/**`)  
- STAC Items/Collections (`data/stac/**`)  
- DCAT Dataset descriptions (`schemas/dcat/**`)  
- Story Node v3 and Focus Mode v3 schemas  
- GeoSPARQL geometry validity  
- PROV-O lineage completeness  
- JSON-LD + ontology context mappings  

All core artifacts must validate before merge.

---

### 🧪 Stage 3 — Testing

Includes:

- Unit tests (backend, pipelines, graph, web)  
- Integration tests (API/graph/pipeline combos)  
- E2E tests (core user journeys)  
- A11y tests (WCAG 2.1 AA+ via Axe/Lighthouse)  
- Data validation tests (contracts, metadata completeness)  

Failures in Stage 3 block deployments to staging/production.

---

### 🛡️ Stage 4 — FAIR+CARE & Sovereignty Enforcement

Based on:

- `../docs/standards/faircare/FAIRCARE-GUIDE.md`  
- `../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md`  

Automations:

- CARE classification checks  
- Sovereignty-aware masking for sensitive locations (via H3)  
- Ethics checks on narrative and AI outputs  
- License and consent verification  

Infra-level governance events are captured via the `prov_profile` and streamed to governance dashboards.

---

### 🔒 Stage 5 — Security & Supply-Chain Integrity

Implements:

- Dependency vulnerability scanning  
- Secret scanning  
- Workflow and token hardening  
- Supply-chain validation via SBOM/SLSA  
- Dependabot orchestration per `.github/dependabot.yml`  

**Critical** security issues → automatic PR block until resolved.

---

### 📦 Stage 6 — Build, Package & Release

Outputs:

- Web client (React/MapLibre/Cesium) builds  
- Docs site artifacts  
- `manifest.zip`  
- `sbom.spdx.json` (signed & verified)  
- `focus-telemetry.json` for the release  

Only fully governed, green pipelines can produce release artifacts.

---

## 🧬 Governance, Ontologies & Lineage

`.github` encodes:

- **PROV-O Plan + KFM Governance Extensions** (`prov_profile`)  
- **OpenLineage v2.5 · CI/CD events only** (`openlineage_profile`)  

Each workflow:

- Acts as a **prov:Activity** realizing this plan  
- References inputs/outputs as **prov:Entity** instances  
- Emits OpenLineage events for pipeline & CI steps  

This creates an infrastructure-level provenance trail for all changes.

---

## 🛰 Telemetry, Reporting & Observability

Telemetry schema (`telemetry_schema`) covers:

- CI durations and pass/fail rates  
- Governance rule violations and enforcement counts  
- FAIR+CARE metrics (e.g., number of restricted datasets)  
- a11y metrics  
- Security & supply-chain events  
- Energy/carbon estimations from `energy_schema` and `carbon_schema`  

Telemetry is consolidated in:

```text
releases/<version>/focus-telemetry.json
```

and powers:

- Governance dashboards  
- SLO/SLI reports  
- Focus Mode v3 meta-context about system health  

---

## 🧭 Role of `.github/` in the KFM Stack

`.github/` functions as:

- The **policy and enforcement plane** for:
  - Data ingestion  
  - Pipelines & AI behaviors  
  - Graph schema evolution  
  - Documentation standards  
  - Web deployment  
  - Story Node & Focus Mode narrative safety  

- The glue that ensures **no code, data, or narrative** can reach production without:
  - Passing governance gates  
  - Being observable via telemetry  
  - Being properly documented and schematized  

---

## 🕰 Version History

| Version | Date       | Summary                                                                                                                    |
|--------:|------------|----------------------------------------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-27 | Updated to v11.2.2 style; aligned release references; applied emoji directory layout & standardized footer pattern.       |
| v11.0.2 | 2025-11-27 | Tightened descriptions of CI stages; clarified governance & security integration; synchronized with root ARCHITECTURE.    |
| v11.0.1 | 2025-11-23 | Semantic + structural v11 upgrade; enriched ontology, governance, lineage, AI behavior, telemetry, and security sections. |
| v11.0.0 | 2025-11-19 | Initial v11 GitHub infrastructure overview; aligned with v11 monorepo and CI/CD design.                                   |
| v10.4.1 | 2025-11-16 | Extended governance/AI metadata and refined directory overview.                                                           |
| v10.4.0 | 2025-11-15 | KFM-MDP v10.4 rewrite; clarified CI/CD + governance + telemetry architecture.                                            |
| v10.3.2 | 2025-11-14 | Added STAC, DCAT, governance, and telemetry integration.                                                                  |
| v10.0.0 | 2025-11-10 | Initial GitHub infrastructure overview.                                                                                   |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅️ Back](../README.md) · [🏗️ CI/CD Architecture](ARCHITECTURE.md) · [🛡️ Security Policy](SECURITY.md)

</div>