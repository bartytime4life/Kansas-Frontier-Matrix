---
title: "📊 KFM v11.2.3 — Annual NRCS Soils Deltas (Geometry · Tabular) (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
description: "Machine-readable geometric and tabular diff outputs for the annual NRCS SSURGO/gNATSGO soils refresh pipeline in the Kansas Frontier Matrix."
path: "docs/data/soils/annual-refresh/deltas/README.md"
version: "v11.2.3"
last_updated: "2025-12-03"

release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Annual · Geospatial Systems · FAIR+CARE Oversight"
content_stability: "stable"
status: "Active · Enforced"
backward_compatibility: "v10.x → v11.x soils-deltas-contract compatible"

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

doc_kind: "Diff Data Index"
intent: "nrcs-soils-annual-refresh-deltas"

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
  cidoc: "E73 Information Object"
  prov_o: "prov:Entity"
  owl_time: "TemporalEntity"
  geosparql: "geo:FeatureCollection"

json_schema_ref: "../../../../schemas/json/data-soils-annual-refresh-deltas-readme-v1.json"
shape_schema_ref: "../../../../schemas/shacl/data-soils-annual-refresh-deltas-readme-v1.shape.ttl"

immutability_status: "version-pinned"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"

ttl_policy: "Permanent"
sunset_policy: "Never (per-year diff outputs are immutable audit artifacts)"
---

<div align="center">

# 📊 Annual NRCS Soils Deltas — Geometry & Tabular  
`docs/data/soils/annual-refresh/deltas/README.md`

**Purpose:**  
Define the **structure, semantics, and governance** of **machine-readable soils deltas** (geometry + tabular) produced by the KFM **Annual NRCS Soils Refresh** pipeline, enabling:

- Year-over-year soils comparison  
- Downstream modeling & analytics (hydrology, archaeology, land use, climate)  
- Reproducible, PROV-O-aligned change tracking

</div>

---

## 📘 1. Scope

This directory contains **diff artifacts** that describe how NRCS soils datasets changed between years:

- **Geometry deltas** — polygon-level changes in SSURGO coverage.  
- **Tabular deltas** — mapunit/component/horizon/interpretation changes.  

These files are:

- Purely **derived** from validated NRCS upstream data and prior-year KFM baselines.  
- Used by:
  - `processing/diff-report-YYYY.md` for human-readable summaries.  
  - Downstream pipelines (hydrology, archaeology, risk models, Story Nodes).  
  - PROV-O lineage and telemetry.

No raw NRCS data or STAC catalogs live here; this is the **delta layer only**.

---

## 🗂️ 2. Directory Layout (Deltas)

~~~text
docs/data/soils/annual-refresh/deltas/
│
├── 📄 README.md                            # This file — soils deltas overview & contracts
│
├── 🧩 geometry-diff-2024-2025.parquet      # Geometry-level diff: SSURGO polygons 2024 → 2025
└── 🧩 tabular-diff-2024-2025.parquet       # Tabular diff: mapunit/component/horizon/interpretations
~~~

**Directory contract:**

- Filenames MUST make the **year pairing** explicit: `YYYY-prev` → `YYYY`.  
- Additional year pairs (e.g., `geometry-diff-2025-2026.parquet`) MUST follow the same naming pattern.  
- Deltas are **append-only** across years:
  - New year → new diff files.  
  - Existing diff files MUST NOT be mutated.

If diff schema or encoding changes in a future major revision, new files MUST use new names or version suffixes and be documented here.

---

## 🧮 3. Geometry Deltas (`geometry-diff-YYYY-prev.parquet`)

### 3.1 Purpose

Capture **polygon-level geometry changes** between:

- Prior-year SSURGO baseline (e.g., 2024).  
- Current-year SSURGO ingest (e.g., 2025).

Used for:

- Spatial change analyses (AOI-level, basin-level).  
- Downstream model updates (e.g., watershed recalibration).  
- Visualizations in Story Nodes / Focus Mode.

### 3.2 Conceptual Schema (Illustrative)

Exact schema is governed by dedicated JSON/Parquet schema docs; an illustrative shape:

| Column              | Type      | Description                                                  |
|---------------------|-----------|--------------------------------------------------------------|
| `year_prev`         | int       | Previous year (e.g., `2024`)                                |
| `year_curr`         | int       | Current year (e.g., `2025`)                                 |
| `mukey_prev`        | string    | Mapunit key in previous year (if applicable)                |
| `mukey_curr`        | string    | Mapunit key in current year (if applicable)                 |
| `change_type`       | string    | `added`, `removed`, `modified_geometry`, `unchanged`, `deprecated` |
| `area_prev_m2`      | double    | Polygon area in previous year (m²)                          |
| `area_curr_m2`      | double    | Polygon area in current year (m²)                           |
| `geometry_prev_wkb` | binary    | Prior-year geometry (WKB, optional or in a companion file)  |
| `geometry_curr_wkb` | binary    | Current-year geometry (WKB, optional or in a companion file)|
| `region_key`        | string    | Optional grouping key (e.g., county, HUC, planning region)  |

**Notes:**

- Geometry may be represented:
  - Directly in WKB columns.  
  - Or via references to external geometry stores (depending on size constraints).  
- `change_type` classification MUST be consistent with `processing/diff-report-YYYY.md`.

---

## 📊 4. Tabular Deltas (`tabular-diff-YYYY-prev.parquet`)

### 4.1 Purpose

Capture **attribute-level changes** in:

- Mapunit-level tables (e.g., `muaggatt`).  
- Component-level tables.  
- Horizon-level tables (`chorizon`).  
- Derived interpretation tables.

Used for:

- Detecting shifts in soil interpretations, lab data, or structural changes.  
- Driving updates to derived risk layers and interpretive Story Nodes.  
- Fine-grain QA and analytics.

### 4.2 Conceptual Schema (Illustrative)

Common pattern: **per-record, per-field** change representation, e.g.:

| Column           | Type      | Description                                                  |
|------------------|-----------|--------------------------------------------------------------|
| `year_prev`      | int       | Previous year (e.g., `2024`)                                |
| `year_curr`      | int       | Current year (e.g., `2025`)                                 |
| `table_name`     | string    | Table name (`mapunit`, `component`, `chorizon`, etc.)       |
| `record_key`     | string    | Primary key (e.g., `mukey`, `cokey`)                        |
| `field_name`     | string    | Column that changed                                         |
| `value_prev`     | string    | Previous-year value (stringified)                           |
| `value_curr`     | string    | Current-year value (stringified)                            |
| `change_type`    | string    | `added`, `removed`, `modified`, `unchanged`, `deprecated`   |
| `region_key`     | string    | Optional grouping key (e.g., region/HUC/county)             |

**Notes:**

- Casting to string for `value_prev`/`value_curr` simplifies diff representation; domain-aware consumers can re-interpret types.  
- Additional normalized tables or views can be created downstream for performance.

---

## 🔗 5. Relationship to Processing, STAC & Provenance

Deltas tie together multiple layers of the annual refresh:

- **Processing layer** (`../processing/`):
  - `diff-report-YYYY.md` (human-readable) summarizes these Parquet diffs.  
  - `schema-validation.md` ensures diffs are only computed from validated data.  

- **STAC layer** (`../stac/`):
  - STAC Collections/Items for SSURGO/gNATSGO may:
    - Link to diff artifacts.  
    - Reference diff statistics in metadata.

- **Provenance layer** (`../provenance/`):
  - PROV-O documents **describe activities** that produce these diffs:
    - Inputs: prior-year STAC/curated tables + current-year raw/curated data.  
    - Outputs: geometry/tabular diff Parquets.

Consumers MUST treat these deltas as:

- **Derived entities** (`prov:Entity`) in the soils provenance graph.  
- **Read-only audit artifacts** for change analysis.

---

## 🧪 6. Telemetry & CI Expectations

### 6.1 Telemetry

Diff-generation steps emit metrics to:

- `../../../../releases/v11.2.3/soils-refresh-telemetry.json`  
- Under the `deltas` or equivalent section in the `soils-refresh-v1.json` schema.

Tracked metrics include:

- Counts of diff records (geometry + tabular).  
- Distribution of change types (`added`, `removed`, `modified`, etc.).  
- Processing time and resource usage.  
- Potential anomalies (e.g., unexpectedly high rates of change in specific regions).

### 6.2 CI Checks

CI pipelines should:

- Validate **schema compatibility** of Parquet deltas:
  - Using schemas or contracts defined external to this README.  
- Confirm files exist for the expected year-pair once processing completes.  
- Validate that:
  - Year pair fields in the data (`year_prev`, `year_curr`) match filenames.  
  - No “future” years or inconsistent labelings are present.

Failures MUST:

- Block marking the soils refresh as **complete**.  
- Trigger investigation by the Geospatial Systems WG.

---

## 🛡️ 7. Governance & FAIR+CARE Implications

Although soils data is generally non-sensitive:

- **Magnitude and pattern of changes** can influence:
  - Long-term land-use decisions.  
  - Interpretive maps used in risk/heritage contexts.  

Therefore:

- Deltas must be:
  - Accurate, reproducible, and **non-lossy** with respect to soils change semantics.  
  - Interpreted in governance-aware contexts when used to revise risk or sensitivity overlays.

Any delta that suggests:

- Major classification shifts.  
- Systematic changes in key interpretation attributes.

should be explicitly discussed in:

- `diff-report-YYYY.md`  
- Relevant domain-working group notes (hydrology, archaeology, planning).

---

## 🕰️ 8. Version History (Deltas Index)

| Version  | Date       | Author                                   | Summary                                                                 |
|----------|------------|------------------------------------------|-------------------------------------------------------------------------|
| v11.2.3  | 2025-12-03 | Geospatial Systems WG · FAIR+CARE Council | Initial soils deltas README; defined directory layout, conceptual schemas, relationships to processing/STAC/provenance layers, and telemetry/CI expectations. |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — MIT**  
FAIR+CARE Certified · MCP-DL v6.3 · KFM-MDP v11.2.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[⬅ Back to Annual Soils Refresh](../README.md) · [⬅ Back to Soils Processing Overview](../processing/README.md) · [📜 Governance Charter](../../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>

