---
title: "🌍 Sentinel-1 Deformation — STAC Collections (Generalized InSAR LOS Displacement · Subsidence · Uplift)"
path: "docs/data/satellites/sentinel-1/stac/deformation/collections/README.md"
version: "v11.2.2"
last_updated: "2025-11-29"

classification: "Public With Restrictions (Governed SAR-Derived Dataset)"
status: "Active / Enforced"
release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Remote Sensing WG · FAIR+CARE Council Oversight"

license: "CC-BY 4.0 (ESA Open Data)"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
provenance_profile: "KFM-PROV-O v11.2"

commit_sha: "<latest-commit>"
previous_version_hash: "<previous-sha>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../../releases/v11.2.2/data-telemetry.json"
telemetry_schema: "../../../../../../schemas/telemetry/sat-sentinel1-stac-v11.json"

governance_ref: "../../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

fair_category: "F3-A1-I2-R5"
care_label: "CARE-B (Generalized InSAR Displacement)"
indigenous_rights_flag: true
sensitivity_level: "High"
public_exposure_risk: "Medium"
risk_category: "High"
redaction_required: true

data_steward: "Remote Sensing WG · FAIR+CARE Council"

ontology_alignment:
  schema_org: "Dataset"
  cidoc: "E84 Information Carrier"
  prov_o: "prov:Entity"
  geosparql: "geo:FeatureCollection"
  owl_time: "TemporalEntity"

json_schema_ref: "../../../../../../schemas/json/sentinel1-deformation-collections-v11.json"
shape_schema_ref: "../../../../../../schemas/shacl/sentinel1-deformation-collections-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:sentinel1:stac-deformation-collections-readme:v11.2.2"
semantic_document_id: "kfm-doc-data-sentinel1-stac-deformation-collections"
event_source_id: "ledger:docs/data/satellites/sentinel-1/stac/deformation/collections/README.md"
immutability_status: "version-pinned"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

ttl_policy: "36 months"
sunset_policy: "Superseded upon next ESA InSAR reprocessing epoch"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 🌍 **Sentinel-1 InSAR Deformation — Governed STAC Collections**  
`docs/data/satellites/sentinel-1/stac/deformation/collections/`

Catalogs for **Line-of-Sight (LOS) Displacement**,  
**subsidence**, **uplift**, and **seasonal ground motion**,  
all **sovereignty-generalized** per KFM’s H3 masking rules.

</div>

---

## 📘 1. Overview

This directory contains the governed **STAC Collections** for all Sentinel-1 deformation datasets  
produced from InSAR pipelines:

- LOS displacement (mm–cm scale)  
- subsidence / uplift patterns  
- seasonal ground-motion cycles  
- coherence-supported deformation indicators  
- generalized deformation surfaces inside sovereign H3 cells  

Because raw InSAR displacement can reveal sensitive ecological, cultural, or infrastructural details,  
**these Collections are sovereignty-generalized and CARE-B governed**.

These Collections define:

- spatial + temporal extents  
- SAR + InSAR metadata  
- DCAT dataset definitions  
- JSON-LD contexts  
- governance inheritance  
- PROV-O lineage anchors  

---

## 🗂️ 2. Directory Layout (Emoji-Strict Option A)

~~~text
docs/data/satellites/sentinel-1/stac/deformation/collections/
├── 📄 README.md                            # This file
│
└── 🌍 collection_deformation.json          # Main STAC Collection for InSAR deformation
~~~

---

## 🧩 3. Collection Responsibilities

### 🌐 Core STAC Metadata
- `"sar:product_type" = "INSAR"`  
- LOS deformation semantic fields  
- `"sar:instrument_mode" = "IW"`  
- `"sar:frequency_band" = "C"`  
- mission/platform metadata  
- bounding boxes + geometry (generalized)  
- temporal extent (pair or time-series window)  
- license = CC-BY-4.0  

### 📦 Assets
Collection assets may include:

- `"extent_preview"` — PNG snapshot  
- `"qa_overview"` — displacement QA overview  
- `"metadata"` — collection-level metadata descriptor  

### 🔗 Links
- `"self"`  
- `"root"`  
- `"parent"` (Sentinel-1 STAC root)  
- `"items"` → deformation items directory  
- `"child"` links (if separated by pair/time-series type)

### 🧬 PROV-O Lineage
The Collection encodes:

- SAR transformation chain  
- interferogram → unwrapping → LOS conversion provenance  
- sovereignty masking lineage  
- sustainability metrics (energy + carbon)  

---

## 🔐 4. FAIR+CARE & Sovereignty Controls (Mandatory)

InSAR deformation data is **highly sensitive**.  
Thus the Collection **must** include:

- `"kfm:care_label" = "CARE-B"`  
- `"kfm:care_label_reason"`  
- `"kfm:h3_sensitive"`  
- `"kfm:mask_required"`  
- `"kfm:sovereignty_uncertainty_floor"`  
- `"kfm:governance_notes"`  
- `"kfm:data_steward"`  

Sovereignty generalization:  
- deformation values & geometries are **coarsened** in H3-protected regions  
- uncertainty floors ensure no inference of precise motion  

CI validates these rules using:

- `faircare_validate.yml`  
- `jsonld_validate.yml`  
- `stac_validate.yml`

---

## 🧪 5. CI Validation Requirements

The deformation Collection must pass:

- STAC 1.x schema validation  
- SAR & InSAR extension checks  
- geometry sanity & bbox consistency  
- JSON-LD context resolution  
- DCAT dataset compliance  
- PROV-O lineage structure integrity  
- full `"kfm:*"` governance field verification  
- sovereignty-generalization enforcement  

Any violations → **blocked release**.

---

## 🔁 6. Role in the Sentinel-1 ETL Pipeline

~~~text
ESA ingest
 → orbit correction
 → radiometric calibration
 → coherence generation
 → interferogram formation
 → phase unwrapping
 → LOS displacement calculation
 → sovereignty generalization (mandatory)
 → displacement QA
 → STAC Item creation
 → deformation Collection update (this directory)
 → governed release bundle
~~~

---

## 🔮 7. Applications Across KFM

- subsidence/uplift studies  
- cultural-landscape hazard assessments  
- infrastructure stability (sovereignty-generalized)  
- hydrological ground-motion coupling  
- Story Node v3 environmental narratives  
- Focus Mode v3 sovereign-safe reasoning  

---

## 🧭 8. Version History

| Version | Date       | Summary                                                                                                     |
|--------:|------------|-------------------------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-29 | Initial Sentinel-1 deformation collections README; FAIR+CARE/H3 aligned; STAC/DCAT/PROV integrated; CI-safe.|

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅️ Back](../README.md) · [📦 Deformation Items](../items/README.md) · [🛡 Governance](../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

