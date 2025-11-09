---
title: "🌐 Kansas Frontier Matrix — STAC ↔ DCAT 3.0 Metadata Bridge (FAIR+CARE Integrated)"
path: "docs/guides/data/stac-dcat-bridge.md"
version: "v10.0.0"
last_updated: "2025-11-09"
review_cycle: "Quarterly / FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../releases/v10.0.0/sbom.spdx.json"
manifest_ref: "../../../releases/v10.0.0/manifest.zip"
data_contract_ref: "../../../docs/contracts/data-contract-v3.json"
telemetry_ref: "../../../releases/v10.0.0/focus-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/data-stac-dcat-v1.json"
governance_ref: "../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 🌐 **Kansas Frontier Matrix — STAC ↔ DCAT 3.0 Metadata Bridge**
`docs/guides/data/stac-dcat-bridge.md`

**Purpose:**  
Establish the **translation framework** between **STAC 1.0.0** (SpatioTemporal Asset Catalog) and **W3C DCAT 3.0** metadata for KFM’s datasets, ensuring alignment with **FAIR+CARE**, **ISO 19115**, and **OGC** interoperability principles.  
This bridge allows KFM metadata to interoperate seamlessly with global catalogs while preserving provenance, licensing, and ethical data control.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP_v6.3-blue)](../../README.md)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../../LICENSE)
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Interoperable-orange)](../../../docs/standards/README.md)
[![Status](https://img.shields.io/badge/Status-Stable_Bridge-brightgreen)](../../../releases/)
</div>

---

## 📘 Overview

The **STAC ↔ DCAT Bridge** defines the bi-directional translation of metadata fields between the two standards used in KFM:
- **STAC (OGC)**: Optimized for spatiotemporal assets and geospatial datasets.  
- **DCAT (W3C)**: Designed for open data catalogs and FAIR-aligned interoperability.

This translation layer ensures that:
- Metadata from `data/stac/**` is exported into `data/dcat/**`.  
- FAIR+CARE fields and provenance are synchronized automatically.  
- STAC/DCAT compliance validations run during each dataset release.

---

## 🗂️ Directory Layout

```plaintext
docs/guides/data/
├── stac-dcat-bridge.md                    # This document
src/pipelines/metadata_bridge/
├── convert_stac_to_dcat.py                # STAC → DCAT mapping script
├── convert_dcat_to_stac.py                # DCAT → STAC back-translation
├── validate_stac_dcat_sync.py             # Schema parity validator
├── stac_dcat_map.yaml                     # Field-level mapping specification
└── governance_hooks.py                    # FAIR+CARE telemetry + ledger sync
```

---

## 🧩 STAC ↔ DCAT Field Mapping Table

| STAC Field | DCAT Field | Description |
|-------------|------------|--------------|
| `id` | `identifier` | Unique dataset identifier |
| `type` | `type` | Dataset class |
| `stac_version` | `dcat:version` | Metadata schema version |
| `description` | `description` | Dataset abstract |
| `bbox` | `spatial/geographicBoundingBox` | Geographic extent |
| `datetime` | `temporal/startDate`, `temporal/endDate` | Temporal extent |
| `properties.license` | `license` | License (SPDX / CC) |
| `assets.href` | `distribution.downloadURL` | Asset file location |
| `assets.type` | `distribution.mediaType` | File format |
| `keywords` | `theme` | Topical classification |
| `providers` | `publisher` | Organization name |
| `created` | `issued` | Publication date |
| `updated` | `modified` | Last updated |
| `provenance` | `dct:provenance` | Source lineage |
| `faircare` | `dct:rights` | FAIR+CARE ethics metadata |

---

## ⚙️ Example Conversion (STAC → DCAT)

```bash
python src/pipelines/metadata_bridge/convert_stac_to_dcat.py \
  --input data/stac/hydrology.json \
  --output data/dcat/hydrology-dcat.json \
  --mapping src/pipelines/metadata_bridge/stac_dcat_map.yaml
```

**Output:**  
`data/dcat/hydrology-dcat.json` containing FAIR+CARE-validated DCAT 3.0 metadata.

---

## 🧾 Example: STAC Item → DCAT Dataset

**Input (STAC)**

```json
{
  "stac_version": "1.0.0",
  "type": "Feature",
  "id": "kfm-climate-2025-001",
  "properties": {
    "datetime": "2025-11-09T00:00:00Z",
    "license": "CC-BY 4.0"
  },
  "bbox": [-102.05, 37.0, -94.6, 40.0],
  "assets": {
    "data": {
      "href": "https://data.kfm.org/tiles/climate.tif",
      "type": "image/tiff; application=geotiff"
    }
  },
  "collection": "climate_v10"
}
```

**Output (DCAT 3.0)**

```json
{
  "@context": "https://www.w3.org/ns/dcat3.jsonld",
  "id": "kfm-climate-2025-001",
  "type": "Dataset",
  "title": "Kansas Climate Surface Temperature 2025",
  "description": "Gridded raster dataset of mean surface temperature across Kansas for 2025.",
  "spatial": {
    "bbox": [-102.05, 37.0, -94.6, 40.0],
    "crs": "EPSG:4326"
  },
  "temporal": {
    "startDate": "2025-01-01T00:00:00Z",
    "endDate": "2025-12-31T00:00:00Z"
  },
  "distribution": [{
    "downloadURL": "https://data.kfm.org/tiles/climate.tif",
    "mediaType": "image/tiff; application=geotiff"
  }],
  "license": "CC-BY 4.0",
  "provenance": {
    "wasGeneratedBy": "src/pipelines/etl/climate/process_climate_data.py",
    "sha256": "4fe3e6f7..."
  },
  "rights": "FAIR+CARE compliant; reviewed by Council"
}
```

---

## 🧮 Validation Workflows

| Workflow | Purpose | Output |
|-----------|----------|--------|
| `stac-dcat-validate.yml` | Check field-level consistency | `reports/stac-dcat-validation.json` |
| `stac-validate.yml` | Validate STAC 1.0 schema | `reports/stac-validation.json` |
| `dcat-validate.yml` | Validate DCAT 3.0 schema | `reports/dcat-validation.json` |
| `faircare-validate.yml` | Audit FAIR+CARE metadata | `reports/faircare/metadata-audit.json` |
| `ledger-sync.yml` | Append metadata hashes to governance ledger | `docs/standards/governance/LEDGER/metadata-ledger.json` |

---

## ⚖️ FAIR+CARE Integration Mapping

| Principle | Implementation | Audit Source |
|------------|----------------|---------------|
| **Findable** | Dataset IDs synchronized across STAC/DCAT | `stac-dcat-validation.json` |
| **Accessible** | Metadata hosted in JSON-LD under open license | `data/dcat/` |
| **Interoperable** | Shared schema field mapping for cross-platform search | `stac_dcat_map.yaml` |
| **Reusable** | Provenance fields & checksum references retained | Governance ledger |
| **Collective Benefit** | Open interoperability for scientific & cultural use | FAIR+CARE audit |
| **Authority to Control** | Council-verified metadata publication rights | `faircare-validate.yml` |
| **Responsibility** | Ethics + consent embedded in metadata fields | `telemetry_schema` |
| **Ethics** | Restricts exposure of culturally sensitive data | `data-generalization/README.md` |

---

## 🧩 Governance Ledger Record

```json
{
  "ledger_id": "metadata-bridge-2025-11-09-0001",
  "source_stac": "data/stac/climate.json",
  "target_dcat": "data/dcat/climate-dcat.json",
  "stac_hash": "b6e13f7f3b1...",
  "dcat_hash": "a9f4be72e41...",
  "faircare_status": "Pass",
  "auditor": "FAIR+CARE Council",
  "timestamp": "2025-11-09T12:00:00Z"
}
```

---

## 🔐 Validation Rules

- All metadata pairs must pass both STAC and DCAT schema validations.  
- FAIR+CARE ethical review must precede DCAT publication.  
- Provenance and checksum hashes are logged to the **Governance Ledger**.  
- All temporal and spatial extents must match between standards.  
- Metadata updates are **non-destructive** and version-controlled.

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|----------|------|--------|----------|
| v10.0.0 | 2025-11-09 | Core Team | Added STAC↔DCAT bridge with FAIR+CARE audit and ledger sync |
| v9.7.0 | 2025-11-03 | A. Barta | Initial mapping logic and metadata validation setup |

---

<div align="center">

© 2025 Kansas Frontier Matrix Project  
Master Coder Protocol v6.3 · FAIR+CARE Certified · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[Back to Data Guides](./README.md) · [Governance Charter](../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>

