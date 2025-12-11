---
title: "🧪 Kansas Frontier Matrix — Experiment Documentation Template (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/templates/experiment.md"

version: "v11.2.6"
last_updated: "2025-12-11"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly / Autonomous"
content_stability: "stable"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
signature_ref: "../../releases/v11.2.6/signature.sig"
attestation_ref: "../../releases/v11.2.6/slsa-attestation.json"
sbom_ref: "../../releases/v11.2.6/sbom.spdx.json"
manifest_ref: "../../releases/v11.2.6/manifest.zip"
telemetry_ref: "../../releases/v11.2.6/docs-experiment-template-telemetry.json"
telemetry_schema: "../../schemas/telemetry/docs-experiment-template-v11.2.6.json"
energy_schema: "../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../schemas/telemetry/carbon-v2.json"

governance_ref: "../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
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
  - "docs/templates/experiment.md@v11.2.4"
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

json_schema_ref: "../../schemas/json/kfm-markdown-protocol-v11.2.6.schema.json"
shape_schema_ref: "../../schemas/shacl/kfm-markdown-protocol-v11.2.6-shape.ttl"
story_node_refs: []

immutability_status: "version-pinned"
doc_uuid: "urn:kfm:doc:templates:experiment:v11.2.6"
semantic_document_id: "kfm-experiment-template-v11.2.6"
event_source_id: "ledger:kfm:doc:templates:experiment:v11.2.6"
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
Provide a **strict, fully governed, machine-validated experiment template** for documenting **ETL, AI/ML, geospatial processing, historical analysis, and validation experiments** within the Kansas Frontier Matrix (KFM).  
Aligned with **MCP‑DL v6.3**, **KFM‑MDP v11.2.6**, **Diamond⁹ Ω / Crown∞Ω**, **FAIR+CARE**, and STAC/DCAT/PROV‑aware provenance.

[![Docs · MCP v6.3](https://img.shields.io/badge/Docs-MCP_v6.3-blue)]()  
[![KFM‑MDP v11.2.6](https://img.shields.io/badge/KFM%E2%80%93MDP-v11.2.6-purple)]()  
[![License · CC‑BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-green)]()  
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Governance%20Aligned-orange)]()  
[![Status · Template](https://img.shields.io/badge/Status-Template-lightgrey)]()

</div>

---

## 📘 Overview

Use this template to document any **experiment** that affects KFM datasets, workflows, AI pipelines, or governance systems.

Experiment docs produced from this template:

- Must pass **docs-lint**, FAIR+CARE validation, and telemetry export gates.  
- Must follow **strict YAML front-matter**, **emoji section headers**, and KFM‑MDP v11.2.6 layout rules.  
- Are registered in the **governance and provenance ledgers** with checksums.  
- Are used for **Focus Mode** narrative citations and STAC/DCAT/PROV linking.  
- Must maintain **fully reproducible, ethical, and transparent scientific practice**.

Concrete experiment docs are usually stored as:

~~~text
docs/experiments/<domain>/<experiment-name>.md
~~~

Recommended domains: `etl`, `ai`, `geospatial`, `history`, `archaeology`, `ci-cd`.

---

## 🗂️ Directory Layout

Use this section as a guide when placing a new experiment document.

~~~text
📁 docs/
  📁 experiments/
    📁 <domain>/
      📄 <experiment-name>.md      # Experiment documented using this template

📁 mcp/
  📁 experiments/
    🧾 <experiment-id>.json       # (Optional) machine-readable experiment metadata

📁 reports/
  📁 experiments/
    📁 logs/
    📁 figures/
    📁 summaries/

📁 releases/
  📁 vX.Y.Z/
    🧾 focus-telemetry.json       # Telemetry including experiment events
    🧾 manifest.zip               # Manifests & checksums
    🧾 sbom.spdx.json             # SBOM for experiment/tooling environment
~~~

When instantiating this template:

- Update paths to reflect the **actual domain and experiment name**.  
- Ensure `reports/` and `releases/` references match the release/version used by the experiment.

---

## 🧭 Context

### 1. When to Use This Template

Use this template whenever you:

- Run a **non-trivial experiment** that influences KFM data, AI models, narratives, or governance policies.  
- Need **reproducibility** so other contributors (or future you) can re-run the work.  
- Intend results to be referenced by **Story Nodes**, **Focus Mode**, or governance reviews.

Typical experiment categories:

- ETL / normalization pipelines.  
- AI training / fine-tuning / evaluation.  
- Geospatial analysis (e.g., LiDAR, land cover, hydrology).  
- Historical or archival text extraction and NER.  
- CI/CD, reliability, or governance mechanism experiments.

### 2. Section Map (for Authors)

Concrete experiment docs created from this template typically map content as:

- **Objective** → why the experiment exists and what you expect.  
- **Methodology** → data, tools, pipelines, environment.  
- **Results** → metrics, derived datasets, figures.  
- **Discussion** → interpretation, limitations, and next steps.  
- **FAIR+CARE Validation** → ethics and provenance outcomes.  
- **Reproducibility** → exact instructions and configs.  
- **Outputs & Storage** → where artifacts live and how they are referenced.

---

## 🧱 Architecture

Experiment docs must explain how the experiment fits into the KFM pipeline:

> Deterministic ETL → STAC/DCAT/PROV catalogs → Neo4j → API → React/MapLibre/Cesium → Story Nodes → Focus Mode

In your concrete experiment:

- Describe which **ETL pipelines** (`src/pipelines/...`) are involved.  
- Note which **catalogs** (`data/stac/`, `data/*/dcat/`, `data/*/dcat-prov/`) produce or consume experiment outputs.  
- Identify which **graph entities** are affected (e.g., `:Dataset`, `:RasterLayer`, `:HistoricalEvent`, `:ModelRun`).  
- Clarify which **APIs** and **UI components** will rely on the experiment’s results.

### Objective (Author-Filled in Concrete Docs)

Use an **Objective** subsection to describe:

- The **purpose** of the experiment.  
- The **hypothesis** being tested.  
- The **expected outcomes** or decision criteria.

Example snippet:

> Assess viability of using multi-temporal NDVI derivatives to detect prairie restoration zones and rank restoration opportunities.

### Methodology (Author-Filled in Concrete Docs)

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

## 📦 Data & Metadata

### 1. YAML Front-Matter (Required Pattern)

Every experiment doc MUST begin with a YAML block derived from this pattern (also see `kfm-markdown-template.md`):

~~~yaml
---
title: "🧪 [Experiment Title]"
path: "docs/experiments/[domain]/[filename].md"
version: "vX.Y.Z"
last_updated: "YYYY-MM-DD"

release_stage: "Draft / Experimental / Stable / Historical"
lifecycle: "Incubation / LTS / Archive"
review_cycle: "Quarterly / Autonomous"
content_stability: "evolving / stable / frozen"

status: "Active / Deprecated / Historical Record"
doc_kind: "Experiment"
header_profile: "standard"
footer_profile: "standard"

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

commit_sha: "<commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

semantic_document_id: "<kfm-experiment-*-vX.Y.Z>"
doc_uuid: "<urn:kfm:doc:experiment:...:vX.Y.Z>"
event_source_id: "ledger:docs/experiments/[domain]/[filename].md"
immutability_status: "version-pinned"

sbom_ref: "releases/vX.Y.Z/sbom.spdx.json"
manifest_ref: "releases/vX.Y.Z/manifest.zip"
telemetry_ref: "releases/vX.Y.Z/focus-telemetry.json"
telemetry_schema: "schemas/telemetry/docs-experiment-template-v11.2.6.json"

governance_ref: "docs/standards/governance/ROOT-GOVERNANCE.md"
---
~~~

Missing or malformed required fields will fail `docs-lint.yml` and block merge.

### 2. Configuration & Parameters

Concrete experiment docs should capture key parameters in a small table:

| Parameter         | Description          | Value / Example                         |
|-------------------|----------------------|-----------------------------------------|
| `epochs`          | Training iterations  | `20`                                    |
| `learning_rate`   | Optimizer step       | `5e-4`                                  |
| `bbox`            | Spatial extent       | `[-102.05, 37.00, -94.60, 40.00]`      |
| `temporal_range`  | Time coverage        | `1950–2025`                             |
| `ocr_model`       | OCR engine & version | `tesseract-5.3.2`                       |

Reference any manifest or checksum files used, such as:

~~~text
data/checksums/manifest.json
data/sources/*_source_metadata.json
~~~

---

## 🌐 STAC, DCAT & PROV Alignment

Experiments often produce or alter cataloged assets:

- If the experiment generates STAC Items/Collections:
  - Link to affected `data/stac/**` objects.  
  - Note changes in `license`, `extent`, `providers`, or sensitivity tags.  

- If DCAT records are updated:
  - Reference updated dataset records or catalogs (paths under `data/*/dcat/`).  

Provenance expectations:

- Treat the experiment as:
  - `prov:Activity` — the run itself.  
  - `prov:Entity` — this documentation plus produced datasets/models.  
  - `prov:Agent` — the team, automation, or services involved.

Concrete PROV representation (JSON‑LD or graph) should use:

- `prov:wasGeneratedBy` for new/updated datasets.  
- `prov:used` for input entities.  
- `prov:wasDerivedFrom` when updating or refining existing assets.

---

## 🧠 Story Node & Focus Mode Integration

Concrete experiment docs may underpin Story Nodes like:

- `urn:kfm:story-node:experiment:<experiment-id>`  
- `urn:kfm:story-node:experiment-trend:<domain>:<period>`

When writing an experiment:

- Use **clear, localized sections** so Focus Mode can surface targeted answers (Objective, Method, Results, Governance).  
- Include **stable identifiers** (experiment IDs, dataset IDs, model IDs) to support graph linkage.  
- Reference:
  - STAC Collections/Items,  
  - DCAT datasets,  
  - Model cards and SOPs where applicable.

Focus Mode:

- **MAY** summarize experiment docs, highlight metrics, and provide links to results.  
- **MUST NOT** invent results or governance outcomes that are not present in the document.  
- **MUST NOT** alter the normative content of the experiment.

---

## 🗺️ Diagrams

Use this section for **optional** diagrams in concrete experiment docs.  
The template provides an example that authors may copy and adapt.

### Example Experiment Flow

~~~mermaid
flowchart TD
  A["Raw Data (Ingest)"] --> B["ETL / Preprocessing"]
  B --> C["Experiment Logic (Model / Analysis)"]
  C --> D["Validation & Metrics"]
  D --> E["Artifacts & Telemetry Export"]
~~~

Author rules:

- At most **one mermaid diagram per section**.  
- Use labels that match your experiment’s actual terminology.  
- Summarize the key takeaway of the diagram in surrounding prose.

---

## 🧪 Validation & CI/CD

Every experiment document is part of the CI/CD surface and must integrate with the following workflows:

| Workflow                | Purpose                                            |
|-------------------------|----------------------------------------------------|
| `docs-lint.yml`         | YAML, headings, links, diagrams, layout checks     |
| `faircare-validate.yml` | Ethics, FAIR+CARE alignment, PII / sensitive scan |
| `stac-validate.yml`     | STAC/DCAT validation (if experiment emits STAC)    |
| `telemetry-export.yml`  | Aggregates experiment metrics into telemetry       |

Concrete docs should describe what passed and what failed when relevant, and may link to:

~~~text
reports/self-validation/docs/lint_summary.json
reports/faircare/faircare_summary.json
reports/self-validation/stac/stac_validation.json
releases/vX.Y.Z/focus-telemetry.json
~~~

Treat failing CI as a **specification or implementation issue** that must be addressed before the experiment is considered complete.

---

## ⚖ FAIR+CARE & Governance

Concrete experiment docs must include a **FAIR+CARE validation** subsection similar to:

| Principle        | Evidence / Notes                                                              |
|------------------|-------------------------------------------------------------------------------|
| **Findable**     | STAC Items/Collections updated; stable IDs/DOIs used; catalog entries linked |
| **Accessible**   | License clarity (e.g., CC‑BY); accessible formats; alt-text for key figures  |
| **Interoperable**| ISO/OGC metadata; STAC/DCAT alignment; standard CRS & units                  |
| **Reusable**     | Versioned scripts; SBOM; checksums; documented limitations & assumptions     |
| **CARE**         | Cultural sensitivity review; Indigenous land checks; no harmful disclosures  |

If an experiment touches sensitive topics or data:

- Explicitly document **governance decisions** (e.g., redaction, generalization, access controls).  
- Reference relevant SOPs or governance standards.  
- Confirm that Sovereignty and FAIR+CARE guidelines were followed.

Governance artifacts to reference may include:

~~~text
reports/faircare/faircare_summary.json
reports/audit/data_provenance_ledger.json
docs/standards/governance/ROOT-GOVERNANCE.md
docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md
~~~

---

## 🕰️ Version History

| Version   | Date       | Author        | Summary                                                                                                                |
|----------:|-----------:|--------------|------------------------------------------------------------------------------------------------------------------------|
| v11.2.6   | 2025-12-11 | `@kfm-docs`  | Updated to KFM‑MDP v11.2.6; aligned paths to v11.2.6 releases/schemas; synchronized structure with Core Markdown Template and Templates Index; clarified CI and Story Node usage. |
| v11.2.4   | 2025-12-06 | `@kfm-docs`  | Added full front‑matter metadata, directory layout, Story Node guidance, STAC/DCAT/PROV alignment, and CI/CD integration. |
| v10.2.2   | 2025-11-12 | `@kfm-docs`  | Aligned refs to v10.2.0; enforced stricter markdown protocol; added governance and telemetry rules.                   |
| v10.0.0   | 2025-11-10 | `@kfm-docs`  | Introduced telemetry schema v2; ensured MCP/FAIR+CARE compliance.                                                     |
| v9.7.0    | 2025-11-05 | `@kfm-docs`  | Standardized experiment template into shared `docs/templates`.                                                        |
| v9.5.0    | 2025-10-20 | `@kfm-docs`  | Added FAIR+CARE & telemetry hooks; linked to governance workflows.                                                    |
| v9.0.0    | 2025-06-01 | `@kfm-core`  | Initial experiment documentation template for KFM.                                                                     |

---

<div align="center">

🧪 **Kansas Frontier Matrix — Experiment Documentation Template (v11.2.6)**  
Reproducible Experiments · FAIR+CARE Governance · Scientific & Historical Integrity  

[⬅ Back to Templates Index](README.md) ·  
[📘 Markdown Protocol (KFM‑MDP v11.2.6)](../standards/kfm_markdown_protocol_v11.2.6.md) ·  
[⚖ Governance Charter](../standards/governance/ROOT-GOVERNANCE.md)

</div>