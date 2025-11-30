---
title: "🧬🧠 KFM v11 — Embeddings Training Explainability Framework (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/pipelines/ai/training/embeddings/explainability/README.md"
version: "v11.2.3"
last_updated: "2025-11-29"

release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Embeddings Working Group · FAIR+CARE Council"
content_stability: "stable"
status: "Active / Enforced"

commit_sha: "<latest-commit>"
previous_version_hash: "<previous-version-sha>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../../../../../releases/v11.2.3/manifest.zip"
attestation_ref: "../../../../../../releases/v11.2.3/slsa-attestation.json"
signature_ref: "../../../../../../releases/v11.2.3/signature.sig"

telemetry_ref: "../../../../../../releases/v11.2.3/embeddings-training-explainability-telemetry.json"
telemetry_schema: "../../../../../../schemas/telemetry/ai-training-embeddings-explainability-v11.json"
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

doc_kind: "Explainability Module"
intent: "embeddings-training-explainability"
fair_category: "F1-A1-I1-R2"
care_label: "CARE-Compliant · Sensitive-Content-Aware"

classification: "Public (Governed)"
sensitivity: "Moderate (cross-domain semantic explainability)"
machine_extractable: true
jurisdiction: "United States · Kansas"
accessibility_compliance: "WCAG 2.1 AA+"
---

<div align="center">

# 🧬🧠 **Embeddings Training Explainability Framework (KFM v11)**  
`docs/pipelines/ai/training/embeddings/explainability/`

**Purpose**  
Define the **v11 governed explainability framework** for embedding-model training pipelines,  
including semantic attribution, neighborhood explainability, contrastive attribution,  
cross-domain concept explanation, and JSON-LD explainability metadata used throughout  
KFM’s semantic search, Focus Mode v3, and Knowledge Graph pipelines.

</div>

---

## 📘 1. Overview

Embedding models learn semantic structure across multiple domains in KFM:

- Climate (CAMS/ERA5/HRRR text + metadata)  
- Hydrology (watersheds, runoff, soil–water interactions)  
- Soil & Terrain  
- Archaeology (CARE-screened summaries only)  
- Governance metadata (FAIR+CARE, sovereignty, lineage)  
- STAC/DCAT metadata corpora  
- Story Nodes & explainability narratives  

Explainability is needed to:

- Understand **why embeddings cluster entities together**  
- Detect **semantic drift** across dataset updates  
- Interpret **multimodal linkage** (text ↔ metadata ↔ numeric summaries)  
- Provide **Focus Mode narratives** rooted in embedding semantics  
- Guarantee **ethical + safe reasoning** via CARE filtering  

This module provides v11 rules for generating and validating semantic explainability artifacts.

---

## 🗂️ 2. Directory Layout (Emoji-Prefix Standard)

~~~text
docs/pipelines/ai/training/embeddings/explainability/
├── 📄 README.md
│
├── 🔍 semantic-attribution/                # Feature- or token-level attribution
│   ├── 📄 README.md
│   ├── 🧠 templates/
│   ├── 🌐 stac/
│   ├── 🔗 lineage/
│   ├── 🧪 validation/
│   └── 📊 examples/
│
├── 🧭 neighborhood/                        # Nearest-neighbor explanation modules
│   ├── 📄 README.md
│   ├── 🧠 templates/
│   ├── 🌐 stac/
│   ├── 🔗 lineage/
│   ├── 🧪 validation/
│   └── 📊 examples/
│
├── 🔍 cross-domain/                        # Climate↔Soil↔Hydro↔Archaeology explainability
│   ├── 📄 README.md
│   ├── 🧠 templates/
│   ├── 🌐 stac/
│   ├── 🔗 lineage/
│   ├── 🧪 validation/
│   └── 📊 examples/
│
├── 📚 jsonld/                              # JSON-LD explainability metadata
│   ├── 📄 README.md
│   ├── 📁 context/
│   ├── 🧠 templates/
│   ├── 🔗 lineage/
│   ├── 🧪 validation/
│   └── 📊 examples/
│
└── 📦 examples/                             # High-level example sets
    ├── 📁 semantic/
    ├── 📁 neighborhood/
    ├── 📁 cross-domain/
    └── 📁 jsonld/
~~~

---

## 🧬 3. Explainability Standards (v11)

### Required Metadata for Semantic Explainability

| Field | Required | Description |
|-------|---------|-------------|
| `model:version` | ✔ | Embedding model version |
| `dataset_id` | ✔ | Dataset used during training |
| `kfm:domain` | ✔ | climate / hydro / soil / archaeology / general |
| `kfm:explainability_method` | ✔ | semantic-attribution / neighborhood / cross-domain |
| `datetime` | ✔ | Explainability timestamp |
| `kfm:sensitivity_flag` | ✔ | CARE/sovereignty indicator |
| `kfm:energy_wh` | ✔ | Energy usage |
| `kfm:carbon_gco2e` | ✔ | Sustainability cost |
| `prov:*` | ✔ | PROV-O lineage |
| `openlineage:*` | recommended | Evaluation lineage |
| `crs` | conditional | Required for spatial semantic embedding explainers |
| `kfm:h3_res` | conditional | For H3-based spatial attribution |

### Required Explainability Outputs

- Attribution vectors (token-level or concept-level)  
- Semantic neighborhoods  
- Cross-domain alignment maps  
- JSON-LD explainability metadata  
- STAC Item + Collection metadata  
- Provenance bundles (OpenLineage + PROV-O)  
- Sustainability telemetry  

---

## 🧪 4. Validation Requirements (v11)

### ✔ Semantic Integrity  
- Token- and concept-level scores finite  
- Dimensionally consistent attribution vectors  
- Valid vocabulary mappings  
- No leakage of sensitive text  

### ✔ Cross-Domain Integrity  
- Climate ↔ hydro ↔ soil ↔ archaeology embeddings consistent  
- No improper merging of sensitive archaeology text  
- Ontology alignment verified  

### ✔ FAIR+CARE Compliance  
- Sensitive cultural/tribal text masked  
- Governance-aligned filtering applied  
- Ethics block in explainability JSON-LD  

### ✔ Sustainability  
- Energy/carbon < explainability budget  
- Logged into telemetry package  

### ✔ Provenance  
- Complete PROV-O chain  
- Matching OpenLineage run  
- Accurate dataset→model→explainability mapping  

Failures → rollback or ethics review.

---

## 🌐 5. STAC + JSON-LD Integration

Each explainability artifact MUST include:

### STAC Item  
- `datetime`  
- Explainability assets (vectors, heatmaps, json)  
- Provenance links  
- Energy/carbon metadata  
- CARE classification  

### JSON-LD Explainability  
- Semantic graph structure  
- Variable/feature vocab mapping  
- Domain alignment (climate/hydro/soil/etc.)  
- PROV-O embedded block  

---

## 🔗 6. Provenance (PROV-O + OpenLineage)

Each explainability run MUST capture:

- `prov:Activity` — explainability computation  
- `prov:used` — training dataset + model artifact  
- `prov:generated` — semantic attribution artifacts  
- `prov:wasAssociatedWith` — agent  

OpenLineage data SHOULD include:

- `runId`  
- Input datasets  
- Output explainability artifacts  
- Telemetry facets  

---

## 📡 7. Telemetry (OTel v11)

Embedded explainability MUST emit:

- `kfm.expl_method="embeddings"`  
- `kfm.expl_energy_wh`  
- `kfm.expl_carbon_gco2e`  
- `kfm.expl_latency_ms`  
- CPU/GPU utilization  
- Tokens processed  
- Drift metrics (semantic drift across versions)

Telemetry is written into:

`releases/v11.2.3/embeddings-training-explainability-telemetry.json`

---

## 🔮 8. Story Node Integration (Focus Mode v3)

Explainability outputs generate Story Nodes on:

- Embedding behavior  
- Domain influence  
- Climate ↔ hydro ↔ soil ↔ archaeology semantic connections  
- Sensitive content filtering  
- Cross-version drift  
- Provenance & sustainability  

These drive **Embedding Explainability Explorer** features.

---

## 🧭 9. Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v11.2.3 | 2025-11-29 | Initial v11 embeddings training explainability framework; CARE + STAC + lineage integrated. |

---

<div align="center">

🧬🧠 **Kansas Frontier Matrix — Embeddings Training Explainability (v11.2.3)**  
Explainable · Ethical · Semantic · FAIR+CARE · Provenance-Driven  

[📘 Docs Root](../../../../../..) • [🧬 Embeddings Training Pipelines](../README.md) • [🛡 Governance](../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>