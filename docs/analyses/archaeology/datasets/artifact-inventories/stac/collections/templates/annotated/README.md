---
title: "📁📝 Kansas Frontier Matrix — Annotated STAC Collection Templates for Artifact Inventories (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/datasets/artifact-inventories/stac/collections/templates/annotated/README.md"
description: "Annotated STAC 1.0 Collection templates for KFM v11 artifact inventories, explaining every required field, extension, and CARE constraint."
version: "v11.2.3"
last_updated: "2025-12-02"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Biannual · Archaeology Working Group · FAIR+CARE Council · Metadata Standards Subcommittee"
content_stability: "stable"
status: "Active / Enforced"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-version-hash>"
doc_uuid: "urn:kfm:doc:archaeology-artifact-stac-collection-templates-annotated-v11.2.3"
doc_kind: "Annotated Templates"
intent: "artifact-inventory-stac-collection-templates-annotated"
semantic_document_id: "kfm-doc-archaeology-artifact-stac-collection-templates-annotated-v11.2.3"
category: "Analyses · Archaeology · STAC Collections · Templates"

sbom_ref: "../../../../../../../../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../../../../../../../../releases/v11.2.3/manifest.zip"
telemetry_ref: "../../../../../../../../../releases/v11.2.3/focus-telemetry.json"
telemetry_schema: "../../../../../../../../../schemas/telemetry/archaeology-artifact-stac-collection-templates-annotated-v1.json"
energy_schema: "../../../../../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../../../../../schemas/telemetry/carbon-gco2e-v1.json"

governance_ref: "../../../../../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

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
  - "docs/analyses/archaeology/datasets/artifact-inventories/stac/collections/templates/annotated/README.md@v10.4.0"
provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: true
---

# 📁📝 Kansas Frontier Matrix — Annotated Artifact STAC Collection Templates (v11)

`docs/analyses/archaeology/datasets/artifact-inventories/stac/collections/templates/annotated/README.md`

**Purpose**  
Provide **line-by-line annotated STAC Collection templates** for artifact inventory categories in the Kansas Frontier Matrix (KFM).  
These annotated templates explain every field, requirement, controlled vocabulary, and CARE constraint needed to build compliant, culturally safe STAC Collections.

Intended users include:

- Metadata engineers  
- Archaeologists  
- FAIR+CARE and sovereignty reviewers  
- STAC contributors  
- Knowledge-graph modelers  
- AI and ETL specialists  

Templates align with:

- STAC 1.0  
- DCAT 3.0  
- PROV-O  
- CIDOC-CRM  
- GeoSPARQL  
- CARE and sovereignty policies  
- MCP-DL v6.3  
- KFM-MDP v11.2.2 and KFM-OP v11  

All examples are **synthetic, generalized, and culturally safe**.

---

## 📘 Overview

Annotated templates in this directory describe:

- Root artifact collection  
- Lithics collection  
- Ceramics collection  
- Metals / protohistoric collection  
- Faunal (public-domain) collection  

Each annotated template includes:

- STAC field explanations  
- Extension usage notes (`kfm:*`, `care:*`)  
- CARE sensitivity justification and sovereignty notes  
- Guidance on what **belongs** and what **must not** be included  
- Spatial, temporal, and provenance metadata requirements  
- Validation cues for CI (for example: `artifact-stac-validate.yml`)  

These annotated files are **documentation and teaching artifacts**; production Collections must be derived from the non-annotated templates one directory up.

---

## 🗂️ Directory Layout

~~~text
docs/analyses/archaeology/datasets/artifact-inventories/stac/collections/templates/annotated/
├── 📄 README.md                          # This file
├── 📄 collection_root_annotated.json     # Annotated root artifact collection
├── 📄 collection_lithics_annotated.json  # Annotated lithics collection
├── 📄 collection_ceramics_annotated.json # Annotated ceramics collection
├── 📄 collection_metals_annotated.json   # Annotated metals collection
├── 📄 collection_faunal_annotated.json   # Annotated faunal collection
└── 📄 field_guide.md                     # Field-level explanations (STAC / KFM / CARE)
~~~

This layout is **normative** for annotated artifact STAC Collection templates.

---

## 🧱 Annotated Template — Root Artifact Collection

~~~json
{
  "stac_version": "1.0.0",
  "_comment_stac_version": "Must always be 1.0.0 for STAC Collections in KFM.",

  "type": "Collection",
  "_comment_type": "Collections group multiple STAC Items and/or sub-Collections.",

  "id": "artifact-inventories",
  "_comment_id": "Top-level grouping for all artifact inventory datasets; controlled ID.",

  "description": "Root collection for all artifact inventory datasets in the Kansas Frontier Matrix.",
  "_comment_description": "Human-readable summary used by STAC browsers and KFM metadata UI.",

  "license": "CC-BY-4.0",
  "_comment_license": "KFM public artifact datasets must use open licenses such as CC-BY.",

  "extent": {
    "spatial": { "bbox": [[-102.1, 37.0, -94.6, 40.1]] },
    "_comment_spatial": "Generalized bounding box for Kansas; never site-precise coordinates.",

    "temporal": { "interval": [["1000-01-01T00:00:00Z", "2025-01-01T00:00:00Z"]] },
    "_comment_temporal": "Earliest and latest representative dates across all artifact inventories."
  },

  "links": [],
  "_comment_links": "Can remain empty for file-only catalogs; required when exposed via STAC API.",

  "kfm:material_class": "all",
  "_comment_material_class": "Indicates this root Collection groups all artifact material classes.",

  "kfm:domain": "archaeology-artifact-inventories",
  "_comment_kfm_domain": "KFM domain identifier used by ETL, Focus Mode, and graph mappers.",

  "kfm:review_cycle": "Biannual",
  "_comment_review_cycle": "Governance review cadence tracked by FAIR+CARE tooling.",

  "care:sensitivity": "general",
  "_comment_care_sensitivity": "Root-level sensitivity; child Collections and Items may be more restrictive.",

  "care:review": "faircare",
  "_comment_care_review": "Indicates the body responsible for cultural safety review.",

  "care:notes": "All artifact datasets within this collection must be spatially generalized (H3) and culturally reviewed.",
  "_comment_care_notes": "Describes high-level CARE and sovereignty constraints applied to this grouping."
}
~~~

---

## 🧱 Annotated Template — Lithics Collection

~~~json
{
  "stac_version": "1.0.0",
  "_comment_stac": "STAC version; fixed at 1.0.0 for KFM v11.",

  "type": "Collection",
  "_comment_type": "Collection groups lithic artifact inventory Items.",

  "id": "lithics",
  "_comment_id": "Controlled ID; must match child Item link targets and catalog references.",

  "description": "Public-governed lithic artifact inventories from the Kansas region, generalized via H3.",
  "_comment_description": "Scope and purpose of the lithics Collection.",

  "license": "CC-BY-4.0",
  "_comment_license": "License must be compatible with all child Items.",

  "extent": {
    "spatial": { "bbox": [[-102.1, 37.0, -94.6, 40.1]] },
    "_comment_extent_spatial": "Envelope of all lithic inventories, generalized to region scale.",

    "temporal": { "interval": [["1200-01-01T00:00:00Z", "1500-01-01T00:00:00Z"]] },
    "_comment_extent_temporal": "Combined cultural-phase time span for lithic datasets."
  },

  "links": [],
  "_comment_links": "Populate with links to Items and parent/root Collections when integrating into a larger catalog.",

  "kfm:material_class": "lithic",
  "_comment_material_class": "Controlled vocabulary defining material class for this Collection.",

  "kfm:domain": "archaeology-artifact-inventories",
  "_comment_domain": "Stable domain string for cross-system joins.",

  "kfm:review_cycle": "Biannual",
  "_comment_review_cycle": "Used by governance tooling to schedule re-validation.",

  "care:sensitivity": "general",
  "_comment_care_sensitivity": "Lithic inventories generally low sensitivity; still must be generalized.",

  "care:review": "faircare",
  "_comment_care_review": "Indicates FAIR+CARE governance review path.",

  "care:notes": "Lithic datasets must exclude any sacred lithic materials or restricted quarry locations.",
  "_comment_care_notes": "Summarizes key cultural and sovereignty constraints for this grouping."
}
~~~

---

## 🧱 Annotated Template — Ceramics Collection

~~~json
{
  "stac_version": "1.0.0",
  "_comment_stac": "STAC version header required for all KFM STAC documents.",

  "type": "Collection",
  "_comment_type": "Groups ceramic artifact inventory Items.",

  "id": "ceramics",
  "_comment_id": "Collection ID; referenced by catalog and graph systems.",

  "description": "Ceramic artifact inventories with motif categories generalized for cultural safety.",
  "_comment_description": "Indicates that motif-level details are generalized to protect cultural knowledge.",

  "license": "CC-BY-4.0",
  "_comment_license": "Must be consistent with child Items and source datasets.",

  "extent": {
    "spatial": { "bbox": [[-101.9, 37.0, -94.9, 40.0]] },
    "_comment_spatial": "Generalized spatial footprint for all ceramic inventories.",

    "temporal": { "interval": [["1000-01-01T00:00:00Z", "1800-01-01T00:00:00Z"]] },
    "_comment_temporal": "Time span for ceramic phases included in this Collection."
  },

  "links": [],
  "_comment_links": "Populate with links to ceramic Items and root artifact Collection where needed.",

  "kfm:material_class": "ceramic",
  "_comment_material_class": "Controlled value identifying this as a ceramics grouping.",

  "kfm:domain": "archaeology-artifact-inventories",
  "_comment_domain": "Stable domain for ETL and query routing.",

  "kfm:review_cycle": "Biannual",
  "_comment_review_cycle": "Used for regular CARE and sovereignty re-review scheduling.",

  "care:sensitivity": "generalized",
  "_comment_sensitivity": "Motif and design data can be sensitive; only generalized patterns are allowed.",

  "care:review": "faircare",
  "_comment_review": "Indicates review by a FAIR+CARE-aligned body.",

  "care:notes": "Motif categories are generalized and exclude culturally restricted symbolism unless explicitly approved.",
  "_comment_notes": "Documents CARE transformations applied to ceramic datasets."
}
~~~

---

## 🧱 Annotated Template — Metals Collection

~~~json
{
  "stac_version": "1.0.0",
  "_comment_stac": "Always 1.0.0 for KFM STAC documents.",

  "type": "Collection",
  "_comment_type": "Metals and protohistoric trade-material inventories.",

  "id": "metals",
  "_comment_id": "Identifier used by catalog browser and graph builders.",

  "description": "Protohistoric and historic metal artifacts and trade items, generalized and sovereignty-reviewed.",
  "_comment_description": "Highlights protohistoric focus and sovereignty review requirements.",

  "license": "CC-BY-4.0",
  "_comment_license": "License must be compatible with source datasets and reuse patterns.",

  "extent": {
    "spatial": { "bbox": [[-102.1, 37.0, -94.6, 40.1]] },
    "_comment_spatial": "Generalized bounding box for all metals/protohistoric inventories.",

    "temporal": { "interval": [["1500-01-01T00:00:00Z", "1900-01-01T00:00:00Z"]] },
    "_comment_temporal": "Common interval for contact and historic-era metal artifacts."
  },

  "links": [],
  "_comment_links": "Populate with links to metal Items and root Collection in production.",

  "kfm:material_class": "metal",
  "_comment_material_class": "Marks this Collection as metal/protohistoric-focused.",

  "kfm:domain": "archaeology-artifact-inventories",
  "_comment_domain": "Domain string reused across artifact components.",

  "kfm:review_cycle": "Biannual",
  "_comment_review_cycle": "Ensures repeating sovereignty review of contact-era material.",

  "care:sensitivity": "generalized",
  "_comment_sensitivity": "Spatial and contextual details must be generalized due to contact-era sensitivities.",

  "care:review": "tribal",
  "_comment_review": "Indicates that metals are reviewed through tribal/sovereignty governance processes.",

  "care:notes": "Contact-era and trade metal items must be reviewed for cultural implications before inclusion.",
  "_comment_notes": "Summarizes contact-era cultural review expectations."
}
~~~

---

## 🧱 Annotated Template — Faunal Collection

~~~json
{
  "stac_version": "1.0.0",
  "_comment_stac": "STAC version header.",

  "type": "Collection",
  "_comment_type": "Groups faunal inventories related to archaeological analyses.",

  "id": "faunal",
  "_comment_id": "Faunal Collection identifier.",

  "description": "Public-domain faunal datasets suitable for archaeological correlation and environmental reconstruction.",
  "_comment_description": "Clarifies that only PD-suitable faunal inventories are included.",

  "license": "CC-BY-4.0",
  "_comment_license": "Open license to support reuse under KFM governance.",

  "extent": {
    "spatial": { "bbox": [[-102.1, 37.0, -94.6, 40.1]] },
    "_comment_spatial": "Generalized spatial extent covering the relevant faunal observation area.",

    "temporal": { "interval": [["0001-01-01T00:00:00Z", "2025-01-01T00:00:00Z"]] },
    "_comment_temporal": "Broad interval covering Pleistocene, Holocene, and historic faunal data."
  },

  "links": [],
  "_comment_links": "Link to faunal Items and root artifact Collection where appropriate.",

  "kfm:material_class": "faunal",
  "_comment_material_class": "Identifies the Collection as faunal-focused.",

  "kfm:domain": "archaeology-artifact-inventories",
  "_comment_domain": "Same domain identifier used throughout artifact inventories.",

  "kfm:review_cycle": "Biannual",
  "_comment_review_cycle": "Ensures recurring review of species lists and contextual use.",

  "care:sensitivity": "general",
  "_comment_sensitivity": "Faunal data is usually low sensitivity but still requires sacred-species filtering.",

  "care:review": "faircare",
  "_comment_review": "Cultural safety review path.",

  "care:notes": "Faunal datasets must exclude sacred species and contexts tied to restricted sites.",
  "_comment_notes": "Documents cultural and sovereignty constraints for faunal inventories."
}
~~~

---

## 📚 Field Guide (`field_guide.md`)

The field guide in this directory should provide:

- Definitions for STAC core fields used across Collections  
- Requirements for `kfm:*` archaeology extension fields  
- CARE and sovereignty field descriptions (`care:*`)  
- Controlled vocabularies:
  - `kfm:material_class`  
  - domain identifiers  
  - review_cycle terms  
- Spatial and temporal generalization rules (H3 levels, OWL-Time intervals)  
- Crosswalk notes between:
  - STAC  
  - DCAT  
  - PROV-O  
  - KFM knowledge graph schema  

---

## 🧪 Validation Workflow for Contributors

When using these annotated templates to build real Collections:

1. Choose the appropriate annotated template and review comments.  
2. Use the non-annotated template from `../` as the actual starting JSON.  
3. Fill in fields according to the guidance here and in `field_guide.md`.  
4. Validate against schemas used in KFM:
   - STAC Collection core schema  
   - KFM archaeology extension schema  
   - CARE/sensitivity extension schema  
   - Any DCAT or governance crosswalk schemas used by the catalog.  
5. Confirm:
   - Spatial metadata is generalized (no site-precise geometry).  
   - Temporal ranges align with the cultural/analytical scope.  
   - Licenses and rights holders are correct and open-licensed.  
   - CARE and sovereignty settings match governance decisions.  
6. Ensure `links` are wired to:
   - Child Items in `../items/`  
   - Root artifact Collection (where applicable)  
   - Governance and documentation targets if required.  
7. Run the STAC validation workflow (for example: `.github/workflows/artifact-stac-validate.yml`) before opening a PR.

---

## 🕰 Version History

| Version   | Date       | Summary                                                                                             |
|-----------|------------|-----------------------------------------------------------------------------------------------------|
| v11.2.3   | 2025-12-02 | Aligned with KFM-MDP v11.2.2; added energy/carbon schemas; clarified CARE/sovereignty notes and validation workflow. |
| v10.4.0   | 2025-11-17 | Created annotated artifact STAC Collection templates with CARE and KFM extension commentary.        |
| v10.0.0   | 2025-11-10 | Initial placeholder annotation directory.                                                           |

---

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
FAIR+CARE Certified · Sovereignty-Governed  
KFM-MDP v11.2.2 · MCP-DL v6.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[⬅ Back to Collection Templates](../README.md)