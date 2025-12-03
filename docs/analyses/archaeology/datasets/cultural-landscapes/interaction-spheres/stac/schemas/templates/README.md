---
title: "🧩 Kansas Frontier Matrix — Interaction Sphere STAC Schema Templates (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/datasets/cultural-landscapes/interaction-spheres/stac/schemas/templates/README.md"
description: "Template library for JSON Schemas that validate KFM v11 interaction-sphere STAC Items and Collections, including KFM and CARE extensions and DCAT crosswalks."
version: "v11.2.3"
last_updated: "2025-12-02"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Biannual · Cultural Landscape Working Group · FAIR+CARE Council · Metadata Standards Subcommittee"
content_stability: "stable"
status: "Active / Enforced"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-version-hash>"
doc_uuid: "urn:kfm:doc:archaeology-interaction-spheres-stac-schema-templates-v11.2.3"
doc_kind: "Schema Template Library"
intent: "interaction-spheres-stac-schema-templates"
semantic_document_id: "kfm-doc-archaeology-interaction-spheres-stac-schema-templates-v11.2.3"
category: "Analyses · Archaeology · Cultural Landscapes · STAC · Schemas"

sbom_ref: "../../../../../../../../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../../../../../../../../releases/v11.2.3/manifest.zip"
telemetry_ref: "../../../../../../../../../releases/v11.2.3/focus-telemetry.json"
telemetry_schema: "../../../../../../../../../schemas/telemetry/archaeology-interaction-spheres-stac-schema-templates-v1.json"
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
sensitivity: "Cultural / Historical / Archaeological"
sensitivity_level: "Medium"
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

data_steward: "Cultural Landscape Working Group · Metadata Standards Subcommittee · FAIR+CARE Council"
provenance_chain:
  - "docs/analyses/archaeology/datasets/cultural-landscapes/interaction-spheres/stac/schemas/templates/README.md@v11.0.0"
provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: true
---

# 🧩 Kansas Frontier Matrix — Interaction Sphere STAC Schema Templates (v11)

`docs/analyses/archaeology/datasets/cultural-landscapes/interaction-spheres/stac/schemas/templates/README.md`

**Purpose**  
Provide **schema templates** for building JSON Schemas that validate **interaction-sphere STAC Items and Collections** in KFM v11.

These templates ensure that any new or extended schemas remain:

- STAC 1.0 core compliant  
- Integrated with KFM cultural-landscape extensions (`kfm:*`)  
- Ethically governed using CARE (`care:*`) and sovereignty policies  
- Aligned with the DCAT crosswalk and PROV-O provenance model  
- Compatible with the broader STAC schema patterns used for artifact inventories and other landscape data  

Schema authors MUST start from these templates rather than writing schemas from scratch.

---

## 📘 Overview

This directory defines:

- Starter templates for **STAC Item** schemas (interaction spheres)  
- Starter templates for **STAC Collection** schemas (interaction-sphere groupings)  
- Extension templates for **KFM interaction-sphere fields** (`kfm:*`)  
- Extension templates for **CARE sensitivity & sovereignty metadata** (`care:*`)  
- Templates for **DCAT ↔ STAC crosswalk** schemas specific to interaction spheres  

All templates use **JSON Schema Draft 2020-12**, consistent with global KFM schema practice.

---

## 🗂️ Directory Layout

~~~text
docs/analyses/archaeology/datasets/cultural-landscapes/interaction-spheres/stac/schemas/templates/
├── 📄 README.md                             # This file
├── 📄 template-stac-item-schema.json        # Base Item schema template (interaction spheres)
├── 📄 template-stac-collection-schema.json  # Base Collection schema template
├── 📄 template-kfm-extension-schema.json    # KFM interaction-sphere extension schema template
├── 📄 template-care-extension-schema.json   # CARE cultural safety extension template
└── 📄 template-dcat-crosswalk.json          # DCAT ↔ STAC mapping template
~~~

These templates mirror the pattern used by artifact-inventory STAC schemas, adapted for cultural-landscape / interaction-sphere semantics.

---

## 📦 Template — STAC Item Schema (Minimal)

`template-stac-item-schema.json` is the starting point for validating interaction-sphere STAC Items.

~~~json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "KFM Interaction Sphere — STAC Item Schema Template",
  "type": "object",

  "required": ["id", "stac_version", "type", "bbox", "geometry", "properties", "assets"],

  "properties": {
    "stac_version": { "const": "1.0.0" },
    "type": { "const": "Feature" },

    "id": {
      "type": "string",
      "description": "Interaction-sphere STAC Item ID (matches filename)."
    },

    "bbox": {
      "type": "array",
      "minItems": 4,
      "maxItems": 4,
      "items": { "type": "number" },
      "description": "Generalized bounding box; never site-level precision."
    },

    "geometry": {
      "type": "object",
      "properties": {
        "type": { "enum": ["Polygon", "MultiPolygon"] }
      },
      "required": ["type"],
      "description": "Generalized polygons/multipolygons only; H3 or simplified geometries."
    },

    "properties": {
      "type": "object",
      "description": "STAC properties including kfm:* and care:* extensions."
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
            "roles": {
              "type": "array",
              "items": { "type": "string" }
            }
          }
        }
      }
    }
  }
}
~~~

Schema authors should extend this with `kfm:*` and `care:*` constraints via the extension templates below.

---

## 📦 Template — STAC Collection Schema (Minimal)

`template-stac-collection-schema.json` provides the base for interaction-sphere Collections.

~~~json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "KFM Interaction Sphere — STAC Collection Schema Template",
  "type": "object",

  "required": ["id", "stac_version", "type", "extent", "license"],

  "properties": {
    "stac_version": { "const": "1.0.0" },
    "type": { "const": "Collection" },

    "id": {
      "type": "string",
      "description": "STAC Collection ID (e.g., interaction-spheres, great-bend-aspect)."
    },

    "description": {
      "type": "string",
      "description": "Human-readable summary of the interaction-sphere grouping."
    },

    "license": {
      "type": "string",
      "description": "SPDX license identifier (e.g., CC-BY-4.0)."
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

Extend with `kfm:*` and `care:*` fields at the Collection level for region types, sensitivity, and sovereignty.

---

## 📦 Template — KFM Interaction-Sphere Extension Schema

`template-kfm-extension-schema.json` is used for `kfm:*` fields in interaction-sphere Items and Collections.

~~~json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "KFM Interaction Sphere Extension Schema Template",
  "type": "object",

  "properties": {
    "kfm:domain": {
      "type": "string",
      "const": "archaeology-cultural-landscapes",
      "description": "Domain identifier for cultural-landscape interaction spheres."
    },
    "kfm:region_type": {
      "type": "string",
      "enum": ["interaction_sphere", "exchange_zone", "contact_region"],
      "description": "High-level classification for this interaction region."
    },
    "kfm:interaction_type": {
      "type": "string",
      "enum": ["influence_sphere", "contact_zone", "exchange_corridor", "other"],
      "description": "Interaction type; aligns with controlled vocabularies."
    },
    "kfm:culture_phase": {
      "type": "string",
      "description": "Cultural-phase label associated with this sphere."
    },
    "kfm:generalization": {
      "type": "string",
      "description": "Spatial generalization (e.g., H3-r7, H3-r8, simplified-polygon)."
    },
    "kfm:review_cycle": {
      "type": "string",
      "description": "Review cadence (e.g., Biannual)."
    },
    "kfm:provenance": {
      "type": "string",
      "description": "Path to PROV-O lineage JSON for this dataset."
    }
  }
}
~~~

Adjust field names/types to align with the shared KFM cultural-landscape extension as needed.

---

## 📦 Template — CARE Sensitivity Schema

`template-care-extension-schema.json` defines CARE-related fields.

~~~json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "CARE Sensitivity Extension Template — Interaction Spheres",
  "type": "object",

  "properties": {
    "care:sensitivity": {
      "type": "string",
      "enum": ["general", "generalized", "restricted-generalized"],
      "description": "Cultural sensitivity level; 'restricted' is not allowed in public catalog."
    },
    "care:review": {
      "type": "string",
      "enum": ["faircare", "tribal", "none-required"],
      "description": "Cultural review authority; protohistoric/ethnohistoric spheres commonly require 'tribal'."
    },
    "care:notes": {
      "type": "string",
      "description": "Explanation of cultural safety and sovereignty decisions."
    },
    "care:visibility_rules": {
      "type": "string",
      "enum": ["h3-only", "no-exact-points"],
      "description": "Constraints on geometry visibility in public outputs."
    },
    "care:consent_status": {
      "type": "string",
      "enum": ["approved", "conditional", "not-approved", "not-applicable"],
      "description": "Consent status as per sovereignty and CARE governance."
    }
  }
}
~~~

This template should be kept aligned with global CARE schema patterns used elsewhere in KFM.

---

## 📦 Template — DCAT Crosswalk Schema

`template-dcat-crosswalk.json` ensures DCAT ↔ STAC alignment.

~~~json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "DCAT–STAC Crosswalk Template — Interaction Spheres",
  "type": "object",

  "properties": {
    "dct:title": {
      "type": "string",
      "description": "DCAT dataset title; must align with STAC id/description."
    },
    "dct:license": {
      "type": "string",
      "description": "License string consistent with STAC Collection/Item license."
    },
    "dct:temporal": {
      "type": "string",
      "description": "Temporal coverage; must reflect STAC temporal extent."
    },
    "dcat:distribution": {
      "type": "string",
      "description": "Reference to distribution; maps to STAC assets.data.href."
    },
    "dcat:keyword": {
      "type": "array",
      "items": { "type": "string" },
      "description": "Optional keywords; may mirror STAC keywords."
    }
  }
}
~~~

Extend and constrain further as DCAT/metadata patterns evolve.

---

## 🧪 Validation Workflow for Schema Authors

When creating or modifying schemas based on these templates:

1. **Implement your schema** by copying and adapting the relevant template.  
2. **Validate** the new schema using a Draft 2020-12–compatible validator (for example, `jsonschema`, `ajv`).  
3. **Integrate** the schema into the interaction-sphere STAC validation pipeline:
   - Reference it from `../README.md` and higher-level docs as appropriate.  
   - Add it to CI workflows (for example, `.github/workflows/artifact-stac-validate.yml`).  
4. Ensure:
   - Controlled vocabularies match those specified in the interaction-sphere docs.  
   - CARE constraints align with sovereignty policies and CARE guidelines.  
   - Crosswalks reflect actual usage in metadata and STAC documents.

---

## 🔗 Related Specifications

- `../README.md`  
  – Interaction Sphere STAC Schemas index and description.  
- `../items/README.md`  
  – STAC Items requirements for interaction spheres.  
- `../collections/README.md`  
  – STAC Collections requirements and patterns.  
- `../../metadata/README.md`  
  – DCAT metadata rules for interaction spheres.  
- `../../provenance/README.md`  
  – Provenance and sovereignty review logging.  
- `../../../../../artifact-inventories/stac/schemas/templates/README.md`  
  – Global STAC schema templates used across KFM.

---

## 🕰 Version History

| Version   | Date       | Author                                                   | Summary                                                                 |
|-----------|------------|----------------------------------------------------------|-------------------------------------------------------------------------|
| v11.2.3   | 2025-12-02 | Cultural Landscape WG · Metadata Standards Subcommittee · FAIR+CARE Council | Created interaction-sphere STAC schema templates; aligned with global STAC/CARE patterns and interaction-sphere vocabularies. |
| v11.0.0   | 2025-11-24 | Cultural Landscape WG                                   | Initial scaffolding for interaction-sphere schema templates.           |

---

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
FAIR+CARE · Sovereignty-Governed  
KFM-MDP v11.2.2 · MCP-DL v6.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[⬅ Back to Interaction Sphere STAC Schemas](../README.md)

