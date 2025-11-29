---
title: "💧🔡🧠 KFM v11.2.2 — Hydrology Embeddings Model (Runoff 🌧️ · Soil Moisture 🪴 · Streamflow 🌊 · Flood Risk ⚠️ · Drought 🏜️ · Deterministic · XAI 💡 · FAIR+CARE 🛡️)"
path: "docs/pipelines/ai/inference/embeddings/hydrology-embeddings.md"
version: "v11.2.2"
last_updated: "2025-11-28"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Hydrology Working Group 💧 · FAIR+CARE Council 🛡️"
status: "Active / Enforced"
content_stability: "stable"
doc_kind: "Embeddings · Hydrology Embeddings Model 💧🔡"

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
care_label: "Public · Medium-Risk"
sensitivity: "Hydrology-Embeddings"
sensitivity_level: "Medium"
public_exposure_risk: "Low"
immutability_status: "version-pinned"

semantic_intent:
  - "hydrology-embeddings"
  - "runoff-embeddings"
  - "soil-moisture-embeddings"
  - "streamflow-embeddings"
  - "flood-embeddings"
  - "drought-embeddings"
  - "watershed-latents"
  - "xai-hydrology-vectors"
  - "vector-search-hydro"
  - "hydro-regime-similarity"
  - "faircare-sovereignty"

scope:
  domain: "pipelines/ai/inference/embeddings/hydrology-embeddings"
  applies_to:
    - "hydrology-embeddings.md"
    - "climate-embeddings.md"
    - "hazard-embeddings.md"
    - "spatial-embeddings.md"
    - "narrative-embeddings.md"
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

# 💧🔡🧠 **Hydrology Embeddings Model — KFM v11.2.2 (MAX MODE)**  
`docs/pipelines/ai/inference/embeddings/hydrology-embeddings.md`

**Purpose**  
Define the deterministic, FAIR+CARE-compliant, sovereignty-protected  
**Hydrology Embeddings Model**, generating latent vectors representing:

🌧️ **Runoff**  
🪴 **Soil Moisture**  
🌊 **Streamflow**  
⚠️ **Flood Risk Precursors**  
🏜️ **Drought Signatures (SPI/SPEI/SSI)**  
🌀 **Watershed State Fingerprints**  

Supports hydrology similarity search, anomaly pattern recognition, hazard chaining,  
Story Node v3 hydrology narratives, and Focus Mode v3 watershed intelligence.

</div>

---

## 💧📘🔡 **Overview — Hydrology Embeddings**

Hydrology embeddings compress spatial + temporal hydrological states into stable vector  
representations that capture:

- Soil moisture structure  
- Saturation & infiltration regime  
- Runoff response to rainfall  
- Streamflow morphology  
- Flood precursors: RRHI, ΔQ/Δt rise rate  
- Watershed flow hierarchy  
- Drought morphology (multi-timescale SPI/SPEI/SSI)  
- Terrain + wetness index interactions  
- Climate–hydrology coupling signals  

These vectors enable:

- Watershed analog search  
- Regime classification  
- Downstream hazard-driver matching  
- Hydrology-aware narrative generation  
- Multi-decade hydrology retrieval  

---

## 🧬💧🔡 **Hydrology Embeddings Pipeline (Mermaid-Safe)**

```mermaid
flowchart TD
    A[🌧️ Runoff · Soil Moisture · Streamflow Inputs] --> B[🧽 Hydrology Normalization Layer]
    B --> C[🧠 Embedding Encoder · Hydro Transformer]
    C --> D[🔡 Hydro Embedding Vector Output · Seed Locked]
    D --> E[🗂️ STAC Hydrology Embedding Item Builder]
    E --> F[📜 PROV Lineage And Telemetry]
    F --> G[🛡️ CARE Sovereignty Filters]
    G --> H[📦 Register Hydrology Embeddings In Vector Index]
```

---

## 🌧️🪴🌊 **Input Requirements**

Hydrology embeddings ingest the following **seed-locked, STAC-linked, FAIR+CARE-compliant** fields:

### 1️⃣ 🌧️ Runoff  
- Runoff depth  
- Rapid Runoff Hazard Index (RRHI)  
- Infiltration parameters  

### 2️⃣ 🪴 Soil Moisture  
- Absolute + anomaly fields  
- Saturation index  
- Water-balance components  

### 3️⃣ 🌊 Streamflow  
- Discharge (Q)  
- Rise rate (ΔQ/Δt)  
- Routing topology  

### 4️⃣ 🗺️ Terrain + Watershed  
- DEM slope  
- Flow direction  
- TWI  
- Watershed membership  

### 5️⃣ 🏜️ Drought Signatures  
- SPI  
- SPEI  
- SSI  
- Multi-scale windows  

Metadata MUST include:

- CRS  
- Units  
- ISO timestamps  
- FAIR+CARE labels  
- Sovereignty constraints  
- PROV lineage  

---

## 🔡🧮💧 **Embedding Process (ASCII-Safe)**

```
hydro_embedding = f( hydrology_tensor ; model_version, seed )
```

Where:

- `f` = deterministic encoder model  
- Inputs undergo **normalization**, **masking**, **sovereignty filtering**  
- Output = **fixed-length vector** (e.g., 256–2048 dims)

---

## 📦💧📊 **Outputs**

Hydrology embeddings MUST produce:

- `hydrology_embedding_vector.npy` or `.parquet`  
- `hydrology_embedding_metadata.json`  
- `hydrology_embedding_summary.json`  
- CAM/attention overlays (optional)  
- STAC-XAI Hydrology Embedding Item  
- PROV-O lineage block  
- CARE metadata block  
- Deterministic seed metadata  

---

## 💡🧠💧 **XAI for Hydrology Embeddings**

XAI MUST explain contributions:

- Soil moisture structure  
- Runoff sensitivity  
- Streamflow rise-rate factors  
- Drought multi-scale weights  
- Terrain & watershed topology  
- Hazard-hydro coupling  
- CAM overlays for spatial components  
- Attention maps for sequence/context models  

Example:

```json
{
  "xai": {
    "importance": {
      "soil_moisture": 0.29,
      "runoff": 0.22,
      "streamflow": 0.18,
      "drought": 0.15,
      "terrain": 0.16
    },
    "seed": 42
  }
}
```

---

## 🛡️⚖️🧭 **FAIR+CARE + Sovereignty Enforcement**

Hydrology embeddings MUST:

- Mask sensitive hydrology signals in sovereignty-protected watersheds  
- Generalize hyperlocal flow-risk patterns  
- Protect culturally sensitive hydrological regions  

CARE block:

```json
{
  "care": {
    "masking": "h3-hydro-generalized",
    "scope": "public-generalized",
    "notes": ["Hydrology embedding generalized in sovereignty-protected basin"]
  }
}
```

---

## 🔒⚙️🧪 **Determinism Requirements**

- Fully seed-locked  
- No probabilistic modeling  
- Deterministic DEM + routing transforms  
- Stable floating-point ops  
- Reproducible normalization  

---

## 🧪📏🔬 **CI Validation Requirements**

CI MUST verify:

- Deterministic embeddings  
- Correct CRS/units  
- XAI metadata present  
- STAC-XAI compliance  
- PROV lineage complete  
- CARE metadata included  
- No sensitive watershed leakage  
- Telemetry recorded (OTel + energy + carbon)  

Failure → ❌ merge blocked.

---

## 🕰️📜 **Version History**

| Version  | Date       | Notes                                              |
|----------|------------|----------------------------------------------------|
| v11.2.2  | 2025-11-28 | Initial Hydrology Embeddings Model (MAX MODE)      |

---

<div align="center">

### 🔗 Footer  
[🔡 Back to Embeddings Pipeline](./README.md) ·  
[💧 Hydrology AI](../../hydrology/README.md) ·  
[🏛 Governance](../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

