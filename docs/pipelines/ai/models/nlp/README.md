---
title: "📝 KFM v11.2.2 — NLP Model Family (Entity Extraction · OCR · Text Classification · Narrative Reasoning)"
path: "docs/pipelines/ai/models/nlp/README.md"
version: "v11.2.2"
last_updated: "2025-11-28"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · NLP Working Group · FAIR+CARE Council"
content_stability: "stable"

status: "Active / Enforced"
doc_kind: "Model Family"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../releases/v11.2.2/ai-models-nlp-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/ai-models-nlp-v11.2.2.json"
energy_schema: "../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"
data_contract_ref: "../../../../contracts/data-contract-v3.json"

license: "CC-BY 4.0"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Medium-Risk"
sensitivity: "Text-Model"
sensitivity_level: "Medium"
public_exposure_risk: "Moderate"
immutability_status: "version-pinned"

semantic_intent:
  - "nlp-models"
  - "entity-extraction"
  - "ocr"
  - "text-classification"
  - "embeddings"
  - "narrative-ai"
  - "story-node-nlp"
  - "focus-mode"

scope:
  domain: "ai-models-nlp"
  applies_to:
    - "model-cards"
    - "training-metadata"
    - "evaluation-bundles"
    - "entity-extraction"
    - "token-classification"
    - "text-classification"
    - "ocr-pipelines"
    - "nlp-explainability"
    - "story-node-nlp"
    - "focus-mode-nlp"
    - "provenance"
    - "sensitive-term-governance"

layout_profiles:
  - "immediate-one-branch-with-descriptions-and-emojis"

requires_purpose_block: true
requires_directory_layout_section: true
requires_version_history: true
requires_governance_links_in_footer: true

diagram_profiles:
  - "mermaid-flowchart-v1"
  - "mermaid-timeline-v1"
---

<div align="center">

# 📝 **KFM v11.2.2 — NLP Model Family**  
`docs/pipelines/ai/models/nlp/README.md`

**Purpose:**  
Define and govern all **NLP models** used in KFM for entity extraction, OCR, text classification, embeddings, semantic grounding, and narrative reasoning.  
These models provide **critical linguistic structure** for Story Node generation, graph entities (CIDOC-CRM), Focus Mode v3 semantic windows, and controlled narrative generation.

</div>

---

## 📘 Overview

NLP models in KFM cover:

- Named Entity Recognition (NER)  
- Geoparsing, geotemporal extraction  
- OCR → text normalization pipelines  
- Text classification (hazard mentions, hydrology, archaeology, climate)  
- Sentence/document embeddings  
- Semantic search  
- Narrative reasoning kernels used by Focus Mode v3  

NLP outputs feed:

- **Neo4j graph entities**  
- **STAC Items containing extracted geo/time metadata**  
- **Story Node v3 narrative fields**  
- **Focus Mode evidence fusion**  
- **Explainability overlays**  

Every model must include:

- Model Card v11.2.2  
- Training metadata bundle  
- Evaluation suite  
- Explainability vectors (attention maps / attribution)  
- CARE masking logic for sensitive content  

---

## 🗂 Directory Layout (v11.2.2)

    docs/pipelines/ai/models/nlp/
    ├── 📄 README.md                              # This file
    │
    ├── 📄 model-card.jsonld                      # Model Card v11.2.2
    ├── 📄 training-metadata.json                 # Hyperparameters, datasets, seeds
    ├── 📄 evaluation-report.md                   # Precision/recall/F1 + regression tests
    ├── 📄 explainability.json                    # Attention maps, attribution vectors
    │
    ├── 📁 examples/                              # Example extractions + narratives
    │   ├── 📄 ner-example.json
    │   ├── 📄 ocr-cleaned-text.md
    │   ├── 📄 geoparse-output.json
    │   └── 📄 narrative-example.md
    │
    ├── 📁 stac/                                  # STAC metadata templates for NLP outputs
    │   ├── 📄 nlp-item.json
    │   └── 📄 assets-template.json
    │
    └── 📁 mlops/                                 # Deployment + drift detection
        ├── 📄 inference-config.yaml
        ├── 📄 sensitive-term-policy.md
        └── 📄 drift-monitoring.md

---

## 🧬 NLP Model Categories

### 1. 🔍 Named Entity Recognition (NER)
Extract:

- Places  
- People  
- Organizations  
- Dates/time ranges  
- Tribal nations (subject to CARE masking rules)  
- Historic events  

NER MUST:

- Output CIDOC-CRM entity-compatible IDs  
- Provide provenance for each recognized entity  
- Enforce CARE masking on heritage or sensitive identities  

---

### 2. 🌐 Geoparsing & Geotemporal Extraction

- Convert text mentions into GNIS / KFM place IDs  
- Extract temporal windows  
- Produce Story Node v3 structural fields  
- Attach uncertainty metrics  

STAC mapping required for:

- GeoJSON footprints  
- Temporal intervals (`time:ProperInterval`)  

---

### 3. 📄 OCR Pipelines

OCR models MUST:

- Normalize text  
- Remove artifacts + handle historic fonts  
- Provide uncertainty metadata  
- Produce token-level provenance  
- Mask sensitive content (if OCR’ing culturally sensitive material)  

---

### 4. 🧭 Focus Mode v3 NLP Reasoners

NLP reasoning models provide:

- Narrative semantic expansion  
- Language-grounded evidence fusion  
- Story Node text generation  
- Entity disambiguation  
- CARE-safe narrative abstraction  

CARE RULE:  
**No speculation. No hallucination. No inference of tribal identity or sacred context.**

---

### 5. 🧠 Embedding Models (Text)

Used for:

- Semantic search  
- Narrative grounding  
- Entity similarity  
- Linking to Focus Mode v3  

Must include:

- Deterministic vectors  
- Drift-safe evaluation  
- Explainability projections (PCA/UMAP)  

---

## 📡 STAC Integration (KFM-STAC v11)

NLP outputs that produce spatial or temporal content MUST be packaged as STAC Items including:

- `kfm:nlp:model_name`  
- `kfm:nlp:model_version`  
- `kfm:nlp:method`  
- `kfm:input_items` array  
- Spatial extents (if present)  
- Temporal extents  
- Confidence metadata  
- Provenance: `prov:*`  

OCR outputs MAY include:

- Text assets  
- Token maps  
- CITED provenance chain  

---

## 🧠 Explainability Requirements

All NLP models MUST provide:

- Attention maps  
- Attribution vectors  
- Token/feature-level weights  
- JSON-LD explainability bundle  
- CARE-masked highlights for protected text  

Explainability maps MUST NOT leak sensitive cultural information.

---

## 🔐 FAIR+CARE Requirements

NLP models MUST:

- Mask tribal names, burial sites, restricted ceremonial terms  
- Clearly annotate uncertainties  
- Prohibit any identity inference in Story Nodes  
- Maintain dataset licensing + restrictions in Model Cards  
- Use CARE scope + approval references in metadata  

---

## 🧪 Testing Requirements

All NLP model families MUST pass:

- Seed-locked reproducibility tests  
- Model Card schema validation  
- NER precision/recall regression checks  
- OCR accuracy tests  
- Explainability drift tests  
- STAC + DCAT + PROV-O schema checks  
- CARE-compliance unit tests  

Failures → **PR blocked**.

---

## 🕰 Version History

| Version  | Date       | Notes                                                         |
|----------|------------|---------------------------------------------------------------|
| v11.2.2  | 2025-11-28 | Full v11.2.2 uplift; governance refinement; emoji tree added |
| v11.0.0  | 2025-11-22 | Initial NLP model family specification                        |

---

<div align="center">

### 🔗 Footer  
[⬅ AI Models Index](../README.md) · [⚙️ Inference Layer](../../inference/README.md) · [🏛 Governance](../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

