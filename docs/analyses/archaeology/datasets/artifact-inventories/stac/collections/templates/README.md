---
title: "📁 Kansas Frontier Matrix — Artifact STAC Collection Templates (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/datasets/artifact-inventories/stac/collections/templates/README.md"
version: "v10.4.0"
last_updated: "2025-11-17"
review_cycle: "Biannual · Archaeology Working Group · FAIR+CARE Council · Metadata Standards Subcommittee"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../../../releases/v10.4.0/sbom.spdx.json"
manifest_ref: "../../../../../../../../releases/v10.4.0/manifest.zip"
telemetry_ref: "../../../../../../../../releases/v10.4.0/focus-telemetry.json"
telemetry_schema: "../../../../../../../../schemas/telemetry/archaeology-artifact-stac-collection-templates-v1.json"
governance_ref: "../../../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4"
status: "Active / Enforced"
doc_kind: "Template Library"
intent: "artifact-inventory-stac-collection-templates"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Compliant"
---

<div align="center">

# 📁 **Kansas Frontier Matrix — Artifact STAC Collection Templates**  
`docs/analyses/archaeology/datasets/artifact-inventories/stac/collections/templates/README.md`

**Purpose:**  
Provide a library of **validated STAC Collection templates** for all artifact inventory categories within the Kansas Frontier Matrix (KFM).  
These templates guarantee contributors produce metadata-complete, FAIR+CARE-aligned, KFM-compatible STAC Collections without risk of schema violations or cultural sensitivity breaches.

Templates follow:

- **STAC 1.0 Core Specification**  
- **KFM Archaeology STAC Extension (`kfm:*`)**  
- **CARE Cultural Safety Extension (`care:*`)**  
- **DCAT 3.0 crosswalk requirements**  
- **MCP-DL v6.3 documentation-first standards**

These templates act as the **required starting point** for any new artifact inventory Collection.

</div>

---

## 🗂️ Directory Layout

~~~text
docs/analyses/archaeology/datasets/artifact-inventories/stac/collections/templates/
├── README.md                                 # This file
├── template-collection-root.json             # Root artifact-inventories collection template
├── template-collection-lithics.json          # Lithic artifact collection
├── template-collection-ceramics.json         # Ceramic artifact collection
├── template-collection-metals.json           # Metal/protohistoric artifact collection
├── template-collection-faunal.json           # Faunal (public domain) artifact collection
└── annotated/                                # Annotated templates with inline guidance
~~~

---

## 📘 Template Purpose and Usage

All artifact inventory STAC Collections **must begin** from one of these templates.

They ensure:
- Consistency across all artifact metadata  
- Correct use of archaeological domain vocabulary  
- Proper inclusion of CARE sensitivity metadata  
- Compliance with DCAT crosswalk fields  
- Compatibility with catalog browsers and STAC crawlers  
- Enforceable reproducibility and provenance tracking  

Contributors should:

1. Copy the appropriate template into `../`  
2. Fill in required fields (title, description, extent, keywords)  
3. Update `kfm:*` fields to match dataset class  
4. Confirm CARE sensitivity classification  
5. Validate using schema in `../../schemas/`  
6. Link to child Items in `../items/`  

---

## 📦 Example — Root Artifact Collection Template (Minimal)

~~~json
{
  "stac_version": "1.0.0",
  "type": "Collection",
  "id": "artifact-inventories",
  "description": "Root collection for all artifact inventory datasets in the Kansas Frontier Matrix.",
  "license": "CC-BY-4.0",

  "extent": {
    "spatial": { "bbox": [[-102.1, 37.0, -94.6, 40.1]] },
    "temporal": { "interval": [["1000-01-01T00:00:00Z", "2025-01-01T00:00:00Z"]] }
  },

  "links": [],

  "kfm:material_class": "all",
  "kfm:domain": "archaeology:artifact-inventories",
  "kfm:review_cycle": "Biannual",

  "care:sensitivity": "general",
  "care:review": "faircare",
  "care:notes": "All datasets within this collection must be generalized to H3 and culturally reviewed."
}
~~~

---

## 📦 Example — Lithics Collection Template

~~~json
{
  "stac_version": "1.0.0",
  "type": "Collection",
  "id": "lithics",
  "description": "Lithic artifact inventories from public-domain archaeological datasets.",
  "license": "CC-BY-4.0",

  "extent": {
    "spatial": { "bbox": [[-102.0, 37.0, -94.6, 40.1]] },
    "temporal": { "interval": [["1200-01-01T00:00:00Z", "1500-01-01T00:00:00Z"]] }
  },

  "links": [],

  "kfm:material_class": "lithic",
  "kfm:domain": "archaeology:artifact-inventories",
  "kfm:review_cycle": "Biannual",

  "care:sensitivity": "general",
  "care:review": "faircare",
  "care:notes": "Lithic inventories must be spatially generalized and culturally reviewed for tone and representation."
}
~~~

---

## 📦 Example — Ceramics Collection Template

~~~json
{
  "stac_version": "1.0.0",
  "type": "Collection",
  "id": "ceramics",
  "description": "Ceramic artifact inventories with generalized motif categories for cultural safety.",
  "license": "CC-BY-4.0",

  "extent": {
    "spatial": { "bbox": [[-101.9, 37.0, -94.9, 40.0]] },
    "temporal": { "interval": [["1000-01-01T00:00:00Z", "1800-01-01T00:00:00Z"]] }
  },

  "links": [],

  "kfm:material_class": "ceramic",
  "kfm:domain": "archaeology:artifact-inventories",
  "kfm:review_cycle": "Biannual",

  "care:sensitivity": "general",
  "care:review": "faircare",
  "care:notes": "Motif categories must exclude culturally restricted symbolism unless approved by tribal councils."
}
~~~

---

## 🧪 Validation Guidance for Template Use

Before committing a new STAC Collection derived from a template:

1. Validate against:  
   - `stac-collection-schema.json`  
   - `kfm-archaeology-extension.json`  
   - `care-sensitivity-extension.json`  
   - `dcat-crosswalk.json`  

2. Confirm all spatial metadata is generalized (H3 or simplified polygons).  

3. Ensure cultural-phase time spans match archaeological consensus.  

4. Confirm license is correct (PD or CC-BY only).  

5. Include `links` to all STAC Items belonging to the Collection.  

6. Run `.github/workflows/artifact-stac-validate.yml` locally if possible.  

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|---|---|---|---|
| v10.4.0 | 2025-11-17 | Archaeology WG · FAIR+CARE Council | Created full library of STAC Collection templates; added annotated directory and validation guidelines |
| v10.0.0 | 2025-11-10 | Artifact Metadata Team | Initial scaffold of template directory |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — CC-BY 4.0**  
FAIR+CARE Certified · MCP-DL v6.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  
[⬅ Back to STAC Collections](../README.md)

</div>