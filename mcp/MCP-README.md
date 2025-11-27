---
title: "🧬 Kansas Frontier Matrix — Master Coder Protocol Workspace (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "mcp/README.md"
version: "v11.2.2"
last_updated: "2025-11-27"
review_cycle: "Annual · FAIR+CARE Council & Architecture Board"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-version-sha256>"
doc_integrity_checksum: "<sha256>"
semantic_document_id: "kfm-mcp-root"
doc_uuid: "urn:kfm:mcp:readme:v11.0.0"
event_source_id: "ledger:mcp/README.md"
immutability_status: "version-pinned"

sbom_ref: "../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../releases/v11.2.2/manifest.zip"
telemetry_ref: "../releases/v11.2.2/mcp-telemetry.json"
telemetry_schema: "../schemas/telemetry/mcp-v11.json"
energy_schema: "../schemas/telemetry/energy-v2.json"
carbon_schema: "../schemas/telemetry/carbon-v2.json"

governance_ref: "../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11.0"
pipeline_contract_version: "KFM-PDC v11.0"

status: "Active / Enforced"
doc_kind: "Workspace Overview"
intent: "mcp-workspace-overview"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
classification: "Public Document"
sensitivity: "Low"
fair_category: "F1-A1-I2-R3"
care_label: "Mixed"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 🧬 **Kansas Frontier Matrix — Master Coder Protocol Workspace (v11)**  
`mcp/README.md`  

**Purpose**  
Define the **workspace, workflow, and governance rules** for all Master Coder Protocol (MCP) artifacts in KFM v11 — experiments, SOPs, model cards, lineage bundles, and reproducibility assets.

</div>

---

## 📘 1. Overview — What “MCP” Means in KFM v11

The **Master Coder Protocol (MCP v6.3)** is the **documentation-first, experiment-first, reproducibility-first** framework governing all analytical, scientific, and AI/ML work inside the Kansas Frontier Matrix.

The MCP workspace (`mcp/`) contains:

- 🧪 **Experiments** — deterministic scientific or ML runs  
- 📝 **SOPs** — Standard Operating Procedures for recurring workflows  
- 📄 **Model Cards** — documentation for trained models and explainability results  
- 🧵 **Reproducibility bundles** — configs, seeds, telemetry, lineage  
- 🔗 **OpenLineage + PROV-O** artifacts  
- 🧭 **Governed instructions** for contributors (MCP protocol enforcement)  

The MCP subsystem ensures that **every scientific or computational result can be reproduced, audited, and governed** in accordance with:

- FAIR+CARE  
- Indigenous data sovereignty  
- KFM Ontology v11  
- Story Node v3 / Focus Mode v3 integration  
- OpenLineage v2.5 provenance  
- STAC / DCAT alignment for data-derived outputs  

---

## 🗂 2. Directory Layout — MCP Workspace Structure (Emoji Style A)

```text
mcp/
├── 📄 README.md                  # This document (workspace overview)
│
├── 🧪 experiments/               # All formal experiments logged here
│   ├── 🧪 2025-11-01_CLIMATE-EXP-001.md      # Example experiment (seeded, reproducible)
│   ├── 🧪 2025-11-12_AI-EXP-004.md           # NLP or ML experiments
│   └── 🧪 ...                                # Each experiment is versioned + lineage-bound
│
├── 📋 sops/                      # Standard Operating Procedures
│   ├── 📋 climate_downscaling.md
│   ├── 📋 hydrology_reconstruction.md
│   ├── 📋 storynode_generation.md
│   └── 📋 ai_bias_check.md
│
├── 🧾 model_cards/               # AI/ML model transparency + lineage docs
│   ├── 🧾 climate_anomaly_net_v3.md
│   ├── 🧾 hydrology_seq2seq_v11.md
│   ├── 🧾 focus_mode_transformer_v3.md
│   └── 🧾 ...
│
└── 📘 MCP-README.md              # Core MCP-DL v6.3 protocol reference (the “MCP bible”)
```

The MCP filesystem is structured to be **machine-indexable**, **graph-safe**, and **CI-enforced**.

---

## 🧪 3. Experiments — Scientific Reproducibility at Scale

All experiments must follow MCP-DL v6.3 and KFM-MDP v11.2.2.

### 3.1 Required Sections

Each experiment file MUST include (at minimum):

- **Objective / Hypothesis**  
- **Background & references** (including dataset and model references)  
- **Methods**  
  - data sources + versions (STAC/DCAT IDs)  
  - configs, seeds, hyperparameters  
  - pipeline code + environment details  
- **Execution logs** (summary; full logs stored separately if large)  
- **Results** (tables, plots, metrics)  
- **Analysis & interpretation**  
- **Limitations**  
- **Next steps**  
- **Provenance** (PROV-O + OpenLineage links)  
- **FAIR+CARE review** (critical for sensitive domains)  

### 3.2 Metadata Requirements

Each experiment MUST declare:

- Dataset versions (STAC/DCAT refs)  
- Seeds used for deterministic runs  
- Model version / config hash  
- Pipeline contract version (`KFM-PDC v11`)  
- Hardware metadata (CPU/GPU, region)  
- Energy/Carbon telemetry (via `energy_schema`, `carbon_schema`) where applicable  

This ensures transparency across climate, hydrology, NLP, geospatial, and simulation experiments.

---

## 📋 4. SOPs — Repeatable, Governed Procedures

**SOPs** define **canonical, repeatable tasks**, including but not limited to:

- Climate anomaly downscaling  
- Streamflow reconstruction and gap-filling  
- Story Node generation (human-in-the-loop AI)  
- H3 masking of sensitive archaeological and cultural sites  
- Cleaning legacy historical datasets (OCR → structured)  
- Geospatial harmonization workflows (CRS, grid, and tiling conventions)  

Each SOP MUST:

- Use the MCP template:
  - **Purpose**  
  - **Inputs** (data, parameters, contracts)  
  - **Procedure** (step-by-step)  
  - **Verification & validation**  
  - **Failure modes & mitigation**  
  - **Lineage & governance references**  
- Be versioned (front-matter + in-text history)  
- Refer to relevant:
  - data contracts  
  - STAC/DCAT schemas  
  - FAIR+CARE and sovereignty policies  

---

## 🧾 5. Model Cards — Transparency for All AI Models

Every AI/ML model in KFM MUST have a **model card** in `mcp/model_cards/` describing:

- Model architecture & objectives  
- Training and evaluation datasets (with FAIR+CARE considerations)  
- Seeds, hyperparams, major config choices  
- Training/evaluation pipeline (DAG, tools, hardware)  
- Metrics (accuracy/F1/MSE/etc.) across relevant groups  
- Limitations and known biases  
- CARE rules (what outputs are disallowed, when to mask)  
- Explainability results (SHAP/LIME, attention, counterfactuals)  
- Provenance:
  - OpenLineage activity chain IDs  
  - Git commit + environment  
- Deployment/usage boundaries:
  - `allowed_use_cases` vs `prohibited_use_cases`  

Model cards are **primary documentation** for models used in:

- Focus Mode v3  
- AI geospatial inference  
- Climate/hydrology reconstruction  
- NLP over archives and historical documents  

---

## 🔗 6. Provenance, Lineage & OpenLineage v2.5

All MCP artifacts MUST write lineage using:

- **PROV-O**  
  - `prov:Activity` for experiments, training runs, and major steps  
  - `prov:Entity` for datasets, models, configs, and outputs  
  - `prov:Agent` for people, bots, CI jobs  

- **OpenLineage v2.5**  
  - Standard `job` and `run` fields  
  - Input/output dataset definitions  
  - KFM-specific facets for:
    - CARE classification  
    - Sovereignty flags  
    - Energy/carbon metrics  

KFM-specific extensions:

- STAC/DCAT dataset mapping fields  
- H3 masking metadata for sensitive geometry  
- Story Node & Focus Mode references for narrative-based outputs  

All pipelines in `src/pipelines/**` that are under MCP control must:

- Emit OpenLineage events  
- Produce PROV-O RDF/JSON-LD fragments  
- Include experiment, SOP, and model card IDs in metadata  

---

## ⚙️ 7. CI/CD Enforcement — MCP Validation Workflows

`.github/workflows/mcp-validate.yml` and related jobs enforce:

- KFM-MDP v11.2.2 markdown & metadata rules in `mcp/**`  
- MCP experiment schema (via JSON Schema & SHACL)  
- Model card schema compliance  
- SOP format & completeness  
- Lineage completeness (e.g., no “orphan” experiments without dataset refs)  
- FAIR+CARE validations (sensitive experiments MUST be tagged/approved)  
- Prohibited content checks (no raw sensitive coordinates or ungoverned archives)  

**No experiment or model card can be merged** unless **all** validations pass.

---

## 🧭 8. Integration with Story Nodes & Focus Mode

MCP outputs directly feed KFM’s narrative engines:

### 8.1 Story Nodes v3

- Story Nodes referencing scientific conclusions must:
  - Cite experiment IDs (`mcp/experiments/**`)  
  - Reference model cards where AI is involved  
  - Embed temporal and spatial context from MCP metadata  

- Narrative claims must be:
  - Traceable to experiments or authoritative references  
  - Governed by FAIR+CARE and sovereignty rules  

### 8.2 Focus Mode v3

- Uses MCP outputs to:

  - Provide scientifically accurate context for:
    - Climate anomalies  
    - Hydrology reconstructions  
    - Historical reconstructions  
    - Cultural landscape narratives  

- Focus Mode v3 explainability panels may:
  - Link directly to model cards  
  - Visualize XAI artifacts (e.g., SHAP bar plots)  
  - Show provenance/lineage chain fragments  

This ensures narrative layers are **grounded**, **explainable**, and **governed**.

---

## 📊 9. Telemetry & Sustainability — MCP-Level Metrics

All MCP workflows (experiments, training, evaluations, audits) MUST capture:

- `energy_wh` — energy used (per run or batch)  
- `carbon_gco2e` — estimated CO₂-equivalent  
- `runtime_sec` — execution runtime  
- `io_bytes_read`, `io_bytes_written` (where available)  
- `records_processed` — data volume indicator  

Telemetry is aggregated into:

```text
../releases/<version>/mcp-telemetry.json
docs/reports/telemetry/mcp/*.json
```

and used for:

- Sustainability dashboards and reports  
- Governance board reviews of computational footprint  
- Optimization of experiments and model training strategies  

---

## 📐 10. MCP & Standards Interoperability

MCP artifacts must align with:

- **DCAT 3.0** — experiments and model outputs as datasets/distributions  
- **ISO 19115** — metadata lineage for spatial & environmental data  
- **STAC 1.x** — for experiment-generated spatial outputs  
- **PROV-O** and **OpenLineage** — full lifecycle provenance  

Where possible, experiments and model cards should include:

- `dcat:Dataset` references for key derived datasets  
- `stac_ref` fields for spatial outputs  
- `prov:Activity` IDs mapping to OpenLineage job/run IDs  

---

## 🕰 11. Version History

| Version | Date       | Summary                                                                                             |
|--------:|-----------:|-----------------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-27 | Upgraded to KFM-MDP v11.2.2; added emoji directory layout; clarified CI enforcement & sustainability telemetry. |
| v11.0.0 | 2025-11-23 | Initial MCP workspace overview for KFM v11; defined experiments, SOPs, model cards, and lineage rules. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
🧬 Master Coder Protocol Workspace · MCP-DL v6.3 · KFM-MDP v11.2.2 · Diamond⁹ Ω / Crown∞Ω  

[⬅️ Back to Root](../README.md) · [📘 MCP Protocol](MCP-README.md) · [🛡 Governance Charter](../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>