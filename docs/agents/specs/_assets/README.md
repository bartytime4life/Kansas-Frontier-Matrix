---
title: "KFM Agents Specs — _assets/ README"
path: "docs/agents/specs/_assets/README.md"
version: "v1.0.0"
last_updated: "2025-12-17"
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

doc_uuid: "urn:kfm:doc:agents:specs:assets-readme:v1.0.0"
semantic_document_id: "kfm-agents-specs-assets-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:agents:specs:assets-readme:v1.0.0"
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

# KFM Agents Specs — _assets/ README

## 📘 Overview

### Purpose
This directory (`docs/agents/specs/_assets/`) holds **supporting, non-Markdown artifacts** referenced by agent specification documents under `docs/agents/specs/` (e.g., diagrams, UI screenshots, and small example payloads).

The goal is to keep specs readable while ensuring assets remain **reviewable, provenance-aware, and appropriately redacted/generalized**.

### Scope
| In Scope | Out of Scope |
|---|---|
| Diagrams for agent specs (prefer text-first diagrams; use images when needed) | Raw/derived datasets (use `data/` + STAC/DCAT/PROV instead) |
| UI screenshots used to explain workflows | Secrets, tokens, credentials, private keys |
| Small sample payloads (JSON/YAML) used in specs | Unredacted sensitive location data or culturally restricted materials |
| Redacted example outputs used only for documentation | Large binaries (model weights, full exports) |

### Audience
- Primary: Contributors authoring or updating agent specs in `docs/agents/specs/`
- Secondary: Maintainers and reviewers (governance, security, CARE/sovereignty review)

### Definitions (link to glossary)
- Link: `docs/glossary.md`
- Terms used in this doc: **agent spec**, **asset**, **provenance**, **redaction/generalization**, **sensitivity/classification**

### Key artifacts (what this doc points to)
| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Agents README | `docs/agents/README.md` | Maintainers | Entry point for agent documentation |
| Agent specs README | `docs/agents/specs/README.md` | Maintainers | Conventions for writing specs |
| This README | `docs/agents/specs/_assets/README.md` | Maintainers | Rules + patterns for spec assets |
| Governance root | `docs/governance/ROOT_GOVERNANCE.md` | Governance | Review triggers + authority |
| Ethics | `docs/governance/ETHICS.md` | Governance | Narrative + model constraints |
| Sovereignty / CARE | `docs/governance/SOVEREIGNTY.md` | Governance | Restricted locations + community protections |

### Definition of done (for this document)
- [ ] Front-matter complete + valid
- [ ] Clear guidance on what belongs in `_assets/` (and what does not)
- [ ] Naming + provenance expectations stated
- [ ] Validation steps listed and repeatable
- [ ] Governance + CARE/sovereignty considerations explicitly stated

## 🗂️ Directory Layout

### This document
- `path`: `docs/agents/specs/_assets/README.md` (must match front-matter)

### Related repository paths
| Area | Path | What lives here |
|---|---|---|
| Governed docs | `docs/` | System documentation, templates, runbooks |
| Agent docs | `docs/agents/` | Agent specs, runbooks, eval plans, prompt assets |
| Agent specs | `docs/agents/specs/` | Role/spec contracts (capabilities, I/O, constraints) |
| Spec assets | `docs/agents/specs/_assets/` | Images/diagrams/examples referenced by specs |
| Derived data | `data/processed/` | Reproducible data outputs + artifacts (not docs assets) |
| Catalogs | `data/stac/`, `docs/data/` | STAC/DCAT/PROV artifacts |
| Run logs / experiments | `mcp/runs/`, `mcp/experiments/` | Repeatable experiment logs, run IDs |

### Expected file tree for this sub-area
~~~text
docs/
└── 📁 agents/
    └── 📁 specs/
        └── 📁 _assets/
            ├── 📄 README.md
            ├── 🖼️ <agent-id>--<artifact>.svg          # preferred for diagrams (diff-friendly)
            ├── 🖼️ <agent-id>--<screenshot>.webp       # preferred for screenshots (compressed)
            ├── 🖼️ <agent-id>--<screenshot>.png        # allowed when lossless is required
            └── 📄 <agent-id>--<example>.json          # small payload examples (optional)
~~~

## 🧭 Context

### Background
Agent specs often require visuals or “worked examples” to communicate:
- scope boundaries (what the agent can/can’t do),
- dataflow and provenance expectations,
- review/redaction steps,
- UI behaviors and user-facing surfaces.

Keeping these artifacts in `_assets/` avoids bloating specs with large inline content while still keeping everything auditable.

### Assumptions
- Specs are rendered in a markdown viewer (GitHub and/or doc site build).
- Relative links from `docs/agents/specs/*.md` into `docs/agents/specs/_assets/*` are supported.

### Constraints / invariants
- **Documentation assets are not data products.** Use `data/` + STAC/DCAT/PROV for datasets and derived artifacts that belong to the pipeline.
- **No secrets or credentials** (ever) in any asset file.
- **No unredacted sensitive locations** (or anything that enables inference of restricted locations).
- The system-level invariant ordering is preserved: ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode (this folder is documentation-only and must not be used to bypass pipeline contracts).

### Open questions
- Should we require per-asset sidecar metadata files (e.g., `*.meta.yml`) for provenance/licensing, or is the registry table (below) sufficient?
- Should we add/confirm repo-wide size limits for binary docs assets (to avoid repo bloat)?

### Future extensions
- Optional: add a lightweight convention for keeping diagram *sources* (e.g., Mermaid in-spec, or vector sources) alongside rendered exports.
- Optional: add CI checks to detect large binaries, broken links, and missing provenance entries.

## 🗺️ Diagrams

### System / dataflow diagram (docs-only asset lifecycle)
~~~mermaid
flowchart LR
  Spec["Agent spec (.md)"] -->|references| Asset["_assets/ (docs-only)"]
  Author["Contributor"] --> Spec
  Author --> Asset
  Spec --> Review["Review: governance + redaction + licensing"]
  Asset --> Review
  Review --> Merge["Merge"]
  Merge --> Render["GitHub / Docs render"]
~~~

### Optional: sequence diagram (review loop)
~~~mermaid
sequenceDiagram
  participant Author as Contributor
  participant Repo as Repo (docs/)
  participant Reviewer as Reviewer

  Author->>Repo: Add asset file in specs/_assets/
  Author->>Repo: Reference asset from spec (relative link)
  Author->>Repo: Update asset registry row (below)
  Reviewer->>Reviewer: Check redaction/generalization
  Reviewer->>Reviewer: Check provenance + licensing notes
  Reviewer->>Repo: Approve/merge (or request changes)
~~~

## 📦 Data & Metadata

### What belongs here
- **Diagrams** used in specs (prefer `.svg` for diff-friendliness).
- **Screenshots** demonstrating UI/flows (prefer compressed formats when possible).
- **Small** example payloads used in specs (`.json`, `.yml`) that are **sanitized**.

### What does NOT belong here
- Datasets, analysis outputs, or anything that should be cataloged (use `data/` + STAC/DCAT/PROV).
- Model weights, large exports, or logs (use appropriate `data/` and/or `mcp/` paths).
- Any file containing secrets or sensitive location details.

### Naming conventions
- **MUST:** lowercase, hyphen/`--` separated, no spaces.
- **SHOULD:** include an agent/spec identifier prefix to prevent collisions.
- **SHOULD:** encode meaning in the filename (what it is + where it’s used).

Recommended pattern:
- `agent-<agent-id>--<short-artifact-name>--<yyyymmdd>.<ext>` (date optional)

Examples:
- `agent-focus-transformer--dataflow--20251217.svg`
- `agent-coordinator--ui-audit-panel.webp`
- `agent-extractor--example-output.json`

### Provenance + licensing (documentation assets)
- If an asset is **created from a dataset**, record the **dataset/document identifier** in:
  - the spec section that references it, and/or
  - the asset registry table below.
- If an asset is **third‑party**, record:
  - source (publisher/author),
  - license/usage terms,
  - any required attribution.

### Asset registry
Add a row when a new asset is introduced or materially updated.

| Asset file | Used by spec(s) | Source / provenance ref | Sensitivity | Notes |
|---|---|---|---|---|
| (add) | `docs/agents/specs/<spec>.md` | (dataset/document ID or “original”) | public / restricted | attribution, redaction notes |

## 🌐 STAC, DCAT & PROV Alignment

This folder is **not** a STAC asset store.

If an “asset” is actually a pipeline artifact (e.g., generated plot, derived raster, evidence bundle) that should be preserved and queryable, it belongs in the governed data flow:
- store it under an appropriate `data/` location,
- register it as STAC/DCAT,
- link lineage via PROV,
- then reference the catalog IDs from docs/specs.

For documentation-only images that summarize or explain a pipeline artifact, keep them here **only if** they are suitably redacted/generalized and do not substitute for the real cataloged artifact.

## 🧱 Architecture

### How assets are consumed
- Specs reference assets using **relative links**, for example:
  - `![Dataflow diagram](./_assets/agent-focus-transformer--dataflow.svg)`
- Reviewers should be able to evaluate:
  - whether the asset content is appropriate,
  - whether it leaks sensitive info,
  - whether it has provenance/attribution.

### Storage considerations
- Prefer formats that are reviewable and diff-friendly (vector where possible).
- Keep binaries as small as practical without sacrificing clarity.

## 🧠 Story Node & Focus Mode Integration

Agent spec assets are primarily for **documentation**.

If an asset is intended for user-facing Story Nodes / Focus Mode:
- place it with the story node (or in the appropriate user-facing docs area), and
- ensure it has provenance linkage and sensitivity handling consistent with Focus Mode’s provenance-only rule.

Do not use this folder to “smuggle” user-facing evidence artifacts outside the governed pipeline.

## 🧪 Validation & CI/CD

### Validation steps
- [ ] File naming follows conventions (lowercase, no spaces)
- [ ] Spec links resolve (no broken relative links)
- [ ] No secrets/credentials embedded (including in screenshots)
- [ ] Sensitive locations are not present or are properly generalized/redacted
- [ ] Provenance/attribution recorded (spec text and/or registry table)

### Reproduction
~~~bash
# Example placeholders — replace with repo-specific commands
# - build docs site / render markdown
# - run markdown lint / link check
# - run any repo policy scanners for secrets / large files
~~~

### AI usage constraints
- Ensure this document’s AI permissions/prohibitions match intended use.
- This area must not be used to justify policy changes (“generate_policy”).
- This area must not be used to infer restricted site locations (“infer_sensitive_locations”).

## ⚖ FAIR+CARE & Governance

### Review gates
Escalate review if an asset includes (or could imply) any:
- culturally sensitive information,
- restricted ecological/heritage locations,
- partner-contributed images with special access terms.

### CARE / sovereignty considerations
- Prefer generalization over specificity when locations or cultural knowledge are sensitive.
- Avoid publishing anything that could enable looting, harassment, or misuse.

## 🕰️ Version History
| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-17 | Initial README for `docs/agents/specs/_assets/` | TBD |

---
Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
