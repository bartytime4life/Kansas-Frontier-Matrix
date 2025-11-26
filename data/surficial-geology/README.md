---
title: "🪨 Kansas Frontier Matrix — Surficial Geology (KGS M-118 Lineage) · Ingest & Processing Hub (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "data/geo/surficial-geology/README.md"
version: "v11.2.0"
last_updated: "2025-11-27"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Semiannual · Geo Working Group · FAIR+CARE Council Oversight"
content_stability: "stable"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../releases/v11.2.0/sbom.spdx.json"
manifest_ref: "../../../releases/v11.2.0/manifest.zip"
telemetry_ref: "../../../releases/v11.2.0/geo-surficial-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/geo-surficial-v11.json"
energy_schema: "../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "Open Data (KGS Source) + MIT for derived artifacts"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"

status: "Active / Enforced"
doc_kind: "Dataset · Ingest Hub"
intent: "surficial-geology-ingest"
category: "Geology · GIS · Geospatial · Environmental Data"

fair_category: "F1-A1-I1-R1"
care_label: "Respectful · Minimally Intrusive · Community Aligned"
sensitivity_level: "Low"
public_exposure_risk: "Low"
indigenous_rights_flag: true
data_steward: "KFM FAIR+CARE Council"

sensitivity: "General (non-sensitive), but CARE screening applies to contextual relationships"
risk_category: "Low"
redaction_required: false

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "Dataset"
  owl_time: "ProperInterval"
  prov_o: "prov:Plan"
  geosparql: "geo:FeatureCollection"

metadata_profiles:
  - "STAC 1.0.0"
  - "DCAT 3.0"
  - "PROV-O"
  - "FAIR+CARE"

provenance_chain:
  - "data/geo/surficial-geology/README.md@v11.1.0"
  - "KGS Surficial Geology — Map M-118"
  - "USGS Elevation / Hydrology Cross-Checks"
  - "KFM Geo Harmonization v11 pipelines"
provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: false

json_schema_ref: "../../../schemas/json/geo-surficial-v11.schema.json"
shape_schema_ref: "../../../schemas/shacl/geo-surficial-v11-shape.ttl"

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
    - "summary"
    - "semantic-highlighting"
    - "diagram-extraction"
    - "metadata-extraction"
  prohibited:
    - "content-alteration"
    - "unverified-architectural-claims"

layout_profiles:
  - "immediate-one-branch-with-descriptions-and-emojis"
badge_profiles:
  - "root-centered-badge-row"
requires_purpose_block: true
requires_version_history: true
requires_directory_layout_section: true
requires_governance_links_in_footer: true

doc_uuid: "urn:kfm:doc:dataset:surficial-geology:v11.2.0"
semantic_document_id: "kfm-surficial-geology"
event_source_id: "ledger:data/geo/surficial-geology/README.md"
immutability_status: "version-pinned"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

jurisdiction: "Kansas / United States"
classification: "Public"
lifecycle_stage: "stable"
ttl_policy: "Review required every 12 months"
sunset_policy: "Superseded by surficial-geology-v12"
---

<div align="center">

# 🪨 **Surficial Geology of Kansas — Ingest, Harmonization & STAC Publishing Hub**  
`data/geo/surficial-geology/`

[![Geo Data](https://img.shields.io/badge/Domain-Geology%20%2F%20GIS-795548)]()
[![STAC](https://img.shields.io/badge/STAC-v1.0.0-4caf50)]()
[![Lineage](https://img.shields.io/badge/OpenLineage-v2.5-9c27b0)]()
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Compliant-gold)]()
[![License](https://img.shields.io/badge/License-KGS%20Open%20Data%20%2B%20MIT-blue)]()

**Primary Source:** Kansas Geological Survey (KGS), Surficial Geology (Map M-118 lineage)  

**Purpose:**  
Provide clean ingest, deterministic normalization, CRS harmonization, topology repair, H3 indexing, and STAC-ready GeoParquet for statewide surficial units under KFM v11.2 governance and FAIR+CARE oversight.

</div>

---

## 📘 1. Scope & Responsibilities (v11.2)

This directory is the **canonical ingest + harmonization hub** for surficial geology datasets (KGS Map M-118 lineage).  
It supports:

- Download & checksum-verify raw KGS layers  
- Normalize attributes (`unit_code`, `unit_desc`, `map_symbol`, `color_hex`)  
- CRS harmonization to **EPSG:5070** (analysis) and **EPSG:4326** (visualization)  
- Unit dictionary generation (DMU-lite, GeMS-aligned)  
- QA operations: geometry validity, sliver detection, dissolve-by-unit  
- CARE-compliant H3 tagging (R8–R10)  
- STAC Collection + Item generation  
- PROV-O lineage + OpenLineage event emission  
- Telemetry export (energy, carbon, QA metrics)  
- Zero modification of raw KGS distributions (immutability guaranteed)

---

## 🗂️ 2. Directory Layout (v11.2 · Immediate + One Branch · Emojis + Descriptions)

```text
📁 data/geo/surficial-geology/                  — Surficial geology ingest & processing root
│   📂 raw/                                     — Raw KGS GIS inputs (immutable, checksum-verified)
│   📂 work/                                    — Harmonization, CRS ops, topology fixes, H3 prep
│   📂 outputs/                                 — GeoParquet + tiles + derived unit dictionaries
│   📂 stac/                                    — STAC Collection + Item JSON documents
│   📂 lineage/                                 — PROV-O + JSON-LD lineage outputs
│   📄 README.md                                — This governed ingest hub document
```

---

## 🧬 3. Ingest & Normalization Workflow (v11.2)

### 3.1 Acquire Raw KGS Data  
- Stored 1:1 under `/raw/`.  
- SHA256 checksum required; stored in a checksum manifest.  
- Logged via provenance events and OpenLineage.

### 3.2 Standardize Schema (Geo Schema v11.2)  
Fields include:  
- `unit_code`  
- `unit_desc`  
- `map_symbol`  
- `color_hex` (from DMU-lite color tables)

### 3.3 CRS Harmonization  
- Convert all geometries to **EPSG:5070** for analysis.  
- Derive visualization derivatives in **EPSG:4326** or tiling-native CRSs.  
- Document all transforms in lineage metadata.

### 3.4 Topology QA  
- Validate geometries (`is_valid`).  
- Repair invalid polygons via `buffer(0)` or equivalent.  
- Remove slivers below a configured tolerance.  
- Dissolve by `unit_code` to build stable unit geometries.

### 3.5 H3 Index Assignment  
- Compute centroids and assign H3 indices at R8–R10.  
- CARE-controlled: ensure no inference about sensitive cultural or sacred contexts is possible via unit/H3 overlays.  
- Used for spatial filtering, clustering, and cross-domain overlays.

### 3.6 GeoParquet Emission  
- Emit partitioned, metadata-rich GeoParquet files.  
- Embed references to STAC Items, CRS, and source lineage.  
- Comply with KFM-STAC v11 geologic extension conventions.

---

## 🌐 4. STAC Publishing Requirements

### 4.1 STAC Collection MUST Include

- Source attribution: **Kansas Geological Survey (KGS)**.  
- `proj:epsg=5070` for analysis assets (GeoParquet).  
- `proj:epsg=4326` for visualization tiles (if produced).  
- Complete lineage chain (link to `lineage/*.jsonld`).  
- QA metrics (geometry validity, sliver removal counts).  
- Telemetry summary (energy, carbon, run metadata).

### 4.2 STAC Items MUST Cover

- Final GeoParquet dataset.  
- DMU-lite unit dictionary.  
- Optional PMTiles/XYZ tiles (if generated).  

All Items MUST validate against:

- STAC v1.0.0.  
- KFM-STAC v11 Geology Extension.  
- `geo-surficial-v11` JSON schema.

---

## 🧪 5. Quality & Compliance Requirements

Each governed release MUST achieve:

- **Geometry validity:** ≥ 99.999% of polygons valid.  
- **Attribute completeness:** 100% for `unit_code` + `unit_desc`.  
- **Lineage coverage:** full PROV-O chain covering ingest → harmonization → QA → output.  
- **Telemetry:** energy & carbon logs populated and schema-valid.  
- **CARE compliance:** H3 usage reviewed and approved by FAIR+CARE governance guidelines.

---

## 🤖 6. AI / Focus-Mode Integration

Surficial geology provides key **context layers** for:

- Terrain–unit narratives (e.g., loess vs bedrock exposures).  
- Hazard and erosion risk overlays.  
- Ecological suitability narratives (in combination with soils, climate, and hydrology).  

Focus Mode v3:

- MAY surface this dataset as **supporting context** when explaining landforms and surficial processes.  
- MUST NOT fabricate geological sequences; all descriptions MUST link back to real units and provenance.  
- MAY consume H3/GeoParquet derivatives as input for map overlays and narrative highlight regions.

---

## 🧪 7. Example (Reference Only · Not the Production Pipeline)

```python
import geopandas as gpd
import h3

g = gpd.read_file("kgs_surficial.gpkg").rename(columns={
    "UNIT_CODE": "unit_code",
    "UNIT_DESC": "unit_desc",
    "MAP_SYMBOL": "map_symbol"
})

g = g.to_crs(5070)
g["h3_9"] = g.centroid.apply(lambda c: h3.geo_to_h3(c.y, c.x, 9))

g.to_parquet("outputs/geoparquet/surficial.parquet", index=False)
```

> This example demonstrates the shape of the workflow.  
> The production implementation uses KFM’s Reliable Pipelines v11, lakeFS, and OpenLineage for controlled runs.

---

## 🧾 8. Provenance & Governance

All transformations MUST produce:

- `lineage/<timestamp>.jsonld` (PROV-O) capturing activities, entities, and agents.  
- WAL entries suitable for deterministic replay under Reliable Pipelines v11.  
- Energy + carbon telemetry aligned with ISO 14064-1.  
- Immutable raw source checksums in `/raw/`.

Governance:

- FAIR+CARE-aligned (no misuse of geology to infer sensitive cultural data).  
- Sovereignty and heritage policies apply when geology is combined with sensitive cultural datasets.  
- All governance decisions regarding masking/generalization recorded in lineage.

---

## 🕰️ 9. Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| **v11.2.0** | 2025-11-27 | Upgraded to KFM-MDP v11.2.2, added badges, v11 directory layout, telemetry & governance integration refinements. |
| **v11.1.0** | 2025-11-26 | Initial KFM v11 uplift, new CRS/QA/H3/DMU-lite structure. |

---

<div align="center">

**Kansas Frontier Matrix**  
*Scientific Insight × FAIR+CARE Ethics × Sustainable Intelligence*

[⬅ Back to Geo Index](../README.md) ·  
[🏗 Repository Architecture](../../../ARCHITECTURE.md) ·  
[⚖ Governance Charter](../../../docs/standards/governance/ROOT-GOVERNANCE.md) ·  
[🛰 Telemetry Schema](../../../schemas/telemetry/geo-surficial-v11.json)

</div>
