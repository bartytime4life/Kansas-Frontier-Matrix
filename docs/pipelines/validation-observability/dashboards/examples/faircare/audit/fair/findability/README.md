---
title: "🔍📘 Kansas Frontier Matrix — FAIR Audit Examples: Findability (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/pipelines/validation-observability/dashboards/examples/faircare/audit/fair/findability/README.md"

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
telemetry_schema: "../../../../../../../../../../../schemas/telemetry/dashboards-examples-faircare-audit-fair-findability-v11.json"
energy_schema: "../../../../../../../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../../../../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../../../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

care_label: "Collective Benefit · Authority to Control · Responsibility · Ethics"
risk_profile: "Medium–High · Metadata Integrity · Findability Governance"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
ontology_protocol_version: "KFM-OP v11.0"

status: "Active · Reference"
doc_kind: "Dashboards · Examples"
intent: "observability-dashboard-examples-faircare-audit-fair-findability"
category: "FAIR · Metadata Quality · Findability · Governance"
sensitivity: "Medium"
classification: "Public Examples (Governance-Safe)"
jurisdiction: "Kansas / United States"

prov_profile: "PROV-O Core + KFM FAIR-Findability Extensions"
openlineage_profile: "Optional (Metadata Provenance Alignment)"

metadata_profiles:
  - "../../../../../../../../../../../schemas/stac/kfm-stac-v11.json"
  - "../../../../../../../../../../../schemas/dcat/kfm-dcat-v11.json"
  - "../../../../../../../../../../../schemas/jsonld/kfm-context-v11.json"

validation_profiles:
  - "docs-lint-v11"
  - "schema-lint-v11"
  - "fair-schema-audit-v11"
  - "metadata-quality-check-v11"
  - "sovereignty-schema-audit-v11"

ci_integration:
  workflow: ".github/workflows/kfm-ci.yml"
  environment: "N/A · Reference Only"

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

json_schema_ref: "../../../../../../../../../../../schemas/json/dashboards-examples-faircare-audit-fair-findability-v11.json"
shape_schema_ref: "../../../../../../../../../../../schemas/shacl/dashboards-examples-faircare-audit-fair-findability-v11.shacl"

doc_uuid: "urn:kfm:docs:dashboards:examples:faircare:audit:fair:findability:v11.0.0"
semantic_document_id: "kfm-dashboard-examples-faircare-audit-fair-findability"
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"
---

<div align="center">

# 🔍📘 **FAIR Audit Examples — Findability (v11.0.0)**  
`docs/pipelines/validation-observability/dashboards/examples/faircare/audit/fair/findability/README.md`

**Purpose:**  
Provide authoritative examples of dashboards used to measure **FAIR Findability (F1, F1.1, F1.2, F2, F3, F4)** compliance across all KFM v11 datasets, AI outputs, lineage artifacts, and narrative/STAC/DCAT metadata layers—while preserving sovereignty and CARE protections.

</div>

---

# 📘 Overview

Findability dashboards validate:

- Persistent identifiers (PIDs) and resolvable URIs  
- STAC/DCAT metadata registrability  
- Dataset indexing completeness  
- Metadata discoverability scoring  
- Crosswalk alignment across STAC → DCAT → JSON-LD → PROV  
- Sovereignty safe-search overlays (no exposure of protected info)  
- Semantic metadata (ontology alignment) that enhances Findability  
- FAIR+CARE conflict indicators  
- Promotion-blocking findability violations  
- Metadata provenance lineage (PROV-O)

These dashboards help ensure KFM is **discoverable, searchable, semantically coherent, and ethically governed**.

---

# 🗂 Directory Layout

```text
findability/
│
├── identifiers/              # Persistent IDs, resolvability, namespace quality
├── indexing/                 # STAC/DCAT indexing completeness
├── metadata/                 # Metadata completeness, schema-lint results
├── crosswalks/               # Cross-schema mapping (STAC↔DCAT↔JSON-LD)
├── searchability/            # Search index quality & discoverability
└── risk/                     # Findability risk scoring & promotion blockers
```

---

# 🔑 1. Persistent Identifier Dashboard Example

Shows:

- PID validity (URN, DOI, handles)  
- Namespace structure compliance  
- FAIR F1/F1.1/F1.2 scoring  
- Sovereignty overlays for sensitive domains  

---

# 📇 2. Indexing Dashboard Example

Tracks:

- STAC/DCAT registration  
- Catalog indexing completeness  
- Cross-collection entry validation  
- Metadata drift warnings  

---

# 📑 3. Metadata Completeness Dashboard Example

Includes:

- Missing fields (required/optional Enums)  
- Schema-lint results  
- FAIR+CARE annotation completeness  
- DCAT/STAC alignment errors  

---

# 🔀 4. Crosswalk Dashboard Example

Visualizes:

- STAC → DCAT → JSON-LD field mappings  
- Ontology (CIDOC-CRM, GeoSPARQL, OWL-Time) match quality  
- Semantic conflicts or gaps  
- FAIR compliance for interoperability  

---

# 🔍 5. Searchability Dashboard Example

Shows:

- Document/dataset discoverability  
- Search index health  
- Misalignment between metadata & search surfaces  
- CARE safe-search overlays  

---

# ⚠️ 6. Findability Risk Dashboard Example

Provides:

- Findability risk score  
- Promotion-blocking metadata issues  
- Governance escalation requirements  
- FAIR+CARE conflict traces  

---

# 🎨 Dashboard Construction Requirements (v11)

All Findability dashboards MUST:

- Conform to FAIR+CARE + sovereignty constraints  
- Provide PROV-O metadata lineage visualizations  
- Follow KFM Observability UI Style Guide v11  
- Maintain WCAG 2.1 AA readability  
- Mask sensitive cultural/spatial/temporal details where applicable  
- Validate STAC/DCAT metadata compliance  
- Block promotion if findability requirements fail  
- Avoid any speculative generation of metadata not backed by provenance  

---

# 🕰 Version History

| Version | Date       | Notes                                                               |
|--------:|-----------:|---------------------------------------------------------------------|
| v11.0.0 | 2025-11-20 | Initial FAIR Findability Audit Dashboard Example Library (v11 LTS). |

---

# 🔗 Footer

**Back to Root:** `../../../../../../../../README.md`  
**Back to FAIR+CARE Audit Examples:** `../../README.md`  
**Back to Dashboard Schemas:** `../../../schemas/README.md`  
**Back to Validation & Observability:** `../../../../../README.md`  
**Back to Standards:** `../../../../../../standards/README.md`

