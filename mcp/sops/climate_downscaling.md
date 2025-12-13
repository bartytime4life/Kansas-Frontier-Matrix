---
title: "🌦️ KFM SOP — Climate Downscaling & Bias Correction Workflow (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "mcp/sops/climate_downscaling.md"

version: "v11.0.0"
last_updated: "2025-12-13"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Climate Working Group · FAIR+CARE Council"
status: "Active / Enforced"
content_stability: "stable"

doc_kind: "SOP"
intent: "climate-downscaling"
semantic_document_id: "kfm-sop-climate-downscaling"
doc_uuid: "urn:kfm:mcp:sop:climate-downscaling:v11.0.0"
event_source_id: "ledger:kfm:mcp:sop:climate-downscaling:v11.0.0"
machine_extractable: true
immutability_status: "version-pinned"

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11.0"
pipeline_contract_version: "KFM-PDC v11.0"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

classification: "Scientific Procedure"
sensitivity: "Low"
fair_category: "F1-A1-I2-R2"
care_label: "Responsible · Ethics · Stewardship"
accessibility_compliance: "WCAG 2.1 AA+"
jurisdiction: "Kansas / United States"
indigenous_rights_flag: true

commit_sha: "<latest-commit-hash>"
doc_integrity_checksum: "<sha256>"
signature_ref: "../../releases/v11.0.0/signature.sig"
attestation_ref: "../../releases/v11.0.0/slsa-attestation.json"
sbom_ref: "../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../releases/v11.0.0/manifest.zip"

telemetry_ref: "../../releases/v11.0.0/mcp-sops-telemetry.json"
telemetry_schema: "../../schemas/telemetry/mcp-sops-v11.json"

governance_ref: "../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summary"
  - "timeline-generation"
  - "semantic-highlighting"
  - "a11y-adaptations"
  - "diagram-extraction"
  - "metadata-extraction"
  - "layout-normalization"
ai_transform_prohibited:
  - "content-alteration"
  - "speculative-additions"
  - "unverified-climate-claims"
  - "narrative-fabrication"
  - "governance-override"
  - "sensitive-coordinate-exposure"
  - "fabricate-provenance"

provenance_chain:
  - "prov:Plan:urn:kfm:mcp:sop:climate-downscaling:v11.0.0"
---

<div align="center">

# 🌦️ **KFM SOP — Climate Downscaling & Bias Correction Workflow (v11 LTS)**
`mcp/sops/climate_downscaling.md`

**Purpose**  
Define the **deterministic, reproducible, fairness-aware** workflow for downscaling and bias-correcting climate datasets (PRISM, ERA5, NOAA NCEI, CMIP-class products where permitted) into high-resolution Kansas-ready environmental layers for Kansas Frontier Matrix pipelines.

Scientific Insight × FAIR+CARE Ethics × Sustainable Intelligence  
Designed for Longevity · Governed for Integrity

<img src="https://img.shields.io/badge/MCP--DL-v6.3-blueviolet" />
<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/Climate-Downscaling-informational" />
<img src="https://img.shields.io/badge/Bias%20Correction-BCSD%20%2F%20QM-informational" />
<img src="https://img.shields.io/badge/FAIR%2BCARE-Governed-orange" />
<img src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />

[🧪 MCP Experiments](../experiments/README.md) ·
[🧬 Model Cards](../model_cards/README.md) ·
[🏛️ Governance](../../docs/standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE](../../docs/standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Sovereignty](../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

</div>

---

## 📘 Overview

### 🎯 Scope
This SOP governs climate downscaling and bias correction executed within KFM v11, including:
- 🧠 LangGraph v11 climate pipelines
- 🤖 CrewAI climate harmonization/downscaling workers (deterministic mode only)
- 💧 hydrology/hazard pipelines that require climate forcings
- 🧾 STAC/DCAT record creation for climate layers
- 🧬 PROV-O + OpenLineage-referenced lineage for all derived outputs

### 🧷 Non-negotiables
- **Deterministic runs:** same inputs + config + seeds → same outputs.
- **No unbounded invention:** downscaling/bias correction must not create physically implausible climate.
- **Evidence + contracts:** outputs must satisfy the climate contract (KFM-PDC v11) and retain provenance.
- **Safe overlays:** when climate layers intersect sovereignty-tagged narrative surfaces, masking/generalization rules apply at integration time.
- **CI-gated:** outputs lacking metadata/lineage/telemetry do not pass merge gates.

### 🧾 Key definitions
- **Downscaling:** transforming coarse climate fields to higher-resolution grids using deterministic spatial/temporal methods.
- **Bias correction:** adjusting distributions to match trusted reference observations over a calibration period.
- **Reference observations:** station-validated or high-quality gridded baseline used for bias correction (e.g., PRISM, NCEI, Mesonet where permitted).
- **Calibration period:** defined interval used to compute bias correction mappings (e.g., 1981–2010), pinned in config.

---

## 🗂️ Directory Layout

~~~text
📁 KansasFrontierMatrix/
├── 📁 mcp/
│   ├── 📁 sops/
│   │   └── 📄 climate_downscaling.md                         — 🌦️ This SOP
│   ├── 📁 experiments/
│   │   ├── 📄 README.md                                       — 🧪 MCP experiments index
│   │   └── 📄 2025-11-01_CLIMATE-EXP-001.md                    — 🌡️ Climate anomaly reconstruction (example upstream)
│   └── 📁 model_cards/
│       ├── 📄 README.md                                       — 🧬 Model cards index
│       └── 📄 climate_anomaly_net_v3.md                        — 🌡️ CAN-v3 (example upstream model)
├── 📁 src/
│   └── 📁 pipelines/
│       └── 📁 climate/
│           ├── 📁 config/                                      — ⚙️ Deterministic YAML configs
│           ├── ⚙️ downscale_v11.py                              — 🌦️ Downscaling entrypoint (example)
│           ├── ⚙️ bias_correct_v11.py                           — 🎛️ Bias correction entrypoint (example)
│           └── ⚙️ validate_climate_outputs_v11.py               — ✅ Validation entrypoint (example)
├── 📁 schemas/
│   └── 📁 telemetry/
│       └── 📄 mcp-sops-v11.json                                 — 📊 SOP telemetry schema
├── 📁 data/
│   ├── 📁 raw/
│   │   └── 📁 climate/                                          — 🧊 Raw climate sources (as acquired)
│   ├── 📁 work/
│   │   └── 📁 climate_downscaling/                               — 🧰 Intermediate deterministic artifacts
│   ├── 📁 processed/
│   │   └── 📁 climate/
│   │       └── 📁 downscaled/
│   │           └── 📁 v11/                                       — 🌦️ Final downscaled + bias-corrected outputs
│   ├── 📁 stac/
│   │   └── 📁 climate/                                          — 🗂️ STAC Collections/Items for climate products
│   └── 📁 provenance/
│       └── 📁 experiments/
│           └── 📁 climate/                                      — 🧬 PROV-O bundles + OpenLineage refs
└── 📁 .github/
    └── 📁 workflows/
        └── 📄 mcp-validate.yml                                   — ✅ CI gates for governed docs + artifacts
~~~

---

## 🧭 Context

### ✅ Preconditions
Before executing this SOP, ensure:
1. 📦 **Inputs are acquired and pinned**
   - Sources exist under `data/raw/climate/` (or pointer-managed equivalents).
   - Source licensing/rights and retrieval metadata are recorded.

2. 🧾 **Data contract is satisfied**
   - Climate contract reference: `KFM-PDC v11 — climate.json`
   - Units, variable names, and required metadata fields are declared in config.

3. ⚙️ **Determinism controls are declared**
   - seed(s)
   - config hash
   - toolchain versions / container tag
   - calibration period (start/end)

4. 🗺️ **Spatial scope is pinned**
   - Kansas bounds mask and target grid are pinned in config.
   - Reprojection policy is pinned (EPSG:4326 default unless contract overrides).

5. 🛡️ **Governance posture is set**
   - Climate layers are generally low sensitivity, but:
     - overlays that feed narrative or sovereignty-tagged map contexts must respect integration masking rules.
     - governance labels must be present in STAC/DCAT metadata.

### 🧩 Required inputs
- 🌡️ climate datasets (examples by category; actual list is config-driven):
  - reference climatology/baseline (trusted observations/grids)
  - reanalysis/hindcast grids
  - projection grids (if permitted and governance-approved)
- 🧾 metadata stubs (or autogen plan):
  - STAC Item/Collection scaffolds
  - DCAT dataset mapping fields
- ⚙️ pipeline config:
  - target grid, resolution, timestep
  - calibration window
  - downscaling methods
  - bias correction method + constraints
- 🧪 validation thresholds:
  - metric bounds and acceptable failure tolerances

### 🧷 Required variable conventions (contract-driven)
Common climate variables (examples):
- `tas` — near-surface air temperature (°C)
- `pr` — precipitation (mm/day)
- anomaly variants when produced:
  - `anom_tas`
  - `anom_pr`

All variables must include:
- units
- temporal resolution
- spatial grid definition
- provenance references

---

## 🗺️ Diagrams

~~~mermaid
flowchart TD
  A[🟢 Start: select sources + config] --> B[📥 Load raw grids + metadata]
  B --> C[🧾 Contract validation + unit/CRS checks]
  C --> D[🗺️ Spatial downscaling to target grid]
  D --> E[🕒 Temporal harmonization / downscaling]
  E --> F[🎛️ Bias correction (QM / Delta / BCSD hybrids)]
  F --> G[✅ Validation (stats + extremes + sanity constraints)]
  G --> H{Pass?}
  H -->|No| I[🛠️ Tune bounded params + rerun]
  H -->|Yes| J[📦 Write outputs + STAC/DCAT]
  J --> K[🧬 Write PROV-O + OpenLineage refs]
  K --> L[📊 Telemetry write + CI gates]
  L --> M[🚦 Publish / integrate (hydrology, hazards, Focus Mode)]
~~~

---

## 🧱 Architecture

### 🛠️ Procedure (deterministic workflow)

#### Step 1 — Load raw climate data
- load multiband rasters / NetCDF grids from `data/raw/climate/`
- validate:
  - time axis completeness and ordering
  - CRS tags present and consistent
  - units present and contract-compliant
  - variable names match contract mapping

Hard rejects:
- missing or inconsistent timestamps
- missing CRS tags that cannot be deterministically inferred
- units that do not match contract and cannot be deterministically converted

#### Step 2 — Normalize to KFM climate canonical form
- normalize to CF-style conventions (as required by contract)
- standardize:
  - units (e.g., K → °C)
  - variable naming (`tas`, `pr`, etc.)
  - time encoding (UTC recommended; pinned by config)
- write deterministic normalization logs

Write intermediates:
~~~text
data/work/climate_downscaling/normalized/<run-id>/
~~~

#### Step 3 — Spatial downscaling (target grid production)
Allowed spatial methods (select by variable type in config):
- temperature/anomalies: bilinear or bicubic interpolation
- precipitation/flux-like variables: conservative remapping
- terrain-sensitive adjustments (when enabled):
  - elevation lapse rate correction
  - DEM-driven adjustments (pinned DEM asset/version)

Outputs:
- target-grid fields at configured resolution (e.g., 1 km)
- stored as GeoTIFF or NetCDF as declared in config

Record in run report:
- method, parameters
- target CRS/grid fingerprint
- DEM asset/version (if used)

#### Step 4 — Temporal harmonization and downscaling
Common cases:
- monthly → daily
- hourly → daily
- daily alignment across multiple sources

Allowed temporal methods (config-driven):
- deterministic decomposition + reconstruction
- spline interpolation with pinned smoothing parameters
- Gaussian kernel redistribution (bounded)
- rolling climatology alignment

Validation at this stage:
- preserved monthly totals/means (as appropriate)
- no negative precipitation
- temperature bounds remain physical for region and season

Write intermediates:
~~~text
data/work/climate_downscaling/temporal/<run-id>/
~~~

#### Step 5 — Bias correction (distribution alignment)
Allowed bias correction methods (config-driven):
- Quantile Mapping (QM) with bounded tails
- Delta Method (additive/multiplicative as appropriate)
- CDF-based scaling
- LOESS-based correction (fixed smoothing)
- BCSD-style hybrid pipelines (when enabled)

Safeguards (required):
- physical constraints:
  - precip ≥ 0
  - bounded extremes (configured clipping policy)
- calibration window pinned (e.g., 1981–2010)
- out-of-window behavior constrained (no uncontrolled extrapolation)

Write:
~~~text
data/work/climate_downscaling/bias_corrected/<run-id>/
~~~

#### Step 6 — Validation (accept/reject gates)
Run validation suite:
- distribution match vs reference during calibration window:
  - RMSE / MAE
  - bias (%)
  - seasonal retention score
- extremes handling:
  - extreme quantile behavior within configured tolerance
- spatial coherence checks:
  - smoothness constraints appropriate to variable
  - no seam artifacts across tiles
- sanity checks:
  - no missing timestamps
  - no CRS drift
  - unit correctness verified

If fails:
- adjust only **bounded** parameters declared as tunable in config
- rerun from the earliest affected stage
- record delta in run report and provenance activity

#### Step 7 — Export final products
Write final outputs:
~~~text
data/processed/climate/downscaled/v11/<product-id>/
~~~

Recommended contents:
- final gridded outputs
- run report (method + config fingerprint)
- validation metrics summary
- checksums

#### Step 8 — Publish gate (repo + release)
- generate STAC/DCAT artifacts
- write provenance bundle
- write telemetry
- pass CI checks before downstream integration

---

## 📦 Data & Metadata

### 📤 Output packaging (normative)
Each product must include:
- 🧊 climate grids (GeoTIFF or NetCDF) with clear naming
- 🧾 `run_report.json` capturing:
  - input IDs and versions
  - config hash
  - seed(s)
  - toolchain/container tag
  - calibration window
  - methods used by stage
- ✅ `metrics.json` capturing validation results
- 🔐 checksums file (or checksum fields inside run report)

Suggested structure:
~~~text
data/processed/climate/downscaled/v11/<product-id>/
├── 🌦️ grids/                         # GeoTIFF/NetCDF outputs
├── ✅ metrics.json                    # Validation metrics
├── 🧾 run_report.json                 # Config + method summary
└── 🔐 checksums.json                  # Output integrity
~~~

### 🧾 Required metadata fields (minimum)
For each product:
- title, description
- spatial extent (Kansas bounds; geometry as appropriate)
- temporal extent
- resolution + grid fingerprint
- variables + units
- license
- care_label + fair_category (even when low sensitivity)
- provenance pointers

---

## 🌐 STAC, DCAT & PROV Alignment

### 🗂️ STAC
- Create:
  - a STAC **Collection** for the climate downscaling product family
  - STAC **Item** per product (or per time-bounded chunk, if configured)

Suggested locations:
~~~text
data/stac/climate/downscaled_v11/collection.json
data/stac/climate/downscaled_v11/items/<item-id>.json
~~~

STAC Item must include:
- spatial geometry/bbox
- datetime / start_datetime / end_datetime
- asset links to output grids + metrics + run report
- processing properties:
  - `processing:workflow = climate_downscaling_v11`
  - `processing:method = <method>`
  - `processing:calibration_period = <start/end>`

### 🧾 DCAT
DCAT record must include:
- publisher/creator
- license
- keywords
- spatial + temporal coverage
- distributions that point to STAC assets (or direct file paths where required)
- lineage references (PROV)

### 🧬 PROV-O + OpenLineage references
Every run must produce a provenance bundle recording:
- entities:
  - raw source datasets
  - intermediate normalized products
  - final downscaled products
- activities:
  - normalize → spatial_downscale → temporal_downscale → bias_correct → validate → publish
- agents:
  - pipelines/services/reviewers (as applicable)

Write provenance bundles under:
~~~text
data/provenance/experiments/climate/<timestamp>/
~~~

OpenLineage reference event names (references only; no secrets):
~~~text
climate.downscaling
climate.bias_correction
~~~

---

## 🧠 Story Node & Focus Mode Integration

Climate downscaled products may be used for:
- 💧 hydrology forcing generation (reconstruction pipelines)
- 🌊 hazard overlays (flood/drought context layers)
- 🧠 Focus Mode v3 context panels (quantitative climate facts)
- 📖 Story Node v3 environmental context (with evidence links)

Rules:
- climate layers are not narratives; any narrative claim must cite the dataset/STAC item
- no “forecast certainty” language when outputs are reconstructions/bias-corrected products
- when intersecting sovereignty-tagged narrative surfaces:
  - follow integration masking/generalization requirements
  - avoid implying protected community impacts without governance review

---

## 🧪 Validation & CI/CD

### ✅ Local runbook (recommended)
~~~bash
# 1) Downscale (example)
python -m src.pipelines.climate.downscale_v11 \
  --config src/pipelines/climate/config/downscale_v11.yaml \
  --product_id <product-id>

# 2) Bias correct (example)
python -m src.pipelines.climate.bias_correct_v11 \
  --config src/pipelines/climate/config/bias_correct_v11.yaml \
  --product_id <product-id>

# 3) Validate (example)
python -m src.pipelines.climate.validate_climate_outputs_v11 \
  --config src/pipelines/climate/config/validate_v11.yaml \
  --product_id <product-id>
~~~

### ✅ CI expectations (minimum)
- markdown-lint (KFM-MDP structure + heading registry)
- metadata-check (front matter completeness)
- diagram-check (Mermaid parse)
- provenance-check (bundle present + coherent references)
- schema-lint (telemetry/schema alignment where applicable)
- secret-scan + pii-scan
- footer-check (governance links present)

### 🎯 Acceptance criteria (configured thresholds)
Must pass thresholds declared in config (examples):
- bias under threshold during calibration window
- physically plausible bounds
- temporal completeness and no missing timestamps
- no CRS drift and grid fingerprint matches target

---

## ⚖ FAIR+CARE & Governance

### 🤝 FAIR posture
Climate downscaling outputs must be:
- Findable: STAC/DCAT records created
- Accessible: formats declared + readable by standard tools
- Interoperable: CRS + units + variable naming contract
- Reusable: CC-BY + provenance + validation metrics

### 🪶 CARE + sovereignty posture
Even when the climate data is low sensitivity:
- do not use outputs to imply sensitive community impacts without review
- ensure sovereignty-related integration layers apply masking/generalization rules
- if any restricted geographies are used as overlays, route through governance gates

### 🧭 Ethics posture
- avoid misleading certainty in narratives derived from corrected grids
- present uncertainty where available (metrics + bounds)
- document limitations in run reports and downstream usage notes

---

## 🕰️ Version History

| Version | Date | Summary |
|---:|---|---|
| v11.0.0 | 2025-11-23 | Initial climate downscaling SOP for KFM-MCP v11. |
| v11.0.0 | 2025-12-13 | Updated to KFM-MDP v11.2.6 structure (approved H2 registry, directory layout profile, badges, governed footer, deterministic stage breakdown). |

---

<div align="center">

[🏛️ Governance Charter](../../docs/standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../docs/standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
MCP-DL v6.3 · KFM-MDP v11.2.6 · KFM-OP v11.0 · KFM-PDC v11.0 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>
