---
title: "📚🧠🔡 KFM v11.2.2 — Narrative Embeddings Model (Story Nodes 📖 · Place-Based Semantics 🗺️ · Climate/Hazard Context 🌡️🌪️ · Deterministic · XAI 💡 · FAIR+CARE 🛡️)"
path: "docs/pipelines/ai/inference/embeddings/narrative-embeddings.md"
version: "v11.2.2"
last_updated: "2025-11-28"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Story Node Working Group 📖 · FAIR+CARE Council 🛡️"
status: "Active / Enforced"
content_stability: "stable"
doc_kind: "Embeddings · Narrative Embedding Model 📚🔡"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<prev>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../../releases/v11.2.2/embeddings-inference-telemetry.json"
telemetry_schema: "../../../../../../schemas/telemetry/ai-embeddings-inference-v11.2.2.json"
energy_schema: "../../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"
data_contract_ref: "../../../../../contracts/data-contract-v3.json"

license: "MIT"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"

fair_category: "F1-A1-I1-R1"
care_label: "Public · High-Risk (Contextual Data)"
sensitivity: "Narrative-Embeddings"
sensitivity_level: "High"
public_exposure_risk: "Medium"
immutability_status: "version-pinned"

semantic_intent:
  - "narrative-embeddings"
  - "storynode-embeddings"
  - "contextual-vectors"
  - "place-based-meaning"
  - "cultural-landscape-semantics"
  - "climate-hazard-context"
  - "text-geospatial-fusion"
  - "xai-narrative-vectors"
  - "faircare-governance"
  - "sovereignty-protection"

scope:
  domain: "pipelines/ai/inference/embeddings/narrative-embeddings"
  applies_to:
    - "narrative-embeddings.md"
    - "storynode-embeddings"
    - "focusmode-embeddings"
    - "hazard-embeddings.md"
    - "climate-embeddings.md"
    - "hydrology-embeddings.md"
    - "index/*"
    - "telemetry/*"
    - "xai/*"

layout_profiles:
  - "immediate-one-branch-with-descriptions-and-emojis"

requires_purpose_block: true
requires_version_history: true
requires_governance_links_in_footer: true
requires_directory_layout_section: false

diagram_profiles:
  - "mermaid-flowchart-v1"
---

<div align="center">

# 📚🧠🔡 **Narrative Embeddings Model — KFM v11.2.2 (MAX MODE)**  
`docs/pipelines/ai/inference/embeddings/narrative-embeddings.md`

**Purpose**  
Define the sovereignty-safe, FAIR+CARE-governed, deterministic **Narrative Embeddings Model**  
that powers:  
📖 **Story Node v3 embeddings**,  
🧭 **Focus Mode v3 contextual cues**,  
🌡️💧🌪️ **climate/hydrology/hazard narrative linking**,  
🗺️ **place-based semantic modeling**, and  
🧠 **multimodal vector reasoning** across the entire Kansas Frontier Matrix.

</div>

---

## 📚🧬🔡 **Overview — What Are Narrative Embeddings?**

Narrative embeddings encode *meaning*, *context*, and *place* by fusing:

- 📜 Historical text fragments  
- 🗺️ Geospatial references (H3, coordinates, regions)  
- 🌡️ Climate/hazard signals tied to place  
- 💧 Hydrological events (floods, droughts, land–water interactions)  
- 🌾 Land-use/landscape semantic cues  
- 🧑‍🤝‍🧑 Cultural/tribal governance context (FAIR+CARE)  
- 🌀 Multi-hazard environmental context  
- 🧠 Embedding-level narrative structure  

They unify **text + geospatial + environmental signals** into a **single vector** suitable for:

- Story Node generation  
- Contextual retrieval  
- Focus Mode guidance  
- Historical analog search  
- Environmental narrative construction

Vectors MUST be deterministic, seed-locked, and provenance-safe.

---

## 🧬📚🧠 **Narrative Embeddings Pipeline (Mermaid-Safe)**

```mermaid
flowchart TD
    A[📜 Text And Place-Based Inputs] --> B[🧽 Normalize Token And Geo Context]
    B --> C[🧠 Narrative Encoder Transformer]
    C --> D[🔡 Narrative Embedding Vector Output Seed Locked]
    D --> E[🗂️ STAC Narrative Embedding Item]
    E --> F[📜 PROV Lineage And Telemetry]
    F --> G[🛡️ CARE Sovereignty Filters]
    G --> H[📦 Register Narrative Embeddings In Vector Index]
```

---

## 📜🗺️🧠 **Input Requirements**

### 1️⃣ 📜 Text Inputs  
- Historical documents  
- Climate or hydrology narratives  
- Research summaries  
- Story Node v3 text blocks  
- Local/regional descriptions  

### 2️⃣ 🗺️ Geospatial Inputs  
- Points, polygons, H3 cells  
- Watershed identifiers  
- Cultural boundaries  
- Elevation/terrain context  

### 3️⃣ 🌡️ Environmental Inputs  
- Climate states (temp, dewpoint, wind)  
- Hazards context (severe storms, flood, fire, heat, winter)  
- Hydrology: runoff, soil moisture, streamflow, drought  

### 4️⃣ 🔍 Derived Context  
- Place-based embeddings from spatial models  
- Hazard embeddings  
- Climate envelope embeddings  

All MUST include:

- CRS  
- Units (if applicable)  
- Timestamp (for temporal narratives)  
- FAIR+CARE classification  
- Sovereignty metadata  
- STAC lineage references  

---

## 🔡🧮📚 **Embedding Process (ASCII-Safe)**

```
narrative_embedding = f( narrative_tensor ; model_version, seed )
```

Where:

- `f` = deterministic narrative transformer  
- Inputs include fused text + geo + climate/hydro/hazard tensors  
- Output is a **fixed-length semantic vector**  

---

## 📦📚📊 **Outputs**

Narrative embeddings MUST produce:

- `narrative_embedding_vector.npy` or `.parquet`  
- `narrative_embedding_metadata.json`  
- `narrative_embedding_summary.json`  
- CAM/attention overlays (if enabled)  
- STAC-XAI embedding Item  
- PROV-O lineage  
- CARE block  
- Deterministic seed metadata  

---

## 💡🧠📚 **XAI for Narrative Embeddings**

XAI MUST show:

- Contribution of text vs geospatial vs environmental inputs  
- CAM/attention maps over narrative text  
- Attention over spatial tokens (H3, regions, basins)  
- Influence of climate/hazard embeddings  
- Feature importance vectors  
- STAC-XAI linkage  
- Seed metadata  

Example:

```json
{
  "xai": {
    "importance": {
      "text_content": 0.42,
      "geospatial_context": 0.22,
      "climate_context": 0.15,
      "hydrology_context": 0.11,
      "hazard_context": 0.10
    },
    "seed": 42
  }
}
```

---

## 🛡️⚖️🧭 **FAIR+CARE + Sovereignty Enforcement**

Narrative embeddings MUST:

- Mask culturally sensitive narrative cues  
- Remove location-precise tribal references  
- Prevent exposure of sensitive landscape associations  
- Carry explicit CARE metadata:

```json
{
  "care": {
    "masking": "h3-narrative-generalized",
    "scope": "public-generalized",
    "notes": ["Narrative embeddings generalized to protect sovereignty-sensitive cultural contexts"]
  }
}
```

---

## 🔒⚙️🧪 **Determinism Requirements**

- No stochastic token sampling  
- No random embedding noise  
- Seed-locked tokenizer + transformer path  
- Stable floating-point ops  
- Reproducible narrative vector generation  

---

## 🧪📏🔬 **CI Validation Requirements**

CI MUST ensure:

- Deterministic embeddings  
- Correct FAIR+CARE labeling  
- Complete STAC-XAI metadata  
- PROV lineage present  
- No sensitive region leakage  
- Text + spatial + environmental metadata integrity  
- Telemetry bundles (OTel + carbon + energy) included  

Failure → ❌ block merge.

---

## 🕰️📜 **Version History**

| Version  | Date       | Notes                                                   |
|----------|------------|---------------------------------------------------------|
| v11.2.2  | 2025-11-28 | Initial Narrative Embeddings Model (MAX MODE)           |

---

<div align="center">

### 🔗 Footer  
[🔡 Back to Embeddings Pipeline](./README.md) ·  
[📖 Story Node Embeddings](../../storynode/README.md) ·  
[🏛 Governance](../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

