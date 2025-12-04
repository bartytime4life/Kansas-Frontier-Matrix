---
title: "🌐 KFM v11.2.3 — gNATSGO 2025 STAC Items (Kansas AOI) (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
description: "Index and conventions for gNATSGO 2025 STAC Items (tiles/regions) in the Kansas Frontier Matrix annual soils refresh pipeline."
path: "docs/data/soils/annual-refresh/stac/gnatsgo-2025/items/README.md"
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

governance_ref: "../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.3"

doc_kind: "STAC Items Index"
intent: "nrcs-soils-gnatsgo-2025-stac-items"

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

json_schema_ref: "../../../../../../../schemas/json/data-soils-annual-refresh-gnatsgo-2025-items-readme-v1.json"
shape_schema_ref: "../../../../../../../schemas/shacl/data-soils-annual-refresh-gnatsgo-2025-items-readme-v1.shape.ttl"

immutability_status: "version-pinned"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"

ttl_policy: "Permanent"
sunset_policy: "Never (per-year soils items form part of the long-term soils baseline)"
---

<div align="center">

# 🌐 gNATSGO 2025 — STAC Items (Kansas AOI)  
`docs/data/soils/annual-refresh/stac/gnatsgo-2025/items/README.md`

**Purpose:**  
Define the **structure, naming, and governance** of **STAC Items** under the **gNATSGO 2025 STAC Collection** in KFM, including:

- How Items are partitioned (AOI-wide, tiles, or regions)  
- How geometries, temporal fields, and assets are modeled  
- How Items align with the **KFM STAC profile** and the soils-refresh provenance/diff pipeline  

</div>

---

## 📘 1. Scope

This directory contains **STAC Items** for the **gNATSGO 2025** gridded soils dataset in KFM:

- Each Item is a **spatial subset** or **tile** of gNATSGO 2025 (e.g., AOI-wide, regular tiles, or region-based partitions).  
- All Items are children of the **gNATSGO 2025 STAC Collection** documented in:

  - `../README.md`  
  - `../collection.json`

Items here:

- Serve as **discovery and access units** for gridded soils in KFM.  
- Reference grid assets stored in KFM infrastructure (e.g., Zarr/NetCDF/COG on S3).  
- Provide the gridded soils **baseline for 2025** used by hydrology, climate, and land-use models.

---

## 🗂️ 2. Directory Layout

~~~text
docs/data/soils/annual-refresh/stac/gnatsgo-2025/items/
│
├── 📄 README.md                         # This file — items index & conventions
│
├── 📄 gnatsgo-2025-ks.json             # (Optional) Kansas-wide Item
├── 📄 gnatsgo-2025-tile-001.json       # Example tile-based Item
├── 📄 gnatsgo-2025-tile-002.json       # Example tile-based Item
├── 📄 gnatsgo-2025-huc8-11030001.json  # Example HUC8-based Item (if used)
└── …                                   # Additional Items per pipeline design
~~~

**Directory contract:**

- Every `*.json` (other than this `README.md`) MUST be a **valid STAC Item**.  
- All Items MUST:
  - Set `"collection"` to the gNATSGO 2025 Collection ID (e.g., `"gnatsgo-2025-ks"`).  
  - Include a `links` entry with `rel: "collection"` pointing to `../collection.json`.  
  - Adhere to the **KFM STAC profile** and soils-specific patterns.

---

## 🧱 3. Item Granularity & Naming Conventions

KFM may choose a combination of the following patterns, depending on performance and modeling needs.

### 3.1 AOI-Wide Item

- **ID:** `gnatsgo-2025-ks`  
- **Use case:**  
  - Whole-AOI analyses where reading the full grid is feasible.  
  - Catalog browsing and summary usage.

### 3.2 Tile-Based Items (Recommended for Grids)

For operational gridded use:

- **ID pattern:** `gnatsgo-2025-tile-<tile-id>`  
  - Example: `gnatsgo-2025-tile-001`, or `gnatsgo-2025-tile-row03-col07`.  
- **Geometry/bbox:**  
  - The spatial extent of each tile.  
- **Use case:**  
  - Efficient tiled access for web services and compute workloads.  
  - Alignment with standard grid/tile systems in KFM.

### 3.3 Region-Based Items (Optional)

Items may additionally be partitioned by:

- HUC8 or other hydrologic units.  
- Counties or planning regions.

**ID examples:**

- `gnatsgo-2025-huc8-11030001`  
- `gnatsgo-2025-county-<FIPS>`  

**Naming rules (all patterns):**

- IDs MUST be:
  - ASCII-safe.  
  - Hyphen-separated.  
  - Stable across re-runs of the 2025 pipeline.  
  - Lowercase where practical.

---

## 🌍 4. Core STAC Fields per Item

Each gNATSGO 2025 Item MUST include:

- `stac_version` — `1.0.x`, matching Collection.  
- `type` — `"Feature"`.  
- `id` — following the naming conventions above.  
- `geometry` — valid GeoJSON polygon/multipolygon for the subset/tile extent.  
- `bbox` — derived from `geometry`.  
- `properties.datetime` — soils refresh effective date (e.g., `"2025-10-01T00:00:00Z"`).  
- `collection` — ID of the gNATSGO 2025 Collection.  
- `links` — minimally:
  - `rel: "self"`  
  - `rel: "collection"` → `../collection.json`  
  - `rel: "root"` → soils STAC root, if used.

### 4.1 KFM Core & FAIR+CARE Extensions

Items SHOULD (or MUST, per internal standards) include:

- `kfm:dataset_id` — same as the Collection (`urn:kfm:dataset:gnatsgo-ks-2025`) or a region-specific derivative if used.  
- `kfm:domain = "soils"`  
- `kfm:release_stage = "stable"`

FAIR+CARE extension (`kfmfc:*`) is typically minimal for raw gNATSGO:

- `kfmfc:sensitivity = "general"`  
- `kfmfc:care_label = "Public"`  
- `kfmfc:sovereignty_flag = false`  

Any derived or combined products that intersect sensitive contexts should use **their own** collections/items with appropriate governance metadata.

---

## 📦 5. Assets & Access Patterns

Each Item’s `assets` block exposes grid data for that subset or tile.

### 5.1 Common Asset Types

Likely asset patterns (depending on implementation):

- `data-grid`:
  - `href` → grid dataset for this tile/region (e.g., Zarr, NetCDF, COG).  
  - `type` → `"application/x-zarr"`, `"application/x-netcdf"`, or appropriate MIME.  
  - `roles` → `["data"]`.

- `thumbnail`:
  - `href` → PNG/WEBP preview of one or more key soil variables.  
  - `roles` → `["thumbnail"]`.

- `metadata`:
  - `href` → additional documentation or summarizing stats (if per-tile/regional docs exist).  
  - `roles` → `["metadata"]`.

### 5.2 Integrity

Where feasible:

- **Data assets** SHOULD include `checksum:sha256` to support:
  - Integrity checks for tiles/grids.  
  - Consistency checks between KFM layers and external federations.

---

## 🔁 6. Relationship to SSURGO, Deltas & Provenance

gNATSGO tiles/items:

- Are **derived**, in part, from SSURGO 2025 and other upstream sources.  
- Should be linked, via Collection-level or Item-level `links` and/or PROV-O, to:
  - SSURGO 2025 Collection (`../ssurgo-2025/collection.json`).  
  - Diff outputs when gNATSGO-specific changes are tracked.

Per-subset/tiling diff and provenance patterns (if implemented) MUST be:

- Documented in `../../processing/README.md` and `diff-report-2025.md`.  
- Reflected in KFM PROV-O records (`../provenance/prov-gnatsgo-2025.jsonld`).

---

## 🧪 7. Validation & CI Expectations

All Items under `gnatsgo-2025/items/` MUST pass:

1. **STAC Item schema validation** via `stac-validator`.  
2. **KFM STAC profile checks**, including:
   - Presence of `geometry`, `bbox`, `properties.datetime`, `collection`, `links`.  
   - Correct use of `kfm:*` fields.  
   - Consistent temporal semantics (2025 refresh date).  
3. **Crosswalk readiness**:
   - STAC → DCAT tests verifying:
     - Item-level metadata consistent with the gNATSGO 2025 Collection.  
     - Correct mapping of `data-grid` assets to DCAT `dcat:Distribution`s.  
     - No internal-only assets exposed in public DCAT.

CI MUST prevent:

- Adding Items that violate naming or profile rules.  
- Silent changes to Items that undermine historical comparability.

---

## 🕰️ 8. Version History (Items Index)

| Version  | Date       | Author                                   | Summary                                                                 |
|----------|------------|------------------------------------------|-------------------------------------------------------------------------|
| v11.2.3  | 2025-12-03 | Geospatial Systems WG · FAIR+CARE Council | Initial gNATSGO 2025 STAC Items README; defined naming, granularity options, asset patterns, and validation expectations. |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — MIT**  
FAIR+CARE Certified · MCP-DL v6.3 · KFM-MDP v11.2.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[⬅ Back to gNATSGO 2025 STAC Collection](../README.md) · [⬅ Back to Soils STAC Overview](../../README.md) · [📜 Governance Charter](../../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>

