---
title: "📦 KFM Geoprivacy Masking — Schema Catalog & Profiles"
path: "docs/standards/geospatial/geoprivacy-masking/schemas/README.md"
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

sbom_ref: "../../../../releases/v11.2.4/sbom.spdx.json"
manifest_ref: "../../../../releases/v11.2.4/manifest.zip"
telemetry_ref: "../../../../releases/v11.2.4/privacy-masking-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/geoprivacy/v1.json"
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
  - "docs/standards/geospatial/geoprivacy-masking/examples/fixtures/README.md@v11.2.4"
  - "docs/standards/geospatial/geoprivacy-masking/examples/masking-runs/README.md@v11.2.4"
  - "docs/standards/geospatial/geoprivacy-masking/examples/ci-scenarios/README.md@v11.2.4"

provenance_requirements:
  versions_required: false
  newest_first: true
  must_reference_superseded: false
  must_reference_origin_root: true

json_schema_ref: "schemas/json/geoprivacy-masking-v1.json"
shape_schema_ref: "schemas/shacl/geoprivacy-masking-v1-shape.ttl"

story_node_refs: []
immutability_status: "version-pinned"

doc_uuid: "urn:kfm:doc:standards:geoprivacy-masking-schemas-v11.2.4"
semantic_document_id: "kfm-doc-geoprivacy-masking-schemas-v11.2.4"
event_source_id: "ledger:kfm:doc:standards:geoprivacy:schemas"

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

# 📦 KFM Geoprivacy Masking — Schema Catalog & Profiles  
v11.2.4 · JSON / SHACL · STAC/DCAT/PROV-Aligned  

`docs/standards/geospatial/geoprivacy-masking/schemas/README.md`

**Purpose:**  
Describe and govern the **schema layer** for KFM geoprivacy masking — including JSON Schemas and SHACL shapes that validate masking metadata blocks, fixtures, run manifests, and CI scenarios — so that all geoprivacy-related data structures are deterministic, catalog-ready, provenance-aligned, and FAIR+CARE compliant.

</div>

---

## 🗂️ Directory Layout

~~~text
📂 docs/standards/geospatial/geoprivacy-masking/
└── 📂 schemas/
    ├── 📄 README.md                        # 📦 This file: schema catalog & guidance
    └── 📄 geoprivacy-masking-v1.json       # Core masking metadata JSON Schema (profile for kfm:* fields)
~~~

Related **repository-level** schema locations (referenced by this guide):

~~~text
📂 schemas/
├── 📂 json/
│   ├── 📄 geoprivacy-masking-v1.json                          # Core masking metadata block
│   ├── 📄 geoprivacy-masking-fixtures-v11.2.4.schema.json     # Fixtures schema (example sets)
│   ├── 📄 geoprivacy-masking-runs-v11.2.4.schema.json         # Masking run manifests
│   ├── 📄 geoprivacy-masking-ci-distance-validation-v11.2.4.schema.json
│   ├── 📄 geoprivacy-masking-ci-determinism-v11.2.4.schema.json
│   ├── 📄 geoprivacy-masking-ci-anti-triangulation-v11.2.4.schema.json
│   ├── 📄 geoprivacy-masking-ci-sovereignty-compliance-v11.2.4.schema.json
│   └── 📄 geoprivacy-masking-ci-metadata-provenance-v11.2.4.schema.json
└── 📂 shacl/
    ├── 📄 geoprivacy-masking-v1-shape.ttl                     # Core masking metadata SHACL shape
    ├── 📄 geoprivacy-masking-fixtures-v11.2.4-shape.ttl
    ├── 📄 geoprivacy-masking-runs-v11.2.4-shape.ttl
    ├── 📄 geoprivacy-masking-ci-distance-validation-v11.2.4-shape.ttl
    ├── 📄 geoprivacy-masking-ci-determinism-v11.2.4-shape.ttl
    ├── 📄 geoprivacy-masking-ci-anti-triangulation-v11.2.4-shape.ttl
    ├── 📄 geoprivacy-masking-ci-sovereignty-compliance-v11.2.4-shape.ttl
    └── 📄 geoprivacy-masking-ci-metadata-provenance-v11.2.4-shape.ttl
~~~

Author rules:

- Any new schema or SHACL shape **MUST**:
  - Live under `schemas/json/` or `schemas/shacl/`.  
  - Be referenced from this catalog and from the relevant example/CI docs.  
  - Undergo schema review before being used in production CI.  
- `geoprivacy-masking-v1.json` in this directory is the **human-facing entrypoint**; the authoritative file lives under `schemas/json/` and is imported by tooling.

---

## 📘 Overview

The geoprivacy masking schemas:

- Define the **canonical structure** of masking metadata blocks (`kfm:*` fields attached to features, STAC Items, graph nodes).  
- Validate **supporting artifacts**:
  - Synthetic fixtures (example datasets).  
  - Masking run manifests (control plane).  
  - CI scenarios (distance, determinism, anti-triangulation, sovereignty, metadata & PROV).  
- Provide a bridge between:
  - ETL and API code,  
  - STAC/DCAT catalogs,  
  - Neo4j graph,  
  - Story Nodes and Focus Mode.

This guide explains:

- How the schemas are organized.  
- Which artifacts they validate.  
- How they align with STAC, DCAT, and PROV-O profiles.  
- How to extend them safely under KFM governance.

---

## 🧭 Context

This schema layer sits inside the broader KFM architecture:

> Deterministic ETL → STAC/DCAT/PROV catalogs → Neo4j knowledge graph → API layer → React/MapLibre/Cesium frontend → Story Nodes → Focus Mode

Where:

- **Schemas** are the **contract**:
  - ETL output must conform to them.  
  - Catalog loaders expect them.  
  - Graph ingest and CI enforce them.  

This guide is tightly coupled to:

- Geoprivacy standard:  
  `docs/standards/geospatial/geoprivacy-masking/README.md`  
- Example docs (fixtures, masking runs, CI scenarios).  
- Repository-level schema directories under `schemas/`.

Any changes to schemas must be reflected in:

- These docs,  
- The geoprivacy standard,  
- The affected tests and CI scenarios.

---

## 🧱 Architecture

### 1. Core masking metadata schema (`geoprivacy-masking-v1`)

Purpose:

- Define the structure of the **embedding** `kfm:*` masking metadata block attached to:
  - GeoJSON features,  
  - STAC Items/properties,  
  - Neo4j nodes (via JSON-serialized properties or mapped fields).

Key responsibilities:

- Enforce presence and types of core fields:
  - `kfm:privacy_method`  
  - `kfm:sensitivity_label`  
  - `kfm:r_min_m`, `kfm:r_max_m`  
  - `kfm:masking_run_id`  
  - `kfm:prov_ref`  
- Optionally include:
  - `kfm:access_label`  
  - `kfm:sovereignty_label`  
  - `kfm:fixture_flag` (for example-only data).

The SHACL shape (`geoprivacy-masking-v1-shape.ttl`) mirrors this for RDF/graph contexts.

### 2. Fixtures schemas

- **JSON:** `geoprivacy-masking-fixtures-v11.2.4.schema.json`  
- **SHACL:** `geoprivacy-masking-fixtures-v11.2.4-shape.ttl`

Purpose:

- Constrain synthetic fixtures (e.g., `points_kansas_small.geojson`, `points_sacred_synthetic.geojson`) used in examples and CI.  
- Ensure:
  - CRS is WGS84.  
  - Features have `id` and `kfm:sensitivity_label`.  
  - No real-world identifiers are accidentally included.

### 3. Masking run manifest schemas

- **JSON:** `geoprivacy-masking-runs-v11.2.4.schema.json`  
- **SHACL:** `geoprivacy-masking-runs-v11.2.4-shape.ttl`

Purpose:

- Validate masking run manifests (e.g., `run_2025-12-05T00-00Z.json`).  
- Enforce structure for:
  - `run_id`, `standard_ref`, `fixtures`, `privacy_method`, `radius_profiles`, `summary`, `telemetry_ref`, `prov_bundle`.  

### 4. CI scenario schemas

For each CI scenario (`distance_validation`, `determinism`, `anti_triangulation`, `sovereignty_compliance`, `metadata_provenance`):

- JSON schema defines the **scenario metadata object** (scenario ID, fixtures, manifests, tests).  
- SHACL shape allows integration into PROV/graph-based CI registries.

These schemas are mostly for:

- Scenario registries.  
- CI dashboards.  
- Governance queries (e.g., “Which scenarios apply to this dataset?”).

---

## 🧪 Validation & CI/CD

The schema layer is wired into CI via:

- `test_profiles`:
  - `schema-lint`  
  - `metadata-check`  
  - `provenance-check`  

### 1. JSON Schema validation

- Tools (e.g., `ajv`, `jsonschema`) validate:
  - Masking metadata blocks in features/STAC Items.  
  - Fixtures, run manifests, CI scenario descriptors.

Typical CI step:

```bash
# Example: validate geoprivacy masking run manifests
jsonschema -i docs/standards/geospatial/geoprivacy-masking/examples/masking-runs/run_2025-12-05T00-00Z.json \
  schemas/json/geoprivacy-masking-runs-v11.2.4.schema.json

