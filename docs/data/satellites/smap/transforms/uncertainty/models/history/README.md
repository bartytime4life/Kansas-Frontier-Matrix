---
title: "🕰️ NASA SMAP — Uncertainty Model History (Radiometer · QA/RFI · Combined) · ETL Stage 5"
path: "docs/data/satellites/smap/transforms/uncertainty/models/history/README.md"
version: "v11.2.2"
last_updated: "2025-11-29"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Uncertainty Subcommittee · FAIR+CARE Council"
status: "Active / Enforced"

classification: "Public ETL Modeling History"
license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
provenance_profile: "KFM-PROV-O v11.2"

commit_sha: "<latest-commit>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../../../../../releases/v11.2.2/data-telemetry.json"
telemetry_schema: "../../../../../../../../../schemas/telemetry/sat-smap-transforms-v11.json"

governance_ref: "../../../../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

fair_category: "F1-A1-I2-R4"
care_label: "CARE-A/B (depends on variable sensitivity)"
indigenous_rights_flag: true
sensitivity_level: "Medium"
public_exposure_risk: "Low"
risk_category: "Low–Medium"
redaction_required: false

data_steward: "Uncertainty Subcommittee · Earth Systems Working Group · KFM FAIR+CARE Council"

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "Dataset"
  prov_o: "prov:Entity"
  owl_time: "TemporalEntity"

json_schema_ref: "../../../../../../../../../schemas/json/transform-smap-uncertainty-model-history-v11.json"
shape_schema_ref: "../../../../../../../../../schemas/shacl/transform-smap-uncertainty-model-history-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:smap:uncertainty-model-history-readme:v11.2.2"
semantic_document_id: "kfm-doc-data-smap-uncertainty-model-history"
event_source_id: "ledger:docs/data/satellites/smap/transforms/uncertainty/models/history/README.md"
immutability_status: "version-pinned"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
ttl_policy: "30 months"
sunset_policy: "Superseded when uncertainty model is upgraded"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 🕰️ **NASA SMAP — Uncertainty Model History (ETL Stage 5)**  
`docs/data/satellites/smap/transforms/uncertainty/models/history/README.md`

**Purpose**  
Record the **evolution** of SMAP uncertainty models (radiometer-only, QA/RFI, combined)  
across KFM releases, calibration epochs, and NASA model updates.  
Ensures reproducibility, scientific traceability, FAIR+CARE governance compliance,  
and predictable behavior for Story Node v3 and Focus Mode v3 environmental reasoning.

</div>

---

## 📘 1. Overview

This directory tracks **versioned uncertainty models** used in ETL Stage 5:

- 🧮 Radiometer uncertainty models  
- ⚠️ QA/RFI-driven uncertainty models  
- 🔗 Combined uncertainty models  
- 📉 Sovereignty-aware minimum uncertainty floors  
- 📏 Error propagation method changes  
- 🔐 Governance-related uncertainty policies  

Models stored here feed into:

- `propagate_uncertainty.py`  
- STAC `uncertainty` asset generation  
- DCAT uncertainty metadata  
- Story Node v3 uncertainty narratives  
- Focus Mode v3 environmental confidence scoring  

---

## 🗂️ 2. Directory Layout (Emoji-Rich · Option A)

~~~text
docs/data/satellites/smap/transforms/uncertainty/models/history/
├── 📄 README.md                     # This file
│
├── 🧮 model_v001.json               # First published uncertainty model
├── 🧮 model_v002.json               # Second uncertainty model version
├── 🧮 model_v003.json               # Latest uncertainty update
│
└── 📊 diffs/                        # Model-to-model deltas
    ├── diff_v001_v002.json
    ├── diff_v002_v003.json
    └── diff_v003_v004.json         # Reserved for future updates
~~~

Files must follow:

- KFM-UncertaintyModel v11 schema  
- PROV-O lineage patterns  
- FAIR+CARE metadata requirements  

---

## 🧩 3. Required Model Fields

### Each `model_vXXX.json` MUST include:

- `model_version`  
- `radiometer_uncertainty` block  
- `qa_rfi_uncertainty` block  
- `combined_uncertainty` block  
- `uncertainty_floor_rules` (incl. sovereignty-aware floors)  
- `propagation_rules`  
- `nasa_source_model`  
- `kfm_adjustments`  
- PROV-O lineage:  
  - `prov:used`  
  - `prov:wasGeneratedBy`  
  - `prov:wasDerivedFrom`  
  - `prov:generatedAtTime`

---

## 📊 4. Diff Logs (Model Evolution)

Each diff file (`diff_vXXX_vYYY.json`) MUST describe:

- Numeric uncertainty deltas  
- Changes in noise model parameters  
- RFI → uncertainty multiplier changes  
- Governance-related uncertainty-floor changes  
- Calibration-epoch-coupled uncertainty shifts  
- NASA source model changes  
- KFM adjustments with justification  
- FAIR+CARE impact explanation  
- PROV-O metadata documenting lineage  

Diffs ensure transparency in uncertainty evolution affecting hydrology, climate, archaeology,  
Story Nodes, and Focus Mode.

---

## 🔐 5. Governance & Sovereignty Implications

Uncertainty models influence how environmental signals are interpreted across:

- Tribal lands  
- Sensitive ecological regions  
- Archaeological landscapes  
- Multi-sensor fused climate signals  

Thus:

- Sovereignty-aware uncertainty floors MUST remain in place  
- Uncertainty **must never artificially decrease** near sensitive areas  
- `"kfm:mask_required"` flags propagate where uncertainty implies ethical risk  
- CARE classification preserved for all uncertainty outputs  

Validated via:

- `faircare_validate.yml`  
- `jsonld_validate.yml`  
- `data_pipeline.yml`

---

## 🧪 6. QA & Validation Requirements

Model history validation includes:

- JSON Schema validation across all versions  
- SHACL shape conformance  
- Diff verification (no undocumented changes)  
- Consistency with decode/reprojection/calibration models  
- Check that uncertainty floors escalate or remain stable, never decrease  
- PROV-O lineage correctness  

Any violation → **CI Hard Fail**

---

## 🔁 7. Integration Into Full ETL Pipeline

~~~text
decode
 → reprojection
 → calibration
 → QA/RFI integration
 → uncertainty propagation (uses model history)
 → governance masking (CARE/H3)
 → STAC/DCAT dataset creation
 → PROV-O lineage export
 → OpenLineage telemetry
~~~

Uncertainty model history ensures **scientifically traceable** outputs across KFM releases.

---

## 🔮 8. Applications Inside KFM

### Hydrology  
- Stable soil-moisture confidence layers  

### Climate  
- Uncertainty-aware VWC and FT anomalies  

### Archaeology  
- Mitigate risk of overconfidence in environmentally sensitive zones  

### Story Node v3  
- Temporal narratives enriched with uncertainty evolution  

### Focus Mode v3  
- Uncertainty-weighted explanations for environmental layers  

---

## 🧭 9. Version History

| Version | Date       | Summary                                                                                               |
|--------:|------------|-------------------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-29 | Full uncertainty-model history README; emoji layout; governance-aware; STAC/DCAT/PROV-compliant.      |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅️ Back](../README.md) · [🧮 Uncertainty Models](../README.md) · [🛡 Governance](../../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

