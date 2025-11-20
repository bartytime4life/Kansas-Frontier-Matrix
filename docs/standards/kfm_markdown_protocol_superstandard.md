---
title: "📘 Kansas Frontier Matrix — Markdown Protocol Super-Standard (KFM-MDP v11.0.0)"
path: "docs/standards/kfm_markdown_protocol_superstandard.md"
version: "v11.0.0"
last_updated: "2025-11-20"
review_cycle: "Annual / FAIR+CARE Council & Focus Mode Board"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../schemas/telemetry/docs-markdown-protocol-v11.json"
governance_ref: "governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active / Enforced"
doc_kind: "Standard"
intent: "markdown-governance"
semantic_document_id: "kfm-mdp-v11"
doc_uuid: "urn:kfm:docs:standards:kfm-mdp-v11"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
fair_category: "F1-A1-I1-R1"
care_label: "Public / Low-Risk"
immutability_status: "version-pinned"
---

<div align="center">

# 📘 **Kansas Frontier Matrix — Markdown Protocol Super-Standard (v11.0.0)**  
`docs/standards/kfm_markdown_protocol_superstandard.md`

**Purpose:**  
Define the **strict, enforced, unified Markdown protocol** governing **all documentation** produced for Kansas Frontier Matrix v11.  
This super-standard consolidates **all prior rules**, expands to v11 requirements, and ensures:

- **MCP-DL v6.3 documentation-first compliance**  
- **FAIR+CARE ethics**  
- **WCAG 2.1 AA+ accessibility**  
- **STAC 1.x & DCAT 3.0 metadata alignment**  
- **CIDOC-CRM / GeoSPARQL / OWL-Time compatibility**  
- **Focus Mode v3 narrative integration**  
- **Story Node v3 schema integration**  
- **Full CI/CD lint enforcement**  
- **Monorepo structural cohesion**  
- **Deterministic reproducibility + provenance**

**This is the single authoritative standard.**  
All Markdown MUST comply. Non-compliant documents are rejected by CI.

</div>

---

# 📘 1. Philosophy & High-Level Requirements

## 1.1 Documentation-First Mandate
All KFM documentation MUST:

- Be written before or alongside implementation  
- Be machine-extractable  
- Follow strict YAML metadata  
- Encode FAIR+CARE  
- Comply with STAC/DCAT/PROV-O  
- Be accessible and WCAG-aligned  
- Integrate with Focus Mode v3 and Story Node v3

Documentation is treated as **code**.  
CI will reject any Markdown failing these rules.

## 1.2 Scope of Enforcement
This standard governs **all**:

- READMEs  
- Guides  
- SOPs  
- Standards  
- Data documentation  
- Architecture docs  
- Story Nodes (Markdown representations)  
- Narrative content  
- Example blocks  
- Internal developer docs  
- Public-facing docs  

---

# 🧱 2. Mandatory Document Structure

Every file MUST follow this exact structure:

```
---
<YAML FRONT-MATTER>
---

<div align="center">

# <EMOJI + TITLE>  
`path/to/file.md`

**Purpose:**  
1–4 lines max.

</div>

---

# 📘 Overview  
# 🗂 Directory Layout (if applicable)  
# 🧩 Content Sections  
# 🛠 Examples (optional)  
# ⚙️ Validation & CI Requirements  
# 🕰 Version History  
<Footer Block>
```

### Strict Rules:
- Only **one** H1 per file (inside `<div align="center">`)  
- H2 headings MUST begin with emojis  
- H3 for subsections, H4 for deep details  
- No H5+ allowed  
- No blank line above YAML  
- No trailing whitespace  
- No tabs  

---

# 🧾 3. YAML Front-Matter Standard (v11)

A KFM Markdown file MUST begin with a YAML block containing:

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
machine_extractable:
accessibility_compliance:
fair_category:
care_label:
immutability_status:
```

### Mandatory Behavior:
- NO unknown keys  
- NO tabs  
- NO blank line above or below fence  
- MUST match file path exactly  
- MUST update `version` and `last_updated` whenever file changes  
- MUST generate new `doc_uuid` on version changes  

---

# 🧭 4. Title Block Rules

Inside `<div align="center">`:

```
# ✨ **Document Title**  
`path/to/file.md`

**Purpose:**  
Short clear description.
```

Rules:
- MUST contain an emoji  
- MUST match YAML `title`  
- Path MUST match YAML  
- Purpose 1–4 lines  

---

# 🗂 5. Directory Layout Rules

Use ONLY this ASCII style:

```text
root/
│
├── folder/           # comment
│   ├── file.md       # comment
│   └── subfolder/    # comment
└── another/          # comment
```

Constraints:
- MUST use │ ├── └──  
- MUST use 4 spaces per indent  
- MUST include comments  
- MUST be inside ```text fenced block  

---

# 🔤 6. Content Rules

## 6.1 Headings
- H1 only once  
- H2 must use emojis  
- H3/H4 optional  
- Never skip levels  

## 6.2 Paragraphs
- One blank line between sections  
- No trailing spaces  

## 6.3 Lists
- Use `-` or `*` only  
- Nested lists: 2-space indent  

---

# 🧩 7. Code Block Rules

Use triple backticks:

````markdown
```json
{
  "example": true
}
```
````

Rules:
- Always specify language  
- Never indent fences  
- JSON/YAML MUST validate  
- No inline HTML except the top `<div>`  

---

# 🎨 8. Tables

Use GitHub-flavored tables:

```
| Field | Description |
|------:|-------------|
| id    | Unique ID   |
```

Rules:
- No merged cells  
- No HTML tables  

---

# ♿ 9. Accessibility (WCAG 2.1 AA+)

MUST:
- Provide alt-text for every image  
- Provide descriptive link labels  
- Avoid color-only meaning  
- Provide title + summary for diagrams  
- Use heading order correctly  
- Ensure all tables have headers  

---

# ⚖️ 10. FAIR+CARE Mandates

### MUST:
- Include license metadata  
- Include provenance for all datasets  
- Avoid sensitive personal or Indigenous site details  
- Use generalized geospatial references when required  
- Label synthetic or AI-generated content  

---

# 🛰 11. STAC 1.x Integration

Every dataset referenced MUST include or link to a STAC Item.

### Example STAC Item:
```json
{
  "stac_version": "1.0.0",
  "type": "Item",
  "id": "dataset-123",
  "bbox": [-102.0, 37.0, -94.6, 40.0],
  "geometry": { "type": "Polygon", "coordinates": [...] },
  "properties": {
    "datetime": "2025-01-01T00:00:00Z",
    "kfm:lineage": "data/work/staging"
  },
  "assets": {
    "data": {
      "href": "https://example.com/data/file.geojson",
      "type": "application/geo+json"
    }
  }
}
```

---

# 📦 12. DCAT 3.0 Integration

YAML MUST map to DCAT terms:

| YAML Key | DCAT Equivalent |
|----------|-----------------|
| title | dct:title |
| description | dct:description |
| license | dct:license |
| path | dcat:accessURL |
| version | dct:hasVersion |

---

# 🕰 13. OWL-Time Integration

Events and periods MUST include:

- `start` ISO8601  
- `end` ISO8601 (optional)  
- `precision`  

---

# 🌐 14. GeoSPARQL Integration

Spatial metadata MUST be extractable as:

- GeoJSON  
- bbox  
- CRS  

---

# 📚 15. Story Node v3 Alignment

Markdown representing Story Nodes MUST follow:

### Required fields:
```yaml
id:
type: story-node
version:
title:
summary:
spacetime:
  geometry:
  when:
narrative:
  body:
relations:
```

Narrative content MUST be fact-based and provenance-derived.

---

# 🎯 16. Focus Mode v3 Integration

Every document MUST be extractable for:

- Entity summaries  
- Temporal anchoring  
- Spatial anchoring  
- Narrative hooks  
- Provenance tracking  

Focus Mode MUST be able to parse:

- Title  
- Purpose  
- Overview  
- Key entities  

---

# ⚙️ 17. CI/CD Enforcement

CI pipelines MUST validate:

- YAML schema  
- Heading structure  
- Table formatting  
- Link validity  
- JSON/YAML correctness  
- FAIR+CARE compliance  
- Accessibility heuristics  
- Story Node schema conformance  
- STAC item references  
- No tabs  
- No trailing whitespace  

Documents failing validation MUST NOT MERGE.

---

# 🧪 18. Example Full Document Skeleton

````markdown
---
title: "🗺 Example Doc"
path: "docs/example.md"
version: "v1.0.0"
last_updated: "2025-11-20"
review_cycle: "Annual"
commit_sha: "<latest>"
sbom_ref: "../../releases/v1/sbom.spdx.json"
manifest_ref: "../../releases/v1/manifest.zip"
telemetry_ref: "../../releases/v1/telemetry.json"
telemetry_schema: "../../schemas/telemetry/example-schema.json"
governance_ref: "governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active"
doc_kind: "Guide"
intent: "example"
semantic_document_id: "kfm-example"
doc_uuid: "urn:kfm:example-v1.0.0"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
fair_category: "F1-A1-I1-R1"
care_label: "Public / Low-Risk"
immutability_status: "version-pinned"
---

<div align="center">

# 🗺 **Example KFM Document**  
`docs/example.md`

**Purpose:**  
Short description here.

</div>

---

# 📘 Overview
This document demonstrates the structure.

# 🗂 Directory Layout
```text
docs/
└── example.md      # This file
```

# 🧩 Content
Example text.

# 🕰 Version History

| Version | Date | Summary |
|--------:|------|---------|
| v1.0.0 | 2025-11-20 | Initial |
````

---

# 🔚 Footer (Required)

<div align="center">

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
Master Coder Protocol v6.3 · FAIR+CARE Certified  
Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

</div>

~~~~markdown
