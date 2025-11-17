---
title: "📁📝 Kansas Frontier Matrix — Annotated STAC Collection Templates for Artifact Inventories (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/datasets/artifact-inventories/stac/collections/templates/annotated/README.md"
version: "v10.4.0"
last_updated: "2025-11-17"
review_cycle: "Biannual · Archaeology Working Group · FAIR+CARE Council · Metadata Standards Subcommittee"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../../../../releases/v10.4.0/sbom.spdx.json"
manifest_ref: "../../../../../../../../../releases/v10.4.0/manifest.zip"
telemetry_ref: "../../../../../../../../../releases/v10.4.0/focus-telemetry.json"
telemetry_schema: "../../../../../../../../../schemas/telemetry/archaeology-artifact-stac-collection-templates-annotated-v1.json"
governance_ref: "../../../../../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4"
status: "Active / Enforced"
doc_kind: "Annotated Templates"
intent: "artifact-inventory-stac-collection-templates-annotated"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Compliant"
---

<div align="center">

# 📁📝 **Kansas Frontier Matrix — Annotated Artifact STAC Collection Templates**  
`docs/analyses/archaeology/datasets/artifact-inventories/stac/collections/templates/annotated/README.md`

**Purpose:**  
Provide **line-by-line annotated STAC Collection templates** for all artifact inventory categories in the Kansas Frontier Matrix (KFM).  
These annotated templates explain every field, requirement, controlled vocabulary, and CARE constraint necessary to build fully compliant, culturally safe STAC Collections.

Users of these templates include:  
Metadata engineers · Archaeologists · FAIR+CARE reviewers · STAC contributors · Graph modelers · AI/ETL specialists.

They ensure 100% compliance with:  
**STAC 1.0 · DCAT 3.0 · PROV-O · CIDOC-CRM · GeoSPARQL · CARE · MCP-DL v6.3 · KFM-MDP v10.4**

</div>

---

## 📘 Overview

Annotated templates in this directory describe:

- **Root Artifact Collection**  
- **Lithics Collection**  
- **Ceramics Collection**  
- **Metals/Protohistoric Collection**  
- **Faunal (PD-only) Collection**

Each annotated template includes:

- STAC field explanation  
- Extension usage notes  
- CARE sensitivity justification  
- What belongs and *does not* belong in each collection  
- Requirements for spatial, temporal, and provenance metadata  
- Validation cues for CI (`artifact-stac-validate.yml`)  

All examples are synthetic, generalizable, and culturally safe.

---

## 🗂️ Directory Layout

~~~text
docs/analyses/archaeology/datasets/artifact-inventories/stac/collections/templates/annotated/
├── README.md                                  # This file
├── collection_root_annotated.json             # Annotated root artifact collection
├── collection_lithics_annotated.json          # Annotated lithics collection
├── collection_ceramics_annotated.json         # Annotated ceramics collection
├── collection_metals_annotated.json           # Annotated metals collection
├── collection_faunal_annotated.json           # Annotated faunal collection
└── field_guide.md                             # Explanation of all STAC/KFM/CARE fields
~~~

---

## 🧱 Annotated Template — Root Artifact Collection

~~~json
{
  "stac_version": "1.0.0",
  "_comment_stac_version": "Must always be 1.0.0 for STAC items/collections in KFM.",

  "type": "Collection",
  "_comment_type": "Collections group multiple STAC Items.",

  "id": "artifact-inventories",
  "_comment_id": "Top-level grouping for all artifact datasets. Required naming convention.",

  "description": "Root collection for all artifact inventory datasets in the Kansas Frontier Matrix.",
  "_comment_description": "Human-readable; used for STAC browsers and KFM's metadata viewer.",

  "license": "CC-BY-4.0",
  "_comment_license": "All artifact datasets in KFM must be PD/CC-BY-only.",

  "extent": {
    "spatial": { "bbox": [[-102.1, 37.0, -94.6, 40.1]] },
    "_comment_spatial": "Generalized bounding box for Kansas; site-level precision not allowed.",

    "temporal": { "interval": [["1000-01-01T00:00:00Z", "2025-01-01T00:00:00Z"]] },
    "_comment_temporal": "Earliest and latest time period for all artifact records."
  },

  "links": [],
  "_comment_links": "Optional here; required when exposing via STAC API.",

  "kfm:material_class": "all",
  "_comment_material_class": "Indicates this collection groups all artifact datasets.",

  "kfm:domain": "archaeology:artifact-inventories",
  "_comment_kfm_domain": "KFM domain identifier for cross-tool compatibility.",

  "kfm:review_cycle": "Biannual",
  "_comment_review_cycle": "Required for MCP governance tracking.",

  "care:sensitivity": "general",
  "_comment_care_sensitivity": "Root collection sensitivity = general; specific datasets may have generalized sensitivity.",

  "care:review": "faircare",
  "_comment_care_review": "Indicates who last reviewed cultural safety of this collection.",

  "care:notes": "All artifact datasets within this collection must be generalized to H3 and culturally reviewed.",
  "_comment_care_notes": "Critical for Heritage Ethics compliance."
}
~~~

---

## 🧱 Annotated Template — Lithics Collection

~~~json
{
  "stac_version": "1.0.0",
  "_comment": "STAC version required for all datasets.",

  "type": "Collection",
  "_comment": "All groupings use type=Collection.",

  "id": "lithics",
  "_comment": "Required naming; lowercase; matches items in items/ folder.",

  "description": "Public-domain lithic artifacts from the Kansas region, generalized via H3.",
  "_comment_description": "Describes purpose and scope.",

  "license": "CC-BY-4.0",
  "_comment_license": "Must match dataset-level licensing.",

  "extent": {
    "spatial": { "bbox": [[-102.1, 37.0, -94.6, 40.1]] },
    "_comment_extent_spatial": "Combined extents of all lithic datasets.",

    "temporal": { "interval": [["1200-01-01T00:00:00Z", "1500-01-01T00:00:00Z"]] },
    "_comment_extent_temporal": "Cultural-phase time spans across lithic inventories."
  },

  "links": [],
  "_comment_links": "Not required without STAC API exposure.",

  "kfm:material_class": "lithic",
  "_comment_material_class": "Controlled vocabulary.",

  "kfm:domain": "archaeology:artifact-inventories",
  "_comment_domain": "Semantic consistency across KFM.",

  "kfm:review_cycle": "Biannual",
  "_comment_review_cycle": "Used by FAIR+CARE governance for re-validation scheduling.",

  "care:sensitivity": "general",
  "_comment_care_sensitivity": "Lithics datasets rarely require advanced restriction.",

  "care:review": "faircare",
  "_comment_care_review": "Reviewed via FAIR+CARE council.",

  "care:notes": "Lithics generally low sensitivity; ensure no sacred lithic materials included.",
  "_comment_care_notes": "Important for ensuring cultural safety."
}
~~~

---

## 🧱 Annotated Template — Ceramics Collection

~~~json
{
  "stac_version": "1.0.0",
  "_comment_stac": "Always required.",

  "type": "Collection",
  "_comment_type": "STAC Collection grouping ceramic inventories.",

  "id": "ceramics",
  "_comment_id": "Required ID; used by catalog browser & graph mapping.",

  "description": "Ceramic inventories with motif categories generalized for cultural safety.",
  "_comment_description": "Explains how sensitive motifs are handled.",

  "license": "CC-BY-4.0",
  "_comment_license": "All KFM datasets must be open-license.",

  "extent": {
    "spatial": { "bbox": [[-101.9, 37.0, -94.9, 40.0]] },
    "_comment_spatial": "Generalized region for ceramic assemblages.",

    "temporal": { "interval": [["1000-01-01T00:00:00Z", "1800-01-01T00:00:00Z"]] },
    "_comment_temporal": "Covers major ceramic cultural phases."
  },

  "links": [],

  "kfm:material_class": "ceramic",
  "_comment_material": "Required classification term.",

  "kfm:domain": "archaeology:artifact-inventories",

  "kfm:review_cycle": "Biannual",

  "care:sensitivity": "general",
  "_comment_sensitivity": "Ceramic datasets may contain motif data requiring filtering.",

  "care:review": "faircare",

  "care:notes": "Motifs filtered to remove culturally restricted symbolism.",
  "_comment_notes": "Explains CARE transformations applied."
}
~~~

---

## 🧱 Annotated Template — Metals Collection

~~~json
{
  "stac_version": "1.0.0",
  "type": "Collection",
  "id": "metals",

  "description": "Protohistoric metal artifacts and trade items, generalized and reviewed.",
  
  "license": "CC-BY-4.0",

  "extent": {
    "spatial": { "bbox": [[-102.1, 37.0, -94.6, 40.1]] },
    "temporal": { "interval": [["1500-01-01T00:00:00Z", "1900-01-01T00:00:00Z"]] }
  },

  "links": [],

  "kfm:material_class": "metal",
  "kfm:domain": "archaeology:artifact-inventories",
  "kfm:review_cycle": "Biannual",

  "care:sensitivity": "generalized",
  "_comment_sensitivity": "Protohistoric materials often require removal of culturally sensitive associations.",
  
  "care:review": "tribal",
  "_comment_review": "Metals associated with contact-era sites require tribal consultation.",
  
  "care:notes": "Trade metal items reviewed for cultural implications."
}
~~~

---

## 🧱 Annotated Template — Faunal Collection

~~~json
{
  "stac_version": "1.0.0",
  "type": "Collection",
  "id": "faunal",

  "description": "Public-domain faunal datasets for archaeological correlation.",
  
  "license": "CC-BY-4.0",

  "extent": {
    "spatial": { "bbox": [[-102.1, 37.0, -94.6, 40.1]] },
    "temporal": { "interval": [["0-01-01T00:00:00Z", "2025-01-01T00:00:00Z"]] }
  },

  "links": [],

  "kfm:material_class": "faunal",
  "kfm:domain": "archaeology:artifact-inventories",

  "care:sensitivity": "general",
  "_comment_sensitivity": "Faunal datasets must exclude sacred species.",
  
  "care:review": "faircare",

  "care:notes": "Dataset restricted to public-domain faunal observations."
}
~~~

---

## 📚 Field Guide (Located at `field_guide.md`)

The field guide provides:

- Definitions for all **STAC core fields**  
- **KFM archaeology extension** (`kfm:*`) requirements  
- **CARE** sensitivity rules  
- Controlled vocabularies used across artifact metadata  
- Spatial & temporal generalization rules  
- KFM → Neo4j → DCAT → STAC crosswalks  

---

## 🧪 Validation Workflow for Contributors

1. Choose appropriate annotated template.  
2. Copy → adapt → save as real STAC Collection.  
3. Validate against schemas:  
   - `stac-collection-schema.json`  
   - `kfm-archaeology-extension.json`  
   - `care-sensitivity-extension.json`  
4. Verify CARE visibility rules:  
   - `h3-only`  
   - `no-exact-points`  
5. Confirm metadata alignment with dataset file + provenance file.  
6. Submit PR → FAIR+CARE council review → approval.  

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|---|---|---|---|
| v10.4.0 | 2025-11-17 | Archaeology WG · FAIR+CARE Council | Created annotated artifact STAC collection templates library with CARE + KFM extension commentary |
| v10.0.0 | 2025-11-10 | Artifact Metadata Team | Initial placeholder annotation directory |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — CC-BY 4.0**  
FAIR+CARE Certified · MCP-DL v6.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  
[⬅ Back to Collection Templates](../README.md)

</div>