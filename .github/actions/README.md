---
title: "🧱 KFM v11.2.2 — Composite Actions Library (GitHub Actions)"
path: ".github/actions/README.md"
version: "v11.2.2"
last_updated: "2025-11-28"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Infrastructure & Provenance Committee"
content_stability: "stable"
backward_compatibility: "Aligned with v10.x → v11.x CI/CD model"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../releases/v11.2.2/manifest.zip"
attestation_ref: "../../releases/v11.2.2/slsa-attestation.json"
signature_ref: "../../releases/v11.2.2/signature.sig"
telemetry_ref: "../../releases/v11.2.2/github-infra-telemetry.json"
telemetry_schema: "../../schemas/telemetry/actions-library-v11.json"
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
doc_kind: "Component Guide"
intent: "github-composite-actions"
role: "ci-cd-infrastructure"
category: "CI/CD · Automation · Governance · Reusability"

classification: "Public"
sensitivity: "General (non-sensitive; auto-mask rules apply)"
sensitivity_level: "None"
public_exposure_risk: "Low"
indigenous_rights_flag: false

care_label: "Collective Benefit · Authority to Control · Responsibility · Ethics"
fair_category: "F1-A1-I1-R1"

data_steward: "KFM Infrastructure & Provenance Committee"

provenance_chain:
  - ".github/actions/README.md@v11.0.0"
  - ".github/actions/README.md@v11.1.0"
  - ".github/actions/README.md@v11.2.0"
  - ".github/actions/README.md@v11.2.2"

prov_profile: "PROV-O Plan + KFM Governance Extensions"
openlineage_profile: "OpenLineage v2.5 (CI/CD events)"

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "TechArticle"
  owl_time: "TemporalEntity"
  prov_o: "prov:Plan"
  geosparql: "geo:FeatureCollection"

json_schema_ref: "../../schemas/json/actions-readme-v11.schema.json"
shape_schema_ref: "../../schemas/shacl/actions-readme-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:github-actions-readme:v11.2.2"
semantic_document_id: "kfm-doc-github-actions-library"
event_source_id: "ledger:.github/actions/README.md"

immutability_status: "mutable-plan"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

heading_registry:
  approved_h2:
    - "📘 Overview"
    - "🗂️ Directory Layout"
    - "🧱 Composite Action Specifications"
    - "🧭 Governance Requirements"
    - "🕰️ Version History"

test_profiles:
  - "markdown-lint"
  - "schema-lint"
  - "metadata-check"
  - "footer-check"
  - "accessibility-check"
  - "provenance-check"

ci_integration:
  workflow: ".github/workflows/kfm-ci.yml"
  environment: "dev · staging · production"

branding_registry:
  standard: "Scientific Insight × FAIR+CARE Ethics × Sustainable Intelligence"
  architecture: "Designed for Longevity · Governed for Integrity"
  analysis: "CI-Driven · Evidence-Led · FAIR+CARE Grounded"
  data-spec: "Open Pipelines × Responsible Automation"
  pipeline: "Deterministic CI/CD · Explainable Workflows · Open Provenance"
  telemetry: "Transparent Systems · Ethical Metrics · Sustainable Intelligence"
  graph: "Semantics × Provenance × Automation Intelligence"

layout_profiles:
  - "immediate-one-branch-with-descriptions-and-emojis"
badge_profiles:
  - "root-centered-badge-row"

requires_purpose_block: true
requires_version_history: true
requires_directory_layout_section: true
requires_governance_links_in_footer: true

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summary"
  - "a11y-adaptations"
ai_transform_prohibited:
  - "speculative-additions"
  - "unverified-architectural-claims"
  - "narrative-fabrication"
  - "governance-override"

deprecated_fields:
  - "old_actions_readme_v10.4"
---

<div align="center">

# 🧱 **KFM v11 — Composite Actions Library**  
`.github/actions/README.md`

**Purpose**  
Provide the **governed, reusable, deterministic composite GitHub Actions** used across all KFM v11.2.2 CI/CD workflows.  
These actions encode **shared CI/CD logic** once, with **FAIR+CARE**, **provenance**, and **security** guarantees.

[![KFM-MDP v11.2.2](https://img.shields.io/badge/Markdown-KFM--MDP_v11.2.2-blue)](../../docs/standards/kfm_markdown_protocol_v11.2.2.md)
· [![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Enforced-gold)](../../docs/standards/faircare/FAIRCARE-GUIDE.md)
· [![License: MIT](https://img.shields.io/badge/License-MIT-green)](../../LICENSE)

</div>

---

## 🗂️ Directory Layout

~~~text
.github/actions/
├── 📄 README.md                      # Composite Actions Library (this file)
├── 📂 markdown-lint/                 # Markdown + YAML front-matter validation (KFM-MDP v11.2.2)
│   └── 📄 action.yml
├── 📂 schema-validate/               # JSON/YAML schema validation (AJV + KFM schemas)
│   └── 📄 action.yml
├── 📂 stac-validate/                 # STAC Item/Collection/Catalog validator
│   └── 📄 action.yml
├── 📂 dcat-validate/                 # DCAT 3.0 dataset & distribution validator
│   └── 📄 action.yml
├── 📂 pytest-runner/                 # Standardized pytest executor (coverage, xfail rules)
│   └── 📄 action.yml
└── 📂 security-scan/                 # Dependency & secret scanning, supply-chain checks
    └── 📄 action.yml
~~~

**Layout rules**  
- 📂 is used only for directories; 📄 is used only for files.  
- No emojis appear inside the ASCII connectors themselves.  
- Every directory above MUST maintain this structure (single `action.yml` per composite).

---

## 📘 Overview

This directory contains the **governed composite GitHub Actions** that form the backbone of KFM v11 CI/CD.

Composite actions here are:

- 🧩 **Reusable** – centralize repeated workflow logic.  
- 🛡 **Governed** – reviewed and enforced by Infrastructure & Provenance Committee.  
- 🧬 **Schema-validated** – aligned with KFM-PDC v11 and KFM-OP v11.  
- 🛰 **Observable** – emitting telemetry and OpenLineage events.  
- 🔒 **Secure** – pinned, hardened, and subject to security scanning.

All new workflows MUST use these composites instead of re-implementing low-level logic.

---

## 🧱 Composite Action Specifications

Each composite action MUST:

- Declare **inputs** with explicit types and defaults.  
- Declare **outputs** with documented meaning.  
- Use **pinned actions** (`@<commit_sha>` not tags).  
- Emit **OpenLineage** events for key steps.  
- Emit **telemetry** conforming to `actions-library-v11.json`.  
- Avoid network calls or side-effects beyond those explicitly documented.  
- Fail fast on errors and surface clear diagnostics.

### 📐 `markdown-lint/`

- Validates:
  - YAML front-matter structure.  
  - KFM-MDP v11.2.2 heading usage.  
  - Footer presence & integrity.  
  - Fence and box safety (no stray backticks).  

- Used by:
  - `docs_validate.yml`  
  - `ci.yml`  

### 🧾 `schema-validate/`

- Validates:
  - JSON & YAML files against their schemas.  
  - Telemetry schemas.  
  - Story Node & Focus Mode schemas.  
  - STAC/DCAT-related JSON.

- Used by:
  - `ci.yml`  
  - Data and metadata pipelines.

### 🛰️ `stac-validate/`

- Validates:
  - STAC Items, Collections, Catalogs.  
  - Asset completeness and roles.  
  - Spatial and temporal extents.  
  - Provenance metadata presence.

- Blocks merges when STAC is invalid.

### 🗂️ `dcat-validate/`

- Validates:
  - DCAT datasets & distributions.  
  - License fields.  
  - DCAT/STAC alignment.

- Ensures FAIR metadata is present for all catalog entries.

### 🧪 `pytest-runner/`

- Runs:
  - `pytest` with standardized options (coverage, xfail policy).  
  - In a controlled environment with deterministic dependencies.  

- Emits:
  - Coverage metrics.  
  - Basic test telemetry for CI dashboards.

### 🔍 `security-scan/`

- Performs:
  - Secret scanning.  
  - Dependency vulnerability scanning.  
  - Lockfile verification.  
  - Supply-chain checks aligned with SLSA.

- Used by:
  - `security_audit.yml`  
  - Nightly or scheduled workflows.

---

## 🧭 Governance Requirements

All composite actions MUST:

1. Be referenced by **pinned SHAs** only (no moving tags).  
2. Include provenance metadata (`prov:Activity` assignments via OpenLineage).  
3. Emit telemetry conforming to `telemetry_schema`.  
4. Avoid implicit network access or credential usage.  
5. Be reviewed by:
   - Infrastructure & Provenance Committee.  
   - FAIR+CARE Council when narratives or data exports are involved.  
   - Security Response Group for security-related composites.  

Any change to an action MUST:

- Update its `action.yml` metadata.  
- Update any referenced schema documents.  
- Pass CI checks (lint, schema, provenance, security).  

---

## 🕰️ Version History

| Version | Date       | Summary                                                                                                                |
|--------:|------------|------------------------------------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-28 | Aligned metadata with KFM-MDP v11.2.2; added heading registry, test profiles, and clarified governance requirements.  |
| v11.2.0 | 2025-11-20 | Introduced telemetry & OpenLineage emission for composite actions.                                                     |
| v11.1.0 | 2025-11-10 | Documentation and schema enhancements for actions library.                                                             |
| v11.0.0 | 2025-11-01 | Initial Composite Actions Library introduction for KFM v11 CI/CD.                                                      |

---

<div align="center">

🧱 **KFM v11 — Composite Actions Library (GitHub Actions)**  
Reusable CI Building Blocks · Deterministic Pipelines · FAIR+CARE-Aligned Automation  

[📘 Docs Root](../../README.md) · [📂 Standards Index](../../docs/standards/README.md) · [⚖ Governance](../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>
