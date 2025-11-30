---
title: "🧬 KFM v11 — Embeddings Training Datasets Framework (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/pipelines/ai/training/embeddings/datasets/README.md"
version: "v11.2.3"
last_updated: "2025-11-29"

release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Embeddings Working Group · FAIR+CARE Council"
content_stability: "stable"
status: "Active / Enforced"

commit_sha: "<latest-commit>"
previous_version_hash: "<previous-version-hash>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../../../../../releases/v11.2.3/manifest.zip"
attestation_ref: "../../../../../../releases/v11.2.3/slsa-attestation.json"
signature_ref: "../../../../../../releases/v11.2.3/signature.sig"

telemetry_ref: "../../../../../../releases/v11.2.3/embeddings-training-datasets-telemetry.json"
telemetry_schema: "../../../../../../schemas/telemetry/ai-training-embeddings-datasets-v11.json"
energy_schema: "../../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"

doc_kind: "Dataset Group"
intent: "embeddings-training-datasets"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Compliant · Sensitive-Content Screening"

classification: "Public (Governed)"
sensitivity: "Moderate (semantic embeddings across climate/archaeology/hydro/soil domains)"
machine_extractable: true
jurisdiction: "United States · Kansas"
accessibility_compliance: "WCAG 2.1 AA+"
---

<div align="center">

# 🧬 **KFM v11 — Embeddings Training Datasets Framework**  
`docs/pipelines/ai/training/embeddings/datasets/`

**Purpose**  
Define the **governed v11 dataset framework** for all embedding-model training pipelines in KFM,  
including domain embeddings (climate, soil, hydrology, archaeology), cross-domain semantic  
embeddings, STAC/DCAT-text embeddings, Story Node embeddings, and contextual embeddings  
used by Focus Mode v3 and KFM’s semantic search engines.

This module specifies ingestion, validation, provenance, FAIR+CARE alignment,  
sustainability, and ethics gating for all embedding datasets.

</div>

---

## 📘 1. Overview

Embedding models require **large, diverse, high-quality corpora**, including:

- **Geospatial text** (metadata, STAC Items, DCAT datasets, provenance bundles)  
- **Scientific/technical text** (climate, hydrology, soil, ecology, remote sensing)  
- **Environmental observations** (logs, explanations, climate model summaries)  
- **Training-time Story Nodes**  
- **Semantic documentation** (pipeline specs, lineage, governance)  
- **AI explainability summaries** (SHAP/IG narratives)  
- **Synthetic augmentation rules** (while governed & ethics-checked)

This document defines standards for **collecting, filtering, de-duplicating, validating**,  
and **ethically transforming** embeddings input datasets.

---

## 🗂️ 2. Directory Layout (Emoji-Prefix Standard)

~~~text
docs/pipelines/ai/training/embeddings/datasets/
├── 📄 README.md
│
├── 📁 text/                                 # Text corpora for embeddings
│   ├── 📄 README.md
│   ├── 📝 stac-metadata/                     # STAC/DCAT textual metadata
│   ├── 📝 story-nodes/                       # Story Node narrative sources
│   ├── 📝 climate/                           # Climate scientific text
│   ├── 📝 hydrology/                         # Watershed/hydrology text
│   ├── 📝 soil/                              # Soil/terrain documentation
│   ├── 📝 archaeology/                       # Archaeology domain text (screened)
│   └── 📝 misc/                              # Additional domain-safe sources
│
├── 📁 numeric/                              # Embedding contexts requiring numerical → textual conversion
│   ├── 📄 README.md
│   ├── 🔢 climate-summaries/
│   ├── 🔢 soil-hydro-indicators/
│   └── 🔢 hazard-profiles/
│
├── 📁 stac/                                 # STAC item/collection embeddings
│   ├── 📄 README.md
│   ├── 🌐 collections/
│   └── 🌐 items/
│
├── 📁 provenance/                           # Text from PROV-O, OpenLineage, DCAT metadata
│   ├── 📄 README.md
│   ├── 🧾 prov-o/
│   ├── 📡 openlineage/
│   └── 📚 dcat/
│
├── 📁 governance/                           # Ethics, FAIR+CARE policies as embedding corpora
│   ├── 📄 README.md
│   ├── ⚖️ faircare/
│   ├── ⚖️ sovereignty/
│   └── ⚖️ licensing/
│
├── 📁 validation/                           # Screens for safe embeddings
│   ├── 📄 validate-corpus-integrity.md
│   ├── 📄 validate-sensitive-content.md
│   ├── 📄 validate-faircare.md
│   └── 📄 validate-governance-alignment.md
│
└── 📊 examples/                             # Example embedding corpora (sanitized)
    ├── 📁 climate/
    ├── 📁 hydrology/
    ├── 📁 soil/
    ├── 📁 archaeology/
    └── 📁 stac/
~~~

---

## 🧬 3. Dataset Standards (v11)

### Required Metadata

| Field | Required | Description |
|-------|---------|-------------|
| `dataset_id` | ✔ | Unique ID for embedding dataset |
| `version` | ✔ | Version of the embedding dataset |
| `kfm:domain` | ✔ | climate, soil, hydro, archaeology, general |
| `temporal_coverage` | ✔ | Relevant years/time periods |
| `source_list` | ✔ | List of upstream data sources |
| `provenance` | ✔ | PROV-O lineage |
| `openlineage` | ✔ | Dataset creation lineage |
| `kfm:sensitivity_flag` | ✔ | CARE/sovereignty sensitivity |
| `validation_log` | ✔ | Results of corpus & ethics checks |
| `kfm:energy_wh` | ✔ | Compute cost to produce dataset |
| `kfm:carbon_gco2e` | ✔ | Sustainability impact |
| `stac_collection` | ✔ | STAC metadata |

### Governance Requirements

- No sensitive archaeological coordinates  
- All tribal/sovereignty text screened per CARE rules  
- No GPL/CC-NC/closed-source license contamination  
- Synthetic augmentation rules MUST be documented  
- Text from restricted datasets must be redacted or excluded  

### Dataset Form

- `.parquet` (preferred)  
- `.jsonl` (for text corpora)  
- `.txt` (only for raw governance-approved blocks)  
- Zarr (optional for hybrid numeric/semantic models)  

---

## 🧪 4. Validation Requirements (v11)

Validation MUST check:

### ✔ Corpus Integrity
- Deduplication  
- Noise removal  
- Encoded metadata accuracy  
- Maximum token limits  

### ✔ Sensitive Content Screening
- Removal of tribal/sensitive archaeological descriptions  
- Masking of watershed/soil units if needed for sovereignty  
- Climate hazard communication checks (risk metadata)

### ✔ FAIR+CARE Governance
- Provenance completeness  
- Licensing compliance  
- Ethics model (ACES) alignment  

### ✔ Sustainability
- Telemetry exported for ingestion  
- Dataset creation carbon footprint logged  

---

## 🌐 5. Provenance Requirements

Embedding datasets must include:

### PROV-O
- Activity = embedding dataset assembly  
- Used = source textual corpora  
- Generated = embedding dataset artifact  
- Agent = KFM pipeline or reviewer  

### OpenLineage
- runId  
- Input sources  
- Output dataset pointers  
- Sustainability facets  

### STAC
- Collection + Items  
- Domain assignment  
- Asset list  
- Temporal + spatial coverage (if applicable)

---

## 📚 6. Types of Embeddings Training Datasets

### Domain-Specific
- Climate  
- Hydrology  
- Soil & terrain  
- Archaeology (with strict CARE filtering)

### Cross-Domain Unified Corpora
- Scientific metadata from climate–soil–hydro interactions  
- Story Nodes & explainability narratives  
- Pipeline specifications + model cards  

### Numeric-Semantic Hybrids
- Structured climate summaries → textual embeddings  
- Soil/hydrology numeric validators → semantic descriptions  

### Governance/Ethics Embeddings
- FAIR+CARE  
- Sovereignty rules  
- Licensing requirements  

---

## 📡 7. Telemetry & Sustainability

Embedding dataset creation MUST emit:

- `kfm.energy_wh`  
- `kfm.carbon_gco2e`  
- `kfm.records_processed`  
- `cpu_pct`, `gpu_pct`, `ram_mb`  
- Tokenization + preprocessing stats  

Telemetry events go to:

`releases/v11.2.3/embeddings-training-datasets-telemetry.json`

---

## 🔮 8. Story Node Integration (Focus Mode v3)

Embedding datasets produce Story Nodes describing:

- What corpus was used  
- Which domains the model learns from  
- What CARE filters were applied  
- Provenance & license rules  
- Sustainability cost  
- Dataset lineage narrative  

These feed into the **Embeddings Explorer** in Focus Mode.

---

## 🧭 9. Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v11.2.3 | 2025-11-29 | Initial v11 embeddings training dataset specification; lineage + CARE + sustainability integrated. |

---

<div align="center">

🧬 **Kansas Frontier Matrix — Embeddings Training Datasets (v11.2.3)**  
Semantic · Ethical · Sustainable · Provenance-Grounded  

[📘 Docs Root](../../../../../..) • [🧠 Embeddings Training Pipelines](../README.md) • [🛡 Governance](../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>