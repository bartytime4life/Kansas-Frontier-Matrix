---
title: "🌐 KFM v11.2.3 — gNATSGO 2024 STAC Items (Kansas AOI) (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
description: "Index and conventions for gNATSGO 2024 STAC Items (tiles/regions) in the Kansas Frontier Matrix annual soils refresh pipeline."
path: "docs/data/soils/annual-refresh/stac/gnatsgo-2024/items/README.md"
version: "v11.2.3"
last_updated: "2025-12-03"

release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Annual · Geospatial Systems · FAIR+CARE Oversight"
content_stability: "stable"
status: "Active / Enforced"
backward_compatibility: "v10.x → v11.x soils-gnatsgo-items-contract compatible"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../../../../../../releases/v11.2.3/manifest.zip"
telemetry_ref: "../../../../../../../releases/v11.2.3/soils-refresh-telemetry.json"
telemetry_schema: "../../../../../../../schemas/telemetry/soils-refresh-v1.json"

governance_ref: "../../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.3"

doc_kind: "STAC Items Index"
intent: "nrcs-soils-gnatsgo-2024-stac-items"

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

json_schema_ref: "../../../../../../../schemas/json/data-soils-annual-refresh-gnatsgo-2024-items-readme-v1.json"
shape_schema_ref: "../../../../../../../schemas/shacl/data-soils-annual-refresh-gnatsgo-2024-items-readme-v1.shape.ttl"

immutability_status: "version-pinned"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"

ttl_policy: "Permanent"
sunset_policy: "Never (per-year soils items form part of the long-term soils baseline)"
---

<div align="center">

# 🌐 gNATSGO 2024 — STAC Items (Kansas AOI)  
`docs/data/soils/annual-refresh/stac/gnatsgo-2024/items/README.md`

**Purpose:**  
Define the **structure, naming, and governance** of **STAC Items** under the **gNATSGO 2024 STAC Collection** in KFM, including:

- How Items are partitioned (AOI-wide, tiles, or regions)  
- How geometries, temporal fields, and assets are modeled  
- How Items align with the **KFM STAC profile** and the soils-refresh provenance/diff pipeline, especially as the **baseline** for gNATSGO 2025  

</div>

---

## 📘 1. Scope

This directory contains **STAC Items** for the **gNATSGO 2024** gridded soils dataset in KFM:

- Each Item is a **spatial subset** or **tile** of gNATSGO 2024 (e.g., AOI-wide, regular tiles, or region-based partitions).  
- All Items are children of the **gNATSGO 2024 STAC Collection** documented in:

  - `../README.md`  
  - `../collection.json`

Items here:

- Serve as **discovery and access units** for 2024 gridded soils.  
- Reference grid assets stored in KFM infrastructure (e.g., Zarr/NetCDF/COG on S3).  
- Provide the **2024 gridded baseline** for soils, used by hydrology, climate, and land-use models and for 2025 diffs.

---

## 🗂️ 2. Directory Layout

~~~text
docs/data/soils/annual-refresh/stac/gnatsgo-2024/items/
│
├── 📄 README.md                         # This file — items index & conventions
│
├── 📄 gnatsgo-2024-ks.json             # (Optional) Kansas-wide Item
├── 📄 gnatsgo-2024-tile-001.json       # Example tile-based Item
├── 📄 gnatsgo-2024-tile-002.json       # Example tile-based Item
├── 📄 gnatsgo-2024-huc8-11030001.json  # Example HUC8-based Item (if used)
└── …                                   # Additional Items per pipeline design
~~~

**Directory contract:**

- Every `*.json` (other than this `README.md`) MUST be a **valid STAC Item**.  
- All Items MUST:
  - Set `"collection"` to the gNATSGO 2024 Collection ID (e.g., `"gnatsgo-2024-ks"`).  
  - Include a `links` entry with `rel: "collection"` pointing to `../collection.json`.  
  - Adhere to the **KFM STAC profile** and soils-specific patterns.

---

## 🧱 3. Item Granularity & Naming Conventions

KFM may reuse the same itemization strategy as gNATSGO 2025 for 2024, to simplify diffs and cross-year comparisons.

### 3.1 AOI-Wide Item

- **ID:** `gnatsgo-2024-ks`  
- **Use case:**  
  - Whole-AOI analyses for 2024 soils grids.  
  - Catalog-level browsing and some model workflows.

### 3.2 Tile-Based Items (Recommended for Grids)

For operational gridded workflows:

- **ID pattern:** `gnatsgo-2024-tile-<tile-id>`  
  - Example: `gnatsgo-2024-tile-001`, `gnatsgo-2024-tile-row03-col07`.  
- **Geometry/bbox:**  
  - Spatial extent of each tile.  
- **Use case:**  
  - Efficient tiled access for web services and large-scale computations.  
  - Alignment with standard KFM tile schemas.

### 3.3 Region-Based Items (Optional)

Items may also be partitioned by:

- HUC8 or other hydrologic regions.  
- Counties or planning regions.

**Examples:**

- `gnatsgo-2024-huc8-11030001`  
- `gnatsgo-2024-county-<FIPS>`

**Naming rules:**

- IDs MUST be:
  - ASCII-safe and hyphen-separated.  
  - Stable across re-runs of the 2024 pipeline.  
  - Lowercase where practical.

---

## 🌍 4. Core STAC Fields per Item

Each gNATSGO 2024 Item MUST include:

- `stac_version` — `1.0.x`, matching Collection.  
- `type` — `"Feature"`.  
- `id` — following naming conventions above.  
- `geometry` — valid GeoJSON polygon/multipolygon representing the subset/tile.  
- `bbox` — derived from `geometry`.  
- `properties.datetime` — soils refresh effective date (e.g., `"2024-10-01T00:00:00Z"`).  
- `collection` — ID of the gNATSGO 2024 Collection.  
- `links` — minimally:
  - `rel: "self"`  
  - `rel: "collection"` → `../collection.json`  
  - `rel: "root"` → soils STAC root, if used.

### 4.1 KFM Core & FAIR+CARE Extensions

Items SHOULD (or MUST, per soils standards) include:

- `kfm:dataset_id` — same as the Collection (`urn:kfm:dataset:gnatsgo-ks-2024`) or a region-specific derivative if applicable.  
- `kfm:domain = "soils"`  
- `kfm:release_stage = "stable"`

Typical FAIR+CARE extension (`kfmfc:*`) for raw gNATSGO:

- `kfmfc:sensitivity = "general"`  
- `kfmfc:care_label = "Public"`  
- `kfmfc:sovereignty_flag = false`  

Any derived or combined products that intersect sensitive/sovereignty contexts must use **separate collections/items** with their own governance metadata.

---

## 📦 5. Assets & Access Patterns

Each Item’s `assets` block exposes gridded soils data for that subset or tile.

### 5.1 Common Asset Types

Examples (implementation-dependent):

- `data-grid`:
  - `href` → grid dataset (e.g., Zarr, NetCDF, COG) for this tile or region.  
  - `type` → `"application/x-zarr"`, `"application/x-netcdf"`, or appropriate MIME.  
  - `roles` → `["data"]`.

- `thumbnail`:
  - `href` → PNG/WEBP preview of a key variable (e.g., depth to restrictive layer).  
  - `roles` → `["thumbnail"]`.

- `metadata`:
  - `href` → per-tile/regional docs or summary stats (if generated).  
  - `roles` → `["metadata"]`.

### 5.2 Integrity

Where practical:

- Include `checksum:sha256` on `data-grid` assets for:
  - Integrity checking across pipeline runs.  
  - Detecting tile-level corruption or mismatches.

---

## 🔁 6. Relationship to SSURGO, Deltas & Baseline Role

gNATSGO 2024 Items:

- Form the **gridded baseline** that 2025 gNATSGO Items will be compared against.  
- Are conceptually derived from SSURGO 2024 and other sources (modeled in Collection-level provenance).

Per-subset relationships:

- If tiling/partitioning is **consistent** between 2024 and 2025:
  - Item IDs (e.g., `gnatsgo-2024-tile-001` vs `gnatsgo-2025-tile-001`) can be used to align diff analysis per tile.  
- Provenance and diff logic should be documented in:
  - `../../processing/README.md`  
  - `../../processing/diff-report-2025.md`  
  - `../../provenance/prov-gnatsgo-2025.jsonld`

---

## 🧪 7. Validation & CI Expectations

All Items under `gnatsgo-2024/items/` MUST pass:

1. **STAC Item schema validation** via `stac-validator`.  
2. **KFM STAC profile checks**:
   - Core fields (geometry, bbox, datetime, collection, links).  
   - `kfm:*` fields as required.  
   - Temporal semantics consistent with 2024 gNATSGO refresh.

3. **Crosswalk readiness**:
   - STAC → DCAT tests confirming:
     - Item metadata consistent with the gNATSGO 2024 Collection.  
     - Correct mapping of `data-grid` assets to DCAT `dcat:Distribution`s.  
     - No internal-only or test assets exposed in public DCAT.

CI MUST prevent:

- Addition of Items that violate naming, profile, or governance rules.  
- Silent structural changes that break historical comparability or cross-year diffs.

---

## 🕰️ 8. Version History (Items Index)

| Version  | Date       | Author                                   | Summary                                                                 |
|----------|------------|------------------------------------------|-------------------------------------------------------------------------|
| v11.2.3  | 2025-12-03 | Geospatial Systems WG · FAIR+CARE Council | Initial gNATSGO 2024 STAC Items README; defined naming, granularity options, asset patterns, baseline role, and validation expectations. |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — MIT**  
FAIR+CARE Certified · MCP-DL v6.3 · KFM-MDP v11.2.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[⬅ Back to gNATSGO 2024 STAC Collection](../README.md) · [⬅ Back to Soils STAC Overview](../../README.md) · [📜 Governance Charter](../../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>

