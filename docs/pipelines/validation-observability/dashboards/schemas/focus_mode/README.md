---
title: "🧠🗂️ Kansas Frontier Matrix — Focus Mode v3 Dashboard Schema Reference (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/pipelines/validation-observability/dashboards/schemas/focus_mode/README.md"

version: "v11.0.0"
last_updated: "2025-11-20"
release_stage: "Stable · Schema Reference"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Focus Mode Governance Board · FAIR+CARE Council · Sovereignty Review Board"

commit_sha: "<latest-commit-hash>"
signature_ref: "../../../../../releases/v11.0.0/signature.sig"
attestation_ref: "../../../../../releases/v11.0.0/slsa-attestation.json"

sbom_ref: "../../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/dashboards-schemas-focusmode-v11.json"
energy_schema: "../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

care_label: "Collective Benefit · Authority to Control · Responsibility · Ethics"
risk_profile: "High — Narrative Safety · Cultural & Sovereignty Sensitive"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
ontology_protocol_version: "KFM-OP v11.0"

status: "Active / Reference"
doc_kind: "Schemas · Dashboard Specification"
intent: "schema-focusmode"
category: "Schemas · Focus Mode v3 · AI Reasoning · Narrative Safety"
sensitivity: "High"
classification: "Public (Governance-Safe)"
jurisdiction: "Kansas / United States"

prov_profile: "PROV-O Core + KFM Schema-Lineage Extensions"
openlineage_profile: "Supported"
metadata_profiles:
  - "../../../../../schemas/stac/kfm-stac-v11.json"
  - "../../../../../schemas/dcat/kfm-dcat-v11.json"
  - "../../../../../schemas/jsonld/kfm-context-v11.json"

validation_profiles:
  - "schema-lint-v11"
  - "dashboards-schema-check-v11"
  - "focusmode-schema-validation"

ci_integration:
  workflow: ".github/workflows/kfm-ci.yml"

runtime:
  compute: "Schema Reference Only"
  dashboard_engine: "N/A"

fair_category: "F1-A1-I1-R1"
indigenous_rights_flag: true
redaction_required: true

ontology_alignment:
  cidoc: "E7 Activity · E73 Information Object · E5 Event"
  schema_org: "Dataset"
  owl_time: "ProperInterval"
  geosparql: "geo:FeatureCollection"

json_schema_ref: "../../../../../schemas/json/dashboards-focusmode.schema.json"
shape_schema_ref: "../../../../../schemas/shacl/dashboards-focusmode.shacl"

doc_uuid: "urn:kfm:docs:dashboards:schemas:focusmode:v11.0.0"
semantic_document_id: "kfm-dashboard-schemas-focusmode"
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"
---

<div align="center">

# 🧠🗂️ **Focus Mode v3 — Dashboard Schema Reference (v11.0.0)**  
`docs/pipelines/validation-observability/dashboards/schemas/focus_mode/README.md`

**Purpose:**  
Define the **authoritative schema specification** for all Focus Mode v3 dashboard data structures, guarantees, validation rules, lineage integration, sovereignty masking requirements, and FAIR+CARE-aligned semantics.

</div>

---

# 📘 Overview

Focus Mode v3 dashboards depend on strict, schema-governed data structures.  
These schemas ensure:

- Safe narrative reasoning  
- Proper entity/event grounding  
- Spatial/temporal sovereignty masking  
- Cultural-sensitivity enforcement  
- Bias/drift/anomaly integration  
- Narrative alignment with ontology & PROV-O lineage  
- Promotion-gate compatibility  
- FAIR+CARE-compliant metadata semantics  

This reference file documents all schema expectations and their validation behavior.

---

# 🗂 Directory Layout

```text
focus_mode/
│
├── grounding/               # Grounding schema (entity, spatial, temporal, semantic)
├── narrative/               # Narrative structure, Story Node v3 schema
├── reasoning/               # Reasoning DAG schema, justification chain
├── risk/                    # Focus Mode risk schema (drift/bias/harm)
├── sovereignty/             # Spatial/temporal/cultural sovereignty schema
└── lineage/                 # PROV-O lineage linking for Focus Mode events
```

---

# 🧩 Schema Domains

## 1. 🧭 Grounding Schema
Defines the required fields for:

- Entity selection & canonical identifiers  
- Spatial generalization (H3 r7+)  
- Temporal coarsening (decade/era)  
- Semantic grounding (CIDOC-CRM, OWL-Time, GeoSPARQL)  
- Uncertainty metrics  
- Provenance/lineage hooks  

## 2. 📖 Narrative Schema
Governs:

- Story Node v3 JSON structure  
- Narrative sequence ordering  
- Spatial/temporal/cultural correctness rules  
- Explanation components  
- FAIR+CARE filtering  

## 3. 🧠 Reasoning Schema
Specifies:

- Reasoning-path DAG nodes  
- Justification metadata  
- Evidence-link requirements  
- Explainability (SHAP/LIME) integration  
- Governance annotations  

## 4. ⚠️ Risk Schema
Covers:

- Drift/bias indicators  
- Harm probability  
- Sovereignty violation risk  
- Promotion blocking thresholds  

## 5. 🛡️ Sovereignty Schema
Defines:

- Cultural-site masking  
- Spatial generalization rules  
- Sensitive-era protection  
- Authority-to-Control fields  
- Redaction lineage requirements  

## 6. 🔗 Lineage Schema
Ensures:

- PROV-O Entity/Activity/Agent completeness  
- Story Node lineage consistency  
- Transformation/derivation mapping  
- Metadata propagation compliance  

---

# 🔍 Validation Rules

All Focus Mode schemas MUST:

- Pass JSON Schema v2020-12 validation  
- Pass SHACL shape constraints  
- Mask sensitive data (H3 r7+, decade/era)  
- Include FAIR+CARE + sovereignty fields  
- Embed PROV-O lineage requirements  
- Provide deterministic identifier structures  
- Avoid semantic drift or unbounded ambiguity  

CI/CD enforces:

- `schema-lint-v11`  
- `focusmode-schema-validation`  
- `lineage-schema-check-v11`  
- `faircare-schema-audit-v11`  

---

# 🏛 Integration with KFM v11 System

Valid Focus Mode schemas ensure compatibility with:

- Neo4j graph entity-linking  
- MapLibre/Cesium spatial rendering  
- Focus Reasoner v3  
- Story Node v3  
- LangGraph ETL pipelines  
- FAIR+CARE Governance Plane  
- OpenLineage v2.5 emissions  
- STAC/DCAT catalog propagation  

---

# 🕰 Version History

| Version | Date       | Notes                                                                  |
|--------:|-----------:|------------------------------------------------------------------------|
| v11.0.0 | 2025-11-20 | Initial Focus Mode v3 Dashboard Schema Reference (v11 LTS).            |

---

# 🔗 Footer

**Back to Root:** `../../../../../../README.md`  
**Back to Dashboard Schemas:** `../README.md`  
**Back to Validation & Observability:** `../../../README.md`  
**Back to Standards:** `../../../../standards/README.md`

