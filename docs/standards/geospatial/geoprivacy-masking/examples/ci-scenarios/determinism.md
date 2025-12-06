---
title: "🧪 KFM Geoprivacy Masking — CI Scenario: Deterministic Stability"
path: "docs/standards/geospatial/geoprivacy-masking/examples/ci-scenarios/determinism.md"
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

json_schema_ref: "schemas/json/geoprivacy-masking-ci-determinism-v11.2.4.schema.json"
shape_schema_ref: "schemas/shacl/geoprivacy-masking-ci-determinism-v11.2.4-shape.ttl"

story_node_refs: []
immutability_status: "version-pinned"

doc_uuid: "urn:kfm:doc:standards:geoprivacy-masking-ci-determinism-v11.2.4"
semantic_document_id: "kfm-doc-geoprivacy-masking-ci-determinism-v11.2.4"
event_source_id: "ledger:kfm:doc:standards:geoprivacy:examples:ci-scenarios:determinism"

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

# 🧪 KFM Geoprivacy Masking — CI Scenario: Deterministic Stability  
v11.2.4 · Seeded Randomness · Reproducible ETL · Governance-Enforced  

`docs/standards/geospatial/geoprivacy-masking/examples/ci-scenarios/determinism.md`

**Purpose:**  
Define the canonical continuous integration (CI) scenario that verifies **deterministic stability** of KFM’s geoprivacy donut masking: given the same inputs and configuration, masked outputs must be identical across ETL runs, ensuring reproducible privacy guarantees, stable catalogs, and PROV-aligned lineage.

</div>

---

## 🗂️ Directory Layout

~~~text
📂 docs/standards/geospatial/geoprivacy-masking/examples/
└── 📂 ci-scenarios/
    ├── 📄 README.md                      # CI scenario index & governance
    ├── 📄 distance_validation.md         # r_min / r_max enforcement
    ├── 📄 determinism.md                 # 🔁 This file: deterministic stability checks
    ├── 📄 anti_triangulation.md          # cross-layer de-anonymization defenses
    ├── 📄 sovereignty_compliance.md      # sacred generalization & access gating
    └── 📄 metadata_provenance.md         # masking metadata & PROV checks
~~~

Related inputs for this scenario:

~~~text
📂 docs/standards/geospatial/geoprivacy-masking/examples/
├── 📂 fixtures/
│   ├── 📄 points_kansas_small.geojson        # Mixed-sensitivity baseline
│   └── 📄 points_sacred_synthetic.geojson    # Synthetic sacred sites
└── 📂 masking-runs/
    ├── 📄 run_2025-12-05T00-00Z.json         # Baseline mixed run manifest
    └── 📄 run_2025-12-06T00-00Z_sacred.json  # Sacred-focused run manifest
~~~

Author rules:

- Any new determinism-focused fixtures or run manifests must be added to the above trees and referenced in this scenario.  
- Scenario file names and paths must remain stable once wired into CI or governance dashboards.

---

## 📘 Overview

Deterministic masking is a **core contract** of the KFM geoprivacy standard:

> Same `(record_id, sensitivity_label, global_salt, configuration)` → same masked coordinates, across time and environments.

This CI scenario exists to:

- Detect any introduction of **non-determinism** in:
  - Masking algorithms,  
  - Random number generator (RNG) configuration,  
  - ETL parameter handling.  
- Provide a **repeatable test harness** using only synthetic fixtures and example run manifests.  
- Support **catalog stability** (STAC/DCAT IDs, H3 indexes, graph node locations) and PROV-aligned lineage.

Passing this scenario is required before changes to masking logic, RNG configuration, or ETL orchestration can be deployed.

---

## 🧭 Context

KFM’s masking pipeline relies on seeded RNG:

> `seed = HMAC_SHA256(secret_salt, record_id)` → seeded RNG → bearing + radius → masked coordinates.

Determinism is critical for:

- **Reprocessing & backfills**  
  - Re-running ETL on the same raw data should not move masked geometries, or previously published maps and Story Nodes would “drift”.

- **Incremental updates**  
  - New records can be added without perturbing previously masked ones.

- **Provenance & auditability**  
  - PROV traces and telemetry rely on stable behavior for the same inputs.

This scenario complements:

- `distance_validation.md` (ensures radius windows), and  
- `anti_triangulation.md` (ensures spatial privacy when combining layers).

Here we focus solely on **same inputs → same outputs**.

---

## 🧱 Architecture

This CI scenario uses:

- Fixtures:
  - `examples/fixtures/points_kansas_small.geojson`  
  - `examples/fixtures/points_sacred_synthetic.geojson`  

- Example masking runs:
  - `examples/masking-runs/run_2025-12-05T00-00Z.json` (baseline mixed).  
  - `examples/masking-runs/run_2025-12-06T00-00Z_sacred.json` (sacred-focused).  

High-level pattern:

1. Load fixtures.  
2. Run the masking function twice with **identical** configuration:
   - Same `secret_salt` (from test config, not committed secrets).  
   - Same algorithm version and parameters.  
3. Compare outputs:
   - Coordinates, IDs, metadata.  
4. Optionally, compare to a **golden output** stored in test data for regression checks.

Any divergence indicates a loss of determinism and must fail CI.

---

## 🧪 Validation & CI/CD

This section defines the minimum CI tests for deterministic stability.

### 1. Same-run determinism (two passes, one config)

**Intent:** ensure masking is deterministic within the same environment for the same run configuration.

Pseudocode (Python-style):

~~~python
def test_determinism_same_run(mask_func, fixtures, config):
    # First pass
    first = {}
    for rec in fixtures:
        first[rec["id"]] = mask_func(rec, config)

    # Second pass with identical config
    second = {}
    for rec in fixtures:
        second[rec["id"]] = mask_func(rec, config)

    assert first == second, "Masked outputs differ across repeated runs with identical config"
~~~

Test coverage:

- Run separately for:
  - `points_kansas_small.geojson` (mixed labels).  
  - `points_sacred_synthetic.geojson` (sacred behavior).

### 2. Cross-run determinism (replay from manifest)

**Intent:** confirm that re-running a masking run using its manifest yields the **same outputs**.

Approach:

- Use run manifest (e.g., `run_2025-12-05T00-00Z.json`) to:
  - Load fixtures.  
  - Configure masking parameters (radius profiles, `max_retries`, ellipsoid, etc.).  
- Run masking and compare against:
  - Previously stored masked output (e.g., a golden file), or  
  - A hash of outputs recorded in the manifest.

Pseudocode:

~~~python
def test_determinism_from_manifest(mask_func, load_manifest, load_golden):
    manifest = load_manifest("run_2025-12-05T00-00Z.json")
    fixtures = load_fixtures(manifest["fixtures"])
    config = config_from_manifest(manifest)

    current = {
        rec["id"]: mask_func(rec, config)
        for rec in fixtures
    }

    golden = load_golden("run_2025-12-05T00-00Z_golden.geojson")

    assert current == golden, "Current masking output diverges from golden baseline"
~~~

Implementation notes:

- Golden outputs must not contain any real sensitive coordinates; they are derived from **synthetic fixtures** only.  
- If golden files are not feasible, manifests may instead store:
  - Hashes of sorted coordinate lists,  
  - Or distance distributions that can be compared.

### 3. Sensitivity to configuration changes

**Intent:** detect unintended configuration-dependent non-determinism (e.g., default parameter changes).

Pattern:

- Use a **minimal config** plus optional explicit overrides.  
- Ensure that changing irrelevant parameters (e.g., logging verbosity) does **not** change masked coordinates.

Pseudocode sketch:

~~~python
def test_irrelevant_config_changes_do_not_affect_output(mask_func, fixtures, base_config):
    cfg1 = {**base_config, "log_level": "INFO"}
    cfg2 = {**base_config, "log_level": "DEBUG"}

    out1 = {rec["id"]: mask_func(rec, cfg1) for rec in fixtures}
    out2 = {rec["id"]: mask_func(rec, cfg2) for rec in fixtures}

    assert out1 == out2, "Non-functional config change altered masked outputs"
~~~

### 4. CI integration

Recommended test module:

- `tests/geoprivacy/test_determinism.py`

Example CLI invocations:

~~~bash
pytest tests/geoprivacy/test_determinism.py::test_determinism_same_run
pytest tests/geoprivacy/test_determinism.py::test_determinism_from_manifest
pytest tests/geoprivacy/test_determinism.py::test_irrelevant_config_changes_do_not_affect_output
~~~

Workflow hook (conceptual):

~~~yaml
- name: Geoprivacy determinism tests
  run: |
    pytest tests/geoprivacy/test_determinism.py
~~~

Any failure should block merge/deploy and trigger review, as it implies a potential break in the **deterministic ETL contract**.

---

## 📦 Data & Metadata

This scenario depends on:

- Fixtures:
  - `docs/standards/geospatial/geoprivacy-masking/examples/fixtures/points_kansas_small.geojson`  
  - `docs/standards/geospatial/geoprivacy-masking/examples/fixtures/points_sacred_synthetic.geojson`  

- Example masking runs:
  - `docs/standards/geospatial/geoprivacy-masking/examples/masking-runs/run_2025-12-05T00-00Z.json`  
  - `docs/standards/geospatial/geoprivacy-masking/examples/masking-runs/run_2025-12-06T00-00Z_sacred.json`  

Suggested scenario metadata object:

~~~json
{
  "scenario_id": "geoprivacy-determinism-v1",
  "standard_ref": "kfm-doc-geoprivacy-masking-v11.2.4",
  "fixtures": [
    "docs/standards/geospatial/geoprivacy-masking/examples/fixtures/points_kansas_small.geojson",
    "docs/standards/geospatial/geoprivacy-masking/examples/fixtures/points_sacred_synthetic.geojson"
  ],
  "run_manifests": [
    "docs/standards/geospatial/geoprivacy-masking/examples/masking-runs/run_2025-12-05T00-00Z.json",
    "docs/standards/geospatial/geoprivacy-masking/examples/masking-runs/run_2025-12-06T00-00Z_sacred.json"
  ],
  "tests": [
    "tests/geoprivacy/test_determinism.py::test_determinism_same_run",
    "tests/geoprivacy/test_determinism.py::test_determinism_from_manifest",
    "tests/geoprivacy/test_determinism.py::test_irrelevant_config_changes_do_not_affect_output"
  ]
}
~~~

This can feed a CI scenario registry or QA dashboard.

---

## 🌐 STAC, DCAT & PROV Alignment

Deterministic behavior ties directly into catalog and provenance semantics.

### STAC alignment

- Masked Items should record `kfm:masking_run_id`, which is stable if masking is deterministic.  
- CI can assert that re-running a known `kfm:masking_run_id` does **not** change STAC IDs or geometry.

Example STAC properties snippet:

~~~json
{
  "kfm:masking_run_id": "urn:kfm:etl-run:2025-12-05T00:00Z",
  "kfm:privacy_method": "donut_geomask_v1",
  "kfm:ci_scenarios": [
    "geoprivacy-determinism-v1"
  ]
}
~~~

### DCAT alignment

- A `dcat:Dataset` that declares conformance to the geoprivacy standard can also reference the determinism scenario via a KFM extension property (e.g., `kfm:ci_scenarios`).

### PROV alignment

- Deterministic masking expectations are encoded in PROV as:
  - Stable `prov:Activity` (`run_id`) and consistent `prov:generated` entities (masked outputs).  
- CI runs for this scenario can be represented as separate `prov:Activity` instances (CI activities), linked to:
  - The masking `prov:Activity`.  
  - The determinism scenario document (this file).

This enables audits tracing from a dataset back to:

- The masking run that generated it.  
- The CI runs that verified determinism.

---

## 🗺️ Diagrams

A high-level view of the determinism scenario:

~~~mermaid
flowchart LR
    A[Fixtures: points_kansas_small<br/>+ points_sacred_synthetic] --> B[Masking ETL Run 1]
    A --> C[Masking ETL Run 2]

    B --> D[Masked Output 1]
    C --> E[Masked Output 2]

    D --> F[Determinism CI Tests]
    E --> F

    F --> G[CI Result & Governance Decision]
~~~

Key point:

- For fixed inputs/config, **D and E must be identical**; otherwise CI fails and governance review is required.

---

## 🧠 Story Node & Focus Mode Integration

Determinism is important to explain to non-engineering stakeholders:

- Story Nodes can describe, for example:

  > “When we rerun our systems on the same data, masked locations do not move. This stability is enforced by automated determinism tests.”

- Focus Mode for a dataset or layer can indicate that:
  - It conforms to `geoprivacy-determinism-v1`.  
  - Last determinism CI run passed at a specific time.

Guidelines:

- Narrative references should:
  - Emphasize **stability and predictability** as a trust feature.  
  - Make clear that deterministic behavior applies to **masked outputs**, not to any hypothetical unmasked locations.  

---

## ⚖ FAIR+CARE & Governance

Deterministic CI checks support FAIR+CARE in several ways:

- **FAIR**
  - *Findable*: stable masked geometries and IDs make catalog references persistent.  
  - *Accessible*: users can reliably re-acquire the same masked dataset given its identifiers.  
  - *Interoperable*: deterministic behavior makes it easier to align with external catalogs and graphs.  
  - *Reusable*: analyses built on masked datasets remain valid across reprocessing runs.

- **CARE & sovereignty**
  - Deterministic masking ensures that sovereignty-driven decisions (e.g., how far to mask sacred sites) are applied **consistently over time**, not subject to random drift.  
  - Governance bodies can review a single algorithm and configuration, knowing that it will behave repeatably.

Governance expectations:

- Changes to masking algorithms, RNG libraries, or configuration logic that could affect determinism must:
  - Update this scenario and associated tests where needed.  
  - Undergo FAIR+CARE and sovereignty review.  
- Failing this scenario in CI is a **governance event**, not just a technical bug.

---

## 🕰️ Version History

| Version    | Date       | Status            | Notes                                                                                                       |
|-----------:|------------|-------------------|-------------------------------------------------------------------------------------------------------------|
| **v11.2.4** | 2025-12-06 | Active / Enforced | Initial determinism CI scenario aligned with geoprivacy-masking v11.2.4; defines tests, fixtures, and governance role. |

Future updates should:

- Refine tests as new masking methods or sensitivity labels are added.  
- Add additional checks for cross-environment determinism (e.g., container image changes, library upgrades).  
- Maintain stable scenario IDs; use new IDs for breaking conceptual changes.

---

<div align="center">

🧪 **KFM Geoprivacy Masking — CI Scenario: Deterministic Stability (v11.2.4)**  
Seeded Randomness · Reproducible Privacy · FAIR+CARE Sovereignty  

[📘 Docs Root](../../../../../..) · [🧪 CI Scenarios Index](./README.md) · [🛡 Geoprivacy Standard](../../README.md) · [⚖ Governance](../../../../../governance/ROOT-GOVERNANCE.md)

</div>

