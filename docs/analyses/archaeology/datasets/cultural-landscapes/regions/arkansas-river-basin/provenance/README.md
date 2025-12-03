---
title: "🧬 KFM v11.2.3 — Arkansas River Basin Region Provenance Refs (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/datasets/cultural-landscapes/regions/arkansas-river-basin/provenance/README.md"
version: "v11.2.3"
last_updated: "2025-12-02"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Biannual · Cultural Landscape Working Group · FAIR+CARE Council · Metadata Standards Subcommittee"
content_stability: "stable"
backward_compatibility: "Aligned with v11.2.3 cultural-landscape-region provenance-ref contract"

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
doc_kind: "Region Provenance Refs"
intent: "cultural-landscape-region-arkansas-river-basin-provenance-refs"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Compliant"
---

<div align="center">

# 🧬 **KFM — Arkansas River Basin Cultural Landscape Region · Provenance Refs**  
`docs/analyses/archaeology/datasets/cultural-landscapes/regions/arkansas-river-basin/provenance/README.md`

**Purpose:**  
Define and govern the **region-local provenance reference layer** for the **Arkansas River Basin Cultural Landscape Region**.  
This directory does **not** store canonical PROV-O JSON-LD; instead it provides:

- Lightweight JSON **reference objects** that point to **canonical provenance logs**  
- Fast lookup for web clients, Story Nodes, and Focus Mode using the **region slug**  
- A small, region-scoped surface on top of the global cultural landscape provenance system  

Canonical PROV-O provenance logs live in:

`docs/analyses/archaeology/datasets/cultural-landscapes/provenance/`

</div>

---

## 📘 Overview

This `provenance/` directory is the **Arkansas River Basin–specific view** of KFM’s provenance system.

It ties together:

- The region dataset spec:  
  `docs/analyses/archaeology/datasets/cultural-landscapes/regions/arkansas-river-basin/README.md`
- The global cultural landscape provenance standard and logs:  
  `docs/analyses/archaeology/datasets/cultural-landscapes/provenance/`
- The region provenance registry and refs:  
  `docs/analyses/archaeology/datasets/cultural-landscapes/regions/provenance/`

This directory exists so that:

- Region-focused tools (e.g., region page, Story Node inspectors) can resolve provenance via **simple local refs**  
- We avoid duplicating canonical PROV-O JSON while still making provenance **discoverable and cacheable** at region scope  

---

## 🗂️ Directory Layout

~~~text
docs/analyses/archaeology/datasets/cultural-landscapes/regions/arkansas-river-basin/provenance/
├── 📄 README.md                                      # This file (region-local provenance ref contract)
└── 🧬 arkansas-river-basin-region-v1.prov-ref.json   # Thin reference → canonical PROV-O provenance log(s)
~~~

**Directory contract:**

- This directory must **never** contain canonical PROV-O JSON-LD provenance logs.  
- Only **reference objects** (e.g., `*.prov-ref.json`) and this README are allowed.  
- Canonical provenance JSON-LD for this region resides under:  
  `docs/analyses/archaeology/datasets/cultural-landscapes/provenance/`  
  (e.g., `arkansas-river-basin-region-v1.json`).

---

## 🧬 Provenance Ref File Contract

The file:

- `arkansas-river-basin-region-v1.prov-ref.json`

is a **thin, non-authoritative** reference that:

- Maps the **region slug** and dataset ID → one or more canonical PROV-O logs  
- Provides a small **summary cache** (e.g., review status, sensitivity, last review date)  
- Is used by web clients, Story Nodes, and Focus Mode to quickly access provenance info

### Required Fields (Ref JSON)

Illustrative shape (for guidance only):

~~~json
{
  "region_slug": "arkansas-river-basin-region",
  "dataset_id": "kfm-arch-lands-arkansas-river-basin-region-v1",
  "canonical_provenance_paths": [
    "docs/analyses/archaeology/datasets/cultural-landscapes/provenance/arkansas-river-basin-region-v1.json"
  ],
  "care:sensitivity": "generalized",
  "care:review": "faircare+tribal",
  "care:visibility_rules": "polygon-generalized",
  "last_review_date": "2025-11-17"
}
~~~

**Requirements:**

- `region_slug` must be `"arkansas-river-basin-region"`.  
- `dataset_id` must match the primary STAC Item ID for this region.  
- `canonical_provenance_paths` must list only **canonical** PROV-O JSON-LD paths.  
- CARE fields (`care:*`) must be **consistent** with the canonical provenance logs and region metadata.  
- Any temporal fields (e.g., `last_review_date`) are **summaries**, not authority.

---

## ⚖ CARE, Sovereignty & Consistency Rules

Provenance ref files must **strengthen**, not weaken, CARE and sovereignty protections:

- CARE fields in refs (`care:sensitivity`, `care:review`, `care:visibility_rules`) must **match**:
  - Canonical PROV-O logs for Arkansas River Basin.  
  - Region metadata JSON-LD in:  
    `docs/analyses/archaeology/datasets/cultural-landscapes/regions/arkansas-river-basin/metadata/`  
  - Region entries in the global region provenance registry:  
    `docs/analyses/archaeology/datasets/cultural-landscapes/regions/provenance/registry/`.

- Refs must **not**:
  - Downgrade sensitivity relative to canonical provenance.  
  - Override governance or sovereignty decisions.  
  - Introduce new semantics not present in canonical logs.

Any mismatch between a ref file and canonical provenance is treated as a **bug**; canonical PROV-O logs always win.

---

## 🧭 Relationship to Global Provenance & Registries

This region-local directory is tightly coupled to:

1. **Global Cultural Landscape Provenance Standard & Logs**  
   - `docs/analyses/archaeology/datasets/cultural-landscapes/provenance/README.md`  
   - `docs/analyses/archaeology/datasets/cultural-landscapes/provenance/*.json`

2. **Region Provenance Registry**  
   - `docs/analyses/archaeology/datasets/cultural-landscapes/regions/provenance/README.md`  
   - `docs/analyses/archaeology/datasets/cultural-landscapes/regions/provenance/registry/region-provenance-index.v1.json`

3. **Region Metadata Registry & Per-Region Metadata**  
   - Global registry: `docs/analyses/archaeology/datasets/cultural-landscapes/regions/metadata/README.md`  
   - Per-region: `../metadata/dcat-arkansas-river-basin-region-v1.jsonld`

**Contract:**

- The global **region-provenance-index** must include an entry for `arkansas-river-basin-region`.  
- This local `*.prov-ref.json` file must be **derivable** from that global index and canonical PROV-O logs.  
- If the canonical provenance path or CARE fields change, this ref must be updated to match.

---

## 🧪 Validation & CI/CD

This directory is protected by CI to maintain **consistency** and **safety**.

### Schema & Shape Checks

- `*.prov-ref.json` must validate against a region provenance ref schema (defined under the global region provenance registry).  
- Required fields (`region_slug`, `dataset_id`, `canonical_provenance_paths`, CARE fields) must be present and typed correctly.

### Cross-Link Validation

CI must verify that:

- Each `canonical_provenance_paths` entry points to an existing canonical PROV-O JSON-LD file.  
- `region_slug` matches `arkansas-river-basin-region`.  
- `dataset_id` matches a STAC Item ID under:  
  `docs/analyses/archaeology/datasets/cultural-landscapes/regions/stac/items/`.  
- CARE fields match those in canonical provenance and metadata.

### CARE & Governance Validation

- No ref file may:

  - Downgrade sensitivity or visibility fields relative to canonical logs.  
  - Introduce disagreement about review status.

Indicative CI workflows:

- `archaeology-provenance-validate.yml`  
- `region-provenance-registry-validate.yml`  
- `metadata-validate.yml`  
- `faircare-audit.yml`

CI must **block**:

- Any ref file pointing at missing or renamed canonical provenance logs.  
- Any CARE/sensitivity mismatch relative to canonical sources.  
- Any new ref file for which no region + provenance registry entry exists.

---

## 🧠 Graph, Story Node & Focus Mode Integration

### Knowledge Graph (Neo4j)

Graph loaders will typically:

- Use the **global** region provenance registry and canonical PROV-O logs as their primary source.  
- Optionally consult local ref files like `arkansas-river-basin-region-v1.prov-ref.json` for:

  - Quick discovery of canonical paths.  
  - Caching of review dates and sensitivity.

### Story Nodes

Story Nodes and region-centric UIs can:

- Read this ref to quickly:

  - Attach provenance chips (e.g., “FAIR+CARE + Tribal Review · 2025-11-17”).  
  - Link out to full provenance views when requested.

Ref files allow Story Nodes to remain **lightweight** and **region-focused** while relying on canonical logs in deeper provenance views.

### Focus Mode v2/v3

Focus Mode uses refs to:

- Quickly resolve which canonical provenance log(s) back each regional overlay.  
- Enforce CARE visibility rules when rendering the Arkansas River Basin region in map panels.  
- Provide “Why am I seeing this?” explanations driven by canonical provenance.

---

## 🧭 Authoring & Maintenance Workflow

When adding or updating provenance for the Arkansas River Basin region:

1. **Update Canonical Provenance**
   - Edit or add PROV-O JSON-LD under:  
     `docs/analyses/archaeology/datasets/cultural-landscapes/provenance/arkansas-river-basin-region-*.json`

2. **Update Global Region Provenance Registry**
   - Adjust `region-provenance-index.v1.json` to reflect new or updated provenance docs.

3. **Update Region Metadata**
   - Ensure per-region metadata JSON-LD and global registry entries reference the correct provenance (`kfm:provenance_ref`).

4. **Update Local Ref JSON**
   - Edit `arkansas-river-basin-region-v1.prov-ref.json` (or bump version) to:
     - List correct `canonical_provenance_paths`.  
     - Update CARE fields and `last_review_date` as needed.

5. **Run Local Validation**
   - Use repo tooling (e.g., `make validate-region-arkansas-provenance-refs`) to run schema and cross-link checks.

6. **Submit PR & Address CI/Governance Feedback**
   - CI will enforce schema, linkage, and CARE/sovereignty consistency before merge.

---

## 🕰️ Version History

| Version  | Date       | Author                                      | Summary                                                                 |
|----------|------------|---------------------------------------------|-------------------------------------------------------------------------|
| v11.2.3  | 2025-12-02 | Cultural Landscape WG · FAIR+CARE Council   | Created Arkansas River Basin region-local provenance ref layout; defined ref JSON contract, CARE/sovereignty safeguards, and CI linkage to global provenance and registries; aligned with KFM-MDP v11.2.2. |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — CC-BY 4.0**  
FAIR+CARE Certified · MCP-DL v6.3 · KFM-MDP v11.2.2 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[⬅ Back to Arkansas River Basin Region](../README.md) · [⬅ Back to Arkansas River Basin Region Metadata](../metadata/README.md) · [⬅ Back to Global Region Provenance Registry](../../provenance/README.md)

</div>