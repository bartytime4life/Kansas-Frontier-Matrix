---
title: "🌦️ KFM v11.2.2 — Climate Story Node Domain (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/story-nodes/domains/climate/README.md"
version: "v11.2.2"
last_updated: "2025-11-30"
review_cycle: "Annual · Climate Systems Board · FAIR+CARE Council"

commit_sha: "<latest-commit>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

doc_uuid: "urn:kfm:storynodes:climate:v11.2.2"
semantic_document_id: "kfm-storynodes-climate-domain"
event_source_id: "ledger:storynodes/climate"
immutability_status: "version-pinned"

sbom_ref: "../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../releases/v11.2.2/storynode-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/storynodes-v11.json"

governance_ref: "../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"

status: "Active / Enforced"
doc_kind: "Domain Specification"
intent: "kfm-climate-storynode-domain"
lifecycle_stage: "stable"

fair_category: "F1-A2-I2-R2"
care_label: "Mixed / Environmental"
classification: "Public"
jurisdiction: "Kansas / United States"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"

ttl_policy: "36 months"
sunset_policy: "Superseded by v12 climate domain rewrite"
---

<div align="center">

# 🌦️ **Climate Story Node Domain (KFM v11)**  
### **Diamond⁹ Ω / Crown∞Ω Ultimate Certified**  
### *Atmosphere · Weather · Climate · Long-Term Trends · Extreme Events*  

`docs/story-nodes/domains/climate/README.md`

**Purpose**  
Define the governed rules for **climate-focused Story Nodes**, ensuring  
scientific accuracy, provenance integrity, standards alignment (CF, STAC, DCAT),  
and Focus Mode v3 compatibility.

</div>

---

## 🗂️ Directory Layout

~~~text
docs/story-nodes/domains/climate/
├── 📄 README.md                               # Climate domain overview (this file)
├── 📁 templates/                               # Authoring templates (MD + JSON)
│   ├── 📝 story-node-climate.md                # Markdown authoring template
│   ├── 🧩 story-node-climate.json              # JSON schema-aligned skeleton
│   └── 🔗 relation-patterns.md                 # Climate graph relation patterns
├── 📁 examples/                                # Curated Story Node examples
│   ├── 🌪️ hrrr-tornado-outbreak.json           # Severe weather example
│   ├── 🌡️ heatwave-2022-kansas.json            # Heatwave/climate anomaly example
│   └── 📂 ...                                   # Additional examples
├── 📘 glossary.md                              # Climate terminology
└── 📁 notes/                                   # Drafts, backlog, ethics review
    ├── 📑 backlog.md                           # Candidate Story Nodes
    └── ⚖️ ethics-checklist.md                  # Environmental/AI ethics checklist
~~~

---

## 📘 Overview

The climate domain supports Story Nodes that explain:

- Local & statewide **weather events**
- **Climate anomalies**, departures, and extremes  
- **Long-term climate trends** (warming, precipitation changes)  
- **Seasonal cycles** & oscillations (ENSO, PDO)  
- Climate model results (HRRR, ERA5, GFS, CMIP6)  
- **Drought**, **heatwaves**, **cold spells**, **flood events**, **wind systems**  
- **Climate impacts** relevant to Kansas: agriculture, hydrology, ecology, hazards  

Climate Story Nodes unify:

- **Spacetime-grounded events**  
- **Observations** (NOAA/NCEI, HRRR, ERA5, radar, satellite)  
- **Scientific interpretation**  
- **Model provenance** (source datasets, parameters, versions)  
- Links into **Focus Mode v3**  
- Strict compliance with **STAC**, **DCAT**, **CF conventions**, **PROV-O**, **GeoSPARQL**, **OWL-Time**

---

## 🧠 Story Node Requirements

### 1. Scientific Rigor

Story Nodes must:

- Distinguish **observations**, **model output**, and **interpretation**
- Include uncertainty ranges where applicable
- Avoid overstating causal claims
- Use standardized climate terminology (glossary-backed)

### 2. Spacetime Rules

**Geometry:**

- Points / polygons for event locations  
- County-level or statewide polygons for large-scale events  
- Raster footprints for satellite/model layers  
- GeoJSON required

**Temporal:**

- Use ISO intervals: `start` + `end`  
- Include `precision` (“hour”, “day”, “month”, “year”)  
- Use `original_label` for meteorological phrasing  
  - e.g., `"June 2022 Heatwave"`  

### 3. Asset & Dataset Linking

Climate Story Nodes may link:

- STAC raster assets (HRRR, NEXRAD, GOES, ERA5, model outputs)
- DCAT dataset entries
- PROV-O lineage records from pipelines

Media and datasets must include:

- license  
- mime type  
- description  
- dataset version  
- spatial/temporal coverage  

### 4. Graph Relations

Examples:

- `about` → tornado outbreak event, heatwave event, drought interval  
- `references` → NOAA reports, HRRR model run, ERA5 reanalysis  
- `derived-from` → pipeline/model outputs  
- `counterpoint` → updates to climate attribution or interpretations  

See: `templates/relation-patterns.md`.

---

## 🧭 Focus Mode Integration

Focus Mode v3 will:

- Zoom to the event’s spatial footprint  
- Align the timeline with:
  - event duration  
  - precursor conditions  
  - aftermath analyses  
- Surface related:
  - datasets  
  - radar/satellite assets  
  - climate anomalies  
  - historical analogs  
  - relevant Story Nodes  
  - hydrology/soil impacts  

Everything must be **data-grounded** and scientifically accurate.  
No speculation. No invented climate causes.

---

## 📦 Metadata & Provenance Requirements

Climate Story Nodes must include:

- **Primary dataset used** (NEXRAD, HRRR, GOES, ERA5)  
- **Model version**, run hour, initialization time  
- **Parameter set** (if AI models used)  
- **Processing pipeline** (LangGraph DAG ID, config, checksum)  
- **Sources**, **citations**, **licensing**  
- **Limitations** of data or models  

All climate nodes must validate against:

- `story-node.schema.json`
- STAC asset schemas (if applicable)
- KFM provenance core (`prov:Entity`, `prov:Activity`)

---

## 🧪 Validation

CI checks include:

- Story Node schema  
- GeoJSON validity  
- Temporal precision correctness  
- Dataset link checks (STAC/DCAT)  
- Units, CRS, CF compliance  
- Provenance completeness  
- AI attribution safety (no hallucinated claims)  

---

## ⚖ FAIR+CARE Considerations

Climate data is generally **public**, but care applies to:

- Avoiding misinterpretations of climate events  
- Preventing amplification of harmful narratives  
- Ensuring equitable framing of impacts  
- Representing environmental justice contexts sensitively  

No sensitive personal data is allowed in climate Story Nodes.

---

## 🕰️ Version History

| Version | Date       | Summary                                                          |
|--------:|------------|------------------------------------------------------------------|
| v11.2.2 | 2025-11-30 | Initial governed climate Story Node domain; emoji layout added. |
| v11.2.1 | 2025-11-29 | Added structure for templates, examples, glossary, notes.        |

---

<div align="center">

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
[📚 Docs Home](../../../README.md) · [📏 Standards Index](../../../standards/README.md) · [🛡 Governance Charter](../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

