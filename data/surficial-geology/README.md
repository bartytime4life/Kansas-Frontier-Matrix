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

**Primary Source:** Kansas Geological Survey (KGS), Surficial Geology (Map M-118 lineage)  
**Purpose:**  
Provide clean ingest, deterministic normalization, CRS harmonization, topology repair, H3 indexing, and STAC-publishable GeoParquet for statewide surficial units under KFM v11.2 governance.

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
│   📂 work/                                    — Harmonization, CRS ops, topology fixes
│   📂 outputs/                                 — GeoParquet + tiles + derived unit dictionaries
│   📂 stac/                                    — STAC Collection + Item JSON documents
│   📂 lineage/                                 — PROV-O + JSON-LD lineage outputs
│   📄 README.md                                — This governed ingest hub document
```

---

## 🧬 3. Ingest & Normalization Workflow (v11.2)

### 3.1 Acquire Raw KGS Data  
- Stored 1:1 under `/raw/`  
- SHA256 checksum required  
- Logged in provenance events  

### 3.2 Standardize Schema (Geo Schema v11.2)  
Fields include:  
- `unit_code`  
- `unit_desc`  
- `map_symbol`  
- `color_hex` (derived via DMU-lite table)

### 3.3 CRS Harmonization  
- Convert geometry to **EPSG:5070**  
- Visualization derivatives use **EPSG:4326** or tile-native projections  
- All transforms logged to lineage

### 3.4 Topology QA  
- Validate geometries (`is_valid`)  
- Repair invalid polygons via `buffer(0)`  
- Remove slivers < tolerance  
- Dissolve by `unit_code` to produce stable unit geometries  

### 3.5 H3 Index Assignment  
- Centroid-based indexing at R8–R10  
- CARE screening ensures no sensitive contextual inference is violated  
- Facilitates geoprocessing, clustering, and environmental overlays

### 3.6 GeoParquet Emission  
- Partitioned  
- Metadata-rich  
- Follows **KFM-STAC v11** soil/geology extension rules  
- Includes provenance + QA + telemetry inside Item properties

---

## 🌐 4. STAC Publishing Requirements

### Collection MUST include:
- Source attribution: **Kansas Geological Survey (KGS)**  
- `proj:epsg=5070` for GeoParquet  
- `proj:epsg=4326` for visualization tiles  
- Full PROV-O lineage chain  
- Processing steps + QA  
- Energy/carbon telemetry  

### Items MUST cover:
- Final GeoParquet  
- DMU-lite unit dictionary  
- Optional PMTiles/XYZ tiles  

All Items MUST validate against:

- STAC v1.0.0  
- KFM-STAC v11 Geology Extension  
- geo-surficial-v11 schema  

---

## 🧪 5. Quality & Compliance Requirements

Every release MUST pass:

- **Geometry validity:** ≥ 99.999%  
- **Attribute completeness:** 100% for `unit_code` + `unit_desc`  
- **Lineage:** complete PROV-O chain with timestamps  
- **Telemetry:** energy & carbon logs populated  
- **CARE:** H3 masking rules evaluated (no sensitive cultural inference)

---

## 🤖 6. AI / Focus-Mode Integration

Surficial geology layers provide:

- **Story Node v3 context:**  
  - Terrain–unit interactions  
  - Soil/erosion suitability  
  - Landform evolution cues  

- **Embeddable H3 tiles:**  
  - AI-safe generalizations  
  - Used by Focus Mode to render geology-aware narratives  

- **Environmental affordance layers:**  
  - Inputs to climate, hydrology, hazard narratives  

Focus Mode MUST NOT fabricate geological chronology; all context MUST link to real provenance.

---

## 🧪 7. Example (Reference Only · Not Executed in Pipelines)

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

*(Allowed: single-level fenced code block. Nested fences prohibited.)*

---

## 🧾 8. Provenance & Governance

All transformations MUST produce:

- `lineage/<timestamp>.jsonld` (PROV-O)  
- WAL entries for deterministic replay  
- Energy + carbon telemetry (ISO 14064 alignment)  
- Immutable raw source checksums (`/raw/checksums.txt`)  

Governed by:  
- **FAIR+CARE**  
- **KFM-OP v11**  
- **KGS data-use expectations**  
- **KFM Sovereignty Policy**  

---

## 🕰️ 9. Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| **v11.2.0** | 2025-11-27 | Upgraded to fully compliant KFM-MDP v11.2.2 formatting, added directory layout enhancements, AI governance rules, telemetry schema alignment. |
| **v11.1.0** | 2025-11-26 | Initial v11 ingest hub with CRS/QA/H3/DMU-lite structure. |

---

<div align="center">

**Kansas Frontier Matrix**  
*Scientific Insight × FAIR+CARE Ethics × Sustainable Intelligence*

[⬅ Back to Geo Index](../README.md) ·  
[📜 Governance Charter](../../../docs/standards/governance/ROOT-GOVERNANCE.md) ·  
[🛰 Telemetry Schema](../../../schemas/telemetry/geo-surficial-v11.json)

</div>
