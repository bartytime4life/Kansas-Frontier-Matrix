---
title: "🌦️ KFM v11.2.2 — Climate Story Node Examples"
path: "docs/story-nodes/domains/climate/examples/README.md"
version: "v11.2.2"
last_updated: "2025-11-30"
review_cycle: "Annual · Climate Systems Board · FAIR+CARE Council"

commit_sha: "<latest-commit>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

doc_uuid: "urn:kfm:storynodes:climate:examples:v11.2.2"
semantic_document_id: "kfm-storynodes-climate-examples"
event_source_id: "ledger:storynodes/climate/examples"
immutability_status: "version-pinned"

sbom_ref: "../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../releases/v11.2.2/storynode-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/storynodes-v11.json"

governance_ref: "../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"

status: "Active / Enforced"
doc_kind: "Example Collection"
intent: "kfm-climate-storynode-examples"
lifecycle_stage: "stable"

fair_category: "F1-A2-I2-R2"
care_label: "Environmental"
classification: "Public"
jurisdiction: "Kansas / United States"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"

ttl_policy: "36 months"
sunset_policy: "Superseded by v12 climate example set"
---

<div align="center">

# 🌦️ **Climate Story Node Examples (KFM v11)**  
### *Severe Weather · Heatwaves · Drought · Anomalies · Model Insights*  

`docs/story-nodes/domains/climate/examples/README.md`

**Purpose**  
Provide **public-safe**, **scientifically rigorous**, and **schema-valid**  
example Story Nodes illustrating correct structure, spacetime modeling,  
relations, provenance, and STAC/DCAT dataset integration for the climate domain.

</div>

---

## 🗂️ Directory Layout

~~~text
docs/story-nodes/domains/climate/examples/
├── 📄 README.md                           # This file
├── 🌪️ hrrr-tornado-outbreak.json          # Severe weather example
├── 🌡️ heatwave-2022-kansas.json           # Regional heatwave/climate anomaly
└── 📂 ...                                  # Additional examples
~~~

All examples in this directory are:

- **public-safe**
- **generalized**
- **scientifically accurate**
- **schema-validated**
- **STAC/DCAT/provenance-complete**
- **Focus Mode v3 compatible**

---

## 📘 What These Examples Demonstrate

Each example Story Node illustrates:

- Correct **spacetime** modeling  
  - GeoJSON polygons / regions  
  - time intervals with precision (`hour`, `day`, `month`)

- Clear separation of:  
  - **observations** (NEXRAD, ERA5, GOES, HRRR)  
  - **model outputs**  
  - **interpretation**  
  - **uncertainty**

- Proper **scientific terminology** (CF conventions)

- Valid links to:  
  - **STAC rasters** (HRRR, GOES, NEXRAD composite)  
  - **DCAT datasets**  
  - **PROV-O lineage entries**  

- Climate-specific **graph relations**, including:  
  - `about` (main climate event)  
  - `references` (NOAA reports, datasets)  
  - `derived-from` (models, reanalysis)  
  - `analog-of` (historical analog events)

---

## 🎯 Example Categories Included

### 🌪️ Severe Weather
Tornado outbreaks, derechos, high-wind episodes, supercell days.

### 🌡️ Temperature Extremes
Heatwaves, cold spells, arctic intrusions.

### 💧 Hydrologic/Climate Links
Drought, flash flooding precursors, precipitation anomalies.

### ☁️ Satellite & Model Driven
GOES visible/IR composites, HRRR smoke/fire-weather layers, ERA5 anomalies.

### 📈 Long-Term Trends
Multi-decadal temperature/precipitation trend summaries.

---

## 🚫 What Will Never Appear Here

- Personal data  
- Sensitive infrastructure details  
- Hinted tornado track coordinates that could endanger privacy  
- Unlicensed or proprietary model data  
- Exaggerated or speculative climate attribution claims  
- Political or normative statements  

All examples follow **scientific neutrality** and **public safety** standards.

---

## 🧪 Validation Requirements

All example Story Nodes must:

- Validate against `story-node.schema.json`  
- Use correct **CF units** and **climate variables**  
- Include STAC/DCAT metadata  
- Have complete PROV-O lineage  
- Pass climate ethics & attribution checks  
- Use only approved relations  
- Include geometry that is **valid GeoJSON** and **public-safe**  
- Avoid speculation or unsupported causal claims  

---

## 🕰️ Version History

| Version | Date       | Summary                                                        |
|--------:|------------|----------------------------------------------------------------|
| v11.2.2 | 2025-11-30 | Initial governed climate example set; aligned with templates. |
| v11.2.1 | 2025-11-29 | Added tornado + heatwave draft examples (generalized).        |

---

<div align="center">

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
[📚 Docs Home](../../../../README.md) · [📏 Standards Index](../../../standards/README.md) · [🛡 Governance Charter](../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

