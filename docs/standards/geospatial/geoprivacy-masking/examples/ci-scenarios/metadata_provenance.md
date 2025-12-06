---
title: "🧪 KFM Geoprivacy Masking — CI Scenario: Metadata & PROV Alignment"
path: "docs/standards/geospatial/geoprivacy-masking/examples/ci-scenarios/metadata_provenance.md"
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

json_schema_ref: "schemas/json/geoprivacy-masking-ci-metadata-provenance-v11.2.4.schema.json"
shape_schema_ref: "schemas/shacl/geoprivacy-masking-ci-metadata-provenance-v11.2.4-shape.ttl"

story_node_refs: []
immutability_status: "version-pinned"

doc_uuid: "urn:kfm:doc:standards:geoprivacy-masking-ci-metadata-provenance-v11.2.4"
semantic_document_id: "kfm-doc-geoprivacy-masking-ci-metadata-provenance-v11.2.4"
event_source_id: "ledger:kfm:doc:standards:geoprivacy:examples:ci-scenarios:metadata-provenance"

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

# 🧪 KFM Geoprivacy Masking — CI Scenario: Metadata & PROV Alignment  
v11.2.4 · Catalog-Ready Privacy · Provenance-First · Governance-Enforced  

`docs/standards/geospatial/geoprivacy-masking/examples/ci-scenarios/metadata_provenance.md`

**Purpose:**  
Define the canonical continuous integration (CI) scenario that verifies **masking metadata completeness** and **PROV-O alignment** for geoprivacy operations: every masked geometry, STAC/DCAT record, and graph node must carry the required `kfm:*` privacy fields and valid `kfm:prov_ref` links so that geoprivacy is fully auditable and catalog-ready across KFM.

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
    ├── 📄 sovereignty_compliance.md        # sacred generalization & access gating
    └── 📄 metadata_provenance.md           # 📦 This file: masking metadata & PROV checks
~~~

Related inputs for this scenario:

~~~text
📂 docs/standards/geospatial/geoprivacy-masking/examples/
├── 📂 fixtures/
│   ├── 📄 points_kansas_small.geojson          # Mixed-sensitivity baseline
│   ├── 📄 points_sacred_synthetic.geojson      # Synthetic sacred sites
│   └── 📄 parcels_synthetic.geojson            # For cross-layer metadata checks (optional)
└── 📂 masking-runs/
    ├── 📄 run_2025-12-05T00-00Z.json           # Baseline masking run manifest
    ├── 📄 run_2025-12-06T00-00Z_sacred.json    # Sacred-focused masking run manifest
    └── 📄 run_2025-12-05T00-00Z_prov.jsonld    # Example PROV bundle (baseline)
~~~

Author rules:

- Any new masking metadata or PROV field added to the standard must be reflected in this scenario and its tests.  
- New PROV bundles or run manifests used in this scenario must be listed in the layout above and referenced in the tests section.

---

## 📘 Overview

Geoprivacy in KFM is not just about shifting points; it’s about **traceable, cataloged decisions**:

- Masked geometries must expose **how** they were masked (method, radii, sensitivity).  
- Catalog records (STAC/DCAT) must indicate that masking occurred and under which standard.  
- PROV bundles must capture **who/what/when** for each masking run.

This CI scenario ensures that:

1. Masked features carry required `kfm:*` masking metadata.  
2. STAC-like records expose the same metadata consistently.  
3. `kfm:prov_ref` links are present and point to valid PROV-O documents.  
4. Run manifests, masked records, and PROV bundles are **mutually consistent**.

If this scenario fails, geoprivacy becomes opaque and un-auditable — a governance violation.

---

## 🧭 Context

This scenario operates across multiple layers:

> Fixtures → Masking ETL → Masked GeoJSON + Run Manifests + PROV Bundles → STAC/DCAT → Neo4j → APIs → Story Nodes / Focus Mode

Key metadata & provenance elements:

- **Per-feature masking metadata** (in GeoJSON / STAC properties), e.g.:

  - `kfm:privacy_method`  
  - `kfm:sensitivity_label`  
  - `kfm:r_min_m`, `kfm:r_max_m`  
  - `kfm:masking_run_id`  
  - `kfm:prov_ref`  
  - `kfm:access_label` and sovereignty/geoethics fields where applicable  

- **Run manifests** (JSON control plane), including:

  - `run_id`, `standard_ref`, `radius_profiles`, `summary.*`.  

- **PROV bundles** (JSON-LD), including:

  - Masking `prov:Activity` (`run_id`).  
  - `prov:Entity` for masked outputs.  
  - `prov:used` fixtures or vault entities.  
  - `prov:wasGeneratedBy` for masked geometries.

This CI scenario ensures that all three layers are **wired together correctly**.

---

## 🧪 Validation & CI/CD

This section defines the minimum tests CI must run for metadata & provenance.

### 1. Required masking metadata fields

**Intent:** every masked feature must include key `kfm:*` fields.

Required fields (baseline):

- `kfm:privacy_method`  
- `kfm:sensitivity_label`  
- `kfm:r_min_m`, `kfm:r_max_m`  
- `kfm:masking_run_id`  
- `kfm:prov_ref`  

Recommended (if applicable):

- `kfm:access_label`  
- Sovereignty/geoethics tags (e.g., `kfm:sovereignty_label`, `kfm:geoethics_profile`).  

Pseudocode:

~~~python
REQUIRED_FIELDS = [
    "kfm:privacy_method",
    "kfm:sensitivity_label",
    "kfm:r_min_m",
    "kfm:r_max_m",
    "kfm:masking_run_id",
    "kfm:prov_ref",
]

def test_required_masking_metadata_present(masked_records):
    for rec in masked_records:
        props = rec["properties"]
        missing = [f for f in REQUIRED_FIELDS if f not in props]
        assert not missing, f"{rec['id']} missing required masking fields: {missing}"
~~~

This runs on masked outputs derived from fixtures.

### 2. `masking_run_id` consistency with manifest

**Intent:** masked records’ `kfm:masking_run_id` must match a known run manifest and the `run_id` field inside it.

Pseudocode:

~~~python
def test_masking_run_id_matches_manifest(masked_records, manifest):
    expected_run_id = manifest["run_id"]
    for rec in masked_records:
        rid = rec["properties"]["kfm:masking_run_id"]
        assert rid == expected_run_id, (
            f"{rec['id']} has masking_run_id={rid}, expected {expected_run_id}"
        )
~~~

Optionally, CI can confirm that the `standard_ref` in the manifest matches the current standard’s semantic ID.

### 3. `kfm:privacy_method` and radius profile alignment

**Intent:** ensure that `kfm:privacy_method` and radius fields align with manifest configuration.

Pseudocode:

~~~python
def test_privacy_method_and_radii_match_manifest(masked_records, manifest):
    expected_method = manifest["privacy_method"]
    radius_profiles = manifest["radius_profiles"]  # per label

    for rec in masked_records:
        props = rec["properties"]
        label = props["kfm:sensitivity_label"]
        assert props["kfm:privacy_method"] == expected_method

        expected_profile = radius_profiles[label]
        assert props["kfm:r_min_m"] == expected_profile["min_m"]
        assert props["kfm:r_max_m"] == expected_profile["max_m"]
~~~

This ties the record-level metadata directly to run-level configuration.

### 4. `kfm:prov_ref` must resolve to valid PROV-O bundle

**Intent:** confirm that `kfm:prov_ref` is present, unique per feature, and resolves to a valid PROV document.

Pseudocode skeleton:

~~~python
import json
from pathlib import Path

def load_prov(path_or_uri):
    # In CI, likely a local path; production may use URIs/resolvers
    return json.loads(Path(path_or_uri).read_text())

def test_prov_refs_resolve_and_match_run(masked_records, expected_run_id):
    for rec in masked_records:
        prov_ref = rec["properties"]["kfm:prov_ref"]
        prov_doc = load_prov(prov_ref)

        # Example: assert that the PROV entity or activity references the same run_id
        activities = [e for e in prov_doc.get("@graph", []) if "prov:Activity" in e.get("@type", [])]
        run_activities = [a for a in activities if a.get("@id") == expected_run_id]
        assert run_activities, f"{rec['id']} prov_ref={prov_ref} missing activity for {expected_run_id}"
~~~

Depending on PROV structure, more detailed checks may be added (e.g., `prov:used` fixture IDs).

### 5. CI integration

Recommended test module:

- `tests/geoprivacy/test_metadata_provenance.py`

Example CLI:

~~~bash
pytest tests/geoprivacy/test_metadata_provenance.py::test_required_masking_metadata_present
pytest tests/geoprivacy/test_metadata_provenance.py::test_masking_run_id_matches_manifest
pytest tests/geoprivacy/test_metadata_provenance.py::test_privacy_method_and_radii_match_manifest
pytest tests/geoprivacy/test_metadata_provenance.py::test_prov_refs_resolve_and_match_run
~~~

Workflow hook (conceptual):

~~~yaml
- name: Geoprivacy metadata & PROV tests
  run: |
    pytest tests/geoprivacy/test_metadata_provenance.py
~~~

Any failure is a **hard CI failure**; missing or inconsistent metadata/provenance is not acceptable for geoprivacy-governed datasets.

---

## 📦 Data & Metadata

This scenario interacts with:

- **Fixtures**

  - `docs/standards/geospatial/geoprivacy-masking/examples/fixtures/points_kansas_small.geojson`  
  - `docs/standards/geospatial/geoprivacy-masking/examples/fixtures/points_sacred_synthetic.geojson`  

- **Run manifests**

  - `docs/standards/geospatial/geoprivacy-masking/examples/masking-runs/run_2025-12-05T00-00Z.json`  
  - `docs/standards/geospatial/geoprivacy-masking/examples/masking-runs/run_2025-12-06T00-00Z_sacred.json`  

- **PROV bundles**

  - `docs/standards/geospatial/geoprivacy-masking/examples/masking-runs/run_2025-12-05T00-00Z_prov.jsonld`  
  - (Additional bundles as needed for sacred or extended scenarios.)

Suggested scenario metadata object:

~~~json
{
  "scenario_id": "geoprivacy-metadata-provenance-v1",
  "standard_ref": "kfm-doc-geoprivacy-masking-v11.2.4",
  "fixtures": [
    "docs/standards/geospatial/geoprivacy-masking/examples/fixtures/points_kansas_small.geojson",
    "docs/standards/geospatial/geoprivacy-masking/examples/fixtures/points_sacred_synthetic.geojson"
  ],
  "run_manifests": [
    "docs/standards/geospatial/geoprivacy-masking/examples/masking-runs/run_2025-12-05T00-00Z.json"
  ],
  "prov_bundles": [
    "docs/standards/geospatial/geoprivacy-masking/examples/masking-runs/run_2025-12-05T00-00Z_prov.jsonld"
  ],
  "tests": [
    "tests/geoprivacy/test_metadata_provenance.py::test_required_masking_metadata_present",
    "tests/geoprivacy/test_metadata_provenance.py::test_masking_run_id_matches_manifest",
    "tests/geoprivacy/test_metadata_provenance.py::test_privacy_method_and_radii_match_manifest",
    "tests/geoprivacy/test_metadata_provenance.py::test_prov_refs_resolve_and_match_run"
  ]
}
~~~

This object can feed CI dashboards or scenario registries.

---

## 🌐 STAC, DCAT & PROV Alignment

This scenario is a direct enforcement of STAC/DCAT/PROV alignment for geoprivacy.

### STAC

CI should confirm:

- Masked STAC Items include:

  - `properties["kfm:privacy_method"]`  
  - `properties["kfm:sensitivity_label"]`  
  - `properties["kfm:r_min_m"]`, `properties["kfm:r_max_m"]`  
  - `properties["kfm:masking_run_id"]`  
  - `properties["kfm:prov_ref"]`  

- Optionally, `properties["kfm:ci_scenarios"]` includes `"geoprivacy-metadata-provenance-v1"`.

### DCAT

For internal QA DCAT records, CI can assert that:

- `dct:conformsTo` references the geoprivacy standard.  
- A KFM extension property (e.g., `kfm:masking_run_id`) matches the STAC property.  
- `dct:provenance` (or extension) points at a PROV bundle consistent with `kfm:prov_ref`.

### PROV

The scenario enforces that:

- `kfm:prov_ref` links to PROV documents where:

  - Masking run is a `prov:Activity` with ID matching `kfm:masking_run_id`.  
  - Masked geometries are `prov:Entity` records.  
  - Input fixtures or vault entities appear in `prov:used`.  

This enables graph-based audits of geoprivacy decisions.

---

## 🗺️ Diagrams

High-level flow for metadata & PROV verification:

~~~mermaid
flowchart LR
    A[Fixtures] --> B[Deterministic Donut Masking]
    B --> C[Masked GeoJSON + Properties]
    B --> D[Run Manifest]
    B --> E[PROV Bundle]

    C --> F[Metadata CI Checks]
    D --> F
    E --> G[PROV Consistency Checks]

    F --> H[CI Result]
    G --> H
~~~

Key idea:

- Masked features, manifests, and PROV bundles must **tell the same story** about what happened.

---

## 🧠 Story Node & Focus Mode Integration

Metadata & provenance CI checks are vital for trustworthy narratives:

- Story Nodes can explain:

  > “Each masked location is linked to a provenance record describing when and how the masking happened, and which standard it follows.”

- Focus Mode for a dataset or layer can show:

  - That `geoprivacy-metadata-provenance-v1` has passed.  
  - Which masking method and run ID were used.  
  - That a PROV record exists and is machine-readable.

Guidelines:

- When surfacing PROV info to non-technical users, emphasize **who/what/when** (not raw IDs).  
- Avoid exposing any internal vault identifiers; fixture-based examples are safest for teaching.

---

## ⚖ FAIR+CARE & Governance

This scenario is a governance backbone:

- **FAIR**
  - *Findable*: masking metadata and PROV links make masked datasets easily discoverable and traceable.  
  - *Accessible*: provenance and masking details are available through standard APIs and catalogs.  
  - *Interoperable*: STAC/DCAT/PROV profiles ensure metadata can be used across systems.  
  - *Reusable*: clear masking documentation allows downstream users to reuse data with confidence.

- **CARE & sovereignty**
  - Ensures that decisions about sacred and sensitive data are recorded as **first-class entities**, not hidden side effects.  
  - Makes it easier for Tribal Sovereignty Boards and FAIR+CARE Council to review and audit geoprivacy behavior.  
  - Helps ensure no masked dataset is published without a corresponding provenance record.

Governance expectations:

- Removing or weakening these checks requires formal review and updated documentation in both this scenario and the geoprivacy standard.  
- Failing this scenario is a **governance event**, not just a technical bug, because it implies untraceable geoprivacy behavior.

---

## 🕰️ Version History

| Version    | Date       | Status            | Notes                                                                                                              |
|-----------:|------------|-------------------|--------------------------------------------------------------------------------------------------------------------|
| **v11.2.4** | 2025-12-06 | Active / Enforced | Initial metadata & PROV CI scenario aligned with geoprivacy-masking v11.2.4; defines required fields, PROV links, and governance role. |

Future updates should:

- Track any changes to required masking metadata fields or PROV profiles.  
- Extend checks as new catalogs or graph schemas incorporate geoprivacy fields.  
- Maintain stable scenario IDs, introducing new IDs for conceptually breaking changes.

---

<div align="center">

🧪 **KFM Geoprivacy Masking — CI Scenario: Metadata & PROV Alignment (v11.2.4)**  
Catalog-Ready Privacy · Transparent Provenance · FAIR+CARE Sovereignty  

[📘 Docs Root](../../../../../..) · [🧪 CI Scenarios Index](./README.md) · [🛡 Geoprivacy Standard](../../README.md) · [⚖ Governance](../../../../../governance/ROOT-GOVERNANCE.md)

</div>

