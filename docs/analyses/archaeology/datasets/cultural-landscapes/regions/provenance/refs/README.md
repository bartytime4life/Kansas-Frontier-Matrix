---
title: "🧬 KFM v11.2.3 — Cultural Landscape Region Provenance Ref Files (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/datasets/cultural-landscapes/regions/provenance/refs/README.md"
version: "v11.2.3"
last_updated: "2025-12-02"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Biannual · Cultural Landscape Working Group · FAIR+CARE Council · Metadata Standards Subcommittee"
content_stability: "stable"
backward_compatibility: "v10.4.0 → v11.2.3 region-provenance-ref-contract compatible"

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
doc_kind: "Region Provenance Ref Files"
intent: "cultural-landscape-region-provenance-refs"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Compliant"
---

<div align="center">

# 🧬 **KFM — Cultural Landscape Region Provenance Ref Files**  
`docs/analyses/archaeology/datasets/cultural-landscapes/regions/provenance/refs/README.md`

**Purpose:**  
Define and govern the **region-level provenance ref JSON files** used to quickly resolve **canonical PROV-O provenance logs** for each cultural landscape region.  

This directory provides **lightweight, non-authoritative reference objects** that:

- Map **region slugs + dataset versions → canonical provenance log paths**  
- Expose **summary CARE / review info** for Story Nodes & Focus Mode chips  
- Allow web clients and tooling to resolve provenance **without scanning full directories**

Canonical PROV-O provenance JSON-LD documents remain in:

`docs/analyses/archaeology/datasets/cultural-landscapes/provenance/`

</div>

---

## 📘 Overview

The **refs layer** sits underneath the region provenance registry:

- Registry (index):  
  `docs/analyses/archaeology/datasets/cultural-landscapes/regions/provenance/registry/regions-provenance-index.v1.json`
- Region-local refs (per region):  
  `docs/analyses/archaeology/datasets/cultural-landscapes/regions/<region-slug>/provenance/<region-slug>-v*.prov-ref.json`
- Shared refs (this directory):  
  `docs/analyses/archaeology/datasets/cultural-landscapes/regions/provenance/refs/*.prov-ref.json`

This directory is the **central home** for region provenance ref JSONs, providing:

- A **consistent file naming pattern** for all regions  
- A single place CI can validate all ref files  
- A “cache layer” that higher-level systems can read without walking every region directory

Ref files are **non-authoritative**:

- Canonical truth for provenance always lives in **PROV-O JSON-LD logs** and the **provenance index registry**.  
- Any disagreement between a ref file and canonical logs is treated as a **bug** in the ref file.

---

## 🗂️ Directory Layout

~~~text
docs/analyses/archaeology/datasets/cultural-landscapes/regions/provenance/refs/
├── 📄 README.md                                        # This file (ref file contract & layout)
│
├── 🧬 flint-hills-region-v1.prov-ref.json              # Ref → canonical Flint Hills provenance log(s)
├── 🧬 smoky-hill-region-v1.prov-ref.json               # Ref → canonical Smoky Hill provenance log(s)
├── 🧬 arkansas-river-basin-region-v1.prov-ref.json      # Ref → canonical Arkansas River Basin provenance log(s)
└── 🧬 <region-slug>-v<semver>.prov-ref.json            # Future governed region provenance refs
~~~

**Directory contract:**

- Only **ref JSON files** (`*.prov-ref.json`) and this `README.md` may live here.  
- No canonical PROV-O JSON-LD logs are allowed in this directory.  
- Per-region directories may keep their own local ref files, but this directory is the **governed master set** used by CI and central tooling.

---

## 🧬 Ref File Contract (`*.prov-ref.json`)

Each file in this directory:

- Represents a single **region slug + dataset semantic version** pair  
- Points to one or more **canonical PROV-O provenance logs**  
- Provides **summary CARE / review / timestamp** fields for fast access

### Required Fields (Per Ref File)

Each `*.prov-ref.json` must include, at minimum:

- `region_slug`  
  - String. Example: `"flint-hills-region"`, `"smoky-hill-region"`, `"arkansas-river-basin-region"`.  
- `dataset_id`  
  - String. Primary STAC Item ID for the region (e.g., `"kfm-arch-lands-flint-hills-region-v1"`).  
- `canonical_provenance_paths`  
  - Array of string paths/URIs to canonical PROV-O logs under:  
    `docs/analyses/archaeology/datasets/cultural-landscapes/provenance/`  
- `care:sensitivity`  
  - `"generalized"` or `"restricted-generalized"` (public artifacts only).  
- `care:review`  
  - `"faircare"`, `"tribal"`, or combined form (e.g., `"faircare+tribal"`).  
- `care:visibility_rules`  
  - `"polygon-generalized"`, `"h3-only"`, `"no-exact-boundaries"`, or governed combinations.  

Recommended additional fields:

- `last_review_date` — ISO8601 date when provenance/CARE review was last completed.  
- `status` — `"active"`, `"deprecated"`, `"internal-only"`, `"draft"`.

### Illustrative Example

> **Note:** This is illustrative only; exact constraints are enforced by the region provenance ref schema used by CI.

~~~json
{
  "region_slug": "flint-hills-region",
  "dataset_id": "kfm-arch-lands-flint-hills-region-v1",
  "canonical_provenance_paths": [
    "docs/analyses/archaeology/datasets/cultural-landscapes/provenance/flint-hills-region-v1.json"
  ],
  "care:sensitivity": "generalized",
  "care:review": "faircare+tribal",
  "care:visibility_rules": "polygon-generalized",
  "last_review_date": "2025-11-17",
  "status": "active"
}
~~~

---

## ⚖ CARE, Sovereignty & Consistency Rules

Ref files must **reinforce**, not weaken, CARE and sovereignty protections:

- `care:sensitivity`, `care:review`, and `care:visibility_rules` in refs **must match**:
  - CARE fields in the canonical PROV-O logs  
  - CARE fields in region metadata JSON-LD  
  - CARE fields in the region provenance index registry

Ref files:

- **Must not** downgrade sensitivity relative to canonical sources.  
- **Must not** invent new review statuses or visibility policies.  
- **Must not** contradict per-region metadata or provenance.

Any change to CARE fields in these ref files is a **governance event** and must:

1. Be made first in canonical provenance + metadata.  
2. Then be propagated into:
   - Region provenance index registry  
   - These ref files.

---

## 🔗 Relationship to Other Provenance Components

This directory is tightly coupled to:

1. **Global Cultural Landscape Provenance Logs**  
   - `docs/analyses/archaeology/datasets/cultural-landscapes/provenance/README.md`  
   - `docs/analyses/archaeology/datasets/cultural-landscapes/provenance/*.json`

2. **Region Provenance Registry (Index)**  
   - `docs/analyses/archaeology/datasets/cultural-landscapes/regions/provenance/README.md`  
   - `docs/analyses/archaeology/datasets/cultural-landscapes/regions/provenance/registry/region-provenance-index.v1.json`

3. **Region Metadata Registry**  
   - `docs/analyses/archaeology/datasets/cultural-landscapes/regions/metadata/README.md`  
   - `docs/analyses/archaeology/datasets/cultural-landscapes/regions/metadata/registry/regions-metadata-index.v1.json`

4. **Per-Region Provenance Folders**  
   - `docs/analyses/archaeology/datasets/cultural-landscapes/regions/<region-slug>/provenance/`

**Contract:**

- Every **public region dataset** should have:
  - Canonical PROV-O log(s) under `../../../../provenance/`.  
  - An entry in the **region provenance index**.  
  - A corresponding `*.prov-ref.json` in this `refs/` directory.

If any of these links are missing or inconsistent, CI must treat this as an **error**.

---

## 🧪 Validation & CI/CD

Ref files in this directory are **CI-enforced**.

### Schema Validation

- All `*.prov-ref.json` must validate against a **region provenance ref schema**, referenced by:
  - `region-provenance-registry-validate.yml` (or equivalent CI job).  

Schema checks ensure:

- Required fields are present and correctly typed.  
- Values such as `region_slug`, `dataset_id`, and `canonical_provenance_paths` follow naming and path rules.

### Cross-Link Validation

CI must verify that for each ref file:

- `canonical_provenance_paths` entries:
  - Point to existing PROV-O logs.  
  - Match entries in the region provenance index registry.  

- `region_slug`:
  - Matches an existing region directory under `../../..`.  

- `dataset_id`:
  - Matches an existing STAC Item ID in the region STAC registry.  

- CARE fields:
  - Match those in:
    - Canonical PROV-O logs  
    - Region metadata JSON-LD  
    - Region provenance index registry

### Governance Checks

CI must **block**:

- Ref files pointing at missing or renamed canonical provenance logs.  
- CARE/sovereignty inconsistencies between refs and canonical sources.  
- Introduction of refs for regions that do not exist or lack valid provenance.

Indicative workflows:

- `archaeology-provenance-validate.yml`  
- `region-provenance-registry-validate.yml`  
- `metadata-validate.yml`  
- `faircare-audit.yml`

---

## 🧭 Authoring & Maintenance Workflow

When adding or updating provenance for a region:

1. **Update Canonical Provenance (Required First)**  
   - Edit or add PROV-O JSON-LD under:  
     `docs/analyses/archaeology/datasets/cultural-landscapes/provenance/`

2. **Update Region Metadata & STAC**  
   - Ensure region metadata JSON-LD and STAC artifacts reference the correct provenance IDs/paths.

3. **Update Region Provenance Index Registry**  
   - Add or modify the region entry in:  
     `docs/analyses/archaeology/datasets/cultural-landscapes/regions/provenance/registry/region-provenance-index.v1.json`

4. **Create/Update Ref JSON in `refs/`**  
   - Add or update `<region-slug>-v<semver>.prov-ref.json` in this directory.  
   - Ensure `region_slug`, `dataset_id`, and `canonical_provenance_paths` match canonical sources.  
   - Sync CARE fields and `last_review_date`.

5. **Run Local Validation**  
   - Use repo tooling (e.g., `make validate-region-provenance-refs`) to run schema + cross-link checks.

6. **Submit PR & Address CI/Governance Feedback**  
   - CI enforces schema, linkage, and CARE/sovereignty consistency.  
   - Governance reviewers approve changes where CARE/sovereignty semantics have shifted.

---

## 🕰️ Version History

| Version  | Date       | Author                                      | Summary                                                                 |
|----------|------------|---------------------------------------------|-------------------------------------------------------------------------|
| v11.2.3  | 2025-12-02 | Cultural Landscape WG · FAIR+CARE Council   | Established cultural landscape region provenance ref directory; defined ref JSON contract, CI cross-link rules, and CARE/sovereignty safeguards; aligned with provenance index, region metadata, and KFM-MDP v11.2.2. |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — CC-BY 4.0**  
FAIR+CARE Certified · MCP-DL v6.3 · KFM-MDP v11.2.2 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[⬅ Back to Region Provenance Registry](../README.md) · [⬅ Back to Region Provenance Index Registry](../registry/README.md) · [⬅ Back to Cultural Landscape Regions](../../README.md)

</div>
