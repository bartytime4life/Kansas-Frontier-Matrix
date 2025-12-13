---
title: "🧬 Kansas Frontier Matrix — MCP Model Cards Index (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "mcp/model_cards/README.md"

version: "v11.0.0"
last_updated: "2025-12-13"
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
event_source_id: "urn:kfm:mcp:modelcards:index"

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
  - "a11y-adaptations"
  - "layout-normalization"
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
Provide the **governed, reproducible, CARE-aligned index** for all AI/ML models used inside the Kansas Frontier Matrix.  
This directory hosts **Model Cards**, the official documentation for every AI model used in pipelines, inference engines, geospatial processors, and Focus Mode v3.

Model Cards exist to ensure **transparency**, **safety**, **ethics**, **sovereignty**, and **scientific reproducibility**.

</div>

---

## 📘 Overview

### Role of model cards in KFM v11
Model Cards are mandatory documentation artifacts for every model that:

- generates predictions
- performs inference in ETL pipelines
- supports Focus Mode or Story Node v3
- performs geospatial interpolation, alignment, or imputation
- reconstructs historical fields (climate, hydrology, hazards)
- processes documents, archives, or imagery (NLP/CV)
- performs narrative generation or narrative shaping
- is used by CrewAI or LangGraph participants

Model Cards are used to:
- document intended use and restricted use
- enable reproducibility (seeds, environments, references to experiments)
- enforce FAIR+CARE and sovereignty boundaries
- support provenance via PROV-O and OpenLineage
- record limitations, failure modes, and required human oversight

### Model card index
| Model | File | Model version | Domain | Sensitivity | Status |
|------|------|---------------|--------|------------|--------|
| Climate Anomaly Net | `./climate_anomaly_net_v3.md` | v3 | Climate anomaly reconstruction | Low | Active / Enforced |
| Hydrology Seq2Seq | `./hydrology_seq2seq_v11.md` | v11 | Hydrologic reconstruction (gap-fill) | Mixed | Active / Enforced |
| Focus Mode Transformer | `./focus_mode_transformer_v3.md` | v3 | Governed narrative reasoning | Mixed | Active / Enforced |
| Geo Alignment Net | `./geo_alignment_net_v4.md` | v4 | Geospatial alignment and harmonization | Mixed | Active / Enforced |

---

## 🗂️ Directory Layout

~~~text
mcp/model_cards/
│
├── README.md                          # This file — index + rules
│
├── climate_anomaly_net_v3.md          # Climate anomaly reconstruction model
├── hydrology_seq2seq_v11.md           # Time-series hydrology reconstruction model
├── focus_mode_transformer_v3.md       # Governed narrative reasoning model
├── geo_alignment_net_v4.md            # Geospatial harmonization/alignment model
└── <model_name>_v<version>.md         # Additional model cards (required naming convention)
~~~

### Naming convention
Model card filenames MUST follow:

~~~text
<model_name>_v<version>.md
~~~

Downstream pipelines MUST reference:
- the model card path under `mcp/model_cards/`
- the model card version (doc `version:`) and the model version where applicable
- the governing experiment(s) and provenance references

---

## 🧭 Context

### Model card requirements (what every model card must contain)
Each model card MUST include:

- metadata header (model name, versions, domain, FAIR+CARE fields, sovereignty notes)
- intended use and restricted/out-of-scope use
- training/evaluation dataset references (STAC/DCAT identifiers)
- training procedure and reproducibility (seeds, hardware, environment, SBOM references)
- evaluation metrics and validation approach
- limitations, failure modes, and safety boundaries
- governance notes (CARE classification, sovereignty handling, required human oversight)
- provenance and lineage (PROV-O JSON-LD + OpenLineage events + checksums)
- telemetry references (energy and carbon where applicable)

### When a model card is required
A model card is required if the model:
- is executed in any pipeline under `src/pipelines/**`
- influences Story Node content or Focus Mode context
- produces geospatially keyed outputs (rasters, vectors, indexes)
- performs alignment, inference, or reconstruction over time series
- could meaningfully impact interpretation, safety, or governance decisions

---

## 📦 Data & Metadata

### Training and evaluation dataset expectations
Model cards MUST:
- list training and evaluation datasets with STAC/DCAT identifiers
- record temporal/spatial coverage bounds of training data
- note known bias/coverage gaps and mitigations
- explicitly state whether Indigenous-only or sovereignty-restricted datasets were used (and how they were handled)

### Contract alignment expectations
Model cards MUST declare:
- pipeline contract version (KFM-PDC v11)
- data contract name(s) where applicable
- any required masking/generalization policy for inputs and outputs

---

## 🧠 Story Node & Focus Mode Integration

### Focus Mode v3
Any model that feeds Focus Mode must document:
- evidence/citation requirements for model-derived claims
- narrative safety boundaries (non-speculative, neutral tone)
- sovereignty masking behavior (H3 or other policy mechanisms)
- required gating and human review rules

### Story Node v3
Any model that influences Story Nodes must document:
- what fields it can populate or modify
- what evidence links are required
- prohibited outputs and disallowed inference categories
- masking/generalization defaults for sensitive geographies and cultural material

---

## 🧪 Validation & CI/CD

Model cards must pass:
- KFM-MDP v11.2.6 markdown validation
- model card schema validation (where enforced)
- presence checks for required sections/fields
- provenance presence checks (PROV-O + OpenLineage + checksums)
- FAIR+CARE field presence checks
- sovereignty constraints (no coordinate leakage, masking rules documented)
- telemetry reference checks (where required)

CI should block merge for:
- missing provenance artifacts
- missing FAIR+CARE metadata
- missing training/evaluation dataset identifiers
- invalid naming conventions
- ambiguous narrative boundaries (for narrative-capable systems)
- absent telemetry references where required

---

## 🌐 STAC, DCAT & PROV Alignment

Model cards must:
- reference STAC/DCAT identifiers for training/evaluation datasets and derived publishable artifacts
- specify where STAC/DCAT records are emitted (if the model produces assets)
- provide a PROV-O JSON-LD block that links:
  - datasets used
  - training activity (experiment/run)
  - model artifact entity
  - responsible agent(s) and pipeline identity
- link to OpenLineage event storage location for key runs

---

## ⚖ FAIR+CARE & Governance

All model cards must:
- declare CARE posture and any sovereignty implications
- include prohibited use categories and human review requirements
- document masking/generalization defaults for restricted content
- avoid publishing sensitive locations or restricted knowledge
- preserve traceability from claim → dataset/document → provenance → run identity

---

## 🕰️ Version History

| Version | Date | Summary |
|--------:|------|---------|
| v11.0.0 | 2025-11-23 | Initial KFM-MCP v11 model cards index. |
| v11.0.0 | 2025-12-13 | Normalized document to KFM-MDP v11.2.6 (approved H2 set, required directory layout section, tilde fences, governance links in footer). |

---

<div align="center">

🧬 **MCP Model Cards Index**  
[🏛️ Governance Charter](../../docs/standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../docs/standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

© 2025 Kansas Frontier Matrix — CC‑BY 4.0  
MCP‑DL v6.3 · KFM‑MDP v11.2.6 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  
Reproducibility · Transparency · Governance

</div>
