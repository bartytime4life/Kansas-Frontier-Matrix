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
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"

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
doc_uuid: "urn:kfm:doc:agents:index:v11.2.6"
semantic_document_id: "kfm-doc-agents-index-v11.2.6"
event_source_id: "ledger:kfm:doc:agents:index:v11.2.6"

governance_ref: "governance/ROOT-GOVERNANCE.md"
ethics_ref: "faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "sovereignty/INDIGENOUS-DATA-PROTECTION.md"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed (documentation-only; no sensitive locations)"
ai_transform_permissions:
  - "summarize"
  - "extract_task_checklist"
  - "format_to_kfm_mdp"
  - "link_normalization"
ai_transform_prohibited:
  - "invent_sources_or_citations"
  - "generate_sensitive_locations"
  - "include_credentials_or_secrets"
---

# 🤖 Agents

**Purpose**  
Define what “agents” are in KFM, where agent documentation lives, and what minimum governance + validation requirements apply to agent specifications.

## 📘 Overview

In KFM, an **agent** is a constrained, role-oriented specification used to produce **repeatable, reviewable outputs** across the pipeline:

ETL → catalogs (STAC/DCAT/PROV) → graph (Neo4j) → API → frontend → Story Nodes → Focus Mode.

Agents exist to:

- Reduce ambiguity (clear scope, clear non-goals).
- Prevent prompt drift (documented constraints).
- Improve reproducibility (deterministic steps, explicit inputs/outputs).
- Improve governance (sovereignty + safety boundaries are explicit).

## 🗂️ Directory Layout

~~~text
📁 docs/
└── 📁 agents/                              — Agent documentation (roles, constraints, patterns)
    └── 📄 README.md                        — Index and authoring rules for agent specs (this file)
~~~

## 🧭 Context

Agent docs should read like **contracts** that a reviewer can validate.

A compliant agent specification makes it obvious:

- which pipeline stage(s) it can act in,
- what artifacts it may create or modify,
- which checks must pass,
- what it must refuse (secrets, PII, restricted locations, sovereignty constraints).

## 🧱 Architecture

An agent spec is expected to be usable in three modes:

- **Human-run**: a developer follows the steps as a checklist.
- **Tool-assisted**: automation generates consistent PRs, logs, and metadata.
- **Audit-ready**: reviewers can trace what changed, why, and how it was validated.

Minimum recommended sections for agent documents (choose only from approved H2 headings):

- Overview of scope and non-goals
- Interfaces: inputs/outputs (paths, schemas, API contracts)
- Determinism rules (config-driven, replayable)
- Validation (lint, schema checks, tests)
- Governance boundaries (masking rules, refusal behavior)

## 🧠 Story Node & Focus Mode Integration

If an agent produces Story Nodes or Focus Mode outputs, it MUST:

- Keep narrative structured and evidence-led.
- Separate **facts** (source-backed) from **interpretation** (reasoned) and **speculation** (explicitly hypothetical).
- Never fabricate evidence links, entities, or relationships.

## 🧪 Validation & CI/CD

Agent docs are expected to pass repository documentation checks.

Minimum expectations:

- Front-matter present and schema-valid.
- Exactly one H1.
- Approved H2 headings only.
- Directory trees fenced as `~~~text`.
- No secrets / no PII.
- Footer includes governance links.

Reference: `.github/workflows/kfm-ci.yml`.

## ⚖ FAIR+CARE & Governance

Hard constraints for agent docs:

- **No secrets**: never include credentials, tokens, private keys, or internal endpoints.
- **Sovereignty-first**: apply masking/generalization rules by default for sensitive cultural or archaeological information.
- **Least privilege**: agent scope must be the smallest set of actions needed.

## 🕰️ Version History

- v11.2.6 (2025-12-14): Created `docs/agents/README.md` and aligned headings + footer to KFM-MDP v11.2.6.

---

[📂 Standards Index](../standards/README.md) · [🏛️ Governance Charter](../../governance/ROOT-GOVERNANCE.md) · [🤝 FAIR+CARE Guide](../../faircare/FAIRCARE-GUIDE.md) · [🪶 Indigenous Data Protection](../../sovereignty/INDIGENOUS-DATA-PROTECTION.md)