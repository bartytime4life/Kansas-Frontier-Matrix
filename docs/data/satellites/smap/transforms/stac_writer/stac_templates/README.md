---
title: "📐 NASA SMAP — STAC Template Library (Collections · Items · Assets · Provenance) · ETL Finalization"
path: "docs/data/satellites/smap/transforms/stac_writer/stac_templates/README.md"
version: "v11.2.2"
last_updated: "2025-11-29"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · STAC Review Board · FAIR+CARE Council"
status: "Active / Enforced"

classification: "Public STAC Template Documentation"
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

sbom_ref: "../../../../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../../../../releases/v11.2.2/data-telemetry.json"
telemetry_schema: "../../../../../../../../schemas/telemetry/sat-smap-transforms-v11.json"

governance_ref: "../../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

fair_category: "F1-A1-I2-R5"
care_label: "CARE-A / CARE-B"
indigenous_rights_flag: true
sensitivity_level: "Medium"
public_exposure_risk: "Low–Medium"
risk_category: "Medium"
redaction_required: true

data_steward: "STAC/DCAT Review Board · FAIR+CARE Council · Earth Systems Working Group"

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "Dataset"
  prov_o: "prov:Plan"
  owl_time: "TemporalEntity"
  geosparql: "geo:FeatureCollection"

json_schema_ref: "../../../../../../../../schemas/json/stac-templates-v11.json"
shape_schema_ref: "../../../../../../../../schemas/shacl/stac-templates-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:smap:stac-templates-readme:v11.2.2"
semantic_document_id: "kfm-doc-data-smap-stac-templates"
event_source_id: "ledger:docs/data/satellites/smap/transforms/stac_writer/stac_templates/README.md"
immutability_status: "version-pinned"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
ttl_policy: "48 months"
sunset_policy: "Superseded upon next STAC schema evolution"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 📐 **NASA SMAP — STAC Template Library (Collections, Items, Assets, Provenance)**  
`docs/data/satellites/smap/transforms/stac_writer/stac_templates/README.md`

**Purpose**  
Document the **canonical JSON templates** used by the SMAP STAC Writer to generate:  
✔ STAC v1.0 Collections  
✔ STAC v1.0 Items  
✔ STAC Assets (COGs, masks, uncertainty, QA)  
✔ Governance extension metadata  
✔ PROV-O lineage entries  
✔ DCAT alignment pre-structures  

These templates enforce **consistency, governance safety, and schema validity**  
across all SMAP-derived products in KFM.

</div>

---

## 📘 1. Overview

The STAC Writer uses these templates to:

- Build reproducible STAC Collections and Items  
- Ensure all STAC output follows KFM-STAC v11 rules  
- Enforce governance, H3 masking, and CARE labels  
- Maintain uncertainty metadata compatibility  
- Guarantee all Items include correct projections, raster metadata, and provenance  
- Stabilize STAC structure across ETL runs  
- Prevent schema drift  
- Power Focus Mode v3 environmental lineage views  

Templates are **JSON Schema–validated**, **SHACL-constrained**, and governable by the FAIR+CARE Council.

---

## 🗂️ 2. Directory Layout (Emoji-Rich · Option A)

~~~text
docs/data/satellites/smap/transforms/stac_writer/stac_templates/
├── 📄 README.md                      # This file
│
├── 📚 collection_template.json       # Template for STAC Collections
├── 📚 item_template.json             # Template for STAC Items
├── 📚 asset_template.json            # COG + mask + uncertainty asset template
├── 📚 provenance_template.json       # PROV-O lineage template for STAC Items
│
└── 🗂️ history/                       # Template evolution + diffs
    ├── stac_templates_v001.json
    ├── stac_templates_v002.json
    └── diff_v001_v002.json
~~~

---

## 🧩 3. Template Responsibilities

### 📚 **collection_template.json**
Defines:

- STAC Collection root metadata  
- `extent.spatial` + `extent.temporal`  
- `summaries` for soil moisture, FT, VWC, QA, uncertainty  
- Required STAC extensions  
- CARE/H3 governance metadata  
- PROV-O dataset-level lineage fields  

### 📚 **item_template.json**
Defines:

- geospatial footprint  
- bounding box  
- timestamp fields (`datetime`, `start_datetime`, `end_datetime`)  
- complete asset dictionary  
- governance + uncertainty fields  
- QA metadata  
- tile ID, version info  
- links to parent Collection  

### 📚 **asset_template.json**
Defines per-asset structure:

- COGs  
- uncertainty surfaces  
- QA masks  
- governance masks  
- raster metadata  
- roles, media types, band info  
- CARE/H3 metadata propagation  

### 📚 **provenance_template.json**
Defines PROV-O lineage:

- `prov:wasGeneratedBy`  
- `prov:used` (decode→reprojection→calibration→QA→uncertainty→governance)  
- `prov:wasDerivedFrom`  
- `prov:atLocation`  

Used for:

- Focus Mode v3  
- Story Node v3 environmental linking  
- Governance violation audits  

---

## 🔐 4. Governance & FAIR+CARE Integration

Templates ensure:

- no STAC Item misses required governance fields  
- CARE labels propagate to all assets  
- `"kfm:mask_required"` is included when needed  
- sovereignty/H3 sensitivity explicitly represented  
- uncertainty floors captured in STAC metadata  
- lineage is fully represented with PROV-O  
- Indigenous sovereignty rules cannot be bypassed  

CI checks:

- `faircare_validate.yml`  
- `jsonld_validate.yml`  
- `stac_validate.yml`  
- `data_pipeline.yml`  

---

## 🧪 5. QA & Validation

Templates undergo:

- JSON Schema validation  
- SHACL shape validation  
- STAC 1.0 compliance checks  
- Governance metadata conformance  
- Cross-template consistency tests  
- Provenance mapping tests  

All STAC generation depends on these templates; failure would halt ETL.

---

## 🔁 6. Role in Full SMAP ETL Pipeline

~~~text
decode
 → reprojection
 → calibration
 → QA/RFI integration
 → uncertainty propagation
 → governance masking
 → STAC Writer (uses these templates)
 → STAC/DCAT publication
 → PROV-O lineage archival
~~~

---

## 🔮 7. Applications Inside KFM

### Hydrology  
STAC-compliant soil moisture tiles with QA, masks, uncertainty, lineage.

### Climate  
Freeze–Thaw / VWC anomaly collections with governance safety.

### Archaeology  
Sensitive-environment-aware STAC layers for Story Node v3.

### Story Node v3  
Direct STAC-linked environmental evidentiary chains.

### Focus Mode v3  
Immediate STAC-backed context, uncertainty, governance, lineage.

---

## 🧭 8. Version History

| Version | Date       | Summary                                                                                              |
|--------:|------------|------------------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-29 | Full STAC Template Library README; emoji-rich; governance/H3 aligned; STAC/DCAT/PROV compliant; CI-safe. |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅️ Back](../README.md) · [📦 STAC Writer](../README.md) · [🛡 Governance Standards](../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

