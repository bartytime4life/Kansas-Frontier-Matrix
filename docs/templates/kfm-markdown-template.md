---
title: "📘 Kansas Frontier Matrix — Core Markdown Template"
path: "docs/templates/kfm-markdown-template.md"
version: "v11.2.6"
last_updated: "2025-12-11"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · FAIR+CARE Council"
content_stability: "stable"
status: "Active"

doc_kind: "Standard Template"
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
governance_ref: "../standards/governance/ROOT-GOVERNANCE.md"
---

# 📘 Kansas Frontier Matrix — Core Markdown Template (v11.2.6)

## 📘 Overview

This file provides the **canonical template** for producing KFM-compliant documentation under **KFM-MDP v11.2.6**.  
All new Markdown documents should follow this structure, including:

- YAML front-matter fields and ordering  
- H1/H2 heading patterns (emoji + label)  
- Directory layout style (emoji + ASCII tree)  
- Governance footer format  

The template is intended for:

- STAC/DCAT/PROV-aligned data-domain READMEs  
- Architecture and design notes  
- Telemetry and governance specs  
- Event summaries and incident reports  

When AI assistants generate drafts for this template, the **transport format** in ChatGPT is a single fenced `markdown` block; once saved in the repo, the file is stored as normal Markdown with YAML front-matter at the top.

---

## 🗂️ Directory Layout

This template lives under `docs/templates/` and governs how other docs should represent directory trees.

~~~text
📁 docs/
  📁 templates/
    📄 kfm-markdown-template.md   # This file – core KFM-MDP v11.2.6 markdown template
~~~

**Directory layout rules:**

- Use emojis:
  - `📁` directories
  - `📄` markdown/text
  - `🧾` JSON/YAML/config
  - `🧪` tests/fixtures
  - `🖼️` images/media
- Use `📁` / `📄` + short description comments where helpful.
- Use `~~~text` fences for directory trees (never nested ``` inside KFM docs).
- Keep paths **relative to the file** and stable across refactors whenever possible.

---

## 🧭 Context

This template is the **baseline** for all KFM docs and is aligned with:

- `docs/standards/kfm_markdown_protocol_v11.2.6.md` (KFM-MDP)  
- KFM-OP v11 ontologies and graph modeling  
- KFM-PDC v11 pipeline contracts and governance patterns  

Recommended H2 sections (drawn from the global heading registry):

- `📘 Overview`  
- `🗂️ Directory Layout`  
- `🧭 Context`  
- `🧱 Architecture`  
- `📦 Data & Metadata`  
- `🌐 STAC, DCAT & PROV Alignment`  
- `⚖ FAIR+CARE & Governance`  
- `🧠 Story Node & Focus Mode Integration`  
- `🧪 Validation & CI/CD`  
- `🕰️ Version History`  

Not every doc needs all headings, but:

- **Overview** and **Version History** are required.  
- A **Directory Layout** section is required for domain/area READMEs and core standards.  

---

## 🧱 Architecture Alignment

Each KFM document should explain how its subject fits into the core pipeline:

> Deterministic ETL → STAC/DCAT/PROV catalogs → Neo4j → API → React/MapLibre/Cesium → Story Nodes → Focus Mode

At minimum, authors should specify:

- Which **ETL pipelines** are relevant (`src/pipelines/...`).
- Which **catalogs** are produced/consumed (`data/stac/`, `data/*/dcat/`, `data/*/dcat-prov/`).
- Which **graph entities** and relationships are involved (`src/graph/...`, KFM-OP labels).
- Which **APIs** expose the results (`src/api/...`).
- Which **UI areas** depend on this work (`src/web/...`, Focus Mode panels, Story Nodes).

Architecture sections should be:

- Descriptive enough for new contributors to orient themselves.
- Precise enough that CI, telemetry, and governance can reference specific modules.

---

## 📦 Data & Metadata

### Front-Matter Requirements

Every KFM document MUST:

- Start with a single YAML front-matter block, no blank lines above `---`.
- Include (at minimum) the following keys in this order (when applicable):

  1. `title`  
  2. `path`  
  3. `version`  
  4. `last_updated`  
  5. `release_stage`  
  6. `lifecycle`  
  7. `review_cycle`  
  8. `content_stability`  
  9. `status`  
  10. `doc_kind`  
  11. `header_profile`  
  12. `footer_profile`  
  13. `license`  
  14. `mcp_version` (if relevant)  
  15. `markdown_protocol_version`  
  16. `ontology_protocol_version`  
  17. `pipeline_contract_version`  
  18. `stac_profile`  
  19. `dcat_profile`  
  20. `prov_profile`  
  21. provenance & integrity fields (`commit_sha`, `previous_version_hash`, `doc_integrity_checksum`)  
  22. identifier fields (`semantic_document_id`, `doc_uuid`, `event_source_id`, `immutability_status`)  
  23. references (`sbom_ref`, `manifest_ref`, `telemetry_ref`, `governance_ref`, etc.)

Additional fields (scope, sensitivity, heading registry, etc.) may be added as needed for standards and domain docs.

### Content Metadata

Within the body, authors SHOULD:

- State explicit **scope** and **role** of the doc (what it governs and what it does not).
- Reference related docs via **relative paths** (e.g. `../standards/...`, `../../data/...`).
- Document any **associated schemas** under `schemas/` and telemetry under `schemas/telemetry/`.

---

## 🌐 STAC, DCAT & PROV Alignment

For data and catalog-related docs, authors should use this template to:

- Declare how STAC Collections/Items are structured and linked.
- Explain how DCAT Datasets and Distributions represent the same assets.
- Show how PROV-O captures lineage:

  - `prov:Entity` (datasets, docs, models),
  - `prov:Activity` (ETL runs, AI inferences),
  - `prov:Agent` (teams, automated systems).

Even for purely textual docs (like this template), the **front-matter** plus **provenance fields** enable STAC/DCAT/PROV alignment through doc catalogs.

---

## ⚖ FAIR+CARE & Governance

All KFM documents must reflect KFM’s FAIR+CARE and sovereignty commitments:

- **FAIR**  
  - Make docs and datasets **Findable** and **Interoperable** via stable IDs, paths, and schemas.  
  - Ensure **Accessibility** (license, access notes) and **Reusability** (clear scope and caveats).

- **CARE**  
  - When docs describe workflows that touch Indigenous data, sensitive sites, or community-held knowledge:
    - Flag them using appropriate front-matter fields (`indigenous_rights_flag`, sensitivity levels in other docs).  
    - Reference relevant governance and sovereignty docs.  
    - Explicitly state any constraints, redaction rules, or special review requirements.

Docs built from this template MUST avoid:

- Exposing sensitive coordinates or PII.
- Overstating certainty on contested histories or governance policies.
- Bypassing KFM governance processes.

---

## 🧪 Validation & CI/CD

Docs created from this template should be expected to pass:

- `markdown-lint` — structure, headings, spacing.  
- `schema-validate` — front-matter schema checks.  
- `provenance-check` — presence and consistency of version and integrity fields.  
- `telemetry-validate` — where `telemetry_ref` and related schemas are present.  

Optional but recommended checks:

- `footer-check` — ensures presence of governance footer.  
- `link-check` — validates internal relative links.  

When introducing a new doc type or pattern, authors should:

- Update any relevant schemas under `schemas/`.  
- Update CI config (e.g., `.github/workflows/kfm-ci.yml`) if new checks are required.

---

## 🕰️ Version History

| Version   | Date       | Summary                                      | Commit        |
|----------:|-----------:|----------------------------------------------|---------------|
| v11.2.6   | 2025-12-11 | Initial template standardization for KFM-MDP | `<latest-sha>` |

---

<div align="center">

📘 **Kansas Frontier Matrix — Core Markdown Template (v11.2.6)**  
Documentation · Standards · Reproducibility  

[📘 Docs Root](../README.md) · [📚 Markdown Standard (KFM-MDP)](../standards/kfm_markdown_protocol_v11.2.6.md) · [🏛 Governance Charter](../standards/governance/ROOT-GOVERNANCE.md)

</div>