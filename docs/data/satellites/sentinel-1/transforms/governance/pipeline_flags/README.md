---
title: "🛡️ Sentinel-1 Governance — Pipeline Flags (CARE Labels · Sovereignty Signals · Governance Tokens)"
path: "docs/data/satellites/sentinel-1/transforms/governance/pipeline_flags/README.md"
version: "v11.2.2"
last_updated: "2025-11-29"

classification: "High Sensitivity · Governance-Layer Control (CARE-A/B · Sovereignty)"
status: "Active · Enforced"
release_stage: "Stable · Governed"
lifecycle: "LTS"
review_cycle: "Quarterly · Sovereignty Board · FAIR+CARE Council"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
provenance_profile: "KFM-PROV-O v11.2"
care_profile: "CARE-A/B depending on product sensitivity"

commit_sha: "<latest>"
previous_version_hash: "<prev-sha>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../releases/v11.2.2/data-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/sat-governance-pipelineflags-v11.json"

governance_ref: "../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

fair_category: "F4-A2-I3-R5"
care_label: "CARE-B"
indigenous_rights_flag: true
sensitivity_level: "High"
risk_category: "Very High"
public_exposure_risk: "High"
redaction_required: true

data_steward: "Sovereignty Board · Remote Sensing Working Group"

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "DefinedTermSet"
  prov_o: "prov:Entity"
  geosparql: "geo:Feature"
  owl_time: "Instant"

json_schema_ref: "../../../../../schemas/json/sentinel1-governance-pipelineflags-v11.json"
shape_schema_ref: "../../../../../schemas/shacl/sentinel1-governance-pipelineflags-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:sentinel1:transform-governance-pipelineflags:v11.2.2"
semantic_document_id: "kfm-doc-data-sentinel1-transform-governance-pipelineflags"
event_source_id: "ledger:docs/data/satellites/sentinel-1/transforms/governance/pipeline_flags/README.md"
immutability_status: "version-pinned"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

ttl_policy: "48 months"
sunset_policy: "Superseded upon next governance policy update"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 🛡️ **Governance Pipeline Flags Directory**  
`docs/data/satellites/sentinel-1/transforms/governance/pipeline_flags/`

Provides the **CARE**, **sovereignty**, and **governance tokens** used throughout the  
Sentinel-1 ETL pipeline to ensure derivative products are:

**sovereignty-compliant**,  
**FAIR+CARE aligned**,  
**redaction-safe**,  
and **legally + ethically governed**.

</div>

---

## 🗂️ 1. Directory Layout (STRICT Option-A Emoji Style)

~~~text
docs/data/satellites/sentinel-1/transforms/governance/pipeline_flags/
├── 📄 README.md
│
├── 🛡️ care_flags.json              # CARE-A/B classification logic + sensitivity profiles
├── 🛡️ sovereignty_flags.json        # Sovereignty/H3-sensitive flags & protected-region tokens
└── 🛡️ governance_tokens.json        # Global governance signals passed through ETL pipelines
~~~

✔ Emojis BEFORE filenames  
✔ No drift, no missing directories  
✔ Box-safe, perfectly aligned with parent governance structure  

---

## 📘 2. Purpose

Pipeline flags represent the **governance metadata backbone** of  
all Sentinel-1 transforms and outputs inside KFM.

They provide:

- `"kfm:care_label"` → CARE-A/B classification  
- `"kfm:h3_sensitive"` → marks sovereign area sensitivity  
- `"kfm:mask_required"` → signals mandatory masking/generalization  
- `"kfm:sovereignty_generalized"` → ensures sovereignty rules applied  
- `"kfm:uncertainty_floor_applied"` → indicates minimum uncertainty added  
- `"kfm:governance_notes"` → explanation of applied rules  
- `"kfm:restricted_release"` → prevents ungoverned output release  

These flags control **how downstream STAC Items are generated**,  
and how sensitive data is protected in all S1‐based products.

---

## 🧩 3. File Descriptions

### 🛡️ `care_flags.json`
Defines:

- CARE-A (low risk) conditions  
- CARE-B (high sensitivity) triggers  
- hydrology, InSAR, wetlands, flood categories  
- cultural/environmental sensitivity mappings  
- required redaction/generalization behavior for each category  

Example:

~~~json
{
  "care_flags": {
    "flood": "CARE-B",
    "wetlands": "CARE-B",
    "deformation": "CARE-B",
    "coherence": "CARE-B",
    "rtc": "CARE-A"
  }
}
~~~

---

### 🛡️ `sovereignty_flags.json`
Defines:

- sovereign area IDs  
- `"h3_sensitive": true/false`  
- `"mask_required": true/false"`  
- `"sovereignty_generalized": true/false"`  
- region-specific generalization preferences  

Example:

~~~json
{
  "sovereignty": {
    "tribal_territory": {
      "h3_sensitive": true,
      "mask_required": true,
      "sovereignty_generalized": true
    }
  }
}
~~~

---

### 🛡️ `governance_tokens.json`
Defines global governance tokens passed between ETL stages:

- `"kfm:governance_token": "<uuid>"`  
- `"sensitivity_tier"`  
- `"release_constraints"`  
- `"redaction_required"`  
- `"audit_required"`  
- `"internal_only"`  

Example:

~~~json
{
  "tokens": {
    "global_governance_token": "kfm-governance-uuid-v11",
    "audit_required": true,
    "restricted_release": true
  }
}
~~~

---

## 🔗 4. PROV-O Lineage

Pipeline flags appear as:

~~~json
{
  "prov:Entity": "s1_governance_pipeline_flags",
  "prov:label": "Governance Pipeline Flags",
  "kfm:care_label": "CARE-B",
  "kfm:mask_required": true
}
~~~

Every downstream STAC Item for S1 federally-sensitive products must  
reference these governance entities.

---

## 🔐 5. FAIR+CARE & Sovereignty Enforcement

These flags are the **source of truth** for all governance decisions.

Rules enforced:

- `"kfm:h3_sensitive" = true` for protected zones  
- `"kfm:mask_required" = true` for hydrology + InSAR  
- `"kfm:sovereignty_generalized" = true` when needed  
- `"kfm:restricted_release"` controls STAC dissemination  
- `"kfm:uncertainty_floor_applied"` ensures uncertainty is increased in sensitive zones  

This prevents misuse, misinterpretation, and sensitive pattern exposure.

---

## 🧪 6. CI Validation Requirements

CI validates:

- schema correctness for all three files  
- required governance keys present  
- forbidden values absent  
- correct CARE-B alignment  
- consistent sovereignty flags  
- deterministic token behavior  
- governance metadata alignment with upstream transforms  
- STAC compatibility  

Any inconsistency → **ETL pipeline blocked**.

---

## 🧭 7. Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v11.2.2 | 2025-11-29 | Initial strict governance pipeline-flags README; emoji-prefix validated; zero drift. |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅ Back](../README.md) · [🛡️ H3 Masks](../h3_masks/README.md) · [🛡️ Generalization Rules](../generalization_rules/README.md) · [🧪 Governance Tests](../tests/README.md)

</div>

