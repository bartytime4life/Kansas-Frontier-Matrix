---
title: ".github/ISSUE_TEMPLATE — Issue Forms for KFM"
path: ".github/ISSUE_TEMPLATE/README.md"
version: "v1.0.1"
last_updated: "2025-12-27"
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


doc_uuid: "urn:kfm:doc:github:issue-templates-readme:v1.0.1"
semantic_document_id: "kfm-github-issue-templates-readme-v1.0.1"
event_source_id: "ledger:kfm:doc:github:issue-templates-readme:v1.0.1"
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

> **Purpose:** Provide a governed “front door” for opening issues in Kansas Frontier Matrix (KFM) so every issue captures enough **stage**, **evidence**, **provenance/licensing**, and **sensitivity** context for maintainers to triage work into the correct subsystem without breaking KFM contracts.


## 📘 Overview

### Purpose

This directory standardizes how contributors and maintainers open issues in Kansas Frontier Matrix (KFM).

Issue templates exist to:
- capture the *minimum required context* to reproduce and triage problems quickly,
- route issues cleanly to the correct **pipeline stage** (ETL → catalogs → graph → API → UI → story → Focus Mode),
- reduce governance risk by prompting for provenance/licensing and preventing accidental disclosure of sensitive information.

> Design intent: collaboration templates (issue templates + PR templates) are part of the repo’s operational scaffolding. They should prompt for key “contract inputs” (stage, evidence, licensing, sensitivity) rather than attempting to define new governance policy.

### Scope

| In Scope | Out of Scope |
|---|---|
| GitHub Issue Forms (YAML) and/or Markdown issue templates stored under `.github/ISSUE_TEMPLATE/` | Implementing fixes (belongs in code/data/docs areas) |
| Guidance on what information each issue must include to be actionable | Defining new governance policies (belongs in governed policy docs; requires human review) |
| Triage routing to canonical pipeline stages | Reporting secrets, credentials, private keys, or restricted coordinates (use security process; do not post publicly) |

### Audience

- Contributors filing bugs, data requests, feature ideas, or governance questions.
- Maintainers triaging issues and mapping them to the correct pipeline stage / owners.
- Reviewers validating that proposed work stays aligned to KFM contracts (schemas, API boundaries, provenance rules).

### Definitions (link to glossary)

- Link (expected): `docs/glossary.md` (**not confirmed in repo snapshot**)
- **Pipeline stage**: the canonical segment of work a change belongs to (ETL, catalogs, graph, API, UI, story).
- **Deterministic**: same inputs + same config + same code revision ⇒ same outputs (byte-for-byte when practical).
- **Idempotent**: running the same job twice does not duplicate records or produce inconsistent results.
- **Run manifest**: a small record capturing how to reproduce a run (inputs, config, commit SHA, versions).
- **PROV bundle**: provenance artifacts describing inputs, activities, outputs, and agents.

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| System + pipeline source of truth | `docs/MASTER_GUIDE_v12.md` | KFM Core | Canonical ordering + invariants |
| v13 redesign blueprint (if adopted) | `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md` | Architecture Team | Canonical homes + migration targets |
| Full architecture vision (if adopted) | `docs/architecture/KFM_VISION_FULL_ARCHITECTURE.md` | Architecture Team | End-to-end context + extension checklist |
| Universal governed doc template | `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` | Docs Team | Default governed Markdown structure |
| Story Node template | `docs/templates/TEMPLATE__STORY_NODE_V3.md` | Narrative Curators | Narrative + evidence rules |
| API contract extension template | `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md` | API Maintainers | Contract-first API change process |
| CI/debugging map | `tests/README.md` | CI Maintainers | Where “what failed” is mapped to “where to debug” (**not confirmed in repo snapshot**) |
| Schemas registry | `schemas/` | Data/Platform | STAC/DCAT/PROV + contract schemas |
| Data lifecycle layout | `data/README.md` | Data Eng | raw/work/processed + metadata outputs (**not confirmed in repo snapshot**) |
| Security reporting process | `SECURITY.md` or `.github/SECURITY.md` | Security | Vulnerability / sensitive disclosure process (**not confirmed in repo snapshot**) |

### Definition of done (for this document)

- [ ] Front-matter complete and `path` matches file location.
- [ ] This README reflects the **actual** templates present in `.github/ISSUE_TEMPLATE/` (no drift).
- [ ] Every template (or the “blank issue” fallback) captures:
  - pipeline stage (best guess),
  - reproduction/evidence (or minimal failure context),
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
| Issue forms | `.github/ISSUE_TEMPLATE/` | Issue Forms YAML + this README |
| CI workflows | `.github/workflows/` | Validation gates + scans (**not confirmed in repo snapshot**) |
| PR template(s) | `.github/PULL_REQUEST_TEMPLATE.md` | PR intake scaffold (**not confirmed in repo snapshot**) |
| Governance | `docs/governance/` | ROOT_GOVERNANCE, ETHICS, SOVEREIGNTY |
| Documentation templates | `docs/templates/` | Universal / Story Node / API contract templates |
| Pipelines | `src/pipelines/` | ETL + transforms + catalog builders |
| Catalog outputs | `data/stac/`, `data/catalog/dcat/`, `data/prov/` | STAC/DCAT/PROV artifacts |
| Graph | `src/graph/` (+ `data/graph/` if present) | Ontology bindings + import fixtures (Neo4j ingest) |
| API boundary | `src/server/` (canonical target) | Contracted REST/GraphQL boundary (**`src/api/` treated as legacy if present**) |
| UI | `web/` | React/MapLibre UI (never reads Neo4j directly) |
| Story Nodes | `docs/reports/story_nodes/` | Governed narrative artifacts |

### Expected file tree for this sub-area

> This is the **recommended** structure. Keep it synchronized with the actual templates in-repo.

~~~text
📁 .github/
└── 🧩 ISSUE_TEMPLATE/
    ├── 📘 README.md
    ├── ⚙️ config.yml                        # optional GitHub issue forms config (may be missing)
    ├── 🐛 bug_report.yml                    # recommended (may be missing)
    ├── ✨ feature_request.yml               # recommended (may be missing)
    ├── ➕ data_addition_request.yml          # recommended (may be missing)
    ├── 🧱 graph_model_change.yml             # recommended (may be missing)
    ├── 📜 api_contract_change.yml            # recommended (may be missing)
    ├── 🗺️ ui_layer_issue.yml                 # recommended (may be missing)
    ├── 🧠 story_node_request.yml             # recommended (may be missing)
    ├── 🧪 ci_failure.yml                     # recommended (may be missing)
    └── ⚖️ governance_question.yml             # recommended (may be missing)
~~~

### Recommended template inventory (quick map)

> If a file does not exist in the directory, treat it as **planned** and do not imply it is available.

| Template | Intended use | Must capture (minimum) |
|---|---|---|
| `bug_report.yml` | Bugs anywhere in the stack | stage; repro; expected vs actual; logs/screenshots (safe); affected paths |
| `feature_request.yml` | New feature idea | stage(s) likely affected; user story; acceptance criteria; contracts impacted |
| `data_addition_request.yml` | Ingesting a new dataset | source; license; retrieval date; coverage; sensitivity; intended domain placement |
| `graph_model_change.yml` | Ontology/entity/edge changes | labels/rels; migration notes; impacts to API/UI/story; validation plan |
| `api_contract_change.yml` | Endpoint/schema change | contract diff; sample req/res; breaking-change assessment; tests required |
| `ui_layer_issue.yml` | Map layer or UX issue | repro; screenshots; API excerpt; browser/device; accessibility notes |
| `story_node_request.yml` | Narrative or evidence issue | story node ID/path; claim→evidence mapping; provenance refs |
| `ci_failure.yml` | CI gate failures | workflow/job/step; error output; changed paths; local repro if known |
| `governance_question.yml` | Governance/ethics/sovereignty concerns | concern summary; sensitivity notes; refs to governance docs |

> If you are unsure which template to use, open a blank issue and include the “must-have” fields listed under **Architecture** below.


## 🧭 Context

### Background

KFM is a governed geospatial + historical knowledge system. Work is deliberately staged so that:
- transformations are deterministic (ETL),
- metadata is schema-valid (catalog outputs: STAC/DCAT/PROV),
- semantics are explicit (graph / Neo4j),
- access is contract-first (API boundary),
- presentation is provenance-linked (UI + Story Nodes + Focus Mode).

Issue templates are the intake surface for changes and should help route requests to the correct stage with enough evidence to reproduce.

### Assumptions

- Contributors may not know which subsystem owns a problem.
- Some paths may vary by repo snapshot; where ambiguity exists, prefer canonical targets (e.g., `src/server/` for APIs).
- CI is treated as contract enforcement, not just unit tests.

### Constraints / invariants

- Canonical ordering is preserved: **ETL → Catalogs (STAC/DCAT/PROV) → Graph → API → UI → Story Nodes → Focus Mode**.
- The **UI must not connect to Neo4j directly**; all graph access is via the contracted API boundary.
- **Contracts are canonical**: schemas/specs live under `schemas/`, and API contracts live under the API boundary (target: `src/server/contracts/`).
- **No unsourced narrative**: Story Nodes intended for publication must be provenance-linked and validate.
- **No secrets in issues**: do not post credentials, private keys, or restricted coordinates in public issues.

### Open questions

| Question | Owner | Target date |
|---|---|---|
| Which issue templates are currently implemented in this repo snapshot? | TBD | TBD |
| What label taxonomy is used for pipeline stages and priorities? | TBD | TBD |
| Where should sensitive reports be routed (security process / SECURITY.md)? | TBD | TBD |
| Should blank issues be disabled via `config.yml` (and replaced with guided intake only)? | TBD | TBD |

### Future extensions

- Add a required “stage picker” + “risk/sensitivity picker” to every issue form.
- Add a dedicated “CI gate failure” form if not present.
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
  S6 --> S7["Focus Mode<br/>provenance-linked only"]
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
| Catalogs (STAC/DCAT/PROV) | Catalog validation failures; metadata drift | collection/item IDs; dataset record IDs; PROV bundle IDs; validator output |
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
- link the relevant Story Node(s) under `docs/reports/story_nodes/` (**not confirmed in repo snapshot**),
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
| v1.0.1 | 2025-12-27 | Align to canonical pipeline wording + v13 API/UI boundary invariants; standardize footer refs | TBD |


---

## Footer refs (do not remove)

- Master guide: `docs/MASTER_GUIDE_v12.md`
- v13 blueprint (if adopted): `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md`
- Full architecture vision (if adopted): `docs/architecture/KFM_VISION_FULL_ARCHITECTURE.md`
- Universal template: `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`
- Story Node template: `docs/templates/TEMPLATE__STORY_NODE_V3.md`
- API contract template: `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
