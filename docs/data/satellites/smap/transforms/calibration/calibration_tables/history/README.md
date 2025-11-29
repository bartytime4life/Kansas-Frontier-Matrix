---
title: "🕰️ NASA SMAP — Calibration Table History & Diff Records (Radiometer Drift/Gain Epochs)"
path: "docs/data/satellites/smap/transforms/calibration/calibration_tables/history/README.md"
version: "v11.2.2"
last_updated: "2025-11-29"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Calibration Subcommittee · FAIR+CARE Council"
status: "Active / Enforced"

commit_sha: "<latest-commit>"
previous_version_hash: "<previous-sha>"
doc_integrity_checksum: "<sha256>"

classification: "Public ETL Calibration History"
license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
provenance_profile: "KFM-PROV-O v11.2"

sbom_ref: "../../../../../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../../../../../releases/v11.2.2/data-telemetry.json"
telemetry_schema: "../../../../../../../../../schemas/telemetry/sat-smap-transforms-v11.json"

governance_ref: "../../../../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

fair_category: "F1-A1-I1-R3"
care_label: "CARE-A / CARE-B (values inherit from parent datasets)"
indigenous_rights_flag: false
sensitivity_level: "None (technical calibration metadata only)"
public_exposure_risk: "Low"
risk_category: "Low"
redaction_required: false

data_steward: "Calibration Subcommittee · Earth Systems Working Group · KFM FAIR+CARE Council"

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  prov_o: "prov:Entity"
  schema_org: "Dataset"
  owl_time: "TemporalEntity"

json_schema_ref: "../../../../../../../../../schemas/json/transform-smap-calibration-tables-history-v11.json"
shape_schema_ref: "../../../../../../../../../schemas/shacl/transform-smap-calibration-tables-history-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:smap:calibration-tables:history-readme:v11.2.2"
semantic_document_id: "kfm-doc-data-smap-calibration-history"
event_source_id: "ledger:docs/data/satellites/smap/transforms/calibration/calibration_tables/history/README.md"
immutability_status: "version-pinned"
machine_extractable: true

accessibility_compliance: "WCAG 2.1 AA+"
ttl_policy: "48 months"
sunset_policy: "Superseded upon next calibration epoch migration"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 🕰️ **NASA SMAP — Calibration Table History & Diff Records**  
`docs/data/satellites/smap/transforms/calibration/calibration_tables/history/README.md`

**Purpose**  
Document **all historical calibration epochs**, including deprecated tables,  
inter-epoch diffs, and calibration-lineage metadata used to ensure  
reproducibility, FAIR+CARE compliance, STAC provenance, and  
stable cross-epoch hydrology/climate/archaeology interpretation.

</div>

---

## 📘 1. Overview

This directory stores the **history and evolution** of SMAP calibration tables, including:

- Epoch-to-epoch coefficient changes  
- Drift updates  
- Gain/offset updates  
- Version deprecations  
- Diff logs explaining numerical and uncertainty changes  
- Provenance connections to NASA radiometer calibration bulletins  
- FAIR+CARE governance notes where calibration shifts affect environmental interpretation  

These historical files provide **traceability** and **decision transparency** across the entire KFM system.

---

## 🗂️ 2. Directory Layout (Emoji-Rich · Option A)

~~~text
docs/data/satellites/smap/transforms/calibration/calibration_tables/history/
├── 📄 README.md                        # This file
│
├── 🗃️ table_v000_legacy.json           # Pre-v001 legacy calibration (deprecated)
├── 🗃️ table_v001.json                  # First KFM-verified calibration epoch
├── 🗃️ table_v002.json                  # Second calibration epoch
├── 🗃️ table_v003.json                  # Third calibration epoch
│
└── 📊 diffs/                           # Numeric & semantic change logs
    ├── diff_v001_v002.json
    ├── diff_v002_v003.json
    └── diff_v003_v004.json
~~~

All files must follow:

- **KFM-CalTable v11 JSON Schema**  
- **PROV-O provenance metadata**  
- **FAIR+CARE governance fields**  
- **Machine extractability** rules  

---

## 🧩 3. Calibration History Requirements

### Each historical table MUST include:

- `calibration_version`  
- `nasa_product_version`  
- `valid_from` / `valid_to`  
- Complete **coefficient groups**:
  - radiometer gain  
  - offset  
  - drift per year  
  - mode-specific corrections  
- Uncertainty model for that epoch  
- PROV-O fields:
  - `prov:used` (source NASA products)  
  - `prov:wasGeneratedBy` (KFM calibration step)  
  - `prov:wasDerivedFrom` previous epoch  
- CARE notation when calibration affects environmental interpretability  

---

## 📊 4. Diff Logs (Inter-Epoch Changes)

Diff files (`diff_v001_v002.json`, etc.) must detail:

- Numeric deltas for each coefficient  
- Drift-rate changes  
- Offset and gain shifts  
- Changes in uncertainty floors  
- Updated calibration assumptions  
- NASA documentation references  
- KFM transparency notes for Story Node v3 / Focus Mode v3  

These diffs are **inputs** into Story Node v3 “environmental change provenance” and  
Focus Mode v3 “calibration explanation” paths.

---

## 🔐 5. Governance, FAIR+CARE & Sovereignty

Although calibration tables are **non-geospatial**, changes in calibration can affect:

- environmental interpretation  
- sensitivity of anomaly detection  
- perceived environmental gradients  

Thus governance rules require:

- CARE labels in metadata  
- Sovereignty awareness when calibration affects derived products used on Indigenous lands  
- No reduction in uncertainty that could produce **false certainty**  
- Never sharpening environmental contrasts in sensitive areas  

Governance is validated through:

- `faircare_validate.yml`  
- `jsonld_validate.yml`  
- `data_pipeline.yml`  

---

## 🧪 6. QA & Validation

Each historical calibration table:

- Undergoes schema validation  
- Gets compared with previous versions  
- Must not contain breaking coefficient changes without diff documentation  
- Must maintain monotonic uncertainty behavior  
- Must pass reproducibility tests in:

```
docs/data/satellites/smap/transforms/calibration/tests/
```

All diffs are tested against expected value ranges and acceptable drift patterns.

---

## 🔁 7. Placement in the Full ETL Pipeline

~~~text
decode
 → reprojection
 → calibration (uses history/* and diffs/*)
 → QA/RFI integration
 → uncertainty propagation
 → governance masking
 → STAC Item/Collection creation
 → DCAT metadata registration
 → PROV-O lineage export
 → OpenLineage telemetry
~~~

Historical tables ensure **auditability** across calibration epochs.

---

## 🔮 8. Applications Inside KFM

### Hydrology  
- Stable soil moisture inference across calibration epochs  

### Climate  
- Consistent VWC anomaly detection  

### Archaeology  
- Avoid misinterpretation caused by calibration-induced environmental contrast changes  

### Story Node v3  
- “Environmental provenance” explanations referencing calibration epoch  
- Calibration-aware narratives  

### Focus Mode v3  
- Accurate calibration-aware reasoning & metadata surfacing  

---

## 🧭 9. Version History

| Version | Date       | Summary                                                                                                  |
|--------:|------------|----------------------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-29 | Complete calibration-history README; diffs; governance/H3 alignment; CI-safe; KFM-CalTable v11 schema.   |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅️ Back](../README.md) · [🎚️ Calibration Tables](../README.md) · [🛡 Governance](../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

