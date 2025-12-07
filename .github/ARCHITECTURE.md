---
title: "⚙️ Kansas Frontier Matrix — GitHub Infrastructure Architecture (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: ".github/ARCHITECTURE.md"
version: "v11.2.2"
last_updated: "2025-11-28"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · FAIR+CARE Council & Architecture Board"
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
markdown_protocol_version: "KFM-MDP v11.2.4"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

status: "Active / Enforced"
doc_kind: "Architecture"
intent: "github-infrastructure-architecture"
role: "infrastructure-hub"
category: "CI/CD · Governance · Automation · Telemetry"

classification: "Public Document"
sensitivity: "General (non-sensitive)"
sensitivity_level: "None"
public_exposure_risk: "Low"
risk_category: "Low"
indigenous_rights_flag: false
redaction_required: false
data_steward: "KFM FAIR+CARE Council"

fair_category: "F1-A1-I1-R1"
care_label: "Collective Benefit · Authority to Control · Responsibility · Ethics"

provenance_chain:
  - ".github/ARCHITECTURE.md@v10.0.0"
  - ".github/ARCHITECTURE.md@v11.0.0"
  - ".github/ARCHITECTURE.md@v11.0.1"
  - ".github/ARCHITECTURE.md@v11.2.2"

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "TechArticle"
  owl_time: "TemporalEntity"
  prov_o: "prov:Plan"
  geosparql: "geo:FeatureCollection"

json_schema_ref: "../schemas/json/github-architecture-v11.schema.json"
shape_schema_ref: "../schemas/shacl/github-architecture-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:github-architecture:v11.2.2"
semantic_document_id: "kfm-doc-github-architecture"
event_source_id: "ledger:.github/ARCHITECTURE.md"
immutability_status: "mutable-plan"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summaries"
  - "semantic-highlighting"
  - "a11y-adaptations"
ai_transform_prohibited:
  - "speculative additions"
  - "unverified architectural claims"
  - "governance-override"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
jurisdiction: "United States / Kansas"
lifecycle_stage: "stable"
ttl_policy: "Annual review"
sunset_policy: "Superseded upon next infrastructure-architecture update"
---

<div align="center">

# ⚙️ **Kansas Frontier Matrix — GitHub Infrastructure Architecture**  
`.github/ARCHITECTURE.md`

**Purpose**  
Define the **architectural role, structure, and control flows** of the `.github/` subsystem for KFM v11 — including CI/CD, security, FAIR+CARE enforcement, sovereignty checks, AI governance, and telemetry — in a way that is **reproducible, auditable, and machine-readable**.

[![GitHub Infra](https://img.shields.io/badge/Subsystem-GitHub_Infrastructure-informational)](README.md) ·
[![KFM-MDP v11.2.4](https://img.shields.io/badge/Markdown-KFM--MDP_v11.2.4-blue)](../docs/standards/kfm_markdown_protocol_v11.2.4.md) ·
[![FAIR+CARE](https://img.shields.io/badge/Data-FAIR%2BCARE-gold)](../docs/standards/faircare/FAIRCARE-GUIDE.md) ·
[![Status: Active](https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen)](#-version-history)

</div>

---

## 📘 Overview

The `.github/` directory is the **governance and automation fabric** for the Kansas Frontier Matrix monorepo:

- Drives **CI/CD pipelines** for code, data, docs, and AI.  
- Enforces **KFM-MDP v11.2.4** Markdown rules and front‑matter schemas.  [oai_citation:0‡Kansas Frontier Matrix — Markdown Authoring Protocol (KFM-MDP) v11.2.4.pdf](file-service://file-57iDMaU6FoN7pZ8e5HbsPp)  
- Validates **STAC, DCAT, PROV-O, JSON-LD, and telemetry** artifacts.  [oai_citation:1‡GeoSPARQL: Geospatial SPARQL for the Semantic Web.pdf](file-service://file-Gcko4NCD4BXhFG42Sh7Z1o)  
- Applies **FAIR+CARE and sovereignty constraints** before any public exposure.  [oai_citation:2‡Kansas Frontier Matrix — Markdown Authoring Protocol (KFM-MDP) v11.2.4.pdf](file-service://file-57iDMaU6FoN7pZ8e5HbsPp)  
- Governs **AI behavior** (Story Nodes & Focus Mode v3) via test suites and policies.  
- Emits **OpenLineage + security + sustainability telemetry** used in audits and narratives.  

This document explains **how the pieces fit together** — workflows, composite actions, policies, and telemetry — and how they relate to the rest of the KFM architecture.

---

## 🗂️ Directory Layout

Canonical layout for `.github/` (two levels, GitHub-safe):

~~~text
.github/                                           # ⚙️ GitHub governance & automation subsystem
│
├── 📄 README.md                                   # High-level GitHub infrastructure overview
├── 🏗️ ARCHITECTURE.md                             # This architecture document
│
├── 🤖 workflows/                                  # GitHub Actions workflows (CI/CD + governance)
│   ├── 🧪 ci.yml                                  # Core CI: lint, tests, type-checks, schema checks
│   ├── 📚 docs_validate.yml                       # KFM-MDP v11.2.4 markdown + front-matter validation
│   ├── 🛰️ stac_validate.yml                       # STAC 1.x validation (collections/items)
│   ├── 🗂️ dcat_validate.yml                       # DCAT 3.0 validation (datasets/distributions)
│   ├── 🧬 jsonld_validate.yml                     # JSON-LD + ontology consistency (CIDOC/GeoSPARQL/OWL-Time/PROV-O)
│   ├── ⚖️ faircare_validate.yml                   # FAIR+CARE & sovereignty checks (sensitivity flags, masking)
│   ├── 🧊 h3_generalization.yml                   # H3 spatial generalization for sensitive sites
│   ├── 🔐 security_audit.yml                      # Dependency, CVE, secret, and supply-chain scans
│   ├── 📦 sbom_verify.yml                         # SBOM + manifest + SLSA attestations
│   ├── 🔁 data_pipeline.yml                       # Data/ETL contract & lineage enforcement
│   ├── 🌡️ climate_mlops.yml                       # Climate-related model governance
│   ├── 💧 hydrology_mlops.yml                     # Hydrology & water models governance
│   ├── 🌪️ hazards_mlops.yml                       # Severe weather / hazards models governance
│   ├── 🔡 embeddings_mlops.yml                    # Embedding model governance (semantic/spatial)
│   ├── 🎯 focusmode_mlops.yml                     # Focus Mode v3 narrative-safety checks
│   ├── 🤖 ai_behavior_check.yml                   # LLM behavior, drift, and forbidden-output checks
│   ├── 📊 telemetry_export.yml                    # Telemetry export → github-infra-telemetry.json
│   ├── 🚀 release.yml                             # Signed releases, tagging, packaging, publishing
│   ├── 🏷️ labeler.yml                             # Auto-labeling PRs based on path & semantics
│   └── 🌐 site.yml                                # Docs + web build/deploy pipelines
│
├── 🧱 actions/                                    # Reusable composite actions
│   ├── 📐 markdown-lint/                          # KFM-MDP v11.2.4 markdown & front-matter checks
│   ├── 🧾 schema-validate/                        # JSON, YAML, and JSON-LD schema validation
│   ├── 🛰️ stac-validate/                          # STAC validation wrapper
│   ├── 🗂️ dcat-validate/                          # DCAT validation wrapper
│   ├── 🧪 pytest-runner/                          # Python test runner harness
│   └── 🔍 security-scan/                          # Dependency + secret scanning wrapper
│
├── 📂 ISSUE_TEMPLATE/                             # Issue templates (governance-aware)
│   ├── 🐛 bug_report.md                           # Bug reports (pipelines, datasets, UI, AI)
│   ├── 💡 feature_request.md                      # Feature/enhancement requests
│   ├── 🗺️ data_issue.md                           # Data/STAC/DCAT/FAIR+CARE issues
│   └── ⚖️ governance_issue.md                     # Governance, ethics, sovereignty issues
│
├── ⚙️ ISSUE_TEMPLATE/config.yml                   # Template routing, required fields, auto-label configuration
├── 📜 PULL_REQUEST_TEMPLATE.md                    # PR metadata & governance checklist
├── 👥 CODEOWNERS                                  # Ownership boundaries & review requirements
├── 🧩 dependabot.yml                              # Automated dependency and security updates
├── 💸 FUNDING.yml                                 # Funding and sponsor links
├── 📏 CODE_OF_CONDUCT.md                          # Community norms and conduct guidelines
└── 🛡 SECURITY.md                                 # Security policy & vulnerability disclosure
~~~

Rules:

- Any new workflow or action MUST be reflected here and in `.github/README.md`.  
- Structural changes MUST be accompanied by updated schemas and CI config.  

---

## 🧭 Context

`.github/` is one of the **core subsystems** in the KFM v11 architecture:

- At the **repository level**, it orchestrates:
  - Tests and validation for `src/`, `web/`, `data/`, `docs/`, `mcp/`, and `tools/`.
  - Root contracts in `ARCHITECTURE.md` and `README.md`.  

- At the **governance level**, it encodes:
  - Enforcement of **KFM-MDP v11.2.4** for all Markdown docs.  [oai_citation:3‡Kansas Frontier Matrix — Markdown Authoring Protocol (KFM-MDP) v11.2.4.pdf](file-service://file-57iDMaU6FoN7pZ8e5HbsPp)  
  - FAIR+CARE & sovereignty requirements for high-risk datasets and narratives.  
  - Approval workflows (CODEOWNERS, required reviews, and protected branches).  

- At the **observability level**, it:
  - Emits telemetry (energy, carbon, security, governance, and lineage) under the telemetry schemas.  [oai_citation:4‡GeoSPARQL: Geospatial SPARQL for the Semantic Web.pdf](file-service://file-Gcko4NCD4BXhFG42Sh7Z1o)  
  - Integrates with OpenLineage to trace CI/CD, data pipelines, and AI flows.  

This architecture document should be read alongside:

- `.github/README.md` — conceptual overview & onboarding.  
- `ARCHITECTURE.md` — global system & repo architecture.  
- `docs/security/` — detailed security, supply-chain, and incident response frameworks.  

---

## 🗺️ Diagrams

### 1. Pull Request → Governance → Release Flow

~~~mermaid
flowchart LR
    dev[Developer<br/>opens PR] --> checks[CI Workflows<br/>ci.yml + docs/stac/dcat/ai/security]
    checks -->|pass| review[Required Reviews<br/>CODEOWNERS + Governance]
    checks -->|fail| fix[Author Fixes<br/>push updates]

    review -->|approved| merge[Protected Branch<br/>main/release/*]
    review -->|changes requested| fix

    merge --> release[Release Workflow<br/>release.yml]
    release --> artifacts[Signed Artifacts<br/>SBOM + manifest + attestations]
    artifacts --> telemetry[Telemetry Export<br/>github-infra-telemetry.json]
~~~

This diagram shows how every change must pass **tests + governance** before landing on protected branches and producing signed release artifacts and telemetry.

### 2. Workflow & Composite Action Relationship

~~~mermaid
flowchart TB
    subgraph Workflows
        ci[ci.yml]
        docs[docs_validate.yml]
        stac[stac_validate.yml]
        dcat[dcat_validate.yml]
        fair[faircare_validate.yml]
        sec[security_audit.yml]
        sbom[sbom_verify.yml]
    end

    subgraph Composite_Actions
        mdLint[actions/markdown-lint]
        schema[actions/schema-validate]
        stacAct[actions/stac-validate]
        dcatAct[actions/dcat-validate]
        secScan[actions/security-scan]
    end

    ci --> mdLint
    ci --> schema
    docs --> mdLint
    stac --> stacAct
    dcat --> dcatAct
    sec --> secScan
    sbom --> schema
~~~

Workflows stay **thin** and declarative; composite actions centralize complex logic for reuse and versioning.

---

## 🧠 Story Node & Focus Mode Integration

While `.github/` doesn’t serve user-facing content, its architecture is critical for **narrative integrity**:

- Story Nodes and Focus Mode v3 depend on:
  - **Schema-valid docs** (KFM-MDP-compliant) that can be parsed into Story Nodes.  [oai_citation:5‡Kansas Frontier Matrix — Markdown Authoring Protocol (KFM-MDP) v11.2.4.pdf](file-service://file-57iDMaU6FoN7pZ8e5HbsPp)  
  - **Reliable lineage** (OpenLineage/PROV-O) from CI/CD for telling “how this model/layer was built.”  [oai_citation:6‡GeoSPARQL: Geospatial SPARQL for the Semantic Web.pdf](file-service://file-Gcko4NCD4BXhFG42Sh7Z1o)  

- CI workflows can:
  - Block merges if Story Node schemas are invalid or if AI behavior tests fail.  
  - Emit telemetry about narrative safety & grounding tests.  

- Architecture constraint:
  - Focus Mode MUST NOT rely on ungoverned content paths; only assets that pass `.github/` workflows are eligible for production narratives.  

---

## 🧪 Validation & CI/CD

### 1. Workflow Classes

1. **Core Quality (ci.yml)**  
   - Linting, formatting, static analysis.  
   - Unit/integration tests for Python, Node, and other languages.  
   - Core schema validation for configs and contracts.  

2. **Documentation & Metadata**  
   - `docs_validate.yml`: KFM-MDP v11.2.4 + YAML front-matter schema checks.  [oai_citation:7‡Kansas Frontier Matrix — Markdown Authoring Protocol (KFM-MDP) v11.2.4.pdf](file-service://file-57iDMaU6FoN7pZ8e5HbsPp)  
   - `stac_validate.yml`: STAC item/collection validation.  [oai_citation:8‡GeoSPARQL: Geospatial SPARQL for the Semantic Web.pdf](file-service://file-Gcko4NCD4BXhFG42Sh7Z1o)  
   - `dcat_validate.yml`: DCAT dataset/distribution checks.  

3. **Ontology & Graph Semantics**  
   - `jsonld_validate.yml`: validates JSON-LD contexts, graph exports, and ontology alignment (CIDOC, GeoSPARQL, OWL-Time, PROV-O).  [oai_citation:9‡GeoSPARQL: Geospatial SPARQL for the Semantic Web.pdf](file-service://file-Gcko4NCD4BXhFG42Sh7Z1o)  

4. **FAIR+CARE & Sovereignty**  
   - `faircare_validate.yml`: ensures required FAIR+CARE metadata and masks; checks classification and sensitivity tags.  [oai_citation:10‡Kansas Frontier Matrix — Markdown Authoring Protocol (KFM-MDP) v11.2.4.pdf](file-service://file-57iDMaU6FoN7pZ8e5HbsPp)  
   - `h3_generalization.yml`: verifies H3 aggregation for sensitive sites and domains.  

5. **Security & Supply Chain**  
   - `security_audit.yml`: dependency scanning, secret detection, policy enforcement.  
   - `sbom_verify.yml`: rebuilds/verifies SBOMs and manifests; checks signatures and attestations.  

6. **Data & AI Pipelines**  
   - `data_pipeline.yml`: ETL/data contract + lineage enforcement.  
   - `*_mlops.yml` workflows: domain-specific model governance gates.  
   - `ai_behavior_check.yml`: LLM behavior and narrative safety tests.  
   - `focusmode_mlops.yml`: ensures Focus Mode uses only approved, grounded patterns.  

7. **Releases & Telemetry**  
   - `release.yml`: orchestrates version bumping, tagging, packaging, signing, artifact upload.  
   - `telemetry_export.yml`: writes `github-infra-telemetry.json` with CI/CD + governance metrics.  

### 2. Branch Protection & Required Checks

Protected branches (e.g., `main`, `release/*`) require:

- Success from a defined set of workflows (at minimum `ci.yml`, `docs_validate.yml`, security/metadata checks).  
- Minimum review counts and CODEOWNERS approval for sensitive paths.  
- Prohibition of force-pushes and direct commits.  

These rules are treated as **part of the architecture**: changing them demands updates to this document and the governance charter.

---

## 📦 Data & Metadata

The `.github/` architecture produces and consumes metadata, including:

- **SBOMs** (`sbom_ref`) and **manifests** (`manifest_ref`).  
- **SLSA attestations** (`attestation_ref`) for builds and releases.  
- **Telemetry** (`telemetry_ref`) under `telemetry_schema`, `energy_schema`, and `carbon_schema`.  

All of these:

- Are versioned per release and linked via provenance records in `docs/security/` and `docs/data/`.  
- Feed into security, governance, and sustainability dashboards.  
- Can be referenced by Story Nodes to describe system trust and lineage context.  

---

## 🌐 STAC, DCAT & PROV Alignment

Although `.github/` doesn’t hold STAC/DCAT data itself, its workflows are responsible for enforcing:

- Compliance of STAC collections/items in `data/stac/`.  [oai_citation:11‡GeoSPARQL: Geospatial SPARQL for the Semantic Web.pdf](file-service://file-Gcko4NCD4BXhFG42Sh7Z1o)  
- DCAT dataset/distribution records in `docs/data/` and `data/releases/`.  
- PROV-O lineage exports and OpenLineage event schemas used to describe CI/CD and pipeline runs.  [oai_citation:12‡GeoSPARQL: Geospatial SPARQL for the Semantic Web.pdf](file-service://file-Gcko4NCD4BXhFG42Sh7Z1o)  

Architecturally, `.github/` is the **gatekeeper** ensuring catalog and provenance layers remain internally consistent and standards-compliant.

---

## ⚖ FAIR+CARE & Governance

The design of `.github/` must always satisfy:

- **FAIR**  
  - **Findable** — workflows, actions, and policies clearly named and documented.  
  - **Accessible** — logs and telemetry accessible to maintainers and relevant councils.  
  - **Interoperable** — schemas and telemetry compatible with external tooling.  
  - **Reusable** — documented patterns and composite actions for other projects.  

- **CARE**  
  - **Collective Benefit** — automation serves communities and stewards, not only developers.  
  - **Authority to Control** — sovereignty and ethics policies are encoded in CI checks.  
  - **Responsibility** — security, privacy, and narrative safety are first-class responsibilities.  
  - **Ethics** — high-risk flows (heritage, identity, environment) require extra scrutiny.  

Governance hooks:

- Changes to `.github/` that affect policy, security, or FAIR+CARE constraints MUST be reviewed by relevant councils (Security, FAIR+CARE, Architecture Board) before merging.  
- This architecture document and `.github/README.md` MUST be updated when governance scope changes.  

---

## 🕰️ Version History

| Version | Date       | Summary                                                                                                   |
|--------:|------------|-----------------------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-28 | Aligned GitHub architecture with KFM-MDP v11.2.4, expanded workflow map, clarified FAIR+CARE and telemetry integration. |
| v11.0.1 | 2025-11-23 | Linked CI workflows with PROV-O and OpenLineage; introduced AI behavior and Focus Mode governance flows.  |
| v11.0.0 | 2025-11-19 | First v11 GitHub architecture doc; defined workflow classes and composite-action patterns.                |
| v10.0.0 | Legacy     | Pre-v11 baseline, prior to FAIR+CARE and sovereignty integration.                                        |

---

<div align="center">

⚙️ **Kansas Frontier Matrix — GitHub Infrastructure Architecture (v11.2.2)**  
Automation-First · FAIR+CARE-Governed · Provenance-Aware  

[⬅️ Back to GitHub Infra Overview](README.md) · [🏗 Repository Architecture](../ARCHITECTURE.md) · [🛡 Security Policy](SECURITY.md)

</div>
