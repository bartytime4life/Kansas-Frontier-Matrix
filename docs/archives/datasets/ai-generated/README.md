---
title: "🧠 Kansas Frontier Matrix — Archives AI-Generated Datasets Layer (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/archives/datasets/ai-generated/README.md"

version: "v11.2.4"
last_updated: "2025-12-06"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Autonomous · FAIR+CARE Council Oversight"
content_stability: "stable"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-version-hash>"
doc_integrity_checksum: "<sha256>"

doc_uuid: "urn:kfm:doc:archives-datasets-ai-generated:v11.2.4"
semantic_document_id: "kfm-doc-archives-datasets-ai-generated"
event_source_id: "ledger:kfm:doc:archives-datasets-ai-generated:v11.2.4"

sbom_ref: "../../../../releases/v11.2.4/sbom.spdx.json"
manifest_ref: "../../../../releases/v11.2.4/manifest.zip"
telemetry_ref: "../../../../releases/v11.2.4/focus-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/archives-datasets-ai-generated-v4.json"
signature_ref: "../../../../releases/v11.2.4/signature.sig"
attestation_ref: "../../../../releases/v11.2.4/slsa-attestation.json"
energy_schema: "../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.4"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

status: "Active / Enforced"
doc_kind: "Module Subsystem Overview"
intent: "archives-datasets-ai-generated"

fair_category: "F1-A1-I1-R1"
care_label: "C1 · Indigenous Knowledge Protection Enabled"
sensitivity: "Culturally Sensitive (archives; auto-mask rules apply)"
sensitivity_level: "Elevated"
public_exposure_risk: "Medium"
classification: "Public (Governed · Archive-Scoped)"
jurisdiction: "Kansas / United States"
indigenous_rights_flag: true
immutability_status: "version-pinned"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"

ontology_alignment:
  cidoc: "E78 Collection"
  schema_org: "Dataset"
  prov_o: "prov:Collection"
  owl_time: "ProperInterval"
  geosparql: "geo:FeatureCollection"

metadata_profiles:
  - "STAC 1.0.0"
  - "DCAT 3.0"
  - "PROV-O"
  - "FAIR+CARE"

provenance_chain:
  - "docs/archives/datasets/ai-generated/README.md@v11.0.1"
  - "docs/archives/datasets/ai-generated/README.md@v10.4.x"
  - "docs/archives/datasets/ai-generated/README.md@v10.x"

provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: true

json_schema_ref: "../../../../schemas/json/kfm-archives-datasets-ai-generated-v11.2.4.schema.json"
shape_schema_ref: "../../../../schemas/shacl/kfm-archives-datasets-ai-generated-v11.2.4-shape.ttl"
story_node_refs: []

header_profile: "standard"
footer_profile: "standard"
diagram_profiles:
  - "mermaid-flowchart-v1"

scope:
  domain: "archives-datasets-ai-generated"
  applies_to:
    - "docs/archives/datasets/ai-generated/**"
    - "data/archives/datasets/ai-generated/**"

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
  workflow: ".github/workflows/kfm-ci.yml"
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

# 🤖 **Kansas Frontier Matrix — Archives AI-Generated Datasets Layer (v11.2.4)**  
`docs/archives/datasets/ai-generated/README.md`

**Purpose**  
Define the **AI-generated datasets segment** of the Archives Datasets Layer — the place where **Focus Mode**, **Story Node v3**, and other AI/ML outputs are preserved as **immutable, FAIR+CARE-governed archival datasets** with complete provenance, telemetry, and reconstruction instructions.

<img src="https://img.shields.io/badge/Docs-MCP_v6.3-blue" />
<img src="https://img.shields.io/badge/KFM--MDP-v11.2.4-purple" />
<img src="https://img.shields.io/badge/License-CC--BY%204.0-green" />
<img src="https://img.shields.io/badge/FAIR%2BCARE-C1_Indigenous_Protection-gold" />
<img src="https://img.shields.io/badge/Status-Active-brightgreen" />

</div>

---

## 📘 Overview

The **Archives AI-Generated Datasets Layer** treats AI outputs as **first-class archival entities**:

- 🤖 Focus Mode narrative corpora and derived semantic layers.  
- 🧩 Story Node v3 JSON bundles and graph-aligned emissions.  
- 📊 AI-generated or AI-augmented tabular/geo datasets used in KFM analyses.  
- 🧠 Model evaluation, drift, and explainability datasets (where archived long-term).

Each archived AI dataset is:

- **Immutable** — new results → new versioned snapshot (no overwrite).  
- **Traceable** — bound to models, data, and configs through **PROV-O**.  
- **Governed** — subject to **FAIR+CARE (C1)**, including Indigenous knowledge protections.  
- **Reconstructable** — contains or references scripts, configs, and prompts needed to reproduce the output.  

It is a **specialized sub-layer** under:

- `docs/archives/README.md` (Archives Module).  
- `docs/archives/datasets/README.md` (Archives Datasets Layer).

---

## 🗂️ Directory Layout

~~~text
📁 docs/archives/datasets/ai-generated/      # 🤖 AI-generated archives documentation root
│
├── 📄 README.md                             # 🤖 This overview file (v11.2.4)
│
├── 📁 focus-mode/                           # 🧠 Focus Mode narrative corpora & contexts
│   ├── 📄 README.md                         #   Scope & governance for Focus Mode archives
│   └── …                                    #   Per-release docs (indices, ledgers, SOP refs)
│
├── 📁 story-node-v3/                        # 🧩 Story Node v3 archival bundles
│   ├── 📄 README.md                         #   Story-node specific structures & policies
│   └── …                                    #   Node collections, schemas, examples
│
└── 📁 analysis-summaries/                   # 📊 AI-generated cross-domain synthesis datasets
    ├── 📄 README.md                         #   Summary corpus design & limits
    └── …                                    #   Experiment-linked summaries (by domain/release)
~~~

**Data counterparts (conceptual target layout):**

~~~text
📁 data/archives/datasets/ai-generated/      # 📦 Physical AI-generated datasets
├── 📁 focus-mode/                           #   Serialized corpora (JSONL, parquet, pmtiles)
├── 📁 story-node-v3/                        #   Node bundles, graph exports, GeoJSON, JSON-LD
└── 📁 analysis-summaries/                   #   Structured summaries (parquet, CSV, JSONL)
~~~

All subdirectories must have:

- A `README.md` describing scope, governance constraints, and expected formats.  
- References to the STAC/DCAT collections/items that index the actual data assets.

---

## 🧭 Context

This layer sits at the intersection of:

- **AI/ML systems** (e.g., Focus Transformer, explainability pipelines).  
- **Archives** (immutable, governed long-term storage).  
- **Story Node & Focus Mode** narrative infrastructure.

Typical lifecycle:

1. AI workflows (e.g., `ai-train.yml`, `ai-explainability.yml`, custom analysis notebooks) produce **candidate AI datasets**.  
2. These go through **FAIR+CARE + governance review** to decide what is promoted to **archive** status.  
3. Approved outputs are **normalized**, **versioned**, and written into `data/archives/datasets/ai-generated/**`.  
4. Matching **documentation and indexes** are added under `docs/archives/datasets/ai-generated/**`.  
5. Telemetry about creation (energy, carbon, scope, model) is appended to `focus-telemetry.json`.

The Archives AI-generated Layer is optimized for **time travel and introspection** — allowing future users to understand:

- What the AI said / inferred.  
- Which models and data were used.  
- Under which governance rules and energy/carbon budgets.

---

## 🗺️ Diagrams

### AI-Generated Dataset Ingestion (Conceptual)

~~~mermaid
flowchart TD
  A["AI Workflow Outputs<br/>(Focus Mode · Story Nodes · Summaries)"]
    --> B["Candidate Datasets<br/>(staging)"]
  B --> C["FAIR+CARE + Governance Review<br/>(C1 · Indigenous Protections)"]
  C -->|Approved| D["Archive Normalization<br/>(STAC/DCAT/PROV + hashes)"]
  D --> E["Write to data/archives/datasets/ai-generated/**"]
  E --> F["Docs & Indexes<br/>(docs/archives/datasets/ai-generated/**)"]
  F --> G["Telemetry Append<br/>(focus-telemetry.json)"]
  C -->|Rejected / Restricted| H["Remediation · Restricted Holding · Redaction"]
~~~

---

## 🧠 Story Node & Focus Mode Integration

This layer is tightly coupled to **Focus Mode** and **Story Node v3**:

- **Focus Mode**  
  - Uses archived corpora under `focus-mode/` to provide **explainable, reproducible narratives**.  
  - Each narrative segment keeps pointers to:
    - Source documents (STAC/DCAT).  
    - Model ID & version.  
    - Time of generation and governance decision.

- **Story Node v3**  
  - Uses `story-node-v3/` to store:
    - Node JSON definitions.  
    - Links to archival datasets (treaties, hydrology baselines, etc.).  
    - Temporal and spatial extents (for map/timeline overlay).

Examples of Story Node targets:

~~~text
urn:kfm:story-node:archive:ai:focus-mode:v2.1:summary:blue-river-watershed
urn:kfm:story-node:archive:ai:historical:treaty-context:1867-kp
~~~

Rules:

- Story Nodes may **summarize or contextualize** archive content; they must **not alter** it.  
- For Indigenous or culturally sensitive materials:
  - Node text must follow sovereignty policies and avoid disclosing sensitive details.  
  - Node metadata must capture CARE decisions and governance references.

---

## 🧪 Validation & CI/CD

AI-generated datasets are validated by a combination of workflows:

- `faircare-validate.yml`  
  - Ensures CARE C1 rules are respected (especially for historical/Indigenous-related outputs).  
  - Checks for PII, sensitive topics, and governance flags.

- `stac-validate.yml`  
  - Validates STAC Collections/Items used to index AI datasets.  
  - Confirms required AI-specific fields (e.g., model, version, lineage references).

- `ai-explainability.yml` (where applicable)  
  - Produces explainability datasets (SHAP, LIME, IG, attention) which may themselves be archived.  

- `telemetry-export.yml`  
  - Pulls summary metrics into `focus-telemetry.json`:
    - `event_type = "ai_archive_dataset"`  
    - `model_id`, `dataset_family`, `energy_wh`, `carbon_gco2e`, `care_tag`.

Only datasets that **pass validation** and have complete metadata are eligible for archive promotion.

---

## 📦 Data & Metadata

AI-generated archive datasets must capture at least:

- **Identity**
  - `dataset_id` / PID.  
  - `title`, `description`, `family` (focus-mode, story-node-v3, analysis-summaries).  

- **Model & Data Provenance**
  - `model_id`, `model_version`, `model_card_ref`.  
  - Input dataset references (STAC IDs, DCAT Dataset IDs).  
  - Training/eval configuration IDs where relevant.

- **Generation Context**
  - Time of generation, environment (e.g., container image digest).  
  - Run IDs (CI/CD run, notebook job ID).  
  - Prompt templates or generation configuration (when using LLMs or generative models).

- **Ethics & Governance**
  - `care_tag` and rationale (e.g., `public`, `restricted`, `sensitive`).  
  - Sovereignty flags and governance decision IDs for C1 contexts.  
  - Links to FAIR+CARE audit outputs.

- **Technical**
  - File formats and encodings (JSONL, parquet, GeoJSON, PMTiles).  
  - Compression and tiling parameters (for large corpora).  
  - Checksums and SBOM references.

Metadata is expressed via:

- STAC Item properties (`kfm:*` extension fields).  
- DCAT dataset fields (`dct:creator`, `dct:provenance`, `dct:license`).  
- PROV-O JSON-LD entities and activities.

---

## 🌐 STAC, DCAT & PROV Alignment

For AI-generated datasets:

- **STAC**  
  - Collections: `kfm-archives-ai-focus-mode`, `kfm-archives-ai-story-nodes`, `kfm-archives-ai-analysis-summaries`.  
  - Items:
    - `properties.kfm:model_id`, `kfm:model_version`.  
    - `properties.kfm:source_datasets` (array of upstream IDs).  
    - `properties.kfm:care_tag`, `kfm:governance_ledger_ref`.  

- **DCAT**  
  - Each AI dataset family is a `dcat:Dataset` with:
    - `dct:title`, `dct:description`, `dct:creator`, `dct:license`.  
    - `dct:provenance` linking to PROV chains.  
    - `dcat:distribution` entries for corpora, docs, and provenance.

- **PROV-O**  
  - AI runs are `prov:Activity` nodes.  
  - Inputs (source datasets, configs, models) are `prov:Entity` nodes with `prov:used` edges.  
  - Resulting AI archives are `prov:Entity` nodes connected via `prov:wasGeneratedBy`, and potentially `prov:wasDerivedFrom`.

---

## 🧱 Architecture

Architecturally, the AI-generated archives layer:

1. **Receives** outputs from AI workflows and notebooks.  
2. **Normalizes** them to stable formats and metadata, with STAC/DCAT/PROV alignment.  
3. **Publishes** them under `data/archives/datasets/ai-generated/**`.  
4. **Documents** them here in `docs/archives/datasets/ai-generated/**`.  
5. **Exposes** them to Story Nodes, Focus Mode, and external archives through catalog APIs.  

Boundaries:

- No component in this layer modifies upstream AI or data pipelines — it only receives, validates, and archives.  
- Access and transformations for user-facing applications (Focus Mode, portals) are built **on top of** these archived datasets, not instead of them.

---

## ⚖ FAIR+CARE & Governance

Given the potential to **recontextualize sensitive material**, this layer is governed under **CARE C1**:

- **Collective Benefit**  
  - AI archives are curated to **benefit communities**, researchers, and cultural stewards, not replace primary sources or human expertise.

- **Authority to Control**  
  - Communities, especially Indigenous partners, retain authority over:
    - Where AI summaries can appear.  
    - How sensitive materials are paraphrased or contextualized.  
    - Whether AI outputs may be publicly exposed.

- **Responsibility & Ethics**  
  - AI-generated narratives must:
    - Avoid speculative claims about people or cultures.  
    - Clearly distinguish between **archival fact** and **AI interpretation**.  
    - Include links back to original sources plus governance decisions.

Governance decisions and reviews are logged to:

~~~text
docs/reports/audit/archives-ai-generated-governance-ledger.json
~~~

---

## 🕰️ Version History

| Version   | Date       | Summary                                                                                                            |
|----------:|------------|--------------------------------------------------------------------------------------------------------------------|
| **v11.2.4** | 2025-12-06 | First KFM-MDP v11.2.4-compliant AI-generated datasets layer doc; added emoji-aligned layout, full metadata, STAC/DCAT/PROV + C1 CARE posture. |
| v11.0.1  | 2025-11-19 | Initial v11 overview of AI-generated archives; defined focus-mode, story-node-v3, and analysis-summaries families. |
| v10.4.x  | 2025-10-XX | Early partial AI archives structure; ad-hoc narrative corpora and node bundles.                                    |
| v10.x    | 2025-0X-XX | Initial appearance of AI-generated artifacts in archives without dedicated subsystem doc.                           |

---

<div align="center">

🤖 **Kansas Frontier Matrix — Archives AI-Generated Datasets Layer (v11.2.4)**  
Immutable AI Narratives · FAIR+CARE (C1) Governance · Transparent Provenance  

[⬅ Back to Archives Datasets Layer](../README.md) ·  
[📁 Archives Module](../../README.md) ·  
[⚖ Governance Charter](../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

