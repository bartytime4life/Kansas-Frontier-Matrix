---
title: "🧭 KFM v11.2.4 — Geoethical Reflection Layer for Story Nodes"
path: "docs/frontend/story-nodes/geoethical-reflection/README.md"
version: "v11.2.4"
last_updated: "2025-12-05"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · FAIR+CARE Council · Tribal Sovereignty Board"
content_stability: "stable"
status: "Active / Enforced"

doc_kind: "Standard"
header_profile: "standard"
footer_profile: "standard"

scope:
  domain: "frontend/story-nodes"
  applies_to:
    - "story-nodes"
    - "focus-mode"
    - "geoethical-reflection-layer"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"
sensitivity: "General (non-sensitive; auto-mask rules apply)"
classification: "Public"
indigenous_rights_flag: true

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../releases/v11.2.4/sbom.spdx.json"
manifest_ref: "../../../releases/v11.2.4/manifest.zip"
telemetry_ref: "../../../releases/v11.2.4/geoethics-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/geoethics-v1.json"
governance_ref: "../../../standards/governance/ROOT-GOVERNANCE.md"

license: "Apache-2.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.4"
---

<div align="center">

# 🧭 KFM v11.2.4 — Geoethical Reflection Layer for Story Nodes  
`docs/frontend/story-nodes/geoethical-reflection/README.md`

**Purpose:**  
Define the canonical Geoethical Reflection Layer for KFM Story Nodes — schema, UI contract, and governance hooks — so every narrative surface in KFM exposes sovereignty, CARE, sensitive-site handling, and provenance in a consistent, machine-readable way.

</div>

---

## 📘 Overview

### 1. Why this layer exists

Kansas Frontier Matrix (KFM) operates over dense Indigenous, archaeological, and historic landscapes; many Story Nodes necessarily touch culturally sensitive places, oral histories, and restricted knowledge that must not be treated as generic “content”.  

The Geoethical Reflection Layer ensures that **every Story Node** can declare, in a structured and inspectable way:

- Sovereignty implications  
- CARE Principle applications  
- Sensitive-site policy declarations  
- Stakeholder review status and scope  
- PROV-O provenance and audit pointers  

These declarations are:

- **Mandatory in ETL** (absence fails validation)  
- **Visible in the UI** (MapLibre/Cesium sidebar + Focus Mode)  
- **Mapped into the graph** (`(:StoryNode)-[:HAS_GEOETHICS]->(:GeoEthicsBlock)`)  
- **Catalog-ready** via STAC/DCAT foreign members and PROV bundles  

### 2. Scope

This standard applies to:

- All KFM Story Nodes surfaced in Map, Timeline, or Focus Mode.  
- Any narrative that references Indigenous knowledge, archaeological sites, burials, sacred places, or other culturally sensitive content.  
- Any Story Node whose spatial footprint overlaps datasets classified as “Restricted / Tribal-only / Withheld” in KFM catalogs.  

The `kfm_geoethics` block is **required** in Story Node front-matter; it is treated as a first-class entity in ETL, STAC/DCAT metadata, and the Neo4j knowledge graph.

---

## 🗂️ Directory Layout

```text
📂 docs/frontend/story-nodes/geoethical-reflection/
├── 📄 README.md                     # 🧭 Geoethical Reflection Layer standard (this file)
├── 📂 schema/
│   └── 📄 kfm.storyNode.geoethics.v1.json
├── 📂 examples/
│   └── 📄 story-node-frontmatter.yaml
└── 📂 ui/
    └── 📄 GeoethicsPanel.tsx
```

This directory is **documentation-first**: JSON Schema, examples, and UI spec live here; production implementations under `src/` **must** stay in sync and reference this standard.  

---

## 🧭 Context

KFM’s operational pipeline is:

> Deterministic ETL → STAC/DCAT/PROV catalogs → Neo4j knowledge graph → API layer → React/MapLibre/Cesium frontend → Story Nodes → Focus Mode.

Within this pipeline:

- **ETL** attaches and validates `kfm_geoethics` alongside core Story Node metadata.  
- **STAC Items / DCAT Datasets** record geoethical access, masking, and provenance policies as foreign members / qualified relations.  
- **Neo4j** stores a dedicated `:GeoEthicsBlock` node connected to each `:StoryNode` (`(:StoryNode)-[:HAS_GEOETHICS]->(:GeoEthicsBlock)`), with nested structures for CARE, sensitive-site policies, and stakeholder review.  
- **APIs + Frontend** expose the block via a stable JSON contract (see `GeoethicsPanel` props below) for Story Node sidebars and Focus Mode views.  

---

## 🧱 Architecture

### 1. Geoethics Story Node schema (UI schema v1)

This JSON Schema is the **single source of truth** for the `kfm_geoethics` block. It is mirrored in:

- `docs/frontend/story-nodes/geoethical-reflection/schema/kfm.storyNode.geoethics.v1.json`  
- ETL validation (Story Node pipeline)  
- API response validation and frontend type generation  

```json
{
  "$id": "kfm.storyNode.geoethics.v1",
  "type": "object",
  "additionalProperties": false,
  "required": [
    "sovereignty_summary",
    "care_application",
    "sensitive_site_policy",
    "stakeholder_review"
  ],
  "properties": {
    "sovereignty_summary": {
      "type": "string",
      "description": "Plain-language summary of sovereignty implications, data governance, and consent considerations."
    },

    "care_application": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "collective_benefit",
        "authority_to_control",
        "responsibility",
        "ethics_notes"
      ],
      "properties": {
        "collective_benefit": { "type": "string" },
        "authority_to_control": { "type": "string" },
        "responsibility": { "type": "string" },
        "ethics_notes": { "type": "string" }
      }
    },

    "sensitive_site_policy": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "masking_rule",
        "h3_resolution_rule",
        "temporal_generalization",
        "access_label"
      ],
      "properties": {
        "masking_rule": {
          "type": "string",
          "enum": ["mask", "offset", "aggregate", "withhold"]
        },
        "h3_resolution_rule": { "type": "string" },
        "temporal_generalization": { "type": "string" },
        "access_label": {
          "type": "string",
          "enum": ["Open", "Restricted", "Tribal-only", "Withheld"]
        }
      }
    },

    "stakeholder_review": {
      "type": "object",
      "additionalProperties": false,
      "required": ["status", "reviewers", "last_reviewed", "scope"],
      "properties": {
        "status": {
          "type": "string",
          "enum": [
            "Not started",
            "In progress",
            "Approved",
            "Approved with conditions",
            "Revisions requested"
          ]
        },
        "reviewers": { "type": "array", "items": { "type": "string" } },
        "last_reviewed": { "type": "string", "format": "date" },
        "scope": { "type": "string" }
      }
    },

    "provenance_ref": { "type": "string" },
    "audit_trail_ref": { "type": "string" }
  }
}
```

> **Graph note:** `provenance_ref` should point to a PROV Entity or Bundle (e.g., `urn:kfm:prov:storynode:…`), while `audit_trail_ref` should point to an OpenLineage or equivalent run identifier for masking/generalization jobs.

### 2. UI component contract

The API delivers `kfm_geoethics` to the frontend as a JSON object matching this TypeScript signature. The same type should be used in React/MapLibre/Cesium Story Node components and in Focus Mode overlays.

```ts
type GeoethicsPanel = {
  sovereignty_summary: string;
  care_application: {
    collective_benefit: string;
    authority_to_control: string;
    responsibility: string;
    ethics_notes: string;
  };
  sensitive_site_policy: {
    masking_rule: "mask" | "offset" | "aggregate" | "withhold";
    h3_resolution_rule: string;
    temporal_generalization: string;
    access_label: "Open" | "Restricted" | "Tribal-only" | "Withheld";
  };
  stakeholder_review: {
    status:
      | "Not started"
      | "In progress"
      | "Approved"
      | "Approved with conditions"
      | "Revisions requested";
    reviewers: string[];
    last_reviewed: string; // ISO 8601 date (YYYY-MM-DD)
    scope: string;
  };
  provenance_ref?: string;
  audit_trail_ref?: string;
};
```

### 3. Implementation touchpoints (modules & files)

Expected module boundaries for the Geoethical Reflection Layer:

- **ETL**  
  - `src/pipelines/story_nodes/geoethics_etl.py`  
    - Validates `kfm_geoethics` via `schema/kfm.storyNode.geoethics.v1.json`.  
    - Fails the run if the block is missing or invalid.  

- **Catalog & metadata**  
  - `data/stac/story-nodes/*.json` — STAC Items with `properties.kfm_geoethics`.  
  - `data/dcat/story-nodes.ttl` — DCAT Datasets with qualified relations pointing to geoethics policies.  

- **Knowledge graph**  
  - `src/graph/schema/story_nodes/geoethics.cypher` — defines `(:StoryNode)-[:HAS_GEOETHICS]->(:GeoEthicsBlock)` plus nested nodes/props.  

- **API & frontend**  
  - `src/api/story_nodes/geoethics.ts` — exposes `kfm_geoethics` as `GeoethicsPanel`.  
  - `src/web/story-nodes/GeoethicsPanel.tsx` — production UI; the docs stub lives at `docs/frontend/story-nodes/geoethical-reflection/ui/GeoethicsPanel.tsx`.  

---

## 🧠 Story Node & Focus Mode Integration

### 1. Story Node sidebar

- The Geoethics panel appears as a **dedicated section** in the Story Node sidebar (MapLibre/Cesium views).  
- It surfaces:
  - `sovereignty_summary` as a short, high-signal explanation.  
  - CARE details in an expandable “CARE” block.  
  - Sensitive-site policy with explicit masking/generalization rules.  
  - Stakeholder review status, reviewers, and last review date.  

### 2. Focus Mode

Focus Mode uses the graph neighborhood around `:GeoEthicsBlock` to build a geoethical overlay:

- Highlights Story Node segments that draw on restricted or sovereignty-sensitive sources.  
- Shows when masking/aggregation has been applied and links to audit runs via `audit_trail_ref`.  
- Lets users follow provenance to upstream datasets (STAC Items, DCAT Datasets) and governance docs.  

The Geoethical Reflection Layer must be **read-only** in Focus Mode; edits happen via governed workflows (KFM governance + Tribal Sovereignty Board), not ad-hoc UI changes.

---

## 🧪 Validation & CI/CD

### 1. ETL & determinism

- The `kfm_geoethics` block **must exist** for all Story Nodes; absence or schema violation fails ETL validation.  
- Enum values, required fields, and ISO date formats are enforced via JSON Schema and pipeline tests.  
- All masking/generalization activities:
  - Emit PROV-O activities (`prov:Activity`) with links to affected Story Nodes and source datasets.  
  - Emit OpenLineage (or equivalent) runs referenced by `audit_trail_ref`.  

### 2. CI/CD checks

Add or extend CI jobs (e.g., `.github/workflows/kfm-ci.yml`) to include:  

- **Schema lint** — Validate `kfm.storyNode.geoethics.v1.json` and sample fixtures under `examples/`.  
- **Markdown lint** — Enforce KFM-MDP v11.2.4 headings, front-matter, and footer rules on this README.  
- **Graph contract tests** — Assert that `HAS_GEOETHICS` relationships exist for all Story Nodes in staging data.  
- **API contract tests** — Type-check `GeoethicsPanel` responses against the TypeScript type.  

Backlog items (Phase 1):

- Wire geoethics schema validation into Story Node ETL.  
- Add a minimal OpenLineage integration for masking/generalization runs.  
- Add a regression test suite for common masking rules (`mask`, `offset`, `aggregate`, `withhold`).  

---

## 📦 Data & Metadata

### 1. Example Story Node front-matter block

```yaml
kfm_geoethics:
  sovereignty_summary: >
    Derived narrative intersects with Tribal oral history; spatial data generalized
    and reviewed under sovereignty protocols.

  care_application:
    collective_benefit: "Public education through responsibly abstracted landscape context."
    authority_to_control: "Access mediated through Sovereignty Board MOA."
    responsibility: "Shared stewardship with annual ethics audit."
    ethics_notes: "No site-level coordinates displayed."

  sensitive_site_policy:
    masking_rule: "aggregate"
    h3_resolution_rule: "≥ r7 for archaeological features"
    temporal_generalization: "±3 years"
    access_label: "Tribal-only"

  stakeholder_review:
    status: "Approved with conditions"
    reviewers:
      - "Tribal Sovereignty Board — Prairie Band"
      - "FAIR+CARE Council"
    last_reviewed: "2025-11-28"
    scope: "Narrative + spatial-generalization policy"

  provenance_ref: "urn:kfm:prov:storynode:xyz123"
  audit_trail_ref: "urn:kfm:openlineage:masking-run:2025-11-28T03:11Z"
```

This example should be mirrored under `docs/frontend/story-nodes/geoethical-reflection/examples/story-node-frontmatter.yaml` and used as a golden fixture in ETL tests.  

### 2. Required artifacts

For each Story Node collection or dataset, the following artifacts should be cataloged:

- STAC Item (with `properties.kfm_geoethics`) for spatial/temporal assets.  
- DCAT Dataset record with:
  - `dct:accessRights` / `dct:rights` derived from `access_label`.  
  - Qualified relations to geoethics policies and governance docs.  
- PROV Bundle describing masking/generalization and review activities referenced by `provenance_ref`.  

---

## 🌐 STAC, DCAT & PROV Alignment

To keep KFM FAIR, interoperable, and provenance-rich, the Geoethical Reflection Layer maps into existing standards as follows:  

- **STAC (1.0+/1.1)**  
  - `kfm_geoethics` stored as a foreign member under `properties.kfm_geoethics` on Story Node–related Items.  
  - `sensitive_site_policy.access_label` feeds into collection-level summaries and informs STAC API filters (e.g., “Tribal-only” assets).  

- **DCAT (2.0/3.0)**  
  - Sovereignty and sensitive-site info align with `dct:accessRights`, `dct:rights`, and versioning/series metadata for dataset revisions.  
  - `provenance_ref` links DCAT Datasets to generating Activities via `prov:wasGeneratedBy` and related qualified relations.  

- **PROV-O**  
  - Each masking/generalization run is a `prov:Activity` that:
    - `prov:used` one or more upstream spatial entities.  
    - `prov:generated` new generalized Story Node or geometry entities.  
    - Is linked to OpenLineage / audit logs via `audit_trail_ref`.  

This alignment ensures KFM’s geoethical metadata can be indexed, federated, and reasoned over alongside the rest of the data ecosystem.

---

## ⚖ FAIR+CARE & Governance

The Geoethical Reflection Layer operationalizes FAIR + CARE + Indigenous data sovereignty in KFM:  

- **FAIR**  
  - *Findable*: geoethics metadata searchable via STAC/DCAT and graph queries.  
  - *Accessible*: policies surfaced directly in the UI and APIs.  
  - *Interoperable*: mapped to STAC/DCAT/PROV.  
  - *Reusable*: clearly licensed and versioned.  

- **CARE & sovereignty**  
  - *Collective benefit*: `collective_benefit` documents who benefits and how.  
  - *Authority to control*: `authority_to_control` records Tribal or community governance.  
  - *Responsibility*: `responsibility` and `ethics_notes` make stewardship explicit.  
  - *Ethics*: masking/generalization rules protect sensitive sites and knowledge.  

All changes to this standard require review and approval by:

- FAIR+CARE Council  
- Tribal Sovereignty Board  
- KFM Governance maintainers  

---

## 📚 Reference Standards & Resources (Footer)

- [FAIR Principles](https://www.go-fair.org/fair-principles/)  
- [CARE Principles for Indigenous Data Governance](https://www.gida-global.org/care)  
- [CIDOC-CRM](https://www.cidoc-crm.org/) · [PROV-O](https://www.w3.org/TR/prov-o/) · [GeoSPARQL](https://www.ogc.org/standard/geosparql/)  
- [Data Access Labels Standard](../../../standards/governance/data-access-labels/README.md)  
- [KFM Governance Framework](../../../standards/governance/ROOT-GOVERNANCE.md)  
- [KFM Markdown Authoring Protocol — KFM-MDP v11.2.4](../../../standards/kfm_markdown_protocol_v11.2.4.md)  
- Archaeology, AI, and Open Technology in Kansas (context for sensitive-site handling)  
- [Frontend Story Node Guide](../README.md)  

---

## 🕰️ Version History

| Version | Date       | Status            | Notes                                                                 |
|--------:|------------|-------------------|-----------------------------------------------------------------------|
| v11.2.4 | 2025-12-05 | Active / Enforced | First LTS standardization of the Geoethical Reflection Layer for Story Nodes. |

Future revisions **must**:

- Preserve schema compatibility or provide explicit migration guidance.  
- Update STAC/DCAT/PROV mappings where needed.  
- Update CI/CD tests and fixtures alongside schema or contract changes.  

---

<div align="center">

🧭 **KFM v11.2.4 — Geoethical Reflection Layer for Story Nodes**  
Scientific Insight · FAIR+CARE Ethics · Sovereignty-First  

[📘 Docs Root](../../..) · [🧵 Story Node Frontend Guide](../README.md) · [⚖ Governance](../../../standards/governance/ROOT-GOVERNANCE.md)

</div>