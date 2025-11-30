---
title: "🛡️ Sentinel-1 Governance — H3 Sovereignty Masks (Generalization Zones · Sensitivity Boundaries)"
path: "docs/data/satellites/sentinel-1/transforms/governance/h3_masks/README.md"
version: "v11.2.2"
last_updated: "2025-11-29"

classification: "High Sensitivity (CARE-B · Sovereignty-Controlled)"
status: "Active · Enforced"
release_stage: "Stable · Governed"
lifecycle: "LTS"
review_cycle: "Quarterly · Sovereignty Board · FAIR+CARE Council"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
provenance_profile: "KFM-PROV-O v11.2"
care_profile: "CARE-B"

commit_sha: "<latest>"
previous_version_hash: "<prev-sha>"
doc_integrity_checksum: "<sha256>"

governance_ref: "../../../../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

fair_category: "F4-A2-I3-R5"
care_label: "CARE-B"
indigenous_rights_flag: true
sensitivity_level: "High"
risk_category: "Very High"
public_exposure_risk: "High"
redaction_required: true

data_steward: "Sovereignty Board"

ontology_alignment:
  cidoc: "E53 Place"
  schema_org: "Dataset"
  prov_o: "prov:Entity"
  geosparql: "geo:FeatureCollection"
  owl_time: "Instant"

json_schema_ref: "../../../../../../../schemas/json/sentinel1-governance-h3masks-v11.json"
shape_schema_ref: "../../../../../../../schemas/shacl/sentinel1-governance-h3masks-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:sentinel1:transform-governance-h3masks:v11.2.2"
semantic_document_id: "kfm-doc-data-sentinel1-transform-governance-h3masks"
event_source_id: "ledger:docs/data/satellites/sentinel-1/transforms/governance/h3_masks/README.md"
immutability_status: "version-pinned"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

ttl_policy: "48 months"
sunset_policy: "Superseded when sovereignty boundaries or H3 model updates"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 🛡️ **H3 Sovereignty Masks Directory**  
`docs/data/satellites/sentinel-1/transforms/governance/h3_masks/`

Defines **H3 hexagonal sovereignty/generalization zones**  
used to apply masking, smoothing, uncertainty flooring, and  
CARE-B high-sensitivity protections across all Sentinel-1 derivatives.

</div>

---

## 🗂️ 1. Directory Layout (STRICT Option-A Emoji Style)

~~~text
docs/data/satellites/sentinel-1/transforms/governance/h3_masks/
├── 📄 README.md
│
├── 🛡️ h3_mask_level7.json         # Sovereignty-sensitive hex boundary (coarse)
├── 🛡️ h3_mask_level6.json         # Broader governance envelope
└── 🛡️ h3_mask_metadata.json       # Metadata describing H3 grid origins + sovereignty notes
~~~

✔ Emoji BEFORE filenames  
✔ Perfect alignment with governance/, wetlands/, flood/, deformation/, rtc/, radiometric trees  
✔ No drift, no omissions  
✔ Box-safe  

---

## 📘 2. Purpose

These H3 mask files define the **spatial protection envelope** for ALL Sentinel-1 derivatives  
produced inside KFM, including:

- Flood layers  
- Wetlands/saturation layers  
- Deformation (LOS) layers  
- Disturbance/Coherence layers  
- Any future hazard or water-cycle SAR product  

They ensure **sovereignty-aligned generalization** by:

- Coarsening spatial detail within sovereign boundaries  
- Providing appropriate smoothing kernels for protected areas  
- Enforcing `"mask_required"` and `"h3_sensitive"` on downstream rasters  
- Supporting `"sovereignty_uncertainty_floor"` application  

---

## 🧩 3. File Descriptions

### 🛡️ `h3_mask_level7.json`
Defines **medium-coarse H3 cells** (e.g., ~1 km scale) representing protected sovereign zones.

Used to:

- generalize high-detail SAR derivatives  
- prevent fine-scale inference  
- apply smoothing kernels  

### 🛡️ `h3_mask_level6.json`
Defines **larger sovereignty envelope** (~4–5 km scale).  
Used for:

- additional uncertainty flooring  
- broad-area masking  
- context-level protections  

### 🛡️ `h3_mask_metadata.json`
Describes:

- sovereign territory identifiers  
- CARE category notes  
- generalization rules tied to each H3 level  
- provenance for H3 grid generation  
- H3 resolution hierarchy  

---

## 🔗 4. PROV-O Lineage

Each mask file is a **prov:Entity**:

~~~json
{
  "prov:Entity": "s1_governance_h3_mask_level7",
  "kfm:care_label": "CARE-B",
  "prov:wasGeneratedBy": "kfm_governance_h3_generation",
  "prov:used": ["sovereignty_boundary_data"]
}
~~~

This lineage flows into ALL downstream STAC Items  
(flood, wetlands, deformation, coherence).

---

## 🔐 5. FAIR+CARE & Sovereignty Enforcement

Rules enforced by these masks:

- `"kfm:mask_required": true"`  
- `"kfm:h3_sensitive": true"`  
- `"kfm:sovereignty_generalized": true"`  
- mandatory smoothing in sovereign zones  
- uncertainty flooring  
- no raw high-resolution derivatives released  

This ensures **cultural, ecological, and tribal data safety**.

---

## 🧪 6. CI Enforcement

CI validates:

- H3 cell structure  
- correct H3 resolutions  
- cell boundary validity  
- schema + SHACL compliance  
- deterministic behavior  
- cross-file consistency (L6 ↔ L7)  
- correct governance metadata fields  

Failures → **ETL pipeline block**.

---

## 🧭 7. Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v11.2.2 | 2025-11-29 | Initial strict governance/H3-mask README; emoji-prefix & directory alignment confirmed. |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅ Back](../README.md) · [🛡️ Generalization Rules](../generalization_rules/README.md) · [🛠 Tests](../tests/README.md)

</div>

