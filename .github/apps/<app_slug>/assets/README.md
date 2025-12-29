---
title: "GitHub Apps — <app_slug> — Assets"
path: ".github/apps/<app_slug>/assets/README.md"
version: "v1.0.0"
last_updated: "2025-12-29"
status: "draft"
doc_kind: "Guide"
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

doc_uuid: "urn:kfm:doc:github:apps:<app_slug>:assets-readme:v1.0.0"
semantic_document_id: "kfm-github-apps-<app_slug>-assets-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:github:apps:<app_slug>:assets-readme:v1.0.0"
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

# GitHub Apps — <app_slug> — Assets

## 📘 Overview

### Purpose

- Provide a tracked, **secret-free** home for diagrams, screenshots, and other supporting artifacts referenced by the GitHub App documentation for `<app_slug>`.
- Ensure visuals used in GitHub App operational docs remain aligned with KFM constraints: public-safe content, sovereignty-aware handling, and contract-first boundaries.

### Scope

| In Scope | Out of Scope |
|---|---|
| Exported diagrams (`.svg`, `.png`), sanitized screenshots, diagram source files (`.mmd`, `.drawio`, `.excalidraw`) when safe, attribution records | Private keys, webhook secrets, installation tokens, PATs; screenshots/logs revealing credentials; any KFM datasets or catalog artifacts (STAC/DCAT/PROV); Story Node assets; proprietary media without clear license/attribution |

### Audience

- Primary: maintainers of `.github/apps/<app_slug>/`
- Secondary: security reviewers validating that automation docs and visuals do not leak secrets/PII/sensitive locations

### Definitions

- Glossary link: `docs/glossary.md` *(expected canonical location; if missing, mark “not confirmed in repo” and link to the repo’s actual glossary path)*
- Terms used in this doc:
  - **Documentation asset**: an image/diagram committed solely to support documentation.
  - **Source diagram**: an editable file used to regenerate an export (e.g., `.mmd`, `.drawio`).
  - **Sanitized screenshot**: a screenshot with secrets, identifying info, and sensitive location details removed/generalized.

### Key artifacts

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Apps overview | `.github/apps/README.md` | Repo maintainers | Contract for GitHub App docs + folder rules |
| App docs | `.github/apps/<app_slug>/README.md` | App owner | Primary app documentation |
| This assets README | `.github/apps/<app_slug>/assets/README.md` | App owner | What belongs here and how to manage it |
| Permission justification | `.github/apps/<app_slug>/permissions.md` | App owner + Security | Least privilege mapping + rationale |
| Workflow mapping | `.github/apps/<app_slug>/workflows.md` | CI owners | Workflows/jobs that depend on the app |
| Apps inventory | `.github/apps/inventory.md` | Repo maintainers | Optional; lists all apps and where used |

### Definition of done

- [ ] Front-matter complete + valid (path/version/last_updated)
- [ ] Assets are safe to disclose in a public repo (no secrets, no sensitive-location leakage)
- [ ] Every non-trivial asset is recorded in the Asset inventory table in this file
- [ ] Links from `.github/apps/<app_slug>/*.md` resolve (no broken relative links)
- [ ] External/third-party media has attribution and licensing recorded
- [ ] Validation checklist below is repeatable

## 🗂️ Directory Layout

### This document

- `path`: `.github/apps/<app_slug>/assets/README.md` *(must match front-matter)*

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| GitHub Apps docs | `.github/apps/` | App manifests + permission/workflow docs (secret-free) |
| Workflows | `.github/workflows/` | CI/CD pipelines that may call GitHub APIs |
| Documentation | `docs/` | Canonical governed docs (architecture, standards, runbooks) |
| Pipelines | `src/pipelines/` | ETL + catalog generation code |
| Graph | `src/graph/` | Ontology bindings, ingest/migrations |
| API boundary | `src/server/` | Contracted access layer; redaction enforcement |
| UI | `web/` | React + MapLibre (+ optional Cesium) |
| Story Nodes | `docs/reports/story_nodes/` *(pattern)* | Narrative artifacts + assets |

### Expected file tree for this sub-area

~~~text
📁 .github/
└── 📁 apps/
    └── 📁 <app_slug>/
        ├── 📄 README.md
        ├── 📄 permissions.md
        ├── 📄 manifest.json
        ├── 📄 workflows.md
        ├── 📄 rotation.md                      # optional
        └── 📁 assets/
            ├── 📄 README.md                    # this file (keeps the folder tracked in git)
            ├── 🖼️ diagram--auth-flow.svg       # example
            ├── 🖼️ diagram--permissions.svg     # example
            ├── 🖼️ screenshot--settings.png     # example (sanitized)
            └── 📄 attribution.md               # optional but recommended when using external media
~~~

## 🧭 Context

### What belongs in this folder

This folder is for **documentation-only** artifacts used to explain:

- the GitHub App’s permission model (diagrams, tables, screenshots),
- authentication flows (high-level token minting and usage patterns),
- operational runbooks (rotation flow charts),
- validation gates (what checks run and when).

### What must not go in this folder

Do not commit:

- any credential material (private keys, webhook secrets, installation tokens, or screenshots/logs that reveal them),
- any data lifecycle outputs (`data/**`), or catalog/provenance artifacts (`data/stac/**`, `data/catalog/dcat/**`, `data/prov/**`),
- Story Node media (story assets belong under `docs/reports/story_nodes/**`).

### Key invariants

- Treat `.github/apps/**` as public-facing documentation: **no secrets** and no sensitive-location leakage.
- When visuals depict KFM runtime flow, preserve the canonical ordering:
  - **ETL → STAC/DCAT/PROV → Graph → API → UI → Story Nodes → Focus Mode**
- UI never reads Neo4j directly; UI uses contracted APIs.

### Future extensions

- Add a lightweight CI validator to:
  - ensure this folder exists for each app,
  - ensure links resolve,
  - ensure the asset inventory table is maintained.

## 🗺️ Diagrams

### Documentation flow

~~~mermaid
flowchart LR
  A[.github/apps/<app_slug>/README.md] -->|references| B[assets/*]
  A --> C[permissions.md]
  A --> D[workflows.md]
  D --> E[.github/workflows/*]
~~~

### Recommended diagram types

- **Auth flow**: how workflows mint and use GitHub App installation tokens (high-level, no secrets).
- **Permissions mapping**: which permissions are required by which workflows/jobs.
- **Rotation runbook**: key rotation steps and review gates (no secret values).

## 📦 Data & Metadata

### Asset inventory

Record each committed asset and its provenance so reviewers can validate safety and licensing.

| File | Type | Purpose | Source / How generated | License / attribution | Sensitivity notes |
|---|---|---|---|---|---|
| `diagram--auth-flow.svg` | Diagram | Explain GitHub App auth path | Exported from Mermaid/Draw.io | CC-BY-4.0 / internal | Must not show secret names/values |
| `screenshot--settings.png` | Screenshot | Show config UI (sanitized) | Taken from GitHub UI, redacted | GitHub UI / review | Must blur tokens/user emails |

> If you add any third-party media (logos, photos, screenshots with external content), add `assets/attribution.md` and record source + license/permission there.

### Inputs

| Input | Format | Where from | Validation / constraints |
|---|---|---|---|
| Diagram sources | `.mmd`, `.drawio`, `.excalidraw` | Authoring tools | Must be secret-free and reproducible |
| Exported diagrams | `.svg`, `.png` | Exports from source | Prefer SVG for diffability; sanitize content |
| Screenshots | `.png` | GitHub UI / tooling UI | Must be sanitized; avoid PII/secrets |

### Outputs

| Output | Format | Where recorded | Contract / notes |
|---|---|---|---|
| Documentation assets | Images + source files | `.github/apps/<app_slug>/assets/` | Documentation-only; safe-to-disclose |
| References in docs | Markdown links | `.github/apps/<app_slug>/*.md` | Relative links should resolve |

### Sensitivity & redaction

- Remove or blur:
  - tokens, private keys, webhook secrets, installation IDs,
  - usernames/emails (when not required),
  - any location identifiers that could be considered sensitive under sovereignty guidance.
- When in doubt: do not commit the image; describe the procedure in text instead.

### Quality signals

- Assets are minimal, relevant, and referenced by docs.
- Diagrams are reproducible (source exists or Mermaid is used in Markdown).
- No broken links.
- Secret/PII scans pass.

## 🌐 STAC, DCAT & PROV Alignment

This folder does **not** contain KFM datasets or catalog artifacts.

- If an automation workflow publishes STAC/DCAT/PROV outputs, they must go to canonical homes:
  - `data/stac/`
  - `data/catalog/dcat/`
  - `data/prov/`

## 🧱 Architecture

### How assets are consumed

Assets in this folder are referenced by:

- `.github/apps/<app_slug>/README.md`
- `.github/apps/<app_slug>/permissions.md`
- `.github/apps/<app_slug>/workflows.md`
- (optionally) `.github/apps/inventory.md`

### Contract boundary reminders

- This assets folder does not change runtime architecture.
- Diagrams depicting runtime flows must preserve canonical ordering and the API boundary.

## 🧠 Story Node & Focus Mode Integration

- Story Node assets belong under `docs/reports/story_nodes/**` (not here).
- If a GitHub App–authenticated workflow produces narrative artifacts:
  - the narrative bundle must include provenance links and evidence pointers,
  - and must follow “do not infer sensitive locations” constraints.

## 🧪 Validation & CI/CD

### Validation checklist

- [ ] Secret scan passes for all files under `.github/apps/<app_slug>/assets/`
- [ ] No screenshots include token values, private keys, webhook secrets, or installation tokens
- [ ] Links from `.github/apps/<app_slug>/*.md` to `assets/*` resolve
- [ ] Every asset is listed in the Asset inventory table (or explicitly marked trivial)
- [ ] If third-party media is used, `assets/attribution.md` exists and is filled

### Optional CI ideas

- Image lint: fail on disallowed extensions, oversized binaries, or missing inventory entries.
- Link checker: fail on broken relative links within `.github/apps/**`.

## ⚖ FAIR+CARE & Governance

### Governance review triggers

- Adding screenshots/diagrams that could reveal sensitive locations or identities
- Adding third-party media with unclear licensing
- Any asset that appears in public-facing docs and could be interpreted as evidence or authoritative data

### Sovereignty safety

- Do not commit imagery that reveals restricted sites or sensitive geographies at high precision.
- If location context is required, generalize the visualization (region-level) and document the generalization.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-29 | Initial assets README for per-app GitHub App documentation | TBD |

---

Footer refs (canonical pointers):

- Apps overview: `.github/apps/README.md`
- App docs: `.github/apps/<app_slug>/README.md`
- Master Guide: `docs/MASTER_GUIDE_v12.md`
- Universal template: `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`
- Markdown work protocol: `docs/standards/KFM_MARKDOWN_WORK_PROTOCOL.md` *(not confirmed in repo)*
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
