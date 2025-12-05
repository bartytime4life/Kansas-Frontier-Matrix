---
title: "⚡ KFM v11.2.4 — Grid-Carbon Intensity Reference Framework (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/standards/energy/grid-carbon-intensity/README.md"
version: "v11.2.4"
last_updated: "2025-12-05"

release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Annual · Energy Systems Board · FAIR+CARE Oversight"
content_stability: "stable"
backward_compatibility: "v10.x → v11.x compliant"
status: "Active / Enforced"

doc_kind: "Standard"
header_profile: "standard"
footer_profile: "standard"

scope:
  domain: "energy/grid-carbon-intensity"
  applies_to:
    - "etl"
    - "ai-workloads"
    - "focus-mode"
    - "frontend"
    - "ci-cd"
    - "telemetry"
    - "provenance"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"
sensitivity: "General (non-sensitive; auto-mask rules apply)"
classification: "Public"
indigenous_rights_flag: true

commit_sha: "<latest-commit-sha>"
previous_version_hash: "<prev-doc-sha256>"
doc_integrity_checksum: "<this-doc-sha256>"

sbom_ref: "../../../../releases/v11.2.4/sbom.spdx.json"
manifest_ref: "../../../../releases/v11.2.4/manifest.zip"
telemetry_ref: "../../../../releases/v11.2.4/grid-carbon-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/energy-grid-intensity-v1.json"
governance_ref: "../../governance/ROOT-GOVERNANCE.md"

doc_uuid: "urn:kfm:doc:standards:energy:grid-carbon-intensity:v11.2.4"
semantic_document_id: "kfm-doc-grid-carbon-intensity-v11.2.4"
event_source_id: "ledger:kfm:doc:standards:energy:grid-carbon-intensity:v11.2.4"

license: "CC-BY-4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.4"
---

<div align="center">

# ⚡ Grid-Carbon Intensity Reference Framework  
*KFM v11.2.4 — Standardization for Regional Electricity CO₂e Factors*  

**Diamond⁹ Ω / Crown∞Ω Ultimate Certified**  
**Deterministic · FAIR+CARE · Provenance-Locked**

`docs/standards/energy/grid-carbon-intensity/README.md`

**Purpose:**  
Define how KFM computes, validates, and applies **region-specific and time-specific carbon-intensity factors (CI/kWh)** for all energy-consuming processes across pipelines, AI workloads, CI/CD, and frontends — ensuring deterministic carbon accounting, alignment with EPA eGRID and related datasets, and a governance-compliant audit chain.

</div>

---

## 📘 Overview

This standard defines the **canonical method** for representing and applying **grid carbon intensity** across KFM:

- Provides a **unified CI model** for every KFM compute environment (ETL, AI inference, Focus Mode, frontend rendering, CI/CD).  
- Aligns KFM carbon accounting with **nationally standardized datasets** (e.g., EPA eGRID) and related regional sources.  
- Enforces **deterministic energy and CO₂e calculations** via region + time attribution and versioned datasets.  
- Integrates CI factors into **telemetry, provenance, and governance** so energy use and emissions can be audited over time.  

This standard is **enforced** for all KFM components that compute or report energy usage or CO₂e estimates.

### Scope

Applies to:

- All Airflow / LangGraph / similar ETL jobs.  
- All model-inference and Focus Mode computational workloads.  
- All interactive browser compute that KFM chooses to estimate (e.g., terrain rasterization, Cesium timelines).  
- All internal benchmarking, profiling, and optimization experiments.  
- All CI/CD workflows that consume compute resources and emit telemetry.  

Excluded (covered by separate or future standards):

- Non-electrical energy sources.  
- Third-party consumption estimates without deterministic provenance and versioned datasets.

---

## 🗂️ Directory Layout

```text
📂 docs/standards/energy/
└── 📂 grid-carbon-intensity/
    ├── 📄 README.md                   # ⚡ Grid-Carbon Intensity Reference Framework (this file)
    ├── 📂 mappings/
    │   ├── 📄 cloud-region-map.yaml   # Cloud-region → KFM region taxonomy mappings
    │   └── 📄 egrid-subregions.yaml   # eGRID subregion metadata & keys
    └── 📂 examples/
        ├── 📄 telemetry-sample.json   # Sample telemetry envelope with CI fields
        └── 📄 prov-sample.jsonld      # Sample PROV representation for CI computation
```

Associated datasets and sources live under `data/`:

- `data/processed/energy/egrid/` — processed and normalized eGRID releases.  
- `data/sources/energy/balancing-authorities/` — source manifests and metadata for BA-region series.

---

## 🧭 Context

KFM treats **energy and carbon accounting** as first-class telemetry and provenance data:

- Every significant compute activity can be associated with:
  - An **energy_kwh** estimate.  
  - A **carbon intensity** value (g CO₂e / kWh).  
  - A **region** and **time** context (eGRID subregion, BA, cloud region + timestamp).  

This framework:

- Ensures CI values are **traceable** to versioned datasets (eGRID releases, BA series, cloud-mix feeds).  
- Provides a **deterministic algorithm** for computing CI and CO₂e across heterogeneous environments.  
- Supports **scenario and optimization modeling** (e.g., moving workloads to lower-carbon regions) while preserving an official accounting baseline.

It interacts with:

- **Telemetry schemas** (`energy-grid-intensity-v1.json`).  
- **System and pipeline docs** that reference energy/CO₂e.  
- **Governance & sustainability reporting**, both internal and public-facing.

---

## 🧱 Architecture

### 1. Canonical concepts

#### 1.1 Carbon intensity (CI)

The mass of CO₂e emitted per kWh of delivered electricity.

KFM encodes this in telemetry and metadata as:

```yaml
carbon_intensity_g_co2e_per_kwh: <number>
```

CI may refer to:

- **Generation CI**: emissions at the generation stage.  
- **Delivered CI**: generation CI adjusted for transmission and distribution (T&D) losses.  

This standard focuses on **delivered CI**, as defined below.

#### 1.2 Region attribution

Every KFM compute activity that emits energy telemetry must map to a **single region key**, chosen from:

1. **EPA eGRID subregions**.  
2. **Balancing Authorities (BA)**.  
3. **Cloud regions** (e.g., `us-central1`, `us-east-1`) mapped deterministically to 1 or 2 via `cloud-region-map.yaml`.  
4. **Custom locality overlays** (for Kansas field deployments and offline environments), defined as overlays that ultimately resolve to an eGRID or BA region.

Pipelines must not invent ad-hoc regions; they must select from the **KFM region taxonomy** maintained in the `mappings/` directory.

#### 1.3 Time sensitivity

Carbon intensity **varies over time**. KFM supports:

- `static_factor`  
  - eGRID annual mean for a given region and year (default for accounting).  
- `quasi_hourly_factor`  
  - Cloud-provider hourly or similar grid-mix feeds, where available and trusted.  
- `marginal_factor`  
  - Used only for **optimization and scenario modeling**, not official accounting.  

When reporting official CO₂e totals, KFM must use a **clearly documented factor type**, typically `static_factor` unless a governance decision approves time-varying or marginal factors for specific use cases.

### 2. Deterministic selection algorithm

All pipelines and workloads that compute CI **must** implement the following conceptual algorithm:

1. **Identify compute region**  
   - From environment metadata (cloud region, datacenter tag, locality config).  

2. **Resolve to KFM region taxonomy**  
   - Use `mappings/cloud-region-map.yaml` and/or `mappings/egrid-subregions.yaml`.  

3. **Load matched CI dataset**  
   - Select the correct eGRID or BA dataset version from `data/processed/energy/egrid/` or related stores.  

4. **Select CI value type**  
   - `static_factor`, `quasi_hourly_factor`, or `marginal_factor` per configuration and governance rules.  

5. **Adjust for T&D losses** (see Data & Metadata).  

6. **Emit telemetry + provenance**  
   - Include required fields (see Mandatory Output Fields).  
   - Link to dataset version and provenance documents.

Implementation details (language, libraries, schema loaders) are left to pipeline modules, but they must respect this sequence and be **config- and version-driven**.

---

## 📦 Data & Metadata

### 1. Primary and secondary data sources

#### 1.1 Primary

- **EPA eGRID** (latest full release)  
  - Regional CI values (kg CO₂e / MWh or similar units).  
  - Transmission/distribution loss rates per region.  
  - Non-baseload / marginal multipliers where available.

#### 1.2 Secondary (optional)

- Cloud providers’ grid-mix intensity feeds (by region and hour).  
- State-level energy profiles (e.g., Kansas-specific reports).  
- Balancing-authority historical time series.

All such datasets must be:

- Registered in `data/sources/energy/...` with DCAT-like metadata.  
- Processed into `data/processed/energy/...` with STAC/PROV references as appropriate.

### 2. Mandatory output fields

Every **telemetry envelope** that reports energy/CO₂e must include:

```yaml
energy_kwh: <float>
carbon_intensity_source: "egrid-<year>"            # or a documented alternative source key
carbon_intensity_g_co2e_per_kwh: <float>
co2e_g_total: <float>
region_key: "<kfm-region>"                        # e.g., "egrid:SPNO" or "ba:SPS"
dataset_version: "<dataset-version>"              # e.g., "egrid-2022.1"
provenance_ref: "<prov-json-ld>"                  # URI/URN for PROV bundle
```

Rules:

- `carbon_intensity_source` and `dataset_version` must map deterministically to a **versioned dataset** in `data/processed/energy/`.  
- `co2e_g_total` must equal `energy_kwh * carbon_intensity_g_co2e_per_kwh` within a small numerical tolerance.  
- `provenance_ref` must resolve to a PROV bundle describing how the CI value was derived.

### 3. Loss adjustment

Delivered CI must include **transmission and distribution (T&D) loss**:

```text
ci_delivered = ci_generation / (1 - loss_rate)
```

Where:

- `ci_generation` is the generation-stage CI (g CO₂e / kWh).  
- `loss_rate` is the fraction (0–1) of energy lost in T&D for that region (from eGRID or a documented source).  

`carbon_intensity_g_co2e_per_kwh` must refer to **delivered CI**, not raw generation CI, unless explicitly labeled otherwise in the dataset and telemetry.

---

## 🌐 STAC, DCAT & PROV Alignment

KFM’s grid-carbon data and usage must be compatible with STAC, DCAT, and PROV:

### 1. DCAT alignment

- eGRID and related CI datasets are modeled as `dcat:Dataset` records with:
  - `dct:title`, `dct:description`, `dct:license`, `dct:issued`, `dct:modified`.  
  - `dct:spatial` and `dct:temporal` coverage metadata.  
- Region mapping files (`cloud-region-map.yaml`, `egrid-subregions.yaml`) may be represented as distributions of these datasets or as supporting datasets in their own right.

### 2. STAC alignment

- CI datasets may be represented as **STAC Collections**:
  - `id` corresponding to dataset/version (`egrid-2022`, etc.).  
  - `assets` containing processed tables and derived products.  
- Time-series CI data (e.g., hourly feeds) can be modeled as STAC Items with:
  - `properties.datetime` = time of measurement.  
  - Region metadata in `properties["kfm:region_key"]`.

### 3. PROV-O alignment

- CI computation for a pipeline run is modeled as a `prov:Activity`:
  - `prov:used` → CI dataset/entity (eGRID record, BA series).  
  - `prov:generated` → telemetry entity with energy and CO₂e fields.  
  - `prov:wasAssociatedWith` → pipeline or service.

The `provenance_ref` in telemetry should point to such a PROV bundle, allowing auditors to trace:

- Which dataset version was used.  
- Which region mapping was applied.  
- Any scenario/optimization modeling (e.g., marginal factors) separate from official accounting.

---

## 🧪 Validation & CI/CD

This standard must be enforced via automated checks:

### 1. Schema validation

- Telemetry documents must be validated against `energy-grid-intensity-v1.json`.  
- CI datasets must pass schema checks for:
  - Region keys.  
  - CI units and types (static, quasi-hourly, marginal).  
  - Loss-rate fields.

### 2. Consistency checks

- For sampled telemetry:
  - Recompute `co2e_g_total` from `energy_kwh * carbon_intensity_g_co2e_per_kwh`.  
  - Verify `region_key` exists in current mappings.  
  - Confirm `dataset_version` and `carbon_intensity_source` correspond to real datasets.

### 3. Pipeline tests

- ETL and AI pipeline tests must:
  - Exercise the region-resolution and CI selection process.  
  - Verify deterministic behavior across reruns given the same configuration.  
  - Check that telemetry envelopes include required fields and valid values.

### 4. Release & governance checks

- Annual **eGRID updates** require:
  - Dataset ingestion and processing.  
  - Mapping updates (cloud-region and eGRID subregions).  
  - Regression tests against previous year’s CI values (change windows, sanity bounds).  
- All changes must be accompanied by:
  - Updated SBOMs and manifests.  
  - SLSA attestations for pipelines that compute or report energy/CO₂e.

---

## ⚖ FAIR+CARE & Governance

This framework supports FAIR+CARE and sustainability commitments:

- **FAIR**
  - *Findable*: CI datasets and mappings are cataloged under `data/sources/` and `data/processed/`, and discoverable via catalogs.  
  - *Accessible*: Telemetry schemas and documentation are publicly documented (subject to internal policy).  
  - *Interoperable*: Uses standard units and aligns with DCAT, STAC, and PROV conventions.  
  - *Reusable*: Versioned datasets and provenance allow future re-analysis and comparisons.

- **CARE & responsibility**
  - *Collective Benefit*: Transparent carbon accounting informs system design, governance, and potential mitigation strategies (e.g., shifting workloads).  
  - *Authority to Control*: Governance bodies (Energy Systems Board, FAIR+CARE Oversight) approve what counts as official CI, and how it is reported.  
  - *Responsibility*: Pipelines and teams must ensure CI reporting is accurate, versioned, and not used in misleading ways.  
  - *Ethics*: Avoids “greenwashing” by clearly separating scenario/marginal modeling from official accounting values.

Governance expectations:

- Annual review of:
  - eGRID updates and region mappings.  
  - Telemetry use in public reports and dashboards.  
- Quarterly or periodic audits:
  - Spot-check energy/CO₂e telemetry against configuration and datasets.  
- All changes to this standard require:
  - Energy Systems Board review.  
  - FAIR+CARE Oversight sign-off.  

---

## 🕰️ Version History

| Version | Date       | Status            | Summary                                      |
|--------:|------------|-------------------|----------------------------------------------|
| v11.2.4 | 2025-12-05 | Active / Enforced | Initial full KFM-MDP-aligned release.        |

Future revisions must:

- Document any updates to dataset sources (eGRID year, BA sources, cloud feeds).  
- Describe changes to required fields, algorithms, or region mappings.  
- Keep telemetry schema references and governance links in sync with KFM-wide standards.

---

<div align="center">

⚡ **KFM v11.2.4 — Grid-Carbon Intensity Reference Framework**  
Deterministic Pipelines · FAIR+CARE-Aligned Energy Accounting · Provenance-Locked Metrics  

[📘 Docs Root](../../../..) · [📂 Standards Index](../../README.md) · [⚖ Governance](../../governance/ROOT-GOVERNANCE.md)

</div>