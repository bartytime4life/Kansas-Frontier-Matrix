---
title: "🌐 KFM v11.2.3 — gNATSGO 2024 STAC Collection (Kansas AOI) (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
description: "STAC Collection overview for the 2024 NRCS gNATSGO gridded soils dataset (Kansas AOI) in the Kansas Frontier Matrix annual soils refresh pipeline."
path: "docs/data/soils/annual-refresh/stac/gnatsgo-2024/README.md"
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
intent: "nrcs-soils-gnatsgo-2024-stac"

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

json_schema_ref: "../../../../../../schemas/json/data-soils-annual-refresh-gnatsgo-2024-stac-readme-v1.json"
shape_schema_ref: "../../../../../../schemas/shacl/data-soils-annual-refresh-gnatsgo-2024-stac-readme-v1.shape.ttl"

immutability_status: "version-pinned"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"

ttl_policy: "Permanent"
sunset_policy: "Never (per-year soils collections form the long-term soils baseline)"
---

<div align="center">

# 🌐 gNATSGO 2024 — STAC Collection (Kansas AOI)  
`docs/data/soils/annual-refresh/stac/gnatsgo-2024/README.md`

**Purpose:**  
Describe the **2024 gNATSGO STAC Collection** for the Kansas Frontier Matrix annual soils refresh, including:

- How `collection.json` is structured and governed  
- How Items (if used) are organized and linked  
- How this Collection participates in cross-year soils versioning and the **STAC-first → DCAT-derived** KFM catalog model  

</div>

---

## 📘 1. Scope

This directory corresponds to the **KFM STAC representation** of the **2024 NRCS gNATSGO gridded soils dataset** over the KFM area of interest (typically Kansas and any governance-defined buffers).

Contents:

- `collection.json` — the **authoritative STAC Collection** for gNATSGO 2024 in KFM.  
- `items/` — optional per-tile / per-region Items if the pipeline exposes finer-grain STAC entries.

This Collection is:

- Derived from **raw NRCS gNATSGO 2024 bundles** stored under `../../../../raw/`.  
- Governed by the **Annual Soils Refresh pipeline** (`../../README.md` and `../../processing/README.md`).  
- Conforming to the **KFM STAC profile** and extensions under `docs/standards/catalogs/stac/`.

It serves as the **gridded soils baseline** for the 2025 gNATSGO refresh and downstream models.

---

## 🗂️ 2. Directory Layout (gNATSGO 2024 STAC)

~~~text
docs/data/soils/annual-refresh/stac/gnatsgo-2024/
│
├── 📄 README.md               # This file — gNATSGO 2024 STAC overview
│
├── 📄 collection.json         # STAC Collection for gNATSGO 2024 (KFM STAC profile-compliant)
│
└── 📂 items/                  # (Optional) per-tile or per-region Items
    ├── 📄 gnatsgo-2024-ks.json          # Example: Kansas-wide Item (if used)
    ├── 📄 gnatsgo-2024-tile-001.json    # Example: tile-based Items (if used)
    └── …                                # Additional Items per tiling/partition strategy
~~~

**Directory contract:**

- `collection.json` MUST exist and be **STAC 1.0.x** compliant.  
- If `items/` is present:
  - All Items MUST set `"collection"` to the gNATSGO 2024 Collection ID.  
  - Items MUST include `links` pointing to the Collection and STAC root.  
  - Items MUST adhere to the **KFM STAC profile** and soils best practices.

---

## 🧱 3. STAC Collection Profile (gNATSGO 2024)

The `collection.json` file for gNATSGO 2024 MUST satisfy:

### 3.1 Core STAC Fields

- `stac_version = "1.0.0"` (or compatible `1.0.x`).  
- `type = "Collection"`.  
- `id` — recommended: `gnatsgo-2024-ks` (or similar AOI-specific identifier).  
- `description` — e.g.:

  > “NRCS gNATSGO 2024 gridded soils dataset for Kansas as processed by the KFM annual soils refresh (gridded attributes and interpretations).”

- `extent.spatial` — bounding boxes for the gNATSGO coverage over KFM AOI.  
- `extent.temporal` — temporal extent of this release (e.g., effective reference date in 2024).  
- `license` — NRCS/public-domain terms as interpreted by KFM.  
- `providers` — including:
  - NRCS (producer/licensor).  
  - KFM (processor/host).

### 3.2 KFM Core Extension (`kfm:*`)

Per `stac-ext-kfm-core.md`, the Collection SHOULD include:

- `kfm:dataset_id = "urn:kfm:dataset:gnatsgo-ks-2024"` (or equivalent).  
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

gNATSGO is inherently **gridded**, so Items may be structured similarly to gNATSGO 2025:

### 4.1 AOI-Wide Item

- `id = "gnatsgo-2024-ks"`  
- Coverage: entire Kansas AOI.  
- Assets:
  - Zarr/NetCDF/COG grids for Kansas (single large artifact).

### 4.2 Tile-Based Items

Tiles may follow:

- A regular grid (e.g., 1°×1°, custom KFM tile schema).  
- Or an existing gNATSGO tiling convention, if NRCS defines one.

**ID pattern examples:**

- `gnatsgo-2024-tile-001`  
- `gnatsgo-2024-tile-row03-col07`

Each tile Item MUST:

- Provide `geometry`/`bbox` for the tile.  
- Point to the appropriate grid subset (COG, Zarr chunk, or service endpoint).

### 4.3 Region-Based Items (Optional)

Items based on HUC / county / planning region boundaries are also possible, mainly when region-specific workflows rely on gridded soils.

---

## 📦 5. Assets & Access Patterns

Common asset patterns for gNATSGO 2024 Items/Collection:

- `data-grid`:
  - `href` → grid dataset for this AOI/tile/region (e.g., Zarr, NetCDF, COG).  
  - `type` → `"application/x-zarr"`, `"application/x-netcdf"`, or suitable MIME.  
  - `roles` → `["data"]`.

- `thumbnail`:
  - `href` → PNG/WEBP preview of one or more key soil variables.  
  - `roles` → `["thumbnail"]`.

- `metadata`:
  - `href` → additional documentation or index for the grid dataset.  
  - `roles` → `["metadata"]`.

**Checksums:**

- Data assets SHOULD include `checksum:sha256` where feasible, to support:

  - Integrity checking.  
  - Consistency across storage tiers and federated catalogs.

---

## 🔁 6. Relationship to SSURGO & Cross-Year Lineage

As a gridded product derived (in part) from SSURGO:

- gNATSGO 2024 Collection should link to:
  - 2024 SSURGO Collection:
    - Via STAC `links` (e.g., `"rel": "derived_from"`).  

- As the **baseline** for gNATSGO 2025:
  - 2025 gNATSGO Collection should reference 2024 via:
    - `rel: "predecessor"` (in STAC) or equivalent.  
  - PROV-O records (`../../provenance/prov-gnatsgo-2025.jsonld`) must capture:
    - Derivation from the 2024 KFM soils baseline and 2025 upstream bundles.

These relationships support:

- Soils time series analysis.  
- Understanding how gridded soils change year-over-year in KFM.

---

## 🧪 7. Validation & CI Expectations for gNATSGO 2024

`collection.json` and any Items under this directory MUST pass:

1. **STAC schema validation**:
   - Core Collection & Item schemas.  

2. **KFM STAC profile validation**:
   - `kfm:*` fields present and valid.  
   - Temporal and spatial coverage consistent with 2024 NRCS release.  
   - Provider and license fields correct.

3. **Crosswalk validation**:
   - STAC → DCAT crosswalk tests:
     - `dct:identifier`, `dct:spatial`, `dct:temporal` correct and consistent.  
     - Data-grid assets correctly mapped to DCAT `dcat:Distribution`s.  
     - No internal-only artifacts included in public DCAT.

CI MUST block:

- Publication of gNATSGO 2024 STAC if any validation fails.  
- Downstream DCAT/portal exports until validation and governance checks pass.

---

## 🕰️ 8. Version History (gNATSGO 2024 STAC Overview)

| Version  | Date       | Author                                   | Summary                                                                 |
|----------|------------|------------------------------------------|-------------------------------------------------------------------------|
| v11.2.3  | 2025-12-03 | Geospatial Systems WG · FAIR+CARE Council | Initial gNATSGO 2024 STAC Collection README; documented structure, baseline role for 2025, relationships to SSURGO, and validation expectations. |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — MIT**  
FAIR+CARE Certified · MCP-DL v6.3 · KFM-MDP v11.2.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[⬅ Back to Soils STAC Overview](../README.md) · [⬅ Back to Annual Soils Refresh](../README.md) · [📜 Governance Charter](../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>

