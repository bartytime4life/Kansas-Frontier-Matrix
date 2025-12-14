---
title: "📦 Kansas Frontier Matrix — Staging Data Workspace (Diamond9 Omega / CrownInfinityOmega Ultimate Certified)"
path: "data/work/staging/README.md"

version: "v11.1.1"
last_updated: "2025-12-14"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Continuous · Autonomous · FAIR+CARE Council Oversight"
content_stability: "stable"

status: "Active / Enforced"
doc_kind: "Data Layer"
header_profile: "standard"
footer_profile: "standard"
diagram_profiles:
  - "mermaid-flowchart-v1"

license: "Internal · FAIR+CARE Certified"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

scope:
  domain: "data-work"
  applies_to:
    - "data/work/staging/**"

fair_category: "F1-A1-I1-R1"
care_label: "Internal · CARE-Verified"
sensitivity: "General (non-sensitive; auto-mask rules apply)"
sensitivity_level: "Low"
public_exposure_risk: "Medium"
classification: "Internal"
jurisdiction: "Kansas / United States"

indigenous_rights_flag: true
data_steward: "KFM FAIR+CARE Council"

ttl_policy: "24 months"
sunset_policy: "Superseded by a later Work Layer staging spec"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"

signature_ref: "../../../releases/v11.1.1/signature.sig"
attestation_ref: "../../../releases/v11.1.1/slsa-attestation.json"
sbom_ref: "../../../releases/v11.1.1/sbom.spdx.json"
manifest_ref: "../../../releases/v11.1.1/manifest.zip"

telemetry_ref: "../../../releases/v11.1.1/focus-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/data-work-staging-v11.json"
energy_schema: "../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "TechArticle"
  prov_o: "prov:Plan"
  owl_time: "ProperInterval"
  geosparql: "geo:FeatureCollection"

metadata_profiles:
  - "STAC 1.0.0"
  - "DCAT 3.0"
  - "PROV-O"
  - "FAIR+CARE"

provenance_chain:
  - "data/work/staging/README.md@v11.1.0"
  - "data/work/staging/README.md@v11.0.0"
  - "data/work/staging/README.md@v10.0.0"

story_node_refs: []
immutability_status: "version-pinned"

doc_uuid: "urn:kfm:doc:data-work:staging:v11.1.1"
semantic_document_id: "kfm-data-work-staging-v11.1.1"
event_source_id: "ledger:kfm:doc:data-work:staging:v11.1.1"
doc_integrity_checksum: "<sha256>"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"

ai_transform_permissions:
  - "summary"
  - "timeline-generation"
  - "semantic-highlighting"
  - "a11y-adaptations"
  - "diagram-extraction"
  - "metadata-extraction"
  - "layout-normalization"

ai_transform_prohibited:
  - "content-alteration"
  - "speculative-additions"
  - "unverified-architectural-claims"
  - "narrative-fabrication"
  - "governance-override"

transform_registry:
  allowed:
    - "summary"
    - "timeline-generation"
    - "semantic-highlighting"
    - "a11y-adaptations"
    - "diagram-extraction"
    - "metadata-extraction"
    - "layout-normalization"
  prohibited:
    - "content-alteration"
    - "speculative-additions"
    - "unverified-architectural-claims"
    - "narrative-fabrication"
    - "governance-override"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
---

<div align="center">

# 📦 **Kansas Frontier Matrix — Staging Data Workspace**
`data/work/staging/README.md`

**Purpose**  
Define the **controlled, FAIR+CARE-supervised staging environment** for Kansas Frontier Matrix datasets.  
This workspace is the **pre-publication validation zone** where datasets undergo **schema alignment**, **FAIR+CARE audits**, **checksum verification**, **provenance registration**, and **telemetry recording** before promotion into the **Processed Layer**.

<img src="https://img.shields.io/badge/MCP--DL-v6.3-blueviolet" />
<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/Classification-Internal-informational" />
<img src="https://img.shields.io/badge/FAIR%2BCARE-Governance%20Aligned-orange" />
<img src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />

</div>

## 📘 Overview

### 1. Role in the KFM pipeline
The Staging Workspace bridges:

**raw ingestion → temporary processing → validation → ethics review → governance registration → processed publication**

It is the internal “gate” used to prevent unsafe, non-compliant, or invalid artifacts from reaching the Processed Layer.

### 2. What staging is (and is not)
**Staging is:**
- a controlled workspace for intermediate artifacts,
- a deterministic-validation checkpoint (schemas, checksums, provenance),
- a governance checkpoint (FAIR+CARE + sovereignty review as needed),
- a telemetry checkpoint (sustainability + audit completeness).

**Staging is not:**
- a long-term storage layer,
- a public distribution layer,
- a place to publish STAC/DCAT as final outputs.

### 3. Promotion rule (high-level)
Promotion to the Processed Layer is allowed only when:
- validation status is `passed`,
- integrity checks match expected manifests,
- provenance is complete and linkable,
- licensing/rights are cleared,
- governance decision is recorded (or explicitly not required for the artifact class).

## 🗂️ Directory Layout

~~~text
📁 data/
└── 📁 work/
    └── 📁 staging/                               — Controlled, internal staging workspace
        ├── 📄 README.md                          — This document
        │
        ├── 📁 tabular/                           — Intermediate tabular artifacts (pre-processed)
        │   ├── 📁 tmp/                           — Ephemeral transformation outputs (safe to purge)
        │   ├── 📁 normalized/                    — Schema-aligned intermediate tables
        │   ├── 📁 validation/                    — Validation results (schema + QC + FAIR+CARE)
        │   └── 📁 logs/                          — Run logs, telemetry, audit traces
        │
        ├── 📁 spatial/                           — Intermediate spatial artifacts (vectors/rasters)
        │   ├── 📁 tmp/                           — Ephemeral transformation outputs (safe to purge)
        │   ├── 📁 normalized/                    — CRS-aligned intermediates, topology-ready outputs
        │   ├── 📁 validation/                    — Spatial validation (CRS/topology/coverage)
        │   └── 📁 logs/                          — Run logs, telemetry, audit traces
        │
        └── 📁 metadata/                          — Metadata bundles for promotion readiness
            ├── 📁 tmp/                           — Ephemeral metadata generation outputs
            ├── 📁 validation/                    — Metadata validation (schemas + completeness)
            └── 📁 logs/                          — Metadata pipeline logs + audit traces
~~~

## 🧭 Context

### 1. Why staging exists
Staging exists to enforce:
- deterministic ETL normalization,
- schema alignment and machine validation,
- provenance completeness (PROV-O),
- integrity checks (hashes + manifests),
- governance constraints (FAIR+CARE + sovereignty),
- telemetry capture for sustainability and auditability.

### 2. Internal-only constraint
This directory is **internal-only** and **must not be treated as published data**. Any artifact intended for public distribution must be promoted into the Processed Layer and represented through the catalog outputs (STAC/DCAT) with the required governance controls.

## 🗺️ Diagrams

~~~mermaid
flowchart LR
  A["Raw ingestion"] --> B["Staging tmp"]
  B --> C["Normalize to schemas"]
  C --> D["Validation and QA"]
  D --> E["FAIR+CARE and sovereignty review"]
  E --> F{"Promotion decision"}
  F -->|approved| G["Processed layer publish"]
  F -->|rejected| H["Fix and re-run"]
  G --> I["STAC and DCAT publication"]
  G --> J["PROV and OpenLineage records"]
~~~

The staging flow above shows the gating function: artifacts only move forward after validation and governance checks, with lineage preserved across each step.

## 🧠 Story Node & Focus Mode Integration

### 1. How Focus Mode may use staging docs
Focus Mode may summarize this document and extract metadata for internal navigation and governance auditing.

### 2. Restrictions
Because staging may reference sensitive operational practices, Focus Mode usage must:
- avoid inventing approval status,
- avoid claiming a dataset is “published” when it is only staged,
- avoid revealing sensitive operational details beyond what is documented.

## 🧪 Validation & CI/CD

### 1. CI-enforced checks
This README (and any staging documentation) is expected to pass:
- `markdown-lint`
- `schema-lint`
- `metadata-check`
- `diagram-check`
- `footer-check`
- `accessibility-check`
- `provenance-check`
- `secret-scan`
- `pii-scan`

### 2. Dataset promotion gates (staging-to-processed)
Before promotion, staged datasets must pass (as applicable):
- JSON schema validation
- checksum integrity checks (e.g., SHA256)
- provenance chain completeness (PROV-O)
- licensing checks (rights + allowed use)
- telemetry completeness (energy + carbon fields where required)
- spatial (if applicable): CRS enforcement + topology QA
- tabular (if applicable): field type enforcement + missingness checks

## 📦 Data & Metadata

### 1. What goes into staging
Typical staged artifacts include:
- intermediate tables (normalized schemas, canonical field types),
- intermediate vectors/rasters (CRS-aligned, simplified, cleaned),
- validation outputs and coverage reports,
- derived metadata bundles required for catalog publication readiness.

### 2. Entity requirements (PROV-O)
All staged artifacts should be representable as `prov:Entity` with:
- a stable identifier (internal staging ID),
- checksum(s) (e.g., `sha256`),
- dataset type (`tabular` / `spatial` / `metadata`),
- schema version reference,
- validation state (`in_review` / `passed` / `failed`),
- governance pointers (where review is required),
- timestamps (ISO 8601).

### 3. Activity and agent requirements
Staging activities should be representable as `prov:Activity` and linked to:
- pipeline version,
- parameter digest,
- timestamps,
- input entities and output entities,
- responsible `prov:Agent` (team, service account, or steward role).

### 4. Example staging metadata record
~~~json
{
  "id": "staging_tabular_environmental_indicators_v11",
  "dataset_type": "tabular",
  "schema_version": "v3.3.0",
  "records_processed": 55204,
  "validation_status": "in_review",
  "checksum_sha256": "sha256:<sha256>",
  "care_status": "in_review",
  "telemetry": {
    "energy_wh": 7.4,
    "co2_g": 9.8,
    "validation_coverage_pct": 100
  },
  "governance_ref": "../../../docs/standards/governance/ROOT-GOVERNANCE.md",
  "created": "2025-12-14T00:00:00Z"
}
~~~

## 🌐 STAC, DCAT & PROV Alignment

### 1. STAC
Staging artifacts are **not** the public catalog. However, staging may prepare STAC-ready metadata so that promotion can emit:
- STAC Collections under `data/stac/collections/`
- STAC Items under `data/stac/items/`
- assets referencing processed outputs (not staging temp paths)

### 2. DCAT
Staging supports DCAT readiness by enforcing:
- stable identifiers,
- rights/license clarity,
- lineage traceability,
- distribution separation (internal staging vs. published processed).

### 3. PROV-O
Staging is expected to emit or prepare:
- Entities: raw inputs, staged intermediates, validation reports, processed outputs
- Activities: normalization, validation, governance review, promotion
- Agents: pipeline runners, stewards, councils, CI bots

## 🧱 Architecture

### 1. Isolation and determinism
Staging must remain isolated from production-facing outputs. Pipelines should be deterministic and replayable, with:
- pinned tool versions,
- config snapshots recorded in logs,
- stable identifiers across runs where applicable,
- explicit promotion activities recorded in provenance.

### 2. Interface boundaries
The frontend must not read from staging. Only:
- processed outputs and catalogs (STAC/DCAT),
- API/graph surfaces,
are supported interfaces for user-facing experiences.

## ⚖ FAIR+CARE & Governance

### 1. Governance constraint
All staging work is governed by:
- the KFM Governance Charter,
- FAIR+CARE guidance,
- sovereignty and Indigenous data protection requirements.

### 2. Default safety posture
When there is any risk of sensitive location disclosure or restricted knowledge:
- staging validation must enforce redaction/generalization rules as required,
- promotion must be blocked until governance requirements are satisfied.

---

<div align="center">

[⬅️ Back to Work Layer](../README.md) ·
[📐 Data Architecture](../../../docs/ARCHITECTURE.md) ·
[🏛️ Governance Charter](../../../docs/standards/governance/ROOT-GOVERNANCE.md) ·
[🧭 FAIR+CARE Guide](../../../docs/standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

</div>

## 🕰️ Version History

| Version | Date | Author | Summary |
|---|---:|---|---|
| v11.1.1 | 2025-12-14 | `@kfm-staging` | KFM-MDP v11.2.6 compliance pass (front-matter requirements, approved H2s, tilde fences, footer governance links). |
| v11.1.0 | 2025-11-19 | `@kfm-staging` | Full staging workspace definition; validation logic expansion; telemetry alignment; directory normalization. |
| v11.0.0 | 2025-11-15 | `@kfm-staging` | Initial v11 staging layer migration. |
| v10.0.0 | 2025-11-09 | `@kfm-staging` | Original staging workspace definition. |
