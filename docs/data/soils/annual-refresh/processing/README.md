---
title: "🧪 KFM v11.2.3 — Annual NRCS Soils Processing & Diff Engine (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
description: "Processing, validation, and diffing layer for the annual NRCS SSURGO/gNATSGO soils refresh pipeline in the Kansas Frontier Matrix."
path: "docs/data/soils/annual-refresh/processing/README.md"
version: "v11.2.3"
last_updated: "2025-12-03"

release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Annual · Geospatial Systems · FAIR+CARE Oversight"
content_stability: "stable"
status: "Active / Enforced"
backward_compatibility: "v10.x → v11.x soils-processing-contract compatible"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.2.3/manifest.zip"
telemetry_ref: "../../../../../releases/v11.2.3/soils-refresh-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/soils-refresh-v1.json"

governance_ref: "../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.3"

doc_kind: "Processing Overview"
intent: "nrcs-soils-annual-refresh-processing"

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

json_schema_ref: "../../../../../schemas/json/data-soils-annual-refresh-processing-readme-v1.json"
shape_schema_ref: "../../../../../schemas/shacl/data-soils-annual-refresh-processing-readme-v1.shape.ttl"

immutability_status: "version-pinned"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"

ttl_policy: "24 Months"
sunset_policy: "Superseded on next major soils processing pipeline revision"
---

<div align="center">

# 🧪 Annual NRCS Soils Processing & Diff Engine  
**Schema Validation · Geometry Checks · Tabular & Geometry Deltas · Lineage Events**  
`docs/data/soils/annual-refresh/processing/README.md`

**Purpose:**  
Describe the **processing layer** for the KFM **Annual NRCS Soils Refresh** pipeline:  
schema & topology validation, diff computation, and lineage logging that sit between **raw NRCS bundles** and **published STAC/provenance artifacts**.

</div>

---

## 📘 1. Scope

This directory captures **all processing artifacts** that:

- Operate on raw NRCS bundles (`../raw/`).  
- Produce **human-readable reports** and **machine-readable logs** about:
  - Schema validation results.  
  - Geometry/topology checks.  
  - Year-over-year soils deltas.  
  - Lineage events used by PROV-O and downstream systems.

Nothing in this directory is **upstream raw data** or **final catalog output**; it is the **intermediate processing documentation** layer.

---

## 🗂️ 2. Directory Layout (Processing Layer)

~~~text
docs/data/soils/annual-refresh/processing/
│
├── 📄 README.md                       # This file — processing/diff engine overview
│
├── 📄 diff-report-2025.md             # Human-readable change report for 2025 vs 2024
├── 📄 schema-validation.md            # Schema & topology validation summary (all years)
└── 📄 lineage-events.json             # Machine-readable lineage / event log (PROV-friendly)
~~~

**Directory contract:**

- `diff-report-YYYY.md` (per year) documents **what changed** between years in human terms.  
- `schema-validation.md` aggregates schema & topology checks, either:
  - As a single rolling document with year-tagged sections; or  
  - As an index referencing year-specific validation files if the pipeline grows.  
- `lineage-events.json` is the **canonical machine-readable log** of processing activities, consumed by provenance builders and telemetry.

---

## 🧪 3. Schema & Topology Validation

### 3.1 Objectives

Validation ensures:

- KFM can trust NRCS bundles before diffing and publication.  
- Cross-table relationships (mapunit, component, horizon, lab data) are intact.  
- Geometry is topologically clean enough for downstream modeling and visualization.

### 3.2 Typical Checks (Documented in `schema-validation.md`)

For each annual refresh:

- **Tabular schema checks**:
  - Presence of required tables (e.g., `mapunit`, `component`, `chorizon`, `muaggatt`).  
  - Column existence and type checks.  
  - Foreign key integrity:
    - `mapunit.mukey` → `component.mukey`  
    - `component.cokey` → `chorizon.cokey`  
    - Optional lab tables.

- **Dictionary & domain checks**:
  - Validity of coded value domains (e.g., soil texture codes).  
  - Detection of deprecated or unknown codes.

- **Geometry/topology checks**:
  - Polygon validity (no self-intersections).  
  - No unexpected multipart anomalies (where not allowed).  
  - Topology summary (number of polygons, boundaries, slivers).

Results are:

- Summarized in `schema-validation.md` (with year-tagged sections).  
- Emitted as machine-readable events in `lineage-events.json`.

---

## 🔍 4. Diff Engine & Change Classification

The **diff engine** compares current-year SSURGO/gNATSGO to prior-year KFM baseline.

### 4.1 Inputs

- **Current year**:
  - Raw bundles (from `../raw/`).  
  - Derived intermediate tables (in pipeline-specific storage, not this directory).  

- **Previous year**:
  - Last year’s STAC soils representation and/or curated tables.  
  - Prior-year deltas (for sanity checks).

### 4.2 Outputs (Documented Here & in `../deltas/`)

- **Human-readable**:
  - `diff-report-YYYY.md`:
    - Summaries of polygon additions/retirements.  
    - Attribute change stats (per table/category).  
    - Notable dictionary changes.  
    - QA notes (sliver cleanups, bug fixes).

- **Machine-readable** (stored in `../deltas/`):
  - `geometry-diff-YYYY-prev.parquet`  
  - `tabular-diff-YYYY-prev.parquet`

### 4.3 Change Types (Aligned with Parent README)

Typical class labels in diff outputs:

- `added` — new polygons or records not present in prior year.  
- `removed` — polygons or records present last year but not now.  
- `modified` — features where geometry or attributes changed.  
- `deprecated` — features marked as superseded by NRCS guidance.  
- `unchanged` — unchanged features (often omitted from diff outputs for efficiency).

`diff-report-YYYY.md` MUST clearly define:

- The **counts and percentages** per change type.  
- Any major thematic patterns (e.g., large re-mapping of a specific basin).

---

## 🧬 5. Lineage Events (`lineage-events.json`)

`lineage-events.json` is a **machine-readable event log** that:

- Mirrors the processing steps described in this README.  
- Is designed to be directly ingested by:
  - PROV-O builders (to generate `provenance/prov-*.jsonld`).  
  - Telemetry pipelines (for soils-refresh metrics).

### 5.1 Event Content (Conceptual)

Each event entry typically includes:

- `event_id` — unique identifier.  
- `event_type` — e.g., `fetch`, `schema_validation`, `geometry_diff`, `tabular_diff`, `stac_publish`.  
- `year` — soils refresh year (e.g., `2025`).  
- `inputs` — references to raw files, tables, or prior-year artifacts.  
- `outputs` — references to diff files, STAC paths, or derived tables.  
- `status` — `success`, `warning`, `error`.  
- `timestamp_start`, `timestamp_end`.  
- `metrics` — counts and numeric summary stats (e.g., polygons changed, records updated).

### 5.2 Relationship to PROV-O

Downstream PROV-O documents (`../provenance/prov-*.jsonld`) use `lineage-events.json` to:

- Construct `prov:Activity` nodes for each stage.  
- Attach `prov:used` and `prov:generated` edges.  
- Provide fine-grained audit trails for the soils-refresh pipeline.

---

## 📊 6. Telemetry Integration

Processing-stage telemetry (for validation + diff) feeds into:

- `../../../../../releases/v11.2.3/soils-refresh-telemetry.json`  
- Validated against `../../../../../schemas/telemetry/soils-refresh-v1.json`

Key metrics at this stage:

- Number of tables/columns validated.  
- Number of geometry issues found/fixed.  
- Diff sizes:
  - Percent of polygons changed.  
  - Count of attribute modifications.  
- Processing time & resource utilization:
  - To support sustainability and cost tracking.

---

## 🛡️ 7. Governance & FAIR+CARE Considerations

While NRCS soils data is generally open:

- Soil interpretations can indirectly influence sensitive decisions (e.g., excavation suitability, hazard zoning).  
- KFM’s processing stage must ensure:
  - **Accuracy and integrity** of soils inputs and diffs.  
  - Clear linkage to NRCS licensing and usage guidance (via upstream metadata).  
  - That any downstream **aggregated or derived risk layers** handled by FAIR+CARE remain clearly distinguished from raw soils.

Governance impacts (e.g., changed NRCS usage terms, large-scale reclassification) MUST be:

- Highlighted in `diff-report-YYYY.md`.  
- Reflected in `../provenance/citations.md` and any STAC/DCAT licensing fields.

---

## 🕰️ 8. Version History (Processing Overview)

| Version  | Date       | Author                                   | Summary                                                                 |
|----------|------------|------------------------------------------|-------------------------------------------------------------------------|
| v11.2.3  | 2025-12-03 | Geospatial Systems WG · FAIR+CARE Council | Initial processing README; documented schema validation, diff engine, and lineage event conventions for the soils-refresh pipeline. |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — MIT**  
FAIR+CARE Certified · MCP-DL v6.3 · KFM-MDP v11.2.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[⬅ Back to Annual Soils Refresh](../README.md) · [⬅ Back to Soils Data Index](../README.md) · [📜 Governance Charter](../../../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>

