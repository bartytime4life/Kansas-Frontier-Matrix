---
title: "🏺 Kansas Frontier Matrix — Sensitive Data Generalization Examples (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/standards/data-generalization/examples/README.md"
version: "v11.0.0"
last_updated: "2025-11-20"
review_cycle: "Annual / FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../releases/v11.0.0/manifest.zip"
data_contract_ref: "../../../../docs/standards/data-contracts.md"
telemetry_ref: "../../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/data-generalization-v11.json"
governance_ref: "../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY-NC 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active / Enforced"
doc_kind: "Examples"
intent: "sensitive-site-generalization-examples"
semantic_document_id: "kfm-doc-sensitive-generalization-examples"
doc_uuid: "urn:kfm:docs:heritage:data-generalization-examples-v11.0.0"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
fair_category: "F1-A1-I2-R3"
care_label: "Restricted / High-Sensitivity"
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"
provenance_chain:
  - "docs/standards/data-generalization/examples/README.md@v10.2.2"
ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "TechArticle"
  prov_o: "prov:Plan"
metadata_profiles:
  - "STAC 1.0.0"
  - "DCAT 3.0"
  - "PROV-O"
  - "FAIR+CARE"
story_node_refs: []
ai_training_inclusion: false
ai_focusmode_usage: "Restricted / Governance-Only"
ai_transform_permissions:
  - "summary"
  - "schema-extraction"
ai_transform_prohibited:
  - "content-alteration"
  - "sensitive-detail-expansion"
jurisdiction: "Kansas / United States"
classification: "Restricted"
lifecycle_stage: "stable"
ttl_policy: "24 months"
sunset_policy: "Superseded by next major examples standard version"
---

<div align="center">

# 🏺 **Kansas Frontier Matrix — Sensitive Data Generalization Examples**  
`docs/standards/data-generalization/examples/README.md`

**Purpose:**  
Provide **concrete, reproducible, synthetic examples** of spatial and temporal generalization, CARE-aligned metadata patterns, anonymization methods, and STAC/DCAT configurations used for releasing sensitive archaeological, Indigenous, or ecological datasets within the Kansas Frontier Matrix (KFM).  
All examples are fully aligned with **MCP-DL v6.3**, **KFM-MDP v11.0.0**, **FAIR+CARE**, **CIDOC CRM**, and **DCAT 3.0** requirements, and are **illustrative only** (no real site data).

[![Docs · MCP v6.3](https://img.shields.io/badge/Docs-MCP_v6.3-blue)](../../../README.md)  
[![KFM-MDP v11.0](https://img.shields.io/badge/KFM%E2%80%93MDP-v11.0-informational)]()  
[![License: CC-BY-NC 4.0](https://img.shields.io/badge/License-CC--BY--NC%204.0-green)](../../../../LICENSE)  
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Certified-orange)](../../faircare.md)  
[![Status](https://img.shields.io/badge/Status-Diamond⁹_Ω_Certified-brightgreen)](../../README.md)

</div>

---

## 📘 Overview

This directory contains **templates and synthetic examples** showing how KFM generalizes and governs sensitive cultural, archaeological, or ecological data in practice. Specifically, examples demonstrate:

- Spatial generalization (rounding, grid aggregation, H3 generalization, masking)  
- Temporal generalization (ranges, eras, aggregated intervals)  
- CARE-aligned metadata patterns (authority, review, ethical notes)  
- STAC/DCAT configurations for restricted and generalized datasets  
- Governance ledger integration and telemetry observability patterns  

> ⚠️ **All examples in this document are synthetic and non-locational.**  
> They are provided for **pattern illustration only** and MUST NOT be interpreted as real sites or real coordinates.

All examples are governed by the core standard:

- `docs/standards/data-generalization/README.md`

and the data contract standard:

- `docs/standards/data-contracts.md`

---

## 🗂️ Directory Layout

```text
docs/standards/data-generalization/examples/
├── README.md                           # ← This file (examples index)
├── example_generalized_point.json      # Example of coordinate rounding / H3-like coarse location
├── example_grid_aggregation.geojson    # Example of grid-based aggregation centroids
├── example_temporal_generalization.json# Example of decade-range temporal aggregation
├── example_care_metadata.json          # Example CARE-compliant metadata block
├── example_dcat_record.json            # DCAT 3.0 aligned generalized dataset record
└── example_stac_item.json              # STAC Item with generalized geometry + CARE fields
```

Each file in this directory MUST:

- Be clearly marked as synthetic or illustrative.  
- Avoid using real-world sensitive locations.  
- Follow KFM-MDP v11 Markdown/JSON quality rules.

---

## 🧭 Example 1 — Coordinate Rounding / Coarse Location

> **Goal:** Show how precise coordinates are generalized to a coarser resolution suitable for high-level visualization, while actual site coordinates remain protected in a secure archive.

### ❌ Input (Raw — NEVER published, kept only in Tier-1 secure storage)

```json
{
  "id": "raw_site_001",
  "coordinates": [-95.25793, 38.91326],
  "timestamp": "1875-04-12T00:00:00Z",
  "cultural_note": "Sacred site with ongoing community relevance."
}
```

### ✅ Output (Generalized — Illustrative Only)

```json
{
  "id": "generalized_site_001",
  "coordinates": [-95.26, 38.91],
  "spatialResolutionInMeters": 1000,
  "temporal_generalization": "1870–1880",
  "sensitivity_class": "High",
  "generalization_method": "1km_coordinate_rounding",
  "care": {
    "status": "approved",
    "reviewer": "FAIR+CARE Council",
    "authority_to_control": "Example Tribal Nation",
    "statement": "Coordinates generalized to ~1 km resolution per community guidance.",
    "review_date": "2025-10-29"
  }
}
```

**Key patterns:**

- Raw coordinates are **never** exposed.  
- Published coordinates are coarse approximations only.  
- Temporal dimension generalized to a decade.  
- CARE block records authority and rationale.

---

## 🧭 Example 2 — Grid Aggregation (10 × 10 km)

> **Goal:** Demonstrate spatial aggregation of multiple sites into a single generalized grid cell.

```json
{
  "grid_cell_id": "10km_038_095",
  "centroid": [-95.20, 38.90],
  "site_count": 14,
  "dominant_periods": ["Great Bend Aspect", "Historic Era"],
  "sensitivity_class": "High",
  "generalization_method": "10km_grid_aggregation"
}
```

**Key patterns:**

- No per-site coordinates.  
- Only counts/attributes at grid cell level.  
- Generalization method explicitly documented.

---

## 🧭 Example 3 — Randomized Masking (±2 km Buffer)

> **Goal:** Show how an internal masked location might be represented for quasi-analytic use, under restricted access; **not** for general public release.

```json
{
  "id": "masked_site_057",
  "masking_strategy": "random_offset_within_buffer",
  "masked_coordinates": [-95.293, 39.021],
  "masking_radius_meters": 2000,
  "original_precision": "withheld",
  "sensitivity_class": "Very High",
  "notes": "Masking applied in addition to H3-level aggregation in public outputs."
}
```

**Key patterns:**

- Masking radius is explicit.  
- Original precision is withheld.  
- Intended for internal restricted use; public data may show only H3 cells or grid counts.

---

## 🧭 Example 4 — Temporal Generalization (Decade Range)

> **Goal:** Replace precise dates with coarse temporal ranges where exact timing might carry risk or reveal sensitive patterns.

```json
{
  "id": "historic_event_223",
  "temporal_generalization": "1850–1860",
  "original_date": "1853-03-09",
  "temporal_generalization_method": "decade_range",
  "reason": "CARE ethics review identified cultural sensitivity; decade range preserves interpretability while obscuring exact timing."
}
```

**Key patterns:**

- `original_date` stored only in restricted context, not published.  
- `temporal_generalization` is the value exposed in public/nearly-public outputs.  

---

## 🧭 Example 5 — CARE Metadata Block (Template, Synthetic)

> **Goal:** Provide a reusable CARE block shape for sensitive datasets.

```json
{
  "care": {
    "status": "approved",
    "reviewer": "FAIR+CARE Council",
    "authority_to_control": "Example Tribal Nation",
    "date_reviewed": "2025-10-29",
    "statement": "Generalization required for safeguarding culturally sensitive locations; this dataset has been masked per community guidance.",
    "notes": "Original geometries stored in an encrypted archive with community-controlled access; dataset is classified as 'Restricted / High-Sensitivity'."
  }
}
```

**Key patterns:**

- CARE status explicitly encoded.  
- Authority to control and reviewer recorded.  
- Statement explains why generalization is required.  

---

## 🧭 Example 6 — DCAT 3.0 Record (Generalized Dataset)

> **Goal:** Show a DCAT 3.0-conformant record for a generalized sensitive dataset.

```json
{
  "@context": "https://www.w3.org/ns/dcat3.jsonld",
  "id": "kfm-sensitive-generalized-2025",
  "type": "Dataset",
  "title": "Generalized Cultural Sites — Example Region (1 km Masked)",
  "description": "Dataset applying ~1 km spatial generalization to culturally sensitive areas, co-produced with community partners. Coordinates are approximate and non-locational.",
  "theme": ["Archaeology", "Indigenous Heritage"],
  "license": "CC-BY-NC 4.0",
  "accessLevel": "restricted",
  "sensitivityClass": "High",
  "authorityToControl": "Example Tribal Nation",
  "provenance": "Derived from protected high-precision archive under MOU #2025-EXAMPLE-KFM-01.",
  "spatialResolutionInMeters": 1000
}
```

**Key patterns:**

- `accessLevel = "restricted"` for generalized sensitive dataset.  
- `spatialResolutionInMeters` explicitly signals coarsening.  
- Provenance includes MOU reference and notes that raw coordinates are protected.

---

## 🧭 Example 7 — STAC Item with Generalized Geometry + CARE Fields

> **Goal:** Show a STAC Item pattern with generalized geometry and CARE metadata.

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
    "kfm:h3_generalization": true,
    "kfm:h3_resolution": 7,
    "care": {
      "status": "approved",
      "reviewer": "FAIR+CARE Council",
      "statement": "Generalized per community stewardship guidelines; precise locations withheld.",
      "review_date": "2025-10-29"
    }
  }
}
```

**Key patterns:**

- STAC Item uses coarse bounding geometry instead of site-level points.  
- KFM-specific `kfm:*` properties encode generalization and CARE.  

---

## ⚙️ Validation & CI Expectations for Examples

Even though these are examples:

- All JSON MUST be valid (no trailing commas, correct structure).  
- All Markdown MUST be compliant with KFM-MDP v11.0.0 (`markdown_rules.md`).  
- Example filenames SHOULD match the patterns indicated in the Directory Layout.  
- CI may run `docs-lint.yml` and JSON schema checks on example files to ensure consistency.

When adding new examples:

1. Make sure they are **synthetic/non-real**.  
2. Update the directory tree block if you add new example files.  
3. Do NOT include any real or plausible coordinates of actual sensitive sites.

---

## 🕰️ Version History

| Version | Date       | Author             | Summary                                                                                                             |
|--------:|------------|-------------------|---------------------------------------------------------------------------------------------------------------------|
| v11.0.0 | 2025-11-20 | FAIR+CARE Council | Upgraded to KFM-MDP v11.0.0; added extended YAML, clarified synthetic-only nature, aligned examples with v11 data-contract and generalization rules. |
| v10.2.2 | 2025-11-12 | FAIR+CARE Council | Added DCAT/STAC examples, expanded metadata blocks, aligned with v10.2.0 telemetry & SBOM paths.                   |
| v10.0.0 | 2025-11-09 | FAIR+CARE Council | Initial release of generalization examples directory (v10).                                                         |

---

<div align="center">

🏺 **Kansas Frontier Matrix — Sensitive Data Generalization Examples**  
“All examples here exist to teach patterns, not to reveal places.”

© 2025 Kansas Frontier Matrix — CC-BY-NC 4.0  
Master Coder Protocol v6.3 · FAIR+CARE Certified · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[⬅ Back to Generalization Guide](../README.md) · [⬅ Standards Index](../../README.md)

</div>
