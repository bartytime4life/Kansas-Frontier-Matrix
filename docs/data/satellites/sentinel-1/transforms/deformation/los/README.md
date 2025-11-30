---
title: "🌍 Sentinel-1 InSAR — LOS Displacement (Generalized & Sovereignty-Protected Deformation Outputs)"
path: "docs/data/satellites/sentinel-1/transforms/deformation/los/README.md"
version: "v11.2.2"
last_updated: "2025-11-29"

classification: "High-Sensitivity (CARE-B · Sovereignty-Generalized)"
status: "Active · Enforced"
release_stage: "Stable · Governed"
lifecycle: "LTS"
review_cycle: "Quarterly · FAIR+CARE Council + Remote Sensing WG"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
provenance_profile: "KFM-PROV-O v11.2"

commit_sha: "<latest>"
previous_version_hash: "<prev>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../../../releases/v11.2.2/data-telemetry.json"
telemetry_schema: "../../../../../../../schemas/telemetry/sat-deformation-los-v11.json"

governance_ref: "../../../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

fair_category: "F4-A2-I3-R5"
care_label: "CARE-B"
indigenous_rights_flag: true
sensitivity_level: "High"
public_exposure_risk: "High"
risk_category: "Very High"
redaction_required: true

data_steward: "Remote Sensing Working Group"

ontology_alignment:
  cidoc: "E84 Information Carrier"
  schema_org: "Dataset"
  prov_o: "prov:Entity"
  owl_time: "Interval"
  geosparql: "geo:Feature"

json_schema_ref: "../../../../../../../schemas/json/sentinel1-los-v11.json"
shape_schema_ref: "../../../../../../../schemas/shacl/sentinel1-los-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:sentinel1:transform-deformation-los:v11.2.2"
semantic_document_id: "kfm-doc-data-sentinel1-transform-deformation-los"
event_source_id: "ledger:docs/data/satellites/sentinel-1/transforms/deformation/los/README.md"
immutability_status: "version-pinned"
machine_extractable: true

accessibility_compliance: "WCAG 2.1 AA+"
ttl_policy: "24 months"
sunset_policy: "Superseded on next LOS deformation model update"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 🌍 **Sentinel-1 InSAR — LOS Displacement Directory**  
`docs/data/satellites/sentinel-1/transforms/deformation/los/`

Contains **sovereignty-generalized Line-Of-Sight (LOS) displacement** rasters produced  
after phase unwrapping. These are the **final deformation outputs** used in  
STAC Items, Focus Mode, Story Nodes, hazard mapping, and long-term land motion analysis.

</div>

---

## 🗂️ 1. Directory Layout (STRICT OPTION-A EMOJI STYLE)

~~~text
docs/data/satellites/sentinel-1/transforms/deformation/los/
├── 📄 README.md
│
├── 🌍 los_displacement_202501.tif        # Sovereignty-generalized LOS displacement map
├── 🌍 los_displacement_202503.tif        # Additional LOS displacement output
└── 🌍 los_displacement_202506.tif        # Additional LOS displacement output(s)
~~~

✔ Emoji BEFORE filenames  
✔ No drift  
✔ Matches interferograms/, unwrapped/, coherence/, rtc/ patterns  
✔ Box-safe (no nested code fences)

---

## 📘 2. Purpose

This directory contains **generalized LOS displacement rasters** derived from:

```
interferograms/ → unwrapped/ → LOS conversion → sovereignty generalization
```

LOS displacement is a **high-sensitivity geophysical indicator** showing:

- subsidence  
- uplift  
- fault/structural shifts  
- hydrologic drawdown  
- terrain instability  

Because of sensitivity, all LOS rasters here are **sovereignty-generalized**.

---

## 🧩 3. How LOS Displacement Is Produced

### 1️⃣ LOS Vector Computation  
Using orbit geometry:

- look vector  
- incidence angle  
- slant-range geometry  

### 2️⃣ Apply LOS Projection  
Convert unwrapped phase to LOS displacement:

~~~text
displacement_los = (phase_unwrapped · λ) / (4π · cos(incidence_angle))
~~~

### 3️⃣ Sovereignty Generalization (MANDATORY)

Generalization rules:

- **H3 coarse generalization** (resolution reduction)  
- **uncertainty flooring** (minimum noise floor)  
- **low-pass spatial smoothing** for sovereign H3 cells  
- explicit `"sovereignty_generalized": true` metadata flag  

### 4️⃣ Output  
Generalized, analysis-ready LOS displacement rasters.

---

## 🔗 4. PROV-O Lineage

Each LOS raster is a **prov:Entity**:

~~~json
{
  "prov:Entity": "s1_los_displacement_202501",
  "prov:used": [
    "unwrapped_phase",
    "orbit_metadata",
    "rtc_dem",
    "incidence_angle"
  ],
  "prov:wasGeneratedBy": "s1_los_displacement_generation",
  "kfm:care_label": "CARE-B",
  "kfm:h3_sensitive": true,
  "kfm:mask_required": true,
  "kfm:sovereignty_generalized": true
}
~~~

---

## 🔐 5. FAIR+CARE & Sovereignty Requirements

LOS displacement is **one of the most sensitive SAR derivatives**.

Mandatory governance applies:

- `"kfm:care_label" = "CARE-B"`
- `"kfm:h3_sensitive" = true`
- `"kfm:mask_required" = true`
- `"kfm:sovereignty_uncertainty_floor"` must be applied
- `"kfm:sovereignty_generalized" = true`
- **NO raw LOS displacement is ever released**

These rasters are always **post-generalization**.

---

## 🧪 6. CI Validation Requirements

CI verifies:

- correct LOS projection math  
- sovereign generalization rules applied  
- `"kfm:*"` metadata present and correct  
- consistency with fixtures  
- deterministic outputs  
- correct CRS + grid alignment  
- schema + SHACL compliance  

Any deviation → **merge blocked**.

---

## 🧭 7. Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v11.2.2 | 2025-11-29 | Initial strict LOS deformation README; emoji-aligned; zero drift. |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅ Back](../README.md) · [🌍 Unwrapped Phase](../unwrapped/README.md) · [🛡 Governance](../../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

