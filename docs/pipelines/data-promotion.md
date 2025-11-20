---
title: "🚀 Kansas Frontier Matrix — Data Promotion Protocol & Governance Guide (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/pipelines/data-promotion.md"

version: "v11.0.0"
last_updated: "2025-11-20"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · FAIR+CARE Council · Autonomous"
backward_compatibility: "Full v10.x → v11.x compatibility"

commit_sha: "<latest-commit-hash>"
signature_ref: "../../releases/v11.0.0/signature.sig"
attestation_ref: "../../releases/v11.0.0/slsa-attestation.json"

sbom_ref: "../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../schemas/telemetry/pipelines-data-promotion-v11.json"
energy_schema: "../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../schemas/telemetry/carbon-v2.json"

governance_ref: "../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"
care_label: "Collective Benefit · Authority to Control · Responsibility · Ethics"
risk_profile: "High Governance · Requires Lineage Completeness · Auto-Masked Sensitive Data"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
ontology_protocol_version: "KFM-OP v11.0"
pipeline_contract_version: "KFM-PDC v11.0"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"

status: "Active / Enforced"
doc_kind: "Architecture"
intent: "data-promotion"
category: "Pipelines · Governance · Data Promotion · Lineage Control"
sensitivity: "General (auto-masking for protected datasets)"
classification: "Public Document"
jurisdiction: "Kansas / United States"

prov_profile: "PROV-O Core + KFM Promotion Lineage Extensions"
openlineage_profile: "OpenLineage v2.5 + KFM Extensions"

ontology_ref:
  - "../graph/ontology/core-entities.md"
  - "../graph/ontology/cidoc-crm-mapping.md"
  - "../graph/ontology/spatial-temporal-patterns.md"

metadata_profiles:
  - "../../schemas/stac/kfm-stac-v11.json"
  - "../../schemas/dcat/kfm-dcat-v11.json"
  - "../../schemas/jsonld/kfm-context-v11.json"

validation_profiles:
  - "docs-lint-v11"
  - "schema-lint-v11"
  - "lineage-audit-v11"
  - "governance-audit-v11"
  - "promotion-check-v11"

ci_integration:
  workflow: ".github/workflows/kfm-ci.yml"
  environment: "dev → staging → production"

runtime:
  compute: "KFM Multi-Cloud Mesh (AWS + GCP + On-Prem)"
  graph_engine: "Neo4j Enterprise v5.x Cluster"
  api_stack: "FastAPI · GraphQL Gateway (GovHooks v4)"
  frontend_stack: "React · MapLibre · Cesium · Vite"
  lineage_bus: "OpenLineage v2.5"
  reliability_engine: "Reliable Pipelines v11 — WAL · Retry · Rollback · Hotfix · Lineage"
  agents: "LangGraph Autonomous Updater v11"

fair_category: "F1-A1-I1-R1"
sensitivity_level: "Medium"
public_exposure_risk: "Low to Medium"
indigenous_rights_flag: true
data_steward: "KFM FAIR+CARE Council"
redaction_required: false

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "TechArticle"
  owl_time: "ProperInterval"
  prov_o: "prov:Plan"
  geosparql: "geo:FeatureCollection"

json_schema_ref: "../../schemas/json/pipelines-data-promotion-v11.schema.json"
shape_schema_ref: "../../schemas/shacl/pipelines-data-promotion-v11-shape.ttl"

doc_uuid: "urn:kfm:docs:pipelines:data-promotion:v11.0.0"
semantic_document_id: "kfm-pipelines-data-promotion"
event_source_id: "ledger:docs/pipelines/data-promotion.md"
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summaries"
  - "semantic-highlighting"
  - "a11y-adaptations"
ai_transform_prohibited:
  - "speculative additions"
  - "modifying authoritative results"
  - "unverified architectural claims"
  - "promotion decisions"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
ttl_policy: "Review required every 12 months"
sunset_policy: "Superseded with Pipeline Promotion Contract v12"
---

<div align="center">

# 🚀 **Kansas Frontier Matrix — Data Promotion Protocol & Governance Guide (v11.0.0)**  
`docs/pipelines/data-promotion.md`

**Purpose:**  
Define the **complete v11 LTS specification** for dataset, entity, and model **promotion** within the KFM pipeline ecosystem.  
Describes how raw → staged → validated → promoted data transitions occur under FAIR+CARE governance, sovereignty-aware controls, STAC/DCAT metadata requirements, and PROV-O lineage enforcement.

</div>

---

# 📘 Executive Summary

Promotion in KFM v11 is a **governed, multi-phase, auditable workflow** ensuring that:

- Only validated, ethical, and sovereignty-compliant data reaches the **trusted graph**  
- All transformations are reproducible and lineage-complete  
- AI-assisted suggestions never bypass review  
- Sensitive cultural data is masked, generalized, or fully withheld  
- STAC/DCAT metadata is attached prior to promotion  
- Promotion is logged immutably in **Ledger v4**  
- Each promotion is auditable against **Pipeline Contracts v11**, CARE policies, and governance rules  

Promotion is **not automatic**. It is a deliberate, evidence-backed, policy-enforced process.

---

# 📦 1. Promotion Lifecycle Overview

Promotion has **four phases**, each required and validated by CI/Governance:

```mermaid
flowchart LR
    A[Raw Layer] --> B[Staging Layer]
    B --> C[Validated Layer]
    C --> D[Promoted Layer]
    D --> E[Ledger v4 Entry]
```

## 1. Raw Layer  
- Data is ingested, checksummed, and frozen  
- No transformations allowed  
- Stored under `data/raw/` or remote equivalent  
- Registered in STAC/DCAT source registry  

## 2. Staging Layer  
- Deterministic ETL + AI enrichment (provenance attached)  
- Intermediate STAC Items produced  
- CI validation required before proceeding  
- Stored under `data/staging/`  

## 3. Validated Layer  
- Passes **full validation suite**:
  - Schema
  - Ontology
  - FAIR+CARE  
  - Sovereignty rules  
  - Lineage completeness  
  - Drift/bias/failure checks  
- Stored under `data/validated/`  

## 4. Promoted Layer  
- Official, canonical representation inside:
  - **Neo4j knowledge graph**  
  - **STAC/DCAT catalogs**  
  - **Historical + narrative pipelines**  
- Immune to modification except through approved hotfix protocol  

---

# 🧪 2. Validation Gates Required for Promotion

Promotion requires all validation pipelines to pass:

### Structural  
- STAC v11 schema  
- DCAT v11 dataset schema  
- JSON-LD w/ KFM context  
- CRS + bbox checks  
- GeoJSON validation  

### Semantic  
- CIDOC-CRM mapping  
- GeoSPARQL compliance  
- OWL-Time reasoning  
- Entity uniqueness  
- Canonical ID enforcement  

### Ethical & Sovereignty  
- CARE rules applied  
- Indigenous sovereignty policy enforced  
- Mask sensitive coordinates (H3 r7 generalization)  
- Remove sensitive narrative or imagery  

### Lineage  
- Full PROV-O chain  
- OpenLineage event completeness  
- Deterministic re-run consistency  

### Sustainability  
- Energy usage  
- Carbon emissions  
- Data movement cost  

Promotion **fails** if any gate fails.

---

# 🔄 3. Promotion Workflows (Human + Automated)

Promotion combines **human signoff** + **automated rule enforcement**.

```mermaid
flowchart TD
    A[CI Validation] --> B[Governance Audit]
    B --> C{FAIR+CARE Review}
    C -->|Approved| D[Promotion Commit]
    C -->|Rejected| E[Quarantine]
    D --> F[Ledger v4]
```

### Required Human Roles  
- FAIR+CARE reviewer  
- Sovereignty reviewer (if Indigenous-linked datasets)  
- Domain steward (hydrology, archaeology, climate, etc.)  

### Automated Roles  
- GovHooks v4  
- Pipeline Contract Enforcer  
- Lineage Auditor  
- STAC/DCAT metadata validator  

---

# 🧱 4. Hotfix, Rollback & Re-Promotion Protocol

Promotion errors are inevitable — KFM v11 supports:

### Hotfix  
- Fix a promoted dataset **without overwriting history**  
- Creates a *sibling* entity with `hotfix` flag  
- Leaves original lineage intact  

### Rollback  
- Invalidate a promoted dataset  
- Does **not** delete the entity  
- Marks as superseded, pushes update to Ledger v4  

### Re-Promotion  
- Requires full pipeline re-run  
- Must generate new lineage + new STAC/DCAT entries  

---

# 🛰️ 5. Promotion Metadata Requirements

Every promoted dataset/entity MUST contain:

- `promotion_version`  
- `promotion_timestamp`  
- `promotion_actor` (human + automated agents)  
- `promotion_reason`  
- Lineage bundles  
- Ethics + CARE labels  
- Sovereignty flags  
- STAC/DCAT Item + Collection links  

Promotion metadata is considered **immutable**.

---

# 🧭 6. Focus Mode & Story Node Interaction

Promotion affects:

### Focus Mode v3  
- Only promoted (trusted) graph entities may influence reasoning  
- Unvalidated or staging-layer entities are ignored  

### Story Nodes v3  
- Story Nodes may only reference **promoted entities**  
- Narrative generation must use canonical IDs  
- Temporal reasoning requires validated OWL-Time intervals  

---

# 🛡️ 7. Governance Plane Integration

Promotion is deeply tied to:

- **GovHooks v4** enforcement  
- **Ledger v4** immutability  
- **FAIR+CARE Council** oversight  
- **Sovereignty review** for culturally sensitive data  
- Automated compliance scoring  

Promotion is not just technical — it is ethical, legal, and community-centered.

---

# 🕰 Version History

| Version | Date       | Notes                                                                 |
|--------:|-----------:|-----------------------------------------------------------------------|
| v11.0.0 | 2025-11-20 | Initial Data Promotion Protocol & Governance Guide for KFM v11 LTS.   |

---

# 🔗 Footer

**Back to Root:** `../../README.md`  
**Back to Architecture:** `../architecture/system_overview.md`  
**Back to Standards:** `../standards/README.md`

