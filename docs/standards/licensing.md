---
title: "📜 Kansas Frontier Matrix — Licensing & Intellectual Property Standards (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/standards/licensing.md"

version: "v11.0.0"
last_updated: "2025-11-20"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Annual / FAIR+CARE Council & Technical Governance Board"
content_stability: "stable"

commit_sha: "<latest-commit-hash>"
sbom_ref: "releases/v11.0.0/sbom.spdx.json"
manifest_ref: "releases/v11.0.0/manifest.zip"
telemetry_ref: "releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "schemas/telemetry/docs-licensing-v11.json"
energy_schema: "schemas/telemetry/energy-v2.json"
carbon_schema: "schemas/telemetry/carbon-gco2e-v1.json"

governance_ref: "governance/ROOT-GOVERNANCE.md"
ethics_ref: "faircare/FAIRCARE-GUIDE.md"
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
intent: "licensing-standards"

header_profile: "standard"
footer_profile: "standard"
diagram_profiles:
  - "mermaid-flowchart-v1"

scope:
  domain: "licensing"
  applies_to:
    - "all-code"
    - "all-datasets"
    - "all-models"
    - "all-docs"
    - "story-nodes"
    - "focus-mode"

semantic_document_id: "kfm-doc-licensing"
doc_uuid: "urn:kfm:docs:standards:licensing-v11.0.0"
event_source_id: "ledger:kfm:doc:standards:licensing:v11.0.0"
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Medium-Sensitivity"
sensitivity: "General (non-PII; normative governance guidance)"
sensitivity_level: "Low"
public_exposure_risk: "Low"
classification: "Public"
jurisdiction: "Kansas / United States"
indigenous_rights_flag: true
data_steward: "KFM FAIR+CARE Council & Technical Governance Board"
lifecycle_stage: "stable"
ttl_policy: "36 months"
sunset_policy: "Superseded by Licensing Standard v12.0"

provenance_chain:
  - "docs/standards/licensing.md@v10.2.2"
  - "Markdown Protocol Super-Standard.pdf"
  - "KFM Technical Guide v11.pdf"

provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: false

ontology_alignment:
  cidoc: "E30 Right"
  schema_org: "CreativeWork"
  prov_o: "prov:Plan"

metadata_profiles:
  - "SPDX 2.3"
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
  - "a11y-adaptations"
  - "diagram-extraction"
  - "metadata-extraction"
ai_transform_prohibited:
  - "content-alteration"
  - "inventing-compliance-status"
  - "speculative-additions"
  - "unverified-architectural-claims"
  - "narrative-fabrication"
  - "governance-override"

transform_registry:
  allowed:
    - summary
    - timeline-generation
    - semantic-highlighting
    - a11y-adaptations
    - diagram-extraction
    - metadata-extraction
  prohibited:
    - content-alteration
    - inventing-compliance-status
    - speculative-additions
    - unverified-architectural-claims
    - narrative-fabrication
    - governance-override

heading_registry:
  approved_h2:
    - "📘 Overview"
    - "🗂️ Directory Layout"
    - "🧭 Context"
    - "🧱 License Categories"
    - "🧩 SPDX Integration"
    - "📦 Data & Metadata"
    - "🧪 Validation & CI/CD"
    - "⚖ FAIR+CARE & Sovereignty"
    - "📊 Licensing Telemetry"
    - "🕰️ Version History"

test_profiles:
  - "markdown-lint"
  - "schema-lint"
  - "metadata-check"
  - "licensing-check"
  - "provenance-check"
  - "footer-check"
  - "accessibility-check"

ci_integration:
  workflow: ".github/workflows/licensing-governance.yml"
  environment: "dev → staging → production"

branding_registry:
  standard: "Open Licensing × Ethical Stewardship × Sustainable Intelligence"
  telemetry: "Trace Rights · Prove Provenance · Respect Communities"

layout_profiles:
  - "immediate-one-branch-with-descriptions-and-emojis"

badge_profiles:
  - "root-centered-badge-row"

requires_purpose_block: true
requires_directory_layout_section: true
requires_version_history: true
requires_governance_links_in_footer: true

deprecated_fields:
  - "legacy_licensing_standard_v10"
---

<div align="center">

# 📜 **Kansas Frontier Matrix — Licensing & Intellectual Property Standards (v11.0.0)**  
`docs/standards/licensing.md`

**Purpose**  
Define and enforce a unified, FAIR+CARE-aligned, SPDX-compliant licensing framework for **all code, datasets, models, documentation, pipelines, Story Nodes, and Focus Mode outputs** within the Kansas Frontier Matrix (KFM).  
This framework ensures transparent, ethical, reproducible, and legally consistent use of KFM assets under **KFM-MDP v11.2.4** and **Master Coder Protocol (MCP-DL v6.3)**.

[![Docs · MCP v6.3](https://img.shields.io/badge/Docs-MCP_v6.3-blue)]() ·
[![KFM-MDP v11.2.4](https://img.shields.io/badge/KFM%E2%80%93MDP-v11.2.4-purple)]() ·
[![Licensing · SPDX 2.3](https://img.shields.io/badge/Licensing-SPDX_2.3-informational)]() ·
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Aligned-gold)]()

</div>

---

## 📘 Overview

Licensing is a core governance function of KFM v11.

The licensing system aims to:

- Ensure **open science** and public transparency where possible.  
- Protect **Indigenous sovereignty & cultural rights** where required.  
- Maintain legal clarity for all code/data/model reuse.  
- Guarantee provenance, attribution, and reproducibility.  
- Integrate licensing into **SBOMs**, **manifests**, **telemetry**, and **CI/CD**.  

Every KFM asset MUST declare a license using:

- **SPDX identifiers**,  
- **YAML front-matter license fields** (for docs & configs), and  
- **SBOM / manifest / STAC / DCAT** license fields.  

---

## 🗂️ Directory Layout

~~~text
📂 KansasFrontierMatrix/
└── 📂 docs/
    ├── 📂 standards/
    │   ├── 📄 README.md                        # Standards index
    │   ├── 📄 licensing.md                     # 📜 Licensing & IP Standards (this file)
    │   ├── 📄 telemetry_standards.md           # 📈 Telemetry Super-Standard
    │   ├── 📄 ui_accessibility.md              # ♿ UI Accessibility & Inclusion Super-Standard
    │   ├── 📄 kfm_markdown_protocol_v11.2.4.md # 📑 Markdown Authoring Protocol
    │   ├── 📂 governance/
    │   │   ├── 📄 README.md                    # 🏛️ Governance & Ethical Oversight Framework
    │   │   └── 📄 ROOT-GOVERNANCE.md           # 🏛️ Root Governance Charter
    │   ├── 📂 faircare/
    │   │   └── 📄 FAIRCARE-GUIDE.md            # ⚖ FAIR+CARE Governance Guide
    │   └── 📂 sovereignty/
    │       └── 📄 INDIGENOUS-DATA-PROTECTION.md # 🪶 Indigenous Data Protection Policy
    └── 📄 glossary.md                          # Shared vocabulary (including licensing terms)
~~~

**Author rules**

- This file is the **root licensing standard** for the monorepo.  
- Any asset-specific licensing guides (e.g., for models or third-party datasets) MUST:
  - Live in `docs/standards/` or an appropriate subfolder.  
  - Reference this document in a “Related Standards” section.  
- All new standards in `docs/standards/` MUST specify an SPDX `license` in front-matter and comply with this standard.

---

## 🧭 Context

Licensing is tightly integrated with other KFM standards:

- **Governance & FAIR+CARE**  
  - `governance/ROOT-GOVERNANCE.md` defines who can approve licensing exceptions or CARE overrides.  
  - `faircare/FAIRCARE-GUIDE.md` explains how community rights and cultural sensitivity intersect with legal licenses.

- **Telemetry & SBOMs**  
  - `telemetry_standards.md` defines licensing telemetry—how compliance metrics appear in dashboards and `focus-telemetry.json`.  
  - `releases/v11.0.0/sbom.spdx.json` encapsulates component-level SPDX data.

- **Markdown & Documentation**  
  - `kfm_markdown_protocol_v11.2.4.md` requires docs to declare `license` in YAML front-matter and to present standardized attribution in footers.

Licensing decisions must therefore be:

- **Machine-readable** (SPDX + JSON-based catalogs),  
- **Graph-compatible** (CIDOC E30 Right, PROV-O Plan), and  
- **Narratively transparent** for Story Nodes and Focus Mode.

---

## 🧱 License Categories

KFM v11 uses a **unified licensing framework** per asset type:

| Asset Type                  | Default License                | Notes                                                                                 |
|-----------------------------|--------------------------------|---------------------------------------------------------------------------------------|
| **Code & Scripts**          | `MIT`                          | Permissive, CI-safe, widely compatible                                                |
| **Documentation**           | `CC-BY-4.0`                    | Attribution required; derivatives allowed                                             |
| **Datasets**                | `CC-BY-4.0` or `CC0-1.0`      | CARE overrides apply for culturally sensitive content                                 |
| **AI Models / Weights**     | `CC-BY-SA-4.0`                 | Ensures derivative models remain open                                                |
| **Governance Documents**    | `CC-BY-4.0`                    | Public transparency required                                                          |
| **Sensitive Cultural Data** | CARE-governed + `CC-BY-NC-4.0` or stricter | Community & sovereignty controls override defaults                      |

**CARE and sovereignty constraints ALWAYS override permissive licenses.**  
A license that appears open (e.g., CC-BY-4.0) MAY have CARE-based restrictions layered on top.

---

## 🧩 SPDX Integration

Every licensed asset MUST use **SPDX-compliant identifiers**.

| SPDX ID         | Use Case                       |
|-----------------|--------------------------------|
| `MIT`           | Source code, scripts           |
| `CC-BY-4.0`     | Docs, datasets                 |
| `CC-BY-SA-4.0`  | AI models                      |
| `CC0-1.0`       | Fully open datasets            |
| `ODbL-1.0`      | Databases                      |
| `Public-Domain` | Public-domain U.S. datasets    |

### Example: SBOM Component Entry

~~~json
{
  "name": "kfm-mltrainer",
  "version": "v11.0.0",
  "license": "MIT",
  "licenseFile": "LICENSE"
}
~~~

### YAML Front-Matter Example (Doc)

~~~yaml
license: "CC-BY 4.0"
spdx_license_id: "CC-BY-4.0"
attribution: "© 2025 Kansas Frontier Matrix"
~~~

SPDX IDs MUST be present wherever feasible:

- SBOM components,  
- STAC / DCAT dataset descriptors,  
- Model cards,  
- Data contracts,  
- YAML front-matter for standards and guides.

---

## 📦 Data & Metadata

### Dataset Licensing Fields (Data Contracts)

~~~json
{
  "license": "CC-BY-4.0",
  "spdx_license_id": "CC-BY-4.0",
  "provenance": "NOAA NCEI",
  "license_text": "Creative Commons Attribution 4.0 International",
  "attribution": "Data courtesy of NOAA & Kansas Frontier Matrix"
}
~~~

### STAC / DCAT Licensing Fields

~~~json
{
  "dct:license": "CC-BY-4.0",
  "dct:rights": "Freely available with attribution.",
  "dcat:accessLevel": "public"
}
~~~

### CARE Overrides (If Sensitive)

~~~json
{
  "license": "CC-BY-4.0",
  "care": {
    "status": "restricted",
    "authority_to_control": "Example Tribal Nation",
    "statement": "Dataset contains sensitive cultural knowledge.",
    "reviewer": "FAIR+CARE Council",
    "review_date": "2025-11-12"
  }
}
~~~

In the graph, licensing becomes a **Right** (CIDOC `E30 Right`) linked to:

- The dataset or model entity,  
- The issuing authority,  
- CARE and sovereignty policies.

---

## 🧪 Validation & CI/CD

Licensing is enforced via CI/CD workflows and telemetry.

~~~mermaid
flowchart TD
  A["Asset Created or Modified"] --> B["SPDX Validation (licensing-check.yml)"]
  B --> C["STAC/DCAT License Check (stac-validate.yml)"]
  C --> D["Docs Badge/Footer Check (docs-lint.yml)"]
  D --> E["SBOM Compilation (build-sbom.yml)"]
  E --> F["Telemetry Export → focus-telemetry.json"]
  F --> G["Provenance Ledger Append"]
~~~

**Outputs stored in:**

- `reports/fair/faircare_summary.json`  
- `reports/self-validation/stac_validation.json`  
- `reports/self-validation/docs/lint_summary.json`  
- `releases/v11.0.0/focus-telemetry.json`  
- `releases/v11.0.0/sbom.spdx.json`  
- `reports/audit/github-workflows-ledger.json`  

Any failure in licensing checks MUST block merge or release unless explicitly waived via a documented governance decision.

---

## ⚖ FAIR+CARE & Sovereignty

Licensing is not only legal but ethical:

- CARE rules may **tighten** usage beyond legal license text through:
  - Restricted redistribution,  
  - Required community review,  
  - Masking or generalizing locations,  
  - Conditional attribution,  
  - Publication limitations,  
  - AI model training prohibitions.

Example CARE + License combination:

~~~json
{
  "license": "CC-BY-4.0",
  "care": {
    "status": "restricted",
    "authority_to_control": "Example Tribal Nation",
    "statement": "Dataset contains sacred site information. Use limited to agreed contexts.",
    "review_date": "2025-11-12"
  }
}
~~~

Focus Mode and Story Nodes MUST respect:

- CARE flags,  
- Sovereignty policy (`sovereignty/INDIGENOUS-DATA-PROTECTION.md`),  
- Licensing terms when generating narrative overlays.

No AI or UI feature may present data in a way that violates these combined constraints.

---

## 📊 Licensing Telemetry

Licensing telemetry is written into `focus-telemetry.json` and related reports.

Tracked metrics include:

- % of assets with valid SPDX IDs.  
- % of assets missing license fields (by type).  
- Ratio of open vs restricted datasets.  
- Count of CARE overrides per asset type.  
- Model licensing consistency (e.g., all model variants aligned).  
- Attribution completeness (number of docs or datasets missing attribution).

Example telemetry entry:

~~~json
{
  "event_type": "governance",
  "category": "licensing",
  "status": "success",
  "timestamp": "2025-11-20T18:00:00Z",
  "payload": {
    "total_assets_scanned": 842,
    "spdx_compliant_assets": 832,
    "missing_license_fields": 10,
    "care_restricted_assets": 17,
    "open_datasets": 210
  },
  "context": {
    "release": "v11.0.0",
    "workflow": "licensing-governance.yml"
  }
}
~~~

Governance dashboards use these metrics to:

- Highlight areas of licensing risk,  
- Track progress toward complete SPDX coverage,  
- Monitor CARE overrides and restricted datasets.

---

## 🕰️ Version History

| Version | Date       | Author                 | Summary                                                                                                                                     |
|--------:|------------|------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| v11.0.0 | 2025-11-20 | KFM Governance Council | Upgraded to KFM-MDP v11.2.4; integrated FAIR+CARE, CIDOC CRM, DCAT/STAC alignment, SBOM v11, telemetry v11, and expanded ethical licensing rules. |
| v10.2.2 | 2025-11-12 | A. Barta               | Updated SBOM & manifest references; added CARE metadata guidance and clarified dataset licensing fields.                                   |
| v10.0.0 | 2025-11-10 | A. Barta               | Added licensing telemetry and CI/CD integration; defined initial SPDX profiles for code, docs, datasets, and models.                       |
| v9.7.0  | 2025-11-05 | KFM Core & Governance  | Unified licensing policy baseline across code, data, and documentation; introduced governance hooks.                                      |

---

<div align="center">

📜 **Kansas Frontier Matrix — Licensing & Intellectual Property Standards (v11.0.0)**  
“Open by default. Ethical always.”

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
Master Coder Protocol v6.3 · FAIR+CARE Certified · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[⬅ Back to Standards Index](README.md) · [🏛 Root Governance Charter](governance/ROOT-GOVERNANCE.md) · [⚖ FAIR+CARE Guide](faircare/FAIRCARE-GUIDE.md)

</div>
