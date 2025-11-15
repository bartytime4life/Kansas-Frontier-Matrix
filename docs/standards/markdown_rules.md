---
title: "📑 Kansas Frontier Matrix — Markdown Structural & Formatting Rules (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/standards/markdown_rules.md"
version: "v10.4.0"
last_updated: "2025-11-14"
review_cycle: "Annual / Autonomous · FAIR+CARE Council Oversight"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../releases/v10.4.0/sbom.spdx.json"
manifest_ref: "../../releases/v10.4.0/manifest.zip"
telemetry_ref: "../../releases/v10.4.0/focus-telemetry.json"
telemetry_schema: "../../schemas/telemetry/docs-markdown-rules-v3.json"
governance_ref: "governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4"
status: "Active / Enforced"
doc_kind: "Standard"
intent: "policy"
fair_category: "F1-A1-I1-R1"
care_label: "Public / Low-Risk"
sensitivity_level: "None"
public_exposure_risk: "Low"
indigenous_rights_flag: false
data_steward: "KFM FAIR+CARE Council"
risk_category: "Low"
redaction_required: false
provenance_chain:
  - "docs/standards/markdown_rules.md@v1.0"
  - "docs/standards/markdown_rules.md@v10.2"
ontology_alignment:
  cidoc: "E31 Document"
  schema_org: "TechArticle"
  owl_time: "TemporalEntity"
  prov_o: "prov:Entity"
  geosparql: "N/A"
shape_schema_ref: "../../schemas/shacl/docs-markdown-rules-shape.ttl"
json_schema_ref: "../../schemas/json/docs-markdown-rules.schema.json"
doc_uuid: "urn:kfm:doc:markdown-rules-v10.4.0"
semantic_document_id: "kfm-doc-markdown-rules"
event_source_id: "ledger:docs/standards/markdown_rules.md"
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"
ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summaries"
  - "semantic-highlighting"
ai_transform_prohibited:
  - "speculative additions"
  - "unverified historical claims"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
jurisdiction: "Kansas / United States"
classification: "Public Document"
role: "policy"
lifecycle_stage: "stable"
ttl_policy: "Review required every 12 months"
sunset_policy: "Superseded upon new protocol release"
---

<div align="center">

# 📑 **Kansas Frontier Matrix — Markdown Structural & Formatting Rules**  
`docs/standards/markdown_rules.md`

**Purpose:**  
Define the *authoritative and enforceable* Markdown standard for all Kansas Frontier Matrix (KFM) documentation.  
This specification guarantees MCP-DL v6.3 compliance, FAIR+CARE validation, ontology alignment, reproducibility,  
machine readability, Story Node compatibility, Focus Mode v2 integration, and full CI/CD enforcement.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP_v6.3-blue)](../README.md)  
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../LICENSE)  
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Certified-orange)](faircare.md)  
[![Status: Enforced](https://img.shields.io/badge/Status-Enforced-success)]()

</div>

---

## 📘 Overview

The Kansas Frontier Matrix Markdown Rules define the **mandatory, non-negotiable protocol** governing all  
KFM documentation. **Any Markdown file that does not fully comply is rejected by CI/CD.**

All documents must pass:

- `make docs-validate`
- `docs-lint.yml`
- `markdown-validate.yml`
- `schema-check.yml`
- `stac-validate.yml`
- FAIR+CARE classifier
- MCPLint v10.4+
- Broken link detector
- JSON/YAML/Turtle/RDF validators
- Accessibility linter (WCAG 2.1 AA)
- Governance chain validator
- Telemetry schema validator

---

# 🧱 YAML Front-Matter Specification (Extended)

Every KFM Markdown MUST begin with a **complete YAML front-matter block** with *no blank lines above it*.

### 🔒 Required YAML Fields (FULL SET)

| Category            | Fields (ALL Required) |
|---------------------|------------------------|
| Metadata            | `title`, `path`, `version`, `last_updated`, `review_cycle`, `commit_sha`, `license` |
| Release Artifacts   | `sbom_ref`, `manifest_ref` |
| Telemetry           | `telemetry_ref`, `telemetry_schema` |
| Governance          | `governance_ref`, `status`, `doc_kind`, `intent`, `lifecycle_stage` |
| Ethical Compliance  | `fair_category`, `care_label`, `sensitivity_level`, `public_exposure_risk`, `indigenous_rights_flag`, `data_steward`, `risk_category`, `redaction_required` |
| Provenance          | `provenance_chain`, `previous_version_hash` (if incremental) |
| Identification      | `doc_uuid`, `semantic_document_id`, `event_source_id` |
| Schemas             | `markdown_protocol_version`, `ontology_alignment`, `json_schema_ref`, `shape_schema_ref` |
| AI Controls         | `ai_training_inclusion`, `ai_focusmode_usage`, `ai_transform_permissions`, `ai_transform_prohibited` |
| Technical           | `machine_extractable`, `accessibility_compliance`, `jurisdiction`, `role` |
| Security            | `doc_integrity_checksum`, `immutability_status` |
| Lifecycle           | `ttl_policy`, `sunset_policy` |

> ⚠️ Missing **any** required field = **automatic CI rejection**.

---

# 🧩 Centered Title Block Specification

~~~~~markdown
<div align="center">

# 🧩 **Document Title**  
`path/to/file.md`

**Purpose:**  
A precise 1–3 sentence summary of document intent.

[![Docs · MCP](...)](...)
[![License: CC-BY 4.0](...)](...)
[![FAIR+CARE](...)](...)
[![Status: Enforced](...)]()

</div>
~~~~~

### Title Block Rules

- MUST follow YAML immediately (**no blank lines** in between).  
- MUST be wrapped in `<div align="center">`.  
- MUST contain:
  - H1 title with emoji.  
  - File path in backticks.  
  - Purpose paragraph.  
  - Standard badge order:

    1. Docs · MCP  
    2. License  
    3. FAIR+CARE  
    4. Status  

- MUST be followed by:
  - Exactly one blank line.  
  - A horizontal rule (`---`).  

---

# 🧱 Section Order (Strict)

ALL documents must follow this exact layout:

1. YAML front-matter  
2. Centered Title Block  
3. `---` (horizontal rule)  
4. Overview  
5. Purpose  
6. Scope  
7. Definitions  
8. Architecture / Context  
9. Procedures / Implementation  
10. Data Contracts & Schemas  
11. Ontology Alignment  
12. STAC/DCAT Metadata  
13. Story Node Integration  
14. Focus Mode Integration  
15. Ethics & CARE  
16. Governance  
17. Validation & Testing  
18. Telemetry  
19. Accessibility  
20. Machine Extractability  
21. Privacy & Security  
22. Dataset Evolution / Deltas  
23. Error Taxonomy  
24. Directory Layout  
25. Version History  
26. Footer  

ANY deviation = **CI failure**.

---

# 🎯 Purpose

Every document MUST include an explicit **Purpose** section that:

- Clearly states **why** the document exists.  
- Identifies the **primary consumers** (e.g., developers, FAIR+CARE Council, public users).  
- Links purpose to **MCP-DL v6.3** and **KFM governance**.

---

# 📍 Scope

The Scope section MUST:

- Define **In Scope** items (topics, components, processes).  
- Define **Out of Scope** items (explicitly).  
- Reference related documents when boundaries intersect (e.g., `src/ARCHITECTURE.md`, `docs/standards/*`).  

---

# 📚 Definitions (Mandatory)

Documents MUST include a **Definitions / Glossary** section that:

- Defines all non-trivial terms introduced in the document.  
- Aligns with:
  - KFM project glossary  
  - MCP-DL glossary  
  - Domain-specific glossaries (e.g., archaeology, geology, climatology)  
- Marks any **new terms** that should be propagated back into the global glossary.

---

# 🏗 Architecture / Context

Architecture-oriented docs MUST:

- Provide a **contextual diagram** (Mermaid recommended).  
- Explain how the component fits into:
  - KFM monorepo structure  
  - ETL/AI pipelines  
  - Knowledge graph  
  - Web UI / Focus Mode / Story Nodes  

- Reference `src/ARCHITECTURE.md` and other relevant files.

Example diagram:

~~~~~mermaid
flowchart LR
  A["Component A"] --> B["Component B"]
  B --> C["Component C"]
~~~~~

---

# ⚙️ Procedures / Implementation

Procedural or implementation docs MUST:

- Describe **step-by-step operations**.  
- Indicate **preconditions** and **postconditions**.  
- Distinguish between:
  - Manual steps  
  - Scripted / automated steps  

- Reference any SOPs or scripts in `tools/`, `scripts/`, or `docs/sop/*.md`.

---

# 📑 Data Contracts & Schemas

Documents that describe data MUST:

- Reference the relevant **data contract** (JSON/YAML).  
- Include:

  - Field names  
  - Types  
  - Units  
  - Constraints  
  - Optional/required flags  

- Include a **machine-validated** schema snippet.

Example contract snippet:

~~~~~text
contract_version: "v3"
fields:
  - name: dataset_id
    type: string
    required: true
  - name: timestamp
    type: datetime
    required: true
~~~~~

---

# 🧬 Ontology Alignment (Complete)

Every document MUST map its concepts to external ontologies:

| System      | Mapping Required (Examples)                |
|-------------|--------------------------------------------|
| CIDOC-CRM   | `E31 Document`, `E7 Activity`, `E53 Place` |
| OWL-Time    | `time:hasBeginning`, `time:hasEnd`         |
| GeoSPARQL   | `geo:hasGeometry` where applicable         |
| PROV-O      | `prov:Entity`, `prov:Activity`, `prov:Agent` |
| schema.org  | `TechArticle` / relevant CreativeWork subclass |
| DCAT 3.0    | Dataset & Distribution semantics           |
| STAC 1.0    | Collection & Item for spatio-temporal assets |

Documents SHOULD include a brief table or bullet list describing mapping logic.

---

# 🛰 STAC/DCAT Metadata Block

Documents attached to datasets or assets MUST include a STAC/DCAT metadata example.

~~~~~json
{
  "stac_version": "1.0.0",
  "type": "Collection",
  "id": "example-collection",
  "dcat:dataset": "https://example.org/dataset",
  "license": "CC-BY-4.0",
  "assets": {}
}
~~~~~

---

# 🧠 Focus Mode v2 Integration

Any document that will be surfaced in **Focus Mode** MUST include:

- `focus_id` (if it describes a primary entity).  
- Narrative guidelines for Focus Mode summarization.  
- Boundaries for explainability and inference:

  - What may be summarized.  
  - What must always be presented with contextual caveats.  
  - Allowed / prohibited AI transformations.  

- SHAP/LIME explanation hints (for model-based focus views).  
- Hazard notes:

  - Trigger warnings.  
  - Culturally sensitive content.  
  - Uncertain interpretations (must be clearly flagged).

Example expectations:

- **Allowed:** factual summarization, neutral description, linked citation snippets.  
- **Prohibited:** speculative reconstruction, invented motives, unverified historical claims.

---

# 📖 Story Node v3 Integration

Any **narrative-ready document** MUST include a **Story Node-compatible** section, or an explicit note that Story Nodes are not applicable.

A compliant narrative section includes:

- `story_node_id` (if it is or defines a node).  
- Narrative body (Markdown or text).  
- Temporal extent (start, end, precision).  
- Spatial extent (GeoJSON geometry or reference).  
- `relations[]` describing narrative links.  
- `media[]` with asset references and licenses.  
- Precision markers and uncertainty description.  
- Original phrasing block (for ambiguous historical dates and terms).

---

# 🔐 Ethics & CARE Requirements

Each document MUST explicitly declare:

- Ethical sensitivities (e.g., trauma, conflict, sacred sites).  
- Stewardship responsibilities (who is responsible for governance).  
- Indigenous sovereignty considerations (where applicable).  
- Culturally restricted knowledge boundaries.  
- Consent requirements (data, media, narratives).

Docs involving culturally significant or Indigenous content MUST reference:

- Relevant governance files.  
- CARE-labelled data sources.  
- Any external community agreements.

---

# 🛡 Privacy & Security

Every document MUST include:

- Data classification (Public / Internal / Restricted).  
- Access requirements (who may read/change this doc).  
- Encryption requirements (if any data references demand it).  
- Retention & destruction policy.  
- Compliance with relevant Kansas and U.S. statutes where applicable.

---

# 🧪 Validation & Reproducibility

Docs MUST describe:

- Which validations apply (schemas, CI jobs).  
- Reproducibility instructions (commands, scripts, environment).  
- Verification environment details:
  - OS  
  - Container image(s)  
  - Runtime versions (Python, Node, etc.)  
  - Required hardware assumptions (CPU/GPU/RAM).

Example:

~~~~~text
$ make docs-validate
$ pytest tests/docs/test_markdown_rules.py
~~~~~

---

# 📈 Telemetry

Documents MUST list telemetry expectations where relevant:

- Events emitted by processes described.  
- Metrics included (e.g., runtimes, counts, error rates).  
- Sampling strategy (all events vs sampled).  
- Any privacy-preserving aggregation (e.g., k-anonymity).

---

# 🎧 Accessibility (WCAG 2.1 AA)

Every doc MUST comply with accessibility rules:

- All images include descriptive alt text.  
- Headings are structured and nested correctly.  
- Lists and tables are properly formed.  
- A brief plain-language summary MUST be provided for complex technical documents.  
- No reliance solely on color to convey meaning in diagrams referencable from the doc.

---

# 🤖 Machine Extractability

Documents MUST ensure:

- Predictable heading structure (no skipped levels).  
- Machine-friendly tables (no row or column misalignment).  
- Well-formed fenced code blocks with language tags.  
- JSON-LD or other semantic blocks where appropriate.  
- Clear patterns for automated parsing (no non-standard structural tricks).

---

# ♻️ Dataset Evolution / Deltas

For dataset and schema-related docs, a **Dataset Evolution** section MUST list:

- Changes since previous version:
  - New fields.  
  - Removed fields.  
  - Type or unit changes.  
- Backward compatibility considerations.  
- Known migration concerns.

---

# 🧩 Error Taxonomy Section

All process, pipeline, or system docs MUST specify:

- Failure modes.  
- Error classes.  
- Mitigation strategies.  
- Safety constraints.  
- Known risky operations and safeguards.

---

# 📁 Directory Layout

Every top-level or major component doc MUST include a **Directory Layout** section using an ASCII tree:

~~~~~text
docs/
├── standards/
│   └── markdown_rules.md
├── analyses/
├── reports/
~~~~~

Rules:

- Use `text` fenced code blocks.  
- No comments inline.  
- No trailing spaces.

---

# 🕰 Version History

A **Version History** section is required, including at least the current and previous versions:

~~~~~markdown
## 🕰 Version History

| Version | Date       | Author   | Summary                                 |
|---------|------------|----------|-----------------------------------------|
| v10.4.0 | 2025-11-14 | A. Barta | Complete upgrade with 80+ requirements. |
| v10.2.8 | 2025-11-13 | A. Barta | Previous stable version.                |
~~~~~

---

# 🧾 Footer (Mandatory)

Every document MUST end with a standardized footer, structurally identical to:

~~~~~markdown
---

<div align="center">

**© 2025 Kansas Frontier Matrix — CC-BY 4.0**  
Validated under **Master Coder Protocol v6.3**  
FAIR+CARE Certified · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  
[Back to Standards Index](README.md) · [Root Governance Charter](governance/ROOT-GOVERNANCE.md)

</div>
~~~~~

---

<div align="center">

**© 2025 Kansas Frontier Matrix — CC-BY 4.0**  
Validated under **Master Coder Protocol v6.3**  
FAIR+CARE Certified · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  
[Back to Standards Index](README.md) · [Root Governance Charter](governance/ROOT-GOVERNANCE.md)

</div>