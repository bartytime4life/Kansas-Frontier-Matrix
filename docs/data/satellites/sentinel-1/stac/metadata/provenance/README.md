---
title: "🔗 Sentinel-1 — PROV-O Lineage Templates (Activities · Entities · Agents · SAR → STAC Transform Provenance)"
path: "docs/data/satellites/sentinel-1/stac/metadata/provenance/README.md"
version: "v11.2.2"
last_updated: "2025-11-29"

classification: "Public · Governed Provenance Metadata"
status: "Active / Enforced"
release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
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
sensitivity_level: "Medium"
public_exposure_risk: "Low–Medium"
risk_category: "Medium"
redaction_required: true

data_steward: "Remote Sensing WG · FAIR+CARE Council"

ontology_alignment:
  cidoc: "E7 Activity"
  schema_org: "Dataset"
  prov_o: "prov:Entity"
  geosparql: "geo:Feature"
  owl_time: "Instant"

json_schema_ref: "../../../../../../../schemas/json/sentinel1-provenance-v11.json"
shape_schema_ref: "../../../../../../../schemas/shacl/sentinel1-provenance-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:sentinel1:stac-metadata-provenance-readme:v11.2.2"
semantic_document_id: "kfm-doc-data-sentinel1-stac-metadata-provenance"
event_source_id: "ledger:docs/data/satellites/sentinel-1/stac/metadata/provenance/README.md"
immutability_status: "version-pinned"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

ttl_policy: "48 months"
sunset_policy: "Superseded upon next ESA InSAR/SAR reprocessing cycle"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 🔗 **Sentinel-1 PROV-O Lineage Templates**  
`docs/data/satellites/sentinel-1/stac/metadata/provenance/`

**Defines provenance structures for all SAR → STAC transformations**  
(orbit → radiometric calibration → RTC → coherence → deformation → flood → wetlands).

</div>

---

## 📘 1. Purpose

This directory contains **canonical PROV-O templates** used by all  
Sentinel-1 STAC Collections and Items.

These templates define how to describe:

- SAR processing activities  
- calibration and orbit-correction dependencies  
- RTC + coherence + flood + deformation workflows  
- data entities (ESA scenes, DEM tiles, LUTs, QA masks, COGs)  
- agents (ESA, KFM pipelines, FAIR+CARE governance agents)  

KFM uses these templates to ensure **consistent, machine-extractable, audit-ready**  
provenance for every Sentinel-1 dataset.

---

## 🗂️ 2. Directory Layout (Emoji-Aligned Option A)

~~~text
docs/data/satellites/sentinel-1/stac/metadata/provenance/
├── 📄 README.md                              # This file
│
├── 🔧 prov-activity.json                      # PROV-O activity template
├── 📦 prov-entity.json                        # PROV-O entity template
└── 🧑‍💼 prov-agent.json                       # PROV-O agent template
~~~

---

## 🧩 3. Template Responsibilities

### 🔧 `prov-activity.json`
Describes SAR/STAC-producing activities:

- orbit correction  
- radiometric calibration  
- speckle filtering  
- RTC generation  
- coherence pair formulation  
- interferogram creation  
- LOS displacement derivation  
- flood detection classifiers  
- wetland/inundation processors  

Includes:

- `prov:startedAtTime` / `prov:endedAtTime`  
- `prov:wasAssociatedWith`  
- `kfm:energy_wh` and `kfm:carbon_gco2e` for sustainability tracking  
- `"kfm:governance_notes"`

---

### 📦 `prov-entity.json`
Represents all data consumed and produced:

- ESA SAFE scenes  
- orbit and auxiliary files  
- DEM tiles  
- LUTs  
- RTC/COG assets  
- coherence rasters  
- flood/wetland layers  
- displacement tiles  
- STAC Items themselves  

Includes:

- `prov:wasDerivedFrom` relationships  
- `"kfm:*"` governance metadata  
- spatial/temporal extents (GeoSPARQL + OWL-Time)

---

### 🧑‍💼 `prov-agent.json`
Defines provenance agents:

- ESA mission  
- KFM SAR transform pipelines (automated agents)  
- FAIR+CARE Council oversight  
- remote-sensing working groups  
- sustainability auditor (KFM governance agent)  

Includes:

- `prov:type`  
- contact/role metadata  
- `"kfm:data_steward"`

---

## 🔐 4. FAIR+CARE & Sovereignty Controls

PROV-O templates **must encode** all governance metadata propagated into STAC Items:

- `"kfm:care_label"`  
- `"kfm:care_label_reason"`  
- `"kfm:h3_sensitive"`  
- `"kfm:mask_required"`  
- `"kfm:sovereignty_uncertainty_floor"`  
- `"kfm:governance_notes"`  
- `"kfm:data_steward"`  

Because degradation, generalization, and masking often happen during processing  
(especially for deformation, wetlands, and flood layers), these templates ensure  
that **sovereignty actions are always represented in the lineage graph**.

---

## 🧪 5. CI Validation Requirements

CI enforces:

- valid PROV-O JSON-LD  
- required IRIs resolvable  
- activity/entity/agent correctness  
- STAC → PROV linkage integrity (Item ↔ PROV)  
- `"kfm:*"` governance metadata present  
- temporal alignment (`prov:startedAtTime` < `prov:endedAtTime`)  
- social/institutional agent definitions correct  
- shape conformance via SHACL  

Any violation → **Sentinel-1 STAC release blocked**.

---

## 🔁 6. Role in the Sentinel-1 ETL Pipeline

~~~text
ESA ingest
 → orbit correction          (prov:Activity)
 → radiometric calibration   (prov:Activity)
 → RTC generation            (prov:Activity)
 → coherence/deformation     (prov:Activity)
 → flood/wetlands detection  (prov:Activity)
 → sovereignty masking       (prov:Activity + prov:Entity)
 → STAC Item assembly        (prov:Entity)
 → Collection update         (prov:Entity + prov:Agent)
 → governed release bundle
~~~

---

## 🔮 7. Applications Across KFM

- governance auditing  
- provenance visualization  
- Focus Mode v3 reasoning: “Why am I seeing this?”  
- Story Node v3 evidence linking  
- sustainability dashboards  
- temporal lineage browsing  
- relationship mapping across satellite & hydrology datasets  

---

## 🧭 8. Version History

| Version | Date       | Summary                                                                                                           |
|--------:|------------|-------------------------------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-29 | Initial Sentinel-1 PROV-O metadata README; FAIR+CARE/H3 aligned; DCAT/JSON-LD integrated; CI-validated; emoji-rich.|

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅️ Back](../README.md) · [📚 DCAT](../dcat/README.md) · [🧩 JSON-LD Contexts](../jsonld/README.md)

</div>

