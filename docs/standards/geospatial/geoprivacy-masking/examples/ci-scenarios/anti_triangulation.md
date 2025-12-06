---
title: "🧪 KFM Geoprivacy Masking — CI Scenario: Anti-Triangulation Defense"
path: "docs/standards/geospatial/geoprivacy-masking/examples/ci-scenarios/anti_triangulation.md"
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
  - "docs/standards/geospatial/geoprivacy-masking/examples/ci-scenarios/README.md@v11.2.4"

provenance_requirements:
  versions_required: false
  newest_first: true
  must_reference_superseded: false
  must_reference_origin_root: true

# NOTE: These schema refs are proposed and require schema design/review.
json_schema_ref: "schemas/json/geoprivacy-masking-ci-anti-triangulation-v11.2.4.schema.json"
shape_schema_ref: "schemas/shacl/geoprivacy-masking-ci-anti-triangulation-v11.2.4-shape.ttl"

story_node_refs: []
immutability_status: "version-pinned"

doc_uuid: "urn:kfm:doc:standards:geoprivacy-masking-ci-anti-triangulation-v11.2.4"
semantic_document_id: "kfm-doc-geoprivacy-masking-ci-anti-triangulation-v11.2.4"
event_source_id: "ledger:kfm:doc:standards:geoprivacy:examples:ci-scenarios:anti-triangulation"

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

# 🧪 KFM Geoprivacy Masking — CI Scenario: Anti-Triangulation Defense  
v11.2.4 · Cross-Layer Privacy · Sovereignty-First · Governance-Enforced  

`docs/standards/geospatial/geoprivacy-masking/examples/ci-scenarios/anti_triangulation.md`

**Purpose:**  
Define the canonical continuous integration (CI) scenario that tests KFM’s defenses against **spatial triangulation and cross-layer re-identification** of sensitive and sacred locations, using only synthetic fixtures and example masking runs while enforcing deterministic donut masking, sovereignty rules, and catalog-ready metadata.

</div>

---

## 📘 Overview

This CI scenario focuses on a specific geoprivacy risk:

> Even when each dataset is individually masked, **combinations** of layers (e.g., masked sacred points + parcel boundaries + auxiliary layers) can allow adversaries to re-identify original sites via spatial triangulation, correlation, or pattern matching.

This document specifies:

- Which **fixtures** and **masking runs** are used to simulate triangulation risk.  
- What **tests** must be implemented to detect trivial or obvious re-identification vectors.  
- How failures in this scenario map to **governance violations** and CI outcomes.  

The scenario is **normative** for example-based CI using the KFM geoprivacy fixtures and manifests. Production systems may implement additional, higher-scale checks, but they **must not do less** than what is defined here.

---

## 🗂️ Directory Layout

~~~text
📂 docs/standards/geospatial/geoprivacy-masking/examples/
└── 📂 ci-scenarios/
    ├── 📄 README.md                      # CI scenario index & governance
    ├── 📄 distance_validation.md         # r_min / r_max enforcement
    ├── 📄 determinism.md                 # seed stability
    ├── 📄 anti_triangulation.md          # 🔍 This file: cross-layer de-anonymization defenses
    ├── 📄 sovereignty_compliance.md      # sacred generalization & access gating
    └── 📄 metadata_provenance.md         # masking metadata & PROV checks
~~~

Related directories:

- Fixtures:  
  `docs/standards/geospatial/geoprivacy-masking/examples/fixtures/`  
- Example masking runs:  
  `docs/standards/geospatial/geoprivacy-masking/examples/masking-runs/`

Any new anti-triangulation scenario variant (e.g., including line networks or DEMs) should either extend this document or introduce a clearly named sibling file and update the scenario index.

---

## 🧭 Context

This anti-triangulation CI scenario sits at the intersection of:

- **Deterministic donut masking** for sensitive and sacred points.  
- **Synthetic parcel polygons** that mimic land-ownership and administrative boundaries.  
- **Sovereignty rules** that demand extra protection for sacred data.  

Threat model (simplified):

- An adversary combines multiple layers:
  - Masked sacred points.  
  - Parcel polygons or other boundary layers.  
  - Possibly additional public context (roads, rivers, known infrastructure).  
- The adversary attempts to:
  - Infer which parcel hosts a sacred site.  
  - Infer original locations more precisely than allowed by the masking radius windows or H3 generalization.  

Goal of this scenario:

- Ensure that **basic, automated checks** can detect when masked outputs have become too tightly coupled to auxiliary layers in ways that would **obviously undermine geoprivacy**.  
- Provide a **reusable framework** for testing new layers or masking profiles against triangulation risks.

This does *not* guarantee perfect protection against all sophisticated attacks, but it sets a **governance minimum** that KFM systems are required to enforce.

---

## 🧱 Architecture

This CI scenario uses these example artifacts:

- Fixtures:
  - `examples/fixtures/points_sacred_synthetic.geojson`  
  - `examples/fixtures/parcels_synthetic.geojson`  

- Example masking runs:
  - `examples/masking-runs/run_2025-12-06T00-00Z_sacred.json`  
  - `examples/masking-runs/run_2025-12-06T00-00Z_sacred_prov.jsonld`  

- Expected behavior:
  - Sacred points are masked with large-radius donut geomasking.  
  - At API/frontend level, sacred data is generalized (H3 or polygons), but this CI scenario focuses specifically on **point-like triangulation** with parcels.

High-level test architecture:

1. **Load fixtures** (sacred points + parcels).  
2. **Load masked outputs** (from the indicated run manifest); this may be either:
   - Masked points (pre-generalization), or  
   - Generalized geometries used in internal analytics.  
3. **Evaluate spatial relationships**:
   - Overlaps, minimal distances, cell/parcel associations.  
4. **Assert safety thresholds**:
   - No exact vertex overlaps.  
   - No one-to-one sacred → parcel mapping that trivially reveals original locations.  

Implementation details (search radius thresholds, tolerances, etc.) belong in test code and/or configuration files referenced from this scenario.

---

## 🧪 Validation & CI/CD

This section defines the **minimal tests** CI must perform for anti-triangulation.

### 1. No exact parcel vertex overlap

**Intent:** avoid the obviously bad case where a masked sacred point lands exactly on a parcel vertex.

Pseudocode:

~~~python
def test_no_exact_parcel_vertex_overlap(masked_points, parcels):
    parcel_vertices = extract_vertices(parcels)  # set of (lon, lat) tuples
    for p in masked_points:
        coords = tuple(p["geometry"]["coordinates"])
        assert coords not in parcel_vertices, (
            f"Masked point {p['id']} exactly matches a parcel vertex"
        )
~~~

Implementation notes:

- `extract_vertices` should:
  - Handle `Polygon` and `MultiPolygon`.  
  - Normalize coordinates (e.g., rounding to a small epsilon) so that CI does not trip on insignificant floating-point noise.

Failure handling:

- Any exact match is a **hard CI failure** and should block merge/deploy.

### 2. No exact parcel centroid overlap

**Intent:** prevent masked points from sitting exactly on parcel centroids, which is a classic triangulation vector.

Pseudocode:

~~~python
def test_no_exact_parcel_centroid_overlap(masked_points, parcels):
    parcel_centroids = extract_centroids(parcels)  # set of (lon, lat) tuples
    for p in masked_points:
        coords = tuple(p["geometry"]["coordinates"])
        assert coords not in parcel_centroids, (
            f"Masked point {p['id']} exactly matches a parcel centroid"
        )
~~~

### 3. Limit “closest parcel” uniqueness

**Intent:** avoid a pattern where each sacred masked point has exactly one uniquely closest parcel at an unrealistically small distance (e.g., a few meters), which could allow parcel-level deanonymization.

Approach:

- Compute distance from each masked point to each parcel centroid.  
- Identify the closest parcel and distance per point.  
- Assert:
  - Distances exceed a minimum parcel-level threshold (e.g., > 100 m).  
  - Optionally, that some points share closest parcels, so there is no direct one-to-one mapping.

Pseudocode:

~~~python
MIN_SAFE_PARCEL_DISTANCE_M = 100.0  # example threshold; tune via governance

def test_no_trivial_closest_parcel_mapping(masked_points, parcels):
    parcel_centroids = extract_centroids(parcels)
    mapping = {}  # point_id -> (closest_parcel_id, distance_m)

    for p in masked_points:
        pid = p["id"]
        dists = [
            (parcel["id"], geodesic_distance(p, parcel_centroid))
            for parcel, parcel_centroid in parcel_centroids
        ]
        closest_parcel_id, d_min = min(dists, key=lambda x: x[1])
        mapping[pid] = (closest_parcel_id, d_min)
        assert d_min >= MIN_SAFE_PARCEL_DISTANCE_M, (
            f"Masked point {pid} is too close ({d_min} m) to parcel {closest_parcel_id}"
        )

    # Optional: additional checks on distribution of closest parcels
    # e.g., ensure not a near-perfect uniqueness mapping
~~~

Exact thresholds and advanced statistical diagnostics should be defined in configuration and reviewed by governance bodies.

### 4. Configuration & wiring into CI

Recommended test module:

- `tests/geoprivacy/test_anti_triangulation.py`

Example CLI invocations:

~~~bash
pytest tests/geoprivacy/test_anti_triangulation.py::test_no_exact_parcel_vertex_overlap
pytest tests/geoprivacy/test_anti_triangulation.py::test_no_exact_parcel_centroid_overlap
pytest tests/geoprivacy/test_anti_triangulation.py::test_no_trivial_closest_parcel_mapping
~~~

CI wiring (conceptual YAML snippet for `.github/workflows/kfm-ci.yml`):

~~~yaml
- name: Geoprivacy anti-triangulation tests
  run: |
    pytest tests/geoprivacy/test_anti_triangulation.py
~~~

Any failure in these tests should:

- Fail the CI job.  
- Be treated as a **governance-relevant incident**, requiring review by the appropriate council(s).

---

## 📦 Data & Metadata

This scenario depends on:

- Fixtures:
  - `docs/standards/geospatial/geoprivacy-masking/examples/fixtures/points_sacred_synthetic.geojson`  
  - `docs/standards/geospatial/geoprivacy-masking/examples/fixtures/parcels_synthetic.geojson`  

- Example masking run:
  - `docs/standards/geospatial/geoprivacy-masking/examples/masking-runs/run_2025-12-06T00-00Z_sacred.json`  

Suggested internal scenario metadata (for registries/dashboards):

~~~json
{
  "scenario_id": "geoprivacy-anti-triangulation-v1",
  "standard_ref": "kfm-doc-geoprivacy-masking-v11.2.4",
  "fixtures": [
    "docs/standards/geospatial/geoprivacy-masking/examples/fixtures/points_sacred_synthetic.geojson",
    "docs/standards/geospatial/geoprivacy-masking/examples/fixtures/parcels_synthetic.geojson"
  ],
  "run_manifests": [
    "docs/standards/geospatial/geoprivacy-masking/examples/masking-runs/run_2025-12-06T00-00Z_sacred.json"
  ],
  "tests": [
    "tests/geoprivacy/test_anti_triangulation.py::test_no_exact_parcel_vertex_overlap",
    "tests/geoprivacy/test_anti_triangulation.py::test_no_exact_parcel_centroid_overlap",
    "tests/geoprivacy/test_anti_triangulation.py::test_no_trivial_closest_parcel_mapping"
  ]
}
~~~

This object can be generated or maintained in a CI scenario catalog to track coverage.

---

## 🌐 STAC, DCAT & PROV Alignment

Although this scenario is not itself a dataset, it ties into KFM’s catalog and provenance ecosystem.

### STAC alignment

- Masked sacred Items derived from this scenario’s runs should include:

  - `properties["kfm:masking_run_id"]` pointing to the example run.  
  - `properties["kfm:ci_scenarios"]` including `"geoprivacy-anti-triangulation-v1"`.

Example snippet:

~~~json
{
  "kfm:masking_run_id": "urn:kfm:etl-run:2025-12-06T00:00Z_sacred",
  "kfm:ci_scenarios": [
    "geoprivacy-anti-triangulation-v1",
    "geoprivacy-sovereignty-compliance-v1"
  ]
}
~~~

### DCAT alignment

- Internal QA `dcat:Dataset` records can list applicable CI scenarios in metadata, using:

  - `dct:conformsTo` → geoprivacy standard.  
  - Custom extension property (e.g., `kfm:ci_scenarios`) referencing scenario IDs.

### PROV alignment

- CI runs executing this scenario can be represented as `prov:Activity` instances:

  - `prov:used` → fixtures, masked outputs, this scenario doc.  
  - `prov:generated` → test reports, coverage metrics, badges.  

Example (conceptual):

~~~json
{
  "@id": "urn:kfm:ci-run:geoprivacy-anti-triangulation:2025-12-06T01:00Z",
  "@type": "prov:Activity",
  "prov:used": [
    "urn:kfm:fixture:points_sacred_synthetic",
    "urn:kfm:fixture:parcels_synthetic",
    "kfm-doc-geoprivacy-masking-ci-anti-triangulation-v11.2.4"
  ],
  "prov:wasAssociatedWith": [
    "urn:kfm:service:kfm-ci"
  ]
}
~~~

This supports audits that trace from a dataset or service back to **which CI scenarios were actually run**.

---

## 🗺️ Diagrams

For a high-level picture of this scenario:

~~~mermaid
flowchart LR
    A[Fixtures: sacred points (synthetic)] --> B[Deterministic Donut Masking]
    A2[Fixtures: parcels (synthetic)] --> C[Parcel Geometry Loader]

    B --> D[Masked Sacred Points]
    C --> E[Parcel Vertices & Centroids]

    D --> F[Anti-Triangulation CI Tests]
    E --> F

    F --> G[CI Result & Governance Decision]
~~~

Key takeaway:

- Anti-triangulation tests operate at the **intersection** of masked sacred points and parcel geometry, and their results directly inform governance decisions about whether a deployment is acceptable.

---

## 🧠 Story Node & Focus Mode Integration

This scenario can be surfaced to users (e.g., researchers, community reviewers) through Story Nodes and Focus Mode:

- A Story Node might explain:

  > “Before any dataset containing sacred locations is published, KFM runs automated anti-triangulation tests to ensure masked points cannot be trivially matched to parcel boundaries or centroids.”

- Focus Mode for a dataset can show:

  - Which CI scenarios passed (including this one).  
  - A plain-language summary of what “anti-triangulation” means.  

Guidelines:

- When referencing this scenario in narratives, clearly state that:
  - It uses **synthetic fixtures**, not real sacred coordinates.  
  - It enforces **minimum standards** but does not eliminate the need for human review.  

---

## ⚖ FAIR+CARE & Governance

This CI scenario is a direct embodiment of CARE and sovereignty principles:

- **FAIR**
  - *Findable*: scenario ID and path are stable and referenced from the geoprivacy standard and CI configs.  
  - *Accessible*: documentation and test code are openly available in the repo.  
  - *Interoperable*: scenario metadata references fixtures, manifests, and tests via consistent IDs.  
  - *Reusable*: other projects can adopt similar patterns for triangulation defense.  

- **CARE & sovereignty**
  - Reduces the risk that sacred or sensitive locations can be inferred from public data.  
  - Provides a clear, auditable **checklist** for whether triangulation concerns have been addressed.  
  - Makes it easier for Tribal Sovereignty Boards and FAIR+CARE Council to demand and verify concrete technical controls.

Governance expectations:

- Disabling or weakening this scenario requires:
  - A formal governance review.  
  - Documentation of rationale and compensating controls.  
- Failing this scenario in CI should block deployment of any change that affects masking or parcel-adjacent layers, until mitigations are in place.

---

## 🕰️ Version History

| Version    | Date       | Status            | Notes                                                                                                           |
|-----------:|------------|-------------------|---------------------------------------------------------------------------------------------------------------|
| **v11.2.4** | 2025-12-06 | Active / Enforced | Initial anti-triangulation CI scenario, aligned with geoprivacy-masking v11.2.4; defines tests, fixtures, and governance role. |

Future updates should:

- Refine thresholds and diagnostics based on empirical experience and governance feedback.  
- Extend coverage to additional auxiliary layers (e.g., hydrology, roads) if they become relevant triangulation vectors.  
- Keep scenario ID and semantics stable wherever possible; breaking changes should be versioned and explained.

---

<div align="center">

🧪 **KFM Geoprivacy Masking — CI Scenario: Anti-Triangulation Defense (v11.2.4)**  
Deterministic Tests · Cross-Layer Privacy · FAIR+CARE Sovereignty  

[📘 Docs Root](../../../../../..) · [🧪 CI Scenarios Index](./README.md) · [🛡 Geoprivacy Standard](../../README.md) · [⚖ Governance](../../../../../governance/ROOT-GOVERNANCE.md)

</div>

