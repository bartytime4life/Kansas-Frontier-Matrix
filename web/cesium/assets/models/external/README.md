---
title: "Cesium External Models — README"
path: "web/cesium/assets/models/external/README.md"
version: "v1.0.0"
last_updated: "2025-12-24"
status: "draft"
doc_kind: "README"
license: "CC-BY-4.0"

markdown_protocol_version: "KFM-MDP v11.2.6"
mcp_version: "MCP-DL v6.3"
ontology_protocol_version: "KFM-ONTO v4.1.0"
pipeline_contract_version: "KFM-PPC v11.0.0"
stac_profile: "KFM-STAC v11.0.0"
dcat_profile: "KFM-DCAT v11.0.0"
prov_profile: "KFM-PROV v11.0.0"

governance_ref: "docs/governance/ROOT_GOVERNANCE.md"
ethics_ref: "docs/governance/ETHICS.md"
sovereignty_policy: "docs/governance/SOVEREIGNTY.md"
fair_category: "FAIR+CARE"
care_label: "TBD"
sensitivity: "public"
classification: "open"
jurisdiction: "US-KS"

doc_uuid: "urn:kfm:doc:web:cesium:assets:models:external:readme:v1.0.0"
semantic_document_id: "kfm-web-cesium-assets-models-external-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:web:cesium:assets:models:external:readme:v1.0.0"
commit_sha: "<latest-commit-hash>"

ai_transform_permissions:
  - "summarize"
  - "structure_extract"
  - "translate"
  - "keyword_index"
ai_transform_prohibited:
  - "generate_policy"
  - "infer_sensitive_locations"

doc_integrity_checksum: "sha256:<calculate-and-fill>"
---

# Cesium External Models — README

## 📘 Overview

### Purpose

- Define what belongs in `web/cesium/assets/models/external/`.
- Ensure any **third-party model** used by the Cesium UI is stored with clear **source + license + attribution**.
- Reduce supply-chain and governance risk by preventing “mystery assets” from entering the UI surface.

> This README documents **folder-level conventions** only. It does **not** replace repo governance documents.

### Scope

| In Scope | Out of Scope |
|---|---|
| Third-party / externally sourced 3D assets (e.g., `.glb`, `.gltf`, textures) vendored into the repo for the Cesium UI | Runtime build outputs, caches, or generated artifacts |
| Attribution + license metadata for each external model | KFM-produced models derived from KFM datasets (location **not confirmed in repo**; do not store those here by default) |
| Minimal validation expectations for assets before commit | Any new “policy” beyond what is defined in `docs/governance/**` |

### Audience

- **Primary:** UI contributors adding/updating Cesium models.
- **Secondary:** maintainers/reviewers verifying license compliance and sensitive-content risk.

### Definitions (link to glossary)

- Link: `docs/glossary.md` *(not confirmed in repo)*
- Terms used in this doc:
  - **glTF / GLB:** 3D model exchange format (GLB = binary glTF).
  - **Attribution:** creator/source credit required by a license.
  - **Redistribution:** permission to include the asset in this repository.

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master Guide | `docs/MASTER_GUIDE_v12.md` | TBD | Canonical pipeline ordering + invariants |
| Governance root | `docs/governance/ROOT_GOVERNANCE.md` | TBD | Review gates and classification rules |
| Ethics policy | `docs/governance/ETHICS.md` | TBD | Sensitive-content handling |
| Sovereignty policy | `docs/governance/SOVEREIGNTY.md` | TBD | Authority-to-control and location sensitivity |
| Universal doc template | `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` | TBD | Structure for governed docs (optional for per-model docs) |

### Definition of done (for this document)

- [ ] Front-matter complete + valid (`path:` matches the file location).
- [ ] Clear definition of what “external model” means in this repo.
- [ ] Per-model metadata requirements are explicit and include licensing.
- [ ] Validation steps are listed and repeatable (or marked “not confirmed in repo” where tooling is unknown).
- [ ] Governance + CARE/sovereignty considerations are explicitly stated.

## 🗂️ Directory Layout

### This document

- `path`: `web/cesium/assets/models/external/README.md`

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| UI root | `web/` | Front-end code + static assets |
| Cesium assets | `web/cesium/assets/` | Static assets consumed by Cesium UI |
| Models root | `web/cesium/assets/models/` | Model assets (external + other model groups if present) |
| Governance | `docs/governance/` | Ethics + sovereignty + review gates |

### Expected file tree for this sub-area

> Keep this tree synchronized with the actual contents of `external/`. If you add new conventions, update this README in the same PR.

~~~text
📁 web/
└── 📁 cesium/
    └── 📁 assets/
        └── 📁 models/
            └── 📁 external/
                ├── 📄 README.md
                ├── 📁 <model_slug>/
                │   ├── 📄 SOURCE_AND_LICENSE.md
                │   ├── 📄 ATTRIBUTION.md
                │   ├── 📄 LICENSE.txt  (or COPYING / LICENSE.md)
                │   ├── 📄 <model_name>.glb
                │   └── 📁 textures/ (optional)
                │       └── 🖼️ <texture_files>
                └── 📁 <another_model_slug>/
                    └── …
~~~

## 🧭 Context

### Why we vendor external models

- The UI is part of KFM’s public-facing surface; static assets should be reproducible and reviewable.
- External models are effectively a **dependency**; we need at least basic provenance (source, version, license) to review and maintain them.

### What “external” means here

A model is considered **external** if any of the following are true:

- It was downloaded from a third-party repository / marketplace / demo pack.
- It was provided by a vendor or collaborator and is not clearly authored/owned by KFM.
- Its license terms require attribution or impose redistribution constraints.

## 🧱 Architecture

### Relationship to the canonical pipeline

- These are **UI assets**, not evidence artifacts (not STAC/DCAT/PROV outputs).
- Do not treat external models as “data products” or use them to introduce unsourced claims in Story Nodes.
- If an external model is used to visually represent historically sensitive places/objects, treat that as a **governance review trigger** (see the governance section below).

## 📦 Data & Metadata

### Per-model required metadata

Every model folder under `external/<model_slug>/` should include, at minimum:

- `SOURCE_AND_LICENSE.md` — where the model came from and the redistribution/license basis
- `ATTRIBUTION.md` — the exact credit text required (if any)
- `LICENSE.*` — the license text itself if redistribution requires it, or if the source license requires including the license file

**If any of these are unclear, do not commit the asset yet — route for review per `docs/governance/ROOT_GOVERNANCE.md`.**

### Suggested content for `SOURCE_AND_LICENSE.md`

~~~markdown
# <Model Name> — Source and License

## Source
- Upstream name: <vendor/project>
- Upstream URL: <https://example.com/...>
- Retrieved on: <YYYY-MM-DD>
- Upstream version/tag/commit: <vX.Y.Z or hash>
- Original filename(s): <...>

## License
- License name: <e.g., CC-BY-4.0 / MIT / custom>
- Redistribution allowed: <Yes/No/Unclear>
- Modification allowed: <Yes/No/Unclear>
- Attribution required: <Yes/No>
- Notes / constraints: <...>

## Transform / Conversion notes
- Original format: <...>
- Converted to: <.glb/.gltf>
- Tools used: <not confirmed in repo>
- Steps: <brief list>
- Known limitations: <...>

## Where used in KFM
- UI reference(s): <file/module path(s) — not confirmed in repo>
- Screenshot (optional): <path if committed>
~~~

## 🧪 Validation & CI/CD

### Validation steps (recommended)

> Commands/tools are intentionally not specified unless they exist in-repo (**not confirmed in repo**).

- [ ] Confirm license permits redistribution in this repository.
- [ ] Confirm required attribution text is captured (and present at runtime, if needed).
- [ ] Validate the model loads in the local Cesium UI without external network fetches (textures/resources are local).
- [ ] Check that file sizes are reasonable for web delivery (thresholds **not confirmed in repo**).
- [ ] Scan for accidental secrets/credentials in any accompanying metadata files (should be none).

## ⚖ FAIR+CARE & Governance

### Review gates

Treat any of the following as a review trigger:

- Adding an external model with **unclear or custom licensing**
- Adding an external model that depicts **culturally sensitive** objects, locations, or contexts
- Adding a model that could indirectly reveal sensitive locations through interaction/zoom or embedded annotations

### CARE / sovereignty considerations

- This directory is “UI,” but it can still create harm if it introduces sensitive representations.
- If a model is tied to sovereignty-controlled knowledge or sensitive sites, follow `docs/governance/SOVEREIGNTY.md` (and prefer non-sensitive/abstract representations where appropriate).

### AI usage constraints

- This README’s AI permissions/prohibitions are for documentation transforms only.
- Do not use AI to “guess” licensing or infer sensitive locations; licensing and sensitivity must be verified by humans and/or authoritative sources.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-24 | Initial README for Cesium external model asset conventions | TBD |

---

## Footer refs (do not remove)

- Master guide: `docs/MASTER_GUIDE_v12.md`
- Template: `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
- Ethics: `docs/governance/ETHICS.md`
---
