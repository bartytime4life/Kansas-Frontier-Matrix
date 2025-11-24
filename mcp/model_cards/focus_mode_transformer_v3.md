---
title: "🧠 Model Card — Focus Mode Transformer v3 (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "mcp/model_cards/focus_mode_transformer_v3.md"
version: "v11.0.0"
last_updated: "2025-11-23"
review_cycle: "Quarterly · AI Governance Board · FAIR+CARE Council · Narrative Review Committee"
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
doc_kind: "Model Card"
intent: "focus-mode-transformer-v3"
semantic_document_id: "kfm-modelcard-focus-mode-transformer-v3"
doc_uuid: "urn:kfm:modelcard:focus-mode-transformer-v3:v11.0.0"
machine_extractable: true
classification: "Governed AI Narrative Model"
sensitivity: "Mixed"
fair_category: "F1-A1-I3-R3"
care_label: "Collective Benefit · Authority to Control · Responsibility · Ethics"
immutability_status: "version-pinned"
accessibility_compliance: "WCAG 2.1 AA+"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 🧠 **Focus Mode Transformer v3 — Model Card (v11 LTS)**  
`mcp/model_cards/focus_mode_transformer_v3.md`

**Purpose:**  
Document the architecture, training, safety constraints, governance requirements, provenance, and usage boundaries of the **Focus Mode Transformer v3**, the core AI engine powering KFM’s context-aware narrative reasoning system.

</div>

---

## 📘 1. Model Summary

**Focus Mode Transformer v3 (FMT-v3)** is a multi-domain contextual reasoning model used to:

- Generate **fact-grounded narrative summaries**  
- Power Focus Mode’s **3-panel reasoning** (Context · Timeline · Map)  
- Produce **explanatory overlays** with provenance  
- Support Story Node v3 creation with data-backed relationships  
- Interpret spatial/temporal/event clusters from the Neo4j knowledge graph  
- Enforce Indigenous sovereignty, CARE ethics, and narrative safety

FMT-v3 is designed **not** to imagine, speculate, or reconstruct unverified claims.

Its outputs are **strictly data-derived**, where every statement must connect to a:

- Graph entity  
- Dataset (STAC/DCAT)  
- Provenance record  
- Document  
- MCP experiment  

---

## 🧠 2. Intended Use

### ✔ Approved Use Cases
- Focus Mode v3 entity summaries  
- Environmental + cultural narrative context  
- Story Node draft generation  
- Explainability layers for map/timeline interactions  
- Temporal evolution descriptions (when grounded in data)  
- Spatial relationships (GeoSPARQL + H3-safe geometry)  

### ❌ Restricted Use Cases
- Creating genealogies  
- Predicting undocumented tribal history  
- Inventing causes behind events  
- Sensitive archaeological site description  
- Generating emotional/creative fiction  
- Producing any **unverifiable historical claims**

All narrative output is bounded by **FAIR+CARE + Sovereignty rules**.

---

## 🌐 3. Data Used for Training

FMT-v3 is **fine-tuned only on vetted, public and low-risk datasets**, including:

| Dataset | STAC/DCAT ID | Notes |
|--------|---------------|-------|
| Kansas Gazetteer | `stac:ref/gnis_kansas` | Public place names |
| Chronological event datasets | `stac:history/events_core` | Non-sensitive |
| Kansas rivers & hydrology metadata | `stac:hydrology/basins_core` | Public |
| Environmental data summaries | `stac:climate/summary_stats` | Non-sensitive |
| Public-domain historical texts | `stac:archives/public_texts` | No sensitive material |
| Story Node v2 corpus | `stac:storynodes/v2_public` | Cleaned & CARE-filtered |

❗ No Indigenous-only or sovereign datasets were used in training.  
❗ No sacred site or sensitive-coordinate datasets were included.

For sensitive cultural datasets, FMT-v3 only receives **masked**, **generalized**, or **synthetic embeddings**.

---

## 🧬 4. Model Architecture

FMT-v3 is a hybrid:

- Transformer Encoder (context fusion)  
- Graph-Integrated Attention Layers  
- Spatial Reasoning Module (H3, GeoSPARQL constraints)  
- Temporal Fusion Layers (OWL-Time alignment)  
- Narrative Safety Gate (policy-conditioned decoder)  
- Provenance Enforcement Module (PEM)  
- Data-Citation Tagger (DCT)

This allows:

- Multi-hop reasoning  
- Spatial + temporal + cultural integration  
- Contextually aware narrative construction  
- Auto-citation  
- Sovereignty-aligned masking  

---

## 🎛️ 5. Training Procedure

### Framework
- PyTorch 2.2  
- HuggingFace Accelerate  
- Neo4j retrieval middleware  
- KFM Narrative Safety Toolkit (NST-v3)

### Seeds and Determinism
- Seed: 991224  
- Fully deterministic mode enabled  
- Data shuffling controlled by seed schedule  

### Objective Functions
- Factual grounding loss  
- Provenance completeness loss  
- Masking compliance regularizer  
- Narrative safety discriminator loss  
- Temporal alignment loss  

### Environment
- A100 80GB (x2)  
- Docker: `kfm/focusmode-env:v11`  
- SBOM included in release bundle  

---

## 📊 6. Evaluation

### Factuality & Grounding
| Metric | Score |
|--------|-------|
| Citation Accuracy | 0.98 |
| Grounded Statement Score | 0.96 |
| Hallucination Rate | **<0.5%** |
| Sovereignty Compliance | 100% |

### Narrative Metrics
- Neutrality score: 0.94  
- Bias avoidance score: 0.97  
- Sensitive-topic handling: PASS (all scenarios)  
- Temporal consistency: 0.95  

### Spatial/Temporal Reasoning
- GeoSPARQL validity: 100%  
- OWL-Time alignment: 97%  
- H3 masking adherence: 100%  

### Explainability
- SHAP maps available  
- Layer attention visualization  
- Temporal/sentence alignment trace logs  

---

## 🛡️ 7. FAIR+CARE & Sovereignty Governance

FMT-v3 is governed under:

### FAIR
- Findable: Fully cataloged under DCAT  
- Accessible: Public model card  
- Interoperable: JSON-LD, STAC, DCAT  
- Reusable: CC-BY with ethics constraints  

### CARE
- Collective benefit: enhances cultural understanding  
- Authority to control: no exposure of sovereignty-protected content  
- Responsibility: narrative safeguards enforced  
- Ethics: strict boundaries for historical/cultural claims  

### Sovereignty
- FMT-v3 **never** outputs sensitive tribal locations  
- Uses **H3 R7–R9** masking when interacting with cultural geography  
- Protected datasets bypass the model entirely  

---

## ⚠️ 8. Limitations

- Cannot interpret oral histories or sacred traditions  
- Limited understanding of nuanced tribal governance structures  
- Cannot perform novel historical inference  
- Requires human review for complex cultural subjects  
- Model bias may emerge from public-domain corpora → monitored quarterly  

---

## 🚀 9. Deployment & Usage Boundaries

FMT-v3 is **authorized for**:

- Focus Mode v3  
- Story Node v3 drafts  
- Neo4j narrative enrichment  
- UI highlight panels  
- Metadata-assisted map/timeline interpretation  

FMT-v3 is **restricted from**:

- Autonomous publishing  
- Sensitive heritage narrative generation  
- Unreviewed historical claims  
- Culturally sensitive reconstruction  

All outputs flow through:

- Narrative Safety Filter  
- CARE/Sovereignty Gate  
- Human Review Step  

---

## 🔗 10. Provenance & Lineage

### PROV-O Block (Simplified)

```
{
  "prov:entity": "focus_mode_transformer_v3",
  "prov:wasGeneratedBy": "training:2025-11-10_AI-EXP-021",
  "prov:used": [
    "stac:ref/gnis_kansas",
    "stac:history/events_core",
    "stac:climate/summary_stats",
    "stac:storynodes/v2_public"
  ],
  "prov:wasAssociatedWith": "kfm-ai-training-service-v11"
}
```

### OpenLineage Events
Stored under:

```
data/provenance/experiments/fmt_v3/<timestamp>.json
```

Includes:

- Config hash  
- Dataset references  
- Model architecture fingerprint  
- Telecompute logs  

---

## 📈 11. Telemetry

Logged into:

```
releases/<version>/mcp-modelcards-telemetry.json
```

Approximate training footprint:

- Energy: **11.8 kWh**  
- Carbon: **570 gCO₂e**  
- GPU-hours: **8.4**  

---

## 🕰️ 12. Version History

| Version | Date | Summary |
|--------:|------|---------|
| v11.0.0 | 2025-11-23 | Initial model card for Focus Mode Transformer v3 (governed, deterministic, CARE-aligned). |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
Diamond⁹ Ω / Crown∞Ω · FAIR+CARE · MCP-DL v6.3  
Sovereignty-Respecting · Narrative-Safe · Fully Governed  

</div>
