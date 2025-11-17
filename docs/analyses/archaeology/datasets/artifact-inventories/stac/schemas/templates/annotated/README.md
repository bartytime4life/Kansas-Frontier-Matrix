---
title: "📐📝 Kansas Frontier Matrix — Annotated STAC Schema Templates for Artifact Inventories (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/datasets/artifact-inventories/stac/schemas/templates/annotated/README.md"
version: "v10.4.0"
last_updated: "2025-11-17"
review_cycle: "Biannual · Metadata Standards Subcommittee · Archaeology WG · FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../../../../releases/v10.4.0/sbom.spdx.json"
manifest_ref: "../../../../../../../../../releases/v10.4.0/manifest.zip"
telemetry_ref: "../../../../../../../../../releases/v10.4.0/focus-telemetry.json"
telemetry_schema: "../../../../../../../../../schemas/telemetry/archaeology-artifact-stac-schema-templates-annotated-v1.json"
governance_ref: "../../../../../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4"
status: "Active / Enforced"
doc_kind: "Annotated Schema Templates"
intent: "artifact-inventory-stac-schema-templates-annotated"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Compliant"
---

<div align="center">

# 📐📝 **Kansas Frontier Matrix — Annotated STAC Schema Templates**  
`docs/analyses/archaeology/datasets/artifact-inventories/stac/schemas/templates/annotated/README.md`

**Purpose:**  
Provide deeply annotated, line-by-line **JSON Schema templates** for validating artifact inventory **STAC Items** and **STAC Collections** within the Kansas Frontier Matrix (KFM).  
These annotated templates explicitly explain:

- STAC 1.0 core validation logic  
- KFM archaeology extension field rules (`kfm:*`)  
- CARE cultural safety metadata schema (`care:*`)  
- DCAT 3.0 crosswalk validation  
- Provenance requirements (PROV-O)  
- Spatial + temporal generalization constraints  
- CI validation expectations  

These are the **authoritative schema-learning resources** for contributors writing or modifying STAC schemas in KFM.

</div>

---

# 📘 Overview

This directory contains annotated versions of:

- **STAC Item schema**  
- **STAC Collection schema**  
- **KFM Archaeology Extension schema**  
- **CARE Cultural Safety Extension schema**  
- **DCAT Crosswalk validation schema**

Each annotated file includes:

- Inline comments describing schema purpose  
- Application rules within the archaeology domain  
- Acceptable value ranges  
- Cultural safety constraints  
- Cross-schema interaction notes  
- CI validation requirements  

All examples use JSON Schema Draft 2020–12 and are fully compatible with KFM’s automated schema validators.

---

# 🗂️ Directory Layout

~~~text
docs/analyses/archaeology/datasets/artifact-inventories/stac/schemas/templates/annotated/
├── README.md                                 # This file
├── stac_item_annotated.json                  # Annotated STAC Item schema template
├── stac_collection_annotated.json            # Annotated STAC Collection schema template
├── kfm_extension_annotated.json              # Annotated archaeology extension schema
├── care_extension_annotated.json             # Annotated CARE cultural safety schema
└── dcat_crosswalk_annotated.json             # Annotated DCAT crosswalk schema
~~~

---

# 🧱 Annotated Template — STAC Item Schema

~~~json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "_comment": "All KFM schemas use JSON Schema Draft 2020-12.",

  "title": "Annotated STAC Item Schema Template — Artifact Inventory",
  "_comment_title": "Human-readable name used in schema validators.",

  "type": "object",
  "_comment_type": "STAC Items must be JSON objects.",

  "required": [
    "id",
    "type",
    "stac_version",
    "bbox",
    "geometry",
    "properties",
    "assets"
  ],
  "_comment_required": "These fields are required by the STAC 1.0 specification.",

  "properties": {
    "stac_version": {
      "const": "1.0.0",
      "_comment": "KFM only supports STAC 1.0.0."
    },

    "type": {
      "const": "Feature",
      "_comment": "All STAC Items must be type=Feature."
    },

    "id": {
      "type": "string",
      "_comment": "Dataset identifier; must match filename and version suffix."
    },

    "bbox": {
      "type": "array",
      "minItems": 4,
      "maxItems": 4,
      "_comment": "Bounding box must be generalized—never derived from raw site coordinates."
    },

    "geometry": {
      "type": "object",
      "properties": {
        "type": { "enum": ["MultiPoint", "Polygon", "MultiPolygon"] }
      },
      "required": ["type"],
      "_comment": "Raw point geometries forbidden; all geometry must be generalized."
    },

    "properties": {
      "type": "object",
      "_comment": "Holds kfm:* and care:* extension fields."
    },

    "assets": {
      "type": "object",
      "properties": {
        "data": {
          "type": "object",
          "required": ["href", "type", "roles"],
          "_comment": "Data asset must reference the actual inventory CSV."
        }
      },
      "required": ["data"]
    }
  }
}
~~~

---

# 🧱 Annotated Template — STAC Collection Schema

~~~json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",

  "title": "Annotated STAC Collection Schema Template",
  "_comment": "Defines grouping metadata for artifact datasets.",

  "type": "object",

  "required": ["id", "type", "stac_version", "extent", "license"],

  "properties": {
    "stac_version": {
      "const": "1.0.0",
      "_comment": "STAC version must match artifact STAC Items."
    },

    "type": {
      "const": "Collection",
      "_comment": "Collections group Items."
    },

    "id": {
      "type": "string",
      "_comment": "Identifier must match folders in stac/collections."
    },

    "description": {
      "type": "string",
      "_comment": "Readable summary; required for users and STAC browsers."
    },

    "license": {
      "type": "string",
      "_comment": "SPDX license must be CC-BY-4.0 or CC0 for PD data."
    },

    "extent": {
      "type": "object",
      "required": ["spatial", "temporal"],
      "_comment": "STAC requires both spatial and temporal coverage metadata.",

      "properties": {
        "spatial": {
          "type": "object",
          "properties": {
            "bbox": {
              "type": "array",
              "items": { "type": "array", "items": { "type": "number" } }
            }
          },
          "_comment_spatial": "Generalized bounding boxes only."
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
          },
          "_comment_temporal": "OWL-Time compatible start/end timestamps."
        }
      }
    }
  }
}
~~~

---

# 🧱 Annotated Template — KFM Archaeology Extension Schema

~~~json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",

  "title": "KFM Archaeology Extension (Annotated)",
  "_comment": "Defines archaeology-specific STAC metadata fields.",

  "type": "object",

  "properties": {
    "kfm:phase": {
      "type": "string",
      "_comment": "Cultural-phase classification ('Late Prehistoric', 'Middle Ceramic', etc.)."
    },

    "kfm:material_class": {
      "enum": ["lithic", "ceramic", "metal", "faunal", "all"],
      "_comment": "Controlled vocabulary for material type."
    },

    "kfm:datatype": {
      "const": "artifact-inventory",
      "_comment": "Hard-coded classification for artifact inventories."
    },

    "kfm:source": {
      "type": "string",
      "_comment": "Source institution or PD archive."
    },

    "kfm:provenance": {
      "type": "string",
      "_comment": "Path to PROV-O lineage JSON file."
    },

    "kfm:review_cycle": {
      "type": "string",
      "_comment": "Validation frequency (Biannual, Quarterly)."
    }
  }
}
~~~

---

# 🧱 Annotated Template — CARE Sensitivity Extension Schema

~~~json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",

  "title": "CARE Sensitivity Extension (Annotated)",

  "type": "object",

  "properties": {
    "care:sensitivity": {
      "enum": ["general", "generalized", "restricted-generalized"],
      "_comment": "Artifact inventories may NOT use 'restricted'. Use 'generalized' for anything derived from sensitive areas."
    },

    "care:review": {
      "enum": ["faircare", "tribal", "none-required"],
      "_comment": "Tribal review required for protohistoric metal datasets."
    },

    "care:notes": {
      "type": "string",
      "_comment": "Explains cultural safety adjustments (e.g., motif filtering, location generalization)."
    },

    "care:visibility_rules": {
      "enum": ["h3-only", "no-exact-points"],
      "_comment": "`h3-only` forbids any visible geometry in the STAC Item; only H3 region is allowed."
    }
  }
}
~~~

---

# 🧱 Annotated Template — DCAT Crosswalk Schema

~~~json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",

  "title": "DCAT → STAC Crosswalk (Annotated)",

  "type": "object",

  "properties": {
    "dct:title": {
      "type": "string",
      "_comment": "Maps to STAC 'description' or collection name."
    },

    "dct:license": {
      "type": "string",
      "_comment": "Must match STAC 'license'."
    },

    "dct:temporal": {
      "type": "string",
      "_comment": "OWL-Time interval; must match STAC temporal extent."
    },

    "dcat:distribution": {
      "type": "string",
      "_comment": "Maps to STAC assets.data.href."
    },

    "dcat:keyword": {
      "type": "array",
      "items": { "type": "string" },
      "_comment": "Optional but recommended."
    }
  }
}
~~~

---

# 🧪 Validation Rules for Contributors

Before committing any new schema built from these annotated templates:

1. Validate using:
   - `jsonschema` or `ajv`
   - KFM’s schema validator (in CI)
2. Confirm all controlled vocabularies are followed.
3. Ensure CARE sensitivity constraints are correct.
4. Verify crosswalk consistency:
   - STAC Item ↔ DCAT metadata ↔ Provenance JSON
5. Add new schema references to:
   - `.github/workflows/artifact-stac-validate.yml`

---

# 🕰️ Version History

| Version | Date | Author | Summary |
|---|---|---|---|
| v10.4.0 | 2025-11-17 | Metadata Subcommittee · Archaeology WG · FAIR+CARE Council | Full annotated STAC schema template suite for artifact inventories; added KFM & CARE field commentary; ensured KFM-MDP v10.4 formatting |
| v10.0.0 | 2025-11-10 | Artifact Metadata Team | Initial placeholder annotation directory |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — CC-BY 4.0**  
FAIR+CARE Certified · MCP-DL v6.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  
[⬅ Back to Schema Templates](../README.md)

</div>