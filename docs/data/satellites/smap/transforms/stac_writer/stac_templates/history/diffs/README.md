---
title: "📊 NASA SMAP — STAC Template Diff Logs (Collection · Item · Asset · Provenance Changes)"
path: "docs/data/satellites/smap/transforms/stac_writer/stac_templates/history/diffs/README.md"
version: "v11.2.2"
last_updated: "2025-11-29"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · STAC Review Board · FAIR+CARE Council"
status: "Active / Enforced"

classification: "Public STAC Template Evolution Logs"
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
  cidoc: "E31 Document"
  schema_org: "Dataset"
  prov_o: "prov:Entity"
  owl_time: "TemporalEntity"
  geosparql: "geo:Feature"

json_schema_ref: "../../../../../../../../../../../schemas/json/stac-templates-diffs-v11.json"
shape_schema_ref: "../../../../../../../../../../../schemas/shacl/stac-templates-diffs-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:smap:stac-templates-diffs-readme:v11.2.2"
semantic_document_id: "kfm-doc-data-smap-stac-templates-diffs"
event_source_id: "ledger:docs/data/satellites/smap/transforms/stac_writer/stac_templates/history/diffs/README.md"
immutability_status: "version-pinned"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
ttl_policy: "48 months"
sunset_policy: "Superseded when template evolution changes"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 📊 **NASA SMAP — STAC Template Diff Logs**  
`docs/data/satellites/smap/transforms/stac_writer/stac_templates/history/diffs/README.md`

**Purpose**  
Document **schema-level**, **metadata-level**, **governance-level**, and **provenance-level**  
changes between STAC template versions (`stac_templates_vXXX.json`).  
These diff logs maintain **traceability**, **governance transparency**, and  
**reproducibility** across SMAP → KFM STAC transformations.

</div>

---

## 📘 1. Overview

These diff logs capture the evolution of:

- STAC Collection templates  
- STAC Item templates  
- STAC Asset templates  
- Governance extension structures (`kfm:*`)  
- Uncertainty + QA metadata fields  
- Provenance metadata templates  
- DCAT + JSON-LD alignment schemas  

Each diff file provides a **machine-readable description** of all changes and  
their governance impacts.

---

## 🗂️ 2. Directory Layout (Emoji-Rich · Option A)

~~~text
docs/data/satellites/smap/transforms/stac_writer/stac_templates/history/diffs/
├── 📄 README.md                        # This file
│
├── 📊 diff_v001_v002.json              # Template evolution: v001 → v002
├── 📊 diff_v002_v003.json              # Template evolution: v002 → v003
├── 📊 diff_v003_v004.json              # Reserved for future updates
│
└── 🧩 templates/                       # Authoritative diff-template schema
    └── diff_template.json
~~~

All diff files MUST be derived from the template.

---

## 🧩 3. Required Diff Structure (KFM-STAC-Diff v11)

Each diff file MUST contain:

### ✔ 1. Version Metadata  
- `"template_version_old"`  
- `"template_version_new"`  
- `"valid_from"` / `"valid_to"`  
- `"stac_schema_version"`  
- `"governance_schema_version"`  

### ✔ 2. Collection Template Changes  
- additions/removals of fields  
- updates to `extent`, `summaries`, `stac_extensions`  
- changes in governance metadata  
- updates to uncertainty/QA summaries  

### ✔ 3. Item Template Changes  
- geometry or bbox changes  
- new/removed Item-level metadata fields  
- projection/raster extension schema changes  
- governance extension (`kfm:*`) diffs  
- PROV-O lineage mapping changes  

### ✔ 4. Asset Template Changes  
- changes to asset roles, media_types, band definitions  
- uncertainty asset adjustments  
- QA mask / governance mask asset changes  
- new fields for sovereignty floors  

### ✔ 5. Provenance Template Changes  
- changes in PROV-O blocks  
- additions/deprecations of lineage relations  
- updates to `prov:used` lists  
- timestamp-policy changes  

### ✔ 6. Governance & Sovereignty Impact Notes  
Diffs MUST annotate:

- `"care_label_change"`  
- `"h3_sensitivity_change"`  
- `"masking_implication"` (true/false)  
- `"sovereignty_uncertainty_floor_change"`  
- `"requires_governance_review"` (true/false)  

### ✔ 7. FAIR+CARE, STAC, DCAT, JSON-LD Conformance  
All template evolutions must:

- retain STAC v1.0 compliance  
- maintain CARE/H3 metadata  
- preserve uncertainty metadata  
- maintain DCAT interoperability  

### ✔ 8. Provenance (PROV-O) Block  
Example:

```json
"provenance": {
  "prov:wasDerivedFrom": "stac_templates_v001.json",
  "prov:used": ["collection_template.json", "item_template.json"],
  "prov:wasGeneratedBy": "kfm-stac-template-diff-process-v11",
  "prov:generatedAtTime": "2025-11-29T00:00:00Z"
}
```

---

## 🔐 4. Governance, FAIR+CARE, & Sovereignty Requirements

Changes to STAC templates may:

- reveal or hide environmental detail  
- alter uncertainty representation  
- modify governance fields  
- affect Indigenous land protections  
- impact public-safety or ethics constraints  

Therefore diff logs MUST ensure:

- all sovereignty constraints preserved  
- no false precision introduced  
- no governance metadata lost  
- CARE labels remain fully accurate  
- uncertainty floors honored  
- explainability preserved for Story Node v3 and Focus Mode v3  

Validated via:

- `faircare_validate.yml`  
- `jsonld_validate.yml`  
- `stac_validate.yml`  

---

## 🧪 5. QA & Validation Requirements

Each diff file MUST:

- pass JSON Schema validation  
- pass SHACL shape validation  
- be fully machine-extractable  
- contain no speculative or inferred metadata  
- conform to KFM-STAC v11 rules  
- explicitly describe user-facing metadata impact  

All diffs are validated in CI alongside STAC Writer tests.

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
    → uses template history + diffs
 → STAC/DCAT publishing
 → PROV-O + OpenLineage archival
~~~

---

## 🔮 7. Applications Inside KFM

### Hydrology  
Ensures stable STAC evolution for soil moisture, wetlands, floodplain layers.

### Climate  
Stable FT/VWC anomaly STAC schema.

### Archaeology  
Governance-safe environmental STAC layers.

### Story Node v3  
Stable metadata → explainable narrative environment linking.

### Focus Mode v3  
Lineage-aware environmental context via stable template history.

---

## 🧭 8. Version History

| Version | Date       | Summary                                                                                                   |
|--------:|------------|-----------------------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-29 | Complete STAC template-diff README; emoji-rich; governance-aware; FAIR+CARE aligned; CI-safe.             |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅️ Back](../README.md) · [📐 Template Diffs](../README.md) · [🛡 Governance](../../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

