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
  - "extract-metadata"
  - "semantic-highlighting"
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

provenance_chain:
  - "mcp/model_cards/README.md@v11.0.0"
  - "docs/standards/kfm_markdown_protocol_v11.2.6.md@v11.2.6"
---

<div align="center">

# 🧬 **Master Coder Protocol — Model Cards Index (v11 LTS)**
`mcp/model_cards/README.md`

**Purpose**  
Provide the governed, reproducible, FAIR+CARE and sovereignty-aligned index for all AI/ML **Model Cards**
used inside the Kansas Frontier Matrix (KFM). Model Cards are mandatory documentation artifacts defining
intended use, restricted use, training data, evaluation, limitations, governance boundaries, provenance, and
sustainability telemetry for every model used in pipelines, Focus Mode, and Story Node workflows.

</div>

---

## 📘 Overview

Model Cards are required for any model that:
- produces predictions, reconstructions, or alignments
- runs inference inside ETL / pipeline steps
- supports Focus Mode or Story Node generation
- performs interpolation, imputation, harmonization, or geospatial alignment
- participates in CrewAI or LangGraph deterministic executors

Model Cards exist to:
- define intended use vs prohibited use
- record training/evaluation dataset identifiers (STAC/DCAT)
- document reproducibility controls (seeds, environments, experiment references)
- enforce governance boundaries (FAIR+CARE + sovereignty constraints)
- preserve provenance evidence (PROV-O + OpenLineage + checksums)
- attach sustainability telemetry (energy + carbon)

---

## 🗂️ Directory Layout

~~~text
mcp/model_cards/
│
├── README.md                           # This file — canonical index + rules
├── climate_anomaly_net_v3.md           # 🌡️ Climate anomaly reconstruction (CAN-v3)
├── hydrology_seq2seq_v11.md            # 💧 Hydrology reconstruction (HS2S-v11)
├── focus_mode_transformer_v3.md        # 🧠 Governed narrative reasoning engine (FMT-v3)
├── geo_alignment_net_v4.md             # 🗺️ Geospatial alignment & harmonization (GAN-v4)
└── <model_slug>_v<version>.md          # Additional model cards (required naming convention)
~~~

---

## 🧭 Context

### Naming convention
Model card filenames MUST follow:

~~~text
<model_slug>_v<version>.md
~~~

Downstream pipelines MUST reference:
- the model card file path under `mcp/model_cards/`
- the model card `version:` (doc version)
- the model artifact version (if different)
- the experiment(s) and provenance bundle(s) that support the model

### Relationship to MCP experiments
Every model card MUST link to at least one `mcp/experiments/*.md` record that documents:
- training or fine-tuning
- evaluation/validation
- deployment validation gates (when applicable)

---

## 📦 Data & Metadata

### Required declarations in model cards
Every model card MUST declare:
- intended use and restricted use
- training and evaluation datasets (STAC/DCAT identifiers)
- reproducibility controls (seed, environment, hardware, SBOM reference)
- evaluation metrics and validation methods
- limitations, failure modes, and required human oversight
- governance boundaries (FAIR+CARE posture + sovereignty implications)
- provenance and lineage (PROV-O + OpenLineage locations + checksums)
- telemetry references (energy + carbon)

### Sovereignty and sensitivity defaults
- Never publish or refine sensitive locations in model outputs.
- Require masking/generalization (H3-based where applicable) whenever a model may touch cultural or sovereignty-restricted content.
- Require human review gates for any narrative-capable model outputs.

---

## 🧱 Architecture

Model Cards bind together:
- pipeline configuration (what calls the model)
- catalog identifiers (STAC/DCAT)
- graph entities and relationships (Neo4j)
- UI consumption boundaries (Focus Mode and Story Nodes)
- provenance traces (PROV-O and OpenLineage)
- telemetry bundles (energy/carbon)

Minimum interface contract each card must state:
- what the model consumes (inputs + required metadata)
- what it produces (outputs + expected schemas)
- where provenance and telemetry are written

---

## 🧠 Story Node & Focus Mode Integration

### Narrative-capable models
If a model can generate or shape narrative output, its model card MUST state:
- what claims are allowed (evidence-led only)
- what claims are prohibited (no speculation, no invented causes, no genealogy)
- required masking rules (H3/generalization) and sovereignty gates
- required human review steps before publish/release

### Non-narrative models
Numeric/geospatial models must still define:
- output precision constraints
- masking/generalization defaults for restricted areas
- downstream usage boundaries for narrative systems

---

## 🧪 Validation & CI/CD

Model cards must pass:
- KFM-MDP v11.2.6 markdown validation (structure + fences)
- required front-matter presence checks
- provenance presence checks (PROV-O + OpenLineage + checksums)
- FAIR+CARE field presence checks
- sovereignty constraints (no coordinate leakage; masking documented)
- telemetry reference checks (where required)

Common failures that must be treated as merge blockers:
- missing provenance artifacts
- missing dataset identifiers for training/eval
- missing or ambiguous restricted-use boundaries
- more than one H1
- unapproved H2 headings
- backtick fences inside repo Markdown (must use `~~~`)

---

## 🌐 STAC, DCAT & PROV Alignment

Model cards must:
- reference STAC/DCAT identifiers for training/evaluation datasets
- specify where STAC/DCAT records are emitted (if the model produces publishable assets)
- provide a PROV-O JSON-LD block in the model card (or reference the location if external)
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
| v11.0.0 | 2025-12-12 | Normalized to KFM-MDP v11.2.6 (approved H2 set, tilde fences, governed footer, required metadata fields). |

---

<div align="center">

[🏛️ Governance Charter](../../docs/standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../docs/standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
MCP-DL v6.3 · KFM-MDP v11.2.6 · KFM-OP v11 · KFM-PDC v11

</div>
