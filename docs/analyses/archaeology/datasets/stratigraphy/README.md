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

<div align="center">

# 🪨 **Kansas Frontier Matrix — Archaeology Stratigraphy Dataset Catalog**  
`docs/analyses/archaeology/datasets/stratigraphy/README.md`

**Purpose:**  
Serve as the authoritative, FAIR+CARE-compliant catalog for all **stratigraphic datasets** in the Kansas Frontier Matrix (KFM).  
Defines metadata, generalization rules, CARE masking, STAC alignment, PROV-O provenance, and integration with Story Node v3 & Focus Mode v3.

</div>

---

## 📘 Overview

Stratigraphic datasets in KFM describe:

- Cultural layers  
- Geological horizons  
- Stratigraphic sequences  
- Harris matrices  
- Digitized profile drawings  
- Vertical sampling datasets (C-14, OSL, pollen, phytoliths, charcoal)  
- AI-assisted stratigraphic reconstructions  

All stratigraphy datasets MUST adhere to:

- **STAC 1.0.0** (Items & Collections)  
- **DCAT 3.0** (dataset catalog alignment)  
- **OWL-Time** (temporal intervals)  
- **GeoSPARQL** (geometries)  
- **PROV-O** (lineage & activities)  
- **FAIR + CARE** archaeology ethics  
- KFM dynamic H3 generalization & masking for sensitive locations  

Stratigraphy data feeds:

- **Story Nodes v3** — narratives anchored in specific depositional episodes  
- **Focus Mode v3** — context-aware summaries of sites, layers, and sequences  
- **3D Timeline/Section Views** — vertical time-slices and section visualizations  

---

## 🗂 Directory Layout

Minimalist dash-style layout for stratigraphy datasets:

```text
docs/
- analyses/
  - archaeology/
    - datasets/
      - stratigraphy/
        - README.md
        - collections/
        - items/
        - schemas/
        - examples/
```

### Directory semantics

- `README.md`  
  - This catalog; defines rules, schemas, CI requirements.  

- `collections/`  
  - STAC Collections describing high-level stratigraphy domains.  

- `items/`  
  - Individual STAC Items for profiles, sequences, matrices, and samples.  

- `schemas/`  
  - JSON Schemas for stratigraphy domain, CARE generalization, and provenance.  

- `examples/`  
  - Machine-verifiable example Items for tests, tutorials, and CI fixtures.  

---

## 🔖 Stratigraphy Collections

Official Collections (all under `collections/`):

| Collection ID           | Description                                           | File                                      |
|-------------------------|-------------------------------------------------------|-------------------------------------------|
| stratigraphic-profiles  | Profile drawings, digitized cuts, soil horizons      | `collections/stratigraphic-profiles.json` |
| stratigraphic-sequences | Layer sequences, depositional models, event chains   | `collections/stratigraphic-sequences.json`|
| layer-taxonomy          | Controlled vocabulary for sediments & cultural layers| `collections/layer-taxonomy.json`         |
| vertical-samples        | C-14, OSL, pollen, phytolith, charcoal depth-series  | `collections/vertical-samples.json`       |

Each Collection MUST define:

- **Spatial extent**  
  - Generalized region only (e.g. drainage basin, physiographic province).  
- **Temporal extent**  
  - OWL-Time interval; may be approximate (e.g. 800–1200 CE).  
- **Summaries**  
  - `kfm:layer_type`, `kfm:chronology_method`, `kfm:material_type`, etc.  
- **CARE metadata**  
  - `care:sensitivity`, `care:notes`, `care:review`.  
- **Provenance**  
  - Links to PROV-O bundles and relevant excavation / lab activities.  

---

## 📦 STAC Item Requirements

All stratigraphy Items under `items/` MUST conform to the following:

### Core

- `stac_version: "1.0.0"`  
- `type: "Feature"`  
- `id` — stable, globally unique (KFM-safe, versioned)  
- `geometry` — **generalized** Polygon or MultiPolygon  
- `bbox` — generalized bounding box  
- `properties.start_datetime`  
- `properties.end_datetime`  

### Domain properties (examples)

- `kfm:sequence_id` — stable ID for depositional sequence or profile set  
- `kfm:profile_type` — e.g. `"north-wall"`, `"west-wall"`, `"isolated-test-unit"`  
- `kfm:layer_type` — array of layer tags (from `layer-taxonomy`)  
- `kfm:sample_depth_cm` — depth of samples (numeric or array)  
- `kfm:chronology_method` — e.g. `"radiocarbon"`, `"OSL"`, `"relative-stratigraphy"`  
- `kfm:context_label` — excavation context codes (generalized, non-identifying)  

### CARE properties

- `care:sensitivity` — `"generalized"`, `"masked"`, `"restricted"`  
- `care:notes` — explanation of masking and ethical constraints  
- `care:review` — e.g. `"tribal"`, `"heritage-council"`, `"archaeology-working-group"`  

### Assets

- `assets.data` — main dataset (e.g. profile GeoJSON, matrix file, sample table)  
- `assets.provenance` — PROV-O bundle describing excavation, sampling, and lab work  
- `assets.diagnostics` (optional) — QA outputs, model fits, or stratigraphy checks  

### Required STAC extensions

- `proj` — CRS & projection metadata (even if using EPSG:4326)  
- `version` — Item-level semantic versioning  
- `checksum` — asset checksums, at minimum SHA-256  
- `scientific` — citation, DOIs, related publications  
- `kfm:archaeology` — local KFM archaeology extension (layer, feature, site semantics)  
- `care` — CARE-tagged sensitivity metadata  

---

## 🌍 Spatial & Temporal Rules

### Spatial generalization

To protect sensitive cultural heritage:

- No precise coordinates for:  
  - Excavation units  
  - Feature cuts  
  - Individual layers  
  - Sample points or coring locations  

- Acceptable geometries:  
  - Site-region polygons (e.g. ±5–20 km generalization)  
  - Watershed polygons  
  - County-level or physiographic region footprints  

Generalization MUST be compatible with:

- **KFM dynamic H3 generalization standard**  
- **CARE-Compliant masking** for Indigenous sites and burial locations  

### Temporal representation

- `start_datetime` and `end_datetime` MUST form a valid interval.  
- For approximate intervals, also store:  
  - `kfm:time_precision` — e.g. `"century"`, `"half-century"`, `"year"`  
  - `kfm:time_label` — e.g. `"ca. 800–1200 CE"`  

OWL-Time compatibility:

- Intervals must be mappable to `time:ProperInterval` with `time:hasBeginning` and `time:hasEnd`.  

---

## 🔗 Example Stratigraphy Item (Generalized Profile)

```json
{
  "stac_version": "1.0.0",
  "type": "Feature",
  "id": "kfm-arch-strat-profile-smokyhill-v1",
  "bbox": [-99.8, 38.5, -98.4, 39.4],
  "geometry": {
    "type": "Polygon",
    "coordinates": [[[0.0, 0.0], [1.0, 0.0], [1.0, 1.0], [0.0, 1.0], [0.0, 0.0]]]
  },
  "properties": {
    "start_datetime": "0800-01-01T00:00:00Z",
    "end_datetime": "1200-01-01T00:00:00Z",
    "kfm:profile_type": "north-wall",
    "kfm:layer_type": ["A-horizon", "cultural-layer", "B-horizon"],
    "kfm:chronology_method": "radiocarbon",
    "kfm:sequence_id": "seq-smokyhill-001",
    "kfm:time_precision": "century",
    "kfm:time_label": "ca. 800–1200 CE",
    "kfm:provenance": "provenance/smokyhill-profile-v1.json",
    "care:sensitivity": "generalized",
    "care:notes": "Generalized to multi-county region; unit coordinates masked.",
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
```

---

## 🧪 Validation & CI Requirements

All files in `docs/analyses/archaeology/datasets/stratigraphy/` MUST pass:

- **STAC validation**  
  - Core spec + required extensions.  
- **Stratigraphy domain schema**  
  - `schemas/kfm-archaeology-stratigraphy-schema.json`.  
- **CARE generalization schema**  
  - `schemas/care-generalization-schema.json`.  
- **Provenance schema**  
  - `schemas/provenance-lineage-schema.json`.  
- **Geometry + time checks**  
  - GeoSPARQL-valid geometries.  
  - OWL-Time-valid intervals.  
- **Checksums**  
  - SHA-256 for all `assets.data` and `assets.provenance`.  
- **Focus Mode v3 readiness**  
  - Items must expose enough `kfm:*` fields for entity extraction.  
- **Story Node v3 extraction safety**  
  - Narratives derived from stratigraphy must not expose sensitive coordinates.  

Typical workflows:

- `stac-validate.yml`  
- `stratigraphy-domain-validate.yml`  
- `faircare-audit.yml`  

---

## 🕰 Version History

| Version | Date       | Author                                   | Notes                                  |
|---------|------------|-------------------------------------------|----------------------------------------|
| v11.0.0 | 2025-11-25 | Archaeology Working Group · FAIR+CARE Council | Initial stratigraphy catalog release.   |

---

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
FAIR+CARE · MCP-DL v6.3 · STAC 1.0.0 · DCAT 3.0  

[⬅ Back to Archaeology Datasets](../README.md) ·  
[📑 Metadata Standards](../../../../standards/README.md) ·  
[📘 Master Guide v11](../../../../reference/kfm_v11_master_documentation.md)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~markdown