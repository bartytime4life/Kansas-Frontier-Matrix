---
title: "🧪 KFM Geoprivacy Masking — CI Scenario Guide"
path: "docs/standards/geospatial/geoprivacy-masking/examples/ci-scenarios/README.md"
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
  - "docs/standards/geospatial/geoprivacy-masking/examples/fixtures/README.md@v11.2.4"
  - "docs/standards/geospatial/geoprivacy-masking/examples/masking-runs/README.md@v11.2.4"

provenance_requirements:
  versions_required: false
  newest_first: true
  must_reference_superseded: false
  must_reference_origin_root: true

json_schema_ref: "schemas/json/geoprivacy-masking-ci-scenarios-v11.2.4.schema.json"
shape_schema_ref: "schemas/shacl/geoprivacy-masking-ci-scenarios-v11.2.4-shape.ttl"

story_node_refs: []
immutability_status: "version-pinned"

doc_uuid: "urn:kfm:doc:standards:geoprivacy-masking-ci-scenarios-v11.2.4"
semantic_document_id: "kfm-doc-geoprivacy-masking-ci-scenarios-v11.2.4"
event_source_id: "ledger:kfm:doc:standards:geoprivacy:examples:ci-scenarios"

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

# 🧪 KFM Geoprivacy Masking — CI Scenario Guide  
v11.2.4 · Deterministic Tests · Governance-Enforced · FAIR+CARE Aligned  

`docs/standards/geospatial/geoprivacy-masking/examples/ci-scenarios/README.md`

**Purpose:**  
Define the canonical continuous integration (CI) scenarios for KFM’s Geospatial Privacy & Cultural-Safety Masking Standard, linking fixtures and masking run manifests to concrete test cases that enforce distance bounds, determinism, anti-triangulation, sovereignty rules, and metadata/provenance requirements across the ETL → STAC/DCAT → Neo4j → API → frontend pipeline.

</div>

---

## 🗂️ Directory Layout

~~~text
📂 docs/standards/geospatial/geoprivacy-masking/examples/
└── 📂 ci-scenarios/
    ├── 📄 README.md                     # 🧪 This guide: CI scenarios index & governance
    ├── 📄 distance_validation.md        # Scenario: r_min / r_max enforcement across labels
    ├── 📄 determinism.md                # Scenario: seed stability & reproducibility
    ├── 📄 anti_triangulation.md         # Scenario: cross-layer de-anonymization defenses
    ├── 📄 sovereignty_compliance.md     # Scenario: sacred data generalization & access gating
    └── 📄 metadata_provenance.md        # Scenario: masking metadata & PROV alignment checks
~~~

Author rules:

- Each scenario file in this directory must describe:
  - **Inputs** (fixtures + masking runs),  
  - **Expected behavior** (what CI must assert), and  
  - **Failure conditions** (what constitutes a governance violation).  
- Scenario names should remain stable once referenced by CI workflows or Story Nodes.  
- New scenarios must be added to this layout block and, where relevant, to the main examples index.

---

## 📘 Overview

This guide turns the geoprivacy standard into **executable CI scenarios** that:

- Verify that deterministic donut geomasking behaves as specified for all sensitivity labels.  
- Guard against regressions in masking logic, sovereignty enforcement, and metadata recording.  
- Provide a human-readable map from high-level principles to specific tests wired into `kfm-ci`.  

The scenarios here are:

- **Normative for example-based CI**: any KFM environment that uses the provided fixtures and manifests should treat these scenarios as required.  
- **Complementary** to production-scale monitoring and telemetry, not a replacement for them.

Core normative rules (masking method, radius windows, forbidden techniques) live in:

- `docs/standards/geospatial/geoprivacy-masking/README.md`  

This guide tells CI **how to enforce** those rules using the example artifacts under `examples/`.

---

## 🧭 Context

The geoprivacy CI stack follows the KFM pipeline:

> Fixtures → Masking ETL → Masked outputs + run manifests + PROV → STAC/DCAT + Neo4j + APIs → UI layers → Story Nodes & Focus Mode

CI scenarios in this directory:

- Bind together:
  - Fixtures (`examples/fixtures/`),  
  - Run manifests (`examples/masking-runs/`), and  
  - Specific assertions against outputs (distance, determinism, metadata, provenance).  
- Are referenced from:
  - `.github/workflows/kfm-ci.yml` via test commands,  
  - Documentation and governance reviews as a **single source of truth** for “what CI checks geoprivacy”.

Use this guide when:

- Adding or modifying geoprivacy-related tests.  
- Explaining CI behavior to FAIR+CARE Council or Tribal Sovereignty Board.  
- Extending masking to new geometry types or labels and updating tests accordingly.

---

## 🧱 Architecture

The CI scenarios are structured along key behavioral dimensions:

1. **Distance bounds (distance_validation.md)**  
   - Ensures masked points respect `[r_min, r_max]` per sensitivity label.  
   - Uses mixed-sensitivity fixtures and baseline masking run manifests.

2. **Determinism (determinism.md)**  
   - Asserts that same `(record_id, label, salt)` yields identical masked coordinates across runs.  
   - Protects against accidental introduction of non-determinism in ETL or RNG configuration.

3. **Anti-triangulation (anti_triangulation.md)**  
   - Ensures that combining masked layers (e.g., points + parcels) cannot trivially re-identify original locations.  
   - Focuses on sacred and sensitive fixtures.

4. **Sovereignty compliance (sovereignty_compliance.md)**  
   - Verifies that sacred data is never exposed as points and is properly generalized (H3 / polygons).  
   - Checks for required sovereignty flags and access labels.

5. **Metadata & provenance (metadata_provenance.md)**  
   - Ensures that masking metadata (`kfm:privacy_method`, `kfm:sensitivity_label`, etc.) and PROV links (`kfm:prov_ref`) are present and consistent.  
   - Cross-checks manifests, fixtures, and PROV bundles.

Each scenario document should:

- Reference the **specific fixtures and runs** it uses.  
- Define **CLI examples** for running tests locally.  
- Map scenario outcomes to **governance implications** (e.g., block deploy vs. warning).

---

## 🧪 Validation & CI/CD

The scenarios in this directory map directly into CI pipelines.

### 1. Distance validation scenario

- **File:** `distance_validation.md`  
- **Goal:** enforce radius windows per label.

Typical CI behavior:

- Load fixtures from `fixtures/points_kansas_small.geojson`.  
- Load corresponding masking run manifest (e.g., `run_2025-12-05T00-00Z.json`).  
- For each record:
  - Compute geodesic distance between original and masked coordinates.  
  - Assert `r_min <= distance <= r_max` for that record’s sensitivity label.  

Failure conditions:

- Any point falls outside its configured radius window.  
- Summary stats in manifest diverge from recomputed values beyond defined tolerances.

### 2. Determinism scenario

- **File:** `determinism.md`  
- **Goal:** guarantee stable masked outputs given fixed inputs and salt.

Typical CI behavior:

- Run masking ETL twice over the same fixtures (`points_kansas_small.geojson`, `points_sacred_synthetic.geojson`) with identical configuration.  
- Compare masked outputs (feature IDs and coordinates).  
- Assert exact equality.

Failure conditions:

- Any coordinate or derived ID differs between runs.  
- Run manifests disagree on summary stats for the same configuration.

### 3. Anti-triangulation scenario

- **File:** `anti_triangulation.md`  
- **Goal:** prevent trivial re-identification via layer intersections.

Typical CI behavior:

- Use masked outputs based on:
  - `fixtures/points_sacred_synthetic.geojson`  
  - `fixtures/parcels_synthetic.geojson`  
- Assertions may include:
  - No masked point exactly coincides with a parcel vertex or centroid.  
  - No one-to-one mapping from masked points to unique parcels that would trivially reveal original locations.  

Failure conditions:

- Any exact coordinate overlap with parcel vertices.  
- Detected patterns that violate anti-triangulation thresholds defined in the scenario doc.

### 4. Sovereignty compliance scenario

- **File:** `sovereignty_compliance.md`  
- **Goal:** enforce high-protection behavior for sacred data.

Typical CI behavior:

- Inspect masked outputs derived from `points_sacred_synthetic.geojson` and associated H3 regions.  
- Assert:
  - No sacred feature is exposed as a `Point` at API/frontend layer.  
  - Sacred data appears only as generalized polygons or H3 index regions.  
  - Required sovereignty and access labels are present on Items and graph nodes.

Failure conditions:

- Any sacred entity appears as a point in external-facing layers.  
- Missing sovereignty flags or access labels for sacred datasets.

### 5. Metadata & provenance scenario

- **File:** `metadata_provenance.md`  
- **Goal:** ensure masking metadata and PROV links are complete and consistent.

Typical CI behavior:

- Sample masked Items and check for required fields:
  - `kfm:privacy_method`  
  - `kfm:sensitivity_label`  
  - `kfm:r_min_m`, `kfm:r_max_m`  
  - `kfm:masking_run_id`  
  - `kfm:prov_ref`  
- Verify that:
  - `kfm:masking_run_id` matches a known run manifest.  
  - `kfm:prov_ref` points to a valid PROV bundle referencing the same `run_id`.

Failure conditions:

- Missing or malformed masking metadata.  
- Orphaned PROV references or mismatches between manifests and bundles.

---

## 📦 Data & Metadata

CI scenarios themselves are documentation artifacts but refer heavily to data/metadata:

- **Scenario → fixtures mapping**  
  - Each scenario must list the fixture files it depends on.  
- **Scenario → run manifest mapping**  
  - Where applicable, scenarios should refer to `run_*.json` manifests.  
- **Scenario → tests mapping**  
  - Each scenario should name the test modules/functions (e.g., `tests/geoprivacy/test_distance_validation.py`) that implement it.

A simple scenario metadata pattern (inside each scenario doc or as YAML front-matter if desired):

~~~json
{
  "scenario_id": "geoprivacy-distance-validation-v1",
  "fixtures": [
    "docs/standards/geospatial/geoprivacy-masking/examples/fixtures/points_kansas_small.geojson"
  ],
  "run_manifests": [
    "docs/standards/geospatial/geoprivacy-masking/examples/masking-runs/run_2025-12-05T00-00Z.json"
  ],
  "tests": [
    "tests/geoprivacy/test_distance_validation.py::test_distance_within_bounds"
  ]
}
~~~

This pattern supports automatic extraction into a CI scenario registry or a QA dashboard.

---

## 🌐 STAC, DCAT & PROV Alignment

While CI scenario docs are not spatial datasets, they sit in the same **metadata universe**:

- **STAC**  
  - Scenarios can be referenced in STAC Collections or Items as:
    - `kfm:ci_scenarios` listing scenario IDs relevant to a dataset.  

- **DCAT**  
  - CI scenarios may appear as part of a `dcat:Dataset` describing QA/validation processes.  
  - Link them to the geoprivacy standard via `dct:conformsTo`.

- **PROV**  
  - CI runs that execute these scenarios can be modeled as `prov:Activity` entities:
    - `prov:used` → fixtures, manifests, scenario docs.  
    - `prov:generated` → test reports, badges, telemetry entries.  

This alignment allows audits to trace from a production dataset or Story Node **back** to:

- The standard it conforms to.  
- The CI scenarios that enforce that standard.  
- The test results for those scenarios.

---

## 🧠 Story Node & Focus Mode Integration

CI scenarios are also narrative material:

- Story Nodes can:
  - Describe “how we test geoprivacy” using scenario IDs and outcomes.  
  - Anchor explanations to concrete test runs, not vague claims.

- Focus Mode can:
  - Summarize which geoprivacy scenarios a given dataset or service has passed.  
  - Highlight gaps (e.g., “Anti-triangulation scenario not configured for this layer”).

Guidelines:

- Scenario docs should use **clear, non-technical language** alongside technical details so Focus Mode summaries are understandable to non-engineers.  
- Avoid referencing any real sensitive data in examples; keep everything anchored to synthetic fixtures and example runs.

---

## ⚖ FAIR+CARE & Governance

These CI scenarios are a **governance mechanism**:

- **FAIR**
  - *Findable*: scenario docs have stable paths, IDs, and references from standards and examples.  
  - *Accessible*: stored in the public repo under an open license.  
  - *Interoperable*: reference fixtures, manifests, and tests via consistent identifiers.  
  - *Reusable*: can be applied across environments (dev/staging/prod) with minimal changes.

- **CARE & sovereignty**
  - Scenario coverage ensures that sacred and sensitive data handling is not left to ad hoc judgment.  
  - Explicit tests for sovereignty compliance operationalize policy documents.  
  - Failures in these scenarios should be treated as **governance events**, not just engineering bugs.

Any change that weakens CI coverage (e.g., removing a scenario, relaxing thresholds) must:

- Be documented in this file and the relevant scenario doc.  
- Go through the same governance review channels as changes to the underlying standard.

---

## 🕰️ Version History

| Version    | Date       | Status            | Notes                                                                                                      |
|-----------:|------------|-------------------|------------------------------------------------------------------------------------------------------------|
| **v11.2.4** | 2025-12-06 | Active / Enforced | Initial CI scenario guide aligned with geoprivacy-masking v11.2.4; defines scenario set and governance role. |

Future updates should:

- Add new scenarios only when they cover distinct behaviors (e.g., new geometry types, new sensitivity labels).  
- Keep scenario names, IDs, and referenced fixtures stable where possible to avoid brittle CI.  
- Document any governance-impacting changes (e.g., raising/lowering thresholds, expanding anti-triangulation checks).

---

<div align="center">

🧪 **KFM Geoprivacy Masking — CI Scenario Guide (v11.2.4)**  
Deterministic Tests · Transparent Governance · FAIR+CARE Ethics  

[📘 Docs Root](../../../../../..) · [🧪 Examples Index](../README.md) · [🛡 Geoprivacy Standard](../../README.md) · [⚖ Governance](../../../../../governance/ROOT-GOVERNANCE.md)

</div>

