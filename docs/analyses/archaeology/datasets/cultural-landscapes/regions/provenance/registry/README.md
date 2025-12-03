---
title: "🧬 KFM v11.2.3 — Cultural Landscape Region Provenance Index Registry (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/datasets/cultural-landscapes/regions/provenance/registry/README.md"
version: "v11.2.3"
last_updated: "2025-12-02"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Biannual · Cultural Landscape Working Group · FAIR+CARE Council · Metadata Standards Subcommittee"
content_stability: "stable"
backward_compatibility: "v10.4.0 → v11.2.3 region-provenance-registry-index compatible"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-version-hash>"
doc_integrity_checksum: "<sha256-of-this-file>"

sbom_ref: "../../../../../../../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../../../../../../../releases/v11.2.3/manifest.zip"
telemetry_ref: "../../../../../../../../releases/v11.2.3/focus-telemetry.json"
telemetry_schema: "../../../../../../../../schemas/telemetry/archaeology-cultural-landscapes-provenance-v1.json"

governance_ref: "../../../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"

status: "Active / Enforced"
doc_kind: "Region Provenance Registry Index"
intent: "cultural-landscape-region-provenance-index-registry"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Compliant"
---

<div align="center">

# 🧬 **KFM — Cultural Landscape Region Provenance Index Registry**  
`docs/analyses/archaeology/datasets/cultural-landscapes/regions/provenance/registry/README.md`

**Purpose:**  
Define and govern the **machine-readable index files** that register all **region-level provenance mappings** for cultural landscape regions in the Kansas Frontier Matrix (KFM).  

This directory provides:

- A **canonical index** mapping region slugs and dataset IDs to **canonical PROV-O provenance logs**  
- Optional **coverage summaries** for audit, dashboards, and CI checks  
- CI-enforced contracts tying region provenance to **STAC**, **metadata**, and **CARE/sovereignty** governance

Canonical PROV-O provenance JSON-LD documents live in:

`docs/analyses/archaeology/datasets/cultural-landscapes/provenance/`

</div>

---

## 📘 Overview

The **Region Provenance Index Registry** is the **routing table** for cultural landscape region provenance:

- It tells KFM **which PROV-O log(s)** govern each region dataset version.  
- It exposes **CARE / sensitivity / visibility** fields at the registry level.  
- It supports:

  - ETL and graph loaders (which provenance to attach to which region node)  
  - Story Node and Focus Mode resolvers (which provenance to surface in the UI)  
  - CI and governance (consistency between provenance, metadata, and STAC)

This directory does **not** contain canonical PROV-O logs or ref JSONs; it only contains:

- **Index JSON** describing the mapping  
- **Optional coverage JSON** summarizing registry contents

For the region-level provenance overview, see:

- `../README.md`  

For per-region provenance ref files, see:

- `../refs/README.md`

---

## 🗂️ Directory Layout

~~~text
docs/analyses/archaeology/datasets/cultural-landscapes/regions/provenance/registry/
├── 📄 README.md                                   # This file (index registry standard)
│
├── 🧾 region-provenance-index.v1.json             # Primary index: region slug ↔ provenance doc(s)
└── 🧾 region-provenance-coverage.v1.json          # Optional coverage/summary (phase, type, sensitivity, status)
~~~

**Directory contract:**

- `region-provenance-index.v1.json` is the **authoritative mapping** from region datasets to canonical PROV-O logs.  
- `region-provenance-coverage.v1.json` is **optional**, and provides aggregated views of that mapping.  
- JSON schemas for these files live in:

  - `../schemas/region-provenance-index.schema.v1.json`  
  - `../schemas/region-provenance-coverage.schema.v1.json`

---

## 🧾 `region-provenance-index.v1.json` — Primary Index

This file is the **core registry** for region-level provenance.

### 1️⃣ Core Structure (Illustrative)

At a high level, the file is expected to hold an array of region entries, for example:

~~~json
{
  "regions": [
    {
      "region_slug": "flint-hills-region",
      "region_dataset_ids": [
        "kfm-arch-lands-flint-hills-region-v1"
      ],
      "provenance_docs": [
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

> **Note:** Exact validation rules are encoded in `region-provenance-index.schema.v1.json` and must be treated as the authority.

### 2️⃣ Required Fields (Per Region Entry)

Each region entry must include at least:

- `region_slug`  
  - String. Must match region directory naming (e.g., `"flint-hills-region"`, `"arkansas-river-basin-region"`).

- `region_dataset_ids`  
  - Array of versioned dataset identifiers (e.g., STAC Item IDs for the region).

- `provenance_docs`  
  - Array of paths/URIs to canonical PROV-O JSON-LD logs under  
    `docs/analyses/archaeology/datasets/cultural-landscapes/provenance/`.

- `care` object:
  - `sensitivity` — `"generalized"` or `"restricted-generalized"` (for public artifacts).  
  - `review` — `"faircare"`, `"tribal"`, or a combined pattern (e.g., `"faircare+tribal"`).  
  - `visibility_rules` — `"polygon-generalized"`, `"h3-only"`, `"no-exact-boundaries"`, or governed combinations.

- `temporal` object:
  - `culture_phases` — array of KFM archaeology ontology phase labels.

Optional (but recommended) fields:

- `status` — `"active"`, `"deprecated"`, `"internal-only"`, `"draft"`.  
- `notes` — short human-readable notes (non-authoritative).  
- `last_review_date` — ISO8601 date for last provenance/CARE review.

---

## 📊 `region-provenance-coverage.v1.json` — Coverage Summary (Optional)

This file is **optional** and provides **aggregated views** over the index, for example:

- Counts of regions by **status** (`active`, `deprecated`, etc.)  
- Distribution by **CARE sensitivity** (`generalized`, `restricted-generalized`)  
- Coverage by **cultural phase** or **region kind** (via metadata linkage)

Illustrative pattern:

~~~json
{
  "summary": {
    "total_regions": 3,
    "by_status": {
      "active": 3,
      "deprecated": 0
    },
    "by_sensitivity": {
      "generalized": 3,
      "restricted-generalized": 0
    },
    "by_culture_phase": {
      "Late Prehistoric": 3,
      "Protohistoric": 2
    }
  }
}
~~~

**Important:**

- This file is **derived** from `region-provenance-index.v1.json` and canonical provenance/metadata.  
- It must **never** contradict the index or canonical logs.  
- CI may regenerate or validate it as part of registry checks.

---

## ⚖ FAIR+CARE & Sovereignty Guardrails

The index registry must **reinforce** FAIR+CARE and sovereignty protections:

- CARE fields in each entry (`care.sensitivity`, `care.review`, `care.visibility_rules`) must **match**:

  - CARE fields in canonical PROV-O logs  
  - CARE fields in per-region metadata JSON-LD  
  - CARE fields in region metadata/index registries

- The index must **not**:

  - Downgrade sensitivity relative to any canonical provenance record.  
  - Introduce new review statuses or visibility rules that are not present in canonical sources.

- Any changes to CARE or sovereignty attributes are **governance events** and must:

  1. Be made first in canonical PROV-O logs and region metadata.  
  2. Then be propagated into this index and associated ref files.

---

## 🔗 Relationship to Other Components

This registry integrates with:

1. **Global Cultural Landscape Provenance Logs**  
   - `docs/analyses/archaeology/datasets/cultural-landscapes/provenance/README.md`  
   - `docs/analyses/archaeology/datasets/cultural-landscapes/provenance/*.json`

2. **Region Provenance Root & Ref Layers**  
   - `../README.md`  
   - `../refs/README.md` and `../refs/*.prov-ref.json`

3. **Region Metadata Registries**  
   - `../../metadata/README.md`  
   - `../../metadata/registry/regions-metadata-index.v1.json`

4. **Region STAC Registry**  
   - `../../stac/README.md`  
   - STAC Collections/Items that reference provenance via `kfm:provenance_ref`.

**Contract:**

Every **public cultural landscape region dataset** must have:

- Canonical PROV-O provenance log(s) under `../../../../provenance/`.  
- A corresponding entry in `region-provenance-index.v1.json`.  
- CARE and temporal information consistent with:

  - Region metadata JSON-LD  
  - Region STAC artifacts  
  - Region metadata index registry

If any of these links are missing, inconsistent, or mis-aligned, CI must treat the registry as **invalid**.

---

## 🧪 Validation & CI/CD

The Region Provenance Index Registry is **CI-enforced**.

### Schema Validation

- `region-provenance-index.v1.json` must validate against:  
  - `../schemas/region-provenance-index.schema.v1.json`  

- `region-provenance-coverage.v1.json` (if present) must validate against:  
  - `../schemas/region-provenance-coverage.schema.v1.json`

### Cross-Link Validation

CI must verify for each index entry:

- All `provenance_docs` paths:
  - Point to existing canonical PROV-O JSON-LD files.  
  - Match IDs/paths referenced in region metadata and STAC.

- All `region_dataset_ids`:
  - Correspond to STAC Item IDs in the region STAC registry.  

- `region_slug`:
  - Matches an existing region directory under `../../..`.  

- CARE fields:
  - Match CARE metadata in canonical provenance and metadata registries.

### CARE & Governance Consistency

- No entry may introduce:

  - A less restrictive sensitivity or visibility rule than canonical sources.  
  - An inconsistent review path compared to provenance and metadata.

### Indicative CI Workflows

- `archaeology-provenance-validate.yml`  
- `region-provenance-registry-validate.yml`  
- `metadata-validate.yml`  
- `artifact-stac-validate.yml`  
- `faircare-audit.yml`

CI must **block**:

- Adding index entries without valid provenance, metadata, and STAC artifacts.  
- CARE/sovereignty inconsistencies.  
- Schema-breaking changes to index or coverage files.

---

## 🧭 Authoring & Maintenance Workflow

When adding or updating region-level provenance:

1. **Update Canonical PROV-O Logs**  
   - Add or modify PROV-O JSON-LD under:  
     `docs/analyses/archaeology/datasets/cultural-landscapes/provenance/`

2. **Update Region Metadata & STAC**  
   - Ensure `kfm:provenance_ref` fields in region metadata JSON-LD and STAC artifacts point to the correct logs.

3. **Update Region Provenance Index**  
   - Add or update the corresponding entry in `region-provenance-index.v1.json`.  
   - Ensure `region_slug`, `region_dataset_ids`, and `provenance_docs` are correct.  
   - Keep CARE and temporal fields in sync with canonical sources.

4. **Update Ref Files (If Applicable)**  
   - Adjust `../refs/*.prov-ref.json` to align with the index and canonical logs.

5. **Update Coverage (Optional)**  
   - Regenerate or update `region-provenance-coverage.v1.json` as needed.

6. **Run Local Validation**  
   - Use repo tooling (e.g., `make validate-region-provenance-registry`) to run schema + cross-link checks.

7. **Submit PR & Address CI/Governance Feedback**  
   - CI enforces schema, linkage, and CARE/sovereignty consistency.  
   - Governance reviewers approve changes affecting CARE, sovereignty, or major provenance logic.

---

## 🕰️ Version History

| Version  | Date       | Author                                      | Summary                                                                 |
|----------|------------|---------------------------------------------|-------------------------------------------------------------------------|
| v11.2.3  | 2025-12-02 | Cultural Landscape WG · FAIR+CARE Council   | Established cultural landscape region provenance index registry; defined index & coverage contracts, CI cross-link rules, and CARE/sovereignty safeguards; aligned with region provenance, metadata, STAC, and KFM-MDP v11.2.2. |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — CC-BY 4.0**  
FAIR+CARE Certified · MCP-DL v6.3 · KFM-MDP v11.2.2 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[⬅ Back to Region Provenance Registry](../README.md) · [⬅ Back to Cultural Landscape Regions](../../README.md)

</div>
