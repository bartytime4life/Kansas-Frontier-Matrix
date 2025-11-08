---
title: "🧮 Abandonment Candidate Queries — Spatial Detection & Scoring Logic (KFM-Ready)"
path: "data/work/staging/tabular/abandonment_candidates/queries/README.md"
version: "v9.9.0"
last_updated: "2025-11-08"
review_cycle: "Continuous / Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../releases/v9.9.0/sbom.spdx.json"
manifest_ref: "../../../../../releases/v9.9.0/manifest.zip"
data_contract_ref: "../../../../../docs/contracts/data-contract-v3.json"
telemetry_ref: "../../../../../releases/v9.9.0/focus-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/abandonment-candidates-queries-v1.json"
governance_ref: "../../../../../docs/standards/governance/DATA-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 🧮 Kansas Frontier Matrix — **Abandonment Candidate Queries**
`data/work/staging/tabular/abandonment_candidates/queries/README.md`

**Purpose:**  
Document the **SQL and spatial query logic** used to identify, validate, and score potential **abandonment or relocation sites** within Kansas Frontier Matrix (KFM).  
Queries unify historical census, environmental, and cadastral datasets to calculate a reproducible abandonment likelihood index under **FAIR+CARE** and **MCP-DL v6.3** governance.

[![Docs · MCP](https://img.shields.io/badge/Docs·MCP-v6.3-blue)](../../../../../docs/)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY--4.0-green)](../../../../../LICENSE)
[![FAIR+CARE](https://img.shields.io/badge/FAIR+CARE-Governance%20Certified-orange)](../../../../../docs/standards/FAIRCARE.md)
[![Status: Stable](https://img.shields.io/badge/Status-Stable-brightgreen)](#)

</div>

---

## 📘 Overview

The **Queries Submodule** provides standardized spatial SQL and scoring scripts used to generate `abandonment_candidates.csv`.  
These queries rely on **PostGIS 3.x** and **PostgreSQL 15+**, with optional integration into **Neo4j spatial extensions**.  
They enable transparent, reproducible candidate detection that aligns with KFM’s **governance-led FAIR+CARE methodology**.

### Core Functions
- Identify overlapping environmental hazards and demographic losses.  
- Compute weighted abandonment scores for each geographic feature.  
- Flag sites for further FAIR+CARE ethical or data quality review.  
- Export GeoJSON/CSV for visualization or governance audit.

---

## 🗂️ Directory Layout

```plaintext
data/work/staging/tabular/abandonment_candidates/queries/
├── README.md                 # This documentation file
├── abandonment_query.sql     # Core candidate selection logic
├── remediation_check.sql     # Schema and record validation before recovery
├── scoring_heuristic.sql     # Weighted scoring for abandonment likelihood
└── metadata.json             # Query lineage, checksum, and governance metadata
```

---

## ⚙️ Query Overview

### `abandonment_query.sql` — Candidate Detection
Detects areas of severe population loss intersecting with drought, flood, or buyout regions.

```sql
SELECT
  c.geoid,
  c.county_name,
  c.pop_change_pct,
  f.buyout_id,
  d.drought_severity,
  h.flood_depth,
  p.parcel_id,
  ST_Area(ST_Intersection(c.geom, COALESCE(f.geom, d.geom, h.geom))) AS overlap_area
FROM census_loss_1930_1940 c
LEFT JOIN fema_buyouts f ON ST_Intersects(c.geom, f.geom)
LEFT JOIN drought_dustbowl_1930s d ON ST_Intersects(c.geom, d.geom)
LEFT JOIN hydro_floods_1993 h ON ST_Intersects(c.geom, h.geom)
LEFT JOIN parcel_history p ON ST_Intersects(c.geom, p.geom)
WHERE c.pop_change_pct <= -50
  AND (f.buyout_id IS NOT NULL OR d.drought_severity >= 3)
ORDER BY overlap_area DESC, c.pop_change_pct ASC;
```

---

### `scoring_heuristic.sql` — Weighted Composite Score
Combines demographic, hydrologic, and infrastructural indicators into a single abandonment likelihood metric.

```sql
SELECT
  a.geoid,
  a.county_name,
  ROUND(
    0.4 * ABS(a.pop_change_pct) +
    0.3 * COALESCE(f.buyout_density, 0) +
    0.2 * COALESCE(d.drought_index, 0) +
    0.1 * (1 - (r.distance_km / 5.0))
  , 3) AS abandonment_score
FROM abandonment_base a
LEFT JOIN fema_buyout_density f USING (geoid)
LEFT JOIN drought_index d USING (geoid)
LEFT JOIN railroad_proximity r USING (geoid)
WHERE a.pop_change_pct <= -30;
```

---

### `remediation_check.sql` — Recovery Eligibility
Validates whether a quarantined dataset can be restored to staging or requires archival.

```sql
SELECT
  id,
  schema_conform,
  ethics_status,
  CASE
    WHEN schema_conform = true AND ethics_status = 'approved' THEN 'RESTAGE_ELIGIBLE'
    WHEN ethics_status = 'restricted' THEN 'PENDING_REDACTION'
    ELSE 'ARCHIVE'
  END AS review_decision
FROM abandonment_registry
WHERE review_status = 'pending';
```

---

## 🧩 Scoring Weights (Default Configuration)

| Metric | Weight | Description | Source |
|--------|--------|--------------|---------|
| Population decline | 0.4 | Percent change 1930–1940 | US Census |
| FEMA buyout density | 0.3 | Parcels/km² | OpenFEMA |
| Drought severity | 0.2 | PDSI index | NOAA / USDA |
| Railroad proximity | 0.1 | Distance < 1 km | FRA Historic GIS |

> All weights configurable in `scoring_heuristic.sql` to support custom temporal analyses.

---

## 📊 Output Artifacts

| File | Purpose | Format |
|------|----------|--------|
| `abandonment_candidates.csv` | Primary output of spatial join and scoring queries | CSV |
| `abandonment_candidates.geojson` | Geospatial representation for visualization | GeoJSON |
| `validation_report.json` | Query integrity and schema validation summary | JSON |
| `provenance_trace.json` | Lineage record for governance ledger | JSON |

---

## ⚖️ FAIR+CARE Governance Alignment

| Principle | Implementation | Audit Reference |
|------------|----------------|-----------------|
| **Findable** | Queries stored under version control; metadata.json logs lineage and hash. | `manifest_ref` |
| **Accessible** | SQL queries are open and documented with SPDX identifiers. | `license` |
| **Interoperable** | Compatible with PostGIS, Neo4j spatial, and DCAT mappings. | `data_contract_ref` |
| **Reusable** | CC-BY 4.0 license and query parameters documented. | `metadata.json` |
| **CARE – Responsibility** | Queries anonymize sensitive geometry and personal data. | `governance_ref` |

---

## 🧾 Internal Citation

```text
Kansas Frontier Matrix (2025). Abandonment Candidate Queries — Spatial Detection & Scoring Logic (v9.9.0).
Defines FAIR+CARE-governed SQL workflows for identifying, scoring, and validating abandonment candidates in Kansas Frontier Matrix data staging pipelines.
```

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|----------|------|--------|----------|
| v9.9.0 | 2025-11-08 | `@kfm-data` | Added remediation validation and governance linkage to abandonment registry. |
| v9.8.0 | 2025-11-06 | `@kfm-geo` | Introduced heuristic scoring query and provenance trace outputs. |
| v9.7.0 | 2025-11-02 | `@kfm-core` | Initial spatial detection query for candidate generation. |

---

<div align="center">

**Kansas Frontier Matrix**  
*Spatial Governance × FAIR+CARE Ethics × Reproducible Analytics*  
© 2025 Kansas Frontier Matrix · Master Coder Protocol v6.3 · FAIR+CARE Certified · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[Back to Abandonment Candidates](../README.md) · [Governance Charter](../../../../../docs/standards/governance/DATA-GOVERNANCE.md)

</div>

