---
title: "💧 KFM v11.2.2 — Hydrology Story Node Relation Patterns"
path: "docs/story-nodes/domains/hydrology/templates/relation-patterns.md"
version: "v11.2.2"
last_updated: "2025-11-30"
review_cycle: "Annual · Hydrology Systems Board · FAIR+CARE Council · Narrative Governance Board"

commit_sha: "<latest-commit>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

doc_uuid: "urn:kfm:storynodes:hydrology:relationpatterns:v11.2.2"
semantic_document_id: "kfm-storynodes-hydrology-relpatterns"
event_source_id: "ledger:storynodes/hydrology/relationpatterns"
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
doc_kind: "Relation Pattern Guide"
intent: "kfm-hydrology-storynode-relpatterns"
lifecycle_stage: "stable"

fair_category: "F1-A2-I2-R2"
care_label: "Environmental"
classification: "Public-Safe"
jurisdiction: "Kansas / United States"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"

ttl_policy: "36 months"
sunset_policy: "Superseded by v12 hydrology domain rewrite"
---

<div align="center">

# 💧 **Hydrology Story Node — Relation Patterns (KFM v11)**  
### *Rivers · Floods · Groundwater · Watersheds · Water Cycle Interactions*  

`docs/story-nodes/domains/hydrology/templates/relation-patterns.md`

**Purpose**  
Define **safe**, **governed**, **schema-aligned** relationships for hydrology Story Nodes  
to ensure graph consistency across hydrology, climate, soil, and ecology domains.

</div>

---

## 📘 Overview

Hydrology Story Nodes require precise, scientifically correct, graph-safe relations linking:

- hydrologic events  
- rivers/streams  
- watersheds  
- flood extents  
- groundwater trends  
- datasets (USGS NWIS, NWM, GRACE, Sentinel-1, GLDAS, etc.)  
- climate/hydrology interactions  
- soil/ecology impacts  

All relations must:

- be **CIDOC-CRM**, **GeoSPARQL**, **OWL-Time**, **PROV-O**, and **KFM v11 ontology** aligned  
- remain **public-safe** (no parcel-level inference)  
- reflect **data-grounded** relationships  
- avoid speculative connections  

---

# 🔗 Hydrology Relation Pattern Library (KFM v11)

Each relation includes:

- **rel** (relation name)  
- Meaning  
- Ontology alignment  
- Usage rules  
- Safe example snippet (JSON)

---

## 🧱 1. Primary Identification

### **`rel: "about"`**
**Meaning:** The Story Node is about a hydrologic event/trend/process.  
**CIDOC:** `E5 Event`, `E7 Activity`, `E53 Place`  
**Rules:**  
- Only **one** `about` relationship per Story Node  
- Used for: floods, streamflow events, groundwater trends, watershed events  

**Example**
~~~json
{
  "rel": "about",
  "id": "hydro:event-2019-arkansas-river-flood"
}
~~~

---

## 🌊 2. Watershed & Basin Relations

### **`rel: "linked-to-watershed"`**
**Meaning:** Links event/node to watershed where process occurs.  
**CIDOC:** `P89 falls within`  
**Rules:**  
- Use HUC-8 or HUC-10 when possible  
- Never more granular than HUC-12 in public nodes  

**Example**
~~~json
{
  "rel": "linked-to-watershed",
  "id": "watershed:huc8-110300"
}
~~~

---

### **`rel: "flows-through"`**
**Meaning:** Connects rivers/streams through which an event propagates.  
**CIDOC:** `P46 is composed of`, `P89 falls within`  

**Example**
~~~json
{
  "rel": "flows-through",
  "id": "river:arkansas-river"
}
~~~

---

## 🌧️ 3. Data & Provenance

### **`rel: "references"`**
**Meaning:** Links to reports, datasets, documents.  
**CIDOC:** `E31 Document`  
**Rules:**  
- Use for USGS NWIS, NOAA, NWM, GRACE, GLDAS reports  
- Must be public-safe datasets  

**Example**
~~~json
{
  "rel": "references",
  "id": "dataset:usgs-nwis-07137500"
}
~~~

---

### **`rel: "derived-from"`**
**Meaning:** Hydrology Story Node derived from a model or dataset.  
**PROV-O:** `prov:wasDerivedFrom`  
**Rules:**  
- Use for NWM, GLDAS, GRACE, reconstructed inundation rasters  
- Must specify dataset version in final node  

**Example**
~~~json
{
  "rel": "derived-from",
  "id": "model:nwm-v3-mediumrange"
}
~~~

---

## 🌀 4. Hydro–Climate Interaction

### **`rel: "climate-driver"`**
**Meaning:** Climate condition influencing hydrology (e.g., heavy rainfall, drought).  
**CIDOC:** `E55 Type`  
**Rules:**  
- Must be supported by data (e.g., ERA5 precipitation anomalies)  
- Avoid causal overstatement  

**Example**
~~~json
{
  "rel": "climate-driver",
  "id": "climate:extreme-precip-june-2019"
}
~~~

---

### **`rel: "analog-of"`**
**Meaning:** Hydrologic event similar to a historical analog.  
**CIDOC:** `P130 shows features of`  
**Rules:**  
- Use when hydrologic behavior matches historic patterns  
- Must be documented  

**Example**
~~~json
{
  "rel": "analog-of",
  "id": "hydro:event-1993-flood"
}
~~~

---

## 💦 5. Impacts

### **`rel: "impacts"`**
**Meaning:** Links hydrology event to another domain affected by it.  
**CIDOC:** `E5 Event` → `E55 Type`  
**Rules:**  
- Use for soil moisture changes, ecological effects, drought follow-up  

**Example**
~~~json
{
  "rel": "impacts",
  "id": "soil:moisture-spike-2019"
}
~~~

---

## 🌍 6. Spatial Context

### **`rel: "located-in"`**
**Meaning:** General region where hydrology event occurred.  
**CIDOC:** `P89 falls within`  
**Rules:**  
- Use counties, watersheds, or basins  
- Avoid fine-scale location unless already public  

**Example**
~~~json
{
  "rel": "located-in",
  "id": "region:kansas-arkansas-river-basin"
}
~~~

---

## 🔬 7. Observation/Measurement Links

### **`rel: "measured-at"`**
**Meaning:** Event measured at specific USGS gauges or model gridpoints.  
**CIDOC:** `P39 measured`  
**Rules:**  
- USGS gauge IDs allowed (public)  
- Avoid privately owned sensors  

**Example**
~~~json
{
  "rel": "measured-at",
  "id": "usgs-gauge:07137500"
}
~~~

---

# 🧩 Quick Reference Matrix

~~~text
about              → primary hydrology event/trend  
linked-to-watershed→ HUC-8/10 watershed context  
flows-through      → river/stream system  
references         → datasets, documents  
derived-from       → models, reanalysis, hydrology rasters  
climate-driver     → climate forcing event  
analog-of          → historical analogs  
impacts            → soil, ecology, agriculture, climate  
located-in         → region, basin, county  
measured-at        → USGS gauge, measurement site  
~~~

---

# 🕰️ Version History

| Version | Date       | Summary                                                                    |
|--------:|------------|----------------------------------------------------------------------------|
| v11.2.2 | 2025-11-30 | Initial governed hydrology relation-pattern library added to domain.       |
| v11.2.1 | 2025-11-29 | Draft scaffolding for CIDOC/GeoSPARQL/PROV-O hydrology relations created. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
[📚 Docs Home](../../../../README.md) · [📏 Standards Index](../../../standards/README.md) · [🛡 Governance Charter](../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

