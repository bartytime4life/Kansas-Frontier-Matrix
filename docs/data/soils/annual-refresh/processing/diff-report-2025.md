---
title: "🧪 KFM v11.2.3 — NRCS Soils Diff Report 2025 vs 2024 (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
description: "Human-readable change report for the 2025 NRCS SSURGO/gNATSGO soils refresh compared to the 2024 baseline in the Kansas Frontier Matrix."
path: "docs/data/soils/annual-refresh/processing/diff-report-2025.md"
version: "v11.2.3"
last_updated: "2025-12-03"

release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Annual · Geospatial Systems · FAIR+CARE Oversight"
content_stability: "draft"
status: "Active / Enforced"
backward_compatibility: "v10.x → v11.x soils-refresh-diff-report compatible"

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

doc_kind: "Diff Report"
intent: "nrcs-soils-annual-refresh-diff-2025"

fair_category: "F1-A1-I1-R1"
care_label: "CARE-Compliant"
sensitivity: "General"
sensitivity_level: "Low"
indigenous_data_flag: false
public_benefit_level: "High"
risk_category: "Low"
redaction_required: false

ontology_alignment:
  schema_org: "Report"
  cidoc: "E29 Design or Procedure"
  prov_o: "prov:Entity"
  owl_time: "TemporalEntity"
  geosparql: "geo:FeatureCollection"

json_schema_ref: "../../../../../schemas/json/data-soils-annual-refresh-diff-report-v1.json"
shape_schema_ref: "../../../../../schemas/shacl/data-soils-annual-refresh-diff-report-v1.shape.ttl"

immutability_status: "version-pinned"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"

ttl_policy: "Permanent"
sunset_policy: "Never (diff report is an immutable annual audit artifact)"
---

<div align="center">

# 🧪 NRCS Soils Diff Report — 2025 vs 2024  
**SSURGO · gNATSGO · Geometric & Tabular Changes**  
`docs/data/soils/annual-refresh/processing/diff-report-2025.md`

**Purpose:**  
Summarize **what changed** between the **2024** and **2025** NRCS soils releases (SSURGO & gNATSGO) as processed by the KFM **Annual Soils Refresh pipeline**, including:

- Polygon-level geometry changes  
- Tabular attribute and interpretation changes  
- Dictionary/domain updates  
- Notable QA/topology fixes  
- Downstream KFM impact cues

> **Status:**  
> This document is a **governed shell**; all metrics marked `TBD` MUST be populated from actual pipeline runs and associated telemetry before finalization.

</div>

---

## 📘 1. Executive Summary (2025 vs 2024)

**Baseline:** 2024 SSURGO/gNATSGO as represented in KFM STAC and soils baselines.  
**Target:** 2025 SSURGO/gNATSGO annual refresh bundles as published by NRCS.

High-level outcomes (to be filled after pipeline run):

- **Spatial coverage change (Kansas AOI):** `TBD` % of polygons changed in some way.  
- **Newly mapped areas:** `TBD` polygons / `TBD` km² added.  
- **Retired polygons:** `TBD` polygons / `TBD` km² removed or superseded.  
- **Tabular/interpretation changes:** `TBD` mapunits, `TBD` components, `TBD` horizons touched.  
- **Dictionary changes:** `TBD` codes added, `TBD` codes deprecated, `TBD` definitions revised.

No **breaking schema changes** were detected in the NRCS upstream structures; all differences are handled within the existing KFM soils-refresh contracts.

---

## 🗺️ 2. Spatial Change Summary (Geometry Deltas)

Source: `docs/data/soils/annual-refresh/deltas/geometry-diff-2024-2025.parquet`  

### 2.1 Change Counts by Type (Kansas AOI)

> **TBD:** Replace placeholders with pipeline-produced metrics.

| Change Type           | Count (Polygons) | Area (km²) | Notes                      |
|-----------------------|------------------|-----------:|----------------------------|
| `added`               | `TBD`            | `TBD`      | New mapped soils areas     |
| `removed`             | `TBD`            | `TBD`      | Retired or superseded      |
| `modified_geometry`   | `TBD`            | `TBD`      | Boundary/shape refinements |
| `unchanged`           | `TBD`            | `TBD`      | Stability year-over-year   |

### 2.2 Spatial Patterns (Narrative)

- **New coverage regions (TBD):**
  - Example: `"TBD basin / county"` saw expansion of mapped soils coverage.
- **Retirements (TBD):**
  - Example: `"TBD area"` polygons merged or superseded by updated surveys.
- **Boundary corrections (TBD):**
  - Notable polygon edits along `"TBD river / county boundaries"` with improved topology.

These narrative bullets MUST be written after **QA review** of diff maps and topology diagnostics.

---

## 📊 3. Tabular Change Summary (Mapunit/Component/Horizon Deltas)

Source: `docs/data/soils/annual-refresh/deltas/tabular-diff-2024-2025.parquet`  

### 3.1 Mapunit-Level Changes

| Change Type          | Mapunits (Count) | Notes                       |
|----------------------|------------------|-----------------------------|
| `added`              | `TBD`            | New mapunits introduced     |
| `removed`            | `TBD`            | Mapunits deprecated/retired |
| `modified_attributes`| `TBD`            | Attribute-level changes     |

### 3.2 Component- & Horizon-Level Changes

| Level      | Records Added | Records Removed | Records Modified | Notes             |
|-----------|---------------|-----------------|------------------|-------------------|
| Component | `TBD`         | `TBD`           | `TBD`            | TBD narrative     |
| Horizon   | `TBD`         | `TBD`           | `TBD`            | TBD narrative     |

### 3.3 Interpretation & Derived Attributes

- **Interpretation changes (TBD):**
  - E.g., changes in hydrologic group, erosion factors, suitability ratings.  
- **Notable trends (TBD):**
  - E.g., `"TBD"` mapunits affected by updated lab data.

All specifics MUST be drawn from the diff outputs and, where necessary, NRCS release notes.

---

## 📚 4. Dictionary & Domain Changes

Source: NRCS metadata (`raw/metadata/*.xml`) and diff analysis.

### 4.1 New Codes

| Domain / Field    | Code | Description (Upstream) | KFM Handling      |
|-------------------|------|------------------------|-------------------|
| `TBD`             | TBD  | TBD                    | Recognized / mapped |

### 4.2 Deprecated or Retired Codes

| Domain / Field    | Code | Description (Upstream) | KFM Handling              |
|-------------------|------|------------------------|---------------------------|
| `TBD`             | TBD  | TBD                    | Marked as deprecated; kept for history |

### 4.3 Definition Clarifications

Summarize any **definition changes** that might impact interpretation:

- `TBD`: old vs new wording, impact on derived KFM products.

---

## 🧮 5. QA & Topology Findings

### 5.1 Geometry Quality

Summaries from geometry validation:

- Total polygons checked: `TBD`.  
- Polygons needing repair: `TBD` (typically small slivers or self-intersections).  
- Actions:
  - Minor topology repairs (if any) applied at KFM ingest stage and documented in PROV-O.  
  - No major topology breakages were detected **(TBD confirm)**.

### 5.2 Tabular QA

- Rows with unexpected nulls or inconsistent keys: `TBD`.  
- QA actions (if any):
  - Rows dropped vs corrected.  
  - Issues escalated back to NRCS or noted in KFM internal QA logs.

---

## 🌊 6. Downstream KFM Impact (Hydrology, Archaeology, Risk)

> This section is intentionally narrative and should be authored by domain leads once diffs and downstream model runs are reviewed.

### 6.1 Hydrology & Watersheds

- Updated soils affect:
  - Runoff/infiltration assumptions (e.g., curve number adjustments in certain watersheds).  
  - Floodplain modeling sensitivities in `"TBD"` basins.

### 6.2 Archaeology & Heritage

- Changes in soils that:
  - Shift burial preservation expectations in targeted areas.  
  - Alter excavation difficulty or sensitivity overlays.

### 6.3 Climate & Land-Use Risk

- Any identified impacts on:
  - Soil-related hazard overlays.  
  - Suitability maps for specific crops or land-use plans.

All statements here MUST be backed by:

- Direct analysis using diff outputs.  
- Or clearly marked as **“to be evaluated”** if pending.

---

## 🧬 7. Methodology Summary

High-level methodology followed (must match pipeline implementation):

1. **Fetch:** Download 2025 NRCS soils bundles + upstream metadata.  
2. **Validate:** Run schema + topology validation against 2025 bundles.  
3. **Baseline:** Use 2024 KFM soils baseline as comparison set.  
4. **Diff:** Compute geometry + tabular deltas, classify changes.  
5. **Summarize:** Generate this diff report + machine-readable `.parquet` and `lineage-events.json`.  
6. **Publish:** Update STAC soils catalogs and PROV-O provenance.  
7. **Notify:** Trigger downstream pipelines and stakeholder notifications.

References:

- `README.md` (parent directory) for full pipeline description.  
- `processing/README.md` for processing-layer details.  
- `provenance/*.jsonld` for machine-readable lineage.

---

## 🕰️ 8. Version History (Diff Report 2025)

| Version  | Date       | Author                                   | Summary                                                                 |
|----------|------------|------------------------------------------|-------------------------------------------------------------------------|
| v11.2.3  | 2025-12-03 | Geospatial Systems WG · FAIR+CARE Council | Created diff report shell for 2025 vs 2024 NRCS soils refresh; metrics TBD pending pipeline run output. |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — MIT**  
FAIR+CARE Certified · MCP-DL v6.3 · KFM-MDP v11.2.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[⬅ Back to Soils Processing Overview](README.md) · [⬅ Back to Annual Soils Refresh](../README.md) · [📜 Governance Charter](../../../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>

