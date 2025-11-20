---
title: "📑 Kansas Frontier Matrix — Markdown Structural & Formatting Rules (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/standards/markdown_rules.md"
version: "v11.0.0"
last_updated: "2025-11-20"
review_cycle: "Annual / FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../schemas/telemetry/docs-markdown-rules-v11.json"
governance_ref: "governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active / Enforced"
doc_kind: "Standard"
intent: "markdown-governance"
semantic_document_id: "kfm-doc-markdown-rules-v11"
doc_uuid: "urn:kfm:docs:standards:markdown-rules-v11"
accessibility_compliance: "WCAG 2.1 AA+"
machine_extractable: true
fair_category: "F1-A1-I1-R1"
care_label: "Public / Low-Risk"
immutability_status: "version-pinned"
---

<div align="center">

# 📑 **Kansas Frontier Matrix — Markdown Structural & Formatting Rules (v11.0)**  
`docs/standards/markdown_rules.md`

**Purpose:**  
Define the **mandatory Markdown authoring rules for KFM v11**, upgraded from v10.4.3 to support:  
• **KFM-MDP v11 metadata extensions**  
• **Focus Mode v3 narrative hooks**  
• **Story Node v3 schema alignment**  
• **STAC/DCAT/PROV-O enrichment**  
• **Full WCAG 2.1 AA+ accessibility compliance**  
• **Monorepo traceability + CI/CD enforcement**  

</div>

---

# 📘 Overview

KFM-MDP v11.0 governs **all Markdown documentation** in the Kansas Frontier Matrix repository.  
Every file must be:

• Documentation-first (MCP-DL v6.3)  
• Machine-extractable  
• Semantically structured  
• FAIR+CARE compliant  
• STAC/DCAT/PROV-O aligned  
• Focus Mode v3 compatible  
• Validated by CI (docs-lint, schema-lint, FAIR+CARE audit, metadata validator)

Any violation → **CI failure** → PR is rejected.

---

# 🧱 Section 1 — Required Layout & Ordering

All KFM v11 Markdown files MUST follow this exact structure:

1. **YAML front-matter block (mandatory, strict)**  
2. **Centered title block** (title + path + short purpose)  
3. **Horizontal rule (`---`)**  
4. **📘 Overview** (H2)  
5. **🗂 Directory Context** (if applicable)  
6. **Main Content Sections** (H2/H3/H4 only)  
7. **Tables, diagrams, examples**  
8. **Focus Mode v3 + Story Node hooks** (if relevant)  
9. **Version History**  
10. **Footer (copyright + certification)**

### Heading rules

• Only H1–H4  
• One H1 per document  
• H2 for primary sections  
• H3 for subsections  
• H4 for deep detail  
• Emojis encouraged but must be followed by text  
• No empty or duplicated headings

---

# 🧱 Section 2 — YAML Front-Matter Requirements (v11 Expanded)

The YAML block **must begin the file** (no blank lines above).

Required fields:

```
title:
path:
version:
last_updated:
review_cycle:
commit_sha:
sbom_ref:
manifest_ref:
telemetry_ref:
telemetry_schema:
governance_ref:
license:
mcp_version:
markdown_protocol_version:
status:
doc_kind:
intent:
semantic_document_id:
doc_uuid:
accessibility_compliance:
machine_extractable:
fair_category:
care_label:
immutability_status:
```

### v11 Additions (new mandatory fields)

```
markdown_protocol_version:
semantic_document_id:
doc_uuid:
accessibility_compliance:
machine_extractable:
fair_category:
care_label:
immutability_status:
```

These support:

• STAC/DCAT catalog export  
• Knowledge-graph document indexing  
• FAIR+CARE ethics audit  
• Focus Mode v3 document targeting  
• Story Node binding

Any missing field → **CI stops merge**.

---

# 🧱 Section 3 — Centered Header Block

Immediately after YAML, insert:

```
<div align="center">

# TITLE  
`path/to/file.md`

**Purpose:**  
Short purpose (1–4 lines).

</div>
```

Rules:

• Title must start with an emoji  
• Path must be monospace  
• Purpose must be concise  
• No trailing spaces or blank lines inside the block

---

# 🗂 Section 4 — Directory Layout Blocks (DL-C v11)

Use the lined ASCII tree format:

```
docs/
│
├── standards/          # governance rules
│   └── markdown/       # this file
└── guides/             # how-tos and SOPs
```

Rules:

• Use `│`, `├──`, `└──` only  
• Every line MUST have a comment  
• Fenced with ```text  
• No tabs, no trailing whitespace  
• Must be vertically aligned and GitHub-safe

---

# 🧩 Section 5 — Mermaid Diagram Standards

• Use fenced ` ```mermaid `  
• No HTML span/style tags  
• Use explicit node brackets (A["Label"])  
• Use `<br/>` for forced line breaks  
• No blank lines inside the block  
• No non-ASCII arrows or Unicode characters that break CI

---

# 📊 Section 6 — Tables

• GitHub-flavored tables only  
• Header row required  
• Alignment row required  
• No merged cells  
• No nested markdown that breaks parsing

Example:

```
| Field | Description |
|------:|-------------|
| cpu_usage_percent | CPU load (%) |
```

---

# 🧾 Section 7 — Code Fences

• Always use triple backticks  
• Always specify the language: `yaml`, `json`, `text`, `bash`, `ts`, `python`  
• No indentation before backticks  
• Code MUST validate if schema-aware (JSON, YAML)

---

# ♿ Section 8 — Accessibility (WCAG 2.1 AA+)

• Alt-text for all images  
• Descriptive link text (no “click here”)  
• Proper heading order  
• Sufficient color contrast in examples  
• No emoji-only headings  
• All tables must have headers  
• All diagrams must have description context

---

# ⚖️ Section 9 — FAIR+CARE Governance Enforcement

Markdown must reflect:

• FAIR (Findable, Accessible, Interoperable, Reusable)  
• CARE (Collective Benefit, Authority to Control, Responsibility, Ethics)  

Required:

• License declaration (SPDX)  
• Source attribution  
• Provenance metadata  
• Sensitive cultural data masked or generalized  
• No speculation about Indigenous communities or individuals  
• No unlicensed images or datasets

---

# 🔍 Section 10 — CI Validation Requirements

Files are validated by:

• docs-lint.yml  
• markdown-structure-validator  
• metadata-validator (YAML schema)  
• link-checker  
• stac-metadata-checker  
• faircare-validate.yml  
• focusmode-validate.yml  

Any failure blocks merge.

---

# 🔭 Section 11 — Focus Mode v3 Integration (New for v11)

Markdown must support:

• Inline Focus Hooks  

```
> **Focus Hook:** entity:kansas_river event:1851_flood
```

• Narrative anchors (for AI contextualization)  
• Story Node v3 linkouts  
• Temporal indexing for Focus Mode queries  
• Spatial references resolvable to GeoJSON/graph IDs

Violations lead to **Focus Mode parsing errors** in CI.

---

# 📚 Section 12 — Story Node v3 Compatibility

Documents containing narratives MUST:

• Use clean extractable prose  
• Avoid ambiguous pronouns (they, it) where context is unclear  
• Include temporal markers (YYYY or YYYY-MM-DD)  
• Include spatial markers resolvable via GNIS/KFM IDs  
• Be free of emojis inside narrative paragraphs (allowed in headings only)

---

# 🕰️ Section 13 — Versioning & Immutability

Each update requires:

• Incremented `version:`  
• Updated `last_updated:`  
• Updated `commit_sha:`  
• Updated `doc_uuid:` (new version = new UUID)  
• Version history entry appended at bottom

---

# 🧩 Section 14 — Example Full Document Skeleton (v11)

````markdown
---
title: "🧩 Example Document"
path: "docs/example/README.md"
version: "v1.2.0"
last_updated: "2025-11-20"
review_cycle: "Quarterly / Autonomous"
commit_sha: "<commit>"
sbom_ref: "../../releases/v1.2.0/sbom.spdx.json"
manifest_ref: "../../releases/v1.2.0/manifest.zip"
telemetry_ref: "../../releases/v1.2.0/focus-telemetry.json"
telemetry_schema: "../../schemas/telemetry/example.schema.json"
governance_ref: "../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active"
doc_kind: "Guide"
intent: "example"
semantic_document_id: "kfm-doc-example"
doc_uuid: "urn:kfm:docs:example-v1.2.0"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
fair_category: "F1-A1-I1-R1"
care_label: "Public / Low-Risk"
immutability_status: "version-pinned"
---

<div align="center">

# 🧩 **Example Document Title**  
`docs/example/README.md`

**Purpose:**  
Short description.

</div>

---

# 📘 Overview
Example text.

# 🗂 Directory Layout

```text
docs/example/
│
├── file.md          # comment
└── sub/             # comment
```

# 🕰️ Version History

| Version | Date | Author | Summary |
|-------:|------------|--------|---------|
| v1.2.0 | 2025-11-20 | Team | Updated for v11 |
````

---

# 🕰️ Version History

| Version | Date | Author | Summary |
|-------:|------------|--------|---------|
| v11.0.0 | 2025-11-20 | Core Team | Full upgrade to KFM-MDP v11.0; added Story Nodes v3, Focus Mode v3, STAC/DCAT/PROV-O expansion, FAIR+CARE v11 enforcement. |
| v10.4.3 | 2025-11-16 | Core Team | Previous stable version. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
Master Coder Protocol v6.3 · FAIR+CARE Certified  
Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>
