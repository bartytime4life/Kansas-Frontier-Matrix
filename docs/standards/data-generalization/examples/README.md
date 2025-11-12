---
title: "🏺 Kansas Frontier Matrix — Sensitive Data Generalization Examples (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/standards/data-generalization/examples/README.md"
version: "v10.2.2"
last_updated: "2025-11-12"
review_cycle: "Annual / FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../releases/v10.2.0/sbom.spdx.json"
manifest_ref: "../../../../releases/v10.2.0/manifest.zip"
data_contract_ref: "../../../../docs/contracts/data-contract-v3.json"
telemetry_ref: "../../../../releases/v10.2.0/focus-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/data-generalization-v1.json"
governance_ref: "../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC BY-NC 4.0"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 🏺 **Kansas Frontier Matrix — Sensitive Data Generalization Examples**
`docs/standards/data-generalization/examples/README.md`

**Purpose:**  
Provide **concrete, reproducible examples** of spatial and temporal generalization, CARE-aligned metadata patterns, anonymization methods, and STAC/DCAT configurations used for releasing sensitive archaeological or Indigenous datasets within the Kansas Frontier Matrix (KFM).  
All examples are fully compliant with **MCP-DL v6.3**, **FAIR+CARE**, **CIDOC CRM**, and **DCAT 3.0** requirements.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP_v6.3-blue)](../../../README.md)
[![License: CC BY-NC 4.0](https://img.shields.io/badge/License-CC--BY--NC%204.0-green)](../../../../LICENSE)
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Certified-orange)](../../faircare.md)
[![Status](https://img.shields.io/badge/Status-Diamond⁹_Ω_Certified-brightgreen)](../../../../releases/v10.2.0/)
</div>

---

## 📘 Overview

This directory contains **templates and real examples** demonstrating how sensitive cultural, archaeological, or ecological site data may be:

- Spatially generalized (coarsened, randomized, aggregated)  
- Temporally generalized (ranges, eras, aggregated intervals)  
- Ethically governed (CARE authority fields, MOU references)  
- Published via **STAC/DCAT** under appropriate access policies  
- Logged to governance & telemetry systems for transparency  

All examples follow the standards defined in:  
`docs/standards/data-generalization/README.md`

---

## 🗂️ Directory Layout

```plaintext
docs/standards/data-generalization/examples/
├── README.md                           # This file
├── example_generalized_point.json      # Example of 1 km rounded coordinates
├── example_grid_aggregation.geojson    # Example of grid-based centroids
├── example_temporal_generalization.json# Example of 10-year interval aggregation
├── example_care_metadata.json          # Example CARE-compliant metadata block
├── example_dcat_record.json            # DCAT 3.0 aligned sensitive dataset record
└── example_stac_item.json              # STAC Item with generalized geometry + CARE fields
```

---

## 🧭 Example 1 — Coordinate Rounding (1 km Resolution)

### Input (Raw — NEVER published)
```json
{
  "id": "raw_site_001",
  "coordinates": [-95.25793, 38.91326],
  "timestamp": "1875-04-12T00:00:00Z",
  "cultural_note": "Sacred site with ongoing community relevance."
}
```

### Output (Generalized)
```json
{
  "id": "generalized_site_001",
  "coordinates": [-95.26, 38.91],
  "spatialResolutionInMeters": 1000,
  "temporal": "1870–1880",
  "sensitivity_class": "High",
  "care": {
    "status": "approved",
    "reviewer": "FAIR+CARE Council",
    "authority_to_control": "Prairie Band Potawatomi Nation",
    "statement": "Coordinates generalized to 1 km per community request."
  }
}
```

---

## 🧭 Example 2 — Grid Aggregation (10 × 10 km)

```json
{
  "grid_cell": "10km_038_095",
  "centroid": [-95.20, 38.90],
  "count": 14,
  "sensitivity_class": "High",
  "generalization_method": "10km_grid_aggregation"
}
```

---

## 🧭 Example 3 — Randomized Masking (±2 km Buffer)

```json
{
  "id": "masked_site_057",
  "original_precision": "withheld",
  "masked_coordinates": [-95.293, 39.021],
  "masking_radius_meters": 2000,
  "method": "random_offset_within_buffer",
  "sensitivity_class": "Very High"
}
```

---

## 🧭 Example 4 — Temporal Generalization (Decade Range)

```json
{
  "id": "historic_event_223",
  "temporal_generalization": "1850–1860",
  "original_date": "1853-03-09",
  "reason": "CARE ethics review identified cultural sensitivity."
}
```

---

## 🧭 Example 5 — CARE Metadata Block (Template)

```json
{
  "care": {
    "status": "approved",
    "reviewer": "FAIR+CARE Council",
    "authority_to_control": "Kickapoo Tribe in Kansas",
    "date_reviewed": "2025-10-29",
    "statement": "Generalization required for safeguarding culturally sensitive locations.",
    "notes": "Original geometries stored in encrypted archive with tribal-access-only key."
  }
}
```

---

## 🧭 Example 6 — DCAT 3.0 Record (Generalized Dataset)

```json
{
  "@context": "https://www.w3.org/ns/dcat3.jsonld",
  "id": "kfm-sensitive-generalized-2025",
  "type": "Dataset",
  "title": "Generalized Cultural Sites — Northeast Kansas (1 km Masked)",
  "description": "Dataset applying 1 km generalization to culturally sensitive areas, co-produced with tribal partners.",
  "theme": ["Archaeology", "Indigenous Heritage"],
  "license": "CC BY-NC 4.0",
  "accessLevel": "restricted",
  "sensitivityClass": "High",
  "authorityToControl": "Prairie Band Potawatomi Nation",
  "provenance": "Derived from protected high-precision archive under MOU #2025-PBPN-KFM-01.",
  "spatialResolutionInMeters": 1000
}
```

---

## 🧭 Example 7 — STAC Item with Generalized Geometry + CARE Fields

```json
{
  "type": "Feature",
  "stac_version": "1.0.0",
  "id": "kfm-gen-arch-001",
  "bbox": [-95.26, 38.91, -95.24, 38.93],
  "geometry": {
    "type": "Polygon",
    "coordinates": [[
      [-95.26, 38.91],
      [-95.24, 38.91],
      [-95.24, 38.93],
      [-95.26, 38.93],
      [-95.26, 38.91]
    ]]
  },
  "properties": {
    "datetime": "1875-01-01T00:00:00Z",
    "sensitivity_class": "High",
    "generalization_method": "1km_coordinate_rounding",
    "kfm:care_tag": "restricted",
    "care": {
      "status": "approved",
      "reviewer": "FAIR+CARE Council",
      "statement": "Generalized per tribal stewardship guidelines."
    }
  }
}
```

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|---|---|---|---|
| v10.2.2 | 2025-11-12 | FAIR+CARE Council | Added DCAT/STAC examples, expanded metadata blocks, aligned with v10.2.0 telemetry & SBOM paths. |
| v10.0.0 | 2025-11-09 | FAIR+CARE Council | Initial release of generalization examples directory. |

---

<div align="center">

© 2025 Kansas Frontier Matrix Project — CC BY-NC 4.0  
Master Coder Protocol v6.3 · FAIR+CARE Certified · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[Back to Generalization Guide](../README.md) · [Standards Index](../../README.md)

</div>
