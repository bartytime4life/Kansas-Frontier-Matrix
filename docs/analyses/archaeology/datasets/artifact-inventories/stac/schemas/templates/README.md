---
title: "🧩 Kansas Frontier Matrix — Artifact STAC Schema Templates (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/datasets/artifact-inventories/stac/schemas/templates/README.md"
description: "Template library for JSON Schemas that validate KFM v11 artifact-inventory STAC Items and Collections, including KFM and CARE extensions."
version: "v11.2.3"
last_updated: "2025-12-02"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Biannual · Archaeology Working Group · FAIR+CARE Council · Metadata Standards Subcommittee"
content_stability: "stable"
status: "Active / Enforced"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-version-hash>"
doc_uuid: "urn:kfm:doc:archaeology-artifact-stac-schema-templates-v11.2.3"
doc_kind: "Schema Template Library"
intent: "artifact-inventory-stac-schema-templates"
semantic_document_id: "kfm-doc-archaeology-artifact-stac-schema-templates-v11.2.3"
category: "Analyses · Archaeology · STAC Schemas · Templates"

sbom_ref: "../../../../../../../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../../../../../../../releases/v11.2.3/manifest.zip"
telemetry_ref: "../../../../../../../../releases/v11.2.3/focus-telemetry.json"
telemetry_schema: "../../../../../../../../schemas/telemetry/archaeology-artifact-stac-schema-templates-v1.json"
energy_schema: "../../../../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../../../../schemas/telemetry/carbon-gco2e-v1.json"

governance_ref: "../../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

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

data_steward: "Archaeology Working Group · Metadata Standards Subcommittee"
provenance_chain:
  - "docs/analyses/archaeology/datasets/artifact-inventories/stac/schemas/templates/README.md@v10.4.0"
provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: true
---

# 🧩 Kansas Frontier Matrix — Artifact STAC Schema Templates (v11)

`docs/analyses/archaeology/datasets/artifact-inventories/stac/schemas/templates/README.md`

**Purpose**  
Provide **schema templates** for building new STAC Item and STAC Collection JSON Schemas for artifact-inventory datasets in the Kansas Frontier Matrix (KFM).

These templates ensure any new schemas remain aligned with:

- STAC 1.0 core  
- Projection extension (`proj`)  
- Scientific extension (`sci`)  
- Versioning extension (`version`)  
- Checksum extension (`checksum`)  
- KFM archaeology extension (`kfm:*`)  
- CARE cultural safety extension (`care:*`)  
- DCAT 3.0 crosswalk requirements  
- MCP-DL v6.3 documentation-first standards  

Templates in this directory are intended to be **copied, adapted, and extended** when designing new validators for artifact-related STAC metadata.

---

## 📘 Overview

This directory provides:

- Starter templates for new **STAC Item** schemas  
- Starter templates for new **STAC Collection** schemas  
- Templates for **KFM archaeology extension** schemas  
- Templates for **CARE sensitivity** schemas  
- Templates for **DCAT ↔ STAC crosswalk** schemas  
- A consistent baseline for integrating new schemas into KFM’s CI validation workflows  

All templates follow **JSON Schema Draft 2020-12**.

---

## 🗂️ Directory Layout

~~~text
docs/analyses/archaeology/datasets/artifact-inventories/stac/schemas/templates/
├── 📄 README.md                                 # This file
├── 📄 template-stac-item-schema.json            # Base STAC Item schema template
├── 📄 template-stac-collection-schema.json      # Base STAC Collection schema template
├── 📄 template-kfm-extension-schema.json        # KFM archaeology extension template
├── 📄 template-care-extension-schema.json       # CARE cultural safety extension template
├── 📄 template-dcat-crosswalk.json              # STAC ↔ DCAT mapping template
└── 📂 annotated/                                # Fully annotated versions of each template
~~~

This layout is **normative** for STAC schema templates.

---

## 📦 Template — STAC Item Schema (Minimal)

`template-stac-item-schema.json` is a minimal starting point for Item schemas.

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

Schema authors should extend this with `kfm:*`, `care:*`, and other extension fields as needed.

---

## 📦 Template — STAC Collection Schema (Minimal)

`template-stac-collection-schema.json` is a minimal Collection schema starting point.

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
      "description": "SPDX license identifier (for example, CC-BY-4.0 for KFM)."
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

Extend this template with `kfm:*` Collection fields (such as `kfm:material_class`) and `care:*` fields.

---

## 📦 Template — KFM Archaeology Extension Schema

`template-kfm-extension-schema.json` provides a baseline for KFM-specific fields.

~~~json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "KFM Archaeology Extension Schema Template",
  "type": "object",

  "properties": {
    "kfm:phase": {
      "type": "string",
      "description": "Cultural-phase classification."
    },
    "kfm:material_class": {
      "enum": ["lithic", "ceramic", "metal", "faunal", "all"],
      "description": "Artifact material class."
    },
    "kfm:datatype": {
      "const": "artifact-inventory",
      "description": "Dataset type for artifact inventories."
    },
    "kfm:source": {
      "type": "string",
      "description": "Source institution or repository."
    },
    "kfm:provenance": {
      "type": "string",
      "description": "Path or identifier for PROV-O lineage record."
    },
    "kfm:review_cycle": {
      "type": "string",
      "description": "Review cadence (for example, Biannual)."
    }
  }
}
~~~

Use this template to design more specific extension schemas when the domain expands.

---

## 📦 Template — CARE Sensitivity Schema

`template-care-extension-schema.json` covers CARE fields.

~~~json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "CARE Sensitivity Extension Template",
  "type": "object",

  "properties": {
    "care:sensitivity": {
      "enum": ["general", "generalized", "restricted-generalized"],
      "description": "Cultural sensitivity classification for this record."
    },
    "care:review": {
      "enum": ["faircare", "tribal", "none-required"],
      "description": "Indicates which body performed cultural review."
    },
    "care:notes": {
      "type": "string",
      "description": "Narrative justification for sensitivity and review decisions."
    },
    "care:visibility_rules": {
      "enum": ["h3-only", "no-exact-points"],
      "description": "Optional rules for how much spatial detail can be exposed."
    }
  }
}
~~~

Adapt this template as CARE policies evolve, but preserve alignment with KFM governance.

---

## 📦 Template — DCAT Crosswalk Schema

`template-dcat-crosswalk.json` helps validate DCAT ↔ STAC alignment.

~~~json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "DCAT–STAC Crosswalk Template",
  "type": "object",

  "properties": {
    "dct:title": {
      "type": "string",
      "description": "DCAT dataset title."
    },
    "dct:license": {
      "type": "string",
      "description": "License identifier aligned with STAC license."
    },
    "dct:temporal": {
      "type": "string",
      "description": "Temporal coverage description or encoded value."
    },
    "dcat:distribution": {
      "type": "string",
      "description": "Reference to primary distribution or asset."
    },
    "dcat:keyword": {
      "type": "array",
      "items": { "type": "string" },
      "description": "Keywords associated with this dataset."
    }
  }
}
~~~

Use and extend this template when building full crosswalk schemas for specific artifact domains.

---

## 🧪 Validation Workflow

New schemas based on these templates should be validated using:

- Local JSON Schema tooling (for example, `jsonschema`, `ajv`) with Draft 2020-12.  
- KFM CI validation flows (for example, `artifact-stac-validate.yml`) once integrated.  

After validation:

- Register schemas in the appropriate CI workflows.  
- Reference them in higher-level documentation (for example, STAC Items / Collections README).  

---

## 🧠 Tips for Schema Authors

- Always start from these templates rather than writing schemas from scratch.  
- Keep schemas strict to prevent malformed metadata from entering KFM.  
- Use controlled vocabularies wherever possible (phase lists, material classes, review cycles).  
- Make cultural-safety constraints (`care:*`) explicit in schemas.  
- Enforce H3-based generalization indirectly (for example, via description and value constraints) and directly where feasible.  
- Add `description` fields generously to support documentation-first workflows and future tooling.  

---

## 🕰 Version History

| Version   | Date       | Author                                       | Summary                                                                 |
|-----------|------------|----------------------------------------------|-------------------------------------------------------------------------|
| v11.2.3   | 2025-12-02 | Archaeology WG · Metadata Standards Subcommittee | Updated schema templates for KFM v11.2.3; added energy/carbon telemetry references and clarified CARE/sovereignty alignment. |
| v10.4.0   | 2025-11-17 | Archaeology WG · FAIR+CARE Council          | Added schema templates for artifact inventories; included KFM & CARE extensions and DCAT crosswalk scaffolds. |
| v10.0.0   | 2025-11-10 | Artifact Metadata Team                       | Initial directory and template placeholders.                            |

---

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
FAIR+CARE · Sovereignty-Governed  
KFM-MDP v11.2.2 · MCP-DL v6.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[⬅ Back to Schema Documentation](../README.md)