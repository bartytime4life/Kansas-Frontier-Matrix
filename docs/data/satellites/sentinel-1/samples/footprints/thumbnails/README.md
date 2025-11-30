---
title: "🖼️ Sentinel-1 Sample Thumbnails — UI-Ready Demo Imagery (CARE-Open)"
path: "docs/data/satellites/sentinel-1/samples/footprints/thumbnails/README.md"
version: "v11.2.2"
last_updated: "2025-11-29"

classification: "Public Demonstration Assets (CARE-Open · Non-Sensitive)"
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
previous_version_hash: "<previous>"
doc_integrity_checksum: "<sha256>"

telemetry_ref: "../../../../../../releases/v11.2.2/data-telemetry.json"
telemetry_schema: "../../../../../../schemas/telemetry/sentinel1-samples-footprints-thumbnails-v11.json"

governance_ref: "../../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../standards/faircare/FAIRCARE-GUIDE.md"

fair_category: "F1-A1-I2-R1"
care_label: "CARE-Open"
indigenous_rights_flag: false
sensitivity_level: "None"
public_exposure_risk: "Low"
risk_category: "Low"

data_steward: "Remote Sensing Working Group"

ontology_alignment:
  cidoc: "E84 Information Carrier"
  schema_org: "ImageObject"
  prov_o: "prov:Entity"
  geosparql: "geo:Feature"
  owl_time: "Instant"

json_schema_ref: "../../../../../../schemas/json/sentinel1-samples-footprints-thumbnails-v11.json"
shape_schema_ref: "../../../../../../schemas/shacl/sentinel1-samples-footprints-thumbnails-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:sentinel1:samples-footprints-thumbnails:v11.2.2"
semantic_document_id: "kfm-doc-data-sentinel1-samples-footprints-thumbnails"
event_source_id: "ledger:docs/data/satellites/sentinel-1/samples/footprints/thumbnails/README.md"
immutability_status: "version-pinned"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

ttl_policy: "60 months"
sunset_policy: "Superseded upon next demo-thumbnail refresh"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 🖼️ **Sentinel-1 Sample Thumbnails Library**  
`docs/data/satellites/sentinel-1/samples/footprints/thumbnails/`

Tiny, **public-safe, CARE-Open demo thumbnails** used in  
documentation, Focus Mode UI previews, STAC examples,  
README illustrations, and developer onboarding.

These images contain **no sensitive content** and are  
pre-generalized for open release.

</div>

---

## 🗂️ 1. Directory Layout (STRICT Option-A Emoji Style)

~~~text
docs/data/satellites/sentinel-1/samples/footprints/thumbnails/
├── 📄 README.md
│
├── 🖼️ scene_footprint.png        # Scene outline over basemap (demo-only)
├── 🖼️ burst_outline.png          # IW burst outline preview
└── 🖼️ overlay_sample.png         # Footprint + raster overlay example (public-safe)
~~~

✔ Emoji BEFORE filenames  
✔ Matches all sample/QA fixture directory standards  
✔ Box-safe (no broken fences)  
✔ Zero drift, aligned with the parent footprints/README.md  

---

## 📘 2. Purpose

This directory hosts lightweight thumbnails used for:

- **README illustrations**  
- **Focus Mode v3 UI demonstrations**  
- **Story Node v3 examples**  
- **MapLibre/Cesium UI previews**  
- **Developer onboarding & documentation**  
- **STAC Item sample previews**

All files are:

- non-sensitive  
- downsampled  
- pre-generalized  
- FAIR-Open  
- sovereignty-safe  

---

## 🧩 3. Files & Descriptions

### 🖼️ `scene_footprint.png`
Shows a simple **scene footprint** polygon on a basemap.  
Used in STAC examples and UI-component demos.

### 🖼️ `burst_outline.png`
Displays a sample **IW burst** outline — helpful for explaining  
burst-level processing and sub-swath geometry.

### 🖼️ `overlay_sample.png`
Composite preview demonstrating **footprint + raster overlay**,  
used in tutorials and Focus-Mode context training.

None of these images represent real sensitive data.  
All geometries and values are synthetic or pre-sanitized.

---

## 🔗 4. PROV-O Lineage

Even demo thumbnails carry minimal provenance so downstream tools  
recognize them as **non-authoritative** sample imagery:

~~~json
{
  "prov:Entity": "s1_demo_thumbnail",
  "kfm:provenance_type": "demo-sample",
  "kfm:care_label": "CARE-Open"
}
~~~

---

## 🔐 5. Governance Notes

- CARE label: **CARE-Open**  
- No sovereign territories, cultural sites, or sensitive features  
- Not for scientific/analytic use  
- Designed solely for UI, documentation, and onboarding  

---

## 🧭 6. Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v11.2.2 | 2025-11-29 | Initial Sentinel-1 sample thumbnails README; emoji alignment validated; zero drift. |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅ Back](../README.md) · [🧭 Footprints](../README.md) · [🧩 STAC Samples](../../stac/README.md)

</div>

