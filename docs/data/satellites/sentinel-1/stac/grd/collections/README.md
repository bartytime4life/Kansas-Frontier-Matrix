---
title: "🛰️ Sentinel-1 GRD — STAC Collections (σ⁰ VV/VH Backscatter · Hydrology · Land-Change)"
path: "docs/data/satellites/sentinel-1/stac/grd/collections/README.md"
version: "v11.2.2"
last_updated: "2025-11-29"

classification: "Public Earth Observation (Governed Metadata)"
status: "Active / Enforced"
release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Remote Sensing WG · FAIR+CARE Council Oversight"

license: "CC-BY-4.0 (ESA Open Data)"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
provenance_profile: "KFM-PROV-O v11.2"

commit_sha: "<latest-commit>"
previous_version_hash: "<prev-sha>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../../releases/v11.2.2/data-telemetry.json"
telemetry_schema: "../../../../../../schemas/telemetry/sat-sentinel1-stac-v11.json"

governance_ref: "../../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

fair_category: "F2-A1-I2-R4"
care_label: "CARE-A / CARE-B (depending on derivation)"
indigenous_rights_flag: true
sensitivity_level: "Low–Medium"
public_exposure_risk: "Low"
risk_category: "Low–Medium"
redaction_required: false

data_steward: "Remote Sensing WG · FAIR+CARE Council"

ontology_alignment:
  schema_org: "Dataset"
  cidoc: "E84 Information Carrier"
  prov_o: "prov:Entity"
  geosparql: "geo:FeatureCollection"
  owl_time: "TemporalEntity"

json_schema_ref: "../../../../../../schemas/json/sentinel1-grd-collections-v11.json"
shape_schema_ref: "../../../../../../schemas/shacl/sentinel1-grd-collections-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:sentinel1:stac-grd-collections-readme:v11.2.2"
semantic_document_id: "kfm-doc-data-sentinel1-stac-grd-collections"
event_source_id: "ledger:docs/data/satellites/sentinel-1/stac/grd/collections/README.md"
immutability_status: "version-pinned"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
ttl_policy: "48 months"
sunset_policy: "Superseded upon next ESA GRD reprocessing cycle"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 🛰️ **Sentinel-1 GRD — Governed STAC Collections**  
`docs/data/satellites/sentinel-1/stac/grd/collections/`

Collections that catalog **σ⁰ VV/VH Ground Range Detected backscatter**  
used across hydrology, land-change detection, agriculture, hazard analysis,  
and as upstream sources for RTC, coherence, flood, deformation, and wetlands pipelines.

</div>

---

## 📘 1. Overview

This directory contains the **STAC Collections** for Sentinel-1 **GRD** backscatter scenes:

- calibrated σ⁰ VV/VH  
- standard (non-high-resolution) GRD  
- multi-temporal hydrology & land-change applications  
- flood pre/post analysis inputs  
- agricultural disturbance and vegetation state mapping  
- upstream inputs to all higher-order SAR derivatives in KFM v11  

All GRD Collections here:

- follow STAC 1.x  
- embed JSON-LD contexts  
- carry `"kfm:*"` governance metadata  
- satisfy DCAT dataset requirements  
- include PROV-O lineage anchors  
- undergo CI validation for sovereignty & FAIR+CARE compliance  

---

## 🗂️ 2. Directory Layout (Emoji-Strict Option A)

~~~text
docs/data/satellites/sentinel-1/stac/grd/collections/
├── 📄 README.md                      # This file
│
└── 🛰️ collection_grd.json            # Primary GRD Collection definition
~~~

---

## 🧩 3. GRD STAC Collection Structure

### 🌐 Core STAC Metadata  
- `"sar:product_type" = "GRD"`  
- `"sar:polarizations" = ["VV","VH"]`  
- `"sar:instrument_mode" = "IW"`  
- `"sar:frequency_band" = "C"`  
- STAC version, ID, description  
- spatial and temporal extent  
- licensing & provider metadata  
- `"kfm:*"` governance inheritance  
- mission/platform details  
- acquisition metadata  

### 📦 Collection-Level Assets  
May include:

- `"extent_preview"` (PNG)  
- `"metadata"` (JSON with collection-scale descriptors)  
- `"qa_overview"` (optional)  

### 🔗 Link Graph  
- `"self"`  
- `"root"`  
- `"parent"` → Sentinel-1 STAC root  
- `"items"` → `../items/`  
- `"child"` → possible sub-collections (e.g., by orbit/track)  

### 🧬 PROV-O Lineage  
The collection embeds:

- SAR → GRD transformation activity metadata  
- ESA SAFE → COG conversion provenance  
- energy/carbon sustainability (optional extension)  
- sovereignty masking lineage (if applied)  

---

## 🔐 4. Governance & Sovereignty Enforcement

Even GRD backscatter can reveal:

- agricultural disturbance  
- land-use transitions  
- flood pre/post patterns  
- ecological boundaries  
- sovereign-land surface patterns  

Thus, all GRD Collections **must include**:

- `"kfm:care_label"`  
- `"kfm:h3_sensitive"`  
- `"kfm:mask_required"` when sovereign intersections occur  
- `"kfm:governance_notes"`  
- `"kfm:data_steward"`  
- `"kfm:care_label_reason"` (if CARE-B designated)  

Sovereignty-generalization is less common at GRD resolution  
but MUST be applied whenever sovereign risk triggers.

Governance is validated in CI via:

- `faircare_validate.yml`
- `jsonld_validate.yml`
- `stac_validate.yml`

---

## 🧪 5. CI Validation Requirements

A GRD Collection must pass:

- STAC 1.x schema validation  
- SAR extension validation  
- geometry/bbox consistency  
- JSON-LD context resolution  
- DCAT dataset conformance  
- `"kfm:*"` governance metadata  
- sovereign masking rules  
- PROV-O lineage integrity  

Any failure → **release blocked**.

---

## 🔁 6. GRD Collection Role in the ETL Pipeline

~~~text
ESA ingest
 → orbit correction
 → radiometric calibration
 → GRD scene generation
 → QA (border noise, calibration anomalies)
 → sovereignty check & potential generalization
 → STAC Item generation
 → GRD Collection update (this directory)
 → governed release bundle
~~~

---

## 🔮 7. Applications Across KFM

- hydrology baselines  
- flood pre/post comparisons  
- land-cover/land-use change  
- agricultural cycle detection  
- hazard early-warning signals  
- Story Node v3 environmental context  
- Focus Mode v3 SAR evidence  
- upstream inputs for RTC, coherence, flood, deformation  

---

## 🧭 8. Version History

| Version | Date       | Summary                                                                                                       |
|--------:|------------|-----------------------------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-29 | Initial Sentinel-1 GRD Collections README; FAIR+CARE/H3 aligned; STAC/DCAT/PROV integrated; CI-validated.      |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅️ Back](../README.md) · [📦 GRD Items](../items/README.md) · [🛡 Governance](../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

