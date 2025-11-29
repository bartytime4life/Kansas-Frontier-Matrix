---
title: "🧩 NASA SMAP — Calibration Diff Templates (KFM-CalDiff v11.2)"
path: "docs/data/satellites/smap/transforms/calibration/calibration_tables/history/diffs/templates/README.md"
version: "v11.2.2"
last_updated: "2025-11-29"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Annual · Calibration Subcommittee · FAIR+CARE Council Oversight"
status: "Active / Enforced"

classification: "Public Calibration-Template Documentation"
license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
provenance_profile: "KFM-PROV-O v11.2"

commit_sha: "<latest-commit>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../../../../../../releases/v11.2.2/data-telemetry.json"
telemetry_schema: "../../../../../../../../../../schemas/telemetry/sat-smap-transforms-v11.json"

governance_ref: "../../../../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

fair_category: "F1-A1-I1-R3"
care_label: "CARE-A / CARE-B (inherited from calibration history context)"
indigenous_rights_flag: false
sensitivity_level: "None (non-geospatial templates)"
public_exposure_risk: "Low"
risk_category: "Low"
redaction_required: false

data_steward: "Calibration Subcommittee · Earth Systems Working Group · KFM FAIR+CARE Council"

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "Dataset"
  prov_o: "prov:Plan"
  owl_time: "TemporalEntity"

json_schema_ref: "../../../../../../../../../../schemas/json/transform-smap-calibration-diffs-template-v11.json"
shape_schema_ref: "../../../../../../../../../../schemas/shacl/transform-smap-calibration-diffs-template-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:smap:calibration-diffs-templates-readme:v11.2.2"
semantic_document_id: "kfm-doc-data-smap-calibration-diff-templates"
event_source_id: "ledger:docs/data/satellites/smap/transforms/calibration/calibration_tables/history/diffs/templates/README.md"
immutability_status: "version-pinned"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
ttl_policy: "48 months"
sunset_policy: "Superseded upon new calibration template framework release"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 🧩 **NASA SMAP — Calibration Diff Templates**  
`docs/data/satellites/smap/transforms/calibration/calibration_tables/history/diffs/templates/README.md`

**Purpose**  
Provide the **official template framework** for generating new  
SMAP calibration diff logs (`diff_vXXX_vYYY.json`).  
Templates enforce *strict reproducibility*, *FAIR+CARE governance*,  
*PROV-O provenance*, and *STAC/DCAT alignment* when documenting  
changes across calibration epochs.

</div>

---

## 📘 1. Overview

Templates in this directory define:

- Required **JSON keys** for KFM-CalDiff v11  
- Numerical delta fields (gain, offset, drift)  
- Uncertainty model fields  
- CARE/H3 governance impact fields  
- NASA documentation linkage fields  
- PROV-O lineage anchors  
- Template commentary blocks for calibration-team reviewers  

These templates standardize how SMAP calibration diffs are authored across years and mission updates.

---

## 🗂️ 2. Directory Layout (Emoji-Rich · Option A)

~~~text
docs/data/satellites/smap/transforms/calibration/calibration_tables/history/diffs/templates/
├── 📄 README.md                      # This file
│
└── 🧩 diff_template.json             # Authoritative template for calibration diff creation
~~~

Only **approved templates** are permitted here.  
Calibration engineers must clone this template when creating a new diff file.

---

## 🧱 3. Structure of `diff_template.json`

The template MUST define:

### 1. Calibration Epoch Metadata
- `calibration_version_old`
- `calibration_version_new`
- `nasa_product_version_old`
- `nasa_product_version_new`
- `valid_from`, `valid_to`

### 2. Numerical Delta Blocks  
Each required block MUST appear:

- `gain_delta[]`
- `offset_delta[]`
- `drift_delta[]`
- `mode_specific_delta[]`

Values must follow KFM numeric conventions  
(no undefined units, no speculative ranges).

### 3. Uncertainty Model Delta
- `uncertainty_floor_change`
- `noise_model_change`
- `propagation_rule_change`
- `uncertainty_notes`

These fields enforce *traceable uncertainty evolution*  
and ensure **no hidden false certainty** is introduced.

### 4. Governance & CARE/H3 Impact
- `governance_note`
- `care_label_change` (if any)
- `h3_sensitivity_change`
- `"masking_implication"`: true/false
- `"requires_sovereignty_review"`: true/false

Calibration changes can affect derived environmental interpretations,  
so governance flags are mandatory.

### 5. PROV-O Block
Every diff MUST include:

```json
"provenance": {
  "prov:wasDerivedFrom": "...",
  "prov:used": ["…"],
  "prov:generatedAtTime": "…",
  "prov:wasGeneratedBy": "kfm-calibration-diff-process-v11"
}
```

This ensures perfect lineage traceability in the Knowledge Graph.

---

## 🔐 4. Governance, FAIR+CARE & Sovereignty Enforcement

The diff template enforces:

- Ethical tracking of calibration-induced interpretation changes  
- Accurate review of any uncertainty decrease near sensitive areas  
- Strict disallowance of speculative or undocumented calibration shifts  
- Review-triggering if calibration affects Indigenous landscape interpretation  
- Sovereignty safeguards through `"requires_sovereignty_review": true`  

All generated diff files must pass:

- `faircare_validate.yml`  
- `jsonld_validate.yml`  
- `data_pipeline.yml`  

---

## 🧪 5. Validation & CI Requirements

Template-based diffs must pass:

- JSON Schema validation (`transform-smap-calibration-diffs-template-v11.json`)
- SHACL conformance (shape-based field checks)
- Toolchain validation using decode/reprojection/calibration tests
- Governance/CARE/H3 checks

If **any** required field is missing → **CI Hard Fail**.

---

## 🔁 6. How Templates Integrate With Full ETL

~~~text
decode
 → reprojection
 → calibration
    → calibration_tables/*
    → history/*
    → diffs/* (template-generated)
 → QA/RFI integration
 → uncertainty propagation
 → governance masking
 → STAC/DCAT metadata registration
 → PROV-O lineage export
 → OpenLineage telemetry
~~~

Diff templates enforce **consistent calibration evolution** across the entire KFM pipeline.

---

## 🔮 7. Applications Inside KFM

### Calibration Engineering  
- Rapid creation of valid calibration diffs  
- Enforcement of consistent structure  
- Guaranteed safety under governance rules  

### Scientific Reanalysis  
- Compare epochs and detect anomalies in SMAP calibration  

### Story Node v3  
- “Calibration provenance” overlays for environmental narratives  

### Focus Mode v3  
- Calibration-aware environmental explanations  

### FAIR+CARE & Governance  
- Provide transparency to Indigenous communities & reviewers  

---

## 🧭 8. Version History

| Version | Date       | Summary                                                                                                      |
|--------:|------------|--------------------------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-29 | First complete calibration-diff template README; governance/H3 integration; PROV-O alignment; CI-safe.       |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅️ Back](../README.md) · [📊 Calibration Diffs](../README.md) · [🛡 Governance](../../../../../../../standard)

