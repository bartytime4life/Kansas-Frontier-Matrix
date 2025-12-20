---
title: "Research Draft Assets — README"
path: "docs/research/drafts/assets/README.md"
version: "v0.1.0"
last_updated: "2025-12-20"
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

doc_uuid: "urn:kfm:doc:research:drafts:assets-readme:v0.1.0"
semantic_document_id: "kfm-research-drafts-assets-readme-v0.1.0"
event_source_id: "ledger:kfm:doc:research:drafts:assets-readme:v0.1.0"
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

# Research Draft Assets — README

## 📘 Overview

### Purpose
This directory holds **supporting assets for research drafts** under `docs/research/drafts/`, such as:
- figures, screenshots, diagrams, and small visual exports that are embedded in draft Markdown
- draft-only “evidence illustrations” that help reviewers understand a work-in-progress

This is **not** a substitute for canonical pipeline outputs (`data/...` + STAC/DCAT/PROV) and should not be treated as an authoritative data store.

### Scope

| In Scope | Out of Scope |
|---|---|
| Draft figures (PNG/SVG/PDF), diagrams (Mermaid render exports), screenshots for documentation, small non-sensitive illustrations | Raw/processed datasets; canonical map layers; anything requiring STAC/DCAT/PROV publication; sensitive or restricted material; large binaries that bloat Git history |

### Audience
- Primary: contributors authoring or reviewing research drafts
- Secondary: maintainers curating/promoting draft outputs into governed reports/story nodes

### Definitions (link to glossary)
- Glossary (if present): `docs/glossary.md`
- Terms used in this doc:
  - **Draft**: exploratory documentation not yet promoted to governed outputs
  - **Asset**: a file referenced by a draft (image, diagram export, etc.)
  - **Promotion**: moving stabilized draft artifacts to canonical locations with provenance

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Assets folder | `docs/research/drafts/assets/` | Docs maintainers | Draft-only supporting files |
| Draft docs | `docs/research/drafts/` | Authors | Where assets are referenced from |
| Canonical story nodes | `docs/reports/<…>/story_nodes/` | Editors + reviewers | Promote stable narrative outputs here |
| Canonical data outputs | `data/` + `data/stac/` | Data/pipeline owners | Promote stable data products here |

### Definition of done (for this document)
- [ ] Front-matter complete + `path` matches file location
- [ ] Clear guidance on what belongs here vs what must live in `data/` / `docs/reports/`
- [ ] Guidance does not imply UI reads graph directly (API boundary preserved)
- [ ] Sensitivity and provenance expectations stated for draft assets
- [ ] File tree + naming guidance included

## 🗂️ Directory Layout

### This document
- `path`: `docs/research/drafts/assets/README.md`

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| Research drafts | `docs/research/drafts/` | Exploratory writeups and working notes |
| Draft assets | `docs/research/drafts/assets/` | Images/figures used by drafts |
| Governed narrative outputs | `docs/reports/<…>/story_nodes/` | Provenance-linked story nodes ready for Focus Mode |
| Data domains | `data/` | Raw/work/processed datasets (not docs assets) |
| STAC catalogs | `data/stac/` | Machine-validated catalog entries for data assets |
| Governance | `docs/governance/` | Ethics/sovereignty and governance policies |

### Expected file tree for this sub-area
(Recommended layout; create subfolders only as needed.)

~~~text
📁 docs/
└── 📁 research/
    └── 📁 drafts/
        ├── 📁 assets/
        │   ├── 📄 README.md
        │   ├── 📁 images/        (optional)
        │   ├── 📁 diagrams/      (optional)
        │   ├── 📁 figures/       (optional)
        │   └── 📁 exports/       (optional)
        └── 📁 <draft-topic>/     (optional)
            ├── 📄 README.md      (optional)
            └── 📄 <draft>.md     (optional)
~~~

## 🧭 Context

### Background
Draft research work benefits from keeping “explainers” (figures/diagrams) close to the draft text.
This folder provides a predictable place for those assets without polluting:
- `data/` (for datasets and pipeline outputs)
- `docs/reports/` (for governed story nodes and published narrative artifacts)

### Assumptions
- Draft docs may evolve quickly; filenames should be stable enough to avoid broken links.
- Anything that becomes public-facing or “canonical” must be promoted to the correct governed location.

### Constraints / invariants
- The canonical pipeline ordering is preserved: **ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode**.
- UI consumption is via API contracts (no direct graph access).
- Draft assets must not bypass provenance/sensitivity rules if they later become part of story nodes.

### Open questions
| Question | Owner | Target date |
|---|---|---|
| Should we enforce maximum asset file size via CI for `docs/research/drafts/assets/`? | TBD | TBD |
| Should we require a lightweight per-asset attribution stub (e.g., adjacent `.meta.md`)? | TBD | TBD |

### Future extensions
- Add a repo-wide lint rule to flag oversized binaries in `docs/` (if CI policy allows).
- Add a “promotion checklist” automation that opens an issue when a draft asset is referenced by a governed report.

## 🗺️ Diagrams

### Draft asset lifecycle (recommended)
~~~mermaid
flowchart LR
  A[Draft analysis / notes] --> B[Draft docs in docs/research/drafts]
  B --> C[Draft assets in docs/research/drafts/assets]
  C --> D{Promote to canonical?}
  D -- Yes --> E[data/processed + STAC/DCAT/PROV]
  D -- Yes --> F[docs/reports/.../story_nodes]
  D -- No --> G[Remain draft-only]
~~~

## 📦 Data & Metadata

### Inputs

| Input | Format | Where from | Validation |
|---|---|---|---|
| Figure/screenshot/diagram export | PNG/SVG/PDF | Local analysis tooling, map exports, screenshots | Ensure non-sensitive; include attribution if external |
| Small table export for illustration | CSV/PNG | Draft analysis output | If it becomes “data,” promote to `data/processed/` |

### Outputs

| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Embedded visuals in drafts | Images referenced from Markdown | `docs/research/drafts/**` | Markdown link integrity |

### Sensitivity & redaction
- Do not store sensitive locations, personal data, credentials, or restricted material in this folder.
- If a screenshot contains incidental PII (names, emails, tokens), redact before committing.

### Quality signals
- Prefer SVG for diagrams where possible (diff-friendly).
- Prefer descriptive filenames and meaningful alt text in Markdown.
- Record external source attribution next to the figure usage in the draft (or in a nearby section).

## 🌐 STAC, DCAT & PROV Alignment

Draft assets here are **not** STAC/DCAT/PROV-cataloged by default.
If an asset becomes a durable “evidence artifact” (used by governed Story Nodes / Focus Mode):
- promote the underlying data product to `data/processed/` and publish via `data/stac/` as appropriate
- ensure the narrative that references it links to dataset/document IDs and (when available) PROV activity/run IDs

## 🧱 Architecture

### How this work is served
- Draft assets are intended for draft documentation rendering (Markdown previews, documentation builds).
- Public UI/Focus Mode content should rely on governed Story Nodes and API-served evidence bundles, not draft assets.

## 🧠 Story Node & Focus Mode Integration

If a draft asset will be used in a Story Node:
- move/copy the finalized asset into the governed Story Node area (`docs/reports/<…>/story_nodes/…`) *or*
  promote it as a STAC asset and reference it by STAC item ID in the Story Node narrative
- ensure the Story Node remains provenance-linked and does not introduce unsourced claims

## 🧪 Validation & CI/CD

### Validation steps
- [ ] Links from drafts to assets resolve (relative paths)
- [ ] No sensitive data present (manual check)
- [ ] No oversized binaries committed unintentionally
- [ ] External sources are attributed in nearby draft text
- [ ] If promoted: STAC/DCAT/PROV + story-node validations applied in the target location

## ⚖ FAIR+CARE & Governance

### Review gates
- Draft assets: author + reviewer sanity check
- Promotion to governed outputs: historian/editor review (and sovereignty/ethics review if sensitive)

### CARE / sovereignty considerations
- If material may intersect culturally sensitive locations or knowledge, follow the repo’s sovereignty and ethics guidance and avoid committing restricted details to a public path.

### AI usage constraints
- Do not infer or reconstruct sensitive locations from partial cues in images or captions.
- Treat draft visuals as illustrative unless provenance is explicitly recorded.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v0.1.0 | 2025-12-20 | Initial README for draft assets folder | TBD |

---
Footer refs:
- Master guide: `docs/MASTER_GUIDE_v12.md`
- Templates: `docs/templates/`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`

