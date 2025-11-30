---
title: "🧭 Sentinel-1 Sample Footprints — Scene Geometry & Thumbnails (Demo-Only)"
path: "docs/data/satellites/sentinel-1/samples/footprints/README.md"
version: "v11.2.2"
last_updated: "2025-11-29"

classification: "Public Demonstration Data (CARE-Open · Non-Sensitive)"
status: "Active · Stable"
release_stage: "Stable"
lifecycle: "LTS"
review_cycle: "Annual · Remote Sensing WG"

license: "CC-BY 4.0"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
provenance_profile: "KFM-PROV-O v11.2"

commit_sha: "<latest-commit>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

telemetry_ref: "../../../../../releases/v11.2.2/data-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/sentinel1-samples-footprints-v11.json"

governance_ref: "../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../standards/faircare/FAIRCARE-GUIDE.md"

fair_category: "F1-A1-I2-R1"
care_label: "CARE-Open"
indigenous_rights_flag: false
sensitivity_level: "None"
public_exposure_risk: "Low"
risk_category: "Low"
redaction_required: false

data_steward: "Remote Sensing Working Group"

ontology_alignment:
  cidoc: "E84 Information Carrier"
  schema_org: "Dataset"
  prov_o: "prov:Entity"
  geosparql: "geo:FeatureCollection"
  owl_time: "Instant"

json_schema_ref: "../../../../../schemas/json/sentinel1-samples-footprints-v11.json"
shape_schema_ref: "../../../../../schemas/shacl/sentinel1-samples-footprints-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:sentinel1:samples-footprints:v11.2.2"
semantic_document_id: "kfm-doc-data-sentinel1-samples-footprints"
event_source_id: "ledger:docs/data/satellites/sentinel-1/samples/footprints/README.md"
immutability_status: "version-pinned"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

ttl_policy: "60 months"
sunset_policy: "Superseded when demo footprint suite is refreshed"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 🧭 **Sentinel-1 Sample Footprints & Thumbnails**  
`docs/data/satellites/sentinel-1/samples/footprints/`

Public-safe **scene footprints** and **mini thumbnails** used in  
documentation, tutorials, Story Node demos, and Focus Mode UI examples.  
These are **demo-only** geometries and images — not used for analysis.

</div>

---

## 🗂️ 1. Directory Layout (STRICT Option-A Emoji Style)

~~~text
docs/data/satellites/sentinel-1/samples/footprints/
├── 📄 README.md
│
├── 🧭 scene_footprint.geojson        # Demo polygon footprint of a Sentinel-1 sample scene
├── 🧭 burst_outline.geojson          # Demo IW burst outline / swath geometry
│
└── 🖼️ thumbnails/                    # Small PNG thumbnails for UI / docs
    ├── 🖼️ scene_footprint.png       # Map frame preview of scene footprint
    ├── 🖼️ burst_outline.png         # Burst outline overlay preview
    └── 🖼️ overlay_sample.png        # Example overlay (footprint + raster)
~~~

✔ Emoji BEFORE filenames and directories  
✔ Matches the sample rasters + STAC patterns  
✔ Box-safe (single fenced block), no nested backticks  

---

## 📘 2. Purpose

This directory provides **non-sensitive geometry + thumbnail previews** that:

- illustrate **Sentinel-1 scene extents**  
- support **MapLibre / Cesium** UI development  
- act as sample geometries for **STAC Item** examples  
- allow Story Node & Focus Mode demos to attach to **fake/demo footprints**  
- help testers and developers understand how footprints, bursts, and overlays work  
- avoid using any real, sensitive, or sovereign-respecting scene boundaries  

All content is **demonstration-only**, **CARE-Open**, and **not** intended for analytical use.

---

## 🧩 3. File Descriptions

### 🧭 `scene_footprint.geojson`

A simplified, public-safe polygon representing a sample Sentinel-1 scene:

- CRS: EPSG:4326  
- Attributes:  
  - `scene_id` (demo ID)  
  - `sensor` (e.g., `"Sentinel-1A"`)  
  - `mode` (e.g., `"IW"`)  
  - `demo:note` explaining that this is **synthetic/modified**  

Used for:

- STAC `geometry` / `bbox` examples  
- map-layer demos  
- Story Node spatial attachment examples  

---

### 🧭 `burst_outline.geojson`

Polyline or polygon representing a **demo IW burst** or subswath footprint:

- may show a single burst tile or sub-scene  
- matches sample rasters’ extents (in `../rasters/`)  
- safe for public demonstration  

Used in:

- tutorials on burst-level processing  
- ETL diagrams  
- Focus Mode spatial selection UIs  

---

### 🖼️ `thumbnails/`

Contains tiny PNGs, safe for embedding in docs and UI:

- `scene_footprint.png` → simple outline + base map  
- `burst_outline.png` → burst geometry highlight  
- `overlay_sample.png` → footprint + example raster overlay  

These are intended for:

- README screenshots  
- KFM docs & tutorials  
- Story Node / Focus Mode UI previews  

No high-resolution or sensitive imagery is stored here.

---

## 🔗 4. PROV-O & Metadata

Even for demo content, basic provenance is recorded:

~~~json
{
  "prov:Entity": "s1_demo_footprint_sample",
  "kfm:provenance_type": "demo-sample",
  "kfm:care_label": "CARE-Open"
}
~~~

This clarifies that:

- geometries are **demo-only**  
- not derived from protected or sensitive datasets  
- safe to include in public documentation and tests  

---

## 🔐 5. Governance & CARE Notes

- Data here is explicitly **non-sensitive**  
- No real sovereign boundaries or cultural sites are encoded  
- All shapes and thumbnails are simplified/generalized and **not suitable** for analytic interpretation  
- CARE label: **CARE-Open**  

These assets are for **training, demos, and UI** only.

---

## 🧭 6. Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v11.2.2 | 2025-11-29 | Initial Sentinel-1 sample footprints README; emoji alignment validated; zero drift. |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅ Back](../README.md) · [🗺️ Raster Samples](../rasters/README.md) · [🧩 STAC Samples](../stac/README.md)

</div>

