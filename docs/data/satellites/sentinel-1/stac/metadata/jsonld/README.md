---
title: "🧩 Sentinel-1 — JSON-LD Contexts (SAR · STAC · GeoSPARQL · Temporal · Governance · PROV-O)"
path: "docs/data/satellites/sentinel-1/stac/metadata/jsonld/README.md"
version: "v11.2.2"
last_updated: "2025-11-29"

classification: "Public · Governed Linked-Data Contexts"
status: "Active / Enforced"
release_stage: "Stable · Governed"
lifecycle: "Long-Term Support · LTS"
review_cycle: "Quarterly · Remote Sensing WG · FAIR+CARE Council"

license: "CC-BY 4.0 (ESA)"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
provenance_profile: "KFM-PROV-O v11.2"

commit_sha: "<latest-commit>"
previous_version_hash: "<previous-sha>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../../../releases/v11.2.2/data-telemetry.json"
telemetry_schema: "../../../../../../../schemas/telemetry/sat-sentinel1-stac-v11.json"

governance_ref: "../../../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

fair_category: "F2-A1-I2-R4"
care_label: "CARE-A / CARE-B"
indigenous_rights_flag: true
sensitivity_level: "Low–Medium"
public_exposure_risk: "Low"
risk_category: "Medium"
redaction_required: true

data_steward: "Remote Sensing WG · FAIR+CARE Council"

ontology_alignment:
  schema_org: "Dataset"
  cidoc: "E73 Information Object"
  prov_o: "prov:Entity"
  geosparql: "geo:FeatureCollection"
  owl_time: "TemporalEntity"

json_schema_ref: "../../../../../../../schemas/json/sentinel1-jsonld-v11.json"
shape_schema_ref: "../../../../../../../schemas/shacl/sentinel1-jsonld-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:sentinel1:stac-metadata-jsonld-readme:v11.2.2"
semantic_document_id: "kfm-doc-data-sentinel1-stac-metadata-jsonld"
event_source_id: "ledger:docs/data/satellites/sentinel-1/stac/metadata/jsonld/README.md"
immutability_status: "version-pinned"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

ttl_policy: "36 months"
sunset_policy: "Superseded upon next ESA metadata cycle"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 🧩 **Sentinel-1 JSON-LD Contexts**  
`docs/data/satellites/sentinel-1/stac/metadata/jsonld/`

**Semantic contexts for STAC, SAR, GeoSPARQL, OWL-Time, PROV-O, and KFM governance fields.**

</div>

---

## 📘 1. Purpose

This directory defines the **JSON-LD semantic contexts** used across all  
Sentinel-1 STAC Collections and Items.

These contexts ensure that all Sentinel-1 metadata can be:

- parsed as linked data  
- reasoned over by KFM’s semantic graph  
- validated using PROV-O + KFM-OP v11 ontologies  
- compliant with FAIR+CARE governance metadata  
- interoperable with GeoSPARQL and OWL-Time  
- aligned with DCAT Dataset/Distribution semantics  
- machine-extractable for Focus Mode v3 and Story Node v3  

---

## 🗂️ 2. Directory Layout (Emoji-Aligned · Option A)

~~~text
docs/data/satellites/sentinel-1/stac/metadata/jsonld/
├── 📄 README.md                            # This file
│
├── 🧩 sentinel1-context.jsonld              # Base context for Sentinel-1 product metadata
├── 🧩 sar-extension.jsonld                  # SAR & Sentinel-1 extension fields (sar:* · s1:*)
├── 🧩 kfm-governance.jsonld                 # CARE, sovereignty, masking, stewardship metadata
└── 🧩 provenance-context.jsonld             # PROV-O activities/entities/agents for STAC lineage
~~~

---

## 🧩 3. JSON-LD Context Responsibilities

### 🧩 `sentinel1-context.jsonld`
Defines semantic mappings for:

- `sar:*` (SAR extension)  
- `s1:*` (Sentinel-1 mission metadata)  
- mission platform, orbit, mode, polarization  
- STAC Item & Collection top-level fields  
- relevant ESA metadata  

Used by **all** Sentinel-1 Items and Collections.

---

### 🧩 `sar-extension.jsonld`
Defines:

- SAR acquisition parameters  
- viewing geometry  
- radiometric calibration attributes  
- product typing (`GRD`, `GRDH`, `RTC`, `COH`, `INSAR`, `FLOOD`, `WETLAND`)  
- polarization & frequency-band semantics  

Used across **all** STAC product families.

---

### 🧩 `kfm-governance.jsonld`
Defines all KFM governance semantics:

- `"kfm:care_label"`  
- `"kfm:care_label_reason"`  
- `"kfm:h3_sensitive"`  
- `"kfm:mask_required"`  
- `"kfm:sovereignty_uncertainty_floor"`  
- `"kfm:data_steward"`  
- `"kfm:governance_notes"`  

This is critical for **sovereignty enforcement**, **CARE compliance**, and  
**KFM provenance alignment**.

---

### 🧩 `provenance-context.jsonld`
Maps all PROV-O elements:

- `prov:Activity` (orbit correction, RTC, coherence, deformation, flood processing)  
- `prov:Entity` (ESA scenes, DEMs, LUTs, COGs)  
- `prov:Agent` (ESA, KFM pipelines, automated agents)  

Used for full semantic lineage in every STAC Item.

---

## 🔐 4. FAIR+CARE & Sovereignty Considerations

JSON-LD contexts **must** represent governance metadata faithfully because reviewers and  
analytical systems rely on them to enforce:

- sovereignty masking  
- CARE label enforcement  
- uncertainty floors for inference-sensitive data  
- ethical interpretability of SAR-derived features  
- correct PROV-O lineage structure  

All contexts undergo validation via:

- `jsonld_validate.yml`  
- `stac_validate.yml`  
- `faircare_validate.yml`

---

## 🧪 5. CI Validation Requirements

CI checks:

- valid JSON-LD syntax  
- required IRIs present  
- correct context expansion  
- STAC extension compatibility  
- PROV-O alignment  
- GeoSPARQL + OWL-Time integration  
- `"kfm:*"` governance fields resolvable  
- duplicate-term collisions prevented  
- DCAT ↔ JSON-LD ↔ STAC crosswalk integrity  

Any violation → **metadata block stops all Sentinel-1 releases**.

---

## 🔁 6. JSON-LD Role in the Sentinel-1 ETL Pipeline

~~~text
ESA ingest
 → SAR transformations (RTC, coherence, deformation, flood, wetlands)
 → STAC Item generation
 → JSON-LD context application (this directory)
 → Collection assembly
 → DCAT metadata integration
 → governed release bundle
~~~

---

## 🔮 7. Applications Across KFM

- Story Node v3 entity semantics  
- Focus Mode v3 reasoning context  
- DCAT catalog & semantic search  
- provenance graph construction  
- FAIR+CARE governance dashboards  
- cross-dataset semantic linking (SAR ↔ hydrology ↔ ecology ↔ archives)  

---

## 🧭 8. Version History

| Version | Date       | Summary                                                                                                       |
|--------:|------------|---------------------------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-29 | Initial Sentinel-1 JSON-LD metadata README; STAC/DCAT/PROV integrated; FAIR+CARE/H3 aligned; CI-safe.         |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅️ Back](../README.md) · [📚 DCAT Metadata](../dcat/README.md) · [🔗 PROV-O Templates](../provenance/README.md)

</div>

