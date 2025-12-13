---
title: "💧 Model Card — Hydrology Seq2Seq v11 (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "mcp/model_cards/hydrology_seq2seq_v11.md"

version: "v11.0.0"
last_updated: "2025-12-12"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Hydrology Working Group · FAIR+CARE Council · AI Governance Board"
content_stability: "stable"

status: "Active / Enforced"
doc_kind: "Model Card"
header_profile: "standard"
footer_profile: "standard"
intent: "hydrology-seq2seq-v11"
semantic_document_id: "kfm-modelcard-hydrology-seq2seq-v11"
doc_uuid: "urn:kfm:modelcard:hydrology-seq2seq-v11:v11.0.0"
event_source_id: "urn:kfm:modelcard:hydrology-seq2seq-v11"

machine_extractable: true
classification: "AI Model Documentation"
sensitivity: "Mixed"
fair_category: "F1-A1-I2-R3"
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

provenance_chain:
  - "mcp/experiments/2025-11-02_HYDRO-EXP-002.md@v11.0.0"
  - "mcp/experiments/2025-11-06_HYDRO-EXP-011.md@v11.0.0"

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
  - "publish-without-human-review"
---

<div align="center">

# 💧 **Hydrology Seq2Seq v11 — Model Card (v11 LTS)**
`mcp/model_cards/hydrology_seq2seq_v11.md`

**Purpose**  
Document model architecture, evaluation, governance, provenance, and usage boundaries for the
**Hydrology Seq2Seq v11 (HS2S‑v11)** model — KFM’s primary engine for hydrologic reconstruction
(daily streamflow, reservoir inflow/outflow, sediment-adjusted series, historical backfilling).

</div>

---

## 📘 Overview

**Hydrology Seq2Seq v11 (HS2S‑v11)** is a sequence-to-sequence reconstruction model designed to:

- reconstruct missing streamflow / inflow / outflow values
- extend incomplete USGS time series
- model hydrologic response to climate forcings (precip, ET, anomalies) for reconstruction workflows
- provide inputs to:
  - reservoir storage adjustments
  - multi-source hydrology fusion
  - flood/drought analysis
  - climate-driven hydrology pipelines
- support Focus Mode v3 and Story Node v3 environmental context (evidence-led, cited)

**Non-goals**
- HS2S‑v11 does not produce operational forecasts.
- HS2S‑v11 is intended for historical reconstruction and gap-filling within training-window coverage.

---

## 🗂️ Directory Layout

~~~text
📁 KansasFrontierMatrix/
├── 📁 mcp/
│   ├── 📁 model_cards/
│   │   └── 📄 hydrology_seq2seq_v11.md                    # This model card (HS2S‑v11)
│   └── 📁 experiments/
│       ├── 📄 2025-11-02_HYDRO-EXP-002.md                 # Multi-source fusion validation (as referenced)
│       └── 📄 2025-11-06_HYDRO-EXP-011.md                 # Training run log (as referenced)
├── 📁 src/
│   └── 📁 pipelines/
│       └── 📁 hydrology/
│           ├── 📁 reconstruction/                         # HS2S‑v11 reconstruction pipeline stages
│           └── 📁 multisource_fusion/                     # Downstream fusion consumers
├── 📁 data/
│   └── 📁 provenance/
│       └── 📁 experiments/
│           └── 📁 hydrology_seq2seq_v11/
│               └── 📁 <timestamp>/
│                   ├── 🧾 prov.jsonld                     # PROV‑O JSON‑LD
│                   ├── 🧾 openlineage.json                # OpenLineage event(s)
│                   ├── 🧾 metrics.json                    # Metrics bundle
│                   ├── 🧾 config_snapshot.json            # Training/config snapshot
│                   └── 🧾 checksums.json                  # Output checksums
└── 📁 releases/
    └── 📁 v11.0.0/
        └── 🧾 mcp-modelcards-telemetry.json               # Energy/carbon/runtime telemetry bundle
~~~

---

## 🧭 Context

**Approved uses**
- daily hydrologic gap-fill
- multi-source hydrology fusion support
- reservoir reconstruction pipelines
- sedimentation-adjusted inflow series reconstruction
- extreme-event reconstruction (drought/flood periods) within supported ranges
- climate-driven reconstructions using:
  - precipitation
  - temperature anomalies
  - evapotranspiration
  - snow metrics (if available)

**Restricted uses**
- regulatory water-rights adjudication
- tribal water-use inference without explicit approval
- high-resolution ecological impact modeling without domain review
- predictive release operations or emergency forecasting
- narratives involving cultural sites or tribal watersheds without governance review and masking

---

## 📦 Data & Metadata

### Training datasets (as referenced)
| Dataset | STAC/DCAT ID | Notes |
|---------|--------------|-------|
| USGS Daily Streamflow | `stac:hydrology/usgs_daily` | Ground truth |
| USACE Reservoir Ops | `stac:hydrology/usace_ops` | Reservoir inflow/outflow |
| Kansas Mesonet Climate | `stac:climate/mesonet` | ET, precip, temp |
| ERA5 Reanalysis | `stac:climate/era5` | Climate forcing |
| DEM / Watershed Data | `stac:terrain/dem` | Basin-based hydrology features |

### Governance posture (as reported)
- data is FAIR-compliant
- tribal watershed data is masked at H3‑R7 unless permissions are granted
- no sensitive cultural datasets used for training

### Bias considerations (as reported)
Known risk areas:
- sparse gauge density in western Kansas
- seasonal imbalance (wet-season dominance)
- drought-heavy training windows (1930s/1950s)

Mitigations (as reported):
- stratified sampling
- data augmentation by regime type
- seasonal balancing

---

## 🧱 Architecture

### Architecture summary (as reported)
- encoder:
  - multi-channel climate + hydrology + watershed embeddings
  - 1D CNN + temporal attention
- decoder:
  - GRU / Transformer hybrid
  - residual prediction heads
  - uncertainty channel output
- auxiliary modules:
  - sedimentation factor estimator
  - basin similarity embedding
  - elevation and terrain-aware correction

### Outputs (as reported)
- reconstructed hydrologic series
- confidence intervals (±CI)
- fill-flag masks
- metadata fields including anomaly alignment

---

## 🧪 Validation & CI/CD

### Training procedure (as reported)
- framework: PyTorch 2.2
- hardware: A100 80GB
- docker: `kfm/hydro-env:v11`
- epochs: 150
- batch size: 64
- learning rate: 2e‑4 (warmup → cosine)
- loss: weighted RMSE + drought-event penalty + uncertainty loss
- seed: 882134

Training run reference (as provided):
~~~text
mcp/experiments/2025-11-06_HYDRO-EXP-011.md
~~~

### Evaluation metrics (as reported)
| Metric | Score |
|--------|-------|
| RMSE (daily flow) | 14.2 cfs |
| MAE (daily flow) | 7.9 cfs |
| Drought period accuracy | 0.93 |
| High-flow event reconstruction | 0.87 |
| Seasonal stability | 0.95 |
| Sedimentation-adjusted storage match | 0.90 |

### Validation studies (as reported)
- 20 basins across Kansas
- flood/drought signature detection
- watersheds with differing physiography
- comparison to observed USGS time series

### Uncertainty (as reported)
Decoder outputs a ±CI range representing model uncertainty, stored in output metadata as:
~~~json
{
  "uncertainty_bounds": { }
}
~~~

---

## 🧠 Story Node & Focus Mode Integration

### Focus Mode v3 usage
- HS2S‑v11 may provide quantitative hydrology context (ranges, anomalies, reconstruction flags)
- Focus Mode presentations must link values to evidence (datasets and provenance traces)

### Story Node v3 usage
- HS2S‑v11 outputs may support environmental context blocks when:
  - dataset citations are present
  - masking/generalization rules are applied where required
  - uncertainty is surfaced (at least via confidence interval or qualitative confidence band)

### Safety boundary
HS2S‑v11 must not be used to infer cultural meaning, water-use intent, or sovereignty-sensitive conclusions.

---

## 🌐 STAC, DCAT & PROV Alignment

### STAC / DCAT expectations
- publishable reconstructed series and basin bundles should be described via DCAT datasets
- spatially keyed assets (if emitted as rasters/grids) should be described via STAC Items/Collections
- all derived artifacts should include license/rights and CARE/sovereignty fields as applicable

### PROV‑O block (simplified)
~~~json
{
  "prov:entity": "hydrology_seq2seq_v11",
  "prov:wasGeneratedBy": "training:2025-11-06_HYDRO-EXP-011",
  "prov:used": [
    "stac:hydrology/usgs_daily",
    "stac:hydrology/usace_ops",
    "stac:climate/era5",
    "stac:climate/mesonet",
    "stac:terrain/dem"
  ],
  "prov:wasAssociatedWith": "kfm-ai-training-service-v11"
}
~~~

### OpenLineage storage (as referenced)
~~~text
data/provenance/experiments/hydrology_seq2seq_v11/<timestamp>/
~~~

Expected contents include:
- dataset mappings
- training/validation alignment
- model fingerprint
- metrics bundle
- (optional) XAI artifacts

---

## ⚖ FAIR+CARE & Governance

### FAIR compliance (as reported)
- STAC/DCAT metadata complete for publishable artifacts
- PROV‑O + OpenLineage preserved for training and key runs
- reusable under CC‑BY (with governance constraints)
- dataset references embedded in output metadata

### CARE + sovereignty constraints (as reported)
- no unrestricted tribal watershed data accepted without permissions
- outputs must be masked/generalized for culturally sensitive regions
- never infer or expose sensitive water-use patterns
- Tier A datasets require council review

Operational boundary:
- HS2S‑v11 cannot reconstruct flows for restricted basins unless permissions are included.
- territorial hydrology must be masked to H3‑R7 → R9 resolution when required.

### Limitations (as reported)
Lower accuracy for:
- sparse data basins
- high-flow extreme events
- snow-driven hydrology (rare in Kansas)
- periods with missing climate forcings

Not suitable for:
- fine-scale ecological modeling
- legal water-rights estimation
- emergency flood forecasting
- tribal water modeling without explicit authorization

Human oversight is required for all uses influencing planning or policy.

### Deployment boundaries
Authorized for:
- hydrology reconstruction pipelines
- sedimentation-adjusted reservoir modeling
- climate-driven multi-source fusion support
- Story Node environmental context (cited, masked where required)
- Focus Mode quantitative hydrology background (cited)

Restricted from:
- high-risk or sovereign basin modeling without review
- narratives involving cultural water-use
- direct decision-making systems

Integration points (as referenced):
~~~text
src/pipelines/hydrology/reconstruction/
src/pipelines/hydrology/multisource_fusion/
~~~

---

## 🕰️ Version History

| Version | Date | Summary |
|--------:|------|---------|
| v11.0.0 | 2025-11-23 | Initial Hydrology Seq2Seq v11 model card (governed, lineage-aligned). |
| v11.0.0 | 2025-12-12 | Normalized document to KFM‑MDP v11.2.6 (approved H2 set, required directory layout section, tilde fences, governance links in footer). No model behavior changes. |

---

<div align="center">

💧 **Hydrology Seq2Seq v11 — Model Card**  
[🏛️ Governance Charter](../../docs/standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../docs/standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

© 2025 Kansas Frontier Matrix — CC‑BY 4.0  
MCP‑DL v6.3 · KFM‑MDP v11.2.6 · Hydrology Governance · Sovereignty‑Aware  
Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>
