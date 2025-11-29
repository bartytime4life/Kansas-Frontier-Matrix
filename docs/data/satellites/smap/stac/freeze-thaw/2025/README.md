---
title: "❄️ NASA SMAP — Freeze/Thaw STAC Items for 2025 (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/data/satellites/smap/stac/freeze-thaw/2025/README.md"
version: "v11.2.2"
last_updated: "2025-11-29"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Earth Systems · FAIR+CARE Council Oversight"
status: "Active / Enforced"

commit_sha: "<latest-commit>"
previous_version_hash: "<previous-sha>"
doc_integrity_checksum: "<sha256>"

stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"

sbom_ref: "../../../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../../../releases/v11.2.2/data-telemetry.json"
telemetry_schema: "../../../../../../../schemas/telemetry/sat-smap-freeze-v11.json"

governance_ref: "../../../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"

classification: "Public Dataset Overview"
fair_category: "F1-A1-I1-R2"
care_label: "CARE-A / CARE-B (depending on intersection with tribal lands)"
indigenous_rights_flag: true
sensitivity_level: "Low (raw) / Medium (derived transition patterns)"
public_exposure_risk: "Low"
risk_category: "Low"
redaction_required: false

data_steward: "Earth Systems Working Group · KFM FAIR+CARE Council"

ontology_alignment:
  cidoc: "E73 Information Object"
  schema_org: "Dataset"
  prov_o: "prov:Entity"
  owl_time: "ProperInterval"
  geosparql: "geo:FeatureCollection"

json_schema_ref: "../../../../../../../schemas/json/stac-smap-freeze-v11.schema.json"
shape_schema_ref: "../../../../../../../schemas/shacl/stac-smap-freeze-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:smap:freeze-thaw:2025:readme:v11.2.2"
semantic_document_id: "kfm-doc-data-smap-freeze-2025"
event_source_id: "ledger:docs/data/satellites/smap/stac/freeze-thaw/2025/README.md"
immutability_status: "version-pinned"
machine_extractable: true

accessibility_compliance: "WCAG 2.1 AA+"
ttl_policy: "24 months"
sunset_policy: "Superseded upon next SMAP FT year revision"
jurisdiction: "Kansas / United States"
---

<div align="center">

# ❄️ **NASA SMAP — Freeze/Thaw STAC Items (Year 2025)**  
`docs/data/satellites/smap/stac/freeze-thaw/2025/README.md`

**Purpose**  
Provide the governed overview of **year 2025** SMAP Freeze/Thaw (FT) STAC Items:  
daily FT state, uncertainty, RFI/QA flags, and ancillary grid/orbit metadata.  
Fully aligned with **KFM-STAC v11**, FAIR+CARE, sovereignty protections,  
and KFM’s hydrology, climate, ecology, archaeology, and Story Node/Focus Mode v3 layers.

</div>

---

## 📘 1. Overview

The 2025 Freeze/Thaw directory contains:

- ❄️ Daily FT state (frozen / thawed / transitional)  
- ⚠️ RFI + QA masks  
- 📉 Uncertainty surfaces  
- 🧭 Geometry + BBox footprints  
- 🌍 EASE-Grid 2.0 mapped & KFM CRS reharmonized  
- 🔐 CARE/H3 sovereignty masking (where required)  
- 🧾 PROV-O lineage metadata  
- 🧬 JSON-LD enriched Items (schema.org + CIDOC + OWL-Time)  

These Items support:

- Seasonal freeze-line migration analytics  
- Spring runoff & ecohydrology modeling  
- Cultural-landscape hazard narratives in Story Node v3  
- Focus Mode v3 “environmental background” layers  
- Cross-mission comparisons (SMAP soil moisture, HydroGNSS, Mesonet, ERA5)

---

## 🗂️ 2. Directory Layout (Emoji-Rich · Option A)

~~~text
docs/data/satellites/smap/stac/freeze-thaw/2025/
├── 📄 README.md                         # This file
│
├── 📅 2025-01-01-item.json              # Daily FT STAC Items
├── 📅 2025-01-02-item.json
├── 📅 2025-01-03-item.json
├── 📅 ...                                # Continues for entire year
│
└── 🗃️ assets/                            # Shared asset repository for 2025 Items
    ├── ❄️ freeze-thaw.tif               # Primary FT raster
    ├── ⚠️ qa-flags.tif                  # RFI + QC mask
    ├── 📈 freeze-uncertainty.tif        # Uncertainty raster
    └── 🧾 metadata.json                 # Orbit/grid/calibration metadata
~~~

---

## 🧩 3. STAC Item Requirements (KFM-STAC v11)

Each 2025 Item **must** include:

### Core Fields
- `"type": "Feature"`  
- `"id": "smap-ft-2025-<date>"`  
- `"collection": "smap-freeze-thaw"`  
- `geometry` + `bbox`  
- `properties.datetime` (ISO 8601)  
- `kfm:state`: `"frozen" | "thawed" | "transition"`  
- `kfm:uncertainty` (numeric or raster-derived)  
- `kfm:qa_flags`  
- `kfm:care_label`  
- `kfm:sovereignty_note`  
- `kfm:mask_applied` (true/false)  
- `kfm:lineage` (PROV-O linked)

### Required Assets
- `data` → freeze-thaw raster COG  
- `qa` → quality mask COG  
- `uncertainty` → uncertainty raster  
- `metadata` → orbit/grid metadata JSON  

### Required STAC Extensions
- `proj`  
- `raster`  
- `sat`  
- `kfm-gov`  
- `kfm-qa`  
- `kfm-provenance`  

---

## 🔐 4. Governance & Sovereignty

Freeze/Thaw layers can reveal:

- wetland susceptibility  
- land-surface seasonal access  
- infrastructure freeze hazard  
- ecohydrological condition shifts  
- culturally sensitive freeze–thaw exposure

Therefore KFM enforces:

- CARE-A/B labels  
- Sovereignty screening  
- Dynamic **H3 masking** for sensitive tribal lands  
- No precise FT anomalies displayed in protected regions  
- Required provenance/uncertainty in all derivative layers  

All Items must pass:

- `faircare_validate.yml`  
- `stac_validate.yml`  
- `jsonld_validate.yml`  
- `data_pipeline.yml`  

---

## 🧪 5. QA & Validation

Each 2025 Freeze/Thaw STAC Item undergoes:

- JSON Schema validation  
- Geometry + BBox checks (GeoJSON-safe)  
- Temporal validity  
- Raster/COG integrity checks  
- QA flag alignment  
- Cross-sensor QA against:
  - SMAP soil moisture  
  - HydroGNSS  
  - Mesonet freeze state  
  - ERA5-Land freeze-line  

QA results stored in:  
`docs/data/satellites/smap/qa/`

Telemetry exported to:  
`releases/<version>/data-telemetry.json`

---

## 🔁 6. Ingestion → Lineage Pipeline (2025)

```
NASA SMAP L3_FT Product
 → decode + grid mapping
 → QA / RFI masking
 → freeze/thaw classification
 → uncertainty propagation
 → STAC Item assembly
 → CARE/H3 enforcement
 → lineage export (PROV-O)
 → catalog registration (STAC/DCAT)
 → OpenLineage + OTel telemetry
```

---

## 🔮 7. Applications Inside KFM

### Hydrology
- Freeze-line migration  
- Spring thaw analysis  
- Flood risk modeling  

### Climate
- Seasonal climate change indicators  
- Freeze–thaw anomaly mapping  

### Archaeology
- Soil stability & site preservation  
- Seasonal access to landscapes  
- Freeze-related erosion vulnerability  

### Story Node v3 & Focus Mode v3
- Environmental-sequence narratives  
- Seasonal transitions contextualized around events or places  

---

## 🧭 8. Version History

| Version | Date       | Summary                                                                                         |
|--------:|------------|-------------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-29 | Full v11.2.2 upgrade; emoji directory, governance/H3 rules, STAC v11 compliance, QA alignment. |
| v10.3.2 | 2025-11-14 | Pre-v11 minimal structure.                                                                      |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅️ Back](../README.md) · [🗂️ Freeze/Thaw STAC](../README.md) · [🛡 Governance](../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

