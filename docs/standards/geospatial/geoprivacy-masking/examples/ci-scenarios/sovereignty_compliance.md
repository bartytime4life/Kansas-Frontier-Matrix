---
title: "🧪 KFM Geoprivacy Masking — CI Scenario: Sovereignty Compliance"
path: "docs/standards/geospatial/geoprivacy-masking/examples/ci-scenarios/sovereignty_compliance.md"
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

json_schema_ref: "schemas/json/geoprivacy-masking-ci-sovereignty-compliance-v11.2.4.schema.json"
shape_schema_ref: "schemas/shacl/geoprivacy-masking-ci-sovereignty-compliance-v11.2.4-shape.ttl"

story_node_refs: []
immutability_status: "version-pinned"

doc_uuid: "urn:kfm:doc:standards:geoprivacy-masking-ci-sovereignty-compliance-v11.2.4"
semantic_document_id: "kfm-doc-geoprivacy-masking-ci-sovereignty-compliance-v11.2.4"
event_source_id: "ledger:kfm:doc:standards:geoprivacy:examples:ci-scenarios:sovereignty-compliance"

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

# 🧪 KFM Geoprivacy Masking — CI Scenario: Sovereignty Compliance  
v11.2.4 · Sacred-Site Protection · Access Control · Governance-Enforced  

`docs/standards/geospatial/geoprivacy-masking/examples/ci-scenarios/sovereignty_compliance.md`

**Purpose:**  
Define the canonical continuous integration (CI) scenario that verifies **sovereignty compliance** for geoprivacy masking: sacred and sovereignty-governed data must never appear as exposed points in external-facing systems, must be generalized and access-labeled correctly, and must show explicit linkage to KFM sovereignty and geoethics policies.

</div>

---

## 🗂️ Directory Layout

~~~text
📂 docs/standards/geospatial/geoprivacy-masking/examples/
└── 📂 ci-scenarios/
    ├── 📄 README.md                        # CI scenarios index & governance
    ├── 📄 distance_validation.md           # radius window enforcement
    ├── 📄 determinism.md                   # seed stability
    ├── 📄 anti_triangulation.md            # cross-layer de-anonymization defenses
    ├── 📄 sovereignty_compliance.md        # 🪶 This file: sacred & sovereignty compliance
    └── 📄 metadata_provenance.md           # masking metadata & PROV checks
~~~

Related inputs for this scenario:

~~~text
📂 docs/standards/geospatial/geoprivacy-masking/examples/
├── 📂 fixtures/
│   ├── 📄 points_sacred_synthetic.geojson      # Synthetic sacred-site points
│   ├── 📄 h3_regions_sacred_synthetic.geojson  # Generalized H3 regions for sacred fixtures
│   └── 📄 points_kansas_small.geojson          # Mixed-sensitivity baseline (includes sacred)
└── 📂 masking-runs/
    ├── 📄 run_2025-12-06T00-00Z_sacred.json    # Sacred-focused masking run manifest
    └── 📄 run_2025-12-06T00-00Z_sacred_prov.jsonld
~~~

Author rules:

- Any new sacred or sovereignty-related fixture must be declared here and in `fixtures/README.md`.  
- Scenario name and path are treated as stable IDs once referenced in CI and governance dashboards.

---

## 📘 Overview

The geoprivacy standard requires **extra protection** for sacred and sovereignty-governed data:

- Sacred locations are masked with the largest radius window (e.g., 3–10 km).  
- Sacred locations must **not** appear as points at API/frontend level; they must be generalized (e.g., H3 regions or broader polygons).  
- Access labels and sovereignty flags must reflect Tribal and community governance agreements.  
- Sovereignty and Indigenous Data Protection policies must be **enforced in practice**, not just cited.

This CI scenario ensures that:

- Sacred features are generalized and gated correctly.  
- Sovereignty and access labels are present and consistent.  
- No “leaky path” exists where sacred point geometries slip into external-facing layers.

It is a **hard governance gate**: failing this scenario means sacred data is not safe to publish.

---

## 🧭 Context

Within the KFM pipeline:

> Vault / raw data → Deterministic Donut Masking → H3 / polygon generalization (for sacred) → STAC/DCAT & Neo4j → APIs & tiles → Story Nodes & Focus Mode

Sovereignty compliance focuses on:

- The **sacred** sensitivity label (`kfm:sensitivity_label = "sacred"`).  
- Sovereignty and access labeling (e.g., `kfm:access_label = "tribal-only"` or equivalent).  
- Enforcement of **non-point** representations for sacred data beyond secure boundaries.

It complements:

- `distance_validation.md` (distance windows are correct).  
- `determinism.md` (behavior is stable).  
- `anti_triangulation.md` (sacred cannot be trivially re-identified).  
- `metadata_provenance.md` (masking decisions are fully documented).

Here, the focus is **sovereignty, sacredness, and access control**, not just geometry math.

---

## 🧱 Architecture

This scenario uses:

- Sacred fixtures:
  - `examples/fixtures/points_sacred_synthetic.geojson`  
  - `examples/fixtures/h3_regions_sacred_synthetic.geojson`  

- Sacred masking run manifest & PROV:
  - `examples/masking-runs/run_2025-12-06T00-00Z_sacred.json`  
  - `examples/masking-runs/run_2025-12-06T00-00Z_sacred_prov.jsonld`  

Conceptual architecture:

1. **Sacred raw fixtures** represent synthetic sacred points (non-sensitive).  
2. **Masking ETL** applies:
   - Donut masking (large radii).  
   - H3 or polygon generalization for external-facing use.  
3. **Catalog & graph** store:
   - Generalized geometries for sacred data.  
   - Sovereignty and access labels.  
4. **APIs & frontend**:
   - Serve only generalized sacred data.  
   - Enforce access gates (e.g., require roles or internal-only flags).

The scenario’s CI checks target the **post-generalization, pre-publication** boundary: what would actually be exposed if a given change were deployed?

---

## 🧪 Validation & CI/CD

Minimum CI tests for sovereignty compliance are:

### 1. Sacred data must not appear as points in external-facing layers

**Intent:** sacred features must only be exposed as generalized shapes (e.g., polygons, H3 regions) at API/tiles/frontend boundary.

Test sketch:

~~~python
SACRED_LABEL = "sacred"
ALLOWED_GEOMETRY_TYPES = {"Polygon", "MultiPolygon"}  # or H3 index container shapes

def test_sacred_not_exposed_as_points(external_layer_features):
    for rec in external_layer_features:
        label = rec["properties"].get("kfm:sensitivity_label")
        if label != SACRED_LABEL:
            continue
        gtype = rec["geometry"]["type"]
        assert gtype in ALLOWED_GEOMETRY_TYPES, (
            f"Sacred feature {rec['id']} exposed as {gtype}, must be generalized polygon/H3"
        )
~~~

This test runs on features representing **what the APIs/tiles actually serve** for sacred layers (not on internal staging geometries).

### 2. Sacred data must carry sovereignty & access labels

**Intent:** sacred features must be clearly marked as sovereignty-governed and access-restricted.

Example requirements:

- `kfm:access_label` ∈ {`tribal-only`, `restricted`, `withheld`} (project-specific set).  
- `kfm:sovereignty_label` (or equivalent) present and non-empty.  

Test sketch:

~~~python
REQUIRED_SACRED_FIELDS = [
    "kfm:access_label",
    "kfm:sovereignty_label"
]

ALLOWED_SACRED_ACCESS_LABELS = {
    "tribal-only",
    "restricted",
    "withheld"
}

def test_sacred_has_sovereignty_and_access_labels(external_layer_features):
    for rec in external_layer_features:
        label = rec["properties"].get("kfm:sensitivity_label")
        if label != SACRED_LABEL:
            continue
        props = rec["properties"]
        missing = [f for f in REQUIRED_SACRED_FIELDS if f not in props]
        assert not missing, f"Sacred feature {rec['id']} missing: {missing}"

        assert props["kfm:access_label"] in ALLOWED_SACRED_ACCESS_LABELS, (
            f"Sacred feature {rec['id']} has invalid access_label={props['kfm:access_label']}"
        )
~~~

### 3. API/zoom-level gating for sacred layers

**Intent:** even generalized sacred data should be hidden or coarsened at high zoom levels.

CI-style test (API contract simulation):

- Call the sacred layer API at:
  - Very high zoom (e.g., z=15–18).  
  - Medium zoom (e.g., z=8–10).  
- Assert behavior:

  - At high zoom, sacred geometries are either:
    - Not returned at all, or  
    - Returned only as coarse, multi-cell regions.  

Pseudocode sketch (conceptual):

~~~python
def test_sacred_zoom_gating(api_client):
    # High zoom: sacred should not appear with detailed geometry
    resp_high = api_client.get("/tiles/sacred", params={"z": 16, "x": 12345, "y": 56789})
    sacred_features_high = [f for f in resp_high["features"]
                            if f["properties"].get("kfm:sensitivity_label") == SACRED_LABEL]
    assert not sacred_features_high, "Sacred data must not appear at high zoom"

    # Medium zoom: sacred may appear, but as generalized regions
    resp_med = api_client.get("/tiles/sacred", params={"z": 9, "x": 123, "y": 456})
    sacred_features_med = [f for f in resp_med["features"]
                           if f["properties"].get("kfm:sensitivity_label") == SACRED_LABEL]
    for f in sacred_features_med:
        assert f["geometry"]["type"] in ALLOWED_GEOMETRY_TYPES
~~~

Zoom thresholds and behavior (hide vs. coarse shapes) are policy decisions; this CI scenario codifies them.

### 4. Sovereignty policy & governance linkage

**Intent:** ensure that sacred datasets explicitly reference sovereignty policies and governance records.

At minimum:

- STAC/DCAT records for sacred datasets must include a link/field referencing:
  - `sovereignty_policy` from the standard, and/or  
  - A dataset-specific governance reference.

CI test sketch:

~~~python
def test_sacred_catalog_records_reference_sovereignty_policy(sacred_catalog_records):
    for rec in sacred_catalog_records:
        props = rec["properties"]
        # Implementation detail: how sovereignty policy is attached to catalog records
        policy_ref = props.get("kfm:sovereignty_policy_ref")
        assert policy_ref, f"Sacred catalog record {rec['id']} missing sovereignty policy ref"
~~~

### 5. CI wiring

Recommended test module:

- `tests/geoprivacy/test_sovereignty_compliance.py`

Example CLI:

~~~bash
pytest tests/geoprivacy/test_sovereignty_compliance.py::test_sacred_not_exposed_as_points
pytest tests/geoprivacy/test_sovereignty_compliance.py::test_sacred_has_sovereignty_and_access_labels
pytest tests/geoprivacy/test_sovereignty_compliance.py::test_sacred_zoom_gating
pytest tests/geoprivacy/test_sovereignty_compliance.py::test_sacred_catalog_records_reference_sovereignty_policy
~~~

Workflow snippet (conceptual):

~~~yaml
- name: Geoprivacy sovereignty compliance tests
  run: |
    pytest tests/geoprivacy/test_sovereignty_compliance.py
~~~

Any failure is a **hard CI failure** and requires FAIR+CARE + Sovereignty Board review before deployment.

---

## 📦 Data & Metadata

This scenario interacts with:

- **Fixtures**
  - `docs/standards/geospatial/geoprivacy-masking/examples/fixtures/points_sacred_synthetic.geojson`
  - `docs/standards/geospatial/geoprivacy-masking/examples/fixtures/h3_regions_sacred_synthetic.geojson`

- **Run manifests & PROV**
  - `docs/standards/geospatial/geoprivacy-masking/examples/masking-runs/run_2025-12-06T00-00Z_sacred.json`
  - `docs/standards/geospatial/geoprivacy-masking/examples/masking-runs/run_2025-12-06T00-00Z_sacred_prov.jsonld`

- **External-facing representations (test endpoints)**
  - Sacred API/tiles outputs (dev/staging URLs or local mocks).  
  - Sacred STAC/DCAT records (dev catalogs).

Suggested scenario metadata object:

~~~json
{
  "scenario_id": "geoprivacy-sovereignty-compliance-v1",
  "standard_ref": "kfm-doc-geoprivacy-masking-v11.2.4",
  "fixtures": [
    "docs/standards/geospatial/geoprivacy-masking/examples/fixtures/points_sacred_synthetic.geojson",
    "docs/standards/geospatial/geoprivacy-masking/examples/fixtures/h3_regions_sacred_synthetic.geojson"
  ],
  "run_manifests": [
    "docs/standards/geospatial/geoprivacy-masking/examples/masking-runs/run_2025-12-06T00-00Z_sacred.json"
  ],
  "prov_bundles": [
    "docs/standards/geospatial/geoprivacy-masking/examples/masking-runs/run_2025-12-06T00-00Z_sacred_prov.jsonld"
  ],
  "tests": [
    "tests/geoprivacy/test_sovereignty_compliance.py::test_sacred_not_exposed_as_points",
    "tests/geoprivacy/test_sovereignty_compliance.py::test_sacred_has_sovereignty_and_access_labels",
    "tests/geoprivacy/test_sovereignty_compliance.py::test_sacred_zoom_gating",
    "tests/geoprivacy/test_sovereignty_compliance.py::test_sacred_catalog_records_reference_sovereignty_policy"
  ]
}
~~~

This can feed a CI scenario registry / governance dashboard.

---

## 🌐 STAC, DCAT & PROV Alignment

Sovereignty compliance is tightly bound to KFM’s STAC/DCAT/PROV profiles.

### STAC

Sacred Items in dev/QA catalogs should include:

- `properties["kfm:sensitivity_label"] = "sacred"`  
- `properties["kfm:access_label"]` ∈ `{"tribal-only","restricted","withheld"}`  
- `properties["kfm:sovereignty_label"]` (e.g., Tribal/community identifier)  
- `properties["kfm:masking_run_id"]`  
- `properties["kfm:ci_scenarios"]` including `"geoprivacy-sovereignty-compliance-v1"`

CI may parse STAC Items and assert presence and values of these properties.

### DCAT

Sacred QA `dcat:Dataset` records should:

- Use `dct:accessRights` and `dct:rights` consistent with access labels.  
- Reference sovereignty policy docs via extension properties (e.g., `kfm:sovereignty_policy_ref`).  
- `dct:conformsTo` → geoprivacy standard ID.

### PROV

PROV bundles for sacred masking runs should:

- Treat masking as `prov:Activity` with a clear `@id` (same as `kfm:masking_run_id`).  
- Represent sacred masked geometries as `prov:Entity` objects, possibly annotated with:
  - `kfm:sensitivity_label = "sacred"`  
  - `kfm:sovereignty_label`  

CI can:

- Verify that PROV bundles referenced by `kfm:prov_ref` reflect sacred status and run IDs.  
- Ensure there is a `prov:wasInfluencedBy` link to a sovereignty or geoethics policy entity.

---

## 🗺️ Diagrams

High-level sovereignty compliance flow:

~~~mermaid
flowchart LR
    A[Fixtures: sacred points (synthetic)] --> B[Donut Masking (large radii)]
    B --> C[Generalization: H3 / polygons]
    C --> D[STAC/DCAT + Neo4j (sacred)]
    D --> E[APIs & Tiles]
    E --> F[Story Nodes & Focus Mode]

    F --> G[Sovereignty Compliance CI Tests]
    E --> G
    D --> G
~~~

Key idea:

- Sacred data is generalized **before** it touches public-facing systems, and CI ensures this remains true as code evolves.

---

## 🧠 Story Node & Focus Mode Integration

Sovereignty compliance is a narrative topic as much as a technical one:

- Story Nodes can explain, for example:

  > “Sacred and sovereignty-governed places are never shown as exact points. They appear as generalized regions and are governed by Tribal and community agreements.”

- Focus Mode on a sacred-related layer or dataset can show:

  - That `geoprivacy-sovereignty-compliance-v1` passed.  
  - That sacred data is exposed only as generalized shapes.  
  - Links to sovereignty and geoethics documentation (e.g., KFM’s Indigenous Data Protection policy).

Guidelines:

- Avoid any example text that mimics real sacred sites too closely; keep examples clearly synthetic.  
- Emphasize governance and consent (who decides how data is shown), not just technical masking.

---

## ⚖ FAIR+CARE & Governance

Sovereignty compliance is a direct embodiment of CARE principles:

- **FAIR**
  - *Findable*: sacred datasets and their governance status are explorable via metadata.  
  - *Accessible*: access is controlled but policies and high-level summaries remain visible.  
  - *Interoperable*: sovereignty and access labels are aligned with STAC/DCAT/PROV vocabularies.  
  - *Reusable*: data can be reused under clear, explicit governance constraints.

- **CARE & sovereignty**
  - *Collective Benefit*: prevents misuse of sacred data, while still enabling high-level insight and planning.  
  - *Authority to Control*: empowers Tribal and community governance to determine exposure and granularity.  
  - *Responsibility*: CI enforces that implementers cannot “forget” sovereignty rules.  
  - *Ethics*: explicit tests reduce reliance on ad hoc judgment for sacred datasets.

Governance expectations:

- Changing geometry rules, access labels, or zoom gating behaviors for sacred data:
  - Requires updating the geoprivacy standard and this scenario.  
  - Must go through FAIR+CARE Council and Tribal Sovereignty Board review.  
- Any failure in this scenario is a **governance event** and must not be silently overridden.

---

## 🕰️ Version History

| Version    | Date       | Status            | Notes                                                                                                                |
|-----------:|------------|-------------------|----------------------------------------------------------------------------------------------------------------------|
| **v11.2.4** | 2025-12-06 | Active / Enforced | Initial sovereignty compliance CI scenario aligned with geoprivacy-masking v11.2.4; defines sacred generalization, access gating, and governance checks. |

Future updates should:

- Refine zoom-level and geometry rules as mapping practices and community requirements evolve.  
- Extend tests as new sovereignty labels or access patterns are introduced.  
- Maintain stable scenario IDs; create new IDs when semantics or guarantees change substantially.

---

<div align="center">

🧪 **KFM Geoprivacy Masking — CI Scenario: Sovereignty Compliance (v11.2.4)**  
Sacred-Site Protection · Access-Aware Maps · FAIR+CARE Sovereignty  

[📘 Docs Root](../../../../../..) · [🧪 CI Scenarios Index](./README.md) · [🛡 Geoprivacy Standard](../../README.md) · [⚖ Governance](../../../../../governance/ROOT-GOVERNANCE.md)

</div>

