---
title: "🧾 Sentinel-1 STAC Metadata — JSON-LD · DCAT · PROV-O · Assets · Extensions (Governed)"
path: "docs/data/satellites/sentinel-1/stac/metadata/README.md"
version: "v11.2.2"
last_updated: "2025-11-29"

classification: "Public · Governed Earth Observation Metadata"
status: "Active / Enforced"
release_stage: "Stable · Governed"
lifecycle: "LTS (Long-Term Support)"
review_cycle: "Quarterly · Remote Sensing WG · FAIR+CARE Council"

license: "CC-BY 4.0 (ESA)"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
provenance_profile: "KFM-PROV-O v11.2"

commit_sha: "<latest>"
previous_version_hash: "<prev>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../../releases/v11.2.2/data-telemetry.json"
telemetry_schema: "../../../../../../schemas/telemetry/sat-sentinel1-stac-v11.json"

governance_ref: "../../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

fair_category: "F2-A1-I2-R4"
care_label: "CARE-A / CARE-B depending on derived dataset"
indigenous_rights_flag: true
sensitivity_level: "Low–Medium"
public_exposure_risk: "Low"
risk_category: "Medium"
redaction_required: true

data_steward: "Remote Sensing WG · FAIR+CARE Council"

ontology_alignment:
  cidoc: "E73 Information Object"
  schema_org: "Dataset"
  prov_o: "prov:Entity"
  geosparql: "geo:FeatureCollection"
  owl_time: "Instant"

json_schema_ref: "../../../../../../schemas/json/sentinel1-stac-metadata-v11.json"
shape_schema_ref: "../../../../../../schemas/shacl/sentinel1-stac-metadata-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:sentinel1:stac-metadata-readme:v11.2.2"
semantic_document_id: "kfm-doc-data-sentinel1-stac-metadata"
event_source_id: "ledger:docs/data/satellites/sentinel-1/stac/metadata/README.md"
immutability_status: "version-pinned"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

ttl_policy: "36 months"
sunset_policy: "Superseded on next ESA metadata reprocessing cycle"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 🧾 **Sentinel-1 STAC Metadata Layer**  
`docs/data/satellites/sentinel-1/stac/metadata/`

**JSON-LD · DCAT · PROV-O · Extensions & Contexts**  
Metadata foundations for **all Sentinel-1 STAC Collections and Items** in KFM v11.

</div>

---

## 📘 1. Purpose

This directory contains **metadata scaffolding** used by all Sentinel-1 STAC Collections and Items:

- 🧩 JSON-LD context files (semantic mapping)  
- 📚 DCAT dataset/distribution metadata  
- 🔗 PROV-O lineage templates  
- 📦 asset-level metadata blocks  
- 🛰 SAR extension fields  
- 🗂 collection inheritance templates  
- 🛡 governance metadata templates  

Every STAC Item and Collection under `sentinel-1/stac/` links to these metadata patterns.

---

## 🗂️ 2. Directory Layout (Emoji-Aligned Option A)

~~~text
docs/data/satellites/sentinel-1/stac/metadata/
├── 📄 README.md                         # This file
│
├── 📚 dcat/                             # DCAT v3 Dataset & Distribution fragments
│   ├── dataset.json
│   └── distribution.json
│
├── 🧩 jsonld/                           # JSON-LD contexts for SAR/STAC/Geo fields
│   ├── sentinel1-context.jsonld
│   ├── sar-extension.jsonld
│   ├── kfm-governance.jsonld
│   └── provenance-context.jsonld
│
└── 🔗 provenance/                       # PROV-O activity/entity/agent templates
    ├── prov-activity.json
    ├── prov-entity.json
    └── prov-agent.json
~~~

---

## 🧩 3. Metadata Responsibilities

### 📚 **DCAT / Dataset Metadata**
Defines:

- dataset title, description, keywords  
- temporal extent & acquisition range  
- spatial extent & bounding boxes  
- license & providers  
- distributions (COG, PNG, JSON)  
- conformance to DCAT v3  
- `"kfm:*"` governance metadata fields  

### 🧩 **JSON-LD Contexts**
Provide semantic definitions for:

- SAR extension fields (`sar:*`, `s1:*`)  
- geospatial relationships (`geo:*`, `geosparql:*`)  
- temporal schema (`time:*`)  
- KFM governance fields (`kfm:*`)  
- PROV-O (`prov:*`)  

These contexts allow STAC Items to be parsed as **linked data**.

### 🔗 **PROV-O Templates**
Define:

- `prov:Activity` patterns (orbit correction, RTC, coherence, InSAR, flood, wetlands)  
- `prov:Entity` (source ESA scenes, DEMs, LUTs, COGs)  
- `prov:Agent` (ESA, KFM pipelines, automated agents)  

All Sentinel-1 STAC Items import these templates and attach IDs.

---

## 🔐 4. FAIR+CARE & Sovereignty Metadata Rules

All metadata templates enforce explicit governance structure:

- `"kfm:care_label"`  
- `"kfm:care_label_reason"`  
- `"kfm:h3_sensitive"`  
- `"kfm:mask_required"`  
- `"kfm:sovereignty_uncertainty_floor"`  
- `"kfm:governance_notes"`  

These fields flow from metadata → Collections → Items → analytics.

Governance validated via:

- **jsonld_validate.yml**  
- **stac_validate.yml**  
- **faircare_validate.yml**

---

## 🧪 5. CI Validation Requirements

CI checks:

- JSON-LD context validity  
- DCAT schema compliance  
- PROV-O structural conformance  
- required `"kfm:*"` governance fields  
- extension compatibility (SAR, proj, eo)  
- metadata inheritance correctness  
- DCAT→STAC consistency  
- integrity of linked references  

Failure → **metadata block halts all Sentinel-1 releases**.

---

## 🔁 6. Metadata in the Sentinel-1 ETL Flow

~~~text
ESA ingest
 → orbit correction
 → radiometric calibration
 → RTC / coherence / flood / deformation derivations
 → sovereignty masking
 → STAC Item generation (metadata pulled from this directory)
 → STAC Collection assembly (root + extension metadata)
 → governed release bundle
~~~

---

## 🔮 7. Applications Across KFM

- STAC browsing  
- Focus Mode v3 narrative metadata  
- Story Node v3 evidence linking  
- DCAT cataloging for the data index  
- provenance visualization & audit trails  
- FAIR+CARE governance dashboards  

---

## 🧭 8. Version History

| Version | Date       | Summary                                                                                                  |
|--------:|------------|----------------------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-29 | Initial Sentinel-1 STAC metadata README; FAIR+CARE/H3 aligned; DCAT/JSON-LD/PROV integrated; CI-safe.    |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅️ Back](../README.md) · [🗂 Collections](../collections/README.md) · [🛡 Governance](../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

