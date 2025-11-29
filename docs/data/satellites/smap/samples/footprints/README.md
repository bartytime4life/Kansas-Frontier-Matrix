---
title: "🗺️ NASA SMAP — Sample Footprints (Tiny Synthetic GeoJSON Extents · Tutorial-Safe)"
path: "docs/data/satellites/smap/samples/footprints/README.md"
version: "v11.2.2"
last_updated: "2025-11-29"

classification: "Public · Non-Sensitive · Synthetic Examples"
status: "Active / Public"
release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Annual · Documentation WG · FAIR+CARE Council Oversight"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
provenance_profile: "KFM-PROV-O v11.2"

commit_sha: "<latest>"
previous_version_hash: "<prev>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../releases/v11.2.2/data-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/sat-smap-v11.json"

governance_ref: "../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

fair_category: "F1-A1-I1-R1"
care_label: "CARE-A (Public / Low-Risk)"
indigenous_rights_flag: false
sensitivity_level: "None"
public_exposure_risk: "Low"
risk_category: "Low"
redaction_required: false

data_steward: "Earth Systems WG · FAIR+CARE Council"

ontology_alignment:
  schema_org: "Dataset"
  cidoc: "E73 Information Object"
  prov_o: "prov:Entity"
  geosparql: "geo:FeatureCollection"
  owl_time: "TemporalEntity"

json_schema_ref: "../../../../../schemas/json/smap-sample-footprints-v11.json"
shape_schema_ref: "../../../../../schemas/shacl/smap-sample-footprints-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:smap:samples-footprints-readme:v11.2.2"
semantic_document_id: "kfm-doc-data-smap-samples-footprints"
event_source_id: "ledger:docs/data/satellites/smap/samples/footprints/README.md"
immutability_status: "version-pinned"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
ttl_policy: "72 months"
sunset_policy: "Superseded upon sample refresh cycle"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 🗺️ **Sample SMAP Footprints**  
`docs/data/satellites/smap/samples/footprints/`

**Purpose**  
Provide **tiny, synthetic, sovereignty-safe GeoJSON footprints** for use in  
tutorials, documentation, STAC examples, Focus Mode visual demos, and CI smoke tests.  
These footprints illustrate STAC geometry patterns without revealing real-world boundaries.

</div>

---

## 📘 1. Overview

These sample footprints:

- show **safe example geographic extents**  
- support **STAC Collection + Item tutorials**  
- are used in **MapLibre/Cesium map demos**  
- demonstrate **bounding boxes**, **coverage polygons**, and **tile extents**  
- help explain **provenance and geometry handling** in the KFM system  
- are **synthetic** and **culturally/ecologically safe**  
- include optional metadata for training (but not required in real ETL)

These GeoJSONs **do not** contain real SMAP geometry;  
they are **downsampled demo geometry** produced artificially.

---

## 🗂️ 2. Directory Layout (Emoji-Rich · Option A)

~~~text
docs/data/satellites/smap/samples/footprints/
├── 📄 README.md                           # This file
│
├── 🗺️ sm_footprint.geojson                # Soil Moisture sample extent
├── 🗺️ ft_footprint.geojson                # Freeze–Thaw sample extent
└── 🗺️ vwc_footprint.geojson               # Vegetation Water Content sample extent
~~~

---

## 🧩 3. Footprint Responsibilities

### 🗺️ `sm_footprint.geojson`
Represents a **small synthetic bounding polygon** used to:

- illustrate STAC Item spatial extents  
- show coverage relationships over sample rasters  
- demonstrate map-layer clipping in tutorials  

### 🗺️ `ft_footprint.geojson`
Used for:

- freeze–thaw classification footprint examples  
- categorical area demos  
- Focus Mode environmental context cards  

### 🗺️ `vwc_footprint.geojson`
Used for:

- vegetation-water coverage illustration  
- STAC/DCAT footprint mapping  
- example story-node overlays  

All footprints exhibit:

- valid GeoJSON  
- safe coordinates  
- small bounding areas  
- no sovereign-sensitive shapes  

---

## 🔐 4. FAIR+CARE & Sovereignty Notes

All footprints:

- are **safe for public sharing**  
- contain **no sensitive ecological or cultural patterns**  
- are synthetic (constructed shapes)  
- do not intersect or imply sovereign H3 regions  
- have **CARE-A** classification only for public documentation  

Metadata fields may include optional tutorial-only `"kfm:*"` tags to illustrate  
governance structures but **do not represent real data**.

---

## 🧪 5. Validation & CI Behavior

CI validates:

- GeoJSON schema correctness  
- coordinate arrays  
- winding order normalization  
- bounding-box structure  
- absence of real coordinates  
- absence of EXIF/geolocation in thumbnails (if generated)  
- documentation integrity  

These files participate in **docs CI**, not production ETL.

---

## 🔁 6. Relationship to SMAP ETL

This folder is **not** part of the ingestion or processing chain.

It is used for:

- 🧭 Focus Mode demos  
- 🌐 web/docs previews  
- 📚 tutorials & notebooks  
- 🧪 CI smoke tests  
- 🗺️ STAC/DCAT training examples  

Use production geometry from:

```
data/satellites/smap/stac/**/item.json
```

---

## 🔮 7. Applications Across KFM

- Documentation  
- Storytelling tutorials  
- UI map previews  
- STAC examples  
- Developer onboarding  
- Public workshops  

---

## 🧭 8. Version History

| Version | Date       | Summary                                                                                      |
|--------:|------------|----------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-29 | Initial sample footprint README; public-safe synthetic shapes; FAIR+CARE aligned; emoji-rich.|

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅️ Back](../README.md) · [🧪 Sample QA](../qa/README.md) · [🛡 Governance](../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

