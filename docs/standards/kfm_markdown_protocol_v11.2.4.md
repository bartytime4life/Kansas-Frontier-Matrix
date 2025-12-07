---
title: "📑 Kansas Frontier Matrix — Markdown Authoring Protocol (KFM-MDP) v11.2.5"
path: "docs/standards/kfm_markdown_protocol_v11.2.5.md"
version: "v11.2.5"
last_updated: "2025-12-06"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Annual · FAIR+CARE Council & Focus Mode Board"
content_stability: "stable"
commit_sha: "<latest-commit-hash>"
signature_ref: "releases/v11.2.5/signature.sig"
attestation_ref: "releases/v11.2.5/slsa-attestation.json"
sbom_ref: "releases/v11.2.5/sbom.spdx.json"
manifest_ref: "releases/v11.2.5/manifest.zip"
telemetry_ref: "releases/v11.2.5/focus-telemetry.json"
telemetry_schema: "schemas/telemetry/markdown-protocol-v11.2.5.json"
energy_schema: "schemas/telemetry/energy-v2.json"
carbon_schema: "schemas/telemetry/carbon-v2.json"
governance_ref: "../governance/ROOT-GOVERNANCE.md"
ethics_ref: "../faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../sovereignty/INDIGENOUS-DATA-PROTECTION.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.5"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"
status: "Active / Enforced"
doc_kind: "Standard"
header_profile: "standard"
footer_profile: "standard"
diagram_profiles:
  - "mermaid-flowchart-v1"
  - "mermaid-timeline-v1"
scope:
  domain: "documentation"
  applies_to:
    - "all-markdown"
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
sunset_policy: "Supersedes KFM-MDP v11.2.4"
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
json_schema_ref: "schemas/json/kfm-markdown-protocol-v11.2.5.schema.json"
shape_schema_ref: "schemas/shacl/kfm-markdown-protocol-v11.2.5-shape.ttl"
story_node_refs: []
immutability_status: "version-pinned"
doc_uuid: "urn:kfm:doc:standards:markdown-protocol:v11.2.5"
semantic_document_id: "kfm-markdown-protocol-v11.2.5"
event_source_id: "ledger:kfm:doc:standards:markdown-protocol:v11.2.5"
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
deprecated_fields:
  - "old_markdown_standard_v10.4"
---

<div align="center">

# 📑 **Kansas Frontier Matrix — Markdown Authoring Protocol v11.2.5**  
`docs/standards/kfm_markdown_protocol_v11.2.5.md`

**Purpose:**  
Define the canonical, enforceable Markdown authoring rules for the Kansas Frontier Matrix (KFM) v11.2.5.  
This protocol standardizes structure, headings, metadata, and narrative patterns so that all Markdown in the monorepo is CI-safe, FAIR+CARE-aligned, semantically interoperable, and ready for advanced Story Node / Focus Mode integration.

[![Docs · MCP v6.3](https://img.shields.io/badge/Docs-MCP_v6.3-blue "Master Coder Protocol v6.3")]() · [![KFM-MDP v11.2.5](https://img.shields.io/badge/KFM%E2%80%93MDP-v11.2.5-informational "Markdown Protocol v11.2.5")]() · [![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Compliant-gold "FAIR+CARE Compliant")]() · [![WCAG AA+](https://img.shields.io/badge/Accessibility-WCAG_2.1_AA%2B-blueviolet "WCAG 2.1 AA+")]() · [![Status: Active](https://img.shields.io/badge/Status-Active-brightgreen "Status: Active & Enforced")]()

</div>

---

## 📘 Overview

### 1. Scope and Intent

KFM-MDP v11.2.5 governs **all Markdown files** within the Kansas Frontier Matrix monorepo, regardless of domain (ETL pipelines, graph schemas, AI docs, UI specs, archaeology analyses, hydrology notes, etc.). If it is `.md` and lives in the repository, this protocol applies.

This version:

- Adds new **approved sections** to the heading registry for standards alignment (**STAC/DCAT metadata and PROV provenance**). These additional H2 sections ensure that semantic metadata is explicitly documented and machine-identifiable.
- Strengthens **Focus Mode** and **Story Node** integration based on AI-architect feedback, improving how documents are segmented and indexed for narrative overlays and knowledge graph ingestion.
- Incorporates the latest **governance rules** and **MCP 2.0** principles, aligning documentation with updated FAIR, CARE, and Indigenous data sovereignty policies.
- Emphasizes **provenance tracking** and **knowledge graph compatibility**: every document is linked in a provenance chain and mapped to ontologies so it can be traced and ingested into the KFM knowledge graph.
- Clarifies **forbidden constructs** and tightens CI enforcement (e.g., schema linting, footer checks) to preempt ambiguous or non-compliant Markdown.
- Maintains backward compatibility **only where essential** – preserving structural elements required by CI workflows and current Focus Mode transformer behavior – while deprecating legacy patterns from pre-v11 standards.

All other documentation standards (e.g. domain-specific SOP templates, experiment log formats) must build on top of this protocol, **not override it**.

### 2. Core Principles

1. **Single Source of Truth**  
   This file is the authoritative reference for Markdown authoring. Other docs may extend it but must never contradict it.

2. **Documentation-First**  
   Every feature, pipeline, model, or dataset change must be accompanied by conforming Markdown docs: architecture notes, experiment logs, model cards, or SOPs. If the docs aren’t updated, the work is not considered complete.

3. **Machine-Readable by Design**  
   Consistent front-matter, standardized headings, and well-formed tables/lists enable automated extraction into DCAT/STAC catalogs and the knowledge graph. The format is designed to be parsed by scripts and AI, facilitating semantic indexing and crosswalks to external standards.

4. **Human-Friendly Narrative**  
   Despite being machine-compatible, docs remain readable to humans: clear language, logical sections, meaningful headings, and a visible Purpose block near the top. Structure should serve both automated systems and human comprehension.

5. **Ethical & Sovereignty-Aware**  
   The protocol embeds FAIR and CARE principles, CIDOC-CRM semantics, and Indigenous data sovereignty flags to ensure documentation respects governance and ethical constraints. Sensitive content must be handled cautiously, and cultural context must be honored in how information is presented.

6. **Predictable Layout & Navigation**  
   Standard documents have a predictable scaffold: a rooted title + badge row, defined section order (per the heading registry), and a version history and governance footer. This consistency enables uniform navigation and UI rendering (e.g., Focus Mode can reliably find key sections).

### 3. Author Quickstart (Human-Facing)

Before writing or editing any KFM Markdown file, follow this checklist:

1. **Copy a compatible template**  
   Start from an existing document of the same `doc_kind` (e.g. Standard, Reference, Guide) in the repository (such as something in `docs/standards/` or `docs/guides/`). This ensures you inherit the correct front-matter and section structure.

2. **Fill in the YAML front-matter**  
   - Set the document’s `title`, file `path`, `version`, and `last_updated` date.  
   - Confirm the `license`, `mcp_version`, `markdown_protocol_version`, and governance references (`governance_ref`, `ethics_ref`, etc.) match current project standards.  
   - For standards, ensure `doc_kind`, `status`, and `review_cycle` are correct.

3. **Add a centered Purpose block**  
   Under the H1 title, include a short **Purpose** paragraph explaining what the document is for and who should read or use it.

4. **Use *only* approved H2 sections**  
   Structure the main content using the allowed H2 headings from the `heading_registry.approved_h2` list (e.g., Overview, Directory Layout, Context, etc.). Do *not* invent new top-level section titles. Use H3/H4 subsections under those as needed.

5. **End with standardized footer sections**  
   Include a **Version History** table and a governance footer at the end. The footer should provide links back to the docs root, the standards index, and the project governance charter.

If in doubt: start from a previous standard, keep the structure clean, and let CI tell you what to fix.

### 4. Author Quickstart (ChatGPT / AI Usage)

When you use ChatGPT (or any AI assistant) to draft KFM documentation, adhere to these patterns so the result can be pasted **directly into GitHub** and still pass this protocol:

1. **Always ask the AI for:**

   - A full Markdown document that **starts with a YAML front-matter block** like the one above (bounded by `---` at the very top and bottom of the YAML section).  
   - Headings using standard Markdown syntax (`#`, `##`, etc.) with no extra decoration beyond emojis and text.  
   - Code blocks fenced with tildes (`~~~`), with a language specified (e.g., `json`, `bash`, `mermaid`, `text`).

2. **Tell the AI explicitly:**

   - Not to include system-specific citation markers or special control characters (e.g. no `【...】` or hidden markup).  
   - Not to include HTML for layout unless absolutely necessary (and then only minimal tags like `<div align="center">`).  
   - To avoid nested backtick fences or constructs that might break Markdown rendering in GitHub.

3. **Post-processing before commit:**

   - After copying the AI’s output, check that the YAML front-matter’s `path` matches the file path you’re saving to.  
   - Confirm the version and date are correct.  
   - Run the repo’s Markdown lint locally to catch obvious errors before pushing.

4. **Common pitfalls when using ChatGPT:**

   - **Citations:** ChatGPT might generate inline citations (`[1]`, `【source】`, etc.). For KFM docs, you should either remove them or convert them into normal prose references.  
   - **Overly nested lists:** GitHub Markdown can render them, but deep nesting can get messy. Keep lists shallow.  
   - **Random HTML:** Some outputs sprinkle `<br>` or `<p>` tags around. Remove any unnecessary HTML so Markdown remains clean.

---

## 🗂️ Directory Layout

~~~text
KansasFrontierMatrix/
├── 📂 docs/                                  # All documentation
│   ├── 📂 standards/                         # Standards & policies (Markdown, FAIR+CARE, governance, etc.)
│   ├── 📂 architecture/                      # System & subsystem designs (ETL, graph, API, UI, Focus Mode)
│   ├── 📂 guides/                            # How-to guides, tutorials, SOP-style walkthroughs
│   ├── 📂 data/                              # Data contracts, source registries, schema notes
│   ├── 📂 analyses/                          # Domain analyses & case studies (archaeology, hydrology, etc.)
│   └── 📄 glossary.md                        # Shared glossary for KFM-wide terminology
├── 📂 src/                                   # Backend & service code
│   ├── 📂 pipelines/                         # ETL, AI/ML, orchestration (batch, streaming, LangGraph, Airflow)
│   ├── 📂 graph/                             # Neo4j schema, loaders, queries, lineage helpers
│   ├── 📂 api/                               # FastAPI / GraphQL services (gateway, auth, routing)
│   └── 📂 tools/                             # Backend utilities, CLIs, migrations
├── 📂 data/                                  # Data lifecycle: raw → work → processed → releases
│   ├── 📂 sources/                           # External dataset manifests (STAC/DCAT-aligned)
│   ├── 📂 raw/                               # Raw ingested data (LFS/DVC; not committed directly)
│   ├── 📂 work/                              # Intermediate normalized / enriched data
│   ├── 📂 processed/                         # Production-ready GeoJSON, COGs, CSVs, graph exports
│   └── 📂 stac/                              # STAC Collections & Items indexing processed assets
├── 📂 schemas/                               # JSON, JSON-LD, STAC, DCAT, SHACL, telemetry schemas
│   ├── 📂 json/                              # JSON schemas (docs, pipelines, Story Nodes, Focus telemetry)
│   └── 📂 telemetry/                         # Energy, carbon, lineage, metrics schemas
├── 📂 mcp/                                   # Master Coder Protocol artifacts
│   ├── 📂 experiments/                       # Experiment logs (timestamped, domain-tagged)
│   ├── 📂 model_cards/                       # Model documentation & evaluation cards
│   └── 📂 sops/                              # SOPs for repeatable processes (ETL, modeling, deployment)
├── 📂 tests/                                 # Automated test suites (unit, integration, UI)
├── 📂 tools/                                 # Repo-level tools, dev utilities, maintenance scripts
└── 📂 .github/                               # CI/CD workflows & GitHub configuration
    └── 📂 workflows/                         # CI pipelines (kfm-ci, docs-lint, lineage-audit, energy/carbon)
~~~

**Author rules:**

- Every directory documented in this layout **MUST** have a corresponding `README.md` describing its contents and purpose.
- All new top-level directories **MUST** be added to the above tree with an appropriate emoji and concise comment.
- Directory trees in documentation **MUST** use a fenced code block with `text` syntax (as above) and the canonical `├──` / `└──` glyphs. Do not nest triple-backtick fences or mix tab/space indentation.

---

## 🧭 Context

This Markdown protocol operates at the nexus of multiple KFM standards and systems:

- **KFM-OP v11 (Ontology Protocol)** – defines how entities, relationships, time, and space are modeled in the KFM knowledge graph. Documentation must use terms consistent with the ontology to describe data and processes.
- **MCP-DL v6.3 (Master Coder Protocol – Documentation Layer)** – reflects the project’s documentation-first workflow mandate. Every code or data change is coupled with docs.
- **File/Data Architecture** – defines where data manifests, STAC catalogs, and provenance metadata reside (e.g., `data/sources/` for DCAT metadata, `data/stac/` for STAC Items). This protocol ensures docs reference these locations consistently.
- **Focus Mode v3 & Story Nodes** – AI-driven narrative features that rely on predictable, parseable Markdown structure. Focus Mode overlays explanations from docs onto the UI, and Story Nodes link narrative text to spatiotemporal context.

The Markdown rules are intentionally **strict** so that:

- CI can automatically reject any non-conforming or ambiguous documentation.
- The knowledge graph can safely ingest documentation as structured records (e.g., treating a doc as a CIDOC CRM E29 Design or Procedure) and link versions via PROV-O provenance chains.
- Focus Mode can generate trustworthy narrative overlays from docs without hallucinating structure or content.

When in doubt:

- Prefer **more structure** (clear headings, lists, tables) over ad-hoc formatting.
- Prefer **explicit metadata** (in YAML or in-text descriptors) over implicit or assumed context.
- Prefer including **Directory Layout** and **Version History** sections where applicable.

---

## 🗺️ Diagrams

Diagrams are encouraged to illustrate concepts, but they must adhere to strict rules:

1. **Allowed Diagram Types**  
   Only the following diagram profiles are sanctioned by this standard:

   - `mermaid-flowchart-v1` – for system architecture or data flow diagrams.
   - `mermaid-timeline-v1` – for chronological timelines (project evolution, historical sequences).

   No other diagram types or raw HTML graphics are allowed in Markdown at this time.

2. **Diagram Placement**

   - Diagrams should usually reside in a dedicated section (often under “🧱 Architecture” or “🧪 Validation & CI/CD”) or immediately adjacent to the text they illustrate.
   - Every diagram **MUST** have a brief title or caption *and* a one- or two-sentence explanation in the text.

3. **Example – Mermaid Flowchart**

   ~~~mermaid
   flowchart LR
       A[Author writes Markdown] --> B[CI lints & checks]
       B --> |Pass| C[Content merges to main]
       B --> |Fail| D[Author fixes issues]
   ~~~

4. **Example – Mermaid Timeline**

   ~~~mermaid
   timeline
       title Markdown Protocol Evolution
       2023-11-10 : v10.4.3 : "Markdown Structural Rules (legacy)"
       2025-11-25 : v11.2.0 : "Re-architecture & Profiles"
       2025-11-26 : v11.2.1 : "Provenance Hardening"
       2025-11-27 : v11.2.2 : "Heading Registry & Transform Rules"
       2025-12-04 : v11.2.4 : "Semantic Alignment & AI Integration"
       2025-12-06 : v11.2.5 : "Metadata Refinements & Unified Markdown Alignment"
   ~~~

5. **Accessibility (A11y) Considerations**

   - Ensure diagram text (labels, axes) is legible with sufficient contrast.
   - Summarize the key insight of each diagram in the surrounding text.
   - Avoid using color alone to differentiate elements; use distinct shapes, line styles, or labels as well.

6. **Forbidden Diagram Practices**

   - Do **not** include ASCII-art diagrams or drawings made of text characters.
   - Do **not** embed secrets, private URLs, or credentials in diagrams.
   - In standards docs, all diagram elements should be labeled or explained in nearby text.

---

## 🧠 Story Node & Focus Mode Integration

All KFM documentation is a potential input to **Story Nodes** and **Focus Mode** features. This protocol ensures Markdown content is:

- **Segmentable** – it can be broken into meaningful narrative chunks.
- **Alignable** – it can be aligned with the Story Node JSON schema.
- **Traceable** – Focus Mode summaries or highlights can reference the exact source via stable IDs and provenance links.

### 1. Linking Docs to Story Nodes

A *Story Node* is a JSON-based narrative element with text and a spatiotemporal footprint. Documentation may interact with Story Nodes in the following ways:

- **Referenced by Story Nodes:**  
  Story Nodes may refer to a document or a specific section via a `target` identifier. For example:

  ~~~text
  "target": "kfm-markdown-protocol-v11.2.5"
  ~~~

- **Referencing Story Nodes from docs:**  
  A document can mention specific Story Nodes by ID when relevant, for example:

  ~~~text
  Related Story Node: urn:kfm:story-node:docs:markdown-protocol:overview
  ~~~

Rules:

- Standards documents should reference Story Nodes **only** to clarify how documentation is used in narratives, not as a general content pattern.
- Story Node definitions reside in JSON (e.g., under `docs/architecture/story_nodes/`); Markdown links out to them but does not embed them.

### 2. Focus Mode Behavior

When a user activates Focus Mode on this document (i.e., focusing the UI or AI assistant on `kfm-markdown-protocol-v11.2.5`):

- **Focus Mode MAY:**

  - Summarize sections of the doc (within `ai_transform_permissions`).
  - Highlight key parts (Overview, Diagrams, CI rules, etc.).
  - Display relationships to other standards (e.g., Governance, FAIR+CARE).

- **Focus Mode MUST NOT:**

  - Alter or rewrite the authoritative content of this document.
  - Generate new policy or normative text not present here.
  - Hide or override governance and ethics references.

These constraints are enforced by the `ai_transform_*` fields and the system’s governance rules.

### 3. AI Transform Permissions

The `ai_transform_permissions` and `ai_transform_prohibited` fields in the YAML front-matter are **normative**.

- **Allowed transforms:**

  - Summarization
  - Highlight extraction
  - Timeline generation
  - 3D/AR context render
  - Accessibility adaptations
  - Diagram extraction
  - Metadata extraction

- **Prohibited transforms:**

  - Content alteration
  - Speculative additions
  - Unverified architectural claims
  - Narrative fabrication
  - Governance overrides

Anything not listed is assumed disallowed until this protocol is updated.

### 4. Focus-Optimized Writing Patterns

To keep documentation **Focus Mode friendly**, authors should:

- Start sections and paragraphs with **clear topic sentences**.
- Keep each sub-section **narrowly scoped** (one concept or task per H3/H4).
- Use **descriptive link text** rather than “here” or bare URLs.
- Avoid ambiguous pronouns when possible; prefer explicit nouns.
- Include short **recap lists** in complex sections so Focus Mode can surface them as quick answers.

---

## 🧪 Validation & CI/CD

KFM treats documentation as a first-class citizen in continuous integration. Every Markdown file must pass a suite of checks before it can merge.

### 1. Validation Profiles

The following automated checks correspond to entries in the `test_profiles` list:

- **`markdown-lint`** – Style and structural linting (headings, lists, whitespace).
- **`schema-lint`** – YAML front-matter validation against the JSON schema for this `doc_kind`.
- **`metadata-check`** – Ensures required metadata is present and correctly formatted.
- **`footer-check`** – Verifies standardized Version History and governance footer are present.
- **`accessibility-check`** – Basic WCAG 2.1 AA checks for structural accessibility.
- **`diagram-check`** – Validates Mermaid diagrams and allowed diagram profiles.
- **`provenance-check`** – Checks `provenance_chain` and Version History entries for consistency.

If any of these fail, CI blocks the merge.

### 2. YAML Front-Matter Rules

- Every Markdown file **MUST** begin with a YAML front-matter block, bounded by `---` lines at the start and end.
- The front-matter must be at the very top of the file (no blank lines ahead of it).
- It must include all required fields defined by the schema for its `doc_kind`.
- Deprecated fields listed in this protocol’s `deprecated_fields` **MUST NOT** be used.
- Order of keys is not semantically important but should follow the standard pattern used here for readability and diffs.

### 3. Heading Rules

- Exactly **one H1** (`#`) per document, typically in the centered header block.
- H2 headings (`##`) must come from the allowed list in `heading_registry.approved_h2` for this doc type.
- Headings must not skip levels (no jumping from H2 to H4).
- H5 and H6 headings are not allowed.
- Do not simulate headings with bold text – use real heading syntax.

### 4. Links and References

- Use **relative paths** for internal links (e.g., `../architecture/graph_schema.md`).
- Use `https://` for external links when available.
- Avoid bare URLs in text; always provide descriptive anchor text.
- For same-document references, use heading anchors (e.g., `#-validation--cicd`), adjusting for GitHub’s slug rules.

### 5. Code Blocks

- Always use fenced code blocks with tildes (`~~~`) in this standard.
- Specify the language when relevant (`json`, `bash`, `text`, `mermaid`, etc.).
- If you need to show a fenced block inside another example, you can still use nested tildes (outer vs inner) or indentation.
- Never include secrets (keys, passwords) in code examples.

### 6. Test Profiles Matrix

| **Test Profile**       | **Purpose**                                   | **Tooling/Workflow**                        |
|------------------------|-----------------------------------------------|---------------------------------------------|
| `markdown-lint`        | Structural and style linting                  | Markdownlint, custom lint scripts           |
| `schema-lint`          | YAML front-matter schema validation           | JSON Schema validator                       |
| `metadata-check`       | Required metadata presence/format             | Custom validation scripts                   |
| `diagram-check`        | Mermaid diagram syntax/profile check          | Mermaid CLI/parser                          |
| `accessibility-check`  | Basic accessibility structure checks          | Markdown a11y tools / axe-like checks       |
| `provenance-check`     | Provenance chain and version history          | Custom script comparing YAML vs footer      |
| `footer-check`         | Governance footer presence and correctness    | Regex/AST-based footer check                |

---

## 📦 Data & Metadata

This protocol document itself can be treated as a **data object** within the KFM ecosystem.

- It can appear as a dataset in a DCAT catalog.
- It can be referenced as a STAC Item within a documentation-oriented Collection.
- It is represented as a node in the Neo4j knowledge graph, linked to other standards and entities.

### 1. Required Metadata Fields (Standard Documents)

For `doc_kind: "Standard"`, the following front-matter fields are required:

**Identity & Versioning**

- `title`
- `path`
- `version`
- `doc_uuid`
- `semantic_document_id`
- `event_source_id`
- `status`
- `doc_kind`

**Lifecycle & Governance**

- `last_updated`
- `release_stage`
- `lifecycle`
- `review_cycle`
- `ttl_policy`
- `sunset_policy`
- `governance_ref`
- `ethics_ref`
- `sovereignty_policy`

**Licensing & Ethics**

- `license`
- `mcp_version`
- `markdown_protocol_version`
- `fair_category`
- `care_label`
- `sensitivity`
- `sensitivity_level`
- `public_exposure_risk`
- `classification`
- `jurisdiction`
- `indigenous_rights_flag`
- `data_steward`

**Provenance & Cataloging**

- `commit_sha`
- `signature_ref`
- `attestation_ref`
- `sbom_ref`
- `manifest_ref`
- `telemetry_ref`
- `telemetry_schema`
- `energy_schema`
- `carbon_schema`
- `ontology_alignment`
- `metadata_profiles`
- `provenance_chain`
- `provenance_requirements`
- `doc_integrity_checksum`

**AI & Transform Permissions**

- `ai_training_inclusion`
- `ai_focusmode_usage`
- `ai_transform_permissions`
- `ai_transform_prohibited`
- `transform_registry`

**Structural & Profile**

- `header_profile`
- `footer_profile`
- `diagram_profiles`
- `scope`
- `heading_registry`
- `test_profiles`
- `ci_integration`
- `branding_registry`
- `layout_profiles`
- `badge_profiles`
- `requires_purpose_block`
- `requires_version_history`
- `requires_directory_layout_section`
- `requires_governance_links_in_footer`
- `deprecated_fields`

### 2. Semantic Alignment

This documentation standard is designed to map cleanly onto:

- **DCAT** – treat the doc as a `dcat:Dataset` or `dcat:CatalogRecord` with `dct:title`, `dct:description`, `dct:license`, `dct:modified`, etc.
- **STAC** – treat the doc as a STAC Item in a “documentation” Collection (no geometry; `datetime` = `last_updated`; asset = Markdown file).
- **PROV-O** – treat each version as a `prov:Plan` and use `prov:wasDerivedFrom` between versions. Release events are `prov:Activity` linked to Agents.
- **schema.org** – treat as a `schema:TechArticle` with `name`, `description`, `identifier`, `dateModified`, `license`.
- **CIDOC-CRM** – treat as `E29 Design or Procedure`.

Explicit ontology mappings are defined in `ontology_alignment`.

### 3. Minimum Metadata Checklist (Per Document)

For any new KFM doc:

1. `title`, `path`, `version`, `last_updated`, `license` set correctly.
2. `doc_kind`, `status`, `review_cycle` defined.
3. `doc_uuid`, `semantic_document_id`, `event_source_id` set.
4. `provenance_chain` includes at least one prior version (or origin).
5. `ai_focusmode_usage`, `ai_transform_*` defined if AI will use the doc.

---

## 🌐 STAC, DCAT & PROV Alignment

This section describes how **documentation itself** fits into the broader STAC/DCAT/PROV ecosystem used by KFM.

### 1. DCAT Alignment

In DCAT:

- The document is modeled as a `dcat:Dataset` or, in portals, via a `dcat:CatalogRecord` plus `dcat:Dataset`.
- Mappings:
  - `title` → `dct:title`
  - Purpose / intro section → `dct:description`
  - `license` → `dct:license`
  - `last_updated` → `dct:modified`
  - `doc_uuid` → `dct:identifier`
  - `path` → part of a `dcat:Distribution` access URL (e.g., GitHub URL)
- A distribution might be the raw Markdown file (`text/markdown`) and/or rendered HTML or PDF.

### 2. STAC Alignment

In STAC:

- Documentation can live in a dedicated Collection (e.g., `kfm-docs`).
- This document appears as a STAC Item:
  - `id` = `semantic_document_id`
  - `properties.datetime` = `last_updated`
  - `assets.markdown`:
    - `href` = URL to raw file
    - `type` = `text/markdown`
- Because it is non-spatial, `geometry` may be `null` and `bbox` omitted. Alternatively, a default geometry (e.g., bounding box of Kansas) can be used if desired for mapping.

### 3. PROV Alignment

In PROV-O:

- Each version is a `prov:Entity` and specifically a `prov:Plan`.
- Versioning relationships:
  - `v11.2.5 prov:wasDerivedFrom v11.2.4` (and earlier).
  - `provenance_chain` encodes this in YAML; a converter can export it as PROV RDF.
- Creation/update events:
  - Release activities (e.g., `ex:release_v11_2_5`) are `prov:Activity`.
  - Architects/councils are `prov:Agent` (often `prov:Organization`).
  - `prov:wasGeneratedBy` links the entity (doc version) to its release activity.
  - `prov:wasAssociatedWith` links activity to agents.

Aligning with these standards makes KFM documentation first-class in catalogs and provenance graphs.

---

## 🧱 Architecture

From an architecture perspective, this standard:

1. **Defines a Contract**  
   - All Markdown files must satisfy this spec’s schema and structure.
   - Tools (linters, doc generators, Focus Mode) rely on this contract for predictable behavior.

2. **Integrates into CI/CD**  
   - `.github/workflows/kfm-ci.yml` runs tests indicated in `test_profiles`.
   - Docs must pass all relevant checks before merge.
   - Any schema change here requires updates to JSON schemas, SHACL shapes, and possibly CI config.

3. **Supports Tooling & Site Generation**  
   - Doc site generation can use the front-matter (e.g., `doc_kind`, `category`, `scope`) to group and layout pages.
   - `heading_registry.approved_h2` enables automatic section TOCs and Focus Mode anchors.
   - `branding_registry` fields can populate consistent subtitles/taglines in site templates.

4. **Change Management**  
   - Any change to this protocol should be proposed via PR, with:
     - Updated markdown.
     - Updated JSON/SHACL schemas.
     - Updated CI config if new tests are added.
   - Version and Version History **must** be updated as part of the same PR.

---

## ⚖ FAIR+CARE & Governance

This standard embeds FAIR and CARE principles into documentation:

1. **FAIR**

   - **Findable:** Stable IDs (`doc_uuid`) and predictable paths; included in catalogs.
   - **Accessible:** Markdown in a public repo with open license.
   - **Interoperable:** Ontology and metadata profile alignment (DCAT, STAC, PROV, schema.org).
   - **Reusable:** Clear licensing, versioning, and provenance history.

2. **CARE**

   - **Collective Benefit:** Documentation is open and written for community use.
   - **Authority to Control:** `indigenous_rights_flag` and `sovereignty_policy` ensure relevant governance over sensitive content.
   - **Responsibility:** Authors are responsible for omitting or generalizing sensitive details (e.g., exact locations of protected sites).
   - **Ethics:** Docs must be accurate, respectful, and free of speculative or sensational claims.

3. **Governance Hooks**

   - `governance_ref`, `ethics_ref`, and `sovereignty_policy` are **authoritative** references.
   - Authors are expected to read and follow those documents when writing.
   - For sensitive topics, additional human review (e.g., FAIR+CARE Council) may be required prior to approval.

---

## 🕰️ Version History

| Version     | Date       | Summary                                                                                                           |
|------------:|------------|-------------------------------------------------------------------------------------------------------------------|
| **v11.2.5** | 2025-12-06 | Minor revision based on v11.2.4, aligning metadata fields and examples with unified Markdown usage; updated provenance_chain and exemplar identifiers; no structural changes. |
| v11.2.4     | 2025-12-04 | Based on v11.2.2, incorporating new governance rules (MCP 2.0, Architect feedback) and project updates. Added STAC/DCAT/PROV alignment section, extended Focus Mode & Story Node guidance, and refined CI enforcement. |
| v11.2.3     | 2025-12-02 | Interim update refining transform permissions and semantic indexing prep for Focus Mode (no structural changes; draft only). |
| v11.2.2     | 2025-11-27 | Introduced heading registry, transform rules, expanded metadata/provenance fields, unified YAML front-matter structure, and tightened anti-pattern definitions. |
| v11.2.1     | 2025-11-26 | Added profile system, stronger provenance chain enforcement, and stricter DCAT/STAC metadata requirements.         |
| v11.2.0     | 2025-11-25 | Major overhaul for KFM v11: re-architected front-matter, added header/footer profiles, CI test profiles, and diagram usage rules. |
| v11.0.1     | 2025-11-20 | Initial KFM v11 release consolidating markdown rules under the new ontology and governance framework.             |
| v10.4.3     | 2023-11-10 | Legacy markdown rules (pre-KFM) covering basic front-matter, H1–H4 structure, and minimal README templates.       |

---

<div align="center">

📑 **Kansas Frontier Matrix — Markdown Authoring Protocol (KFM-MDP) v11.2.5**  
Scientific Insight · Documentation-First · FAIR+CARE Ethics · Sustainable Intelligence  

[📘 Docs Root](..) · [📂 Standards Index](./README.md) · [⚖ Governance](../governance/ROOT-GOVERNANCE.md)

</div>
