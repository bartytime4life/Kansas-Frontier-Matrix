---
title: "💧 KFM v11.2.2 — Hydrology Story Node Domain (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/story-nodes/domains/hydrology/README.md"
version: "v11.2.2"
last_updated: "2025-11-30"
review_cycle: "Annual · Hydrology Systems Board · FAIR+CARE Council"

commit_sha: "<latest-commit>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

doc_uuid: "urn:kfm:storynodes:hydrology:v11.2.2"
semantic_document_id: "kfm-storynodes-hydrology-domain"
event_source_id: "ledger:storynodes/hydrology"
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
intent: "kfm-hydrology-storynode-domain"
lifecycle_stage: "stable"

fair_category: "F1-A2-I2-R2"
care_label: "Environmental"
classification: "Public"
jurisdiction: "Kansas / United States"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"

ttl_policy: "36 months"
sunset_policy: "Superseded by v12 hydrology domain rewrite"
---

<div align="center">

# 💧 **Hydrology Story Node Domain (KFM v11)**  
### **Diamond⁹ Ω / Crown∞Ω Ultimate Certified**  
### *Rivers · Watersheds · Flooding · Groundwater · Wetlands · Water Cycle*  

`docs/story-nodes/domains/hydrology/README.md`

**Purpose**  
Define governed rules for **hydrology Story Nodes**, ensuring scientific accuracy,  
spatial/temporal correctness, STAC/DCAT compliance, and Focus Mode v3 integration.

</div>

---

## 🗂️ Directory Layout

~~~text
docs/story-nodes/domains/hydrology/
├── 📄 README.md                               # Hydrology domain overview (this file)
├── 📁 templates/                               # Authoring templates (MD + JSON)
│   ├── 📝 story-node-hydrology.md              # Markdown authoring template
│   ├── 🧩 story-node-hydrology.json            # JSON schema-aligned skeleton
│   └── 🔗 relation-patterns.md                 # Hydrology graph relation patterns
├── 📁 examples/                                # Curated hydrology examples
│   ├── 🌊 arkansas-river-flood-2019.json       # Flooding example
│   ├── 💦 groundwater-decline-highplains.json  # Groundwater trend example
│   └── 📂 ...                                   # Additional examples
├── 📘 glossary.md                              # Hydrology terminology
└── 📁 notes/                                   # Drafts, backlog, ethics reviews
    ├── 📑 backlog.md                           # Candidate Story Nodes
    └── ⚖️ ethics-checklist.md                  # Water-data ethics & environmental safety
~~~

---

## 📘 Overview

The hydrology domain governs how KFM Story Nodes describe:

- **Rivers & Streams** — flow events, seasonal profiles, high-water episodes  
- **Flooding** — flash floods, riverine flooding, inundation footprints  
- **Groundwater** — aquifer trends, pumping impacts, recharge patterns  
- **Watersheds & Basins** — regional water-cycle dynamics  
- **Wetlands & Hydric Landscapes**  
- **Water Quality** (high-level, public-safe)  
- **Hydrologic Models & Datasets** — NWM, USGS NWIS, NHD, NID, GRACE, GLDAS  
- **Drought ↔ Hydrology interactions**  
- **Climate ↔ Hydrology links** (rainfall extremes, snowmelt, soil moisture)

Hydrology Story Nodes unify:

- **Spacetime-grounded hydrologic events**  
- **Observations** (stream gauges, satellite-derived water indices)  
- **Model outputs** (NWM short/medium-range, GRACE anomalies, GLDAS)  
- Scientific interpretation + uncertainty  
- Provenance (datasets, pipelines, sources)  
- Focus Mode v3 integration  
- STAC/DCAT/CF/PROV-O compliance  
- FAIR+CARE environmental framing

---

## 🧠 Story Node Requirements

### 1. Data Integrity & Scientific Rigor

Hydrology Story Nodes must:

- Clearly differentiate **observations vs. models**  
- Provide uncertainty ranges for streamflow, groundwater, inundation extents  
- Use **CF-compliant units** (e.g., m³/s, mm, ft³/s)  
- Use **NHDPlus**, **HUC** codes, or **region/watershed** names for generalized hydrologic units  
- Avoid implying exact property-level risk or disclosure

---

### 2. Spacetime Modeling

**Geometry:**

- Watershed polygons (HUC-8/HUC-10)  
- River corridor polygons  
- Flood extents (generalized)  
- Aquifer region boundaries  
- Avoid household-level or parcel-level spatial precision

**Temporal:**

- ISO intervals with `start` + `end`  
- Precision levels:
  - `"hour"` for flash-flood events  
  - `"day"` for riverine flooding  
  - `"month"` / `"year"` for aquifer trends  
- Include `original_label` such as:  
  - `"May 2019 Arkansas River Flooding"`  

---

### 3. Provenance & Dataset Requirements

Hydrology nodes may reference:

- **USGS NWIS** (gauges, trend data)  
- **USGS WaterWatch**  
- **NOAA NWM**  
- **NID dam infrastructure**  
- **GRACE water storage anomalies**  
- **Sentinel-1 inundation masks**  
- **NHD/NHDPlus**  
- **KGS aquifer datasets**  
- **Satellite water index rasters** (NDWI, MNDWI, etc.)

Every dataset reference must include:

- license  
- spatial coverage  
- temporal coverage  
- version  
- processing steps (if derived)  
- PROV-O lineage details

---

### 4. Graph Relations (Hydrology Domain)

Examples include:

- `about` → flood event, flow event, aquifer trend  
- `references` → USGS reports, hydrology datasets  
- `derived-from` → NWM/GRACE/GLDAS model outputs  
- `analog-of` → historical flood analogs  
- `impacts` → soil, ecology, agriculture Story Nodes  
- `linked-to-watershed` → HUC/watershed region  

See: `templates/relation-patterns.md`.

---

## 🧭 Focus Mode Integration

Focus Mode v3 will:

- Zoom map to river corridor / watershed  
- Show timeline of hydrologic evolution (before → peak → recession)  
- Surface datasets:
  - stream gauges  
  - satellite water indices  
  - NWM hydrology maps  
  - GRACE anomalies  
- Provide contextual cross-domain connections to:
  - climate events  
  - soil moisture  
  - drought indices  
  - ecological responses  

All narratives must be **data-grounded**, **public-safe**, and **scientifically neutral**.

---

## 📦 Metadata & Standards Integration

Hydrology Story Nodes must include:

- STAC raster links for inundation, model output, and hydrologic indices  
- DCAT dataset metadata  
- PROV-O lineage  
- CF standard name/unit compliance  
- CRS explicitly stated (EPSG:4326 unless otherwise required)  
- QC/QA notes for datasets used  

---

## 🧪 Validation

CI enforces:

- Story Node schema validity  
- GeoJSON validity  
- CF/CRS checks  
- Provenance completeness  
- STAC/DCAT link checks  
- Hydro-event classification checks  
- Environmental ethics guidelines  
- No parcel-level precision or property-level inference  

---

## ⚖ FAIR+CARE Considerations

Hydrology narratives must:

- Avoid exposing specific landowner impacts  
- Avoid privacy risks for infrastructure locations  
- Ensure equitable framing of community impacts  
- Maintain scientific neutrality  
- Avoid political framing  
- Include clear uncertainty statements  

No personal data is allowed.

---

## 🕰️ Version History

| Version | Date       | Summary                                                         |
|--------:|------------|-----------------------------------------------------------------|
| v11.2.2 | 2025-11-30 | Initial governed hydrology Story Node domain; directory added. |
| v11.2.1 | 2025-11-29 | Added template/example/glossary/notes scaffolding.             |

---

<div align="center">

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
[📚 Docs Home](../../../README.md) · [📏 Standards Index](../../../standards/README.md) · [🛡 Governance Charter](../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

