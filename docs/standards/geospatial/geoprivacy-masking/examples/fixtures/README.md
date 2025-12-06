---
title: "🧪 KFM Geoprivacy Masking — Fixtures Guide"
path: "docs/standards/geospatial/geoprivacy-masking/examples/fixtures/README.md"
version: "v11.2.4"
last_updated: "2025-12-06"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · FAIR+CARE Council · Tribal Sovereignty Board"
content_stability: "stable"
backward_compatibility: "v10.x → v11.x privacy-contract compatible"
status: "Active / Enforced"

doc_kind: "Guide"
header_profile: "standard"
footer_profile: "standard"

scope:
  domain: "geospatial-privacy"
  applies_to:
    - "ingest"
    - "etl"
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
sensitivity: "General (non-sensitive; auto-mask rules apply)"
sensitivity_level: "None"
public_exposure_risk: "Low"
classification: "Public"
jurisdiction: "Kansas / United States"
indigenous_rights_flag: true
data_steward: "KFM FAIR+CARE Council"

commit_sha: "<latest-commit>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../../releases/v11.2.4/sbom.spdx.json"
manifest_ref: "../../../../../../releases/v11.2.4/manifest.zip"
telemetry_ref: "../../../../../../releases/v11.2.4/privacy-masking-telemetry.json"
telemetry_schema: "../../../../../../schemas/telemetry/geoprivacy/v1.json"
energy_schema: "../../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../../../governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "Apache-2.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.4"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

ttl_policy: "24 months"
sunset_policy: "Aligned with geoprivacy-masking standard v11.2.4"

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
  - "docs/standards/geospatial/geoprivacy-masking/README.md@v11.2.4"
  - "docs/standards/geospatial/geoprivacy-masking/examples/README.md@v11.2.4"

provenance_requirements:
  versions_required: false
  newest_first: true
  must_reference_superseded: false
  must_reference_origin_root: true

json_schema_ref: "schemas/json/geoprivacy-masking-fixtures-v11.2.4.schema.json"
shape_schema_ref: "schemas/shacl/geoprivacy-masking-fixtures-v11.2.4-shape.ttl"

story_node_refs: []
immutability_status: "version-pinned"

doc_uuid: "urn:kfm:doc:standards:geoprivacy-masking-fixtures-v11.2.4"
semantic_document_id: "kfm-doc-geoprivacy-masking-fixtures-v11.2.4"
event_source_id: "ledger:kfm:doc:standards:geoprivacy:examples:fixtures"

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
    - "📘 Overview"
    - "🗂️ Directory Layout"
    - "🧭 Context"
    - "🗺️ Diagrams"
    - "🧠 Story Node & Focus Mode Integration"
    - "🧪 Validation & CI/CD"
    - "📦 Data & Metadata"
    - "🌐 STAC, DCAT & PROV Alignment"
    - "🧱 Architecture"
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

# 🧪 KFM Geoprivacy Masking — Fixtures Guide  
v11.2.4 · Synthetic Data · Test-First · FAIR+CARE Aligned  

`docs/standards/geospatial/geoprivacy-masking/examples/fixtures/README.md`

**Purpose:**  
Describe and govern the synthetic fixtures used to test and demonstrate KFM’s Geospatial Privacy & Cultural-Safety Masking Standard, ensuring all example datasets are safe, reproducible, sovereignty-aligned, and ready for CI/CD and catalog integration.

</div>

---

## 🗂️ Directory Layout

~~~text
📂 docs/standards/geospatial/geoprivacy-masking/examples/
└── 📂 fixtures/
    ├── 📄 README.md                          # 🧪 This guide: fixtures description & rules
    ├── 📄 points_kansas_small.geojson        # Small mixed-sensitivity point set (public/community/sensitive)
    ├── 📄 points_sacred_synthetic.geojson    # Synthetic sacred-site points (high-protection profile)
    ├── 📄 parcels_synthetic.geojson          # Synthetic parcel polygons for anti-triangulation tests
    ├── 📄 h3_regions_sacred_synthetic.geojson# H3 generalization regions for sacred fixtures
    └── 📄 points_public_demo.geojson         # Low-risk public/demo points for UI demonstrations
~~~

Author rules:

- All fixtures in this directory must be **synthetic** or sufficiently obfuscated; no direct exports from vault or production datasets are allowed.  
- Filenames must clearly indicate intended use (e.g., `_sacred_synthetic`, `_public_demo`, `_small`).  
- Any new file added here must be documented in this layout block and referenced from `docs/standards/geospatial/geoprivacy-masking/examples/README.md` where relevant.

---

## 📘 Overview

This fixtures guide underpins the geoprivacy masking examples by:

- Defining a **canonical set of synthetic datasets** for validating deterministic donut geomasking and related metadata rules.  
- Providing **stable identifiers and semantics** for fixtures so tests, documentation, and Story Nodes can refer to the same data.  
- Ensuring fixtures themselves respect **FAIR+CARE** and sovereignty principles, even though they do not contain real-world sensitive coordinates.  

The fixtures are designed to:

- Cover all sensitivity labels (`public`, `community`, `sensitive`, `sacred`).  
- Exercise distance bounds (`r_min`/`r_max`), determinism, and anti-triangulation behavior.  
- Support STAC/DCAT/PROV examples without revealing real locations.

Normative masking requirements live in:

- `docs/standards/geospatial/geoprivacy-masking/README.md`  

This document is **supporting and descriptive** but still governed.

---

## 🧭 Context

The fixtures sit at the entry point of the KFM geoprivacy test pipeline:

> Fixtures (this directory) → Masking ETL (donut method) → Masked outputs & STAC/DCAT Items → Neo4j test graph → API & frontend demos → Story Node & Focus Mode examples.

Contextual constraints:

- Fixtures must be **safe for public sharing**; they may appear in docs, demos, and training materials.  
- They must be **shape-compatible** with expected production datasets (same geometry types, key fields, coordinate reference system).  
- They are a **control group** for CI: changing their semantics or coordinates without updating tests is a breaking change.

For any new fixture, consider:

- Which masking behavior it is intended to exercise (distance windows, determinism, sovereignty gating, anti-triangulation).  
- Whether it can be reused across multiple CI scenarios (prefer reuse to proliferation).

---

## 🧱 Architecture

This fixtures set is organized around key test dimensions:

1. **Mixed-sensitivity baseline** — `points_kansas_small.geojson`  
   - ~10–100 points across all sensitivity labels.  
   - Spatially distributed across Kansas to avoid degenerate clusters.  
   - Serves as the **default fixture** for distance and determinism tests.

2. **Sacred synthetic set** — `points_sacred_synthetic.geojson`  
   - Synthetic sacred-site analogues (not derived from any real site data).  
   - Designed to test:
     - Large-radius masking (3–10 km).  
     - H3 region generalization.  
     - Sovereignty gating rules.  

3. **Parcel synthetic set** — `parcels_synthetic.geojson`  
   - Artificial parcel polygons with plausible shapes.  
   - Used to test:
     - Anti-triangulation requirements.  
     - No masked point coinciding exactly with parcel vertices or centroids.  

4. **Sacred H3 regions** — `h3_regions_sacred_synthetic.geojson`  
   - Polygonized H3 regions corresponding to generalized sacred fixtures.  
   - Ensures tests can validate that sacred data is exposed **only** as generalized regions/H3 cells.

5. **Public demo points** — `points_public_demo.geojson`  
   - Low-risk, generic points for UI screenshots and Story Node examples.  
   - Used to demonstrate how masking works without any sensitive semantics.

Each fixture file should:

- Use `EPSG:4326` (WGS84) coordinates.  
- Include machine-readable IDs suitable for seeding and PROV references.  
- Be small enough for fast CI runs.

---

## 🧪 Validation & CI/CD

The fixtures are intended for **automated testing**. Typical patterns:

### 1. Distance window tests

- Use `points_kansas_small.geojson` to verify each masked point’s distance from its original location lies within [r_min, r_max] for the assigned label.  
- Optionally, track summary statistics (min/max/mean) and compare to expectations captured in masking run manifests.

### 2. Determinism tests

- Run the masking function twice on `points_kansas_small.geojson` and `points_sacred_synthetic.geojson` with the same salt; coordinates must match exactly.  
- CI can store a “golden” masked output for comparison, but this requires coordination with secret management practices.

### 3. Anti-triangulation tests

- Combine masked outputs derived from:
  - `points_sacred_synthetic.geojson`  
  - `parcels_synthetic.geojson`  
- Assert no trivial re-identification via:
  - Exact vertex overlaps.  
  - Obvious one-to-one parcel associations.  

### 4. Sovereignty/H3 tests

- Validate that any masked outputs from `points_sacred_synthetic.geojson` are **not** exposed as points at UI/API level.  
- Use `h3_regions_sacred_synthetic.geojson` as expected generalized shapes and ensure they appear where sacred data is referenced.

All CI scenarios should reference fixture paths **relative to the repo root** for portability.

---

## 📦 Data & Metadata

### 1. Fixture metadata conventions

Each GeoJSON fixture should follow this pattern:

- Top-level FeatureCollection.  
- Each feature has:
  - `id` — a stable opaque identifier (e.g., `fixture:points_kansas_small:0001`).  
  - `properties.kfm:sensitivity_label` — one of `public`, `community`, `sensitive`, `sacred` where applicable.  
  - Optional descriptive fields (e.g., `fixture:note`) that clarify intent but avoid real-world references.

Example feature (fixture side, before masking):

~~~json
{
  "type": "Feature",
  "id": "fixture:points_kansas_small:0001",
  "geometry": {
    "type": "Point",
    "coordinates": [-97.000000, 38.500000]
  },
  "properties": {
    "kfm:sensitivity_label": "community",
    "fixture:note": "Synthetic community site for distance/determinism tests"
  }
}
~~~

### 2. Linkage to masking runs

Masking run manifests (tracked in `examples/masking-runs/`) should reference fixtures by path and, where needed, by feature ID patterns:

~~~json
{
  "run_id": "urn:kfm:etl-run:2025-12-06T00:00Z",
  "fixtures": [
    "docs/standards/geospatial/geoprivacy-masking/examples/fixtures/points_kansas_small.geojson",
    "docs/standards/geospatial/geoprivacy-masking/examples/fixtures/points_sacred_synthetic.geojson"
  ],
  "standard_ref": "kfm-doc-geoprivacy-masking-v11.2.4"
}
~~~

This linkage allows PROV bundles to trace from masked outputs back to **synthetic fixtures**, not real data.

---

## 🌐 STAC, DCAT & PROV Alignment

Even synthetic fixtures benefit from catalog alignment:

- **STAC alignment (internal dev/QA Collections)**  
  - You may maintain a `kfm-geoprivacy-fixtures` STAC Collection to track fixture sets.  
  - Each file can be a STAC Item with:
    - `id` = fixture filename or semantic ID.  
    - `properties["kfm:fixture_type"]` ∈ {`points-mixed`, `points-sacred`, `parcels-synthetic`, `h3-sacred`, `points-public-demo`}.  

- **DCAT alignment**  
  - Fixtures can appear in an internal `dcat:Dataset` catalog for QA/CI.  
  - Mark them as synthetic in descriptions to avoid confusion with production data.

- **PROV alignment**  
  - PROV bundles should treat fixtures as `prov:Entity` objects that **do not** derive from any sensitive vault entity.  
  - Use `prov:wasGeneratedBy` to link fixtures to fixture-generation scripts where relevant, documenting procedural generation parameters.

This alignment supports reusability of fixtures across tools and environments without ambiguity.

---

## ⚖ FAIR+CARE & Governance

Although these datasets are synthetic, they still embody FAIR+CARE practice:

- **FAIR**
  - *Findable*: stable paths and IDs, simple STAC/DCAT descriptions.  
  - *Accessible*: licensed under the same open terms as the standard, for internal and community use.  
  - *Interoperable*: standard GeoJSON + KFM metadata keys.  
  - *Reusable*: clear fixture semantics; safe for teaching, demos, and tests.

- **CARE & sovereignty**
  - Synthetic sacred fixtures model **behavior**, not real sites.  
  - Labels and policies applied to fixtures mirror those required for real sacred data, reinforcing practice.  
  - Documentation explicitly notes that fixtures must not be back-derived from real sensitive datasets.

Any attempt to create fixtures by directly perturbing real sacred coordinates must go through the same sovereignty and ethics review as production data and is generally discouraged in favor of fully synthetic generation.

---

## 🕰️ Version History

| Version    | Date       | Status            | Notes                                                                                       |
|-----------:|------------|-------------------|---------------------------------------------------------------------------------------------|
| **v11.2.4** | 2025-12-06 | Active / Enforced | Initial fixtures guide aligned with geoprivacy-masking v11.2.4; defines synthetic sets and CI usage. |

Future updates should:

- Add new fixtures only when they represent distinct test scenarios, not minor coordinate tweaks.  
- Update this README whenever files are added/removed/renamed.  
- Keep fixture semantics stable to avoid brittle tests; breaking changes require coordination with CI maintainers.

---

<div align="center">

🧪 **KFM Geoprivacy Masking — Fixtures Guide (v11.2.4)**  
Synthetic Data · Test-First Privacy · FAIR+CARE Ethics  

[📘 Docs Root](../../../../../..) · [🧪 Examples Index](../README.md) · [🛡 Geoprivacy Standard](../../README.md) · [⚖ Governance](../../../../../governance/ROOT-GOVERNANCE.md)

</div>

