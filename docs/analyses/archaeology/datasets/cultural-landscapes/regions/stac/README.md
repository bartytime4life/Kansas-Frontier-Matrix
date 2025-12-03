---
title: "🛰️ KFM v11.2.3 — Cultural Landscape Region STAC Catalogs (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/datasets/cultural-landscapes/regions/stac/README.md"
version: "v11.2.3"
last_updated: "2025-12-02"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Biannual · Cultural Landscape Working Group · FAIR+CARE Council · Metadata Standards Subcommittee"
content_stability: "stable"
backward_compatibility: "v10.4.0 → v11.2.3 region-STAC-contract compatible"

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
doc_kind: "STAC Catalog Registry"
intent: "cultural-landscape-region-stac"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Compliant"
---

<div align="center">

# 🛰️ **KFM — Cultural Landscape Region STAC Catalogs**  
`docs/analyses/archaeology/datasets/cultural-landscapes/regions/stac/README.md`

**Purpose:**  
Define and govern the **SpatioTemporal Asset Catalog (STAC)** structure for all **cultural landscape region datasets** in the Kansas Frontier Matrix (KFM).  
This directory stores the **STAC Collections and Items** that describe:

- Region-level geometries (e.g., Flint Hills, Smoky Hill, Arkansas River Basin)  
- Their temporal coverage, cultural phases, and environmental context  
- CARE sensitivity and visibility policies  
- Links to region metadata and PROV-O provenance logs  

All STAC artifacts here must be **CI-validated**, **graph-safe**, and **FAIR+CARE-aligned**.

</div>

---

## 📘 Overview

The **Cultural Landscape Region STAC Catalogs** provide a governed STAC interface for:

- Discovering cultural landscape regions as geospatial assets  
- Linking region geometries to:
  - Region metadata (`../metadata/`)  
  - Provenance logs (`../../provenance/`)  
  - Region-specific READMEs (e.g., `../flint-hills-region/README.md`)  
- Feeding KFM’s:
  - ETL pipelines  
  - Neo4j graph loaders  
  - Story Node resolver  
  - Focus Mode v2/v3 overlay system  

STAC artifacts here must:

- Follow the **OGC STAC specification** and KFM’s STAC profile.  
- Encode CARE and sovereignty constraints in **properties**.  
- Maintain tight alignment with region metadata and provenance.

---

## 🗂️ Directory Layout

~~~text
docs/analyses/archaeology/datasets/cultural-landscapes/regions/stac/
├── 📄 README.md                                   # This file (STAC registry contracts & patterns)
│
├── 📁 collections/                                # STAC Collections for region datasets
│   ├── collection-flint-hills-region-v1.json      # Flint Hills eco-cultural region collection
│   ├── collection-smoky-hill-region-v1.json       # Smoky Hill cultural drainage collection
│   ├── collection-arkansas-river-basin-region-v1.json # Arkansas River Basin cultural region collection
│   └── collection-<region-slug>-v<semver>.json    # Future governed region collections
│
├── 📁 items/                                      # STAC Items for specific region versions/variants
│   ├── item-flint-hills-region-v1.json           # Flint Hills region v1 STAC Item
│   ├── item-smoky-hill-region-v1.json            # Smoky Hill region v1 STAC Item
│   ├── item-arkansas-river-basin-region-v1.json  # Arkansas River Basin region v1 STAC Item
│   └── item-<region-slug>-v<semver>.json         # Future governed region Items
│
└── 📁 indexes/                                    # Optional higher-level catalogs / summaries
    ├── catalog-regions-root.v1.json              # Root catalog for all cultural landscape regions (optional)
    └── catalog-regions-by-phase.v1.json          # Optional catalog grouping by cultural phase / period
~~~

**Directory contract:**

- **Collections** live in `collections/`, one per region + major version.  
- **Items** live in `items/`, one per region + versioned geometry set or representation.  
- Optional `indexes/` provide navigation catalogs but **must not** override collection/item semantics.  
- Region-specific directories (e.g., `../flint-hills-region/stac/`) may hold **mirrors or symlinks**, but this `stac/` registry is the authoritative location for region STAC JSON.

---

## 🧾 STAC Collection Requirements (Regions)

Each `collection-<region-slug>-v<semver>.json` must:

- Conform to the STAC Collection spec and KFM’s archaeology STAC profile.  
- Represent **one conceptual region** (e.g., Flint Hills, Smoky Hill, Arkansas River Basin) at a given semantic version.

### Core Fields

Required top-level fields (selected):

- `stac_version`  
- `type = "Collection"`  
- `id`  
  - Example: `"kfm-arch-lands-flint-hills-region-v1"`  
- `description`  
  - Human-readable description of the region’s purpose and context.  
- `license`  
  - `CC-BY-4.0` (unless stricter governance applies).  
- `extent`  
  - `spatial` (generalized bbox)  
  - `temporal` (coverage aligned with OWL-Time intervals).  

### KFM-Specific Fields (Collections)

In `properties` or collection-level extensions:

- `kfm:region_slug` — e.g., `"flint-hills-region"`.  
- `kfm:region_kind` — e.g., `"eco-cultural"`, `"drainage"`, `"territorial-generalized"`.  
- `kfm:culture_phase` — array of cultural phase labels.  
- `kfm:temporal_coverage` — structured temporal coverage (aligned with OWL-Time + archaeology ontology).  
- `kfm:metadata_ref` — path/URI to the corresponding region metadata record:  
  - Example: `docs/analyses/archaeology/datasets/cultural-landscapes/regions/metadata/flint-hills-region-metadata-v1.jsonld`.  
- `kfm:provenance_ref` — path/URI to canonical PROV-O provenance log(s) under `../../provenance/`.

### CARE & Sovereignty Fields (Collections)

Collections must also include:

- `care:sensitivity` — `"generalized"` or `"restricted-generalized"` (public records only).  
- `care:review` — `"faircare"`, `"tribal"`, or combinations (e.g., `"faircare+tribal"`).  
- `care:notes` — concise explanation of generalization and review context.  
- `care:visibility_rules` — `"polygon-generalized"`, `"h3-only"`, `"no-exact-boundaries"` or governed combinations.

These fields must **match** metadata and provenance.

---

## 🧱 STAC Item Requirements (Regions)

Each `item-<region-slug>-v<semver>.json` must:

- Conform to the STAC Item spec and the same KFM archaeology STAC profile.  
- Reference one **specific geometry representation** (e.g., primary polygon set).

### Core Fields

Required (selected):

- `stac_version`  
- `type = "Feature"`  
- `id`  
  - Example: `"kfm-arch-lands-smoky-hill-region-v1"`  
- `geometry`  
  - Region polygon or MultiPolygon (generalized; CRS implicitly WGS84).  
- `bbox`  
- `properties.datetime` or `properties.interval` (where appropriate).

### KFM-Specific Fields (Items)

Within `properties`:

- `kfm:region_slug`  
- `kfm:region_kind`  
- `kfm:culture_phase`  
- `kfm:temporal_coverage`  
- `kfm:stac_collection_id` — ID of the parent collection.  
- `kfm:source_ref` — optional references to source datasets (e.g., eco-regions, hydrology, geology).  
- `kfm:provenance_ref` — pointer to canonical provenance JSON-LD.

### CARE Fields (Items)

- `care:sensitivity`  
- `care:review`  
- `care:visibility_rules`  
- `care:notes`

These values must remain **consistent** across:

- Region-level README (per-region directories).  
- Region metadata records (`../metadata/`).  
- Canonical provenance logs (`../../provenance/`).  
- Region provenance registry (`../provenance/`).

### Assets

Typical asset entries:

- `assets.data`  
  - `href`: path/URI to region geometry files (e.g., GeoJSON) in per-region `data/` directories.  
  - `type`: e.g., `"application/geo+json"`.  
  - `roles`: e.g., `["data"]`.  

- Optional `assets.h3`  
  - For H3 mosaic representations at specified resolution(s).  

Assets must **not** expose sensitive or over-precise geometries.

---

## 📚 STAC Index Catalogs (`indexes/`)

The `indexes/` directory may contain:

- `catalog-regions-root.v1.json`  
  - Root `Catalog` linking to all region Collections.  
- `catalog-regions-by-phase.v1.json`  
  - Optional grouping catalog linking Collections or Items by cultural phase or time slice.

Constraints:

- `indexes/` catalogs must **not** introduce new semantics or conflicting IDs.  
- They serve purely as **navigation aids** for clients and ETL, not as alternate sources of truth.  
- They must reference only Collections/Items that exist in `collections/` and `items/`.

---

## ⚖ FAIR+CARE & Governance Constraints

STAC artifacts here must:

- Never weaken CARE constraints relative to canonical provenance and region metadata.  
- Reflect the **governed generalization** level:
  - Polygon vs H3  
  - Zoom behaviors implied by `care:visibility_rules`.  
- Respect sovereignty policies:
  - No depiction of restricted boundaries or sacred/sensitive locations.  
  - No inference of precise site-level distributions from public geometries.

Changes that:

- Alter `care:*` fields,  
- Change spatial extents, or  
- Adjust temporal coverage

are treated as **governance events** and must pass FAIR+CARE and sovereignty review.

---

## 🧬 Relationship to Metadata & Provenance

This STAC registry is tightly coupled to:

1. **Region Datasets & READMEs**  
   - `../README.md`  
   - Per-region directories (e.g., `../flint-hills-region/README.md`, `../smoky-hill-region/README.md`).

2. **Region Metadata Registry**  
   - `../metadata/README.md`  
   - `../metadata/*-metadata-v<semver>.jsonld` records (DCAT/JSON-LD).

3. **Global Cultural Landscape Provenance**  
   - `../../provenance/README.md`  
   - `../../provenance/*.json` PROV-O logs.

4. **Region Provenance Registry**  
   - `../provenance/README.md`  
   - `../provenance/registry/region-provenance-index.v1.json`.

**Contract:**

- Every region Collection and Item must map to:
  - A region metadata record (`../metadata/`).  
  - One or more canonical provenance logs (`../../provenance/`).  
  - A corresponding entry in the region provenance registry (`../provenance/registry/`).

If these links break, STAC artifacts are considered **invalid**.

---

## 🧪 Validation & CI/CD

All STAC artifacts in this directory are **CI-enforced** and must pass:

- **STAC validation**
  - STAC Collection / Item schema validation.  
  - KFM archaeology STAC profile checks (custom schemas).  

- **Cross-link validation**
  - `kfm:region_slug` must match a region directory under `../`.  
  - `kfm:metadata_ref` must point to existing region metadata records.  
  - `kfm:provenance_ref` must point to canonical provenance logs.  
  - CARE fields must be consistent with metadata and provenance.

- **Governance validation**
  - CARE audit to ensure no forbidden sensitivity or visibility changes.  
  - Sovereignty checks where flagged.

### Indicative CI workflows

- `artifact-stac-validate.yml`  
- `metadata-validate.yml`  
- `faircare-audit.yml`  
- `archaeology-provenance-validate.yml`  
- `region-metadata-registry-validate.yml`  
- `region-provenance-registry-validate.yml`  

**CI must block:**

- New or modified STAC artifacts without aligned metadata and provenance.  
- Any schema failures or STAC profile violations.  
- CARE / sovereignty regressions.

---

## 🧠 Graph, Story Node & Focus Mode Integration

### Knowledge Graph (Neo4j)

STAC Collections and Items from this directory are used by graph loaders to create:

- **Nodes**
  - `CulturalRegion` (with `slug`, `kind`, temporal coverage).  
  - `RegionCollection` / `RegionItem` (optional explicit node types).  

- **Relationships**
  - `HAS_STAC_COLLECTION` (region ↔ collection).  
  - `HAS_STAC_ITEM` (region ↔ item).  
  - `HAS_PROVENANCE` and `HAS_METADATA` (via STAC links to provenance and metadata).

### Story Nodes

Story Nodes rely on this STAC registry to:

- Resolve spatial anchors for regional narratives via STAC Item IDs.  
- Pull bounding boxes and geometric context for map-based storytelling.  
- Surface CARE and provenance chips (via STAC → metadata → provenance links).

### Focus Mode v2/v3

Focus Mode uses STAC to:

- Determine which regional overlays are available for a given time slice or cultural phase.  
- Render region polygons/H3 mosaics according to `care:visibility_rules`.  
- Provide “inspect region” panels drawing on STAC + metadata + provenance.

---

## 🧭 Authoring & Maintenance Workflow

Suggested workflow when adding/updating a region:

1. **Define/Update Region Dataset**
   - Update per-region README (e.g., `../flint-hills-region/README.md`) and geometry under `../<region>/data/`.

2. **Update Metadata & Provenance**
   - Add or adjust region metadata in `../metadata/`.  
   - Ensure canonical PROV-O logs exist in `../../provenance/`.

3. **Create/Update STAC Collection & Item**
   - Add `collections/collection-<region-slug>-v<semver>.json`.  
   - Add `items/item-<region-slug>-v<semver>.json`.  
   - Link to metadata and provenance via `kfm:*` and `care:*` fields.

4. **Update Registries (If Needed)**
   - Ensure region metadata and provenance registries reflect new versions.  

5. **Run Local Validation**
   - Use repo tooling (e.g., `make validate-region-stac`) to run STAC + cross-link checks.

6. **Submit PR & Address CI/Governance Feedback**
   - CI enforces:
     - STAC validity  
     - Metadata/provenance linkage  
     - CARE and sovereignty integrity  

---

## 🕰️ Version History

| Version  | Date       | Author                                      | Summary                                                                 |
|----------|------------|---------------------------------------------|-------------------------------------------------------------------------|
| v11.2.3  | 2025-12-02 | Cultural Landscape WG · FAIR+CARE Council   | Established STAC registry structure, collection/item contracts, and CI/governance requirements for cultural landscape regions; aligned with KFM-MDP v11.2.2 and region metadata/provenance standards. |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — CC-BY 4.0**  
FAIR+CARE Certified · MCP-DL v6.3 · KFM-MDP v11.2.2 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[⬅ Back to Cultural Landscape Regions](../README.md) · [⬅ Back to Region Metadata Registry](../metadata/README.md) · [⬅ Back to Region Provenance Registry](../provenance/README.md)

</div>