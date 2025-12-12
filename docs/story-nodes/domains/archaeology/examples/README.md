---
title: "🏺 Kansas Frontier Matrix — Archaeology Story Node Examples (KFM v11.2.2 · Governed · Public-Safe)"
path: "docs/story-nodes/domains/archaeology/examples/README.md"

version: "v11.2.2"
last_updated: "2025-11-30"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Annual · Archaeology Domain Board · FAIR+CARE Council"
content_stability: "stable"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

signature_ref: "../../../../../releases/v11.2.2/signature.sig"
attestation_ref: "../../../../../releases/v11.2.2/slsa-attestation.json"
sbom_ref: "../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.2.2/manifest.zip"

telemetry_ref: "../../../../../releases/v11.2.2/storynodes-archaeology-examples-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/storynodes-v11.json"
energy_schema: "../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

status: "Active / Enforced"
doc_kind: "Example Collection"
intent: "kfm-archaeology-storynode-examples"
header_profile: "standard"
footer_profile: "standard"
diagram_profiles:
  - "mermaid-flowchart-v1"

scope:
  domain: "storynodes-archaeology-examples"
  applies_to:
    - "docs/story-nodes/domains/archaeology/examples/**"
    - "docs/story-nodes/domains/archaeology/templates/**"
    - "docs/story-nodes/domains/archaeology/relation-patterns.md"
    - "schemas/storynodes/**"
    - ".github/workflows/storynodes-validate.yml"
    - ".github/workflows/docs-lint.yml"

fair_category: "F1-A1-I1-R2"
care_label: "Culturally Sensitive · Indigenous-Linked"
sensitivity: "Public-safe archaeology examples; generalized geometry only; no sensitive coordinates; no restricted cultural knowledge; no site numbers"
sensitivity_level: "Low"
public_exposure_risk: "Low"
classification: "Generalized / Public-Safe"
jurisdiction: "Kansas / United States"
indigenous_rights_flag: true
data_steward: "Archaeology Domain Board · KFM FAIR+CARE Council"

ttl_policy: "36 months"
sunset_policy: "Superseded by v12 example set"

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "TechArticle"
  prov_o: "prov:Plan"
  owl_time: "ProperInterval"
  geosparql: "geo:FeatureCollection"

metadata_profiles:
  - "KFM Story Node v11"
  - "STAC 1.0.0 (references only)"
  - "DCAT 3.0 (references only)"
  - "PROV-O"
  - "FAIR+CARE"

provenance_chain:
  - "docs/story-nodes/domains/archaeology/examples/README.md@v11.2.1"
  - "docs/story-nodes/domains/archaeology/examples/README.md@v11.2.2"

provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: true

json_schema_ref: "../../../../../schemas/json/kfm-markdown-protocol-v11.2.2.schema.json"
shape_schema_ref: "../../../../../schemas/shacl/kfm-markdown-protocol-v11.2.2-shape.ttl"
story_node_refs:
  - "docs/story-nodes/domains/archaeology/examples/protohistoric-wichita-site.json"
  - "docs/story-nodes/domains/archaeology/examples/fort-larned-geophysics.json"

immutability_status: "version-pinned"
doc_uuid: "urn:kfm:storynodes:archaeology:examples:v11.2.2"
semantic_document_id: "kfm-storynodes-archaeology-examples"
event_source_id: "ledger:storynodes/archaeology/examples"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summary"
  - "timeline-generation"
  - "semantic-highlighting"
  - "a11y-adaptations"
  - "metadata-extraction"
ai_transform_prohibited:
  - "content-alteration"
  - "speculative-additions"
  - "unverified-architectural-claims"
  - "narrative-fabrication"
  - "governance-override"
transform_registry:
  allowed:
    - "summary"
    - "timeline-generation"
    - "semantic-highlighting"
    - "a11y-adaptations"
    - "metadata-extraction"
  prohibited:
    - "content-alteration"
    - "speculative-additions"
    - "unverified-architectural-claims"
    - "narrative-fabrication"
    - "governance-override"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"

heading_registry:
  approved_h2:
    - "📘 Overview"
    - "🗂️ Directory Layout"
    - "🧭 Context"
    - "🗺️ Diagrams"
    - "🧠 Story Node & Focus Mode Integration"
    - "🧪 Validation & CI/CD"
    - "📦 Data & Metadata"
    - "🌐 STAC, DCAT & PROV Alignment"
    - "🧱 Architecture"
    - "⚖ FAIR+CARE & Governance"
    - "🕰️ Version History"

test_profiles:
  - "markdown-lint"
  - "schema-lint"
  - "metadata-check"
  - "provenance-check"
  - "footer-check"
  - "accessibility-check"
  - "sensitivity-check"

ci_integration:
  workflow: ".github/workflows/docs-lint.yml"
  environment: "dev → staging → production"

branding_registry:
  standard: "Scientific Insight × FAIR+CARE Ethics × Sustainable Intelligence"
  archaeology: "Public-Safe Archaeology · Cultural Respect · Evidence-Led"
  graph: "Semantics × Provenance × Stewardship"

layout_profiles:
  - "immediate-one-branch-with-descriptions-and-emojis"
badge_profiles:
  - "root-centered-badge-row"

requires_purpose_block: true
requires_directory_layout_section: true
requires_version_history: true
requires_governance_links_in_footer: true

deprecated_fields:
  - "old_markdown_standard_v10.4"
---

<div align="center">

# 🏺 **KFM — Archaeology Story Node Examples (v11.2.2)**
`docs/story-nodes/domains/archaeology/examples/README.md`

**Purpose**  
Provide **curated, generalized, public-safe** example Story Nodes demonstrating correct structure, masking, metadata, relations, and narrative alignment for the archaeology domain under governed KFM v11.

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.2-purple" />
<img src="https://img.shields.io/badge/MCP--DL-v6.3-blue" />
<img src="https://img.shields.io/badge/Story_Nodes-Examples-success" />
<img src="https://img.shields.io/badge/Classification-Public--Safe-informational" />
<img src="https://img.shields.io/badge/Status-Active_%2F_Enforced-brightgreen" />

</div>

---

## 🗂️ Directory Layout

~~~text
📁 docs/
└── 📁 story-nodes/
    └── 📁 domains/
        └── 📁 archaeology/
            ├── 📄 README.md                              — Domain index (rules, templates, governance)
            ├── 📄 relation-patterns.md                   — Allowed relation patterns for archaeology
            ├── 📁 templates/                             — Canonical templates for node authors
            └── 📁 examples/
                ├── 📄 README.md                          — ← This index
                ├── 🏞️ protohistoric-wichita-site.json    — Generalized protohistoric narrative (public-safe)
                ├── 🧲 fort-larned-geophysics.json         — Non-invasive survey example (public-safe)
                └── 📂 ...                                 — Additional public-safe examples (if/when added)
~~~

**Notes**

- The examples directory is **public-facing by design**. Anything not safe for `classification: Public` does not belong here.
- Additions to this directory are treated as **contract updates** because they influence onboarding, tooling, and validator expectations.

---

## 📘 Overview

This directory contains **reference-quality example Story Nodes** for archaeology.

These examples are intended to be:

- **Generalized**: no precise coordinates; no site numbers; no restricted location hints.
- **Validator-ready**: schema compliant and consistent with domain templates.
- **Governance-safe**: reflects CARE and sovereignty expectations for culturally linked contexts.
- **Practical**: shows realistic narrative structure without leaking sensitive knowledge.

---

## 🧭 Context

### 1. What qualifies as “public-safe” archaeology here (normative)

A Story Node in this directory MUST:

- use **generalized** geometry (e.g., coarse polygon masks, region-level indicators),
- avoid publishing **site numbers**, **permit identifiers**, or **unpublished field notes**,
- avoid content that enables **re-identification** of restricted locations,
- remain valid for `classification: Generalized / Public-Safe`.

### 2. What will never appear here (normative)

This directory MUST NOT contain:

- precise, unprotected coordinates (lat/lon, UTM, parcel centroids, or equivalent),
- burial/sacred site descriptions or culturally restricted knowledge,
- internal excavation forms, raw notes, or unpublished interpretations,
- sensitive photos or media that expose restricted contexts.

If a “sensitive scenario” must be documented, it must be represented abstractly (flags/labels only), without the sensitive payload.

---

## 🗺️ Diagrams

### Authoring → Validation → Publication (Conceptual)

~~~mermaid
flowchart LR
  A["Author writes Story Node JSON<br/>(public-safe, generalized)"] --> B["Schema validation<br/>(Story Node v11)"]
  B --> C["Domain rules validation<br/>(relations, masking, sovereignty flags)"]
  C --> D["Docs lint + metadata checks<br/>(KFM-MDP v11.2.2)"]
  D --> E["Merge + publish docs<br/>(public docs posture)"]
~~~

---

## 🧠 Story Node & Focus Mode Integration

Examples support Story Node tooling and Focus Mode without fabricating facts:

- Focus Mode MAY:
  - summarize what a given example demonstrates (structure, masking, relations),
  - highlight how to adapt patterns for new, **public-safe** nodes.
- Focus Mode MUST NOT:
  - treat examples as real sites, real investigations, or operational records,
  - infer missing facts or add “color narrative” not contained in the fixture,
  - “improve” realism by adding sensitive details.

Examples are fixtures: **reference structures**, not field truth.

---

## 🧪 Validation & CI/CD

### 1. Required checks (expected)

Every example Story Node SHOULD be validated by CI:

- **docs-lint**
  - validates this README’s front-matter, headings, and footer links
- **storynodes-validate**
  - validates JSON against Story Node v11 schema
  - enforces archaeology domain constraints (relation patterns, masking rules)
- **sovereignty/CARE gate**
  - blocks merges if sensitive markers or restricted patterns appear
- **link validation**
  - if a node references STAC/DCAT assets, validate that references are well-formed and allowed

### 2. What should fail CI (normative)

CI MUST fail if any example includes:

- coordinates with precision beyond the allowed “public-safe” threshold,
- restricted site identifiers, permit numbers, or internal system IDs,
- content that violates indigenous protection policy or CARE expectations,
- secrets, tokens, or private URLs.

---

## 📦 Data & Metadata

### 1. Geometry masking conventions (recommended)

Use one of the following **public-safe** approaches:

- **administrative mask** (county / region / watershed polygon)
- **coarse index** (e.g., H3 at coarse resolution) *only if policy allows*
- **described region** (“Central Kansas river valley”, etc.) without pinpointing

### 2. Minimal Story Node skeleton (sanitized, schematic)

Adapt field names to your Story Node v11 schema (this is intentionally schematic):

~~~json
{
  "schema_version": "v11",
  "node_kind": "archaeology.story_node",
  "id": "kfm-arch-example-protohistoric-001",
  "classification": "Generalized / Public-Safe",
  "jurisdiction": "Kansas / United States",
  "care": {
    "label": "Culturally Sensitive · Indigenous-Linked",
    "indigenous_rights_flag": true
  },
  "spacetime": {
    "time_range": { "start": "1400-01-01", "end": "1700-12-31" },
    "geometry_precision": "generalized"
  },
  "summary": {
    "title": "Generalized protohistoric settlement context",
    "abstract": "Public-safe example narrative demonstrating masking, relations, and provenance."
  },
  "relations": [],
  "provenance": {
    "created_by": "@kfm-archaeology",
    "method": "example_fixture",
    "sources": []
  }
}
~~~

**Sanitization notes**

- IDs are example-only and MUST NOT map to real site registries.
- Geometry must remain generalized; do not include point coordinates.

---

## 🌐 STAC, DCAT & PROV Alignment

If an archaeology Story Node references assets (e.g., generalized survey rasters), examples SHOULD:

- reference **STAC Items** by stable, non-sensitive identifiers (or stub IDs)
- ensure assets are:
  - public-safe (no restricted coordinates embedded in metadata)
  - licensed and attributable
- align provenance:
  - Story Node = narrative/semantic layer
  - STAC = geospatial asset layer
  - PROV = lineage layer for processes/artifacts
  - DCAT = catalog/public distribution layer (if applicable)

If an asset cannot be represented safely, it belongs in an access-controlled internal store, not here.

---

## 🧱 Architecture

This examples directory is part of a governed domain contract:

- `templates/` defines recommended node structure
- `relation-patterns.md` defines allowable relations
- `examples/` demonstrates compliant patterns (public-safe fixtures)
- CI validators enforce the above consistently

Examples are the “living unit tests” for archaeology Story Node authoring rules.

---

## ⚖ FAIR+CARE & Governance

Even “example content” is governance-sensitive in archaeology.

Therefore:

- Every update MUST be reviewed by:
  - Archaeology Domain Board
  - FAIR+CARE Council (when indigenous-linked contexts appear)
- Generalization is not optional; it is the default.
- When in doubt: **reduce precision**, **remove identifiers**, and **document abstractly**.

This directory is designed to remain safely publishable under:
`classification: Generalized / Public-Safe`.

---

## 🕰️ Version History

| Version | Date       | Author             | Summary                                                                 |
|--------:|------------|--------------------|-------------------------------------------------------------------------|
| v11.2.2 | 2025-11-30 | `@kfm-archaeology`  | Initial governed archaeology example set; synced with templates and validation rules. |
| v11.2.1 | 2025-11-29 | `@kfm-archaeology`  | Added initial generalized examples (protohistoric narrative + geophysics). |

---

<div align="center">

🏺 **KFM — Archaeology Story Node Examples (v11.2.2)**  
Public-Safe Fixtures · Cultural Respect · Validator-Ready Examples

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.2-purple" />
<img src="https://img.shields.io/badge/MCP--DL-v6.3-blue" />
<img src="https://img.shields.io/badge/FAIR%2BCARE-Aligned-gold" />
<img src="https://img.shields.io/badge/License-CC--BY%204.0-green" />

[⬅ Domain Index](../README.md) ·
[📄 Relation Patterns](../relation-patterns.md) ·
[📁 Templates](../templates/README.md) ·
[📘 Docs Home](../../../../README.md) ·
[📏 Standards Index](../../../../standards/README.md) ·
[⚖ Governance Charter](../../../../standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../../standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md) ·
[📚 Glossary](../../../../glossary.md)

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
MCP-DL v6.3 · KFM-MDP v11.2.2

</div>
