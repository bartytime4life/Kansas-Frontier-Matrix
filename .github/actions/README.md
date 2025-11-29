---
title: "🧱 KFM v11.2.2 — Composite Actions Library (GitHub Actions)"
path: ".github/actions/README.md"
version: "v11.2.2"
last_updated: "2025-11-28"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Infrastructure & Provenance Committee"
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
ontology_protocol_version: "KFM-OP v11.0"
pipeline_contract_version: "KFM-PDC v11.0"

status: "Active / Enforced"
doc_kind: "Component Guide"
intent: "github-composite-actions"
role: "ci-cd-infrastructure"
category: "CI/CD · Automation · Governance · Reusability"

classification: "Public Document"
sensitivity: "General"
sensitivity_level: "None"
indigenous_rights_flag: false
public_exposure_risk: "Low"

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

ttl_policy: "Annual review"
sunset_policy: "Superseded upon next major CI/CD revision"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summaries"
  - "a11y-adaptations"
ai_transform_prohibited:
  - "speculative-additions"
  - "unverified-architectural-claims"
---

<div align="center">

# 🧱 **KFM v11 — Composite Actions Library**  
`.github/actions/README.md`

**Reusable, deterministic, governed building blocks for all KFM CI/CD workflows.**

[![KFM-MDP v11.2.2](https://img.shields.io/badge/Markdown-KFM--MDP_v11.2.2-blue)](../../docs/standards/kfm_markdown_protocol_v11.2.2.md)
· [![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Enforced-gold)](../../docs/standards/faircare/FAIRCARE-GUIDE.md)
· [![License: MIT](https://img.shields.io/badge/License-MIT-green)](../../LICENSE)

</div>

---

## 📘 Overview

This directory contains **governed composite GitHub Actions** used across the entire KFM v11.2.2 CI/CD system.  

Composite actions are:

- 🧩 **Reusable** – unify repeated logic  
- 🛡 **Governed** – aligned with FAIR+CARE, sovereignty, AI-governance, and security requirements  
- 🧬 **Schema-validated** – follow KFM-PDC and KFM-OP v11 ontology rules  
- 🛰 **Observable** – generate OpenLineage + telemetry for all executions  
- 🔒 **Secure** – hardened to defend against supply-chain and workflow injection attacks  

All new workflows **must use these composites** instead of re-implementing logic.

---

## 🗂 Directory Layout

~~~text
.github/actions/
│
├── 📐 markdown-lint/                 # Markdown + YAML front-matter validation (KFM-MDP v11.2.2)
│    └── action.yml
│
├── 🧾 schema-validate/               # JSON/YAML schema validation (AJV + KFM schemas)
│    └── action.yml
│
├── 🛰️ stac-validate/                 # STAC Item/Collection/Catalog validator
│    └── action.yml
│
├── 🗂️ dcat-validate/                 # DCAT 3.0 dataset & distribution validator
│    └── action.yml
│
├── 🧪 pytest-runner/                 # Standardized pytest executor (coverage, xfail rules)
│    └── action.yml
│
└── 🔍 security-scan/                 # Hardened dependency & secret scanning composite
     └── action.yml
~~~

---

## 🧱 Composite Action Specifications

Each composite action adheres to:

- KFM-PDC v11 pipeline contracts  
- KFM-OP v11.0 ontology mappings  
- KFM-MDP v11.2.2 structural expectations  
- FAIR+CARE governance rules  
- Sovereignty & H3-masking requirements  
- Energy/carbon telemetry policies  
- Security & supply-chain constraints  

### All composites MUST provide:

- `inputs` with explicit schema  
- Formally typed outputs  
- Provenance (`prov:Activity`) emitted through OpenLineage  
- Telemetry (`telemetry_ref`) appended to the release bundle  
- Deterministic execution with fail-fast behavior  
- No network side-effects unless explicitly allowed  
- Strict action-pinning (`@commit_sha`, never tags)  

---

## 📐 markdown-lint/

Purpose:  
Validate KFM-MDP v11.2.2 compliance for all Markdown files, ensuring:

- mandatory YAML front-matter  
- fenced-block integrity  
- heading patterns  
- footer compliance  
- no stray backticks  
- FAIR+CARE metadata presence  

Used by:  
`docs_validate.yml`, `ci.yml`

---

## 🧾 schema-validate/

Validates:

- JSON schemas (`schemas/json/**`)  
- YAML schemas  
- STAC extensions  
- Telemetry schemas  
- Story Node v3, Focus Mode v3 schemas  

Used by:  
`ci.yml`, `data_pipeline.yml`, `stac_validate.yml`, `dcat_validate.yml`

---

## 🛰️ stac-validate/

Validates all:

- STAC Items (`data/stac/items/**`)  
- STAC Collections (`data/stac/collections/**`)  
- STAC Catalog (`data/stac/catalog.json`)  

Requires:

- compliant `bbox`  
- temporal extents  
- asset roles  
- linking completeness  
- PROV-O lineage metadata  

---

## 🗂️ dcat-validate/

Ensures:

- DCAT dataset objects are valid  
- distributions registered  
- dataset → STAC alignment  
- licenses declared  
- provenance included  

Blocks merge for missing FAIR metadata.

---

## 🧪 pytest-runner/

Provides:

- pytest execution in guaranteed reproducible environment  
- coverage collection  
- missing-fixture detection  
- xfail policy enforcement  
- provenance logging  

Used by:  
`ci.yml`, MLOps workflows

---

## 🔍 security-scan/

Performs:

- secret scanning  
- dependency CVE scanning  
- lockfile integrity  
- SLSA-aligned supply-chain checks  
- policy-based security gating  

Used by:  
`security_audit.yml`

---

## 🧭 Governance Requirements

All composite actions:

1. MUST be referenced using pinned SHAs  
2. MUST declare provenance metadata  
3. MUST emit OpenLineage events  
4. MUST comply with FAIR+CARE & sovereignty policies  
5. MUST export telemetry  
6. MUST avoid ambiguous side effects  
7. MUST be reviewed by:
   - Infrastructure & Provenance Committee  
   - FAIR+CARE Council (for narrative-related actions)  
   - Security Response Group (for security-related actions)  

---

## 🕰 Version History

| Version | Date | Summary |
|--------:|------|---------|
| v11.2.2 | 2025-11-28 | Complete rebuild for v11.2.2; added full governance, telemetry, ontology mapping, and composite action contract alignment. |
| v11.2.0 | 2025-11-20 | Introduced telemetry & OpenLineage emission for composites. |
| v11.1.0 | 2025-11-10 | Documentation + schema enhancements. |
| v11.0.0 | 2025-11-01 | Initial Composite Actions Library introduction. |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅️ Back to Repository](../../README.md) · [📐 Architecture](../ARCHITECTURE.md) · [🛡 Security Policy](../SECURITY.md)

</div>