---
title: "🧭 KFM v11.2.3 — Annual NRCS Soils Refresh (SSURGO · gNATSGO · Provenance-Diff Pipeline) (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
description: "Governed pipeline overview for the annual NRCS SSURGO/gNATSGO soils refresh, including deterministic ingest, schema validation, diffing, and STAC publication for the Kansas Frontier Matrix."
path: "docs/data/soils/annual-refresh/README.md"
version: "v11.2.3"
last_updated: "2025-12-03"

release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Annual · Geospatial Systems · FAIR+CARE Oversight"
content_stability: "stable"
status: "Active / Enforced"
backward_compatibility: "v10.x → v11.x soils-refresh-contract compatible"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../../../releases/v11.2.3/manifest.zip"
telemetry_ref: "../../../../releases/v11.2.3/soils-refresh-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/soils-refresh-v1.json"

governance_ref: "../../../../docs/standards/governance/ROOT-GOVERNANCE.md"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.3"

doc_kind: "Pipeline Overview"
intent: "nrcs-soils-annual-refresh"

fair_category: "F1-A1-I1-R1"
care_label: "CARE-Compliant"
sensitivity: "General"
sensitivity_level: "Low"
indigenous_data_flag: false
public_benefit_level: "High"
risk_category: "Low"
redaction_required: false

ontology_alignment:
  schema_org: "DataFeed"
  cidoc: "E29 Design or Procedure"
  prov_o: "prov:Plan"
  owl_time: "TemporalEntity"
  geosparql: "geo:FeatureCollection"

json_schema_ref: "../../../../schemas/json/data-soils-annual-refresh-readme-v1.json"
shape_schema_ref: "../../../../schemas/shacl/data-soils-annual-refresh-readme-v1.shape.ttl"

immutability_status: "version-pinned"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"

ttl_policy: "24 Months"
sunset_policy: "Superseded on next major soils refresh pipeline revision"
---

<div align="center">

# 🧭 Annual NRCS Soils Refresh  
**SSURGO + gNATSGO · October 1 Refresh Window · KFM Provenance-Diff Processing**  
`docs/data/soils/annual-refresh/README.md`

**Purpose:**  
Describe the **governed, deterministic pipeline** KFM v11 uses to ingest the annual NRCS soils refresh (SSURGO & gNATSGO), including validation, diffing, provenance, and STAC publication.

</div>

---

## 📘 1. Overview

NRCS performs an **annual refresh** of its national soil-survey datasets:

- **SSURGO** — detailed soil survey data.  
- **gNATSGO** — gridded national soils (integrating SSURGO, STATSGO, and other sources).

These are typically released on or around **October 1** each year as updated **tabular + spatial bundles**.

The KFM v11 **Annual Soils Refresh pipeline**:

- Ingests the official NRCS bundles.  
- Executes **schema & topology validation**.  
- Computes **geometric and tabular diffs** vs prior year.  
- Emits **versioned STAC Collections & Items** for soils layers.  
- Writes **PROV-O lineage** and soils-refresh telemetry for reproducibility and governance.

---

## 🗂️ 2. Directory Layout (Emoji-Prefix Standard)

~~~text
docs/data/soils/annual-refresh/
│
├── 📄 README.md
│
├── 🗂️ raw/                          # Raw annual SSURGO/gNATSGO bundles (ZIP, GeoPackage, FileGDB)
│   ├── 📦 ssurgo-2025.zip
│   ├── 📦 gnatsgo-2025.zip
│   └── 📦 metadata/                 # Original NRCS metadata, FGDC/ISO docs, etc.
│
├── 🧪 processing/                    # Scripts & logs for diff, schema checks, lineage
│   ├── 📄 diff-report-2025.md        # Human-readable change summary (KFM soils WG)
│   ├── 📄 schema-validation.md       # Validation results across tables + geometry
│   └── 📄 lineage-events.json        # Machine-readable provenance/lineage events
│
├── 🗺️ stac/                          # Versioned STAC Collections + Items
│   ├── 🌐 ssurgo-2025/
│   ├── 🌐 ssurgo-2024/
│   ├── 🌐 gnatsgo-2025/
│   └── 🌐 gnatsgo-2024/
│
├── 📊 deltas/                        # Machine-readable deltas (geometric + tabular)
│   ├── 🧩 geometry-diff-2024-2025.parquet
│   └── 🧩 tabular-diff-2024-2025.parquet
│
└── 📁 provenance/                    # PROV-O lineage, release notes, citation anchors
    ├── 📄 prov-ssurgo-2025.jsonld
    ├── 📄 prov-gnatsgo-2025.jsonld
    └── 📄 citations.md
~~~

**Directory contract:**

- `raw/` holds **verbatim NRCS artifacts** (ZIPs, metadata) with no modification.  
- `processing/` captures **derived logs/reports** that explain how the refresh was processed.  
- `stac/` contains **authoritative KFM STAC catalogs** (SSURGO/gNATSGO by year).  
- `deltas/` provides **parquet-encoded change sets** suitable for analytics or downstream pipelines.  
- `provenance/` anchors all stages with **PROV-O records** and citation details.

---

## 🏛️ 3. NRCS Annual Refresh Overview

### 🔁 Release Cadence

- Occurs **annually** (target: **October 1**).  
- Updates include:
  - **Spatial geometries** (mapunit polygons).  
  - **Mapunit attributes**.  
  - **Component & horizon attributes**.  
  - Derived interpretations and dictionary updates.  
- **gNATSGO** is typically refreshed concurrently with **SSURGO**.

### 🧭 Why KFM Enforces Seasonal Ingestion

Updated soils layers influence:

- **Hydrology** (runoff/infiltration, watershed modeling).  
- **Archaeology** (burial depth modeling, preservation potential, excavation sensitivity).  
- **Land use & planning** (suitability, erosion risk).  
- **Climate-risk simulations** (soil-related hazard & resilience factors).

KFM v11 enforces a **seasonal, deterministic ingest** to:

- Prevent outdated soils from silently contaminating downstream models and AI narratives.  
- Maintain a **year-over-year comparable soils history**.  
- Guarantee that differences between years can be reliably traced and reproduced.

---

## 🔬 4. KFM Provenance-Diff Workflow

### 4.1 Fetch Stage

- Download **official annual bundles** from NRCS (SSURGO and gNATSGO).  
- Verify **signatures + checksums** against NRCS references.  
- Store raw files **verbatim** in `raw/` with:
  - Recorded SHA256 hashes.  
  - Original filenames and metadata.

### 4.2 Schema Validation

- Enforce NRCS **domain dictionaries** and sub-table constraints:
  - Mapunit → Component → Horizon → Lab Data.  
- Run **schema & referential integrity checks**:
  - No orphaned components or horizons.  
  - No broken foreign keys across soils tables.  
- Confirm **spatial topology**:
  - Valid polygons (no self-intersections, slivers).  
  - Expected coverage over Kansas and adjacent areas (if relevant).

### 4.3 Diff Engine

Compute deltas between current year and previous year:

- **Geometry deltas**:
  - New polygons (**additions**).  
  - Retired polygons (**retirements**).  
  - Modified polygons (shape changes).

- **Attribute deltas**:
  - Mapunit-level attribute changes.  
  - Component-level & horizon-level changes.  
  - Derived interpretation changes.

- Classify change types:
  - `added`, `removed`, `modified`, `deprecated`, `unchanged`.

Write results to:

- `deltas/geometry-diff-YYYY-prev.parquet`  
- `deltas/tabular-diff-YYYY-prev.parquet`  

### 4.4 STAC Publication

- Build **versioned STAC Collections** for each year and product:
  - `stac/ssurgo-2025/`, `stac/gnatsgo-2025/`, etc.  
- Connect cross-year relationships:
  - `dct:isVersionOf`, `dct:replaces`, `dct:isReplacedBy` (in STAC/derived DCAT).  
- Link STAC Items to PROV-O:
  - STAC `links` or KFM extensions referencing `prov-*.jsonld` in `provenance/`.

### 4.5 Announce & Downstream Governance

- Register updated soil layers in the **Story Node metadata graph**.  
- Notify governed audiences:
  - Hydrology and watershed modeling custodians.  
  - Archaeology & heritage modeling teams.  
  - Climate & land-use modelers.

- Trigger downstream refresh workflows:
  - Hydrology & flood modeling overlays.  
  - Excavation-sensitivity and heritage risk overlays.  
  - H3-based generalized soils layers for web visualizations.

---

## 📐 5. Expected Change Types Each Year

| Change Type             | Description                                                        |
|-------------------------|--------------------------------------------------------------------|
| **Polygon Additions**   | New survey areas or re-mapped regions, including boundary expansions. |
| **Polygon Retirements** | Areas superseded by new delineations or withdrawn from the dataset. |
| **Attribute Updates**   | Revised interpretations, lab results, component/horizon attributes. |
| **Dictionary Updates**  | Adjustments to soil property definitions and allowable values.      |
| **QA Fixes**            | Geometry repair, duplicate removal, key normalization, minor corrections. |

The diff engine MUST be able to distinguish **true domain changes** from **technical/format-only differences**.

---

## ⚙️ 6. Automation Window & Reliability

### 🚀 Auto-Update Schedule

- **Trigger:** October 1 @ 06:00 UTC (or shortly after NRCS publishes bundles).  
- **Target SLA:** Within **24 hours**, updated soils layers are:
  - Validated.  
  - Diffed.  
  - Published to STAC.  
  - Registered in the KFM catalog & graph.

- **Retry Window:**  
  - Daily retries for **30 days** post-release if upstream issues occur.

### 🔒 Reliability Guarantees

- **Idempotent ingestion**:
  - Write-ahead-logged (WAL) operations.  
  - Yearly refresh runs can be safely re-executed.

- **Reproducible diffs**:
  - Diffs are a pure function of:
    - Year N raw bundles.  
    - Year N-1 STAC & diff outputs.

- **Version-locking**:
  - Each year’s STAC, diff, and provenance outputs are **version-pinned**.  
  - Downstream analyses can always refer to a specific year’s soils representation.

---

## 🧭 7. Provenance Anchors

For each yearly refresh, KFM writes:

- `provenance/prov-ssurgo-YYYY.jsonld`  
- `provenance/prov-gnatsgo-YYYY.jsonld`

Each PROV-O document encodes:

- Fetch activity (source NRCS URLs, timestamps, checksums).  
- Validation activities (schema, topology checks).  
- Diff activities (inputs, outputs, metrics).  
- STAC publication activities (collections & items generated).  

Additionally:

- `provenance/citations.md` contains:
  - NRCS citation blocks (APA/Chicago format).  
  - DOIs where NRCS provides them.  
  - KFM re-publication notes and usage guidance.

---

## 🧪 8. Telemetry

Soils-refresh-specific telemetry is written to:

- `../../../../releases/v11.2.3/soils-refresh-telemetry.json`  

and validated against:

- `../../../../schemas/telemetry/soils-refresh-v1.json`

Tracked metrics include:

- File integrity check counts:
  - Number of bundles, passes/fails.  
- Geometry validation:
  - Count of polygons, invalid vs repaired geometries.  
- Diff magnitude:
  - Percentage of polygons changed.  
  - Number of attributes updated / added / removed.  
- STAC publication:
  - Number of Collections/Items created.  
  - Publication errors and retries.  
- Sustainability:
  - Estimated energy and CO₂ footprint of the refresh run.

---

## 🏁 9. Version History

| Version  | Date       | Notes                                             |
|----------|------------|---------------------------------------------------|
| v11.2.3  | 2025-12-03 | Initial governed release of Soils Refresh README; aligned with KFM-MDP v11.2.3 and soils-refresh telemetry schema. |
| v11.2.2  | 2025-10-01 | Introduced automated diff engine and STAC publication pattern. |
| v11.1.x  | 2024       | Legacy pre-governance ingestion approach (pre-diff, pre-STAC). |

---

## 🪙 10. Governance & Certifications

- **Diamond⁹ Ω / Crown∞Ω Ultimate Certified**  
- FAIR+CARE compliant (**F1-A1-I1-R1**)  
- KFM-MDP v11.2.3  
- MCP-DL v6.3 deterministic documentation contract

---

## 🔗 11. Governance & Standards References

- **Governance:** `docs/standards/governance/ROOT-GOVERNANCE.md`  
- **Ethics:** `docs/standards/ethics/ROOT-ETHICS.md` *(if present in repo)*  
- **Telemetry:** `docs/standards/telemetry/ROOT-TELEMETRY.md`  

These documents define the overarching rules for:

- Dataset-level FAIR+CARE behavior.  
- Soils-refresh provenance and audit requirements.  
- Telemetry collection and sustainability accounting.

---

<div align="center">

**© 2025 Kansas Frontier Matrix — MIT**  
FAIR+CARE Certified · MCP-DL v6.3 · KFM-MDP v11.2.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[⬅ Back to Soils Data Index](../README.md) · [⬅ Back to Data Pipelines Index](../../README.md) · [📜 Governance Charter](../../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>
