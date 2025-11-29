---
title: "📊 NASA SMAP — Uncertainty Model Diff Logs (Model-to-Model Delta Records) · ETL Stage 5"
path: "docs/data/satellites/smap/transforms/uncertainty/models/history/diffs/README.md"
version: "v11.2.2"
last_updated: "2025-11-29"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Uncertainty Subcommittee · FAIR+CARE Council"
status: "Active / Enforced"

classification: "Public Model Evolution Logs"
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

fair_category: "F1-A1-I2-R4"
care_label: "CARE-A / CARE-B (depending on model impact)"
indigenous_rights_flag: true
sensitivity_level: "Medium (uncertainty impacts interpretation)"
public_exposure_risk: "Low"
risk_category: "Low–Medium"
redaction_required: false

data_steward: "Uncertainty Subcommittee · Earth Systems Working Group · KFM FAIR+CARE Council"

ontology_alignment:
  cidoc: "E31 Document"
  schema_org: "Dataset"
  prov_o: "prov:Entity"
  owl_time: "TemporalEntity"

json_schema_ref: "../../../../../../../../../../schemas/json/transform-smap-uncertainty-diffs-v11.json"
shape_schema_ref: "../../../../../../../../../../schemas/shacl/transform-smap-uncertainty-diffs-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:smap:uncertainty-diffs-readme:v11.2.2"
semantic_document_id: "kfm-doc-data-smap-uncertainty-diffs"
event_source_id: "ledger:docs/data/satellites/smap/transforms/uncertainty/models/history/diffs/README.md"
immutability_status: "version-pinned"
machine_extractable: true

accessibility_compliance: "WCAG 2.1 AA+"
ttl_policy: "30 months"
sunset_policy: "Superseded upon uncertainty-model evolution"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 📊 **NASA SMAP — Uncertainty Model Diff Logs (ETL Stage 5)**  
`docs/data/satellites/smap/transforms/uncertainty/models/history/diffs/README.md`

**Purpose**  
Provide **machine-verifiable, governance-aligned delta records** documenting  
changes between SMAP Uncertainty Models (v001 → v002 → v003 → …).  
These diff logs ensure transparent, ethical, scientifically reproducible  
uncertainty evolution across mission epochs and KFM releases.

</div>

---

## 📘 1. Overview

This directory contains the **official change logs** describing how uncertainty models evolve:

- Radiometer noise model updates  
- QA/RFI multiplier changes  
- Calibration-driven uncertainty adjustments  
- Combined-model structural changes  
- Sovereignty-aware floor changes  
- FAIR+CARE governance impact explanations  
- PROV-O provenance lineage updates  

Diff logs support:

- Scientific auditability  
- Ethical environmental interpretation  
- Story Node v3 uncertainty-aware narratives  
- Focus Mode v3 uncertainty-weighted reasoning  
- Cross-epoch comparison of environmental confidence levels  

---

## 🗂️ 2. Directory Layout (Emoji-Rich · Option A)

~~~text
docs/data/satellites/smap/transforms/uncertainty/models/history/diffs/
├── 📄 README.md                          # This file
│
├── 📊 diff_v001_v002.json                # Model evolution from v001 → v002
├── 📊 diff_v002_v003.json                # Model evolution from v002 → v003
├── 📊 diff_v003_v004.json                # Reserved for future update
│
└── 🧩 templates/                         # Authoritative diff templates
    └── diff_template.json
~~~

Each diff file MUST be complete, machine-readable, and FAIR+CARE compliant.

---

## 🧩 3. Required Fields in Diff Logs (KFM-UncertaintyDiff v11)

Each `diff_*.json` MUST contain:

### 1. 🔢 Numeric Uncertainty Deltas
- radiometer noise delta  
- QA/RFI multiplier delta  
- calibration-linked uncertainty shift  
- uncertainty-floor delta  

### 2. 🧬 Structural Differences
- new or deprecated model keys  
- changes to propagation rules  
- changes to sovereignty-floor definitions  

### 3. ⚠️ Governance & Sovereignty Effects
- `"kfm:mask_required"` changes  
- `"kfm:sovereignty_uncertainty_floor"` adjustments  
- whether uncertainty decreased (⚠️ must be reviewed!)  
- CARE label impacts  
- Indigenous data–relevant explanations  

### 4. 🧾 Provenance (PROV-O)
Each diff MUST include:

```json
"provenance": {
  "prov:wasDerivedFrom": "model_v00X.json",
  "prov:used": ["radiometer_model.json", "qa_rfi_model.json"],
  "prov:generatedAtTime": "2025-11-29T00:00:00Z",
  "prov:wasGeneratedBy": "kfm-uncertainty-model-diff-process-v11"
}
```

### 5. 📚 NASA Source Model Changes
- NASA uncertainty adjustments  
- sensor-level updates  
- algorithm version changes  

---

## 🔐 4. Governance, Sovereignty & FAIR+CARE Integration

Uncertainty changes can **directly affect interpretability** of:

- hydrology  
- climate  
- archaeology  
- ecological transitions  
- culturally sensitive landscapes  

Thus diff logs MUST:

- flag all decreases in uncertainty (requires justification)  
- apply sovereignty-floor rules  
- maintain CARE classifications  
- ensure transparency in uncertainty evolution  
- prevent unethical “false certainty” increases  

Validated via:

- `faircare_validate.yml`  
- `jsonld_validate.yml`  
- `data_pipeline.yml`  

---

## 🧪 5. QA & Validation Requirements

Diff logs undergo:

- JSON Schema validation  
- SHACL shape validation  
- Numeric delta consistency  
- Structural diff correctness  
- PROV-O lineage checks  
- Governance compliance checks  
- Comparison against prior diff versions  

Any violation → **CI Hard Stop**

---

## 🔁 6. Placement in the Full ETL Pipeline

~~~text
decode
 → reprojection
 → calibration
 → QA/RFI integration
 → uncertainty propagation
    → uses model history
    → uses diff logs (this directory)
 → governance masking (CARE/H3)
 → STAC/DCAT dataset creation
 → PROV-O lineage export
 → OpenLineage telemetry
~~~

---

## 🔮 7. Applications Inside KFM

### Hydrology  
Maintains stable uncertainty behavior across calibration cycles.

### Climate  
Ensures climate anomalies include uncertainty changes across epochs.

### Archaeology  
Prevents misinterpretation in sensitive regions where uncertainty shifts matter.

### Story Node v3  
Supports “uncertainty evolution” narratives.

### Focus Mode v3  
Delivers uncertainty-aware environmental reasoning.

---

## 🧭 8. Version History

| Version | Date       | Summary                                                                                               |
|--------:|------------|-------------------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-29 | Complete uncertainty-diff README; emoji-rich; governance/H3 compliant; STAC/DCAT/PROV aligned; CI-safe.|

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅️ Back](../README.md) · [🧮 Uncertainty Model History](../README.md) · [🛡 Governance](../../../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

