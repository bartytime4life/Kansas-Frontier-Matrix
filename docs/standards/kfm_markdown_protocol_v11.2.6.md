---
title: "📑 Kansas Frontier Matrix — Markdown Authoring Protocol (KFM-MDP) v11.2.6"
path: "docs/standards/kfm_markdown_protocol_v11.2.6.md"
version: "v11.2.6"
last_updated: "2025-12-10"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Annual · FAIR+CARE Council & Focus Mode Board"
content_stability: "stable"

status: "Active / Enforced"
doc_kind: "Standard"
header_profile: "standard"
footer_profile: "standard"

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
sunset_policy: "Supersedes KFM-MDP v11.2.5"

commit_sha: "<latest-commit-hash>"
signature_ref: "../../releases/v11.2.6/signature.sig"
attestation_ref: "../../releases/v11.2.6/slsa-attestation.json"
sbom_ref: "../../releases/v11.2.6/sbom.spdx.json"
manifest_ref: "../../releases/v11.2.6/manifest.zip"
telemetry_ref: "../../releases/v11.2.6/focus-telemetry.json"
telemetry_schema: "../../schemas/telemetry/markdown-protocol-v11.2.6.json"
energy_schema: "../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../schemas/telemetry/carbon-v2.json"

governance_ref: "../governance/ROOT-GOVERNANCE.md"
ethics_ref: "../faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../sovereignty/INDIGENOUS-DATA-PROTECTION.md"

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
    - summary
    - timeline-generation
    - semantic-highlighting
    - 3d-context-render
    - a11y-adaptations
    - diagram-extraction
    - metadata-extraction
    - layout-normalization
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

# 📑 **Kansas Frontier Matrix — Markdown Authoring Protocol v11.2.6**  
`docs/standards/kfm_markdown_protocol_v11.2.6.md`

**Purpose**  
Define the canonical, enforceable Markdown authoring rules for the Kansas Frontier Matrix (KFM) v11.2.6.  
This protocol standardizes structure, headings, metadata, and narrative patterns so that all Markdown in the
monorepo is CI-safe, FAIR+CARE-aligned, semantically interoperable, and ready for advanced Story Node /
Focus Mode integration.

[![Docs · MCP v6.3](https://img.shields.io/badge/Docs-MCP_v6.3-blue "Master Coder Protocol v6.3")]() ·
[![KFM-MDP v11.2.6](https://img.shields.io/badge/KFM%E2%80%93MDP-v11.2.6-informational "Markdown Protocol v11.2.6")]() ·
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Compliant-gold "FAIR+CARE Compliant")]() ·
[![WCAG AA+](https://img.shields.io/badge/Accessibility-WCAG_2.1_AA%2B-blueviolet "WCAG 2.1 AA+")]() ·
[![Status: Active](https://img.shields.io/badge/Status-Active-brightgreen "Status: Active & Enforced")]()

</div>

---

## 📘 Overview

### 1. Scope and Intent

KFM-MDP v11.2.6 governs **all Markdown files** in the Kansas Frontier Matrix monorepo
(`Kansas-Frontier-Matrix`), across every domain:

- ETL / pipelines (`src/pipelines/`)
- Graph / ontology (`src/graph/`)
- APIs (`src/api/`)
- Web & 3D UI (`src/web/`)
- Data catalogs & specs (`docs/data/`, `data/stac/`)
- Domain analyses (`docs/analyses/`)
- Governance & standards (`docs/standards/`)
- CI/CD & infra (`.github/`)

If it’s `.md` in this repo, this protocol applies.

This version:

- **Makes the `fencing_profile: outer-backticks-inner-tildes-v1` normative** for AI-assisted authoring:
  docs copied from ChatGPT or similar tools **MUST**:
  - be provided as a **single outer ```markdown** fence in chat, and
  - use only **`~~~` (tildes) for all internal fenced blocks** in the actual file.
- Clarifies the **`🗂️ Directory Layout` profile** to prevent broken boxes and ensure emoji rendering:
  - directory trees are always fenced with `~~~text` and never use backtick fences.
- Adds explicit **secret- and PII-scan test profiles** for docs to align with KFM security policy.
- Tightens integration with **STAC 1.x**, **DCAT 3**, **PROV-O**, and **GeoSPARQL** for cataloging docs as
  first-class assets in the data + graph pipeline.
- Aligns Markdown with the **KFM core pipeline**:

  > Deterministic ETL → STAC/DCAT/PROV catalogs → Neo4j → API → React/MapLibre/Cesium → Story Nodes → Focus Mode

All downstream documentation patterns must extend this standard, **not override it**.

### 2. Core Principles

1. **Single Source of Truth** – This document is the authoritative reference for KFM Markdown structure and
   metadata.
2. **Documentation-First** – Code/data changes are incomplete without updated docs.
3. **Machine-Readable by Design** – Uniform front-matter + predictable headings + structured content.
4. **Human-Friendly Narrative** – Clear Purpose, logical sections, concise language, Kansas-context aware.
5. **Ethical & Sovereignty-Aware** – FAIR, CARE, and Indigenous data sovereignty baked into governance
   fields and CI checks.
6. **Predictable Layout** – `📘 Overview` then `🗂️ Directory Layout`, followed by other registered H2s, ending
   with `🕰️ Version History`.
7. **Pipeline-Native** – Every doc can be traced in ETL logs, STAC/DCAT catalogs, PROV provenance, Neo4j
   graph, and Story Node / Focus Mode views.

### 3. Author Quickstart (Human-Facing)

Before writing or editing any KFM Markdown:

1. **Start from a matching template**  
   Copy an existing doc with the same `doc_kind` under `docs/standards/`, `docs/guides/`, or the relevant
   domain directory.

2. **Update YAML front-matter**  
   - Set `title`, `path`, `version`, `last_updated`.
   - Ensure `governance_ref`, `ethics_ref`, `sovereignty_policy` are correct and **relative to the file**.
   - Set `doc_kind`, `status`, `review_cycle`, `classification`, `semantic_document_id`, and IDs (`doc_uuid`,
     `event_source_id`).
   - For event or data-spec docs, align IDs with the corresponding STAC Item and DCAT Dataset identifiers.

3. **Purpose block**  
   Under the H1, include a short **Purpose** paragraph explaining what the doc does and for whom. If the doc
   is event- or dataset-linked, mention those IDs.

4. **Use only approved H2 headings (with emojis)**  
   All H2s **must** be chosen from `heading_registry.approved_h2`, using the exact emoji + text.

5. **Keep ordering predictable (standards/guides)**  
   1. `📘 Overview`  
   2. `🗂️ Directory Layout`  
   3. Appropriate core sections (Context, Architecture, Governance, etc.)  
   4. `🕰️ Version History` last

6. **Close with Version History & footer**  
   - A `🕰️ Version History` table.  
   - Governance footer with links back to docs root, standards index, governance charter.

7. **Security & sovereignty**  
   - Never paste secrets, tokens, or credentials into docs.  
   - For sensitive sites (Indigenous, archaeological, endangered species), follow the sovereignty policy and
     use generalized or masked locations.

### 4. Author Quickstart (ChatGPT / AI Usage)

When using an AI assistant to create or update a KFM Markdown document:

1. **Explicitly request**:

   - A **YAML front-matter block** at the very top, matching this protocol.
   - H1/H2 headings from the **emoji-prefixed registry** (e.g., `## 📘 Overview`, `## 🗂️ Directory Layout`).
   - A `🗂️ Directory Layout` H2 as the **second section**, right after `📘 Overview`.
   - A directory tree under `🗂️ Directory Layout` that:
     - Uses emojis:
       - `📁` for directories  
       - `📄` for Markdown/text files  
       - `🧾` for JSON/YAML/log-like artifacts  
       - `🖼️` for images and visual assets  
       - `🧪` for tests where helpful
     - Uses `├──` / `└──` ASCII branches.
     - Is fenced as `~~~text` (**tildes, not backticks**).

2. **Fencing profile (outer-backticks-inner-tildes-v1)**  

   - The **assistant response** should wrap the **entire document** in a single outer fenced block of type
     `markdown`.
   - **Inside the document**, **all internal code blocks MUST use `~~~` fences**, for example:
     - `~~~text` for directory layouts  
     - `~~~bash` for shell commands  
     - `~~~mermaid` for diagrams  
     - `~~~json` / `~~~yaml` for config examples
   - **Internal fenced blocks MUST NOT use triple backticks**.  
     This prevents the “box break” where the inner ``` accidentally closes the outer fence in chat.

3. **After pasting into the repo**:

   - Remove the outer ` ```markdown` / closing ``` lines before committing the `.md` file.
   - Verify **relative paths** match reality.
   - Ensure `🗂️ Directory Layout` is present and second.
   - Run doc linting / CI locally where possible; otherwise rely on PR CI.

4. **Prohibited AI outputs in committed docs**:

   - Hidden governance changes or speculative architecture not backed by design docs.
   - Fabricated historical or scientific claims about Kansas or Indigenous communities.

---

## 🗂️ Directory Layout

The **canonical repository layout** uses the `immediate-one-branch-with-descriptions-and-emojis` profile.

Docs implementing this profile **MUST**:

- Show either:
  - the **full repo tree root** (`📁 Kansas-Frontier-Matrix/`) for global standards, or
  - a suitably scoped subtree for domain docs (e.g., `📁 docs/energy/`).
- Use the emoji + branch style consistently.
- Fence the tree with `~~~text` (tildes), never backticks.

Global root example (this file’s profile):

~~~text
📁 Kansas-Frontier-Matrix/
├── 📁 docs/                                  # All documentation
│   ├── 📁 standards/                         # Standards & policies (Markdown, FAIR+CARE, governance, etc.)
│   ├── 📁 architecture/                      # System designs (ETL → graph → API → UI → Story Nodes)
│   ├── 📁 guides/                            # How-to guides, tutorials, SOP-style walkthroughs
│   ├── 📁 data/                              # Data contracts, source registries, schema notes
│   ├── 📁 analyses/                          # Domain analyses (archaeology, hydrology, history, energy, etc.)
│   └── 📄 glossary.md                        # Shared glossary for KFM-wide terminology
├── 📁 src/                                   # Pipelines, graph services, APIs, web apps
│   ├── 📁 pipelines/                         # Deterministic ETL/ELT, orchestration, lineage emitters
│   ├── 📁 graph/                             # Neo4j schema, loaders, Cypher, GeoSPARQL views
│   ├── 📁 api/                               # REST/GraphQL gateways, auth, rate-limiting
│   ├── 📁 web/                               # React / MapLibre / Cesium frontends & Story Node UI
│   │   ├── 📁 app/                           # Main web app entrypoint
│   │   └── 📁 story-nodes/                   # Story Node layouts, Focus Mode views
│   └── 📁 tools/                             # Backend utilities, CLIs, migrations
├── 📁 data/                                  # Data lifecycle: raw → work → processed → releases
│   ├── 📁 sources/                           # External dataset manifests (STAC/DCAT-aligned)
│   ├── 📁 raw/                               # Raw ingested data (LFS/DVC; not committed)
│   ├── 📁 work/                              # Intermediate normalized / enriched data
│   ├── 📁 processed/                         # Production-ready assets (GeoJSON, COGs, CSVs, graph exports)
│   └── 📁 stac/                              # STAC Collections & Items indexing processed assets
├── 📁 schemas/                               # JSON, JSON-LD, STAC, DCAT, SHACL, telemetry schemas
│   ├── 🧾 json/                              # JSON schemas (docs, pipelines, Story Nodes, telemetry)
│   └── 🧾 telemetry/                         # Energy, carbon, lineage, metrics schemas
├── 📁 mcp/                                   # Master Coder Protocol artifacts & experiments
│   ├── 📁 experiments/                       # Experiment logs (timestamped, domain-tagged)
│   ├── 📁 model_cards/                       # Model documentation & evaluation cards
│   └── 📁 sops/                              # SOPs for ETL, modeling, deployment, incident response
├── 📁 tests/                                 # Unit, integration, contract, and UI tests
├── 📁 tools/                                 # Repo-level tools, dev utilities, maintenance scripts
├── 📁 .github/                               # CI/CD workflows & GitHub configuration
│   └── 📁 workflows/                         # CI pipelines (kfm-ci, docs-lint, lineage-audit, security)
└── 📄 README.md                              # High-level project overview
~~~

**Directory Layout rules (normative):**

- Every documented directory **SHOULD** have a `README.md` describing purpose and key files.
- Any new top-level directory **MUST** be added to this tree in the next MDP revision.
- All directory trees in docs:
  - **MUST** use this emoji style (`📁`, `📄`, `🧾`, `🖼️`, `🧪`) and branch characters.
  - **MUST** be fenced as `~~~text` blocks (tildes).
- For doc-specific trees, scope from the nearest meaningful root, e.g.:

  - `docs/energy/` for an energy spec.
  - `src/pipelines/` for an ETL guide.

- When using ChatGPT, always explicitly request **emoji-formatted directory layouts** under `🗂️ Directory Layout`.

---

## 🧭 Context

KFM-MDP v11.2.6 sits at the intersection of:

- **KFM-OP v11 (Ontology Protocol)** – ensures docs, datasets, and Story Nodes map cleanly to Neo4j with
  CIDOC-CRM, PROV-O, GeoSPARQL, and OWL-Time alignment.
- **MCP-DL v6.3 (Master Coder Protocol)** – documentation-first, reproducible experiments, and AI usage
  patterns.
- **Data catalog standards** – STAC, DCAT 3, and PROV-O for indexing docs as assets that participate in
  catalogs, provenance graphs, and STAC/OGC APIs.
- **Security & sovereignty policy** – SECURITY.md, FAIR+CARE guides, and Indigenous data protection docs
  govern what may be written, how it’s scanned, and how it’s cataloged.
- **Story Node & Focus Mode** – Markdown as a structured narrative layer over maps, graphs, and time.

This protocol makes Markdown a **first-class, cataloged, provenance-aware geospatial + narrative asset**, not
just commentary around the “real” data.

---

## 🗺️ Diagrams

Diagrams must be **governed, accessible, and machine-checkable**.

Allowed profiles:

- `mermaid-flowchart-v1`
- `mermaid-timeline-v1`

Rules:

- Diagrams live under `🗺️ Diagrams`, `🧱 Architecture`, or `🧪 Validation & CI/CD`.
- Each diagram has a short textual explanation for accessibility.
- Use Mermaid syntax in fenced blocks with tildes (e.g. `~~~mermaid`).
- Do not include secrets, internal URLs, or sensitive coordinates.

**Example flowchart**

~~~mermaid
flowchart LR
    A[Author drafts Markdown] --> B[CI: markdown-lint + schema-lint + secret-scan]
    B -->|Pass| C[Merge to main]
    B -->|Fail| D[Author fixes issues]
~~~

**Example timeline**

~~~mermaid
timeline
    title Markdown Protocol Evolution
    2023-11-10 : v10.4.3 : "Legacy markdown rules"
    2025-11-25 : v11.2.0 : "Front-matter & profile overhaul"
    2025-11-27 : v11.2.2 : "Heading registry & transform rules"
    2025-12-04 : v11.2.4 : "Semantic alignment & AI integration"
    2025-12-07 : v11.2.5 : "Emoji H2 + directory layout elevation"
    2025-12-10 : v11.2.6 : "Fencing profile, security scans, pipeline alignment"
~~~

Forbidden: ASCII art diagrams, unlabeled diagrams, or diagrams that reveal sensitive or governed details.

---

## 🧠 Story Node & Focus Mode Integration

Docs following KFM-MDP v11.2.6 are **Story Node ready**:

- H2 + H3 structure creates natural **Story Node segments** (e.g., `📘 Overview`, `🗂️ Directory Layout`,
  `🧱 Architecture`).
- Front-matter IDs (`doc_uuid`, `semantic_document_id`, `event_source_id`) allow Focus Mode and Story Nodes
  to anchor summaries and map views.
- `ai_transform_permissions` and `ai_transform_prohibited` codify what AI may do.

**Story Node targeting example**

~~~json
{
  "target": "kfm-markdown-protocol-v11.2.6",
  "segment": "🧪 Validation & CI/CD",
  "spatial_extent": null,
  "temporal_extent": {
    "start": "2025-11-25",
    "end": "2025-12-10"
  }
}
~~~

**Focus Mode MAY:**

- Summarize sections, extract constraints, highlight key requirements.
- Generate timeline views and Story Node cards for each H2/H3.

**Focus Mode MUST NOT:**

- Invent governance rules or override normative text.
- Generate fake citations or “hallucinated” Kansas history or Indigenous knowledge.

---

## 🧪 Validation & CI/CD

Markdown is part of the **critical CI/CD path**.

### Test profiles

From `test_profiles`:

| Profile              | Purpose                                             |
|----------------------|-----------------------------------------------------|
| markdown-lint        | Structural & style linting                          |
| schema-lint          | YAML front-matter schema validation                 |
| metadata-check       | Required metadata present & consistent              |
| diagram-check        | Mermaid syntax & profile check                      |
| accessibility-check  | Basic structural a11y checks (headings, lists)      |
| provenance-check     | `provenance_chain` & Version History alignment      |
| footer-check         | Footer & governance-links enforcement               |
| secret-scan          | Ensure no secrets/tokens are present                |
| pii-scan             | Detect and block obvious PII in docs                |

### H1/H2 rules

- Exactly **one H1** per file.
- H2 **must** come from `heading_registry.approved_h2` and include the emoji.
- Standard order (for standards/guides):
  1. `📘 Overview`
  2. `🗂️ Directory Layout`
  3. Other sections as needed
  4. `🕰️ Version History` last

Docs that omit `🗂️ Directory Layout` or place it later are **non-compliant** for standards/guides.

### YAML rules

- Front-matter is required, with no blank lines before `---`.
- Required fields per `doc_kind` must be present and correctly typed.
- Deprecated fields listed in `deprecated_fields` **MUST NOT** be used in new docs.

---

## 📦 Data & Metadata

This document is itself a **metadata-rich, cataloged asset**:

- Can be indexed as a DCAT `dcat:Dataset` / `dcat:CatalogRecord`.
- Can be represented as a STAC Item in a `kfm-docs` Collection.
- Behaves as a `prov:Plan` in the provenance graph.

Required metadata for `doc_kind: "Standard"` includes:

- Identity & versioning: `title`, `path`, `version`, `doc_uuid`, `semantic_document_id`, `event_source_id`.
- Governance & lifecycle: `status`, `release_stage`, `lifecycle`, `review_cycle`, `ttl_policy`, `sunset_policy`,
  `governance_ref`, `ethics_ref`, `sovereignty_policy`.
- Licensing & ethics: `license`, `fair_category`, `care_label`, `classification`, `sensitivity`,
  `indigenous_rights_flag`.
- Provenance & catalogs: `commit_sha`, `signature_ref`, `attestation_ref`, `sbom_ref`, `manifest_ref`,
  `telemetry_ref`, `telemetry_schema`, `energy_schema`, `carbon_schema`, `metadata_profiles`,
  `provenance_chain`, `doc_integrity_checksum`.
- AI behavior: `ai_focusmode_usage`, `ai_transform_permissions`, `ai_transform_prohibited`,
  `transform_registry`.

---

## 🌐 STAC, DCAT & PROV Alignment

**DCAT**

- `title` → `dct:title`  
- Purpose block → `dct:description`  
- `last_updated` → `dct:modified`  
- `doc_uuid` → `dct:identifier`  
- Markdown URL → `dcat:Distribution` with `mediaType: text/markdown`

Docs can participate in **DatasetSeries** (e.g., all MDP versions) with DCAT 3’s `dcat:DatasetSeries` and
versioning properties.

**STAC**

- Each doc can be a non-spatial STAC Item in a documentation Collection:
  - `id` = `semantic_document_id`
  - `properties.datetime` = `last_updated`
  - `assets.docs` for the Markdown file
- Collections can use `item_assets` to define doc asset fields.

**PROV-O**

- Each version of this doc is a `prov:Entity` with type `prov:Plan`.
- `provenance_chain` expresses `prov:wasDerivedFrom` between versions.
- Publication / CI runs are `prov:Activity` instances associated with Agents (teams, bots).

This alignment makes docs **first-class citizens** of the STAC/DCAT/PROV ecosystem used throughout KFM.

---

## 🧱 Architecture

From an architectural perspective, this standard:

1. **Defines the Markdown contract** for all ETL, graph, API, UI, Story Node, and governance modules.
2. **Feeds CI** – `.github/workflows/kfm-ci.yml` applies `test_profiles` to every changed `.md`.
3. **Supports documentation tooling & static sites**, where front-matter and heading registry drive navigation.
4. **Enables AI-safe consumption** via Focus Mode and Story Nodes, respecting `ai_transform_*` constraints.
5. **Connects to the knowledge graph** – every doc is a node in Neo4j, linked via PROV, DCAT, and STAC IDs.

Any change to this protocol **must**:

- Update this file, the JSON schema, and SHACL shapes.
- Adjust CI workflows if new checks are added.
- Bump `version`, `last_updated`, and add a new `🕰️ Version History` entry.
- Update STAC, DCAT, and Neo4j ingestion as needed for new metadata fields.

---

## ⚖ FAIR+CARE & Governance

This protocol encodes FAIR+CARE into documentation:

- **FAIR**
  - Findable: stable IDs, predictable paths, catalog entries.
  - Accessible: CC-BY license, public repo (with sovereignty exceptions).
  - Interoperable: STAC/DCAT/PROV-O, CIDOC, schema.org mappings.
  - Reusable: explicit versioning and provenance.

- **CARE**
  - Collective Benefit: open documentation that benefits communities.
  - Authority to Control: governance & sovereignty policies; `indigenous_rights_flag` drives review.
  - Responsibility: avoid exposing sensitive information (e.g., exact locations of protected sites).
  - Ethics: forbids speculative or misleading governance or historical claims.

`governance_ref`, `ethics_ref`, and `sovereignty_policy` are **normative** and must be followed when
authoring any doc.

---

## 🕰️ Version History

| Version     | Date       | Summary                                                                                                                                                                                                                                                      |
|------------:|-----------:|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **v11.2.6** | 2025-12-10 | Formalized `fencing_profile: outer-backticks-inner-tildes-v1`; locked in `~~~text` directory layouts to prevent “box break” in AI-generated docs; added secret- and PII-scan test profiles; strengthened STAC/DCAT/PROV integration and pipeline alignment for Story Nodes and Focus Mode. |
| **v11.2.5** | 2025-12-07 | Elevated `🗂️ Directory Layout` to second H2 for standards/guides; mandated emoji directory trees; updated heading registry to emoji-prefixed H2s; normalized relative paths for releases/schemas from `docs/standards/`; clarified ChatGPT usage requirements.                                      |
| v11.2.4     | 2025-12-04 | Added STAC/DCAT/PROV alignment section; extended Story Node & Focus Mode guidance; tightened CI enforcement and transform rules.                                                                                                                             |
| v11.2.3     | 2025-12-02 | Refined AI transform permissions and Focus Mode behaviors (no structural changes; internal alignment).                                                                                                                                                       |
| v11.2.2     | 2025-11-27 | Introduced heading registry; expanded metadata/provenance fields; unified YAML front-matter; hardened anti-pattern definitions.                                                                                                                             |
| v11.2.1     | 2025-11-26 | Added profile system; stronger provenance enforcement; stricter DCAT/STAC metadata requirements.                                                                                                                                                             |
| v11.2.0     | 2025-11-25 | Major overhaul for KFM v11, including header/footer profiles, CI test profiles, and diagram usage rules.                                                                                                                                                     |
| v11.0.1     | 2025-11-20 | Initial KFM v11 consolidation of markdown rules under unified ontology and governance.                                                                                                                                                                       |
| v10.4.3     | 2023-11-10 | Legacy markdown rules prior to KFM v11, defining basic front-matter and structural layout.                                                                                                                                                                   |

---

<div align="center">

📑 **Kansas Frontier Matrix — Markdown Authoring Protocol (KFM-MDP) v11.2.6**  
Scientific Insight · Documentation-First · FAIR+CARE Ethics · Sustainable Intelligence  

[📘 Docs Root](..) · [📂 Standards Index](./README.md) · [⚖ Governance Charter](../governance/ROOT-GOVERNANCE.md)

</div>