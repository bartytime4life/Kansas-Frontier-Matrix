---
title: "🏺 Kansas Frontier Matrix — Heritage Standards Examples Library (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/standards/heritage/examples/README.md"
version: "v11.0.0"
last_updated: "2025-11-20"
review_cycle: "Annual / FAIR+CARE Council & Focus Mode Board"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/standards-heritage-examples-v11.json"
governance_ref: "../../governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active / Enforced"
doc_kind: "Standard"
intent: "heritage-example-library"
semantic_document_id: "kfm-heritage-examples-library-v11"
doc_uuid: "urn:kfm:docs:standards:heritage:examples:index:v11"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
fair_category: "F1-A1-I1-R1"
care_label: "Protected / High-Risk"
immutability_status: "version-pinned"
---

<div align="center">

# 🏺 **Kansas Frontier Matrix — Heritage Standards Examples Library (v11)**  
`docs/standards/heritage/examples/README.md`

**Purpose:**  
Provide the canonical v11 library of **developer-ready, FAIR+CARE-compliant example files** demonstrating correct usage of all heritage protection schemas: H3 generalization, sensitive-site metadata, lineage & reproducibility, Story Node v3 integration, and STAC/DCAT publication.  
Every example is fully compatible with KFM **Diamond⁹ Ω / Crown∞Ω** heritage requirements and passes all v11 CI validators.

<img alt="Heritage Examples Badge" src="https://img.shields.io/badge/Examples-Heritage_Standards-brown" />
<img alt="FAIR+CARE Compliant Badge" src="https://img.shields.io/badge/FAIR%2BCARE-Compliant-gold" />
<img alt="Protection Level III Badge" src="https://img.shields.io/badge/Protection_Level-III-red" />

</div>

---

# 📘 Overview

This directory contains **fully validated v11 examples** demonstrating:

- ✔ H3 spatial generalization (protected sites → hexes only)  
- ✔ Sensitive-location metadata (CARE, NHPA §304, sovereignty fields)  
- ✔ STAC Item construction with heritage protection fields  
- ✔ DCAT dataset catalog metadata  
- ✔ PROV-O lineage + reproducibility blocks  
- ✔ Story Node v3 metadata for heritage narratives  
- ✔ FAIR+CARE + NHPA-compliant publishing patterns  
- ✔ Complete machine-readable examples used by CI

Every example:

- Conforms to **KFM-MDP v11.0.0**  
- Uses **strict JSON** (no comments, deterministic ordering)  
- Validates against schemas under:  
  `docs/standards/heritage/schemas/`  
- Includes CARE, sovereignty, and protection metadata  
- Is ready for pipeline integration and automated testing  

---

# 🗂 Directory Layout

```text
examples/
│
├── README.md                            # This index file (v11)
│
├── h3-generalization-demo.json          # Example of H3-masked heritage dataset
├── sensitive-location-example.json      # Example protected cultural-site metadata
├── heritage-dataset-stac.json           # STAC Item example (heritage-compliant)
├── heritage-dataset-dcat.json           # DCAT metadata extract (v11)
├── provenance-lineage-example.json      # Example PROV-O lineage metadata
│
└── storynode-heritage-demo.json         # Story Node v3 compliant heritage narrative
```

---

# 🧱 Example — H3 Generalization Output (r7)

```json
{
  "h3_id": "872830829ffffff",
  "h3_resolution": 7,
  "site_count": 4,
  "periods": ["Archaic", "Late Prehistoric"],
  "heritage_protected": true,
  "generalization_method": "H3",
  "raw_coordinates_removed": true,
  "mcp_protected": true,
  "care_level": "Level III"
}
```

---

# 🏺 Example — Sensitive Location Metadata

```json
{
  "id": "KS-ARCH-004198",
  "type": "heritage_site",
  "cultural_sensitivity": "restricted",
  "legal_basis": "NHPA Section 304",
  "care_level": "Level III",
  "tribal_affiliation": ["Kaw Nation"],
  "description": "Earthen mound feature with significant cultural importance.",
  "h3_id": "872830829ffffff",
  "h3_resolution": 7,
  "raw_coordinates_removed": true,
  "mcp_protected": true
}
```

---

# 📦 Example — STAC Item (Heritage)

```json
{
  "stac_version": "1.0.0",
  "type": "Item",
  "id": "ks-heritage-generalized-2025",
  "collection": "kfm-heritage",
  "properties": {
    "heritage_protected": true,
    "care_level": "Level III",
    "generalization_method": "H3",
    "h3_resolution": 7,
    "raw_coordinates_removed": true,
    "mcp_protected": true
  },
  "assets": {
    "hex_geojson": {
      "href": "hexes/ks-heritage-2025.geojson",
      "type": "application/geo+json",
      "roles": ["data"]
    }
  }
}
```

---

# 🗃️ Example — DCAT Metadata Extract

```json
{
  "dct:title": "Kansas Protected Heritage (Generalized to H3-r7)",
  "dct:spatialResolution": "H3-r7",
  "dct:provenance": "Generalized from protected archaeological coordinates.",
  "dct:conformsTo": "KFM Heritage H3 Generalization Standard v11",
  "dct:rights": "NHPA §304 restrictions apply; CARE Level III."
}
```

---

# 🧬 Example — Lineage & Reproducibility

```json
{
  "version": "2025.11.20",
  "lineage": {
    "predecessor": "2025.07.15",
    "successor": "2026.02.01",
    "latest": "2026.02.01"
  },
  "reproducibility": {
    "workflow_hash": "sha256-b94c...",
    "inputs_hash": "sha256-09af...",
    "prov": {
      "wasDerivedFrom": "urn:kfm:raw:heritage:2025-07-15",
      "generatedBy": "urn:kfm:workflow:heritage-generalization-v11"
    }
  }
}
```

---

# 🧩 Example — Story Node v3 (Heritage)

```json
{
  "id": "node-ks-heritage-102",
  "type": "story-node",
  "title": "Ancient Mound Site (Generalized)",
  "heritage_protected": true,
  "cultural_sensitivity": "restricted",
  "periods": ["Late Woodland"],
  "summary": "A generalized representation of an important cultural heritage location.",
  "h3_id": "872830829ffffff",
  "h3_resolution": 7,
  "mcp_protected": true,
  "display_rules": {
    "map": "hex",
    "timeline": true
  },
  "relations": [],
  "spacetime": {
    "geometry": {
      "type": "Point",
      "coordinates": [0, 0]
    },
    "when": {
      "start": "1600-01-01T00:00:00Z",
      "precision": "year"
    }
  }
}
```

---

# 🕰 Version History

| Version  | Date       | Notes                                                                 |
|----------|------------|-----------------------------------------------------------------------|
| v11.0.0  | 2025-11-20 | Full upgrade to KFM-MDP v11.0.0; STAC/DCAT/PROV-O/Story Node v3 aligned. |
| v10.2.3  | 2025-11-13 | Original examples library.                                            |

---

# 🔗 Footer

Return to **Heritage Standards Schemas**:  
`docs/standards/heritage/schemas/README.md`

Return to **Heritage Standards Root**:  
`docs/standards/heritage/README.md`

Return to **Repository Root**:  
`README.JSON files in v11 format.”**