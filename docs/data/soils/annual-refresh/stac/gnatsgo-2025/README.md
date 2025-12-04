---
title: "🌐 KFM v11.2.3 — gNATSGO 2025 STAC Collection (Kansas AOI) (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
description: "STAC Collection overview for the 2025 NRCS gNATSGO soils dataset (Kansas AOI) in the Kansas Frontier Matrix annual soils refresh pipeline."
path: "docs/data/soils/annual-refresh/stac/gnatsgo-2025/README.md"
version: "v11.2.3"
last_updated: "2025-12-03"

release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Annual · Geospatial Systems · FAIR+CARE Oversight"
content_stability: "stable"
status: "Active / Enforced"
backward_compatibility: "v10.x → v11.x soils-gnatsgo-stac-collection-contract compatible"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../../../../../releases/v11.2.3/manifest.zip"
telemetry_ref: "../../../../../../releases/v11.2.3/soils-refresh-telemetry.json"
telemetry_schema: "../../../../../../schemas/telemetry/soils-refresh-v1.json"

governance_ref: "../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.3"

doc_kind: "STAC Collection Overview"
intent: "nrcs-soils-gnatsgo-2025-stac"

fair_category: "F1-A1-I1-R1"
care_label: "CARE-Compliant"
sensitivity: "General"
sensitivity_level: "Low"
indigenous_data_flag: false
public_benefit_level: "High"
risk_category: "Low"
redaction_required: false

ontology_alignment:
  schema_org: "Dataset"
  cidoc: "E73 Information Object"
  prov_o: "prov:Entity"
  owl_time: "TemporalEntity"
  geosparql: "geo:FeatureCollection"

json_schema_ref: "../../../../../../schemas/json/data-soils-annual-refresh-gnatsgo-2025-stac-readme-v1.json"
shape_schema_ref: "../../../../../../schemas/shacl/data-soils-annual-refresh-gnatsgo-2025-stac-readme-v1.shape.ttl"

immutability_status: "version-pinned"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"

ttl_policy: "Permanent"
sunset_policy: "Never (per-year soils collections form the long-term soils baseline)"
---

<div align="center">

# 🌐 gNATSGO 2025 — STAC Collection (Kansas AOI)  
`docs/data/soils/annual-refresh/stac/gnatsgo-2025/README.md`

**Purpose:**  
Describe the **2025 gNATSGO STAC Collection** for the Kansas Frontier Matrix annual soils refresh, including:

- How `collection.json` is structured and governed  
- How Items (if used) are organized and linked  
- How this Collection fits into the **STAC-first → DCAT-derived** KFM catalog model and the soils diff/provenance pipeline  

</div>

---

## 📘 1. Scope

This directory corresponds to the **KFM STAC representation** of the **2025 NRCS gNATSGO soils dataset** over the KFM area of interest (typically Kansas and relevant buffer regions).

Contents:

- `collection.json` — the **authoritative STAC Collection** for gNATSGO 2025 in KFM.  
- `items/` — optional per-tile/per-region Items, if the soils pipeline exposes finer-grain STAC entries.

This Collection is:

- Derived from **raw NRCS gNATSGO 2025 bundles** stored under `../../../../raw/`.  
- Governed by the **Annual Soils Refresh** pipeline (`../../README.md` and `../../processing/README.md`).  
- Conforming to the **KFM STAC profile** and extensions under `docs/standards/catalogs/stac/`.

It is a key **gridded soils baseline** for hydrology, climate, and land-use modeling.

---

## 🗂️ 2. Directory Layout (gNATSGO 2025 STAC)

~~~text
docs/data/soils/annual-refresh/stac/gnatsgo-2025/
│
├── 📄 README.md               # This file — gNATSGO 2025 STAC overview
│
├── 📄 collection.json         # STAC Collection for gNATSGO 2025 (KFM STAC profile-compliant)
│
└── 📂 items/                  # (Optional) per-tile or per-region Items
    ├── 📄 gnatsgo-2025-ks.json          # Example: Kansas-wide Item (if used)
    ├── 📄 gnatsgo-2025-tile-001.json    # Example: tile-based Items (if used)
    └── …                                # Additional Items per tiling/partition strategy
~~~

**Directory contract:**

- `collection.json` MUST exist and be **STAC 1.0.x** compliant.  
- If `items/` is present:
  - All Items MUST set `"collection"` to the gNATSGO 2025 Collection ID.  
  - Items MUST include `links` pointing to the Collection and STAC root.  
  - Items MUST adhere to the **KFM STAC profile** and soils best practices.

---

## 🧱 3. STAC Collection Profile (gNATSGO 2025)

The `collection.json` file for gNATSGO 2025 MUST satisfy:

### 3.1 Core STAC Fields

- `stac_version = "1.0.0"` (or compatible `1.0.x`).  
- `type = "Collection"`.  
- `id` — recommended: `gnatsgo-2025-ks` (or similar AOI-specific identifier).  
- `description` — e.g.:

  > “NRCS gNATSGO 2025 gridded soils dataset for Kansas as processed by the KFM annual soils refresh (gridded attributes and interpretations).”

- `extent.spatial` — bounding boxes for the gNATSGO coverage over KFM AOI.  
- `extent.temporal` — temporal extent of this release (e.g., effective reference date in 2025).  
- `license` — NRCS/public-domain terms as interpreted by KFM.  
- `providers` — including:
  - NRCS (producer/licensor).  
  - KFM (processor/host).

### 3.2 KFM Core Extension (`kfm:*`)

Per `stac-ext-kfm-core.md`, the Collection SHOULD include:

- `kfm:dataset_id = "urn:kfm:dataset:gnatsgo-ks-2025"` (or equivalent).  
- `kfm:domain = "soils"` (or `"geoscience"` if that’s the standard).  
- `kfm:release_stage = "stable"`.  
- Optional:
  - `kfm:region_slug = "kansas-statewide"`.  
  - `kfm:review_cycle = "Annual · Geospatial Systems · FAIR+CARE Oversight"`.

### 3.3 FAIR+CARE Extension (`kfmfc:*`, Optional)

For the raw gNATSGO dataset:

- `kfmfc:sensitivity = "general"`  
- `kfmfc:care_label = "Public"`  
- `kfmfc:sovereignty_flag = false`  

Any soils-derived layers intersecting sensitive contexts (e.g., combined with other overlays) should use **separate derived collections/items** with their own governance metadata.

---

## 🌐 4. STAC Items (If Used) — Partitioning Strategy

gNATSGO is inherently **gridded**, so Items may be structured differently than SSURGO.

### 4.1 AOI-Wide Item

- `id = "gnatsgo-2025-ks"`  
- Coverage: entire Kansas AOI.  
- Assets:
  - Zarr/NetCDF/Cloud-Optimized grids for Kansas (single but potentially large object).  
- Use case:
  - Whole-AOI analyses, climate/risk workflows that operate on full grids.

### 4.2 Tile-Based Items

Tiles may follow:

- A regular grid (e.g., 1° x 1°, or a custom tile schema).  
- An existing gNATSGO tiling convention (if NRCS defines one).

**ID pattern examples:**

- `gnatsgo-2025-tile-row<r>-col<c>`  
- `gnatsgo-2025-tile-<index>`  

Each tile Item MUST:

- Provide a `geometry`/`bbox` for the tile.  
- Point to the appropriate grid subset (e.g., COG, Zarr chunk, or tile service).

### 4.3 Region-Based Items (Optional)

Less common but possible:

- Items based on HUC / county / planning region boundaries, where gridded gNATSGO is logically clipped.

All Items MUST:

- Include core STAC fields (`geometry`, `bbox`, `properties.datetime`, `collection`, `links`).  
- Follow KFM naming rules (ASCII-safe, hyphen-separated, stable IDs).

---

## 📦 5. Assets & Access Patterns

Common asset patterns for gNATSGO Items/Collection:

- `data-grid`:
  - `href` → grid file or Zarr/NetCDF dataset.  
  - `type` → `"application/x-zarr"`, `"application/x-netcdf"`, or other appropriate type.  
  - `roles` → `["data"]`.

- `thumbnail`:
  - Preview of one or more key variables (e.g., depth to restrictive layer, water holding capacity).  
  - `roles` → `["thumbnail"]`.

- `metadata`:
  - Additional gridded soils docs.  
  - `roles` → `["metadata"]`.

**Checksums:**

- When feasible, include `checksum:sha256` on `data-grid` assets to:

  - Ensure integrity year-over-year.  
  - Detect accidental corruption or mismatches across storage tiers.

---

## 🔁 6. Relationship to SSURGO & Cross-Year Lineage

gNATSGO is derived, in part, from SSURGO and other sources:

- This Collection should be clearly linked to:
  - The 2025 SSURGO Collection (`../ssurgo-2025/collection.json`).  
  - Prior-year gNATSGO Collections (e.g., `../gnatsgo-2024/collection.json`).

Recommended patterns:

- STAC `links` with relationships like:
  - `"rel": "derived_from"` → 2025 SSURGO Collection.  
  - `"rel": "predecessor"` → 2024 gNATSGO Collection.

- PROV-O (`../../provenance/prov-gnatsgo-2025.jsonld`) encodes:
  - Derivation chain: NRCS gNATSGO upstream + SSURGO baseline → KFM gNATSGO 2025 representation.

These relationships support:

- Time series analyses of gridded soils.  
- Understanding how gNATSGO and SSURGO co-evolve in KFM.

---

## 🧪 7. Validation & CI Expectations

The gNATSGO 2025 STAC Collection and Items MUST pass:

1. **STAC schema validation**:
   - Using `stac-validator` with Collections & Items.  

2. **KFM STAC profile validation**:
   - Presence and correctness of `kfm:*` fields.  
   - Geometry/bbox semantics and temporal fields.  
   - Provider and license fields aligned with NRCS and KFM.

3. **Crosswalk validation**:
   - STAC → DCAT tests ensuring:
     - Identifier, spatial, and temporal alignment.  
     - Appropriate mapping of gNATSGO assets into DCAT `dcat:Distribution`s.  
     - No exposure of internal-only or intermediate assets in public catalogs.

Failures of these checks MUST block:

- Publication of gNATSGO 2025 STAC.  
- Downstream DCAT exports and portal integration for this dataset.

---

## 🕰️ 8. Version History (gNATSGO 2025 STAC Overview)

| Version  | Date       | Author                                   | Summary                                                                 |
|----------|------------|------------------------------------------|-------------------------------------------------------------------------|
| v11.2.3  | 2025-12-03 | Geospatial Systems WG · FAIR+CARE Council | Initial gNATSGO 2025 STAC Collection README; documented structure, asset patterns, relationships to SSURGO and prior-year gNATSGO Collections, and validation expectations. |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — MIT**  
FAIR+CARE Certified · MCP-DL v6.3 · KFM-MDP v11.2.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[⬅ Back to Soils STAC Overview](../README.md) · [⬅ Back to Annual Soils Refresh](../README.md) · [📜 Governance Charter](../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>

