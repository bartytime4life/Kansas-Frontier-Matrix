---
title: "📄 Kansas Frontier Matrix — Artifact Inventory STAC Item Templates (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/datasets/artifact-inventories/stac/items/templates/README.md"
version: "v10.4.0"
last_updated: "2025-11-17"
review_cycle: "Biannual · Archaeology Working Group · FAIR+CARE Council · Metadata Standards Subcommittee"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../../../releases/v10.4.0/sbom.spdx.json"
manifest_ref: "../../../../../../../../releases/v10.4.0/manifest.zip"
telemetry_ref: "../../../../../../../../releases/v10.4.0/focus-telemetry.json"
telemetry_schema: "../../../../../../../../schemas/telemetry/archaeology-artifact-stac-item-templates-v1.json"
governance_ref: "../../../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4"
status: "Active / Enforced"
doc_kind: "Template Library"
intent: "artifact-stac-item-templates"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Compliant"
---

<div align="center">

# 📄 **Kansas Frontier Matrix — Artifact Inventory STAC Item Templates**  
`docs/analyses/archaeology/datasets/artifact-inventories/stac/items/templates/README.md`

**Purpose:**  
Provide the official **STAC Item templates** for contributing new artifact inventory datasets to the Kansas Frontier Matrix (KFM).  
These templates guarantee full compliance with:

- **STAC 1.0 Core Specification**  
- **Projection (`proj`) Extension**  
- **Versioning Extension**  
- **Checksum Extension**  
- **Scientific Extension (`sci`)**  
- **KFM Archaeology Extension (`kfm:*`)**  
- **CARE Cultural Safety Extension (`care:*`)**  
- **DCAT 3.0 Metadata Alignment**  
- **MCP-DL v6.3 Documentation-First Protocol**  

These templates *must* be used for every new artifact inventory dataset before validation and ingestion.

</div>

---

## 🗂️ Directory Layout

~~~text
docs/analyses/archaeology/datasets/artifact-inventories/stac/items/templates/
├── README.md                                   # This file
├── template-lithic-item.json                   # Template for lithic artifact inventories
├── template-ceramic-item.json                  # Template for ceramic artifact inventories
├── template-metal-item.json                    # Template for protohistoric metal inventories
├── template-faunal-item.json                   # Template for faunal (public-domain only) datasets
└── annotated/                                   # Fully annotated versions of each template
~~~

---

## 📘 General Instructions for Contributors

Before creating any new STAC Item:

1. **Choose the correct template** based on material class.  
2. **Copy the template** into `../items/` and rename appropriately.  
3. Fill all required fields:
   - Cultural phase
   - Sensitivity level
   - Provenance reference
   - Inventory asset location
   - Bounding box / generalized geometry  
4. Validate the file using schemas in:  
   - `../../schemas/`  
5. Submit for archaeology WG + FAIR+CARE review.  
6. Only after approval, commit to the main catalog.

---

## 📦 Template: Lithic Artifact Inventory (Minimal)

~~~json
{
  "stac_version": "1.0.0",
  "type": "Feature",
  "id": "TEMPLATE-LITHICS-ID",
  "bbox": [-102.0, 37.0, -94.6, 40.1],
  "geometry": {
    "type": "MultiPoint",
    "coordinates": [[ /* H3-generalized sample */ ]]
  },
  "properties": {
    "kfm:phase": "PHASE-HERE",
    "care:sensitivity": "generalized",
    "kfm:material_class": "lithic",
    "kfm:datatype": "artifact-inventory",
    "kfm:source": "INSTITUTION",
    "kfm:provenance": "../../provenance/FILE.json"
  },
  "assets": {
    "data": {
      "href": "../../inventories/FILE.csv",
      "type": "text/csv",
      "roles": ["data"]
    }
  },
  "links": [
    {
      "rel": "collection",
      "href": "../collections/lithics.json"
    }
  ]
}
~~~

---

## 📦 Template: Ceramic Artifact Inventory (Minimal)

~~~json
{
  "stac_version": "1.0.0",
  "type": "Feature",
  "id": "TEMPLATE-CERAMICS-ID",
  "bbox": [-102.0, 37.0, -94.6, 40.1],
  "geometry": {
    "type": "MultiPoint",
    "coordinates": [[ /* generalized */ ]]
  },
  "properties": {
    "kfm:phase": "PHASE-HERE",
    "care:sensitivity": "generalized",
    "care:notes": "MOTIF-SAFETY-NOTES",
    "kfm:material_class": "ceramic",
    "kfm:datatype": "artifact-inventory",
    "kfm:source": "INSTITUTION",
    "kfm:provenance": "../../provenance/FILE.json"
  },
  "assets": {
    "data": {
      "href": "../../inventories/FILE.csv",
      "type": "text/csv",
      "roles": ["data"]
    }
  },
  "links": [
    {
      "rel": "collection",
      "href": "../collections/ceramics.json"
    }
  ]
}
~~~

---

## 📦 Template: Metal / Protohistoric Artifact Inventory (Minimal)

~~~json
{
  "stac_version": "1.0.0",
  "type": "Feature",
  "id": "TEMPLATE-METALS-ID",
  "bbox": [-102.0, 37.0, -94.6, 40.1],
  "geometry": {
    "type": "MultiPoint",
    "coordinates": [[ /* generalized */ ]]
  },
  "properties": {
    "kfm:phase": "PHASE-HERE",
    "care:sensitivity": "generalized",
    "care:review": "tribal",
    "care:notes": "Describe cultural consultation outcomes here.",
    "kfm:material_class": "metal",
    "kfm:datatype": "artifact-inventory",
    "kfm:source": "INSTITUTION",
    "kfm:provenance": "../../provenance/FILE.json"
  },
  "assets": {
    "data": {
      "href": "../../inventories/FILE.csv",
      "type": "text/csv",
      "roles": ["data"]
    }
  },
  "links": [
    {
      "rel": "collection",
      "href": "../collections/metals.json"
    }
  ]
}
~~~

---

## 📦 Template: Faunal Artifact Inventory (Minimal — PD Only)

~~~json
{
  "stac_version": "1.0.0",
  "type": "Feature",
  "id": "TEMPLATE-FAUNAL-ID",
  "bbox": [-102.0, 37.0, -94.6, 40.1],
  "geometry": {
    "type": "MultiPoint",
    "coordinates": [[ /* generalized */ ]]
  },
  "properties": {
    "kfm:phase": "PHASE-HERE",
    "care:sensitivity": "general",
    "kfm:material_class": "faunal",
    "kfm:datatype": "artifact-inventory",
    "kfm:source": "INSTITUTION",
    "kfm:provenance": "../../provenance/FILE.json"
  },
  "assets": {
    "data": {
      "href": "../../inventories/FILE.csv",
      "type": "text/csv",
      "roles": ["data"]
    }
  },
  "links": [
    {
      "rel": "collection",
      "href": "../collections/faunal.json"
    }
  ]
}
~~~

---

## 🧪 Validation Requirements

For any new STAC Item created from these templates, contributors MUST validate:

1. **STAC 1.0 core structure**  
2. **KFM archaeology extension**  
3. **CARE cultural safety fields**  
4. **DCAT alignment**  
5. **Checksum extension**  
6. **Correct provenance linkage**  
7. **Generalization level** (absolute requirement: H3 generalized, never raw provenience)

Validation workflows:  
- `.github/workflows/artifact-stac-validate.yml`  
- `docs/analyses/archaeology/validation/`

---

## 🧠 Tips for Contributors

- Use **ISO 8601** for all temporal metadata.  
- Use **EPSG:4326** as default CRS.  
- Ensure **no sensitive details** appear in descriptions or metadata.  
- When uncertain about cultural safety, mark as `"care:review": "tribal"` and request FAIR+CARE guidance.  
- Keep IDs consistent across inventory → metadata → provenance → STAC.  
- Use H3 **level 5–7** for spatial generalization.

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|---|---|---|---|
| v10.4.0 | 2025-11-17 | Archaeology WG · FAIR+CARE Council | Added complete artifact STAC item template suite with cultural safety rules and validation guidance |
| v10.0.0 | 2025-11-10 | Artifact Metadata Team | Initial structure and placeholder templates |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — CC-BY 4.0**  
FAIR+CARE Certified · MCP-DL v6.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  
[⬅ Back to STAC Items](../README.md)

</div>