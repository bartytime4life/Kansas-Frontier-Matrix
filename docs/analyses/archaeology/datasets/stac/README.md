---
title: "🗂️ Kansas Frontier Matrix — Archaeology STAC Catalog (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/datasets/stac/README.md"
version: "v11.0.0"
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
doc_uuid: "urn:kfm:docs:archaeology:stac:catalog:v11"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
---

<div align="center">

# 🗂️ **Kansas Frontier Matrix — Archaeology STAC Catalog (v11.0.0)**  
`docs/analyses/archaeology/datasets/stac/README.md`

**Purpose:**  
Define the authoritative STAC 1.0.0 catalog for archaeology datasets in KFM v11, ensuring CARE-compliant generalization, Story Node v3 and Focus Mode v3 compatibility, and strict adherence to FAIR+CARE and MCP-DL v6.3.

</div>

---

# 📘 Overview

This catalog governs the creation, validation, and publication of STAC Collections and Items for all archaeology-related datasets within the Kansas Frontier Matrix (KFM).

KFM v11 requires:

- STAC 1.0.0 compliance  
- DCAT 3.0 alignment  
- GeoJSON correctness  
- OWL-Time temporal semantics  
- GeoSPARQL geometry semantics  
- CIDOC-CRM compatible cultural-heritage fields  
- CARE masking and generalization for sensitive locations  
- Provenance via PROV-O  
- Mandatory checksums, versioning, and immutability  
- Focus Mode v3 narrative binding  
- Story Node v3 attachment safety  

Scope of this catalog:

- Generalized site gazetteers  
- Public-domain artifact inventories (non-sensitive, non-identifying subsets)  
- Cultural landscape and interaction-sphere regional models  
- Geophysical survey products (magnetometry, GPR, resistivity)  
- Paleoenvironmental datasets (cores, pollen, charcoal, proxies)  
- AI-assisted derived analytics and interpretive products  

---

# 🗂 Directory Layout (Indent Style B — ASCII Only)

docs/analyses/archaeology/datasets/stac/
 |
 +-- README.md
 |
 +-- collections/
 |   +-- site-gazetteers.json
 |   +-- artifact-inventories.json
 |   +-- cultural-landscapes.json
 |   +-- geophysics.json
 |   +-- paleoenvironment.json
 |
 +-- items/
 |   +-- site-gazetteer-*.json
 |   +-- artifacts-*.json
 |   +-- landscape-*.json
 |   +-- geophysics-*.json
 |   +-- paleo-*.json
 |
 +-- schemas/
 |   +-- kfm-archaeology-schema.json
 |   +-- care-generalization-schema.json
 |   +-- provenance-lineage-schema.json
 |
 +-- examples/
     +-- example-generalized-site.json
     +-- example-landscape.json
     +-- example-paleo.json

All filenames are normative and MUST be used exactly as shown to satisfy automated discovery, STAC validation, and Focus Mode v3 lookups.

---

# 🔖 STAC Collections

Each archaeology subdomain MUST define a STAC Collection including at least:

- `id`, `title`, `description`, `keywords`  
- `license`, `providers`  
- `extent.spatial` (CARE-generalized; no precise coordinates)  
- `extent.temporal` (OWL-Time compatible intervals)  
- `summaries` for key archaeology fields (e.g., culture phase, site types, datatypes)  
- `care:*` sensitivity metadata and review origin  
- Links to Items, schemas, and provenance resources  

Collection registry:

| Collection            | Description                                  | File                                      |
|----------------------|----------------------------------------------|-------------------------------------------|
| Site Gazetteers      | Generalized site-level records               | `collections/site-gazetteers.json`        |
| Artifact Inventories | Public-domain artifact inventory summaries   | `collections/artifact-inventories.json`   |
| Cultural Landscapes  | Interaction spheres, corridors, regions      | `collections/cultural-landscapes.json`    |
| Geophysics           | Magnetometry, GPR, resistivity geophysics    | `collections/geophysics.json`             |
| Paleoenvironment     | Cores, pollen, charcoal, multi-proxy records | `collections/paleoenvironment.json`       |

Collection-level `summaries` SHOULD cover, where applicable:

- `kfm:culture_phase` (enumerated period codes)  
- `kfm:site_type` (controlled vocabulary)  
- `kfm:datatype` (magnetometry-grid, artifact-inventory, pollen-series, etc.)  
- `care:sensitivity` distribution across Items  
- `proj:epsg` CRS codes for assets  

---

# 📦 STAC Item Requirements

## Core Required Fields

Every archaeology STAC Item MUST contain:

Field             | Requirement
-----------------|------------
`stac_version`   | `"1.0.0"`
`type`           | `"Feature"`
`id`             | Stable, versioned ID, e.g. `kfm-arch-<domain>-<slug>-vN`
`geometry`       | Generalized GeoJSON geometry (never precise site centroids)
`bbox`           | CARE-compliant generalized bounding box
`properties`     | Includes time interval, domain fields, CARE fields
`start_datetime` | OWL-Time interval start
`end_datetime`   | OWL-Time interval end (or equal to start)
`assets`         | MUST include at least `data` and `provenance`
`links`          | MUST include `root`, `self`, `collection`, and `provenance`

## Required Extensions

The following STAC extensions are REQUIRED for all archaeology Items:

- `proj` (projection metadata)  
- `version` (semantic versioning of assets)  
- `checksum` (e.g. SHA-256 digests)  
- `scientific` (citations, DOIs)  
- `kfm:archaeology` (domain-specific fields)  
- `care` (sensitivity and review metadata)  

## Archaeology Extension (`kfm:*`) Fields

These properties live under `properties` and MUST be used where applicable:

Field                | Description
---------------------|------------
`kfm:culture_phase`  | Archaeological period or taxonomy (controlled vocabulary)
`kfm:site_type`      | Site class (e.g. village, mound, camp, quarry, ritual, landscape-region)
`kfm:datatype`       | Dataset type (e.g. magnetometry-grid, artifact-inventory, pollen-series)
`kfm:source`         | Origin institution, project, or repository
`kfm:provenance`     | Path or URI to PROV-O lineage bundle for this Item

Values MUST come from controlled vocabularies defined in `kfm-archaeology-schema.json`.

## CARE Extension (`care:*`) Fields

Field            | Description
-----------------|------------
`care:sensitivity` | One of `generalized`, `restricted`, or `public`
`care:notes`       | Non-sensitive explanatory text (no coordinates, no identifying info)
`care:review`      | One of `tribal`, `faircare`, or `none-required`

Rules:

- Items with `care:sensitivity = restricted` MUST NOT be made public; they are for internal governance only.  
- All public-facing Items MUST have `care:sensitivity = generalized` or `public`.  
- `care:review = tribal` MUST be set where any tribal governance review has occurred.  

---

# 🌍 Spatial & Temporal Rules

## Coordinate Reference System

- Default CRS is EPSG:4326 (WGS84 longitude/latitude).  
- Any deviation (e.g., local projected CRS for geophysics) MUST be declared in `proj:*` extension fields and in asset metadata.  

## CARE-Compliant Generalization

For all archaeology Items:

- Never publish precise site coordinates or small bounding boxes that reveal exact site locations.  
- Use:
  - Enlarged envelopes (buffering sites to region polygons).  
  - Aggregated centroids at landscape scale (e.g., county-level or broader).  
- When in doubt, err towards coarser generalization and stricter `care:sensitivity`.  

## Temporal Modeling (OWL-Time Compatible)

- `start_datetime` and `end_datetime` MUST be valid ISO-8601 datetimes.  
- When only an approximate date is known:
  - Set `start_datetime` to earliest plausible bound.  
  - Set `end_datetime` to latest plausible bound.  
  - Include a human-readable range label in a separate property (e.g., `kfm:time_label = "ca. 1200–1450 CE"`).  
- All temporal extents MUST represent intervals, not just points, even when `start_datetime == end_datetime`.  

---

# 🔗 Example STAC Item (Generalized Cultural Landscape)

Example Item for a generalized cultural landscape, suitable for the `cultural-landscapes` Collection:

id: kfm-arch-landscape-great-bend-v2

stac_version: "1.0.0"  
type: "Feature"  

bbox:
-101.5, 37.5, -96.0, 39.5  

geometry:
type: "Polygon"  
coordinates: [[[ /* generalized polygon coordinates elided for brevity */ ]]]  

properties:
  start_datetime: "1200-01-01T00:00:00Z"  
  end_datetime: "1450-01-01T00:00:00Z"  
  kfm:culture_phase: "Late Prehistoric"  
  kfm:site_type: "landscape-region"  
  kfm:datatype: "regional-model"  
  kfm:source: "Example Source Institution"  
  kfm:provenance: "provenance/great-bend-v2.json"  
  kfm:time_label: "ca. 1200–1450 CE"  
  care:sensitivity: "generalized"  
  care:notes: "Geometry generalized to regional scale to protect sensitive locations."  
  care:review: "tribal"  

assets:
  data:
    href: "https://example.org/data/great_bend_landscape_v2.geojson"  
    type: "application/geo+json"  
    roles: ["data"]  

  provenance:
    href: "provenance/great-bend-v2.json"  
    type: "application/json"  
    roles: ["provenance"]  

links:
  - rel: "collection"
    href: "../collections/cultural-landscapes.json"  

  - rel: "root"
    href: "../README.md"  

  - rel: "self"
    href: "../items/landscape-great-bend-v2.json"  

This example is normative for structure; actual geometries and URLs MUST be replaced with real values.

---

# 🧪 Validation & CI Requirements

All archaeology STAC content MUST pass the following checks in CI:

- STAC 1.0.0 JSON Schema validation for:
  - `collections/*.json`  
  - `items/*.json`  
- Domain schema validation:
  - `schemas/kfm-archaeology-schema.json`  
  - `schemas/care-generalization-schema.json`  
  - `schemas/provenance-lineage-schema.json`  
- Checksum verification:
  - Assets MUST include `checksum:sha256` fields and MUST match actual file hashes.  
- DCAT 3.0 crosswalk validation for Collections:
  - Map STAC Collections to DCAT datasets and verify mandatory DCAT fields are present.  
- GeoSPARQL geometry checks:
  - Validate all geometries are well-formed and non-self-intersecting at published generalization levels.  
- OWL-Time interval checks:
  - Ensure `start_datetime <= end_datetime`.  
- PROV-O lineage completeness:
  - Every Item MUST have a corresponding PROV-O bundle or link in `kfm:provenance`.  
- Focus Mode v3 readiness:
  - Items MUST expose sufficient metadata for Focus Mode to:
    - Bind events and regions to Story Nodes.  
    - Generate entity timelines without leaking sensitive locations.  
- Story Node v3 extraction safety:
  - Ensure that any automated Story Node generation from Items does not include restricted attributes.  

CI job identifier:

- `stac-validate.yml` (or equivalent) MUST be configured to run on every PR touching this directory.

---

# 🕰 Version History

| Version | Date       | Author                                  | Notes                                                                 |
|---------|------------|-----------------------------------------|-----------------------------------------------------------------------|
| v11.0.0 | 2025-11-25 | Archaeology Working Group · FAIR+CARE Council | Full v11 rewrite; one-box output rule; ASCII-only tree; MDP v11 alignment |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — CC-BY 4.0**  
FAIR+CARE · MCP-DL v6.3 · STAC 1.0.0 · DCAT 3.0  

[⬅ Back to Archaeology Datasets](../README.md) · [KFM Metadata Standards](../../../../standards/README.md) · [KFM Master Guide v11](../../../../reference/kfm_v11_master_documentation.md)

</div>