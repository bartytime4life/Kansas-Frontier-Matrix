---
title: "🧾 KFM v11.2.3 — Cultural Landscape Region Metadata Index Registry (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/datasets/cultural-landscapes/regions/metadata/registry/README.md"
version: "v11.2.3"
last_updated: "2025-12-02"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Biannual · Cultural Landscape Working Group · FAIR+CARE Council · Metadata Standards Subcommittee"
content_stability: "stable"
backward_compatibility: "v10.4.0 → v11.2.3 region-metadata-registry-index compatible"

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
doc_kind: "Region Metadata Registry Index"
intent: "cultural-landscape-region-metadata-index-registry"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Compliant"
---

<div align="center">

# 🧾 **KFM — Cultural Landscape Region Metadata Index Registry**  
`docs/analyses/archaeology/datasets/cultural-landscapes/regions/metadata/registry/README.md`

**Purpose:**  
Define and govern the **machine-readable index files** that register all **cultural landscape region metadata records** in the Kansas Frontier Matrix (KFM).  
This directory provides:

- A **canonical index** of region metadata records (per region, per version)  
- Optional **coverage summaries** for analysis and UI filtering  
- CI-enforced contracts tying **region metadata JSON-LD** to **STAC**, **provenance**, and **CARE/sovereignty** governance  

Authoritative region metadata records live one level up in:

`docs/analyses/archaeology/datasets/cultural-landscapes/regions/metadata/`

</div>

---

## 📘 Overview

The **Metadata Index Registry** is the **machine-readable backbone** of the cultural landscape region metadata system. It:

- Lists all region metadata records (Flint Hills, Smoky Hill, Arkansas River Basin, etc.)  
- Connects each record to:
  - Region slug  
  - STAC Collection/Item IDs  
  - Provenance references  
  - CARE/sensitivity status  
- Provides optional coverage information:
  - Which cultural phases, region kinds, and sensitivities are represented  
  - Quick counts and summaries for dashboards and CI checks  

This directory **does not** define new schemas; it uses schemas from `../schemas/` to validate the indexes stored here.

For the conceptual, human-readable overview of cultural landscape region metadata, see:

- `../README.md`

---

## 🗂️ Directory Layout

~~~text
docs/analyses/archaeology/datasets/cultural-landscapes/regions/metadata/registry/
├── 📄 README.md                                   # This file (index registry standard)
│
├── 🧾 regions-metadata-index.v1.json              # Primary index: region slug ↔ metadata JSON-LD & related IDs
└── 🧾 regions-metadata-coverage.v1.json           # Optional coverage / summary metrics (phase, type, sensitivity)
~~~

**Directory contract:**

- `regions-metadata-index.v1.json` is the **authoritative mapping** between:
  - Region slugs  
  - Region metadata JSON-LD records  
  - STAC IDs  
  - Provenance references  
  - CARE fields (sensitivity & review)  

- `regions-metadata-coverage.v1.json` is **optional**, and provides summarized / aggregated views.  
- JSON schemas for these files are defined in:

  - `../schemas/region-metadata.schema.v1.json`  
  - `../schemas/region-metadata-profile-archaeology.v1.json`  
  - Plus dedicated index/coverage schemas referenced by CI tooling.

---

## 🧾 `regions-metadata-index.v1.json` — Primary Index

This file is the **core registry** for all cultural landscape region metadata.

### 1️⃣ Core Structure (Illustrative)

At a high level, the file is expected to hold an array or object keyed by region slug, for example:

~~~json
{
  "regions": [
    {
      "region_slug": "flint-hills-region",
      "region_kind": ["eco-cultural"],
      "metadata_path": "docs/analyses/archaeology/datasets/cultural-landscapes/regions/flint-hills-region/metadata/dcat-flint-hills-region-v1.jsonld",
      "stac_collection_id": "kfm-arch-lands-flint-hills-region-v1",
      "stac_item_ids": [
        "kfm-arch-lands-flint-hills-region-v1"
      ],
      "provenance_refs": [
        "docs/analyses/archaeology/datasets/cultural-landscapes/provenance/flint-hills-region-v1.json"
      ],
      "care": {
        "sensitivity": "generalized",
        "review": "faircare+tribal",
        "visibility_rules": "polygon-generalized"
      },
      "temporal": {
        "culture_phases": ["Woodland", "Late Prehistoric", "Protohistoric"]
      },
      "status": "active"
    }
  ]
}
~~~

> **Note:** The exact schema is defined in the JSON schema referenced by CI.  
> This snippet is illustrative and must **not** be treated as the definitive shape.

### 2️⃣ Required Fields (Per Region Entry)

Each region entry must include at least:

- `region_slug`  
  - Matches directory + metadata naming (e.g., `"flint-hills-region"`).  
- `region_kind`  
  - Array of controlled values, e.g., `"eco-cultural"`, `"drainage"`, `"territorial-generalized"`.  
- `metadata_path`  
  - Relative path to the canonical DCAT/JSON-LD file for the region (e.g., `../flint-hills-region/metadata/dcat-flint-hills-region-v1.jsonld`).  
- `stac_collection_id`  
- `stac_item_ids` (optional array).  
- `provenance_refs`  
  - Array of paths/URIs to canonical PROV-O logs.  
- `care` block:
  - `sensitivity` — `"generalized"` or `"restricted-generalized"` (public artifacts).  
  - `review` — `"faircare"`, `"tribal"`, or combined string (e.g., `"faircare+tribal"`).  
  - `visibility_rules` — `"polygon-generalized"`, `"h3-only"`, `"no-exact-boundaries"`, or governed combination.  
- `temporal` block:
  - `culture_phases` — array of KFM archaeology ontology phase labels.

Optional fields may include:

- `status` — `"active"`, `"deprecated"`, `"internal-only"`, `"draft"`.  
- `notes` — short human-readable notes (non-authoritative).

---

## 📊 `regions-metadata-coverage.v1.json` — Coverage Summary (Optional)

This file is **optional** and provides **aggregated views** of the regional metadata coverage. For example:

- Counts by `region_kind` (eco-cultural, drainage, etc.)  
- Coverage by `culture_phase` (how many regions per phase)  
- Distributions by CARE sensitivity (`generalized` vs `restricted-generalized`)  

Illustrative shape:

~~~json
{
  "summary": {
    "total_regions": 3,
    "by_kind": {
      "eco-cultural": 1,
      "drainage": 2
    },
    "by_culture_phase": {
      "Late Prehistoric": 3,
      "Protohistoric": 2
    },
    "by_sensitivity": {
      "generalized": 3,
      "restricted-generalized": 0
    }
  }
}
~~~

**Important:**

- This file is **derived** from `regions-metadata-index.v1.json` and per-region metadata.  
- It must never contradict the index; CI should regenerate or validate it as needed.  
- It is useful for dashboards, coverage tests, and automated documentation.

---

## ⚖ FAIR+CARE & Sovereignty Guardrails

The index registry must **reinforce** FAIR+CARE and sovereignty protections:

- CARE fields in the index (`care.sensitivity`, `care.review`, `care.visibility_rules`) must **match**:
  - Per-region metadata JSON-LD  
  - STAC artifacts  
  - Canonical PROV-O logs  

- The index must **not**:
  - Downgrade sensitivity relative to any canonical sources.  
  - Introduce new interpretations of review status that are not expressed elsewhere.  

- Any changes to CARE or sovereignty attributes are **governance events** and must:
  - Go through FAIR+CARE + sovereignty review.  
  - Be reflected first in provenance and per-region metadata, then synced into this index.

---

## 🔗 Relationship to Other Components

This registry is tightly coupled to:

1. **Region Metadata Records**
   - `../README.md`  
   - `../*-metadata-v*.jsonld` per region  

2. **Region Datasets & READMEs**
   - `../../README.md`  
   - `../../flint-hills-region/README.md`, `../../arkansas-river-basin/README.md`, etc.  

3. **Region STAC Registry**
   - `../../stac/README.md`  
   - `../../stac/collections/*.json`, `../../stac/items/*.json`  

4. **Provenance Systems**
   - Global: `../../../provenance/README.md`  
   - Region provenance registry: `../../provenance/README.md` & `../../provenance/registry/`  

**Contract:**

Every public cultural landscape region **must** have:

- A metadata record JSON-LD under `../`.  
- One or more STAC artifacts under `../../stac/`.  
- One or more provenance logs under `../../../provenance/`.  
- A corresponding entry in `regions-metadata-index.v1.json`.  

If any of these links are missing or inconsistent, CI must mark the registry as **invalid**.

---

## 🧪 Validation & CI/CD

The Metadata Index Registry is **CI-enforced**.

### Schema Validation

- `regions-metadata-index.v1.json` must validate against its dedicated index schema (referenced by CI tooling).  
- `regions-metadata-coverage.v1.json` (if present) must validate against its coverage schema.

### Cross-Link Validation

CI must verify that:

- Each `metadata_path`:
  - Points to an existing JSON-LD file.  
  - Passes validation against `region-metadata.schema.v1.json` and `region-metadata-profile-archaeology.v1.json`.  

- Each `stac_collection_id` and each ID in `stac_item_ids`:
  - Exists in the region STAC registry.  
  - Matches the IDs declared in STAC JSON.  

- Each entry in `provenance_refs`:
  - Points to an existing canonical PROV-O log.  
  - Corresponds to the `kfm:provenance_ref` fields in per-region metadata.

### CARE Consistency

- `care` blocks in the index must match:
  - CARE fields in metadata and provenance.  
  - No forbidden downgrades or inconsistent visibility rules.

### Indicative CI Workflows

- `metadata-validate.yml`  
- `artifact-stac-validate.yml`  
- `faircare-audit.yml`  
- `archaeology-provenance-validate.yml`  
- `region-metadata-registry-validate.yml`  

**CI must block:**

- Adding region entries without valid metadata, STAC, and provenance.  
- CARE/sovereignty inconsistencies.  
- Schema-breaking changes to index or coverage files.

---

## 🧭 Authoring & Maintenance Workflow

When adding or updating a cultural landscape region:

1. **Create/Update Region Dataset & README**  
   - Under `../../<region-slug>/`.

2. **Create/Update Region Metadata JSON-LD**  
   - Under `../<region-slug>/metadata/`.  
   - Ensure it passes schema checks.

3. **Create/Update STAC Artifacts**  
   - Under `../../stac/collections/` and `../../stac/items/`.

4. **Ensure Provenance Exists**  
   - Under `../../../provenance/` with correct CARE and lineage.

5. **Update Metadata Index**  
   - Add or modify entry in `regions-metadata-index.v1.json`.  
   - Optionally update `regions-metadata-coverage.v1.json`.

6. **Run Local Validation**  
   - Use repo tooling (e.g., `make validate-region-metadata-registry`) to run schema and cross-link checks.

7. **Submit PR & Address CI/Governance Feedback**  
   - CI enforces schema, linkage, and CARE/sovereignty integrity.  
   - Governance reviewers approve changes as needed.

---

## 🕰️ Version History

| Version  | Date       | Author                                      | Summary                                                                 |
|----------|------------|---------------------------------------------|-------------------------------------------------------------------------|
| v11.2.3  | 2025-12-02 | Cultural Landscape WG · FAIR+CARE Council   | Established cultural landscape region metadata index registry; defined index & coverage contracts, CI cross-link rules, and CARE/sovereignty safeguards; aligned with region metadata, STAC, and provenance standards and KFM-MDP v11.2.2. |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — CC-BY 4.0**  
FAIR+CARE Certified · MCP-DL v6.3 · KFM-MDP v11.2.2 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[⬅ Back to Region Metadata Registry](../README.md) · [⬅ Back to Cultural Landscape Regions](../../README.md)

</div>
