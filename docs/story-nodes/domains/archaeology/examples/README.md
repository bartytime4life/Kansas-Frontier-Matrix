---
title: "🏺 Kansas Frontier Matrix — Archaeology Story Node Examples (KFM v11.2.6 · Governed · Public-Safe)"
path: "docs/story-nodes/domains/archaeology/examples/README.md"

version: "v11.2.6"
last_updated: "2025-12-12"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Annual · Archaeology Domain Board · FAIR+CARE Council"
content_stability: "stable"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

signature_ref: "../../../../../releases/v11.2.6/signature.sig"
attestation_ref: "../../../../../releases/v11.2.6/slsa-attestation.json"
sbom_ref: "../../../../../releases/v11.2.6/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.2.6/manifest.zip"

telemetry_ref: "../../../../../releases/v11.2.6/storynodes-archaeology-examples-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/storynodes-v11.json"
energy_schema: "../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
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
  - "docs/story-nodes/domains/archaeology/examples/README.md@v11.2.2"
  - "docs/story-nodes/domains/archaeology/examples/README.md@v11.2.1"

provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: true

json_schema_ref: "../../../../../schemas/json/kfm-markdown-protocol-v11.2.6.schema.json"
shape_schema_ref: "../../../../../schemas/shacl/kfm-markdown-protocol-v11.2.6-shape.ttl"
story_node_refs:
  - "docs/story-nodes/domains/archaeology/examples/protohistoric-wichita-site.json"
  - "docs/story-nodes/domains/archaeology/examples/fort-larned-geophysics.json"

immutability_status: "version-pinned"
doc_uuid: "urn:kfm:storynodes:archaeology:examples:v11.2.6"
semantic_document_id: "kfm-storynodes-archaeology-examples-v11.2.6"
event_source_id: "ledger:storynodes/archaeology/examples"
doc_integrity_checksum: "<sha256>"

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
accessibility_compliance: "WCAG 2.1 AA+"

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

# 🏺 **Kansas Frontier Matrix — Archaeology Story Node Examples (v11.2.6)**
`docs/story-nodes/domains/archaeology/examples/README.md`

**Purpose**  
Provide **curated, generalized, public-safe** example Story Nodes demonstrating correct structure, masking, metadata, relations, and narrative alignment for the archaeology domain under governed KFM v11.

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/MCP--DL-v6.3-blue" />
<img src="https://img.shields.io/badge/Story_Nodes-Examples-success" />
<img src="https://img.shields.io/badge/Classification-Public--Safe-informational" />
<img src="https://img.shields.io/badge/Status-Active_%2F_Enforced-brightgreen" />

</div>

---

## 📘 Overview

This directory contains **reference-quality archaeology Story Node fixtures** intended for:

- **Onboarding**: show authors what “correct + governed + public-safe” looks like.
- **Validation**: act as “living unit tests” for Story Node schema + domain validators.
- **Focus Mode**: demonstrate how examples can be summarized without inventing facts.

All examples here are required to be:

- **Generalized**: no precise coordinates, no site numbers, no restricted identifiers.
- **Governance-safe**: CARE + sovereignty aligned for culturally-linked contexts.
- **Schema-ready**: valid per Story Node v11 schema and archaeology domain constraints.
- **Public-safe by default**: this directory is publishable without special handling.

---

## 🗂️ Directory Layout

~~~text
📁 docs/
└── 📁 story-nodes/
    └── 📁 domains/
        └── 📁 archaeology/
            ├── 📄 README.md                          # Domain index (rules, templates, governance)
            ├── 📄 relation-patterns.md               # Allowed relation patterns for archaeology
            ├── 📁 templates/                         # Canonical templates for node authors
            │   └── 📄 README.md                      # Templates index (authoring patterns)
            └── 📁 examples/                          # Public-safe example fixtures
                ├── 📄 README.md                      # ← This index
                ├── 🧾 protohistoric-wichita-site.json# Example: generalized protohistoric narrative (public-safe)
                ├── 🧾 fort-larned-geophysics.json    # Example: non-invasive survey narrative (public-safe)
                └── 📁 ...                            # Additional public-safe examples (if/when added)
~~~

**Notes (normative)**

- Anything not safe for `classification: Generalized / Public-Safe` **MUST NOT** live here.
- New files added under `examples/` are treated as **contract fixtures** (they influence tooling + expectations).

---

## 🧭 Context

### 1. What qualifies as “public-safe” archaeology here

A Story Node in this directory MUST:

- use **generalized** spatial representation (region-level, administrative polygon, or explicitly masked geometry),
- omit **site numbers**, **permit IDs**, **unpublished field notes**, and **internal tracking identifiers**,
- avoid “re-identification” hints (directions, distances, landmark triangulation, unique descriptions).

### 2. What will never appear here

This directory MUST NOT contain:

- precise unmasked coordinates (lat/lon, UTM, parcel centroids, etc.),
- burial/sacred site descriptions or culturally restricted knowledge,
- internal excavation paperwork, raw notes, or unpublished interpretations,
- sensitive media that reveals restricted context.

If a sensitive scenario must be documented for testing, represent it **abstractly** (flags/labels only) with no sensitive payload.

---

## 🗺️ Diagrams

### Authoring → Validation → Publication (Conceptual)

~~~mermaid
flowchart LR
  A["Author writes Story Node JSON (public-safe)"] --> B["Schema validation (Story Node v11)"]
  B --> C["Domain rules validation (masking, relations, sovereignty)"]
  C --> D["Docs lint + metadata checks (KFM-MDP v11.2.6)"]
  D --> E["Merge + publish (public docs posture)"]
~~~

This diagram is intentionally simple (no HTML line breaks) to remain compatible with strict Mermaid parsers.

---

## 🧠 Story Node & Focus Mode Integration

Examples support Story Node tooling and Focus Mode without fabricating facts.

**Focus Mode MAY:**

- summarize what a given example demonstrates (structure, masking, relations),
- highlight which constraints are being illustrated,
- link to templates and relation patterns.

**Focus Mode MUST NOT:**

- treat fixtures as real sites, real investigations, or operational records,
- infer missing facts, add “color narrative,” or “improve realism,”
- output sensitive details not contained in the fixture.

Examples are fixtures: **reference structures**, not field truth.

---

## 🧪 Validation & CI/CD

### Expected checks

Every example Story Node SHOULD be validated by CI:

- **docs-lint**
  - validates this README’s front-matter, headings, links, and footer
- **storynodes-validate**
  - validates JSON against Story Node v11 schema
  - enforces archaeology domain constraints (relation patterns, masking rules)
- **sensitivity-check**
  - blocks merges if disallowed precision or identifiers appear
- **link validation**
  - if nodes reference STAC/DCAT assets, references must be well-formed and allowed

### What must fail CI (normative)

CI MUST fail if any example includes:

- coordinates with precision beyond the “public-safe” threshold,
- restricted site identifiers, permit numbers, or internal system IDs,
- content violating Indigenous data protection policy or CARE expectations,
- secrets/tokens/private URLs.

---

## 📦 Data & Metadata

### 1. Geometry masking conventions (recommended)

Use one of the following **public-safe** approaches:

- **Administrative mask**: county / region / watershed polygon
- **Coarse index** (only if policy allows): a coarse grid/H3 that cannot re-identify a site
- **Named region**: “Central Kansas river valley” without pinning

### 2. Minimal Story Node skeleton (sanitized, schematic)

Adapt field names to your Story Node v11 schema (this is intentionally schematic):

~~~json
{
  "schema_version": "v11",
  "node_kind": "archaeology.story_node",
  "id": "urn:kfm:story-node:archaeology:example:protohistoric:001",
  "classification": "Generalized / Public-Safe",
  "jurisdiction": "Kansas / United States",
  "care": {
    "label": "Culturally Sensitive · Indigenous-Linked",
    "indigenous_rights_flag": true
  },
  "spacetime": {
    "when": { "start": "1400-01-01", "end": "1700-12-31" },
    "geometry_precision": "generalized"
  },
  "summary": {
    "title": "Generalized protohistoric settlement context",
    "abstract": "Public-safe example fixture demonstrating masking, relations, and provenance."
  },
  "relations": [],
  "provenance": {
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

- reference **STAC Items** by stable, non-sensitive identifiers (or stub IDs),
- ensure referenced assets are:
  - public-safe (no restricted coordinates embedded in metadata),
  - licensed and attributable,
- align provenance roles:
  - Story Node = narrative/semantic layer,
  - STAC = geospatial asset layer,
  - PROV = lineage layer,
  - DCAT = catalog/distribution layer (if applicable).

If an asset cannot be represented safely, it belongs in an access-controlled store, not here.

---

## 🧱 Architecture

This examples directory is part of a governed domain contract:

- `templates/` defines recommended node structure
- `relation-patterns.md` defines allowable relations
- `examples/` demonstrates compliant patterns (public-safe fixtures)
- CI validators enforce the above consistently

Treat examples as **fixtures with governance weight**.

---

## ⚖ FAIR+CARE & Governance

Even “example content” is governance-sensitive in archaeology.

Therefore:

- updates SHOULD be reviewed by:
  - Archaeology Domain Board,
  - FAIR+CARE Council (when Indigenous-linked contexts are involved),
- generalization is not optional; it is the default,
- when in doubt: **reduce precision**, **remove identifiers**, **document abstractly**.

This directory is designed to remain safely publishable under:  
`classification: Generalized / Public-Safe`.

---

## 🕰️ Version History

| Version   | Date       | Author             | Summary                                                                                              |
|----------:|------------|--------------------|------------------------------------------------------------------------------------------------------|
| v11.2.6   | 2025-12-12 | `@kfm-archaeology`  | Updated to KFM-MDP v11.2.6; reordered sections (Overview → Directory Layout); tightened diagram safety; refreshed release/schema refs; normalized directory tree icons and alignment. |
| v11.2.2   | 2025-11-30 | `@kfm-archaeology`  | Initial governed archaeology example set; synced with templates and validation rules.               |
| v11.2.1   | 2025-11-29 | `@kfm-archaeology`  | Added initial generalized examples (protohistoric narrative + geophysics).                          |

---

<div align="center">

🏺 **Kansas Frontier Matrix — Archaeology Story Node Examples (v11.2.6)**  
Public-Safe Fixtures · Cultural Respect · Validator-Ready Examples

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/MCP--DL-v6.3-blue" />
<img src="https://img.shields.io/badge/FAIR%2BCARE-Aligned-gold" />
<img src="https://img.shields.io/badge/License-CC--BY%204.0-green" />

[⬅ Domain Index](../README.md) ·
[📄 Relation Patterns](../relation-patterns.md) ·
[📁 Templates](../templates/README.md) ·
[🧠 Story Nodes Index](../../../README.md) ·
[📄 Docs Templates Index](../../../../templates/README.md) ·
[📑 Markdown Protocol](../../../../standards/kfm_markdown_protocol_v11.2.6.md) ·
[📈 Telemetry Standard](../../../../standards/telemetry_standards.md) ·
[♿ UI Accessibility](../../../../standards/ui_accessibility.md) ·
[📘 Docs Home](../../../../README.md) ·
[📏 Standards Index](../../../../standards/README.md) ·
[⚖ Governance Charter](../../../../standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../../standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md) ·
[📚 Glossary](../../../../glossary.md)

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
MCP-DL v6.3 · KFM-MDP v11.2.6

</div>