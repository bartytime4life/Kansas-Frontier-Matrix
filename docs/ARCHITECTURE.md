---
title: "📚 Kansas Frontier Matrix — Documentation System Architecture (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/ARCHITECTURE.md"
version: "v11.2.6"
last_updated: "2025-12-11"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Autonomous · FAIR+CARE Council Oversight"
content_stability: "stable"

status: "Active / Enforced"
doc_kind: "Architecture"
intent: "docs-system-architecture"
header_profile: "standard"
footer_profile: "standard"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
signature_ref: "../releases/v11.2.6/signature.sig"
attestation_ref: "../releases/v11.2.6/slsa-attestation.json"
sbom_ref: "../releases/v11.2.6/sbom.spdx.json"
manifest_ref: "../releases/v11.2.6/manifest.zip"
telemetry_ref: "../releases/v11.2.6/focus-telemetry.json"
telemetry_schema: "../schemas/telemetry/docs-architecture-v1.json"
energy_schema: "../schemas/telemetry/energy-v2.json"
carbon_schema: "../schemas/telemetry/carbon-v2.json"

governance_ref: "standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

fair_category: "F1-A1-I1-R1"
care_label: "Public / Low-Risk"
sensitivity: "General (non-sensitive; auto-mask rules apply)"
sensitivity_level: "None"
public_exposure_risk: "Low"
classification: "Public Document"
jurisdiction: "Kansas / United States"
indigenous_rights_flag: false
risk_category: "Low"
redaction_required: false

ontology_alignment:
  cidoc: "E31 Document"
  schema_org: "CreativeWorkSeries"
  owl_time: "TemporalEntity"
  prov_o: "prov:Plan"

metadata_profiles:
  - "STAC 1.0.0"
  - "DCAT 3.0"
  - "PROV-O"
  - "FAIR+CARE"

json_schema_ref: "../schemas/json/docs-architecture.schema.json"
shape_schema_ref: "../schemas/shacl/docs-architecture-shape.ttl"

provenance_chain:
  - "docs/ARCHITECTURE.md@v11.2.6"
  - "docs/ARCHITECTURE.md@v10.4.0"
  - "docs/ARCHITECTURE.md@v10.3.2"
  - "docs/ARCHITECTURE.md@v10.0.0"

provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: true

doc_uuid: "urn:kfm:doc:docs-architecture:v11.2.6"
semantic_document_id: "kfm-doc-docs-architecture-v11.2.6"
event_source_id: "ledger:docs/ARCHITECTURE.md"
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summary"
  - "semantic-highlighting"
  - "a11y-adaptations"
ai_transform_prohibited:
  - "speculative-additions"
  - "unverified-historical-claims"
  - "governance-override"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"

heading_registry:
  approved_h2:
    - "📘 Overview"
    - "🗂️ Directory Layout"
    - "🧭 Context"
    - "🧱 Architecture"
    - "🌐 STAC, DCAT & PROV Alignment"
    - "⚖ FAIR+CARE & Governance"
    - "🧪 Validation & CI/CD"
    - "🕰️ Version History"

test_profiles:
  - "markdown-lint"
  - "schema-lint"
  - "metadata-check"
  - "provenance-check"
  - "footer-check"
  - "accessibility-check"

ci_integration:
  workflow: ".github/workflows/kfm-ci.yml"
  environment: "dev → staging → production"

branding_registry:
  standard: "Scientific Insight × FAIR+CARE Ethics × Sustainable Intelligence"
  architecture: "Docs as a First-Class System · Governed for Integrity"

layout_profiles:
  - "immediate-one-branch-with-descriptions-and-emojis"

badge_profiles:
  - "root-centered-badge-row"

ttl_policy: "Annual review"
sunset_policy: "Superseded upon next major documentation platform release"
---

<div align="center">

# 📚 **Kansas Frontier Matrix — Documentation System Architecture**  
`docs/ARCHITECTURE.md`

**Purpose**  
Define the **complete architecture of the documentation system** for the Kansas Frontier Matrix (KFM):  
Markdown governance, knowledge organization, FAIR+CARE alignment, schema-driven authoring, telemetry awareness,  
and version-pinned reproducibility across all documentation modules.

</div>

---

## 📘 Overview

The KFM documentation system is a **schema-governed, FAIR+CARE-certified, accessibility-first** subsystem that provides:

- Project-wide documentation under `docs/**`  
- Architecture specifications (system, web, data, pipelines, governance)  
- Standards and policies (Markdown rules, A11y, governance, sovereignty)  
- Reports, audits, provenance logs, FAIR+CARE assessments  
- STAC/DCAT documentation and data-domain READMEs  
- Pipeline, telemetry, and dataset documentation  
- Frontend & backend API documentation  
- Tutorials, onboarding guides, SOPs, and experiment/model templates  

Every document in `docs/**`:

- MUST follow **KFM‑MDP v11.2.6**  
- MUST include YAML front-matter validated by JSON/SHACL schemas  
- MUST be accessible (WCAG 2.1 AA or better)  
- MUST be machine-extractable (structured headings, stable IDs, clear metadata)  
- MUST be version-pinned and appear in SBOM + manifest metadata  
- MUST generate governance traces (provenance & CARE alignment) via telemetry

Documentation is treated as a **first-class system** with its own architecture, CI/CD, and governance.

---

## 🗂️ Directory Layout

Canonical high-level layout for the documentation subsystem (see `docs/README.md` for a broader index):

~~~text
📁 docs/
├── 📄 README.md                          # Documentation home & index
├── 📄 ARCHITECTURE.md                   # Documentation system architecture (this file)
│
├── 📁 standards/                        # Governance, Markdown, ontology, security, FAIR+CARE
│   ├── 📄 kfm_markdown_protocol_v11.2.6.md
│   ├── 📁 governance/
│   │   └── 📄 ROOT-GOVERNANCE.md
│   ├── 📁 faircare/
│   ├── 📁 sovereignty/
│   └── 📁 heritage/
│
├── 📁 templates/                        # Core Markdown + experiment/model/SOP/workflow templates
│   ├── 📄 kfm-markdown-template.md
│   ├── 📄 experiment.md
│   ├── 📄 model_card.md
│   ├── 📄 sop.md
│   └── 📄 workflow_template.md
│
├── 📁 architecture/                     # System, data, API, UI, and graph architecture docs
│   ├── 📄 README.md
│   ├── 📄 system-architecture.md
│   ├── 📄 data-architecture.md
│   ├── 📄 api-architecture.md
│   └── 📄 focus-mode-architecture.md
│
├── 📁 data/                             # Data-domain READMEs (soil, air, hydro, etc.)
│   ├── 📄 README.md
│   ├── 📁 soil/
│   ├── 📁 air/
│   ├── 📁 hydrology/
│   └── 📁 remote-sensing/
│
├── 📁 pipelines/                        # Pipeline, autonomy, and reliability docs
│   ├── 📄 README.md
│   ├── 📁 autonomy-matrix/
│   ├── 📁 reliability/
│   └── 📁 validation-observability/
│
├── 📁 telemetry/                        # Telemetry & observability docs
│   ├── 📄 README.md
│   └── 📁 correlation/
│
├── 📁 reports/                          # FAIR+CARE, audits, validation & governance ledgers
│   ├── 📁 audit/
│   ├── 📁 faircare/
│   └── 📁 self-validation/
│
├── 📁 analyses/                         # Thematic/domain analyses built on KFM data
│   ├── 📁 hydrology/
│   ├── 📁 remote-sensing/
│   ├── 📁 archaeology/
│   └── 📁 history/
│
├── 📁 references/                       # External dataset & research reference summaries
│   ├── 📁 datasets/
│   └── 📁 research/
└── 📄 glossary.md                       # Project-wide glossary & terminology index
~~~

Directory layout rules:

- Use `📁` for directories, `📄` for Markdown/text, `🧾` for JSON/YAML, `🧪` for tests, `🖼️` for images.  
- Use `~~~text` fences for trees (per `fencing_profile: outer-backticks-inner-tildes-v1`).  
- Keep comments short and implementation-focused (what this path is for, not long prose).

---

## 🧭 Context

The documentation subsystem sits alongside code and data as a **governed surface**:

- It encodes:
  - KFM’s **contracts** (Markdown, ontology, pipeline, telemetry).  
  - **Plans and procedures** (SOPs, workflows, governance).  
  - **Narrative layers** (Story Nodes, Focus Mode behavior, analyses).  

- It integrates tightly with the canonical pipeline:

  > Deterministic ETL → STAC/DCAT/PROV catalogs → Neo4j → API → React/MapLibre/Cesium → Story Nodes → Focus Mode

Documentation is:

- The **specification layer** for each of those components.  
- A **data source** for the knowledge graph (via doc catalogs and PROV).  
- A **governance artifact** with telemetry, SBOMs, signatures, and attestations.  

No pipeline, dataset, or model is considered “governed” without corresponding documentation anchored in `docs/**`.

---

## 🧱 Architecture

The documentation system follows a layered architecture.

### 1. Governance & Policy Layer

Defines what “valid documentation” means:

- **Markdown structural rules** — KFM‑MDP v11.2.6:
  - YAML front-matter in canonical order.  
  - Emoji-prefixed H2 registry.  
  - Single H1 per file.  
  - Standardized directory layouts and governance footer.

- **Governance policies**:
  - `standards/governance/ROOT-GOVERNANCE.md` as root charter.  
  - FAIR+CARE and sovereignty standards (`standards/faircare/`, `standards/sovereignty/`).  
  - Heritage protection standards (`standards/heritage/`).

- **Versioning rules**:
  - All docs version-pinned via `version`, `doc_uuid`, `semantic_document_id`.  
  - Provenance requirements encoded in front-matter.

### 2. Schema Layer

Schema-driven enforcement for everything under `docs/**`:

- **JSON Schemas** (`schemas/json/`):
  - Front-matter profiles for:
    - Monorepo overview, docs architecture, templates.  
    - Domain READMEs, events, advisories, telemetry docs.

- **SHACL Shapes** (`schemas/shacl/`):
  - Constraints for how doc metadata appears when projected into the graph.

- **Ontology mappings**:
  - Documentation files modeled as `cidoc:E31 Document`, `prov:Plan` or `prov:Collection`.  
  - Linked to datasets, pipelines, and models via PROV-O and CIDOC-CRM relations.

Schemas make docs **lintable, testable, and graph-loadable**.

### 3. Content Layer

The visible content of `docs/**`:

- Architecture specs (this file, data/API/Fous Mode architecture).  
- Standards and protocols (Markdown, ontology, STAC/DCAT profiles).  
- Templates (experiment, model card, SOP, workflow).  
- Domain documentation (soil, air, hydrology, remote sensing, heritage).  
- Reports (FAIR+CARE, audits, validation).  
- Tutorials, guides, and onboarding materials.

Content is designed to be:

- **Modular** (clear H2/H3 decomposition).  
- **Scope-bounded** (each doc has well-defined intent).  
- **Composable** (Story Nodes and Focus Mode can reuse sections safely).

### 4. Semantic & Machine-Extractability Layer

Ensures docs are consumable by tools, not just humans:

- **Heading conventions**:
  - Approved H2 registry (Overview, Directory Layout, Context, Architecture, etc.).  
  - H3/H4 structured for extraction (Objective, Methodology, Results, Governance, etc.).

- **Stable identifiers**:
  - `doc_uuid`, `semantic_document_id`, `event_source_id`.  
  - Consistent path naming.

- **Cross-document links**:
  - Relative links (no hard-coded domains).  
  - Glossary terms reused consistently across docs.

Docs become a **semantic corpus** that can be indexed, graphed, and surfaced in Focus Mode.

### 5. Telemetry & Observability Layer

Documentation changes and usage emit telemetry:

- Per-release telemetry (e.g., `../releases/v11.2.6/focus-telemetry.json`):
  - Counts and categories of docs changed.  
  - Lint and validation status.  
  - Accessibility and governance results.

- **Correlation with reliability & sustainability**:
  - Documentation workflows appear in CI telemetry (energy, CO₂e, retry behavior).  
  - Docs associated with pipeline runs and governance events.

Telemetry makes documentation **observable** and **auditable** like any other system.

### 6. Rendering & Consumption Layer

Docs are consumed by:

- GitHub’s Markdown renderer (source-of-truth view).  
- Static sites or portals (if configured).  
- Developer tooling and IDE integrations.  
- Focus Mode and Story Nodes (read-only, governed transformations).

Rendering rules:

- No documentation behavior relies on non-standard Markdown features not supported in the main consumption environments.  
- A11y-first: headings, lists, and tables must be screen-reader-friendly.

### 7. Authoring Rules (KFM‑MDP v11.2.6)

Authoring constraints for `docs/**`:

- **Front-matter**:
  - Required fields as defined in KFM‑MDP v11.2.6 and document-specific schemas.  
  - No blank lines before `---`.

- **Structure**:
  - Exactly one H1.  
  - H2 headings must come from the approved registry for this doc.  
  - Directory layouts under `🗂️ Directory Layout` use emoji + ASCII trees.

- **Generation via AI assistants**:
  - Single fenced `markdown` block when produced in chat tools.  
  - Inner fences use tildes (`~~~`) to avoid nesting issues.  
  - No speculative governance text; normative rules must come from standards docs.

---

## 🌐 STAC, DCAT & PROV Alignment

Even though this is “just docs,” the documentation subsystem is cataloged like data.

### STAC

- Documentation can be represented as **non-spatial STAC Items** in a `kfm-docs` Collection:
  - `id` = `semantic_document_id`.  
  - `properties.datetime` = `last_updated`.  
  - `assets.docs` = canonical Markdown URL.

- Links from data Collections to relevant documentation:
  - Data architecture docs linked from domain Collections.  
  - Heritage standards linked from sensitive heritage Collections.

### DCAT

- Documentation catalogs modeled as `dcat:Catalog`:
  - `docs/README.md` as high-level catalog record.  
  - Standards, architecture, templates as `dcat:Dataset` + `dcat:Distribution` (Markdown).

- Fields:
  - `dct:title` ← `title`.  
  - `dct:description` ← Overview section.  
  - `dct:modified` ← `last_updated`.  
  - `dct:identifier` ← `doc_uuid`.

### PROV-O

- Each version of this file is a `prov:Entity` with type `prov:Plan`.  
- `provenance_chain` expresses `prov:wasRevisionOf` or `prov:wasDerivedFrom`.  
- CI workflows and human edits are `prov:Activity` instances with:
  - `prov:used` (prior version, schemas).  
  - `prov:generated` (new doc version, telemetry).  
  - `prov:wasAssociatedWith` (agents: CI + maintainers).

This alignment allows documentation to participate fully in provenance queries.

---

## ⚖ FAIR+CARE & Governance

The documentation architecture embeds FAIR+CARE into authoring and review.

- **FAIR**:
  - **Findable** — predictable paths, stable identifiers, indexed in catalogs and search.  
  - **Accessible** — open licenses (MIT, CC‑BY), WCAG-compliant structure.  
  - **Interoperable** — consistent metadata, ontology mappings, and schemas.  
  - **Reusable** — version history, provenance, clear scope, and documented limitations.

- **CARE**:
  - Documentation about sensitive topics must:
    - Reference relevant governance and sovereignty docs.  
    - Use precise but non-harmful language.  
    - Avoid exposing sensitive coordinates or personal data.  

- **Governance integration**:
  - Docs about heritage, Indigenous knowledge, or sensitive data:
    - Flag `indigenous_rights_flag` and related fields appropriately.  
    - Are subject to FAIR+CARE Council review.  

This file itself is governed:

- Changes are tracked via `provenance_chain` and Version History.  
- AI tools and Focus Mode are constrained by the definitions and rules described here and in referenced standards.

---

## 🧪 Validation & CI/CD

The documentation system is wired into CI/CD via `.github/workflows/kfm-ci.yml`.

Key checks applied to `docs/**`:

- **markdown-lint** — structural rules (H1/H2, spacing, heading order, fenced blocks).  
- **schema-lint** — front-matter validation against `docs-architecture.schema.json` and related schemas.  
- **metadata-check** — presence and formatting of governance, classification, and licensing fields.  
- **provenance-check** — `provenance_chain` consistency vs. Version History.  
- **accessibility-check** — headings, tables, and link text sanity.  
- **footer-check** — governance footer presence and correctness.

Expected artifacts:

- `reports/self-validation/docs/lint_summary.json`  
- `reports/self-validation/docs/metadata_summary.json`  
- `reports/self-validation/docs/provenance_summary.json`  

Any documentation change that fails these checks is treated like a failing code change: it **blocks merge** until corrected.

---

## 🕰️ Version History

| Version   | Date       | Author        | Summary                                                                                           |
|----------:|------------|---------------|---------------------------------------------------------------------------------------------------|
| **v11.2.6** | 2025-12-11 | KFM Docs Team | Upgraded to KFM‑MDP v11.2.6; aligned front‑matter, H2 registry, and telemetry paths; clarified STAC/DCAT/PROV alignment and CI integration for docs as a first‑class subsystem. |
| v10.4.0  | 2025-11-15 | KFM Docs Team | Defined full documentation system architecture for KFM v10.4; introduced telemetry-aware docs stack. |
| v10.3.2  | 2025-11-14 | KFM Docs Team | Extended schema layer and provenance integration; tightened governance references.                |
| v10.0.0  | 2025-11-10 | KFM Core Team | Initial documentation architecture for KFM v10; established docs/ as a governed subsystem.        |

---

<div align="center">

📚 **Kansas Frontier Matrix — Documentation System Architecture (v11.2.6)**  
Docs as Infrastructure · FAIR+CARE Governance · Catalog & Graph Ready  

[📘 Docs Root](./README.md) ·  
[📚 Markdown Protocol (KFM‑MDP v11.2.6)](standards/kfm_markdown_protocol_v11.2.6.md) ·  
[⚖ Governance Charter](standards/governance/ROOT-GOVERNANCE.md)

</div>