---
title: "README — Markdown Protocol Fixtures"
path: ".github/actions/fixtures/markdown_protocol/README.md"
version: "v1.0.0"
last_updated: "2025-12-22"
status: "draft"
doc_kind: "CI Guide"
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

doc_uuid: "urn:kfm:doc:github:actions:fixtures:markdown-protocol-readme:v1.0.0"
semantic_document_id: "kfm-github-actions-fixtures-markdown-protocol-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:github:actions:fixtures:markdown-protocol-readme:v1.0.0"
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

# Markdown Protocol Fixtures

## 📘 Overview

### Purpose
This directory contains Markdown fixtures used by CI checks for the KFM markdown protocol. Fixtures are intentionally small documents that represent either:

- Passing examples of governed docs, or
- Failing examples that exercise specific validation errors.

### Scope

| In Scope | Out of Scope |
|---|---|
| Fixture Markdown files used by tests and CI | The validator implementation itself |
| Good and bad examples of front matter, section structure, and repo-path invariants | GitHub workflow authoring and permissions |
| Minimal sample docs for Universal, Story Node, and API Contract templates | Domain datasets and catalog generation |

### Audience
- Primary: Maintainers of `.github/` actions and CI checks.
- Secondary: Contributors adding or updating governed Markdown documents.

### Definitions
- Fixture: A small, deterministic test document checked in to the repo.
- Markdown protocol validation: The CI gate that ensures Markdown docs conform to the governed templates and repository rules.
- Valid fixture: Expected to pass validation.
- Invalid fixture: Expected to fail validation and produce a specific error code or message.

### Key artifacts

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master Guide | `docs/MASTER_GUIDE_v12.md` | KFM maintainers | Canonical pipeline ordering and doc governance |
| Universal doc template | `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` | Docs governance | Default template for governed docs |
| Story Node template | `docs/templates/TEMPLATE__STORY_NODE_V3.md` | Story governance | Narrative nodes and Focus Mode rules |
| API contract template | `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md` | API governance | REST/GraphQL contract extension format |
| Markdown work protocol | `docs/standards/KFM_MARKDOWN_WORK_PROTOCOL.md` | Docs governance | Not confirmed in repo; referenced by the v13 blueprint |

### Definition of done
- [ ] Fixtures are deterministic and self-contained.
- [ ] Each fixture clearly states whether it is expected to pass or fail.
- [ ] Each invalid fixture targets one primary rule violation.
- [ ] No fixture includes secrets, private data, or sensitive locations.
- [ ] CI can run fixture validation without external network access.

## 🗂️ Directory Layout

### This document
- `path`: `.github/actions/fixtures/markdown_protocol/README.md`

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| GitHub Actions | `.github/` | CI workflows and reusable actions |
| Fixture files | `.github/actions/fixtures/markdown_protocol/` | Test inputs for markdown protocol validation |
| Documentation | `docs/` | Canonical governed docs |
| Templates | `docs/templates/` | Governed Markdown templates |
| Standards | `docs/standards/` | Repo and Markdown standards |

### Suggested fixture layout
If you are creating this directory from scratch, use a structure like:

~~~text
📁 .github/
└── 📁 actions/
    └── 📁 fixtures/
        └── 📁 markdown_protocol/
            ├── 📄 README.md
            ├── 📁 valid/
            │   ├── 📄 universal__minimal.md
            │   ├── 📄 story_node__minimal.md
            │   └── 📄 api_contract__minimal.md
            └── 📁 invalid/
                ├── 📄 missing_front_matter.md
                ├── 📄 path_mismatch.md
                ├── 📄 missing_required_section.md
                └── 📄 forbidden_content.md
~~~

If the validator expects a different on-disk shape, treat this as a documentation hint and align to the validator’s needs.

## 📦 Data & Metadata

Fixtures are documentation artifacts rather than datasets. The validation action may still treat them as inputs and produce structured outputs.

### Inputs

| Input | Format | Where from | Validation |
|---|---|---|---|
| Fixture Markdown files | `.md` | This folder | Markdown protocol checks |

### Outputs

| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Validation results | Logs / JSON | CI job output | Not confirmed in repo |

### Sensitivity and redaction
- Fixtures should never contain PII or culturally sensitive site locations.
- Use placeholders like `TBD`, `Example County`, or generalized coordinates.

### Quality signals
- Fixtures should be minimal but representative.
- Prefer one rule violation per invalid fixture to keep failure signals clear.

## 🌐 STAC, DCAT & PROV Alignment

Not applicable for this fixture README itself. If a fixture is meant to validate cross-links to STAC/DCAT/PROV, ensure the fixture:

- Uses placeholder identifiers, or
- References a stable, committed test artifact under `data/` that is safe for CI.

## 🧱 Architecture

### Components

| Component | Responsibility | Interface |
|---|---|---|
| Fixture set | Test inputs | File paths in repo |
| Markdown protocol validator | Rule evaluation | CLI or action step output |
| CI workflow | Runs the validator | GitHub Actions job |

### Interfaces and contracts
- The validator should treat `valid/` fixtures as expected-pass and `invalid/` fixtures as expected-fail.
- If the validator uses a manifest file, keep it adjacent to this README and document its schema here.

### Extension points checklist
- [ ] Add new fixture category folder if a new rule group is introduced.
- [ ] Add one valid and one invalid fixture for new template rules.
- [ ] Keep fixtures versioned in lock-step with template changes.

## 🧠 Story Node & Focus Mode Integration

Some fixtures may be Story Nodes. When adding Story Node fixtures:

- Keep evidence citations as placeholders unless you also include the referenced stub dataset or doc in a test-safe location.
- Ensure narrative text is clearly marked as test content, not historical claims.

## 🧪 Validation & CI/CD

### Validation steps
- [ ] Markdown protocol checks run on this fixture set.
- [ ] Failures map to a single violated rule where possible.

### Reproduction
The exact command depends on the validator implementation.

~~~bash
# Example placeholders — replace with repo-specific commands
# 1) run the markdown protocol validator on the fixture directory
# 2) assert that ./valid passes and ./invalid fails with expected messages
~~~

### Telemetry signals
If the CI publishes structured validation output, document:

- Where it is stored
- How it is consumed
- Schema versioning rules

## ⚖ FAIR+CARE & Governance

- Fixtures must respect the repo’s governance and ethics references in front matter.
- Use `sensitivity: public` unless the fixture is explicitly testing sensitivity gating.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-22 | Initial README for markdown protocol fixtures | TBD |

---

Footer refs:
- Master Guide: `docs/MASTER_GUIDE_v12.md`
- Templates: `docs/templates/`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
