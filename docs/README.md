---
title: "📚 Kansas Frontier Matrix — Documentation Home (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/README.md"

version: "v11.2.6"
last_updated: "2025-12-11"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Autonomous · FAIR+CARE Council Oversight"
content_stability: "stable"

status: "Active / Enforced"
doc_kind: "Documentation Index"
intent: "docs-root-index"
category: "Documentation · Overview · Architecture"

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-version-hash>"
signature_ref: "../releases/v11.2.6/signature.sig"
attestation_ref: "../releases/v11.2.6/slsa-attestation.json"
sbom_ref: "../releases/v11.2.6/sbom.spdx.json"
manifest_ref: "../releases/v11.2.6/manifest.zip"
telemetry_ref: "../releases/v11.2.6/docs-root-telemetry.json"
telemetry_schema: "../schemas/telemetry/docs-root-v11.2.6.json"
energy_schema: "../schemas/telemetry/energy-v2.json"
carbon_schema: "../schemas/telemetry/carbon-v2.json"

governance_ref: "standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"
classification: "Public"
jurisdiction: "Kansas / United States"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"

layout_profiles:
  - "immediate-one-branch-with-descriptions-and-emojis"
badge_profiles:
  - "root-centered-badge-row"
requires_purpose_block: true
requires_directory_layout_section: true
requires_version_history: true
requires_governance_links_in_footer: true

heading_registry:
  approved_h2:
    - "📘 Overview"
    - "🗂️ Directory Layout"
    - "🧭 Context"
    - "🧱 Architecture"
    - "📦 Data & Metadata"
    - "🌐 STAC, DCAT & PROV Alignment"
    - "⚖ FAIR+CARE & Governance"
    - "🧠 Story Node & Focus Mode Integration"
    - "🧪 Validation & CI/CD"
    - "🕰️ Version History"

test_profiles:
  - "markdown-lint"
  - "schema-lint"
  - "metadata-check"
  - "link-check"
  - "footer-check"
  - "provenance-check"

ci_integration:
  workflow: ".github/workflows/docs-lint.yml"
  environment: "dev → staging → production"
---

<div align="center">

# 📚 **Kansas Frontier Matrix — Documentation Home**  
`docs/README.md`

**Central index for KFM’s standards, data docs, architecture notes, templates, events, and telemetry specifications.**  
All documentation here follows **KFM‑MDP v11.2.6**, is **FAIR+CARE aligned**, and is designed to be **machine‑parseable** and **Focus Mode ready**.

[![Docs · MCP‑DL v6.3](https://img.shields.io/badge/Docs-MCP--DL_v6.3-blue)]()  
[![Markdown · KFM‑MDP v11.2.6](https://img.shields.io/badge/Markdown-KFM--MDP_v11.2.6-purple)]()  
[![Data · FAIR+CARE](https://img.shields.io/badge/Data-FAIR%2BCARE-gold)]()  
[![License · CC‑BY 4.0](https://img.shields.io/badge/License-CC--BY_4.0-green)]()  
[![Status · Active / Enforced](https://img.shields.io/badge/Status-Active_%2F_Enforced-brightgreen)]()

</div>

---

## 📘 Overview

The `docs/` tree is the **governed knowledge layer** of the Kansas Frontier Matrix monorepo. It provides:

- Canonical **standards** (Markdown, ontology, governance, security).  
- Domain‑specific **data documentation** (soil, historical, sensing, air, etc.).  
- System **architecture** diagrams and contracts.  
- Reusable **templates** for experiments, model cards, SOPs, and workflows.  
- **Event records** and telemetry specifications for key operational changes.  

Everything in `docs/` is:

- Written in **KFM‑MDP v11.2.6** house style (YAML front‑matter, emoji headings, directory trees).  
- Designed to map cleanly onto **STAC / DCAT / PROV‑O** representations.  
- Enforced via CI/CD workflows (`docs-lint.yml`, `faircare-validate.yml`, telemetry exports).  

Use this file as your **starting point** when navigating or extending documentation.

---

## 🗂️ Directory Layout

High‑level structure under `docs/` (non‑exhaustive but canonical):

~~~text
📚 docs/
  📄 README.md                         — This file (documentation home)

  🧭 overview/                         — High-level introductions & user guides
    📄 getting-started.md              — Onboarding & quickstart
    📄 glossary.md                     — Shared terminology & definitions

  🏛️ architecture/                    — System & subsystem architecture
    📄 README.md                       — Architecture index
    📄 data-architecture.md            — Data flow, ETL layers, storage contracts
    📄 graph-architecture.md           — Neo4j, schemas, and query patterns
    📄 web-architecture.md             — Web stack, Focus Mode & Story Nodes

  📏 standards/                        — Formal standards & governance
    📄 README.md                       — Standards index
    📄 kfm_markdown_protocol_v11.2.6.md — KFM-MDP (Markdown authoring protocol)
    📄 ai_assistant_protocol_v11.2.6.md — AI assistant behavior & output contract
    📁 governance/
      📄 ROOT-GOVERNANCE.md            — Global governance charter
    📁 faircare/
      📄 FAIRCARE-GUIDE.md             — FAIR+CARE & ethics guidance
    📁 sovereignty/
      📄 INDIGENOUS-DATA-PROTECTION.md — Indigenous data sovereignty policy

  📘 data/                             — Data-domain documentation (by theme)
    📄 README.md                       — Data documentation index
    📁 soil/
      📄 README.md                     — Soil domain (SSURGO, SDA, gNATSGO)
    📁 historical/
      📄 README.md                     — Historical data domain index
      📁 land-treaties/                — Treaty & boundary modules (planned/existing)
    📁 sensing/                        — Remote sensing & telemetry domains (planned)
    📁 air/                            — Air quality & atmospheric endpoints (planned)

  🧪 analyses/                         — Analyses, case studies, notebooks (planned)
    📄 README.md

  🧾 templates/                        — Reusable doc templates
    📄 README.md                       — Templates index
    📄 kfm-markdown-template.md        — Core KFM Markdown template
    📄 experiment.md                   — Experiment documentation template
    📄 model_card.md                   — AI/ML model card template
    📄 sop.md                          — Standard Operating Procedure template
    📄 workflow_template.md            — GitHub Actions workflow documentation template

  📰 events/                           — Event & incident documentation
    📄 README.md                       — Events index (planned)
    📁 neo4j/
      📁 fleet-manager/
        📄 README.md                   — Neo4j Fleet Manager integration overview
    📁 remote-sensing/
      📁 jpss/
        📄 README.md                   — JPSS event docs index
        📄 2025-12-11-idps-block-2.3-mx15.md — NOAA JPSS IDPS Mx15 event record

  🧠 agents/                           — AI/agentic system docs
    📁 auto-refresh/
      📄 README.md                     — Auto-refresh agent loop (telemetry-driven PRs)

  📊 telemetry/                        — Telemetry specs & dashboards
    📄 README.md                       — Telemetry docs index (planned)
    📁 reliability-sustainability-correlation/
      📄 README.md                     — Retries/replays ↔ energy/CO₂ correlation telemetry spec

~~~

Conventions:

- `📁` directories, `📄` Markdown/JSON-ish docs, `🧾` for configs/manifests, `🧪` for test fixtures.  
- Trees are fenced with `~~~text` (never inner triple‑backticks).  
- Entries marked “(planned)” are design targets and may not yet exist on disk.

---

## 🧭 Context

The `docs/` tree is the **authoritative narrative and contract layer** for KFM:

- Root `README.md` describes the **monorepo as a whole**.  
- This `docs/README.md` describes the **documentation system** and how it connects to code, data, and graph.  
- Standards and templates here control:
  - How new documents are authored and validated.  
  - How ETL pipelines, datasets, and APIs are described and governed.  
  - How Story Nodes and Focus Mode draw from documentation as a source of truth.

KFM’s canonical pipeline is:

> Deterministic ETL → STAC/DCAT/PROV catalogs → Neo4j → API → React/MapLibre/Cesium → Story Nodes → Focus Mode

Every major document under `docs/` should explain where it sits in this flow.

---

## 🧱 Architecture

From a system perspective, the documentation layer acts as a **governed interface** between humans, code, and data:

- **Standards** under `docs/standards/` define:
  - Markdown house style (KFM‑MDP).  
  - Ontology, governance, FAIR+CARE, sovereignty rules.  
  - AI assistant behavior and allowable transforms.

- **Domain docs** under `docs/data/`:
  - Describe ETL, cataloging, graph mappings, APIs, and UI dependencies per domain (soil, historical, sensing, air, etc.).  
  - Serve as the “front page” for each data domain tree.

- **Templates** under `docs/templates/`:
  - Provide repeatable patterns for experiments, model cards, SOPs, and workflows.  
  - Allow CI to validate that new docs are structurally correct and governance‑compliant.

- **Events & agents** under `docs/events/` and `docs/agents/`:
  - Capture time‑stamped changes in external systems (e.g., NOAA JPSS algorithm shifts, Neo4j Fleet Manager integration).  
  - Document autonomous and semi‑autonomous behaviors (auto‑refresh loops, Focus Mode evolutions).

In KFM’s provenance graph, many `docs/` entries are modeled as `prov:Plan` or `prov:Entity` nodes that shape how data and models are produced and interpreted.

---

## 📦 Data & Metadata

All documentation under `docs/` must:

- Start with **YAML front‑matter**, no blank line before `---`.  
- Use field ordering and required keys as specified in **KFM‑MDP v11.2.6** and relevant templates.  
- Include:
  - Stable identifiers (`path`, `version`, `doc_uuid`, `semantic_document_id` where applicable).  
  - Integrity and provenance fields (`commit_sha`, `previous_version_hash`, `doc_integrity_checksum`).  
  - Governance references (`governance_ref`, `ethics_ref`, `sovereignty_policy` for standards).

Domain‑level READMEs (e.g., `docs/data/soil/README.md`, `docs/data/historical/README.md`) must also:

- Document **ETL entry points** (`src/pipelines/...`).  
- Reference expected **STAC/DCAT/PROV** outputs.  
- Describe **graph entities and relationships** used (`src/graph/...`, KFM‑OP labels).  
- List dependent **APIs** and **UI surfaces**.

Templates under `docs/templates/` are the preferred starting point for new documents.

---

## 🌐 STAC, DCAT & PROV Alignment

Documentation is part of KFM’s metadata ecosystem:

- **DCAT**  
  - Collections of docs (e.g., standards, templates, domain READMEs) can be modeled as `dcat:Dataset` groups.  
  - Individual files are `dcat:Distribution` entries with `mediaType: text/markdown` and `dct:modified = last_updated`.

- **STAC**  
  - Documentation may live in a `kfm-docs` STAC Collection (non‑spatial) with:
    - `id` mapped from `semantic_document_id`.  
    - `properties.datetime = last_updated`.  
    - `assets` pointing at raw Markdown and rendered forms.

- **PROV‑O**  
  - Standards and templates: `prov:Plan`.  
  - Versioned documents: `prov:Entity` with `prov:wasDerivedFrom` entries in `provenance_chain` where used.  
  - CI workflows that validate or publish docs: `prov:Activity` linked via `prov:wasGeneratedBy` to telemetry bundles and release manifests.

Keeping docs aligned with these profiles ensures they are discoverable, auditable, and linkable from the knowledge graph.

---

## ⚖ FAIR+CARE & Governance

The documentation layer is a primary enforcement point for **FAIR+CARE**:

- **FAIR**  
  - **Findable**: stable paths, versioned filenames, and consistent identifiers.  
  - **Accessible**: CC‑BY 4.0 licensing for docs, clear governance links, public repo visibility.  
  - **Interoperable**: adherence to KFM‑MDP, ontology protocols, and catalog profiles.  
  - **Reusable**: version histories, integrity checks, and clear scopes/limitations.

- **CARE**  
  - Documents that touch Indigenous data, sensitive sites, or community‑held knowledge must:
    - Reference sovereignty policies and CARE guidance.  
    - Explicitly describe masking/generalization rules and access tiers.  
    - Avoid disclosing sensitive locations or PII beyond what governance allows.

Governance is operationalized via:

- Standards under `docs/standards/`.  
- Council reviews (FAIR+CARE, Focus Mode Board, domain working groups).  
- Automated checks in CI/CD (FAIR+CARE validators, sovereignty rule checks where applicable).

---

## 🧠 Story Node & Focus Mode Integration

Most `docs/` entries are **Story Node–friendly**:

- Overviews, architecture sections, and domain READMEs provide **explainable context** that Focus Mode can surface alongside data and graph queries.  
- Versioned standards and templates help Focus Mode explain **why** a dataset or model behaves a certain way (pointing back to contracts and SOPs).  
- Event docs and telemetry specs provide **temporal context** around changes in algorithms, pipelines, or governance.

Focus Mode treats documentation as:

- A governed, non‑speculative source.  
- Something to **summarize and cite**, not rewrite or override.  
- A path to deeper provenance: from narrative → doc → dataset → graph nodes → raw assets.

---

## 🧪 Validation & CI/CD

Documentation is part of the **critical path** in KFM’s CI/CD:

- `docs-lint.yml`  
  - Validates Markdown structure, headings, front‑matter, directory layouts, and Mermaid diagrams.  

- `faircare-validate.yml`  
  - Checks for FAIR+CARE alignment, ethical notes, and basic sensitivity flags.  

- `schema-lint` (where configured)  
  - Confirms front‑matter matches expected schemas for standards, domain docs, and templates.  

- `telemetry-export.yml`  
  - Aggregates documentation events and metrics into `focus-telemetry.json` and related ledgers.

Adding or modifying docs under `docs/` should be expected to:

- Trigger these workflows.  
- Update relevant telemetry (e.g., `docs-root-telemetry.json`, template usage metrics).  
- Contribute to provenance and governance reports under `reports/` (where present).

---

## 🕰️ Version History

| Version  | Date       | Summary                                                                                              |
|---------:|------------|------------------------------------------------------------------------------------------------------|
| v11.2.6  | 2025-12-11 | Aligned docs index to KFM‑MDP v11.2.6; added directory layout, CI/telemetry references, and governance wiring. |
| v11.2.3  | 2025-12-04 | Initial v11 docs home alignment with monorepo layout; established role as documentation root index.  |

---

<div align="center">

📚 **Kansas Frontier Matrix — Documentation Home (v11.2.6)**  
Documentation‑First · FAIR+CARE Governance · Catalog & Graph Ready  

[⬅ Back to Monorepo Root](../README.md) ·  
[📘 Markdown Protocol (KFM‑MDP v11.2.6)](standards/kfm_markdown_protocol_v11.2.6.md) ·  
[⚖ Governance Charter](standards/governance/ROOT-GOVERNANCE.md)

</div>