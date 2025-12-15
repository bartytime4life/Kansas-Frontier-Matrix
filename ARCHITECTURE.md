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
  - "layout-normalization"
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
    - layout-normalization
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

# 📑 **Kansas Frontier Matrix — Markdown Authoring Protocol (KFM-MDP) v11.2.6**
`docs/standards/kfm_markdown_protocol_v11.2.6.md`

**Purpose**  
Define the **canonical, enforceable Markdown authoring rules** for the Kansas Frontier Matrix (KFM).  
This protocol standardizes **structure, headings, metadata, and narrative patterns** so Markdown across the monorepo is **CI-safe, FAIR+CARE-aligned, semantically interoperable**, and ready for **Story Node / Focus Mode** integration.

<img src="https://img.shields.io/badge/MCP--DL-v6.3-blueviolet" />
<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/FAIR%2BCARE-Governance%20Aligned-orange" />
<img src="https://img.shields.io/badge/Accessibility-WCAG_2.1_AA%2B-blueviolet" />
<img src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />

</div>

---

## 📘 Overview

### 1. Scope and intent

KFM-MDP v11.2.6 governs **all Markdown files** in the Kansas Frontier Matrix monorepo (`Kansas-Frontier-Matrix`) across every domain:

- ETL / pipelines (`src/pipelines/`, `docs/pipelines/`)
- Graph / ontology (`src/graph/`, `docs/graph/`)
- Web UI (`web/`, `docs/design/`, `docs/accessibility/`)
- Data lifecycle & catalogs (`data/`, `docs/data/`, `data/stac/`)
- Governance & standards (`docs/standards/`, `docs/governance/`)
- CI/CD & infra docs (`.github/`, `docs/workflows/`)

If it’s `.md` in this repo, this protocol applies.

### 2. Absolute rules (normative)

1. **Front-matter is required**  
   Every governed KFM Markdown file MUST begin with YAML front-matter (`---` … `---`). No blank lines before the first `---`.

2. **Exactly one H1**  
   Each file MUST contain exactly one `#` heading.

3. **Approved H2 registry only**  
   Every H2 MUST match exactly one entry in `heading_registry.approved_h2` (emoji + text must match).

4. **Standards ordering is enforced**  
   Standards MUST place:
   - `## 📘 Overview` as the first H2
   - `## 🗂️ Directory Layout` as the second H2
   - `## 🕰️ Version History` as the final H2

5. **Chat-safe fencing profile is mandatory**  
   `fencing_profile: outer-backticks-inner-tildes-v1` is the default across KFM:
   - Outer fence (in chat / generated output): backticks
   - Inner code fences (inside documents): tildes (`~~~`)

6. **No secrets, no PII, no sensitive coordinates**  
   Markdown is scanned. Secrets and PII MUST NOT appear in docs.  
   Protected-site locations MUST be generalized and masked per sovereignty policy.

7. **Directory trees are standardized**  
   Directory trees MUST use:
   - Emoji markers: `📁` directories, `📄` files, `🧾` structured artifacts
   - ASCII branches: `├──`, `└──`, `│`
   - `~~~text` fence (tildes)

### 3. Core principles

1. **Single Source of Truth** – This document is the authoritative reference for KFM Markdown structure and metadata.
2. **Documentation-First** – Code/data changes are incomplete without updated docs.
3. **Machine-Readable by Design** – Uniform front-matter + predictable headings + structured content.
4. **Human-Friendly Narrative** – Clear purpose, logical sections, and concise language.
5. **Ethical & Sovereignty-Aware** – FAIR+CARE and Indigenous data sovereignty are encoded in metadata and enforced in review.
6. **Predictable Layout** – `📘 Overview` then `🗂️ Directory Layout`, ending with `🕰️ Version History`.

### 4. Author quickstart (human-facing)

1. Copy an existing doc with the same `doc_kind`.
2. Update YAML: `title`, `path`, `version`, `last_updated`, and governance/ethics/sovereignty refs.
3. Keep the second H2 as `🗂️ Directory Layout` for standards and guides.
4. Use only approved H2 headings from the registry.
5. Use `~~~` for all internal fenced blocks (`~~~yaml`, `~~~json`, `~~~bash`, `~~~mermaid`, `~~~text`).
6. Close with `🕰️ Version History` and a governance footer.

### 5. Author quickstart (AI usage)

When generating Markdown for KFM, request:

- YAML front-matter at top
- `## 📘 Overview` then `## 🗂️ Directory Layout` (second)
- Only registry H2 headings
- Internal fences are `~~~` (not backticks)
- No citations with tool-specific syntax, no hidden markup, no secrets

Recommended prompt:

> “Generate a KFM-compliant Markdown doc: YAML front-matter, H2 registry headings, `📘 Overview` then `🗂️ Directory Layout` with emoji tree, internal fences use `~~~`, end with `🕰️ Version History` + governance footer.”

---

## 🗂️ Directory Layout

Canonical monorepo layout (key directories and files):

~~~text
📁 Kansas-Frontier-Matrix/
├── 📄 README.md                                  # Root overview of the KFM system (v11)
├── 📄 ARCHITECTURE.md                            # High-level system & repository architecture
├── 📄 CONTRIBUTING.md                            # Contribution workflow (FAIR+CARE governed)
├── 📄 LICENSE                                    # Project license (code/docs licensing as specified)
│
├── 📁 .github/                                   # GitHub config + CI/CD
│   ├── 📁 ISSUE_TEMPLATE/                        # Issue templates
│   ├── 📁 actions/                               # Reusable composite actions
│   ├── 📁 workflows/                             # CI workflows (lint/tests/audits/build/deploy)
│   ├── 📄 ARCHITECTURE.md                        # CI/CD & GitHub infra architecture
│   ├── 📄 PULL_REQUEST_TEMPLATE.md               # PR checklist (governance & tests)
│   ├── 📄 README.md                              # .github overview
│   ├── 📄 SECURITY.md                            # Security policy (vuln reporting, etc.)
│   └── 🧾 dependabot.yml                          # Dependency update configuration
│
├── 📁 data/                                      # Data lifecycle + catalogs
│   ├── 📁 air-quality/                           # Air quality data sources & products
│   ├── 📁 archive/                               # Archived/deprecated datasets
│   ├── 📁 checksums/                             # Data integrity hashes
│   ├── 📁 hydrology/                             # Hydrology datasets/config
│   ├── 📁 processed/                             # Canonical processed outputs (final datasets)
│   ├── 📁 raw/                                   # Raw ingested inputs (DVC/LFS as applicable)
│   ├── 📁 reports/                               # Data QA/QC and summary reports
│   ├── 📁 stac/                                  # STAC Collections & Items (asset metadata)
│   ├── 📁 surficial-geology/                     # Surficial geology products
│   ├── 📁 updates/                               # Incremental update payloads
│   ├── 📁 work/                                  # Intermediate/working artifacts
│   ├── 📄 ARCHITECTURE.md                        # data/ architecture notes
│   └── 📄 README.md                              # data/ conventions
│
├── 📁 docs/                                      # Documentation (human + machine readable)
│   ├── 📁 accessibility/                         # A11y standards & audits
│   ├── 📁 analyses/                              # Domain analyses and case studies
│   ├── 📁 architecture/                          # System/subsystem design docs
│   ├── 📁 archives/                              # Archival/records documentation
│   ├── 📁 data/                                  # Data contracts, catalogs, schema notes
│   ├── 📁 design/                                # UX/UI design docs
│   ├── 📁 governance/                            # Governance charters, policies, processes
│   ├── 📁 graph/                                 # Ontology and graph modeling docs
│   ├── 📁 guides/                                # How-to guides and tutorials
│   ├── 📁 history/                               # Historical context and timelines
│   ├── 📁 pipelines/                             # Pipeline specs/runbooks/SOPs for ETL/AI workflows
│   ├── 📁 reports/                               # Generated reports and whitepapers
│   ├── 📁 search/                                # Search/indexing behavior docs
│   ├── 📁 security/                              # Security, supply-chain, hardening docs
│   ├── 📁 soil/                                  # Soil and terrain domain docs
│   ├── 📁 standards/                             # KFM standards and protocols
│   ├── 📁 telemetry/                             # Telemetry/observability standards
│   ├── 📁 templates/                             # Document and MCP templates
│   ├── 📁 workflows/                             # Human process/workflow documentation
│   ├── 📄 ARCHITECTURE.md                        # docs/ architecture overview
│   ├── 📄 MASTER_GUIDE_v10.md                    # Legacy KFM v10 master guide (archival)
│   ├── 📄 MASTER_GUIDE_v11.md                    # KFM v11 master guide (current)
│   ├── 📄 README.md                              # docs/ index
│   └── 📄 glossary.md                            # Shared glossary
│
├── 📁 mcp/                                       # Master Coder Protocol workspace
│   ├── 📁 experiments/                           # 🧪 Experiment logs and reproducible run records
│   ├── 📁 model_cards/                           # 🧾 AI/ML model cards (transparency reports)
│   ├── 📁 sops/                                  # 📋 Standard Operating Procedures
│   ├── 📄 MCP-README.md                          # MCP “bible” / core protocol reference
│   └── 📄 README.md                              # MCP workspace overview
│
├── 📁 schemas/                                   # Schema definitions
│   ├── 📁 json/                                  # JSON schemas (docs/pipelines/story nodes/telemetry)
│   └── 📁 telemetry/                             # Telemetry schemas (energy/carbon/lineage/metrics)
│
├── 📁 src/                                       # Backend services, pipelines, core logic
│   ├── 📁 ai/                                    # AI/ML logic and Focus Mode services
│   ├── 📁 design-tokens/                         # Shared design tokens
│   ├── 📁 graph/                                 # Neo4j schema/loaders/queries
│   ├── 📁 icons/                                 # Shared icon assets
│   ├── 📁 map/                                   # Geospatial utilities/helpers
│   ├── 📁 pipelines/                             # ETL and orchestration pipelines
│   ├── 📁 tests/                                 # Backend-focused tests
│   ├── 📁 theming/                               # Theming utilities
│   ├── 📄 ARCHITECTURE.md                        # src/ architecture overview
│   └── 📄 README.md                              # src/ overview
│
├── 📁 tests/                                     # Cross-cutting test suites
│   ├── 📁 fixtures/                              # Shared fixtures/sample data
│   ├── 📄 ARCHITECTURE.md                        # Testing architecture
│   └── 📄 README.md                              # Testing overview
│
├── 📁 tools/                                     # Tooling and utilities
│   ├── 📁 ai/                                    # AI evaluation and drift analysis tools
│   ├── 📁 ci/                                    # CI helper scripts/tools
│   ├── 📁 cli/                                   # Command-line utilities
│   ├── 📁 governance/                            # Governance automation (ledger syncing/compliance)
│   ├── 📁 telemetry/                             # Telemetry aggregation tools
│   ├── 📁 validation/                            # Data/metadata validators (STAC/DCAT/schema checks)
│   ├── 📄 ARCHITECTURE.md                        # Tools subsystem architecture notes
│   └── 📄 README.md                              # tools/ overview
│
├── 📁 web/                                       # Frontend web app (React + MapLibre + Cesium)
│   ├── 📁 public/                                # Static assets
│   ├── 📁 src/                                   # Frontend source code
│   ├── 📄 ARCHITECTURE.md                        # Frontend architecture
│   └── 📄 README.md                              # Frontend overview
│
└── 📁 releases/                                  # Certified release artifacts and provenance
    ├── 📁 v11.2.6/                               # Current release packet (when published)
    ├── 📁 v11.2.2/                               # Example release packet
    ├── 📁 v11.0.0/                               # Example release packet
    ├── 📁 v10.4.0/                               # Legacy release packet
    └── 📁 v10.2.0/                               # Legacy release packet
~~~

Directory layout rules (normative):

- Every documented directory SHOULD have a `README.md` describing purpose and key files.
- Any new top-level directory MUST be reflected in this tree.
- Trees MUST use `~~~text` and the emoji + branch conventions above.
- Avoid listing sensitive filenames/paths that reveal protected sources, credentials, or restricted-site locations.

---

## 🧭 Context

KFM-MDP v11.2.6 sits at the intersection of:

- **KFM-OP v11 (Ontology Protocol)** – aligns document entities to the graph’s semantic model.
- **MCP-DL v6.3** – enforces reproducibility norms and disciplined documentation.
- **STAC / DCAT / PROV-O** – standardizes discovery, distribution metadata, and lineage.
- **Story Nodes & Focus Mode** – uses Markdown as a structured narrative layer over data + graph + UI.

This protocol treats Markdown as a **first-class governed asset**: versioned, validated, cataloged, and provenance-aware.

---

## 🗺️ Diagrams

Diagrams are allowed but remain governed.

Allowed diagram profiles:

- `mermaid-flowchart-v1`
- `mermaid-timeline-v1`

Rules:

- Diagrams MUST live near relevant content (`🗺️ Diagrams`, `🧱 Architecture`, `🧪 Validation & CI/CD`).
- Each diagram MUST include a short text explanation for accessibility.
- Mermaid blocks MUST be fenced with `~~~mermaid`.

Example flowchart:

~~~mermaid
flowchart LR
  A[Author drafts Markdown] --> B[CI: lint + schema + governance checks]
  B -->|Pass| C[Merge to main]
  B -->|Fail| D[Fix issues and re-run CI]
~~~

Example timeline:

~~~mermaid
timeline
  title Markdown Protocol Evolution
  2023-11-10 : v10.4.3 : Legacy markdown rules
  2025-11-25 : v11.2.0 : v11 overhaul (profiles + CI enforcement)
  2025-12-07 : v11.2.5 : Directory Layout elevated + emoji H2 registry
  2025-12-12 : v11.2.6 : Fencing profile hardened + secret/PII scan enforced
~~~

Forbidden:

- ASCII art diagrams
- Diagrams containing secrets or credential-like strings
- Diagrams that reveal protected site coordinates

---

## 🧠 Story Node & Focus Mode Integration

Docs following KFM-MDP are **Story Node ready**:

- H2/H3 structure yields stable narrative segmentation.
- `doc_uuid` and `semantic_document_id` anchor Story Node targeting.
- `ai_transform_permissions` and `ai_transform_prohibited` codify safe usage.

Focus Mode MAY:

- Summarize sections (Overview, Directory Layout rules, etc.)
- Highlight requirements (heading registry, fencing profile, CI profiles)
- Extract metadata for indexing

Focus Mode MUST NOT:

- Invent new governance rules or alter normative statements
- Add speculative architecture claims
- Override sovereignty policy constraints

Example target pattern:

~~~json
{
  "target": "kfm-markdown-protocol-v11.2.6"
}
~~~

---

## 🧪 Validation & CI/CD

Markdown is CI-enforced.

### Test profiles

From `test_profiles`:

| Profile                 | Purpose |
|-------------------------|---------|
| `markdown-lint`         | Structural & style linting |
| `schema-lint`           | YAML front-matter schema validation |
| `metadata-check`        | Required metadata presence & consistency |
| `diagram-check`         | Mermaid syntax & profile check |
| `accessibility-check`   | Structural a11y checks |
| `provenance-check`      | Provenance chain + version history alignment |
| `footer-check`          | Governance footer link enforcement |
| `secret-scan`           | Detect leaked secrets/tokens/keys |
| `pii-scan`              | Detect PII in docs (policy-scoped) |

### Structural rules enforced

- Exactly one H1 per file.
- H2 headings must match registry entries exactly.
- Standards/guides: Directory Layout must be second; Version History last.
- Internal fences must use `~~~` (tildes) consistently.

---

## 📦 Data & Metadata

This standard is a metadata-rich asset.

### Required metadata (doc_kind: Standard)

- **Identity & versioning:** `title`, `path`, `version`, `last_updated`, `doc_uuid`, `semantic_document_id`, `event_source_id`
- **Lifecycle & governance:** `status`, `release_stage`, `review_cycle`, `ttl_policy`, `sunset_policy`, `governance_ref`, `ethics_ref`, `sovereignty_policy`
- **Integrity & provenance:** `commit_sha`, `signature_ref`, `attestation_ref`, `sbom_ref`, `manifest_ref`, `telemetry_ref`, `provenance_chain`, `doc_integrity_checksum`
- **AI constraints:** `ai_transform_permissions`, `ai_transform_prohibited`, `transform_registry`
- **Validation hooks:** `json_schema_ref`, `shape_schema_ref`, `test_profiles`

---

## 🌐 STAC, DCAT & PROV Alignment

### DCAT mapping

- `title` → `dct:title`
- Purpose text → `dct:description`
- `last_updated` → `dct:modified`
- `doc_uuid` → `dct:identifier`
- Markdown distribution → `dcat:Distribution` (`mediaType: text/markdown`)

### STAC mapping

Represent as a non-spatial Item in a documentation Collection:

- `id` = `semantic_document_id`
- `properties.datetime` = `last_updated`
- Asset link for the Markdown file

### PROV-O mapping

- Each version is a `prov:Entity`
- This standard is a `prov:Plan`
- `provenance_chain` defines `prov:wasDerivedFrom` edges across versions
- Governance councils and CI workflows act as `prov:Agent` and `prov:Activity` participants

---

## 🧱 Architecture

Architecturally, KFM-MDP:

1. Defines the Markdown contract for all domains (docs, pipelines, standards, runbooks).
2. Feeds CI enforcement via `.github/workflows/kfm-ci.yml`.
3. Enables catalog ingestion (DCAT/STAC) and provenance linking (PROV-O).
4. Supports Story Nodes / Focus Mode as a structured narrative interface.

Any change to this protocol MUST:

- Bump `version` and `last_updated`
- Update `telemetry_schema`, JSON schema, and SHACL shape references as applicable
- Add a Version History entry describing deltas
- Remain compatible with CI enforcement expectations

---

## ⚖ FAIR+CARE & Governance

This protocol encodes FAIR+CARE into documentation practice.

- **Findable:** stable paths + identifiers + catalogs
- **Accessible:** explicit licensing and governed public exposure risk
- **Interoperable:** STAC/DCAT/PROV alignment + ontology mappings
- **Reusable:** explicit versioning + provenance chain + validation profiles

CARE constraints apply across all docs:

- Avoid disclosure of protected or culturally sensitive site locations
- Respect sovereignty policy requirements and review triggers
- Keep governance claims evidence-led and reviewable

---

## 🕰️ Version History

| Version     | Date       | Summary |
|------------:|-----------:|---------|
| **v11.2.6** | 2025-12-12 | Enforced `outer-backticks-inner-tildes-v1` fencing profile; expanded CI profiles to include `secret-scan` and `pii-scan`; clarified absolute rules; preserved emoji H2 registry and Directory Layout ordering; reinforced governance and sovereignty constraints. |
| v11.2.5     | 2025-12-07 | Elevated `🗂️ Directory Layout` to second H2 for standards/guides; mandated emoji directory trees; updated heading registry to emoji-prefixed H2s; normalized relative paths for standards. |
| v11.2.4     | 2025-12-04 | Added STAC/DCAT/PROV alignment section; extended Story Node & Focus Mode guidance; tightened CI enforcement and transform rules. |
| v11.2.3     | 2025-12-02 | Refined AI transform permissions and Focus Mode behaviors (no structural changes; internal alignment). |
| v11.2.2     | 2025-11-27 | Introduced heading registry; expanded metadata/provenance fields; unified YAML front-matter; hardened anti-pattern definitions. |
| v11.2.1     | 2025-11-26 | Added profile system; stronger provenance enforcement; stricter DCAT/STAC metadata requirements. |
| v11.2.0     | 2025-11-25 | Major overhaul for KFM v11, including header/footer profiles, CI test profiles, and diagram usage rules. |
| v11.0.1     | 2025-11-20 | Initial KFM v11 consolidation of markdown rules under unified ontology and governance. |
| v10.4.3     | 2023-11-10 | Legacy markdown rules prior to KFM v11, defining basic front-matter and structural layout. |

---

<div align="center">

📑 **Kansas Frontier Matrix — Markdown Authoring Protocol (KFM-MDP) v11.2.6**  
Scientific Insight · Documentation-First · FAIR+CARE Ethics · Sustainable Intelligence

[📘 Docs Root](..) · [📂 Standards Index](./README.md) · [⚖ Governance Charter](governance/ROOT-GOVERNANCE.md)

</div>