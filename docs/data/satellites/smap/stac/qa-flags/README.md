---
title: "⚠️ NASA SMAP — QA & RFI Mask STAC Layer (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/data/satellites/smap/stac/qa-flags/README.md"
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
telemetry_schema: "../../../../../schemas/telemetry/sat-smap-qa-v11.json"

governance_ref: "../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"

classification: "Public Dataset Overview"
fair_category: "F1-A1-I2-R2"
care_label: "CARE-A / CARE-B (variable-dependent)"
indigenous_rights_flag: true
sensitivity_level: "Low (raw) / Medium (derived quality metadata)"
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

json_schema_ref: "../../../../../schemas/json/stac-smap-qa-v11.schema.json"
shape_schema_ref: "../../../../../schemas/shacl/stac-smap-qa-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:smap:qa-flags:readme:v11.2.2"
semantic_document_id: "kfm-doc-data-smap-qa-flags"
event_source_id: "ledger:docs/data/satellites/smap/stac/qa-flags/README.md"
immutability_status: "version-pinned"
machine_extractable: true

accessibility_compliance: "WCAG 2.1 AA+"
ttl_policy: "24 months"
sunset_policy: "Superseded upon next QA-flag specification"
jurisdiction: "Kansas / United States"
---

<div align="center">

# ⚠️ **NASA SMAP — QA & RFI Mask STAC Collection (KFM v11.2.2)**  
`docs/data/satellites/smap/stac/qa-flags/README.md`

**Purpose**  
Document the **Quality Assurance (QA) & Radio-Frequency Interference (RFI)**  
mask products for NASA SMAP, provided as a standalone STAC Collection and  
used in soil-moisture, freeze–thaw, and vegetation-water STAC Items.  
These masks ensure safe, reliable, governance-aligned use of SMAP variables  
in KFM’s hydrology, climate, ecology, archaeology, Story Node v3,  
and Focus Mode v3 pipelines.

</div>

---

## 📘 1. Overview

The SMAP QA & RFI mask dataset provides pixel-level indicators for:

- ⚠️ **RFI contamination**  
- 🔧 **Radiometer gain / calibration quality**  
- 🌬️ **Retrieval confidence drops**  
- 🧊 **Potential freeze/wetness ambiguity**  
- 📡 **Sensor & orbit anomalies**  
- 🧪 **Quality flags required by SMAP L2/L3 processing**  

These QA masks are referenced by:

- 🚨 Soil Moisture Items  
- ❄️ Freeze/Thaw Items  
- 🌿 Vegetation Water Content Items  

They act as the **primary quality gate** for KFM’s scientific pipelines.

All STAC Items referencing this product must use:

- `qa` asset role  
- `kfm:qa_flags`  
- `kfm:qa_interpretation`  
- `kfm:qa_flag_schema`  

---

## 🗂️ 2. Directory Layout (Emoji-Rich · Option A)

~~~text
docs/data/satellites/smap/stac/qa-flags/
├── 📄 README.md                        # This file
│
├── 📦 collection.json                  # SMAP QA/RFI STAC Collection definition
│
├── 📅 2025/                             # Example year directory
│   ├── 2025-01-01-item.json            # QA/STAC daily item
│   ├── 2025-01-02-item.json
│   └── ...                             # Full year
│
└── 🗃️ assets/                           # Global QA assets (templates)
    ├── ⚠️ qa-flags.tif                  # QA / RFI mask (primary raster)
    ├── 📈 qa-uncertainty.tif           # Uncertainty / reliability layer
    └── 🧾 metadata.json                # Grid + orbit + provenance metadata
~~~

---

## 🧩 3. STAC Collection Specification (KFM-STAC v11)

The QA Collection must include:

- `"type": "Collection"`  
- `"id": "smap-qa-flags"`  
- `"title": "NASA SMAP QA & RFI Masks"`  
- `extent.spatial` → global  
- `extent.temporal` → 2015 → present  
- `kfm:governance` → CARE/H3/sovereignty metadata  
- `kfm:lineage` → NASA L2/L3 product lineage  
- Required extensions:
  - `raster`
  - `proj`
  - `sat`
  - `kfm-gov`
  - `kfm-qa`
  - `kfm-provenance`

---

## 🧩 4. STAC Item Specification

Every QA Item MUST include:

### Required Properties
- `"type": "Feature"`  
- `"id": "smap-qa-YYYY-MM-DD"`  
- `"collection": "smap-qa-flags"`  
- GeoJSON geometry + BBox  
- `properties.datetime`  
- `kfm:qa_flags`  
- `kfm:qa_interpretation`  
- `kfm:care_label`  
- `kfm:sovereignty_note`  
- `kfm:mask_applied` (H3 generalization)  
- Lineage via `kfm:lineage`

### Required Assets
- **`qa`** → QA mask raster  
- **`uncertainty`** → QA uncertainty raster  
- **`metadata`** → orbit/grid metadata JSON  

These Items are typically used **indirectly** by other SMAP STAC products.

---

## 🔐 5. Governance & Sovereignty

While QA masks are not inherently sensitive, their **derived usage** may be:

- identifying agricultural stress  
- revealing land management practices  
- indicating freeze/wetness transitions near Indigenous lands  

Thus KFM enforces:

- CARE-A/B classification  
- H3 generalization in culturally sensitive areas  
- `"kfm:mask_applied": true` when used in such regions  
- Provenance + uncertainty disclosure in all derivative layers  

Governance validation occurs via:

- `faircare_validate.yml`  
- `stac_validate.yml`  
- `jsonld_validate.yml`  

---

## 🧪 6. QA & Validation

QA Masks undergo:

- COG structural validation  
- Raster/raster alignment with related STAC variables  
- Geometry/BBox consistency  
- Temporal plausibility checks  
- Sensor anomaly checks  
- Cross-sensor QA vs:
  - SMAP soil moisture  
  - SMAP freeze/thaw  
  - SMAP vegetation-water  
  - HydroGNSS wetness indicators  
  - Mesonet QC feeds  
  - ERA5 land-surface diagnostics  

QA results → `docs/data/satellites/smap/qa/`  
Telemetry → `releases/<version>/data-telemetry.json`

---

## 🔁 7. Ingestion → Lineage

```
NASA SMAP L2/L3 QA Product
 → decode + EASE-Grid alignment
 → derive QA mask & RFI indicators
 → propagate uncertainty
 → assemble STAC Item
 → CARE/H3 sovereignty enforcement
 → export lineage (PROV-O)
 → STAC/DCAT registration
 → OpenLineage + OTel telemetry
```

All steps are **WAL-safe, deterministic, and governance-audited**.

---

## 🔮 8. Applications Inside KFM

### Soil Moisture  
- Masking unreliable retrievals  
- Conditioning drought/wetness outputs  

### Freeze/Thaw  
- Identifying RFI-induced false transitions  

### Vegetation Water  
- Filtering biomass/wetness anomalies  
- Removing radiometer artifacts  

### Story Node v3 + Focus Mode v3  
- Ensuring environmental overlays avoid low-quality pixels  
- Better contextual accuracy in environmental narratives  

---

## 🧭 9. Version History

| Version | Date       | Summary                                                                                             |
|--------:|------------|-----------------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-29 | Full STAC v11.2.2 upgrade; emoji layout; CARE/H3 governance; QA schema alignment; CI-safe.          |
| v10.3.2 | 2025-11-14 | Pre-v11 skeleton.                                                                                    |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅️ Back](../README.md) · [🗂️ SMAP STAC Home](../README.md) · [🛡 Governance](../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

