---
title: "Fixtures — Story Nodes (Invalid)"
path: ".github/actions/fixtures/story_nodes/invalid/README.md"
version: "v1.0.0"
last_updated: "2025-12-23"
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

doc_uuid: "urn:kfm:doc:github-actions:fixtures:story-nodes:invalid-readme:v1.0.0"
semantic_document_id: "kfm-github-fixtures-story-nodes-invalid-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:github-actions:fixtures:story-nodes:invalid-readme:v1.0.0"
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

# Fixtures — Story Nodes (Invalid)

## 📘 Overview

### Purpose

This directory contains intentionally **invalid** Story Node fixture files used to verify that Story Node validation gates correctly **fail** when inputs violate schema/template rules.

### Scope

| In Scope | Out of Scope |
|---|---|
| Fixture markdown files that should **fail** Story Node validation | Real Story Nodes meant for publication |
| Minimal examples of common failure modes (missing fields, schema violations, unsourced narrative, etc.) | Training data or production narrative content |
| CI assertions such as “validator must fail” / “expected errors present” | End-user documentation for Focus Mode |

### Audience

- Primary: CI / GitHub Actions maintainers; Story Node validator maintainers
- Secondary: Contributors adding Story Nodes who want to understand validation rules

### Definitions (link to glossary)

- Link: `docs/glossary.md`
- Terms used in this doc:
  - **Story Node**: governed narrative artifact (see `docs/templates/TEMPLATE__STORY_NODE_V3.md`)
  - **Fixture**: test-only sample file used to validate tooling behavior
  - **Expected-to-fail**: a fixture that must be rejected by validators

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Story Node template | `docs/templates/TEMPLATE__STORY_NODE_V3.md` | TBD | Canonical structure + required fields |
| Universal doc template | `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` | TBD | This README follows the universal governed doc structure |
| v13 CI gate expectations | `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md` | TBD | Defines Story Node validation as a minimum CI gate |
| Fixture root | `.github/actions/fixtures/story_nodes/` | TBD | Test-only content (this folder is a child) |

### Definition of done (for this document)

- [ ] Front-matter complete + valid
- [ ] Fixture purpose is clear: “expected-to-fail”
- [ ] Naming guidance + safety constraints documented (no PII, no sensitive locations)
- [ ] Validation steps listed and repeatable
- [ ] Governance + CARE/sovereignty considerations explicitly stated

## 🗂️ Directory Layout

### This document

- `path`: `.github/actions/fixtures/story_nodes/invalid/README.md` (must match front-matter)

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| CI workflows & actions | `.github/` | Workflows, composite actions, and test fixtures |
| Story Nodes (canonical home) | `docs/reports/story_nodes/` | Draft/published Story Nodes (not fixtures) |
| Story Node template | `docs/templates/TEMPLATE__STORY_NODE_V3.md` | Governed Story Node structure |
| Validator schemas | `schemas/` | JSON Schema / SHACL shapes, including Story Node schemas (if present) |

### Emoji directory tree

~~~text
📁 .github/
├── 📁 actions/
│   └── 📁 fixtures/
│       └── 📁 story_nodes/
│           ├── 📁 invalid/
│           │   └── 📄 README.md
│           └── 📁 valid/            # optional (not required for this folder)
~~~

## ✅ Fixture authoring rules

1. **Keep fixtures minimal.** Each file should demonstrate one primary failure mode.
2. **Make failures deterministic.** Avoid relying on ordering, network access, timestamps, or environment-specific behavior.
3. **No real sensitive content.** Use synthetic names/places unless you are deliberately testing redaction logic (**requires governance review**).
4. **Document the intended failure.** At the top of each fixture, add a short note:
   - what rule is violated
   - what the validator is expected to do (stop early vs. accumulate multiple errors)

### Suggested naming convention

Use a predictable prefix + short reason slug:

- `invalid__<reason>__<short>.md`

Examples (illustrative; create as needed):

- `invalid__missing_frontmatter__minimal.md`
- `invalid__bad_yaml__tabs_and_unclosed_list.md`
- `invalid__unsourced_narrative__no_citations.md`
- `invalid__missing_required_section__no_overview.md`

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode

These fixtures never surface in Focus Mode directly. They exist to protect Focus Mode by ensuring:

- Story Nodes that *are* published cannot bypass validation gates.
- “No unsourced narrative” is enforceable by tooling and CI policy.

### Provenance-linked narrative rule

- The Story Node validator should enforce evidence-linked claims consistent with Story Node governance expectations (see `docs/templates/TEMPLATE__STORY_NODE_V3.md`).

### Optional structured controls

Not applicable for fixtures (they are expected-to-fail). If a fixture tests these controls, it should still be rejected for the intended rule.

## 🧪 Validation & CI/CD

### Validation steps

- [ ] Markdown protocol checks (front-matter, required sections, lint rules)
- [ ] Story Node schema/template validation must **fail** for each file in `invalid/`
- [ ] If expected-error matching is implemented, assert the error category/reason is present
- [ ] Ensure CI remains deterministic: fail if fixtures unexpectedly pass

### Reproduction

~~~bash
# Example placeholders — replace with repo-specific commands

# 1) Run the Story Node validator against invalid fixtures (must fail)
# kfm validate story-nodes --path .github/actions/fixtures/story_nodes/invalid

# 2) (Optional) Run validator against valid fixtures (must pass)
# kfm validate story-nodes --path .github/actions/fixtures/story_nodes/valid
~~~

### Telemetry signals (if applicable)

| Signal | Source | Where recorded |
|---|---|---|
| N/A | N/A | N/A |

## ⚖ FAIR+CARE & Governance

### Review gates

- CI/action maintainers approve changes to fixtures that affect validator behavior.
- Any fixture that includes realistic sensitive content or tests redaction logic: **requires human review** (governance + ethics).

### CARE / sovereignty considerations

- Prefer synthetic or public-domain content.
- Do not encode culturally sensitive locations, burial sites, or restricted knowledge in fixtures.

### AI usage constraints

- Fixtures should not be used as training data.
- This README’s AI permissions/prohibitions should remain aligned with the Universal Doc template front-matter.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-23 | Initial README for invalid Story Node fixtures | TBD |

---

Footer refs:

- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
