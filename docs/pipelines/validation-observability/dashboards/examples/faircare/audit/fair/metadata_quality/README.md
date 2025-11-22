---
title: "📑📘 Kansas Frontier Matrix — FAIR Audit Examples: Metadata Quality (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/pipelines/validation-observability/dashboards/examples/faircare/audit/fair/metadata_quality/README.md"

version: "v11.0.0"
last_updated: "2025-11-20"
release_stage: "Stable · Reference"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · FAIR+CARE Council · Metadata Governance Board · Sovereignty Review Board"
backward_compatibility: "Full v11.x-compatible"

commit_sha: "<latest-commit-hash>"
signature_ref: "../../../../../../../../../../../releases/v11.0.0/signature.sig"
attestation_ref: "../../../../../../../../../../../releases/v11.0.0/slsa-attestation.json"

sbom_ref: "../../../../../../../../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../../../../../../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../../../../../../../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../../../../../../../../../schemas/telemetry/dashboards-examples-faircare-audit-fair-metadataquality-v11.json"
energy_schema: "../../../../../../../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../../../../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../../../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

care_label: "Collective Benefit · Authority to Control · Responsibility · Ethics"
risk_profile: "Medium–High · Metadata Integrity · Sovereignty Constraints"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
ontology_protocol_version: "KFM-OP v11.0"

status: "Active · Reference"
doc_kind: "Dashboards · Examples"
intent: "observability-dashboard-examples-faircare-audit-fair-metadata-quality"
category: "FAIR · Metadata Quality · Governance · Interoperability"
sensitivity: "Medium"
classification: "Public Examples (Governance-Safe)"
jurisdiction: "Kansas / United States"

prov_profile: "PROV-O Core + KFM Metadata-Quality Extensions"
openlineage_profile: "Optional (Metadata Drift Event Introspection)"

metadata_profiles:
  - "../../../../../../../../../../../schemas/stac/kfm-stac-v11.json"
  - "../../../../../../../../../../../schemas/dcat/kfm-dcat-v11.json"
  - "../../../../../../../../../../../schemas/jsonld/kfm-context-v11.json"

validation_profiles:
  - "docs-lint-v11"
  - "schema-lint-v11"
  - "metadata-quality-check-v11"
  - "faircare-schema-audit-v11"
  - "sovereignty-schema-audit-v11"

ci_integration:
  workflow: ".github/workflows/kfm-ci.yml"
  environment: "N/A"

runtime:
  compute: "Client-Side Visualization Only"
  dashboard_engine: "Grafana · KFM Observability FAIR+CARE Metadata Layer"
  agents: "N/A"

fair_category: "F1-A1-I1-R1"
indigenous_rights_flag: true
redaction_required: false

ontology_alignment:
  cidoc: "E73 Information Object · E7 Activity"
  schema_org: "Dataset"
  owl_time: "ProperInterval"
  geosparql: "N/A"

json_schema_ref: "../../../../../../../../../../../schemas/json/dashboards-examples-faircare-audit-fair-metadataquality-v11.json"
shape_schema_ref: "../../../../../../../../../../../schemas/shacl/dashboards-examples-faircare-audit-fair-metadataquality-v11.shacl"

doc_uuid: "urn:kfm:docs:dashboards:examples:faircare:audit:fair:metadata_quality:v11.0.0"
semantic_document_id: "kfm-dashboard-examples-faircare-audit-fair-metadata-quality"
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"
---

<div align="center">

# 📑📘 **FAIR Audit Examples — Metadata Quality (v11.0.0)**  
`docs/pipelines/validation-observability/dashboards/examples/faircare/audit/fair/metadata_quality/README.md`

**Purpose:**  
Provide authoritative examples of dashboards used to evaluate **metadata completeness, correctness, consistency, semantic accuracy, and FAIR+CARE compliance**, ensuring every dataset, model output, lineage artifact, and narrative in KFM v11 is represented with ethically sound and findable metadata.

</div>

---

# 📘 Overview

Metadata Quality dashboards evaluate:

- **Required-field completeness** across STAC, DCAT, JSON-LD, PROV-O  
- **Semantic correctness** of ontology-aligned metadata (CIDOC-CRM, GeoSPARQL, OWL-Time)  
- **Metadata drift**, errors, inconsistencies, or schema conflicts  
- **FAIR Findability, Accessibility, Interoperability, Reusability** alignment  
- **CARE cultural/sovereignty integrity fields**, ensuring proper masking & redaction  
- **Metadata provenance lineage**, documenting creator, reviewer, agents, and activities  
- **Promotion-blocking metadata issues** & governance thresholds  
- **Cross-schema validation**, including STAC↔DCAT↔JSON-LD mappings  
- **Metadata transformation lineage** (ETL → graph → UI)  
- **Cultural-sensitivity metadata checks** (no leakage of protected knowledge)

These dashboards enforce **metadata stewardship excellence**.

---

# 🗂 Directory Layout

```text
metadata_quality/
│
├── completeness/            # Required field & schema completeness checks
├── consistency/             # Cross-field & cross-schema consistency checks
├── drift/                   # Metadata drift detection across versions
├── cultural/                # Cultural/sovereignty metadata protections
├── transformations/         # Metadata transformation lineage checks
└── risk/                    # Metadata risk scoring & promotion blockers
```

---

# 📋 1. Metadata Completeness Dashboard Example

Shows:

- Missing required STAC/DCAT/JSON-LD/PROV fields  
- Metadata scoring & completeness heatmaps  
- Cultural masking metadata correctness  

---

# 🔄 2. Metadata Consistency Dashboard Example

Tracks:

- Logical and semantic field consistency  
- Ontology-term alignment  
- Internal/external crosswalk consistency  

---

# 🌀 3. Metadata Drift Dashboard Example

Displays:

- Version drift detection  
- Semantic and structural metadata drift  
- FAIR/CARE drift overlays  

---

# 🏺 4. Cultural Metadata Dashboard Example

Highlights:

- Protection of cultural metadata categories  
- Sovereignty-aligned metadata constraints  
- Cultural-era & cultural-site masking lineage  

---

# 🔗 5. Metadata Transformation Lineage Dashboard Example

Includes:

- Metadata evolution from raw → ETL → graph → UI  
- PROV-O lineage of field generation  
- Sovereignty-filtered transformations  

---

# ⚠️ 6. Metadata Risk Dashboard Example

Provides:

- Metadata risk score  
- FAIR+CARE conflict scoring  
- Promotion-blocking metadata issues  
- Governance escalation indicators  

---

# 🎨 Dashboard Construction Requirements (v11)

All metadata-quality dashboards MUST:

- Follow FAIR+CARE + sovereignty requirements  
- Use PROV-O lineage annotations for metadata generation  
- Mask culturally sensitive and precise spatial/temporal details  
- Follow KFM Observability UI Style Guide v11  
- Maintain WCAG 2.1 AA accessibility  
- Avoid exposing protected metadata fields  
- Block promotion upon metadata failure  
- Validate schema compliance for all metadata formats  

---

# 🕰 Version History

| Version | Date       | Notes                                                                     |
|--------:|-----------:|---------------------------------------------------------------------------|
| v11.0.0 | 2025-11-20 | Initial FAIR Metadata Quality Audit Dashboard Example Library (v11 LTS).  |

---

# 🔗 Footer

**Back to Root:** `../../../../../../../../README.md`  
**Back to FAIR+CARE Audit Examples:** `../../README.md`  
**Back to Dashboard Schemas:** `../../../schemas/README.md`  
**Back to Validation & Observability:** `../../../../../README.md`  
**Back to Standards:** `../../../../../../standards/README.md`

