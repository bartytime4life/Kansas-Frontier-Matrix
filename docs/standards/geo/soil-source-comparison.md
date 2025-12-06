---
title: "🌱 Kansas Frontier Matrix — Soil Data Source Comparison & Provenance Standard (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/standards/geo/soil-source-comparison.md"

version: "v11.2.2"
last_updated: "2025-11-27"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Annual · FAIR+CARE Council"
content_stability: "stable"

status: "Active / Enforced"
doc_kind: "Standard"
intent: "soil-source-comparison-and-provenance-guidance"

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
ethics_ref: "../faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.4"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

scope:
  domain: "soil-data-and-provenance"
  applies_to:
    - "geospatial"
    - "hydrology"
    - "archaeology"
    - "landscape-modeling"
    - "etl"
    - "stac"
    - "dcat"
    - "graph"
    - "ai-ml"
    - "story-nodes"
    - "focus-mode"

fair_category: "F1-A1-I2-R2"
care_label: "Respect · Protect · Authority-to-Control"
sensitivity: "General (land & ecological context; sovereignty-aware)"
sensitivity_level: "Low"
public_exposure_risk: "Low"
classification: "Public (Governed)"
jurisdiction: "Kansas / United States"
indigenous_rights_flag: true
data_steward: "KFM FAIR+CARE Council"

ttl_policy: "24 months"
sunset_policy: "Superseded by next soil standard revision"

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "TechArticle"
  prov_o: "prov:Plan"
  geosparql: "geo:FeatureCollection"
  owl_time: "TemporalEntity"

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

transform_registry:
  allowed:
    - summary
    - semantic-highlighting
    - diagram-extraction
    - metadata-extraction
  prohibited:
    - content-alteration
    - speculative-additions
    - governance-override
    - narrative-fabrication

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

heading_registry:
  approved_h2:
    - "🗂️ Directory Layout"
    - "📘 Overview"
    - "🧭 Context"
    - "📦 Data & Metadata"
    - "🌐 STAC, DCAT & PROV Alignment"
    - "🧱 Architecture"
    - "🧪 Validation & CI/CD"
    - "⚖ FAIR+CARE & Governance"
    - "🕰️ Version History"

test_profiles:
  - "markdown-lint"
  - "schema-lint"
  - "metadata-check"
  - "diagram-check"
  - "accessibility-check"
  - "provenance-check"
  - "footer-check"

ci_integration:
  workflow: ".github/workflows/kfm-ci.yml"
  environment: "dev → staging → production"

branding_registry:
  standard: "Scientific Insight × FAIR+CARE Ethics × Sustainable Intelligence"
  architecture: "Designed for Longevity · Governed for Integrity"
  analysis: "Research-Driven · Evidence-Led · FAIR+CARE Grounded"
  data-spec: "Open Data × Responsible Stewardship"
  pipeline: "Deterministic Pipelines · Explainable AI · Open Provenance"
  telemetry: "Transparent Systems · Ethical Metrics · Sustainable Intelligence"
  graph: "Semantics × Provenance × Spatial Intelligence"
---

<div align="center">

# 🌱 Kansas Frontier Matrix  
## **Soil Data Source Comparison & Provenance Standard (v11.2.2)**  
### SDA · SSURGO · STATSGO2 · gNATSGO  

`docs/standards/geo/soil-source-comparison.md`

**Purpose**  
Provide a unified, audit‑ready comparison of the four major NRCS soil data pathways and define KFM rules for **provenance**, **lineage**, and **reproducibility** across geospatial, archaeological, hydrologic, and landscape‑modeling contexts, so SDA (live) and gNATSGO/SSURGO/STATSGO2 (snapshots) are used consistently, ethically, and safely.

</div>

---

## 🗂️ Directory Layout

```text
📂 docs/
└── 📂 standards/
    ├── 📂 geo/
    │   📄 README.md                      # 🌎 Geo Standards Index
    │   📄 soil-source-comparison.md      # 🌱 Soil source & provenance standard (this file)
    │   📄 vertical-axis-and-dod.md       # 📏 Vertical datums · DoD sign convention
    │   📄 hydrology-standards.md         # 💧 Hydrology & water-surface standards (legacy path)
    │   📄 archaeology-sensitive-locations.md  # 🛡 Archaeology & Indigenous overlays (legacy path)
    └── 📂 governance/
        📄 ROOT-GOVERNANCE.md             # ⚖ Root governance charter
```

Author rules:

- This file is the **soil provenance overlay** for the geo standards; it must not contradict:
  - CRS/geometry rules in the CRS/topology standard, or  
  - Hydrology & vertical‑axis standards where soil covariates are used.  
- Any change to soil source usage or provenance fields must update:
  - This document,  
  - The associated JSON/SHACL schemas, and  
  - CI checks that reference soil provenance.

---

## 📘 Overview

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

- Silent drift between **live SDA queries** and **snapshot products**.  
- Mixing soil sources without explicit documentation.  
- Ambiguous or irreproducible soil‑based analysis and modeling.

It applies to:

- Archaeological landscape analyses.  
- Hydrologic, ecological, geomorphic, and suitability modeling.  
- AI/ML pipelines using soil as predictors or covariates.  
- Any STAC/DCAT items that embed soil‑derived features or rasters.  

All soil‑backed KFM work must treat soil datasets as **first‑class, provenance‑rich entities**, not anonymous background layers.

---

## 🧭 Context

This standard sits alongside and depends on:

- **CRS, Geometry & Topology Governance Standard**  
  - Soil geometries and grids must follow canonical CRS/topology rules.  
- **Hydrology & Water Surface Standards**  
  - Soil‑derived covariates in hydrologic models must carry the same vertical and CRS discipline.  
- **Geoprivacy & Cultural‑Safety Masking / Archaeology Standards**  
  - Soil layers used to reason about cultural landscapes must respect sovereignty and masking rules.  
- **Geo Standards Index**  
  - This file is the soil lineage “leaf” in the geo standards subtree.

From the KFM pipeline perspective:

> Soil ETL → STAC/DCAT & PROV catalogs → Neo4j soil/landscape graph → API & ML feature services → MapLibre/Cesium + Story Nodes / Focus Mode

At each stage, the soil source (SDA/SSURGO/STATSGO2/gNATSGO) must be explicit and traceable.

---

## 📦 Data & Metadata

### 1. Soil data source comparison (feature matrix)

#### 1.1 Source feature matrix

| Dimension         | **SDA**                                   | **SSURGO**                               | **STATSGO2**                            | **gNATSGO**                                      |
|------------------|-------------------------------------------|------------------------------------------|-----------------------------------------|--------------------------------------------------|
| **Type**         | Live database w/ REST/SOAP SQL‑like API   | Detailed vector soil survey              | Generalized vector soil associations    | Composite 10 m raster geodatabase                |
| **Primary Use**  | On‑demand AOI queries; “current truth”    | Fine‑scale site/regional mapping         | Broad regional/eco/hydro context        | Large‑scale 10 m modeling, ML predictors         |
| **Geometry**     | Vector features from national DB          | Detailed polygons (map units)            | Generalized polygons                    | Raster grid (10 m) with attribute tables         |
| **Scale**        | Inherits source surveys                   | ~1:12k–1:24k                             | ~1:250k                                 | 10 m grid; derived from SSURGO/STATSGO/RSS       |
| **Coverage**     | National via backend DB                   | Nationwide (varying survey completeness) | Nationwide                              | Nationwide (CONUS/State)                         |
| **Refresh**      | Live / continuous updates                 | Periodic releases                         | Infrequent major refreshes              | Annual composite refresh                         |
| **Access**       | REST/JSON/XML via SDA                     | FGDB/SQLite downloads from NRCS          | FGDB from NRCS                          | FGDB + raster exports (GeoTIFF, Cloud DB, etc.)  |
| **KFM Best Use** | Deterministic AOI pulls & updated joins   | High‑detail excavations & site mapping   | Broad physio‑region context             | ML‑ready statewide rasters & large‑scale models  |

---

### 2. Provenance requirements by source

#### 2.1 SDA usage (live, non‑snapshot)

Every SDA‑backed computation **must** record:

```json
{
  "soil_source": "SDA",
  "sda_query_timestamp_utc": "<UTC ISO8601>",
  "sda_query_sql_hash": "<sha256(SQL text)>",
  "sda_endpoint_version": "<if returned>",
  "sda_aoi_geometry_wkt_hash": "<sha256(AOI geometry WKT)>"
}
```

Key implications:

- SDA is **live**; underlying data can change between runs.  
- Provenance must allow others to:
  - Reconstruct the query context (or understand why exact repro isn’t possible).  
  - Compare SDA‑time to relevant gNATSGO/SSURGO snapshots.  
  - Audit AOI geometry and query structure via hashes.

SDA is **discouraged** for analyses that require strict bit‑for‑bit reproducibility unless accompanied by a synchronized snapshot (e.g., gNATSGO) for archival.

---

#### 2.2 gNATSGO usage (annual composite raster)

Store the release tag and composition:

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

Rules:

- `gnatsgo_release_tag` is **required** for any gNATSGO‑backed dataset or ML feature set.  
- If NRCS provides official composition metadata, `gnatsgo_source_mix` should mirror it.

---

#### 2.3 SSURGO & STATSGO2 usage (snapshot vectors)

**SSURGO:**

```json
{
  "soil_source": "SSURGO",
  "ssurgo_download_date": "<ISO8601>",
  "ssurgo_snapshot": "<portal/origin tag or URL>",
  "ssurgo_survey_areas": ["KS001", "KS002", "NE100"]
}
```

**STATSGO2:**

```json
{
  "soil_source": "STATSGO2",
  "statsgo2_download_date": "<ISO8601>",
  "statsgo2_snapshot": "<portal/origin tag or URL>"
}
```

Rules:

- `*_snapshot` must identify the actual download / portal release.  
- `ssurgo_survey_areas` must list survey area codes used in the AOI or model.  

These fields are required for:

- Any published analysis that calls out specific map units.  
- Any derived layer that aggregates SSURGO/STATSGO2 attributes.

---

## 🌐 STAC, DCAT & PROV Alignment

### 1. STAC soil metadata

Soil‑backed STAC Items and Collections must include soil provenance:

**Minimum STAC properties:**

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

Rules:

- `soil:source` ∈ {`"SDA"`, `"SSURGO"`, `"STATSGO2"`, `"gNATSGO"`}.  
- `soil:refresh_cadence` ∈ {`"live"`, `"annual"`, `"snapshot"`}.  
- `soil:lineage` may be a short description or identifier linking to a PROV bundle.

---

### 2. DCAT alignment

In DCAT:

- Represent soil‑backed layers as `dcat:Dataset` with:
  - `dct:source` or `dct:provenance` referencing NRCS sources.  
  - Custom properties for `soil:source`, `soil:refresh_cadence`, and `soil:product_line` via KFM‑DCAT profile.  

DCAT records should:

- Make clear whether a dataset is tied to a **live** SDA query or a **snapshot** (gNATSGO/SSURGO/STATSGO2).  
- Link to STAC or PROV bundles for detailed soil lineage.

---

### 3. PROV‑O lineage

For any soil‑backed transformation:

- The soil source entity must be explicit:
  - SDA result set, SSURGO polygons, STATSGO2 polygons, or gNATSGO rasters.  
- Activities (ETL steps) must record:
  - Query or download event.  
  - Transformation from raw soil attributes to derived products.  

Typical PROV skeleton:

```text
prov:Entity        soil_source_entity   # SDA / SSURGO / STATSGO2 / gNATSGO
prov:Activity      soil_ingest_activity
prov:wasGeneratedBy soil_ingest_activity
prov:used          soil_source_entity
prov:wasAssociatedWith kfm-etl-soil-pipeline
prov:generatedAtTime  2025-11-27T05:41:00Z
```

`soil:lineage` in STAC/DCAT should ultimately point to such a PROV bundle.

---

## 🧱 Architecture

Conceptually, this standard enforces the following soil path:

1. **Source selection**  
   - Choose SDA / SSURGO / STATSGO2 / gNATSGO based on scale and use case (see guidance below).

2. **Ingest & normalization**  
   - Apply CRS/geometry rules (CRS/topology standard).  
   - Normalize schema into KFM soil models.

3. **Provenance capture**  
   - Record per‑source metadata (timestamps, tags, hashes, release IDs).  
   - Emit PROV bundles and link them in STAC/DCAT.

4. **Derivation & export**  
   - Build derived rasters, features, and ML feature sets.  
   - Carry soil provenance forward into derived artifacts.

5. **Graph & AI integration**  
   - Attach soil provenance nodes and relationships into Neo4j.  
   - Expose soil source information in Focus Mode and Story Nodes for transparency.

---

## 🧪 Validation & CI/CD

Soil‑backed PRs must pass additional checks:

- **Schema‑lint**  
  - `soil:source`, `soil:refresh_cadence`, and `soil:product_line` present where required.  

- **Metadata‑check**  
  - SDA usage includes timestamp, SQL hash, and AOI geometry hash.  
  - gNATSGO usage includes `gnatsgo_release_tag`.  
  - SSURGO/STATSGO2 usage includes snapshot identifiers and dates.

- **Provenance‑check**  
  - `soil:lineage` provided and resolvable (or clearly documented stub for prototypes).  

- **Footer‑check**  
  - Governance links and version history present.

Any missing or inconsistent soil provenance metadata is a **PR blocker** for datasets or analyses that depend on soil.

---

## ⚖ FAIR+CARE & Governance

Soil data participates in FAIR+CARE responsibilities:

- **FAIR**

  - *Findable*: explicit soil source and release tags make soil assumptions indexable and searchable.  
  - *Accessible*: documented provenance improves trust for downstream users.  
  - *Interoperable*: use of STAC/DCAT/PROV keeps soil metadata open and tool‑agnostic.  
  - *Reusable*: clear lineages enable safe reuse and comparison of soil‑driven models.

- **CARE & sovereignty**

  - Soil layers can be used to make claims about Indigenous lands, agriculture, or ecological change.  
  - Combining soil with other layers inappropriately (e.g., ignoring Tribal land context) can cause harm.  
  - Provenance encourages:
    - Honest disclosure of data sources and their limitations.  
    - Respect for local context and knowledge when interpreting soil‑based results.

Governance hooks:

- Any soil standard changes that weaken provenance or obscure SDA vs snapshot distinctions require FAIR+CARE review.  
- Any soil usage that intersects Indigenous territories should be co‑reviewed with sovereignty governance where applicable.

---

## 🕰️ Version History

| Version | Date       | Status            | Summary                                                                                                  |
|--------:|------------|-------------------|----------------------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-27 | Active / Enforced | Upgraded to KFM‑MDP v11.2.2; added telemetry hooks, STAC/DCAT fields, and explicit SDA/gNATSGO provenance models. |
| v11.1.0 | 2025-11-20 | Superseded        | Initial soil‑source comparison standard; established baseline SDA/SSURGO/STATSGO2/gNATSGO guidance.     |

---

<div align="center">

🌱 **Kansas Frontier Matrix — Soil Data Source Comparison & Provenance Standard (v11.2.2)**  
“Soil is slow memory. Provenance keeps it honest.”  

© 2025 Kansas Frontier Matrix — CC‑BY 4.0  

[⬅ Back to Geo Standards](./README.md) · [⚖ Root Governance Charter](../governance/ROOT-GOVERNANCE.md)

</div>
