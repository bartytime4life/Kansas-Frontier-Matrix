---
title: "🗺️ Kansas Frontier Matrix — Geo Generalization Examples for Sensitive Sites (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/standards/data-generalization/geo/examples/README.md"

version: "v11.0.0"
last_updated: "2025-12-06"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Annual · FAIR+CARE Council"
content_stability: "stable"

status: "Active / Enforced"
doc_kind: "Examples Index"
intent: "geo-sensitive-generalization-examples"
semantic_document_id: "kfm-doc-geo-sensitive-generalization-examples"
doc_uuid: "urn:kfm:docs:heritage:data-generalization-geo-examples:v11.0.0"
event_source_id: "ledger:kfm:doc:heritage:data-generalization-geo-examples:v11.0.0"
immutability_status: "version-pinned"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/data-generalization-geo-examples-v11.json"
energy_schema: "../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../schemas/telemetry/carbon-gco2e-v1.json"

governance_ref: "../../../governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "CC-BY-NC 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.4"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

scope:
  domain: "geo-sensitive-data-generalization"
  applies_to:
    - "examples"
    - "ingest"
    - "etl"
    - "stac"
    - "dcat"
    - "graph"
    - "api"
    - "frontend"
    - "maplibre"
    - "cesium"
    - "story-nodes"
    - "focus-mode"
    - "geoprivacy"
    - "archaeology"
    - "ecology"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

fair_category: "F1-A1-I2-R3"
care_label: "Restricted / High-Sensitivity"
sensitivity: "Cultural, archaeological, ecological (high)"
sensitivity_level: "High"
public_exposure_risk: "High"
classification: "Restricted"
jurisdiction: "Kansas / United States"
indigenous_rights_flag: true
data_steward: "KFM FAIR+CARE Council"

ttl_policy: "24 months"
sunset_policy: "Superseded by next geo-generalization examples revision"

provenance_chain:
  - "docs/standards/data-generalization/README.md@v11.0.0"
  - "docs/standards/data-generalization/geo/README.md@v11.0.0"

provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: true

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "TechArticle"
  prov_o: "prov:Plan"

metadata_profiles:
  - "STAC 1.0.0"
  - "DCAT 3.0"
  - "PROV-O"
  - "FAIR+CARE"

story_node_refs: []

ai_training_inclusion: false
ai_focusmode_usage: "Restricted / Governance-Only"
ai_transform_permissions:
  - "summary"
  - "index-generation"
ai_transform_prohibited:
  - "content-alteration"
  - "sensitive-detail-expansion"
  - "governance-override"
  - "narrative-fabrication"

transform_registry:
  allowed:
    - summary
    - index-generation
  prohibited:
    - content-alteration
    - sensitive-detail-expansion
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

heading_registry:
  approved_h2:
    - "📘 Overview"
    - "🗂️ Directory Layout"
    - "📦 Example Catalog"
    - "🧭 Context"
    - "🧪 Validation & CI/CD"
    - "🕰️ Version History"

test_profiles:
  - "markdown-lint"
  - "schema-lint"
  - "metadata-check"
  - "diagram-check"
  - "accessibility-check"
  - "provenance-check"
  - "footer-check"
  - "sensitivity-check"

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

# 🗺️ **Kansas Frontier Matrix — Geo Generalization Examples for Sensitive Sites (v11.0.0)**  
`docs/standards/data-generalization/geo/examples/README.md`  

**Purpose**  
Act as the **examples index** for geo‑level sensitive generalization in KFM.  
Collects concrete, end‑to‑end examples of H3 generalization, donut geomasking, zoom‑limited tiles, and STAC/graph annotations that implement the parent **Sensitive Site Data Generalization & CARE Governance Guide** and the **Geo Generalization Standard** in real KFM pipelines.

</div>

---

## 📘 Overview

This examples index:

- Provides **ready‑to‑copy patterns** for engineers implementing sensitive‑site generalization in ETL, STAC, MapLibre/Cesium, and Neo4j.  
- Demonstrates how to combine:

  - Sensitivity levels (L1–L4).  
  - H3 resolutions and donut masking.  
  - CRS, tiling, and zoom constraints.  
  - STAC/DCAT/PROV metadata.  
  - CARE blocks and governance references.  

- Serves as the **canonical fixture library** for CI scenarios that test:

  - Anti‑triangulation safety.  
  - Determinism and reproducibility.  
  - Coordinate removal and attribute suppression.  
  - Multi‑layer map behavior for sensitive content.

All examples are illustrative and must be adapted with **real governance decisions** and community‑approved parameters before production use.

---

## 🗂️ Directory Layout

```text
📂 docs/
└── 📂 standards/
    └── 📂 data-generalization/
        ├── 📂 geo/
        │   📄 README.md                  # 🗺️ Geo generalization standard
        │   📂 examples/
        │   │   📄 README.md              # 🧾 This examples index
        │   │   📂 h3-resolution/
        │   │   │   📄 L1_public_r7.md    # H3 r7 examples for L1 public archaeological data
        │   │   │   📄 L2_restricted_r6.md# H3 r6 examples for L2 restricted data
        │   │   │   📄 L3_heritage_r5.md  # H3 r5/r4 examples for L3 Indigenous heritage
        │   │   📂 donut-vs-h3/
        │   │   │   📄 comparison.md      # When to use donut masking vs pure H3 generalization
        │   │   📂 tiles-and-zoom/
        │   │   │   📄 zoom_policies.md   # Example tile endpoints + minzoom/maxzoom policies
        │   │   │   📄 legend_text.md     # Standardized legend text for generalized layers
        │   │   📂 stac-and-dcat/
        │   │   │   📄 stac_item_examples.md # STAC Items with kfm:geo_generalization blocks
        │   │   │   📄 dcat_dataset_examples.md # DCAT entries with spatialResolutionInMeters
        │   │   📂 graph-and-story-nodes/
        │   │   │   📄 neo4j_modeling.md  # How generalized H3 cells become graph nodes
        │   │   │   📄 storynode_patterns.md # Safe Story Node geometry + narrative patterns
        │   │   📂 ci-scenarios/
        │   │       📄 anti_triangulation.md   # Multi-layer examples to test triangulation risk
        │   │       📄 zoom_leakage.md         # Examples where zoom levels could leak precision
        │   │       📄 mixed_layers.md         # Tests for combining sensitive + non-sensitive layers
        │   └── 📂 validation/
        │       📄 README.md              # Validation overview for data-generalization/geo
```

Author rules:

- Any new example file must be **listed in this tree** or in a small per‑subdirectory index.  
- Files under `examples/` must:

  - Be clearly marked as **examples** (not authoritative policy).  
  - Reference the relevant governing standard(s) in their intro.  
  - Avoid including real confidential coordinates or unredacted sensitive narratives.

---

## 📦 Example Catalog

This section summarizes the kinds of examples that live under each subfolder.

### 1. `h3-resolution/` — Sensitivity → H3 mapping

Example themes:

- **`L1_public_r7.md`**  

  - How to convert low‑sensitivity archaeological points into H3 r7 polygons.  
  - How to encode `kfm:h3_resolution` and `dcat:spatialResolutionInMeters`.  

- **`L2_restricted_r6.md`**  

  - Combining H3 r6 with limited zoom ranges and attribute suppression.  
  - Preventing parcel‑level inference from multiple overlays.  

- **`L3_heritage_r5.md`**  

  - Coarse H3 r5/r4 generalization for Indigenous cultural landscapes.  
  - Examples of representing extensive cultural regions rather than discrete points.

Each file should show:

- Before → after geometry sketches (described textually, no real coordinates).  
- STAC property blocks for `kfm:geo_generalization`.  
- Short notes on CARE decisions driving each resolution choice.

---

### 2. `donut-vs-h3/` — Comparison patterns

**`comparison.md`** should include:

- Side‑by‑side examples:

  - Donut geomasked points for low‑sensitivity POIs.  
  - H3 generalized cells for sensitive heritage features.  

- Clear rules of thumb:

  - When donut masking is acceptable (internal/restricted).  
  - When H3 or full concealment is required (L2–L4).  

- Example MapLibre style fragments showing:

  - Donut‑masked points as icons.  
  - H3 cells as filled polygons with appropriate legend text.

---

### 3. `tiles-and-zoom/` — Tile & zoom policies

**`zoom_policies.md`** should demonstrate:

- Tile URL templates for sensitive layers (e.g. restricted endpoints).  
- Recommended `minzoom`/`maxzoom` values by sensitivity level.  
- STAC asset blocks with zoom constraints and `kfm:layer_visibility`.

**`legend_text.md`** should contain:

- Copy‑paste‑ready legend strings like:

  > “Locations generalized into hexagonal regions for cultural and ecological protection.”

- Guidance on:

  - Color palettes that avoid implying point precision.  
  - A11y‑friendly descriptions for screen readers.

---

### 4. `stac-and-dcat/` — Catalog examples

**`stac_item_examples.md`**:

- Full Item JSON snippets with:

  - `heritage:*`, `care:*`, `kfm:geo_generalization`, and `kfm:h3_*` fields.  
  - Assets for COGs and tiles, with correct roles, types, and zooms.  

**`dcat_dataset_examples.md`**:

- DCAT JSON‑LD examples mapping:

  - H3 resolution → `dcat:spatialResolutionInMeters`.  
  - CARE status → `dct:accessLevel` and `dct:rights`.  
  - Provenance → `dct:provenance` with geo generalization descriptions.

---

### 5. `graph-and-story-nodes/` — Neo4j + narrative

**`neo4j_modeling.md`**:

- Example Cypher patterns for:

  - Representing H3 cells as nodes (e.g. `:HexRegion`).  
  - Linking `HexRegion` nodes to `:HeritageArea` or `:EcologicalZone`.  
  - Encoding CARE and sensitivity metadata as node properties / relationship attributes.

**`storynode_patterns.md`**:

- Example Story Nodes that:

  - Reference generalized geometries only.  
  - Use region‑scale narratives instead of site‑scale directions.  
  - Include disclaimers showing that locations are generalized or withheld.

---

### 6. `ci-scenarios/` — Test fixtures

**`anti_triangulation.md`**:

- Example multi‑layer scenarios where:

  - Combining generalized heritage, hydrology, and infrastructure layers could risk triangulation.  
  - CI scripts ensure no single hex or region is uniquely identified across overlays.

**`zoom_leakage.md`**:

- Examples where:

  - Tile servers misconfigure `maxzoom`, making cells appear more precise at high zoom.  
  - Tests catch mismatches between advertised and actual zoom constraints.

**`mixed_layers.md`**:

- Cases where:

  - Sensitive and non‑sensitive layers co‑exist.  
  - CI asserts that sensitive layers retain generalization and do not adopt precision from adjacent layers.

---

## 🧭 Context

These examples are **non‑normative** but **strongly recommended** patterns aligned with:

- `docs/standards/data-generalization/README.md` (global governance).  
- `docs/standards/data-generalization/geo/README.md` (geo implementation).  
- `docs/standards/geospatial/geoprivacy-masking/README.md` (donut masking).  
- `docs/standards/geo/archaeology-sensitive-locations.md` (sensitivity ladder).  

When building new pipelines:

- Start from the closest matching example file.  
- Adapt parameters to governance decisions and local context.  
- Update the example index to point at any new archetype that emerges from production practice.

---

## 🧪 Validation & CI/CD

Examples under this directory are intended to be used directly as:

- **Fixtures** for CI pipelines (`geo-sensitivity-check`, `stac-geo-validate`).  
- **Golden outputs** for regression testing of masking/generalization logic.  
- **Reference snippets** for static analysis of STAC, DCAT, and PROV‑O metadata.

Best practices:

- Mark test fixtures clearly (e.g. `fixtures/` subfolders under each example theme).  
- Use obviously fake coordinates / IDs that cannot be mistaken for real sites.  
- Include a short “What this tests” note at the top of each CI scenario file.

A PR is **blocked** if:

- New or updated examples contradict the governing standards.  
- Real sensitive coordinates or unredacted narratives appear in any example.  
- Example fixtures cause CI to pass incorrectly by weakening detection logic.

---

## 🕰️ Version History

| Version | Date       | Status            | Summary                                                                                           |
|--------:|------------|-------------------|---------------------------------------------------------------------------------------------------|
| v11.0.0 | 2025-12-06 | Active / Enforced | Initial examples index for geo‑level generalization patterns aligned with v11 CARE & geoprivacy. |

---

<div align="center">

🗺️ **Kansas Frontier Matrix — Geo Generalization Examples for Sensitive Sites (v11.0.0)**  
“Examples are safe only when they teach safety.”

CC‑BY‑NC 4.0 · FAIR+CARE Council · MCP‑DL v6.3  

[⬅ Back to Geo Generalization Standard](../README.md) · [🏺 Global Sensitive Data Generalization](../../README.md) · [⚖ Governance](../../../governance/ROOT-GOVERNANCE.md)

</div>

