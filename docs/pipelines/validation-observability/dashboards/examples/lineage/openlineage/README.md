---
title: "📡🔗 Kansas Frontier Matrix — OpenLineage Event Dashboard Examples (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/pipelines/validation-observability/dashboards/examples/lineage/openlineage/README.md"

version: "v11.0.0"
last_updated: "2025-11-20"
release_stage: "Stable / Reference"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Lineage Governance Board · FAIR+CARE Council · Sovereignty Review Board"
backward_compatibility: "Full v11.x-compatible"

commit_sha: "<latest-commit-hash>"
signature_ref: "../../../../../../releases/v11.0.0/signature.sig"
attestation_ref: "../../../../../../releases/v11.0.0/slsa-attestation.json"

sbom_ref: "../../../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../../../../schemas/telemetry/dashboards-examples-lineage-openlineage-v11.json"
energy_schema: "../../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

care_label: "Collective Benefit · Authority to Control · Responsibility · Ethics"
risk_profile: "High · Provenance · ETL Execution Transparency"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
ontology_protocol_version: "KFM-OP v11.0"

status: "Active / Reference"
doc_kind: "Dashboards · Examples"
intent: "observability-dashboard-examples-lineage-openlineage"
category: "Lineage · OpenLineage · ETL Execution · Provenance Integrity"
sensitivity: "Medium–High"
classification: "Public Examples (Governance-Safe)"
jurisdiction: "Kansas / United States"

prov_profile: "PROV-O Core + OpenLineage Event Extensions"
openlineage_profile: "Full Visual Integration (Read-Only)"

metadata_profiles:
  - "../../../../../../schemas/stac/kfm-stac-v11.json"
  - "../../../../../../schemas/dcat/kfm-dcat-v11.json"
  - "../../../../../../schemas/jsonld/kfm-context-v11.json"

validation_profiles:
  - "docs-lint-v11"

ci_integration:
  workflow: ".github/workflows/kfm-ci.yml"
  environment: "N/A"

runtime:
  compute: "Client-Side Visualization Only"
  dashboard_engine: "Grafana · KFM Observability Lineage Layer"
  agents: "N/A"

fair_category: "F1-A1-I1-R1"
indigenous_rights_flag: true
redaction_required: true

ontology_alignment:
  cidoc: "E7 Activity · E5 Event · E73 Information Object"
  schema_org: "Dataset"
  owl_time: "ProperInterval"
  geosparql: "N/A"

json_schema_ref: "../../../../../../schemas/json/dashboards-examples-lineage-openlineage-v11.json"
shape_schema_ref: "../../../../../../schemas/shacl/dashboards-examples-lineage-openlineage-v11.shacl"

doc_uuid: "urn:kfm:docs:pipelines:validation-observability:dashboards:examples:lineage:openlineage:v11.0.0"
semantic_document_id: "kfm-dashboard-examples-lineage-openlineage"
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"
---

<div align="center">

# 📡🔗 **OpenLineage Event Dashboard Examples (v11.0.0)**  
`docs/pipelines/validation-observability/dashboards/examples/lineage/openlineage/README.md`

**Purpose:**  
Provide example dashboards demonstrating **OpenLineage-based observability** across ETL, AI enrichment, Story Node generation, Focus Mode v3 reasoning, and governance workflows.  
These dashboards illustrate how **run-level, task-level, and lineage-level events** are governed and visualized inside KFM v11.

</div>

---

# 📘 Overview

OpenLineage events represent the *operational heartbeat* of KFM pipelines.  
These dashboards allow governance stakeholders to inspect:

- ETL execution paths  
- Task-level success/failure  
- Retry/rollback events  
- WAL replay sequences  
- Sovereignty-aware masking events emitted by pipelines  
- AI inference steps that emit OpenLineage metadata  
- Promotion-gate lineage event groups  
- Run lifecycle timelines  
- Input/output dataset ancestry  
- Cross-pipeline linkage  

Dashboards in this module ensure **transparent, auditable ETL + AI operations**.

---

# 🗂 Directory Layout

```text
openlineage/
│
├── runs/                       # Run-level event timelines
├── tasks/                      # Task-level event breakdowns
├── linkage/                    # Upstream/downstream dataset linking dashboards
├── masking/                    # Masking/redaction events emitted by pipelines
├── ai/                         # AI-specific OpenLineage events
└── promotion/                  # Promotion-gate OpenLineage event diagnostics
```

---

# 🚀 1. Run-Level OpenLineage Dashboard Example

Displays:

- DAG run start/end  
- Task duration bars  
- Retry cycles  
- Hotfix/rollback markers  
- Sovereignty event markers  
- Critical path analysis  

Used for verifying DAG runtime reliability and integrity.

---

# 🧩 2. Task-Level Event Dashboard Example

Shows:

- Per-task success/failure  
- Event emissions (input, output, complete)  
- Masking redaction lineage markers  
- Task-level error chains  
- Performance metrics  

Enables fine-grained diagnostics of ETL task behaviors.

---

# 🔗 3. Dataset Linkage Dashboard Example

Maps:

- Upstream → downstream dataset relations  
- Cross-DAG lineage  
- Provenance propagation  
- Entity merges and splits  
- Story Node binding lineage  

Essential for promotion eligibility.

---

# 🛡️ 4. Masking/Redaction Event Dashboard Example

Visualizes:

- H3 r7+ masking events  
- Temporal precision reduction  
- Sensitive-site suppression events  
- Masking failures & governance alerts  
- Redaction lineage anomalies  

Critical for sovereignty-rule validation.

---

# 🤖 5. AI OpenLineage Event Dashboard Example

Includes:

- AI inference event graphs  
- Model/version lineage emissions  
- Drift/bias-related OpenLineage events  
- AI → Narrative lineage mapping  
- Sensitive-context masking events triggered by AI  

Supports gov reviews of AI safety and provenance.

---

# 🚦 6. Promotion-Gate Lineage Event Dashboard Example

Displays:

- Promotion blockers  
- Required lineage-event thresholds  
- FAIR+CARE audit linkage  
- Sovereignty lineage prerequisites  
- Evidence bundle completeness  

Ensures datasets obey all promotion-gate lineage requirements.

---

# 🎨 Dashboard Construction Requirements (v11)

All OpenLineage dashboards MUST:

- Follow KFM Observability UI Style Guide v11  
- Provide FAIR+CARE & sovereignty metadata  
- Mask sensitive spatial/temporal info  
- Include PROV-O tooltips for event-to-entity linkage  
- Use high-contrast, accessible color palettes  
- Provide explicit lineage justification captions  

---

# 🕰 Version History

| Version | Date       | Notes                                                         |
|--------:|-----------:|---------------------------------------------------------------|
| v11.0.0 | 2025-11-20 | Initial OpenLineage Dashboard Examples for KFM v11 LTS.       |

---

# 🔗 Footer

**Back to Root:** `../../../../../README.md`  
**Back to Lineage Dashboard Examples:** `../README.md`  
**Back to Dashboard Schemas:** `../../schemas/README.md`  
**Back to Dashboard Templates:** `../../templates/README.md`  
**Back to Validation & Observability:** `../../README.md`  
**Back to Standards:** `../../../standards/README.md`
