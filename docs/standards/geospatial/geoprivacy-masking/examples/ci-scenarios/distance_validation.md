---
title: "🧪 KFM Geoprivacy Masking — CI Scenario: Distance Validation"
path: "docs/standards/geospatial/geoprivacy-masking/examples/ci-scenarios/distance_validation.md"
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

json_schema_ref: "schemas/json/geoprivacy-masking-ci-distance-validation-v11.2.4.schema.json"
shape_schema_ref: "schemas/shacl/geoprivacy-masking-ci-distance-validation-v11.2.4-shape.ttl"

story_node_refs: []
immutability_status: "version-pinned"

doc_uuid: "urn:kfm:doc:standards:geoprivacy-masking-ci-distance-validation-v11.2.4"
semantic_document_id: "kfm-doc-geoprivacy-masking-ci-distance-validation-v11.2.4"
event_source_id: "ledger:kfm:doc:standards:geoprivacy:examples:ci-scenarios:distance-validation"

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

# 🧪 KFM Geoprivacy Masking — CI Scenario: Distance Validation  
v11.2.4 · Radius Windows · Metric-First Privacy · Governance-Enforced  

`docs/standards/geospatial/geoprivacy-masking/examples/ci-scenarios/distance_validation.md`

**Purpose:**  
Define the canonical continuous integration (CI) scenario that verifies **distance-based correctness** of KFM’s deterministic donut masking: every masked geometry must fall within the approved `[r_min, r_max]` window for its sensitivity label, ensuring that privacy guarantees are actually enforced in meters on the ground.

</div>

---

## 🗂️ Directory Layout

~~~text
📂 docs/standards/geospatial/geoprivacy-masking/examples/
└── 📂 ci-scenarios/
    ├── 📄 README.md                      # CI scenarios index & governance
    ├── 📄 distance_validation.md         # 🎯 This file: radius window enforcement
    ├── 📄 determinism.md                 # seed stability
    ├── 📄 anti_triangulation.md          # cross-layer de-anonymization defenses
    ├── 📄 sovereignty_compliance.md      # sacred generalization & access gating
    └── 📄 metadata_provenance.md         # masking metadata & PROV checks
~~~

Related inputs for this scenario:

~~~text
📂 docs/standards/geospatial/geoprivacy-masking/examples/
├── 📂 fixtures/
│   ├── 📄 points_kansas_small.geojson        # Mixed-sensitivity baseline (public/community/sensitive/sacred)
│   └── 📄 points_sacred_synthetic.geojson    # Additional sacred-focused fixtures (optional)
└── 📂 masking-runs/
    └── 📄 run_2025-12-05T00-00Z.json         # Baseline mixed run manifest (radius profiles)
~~~

Author rules:

- Any new fixture or run manifest used for distance validation must be added to the above trees and referenced in this scenario.  
- Scenario naming and path are considered **stable IDs** once wired into CI and governance dashboards.

---

## 📘 Overview

The geoprivacy standard defines **radius windows** for each sensitivity label, e.g.:

- `public` → 50 m–150 m  
- `community` → 250 m–500 m  
- `sensitive` → 1 km–3 km  
- `sacred` → 3 km–10 km  

This CI scenario ensures that:

- Every masked point’s distance from its original coordinate is **within** the appropriate window for its label.  
- Distribution-level expectations (min, max, mean distance) match what is recorded in example masking run manifests.  
- No changes to algorithms, libraries, or coordinate handling silently break radius constraints.

This is a **hard requirement**: a masked point outside its configured radius window is a privacy-contract violation.

---

## 🧭 Context

This scenario lives in the broader KFM pipeline:

> Fixtures → Deterministic Donut Masking → Masked Outputs + Run Manifests → STAC/DCAT & Neo4j → API → MapLibre/Cesium → Story Nodes & Focus Mode

Where:

- Distance windows are the **quantitative expression** of privacy rules:
  - Smaller windows for low-risk public points.  
  - Larger windows for sensitive and sacred data.  
- Radius constraints protect against:
  - Overly small shifts (easy re-identification).  
  - Overly large shifts (unrealistic positions that mislead or break downstream analysis).

This scenario complements:

- `determinism.md` (same inputs → same outputs).  
- `anti_triangulation.md` (cross-layer de-anonymization defense).  
- `sovereignty_compliance.md` (sacred generalization & access gating).

Here we focus on **metric correctness of the masking distance**.

---

## 🧱 Architecture

The distance validation scenario uses:

- **Fixtures**
  - `examples/fixtures/points_kansas_small.geojson` (main case).  
  - Optionally `examples/fixtures/points_sacred_synthetic.geojson` for extra sacred coverage.

- **Run manifest**
  - `examples/masking-runs/run_2025-12-05T00-00Z.json` to define expected radius profiles and summary statistics.

High-level steps:

1. Load fixtures with original coordinates and sensitivity labels.  
2. Run donut masking with the radius profiles defined in the manifest.  
3. For each feature, compute geodesic distance between original and masked coordinates.  
4. Assert `r_min <= distance <= r_max` based on sensitivity label.  
5. Summarize distances and optionally compare them to statistics recorded in the run manifest.

This scenario is typically implemented as pure test logic in `tests/geoprivacy/test_distance_validation.py`, using geodesic-distance utilities.

---

## 🧪 Validation & CI/CD

This section defines the **minimum CI tests** for distance validation.

### 1. Per-feature distance window check

**Intent:** every masked feature must respect its configured distance window.

Pseudocode:

~~~python
from geopy.distance import geodesic  # or equivalent

RADIUS_TABLE = {
    "public":    {"min_m": 50,   "max_m": 150},
    "community": {"min_m": 250,  "max_m": 500},
    "sensitive": {"min_m": 1000, "max_m": 3000},
    "sacred":    {"min_m": 3000, "max_m": 10000},
}

def distance_m(a, b):
    # a, b: (lat, lon)
    return geodesic(a, b).meters

def test_distance_within_bounds(masked_records):
    for rec in masked_records:
        label = rec["properties"]["kfm:sensitivity_label"]
        r_min = RADIUS_TABLE[label]["min_m"]
        r_max = RADIUS_TABLE[label]["max_m"]

        orig = (rec["properties"]["orig_lat"], rec["properties"]["orig_lon"])
        masked = tuple(reversed(rec["geometry"]["coordinates"]))  # (lat, lon)

        d_m = distance_m(orig, masked)
        assert r_min <= d_m <= r_max, (
            f"{rec['id']} label={label} distance={d_m} outside [{r_min}, {r_max}] m"
        )
~~~

Notes:

- For fixtures, `orig_lat`/`orig_lon` can be stored in properties or linked from a separate structure; the CI harness can decide.  
- This test runs on **masked output derived from fixtures**, not on vault data.

### 2. Summary statistics consistency

**Intent:** ensure summary stats (min, max, mean distances) are within reasonable tolerance of those recorded in the example run manifest.

Pseudocode:

~~~python
import statistics as stats

MAX_ALLOWED_DELTA_M = 5.0  # example tolerance for min/max differences

def test_distance_summary_matches_manifest(masked_records, manifest):
    distances = []
    for rec in masked_records:
        orig = (rec["properties"]["orig_lat"], rec["properties"]["orig_lon"])
        masked = tuple(reversed(rec["geometry"]["coordinates"]))
        distances.append(distance_m(orig, masked))

    observed = {
        "min": min(distances),
        "max": max(distances),
        "mean": stats.mean(distances),
    }

    expected = manifest["summary"]["distance_m"]

    assert abs(observed["min"] - expected["min"]) <= MAX_ALLOWED_DELTA_M
    assert abs(observed["max"] - expected["max"]) <= MAX_ALLOWED_DELTA_M
    # mean can often be looser; tune via config
~~~

Where:

- `manifest` is loaded from `run_2025-12-05T00-00Z.json`.  
- Tolerances can be configured in test config and reviewed by governance bodies.

### 3. Label coverage checks

**Intent:** ensure that all sensitivity labels are present in the fixture set and tested.

Simple test:

~~~python
def test_all_labels_present(masked_records):
    labels = {rec["properties"]["kfm:sensitivity_label"] for rec in masked_records}
    expected = {"public", "community", "sensitive", "sacred"}
    missing = expected - labels
    assert not missing, f"Missing labels in distance validation fixtures: {missing}"
~~~

This guards against accidental changes to fixtures that drop some labels and weaken coverage.

### 4. CI integration

Recommended test module:

- `tests/geoprivacy/test_distance_validation.py`

Example CLI:

~~~bash
pytest tests/geoprivacy/test_distance_validation.py::test_distance_within_bounds
pytest tests/geoprivacy/test_distance_validation.py::test_distance_summary_matches_manifest
pytest tests/geoprivacy/test_distance_validation.py::test_all_labels_present
~~~

Workflow hook (conceptual):

~~~yaml
- name: Geoprivacy distance validation tests
  run: |
    pytest tests/geoprivacy/test_distance_validation.py
~~~

Any failing assertion is a **hard CI failure** and must block merges/deploys touching masking logic, coordinate handling, or geodesic distance utilities.

---

## 📦 Data & Metadata

This scenario primarily interacts with:

- Fixtures:
  - `docs/standards/geospatial/geoprivacy-masking/examples/fixtures/points_kansas_small.geojson`  
  - Optionally `docs/standards/geospatial/geoprivacy-masking/examples/fixtures/points_sacred_synthetic.geojson`  

- Run manifest:
  - `docs/standards/geospatial/geoprivacy-masking/examples/masking-runs/run_2025-12-05T00-00Z.json`  

Suggested scenario metadata object:

~~~json
{
  "scenario_id": "geoprivacy-distance-validation-v1",
  "standard_ref": "kfm-doc-geoprivacy-masking-v11.2.4",
  "fixtures": [
    "docs/standards/geospatial/geoprivacy-masking/examples/fixtures/points_kansas_small.geojson"
  ],
  "run_manifests": [
    "docs/standards/geospatial/geoprivacy-masking/examples/masking-runs/run_2025-12-05T00-00Z.json"
  ],
  "tests": [
    "tests/geoprivacy/test_distance_validation.py::test_distance_within_bounds",
    "tests/geoprivacy/test_distance_validation.py::test_distance_summary_matches_manifest",
    "tests/geoprivacy/test_distance_validation.py::test_all_labels_present"
  ]
}
~~~

This can be ingested into a CI scenario registry for dashboards and governance review.

---

## 🌐 STAC, DCAT & PROV Alignment

Distance validation hooks into KFM’s catalog and provenance layers.

### STAC alignment

Masked Items should record both:

- `kfm:sensitivity_label`  
- `kfm:r_min_m`, `kfm:r_max_m`  

This CI scenario confirms that the distances **actually** lie within these windows.

Example STAC properties snippet (dev/QA):

~~~json
{
  "kfm:sensitivity_label": "sensitive",
  "kfm:r_min_m": 1000,
  "kfm:r_max_m": 3000,
  "kfm:masking_run_id": "urn:kfm:etl-run:2025-12-05T00:00Z",
  "kfm:ci_scenarios": [
    "geoprivacy-distance-validation-v1"
  ]
}
~~~

### DCAT alignment

In DCAT QA catalogs, distance validation can be reflected as:

- `dct:conformsTo` → geoprivacy standard.  
- Custom extension property `kfm:ci_scenarios` referencing this scenario ID.

### PROV alignment

- Masking run `prov:Activity` already encodes geometry derivation.  
- CI runs for this scenario can be modeled as separate `prov:Activity` entities that:
  - `prov:used` → fixtures, masked outputs, this scenario document.  
  - `prov:generated` → test reports and metrics.

This allows auditors to ask:

> “Did datasets derived from run X pass distance validation scenario `geoprivacy-distance-validation-v1`?”

and answer that via PROV queries.

---

## 🗺️ Diagrams

A high-level view of the distance validation scenario:

~~~mermaid
flowchart LR
    A[Fixtures: points_kansas_small] --> B[Deterministic Donut Masking]
    B --> C[Masked Output + Run Manifest]

    C --> D[Compute per-feature distances]
    D --> E[Check r_min / r_max per label]
    C --> F[Compare summary stats to manifest]

    E --> G[CI Result]
    F --> G
~~~

Key points:

- Validation is done against **synthetic fixtures** plus run manifest metadata.  
- Both per-feature and aggregate behavior are checked.

---

## 🧠 Story Node & Focus Mode Integration

Distance validation can be surfaced to users and reviewers:

- Story Nodes might explain:

  > “For each masked location, we verify the distance between the original and masked point falls within label-specific safety windows (e.g., 3–10 km for sacred sites).”

- Focus Mode, when focused on a dataset or layer, can show:

  - The fact that `geoprivacy-distance-validation-v1` has passed.  
  - A short summary of radius windows per label.  
  - Optional high-level statistics (e.g., average masked distance for a dataset).

Guidelines:

- Make it clear that distances refer to **original vs masked** locations, not to real-world features like town centers or roads.  
- Emphasize that larger windows for sacred/sensitive labels reflect **stronger protection** rather than data inaccuracy.

---

## ⚖ FAIR+CARE & Governance

Distance validation directly supports FAIR+CARE principles:

- **FAIR**
  - *Findable*: radius windows and CI scenario IDs are explicitly recorded in metadata.  
  - *Accessible*: tests and their outputs live in the open repo and CI logs.  
  - *Interoperable*: distance constraints map neatly onto STAC/DCAT properties and PROV semantics.  
  - *Reusable*: other projects can adopt the same pattern for geoprivacy checking.

- **CARE & sovereignty**
  - Ensures that promised protection levels (e.g., “sacred sites are shifted 3–10 km”) are enforced in practice.  
  - Provides sovereign partners with **quantitative evidence** about masking behavior.  
  - Makes it harder for regressions to silently weaken protection for sensitive and sacred locations.

Governance expectations:

- Changing radius windows or distance tolerance thresholds:
  - Requires updating this scenario and the geoprivacy standard.  
  - Must go through FAIR+CARE and sovereignty review.  
- Failing this scenario is a **governance event**, not just a technical bug.

---

## 🕰️ Version History

| Version    | Date       | Status            | Notes                                                                                                   |
|-----------:|------------|-------------------|---------------------------------------------------------------------------------------------------------|
| **v11.2.4** | 2025-12-06 | Active / Enforced | Initial distance validation CI scenario aligned with geoprivacy-masking v11.2.4; defines tests, fixtures, and governance role. |

Future updates should:

- Refine distance thresholds and tolerances based on field experience and governance feedback.  
- Extend coverage as new sensitivity labels or masking profiles are added.  
- Maintain stable scenario IDs; introduce new IDs for conceptually breaking changes.

---

<div align="center">

🧪 **KFM Geoprivacy Masking — CI Scenario: Distance Validation (v11.2.4)**  
Metric-First Privacy · Deterministic Checks · FAIR+CARE Sovereignty  

[📘 Docs Root](../../../../../..) · [🧪 CI Scenarios Index](./README.md) · [🛡 Geoprivacy Standard](../../README.md) · [⚖ Governance](../../../../../governance/ROOT-GOVERNANCE.md)

</div>

