---
title: "🧬 Kansas Frontier Matrix — MCP Model Cards Index (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "mcp/model_cards/README.md"
version: "v11.0.0"
last_updated: "2025-11-23"
review_cycle: "Quarterly · MCP Board · FAIR+CARE Council · AI Governance Team"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../releases/v11.0.0/mcp-modelcards-telemetry.json"
telemetry_schema: "../../schemas/telemetry/mcp-modelcards-v11.json"
governance_ref: "../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
ontology_protocol_version: "KFM-OP v11.0"
pipeline_contract_version: "KFM-PDC v11.0"
status: "Active / Enforced"
doc_kind: "Index"
intent: "mcp-model-card-index"
semantic_document_id: "kfm-mcp-modelcards-index"
doc_uuid: "urn:kfm:mcp:modelcards:index:v11.0.0"
machine_extractable: true
classification: "Governed AI Document"
sensitivity: "Mixed"
fair_category: "F1-A1-I2-R2"
care_label: "Collective Benefit · Responsibility · Ethics"
immutability_status: "version-pinned"
accessibility_compliance: "WCAG 2.1 AA+"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 🧬 **Master Coder Protocol — Model Cards Index (v11 LTS)**  
`mcp/model_cards/README.md`

**Purpose:**  
Provide the **governed, reproducible, CARE-aligned index** for all AI/ML models used inside the Kansas Frontier Matrix.  
This directory hosts **Model Cards**, the official documentation for every AI model used in pipelines, inference engines, geospatial processors, and Focus Mode v3.

Model Cards ensure **transparency**, **safety**, **ethics**, **sovereignty**, and **scientific reproducibility**.

</div>

---

## 📘 1. Role of Model Cards in KFM v11

Model Cards are **mandatory** documentation artifacts for every model that:

- Generates predictions  
- Performs inference in ETL pipelines  
- Supports Focus Mode or Story Node v3  
- Performs geospatial interpolation or imputation  
- Reconstructs historical fields (climate, hydrology, hazards)  
- Processes documents, archives, or imagery (NLP/CV)  
- Performs narrative generation or narrative shaping  
- Is used by CrewAI or LangGraph participants  

Model cards:

- Increase transparency and trust  
- Enable reproducibility  
- Enforce compliance with FAIR+CARE  
- Support OpenLineage lineage tracking  
- Document model limitations and ethical boundaries  
- Provide clear references for downstream analysis  

---

## 🗂 2. Directory Layout (v11)

```text
mcp/model_cards/
│
├── README.md                          # This file — index + rules
│
├── climate_anomaly_net_v3.md          # Example model card
├── hydrology_seq2seq_v11.md           # Time-series reconstruction AI model
├── focus_mode_transformer_v3.md       # Narrative reasoning model
├── climate_biascorrector_bcsd_v11.md  # Bias-correction model
├── geo_alignment_net_v4.md            # Geospatial harmonization model
└── ...                                # Additional model cards
```

Model card filenames must follow:

```
<model_name>_v<version>.md
```

All downstream pipelines must reference the **model card version**, not just the model version.

---

## 🧾 3. Required Structure of a Model Card (MCP-DL v6.3)

Each Model Card **must** include:

### 🧬 A. Metadata Header
- Model name  
- Version  
- Architect(s) / contributors  
- Purpose/Domain  
- FAIR+CARE classification  
- CARE/Sovereignty notes  
- Data Contract version  
- Training dataset STAC/DCAT IDs  
- Model provenance (PROV-O + OpenLineage)  
- Energy/Carbon telemetry references  

### 📚 B. Model Summary
- Intended use cases  
- High-level architecture description  
- Model lineage (previous versions, experiments, related SOPs)  
- Safety limitations & disclaimers  

### 🧪 C. Training Data
- Dataset lists with STAC & DCAT metadata  
- Bias assessment (spatial, demographic, historical)  
- CARE governance assessment  
- Any filtered/masked content  

Required: explicit note on **Indigenous-related or sensitive datasets**.

### ⚙️ D. Training Procedure
- Hyperparameters  
- Seeds  
- Hardware used  
- Software environment (versions)  
- Experiment ID (`mcp/experiments/**`)  
- Reproducibility notes  

### 📊 E. Evaluation & Metrics
- Accuracy / F1 / RMSE / MAE  
- Spatial/temporal performance  
- Uncertainty quantification  
- SHAP/LIME explainability  
- Error maps (if geospatial)  
- Narrative consistency checks (for LLMs)  
- Hazard-specific metrics where relevant  

### 🧭 F. Governance & Ethical Considerations
- CARE compliance  
- Sovereignty checks  
- Narrative safety checks  
- Prohibited output categories  
- Bias mitigation approaches  
- Ethical coverage for human subjects or historical groups  
- Accessibility considerations  

### 🔗 G. Limitations & Warnings
- Known failure modes  
- Situations where the model should not be used  
- Risks or uncertainties  
- Areas requiring further review or expert intervention  

### 📦 H. Deployment & Usage Boundaries
- The exact pipelines where the model is allowed  
- Data domains it can or cannot process  
- Required masking (H3 or other)  
- Required human oversight  

### 📑 I. Provenance & Lineage
- OpenLineage job ID(s)  
- Model training events  
- STAC/DCAT references for inputs  
- Hashes and checksums  
- PROV-O JSON-LD block  

---

## 🛡️ 4. Compliance Requirements

All model cards must:

- Pass **KFM-MDP v11** document validation  
- Pass **model_card.schema.json** validation  
- Contain a **PROV-O evidence block**  
- Contain links to experiments that produced the model  
- Include at least one **Explainability (XAI) asset**  
- Declare explicit CARE classification  
- Declare sovereignty implications (if any)  
- Include sustainability telemetry (energy + carbon)

CI will block merges for:

- Missing provenance  
- Missing FAIR+CARE fields  
- Missing training dataset metadata  
- Invalid schema  
- Non-deterministic training logs  
- Omitted XAI evaluations  
- Unclear narrative boundaries (LLM cases)  

---

## 🔗 5. Integration Pipelines

Model cards integrate into:

### 🔹 ETL Pipelines  
Referenced by pipeline configs under:

```
src/pipelines/<domain>/config/*.yaml
```

Ensures models cannot be updated without updating:

- Model version  
- Card version  
- Contract version  

### 🔹 Focus Mode v3  
Models must include:

- Narrative safety policies  
- CARE rules  
- Relationship extraction limits  
- Claims that require verification  

### 🔹 Story Node v3  
Models influencing narrative generation must include:

- Citable sources  
- Narrative constraints  
- Disallowed patterns  
- Sensitive-topic safeguards  

### 🔹 Geospatial / Climate Engines  
Model cards feed:

- Downscaling (BCSD, QM, Hybrid)  
- Hydrology inference (seq2seq, GNNs)  
- Geospatial harmonization  
- Risk surface modeling (hazard layers)  

---

## 📊 6. Telemetry Requirements

All models must have attached energy + carbon telemetry:

```
releases/<version>/mcp-modelcards-telemetry.json
```

Telemetry includes:

- Runtime duration  
- Hardware profile  
- Energy (Wh)  
- Carbon (gCO₂e)  
- Memory/IO footprints  
- GPU/TPU usage  

Used for:

- Sustainability scoring  
- Governance auditing  
- Model efficiency comparison  

---

## 📚 7. Model Card Index (Auto-Generated Friendly)

| Model Name | Version | Domain | CARE Tier | Status |
|-----------|---------|--------|-----------|--------|
| _(none yet)_ | — | — | — | — |

If you want, I can create a **GitHub Action auto-indexer** that populates this table automatically when new model cards are added.

---

## 🕰 8. Version History

| Version | Date | Summary |
|--------:|------|---------|
| v11.0.0 | 2025-11-23 | Initial KFM-MCP v11 model cards index. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — MCP-DL v6.3  
Diamond⁹ Ω / Crown∞Ω Certified · FAIR+CARE Compliant  
Reproducibility · Transparency · Governance

</div>
