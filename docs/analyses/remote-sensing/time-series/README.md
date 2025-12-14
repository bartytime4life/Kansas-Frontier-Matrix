---
title: "📈 Kansas Frontier Matrix — Remote Sensing Time‑Series Analysis (Deterministic · STAC/DCAT/PROV)"
path: "docs/analyses/remote-sensing/time-series/README.md"

version: "v11.2.6"
last_updated: "2025-12-14"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Remote Sensing Board · FAIR+CARE Council"
content_stability: "stable"

status: "Active / Enforced"
doc_kind: "Analysis Module README"
header_profile: "standard"
footer_profile: "standard"
diagram_profiles:
  - "mermaid-flowchart-v1"

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

intent: "remote-sensing-time-series-analysis"
audience:
  - "Remote Sensing Engineering"
  - "Science QA Reviewers"
  - "Data Engineering"
  - "Reliability Engineering"
  - "Story Node Editors"
  - "Governance Reviewers"

classification: "Public"
sensitivity: "General (non-sensitive) unless overridden by dataset labels"
sensitivity_level: "Low"
public_exposure_risk: "Low"
fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"
jurisdiction: "Kansas / United States"
indigenous_rights_flag: true
data_steward: "Remote Sensing Board · FAIR+CARE Council"

governance_ref: "../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

signature_ref: "../../../../releases/v11.2.6/signature.sig"
attestation_ref: "../../../../releases/v11.2.6/slsa-attestation.json"
sbom_ref: "../../../../releases/v11.2.6/sbom.spdx.json"
manifest_ref: "../../../../releases/v11.2.6/manifest.zip"

telemetry_ref: "../../../../releases/v11.2.6/remote-sensing-timeseries-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/remote-sensing-timeseries-v11.json"
energy_schema: "../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../schemas/telemetry/carbon-v2.json"

doc_uuid: "urn:kfm:doc:analyses:remote-sensing:time-series:index:v11.2.6"
semantic_document_id: "kfm-remote-sensing-time-series"
event_source_id: "ledger:docs/analyses/remote-sensing/time-series/README.md"
immutability_status: "version-pinned"

provenance_chain:
  - "docs/analyses/remote-sensing/time-series/README.md@v10.2.2"
  - "KFM Remote Sensing Time-Series Module v10.x"
  - "Remote Sensing ETL + Indexing Baselines"
  - "Focus Mode Timeline Integration Notes"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summary"
  - "timeline-generation"
  - "semantic-highlighting"
  - "diagram-extraction"
  - "metadata-extraction"
  - "a11y-adaptations"
ai_transform_prohibited:
  - "speculative-additions"
  - "unverified-architectural-claims"
  - "narrative-fabrication"
  - "governance-override"
---

<div align="center">

# 📈 **KFM — Remote Sensing Time‑Series Analysis**
`docs/analyses/remote-sensing/time-series/README.md`

**Purpose**  
Define the governed, deterministic approach used in KFM to compute, validate, and publish
**time‑series remote‑sensing products** (composites, trends, breakpoints, anomalies, and forecasts),
with explicit **STAC/DCAT metadata** and **PROV‑O lineage** suitable for Story Nodes and Focus Mode.

<img src="https://img.shields.io/badge/MCP--DL-v6.3-blueviolet" />
<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/STAC%2FDCAT%2FPROV-Aligned-brightgreen" />
<img src="https://img.shields.io/badge/FAIR%2BCARE-Policy--Aware-gold" />
<img src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />

</div>

---

## 📘 Overview

The Time‑Series Analysis module turns repeat satellite observations into governed temporal products:

- **Composites** (annual/monthly) for indices such as NDVI/NDWI/NBR/SAVI.
- **Trends and breakpoints** (e.g., monotonic slope, structural change years).
- **Anomalies** (standardized deviations, event-linked flags).
- **Forecasts** (optional, policy‑gated) with uncertainty summaries.

Key design goals:

- **Determinism:** same inputs + same config → same artifacts + same digests.
- **Traceability:** every published output links back to source inputs, configs, and code via PROV‑O.
- **Catalog interoperability:** every output is discoverable via STAC/DCAT with consistent IDs.
- **Governance safety:** CARE/sovereignty gates are enforced before any publishable report is emitted.

---

## 🗂️ Directory Layout

~~~text
📁 docs/analyses/remote-sensing/time-series/                      — Time-series analysis module docs (this folder)
├── 📄 README.md                                                  — Overview, contracts, publishing posture (this file)
├── 📁 methods/                                                   — Algorithms (compositing, smoothing, trend, forecast)
├── 📁 results/                                                   — References to published outputs (safe summaries only)
├── 📁 reports/                                                   — Validation summaries and run notes (no sensitive leakage)
└── 📄 governance.md                                               — FAIR+CARE posture, redaction rules, reproducibility
~~~

> Directory trees MUST remain “unbroken” (consistent glyphs) and include emojis + descriptions.

---

## 🧭 Context

KFM uses time‑series remote sensing to support:

- long-horizon landscape change narratives,
- seasonality and trend baselines for comparison,
- event interpretation (drought/flood/fire analogs),
- map‑viewer timelines and Focus Mode summaries.

Temporal spans depend on dataset availability and policy, but typical coverage includes the Landsat era
(e.g., **1984–present**) plus higher-cadence sensors for recent years.

Method selection is governed and explicit:
- compositing and smoothing are **required** when inputs are noisy or cloud‑contaminated,
- forecasting is **optional** and must carry uncertainty outputs and provenance,
- any spatial or heritage‑sensitive context is handled through **generalization/redaction** rules.

---

## 📦 Data & Metadata

### Data sources (typical; policy/config may restrict)

| Dataset | Typical temporal range | Role in module | Typical formats |
|---|---:|---|---|
| Landsat 5–9 Surface Reflectance | 1984–present | Long-term baseline indices | COG GeoTIFF |
| MODIS VI products | 2000–present | High-cadence seasonal context | HDF / NetCDF |
| Sentinel‑2 MSI | 2015–present | Higher-res recent validation | COG GeoTIFF |
| NOAA climate normals/anomalies | 1895–present | Context drivers / covariates | CSV / API |
| Kansas Mesonet / station networks | varies | Ground reference and QA | CSV / API |

### Canonical derived products (examples)

- `composites/` — annual or monthly composites per index.
- `trends/` — slope, significance flags, breakpoint year rasters (policy‑safe).
- `anomalies/` — standardized anomaly surfaces and event tags.
- `forecasts/` — optional forecast rasters with uncertainty bands (policy‑gated).

### Metadata requirements (publication)

Every published artifact MUST carry:

- a stable identifier (STAC `id` and DCAT `dct:identifier`),
- time bounds (`datetime` or `start_datetime`/`end_datetime`),
- spatial scope (geometry/bbox where allowed; else `null` or generalized),
- algorithm/config versioning (`kfm:algorithm_version`, `kfm:config_hash`, `commit_sha`),
- governance posture fields (`care_label`, `kfm:sovereignty_gate`, redaction summary where needed),
- checksums/digests for assets.

---

## 🧱 Architecture

### Deterministic pipeline stages (conceptual)

1. **Ingest & normalize**
   - harmonize inputs to governed CRS and grid rules (contract‑defined),
   - normalize reflectance scaling and metadata fields.

2. **Masking & compositing**
   - apply QA masks (cloud/shadow/snow) as defined by contract,
   - produce annual/monthly composites (mean/max/percentile) with stable ordering.

3. **Smoothing & gap handling**
   - apply deterministic smoothers (e.g., Whittaker / Savitzky–Golay) where configured,
   - fill small gaps with policy‑approved interpolation (seeded where stochastic).

4. **Trend / break detection**
   - compute monotonic trend tests (e.g., Mann–Kendall + Sen slope) where appropriate,
   - compute breakpoints (e.g., BFAST/CCDC style outputs) where configured.

5. **Anomaly computation**
   - compute standardized anomalies from a defined baseline window,
   - emit event flags as reason-coded summaries (avoid sensitive leakage).

6. **Forecasting (optional; gated)**
   - run configured models (e.g., ARIMA/Prophet/LSTM) with pinned parameters,
   - output uncertainty summaries (interval bands or variance layers).

7. **Publish**
   - write governed assets,
   - emit STAC Items/Collections + DCAT Dataset/Distributions,
   - emit PROV‑O bundles (and optional OpenLineage).

### Determinism controls (minimum)

- stable input enumeration and sorting before aggregation,
- pinned parameters and thresholds (config snapshot),
- explicit rounding/dtype rules for numeric outputs when needed,
- fixed seeds for any sampling or stochastic model components (recorded in provenance),
- checksum manifests for outputs.

---

## 🗺️ Diagrams

The diagrams below show the high-level dataflow and graph integration. Labels avoid HTML and use quoted node text.

### Time-series pipeline flow

~~~mermaid
flowchart TD
  A["Ingest sensor imagery + metadata"] --> B["Normalize CRS, scale, and QA fields"]
  B --> C["Apply masks + build composites (annual/monthly)"]
  C --> D["Smooth + gap-handle (deterministic)"]
  D --> E["Compute trends + breakpoints"]
  D --> F["Compute anomalies + flags"]
  E --> G["Optional forecasting (policy-gated)"]
  F --> H["Write governed artifacts"]
  G --> H
  H --> I["Emit STAC + DCAT"]
  H --> J["Emit PROV-O lineage"]
~~~

Plain-language intent: convert repeat observations into stable temporal products, then publish catalogs + lineage for every output.

### Knowledge graph and Focus Mode linkage

~~~mermaid
flowchart LR
  TS["Time-series artifact (STAC Item)"] -->|describes| MET["Metrics + summaries"]
  TS -->|wasGeneratedBy| ACT["PROV Activity: time-series run"]
  ACT -->|used| SRC["Source imagery + reference data"]
  TS -->|links_to| KG["Neo4j nodes: Place · Event · Dataset"]
  KG -->|feeds| FM["Focus Mode summaries + Story Nodes"]
~~~

Plain-language intent: keep narrative outputs evidence-led by anchoring summaries to cataloged artifacts and provable lineage.

---

## 🧪 Validation & CI/CD

Validation is required before promotion:

- **Cross-sensor consistency:** overlap checks (e.g., Landsat vs Sentinel‑2) using aggregated metrics.
- **Ground reference checks:** compare anomalies or indices to station networks where available.
- **Temporal sanity:** cadence checks, missing windows, spike/step detection (reason-coded).
- **Catalog validation:** STAC/DCAT schema validation and link integrity checks.
- **Leakage prevention:** no coordinates or restricted identifiers in public reports unless governance permits.

Recommended CI hooks (examples; adapt to repo tooling):

~~~bash
make validate-remote-sensing
make validate-stac
make docs-validate
~~~

---

## 🧠 Story Node & Focus Mode Integration

Time‑series outputs support narrative synthesis when:

- Story Nodes reference **cataloged artifacts** (STAC Item IDs) rather than ad‑hoc files,
- breakpoints and anomalies are expressed as **time‑bounded claims** with provenance,
- spatial reporting respects governance (generalized footprints where required),
- downstream summaries preserve the distinction between:
  - observed products (composites),
  - inferred products (trends/anomalies),
  - modeled products (forecasts).

Focus Mode constraints apply:
- summarization and navigation aids are allowed,
- governance posture must not be changed by transforms,
- provenance and dataset relationships must not be invented.

---

## 🌐 STAC, DCAT & PROV Alignment

### STAC (recommended)

- Collections by product family:
  - `kfm-rs-timeseries-composites`
  - `kfm-rs-timeseries-trends`
  - `kfm-rs-timeseries-anomalies`
  - `kfm-rs-timeseries-forecasts` (optional)
- Items by spatiotemporal unit (tile × time window) or by aggregated region window (policy‑defined).
- Assets:
  - `cog` (primary raster),
  - `qa_summary` (small JSON),
  - `config_snapshot` (immutable JSON),
  - `prov_bundle` (JSON‑LD reference).

### DCAT (recommended)

- `dcat:Dataset` for each product family release (SemVer),
- `dcat:distribution` entries for each artifact class,
- `dct:provenance` includes pointers to PROV bundles and validation rollups.

### PROV‑O (minimum)

- Activities:
  - `ingest`, `composite`, `smooth`, `trend`, `anomaly`, `forecast` (optional), `publish`
- Entities:
  - source imagery slices, reference datasets, configs, derived rasters, reports
- Agents:
  - pipeline runner, CI validator, governance reviewers (where applicable)

---

## ⚖ FAIR+CARE & Governance

- Apply sovereignty and sensitivity labels **before** deriving or publishing outputs.
- When a dataset is restricted:
  - publish only allowed aggregates,
  - generalize spatial footprints (coarse region / coarse H3),
  - avoid “how to locate” instructions and precise coordinate summaries.
- Forecast products (if enabled) must:
  - carry uncertainty summaries,
  - include explicit “modeled output” labeling in metadata and downstream narratives.

---

## 🕰️ Version History

| Version | Date | Summary |
|---:|---|---|
| v11.2.6 | 2025-12-14 | Rebaselined to KFM‑MDP v11.2.6 (approved H2s, directory tree fencing, governance footer); clarified determinism + STAC/DCAT/PROV alignment. |
| v10.2.2 | 2025-11-12 | Legacy module overview for time-series analysis (pre‑v11 heading and footer rules). |

---

<div align="center">

📈 **KFM — Remote Sensing Time‑Series Analysis**  
Research‑Driven · Evidence‑Led · FAIR+CARE Grounded

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/MCP--DL-v6.3-blueviolet" />
<img src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />

[⬅ Docs Index](../../../README.md) ·
[📡 Remote Sensing](../README.md) ·
[🧪 Validation](../validation/README.md) ·
[🏛️ Governance Charter](../../../standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

© 2025 Kansas Frontier Matrix — CC‑BY 4.0  
MCP‑DL v6.3 · KFM‑MDP v11.2.6 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>
