---
title: "📘 Kansas Frontier Matrix — Standard Markdown Template"
path: "docs/templates/kfm-standard-markdown-template.md"
version: "v11.2.6"
last_updated: "2025-12-11"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · FAIR+CARE Council"
content_stability: "stable"

status: "Active / In-Repo Canonical"
doc_kind: "Standard"
intent: "kfm-markdown-template"

header_profile: "standard"
footer_profile: "standard"

markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

semantic_document_id: "kfm-doc-standard-markdown-template-v11.2.6"
doc_uuid: "urn:kfm:doc:templates:standard-markdown-template:v11.2.6"
event_source_id: "ledger:docs/templates/kfm-standard-markdown-template.md"
immutability_status: "version-pinned"

sbom_ref: "../../releases/v11.2.6/sbom.spdx.json"
manifest_ref: "../../releases/v11.2.6/manifest.zip"
telemetry_ref: "../../releases/v11.2.6/kfm-telemetry.json"
telemetry_schema: "../../schemas/telemetry/markdown-template-usage-v1.json"
governance_ref: "../standards/kfm_markdown_protocol_v11.2.6.md"
license: "CC-BY 4.0"
---

<div align="center">

# 📘 Kansas Frontier Matrix  
## **Standard Markdown Template (KFM v11.2.6)**

This file serves as the **canonical pattern** for constructing new, governed, standards-aligned Markdown documents inside the KFM monorepo.

`docs/templates/kfm-standard-markdown-template.md`

</div>

---

## 📘 Overview

This template provides a **uniform, reproducible structure** that every KFM Markdown file should follow under **KFM-MDP v11.2.6**. It ensures:

- Metadata consistency via YAML front-matter  
- Directory layout continuity (emoji + ASCII trees)  
- Deterministic **ETL → Catalog → Graph → API → UI → Story Node / Focus Mode** alignment  
- Integration with FAIR+CARE, provenance, and telemetry requirements  

Use this template whenever creating a new Markdown file anywhere in the monorepo, then adapt sections as appropriate for the document’s purpose.

---

## 🗂️ Directory Layout (Emoji-Annotated · KFM v11.2.6)

This template lives in `docs/templates/` and is referenced by KFM-MDP:

~~~text
📁 docs/
  📁 standards/
    📄 kfm_markdown_protocol_v11.2.6.md   # KFM-MDP: Markdown authoring standard
  📁 templates/
    📄 kfm-standard-markdown-template.md  # This file – standard Markdown template
~~~

When documenting a specific domain or module, add a **Directory Layout** section with:

- Emoji-prefixed entries (`📁`, `📄`, `🧾`, `🧪`, `🖼️`), and  
- A short inline description for each entry where useful.  

Use `~~~text` fences (not ``` inside docs) for directory trees.

---

## 🧭 Context — How to Use This Template

This file is a **guide** and a **source of copy-paste snippets**. For a new document:

1. Copy the **YAML front-matter skeleton** below into the new file.  
2. Replace placeholder values (`<...>`) with document-specific values.  
3. Select appropriate headings from the KFM heading registry.  
4. Add a Directory Layout section if the doc describes a directory, module, or domain.  
5. Add a Version History table at the end and keep it up to date.

---

## 🧱 Front-Matter Skeleton (Fill Me In)

Paste and edit this at the top of new docs. Adjust fields as needed (e.g., no `sbom_ref` for very simple docs).

~~~markdown
---
title: "<emoji + short, descriptive title>"
path: "<relative/path/from/repo/root>.md"
version: "v11.2.6"
last_updated: "<YYYY-MM-DD>"

release_stage: "<Draft / Stable / Governed>"
lifecycle: "<Incubation / Long-Term Support (LTS) / Archive>"
review_cycle: "<cadence · owning group(s)>"
content_stability: "<evolving / stable / frozen>"

status: "<Active / Deprecated / Historical Record>"
doc_kind: "<Standard / Data Domain Overview / Design Note / Event Summary / ...>"
intent: "<short-purpose-slug>"
header_profile: "standard"
footer_profile: "standard"

license: "CC-BY 4.0"

markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

semantic_document_id: "<kfm-doc-*-v11.2.6>"
doc_uuid: "<urn:kfm:doc:...>"
event_source_id: "ledger:<relative/path>.md"
immutability_status: "version-pinned"

sbom_ref: "<../../releases/v11.2.6/sbom.spdx.json>"
manifest_ref: "<../../releases/v11.2.6/manifest.zip>"
telemetry_ref: "<../../releases/v11.2.6/<area>-telemetry.json>"
telemetry_schema: "<../../schemas/telemetry/<area>-v11.json>"
governance_ref: "<../standards/governance/...md>"
---
~~~

Guidelines:

- **No blank lines before the first `---`.**  
- Update `version` and `last_updated` only when contents change.  
- Use **real values** in new docs; placeholders are for this template only.

---

## 📦 Recommended Section Headings

KFM-MDP v11.2.6 prefers emoji + label headings, chosen from a shared registry. Common options:

- `## 📘 Overview` — high-level purpose and scope.  
- `## 🗂️ Directory Layout` — emoji directory tree (if applicable).  
- `## 🧭 Context` — background, related work, or relationship to other docs.  
- `## 🧱 Architecture` — how this doc’s subject fits the ETL → Catalog → Graph → API → UI pipeline.  
- `## 📦 Data & Metadata` — schemas, fields, STAC/DCAT/PROV constraints.  
- `## 🌐 STAC, DCAT & PROV Alignment` — explicit mapping to catalogs and provenance.  
- `## ⚖ FAIR+CARE & Governance` — governance rules, sovereignty considerations, redaction policies.  
- `## 🧠 Story Node & Focus Mode Integration` — narrative integration and constraints.  
- `## 🧪 Validation & CI/CD` — tests, workflows, and gates.  
- `## 🕰️ Version History` — required version table at the end.

Authors should:

- Pick only the headings that make sense for the doc.  
- Maintain headings in a logical order (Overview → Layout → Context → Architecture → … → Version History).  

---

## ⚖ FAIR+CARE & Governance Hints

Every new doc should consider FAIR+CARE:

- **FAIR**:
  - State where the doc fits in catalogs or schema indexes (if relevant).  
  - Use stable paths and IDs to keep docs findable.

- **CARE**:
  - If the doc touches Indigenous data, sensitive locations, or community-held knowledge:
    - Call out constraints and safeguards explicitly.  
    - Link to the appropriate governance and sovereignty docs.  

When in doubt, add a short `⚖ FAIR+CARE & Governance` section explicitly noting whether sensitive data is involved.

---

## 🧪 Validation & CI/CD Checklist

Docs based on this template must be expected to pass:

- `markdown-lint` (headings, spacing, lists)  
- `schema-validate` (YAML front-matter schema)  
- `metadata-check` (required fields present and coherent)  
- `provenance-check` (version + integrity metadata)  
- `footer-check` (presence and correctness of governance footer)

If a doc introduces new schemas, modules, or telemetry:

- Extend or create JSON Schemas under `schemas/` as needed.  
- Update CI workflows (e.g., `.github/workflows/kfm-ci.yml`) to validate the new artifacts.

---

## 🕰️ Version History

| Version   | Date       | Summary                                                            |
|----------:|-----------:|--------------------------------------------------------------------|
| v11.2.6   | 2025-12-11 | Initial standard Markdown template aligned with KFM-MDP v11.2.6.   |

---

<div align="center">

📘 **Kansas Frontier Matrix — Standard Markdown Template (KFM v11.2.6)**  
Documentation · Standards · Reproducibility  

[📘 Docs Root](../README.md) · [📚 Markdown Standard (KFM-MDP)](../standards/kfm_markdown_protocol_v11.2.6.md) · [🏛 Governance Charter](../standards/governance/ROOT-GOVERNANCE.md)

</div>