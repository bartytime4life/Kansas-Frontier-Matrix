---
title: "🌐 KFM Validation & Observability — STAC-DCAT Schema Integration Index (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/pipelines/validation-observability/schemas/stac-dcat/README.md"
version: "v11.0.0"
last_updated: "2025-11-21"
review_cycle: "Quarterly / FAIR+CARE Council & Metadata Governance Board"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/stac-dcat-schema-index-v11.json"
governance_ref: "../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active / Reference"
doc_kind: "STAC-DCAT-Index"
intent: "validation-observability-stac-dcat-integration-index"
semantic_document_id: "kfm-stac-dcat-schema-index"
doc_uuid: "urn:kfm:schemas:validation-observability:stac-dcat:index:v11"
machine_extractable: true"
accessibility_compliance: "WCAG 2.1 AA+"
fair_category: "F1-A1-I1-R1"
care_label: "Low-Risk"
immutability_status: "version-pinned"
---

<div align="center">

# 🌐 **STAC-DCAT Schema Integration Index**  
`docs/pipelines/validation-observability/schemas/stac-dcat/README.md`

**Purpose:**  
Provide the **authoritative index** for all **STAC (SpatioTemporal Asset Catalog)** and **DCAT (Data Catalog Vocabulary)** mapping schemas used inside the Kansas Frontier Matrix v11.  
These schemas enable the platform to validate *spatiotemporal dataset metadata* at ingestion time and integrate it into the **Validation & Observability** ecosystem, ensuring full alignment between:

- **STAC 1.x** (Items, Collections, Catalogs)  
- **DCAT 3.0** (Datasets, Distributions)  
- **PROV-O** lineage chains  
- **FAIR+CARE metadata governance**  
- **OWL-Time & GeoSPARQL** spatial-temporal standards  

</div>

---

# 📘 Overview

KFM v11 uses STAC and DCAT **together** to describe all dataset metadata, including:

- Hydrology, climate, and environmental datasets  
- Raster/COG geospatial assets  
- Vector layers, geometries, and Story Node spatial footprints  
- Telemetry datasets (compute/energy/carbon)  
- AI anomaly datasets (drift, bias, reasoning, OOD, sovereignty, etc.)

This directory documents the **JSON Schemas** used to validate:

- **STAC → Graph mappings**  
- **DCAT → FAIR metadata enforcement**  
- **STAC + DCAT → Unified dataset provenance**  
- **STAC Items enriched by anomaly pipelines**  
- **Dataset-level governance requirements**  
- **Story Node v3 spatial/temporal constraints**

Every schema here is CI-validated and contributes to KFM’s metadata reliability guarantees.

---

# 🗂 Directory Layout

```text
docs/pipelines/validation-observability/schemas/stac-dcat/
│
├── README.md                                # This file — schema integration index
│
├── stac/                                    # STAC-only schemas (Items, Collections)
│   ├── stac-item-schema-v11.json
│   ├── stac-collection-schema-v11.json
│   └── stac-catalog-schema-v11.json
│
├── dcat/                                    # DCAT-only schemas
│   ├── dcat-dataset-schema-v11.json
│   ├── dcat-distribution-schema-v11.json
│   └── dcat-catalog-schema-v11.json
│
├── mapping/                                 # STAC ↔ DCAT interoperability schemas
│   ├── stac-to-dcat-mapping-v11.json
│   ├── dcat-to-stac-mapping-v11.json
│   └── dataset-provenance-mapping-v11.json
│
├── enrichment/                              # Extension schemas for KFM enrichments
│   ├── provenance-enrichment-v11.json
│   ├── care-safety-enrichment-v11.json
│   ├── telemetry-enrichment-v11.json
│   └── spatial-temporal-enrichment-v11.json
│
└── validators/                              # CI schema validators
    ├── validate_stac_dcat_map.py
    ├── validate_stac_schema.py
    ├── validate_dcat_schema.py
    └── run_all_validations.sh
```

---

# 🧩 What These Schemas Validate

## 1. 🛰 STAC Structural Integrity  
Ensures:

- Valid `bbox`, `geometry`, CRS  
- Valid `datetime`, `start_datetime`, `end_datetime` (OWL-Time)  
- Complete `assets`, `links`, `providers`  
- Item/Collection semantics  

## 2. 📦 DCAT FAIR Metadata  
Validates:

- Dataset titles, descriptions  
- Licensing & rights metadata  
- Distribution compliance  
- Contact & publisher metadata  
- Theme/category alignment  
- FAIR+CARE requirements  
- Accessibility and attribution  

## 3. 🔗 STAC ↔ DCAT Crosswalk  
Ensures KFM datasets are simultaneously:

- STAC Items/Collections  
- DCAT Datasets/Distributions  

Fields must map:

- `license`  
- `keywords`  
- `spatial/geometries`  
- `temporal extents`  
- `provenance`  
- `asset roles`  
- `descriptions`  

## 4. 🧬 PROV-O Provenance Completeness  
Schemas validate required links:

- `prov:wasGeneratedBy`  
- `prov:used`  
- `prov:Agent` associations  

Critical for:

- Drift/bias anomaly metadata  
- Telemetry datasets  
- Story Node v3 spatial/temporal traces  

## 5. 🧡 CARE-S Integration  
Ensures:

- Tribal/Indigenous data sensitivity metadata exists  
- Sovereignty-related fields present  
- Cultural-risk flags properly encoded  

Mandatory for archaeology & tribal-related datasets.

## 6. ♻ Telemetry & Sustainability Integration  
Schemas require:

- `energy_wh`  
- `carbon_gco2e`  
- Hardware/compute profile metadata  
- Telemetry lineage  
- ISO-aligned sustainability tracking  

---

# 🛠 Example STAC–DCAT Mapping Snippet

```json
{
  "stac:item:id": "hydro_bathymetry_clinton_2022",
  "dcat:dataset:id": "dataset-hydro-bathy-clinton-2022",
  "mapping": {
    "title": "dct:title",
    "description": "dct:description",
    "bbox": "dcat:spatial",
    "datetime": "dct:temporal",
    "license": "dct:license",
    "providers": "dct:publisher",
    "assets": "dcat:distribution",
    "kfm:provenance": "prov:wasGeneratedBy"
  }
}
```

---

# 🧪 CI & Validation Requirements

All schemas under this directory must:

- Pass **JSON Schema meta-validation**  
- Pass **STAC Validator** (via `stac-validate`)  
- Pass **DCAT 3.0 structural validation**  
- Pass **PROV-O shape constraints** (via SHACL)  
- Pass **CARE-S logic** (for sensitive datasets)  
- Use canonical examples stored in:  
  - `docs/pipelines/validation-observability/schemas/examples/`  

GitHub Actions enforcing:

- `stac-dcat-schema-validate.yml`  
- `stac-dcat-mapping-validate.yml`  
- `faircare-schema-gate.yml`  
- `governance-dataset-provenance.yml`  

Any failing schema → **merge blocked**.

---

# 🕰 Version History

| Version | Date | Author | Summary |
|--------:|------|--------|---------|
| v11.0.0 | 2025-11-21 | `@kfm-metadata` | Initial creation of STAC-DCAT schema integration index for KFM v11. |

---

<div align="center">

**Kansas Frontier Matrix — STAC-DCAT Metadata Integration Index**  
*FAIR Metadata · Spatiotemporal Precision · Provenance-Complete Datasets · CARE-S Cultural Safety*

[Back to Schema Index](../README.md) •  
[JSON Schema Index](../json/README.md) •  
[SHACL Index](../shacl/README.md)

</div>