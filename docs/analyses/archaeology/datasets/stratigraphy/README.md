---
title: "🗂️ Kansas Frontier Matrix — Archaeology STAC Catalog (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/datasets/stac/README.md"
version: "v11.0.3"
last_updated: "2025-11-25"
review_cycle: "Biannual · Archaeology Working Group · FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/archaeology-stac-v11.json"
governance_ref: "../../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active / Enforced"
doc_kind: "STAC Catalog"
intent: "archaeology-stac"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Compliant"
immutability_status: "version-pinned"
semantic_document_id: "kfm-archaeology-stac-v11"
doc_uuid: "urn:kfm:docs:archaeology:stac:catalog:v11.0.3"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
---

<div align="center">

# 🗂️ **Kansas Frontier Matrix — Archaeology STAC Catalog (v11.0.3)**  
`docs/analyses/archaeology/datasets/stac/README.md`

**Purpose:**  
Define the authoritative archaeology STAC 1.0.0 catalog for the Kansas Frontier Matrix, ensuring FAIR+CARE compliance, CARE-safe spatial generalization, Focus Mode v3 readiness, and Story Node v3 extraction safety.

</div>

---

## 📘 Overview

This document specifies:

- How archaeology STAC **Collections** and **Items** must be structured  
- Required metadata fields and extensions  
- CARE-compliant generalization of sensitive locations  
- Validation rules enforced by CI  
- How this catalog integrates with Focus Mode v3 and Story Node v3  

Applies to:

- Generalized site gazetteers  
- Public-domain artifact inventories (non-identifying subsets)  
- Cultural landscape / interaction-sphere models  
- Geophysical survey products (magnetometry, GPR, resistivity)  
- Paleoenvironmental datasets (cores, pollen, charcoal, proxies)  
- AI-assisted derived archaeology analytics  

All spatial data MUST be generalized to prevent disclosure of precise site locations.

---

## 🧱 Structure

### 🗂 Directory Layout

```text
docs/
└── analyses/
    └── archaeology/
        └── datasets/
            └── stac/
                ├── README.md
                ├── collections/
                │   ├── site-gazetteers.json
                │   ├── artifact-inventories.json
                │   ├── cultural-landscapes.json
                │   ├── geophysics.json
                │   └── paleoenvironment.json
                ├── items/
                │   ├── site-gazetteer-*.json
                │   ├── artifacts-*.json
                │   ├── landscape-*.json
                │   ├── geophysics-*.json
                │   └── paleo-*.json
                ├── schemas/
                │   ├── kfm-archaeology-schema.json
                │   ├── care-generalization-schema.json
                │   └── provenance-lineage-schema.json
                └── examples/
                    ├── example-generalized-site.json
                    ├── example-landscape.json
                    └── example-paleo.json
```

---

## 🔖 STAC Collections

Each archaeology subdomain MUST define a STAC Collection with:

- Core fields: `id`, `title`, `description`, `keywords`  
- `license`, `providers`  
- `extent.spatial` (CARE-generalized geometry)  
- `extent.temporal` (OWL-Time–compatible interval)  
- `summaries.*` listing key archaeology properties (e.g. culture phases, site types)  
- `care:*` metadata (sensitivity, review)  
- `links` to Items, schemas, provenance, and root catalog  

| Collection            | Purpose                                      | File                                      |
|----------------------|----------------------------------------------|-------------------------------------------|
| Site Gazetteers      | Generalized site-level records               | `collections/site-gazetteers.json`        |
| Artifact Inventories | Public-domain artifact inventory summaries   | `collections/artifact-inventories.json`   |
| Cultural Landscapes  | Interaction spheres and landscape models     | `collections/cultural-landscapes.json`    |
| Geophysics           | Magnetometry, GPR, resistivity datasets      | `collections/geophysics.json`             |
| Paleoenvironment     | Cores, pollen, charcoal, and other proxies   | `collections/paleoenvironment.json`       |

---

## 📦 STAC Item Requirements

### Core Fields

Every archaeology STAC Item MUST include:

| Field | Requirement |
|-------|-------------|
| `stac_version` | `"1.0.0"` |
| `type` | `"Feature"` |
| `id` | Stable, semantic, versioned ID (e.g. `kfm-arch-<domain>-<slug>-vN`) |
| `geometry` | CARE-generalized GeoJSON geometry (never precise) |
| `bbox` | CARE-generalized bounding box |
| `properties` | Time interval and archaeology domain metadata |
| `start_datetime` / `end_datetime` | ISO-8601 datetimes (OWL-Time interval) |
| `assets` | MUST include at least `data` and `provenance` assets |
| `links` | MUST include `root`, `self`, `collection`, and `provenance` |

### Required STAC Extensions

- `proj` — projection metadata  
- `version` — semantic versioning of Items and assets  
- `checksum` — SHA-256 hashes for assets  
- `scientific` — citations, DOIs, references  
- `kfm:archaeology` — domain-specific fields  
- `care` — sensitivity and review metadata  

### Archaeology Extension (`kfm:*`)

These fields live under `properties` and use controlled vocabularies from `kfm-archaeology-schema.json`:

| Field | Description |
|--------|-------------|
| `kfm:culture_phase` | Archaeological period (e.g. “Late Prehistoric”) |
| `kfm:site_type` | Site classification (village, mound, camp, quarry, landscape-region, etc.) |
| `kfm:datatype` | Data type (e.g. `magnetometry-grid`, `artifact-inventory`, `pollen-series`) |
| `kfm:source` | Origin institution / project |
| `kfm:provenance` | Path or URI to PROV-O lineage bundle |

### CARE Extension (`care:*`)

| Field | Description |
|--------|-------------|
| `care:sensitivity` | One of `generalized`, `restricted`, `public` |
| `care:notes` | Non-sensitive explanatory metadata (no coordinates, no identifiers) |
| `care:review` | One of `tribal`, `faircare`, `none-required` |

Rules:

- `restricted` Items MUST NOT be publicly published.  
- Public exports MUST have `care:sensitivity` set to `generalized` or `public`.  
- Where tribal review occurred, `care:review` MUST be `tribal`.  

---

## 🌍 Spatial & Temporal Rules

### CRS and Geometry

- Default CRS: EPSG:4326 (WGS84 lon/lat).  
- If a different CRS is used (e.g., for geophysical grids), it MUST be declared via `proj:*` properties.  
- Geometries MUST be generalized to region scale; **no point-level site geometries**.  

### Generalization (CARE)

- Never publish exact site coordinates.  
- Use:
  - Buffered or enlarged envelopes.  
  - Polygon generalization to county/region scale.  
- When in doubt, choose **coarser generalization** and stricter `care:sensitivity`.  

### Temporal Modeling (OWL-Time)

- `start_datetime` and `end_datetime` MUST be valid ISO-8601 strings.  
- For approximate date ranges:
  - Use a conservative earliest `start_datetime` and latest `end_datetime`.  
  - Add a human-readable label (e.g., `kfm:time_label = "ca. 1200–1450 CE"`).  

---

## 🔗 Example STAC Item (Generalized Cultural Landscape)

```json
{
  "stac_version": "1.0.0",
  "type": "Feature",
  "id": "kfm-arch-landscape-great-bend-v2",
  "bbox": [-101.5, 37.5, -96.0, 39.5],
  "geometry": {
    "type": "Polygon",
    "coordinates": [[[/* generalized geometry elided */]]]
  },
  "properties": {
    "start_datetime": "1200-01-01T00:00:00Z",
    "end_datetime": "1450-01-01T00:00:00Z",
    "kfm:culture_phase": "Late Prehistoric",
    "kfm:site_type": "landscape-region",
    "kfm:datatype": "regional-model",
    "kfm:source": "Example Source Institution",
    "kfm:provenance": "provenance/great-bend-v2.json",
    "care:sensitivity": "generalized",
    "care:notes": "Geometry generalized to protect sensitive archaeological locations.",
    "care:review": "tribal"
  },
  "assets": {
    "data": {
      "href": "https://example.org/data/great_bend_landscape_v2.geojson",
      "type": "application/geo+json",
      "roles": ["data"]
    },
    "provenance": {
      "href": "provenance/great-bend-v2.json",
      "type": "application/json",
      "roles": ["provenance"]
    }
  },
  "links": [
    { "rel": "collection", "href": "../collections/cultural-landscapes.json" },
    { "rel": "root",       "href": "../README.md" },
    { "rel": "self",       "href": "../items/landscape-great-bend-v2.json" }
  ]
}
```

This example is normative for structure; real data MUST supply true geometries, URLs, and provenance.

---

## 🧪 Validation & CI Requirements

All archaeology STAC JSON files MUST pass the following CI checks:

- **STAC 1.0.0 schema validation** for Collections and Items  
- **`kfm-archaeology-schema.json`** validation (domain fields)  
- **`care-generalization-schema.json`** validation (sensitivity and review)  
- **`provenance-lineage-schema.json`** validation (PROV-O bundles)  
- **Checksum verification**: all assets MUST expose SHA-256 digests and match their actual files  
- **GeoSPARQL geometry checks**: no invalid geometries, no self-intersections at published resolution  
- **OWL-Time interval checks**: `start_datetime <= end_datetime`  
- **Focus Mode v3 readiness**: Items expose enough metadata to bind into Focus narratives without leaking restricted details  
- **Story Node v3 extraction safety**: automated narrative generation MUST use only generalized metadata for public Story Nodes  

The CI workflow `stac-validate.yml` MUST be configured to run on every PR that touches this directory and block merges on failure.

---

## 🕰 Version History

| Version | Date       | Author                                  | Notes                                                                 |
|---------|------------|-----------------------------------------|-----------------------------------------------------------------------|
| v11.0.3 | 2025-11-25 | Archaeology Working Group · FAIR+CARE Council | Switched to official directory layout style; fixed heading levels; outer/inner fence separation. |
| v11.0.2 | 2025-11-25 | Archaeology Working Group               | Iteration with inline directory layout; superseded by v11.0.3.        |
| v11.0.1 | 2025-11-25 | Archaeology Working Group               | Initial v11 STAC catalog implementation.                              |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — CC-BY 4.0**  
FAIR+CARE · MCP-DL v6.3 · STAC 1.0.0 · DCAT 3.0  

[⬅ Back to Archaeology Datasets](../README.md) · [KFM Metadata Standards](../../../../standards/README.md) · [KFM Master Guide v11](../../../../reference/kfm_v11_master_documentation.md)

</div>