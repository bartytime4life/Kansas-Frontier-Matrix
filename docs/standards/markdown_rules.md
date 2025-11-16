---
title: "📑 Kansas Frontier Matrix — Markdown Structural & Formatting Rules (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/standards/markdown_rules.md"
version: "v10.4.3"
last_updated: "2025-11-16"
review_cycle: "Annual / FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../releases/v10.4.3/sbom.spdx.json"
manifest_ref: "../../releases/v10.4.3/manifest.zip"
telemetry_ref: "../../releases/v10.4.3/focus-telemetry.json"
telemetry_schema: "../../schemas/telemetry/docs-markdown-rules-v4.json"
governance_ref: "governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4.3"
status: "Active / Enforced"
doc_kind: "Standard"
intent: "markdown-governance"
semantic_document_id: "kfm-doc-markdown-rules"
doc_uuid: "urn:kfm:docs:standards:markdown-rules-v10.4.3"
accessibility_compliance: "WCAG 2.1 AA"
machine_extractable: true
fair_category: "F1-A1-I1-R1"
care_label: "Public / Low-Risk"
immutability_status: "version-pinned"
---

<div align="center">

# 📑 **Kansas Frontier Matrix — Markdown Structural & Formatting Rules**  
`docs/standards/markdown_rules.md`

**Purpose:**  
Define the authoritative, enforced Markdown documentation standard for the Kansas Frontier Matrix (KFM).  
All documentation must comply with **KFM-MDP v10.4.3**, **MCP-DL v6.3**, and the **Diamond⁹ Ω / Crown∞Ω Ultimate Certification** framework.  
This governs every README, guide, standard, architecture file, and reference document in the repository.

</div>

---

# 📘 Overview

These rules ensure:

- Absolute consistency across every markdown file  
- Predictable parsing by CI, lineage, telemetry, and governance validators  
- Machine extractability for STAC/DCAT, FAIR+CARE, and AI systems  
- Accessibility compliance (WCAG 2.1 AA)  
- Immutable documentation lineage for governance ledger synchronization  

Any Markdown violating these rules **fails CI**.

---

# 🧱 Section 1 — Required Layout & Ordering

Every document **must** follow this global ordering:

1. **YAML Front-Matter Block**  
2. **Centered Title Block**  
3. **Horizontal Rule (`---`)**  
4. **Overview Section**  
5. **Directory Context (if applicable)**  
6. **Main Content Sections**  
7. **Tables, Diagrams, Examples**  
8. **Version History**  
9. **Footer / Licensing Block**

If a file uses headings, the order must follow:

```

# (H1 – one per document)

## (H2 – major sections)

### (H3 – inner sections)

#### (H4 – optional nested details)

````

No other heading levels are permitted.

---

# 🧱 Section 2 — YAML Front-Matter Requirements

Each file **must begin** with YAML front-matter enclosed by `---` fences.

Minimum required fields:

```yaml
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
````

Optional fields for governance:

```yaml
care_label:
fair_category:
immutability_status:
ai_focusmode_usage:
ai_transform_permissions:
ai_transform_prohibited:
```

Front-matter **must not** contain:

* Tabs
* Trailing spaces
* Mismatched indentation
* Unregistered fields

---

# 🧱 Section 3 — Centered Header Block Rules

Immediately after YAML, include:

```html
<div align="center">

# TITLE HERE  
`path/to/file.md`

**Purpose:**  
Short description here.

</div>
```

Rules:

* Title must include an emoji
* Path must be in backticks
* Purpose must be 1–4 lines maximum
* No extraneous whitespace

---

# 🧱 Section 4 — Directory Layout Blocks (Lined Format)

The lined directory block is **standardized** in KFM-MDP v10.4.3.

Syntax:

```text
root/
│
├── folder/                # comment
│   ├── subfolder/         # comment
│   └── file.md            # comment
└── other/                 # comment
```

Rules:

* Use **vertical lines (`│`)**, **L-shaped connectors (`├──`, `└──`)**
* Must include **comments on every line**
* Use the **blank root separator `│`** after root/
* No tabs. Spaces only.
* No trailing whitespace.
* Must be wrapped in a fenced block (```text).

This block style is **mandatory** for all architecture, features, telemetry, pipelines, and web documentation files.

---

# 🧱 Section 5 — Mermaid Diagram Standards

All diagrams must:

* Use fenced blocks:

  ```mermaid
  flowchart TD
  ...
  ```
* Never include HTML `<span>` or inline styling (breaks CI)
* Use explicit node brackets like:
  `A["Label"] --> B["Label"]`
* Use `<br/>` for line breaks inside nodes
* End with no blank lines inside the block

Forbidden:

* Markdown interpolation inside Mermaid
* Raw HTML attributes
* Unicode arrows not supported by Mermaid

---

# 🧱 Section 6 — Tables

Rules:

* Must use GitHub-flavored markdown tables
* First row = headers
* Must have separator row with `---`
* No merged cells
* No HTML tables

Disallowed:

```
| A | B |
|---|---|
| *No nested formatting that breaks table* |
```

Allowed:

```
| Field | Description |
|-------|-------------|
| cpu_usage_percent | CPU load (%) |
```

---

# 🧱 Section 7 — Code Fences & Example Blocks

Rules:

* Always use **triple backticks**
* Use explicit language tags: `json`, `yaml`, `text`, `bash`, `ts`, `python`
* Never mix tabs and spaces
* No indentation outside the code fence

Correct:

```json
{
  "key": "value"
}
```

Incorrect:

````
    ```json
    { invalid }
    ```
````

---

# 🧱 Section 8 — Accessibility & FAIR+CARE Governance

All Markdown must:

* Follow WCAG 2.1 AA standards
* Include alt-text for all images
* Use inclusive, non-speculative language
* Label sensitive data sections with CARE tags
* Include provenance: STAC/DCAT references where applicable
* Avoid decorative emojis in headings beyond the first emoji
* Use readable contrast ratios in embedded examples

Images:

```
![Alt text — required and descriptive](path)
```

---

# 🧱 Section 9 — Telemetry Enforcement (Docs Build)

CI validates Markdown using:

* `docs-lint.yml`
* `faircare-validate.yml`
* `telemetry-export.yml`

Each file is:

* Parsed
* Checked for headings & YAML
* Checked for invalid inline HTML
* Checked for governance metadata completeness
* Has telemetry usage recorded in
  `releases/<version>/focus-telemetry.json`

---

# 🧱 Section 10 — AI Safety & Content Boundaries

All Markdown must exclude:

* Speculative claims
* Fabricated historical facts
* Unverified datasets
* Unattributed quotes
* Unnotated AI-generated summaries (must include provenance)

If a section includes AI reasoning outputs, annotate:

```
> **AI-Generated Content:**  
> Produced by Focus Transformer v2, validated under FAIR+CARE.
```

---

# 🧱 Section 11 — Prohibited Formatting

Not allowed anywhere:

* HTML tables
* HTML `<style>` blocks
* Non-YAML metadata at document start
* Multiple H1 headers
* Mixing tabs + spaces
* Emoji-only headings
* Footnotes breaking accessibility
* Screenshots without alt text

---

# 🧱 Section 12 — Versioning & Immutability

Every Markdown document:

* Is version-pinned
* Must update `version:` and `last_updated:` when changed
* Must update `doc_uuid:` when version increments
* Must include a **Version History Table**

Templated:

| Version | Date | Author | Summary |
| ------: | ---- | ------ | ------- |

---

# 🧱 Section 13 — Example Full Document Skeleton

Below is the **canonical reference skeleton**:

````markdown
---
title: "🧩 Example Document"
path: "docs/example/README.md"
version: "vX.Y.Z"
last_updated: "2025-11-16"
review_cycle: "Quarterly"
commit_sha: "<commit>"
sbom_ref: "../../releases/vX.Y.Z/sbom.spdx.json"
manifest_ref: "../../releases/vX.Y.Z/manifest.zip"
telemetry_ref: "../../releases/vX.Y.Z/focus-telemetry.json"
telemetry_schema: "../../schemas/telemetry/example.schema.json"
governance_ref: "../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4.3"
status: "Active / Enforced"
doc_kind: "Guide"
intent: "example"
semantic_document_id: "kfm-doc-example"
doc_uuid: "urn:kfm:docs:example-vX.Y.Z"
machine_extractable: true
---

<div align="center">

# 🧩 **Example Document Title**  
`docs/example/README.md`

**Purpose:**  
Short description.

</div>

---

# 📘 Overview

Text...

# 🗂️ Directory Layout

```text
docs/example/
│
├── file.md        # comment
└── sub/           # comment
````

# Content Sections …

# 🕰️ Version History

| Version | Date       | Author | Summary |
| ------: | ---------- | ------ | ------- |
|  vX.Y.Z | 2025-11-16 | Team   | Initial |

```

---

# 🧱 Section 14 — Enforcement

Violations trigger:

- ❌ CI block  
- ❌ FAIR+CARE governance failure  
- ❌ Telemetry non-compliance  
- ❌ Documentation quality failure  

Only compliant documents receive:

- ✅ Diamond⁹ Ω Certification  
- ✅ MCP-DL v6.3 compliance  
- ✅ FAIR+CARE approval  

---

# 🕰️ Version History

| Version | Date | Author | Summary |
|--------:|------------|---------|---------|
| v10.4.3 | 2025-11-16 | Core Team | Complete rewrite to match KFM-MDP v10.4.3, deep inset styling, global lined directory format, strict CI-enforced rules. |
| v10.4.2 | 2025-11-15 | Core Team | Incremental rule expansion for telemetry alignment. |
| v10.4.0 | 2025-11-14 | Documentation Council | Initial Markdown Ruleset. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
Master Coder Protocol v6.3 · FAIR+CARE Certified  
Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>
