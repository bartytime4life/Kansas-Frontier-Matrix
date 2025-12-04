---
title: "🧪 KFM v11.2.3 — NRCS Soils Schema & Topology Validation Summary (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
description: "Schema, referential integrity, and geometry/topology validation summary for the annual NRCS SSURGO/gNATSGO soils refresh in the Kansas Frontier Matrix."
path: "docs/data/soils/annual-refresh/processing/schema-validation.md"
version: "v11.2.3"
last_updated: "2025-12-03"

release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Annual · Geospatial Systems · FAIR+CARE Oversight"
content_stability: "draft"
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

doc_kind: "Validation Summary"
intent: "nrcs-soils-annual-refresh-schema-validation"

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

json_schema_ref: "../../../../../schemas/json/data-soils-annual-refresh-schema-validation-readme-v1.json"
shape_schema_ref: "../../../../../schemas/shacl/data-soils-annual-refresh-schema-validation-readme-v1.shape.ttl"

immutability_status: "version-pinned"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"

ttl_policy: "Permanent"
sunset_policy: "Never (schema validation summary is an immutable annual audit artifact)"
---

<div align="center">

# 🧪 NRCS Soils Schema & Topology Validation Summary — 2025 Refresh  
**SSURGO · gNATSGO · Tables · Dictionaries · Geometry**  
`docs/data/soils/annual-refresh/processing/schema-validation.md`

**Purpose:**  
Summarize the **schema, referential integrity, and geometry/topology validation** results for the **2025 NRCS soils refresh (SSURGO & gNATSGO)** as processed by the KFM **Annual Soils Refresh** pipeline.

> **Status:**  
> This document is a **governed shell**; all `TBD` metrics MUST be populated from actual validation runs and telemetry before finalization.

</div>

---

## 📘 1. Scope & Inputs

**Upstream inputs:**

- `raw/ssurgo-2025.zip` — official NRCS SSURGO 2025 bundle (Kansas AOI or national).  
- `raw/gnatsgo-2025.zip` — official NRCS gNATSGO 2025 bundle.  
- `raw/metadata/*.xml` — FGDC/ISO metadata and NRCS documentation for 2025.

**Baseline for comparison:**

- 2024 KFM soils baseline (validated SSURGO/gNATSGO tables and geometries).  
- 2024 validation results (this document’s previous-year counterpart) for context.

This validation summary covers:

- **Tabular schema** (table structure, column presence/types).  
- **Referential integrity** (mapunit → component → horizon → lab tables).  
- **Domain/dictionary** conformance.  
- **Geometry/topology** checks (polygon validity, slivers, overlaps where relevant).

Detailed diff results (what changed between 2024 and 2025) are captured separately in:

- `diff-report-2025.md`  
- `../deltas/*.parquet`

---

## 📊 2. Validation Coverage

> Fill these metrics from actual pipeline runs.

### 2.1 Tables & Records (SSURGO 2025)

| Table Name  | Rows (2024) | Rows (2025) | Checked (Y/N) | Notes     |
|------------|-------------|-------------|---------------|----------|
| `mapunit`  | `TBD`       | `TBD`       | `TBD`         | `TBD`    |
| `component`| `TBD`       | `TBD`       | `TBD`         | `TBD`    |
| `chorizon` | `TBD`       | `TBD`       | `TBD`         | `TBD`    |
| `muaggatt` | `TBD`       | `TBD`       | `TBD`         | `TBD`    |
| …          | `TBD`       | `TBD`       | `TBD`         | `TBD`    |

### 2.2 Tables & Records (gNATSGO 2025)

| Dataset    | Tiles/Records (2024) | Tiles/Records (2025) | Checked (Y/N) | Notes |
|-----------|----------------------|----------------------|---------------|-------|
| gNATSGO   | `TBD`                | `TBD`                | `TBD`         | `TBD` |

---

## 🧱 3. Tabular Schema Validation

### 3.1 Column & Type Checks

For each NRCS tableset, confirm:

- Expected tables present.  
- Expected columns present and of compatible types.  
- No unexpected breaking type changes.

> Summaries here; details may live in machine logs or ancillary markdown.

Example structure:

- **SSURGO 2025:**
  - ✅ All required tables present (`mapunit`, `component`, `chorizon`, `muaggatt`, etc.).  
  - ✅ No breaking column removals.  
  - ⚠ `TBD` new columns added in `TBD` table(s) (document and crosswalk if needed).  
  - ❌ `TBD` if any breaking changes occur (explain remediation).

- **gNATSGO 2025:**
  - ✅ Geospatial tiles referenced as expected.  
  - ✅ Attribute tables align with 2024 structure.  
  - ⚠ `TBD` if any new attribute fields appear.

Per-table issues should be itemized if they have downstream significance.

---

## 🔗 4. Referential Integrity Checks

### 4.1 Key Relationships

The following key relationships are validated:

- `mapunit.mukey` → `component.mukey`  
- `component.cokey` → `chorizon.cokey`  
- Additional keys for:
  - Lab tables, taxonomic tables, or interpretation tables (if used).

### 4.2 Integrity Metrics

> Fill from actual validation output.

| Relationship                              | Broken Links (Count) | 2024 Broken | 2025 Broken | Notes                    |
|-------------------------------------------|----------------------|-------------|-------------|--------------------------|
| `mapunit.mukey` → `component.mukey`       | `TBD`                | `TBD`       | `TBD`       | `TBD`                    |
| `component.cokey` → `chorizon.cokey`      | `TBD`                | `TBD`       | `TBD`       | `TBD`                    |
| `component.cokey` → `labtable.cokey` (opt)| `TBD`                | `TBD`       | `TBD`       | `TBD`                    |

**Interpretation:**

- Ideally, broken links trend **downward or stable**.  
- Any increase in broken links MUST be:
  - Investigated.  
  - Documented here and in the diff report if it affects interpretation.

---

## 📚 5. Dictionary & Domain Validation

### 5.1 Domain Checks

For important coded fields:

- Validate that values are within known domain sets.  
- Detect new or deprecated codes.  

Examples (non-exhaustive):

- Soil texture codes.  
- Drainage class codes.  
- Hydrologic group codes.  
- Restrictive layer codes.

### 5.2 Summary of Domain Issues

> Populate from validation jobs.

| Domain / Field     | Issues Found            | Notes                                          |
|--------------------|-------------------------|------------------------------------------------|
| `TBD` (e.g., `texcl`) | `TBD` new / `TBD` unknown | New codes; confirm with NRCS documentation.    |
| `TBD`              | `TBD` deprecated        | Remapped or flagged in KFM metadata/styling.   |

Any domain-level changes MUST be reflected in:

- Derived KFM soil interpretations.  
- Styling rules used in maps and overlays.  
- Documentation and user-facing guidance for risk/interpretation layers.

---

## 🗺️ 6. Geometry & Topology Validation

### 6.1 Polygon Validity

Checks:

- Polygon ring orientation and closure.  
- Self-intersections and invalid geometries.  
- Multi-part vs single-part expectations.

> Populate stats from geometry validation tool.

| Metric                                | Value | Notes                    |
|---------------------------------------|------:|--------------------------|
| Total polygons checked (2025)         | `TBD` |                          |
| Invalid polygons detected             | `TBD` |                          |
| Polygons repaired (auto)             | `TBD` | Logged in processing logs |
| Polygons requiring manual follow-up   | `TBD` | If any, documented here. |

### 6.2 Topology Summary (High-Level)

Narrative summary of:

- Where geometry problems occur (if any).  
- Sliver or gap issues along boundaries.  
- Cross-year topology differences that may matter for:

  - Watershed boundaries.  
  - Region-based soil queries.  
  - Map generalization.

---

## 🧯 7. Issues, Remediation & Open Questions

This section should be populated after QA, with explicit references to remediation steps.

### 7.1 Known Issues (2025)

> Example structure; fill with real content.

- **Issue `TBD-001`:** `TBD` description.  
  - Impact: `TBD` (e.g., affects `TBD` mapunits/components).  
  - Status: `TBD` (e.g., resolved via KFM-side correction, escalated to NRCS, accepted as-is).

### 7.2 Remediation Summary

- `TBD` QA fixes applied at KFM ingest stage (documented in PROV-O and diff report).  
- `TBD` issues deferred to future cycles or flagged in user-facing documentation.

### 7.3 Open Questions

List any unresolved items requiring:

- NRCS clarification.  
- Cross-team discussion (e.g., hydrology WG, archaeology WG).  
- Future pipeline/methodology changes.

---

## 🧬 8. Methodology & Tools

High-level description of tools used:

- **Schema validation:**  
  - `TBD` (e.g., custom SQL scripts / Great Expectations / Python checks).

- **Geometry validation:**  
  - `TBD` (e.g., GDAL/OGR, PostGIS `ST_IsValid`, dedicated topology tools).

- **Domain/dictionary validation:**  
  - `TBD` (e.g., Python-based dictionary checks, NRCS domain tables).

Methodology must be consistent with:

- `processing/README.md` (overall processing layer).  
- PROV-O lineage events recorded in `lineage-events.json`.

---

## 🕰️ 9. Version History (Schema Validation Summary)

| Version  | Date       | Author                                   | Summary                                                                 |
|----------|------------|------------------------------------------|-------------------------------------------------------------------------|
| v11.2.3  | 2025-12-03 | Geospatial Systems WG · FAIR+CARE Council | Created 2025 schema/topology validation summary shell for NRCS soils; metrics and details TBD pending pipeline run output. |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — MIT**  
FAIR+CARE Certified · MCP-DL v6.3 · KFM-MDP v11.2.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[⬅ Back to Soils Processing Overview](README.md) · [⬅ Back to Annual Soils Refresh](../README.md) · [📜 Governance Charter](../../../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>

