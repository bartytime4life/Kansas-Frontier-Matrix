---
title: "🌱 Kansas Frontier Matrix — Soil Data Source Comparison & Provenance Standard (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/standards/geo/soil-source-comparison.md"

version: "v11.2.2"
last_updated: "2025-11-27"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Annual · FAIR+CARE Council"
content_stability: "stable"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256-hash>"

sbom_ref: "../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../releases/v11.2.2/standards-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/standards-soil-source-comparison-v11.2.2.json"
energy_schema: "../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../schemas/telemetry/carbon-gco2e-v1.json"

governance_ref: "../governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"

status: "Active / Enforced"
doc_kind: "Standard"
intent: "soil-source-comparison-and-provenance-guidance"
fair_category: "F1-A1-I2-R2"
care_label: "Respect · Protect · Authority-to-Control"

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "TechArticle"
  prov_o: "prov:Plan"

metadata_profiles:
  - "PROV-O"
  - "FAIR+CARE"
  - "DCAT 3.0"
  - "STAC 1.0.0"

json_schema_ref: "../../../schemas/json/soil-source-comparison-v11.2.2.schema.json"
shape_schema_ref: "../../../schemas/shacl/soil-source-comparison-v11.2.2-shape.ttl"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summary"
  - "semantic-highlighting"
  - "diagram-extraction"
  - "metadata-extraction"
ai_transform_prohibited:
  - "content-alteration"
  - "speculative-additions"
  - "governance-override"
  - "narrative-fabrication"

layout_profiles:
  - "immediate-one-branch-with-descriptions-and-emojis"
badge_profiles:
  - "root-centered-badge-row"
requires_purpose_block: true
requires_directory_layout_section: true
requires_version_history: true
requires_governance_links_in_footer: true

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
jurisdiction: "Kansas / United States"
classification: "Public (Governed)"
ttl_policy: "24 months"
sunset_policy: "Superseded by next soil standard revision"
---

<div align="center">

# 🌱 Kansas Frontier Matrix  
## **Soil Data Source Comparison & Provenance Standard**  
### (SDA · SSURGO · STATSGO2 · gNATSGO)  

`docs/standards/geo/soil-source-comparison.md`

**Purpose**  
Provide a unified, audit-ready comparison of the four major NRCS soil data pathways and define KFM rules for **provenance**, **lineage**, and **reproducibility** across geospatial, archaeological, hydrologic, and landscape-modeling contexts, so SDA (live) and gNATSGO/SSURGO/STATSGO2 (snapshots) are used consistently and safely.

</div>

---

## 📘 1. Overview

KFM integrates soil information from multiple NRCS pathways:

- **SDA** (Soil Data Access – live database/API)  
- **SSURGO** (vector soil surveys)  
- **STATSGO2** (generalized soil associations)  
- **gNATSGO** (derived 10 m composite raster geodatabase)

Each pathway differs in:

- Geometry type (vector vs raster)  
- Scale and intended use  
- Refresh cadence and versioning model  
- Access pattern (live API vs downloads)

This standard prevents:

- Silent drift between **live SDA queries** and **snapshot products**  
- Mixing sources without explicit documentation  
- Ambiguous or irreproducible soil-based analysis and modeling

It applies to:

- Archaeological landscape analyses  
- Hydrologic, ecological, geomorphic, and suitability modeling  
- AI/ML pipelines using soil as predictors or covariates  
- Any STAC/DCAT items that embed soil-derived features

---

## 📊 2. Comparison Table

### 2.1 Feature Matrix

| Dimension         | **SDA**                                   | **SSURGO**                               | **STATSGO2**                            | **gNATSGO**                                      |
|------------------|-------------------------------------------|------------------------------------------|-----------------------------------------|--------------------------------------------------|
| **Type**         | Live database w/ REST/SOAP SQL-like API   | Detailed vector soil survey              | Generalized vector soil associations    | Composite 10 m raster geodatabase                |
| **Primary Use**  | On-demand AOI queries; “current truth”    | Fine-scale site/regional mapping         | Broad regional/eco/hydro context        | Large-scale 10 m modeling, ML predictors         |
| **Geometry**     | Vector features returned from national DB | Detailed polygons (map units)            | Generalized polygons                    | Raster grid (10 m) with attribute tables         |
| **Scale**        | Inherits source surveys                   | ~1:12k–1:24k                              | ~1:250k                                 | 10 m grid; derived from SSURGO/STATSGO/RSS       |
| **Coverage**     | National via backend DB                   | Nationwide (varying survey completeness) | Nationwide                              | Nationwide (CONUS/State)                         |
| **Refresh**      | Live / continuous updates                 | Periodic releases                         | Infrequent major refreshes              | Annual composite refresh                         |
| **Access**       | REST/JSON/XML via SDA                     | FGDB/SQLite downloads from NRCS         | FGDB from NRCS                          | FGDB + raster exports (e.g., GeoTIFF, Cloud DB)  |
| **KFM Best Use** | Deterministic AOI pulls & updated joins   | High-detail excavations & site mapping   | Broad physio-region context             | ML-ready statewide rasters + large-scale models  |

---

## 🧬 3. Provenance Requirements

### 3.1 SDA Usage (Live, Non-Snapshot)

Every SDA-backed computation MUST record:

```json
{
  "soil_source": "SDA",
  "sda_query_timestamp_utc": "<UTC ISO8601>",
  "sda_query_sql_hash": "<sha256(SQL text)>",
  "sda_endpoint_version": "<if returned>",
  "sda_aoi_geometry_wkt_hash": "<sha256(AOI geometry WKT)>"
}
```

**Rationale:**

- SDA is inherently **live**; underlying data can change.  
- Provenance MUST allow others to:
  - Re-execute the query (or understand why they cannot perfectly)  
  - Detect drift vs gNATSGO or SSURGO-based snapshots  
  - Evaluate temporal context of soil assumptions

SDA-based workflows should be used **cautiously** when absolute reproducibility is a hard requirement.

---

### 3.2 gNATSGO Usage (Annual Composite Raster)

Store release tag and composition:

```json
{
  "soil_source": "gNATSGO",
  "gnatsgo_release_tag": "gNATSGO_CONUS_2023",
  "gnatsgo_source_mix": {
    "ssurgo_contribution": true,
    "statsgo2_contribution": true,
    "rss_contribution": true
  }
}
```

**Rationale:**

- gNATSGO is a **refresh-bound** composite.  
- The release tag defines the:
  - Soil attribute semantics  
  - Derived field definitions  
  - Underlying updates from SSURGO/STATSGO/RSS

Any model or derived dataset using gNATSGO MUST clearly record the `gnatsgo_release_tag`.

---

### 3.3 SSURGO / STATSGO2 Usage (Snapshot Vectors)

For SSURGO:

```json
{
  "soil_source": "SSURGO",
  "ssurgo_download_date": "<ISO8601>",
  "ssurgo_snapshot": "<portal/origin tag or URL>",
  "ssurgo_survey_areas": ["KS001", "KS002", "NE100", "..."]
}
```

For STATSGO2:

```json
{
  "soil_source": "STATSGO2",
  "statsgo2_download_date": "<ISO8601>",
  "statsgo2_snapshot": "<portal/origin tag or URL>"
}
```

**Rationale:**

- SSURGO/STATSGO2 are nominally stable after download.  
- Snapshot identifiers and survey coverage are key for:
  - Interpreting map-unit meanings  
  - Aligning with historical analyses  
  - Confirming what *version* of the soil surveys were used

---

## 🧾 4. STAC & Metadata Integration

Soil-backed STAC Items & Collections MUST store soil provenance in consistent fields.

### 4.1 Required STAC Properties

Minimum soil-related fields:

- `soil:source` — `"SDA"`, `"SSURGO"`, `"STATSGO2"`, or `"gNATSGO"`  
- `soil:refresh_cadence` — `"live"`, `"annual"`, `"snapshot"`  
- `soil:product_line` — textual descriptor (e.g., `"SSURGO-backed national DB"`)  
- `soil:lineage` — short description or ID referencing full provenance record  

Example STAC properties block:

```json
{
  "soil:source": "SDA",
  "soil:refresh_cadence": "live",
  "soil:product_line": "SSURGO-backed SDA national DB",
  "soil:lineage": "SDA query at 2025-11-27T05:41:00Z; SQL hash 5b3c..."
}
```

For gNATSGO:

```json
{
  "soil:source": "gNATSGO",
  "soil:refresh_cadence": "annual",
  "soil:product_line": "gNATSGO_CONUS_2023",
  "soil:lineage": "Derived from SSURGO + STATSGO2 + RSS (NRCS)"
}
```

These properties MUST be present for any STAC Items whose assets encode soil attributes.

---

## 🧭 5. KFM Guidance — When to Use Which Source

### 5.1 SDA (Soil Data Access – Live)

Use SDA when:

- You need **current truth** for soil properties at an AOI.  
- Doing **targeted AOI queries** for:
  - Archaeological sites  
  - Infrastructure corridors  
  - Small hydrologic catchments  
- Prototyping or exploratory analysis that informs a later snapshot-based workflow.

Be aware:

- SDA may **not** be perfectly reproducible later.  
- For publishable analyses, prefer aligning SDA with a recognized gNATSGO / SSURGO snapshot.

---

### 5.2 SSURGO

Use SSURGO when:

- Fine-scale feature interpretation is required:
  - Excavation boundaries  
  - Micro-watersheds  
  - Slope/aspect/soil interplay  
- You need polygon-level provenance:
  - Map unit codes  
  - Survey metadata  
  - Legacy site interpretations  

SSURGO is the **anchor** for site-level archaeologic and geomorphic work.

---

### 5.3 STATSGO2

Use STATSGO2 when:

- Broad physiographic / eco-region context is sufficient (1:250k scale).  
- You’re summarizing over:
  - Counties  
  - Multi-county regions  
  - River basins  
- You need a lower-resolution substrate to avoid overprecision.

STATSGO2 is a **contextual backdrop**, not a substitute for SSURGO at site scale.

---

### 5.4 gNATSGO

Use gNATSGO when:

- Building **ML/AI predictors** that require rasterized soil attributes.  
- Modeling at statewide or CONUS scales:
  - Erosion potential  
  - Carbon  
  - Recharge  
  - Suitability indices  
- You need:
  - Consistent 10 m grid  
  - Annual snapshot reproducibility  
  - High-performance ingest into tiled formats (COGs, GeoParquet, Zarr)

gNATSGO is the **primary ML-ready soil raster** for KFM.

---

## 🗺️ 6. Directory Layout (Standards Context)

```text
📁 docs/
└── 📁 standards/
    ├── 📁 geo/
    │   ├── 📄 soil-source-comparison.md         — ← This file
    │   ├── 📄 vertical-axis-and-dod.md          — Vertical datums · DoD sign convention
    │   ├── 📄 h3-generalization.md              — Static H3 generalization rules
    │   └── 📄 dynamic-h3-generalization.md      — Dynamic, context-aware H3 masking
    └── 📁 governance/
        └── 📄 ROOT-GOVERNANCE.md
```

This ensures geo standards are discoverable and consistent with the KFM v11.2.2 canonical layout.

---

## 🕰️ 7. Version History

| Version | Date       | Summary                                                                                      |
|--------:|------------|----------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-27 | Upgraded to KFM-MDP v11.2.2; added telemetry hooks, STAC fields, and explicit SDA/gNATSGO provenance models. |
| v11.1.0 | 2025-11-27 | Initial soil-source comparison standard; established baseline SDA/SSURGO/STATSGO2/gNATSGO guidance.        |

---

<div align="center">

🌱 **Kansas Frontier Matrix — Soil Data Source Comparison & Provenance Standard (v11.2.2)**  
“Soil is slow memory. Provenance keeps it honest.”

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
FAIR+CARE Council · MCP-DL v6.3 · KFM-MDP v11.2.2  

[⬅ Back to Geo Standards](../README.md) ·  
[⚖ Root Governance Charter](../governance/ROOT-GOVERNANCE.md)

</div>
