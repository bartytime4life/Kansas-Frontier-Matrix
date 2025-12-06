---
title: "🧪 KFM Geoprivacy Masking — Examples & Validation Patterns"
path: "docs/standards/geospatial/geoprivacy-masking/examples/README.md"
version: "v11.2.4"
last_updated: "2025-12-05"

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

sbom_ref: "../../../../../releases/v11.2.4/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.2.4/manifest.zip"
telemetry_ref: "../../../../../releases/v11.2.4/privacy-masking-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/geoprivacy/v1.json"
energy_schema: "../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../sovereignty/INDIGENOUS-DATA-PROTECTION.md"

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

provenance_requirements:
  versions_required: false
  newest_first: true
  must_reference_superseded: false
  must_reference_origin_root: true

json_schema_ref: "schemas/json/geoprivacy-masking-examples-v11.2.4.schema.json"
shape_schema_ref: "schemas/shacl/geoprivacy-masking-examples-v11.2.4-shape.ttl"

story_node_refs: []
immutability_status: "version-pinned"

doc_uuid: "urn:kfm:doc:standards:geoprivacy-masking-examples-v11.2.4"
semantic_document_id: "kfm-doc-geoprivacy-masking-examples-v11.2.4"
event_source_id: "ledger:kfm:doc:standards:geoprivacy:examples"

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

# 🧪 KFM Geoprivacy Masking — Examples & Validation Patterns  
v11.2.4 · Deterministic ETL · Test-Focused · FAIR+CARE Aligned  

`docs/standards/geospatial/geoprivacy-masking/examples/README.md`

**Purpose:**  
Provide concrete, reproducible examples and validation patterns for the KFM Geospatial Privacy & Cultural-Safety Masking Standard, including sample fixtures, masking scenarios, anti-patterns, and CI-ready tests for deterministic donut geomasking and associated metadata.

</div>

---

## 🗂️ Directory Layout

~~~text
📂 docs/
└── 📂 standards/
    └── 📂 geospatial/
        └── 📂 geoprivacy-masking/
            ├── 📄 README.md                     # 🛡️ Normative geoprivacy & masking standard
            └── 📂 examples/
                ├── 📄 README.md                 # 🧪 This guide: examples & validation patterns
                ├── 📂 fixtures/
                │   ├── 📄 points_kansas_small.geojson      # Minimal example points for unit tests
                │   ├── 📄 points_sacred_synthetic.geojson  # Synthetic sacred-site fixtures
                │   └── 📄 parcels_synthetic.geojson        # Synthetic parcels for triangulation tests
                ├── 📂 masking-runs/
                │   ├── 📄 run_2025-12-05T00-00Z.json       # Example masking run manifest
                │   └── 📄 run_2025-12-05T00-00Z_prov.jsonld# PROV bundle for the same run
                └── 📂 ci-scenarios/
                    ├── 📄 distance_validation.md           # r_min / r_max distance examples
                    ├── 📄 determinism.md                   # seed stability patterns
                    └── 📄 anti_triangulation.md            # cross-layer de-anonymization tests
~~~

Author rules:

- Any new fixture, masking-run manifest, or CI scenario added under this directory **must** be briefly described in this tree or in the corresponding `ci-scenarios/*.md` documents.  
- Synthetic data under `fixtures/` must not be directly derived from vault data; it should be procedurally generated or sufficiently perturbed and labeled as synthetic.  
- Example filenames should clearly reflect their use (e.g., `*_sacred_synthetic`, `*_public_demo`).

---

## 📘 Overview

This guide operationalizes the **Geospatial Privacy & Cultural-Safety Masking Standard v11.2.4** by:

- Providing **ready-to-use fixtures** for unit, integration, and regression tests of deterministic donut geomasking.  
- Demonstrating **correct and incorrect** masking patterns, including forbidden techniques (naïve rounding, unbounded jitter, constant shifts).  
- Showing how to attach **masking metadata**, STAC/DCAT fields, and PROV bundles to masked geometries.  
- Offering **CI-ready scenarios** that can be wired directly into `.github/workflows/kfm-ci.yml` and other pipeline checks.  

This document is **descriptive and example-focused**; the normative rules live in:

- `docs/standards/geospatial/geoprivacy-masking/README.md`  

When in doubt, treat the standard as authoritative and this guide as illustrative.

---

## 🧭 Context

The examples here assume:

- KFM uses the deterministic donut geomasking method for point-based geoprivacy.  
- Raw coordinates reside only in a high-security vault and never leave that context.  
- Masking is applied **in ETL** before STAC/DCAT publication, Neo4j ingestion, tiling, or frontend exposure.  

These examples sit directly in the KFM pipeline:

> Raw vault data → Deterministic masking (donut method) → STAC/DCAT Items with `kfm:*` privacy fields → Neo4j nodes with masked geometry + sensitivity → APIs & MapLibre/Cesium layers → Story Nodes & Focus Mode overlays.

Use these examples to:

- Validate local ETL changes before touching real data.  
- Demonstrate behavior to reviewers (FAIR+CARE Council, Tribal Sovereignty Board).  
- Serve as a template when expanding geoprivacy to new geometry types or domains.

---

## 🧱 Architecture

This directory organizes examples along three axes:

1. **Fixtures (`fixtures/`)**  
   - Minimal, synthetic datasets for:
     - Distance window checks (r_min / r_max).  
     - Determinism checks (seed stability).  
     - Anti-triangulation checks (cross-layer interactions).  

2. **Masking run manifests (`masking-runs/`)**  
   - JSON and PROV bundles representing a **single ETL masking run**:
     - Input fixture identifiers.  
     - Masking parameters (radius bounds, salts, algorithm versions).  
     - Output summary (counts, failure modes, distance stats).  

3. **CI scenarios (`ci-scenarios/`)**  
   - Markdown guides tying fixtures + manifests into:
     - Distance validation tests.  
     - Determinism tests.  
     - Anti-triangulation & sovereignty compliance tests.  

The intention is that:

- `fixtures/` + `masking-runs/` provide **data-side** examples.  
- `ci-scenarios/` provides **test-side** wiring for pipelines and `.github/workflows/kfm-ci.yml`.

---

## 🧪 Validation & CI/CD

This guide is tightly bound to the test profiles defined in the standard.

### 1. Distance validation example

**Goal:** check that masked points fall between `r_min` and `r_max` for the assigned sensitivity label.

Example pseudo-test (Python-style):

~~~python
def test_distance_within_bounds(loaded_masked_points):
    for rec in loaded_masked_points:
        label = rec["properties"]["kfm:sensitivity_label"]
        r_min = RADIUS_TABLE[label]["min"]
        r_max = RADIUS_TABLE[label]["max"]
        d_m = geodesic_distance(rec["orig_lat"], rec["orig_lon"],
                                rec["masked_lat"], rec["masked_lon"])
        assert r_min <= d_m <= r_max
~~~

In this examples directory:

- `fixtures/points_kansas_small.geojson` provides small, labeled sets of points per sensitivity.  
- `masking-runs/run_2025-12-05T00-00Z.json` includes summary statistics for the same run, which CI can validate against.

### 2. Deterministic stability example

**Goal:** same `(record_id, label, salt)` → same masked coordinates on every run.

Example test outline:

~~~python
def test_determinism(mask_func, fixture_points, salt):
    first_run = {r["id"]: mask_func(r, salt) for r in fixture_points}
    second_run = {r["id"]: mask_func(r, salt) for r in fixture_points}
    assert first_run == second_run
~~~

Fixture:

- Use `fixtures/points_kansas_small.geojson` to keep tests lightweight.  
- Optionally include a “stress” fixture file if you need to test thousands of records.

### 3. Anti-triangulation example

**Goal:** combinations of masked layers must not re-identify original locations via intersections.

Approach:

- Load:

  - `fixtures/points_sacred_synthetic.geojson` (masked sacred points).  
  - `fixtures/parcels_synthetic.geojson` (synthetic parcel boundaries).  

- Check:

  - No masked point lies exactly on a parcel boundary vertex.  
  - No masked point is consistently “closest” to one parcel in a way that could trivially re-identify.  

Sketch:

~~~python
def test_no_exact_parcel_vertex_coincidence(masked_points, parcels):
    parcel_vertices = extract_vertices(parcels)
    for p in masked_points:
        assert (p["geometry"]["coordinates"] not in parcel_vertices)
~~~

CI can run this under a profile like `provenance-check` or `metadata-check` to ensure outputs respect anti-triangulation constraints.

### 4. Sovereignty compliance example

For sacred fixtures:

- Ensure **no sacred point** appears as a literal point geometry in outputs:
  - Only generalized H3 indexes or polygons.  
- Confirm that appropriate sovereignty flags are set:

  - `kfm:sensitivity_label = "sacred"`  
  - `kfm:access_label` indicates restricted/tribal-only.  

Example assertion:

~~~python
def test_sacred_points_generalized_only(masked_items):
    for item in masked_items:
        if item["properties"]["kfm:sensitivity_label"] == "sacred":
            assert item["geometry"]["type"] in ("Polygon", "MultiPolygon")
            assert "kfm:h3_cells" in item["properties"]
~~~

---

## 📦 Data & Metadata

The examples here demonstrate the **expected shape** of masking metadata.

### 1. Example masked point feature (GeoJSON-like)

~~~json
{
  "type": "Feature",
  "id": "fixture:community:0001",
  "geometry": {
    "type": "Point",
    "coordinates": [-96.700123, 38.987654]
  },
  "properties": {
    "kfm:privacy_method": "donut_geomask_v1",
    "kfm:r_min_m": 250,
    "kfm:r_max_m": 500,
    "kfm:seed_strategy": "HMAC(record_id, secret_salt)",
    "kfm:sensitivity_label": "community",
    "kfm:access_label": "community-open",
    "kfm:masking_run_id": "urn:kfm:etl-run:2025-12-05T00:00Z",
    "kfm:prov_ref": "prov/fixture_community_0001.jsonld"
  }
}
~~~

### 2. Example masking run manifest (simplified)

~~~json
{
  "run_id": "urn:kfm:etl-run:2025-12-05T00:00Z",
  "standard_ref": "kfm-doc-geoprivacy-masking-v11.2.4",
  "fixtures": [
    "fixtures/points_kansas_small.geojson",
    "fixtures/points_sacred_synthetic.geojson"
  ],
  "privacy_method": "donut_geomask_v1",
  "radius_profiles": {
    "public":    { "min_m": 50,   "max_m": 150 },
    "community": { "min_m": 250,  "max_m": 500 },
    "sensitive": { "min_m": 1000, "max_m": 3000 },
    "sacred":    { "min_m": 3000, "max_m": 10000 }
  },
  "summary": {
    "total_records": 120,
    "failed_records": 0,
    "min_distance_m": 52.3,
    "max_distance_m": 9876.5
  }
}
~~~

These examples are intentionally synthetic and may be simplified; production manifests can add more PROV and telemetry fields while keeping the same core patterns.

---

## 🌐 STAC, DCAT & PROV Alignment

The examples should reinforce the same STAC/DCAT/PROV alignment as the main standard.

### 1. STAC example snippet

~~~json
{
  "type": "Feature",
  "id": "kfm-example-geoprivacy-community-1",
  "properties": {
    "datetime": "2025-12-05T00:00:00Z",
    "kfm:privacy_method": "donut_geomask_v1",
    "kfm:sensitivity_label": "community",
    "kfm:r_min_m": 250,
    "kfm:r_max_m": 500,
    "kfm:masking_run_id": "urn:kfm:etl-run:2025-12-05T00:00Z",
    "kfm:prov_ref": "prov/fixture_community_0001.jsonld"
  },
  "assets": {
    "geomasked": {
      "href": "s3://kfm-example/geoprivacy/community/geomasked.geojson",
      "type": "application/geo+json"
    }
  }
}
~~~

### 2. DCAT example snippet

~~~json
{
  "@type": "dcat:Dataset",
  "dct:title": "KFM Geoprivacy Masking Example — Community Fixtures",
  "dct:identifier": "kfm-doc-geoprivacy-masking-examples-v11.2.4-community",
  "dct:provenance": {
    "@id": "prov/fixture_community_0001.jsonld"
  },
  "dct:accessRights": "community-open",
  "dct:license": "https://www.apache.org/licenses/LICENSE-2.0"
}
~~~

### 3. PROV example snippet (very simplified)

~~~json
{
  "@context": "https://www.w3.org/ns/prov.jsonld",
  "@id": "prov/fixture_community_0001.jsonld",
  "@type": "prov:Entity",
  "prov:wasGeneratedBy": "urn:kfm:etl-run:2025-12-05T00:00Z",
  "prov:wasDerivedFrom": "urn:kfm:vault:community_point_0001",
  "prov:wasInfluencedBy": "urn:kfm:policy:geoprivacy-masking-v11.2.4"
}
~~~

These examples are deliberately minimal; implementations can extend them while preserving structural compatibility.

---

## 🗺️ Diagrams

To clarify how these examples flow through the system, you can include a Mermaid diagram like:

~~~mermaid
flowchart LR
    A[Fixtures in examples/] --> B[Deterministic Masking ETL]
    B --> C[Masked GeoJSON + STAC Items]
    C --> D[Neo4j Geoprivacy Nodes]
    D --> E[API & MapLibre/Cesium Layers]
    E --> F[Story Nodes & Focus Mode]
~~~

Key points:

- Examples are **entry points** for local testing and demonstrations.  
- The same patterns should hold when scaling to production datasets and full ETL runs.

---

## 🧠 Story Node & Focus Mode Integration

While this directory is primarily for engineering and governance review, it is also a rich input for Story Nodes and Focus Mode.

Patterns:

- Story Nodes can reference **example scenarios** to explain geoprivacy to end users (e.g., “How we protect sacred sites”).  
- Focus Mode may summarize:
  - The main masking method.  
  - How sensitive data is transformed.  
  - What synthetic examples show (without revealing any real-world coordinates).  

Guidelines:

- Example text should clearly mark datasets as **synthetic** or **demonstrative**.  
- Avoid fictional narratives that resemble real sacred sites too closely; keep examples generic and educational.  
- If examples are shown in UI, labels should emphasize that they are training/demo data, not real coordinates.

---

## ⚖ FAIR+CARE & Governance

These examples exist to **strengthen** FAIR+CARE and sovereignty-aligned practice, not to weaken it.

- **FAIR**
  - The fixtures and manifests are **findable** via their IDs and paths.  
  - They are **accessible** under a permissive license for internal and community education.  
  - They are **interoperable** via STAC/DCAT/PROV patterns.  
  - They are **reusable** as templates for new masking scenarios and datasets.

- **CARE & sovereignty**
  - Synthetic sacred fixtures demonstrate high-protection patterns without exposing real locations.  
  - Governance metadata (sensitivity labels, sovereignty policies) appears even in examples, reinforcing expected practice.  
  - Example anti-patterns (e.g., naïve rounding) should be clearly labeled as **forbidden** and only used in “what not to do” contexts.

Any use of **real** sensitive or sacred data must be governed by the main standard, the Sovereignty policy, and relevant Tribal/community agreements; this examples directory is not an exception pathway.

---

## 🕰️ Version History

| Version   | Date       | Status            | Notes                                                                                         |
|----------:|------------|-------------------|-----------------------------------------------------------------------------------------------|
| **v11.2.4** | 2025-12-05 | Active / Enforced | Initial examples guide aligned with Geoprivacy Masking Standard v11.2.4; adds fixtures & CI patterns. |

Future revisions should:

- Add new fixtures and CI scenarios as masking extends to new geometry types or domains.  
- Keep metadata, STAC/DCAT examples, and PROV snippets consistent with the main standard.  
- Document any changes that affect test expectations (e.g., new radius profiles or sensitivity labels).

---

<div align="center">

🧪 **KFM Geoprivacy Masking — Examples & Validation Patterns (v11.2.4)**  
Scientific Insight · Test-First Privacy · FAIR+CARE Ethics  

[📘 Docs Root](../../../../..) · [🛡 Geoprivacy Standard](../README.md) · [⚖ Governance](../../../governance/ROOT-GOVERNANCE.md)

</div>

