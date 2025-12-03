---
title: "🛰️ KFM v11.2.3 — Flint Hills Eco-Cultural Region STAC Artifacts (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/datasets/cultural-landscapes/regions/flint-hills-region/stac/README.md"
version: "v11.2.3"
last_updated: "2025-12-02"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Biannual · Cultural Landscape Working Group · FAIR+CARE Council · Metadata Standards Subcommittee"
content_stability: "stable"
backward_compatibility: "Aligned with v11.2.3 cultural-landscape-region STAC-contract"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-version-hash>"
doc_integrity_checksum: "<sha256-of-this-file>"

sbom_ref: "../../../../../../../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../../../../../../../releases/v11.2.3/manifest.zip"
telemetry_ref: "../../../../../../../../releases/v11.2.3/focus-telemetry.json"
telemetry_schema: "../../../../../../../../schemas/telemetry/archaeology-cultural-landscape-regions-v1.json"

governance_ref: "../../../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"

status: "Active / Enforced"
doc_kind: "Region STAC Artifacts"
intent: "cultural-landscape-region-flint-hills-stac"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Compliant"
---

<div align="center">

# 🛰️ **KFM — Flint Hills Eco-Cultural Landscape Region · STAC Artifacts**  
`docs/analyses/archaeology/datasets/cultural-landscapes/regions/flint-hills-region/stac/README.md`

**Purpose:**  
Define and govern the **region-local STAC artifacts** for the **Flint Hills Eco-Cultural Landscape Region**.  
This directory provides the **Collection and Item JSON** representing this region in the KFM STAC ecosystem and:

- Links generalized eco-cultural geometries in `../data/` into STAC  
- Connects to region metadata and provenance records  
- Mirrors or references the **canonical region STAC** stored in the global registry  
- Supports ETL, Neo4j graph loading, Story Nodes, and Focus Mode v2/v3 overlays

Canonical region STAC registry (authoritative layer):

`docs/analyses/archaeology/datasets/cultural-landscapes/regions/stac/`

</div>

---

## 📘 Overview

This `stac/` directory is the **Flint Hills–specific STAC view**. It normally contains:

- A **STAC Collection** describing the Flint Hills Eco-Cultural Landscape Region  
- A **STAC Item** representing a specific region geometry version (e.g., v1 polygon/H3 set)  

Depending on deployment, these files may be:

- Exact copies of the canonical STAC JSON from the global registry, or  
- Thin wrappers that reference canonical IDs and URLs but live here for **region-centric navigation**  

In all cases:

- The **canonical contract** for region STAC is defined at:  
  `docs/analyses/archaeology/datasets/cultural-landscapes/regions/stac/README.md`
- Region-local STAC must be **byte-for-byte compatible** with canonical STAC, or act as **stable redirects/pointers** where tooling supports that pattern.

---

## 🗂️ Directory Layout

~~~text
docs/analyses/archaeology/datasets/cultural-landscapes/regions/flint-hills-region/stac/
├── 📄 README.md                              # This file (region STAC contract)
│
├── 🛰️ collection-flint-hills-region-v1.json  # STAC Collection for Flint Hills eco-cultural region (v1)
│
└── 🛰️ item-flint-hills-region-v1.json        # STAC Item for Flint Hills region v1 geometry (polygon/H3)
~~~

**Directory contract:**

- Exactly **one primary** Collection + Item pair per semantic version (here: `v1`).  
- File names must align with global STAC registry names (same IDs, same version).  
- If additional versions are added (e.g., v2):

  - They must be added here **and** to the global registry.  
  - Versioning must be reflected in IDs, filenames, metadata, and provenance.

---

## 🛰 STAC Collection: `collection-flint-hills-region-v1.json`

This Collection describes the **Flint Hills Eco-Cultural Landscape Region** as a whole.

### Required Core Fields

Selected fields and expectations:

- `stac_version` — must match KFM’s supported STAC version.  
- `type = "Collection"`  
- `id` — e.g., `"kfm-arch-lands-flint-hills-region-v1"`  
- `description` — clear description of the region’s role (tallgrass prairie + chert-bearing uplands, eco-cultural zone).  
- `license` — `"CC-BY-4.0"` (unless stricter governance is explicitly approved).  
- `extent`:
  - `spatial` — generalized bbox (no site-level precision).  
  - `temporal` — temporal coverage for the region’s analytic use (aligned with OWL-Time and archaeology ontology).

### KFM-Specific Properties

The Collection must expose the following fields (either in `properties` or an agreed extension block):

- `kfm:region_slug = "flint-hills-region"`  
- `kfm:region_kind = "eco-cultural"` (and optionally other tags such as `"upland-escarpment"` if modeled)  
- `kfm:culture_phase` — array of cultural phases (e.g., `["Woodland", "Late Prehistoric", "Protohistoric"]`)  
- `kfm:temporal_coverage` — structured representation of time intervals/phases  
- `kfm:metadata_ref` — path/URI to the per-region metadata JSON-LD:  
  - `../metadata/dcat-flint-hills-region-v1.jsonld`  
- `kfm:provenance_ref` — pointer(s) to canonical PROV-O logs:  
  - e.g., `../../provenance/flint-hills-region-v1.json`  

### CARE & Sovereignty Fields

The Collection must include:

- `care:sensitivity` — `"generalized"` or `"restricted-generalized"` (public artifacts only).  
- `care:review` — `"faircare"`, `"tribal"`, or a combined pattern (e.g., `"faircare+tribal"`).  
- `care:notes` — summary of generalization strategy, eco-cultural logic, and review context.  
- `care:visibility_rules` — `"polygon-generalized"`, `"h3-only"`, `"no-exact-boundaries"` or governed combinations.

These values must **match**:

- Region metadata (`../metadata/`).  
- Canonical provenance logs (`../../provenance/`).  
- Region provenance registry (`../../provenance/../../regions/provenance/registry/`).

---

## 🛰 STAC Item: `item-flint-hills-region-v1.json`

This Item describes a **specific region geometry realization** (e.g., primary polygon set for v1).

### Required Core Fields

Selected required fields:

- `stac_version`  
- `type = "Feature"`  
- `id` — e.g., `"kfm-arch-lands-flint-hills-region-v1"`  
- `geometry` — generalized Polygon/MultiPolygon geometry (EPSG:4326, site-safe).  
- `bbox` — matching geometry extent at generalized precision.  
- `properties.datetime` or `properties.interval` — set consistently with Collection temporal extent (or omitted if not applicable per profile).

### KFM-Specific Properties

Within `properties`:

- `kfm:region_slug = "flint-hills-region"`  
- `kfm:region_kind = "eco-cultural"`  
- `kfm:culture_phase` — same or subset of Collection phases.  
- `kfm:temporal_coverage` — region coverage as used for this geometry.  
- `kfm:stac_collection_id` — ID of the Collection above.  
- `kfm:source_ref` — optional references to upstream datasets (eco-regions, geology, hydrology, etc.).  
- `kfm:provenance_ref` — pointer to canonical PROV-O logs (same as Collection or a more specific subset).

### CARE Fields

The Item must mirror the Collection’s CARE values:

- `care:sensitivity`  
- `care:review`  
- `care:visibility_rules`  
- `care:notes`

Any deviation from Collection-level CARE fields must be explicitly justified and governed (e.g., if a particular representation is more restrictive).

### Assets

Typical assets:

- `assets.data`:
  - `href` → region polygon file (e.g., `../data/geojson/flint-hills-region.v1.geojson`)  
  - `type` → `"application/geo+json"`  
  - `roles` → `["data"]`  

- Optional `assets.h3`:
  - `href` → H3 mosaic (e.g., `../data/h3/flint-hills-region-h3-r6.v1.geojson`)  
  - `type` → `"application/geo+json"`  
  - `roles` → `["data"]`  
  - Always aligned with `"h3-only"` visibility rules where applicable.

Assets must **never** expose raw or over-precise geometries.

---

## ⚖ FAIR+CARE & Sovereignty Constraints

STAC JSON in this directory must:

- Accurately reflect CARE and sovereignty decisions recorded in provenance and metadata.  
- Respect generalization requirements:
  - Polygons and H3 mosaics must not encode site-level or sensitive precision.  
- Follow the visibility contract:

  - If `"h3-only"` is configured for certain contexts, UIs must honor that using the STAC assets.  

Changes to:

- Spatial extent  
- Temporal coverage  
- CARE fields

are **governance events** and must be reviewed and approved through FAIR+CARE and sovereignty processes.

---

## 🧬 Relationship to Other Flint Hills Artifacts

This region-local STAC directory is tightly coupled to:

- **Region README & Data Layout**  
  - `../README.md`  
  - `../data/README.md`  

- **Region Metadata**  
  - `../metadata/README.md`  
  - `../metadata/dcat-flint-hills-region-v1.jsonld`  

- **Region Provenance Refs**  
  - `../provenance/README.md`  
  - `../provenance/flint-hills-region-v1.prov-ref.json`  

- **Global STAC Registry**  
  - `../../stac/README.md`  
  - `../../stac/collections/collection-flint-hills-region-v1.json`  
  - `../../stac/items/item-flint-hills-region-v1.json`  

**Contract:**

- IDs, CARE fields, temporal coverage, and paths must match between:

  - This directory’s STAC JSON  
  - Global STAC registry JSON  
  - Region metadata & provenance  

If they diverge, the canonical source is the global STAC registry + provenance + metadata; this directory must be corrected.

---

## 🧪 Validation & CI/CD

STAC artifacts in this directory are **CI-enforced**.

### Validation Expectations

- **STAC schema validation**
  - Collection: STAC Collection schema + KFM archaeology STAC profile.  
  - Item: STAC Item schema + KFM archaeology STAC profile.  

- **Cross-link checks**
  - `kfm:region_slug` matches `flint-hills-region`.  
  - `kfm:metadata_ref` and `kfm:provenance_ref` resolve to existing artifacts.  
  - Asset `href` paths point to existing files in `../data/`.

- **CARE & sovereignty consistency**
  - CARE fields match region metadata and provenance.  
  - Sensitivity and visibility rules are not weakened relative to canonical logs.

Indicative CI workflows:

- `artifact-stac-validate.yml`  
- `metadata-validate.yml`  
- `faircare-audit.yml`  
- `archaeology-provenance-validate.yml`  
- `region-metadata-registry-validate.yml`  
- `region-provenance-registry-validate.yml`  

CI must **block**:

- Any STAC changes that break schema or cross-link contracts.  
- CARE / sovereignty regressions.  
- IDs or fields diverging from the global STAC registry.

---

## 🧭 Authoring & Maintenance Workflow

When updating the Flint Hills region and its STAC:

1. **Update Geometry & Provenance**  
   - Adjust `../data/` and canonical provenance logs under `../../../../provenance/` as needed.  

2. **Update Region Metadata**  
   - Ensure `../metadata/dcat-flint-hills-region-v*.jsonld` remains consistent.

3. **Update Global STAC Registry**  
   - Modify STAC Collection/Item under `../../stac/collections/` and `../../stac/items/`.

4. **Sync Region-Local STAC**  
   - Copy or regenerate `collection-flint-hills-region-v*.json` and `item-flint-hills-region-v*.json` here so they match the canonical registry.

5. **Run Local Validation**  
   - Use repo tooling (e.g., `make validate-region-flint-hills-stac`) to run STAC + linkage + CARE checks.

6. **Submit PR & Address Feedback**  
   - CI and governance review ensure that all Flint Hills STAC artifacts are consistent, safe, and governed.

---

## 🕰️ Version History

| Version  | Date       | Author                                      | Summary                                                                 |
|----------|------------|---------------------------------------------|-------------------------------------------------------------------------|
| v11.2.3  | 2025-12-02 | Cultural Landscape WG · FAIR+CARE Council   | Established governed STAC layout for Flint Hills Eco-Cultural Region; aligned Collection/Item contracts with global region STAC registry, metadata, provenance, and KFM-MDP v11.2.2. |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — CC-BY 4.0**  
FAIR+CARE Certified · MCP-DL v6.3 · KFM-MDP v11.2.2 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[⬅ Back to Flint Hills Eco-Cultural Region](../README.md) · [⬅ Back to Flint Hills Region Metadata](../metadata/README.md) · [⬅ Back to Global Region STAC Registry](../../stac/README.md)

</div>