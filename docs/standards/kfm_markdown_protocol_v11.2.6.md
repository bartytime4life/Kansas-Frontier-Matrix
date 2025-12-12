---
title: "📑 Kansas Frontier Matrix — Markdown Authoring Protocol (KFM-MDP) v11.2.6"
path: "docs/standards/kfm_markdown_protocol_v11.2.6.md"

version: "v11.2.6"
last_updated: "2025-12-12"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Annual · FAIR+CARE Council & Focus Mode Board"
content_stability: "stable"

status: "Active / Enforced"
doc_kind: "Standard"
header_profile: "standard"
footer_profile: "standard"
diagram_profiles:
  - "mermaid-flowchart-v1"
  - "mermaid-timeline-v1"

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

scope:
  domain: "documentation"
  applies_to:
    - "all-markdown"
    - "docs/**"
    - "mcp/**"
    - "src/**/README.md"
    - ".github/**/*.md"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"
sensitivity: "General (non-sensitive; auto-mask rules apply)"
sensitivity_level: "None"
public_exposure_risk: "Low"
classification: "Public"
jurisdiction: "Kansas / United States"
indigenous_rights_flag: true
data_steward: "KFM FAIR+CARE Council"

ttl_policy: "24 months"
sunset_policy: "Superseded by KFM-MDP v12"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"

signature_ref: "../../releases/v11.2.6/signature.sig"
attestation_ref: "../../releases/v11.2.6/slsa-attestation.json"
sbom_ref: "../../releases/v11.2.6/sbom.spdx.json"
manifest_ref: "../../releases/v11.2.6/manifest.zip"

telemetry_ref: "../../releases/v11.2.6/focus-telemetry.json"
telemetry_schema: "../../schemas/telemetry/markdown-protocol-v11.2.6.json"
energy_schema: "../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../schemas/telemetry/carbon-v2.json"

governance_ref: "governance/ROOT-GOVERNANCE.md"
ethics_ref: "faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "sovereignty/INDIGENOUS-DATA-PROTECTION.md"

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
  - "docs/standards/kfm_markdown_protocol_v11.2.5.md@v11.2.5"
  - "docs/standards/kfm_markdown_protocol_v11.2.4.md@v11.2.4"
  - "docs/standards/kfm_markdown_protocol_v11.2.3.md@v11.2.3"
  - "docs/standards/kfm_markdown_protocol_v11.2.2.md@v11.2.2"
  - "docs/standards/kfm_markdown_protocol_v11.2.1.md@v11.2.1"
  - "docs/standards/kfm_markdown_protocol_v11.2.md@v11.2.0"
  - "docs/standards/kfm_markdown_protocol_v11.md@v11.0.1"
  - "docs/standards/markdown_rules.md@v10.4.3"

provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: true

json_schema_ref: "../../schemas/json/kfm-markdown-protocol-v11.2.6.schema.json"
shape_schema_ref: "../../schemas/shacl/kfm-markdown-protocol-v11.2.6-shape.ttl"

story_node_refs: []
immutability_status: "version-pinned"
doc_uuid: "urn:kfm:doc:standards:markdown-protocol:v11.2.6"
semantic_document_id: "kfm-markdown-protocol-v11.2.6"
event_source_id: "ledger:kfm:doc:standards:markdown-protocol:v11.2.6"
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
  - "layout-normalization"

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
    - "3d-context-render"
    - "a11y-adaptations"
    - "diagram-extraction"
    - "metadata-extraction"
    - "layout-normalization"
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
  - "footer-check"
  - "accessibility-check"
  - "diagram-check"
  - "metadata-check"
  - "provenance-check"
  - "secret-scan"
  - "pii-scan"

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

fencing_profile: "outer-backticks-inner-tildes-v1"

badge_profiles:
  - "root-centered-badge-row"

requires_purpose_block: true
requires_version_history: true
requires_directory_layout_section: true
requires_governance_links_in_footer: true

deprecated_fields:
  - "old_markdown_standard_v10.4"
---

<div align="center">

# 📑 **Kansas Frontier Matrix — Markdown Authoring Protocol (KFM‑MDP) v11.2.6**
`docs/standards/kfm_markdown_protocol_v11.2.6.md`

**Purpose**  
Define the **canonical, enforceable Markdown authoring rules** for the Kansas Frontier Matrix (KFM).  
This protocol standardizes **structure, headings, metadata, and narrative patterns** so Markdown across the monorepo is **CI‑safe, FAIR+CARE‑aligned, semantically interoperable**, and ready for **Story Node / Focus Mode** integration.

<img src="https://img.shields.io/badge/MCP--DL-v6.3-blueviolet" />
<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/FAIR%2BCARE-Governance%20Aligned-orange" />
<img src="https://img.shields.io/badge/Accessibility-WCAG_2.1_AA%2B-blueviolet" />
<img src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />

</div>

---

## 📘 Overview

### 1. Scope and intent

KFM‑MDP v11.2.6 governs **all Markdown files** in the Kansas Frontier Matrix monorepo.

If it’s `.md` in this repo, this protocol applies—especially:

- Standards, governance, and guides under `docs/**`
- Workflow documentation under `docs/workflows/**`
- Telemetry documentation under `docs/telemetry/**`
- Experiment logs, model cards, and SOPs under `mcp/**`
- Any `README.md` in `src/**`

This protocol exists to ensure Markdown is:

- **Predictable for humans** (consistent layout, consistent headings)
- **Parseable for machines** (front‑matter + stable sections)
- **Governable** (FAIR+CARE and sovereignty constraints are explicit)
- **Indexable** (DCAT/STAC/PROV aligned)
- **Safe to transform** (Focus Mode can summarize without inventing policy)

KFM‑MDP v11.2.6 supersedes v11.2.5.

### 2. Absolute rules (normative)

1. **Front‑matter is required**  
   Every governed KFM Markdown document MUST start with YAML front‑matter (`---` … `---`).

2. **Exactly one H1**  
   One—and only one—`#` heading per file.

3. **Approved H2s only**  
   Every H2 MUST match exactly one entry in `heading_registry.approved_h2`, including the emoji.

4. **Standards ordering**  
   Standards and indexes MUST place:
   - `## 📘 Overview` first
   - `## 🗂️ Directory Layout` second
   - `## 🕰️ Version History` last

5. **Directory layout must not “break the box”**  
   Every directory tree MUST be fenced as `~~~text` and use consistent branch glyphs (`├──`, `└──`, `│`).

6. **Internal fences use tildes**  
   In committed docs: use `~~~` for fenced blocks (`~~~json`, `~~~yaml`, `~~~bash`, `~~~mermaid`, `~~~text`).  
   Do not mix `~~~` and backticks inside the same document.

7. **No secrets / no PII**  
   Docs are scanned. Secrets and PII MUST NOT appear anywhere in Markdown.

### 3. The chat-safe fencing profile

`fencing_profile: outer-backticks-inner-tildes-v1` is mandatory for AI-assisted authoring.

- In chat (assistant output), wrap the entire document in **one** outer fence: ` ```markdown … ``` `
- Inside the document, ALL examples MUST use **tildes** (`~~~`) for code blocks.

This prevents nested “```” blocks from closing the outer fence and breaking the rendered box.

---

## 🗂️ Directory Layout

Directory layouts MUST follow `immediate-one-branch-with-descriptions-and-emojis`.

Rules:

- Use `~~~text` fences (tildes).
- Use `📁` for directories and `📄` for files (add `🧾` for JSON/YAML/log artifacts when helpful).
- Use `├──` / `└──` and maintain vertical bars for readability.
- Keep comments aligned for human scanning.

Canonical monorepo layout (documentation-relevant):

~~~text
📁 KansasFrontierMatrix/
├── 📁 docs/                                   — Documentation layer (standards, workflows, telemetry, guides)
│   ├── 📁 standards/                          — Standards, governance, FAIR+CARE, sovereignty
│   │   ├── 📄 README.md                       — Standards index
│   │   ├── 📄 kfm_markdown_protocol_v11.2.6.md— ← This document (KFM‑MDP)
│   │   ├── 📄 telemetry_standards.md          — Telemetry governance super-standard
│   │   ├── 📄 ui_accessibility.md             — UI accessibility super-standard
│   │   ├── 📁 governance/                     — Governance charter and governance standards
│   │   ├── 📁 faircare/                       — FAIR+CARE guidance
│   │   └── 📁 sovereignty/                    — Indigenous data protection and sovereignty policy
│   │
│   ├── 📁 workflows/                          — Workflow docs (one .yml.md per .github workflow)
│   ├── 📁 telemetry/                          — Telemetry documentation suites (events, validators, lineage, dashboards)
│   ├── 📁 templates/                          — Canonical templates (experiments, model cards, SOPs, core markdown)
│   ├── 📁 architecture/                       — System design docs (ETL → graph → API → UI → Story Nodes)
│   ├── 📁 guides/                             — Author/operator guides
│   ├── 📁 analyses/                           — Research and domain analyses
│   └── 📄 glossary.md                         — Shared vocabulary
│
├── 📁 schemas/                                — Schemas (docs, telemetry, SHACL, STAC/DCAT mappings)
├── 📁 releases/                               — Release packets (manifest, SBOM, signatures, telemetry snapshots)
├── 📁 mcp/                                    — Experiments, model cards, SOPs (MCP‑DL artifacts)
├── 📁 src/                                    — Code (pipelines, graph, APIs, web UI)
└── 📁 .github/                                — CI/CD workflows and repo governance automation
~~~

---

## 🧭 Context

KFM‑MDP sits at the junction of:

- **MCP‑DL v6.3** (documentation-first reproducibility)
- **FAIR+CARE governance** (ethics, stewardship, authority, responsibility)
- **Sovereignty policy** (masking, consent, and restricted content controls)
- **STAC/DCAT/PROV** (catalog discovery and provenance)
- **Story Nodes / Focus Mode** (safe summarization, narrative overlays)

The KFM pipeline is documentation-dependent:

> Deterministic ETL → STAC/DCAT/PROV catalogs → Neo4j → API → React/MapLibre/Cesium → Story Nodes → Focus Mode

If Markdown drifts, downstream cataloging and Focus Mode narratives become unsafe or unreliable—so this protocol is enforced by CI.

---

## 🗺️ Diagrams

Diagrams MUST be:

- placed under `🗺️ Diagrams` (or `🧱 Architecture` / `🧪 Validation & CI/CD` when appropriate),
- fenced with `~~~mermaid`,
- accompanied by a short plain-language explanation.

### Mermaid guardrails (practical rules)

To avoid rendering failures:

- Do NOT use HTML in Mermaid labels (no `<br/>`, no inline tags).
- Keep labels simple; prefer ASCII punctuation.
- If a label includes special characters, use the quoted node label form: `A["Label text"]`.

Example:

~~~mermaid
flowchart LR
  A["Author edits doc"] --> B["CI runs lint + schema validation"]
  B -->|pass| C["Merge allowed"]
  B -->|fail| D["Fix required"]
~~~

---

## 🧠 Story Node & Focus Mode Integration

KFM‑MDP makes Markdown **Story Node friendly**:

- predictable H2 sections become stable “facets” for Focus Mode summaries,
- front‑matter IDs provide stable anchors for graph ingestion,
- transform permissions constrain what AI is allowed to do.

**Focus Mode MAY:**

- summarize and highlight sections,
- produce timelines and navigation aids,
- extract metadata fields and link them to catalogs.

**Focus Mode MUST NOT:**

- alter normative requirements,
- invent governance status,
- fabricate provenance or dataset relationships.

---

## 🧪 Validation & CI/CD

Markdown compliance is CI-enforced.

### Minimum validation profiles

| Profile | What it protects |
|---|---|
| `markdown-lint` | structure (H1/H2 rules), formatting constraints |
| `schema-lint` | YAML front‑matter schema compliance |
| `metadata-check` | required keys present and consistent |
| `diagram-check` | Mermaid parse + allowed diagram profiles |
| `footer-check` | governance links + footer ordering |
| `accessibility-check` | basic a11y checks (heading order, list semantics) |
| `provenance-check` | provenance chain + version history coherence |
| `secret-scan` | blocks secrets/tokens/credentials |
| `pii-scan` | blocks obvious PII leakage |

### Common failure causes

- Missing or malformed front‑matter
- More than one H1
- Unapproved H2 headings (emoji mismatch, text mismatch)
- Directory layouts not fenced with `~~~text`
- Mixed fence styles (using ``` inside files)
- Mermaid node labels with HTML (breaks render)
- Footer missing governance links

---

## 📦 Data & Metadata

### Front‑matter requirements (normative)

A governed KFM doc MUST include:

- identity: `title`, `path`, `version`, `last_updated`
- governance: `governance_ref`, `ethics_ref`, `sovereignty_policy`
- compliance: `license`, `classification`, `sensitivity`, `fair_category`, `care_label`
- provenance: `commit_sha`, `signature_ref` (when release-pinned), `provenance_chain`
- IDs: `doc_uuid`, `semantic_document_id`, `event_source_id`
- AI transform limits: `ai_transform_permissions`, `ai_transform_prohibited`

Placeholders are allowed only where explicitly indicated (e.g., `<latest-commit-hash>`), and MUST be resolved for release-tagged documents.

---

## 🌐 STAC, DCAT & PROV Alignment

### DCAT

- This document is a documentation dataset (`dcat:Dataset` or `dcat:CatalogRecord`).
- `semantic_document_id` maps to `dct:identifier`.
- Markdown is a `dcat:Distribution` (`mediaType: text/markdown`).

### STAC

- The document may be represented as a non-spatial STAC Item:
  - `geometry: null`
  - `properties.datetime = last_updated`
  - `assets.markdown.href` points to the file path in the repo or artifact store.

### PROV‑O

- This standard is a `prov:Plan`.
- Updates and validations are `prov:Activity` instances.
- CI bots, councils, and maintainers are `prov:Agent`s.

---

## 🧱 Architecture

KFM‑MDP drives architecture indirectly by constraining documentation shape:

- documentation can be parsed and transformed deterministically,
- pipeline “contracts” can reference docs as stable entities,
- the graph can ingest doc metadata to link code, data, and governance.

Any change to KFM‑MDP MUST be accompanied by:

- schema updates (`json_schema_ref`, `shape_schema_ref`),
- CI rule updates (lint/validators),
- a new Version History entry,
- updated release packet references when pinned.

---

## ⚖ FAIR+CARE & Governance

KFM‑MDP encodes FAIR+CARE requirements into Markdown:

- **FAIR**: stable identifiers, licenses, and provenance enable findability and reuse.
- **CARE**: sovereignty and stewardship constraints prevent harm and respect authority to control.

Governance is binding and traceable through:

- `governance_ref`
- CI enforcement (required checks)
- release manifests and signatures

---

## 🕰️ Version History

| Version     | Date       | Summary |
|------------:|-----------:|---------|
| **v11.2.6** | 2025-12-12 | Normalized governance/ethics/sovereignty relative paths for `docs/standards/`; clarified normative rules and Mermaid guardrails; reinforced `outer-backticks-inner-tildes-v1` for AI-assisted authoring; improved directory layout readability and alignment. |
| v11.2.5     | 2025-12-07 | Elevated `🗂️ Directory Layout` to second H2 for standards/guides; mandated emoji trees and `~~~text` fences; strengthened AI authoring guidance. |
| v11.2.4     | 2025-12-04 | Added STAC/DCAT/PROV alignment; expanded Story Node & Focus Mode guidance; tightened CI enforcement rules. |
| v11.2.3     | 2025-12-02 | Refined AI transform permissions and Focus Mode behaviors. |
| v11.2.2     | 2025-11-27 | Introduced heading registry; expanded metadata/provenance fields; unified front‑matter patterns. |
| v11.2.1     | 2025-11-26 | Added profile system; stronger provenance enforcement. |
| v11.2.0     | 2025-11-25 | Major overhaul for v11 (profiles, CI test profiles, diagram rules). |
| v11.0.1     | 2025-11-20 | Initial consolidation of markdown rules under v11 governance and ontology alignment. |
| v10.4.3     | 2023-11-10 | Legacy markdown rules prior to v11. |

---

<div align="center">

📑 **Kansas Frontier Matrix — Markdown Authoring Protocol (KFM‑MDP) v11.2.6**  
Documentation-First · FAIR+CARE Governance · Sustainable Intelligence

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/MCP--DL-v6.3-blueviolet" />
<img src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />

[📘 Docs Root](../README.md) ·
[📂 Standards Index](./README.md) ·
[📄 Templates Index](../templates/README.md) ·
[⚙ CI/CD Workflows](../workflows/README.md) ·
[📈 Telemetry Standard](./telemetry_standards.md) ·
[📊 Telemetry Docs](../telemetry/README.md) ·
[♿ UI Accessibility Standard](./ui_accessibility.md) ·
[🏛️ Governance Charter](./governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](./faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](./sovereignty/INDIGENOUS-DATA-PROTECTION.md)

© 2025 Kansas Frontier Matrix — CC‑BY 4.0  
MCP‑DL v6.3 · KFM‑MDP v11.2.6 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>