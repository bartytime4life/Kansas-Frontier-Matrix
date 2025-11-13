````markdown
---
title: "🏺 Kansas Frontier Matrix — Archaeological Symbol Legend Metadata Field Definitions (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/reports/visualization/focus_mode/story_nodes/assets/legends/symbols/archaeological/metadata/field_definitions.md"
version: "v10.2.0"
date: "2025-11-12"
review_cycle: "Quarterly / FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../../../../../releases/v10.2.0/sbom.spdx.json"
manifest_ref: "../../../../../../../../../../releases/v10.2.0/manifest.zip"
telemetry_ref: "../../../../../../../../../../releases/v10.2.0/focus-telemetry.json"
telemetry_schema: "../../../../../../../../../../schemas/telemetry/reports-visualization-archaeological-legends-v1.json"
governance_ref: "../../../../../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 🏺 **Kansas Frontier Matrix — Archaeological Symbol Legend Metadata Field Definitions**  
`docs/reports/visualization/focus_mode/story_nodes/assets/legends/symbols/archaeological/metadata/field_definitions.md`

**Purpose:**  
Provide the authoritative, version-controlled metadata schema for **archaeological-feature symbol definitions** used within all Focus Mode visualization layers, Story Nodes, cartographic assets, and STAC/DCAT metadata pipelines. Enables strict **FAIR+CARE**, **MCP-DL**, and **KFM v10** compliance.

![Docs · MCP](https://img.shields.io/badge/Docs-MCP--DL%20v6.3-blue)
![Story Nodes](https://img.shields.io/badge/Spec-Story%20Nodes%20v2-9cf)
![STAC 1.0](https://img.shields.io/badge/Metadata-STAC%201.0%20Aligned-4b8bbe)
![FAIR+CARE](https://img.shields.io/badge/Ethics-FAIR+CARE-green)
![MIT License](https://img.shields.io/badge/License-CC--BY%204.0-brightgreen)

</div>

---

## 📁 Directory Layout

```text
docs/
  reports/
    visualization/
      focus_mode/
        story_nodes/
          assets/
            legends/
              symbols/
                archaeological/
                  README.md
                  metadata/
                    field_definitions.md      ← (this file)
                    examples/
                      single_symbol.json
                      symbol_catalog.csv
                      stac_item_example.json
````

---

## 🧱 Schema Overview

This schema defines **how archaeological map symbols are standardized** across the Kansas Frontier Matrix.
Each symbol entry controls:

* 🏺 **Archaeological semantics & feature classes**
* 🗺️ **Map rendering rules & styling**
* 🔐 **FAIR+CARE handling, sensitivity, and access tiers**
* 🧬 **Story Node linkage**
* 🛰️ **STAC 1.0 / DCAT metadata compliance**
* 🔗 **Neo4j knowledge graph relationships (CIDOC-CRM, OWL-Time, GeoSPARQL)**

All symbol definitions must include required fields and pass automated validation.

---

## 📊 Metadata Field Definitions

| #  | Field                  | Type     | Req | Description                                                    | Example                                   |
| -- | ---------------------- | -------- | :-: | -------------------------------------------------------------- | ----------------------------------------- |
| 1  | `symbol_id`            | string   |  ✅  | Stable global ID for this legend symbol.                       | `arch_sym:pit_house_v1`                   |
| 2  | `label`                | string   |  ✅  | Human-friendly name for display.                               | `Pit House (Probable)`                    |
| 3  | `description`          | string   |  ✅  | Archaeological meaning or interpretation.                      | `Subsurface domestic dwelling structure.` |
| 4  | `geometry_type`        | enum     |  ✅  | Expected geometry (`Point`, `LineString`, `Polygon`).          | `Point`                                   |
| 5  | `feature_class`        | enum     |  ✅  | Feature category (`settlement`, `burial`, `earthwork`).        | `settlement`                              |
| 6  | `subtype`              | string   |  ⬜  | Optional refinement.                                           | `domestic_structure`                      |
| 7  | `period_label`         | string   |  ✅  | Human-readable cultural/temporal period.                       | `Great Bend aspect (1450–1700 CE)`        |
| 8  | `period_start`         | date     |  ⬜  | ISO 8601 date.                                                 | `1450-01-01`                              |
| 9  | `period_end`           | date     |  ⬜  | ISO 8601 date.                                                 | `1700-12-31`                              |
| 10 | `culture_label`        | string   |  ⬜  | Cultural affiliation.                                          | `Ancestral Wichita`                       |
| 11 | `certainty`            | enum     |  ✅  | Interpretation confidence.                                     | `medium`                                  |
| 12 | `sensitivity`          | enum     |  ✅  | Ethical status: `public`, `restricted`, `sensitive`, `sacred`. | `sensitive`                               |
| 13 | `care_label`           | string   |  ⬜  | Protocol notes for Indigenous stewardship.                     | `Consult THPO before display.`            |
| 14 | `access_tier`          | enum     |  ✅  | `full`, `generalized`, `hidden`.                               | `generalized`                             |
| 15 | `min_scale`            | number   |  ⬜  | Minimum display scale.                                         | `25000`                                   |
| 16 | `max_scale`            | number   |  ⬜  | Maximum display scale.                                         | `150000`                                  |
| 17 | `fill_color_hex`       | string   |  ✅  | Symbol fill color.                                             | `#b5651d`                                 |
| 18 | `stroke_color_hex`     | string   |  ⬜  | Outline color.                                                 | `#3b2a1a`                                 |
| 19 | `stroke_width_px`      | number   |  ⬜  | Pixel stroke width.                                            | `1.5`                                     |
| 20 | `opacity`              | number   |  ⬜  | 0.0–1.0 opacity.                                               | `0.85`                                    |
| 21 | `icon_href`            | uri      |  ⬜  | Path to SVG/PNG icon.                                          | `/assets/icons/arch/pit_house.svg`        |
| 22 | `icon_role`            | string   |  ⬜  | Usage: `legend`, `map-marker`, etc.                            | `legend`                                  |
| 23 | `source_dataset_id`    | string   |  ✅  | Origin dataset ID.                                             | `kshs_arch_survey_v4`                     |
| 24 | `source_feature_codes` | array    |  ⬜  | Upstream codes mapped to this symbol.                          | `["PH","pithouse_prob"]`                  |
| 25 | `stac_item_ids`        | array    |  ⬜  | Linked STAC Items.                                             | `["stac:kfm-arch-sites-2025-01"]`         |
| 26 | `story_node_ids`       | array    |  ⬜  | Linked Story Nodes.                                            | `["story:great_bend_village_cluster"]`    |
| 27 | `license`              | string   |  ✅  | License identifier.                                            | `CC-BY 4.0`                               |
| 28 | `citation`             | string   |  ⬜  | Scholarly reference.                                           | `Wedel 1959`                              |
| 29 | `created_at`           | datetime |  ✅  | Creation timestamp.                                            | `2025-10-01T14:33:00Z`                    |
| 30 | `updated_at`           | datetime |  ✅  | Last modified timestamp.                                       | `2025-11-10T09:12:45Z`                    |
| 31 | `created_by`           | string   |  ✅  | Curator ID.                                                    | `@kfm-arch-curator`                       |
| 32 | `review_status`        | enum     |  ✅  | `draft`, `in_review`, `approved`, `deprecated`.                | `approved`                                |
| 33 | `review_notes`         | string   |  ⬜  | Curatorial commentary.                                         | `Generalized to 1 km grid.`               |

---

## 🧬 JSON Example

```json
{
  "symbol_id": "arch_sym:pit_house_v1",
  "label": "Pit House (Probable)",
  "description": "Subsurface dwelling feature based on stratigraphy and artifact scatter.",
  "geometry_type": "Point",
  "feature_class": "settlement",
  "subtype": "domestic_structure",
  "period_label": "Great Bend aspect (1450–1700 CE)",
  "period_start": "1450-01-01",
  "period_end": "1700-12-31",
  "culture_label": "Ancestral Wichita",
  "certainty": "medium",
  "sensitivity": "sensitive",
  "care_label": "Consult THPO before any public display.",
  "access_tier": "generalized",
  "min_scale": 25000,
  "max_scale": 150000,
  "fill_color_hex": "#b5651d",
  "stroke_color_hex": "#3b2a1a",
  "stroke_width_px": 1.5,
  "opacity": 0.85,
  "icon_href": "/assets/icons/arch/pit_house.svg",
  "icon_role": "legend",
  "source_dataset_id": "kshs_arch_survey_v4",
  "source_feature_codes": ["PH","pithouse_prob"],
  "stac_item_ids": ["stac:kfm-arch-sites-2025-01"],
  "story_node_ids": ["story:great_bend_village_cluster"],
  "license": "CC-BY 4.0",
  "citation": "Wedel, W.R. 1959. An Introduction to Kansas Archeology.",
  "created_at": "2025-10-01T14:33:00Z",
  "updated_at": "2025-11-10T09:12:45Z",
  "created_by": "@kfm-arch-curator",
  "review_status": "approved",
  "review_notes": "Location generalized to 1 km grid for protection."
}
```

---

## 📑 CSV Header

```text
symbol_id,label,description,geometry_type,feature_class,subtype,period_label,period_start,period_end,culture_label,certainty,sensitivity,care_label,access_tier,min_scale,max_scale,fill_color_hex,stroke_color_hex,stroke_width_px,opacity,icon_href,icon_role,source_dataset_id,source_feature_codes,stac_item_ids,story_node_ids,license,citation,created_at,updated_at,created_by,review_status,review_notes
```

---

## 🧯 Validation Rules

* All required fields must be present.
* `sensitivity = sacred` ⇒ `access_tier` ≠ `full`.
* HEX colors must be valid.
* Story Node & STAC references must resolve.
* CSV multi-value fields must use `|`.
* All symbol catalogs must pass `make docs-validate`.

---

## 📚 Version History

| Version | Date       | Author           | Description                                                                        |
| ------- | ---------- | ---------------- | ---------------------------------------------------------------------------------- |
| v10.2.0 | 2025-11-12 | KFM AI Assistant | Initial MCP/Diamond⁹Ω-compliant schema creation for archaeological symbol legends. |

```
```
