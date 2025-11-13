---
title: "🌦️ Kansas Frontier Matrix — Climate Symbol Legend Overview (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/reports/visualization/focus_mode/story_nodes/assets/legends/symbols/climate/README.md"
version: "v10.2.2"
last_updated: "2025-11-12"
review_cycle: "Quarterly / FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../../../../releases/v10.2.0/sbom.spdx.json"
manifest_ref: "../../../../../../../../../releases/v10.2.0/manifest.zip"
telemetry_ref: "../../../../../../../../../releases/v10.2.0/focus-telemetry.json"
telemetry_schema: "../../../../../../../../../schemas/telemetry/reports-visualization-climate-symbols-v1.json"
governance_ref: "../../../../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 🌦️ **Kansas Frontier Matrix — Climate Symbol Legend Overview**  
`docs/reports/visualization/focus_mode/story_nodes/assets/legends/symbols/climate/README.md`

**Purpose:**  
Provide the official overview of **climate-related legend symbols** used in Focus Mode, Story Nodes, and geospatial visualization layers across the Kansas Frontier Matrix (KFM). These symbols represent meteorological patterns, extreme weather indicators, seasonal phenomena, and climate-driven environmental changes. All definitions follow FAIR+CARE, STAC/DCAT standards, and the Platinum README Documentation Framework.

![Docs · MCP](https://img.shields.io/badge/Docs-MCP_v6.3-blue)
![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Certified-orange)
![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-green)
![Status: Stable](https://img.shields.io/badge/Status-Stable-success)

</div>

---

## 📘 Overview

The **Climate Symbol Legend** standardizes all climate-related visual symbols used across KFM’s visualization stack.  
These symbols inform:

- 🌩️ Weather and storm-related Story Nodes  
- 🌡️ Climate-change timelines  
- 📈 Environmental trend modeling overlays  
- 🗺️ MapLibre/3D globe visualizations  
- 🧠 Focus Mode predictive insights  

All symbols must align with KFM metadata and visualization rules to ensure consistent rendering, ethics, and interpretability.

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
                climate/
                  README.md                  ← (this file)
                  metadata/
                    field_definitions.md
                    examples/
                      single_symbol.json
                      symbol_catalog.csv
                      stac_item_example.json


⸻

🧱 Purpose of Climate Legend Symbols

Climate symbols in KFM represent:
	•	Weather conditions (fog, hail, windstorm, thunderstorm, drought index, heatwaves)
	•	Climate anomalies (ENSO impacts, unusual temperature deviation, precipitation deficits)
	•	Seasonal transitions (first freeze, leaf-out, high fire-risk days)
	•	Impact indicators (crop stress, wildfire risk, flood probability, soil moisture deficit)

These symbols allow the KFM interface to communicate climate context quickly and consistently across spatial and temporal layers.

⸻

🧩 Symbol Usage Across KFM

🌐 Focus Mode

Climate symbols attach to:
	•	Event Story Nodes (e.g., “The 1936 Heatwave”)
	•	Environmental modifiers
	•	Location-based climate summaries

Focus Mode uses these symbols to generate entity-centric climate narratives.

🧠 Story Nodes

Climate symbols appear in:
	•	Narrative timelines
	•	Map overlays
	•	Cause-effect relationship diagrams
	•	Historical climate reconstructions

🛰 STAC Integration

Climate symbols appear in:
	•	Legend assets within STAC Items
	•	Temperature raster metadata
	•	Precipitation anomaly layers
	•	Fire-risk COG collections

KFM uses STAC roles such as ["legend"], ["qa"], or ["metadata"] to connect symbols to assets.

⸻

🧾 Examples of Climate Symbol Types

Symbol	Meaning	Context
☀️	Clear sky / high-sun period	Summer extremes, drought episodes
🌧️	Rain event	Storm nodes, precipitation records
⛈️	Severe storm	Tornado-era Story Nodes, early-warning indicators
🌡️	Heat anomaly	Heatwave clusters in timelines
❄️	Freeze event	First freeze maps, crop-kill analysis
💨	High wind	Dust Bowl narratives, windstorm impact layers
🔥	Fire risk	Flint Hills fire ecology overlays


⸻

🧬 Metadata Standardization

Each climate symbol must conform to the Climate Field Definitions Schema located at:

metadata/field_definitions.md

This schema includes:
	•	Semantic fields
	•	Cartographic styling fields
	•	Sensitivity and ethical fields
	•	Provenance and review tracking
	•	Linkage to datasets, STAC Items, Story Nodes, and Focus Mode summaries

⸻

🧮 Integration Pipeline

Climate symbol data is:
	1.	Extracted from environmental, meteorological, and reanalysis datasets
	2.	Normalized via ETL pipelines (spaCy NER, OCR for historic meteorology logs, NOAA/Kansas Mesonet data)
	3.	Ingested into the Neo4j Knowledge Graph
	4.	Published into STAC/DCAT catalogs with legend assets
	5.	Rendered by MapLibre/KFM UI with consistent styling rules
	6.	Linked to Story Nodes for temporal-spatial climate context

⸻

📦 Examples Included

Located in metadata/examples/:
	•	single_symbol.json — one climate symbol entry
	•	symbol_catalog.csv — full catalog of climate symbols
	•	stac_item_example.json — STAC Item referencing climate legend assets

⸻

🧯 Validation Rules
	•	All YAML front-matter in symbol files must conform to KFM docs-lint and MCP schemas
	•	Climate symbols must use valid #RRGGBB hex colors
	•	Sensitivity flags must follow FAIR+CARE rules
	•	STAC legend links must resolve
	•	Story Node IDs must reference existing nodes

⸻

🕰️ Version History

Version	Date	Author	Summary
v10.2.2	2025-11-12	KFM AI Assistant	Initial creation of Climate Symbol Legend Overview following strict KFM Markdown standards.

