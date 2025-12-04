---
title: "🌐 KFM v11.2.3 — SSURGO 2024 STAC Items (Kansas AOI) (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
description: "Index and conventions for SSURGO 2024 STAC Items (tiles/regions) in the Kansas Frontier Matrix annual soils refresh pipeline."
path: "docs/data/soils/annual-refresh/stac/ssurgo-2024/items/README.md"
version: "v11.2.3"
last_updated: "2025-12-03"

release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Annual · Geospatial Systems · FAIR+CARE Oversight"
content_stability: "stable"
status: "Active / Enforced"
backward_compatibility: "v10.x → v11.x soils-ssurgo-items-contract compatible"

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
intent: "nrcs-soils-ssurgo-2024-stac-items"

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

json_schema_ref: "../../../../../../../schemas/json/data-soils-annual-refresh-ssurgo-2024-items-readme-v1.json"
shape_schema_ref: "../../../../../../../schemas/shacl/data-soils-annual-refresh-ssurgo-2024-items-readme-v1.shape.ttl"

immutability_status: "version-pinned"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"

ttl_policy: "Permanent"
sunset_policy: "Never (per-year soils items form part of the long-term soils baseline)"
---

<div align="center">

# 🌐 SSURGO 2024 — STAC Items (Kansas AOI)  
`docs/data/soils/annual-refresh/stac/ssurgo-2024/items/README.md`

**Purpose:**  
Define the **structure, naming, and governance** of **STAC Items** under the **SSURGO 2024 STAC Collection** in KFM, including:

- How Items are partitioned (AOI, HUC, county, or tiles)  
- How geometries, temporal fields, and assets are modeled  
- How Items align with the **KFM STAC profile** and the soils-refresh provenance/diff pipeline, especially as the **baseline** for 2025 diffs  

</div>

---

## 📘 1. Scope

This directory contains **STAC Items** for the **SSURGO 2024** soils dataset in KFM:

- Each Item is a **spatial subset** of SSURGO 2024 (e.g., AOI-wide, HUC-level, county-level, or tiling scheme).  
- All Items are children of the **SSURGO 2024 STAC Collection** documented in:

  - `../README.md`  
  - `../collection.json`

Items here:

- Serve as **discovery and access units** for SSURGO 2024 in KFM.  
- Reference data assets in KFM storage (e.g., S3/Cloud-Optimized vectors).  
- Provide the **per-region baseline** for 2024 used in 2025 soils diffs and downstream modeling.

---

## 🗂️ 2. Directory Layout

~~~text
docs/data/soils/annual-refresh/stac/ssurgo-2024/items/
│
├── 📄 README.md                       # This file — items index & conventions
│
├── 📄 ssurgo-2024-ks.json            # (Optional) Kansas-wide Item
├── 📄 ssurgo-2024-huc8-11030001.json # Example HUC8-based Item
├── 📄 ssurgo-2024-huc8-11030002.json # Example HUC8-based Item
├── 📄 ssurgo-2024-county-XYZ.json    # Example county-based Item(s), if used
└── …                                 # Additional Items per pipeline design
~~~

**Directory contract:**

- Every `*.json` (except this `README.md`) MUST be a **valid STAC Item**.  
- All Items MUST:
  - Set `"collection"` to the SSURGO 2024 Collection ID (e.g., `"ssurgo-2024-ks"`).  
  - Include a `links` entry with `rel: "collection"` pointing to `../collection.json`.  
  - Adhere to the **KFM STAC profile** and soils-specific patterns.

---

## 🧱 3. Item Granularity & Naming Conventions

KFM recommends the same patterns used for SSURGO 2025, applied to 2024:

### 3.1 AOI-Wide Item

- **ID:** `ssurgo-2024-ks`  
- **Use case:**  
  - High-level access to “all SSURGO 2024 soils for Kansas AOI”.  
  - Useful for catalog browsing and some analysis, but may be heavy for map tiling.

### 3.2 HUC8-Based Items (Hydrology Alignment)

- **ID pattern:** `ssurgo-2024-huc8-<HUC8>`  
  - Example: `ssurgo-2024-huc8-11030001`  
- **Geometry/bbox:**  
  - HUC8 watershed boundary intersected with SSURGO coverage.  
- **Use case:**  
  - Hydrology-aware soils subsets.  
  - Alignment with other HUC8-indexed hydrology datasets in KFM.

### 3.3 County-/Region-Based Items (Optional)

- **ID pattern:** `ssurgo-2024-county-<FIPS>` or `ssurgo-2024-region-<slug>`.  
- **Use case:**  
  - County/region-centric planning, overlays in Story Nodes & Focus Mode.

**Naming rules:**

- IDs MUST be stable, ASCII-safe, hyphen-separated; lowercasing is recommended.

---

## 🌍 4. Core STAC Fields per Item

Each SSURGO 2024 Item MUST include:

- `stac_version` — `1.0.x` (matching Collection).  
- `type` — `"Feature"`.  
- `id` — following the naming conventions above.  
- `geometry` — valid GeoJSON polygon/multipolygon for the subset.  
- `bbox` — derived from `geometry`.  
- `properties.datetime` — soils refresh effective date (e.g., `"2024-10-01T00:00:00Z"`).  
- `collection` — ID of the SSURGO 2024 Collection.  
- `links` — minimally:
  - `rel: "self"`  
  - `rel: "collection"` → `../collection.json`  
  - `rel: "root"` → soils STAC root, if used.

### 4.1 KFM Core & FAIR+CARE Extensions

Items SHOULD (or MUST, depending on internal soils standards) include:

- `kfm:dataset_id` — same as Collection (`urn:kfm:dataset:ssurgo-ks-2024`) or a region-specific derivative if designed.  
- `kfm:domain = "soils"`  
- `kfm:release_stage = "stable"`

Typical FAIR+CARE extension (`kfmfc:*`) for raw soils:

- `kfmfc:sensitivity = "general"`  
- `kfmfc:care_label = "Public"`  
- `kfmfc:sovereignty_flag = false`  

Derived or combined products that intersect sensitive contexts should carry additional governance metadata in **their own collections/items**, not by altering the raw SSURGO 2024 Items.

---

## 📦 5. Assets & Access Patterns

Each Item’s `assets` block exposes soils data for that subset.

### 5.1 Common Asset Types

Examples (actual formats depend on implementation):

- `data-vector`:
  - `href` → Cloud-optimized vector subset (e.g., FlatGeobuf, GeoPackage, FileGDB).  
  - `type` → appropriate vector MIME type.  
  - `roles` → `["data"]`.

- `thumbnail`:
  - `href` → small PNG/WEBP preview.  
  - `roles` → `["thumbnail"]`.

- `metadata`:
  - `href` → additional documentation for the region (if any).  
  - `roles` → `["metadata"]`.

### 5.2 Integrity

Where feasible, **data assets** SHOULD include:

- `checksum:sha256` — to support:
  - Integrity checking over time.  
  - Consistency across downstream copies and external catalogs.

---

## 🔁 6. Relationship to Deltas & Baseline Role

SSURGO 2024 Items form the **baseline** for:

- Geometry and tabular diffs used in:
  - `../processing/diff-report-2025.md`  
  - `../deltas/geometry-diff-2024-2025.parquet`  
  - `../deltas/tabular-diff-2024-2025.parquet`

Patterns:

- Items in `ssurgo-2025/items/` may have alignable IDs (e.g., `ssurgo-2025-huc8-11030001`) so diffing is simpler per subset.  
- PROV-O and lineage events (`../provenance/`) should reflect:
  - 2024 Items as inputs.  
  - 2025 Items as derived entities.

This README does not enforce a specific per-subset diff scheme, but any such scheme MUST be:

- Documented in `processing/README.md` and diff report docs.  
- Reflected in STAC links and/or asset metadata as needed.

---

## 🧪 7. Validation & CI Expectations

All Items under `ssurgo-2024/items/` MUST pass:

1. **STAC Item schema validation** via `stac-validator`.  
2. **KFM STAC profile checks**, including:
   - Required core fields (geometry, bbox, datetime, collection, links).  
   - KFM core extension fields (`kfm:*`) where required.  
   - Temporal semantics consistent with 2024 NRCS refresh.  
3. **Crosswalk readiness**:
   - STAC → DCAT tests verifying:
     - Identifier, spatial, and temporal alignment with the Collection.  
     - Correct mapping of soils assets into DCAT `dcat:Distribution`s.  
     - No internal-only or sensitive assets appearing in public DCAT.

CI must prevent:

- Addition of new Items that violate profile or naming conventions.  
- Silent changes to existing Items that undermine historical comparability.

---

## 🕰️ 8. Version History (Items Index)

| Version  | Date       | Author                                   | Summary                                                                 |
|----------|------------|------------------------------------------|-------------------------------------------------------------------------|
| v11.2.3  | 2025-12-03 | Geospatial Systems WG · FAIR+CARE Council | Initial SSURGO 2024 STAC Items README; defined naming, granularity options, asset patterns, baseline role, and validation expectations. |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — MIT**  
FAIR+CARE Certified · MCP-DL v6.3 · KFM-MDP v11.2.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[⬅ Back to SSURGO 2024 STAC Collection](../README.md) · [⬅ Back to Soils STAC Overview](../../README.md) · [📜 Governance Charter](../../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>

