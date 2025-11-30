---
title: "🧩 Sentinel-1 Sample STAC Items — Demonstration Metadata (GRD · RTC · Coherence · Flood · Wetlands · Deformation)"
path: "docs/data/satellites/sentinel-1/samples/stac/README.md"
version: "v11.2.2"
last_updated: "2025-11-29"

classification: "Public Demonstration Metadata (CARE-Open · Non-Sensitive)"
status: "Active · Stable"
release_stage: "Stable"
lifecycle: "LTS"
review_cycle: "Annual · Remote Sensing WG"

license: "CC-BY 4.0"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
provenance_profile: "KFM-PROV-O v11.2"

commit_sha: "<latest>"
previous_version_hash: "<prev>"
doc_integrity_checksum: "<sha256>"

telemetry_ref: "../../../../../releases/v11.2.2/data-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/sentinel1-samples-stac-v11.json"

governance_ref: "../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../standards/faircare/FAIRCARE-GUIDE.md"

fair_category: "F1-A1-I2-R1"
care_label: "CARE-Open"
indigenous_rights_flag: false
sensitivity_level: "None"
public_exposure_risk: "Low"
risk_category: "Low"

data_steward: "Remote Sensing Working Group"

ontology_alignment:
  cidoc: "E84 Information Carrier"
  schema_org: "Dataset"
  prov_o: "prov:Entity"
  geosparql: "geo:FeatureCollection"
  owl_time: "Instant"

json_schema_ref: "../../../../../schemas/json/sentinel1-samples-stac-v11.json"
shape_schema_ref: "../../../../../schemas/shacl/sentinel1-samples-stac-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:sentinel1:samples-stac:v11.2.2"
semantic_document_id: "kfm-doc-data-sentinel1-samples-stac"
event_source_id: "ledger:docs/data/satellites/sentinel-1/samples/stac/README.md"
immutability_status: "version-pinned"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

ttl_policy: "60 months"
sunset_policy: "Superseded when sample STAC suite is refreshed"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 🧩 **Sentinel-1 Sample STAC Items Library**  
`docs/data/satellites/sentinel-1/samples/stac/`

A **public-safe**, fully governed set of **demonstration STAC Items**  
for GRD, RTC, coherence, flood, wetlands, and deformation products.  
Used for tutorials, documentation, UI mockups, Focus-Mode examples, and  
developer onboarding — not for analytical use.

</div>

---

## 🗂️ 1. Directory Layout (STRICT Option-A Emoji Style)

~~~text
docs/data/satellites/sentinel-1/samples/stac/
├── 📄 README.md
│
├── 📄 item_grd.json              # Sample STAC Item (σ⁰ calibrated GRD)
├── 📄 item_rtc.json              # Sample STAC Item (γ⁰ terrain-corrected RTC)
├── 📄 item_coherence.json        # Sample STAC Item (coherence magnitude)
├── 📄 item_flood.json            # Sample STAC Item (flood mask demo)
├── 📄 item_wetlands.json         # Sample STAC Item (wetness/saturation demo)
└── 📄 item_deformation.json      # Sample STAC Item (generalized LOS demo)
~~~

✔ Emoji BEFORE filenames  
✔ Matches sample raster + footprint directory structure  
✔ Zero drift, no broken fences  

---

## 📘 2. Purpose

This directory contains **demonstration-only STAC Items**, designed to help:

- developers learn STAC routing in KFM  
- UI/MapLibre/Cesium teams test layer loading  
- documentation authors illustrate STAC structure  
- Focus-Mode v3 demos reference safe Items  
- Story Node v3 examples attach to non-sensitive layers  
- tutorials explain how STAC assets, geometry, and metadata work  

These Items are constructed using **public-safe**, simplified,  
pre-generalized data — no sovereign or sensitive information is included.

---

## 🧩 3. About the Sample STAC Items

Each sample STAC Item includes:

- `type: "Feature"`  
- `geometry` & `bbox` from **demo footprints**  
- `properties.datetime` & simplified metadata  
- `assets` referencing **demo rasters** (under `samples/rasters/`)  
- KFM-STAC v11 fields (`kfm:*`)  
- FAIR-Open CARE label  
- `prov:Entity` minimal provenance block  
- No sensitive coordinates, no real ENV data  

### Example content included:

- **GRD:** σ⁰ VV demonstration  
- **RTC:** γ⁰ VV terrain-normalized demo  
- **Coherence:** magnitude (0–1)  
- **Flood:** safe flood mask example  
- **Wetlands:** pseudo wetness/saturation  
- **Deformation:** generalized LOS displacement  

---

## 🔐 4. Governance & CARE-Open Notes

All Items are:

- CARE-Open  
- pre-generalized  
- stripped of sovereign or cultural coordinates  
- safe for external publication  
- valid for tutorials  
- **NOT** valid for environmental, hydrological, or hazard analysis  

---

## 🔗 5. PROV-O Lineage

Sample Items include a minimal provenance block:

~~~json
{
  "prov:Entity": "s1_sample_stac_item",
  "kfm:provenance_type": "demo-sample",
  "kfm:care_label": "CARE-Open"
}
~~~

This explicitly marks them as “non-truth,” non-scientific examples.

---

## 🧭 6. Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v11.2.2 | 2025-11-29 | Initial Sentinel-1 sample STAC README; emoji alignment validated; zero drift. |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅ Back](../README.md) · [🗺️ Raster Samples](../rasters/README.md) · [🧭 Footprints](../footprints/README.md)

</div>

