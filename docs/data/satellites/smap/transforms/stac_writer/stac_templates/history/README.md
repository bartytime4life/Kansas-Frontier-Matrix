---
title: "🕰️ NASA SMAP — STAC Template History (Collections · Items · Assets · Provenance) · ETL Finalization"
path: "docs/data/satellites/smap/transforms/stac_writer/stac_templates/history/README.md"
version: "v11.2.2"
last_updated: "2025-11-29"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · STAC Review Board · FAIR+CARE Council"
status: "Active / Enforced"

classification: "Public STAC Template History"
license: "MIT"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
provenance_profile: "KFM-PROV-O v11.2"

commit_sha: "<latest-commit>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
jsonld_profile: "KFM-JSONLD v11"

sbom_ref: "../../../../../../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../../../../../../releases/v11.2.2/data-telemetry.json"
telemetry_schema: "../../../../../../../../../../schemas/telemetry/sat-smap-transforms-v11.json"

governance_ref: "../../../../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

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
  prov_o: "prov:Entity"
  owl_time: "TemporalEntity"
  geosparql: "geo:Feature"

json_schema_ref: "../../../../../../../../../../schemas/json/stac-templates-history-v11.json"
shape_schema_ref: "../../../../../../../../../../schemas/shacl/stac-templates-history-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:smap:stac-templates-history-readme:v11.2.2"
semantic_document_id: "kfm-doc-data-smap-stac-templates-history"
event_source_id: "ledger:docs/data/satellites/smap/transforms/stac_writer/stac_templates/history/README.md"
immutability_status: "version-pinned"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
ttl_policy: "48 months"
sunset_policy: "Superseded with next STAC template revision"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 🕰️ **NASA SMAP — STAC Template History**  
`docs/data/satellites/smap/transforms/stac_writer/stac_templates/history/README.md`

**Purpose**  
Record the **evolution** of the SMAP STAC Templates (Collections, Items, Assets,  
Provenance templates) used by the STAC Writer Finalization Layer.  
Ensures **reproducibility, schema stability, sovereignty compliance, and  
FAIR+CARE oversight** across KFM releases.

</div>

---

## 📘 1. Overview

This directory stores the **versioned STAC template snapshots** used to generate:

- STAC v1.0 Collections  
- STAC v1.0 Items  
- Asset templates (COGs, masks, uncertainty, QA)  
- Governance extension blocks  
- PROV-O lineage templates  

These templates are **critical** to:

- downstream publishing safety  
- STAC/DCAT interoperability  
- sovereignty-compliant spatial & uncertainty metadata  
- Focus Mode v3 lineage parsing  
- Story Node v3 environmental linking  
- KFM-wide reproducibility

Any change to these templates must be:

- assessed by the STAC Review Board  
- approved by the FAIR+CARE Council  
- validated via CI (STAC+JSON-LD+PROV+governance)  
- logged in this history directory  

---

## 🗂️ 2. Directory Layout (Emoji-Rich · Option A)

~~~text
docs/data/satellites/smap/transforms/stac_writer/stac_templates/history/
├── 📄 README.md                             # This file
│
├── 📚 stac_templates_v001.json              # Initial template set
├── 📚 stac_templates_v002.json              # Updated template set (e.g., governance fields added)
│
└── 📊 diffs/                                 # Machine-readable diffs between template versions
    ├── diff_v001_v002.json
    ├── diff_v002_v003.json
    └── diff_v003_v004.json                  # Reserved for future updates
~~~

---

## 🧩 3. Required Contents of Template Snapshots

Each `stac_templates_vXXX.json` MUST contain:

### ✔ Collection Template State  
- `stac_version`, `type`, `id`, `description`  
- `extent.spatial`, `extent.temporal`  
- required STAC extensions  
- governance extension metadata  
- uncertainty + QA summaries  

### ✔ Item Template State  
- geometry & bbox  
- temporal fields (`datetime`, `start_datetime`, `end_datetime`)  
- asset definitions  
- projection/raster extension blocks  
- governance metadata (`kfm:*`)  
- PROV-O lineage scaffolding  

### ✔ Asset Template State  
- COG definitions  
- QA masks  
- uncertainty grids  
- governance masks  
- media types, roles, bands, nodata values  

### ✔ Provenance Template State  
- `prov:wasGeneratedBy`  
- `prov:used`  
- `prov:wasDerivedFrom`  
- `prov:atLocation`  

### ✔ Metadata for Governance  
- CARE/H3 flags  
- `"kfm:mask_required"`  
- `"kfm:sovereignty_uncertainty_floor"`  
- `"kfm:h3_sensitive"`  

---

## 📊 4. Template Diff Logs (Evolution Tracking)

Each diff file MUST describe:

- STAC structural changes  
- new/removed template keys  
- governance extension updates  
- uncertainty-metadata changes  
- QA metadata adjustments  
- provenance field changes  
- backward-compatibility notes  
- FAIR+CARE impact analysis  
- sovereignty-floor policy implications  
- validation test expectations  

Diff logs are **machine-readable** and validated via JSON Schema & SHACL.

---

## 🔐 5. Governance & FAIR+CARE Requirements

Because template changes impact **every final dataset**, all changes must ensure:

- no degradation in governance metadata  
- no removal of sovereignty fields  
- no false precision introduced  
- uncertainty metadata preserved  
- CARE labels consistently applied  
- DCAT + JSON-LD safety maintained  
- STAC Items always mask sensitive geographies  

Approved via:

- FAIR+CARE Council  
- Sovereignty Working Group  
- STAC Review Board  

---

## 🧪 6. QA & Validation

Template history undergoes CI validation:

- JSON Schema  
- SHACL constraints  
- STAC Schema  
- Governance metadata integrity  
- PROV-O lineage correctness  
- Backwards-compatibility checks  

---

## 🔁 7. Template Role in Full SMAP ETL Pipeline

~~~text
decode
 → reprojection
 → calibration
 → QA/RFI integration
 → uncertainty propagation
 → governance masking
 → STAC Writer (uses template set)
    → Collection/Item/Asset creation
    → DCAT metadata
    → PROV-O lineage
~~~

These templates define the **final public representation** of all SMAP datasets.

---

## 🔮 8. Applications Inside KFM

### Hydrology  
Consistent STAC schema for wetness/floodplain layers.

### Climate  
Stable FT/VWC anomaly STAC surfaces.

### Archaeology  
Governance-aligned environmental layers for Story Nodes.

### Story Node v3  
Template-driven consistent STAC entities for narrative contexts.

### Focus Mode v3  
Template-based lineage and governance-driven context retrieval.

---

## 🧭 9. Version History

| Version | Date       | Summary                                                                                                   |
|--------:|------------|-----------------------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-29 | Complete STAC Template History README; emoji layout; governance/H3 aligned; STAC/DCAT/PROV compliant.     |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅️ Back](../README.md) · [📐 Template Diffs](./diffs/README.md) · [🛡 Governance](../../../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

