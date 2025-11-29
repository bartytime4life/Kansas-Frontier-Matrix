---
title: "📊 NASA SMAP — Calibration Diff Logs (Epoch-to-Epoch Coefficient Changes)"
path: "docs/data/satellites/smap/transforms/calibration/calibration_tables/history/diffs/README.md"
version: "v11.2.2"
last_updated: "2025-11-29"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Calibration Subcommittee · FAIR+CARE Council Oversight"
status: "Active / Enforced"

license: "MIT"
classification: "Public ETL Calibration Change Records"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
provenance_profile: "KFM-PROV-O v11.2"

commit_sha: "<latest-commit>"
previous_version_hash: "<previous-sha>"
doc_integrity_checksum: "<sha256>"

stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"

sbom_ref: "../../../../../../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../../../../../../releases/v11.2.2/data-telemetry.json"
telemetry_schema: "../../../../../../../../../../schemas/telemetry/sat-smap-transforms-v11.json"

governance_ref: "../../../../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

fair_category: "F1-A1-I1-R3"
care_label: "CARE-A (technical metadata) / CARE-B (if used in sovereign-land interpretive workflows)"
indigenous_rights_flag: false
sensitivity_level: "None (non-geospatial diff metadata)"
public_exposure_risk: "Low"
risk_category: "Low"
redaction_required: false

data_steward: "Calibration Subcommittee · Earth Systems Working Group · KFM FAIR+CARE Council"

ontology_alignment:
  cidoc: "E31 Document"
  prov_o: "prov:Entity"
  schema_org: "Dataset"
  owl_time: "TemporalEntity"

json_schema_ref: "../../../../../../../../../../schemas/json/transform-smap-calibration-diffs-v11.json"
shape_schema_ref: "../../../../../../../../../../schemas/shacl/transform-smap-calibration-diffs-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:smap:calibration-diffs-readme:v11.2.2"
semantic_document_id: "kfm-doc-data-smap-calibration-diffs"
event_source_id: "ledger:docs/data/satellites/smap/transforms/calibration/calibration_tables/history/diffs/README.md"
immutability_status: "version-pinned"
machine_extractable: true

accessibility_compliance: "WCAG 2.1 AA+"
ttl_policy: "48 months"
sunset_policy: "Superseded upon next calibration-diff cycle"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 📊 **NASA SMAP — Calibration Diff Logs**  
`docs/data/satellites/smap/transforms/calibration/calibration_tables/history/diffs/README.md`

**Purpose**  
Document **numerical & semantic differences** between SMAP calibration epochs  
(`table_v001.json → table_v002.json`, etc.), including:  
drift corrections, gain adjustments, offset updates, and uncertainty model changes.  
These diffs ensure reproducibility, provenance integrity, and transparent  
FAIR+CARE compliance across calibration cycles.

</div>

---

## 📘 1. Overview

This directory contains **delta records** describing how calibration tables evolve across epochs:

- Gain/offset changes  
- Drift-rate adjustments  
- Calibration metadata updates  
- New or deprecated coefficient groups  
- Uncertainty model changes  
- Validation domain comparisons  
- Impacts on downstream hydrology/climate/archaeology layers  

Diff logs provide **fine-grained traceability** for:

- ETL audits  
- Story Node v3 environmental provenance  
- Focus Mode v3 calibration-aware explanations  
- FAIR+CARE governance reviews  
- Scientific reproducibility  

---

## 🗂️ 2. Directory Layout (Emoji-Rich · Option A)

~~~text
docs/data/satellites/smap/transforms/calibration/calibration_tables/history/diffs/
├── 📄 README.md                         # This file
│
├── 📊 diff_v001_v002.json               # Changes between calibration epochs 001 → 002
├── 📊 diff_v002_v003.json               # Changes between epochs 002 → 003
├── 📊 diff_v003_v004.json               # Changes between epochs 003 → 004
│
└── 🗃️ templates/                        # Optional templates for future diffs
    └── diff_template.json
~~~

Each diff file documents numerical, structural, and semantic changes.

---

## 🧩 3. Required Diff Structure (KFM-CalDiff v11)

Each `diff_*.json` MUST include:

### 🔢 Numeric Differences  
- `gain_delta` (per band, per mode)  
- `offset_delta`  
- `drift_delta`  
- `mode_specific_delta[]`  

### 🧬 Uncertainty Differences  
- `uncertainty_floor_change`  
- `noise_model_change`  
- `propagation_rule_change`  

### 📄 Metadata Changes  
- `calibration_version_old`  
- `calibration_version_new`  
- `valid_from` / `valid_to` deltas  
- `nasa_product_source_change`  

### 🔐 Governance & FAIR+CARE Effects  
- Does the calibration change influence visible environmental interpretation?  
- Does it impact Indigenous land–adjacent climate/soil variables?  
- Does it require updated `"kfm:mask_required"` logic downstream?  

### 🧾 Provenance Block  
- `prov:wasDerivedFrom` previous epoch  
- `prov:used` NASA sources  
- `prov:generatedAtTime` timestamp  
- `prov:wasGeneratedBy` calibration-diff process  

---

## 🔐 4. Governance & Sovereignty Notes

Even though calibration tables are **non-geospatial**, diffs influence **interpretation** of:

- Soil moisture patterns  
- Freeze/thaw classification  
- Vegetation water content  
- QA/RFI signal quality  

Thus each diff MUST declare:

- Whether calibration changes alter environmental interpretation  
- Whether uncertainty was reduced (flagged!)  
- Whether masking behavior should be stricter in sensitive H3 regions  
- CARE label continuity  
- Sovereignty review triggers (if interpretive impact is non-trivial)

Governance validation runs under:

- `faircare_validate.yml`  
- `jsonld_validate.yml`  
- `data_pipeline.yml`

---

## 🧪 5. QA & Validation Requirements

Each diff log must:

- Pass JSON Schema validation  
- Match calibration table structure exactly  
- Accurately represent all coefficient changes  
- Declare downstream impacts (if any)  
- Avoid speculative or undefined fields  
- Provide machine-extractable provenance  

Test coverage verified via:

```
docs/data/satellites/smap/transforms/calibration/tests/
```

---

## 🔁 6. Placement in the Full ETL Pipeline

~~~text
decode
 → reprojection
 → calibration
    → uses calibration_tables/*
    → uses history/*
    → uses diffs/* (this directory)
 → QA/RFI integration
 → uncertainty propagation
 → governance masking
 → STAC/DCAT metadata generation
 → PROV-O lineage export
 → OpenLineage telemetry
~~~

Diff logs ensure **epoch-to-epoch auditability**.

---

## 🔮 7. Applications Inside KFM

### Hydrology  
- Stability of moisture fields across calibration cycles  

### Climate  
- Consistency in VWC anomaly detection  

### Archaeology  
- Calibration-aware visibility/environmental reconstructions  

### Story Node v3  
- “How calibration changed this dataset” provenance explanations  

### Focus Mode v3  
- Calibration-aware environmental context (“This value was produced using epoch v002…”)  

---

## 🧭 8. Version History

| Version | Date       | Summary                                                                                                  |
|--------:|------------|----------------------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-29 | Full diff-history README; emoji layout; PROV-O alignment; governance-aware; CI-safe; KFM-CalDiff v11.2. |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅️ Back](../README.md) · [🎚️ Calibration History](../README.md) · [🛡 Governance](../../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

