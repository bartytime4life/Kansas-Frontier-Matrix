---
title: "Kansas Frontier Matrix (KFM) — CHANGELOG"
doc_kind: "Changelog"
version: "v1.0.0-draft"
date_created: "2025-12-31"
last_updated: "2025-12-31"
author: "TBD (KFM Docs Team)"
status: "draft"
path: "CHANGELOG.md"
repo: "Kansas Frontier Matrix (KFM)"
language: "en"
pipeline_stage: "Docs / Repo Root"
related_docs:
  - "docs/MASTER_GUIDE_v13.md"
  - "docs/standards/KFM_MARKDOWN_FORMATTING_STYLE_GUIDE.md"
  - "docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md"
  - "docs/templates/TEMPLATE__STORY_NODE_V3.md"
  - "docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md"
  - "docs/governance/ROOT_GOVERNANCE.md"
  - "docs/governance/REVIEW_GATES.md"
markdown_protocol_version: "KFM-MDP v11.2.6"
governance_protocol_version: "KFM-GOV v4.1"
pipeline_contract_version: "KFM-PPC v11.0.0"
stac_profile_version: "KFM-STAC v11"
dcat_profile_version: "KFM-DCAT v11"
prov_profile_version: "KFM-PROV v11"
license: "CC-BY-4.0"
fair_category: "FAIR+CARE"
care_label: "Public · Low-Risk"
doc_uuid: "urn:uuid:9f1d2b26-7bdc-45c0-ac56-d73556cd9bef"
---

# CHANGELOG

## 📘 Overview

This file captures *human-readable* project milestones and notable changes for Kansas Frontier Matrix (KFM).

**Important scope note**
- This changelog is seeded from the **project documentation bundle** (Master Guide v12/v13 drafts, Markdown guide, architecture/governance docs, and the provided reference library).
- It is **not** a replacement for Git history. Treat Git commits/tags as the source of truth for code-level diffs.

**Changelog conventions (recommended)**
- Use these headings inside each release entry:
  - **Added** (new capability, new doc/standard, new directory)
  - **Changed** (behavior/contract updates, moved paths, updated invariants)
  - **Deprecated** (still works, but planned removal)
  - **Removed** (deleted or no longer supported)
  - **Fixed** (bugfixes)
  - **Security / Governance** (FAIR+CARE, sovereignty, access boundary changes)

## 🕰️ Changelog

### [Unreleased]
#### Added
- (placeholder)

#### Changed
- (placeholder)

#### Fixed
- (placeholder)

---

### 2025-12-31 — CHANGELOG seed (v1.0.0-draft)
#### Added
- Created `CHANGELOG.md` as the repo-level changelog file.
- Added a “Project file bundle snapshot” section listing the currently supplied project files (to support audits and reproducibility).

#### Notes
- Dates and version labels in older entries below reflect **documented version history** in the Master Guide / Markdown standards docs, and may not correspond to Git tags unless explicitly tagged.

---

### 2025-12-30 — Documentation standard milestone: KFM Markdown Formatting Guide (v1.0.0, draft)
#### Added
- Drafted/updated Markdown governance rules:
  - YAML front-matter requirements (including FAIR+CARE labels)
  - Section/heading standards (emoji-anchored registry)
  - Citation requirements and AI attribution notes
  - Validation expectations for governed docs

---

### 2025-12-28 — Master Guide milestone: v13.0.0-draft (v13 redesign)
#### Added
- v13 “one canonical home per subsystem” structure (contract-first + evidence-first framing).
- Expected repository roots called out explicitly in v13:
  - `schemas/` (contracts: JSON Schemas for catalogs/story/ui/telemetry)
  - `releases/` (release artifacts + auditables, e.g., SBOM/attestations)
  - `data/prov/` and `data/catalog/dcat/` as first-class metadata/lineage roots

#### Changed
- Story content expected under governed path:
  - `docs/reports/story_nodes/` with `draft/` vs `published/` workflow.
- Profiles references updated to the v11 family (STAC/DCAT/PROV), and CI/validation “gates” enumerated as required expectations.

#### Notes
- This milestone supersedes v12 guide structure.

---

### 2025-12-27 — Master Guide milestone: v12.0.1-draft
#### Changed
- Refined doc structure to align with the universal doc template conventions.
- Clarified canonical paths, invariants, and the contract-first / evidence-first boundary language.

---

### 2025-12-17 — Master Guide milestone: v12.0.0-draft
#### Added
- Initial scaffolding for Master Guide v12:
  - Established pipeline ordering conceptually
  - Introduced governance structure baseline

## 🗂️ Directory Layout

**Repo layout is defined by the Master Guide.** A typical v13-style skeleton (illustrative):

- 📁 data/
  - 📁 `<domain>/`
    - 📁 raw/
    - 📁 work/
    - 📁 processed/
    - 📁 mappings/
    - 📄 README.md
  - 📄 README.md
- 📁 docs/
  - 📄 MASTER_GUIDE_v12.md
  - 📄 MASTER_GUIDE_v13.md
  - 📄 glossary.md
  - 📁 architecture/
  - 📁 standards/
  - 📁 templates/
  - 📁 governance/
  - 📁 reports/
    - 📁 story_nodes/
      - 📁 templates/
      - 📁 draft/
      - 📁 published/
- 📁 schemas/
- 📁 src/
  - 📁 pipelines/
  - 📁 graph/
  - 📁 server/
- 📁 web/
- 📁 releases/
- 📁 tests/
- 📁 tools/
- 📄 README.md
- 📄 LICENSE
- 📄 CITATION.cff
- 📄 CHANGELOG.md
- 📄 CONTRIBUTING.md
- 📄 SECURITY.md
- 📄 .editorconfig
- 📄 .pre-commit-config.yaml
- 📄 docker-compose.yml
- 📄 .env.example

## 📚 Project file bundle snapshot

This section records the currently supplied project files used to seed this changelog (helpful for audit/repro).

### Core KFM docs (governing / architectural)
- `KFM Architecture Document.pdf`
- `Kansas Frontier Matrix – Unified Technical Plan.docx`
- `Kansas Frontier Matrix (KFM) – Master Documentation.docx`
- `Inside and Out of GitHub_ A Deep Guide for the Kansas Frontier Matrix.docx`
- `KFM Markdown Guide.docx`

### Reference library (supporting, non-normative)
- `Scientific Modeling and Simulation_ A Comprehensive NASA-Grade Guide.pdf`
- `Understanding Statistics & Experimental Design.pdf`
- `Statistics Done Wrong - Alex_Reinhart-Statistics_Done_Wrong-EN.pdf`
- `Bayesian computational methods.pdf`
- `regression-analysis-with-python.pdf`
- `graphical-data-analysis-with-r.pdf`
- `deep-learning-in-python-prerequisites.pdf`
- `Artificial-neural-networks-an-introduction.pdf`
- `AI Foundations of Computational Agents 3rd Ed.pdf`
- `Data Mining Concepts & applictions.pdf`
- `Data Science &-  Machine Learning (Mathematical & Statistical Methods).pdf`
- `clean-architectures-in-python.pdf`
- `Command Line Kung Fu_ Bash Scripting Tricks, Linux Shell Programming Tips, and Bash One-liners - Command_Line_Kung_Fu_Bash_Scripting_Tricks,_Linux_Shell_Program.pdf`
- `Scalable Data Management for Future Hardware.pdf`
- `Spectral Geometry of Graphs.pdf`
- `Generalized Topology Optimization for Structural Design.pdf`
- `Computer Graphics using JAVA 2D & 3D.pdf`
- `webgl-programming-guide-interactive-3d-graphics-programming-with-webgl.pdf`
- `responsive-web-design-with-html5-and-css3.pdf`
- `Geographic Information System Basics - geographic-information-system-basics.pdf`
- `geoprocessing-with-python.pdf`
- `python-geospatial-analysis-cookbook-over-60-recipes-to-work-with-topology-overlays-indoor-routing-and-web-application-analysis-with-python.pdf`
- `making-maps-a-visual-guide-to-map-design-for-gis.pdf`
- `Google Maps API Succinctly - google_maps_api_succinctly.pdf`
- `google-maps-javascript-api-cookbook.pdf`
- `Cloud-Based Remote Sensing with Google Earth Engine-Fundamentals and Applications.pdf`
- `Google Earth Engine Applications.pdf`
- `Map Reading & Land Navigation` (file present in bundle; extension/format to confirm)

### Referenced in docs but not present in this bundle (to confirm)
- `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` (referenced; not included here)
- `Kansas Frontier Matrix – Unified Template Reference.docx` (referenced; not included here)
- `Kansas Frontier Matrix – Master Reference Index.docx` (referenced; not included here)

## ✅ Updating this file

When you make a PR that changes **contracts, schemas, directory structure, governance rules, or release behavior**, update `CHANGELOG.md` under **[Unreleased]** (or add a dated entry if cutting a release).

If the change is breaking:
- include **Changed** + **Security/Governance** notes as applicable
- link to the governing doc(s) or ADR(s) that justify the break
- ensure corresponding schema/contract versions are bumped

## 🔗 References

- Master Guide v13: `docs/MASTER_GUIDE_v13.md`
- Markdown rules: `docs/standards/KFM_MARKDOWN_FORMATTING_STYLE_GUIDE.md` (and/or Markdown Work Protocol)
- Repo templates: `docs/templates/`
- Governance: `docs/governance/`
