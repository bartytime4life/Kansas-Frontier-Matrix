---
title: "🖼️ NASA SMAP — Sample Raster Thumbnails (Public-Safe Previews for Docs & UI)"
path: "docs/data/satellites/smap/samples/rasters/thumbnails/README.md"
version: "v11.2.2"
last_updated: "2025-11-29"

classification: "Public · Non-Sensitive · Synthetic Previews"
status: "Active / Public"
release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Annual · Documentation Systems WG · FAIR+CARE Council"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
provenance_profile: "KFM-PROV-O v11.2"

commit_sha: "<latest-commit>"
previous_version_hash: "<prev-sha>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../../../releases/v11.2.2/data-telemetry.json"
telemetry_schema: "../../../../../../../schemas/telemetry/sat-smap-v11.json"

governance_ref: "../../../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

fair_category: "F1-A1-I1-R1"
care_label: "CARE-A (Public / Low-Risk)"
indigenous_rights_flag: false
sensitivity_level: "None"
public_exposure_risk: "Low"
risk_category: "Low"
redaction_required: false

data_steward: "Earth Systems Working Group · FAIR+CARE Council"

ontology_alignment:
  cidoc: "E36 Visual Item"
  schema_org: "ImageObject"
  prov_o: "prov:Entity"
  owl_time: "TemporalEntity"

json_schema_ref: "../../../../../../../schemas/json/smap-sample-thumbnails-v11.json"
shape_schema_ref: "../../../../../../../schemas/shacl/smap-sample-thumbnails-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:smap:sample-thumbnails-readme:v11.2.2"
semantic_document_id: "kfm-doc-data-smap-sample-thumbnails"
event_source_id: "ledger:docs/data/satellites/smap/samples/rasters/thumbnails/README.md"
immutability_status: "version-pinned"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
ttl_policy: "72 months"
sunset_policy: "Superseded on next preview refresh"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 🖼️ **SMAP Sample Raster Thumbnails**  
`docs/data/satellites/smap/samples/rasters/thumbnails/`

**Purpose**  
Provide **small, synthetic, public-safe PNG previews** of sample SMAP raster datasets  
used in documentation, tutorials, UI mockups, MapLibre/Cesium examples,  
and CI documentation tests.

</div>

---

## 📘 1. Overview

Thumbnail images in this directory:

- visually preview synthetic sample COGs  
- are safe for **public distribution**, demos, workshops, and training materials  
- contain **no real SMAP data**  
- highlight approximate raster structure, not scientific values  
- assist with UI and UX documentation (storybook, MapLibre layers, etc.)  
- are sized to be **lightweight** for docs and CI  
- include **alt-text metadata** for accessibility (WCAG 2.1 AA+)  

They are **not** used in ETL or real modeling pipelines.

---

## 🗂️ 2. Directory Layout (Emoji-Rich · Option A)

~~~text
docs/data/satellites/smap/samples/rasters/thumbnails/
├── 📄 README.md                  # This file
│
├── 💧 sm_preview.png             # Soil Moisture raster preview
├── 🌡️ ft_preview.png             # Freeze–Thaw raster preview
├── 🌿 vwc_preview.png            # Vegetation Water Content preview
└── 📉 uncertainty_preview.png    # QA → Uncertainty scaling preview
~~~

---

## 🧩 3. Thumbnail Responsibilities

### 💧 `sm_preview.png`
- Synthetic visualization of a “soil moisture-like” field  
- Used in STAC examples, docs tables, app UI mockups  

### 🌡️ `ft_preview.png`
- Demonstrates a simplified Freeze–Thaw classification pattern  
- Suitable for showing legend and categorical STAC assets  

### 🌿 `vwc_preview.png`
- Shows a vegetation-water texture style preview  
- Used for documentation, Focus Mode explanation examples  

### 📉 `uncertainty_preview.png`
- Depicts synthetic uncertainty multipliers  
- Used in tutorials explaining QA → uncertainty propagation  

**All images** are:
- low resolution  
- non-sensitive  
- public training-ready  
- FAIR+CARE approved  

---

## 🔐 4. FAIR+CARE & Sovereignty Notes

Thumbnails:

- contain **no sovereign-sensitive** geo-information  
- are **purely synthetic** and **safe to publish**  
- may include optional tutorial metadata (e.g., `"kfm:care_label": "CARE-A"`)  
- do NOT require sovereignty masking  

They serve as visual scaffolding for documentation, not scientific analysis.

---

## 🧪 5. Validation & CI Behavior

CI checks that:

- preview files exist  
- images load without corruption  
- alt-text is registered for accessibility  
- sizes stay small (< 500 KB typically)  
- filenames match STAC asset naming conventions  
- no EXIF geolocation metadata exists  
- image format is PNG only  

---

## 🔁 6. Relation to Other SMAP Directories

These thumbnails visually represent the sample COGs found in:

`docs/data/satellites/smap/samples/rasters/`

They are used by:

- documentation  
- story-driven tutorials  
- Focus Mode demo flows  
- STAC tutorials  
- developer onboarding  

They are **not** used in:

- SMAP ETL pipelines  
- scientific workflows  
- sovereign-sensitive domains  

---

## 🔮 7. Applications Across KFM

- 📘 Documentation pages  
- 🌐 Web UI previews  
- 🧭 Focus Mode narrative examples  
- 🧪 CI smoke test previews  
- 🎓 Training & workshops  
- 🗺️ STAC educational materials  

---

## 🧭 8. Version History

| Version | Date       | Summary                                                                                                |
|--------:|------------|--------------------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-29 | Initial sample raster thumbnail README; FAIR+CARE aligned; public-safe; tutorial-ready; emoji-rich.     |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅️ Back](../README.md) · [🗺️ Sample Rasters](../README.md) · [🛡 Governance](../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

