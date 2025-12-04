---
title: "🗺️ KFM v11.2.3 — Annual NRCS Soils STAC Catalogs (SSURGO · gNATSGO) (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
description: "STAC catalog structure and publication rules for annual NRCS SSURGO/gNATSGO soils refreshes in the Kansas Frontier Matrix."
path: "docs/data/soils/annual-refresh/stac/README.md"
version: "v11.2.3"
last_updated: "2025-12-03"

release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Annual · Geospatial Systems · FAIR+CARE Oversight"
content_stability: "stable"
status: "Active / Enforced"
backward_compatibility: "v10.x → v11.x soils-refresh-stac-contract compatible"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.2.3/manifest.zip"
telemetry_ref: "../../../../../releases/v11.2.3/soils-refresh-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/soils-refresh-v1.json"

governance_ref: "../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.3"

doc_kind: "STAC Catalog Overview"
intent: "nrcs-soils-annual-refresh-stac"

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

json_schema_ref: "../../../../../schemas/json/data-soils-annual-refresh-stac-readme-v1.json"
shape_schema_ref: "../../../../../schemas/shacl/data-soils-annual-refresh-stac-readme-v1.shape.ttl"

immutability_status: "version-pinned"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"

ttl_policy: "24 Months"
sunset_policy: "Superseded on next major soils STAC catalog revision"
---

<div align="center">

# 🗺️ Annual NRCS Soils STAC Catalogs (SSURGO · gNATSGO)  
`docs/data/soils/annual-refresh/stac/README.md`

**Purpose:**  
Describe the **STAC catalog layer** for the KFM **Annual NRCS Soils Refresh** (SSURGO & gNATSGO), including:

- Directory layout for per-year STAC Collections & Items  
- Alignment with the **KFM STAC profile** and STAC-first → DCAT-derived model  
- Provenance and cross-year versioning semantics  

</div>

---

## 📘 1. Scope

This directory contains the **authoritative KFM STAC representation** of annual NRCS soils releases:

- **SSURGO** — detailed, polygon-based soils survey.  
- **gNATSGO** — gridded soils dataset built from SSURGO/STATSGO and other sources.

STAC here is:

- The **primary discovery and spatial metadata layer** for soils in KFM.  
- The **source** from which DCAT and portal metadata are derived.  
- Versioned **per year** and **per product** (SSURGO / gNATSGO).

This README is the STAC-specific companion to:

- `../README.md` — Annual Soils Refresh pipeline overview.  
- `../processing/README.md` — Processing & diff engine.  
- `../provenance/` — PROV-O lineage & citations.  

STAC conformance is governed by:

- `docs/standards/catalogs/stac/stac-kfm-profile.md`  
- `docs/standards/catalogs/stac/stac-best-practices.md`  
- STAC extensions and crosswalks under `docs/standards/catalogs/`.

---

## 🗂️ 2. Directory Layout (STAC Catalogs)

~~~text
docs/data/soils/annual-refresh/stac/
│
├── 📄 README.md                           # This file — STAC overview for soils refresh
│
├── 🌐 ssurgo-2025/                        # STAC Collection + Items for SSURGO 2025
│   ├── 📄 collection.json                 # STAC Collection (KFM STAC profile-compliant)
│   └── 📂 items/                          # Optional per-tile/per-region Items (if used)
│
├── 🌐 ssurgo-2024/                        # STAC Collection + Items for SSURGO 2024
│   └── …                                  # Same pattern as ssurgo-2025/
│
├── 🌐 gnatsgo-2025/                       # STAC Collection + Items for gNATSGO 2025
│   ├── 📄 collection.json
│   └── 📂 items/
│
└── 🌐 gnatsgo-2024/                       # STAC Collection + Items for gNATSGO 2024
    └── …                                  # Same pattern as gnatsgo-2025/
~~~

**Directory contract:**

- Each `*-YYYY/` directory MUST contain at least one **STAC Collection** (`collection.json`).  
- Items may be:
  - Aggregated (e.g., **Kansas-only** or **sub-region** Items), or  
  - Fine-grained (per-tileset, per-county, etc.) as defined by KFM soils modeling needs.  
- STAC MUST conform to the **KFM STAC profile** and soils-specific practices.

---

## 🧱 3. STAC Collections — Profile & Required Fields

Each soils STAC Collection (e.g., `ssurgo-2025/collection.json`, `gnatsgo-2025/collection.json`) MUST satisfy:

- STAC version: `stac_version = "1.0.0"` (or compatible 1.0.x).  
- Core Collection fields:
  - `id` — e.g., `ssurgo-2025-ks`, `gnatsgo-2025-ks`.  
  - `description` — summary of the NRCS soils product for that year & AOI.  
  - `extent.spatial` — bounding box over Kansas (or KFM AOI).  
  - `extent.temporal` — temporal coverage (e.g., `[2025-10-01T00:00:00Z, null]`).  
  - `license` — NRCS / public-domain terms as interpreted by KFM.  
  - `providers` — NRCS + KFM (producer/processor/host roles).

### 3.1 KFM Core & FAIR+CARE Extensions

Collections should use KFM STAC extensions:

- `kfm-core` (`kfm:*`):
  - `kfm:dataset_id` — stable KFM soils dataset ID, e.g., `urn:kfm:dataset:ssurgo-ks-2025`.  
  - `kfm:domain = "soils"` (or `"geoscience"` as defined).  
  - `kfm:release_stage = "stable"`.  

- `kfm-faircare` (`kfmfc:*`), if applicable:
  - Soils are generally public + low-sensitivity, but FAIR+CARE fields can still be used to track governance context.

Extensions MUST conform to:

- `docs/standards/catalogs/stac/extensions/stac-ext-kfm-core.md`  
- `docs/standards/catalogs/stac/extensions/stac-ext-faircare.md`

---

## 🌐 4. STAC Items — Patterns & Granularity

KFM soils STAC items may follow one of these patterns (to be chosen per pipeline design):

### 4.1 Region/Tileset Items

Items represent **logical subsets** of the soils dataset:

- Per county / HUC / planning region.  
- Per vector tile or grids used in map services.

Item fields (profile-summary):

- `id` — stable ID per region/tileset (e.g., `ssurgo-2025-huc8-11030001`).  
- `geometry` / `bbox` — coverage of that region/tileset.  
- `properties.datetime` — soils refresh date (e.g., `2025-10-01T00:00:00Z`).  
- `assets`:
  - Data asset(s) for soils tables/rasters specific to that region.  
  - Optional overviews or derivatives.

### 4.2 Single-Collection / No-Item Model

For some cases, KFM may choose:

- A single **Collection-level representation** (with no or minimal Items) if:
  - Soils are mainly used as a monolithic dataset in downstream pipelines.  
  - All fine-grained tiling is handled at the storage/service level, not in STAC.

In this case:

- `collection.json` is the primary spatial metadata object.  
- Service/tiling details can be captured via:
  - `assets` on the Collection.  
  - `DataService` records in DCAT (derived).

---

## 🔁 5. Cross-Year Versioning & Relationships

Cross-year relationships MUST be encoded to allow:

- Users and systems to understand how 2025 relates to 2024.

Recommended patterns (either in STAC via `links` or in derived DCAT):

- `rel: "predecessor"` / `"successor"` or KFM equivalents:
  - 2025 Collections may reference 2024 Collections using:
    - `dct:isVersionOf` (in derived DCAT).  
    - STAC `links` to 2024.  

- Use PROV-O for deeper lineage (in `../provenance/`), and ensure:
  - STAC `links` point to the corresponding PROV-O documents.

All versioning must be consistent with:

- `docs/standards/catalogs/stac-dcat-derivation.md`  
- `docs/standards/catalogs/crosswalks/stac-dcat-crosswalk.md`

---

## 📊 6. Relationship to Deltas & Provenance

STAC catalogs are connected to:

- **Deltas** (`../deltas/`):
  - STAC Items or Collections may have:
    - Assets or links pointing to per-year diffs (e.g., geometry/tabular diff Parquet files).  

- **Provenance** (`../provenance/`):
  - STAC Collections should include links to PROV-O documents:
    - `prov-ssurgo-YYYY.jsonld`  
    - `prov-gnatsgo-YYYY.jsonld`

Recommended STAC `links` (conceptual):

- `"rel": "derived_from"` pointing to:
  - NRCS upstream metadata in `raw/metadata/`.  
  - KFM baseline from previous year.  

- `"rel": "provenance"` or KFM-specific link to PROV-O documents.

---

## 🧪 7. Validation & CI Expectations

All STAC content under this directory MUST pass:

1. **STAC Schema Validation**  
   - `stac-validator` with:
     - Core STAC Collection/Item schemas.  
     - KFM extensions (core, FAIR+CARE, domain-specific if any).

2. **Profile & Best-Practice Checks**  
   - KFM-specific linters to ensure:
     - `kfm:*` fields present and valid.  
     - Geometry/bbox semantics respected.  
     - Temporal fields consistent with refresh schedule.

3. **Crosswalk Readiness**  
   - STAC → DCAT crosswalk tests must confirm:
     - DCAT `dct:identifier`, `dct:spatial`, `dct:temporal` match STAC.  
     - No internal-only assets are exposed in public DCAT.

CI workflows (indicative):

- `catalog-stac-validate.yml`  
- `catalog-stac-lint.yml`  
- `catalog-crosswalk-validate.yml` (for soils-related datasets)

Builds MUST fail when:

- STAC records violate the KFM STAC profile.  
- Crosswalk invariants (STAC → DCAT) are broken.  
- Governance/telemetry rules for soils-refresh are not met.

---

## 🕰️ 8. Version History (Soils STAC Overview)

| Version  | Date       | Author                                   | Summary                                                                 |
|----------|------------|------------------------------------------|-------------------------------------------------------------------------|
| v11.2.3  | 2025-12-03 | Geospatial Systems WG · FAIR+CARE Council | Initial soils STAC README; defined directory structure, profile alignment, cross-year versioning, and CI expectations for SSURGO/gNATSGO Collections & Items. |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — MIT**  
FAIR+CARE Certified · MCP-DL v6.3 · KFM-MDP v11.2.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[⬅ Back to Annual Soils Refresh](../README.md) · [⬅ Back to Soils Data Index](../README.md) · [📜 Governance Charter](../../../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>

