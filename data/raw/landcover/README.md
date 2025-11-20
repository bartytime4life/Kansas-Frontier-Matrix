---
title: "🌿 Kansas Frontier Matrix — Raw Landcover Data (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "data/raw/landcover/README.md"

version: "v11.0.0"
last_updated: "2025-11-19"
release_stage: "Stable / Governed"
review_cycle: "Continuous · FAIR+CARE Council Oversight"
lifecycle: "Long-Term Support (LTS)"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"
doc_uuid: "urn:kfm:doc:data-raw-landcover-v11.0.0"
semantic_document_id: "kfm-doc-data-raw-landcover-readme"
event_source_id: "ledger:data/raw/landcover/README.md"
immutability_status: "version-pinned"

sbom_ref: "../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../releases/v11.0.0/manifest.zip"
data_contract_ref: "../../../docs/contracts/data-contract-v3.json"

telemetry_ref: "../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/data-raw-landcover-v11.json"
energy_schema: "../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "Public Domain / Open Data Commons"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0"
ontology_protocol_version: "KFM-OP v11.0"
pipeline_contract_version: "KFM-PDC v11.0"

status: "Active / Enforced"
doc_kind: "Domain Architecture"
intent: "raw-landcover-data"
role: "raw-landcover-domain"
category: "Data · Raw · Landcover · FAIR+CARE"

fair_category: "F1-A1-I1-R1"
care_label: "Low–Moderate (ecological sensitivity varies by dataset)"
sensitivity_level: "Dataset-dependent"
indigenous_rights_flag: "Dataset-dependent"
public_exposure_risk: "Dataset-dependent"
redaction_required: false
data_steward: "KFM FAIR+CARE Council"
risk_category: "Low–Moderate"

ontology_alignment:
  cidoc: "E73 Information Object"
  schema_org: "Dataset"
  owl_time: "TemporalEntity"
  prov_o: "prov:Entity"
  geosparql: "geo:FeatureCollection"

json_schema_ref: "../../../schemas/json/data-raw-landcover-readme-v11.schema.json"
shape_schema_ref: "../../../schemas/shacl/data-raw-landcover-readme-v11-shape.ttl"

ai_training_inclusion: false
ai_focusmode_usage: "Restricted"
ai_transform_permissions:
  - "summaries"
  - "semantic-highlighting"
  - "a11y-adaptations"
ai_transform_prohibited:
  - "speculative"
  - "unverified historical claims"

machine_extractable: true
classification: "Public Data / Low Sensitivity"
jurisdiction: "Kansas / United States"
accessibility_compliance: "WCAG 2.1 AA"
ttl_policy: "Permanent"
sunset_policy: "Superseded upon next raw-landcover-domain update"
---

<div align="center">

# 🌿 Kansas Frontier Matrix — **Raw Landcover Data**  
`data/raw/landcover/README.md`

**Purpose**  
Immutable repository for **unaltered vegetation, soil, and surface classification datasets** from:

- NASA (MODIS / VIIRS / Landsat)  
- USGS (NLCD)  
- ESA / Copernicus (GLC / CCI)  
- Kansas DASC / KGS partners  

This layer provides foundational inputs for:

- NDVI analysis & vegetation monitoring  
- Land-use / landcover classification and change detection  
- Canopy-cover trends and ecological indicators  
- FAIR+CARE-governed Focus Mode v3 land systems narratives  

All sources are preserved with **checksums**, **provenance**, **licensing**, and **FAIR+CARE pre-audit** metadata.

</div>

---

## 1. 📘 Overview

The **Raw Landcover Data Layer** stores **original, unmodified geospatial datasets** that describe Kansas landcover, vegetation, and soil/surface characteristics.

Key properties:

- Files are stored exactly as delivered — **no re-projection, resampling, or clipping**.  
- Each file has **SHA-256 integrity logs** and **license metadata**.  
- FAIR+CARE pre-audits document sensitivity, community implications, and attribution.  
- This layer is the **canonical origin** for all landcover-related ETL pipelines and processed products.

---

## 2. 🗂️ Directory Layout (GitHub-Safe)

~~~~text
data/raw/landcover/
├── README.md
│
├── nlcd_landcover_2021.tif                ← USGS NLCD 2021 landcover (Kansas)
├── modis_ndvi_2025.tif                    ← MODIS NDVI composite imagery
├── viirs_ndvi_2025.tif                    ← VIIRS NDVI composite imagery
├── landsat_surface_reflectance.tif        ← Landsat 8/9 surface reflectance
├── copernicus_landcover_2025.geojson      ← Copernicus GLC vegetation classes
├── soil_moisture_surface_esa_2025.tif     ← ESA CCI surface soil moisture
│
├── metadata.json                          ← checksums, provenance, FAIR+CARE pre-audit refs
└── source_licenses.json                   ← per-provider licensing & attribution notes
~~~~

Each file path must be:

- Registered in `metadata.json` with checksum, license, and provenance.  
- Referenced by any downstream staging/processed landcover pipelines.  

---

## 3. 🧭 Data Acquisition Summary

| Dataset                  | Source / Provider      | Resolution | Format   | License        | Integrity |
|--------------------------|------------------------|-----------:|----------|----------------|----------:|
| NLCD Landcover 2021      | USGS NLCD             | 30 m       | GeoTIFF  | Public Domain  | ✅        |
| MODIS NDVI 2025          | NASA MODIS (MOD13)    | 250 m      | GeoTIFF  | Public Domain  | ✅        |
| VIIRS NDVI 2025          | NASA VIIRS (VNP13)    | 500 m      | GeoTIFF  | Public Domain  | ✅        |
| Landsat Surface Reflect. | NASA / USGS           | 30 m       | GeoTIFF  | Public Domain  | ✅        |
| Copernicus GLC 2025      | ESA Copernicus GLC    | 100 m      | GeoJSON  | Open Data      | ✅        |
| ESA Soil Moisture 2025   | ESA CCI               | 0.25°      | GeoTIFF  | Open Data      | ✅        |

---

## 4. 🧩 Example Source Metadata Record

~~~~json
{
  "id": "modis_ndvi_2025_raw",
  "domain": "landcover",
  "source": "NASA MODIS MOD13 NDVI Product",
  "data_url": "https://lpdaac.usgs.gov/products/mod13a1v061/",
  "provider": "NASA LP DAAC / USGS EROS",
  "format": "GeoTIFF",
  "license": "Public Domain (NASA)",
  "records_fetched": 1,
  "checksum_sha256": "sha256:7b6e214bb5c5d67ea4db8afc1a2d9bba9f08e276ccf3d0a1d4d8e2e41f59b4af",
  "retrieved_on": "2025-11-12T20:48:00Z",
  "validator": "@kfm-landcover-lab",
  "faircare_preaudit": {
    "sensitivity": "none",
    "license_review": "ok",
    "community_flags": []
  },
  "governance_ref": "docs/reports/audit/data_provenance_ledger.json"
}
~~~~

---

## 5. ⚖️ FAIR+CARE Compliance Matrix

| Principle            | Implementation                                                          | Oversight             |
|----------------------|-------------------------------------------------------------------------|-----------------------|
| 🔍 **Findable**      | STAC/DCAT index and JSON-LD in `data/raw/metadata/`.                    | `@kfm-data`           |
| 🔓 **Accessible**    | Public domain / open data; download and API usage documented.          | `@kfm-accessibility`  |
| 🔗 **Interoperable** | CRS information preserved; standard GeoTIFF/GeoJSON formats.           | `@kfm-architecture`   |
| 🔁 **Reusable**      | Complete source, checksum, and license metadata.                        | `@kfm-design`         |
| 🤝 **Collective Benefit** | Datasets support ecological, agricultural, and climate resilience. | `@faircare-council`   |
| 🛡️ **Authority**     | FAIR+CARE Council reviews ingestion ethics and licensing.              | `@kfm-governance`     |
| 📋 **Responsibility**| Data stewards validate metadata completeness and checksums.             | `@kfm-security`       |
| 🧠 **Ethics**        | Sensitive ecological sites may be masked in downstream layers.          | `@kfm-ethics`         |

---

## 6. 🔐 Integrity & Cataloging

### 6.1 Checksum Verification

Checksums computed for each raw landcover file are stored in:

~~~~text
data/raw/landcover/metadata.json
data/checksums/manifest.json
~~~~

Each record includes:

- `file` — relative path under `data/raw/landcover/`  
- `checksum_sha256` — SHA-256 hash with `sha256-` prefix  
- `validated` — whether verified against upstream hash (if provided)  
- `verified_on` — timestamp  

### 6.2 License & Attribution

Licensing and attribution metadata are recorded in:

~~~~text
data/raw/landcover/source_licenses.json
~~~~

Entries must:

- Preserve upstream license text or official statement  
- List required attribution lines (if any)  
- Flag any restrictions or terms beyond public/open data defaults  

### 6.3 Catalog Hooks

Raw landcover sources may be:

- Referenced as **upstream STAC Collections** for processed items  
- Declared as **source datasets** in DCAT JSON-LD, linked from downstream distributions  

---

## 7. ♻️ Retention & Sustainability

| Data Type           | Retention | Policy                                             |
|---------------------|----------:|----------------------------------------------------|
| Raw Landcover Data  | Permanent | Immutable archival; never modified in-place        |
| Source Metadata     | Permanent | ISO 19115 lineage and FAIR+CARE audit retention    |
| Checksum Records    | Permanent | Evidence for integrity & compliance audits         |
| FAIR+CARE Pre-Audits| 5 years   | Ethics & licensing review archive                  |
| Ingestion Logs      | 365 days  | Rotated per CI/CD and governance policy            |

Retention rules are defined in:

~~~~text
data/raw/metadata/raw_data_retention.yml
~~~~

---

## 8. 🌱 Telemetry & Sustainability Metrics

Ingestion telemetry for the raw landcover domain includes:

- `energy_wh` — estimated energy per ingestion run  
- `carbon_gCO2e` — carbon footprint estimate  
- `files_ingested` — number of raw landcover files added/updated  
- `validation_failures` — ingestion-time issues (e.g., checksum mismatch)  

Telemetry outputs:

~~~~text
releases/v11.0.0/focus-telemetry.json
docs/reports/telemetry/data-raw-landcover-v11.json
~~~~

These metrics support:

- Sustainability analysis  
- Infrastructure tuning  
- Governance reporting  

---

## 9. 🧾 Internal Use Citation

~~~~text
Kansas Frontier Matrix (2025). Raw Landcover Data (v11.0.0).
Unaltered landcover, vegetation, soil, and surface datasets from NASA, USGS,
ESA/Copernicus, and Kansas partners, providing FAIR+CARE-governed baselines
for downstream ETL, modeling, and Focus Mode v3 land systems analytics.
~~~~

---

## 10. 🕰 Version History

| Version | Date       | Summary                                                                                                   |
|--------:|------------|-----------------------------------------------------------------------------------------------------------|
| v11.0.0 | 2025-11-19 | Upgraded to v11; telemetry v4, FAIR+CARE pre-audits v11, ROOT-GOVERNANCE alignment, sustainability metrics.|
| v10.2.2 | 2025-11-12 | Streaming STAC for NDVI feeds, telemetry v2, expanded FAIR+CARE pre-audit fields.                        |
| v10.0.0 | 2025-11-09 | Initial v10 raw landcover spec; telemetry hooks and license audits added.                                |

<div align="center">

**Kansas Frontier Matrix — Raw Landcover Data Layer**  
🌿 Environmental Integrity · ⚖️ FAIR+CARE Governance · 🧬 Provenance Assurance  

[⬅️ Back to Raw Data Index](../README.md) ·  
[📐 Data Architecture](../ARCHITECTURE.md) ·  
[⚖️ Governance Charter](../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>