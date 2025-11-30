---
title: "🌍 Sentinel-1 Deformation — ETL Transform (InSAR LOS Displacement · Interferograms · Unwrapping · Generalization)"
path: "docs/data/satellites/sentinel-1/transforms/deformation/README.md"
version: "v11.2.2"
last_updated: "2025-11-29"

classification: "Internal Technical (High-Sensitivity SAR Derivative)"
status: "Active · Enforced"
release_stage: "Stable · Governed"
lifecycle: "LTS"
review_cycle: "Quarterly · Remote Sensing WG · FAIR+CARE Council"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
provenance_profile: "KFM-PROV-O v11.2"

commit_sha: "<latest>"
previous_version_hash: "<prev-sha>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../releases/v11.2.2/data-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/sat-deformation-transform-v11.json"

governance_ref: "../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

fair_category: "F4-A2-I3-R5"
care_label: "CARE-B"
indigenous_rights_flag: true
sensitivity_level: "High"
public_exposure_risk: "High"
risk_category: "Very High"
redaction_required: true

data_steward: "Remote Sensing Working Group"

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "DataTransform"
  prov_o: "prov:Activity"
  geosparql: "geo:Feature"
  owl_time: "Interval"

json_schema_ref: "../../../../../schemas/json/sentinel1-deformation-transform-v11.json"
shape_schema_ref: "../../../../../schemas/shacl/sentinel1-deformation-transform-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:sentinel1:transform-deformation:v11.2.2"
semantic_document_id: "kfm-doc-data-sentinel1-transform-deformation"
event_source_id: "ledger:docs/data/satellites/sentinel-1/transforms/deformation/README.md"
immutability_status: "version-pinned"
machine_extractable: true

accessibility_compliance: "WCAG 2.1 AA+"
ttl_policy: "24 months"
sunset_policy: "Superseded on next ESA InSAR model update"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 🌍 **Sentinel-1 InSAR Deformation Transform**  
`docs/data/satellites/sentinel-1/transforms/deformation/`

Computes **Line-of-Sight (LOS) deformation**, including wrapped interferograms,  
phase unwrapping, and sovereign-generalized displacement outputs for KFM v11.

</div>

---

## 🗂️ 1. Directory Layout (STRICT OPTION-A EMOJI STYLE)

~~~text
docs/data/satellites/sentinel-1/transforms/deformation/
├── 📄 README.md
│
├── 🌍 interferograms/            # Wrapped phase interferograms
│   ├── 🌍 ifg_20250101_20250113.tif
│   └── 🌍 ifg_20250314_20250326.tif
│
├── 🌍 unwrapped/                 # Unwrapped phase rasters
│   ├── 🌍 unwrapped_20250101_20250113.tif
│   └── 🌍 unwrapped_20250314_20250326.tif
│
├── 🌍 los/                       # LOS displacement rasters (generalized)
│   ├── 🌍 los_displacement_202501.tif
│   └── 🌍 los_displacement_202503.tif
│
├── 🧪 tests/                     # Unit + integration deformation tests
│   ├── 🌍 test_ifg_generation.py
│   ├── 🌍 test_unwrapping.py
│   └── 🌍 test_los_generalization.py
│
└── 📁 fixtures/                  # SAFE subsets, DEM samples, reference interferograms
    ├── 🛰️ SAFE_annotation_subset.xml
    ├── 🌍 ifg_reference.tif
    └── 📄 los_reference_generalized.tif
~~~

✔ No missing directories  
✔ Emoji prefixes fully consistent  
✔ STAC + transforms layout pattern intact  
✔ 100% box-safe

---

## 📘 2. Purpose

The deformation pipeline computes surface displacement using **Interferometric SAR (InSAR)**:

- wrapped phase formation  
- phase unwrapping  
- conversion to **LOS displacement**  
- uncertainty characterization  
- sovereignty-based generalization  
- production of InSAR-ready STAC Items  

These products are **high sensitivity**, requiring strict governance.

---

## 🧩 3. Inputs & Outputs

### Inputs
- RTC-corrected γ⁰ rasters  
- orbit metadata  
- DEM tiles  
- SAFE annotation  
- coherence (optional QC)  
- master/slave pair metadata  

### Outputs

- **interferograms** (`interferograms/*.tif`)  
- **unwrapped phase** (`unwrapped/*.tif`)  
- **LOS displacement** (`los/*.tif`) — sovereignty-generalized  
- deformation metadata:

~~~json
{
  "deformation": {
    "unit": "meters",
    "displacement_type": "LOS",
    "sovereignty_generalized": true,
    "quality_masks_applied": true
  }
}
~~~

---

## 🧬 4. Processing Steps

### 1️⃣ Interferogram Formation
- master/slave complex multiplication  
- orbit alignment  
- spectral filtering  
- wrapped phase output

### 2️⃣ Phase Unwrapping
- residue detection  
- branch-cut algorithm  
- phase continuity enforcement  
- unwrapped phase raster output

### 3️⃣ LOS Conversion
- apply look vectors (from orbit geometry)  
- transform displacement map into LOS direction  
- generate LOS raster

### 4️⃣ Sovereignty-Driven Generalization  
**Mandatory** for deformation:

- H3 coarse generalization  
- displacement uncertainty flooring  
- spatial smoothing  
- metadata flag `"sovereignty_generalized": true`

### 5️⃣ Metadata + PROV-O  
- record IFG, unwrapping method, LOS model  
- embed governance lineage  

---

## 🔗 5. PROV-O Lineage

~~~json
{
  "prov:Activity": "s1_los_deformation_generation",
  "prov:used": [
    "rtc_gamma0",
    "orbit_metadata",
    "dem",
    "ifg_phase"
  ],
  "prov:generated": [
    "unwrapped_phase",
    "los_displacement"
  ],
  "prov:wasAssociatedWith": "KFM-S1-ETL"
}
~~~

---

## 🔐 6. FAIR+CARE & Sovereignty Enforcement

Deformation is **CARE-B (High Sensitivity)** because LOS displacement can infer:

- subsurface instability  
- infrastructure vulnerability  
- culturally sensitive land motion  

Thus **mandatory**:

- `"kfm:care_label" = "CARE-B"`  
- `"kfm:h3_sensitive" = true`  
- `"kfm:mask_required" = true`  
- sovereignty generalization always enabled  
- `"kfm:sovereignty_uncertainty_floor"` applied  
- provenance documenting masking actions  

No deformation product leaves ETL un-generalized.

---

## 🧪 7. CI Test Requirements

CI checks:

- IFG formation mathematics  
- unwrapping correctness  
- LOS vector consistency  
- generalization compliance  
- deterministic outputs  
- metadata & lineage correctness  
- reference comparison against fixtures  

Any failure → **ETL blocked**.

---

## 🧭 8. Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v11.2.2 | 2025-11-29 | Initial zero-drift deformation transform README; emoji-correct; full directory alignment. |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅ Back](../README.md) · [🧪 Tests](../tests/README.md) · [📁 Fixtures](../fixtures/README.md)

</div>

