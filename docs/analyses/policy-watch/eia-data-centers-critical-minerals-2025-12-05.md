---
title: "⚡ KFM v11.2.4 — EIA Data-Center & Critical-Minerals Surveys — Policy Watch Note (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/energy/policy-watch/eia-data-centers-critical-minerals-2025-12-05.md"
version: "v11.2.4"
last_updated: "2025-12-07"

release_stage: "Draft · Tracking"
lifecycle: "Living Document"
review_cycle: "Quarterly · Energy Systems Board · FAIR+CARE Oversight"
content_stability: "beta"
backward_compatibility: "Not Applicable"

status: "Active / Monitoring"
doc_kind: "Policy Watch Note"
header_profile: "standard"
footer_profile: "standard"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-commit-hash-or-null>"
doc_integrity_checksum: "<sha256-of-this-file>"

sbom_ref: "releases/v11.2.4/sbom.spdx.json"
manifest_ref: "releases/v11.2.4/manifest.zip"
telemetry_ref: "releases/v11.2.4/energy-policy-watch-telemetry.json"
telemetry_schema: "schemas/telemetry/energy-policy-watch-v1.json"
governance_ref: "docs/standards/governance/ROOT-GOVERNANCE.md"
license: "MIT"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.4"
ontology_protocol_version: "KFM-OP v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

provenance_chain:
  - "docs/standards/kfm_markdown_protocol_v11.2.4.md@v11.2.4"
  - "docs/standards/energy/README.md@v11.2.4"

doc_uuid: "urn:kfm:doc:analyses:energy:policy-watch:eia-data-centers-critical-minerals-2025-12-05"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"
sensitivity: "General (non-sensitive; auto-mask rules apply)"
classification: "Public / External-Data-Scan"

energy_schema: "<energy-schema-ref-or-null>"
carbon_schema: "<carbon-schema-ref-or-null>"

test_profiles:
  - "markdown-frontmatter-v11"
  - "markdown-structure-v11"
  - "footer-governance-links-v11"

ci_integration: ".github/workflows/docs-lint.yml"

scope:
  domain: "energy"
  applies_to:
    - "etl"
    - "telemetry"
    - "provenance"
    - "governance"
    - "frontier-watch"
    - "story-nodes"
  impacted_modules:
    - "data/raw/external/eia"
    - "data/processed/external/eia"
    - "data/stac/external/eia"
    - "src/pipelines/external/eia"
    - "src/graph/energy"
    - "src/api/energy"
    - "src/web/story-nodes/energy"
---

<div align="center">

# ⚡ **KFM v11.2.4 — EIA Data-Center & Critical-Minerals Surveys — Policy Watch Note**  

`docs/analyses/energy/policy-watch/eia-data-centers-critical-minerals-2025-12-05.md`

---

**Kansas Frontier Matrix (KFM v11)** · **Diamond⁹ Ω / Crown∞Ω Ultimate Certified**  
**Alignment:** STAC 1.x · DCAT 3.0 · PROV-O · GeoSPARQL · FAIR+CARE · ISO 19115 · Energy & Critical-Minerals Telemetry

</div>

---

## 📘 Overview

### Purpose

This note tracks structural changes at the U.S. Energy Information Administration (EIA): retirement of selected legacy reports, introduction of new surveys on **data centers** and **critical minerals**, and planned updates to the **Annual Energy Outlook (AEO)** family.

The goal is to pre-wire KFM so that, once the new surveys stabilize and become machine-readable, they can be ingested, cataloged, graphed, and narrated with **minimal ad-hoc work**.

### Scope

This Policy Watch Note:

- Monitors EIA activities around:
  - Data-center energy consumption and fuel mix.
  - Critical-minerals production, trade, and supply risk.
  - AEO / IEO scenario restructuring.
- Defines **intended KFM hooks**:
  - STAC collections and DCAT datasets.
  - Deterministic ETL and energy telemetry.
  - Neo4j graph entities and Story Nodes.

It does **not** itself implement ETL code or schemas; instead, it guides:

- `data/raw|processed|stac/external/eia`
- `src/pipelines/external/eia`
- `src/graph/energy`
- `src/api/energy`
- `src/web/story-nodes/energy`

### Status

- **Release stage:** Draft · Tracking.
- **Use:** Reference for pipeline and schema design; updated as EIA publishes concrete instruments and first-wave outputs.
- **Governance:** Energy Systems Board with FAIR+CARE oversight.

---

## 🗂️ Directory Layout

The EIA Policy Watch Note touches **docs**, **data**, **pipelines**, **graph**, **API**, and **web Story Nodes**. The expected layout follows the standard emoji + tree pattern:

```text
📁 docs/
└── 📁 analyses/
    └── 📁 energy/
        └── 📁 policy-watch/
            ├── 📄 README.md                                  # Index of energy policy-watch notes
            └── 📄 eia-data-centers-critical-minerals-2025-12-05.md  # This Policy Watch Note

📁 data/
├── 📁 raw/
│   └── 📁 external/
│       └── 📁 eia/
│           ├── 📁 data_centers/                             # Raw EIA data-center survey tables + docs
│           └── 📁 critical_minerals/                        # Raw EIA critical-minerals tables + docs
├── 📁 processed/
│   └── 📁 external/
│       └── 📁 eia/
│           ├── 📁 data_centers/                             # Normalized data-center-energy-v1 tables
│           └── 📁 critical_minerals/                        # Normalized critical-minerals-indicators-v1 tables
└── 📁 stac/
    └── 📁 external/
        └── 📁 eia/
            ├── 🛰️ eia-data-centers-surveys/                 # STAC Collection + Items for data centers
            └── 🛰️ eia-critical-minerals-surveys/            # STAC Collection + Items for critical minerals

📁 src/
├── 📁 pipelines/
│   └── 📁 external/
│       └── 📁 eia/                                          # Deterministic ETL for EIA datasets
├── 📁 graph/
│   └── 📁 energy/                                           # Neo4j schema + logic for energy + minerals series
├── 📁 api/
│   └── 📁 energy/                                           # API endpoints exposing EIA-derived series
└── 📁 web/
    └── 📁 story-nodes/
        └── 📁 energy/                                       # Story Nodes & UI for EIA-linked narratives
```

---

## 🧭 Context

### External changes at EIA (high level)

Recent public statements and reporting around EIA indicate:

1. **Retirement and consolidation of legacy reports**

   - Certain historical products will be discontinued or merged.
   - Rationale: reduce redundancy and free capacity for new statistical domains.

2. **Launch of >10 new survey families**

   With particular relevance to KFM:

   - **Data-center energy surveys**
     - Targeting hyperscale, colocation, and other digital-infrastructure facilities.
     - Intended to measure electricity demand, load shapes, and potentially AI-intensive workloads.

   - **Critical-minerals surveys**
     - Covering minerals such as *vanadium, zirconium, graphite*, and others now flagged as critical.
     - Designed to track production, consumption, trade, and supply risk.

3. **Re-thinking the Annual Energy Outlook (AEO)**

   - Possible separation of **medium-term** vs **long-term** projections.
   - Tighter integration with the International Energy Outlook (IEO), rather than entirely independent workflows.

4. **IT modernization and resilience**

   - A recent **IT glitch** delayed a weekly data release, prompting internal review.
   - EIA is signaling stronger investment in:
     - IT modernization, including potential field presence in Houston.
     - More scalable use of **AI and advanced analytics** to manage survey and modeling workloads.

### Why KFM cares

EIA’s changes reshape the **baseline national data** that underpins many KFM energy, climate, and critical-minerals narratives. Policy, planning, and scenario work in Kansas must increasingly be read against:

- Evolving national-scale data-center loads.
- Shifting perceptions of mineral criticality and supply risk.
- Modified AEO trajectories and scenario architecture.

---

## 🧱 Architecture

### Deterministic ETL pattern for EIA (conceptual)

KFM should treat EIA as an **external authoritative source** and reuse the KFM run-state pattern (`docs/pipelines/patterns/run-state/README.md`) for all EIA integrations.

1. **Source discovery**
   - Poll EIA metadata/documentation endpoints for new releases.
   - Emit a per-release **“survey release manifest”** (YAML/JSON) capturing:
     - Release ID, publication datetime, source URIs.
     - Expected files, formats, sizes, checksums (where provided).

2. **Ingestion (raw layer)**
   - Deterministic download of all referenced artifacts.
   - Validate checksums and sizes; record:
     - `etl_run_id`
     - `source_url`
     - `bytes`
     - `download_checksum`
   - Persist into `data/raw/external/eia/<domain>/...` with immutable naming.

3. **Normalization (work/processed layers)**
   - Map raw tables to KFM canonical schemas:
     - `data-center-energy-v1`
     - `critical-minerals-indicators-v1`
   - Normalize units (e.g., MWh, metric tons, tCO₂e) and encode:
     - Conversion factors.
     - Any imputation or smoothing operations.
   - Store normalized outputs in `data/processed/external/eia/...`.

4. **STAC / DCAT emission**
   - Generate STAC Items and Collections under `data/stac/external/eia/...`.
   - Drive DCAT 3.0 datasets and distributions from STAC via the derivation model.

5. **Graph integration**
   - Upsert Neo4j entities:
     - `:DataCenterEnergySeries`
     - `:CriticalMineralSeries`
   - Connect to:
     - `:Region`, `:State`, `:BalancingAuthority`, `:Mineral`.
     - KFM Story Nodes capturing Kansas-relevant narratives.

Each ETL step should be **idempotent**, WAL-backed, and keyed by **dataset version** nodes in Neo4j for lineage queries.

---

## 📦 Data & Metadata

### Data-center energy demand and Kansas

For KFM, EIA’s data-center surveys are structurally important because:

- Kansas and neighboring states are plausible sites for large **AI and hyperscale data centers** (grid topology, transmission access, land, and incentives).
- KFM’s energy and climate-impact layers will rely on **credible national baselines** for:
  - Data-center load (MWh, MW, load duration curves, seasonal patterns).
  - Fuel mix and associated **CO₂e**, air pollution, and water-use impacts.
  - Regulatory and planning responses at federal, regional, and state levels.

Within KFM, these data should materialize as:

- Time series and aggregates ingested via deterministic ETL.
- STAC Items and DCAT Distributions with clear units and uncertainty.
- Neo4j nodes and relationships that can be intersected with Kansas-regional grid structures.

### Critical minerals, supply chains, and regional stories

Critical-minerals surveys will intersect with existing USGS and DOE work:

- KFM will need crosswalks among:
  - EIA critical-minerals survey outputs.
  - USGS assessments and formal critical-minerals lists.
  - DOE materials and grid-reliability studies.

This supports:

- Understanding **grid and storage dependencies** (e.g., vanadium in flow batteries, graphite in anodes, copper and silver as elevated importance materials).
- Constructing **Kansas-relevant supply-chain narratives**, even where extraction and refining occur elsewhere but infrastructure and demand exist within or near Kansas.

Within KFM, critical-minerals data should be:

- Harmonized around canonical **Mineral** entities.
- Mapped to time- and place-bound indicators suitable for Story Nodes and Focus Mode.

---

## 🌐 STAC, DCAT & PROV Alignment

### STAC collections (conceptual design)

Proposed STAC collections under `data/stac/external/eia/`:

- **`eia-data-centers-surveys`**
  - **Description:** Survey-based observations and aggregates of data-center electricity demand, fuel mix, load shapes, and regional attributes.
  - **Key dimensions:**
    - Time: survey waves, reporting periods, publication dates.
    - Geography: census regions, NERC regions, balancing authorities; later state-level where allowed.
    - Facility attributes: size classes, cooling technologies, load factors, AI-intensive vs general workloads (when available).
  - **Extensions:**
    - `proj` / `geometry` for any spatial aggregates.
    - `table` extension for tabular microdata or public-use samples.
    - `version` to track instrument revisions and respecification.

- **`eia-critical-minerals-surveys`**
  - **Description:** Indicators of production, consumption, trade, and supply risk for critical minerals, aligned with evolving U.S. lists.
  - **Key dimensions:**
    - Minerals: vanadium, zirconium, graphite, copper, silver, etc., each mapped to canonical **Mineral** IDs within KFM.
    - Time: survey wave, year, quarter.
    - Geography: country/region and state-level where applicable.
  - **Extensions:**
    - `table` for survey and indicator tables.
    - `science` for methodology, sampling, weighting, and confidence metadata.

Each collection must be:

- Self-describing with `license`, `provider`, and `sci:doi` / reference documentation when available.
- Linked via PROV-O to the EIA activities and KFM ETL runs that generated KFM-level derivatives.

### DCAT datasets and distributions

Using the STAC→DCAT derivation model (`docs/standards/catalogs/stac-dcat-derivation.md`), KFM should emit DCAT datasets such as:

- `EIA Data-Center Energy Survey — National Aggregates`
- `EIA Data-Center Energy Survey — Regional Aggregates`
- `EIA Critical-Minerals Survey — U.S. Indicators`
- `EIA Critical-Minerals Survey — Global Indicators`

Each DCAT Dataset:

- Includes a **PROV-O provenance chain**:
  - Survey instrument → EIA processing → published dataset → KFM ETL → KFM derivatives.
- Clearly encodes:
  - **License and usage constraints**, even when broadly open.
  - **Temporal coverage** and **spatial coverage** using DCAT and GeoSPARQL patterns.
- Carries **KFM telemetry annotations**:
  - Linking ingestion runs to energy/carbon/cost metrics.

---

## 🧪 Validation & CI/CD

### Energy, carbon, and cost telemetry

Every EIA ETL run must produce **energy, carbon, and cost telemetry**, aligned with `docs/standards/energy/README.md`:

- **Per-step metrics**
  - Bytes downloaded, parsed, and written.
  - CPU/GPU runtime and peak memory.
- **Derived metrics**
  - Energy (kWh) and **CO₂e** (kg) using region-appropriate factors.
  - Estimated **marginal cost** for compute and storage.

Telemetry paths:

- Summaries referenced via:
  - `telemetry_ref: "releases/v11.2.4/energy-policy-watch-telemetry.json"`
  - `telemetry_schema: "schemas/telemetry/energy-policy-watch-v1.json"`
- Beam into:
  - Prometheus / OpenTelemetry spans tagged with `data_source="EIA"` and `domain="energy"` / `domain="critical-minerals"`.

### SLOs, error budgets, and schema drift

- Define SLOs for **freshness**:
  - E.g., `P95(time_to_ingest) < 7 days` from EIA publication to KFM availability.
- Track **error budgets** for:
  - Ingestion failures.
  - Schema drift or breaking changes in EIA formats.
- Wire **schema drift checks** and **metadata lints** into:
  - `.github/workflows/docs-lint.yml`
  - Data pipeline CI to fail fast when clients would break.

---

## ⚖ FAIR+CARE & Governance

### Governance & review checklist

When EIA publishes concrete survey documentation and first-wave data, KFM reviewers should:

1. **License and usage**
   - Confirm data is public or otherwise safe to ingest and redistribute as modeled.
   - Record license and usage notes explicitly in STAC and DCAT.

2. **Survey methodology**
   - Review sampling frames, response rates, weighting, and non-response treatment.
   - Record known biases or coverage gaps:
     - E.g., undercounting small/unregistered data centers.

3. **Linkage to Kansas**
   - Identify spatial units meaningful for Kansas narratives:
     - NERC regions, balancing authorities, state-level aggregates.
   - Mark where disaggregation is not permitted or would be misleading.

4. **Indigenous and Tribal dimensions**
   - If siting, land-use, or transmission-expansion issues intersect Tribal lands:
     - Flag for CARE-aligned review.
     - Consider additional Story Node layers for sovereignty and governance.

5. **Update cadence**
   - Document survey periodicity and expected latency.
   - Align KFM polling schedules and SLOs with EIA release calendars.

This checklist should be mirrored in a small governance record (JSON/YAML) under `docs/standards/governance/` and referenced from this note via `governance_ref`.

### Open questions & TODOs

- [ ] Track publication of actual **survey forms and technical documentation** and summarize key dimensions and units.
- [ ] Decide on **granularity of Neo4j nodes** for data-center series (per region vs per survey wave vs hybrid).
- [ ] Define canonical **Mineral identifiers** and mappings (EIA ↔ USGS ↔ DOE ↔ KFM).
- [ ] Integrate with KFM **energy dashboards** and policy Story Nodes for:
  - Data-center build-out.
  - Grid stress, reliability, and price impacts.
  - Critical-minerals constraints and scenario narratives.

---

## 🧠 Story Node & Focus Mode Integration

### Story Node patterns

This Policy Watch Note should drive creation of Story Nodes such as:

- **“Rising Data-Center Loads in the Central U.S.”**
  - Links:
    - EIA data-center survey series.
    - Kansas/region-specific grid and emissions data.
    - Policy and planning documents (state and regional).

- **“Critical Minerals and Kansas Energy Infrastructure”**
  - Links:
    - Critical-minerals indicators relevant to grid-scale storage and transmission.
    - Infrastructure projects affecting or affected by minerals supply chains.

Each Story Node should be modeled with:

- Clear **temporal extent** (survey periods, scenario years).
- **Spatial extent** (regions, states, balancing authorities).
- Links to:
  - STAC/DCAT entities.
  - Neo4j series nodes (`:DataCenterEnergySeries`, `:CriticalMineralSeries`).
  - Relevant governance documents.

### Focus Mode usage

In Focus Mode, this note should:

- Surface:
  - Latest EIA-linked series intersecting Kansas or its grid neighbors.
  - Policy and planning documents referencing data centers and critical minerals.
- Allow:
  - Time-slicing (by survey wave or AEO vintage).
  - Spatial slicing (by NERC region, state, or balancing authority).
- Support:
  - Side-by-side comparison of **EIA baselines** with:
    - KFM climate and energy scenarios.
    - Local data sources, where available.

---

## 🕰️ Version History

| Version   | Date       | Author       | Notes                                       |
|----------|------------|-------------|---------------------------------------------|
| v11.2.4  | 2025-12-07 | KFM AI Lead | Initial Policy Watch Note scaffolded.       |

---

<div align="center">

**Kansas Frontier Matrix (KFM v11)**  

[🏠 Monorepo Root](/) · [📝 KFM Markdown Protocol v11.2.4](../../../standards/kfm_markdown_protocol_v11.2.4.md) · [⚖️ Root Governance](../../../standards/governance/ROOT-GOVERNANCE.md)

</div>
