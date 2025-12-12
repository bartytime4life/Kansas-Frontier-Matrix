---
title: "🌡️ Model Card — Climate Anomaly Net v3 (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "mcp/model_cards/climate_anomaly_net_v3.md"

version: "v11.0.0"
last_updated: "2025-12-12"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Climate Working Group · FAIR+CARE Council · AI Governance Board"
content_stability: "stable"

status: "Active / Enforced"
doc_kind: "Model Card"
header_profile: "standard"
footer_profile: "standard"
intent: "climate-anomaly-net-v3"
semantic_document_id: "kfm-modelcard-climate-anomaly-net-v3"
doc_uuid: "urn:kfm:modelcard:climate-anomaly-net-v3:v11.0.0"
event_source_id: "urn:kfm:modelcard:climate-anomaly-net-v3"

machine_extractable: true
classification: "AI Model Documentation"
sensitivity: "Low"
fair_category: "F1-A1-I2-R2"
care_label: "Responsible · Ethics · Stewardship"
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

provenance_chain:
  - "mcp/experiments/2025-11-01_CLIMATE-EXP-001.md@v11.0.0"

ai_transform_permissions:
  - "summarize"
  - "extract-metadata"
  - "a11y-adaptations"
  - "layout-normalization"
ai_transform_prohibited:
  - "fabricate-results"
  - "fabricate-provenance"
  - "invent-dataset-ids"
  - "invent-license-rights"
  - "override-governance"
  - "expose-sensitive-coordinates"
  - "deanonymize"
---

<div align="center">

# 🌡️ **Climate Anomaly Net v3 — Model Card (v11 LTS)**
`mcp/model_cards/climate_anomaly_net_v3.md`

**Purpose**  
Document the architecture, training, evaluation, governance, ethics, provenance, and usage boundaries of
**Climate Anomaly Net v3 (CAN‑v3)** — used for anomaly detection, historical climate reconstruction, and
bias-correction support within Kansas Frontier Matrix v11.

</div>

---

## 📘 Overview

**Climate Anomaly Net v3 (CAN‑v3)** is a hybrid CNN + Transformer model designed to:

- detect climate anomalies (temperature, precipitation, drought indices)
- reconstruct missing climate sequences (hindcast / reconstruction)
- support bias-correction (BCSD/QM pipelines)
- produce anomaly surfaces for:
  - hydrology models
  - climate reconstructions
  - hazard overlays
  - Story Node environmental context
  - Focus Mode v3 contextual explanations

**Non-goals**
- CAN‑v3 does not generate forward climate projections.
- CAN‑v3 outputs are not an emergency alert system.
- CAN‑v3 is not a narrative model and must not be used to infer cultural or historical meaning.

---

## 🗂️ Directory Layout

~~~text
📁 KansasFrontierMatrix/
├── 📁 mcp/
│   ├── 📁 model_cards/
│   │   └── 📄 climate_anomaly_net_v3.md                     # This model card (CAN‑v3)
│   └── 📁 experiments/
│       ├── 📄 2025-11-01_CLIMATE-EXP-001.md                 # Climate anomaly reconstruction experiment
│       └── 📄 YYYY-MM-DD_CLIMATE-EXP-###.md                 # (Optional) dedicated CAN‑v3 training run log
├── 📁 data/
│   ├── 📁 processed/
│   │   └── 📁 climate/
│   │       └── 📁 anomalies/
│   │           └── 📁 v11/                                  # Anomaly surfaces used by KFM pipelines
│   └── 📁 provenance/
│       └── 📁 experiments/
│           └── 📁 climate_anomaly_net_v3/
│               └── 📁 <timestamp>/
│                   ├── 🧾 prov.jsonld                        # PROV‑O JSON‑LD
│                   ├── 🧾 openlineage.json                   # OpenLineage event(s)
│                   └── 🧾 checksums.json                     # Output checksums
└── 📁 releases/
    └── 📁 v11.0.0/
        └── 🧾 mcp-modelcards-telemetry.json                  # Model card telemetry bundle
~~~

---

## 🧭 Context

### Intended use
Primary allowed uses include:
- climate anomaly surface generation (temperature, precipitation, indices)
- hydrology reconstruction forcing inputs (hindcast/reconstruction workflows)
- bias-correction support for downscaling (BCSD/QM hybrids)
- hazard overlay context layers (non-forecast)
- Focus Mode v3: contextual climate facts (evidence-led, non-narrative)
- Story Node environmental facts (with dataset citations and masking rules applied)

### Out-of-scope use
CAN‑v3 must not be used for:
- predictive climate modeling beyond the training/observation range
- emergency alerting or operational warning systems
- policy decision-making without domain expert oversight
- cultural or historical interpretation (beyond factual environmental context)
- unreviewed use on sovereignty-restricted geographies without required masking and governance review

---

## 📦 Data & Metadata

### Training datasets (as referenced)
| Dataset | Version / Range | STAC/DCAT ID | Notes |
|--------|------------------|--------------|------|
| PRISM Climate Normals | 1981–2010 | `stac:climate/prism_normals` | Baseline climatology |
| NOAA NCEI Daily | v2025 | `stac:climate/ncei_daily` | Observations |
| ERA5 Reanalysis | 1979–2024 | `stac:climate/era5` | Spatial/temporal context |
| Kansas Mesonet | 1980–2024 | `stac:climate/mesonet` | High-res microclimate |
| Terrain DEM | v11 | `stac:terrain/dem` | Lapse-rate / terrain features |

### Data governance (as reported)
- datasets classified as FAIR-compliant
- CARE-sensitive agricultural data masked at H3‑R6 (where applicable)
- no Indigenous-sensitive datasets used in training (as reported)

### Bias considerations (as reported)
Known risk areas:
- sparse station density in western Kansas
- dry-year overrepresentation (1930s/1950s)
- urban heat island heterogeneity (Wichita / KC region)

Mitigations (as reported):
- reweighting
- temporal stratification
- ensemble debiasing

---

## 🧱 Architecture

### Model architecture (as reported)
- CNN encoder for spatial feature extraction
- Transformer decoder for temporal sequence reconstruction
- hybrid attention for anomaly signals
- graph-enhanced features from watershed/ecoregion vectors

### Training procedure (as reported)
- epochs: 200
- batch size: 32
- optimizer: AdamW
- learning rate: 1e‑4 (warmup + cosine decay)
- loss: hybrid RMSE + anomaly-weighted loss

### Reproducibility (as reported)
- seed: 223487
- framework: PyTorch 2.2
- hardware: A100 40GB
- docker image: `kfm/climate-env:v11`
- dependencies: pinned via SBOM
- environment hash: `.hash.env` (as referenced)

**Training run reference**
- Primary reconstruction foundation: `mcp/experiments/2025-11-01_CLIMATE-EXP-001.md`
- If a dedicated training log exists, record it under:
  - `mcp/experiments/YYYY-MM-DD_CLIMATE-EXP-###.md`

---

## 🧪 Validation & CI/CD

### Evaluation metrics (as reported)
| Metric | Score |
|--------|-------|
| RMSE (temperature anomaly) | 0.42°C |
| RMSE (precip anomaly) | 1.7 mm |
| Spatial coherence index | 0.91 |
| Seasonal retention score | 0.97 |
| Bias-correction support score | 0.94 |

### Spatial validation (as reported)
- verified against Kansas Mesonet & NOAA stations
- Moran’s I used to assess spatial coherence

### Temporal validation (as reported)
- autocorrelation and seasonal-cycle recovery validated
- strong performance on drought/flood signature detection

### Explainability (XAI) (as reported)
XAI artifacts referenced at:
~~~text
mcp/experiments/2025-11-14_CLIMATE-EXP-006/
~~~

Reported highlights:
- SHAP: terrain elevation strongly influences temperature anomalies; station density correlates with confidence
- LIME: precip anomalies heavily driven by synoptic-scale features; heatwave anomalies depend on ERA5 inputs

### Telemetry (Energy & Carbon) (as reported)
Stored in:
~~~text
releases/v11.0.0/mcp-modelcards-telemetry.json
~~~

Approximate training footprint:
- energy: 14.2 kWh
- carbon: 680 gCO₂e
- GPU-hours: 9.6

---

## 🧠 Story Node & Focus Mode Integration

### Focus Mode usage
- CAN‑v3 may provide climate context facts (anomaly summaries, ranges, confidence cues)
- Focus Mode outputs must link anomalies to evidence and/or the derived anomaly surface datasets

### Story Node usage
- CAN‑v3 outputs may be used for environmental context blocks only
- narrative statements must include citations to source datasets and/or derived STAC assets
- masking/generalization is required where sovereignty or sensitivity rules apply

### Narrative safety boundary
CAN‑v3 is not a text generator. If CAN‑v3 outputs are summarized by LLM components, summaries must be:
- evidence-led (source-linked)
- non-speculative
- culturally neutral
- bounded to the supported time/spatial extent

---

## 🌐 STAC, DCAT & PROV Alignment

### STAC / DCAT expectations
- anomaly surfaces integrated into KFM should be described via:
  - STAC Items/Collections (for spatial assets)
  - DCAT dataset records (for publishable bundles)
- derived artifacts should include explicit license/rights and CARE/sovereignty fields

### PROV‑O block (simplified)
~~~json
{
  "prov:entity": "climate_anomaly_net_v3",
  "prov:wasGeneratedBy": "training:CAN-v3",
  "prov:used": [
    "stac:climate/prism_normals",
    "stac:climate/ncei_daily",
    "stac:climate/era5",
    "stac:climate/mesonet",
    "stac:terrain/dem"
  ],
  "prov:wasAssociatedWith": "kfm-ai-training-service-v11"
}
~~~

### OpenLineage (as referenced)
OpenLineage events stored under:
~~~text
data/provenance/experiments/climate_anomaly_net_v3/<timestamp>/
~~~

---

## ⚖ FAIR+CARE & Governance

### FAIR compliance (as reported)
- STAC/DCAT metadata complete (where emitted)
- PROV‑O lineage preserved
- reusable via open licensing (CC‑BY)

### CARE + sovereignty compliance (as reported)
- no culturally sensitive datasets used in training
- no disallowed spatial precision in governed outputs
- outputs must be masked when integrated into Story Nodes where required
- CAN‑v3 must not be used to reconstruct patterns on sovereignty-restricted geographies without required masking and governance review

### Limitations (as reported)
- reduced accuracy in:
  - sparse-station regions of western Kansas
  - extreme precipitation events
  - long pre-instrumental reconstructions
- possible drift in anomaly magnitude under multi-variable forcing
- not suitable for climate projection use (reconstruction/hindcast only)
- outputs require careful human review when used in narrative contexts

### Deployment & usage boundaries
Allowed:
- climate downscaling support
- hydrologic forcing generation (hindcast/reconstruction)
- hazard scenario layers (non-forecast)
- Focus Mode v3 climate facts (with citations)
- Story Node environmental facts (with citations + masking)

Restricted:
- automated narrative or historical interpretation
- direct decision-making or forecasting use
- high-risk modeling without expert oversight

---

## 🕰️ Version History

| Version | Date | Summary |
|--------:|------|---------|
| v11.0.0 | 2025-11-23 | Initial model card for Climate Anomaly Net v3, aligned with MCP‑DL v6.3 and KFM v11. |
| v11.0.0 | 2025-12-12 | Normalized document to KFM‑MDP v11.2.6 (approved H2 set, required directory layout section, tilde fences, governance links in footer). No model behavior changes. |

---

<div align="center">

🌡️ **Climate Anomaly Net v3 — Model Card**  
[🏛️ Governance Charter](../../docs/standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../docs/standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

© 2025 Kansas Frontier Matrix — CC‑BY 4.0  
MCP‑DL v6.3 · KFM‑MDP v11.2.6 · Sovereignty‑Aware · Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>
