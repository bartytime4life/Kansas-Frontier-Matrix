---
title: ".github/ISSUE_TEMPLATE — Issue Forms for KFM"
path: ".github/ISSUE_TEMPLATE/README.md"
version: "v1.0.0"
last_updated: "2025-12-26"
status: "draft"
doc_kind: "Reference"
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


doc_uuid: "urn:kfm:doc:github:issue-templates-readme:v1.0.0"
semantic_document_id: "kfm-github-issue-templates-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:github:issue-templates-readme:v1.0.0"
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


# .github/ISSUE_TEMPLATE — Issue Forms for KFM

## 📘 Overview

### Purpose

This directory standardizes how contributors and maintainers open issues in Kansas Frontier Matrix (KFM).

Issue templates exist to:
- capture the *minimum required context* to reproduce and triage problems quickly,
- route issues cleanly to the correct **pipeline stage** (ETL → catalogs → graph → API → UI → story),
- reduce governance risk by prompting for provenance/licensing and preventing accidental disclosure of sensitive information.

> Design intent (reference): collaboration templates (issue templates + PR templates) are part of the repo’s operational scaffolding and should prompt for key info like source/licensing/coverage for data-related work. (Details live in higher-level governed docs.) 

### Scope

| In Scope | Out of Scope |
|---|---|
| GitHub Issue Forms (YAML) and/or Markdown issue templates stored under `.github/ISSUE_TEMPLATE/` | Implementing fixes (belongs in code/data/docs areas) |
| Guidance on what information each issue must include to be actionable | Defining new governance policies (belongs in governed policy docs; requires human review) |
| Triage routing to canonical pipeline stages | Reporting secrets, credentials, or restricted coordinates (use security process; do not post publicly) |

### Audience

- Contributors filing bugs, data requests, feature ideas, or governance questions.
- Maintainers triaging issues and mapping them to the correct pipeline stage / owners.
- Reviewers validating that proposed work stays aligned to KFM contracts (schemas, API boundaries, provenance rules).

### Definitions (link to glossary)

- Link (expected): `docs/glossary.md` (**not confirmed in repo**)
- **Pipeline stage**: the canonical segment of work a change belongs to (ETL, catalogs, graph, API, UI, story).
- **Deterministic**: same inputs + same config + same code revision ⇒ same outputs (byte-for-byte when practical).
- **Idempotent**: running the same job twice does not duplicate records or produce inconsistent results.
- **Run manifest**: a small record capturing how to reproduce a run (inputs, config, commit SHA, versions).
- **PROV bundle**: provenance artifacts describing inputs, activities, outputs, and agents.

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| System + pipeline source of truth | `docs/MASTER_GUIDE_v12.md` | KFM Core | Canonical ordering + invariants |
| Redesign blueprint (if adopted) | `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md` | KFM Core | Canonical roots + v13 readiness gates (**not confirmed in repo**) |
| Universal governed doc template | `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` | KFM Core | Default governed Markdown structure |
| Story Node template | `docs/templates/TEMPLATE__STORY_NODE_V3.md` | KFM Core | Narrative + evidence rules |
| API contract extension template | `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md` | KFM Core | Contract-first API change process |
| CI gates + validation expectations | `.github/workflows/README.md` | CI maintainers | Where “what failed” is mapped to “where to debug” (**not confirmed in repo**) |
| Schemas registry | `schemas/` | Data/Platform | STAC/DCAT/PROV + contract schemas |
| Data lifecycle layout | `data/README.md` | Data Eng | raw/work/processed + metadata outputs |

### Definition of done (for this document)

- [ ] Front-matter complete and `path` matches file location.
- [ ] This README reflects the **actual** templates present in `.github/ISSUE_TEMPLATE/` (no drift).
- [ ] Every template (or the “blank issue” fallback) captures:
  - pipeline stage,
  - reproduction/evidence,
  - expected vs actual,
  - provenance/licensing when data-related,
  - governance/sensitivity notes when relevant.
- [ ] Security note included: no secrets / no restricted coordinates in public issues.
- [ ] Version history updated when templates are added/removed/renamed.


## 🗂️ Directory Layout

### This document

- `path`: `.github/ISSUE_TEMPLATE/README.md` (must match front-matter)

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| CI workflows | `.github/workflows/` | Validation gates (markdown-lint, schema-lint, tests, scans) |
| PR template(s) | `.github/PULL_REQUEST_TEMPLATE.md` | PR intake scaffold (**not confirmed in repo**) |
| Governance | `docs/governance/` | ROOT_GOVERNANCE, ETHICS, SOVEREIGNTY |
| Documentation templates | `docs/templates/` | Universal / Story Node / API contract templates |
| Pipelines | `src/pipelines/` | ETL + transforms + catalog builders |
| Catalog outputs | `data/stac/`, `data/catalog/dcat/`, `data/prov/` | STAC/DCAT/PROV artifacts |
| Graph | `src/graph/` (+ `data/graph/` if present) | Ontology bindings + import fixtures |
| API boundary | `src/server/` | Contracted REST/GraphQL boundary (**target; not confirmed in repo**) |
| UI | `web/` | React/MapLibre UI (never reads Neo4j directly) |
| Story Nodes | `docs/reports/story_nodes/` | Governed narrative artifacts |

### Expected file tree for this sub-area

> This is the **recommended** structure. Some templates may not exist yet (**not confirmed in repo**).

~~~text
📁 .github/
└── 🧩 ISSUE_TEMPLATE/
    ├── 📘 README.md
    ├── 🐛 bug_report.yml                  # recommended (not confirmed in repo)
    ├── ✨ feature_request.yml              # recommended (not confirmed in repo)
    ├── ➕ data_addition_request.yml         # recommended (not confirmed in repo)
    ├── 🧱 graph_model_change.yml            # recommended (not confirmed in repo)
    ├── 📜 api_contract_change.yml           # recommended (not confirmed in repo)
    ├── 🗺️ ui_layer_issue.yml                # recommended (not confirmed in repo)
    ├── 🧠 story_node_request.yml            # recommended (not confirmed in repo)
    └── ⚙️ config.yml                        # optional GitHub issue forms config (not confirmed in repo)
~~~


## 🧭 Context

### Background

KFM is a governed geospatial + historical knowledge system. Work is deliberately staged so that:
- transformations are deterministic (ETL),
- metadata is schema-valid (STAC/DCAT/PROV),
- semantics are explicit (graph),
- access is contract-first (API),
- presentation is provenance-linked (UI + Story Nodes + Focus Mode).

Issue templates are the “front door” for changes and must help route requests to the correct stage with enough evidence to reproduce.

### Assumptions

- Contributors may not know which subsystem owns a problem.
- Canonical paths may differ by repo snapshot (some are “target layout”); missing roots are treated as **not confirmed in repo**.
- CI is treated as contract enforcement, not just unit tests.

### Constraints / invariants

- **ETL → STAC/DCAT/PROV → Graph → API → UI → Story Nodes → Focus Mode** is preserved.
- The **UI must not connect to Neo4j directly**; all graph access is via contracted APIs.
- Focus Mode and Story Nodes must remain **provenance-linked** (no uncited factual claims).

### Open questions

| Question | Owner | Target date |
|---|---|---|
| Which issue templates are currently implemented in this repo snapshot? | TBD | TBD |
| What label taxonomy is used for pipeline stages and priorities? | TBD | TBD |
| Where should sensitive reports be routed (SECURITY.md process)? | TBD | TBD |

### Future extensions

- Add “stage picker” + “risk/sensitivity picker” to every issue form.
- Add template(s) for “CI gate failure” to standardize failure reports.
- Add an issue template for “governance exception request” (human review required).


## 🗺️ Diagrams

### Issue intake → triage → pipeline stage

~~~mermaid
flowchart LR
  I["Issue opened<br/>.github/ISSUE_TEMPLATE"] --> T["Triage<br/>labels + stage + priority"]
  T --> S1["ETL<br/>src/pipelines + data/<domain>"]
  T --> S2["Catalogs<br/>data/stac + data/catalog/dcat + data/prov"]
  T --> S3["Graph<br/>src/graph (+ data/graph)"]
  T --> S4["API boundary<br/>src/server + contracts"]
  T --> S5["UI<br/>web/"]
  T --> S6["Story Nodes<br/>docs/reports/story_nodes/"]
~~~


## 🧪 Validation & CI/CD

### What to include when reporting a CI failure

Include:
- workflow name + job name + failing step,
- exact error output (redact secrets),
- the changed paths in your PR/branch,
- whether the failure is reproducible locally (commands if known; otherwise mark **not confirmed in repo**).

Common failure “buckets” (names are conceptual; actual job names may differ):
- markdown protocol / lint failures,
- schema validation (STAC/DCAT/PROV),
- graph integrity checks,
- API contract tests,
- UI schema/a11y checks,
- security / secret / PII scans.

### Reproduction (pattern)

~~~text
1) Identify pipeline stage from the failure context.
2) Capture minimal repro: smallest set of changed files + commands.
3) Provide evidence:
   - validator output
   - dataset/item IDs
   - run manifest / PROV bundle references (when applicable)
~~~


## 📦 Data & Metadata

### If your issue involves adding or correcting data

Provide at minimum:
- **source** (publisher/authority + citation or reference),
- **license/terms** (explicit; include restrictions if any),
- **retrieval date** (when the source was accessed),
- **spatial coverage** (bbox or narrative description; avoid restricted coordinates),
- **temporal coverage** (start/end or specific event date window),
- **intended domain placement** (e.g., `data/<domain>/{raw,work,processed}/`),
- **known sensitivity** (PII risk, culturally sensitive locations, sovereignty constraints).

If you cannot provide all fields, open the issue anyway but clearly mark unknowns as “TBD”.

### If your issue is about a processed output

Include:
- the schema/contract you believe applies (e.g., a `schemas/...` reference),
- sample record(s) (small, non-sensitive),
- the expected normalization rules (units, CRS, time zone conventions),
- the stable identifier key(s) expected to remain consistent between runs.


## 🌐 STAC, DCAT & PROV Alignment

### STAC

When relevant, include:
- Collection identifier(s) involved (path under `data/stac/collections/**`),
- Item identifier(s) involved (path under `data/stac/items/**`),
- asset key(s) and the referenced artifact path(s),
- the validator error output (schema + any KFM profile constraints).

### DCAT

When relevant, include:
- dataset record path(s) under `data/catalog/dcat/**`,
- license consistency concerns (STAC vs DCAT mismatch),
- publisher/contact/keywords concerns (if required by adopted profile).

### PROV-O

When relevant, include:
- PROV bundle path(s) under `data/prov/**`,
- the activity/run identifier(s),
- which raw/work/processed artifacts should be linked by provenance.


## 🧱 Architecture

### Use this stage-to-evidence matrix when opening issues

| Stage | When to use | Include these fields |
|---|---|---|
| ETL | Ingest/transforms, raw→processed issues | source + license + retrieval date; input sample; expected output; run manifest (if available) |
| STAC/DCAT/PROV | Catalog validation failures; metadata drift | collection/item IDs; dataset record IDs; PROV bundle IDs; validator output |
| Graph | Ontology/entity/edge modeling issues | label/relationship expectations; entity IDs; import artifacts; migration notes |
| API | Contract/endpoint behavior or redaction | endpoint + contract ref; request/response samples; breaking-change assessment |
| UI | Layer rendering, time slider, interaction bugs | reproduction steps; screenshots if safe; API response excerpt; browser/device info |
| Story Nodes | Narrative evidence or citation issues | Story Node doc ID/path; claim→evidence mapping; provenance refs |

### Minimal “must-have” fields for every issue (if templates are missing)

- What happened (actual)
- What you expected
- Reproduction steps / evidence
- Pipeline stage (best guess)
- Affected paths (best guess)
- Governance note (any sensitivity concerns?)


## 🧠 Story Node & Focus Mode Integration

If the issue relates to narrative or Focus Mode:
- link the relevant Story Node(s) under `docs/reports/story_nodes/` (**not confirmed in repo**),
- list each claim that is in question,
- provide the dataset/document IDs that should support each claim (STAC/DCAT/PROV preferred),
- do **not** introduce new factual claims without citations/evidence identifiers.


## ⚖ FAIR+CARE & Governance

### Do not post in public issues

- secrets, tokens, credentials, private keys,
- restricted coordinates or culturally sensitive site locations (use generalized descriptions),
- personal data or anything that could identify private individuals.

### CARE / sovereignty considerations

- If the issue involves Indigenous knowledge, culturally sensitive places, or restricted locations:
  - flag it clearly in the issue,
  - prefer coarse/generalized geography,
  - reference `docs/governance/SOVEREIGNTY.md` for handling rules.

### AI usage constraints

- Allowed uses for issue content: summarization, structure extraction, translation, keyword indexing.
- Prohibited: generating new policy or inferring sensitive locations from data.


## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-26 | Initial README scaffold for `.github/ISSUE_TEMPLATE/` | TBD |


---

Footer refs (do not remove)

- Master guide: `docs/MASTER_GUIDE_v12.md`
- Template: `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`
- Templates: `docs/templates/`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
