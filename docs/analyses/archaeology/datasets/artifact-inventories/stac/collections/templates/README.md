---
title: "📁 Kansas Frontier Matrix — Artifact STAC Collection Templates (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/datasets/artifact-inventories/stac/collections/templates/README.md"
description: "Template library for KFM v11 artifact inventory STAC Collections, enforcing consistent, FAIR+CARE-aligned, sovereignty-governed metadata structures."
version: "v11.2.3"
last_updated: "2025-12-02"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Biannual · Archaeology Working Group · FAIR+CARE Council · Metadata Standards Subcommittee"
content_stability: "stable"
status: "Active / Enforced"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-version-hash>"
doc_uuid: "urn:kfm:doc:archaeology-artifact-stac-collection-templates-v11.2.3"
doc_kind: "Template Library"
intent: "artifact-inventory-stac-collection-templates"
semantic_document_id: "kfm-doc-archaeology-artifact-stac-collection-templates-v11.2.3"
category: "Analyses · Archaeology · STAC Collections · Templates"

sbom_ref: "../../../../../../../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../../../../../../../releases/v11.2.3/manifest.zip"
telemetry_ref: "../../../../../../../../releases/v11.2.3/focus-telemetry.json"
telemetry_schema: "../../../../../../../../schemas/telemetry/archaeology-artifact-stac-collection-templates-v1.json"
energy_schema: "../../../../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../../../../schemas/telemetry/carbon-gco2e-v1.json"

governance_ref: "../../../../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"

fair_category: "F1-A1-I1-R1"
care_label: "High-Sensitivity · Sovereignty-Governed"
sensitivity: "Cultural / Archaeological / Heritage"
sensitivity_level: "High"
indigenous_rights_flag: true
risk_category: "Moderate"
public_exposure_risk: "Governed"
redaction_required: true

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
classification: "Public (Governed)"
jurisdiction: "Kansas / United States"
immutability_status: "mutable-plan"

header_profile: "standard"
footer_profile: "standard"

data_steward: "Archaeology & Heritage WG · Metadata Standards Subcommittee"
provenance_chain:
  - "docs/analyses/archaeology/datasets/artifact-inventories/stac/collections/templates/README.md@v10.4.0"
provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: true
---

# 📁 Kansas Frontier Matrix — Artifact STAC Collection Templates (v11)

`docs/analyses/archaeology/datasets/artifact-inventories/stac/collections/templates/README.md`

**Purpose**  
Provide a library of **validated STAC Collection templates** for artifact inventory categories in KFM v11.  
Templates ensure contributors produce:

- Metadata-complete STAC Collections  
- FAIR+CARE and sovereignty-aligned records  
- KFM-OP v11–compatible archaeology metadata  
- Structures that pass CI validation and governance checks  

These templates are the **required starting point** for any new artifact inventory STAC Collection.

---

## 📘 Overview

Artifact inventory STAC Collections must:

- Start from one of the templates in this directory  
- Preserve required STAC, KFM, and CARE fields  
- Avoid introducing schema drift across lithic, ceramic, metal, and faunal groupings  

Templates are aligned with:

- STAC 1.0 core specification  
- KFM archaeology STAC extension (`kfm:*`)  
- CARE cultural safety extension (`care:*`)  
- DCAT 3.0 crosswalk requirements  
- MCP-DL v6.3 documentation-first standards  

---

## 🗂️ Directory Layout

~~~text
docs/analyses/archaeology/datasets/artifact-inventories/stac/collections/templates/
├── 📄 README.md                                 # This file (template library index)
├── 📄 template-collection-root.json             # Root artifact-inventories collection template
├── 📄 template-collection-lithics.json          # Lithic artifact collection template
├── 📄 template-collection-ceramics.json         # Ceramic artifact collection template
├── 📄 template-collection-metals.json           # Metal / protohistoric artifact collection template
├── 📄 template-collection-faunal.json           # Faunal (public-domain) artifact collection template
└── 📂 annotated/                                # Annotated templates with inline guidance
~~~

This layout is **normative** for artifact STAC Collection templates.

---

## 🎯 Template Purpose and Usage

All artifact inventory STAC Collections in:

`docs/analyses/archaeology/datasets/artifact-inventories/stac/collections/`

must be derived from templates in this directory.

Templates enforce:

- Consistent field naming and structure  
- Use of archaeology domain vocabulary (material, phase, culture)  
- Required CARE and sovereignty metadata (`care:*`)  
- DCAT and PROV-O crosswalk compatibility  
- Compatibility with STAC crawlers and KFM discovery APIs  
- Reproducibility and auditable provenance  

**Contributor workflow**

1. Copy the appropriate `template-collection-*.json` into `../` and rename.  
2. Fill in required fields:
   - `id`, `description`, `extent.spatial`, `extent.temporal`, `keywords` (if used).  
3. Update `kfm:*` fields to match material class and domain.  
4. Set `care:sensitivity`, `care:review`, and `care:notes` based on governance decisions.  
5. Add `links` to:
   - Root collection (if not the root template).  
   - Child Items in `../items/`.  
   - Related metadata/provenance resources.  
6. Validate against schemas in `../../schemas/`.  
7. Run the STAC validation workflow (`artifact-stac-validate`) before commit.

---

## 📦 Root Artifact Collection Template (Example)

~~~json
{
  "stac_version": "1.0.0",
  "type": "Collection",
  "id": "artifact-inventories",
  "description": "Root collection for artifact inventory datasets in the Kansas Frontier Matrix.",
  "license": "CC-BY-4.0",
  "extent": {
    "spatial": {
      "bbox": [[-102.1, 37.0, -94.6, 40.1]]
    },
    "temporal": {
      "interval": [["1000-01-01T00:00:00Z", "2025-01-01T00:00:00Z"]]
    }
  },
  "links": [],
  "kfm:material_class": "all",
  "kfm:domain": "archaeology-artifact-inventories",
  "kfm:review_cycle": "Biannual",
  "care:sensitivity": "generalized",
  "care:review": "faircare",
  "care:notes": "All datasets in this collection must be spatially generalized and culturally reviewed."
}
~~~

Use `template-collection-root.json` for the actual editable template; this snippet is illustrative.

---

## 📦 Lithics Collection Template (Example)

~~~json
{
  "stac_version": "1.0.0",
  "type": "Collection",
  "id": "lithics",
  "description": "Lithic artifact inventories from public-governed archaeological datasets.",
  "license": "CC-BY-4.0",
  "extent": {
    "spatial": {
      "bbox": [[-102.0, 37.0, -94.6, 40.1]]
    },
    "temporal": {
      "interval": [["1200-01-01T00:00:00Z", "1500-01-01T00:00:00Z"]]
    }
  },
  "links": [],
  "kfm:material_class": "lithic",
  "kfm:domain": "archaeology-artifact-inventories",
  "kfm:review_cycle": "Biannual",
  "care:sensitivity": "generalized",
  "care:review": "faircare",
  "care:notes": "Lithic inventories must be generalized spatially and reviewed for cultural tone and representation."
}
~~~

---

## 📦 Ceramics Collection Template (Example)

~~~json
{
  "stac_version": "1.0.0",
  "type": "Collection",
  "id": "ceramics",
  "description": "Ceramic artifact inventories with generalized motif categories for cultural safety.",
  "license": "CC-BY-4.0",
  "extent": {
    "spatial": {
      "bbox": [[-101.9, 37.0, -94.9, 40.0]]
    },
    "temporal": {
      "interval": [["1000-01-01T00:00:00Z", "1800-01-01T00:00:00Z"]]
    }
  },
  "links": [],
  "kfm:material_class": "ceramic",
  "kfm:domain": "archaeology-artifact-inventories",
  "kfm:review_cycle": "Biannual",
  "care:sensitivity": "generalized",
  "care:review": "faircare",
  "care:notes": "Motif categories must exclude culturally restricted symbolism unless approved under sovereignty governance."
}
~~~

---

## 🧪 Validation Guidance

Before committing a new STAC Collection derived from a template:

1. Validate against STAC and extension schemas:
   - STAC Collection core schema  
   - KFM archaeology extension schema  
   - CARE sensitivity extension schema  
   - Any DCAT crosswalk or additional governance schemas used by KFM.  

2. Confirm spatial metadata:
   - BBOX reflects generalized coverage, not site-precise extents.  
   - Any internal geometry-based statistics derive from H3 or similarly generalized footprints.  

3. Confirm temporal metadata:
   - Intervals match the archaeological phases represented.  
   - There are no impossible or contradictory date ranges.  

4. Confirm licensing:
   - Only PD or open licenses (for example: CC0, CC-BY) used for public-governed datasets.  

5. Confirm CARE and sovereignty alignment:
   - `care:sensitivity`, `care:review`, and `care:notes` match governance decisions.  

6. Ensure `links` are complete:
   - Links to child Items in `../items/`.  
   - Links to root Collection (where applicable).  
   - Links to governance and documentation where required.  

7. Run the repository CI workflow (for example: `.github/workflows/artifact-stac-validate.yml`) locally when practical.

---

## 🕰 Version History

| Version   | Date       | Summary                                                                                     |
|-----------|------------|---------------------------------------------------------------------------------------------|
| v11.2.3   | 2025-12-02 | Aligned with KFM-MDP v11.2.2; added energy/carbon schemas and sovereignty references; clarified template usage and validation flow. |
| v10.4.0   | 2025-11-17 | Created STAC Collection template library; added annotated directory and validation guidance. |
| v10.0.0   | 2025-11-10 | Initial scaffold of template directory.                                                     |

---

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
FAIR+CARE Certified · Sovereignty-Governed  
KFM-MDP v11.2.2 · MCP-DL v6.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[⬅ Back to STAC Collections](../README.md)