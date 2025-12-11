---
title: "📘 Kansas Frontier Matrix — Core Markdown Template"
path: "docs/templates/kfm-markdown-template.md"
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

semantic_document_id: "kfm-doc-template-v11.2.6"
doc_uuid: "urn:kfm:doc:template:kfm-markdown-template:v11.2.6"
event_source_id: "ledger:docs/templates/kfm-markdown-template.md"
immutability_status: "version-pinned"

sbom_ref: "../../releases/v11.2.6/sbom.spdx.json"
manifest_ref: "../../releases/v11.2.6/manifest.zip"
telemetry_ref: "../../releases/v11.2.6/kfm-telemetry.json"
telemetry_schema: "../../schemas/telemetry/markdown-template-usage-v1.json"
governance_ref: "../standards/governance/ROOT-GOVERNANCE.md"
---

<div align="center">

# 📘 Kansas Frontier Matrix  
## **Core Markdown Template (KFM v11.2.6)**

This file is the **canonical pattern** for constructing new, governed, standards-aligned Markdown documents inside the Kansas Frontier Matrix monorepo.

`docs/templates/kfm-markdown-template.md`

</div>

---

## 📘 Overview

This template defines the **uniform, reproducible structure** that KFM Markdown files should follow under **KFM-MDP v11.2.6**. It encodes:

- Metadata layout and front-matter ordering  
- H1/H2 heading patterns (emoji + label)  
- Directory layout style (emoji + ASCII tree)  
- Governance footer format  
- Alignment with FAIR+CARE, provenance, and telemetry requirements  

Use this template whenever creating a new Markdown file anywhere in the monorepo.  
When AI assistants generate drafts, the **transport format** in ChatGPT is a single fenced `markdown` block. Once saved in the repo, documents are plain `.md` files with YAML front-matter at the top.

---

## 🗂️ Directory Layout

This template lives under `docs/templates/` and governs how other docs should represent directory trees.

~~~text
📁 docs/
  📁 standards/
    📄 kfm_markdown_protocol_v11.2.6.md   # KFM-MDP: markdown authoring standard
  📁 templates/
    📄 kfm-markdown-template.md           # This file – core KFM-MDP v11.2.6 markdown template
~~~

**Directory layout rules:**

- Use emojis:
  - `📁` directories
  - `📄` markdown/text
  - `🧾` JSON/YAML/config
  - `🧪` tests/fixtures
  - `🖼️` images/media
- Use `📁` / `📄` plus short description comments where helpful.  
- Use `~~~text` fences for directory trees (never inner ``` fences in KFM docs).  
- Keep paths **relative to the file** and stable across refactors whenever possible.  
- For domain or module docs, always include a `🗂️ Directory Layout` section similar to this one.

---

## 🧭 Context — How & When to Use This Template

This file is both:

- A **guide** (what KFM expects from Markdown docs), and  
- A **copy-paste source** (front-matter skeletons and standard sections).

For any new KFM Markdown file:

1. Start from this template.  
2. Copy the **front-matter skeleton** and adjust fields.  
3. Choose headings from the recommended set below.  
4. Add a `🗂️ Directory Layout` section if the doc describes a directory/module/domain.  
5. Add and maintain a `🕰️ Version History` table at the end.  

This template is aligned with:

- `docs/standards/kfm_markdown_protocol_v11.2.6.md` (KFM-MDP)  
- KFM-OP v11 ontologies and graph modeling conventions  
- KFM-PDC v11 pipeline contracts and governance patterns  

---

## 🧱 Front-Matter Skeleton (Copy & Adapt)

Paste this at the top of new docs, then customize. Adjust fields as needed (for very small docs you may omit some references, but keep ordering where fields exist).

~~~markdown
---
title: "<emoji + short, descriptive title>"
path: "<relative/path/from/repo/root>.md"
version: "v11.2.6"
last_updated: "<YYYY-MM-DD>"

release_stage: "<Draft / Stable / Governed / Historical>"
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
doc_uuid: "<urn:kfm:doc:...:v11.2.6>"
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

- **No blank lines** before the first `---`.  
- Update `version` and `last_updated` only on substantive content changes.  
- Use **real values** in new docs; placeholders (`<...>`) are for templates only.  
- Keep field ordering consistent with KFM-MDP v11.2.6 where fields exist.

---

## 📦 Data & Metadata — Content-Level Rules

Beyond front-matter, each doc SHOULD:

- Clearly state its **scope** and **role** (what it governs / describes vs what it does not).  
- Reference related docs via **relative paths** (e.g. `../standards/...`, `../../data/...`).  
- Describe any associated **schemas** under `schemas/` and telemetry schemas under `schemas/telemetry/`.  
- When relevant, explain:
  - Where this doc’s subject appears in STAC/DCAT catalogs.  
  - Which PROV records or OpenLineage events are relevant.  

For data/domain or API docs, add explicit `📦 Data & Metadata` sections that outline:

- Key fields and their types.  
- Required IDs and identifiers (e.g. dataset IDs, graph node IDs, URNs).  
- Which catalogs and schemas enforce these structures.

---

## 🧱 Architecture Alignment

Every KFM document that describes systems, data, or workflows should explain how its subject fits into the **canonical pipeline**:

> Deterministic ETL → STAC/DCAT/PROV catalogs → Neo4j → API → React/MapLibre/Cesium → Story Nodes → Focus Mode

At minimum, authors should specify:

- Relevant **ETL pipelines** (`src/pipelines/...`).  
- Which **catalogs** are produced/consumed (`data/stac/`, `data/*/dcat/`, `data/*/dcat-prov/`).  
- Which **graph entities** and relationships are involved (`src/graph/...`, KFM-OP labels).  
- Which **APIs** expose the results (`src/api/...`).  
- Which **UI areas** depend on this work (`src/web/...`, Focus Mode panels, Story Nodes).

Architecture sections should be:

- Descriptive enough for new contributors to orient themselves.  
- Precise enough that CI, telemetry, and governance can anchor checks to specific modules.

---

## 🌐 STAC, DCAT & PROV Alignment

For data and catalog-related docs, authors should:

- Declare how STAC Collections/Items are structured, versioned, and linked.  
- Explain how DCAT Datasets and Distributions represent the same assets.  
- Show how PROV-O captures lineage across ETL, modeling, and publication:

  - `prov:Entity` — datasets, files, docs, models, snapshots.  
  - `prov:Activity` — ETL runs, AI inferences, document generation.  
  - `prov:Agent` — teams, services, automated agents.

Even purely textual docs (like this one) participate in catalogs:

- Front-matter identifier fields (`semantic_document_id`, `doc_uuid`, `event_source_id`) support STAC/DCAT cataloging.  
- `sbom_ref`, `manifest_ref`, and `telemetry_ref` connect docs to release artifacts and telemetry bundles.

---

## ⚖ FAIR+CARE & Governance

All KFM documents must reflect FAIR+CARE and sovereignty commitments:

- **FAIR**  
  - *Findable*: use stable paths, IDs, and catalog entries.  
  - *Accessible*: state licenses, access notes, and any restrictions.  
  - *Interoperable*: align with KFM-OP, STAC/DCAT/PROV, and other adopted standards.  
  - *Reusable*: describe scope, assumptions, and limitations clearly.

- **CARE**  
  - When docs describe workflows involving Indigenous data, sensitive sites, or community-held knowledge:
    - Flag them with appropriate front-matter (e.g., additional sensitivity/scope fields in that doc).  
    - Reference relevant governance and sovereignty docs.  
    - Document any constraints, redaction rules, or special review requirements.  

Docs built from this template MUST avoid:

- Exposing sensitive coordinates, PII, or disallowed internal identifiers.  
- Overstating certainty on contested histories, governance policies, or interpretations.  
- Bypassing or contradicting established KFM governance processes.

When in doubt, add a short `⚖ FAIR+CARE & Governance` section and explicitly state whether sensitive or sovereign data is involved.

---

## 🧠 Story Node & Focus Mode Integration (Optional)

If a doc is likely to be used in **Story Nodes** or **Focus Mode**:

- Add a section describing:
  - Which entities, datasets, or APIs Story Nodes might reference.  
  - How Focus Mode should interpret/visualize the subject (e.g., map layers, timelines).  
- Make it easy to:
  - Extract narrative segments for Story Node cards.  
  - Link to `doc_uuid`, `semantic_document_id`, and key graph IDs.  

Always distinguish between:

- **Facts** (data-backed, catalog/graph supported).  
- **Interpretation** (explicitly labeled narrative reading of those facts).  
- **Speculation** (either clearly labeled or omitted).

---

## 🧪 Validation & CI/CD

Docs created from this template should be expected to pass:

- `markdown-lint` — structure, headings, spacing.  
- `schema-validate` — front-matter schema checks.  
- `metadata-check` — presence and coherence of required metadata fields.  
- `provenance-check` — version and integrity metadata consistency.  
- `footer-check` — presence and correctness of the governance footer.  

Where `telemetry_ref` and `telemetry_schema` are present:

- `telemetry-validate` — ensures referenced telemetry bundles match schemas.

If a doc introduces new schemas, modules, or telemetry:

- Extend or create JSON Schemas under `schemas/` or `schemas/telemetry/`.  
- Update CI config (e.g., `.github/workflows/kfm-ci.yml`) to validate the new artifacts.  

Treat failing CI as a **spec problem**, not just an implementation detail.

---

## 🕰️ Version History

| Version   | Date       | Summary                                                                           | Commit        |
|----------:|-----------:|-----------------------------------------------------------------------------------|---------------|
| v11.2.6   | 2025-12-11 | Initial unified core/standard Markdown template aligned with KFM-MDP v11.2.6.     |

---

<div align="center">

📘 **Kansas Frontier Matrix — Core Markdown Template (v11.2.6)**  
Documentation · Standards · Reproducibility  

[📘 Docs Root](../README.md) · [📚 Markdown Standard (KFM-MDP)](../standards/kfm_markdown_protocol_v11.2.6.md) · [🏛 Governance Charter](../standards/governance/ROOT-GOVERNANCE.md)

</div>