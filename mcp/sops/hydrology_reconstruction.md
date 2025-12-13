---
title: "💧 KFM SOP — Hydrology Time-Series Reconstruction & Multi-Source Fusion (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "mcp/sops/hydrology_reconstruction.md"

version: "v11.0.0"
last_updated: "2025-12-13"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Hydrology Working Group · FAIR+CARE Council"
status: "Active / Enforced"
content_stability: "stable"

doc_kind: "SOP"
intent: "hydrology-reconstruction"
semantic_document_id: "kfm-sop-hydrology-reconstruction"
doc_uuid: "urn:kfm:mcp:sop:hydrology-reconstruction:v11.0.0"
event_source_id: "ledger:kfm:mcp:sop:hydrology-reconstruction:v11.0.0"
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
sensitivity: "Mixed"
fair_category: "F1-A1-I2-R2"
care_label: "Responsibility · Ethics · Stewardship"
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
  - "metadata-extraction"
  - "layout-normalization"
  - "a11y-adaptations"
  - "diagram-extraction"
ai_transform_prohibited:
  - "speculative-additions"
  - "unverified-hydrology-claims"
  - "regulatory-decision-output"
  - "tribal-water-use-inference"
  - "sensitive-coordinate-exposure"
  - "governance-override"
  - "fabricate-provenance"

provenance_chain:
  - "prov:Plan:urn:kfm:mcp:sop:hydrology-reconstruction:v11.0.0"
---

<div align="center">

# 💧 **KFM SOP — Hydrology Time-Series Reconstruction & Multi-Source Fusion (v11 LTS)**
`mcp/sops/hydrology_reconstruction.md`

**Purpose**  
Define the **deterministic, multi-source, reproducible** procedure for reconstructing hydrologic time-series (streamflow, reservoir inflow/outflow, storage, sedimentation-adjusted series) using observed data, governed AI inference, climate forcings, and geospatial constraints — aligned with **FAIR+CARE**, sovereignty protections, and **KFM-PDC v11**.

<img src="https://img.shields.io/badge/MCP--DL-v6.3-blueviolet" />
<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/Hydrology-Reconstruction-informational" />
<img src="https://img.shields.io/badge/FAIR%2BCARE-Governed-orange" />
<img src="https://img.shields.io/badge/Sovereignty-Enforced-critical" />
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
This SOP applies to:
- 🏞️ reservoir inflow/outflow reconstruction
- 📈 daily streamflow gap-fills (e.g., missing gauge periods)
- 🪨 sedimentation-adjusted reservoir histories
- 🧭 hindcast / backfill hydrology inference (within governed windows)
- 🧩 multi-source fusion of:
  - USGS gauges
  - USACE reservoir operations
  - Kansas Mesonet precipitation / ET
  - climate hindcasts / reanalysis (ERA5, PRISM)
  - governed AI reconstructions (Seq2Seq + auxiliary models)

This SOP governs:
- deterministic ingestion + temporal harmonization
- gap-filling and reconstruction (with method tags)
- bias correction and uncertainty quantification
- STAC/DCAT record generation for outputs
- lineage capture (PROV-O + OpenLineage references)
- CARE + sovereignty masking rules for sensitive basins/geographies

### 🧷 Non-negotiables
- **Deterministic workflow:** same inputs + config → same outputs (seeded where applicable).
- **No “forecasting” claims:** this SOP produces reconstructions and gap-fills, not emergency forecasts.
- **Sovereignty-first:** restricted basins and sensitive water-use implications are masked/routed for review.
- **Provenance is mandatory:** outputs without lineage do not pass validation.

---

## 🗂️ Directory Layout

~~~text
📁 KansasFrontierMatrix/
├── 📁 mcp/
│   ├── 📁 sops/
│   │   └── 📄 hydrology_reconstruction.md                — 💧 This SOP
│   ├── 📁 experiments/
│   │   ├── 📄 README.md                                  — 🧪 Experiments index
│   │   └── 📄 2025-11-02_HYDRO-EXP-002.md                 — 💧 Fusion validation experiment (example reference)
│   └── 📁 model_cards/
│       ├── 📄 README.md                                  — 🧬 Model cards index
│       └── 📄 hydrology_seq2seq_v11.md                    — 💧 Hydrology Seq2Seq model card (example reference)
├── 📁 src/
│   └── 📁 pipelines/
│       └── 📁 hydrology/
│           ├── 📁 config/                                 — ⚙️ Deterministic pipeline configs (YAML)
│           ├── ⚙️ reconstruct_timeseries_v11.py            — 🧪 Reconstruction entrypoint (example)
│           ├── ⚙️ multisource_fusion_v11.py                — 🧩 Fusion entrypoint (example)
│           └── ⚙️ validate_outputs_v11.py                  — ✅ Validation entrypoint (example)
├── 📁 schemas/
│   └── 📁 telemetry/
│       └── 📄 mcp-sops-v11.json                            — 📊 Telemetry schema (SOPs)
├── 📁 data/
│   ├── 📁 raw/
│   │   ├── 📁 hydrology/
│   │   │   ├── 📁 usgs/                                    — 📈 Raw gauge series (as acquired)
│   │   │   └── 📁 usace/                                   — 🏞️ Reservoir ops (as acquired)
│   │   └── 📁 climate/                                     — 🌦️ Climate forcings (as acquired)
│   ├── 📁 processed/
│   │   └── 📁 hydrology/
│   │       └── 📁 reconstructed/
│   │           └── 📁 v11/                                 — 💧 Reconstructed + fused outputs
│   ├── 📁 stac/
│   │   └── 📁 hydrology/                                   — 🗂️ STAC Collections/Items for hydrology products
│   └── 📁 provenance/
│       └── 📁 experiments/
│           └── 📁 hydrology/                               — 🧬 PROV-O bundles + OpenLineage refs
└── 📁 .github/
    └── 📁 workflows/
        └── 📄 mcp-validate.yml                              — ✅ CI gates for governed docs + artifacts
~~~

---

## 🧭 Context

### ✅ Preconditions (must be satisfied before running)
1. **Contract readiness**
   - Confirm the hydrology data contract is available and referenced by pipeline config.
   - Contract identifier: `KFM-PDC v11 — hydrology.json`

2. **Time + CRS conventions**
   - Timeseries are harmonized to a common timestep (daily by default).
   - Time normalization uses a declared timezone strategy (UTC recommended).
   - Spatial layers align to `EPSG:4326` unless contract specifies otherwise.

3. **Dataset governance classification**
   - Each dataset must carry licensing/rights metadata.
   - CARE + sovereignty tags must be applied where relevant.
   - Restricted basins/geographies must be masked/generalized per sovereignty policy.

4. **Required input metadata**
   Every input MUST declare:
   - time coverage
   - spatial bounding box (if spatial)
   - units
   - sampling frequency
   - provenance reference (STAC/DCAT ID, source manifest, or governance ledger pointer)

### 🗂️ Required inputs
- **Hydrology observations**
  - USGS gauge series (daily or sub-daily)
  - USACE reservoir ops (inflow/outflow/storage)

- **Climate forcings**
  - Mesonet precipitation / ET / temperature
  - ERA5 / PRISM hindcast or reanalysis forcings (as permitted)

- **Geospatial constraints**
  - DEM and watershed boundaries / basin features
  - basin similarity embeddings (if used)

- **Models (optional but governed)**
  - Hydrology Seq2Seq model (if used) must have an approved model card and pinned version.

### 🧾 Determinism controls (required when AI is used)
- Config hash recorded per run
- Seed(s) recorded per run
- Model versions recorded per run
- Hardware / environment fingerprint recorded per run (container tag + SBOM reference)

---

## 🗺️ Diagrams

~~~mermaid
flowchart TD
  A[🟢 Start: basin or asset selection] --> B[📥 Load sources: USGS / USACE / climate forcings]
  B --> C[🧾 Validate metadata + contract checks]
  C --> D[🕒 Temporal harmonization + gap mask]
  D --> E{Gap class?}
  E -->|Short (1–7d)| F[🔧 Deterministic interpolation / filter]
  E -->|Mid (1w–1m)| G[🧩 Regression + neighbor imputation]
  E -->|Long (>1m)| H[🤖 Climate-driven + Seq2Seq inference (governed)]
  F --> I[📈 Candidate recon series]
  G --> I
  H --> I
  I --> J[🪨 Reservoir sedimentation adjustment (if applicable)]
  J --> K[🧠 Multi-source fusion + uncertainty]
  K --> L[✅ Validation (RMSE/MAE/NSE + seasonal + extremes)]
  L --> M{Pass thresholds?}
  M -->|No| N[🛠️ Tune weights / rerun constrained steps]
  M -->|Yes| O[🗂️ Write outputs + STAC/DCAT + PROV-O]
  O --> P[🚦 Publish gate + downstream integration]
~~~

---

## 🧱 Architecture

### 🧰 Pipeline steps (deterministic reconstruction)

#### Step 1 — Load datasets & validate metadata
Load candidate sources:
- USGS gauge time-series
- USACE operations (inflow/outflow/storage)
- Mesonet precipitation / ET
- climate hindcast/reanalysis (ERA5, PRISM)
- DEM + watershed boundaries

Validate:
- timestamp parseability + monotonic ordering
- unit consistency (cfs/cms/AF/day/mm/day) per contract
- missing intervals (build a gap mask)
- spatial consistency for basin association (when used)

Reject or quarantine inputs when:
- unit mismatch cannot be resolved deterministically
- station discontinuity exceeds configured limits (unless long-gap inference is explicitly enabled)
- spatial association is ambiguous or violates sovereignty constraints

#### Step 2 — Temporal harmonization
- resample all series to the configured timestep (daily default)
- apply timezone normalization (UTC recommended)
- classify gaps:
  - short: 1–7 days
  - mid: ~1 week to 1 month
  - long: >1 month

Write the gap mask artifact (recommended):
~~~text
data/processed/hydrology/reconstructed/v11/<basin-id>/gap_mask.parquet
~~~

#### Step 3 — Gap-filling (method-tagged, deterministic)
**Short gaps (1–7 days)**  
Allowed (choose by config):
- linear interpolation (bounded)
- Kalman filter (fixed parameters)
- bias-aware spline fill (seedless deterministic)

**Mid gaps (week–1 month)**  
Allowed:
- climate-driven regression (fixed feature set)
- nearest-neighbor gauge imputation (declared neighbor list)
- watershed similarity weighting (declared embedding version)

**Long gaps (>1 month)**  
Allowed (governed):
- basin-transfer models (declared donor basins)
- climate→hydrology inference (declared forcing set)
- Seq2Seq inference (model card required; seed required)

All fills MUST write tags into the output metadata:
~~~json
{
  "fill_method": "<method>",
  "fill_confidence": 0.0,
  "fill_flags": ["<flag-a>", "<flag-b>"],
  "gap_class": "short|mid|long"
}
~~~

#### Step 4 — Sedimentation adjustment (reservoirs only; when enabled)
For sedimentation-affected reservoirs:
- load bathymetry-derived volume curves (if available)
- load dredging/operations notes (if available and permitted)
- reconstruct elevation-area-volume changes using the configured approach
- apply volume/area corrections to storage series

Write sediment-adjusted artifacts (example):
~~~text
data/processed/hydrology/reconstructed/v11/<reservoir-id>/storage_adjusted.parquet
data/processed/hydrology/reconstructed/v11/<reservoir-id>/eav_curve_v11.json
~~~

#### Step 5 — Multi-source fusion (final series + uncertainty)
Combine candidate series:
- observed gauges (USGS)
- reservoir ops (USACE)
- climate-driven inference
- terrain/basin-runoff estimates (if used)
- AI reconstruction outputs (if enabled)

Allowed fusion methods (select by config):
- weighted ensemble (deterministic optimizer)
- Bayesian model averaging (seeded)
- error-minimizing constrained regression (deterministic solver)

Outputs MUST include:
- final fused time-series
- confidence intervals / uncertainty bands
- fusion weights and diagnostics

#### Step 6 — Validation (acceptance thresholds)
Run:
- MAE / RMSE
- NSE (Nash–Sutcliffe)
- seasonal cycle retention
- autocorrelation similarity checks
- extreme event fidelity checks (flood + drought patterns)
- cross-basin transfer error checks (when enabled)

If thresholds fail, remediation is constrained:
- adjust weights within allowed bounds
- swap deterministic gap-fill strategy per config
- re-run validation with a recorded config change

---

## 📦 Data & Metadata

### 📤 Output locations (normative)
Final reconstructed products are written under:
~~~text
data/processed/hydrology/reconstructed/v11/
~~~

Recommended structure:
~~~text
data/processed/hydrology/reconstructed/v11/<basin-id>/
├── 🧾 series_fused.parquet
├── 🧾 series_sources.parquet
├── 🧾 uncertainty_bounds.parquet
├── 🧾 fusion_weights.json
├── 🧾 gap_mask.parquet
└── 🧾 run_report.json
~~~

### 🧾 Minimum output metadata (required)
Each basin/reservoir output MUST record:
- basin/reservoir identifier(s)
- time coverage
- timestep/frequency
- units
- methods used (gap-fill + fusion)
- uncertainty method
- sovereignty/masking status
- contract version + config hash
- provenance pointers (PROV-O bundle + OpenLineage refs)

---

## 🌐 STAC, DCAT & PROV Alignment

### 🗂️ STAC
- Create a **STAC Item** for each reconstructed series artifact (or basin bundle).
- Create a **STAC Collection** for broader hydrology products (statewide or domain-level).
- Ensure STAC assets include media types (e.g., `application/parquet`, `application/json`).

Suggested locations:
~~~text
data/stac/hydrology/<basin-id>/collection.json
data/stac/hydrology/<basin-id>/items/<item-id>.json
~~~

### 🧾 DCAT
- Each reconstructed product set should map to a DCAT dataset record including:
  - title/description
  - license
  - temporal coverage
  - spatial coverage (masked/generalized if required)
  - distributions (Parquet/CSV/NetCDF + metadata)
  - lineage references

### 🧬 PROV-O + OpenLineage references
Every run MUST produce a provenance bundle capturing:
- entities: raw inputs + processed outputs
- activities: harmonize, gap-fill, sediment adjust, fuse, validate, publish
- agents: pipelines, reviewers, councils (as applicable)

Write provenance bundles to:
~~~text
data/provenance/experiments/hydrology/<timestamp>/
~~~

Emit the OpenLineage event name (reference only; no secrets):
~~~text
hydrology.reconstruction
~~~

---

## 🧪 Validation & CI/CD

### ✅ Minimum validation profiles (expected)
- `markdown-lint` (structure: H1/H2, fences)
- `schema-lint` (front-matter keys)
- `metadata-check` (required keys present)
- `diagram-check` (Mermaid parse)
- `footer-check` (governance links in footer)
- `accessibility-check` (heading order, list semantics)
- `provenance-check` (run bundle present, references coherent)
- `secret-scan` + `pii-scan`

### 🧰 Local runbook (recommended)
~~~bash
# 1) Run the reconstruction (example)
python -m src.pipelines.hydrology.reconstruct_timeseries_v11 \
  --config src/pipelines/hydrology/config/reconstruct_v11.yaml \
  --basin_id <basin-id>

# 2) Run fusion (example)
python -m src.pipelines.hydrology.multisource_fusion_v11 \
  --config src/pipelines/hydrology/config/fusion_v11.yaml \
  --basin_id <basin-id>

# 3) Validate outputs (example)
python -m src.pipelines.hydrology.validate_outputs_v11 \
  --config src/pipelines/hydrology/config/validate_v11.yaml \
  --basin_id <basin-id>
~~~

### 🧯 Failure modes & recovery
Common failures:
- climate forcing mismatch (seasonal drift)
- negative flow artifacts / impossible storage changes
- fusion instability (weights oscillate)
- sedimentation correction unrealistically amplifies/erases signal
- sovereignty flag violations (attempted precision on restricted basins)

Recovery actions:
- rerun with alternative deterministic regression model (configured)
- constrain negative values with physically valid bounds
- tighten fusion regularization; clamp weights
- switch sedimentation curve source or disable sedimentation step (logged)
- apply masking/generalization and route to required governance review

---

## ⚖ FAIR+CARE & Governance

### 🪶 Sovereignty requirements (hard constraints)
- Do not publish restricted basin outputs at precision disallowed by sovereignty policy.
- Mask/generalize restricted geographies by default (H3 R7–R9 as required).
- Do not infer or expose culturally sensitive water-use patterns.
- When a basin is sovereignty-tagged, required reviewers must approve before publish.

### 🧾 CARE review routing (operational)
Trigger additional review when:
- outputs touch tribal watersheds
- results could imply sensitive water-use patterns
- reconstructions are reused in hazard narratives or public storytelling layers

### ✅ FAIR requirements (minimum)
Outputs must be:
- Findable: STAC/DCAT records
- Accessible: open formats where permitted (CSV/Parquet/NetCDF)
- Interoperable: CRS + units + contract version in metadata
- Reusable: license + lineage + uncertainty notes

---

## 🧠 Story Node & Focus Mode Integration

Hydrology reconstruction outputs may feed:
- Focus Mode v3 context panels (quantitative hydrology summaries)
- Story Node v3 environmental context layers (with evidence links)
- hazard overlays (flood/drought narratives) **only when governed and reviewed**

Rules:
- Narrative layers must reference dataset/series identifiers (STAC/DCAT IDs).
- Any basin/geography requiring masking must remain masked in UI outputs.
- Hydrology reconstructions must be presented as reconstructions (not forecasts).

---

## 🕰️ Version History

| Version | Date | Summary |
|---:|---|---|
| v11.0.0 | 2025-11-23 | Initial hydrology reconstruction SOP for KFM-MCP v11 (governed, deterministic). |
| v11.0.0 | 2025-12-13 | Updated to KFM-MDP v11.2.6 layout rules (approved H2 registry, tilde fences, directory layout profile, governed footer). |

---

<div align="center">

[🏛️ Governance Charter](../../docs/standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../docs/standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
MCP-DL v6.3 · KFM-MDP v11.2.6 · KFM-OP v11.0 · KFM-PDC v11.0 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>
