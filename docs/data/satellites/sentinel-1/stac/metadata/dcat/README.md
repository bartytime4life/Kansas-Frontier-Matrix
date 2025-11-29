---
title: "📚 Sentinel-1 — DCAT Metadata Blocks (Dataset · Distribution · Catalog Integration)"
path: "docs/data/satellites/sentinel-1/stac/metadata/dcat/README.md"
version: "v11.2.2"
last_updated: "2025-11-29"

classification: "Public · Governed Metadata"
status: "Active / Enforced"
release_stage: "Stable · Governed"
lifecycle: "Long-Term Support · LTS"
review_cycle: "Quarterly · Remote Sensing WG · FAIR+CARE Council"
content_stability: "Stable"

license: "CC-BY 4.0 (ESA)"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
provenance_profile: "KFM-PROV-O v11.2"

commit_sha: "<latest>"
previous_version_hash: "<prev>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../../../releases/v11.2.2/data-telemetry.json"
telemetry_schema: "../../../../../../../schemas/telemetry/sat-sentinel1-stac-v11.json"

governance_ref: "../../../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

fair_category: "F2-A1-I2-R4"
care_label: "CARE-A / CARE-B depending on derived dataset"
indigenous_rights_flag: true
sensitivity_level: "Low–Medium"
public_exposure_risk: "Low"
risk_category: "Medium"
redaction_required: true

data_steward: "Remote Sensing Working Group · FAIR+CARE Council"

ontology_alignment:
  cidoc: "E73 Information Object"
  schema_org: "Dataset"
  prov_o: "prov:Entity"
  geosparql: "geo:FeatureCollection"
  owl_time: "Instant"

json_schema_ref: "../../../../../../../schemas/json/sentinel1-dcat-metadata-v11.json"
shape_schema_ref: "../../../../../../../schemas/shacl/sentinel1-dcat-metadata-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:sentinel1:stac-metadata-dcat-readme:v11.2.2"
semantic_document_id: "kfm-doc-data-sentinel1-stac-metadata-dcat"
event_source_id: "ledger:docs/data/satellites/sentinel-1/stac/metadata/dcat/README.md"
immutability_status: "version-pinned"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

ttl_policy: "36 months"
sunset_policy: "Superseded upon next ESA metadata cycle"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 📚 **Sentinel-1 DCAT Metadata Directory**  
`docs/data/satellites/sentinel-1/stac/metadata/dcat/`

**DCAT v3 Dataset & Distribution building blocks**  
for all governed Sentinel-1 STAC Collections and Items.

</div>

---

## 📘 1. Purpose

This directory contains the **DCAT metadata fragments** that provide:

- `dcat:Dataset` templates  
- `dcat:Distribution` metadata blocks  
- license, keywords, provider info  
- spatial/temporal coverage definitions  
- governance metadata carriers  
- sovereign-sensitive masking attributes  
- crosswalk fields between DCAT ↔ STAC ↔ JSON-LD  

These fragments are imported into:

- `/collections/*.json`  
- `/items/**/` STAC Items  
- the global DCAT catalog used by KFM’s data registry  

---

## 🗂️ 2. Directory Layout (Emoji-Aligned Option A)

~~~text
docs/data/satellites/sentinel-1/stac/metadata/dcat/
├── 📄 README.md                       # This file
│
├── 📚 dataset.json                    # DCAT Dataset template (collection-level)
└── 📦 distribution.json               # DCAT Distribution template (per STAC asset)
~~~

---

## 🧩 3. DCAT Metadata Responsibilities

### 📚 `dataset.json`
Defines DCAT-level dataset attributes:

- `dct:title`, `dct:description`  
- `dcat:keyword` list (hydrology, SAR, flood, coherence)  
- `dct:spatial` (GeoJSON bbox or WKTs)  
- `dct:temporal` (`time:Interval`)  
- ESA + KFM providers (`dcat:contactPoint`, `dct:publisher`)  
- distribution references  
- `"kfm:*"` governance fields  
- STAC/DCAT equivalence keys (`dct:identifier`, `dct:isPartOf`)  

This file anchors **Sentinel-1 product families** (GRD/GRDH/RTC/Coherence/Deformation/Flood/Wetlands).

---

### 📦 `distribution.json`
Defines per-asset metadata:

- media type (image/tiff; application/json; image/png)  
- access pattern (HTTP/COG)  
- compression/auth info  
- `"proj:*"` crosswalk fields for geometry CCR  
- `"sar:*"` and `"s1:*"` SAR-specific metadata  
- `"kfm.*"` sovereignty & CARE metadata (propagated into Items)  
- versioning (`dcat:version`)  
- PROV-O lineage references  

This is used for **all COG/PNG/QA/JSON assets** across Sentinel-1 Items.

---

## 🔐 4. FAIR+CARE & Sovereignty Controls

DCAT metadata enforces complete governance structure:

- `"kfm:care_label"`  
- `"kfm:care_label_reason"`  
- `"kfm:h3_sensitive"`  
- `"kfm:mask_required"`  
- `"kfm:sovereignty_uncertainty_floor"`  
- `"kfm:governance_notes"`  
- `"kfm:data_steward"`  

All DCAT fragments undergo sovereignty validation under:

- `faircare_validate.yml`  
- `jsonld_validate.yml`  

This ensures governance consistency across all STAC products.

---

## 🧪 5. CI Validation

CI checks:

- DCAT v3 schema correctness  
- alignment with STAC + JSON-LD fields  
- PROV-O compatibility  
- required governance metadata  
- dataset/distribution relationships  
- versioning and integrity keys  
- duplicate field prevention  
- crosswalk completeness  

Any violation → **Sentinel-1 release blocked** until corrected.

---

## 🔁 6. DCAT in the Sentinel-1 ETL Flow

~~~text
Sentinel-1 ingest
 → SAR transforms (orbit, radiometric, RTC, coherence, deformation, flood, wetlands)
 → STAC Item assembly
 → DCAT Dataset & Distribution assembly (this directory)
 → STAC Collection generation
 → governed release bundle
~~~

---

## 🔮 7. Applications Across KFM

- global dataset registry  
- Story Node v3 dataset lineage  
- Focus Mode v3 “dataset provenance” cards  
- DCAT export for portals  
- metadata search & semantic indexing  
- governance auditing  

---

## 🧭 8. Version History

| Version | Date       | Summary                                                                                                 |
|--------:|------------|---------------------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-29 | Initial Sentinel-1 DCAT metadata README; STAC/DCAT/JSON-LD/PROV-O integrated; FAIR+CARE/H3 aligned.     |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅️ Back](../README.md) · [🧩 JSON-LD](../jsonld/README.md) · [🔗 PROV-O](../provenance/README.md)

</div>

