---
title: "🧩 KFM v11.2.3 — Cultural Landscape Region Metadata Schemas (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/datasets/cultural-landscapes/regions/metadata/schemas/README.md"
version: "v11.2.3"
last_updated: "2025-12-02"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Biannual · Cultural Landscape Working Group · FAIR+CARE Council · Metadata Standards Subcommittee"
content_stability: "stable"
backward_compatibility: "v10.4.0 → v11.2.3 region-metadata-schema-contract compatible"

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
doc_kind: "Region Metadata Schemas"
intent: "cultural-landscape-region-metadata-schemas"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Compliant"
---

<div align="center">

# 🧩 **KFM — Cultural Landscape Region Metadata Schemas**  
`docs/analyses/archaeology/datasets/cultural-landscapes/regions/metadata/schemas/README.md`

**Purpose:**  
Define and govern the **JSON/JSON-LD schema layer** for all **cultural landscape region metadata artifacts** in KFM, including:

- Per-region DCAT/JSON-LD metadata records  
- Archaeology-specific metadata profiles  
- Region metadata **index** and **coverage** registry files  

These schemas are used by **CI**, **ETL**, **graph loaders**, **Story Nodes**, and **Focus Mode** to validate metadata for cultural landscape regions.

</div>

---

## 📘 Overview

This directory holds the **schema contracts** that every region metadata artifact must satisfy:

- **Core region metadata schema** (DCAT/JSON-LD + KFM core fields)  
- **Archaeology profile** (cultural phases, region kinds, ontology links)  
- **Registry index schema** (per-region index entries)  
- **Coverage schema** (aggregated views over the registry)

These schemas ensure that:

- All region metadata is **machine-valid**, **graph-safe**, and **FAIR+CARE-aligned**  
- Index/coverage files can be used safely by automation, dashboards, and CI  
- No ad-hoc or schema-free metadata structures are allowed into the monorepo

Human-readable metadata overview for regions:

- `../README.md`  
Metadata index registry overview:

- `../registry/README.md`

---

## 🗂️ Directory Layout

~~~text
docs/analyses/archaeology/datasets/cultural-landscapes/regions/metadata/schemas/
├── 📄 README.md                                   # This file (schemas standard & contracts)
│
├── 🧩 region-metadata.schema.v1.json              # Core region metadata schema (DCAT + KFM core)
├── 🧩 region-metadata-profile-archaeology.v1.json # Archaeology-specific metadata profile
│
├── 🧩 region-metadata-index.schema.v1.json        # Schema for regions-metadata-index.v1.json
└── 🧩 region-metadata-coverage.schema.v1.json     # Schema for regions-metadata-coverage.v1.json (optional summary)
~~~

**Directory contract:**

- All schemas in this directory are **governed artifacts**; changes require FAIR+CARE + metadata governance review.  
- Schema filenames must include:
  - A descriptive slug (e.g., `region-metadata-index`)  
  - A `schema` marker  
  - A semantic version (`v1`, `v2`, …).  
- CI must reference these schemas explicitly when validating region metadata, registries, and coverage.

---

## 📦 Core Schema: `region-metadata.schema.v1.json`

This schema defines the **base shape** for all **per-region DCAT/JSON-LD metadata records**, such as:

- `dcat-flint-hills-region-v1.jsonld`  
- `dcat-arkansas-river-basin-region-v1.jsonld`  

### Required High-Level Concepts

The core schema must enforce presence and basic typing for:

- **Identification**
  - `@id` — Stable URI/URN  
  - `dct:title` — Human-readable region title  
  - `kfm:region_slug` — Slug (e.g., `"flint-hills-region"`)  
  - `kfm:region_kind` — Array of controlled string values  

- **Descriptive Metadata**
  - `dct:description`  
  - `dcat:keyword` (array of strings)  
  - `dct:license`  

- **Temporal Coverage**
  - `dct:temporal` block (OWL-Time compatible)  

- **CARE Block**
  - `care:sensitivity`  
  - `care:review`  
  - `care:notes`  
  - `care:visibility_rules`  

- **Linkage Fields**
  - `kfm:stac_collection_id`  
  - `kfm:stac_item_ids` (optional array)  
  - `kfm:provenance_ref` (one or more canonical PROV-O logs)

### Example (Illustrative Only)

~~~json
{
  "type": "object",
  "required": ["@id", "dct:title", "kfm:region_slug", "kfm:region_kind"],
  "properties": {
    "@id": { "type": "string", "format": "uri" },
    "dct:title": { "type": "string" },
    "kfm:region_slug": { "type": "string" },
    "kfm:region_kind": {
      "type": "array",
      "items": { "type": "string" }
    }
  }
}
~~~

> Exact schema lives in `region-metadata.schema.v1.json` and must be treated as the authority.

---

## 🧭 Archaeology Profile: `region-metadata-profile-archaeology.v1.json`

This profile extends the core schema with **archaeology-specific** constraints:

### Additional Required/Constrained Fields

- `temporal` / `dct:temporal`:
  - Must include KFM archaeology ontology phases in `kfm:culture_phase` or similar.  
  - May restrict format of time intervals (e.g., start/end dates or period URIs).

- `kfm:region_kind`:
  - Values constrained to controlled vocabulary:
    - `"eco-cultural"`  
    - `"drainage"`  
    - `"territorial-generalized"`  
    - (Others as defined in KFM ontology)

- Ontology Links (optional but strongly encouraged):
  - `kfm:eco_region_ref`  
  - `kfm:hydrological_unit_ref`  
  - `kfm:geologic_unit_ref`

### Role in CI

- Used in addition to `region-metadata.schema.v1.json` when validating:
  - `dcat-*-region-v*.jsonld` files  
- Ensures archaeological semantics are consistent and graph-ready.

---

## 🧾 Registry Index Schema: `region-metadata-index.schema.v1.json`

This schema defines the shape of:

- `docs/analyses/archaeology/datasets/cultural-landscapes/regions/metadata/registry/regions-metadata-index.v1.json`

### Core Fields per Region Entry

The index schema must validate:

- `region_slug` — string, matching directory and metadata naming.  
- `region_kind` — array of controlled values.  
- `metadata_path` — string path to per-region JSON-LD metadata.  
- `stac_collection_id` — string ID for STAC Collection.  
- `stac_item_ids` — array of STAC Item IDs (optional but recommended).  
- `provenance_refs` — array of strings pointing to PROV-O logs.  
- `care` object:
  - `sensitivity`  
  - `review`  
  - `visibility_rules`  
- `temporal` object:
  - `culture_phases` array.

### Example Entry Shape (Illustrative Only)

~~~json
{
  "region_slug": "flint-hills-region",
  "region_kind": ["eco-cultural"],
  "metadata_path": "docs/analyses/archaeology/datasets/cultural-landscapes/regions/flint-hills-region/metadata/dcat-flint-hills-region-v1.jsonld",
  "stac_collection_id": "kfm-arch-lands-flint-hills-region-v1",
  "stac_item_ids": ["kfm-arch-lands-flint-hills-region-v1"],
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
~~~

> Exact validation rules are encoded in `region-metadata-index.schema.v1.json`.

---

## 📊 Coverage Schema: `region-metadata-coverage.schema.v1.json`

This schema defines the shape of:

- `docs/analyses/archaeology/datasets/cultural-landscapes/regions/metadata/registry/regions-metadata-coverage.v1.json`

### Typical Structure

Coverage files provide summary statistics such as:

- Total number of regions  
- Counts grouped by:
  - `region_kind`  
  - `culture_phase`  
  - CARE sensitivity  

Illustrative pattern:

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

The coverage schema ensures:

- Stable structure for dashboards and automated checks.  
- That coverage files remain **derived** from index + metadata and **never contradict them**.

---

## ⚖ FAIR+CARE & Sovereignty in Schemas

All region metadata schemas must:

- Enforce the presence and type of **CARE fields** where required.  
- Avoid optionalizing critical governance fields (e.g., `care:sensitivity`) in ways that would allow non-compliant records.  
- Support explicit representation of **sovereignty-related references** where needed (e.g., `kfm:sovereignty_policy_ref`).

This directory **must not** include schemas that:

- Remove CARE requirements for production metadata.  
- Permit region metadata records without clear linkage to provenance or STAC.

Any change to CARE-related parts of these schemas is a **governance event**.

---

## 🔗 Integration with CI, ETL, and Graph

These schemas are used by:

- **CI pipelines**:
  - `metadata-validate.yml`  
  - `region-metadata-registry-validate.yml`  
- **ETL/graph loaders**:
  - To guarantee that ingested metadata conforms to expectations and can be mapped into Neo4j.  
- **Story Nodes / Focus Mode**:
  - To reliably query region metadata for:
    - Culture phases  
    - Region kinds  
    - CARE/sensitivity metadata  

If a metadata artifact fails schema validation here, it must **not** be ingested or used downstream.

---

## 🧭 Authoring & Maintenance Workflow for Schemas

When updating or adding schemas in this directory:

1. **Propose Schema Changes**
   - Describe the motivation (new fields, stricter constraints, new versions).  

2. **Update JSON Schema Files**
   - Add new `*.schema.vX.json` files or bump versions.  
   - Keep old versions available if backward compatibility is required.

3. **Update Documentation**
   - Reflect changes in this `README.md`.  
   - Update related READMEs (e.g., `../README.md`, `../registry/README.md`) if semantics changed.

4. **Wire into CI**
   - Ensure CI workflows reference the new schema versions.  
   - Add/update tests for sample metadata, index, and coverage artifacts.

5. **Governance Review**
   - FAIR+CARE Council and Metadata Standards Subcommittee review the schema change.  
   - Confirm no weakening of CARE, provenance, or ontology constraints.

6. **Merge & Monitor**
   - Once merged, monitor CI and downstream systems for validation or integration issues.

---

## 🕰️ Version History

| Version  | Date       | Author                                      | Summary                                                                 |
|----------|------------|---------------------------------------------|-------------------------------------------------------------------------|
| v11.2.3  | 2025-12-02 | Cultural Landscape WG · Metadata Subcommittee · FAIR+CARE Council | Established schema layout and contracts for cultural landscape region metadata, archaeology profile, index, and coverage; aligned with KFM-MDP v11.2.2 and region metadata/provenance/STAC standards. |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — CC-BY 4.0**  
FAIR+CARE Certified · MCP-DL v6.3 · KFM-MDP v11.2.2 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[⬅ Back to Region Metadata Registry](../README.md) · [⬅ Back to Region Metadata Index Registry](../registry/README.md) · [⬅ Back to Cultural Landscape Regions](../../README.md)

</div>
