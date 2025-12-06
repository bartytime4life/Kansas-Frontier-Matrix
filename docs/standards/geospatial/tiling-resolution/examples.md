---
title: "🧩 KFM Tiling Resolution — Worked Examples & Zoom Profiles"
path: "docs/standards/geospatial/tiling-resolution/examples.md"
version: "v11.2.4"
last_updated: "2025-12-06"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · FAIR+CARE Council · Spatial Governance Board"
content_stability: "stable"
backward_compatibility: "v10.x → v11.x tiling-contract compatible"
status: "Active / Enforced"

doc_kind: "Guide"
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
sunset_policy: "Aligned with tiling-resolution standard v11.2.4"

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
  - "docs/standards/geospatial/tiling-resolution/README.md@v11.2.4"
  - "docs/standards/geospatial/geoprivacy-masking/README.md@v11.2.4"

provenance_requirements:
  versions_required: false
  newest_first: true
  must_reference_superseded: false
  must_reference_origin_root: true

json_schema_ref: "schemas/json/tiling-resolution-examples-v11.2.4.schema.json"
shape_schema_ref: "schemas/shacl/tiling-resolution-examples-v11.2.4-shape.ttl"

story_node_refs: []
immutability_status: "version-pinned"

doc_uuid: "urn:kfm:doc:standards:tiling-resolution-examples-v11.2.4"
semantic_document_id: "kfm-doc-tiling-resolution-examples-v11.2.4"
event_source_id: "ledger:kfm:doc:standards:geospatial:tiling-resolution:examples"

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
    - "🧪 Validation & CI/CD"
    - "📦 Data & Metadata"
    - "🌐 STAC, DCAT & PROV Alignment"
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

# 🧩 KFM Tiling Resolution — Worked Examples & Zoom Profiles  
v11.2.4 · Kansas-Focused Recipes · Zoom-Band Contracts  

`docs/standards/geospatial/tiling-resolution/examples.md`

**Purpose:**  
Provide **concrete, copy-pasteable examples** of KFM tiling configuration, zoom-band usage, and Kansas-focused layer designs that implement the normative rules in the Tiling Resolution & Zoom-Level Governance Standard. These examples are **non-normative**, but every example must remain compliant with the standard and with geoprivacy/sovereignty rules.

</div>

---

## 🗂️ Directory Layout

~~~text
📂 docs/standards/geospatial/tiling-resolution/
├── 📄 README.md               # 🧩 Normative tiling resolution & zoom governance standard
└── 📄 examples.md             # 📚 This guide: worked examples & profiles
~~~

Recommended related test/config locations (for reference):

~~~text
📂 src/pipelines/tiling/
├── 📄 tiler_config.yaml             # Main tiler config (imports examples as profiles)
└── 📄 tiler_jobs.py                 # Jobs implementing standard-compliant tiling

📂 tests/geospatial/
└── 📄 test_tiling_profiles.py       # CI tests that instantiate these examples

📂 schemas/json/
└── 📄 tiling-resolution-examples-v11.2.4.schema.json
~~~

Author rules:

- Examples in this file must:
  - Point back to the standard (`README.md`) instead of redefining rules.  
  - Use band IDs (`B0`–`B4`) and categories (`base`, `analytic-open`, `analytic-sensitive`, `sensitive`, `sacred`).  
  - Be safe to use as starting points in `tiler_config.yaml` with minimal edits (paths, IDs).  

---

## 📘 Overview

This guide offers **three main kinds of examples**:

1. **Basemap & open analytic profiles**  
   - Kansas basemap, elevation, hydrology context.  
2. **Sensitive analytic profiles**  
   - County-level patterns without parcel-level exposure.  
3. **Sacred & sovereignty-aware overlays**  
   - Generalized, zoom-gated Kansas regions using geoprivacy masking outputs.

Each example includes:

- A **YAML fragment** suitable for `tiler_config.yaml`.  
- Suggested **STAC/DCAT metadata** fields.  
- Optional **test snippets** for CI.

These examples are meant to be cloned/adapted with:

- `layer_id` renamed for the consuming project.  
- Data `source_uri` adjusted to local KFM STAC catalogs or COG/vector sources.

---

## 🧭 Context

Recall from the standard:

- Zoom bands:

  - `B0` = z4–6 (continental/national)  
  - `B1` = z7–9 (state/multi-county)  
  - `B2` = z10–11 (county/sub-basin)  
  - `B3` = z12–13 (corridor/neighborhood)  
  - `B4` = z14–16 (parcel-ish / site; open data only)  

- Layer categories:

  - `base`, `analytic-open`, `analytic-sensitive`, `sensitive`, `sacred`.  

These examples apply those bands and categories to **plausible, synthetic Kansas layers**, such as:

- State basemap for Kansas Frontier Matrix.  
- County-level crop/landcover patterns.  
- Sacred-region overlay derived from geoprivacy-masked inputs.

---

## 🧱 Architecture

### Example 1 — Kansas basemap profile (`base` category)

**Goal:** A statewide basemap for KFM maps, with generous zoom range but still respecting B5 prohibition (no public z≥17).

**Tiler profile (YAML fragment):**

~~~yaml
profiles:
  - id: "kansas_basemap_v1"
    category: "base"
    description: "Kansas basemap: terrain + administrative + roads (reference only)"
    source_uri: "stac://collections/kfm-basemap/items/kansas-basemap-v1"
    tiling_profile: "kfm-xyz-v1"
    crs: "EPSG:3857"
    min_zoom: 4      # B0
    max_zoom: 16     # B4 (B5 forbidden)
    zoom_band_min: "B0"
    zoom_band_max: "B4"
    attribution: "© Contributors · See STAC collection for licenses"
    sensitivity_label: "public"
    access_label: "open"
~~~

**Notes:**

- `max_zoom: 16` keeps tiles below the forbidden B5.  
- No geoprivacy masking required; basemap derived from open/ref data.  

**Suggested STAC properties:**

~~~json
{
  "kfm:tiling_category": "base",
  "kfm:min_zoom": 4,
  "kfm:max_zoom": 16,
  "kfm:zoom_band_min": "B0",
  "kfm:zoom_band_max": "B4",
  "kfm:tiling_profile": "kfm-xyz-v1",
  "kfm:tiling_crs": "EPSG:3857",
  "kfm:sensitivity_label": "public",
  "kfm:access_label": "open"
}
~~~

---

### Example 2 — County-level landcover (`analytic-open`)

**Goal:** Provide **open** landcover at county-to-township scales without over-emphasizing parcel detail.

**Tiler profile:**

~~~yaml
profiles:
  - id: "kansas_landcover_county_v1"
    category: "analytic-open"
    description: "Kansas landcover aggregated to county/township scale"
    source_uri: "stac://collections/kfm-landcover/items/kansas_landcover_v1"
    tiling_profile: "kfm-xyz-v1"
    crs: "EPSG:3857"
    min_zoom: 7      # B1 (state / multi-county)
    max_zoom: 13     # Up to B3 (corridor/township)
    zoom_band_min: "B1"
    zoom_band_max: "B3"
    sensitivity_label: "public"
    access_label: "open"
    rendering:
      style: "choropleth"
      legend_id: "landcover_simple"
~~~

**Reasoning:**

- At B1–B3, users see meaningful patterns without pseudo-parcel detail.  
- Because data is open and not individually identifying, B4 is **optional**; here we cap at B3 for performance and clarity.

---

### Example 3 — Sensitive analytic layer (e.g., soil vulnerability)

**Goal:** Show **county-level patterns** of soil vulnerability without site-level exposure.

**Tiler profile:**

~~~yaml
profiles:
  - id: "kansas_soil_vulnerability_v1"
    category: "analytic-sensitive"
    description: "Soil vulnerability index aggregated to county or HUC-10 basins"
    source_uri: "stac://collections/kfm-soils/items/soil_vulnerability_v1"
    tiling_profile: "kfm-xyz-v1"
    crs: "EPSG:3857"
    min_zoom: 8      # B1/B2 boundary
    max_zoom: 12     # Up to lower B3 only
    zoom_band_min: "B1"
    zoom_band_max: "B3"
    sensitivity_label: "sensitive"
    access_label: "restricted"
    aggregation:
      method: "mean"
      unit: "index_0_1"
      geometry_unit: "county"
~~~

**Constraints:**

- Zoom range matches **analytic-sensitive** rules from the standard.  
- The underlying data may be high resolution, but tiles should show **only aggregated cells/polygons**, not raw survey points.

---

### Example 4 — Sacred-region overlay (`sacred` + geoprivacy)

**Goal:** Display sacred-related regions as **generalized H3 or polygons**, following sovereign governance and geoprivacy masking rules.

**Tiler profile:**

~~~yaml
profiles:
  - id: "kansas_sacred_regions_v1"
    category: "sacred"
    description: "Generalized sacred-region overlay (H3-based), geoprivacy- and sovereignty-governed"
    source_uri: "stac://collections/kfm-sacred/items/sacred_regions_h3_v1"
    tiling_profile: "kfm-xyz-v1"
    crs: "EPSG:3857"
    min_zoom: 8       # B1/B2
    max_zoom: 10      # B2 only (county/sub-basin scale)
    zoom_band_min: "B1"
    zoom_band_max: "B2"
    sensitivity_label: "sacred"
    access_label: "tribal-only"
    sovereignty_label: "example-tribal-partner"
    geoprivacy_profile: "donut_geomask_v1 + H3_R8"
    frontend_rules:
      hide_above_zoom: 10   # strictly enforced in API as well
      show_legend_notice: true
~~~

**Key points:**

- No point geometries are tiled; only generalized shapes.  
- `max_zoom: 10` reflects the **B2** ceiling for sacred content.  
- Frontend rules mirror API constraints.

---

### Example 5 — Parcel-ish public POIs (`analytic-open` @ B4)

**Goal:** Enable public “points of interest” in towns, aligned with parcel-ish zooms, but only for **public** data.

**Tiler profile:**

~~~yaml
profiles:
  - id: "kansas_public_poi_v1"
    category: "analytic-open"
    description: "Public points of interest (e.g., libraries, museums, parks)"
    source_uri: "stac://collections/kfm-poi/items/public_poi_v1"
    tiling_profile: "kfm-xyz-v1"
    crs: "EPSG:3857"
    min_zoom: 10      # B2
    max_zoom: 16      # B4 (parcel-ish)
    zoom_band_min: "B2"
    zoom_band_max: "B4"
    sensitivity_label: "public"
    access_label: "open"
    geoprivacy_profile: "none"
~~~

**Constraint:**  
If any POI dataset becomes sensitive (e.g., shelters), it must be reclassified and moved to an appropriate **analytic-sensitive** or **sensitive** profile with reduced `max_zoom`.

---

## 🗺️ Diagrams

A simple diagram showing how profiles map into the stack:

~~~mermaid
flowchart LR
    A[STAC Collections & Items] --> B[ETL Normalization & Masking]
    B --> C[Tiling Profiles (this doc)]
    C --> D[Tile Generation Jobs]
    D --> E[Tile Services / APIs]
    E --> F[MapLibre / Cesium Clients]
    F --> G[Story Nodes & Focus Mode]
~~~

Each profile in this guide is essentially a **parameterization** of the tiling step (`C → D → E`), with the standard ensuring consistency and geoprivacy compliance.

---

## 🧪 Validation & CI/CD

### 1. Profile schema checks

Profiles in `tiler_config.yaml` that reference these examples should conform to a schema like:

~~~yaml
- name: "Validate tiling profiles"
  run: |
    jsonschema -i tiler_config.expanded.json \
      schemas/json/tiling-resolution-standard-v11.2.4.schema.json
~~~

Where `tiler_config.expanded.json` is generated from YAML.

### 2. Zoom-rule tests

Example pytest fragment (conceptual):

~~~python
from kfm_tiling_profiles import load_profiles

def test_profiles_respect_standard_bands():
    profiles = load_profiles("src/pipelines/tiling/tiler_config.yaml")

    for p in profiles:
        cat = p.category
        min_z = p.min_zoom
        max_z = p.max_zoom

        # Assert against the tiling-resolution standard rules
        if cat == "base":
            assert 4 <= min_z <= max_z <= 16
        elif cat == "analytic-open":
            assert 7 <= min_z <= max_z <= 16
        elif cat == "analytic-sensitive":
            assert 8 <= min_z <= max_z <= 12
        elif cat in {"sensitive", "sacred"}:
            assert 8 <= min_z <= max_z <= 10
~~~

These tests should live in `tests/geospatial/test_tiling_profiles.py` or equivalent.

---

## 📦 Data & Metadata

Each example profile implies:

- A STAC Collection/Item with `kfm:*` tiling metadata fields.  
- Alignment with `kfm:sensitivity_label` and `kfm:access_label` as defined in other KFM standards.  
- Optionally, link to geoprivacy masking profiles for sensitive/sacred overlays.

You may maintain a small **registry file** for example profiles, e.g.:

~~~json
{
  "profiles": [
    "kansas_basemap_v1",
    "kansas_landcover_county_v1",
    "kansas_soil_vulnerability_v1",
    "kansas_sacred_regions_v1",
    "kansas_public_poi_v1"
  ]
}
~~~

This can help CI confirm that every documented example has a corresponding implementation.

---

## 🌐 STAC, DCAT & PROV Alignment

These examples assume:

- STAC Collections for each tiling source (`kfm-basemap`, `kfm-landcover`, `kfm-soils`, `kfm-sacred`, `kfm-poi`).  
- DCAT datasets representing tile services where appropriate.  
- PROV bundles capturing tiling runs.

When implementing an example:

- Ensure the `standard_ref` in PROV and DCAT points to:
  - `kfm-doc-tiling-resolution-v11.2.4` (standard).  
  - `kfm-doc-tiling-resolution-examples-v11.2.4` (this guide) if you want a “recipe” reference.

---

## 🧠 Story Node & Focus Mode Integration

These examples are designed to produce tiles that:

- Map cleanly onto narrative scales:

  - B1: “Across Kansas…”  
  - B2: “At the county level…”  
  - B3: “Within this corridor or township…”  
  - B4: “At the level of individual public facilities…”  

- Respect geoprivacy and sovereignty for sacred/sensitive overlays.

Example Story Node metadata referencing a tiling profile:

~~~json
{
  "target_layer_id": "kansas_sacred_regions_v1",
  "target_zoom_band": "B2",
  "target_standard": "kfm-doc-tiling-resolution-v11.2.4",
  "narrative_scale": "county-sub-basin"
}
~~~

Focus Mode can use `target_zoom_band` and `target_layer_id` to:

- Clamp zoom levels.  
- Show summaries appropriate to the scale of the tiles.  

---

## ⚖ FAIR+CARE & Governance

These examples:

- **FAIR**
  - Make tiling configuration more **discoverable** and **reusable** (common patterns).  
  - Support interoperability by using `kfm:*` fields and standard profiles.  

- **CARE & sovereignty**
  - Show how sacred and sensitive layers are given stricter zoom ceilings and generalized geometries.  
  - Provide starting points that help teams avoid accidental overexposure.

Governance note:

- When a new project needs a custom tiling profile, it should **start from** the closest example here and:
  - Document deviations.  
  - Seek governance review if deviating from category-based zoom limits.

---

## 🕰️ Version History

| Version    | Date       | Status            | Notes                                                                                                   |
|-----------:|------------|-------------------|---------------------------------------------------------------------------------------------------------|
| **v11.2.4** | 2025-12-06 | Active / Enforced | Initial examples guide for tiling-resolution v11.2.4; adds Kansas-focused profiles and CI-friendly snippets. |

Future updates should:

- Add more **domain-specific examples** (e.g., hydrology, archaeology, historical imagery) as standards mature.  
- Track any changes in tiling standard rules (bands, categories) and update examples accordingly.  

---

<div align="center">

🧩 **KFM Tiling Resolution — Worked Examples & Zoom Profiles (v11.2.4)**  
Kansas-Focused Maps · Deterministic Profiles · FAIR+CARE Sovereignty  

[📘 Docs Root](../../../..) · [🧩 Tiling Standard](./README.md) · [🛡 Geoprivacy Masking](../geoprivacy-masking/README.md) · [⚖ Governance](../../governance/ROOT-GOVERNANCE.md)

</div>

