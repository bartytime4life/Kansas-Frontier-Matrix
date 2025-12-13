---
title: "🧬 Kansas Frontier Matrix — MCP Model Cards Index (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "mcp/model_cards/README.md"

version: "v11.0.0"
last_updated: "2025-12-12"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · MCP Board · FAIR+CARE Council · AI Governance Team"
content_stability: "stable"

status: "Active / Enforced"
doc_kind: "Index"
header_profile: "standard"
footer_profile: "standard"
intent: "mcp-model-card-index"
semantic_document_id: "kfm-mcp-modelcards-index"
doc_uuid: "urn:kfm:mcp:modelcards:index:v11.0.0"
event_source_id: "urn:kfm:mcp:modelcards:index:v11.0.0"

machine_extractable: true
classification: "Governed AI Document"
sensitivity: "Mixed"
fair_category: "F1-A1-I2-R2"
care_label: "Collective Benefit · Responsibility · Ethics"
immutability_status: "version-pinned"
accessibility_compliance: "WCAG 2.1 AA+"
jurisdiction: "Kansas / United States"

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"

stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
signature_ref: "../../releases/v11.0.0/signature.sig"
attestation_ref: "../../releases/v11.0.0/slsa-attestation.json"
sbom_ref: "../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../releases/v11.0.0/manifest.zip"

telemetry_ref: "../../releases/v11.0.0/mcp-modelcards-telemetry.json"
telemetry_schema: "../../schemas/telemetry/mcp-modelcards-v11.json"

governance_ref: "../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

ai_transform_permissions:
  - "summarize"
  - "semantic-highlighting"
  - "metadata-extraction"
  - "layout-normalization"
  - "a11y-adaptations"
ai_transform_prohibited:
  - "fabricate-model-claims"
  - "fabricate-provenance"
  - "invent-dataset-ids"
  - "invent-license-rights"
  - "override-governance"
  - "expose-sensitive-coordinates"
  - "deanonymize"
---

<div align="center">

# 🧬 **Master Coder Protocol — Model Cards Index (v11 LTS)**
`mcp/model_cards/README.md`

**Purpose**  
Provide the **governed, reproducible, FAIR+CARE + sovereignty-aligned index** for all AI/ML **Model Cards**
used inside the Kansas Frontier Matrix (KFM). Model Cards are mandatory documentation artifacts defining
intended use, restricted use, training data, evaluation, limitations, governance boundaries, provenance, and
sustainability telemetry for every model used in pipelines, Focus Mode, and Story Node workflows.

<img src="https://img.shields.io/badge/MCP--DL-v6.3-blueviolet" />
<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/FAIR%2BCARE-Governance%20Aligned-orange" />
<img src="https://img.shields.io/badge/Accessibility-WCAG_2.1_AA%2B-blueviolet" />
<img src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />

[🧪 MCP Experiments Index](../experiments/README.md) ·
[📈 Model Cards Telemetry](../../releases/v11.0.0/mcp-modelcards-telemetry.json) ·
[🧾 Telemetry Schema](../../schemas/telemetry/mcp-modelcards-v11.json) ·
[🏛️ Governance Charter](../../docs/standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../docs/standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

</div>

---

## 📘 Overview

### ✅ What a Model Card is in KFM
A Model Card is the authoritative, governed contract for a model’s:

- 🎯 Intended use and prohibited use
- 🧪 Training and evaluation inputs (STAC/DCAT identifiers)
- 📊 Evaluation results and validation methodology
- ⚠️ Limitations, failure modes, and required human oversight
- 🛡️ Governance boundaries (FAIR+CARE + sovereignty constraints)
- 🧾 Provenance evidence (PROV-O + OpenLineage references + checksums)
- ♻️ Sustainability telemetry (energy + carbon)

### ✅ When a Model Card is required
A Model Card is required for any model that:

- 🧠 Produces predictions, reconstructions, or alignments
- ⚙️ Runs inference inside ETL/pipeline steps
- 🧭 Supports Focus Mode v3 or Story Node v3 workflows
- 🗺️ Performs interpolation, imputation, harmonization, or geospatial alignment
- 🤖 Participates in CrewAI or LangGraph deterministic executors

### ✅ Naming convention
Model Card filenames MUST follow:

~~~text
<model_slug>_v<version>.md
~~~

Downstream pipelines MUST reference:
- the model card path under `mcp/model_cards/`
- the model card `version:` (doc version)
- the model artifact version (if different)
- the experiment(s) and provenance bundle(s) supporting the model

### 📚 Current Model Card Index

| 🧠 Model | 📄 Model Card | 🔢 Model Version | 🧭 Domain | 🛡️ Sensitivity | ✅ Status |
|---|---|---:|---|---|---|
| 🌡️ Climate Anomaly Net | `./climate_anomaly_net_v3.md` | v3 | Climate anomaly reconstruction | Low | Active / Enforced |
| 💧 Hydrology Seq2Seq | `./hydrology_seq2seq_v11.md` | v11 | Hydrologic reconstruction (gap-fill) | Mixed | Active / Enforced |
| 🧠 Focus Mode Transformer | `./focus_mode_transformer_v3.md` | v3 | Governed narrative reasoning | Mixed | Active / Enforced |
| 🗺️ Geo Alignment Net | `./geo_alignment_net_v4.md` | v4 | Geospatial alignment & harmonization | Mixed | Active / Enforced |

---

## 🗂️ Directory Layout

~~~text
📁 KansasFrontierMatrix/                                   — Monorepo root
├── 📁 mcp/                                                — Master Coder Protocol (governed R&D)
│   ├── 📁 experiments/                                    — Experiment logs (MCP-DL)
│   │   └── 📄 README.md                                   — Experiments index + rules
│   └── 📁 model_cards/                                    — Model Cards (this directory)
│       ├── 📄 README.md                                   — 🧬 This file (index + rules)
│       ├── 📄 climate_anomaly_net_v3.md                   — 🌡️ CAN-v3 (climate anomaly reconstruction)
│       ├── 📄 hydrology_seq2seq_v11.md                    — 💧 HS2S-v11 (hydrology reconstruction)
│       ├── 📄 focus_mode_transformer_v3.md                — 🧠 FMT-v3 (governed narrative reasoning)
│       ├── 📄 geo_alignment_net_v4.md                     — 🗺️ GAN-v4 (geospatial alignment)
│       └── 📄 <model_slug>_v<version>.md                  — ➕ Add new model cards here (one per model+version)
├── 📁 data/                                               — Data layer (raw + processed + provenance)
│   └── 📁 provenance/                                     — Provenance artifacts (PROV-O + OpenLineage)
└── 📁 releases/                                           — Release bundles (SBOM, attestations, telemetry)
    └── 📁 v11.0.0/                                        — Version-pinned release artifacts
        └── 🧾 mcp-modelcards-telemetry.json               — Energy/carbon telemetry for model work
~~~

---

## 🧭 Context

### 🔗 Relationship to MCP experiments
Every model card MUST link to at least one `mcp/experiments/*.md` record documenting:
- training or fine-tuning
- evaluation/validation
- deployment validation gates (when applicable)
- reproducibility controls (seed, environment, dependencies, provenance outputs)

### 🧾 Minimum required declarations inside every model card
- ✅ Intended use vs ❌ restricted use
- 🧪 Training and evaluation datasets (STAC/DCAT IDs)
- 🎛️ Reproducibility (seed, framework, hardware, container, SBOM reference)
- 📊 Metrics and validation methodology
- ⚠️ Limitations and failure modes
- 🛡️ Governance boundaries + human oversight requirements
- 🧾 PROV-O + OpenLineage locations + checksums
- ♻️ Telemetry reference (energy/carbon)

---

## 📦 Data & Metadata

### 🪶 Sovereignty and sensitivity defaults
- Never publish or refine sensitive locations in model outputs.
- Require masking/generalization (H3-based where applicable) whenever a model may touch cultural or sovereignty-restricted content.
- Require human review gates for narrative-capable models and for any output used in high-stakes contexts.

### 🧩 Contract alignment expectations
Model cards MUST declare:
- pipeline contract version (KFM-PDC v11)
- any data contracts they rely on (if applicable)
- required masking/generalization policy for inputs and outputs

---

## 🧱 Architecture

Model cards bind together:
- 🧰 pipeline configuration (what calls the model)
- 🗂️ catalog identifiers (STAC/DCAT)
- 🧠 graph entities and relationships (Neo4j)
- 🖥️ UI consumption boundaries (Focus Mode + Story Nodes)
- 🧾 provenance traces (PROV-O + OpenLineage)
- ♻️ telemetry bundles (energy/carbon)

Minimum interface contract each card must state:
- what the model consumes (inputs + required metadata)
- what it produces (outputs + expected schemas)
- where provenance and telemetry are written

---

## 🧠 Story Node & Focus Mode Integration

### 🧠 Narrative-capable models (must be explicit)
If a model can generate or shape narrative output, its model card MUST state:
- ✅ allowed claim types (evidence-led only)
- ❌ prohibited claim types (no speculation, no invented causes, no genealogy)
- 🪶 masking rules (H3/generalization) and sovereignty gates
- 👤 required human review steps before publish/release

### 🗺️ Non-narrative geospatial models
Geospatial alignment/interpolation models must define:
- output precision constraints and confidence propagation
- masking/generalization defaults for restricted areas
- downstream boundaries for narrative systems

---

## 🧪 Validation & CI/CD

Model cards must pass:
- KFM-MDP v11.2.6 markdown validation (structure + fences)
- required front-matter presence checks
- provenance presence checks (PROV-O + OpenLineage + checksums)
- FAIR+CARE field presence checks
- sovereignty constraints (no coordinate leakage; masking documented)
- telemetry reference checks

Common merge blockers:
- missing provenance artifacts
- missing dataset identifiers for training/eval
- missing or ambiguous restricted-use boundaries
- more than one H1
- unapproved H2 headings
- backtick fences inside committed Markdown (use `~~~` only)

---

## 🌐 STAC, DCAT & PROV Alignment

Model cards must:
- reference STAC/DCAT identifiers for training/evaluation datasets
- specify where STAC/DCAT records are emitted (if the model produces publishable assets)
- provide a PROV-O JSON-LD block in the model card (or a stable path to it)
- identify OpenLineage event storage location(s) for key runs

---

## ⚖ FAIR+CARE & Governance

All model cards must:
- declare FAIR category and CARE label
- declare sovereignty implications and required masking/approvals
- list prohibited outputs and required human oversight
- ensure traceability from claim → dataset/document → provenance → run identity

---

## 🕰️ Version History

| Version | Date | Summary |
|--------:|------|---------|
| v11.0.0 | 2025-11-23 | Initial MCP model cards index for KFM v11. |
| v11.0.0 | 2025-12-12 | Updated to KFM-MDP v11.2.6: approved H2 set, emoji directory layout, tilde fences, governed footer links. |

---

<div align="center">

[🏛️ Governance Charter](../../docs/standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../docs/standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
MCP-DL v6.3 · KFM-MDP v11.2.6 · KFM-OP v11 · KFM-PDC v11 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>
