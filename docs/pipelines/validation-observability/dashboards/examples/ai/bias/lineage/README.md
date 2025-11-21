---
title: "🔗⚖️ Kansas Frontier Matrix — AI Bias Lineage Dashboard Examples (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/pipelines/validation-observability/dashboards/examples/ai/bias/lineage/README.md"

version: "v11.0.0"
last_updated: "2025-11-20"
release_stage: "Stable · Reference"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · AI Governance Board · Lineage Governance Board · FAIR+CARE Council · Sovereignty Review Board"
backward_compatibility: "Full v11.x-compatible"

commit_sha: "<latest-commit-hash>"
signature_ref: "../../../../../../../../releases/v11.0.0/signature.sig"
attestation_ref: "../../../../../../../../releases/v11.0.0/slsa-attestation.json"

sbom_ref: "../../../../../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../../../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../../../../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../../../../../../schemas/telemetry/dashboards-examples-ai-bias-lineage-v11.json"
energy_schema: "../../../../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

care_label: "Collective Benefit · Authority to Control · Responsibility · Ethics"
risk_profile: "High · AI Provenance Integrity · Sovereignty-Sensitive Bias"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
ontology_protocol_version: "KFM-OP v11.0"

status: "Active / Reference"
doc_kind: "Dashboards · Examples"
intent: "observability-dashboard-examples-ai-bias-lineage"
category: "AI Bias · Lineage · Sovereignty · Governance"
sensitivity: "High"
classification: "Public Examples (Governance-Safe)"
jurisdiction: "Kansas / United States"

prov_profile: "PROV-O Core + KFM AI Bias Lineage Extensions"
openlineage_profile: "Optional (Read-Only Event Alignment)"

metadata_profiles:
  - "../../../../../../../../schemas/stac/kfm-stac-v11.json"
  - "../../../../../../../../schemas/dcat/kfm-dcat-v11.json"
  - "../../../../../../../../schemas/jsonld/kfm-context-v11.json"

validation_profiles:
  - "docs-lint-v11"
  - "schema-lint-v11"

ci_integration:
  workflow: ".github/workflows/kfm-ci.yml"

runtime:
  compute: "Client-Side Visualization Only"
  dashboard_engine: "Grafana · KFM Observability AI Layer"
  agents: "N/A"

fair_category: "F1-A1-I1-R1"
indigenous_rights_flag: true
redaction_required: true

ontology_alignment:
  cidoc: "E7 Activity · E73 Information Object · E5 Event"
  schema_org: "Dataset"
  owl_time: "ProperInterval"
  geosparql: "N/A"

json_schema_ref: "../../../../../../../../schemas/json/dashboards-examples-ai-bias-lineage-v11.json"
shape_schema_ref: "../../../../../../../../schemas/shacl/dashboards-examples-ai-bias-lineage-v11.shacl"

doc_uuid: "urn:kfm:docs:dashboards:examples:ai:bias:lineage:v11.0.0"
semantic_document_id: "kfm-dashboard-examples-ai-bias-lineage"
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"
---

<div align="center">

# 🔗⚖️ **AI Bias Lineage Dashboard Examples (v11.0.0)**  
`docs/pipelines/validation-observability/dashboards/examples/ai/bias/lineage/README.md`

**Purpose:**  
Show governance-safe, sovereignty-aligned examples of dashboards used to audit **AI bias lineage**, including how bias emerges, propagates, interacts with masking/redaction rules, and influences Story Node v3 and Focus Mode v3 reasoning chains.

</div>

---

# 📘 Overview

AI bias lineage dashboards reveal:

- Where bias originates in an AI pipeline  
- How bias propagates through embeddings, inference, and reasoning  
- Bias lineage across model versions & configurations  
- CARE & sovereignty-filtered lineage nodes  
- Story Node v3 lineage influenced by biased inference  
- Masking-lineage, redaction-lineage, and sovereign-lineage ties  
- Promotion-blocking lineage gaps & anomalies  
- Bias → drift → narrative impact chains  
- PROV-O structured provenance for bias events  

These examples provide **audit-grade insight** for the AI Governance and Sovereignty Councils.

---

# 🗂 Directory Layout

```text
lineage/
│
├── embeddings/              # Embedding-level bias lineage examples
├── inference/               # Inference-level bias lineage paths
├── drift/                   # Drift-driven bias lineage propagation
├── narrative/               # Story Node v3 lineage impacted by bias
├── masking/                 # Masking/redaction lineage for bias nodes
└── promotion/               # Promotion-gate lineage validation examples
```

---

# 🔗 1. Embedding Bias Lineage Dashboard Example

Shows:

- Embedding clusters producing biased outcomes  
- Latent-space linkages to sensitive attributes (masked)  
- Drift-induced bias lineage  
- H3/temporal masking lineage constraints  

---

# 🧠 2. Inference Bias Lineage Dashboard Example

Tracks:

- prov:Activity inference steps  
- Model → inference → output lineage  
- Sensitive-attribute interactions (masked)  
- Bias-risk propagation  

---

# 📖 3. Narrative Bias Lineage Dashboard Example

Visualizes:

- Story Node v3 nodes influenced by biased reasoning  
- Cultural-harm lineage markers  
- CARE ethics lineage overlays  
- Promotion-blocking narrative bias lineage  

---

# 🌀 4. Bias-Drift Lineage Dashboard Example

Highlights:

- Model drift producing new bias pathways  
- Bias drift → narrative drift lineage  
- Sovereignty-related drift lineage  

---

# 🛡️ 5. Masking/Redaction Bias Lineage Dashboard Example

Includes:

- Redaction lineage for sensitive bias sources  
- Masking lineage preventing leak of protected data  
- CARE + sovereignty justification nodes  

---

# 🚦 6. Promotion-Gate Bias Lineage Dashboard Example

Displays:

- Lineage completeness for datasets impacted by bias  
- Governance signature requirements  
- Bias-blocking promotion logic  
- FAIR+CARE audit overlays  

---

# 🎨 Dashboard Construction Requirements (v11)

All bias lineage dashboards MUST:

- Use fully masked spatial/temporal/cultural data  
- Provide PROV-O lineage tooltips  
- Follow KFM Observability UI Style Guide v11  
- Use WCAG 2.1 AA-compliant palettes  
- Include sovereignty + FAIR+CARE metadata  
- Provide governance-readable explanation captions  
- Block promotion if lineage shows unresolved bias propagation  

---

# 🕰 Version History

| Version | Date       | Notes                                                             |
|--------:|-----------:|-------------------------------------------------------------------|
| v11.0.0 | 2025-11-20 | Initial AI Bias Lineage Dashboard Example Library (v11).          |

---

# 🔗 Footer

**Back to Root:** `../../../../../../../README.md`  
**Back to AI Bias Examples:** `../README.md`  
**Back to Dashboard Schemas:** `../../../schemas/README.md`  
**Back to Validation & Observability:** `../../../../README.md`  
**Back to Standards:** `../../../../../standards/README.md`