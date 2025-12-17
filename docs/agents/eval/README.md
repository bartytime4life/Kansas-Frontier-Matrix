---
title: "KFM Agent Evaluation — README"
path: "docs/agents/eval/README.md"
version: "v1.0.0"
last_updated: "2025-12-17"
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

doc_uuid: "urn:kfm:doc:agents:eval:readme:v1.0.0"
semantic_document_id: "kfm-doc-agents-eval-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:agents:eval:readme:v1.0.0"
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

# KFM Agent Evaluation — README

## 📘 Overview

### Purpose
- Define how to document and maintain **evaluation artifacts** for KFM agents.
- Ensure agent behavior stays aligned with specs, governance, and KFM’s evidence/provenance requirements.

### Scope
| In Scope | Out of Scope |
|---|---|
| Evaluation plans, test cases, acceptance criteria, and governance checks for agents | Production benchmarking infrastructure (unless documented elsewhere), model training, secrets |

### Audience
- Primary: Contributors defining how agents are tested and validated
- Secondary: Reviewers and maintainers performing regressions

### Definitions (link to glossary)
- Link: `docs/glossary.md`
- Terms used in this doc: `eval`, `acceptance criteria`, `regression`, `golden case`, `governance check`

### Key artifacts (what this doc points to)
| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Agent specs | `docs/agents/specs/` | TBD | Source-of-truth behavioral contracts |
| Eval directory | `docs/agents/eval/` | TBD | Home for eval docs |
| Agents index | `docs/agents/README.md` | TBD | Cross-links |

### Definition of done (for this document)
- [ ] Front-matter complete + valid
- [ ] Eval artifact layout documented
- [ ] Governance checks included as eval dimensions (where applicable)

## 🗂️ Directory Layout

### This document
- `path`: `docs/agents/eval/README.md` (must match front-matter)

### Related repository paths
| Area | Path | What lives here |
|---|---|---|
| Specs | `docs/agents/specs/` | Contracts to test against |
| Eval | `docs/agents/eval/` | Evaluation plans + cases |
| Tests (optional) | `tests/` | Automated harness, if later implemented |
| MCP (optional) | `mcp/` | Run logs / experiments, if later used |

### Expected file tree for this sub-area
~~~text
📁 docs/
└── 📁 agents/
    └── 📁 eval/
        ├── 📄 README.md
        └── 📁 <agent_id>/             (recommended)
            ├── 📄 README.md           (recommended)
            └── 📄 cases.md            (optional)
~~~

## 🧭 Context

### Background
- Agent behavior must be evaluated in three dimensions:
  1) Contract compliance (matches the spec)
  2) Governance compliance (redaction, sensitive inference prohibitions)
  3) Quality/reproducibility (deterministic, auditable outputs)

### Assumptions
- Each agent has a spec; eval docs reference the spec version they validate.
- Evaluations can start as documentation-only and later be automated.

### Constraints / invariants
- ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode is preserved.
- Frontend consumes contracts via APIs (no direct graph dependency).

### Open questions
| Question | Owner | Target date |
|---|---|---|
| Where will automated evaluation code live (if added): `tests/` or `tools/`? | TBD | TBD |
| Do we need standard scoring rubrics for narrative/evidence outputs? | TBD | TBD |

### Future extensions
- Add a standard eval rubric template.
- Add automated CI gating for “must pass” governance checks.

## 🗺️ Diagrams

### System / dataflow diagram
~~~mermaid
flowchart LR
  Spec[Agent spec] --> EvalPlan[Eval plan + cases]
  EvalPlan --> Run[Run evaluation (manual or automated)]
  Run --> Results[Findings + remediation]
  Results --> Update[Update spec/runbook/eval]
~~~

### Optional: sequence diagram
~~~mermaid
sequenceDiagram
  participant Contributor
  participant Spec
  participant Eval
  participant Reviewer

  Contributor->>Spec: Update agent contract
  Contributor->>Eval: Update eval cases to match contract
  Reviewer->>Eval: Validate governance checks included
  Reviewer-->>Contributor: Approve or request changes
~~~

## 📦 Data & Metadata

### Inputs
| Input | Format | Where from | Validation |
|---|---|---|---|
| Spec version under test | Markdown | `docs/agents/specs/<agent_id>.md` | Must be explicit |
| Test prompts/cases | Markdown | `docs/agents/eval/<agent_id>/...` | Must be deterministic and bounded |
| Optional fixture references | IDs/paths | STAC/DCAT/graph refs | Must be stable identifiers |

### Outputs
| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Eval documentation | Markdown | `docs/agents/eval/**` | KFM-MDP + Universal template |
| Findings | Text/links | TBD | Must avoid sensitive data; include provenance where relevant |

### Sensitivity & redaction
- Eval cases must not embed sensitive locations, private endpoints, or secrets.
- If sensitive fixtures are required, document a safe substitute or a redacted proxy dataset.

### Quality signals
- Coverage: cases cover core capabilities and known failure modes.
- Governance: cases include explicit “should refuse” and “should redact/generalize” checks.
- Reproducibility: cases can be repeated without ambiguity.

## 🌐 STAC, DCAT & PROV Alignment

### STAC
- If eval uses dataset fixtures, prefer referencing STAC IDs (Collection/Item) rather than ad-hoc filenames.

### DCAT
- If eval includes metadata publication behavior, specify expected DCAT fields and constraints at a high level.

### PROV-O
- If eval checks provenance behavior, specify what PROV links must exist (inputs/outputs, activities, responsible agents).

### Versioning
- Eval docs should note which spec version they validate and be updated when the spec changes.

## 🧠 Story Node & Focus Mode Integration

### How this doc influences Story Nodes
- Any agent that drafts Story Nodes should have eval cases that check:
  - claims are evidence-linked
  - hypotheses are labeled
  - prohibited inferences are not made

### How it appears in Focus Mode
- Eval outcomes may inform governance flags, but Focus Mode UX is governed elsewhere.

## 🧪 Validation & CI/CD

### How to validate this doc
- Confirm `path` front-matter matches the file path.
- Confirm links to the agent spec resolve.
- Confirm eval cases are deterministic and bounded in scope.

### Links to checks/scripts
- TBD

## ⚖ FAIR+CARE & Governance

### FAIR considerations
- Keep eval artifacts discoverable and linked to the relevant spec version.
- Prefer stable dataset identifiers for fixtures.

### CARE considerations
- Include explicit tests preventing sensitive location inference or disclosure.
- Require governance approval for any eval fixtures that touch restricted content.

### Required approvals
- Governance review recommended for eval cases involving potentially sensitive subject matter.

## 🕰️ Version History
| Version | Date | Change | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-17 | Initial eval README | TBD |

---

### Related protocols and templates
- `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`
- `docs/templates/TEMPLATE__STORY_NODE_V3.md`
- `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md`

### Master guide pointer
- `docs/MASTER_GUIDE_v12.md`
