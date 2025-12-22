---
title: "KFM AI Fairness Validators — README"
path: "tools/ai/fairness/validators/README.md"
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

doc_uuid: "urn:kfm:doc:tools:ai:fairness:validators:readme:v1.0.0"
semantic_document_id: "kfm-tools-ai-fairness-validators-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:tools:ai:fairness:validators:readme:v1.0.0"
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

# KFM AI Fairness Validators

## 📘 Overview

### Purpose
- Provide **deterministic, auditable fairness checks** (“validators”) for AI-assisted artifacts produced in KFM workflows (e.g., summaries, extracted entities, draft Story Nodes).
- Emit **machine-readable validation reports** suitable for CI gates and governance review (warn/error semantics).

### Scope

| In Scope | Out of Scope |
|---|---|
| Deterministic scans (lexicon/rules), schema checks, structural completeness checks, “must-cite” enforcement, risk flagging. | Writing or rewriting narrative; generating policy; inferring sensitive locations; making final ethical determinations without review. |

### Audience
- **Primary:** contributors implementing or updating validators under `tools/ai/fairness/validators/`.
- **Secondary:** reviewers (governance/ethics), pipeline owners integrating validation gates, Story Node editors responding to validator findings.

### Definitions
- **Validator:** a deterministic function/module that inspects an artifact and returns a structured list of findings (severity + remediation).
- **Artifact:** any AI-adjacent output subject to checks (text, JSON, metadata bundle, Story Node draft).
- **Finding / Issue:** a single flagged item (e.g., biased framing, missing citations, unsafe phrasing).
- **Gate:** an enforcement point (CI, pre-publish, pre-merge) that fails builds/releases on `error` findings.

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Fairness overview | `tools/ai/fairness/README.md` | AI Tooling | Parent scope + goals. |
| Provenance tooling | `tools/ai/provenance/README.md` | AI Tooling | Evidence + traceability expectations. |
| Master pipeline invariants | `docs/MASTER_GUIDE_v12.md` | KFM Core | Canonical pipeline + “no unsourced narrative” invariant. |
| Governance + ethics | `docs/governance/*` | Governance | Review triggers, CARE/sovereignty rules. |

### Definition of done (for this document)
- [ ] Front-matter complete + valid
- [ ] Validator interface + reporting expectations documented
- [ ] Governance + CARE/sovereignty considerations explicitly stated
- [ ] Clear “how to add a validator” checklist

---

## 🗂️ Directory Layout

### This document
- `path`: `tools/ai/fairness/validators/README.md`

### Related repository paths
| Area | Path | What lives here |
|---|---|---|
| Fairness tooling | `tools/ai/fairness/` | Fairness scope, reports, shared utilities |
| Fairness validators | `tools/ai/fairness/validators/` | Individual validator modules + registry |
| Provenance tooling | `tools/ai/provenance/` | PROV/STAC/DCAT pointers and lineage helpers |
| Schemas | `schemas/` | JSON Schemas for validator reports (if/when added) |
| Tests | `tests/` | Golden tests for validator determinism |

### Expected file tree for this sub-area
> Note: files other than this README are **proposed structure** (not confirmed in repo) and should only be created if/when implementing the validator runner.

~~~text
📁 tools/
└── 📁 ai/
    └── 📁 fairness/
        └── 📁 validators/
            ├── 📄 README.md
            ├── 📄 registry.py                 # (proposed) validator discovery/registry
            ├── 📁 rules/                      # (proposed) rule-based validators
            │   ├── 📄 language_bias.py
            │   ├── 📄 citation_requirements.py
            │   └── 📄 sensitive_terms.py
            ├── 📁 schemas/                    # (proposed) report schema(s)
            │   └── 📄 fairness_validation_report.schema.json
            └── 📁 fixtures/                   # (proposed) golden test artifacts
                └── 📄 sample_story_node.md
~~~

---

## 🧭 Context

### Where validators sit in the KFM flow
Validators are intended to run **as gates** around AI-assisted transformations, so that:
- artifacts can be blocked on **hard errors** (e.g., unsafe language, missing “must have” citations),
- artifacts can be flagged with **warnings** for human review (e.g., framing risks, ambiguous attributions),
- all results are **traceable** (artifact ID + run ID + rule IDs).

They must preserve KFM architecture invariants:
- **No unsourced narrative** in user-facing contexts (validators should help detect missing evidence links).
- **Provenance-first outputs** (reports should carry pointers to dataset/document IDs and run IDs where applicable).

### What “fairness” means operationally here
This folder is for checks that reduce risks of:
- **Representational harm** (demeaning framing, stereotyping, othering language, slurs).
- **Attribution harm** (claims about communities without evidence, quoting or paraphrasing without citations).
- **Context collapse** (summaries that erase agency, conflate groups, or omit historically relevant qualifiers).

> Governance note: validators are *assistive controls*. They do not replace expert/human review.

---

## 🗺️ Diagrams

~~~mermaid
flowchart LR
  A[AI-assisted artifact] --> B[Fairness validator runner]
  B --> C{Findings?}
  C -->|errors| D[Fail gate / block publish]
  C -->|warnings| E[Allow w/ review required]
  C -->|none| F[Pass]
  D --> G[Human remediation + re-run]
  E --> G
  G --> B
~~~

---

## 📦 Data & Metadata

### Validator reporting format
A validator should emit a structured report that can be:
- stored as a build artifact,
- diffed in PRs,
- aggregated across runs.

**Proposed minimal report shape (not confirmed in repo):**

~~~json
{
  "tool": "kfm.tools.ai.fairness.validators",
  "tool_version": "v1",
  "run_id": "prov:activity:<id-or-run-hash>",
  "artifact": {
    "artifact_id": "kfm:artifact:<id>",
    "artifact_type": "story_node_draft|summary|entities_json",
    "path": "docs/reports/story_nodes/draft/<file>"
  },
  "findings": [
    {
      "validator_id": "kfm.fairness.language_bias.v1",
      "severity": "error|warn|info",
      "code": "FAIRNESS_LANGUAGE_001",
      "message": "Potential biased framing detected…",
      "location": { "line_start": 12, "line_end": 14 },
      "evidence_refs": {
        "stac_item_ids": [],
        "dcat_dataset_ids": [],
        "prov_activity_ids": []
      },
      "remediation": "Rewrite to attribute claims and add citations…"
    }
  ]
}
~~~

---

## 🌐 STAC, DCAT & PROV Alignment

Even when validating *text*, findings should remain linkable to KFM evidence conventions:

- **STAC:** if an artifact references media/assets, findings should prefer referencing **STAC Item IDs** rather than raw URLs.
- **DCAT:** if an artifact summarizes a dataset, findings should prefer referencing **DCAT dataset identifiers** as the dataset “anchor.”
- **PROV:** every validator run should be attributable to a **PROV activity/run ID** (even if only a local run hash), so reports can be audited and reproduced.

> If a validator needs additional context from the graph, it must go through the **API boundary** (do not read Neo4j directly from the UI/tooling context).

---

## 🧱 Architecture

### Validator interface contract
A validator should be written so it can be executed:
- standalone (developer runs locally),
- in CI (non-interactive),
- as a pre-publish gate (Story Node / Focus Mode pipeline).

**Recommended interface (not confirmed in repo):**
- `validator_id: str` (stable, versioned)
- `validate(artifact, context) -> report/findings`
- deterministic behavior (no remote calls; pinned resources; stable lexicons)

### Determinism requirements
- No network calls (unless explicitly approved and pinned; default: offline).
- If using models: version-pin and record in the report metadata; prefer rule-based checks.
- Stable sorting of findings and stable IDs for reproducible diffs.

---

## ✅ Validation

### How to add a new validator
1. Create a new validator module under `tools/ai/fairness/validators/` (or `rules/` if that structure exists).
2. Assign a **stable, versioned** `validator_id`.
3. Add golden fixtures + tests to ensure deterministic outputs.
4. Register it in the validator registry (if present).
5. Update:
   - `tools/ai/fairness/README.md` (overview list)
   - any CI hooks / pipeline docs that invoke validators

### How to run validators
Not confirmed in repo. Suggested patterns (choose one and document in the parent fairness README):
- `python -m tools.ai.fairness.validators <artifact_path>`
- `make fairness-validate ARTI=<path>`
- CI job that runs validator runner and uploads JSON reports

---

## 🔐 Security, Privacy, and Misuse Resistance

- Do not log or persist unnecessary sensitive text.
- Findings should avoid repeating harmful content verbatim unless required for debugging; prefer spans/line references.
- Never attempt to infer sensitive locations or re-identify individuals.
- Treat validator reports as potentially sensitive if they include excerpts; prefer redacted reporting.

---

## ⚖ FAIR+CARE & Governance

### Review gates
Changes that may require review (confirm exact criteria in governance docs):
- Adding/removing a validator that blocks publication (new “gate” behavior).
- Changing severity thresholds (e.g., warning → error) that affects what can ship.
- Adding rules that specifically impact Indigenous or culturally sensitive content.

### CARE / sovereignty considerations
Validators should be designed to:
- **flag** likely sovereignty risks (e.g., overly precise sensitive locations) rather than “fixing” them automatically.
- avoid extracting/deriving new sensitive facts from partial data.

### AI usage constraints
- Validators must not generate policy or new narrative content.
- If a validator uses ML models at all, document:
  - model name/version
  - input/output constraints
  - failure modes
  - how it avoids hallucinations and sensitive inference

---

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-22 | Initial README for fairness validators submodule | TBD |

---

Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
