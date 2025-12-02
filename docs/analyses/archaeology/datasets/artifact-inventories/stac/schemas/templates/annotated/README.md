---
title: "📐📝 Kansas Frontier Matrix — Annotated STAC Schema Templates for Artifact Inventories (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/datasets/artifact-inventories/stac/schemas/templates/annotated/README.md"
description: "Annotated JSON Schema templates for validating KFM v11 artifact-inventory STAC Items and Collections, with field-by-field KFM and CARE commentary."
version: "v11.2.3"
last_updated: "2025-12-02"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Biannual · Archaeology Working Group · FAIR+CARE Council · Metadata Standards Subcommittee"
content_stability: "stable"
status: "Active / Enforced"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-version-hash>"
doc_uuid: "urn:kfm:doc:archaeology-artifact-stac-schema-templates-annotated-v11.2.3"
doc_kind: "Annotated Schema Templates"
intent: "artifact-inventory-stac-schema-templates-annotated"
semantic_document_id: "kfm-doc-archaeology-artifact-stac-schema-templates-annotated-v11.2.3"
category: "Analyses · Archaeology · STAC Schemas · Templates"

sbom_ref: "../../../../../../../../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../../../../../../../../releases/v11.2.3/manifest.zip"
telemetry_ref: "../../../../../../../../../releases/v11.2.3/focus-telemetry.json"
telemetry_schema: "../../../../../../../../../schemas/telemetry/archaeology-artifact-stac-schema-templates-annotated-v1.json"
energy_schema: "../../../../../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../../../../../schemas/telemetry/carbon-gco2e-v1.json"

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

data_steward: "Metadata Standards Subcommittee · Archaeology Working Group"
provenance_chain:
  - "docs/analyses/archaeology/datasets/artifact-inventories/stac/schemas/templates/annotated/README.md@v10.4.0"
provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: true
---

# 📐📝 Kansas Frontier Matrix — Annotated STAC Schema Templates

`docs/analyses/archaeology/datasets/artifact-inventories/stac/schemas/templates/annotated/README.md`

**Purpose**  
Provide **annotated JSON Schema templates** for validating artifact-inventory **STAC Items** and **STAC Collections** within the Kansas Frontier Matrix (KFM).

These annotated templates explain:

- STAC 1.0 core validation logic  
- KFM archaeology extension field rules (`kfm:*`)  
- CARE cultural safety metadata schema (`care:*`)  
- DCAT 3.0 crosswalk validation patterns  
- Provenance requirements (PROV-O)  
- Spatial and temporal generalization constraints  
- CI validation expectations for KFM v11  

They are the **authoritative learning resources** for contributors who write or modify STAC schemas in KFM.

---

## 📘 Overview

This directory contains annotated versions of:

- STAC Item schema  
- STAC Collection schema  
- KFM Archaeology Extension schema  
- CARE Cultural Safety Extension schema  
- DCAT Crosswalk validation schema  

Each annotated file includes:

- Inline `_comment` fields describing schema purpose and semantics  
- Domain rules for archaeology (`kfm:*`) and CARE (`care:*`)  
- Acceptable values and controlled vocabularies  
- Cultural safety and sovereignty constraints  
- Notes on how schemas interact with DCAT and PROV-O  
- CI validation and integration hints  

All schemas use **JSON Schema Draft 2020-12** and are compatible with KFM’s automated validators.

---

## 🗂️ Directory Layout

~~~text
docs/analyses/archaeology/datasets/artifact-inventories/stac/schemas/templates/annotated/
├── 📄 README.md                      # This file (annotated schemas index)
├── 📄 stac_item_annotated.json       # Annotated STAC Item schema template
├── 📄 stac_collection_annotated.json # Annotated STAC Collection schema template
├── 📄 kfm_extension_annotated.json   # Annotated KFM archaeology extension schema
├── 📄 care_extension_annotated.json  # Annotated CARE cultural safety schema
└── 📄 dcat_crosswalk_annotated.json  # Annotated DCAT crosswalk schema
~~~

This layout is **normative** for annotated artifact-inventory STAC schemas.

---

## 🧱 Annotated Template — STAC Item Schema

Illustrative fragment from `stac_item_annotated.json`:

~~~json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "_comment": "All KFM schemas use JSON Schema Draft 2020-12.",

  "title": "Annotated STAC Item Schema Template — Artifact Inventory",
  "_comment_title": "Human-readable name used in schema validators and documentation.",

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
  "_comment_required": "These fields are required by the STAC 1.0 specification for Items.",

  "properties": {
    "stac_version": {
      "const": "1.0.0",
      "_comment": "KFM artifact Items are locked to STAC 1.0.0."
    },

    "type": {
      "const": "Feature",
      "_comment": "All STAC Items must use type=\"Feature\"."
    },

    "id": {
      "type": "string",
      "_comment": "Dataset identifier; should match filename stem and version suffix."
    },

    "bbox": {
      "type": "array",
      "minItems": 4,
      "maxItems": 4,
      "_comment": "Bounding box must reflect generalized coverage, not raw site coordinates."
    },

    "geometry": {
      "type": "object",
      "properties": {
        "type": {
          "enum": ["MultiPoint", "Polygon", "MultiPolygon"]
        }
      },
      "required": ["type"],
      "_comment": "Raw point geometries are forbidden; geometry must be generalized (for example, H3-derived)."
    },

    "properties": {
      "type": "object",
      "_comment": "Contains KFM archaeology (kfm:*) and CARE (care:*) extension fields as well as other metadata."
    },

    "assets": {
      "type": "object",
      "properties": {
        "data": {
          "type": "object",
          "required": ["href", "type", "roles"],
          "_comment": "Primary inventory asset. Must point to the artifact inventory table.",
          "properties": {
            "href": {
              "type": "string",
              "_comment": "Relative or absolute path to the inventory CSV/Parquet."
            },
            "type": {
              "type": "string",
              "_comment": "MIME type for the inventory asset, for example, text/csv."
            },
            "roles": {
              "type": "array",
              "items": { "type": "string" },
              "_comment": "Must include \"data\" to mark the main data asset."
            }
          }
        }
      },
      "required": ["data"]
    }
  }
}
~~~

---

## 🧱 Annotated Template — STAC Collection Schema

Illustrative fragment from `stac_collection_annotated.json`:

~~~json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",

  "title": "Annotated STAC Collection Schema Template",
  "_comment": "Defines grouping metadata for artifact inventory datasets.",

  "type": "object",

  "required": ["id", "type", "stac_version", "extent", "license"],

  "properties": {
    "stac_version": {
      "const": "1.0.0",
      "_comment": "Collection STAC version must match associated Items."
    },

    "type": {
      "const": "Collection",
      "_comment": "Collection documents group multiple Items."
    },

    "id": {
      "type": "string",
      "_comment": "Identifier should align with Collection filename and directory naming."
    },

    "description": {
      "type": "string",
      "_comment": "Readable summary for humans and STAC browsers."
    },

    "license": {
      "type": "string",
      "_comment": "SPDX license string (for example, CC-BY-4.0)."
    },

    "extent": {
      "type": "object",
      "required": ["spatial", "temporal"],
      "_comment": "STAC Collections must describe both spatial and temporal coverage.",

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
          },
          "_comment_spatial": "Generalized bounding boxes only; no site-precise geometry."
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
          "_comment_temporal": "OWL-Time compatible start and end timestamps across all Items."
        }
      }
    }
  }
}
~~~

---

## 🧱 Annotated Template — KFM Archaeology Extension Schema

From `kfm_extension_annotated.json`:

~~~json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",

  "title": "KFM Archaeology Extension (Annotated)",
  "_comment": "Defines archaeology-specific metadata fields used by KFM artifact inventories.",

  "type": "object",

  "properties": {
    "kfm:phase": {
      "type": "string",
      "_comment": "Cultural-phase classification, used in timelines and Focus Mode."
    },

    "kfm:material_class": {
      "enum": ["lithic", "ceramic", "metal", "faunal", "all"],
      "_comment": "Controlled vocabulary for artifact material class."
    },

    "kfm:datatype": {
      "const": "artifact-inventory",
      "_comment": "KFM artifact inventory STAC Items must use this constant."
    },

    "kfm:source": {
      "type": "string",
      "_comment": "Source institution, archive, or project name."
    },

    "kfm:provenance": {
      "type": "string",
      "_comment": "Path or identifier for the PROV-O lineage record associated with this dataset."
    },

    "kfm:review_cycle": {
      "type": "string",
      "_comment": "Describes how often this dataset is revalidated (for example, Biannual)."
    }
  }
}
~~~

---

## 🧱 Annotated Template — CARE Sensitivity Extension Schema

From `care_extension_annotated.json`:

~~~json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",

  "title": "CARE Sensitivity Extension (Annotated)",
  "_comment": "Encodes cultural safety and sovereignty-related metadata.",

  "type": "object",

  "properties": {
    "care:sensitivity": {
      "enum": ["general", "generalized", "restricted-generalized"],
      "_comment": "Artifact inventories in the public catalog must not use 'restricted'."
    },

    "care:review": {
      "enum": ["faircare", "tribal", "none-required"],
      "_comment": "Tribal review is required for contact-era metals and other high-sensitivity datasets."
    },

    "care:notes": {
      "type": "string",
      "_comment": "Documents cultural safety adjustments (for example, motif filtering, H3 generalization)."
    },

    "care:visibility_rules": {
      "enum": ["h3-only", "no-exact-points"],
      "_comment": "`h3-only` can be used when no explicit geometry should be visible; only derived H3 indices."
    }
  }
}
~~~

---

## 🧱 Annotated Template — DCAT Crosswalk Schema

From `dcat_crosswalk_annotated.json`:

~~~json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",

  "title": "DCAT → STAC Crosswalk (Annotated)",
  "_comment": "Ensures DCAT metadata remains consistent with STAC fields.",

  "type": "object",

  "properties": {
    "dct:title": {
      "type": "string",
      "_comment": "Maps to STAC Collection description or a title field."
    },

    "dct:license": {
      "type": "string",
      "_comment": "Must match or be compatible with the STAC 'license' field."
    },

    "dct:temporal": {
      "type": "string",
      "_comment": "Represents temporal coverage; must align with STAC temporal extent."
    },

    "dcat:distribution": {
      "type": "string",
      "_comment": "Typically corresponds to STAC assets.data.href or related asset fields."
    },

    "dcat:keyword": {
      "type": "array",
      "items": { "type": "string" },
      "_comment": "Optional keyword list; may mirror STAC keywords where used."
    }
  }
}
~~~

---

## 🧪 Validation Rules for Schema Authors

When creating or modifying schemas based on these annotated templates:

1. **Validate the schema itself**  
   - Use a Draft 2020-12–compatible validator (for example, `jsonschema` in Python, `ajv` in Node).  

2. **Check controlled vocabularies**  
   - Ensure any `enum` values match KFM archaeology and CARE specifications.  

3. **Align with CARE and sovereignty policies**  
   - Confirm `care:*` rules match KFM governance requirements.  

4. **Verify crosswalk semantics**  
   - Make sure DCAT mappings reflect how fields are actually used in STAC metadata.  

5. **Integrate into CI**  
   - Add new or modified schemas to:
     - `.github/workflows/artifact-stac-validate.yml`  
     - Any archaeology-specific metadata validation docs or scripts.  

---

## 🕰 Version History

| Version   | Date       | Author                                               | Summary                                                                 |
|-----------|------------|------------------------------------------------------|-------------------------------------------------------------------------|
| v11.2.3   | 2025-12-02 | Metadata Standards Subcommittee · Archaeology WG     | Updated annotated schema templates for KFM v11.2.3; added energy/carbon telemetry references and clarified CARE/sovereignty semantics. |
| v10.4.0   | 2025-11-17 | Metadata Subcommittee · Archaeology WG · FAIR+CARE Council | Added annotated STAC schema template suite for artifact inventories; included KFM & CARE commentary and CI guidance. |
| v10.0.0   | 2025-11-10 | Artifact Metadata Team                               | Initial placeholder annotation directory.                              |

---

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
FAIR+CARE · Sovereignty-Governed  
KFM-MDP v11.2.2 · MCP-DL v6.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[⬅ Back to Schema Templates](../README.md)