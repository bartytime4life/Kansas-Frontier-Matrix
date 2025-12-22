---
title: "KFM Dev Docs — How-To Guides"
path: "tools/dev/docs/howto/README.md"
version: "v1.0.0"
last_updated: "2025-12-22"
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

doc_uuid: "urn:kfm:doc:tools:dev:docs:howto:readme:v1.0.0"
semantic_document_id: "kfm-tools-dev-docs-howto-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:tools:dev:docs:howto:readme:v1.0.0"
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

# KFM Dev Docs — How-To Guides

## 📘 Overview

### Purpose

This directory contains **step-by-step “how-to” guides** for working with KFM developer tooling and local workflows (running scripts, debugging a pipeline step, validating outputs, etc.). These are operational guides intended to be copy/paste friendly and reproducible.

### Scope

| In Scope | Out of Scope |
|---|---|
| Local dev and contributor workflows for KFM tooling and pipeline steps | System architecture, standards, and governance definitions (those live under `docs/`) |
| Step-by-step runbooks with prerequisites, commands, validation, troubleshooting | Narrative Story Nodes (use `docs/templates/TEMPLATE__STORY_NODE_V3.md`) |
| “How do I…?” procedures for repeatable tasks | API contract changes (use `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md`) |

### Audience

- Primary: contributors and maintainers running KFM locally (or in CI) to develop/debug.
- Secondary: reviewers who need a predictable checklist and validation trail.

### Definitions (link to glossary)

- Link: `docs/glossary.md`
- Terms used in this doc:
  - **How-to**: a procedure with explicit prerequisites + steps + verification.
  - **Runbook**: a how-to intended for repetitive or higher-risk actions (include rollback/cleanup).
  - **Fixture**: controlled test data (see `tools/dev/fixtures/README.md`).

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Dev docs index | `tools/dev/docs/README.md` | KFM maintainers | Entry point for dev documentation |
| Fixtures overview | `tools/dev/fixtures/README.md` | KFM maintainers | What fixtures exist + how to use them |
| Master Guide | `docs/MASTER_GUIDE_v12.md` | KFM core | Canonical pipeline + repo invariants |
| Universal doc template | `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` | KFM core | Default governed doc shape |
| Story Node template | `docs/templates/TEMPLATE__STORY_NODE_V3.md` | KFM core | Narrative artifacts (not for this folder) |
| API contract template | `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md` | KFM core | API changes (not for this folder) |

### Definition of done (for this document)

- [ ] Front-matter complete + valid
- [ ] Directory intent is clear (what belongs here vs elsewhere)
- [ ] Includes a file tree for navigation
- [ ] Includes guidance for writing new how-tos (structure + validation + safety)

## 🗂️ Directory Layout

### This document

- `path`: `tools/dev/docs/howto/README.md` (must match front-matter)

### File tree

~~~text
📁 tools/
└── 📁 dev/
    └── 📁 docs/
        └── 📁 howto/
            └── 📄 README.md
~~~

### What belongs in this folder

Add a new Markdown file here when you want to answer a repeatable question like:

- “How do I run <X> locally?”
- “How do I validate <Y> output?”
- “How do I reproduce <Z> CI failure?”
- “How do I generate / refresh <fixture> safely?”

### Recommended structure for each how-to

Use the **Universal governed doc template** shape, but keep it practical:

1. **Purpose** (what the procedure achieves)
2. **Prerequisites** (tools, env vars, data, access)
3. **Inputs / outputs** (what it reads/writes; expected artifact paths)
4. **Steps** (numbered, copy/paste friendly)
5. **Verification** (how to confirm success)
6. **Troubleshooting** (common failure modes)
7. **Cleanup / rollback** (when applicable)
8. **References** (schemas, issues, commits, dataset IDs, run IDs)

> Tip: Prefer `~~~bash` code fences (not backticks) to avoid nesting conflicts and to match repo conventions.

## 🧭 Context

### Where “how-to” docs fit in KFM’s overall flow

How-to docs are **supporting developer artifacts**. They should not redefine architecture; they should help people execute or verify work that is already governed elsewhere.

~~~mermaid
flowchart LR
  Dev[Developer / CI] --> Tools[tools/dev/* scripts & helpers]
  Tools --> Pipeline[ETL / Catalog / Graph / API / UI tasks]
  Pipeline --> Evidence[Outputs: data/** + schemas/** references]
  Evidence --> Docs[Governed docs under docs/]
~~~

### Guardrails (keep these docs safe)

- **No secrets**: never include real API keys/tokens; use `.env.example` style placeholders.
- **No PII**: avoid including raw personal data in examples; prefer redacted fixtures.
- **No “UI reads graph directly” instructions**: if a workflow touches UI data access, route through the API boundary.

## 🧠 Story Node & Focus Mode Integration

Most how-tos here are *not* Story Nodes. However, if a how-to generates, validates, or publishes Story Node artifacts:

- Ensure outputs link back to provenance-bearing artifacts (STAC/DCAT/PROV IDs and/or run IDs where applicable).
- Use the Story Node template for the narrative artifact itself:
  - `docs/templates/TEMPLATE__STORY_NODE_V3.md`

## 🧪 Validation & CI/CD

When adding or updating how-to docs:

- [ ] Front-matter is valid and `path` matches location
- [ ] Internal links are correct (relative paths)
- [ ] Steps are deterministic and do not rely on unstated local state
- [ ] Any referenced schemas / fixtures exist and are named exactly

## ⚖ FAIR+CARE & Governance

### Governance review triggers

Escalate (or mark **requires human review**) when a how-to introduces:

- New external data sources
- New sensitive layers or restricted-location handling
- New AI narrative behaviors
- New public-facing endpoints or changes in access controls

### CARE / sovereignty considerations

If your how-to touches culturally sensitive content, restricted site locations, or community data rules:

- document the safe handling expectation (redaction/generalization),
- reference the sovereignty policy: `docs/governance/SOVEREIGNTY.md`.

### AI usage constraints

- This doc allows summarization/structuring, but prohibits policy generation and sensitive-location inference (see front-matter).

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-22 | Initial how-to directory README | TBD |

---

Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
