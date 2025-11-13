````markdown
---
title: "🏺 Kansas Frontier Matrix — Archaeological Symbol Legend Metadata Field Definitions (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/reports/visualization/focus_mode/story_nodes/assets/legends/symbols/archaeological/metadata/field_definitions.md"
version: "v10.2.2"
last_updated: "2025-11-12"
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
Define the **canonical, version-controlled metadata schema** for archaeological legend symbols used by Focus Mode, Story Nodes, and map visualizations in KFM — ensuring consistent semantics, cartography, and FAIR+CARE governance across STAC/DCAT catalogs and the Neo4j knowledge graph.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP_v6.3-blue)](../../../../../../../../docs/README.md)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../../../../../../../LICENSE)
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Certified-orange)](../../../../../../../../docs/standards/faircare.md)
[![Status: Stable](https://img.shields.io/badge/Status-Stable-success)]()

</div>

---

## 📘 Overview

This document specifies the **field definitions** for archaeological symbol legends used in:

- 🧠 **Focus Mode** entity-centric views  
- 🧩 **Story Nodes** and narrative timelines  
- 🗺️ **MapLibre** and other web map layers  
- 🛰️ **STAC 1.0 / DCAT 3.0** metadata and assets  

Each symbol definition controls:

- Archaeological **semantics** (feature class, period, culture, certainty)  
- **Cartographic style** (icon, color, scale ranges, opacity)  
- **Ethics and access** (sensitivity, CARE notes, access tier)  
- **Provenance and linkage** (datasets, Story Nodes, STAC Items, review metadata)  

All downstream implementations (CSV catalogs, JSON symbol sets, graph nodes) **must** map to these fields.

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

> 💡 **Tip:** Any new archaeological symbol catalog or example must live under `metadata/examples/` and reference the fields in this document. CI checks assume this layout.

---

## 🧱 Schema Overview

The archaeological symbol legend schema is designed to:

* Normalize **archaeological feature types** into a shared vocabulary.
* Attach **time-period information** compatible with OWL-Time.
* Capture **cultural affiliations** and **interpretation certainty**.
* Encode **FAIR+CARE-sensitive controls** to protect sites.
* Provide **cartographic definitions** that can be injected into:

  * Focus Mode styling engines
  * Story Node map panes
  * STAC legend assets and map styles

Each symbol record corresponds to **one visual symbol** used to represent one or more feature codes in upstream datasets.

---

## 🧩 Core Metadata Fields

### 🧾 Field Definition Table

| #  | Field Name             | Type       | Req | Description                                                                              | Example                                                      |
| -- | ---------------------- | ---------- | :-: | ---------------------------------------------------------------------------------------- | ------------------------------------------------------------ |
| 1  | `symbol_id`            | string     |  ✅  | Stable, unique ID for the symbol (UUID or scoped slug).                                  | `arch_sym:pit_house_v1`                                      |
| 2  | `label`                | string     |  ✅  | Short human-readable label shown in legends and UI.                                      | `Pit house (probable)`                                       |
| 3  | `description`          | string     |  ✅  | Longer description of the feature represented by this symbol.                            | `Subsurface pit structure interpreted as domestic dwelling.` |
| 4  | `geometry_type`        | enum       |  ✅  | Expected geometry type: `Point`, `LineString`, `Polygon`, `MultiPoint`, etc.             | `Point`                                                      |
| 5  | `feature_class`        | enum       |  ✅  | High-level class e.g. `settlement`, `burial`, `earthwork`, `ritual`, `artifact_cluster`. | `settlement`                                                 |
| 6  | `subtype`              | string     |  ⬜  | Optional refinement within `feature_class`.                                              | `domestic_structure`                                         |
| 7  | `period_label`         | string     |  ✅  | Human-readable cultural/chronological period.                                            | `Great Bend aspect (c. 1450–1700 CE)`                        |
| 8  | `period_start`         | date       |  ⬜  | ISO 8601 start date of interpreted period (if known).                                    | `1450-01-01`                                                 |
| 9  | `period_end`           | date       |  ⬜  | ISO 8601 end date of interpreted period (if known).                                      | `1700-12-31`                                                 |
| 10 | `culture_label`        | string     |  ⬜  | Culture, community, or people associated with the feature (where appropriate).           | `Ancestral Wichita`                                          |
| 11 | `certainty`            | enum       |  ✅  | Interpretation confidence: `high`, `medium`, `low`, `hypothetical`.                      | `medium`                                                     |
| 12 | `sensitivity`          | enum       |  ✅  | Cultural/ethical sensitivity: `public`, `restricted`, `sensitive`, `sacred`.             | `sensitive`                                                  |
| 13 | `care_label`           | string     |  ⬜  | CARE / Indigenous data sovereignty note or handling guidance.                            | `Consult THPO before any public display.`                    |
| 14 | `access_tier`          | enum       |  ✅  | Default public display tier: `full`, `generalized`, `hidden`.                            | `generalized`                                                |
| 15 | `min_scale`            | number     |  ⬜  | Minimum map scale denominator where symbol should render (e.g., 1:25k → `25000`).        | `25000`                                                      |
| 16 | `max_scale`            | number     |  ⬜  | Maximum map scale denominator where symbol should render.                                | `150000`                                                     |
| 17 | `fill_color_hex`       | string     |  ✅  | Symbol fill color as `#RRGGBB` (no alpha).                                               | `#b5651d`                                                    |
| 18 | `stroke_color_hex`     | string     |  ⬜  | Outline color as `#RRGGBB`.                                                              | `#3b2a1a`                                                    |
| 19 | `stroke_width_px`      | number     |  ⬜  | Stroke width in CSS pixels at reference zoom.                                            | `1.5`                                                        |
| 20 | `opacity`              | number     |  ⬜  | Symbol opacity in range `0.0`–`1.0`.                                                     | `0.85`                                                       |
| 21 | `icon_href`            | uri        |  ⬜  | Relative or absolute URI to SVG/PNG icon asset.                                          | `/assets/icons/arch/pit_house.svg`                           |
| 22 | `icon_role`            | string     |  ⬜  | Icon usage role: `legend`, `map-marker`, `thumbnail`, etc.                               | `legend`                                                     |
| 23 | `source_dataset_id`    | string     |  ✅  | Primary source dataset identifier in the KFM data catalog.                               | `kshs_arch_survey_v4`                                        |
| 24 | `source_feature_codes` | array[str] |  ⬜  | Upstream feature codes that map to this symbol.                                          | `["PH","pithouse_prob"]`                                     |
| 25 | `stac_item_ids`        | array[str] |  ⬜  | IDs of STAC Items that reference this symbol or its legend catalog.                      | `["stac:kfm-arch-sites-2025-01"]`                            |
| 26 | `story_node_ids`       | array[str] |  ⬜  | IDs of Story Nodes in which this symbol is prominently used.                             | `["story:great_bend_village_cluster"]`                       |
| 27 | `license`              | string     |  ✅  | License covering the symbol definition and icon assets.                                  | `CC-BY 4.0`                                                  |
| 28 | `citation`             | string     |  ⬜  | Human-readable academic or archival reference.                                           | `Wedel, W.R. 1959. An Introduction to Kansas Archeology.`    |
| 29 | `created_at`           | datetime   |  ✅  | ISO 8601 timestamp when the symbol record was created.                                   | `2025-10-01T14:33:00Z`                                       |
| 30 | `updated_at`           | datetime   |  ✅  | ISO 8601 timestamp when the symbol record was last modified.                             | `2025-11-10T09:12:45Z`                                       |
| 31 | `created_by`           | string     |  ✅  | Curator or process ID (e.g., GitHub user, automation account).                           | `@kfm-arch-curator`                                          |
| 32 | `review_status`        | enum       |  ✅  | Review state: `draft`, `in_review`, `approved`, `deprecated`.                            | `approved`                                                   |
| 33 | `review_notes`         | string     |  ⬜  | Curatorial notes documenting decisions, caveats, or changes.                             | `Location generalized to 1 km grid for protection.`          |

> ⚠️ **Ethics Guardrail:** Any symbol with `sensitivity = "sacred"` or `sensitivity = "sensitive"` must not default to `access_tier = "full"` in public deployments. Use `generalized` or `hidden` and follow governance workflows for exceptions.

---

## 🧩 Story Node & STAC Integration

### 🧠 Story Node Usage

Within a **Story Node**, archaeological symbols can be referenced via:

* `narrative.media[*].href` → uses `icon_href` for legend thumbnails.
* `relations[*]` → explicit `uses-symbol` links to `symbol_id`.
* Map panels that render features using styling derived from these definitions.

Example relation block in a Story Node:

```json
{
  "rel": "uses-symbol",
  "target": "arch_sym:pit_house_v1",
  "role": "cartographic-convention"
}
```

This allows Focus Mode to explain **why** a feature is styled in a particular way by referencing this legend schema.

### 🛰 STAC Item Usage

A STAC Item describing an archaeological vector layer should reference the symbol catalog as a legend asset:

```json
{
  "type": "Feature",
  "stac_version": "1.0.0",
  "id": "kfm-arch-pithouses-2025-01",
  "properties": {
    "datetime": "2025-01-01T00:00:00Z",
    "kfm:symbol_catalog_id": "arch_legend_v1"
  },
  "assets": {
    "data": {
      "href": "https://data.kfm.dev/arch/pithouses_2025.geojson",
      "type": "application/geo+json",
      "roles": ["data"]
    },
    "legend": {
      "href": "https://data.kfm.dev/arch/arch_legend_v1.json",
      "type": "application/json",
      "roles": ["legend"],
      "kfm:symbol_ids": [
        "arch_sym:pit_house_v1",
        "arch_sym:burial_mound_v1"
      ]
    }
  }
}
```

> 💡 **Tip:** Treat the legend file itself (`arch_legend_v1.json` or `.csv`) as a versioned STAC asset so it can be indexed, validated, and linked to map styles.

---

## 🧾 JSON & CSV Representations

### 📄 JSON Example (Single Symbol)

```json
{
  "symbol_id": "arch_sym:pit_house_v1",
  "label": "Pit house (probable)",
  "description": "Subsurface pit structure interpreted as domestic dwelling based on artifact scatter and stratigraphy.",
  "geometry_type": "Point",
  "feature_class": "settlement",
  "subtype": "domestic_structure",
  "period_label": "Great Bend aspect (c. 1450–1700 CE)",
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
  "source_feature_codes": ["PH", "pithouse_prob"],
  "stac_item_ids": ["stac:kfm-arch-sites-2025-01"],
  "story_node_ids": ["story:great_bend_village_cluster"],
  "license": "CC-BY 4.0",
  "citation": "Wedel, W.R. 1959. An Introduction to Kansas Archeology.",
  "created_at": "2025-10-01T14:33:00Z",
  "updated_at": "2025-11-10T09:12:45Z",
  "created_by": "@kfm-arch-curator",
  "review_status": "approved",
  "review_notes": "Location generalized to 1 km grid for site protection."
}
```

### 📑 CSV Header (Symbol Catalog)

```text
symbol_id,label,description,geometry_type,feature_class,subtype,period_label,period_start,period_end,culture_label,certainty,sensitivity,care_label,access_tier,min_scale,max_scale,fill_color_hex,stroke_color_hex,stroke_width_px,opacity,icon_href,icon_role,source_dataset_id,source_feature_codes,stac_item_ids,story_node_ids,license,citation,created_at,updated_at,created_by,review_status,review_notes
```

> 🧩 **Multi-valued Fields:** In CSV exports, treat `source_feature_codes`, `stac_item_ids`, and `story_node_ids` as pipe-delimited (`|`) lists and parse them explicitly in ETL pipelines.

---

## 🧯 Validation & CI Integration

### 🧪 Schema Validation

* JSON symbol catalogs must validate against a JSON Schema that implements the field table above.
* CSV symbol catalogs must be checked for:

  * Presence of all required columns.
  * Non-empty values for required fields.

### 🔐 Ethics & Semantics Checks

* `sensitivity` of `sacred` or `sensitive` must not be paired with `access_tier = "full"` in public-facing layers.
* Color fields (`fill_color_hex`, `stroke_color_hex`) must be valid `#RRGGBB` values.
* `certainty = "low"` or `certainty = "hypothetical"` should trigger warnings when used in highly visible public contexts.

### ⚙️ CI Workflows

Recommended make targets and workflows:

* `make docs-validate` for global documentation rules.
* `make validate-arch-symbols` for:

  * JSON Schema validation.
  * CSV header and required-field checks.
  * Optional link checks ensuring referenced `symbol_id`, `story_node_ids`, and `stac_item_ids` exist in catalogs or the graph.

All changes to symbol catalogs should be gated in CI; merges are blocked until validations pass.

---

## 🕰️ Version History

| Version | Date       | Author           | Summary                                                                                                          |
| ------- | ---------- | ---------------- | ---------------------------------------------------------------------------------------------------------------- |
| v10.2.2 | 2025-11-12 | KFM AI Assistant | Realigned archaeological symbol field definitions to KFM markdown guide; tightened ethics notes and CI guidance. |
| v10.2.0 | 2025-11-12 | KFM AI Assistant | Initial creation of archaeological symbol legend metadata field definitions for Focus Mode and Story Nodes.      |

```
```
