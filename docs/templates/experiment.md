---
title: "🧪 Kansas Frontier Matrix — Experiment Documentation Template (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/templates/experiment.md"

version: "v11.2.4"
last_updated: "2025-12-06"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly / Autonomous"
content_stability: "stable"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
signature_ref: "releases/v11.2.4/signature.sig"
attestation_ref: "releases/v11.2.4/slsa-attestation.json"
sbom_ref: "releases/v11.2.4/sbom.spdx.json"
manifest_ref: "releases/v11.2.4/manifest.zip"
telemetry_ref: "releases/v11.2.4/docs-experiment-template-telemetry.json"
telemetry_schema: "schemas/telemetry/docs-experiment-template-v11.2.4.json"
energy_schema: "schemas/telemetry/energy-v2.json"
carbon_schema: "schemas/telemetry/carbon-v2.json"

governance_ref: "../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.4"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

status: "Active / Enforced"
doc_kind: "Guide"
header_profile: "standard"
footer_profile: "standard"
diagram_profiles:
  - "mermaid-flowchart-v1"
  - "mermaid-timeline-v1"

scope:
  domain: "experiment-templates"
  applies_to:
    - "docs/experiments/**"
    - "mcp/experiments/**"

fair_category: "F1-A1-I2-R2"
care_label: "FAIR+CARE Governance Aligned"
sensitivity: "General (non-sensitive; auto-mask rules apply)"
sensitivity_level: "None"
public_exposure_risk: "Low"
classification: "Public"
jurisdiction: "Kansas / United States"
indigenous_rights_flag: true
data_steward: "KFM FAIR+CARE Council"

ttl_policy: "24 months"
sunset_policy: "Superseded by Experiment Documentation Template v12"

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
  - "docs/templates/experiment.md@v10.2.2"
  - "docs/templates/experiment.md@v10.0.0"
  - "docs/templates/experiment.md@v9.7.0"
  - "docs/templates/experiment.md@v9.5.0"
  - "docs/templates/experiment.md@v9.0.0"

provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: true

json_schema_ref: "schemas/json/kfm-markdown-protocol-v11.2.4.schema.json"
shape_schema_ref: "schemas/shacl/kfm-markdown-protocol-v11.2.4-shape.ttl"
story_node_refs: []

immutability_status: "version-pinned"
doc_uuid: "urn:kfm:doc:templates:experiment:v11.2.4"
semantic_document_id: "kfm-experiment-template-v11.2.4"
event_source_id: "ledger:kfm:doc:templates:experiment:v11.2.4"
doc_integrity_checksum: "<sha256>"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summary"
  - "timeline-generation"
  - "semantic-highlighting"
  - "3d-context-render"
  - "a11y-adaptations"
  - "diagram-extraction"
  - "metadata-extraction"
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
    - "3d-context-render"
    - "a11y-adaptations"
    - "diagram-extraction"
    - "metadata-extraction"
  prohibited:
    - "content-alteration"
    - "speculative-additions"
    - "unverified-architectural-claims"
    - "narrative-fabrication"
    - "governance-override"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

heading_registry:
  approved_h2:
    - "📘 Overview"
    - "🗂️ Directory Layout"
    - "🧭 Context"
    - "🗺️ Diagrams"
    - "🧠 Story Node & Focus Mode Integration"
    - "🧪 Validation & CI/CD"
    - "📦 Data & Metadata"
    - "🌐 STAC, DCAT & PROV Alignment"
    - "🧱 Architecture"
    - "⚖ FAIR+CARE & Governance"
    - "🕰️ Version History"

test_profiles:
  - "markdown-lint"
  - "schema-lint"
  - "metadata-check"
  - "diagram-check"
  - "accessibility-check"
  - "provenance-check"
  - "footer-check"

ci_integration:
  workflow: ".github/workflows/docs-lint.yml"
  environment: "dev → staging → production"

branding_registry:
  standard: "Scientific Insight × FAIR+CARE Ethics × Sustainable Intelligence"
  architecture: "Designed for Longevity · Governed for Integrity"
  analysis: "Research-Driven · Evidence-Led · FAIR+CARE Grounded"
  data-spec: "Open Data × Responsible Stewardship"
  pipeline: "Deterministic Pipelines · Explainable AI · Open Provenance"
  telemetry: "Transparent Systems · Ethical Metrics · Sustainable Intelligence"
  graph: "Semantics × Provenance × Spatial Intelligence"

layout_profiles:
  - "immediate-one-branch-with-descriptions-and-emojis"

badge_profiles:
  - "root-centered-badge-row"

requires_purpose_block: true
requires_directory_layout_section: true
requires_version_history: true
requires_governance_links_in_footer: true

deprecated_fields:
  - "old_markdown_standard_v10.4"
---

<div align="center">

# 🧪 **Kansas Frontier Matrix — Experiment Documentation Template**  
`docs/templates/experiment.md`

**Purpose**  
Provide a **strict, fully governed, machine‑validated experiment template** for documenting **ETL, AI/ML, geospatial processing, historical analysis, and validation experiments** within the Kansas Frontier Matrix (KFM).  
Aligned with **MCP‑DL v6.3**, **KFM‑MDP v11.2.4**, **Diamond⁹ Ω / Crown∞Ω**, **FAIR+CARE**, **ISO 19115**, and **STAC/DCAT/PROV**.

<img src="https://img.shields.io/badge/Docs-MCP_v6.3-blue" />
<img src="https://img.shields.io/badge/KFM--MDP-v11.2.4-purple" />
<img src="https://img.shields.io/badge/License-CC--BY%204.0-green" />
<img src="https://img.shields.io/badge/FAIR%2BCARE-Certified-orange" />
<img src="https://img.shields.io/badge/Status-Template-lightgrey" />

</div>

---

## 📘 Overview

Use this template to document any **experiment** that affects KFM datasets, workflows, AI pipelines, or governance systems.

All experiment docs:

- Must pass **docs-lint**, **FAIR+CARE audit**, and **telemetry export**.  
- Must follow **strict YAML front‑matter**, **emoji section headers**, and **one‑mermaid‑per‑section** guardrails.  
- Are registered in the **Governance Ledger** with provenance and checksum linkage.  
- Are used for **Focus Mode** narrative citations and STAC/DCAT/PROV linking.  
- Must maintain **fully reproducible, ethical, and transparent scientific practice**.

**Storage pattern for concrete experiments:**

~~~text
docs/experiments/<domain>/<experiment-name>.md
~~~

Recommended domain examples: `etl`, `ai`, `geospatial`, `history`, `archaeology`, `ci-cd`.

---

## 🗂️ Directory Layout

Use this section as a guide when placing a new experiment document.

~~~text
📁 docs/
└── 📁 experiments/
    📁 <domain>/
        📄 <experiment-name>.md          — Experiment documented using this template

📁 mcp/
└── 📁 experiments/
    📄 <experiment-id>.json             — (Optional) machine-readable experiment metadata

📁 reports/
└── 📁 experiments/
    📁 logs/
    📁 figures/
    📁 summaries/

📁 releases/
└── 📁 vX.Y.Z/
    📄 focus-telemetry.json             — Telemetry including experiment events
    📄 manifest.zip                     — Manifests & checksums
    📄 sbom.spdx.json                   — SBOM for experiment/tooling environment
~~~

When instantiating this template:

- Update paths to reflect the **actual domain and experiment name**.  
- Ensure **reports/** and **releases/** references match the release/version you are working under.

---

## 🧭 Context

### 1. When to Use This Template

Use this template whenever you:

- Run a **non-trivial experiment** that influences KFM data, AI models, or governance policies.  
- Need **reproducibility** (others must be able to re‑run your work).  
- Intend results to be referenced by **Story Nodes**, **Focus Mode**, or **governance reviews**.

Typical experiment categories:

- ETL / normalization pipelines.  
- AI training / fine‑tuning / evaluation.  
- Geospatial analysis (e.g., LiDAR + GLO).  
- Historical or archival text extraction and NER.  
- CI/CD or governance mechanism experiments.

### 2. Section Map (for Authors)

Concrete experiment docs created from this template typically map content as:

- **Objective** → why the experiment exists and what you expect.  
- **Methodology** → data, tools, pipelines, environment.  
- **Results** → metrics, derived datasets, figures.  
- **Discussion** → interpretation, limitations, next steps.  
- **FAIR+CARE Validation** → ethics and provenance outcomes.  
- **Reproducibility** → exact instructions and configs.  
- **Outputs & Storage** → where artifacts live and how they are referenced.  

---

## 🗺️ Diagrams

Use this section for **optional** mermaid diagrams in concrete experiment docs.  
The template itself provides an example that authors may copy and adapt.

### 1. Example Experiment Flow

~~~mermaid
flowchart TD
    A["Raw Data (Ingest)"] --> B["ETL / Preprocessing"]
    B --> C["Experiment Logic (Model / Analysis)"]
    C --> D["Validation & Metrics"]
    D --> E["Artifacts & Telemetry Export"]
~~~

**Author rules:**

- At most **one mermaid diagram per section**.  
- Use clear labels that match your experiment’s terminology.  
- Summarize the key point of the diagram in surrounding text.

---

## 🧠 Story Node & Focus Mode Integration

Concrete experiment docs may be referenced as Story Nodes such as:

- `urn:kfm:story-node:experiment:<experiment-id>`  
- `urn:kfm:story-node:experiment-trend:<domain>:<period>`

When writing an experiment:

- Use **clear, localized sections** so Focus Mode can surface targeted answers (Objective, Method, Results, Governance).  
- Include **stable identifiers** in the text (experiment IDs, dataset IDs, model IDs).  
- Reference relevant STAC Collections, model cards, and SOPs via links.

Focus Mode:

- **MAY** summarize experiment docs, highlight metrics, and show links to results.  
- **MUST NOT** invent results or governance outcomes that are not present in the document.  

---

## 📦 Data & Metadata

### 1. Metadata (YAML Front‑Matter – Required)

Every experiment doc must begin with a YAML block derived from this pattern:

~~~yaml
---
title: "🧪 [Experiment Title]"
path: "docs/experiments/[domain]/[filename].md"
version: "vX.Y.Z"
last_updated: "YYYY-MM-DD"
review_cycle: "Quarterly / Autonomous"
commit_sha: "<commit-hash>"

sbom_ref: "releases/vX.Y.Z/sbom.spdx.json"
manifest_ref: "releases/vX.Y.Z/manifest.zip"
telemetry_ref: "releases/vX.Y.Z/focus-telemetry.json"
telemetry_schema: "schemas/telemetry/docs-experiment-template-v11.2.4.json"

governance_ref: "docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
---
~~~

> **Missing or malformed required fields will fail `docs-lint.yml` and block merge.**

Authors may extend front‑matter with experiment‑specific keys (e.g., `experiment_id`, `domain`, `status`) as long as they remain valid YAML.

### 2. Configuration & Parameters

Concrete experiment docs should capture key parameters in a table:

| Parameter         | Description          | Value / Example                         |
|-------------------|----------------------|-----------------------------------------|
| `epochs`          | Training iterations  | `20`                                    |
| `learning_rate`   | Optimizer step       | `5e-4`                                  |
| `bbox`            | Spatial extent       | `[-102.05, 37.00, -94.60, 40.00]`      |
| `temporal_range`  | Time coverage        | `1950–2025`                             |
| `ocr_model`       | OCR engine & version | `tesseract-5.3.2`                       |

Include references to any manifest files, such as:

~~~text
data/checksums/manifest.json
data/sources/*_source_metadata.json
~~~

---

## 🧱 Architecture

### 1. Objective (Author-Filled)

In concrete docs, use an **“Objective”** subsection to describe:

- The **purpose** of the experiment.  
- The **hypothesis** being tested.  
- The **expected outcomes** or decision criteria.

Example narrative:

> Assess viability of using multi‑temporal NDVI derivatives to detect prairie restoration zones and rank restoration opportunities.

### 2. Methodology (Author-Filled)

Methodology should enumerate:

| Component         | Description                                                |
|-------------------|------------------------------------------------------------|
| Data Sources      | e.g., NOAA, USGS 3DEP, MODIS/VIIRS, KHS, NARA             |
| Transform Pipeline| ETL steps, scripts, staging paths                         |
| Models            | AI model versions, architectures, configs                 |
| Tools             | Python, GDAL, PyTorch, spaCy, Neo4j, Cesium, QGIS        |
| Environment       | Docker tag, image digest, GPU model, RAM, OS, region     |

Example commands (adapt to your experiment):

~~~bash
python src/pipelines/etl/landsat_ingest.py --year 1995 --bbox kansas
python src/ai/train_focus_v2.py --epochs 25 --config configs/ai/focus_v2.yaml
~~~

---

## 🧪 Validation & CI/CD

Every experiment document is part of the CI/CD surface and must integrate with the following workflows:

| Workflow                | Purpose                                            |
|-------------------------|----------------------------------------------------|
| `docs-lint.yml`         | YAML, headings, links, diagrams, layout checks     |
| `faircare-validate.yml` | Ethics, FAIR+CARE alignment, PII / sensitive scan |
| `stac-validate.yml`     | STAC/DCAT validation (if experiment emits STAC)    |
| `telemetry-export.yml`  | Aggregates experiment metrics into telemetry       |

Concrete docs should describe **what passed** and **what failed** where relevant, and may link to:

~~~text
reports/self-validation/docs/lint_summary.json
reports/faircare/faircare_summary.json
reports/self-validation/stac/stac_validation.json
releases/vX.Y.Z/focus-telemetry.json
~~~

---

## 🌐 STAC, DCAT & PROV Alignment

Experiments often produce new assets or change metadata:

- If the experiment generates STAC Items/Collections:
  - Link directly to affected `data/stac/**` objects.  
  - Note any changes in `license`, `extent`, `providers`, or `kfm:care_tag`.  

- If DCAT records are updated:
  - Reference any affected dataset records or catalogs.  

For provenance:

- Treat the experiment doc as a `prov:Entity` describing a `prov:Activity` (the experiment run).  
- Data products mentioned should be linked using `prov:wasGeneratedBy` and `prov:used` in the PROV representation (outside this Markdown, e.g., in JSON‑LD or graph loaders).

---

## ⚖ FAIR+CARE & Governance

Concrete experiment docs must include a **FAIR+CARE Validation** subsection similar to:

| Principle        | Evidence / Notes                                                              |
|------------------|-------------------------------------------------------------------------------|
| **Findable**     | STAC Item created; DOIs or stable IDs issued; catalog entries updated        |
| **Accessible**   | License clarity (e.g., CC‑BY); accessible formats; alt‑text for key figures  |
| **Interoperable**| ISO 19115 metadata; STAC/DCAT alignment; standard CRS & units                |
| **Reusable**     | Versioned scripts; SBOM; checksums; clear limitations & assumptions          |
| **CARE**         | Cultural sensitivity review; Indigenous land checks; no harmful disclosures  |

Relevant reports to reference:

~~~text
reports/faircare/faircare_summary.json
reports/audit/data_provenance_ledger.json
~~~

If an experiment touches sensitive topics or data:

- Explicitly note **governance decisions** (e.g., redaction, generalization, access controls).  
- Reference any relevant SOPs or governance standards used.

---

## 🕰️ Version History

| Version    | Date       | Author        | Summary                                                                                                         |
|-----------:|------------|---------------|-----------------------------------------------------------------------------------------------------------------|
| **v11.2.4** | 2025-12-06 | `@kfm-docs`   | Updated to KFM‑MDP v11.2.4; added full front‑matter metadata, directory layout, Story Node guidance, STAC/DCAT/PROV alignment, and explicit CI/CD integration. |
| v10.2.2   | 2025-11-12 | `@kfm-docs`   | Aligned refs to v10.2.0; enforced strict markdown protocol; added governance + telemetry rules.                |
| v10.0.0   | 2025-11-10 | `@kfm-docs`   | Introduced telemetry schema v2; ensured MCP/FAIR+CARE compliance.                                              |
| v9.7.0    | 2025-11-05 | `@kfm-docs`   | Standardized experiment template into shared docs/templates.                                                   |
| v9.5.0    | 2025-10-20 | `@kfm-docs`   | Added FAIR+CARE & telemetry hooks; linked to governance workflows.                                             |
| v9.0.0    | 2025-06-01 | `@kfm-core`   | Initial experiment documentation template for KFM.                                                              |

---

<div align="center">

🧪 **Kansas Frontier Matrix — Experiment Documentation Template (v11.2.4)**  
Reproducible Experiments · FAIR+CARE Governance · Scientific & Historical Integrity  

[⬅ Back to Templates Index](README.md) ·  
[📘 Markdown Protocol (KFM‑MDP v11.2.4)](../standards/kfm_markdown_protocol_v11.2.4.md) ·  
[⚖ Governance Charter](../standards/governance/ROOT-GOVERNANCE.md)

</div>
