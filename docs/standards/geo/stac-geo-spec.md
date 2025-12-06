---
title: "🛰️ Kansas Frontier Matrix — STAC Geospatial Metadata Specification (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/standards/geo/stac-geo-spec.md"

version: "v11.0.0"
last_updated: "2025-11-22"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Semiannual · FAIR+CARE Council"
content_stability: "stable"

status: "Active / Enforced"
doc_kind: "Standard"
intent: "stac-geospatial-metadata-specification"
immutability_status: "version-pinned"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256-hash>"

sbom_ref: "../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../releases/v11.0.0/standards-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/standards-stac-geo-v11.json"
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

semantic_document_id: "kfm-stac-geo-spec-v11"
doc_uuid: "urn:kfm:docs:standards:geo:stac-geo-spec:v11"
event_source_id: "ledger:kfm:doc:standards:geo:stac-geo-spec:v11"

scope:
  domain: "stac-geospatial-metadata"
  applies_to:
    - "ingest"
    - "etl"
    - "stac"
    - "dcat"
    - "graph"
    - "hydrology"
    - "terrain"
    - "bathymetry"
    - "archaeology"
    - "climate"
    - "frontend"
    - "story-nodes"
    - "focus-mode"

fair_category: "F1-A1-I1-R1"
care_label: "Public / Medium-Risk"
sensitivity: "General (non-sensitive; catalog metadata)"
sensitivity_level: "Low"
public_exposure_risk: "Low"
classification: "Public (Governed)"
jurisdiction: "Kansas / United States"
indigenous_rights_flag: true
data_steward: "KFM FAIR+CARE Council"

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "TechArticle"
  prov_o: "prov:Plan"
  geosparql: "geo:FeatureCollection"
  owl_time: "TemporalEntity"

metadata_profiles:
  - "STAC 1.0.0"
  - "DCAT 3.0"
  - "PROV-O"
  - "FAIR+CARE"

json_schema_ref: "../../../schemas/json/stac-geo-spec-v11.0.0.schema.json"
shape_schema_ref: "../../../schemas/shacl/stac-geo-spec-v11.0.0-shape.ttl"

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
    - "🧠 Story Node & Focus Mode Integration"
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

# 🛰️ **STAC Geospatial Metadata Specification (v11.0.0)**  
`docs/standards/geo/stac-geo-spec.md`

**Purpose**  
Define the KFM v11‑compliant STAC 1.0 geospatial metadata standard for all raster, vector, DEM, bathymetry, hydrology, archaeological, climate, and temporal–spatial datasets.  
Ensure deterministic metadata, correct CRS/vertical‑axis representation, FAIR+CARE alignment, DCAT 3 compatibility, and PROV‑O lineage integration so that every KFM dataset is catalog‑ready, graph‑ingestable, and Focus‑Mode aware.

</div>

---

## 🗂️ Directory Layout

```text
📂 docs/
└── 📂 standards/
    ├── 📂 geo/
    │   📄 README.md                  # 🌎 Geo Standards Index
    │   📄 stac-geo-spec.md           # 🛰 STAC geospatial metadata spec (this file)
    │   📄 crs-standard.md            # 🗺 CRS standard (v11 legacy baseline)
    │   📄 vertical-axis-and-dod.md   # 📏 Vertical datums & DoD conventions
    │   📄 hydrology-standards.md     # 💧 Hydrology & water-surface (legacy path)
    │   📄 archaeology-sensitive-locations.md  # 🛡 Archaeology & Indigenous overlays (legacy path)
    └── 📂 governance/
        📄 ROOT-GOVERNANCE.md         # ⚖ Root governance charter
```

Author rules:

- This file defines the **STAC geospatial metadata contract**; all domain standards (hydrology, archaeology, etc.) extend it but must not contradict it.  
- Any change to required STAC fields must be reflected here, in the JSON/SHACL schemas, and in CI (`standards-stac-geo` checks).  

---

## 📘 Overview

All KFM v11 dataset metadata **must** be published using **STAC 1.0.0** plus KFM profiles. This standard governs:

- STAC **Catalog**, **Collection**, and **Item** structure.  
- CRS metadata (`proj:*`) in alignment with the CRS/topology standard.  
- Vertical‑axis metadata (`vertical:*`, `kfm:cf_positive`, DoD sign conventions).  
- Hydrology, bathymetry, and DoD semantic fields.  
- Archaeology‑sensitive and sovereignty‑aware masking fields (`heritage:*`, `care:*`).  
- Temporal metadata (`datetime`, `start_datetime`, `end_datetime`, OWL‑Time alignment).  
- Provenance metadata (`kfm:lineage`, PROV bundles).  
- DCAT 3.0 mapping and JSON‑LD compatibility.

Every STAC document in KFM must be:

- **Valid** against STAC + KFM schemas.  
- **Machine‑extractable** for catalogs, graph, and Focus Mode.  
- **CI‑verified** before merge.

---

## 🧭 Context

This specification operates at the intersection of:

- **CRS / Geometry / Topology standards**  
  - `proj:*` fields and geometry representation must match canonical CRS rules.  
- **Vertical Axis & DoD standard**  
  - Vertical metadata (`vertical:*`, `kfm:cf_positive`) must match datum/sign conventions.  
- **Hydrology & Water Surface standards**  
  - Hydrology STAC extensions (`hydro:*`) provide domain‑specific semantics.  
- **Archaeology & Indigenous Sensitive Location standard**  
  - `heritage:*` + `care:*` fields encode sensitivity and sovereignty expectations.  
- **Geo Standards Index & Governance**  
  - This doc is the STAC anchor within the geo standards tree.

In KFM’s pipeline:

> Deterministic ETL → STAC/DCAT/PROV catalogs → Neo4j graph → APIs → MapLibre/Cesium → Story Nodes & Focus Mode

this standard defines **what ETL must emit** and **what downstream systems can rely on**.

---

## 📦 Data & Metadata

### 1. STAC object requirements

KFM v11 uses all three STAC object types:

```text
Catalog → Collections → Items → Assets
```

- IDs must be **lowercase hyphenated** (e.g., `kfm-hydro-arkansas-2020-dem`).  
- Links must be resolvable and stable across deployments (dev/staging/prod environment separation is handled at config level, not IDs).

### 2. STAC Item (mandatory fields)

Every STAC Item **must** include at minimum:

```json
{
  "stac_version": "1.0.0",
  "type": "Feature",
  "id": "<item-id>",
  "bbox": [ ... ],
  "geometry": { ... },
  "properties": {
    "datetime": "YYYY-MM-DDTHH:MM:SSZ",
    "start_datetime": "YYYY-MM-DDTHH:MM:SSZ",
    "end_datetime": "YYYY-MM-DDTHH:MM:SSZ",
    "kfm:cf_positive": "up or down",
    "kfm:processing_level": "L1 or L2 or L3",
    "kfm:domain": "hydrology or terrain or bathymetry or archaeology or climate or vector or other"
  },
  "assets": { },
  "links": [ ]
}
```

Rules:

- `geometry` and `bbox` must be **EPSG:4326 GeoJSON**, consistent with CRS standards.  
- Temporal fields:
  - At least one of `datetime` or `start_datetime` + `end_datetime` must be present.  
  - For time‑varying rasters (hydrology/climate), use intervals plus domain‑specific time metadata.

---

### 3. CRS metadata (`proj:*` fields)

In alignment with the CRS standard, Items must declare:

```json
"proj:epsg": 4326,
"proj:wkt2": "<WKT2>",
"proj:shape": [height, width],
"proj:transform": [a, b, c, d, e, f],
"proj:bbox": [minx, miny, maxx, maxy],
"proj:centroid": { "lat": 38.5, "lon": -98.2 }
```

If the **processing CRS** differs from storage CRS (e.g., EPSG:26914), additional KFM fields may be used:

```json
"kfm:processing_crs": "EPSG:26914"
```

All spatial assets (COGs, vector tiles, etc.) must be consistent with `proj:*` metadata.

---

### 4. Vertical metadata (`vertical:*` fields)

Derived from the Vertical Axis & DoD standard:

```json
"vertical:reference_frame": "NAVD88",
"vertical:geoid_model": "GEOID18",
"vertical:unit": "meter",
"kfm:cf_positive": "up or down",
"kfm:dod_sign": "erosion_negative_deposition_positive"
```

- DEM and water‑surface products must use `kfm:cf_positive = "up"`.  
- Bathymetry and depth‑style products must use `kfm:cf_positive = "down"`.

Example for bathymetry:

```json
{
  "vertical:reference_frame": "NAVD88",
  "vertical:geoid_model": "GEOID18",
  "vertical:unit": "meter",
  "kfm:cf_positive": "down"
}
```

---

### 5. Hydrology STAC extensions

For hydrology datasets (see hydrology standard):

```json
{
  "hydro:type": "streamflow or bathymetry or water_surface or wid or sediment or lake_level",
  "hydro:temporal_resolution": "hourly or daily or subdaily or irregular",
  "hydro:reference_plane": "orthometric",
  "hydro:units": "m",
  "hydro:uncertainty_m": 0.15
}
```

Domain rules:

- `hydro:type` distinguishes between flow, depth, surface, and sediment.  
- `hydro:reference_plane` must be consistent with vertical metadata (e.g., `ORTHOMETRIC_NAVD88` when encoded as a more specific string).

---

### 6. Archaeology & Indigenous sovereignty extensions

For archaeology and culturally sensitive datasets:

```json
{
  "heritage:sensitivity": "L1 or L2 or L3 or L4",
  "heritage:sovereignty": "tribal or state or federal or mixed",
  "heritage:taxonomy": "archaeological or ceremonial or burial or traditional or historic",
  "heritage:masking_method": "h3-generalization or redaction",
  "heritage:h3_index": "8ab4dxxxxxx",
  "care:authority": "Tribal Nation Name",
  "care:consent_required": true
}
```

Rules:

- L3/L4 Items must **not** expose precise point geometries; only H3 polygons (or higher‑level generalized geometry) are allowed.  
- Masking method and H3 resolution must be compatible with the geoprivacy and archaeology standards.

---

### 7. Assets (data objects)

Each asset must include at least:

```json
{
  "href": "https://...",
  "type": "image/tiff; application=geotiff",
  "roles": ["data"],
  "title": "Bathymetry 2018",
  "kfm:checksum_sha256": "<hex>"
}
```

Additional guidance:

- COG assets:
  - Must be tiled with internal overviews.  
  - Must use LZW or ZSTD compression.  
- Vector assets:
  - Should include `type` such as `application/geopackage+sqlite3`, `application/vnd.mapbox-vector-tile`, or `application/geo+json`.

---

## 🌐 STAC, DCAT & PROV Alignment

### 1. STAC ↔ DCAT 3.0 mapping

| STAC field       | DCAT 3.0 term     |
|------------------|-------------------|
| `id`             | `dct:identifier`  |
| `description`    | `dct:description` |
| `keywords`       | `dcat:keyword`    |
| `license`        | `dct:license`     |
| `providers`      | `dct:publisher`   |
| `assets`         | `dcat:Distribution` |
| `links`          | `dcat:distribution` / `dcat:accessURL` |

KFM catalogs must maintain this mapping so external DCAT‑based portals can ingest STAC metadata without loss of meaning.

---

### 2. JSON‑LD, GeoSPARQL, and OWL‑Time

STAC Item JSON documents must be **expandable** into RDF via JSON‑LD contexts, enabling:

- GeoSPARQL geometry integration.  
- OWL‑Time temporal reasoning.  
- PROV‑O lineage modeling.

Minimal context pattern:

```json
"@context": {
  "geo": "http://www.opengis.net/ont/geosparql#",
  "time": "http://www.w3.org/2006/time#",
  "prov": "http://www.w3.org/ns/prov#"
}
```

Geometry must be convertible to GeoSPARQL WKT for use in Neo4j or other triple stores.

---

### 3. PROV‑O lineage (`kfm:lineage`)

All Items must include a lineage block summarizing transformation provenance:

```json
"kfm:lineage": {
  "prov:activity": "crs-transform-v11 or vertical-transform-v11 or hydro-processing-v11",
  "prov:wasGeneratedBy": "gdalwarp-3.8 or ogr2ogr-3.8 or kfm-etl-v11",
  "prov:used": ["source.dem.tif", "source.gpkg"],
  "prov:generatedAtTime": "2025-11-22T14:22:00Z",
  "prov:wasAssociatedWith": "kfm-etl-agent"
}
```

- Detailed PROV bundles may be stored as separate JSON‑LD documents and referenced from Items (e.g., `kfm:prov_ref`).  
- The inline `kfm:lineage` block acts as a summary index for CI, catalogs, and Focus Mode.

---

## 🧱 Architecture

From an architectural perspective, this spec:

1. **Defines the STAC side of the data contract**  
   - ETL pipelines must emit Items/Collections conforming to this spec.  
   - Graph loaders and web services may assume these fields exist and are well‑formed.

2. **Acts as a hub across domain standards**  
   - Hydrology, archaeology, vertical axis, CRS, and geoprivacy standards all attach their domain fields to STAC via specific property names.  
   - Changes in domain semantics must propagate through this spec to remain coherent.

3. **Supports multi‑store catalogs**  
   - STAC JSON as primary representation.  
   - DCAT RDF for open data catalogs.  
   - Neo4j graph nodes for query and reasoning.

Any change to the STAC field set or semantics must:

- Be proposed via PR against this doc.  
- Update JSON/SHACL schemas.  
- Update CI checks and any dependent tooling.

---

## 🧪 Validation & CI/CD

KFM CI enforces STAC metadata rules using `test_profiles` defined in the front‑matter:

- **`markdown-lint`** – structural linting of this documentation.  
- **`schema-lint`** – JSON Schema & SHACL validation of STAC Items and Collections.  
- **`metadata-check`** – presence and format of required `proj:*`, `vertical:*`, `hydro:*`, `heritage:*`, and `kfm:*` fields.  
- **`diagram-check`** – (when diagrams are added) ensures Mermaid blocks are valid.  
- **`accessibility-check`** – names and descriptions for assets, clear metadata.  
- **`provenance-check`** – checks `kfm:lineage` or `kfm:prov_ref` consistency.  
- **`footer-check`** – governance links and version history present in this doc.

**PR blockers** for STAC metadata:

- Missing `proj:*` fields for spatial assets.  
- Missing vertical metadata where elevation/depth is relevant.  
- Geometry not EPSG:4326.  
- Missing `kfm:lineage` / PROV link for derived products.  
- Missing hydrology/archaeology extensions where domain standards indicate they are required.  
- Bathymetry/DoD sign conventions inconsistent with vertical standard.  
- Assets lacking `href`, `type`, or `roles`.  
- Any STAC document failing schema validation.

---

## 🧠 Story Node & Focus Mode Integration

Story Nodes and Focus Mode rely heavily on STAC metadata:

- Story Nodes reference STAC Items/Collections via IDs and spatial/temporal extents.  
- Focus Mode queries STAC catalogs to assemble context for specific map views, times, and domains.

Requirements:

- STAC Items must provide:
  - Reliable `kfm:domain` classification.  
  - Temporal metadata compatible with OWL‑Time (to align with Story Node intervals).  
  - Geospatial metadata suitable for spatial joins (CRS and topology rules).  
- Sensitive or sovereignty‑constrained datasets must expose `heritage:*` and `care:*` fields so Focus Mode can switch to restricted narrative behaviors.

Focus Mode must **never**:

- Assume STAC Items exist without verifying IDs.  
- Override or ignore `heritage:*` and `care:*` metadata.  
- Invent STAC metadata where none exists; it must operate strictly within this spec and the underlying catalogs.

---

## ⚖ FAIR+CARE & Governance

This specification is a key FAIR+CARE mechanism:

- **FAIR**

  - *Findable*: standardized IDs, domains, and lineage fields make datasets searchable.  
  - *Accessible*: STAC + DCAT mapping supports open access and reuse.  
  - *Interoperable*: alignment with STAC 1.0, DCAT 3.0, GeoSPARQL, OWL‑Time, and PROV‑O.  
  - *Reusable*: explicit provenance and domain semantics enable safe reuse across analyses.

- **CARE**

  - *Collective Benefit*: STAC metadata clarifies appropriate use of datasets and their context.  
  - *Authority to Control*: `heritage:*` and `care:*` fields encode Tribal and community governance signals.  
  - *Responsibility*: KFM operators must not strip or minimize sensitive metadata; STAC acts as the carrier of ethical context.  
  - *Ethics*: Mislabeling or omitting sensitivity fields is considered a governance violation.

Any material change to:

- Sensitive metadata fields (`heritage:*`, `care:*`),  
- Hydrology and DoD semantics (`hydro:*`, `kfm:dod_sign`), or  
- Provenance requirements (`kfm:lineage`, `kfm:prov_ref`)

must be reviewed by the FAIR+CARE Council and recorded in this document’s Version History.

---

## 🕰️ Version History

| Version   | Date       | Status            | Notes                                                                                         |
|----------:|------------|-------------------|-----------------------------------------------------------------------------------------------|
| v11.0.0   | 2025-11-22 | Active / Enforced | Initial STAC geospatial metadata standard for KFM v11; aligned with CRS, vertical, hydro, and archaeology standards. |

---

<div align="center">

🛰️ **Kansas Frontier Matrix — STAC Geospatial Metadata Specification (v11.0.0)**  
Interoperable · Deterministic · FAIR+CARE‑Aligned  

[⬅ Back to Geo Standards](./README.md) · [🗺 CRS Standard](./crs-standard.md) · [📐 Vertical Axis & DoD](./vertical-axis-and-dod.md) · [⚖ Governance](../governance/ROOT-GOVERNANCE.md)

</div>
