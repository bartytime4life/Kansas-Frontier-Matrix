---
title: "⚙️ Kansas Frontier Matrix — GitHub Infrastructure Overview (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: ".github/README.md"
version: "v11.2.3"
last_updated: "2025-12-08"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Autonomous · FAIR+CARE Council Oversight"
backward_compatibility: "Aligned with v10.x → v11.2.3 CI/CD and metadata model"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

signature_ref: "../releases/v11.2.3/signature.sig"
attestation_ref: "../releases/v11.2.3/slsa-attestation.json"
sbom_ref: "../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../releases/v11.2.3/manifest.zip"
telemetry_ref: "../releases/v11.2.3/github-infra-telemetry.json"
telemetry_schema: "../schemas/telemetry/github-readme-v11.json"
energy_schema: "../schemas/telemetry/energy-v2.json"
carbon_schema: "../schemas/telemetry/carbon-v2.json"

governance_ref: "../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.5"
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
  - ".github/README.md@v11.2.3"

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

doc_uuid: "urn:kfm:doc:github-readme-v11.2.3"
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
  - "summary"
  - "semantic-highlighting"
  - "a11y-adaptations"
ai_transform_prohibited:
  - "content-alteration"
  - "speculative-additions"
  - "unverified-architectural-claims"
  - "narrative-fabrication"
  - "governance-override"
---

<div align="center">

# ⚙️ **Kansas Frontier Matrix — GitHub Infrastructure Overview**  
`.github/README.md`

**Purpose**  
Describe the **governed CI/CD, security, FAIR+CARE, sovereignty, AI-safety, and telemetry** infrastructure that GitHub provides for the KFM v11.2.x monorepo.

[![KFM-MDP v11.2.5](https://img.shields.io/badge/Markdown-KFM--MDP_v11.2.5-informational)](../docs/standards/kfm_markdown_protocol_v11.2.5.md) ·
[![FAIR+CARE](https://img.shields.io/badge/Data-FAIR%2BCARE-gold)](../docs/standards/faircare/FAIRCARE-GUIDE.md) ·
[![License: MIT](https://img.shields.io/badge/License-MIT-green)](../LICENSE) ·
[![Status: Active](https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen)](#-version-history)

</div>

---

## 📘 Overview

The `.github/` directory is the **automation and governance control plane** for the Kansas Frontier Matrix (KFM):

- Enforces **CI/CD** rules for linting, tests, schemas, and releases  
- Guards **security & supply-chain** (SBOM, SLSA, signatures, dependency policy)  
- Applies **FAIR+CARE & sovereignty** constraints (H3 masking, ethics checks)  
- Governs **AI & Focus Mode** behavior (narrative safety, grounding, bias)  
- Emits **OpenTelemetry + OpenLineage** for provenance, sustainability, and Story Nodes  
- Serves as the **entry point** for community standards (CODE_OF_CONDUCT, SECURITY, templates)  

Nothing reaches protected branches or official releases unless `.github/` workflows and governance checks succeed.

---

## 🗂️ Directory Layout

```text
.github/                                           # ⚙️ GitHub governance & automation subsystem
│
├── 📄 README.md                                   # GitHub infrastructure overview (this file)
├── 🏗️ ARCHITECTURE.md                             # Deep-dive CI/CD + governance architecture
│
├── 🤖 workflows/                                  # GitHub Actions workflows (CI/CD + governance)
│   ├── 🧪 ci.yml                                  # Core CI: lint, type-check, tests, schema checks
│   ├── 📚 docs_validate.yml                       # KFM-MDP v11.2.5 markdown + YAML validation
│   ├── 🛰️ stac_validate.yml                       # STAC 1.x Item/Collection validation
│   ├── 🗂️ dcat_validate.yml                       # DCAT 3.0 dataset/distribution validation
│   ├── 🧬 jsonld_validate.yml                     # JSON-LD / ontology validation (CIDOC, OWL-Time, GeoSPARQL)
│   ├── ⚖️ faircare_validate.yml                   # FAIR+CARE, sovereignty, ethics enforcement
│   ├── 🧊 h3_generalization.yml                   # H3 masking for sensitive archaeological/tribal sites
│   ├── 🔐 security_audit.yml                      # CVEs, dependencies, secrets, supply-chain checks
│   ├── 📦 sbom_verify.yml                         # SBOM + manifest + SLSA attestation checks
│   ├── 🔁 data_pipeline.yml                       # ETL lineage tests & data contract enforcement
│   ├── 🌡️ climate_mlops.yml                       # Climate model MLOps governance
│   ├── 💧 hydrology_mlops.yml                     # Hydrology models & indices governance
│   ├── 🌪️ hazards_mlops.yml                       # Severe weather / hazards model governance
│   ├── 🔡 embeddings_mlops.yml                    # Embedding model governance (spatial/semantic)
│   ├── 🎯 focusmode_mlops.yml                     # Focus Mode v3 narrative-safety + fusion checks
│   ├── 🤖 ai_behavior_check.yml                   # LLM behavior, drift, bias, forbidden-output detection
│   ├── 📊 telemetry_export.yml                    # CI/AI telemetry → releases/github-infra-telemetry.json
│   ├── 🚀 release.yml                             # Signed release packaging + artifact publishing
│   ├── 🏷️ labeler.yml                             # Auto-labeling PRs by component/domain
│   └── 🌐 site.yml                                # docs + web build/deploy pipelines
│
├── 🧱 actions/                                    # Reusable composite actions
│   ├── 📐 markdown-lint/                          # Enforce KFM-MDP v11.2.5 markdown rules
│   ├── 🧾 schema-validate/                        # JSON/YAML schema validation
│   ├── 🛰️ stac-validate/                          # STAC validator wrapper
│   ├── 🗂️ dcat-validate/                          # DCAT validator wrapper
│   ├── 🧪 pytest-runner/                          # Standard Python test runner harness
│   └── 🔍 security-scan/                          # Hardened dependency & secret scanning
│
├── 📂 ISSUE_TEMPLATE/                             # Issue governance templates
│   ├── 🐛 bug_report.md                           # Bug reports (pipelines, AI, datasets, UI)
│   ├── 💡 feature_request.md                      # Feature/enhancement requests
│   ├── 🗺️ data_issue.md                           # Data/STAC/DCAT/CARE/sensitivity issues
│   └── ⚖️ governance_issue.md                     # Governance, sovereignty, ethics issues
│
├── ⚙️ ISSUE_TEMPLATE/config.yml                   # Routing, required fields, auto-label logic
├── 📜 PULL_REQUEST_TEMPLATE.md                    # Required PR metadata & governance checklist
├── 👥 CODEOWNERS                                  # Ownership boundaries for governed domains
├── 🧩 dependabot.yml                              # Supply-chain dependency automation rules
├── 💸 FUNDING.yml                                 # Sponsorship configuration
├── 📏 CODE_OF_CONDUCT.md                          # Community and collaboration norms
└── 🛡 SECURITY.md                                 # Security policy & vulnerability disclosure
```

This layout is the **source of truth** for `.github/`. Any structural changes MUST be reflected here and in `ARCHITECTURE.md`.

---

## 🧭 Context

`.github/` sits at the front door of the KFM pipeline:

> Deterministic ETL → STAC/DCAT/PROV catalogs → Neo4j knowledge graph → API layer → React/MapLibre/Cesium frontend → Story Nodes → Focus Mode.

In practice:

- **Pipelines (`src/pipelines/…`)**  
  - Workflows gate ETL configs, schema migrations, and data contracts before any change touches `data/raw`, `data/work`, or `data/processed`.  

- **Catalogs (`data/stac/`, `docs/data/…`)**  
  - STAC/DCAT validation steps guarantee catalog JSON and RDF stay compatible with OGC STAC and DCAT profiles.  

- **Knowledge graph (`src/graph/…`)**  
  - JSON-LD and ontology checks ensure Neo4j content stays consistent with PROV-O, GeoSPARQL, CIDOC-CRM, and KFM-OP v11.  

- **APIs (`src/api/…`) & web (`src/web/…`)**  
  - `site.yml` and API checks prevent API/contract drift, ensuring React/MapLibre/Cesium UIs get strongly-typed, versioned responses.  

- **Story Nodes & Focus Mode**  
  - Telemetry and provenance from Actions runs are ingested as entities/activities/agents, so Story Nodes can narrate *how* a dataset/model entered KFM, not just *what* it contains.  

---

## 🧱 Architecture

The `.github/` architecture orchestrates governed layers:

1. **Core CI**  
   - Every PR and commit passes linting, tests, and schema checks before merging.  
   - Markdown is validated against **KFM-MDP v11.2.5** and YAML front-matter schemas.  

2. **Metadata & Ontology Compliance**  
   - STAC/DCAT/JSON-LD validation enforces catalog and ontology integrity across geospatial layers and docs.  
   - PROV-O and OpenLineage metadata are checked for completeness, ensuring end-to-end lineage from ETL job → catalog → graph.  

3. **Security & Supply-Chain**  
   - `security_audit.yml` and `dependabot.yml` enforce dependency and secret hygiene.  
   - `sbom_verify.yml` and SLSA attestations ensure reproducible, trustworthy releases.  

4. **AI & Focus Mode Governance**  
   - `ai_behavior_check.yml` and `focusmode_mlops.yml` verify narrative safety, drift, and forbidden behaviors before any AI config or model card merge.  

5. **FAIR+CARE & Sovereignty Enforcement**  
   - `faircare_validate.yml` and `h3_generalization.yml` prevent exposing sensitive heritage or tribal locations and enforce CARE labels.  

6. **Telemetry & Sustainability**  
   - `telemetry_export.yml` aggregates metrics on CI runs, governance outcomes, and energy/carbon usage into `github-infra-telemetry.json`.  

---

## 🧪 Validation & CI/CD

### Required Checks for Protected Branches

For `main` and release branches, merges MUST pass:

- `ci.yml` — core tests and linting  
- `docs_validate.yml` — markdown & documentation checks  
- `stac_validate.yml` — STAC validation for updated assets  
- `dcat_validate.yml` — DCAT validation for dataset records  
- `jsonld_validate.yml` — ontology and JSON-LD checks  
- `faircare_validate.yml` — FAIR+CARE and ethics checks  
- `h3_generalization.yml` — enforcement of spatial masking rules  
- `ai_behavior_check.yml` — AI narrative safety checks (if AI paths touched)  
- `security_audit.yml` — security scanning and dependency checks  
- `sbom_verify.yml` — SBOM and release manifest verification  
- `telemetry_export.yml` — telemetry emission and schema validation  

Workflows run **selectively but deterministically** based on changed paths (e.g., only run STAC checks if `data/stac/` changes).

### Environments

- **dev → staging**: automated promotions once CI passes.  
- **staging → production**: require human approval, signing, and governance review.  

All promotions emit **OpenLineage events** and are modeled as PROV activities in the knowledge graph.

---

## 📦 Data & Metadata

`.github/` contributes to KFM metadata and provenance via:

- **SBOMs** (`sbom_ref`) for each release  
- **Manifests** (`manifest_ref`) listing all release artifacts  
- **Signatures** (`signature_ref`) proving artifact authenticity  
- **SLSA Attestations** (`attestation_ref`) capturing supply-chain provenance  
- **Telemetry** (`telemetry_ref`) describing CI/CD, AI, and governance behavior  

These artifacts are:

- Referenced by data catalogs and documentation (`docs/data/`, `docs/security/`)  
- Persisted for reproducibility and audit trails  
- Used by Story Nodes / Focus Mode to generate system-level narratives (e.g., “how trustworthy is this release?”).  

---

## 🌐 STAC, DCAT & PROV Alignment

`.github/` is the enforcement layer for KFM’s catalog and provenance strategy:

- **STAC (SpatioTemporal Asset Catalog)**  
  - `stac_validate.yml` validates Items and Collections under `data/stac/**` against STAC 1.x schemas and KFM-STAC profiles.  
  - Ensures `id`, `geometry`, `bbox`, `datetime`, and `assets` are present and coherent for ingestion into the knowledge graph.  

- **DCAT 3.0**  
  - `dcat_validate.yml` checks dataset/distribution records and dataset series, including versioning and checksum metadata aligned with SPDX.  
  - Guarantees catalog metadata is federatable while preserving KFM-specific FAIR+CARE fields.  

- **PROV-O + OpenLineage**  
  - `jsonld_validate.yml` and telemetry checks ensure datasets, models, workflows, and releases can be expressed as PROV entities, activities, and agents.  
  - CI jobs themselves are modeled as Activities emitting lineage for ETL runs and AI training, consistent with KFM reproducibility requirements.  

- **GeoSPARQL & Spatial Semantics**  
  - Geometry and spatial metadata (e.g., footprints from STAC) are validated so they can be mapped to GeoSPARQL `geo:Feature` and `geo:Geometry` in the graph.  

---

## 🧠 Story Node & Focus Mode Integration

KFM’s narrative system builds **Story Nodes** over the graph and documents; `.github/` provides the **operational backstory**:

- Each successful CI run is a **PROV Activity** with associated Agents (humans, bots, services) and Entities (artifacts, docs, STAC/DCAT records).  
- Focus Mode can answer questions like:  
  - “How was this hazards model validated before deployment?”  
  - “Which release first introduced archaeology-sensitive masking?”  
- Telemetry and provenance events are routed into Neo4j so narratives can cross-link:  
  - Historical & ecological layers  
  - New data domains (paleontology, climate futures, biodiversity, etc.)  
  - Open data sources and tools (KGS, DASC, BLM, county portals, etc.)  

`.github/` thus acts as a **governed narrative spine**: every dataset, model, or feature in Story Nodes should be traceable back to at least one governed CI path and release event.

---

## 🗺️ Diagrams

Detailed architecture and workflow diagrams live in:

- `.github/ARCHITECTURE.md` — CI/CD topology, workflow dependencies, and environment promotion flows  
- `docs/architecture/**` — system-level diagrams linking ETL, catalogs, graph, API, and web  

All diagrams MUST:

- Be referenced from this section,  
- Use machine-readable formats (e.g., Mermaid, PlantUML) where possible, and  
- Align with the STAC/DCAT/PROV and GeoSPARQL modeling described here.  

---

## ⚖ FAIR+CARE & Governance

`.github/` encodes FAIR+CARE principles by:

- Requiring provenance for datasets, pipelines, and models, especially for sensitive domains like archaeology and Indigenous histories.  
- Validating metadata completeness for STAC/DCAT, ensuring **Findable, Accessible, Interoperable, Reusable** datasets.  
- Enforcing CARE labels and sovereignty flags wherever required in front-matter and catalog JSON.  
- Blocking merges that might expose sensitive heritage locations (H3 generalization of archaeological and tribal sites).  
- Ensuring documentation is markdown-protocol compliant so it can be ingested as Story Nodes and graph entities.  

Normative governance references:

- `../docs/standards/governance/ROOT-GOVERNANCE.md`  
- `../docs/standards/faircare/FAIRCARE-GUIDE.md`  
- `../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md`  

These are authoritative for any change touching policy, data sensitivity, or community impacts.

---

## 🕰️ Version History

| Version | Date       | Summary                                                                                                                |
|--------:|------------|------------------------------------------------------------------------------------------------------------------------|
| v11.2.3 | 2025-12-08 | Aligned with KFM-MDP v11.2.5; added Context, STAC/DCAT/PROV, Story Node, and Diagrams sections; updated provenance.   |
| v11.2.2 | 2025-11-28 | Rebuilt to align with KFM-MDP v11.2.4; stabilized directory layout; documented AI, FAIR+CARE, and telemetry wiring.   |
| v11.0.2 | 2025-11-27 | Governance & supply-chain refinements; expanded FAIR+CARE enforcement hooks.                                          |
| v11.0.1 | 2025-11-23 | Ontology/metadata integration; narrative-safety checks routed into CI.                                                |
| v11.0.0 | 2025-11-19 | First governed v11 GitHub infrastructure README; CI/CD baseline.                                                      |
| v10.4.1 | 2025-11-16 | Pre-v11 FAIR+CARE integration into CI workflows.                                                                      |
| v10.4.0 | 2025-11-15 | KFM-MDP v10.4 aligned repo-level CI documentation.                                                                    |
| v10.3.2 | 2025-11-14 | Added telemetry capture and reporting for CI.                                                                         |
| v10.0.0 | 2025-11-10 | Initial `.github/` infrastructure documentation.                                                                      |

---

<div align="center">

⚙️ **Kansas Frontier Matrix — GitHub Infrastructure (v11.2.3)**  
Automation-First · FAIR+CARE-Governed · Provenance-Aware  

[⬅️ Back to Repository Root](../README.md) · [🏗 ARCHITECTURE](ARCHITECTURE.md) · [🛡 SECURITY Policy](SECURITY.md) · [📜 Governance](../docs/standards/governance/ROOT-GOVERNANCE.md) · [⚖ FAIR+CARE](../docs/standards/faircare/FAIRCARE-GUIDE.md) · [🪶 Indigenous Data Protection](../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

</div>