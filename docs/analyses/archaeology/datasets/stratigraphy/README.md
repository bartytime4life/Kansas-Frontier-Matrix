---
title: "🪨 Kansas Frontier Matrix — Archaeology Stratigraphy Dataset Catalog (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/datasets/stratigraphy/README.md"
version: "v11.0.0"
last_updated: "2025-11-25"
review_cycle: "Biannual · Archaeology Working Group · FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/archaeology-stratigraphy-v11.json"
governance_ref: "../../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active / Enforced"
doc_kind: "Dataset Catalog"
intent: "archaeology-stratigraphy"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Compliant"
immutability_status: "version-pinned"
semantic_document_id: "kfm-archaeology-stratigraphy-v11"
doc_uuid: "urn:kfm:docs:archaeology:stratigraphy:catalog:v11"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
---

# 🪨 Kansas Frontier Matrix — Archaeology Stratigraphy Dataset Catalog  
`docs/analyses/archaeology/datasets/stratigraphy/README.md`

**Purpose:**  
Serve as the authoritative catalog for all **stratigraphic datasets** in the Kansas Frontier Matrix.  
Defines metadata, generalization, CARE rules, STAC requirements, and integration with Story Node v3 & Focus Mode v3.

---

## 📘 Overview

Stratigraphy datasets in the Kansas Frontier Matrix describe:

- Cultural layers  
- Geological horizons  
- Feature stratigraphic sequences  
- Harris matrices  
- Profile drawings / digitized profiles  
- Vertical sampling datasets (C-14, OSL, pollen, phytoliths, charcoal)  
- AI-assisted stratigraphic reconstructions  

All datasets MUST follow:

- STAC 1.0.0  
- DCAT 3.0  
- OWL-Time  
- GeoSPARQL  
- PROV-O  
- FAIR+CARE archaeology ethics  
- CARE generalization (no sensitive coordinates, no precise feature depths tied to site locations)

---

## 🧱 Directory Layout

docs/  
└── analyses/  
    └── archaeology/  
        └── datasets/  
            └── stratigraphy/  
                ├── README.md  
                ├── collections/  
                │   ├── stratigraphic-profiles.json  
                │   ├── stratigraphic-sequences.json  
                │   ├── layer-taxonomy.json  
                │   └── vertical-samples.json  
                ├── items/  
                │   ├── profile-*.json  
                │   ├── sequence-*.json  
                │   ├── matrix-*.json  
                │   └── sample-*.json  
                ├── schemas/  
                │   ├── kfm-archaeology-stratigraphy-schema.json  
                │   ├── care-generalization-schema.json  
                │   └── provenance-lineage-schema.json  
                └── examples/  
                    ├── example-profile.json  
                    ├── example-matrix.json  
                    └── example-sample.json  

---

## 🔖 Stratigraphy Collections

Stratigraphic datasets are grouped into four official Collections:

| Collection ID | Description | File |
|---------------|-------------|------|
| stratigraphic-profiles | Profile drawings, digitized cuts, soil horizons | `collections/stratigraphic-profiles.json` |
| stratigraphic-sequences | Layer sequences, depositional models | `collections/stratigraphic-sequences.json` |
| layer-taxonomy | Controlled vocabulary for sediment types / cultural layers | `collections/layer-taxonomy.json` |
| vertical-samples | Radiocarbon, OSL, pollen, phytolith, charcoal by depth | `collections/vertical-samples.json` |

Each Collection MUST include:

- `extent.spatial` (generalized)  
- `extent.temporal`  
- `summaries` for layer types, horizons, methods  
- `care:*` metadata  
- Links to Items, provenance bundles, schemas  

---

## 📦 STAC Item Requirements

Every Stratigraphy Item MUST define:

- `stac_version = 1.0.0`  
- `type = Feature`  
- Generalized `geometry` (never exact site or feature coordinates)  
- `bbox` (generalized)  
- `start_datetime` / `end_datetime`  
- Domain fields:  
  - `kfm:layer_type`  
  - `kfm:profile_type`  
  - `kfm:sequence_id`  
  - `kfm:sample_depth_cm`  
  - `kfm:chronology_method`  
- CARE fields:  
  - `care:sensitivity`  
  - `care:notes`  
  - `care:review`  
- Assets:  
  - `data` (profile drawing, layer set, or sample dataset)  
  - `provenance` (PROV-O lineage bundle)

### Required Extensions
- `proj`  
- `version`  
- `checksum`  
- `scientific`  
- `kfm:archaeology`  
- `care`  

---

## 🌍 Spatial & Temporal Rules

- Geometry MUST be **generalized** to region scale.  
- No coordinates for:  
  - Feature cuts  
  - Individual layers  
  - Sample points  
- Depth metadata MAY be included because it does **not** expose spatial location.  
- Temporal ranges MUST use OWL-Time intervals.  
- Approximate date ranges MUST include a human label (e.g., “ca. 800–1200 CE”).

---

## 🔗 Example Stratigraphy Item (Generalized Profile)

    {
      "stac_version": "1.0.0",
      "type": "Feature",
      "id": "kfm-arch-strat-profile-smokyhill-v1",
      "bbox": [-99.8, 38.5, -98.4, 39.4],
      "geometry": {
        "type": "Polygon",
        "coordinates": [[[/* generalized */]]]
      },
      "properties": {
        "start_datetime": "0800-01-01T00:00:00Z",
        "end_datetime": "1200-01-01T00:00:00Z",
        "kfm:profile_type": "north-wall",
        "kfm:layer_type": ["A-horizon", "cultural-layer", "B-horizon"],
        "kfm:chronology_method": "radiocarbon",
        "kfm:provenance": "provenance/smokyhill-profile-v1.json",
        "care:sensitivity": "generalized",
        "care:review": "tribal"
      },
      "assets": {
        "data": {
          "href": "https://example.org/profiles/smokyhill_v1.geojson",
          "type": "application/geo+json",
          "roles": ["data"]
        },
        "provenance": {
          "href": "provenance/smokyhill-profile-v1.json",
          "type": "application/json",
          "roles": ["provenance"]
        }
      },
      "links": [
        { "rel": "collection", "href": "../collections/stratigraphic-profiles.json" },
        { "rel": "root", "href": "../README.md" },
        { "rel": "self", "href": "../items/profile-smokyhill-v1.json" }
      ]
    }

---

## 🧪 Validation & CI Requirements

All files in this directory MUST pass:

- STAC 1.0.0 validation  
- Stratigraphy domain schema validation  
- CARE schema validation  
- PROV-O lineage completeness  
- GeoSPARQL geometry validation  
- OWL-Time interval validity  
- SHA-256 checksums for all assets  
- Focus Mode v3 readiness  
- Story Node v3 extraction safety  
- CI workflow: `stac-validate.yml`

---

## 🕰 Version History

| Version | Date | Author | Notes |
|---------|-------|--------|-------|
| v11.0.0 | 2025-11-25 | Archaeology Working Group · FAIR+CARE Council | Initial stratigraphy catalog release. |

---

**© 2025 Kansas Frontier Matrix — CC-BY 4.0**  
FAIR+CARE · MCP-DL v6.3 · STAC 1.0.0 · DCAT 3.0

[⬅ Back to Archaeology Datasets](../README.md)  
[Metadata Standards](../../../../standards/README.md)  
[Master Guide v11](../../../../reference/kfm_v11_master_documentation.md)