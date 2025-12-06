---
title: "🏛️ Kansas Frontier Matrix — Governance Release v10.4 (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/standards/governance/releases/kfm-governance-v10.4.md"
version: "v10.4.1"
last_updated: "2025-12-06"
release_stage: "Released / Immutable Governance Record"
lifecycle: "Release Record (Immutable)"
review_cycle: "Annual / FAIR+CARE Council"
content_stability: "stable"
commit_sha: "<latest-commit-hash>"

signature_ref: "releases/v10.4.1/signature.sig"
attestation_ref: "releases/v10.4.1/slsa-attestation.json"
sbom_ref: "releases/v10.4.0/sbom.spdx.json"
manifest_ref: "releases/v10.4.0/manifest.zip"
telemetry_ref: "releases/v10.4.0/focus-telemetry.json"
telemetry_schema: "schemas/telemetry/governance-release-v1.json"
energy_schema: "schemas/telemetry/energy-v2.json"
carbon_schema: "schemas/telemetry/carbon-v2.json"

governance_ref: "../ROOT-GOVERNANCE.md"
ethics_ref: "../../faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.4"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

status: "Active / Enforced"
doc_kind: "governance-release"
header_profile: "standard"
footer_profile: "standard"
diagram_profiles:
  - "mermaid-flowchart-v1"

scope:
  domain: "governance"
  applies_to:
    - "governance-releases"
    - "all-markdown"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"
sensitivity: "General (non-sensitive; auto-mask rules apply)"
sensitivity_level: "None"
public_exposure_risk: "Low"
classification: "Public"
jurisdiction: "Kansas / United States"
indigenous_rights_flag: false
data_steward: "KFM FAIR+CARE Council"
risk_category: "Low"
redaction_required: false

ttl_policy: "24 months"
sunset_policy: "Superseded by v10.5+ governance release"

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "TechArticle"
  prov_o: "prov:Plan"
  owl_time: "ProperInterval"
  geosparql: "geo:FeatureCollection"

metadata_profiles:
  - "STAC 1.0.0"
  - "DCAT 3.0"
  - "PROV-O"
  - "FAIR+CARE"

provenance_chain:
  - "docs/standards/governance/releases/kfm-governance-v10.4.md@v10.4.0"
  - "docs/standards/governance/releases/kfm-governance-v9.7.md@v9.7.0"
  - "docs/standards/markdown_rules.md@v10.0"
  - "docs/standards/markdown_rules.md@v10.4"

provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: true

json_schema_ref: "schemas/json/kfm-governance-release-v10.4.1.schema.json"
shape_schema_ref: "schemas/shacl/kfm-governance-release-v10.4.1-shape.ttl"

story_node_refs: []

immutability_status: "immutable"
doc_uuid: "urn:kfm:gov:release-v10.4.1"
semantic_document_id: "kfm-governance-release-v10.4.1"
event_source_id: "ledger:governance:release:10.4"
doc_integrity_checksum: "<sha256>"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summary"
  - "timeline-generation"
  - "semantic-highlighting"
  - "3d-context-render"
  - "a11y-adaptations"
  - "diagram-extraction"
  - "metadata-extraction"
ai_transform_prohibited:
  - "content-alteration"
  - "speculative-additions"
  - "unverified-architectural-claims"
  - "narrative-fabrication"
  - "governance-override"
  - "modification"
  - "reinterpretation"

transform_registry:
  allowed:
    - summary
    - timeline-generation
    - semantic-highlighting
    - 3d-context-render
    - a11y-adaptations
    - diagram-extraction
    - metadata-extraction
  prohibited:
    - content-alteration
    - speculative-additions
    - unverified-architectural-claims
    - narrative-fabrication
    - governance-override
    - modification
    - reinterpretation

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

heading_registry:
  approved_h2:
    - "📘 Overview"
    - "🗂️ Directory Layout"
    - "🧭 Context"
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
  - "footer-check"
  - "accessibility-check"
  - "diagram-check"
  - "metadata-check"
  - "provenance-check"

ci_integration:
  workflow: ".github/workflows/kfm-ci.yml"
  environment: "dev → staging → production"

branding_registry:
  standard: "Scientific Insight × FAIR+CARE Ethics × Sustainable Intelligence"
  architecture: "Designed for Longevity · Governed for Integrity"
  analysis: "Research-Driven · Evidence-Led · FAIR+CARE Grounded"
  data-spec: "Open Data × Responsible Stewardship"
  pipeline: "Deterministic Pipelines · Explainable AI · Open Provenance"
  telemetry: "Transparent Systems · Ethical Metrics · Sustainable Intelligence"
  graph: "Semantics × Provenance × Spatial Intelligence"

layout_profiles:
  - "immediate-one-branch-with-descriptions-and-emojis"

badge_profiles:
  - "root-centered-badge-row"

requires_purpose_block: true
requires_version_history: true
requires_directory_layout_section: true
requires_governance_links_in_footer: true

role: "governance"
lifecycle_stage: "active"

deprecated_fields:
  - "old_markdown_standard_v10.4"
---

<div align="center">

# 🏛️ **Kansas Frontier Matrix — Governance Release v10.4**  
`docs/standards/governance/releases/kfm-governance-v10.4.md`

**Purpose:**  
Formally adopt and enforce the **Kansas Frontier Matrix Markdown Structural & Formatting Rules v10.4** as binding governance for documentation at the time of release v10.4.  
This document records the FAIR+CARE Council’s governance actions, CI/CD enforcement decisions, and alignment with the **Root Governance Charter** and **Master Coder Protocol (MCP-DL v6.3)**.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP_v6.3-blue)](../../../README.md)  
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Certified-orange)](../../faircare.md)  
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../../../LICENSE)  
[![Status: Enforced](https://img.shields.io/badge/Status-Enforced-success)]()

</div>

---

## 📘 Overview

### Executive Summary

This governance release records the **official integration** of the **Markdown Structural & Formatting Rules v10.4** into the Kansas Frontier Matrix (KFM) governance system.

At release **v10.4**:

- The **Markdown rules v10.4** became the **authoritative documentation standard** for KFM.  
- CI/CD, FAIR+CARE validation, and governance ledgers were updated to enforce these rules.  
- All prior Markdown conventions and partial metadata patterns were **deprecated**.  

While KFM documentation has since advanced to **KFM-MDP v11.2.4**, this document is the **immutable governance record** for how v10.4 was governed and what rules it enforced at that time.

### Governance Outcomes for v10.4

For release v10.4, the FAIR+CARE Council and governance automation:

- **Adopted** Markdown Protocol v10.4 as mandatory for all docs.  
- **Deprecated** pre-10.4 patterns and incomplete metadata formats.  
- **Mandated** CI/CD enforcement of documentation standards.  
- **Activated** immutable governance tracking (UUIDs, checksums, ledger anchoring) for Markdown.  

All of these actions are binding for the v10.4 release and remain part of KFM’s governance lineage.

---

## 🗂️ Directory Layout

~~~text
📂 docs/
└── 📂 standards/
    ├── 📂 governance/
    │   ├── 📄 README.md                  # Governance & Ethical Oversight Framework
    │   ├── 📄 ROOT-GOVERNANCE.md         # Root Governance Charter (authoritative)
    │   └── 📂 releases/
    │       ├── 📄 README.md              # Governance Release Records Index
    │       └── 📄 kfm-governance-v10.4.md# Governance Release v10.4 (this document)
    └── 📄 markdown_rules.md              # Markdown Structural & Formatting Rules (v10.4 at time of release)
~~~

**Author rules:**

- This file **MUST** remain at `docs/standards/governance/releases/kfm-governance-v10.4.md`.  
- Any later governance release (e.g., v10.5, v11.x) must:
  - Use its own file (e.g., `kfm-governance-v10.5.md`).  
  - Reference this document in its `provenance_chain` where relevant.  
- This release document is **immutable** except for:
  - Error corrections / errata (which must be logged in the governance ledger and reflected in `version` + `provenance_chain`).  

---

## 🧭 Context

### Relationship to Root Charter & Markdown Standards

This release sits under:

- **Root Governance Charter:** `docs/standards/governance/ROOT-GOVERNANCE.md`  
- **Governance & Ethical Oversight Framework:** `docs/standards/governance/README.md`  
- **Markdown Structural & Formatting Rules:** `docs/standards/markdown_rules.md` (v10.4 at release time)

At v10.4, the Council:

- Elevated Markdown rules to **governance-backed policy**, not just style.  
- Required that all documentation changes be **schema-valid**, **governance-aware**, and **machine-extractable**.  
- Established Markdown rules as a **dependency** for Focus Mode, Story Nodes, STAC/DCAT exports, and provenance modeling.

### Scope of this Governance Release

This document governs:

- All **Markdown files** present in the repository as of the v10.4 release.  
- All **CI/CD workflows** enforcing v10.4 Markdown rules.  
- All **governance decisions** explicitly tied to documentation standards in v10.4.

It does **not** supersede newer standards (e.g., **KFM-MDP v11.2.4**). Instead, it provides the **historical governance snapshot** for v10.4.

---

## 🧠 Story Node & Focus Mode Integration

### Focus Mode Behavior

For this governance release document:

- **Allowed Focus Mode behaviors (via `ai_transform_permissions`):**
  - Summarize sections (e.g., “What changed at v10.4 governance-wise?”).  
  - Generate timelines of documentation governance (e.g., v9.7 → v10.0 → v10.4 → v11.x).  
  - Highlight specific governance actions affecting a given dataset/model.  
  - Extract metadata/diagram structure for visualization or accessibility adaptations.

- **Disallowed behaviors (via `ai_transform_prohibited`):**
  - Altering or paraphrasing normative policy text as if it were new policy.  
  - Speculating about unrecorded governance decisions.  
  - Overriding the meanings of “adopted,” “deprecated,” or “enforced.”  
  - Reinterpreting or weakening constraints defined in this document or in `markdown_rules.md@v10.4`.

### Story Node Patterns

Typical governance Story Nodes referencing this file:

~~~text
{
  "target": "kfm-governance-release-v10.4.1",
  "scope": {
    "kind": "release",
    "id": "v10.4.0"
  },
  "references": [
    "docs/standards/governance/releases/kfm-governance-v10.4.md",
    "docs/standards/markdown_rules.md",
    "reports/audit/governance-ledger.json"
  ]
}
~~~

These nodes enable Focus Mode to:

- Quickly explain what v10.4 changed in governance and documentation.  
- Link a dataset or model to the governance rules active when it was released.  

---

## 🧪 Validation & CI/CD

### Governance Actions (Binding & Immediate at v10.4)

At release v10.4, the FAIR+CARE Council and MCP-DL governance authority:

#### 1. Adopted KFM Markdown Protocol v10.4 as authoritative

All Markdown files were required to comply with the **KFM Markdown Protocol v10.4**, including:

- Extended YAML front-matter (30+ fields).  
- Standardized title and header blocks.  
- Mandatory sections and ordering (as defined in v10.4).  
- Ontology and STAC/DCAT alignment fields.  
- Focus Mode v2 and Story Node v3 hooks.  
- Ethics, CARE, and sensitivity fields.  
- Accessibility and machine-extractability requirements.  

#### 2. Deprecated pre-10.4 conventions

Non-compliant patterns (e.g., missing metadata, ad-hoc headings, outdated fencing practices, or non-standard diagrams) were:

- Marked as **deprecated**.  
- Subject to CI/CD rejection and governance remediation.  

#### 3. Mandated CI/CD enforcement

The following CI workflows became **non-optional gates** for documentation at v10.4:

- `docs-lint.yml`  
- `markdown-validate.yml`  
- `schema-check.yml`  
- `stac-validate.yml`  
- `faircare-validate.yml`  
- `mcp-lint.yml`  
- `ledger-validate.yml`  
- `accessibility-lint.yml`  

Failure of any of these resulted in blocked merges and governance review.

#### 4. Activated immutable governance tracking for docs

For Markdown files:

- Each document received a `doc_uuid`.  
- Each change became a governance event (`event_source_id`).  
- Each version had a `doc_integrity_checksum`.  
- Entries were recorded in the governance ledger.

### Governance Release Flow at v10.4

~~~mermaid
flowchart LR
  A["Docs & Pipelines Updated for v10.4"] --> B["Markdown v10.4 Rules Applied"]
  B --> C["CI/CD Validation (lint, schema, FAIR+CARE, STAC/DCAT)"]
  C --> D{"All Checks Pass?"}
  D -->|No| E["Block Release → Governance Remediation"]
  D -->|Yes| F["Record Governance Release v10.4"]
  F --> G["Update Governance Ledger & Telemetry"]
  G --> H["Publish Release Manifests & Docs"]
~~~

---

## 📦 Data & Metadata

### Integrated Rule Block (Summary at v10.4)

The **Markdown Protocol v10.4** (as referenced by this governance release) included, at minimum:

1. Extended YAML front-matter (30+ fields).  
2. Strict centered title block rules.  
3. Mandatory section ordering for key doc types.  
4. Ontology alignment mapping fields.  
5. Required STAC/DCAT metadata blocks.  
6. Focus Mode v2 narrative and explainability hooks.  
7. Story Node v3 integration fields.  
8. Sensitivity, exposure, and ethics declarations.  
9. Version lineage and immutable governance chain.  
10. WCAG 2.1 AA accessibility conformance.  
11. Reproducibility environment metadata.  
12. AI transform restrictions and authorship transparency.  
13. Document TTL and sunset policies.  
14. Event sourcing and ledger anchoring fields.  
15. Sustainability metrics hooks (energy/carbon telemetry).  

The **full normative text** of these rules is recorded in:

- `docs/standards/markdown_rules.md@v10.4`

This governance release **incorporates that document by reference** and does not override it.

### Crosswalk to JSON Artifacts

Governance decisions and CI/CD results for v10.4 were reflected in:

- `reports/audit/governance-ledger.json` — decisions, approvals, rejections.  
- `reports/fair/faircare_summary.json` — FAIR+CARE validations.  
- `reports/audit/release-manifest-log.json` — manifests and checksum records.  
- `releases/v10.4.0/manifest.zip` — packaged docs and data for the release.  

This document links narrative governance to those machine-readable artifacts.

---

## 🌐 STAC, DCAT & PROV Alignment

### DCAT View

For the v10.4 governance release:

- This document is modeled as a `dcat:Dataset` or `dcat:CatalogRecord` in the KFM standards catalog.  
- Key DCAT properties:
  - `dct:title` → this document’s `title`.  
  - `dct:description` → Purpose + Overview sections.  
  - `dct:license` → `CC-BY 4.0`.  
  - `dct:modified` → `last_updated`.  
  - `dct:identifier` → `doc_uuid` / `semantic_document_id`.  
  - `dcat:distribution` → references to Markdown/HTML versions and JSON governance artifacts.

### STAC View

In a `kfm-releases` or `kfm-governance` STAC Collection:

- Release v10.4 appears as a STAC Item:
  - `id` = `"v10.4.0"`.  
  - `properties.datetime` = release cut timestamp.  
  - Governance assets:
    - `assets.governance-release` → this document.  
    - `assets.governance-ledger` → release-specific ledger extracts.  
    - `assets.faircare-summary` → FAIR+CARE JSON.

### PROV View

- This governance release is a `prov:Plan` (this document) and a `prov:Entity` instance (v10.4.1) that:
  - `prov:wasGeneratedBy` a release governance activity (e.g., `ex:governance_release_v10_4`).  
  - `prov:wasDerivedFrom` earlier governance releases (e.g., v9.7) and Markdown standards (v10.0, v10.4).  

- Activities:
  - Use:
    - `markdown_rules.md@v10.4`.  
    - Governance ledger entries leading up to v10.4.  
    - CI/CD result entities.  

- Agents:
  - FAIR+CARE Council, Technical Standards Committee, and other bodies defined in the Root Charter.

---

## 🧱 Architecture

From the perspective of the KFM architecture, v10.4 governance impacted:

1. **ETL / Validation Pipelines**  
   - Documentation validation became a hard gate for data and model deployments.  
   - Pipelines were updated to:
     - Emit richer telemetry on documentation quality.  
     - Fail builds when Markdown rules were violated.  

2. **Knowledge Graph (Neo4j)**  
   - Documentation and governance entities (docs, decisions, policies, releases) were modeled as nodes and relationships.  
   - Queries such as “Which docs were governed by v10.4 rules?” became answerable via the graph.

3. **API Layer**  
   - APIs could surface governance status for:
     - Releases (e.g., v10.4).  
     - Specific documents or data products.  
   - Clients could request “governance view as of v10.4” for regulatory or research purposes.

4. **Web / Focus Mode**  
   - UI and Focus Mode overlays:
     - Displayed that Markdown rules v10.4 were in effect for the release.  
     - Explained governance reasons when docs or datasets were blocked or restricted at that time.

This document is the architectural “anchor” that explains **why** those behaviors are correct for any asset governed under v10.4.

---

## ⚖ FAIR+CARE & Governance

### Ethical & CARE Compliance at v10.4

The v10.4 governance release required that documentation governance:

- Respect CARE principles for any data involving communities or Indigenous knowledge.  
- Make documentation governance **transparent** via ledgers and public reports.  
- Ensure documentation standards did not obscure or misrepresent ethical constraints.  

Although `indigenous_rights_flag` is `false` for this document (no sensitive cultural content here), it still:

- Operates under the **Root Governance Charter** and **FAIR+CARE guidance**.  
- Must be interpreted with those frameworks in mind when applied to datasets.

### AI Governance & Safety Boundaries

At v10.4:

- AI assistants and Focus Mode were explicitly constrained to:
  - Avoid hallucinating governance rules or approvals.  
  - Avoid speculative reconstruction of undocumented decisions.  
  - Clearly differentiate summaries from authoritative source text.  

- Any AI-based explanation of v10.4 governance must:
  - Ground statements in this document, the charter, or referenced artifacts (e.g., ledgers, manifests).  
  - Respect `ai_transform_prohibited` and `transform_registry.prohibited` lists.

---

## 🕰️ Version History

| Version   | Date       | Author      | Summary                                                                 |
|----------|------------|-------------|-------------------------------------------------------------------------|
| **v10.4.1** | 2025-12-06 | A. Barta   | Aligned governance release doc with KFM-MDP v11.2.4 (front-matter, heading structure, AI transform metadata, catalog/provenance alignment) while preserving historical v10.4 governance semantics. |
| v10.4.0 | 2025-11-14 | A. Barta     | Initial governance release for v10.4: adopted Markdown Protocol v10.4, mandated CI/CD enforcement, deprecated pre-10.4 patterns, and activated immutable governance tracking for docs. |
| v9.7.0  | 2025-10-01 | KFM Maintainers | Pre-v10 governance policies that informed the v10.0 and v10.4 modernization steps. |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — CC-BY 4.0**  
Validated under **Master Coder Protocol v6.3**  
FAIR+CARE Certified · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

Governance Ledger Event: `governance-release-v10.4`  

[Back to Governance Releases Index](README.md) · [Governance Index](../README.md) · [Root Charter](../ROOT-GOVERNANCE.md)

</div>
