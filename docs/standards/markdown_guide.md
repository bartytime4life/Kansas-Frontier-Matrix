---
title: "🏺 Kansas Frontier Matrix — Archaeological Symbol Legend Metadata Field Definitions (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/reports/visualization/focus_mode/story_nodes/assets/legends/symbols/archaeological/metadata/field_definitions.md"
version: "v10.4.2"
last_updated: "2025-11-16"
review_cycle: "Quarterly · FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../../../../../releases/v10.4.2/sbom.spdx.json"
manifest_ref: "../../../../../../../../../../releases/v10.4.2/manifest.zip"
telemetry_ref: "../../../../../../../../../../releases/v10.4.2/focus-telemetry.json"
telemetry_schema: "../../../../../../../../../../schemas/telemetry/reports-visualization-archaeological-legends-v2.json"
governance_ref: "../../../../../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4.2"
status: "Active / Enforced"
doc_kind: "Standard"
intent: "archaeological-symbol-metadata"
fair_category: "F1-A1-I1-R1"
care_label: "C2-A3-R2-E2"
sensitivity_level: "High (cultural heritage)"
public_exposure_risk: "Medium"
machine_extractable: true
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"
semantic_document_id: "kfm-doc-archaeological-symbol-field-definitions"
doc_uuid: "urn:kfm:doc:arch-symbol-field-defs-v10.4.2"
---

<div align="center">

# 🏺 **Kansas Frontier Matrix — Archaeological Symbol Legend Metadata Field Definitions**  
`docs/reports/visualization/focus_mode/story_nodes/assets/legends/symbols/archaeological/metadata/field_definitions.md`

**Purpose**  
Define the **canonical, version-controlled metadata schema** for archaeological legend symbols used by **Focus Mode**, **Story Nodes**, and **map visualizations** in the KFM stack.  
This ensures consistent semantics, cartographic behavior, and FAIR+CARE governance across STAC/DCAT catalogs, MapLibre styles, and the Neo4j knowledge graph.

</div>

---

# 📘 Overview

This standard specifies **field definitions** for archaeological symbol legends used in:

- 🧠 **Focus Mode** entity-centric views  
- 🧩 **Story Nodes** & narrative timelines  
- 🗺️ **MapLibre** and other map layers  
- 🛰️ **STAC 1.0 / DCAT 3.0** metadata and legends  

Each symbol record controls:

- Archaeological **semantics** (feature class, period, culture, certainty)  
- **Cartographic styling** (icon, color, scale, opacity)  
- **Ethical & access controls** (sensitivity, CARE notes, access tiers)  
- **Provenance & linkage** (datasets, Story Nodes, STAC Items, review metadata)  

All downstream symbol catalogs (JSON, CSV), map styles, and graph nodes MUST map back to these fields.

---

# 🗂️ Directory Layout

~~~text
docs/
│
└── reports/
    │
    └── visualization/
        │
        └── focus_mode/
            │
            └── story_nodes/
                │
                └── assets/
                    │
                    └── legends/
                        │
                        └── symbols/
                            │
                            └── archaeological/
                                │
                                ├── README.md
                                └── metadata/
                                    │
                                    ├── field_definitions.md      # ← THIS FILE
                                    └── examples/
                                        ├── single_symbol.json
                                        ├── symbol_catalog.csv
                                        └── stac_item_example.json
~~~

> 💡 **Note:** Any new archaeological symbol catalogs or examples MUST live under `metadata/examples/` and reference the fields defined in this document.

---

# 🧱 Schema Overview

The archaeological symbol legend schema is designed to:

- Normalize **archaeological feature types** into a shared vocabulary.  
- Attach **time-period** information compatible with OWL-Time.  
- Capture **cultural affiliations** and **interpretation certainty**.  
- Encode **FAIR+CARE-sensitive controls** (sensitivity, sovereign rights).  
- Provide **cartographic definitions** that can be mapped into:
  - Focus Mode and Story Node UIs  
  - MapLibre styles / sprites  
  - STAC/DCAT legend assets & style references  

Each symbol record corresponds to **one visual symbol** used to represent one or more feature codes across upstream datasets.

---

# 🧾 Field Definition Table

| #  | Field Name             | Type       | Req | Description                                                                              | Example                                                      |
|----|------------------------|------------|:--:|------------------------------------------------------------------------------------------|--------------------------------------------------------------|
| 1  | `symbol_id`            | string     | ✅  | Stable, unique ID for the symbol (UUID or namespaced slug).                             | `arch_sym:pit_house_v1`                                      |
| 2  | `label`                | string     | ✅  | Short human label shown in legends and UI.                                              | `Pit house (probable)`                                       |
| 3  | `description`          | string     | ✅  | Longer explanation of the feature represented by this symbol.                           | `Subsurface pit structure interpreted as domestic dwelling.` |
| 4  | `geometry_type`        | enum       | ✅  | Geometry type: `Point`, `LineString`, `Polygon`, `MultiPoint`, etc.                     | `Point`                                                      |
| 5  | `feature_class`        | enum       | ✅  | High-level class: `settlement`, `burial`, `earthwork`, `ritual`, `artifact_cluster`, etc.| `settlement`                                                |
| 6  | `subtype`              | string     | ⬜  | Optional refinement within `feature_class`.                                             | `domestic_structure`                                         |
| 7  | `period_label`         | string     | ✅  | Human-readable cultural/chronological period.                                           | `Great Bend aspect (c. 1450–1700 CE)`                        |
| 8  | `period_start`         | date       | ⬜  | ISO 8601 start date of interpreted period.                                              | `1450-01-01`                                                 |
| 9  | `period_end`           | date       | ⬜  | ISO 8601 end date of interpreted period.                                                | `1700-12-31`                                                 |
| 10 | `culture_label`        | string     | ⬜  | Culture, community, or people associated with the feature (where appropriate).          | `Ancestral Wichita`                                          |
| 11 | `certainty`            | enum       | ✅  | Interpretation confidence: `high`, `medium`, `low`, `hypothetical`.                     | `medium`                                                     |
| 12 | `sensitivity`          | enum       | ✅  | Cultural/ethical sensitivity: `public`, `restricted`, `sensitive`, `sacred`.            | `sensitive`                                                  |
| 13 | `care_label`           | string     | ⬜  | CARE / data sovereignty note or handling guidance.                                      | `Consult THPO before any public display.`                    |
| 14 | `access_tier`          | enum       | ✅  | Default display tier: `full`, `generalized`, `hidden`.                                  | `generalized`                                                |
| 15 | `min_scale`            | number     | ⬜  | Minimum map scale denominator (e.g. 1:25k → `25000`) where symbol should render.        | `25000`                                                      |
| 16 | `max_scale`            | number     | ⬜  | Maximum map scale denominator where symbol should render.                               | `150000`                                                     |
| 17 | `fill_color_hex`       | string     | ✅  | Fill color `#RRGGBB` (no alpha).                                                       | `#b5651d`                                                    |
| 18 | `stroke_color_hex`     | string     | ⬜  | Outline color `#RRGGBB`.                                                               | `#3b2a1a`                                                    |
| 19 | `stroke_width_px`      | number     | ⬜  | Stroke width in CSS pixels at reference zoom.                                          | `1.5`                                                        |
| 20 | `opacity`              | number     | ⬜  | Opacity in `0.0`–`1.0`.                                                                | `0.85`                                                       |
| 21 | `icon_href`            | uri        | ⬜  | Path/URL to SVG/PNG icon asset.                                                        | `/assets/icons/arch/pit_house.svg`                           |
| 22 | `icon_role`            | string     | ⬜  | Icon usage role: `legend`, `marker`, `thumbnail`, etc.                                  | `legend`                                                     |
| 23 | `source_dataset_id`    | string     | ✅  | Primary source dataset in KFM’s data catalog.                                           | `kshs_arch_survey_v4`                                        |
| 24 | `source_feature_codes` | array[str] | ⬜  | Upstream feature codes that map to this symbol.                                        | `["PH","pithouse_prob"]`                                    |
| 25 | `stac_item_ids`        | array[str] | ⬜  | STAC Items that use this symbol catalog in `assets.legend`.                             | `["stac:kfm-arch-sites-2025-01"]`                            |
| 26 | `story_node_ids`       | array[str] | ⬜  | Story Node IDs featuring this symbol prominently.                                      | `["story:great_bend_village_cluster"]`                       |
| 27 | `license`              | string     | ✅  | License for symbol definition & icon assets.                                           | `CC-BY 4.0`                                                  |
| 28 | `citation`             | string     | ⬜  | Academic or archival reference.                                                       | `Wedel, W.R. 1959. An Introduction to Kansas Archeology.`    |
| 29 | `created_at`           | datetime   | ✅  | ISO 8601 creation timestamp.                                                          | `2025-10-01T14:33:00Z`                                       |
| 30 | `updated_at`           | datetime   | ✅  | ISO 8601 last-update timestamp.                                                       | `2025-11-10T09:12:45Z`                                       |
| 31 | `created_by`           | string     | ✅  | Curator / account (e.g., GitHub handle).                                              | `@kfm-arch-curator`                                          |
| 32 | `review_status`        | enum       | ✅  | `draft`, `in_review`, `approved`, `deprecated`.                                       | `approved`                                                   |
| 33 | `review_notes`         | string     | ⬜  | Curatorial notes documenting decisions or caveats.                                     | `Location generalized to 1 km grid for protection.`          |

> ⚠️ **Ethics Guardrail:**  
> For `sensitivity = "sacred"` or `"sensitive"`, public map styles MUST NOT default to `access_tier = "full"`. Use `generalized` or `hidden` and follow governance workflows.

---

# 🧠 Story Node & Focus Mode Integration

## Story Nodes

Story Nodes can explicitly reference symbols to make the UI explainable:

```json
{
  "rel": "uses-symbol",
  "target": "arch_sym:pit_house_v1",
  "role": "cartographic-convention"
}
````

Focus Mode can then:

* Highlight where and why this symbol appears
* Show legend entries & CARE notes inline
* Link to provenance in the graph and STAC catalogs

---

# 🛰 STAC/DCAT Integration

A STAC Item describing an archaeological dataset should reference a symbol catalog asset:

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

---

# 🧾 JSON Example (Single Symbol Record)

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

---

# 📑 CSV Header Specification

CSV catalogs MUST use the following header row (order may vary but all required fields must be present):

```text
symbol_id,label,description,geometry_type,feature_class,subtype,period_label,period_start,period_end,culture_label,certainty,sensitivity,care_label,access_tier,min_scale,max_scale,fill_color_hex,stroke_color_hex,stroke_width_px,opacity,icon_href,icon_role,source_dataset_id,source_feature_codes,stac_item_ids,story_node_ids,license,citation,created_at,updated_at,created_by,review_status,review_notes
```

Multi-valued fields (e.g., `source_feature_codes`) should use pipe-delimited strings in CSV (e.g., `PH|pithouse_prob`) and be split in ETL.

---

# ⚙️ Validation & CI Integration

Recommended checks:

* JSON Schema validation for `.json` symbol catalogs.
* CSV header and required-field validation.
* Color format validation for `*_color_hex`.
* Logical governance checks:

  * If `sensitivity` is `sacred` or `sensitive` → enforce `access_tier != "full"` for public catalogs.

Examples of CI workflows:

* `arch-symbols-validate.yml` → runs JSON/CSV schema checks and governance rules.
* `docs-lint.yml` → ensures this file and `README.md` conform to KFM-MDP.

---

# 🕰 Version History

| Version | Date       | Author                    | Summary                                                                                                        |
| ------: | ---------- | ------------------------- | -------------------------------------------------------------------------------------------------------------- |
| v10.4.2 | 2025-11-16 | KFM Documentation Council | Upgraded to KFM-MDP v10.4.2, deep-inset directory layout, Telemetry v2 references, and stricter CARE guidance. |
| v10.2.2 | 2025-11-12 | KFM AI Assistant          | Realigned archaeological symbol field definitions to Markdown standards; added CI guidance and ethics notes.   |
| v10.2.0 | 2025-11-12 | KFM AI Assistant          | Initial schema for archaeological symbol legend metadata.                                                      |

<div align="center">

© 2025 Kansas Frontier Matrix — CC-BY 4.0
Master Coder Protocol v6.3 · FAIR+CARE Certified
Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>
