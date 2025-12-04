---
title: "🌐 KFM v11.2.3 — SSURGO 2025 STAC Items (Kansas AOI) (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
description: "Index and conventions for SSURGO 2025 STAC Items (tiles/regions) in the Kansas Frontier Matrix annual soils refresh pipeline."
path: "docs/data/soils/annual-refresh/stac/ssurgo-2025/items/README.md"
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
intent: "nrcs-soils-ssurgo-2025-stac-items"

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

json_schema_ref: "../../../../../../../schemas/json/data-soils-annual-refresh-ssurgo-2025-items-readme-v1.json"
shape_schema_ref: "../../../../../../../schemas/shacl/data-soils-annual-refresh-ssurgo-2025-items-readme-v1.shape.ttl"

immutability_status: "version-pinned"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"

ttl_policy: "Permanent"
sunset_policy: "Never (per-year soils items form part of the long-term soils baseline)"
---

<div align="center">

# 🌐 SSURGO 2025 — STAC Items (Kansas AOI)  
`docs/data/soils/annual-refresh/stac/ssurgo-2025/items/README.md`

**Purpose:**  
Define the **structure, naming, and governance** of **STAC Items** under the **SSURGO 2025 STAC Collection** in KFM, including:

- How Items are partitioned (AOI, HUC, county, or tiles)  
- How geometries, temporal fields, and assets are modeled  
- How Items align with the **KFM STAC profile** and soils-refresh provenance/diff pipeline  

</div>

---

## 📘 1. Scope

This directory contains **STAC Items** for the **SSURGO 2025** soils dataset in KFM:

- Each Item is a **spatial subset** of SSURGO 2025 (e.g., AOI-wide, HUC-level, county-level, or tiling scheme).  
- Items are children of the **SSURGO 2025 STAC Collection** documented in:

  - `../README.md`  
  - `../collection.json`

Items here:

- Are **discovery and access units** for soils in KFM.  
- Reference data assets held in KFM storage (e.g., S3/Cloud-Optimized vector formats).  
- Enable downstream pipelines and web maps to retrieve SSURGO subsets efficiently.

---

## 🗂️ 2. Directory Layout

~~~text
docs/data/soils/annual-refresh/stac/ssurgo-2025/items/
│
├── 📄 README.md                       # This file — items index & conventions
│
├── 📄 ssurgo-2025-ks.json            # (Optional) Kansas-wide Item
├── 📄 ssurgo-2025-huc8-11030001.json # Example HUC8-based Item
├── 📄 ssurgo-2025-huc8-11030002.json # Example HUC8-based Item
├── 📄 ssurgo-2025-county-XYZ.json    # Example county-based Item(s), if used
└── …                                 # Additional Items per pipeline design
~~~

**Directory contract:**

- All `*.json` files (other than this `README.md`) MUST be **valid STAC Items**.  
- All Items MUST:
  - Set `"collection"` to the SSURGO 2025 Collection ID (e.g., `"ssurgo-2025-ks"`).  
  - Include a `links` entry with `rel: "collection"` pointing to `../collection.json`.  
  - Adhere to the **KFM STAC profile** and soils-specific rules.

---

## 🧱 3. Item Granularity & Naming Conventions

KFM recommends the following patterns (actual choice defined by soils pipeline design):

### 3.1 AOI-Wide Item

- **ID:** `ssurgo-2025-ks`  
- **Use case:**  
  - Quick reference to “all SSURGO 2025 soils for Kansas AOI”.  
  - May have large geometry/bbox; best for catalog-level browsing, less for tiling.

### 3.2 HUC8-Based Items (Recommended for Hydrology Alignment)

- **ID pattern:** `ssurgo-2025-huc8-<HUC8>`  
  - Example: `ssurgo-2025-huc8-11030001`  
- **Geometry/bbox:**  
  - Derived from the HUC8 watershed boundary intersected with SSURGO coverage.  
- **Use case:**  
  - Hydrology & watershed-model-aware soils subsets.  
  - Alignment with other HUC8-indexed datasets in KFM.

### 3.3 County-/Planning-Region-Based Items (Optional)

- **ID pattern:** `ssurgo-2025-county-<FIPS>` or `ssurgo-2025-region-<slug>`  
- **Use case:**  
  - County-centric planning workflows.  
  - Regional overlays in Story Nodes & Focus Mode.

**Naming rules:**

- IDs MUST be:
  - Lowercase where practical.  
  - ASCII-safe.  
  - Hyphen-separated.  
  - Stable across re-runs of the 2025 pipeline.

---

## 🌍 4. Core STAC Fields per Item

Each Item MUST include:

- `stac_version` — `1.0.x` (matching Collection).  
- `type` — `"Feature"`.  
- `id` — following naming patterns above.  
- `geometry` — valid GeoJSON polygon/multipolygon covering the subset.  
- `bbox` — derived from `geometry`.  
- `properties.datetime` — soils refresh effective date (e.g., `"2025-10-01T00:00:00Z"`).  
- `collection` — ID of SSURGO 2025 Collection.  
- `links` — at least:
  - `rel: "self"`  
  - `rel: "collection"` → `../collection.json`  
  - `rel: "root"` → soils STAC root, if used.

### 4.1 KFM Core & FAIR+CARE Extensions

Items SHOULD (or MUST, depending on internal standards) include:

- `kfm:dataset_id` — same as Collection, or a region-specific derivative if defined.  
- `kfm:domain = "soils"`  
- `kfm:release_stage = "stable"`

FAIR+CARE extension (`kfmfc:*`) is usually minimal for soils:

- `kfmfc:sensitivity = "general"`  
- `kfmfc:care_label = "Public"`  
- `kfmfc:sovereignty_flag = false`  

Unless this particular Item carries additional governance context (e.g., combined with sensitive overlays in a derived dataset).

---

## 📦 5. Assets & Access Patterns

Each Item’s `assets` block exposes access to soils data for that subset.

### 5.1 Typical Assets

Examples (actual choices depend on pipeline implementation):

- `data-vector`:
  - `href` → Cloud-optimized vector (e.g., FlatGeobuf, GeoPackage, FileGDB subset).  
  - `type` → `"application/vnd.fgb"` / `"application/geopackage+sqlite"` / relevant MIME.  
  - `roles` → `["data"]`.

- `data-raster` (if derived gNATSGO-aligned tiles are attached to SSURGO Items):
  - `href` → tile or raster subset.  
  - `roles` → `["data"]`.

- `thumbnail`:
  - Small PNG/WEBP preview for UI.  
  - `roles` → `["thumbnail"]`.

- `metadata`:
  - Links to per-region soils docs, if any.  
  - `roles` → `["metadata"]`.

### 5.2 Checksums & Sizes

Where feasible:

- Include `checksum:sha256` on **data assets** to support:
  - Integrity verification.  
  - Graph & provenance consistency checks.

---

## 🔁 6. Relationship to Deltas & Provenance

Soils Items may link to:

- Corresponding geometry/tabular diffs:
  - If Items align with subset-level diff outputs, assets or `links` may point to relevant **rows** in `geometry-diff-YYYY-prev.parquet` / `tabular-diff-YYYY-prev.parquet`.

- PROV-O lineage:
  - Items may carry `links` with `rel: "provenance"` pointing to PROV-O entries in:
    - `../provenance/prov-ssurgo-2025.jsonld`.

The exact pattern should be consistent with:

- `docs/standards/catalogs/stac-dcat-derivation.md`  
- `docs/standards/catalogs/crosswalks/stac-dcat-crosswalk.md`

---

## 🧪 7. Validation & CI Expectations for Items

All Items in this directory MUST pass:

1. **STAC schema validation** (Items) via `stac-validator`.  
2. **KFM STAC profile checks**:
   - Required core fields.  
   - `kfm:*` fields where mandated.  
   - Geometry/bbox correctness.  
   - Temporal correctness (refresh date).  
3. **Crosswalk readiness**:
   - STAC → DCAT tests verify:
     - `dct:identifier`, `dct:spatial`, `dct:temporal` consistent with Collection and Items.  
     - No sensitive or internal-only assets/fields leak into derived DCAT.

Any new Item-added pattern (e.g., new tiling scheme) MUST:

- Update this README if materially different.  
- Be covered by CI tests (schema + profile validation).

---

## 🕰️ 8. Version History (Items Index)

| Version  | Date       | Author                                   | Summary                                                                 |
|----------|------------|------------------------------------------|-------------------------------------------------------------------------|
| v11.2.3  | 2025-12-03 | Geospatial Systems WG · FAIR+CARE Council | Initial SSURGO 2025 STAC Items README; defined naming, granularity options, asset patterns, and validation expectations. |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — MIT**  
FAIR+CARE Certified · MCP-DL v6.3 · KFM-MDP v11.2.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[⬅ Back to SSURGO 2025 STAC Collection](../README.md) · [⬅ Back to Soils STAC Overview](../README.md) · [📜 Governance Charter](../../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>

