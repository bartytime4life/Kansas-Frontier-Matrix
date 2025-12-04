---
title: "🌐 KFM v11.2.3 — SSURGO 2024 STAC Collection (Kansas AOI) (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
description: "STAC Collection overview for the 2024 NRCS SSURGO soils dataset (Kansas AOI) in the Kansas Frontier Matrix annual soils refresh pipeline."
path: "docs/data/soils/annual-refresh/stac/ssurgo-2024/README.md"
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
intent: "nrcs-soils-ssurgo-2024-stac"

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

json_schema_ref: "../../../../../../schemas/json/data-soils-annual-refresh-ssurgo-2024-stac-readme-v1.json"
shape_schema_ref: "../../../../../../schemas/shacl/data-soils-annual-refresh-ssurgo-2024-stac-readme-v1.shape.ttl"

immutability_status: "version-pinned"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"

ttl_policy: "Permanent"
sunset_policy: "Never (per-year soils collections form the long-term soils baseline)"
---

<div align="center">

# 🌐 SSURGO 2024 — STAC Collection (Kansas AOI)  
`docs/data/soils/annual-refresh/stac/ssurgo-2024/README.md`

**Purpose:**  
Describe the **2024 SSURGO STAC Collection** for the Kansas Frontier Matrix annual soils refresh, including:

- How `collection.json` is structured and governed  
- How Items (if used) are organized and linked  
- How this Collection participates in cross-year soils versioning and the **STAC-first → DCAT-derived** KFM catalog model  

</div>

---

## 📘 1. Scope

This directory corresponds to the **KFM STAC representation** of the **2024 NRCS SSURGO soils dataset** over the KFM area of interest (typically Kansas and any governance-defined buffers).

Contents:

- `collection.json` — the **authoritative STAC Collection** for SSURGO 2024 in KFM.  
- `items/` — optional per-region/per-tileset Items if the pipeline exposes finer-grain STAC entries.

This Collection is:

- Derived from **raw NRCS SSURGO 2024 bundles** stored under `../../../../raw/`.  
- Governed by the **Annual Soils Refresh pipeline** (`../../README.md` and `../../processing/README.md`).  
- Conforming to the **KFM STAC profile** and extensions under `docs/standards/catalogs/stac/`.

It serves as the **baseline** for the 2025 diff and thus is a critical part of the soils time series.

---

## 🗂️ 2. Directory Layout (SSURGO 2024 STAC)

~~~text
docs/data/soils/annual-refresh/stac/ssurgo-2024/
│
├── 📄 README.md               # This file — SSURGO 2024 STAC overview
│
├── 📄 collection.json         # STAC Collection for SSURGO 2024 (KFM STAC profile-compliant)
│
└── 📂 items/                  # (Optional) per-region or per-tileset Items
    ├── 📄 ssurgo-2024-ks.json            # Example: Kansas-wide Item (if used)
    ├── 📄 ssurgo-2024-huc8-....json      # Example: HUC8-level Items (if used)
    └── …                                 # Additional items as pipeline design requires
~~~

**Directory contract:**

- `collection.json` MUST exist and be **STAC 1.0.x** compliant.  
- If `items/` is present:
  - All Items MUST set `"collection"` to the SSURGO 2024 Collection ID.  
  - Items MUST include appropriate `links` to the Collection and STAC root.  

---

## 🧱 3. STAC Collection Profile (SSURGO 2024)

The `collection.json` file for SSURGO 2024 MUST satisfy:

### 3.1 Core STAC Fields

- `stac_version = "1.0.0"` (or compatible 1.0.x).  
- `type = "Collection"`.  
- `id` — recommended: `ssurgo-2024-ks` (or similar AOI-specific ID).  
- `description` — e.g.:

  > “NRCS SSURGO 2024 soils survey data for Kansas as processed by KFM annual soils refresh (geometry + tabular).”

- `extent.spatial` — bounding boxes for the SSURGO coverage over KFM AOI.  
- `extent.temporal` — temporal extent of this release (e.g., reference date in 2024).  
- `license` — NRCS/public-domain terms as interpreted by KFM.  
- `providers` — including:
  - NRCS (producer/licensor).  
  - KFM (processor/host).

### 3.2 KFM Core Extension (`kfm:*`)

Per `stac-ext-kfm-core.md`, the Collection SHOULD include:

- `kfm:dataset_id = "urn:kfm:dataset:ssurgo-ks-2024"` (or equivalent).  
- `kfm:domain = "soils"` (or `"geoscience"`).  
- `kfm:release_stage = "stable"`.  
- Optional:
  - `kfm:region_slug = "kansas-statewide"`.  
  - `kfm:review_cycle = "Annual · Geospatial Systems · FAIR+CARE Oversight"`.

### 3.3 FAIR+CARE Extension (`kfmfc:*`, Optional)

Typical soils profile:

- `kfmfc:sensitivity = "general"`  
- `kfmfc:care_label = "Public"`  
- `kfmfc:sovereignty_flag = false`  

If a particular derivative or combined product implements additional governance rules, that should be modeled in **derived collections/items**, not by altering the core SSURGO 2024 raw representation.

---

## 🌐 4. STAC Items (If Used) — Partitioning Strategy

Items under `items/` may be partitioned for performance and usability. Common options:

### 4.1 Kansas-Wide Item

- `id = "ssurgo-2024-ks"`  
- Coverage: entire Kansas AOI.  
- Assets: one or more vector datasets representing all SSURGO soils for Kansas.

### 4.2 HUC8-Based Items (Hydrology Alignment)

- `id = "ssurgo-2024-huc8-<HUC8>"`, e.g., `ssurgo-2024-huc8-11030001`.  
- Geometry: HUC8 watershed boundaries intersected with SSURGO coverage.  
- Use case: hydrology-aligned soils subsets.

### 4.3 County/Region Items

- `id = "ssurgo-2024-county-<FIPS>"` or `ssurgo-2024-region-<slug>`.  
- Use case: county planning, regional overlays.

All Items MUST:

- Include `geometry`, `bbox`, `properties.datetime`, `collection`, and `links` per KFM STAC profile.  
- Use stable, ASCII-safe, hyphenated IDs (`lowercase` recommended).

---

## 📦 5. Assets & Access Patterns in SSURGO 2024 Items

Typical asset patterns:

- `data-vector`:
  - Primary soils data for the subset (vector).  
  - `type`: suitable MIME type for vector format.  
  - `roles`: `["data"]`.

- `thumbnail`:
  - Quick preview rendered from soils polygons.  
  - `roles`: `["thumbnail"]`.

- `metadata`:
  - Additional soils docs (if per-region docs exist).  
  - `roles`: `["metadata"]`.

**Checksums:**

- Where feasible, each `data-vector` asset SHOULD include `checksum:sha256` to support:
  - Integrity checks.  
  - Consistency across year comparisons.

---

## 🔁 6. Relationship to 2025 & Cross-Year Lineage

As the **baseline** for the 2025 refresh:

- The SSURGO 2024 Collection is:

  - The “previous year” for `deltas/geometry-diff-2024-2025.parquet` and `tabular-diff-2024-2025.parquet`.  
  - Referenced in:
    - `processing/diff-report-2025.md`.  
    - `processing/lineage-events.json`.  
    - `provenance/prov-ssurgo-2025.jsonld`.

Recommended linkage:

- 2025 Collection (`ssurgo-2025/collection.json`) may include a `links` entry referencing 2024:

  ~~~json
  {
    "rel": "predecessor",
    "href": "../ssurgo-2024/collection.json"
  }
  ~~~

- SSURGO 2024 may reciprocally link to SSURGO 2025 as `successor`.

These relationships support:

- Catalog navigation.  
- Time-series modeling with soils layers.  
- Provenance-based queries.

---

## 🧪 7. Validation & CI Expectations for SSURGO 2024

The SSURGO 2024 STAC Collection and Items MUST pass:

1. **STAC validator**  
   - Collection and Item schemas.  

2. **KFM STAC Profile checks**  
   - Proper use of `kfm:*` fields.  
   - Temporal & spatial semantics consistent with 2024 NRCS release.  

3. **Crosswalk readiness**  
   - STAC → DCAT tests verifying:
     - `dct:identifier`, `dct:spatial`, `dct:temporal` consistency.  
     - No internal-only assets included in public DCAT.

CI MUST block publication if:

- STAC fails schema/profile validation.  
- Crosswalk invariants fail.  
- Governance/telemetry rules for soils are not met.

---

## 🕰️ 8. Version History (SSURGO 2024 STAC Overview)

| Version  | Date       | Author                                   | Summary                                                                 |
|----------|------------|------------------------------------------|-------------------------------------------------------------------------|
| v11.2.3  | 2025-12-03 | Geospatial Systems WG · FAIR+CARE Council | Initial SSURGO 2024 STAC Collection README; documented structure, cross-year role, and validation expectations under KFM STAC profile. |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — MIT**  
FAIR+CARE Certified · MCP-DL v6.3 · KFM-MDP v11.2.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[⬅ Back to Soils STAC Overview](../README.md) · [⬅ Back to Annual Soils Refresh](../README.md) · [📜 Governance Charter](../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>

