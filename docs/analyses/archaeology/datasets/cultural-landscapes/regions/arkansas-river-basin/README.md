---
title: "🗺️ KFM v11.2.3 — Arkansas River Basin Cultural Landscape Region (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/datasets/cultural-landscapes/regions/arkansas-river-basin/README.md"
version: "v11.2.3"
last_updated: "2025-12-02"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Biannual · Cultural Landscape Working Group · FAIR+CARE Council"
content_stability: "stable"
backward_compatibility: "Aligned with v11.2.3 cultural-landscape-region contract"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-version-hash>"
doc_integrity_checksum: "<sha256-of-this-file>"

sbom_ref: "../../../../../../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../../../../../../releases/v11.2.3/manifest.zip"
telemetry_ref: "../../../../../../../releases/v11.2.3/focus-telemetry.json"
telemetry_schema: "../../../../../../../schemas/telemetry/archaeology-cultural-landscape-regions-v1.json"

governance_ref: "../../../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"

status: "Active / Enforced"
doc_kind: "Region Dataset"
intent: "cultural-landscape-region-arkansas-river-basin"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Compliant"
---

<div align="center">

# 🗺️ **KFM — Arkansas River Basin Cultural Landscape Region**  
`docs/analyses/archaeology/datasets/cultural-landscapes/regions/arkansas-river-basin/README.md`

**Purpose:**  
Define the **Arkansas River Basin Cultural Landscape Region** dataset within the Kansas Frontier Matrix (KFM).  
This region provides a **generalized cultural–environmental landscape** used for:

- Multi-phase settlement and interaction synthesis  
- Story Node narratives centered on the Arkansas River corridor  
- Focus Mode v2/v3 interpretive overlays and explainability chips  
- MapLibre & Cesium regional polygons (with governed zoom behavior)  
- Cross-watershed cultural modeling and AI reasoning  
- Integration of archaeological, historical, and environmental evidence  

This document specifies the **data layout**, **metadata profile**, **provenance expectations**, and **governance rules** unique to the Arkansas River Basin region while remaining aligned with the global cultural landscape region standard.

</div>

---

## 📘 Conceptual Overview

The **Arkansas River Basin Cultural Landscape Region** represents a **generalized, multi-era cultural landscape** focused on:

- The main Arkansas River corridor and major tributaries within the KFM scope  
- Long-term patterns of settlement, subsistence, and interaction  
- Protohistoric and early historic intercultural movements  
- Environmental continuity and hydrological structure underpinning cultural dynamics  

Key conceptual properties:

- **Multi-phase**: spans multiple cultural phases (e.g., Late Prehistoric, Protohistoric, early Historic), expressed via OWL-Time.  
- **Hydrologically structured**: region geometry is derived from basin-scale hydrology, terrain, and eco-regions, then generalized.  
- **Culturally synthesized**: integrates archaeological sites (internally), ethnohistoric sources, environmental proxies, and archival maps.  
- **Sensitivity-aware**: region boundaries are generalized to avoid exposing sensitive or confidential locations.

This region functions as a **meso-scale anchor** that connects:

- Site-level and sub-regional datasets  
- Hydrology, soils, and eco-regions  
- Story Nodes about riverine movement, exchange, settlement, and cultural change.

---

## 🗂️ Directory Layout

~~~text
docs/analyses/archaeology/datasets/cultural-landscapes/regions/arkansas-river-basin/
├── 📄 README.md                             # This file (Arkansas River Basin region standard)
│
├── 📁 data/                                 # Region geometries and derivative products
│   ├── 🌐 geojson/                          # Generalized polygons (EPSG:4326) for public use
│   │   ├── arkansas-river-basin-region.v1.geojson
│   │   └── arkansas-river-basin-region.v1-topology-simplified.geojson
│   └── 🔷 h3/                               # H3 mosaic representations (for high-sensitivity views)
│       └── arkansas-river-basin-region-h3-r6.v1.geojson
│
├── 🗂️ stac/                                # STAC Items & Collections for this region
│   ├── collection-arkansas-river-basin-region-v1.json
│   └── item-arkansas-river-basin-region-v1.json
│
├── 🧾 metadata/                             # DCAT, JSON-LD, narrative/context metadata
│   ├── dcat-arkansas-river-basin-region-v1.jsonld
│   └── context-arkansas-river-basin-region-v1.md
│
└── 🧬 provenance/                           # Optional region-local pointers; canonical logs live in ../provenance/
    └── arkansas-river-basin-region-v1.prov-ref.json
~~~

**Directory contract:**

- **Authoritative provenance** for this region is defined under:  
  `docs/analyses/archaeology/datasets/cultural-landscapes/provenance/`  
  (e.g., `arkansas-river-basin-region-v1.json`), with this directory optionally containing thin reference files.  
- `data/` geometries must always be **derived from** internal, more detailed sources but **published only in generalized form**.  
- `stac/` and `metadata/` files must remain in sync with the global region registry at:  
  `docs/analyses/archaeology/datasets/cultural-landscapes/regions/README.md`.

---

## 🌄 Region Definition (Arkansas River Basin)

The Arkansas River Basin Cultural Landscape Region must define:

| Element                   | Requirement |
|---------------------------|------------|
| **Region Name**          | `"Arkansas River Basin Cultural Landscape Region"` (or equivalent human-readable label) |
| **Region Identifier**    | Slug: `arkansas-river-basin-region` (used in STAC IDs and file names) |
| **Region Kind**          | `"drainage"` and/or `"eco-cultural"` |
| **Temporal Span**        | Multi-phase OWL-Time intervals, covering relevant Late Prehistoric → Protohistoric → early Historic phases |
| **Spatial Representation** | Generalized polygon(s) and optional H3 mosaic(s) describing the basin-scale region; CRS = EPSG:4326 |
| **Environmental Context** | Hydrology (river + tributaries), floodplain structure, adjacent eco-regions, soils, and topography |
| **Cultural Connections** | Archaeological settlement clusters, material culture distributions, exchange networks, and ethnohistoric routes (described at generalized scale) |
| **Sources**              | Archaeological survey syntheses, geomorphological mapping, historical maps, ethnohistoric accounts, paleoenvironmental datasets |
| **Sensitivity Classification** | CARE-compliant (`generalized` or `restricted-generalized`), with clear visibility rules |

---

## 📦 Metadata Profile (Arkansas River Basin Region)

### ✔ STAC Item / Collection

The STAC representation for this region must include:

- `id`:  
  - Example: `"kfm-arch-lands-arkansas-river-basin-region-v1"`  
- `bbox`:  
  - Generalized bounding box of the region (no site-level precision).  
- `geometry`:  
  - Polygon/MultiPolygon for the region, with simplification applied; CRS = EPSG:4326.  
- `properties` (selected fields):  
  - `kfm:region_slug = "arkansas-river-basin-region"`  
  - `kfm:region_kind = "drainage"` (and optionally `"eco-cultural"`)  
  - `kfm:culture_phase`: array of cultural phases (e.g., `["Late Prehistoric", "Protohistoric", "Early Historic"]`)  
  - `kfm:temporal_coverage`: OWL-Time-compatible representation (intervals and/or named periods)  
  - `care:sensitivity`: `"generalized"` or `"restricted-generalized"`  
  - `care:visibility_rules`: `"polygon-generalized"`, `"h3-only"`, or combination policies  
  - `kfm:provenance`: reference to PROV-O record under `../provenance/`  
- `assets`:  
  - `data`: link(s) into `../arkansas-river-basin/data/geojson/` and/or `../arkansas-river-basin/data/h3/`  

### ✔ DCAT & Context Metadata

Under `metadata/`, DCAT/JSON-LD records must specify:

- `dct:title`: `"Arkansas River Basin Cultural Landscape Region"`  
- `dct:description`: narrative description of region purpose, derivation, and intended uses.  
- `dct:temporal`: temporal coverage matching STAC properties.  
- `dct:license`: `CC-BY 4.0` (unless stricter governance applies).  
- `dcat:keyword`:  
  - Examples: `"Arkansas River"`, `"cultural region"`, `"drainage basin"`, `"protohistoric"`, `"eco-cultural landscape"`.  

Context documentation (`context-arkansas-river-basin-region-v1.md`) may provide:

- Human-readable narrative, maps, and diagrams.  
- Explicit descriptions of generalization and sovereignty/CARE decisions.

---

## ⚖ CARE & Sovereignty Requirements

The Arkansas River Basin region is subject to the global CARE rules but with specific constraints:

- `care:sensitivity` must be **at least** `"generalized"`; `"restricted-generalized"` may be required if review identifies elevated risks.  
- `care:review` must indicate the review path, e.g.:
  - `"faircare"`  
  - `"tribal"`  
  - `"faircare+tribal"` (recommended for multi-phase, multi-community contexts).  
- `care:notes` must explain:
  - Why boundaries are generalized the way they are.  
  - Any constraints or exclusions (e.g., known but non-mapped sensitive areas).  
- `care:visibility_rules` must ensure:
  - No zoom level reveals implied precision beyond governance policy.  
  - Potential use of `"h3-only"` for certain Focus Mode layers.

**Forbidden for this public region dataset:**

- Any geometry that could be reverse-engineered to reveal sensitive ceremonial or burial locations.  
- Any depiction of sovereign or disputed boundaries beyond what is agreed and documented in governance.

---

## 🧬 Provenance Requirements

The Arkansas River Basin region must have at least one PROV-O provenance record under:

- `docs/analyses/archaeology/datasets/cultural-landscapes/provenance/`

Expected properties in the provenance log:

- Entities (`prov:Entity`):
  - `raw`: internal, detailed hydrology + site + environmental evidence.  
  - `generalized`: basin-scale generalized region (polygon / H3).  
  - `processed`: published region dataset v1 (linked to STAC/metadata).  
- Activities (`prov:Activity`):
  - `generalization`: creation of generalized polygon/H3 mosaic.  
  - `boundary_estimation`: choice of basin extent and ecotone.  
  - `review`: FAIR+CARE and tribal governance review.  
- Agents (`prov:Agent`):
  - `analyst`: dataset engineer / GIS specialist.  
  - `faircare`: FAIR+CARE Council representative group.  
  - `tribal`: appropriate tribal/sovereign reviewers (where applicable).  
- CARE fields:
  - `care:sensitivity`, `care:notes`, `care:visibility_rules` aligned with this README.

The optional local file `provenance/arkansas-river-basin-region-v1.prov-ref.json` may:

- Store a **pointer** to the canonical provenance JSON-LD.  
- Provide a minimal summary used by UIs or tooling.

---

## 🧭 Spatial Specifications

- CRS: **EPSG:4326** for all public geometries.  
- Geometries must be:

  - Simplified using documented algorithms (e.g., Douglas–Peucker) with parameters recorded in provenance.  
  - Topologically cleaned (no self-intersections; valid polygons).  
  - Clipped in ways that avoid leakage of site-level or sensitive detail.

- The basin region should:

  - Encompass relevant hydrological catchments and adjacent eco-cultural zones.  
  - Avoid encoding contested modern political boundaries as culturally definitive lines.  
  - Be representable at **multiple scales** (polygon and H3 mosaic) for different visibility levels.

---

## 🕰️ Temporal Specifications

- Temporal coverage must represent:

  - The earliest cultural phases for which the Arkansas River Basin is a meaningful analytic unit in KFM.  
  - The latest phases included in the dataset (e.g., early Historic limit).  

- Use OWL-Time and/or compatible properties for:

  - `time:hasBeginning` / `time:hasEnd` (for intervals).  
  - Named cultural phases (`kfm:culture_phase`), aligned with KFM’s archaeology ontology.

- Where uncertainty exists:

  - Include uncertainty ranges or notes (e.g., ±50 years, ambiguous phase boundaries).  
  - Ensure temporal uncertainty is consistent across STAC, DCAT, and provenance.

---

## 🧪 Validation & CI/CD

The Arkansas River Basin region dataset must pass all applicable governed validations:

- **Schema checks**
  - Region metadata schema (KFM archaeology region profile).  
  - CARE schema.  
  - DCAT and STAC schemas.

- **Provenance checks**
  - Valid PROV-O JSON-LD shape.  
  - Correct CARE fields in provenance.  
  - Working links between STAC/metadata and provenance.

- **Generalization checks**
  - Confirm polygon simplification / H3 generalization meets minimum abstraction levels.  
  - Ensure no geometry violates sovereignty or confidentiality rules.

### CI Workflows (indicative)

- `metadata-validate.yml`  
- `artifact-stac-validate.yml`  
- `faircare-audit.yml`  
- `archaeology-provenance-validate.yml`  

CI must **block**:

- Any update that changes geometry or temporal coverage without updated provenance.  
- Any change that weakens CARE protections or breaks visibility rules.  
- Any inconsistency between this region README, STAC, metadata, and provenance.

---

## 🧠 Graph, Story Node & Focus Mode Integration

### Knowledge Graph (Neo4j)

From this dataset, KFM graph loaders create:

- Nodes:
  - `CulturalRegion { slug: "arkansas-river-basin-region" }`  
  - `HydrologicalUnit` (basin-level units)  
  - `CulturalPhase` (linked to archaeology ontology)  
  - `ProvenanceRecord`  

- Relationships:
  - `OCCURRED_DURING` (region ↔ phases).  
  - `ASSOCIATED_WITH` (region ↔ hydrological units, eco-regions, material culture clusters).  
  - `HAS_PROVENANCE` (region ↔ provenance).  
  - `HAS_SENSITIVITY` (region ↔ sensitivity classification).  

### Story Nodes

Story Nodes using this region must:

- Reference the region slug and/or STAC ID.  
- Provide narrative about:

  - Riverine movement and exchange.  
  - Settlement changes across time.  
  - Environmental shifts impacting cultural patterns.

- Use region provenance to:

  - Explain limitations and generalization.  
  - Show review status (FAIR+CARE, tribal).  

### Focus Mode v2/v3

Focus Mode behavior for this region includes:

- Region-aware overlays and tooltips that:

  - Show cultural-phase summaries.  
  - Surface provenance and CARE badges.  
  - Respect zoom-dependent visibility rules (polygon vs H3).  

- Model constraints:

  - Avoid suggesting more precise boundaries than documented.  
  - Reflect uncertainty and multi-era nature of the region.

---

## 🕰️ Version History

| Version  | Date       | Author                                      | Summary                                                                 |
|----------|------------|---------------------------------------------|-------------------------------------------------------------------------|
| v11.2.3  | 2025-12-02 | Cultural Landscape WG · FAIR+CARE Council   | Established governed dataset spec, layout, and CI/CARE/provenance requirements for Arkansas River Basin region; aligned with KFM-MDP v11.2.2 and global region standard. |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — CC-BY 4.0**  
FAIR+CARE Certified · MCP-DL v6.3 · KFM-MDP v11.2.2 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[⬅ Back to Cultural Landscape Regions](../README.md) · [⬅ Back to Cultural Landscapes](../../README.md)

</div>