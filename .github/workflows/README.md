---
title: "🔄 Kansas Frontier Matrix — CI/CD Workflows Master Architecture (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: ".github/workflows/README.md"
version: "v11.2.2"
last_updated: "2025-11-28"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Autonomous · FAIR+CARE Council Oversight"
content_stability: "stable"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../releases/v11.2.2/github-infra-telemetry.json"
telemetry_schema: "../../schemas/telemetry/github-workflows-v4.json"
energy_schema: "../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"

status: "Active / Enforced"
doc_kind: "Architecture"
intent: "github-workflows-ci-cd-master"
role: "ci-cd-overview"
category: "CI/CD · Governance · Automation · Security · Telemetry"

classification: "Public Document"
sensitivity: "General"
sensitivity_level: "None"
public_exposure_risk: "Low"
indigenous_rights_flag: false
data_steward: "KFM FAIR+CARE Council"
risk_category: "Low"
redaction_required: false

fair_category: "F1-A1-I1-R1"
care_label: "Public / Low-Risk"

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "CreativeWork"
  owl_time: "TemporalEntity"
  prov_o: "prov:Plan"
  geosparql: "geo:FeatureCollection"

metadata_profiles:
  - "STAC 1.0.0"
  - "DCAT 3.0"
  - "PROV-O"
  - "FAIR+CARE"

provenance_chain:
  - ".github/workflows/README.md@v11.2.0"
  - ".github/workflows/README.md@v11.0.2"
  - ".github/workflows/README.md@v11.0.1"
  - ".github/workflows/README.md@v11.0.0"
  - ".github/workflows/README.md@v10.4.1"
  - ".github/workflows/README.md@v10.3.1"
  - ".github/workflows/README.md@v10.2.2"
  - ".github/workflows/README.md@v10.0.0"
provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: false

json_schema_ref: "../../schemas/json/github-workflows-readme-v11.schema.json"
shape_schema_ref: "../../schemas/shacl/github-workflows-readme-v11-shape.ttl"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summaries"
  - "semantic-highlighting"
  - "a11y-adaptations"
  - "diagram-extraction"
  - "metadata-extraction"
ai_transform_prohibited:
  - "speculative-additions"
  - "unverified-historical-claims"
  - "governance-override"
  - "content-alteration"

layout_profiles:
  - "immediate-one-branch-with-descriptions-and-emojis"
badge_profiles:
  - "root-centered-badge-row"
requires_purpose_block: true
requires_directory_layout_section: true
requires_version_history: true
requires_governance_links_in_footer: true

doc_uuid: "urn:kfm:doc:github-workflows:architecture:v11.2.2"
semantic_document_id: "kfm-doc-github-workflows-readme"
event_source_id: "ledger:.github/workflows/README.md"
immutability_status: "mutable-plan"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

jurisdiction: "United States / Kansas"
lifecycle_stage: "stable"
ttl_policy: "Annual review"
sunset_policy: "Superseded upon next CI/CD architecture update"
---

<div align="center">

# 🔄 **Kansas Frontier Matrix — CI/CD Workflows Master Architecture (v11.2.2 LTS)**  
`.github/workflows/README.md`

[![KFM-MDP v11.2.2](https://img.shields.io/badge/Markdown-KFM--MDP_v11.2.2-blue)](../../docs/standards/kfm_markdown_protocol_v11.2.2.md)
[![FAIR+CARE](https://img.shields.io/badge/Data-FAIR%2BCARE-gold)](../../docs/standards/faircare/FAIRCARE-GUIDE.md)
[![CI/CD](https://img.shields.io/badge/Pipelines-Automated-success)]()
[![Security](https://img.shields.io/badge/Supply--Chain-Secure-critical)]()
[![Telemetry](https://img.shields.io/badge/Telemetry-OpenLineage%20%2B%20OTel-9c27b0)]()
[![License: MIT](https://img.shields.io/badge/License-MIT-green)](../../LICENSE)

**Purpose**  
Describe the **canonical CI/CD architecture** for all workflows in `.github/workflows/` that implement  
validation, FAIR+CARE governance, supply-chain integrity, security, telemetry, data lineage, and automated deployment  
for the Kansas Frontier Matrix (KFM) v11.2.2 monorepo.

</div>

---

## 📘 Overview

This document is the **master CI/CD architecture spec** for KFM:

- Treats GitHub Actions as a **governed policy engine**, not just build scripts.  
- Defines how workflows together realize a **prov:Plan** for safe evolution of code, data, models, and narratives.  
- Connects CI/CD behavior to **FAIR+CARE**, **sovereignty**, **ontology**, and **supply-chain** standards.  
- Ensures every change is **reproducible, observable, auditable**, and **ethically constrained**.

Workflows in this directory:

- **Validate** code, docs, schemas, and geospatial/temporal metadata.  
- **Enforce** FAIR+CARE and sovereignty rules.  
- **Protect** supply-chain and secrets.  
- **Govern** AI models, Story Nodes, and Focus Mode narratives.  
- **Emit** OpenTelemetry + OpenLineage telemetry into KFM’s governance data lake.  

---

## 🗂️ Directory Layout

~~~text
.github/
└── 🤖 workflows/                             # All governed CI/CD workflows (this directory)
    ├── 🧪 ci.yml                             # Core CI: lint, tests, type-checks, base schema checks
    ├── 📚 docs_validate.yml                  # KFM-MDP v11.2.2 markdown + front-matter validation
    ├── 🛰️ stac_validate.yml                  # STAC 1.x Item/Collection validation (data/stac/**)
    ├── 🗂️ dcat_validate.yml                  # DCAT 3.0 dataset/distribution validation
    ├── 🧬 jsonld_validate.yml                # JSON-LD + ontology checks (CIDOC/OWL-Time/GeoSPARQL/PROV-O)
    ├── ⚖️ faircare_validate.yml              # FAIR+CARE & ethics checks
    ├── 🧊 h3_generalization.yml              # H3 generalization enforcement for sensitive coordinates
    ├── 🔐 security_audit.yml                 # Dependency CVEs, secret scanning, workflow hardening
    ├── 📦 sbom_verify.yml                    # SBOM + manifest + SLSA attestation verification
    ├── 🔁 data_pipeline.yml                  # ETL contract & lineage validation (KFM-PDC v11)
    ├── 🤖 ai_behavior_check.yml              # AI behavior, drift, bias, forbidden narratives
    ├── 🎯 focusmode_mlops.yml                # Focus Mode v3 MLOps (fusion, narrative safety, explainability)
    ├── 📊 telemetry_export.yml               # Telemetry aggregation → github-infra-telemetry.json
    ├── 🚀 release.yml                        # Signed release packaging, manifest, SBOM
    ├── 🏷️ labeler.yml                        # Auto-label PRs by component/domain
    └── 🌐 site.yml                           # Web + docs build & deployment pipelines
~~~

Any new workflow added to this directory MUST be:

- Documented in this README.  
- Wired into schemas under `schemas/telemetry/` where it affects telemetry.  
- Aligned with FAIR+CARE and sovereignty policy documents.

---

## 🧱 Architecture

At a high level, `.github/workflows/` implements a **multi-stage gate**:

~~~mermaid
flowchart TB
    A["🔔 Triggers\npush · PR · schedule · manual"] --> B["🧪 Core CI\nci.yml"]
    B --> C["📚 Docs & Metadata\n docs_validate · stac_validate · dcat_validate · jsonld_validate"]
    C --> D["⚖ Governance\n faircare_validate · h3_generalization"]
    D --> E["🔐 Security & Supply Chain\n security_audit · sbom_verify"]
    E --> F["📦 Build & Release\n site · release"]
    F --> G["📊 Telemetry & Lineage\n telemetry_export + OpenLineage"]
~~~

**Design principles:**

- **Single-pass correctness**: each stage either passes or fails; no “best-effort” modes for core governance.  
- **Path-aware execution**: workflows trigger only when relevant files change, but never skip required checks for those paths.  
- **Provenance-first**: every critical step emits lineage and telemetry, forming an audit graph.  

---

## 🧪 Validation & CI/CD

### Core CI (`ci.yml`)

- Runs for most PRs and pushes.  
- Responsibilities:
  - Linting (TS/JS/CSS/Python).  
  - Unit + integration tests.  
  - Minimal schema checks (e.g., config files).  
- Provides a **fast feedback loop** before deeper governance workflows.

---

### Documentation, Metadata & Ontology

**`docs_validate.yml`**

- Enforces **KFM-MDP v11.2.2**, including:  
  - YAML front-matter presence & shape.  
  - Heading hierarchy & emoji usage.  
  - Single fenced block rule (for generated docs) where applicable.  
  - Directory layout & version history sections for governed docs.

**`stac_validate.yml` / `dcat_validate.yml` / `jsonld_validate.yml`**

- Enforce KFM-STAC v11 & KFM-DCAT v11:
  - Bounding boxes, datetimes, CRS, licenses, and assets for STAC.  
  - Dataset metadata, distributions, and contexts for DCAT.  

- Validate JSON-LD & ontology alignment:
  - CIDOC-CRM classes and properties.  
  - OWL-Time time instants/intervals for events & datasets.  
  - GeoSPARQL geometry representation.

Failures anywhere in this block **block merges and releases**.

---

### FAIR+CARE, Sovereignty & H3

**`faircare_validate.yml`**

- Validates:
  - CARE labels and FAIR categories in metadata.  
  - Sovereignty flags for Indigenous and culturally sensitive data.  
  - Presence of references to relevant policy docs when required.  

**`h3_generalization.yml`**

- Automatically checks for high-precision coordinates in sensitive layers.  
- Ensures they are generalized to H3 (or masked) as per policy.  
- Validates metadata flags indicating generalization was applied.

Result: No PR can silently introduce high-risk site coordinates or ungoverned sensitive content.

---

### Security & Supply-Chain

**`security_audit.yml`**

- Performs:
  - Dependency scanning (npm, Python, Actions).  
  - Secret scanning (config, code, tests).  
  - Optional container scanning.  
- Policy:
  - Critical CVEs → block.  
  - High CVEs → require explicit governance sign-off.

**`sbom_verify.yml`**

- Checks:
  - SBOM presence and schema.  
  - Alignment with `manifest.zip`.  
  - SLSA-style attestation presence.  
- Ensures each release is **cryptographically and supply-chain sound**.

---

### Data Pipelines & Lineage (`data_pipeline.yml`)

- Ensures:
  - Pipeline configs adhere to KFM-PDC v11 contracts.  
  - Lineage events are emitted and can be joined to ETL assets.  
  - Backfills and historical reconstructions are properly tagged.  

This workflow helps ensure that all ETL-derived products remain reproducible and explainable.

---

### AI & Focus Mode Governance

**`ai_behavior_check.yml`**

- Detects:
  - Prohibited content patterns in AI outputs.  
  - Inadequate grounding or missing citations.  
  - Potential bias or harmful narrative patterns.  

**`focusmode_mlops.yml`**

- Validates:
  - Story Node and Focus Mode model configurations.  
  - Presence and freshness of model cards (`mcp/model_cards/**`).  
  - Explainability artifacts for critical models (where required).  

No AI or Focus Mode change is allowed to bypass governance or narrative-safety checks.

---

### Telemetry & Reporting (`telemetry_export.yml`)

- Collects:
  - Per-workflow pass/fail counts.  
  - Governance violation counts.  
  - Energy & carbon estimates per pipeline.  
  - High-level SLO/SLA metrics.

- Writes to `github-infra-telemetry.json` using `github-workflows-v4.json` schema.  
- Enables governance dashboards and system health Story Nodes.

---

### Site & Release Workflows (`site.yml`, `release.yml`)

- **`site.yml`**
  - Builds and optionally deploys:
    - Web app (MapLibre/Cesium).  
    - Docs site.  

- **`release.yml`**
  - Creates signed GitHub Releases.  
  - Attaches SBOM, manifest, and telemetry.  
  - Emits final OpenLineage events marking release completion.

---

## 📦 Data & Metadata

This architecture treats workflows as first-class **metadata producers**:

- Each workflow is a `prov:Activity` executing the CI/CD plan.  
- Artifacts like SBOMs, manifests, telemetry JSON, and logs are `prov:Entity` instances.  
- `telemetry_schema`, `energy_schema`, and `carbon_schema` define how performance, sustainability, and governance metrics are recorded.

These artifacts:

- Are referenced from `data/releases/` and `docs/` for audit and reproducibility.  
- Can be ingested into STAC/DCAT-like catalogs for release-level discovery.  
- Provide Focus Mode with context for system health and reliability narratives.

---

## ⚖ FAIR+CARE & Governance

Within CI/CD, FAIR+CARE is operationalized as:

- **FAIR**  
  - Metadata tests for findability, accessibility, interoperability, and reusability.  
  - Required provenance (provenance_chain, doc_uuid, semantic_document_id).  

- **CARE**  
  - CARE labels enforced on relevant datasets.  
  - Sovereignty policies applied via `faircare_validate` and `h3_generalization`.  
  - Governance references checked and required for sensitive domains.

Governance documents referenced in front-matter are **normative** for these workflows.

---

## 🕰️ Version History

| Version | Date       | Summary                                                                                                                                |
|--------:|------------|----------------------------------------------------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-28 | Deep v11.2.2 architecture update; aligned with updated GitHub Infra README; clarified workflow roles, telemetry, and FAIR+CARE wiring. |
| v11.2.0 | 2025-11-27 | First v11.2 CI/CD master architecture; consolidated governance, security, AI, and telemetry views.                                     |
| v11.0.2 | 2025-11-19 | Expanded ETL and lineage workflows; added sustainability considerations.                                                               |
| v11.0.1 | 2025-11-19 | Fixed directory layout; aligned schemas and telemetry references with GitHub infra docs.                                              |
| v11.0.0 | 2025-11-18 | Initial v11 CI/CD overview with FAIR+CARE-aware workflows.                                                                             |
| v10.4.1 | 2025-11-16 | Added AI workflow descriptions; improved metadata checks.                                                                              |
| v10.3.1 | 2025-11-13 | Introduced STAC/DCAT validators and telemetry bundling concepts.                                                                      |
| v10.2.2 | 2025-11-12 | Added sustainability metrics to CI/CD; started CVE gating.                                                                             |
| v10.0.0 | 2025-11-09 | Initial CI/CD workflow documentation for early KFM versions.                                                                           |

---

<div align="center">

🔄 **Kansas Frontier Matrix — CI/CD Workflows Master Architecture (v11.2.2)**  
Automation-First · FAIR+CARE-Governed · Provenance-Aware  

[⬅ GitHub Infrastructure Overview](../README.md) · [🏗 Repository Architecture](../ARCHITECTURE.md) · [🛡 Governance Charter](../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>
