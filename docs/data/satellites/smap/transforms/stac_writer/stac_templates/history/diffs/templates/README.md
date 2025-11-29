---
title: "🧩 NASA SMAP — STAC Template Diff Templates (KFM-STAC-Diff v11.2)"
path: "docs/data/satellites/smap/transforms/stac_writer/stac_templates/history/diffs/templates/README.md"
version: "v11.2.2"
last_updated: "2025-11-29"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Annual · STAC Review Board · FAIR+CARE Council"
status: "Active / Enforced"

classification: "Public Template Documentation"
license: "MIT"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
provenance_profile: "KFM-PROV-O v11.2"

commit_sha: "<latest-commit>"
previous_version_hash: "<previous-sha>"
doc_integrity_checksum: "<sha256>"

stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
jsonld_profile: "KFM-JSONLD v11"

sbom_ref: "../../../../../../../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../../../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../../../../../../../releases/v11.2.2/data-telemetry.json"
telemetry_schema: "../../../../../../../../../../../schemas/telemetry/sat-smap-transforms-v11.json"

governance_ref: "../../../../../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

fair_category: "F1-A1-I2-R5"
care_label: "CARE-A / CARE-B"
indigenous_rights_flag: true
sensitivity_level: "Medium"
public_exposure_risk: "Low–Medium"
risk_category: "Medium"
redaction_required: false

data_steward: "STAC/DCAT Review Board · FAIR+CARE Council · Earth Systems Working Group"

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "Dataset"
  prov_o: "prov:Plan"
  owl_time: "TemporalEntity"
  geosparql: "geo:Feature"

json_schema_ref: "../../../../../../../../../../../schemas/json/stac-templates-diff-template-v11.json"
shape_schema_ref: "../../../../../../../../../../../schemas/shacl/stac-templates-diff-template-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:smap:stac-templates-diff-template-readme:v11.2.2"
semantic_document_id: "kfm-doc-data-smap-stac-template-diff-templates"
event_source_id: "ledger:docs/data/satellites/smap/transforms/stac_writer/stac_templates/history/diffs/templates/README.md"
immutability_status: "version-pinned"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
ttl_policy: "48 months"
sunset_policy: "Superseded on next template-diff framework revision"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 🧩 **NASA SMAP — STAC Template Diff Template Library**  
`docs/data/satellites/smap/transforms/stac_writer/stac_templates/history/diffs/templates/README.md`

**Purpose**  
Provide the **authoritative JSON template** used to generate all  
STAC Template Diff logs (`diff_vXXX_vYYY.json`) describing version-to-version  
evolution in STAC Collection, Item, Asset, Governance, and PROV-O templates.  
Ensures **governance transparency**, **FAIR+CARE compliance**, and  
**machine-verifiable lineage** for KFM’s STAC metadata evolution.

</div>

---

## 📘 1. Overview

This directory defines the **canonical template** used to create diff logs that capture:

- Changes to STAC Collection templates  
- Changes to STAC Item templates  
- Changes to STAC Asset templates  
- Updates to governance (`kfm:*`) metadata fields  
- Adjustments in uncertainty + QA metadata  
- Evolution of PROV-O lineage blocks  
- Additions/deprecations in DCAT alignment  
- Sovereignty/H3 masking metadata  
- CARE label propagation updates  

All diff files generated from this template must be **CI-validated**,  
**schema-verified**, and **governance-approved**.

---

## 🗂️ 2. Directory Layout (Emoji-Rich · Option A)

~~~text
docs/data/satellites/smap/transforms/stac_writer/stac_templates/history/diffs/templates/
├── 📄 README.md                  # This file
│
└── 🧩 diff_template.json         # Authoritative template for all STAC template diff logs
~~~

---

## 🧱 3. Required Template Structure (KFM-STAC-Diff v11)

Each diff created from `diff_template.json` MUST contain:

### 1. 📅 Version Metadata
- `"template_version_old"`  
- `"template_version_new"`  
- `"valid_from"`  
- `"valid_to"`  
- `"stac_schema_version"`  
- `"projection_extension_version"`  
- `"governance_extension_version"`  

### 2. 📚 Collection Template Differences
- spatial/temporal extent changes  
- summaries/metadata updates  
- governance extension modifications  
- STAC extension additions/removals  

### 3. 🗂 Item Template Differences
- geometry/bbox schema updates  
- datetime / start_datetime / end_datetime changes  
- projection/raster extension field updates  
- governance metadata field changes  

### 4. 🖼 Asset Template Differences
- asset structure changes  
- role/media_type updates  
- COG, mask, uncertainty, QA asset changes  
- sovereign-mask asset behavior  

### 5. 🧬 Provenance Template Updates
- `prov:wasDerivedFrom`  
- `prov:wasGeneratedBy`  
- `prov:used`  
- updated activity/entity blocks  

### 6. 🛡 Governance + Sovereignty Effects
The template requires explicit reporting of:

- `"care_label_change"`  
- `"h3_sensitivity_change"`  
- `"masking_implication"`  
- `"sovereignty_uncertainty_floor_change"`  
- `"requires_governance_review"`  

### 7. ⚖ FAIR+CARE + STAC/DCAT Compliance Notes
Each diff MUST document:

- STAC v1.0 compliance effect  
- JSON-LD / DCAT v3 impact  
- CARE label propagation impact  
- Uncertainty metadata impact  
- Sovereignty protection implications  

### 8. 🧾 PROV-O Provenance Block
Every generated diff MUST include:

```json
"provenance": {
  "prov:wasDerivedFrom": "stac_templates_v00X.json",
  "prov:used": [
    "collection_template.json",
    "item_template.json",
    "asset_template.json",
    "provenance_template.json"
  ],
  "prov:wasGeneratedBy": "kfm-stac-template-diff-process-v11",
  "prov:generatedAtTime": "2025-11-29T00:00:00Z"
}
```

---

## 🔐 4. Governance, FAIR+CARE, and Sovereignty Compliance

Because template changes govern the **public representation** of SMAP data:

- sovereignty rules MUST remain in the schema  
- uncertainty floors MUST remain represented  
- CARE labels MUST propagate  
- `"kfm:mask_required"` MUST be preserved  
- no template diff may weaken sovereignty protection  
- all metadata interactions MUST be fully auditable  

CI validation enforces:

- `faircare_validate.yml`  
- `jsonld_validate.yml`  
- `stac_validate.yml`  
- schema + SHACL compliance  

---

## 🧪 5. Validation Requirements

Each diff derived from this template must:

- be valid JSON  
- pass JSON Schema & SHACL validation  
- be machine-extractable  
- include all mandatory governance fields  
- pass STAC/DCAT compliance testing  
- include complete provenance metadata  
- be reproducible across ETL cycles  

Any missing required fields → **CI HARD FAIL**.

---

## 🔁 6. Role in Full ETL Pipeline

~~~text
decode
 → reprojection
 → calibration
 → QA/RFI integration
 → uncertainty propagation
 → governance masking
 → STAC Writer
    → uses template history
    → uses diff logs (generated from this template)
 → STAC/DCAT publication
 → PROV-O lineage archival
~~~

---

## 🔮 7. Applications Inside KFM

### Hydrology  
Stable soil-moisture STAC schema evolution.

### Climate  
Predictable FT/VWC STAC models across releases.

### Archaeology  
Governance-safe template evolution ensures cultural protections remain intact.

### Story Node v3  
Stable linking to STAC Items in environmental narratives.

### Focus Mode v3  
STAC lineage and governance metadata consumed in reasoning.

---

## 🧭 8. Version History

| Version | Date       | Summary                                                                                                     |
|--------:|------------|--------------------------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-29 | Initial STAC template-diff template README; governance/H3 aligned; PROV-linked; CI-safe; emoji-rich output. |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅️ Back](../README.md) · [📊 Template Diff Logs](../README.md) · [🛡 Governance](../../../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

