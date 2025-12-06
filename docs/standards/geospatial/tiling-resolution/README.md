---
title: "🧩 KFM v11.2.4 — Tiling Resolution & Zoom-Level Governance Standard"
path: "docs/standards/geospatial/tiling-resolution/README.md"
version: "v11.2.4"
last_updated: "2025-12-06"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · FAIR+CARE Council · Spatial Governance Board"
content_stability: "stable"
backward_compatibility: "v10.x → v11.x tiling-contract compatible"
status: "Active / Enforced"

doc_kind: "Standard"
header_profile: "standard"
footer_profile: "standard"

scope:
  domain: "geospatial-tiling-resolution"
  applies_to:
    - "ingest"
    - "etl"
    - "tiling"
    - "analysis"
    - "stac"
    - "dcat"
    - "graph"
    - "api"
    - "frontend"
    - "story-nodes"
    - "focus-mode"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"
sensitivity: "General (non-sensitive; auto-mask & zoom-governance rules apply)"
sensitivity_level: "None"
public_exposure_risk: "Low"
classification: "Public"
jurisdiction: "Kansas / United States"
indigenous_rights_flag: true
data_steward: "KFM FAIR+CARE Council"

commit_sha: "<latest-commit>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../releases/v11.2.4/sbom.spdx.json"
manifest_ref: "../../../../releases/v11.2.4/manifest.zip"
telemetry_ref: "../../../../releases/v11.2.4/tiling-resolution-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/tiling-resolution/v1.json"
energy_schema: "../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "Apache-2.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.4"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

ttl_policy: "24 months"
sunset_policy: "Supersedes ad-hoc tiling rules in v10.x mapping stack"

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "TechArticle"
  prov_o: "prov:Plan"
  owl_time: "ProperInterval"
  geosparql: "geo:FeatureCollection"

metadata_profiles:
  - "STAC 1.0.0"
  - "DCAT 3.0"
  - "PROV-O"
  - "FAIR+CARE"

provenance_chain:
  - "docs/standards/architecture/map-stack-v10.4.md@v10.4.3"
  - "docs/standards/geospatial/zoom-governance-v11.0.md@v11.0.1"
  - "docs/standards/geospatial/tiling-resolution/README.md@v11.2.0"
  - "docs/standards/geospatial/tiling-resolution/README.md@v11.2.2"

provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: true

json_schema_ref: "schemas/json/tiling-resolution-standard-v11.2.4.schema.json"
shape_schema_ref: "schemas/shacl/tiling-resolution-standard-v11.2.4-shape.ttl"

story_node_refs: []
immutability_status: "version-pinned"

doc_uuid: "urn:kfm:doc:standards:tiling-resolution-v11.2.4"
semantic_document_id: "kfm-doc-tiling-resolution-v11.2.4"
event_source_id: "ledger:kfm:doc:standards:geospatial:tiling-resolution"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summary"
  - "timeline-generation"
  - "semantic-highlighting"
  - "3d-context-render"
  - "a11y-adaptations"
  - "diagram-extraction"
  - "metadata-extraction"
ai_transform_prohibited:
  - "content-alteration"
  - "speculative-additions"
  - "unverified-architectural-claims"
  - "narrative-fabrication"
  - "governance-override"
transform_registry:
  allowed:
    - summary
    - timeline-generation
    - semantic-highlighting
    - 3d-context-render
    - a11y-adaptations
    - diagram-extraction
    - metadata-extraction
  prohibited:
    - content-alteration
    - speculative-additions
    - unverified-architectural-claims
    - narrative-fabrication
    - governance-override

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

heading_registry:
  approved_h2:
    - "🗂️ Directory Layout"
    - "📘 Overview"
    - "🧭 Context"
    - "🧱 Architecture"
    - "🗺️ Diagrams"
    - "📦 Data & Metadata"
    - "🌐 STAC, DCAT & PROV Alignment"
    - "🧪 Validation & CI/CD"
    - "🧠 Story Node & Focus Mode Integration"
    - "⚖ FAIR+CARE & Governance"
    - "🕰️ Version History"

test_profiles:
  - "markdown-lint"
  - "schema-lint"
  - "footer-check"
  - "accessibility-check"
  - "diagram-check"
  - "metadata-check"
  - "provenance-check"

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

layout_profiles:
  - "immediate-one-branch-with-descriptions-and-emojis"

badge_profiles:
  - "root-centered-badge-row"

requires_purpose_block: true
requires_version_history: true
requires_directory_layout_section: true
requires_governance_links_in_footer: true

deprecated_fields:
  - "old_markdown_standard_v10.4"
---

<div align="center">

# 🧩 KFM v11.2.4 — Tiling Resolution & Zoom-Level Governance Standard  
Deterministic Tiles · Geoethically Governed Zoom · STAC/DCAT/PROV-Aligned  

`docs/standards/geospatial/tiling-resolution/README.md`

**Purpose:**  
Define the **only approved tiling resolution and zoom-level governance rules** for the Kansas Frontier Matrix (KFM) mapping stack, covering how raster/vector tiles are generated and served in MapLibre, Cesium, and related frontends. This standard ensures that all tiles are **deterministic**, **geoprivacy-aware**, **FAIR+CARE-aligned**, and fully compatible with KFM’s STAC/DCAT/PROV catalogs, Neo4j graph, and Story Node / Focus Mode layers.

</div>

---

## 🗂️ Directory Layout

~~~text
📂 docs/standards/geospatial/
└── 📂 tiling-resolution/
    ├── 📄 README.md                      # 🧩 This standard: tiling resolution & zoom-level governance
    └── 📄 examples.md                    # 📚 (Optional) Worked examples of zoom policies, Kansas-specific patterns
~~~

Related implementation & data locations (non-exhaustive, for reference):

~~~text
📂 src/
├── 📂 pipelines/
│   └── 📂 tiling/
│       ├── 📄 tiler_config.yaml          # Configs for resolution, zoom ranges, and sources
│       └── 📄 tiler_jobs.py              # Batch/stream tiling jobs (COGs, vector layers)
├── 📂 api/
│   └── 📂 tiles/
│       ├── 📄 router.py                  # Tile endpoints, zoom validation, layer contracts
│       └── 📄 auth_policies.py           # Access control for sensitive/sacred zooms
└── 📂 web/
    └── 📂 map/
        ├── 📄 map_config.ts              # Default zoom ranges, layer definitions
        └── 📄 legends.tsx                # Legends with resolution / sensitivity hints
~~~

Author rules:

- Any new tiling-related standard or example under `docs/standards/geospatial/tiling-resolution/` must be referenced in this tree.  
- Tiling configuration files (`tiler_config.yaml`, etc.) must document which clauses of this standard they implement (e.g., section references in comments).  

---

## 📘 Overview

KFM uses multi-scale tiling (raster + vector) to render Kansas-linked data in MapLibre, Cesium, and derived interfaces. Without a governed standard, zoom-level decisions risk:

- Over-exposing sensitive/sacred patterns at high zoom.  
- Hiding important regional patterns at low zoom.  
- Producing inconsistent detail across layers and deployments.  

This standard:

1. Defines the **canonical zoom scale bands** for KFM (regional → landscape → parcel-ish → building-ish).  
2. Specifies **max and min zoom** per layer category (base, analytic, sensitive, sacred).  
3. Binds tiling behavior to **geoprivacy masking** and sovereignty rules.  
4. Aligns **tile contracts** with STAC/DCAT metadata and Neo4j graph semantics.  
5. Provides constraints for Story Nodes and Focus Mode so narrative overlays never exceed approved resolution.

All KFM tilers, APIs, and frontends **must conform** to this document. Ad-hoc per-project zoom logic is forbidden unless explicitly approved as an exception.

---

## 🧭 Context

KFM’s operational pipeline:

> Deterministic ETL → STAC/DCAT/PROV catalogs → Neo4j knowledge graph → API layer → React/MapLibre/Cesium frontend → Story Nodes → Focus Mode

Within this pipeline:

- **ETL**:
  - Produces tiled inputs (COGs, vector layers) at one or more base resolutions.  
  - Applies geoprivacy masking **before** any tiling of sensitive data.  

- **Tiling**:
  - Converts masked/generalized layers into tile pyramids following this standard.  
  - Registers resulting tiling schemes in STAC Collections/Items and internal schema.  

- **APIs**:
  - Enforce zoom constraints and access control (e.g., disallow sacred tiles at z≥N).  

- **Frontend**:
  - Uses standard zoom bands for default view, max zoom, and “jump to” behaviors.  

- **Story Nodes & Focus Mode**:
  - Respect zoom ceilings for sensitive/sacred content.  
  - Align narrative detail with authorized spatial resolution.

This standard is tightly coupled to:

- 🛡 `docs/standards/geospatial/geoprivacy-masking/README.md`  
- Catalog standards (STAC/DCAT profiles) and PROV-O provenance design  
- Map stack architecture docs (not shown here, but referenced by `pipeline_contract_version`)

---

## 🧱 Architecture

### 1. Canonical zoom bands

KFM defines **semantic zoom bands** to avoid per-layer improvisation:

| Band ID | Approx. Zoom Range | Typical Use                            | Notes                                |
|--------:|--------------------|----------------------------------------|--------------------------------------|
| B0      | z 4–6              | Continental / national context         | Kansas outline, neighboring states   |
| B1      | z 7–9              | State / multi-county overview          | Statewide themes, major basins       |
| B2      | z 10–11            | County / sub-basin                     | County-level stats, landcover        |
| B3      | z 12–13            | Township / neighborhood / corridor     | Detailed land use, infrastructure    |
| B4      | z 14–16            | Parcel-ish / site (open data only)     | Public points, buildings, streets    |
| B5      | z ≥17              | Building-sublevel (KFM: **forbidden**) | Disallowed except internal debugging |

**Normative rules:**

- **B5 (z≥17)** is reserved for **internal debugging only** and must never be exposed in public deployments.  
- **Sacred/sensitive** layers may not be served beyond B2–B3 (policy details below).  
- Base maps can optionally extend to B4, but internal details must respect licensing and attribution constraints.

### 2. Layer categories and zoom limits

KFM classifies layers into four tiling categories:

1. `base` — basemap imagery, terrain, reference.  
2. `analytic-open` — analytic layers derived from open data.  
3. `analytic-sensitive` — analytic layers with latent privacy risk.  
4. `sensitive/sacred` — layers governed by geoprivacy/sovereignty rules.

**Normative zoom table (public deployments):**

| Category            | Min Zoom | Max Zoom | Notes                                                                 |
|---------------------|---------:|---------:|-----------------------------------------------------------------------|
| base                | 4        | 16       | Terrain, reference layers; must respect source licenses.             |
| analytic-open       | 7        | 15       | Open layers; parcel-ish detail allowed where data supports it.       |
| analytic-sensitive  | 8        | 12       | High-res detail suppressed; focus on county/regional patterns.       |
| sensitive/sacred    | 8        | 10       | Only generalized regions (no points); zoom-gated per sovereignty.    |

These categories must be recorded in layer configuration and referenced in STAC/DCAT as `kfm:tiling_category`.

### 3. Interaction with geoprivacy masking

For any layer with `kfm:sensitivity_label`:

- `public` or `community`:
  - Masked points may be tiled up to B4 (z≤16), subject to general privacy rules.  

- `sensitive`:
  - Masked points may be tiled internally, but public-facing tiles **must not** exceed B3 (z≤13).  
  - At B2 and below, aggregations or density surfaces are preferred.  

- `sacred`:
  - Sacred geometries must never appear as points in tiles.  
  - Only generalized regions (H3 cells, coarse polygons) may be tiled, and only up to B2 (z≤11).  
  - At B1 and below, sacred presence should be signaled only where governance approves.

These rules must be consistent with the Geoprivacy Masking Standard and its CI scenarios.

### 4. Tiling matrix and projection

KFM standardizes on:

- A Web Mercator compatible tile matrix (XYZ) for web maps.  
- EPSG:3857 or equivalent as the display CRS, with canonical tile bounds for Kansas-centric tiles.  

Internally, KFM may maintain EPSG:4326/GeoJSON geometries, but:

- Tiling must be deterministic across environments.  
- Tile coordinate to zoom mapping must match MapLibre/Cesium expectations.

---

## 🗺️ Diagrams

### 1. Zoom band overview

~~~mermaid
flowchart LR
    Z4[Z4-6\nB0\nContinental/National] --> Z7[Z7-9\nB1\nState/Multi-County]
    Z7 --> Z10[Z10-11\nB2\nCounty/Sub-basin]
    Z10 --> Z12[Z12-13\nB3\nCorridor/Neighborhood]
    Z12 --> Z14[Z14-16\nB4\nParcel-ish (Open Only)]
    Z14 -. forbidden .-> Z17[Z17+\nB5\nDebug Only]

    class Z17 forbidden;
~~~

*(Styling is conceptual; actual rendering depends on Mermaid theme.)*

### 2. Layer category vs band matrix

~~~mermaid
flowchart TB
    A[Layer Category] --> B0[B0 (z4-6)]
    A --> B1[B1 (z7-9)]
    A --> B2[B2 (z10-11)]
    A --> B3[B3 (z12-13)]
    A --> B4[B4 (z14-16)]

    subgraph Base
      B0 -->|allowed| B1
      B1 -->|allowed| B2
      B2 -->|allowed| B3
      B3 -->|allowed| B4
    end
~~~

Diagrams are illustrative; the normative rules are in the text and tables.

---

## 📦 Data & Metadata

### 1. Required tiling-related metadata

Each STAC Item/Collection and internal layer config participating in tiling must include:

- `kfm:tiling_category` — one of:
  - `base`, `analytic-open`, `analytic-sensitive`, `sensitive`, `sacred`.  
- `kfm:min_zoom` — integer.  
- `kfm:max_zoom` — integer.  
- `kfm:zoom_band_min` / `kfm:zoom_band_max` — semantic bands (e.g., `B1`, `B3`).  
- `kfm:tiling_profile` — profile identifier (e.g., `kfm-xyz-v1`).  
- `kfm:tiling_crs` — CRS used for tiling (e.g., `EPSG:3857`).  

For sensitive/sacred layers, also:

- `kfm:sensitivity_label` (from geoprivacy standard).  
- `kfm:access_label` (data-access labels standard).  
- `kfm:geoethics_profile` / `kfm:sovereignty_label` as applicable.

### 2. Example metadata snippet

~~~json
{
  "kfm:tiling_category": "analytic-sensitive",
  "kfm:min_zoom": 8,
  "kfm:max_zoom": 12,
  "kfm:zoom_band_min": "B1",
  "kfm:zoom_band_max": "B3",
  "kfm:tiling_profile": "kfm-xyz-v1",
  "kfm:tiling_crs": "EPSG:3857",
  "kfm:sensitivity_label": "sensitive",
  "kfm:access_label": "restricted"
}
~~~

---

## 🌐 STAC, DCAT & PROV Alignment

### STAC

- Collections representing tiled layers must specify:
  - Tiling-specific extensions or `kfm:*` metadata described above.  
  - Links to tile endpoints (e.g., XYZ template URLs).  

- Items may carry:
  - per-asset zoom hints,  
  - or reference a shared Collection-level tiling profile.

### DCAT

- DCAT datasets representing tiled resources should:
  - Use `dcat:Distribution` to describe tile services.  
  - Include `kfm:min_zoom`, `kfm:max_zoom`, and `kfm:tiling_profile` in an extension.  
  - Reference this standard via `dct:conformsTo`.

### PROV

Tiling processes are modeled as:

- `prov:Activity` — tile generation jobs (per layer, per zoom set).  
- `prov:Entity` — resulting tile pyramids or tile services.  
- `prov:used` — masked/base layers, configuration documents.  
- `prov:wasGeneratedBy` — link from tile services to tiling jobs.

Provenance for tiling must be consistent with ETL and geoprivacy provenance; tiling is not allowed to “strip away” sensitivity or sovereignty information.

---

## 🧪 Validation & CI/CD

KFM CI must enforce tiling rules using:

- Configuration validation.  
- API contract tests.  
- Frontend integration tests.

Minimum checks:

1. **Config schema validation**  
   - `tiler_config.yaml` validated against `tiling-resolution-standard-v11.2.4.schema.json`.  

2. **Zoom range enforcement**  
   - Tests ensure each layer’s configured `min_zoom`/`max_zoom` is within this standard’s allowed band for its category.  

3. **API-level max zoom**  
   - API tests confirm tile endpoints reject requests with:
     - Zoom > configured `max_zoom`.  
     - Zoom outside allowed ranges for sensitive/sacred layers.  

4. **Frontend compliance**  
   - MapLibre/Cesium configuration tested to ensure:
     - UI cannot request disallowed zooms for sensitive/sacred layers.  
     - Default map initialization uses B1/B2 for statewide views.

Failures in these checks must block merges affecting tiling code or configs.

---

## 🧠 Story Node & Focus Mode Integration

Story Nodes and Focus Mode must respect tiling resolution:

- Story Nodes that reference spatial content must:
  - Include an implicit or explicit scale (e.g., “statewide”, “county-level”, “site-level”).  
  - Never encourage zooming beyond allowed `max_zoom` for a layer.  

- Focus Mode:
  - May display “you are at the maximum allowed zoom for this layer” hints.  
  - Should compute summaries consistent with the band in use (e.g., statewide stats at B1).

When generating narratives, AI-based systems should:

- Prefer band-aware language (“at neighborhood scale”, “across Kansas”), not arbitrary zoom numbers.  
- Avoid describing detail finer than maps actually expose for sensitive/sacred layers.

---

## ⚖ FAIR+CARE & Governance

This tiling standard supports FAIR+CARE and sovereignty by:

- **FAIR**
  - *Findable*: standard zoom bands and `kfm:*` tiling metadata make it easy to discover usable resolutions.  
  - *Accessible*: consistent tiling contracts simplify client code and tooling.  
  - *Interoperable*: alignment with STAC/DCAT/PROV allows external tools to interpret KFM tiling semantics.  
  - *Reusable*: downstream analysis can rely on predictable scale and resolution.

- **CARE & sovereignty**
  - Ensures sacred/sensitive data is not exposed at inappropriate spatial resolution.  
  - Binds zoom behavior to geoprivacy and sovereignty policies, not UI convenience.  
  - Facilitates review by FAIR+CARE Council and Tribal Sovereignty Board through clear, auditable rules.

Governance expectations:

- Any change to zoom bands or layer category rules is a **governance change** and must:
  - Update this standard.  
  - Update affected configs, schemas, and CI checks.  
  - Document impacts on geoprivacy and sovereignty.

---

## 🕰️ Version History

| Version    | Date       | Status            | Notes                                                                                                  |
|-----------:|------------|-------------------|--------------------------------------------------------------------------------------------------------|
| **v11.2.4** | 2025-12-06 | Active / Enforced | Current standard; defines canonical zoom bands, layer categories, and geoprivacy-aware zoom ceilings. |
| v11.2.2    | 2025-11-28 | Superseded        | Introduced band vocabulary (B0–B4) and initial layer-category mapping (no sacred rules).              |
| v11.2.0    | 2025-11-22 | Superseded        | First v11 tiling governance draft; basic min/max zoom guidance for open vs sensitive layers.          |
| v11.0.1    | 2025-11-15 | Superseded        | Legacy v11 map-stack zoom defaults; lacked explicit band semantics and FAIR+CARE integration.         |
| v10.4.3    | 2023-10-10 | Legacy            | Pre-KFM tiling rules, ad-hoc per project; no formal bands or sovereignty integration.                 |

---

<div align="center">

🧩 **KFM v11.2.4 — Tiling Resolution & Zoom-Level Governance Standard**  
Deterministic Tiles · Geoethical Zoom · FAIR+CARE Sovereignty  

[📘 Docs Root](../../../..) · [📂 Geospatial Standards](../README.md) · [🛡 Geoprivacy Masking](../geoprivacy-masking/README.md) · [⚖ Governance](../../governance/ROOT-GOVERNANCE.md)

</div>

