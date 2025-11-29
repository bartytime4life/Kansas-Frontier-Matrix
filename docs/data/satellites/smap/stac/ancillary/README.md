---
title: "📚 NASA SMAP — Ancillary Metadata, Orbits, Grids & Calibration (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/data/satellites/smap/stac/ancillary/README.md"
version: "v11.2.2"
last_updated: "2025-11-29"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Earth Systems · FAIR+CARE Council"
status: "Active / Enforced"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha>"
doc_integrity_checksum: "<sha256>"

stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"

sbom_ref: "../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../releases/v11.2.2/data-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/sat-smap-ancillary-v11.json"

governance_ref: "../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"

classification: "Public Dataset Ancillary Overview"
fair_category: "F1-A1-I1-R2"
care_label: "CARE-A / CARE-B depending on overlap with sovereign lands"
indigenous_rights_flag: true
sensitivity_level: "Low"
public_exposure_risk: "Low"
risk_category: "Low"
redaction_required: false

data_steward: "Earth Systems Working Group · KFM FAIR+CARE Council"

ontology_alignment:
  cidoc: "E73 Information Object"
  schema_org: "Dataset"
  prov_o: "prov:Entity"
  owl_time: "Duration"
  geosparql: "geo:FeatureCollection"

json_schema_ref: "../../../../../schemas/json/stac-smap-ancillary-v11.schema.json"
shape_schema_ref: "../../../../../schemas/shacl/stac-smap-ancillary-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:smap:ancillary-readme:v11.2.2"
semantic_document_id: "kfm-doc-data-smap-ancillary"
event_source_id: "ledger:docs/data/satellites/smap/stac/ancillary/README.md"
immutability_status: "version-pinned"
machine_extractable: true

accessibility_compliance: "WCAG 2.1 AA+"
ttl_policy: "24 months"
sunset_policy: "Superseded by next SMAP ancillary schema revision"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 📚 **NASA SMAP — Ancillary Metadata (Orbits · Grids · Calibration · Sensor Modes)**  
`docs/data/satellites/smap/stac/ancillary/README.md`

**Purpose**  
Document the **ancillary SMAP metadata** required for interpreting all SMAP STAC datasets  
(soil moisture, freeze–thaw, VWC, QA/RFI).  
These include **orbit tracks**, **EASE-Grid definitions**, **calibration structures**,  
**radiometer mode files**, and **sensor geometry metadata**,  
all aligned with **KFM-STAC v11**, FAIR+CARE, and sovereignty governance.

</div>

---

## 📘 1. Overview

SMAP ancillary metadata provides the **non-raster context** needed for:

- Correct spatial interpretation (EASE-Grid 2.0)  
- Orbit/overpass timing  
- Sensor geometry  
- Calibration states  
- Radiometer mode & performance details  
- Provenance references to NASA L1–L3 products  
- QA schema references for SMAP soil-moisture, FT, VWC

These files support:

- Per-Item STAC creation  
- Sensor correction workflows  
- ETL reproducibility  
- Story Node v3 environmental context  
- Focus Mode v3 environmental reliability  

---

## 🗂️ 2. Directory Layout (Emoji-Rich · Option A)

~~~text
docs/data/satellites/smap/stac/ancillary/
├── 📄 README.md                          # This file
│
├── 🛰️ orbit-tracks.json                 # Orbit geometry, overpass times, swath metadata
├── 🗺️ ease-grid-2.0.json                # EASE-Grid 2.0 projection + cell definitions
├── 🎚️ calibration.json                   # Calibration coefficients, drift notes, radiometer configs
├── 📐 sensor-geometry.json               # Incidence angle, footprint, beam parameters
├── 🧭 radiometer-modes.json              # Radiometer mode states, transitions, expected performance
└── 🔗 provenance-map.json                # NASA L1/L2/L3 source file mapping + lineage anchors
~~~

These ancillary files are referenced by all SMAP STAC Collections:

- `soil-moisture/collection.json`  
- `freeze-thaw/collection.json`  
- `vegetation-water/collection.json`  
- `qa-flags/collection.json`  

---

## 🧩 3. Ancillary File Requirements (KFM-STAC v11)

### 🛰️ orbit-tracks.json
Must include:

- Orbit track geometry  
- Ascending / descending pass indicators  
- Local Time of Ascending Node (LTAN)  
- Pass-frequency metadata  
- Swath width and overlap  
- PROV-O `prov:used` references to NASA spacecraft identifiers  

---

### 🗺️ ease-grid-2.0.json
Contains mandatory grid definitions:

- CRS parameters (equal-area EASE-Grid 2.0)  
- Shape, transform, resolution  
- Cell area metadata  
- Relationship to KFM CRS  
- JSON-LD context link for projection metadata  

---

### 🎚️ calibration.json
Defines:

- Radiometer calibration coefficients  
- Drift corrections  
- Performance changes over mission lifetime  
- QA thresholds  
- Care-required fields where calibration uncertainty could imply sensitive environmental interpretation  

---

### 📐 sensor-geometry.json
Includes:

- Incidence angle  
- Beam footprint and shape  
- Brightness temperature pattern  
- Swath geometry  
- Application guidance for freeze–thaw and soil-moisture corrections  

---

### 🧭 radiometer-modes.json
Specifies:

- All operational radiometer modes  
- Known transitions  
- Mode-dependent uncertainty assumptions  
- Interaction with QA flags  
- Documentation for STAC `kfm:state` logic  

---

### 🔗 provenance-map.json
Contains:

- NASA L1–L3 source product mapping  
- DOIs  
- Version references  
- PROV-O lineage chains for:
  - soil moisture  
  - freeze–thaw  
  - VWC  
  - QA/RFI  
- Required for full reproducibility  

---

## 🔐 4. Governance & Sovereignty

Ancillary metadata interacts with governance rules when:

- Radiometer performance biases map to sensitive land behaviors  
- Freeze–thaw transitions intersect tribal landscapes  
- Calibration or uncertainty structures reveal land-use cycles  

KFM enforces:

- CARE-A/B classification  
- Sovereignty review for grid or orbit metadata involving protected lands  
- `"kfm:mask_applied": true` where masking required  
- No speculative calibration or sensor geometry fields  

Governance validated via:

- `faircare_validate.yml`  
- `stac_validate.yml`  
- `jsonld_validate.yml`  

---

## 🧪 5. QA & Validation

Ancillary metadata undergoes:

- JSON Schema validation  
- Semantic conformance with KFM-STAC v11  
- Geometry validation (orbit track polygons / lines)  
- CRS validation  
- Cross-checks with NASA OPeNDAP sources  
- Internal consistency tests (grid + orbit + calibration)  

Errors block ingestion pipelines.

---

## 🔁 6. Ingestion → Lineage Workflow

```
NASA SMAP Mission Ancillary Data
 → decode / ingest
 → harmonize to KFM-STAC ancillary schema
 → validate orbit + grid + calibration
 → attach PROV-O lineage (prov:Entity → prov:Plan)
 → publish to STAC Collections
 → OpenLineage + Telemetry export
```

---

## 🔮 7. Applications Inside KFM

### Hydrology  
- Soil moisture correction  
- Freeze–thaw anomaly interpretation  

### Climate  
- Seasonal radiometer consistency  
- VWC environmental context alignment  

### Ecology  
- Vegetation modeling refinements  

### Archaeology  
- Vegetation masking & hydrology-informed risk analysis  

### Story Node v3  
- Environmental reliability context  

### Focus Mode v3  
- Provide “why/why not reliable” explanations for environmental layers  

---

## 🧭 8. Version History

| Version | Date       | Summary                                                                                              |
|--------:|------------|------------------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-29 | Complete ancillary README; emoji directory; governance/H3 integration; STAC v11 validation; CI-safe. |
| v10.3.2 | 2025-11-14 | Pre-v11 ancillary skeleton.                                                                          |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅️ Back](../README.md) · [🗂️ SMAP STAC Home](../README.md) · [🛡 Governance](../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

