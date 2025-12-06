---
title: "⚖️ Kansas Frontier Matrix — FAIR+CARE Data Governance Framework (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/standards/faircare.md"

version: "v11.0.0"
last_updated: "2025-11-20"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Annual / FAIR+CARE Council"
content_stability: "stable"

commit_sha: "<latest-commit-hash>"
signature_ref: "releases/v11.0.0/signature.sig"
attestation_ref: "releases/v11.0.0/slsa-attestation.json"
sbom_ref: "releases/v11.0.0/sbom.spdx.json"
manifest_ref: "releases/v11.0.0/manifest.zip"
telemetry_ref: "releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "schemas/telemetry/docs-faircare-v11.json"
energy_schema: "schemas/telemetry/energy-v2.json"
carbon_schema: "schemas/telemetry/carbon-gco2e-v1.json"

governance_ref: "governance/ROOT-GOVERNANCE.md"
ethics_ref: "faircare.md"
sovereignty_policy: "sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.4"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

status: "Active / Enforced"
doc_kind: "Standard"
intent: "faircare-governance"

header_profile: "standard"
footer_profile: "standard"
diagram_profiles:
  - "mermaid-flowchart-v1"

scope:
  domain: "governance-faircare"
  applies_to:
    - "all-datasets"
    - "all-models"
    - "all-story-nodes"
    - "focus-mode"
    - "governance-ledgers"
    - "telemetry"

semantic_document_id: "kfm-doc-faircare"
doc_uuid: "urn:kfm:docs:standards:faircare-v11.0.0"
event_source_id: "ledger:kfm:doc:standards:faircare:v11.0.0"
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Medium-Sensitivity"
sensitivity: "Governance & ethics guidance (non-PII)"
sensitivity_level: "Low"
public_exposure_risk: "Low"
classification: "Public"
jurisdiction: "Kansas / United States"
indigenous_rights_flag: true
data_steward: "KFM FAIR+CARE Council"
lifecycle_stage: "stable"
ttl_policy: "36 months"
sunset_policy: "Superseded by FAIR+CARE v12.0"

provenance_chain:
  - "docs/standards/faircare.md@v10.2.2"
  - "Master Coder Protocol 2.0.pdf"
  - "Archaeology (MCP Domain Module).pdf"
  - "KFM Technical Guide v11.pdf"

provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: false

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "Dataset"
  prov_o: "prov:Plan"

metadata_profiles:
  - "FAIR"
  - "CARE"
  - "STAC 1.0.0"
  - "DCAT 3.0"
  - "PROV-O"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summary"
  - "timeline-generation"
  - "semantic-highlighting"
  - "representation"
  - "metadata-extraction"
ai_transform_prohibited:
  - "content-alteration"
  - "speculative-additions"
  - "unverified-ethical-claims"
  - "narrative-fabrication"
  - "governance-override"

transform_registry:
  allowed:
    - summary
    - timeline-generation
    - semantic-highlighting
    - representation
    - metadata-extraction
  prohibited:
    - content-alteration
    - speculative-additions
    - unverified-ethical-claims
    - narrative-fabrication
    - governance-override

json_schema_ref: "schemas/json/kfm-faircare-v11.0.0.schema.json"
shape_schema_ref: "schemas/shacl/kfm-faircare-v11.0.0-shape.ttl"
story_node_refs: []

heading_registry:
  approved_h2:
    - "📘 Overview"
    - "🗂️ Directory Layout"
    - "🧭 FAIR Principles"
    - "🤝 CARE Principles"
    - "🧱 FAIR+CARE Metadata Requirements"
    - "🧬 FAIR+CARE Data Lifecycle"
    - "🧪 Validation & CI/CD"
    - "🔐 Governance Ledger Compliance"
    - "📖 Narrative Governance (Story Nodes & Focus Mode)"
    - "📊 Audits & Scoring"
    - "🧾 Examples"
    - "🕰️ Version History"

test_profiles:
  - "markdown-lint"
  - "schema-lint"
  - "metadata-check"
  - "faircare-check"
  - "diagram-check"
  - "provenance-check"
  - "footer-check"
  - "accessibility-check"

ci_integration:
  workflow: ".github/workflows/faircare-governance.yml"
  environment: "dev → staging → production"

branding_registry:
  standard: "Technical Integrity × Ethical Responsibility × Community Sovereignty"

layout_profiles:
  - "immediate-one-branch-with-descriptions-and-emojis"

badge_profiles:
  - "root-centered-badge-row"

requires_purpose_block: true
requires_directory_layout_section: true
requires_version_history: true
requires_governance_links_in_footer: true

deprecated_fields:
  - "legacy_faircare_standard_v10"
---

<div align="center">

# ⚖️ **Kansas Frontier Matrix — FAIR+CARE Data Governance Framework (v11.0.0)**  
`docs/standards/faircare.md`

**Purpose**  
Define the **ethical, procedural, and technical governance framework** for applying  
**FAIR (Findable, Accessible, Interoperable, Reusable)** and  
**CARE (Collective Benefit, Authority to Control, Responsibility, Ethics)**  
principles across the entire Kansas Frontier Matrix (KFM) ecosystem.  

This standard governs all **datasets**, **metadata**, **models**, **AI pipelines**, **scientific workflows**,  
**Story Node v3 narratives**, and **Focus Mode v3 contexts**, ensuring an integrated approach to  
open science, community sovereignty, cultural protection, and ethical AI.

[![Docs · MCP v6.3](https://img.shields.io/badge/Docs-MCP_v6.3-blue)]() ·
[![KFM-MDP v11.2.4](https://img.shields.io/badge/KFM%E2%80%93MDP-v11.2.4-purple)]() ·
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Framework-gold)]()

</div>

---

## 📘 Overview

The KFM FAIR+CARE Framework ensures:

- **FAIR** — technical interoperability, discoverability, and reusability.  
- **CARE** — cultural sovereignty, community benefit, and ethical governance.

It applies to:

- Data ingestion and normalization  
- Metadata creation and cataloging  
- Modeling & simulation workflows  
- Story Node generation and curation  
- Focus Mode overlays and summarization  
- Public datasets & internal restricted sets  
- Sustainability telemetry and audits  
- AI model training and deployment governance  

All FAIR+CARE rules are **machine-enforced** via CI/CD pipelines and **human-governed** via the FAIR+CARE Council and partner communities.

---

## 🗂️ Directory Layout

~~~text
📂 KansasFrontierMatrix/
└── 📂 docs/
    ├── 📂 standards/
    │   ├── 📄 README.md                        # Standards index
    │   ├── 📄 faircare.md                      # ⚖️ FAIR+CARE Governance Framework (this file)
    │   ├── 📄 licensing.md                     # 📜 Licensing & IP Standards
    │   ├── 📄 telemetry_standards.md           # 📈 Telemetry Super-Standard
    │   ├── 📄 ui_accessibility.md              # ♿ UI Accessibility & Inclusion Super-Standard
    │   ├── 📄 kfm_markdown_protocol_v11.2.4.md # 📑 Markdown Authoring Protocol
    │   ├── 📂 governance/
    │   │   ├── 📄 README.md                    # 🏛️ Governance & Ethical Oversight Framework
    │   │   └── 📄 ROOT-GOVERNANCE.md           # 🏛️ Root Governance Charter
    │   └── 📂 sovereignty/
    │       └── 📄 INDIGENOUS-DATA-PROTECTION.md # 🪶 Indigenous Data Protection Policy
    └── 📄 glossary.md                          # Shared terms (including FAIR+CARE)
~~~

**Author rules**

- This file is the **root FAIR+CARE governance standard** for KFM.  
- Any domain-specific FAIR+CARE guidance (e.g., for archaeology, hydrology, education) MUST:
  - Live under `docs/standards/` or a domain subfolder, and  
  - Reference this file in a “Related Standards” or “FAIR+CARE Alignment” section.  
- All new data-related standards MUST explicitly reference FAIR+CARE expectations defined here.

---

## 🧭 FAIR Principles

| Principle | Meaning                                       | KFM v11 Implementation                               |
|----------|-----------------------------------------------|-----------------------------------------------------|
| **F1 — Findable**     | Persistent IDs & searchable metadata     | Global UUIDs, STAC/DCAT identifiers, JSON-LD       |
| **F2 — Accessible**   | Retrievable through standard protocols   | HTTPS, Range-GET, CDNs, tiered access               |
| **F3 — Interoperable**| Shared vocabularies / ontologies         | STAC 1.x, DCAT 3.0, CIDOC CRM, OWL-Time, schema.org |
| **F4 — Reusable**     | Clear licensing & provenance             | SPDX, SBOMs, checksums, KFM lineage chain           |

### FAIR CI Enforcement

FAIR is enforced via:

- `stac-validate.yml`  
- `data-contract-validate.yml`  
- `docs-lint.yml`  
- `telemetry-export.yml`  

Core outputs:

~~~text
reports/self-validation/stac_validation.json
reports/fair/faircare_summary.json
~~~

These outputs are modeled as PROV entities and linked to datasets, workflows, and governance events.

---

## 🤝 CARE Principles

| Principle | Meaning                                | KFM v11 Implementation                                  |
|----------|-----------------------------------------|--------------------------------------------------------|
| **C1 — Collective Benefit**   | Data should provide shared value      | Contextual education layers, ethical Story Nodes       |
| **C2 — Authority to Control** | Communities control data about them   | CARE blocks, MOUs, sovereignty workflows               |
| **C3 — Responsibility**       | Stewards must protect from harm       | Generalization, suppression, audits, access controls   |
| **C4 — Ethics**               | Prioritize rights, protection & context | Cultural protocols, site restrictions, narrative rules |

### CARE Enforcement Mechanisms

- Required **CARE block** for any dataset involving cultural, Indigenous, or sensitive community data.  
- Required **tribal/Indigenous approval workflows** before publication or AI training.  
- Required **governance ledger entry** for sensitive decisions.  
- Required **spatial and narrative generalization** for sensitive sites.  
- Required **narrative validation** for Story Nodes and Focus Mode where CARE applies.

---

## 🧱 FAIR+CARE Metadata Requirements

All datasets MUST contain FAIR+CARE-aligned metadata.

### Core Metadata (FAIR)

~~~json
{
  "id": "unique-id",
  "title": "Human title",
  "provenance": "Source or origin",
  "checksum": "sha256-...",
  "license": "CC-BY-4.0"
}
~~~

### CARE Block (Required for Cultural/Sensitive Data)

~~~json
{
  "care": {
    "status": "approved | revision | restricted",
    "reviewer": "FAIR+CARE Council",
    "authority_to_control": "Tribal/Community Authority",
    "statement": "Ethical review notes",
    "date_reviewed": "2025-11-10"
  }
}
~~~

### Interoperability Fields

At minimum:

- `dcat:accessLevel`  
- `dct:rights`  
- `time:hasBeginning` / `time:hasEnd`  
- `geo:geometry` (generalized if sensitive)  
- `prov:wasGeneratedBy`  
- `schema:creator`  

These fields must be present in STAC/DCAT records and reflected in graph modeling.

---

## 🧬 FAIR+CARE Data Lifecycle

~~~mermaid
flowchart TD
  A["Data Submission"] --> B["FAIR+CARE Validation (CI/CD)"]
  B --> C{"FAIR-compliant?"}
  C -->|No| D["Reject · quarantine registry"]
  C -->|Yes| E["CARE Review (Council + Community)"]
  E --> F{"CARE-safe?"}
  F -->|No| D["Reject · remediation / restricted"]
  F -->|Yes| G["Metadata Enrichment (STAC/DCAT)"]
  G --> H["Publication (Public or Restricted)"]
  H --> I["Telemetry Logging (focus-telemetry.json)"]
~~~

Key lifecycle stages:

1. **Submission** – Data contract and initial metadata registered.  
2. **FAIR Validation** – Structural, schema, and catalog checks.  
3. **CARE Review** – Human + community review when applicable.  
4. **Enrichment** – Ontology-based metadata, STAC/DCAT alignment.  
5. **Publication** – Public, restricted, or internal-only.  
6. **Telemetry & Governance** – FAIR+CARE events recorded for audits.

---

## 🧪 Validation & CI/CD

Validation is structured as a composable pipeline:

| Stage                 | Tool / Workflow              | Output File                                  |
|-----------------------|------------------------------|----------------------------------------------|
| FAIR Metadata         | `faircare-validate.yml`      | `reports/fair/faircare_summary.json`        |
| Sensitive Scan        | PII/Spatial Scan             | `reports/fair/pii_scan.json`                |
| STAC/DCAT Validation  | `stac-validate.yml`          | `reports/self-validation/stac_validation.json` |
| Data Contract Check   | `data-contract-validate.yml` | `reports/self-validation/contract_validation.json` |
| Documentation         | `docs-lint.yml`              | `reports/self-validation/docs_lint_summary.json` |
| Telemetry Export      | `telemetry-export.yml`       | `releases/v11.0.0/focus-telemetry.json`     |

Failure at any stage is a **governance event** and MUST be:

- Logged in the governance ledger, and  
- Addressed (fix, restrict, or reject) before public publication.

---

## 🔐 Governance Ledger Compliance

All FAIR+CARE decisions MUST be logged in:

~~~text
reports/audit/governance-ledger.json
~~~

### Example Ledger Entry

~~~json
{
  "event": "faircare_review",
  "dataset_id": "example_dataset_2025",
  "decision": "approved",
  "reviewer": "FAIR+CARE Council",
  "notes": "No cultural sensitivity identified; standard FAIR publication.",
  "timestamp": "2025-11-20T14:55:00Z"
}
~~~

Ledger entries MUST include:

- Dataset/model ID  
- Decision (`approved`, `revision`, `restricted`, `rejected`)  
- Reviewer or committee identity  
- CARE status and justification where applicable  
- Timestamp and links to underlying reports (FAIR, PII scan, etc.)

---

## 📖 Narrative Governance (Story Nodes & Focus Mode)

FAIR+CARE rules apply directly to:

- **Story Node** narratives and metadata.  
- **Focus Mode** event summaries, overlays, and “context panels”.  
- All spatiotemporal anchors used in narratives.

### Forbidden Narrative Content

- Precise coordinates for **sensitive cultural or sacred sites**.  
- Unreviewed or speculative cultural knowledge.  
- Detailed ritual, ceremonial, or burial information.  
- Use of tribal/community names without approval when flagged.  
- Inference of sacred/burial sites from non-sensitive layers.

### Required Narrative Safeguards

- Use **regional-scale** or generalized spatial language for sensitive content.  
- Include cultural-context disclaimers where appropriate.  
- Show explicit linkage to CARE status (e.g., “Narrative approved under CARE: approved / restricted”).  
- Mask or omit content when CARE status is `restricted` or under review.  

Focus Mode and Story Nodes must read and respect:

- `care.status` and `care.authority_to_control` in dataset metadata.  
- Sovereignty policies defined in `sovereignty/INDIGENOUS-DATA-PROTECTION.md`.  
- Governance decisions recorded in `governance-ledger.json`.

---

## 📊 Audits & Scoring

### Quarterly Audit & Scorecard

Quarterly audits produce:

- FAIR+CARE compliance scores.  
- Trends in dataset compliance.  
- CARE status summaries (approved / revision / restricted).  
- Deviation reports and governance incident logs.

Published to:

~~~text
docs/reports/telemetry/governance_scorecard.json
~~~

### FAIR+CARE Composite Score (FCS v11)

~~~text
FCS = (FAIR_score * 0.7) + (CARE_score * 0.3)
~~~

Where:

- `FAIR_score` ∈ [0, 100] from FAIR validation metrics.  
- `CARE_score` ∈ [0, 100] from CARE governance metrics.

Ranges:

| Score | Label        | Meaning                         |
|-------|--------------|---------------------------------|
| 95–100| ✔ Excellent  | Fully compliant                 |
| 80–94 | ⚙ Strong     | Minor gaps, monitored           |
| 65–79 | ⚠ Review     | Publication delayed pending fix |
| <65   | 🚫 Blocked   | Not eligible for release        |

These scores are surfaced in dashboards and used for governance summaries.

---

## 🧾 Examples

### Example Dataset Metadata (v11 Compliant, Non-Sensitive)

~~~json
{
  "id": "historic_hydrography_1890",
  "title": "Historic Hydrography of Kansas (1890)",
  "provenance": "USGS Archive",
  "license": "Public Domain",
  "checksum": "sha256-aaaabbbbcccc",
  "care": {
    "status": "approved",
    "reviewer": "FAIR+CARE Council",
    "statement": "No cultural sensitivity issues identified.",
    "date_reviewed": "2025-11-15"
  },
  "dcat:accessLevel": "public",
  "prov:wasGeneratedBy": "digitization_pipeline_v3.2"
}
~~~

### Example Dataset Metadata (Culturally Sensitive)

~~~json
{
  "id": "cultural_sites_kansas_1870",
  "title": "Documented Cultural Sites in Kansas (circa 1870)",
  "provenance": "Historical Archives + Community Oral Histories",
  "license": "CC-BY-4.0",
  "checksum": "sha256-ddddeeeeffff",
  "care": {
    "status": "restricted",
    "authority_to_control": "Example Tribal Nation",
    "reviewer": "FAIR+CARE Council",
    "statement": "Contains culturally sensitive location information. Use restricted to approved research contexts.",
    "date_reviewed": "2025-11-18"
  },
  "dcat:accessLevel": "restricted",
  "prov:wasGeneratedBy": "heritage_mapping_pipeline_v2.1"
}
~~~

Such datasets MUST use generalized geometries and narrative constraints per sensitive-site governance.

---

## 🕰️ Version History

| Version | Date       | Author                 | Summary                                                                                                                     |
|--------:|------------|------------------------|-----------------------------------------------------------------------------------------------------------------------------|
| v11.0.0 | 2025-11-20 | KFM Governance Council | Upgraded FAIR+CARE framework for KFM v11; added ontology mappings, narrative governance rules, telemetry v11 integration, and KFM-MDP v11.2.4 compliance. |
| v10.2.2 | 2025-11-12 | A. Barta               | Updated SBOM/manifest references; added DCAT and STAC alignment; extended composite FAIR+CARE scoring.                     |
| v10.0.0 | 2025-11-10 | A. Barta               | Major improvements; added telemetry and governance ledger integration; clarified CARE review flows.                        |
| v9.7.0  | 2025-11-05 | KFM Core Team          | Established authoritative FAIR+CARE baseline for KFM.                                                                       |

---

<div align="center">

⚖️ **Kansas Frontier Matrix — FAIR+CARE Governance Framework (v11.0.0)**  
“Technical integrity × Ethical responsibility.”

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
Master Coder Protocol v6.3 · FAIR+CARE Certified · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[⬅ Back to Standards Index](README.md) ·  
[🏛 Root Governance Charter](governance/ROOT-GOVERNANCE.md) ·  
[📜 Licensing Standard](licensing.md)

</div>
