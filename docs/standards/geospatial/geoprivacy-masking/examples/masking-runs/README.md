---
title: "🧪 KFM Geoprivacy Masking — Masking Run Manifests Guide"
path: "docs/standards/geospatial/geoprivacy-masking/examples/masking-runs/README.md"
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

json_schema_ref: "schemas/json/geoprivacy-masking-runs-v11.2.4.schema.json"
shape_schema_ref: "schemas/shacl/geoprivacy-masking-runs-v11.2.4-shape.ttl"

story_node_refs: []
immutability_status: "version-pinned"

doc_uuid: "urn:kfm:doc:standards:geoprivacy-masking-runs-v11.2.4"
semantic_document_id: "kfm-doc-geoprivacy-masking-runs-v11.2.4"
event_source_id: "ledger:kfm:doc:standards:geoprivacy:examples:masking-runs"

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

# 🧪 KFM Geoprivacy Masking — Masking Run Manifests Guide  
v11.2.4 · Deterministic ETL · Telemetry-Aware · PROV-Aligned  

`docs/standards/geospatial/geoprivacy-masking/examples/masking-runs/README.md`

**Purpose:**  
Define and document the example masking run manifests used to validate KFM’s Geospatial Privacy & Cultural-Safety Masking Standard, ensuring each run is reproducible, telemetry-ready, STAC/DCAT/PROV-aligned, and suitable for CI/CD, audits, and Story Node explanations.

</div>

---

## 🗂️ Directory Layout

~~~text
📂 docs/standards/geospatial/geoprivacy-masking/examples/
└── 📂 masking-runs/
    ├── 📄 README.md                            # 🧪 This guide: masking run manifests & rules
    ├── 📄 run_2025-12-05T00-00Z.json           # Example donut masking run manifest (baseline)
    ├── 📄 run_2025-12-05T00-00Z_prov.jsonld    # PROV bundle for baseline run
    ├── 📄 run_2025-12-06T00-00Z_sacred.json    # Sacred-focused masking run manifest (H3 regions)
    ├── 📄 run_2025-12-06T00-00Z_sacred_prov.jsonld
    └── 📄 run_template.json                    # Template manifest for new example runs
~~~

Author rules:

- Each new example masking run must have:
  - A JSON manifest file (e.g., `run_<timestamp>[_profile].json`).  
  - An associated PROV bundle file (e.g., `*_prov.jsonld`).  
- Every new file in this directory must be briefly described in this layout block.  
- Example manifests must only reference **synthetic fixtures** from `examples/fixtures/`, not real vault data.

---

## 📘 Overview

This guide operationalizes the geoprivacy standard by:

- Defining a **canonical structure** for masking run manifests used in tests, demos, and audits.  
- Providing **named example runs** that combine fixtures, algorithm parameters, and summary metrics.  
- Showing how to connect run manifests to **PROV bundles** and **telemetry records**.  

These manifests sit between:

- **Fixtures** (synthetic datasets) and  
- **Masked outputs** (GeoJSON, STAC Items, graph nodes, tiles, UI layers).

Normative behavior of the masking algorithm is defined in:

- `docs/standards/geospatial/geoprivacy-masking/README.md`  

This guide focuses on **how to describe specific runs** of that algorithm in a deterministic, catalog-ready way.

---

## 🧭 Context

In KFM’s pipeline:

> Fixtures → Masking ETL (donut method) → Masked outputs + run manifest + PROV bundle → STAC/DCAT catalog + Neo4j + telemetry.

Masking run manifests serve three main purposes:

1. **Reproducibility**  
   - Record which fixtures, parameters, and algorithm versions were used.  
   - Allow re-running the same ETL configuration in the future.

2. **Auditability**  
   - Provide a concise view of what happened in a run (counts, distances, failures).  
   - Connect to PROV bundles for detailed lineage.

3. **Communication & Education**  
   - Enable Focus Mode and Story Nodes to explain how masking works using concrete, non-sensitive runs.  

They are not a replacement for full ETL configs or production run metadata, but they are a **curated, example-oriented layer** for docs and CI.

---

## 🧱 Architecture

Masking run manifests follow a simple, strongly-typed structure.

### 1. Core sections

A typical run manifest JSON has:

- `run_id` — a globally unique identifier (URN or UUID).  
- `standard_ref` — semantic ID of the geoprivacy standard version.  
- `fixtures` — list of fixture paths used as input.  
- `privacy_method` — algorithm identifier (e.g., `donut_geomask_v1`).  
- `radius_profiles` — per-sensitivity radius windows used in this run.  
- `parameters` — additional algorithm parameters (e.g., “max_retries”, “ellipsoid”).  
- `summary` — counts and distance stats (safe aggregates).  
- `telemetry_ref` — optional pointer into telemetry logs.  
- `prov_bundle` — path/ID of the corresponding PROV document.

### 2. Example: baseline run manifest

~~~json
{
  "run_id": "urn:kfm:etl-run:2025-12-05T00:00Z",
  "standard_ref": "kfm-doc-geoprivacy-masking-v11.2.4",
  "profile": "baseline-mixed",
  "fixtures": [
    "docs/standards/geospatial/geoprivacy-masking/examples/fixtures/points_kansas_small.geojson"
  ],
  "privacy_method": "donut_geomask_v1",
  "algorithm_version": "1.0.0",
  "radius_profiles": {
    "public":    { "min_m": 50,   "max_m": 150 },
    "community": { "min_m": 250,  "max_m": 500 },
    "sensitive": { "min_m": 1000, "max_m": 3000 },
    "sacred":    { "min_m": 3000, "max_m": 10000 }
  },
  "parameters": {
    "ellipsoid": "WGS84",
    "max_retries": 5,
    "seed_strategy": "HMAC(record_id, secret_salt)"
  },
  "summary": {
    "total_records": 64,
    "by_label": {
      "public": 20,
      "community": 24,
      "sensitive": 12,
      "sacred": 8
    },
    "distance_m": {
      "min": 52.3,
      "max": 9876.5,
      "mean": 2437.1
    },
    "failed_records": 0
  },
  "telemetry_ref": "urn:kfm:telemetry:geoprivacy:run:2025-12-05T00:00Z",
  "prov_bundle": "docs/standards/geospatial/geoprivacy-masking/examples/masking-runs/run_2025-12-05T00-00Z_prov.jsonld"
}
~~~

Production manifests may include additional fields; examples should remain small and focused.

---

## 🧪 Validation & CI/CD

These manifests are **first-class inputs** to CI.

### 1. Schema validation

- All `run_*.json` files must validate against `geoprivacy-masking-runs-v11.2.4.schema.json`.  
- CI should fail if:
  - Required fields are missing.  
  - Types or allowed values are incorrect.  

### 2. Consistency checks

CI can cross-check manifests against:

- Fixtures:
  - Ensure all paths exist under `examples/fixtures/`.  
- PROV bundles:
  - Ensure each `prov_bundle` path exists and parses as PROV JSON-LD.  
- Telemetry:
  - Optionally confirm that `telemetry_ref` keys are present in telemetry stores.

### 3. Derived tests

Manifests can drive higher-level tests, e.g.:

- Re-running masking using `fixtures`, `privacy_method`, `radius_profiles`, and `parameters` and comparing:
  - Counts.
  - Distance stats (within tolerances).  
- Confirming PROV bundles reference:
  - The same `run_id`.  
  - The same fixtures (via `prov:used`).  

This makes example runs a convenient target for regression suites.

---

## 📦 Data & Metadata

### 1. Required manifest fields

At minimum, each manifest in this directory must have:

- `run_id` (string, URN/UUID)  
- `standard_ref` (string, semantic ID)  
- `fixtures` (array of strings)  
- `privacy_method` (string)  
- `radius_profiles` (object keyed by sensitivity label)  
- `summary.total_records` (integer)  
- `summary.failed_records` (integer)  
- `prov_bundle` (string path or URI)

Additional recommended fields:

- `profile` — short name like `baseline-mixed` or `sacred-high-protection`.  
- `algorithm_version` — version of masking algorithm implementation.  
- `telemetry_ref` — pointer into telemetry system.  

### 2. Naming conventions

- Use ISO-like timestamps in `run_*` filenames:  
  - `run_YYYY-MM-DDTHH-MMZ[_profile].json`  
- Pair with PROV bundles using `_prov.jsonld`.  

Examples:

- `run_2025-12-05T00-00Z.json`  
- `run_2025-12-05T00-00Z_prov.jsonld`  
- `run_2025-12-06T00-00Z_sacred.json`  
- `run_2025-12-06T00-00Z_sacred_prov.jsonld`

This pattern makes it easy to map between manifest, PROV, and telemetry.

---

## 🌐 STAC, DCAT & PROV Alignment

### 1. STAC alignment

While run manifests are not spatial datasets themselves, they can be:

- Referenced as `assets` in a STAC Item describing an example geoprivacy dataset.  
- Linked via `properties["kfm:masking_run_id"]` on masked Items.

Example STAC `properties` snippet:

~~~json
{
  "kfm:masking_run_id": "urn:kfm:etl-run:2025-12-05T00:00Z",
  "kfm:privacy_method": "donut_geomask_v1"
}
~~~

### 2. DCAT alignment

In DCAT, a masking run manifest can be:

- Modeled as a `dcat:Distribution` of a QA `dcat:Dataset` describing geoprivacy tests.  
- Linked to the geoprivacy standard via `dct:conformsTo`.

Example snippet:

~~~json
{
  "@type": "dcat:Distribution",
  "dct:title": "KFM Geoprivacy Masking Run 2025-12-05T00:00Z",
  "dct:identifier": "urn:kfm:etl-run:2025-12-05T00:00Z",
  "dct:conformsTo": "kfm-doc-geoprivacy-masking-v11.2.4"
}
~~~

### 3. PROV alignment

PROV is the **primary** alignment:

- Manifest fields map to PROV as:
  - `run_id` → `prov:Activity` ID.  
  - `fixtures` → `prov:used` entities.  
  - Masked outputs → `prov:generated` entities.  
- The PROV bundle (`*_prov.jsonld`) is the detailed representation; the run manifest is a concise control plane.

Example activity sketch (inside PROV bundle):

~~~json
{
  "@id": "urn:kfm:etl-run:2025-12-05T00:00Z",
  "@type": "prov:Activity",
  "prov:used": [
    "fixture:points_kansas_small"
  ],
  "prov:wasAssociatedWith": [
    "urn:kfm:service:etl-geoprivacy"
  ]
}
~~~

---

## 🧠 Story Node & Focus Mode Integration

Masking run manifests are useful for **explaining** geoprivacy:

- Story Nodes can:
  - Reference specific example runs (`run_id`) when describing how masking operates.  
  - Use summary stats from manifests to illustrate distance windows and protection levels.

- Focus Mode can:
  - Surface explanations like “In this example run, 64 points were masked with donut_geomask_v1 using radius profiles X/Y/Z.”  
  - Link to fixtures and masked outputs without any reliance on real sensitive data.

Guidelines:

- When used in narratives, clearly label runs as **examples** and tie them back to their synthetic fixtures.  
- Avoid mixing example runs with production telemetry in user-facing UI without clear differentiation.

---

## ⚖ FAIR+CARE & Governance

Masking run manifests support FAIR+CARE by:

- **FAIR**
  - *Findable*: stable `run_id` and filenames; can be indexed in internal catalogs.  
  - *Accessible*: stored in the repo under open license and documented schema.  
  - *Interoperable*: aligned with PROV, and linkable from STAC/DCAT.  
  - *Reusable*: serve as templates for future runs and regression tests.

- **CARE & sovereignty**
  - Document how masking is applied, without exposing raw coordinates.  
  - Enable transparent review by FAIR+CARE Council and Tribal Sovereignty Board.  
  - Reinforce that sovereign and sacred data are handled via documented, auditable processes.

Any use of real-world runs in public-facing docs must:

- Obey the main geoprivacy standard.  
- Undergo governance review when sacred or high-sensitivity data are involved.  
- Ensure raw or lightly perturbed coordinates are never surfaced.

---

## 🕰️ Version History

| Version    | Date       | Status            | Notes                                                                                           |
|-----------:|------------|-------------------|-------------------------------------------------------------------------------------------------|
| **v11.2.4** | 2025-12-06 | Active / Enforced | Initial masking run manifests guide aligned with geoprivacy-masking v11.2.4; defines structure, examples, and CI usage. |

Future revisions should:

- Extend examples as new masking profiles or geometry types are introduced.  
- Keep manifest schema and examples synchronized with `geoprivacy-masking-runs-v11.2.4.schema.json`.  
- Note any changes that affect how CI, telemetry, or Story Nodes interpret run metadata.

---

<div align="center">

🧪 **KFM Geoprivacy Masking — Masking Run Manifests Guide (v11.2.4)**  
Deterministic ETL · Transparent Provenance · FAIR+CARE Ethics  

[📘 Docs Root](../../../../../..) · [🧪 Examples Index](../README.md) · [🛡 Geoprivacy Standard](../../README.md) · [⚖ Governance](../../../../../governance/ROOT-GOVERNANCE.md)

</div>

