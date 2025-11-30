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

**The governed CI/CD, reliability, FAIR+CARE, supply-chain, AI-safety, and automation backbone of the Kansas Frontier Matrix monorepo.**

[![KFM-MDP v11.2.2](https://img.shields.io/badge/Markdown-KFM--MDP_v11.2.2-informational)](../docs/standards/kfm_markdown_protocol_v11.2.2.md) ·
[![FAIR+CARE](https://img.shields.io/badge/Data-FAIR%2BCARE-gold)](../docs/standards/faircare/FAIRCARE-GUIDE.md) ·
[![License: MIT](https://img.shields.io/badge/License-MIT-green)](../LICENSE) ·
[![Status: Active](https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen)](#-version-history)

</div>

---

## 📘 Overview

The `.github/` directory is the **GitHub Infrastructure Plane** for KFM v11.2.2:

- Enforces **documentation-first** development (MCP-DL v6.3 + KFM-MDP v11.2.2).  
- Validates **schemas & ontologies** (STAC 1.x, DCAT 3.0, JSON-LD, CIDOC-CRM, GeoSPARQL, OWL-Time, PROV-O).  
- Applies **FAIR+CARE & sovereignty policies**, including H3-based masking for sensitive sites.  
- Governs **CI/CD**, **security & supply-chain**, and **AI behavior** (Story Nodes, Focus Mode).  
- Generates **OpenLineage v2.5** events for CI/CD + AI pipelines.  
- Emits **telemetry** for governance dashboards, SLO/SLA monitoring, and Focus Mode system health.

Nothing enters production branches or release artifacts without passing the checks defined here.

---

## 🗂️ Directory Layout

~~~text
.github/                                           # ⚙️ GitHub governance & automation subsystem
│
├── 📄 README.md                                   # GitHub infrastructure overview (this file)
├── 🏗️ ARCHITECTURE.md                             # CI/CD & governance architecture deep dive
│
├── 🤖 workflows/                                  # GitHub Actions workflows
│   ├── 🧪 ci.yml                                  # Core CI: lint, tests, type-checks, basic schemas
│   ├── 📚 docs_validate.yml                       # KFM-MDP v11.2.2 markdown + front-matter validation
│   ├── 🛰️ stac_validate.yml                       # STAC Item/Collection validation (data/stac/**)
│   ├── 🗂️ dcat_validate.yml                       # DCAT dataset/distribution validation
│   ├── 🧬 jsonld_validate.yml                     # JSON-LD + ontology checks (CIDOC/OWL-Time/GeoSPARQL/PROV-O)
│   ├── ⚖️ faircare_validate.yml                   # FAIR+CARE, ethics, and sovereignty enforcement
│   ├── 🧊 h3_generalization.yml                   # Dynamic H3 generalization for sensitive coordinates
│   ├── 🔐 security_audit.yml                      # Dependency, CVE, and secret scanning
│   ├── 📦 sbom_verify.yml                         # SBOM + manifest + SLSA attestation verification
│   ├── 🔁 data_pipeline.yml                       # ETL pipeline lineage tests & data contract checks
│   ├── 🤖 ai_behavior_check.yml                   # AI behavior, drift, bias, prohibited-output checks
│   ├── 🎯 focusmode_mlops.yml                     # Focus Mode v3 narrative-safety + fusion governance
│   ├── 📊 telemetry_export.yml                    # CI/AI telemetry → releases/<version>/focus-telemetry.json
│   ├── 🚀 release.yml                             # Release packaging, signing, and artifact publishing
│   ├── 🏷️ labeler.yml                             # Automatic PR labeling by domain/component
│   └── 🌐 site.yml                                # Docs and web build/deploy
│
├── 🧱 actions/                                    # Reusable composite actions (governed building blocks)
│   ├── 📐 markdown-lint/                          # Enforce KFM-MDP v11.2.2 markdown rules
│   ├── 🧾 schema-validate/                        # JSON/YAML schema validation
│   ├── 🛰️ stac-validate/                          # STAC validation wrapper
│   ├── 🗂️ dcat-validate/                          # DCAT validation wrapper
│   ├── 🧪 pytest-runner/                          # Standardized Python test runner harness
│   └── 🔍 security-scan/                          # Hardened dependency & secret scanning
│
├── 📂 ISSUE_TEMPLATE/                             # Governance-aware issue templates
│   ├── 🐛 bug_report.md                           # Bugs (code, data, pipelines, AI, UI)
│   ├── 💡 feature_request.md                      # Feature/enhancement proposals
│   ├── 🗺️ data_issue.md                           # Data, STAC/DCAT, CARE/sensitivity issues
│   └── ⚖️ governance_issue.md                     # Governance, ethics, sovereignty questions
│
├── ⚙️ ISSUE_TEMPLATE/config.yml                   # Issue routing, labels, and required fields
├── 📜 PULL_REQUEST_TEMPLATE.md                    # PR template (provenance, FAIR+CARE, SBOM, telemetry)
├── 👥 CODEOWNERS                                  # Ownership boundaries & mandatory reviewers
├── 🧩 dependabot.yml                              # Supply-chain & dependency automation
├── 💸 FUNDING.yml                                 # Sponsorship configuration
├── 📏 CODE_OF_CONDUCT.md                          # Community behavior standards
└── 🛡 SECURITY.md                                 # Security policy & vulnerability disclosure
~~~

The emoji-enhanced layout is **canonical** for v11.2.2 and must be kept in sync with actual repo contents.

---

## 🧱 Architecture

The `.github/` infrastructure implements a **multi-stage governed pipeline**:

1. **Linting & Style**  
   - Enforces code style (Python/TS/JS/CSS) and markdown structure.  
   - Ensures front-matter complies with KFM-MDP v11.2.2 (YAML presence, required fields, no broken fences).

2. **Schema & Ontology Validation**  
   - Validates JSON/YAML schemas, STAC Items/Collections, DCAT datasets, JSON-LD contexts, Story Node v3, telemetry schemas.  
   - Checks ontology alignment (CIDOC-CRM, GeoSPARQL, OWL-Time, PROV-O) for graph-related artifacts.

3. **Testing**  
   - Runs unit, integration, E2E tests for backend, pipelines, web, and graph components.  
   - Executes data contract tests (KFM-PDC v11.0) where appropriate.

4. **FAIR+CARE & Sovereignty Enforcement**  
   - Confirms FAIR (F1-A1-I1-R1) metadata properties.  
   - Ensures CARE labels and sovereignty rules are honored, using H3 generalization for sensitive sites.  

5. **Security & Supply-Chain Governance**  
   - Performs CVE scanning, secret detection, lockfile integrity checks, SBOM verification, and SLSA-style attestation checks.  

6. **Release Packaging & Telemetry**  
   - Produces SBOM, manifest, signatures, and telemetry for each governed release.  
   - Emits OpenLineage events for CI/CD steps and AI pipeline runs.

Each stage must pass before changes are merged into protected branches.

---

## 🧪 Validation & CI/CD

### Required Checks for Protected Branches

For `main` and release branches, merges require:

- `ci.yml` — core tests, linting, and base schema checks  
- `docs_validate.yml` — markdown + front-matter + diagram checks  
- `stac_validate.yml` — STAC validation for any changed STAC assets  
- `dcat_validate.yml` — DCAT validation for dataset-level records  
- `jsonld_validate.yml` — JSON-LD and ontology checks  
- `faircare_validate.yml` — FAIR+CARE + ethics checks for data and docs  
- `h3_generalization.yml` — masking for sensitive coordinates in public outputs  
- `security_audit.yml` — dependency/secret scanning and security posture  
- `sbom_verify.yml` — SBOM/manifest/SLSA attestation checks for release-impacting changes  
- `ai_behavior_check.yml` — AI narrative-safety and grounding checks (if AI/Focus touched)  
- `telemetry_export.yml` — telemetry generation and schema validation  

Workflows are path-aware, running only where relevant but always enforcing **deterministic rules**.

### Environments & Promotion

- **dev → staging** — automatic promotion when all required checks pass.  
- **staging → production** — manual approval, signing, and governance review required.  

All promotions emit **OpenLineage** events so infra-level lineage is queryable.

---

## 📦 Data & Metadata

`.github/` is responsible for emitting and validating key **metadata artifacts**:

- **SBOM** (`sbom_ref`) — SPDX inventory for each release.  
- **Manifest** (`manifest_ref`) — enumerates all release artifacts and checksums.  
- **Signature** (`signature_ref`) — cryptographic proof of artifact authenticity.  
- **SLSA Attestation** (`attestation_ref`) — supply-chain provenance for builds.  
- **Telemetry** (`telemetry_ref`) — CI/CD + AI + governance metrics (using `telemetry_schema`, `energy_schema`, `carbon_schema`).  

These artifacts:

- Support reproducibility and long-term governance.  
- Feed governance dashboards and compliance reviews.  
- Provide Focus Mode with system-health context (e.g., “this layer is from a fully governed release with complete metadata and passing security checks”).

---

## ⚖ FAIR+CARE & Governance

The GitHub infrastructure is tightly coupled with KFM’s governance framework:

- Uses `governance_ref`, `ethics_ref`, and `sovereignty_policy` as **normative anchors**.  
- Enforces **FAIR** by requiring metadata completeness, stable IDs, and open formats.  
- Enforces **CARE** via CARE labels, sovereignty flags, and H3 masking policies.  
- Blocks merges when:

  - Licensing is incompatible or unspecified.  
  - CARE/sovereignty constraints are violated.  
  - Sensitive heritage sites might be exposed beyond allowed resolution.  

Governance bodies (FAIR+CARE Council, Architecture Board, Security Council, AI Safety Board) rely on this infrastructure to implement and audit policy decisions.

---

## 🧭 Extending & Maintaining `.github/`

When adding or modifying CI/CD behavior:

1. **Reuse existing composite actions** in `actions/` where possible.  
2. **Emit telemetry** that conforms to `telemetry_schema`.  
3. **Update schemas** and tests when introducing new metadata.  
4. **Document changes** in this README and in `.github/ARCHITECTURE.md`.  
5. **Respect FAIR+CARE and sovereignty policies**; if in doubt, consult the appropriate council.  
6. **Update provenance_chain** and version history when significant changes are made.  
7. **Ensure CODEOWNERS coverage** for new workflows or sensitive paths.  

Changes that bypass these steps should be considered non-compliant with the v11.2.2 infrastructure contract.

---

## 🕰️ Version History

| Version | Date       | Summary                                                                                                                    |
|--------:|------------|----------------------------------------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-27 | Deep v11.2.2 update; expanded workflows list; aligned with security, FAIR+CARE, AI-safety, telemetry, and KFM-MDP v11.2.2. |
| v11.0.2 | 2025-11-23 | Tightened CI/CD descriptions; clarified governance and security integration; synced with root ARCHITECTURE.               |
| v11.0.1 | 2025-11-20 | Introduced ontology-aware validation, governance hooks, and AI-related workflow overview.                                  |
| v11.0.0 | 2025-11-19 | Initial v11 GitHub infrastructure overview aligned with the v11 monorepo architecture.                                    |
| v10.4.1 | 2025-11-16 | Pre-v11 enhancements: stronger governance, FAIR+CARE integration, and directory layout improvements.                      |
| v10.4.0 | 2025-11-15 | KFM-MDP v10.4 alignment: restructured CI/CD documentation and metadata linkage.                                           |
| v10.3.2 | 2025-11-14 | Added telemetry integration and improved STAC/DCAT validation references.                                                 |
| v10.0.0 | 2025-11-10 | Initial `.github/` infrastructure documentation.                                                                           |

---

<div align="center">

⚙️ **Kansas Frontier Matrix — GitHub Infrastructure (v11.2.2)**  
Automation-First · FAIR+CARE-Governed · Provenance-Aware  

[⬅️ Back to Repository Root](../README.md) · [🏗 CI/CD Architecture](ARCHITECTURE.md) · [🛡 Security Policy](SECURITY.md)

</div>
