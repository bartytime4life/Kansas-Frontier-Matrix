---
title: "🌫️ Kansas Frontier Matrix — CAMS NRT PM2.5 Gap-Fill Pipeline (Bias-Corrected · STAC+PROV)"
path: "docs/data/air-quality/cams-nrt-gapfill/README.md"
version: "v11.2.6"
last_updated: "2025-12-13"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Air Quality Systems Board · FAIR+CARE Council"
content_stability: "stable"
status: "Active / Enforced"

doc_kind: "Pipeline Design + Ops Runbook"
header_profile: "standard"
footer_profile: "standard"
diagram_profiles:
  - "mermaid-flowchart-v1"

intent: "use-cams-nrt-to-gapfill-pm25-streams"
audience:
  - "Data Engineering"
  - "Air Quality Science"
  - "Graph + Catalog Engineering"
  - "Reliability + Governance"

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

governance_ref: "../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"
classification: "Public"
sensitivity: "General (non-sensitive; auto-mask rules apply)"
sensitivity_level: "None"
public_exposure_risk: "Low"
jurisdiction: "Kansas / United States"
indigenous_rights_flag: true
data_steward: "Air Quality Systems Board · FAIR+CARE Council"

doc_uuid: "urn:kfm:doc:data:air-quality:cams-nrt-gapfill:v11.2.6"
semantic_document_id: "kfm-cams-nrt-gapfill-v11.2.6"
event_source_id: "ledger:kfm:doc:data:air-quality:cams-nrt-gapfill:v11.2.6"
commit_sha: "<latest-commit-hash>"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summary"
  - "timeline-generation"
  - "semantic-highlighting"
  - "diagram-extraction"
  - "metadata-extraction"
  - "layout-normalization"
ai_transform_prohibited:
  - "content-alteration"
  - "speculative-additions"
  - "unverified-architectural-claims"
  - "narrative-fabrication"
  - "governance-override"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

tags:
  - "air-quality"
  - "pm25"
  - "cams"
  - "ecmwf"
  - "gapfill"
  - "bias-correction"
  - "stac"
  - "prov"
---

<div align="center">

# 🌫️ **Kansas Frontier Matrix — CAMS NRT PM2.5 Gap-Fill Pipeline**

`docs/data/air-quality/cams-nrt-gapfill/README.md`

**Purpose**  
Define a **deterministic, provenance-enforced** pipeline to gap-fill Kansas PM₂.₅ station/sensor time series using **ECMWF/CAMS near-real-time (NRT) surface PM₂.₅** with **short-window bias correction**, emitting **STAC Items** and **PROV-O lineage** for every derived artifact.

<img src="https://img.shields.io/badge/MCP--DL-v6.3-blueviolet" />
<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/KFM--PDC-v11-blue" />
<img src="https://img.shields.io/badge/STAC%2BPROV-Aligned-brightgreen" />
<img src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />

</div>

---

## 📘 Overview

This module defines a replayable recipe to gap-fill Kansas PM₂.₅ observation streams using CAMS NRT model fields, while preserving explicit lineage:

- Which CAMS product / cycle / valid time / lead time?
- Which spatial + temporal collocation method + tolerance window?
- Which bias method and parameterization?
- Which algorithm version + code commit?

### Pipeline steps (high-level)

1. **Ingest CAMS NRT surface PM₂.₅** for a Kansas AOI (plus buffer).
2. **Collocate** model grid values to station/sensor observations (space + time).
3. Fit **short-window bias correction** (station-local by default).
4. **Fill gaps** in observation series using **bias-corrected CAMS** estimates.
5. Emit **STAC Items** + **PROV-O bundles** for every derived output.

### Outputs (governed artifacts)

- `collocations` (station × time collocations; Parquet)
- `bias_model` (per-station or pooled model parameters; JSON)
- `pm25_gapfilled` (station time series with fill metadata; Parquet)
- `stac_item` (STAC Item JSON referencing outputs)
- `prov_bundle` (PROV-O JSON-LD referencing sources + activities)

---

## 🗂️ Directory Layout

~~~text
📁 docs/data/air-quality/cams-nrt-gapfill/
├── 📄 README.md                                 — This governed pipeline spec
├── 📁 specs/                                    — Contracts + profiles (PDC/STAC/PROV)
│   ├── 🧾 cams_gapfill_contract.kfm-pdc.v11.json  — Pipeline contract (inputs/outputs/params)
│   ├── 🧾 stac_item_profile.kfm-stac.v11.json     — STAC Item profile for derived outputs
│   └── 🧾 prov_profile.kfm-prov.v11.jsonld        — PROV profile for lineage bundles
├── 📁 configs/                                  — Replayable, deterministic runtime configs
│   ├── 🧾 cams_ads_query.yml
│   ├── 🧾 collocation.yml
│   ├── 🧾 bias_model.yml
│   └── 🧾 gapfill_policy.yml
├── 📁 examples/                                 — Sample artifacts for validators/tests
│   ├── 🧾 sample_stac_item.json
│   ├── 🧾 sample_prov_bundle.jsonld
│   └── 🧾 sample_timeseries.parquet
└── 📁 runbooks/                                 — Ops runbooks (SLOs, incidents, backfills)
    ├── 📄 reliability_slo.md
    ├── 📄 incident_playbook.md
    └── 📄 backfill_procedure.md
~~~

---

## 🧭 Context

### Objective

Map each station observation `(lat, lon, t_obs)` to a CAMS value `CAMS_PM25(cell, t_model)` with controlled tolerances, then correct local model bias and use the corrected estimate to fill missing PM₂.₅ points.

### Why short-window bias correction?

CAMS bias is typically **location-dependent** and can drift with synoptic regimes, transport, and emissions patterns. A short training window improves agility while keeping production stable.

Default governed posture:

- Rolling window: **14 days** (configurable 7–21)
- Minimum samples per station: **N ≥ 50** (configurable)
- If insufficient: **regional pooling** or **no correction** (policy-gated)

### External references (pinned anchors)

- [CAMS global atmospheric composition forecasts (ADS landing)](https://ads.atmosphere.copernicus.eu/datasets/cams-global-atmospheric-composition-forecasts)
- [ECMWF dataset page: CAMS global forecasts](https://www.ecmwf.int/en/forecasts/dataset/cams-global-atmospheric-composition-forecasts)
- [ECMWF charts: particulate matter forecasts](https://charts.ecmwf.int/products/particulate-matter-forecasts)
- [ECMWF story: tracking air pollution](https://stories.ecmwf.int/tracking-air-pollution/index.html)
- [CAMS global system evaluation context (ACP, 2024)](https://acp.copernicus.org/articles/24/9475/2024/)

---

## 📦 Data & Metadata

### Inputs

#### 1) CAMS NRT (global atmospheric composition forecasts)

Recommended source: Copernicus Atmosphere Data Store (ADS), CAMS global composition forecasts.

- Primary variable: surface **PM2.5** (µg/m³)
- Optional covariates (if used/available): PBL height, RH, wind, etc.
- Temporal cadence: product-dependent (often issued in operational cycles; capture `cycle` and `valid_time`)
- Spatial: coarse grid; representation error vs point monitors is expected

Suggested storage (raw):

- `data/air-quality/raw/cams/global-forecasts/...` (NetCDF/Zarr/Parquet tiles)
- Store Kansas AOI + buffer (e.g., 100–200 km)

#### 2) Ground observations

Any of:

- EPA AQS / AirNow stations
- OpenAQ streams
- PurpleAir (after harmonization / QA)
- Tribal / local networks (**sovereignty policy gates apply**)

Suggested storage (raw):

- `data/air-quality/raw/aqs/...`
- `data/air-quality/raw/openaq/...`
- `data/air-quality/raw/purpleair/...`

### Collocation record schema (row-wise)

| field               | meaning                       |
| ------------------- | ----------------------------- |
| station_id          | canonical KFM station node id |
| obs_time_utc        | observation timestamp         |
| obs_pm25_ugm3       | observed PM₂.₅                |
| cams_cycle_utc      | CAMS base time                |
| cams_valid_time_utc | CAMS valid time               |
| cams_lead_hours     | valid - cycle                 |
| cams_pm25_ugm3      | raw CAMS PM₂.₅ at collocation |
| spatial_method      | nearest / bilinear / IDW-grid |
| temporal_method     | nearest / linear-interp       |
| rep_error_class     | optional categorical metadata |

Persist collocations (processed):

- `data/air-quality/processed/collocations/cams_pm25_station/*.parquet`
- Partition by `date`, `region`, `cams_cycle_utc`

### Bias model artifact (minimum fields)

Every fit MUST record:

- Training window start/end
- Sample counts and station set
- Method name + hyperparameters
- Random seed(s) if applicable
- Coefficients + fit diagnostics

Persist per cycle/day:

- `data/air-quality/processed/bias-models/cams_pm25/<yyyy>/<mm>/<dd>/model.json`

### Gap-filled time series record (minimum fields)

Recommended columns for `pm25_gapfilled` Parquet:

| field              | meaning |
| ------------------ | ------- |
| station_id         | canonical station id |
| time_utc           | timestamp |
| pm25_obs_ugm3      | observed (nullable) |
| pm25_filled_ugm3   | filled value (nullable if not filled) |
| pm25_final_ugm3    | chosen output value (obs if present else filled) |
| is_imputed         | boolean |
| fill_class         | `none` \| `cams_corrected` \| `cams_raw_fallback` \| `regional_pool_corrected` |
| cams_cycle_utc     | provenance |
| cams_valid_time_utc| provenance |
| cams_lead_hours    | provenance |
| bias_method        | provenance |
| bias_params_hash   | provenance |
| qa_flags           | JSON (policy + sanity checks) |

Persist (processed):

- `data/air-quality/processed/timeseries/pm25_gapfilled/<station_id>.parquet`

---

## 🧱 Architecture

### Collocation method (defaults)

Objective: Map each station observation to a model value with controlled spatial/temporal tolerance.

Governed defaults:

- Spatial: **nearest grid cell** or **bilinear** (configurable)
- Temporal: nearest model time within **±90 minutes** (configurable)
- Capture `cams_cycle_utc`, `cams_valid_time_utc`, and `cams_lead_hours` as first-class provenance

### Bias correction (ranked options)

1. **Local robust linear model** (default)  
   `obs = a + b * cams` per station (or per H3 cell), robust regression (Huber/RANSAC).
2. **Local IDW residual field**  
   residual `r = obs - cams`, interpolate residuals across neighbors (IDW in H3/space).
3. **Lead-time stratified linear**  
   coefficients by lead buckets (0–6, 6–12, …).
4. **Probabilistic calibration (EMOS)** (future/optional)  
   use only if emitting distributions (not point-only).

### Gap-fill policy (core logic)

Fill only when:

- Observation is missing/invalid by QA rules
- Station is eligible (not sovereignty-restricted / embargoed)
- CAMS value exists within permitted lead-time bucket

For each missing `(station_id, t)`:

1. Collocate CAMS to station at `t` (or nearest within tolerance).
2. Apply correction:
   - `pm25_filled = clamp(a + b * cams_pm25, floor=0, ceiling=1000)`  
     or
   - `pm25_filled = clamp(cams_pm25 + residual_interp, floor=0, ceiling=1000)`
3. Tag record with imputation metadata and provenance fields.

### Configuration surface (governed)

#### `configs/collocation.yml`

~~~yaml
spatial_method: nearest  # nearest|bilinear
temporal_tolerance_minutes: 90
max_station_to_grid_km: 60
~~~

#### `configs/bias_model.yml`

~~~yaml
window_days: 14
method: robust_linear  # robust_linear|idw_residual|lead_stratified
min_samples: 50
lead_buckets: [0, 6, 12, 18, 24, 48, 72, 120]
~~~

#### `configs/gapfill_policy.yml`

~~~yaml
enable_gapfill: true
max_lead_hours: 24
fallback_to_raw: false
clamp_floor: 0
clamp_ceiling: 1000
~~~

### Neo4j graph mapping (minimum viable)

#### Nodes

- `:Station {station_id, name, owner, h3}`
- `:ModelRun {model:'CAMS', cycle_utc, dataset_id}`
- `:BiasModel {method, window_days, params_hash}`
- `:TimeSeries {metric:'PM25', station_id, date}`

#### Relationships

- `(:TimeSeries)-[:DERIVED_FROM]->(:ModelRun)`
- `(:TimeSeries)-[:DERIVED_FROM]->(:Station)` (observations)
- `(:BiasModel)-[:CALIBRATES]->(:ModelRun)`
- `(:BiasModel)-[:TRAINED_ON]->(:Station)` (or station set)
- `(:TimeSeries)-[:USES_MODEL]->(:BiasModel)`

Mapping file location:

- `docs/graph/mappings/air_quality_pm25_gapfill.yml`

---

## 🗺️ Diagrams

~~~mermaid
flowchart TD
  A[CAMS NRT PM2.5 fields] --> B[Ingest + subset AOI]
  C[Station PM2.5 observations] --> D[QA + normalize units]
  B --> E[Collocate model to stations]
  D --> E
  E --> F[Fit bias model (rolling window)]
  F --> G[Gap-fill missing station points]
  E --> G
  G --> H[Write processed artifacts]
  H --> I[Emit STAC Items]
  H --> J[Emit PROV bundles]
~~~

---

## 🌐 STAC, DCAT & PROV Alignment

### STAC (what gets an Item)

Emit STAC Items for:

- Daily station time series bundles (gap-filled)
- Regional tiles (H3 or raster grids) of corrected CAMS PM₂.₅ (if generated)
- Bias model artifacts (as “model” assets) when appropriate

STAC Item minimums:

- `id`: `urn:kfm:aq:pm25:gapfill:<station_id>:<date>`
- `collection`: `kfm-aq-pm25-gapfill`
- `datetime`: day start (or exact time for point items)
- `geometry`: station point (or `null` for non-spatial artifacts where permitted)
- `assets`:
  - `timeseries_parquet` (filled series)
  - `collocations_parquet` (optional)
  - `bias_model_json` (optional)
  - `qa_report_json` (optional)

Required STAC properties (provenance-critical):

- `kfm:source_models` (array of CAMS identifiers)
- `kfm:cams_product`
- `kfm:cams_cycle_utc`, `kfm:cams_valid_time_utc`, `kfm:cams_lead_hours`
- `kfm:collocation_window_minutes`
- `kfm:bias_method`, `kfm:bias_window_days`, `kfm:bias_params_hash`
- `kfm:algorithm_version`, `kfm:code_commit_sha`
- `kfm:fill_policy_version`
- `kfm:data_rights_class`, `kfm:sovereignty_gate`

### DCAT (minimum mapping)

For published derivatives:

- `dct:identifier` SHOULD use the same stable identifier as STAC `id` (or a canonical dataset id).
- `dct:provenance` SHOULD summarize source roll-up (CAMS + observation providers).
- `dct:license` MUST match the governed output license policy for the derivative.

### PROV-O lineage (minimum set)

#### Entities

- Raw:
  - `cams_field_<cycle>_<valid>`
  - `station_obs_<station_id>_<day>`
- Derived:
  - `collocations_<station_id>_<day>`
  - `bias_model_<station_id>_<day>`
  - `pm25_gapfilled_<station_id>_<day>`

#### Activities

- `ingest_cams`
- `collocate_cams_to_station`
- `fit_bias_model`
- `gapfill_timeseries`
- `emit_stac_item`

#### Agents

- `kfm_pipeline_runner`
- `kfm_ci_validator`

#### Relations

- `prov:used` (gapfill uses collocations + bias model + CAMS field)
- `prov:wasGeneratedBy` (outputs generated by activities)
- `prov:wasAssociatedWith` (activities associated with pipeline agent)
- `prov:wasDerivedFrom` (final series derived from obs + CAMS)

Persist:

- `data/air-quality/processed/prov/pm25_gapfill/<date>/<station_id>.jsonld`

---

## 🧠 Story Node & Focus Mode Integration

### Story Node linkage (recommended)

This pipeline enables Story Nodes that remain evidence-led even when observations have gaps.

Recommended linking patterns:

- Story Nodes reference `:TimeSeries` nodes for PM₂.₅ and attach:
  - STAC Item references (assets)
  - PROV bundle references (lineage)
  - QA summaries (imputation rates, bias-fit diagnostics)
- Narrative should clearly distinguish:
  - **Observed** PM₂.₅ values
  - **Imputed** (gap-filled) values
  - Any interpretive analytics derived downstream

### Focus Mode constraints (governed)

Focus Mode MAY:

- summarize sections,
- produce timelines and navigation aids,
- extract metadata fields and link them to catalogs.

Focus Mode MUST NOT:

- alter normative requirements,
- invent governance status,
- fabricate provenance or dataset relationships.

---

## 🧪 Validation & CI/CD

### Validation gates (pipeline outputs)

- Schema validation:
  - STAC Items validate against `KFM-STAC v11`
  - PROV bundles validate against `KFM-PROV v11`
- Data checks:
  - Units are µg/m³ only
  - Non-negative constraints
  - Sanity bounds (e.g., ceiling clamp)
  - Missingness accounting (expected vs delivered)
- Governance checks:
  - Sovereignty gate flags enforced
  - Cross-label merges or restricted sources trigger `manual_review` where applicable

### Reliability signals and SLO hooks (recommended)

- Freshness: NRT gap-fill for last 24h available by `T+2h` after latest CAMS valid time
- Completeness: ≥ 98% expected station-hours delivered (excluding planned outages)
- Lineage: 100% outputs have STAC + PROV references

### Known failure modes (and safe degradations)

- CAMS missing cycle:
  - default degrade: “no fill”
  - optional: “raw forecast fill” if policy permits
- Station data drift / units mismatch:
  - quarantine station and emit QA failure artifact
- Bias model instability (too few samples):
  - regional pooling or no-correction fallback (policy-gated)

---

## ⚖ FAIR+CARE & Governance

### Sovereignty / CARE gates

- If a station stream is sovereignty-restricted or has conflicting rights labels:
  - gap-fill may be disabled (`enable_gapfill=false`) for that stream
  - derived outputs MUST carry `kfm:sovereignty_gate` and a rights class
  - policy may require `manual_review=true` for any cross-provider linkage

### Determinism controls (contracted)

Determinism is enforced by pinning:

- `R_metres` / spatial tolerance
- `T_minutes` / temporal tolerance
- bias window length
- bias model method + parameters
- provider inclusion policy + preference order (if applicable)
- algorithm version and code commit SHA (recorded in STAC + PROV)

---

## 🕰️ Version History

- v11.2.6 (2025-12-13): Initial governed pipeline spec for CAMS NRT PM₂.₅ gap-fill with STAC+PROV emission.

---

Back to index · [`docs/data/air-quality/README.md`](../README.md) · Data Architecture · [`docs/architecture/data/README.md`](../../../architecture/data/README.md) · Governance · [`docs/standards/governance/ROOT-GOVERNANCE.md`](../../../standards/governance/ROOT-GOVERNANCE.md) · FAIR+CARE · [`docs/standards/faircare/FAIRCARE-GUIDE.md`](../../../standards/faircare/FAIRCARE-GUIDE.md) · Sovereignty · [`docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md`](../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)
