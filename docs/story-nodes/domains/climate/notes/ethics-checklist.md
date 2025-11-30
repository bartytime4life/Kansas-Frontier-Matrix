---
title: "🌦️ KFM v11.2.2 — Climate Story Node Ethics & Attribution Checklist"
path: "docs/story-nodes/domains/climate/notes/ethics-checklist.md"
version: "v11.2.2"
last_updated: "2025-11-30"
review_cycle: "Annual · Climate Systems Board · FAIR+CARE Council · AI Attribution Governance Board"

commit_sha: "<latest-commit>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

doc_uuid: "urn:kfm:storynodes:climate:ethicschecklist:v11.2.2"
semantic_document_id: "kfm-storynodes-climate-ethicschecklist"
event_source_id: "ledger:storynodes/climate/ethicschecklist"
immutability_status: "version-pinned"

governance_ref: "../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"

status: "Active / Enforced"
doc_kind: "Ethics Checklist"
intent: "kfm-climate-ethics-checklist"
lifecycle_stage: "stable"

fair_category: "F1-A2-I2-R2"
care_label: "Environmental · Attribution-Sensitive"
classification: "Internal-Review"
jurisdiction: "Kansas / United States"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"

ttl_policy: "36 months"
sunset_policy: "Superseded by v12 climate ethics checklist"
---

<div align="center">

# 🌦️ **Climate Story Node — Ethics & Attribution Checklist (KFM v11)**  
### *Scientific Integrity · Attribution Safety · Environmental Justice · FAIR+CARE*  

`docs/story-nodes/domains/climate/notes/ethics-checklist.md`

**Purpose**  
Provide a governed checklist ensuring climate Story Nodes follow  
**scientific rigor**, **ethical attribution**, **public-safe communication**,  
and **environmental justice considerations**.

</div>

---

# 🧭 How to Use This Checklist

Run this checklist **before** submitting any climate Story Node (MD or JSON).  
Non-passing items **block CI/CD** until fixed.

Climate Story Nodes are vulnerable to:

- over-attribution  
- sensationalism  
- data misuse  
- model/observation confusion  
- environmental justice blindspots  
- improper uncertainty framing  

This checklist prevents those failures.

---

# ✅ **Climate Ethics & Attribution Checklist (KFM v11)**

## 🌡️ 1. Scientific Accuracy & Rigor

| Question | Yes/No | Notes |
|----------|--------|-------|
| Are all claims supported by NOAA/ERA5/HRRR/GFS/GOES datasets? |  |  |
| Are observations clearly separated from model output? |  |  |
| Is uncertainty stated for all key findings? |  |  |
| Are extreme event metrics (e.g., SPI, SPEI, anomalies) used correctly? |  |  |
| Are CF units and variable names correct? |  |  |

---

## 🌀 2. Event Classification & Boundaries

| Question | Yes/No | Notes |
|----------|--------|-------|
| Is the event classification (heatwave, drought, tornado outbreak) consistent with NOAA/NWS conventions? |  |  |
| Is the temporal interval realistic and data-backed? |  |  |
| Are regional boundaries generalized appropriately? |  |  |
| Are NEXRAD/GOES/ERA5 footprints described without over-precision? |  |  |

---

## 🔭 3. Attribution & Interpretation Controls

| Question | Yes/No | Notes |
|----------|--------|-------|
| Are climate change attribution statements fully evidence-backed? |  |  |
| Are no exaggerated or speculative causal claims made? |  |  |
| Are attribution confidence levels explicitly stated? |  |  |
| Are any conflicting analyses acknowledged? |  |  |

---

## 🧩 4. Data Sources & Provenance

| Question | Yes/No | Notes |
|----------|--------|-------|
| Are all datasets public and properly cited? |  |  |
| Are STAC/DCAT dataset references complete? |  |  |
| Are model run IDs, initialization times, and parameters documented? |  |  |
| Is PROV-O lineage included (pipeline, source data, transformations)? |  |  |

---

## 🌐 5. Geometry & Temporal Modeling

| Question | Yes/No | Notes |
|----------|--------|-------|
| Is the geometry valid GeoJSON (region, county, raster footprint)? |  |  |
| Is temporal precision correct (hour/day/month/year)? |  |  |
| Is a proper `original_label` included (“June 2022 Heatwave”, etc.)? |  |  |
| Are multi-phase or multi-day events modeled with intervals? |  |  |

---

## 🔗 6. Graph Relations

| Question | Yes/No | Notes |
|----------|--------|-------|
| Are relations chosen from approved patterns (`relation-patterns.md`)? |  |  |
| Is `about` used only once? |  |  |
| Are `derived-from` and `references` used correctly for datasets/models? |  |  |
| Are linked nodes public-safe? |  |  |

---

## 🖼 7. Media & Asset Licensing

| Question | Yes/No | Notes |
|----------|--------|-------|
| Are radar/satellite images properly licensed? |  |  |
| Are HRRR/ERA5 rasters linked through STAC? |  |  |
| Do images avoid private property/individuals? |  |  |
| Are derivative visualizations labeled as processed data? |  |  |

---

## 🌍 8. Environmental Justice Considerations

| Question | Yes/No | Notes |
|----------|--------|-------|
| Does the narrative address disproportionate impacts when relevant? |  |  |
| Is no community portrayed negatively or stereotypically? |  |  |
| Is the framing respectful and evidence-backed? |  |  |
| Does the narrative avoid politicization? |  |  |

---

## 🧪 9. CI/CD Readiness

| Question | Yes/No | Notes |
|----------|--------|-------|
| Schema validation passed? |  |  |
| Markdown protocol (if applicable) passed? |  |  |
| Provenance completeness check passed? |  |  |
| Environmental ethics linting passed? |  |  |
| STAC/DCAT dataset links valid? |  |  |

---

## 🕊 10. Reviewer Sign-off

| Reviewer Type | Name/Org | Approved? | Notes |
|---------------|-----------|-----------|-------|
| Climate Domain Reviewer |  |  |  |
| Attribution Specialist |  |  |  |
| FAIR+CARE Council |  |  |  |
| Governance Board (if needed) |  |  |  |

---

# 🕰️ Version History

| Version | Date       | Summary                                                        |
|--------:|------------|----------------------------------------------------------------|
| v11.2.2 | 2025-11-30 | Initial governed climate ethics & attribution checklist.        |
| v11.2.1 | 2025-11-29 | Added attribution safety & environmental justice sections.      |

---

<div align="center">

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
[📚 Docs Home](../../../../README.md) · [📏 Standards Index](../../../standards/README.md) · [🛡 Governance Charter](../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

