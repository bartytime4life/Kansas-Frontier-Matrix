---
title: "🔗🎛️ Kansas Frontier Matrix — Focus Mode v3 Lineage Dashboard Examples (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/pipelines/validation-observability/dashboards/examples/focus_mode/lineage/README.md"

version: "v11.0.0"
last_updated: "2025-11-20"
release_stage: "Stable / Reference"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Narrative Governance Board · FAIR+CARE Council · Sovereignty Review Board"
backward_compatibility: "Full v11.x-compatible"

commit_sha: "<latest-commit-hash>"
signature_ref: "../../../../../../releases/v11.0.0/signature.sig"
attestation_ref: "../../../../../../releases/v11.0.0/slsa-attestation.json"

sbom_ref: "../../../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../../../../schemas/telemetry/dashboards-examples-focusmode-lineage-v11.json"
energy_schema: "../../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

care_label: "Collective Benefit · Authority to Control · Responsibility · Ethics"
risk_profile: "High · Narrative & AI Provenance Oversight"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
ontology_protocol_version: "KFM-OP v11.0"

status: "Active / Reference"
doc_kind: "Dashboards · Examples"
intent: "observability-dashboard-examples-focusmode-lineage"
category: "Focus Mode v3 · Story Node v3 · Narrative Provenance · Sovereignty Compliance"
sensitivity: "High"
classification: "Public Examples (Governance-Safe)"
jurisdiction: "Kansas / United States"

prov_profile: "PROV-O Core + KFM Narrative Lineage Extensions"
openlineage_profile: "Visualization Layer Only"

metadata_profiles:
  - "../../../../../../schemas/stac/kfm-stac-v11.json"
  - "../../../../../../schemas/dcat/kfm-dcat-v11.json"
  - "../../../../../../schemas/jsonld/kfm-context-v11.json"

validation_profiles:
  - "docs-lint-v11"

ci_integration:
  workflow: ".github/workflows/kfm-ci.yml"
  environment: "N/A (Reference Layer Only)"

runtime:
  compute: "Client-Side Visualization Only"
  dashboard_engine: "Grafana · KFM Observability FocusMode Layer"
  agents: "N/A"

fair_category: "F1-A1-I1-R1"
indigenous_rights_flag: true
redaction_required: true

ontology_alignment:
  cidoc: "E5 Event · E7 Activity · E73 Information Object"
  schema_org: "Dataset"
  owl_time: "ProperInterval"
  geosparql: "N/A"

json_schema_ref: "../../../../../../schemas/json/dashboards-examples-focusmode-lineage-v11.json"
shape_schema_ref: "../../../../../../schemas/shacl/dashboards-examples-focusmode-lineage-v11.shacl"

doc_uuid: "urn:kfm:docs:pipelines:validation-observability:dashboards:examples:focus_mode:lineage:v11.0.0"
semantic_document_id: "kfm-dashboard-examples-focusmode-lineage"
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"
---

<div align="center">

# 🔗🎛️ **Focus Mode v3 Lineage Observability Dashboard Examples (v11.0.0)**  
`docs/pipelines/validation-observability/dashboards/examples/focus_mode/lineage/README.md`

**Purpose:**  
Provide example dashboard patterns used to visualize **narrative lineage**, Story Node v3 lifecycle provenance, sovereignty-aware masking lineage, and end-to-end Focus Mode v3 reasoning provenance within the KFM.

These designs demonstrate how governance verifies and trusts narrative generation processes.

</div>

---

# 📘 Overview

Focus Mode lineage dashboards allow governance teams to audit:

- Story Node v3 creation lineage (entity → activity → agent)  
- Narrative input → reasoning → output paths  
- AI reasoning steps and masked reasoning nodes  
- CARE and sovereignty filtering provenance  
- Temporal & spatial grounding chains  
- Masking & redaction lineage correctness  
- Narrative conflict lineage (identifying which inputs caused misalignment)  
- Story Node validation lifecycle (draft → validated → published)  
- Graph-based lineage connectivity using PROV-O + OWL-Time  

These dashboards ensure narratives are **fact-grounded, explainable, governed, and sovereignty-compliant**.

---

# 🗂 Directory Layout

```text
lineage/
│
├── prov/                       # PROV-O lineage dashboards for Story Nodes
├── masking/                    # Masking/redaction lineage for narrative flows
├── reasoning/                  # Reasoning-chain lineage diagnostics
├── spatial/                    # Spatial lineage (H3 masked) for narrative anchors
├── temporal/                   # Temporal lineage & precision-reduction dashboards
└── validation/                 # Validation lifecycle lineage (draft→validated→published)
```

---

# 🧬 1. Story Node PROV-O Lineage Dashboard Example

Displays:

- Full Entity → Activity → Agent chain  
- Narrative-input provenance (documents, datasets, events)  
- Story Node generation events  
- Derived-from relationships shown in graph form  
- Focus Mode v3 invocation lineage  

Ensures **auditable, traceable narrative creation**.

---

# 🛡️ 2. Masking & Redaction Lineage Dashboard Example

Includes:

- Masking activities (`kfm:MaskingActivity`)  
- Spatial H3 r7+ generalization lineage  
- Temporal precision reduction lineage  
- CARE & sovereignty justification references  
- Narrative suppression lineage  

Critical for sovereignty compliance.

---

# 🧠 3. Reasoning Path Lineage Dashboard Example

Visualizes:

- Which reasoning rules fired  
- What embeddings/entities influenced narrative selection  
- Divergent branches in reasoning  
- Story Node grounding lineage trails  
- Decision-chain explainability  

Used for **transparency of AI-driven reasoning**.

---

# 🗺️ 4. Spatial Lineage Dashboard Example

Shows:

- Spatial containment lineage  
- H3 masked trajectories  
- Spatial risk overlays  
- Spatial grounding relationships between data sources and narrative anchors  

Ensures spatial fidelity while enforcing protection of sensitive locations.

---

# 🕒 5. Temporal Lineage Dashboard Example

Displays:

- OWL-Time alignment  
- Interval-derivation lineage  
- Narrative temporal window computation  
- Masked temporal precision lineage  
- Sensitive-era suppression provenance  

Ensures proper **temporal reasoning governance**.

---

# 🧰 6. Validation Lifecycle Lineage Dashboard Example

Tracks:

- Story Node draft creation  
- Automated validation checks  
- Governance review lineage  
- FAIR+CARE scoring lineage  
- Published-version provenance  

Confirms **narrative output meets all promotion requirements**.

---

# 🎨 Dashboard Construction Requirements (v11)

Focus Mode lineage dashboards MUST:

- Mask all sensitive coordinates and precise dates  
- Provide FAIR+CARE + sovereignty indicators  
- Render full-provenance tooltips  
- Follow the KFM Observability UI Style Guide v11  
- Achieve WCAG 2.1 AA accessibility  
- Use safe color palettes (governance-neutral, high contrast)  
- Avoid speculative or inferred cultural/historical details  

---

# 🕰 Version History

| Version | Date       | Notes                                                             |
|--------:|-----------:|-------------------------------------------------------------------|
| v11.0.0 | 2025-11-20 | Initial Focus Mode v3 Lineage Dashboard Example Library.          |

---

# 🔗 Footer

**Back to Root:** `../../../../../README.md`  
**Back to Focus Mode Dashboard Examples:** `../README.md`  
**Back to Dashboard Schemas:** `../../schemas/README.md`  
**Back to Dashboard Templates:** `../../templates/README.md`  
**Back to Validation & Observability:** `../../README.md`  
**Back to Standards:** `../../../standards/README.md`
