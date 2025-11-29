---
title: "🌿 NASA SMAP — Vegetation Water Content (VWC) STAC Layer (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/data/satellites/smap/stac/vegetation-water/README.md"
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

sbom_ref: "../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../releases/v11.2.2/data-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/sat-smap-vwc-v11.json"

governance_ref: "../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"

classification: "Public Dataset Overview"
fair_category: "F1-A1-I1-R2"
care_label: "CARE-A / CARE-B (variable-dependent)"
indigenous_rights_flag: true
sensitivity_level: "Low (raw) / Medium (derived biomass & land-use transitions)"
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

json_schema_ref: "../../../../../schemas/json/stac-smap-vwc-v11.schema.json"
shape_schema_ref: "../../../../../schemas/shacl/stac-smap-vwc-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:smap:vwc:stac-readme:v11.2.2"
semantic_document_id: "kfm-doc-data-smap-vwc-stac"
event_source_id: "ledger:docs/data/satellites/smap/stac/vegetation-water/README.md"
immutability_status: "version-pinned"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
ttl_policy: "24 months"
sunset_policy: "Superseded upon next VWC STAC revision"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 🌿 **NASA SMAP — Vegetation Water Content (VWC) STAC Collection (KFM v11.2.2)**  
`docs/data/satellites/smap/stac/vegetation-water/README.md`

**Purpose**  
Document the **Vegetation Water Content (VWC)** STAC Collection + Items for NASA SMAP  
within the Kansas Frontier Matrix (KFM).  
VWC is essential for understanding **soil–vegetation interactions**,  
**biomass changes**, **site visibility**, **fire risk**,  
and **Story Node v3 environmental narratives**.

</div>

---

## 📘 1. Overview

The SMAP **Vegetation Water Content** STAC layer provides:

- 🌿 **Vegetation water content (VWC)**  
- 🌾 **Biomass moisture indicators**  
- 🔥 **Vegetation stress precursors**  
- 🌀 **Hydrologic coupling** with SMAP soil moisture  
- ⚠️ **RFI & quality flags**  
- 📉 **Uncertainty surfaces**  
- 🧾 **Orbit, grid, and calibration metadata**  

All Items in this product line:

- Are **STAC 1.x compliant**  
- Include **JSON-LD** (schema.org + GeoSPARQL + OWL-Time)  
- Export **PROV-O lineage**  
- Are governed under **CARE-A/B + H3 sovereignty masking**  
- Are mapped to **EASE-Grid 2.0**  
- Are stored as **COG assets** (primary + QA + uncertainty)  

---

## 🗂️ 2. Directory Layout (Emoji-Rich · Option A)

~~~text
docs/data/satellites/smap/stac/vegetation-water/
├── 📄 README.md                         # This file
│
├── 📦 collection.json                   # SMAP VWC STAC Collection
│
├── 📅 2025/                              # Example year directory
│   ├── 2025-01-01-item.json             # Daily/3-day VWC Items
│   ├── 2025-01-02-item.json
│   └── ...                              # Entire year’s worth of Items
│
└── 🗃️ assets/                           # Common asset repository
    ├── 🌿 vegetation-water.tif          # VWC raster
    ├── 📈 vegetation-uncertainty.tif    # Uncertainty raster
    ├── ⚠️ qa-flags.tif                  # QA/RFI mask
    └── 🧾 metadata.json                 # Orbit/grid/provenance metadata
~~~

---

## 🧩 3. STAC Collection Specification (KFM-STAC v11)

The **VWC collection.json** MUST include:

- `"type": "Collection"`  
- `"id": "smap-vegetation-water"`  
- `"title": "NASA SMAP Vegetation Water Content (VWC)"`  
- `extent.spatial` → global  
- `extent.temporal` → mission lifetime (2015 → present)  
- `kfm:governance` metadata  
- `kfm:lineage` PROV-O chain  
- Required extensions:
  - `proj`  
  - `raster`  
  - `sat`  
  - `kfm-gov`  
  - `kfm-provenance`  
  - `kfm-qa`  

---

## 🧩 4. STAC Item Specification (Daily / 3-Day Items)

Each Item **must** include:

### Core Fields
- `"type": "Feature"`  
- `"id": "smap-vwc-YYYY-MM-DD"`  
- `collection: "smap-vegetation-water"`  
- GeoJSON `geometry` + `bbox`  
- Temporal fields (ISO8601 or interval)  
- `kfm:unit: "kg/m²"` or `"dimensionless"` (depending on SMAP variant)  
- `kfm:uncertainty`  
- `kfm:qa_flags`  
- `kfm:care_label`  
- `kfm:sovereignty_note`  
- `kfm:mask_applied` (H3 generalization flag)  
- `kfm:lineage` (PROV-O entity mapping)

### Required Asset Roles
- `data` → VWC raster  
- `uncertainty` → uncertainty raster  
- `qa` → QA/RFI mask  
- `metadata` → ancillary orbit/grid metadata  

---

## 🔐 5. Governance & Sovereignty

Vegetation & biomass patterns can reveal:

- land-management practices  
- ecological stress  
- culturally sensitive land transitions  
- potential archaeological exposure or risk  

Thus KFM enforces:

- **CARE-A/B** applicability  
- **Dynamic H3 masking** in sensitive Indigenous territories  
- `"kfm:mask_applied": true` when generalization is active  
- Full provenance + uncertainty disclosure  

All Items must pass governance validation:

- `faircare_validate.yml`  
- `stac_validate.yml`  
- `jsonld_validate.yml`  

---

## 🧪 6. QA & Validation

Validation checks include:

- COG structure & band metadata  
- Raster alignment (data, QA, uncertainty)  
- BBox + geometry cross-checks  
- Temporal continuity  
- Cross-sensor QA vs:
  - SMAP soil moisture  
  - HydroGNSS biomass/wetness indicators  
  - Landsat/Sentinel NDVI/EVI  
  - VIIRS fire/thermal signals  
  - ERA5 vegetation + surface fluxes  

QA results stored under:

`docs/data/satellites/smap/qa/`

Telemetry exported to:

`releases/<version>/data-telemetry.json`

---

## 🔁 7. Ingestion → Lineage Workflow

```
NASA SMAP L3 Radiometer Product
 → decode + EASE-Grid mapping
 → RFI & QA mask integration
 → vegetation water retrieval
 → uncertainty propagation
 → STAC Item assembly
 → CARE/H3 review
 → PROV-O lineage export
 → STAC/DCAT registration
 → OpenLineage + Telemetry export
```

All steps are **WAL-protected** and deterministic.

---

## 🔮 8. Applications Inside KFM

### 🌡️ Climate
- Vegetation water stress  
- Drought-linked biomass anomalies  

### 🌾 Ecology
- Grassland dynamics  
- Fire-risk indicators  
- Seasonal greenness/hydration cycles  

### 🏺 Archaeology
- Vegetation masking of cultural features  
- Moisture-driven visibility variation  
- Landscape occupation reconstructions  

### Story Node v3  
- Environmental backdrops (vegetation state)  
- Seasonal context for events / narratives  

### Focus Mode v3  
- “Hydro-ecological context” reasoning  
- Multi-sensor vegetation-wetness fusion  

---

## 🧭 9. Version History

| Version | Date       | Summary                                                                                           |
|--------:|------------|---------------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-29 | Full v11.2.2 VWC STAC README; emoji layout; governance/H3 rules; STAC v11 compliance; CI-safe.    |
| v10.3.2 | 2025-11-14 | Pre-v11 minimal structure.                                                                         |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅️ Back](../README.md) · [🗂️ SMAP STAC Home](../README.md) · [🛡 Governance](../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

