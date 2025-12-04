---
title: "🌐 KFM v11.2.3 — SSURGO 2025 STAC Collection (Kansas AOI) (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
description: "STAC Collection overview for the 2025 NRCS SSURGO soils dataset (Kansas AOI) in the Kansas Frontier Matrix annual soils refresh pipeline."
path: "docs/data/soils/annual-refresh/stac/ssurgo-2025/README.md"
version: "v11.2.3"
last_updated: "2025-12-03"

release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Annual · Geospatial Systems · FAIR+CARE Oversight"
content_stability: "stable"
status: "Active / Enforced"
backward_compatibility: "v10.x → v11.x soils-ssurgo-stac-collection-contract compatible"

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
intent: "nrcs-soils-ssurgo-2025-stac"

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

json_schema_ref: "../../../../../../schemas/json/data-soils-annual-refresh-ssurgo-2025-stac-readme-v1.json"
shape_schema_ref: "../../../../../../schemas/shacl/data-soils-annual-refresh-ssurgo-2025-stac-readme-v1.shape.ttl"

immutability_status: "version-pinned"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"

ttl_policy: "Permanent"
sunset_policy: "Never (per-year soils collections form the long-term soils baseline)"
---

<div align="center">

# 🌐 SSURGO 2025 — STAC Collection (Kansas AOI)  
`docs/data/soils/annual-refresh/stac/ssurgo-2025/README.md`

**Purpose:**  
Describe the **2025 SSURGO STAC Collection** for the Kansas Frontier Matrix annual soils refresh, including:

- How `collection.json` is structured and governed  
- How Items (if used) are organized and linked  
- How this Collection fits into the **STAC-first → DCAT-derived** KFM catalog model  

</div>

---

## 📘 1. Scope

This directory corresponds to the **KFM STAC representation** of the **2025 NRCS SSURGO soils dataset** over the KFM area of interest (typically Kansas and relevant buffer regions).

Contents:

- `collection.json` — the **authoritative STAC Collection** for SSURGO 2025 in KFM.  
- `items/` — optional per-region/per-tileset Items, if the pipeline chooses to expose finer-grain STAC entries.

This Collection is:

- Derived from **raw NRCS SSURGO 2025 bundles** stored under `../raw/`.  
- Governed by the **Annual Soils Refresh pipeline** (`../README.md` and `../processing/README.md`).  
- Conforming to the **KFM STAC profile** and extensions documented under `docs/standards/catalogs/stac/`.

---

## 🗂️ 2. Directory Layout (SSURGO 2025 STAC)

~~~text
docs/data/soils/annual-refresh/stac/ssurgo-2025/
│
├── 📄 README.md               # This file — SSURGO 2025 STAC overview
│
├── 📄 collection.json         # STAC Collection for SSURGO 2025 (KFM STAC profile-compliant)
│
└── 📂 items/                  # (Optional) per-region or per-tileset Items
    ├── 📄 ssurgo-2025-ks.json         # Example: Kansas-wide Item (if used)
    ├── 📄 ssurgo-2025-huc8-....json   # Example: HUC8-level Items (if used)
    └── …                              # Additional items as pipeline design requires
~~~

**Directory contract:**

- `collection.json` MUST exist and be **STAC 1.0.x** compliant.  
- The existence and granularity of `items/` is a **pipeline design choice**, but:
  - If `items/` is present, Item IDs and coverage must follow KFM STAC best practices.  
  - All Items MUST belong to this Collection (`"collection": "ssurgo-2025-..."`).

---

## 🧱 3. STAC Collection Profile (SSURGO 2025)

The `collection.json` file for SSURGO 2025 MUST satisfy:

### 3.1 Core STAC Fields

- `stac_version = "1.0.0"` (or compatible `1.0.x`).  
- `type = "Collection"`.  
- `id` — recommended: `ssurgo-2025-ks` (or similar AOI-specific ID).  
- `description` — high-level description, e.g.:

  > “NRCS SSURGO 2025 soils survey data for Kansas as processed by KFM annual soils refresh (geometry + tabular).”

- `extent.spatial` — bounding boxes encompassing the SSURGO coverage for the AOI.  
- `extent.temporal` — temporal extent of this release, typically:

  - Start date: the **effective release or reference date**, e.g. `"2025-10-01T00:00:00Z"`.  
  - End date: `null` (open-ended) or same date, depending on KFM temporal modeling.

- `license` — NRCS/public-domain terms as interpreted by KFM.  
- `providers` — array including:
  - NRCS (role: `producer`, `licensor`).  
  - KFM (role: `processor`, `host`).

### 3.2 KFM Core Extension (`kfm:*`)

Per `stac-ext-kfm-core.md`, the Collection SHOULD include:

- `kfm:dataset_id = "urn:kfm:dataset:ssurgo-ks-2025"` (or equivalent).  
- `kfm:domain = "soils"` (or `"geoscience"`, as standardized).  
- `kfm:release_stage = "stable"`.  
- Optional:
  - `kfm:region_slug = "kansas-statewide"` or similar.  
  - `kfm:review_cycle = "Annual · Geospatial Systems · FAIR+CARE Oversight"`.

### 3.3 FAIR+CARE Extension (`kfmfc:*`, Optional)

Soils are generally low-sensitivity, but FAIR+CARE metadata can still apply:

- `kfmfc:sensitivity = "general"`  
- `kfmfc:care_label = "Public"`  
- `kfmfc:sovereignty_flag = false` (unless a specific soils-derived product intersects sovereignty concerns)  

If any soils derivatives are used in culturally sensitive contexts, that should be governed at the **derived-product level**; SSURGO raw representation remains general-purpose.

---

## 🌐 4. STAC Items (If Used) — Recommended Patterns

Depending on performance and access patterns, KFM may define Items under `items/` using one of the following:

### 4.1 Single AOI Item

A single Item representing the **entire Kansas AOI**:

- `id = "ssurgo-2025-ks"`  
- `geometry` / `bbox` = Kansas AOI coverage.  
- One or more `assets` pointing to:

  - Vector datasets (e.g., FileGDB/GeoPackage/FlatGeobuf).  
  - Derived soils tilesets or partitions.

### 4.2 Region-Based Items (HUC/County/Planning Region)

Items per HUC8 / county / planning area:

- `id = "ssurgo-2025-huc8-11030001"` (example).  
- `geometry` derived from region boundaries.  
- `assets` pointing to **subsets** of SSURGO data relevant to that region.

### 4.3 Item-Level Extensions & Properties

Items may use:

- `kfm-core` fields for region-specific dataset IDs or tags (if needed).  
- Domain-agnostic or domain-specific properties to tag:
  - Variable naming for derived soils metrics.  
  - Links to diff artifacts where relevant.

All Items MUST:

- Include `"collection": "<ssurgo-2025-collection-id>"`.  
- Set `links` with `rel: "collection"` and `rel: "root"` appropriately.

---

## 🔁 5. Cross-Year Versioning & Links

The SSURGO 2025 Collection should capture its relationship to earlier years:

- In STAC (via `links[]`) and/or DCAT derivatives:

  - Link to **SSURGO 2024** Collection with:

    ~~~text
    { "rel": "predecessor", "href": "../ssurgo-2024/collection.json" }
    ~~~

  - Optionally reciprocal links in `ssurgo-2024/collection.json` (`rel: "successor"`).

- In PROV-O (`../provenance/prov-ssurgo-2025.jsonld`):

  - The 2025 Collection is a `prov:Entity` derived from:
    - NRCS raw bundles (`raw/ssurgo-2025.zip`).  
    - 2024 baseline.  
    - Diff and validation activities.

All versioning semantics MUST remain consistent with:

- `docs/standards/catalogs/stac-dcat-derivation.md`.  
- `docs/standards/catalogs/crosswalks/stac-dcat-crosswalk.md`.

---

## 🧪 6. Validation & CI for SSURGO 2025 STAC

`collection.json` and any Items under this directory MUST pass:

1. **STAC schema validation**  
   - `stac-validator` with:
     - Collection schema.  
     - Item schema (if Items present).

2. **KFM STAC profile checks**  
   - Enforcement of:
     - `kfm:*` fields.  
     - Geometry/bbox and temporal semantics.  
     - Provider and license rules.

3. **Crosswalk validation**  
   - STAC → DCAT tests ensure:
     - `dct:identifier`, `dct:spatial`, `dct:temporal` match STAC.  
     - No internal-only assets are included in public DCAT exports.

Failures in any of these steps MUST block:

- Soils STAC publication for 2025.  
- Downstream DCAT exports and portal updates.

---

## 🕰️ 7. Version History (SSURGO 2025 STAC Overview)

| Version  | Date       | Author                                   | Summary                                                                 |
|----------|------------|------------------------------------------|-------------------------------------------------------------------------|
| v11.2.3  | 2025-12-03 | Geospatial Systems WG · FAIR+CARE Council | Initial STAC Collection README for SSURGO 2025; documented Collection expectations, Item patterns, and validation requirements under KFM STAC profile. |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — MIT**  
FAIR+CARE Certified · MCP-DL v6.3 · KFM-MDP v11.2.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[⬅ Back to Soils STAC Overview](../README.md) · [⬅ Back to Annual Soils Refresh](../README.md) · [📜 Governance Charter](../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>

