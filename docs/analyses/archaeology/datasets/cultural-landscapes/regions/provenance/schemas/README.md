---
title: "🧩 KFM v11.2.3 — Cultural Landscape Region Provenance Schemas (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/datasets/cultural-landscapes/regions/provenance/schemas/README.md"
version: "v11.2.3"
last_updated: "2025-12-02"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Biannual · Cultural Landscape Working Group · FAIR+CARE Council · Metadata Standards Subcommittee"
content_stability: "stable"
backward_compatibility: "v10.4.0 → v11.2.3 region-provenance-schema-contract compatible"

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
doc_kind: "Region Provenance Schemas"
intent: "cultural-landscape-region-provenance-schemas"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Compliant"
---

<div align="center">

# 🧩 **KFM — Cultural Landscape Region Provenance Schemas**  
`docs/analyses/archaeology/datasets/cultural-landscapes/regions/provenance/schemas/README.md`

**Purpose:**  
Define and govern the **JSON schema layer** for all **region-level provenance artifacts** in KFM, including:

- Region provenance **index registry** files  
- Region provenance **coverage** summaries  
- Region-level **provenance ref** JSON files  

These schemas are the authoritative contracts used by **CI**, **ETL**, **graph loaders**, **Story Nodes**, and **Focus Mode** when working with cultural landscape region provenance.

</div>

---

## 📘 Overview

This directory holds the schemas that all region provenance artifacts must validate against:

- **Index schema** — structure of `region-provenance-index.v1.json`  
- **Coverage schema** — structure of `region-provenance-coverage.v1.json`  
- **Ref schema** — structure of `*.prov-ref.json` files under `regions/provenance/refs/` and per-region `provenance/` folders  

These schemas ensure that:

- All region provenance mappings are **machine-valid**, **graph-safe**, and **FAIR+CARE-aligned**  
- Index and ref files can be trusted as routing tables into canonical PROV-O logs  
- No schema-less or ad-hoc provenance mappings enter the KFM monorepo

Conceptual overviews:

- Region provenance root: `../README.md`  
- Provenance refs: `../refs/README.md`  
- Provenance index registry: `../registry/README.md`

---

## 🗂️ Directory Layout

~~~text
docs/analyses/archaeology/datasets/cultural-landscapes/regions/provenance/schemas/
├── 📄 README.md                                   # This file (schema contracts)
│
├── 🧩 region-provenance-index.schema.v1.json      # Schema for region-provenance-index.v1.json
├── 🧩 region-provenance-coverage.schema.v1.json   # Schema for region-provenance-coverage.v1.json
└── 🧩 region-provenance-ref.schema.v1.json        # Schema for *.prov-ref.json (region provenance ref files)
~~~

**Directory contract:**

- All files here are **governed schemas**; changes require FAIR+CARE + provenance/metadata governance approval.  
- Schema filenames must encode:
  - A descriptive slug (`region-provenance-index`, `region-provenance-ref`, etc.)  
  - The word `schema`  
  - A semantic version (`v1`, `v2`, …).  
- CI must reference these schemas explicitly when validating provenance index, coverage, and ref files.

---

## 🧾 Index Schema — `region-provenance-index.schema.v1.json`

This schema defines the shape of:

- `docs/analyses/archaeology/datasets/cultural-landscapes/regions/provenance/registry/region-provenance-index.v1.json`

### Required Concepts

Per region entry, the schema must validate:

- `region_slug`  
  - String; must match region directory name (e.g., `"flint-hills-region"`, `"arkansas-river-basin-region"`).  

- `region_dataset_ids`  
  - Array of string dataset IDs (typically STAC Item IDs for region geometries).  

- `provenance_docs`  
  - Array of string paths/URIs to canonical PROV-O JSON-LD under  
    `docs/analyses/archaeology/datasets/cultural-landscapes/provenance/`.

- `care` object:
  - `sensitivity` — `"generalized"` or `"restricted-generalized"` (for public artifacts).  
  - `review` — `"faircare"`, `"tribal"`, or combined string (e.g., `"faircare+tribal"`).  
  - `visibility_rules` — `"polygon-generalized"`, `"h3-only"`, `"no-exact-boundaries"`, or governed combination.

- `temporal` object:
  - `culture_phases` — array of KFM archaeology ontology phase labels.

Recommended optional fields:

- `status` — `"active"`, `"deprecated"`, `"internal-only"`, `"draft"`.  
- `last_review_date` — ISO8601 date string.  
- `notes` — short free-text notes.

### Illustrative Snippet (Non-Canonical)

~~~json
{
  "type": "object",
  "properties": {
    "regions": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["region_slug", "region_dataset_ids", "provenance_docs", "care", "temporal"],
        "properties": {
          "region_slug": { "type": "string" },
          "region_dataset_ids": {
            "type": "array",
            "items": { "type": "string" }
          },
          "provenance_docs": {
            "type": "array",
            "items": { "type": "string" }
          },
          "care": {
            "type": "object",
            "required": ["sensitivity", "review", "visibility_rules"],
            "properties": {
              "sensitivity": { "type": "string" },
              "review": { "type": "string" },
              "visibility_rules": { "type": "string" }
            }
          },
          "temporal": {
            "type": "object",
            "properties": {
              "culture_phases": {
                "type": "array",
                "items": { "type": "string" }
              }
            }
          }
        }
      }
    }
  }
}
~~~

> Exact rules live in `region-provenance-index.schema.v1.json` and must be treated as authoritative.

---

## 📊 Coverage Schema — `region-provenance-coverage.schema.v1.json`

This schema defines the shape of:

- `docs/analyses/archaeology/datasets/cultural-landscapes/regions/provenance/registry/region-provenance-coverage.v1.json`

Coverage files summarize registry contents for dashboards, audits, and automated checks.

### Typical Content

- `summary.total_regions` — integer  
- `summary.by_status` — object keyed by status with integer counts  
- `summary.by_sensitivity` — object keyed by CARE sensitivity with integer counts  
- Optional additional groupings (e.g., by culture phase, by region kind via metadata linkage)

Illustrative pattern:

~~~json
{
  "type": "object",
  "required": ["summary"],
  "properties": {
    "summary": {
      "type": "object",
      "required": ["total_regions"],
      "properties": {
        "total_regions": { "type": "integer" },
        "by_status": {
          "type": "object",
          "additionalProperties": { "type": "integer" }
        },
        "by_sensitivity": {
          "type": "object",
          "additionalProperties": { "type": "integer" }
        }
      }
    }
  }
}
~~~

Coverage files must always be **derived** from the index + canonical sources and **never contradict** them.

---

## 🧬 Ref Schema — `region-provenance-ref.schema.v1.json`

This schema defines the shape of all region provenance ref files:

- Global refs under:  
  `docs/analyses/archaeology/datasets/cultural-landscapes/regions/provenance/refs/*.prov-ref.json`
- Region-local refs under:  
  `docs/analyses/archaeology/datasets/cultural-landscapes/regions/<region-slug>/provenance/<region-slug>-v*.prov-ref.json`

### Required Fields

Every ref file must include:

- `region_slug`  
- `dataset_id`  
- `canonical_provenance_paths` — array of string paths to PROV-O JSON-LD.  
- `care:sensitivity`  
- `care:review`  
- `care:visibility_rules`

Recommended additional fields:

- `last_review_date` — ISO8601 date string.  
- `status` — `"active"`, `"deprecated"`, `"internal-only"`, `"draft"`.

### Illustrative Snippet (Non-Canonical)

~~~json
{
  "type": "object",
  "required": [
    "region_slug",
    "dataset_id",
    "canonical_provenance_paths",
    "care:sensitivity",
    "care:review",
    "care:visibility_rules"
  ],
  "properties": {
    "region_slug": { "type": "string" },
    "dataset_id": { "type": "string" },
    "canonical_provenance_paths": {
      "type": "array",
      "items": { "type": "string" }
    },
    "care:sensitivity": { "type": "string" },
    "care:review": { "type": "string" },
    "care:visibility_rules": { "type": "string" },
    "last_review_date": { "type": "string", "format": "date-time" },
    "status": { "type": "string" }
  }
}
~~~

Ref schema ensures that:

- All ref files have **minimal, consistent structure**.  
- CARE fields cannot be omitted in production ref files.

---

## ⚖ FAIR+CARE & Sovereignty in Schemas

All provenance schemas must:

- Require CARE fields wherever provenance is exposed at registry/ref level.  
- Prohibit schemas that allow provenance mappings without CARE metadata.  
- Support explicit representation of review processes and sovereignty-sensitive visibility rules.

These schemas **must not**:

- Remove CARE requirements for production artifacts.  
- Enable provenance mappings that lack clear STAC/metadata/provenance linkage.

Any schema change that touches CARE fields or visibility policies is a **governance event**.

---

## 🔗 Integration with CI, ETL, and Graph

These schemas underpin:

- **CI pipelines**:

  - `archaeology-provenance-validate.yml`  
  - `region-provenance-registry-validate.yml`  
  - `metadata-validate.yml`  
  - `faircare-audit.yml`

- **ETL & graph loaders**:

  - To safely look up which PROV-O logs attach to which region nodes.  
  - To enforce consistent CARE and temporal behavior.

- **Story Nodes & Focus Mode**:

  - To confidently query region provenance refs and index entries for:
    - “Why am I seeing this?” panels  
    - Provenance chips and CARE badges  

If a provenance artifact fails schema validation here, it must **not** be ingested or used downstream.

---

## 🧭 Authoring & Maintenance Workflow for Schemas

When updating or adding schemas in this directory:

1. **Design Change & Rationale**
   - Document why new fields, constraints, or versions are needed.  

2. **Edit/Add Schema Files**
   - Create or modify `region-provenance-*.schema.vX.json`.  
   - Maintain older versions if backward compatibility is required.

3. **Update Documentation**
   - Reflect changes in this `README.md`.  
   - Update `../registry/README.md` and `../refs/README.md` if semantics changed.

4. **Wire Into CI**
   - Ensure CI workflows reference the new or updated schema versions.  
   - Add/update fixtures and tests for index, coverage, and ref files.

5. **Governance Review**
   - FAIR+CARE Council, Metadata Standards Subcommittee, and Provenance/Lineage maintainers review the change.  
   - Confirm no weakening of CARE, sovereignty, or provenance integrity.

6. **Merge & Monitor**
   - After merge, monitor CI and downstream systems for validation/integration issues.

---

## 🕰️ Version History

| Version  | Date       | Author                                      | Summary                                                                 |
|----------|------------|---------------------------------------------|-------------------------------------------------------------------------|
| v11.2.3  | 2025-12-02 | Cultural Landscape WG · Metadata Subcommittee · FAIR+CARE Council | Established schema layout and contracts for region provenance index, coverage, and ref files; aligned with global provenance, STAC, metadata, and KFM-MDP v11.2.2. |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — CC-BY 4.0**  
FAIR+CARE Certified · MCP-DL v6.3 · KFM-MDP v11.2.2 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[⬅ Back to Region Provenance Registry](../README.md) · [⬅ Back to Region Provenance Index Registry](../registry/README.md) · [⬅ Back to Cultural Landscape Regions](../../README.md)

</div>
