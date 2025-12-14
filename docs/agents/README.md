---
title: "🤖 Agents"
path: "docs/agents/README.md"

version: "v11.2.6"
last_updated: "2025-12-14"
release_stage: "Draft / Governed"
lifecycle: "Active"
review_cycle: "Quarterly · FAIR+CARE Council & Focus Mode Board"
content_stability: "evolving"

status: "Active"
doc_kind: "Guide"
header_profile: "standard"
footer_profile: "standard"

license: "CC-BY 4.0"
markdown_protocol_version: "KFM-MDP v11.2.6"

scope:
  domain: "documentation"
  applies_to:
    - "docs/agents/**"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"
sensitivity: "General (non-sensitive; auto-mask rules apply)"
sensitivity_level: "None"
public_exposure_risk: "Low"
classification: "Public"
jurisdiction: "Kansas / United States"
indigenous_rights_flag: true

data_steward: "KFM FAIR+CARE Council"
ttl_policy: "24 months"
sunset_policy: "Reviewed at next minor release"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<none>"
provenance_chain: []

# Stable identifiers (do not change once published)
doc_uuid: "urn:kfm:doc:agents:readme:v11.2.6"
semantic_document_id: "kfm-agents-readme-v11.2.6"
event_source_id: "ledger:kfm:doc:agents:readme:v11.2.6"

governance_ref: "governance/ROOT-GOVERNANCE.md"
ethics_ref: "faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "sovereignty/INDIGENOUS-DATA-PROTECTION.md"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed (documentation-only; no sensitive locations)"
ai_transform_permissions:
  - "summarize"
  - "translate"
  - "format_to_kfm_mdp"
  - "extract_task_checklist"
ai_transform_prohibited:
  - "invent_sources_or_citations"
  - "generate_sensitive_locations"
  - "include_credentials_or_secrets"
---

<div align="center">

# 🤖 Agents

**Purpose:** Define what “agents” are in KFM, where their documentation lives, and how to author governed agent specs that are safe, reproducible, and pipeline-aligned.

</div>

---

## Overview

This folder is the documentation home for **KFM agent specifications**.

In KFM, an *agent* is a constrained, role-oriented assistant profile used to:

- Perform a specific job in the KFM pipeline (ETL → catalogs → graph → API → frontend → Story Nodes → Focus Mode).
- Produce deterministic, reviewable outputs (configs, manifests, metadata, runbooks, checklists) rather than “freeform” changes.
- Enforce governance and sovereignty boundaries by default.

Use this directory to keep agent behaviors explicit, reviewable, and testable.

**Related standards and policies:**

- Markdown rules and front matter: [docs/standards/kfm_markdown_protocol_v11.2.6.md](../standards/kfm_markdown_protocol_v11.2.6.md)
- CI entrypoint for Markdown checks: [.github/workflows/kfm-ci.yml](../../.github/workflows/kfm-ci.yml)

## Directory Layout

~~~text
📁 docs/
└── 📁 agents/
    └── 📄 README.md — Entry point for agent documentation (this file)
~~~

## Context

Agent docs exist to reduce ambiguity and prevent “prompt drift.” Each agent spec should make it clear:

- **Role & scope:** Which KFM pipeline stage(s) the agent may act within.
- **Inputs/outputs:** What files, schemas, APIs, or graph structures the agent can touch.
- **Constraints:** Determinism requirements, allowed tooling, and non-goals.
- **Evidence:** What constitutes sufficient provenance and verification.

If you add new agent documents under `docs/agents/`, keep them narrow in scope and write them as contracts a reviewer can validate.

## Architecture

A KFM agent spec should be written so it can be used in three ways:

- **Human-run:** a developer follows the spec as a checklist.
- **Tool-assisted:** automation uses the spec to generate consistent PRs and run logs.
- **Audit-ready:** reviewers can trace what changed, why, and what standards were applied.

Minimum recommended content for an agent doc (use *only* approved headings per KFM-MDP):

- Purpose and non-goals
- Pipeline placement (ETL / Catalog / Graph / API / Frontend / Story)
- Inputs/outputs (paths, schemas, API contracts)
- Determinism rules (config-driven, replayable, version-aware)
- Validation steps (lint, schema checks, unit/integration tests)
- Governance & sovereignty constraints (what must be masked or refused)

## Story Node & Focus Mode Integration

If an agent produces Story Nodes or Focus Mode outputs, it must:

- Keep narrative structured and evidence-led.
- Separate **facts** (source-backed) from **interpretation** (reasoned) and **speculation** (explicitly hypothetical).
- Never fabricate evidence links, citations, entities, or relationships.

## Validation & CI/CD

All agent docs must pass the repository’s documentation checks.

At minimum, ensure:

- Front matter is present and schema-valid.
- H2 headings match the approved registry.
- No raw URLs appear in committed Markdown.
- Links resolve within the repo.

See the CI workflow for the authoritative enforcement set: [.github/workflows/kfm-ci.yml](../../.github/workflows/kfm-ci.yml).

## ⚖ FAIR+CARE & Governance

Agent documentation must not be used to bypass governance.

Hard constraints:

- **No secrets:** never place credentials, tokens, private keys, or internal endpoints in agent docs.
- **Sovereignty-first:** if a dataset, place, or story involves Indigenous communities or culturally sensitive knowledge, apply KFM’s masking/generalization rules by default and follow the sovereignty policy.
- **Least privilege:** specify the smallest set of actions and data access needed to do the job.

Governance references (must remain valid):

- Governance: [governance/ROOT-GOVERNANCE.md](../../governance/ROOT-GOVERNANCE.md)
- Ethics / FAIR+CARE: [faircare/FAIRCARE-GUIDE.md](../../faircare/FAIRCARE-GUIDE.md)
- Indigenous data protection: [sovereignty/INDIGENOUS-DATA-PROTECTION.md](../../sovereignty/INDIGENOUS-DATA-PROTECTION.md)

## Version History

- v11.2.6 (2025-12-14): Initial creation of `docs/agents/README.md`.

---

**Governance:** [governance/ROOT-GOVERNANCE.md](../../governance/ROOT-GOVERNANCE.md) · **Ethics:** [faircare/FAIRCARE-GUIDE.md](../../faircare/FAIRCARE-GUIDE.md) · **Sovereignty:** [sovereignty/INDIGENOUS-DATA-PROTECTION.md](../../sovereignty/INDIGENOUS-DATA-PROTECTION.md)