---
title: "🧬 KFM v11.2.3 — Cultural Landscape Region Provenance Registry (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/datasets/cultural-landscapes/regions/provenance/README.md"
version: "v11.2.3"
last_updated: "2025-12-02"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Biannual · Cultural Landscape Working Group · FAIR+CARE Council · Metadata Standards Subcommittee"
content_stability: "stable"
backward_compatibility: "v10.4.0 → v11.2.3 region-provenance-contract compatible"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-version-hash>"
doc_integrity_checksum: "<sha256-of-this-file>"

sbom_ref: "../../../../../../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../../../../../../releases/v11.2.3/manifest.zip"
telemetry_ref: "../../../../../../../releases/v11.2.3/focus-telemetry.json"
telemetry_schema: "../../../../../../../schemas/telemetry/archaeology-cultural-landscapes-provenance-v1.json"

governance_ref: "../../../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"

status: "Active / Enforced"
doc_kind: "Region Provenance Registry"
intent: "cultural-landscape-region-provenance-registry"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Compliant"
---

<div align="center">

# 🧬 **KFM — Cultural Landscape Region Provenance Registry**  
`docs/analyses/archaeology/datasets/cultural-landscapes/regions/provenance/README.md`

**Purpose:**  
Define and govern the **region-scoped provenance registry** for cultural landscape regions in the Kansas Frontier Matrix (KFM).  
This directory provides a **region-centric index and linkage layer** on top of the canonical cultural landscape provenance system, ensuring that:

- Each **region dataset** (e.g., Flint Hills, Smoky Hill, Arkansas River Basin) has discoverable, validated **PROV-O provenance**  
- Region-level UIs, Story Nodes, and Focus Mode can resolve provenance quickly via **region slugs and dataset IDs**  
- FAIR+CARE and sovereignty constraints encoded in provenance are **enforced consistently** at the region layer  

Canonical PROV-O JSON-LD logs remain in the **global provenance directory**:  
`docs/analyses/archaeology/datasets/cultural-landscapes/provenance/`.

</div>

---

## 📘 Overview

The **Region Provenance Registry** is a **linkage and indexing layer** that ties together:

- **Region datasets** under  
  `docs/analyses/archaeology/datasets/cultural-landscapes/regions/`
- **Canonical PROV-O provenance logs** under  
  `docs/analyses/archaeology/datasets/cultural-landscapes/provenance/`
- **Region metadata records** under  
  `docs/analyses/archaeology/datasets/cultural-landscapes/regions/metadata/`

This directory does **not** introduce new canonical provenance logs.  
Instead, it:

- Registers which PROV-O documents apply to which **region slugs and dataset versions**  
- Exposes **machine-readable indices** for CI, ETL, Story Node, and Focus Mode pipelines  
- Stores **lightweight per-region reference files** to accelerate lookups in web clients  

The canonical contract for cultural landscape provenance structure and CARE rules is defined at:

- `docs/analyses/archaeology/datasets/cultural-landscapes/provenance/README.md`

---

## 🗂️ Directory Layout

~~~text
docs/analyses/archaeology/datasets/cultural-landscapes/regions/provenance/
├── 📄 README.md                                   # This file (region provenance registry standard)
│
├── 📚 registry/                                   # Region ↔ provenance index and linkage tables
│   ├── region-provenance-index.v1.json            # Primary index: region slug ↔ provenance document(s)
│   └── region-provenance-coverage.v1.json         # Optional summary: coverage by phase, type, sensitivity
│
├── 📑 schemas/                                    # JSON schemas for region provenance registry files
│   ├── region-provenance-index.schema.v1.json     # Shape for region-provenance-index.v1.json
│   └── region-provenance-coverage.schema.v1.json  # Shape for coverage/summary files
│
└── 🧬 refs/                                       # Optional thin references for UI/tooling
    ├── flint-hills-region-v1.prov-ref.json        # Pointer to canonical Flint Hills provenance log(s)
    ├── smoky-hill-region-v1.prov-ref.json         # Pointer to canonical Smoky Hill provenance log(s)
    ├── arkansas-river-basin-region-v1.prov-ref.json # Pointer to canonical Arkansas River Basin provenance log(s)
    └── <region-slug>-v<semver>.prov-ref.json      # Future region provenance references
~~~

**Directory contract:**

- Canonical **PROV-O JSON-LD documents** live in:  
  `docs/analyses/archaeology/datasets/cultural-landscapes/provenance/`  
  (including templates and examples).  
- This `regions/provenance/` directory must **never** contain canonical provenance logs; only:
  - **Indices** (`registry/*.json`)  
  - **Schemas** for those indices  
  - **Lightweight reference objects** under `refs/` pointing at canonical logs.  
- Per-region folders (e.g., `../flint-hills-region/`) may also contain **local ref files** for convenience, but their content must stay consistent with this registry.

---

## 📦 Region Provenance Index Requirements

The primary index file:

- `registry/region-provenance-index.v1.json`

must provide a **complete, machine-readable mapping** from region datasets to their canonical provenance logs.

### 1. Core Structure

At minimum, each region entry must define:

- `region_slug`  
  - Example: `"flint-hills-region"`, `"smoky-hill-region"`, `"arkansas-river-basin-region"`.  
- `region_dataset_ids`  
  - Versioned dataset identifiers (e.g., STAC IDs, or internal dataset IDs).  
- `provenance_docs`  
  - One or more references to canonical provenance JSON-LD documents under `../../provenance/`.  
- `status`  
  - `"active"`, `"deprecated"`, `"draft"`, or `"internal-only"`.

Illustrative structure:

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
      "status": "active"
    }
  ]
}
~~~

### 2. CARE & Governance Fields

Each entry must also include:

- `care:sensitivity`  
- `care:review`  
- `care:visibility_rules`  

These must **mirror** the values declared in:

- Canonical provenance documents, and  
- Region metadata records in `../metadata/`.

Optional extras:

- `governance_refs` for additional policies or review notes.  

---

## 🧬 Provenance Reference Files (`refs/`)

Files under `refs/` (e.g., `flint-hills-region-v1.prov-ref.json`) are **thin, non-canonical** references used by:

- Web clients (MapLibre/Cesium overlays)  
- Story Node resolvers  
- Focus Mode provenance-chip loaders  

Each file must:

- Be JSON (not full PROV-O); it may include:

  - `region_slug`  
  - `dataset_id`  
  - `canonical_provenance_paths` (array of paths/URIs into the canonical provenance directory)  
  - Extracted summary fields (e.g., review status, sensitivity, last review date), purely as **cache**, not authority  

Example sketch (illustrative):

~~~json
{
  "region_slug": "flint-hills-region",
  "dataset_id": "kfm-arch-lands-flint-hills-region-v1",
  "canonical_provenance_paths": [
    "docs/analyses/archaeology/datasets/cultural-landscapes/provenance/flint-hills-region-v1.json"
  ],
  "care:sensitivity": "generalized",
  "care:review": "faircare+tribal",
  "last_review_date": "2025-11-17"
}
~~~

**Important:**

- Any discrepancy between `refs/` and the canonical provenance logs is treated as a **bug**; canonical logs always win.  
- CI must validate that ref files are consistent with both:
  - `registry/region-provenance-index.v1.json`  
  - Canonical provenance JSON-LD.

---

## ⚖ CARE & Sovereignty Requirements

Region-level provenance metadata in this registry must **reinforce**, not weaken, CARE protections:

- `care:sensitivity` must **never** be downgraded relative to canonical provenance.  
- `care:review` must remain accurate about:
  - FAIR+CARE review  
  - Tribal/sovereign review  
  - Any joint or multi-party governance.  
- `care:visibility_rules` must align with:
  - Region README rules (e.g., Flint Hills, Arkansas River Basin).  
  - Canonical provenance logs and STAC metadata.

**Forbidden behaviors:**

- Introducing region entries in this registry for which **no canonical provenance log exists**.  
- Overriding canonical CARE or sovereignty decisions via local tweaks in the registry.  
- Pointing multiple region entries to the **same** provenance log in ways that confuse interpretation (shared logs must be intentional and documented).

---

## 🧭 Relationship to Other Cultural Landscape Components

This registry is tightly coupled to:

1. **Global Cultural Landscape Provenance Standard**  
   - `docs/analyses/archaeology/datasets/cultural-landscapes/provenance/README.md`  
   - Defines the canonical **PROV-O + CARE + KFM** structure.

2. **Region Datasets**  
   - `docs/analyses/archaeology/datasets/cultural-landscapes/regions/README.md`  
   - Per-region READMEs (e.g., `flint-hills-region/README.md`, `arkansas-river-basin/README.md`).

3. **Region Metadata Registry**  
   - `docs/analyses/archaeology/datasets/cultural-landscapes/regions/metadata/README.md`  
   - DCAT/JSON-LD descriptors for each region.

**Contract:**

- Every **region dataset** must have:
  - A metadata record in `../metadata/`.  
  - One or more canonical provenance logs in `../../provenance/`.  
  - A corresponding entry in `registry/region-provenance-index.v1.json`.  

- Optional `refs/` files and region-local provenance refs (inside each region folder) must be **consistent** with this registry and canonical provenance.

---

## 🧪 Validation & CI/CD

The Region Provenance Registry is **CI-enforced**.  
Every change must pass:

- **Schema validation**  
  - `schemas/region-provenance-index.schema.v1.json`  
  - `schemas/region-provenance-coverage.schema.v1.json` (if used).  

- **Cross-link validation**  
  - All `provenance_docs` entries must point to existing canonical provenance JSON-LD files.  
  - All `region_slug` entries must correspond to:
    - Region directories under `../`.  
    - Metadata records in `../metadata/`.  

- **CARE consistency checks**  
  - `care:*` fields must match canonical provenance logs.  
  - No forbidden downgrades of sensitivity or visibility.

### Indicative CI Workflows

- `metadata-validate.yml`  
- `artifact-stac-validate.yml`  
- `faircare-audit.yml`  
- `archaeology-provenance-validate.yml`  
- `region-provenance-registry-validate.yml` (or equivalent)

**CI must block:**

- Adding region entries with missing or invalid canonical provenance references.  
- Removing or renaming provenance logs without updating this registry.  
- Any conflict between CARE metadata here and canonical logs.

---

## 🧠 Knowledge Graph, Story Node & Focus Mode Integration

### Knowledge Graph (Neo4j)

From this registry, graph loaders infer:

- **Nodes**
  - `CulturalRegion` (linked from region metadata).  
  - `ProvenanceRecord` (from canonical PROV-O logs).  
  - `RegionProvenanceIndexEntry` (optional explicit node type, if modeled).

- **Relationships**
  - `HAS_PROVENANCE` (region ↔ provenance record), driven by this registry.  
  - `HAS_SENSITIVITY` (region ↔ sensitivity classification).  
  - `REVIEWED_BY` (from provenance activities, inferred through canonical logs).

The registry provides a **lightweight lookup** so graph-loading jobs know exactly which provenance documents to attach to each region without re-scanning entire directories.

### Story Nodes

For Story Nodes, this registry provides the **fast mapping** from:

- Region slug → provenance log(s) → narrative-safe explanations  

Story Nodes can use the `refs/` layer to:

- Display provenance chips (e.g., “FAIR+CARE + Tribal Review on 2025-11-17”)  
- Link out to full provenance detail only when requested by the user.

### Focus Mode v2/v3

Focus Mode uses the registry to:

- Enforce **CARE-aware overlays**:
  - Hide or generalize layers when `care:visibility_rules` demand it.  
- Provide consistent provenance explanations in:
  - Side panels  
  - Tooltip chips  
  - “Why am I seeing this region?” dialogs  

By separating the **region-centered index** from the **canonical provenance content**, Focus Mode remains fast and predictable while still respecting the deeper PROV-O graph.

---

## 🧭 Authoring & Maintenance Workflow

Suggested steps when adding/updating a region:

1. **Define/Update Canonical Provenance**  
   - Add or revise PROV-O JSON-LD in:  
     `docs/analyses/archaeology/datasets/cultural-landscapes/provenance/`

2. **Update Region Dataset & Metadata**  
   - Ensure `../<region-slug>/README.md` and `../metadata/*-metadata-v<semver>.jsonld` reference the correct provenance.

3. **Update Region Provenance Registry**  
   - Add/adjust entries in `registry/region-provenance-index.v1.json`.  
   - Create or update `refs/<region-slug>-v<semver>.prov-ref.json` as needed.

4. **Run Local Validation**  
   - Use repo tooling (e.g., `make validate-region-provenance-registry`) to run all schema and cross-link checks.

5. **Submit PR & Address Feedback**  
   - CI will enforce:
     - Schema correctness  
     - CARE consistency  
     - Link integrity  
   - Governance reviewers ensure FAIR+CARE and sovereignty compliance.

---

## 🕰️ Version History

| Version  | Date       | Author                                      | Summary                                                                 |
|----------|------------|---------------------------------------------|-------------------------------------------------------------------------|
| v11.2.3  | 2025-12-02 | Cultural Landscape WG · FAIR+CARE Council   | Created region provenance registry; defined index, schemas, refs, and CI/governance rules; aligned with global cultural landscape provenance standard and KFM-MDP v11.2.2. |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — CC-BY 4.0**  
FAIR+CARE Certified · MCP-DL v6.3 · KFM-MDP v11.2.2 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[⬅ Back to Cultural Landscape Regions](../README.md) · [⬅ Back to Cultural Landscape Region Metadata Registry](../metadata/README.md) · [⬅ Back to Global Cultural Landscape Provenance](../../provenance/README.md)

</div>