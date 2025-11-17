---
title: "🧩 Kansas Frontier Matrix — Artifact STAC Schema Templates (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/datasets/artifact-inventories/stac/schemas/templates/README.md"
version: "v10.4.0"
last_updated: "2025-11-17"
review_cycle: "Biannual · Archaeology Working Group · FAIR+CARE Council · Metadata Standards Subcommittee"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../../../releases/v10.4.0/sbom.spdx.json"
manifest_ref: "../../../../../../../../releases/v10.4.0/manifest.zip"
telemetry_ref: "../../../../../../../../releases/v10.4.0/focus-telemetry.json"
telemetry_schema: "../../../../../../../../schemas/telemetry/archaeology-artifact-stac-schema-templates-v1.json"
governance_ref: "../../../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4"
status: "Active / Enforced"
doc_kind: "Schema Template Library"
intent: "artifact-inventory-stac-schema-templates"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Compliant"
---

<div align="center">

# 🧩 **Kansas Frontier Matrix — Artifact STAC Schema Templates**  
`docs/analyses/archaeology/datasets/artifact-inventories/stac/schemas/templates/README.md`

**Purpose:**  
Provide **validated schema templates** for building new STAC Item and STAC Collection schemas for artifact inventory datasets in the Kansas Frontier Matrix (KFM).  
These templates ensure new schemas remain fully compliant with:

- **STAC 1.0 Core Specification**  
- **Projection (`proj`) Extension**  
- **Scientific Extension (`sci`)**  
- **Versioning Extension (`version`)**  
- **Checksum Extension (`checksum`)**  
- **KFM Archaeology Extension (`kfm:*`)**  
- **CARE Cultural Safety Extension (`care:*`)**  
- **DCAT 3.0 Crosswalk Requirements**  
- **MCP-DL v6.3 Documentation Standards**

All schema templates in this folder are meant to be **cloned, adapted, and expanded** by contributors building new metadata validators.

</div>

---

## 📘 Overview

This directory defines:

- Starter templates for new **STAC Item schemas**  
- Starter templates for new **STAC Collection schemas**  
- Extension templates for **KFM Archaeology fields**  
- Extension templates for **CARE sensitivity metadata**  
- Templates for **DCAT–STAC crosswalk schemas**  
- Instructions for integrating new schemas into CI validation pipelines  

All templates follow **JSON Schema Draft 2020–12**.

---

## 🗂️ Directory Layout

~~~text
docs/analyses/archaeology/datasets/artifact-inventories/stac/schemas/templates/
├── README.md                                 # This file
├── template-stac-item-schema.json            # Base STAC Item schema template
├── template-stac-collection-schema.json      # Base STAC Collection schema template
├── template-kfm-extension-schema.json        # KFM archaeology extension template
├── template-care-extension-schema.json       # CARE cultural safety schema template
├── template-dcat-crosswalk.json              # STAC ↔ DCAT mapping template
└── annotated/                                # Fully annotated versions of each template
~~~

---

## 📦 Template — STAC Item Schema (Minimal)

~~~json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "KFM Artifact Inventory — STAC Item Schema Template",
  "type": "object",

  "required": ["id", "stac_version", "type", "bbox", "geometry", "properties", "assets"],

  "properties": {
    "stac_version": { "const": "1.0.0" },
    "type": { "const": "Feature" },

    "id": {
      "type": "string",
      "description": "Dataset ID (matches STAC Item filename)."
    },

    "bbox": {
      "type": "array",
      "minItems": 4,
      "maxItems": 4,
      "items": { "type": "number" }
    },

    "geometry": {
      "type": "object",
      "properties": {
        "type": { "enum": ["MultiPoint", "Polygon", "MultiPolygon"] }
      },
      "required": ["type"]
    },

    "properties": {
      "type": "object"
    },

    "assets": {
      "type": "object",
      "required": ["data"],
      "properties": {
        "data": {
          "type": "object",
          "required": ["href", "type", "roles"],
          "properties": {
            "href": { "type": "string" },
            "type": { "type": "string" },
            "roles": { "type": "array", "items": { "type": "string" } }
          }
        }
      }
    }
  }
}
~~~

---

## 📦 Template — STAC Collection Schema (Minimal)

~~~json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "KFM Artifact Inventory — STAC Collection Schema Template",
  "type": "object",

  "required": ["id", "stac_version", "type", "extent", "license"],

  "properties": {
    "stac_version": { "const": "1.0.0" },
    "type": { "const": "Collection" },

    "id": {
      "type": "string",
      "description": "Collection ID."
    },

    "description": {
      "type": "string"
    },

    "license": {
      "type": "string",
      "description": "SPDX license identifier (CC-BY-4.0 for KFM)."
    },

    "extent": {
      "type": "object",
      "required": ["spatial", "temporal"],

      "properties": {
        "spatial": {
          "type": "object",
          "properties": {
            "bbox": {
              "type": "array",
              "items": {
                "type": "array",
                "items": { "type": "number" }
              }
            }
          }
        },
        "temporal": {
          "type": "object",
          "properties": {
            "interval": {
              "type": "array",
              "items": {
                "type": "array",
                "items": { "type": "string" }
              }
            }
          }
        }
      }
    }
  }
}
~~~

---

## 📦 Template — KFM Archaeology Extension Schema

~~~json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "KFM Archaeology Extension Schema Template",
  "type": "object",

  "properties": {
    "kfm:phase": { "type": "string" },
    "kfm:material_class": { "enum": ["lithic", "ceramic", "metal", "faunal", "all"] },
    "kfm:datatype": { "const": "artifact-inventory" },
    "kfm:source": { "type": "string" },
    "kfm:provenance": { "type": "string" },
    "kfm:review_cycle": { "type": "string" }
  }
}
~~~

---

## 📦 Template — CARE Sensitivity Schema

~~~json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "CARE Sensitivity Extension Template",
  "type": "object",

  "properties": {
    "care:sensitivity": { "enum": ["general", "generalized", "restricted-generalized"] },
    "care:review": { "enum": ["faircare", "tribal", "none-required"] },
    "care:notes": { "type": "string" },
    "care:visibility_rules": { "enum": ["h3-only", "no-exact-points"] }
  }
}
~~~

---

## 📦 Template — DCAT Crosswalk Schema

~~~json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "DCAT–STAC Crosswalk Template",
  "type": "object",

  "properties": {
    "dct:title": { "type": "string" },
    "dct:license": { "type": "string" },
    "dct:temporal": { "type": "string" },
    "dcat:distribution": { "type": "string" },
    "dcat:keyword": {
      "type": "array",
      "items": { "type": "string" }
    }
  }
}
~~~

---

## 🧪 Validation Workflow

Contributors MUST validate new schemas using:

- `jsonschema` (Python)  
- KFM’s schema validator in CI  
- `ajv` (Node) for testing draft-2020–12 compatibility  

Once validated, schemas should be added to:

- `.github/workflows/artifact-stac-validate.yml`  
- `docs/analyses/archaeology/validation/` crosswalks  

---

## 🧠 Tips for Building New Schemas

- Always start from these templates—never from scratch.  
- Keep schemas strict to avoid malformed metadata entering KFM.  
- Use controlled vocabularies for all archaeology domain fields.  
- Mark all culturally sensitive metadata clearly (`care:*`).  
- Enforce H3 generalization rules via schema where possible.  
- Include description fields to support MCP documentation-first workflows.  

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|---|---|---|---|
| v10.4.0 | 2025-11-17 | Archaeology WG · FAIR+CARE Council | Added complete schema templates for artifact inventories; includes KFM & CARE extensions and DCAT crosswalk scaffolds |
| v10.0.0 | 2025-11-10 | Artifact Metadata Team | Initial directory and templates placeholder |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — CC-BY 4.0**  
FAIR+CARE Certified · MCP-DL v6.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  
[⬅ Back to Schema Documentation](../README.md)

</div>