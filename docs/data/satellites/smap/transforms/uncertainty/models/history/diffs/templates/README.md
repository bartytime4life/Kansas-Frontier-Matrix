---
title: "🧩 NASA SMAP — Uncertainty Model Diff Templates (KFM-UncertaintyDiff v11.2)"
path: "docs/data/satellites/smap/transforms/uncertainty/models/history/diffs/templates/README.md"
version: "v11.2.2"
last_updated: "2025-11-29"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Annual · Uncertainty Subcommittee · FAIR+CARE Council"
status: "Active / Enforced"

classification: "Public Modeling Templates"
license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
provenance_profile: "KFM-PROV-O v11.2"

commit_sha: "<latest-commit>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../../../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../../../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../../../../../../../releases/v11.2.2/data-telemetry.json"
telemetry_schema: "../../../../../../../../../../../schemas/telemetry/sat-smap-transforms-v11.json"

governance_ref: "../../../../../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

fair_category: "F1-A1-I2-R4"
care_label: "CARE-A / CARE-B (depends on model domain)"
indigenous_rights_flag: true
sensitivity_level: "Medium (uncertainty influences interpretation)"
public_exposure_risk: "Low"
risk_category: "Low–Medium"
redaction_required: false

data_steward: "Uncertainty Subcommittee · Earth Systems Working Group · KFM FAIR+CARE Council"

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "Dataset"
  prov_o: "prov:Plan"
  owl_time: "TemporalEntity"

json_schema_ref: "../../../../../../../../../../../schemas/json/transform-smap-uncertainty-diffs-template-v11.json"
shape_schema_ref: "../../../../../../../../../../../schemas/shacl/transform-smap-uncertainty-diffs-template-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:smap:uncertainty-diffs-templates-readme:v11.2.2"
semantic_document_id: "kfm-doc-data-smap-uncertainty-diffs-templates"
event_source_id: "ledger:docs/data/satellites/smap/transforms/uncertainty/models/history/diffs/templates/README.md"
immutability_status: "version-pinned"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
ttl_policy: "36 months"
sunset_policy: "Superseded upon next model-diff template framework"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 🧩 **NASA SMAP — Uncertainty Model Diff Templates**  
`docs/data/satellites/smap/transforms/uncertainty/models/history/diffs/templates/README.md`

**Purpose**  
Define the **official template structure** for `diff_vXXX_vYYY.json` files that describe  
evolution between SMAP Uncertainty Model versions.  
Templates enforce **reproducible**, **FAIR+CARE-aligned**, and **provenance-correct**  
uncertainty evolution across radiometer, QA/RFI, calibration, and sovereignty contexts.

</div>

---

## 📘 1. Overview

Uncertainty model diffs express how SMAP uncertainty logic changes over time:

- Radiometer noise evolution  
- Calibration-linked uncertainty changes  
- QA/RFI-based uncertainty scaling changes  
- Combined-model structural updates  
- Sovereignty-driven uncertainty-floor adjustments  
- FAIR+CARE-driven transparency requirements  
- PROV-O lineage semantics  

This directory provides **template(s)** that standardize the authoring of these diffs.

---

## 🗂️ 2. Directory Layout (Emoji-Rich · Option A)

~~~text
docs/data/satellites/smap/transforms/uncertainty/models/history/diffs/templates/
├── 📄 README.md                 # This file
│
└── 🧩 diff_template.json        # Authoritative template for all uncertainty-model diff logs
~~~

Only **approved** templates may be stored here.  
All new diffs MUST be derived from this template.

---

## 🧱 3. Structure of `diff_template.json` (KFM-UncertaintyDiff v11 Required Fields)

Each diff MUST include the following sections:

### 1. 📅 Version Metadata
- `"model_version_old"`  
- `"model_version_new"`  
- `"valid_from"`  
- `"valid_to"`  
- `"nasa_source_model_version"`  

### 2. 🔢 Numeric Deltas
- `"radiometer_uncertainty_delta"`  
- `"qa_rfi_uncertainty_delta"`  
- `"combined_uncertainty_delta"`  
- `"uncertainty_floor_delta"`  

### 3. 🧬 Structural Changes
- new/removed keys  
- unit changes  
- propagation rule changes  
- sovereignty-floor policy changes  

### 4. ⚠️ Governance & Sovereignty Effects
Templates must enforce explicit documentation of:

- `"care_label_change"`  
- `"h3_sensitivity_change"`  
- `"sovereignty_uncertainty_floor_change"`  
- `"masking_implication"` (true/false)  
- `"requires_governance_review"` (true/false)  

### 5. 🧾 Provenance Block (PROV-O)
Mandatory:

```json
"provenance": {
  "prov:wasDerivedFrom": "model_v00X.json",
  "prov:used": [
    "radiometer_model.json",
    "qa_rfi_model.json"
  ],
  "prov:wasGeneratedBy": "kfm-uncertainty-model-diff-process-v11",
  "prov:generatedAtTime": "2025-11-29T00:00:00Z"
}
```

---

## 🔐 4. Governance, FAIR+CARE, and Sovereignty Compliance

Templates enforce:

- explicit justification for uncertainty decreases  
- sovereignty-floor correctness  
- correct CARE label propagation  
- explicit recognition of Indigenous-land intersections  
- no speculative or undefined model changes  
- full provenance for all adjustments  

All diffs derived from the template are validated through:

- `faircare_validate.yml`  
- `jsonld_validate.yml`  
- `data_pipeline.yml`  

---

## 🧪 5. CI & Schema Validation Requirements

Any diff created from this template must:

- pass JSON Schema validation  
- pass SHACL shape validation  
- include all mandatory governance fields  
- include complete PROV-O lineage  
- show no discontinuities between versions unless documented  
- produce deterministic machine-readable metadata  

Any missing field → **CI Hard Fail**

---

## 🧭 6. Version History

| Version | Date       | Summary                                                                                                        |
|--------:|------------|----------------------------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-29 | First full uncertainty-diff template README; governance/H3 aligned; PROV-O-aligned; CI-safe; emoji-rich.       |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅️ Back](../README.md) · [📊 Uncertainty Model Diffs](../README.md) · [🛡 Governance](../../../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

